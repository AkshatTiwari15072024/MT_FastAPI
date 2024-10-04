
from fastapi import FastAPI
from .routes import router

# Create FastAPI instance
app = FastAPI()

@app.get("/")
async def read_root():
    """
    Root endpoint for the API.
    
    Returns:
        dict: Welcome message.
    """
    return {"message": "Welcome to the FastAPI CRUD API!"}

# Include product routes with a prefix
app.include_router(router, prefix="/api")

