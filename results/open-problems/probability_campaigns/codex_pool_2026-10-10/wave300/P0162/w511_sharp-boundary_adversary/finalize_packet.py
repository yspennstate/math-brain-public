"""Finalize measured research deliverables; no live integration or service changes."""
import json
from pathlib import Path

base = Path(__file__).resolve().parent
measure = json.loads((base/"measurements.json").read_text(encoding="utf-8"))
audit = json.loads((base/"affine_audit_measurements.json").read_text(encoding="utf-8"))
delivery = json.loads((base/"DELIVERY_STATE.json").read_text(encoding="utf-8"))
assert delivery["submitted"] and not delivery["reviewed"] and not delivery["ingested"]
bundle = json.loads((base/"bundle_001.json").read_text(encoding="utf-8"))
submitted = json.loads(Path(delivery["submission_path"]).read_text(encoding="utf-8"))
assert bundle == submitted and len(bundle["entries"])==7
assert all(entry["kind"]=="concept" for entry in bundle["entries"])

source_path = base/"SOURCE_STATUS.json"
source = json.loads(source_path.read_text(encoding="utf-8"))
source["local_target_records"] = {"intake_artifact":"SOURCE_RECORDS.json", "read_only_store_artifact":"TARGET_CARDS.json", "exact_nodes_matched":2,
    "open_problem_card":"claim_d7e82bff88909352dff2f23bfcaf7a76446d6bfd14af38c5bda1d5efeb9d9c06",
    "prior_attempt_card":"claim_06b0c09db7e28efc6febd3962e234332a00c2ba45a17792cc4d83fdbc6752fba",
    "prior_attempt_scope":"Real-valued singleton-spectrum obstruction; no full FEI solution recorded in this target card"}
source["primary_sources"].append({"title":"A new bound for the Fourier-Entropy-Influence conjecture","author":"Xiao Han",
    "url":"https://arxiv.org/abs/2312.08271","version":"v2 2025-12-10","scope_read":"Abstract bound with the additional sum_i I_i log(1/I_i) term","verified":True})
source["owner_status_check_limit"] = "Named H/I folders had no matching P0162 text. Relevant recalled prior FEI note still reports full FEI open as of September. The referenced math-open-problems checkout was unavailable at the tested local path. No exhaustive current solved/retired check is certified."
source["current_openness"] = "UNKNOWN"
source["next"] = "Independent referee should check the sharp profile proof; current openness and novelty remain UNKNOWN."
source_path.write_text(json.dumps(source,indent=2,ensure_ascii=False)+"\n",encoding="utf-8")

report = f"""The explicit Boolean bent-plus-point-flip family makes an arbitrary-coordinate FEI restriction charge fail: Delta_i/I_i grows as n+3/ln 2. It also shows that the additive coefficient 2/ln 2 in the known bound Delta_i<=h_2(I_i)+(2/ln 2)I_i is sharp. An independent dictator balances the function and its restrictions without changing the obstruction. Another coordinate remains good, so coordinate selection is the remaining premise in this induction route. Current openness and novelty are UNKNOWN; unrestricted FEI is not solved by this work.

Before the new witness, the targeted prior brain card only excluded a non-Boolean singleton spectrum. The submitted mathematical draft adds an explicit Boolean split obstruction and sharp profile evidence. This is a proposed brain-content improvement; no live recall-quality improvement or live-store ingestion is claimed.

Measured with `python -X utf8 verify_boundary.py`: exact Fourier/influence checks passed 5/5 dimensions; all 256 small Boolean restriction pairs passed. Specified-split ratios were 4.8676687468 at n=2 and 132.3280851227 at n=128, while global H/I tends to 2. Maximum entropy identity error was 8.53e-16; the run took {measure['wall_seconds']:.6f} seconds. With `python -X utf8 verify_affine_audit.py`, all 372 affine subspaces through ambient dimension 4 passed in {audit['wall_seconds']:.6f} seconds, with entropy formula error 0. Four paired-proof KEEP verdicts are in AUDIT_W510.md and AUDIT_W510.jsonl.

Seven concept/draft entries were submitted as ~/math-brain-inbox/w511/bundle_001.json. They are not reviewed, ingested, or verified retrievable. Own mathematical claims still need w512's independent referee check. The first mesh review request failed because w512 was not registered; REVIEW_PACKET.md is the durable handoff. No formal theorem receipt is claimed.

Apply: the validating coordinator reviews REVIEW_PACKET.md and the submitted bundle, ingests only accepted entries with the draft labels preserved, and records retrieval separately. The local hook proposal can be filed using patches/01_math_hook_proposal.diff; it is a proposal with fire/silent cases, not a tested deployed hook. No live code patch or live recall control was changed.

NEXT: w512 independently checks C001-C004, especially the analytic sharpness expansion; the coordinator then records review, ingestion and retrieval receipts for accepted draft entries.
"""
(base/"REPORT.md").write_text(report,encoding="utf-8")

