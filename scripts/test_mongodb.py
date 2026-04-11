import asyncio
import os
from motor.motor_asyncio import AsyncIOMotorClient
from dotenv import load_dotenv

# Load local .env if available
load_dotenv()

async def test_mongodb_connection():
    # 1. Get URL from environment
    mongodb_url = os.environ.get("MONGODB_URL")
    
    if not mongodb_url:
        print("❌ ERROR: MONGODB_URL not found in environment variables.")
        print("Please set MONGODB_URL in your .env file or export it.")
        return

    print(f"📡 Attempting to connect to: {mongodb_url.split('@')[-1]}") # Print only the host part for security
    
    try:
        # 2. Initialize Client
        client = AsyncIOMotorClient(mongodb_url, serverSelectionTimeoutMS=5000)
        
        # 3. Ping the database
        # The 'ping' command is cheap and does not require credentials to be perfect, 
        # but will fail if the networking/cluster is unreachable.
        print("⏳ Pinging MongoDB...")
        await client.admin.command('ping')
        
        # 4. List databases to verify access rights
        db_names = await client.list_database_names()
        
        print("✅ SUCCESS: Connected to MongoDB Atlas!")
        print(f"📊 Available Databases: {', '.join(db_names)}")
        
    except Exception as e:
        print("❌ CONNECTION FAILED!")
        print(f"Reason: {str(e)}")
        print("\nCommon fixes:")
        print("1. IP Whitelisting: Ensure your current IP is allowed in MongoDB Atlas Network Access.")
        print("2. Credentials: Check if your username/password in the connection string are correct.")
        print("3. Special Characters: If your password contains '@' or ':', URL-encode them.")
    finally:
        if 'client' in locals():
            client.close()

if __name__ == "__main__":
    asyncio.run(test_mongodb_connection())
