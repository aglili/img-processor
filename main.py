from fastapi import FastAPI,UploadFile,File,HTTPException,status
from pydantic import BaseModel
from tasks import process_image
from starlette.responses import FileResponse
import os,uuid


app = FastAPI()


class Transformation(BaseModel):
    effect:str
    
    

UPLOAD_DIR = "temp"
OUTPUT_DIR = "output"

# Create the upload directory if it doesn't exist
os.makedirs(UPLOAD_DIR, exist_ok=True)
os.makedirs(OUTPUT_DIR, exist_ok=True)
    
    
    
    
@app.post("/upload")
async def upload_image(file:UploadFile = File(...)):
    # check file is an image 
    extension = os.path.splitext(file.filename)[1]
    if extension not in [".jpg",".png",".jpeg"]:
        raise HTTPException(status_code=400,detail="File must be an image")
    
    temp_filepath =  f"temp/{uuid.uuid4()}{extension}"
    
    with open(temp_filepath,"wb") as buffer:
        buffer.write(await file.read())       
        
    return {"filename":file.filename,"filepath":temp_filepath}


@app.post("/transform")
async def transform_image(transformation:Transformation,file_path:str):
    output_path = f"output/{uuid.uuid4()}.png"
    task = process_image.delay(file_path,output_path,transformation.effect)
    
    return {
        "task_id":task.id,
        "output_path":output_path,
        "status":"processing"
    }
    
    
@app.get("/status/{task_id}")
async def task_status(task_id:str):
    task = process_image.AsyncResult(task_id)
    
    if task.state == "SUCCESS":
        return {"status":task.state,"output_path":task.result}
    elif task.state == "FAILURE":
        return {"status":task.state,"error":task.result}
    else:
        return {"status":task.state}
    
    
    
@app.get("/download/{file_path}")
def download_processed_image(filename:str):
    file_path = "output/"+filename
    
    if os.path.exists(file_path):
        return FileResponse(file_path,media_type="image/png",filename=filename)
    else:
        raise HTTPException(status_code=404,detail="File not found")
    
    
    
    
    
   
    
    
        
    
    
    





    
    




