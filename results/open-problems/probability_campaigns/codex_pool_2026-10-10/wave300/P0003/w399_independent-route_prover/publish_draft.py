"""Only explicitly authorized external write: this worker's DRAFT inbox."""
import difflib
import json
from pathlib import Path

ROOT=Path(__file__).resolve().parent
assert json.loads((ROOT/"VALIDATION.json").read_text(encoding="utf-8"))["passed"]
payload=(ROOT/"drafts/bundle_001.json").read_text(encoding="utf-8")
data=json.loads(payload)
assert data["author_agent"]=="w399" and all(e["kind"] in {"concept","definition"} for e in data["entries"])
inbox=Path("~/math-brain-inbox/w399")
assert inbox.parent.is_dir()
inbox.mkdir(exist_ok=True)
target=None
reused=False
for n in range(1,1000):
    candidate=inbox/f"bundle_{n:03d}.json"
    partial=candidate.with_suffix(".part")
    if candidate.exists():
        if candidate.read_text(encoding="utf-8")==payload:
            target=candidate
            reused=True
            break
        continue
    if partial.exists():
        continue
    with partial.open("x",encoding="utf-8") as handle:
        handle.write(payload)
    partial.rename(candidate)
    target=candidate
    break
if target is None:
    raise RuntimeError("no free draft number; no prior artifacts overwritten")
assert json.loads(target.read_text(encoding="utf-8"))==data
receipt=json.loads((ROOT/"DELIVERY_STATUS.json").read_text(encoding="utf-8"))
receipt.update(submitted=True,inbox_target=str(target),submission_method="complete .part file renamed to .json; prior files preserved",reused_identical=reused,reviewed=False,ingested=None,retrievable=None)
(ROOT/"DELIVERY_STATUS.json").write_text(json.dumps(receipt,indent=2)+"\n",encoding="utf-8")
live=target.as_posix()
patch="".join(difflib.unified_diff([],payload.splitlines(keepends=True),fromfile="a/"+live,tofile="b/"+live))
(ROOT/"patches/01_w399_three_probe_draft.diff").write_text(patch,encoding="utf-8")
if target.name!="bundle_001.json":
    report=(ROOT/"REPORT.md").read_text(encoding="utf-8").replace("w399/bundle_001.json","w399/"+target.name)
    (ROOT/"REPORT.md").write_text(report,encoding="utf-8")
with (ROOT/"HANDOFFS.jsonl").open("a",encoding="utf-8") as handle:
    handle.write(json.dumps({"recipient":"math-brain validating coordinator","state":"submitted-draft","artifact":str(target),"entries":len(data["entries"]),"relations":len(data["relations"]),"reviewed":False,"ingested":None,"retrievable":None})+"\n")
print(json.dumps(receipt,indent=2))
