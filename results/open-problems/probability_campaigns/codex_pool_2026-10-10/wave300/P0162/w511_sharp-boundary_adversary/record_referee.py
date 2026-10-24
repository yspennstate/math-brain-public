"""Record the named referee receipt and submit a proof-bearing successor draft."""
import json
from pathlib import Path

base = Path(__file__).resolve().parent
verdict_path = Path("~/brain_workers/w512/VERDICTS.jsonl")
verdicts = [json.loads(line) for line in verdict_path.read_text(encoding="utf-8-sig").splitlines() if line.strip()]
keeps = {row["target"]:row for row in verdicts if row["target"].startswith("P0162-w511-")}
expected = {f"P0162-w511-C00{i}" for i in range(1,5)}
assert set(keeps)==expected and all(row["verdict"]=="KEEP" and row["reviewer"]=="w512" for row in keeps.values())
receipt = {"reviewer":"w512","receipt_path":str(verdict_path),"claims":list(keeps.values()),
           "independent_mathematical_review":"KEEP 4/4","formal_verification":False,
           "scope":"Exact special cases and auxiliary obstructions; no full FEI or novelty certification"}
(base/"REVIEW_RECEIPT.json").write_text(json.dumps(receipt,indent=2)+"\n",encoding="utf-8")
claim_path = base/"CLAIMS.jsonl"
rows = [json.loads(line) for line in claim_path.read_text(encoding="utf-8").splitlines() if line.strip()]
for row in rows:
    assert row["id"] in expected
    row["status"] = "independently checked proof"
    row["independent_reviewer"] = {"agent":"w512","verdict":"KEEP","receipt":"REVIEW_RECEIPT.json"}
    row["review_state"] = "independently checked; validating coordinator review still required for ingestion"
    row["remaining_gap"] = keeps[row["id"]]["gap"] + " No formal theorem receipt; novelty UNKNOWN."
claim_path.write_text("".join(json.dumps(row,ensure_ascii=False)+"\n" for row in rows),encoding="utf-8")

bundle = json.loads((base/"bundle_001.json").read_text(encoding="utf-8"))
bundle["bundle_slug"] = "fei-coordinate-restriction-sharp-boundary-reviewed-20261010"
old_prefix = "DRAFT: independent mathematical referee review pending; no novelty claim. "
proofs = {
    "split-profile": "For restriction coefficients a,b set w=(a^2+b^2)/2, q=a^2/(a^2+b^2), r=(a-b)^2/[2(a^2+b^2)]. The exact increment is sum w[1+h_2(r)-h_2(q)]. If u=|a^2-b^2|/(a^2+b^2), integration of atanh(u)<=u/sqrt(1-u^2) gives 1-h_2(q)<=(1-sqrt(1-u^2))/ln 2<=2r/ln 2. Since sum w=1 and sum wr=delta, Jensen gives the asserted upper bound. The explicit point-flip family supplies an unbounded Delta/delta ratio.",
    "point-flip": "Each quadratic two-bit factor has Fourier coefficients (1,1,1,-1)/2; tensoring gives ghat=s sigma, with s=2^(-n/2) and signs summing to 1/s. The point indicator has coefficient p at every index. The selector's Fourier blocks are A=s sigma-p and B=p, so I_z=p. The normalized A-block distribution P_A relative to uniform U has chi-square divergence 4p/(1-p). Entropy chain expansion gives Delta=h_2(p)-(1-p)D_2(P_A||U)+D_2(P_h||U)/2. Using D_2<=chi-square/ln 2 and h_2(p)>=np gives Delta/p>=n-4/ln 2. Each old influence becomes 1/2+p, giving I(F)=n/2+(n+1)p and H(F)/I(F)->2.",
    "profile-sharpness": "Put s=sqrt(p) and L_k(s)=(1/2)sum_{sigma=+1,-1}(1+sigma s)(1-k sigma s)^2 log_2((1-k sigma s)^2). This is even analytic near zero, and its Taylor expansion is (3k^2-2k)s^2/ln 2+O(s^4). Exact sign counts yield H(h)=n-L_2(s) and H(F)=n(1+p)-L_1(s). Thus Delta/p=n+3/ln 2+O(p), whereas h_2(p)/p=n+1/ln 2+O(p), proving the sharp coefficient. Multiplication by an independent dictator simply shifts Fourier indices, preserving entropy and selector influence, and makes the functions balanced.",
    "absolute-two": "For the two restriction coefficient vectors a,b, put w=(a^2+b^2)/2, q=a^2/(a^2+b^2), r=(a-b)^2/[2(a^2+b^2)], omitting zero weights. The two-output entropy chain rule gives Delta=sum w[1+h_2(r)-h_2(q)]. Weights sum to 1 and both binary entropies lie in [0,1], giving 0<=Delta<=2. The stated selector has four coefficients of magnitude 1/2 and restricted spectra concentrated at one character, attaining Delta=2.",
    "spectrum-l1": "The quadratic bent function has Fourier coefficients s sigma, with N_+=(1/p+1/s)/2 positive and N_-=(1/p-1/s)/2 negative signs. The point flip changes each coefficient by -2p. Hence the squared-coefficient difference has absolute value 4p|s sigma-p|. Summing these two sign classes gives 4sqrt(p)(1-p). Dividing by the selector influence p yields 4(1-p)/sqrt(p)."
}
for entry in bundle["entries"]:
    assert entry["statement"].startswith(old_prefix)
    entry["statement"] = entry["statement"][len(old_prefix):]
    if entry["key"] in proofs:
        entry["kind"] = "lemma"
        entry["proof_text"] = proofs[entry["key"]]
        entry["title"] = entry["title"].removeprefix("Draft: ")
    else:
        entry["statement"] = "Reviewed mathematical route note; no novelty claim. " + entry["statement"]
    entry["source"]["revision"] = "independently-reviewed-campaign-draft-2026-10-10"
