# waggle.sol/scripts/lookup_agent.py
# Simulates looking up an agent from Hive.bnb's registry
# This version supports fallback to Arweave-hosted registry if local file is missing

import json
import os
import urllib.request

# Local agent registry path
AGENTS_FILE = "../../hive.bnb/scripts/agents_sample.json"

# Arweave fallback if local file not found
ARWEAVE_FALLBACK_URL = "https://arweave.net/gQPJ3lVROKnnQVbsJ_Y-XD7HfMvYHExFu-_OoDlPNwU"

# Example agent address to test
TEST_AGENT_ADDRESS = "0xBEEf1234567890abcdef1234567890abcdefBEEF"

def load_agents():
    if os.path.exists(AGENTS_FILE):
        print("[INFO] Loading local agent registry...")
        with open(AGENTS_FILE, "r") as f:
            return json.load(f)
    else:
        print("[WARN] Local registry not found. Trying Arweave fallback...")
        try:
            with urllib.request.urlopen(ARWEAVE_FALLBACK_URL) as response:
                return json.loads(response.read().decode())
        except Exception as e:
            print(f"[ERROR] Failed to load registry from Arweave: {e}")
            return {}

def lookup_agent(address):
    agents = load_agents()
    agent = agents.get(address)

    if agent:
        print(f"[OK] Agent found: {address}")
        print(f"  Subdomain     : {agent.get('subdomain', 'N/A')}")
        print(f"  Metadata Hash : {agent.get('metadataHash', 'N/A')}")
        print(f"  Active        : {agent.get('active', 'N/A')}")
    else:
        print(f"[FAIL] No agent registered for: {address}")

if __name__ == "__main__":
    lookup_agent(TEST_AGENT_ADDRESS)
