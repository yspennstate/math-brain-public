"""Make local reports reflect actual review, lookup and handoff receipts."""
import json
from pathlib import Path

folder = Path("~/brain_workers/w412")
claims = [json.loads(line) for line in (folder/"CLAIMS.jsonl").read_text(encoding="utf-8").splitlines() if line]
for claim in claims:
    claim["independent_reviewer"] = "w413; scoped KEEP in ~/brain_workers/w413/REVIEW_PACKET.md, 2026-10-10"
    claim["review_receipt"] = "~/brain_workers/w412/INDEPENDENT_REVIEW_RECEIPT.json"
    if claim["id"] == "w412-C0017-S0":
        claim["remaining_gap"] = "Current accepted proof status is UNKNOWN; primary claimed proofs are unassessed. Historical source and exact target have been recovered."
        claim["review_state"] = "independently checked source guard; no theorem assertion"
    else:
        claim["status"] = "independently checked proof"
        claim["review_state"] = "mathematical KEEP; served-model/different-model integration gate unestablished"
        if claim["id"] == "w412-C0017-L1":
            claim["remaining_gap"] = "No gap found by the assigned referee in the stated local conditional reduction. C0017 still needs actual square-lattice joint conditional Cardy limits, trace convergence and lifetime extension. Different-model gate for store promotion is unestablished."
        else:
            claim["remaining_gap"] = "No gap found by the assigned referee in the explicit deterministic counterexample. It refutes only the general one-observable inference. Different-model gate for store promotion is unestablished."
(folder/"CLAIMS.jsonl").write_text("".join(json.dumps(c, ensure_ascii=False)+"\n" for c in claims), encoding="utf-8")

status = json.loads((folder/"SOURCE_STATUS.json").read_text(encoding="utf-8"))
status["local_work_check"]["owner_folder"] = "The named owner's percolation project README concerns the Benjamini-Schramm nonuniqueness conjecture, not square-lattice conformal invariance. Its cited Open problem project/solved_register.md had no target match in the bounded C0017/conformal-square-percolation search. This is not an exhaustive global solved-work certificate."
status["local_work_check"]["canonical_store_check"] = "The named math-research-brain repository's local directories contain audits/evaluation/tooling; only audit-snapshot SQLite filenames were located by the bounded store lookup. They were not opened, and evaluation material was not read. A current canonical runtime store for that repository was not recovered."
live = json.loads((folder/"LIVE_TARGET_RECEIPT.json").read_text(encoding="utf-8"))
status["local_work_check"]["live_population_check"] = {"receipt": "LIVE_TARGET_RECEIPT.json", "matched_ids": [r["id"] for r in live["rows"]], "error": live["error"], "scope": "Read-only, exact-ID lookup of the target and attempt cards; no global store export or proof certification."}
status["disposition"] = "Exact historical target recovered; present openness UNKNOWN; no novelty claim. w413 kept the local conditional derivation and deterministic counterexample. Brain entries remain concept/draft material pending the served-model/different-model integration gate."
(folder/"SOURCE_STATUS.json").write_text(json.dumps(status, ensure_ascii=False, indent=2)+"\n", encoding="utf-8")

attempt = (folder/"ATTEMPT.md").read_text(encoding="utf-8")
attempt = attempt.replace("C0017 is not proved; independent review by w413 is pending.", "C0017 is not proved. w413 independently kept the conditional lemma and deterministic counterexample; served-model/different-model integration evidence remains unavailable.")
attempt = attempt.replace("## Review request", "## Independent review receipt")
attempt = attempt.replace("w413: independently check the inverse-observable semimartingale step, quotient-Itô signs, signed-measure subtraction, localization/lifetime scope, and the explicit deterministic counterexample.", "w413 independently reproduced the inverse-observable semimartingale step, quotient-Itô identity, signed-measure subtraction and deterministic counterexample, and kept L1 and X1 at their conditional/finite scope. See INDEPENDENT_REVIEW_RECEIPT.json.")
attempt = attempt.replace("NEXT: Check the primary target page and then inspect w411's actual replacement/interpolation proof for the missing accumulated-defect estimate.", "NEXT: Establish joint conditional Cardy limits for actual square-lattice observables in random slit domains; w411's route separately needs a specified cell comparison with vanishing signed defect.")
(folder/"ATTEMPT.md").write_text(attempt, encoding="utf-8")
print(json.dumps({"claims": len(claims), "mathematically_kept_claims": [c["id"] for c in claims], "live_population_matches": len(live["rows"]), "canonical_runtime_store": "not recovered; no snapshots/evaluation contents opened"}), flush=True)
