import socket
from dnslib import DNSRecord, RR, A, QTYPE

# 1. The Blocklist: Domains used by Snapchat for Discover/Spotlight content.
# (Note: App developers change these sometimes, so we may need to add more later!)
BLOCKED_DOMAINS = [
    "discover.snapchat.com",
    "addiscover.snapchat.com",
    "story.snapchat.com"
    "spotlight.snapchat.com",
    "story-feed.api.snapchat.com",
    "sc-cdn.net",
    "sc-static.net",
    "bolt-gcdn.sc-cdn.net",
    "cf-st.sc-cdn.net"
    # --- YouTube Shorts Specific ---
    "youtube.com/shorts",             # Main Shorts path
    "m.youtube.com/shorts",           # Mobile web Shorts
    "youtubei/v1/reel",               # The internal API for the "Reel" (Shorts) player
    "googlevideo.com/videoplayback?*cpn=Shorts", # Specific Shorts traffic patterns
    "yt3.ggpht.com",                  # Often used for Shorts channel icons/thumbnails
]

# 2. Server Configuration
LOCAL_IP = "0.0.0.0"       # This tells the script to listen on all your computer's network adapters
PORT = 53                  # Port 53 is the universal standard port for DNS traffic
UPSTREAM_DNS = "8.8.8.8"   # Google's public DNS server (we use this to load safe websites)

def start_dns_blocker():
    # Create a UDP network socket (DNS traffic uses the UDP protocol)
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    # Bind the socket to our IP and Port so it can start listening
    sock.bind((LOCAL_IP, PORT))
    print(f"[*] Python DNS Blocker is actively listening on port {PORT}... (i dare you to try doomscroll)")


    # An infinite loop to continuously listen for requests from your phone
    while True:
        try:
            # Wait for data (a DNS request) to arrive from the phone
            data, addr = sock.recvfrom(512)
            request = DNSRecord.parse(data)
            
            # Extract the actual website domain the phone is asking for
            domain_requested = str(request.q.qname).strip('.')
            
            # 3. The Logic: Check if the requested domain is in our blocklist
            if any(blocked in domain_requested for blocked in BLOCKED_DOMAINS):
                print(f"[BLOCKED:stopped ur silly phone from loading {domain_requested}] GET OFF SNAPCHAT - WORLD DOMINATION DOES NOT HAPPEN ON ITS OWN, GREATNESS IS AROUND THE CORNER")
                
                # Create a "fake" reply pointing to 0.0.0.0 (a null IP address)
                reply = request.reply()
                reply.add_answer(RR(request.q.qname, QTYPE.A, rdata=A("0.0.0.0")))
                
                
                # Send the fake reply back to the iPhone
                sock.sendto(reply.pack(), addr)
                
            else:
                # 4. If the domain is safe, forward the request to Google's real DNS
                forward_sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
                forward_sock.sendto(data, (UPSTREAM_DNS, 53))
                
                # Get the real answer back from Google
                response_data, _ = forward_sock.recvfrom(512)
                
                # Send the real answer back to the iPhone so the safe app/website loads
                sock.sendto(response_data, addr)
                
                
        except Exception as e:
            print(f"[ERROR] Something went wrong: {e}")

if __name__ == "__main__":
    start_dns_blocker()