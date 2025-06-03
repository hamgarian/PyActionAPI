# free python backend that runs forever yippee 🎉

Current Link : https://red-appearance-rational-worry.trycloudflare.com

Frontend : https://hamgarian.github.io/PyActionAPI/

<hr>


#### Perpetually Running Python Backend with GitHub Actions + Cloudflare Workers + GitHub Pages

This project demonstrates a modern, serverless architecture where a Python backend is run **continuously** using **GitHub Actions** — not just for CI/CD, but as a perpetual service. It integrates with a frontend hosted on GitHub Pages and uses Cloudflare Workers as a secure gateway.

---

## Overview

### Key Components:

- **Python Backend running on GitHub Actions**  
  The backend runs as a long-lived GitHub Actions workflow, providing a continuously operating Python service without a traditional server.

- **Cloudflare Worker as Secure Proxy**  
  Acts as a secure “doorman” that validates requests and proxies backend data to the frontend, enabling a pure HTML frontend without exposing sensitive API keys.

- **Firestore Database**  
  Used to store and update the current backend URL dynamically, helping the system work around GitHub Actions’ 6-hour runtime limit.

- **Frontend hosted on GitHub Pages**  
  A static website that interacts with the backend via Cloudflare Worker.

---

## How It Works

### 1. GitHub Actions as a Perpetual Python Backend

- The Python backend runs inside a GitHub Actions workflow.
- Since GitHub Actions have a **6-hour maximum runtime**, the backend cannot run indefinitely.
- To handle this, the backend updates the Firestore database with its current active public URL before the workflow stops.
- This way, other system components always know where to find the **currently active backend instance**.

### 2. Firestore: Managing Backend URL State

- Firestore acts as a dynamic registry that stores the URL of the active Python backend.
- When the GitHub Actions backend instance starts, it writes its accessible URL to Firestore.
- Other parts of the system (Cloudflare Worker, frontend) query Firestore to find the current backend URL to use.
- This ensures seamless switching between backend instances every 6 hours.

### 3. Cloudflare Worker: Secure Proxy and API Key Protection

- The frontend is a **pure static HTML site** hosted on GitHub Pages.
- Since Firestore requires authentication via API keys, exposing these keys directly in frontend code would be insecure.
- The Cloudflare Worker acts as a **secure proxy** that:
  - Validates incoming requests to allow only trusted origins (e.g., your GitHub Pages site).
  - Requests the current backend URL from Firestore.
  - Proxies backend data to the frontend without exposing Firestore API keys.
- This architecture allows a secure, keyless frontend experience.

### 4. Frontend on GitHub Pages

- The static frontend lets users interact with the system by requesting URLs via the Cloudflare Worker.
- The Worker returns the backend data fetched through Firestore, enabling dynamic functionality without server code on the frontend.


## Benefits

- **Overcomes GitHub Actions runtime limits:** Uses Firestore to keep backend URL state across backend restarts every 6 hours.
- **Secure frontend without API keys:** Cloudflare Worker hides Firestore API keys and validates requests.
- **No traditional servers needed:** Backend runs on free GitHub Actions CI infrastructure.
- **Fully automated:** Deployment and backend execution are managed via GitHub Actions workflows.


## Usage

1. **Set up Firestore database**  
   Create Firestore collections to store the active backend URL and any necessary data.

2. **Deploy Python backend with GitHub Actions**  
   Configure a workflow that runs the backend, updates Firestore with the active URL, and renews itself as needed.

3. **Deploy Cloudflare Worker**  
   Write and deploy a Worker script to securely proxy requests between frontend and backend.

4. **Host frontend on GitHub Pages**  
   Publish the static site that interacts with the Cloudflare Worker.

## Notes

- GitHub Actions runtime limit of 6 hours requires backend URL rotation.
- Firestore stores and updates backend URLs dynamically.
- Cloudflare Worker protects Firestore API keys from exposure in frontend code.
- Monitor GitHub Actions usage to avoid hitting limits.


## License

MIT License

---

## Author

hamgarian
