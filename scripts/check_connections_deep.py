import socket
import dns.resolver
import sys

def check_dns(host):
    print(f"🔍 Testing DNS resolution for {host}...")
    try:
        # Note: SRV records are usually for +srv URLs. 
        # For standard mongodb:// URLs, we check A/AAAA records.
        answers = dns.resolver.resolve(host, 'A')
        print(f"✅ DNS OK: Found {len(answers)} A records.")
        return True
    except Exception as e:
        # Try SRV just in case it's an SRV host
        try:
            answers = dns.resolver.resolve(host, 'SRV')
            print(f"✅ DNS OK: Found {len(answers)} SRV records.")
            return True
        except:
            print(f"❌ DNS FAILED: {e}")
            return False

def check_port(host, port=27017):
    print(f"🔌 Testing TCP Port {port} on {host}...")
    try:
        s = socket.create_connection((host, port), timeout=5)
        s.close()
        print(f"✅ PORT OK: Port {port} is OPEN.")
        return True
    except Exception as e:
        print(f"❌ PORT BLOCKED: {e}")
        return False

if __name__ == "__main__":
    # Extracted from the URL you pasted:
    # mongodb://atlas-sql-69da69c4e43bf6482e98fe8a-drs4wd.a.query.mongodb.net/sample_mflix
    host = "atlas-sql-69da69c4e43bf6482e98fe8a-drs4wd.a.query.mongodb.net"
    
    dns_ok = check_dns(host)
    port_ok = check_port(host)
    
    print("\n--- DIAGNOSIS ---")
    if not dns_ok:
        print("💡 Your local DNS cannot find the host. Try changing your DNS (e.g., to 8.8.8.8).")
    elif not port_ok:
        print("💡 Port 27017 (or the connection port) is BLOCKED. If this is an Atlas SQL port, it might be different (e.g., 27015 or 27017).")
    else:
        print("💡 Network is CLEAR. If authentication fails, check your username/password/IP whitelist.")
