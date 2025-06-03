from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = [
    "https://hamgarian.github.io/PyActionAPI",
]

# Add CORS middleware to the app
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,            # Allowed origins
    allow_credentials=True,           # Allow cookies and credentials
    allow_methods=["*"],              # Allow all HTTP methods (GET, POST, etc.)
    allow_headers=["*"],              # Allow all headers
)


@app.on_event("startup")
def on_startup():
    print("running on startup")

@app.get("/")
def read_root():
    return {"message": "Hello from FastAPI via Cloudflared without token!"}
