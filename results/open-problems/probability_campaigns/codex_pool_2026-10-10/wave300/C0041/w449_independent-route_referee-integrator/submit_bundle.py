"""Submit only w449's validated draft JSON to the explicitly named inbox path."""
from pathlib import Path
import os

root = Path(__file__).parent
source = root / "drafts" / "bundle_001.json"
target_dir = Path("~/math-brain-inbox/w449")
target = target_dir / "bundle_001.json"
part = target_dir / "bundle_001.part"
data = source.read_bytes()

if target.exists():
    if target.read_bytes() != data:
        raise SystemExit(f"Refusing to replace different existing draft: {target}")
    print(f"already submitted: {target}")
else:
    target_dir.mkdir(parents=True, exist_ok=True)
    if part.exists():
        raise SystemExit(f"Refusing to replace existing part: {part}")
    part.write_bytes(data)
    os.replace(part, target)
    print(f"submitted {len(data)} bytes: {target}")
