# automation_script.py

import os

# Optional: import the technical spec agent if present
try:
    import technical_spec_agent
    has_spec_agent = True
except ImportError:
    has_spec_agent = False

# Core repo folders
folders = [
    "kernel",                # Core logic, consensus, and 69 Protocol
    "governance",            # MetaDAO, agents, 3 Laws supremacy
    "execution",             # Execution layer and smart contract logic
    "chronosphere",          # Temporal intelligence, time-indexing, history hashing
    "nectar",                # Cosmos layer zero-gas architecture
    "hive.bnb",              # BNB-side operations
    "waggle.sol",            # Solana-side smart contract work
    "agents",                # AI agent templates and swarm logic
    "NFTs",                  # Identity, permissions, logic-carrying NFTs
    "iOT",                   # Lightweight IoT device scaffolding
    "neuralink",             # Add-ons for brain-computer interface
    "docs",                  # Whitepaper, Manifesto, architecture diagrams
    "utils",                 # Post-quantum cryptographic tools, entropy gen, etc
    ".github/workflows"      # GitHub Actions
]

# Key files to write to root
files = {
    "README.md": "# Waggle.sol\n\nLinux-for-Crypto OS enabling agentic AI, layered governance, and cross-chain swarm intelligence.",
    "LICENSE": "All code released under the Universal Public Domain. No rights reserved.",
    ".gitignore": "__pycache__/\n*.pyc\n.env\nnode_modules/\nbuild/\ndist/",
    "docs/manifesto.md": "## Manifesto\n\nOpen Source Without Malice. We believe in a fertile, permissioned ground for ASI emergence.",
    "docs/whitepaper.md": "# Whitepaper\n\nCore architecture, tokenomics, 69 Protocol, governance stack, and swarm-enabled AI models."
}

# Create folders
for folder in folders:
    os.makedirs(folder, exist_ok=True)
    readme_path = os.path.join(folder, "README.md")
    with open(readme_path, "w") as f:
        f.write(f"# {folder}\n\nThis folder handles logic related to `{folder}`.")

# Create core files
for filename, content in files.items():
    os.makedirs(os.path.dirname(filename) or ".", exist_ok=True)
    with open(filename, "w") as f:
        f.write(content)

# Run technical spec generation if available
if has_spec_agent:
    technical_spec_agent.create_spec_files()
    print("🧠 Technical spec files generated.")

print("✅ Repo structure initialized with core files.")