from fastapi import FastAPI

posts = {"Title":"Ehsas Lab","Descripation":"Like minded people"}

app = FastAPI()
@app.get("/")
def home():
    return{"Message":"Hi Sir!"}
@app.get("/posts")
def get_posts():
    return posts