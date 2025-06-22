# waggle.sol/scripts/validate_kernel.py
# Validates anchors_manifest_hash.md against the expected Kernel69 SHA-256

import hashlib
import os

# Path to the manifest file (adjust if structure changes)
MANIFEST_PATH = "../../alvearium/docs/anchors_manifest_hash.md"

# Replace this with actual hash from anchors_manifest_hash.md
EXPECTED_HASH = "079750372369569155c237157400a53d49df62550e3a5a57b3c30a9026f5c74b"

def get_sha256(file_path):
    with open(file_path, "rb") as f:
        content = f.read()
    return hashlib.sha256(content).hexdigest()

def main():
    if not os.path.exists(MANIFEST_PATH):
        print(f"[ERROR] File not found: {MANIFEST_PATH}")
        return

    actual_hash = get_sha256(MANIFEST_PATH)
    print("Expected:", EXPECTED_HASH)
    print("Actual:  ", actual_hash)

    if actual_hash == EXPECTED_HASH:
        print("[OK] Kernel validation PASSED")
    else:
        print("[FAIL] Kernel validation FAILED")

if __name__ == "__main__":
    main()
