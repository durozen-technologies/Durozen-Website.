import uvicorn
import os
import sys

# Ensure backend directory is in python sys.path
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
if BASE_DIR not in sys.path:
    sys.path.insert(0, BASE_DIR)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8000))
    print(f"\n=======================================================")
    print(f"  Starting DUROZEN FastAPI Server on http://localhost:{port}")
    print(f"  Interactive API Docs: http://localhost:{port}/docs")
    print(f"=======================================================\n")
    app_dir = os.path.join(BASE_DIR, "app")
    uvicorn.run("app.main:app", host="0.0.0.0", port=port, reload=True, reload_dirs=[app_dir])

