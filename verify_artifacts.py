import hashlib
from pathlib import Path

artifact_dir = Path("../artifacts")
signature_dir = Path("../signatures")

for sig_file in signature_dir.iterdir():
    artifact_file = artifact_dir / f"{sig_file.stem}.txt"  # adjust as needed
    if artifact_file.exists():
        with open(artifact_file, "rb") as f:
            data = f.read()
            hash_check = hashlib.sha256(data).hexdigest()
        saved_hash = sig_file.read_text().strip()
        print(f"{artifact_file.name}: {'OK' if hash_check == saved_hash else 'CORRUPT'}")
