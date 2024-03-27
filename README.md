# Simple Image Processor With Celery, Redis, and FastAPI

This project is a simple image processing application built with Celery, Redis, and FastAPI. It allows users to upload images, apply various transformations asynchronously using Celery workers, and retrieve the processed images.

## Setup Instructions

1. **Activate Virtual Environment**

   Activate your virtual environment to isolate dependencies:
   
   ```bash
   source venv/bin/activate  # For Unix/Linux
   .\venv\Scripts\activate   # For Windows
   ```
2. **Install Requirements**
    ```bash
    pip install -r requirements.txt
    ```
3. **Configure Redis**
    - Rename .env.env file to .env and replace it with your Redis URL/paths or remote Redis configuration.
    - For instructions on how to install Redis on your local computer, refer to Redis Documentation
    - You can also use Redis with Docker. Check out Redis Docker Hub for more details.
4. **Run FastAPI Server**
    ```bash
    uvicorn main:app
    ```

5. **Run Celery Worker**
    ```bash
    celery -A tasks worker --loglevel=info
    ```
    - Add the "-P solo" flag if you're running the Windows version of Redis.


## Documentation is at http://127.0.0.1:8000/docs






