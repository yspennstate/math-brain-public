"""Prepare C0029 review artifacts inside w568; stage only with --submit."""
from __future__ import annotations

import argparse
import copy
import datetime as dt
import difflib
import hashlib
import itertools
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent
OLD_LOGICAL = "math:probability.random-matrices:attempt-c0029-spielman-teng-conjecture-on-the-least-singular-value-of-bernoulli-matr"
TARGET_LOGICAL = "math:probability.random-matrices:open-problem-c0029-spielman-teng-conjecture-on-the-least-singular-value-of-bernoulli-matr"


def write(name: str, value: object) -> None:
    p = ROOT / name
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(json.dumps(value, ensure_ascii=False, indent=2)+"\n", encoding="utf-8")


def append_claim(row: dict) -> None:
    p = ROOT / "CLAIMS.jsonl"
    existing = {json.loads(line)["id"] for line in p.read_text(encoding="utf-8").splitlines() if line.strip()}
    if row["id"] not in existing:
        with p.open("a", encoding="utf-8") as out:
            out.write(json.dumps(row, ensure_ascii=False)+"\n")


def sha(p: Path) -> str:
    return hashlib.sha256(p.read_bytes()).hexdigest()


def prepare() -> None:
    source = Path("~/<private-repo>/06_math_research/probability_1000_intake_claude_20260907/attempts.jsonl")
    with source.open(encoding="utf-8") as handle:
        original_line = next(itertools.islice(handle, 22, 23))
    original = json.loads(original_line)
    assert original["problem_id"] == "C0029" and original["attempt_id"] == "C0029-A001"
    corrected = copy.deepcopy(original)
    corrected["key_identity"] = "Real Gaussian hard-edge LIMIT: for each fixed t>=0, P(sqrt(n) s_min(G_n)<=t)=1-exp(-t-t^2/2)+o(1) as n tends to infinity. This is not an exact finite-n identity."
    corrected["result"] = "The limiting real-Gaussian law has slope one at zero. At finite n=1 the CDF is erf(t/sqrt(2)), with slope sqrt(2/pi). Tao--Vu Theorem 1.1 gives the real formula with an o(1) error, and Theorem 1.3 gives a uniform polynomial error under its moment hypotheses. Sah--Sahasrabudhe--Sawhney Theorem 1.1 supplies coefficient 1+O((log n)^(-1/16)) and an exponential remainder, rather than the exact coefficient one. The original exact-coefficient route remains incomplete; no improvement or solved claim is inferred."
    corrected["original_key_identity_before_source_correction"] = original["key_identity"]
    corrected["original_result_before_source_correction"] = original["result"]
    corrected["source_correction"] = {"author": "w568", "date": "2026-10-10", "status": "DRAFT, w569 independent review pending", "source": "https://arxiv.org/pdf/0903.0614", "locator": "Theorem 1.1, equations (1)-(2), printed page 3", "counterexample": "n=1 right derivative sqrt(2/pi) differs from one"}
    replacement = json.dumps(corrected, ensure_ascii=False, sort_keys=True)+"\n"
    relative = "06_math_research/probability_1000_intake_claude_20260907/attempts.jsonl"
    diff = "".join(difflib.unified_diff([original_line], [replacement], fromfile="a/"+relative, tofile="b/"+relative, n=0)).replace("@@ -1 +1 @@", "@@ -23 +23 @@")
    (ROOT / "patches").mkdir(exist_ok=True)
    (ROOT / "patches/01_C0029_gaussian_limit.diff").write_text(diff, encoding="utf-8")
    write("SOURCE_CORRECTION.json", {"source_path": str(source), "line": 23, "expected_original_line_sha256": hashlib.sha256(original_line.encode("utf-8")).hexdigest(), "original": original, "corrected_draft": corrected, "brain_node_id": "claim_cbd6e1bc44ea67c88a3ad2112abab63bbfcf63f991be2eeccb063fdba514f1fa", "brain_logical_id": OLD_LOGICAL, "original_brain_quote": "Edelman's exact law gives P(sqrt n s_n <= t) = 1 - e^{-t^2/2 - t}", "primary_source_quote": "Limiting distributions for gaussian models", "primary_locator": "Tao--Vu 0903.0614, Theorem 1.1, printed page 3; real case has +o(1)", "review_state": "DRAFT", "store_mutation": False})

    obstruction = {"id": "w568-C0029-obstruction-003", "exact_statement": "Let F(t)=1-exp(-t-t^2/2) for t>=0, eta_n=(log(n+e))^(-1/16), a_n=exp(-sqrt(n)), q_n=2^(-n), m_n=eta_n F(a_n)/2, and G_n(t)=q_n+(1-q_n)[(1-m_n)F(t)+m_n 1_{t>=a_n}] for t>=0, with G_n(t)=0 for t<0. G_n is a CDF with G_n(0)=q_n, |G_n(t)-F(t)|<=(eta_n/2)F(t)+q_n, and G_n(t)<=(3/2)t+q_n. For every fixed d>0, G_n(t)<=t for all t>=n^(-d) once n is sufficiently large depending on d. For large n, G_n(a_n)-a_n>=eta_n a_n/16; thus no fixed C,c>0 give G_n(t)<=t+C exp(-cn) uniformly in t and all large n.", "assumptions": ["n is a positive integer", "t>=0", "d>0 is fixed before the dimension threshold", "G_n is an artificial scalar law; no iid Bernoulli realization is asserted", "F is a limiting reference, not a finite-n Gaussian matrix CDF"], "source": {"tag": "owner-own-work:w568:C0029-scalar-obstruction", "path": str(ROOT / "OBSTRUCTION_PROOF.md")}, "proof_or_counterexample": "Complete elementary mixture and derivative proof in OBSTRUCTION_PROOF.md.", "independent_reviewer": "w569 pending; referee's own new results require w572", "remaining_gap": "Independent mathematical check and response-side served-model/account evidence pending. The original Bernoulli coefficient-one conjecture remains unresolved by this result.", "status": "proved special case", "promotion_status": "DRAFT concept only"}
    append_claim(obstruction)

    peer_files = [ROOT / "review_inputs/w567_ATTEMPT.md", ROOT / "review_inputs/w567_CLAIMS.jsonl"]
    peer_claim = next(json.loads(line) for line in peer_files[1].read_text(encoding="utf-8").splitlines() if "C0029-w567-L1" in line)
    audit = {"candidate": "C0029", "auditor": "w568", "reviewed_snapshot_sha256": {str(p): sha(p) for p in peer_files}, "order": "ATTEMPT.md was saved before reading any w567 proof; the paired inputs were then frozen and read.", "verdict": "KEEP elementary scope; full-target gap remains", "checks": [{"claim": "C0029-w567-L1", "statement": peer_claim["statement"], "verdict": "KEEP_SCOPED", "independent_derivation": "For n>=2 condition on row 1. Row 2 is uniform on 2^n sign vectors, and precisely r and -r are proportional. They are distinct, so the probability is 2^(1-n). Row dependence forces singularity. This is a lower bound only."}, {"claim": "arithmetic separation", "statement": "For nonsingular sign B of order n>=2, s_min(B)>=alpha_n=2^(n-1)((n-1)/n^2)^((n-1)/2). For 0<=t<sqrt(n)alpha_n, the small-singular-value event is exactly singularity.", "verdict": "KEEP_SCOPED", "independent_derivation": "Subtract the first row from each other row and factor a 2 from each of those n-1 rows: the nonzero determinant is a multiple of 2^(n-1). Frobenius norm squared is n^2. AM-GM bounds the product of the largest n-1 singular values by (n^2/(n-1))^((n-1)/2); division gives alpha_n. Use the strict threshold as stated. This needs no random-row product."}, {"claim": "extension from all small t to all t", "verdict": "FIX_SCOPE_EXPLANATION", "why": "Adjusting exponential constants covers finitely many dimensions, but does not by itself cover a fixed interval between the historical small-t range and t=1. A sufficient extra input is uniform fixed-scale universality plus F(t)<t; Tao--Vu Theorem 1.3 provides that input. The modern source already states the all-t target, so this is an omitted equivalence argument, not a contradiction to the target."}], "hardest_gap": "sqrt(n)alpha_n/exp(-sqrt(n)) tends to zero. Arithmetic separation therefore leaves the intermediate window. A Bernoulli-specific one-sided comparison with the actual finite-n Gaussian CDF, or control of positive error by its coefficient-one slack, is still needed.", "countermodel": str(ROOT / "OBSTRUCTION_PROOF.md"), "formal_check": None, "served_model_acceptance_gate": "NOT PASSED: no response-side identity evidence available for this author/auditor; scoped checks are not an admission receipt", "full_problem_solved": False}
    write("AUDIT_W567.json", audit)
    for number, check in enumerate(audit["checks"][:2], 4):
        append_claim({"id": f"w568-C0029-audit-{number:03d}", "exact_statement": check["statement"], "assumptions": ["n>=2", "uniform independent sign entries for the probability lower bound", "nonsingular deterministic sign matrix for arithmetic separation"], "source": {"path": str(peer_files[0]), "sha256": sha(peer_files[0])}, "proof_or_counterexample": check["independent_derivation"], "independent_reviewer": "w568 scoped audit; w569 acceptance pending", "remaining_gap": audit["hardest_gap"], "status": "proved special case", "acceptance_gate": "pending served identity and referee review"})

    status = json.loads((ROOT / "SOURCE_STATUS.json").read_text(encoding="utf-8"))
    status["known_primary_result"].update(inspected_text_url="https://arxiv.org/html/2405.20308v2", inspected_text_version="v2 verified: equation (2), Theorems 1.1 and 1.2")
    status["primary_sources"] = [{"url": "https://arxiv.org/pdf/1109.3343", "locator": "Section 7, printed p.53 (PDF page index 52)", "role": "The exact historical C0029 target; iid symmetric Bernoulli, large n, small t"}, {"url": "https://arxiv.org/pdf/math/0212413", "locator": "Conjecture 2, printed p.605 (PDF index 8)", "role": "Original ICM statement in inverse-norm notation; modern source fixes dimension notation"}, {"url": "https://arxiv.org/pdf/0903.0614", "locator": "Theorem 1.1 equations (1)-(2), printed p.3; Conjecture 1.2 and Theorem 1.3", "role": "Real Gaussian law is a limit; uniform polynomial comparison includes an error"}, {"url": "https://arxiv.org/html/2405.20308v2", "locator": "Introduction equation (2), Theorems 1.1-1.2", "role": "Coefficient 1+o(1), not exact one; comparison uses finite-n Gaussian CDF"}]
    status["local_status"] = "Recovered problems.jsonl:29 and attempts.jsonl:23; H/I and Lean exact-ID searches found no extra C0029 proof; Team O has no target row. Checked the two exact C0029 export cards. Owner-wide retirement status was not independently certified; current openness remains UNKNOWN."
    status["historical_quantifiers"] = "There exist b in (0,1), N and a fixed t0>0 with P(sqrt(n)s_min<=t)<=t+b^n for all n>=N and 0<=t<=t0. The modern primary statement uses all t>=0."
    status["source_hash_scope"] = "Local input line and frozen proof hashes are recorded. Web source locators were read, but no PDF-byte hash or formal proof receipt is claimed. Bundle/store digests and seals are left to the coordinator."
    status["paired_scope"] = audit["verdict"]
    write("SOURCE_STATUS.json", status)

    bundle = {"spec": "mathbrain-draft-v1", "author_agent": "w568", "bundle_slug": "c0029-scalar-obstruction-and-gaussian-limit-correction", "review_state": "DRAFT", "entries": [{"key": "c0029-real-gaussian-scope", "namespace": "probability.random-matrices", "logical_name": "c0029-real-gaussian-finite-versus-limiting-law", "kind": "concept", "title": "C0029 source correction: real Gaussian finite and limiting laws", "statement": "DRAFT source correction, independent review pending. For an n by n real Gaussian matrix with independent N(0,1) entries, the CDF of sqrt(n)s_min converges, at each fixed t>=0, to F(t)=1-exp(-t-t^2/2). This is not an exact finite-n identity: at n=1 the CDF is erf(t/sqrt(2)), with right derivative sqrt(2/pi) at zero, while F has derivative one. The C0029-A001 exact-law wording must retain the limiting qualifier. This correction does not solve the Bernoulli conjecture.", "proof_text": None, "assumptions": ["real standard Gaussian iid entries", "fixed t>=0 before n tends to infinity", "source audit is pending referee acceptance"], "domain": "random matrix probability", "source": {"source_id": "owner-own-work:w568:c0029-gaussian-source-correction", "url": (ROOT / "SOURCE_CORRECTION.json").as_uri(), "revision": "draft-2026-10-10", "license": "owner-own-work (elementary counterexample and attributed source correction)", "excerpt": None}}, {"key": "c0029-scalar-obstruction", "namespace": "probability.random-matrices", "logical_name": "c0029-intermediate-scale-scalar-cdf-obstruction", "kind": "concept", "title": "C0029 draft obstruction to combining scalar universality bounds", "statement": "DRAFT author-derived scalar obstruction; w569 independent review pending. Let F(t)=1-exp(-t-t^2/2), eta_n=(log(n+e))^(-1/16), a_n=exp(-sqrt(n)), q_n=2^(-n), m_n=eta_n F(a_n)/2. For t>=0 set G_n(t)=q_n+(1-q_n)[(1-m_n)F(t)+m_n 1_{t>=a_n}], and set G_n(t)=0 for t<0. These CDFs have G_n(0)=q_n, uniform error |G_n-F|<=(eta_n/2)F+q_n, and G_n(t)<=(3/2)t+q_n. For every fixed d>0, eventually G_n(t)<=t for all t>=n^(-d). Yet eventually G_n(a_n)-a_n>=eta_n a_n/16, which defeats every bound t+C exp(-cn) with fixed C,c>0. The reference F is limiting; no realization by iid Bernoulli matrices or counterexample to their conjecture is asserted.", "proof_text": None, "assumptions": ["n is a positive integer", "t>=0", "d is fixed before the eventual dimension threshold", "artificial scalar probability distributions", "no finite-n Gaussian comparison or Bernoulli realization is asserted"], "domain": "probability proof auditing", "source": {"source_id": "owner-own-work:w568:c0029-scalar-obstruction", "url": (ROOT / "OBSTRUCTION_PROOF.md").as_uri(), "revision": "draft-2026-10-10", "license": "owner-own-work (campaign refuted route, unreviewed concept)", "excerpt": None}}], "relations": [{"from_key": "c0029-real-gaussian-scope", "to_existing_logical": OLD_LOGICAL, "kind": "cites", "rationale": "The existing C0029-A001 card says exact real-Gaussian law; this draft provides the finite-n counterexample and limiting-law qualifier."}, {"from_key": "c0029-scalar-obstruction", "to_existing_logical": TARGET_LOGICAL, "kind": "semantic_association", "rationale": "The target requires exact coefficient one at small scales; the scalar example identifies why endpoint and relative-error estimates alone do not fill that window."}, {"from_key": "c0029-scalar-obstruction", "to_key": "c0029-real-gaussian-scope", "kind": "semantic_association", "rationale": "Both entries require distinguishing the limiting reference law from the finite-n law; the scalar construction does not claim to instantiate the matrix comparison theorem."}]}
    write("drafts/bundle_001.json", bundle)

    hook = {"id": "gaussian-limit-w568-01", "area": "math", "event": "stage-start", "cue": "real Gaussian least-singular-value formula 1-exp(-t-t^2/2) is asserted as an exact finite-n identity", "fire_when": "C0029-A001 says Edelman's exact law without a limiting qualifier", "silent_when": "The formula is explicitly an n-to-infinity limit, or the exact law is the complex Gaussian n*s_min^2 law", "text": "For real Gaussian matrices, 1-exp(-t-t^2/2) is a limiting CDF. Check finite n versus n->infinity before using an exact identity; n=1 has slope sqrt(2/pi), not one.", "evidence": "~/brain_workers/w568/SOURCE_CORRECTION.json; CLAIMS.jsonl row w568-C0029-correction-002; Tao--Vu Theorem 1.1", "proposer": "w568"}
    line = json.dumps(hook, ensure_ascii=False)+"\n"
    (ROOT / "hooks").mkdir(exist_ok=True)
    (ROOT / "hooks/math-w568.jsonl").write_text(line, encoding="utf-8")
    hookdiff = "".join(difflib.unified_diff([], [line], fromfile="/dev/null", tofile="b/primary_directive/hooks1000/proposals/math-w568.jsonl", n=0))
    (ROOT / "patches/02_gaussian_limit_hook.diff").write_text(hookdiff, encoding="utf-8")
    write("HOOK_CONTROLS.json", {"fire": hook["fire_when"], "silent": hook["silent_when"], "controls_status": "specified, not live-fired", "publication_status": "staged in worker folder; no shared hook file mutated"})
    write("PROGRESS_EVENT.json", {"agent": "w568", "row": "S1.1", "event": "C0029: saved concrete Gaussian-law source correction, intermediate-scale scalar obstruction, and scoped w567 audit; referee review pending", "evidence": str(ROOT / "REVIEW_PACKET.json")})
    print(json.dumps({"prepared": True, "draft_entries": len(bundle["entries"]), "claim_rows": len((ROOT / "CLAIMS.jsonl").read_text(encoding="utf-8").splitlines()), "paired_snapshot_sha256": audit["reviewed_snapshot_sha256"]}))


