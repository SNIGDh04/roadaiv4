import os
from pymongo import MongoClient
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# --- CONNECTION SETTINGS ---
# You can either paste your URL here OR set it in your .env file
MONGODB_URL = os.getenv("MONGODB_URL") 

if not MONGODB_URL or MONGODB_URL == "PASTE_YOUR_MONGODB_URL_HERE":
    print("❌ ERROR: MONGODB_URL not found.")
    print("Please paste your URL in the script or set it in your .env file.")
    exit()

print("📡 Attempting to connect to MongoDB...")

try:
    # Create client with a 10-second timeout (Better for initial cloud handshake)
    client = MongoClient(MONGODB_URL, serverSelectionTimeoutMS=10000)

    # The 'ping' command is the standard way to verify a connection
    client.admin.command('ping')

    print("✅ MongoDB Connection Successful!")
    
    # List databases to verify access
    dbs = client.list_database_names()
    print(f"📊 Access verified. Databases found: {', '.join(dbs)}")

except Exception as e:
    print("❌ MongoDB Connection Failed:")
    print(f"Error Details: {e}")
    print("\nTroubleshooting:")
    print("1. Check if your IP is whitelisted in MongoDB Atlas (Network Access).")
    print("2. Verify your username and password in the connection string.")
    print("3. Ensure you are using the correct connection string for 'Drivers' -> 'Python'.")
finally:
    if 'client' in locals():
        client.close()