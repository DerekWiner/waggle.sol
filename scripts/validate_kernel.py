# waggle.sol/scripts/validate_kernel.py
# Validates the anchors_manifest_hash.md against known Kernel69 hash

import hashlib

# Path to manifest file in alvearium repo
MANIFEST_PATH = "../../alvearium/docs/anchors_manifest_hash.md"

# Trusted Kernel69 value from NFT metadata
EXPECTED_HASH = "YK4h0pepnRw5lFmxwA9-61ODxEbnlyCSFznH9DUfhyQ"

def get_sha256(file_path):
    with open(file_path, "rb") as f:
        content = f.read()
    return hashlib.sha256(content).hexdigest()

def main():
    actual_hash = get_sha256(MANIFEST_PATH)
    print("Expected:", EXPECTED_HASH)
    print("Actual:  ", actual_hash)

    if actual_hash.startswith(EXPECTED_HASH[:8]):  # short match or full
        print("✅ Kernel validation PASSED")
    else:
        print("❌ Kernel validation FAILED")

if __name__ == "__main__":
    main()
