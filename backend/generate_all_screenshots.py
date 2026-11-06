import os
import sys
import asyncio
import logging
import dotenv

# Load environment
BACKEND_DIR = os.path.dirname(os.path.abspath(__file__))
dotenv.load_dotenv(os.path.join(BACKEND_DIR, ".env"))

if BACKEND_DIR not in sys.path:
    sys.path.insert(0, BACKEND_DIR)

from app.database import SessionLocal
from app.models import Project
from app.screenshot_service import capture_website_screenshot

logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s")
logger = logging.getLogger("generate_screenshots")

# All known projects including database and static defaults
FALLBACK_PROJECTS = [
    {"id": "restaurant", "name": "Restaurant", "url": "https://rrhotell.netlify.app"},
    {"id": "hospital", "name": "Hospital", "url": "https://carehosptial.netlify.app"},
    {"id": "bridal-makeover", "name": "Bridal Makeover", "url": "https://bridall.netlify.app"},
    {"id": "bridal", "name": "Bridal Makeover", "url": "https://bridall.netlify.app"},
    {"id": "eye-care", "name": "Eye Care Center", "url": "https://eyecareee.netlify.app"},
    {"id": "resort", "name": "Resort Getaway", "url": "https://resortt2.netlify.app"},
    {"id": "mmr-motors", "name": "MMR Motors", "url": "https://mmrmotors.uk"},
    {"id": "mmr-motor", "name": "MMR Motor", "url": "https://mmrmotor.netlify.app"},
    {"id": "scootyy", "name": "Scootyy", "url": "https://scootyy.netlify.app"},
    {"id": "salon", "name": "Salon Studio", "url": "https://salonn1.netlify.app"},
    {"id": "nurserie-plant", "name": "Nurserie Plant", "url": "https://nurserieplant.netlify.app"},
    {"id": "makeover", "name": "Makeover Studio", "url": "https://makeeeover.netlify.app"},
    {"id": "eye-hospital", "name": "Eye Hospital", "url": "https://eyehospital1.netlify.app"},
]

async def process_all_screenshots():
    logger.info("Connecting to database...")
    db = SessionLocal()
    
    # 1. Fetch DB projects
    db_projects = []
    try:
        db_projects = db.query(Project).all()
        logger.info(f"Retrieved {len(db_projects)} projects from database.")
    except Exception as e:
        logger.error(f"Error querying database: {e}")

    # Build unique map of project items by id
    project_map = {}
    for p in db_projects:
        project_map[p.id] = {
            "id": p.id,
            "name": p.name,
            "url": p.url,
            "db_instance": p
        }

    # Add fallback projects if not present in DB
    for fb in FALLBACK_PROJECTS:
        if fb["id"] not in project_map:
            project_map[fb["id"]] = {
                "id": fb["id"],
                "name": fb["name"],
                "url": fb["url"],
                "db_instance": None
            }

    logger.info(f"Total projects to capture screenshots for: {len(project_map)}")

    success_count = 0
    failure_count = 0

    for pid, pdata in project_map.items():
        name = pdata["name"]
        url = pdata["url"]
        logger.info(f"\n---> Capturing [{pid}] '{name}' ({url})...")

        try:
            filename = f"{pid}.jpg"
            saved_url = await capture_website_screenshot(url, filename)

            if saved_url:
                success_count += 1
                logger.info(f"SUCCESS: Captured {name} -> {saved_url}")

                # Update database record if exists
                if pdata["db_instance"]:
                    pdata["db_instance"].image_url = saved_url
                    try:
                        db.commit()
                        logger.info(f"DB Updated: Project '{pid}' image_url = '{saved_url}'")
                    except Exception as db_err:
                        logger.error(f"Failed to commit DB update for {pid}: {db_err}")
                        db.rollback()
            else:
                failure_count += 1
                logger.warning(f"FAILED to capture screenshot for '{name}' ({url})")

        except Exception as e:
            failure_count += 1
            logger.error(f"Exception capturing screenshot for {name}: {e}")

    db.close()
    logger.info("\n=======================================================")
    logger.info(f"SCREENSHOT GENERATION COMPLETED!")
    logger.info(f"  Success: {success_count}")
    logger.info(f"  Failed:  {failure_count}")
    logger.info("=======================================================\n")

if __name__ == "__main__":
    asyncio.run(process_all_screenshots())

