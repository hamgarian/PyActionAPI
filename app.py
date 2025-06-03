from fastapi import FastAPI
from updateDb import update_firestore

app = FastAPI()
update_firestore()

@app.get("/")
def read_root():
    return {"message": "Hello from FastAPI via Cloudflared without token!"}
