import hashlib
from pathlib import Path

artifact_dir = Path("../artifacts")
signature_dir = Path("../signatures")
signature_dir.mkdir(exist_ok=True)

for file in artifact_dir.iterdir():
    if file.is_file():
        with open(file, "rb") as f:
            data = f.read()
            hash = hashlib.sha256(data).hexdigest()
        sig_file = signature_dir / f"{file.stem}.sig"
        sig_file.write_text(hash)
        print(f"Signed {file.name} -> {sig_file.name}")
