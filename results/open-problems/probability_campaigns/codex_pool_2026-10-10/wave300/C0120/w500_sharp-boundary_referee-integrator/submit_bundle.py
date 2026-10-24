"""Place the validated draft in this task's named inbox, using the specified .part handoff."""

import json
from pathlib import Path

from validate_packet import root

source = root / "bundle_001.json"
data = source.read_text(encoding="utf-8")
bundle = json.loads(data)
assert bundle["author_agent"] == "w500"

inbox = Path("~/math-brain-inbox/w500")
inbox.mkdir(parents=True, exist_ok=True)
part = inbox / "bundle_001.json.part"
final = inbox / "bundle_001.json"
if final.exists():
    raise FileExistsError(f"Won't overwrite existing bundle: {final}")
with part.open("x", encoding="utf-8") as handle:
    handle.write(data)
part.replace(final)
assert json.loads(final.read_text(encoding="utf-8"))["bundle_slug"] == bundle["bundle_slug"]
print(f"submitted DRAFT: {final}")
