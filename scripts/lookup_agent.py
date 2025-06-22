# waggle.sol/scripts/lookup_agent.py
# Simulates looking up an agent from Hive.bnb's registry
# This is a placeholder for testing interop with hive agent registry

import json
import os

# Simulated registry file path (this would eventually be on-chain or Arweave)
AGENTS_FILE = "../../hive.bnb/scripts/agents_sample.json"

# Example agent address to test
TEST_AGENT_ADDRESS = "0xBEEf1234567890abcdef1234567890abcdefBEEF"

def load_agents():
    if not os.path.exists(AGENTS_FILE):
        print("[ERROR] Agent registry file not found.")
        return {}

    with open(AGENTS_FILE, "r") as f:
        return json.load(f)

def lookup_agent(address):
    agents = load_agents()
    agent = agents.get(address)

    if agent:
        print(f"[OK] Agent found: {address}")
        print(f"  Subdomain     : {agent['subdomain']}")
        print(f"  Metadata Hash : {agent['metadataHash']}")
        print(f"  Active        : {agent['active']}")
    else:
        print(f"[FAIL] No agent registered for: {address}")

if __name__ == "__main__":
    lookup_agent(TEST_AGENT_ADDRESS)
