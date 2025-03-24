from fastapi import APIRouter, UploadFile, File, HTTPException
import os
from starlette.responses import FileResponse

from services.service import save_file_info, get_all_files, get_file_path_by_name

router = APIRouter()

UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)


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
