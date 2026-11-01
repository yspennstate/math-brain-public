import json,time
from pathlib import Path
root=Path(__file__).resolve().parent
inbox=Path("~/math-brain-inbox/w405").resolve()
assert str(inbox).replace("\\","/").lower()=="~/math-brain-inbox/w405"
bundle=json.loads((root/"DRAFT_BUNDLE.json").read_text(encoding="utf-8"))
assert bundle["author_agent"]=="w405" and bundle["spec"]=="mathbrain-draft-v1"
inbox.mkdir(parents=True,exist_ok=True)
n=1
while (inbox/("bundle_"+str(n).zfill(3)+".json")).exists() or (inbox/("bundle_"+str(n).zfill(3)+".part")).exists():
    n+=1
    assert n<=200
part=inbox/("bundle_"+str(n).zfill(3)+".part")
dest=part.with_suffix(".json")
assert part.parent==inbox and dest.parent==inbox and not dest.exists()
with part.open("x",encoding="utf-8") as f:
    json.dump(bundle,f,ensure_ascii=False,indent=2)
part.rename(dest)
delivery={"submitted":True,"reviewed":False,"ingested":False,"retrievable":False,"inbox_file":str(dest),"local_bundle":str(root/"DRAFT_BUNDLE.json"),"claim_id":"clm-166d8618ef","submission_unix":time.time(),"review_state":"w406 original L1/L2/R1 kept; final w407 referee verdict pending","live_store_mutated":False}
(root/"DELIVERY_STATE.json").write_text(json.dumps(delivery,indent=2),encoding="utf-8")
p=root/"SOURCE_STATUS.json"
s=json.loads(p.read_text(encoding="utf-8"))
s["draft_delivery"]=delivery
p.write_text(json.dumps(s,ensure_ascii=False,indent=2),encoding="utf-8")
print(json.dumps(delivery,indent=2))
