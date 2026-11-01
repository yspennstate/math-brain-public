"""Publish only the complete, claimed, concept-only author draft; never ingest."""
import argparse
import datetime
import hashlib
import json
from pathlib import Path

root=Path(__file__).resolve().parent
claim=json.loads((root/"INBOX_CLAIM.json").read_text(encoding="utf-8"))
deadline=datetime.datetime.fromisoformat(claim["expires_at"].replace("Z","+00:00"))
if datetime.datetime.now(datetime.timezone.utc)>=deadline:
    raise SystemExit("Claim expired; renew the narrow author-inbox claim before publishing.")
inbox=Path(claim["resource"])
inbox.mkdir(parents=True,exist_ok=True)
assert inbox.resolve()==inbox.absolute(),"Author inbox must not redirect elsewhere."
target=inbox/"bundle_001.json"
payload=(root/"bundle_001.json").read_bytes()
if target.exists():
    assert target.read_bytes()==payload,"Preserve a different existing author's artifact."
else:
    part=inbox/("bundle_001."+datetime.datetime.now().strftime("%H%M%S%f")+".part")
    assert part.resolve().is_relative_to(inbox.resolve()) and target.resolve().is_relative_to(inbox.resolve())
    with part.open("xb") as f:
        f.write(payload)
        f.flush()
    part.rename(target)
life=json.loads((root/"BUNDLE_LIFECYCLE.json").read_text(encoding="utf-8"))
life.update({"submitted":True,"inbox_path":str(target),"sha256":hashlib.sha256(payload).hexdigest(),
 "submitted_at":datetime.datetime.now(datetime.timezone.utc).isoformat(),
 "reviewed":False,"ingested":False,"retrievable":False})
(root/"BUNDLE_LIFECYCLE.json").write_text(json.dumps(life,indent=2)+"\n",encoding="utf-8")
print(json.dumps(life))
