import sys
import asyncio
import socket
import ssl
import certifi
from motor.motor_asyncio import AsyncIOMotorClient
from pymongo.errors import ServerSelectionTimeoutError
import os
from dotenv import load_dotenv

load_dotenv()

async def test_connection(name, **kwargs):
    uri = os.environ.get("MONGODB_URL")
    print(f"\n--- Testing: {name} ---")
    print(f"Options: {kwargs}")
    try:
        client = AsyncIOMotorClient(uri, serverSelectionTimeoutMS=5000, **kwargs)
        # Ping
        await client.admin.command('ping')
        print(f"✅ SUCCESS: {name} worked!")
        return True
    except Exception as e:
        print(f"❌ FAILED: {name}")
        print(f"Error: {e}")
        return False
    finally:
        if 'client' in locals():
            client.close()

async def run_diagnostics():
    uri = os.environ.get("MONGODB_URL")
    if not uri:
        print("Error: MONGODB_URL not found in .env")
        return

    # Test 1: Standard
    await test_connection("Standard (Current)")

    # Test 2: Trust all certs (Diagnostic only)
    await test_connection("TLS Allow Invalid (Cert Test)", tlsAllowInvalidCertificates=True)

    # Test 3: Force IPv4
    await test_connection("Force IPv4", family=socket.AF_INET)
    
    # Test 4: Use certifi context
    ssl_context = ssl.create_default_context(cafile=certifi.where())
    await test_connection("Explicit Certifi Context", tlsContext=ssl_context)

if __name__ == "__main__":
    asyncio.run(run_diagnostics())
