"""Place only this C0052 draft in the specifically requested inbox directory."""

import os
from pathlib import Path


source = Path(__file__).resolve().parent / "bundle_001.json"
inbox = Path("~/math-brain-inbox/w476").resolve()
parent = Path("~/math-brain-inbox").resolve()
if inbox.parent != parent or inbox.name != "w476":
    raise RuntimeError("Unexpected inbox destination")
inbox.mkdir(parents=True, exist_ok=True)
part = inbox / "bundle_001.json.part"
final = inbox / "bundle_001.json"
if final.exists() or part.exists():
    raise RuntimeError("Refusing to overwrite an existing draft")
part.write_bytes(source.read_bytes())
os.replace(part, final)
print(f"submitted={final}; bytes={final.stat().st_size}")
