"""Build the scoped C0047 handoff inside this worker folder only."""
from __future__ import annotations
import difflib
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent
DATE = "2026-10-10"
PRIOR = Path("~/<private-repo>/06_math_research/probability_1000_intake_claude_20260907/attempts.jsonl")


def save(name, obj):
    (ROOT / name).write_text(json.dumps(obj, ensure_ascii=False, indent=2)+"\n", encoding="utf-8")


proof = (ROOT / "PROOFS.md").read_text(encoding="utf-8")
claims_path = ROOT / "CLAIMS.jsonl"
claims = [json.loads(line) for line in claims_path.read_text(encoding="utf-8").splitlines() if line.strip()]
known = {row["claim_id"] for row in claims}
new_claims = [
    {"claim_id": "C0047-L4", "statement": "For m>=3 and the simple Cayley graph of C_2*C_m with S={a,b,b^-1}, h_E>=1-2/m>0, p_u=1, and p_c is the unique p in (0,1) solving p[2 sum_{k=1}^{m-1}p^k-(m-1)p^m]=1.",
     "assumptions": ["One undirected a-edge per involution pair", "No loops or parallel edges", "Independent Bernoulli bond variables", "m>=3"],
     "source": {"path": str(ROOT / "PROOFS.md"), "locator": "L4", "source_tag": "owner-own-work", "prior_primary": "https://arxiv.org/pdf/math/0611668, Theorem 1; edge convention differs"},
     "proof_or_counterexample": "Free-product normal form gives a tree of disjoint cycle blocks. Fresh block-cluster exploration has offspring Bin(X-1,p), with exact mean. Bridge cutsets give two-point decay; L2 proves pu=1. Cyclomatic counting gives the Cheeger bound.",
     "independent_reviewer": "w557 (pending), adversarial check w556 (pending)", "remaining_gap": "No general generating-set or one-ended extension; no novelty claim; review pending.", "status": "proved special case"},
    {"claim_id": "C0047-L5", "statement": "For an infinite connected d-regular vertex-transitive undirected graph and normalized walk operator P=A/d with rho=||P||_2, pd rho<1 implies tau_p(x,y)<=(pd rho)^dist(x,y)/(1-pd rho), so pu>=1/(d rho). Thus pc<1/(d rho) suffices for pc<pu, without being necessary.",
     "assumptions": ["d-regularity", "Normalized rho=||A/d||_2", "Bernoulli bond percolation", "Vertex transitivity for the uniqueness conclusion"],
     "source": {"path": str(ROOT / "PROOFS.md"), "locator": "L5", "source_tag": "owner-own-work"},
     "proof_or_counterexample": "Use union bound on simple open paths, then upper-bound their count by A^n matrix entries <=d^n rho^n; Harris contradicts uniqueness when the bound decays. Repeated-edge walks are not assigned probability p^n.",
     "independent_reviewer": "w557 (pending)", "remaining_gap": "No universal proof that pc<1/(d rho); this criterion even fails to certify T3's genuine nonuniqueness interval.", "status": "proved special case"},
    {"claim_id": "C0047-N1", "statement": "The normalized-rho reduction pc<1/rho in C0047-A001 is vacuous when rho<1, because pc<=1<1/rho; its proposed remaining case pc>=1/rho is impossible. The degree factor is required in L5's elementary sufficient criterion.",
     "assumptions": ["rho is the normalized simple-random-walk spectral radius, as explicitly specified in A001", "0<rho<1"],
     "source": {"prior_path": str(PRIOR), "prior_line": 37, "prior_quote": "p_c < 1/rho (Benjamini-Schramm criterion)", "proof_path": str(ROOT / "PROOFS.md"), "proof_locator": "L5", "source_tag": "owner-own-work"},
     "proof_or_counterexample": "pc is in [0,1], whereas 1/rho>1. On T3, rho=2sqrt(2)/3, pc=1/2 and pu=1; the valid sufficient threshold 1/(3rho) is below pc.",
     "independent_reviewer": "w557 (pending)", "remaining_gap": "Source correction not yet applied; does not refute or solve C0047.", "status": "proved special case"},
    {"claim_id": "C0047-GAP", "statement": "The independent barrier-exploration attempt does not prove pc<pu for a general one-ended nonamenable Cayley graph. A fresh effective-barrier construction or quantitative nonmerger bound at some p>pc is still required.",
     "assumptions": ["All generating sets in the parent target are fixed; none substituted", "No conditional products without derived filtration structure"],
     "source": {"path": str(ROOT / "PROOFS.md"), "locator": "Attempted extension and exact remaining obligation", "source_tag": "owner-own-work"},
     "proof_or_counterexample": "L3 rules out arbitrarily many disjoint deterministic bounded cuts in every one-ended h_E>0 transitive graph. Block independence fails if child branches merge, and inspecting a barrier before selecting it biases its law.",
     "independent_reviewer": "w557 (pending)", "remaining_gap": "Fresh effective-barrier or merger-control estimate in the unresolved one-ended class.", "status": "conjecture"}]
