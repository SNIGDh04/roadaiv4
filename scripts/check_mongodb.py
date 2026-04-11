#!/usr/bin/env python3
"""
ROADAI v4.0 — MongoDB Atlas Connection Verifier
"""
import os
import asyncio
import sys
from motor.motor_asyncio import AsyncIOMotorClient
from pymongo.errors import ConnectionFailure, OperationFailure

async def verify_connection():
    uri = os.environ.get("MONGODB_URL")
    
    if not uri:
        print("❌ ERROR: MONGODB_URL environment variable is not set.")
        sys.exit(1)
        
    print(f"🚦 Attempting to connect to MongoDB...")
    
    try:
        client = AsyncIOMotorClient(uri, serverSelectionTimeoutMS=5000)
        await client.admin.command('ping')
        print("✅ SUCCESS: Successfully connected to MongoDB Atlas!")
        server_info = await client.server_info()
        print(f"📦 MongoDB Version: {server_info.get('version')}")
        db_name = uri.split('/')[-1].split('?')[0] or "roadai"
        print(f"🗄️  Default Database: {db_name}")
    except Exception as e:
        print(f"❌ CONNECTION FAILURE: {e}")
    finally:
        client.close()

if __name__ == "__main__":
    if sys.platform == 'win32':
        asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
    asyncio.run(verify_connection())