assert len(proofs)==5 and len(bundle["entries"])==7
(base/"bundle_002.json").write_text(json.dumps(bundle,indent=2,ensure_ascii=False)+"\n",encoding="utf-8")
inbox = Path("~/math-brain-inbox/w511")
destination = inbox/"bundle_002.json"
payload = (base/"bundle_002.json").read_text(encoding="utf-8")
if destination.exists():
    assert destination.read_text(encoding="utf-8")==payload, "Refuse to overwrite a different draft"
else:
    partial = inbox/"bundle_002.json.part"
    with partial.open("x",encoding="utf-8") as out:
        out.write(payload)
    partial.rename(destination)

delivery_path = base/"DELIVERY_STATE.json"
delivery = json.loads(delivery_path.read_text(encoding="utf-8"))
delivery.update({"reviewed":True,"reviewer":"w512","review_receipt":"REVIEW_RECEIPT.json",
    "review_state":"4/4 mathematical claims KEEP; coordinator integration review pending",
    "submission_path":str(destination),"supersedes_submission":"bundle_001.json",
    "entry_kind":"5 proof-bearing lemmas and 2 concepts in a coordinator DRAFT",
    "ingested":False,"retrievable":False,"ingestion_observation":"No ingestion or retrieval receipt is claimed by this worker"})
delivery_path.write_text(json.dumps(delivery,indent=2)+"\n",encoding="utf-8")
source_path = base/"SOURCE_STATUS.json"
source = json.loads(source_path.read_text(encoding="utf-8"))
source["mathematical_proof_status"] = "C001-C004 independently checked by named referee w512, 4 KEEP verdicts; no formal theorem receipt"
source["next"] = "Coordinator validates and ingests reviewed bundle_002; confirm retrieval separately. Openness and novelty remain UNKNOWN."
source_path.write_text(json.dumps(source,indent=2)+"\n",encoding="utf-8")

for filename in ["REPORT.md","REVIEW_PACKET.md"]:
    path = base/filename
    body = path.read_text(encoding="utf-8")
    body = body.replace("Own mathematical claims still need w512's independent referee check.", "w512 independently kept all four own mathematical claims; REVIEW_RECEIPT.json identifies the exact assertions and checks.")
    body = body.replace("independent review pending", "independent review received")
    body = body.replace("They are not reviewed, ingested, or verified retrievable.", "Their mathematical claims now have independent referee KEEP verdicts; ingestion and retrieval remain unconfirmed.")
    body = body.replace("~/math-brain-inbox/w511/bundle_001.json", "~/math-brain-inbox/w511/bundle_002.json (the reviewed successor to bundle_001)")
    body += "\n2026-10-10 referee receipt: w512 KEEP C001-C004 after independent analytic rederivation and bounded checks. Reviewed bundle_002 contains five proof-bearing lemmas and two concepts, superseding the initial seven concept drafts. The validating coordinator should use bundle_002; source/current-openness/novelty and integration checks remain separate.\n"
    path.write_text(body,encoding="utf-8")
status_path = base/"STATUS.md"
status = status_path.read_text(encoding="utf-8")
lines = status.splitlines()
lines[1] = "NEXT: Validating coordinator reviews and ingests bundle_002 using w512's 4 KEEP receipts, then confirms retrieval; full FEI and novelty remain unclaimed."
status_path.write_text("\n".join(lines)+"\n2026-10-10: Received w512's exact KEEP verdicts for C001-C004. Recorded REVIEW_RECEIPT.json and independently checked claim status. Submitted proof-bearing bundle_002, superseding the initial concept draft; coordinator ingestion and retrieval remain unconfirmed.\n",encoding="utf-8")
progress_path = base/"PROGRESS_EVENT.json"
progress = json.loads(progress_path.read_text(encoding="utf-8"))
progress["event"] = "P0162 sharp Boolean split profile: w512 kept 4/4 claims; 256 split checks and 372 affine audits passed; reviewed 7-entry draft submitted, ingestion pending"
progress_path.write_text(json.dumps(progress,indent=2)+"\n",encoding="utf-8")
print(json.dumps({"independently_checked_claims":4,"referee":"w512","submitted_reviewed_draft":str(destination),
                  "proof_bearing_lemmas":5,"concepts":2,"state":"NEEDS_REVIEW","ingestion":"unconfirmed"},indent=2))
