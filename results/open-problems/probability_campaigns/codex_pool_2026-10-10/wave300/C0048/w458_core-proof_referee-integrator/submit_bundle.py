"""Submit only the named w458 draft, complete via .part then atomic rename."""
from pathlib import Path
import shutil
import os

src = Path(__file__).parent / "bundle_001.json"
dest_dir = Path("~/math-brain-inbox/w458")
dest_dir.mkdir(parents=True, exist_ok=True)
part = dest_dir / "bundle_001.json.part"
final = dest_dir / "bundle_001.json"
shutil.copyfile(src, part)
os.replace(part, final)
assert src.read_bytes() == final.read_bytes()
print(str(final), "bytes", final.stat().st_size)
