"""Prepare small unreviewed concept drafts; submit only to the named worker inbox."""
import argparse
from datetime import datetime, timezone
import json
from pathlib import Path

ROOT=Path(__file__).resolve().parent
INBOX=Path("~/math-brain-inbox/w351")
TARGET="math:probability.core:open-problem-p0017-dimension-free-log-concave-poincare-or-cheeger-constant"
ATTEMPT="math:probability.core:attempt-p0017-dimension-free-log-concave-poincare-or-cheeger-constant"
claims=[json.loads(line) for line in (ROOT/"CLAIMS.jsonl").read_text(encoding="utf-8").splitlines() if line.strip()]
entries=[]
names={"w351-L0":("affine-normalization-covariance-weighted-poincare","Affine normalization of a Poincare target"),"w351-L1":("two-block-poincare-maximal-correlation-criterion","Two-block variance criterion requires maximal correlation"),"w351-L2":("isotropic-simplex-edge-conditional-poincare-blowup","Isotropic simplex fibers have large conditional constants"),"w351-L3":("averaged-conditional-poincare-shortcut-simplex-obstruction","Averaging conditional Poincare constants fails"),"w351-L4":("isotropic-simplex-nonlinear-block-correlation","Isotropy does not remove nonlinear block dependence")}
for claim in claims:
    logical,title=names[claim["id"]]
    entries.append({"key":claim["id"],"namespace":"probability.poincare","logical_name":logical,"kind":"concept","title":"DRAFT: "+title,"statement":"DRAFT: independent mathematical review pending; no novelty claim. "+claim["statement"],"proof_text":None,"assumptions":claim["assumptions"],"domain":"probability theory","source":{"source_id":"owner-probability-campaign-w351:P0017:"+claim["id"],"url":str(ROOT/"ATTEMPT.md"),"revision":"author-draft-2026-10-10","license":"owner-own-work (campaign proof draft; independent review pending)","excerpt":None}})
entries.append({"key":"source-status","namespace":"probability.poincare","logical_name":"p0017-kls-publication-status-2026-10-10","kind":"concept","title":"P0017 source status as of 10 October 2026","statement":"The September 2026 campaign label attempted_unsolved for P0017 does not certify current openness. As of 10 October 2026, primary preprints arXiv:2610.05474v1 (Bizeul, Klartag, Lehec), arXiv:2610.01447v2 (Song, Zhang), and arXiv:2610.07728 (Balasubramanian, Kasiviswanathan) claim a universal Poincare constant for isotropic log-concave measures. This campaign worker checked the exact theorem statements of the first two, not their complete proofs. Current openness is UNKNOWN for this packet; neither a new proof nor independent validation of those papers is asserted.","proof_text":None,"assumptions":["dated primary-source access on 2026-10-10","source verification is separate from mathematical proof audit"],"domain":"probability theory","source":{"source_id":"owner-probability-campaign-w351:P0017:source-status-20261010","url":str(ROOT/"SOURCE_STATUS.json"),"revision":"as-read-2026-10-10","license":"owner-own-work (original dated source-status annotation; public papers attributed)","excerpt":None}})
relations=[
 {"from_key":"w351-L3","to_key":"w351-L2","kind":"depends_on","rationale":"The averaged-constant obstruction uses exactly the isotropic simplex and its edge conditional interval from L2."},
 {"from_key":"w351-L4","to_key":"w351-L2","kind":"depends_on","rationale":"The nonlinear-correlation calculation uses the same T,Y split and the conditional uniform interval from L2."},
 {"from_key":"source-status","to_existing_logical":TARGET,"kind":"cites","rationale":"The existing P0017 card explicitly says current status unverified and records 2026-09-07; this dated annotation supplies subsequently accessed primary publication claims without declaring a theorem."},
 {"from_key":"w351-L1","to_existing_logical":TARGET,"kind":"semantic_association","rationale":"The conditional-variance criterion supplies an additional-hypothesis route to the P0017 Poincare target, with missing uniform dependence and slice hypotheses stated."},
 {"from_key":"w351-L2","to_existing_logical":ATTEMPT,"kind":"semantic_association","rationale":"Both are bounded-scope P0017 attempt records: the old card treats the Gaussian/Hermite case; this draft treats a conditional-fiber obstruction and does not prove general KLS."}
]
bundle={"spec":"mathbrain-draft-v1","author_agent":"w351","bundle_slug":"p0017-conditional-fiber-obstruction-w351-20261010","entries":entries,"relations":relations}
(ROOT/"bundle_001.json").write_text(json.dumps(bundle,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
ends={entry["key"]:entry["statement"] for entry in entries}
existing={TARGET:"OPEN PROBLEM from the Codex campaign ledger (source_says_open; current status unverified; result status attempted_unsolved). Is there a universal positive lower bound for the Euclidean Cheeger constant of every isotropic log-concave probability measure, in every dimension?",ATTEMPT:"ATTEMPT RECORD from the Codex campaign (author-checked by that worker only). Method: Gaussian special case by orthogonal expansion"}
with (ROOT/"RELATION_EVIDENCE.jsonl").open("w",encoding="utf-8") as handle:
    for relation in relations:
        end=relation.get("to_key") or relation["to_existing_logical"]
        handle.write(json.dumps({**relation,"from_end_quote":ends[relation["from_key"]],"to_end_quote":ends.get(end) or existing[end],"existing_end_source":"~/math-brain-build/export/population/nodes.jsonl:7594 or :9049" if end in existing else "same bundle"},ensure_ascii=False)+"\n")
parser=argparse.ArgumentParser()
parser.add_argument("--submit",action="store_true")
args=parser.parse_args()
state={"prepared":True,"submitted":False,"reviewed":"PENDING-w353","ingested":"UNKNOWN-no-receipt","retrievable":"UNKNOWN-no-receipt","live_store_mutated_by_worker":False,"entries":len(entries),"relations":len(relations),"as_of":datetime.now(timezone.utc).isoformat()}
if args.submit:
    claim=json.loads((ROOT/"MESH_CLAIM_RECEIPT.json").read_text(encoding="utf-8"))
    assert claim["acquired"] is True and claim["resource"] == str(INBOX), "named inbox claim required"
    assert datetime.fromisoformat(claim["expires_at"].replace("Z","+00:00")) > datetime.now(timezone.utc), "fresh inbox claim required"
    INBOX.mkdir(parents=True,exist_ok=True)
    final=INBOX/"bundle_001.json"
    part=INBOX/"bundle_001.json.part"
    assert final.resolve().parent == INBOX.resolve() and part.resolve().parent == INBOX.resolve()
    if final.exists() or part.exists():
        raise FileExistsError("Never overwrite another saved submission")
    with part.open("x",encoding="utf-8") as handle:
        handle.write(json.dumps(bundle,ensure_ascii=False,indent=2)+"\n")
    part.rename(final)
    state.update(submitted=True,submitted_path=str(final))
(ROOT/"SUBMISSION_STATE.json").write_text(json.dumps(state,indent=2)+"\n",encoding="utf-8")
print(json.dumps(state))