with claims_path.open("a", encoding="utf-8", newline="\n") as out:
    for row in new_claims:
        if row["claim_id"] not in known:
            out.write(json.dumps(row, ensure_ascii=False)+"\n")
            claims.append(row)

source_status = {
    "candidate_id": "C0047", "checked_on": DATE, "current_openness": "UNKNOWN",
    "parent_problem_solved": False, "novelty_claim": False,
    "exact_target": "For every infinite finitely generated group Gamma and every finite symmetric generating set S excluding the identity, independent Bernoulli bond percolation on the simple undirected Cayley graph Cay(Gamma,S) satisfies pc<pu iff Gamma is nonamenable.",
    "definitions": {"pc": "inf{p in [0,1]: there is an infinite cluster almost surely}",
                    "pu": "inf{p in [0,1]: there is exactly one infinite cluster almost surely}",
                    "h_E": "inf{|boundary_E A|/|A|: A finite nonempty}",
                    "rho": "ell2 norm of the NORMALIZED operator A/d on a d-regular graph"},
    "primary_statement": {"title": "Hugo Duminil-Copin, Sixty years of percolation (ICM 2018)",
                          "url": "https://www.ihes.fr/~duminil/publi/2018ICM.pdf",
                          "locator": "Conjecture 2, printed page 4 (PDF page index 3)",
                          "quote": "Consider a Cayley graph G of a finitely generated (infinite) group G.",
                          "display_in_own_notation": "pc(G)<pu(G) iff Gamma is nonamenable",
                          "verification": "Primary PDF directly viewed via web; exact statement and quantifiers recovered, not a proof."},
    "definitions_primary": {"url": "https://arxiv.org/html/1804.10191v3", "locator": "Introduction and Conjecture 1.1",
                            "quote": "Let G be a connected, locally finite, quasi-transitive graph."},
    "recent_primary_checks": [
        {"url": "https://arxiv.org/abs/2601.09958", "scope": "Planar SITE conjecture, distinct from universal Cayley BOND nonuniqueness."},
        {"url": "https://arxiv.org/abs/2609.07768", "scope": "Weighted-isoperimetry existence threshold; abstract's recent Benjamini-Schramm resolution concerns a different threshold question."},
        {"url": "https://arxiv.org/abs/2502.02560", "scope": "Weighted-amenability / relaxed ph<pu, not a proof of this exact target."}],
    "openness_limit": "Bounded recent search and local unsolved records do not certify absence of a 2026 proof; no current-open or novelty assertion.",
    "owner_work_check": {"solved_register": "~/Open problem project/solved_register.md",
                         "relevant_workspace": "~/Big Open problem in probability theory",
                         "observed": "README says project incomplete; round_339 lines66-69 says no general proof located. Prior core routes are L2/SAW, tensor-product and confined-bridge estimates; distinct from this route.",
                         "no_retired_problem_claim": True},
    "named_attempts_H_I": "Scoped C0047/Benjamini-Schramm search found no relevant exact attempt in the H_20260912 or I_20260914 directories.",
    "peer_boundary": {"adversary": "w556", "message": "2026-10-10 received precommit to operator/row-square-norm obstruction; block lane kept disjoint.",
                      "core_prover": "w552", "method_boundary_request_message": "msg-9046120cd8", "core_proof_read": False},
    "brain_scars": ["proof_steps_need_derived_joint_structure_2026_09_09", "perceptron_proof_open_gaps_fleet_2026_07_12"],
    "recall": "brain.py recall terminated its query at timeout=60 seconds; targeted index/slug files used instead.",
    "requested_model": "gpt-6.1-sol", "requested_reasoning": "max", "requested_service_tier": "Fast",
    "served_model_evidence": "UNAVAILABLE: no response-side identity record accessible in this task; requested settings are not served evidence.",
    "formal_verification": {"performed": False, "theorem": None, "trusted_axioms": None, "admitted_placeholders": None},
    "submission_state": "local packet prepared; inbox submission recorded separately", "review_state": "pending w557; w556 adversarial check pending",
    "ingestion_state": "NOT_INGESTED", "retrieval_state": "NOT_TESTED"}
save("SOURCE_STATUS.json", source_status)

