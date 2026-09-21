=== FILE: package.json ===
{
  "name": "fast-ai-chat",
  "version": "1.0.0",
  "description": "Fast reliable AI chat website",
  "main": "server.js",
  "type": "module",
  "scripts": {
    "start": "node server.js"
  },
  "dependencies": {
    "express": "^4.18.2",
    "node-fetch": "^3.3.2",
    "dotenv": "^16.4.5"
  }
}

=== FILE: .gitignore ===
node_modules
.env

=== FILE: README.md ===
# Fast AI Chat

Simple, fast AI chat website using Node.js + Express and an external AI API.

## Setup

1. Install dependencies:
   ```bash
   npm install
