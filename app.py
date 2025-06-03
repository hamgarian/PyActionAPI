from fastapi import FastAPI
from updateDb import update_db

app = FastAPI()
update_db()

@app.get("/")
def read_root():
    return {"message": "Hello from FastAPI via Cloudflared without token!"}
