from fastapi import FastAPI

app = FastAPI()


@app.get("/items/{item_id}")
def read_item(item_id: int):
    return {"item_id": item_id}


@app.get("/items/{item_id}/details")
def read_item_details(item_id: int):
    return {"item_id": item_id, "details": "This is the item details."}


@app.get("/users/{username}")
def read_user(username: str):
    return {"username": username}
