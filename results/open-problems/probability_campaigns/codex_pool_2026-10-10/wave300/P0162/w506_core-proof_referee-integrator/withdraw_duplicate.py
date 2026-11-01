"""Preserve this worker's duplicate, superseded draft as an ignored .part."""
from pathlib import Path

directory = Path("~/math-brain-inbox/w506").resolve()
source = (directory / "bundle_001.json").resolve()
target = (directory / "bundle_001.withdrawn.part").resolve()
assert source.parent == directory and target.parent == directory
assert source.is_file() and not target.exists()
source.rename(target)
assert target.is_file() and not source.exists()
print(f"withdrawn={target}; preserved_bytes={target.stat().st_size}")
