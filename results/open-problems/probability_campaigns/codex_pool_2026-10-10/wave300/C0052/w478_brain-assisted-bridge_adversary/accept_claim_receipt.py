"""Record the actual successful renewed claim; never invent a lease."""
import json
from pathlib import Path

root=Path(__file__).resolve().parent
raw=json.loads((root/"INBOX_CLAIM_RAW.json").read_text(encoding="utf-8-sig"))
assert raw["agent"]=="w478" and len(raw["acquired"])==1
c=raw["acquired"][0]
assert Path(c["resource"]).resolve()==Path("~/math-brain-inbox/w478").resolve()
assert c["mode"]=="exclusive"
record={"agent":"w478","claim_id":c["claim_id"],"resource":c["resource"],"expires_at":c["expires_at"]}
(root/"INBOX_CLAIM.json").write_text(json.dumps(record,indent=2)+"\n",encoding="utf-8")
print(json.dumps(record))
