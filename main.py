from fastapi import FastAPI

# Create a FastAPI instance
app = FastAPI()

# Define a GET endpoint at the root URL
@app.get("/")
async def read_root():
    # Return a JSON response with the message "Hello World"
    return {"message": "Hello World"}
