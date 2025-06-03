import firebase_admin
from firebase_admin import credentials, firestore
from dotenv import load_dotenv
import os

def update_firestore():
    # Load environment variables from .env file
    load_dotenv()

    # Initialize Firebase Admin with Firestore
    cred = credentials.Certificate('serviceAccountKey.json')
    firebase_admin.initialize_app(cred)

    # Create Firestore client
    db = firestore.client()

    # Add a simple document to a 'test' collection
    test_ref = db.collection('test').document('main')
    test_ref.set({
        'text_input': 'This is a sample text'  # Replace with your desired text
    })

    # Add or update nested fields in a subcollection or as nested fields
    test_ref.update({
        'subnode.nested_text': 'Nested text example'
    })

    # Update a specific user document
    user_ref = db.collection('users').document('user123')
    user_ref.set({
        'name': 'John Doe',
        'age': 30,
        'comment': 'Additional text input'
    }, merge=True)

if __name__ == "__main__":
    update_firestore()
    print("Firestore updated successfully.")
