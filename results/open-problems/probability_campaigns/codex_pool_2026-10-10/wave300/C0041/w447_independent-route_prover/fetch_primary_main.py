"""Copy only the named primary proof entrypoint and print targeted excerpts."""
import hashlib
import json
import urllib.request
from pathlib import Path

root = Path(__file__).resolve().parent / "sources"
root.mkdir(exist_ok=True)
url = "https://raw.githubusercontent.com/openai/math/main/lean/OAI/Probability/Ballisticity/Main.lean"
with urllib.request.urlopen(url, timeout=25) as response:
    data = response.read(262145)
if len(data) > 262144:
    raise RuntimeError("named entrypoint exceeds 256 KiB source-read gate")
path = root / "Ballisticity.Main.lean"
path.write_bytes(data)
lines = data.decode("utf-8").splitlines()
selected = set(range(min(18, len(lines))))
for i, line in enumerate(lines):
    if any(cue in line for cue in ("directional_transience_implies_ballisticity", "MainStatement", "sorry", "axiom ")):
        selected.update(range(max(0, i - 5), min(len(lines), i + 22)))
print(json.dumps({"url": url, "bytes": len(data), "sha256": hashlib.sha256(data).hexdigest(), "lines": len(lines)}))
for i in sorted(selected):
    print(f"{i+1}: {lines[i]}")
