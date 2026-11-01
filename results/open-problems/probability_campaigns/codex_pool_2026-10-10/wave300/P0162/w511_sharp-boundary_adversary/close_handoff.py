"""Close the reviewed packet and post the expressly requested progress event."""
import json
import subprocess
import sys
from pathlib import Path

base = Path(__file__).resolve().parent
measure = json.loads((base/"measurements.json").read_text(encoding="utf-8"))
audit = json.loads((base/"affine_audit_measurements.json").read_text(encoding="utf-8"))
review = json.loads((base/"REVIEW_RECEIPT.json").read_text(encoding="utf-8"))
delivery = json.loads((base/"DELIVERY_STATE.json").read_text(encoding="utf-8"))
assert len(review["claims"])==4 and delivery["reviewed"] and delivery["submitted"]
assert not delivery["ingested"] and not delivery["retrievable"]

report = f"""The explicit Boolean bent-plus-point-flip family has an unbounded entropy increment divided by influence at its selector coordinate. It also proves sharpness of the additive coefficient 2/ln 2 in the known restriction bound Delta_i<=h_2(I_i)+(2/ln 2)I_i. An independent dictator balances the function and both restrictions while preserving this obstruction. Other coordinates remain good, so the existential coordinate-selection route is still unresolved by this work. Current openness and novelty remain UNKNOWN.

w512 independently kept all four new mathematical claims after analytic rederivation and bounded checks. REVIEW_RECEIPT.json identifies the exact claims and the referee's reproductions. The paired affine-indicator C001-C004 also received four independent KEEP verdicts from this worker, with evidence in AUDIT_W510.md/jsonl. No formal theorem receipt is claimed.

Measured with `python -X utf8 verify_boundary.py`: exact Fourier/influence checks passed 5/5 dimensions and all 256 small Boolean split pairs passed, in {measure['wall_seconds']:.6f}s. The split ratio was 4.8676687468 at n=2 and 132.3280851227 at n=128, while global H/I approaches 2. Maximum entropy identity error was 8.53e-16. `python -X utf8 verify_affine_audit.py` passed all 372 affine cases through ambient dimension 4 in {audit['wall_seconds']:.6f}s, with entropy formula error 0.

The targeted prior brain card only excluded a non-Boolean singleton spectrum. The proposed content change adds an explicit Boolean obstruction and its sharp restriction profile. It is a measured mathematical result and a proposed brain-content improvement; no live recall-quality gain is claimed.

Apply: the validating coordinator uses ~/math-brain-inbox/w511/bundle_002.json with REVIEW_RECEIPT.json. This reviewed successor to bundle_001 contains five proof-bearing lemmas and two concepts. Submission and independent review are recorded; ingestion and retrieval are unconfirmed. The local hook proposal and its fire/silent cases are in math-w511.jsonl and patches/01_math_hook_proposal.diff. That patch files a proposal; it does not deploy a hook. No live code or store was modified by this worker.

NEXT: Coordinator validates and ingests bundle_002, records its integration receipt, and verifies retrieval; keep full FEI and novelty unclaimed.
"""
(base/"REPORT.md").write_text(report,encoding="utf-8")

