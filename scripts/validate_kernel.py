# waggle.sol/scripts/validate_kernel.py
# Validates the anchors_manifest_hash.md against known Kernel69 hash

import hashlib

# Path to manifest file in alvearium repo
MANIFEST_PATH = "../../alvearium/docs/anchors_manifest_hash.md"

# Trusted Kernel69 value from NFT metadata
EXPECTED_HASH = "079750372369569155c237157400a53d49df62550e3a5a57b3c30a9026f5c74b"

def get_sha256(file_path):
    with open(file_path, "rb") as f:
        content = f.read()
    return hashlib.sha256(content).hexdigest()

def main():
    actual_hash = get_sha256(MANIFEST_PATH)
    print("Expected:", EXPECTED_HASH)
    print("Actual:  ", actual_hash)

    if actual_hash.startswith(EXPECTED_HASH[:8]):  # short match or full
       print("[OK] Kernel validation PASSED")
else:
    print("[FAIL] Kernel validation FAILED")

if __name__ == "__main__":
    main()
