"""Submit the exact authorized DRAFT only; no integration or live-store mutation."""
from pathlib import Path
import json
import os

root = Path(__file__).resolve().parent
folder = Path("~/math-brain-inbox/w481")
folder.mkdir(exist_ok=True)
target = folder / "bundle_001.json"
part = folder / "bundle_001.json.part"
data = (root / "bundle_001.json").read_bytes()
validation = json.loads((root / "VALIDATION.json").read_text(encoding="utf-8"))
assert all(validation["checks"].values()) and validation["theorem_or_lemma_promotions"] == 0
assert json.loads(data)["author_agent"] == "w481"
if target.exists():
    assert target.read_bytes() == data, "Existing draft differs; refusing to overwrite it"
else:
    if part.exists():
        assert part.read_bytes() == data, "Incomplete earlier draft differs; preserve it for review"
    else:
        with part.open("xb") as handle:
            handle.write(data)
            handle.flush()
            os.fsync(handle.fileno())
    part.rename(target)
status = json.loads((root / "SOURCE_STATUS.json").read_text(encoding="utf-8"))
status["submission"] = {"submitted": True, "draft_path": str(target), "reviewed": False,
                        "ingested": False, "retrievable": False,
                        "note": "Staged DRAFT only. Independent mathematical and provenance gates remain pending; worker did not run the live integrator."}
(root / "SOURCE_STATUS.json").write_text(json.dumps(status, indent=2, ensure_ascii=False)+"\n", encoding="utf-8")
(root / "SUBMISSION_RECEIPT.json").write_text(json.dumps(status["submission"], indent=2)+"\n", encoding="utf-8")
print(json.dumps(status["submission"], indent=2))
