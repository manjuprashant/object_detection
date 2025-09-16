from fastapi import FastAPI, File, UploadFile
import requests
import shutil

app = FastAPI()

AI_BACKEND_URL = "http://ai_backend:5000/detect"

@app.post("/upload-image")
async def upload_image(file: UploadFile = File(...)):
    file_location = f"/tmp/{file.filename}"
    with open(file_location, "wb") as f:
        shutil.copyfileobj(file.file, f)
    with open(file_location, "rb") as f:
        files = {"file": (file.filename, f, "multipart/form-data")}
        response = requests.post(AI_BACKEND_URL, files=files)
    return response.json()
