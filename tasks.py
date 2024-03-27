from celery import Celery
from PIL import Image, ImageOps,ImageFilter
from fastapi import HTTPException
from dotenv import load_dotenv
import os
load_dotenv()



app = Celery('tasks', broker=os.getenv("BROKER_URL"),backend=os.getenv("BACKEND_URL"))

@app.task
def process_image(file_path:str,output_path:str,transformation:str):
    try:
        with Image.open(file_path) as img:
            if transformation == "resize":
                img.thumbnail((128,128))
            elif transformation == "rotate":
                img = img.rotate(90)
            elif transformation == "flip":
                img = img.transpose(Image.FLIP_LEFT_RIGHT)
            elif transformation == "grayscale":
                img = img.convert('L')
            elif transformation == "invert":
                img = ImageOps.invert(img) 
            elif transformation == "blur":
                img = img.filter(ImageFilter.BLUR)
                
            img.save(output_path)
    except Exception as e:
        raise RuntimeError(str(e))
    
    
    
            
                
            
        