prior_line = None
with PRIOR.open(encoding="utf-8") as stream:
    for number, line in enumerate(stream, 1):
        if '"attempt_id": "C0047-A001"' in line:
            prior_line = line.rstrip("\r\n")
            prior_number = number
            prior = json.loads(prior_line)
            break
if prior_line is None:
    raise RuntimeError("Exact C0047-A001 prior record not found")
corrected = dict(prior)
corrected["method"] = "Elementary simple-path union bound with normalized-walk degree factor; diagnostic sufficient condition only."
corrected["result"] = "CORRECTED AUTHOR DRAFT, review pending: rho denotes ||A/d||_2 on an infinite connected d-regular vertex-transitive graph. For p d rho<1, tau_p(x,y)<=(p d rho)^dist(x,y)/(1-p d rho), so pu>=1/(d rho). Therefore pc<1/(d rho) is a sufficient, not necessary, criterion for pc<pu. The prior pc<1/rho reduction with normalized rho was vacuous for rho<1 because pc<=1<1/rho. In particular its supposed remaining case pc>=1/rho is impossible. For T3, rho=2sqrt(2)/3, pc=1/2, pu=1, but 1/(3rho)<pc; the sufficient criterion does not certify all true gaps. See w555 PROOFS.md L5. No proof of the universal fixed-generating-set conjecture is supplied."
corrected["obstruction"] = "Need a different sufficient criterion or a sharper estimate for the fixed generating set; no general proof that pc<1/(d rho), which already fails on T3."
corrected["correction_note"] = "w555 2026-10-10: normalized spectral-radius degree factor repaired in a reviewable proposal; parent status unchanged."
corrected["independent_check"] = "pending w557; not mathematically reviewed or deployed"
corrected["correction_packet"] = str(ROOT / "REVIEW_PACKET.md")
corrected_line = json.dumps(corrected, ensure_ascii=False, sort_keys=True)
patch = list(difflib.unified_diff([prior_line+"\n"], [corrected_line+"\n"],
             fromfile="a/"+PRIOR.as_posix(), tofile="b/"+PRIOR.as_posix(), n=0))
patch[2] = f"@@ -{prior_number} +{prior_number} @@\n"
(ROOT / "patches").mkdir(exist_ok=True)
(ROOT / "patches/01_c0047_normalized_spectral_degree.diff").write_text("".join(patch), encoding="utf-8", newline="\n")
save("PRIOR_ATTEMPT_SOURCE_REPORT.json", {"path": str(PRIOR), "line": prior_number,
     "line_sha256": hashlib.sha256(prior_line.encode()).hexdigest(), "record": prior})

snapshot = json.loads((ROOT / "STORE_SOURCE_REPORT.json").read_text(encoding="utf-8"))
attempt_node = next(row for row in snapshot["rows"] if row["id"].startswith("claim_77d417"))
metadata = json.loads(attempt_node["metadata_json"])
save("STORE_CORRECTION.json", {
    "status": "DRAFT_NOT_APPLIED", "target_id": attempt_node["id"], "current_digest": attempt_node["digest"],
    "target_logical": metadata["logical_id"], "current_title": attempt_node["title"],
    "current_body": attempt_node["body"], "incorrect_quote": "p_c < 1/rho (Benjamini-Schramm criterion)",
    "corrected_statement": corrected["result"], "source_proof": str(ROOT / "PROOFS.md")+"#L5",
    "scope": "Correct only the normalized-rho reduction in the historical concept; preserve C0047 as a conjecture.",
    "reviewer": "w557 pending", "do_not_write_store": True,
    "apply_route": "Coordinator validates, checks exact current digest, and records a superseding correction through supported store ingestion; no SQL UPDATE."})

entry_statements = {
 "cutset": claims[1]["statement"],
 "one-ended": next(x["statement"] for x in claims if x["claim_id"]=="C0047-L3"),
 "blocks": next(x["statement"] for x in claims if x["claim_id"]=="C0047-L4"),
 "normalization": next(x["statement"] for x in claims if x["claim_id"]=="C0047-L5"),
 "gap": next(x["statement"] for x in claims if x["claim_id"]=="C0047-GAP")}
names = {"cutset": "percolation-disjoint-cutset-connection-bound", "one-ended": "bounded-cut-multiplicity-in-one-ended-nonamenable-graphs",
         "blocks": "simple-cyclic-free-product-percolation-threshold", "normalization": "normalized-spectral-radius-percolation-degree-factor",
         "gap": "benjamini-schramm-fresh-barrier-exploration-gap"}
titles = {"cutset": "Disjoint cutsets bound Bernoulli connections", "one-ended": "Bounded cutsets cannot cover one-ended nonamenable graphs",
          "blocks": "Exact simple cyclic free-product percolation special case", "normalization": "Normalized spectral percolation criteria need the degree factor",
          "gap": "Unclosed barrier and merger obligation for C0047"}
