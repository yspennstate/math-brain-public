"""Deliver a complete DRAFT to the specifically authorized worker inbox; never ingest."""
from pathlib import Path
import datetime as dt
import json
import os

ROOT=Path(__file__).resolve().parent
inbox=Path("~/math-brain-inbox/w517").resolve()
target=(inbox/"bundle_001.json").resolve()
part=(inbox/"bundle_001.json.part").resolve()
assert target.parent==inbox and part.parent==inbox
validation=json.loads((ROOT/"VALIDATION.json").read_text(encoding="utf-8"))
assert validation["structural"]["integrator_parse_errors"]==[]
content=(ROOT/"bundle_001.json").read_bytes()
inbox.mkdir(exist_ok=True)
if target.exists():
    assert target.read_bytes()==content,"Existing inbox draft differs; preserve it."
else:
    if part.exists():
        assert part.read_bytes()==content,"Existing partial differs; preserve it."
    else:
        with part.open("xb") as stream:
            stream.write(content)
            stream.flush()
            os.fsync(stream.fileno())
    part.rename(target)
assert target.read_bytes()==content
receipt={"worker":"w517","delivered_utc":dt.datetime.now(dt.timezone.utc).isoformat(),"path":str(target),
         "prepared":True,"submitted":True,"reviewed":False,"ingested":False,"retrievable":False,
         "entries":4,"relations":3,"kind":"unreviewed concept DRAFT; coordinator review/integration only",
         "exclusive_claim":"clm-acdb907b67","claim_expires_at":"2026-10-10T06:35:27Z"}
(ROOT/"SUBMISSION.json").write_text(json.dumps(receipt,indent=2)+"\n",encoding="utf-8")
source=json.loads((ROOT/"SOURCE_STATUS.json").read_text(encoding="utf-8"))
source["brain_bundle"].update(prepared=True,submitted=True,reviewed=False,ingested=False,retrievable=False,path=str(target))
(ROOT/"SOURCE_STATUS.json").write_text(json.dumps(source,indent=2)+"\n",encoding="utf-8")
print(json.dumps(receipt))
