from sqlalchemy.orm import Session
from .models import Project
import logging

logger = logging.getLogger("durozen.seed")

DEFAULT_PROJECTS = [
    {
        "id": "makeover",
        "name": "Makeover Studio",
        "category": "Beauty",
        "tagline": "Luxury makeup, beauty styling & personal makeover destination",
        "description": "A chic, high-fashion makeover and beauty consultation platform showcasing artist portfolios, transformation lookbooks, and customized packages.",
        "url": "https://makeeeover.netlify.app",
        "accent_color": "#FACC15",
        "accent_badge": "Beauty",
        "year": "2026",
        "tags": ["Beauty Styling", "Lookbook", "Personal Makeover", "Netlify Live"],
        "client": "Makeover Studio",
        "highlights": ["Transformation Gallery", "Artist Booking", "Custom Packages"],
        "domain": "makeeeover.netlify.app"
    },
    {
        "id": "eye-hospital",
        "name": "Eye Hospital",
        "category": "Healthcare",
        "tagline": "Advanced ophthalmology clinic, laser vision & surgical care",
        "description": "An institutional healthcare portal for eye care, cataract surgery, and retinal treatments featuring specialist directories and online appointment booking.",
        "url": "https://eyehospital1.netlify.app",
        "accent_color": "#22C55E",
        "accent_badge": "Healthcare",
        "year": "2026",
        "tags": ["Ophthalmology", "Doctor Directory", "Appointment Booking", "Netlify Live"],
        "client": "Apex Eye Hospital",
        "highlights": ["Specialist Profiles", "Online Appointment Booking", "Surgical Guides"],
        "domain": "eyehospital1.netlify.app"
    },
    {
        "id": "salon",
        "name": "Salon Studio",
        "category": "Beauty",
        "tagline": "Premium hair styling, spa therapies & grooming experience",
        "description": "A contemporary salon web experience with service menus, pricing tiers, hair stylist selection, and automated slot reservations.",
        "url": "https://salonn1.netlify.app",
        "accent_color": "#E52521",
        "accent_badge": "Beauty",
        "year": "2026",
        "tags": ["Hair & Spa", "Service Menu", "Slot Booking", "Netlify Live"],
        "client": "Urban Salon Studio",
        "highlights": ["Slot Reservation", "Tiered Service Menu", "Stylist Portfolio"],
        "domain": "salonn1.netlify.app"
    },
    {
        "id": "mmr-motor",
        "name": "MMR Motor",
        "category": "Automotive",
        "tagline": "Modern two-wheeler sales, maintenance & spare parts portal",
        "description": "A full-service two-wheeler automotive platform featuring interactive bike models, service booking schedules, and genuine spare parts catalog.",
        "url": "https://mmrmotor.netlify.app",
        "accent_color": "#E52521",
        "accent_badge": "Automotive",
        "year": "2026",
        "tags": ["Automotive", "Bike Service", "Parts Catalog", "Netlify Live"],
        "client": "MMR Motor Hub",
        "highlights": ["Instant Service Booking", "Multi-Brand Catalog", "Mobile First"],
        "domain": "mmrmotor.netlify.app"
    },
    {
        "id": "scootyy",
        "name": "Scootyy",
        "category": "Automotive",
        "tagline": "Smart electric scooter rental, test drives & urban mobility",
        "description": "An eco-friendly electric scooter showcase featuring battery specs, range estimators, online test drive reservations, and urban dealership locators.",
        "url": "https://scootyy.netlify.app",
        "accent_color": "#2563EB",
        "accent_badge": "Automotive",
        "year": "2026",
        "tags": ["EV Mobility", "Scooter Rental", "Test Drive UI", "Netlify Live"],
        "client": "Scootyy Urban Mobility",
        "highlights": ["Range Calculator", "Test Ride Scheduler", "Interactive Fleet"],
        "domain": "scootyy.netlify.app"
    },
    {
        "id": "bridal",
        "name": "Bridal Makeover",
        "category": "Beauty",
        "tagline": "Bespoke bridal makeover, couture beauty & wedding glam packages",
        "description": "An ethereal bridal platform highlighting wedding day looks, mehendi and reception styling packages, and client testimonial showcases.",
        "url": "https://bridall.netlify.app",
        "accent_color": "#FACC15",
        "accent_badge": "Beauty",
        "year": "2026",
        "tags": ["Bridal Glam", "Couture Styling", "Wedding Lookbook", "Netlify Live"],
        "client": "Bridal Makeover Atelier",
        "highlights": ["Wedding Day Lookbook", "Bridal Consultations", "Package Customizer"],
        "domain": "bridall.netlify.app"
    },
    {
        "id": "eye-care",
        "name": "Eye Care Center",
        "category": "Healthcare",
        "tagline": "Comprehensive optical diagnostics, contact lenses & eyewear",
        "description": "A modern vision care and optical dispensary website providing eye examinations, designer frames gallery, and prescription renewal support.",
        "url": "https://eyecareee.netlify.app",
        "accent_color": "#22C55E",
        "accent_badge": "Healthcare",
        "year": "2026",
        "tags": ["Optometry", "Eyewear Gallery", "Vision Check", "Netlify Live"],
        "client": "Vision Eye Care Center",
        "highlights": ["Vision Check Guidance", "Eyewear Catalog", "Prescription Care"],
        "domain": "eyecareee.netlify.app"
    },
    {
        "id": "nurserie-plant",
        "name": "Nurserie Plant",
        "category": "Lifestyle",
        "tagline": "Botanical nursery, exotic indoor plants & landscape greens",
        "description": "A vibrant gardening and botanical nursery website showcasing rare indoor houseplants, bonsai trees, organic soils, and plant care instructions.",
        "url": "https://nurserieplant.netlify.app/",
        "accent_color": "#22C55E",
        "accent_badge": "Lifestyle",
        "year": "2026",
        "tags": ["Botanical Nursery", "Houseplants", "Garden Greens", "Netlify Live"],
        "client": "Nurserie Botanical Greens",
        "highlights": ["Plant Care Guides", "Rare Species Catalog", "Gardening Supplies"],
        "domain": "nurserieplant.netlify.app"
    },
    {
        "id": "resort",
        "name": "Resort Getaway",
        "category": "Hospitality",
        "tagline": "Luxury vacation retreat, villas, private dining & wellness spa",
        "description": "An immersive hospitality experience presenting luxury villa accommodations, beachfront suites, dining menus, and direct online suite booking.",
        "url": "https://resortt2.netlify.app/",
        "accent_color": "#2563EB",
        "accent_badge": "Hospitality",
        "year": "2026",
        "tags": ["Luxury Resort", "Villa Booking", "Dining & Spa", "Netlify Live"],
        "client": "Azure Bay Luxury Resort",
        "highlights": ["Direct Room Booking", "Virtual Villa Tour", "Spa Packages"],
        "domain": "resortt2.netlify.app"
    },
    {
        "id": "mmr-motors",
        "name": "MMR Motors",
        "category": "Automotive",
        "tagline": "Premium pre-owned cars, vehicle trade-ins & certified auto dealership",
        "description": "A comprehensive automotive dealership platform with certified pre-owned vehicle listings, EMI financing calculators, and instant test drive bookings.",
        "url": "https://mmrmotors.uk",
        "accent_color": "#E52521",
        "accent_badge": "Automotive",
        "year": "2026",
        "tags": ["Pre-Owned Cars", "Auto Dealership", "EMI Calculator", "Netlify Live"],
        "client": "MMR Motors Dealership",
        "highlights": ["Certified Inventory", "Auto Financing Calculator", "Instant Vehicle Inspection"],
        "domain": "mmrmotors.uk",
        "image_url": "/assets/projects/mmrmotors_preview.jpg"
    }
]

def seed_default_projects(db: Session, force: bool = False) -> int:
    """Seed the default 10 projects if table is empty or force=True."""
    count = db.query(Project).count()
    if count > 0 and not force:
        return 0
    
    added = 0
    for item in DEFAULT_PROJECTS:
        existing = db.query(Project).filter(Project.id == item["id"]).first()
        if existing and not force:
            continue
        
        if existing and force:
            for k, v in item.items():
                setattr(existing, k, v)
        else:
            proj = Project(**item)
            db.add(proj)
            added += 1
            
    db.commit()
    logger.info(f"Seeded {added} demo projects into database.")
    return added

