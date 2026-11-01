"""Record reported peer scope and validate drafts without any ingestion."""
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path
import re

ROOT=Path(__file__).resolve().parent
stamp=datetime.now(timezone.utc).isoformat()
peer={"agent":"w502","reported_verdict":"SCOPED KEEP L1-L4","artifact":"~/brain_workers/w502/PAIR_AUDIT.md",
      "source":"direct mesh message read with team_comm.py; not a re-audit",
      "served_model_evidence_verified":False,"not_a_completed_referee_gate":True}
for filename in ("SOURCE_STATUS.json","BUNDLE_STATES.json"):
    value=json.loads((ROOT/filename).read_text(encoding="utf-8"))
    value["reported_peer_audit"]=peer
    (ROOT/filename).write_text(json.dumps(value,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
with (ROOT/"REVIEW_PACKET.md").open("a",encoding="utf-8") as stream:
    stream.write("\n2026-10-10: w502 reported scoped KEEP of L1-L4 at ~/brain_workers/w502/PAIR_AUDIT.md after an independent statement/OU checkpoint. This is a peer report, not a completed w503 review or a verified served-model receipt. The concepts remain DRAFT; no theorem promotion follows.\n")

bundle=json.loads((ROOT/"bundle_001.json").read_text(encoding="utf-8"))
submitted=Path("~/math-brain-inbox/w501/bundle_001.json")
assert submitted.read_bytes()==(ROOT/"bundle_001.json").read_bytes()
required={"key","namespace","logical_name","kind","title","statement","proof_text","assumptions","domain","source"}
keys=set()
for row in bundle["entries"]:
    assert required<=row.keys()
    assert row["kind"] in {"concept","definition"} and row["proof_text"] is None
    assert row["statement"].strip() and row["source"]["license"].startswith("owner-own-work")
    assert row["key"] not in keys
    keys.add(row["key"])
allowed={"depends_on","defines","proves","refutes","generalizes","specializes","analogous_to","cites","semantic_association"}
graph={k:[] for k in keys}
for row in bundle["relations"]:
    assert row["kind"] in allowed and row["from_key"] in keys
    assert ("to_key" in row) != ("to_existing_logical" in row)
    if "to_key" in row:
        assert row["to_key"] in keys
        if row["kind"]=="depends_on": graph[row["from_key"]].append(row["to_key"])
    else:
        assert row["to_existing_logical"].startswith("math:")
seen=set()
active=set()
def visit(key):
    assert key not in active, "dependency cycle"
    if key in seen: return
    active.add(key)
    for target in graph[key]: visit(target)
    active.remove(key)
    seen.add(key)
for key in keys: visit(key)
states=json.loads((ROOT/"BUNDLE_STATES.json").read_text(encoding="utf-8"))
assert states["submitted"] and not any(states[k] for k in ("reviewed","ingested","retrievable"))
claims=[json.loads(line) for line in (ROOT/"CLAIMS.jsonl").read_text(encoding="utf-8").splitlines() if line]
assert len({r["id"] for r in claims})==len(claims)
assert all(not row["parent_problem_solved"] for row in claims)
statuses={"conjecture","numerical evidence","sketch","proved special case","independently checked proof"}
assert all(row["status"] in statuses for row in claims)
assert all(row["status"]!="independently checked proof" for row in claims)

patch_checks=[]
repo=Path("~/<private-repo>")
for patch_path in sorted((ROOT/"patches").glob("*.diff")):
    lines=patch_path.read_text(encoding="utf-8").splitlines()
    target=lines[0].removeprefix("--- a/")
    assert lines[1]=="+++ b/"+target
    match=re.fullmatch(r"@@ -(\d+) \+(\d+) @@",lines[2])
    assert match and match[1]==match[2]
    with (repo/target).open(encoding="utf-8") as stream:
        actual=next(line.rstrip("\r\n") for n,line in enumerate(stream,1) if n==int(match[1]))
    assert lines[3]=="-"+actual, "live source differs; refuse candidate patch"
    new_row=json.loads(lines[4][1:])
    assert new_row.get("problem_id")=="C0120"
    patch_checks.append({"patch":str(patch_path),"target":str(repo/target),"old_line_matches":True,"live_write":False})
receipt={"schema":"w501-packet-validation-v1","as_of":stamp,"passed":True,"entries":len(keys),"relations":len(bundle["relations"]),
         "claim_rows":len(claims),"only_draft_concepts_and_definitions":True,"dependency_graph_acyclic":True,
         "submitted_bytes_match_local":True,"patch_checks":patch_checks,"store_ingestion_performed":False}
(ROOT/"packet_validation.json").write_text(json.dumps(receipt,indent=2)+"\n",encoding="utf-8")
manifest=json.loads((ROOT/"REVIEW_MANIFEST.json").read_text(encoding="utf-8"))
manifest["created_at"]=stamp
manifest["files"].append({"path":str(ROOT/"packet_validation.json"),"sha256":""})
manifest["files"].append({"path":str(ROOT/"finalize_packet.py"),"sha256":""})
for row in manifest["files"]: row["sha256"]=hashlib.sha256(Path(row["path"]).read_bytes()).hexdigest()
(ROOT/"REVIEW_MANIFEST.json").write_text(json.dumps(manifest,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
print(json.dumps({**{k:v for k,v in receipt.items() if k!="patch_checks"},
      "review_manifest_sha256":hashlib.sha256((ROOT/"REVIEW_MANIFEST.json").read_bytes()).hexdigest()}))
