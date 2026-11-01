"""Write a reviewable unified diff for the already-queued P0043 draft."""
from pathlib import Path

src = Path("drafts/bundle_001.json")
target = "~/math-brain-inbox/w443/bundle_001.json"
lines = src.read_text(encoding="utf-8").splitlines()
header = f"--- a/{target}\n+++ b/{target}\n@@ -0,0 +1,{len(lines)} @@\n"
Path("patches").mkdir(exist_ok=True)
Path("patches/01_p0043_bundle.diff").write_text(
    header + "\n".join("+" + line for line in lines) + "\n", encoding="utf-8"
)
print(f"patch lines={len(lines)}")
