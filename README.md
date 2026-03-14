# DNS-Reels-Blocker
A Python-based DNS sinkhole to mitigate social media distractions and track network habits.
Created on March 13th 2026


# DNS Focus Blocker (Python)

## My "Why"
As a 1st year Computer Science student, I noticed how short form content (Snapchat Spotlight/YouTube Shorts) was impacting my study sessions and attention span. I built this project to reclaim my focus through network engineering rather than just willpower (that fails me more often than not!).

## Key Features
- **DNS Sinkholing:** Intercepts UDP traffic on Port 53 to block specific social media domains.
- **Behavioral Nudge:** Redirects blocked requests to a local Flask web server displaying a "Get back to work" warning.
- **Network Analytics:** Logs domain request frequency to a JSON database for habit analysis.

## Technical Stack
- **Language:** Python 3.x
- **Libraries:** `dnslib` (DNS parsing), `flask` (Warning page server), `socket` (Network communication).
- **Network Layer:** Operates at Layer 3/4 of the OSI Model.

## Learning Outcomes
- Understanding the DNS request/response lifecycle.
- Managing data persistence using JSON.
- Implementing graceful error handling for malformed UDP packets.
- Navigating the limitations of blocking encrypted (HTTPS) application-layer traffic.
