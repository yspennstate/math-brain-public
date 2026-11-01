"""Submit this worker's validated draft to the explicitly assigned inbox slot."""

from pathlib import Path

source = Path(__file__).resolve().parent / "bundle_001.json"
target_dir = Path("~/math-brain-inbox/w527")
target_dir.mkdir(parents=True, exist_ok=True)
part = target_dir / "bundle_001.part"
final = target_dir / "bundle_001.json"
content = source.read_bytes()
if final.exists():
    if final.read_bytes() != content:
        raise RuntimeError("Existing submitted bundle differs; refusing overwrite")
    print(f"already submitted: {final}")
else:
    part.write_bytes(content)
    if part.read_bytes() != content:
        raise RuntimeError("Incomplete draft copy")
    part.replace(final)
    print(f"submitted: {final}")