packet = """# P0162 reviewed boundary packet

The named referee w512 independently kept C001-C004. Read REVIEW_RECEIPT.json for the exact receipt and ATTEMPT.md for the complete author proofs. CLAIMS.jsonl records independently checked proof status, hypotheses, sources and remaining scope limitations. INDEPENDENT_CHECKPOINT.json records the independent derivation before reading the paired proof.

C001 gives a Boolean prescribed-coordinate obstruction Delta/p>=n-4/ln 2 and its balanced wrapper. C002 proves the sharp absolute two-bit increment bound. C003 independently rederives the known binary-entropy envelope and proves its additive coefficient is sharp within Boolean functions. C004 gives the exact squared-spectrum L1 obstruction. These statements leave full FEI and the existential coordinate-selection route unresolved by this work; novelty and present openness are UNKNOWN.

The referee independently checked the bent Fourier coefficients, sign counts, normalized chi-square calculation, entropy chain identity, derivative comparison, and analytic L_k expansion. The receipt also records separate bounded numerical reproductions. This is independent mathematical checking, not a formal theorem receipt.

Reproduce the two small experiments with `python -X utf8 verify_boundary.py` and `python -X utf8 verify_affine_audit.py`. Their gates and measurements are saved. The first passed 5 exact Fourier dimensions and all 256 small split pairs; the second passed every one of 372 affine cases in dimensions 1 through 4. AUDIT_W510.md/jsonl has four independent KEEP verdicts for the paired affine proof, without promoting the class theorem to unrestricted FEI.

Use bundle_002.json, the reviewed successor to the initial concept draft. It contains five proof-bearing lemmas and two concepts, all with the accepted owner-own-work source tag and complete mathematical statements. Relations have explicit ends within the bundle. The validating coordinator handles source validation and ingestion; this worker must not run the live integrator.

DELIVERY_STATE.json separates submission, independent review, ingestion and retrieval. Only the first two have receipts. The local hook proposal has a narrow fire case, a silent case and a live-path unified diff; hook deployment remains a separate unmeasured proposal.

NEXT: Coordinator ingests accepted bundle_002 entries and verifies that the resulting cards can be retrieved.
"""
(base/"REVIEW_PACKET.md").write_text(packet,encoding="utf-8")

hook_path = base/"math-w511.jsonl"
hook = json.loads(hook_path.read_text(encoding="utf-8"))
hook["evidence"] = "~/brain_workers/w511/ATTEMPT.md C001; measurements.json n=128 split ratio 132.3280851227; REVIEW_RECEIPT.json w512 KEEP C001-C004"
hook_path.write_text(json.dumps(hook)+"\n",encoding="utf-8")
live = "~/primary_directive/hooks1000/proposals/math-w511.jsonl"
(base/"patches"/"01_math_hook_proposal.diff").write_text(
    f"diff --git a/{live} b/{live}\nnew file mode 100644\n--- a/{live}\n+++ b/{live}\n@@ -0,0 +1 @@\n+"+json.dumps(hook)+"\n",encoding="utf-8")

event = json.loads((base/"PROGRESS_EVENT.json").read_text(encoding="utf-8"))
command = [sys.executable,"-X","utf8","~/primary_directive/pd_progress.py",
    "--event",event["event"],"--agent",event["agent"],"--row",event["row"],"--evidence",event["evidence"]]
# The inspected --event branch only appends the authorized event and returns;
# it does not build reports, read test banks, send email or manage processes.
posted = subprocess.run(command,capture_output=True,text=True,encoding="utf-8",creationflags=0x08000000)
(base/"PROGRESS_RECEIPT.json").write_text(json.dumps({"command":command,"exit_code":posted.returncode,
    "stdout":posted.stdout,"stderr":posted.stderr,"event_logged":posted.returncode==0},indent=2)+"\n",encoding="utf-8")
with (base/"STATUS.md").open("a",encoding="utf-8") as out:
    out.write("2026-10-10: Final handoff cleaned around the received referee verdicts; official progress event "
              +("logged" if posted.returncode==0 else "failed; see PROGRESS_RECEIPT.json")+". Coordinator ingestion and retrieval are the next step.\n")

assert (base/"STATUS.md").read_text(encoding="utf-8").splitlines()[0]=="STATE: NEEDS_REVIEW"
bundle = json.loads((base/"bundle_002.json").read_text(encoding="utf-8"))
assert json.loads(Path(delivery["submission_path"]).read_text(encoding="utf-8"))==bundle
assert sum(entry["kind"]=="lemma" and bool(entry["proof_text"]) for entry in bundle["entries"])==5
claims = [json.loads(line) for line in (base/"CLAIMS.jsonl").read_text(encoding="utf-8").splitlines()]
assert all(row["status"]=="independently checked proof" for row in claims)
print(json.dumps({"state":"NEEDS_REVIEW","referee_keeps":4,"boundary_checks":256,"affine_checks":372,
    "reviewed_entries_submitted":7,"progress_event_logged":posted.returncode==0,"ingestion":"unconfirmed"},indent=2))