claim_lookup = {"cutset":"C0047-L1", "one-ended":"C0047-L3", "blocks":"C0047-L4", "normalization":"C0047-L5", "gap":"C0047-GAP"}
entries=[]
for key, statement in entry_statements.items():
    claim = next(x for x in claims if x["claim_id"]==claim_lookup[key])
    entries.append({"key": key, "namespace": "probability.percolation", "logical_name": names[key], "kind": "concept",
       "title": titles[key], "statement": "DRAFT: author proof or explicit gap; independent mathematical review pending. "+statement,
       "proof_text": None, "assumptions": claim["assumptions"], "domain": "probability theory",
       "source": {"source_id": "owner-own-work:C0047:w555:"+DATE+":"+key,
                  "url": (ROOT / "PROOFS.md").as_uri(), "revision": "author-draft-"+DATE,
                  "license": "owner-own-work", "excerpt": None}})
bundle = {"spec":"mathbrain-draft-v1", "author_agent":"w555", "bundle_slug":"c0047-independent-separators-normalization-20261010",
    "entries": entries, "relations":[
       {"from_key":"blocks", "to_key":"cutset", "kind":"depends_on", "rationale":"L4's bridge cuts satisfy L1's disjoint edge-index hypothesis; L2 then excludes uniqueness."},
       {"from_key":"gap", "to_key":"one-ended", "kind":"depends_on", "rationale":"L3 gives a uniform finite bound on size-K cut multiplicity; the parent lane lacks a fresh-barrier replacement."},
       {"from_key":"normalization", "to_existing_logical":metadata["logical_id"], "kind":"refutes",
        "rationale":"Scoped correction only: the prior concept says 'p_c < 1/rho (Benjamini-Schramm criterion)' with normalized rho. L5 proves the degree-scaled sufficient bound, while pc<=1<1/rho makes the prior reduction vacuous. No refutation of the parent conjecture."}],
    "review_state":"pending w557; concepts only", "parent_problem_solved":False}
save("bundle_001.json", bundle)
save("RELATION_EVIDENCE.json", [{"from_key": r["from_key"], "to": r.get("to_key", r.get("to_existing_logical")),
     "kind": r["kind"], "supporting_from": entry_statements[r["from_key"]],
     "supporting_to": entry_statements[r["to_key"]] if "to_key" in r else "p_c < 1/rho (Benjamini-Schramm criterion)",
     "rationale":r["rationale"]} for r in bundle["relations"]])

hook = {"id":"percolation-w555-01", "area":"math", "event":"PreToolUse",
        "cue":"percolation proof uses pc<1/rho or pu>=1/rho with rho explicitly normalized as A/d",
        "fire_when":"C0047-A001 reduction uses the normalized simple-random-walk radius yet omits degree d",
        "silent_when":"rho is explicitly the unnormalized adjacency norm, or the formula contains d*rho, or only a gap is being recorded",
        "text":"Pin the spectral normalization before comparing thresholds. With P=A/d, the elementary path bound uses p*d*||P||<1. Since pc<=1<1/rho when rho<1, pc<1/rho alone is vacuous; it does not supply a gap proof.",
        "evidence":"~/brain_workers/w555/PROOFS.md L5; live concept claim_77d417df1817eac0893d67dcfcf0d7140581f4e26ce07c31919403d44d301960; scar proof_steps_need_derived_joint_structure_2026_09_09",
        "proposer":"w555"}
(ROOT / "HOOK_PROPOSAL.jsonl").write_text(json.dumps(hook)+"\n", encoding="utf-8")
assert len(hook["text"]) <= 300
assert all(e["kind"] == "concept" and e["proof_text"] is None for e in bundle["entries"])
assert len(bundle["entries"]) <= 200

measurements = json.loads((ROOT / "MEASUREMENTS.json").read_text(encoding="utf-8"))
save("PACKET_VALIDATION.json", {"claim_rows":len(claims), "duplicate_claim_ids":len(claims)-len({x["claim_id"] for x in claims}),
    "source_store_rows":snapshot["row_count"], "draft_entries":len(entries), "relations_with_both_ends":len(bundle["relations"]),
    "all_new_entries_concept":True, "parent_solved":False, "finite_control_status":measurements["status"],
    "source_check_is_not_math_proof":True, "live_store_writes":0})
print(json.dumps({"claims":len(claims), "draft_entries":len(entries), "finite_control_status":measurements["status"],
                  "patch":str(ROOT / "patches/01_c0047_normalized_spectral_degree.diff"), "live_writes":0}, indent=2))
