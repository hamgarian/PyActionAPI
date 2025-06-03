import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
from dotenv import load_dotenv
import os

def update_db():
    # Load environment variables from .env file
    load_dotenv()

    # Initialize the app with the service account key
    cred = credentials.Certificate('serviceAccountKey.json')
    firebase_admin.initialize_app(cred, {
        'databaseURL': os.getenv('FIREBASE_DATABASE_URL')
    })

    # Reference to the 'test' node in the database
    ref = db.reference('test')

    # Add a text input (e.g., a string field) to the 'test' node
    ref.update({
        'text_input': 'This is a sample text'  # Replace with your desired text
    })

    # Example: Update or add nested fields if needed
    ref.child('subnode').update({
        'nested_text': 'Nested text example'
    })

    # Example: Update a specific user node (if it exists or needs to be created)
    user_ref = db.reference('users/user123')
    user_ref.update({
        'name': 'John Doe',
        'age': 30,
        'comment': 'Additional text input'  # Another text field
    })