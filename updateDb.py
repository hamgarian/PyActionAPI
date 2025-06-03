import firebase_admin
from firebase_admin import credentials, firestore
from dotenv import load_dotenv
import os

def update_firestore(tunnel_url: str):
    # Load environment variables from .env file
    load_dotenv()

    # Initialize Firebase Admin with Firestore
    cred = credentials.Certificate('serviceAccountKey.json')
    # Initialize app only once to avoid errors if called multiple times
    if not firebase_admin._apps:
        firebase_admin.initialize_app(cred)

    # Create Firestore client
    db = firestore.client()


    # Store the cloudflared tunnel URL in Firestore
    url_ref = db.collection('config').document('cloudflared')
    url_ref.set({
        'tunnel_url': tunnel_url
    }, merge=True)

if __name__ == "__main__":
    # Example usage: pass the tunnel URL as an environment variable or hardcoded for testing
    tunnel_url = os.getenv('CLOUDFLARED_TUNNEL_URL', 'https://example.trycloudflare.com')
    update_firestore(tunnel_url)
    print("Firestore updated successfully with tunnel URL:", tunnel_url)
