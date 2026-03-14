# Reels Blocker for Focus

## My Project Vision
As a 1st year Computer Science student, I wanted to engineer a "distraction-free" environment by blocking the doomscrolling algorthims (Snapchat Spotlight and Instagram Reels) at the network and system level.

## My Technical Hurdles and Evolution
This project underwent several iterations as I navigated modern web security architectures:

1. **Phase 1: DNS Sinkholing (in Python)** Built a custom DNS server using `dnslib` to intercept UDP Port 53 traffic and sinkhole social media API domains.
   
2. **Phase 2: Browser Manipulation & Security Hurdles** Attempted to use JavaScript (Tampermonkey) to redirect Reels/Spotlight to a local Flask server. 
   - **Hurdle:** Encountered **Content Security Policy (CSP)** restrictions, learning that high-security sites like Instagram and Snapchat block external redirects and the use of `eval()` to prevent cross-site scripting (XSS).
   - **Hurdle:** Encountered **React Hydration Errors**. Modifying the DOM caused state mismatches in the React framework.

3. **Phase 3: System Level Optimization (The Final Solution)** To maximize efficiency and bypass Application-Layer security, I migrated the blocking logic to the **Operating System Hosts File**. This provides a zero-latency, zero-RAM solution that works at the kernel level.

## Learning Points
- **OSI Model:** Applied knowledge of Layer 3 (Network) vs. Layer 7 (Application) filtering.
- **Web Security:** Deep dive into CSP (Content Security Policy) and why modern browsers block certain scripts.
- **Framework Mechanics:** Understanding how React "Hydration" works and why it crashes when the DOM is modified externally.
- **Efficiency:** Choosing the Hosts file over a running Python script to save system resources.

## Repository Structure
- `/hosts_backup`: Reference list of blocked domains.
- `dns_blocker_legacy.py`: Initial Python prototype for educational reference.
- `README.md`: Project documentation.
