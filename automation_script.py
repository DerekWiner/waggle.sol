import os

directories = [
    "kernel",
    "contracts",
    "docs",
    "agents",
    "nfts",
    "whitepapers"
]

readme_template = "# {name}\n\nThis is the {name} directory for the waggle.sol project."

# Create directories and README files
for dir_name in directories:
    os.makedirs(dir_name, exist_ok=True)
    with open(os.path.join(dir_name, "README.md"), "w") as f:
        f.write(readme_template.format(name=dir_name.capitalize()))

# Optionally create a master README
with open("README.md", "w") as f:
    f.write("# waggle.sol\n\nDecentralized OS infrastructure and agent ecosystem.\n")