# waggle.sol/scripts/validate_kernel.py
# Validates anchors_manifest_hash.md against the expected Kernel69 SHA-256

import hashlib
import os

# Path to the manifest file (adjust if structure changes)
MANIFEST_PATH = "../../alvearium/docs/anchors_manifest_hash.md"

# Replace this with actual hash from anchors_manifest_hash.md
EXPECTED_HASH = "e70f2dad191ea8702fa6653e089d0abe140653137aeb9e8864224353881b02ab"

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
