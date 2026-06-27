from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return {"message": "Hello, World"}


@app.get("/about")
def read_about():
    return {"about": "This is a sample FastAPI application."}


@app.get("/status")
def read_status():
    return {"status": "Running"}