def submit() -> None:
    from verify_packet import validate
    local = ROOT / "drafts/bundle_001.json"
    validate(local)
    target_dir = Path("~/math-brain-inbox/w568")
    assert target_dir.resolve().as_posix().lower() == "~/math-brain-inbox/w568"
    target_dir.mkdir(exist_ok=True)
    target = target_dir / "bundle_001.json"
    data = local.read_bytes()
    if target.exists():
        if target.read_bytes() != data:
            raise RuntimeError("existing own draft differs; preserve it and request a new bundle number")
    else:
        part = target_dir / "bundle_001.part"
        if part.exists() and part.read_bytes() != data:
            raise RuntimeError("existing part differs; preserve it")
        part.write_bytes(data)
        part.rename(target)
    write("DELIVERY_STATUS.json", {"prepared": True, "submitted": {"state": True, "path": str(target), "time": dt.datetime.now().isoformat(), "kind": "DRAFT concepts"}, "reviewed": {"state": False, "referee": "w569", "scope": "independent mathematical and served-identity gates pending"}, "ingested": {"state": "not confirmed", "evidence": None}, "retrievable": {"state": "not tested", "evidence": None}, "live_store_written_by_worker": False, "canonical_integrator_run_by_worker": False})
    print(json.dumps({"submitted": str(target), "reviewed": False, "ingested": "not confirmed", "retrievable": "not tested"}))


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--submit", action="store_true")
    args = parser.parse_args()
    if args.submit:
        submit()
    else:
        prepare()
