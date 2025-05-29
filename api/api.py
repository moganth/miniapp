from fastapi import APIRouter, UploadFile, File, HTTPException
import os
from starlette.responses import FileResponse

from services.service import save_file_info, get_all_files, get_file_path_by_name

router = APIRouter()

# Use a writable directory instead of relative "uploads" path
UPLOAD_FOLDER = "/tmp/uploads"

# Add error handling for directory creation
try:
    os.makedirs(UPLOAD_FOLDER, exist_ok=True)
except OSError as e:
    if e.errno == 30:  # Read-only file system
        # Fallback to user's home directory
        UPLOAD_FOLDER = os.path.expanduser("~/plugin_uploads")
        os.makedirs(UPLOAD_FOLDER, exist_ok=True)
        print(f"Warning: Using fallback upload directory: {UPLOAD_FOLDER}")
    else:
        raise


@router.post("/file/{name}")
async def upload_file(name: str, file: UploadFile = File(...)):
    file_location = f"{UPLOAD_FOLDER}/{file.filename}"

    with open(file_location, "wb") as buffer:
        buffer.write(file.file.read())

    save_file_info(name, file.filename, file_location)

    return {"message": "File uploaded successfully", "filename": file.filename, "path": file_location}


@router.get("/files")
async def get_files():
    return get_all_files()


@router.get("/download/{name}")
async def download_file(name: str):
    file_path = get_file_path_by_name(name)

    if not file_path or not os.path.exists(file_path):
        raise HTTPException(status_code=404, detail="File not found")

    return FileResponse(file_path, filename=os.path.basename(file_path))