status = f"""STATE: NEEDS_REVIEW
NEXT: w512 independently checks C001-C004 and returns a verdict path; the validating coordinator ingests accepted draft entries and confirms retrieval.

2026-10-10: Read PRIMARY_DIRECTIVE.md, exact P0162 sources, targeted prior records, relevant recall memories and the perceptron proof-completion scar. No assigned hook audit and no open vote for this worker. Current openness and novelty remain UNKNOWN.
2026-10-10: Saved independent Boolean bent-plus-point-flip obstruction before reading the paired proof. Proved a divergent specified-split ratio, sharp 2-bit absolute bound and sharp additive coefficient in the known binary-entropy profile, subject to independent referee check.
2026-10-10: Boundary run passed 5/5 exact Fourier dimensions and 256/256 split pairs in {measure['wall_seconds']:.6f}s, with maximum identity error 8.53e-16; grouped n=128 ratio 132.3280851227. A serialization typo was fixed before the passing run.
2026-10-10: Audited w510 C001-C004 with four KEEP verdicts and 372/372 exact affine checks in {audit['wall_seconds']:.6f}s. Saved AUDIT_W510.md/jsonl, CLAIMS.jsonl, SOURCE_STATUS.json and REVIEW_PACKET.md.
2026-10-10: Submitted 7 concept/draft entries to the expressly authorized math-brain inbox. DELIVERY_STATE.json separates submission, review, ingestion and retrieval; latter three remain pending. Hook proposal and live-path unified diff are saved locally. No live code or store was changed.
2026-10-10: w510 received lane and review-packet messages. The w512 mesh request was rejected as unregistered; the local review packet remains available. Deliverables complete and measured; referee review pending.
"""
(base/"STATUS.md").write_text(status,encoding="utf-8")

progress = {"event":"P0162 sharp Boolean split profile saved; 256 split checks and 372 affine audits passed; 7 concept drafts submitted, referee and ingestion pending",
            "agent":"w511","row":"S1.P0162.w511.C003","evidence":str(base/"REPORT.md")}
(base/"PROGRESS_EVENT.json").write_text(json.dumps(progress,indent=2)+"\n",encoding="utf-8")
required = ["STATUS.md","SOURCE_STATUS.json","ATTEMPT.md","CLAIMS.jsonl","REVIEW_PACKET.md","REPORT.md","DELIVERY_STATE.json","bundle_001.json","AUDIT_W510.jsonl","measurements.json","affine_audit_measurements.json"]
assert all((base/name).is_file() and (base/name).stat().st_size>0 for name in required)
for filename in ["CLAIMS.jsonl","AUDIT_W510.jsonl","SOURCE_ROWS.jsonl"]:
    for line in (base/filename).read_text(encoding="utf-8-sig").splitlines():
        json.loads(line)
assert (base/"STATUS.md").read_text(encoding="utf-8").splitlines()[0]=="STATE: NEEDS_REVIEW"
print(json.dumps({"status":"NEEDS_REVIEW","required_artifacts":len(required),"math_claims":4,"paired_keep_verdicts":4,
                  "submitted_concept_entries":7,"independent_referee":"pending","live_store_modified":False},indent=2))
