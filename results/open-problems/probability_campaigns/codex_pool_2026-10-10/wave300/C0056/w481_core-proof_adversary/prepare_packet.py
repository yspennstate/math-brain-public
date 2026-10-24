"""Prepare local review artifacts. Never writes a live store or starts compute jobs."""
from pathlib import Path
import hashlib
import json
import math
import time
from fractions import Fraction

ROOT = Path(__file__).resolve().parent
started = time.perf_counter()

def save(name, data):
    (ROOT / name).write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")

claims_path = ROOT / "CLAIMS.jsonl"
existing = [json.loads(s) for s in claims_path.read_text(encoding="utf-8-sig").splitlines() if s.strip()]
new_claims = [
    {
        "id": "w481.C0056.02", "kind": "source_scope",
        "statement": "C0056's intake includes both absolutely continuous spectrum and finite-volume GOE local statistics; a spectral reduction alone does not settle the full record.",
        "assumptions": "Exact intake row 56 and Bourgade ICM 2018 Section 2.1, page 7; source iid potentials centered with variance one, periodic boxes, microscopic volume scaling.",
        "source": "SOURCE_STATUS.json; primary source https://math.nyu.edu/~bourgade/papers/ICMProceedings.pdf",
        "proof_or_counterexample": "Source quote: there is no clear understanding about how extended states imply GOE spectral statistics. The recent September 23 main theorem has a spectral conclusion and no GOE conclusion.",
        "independent_reviewer": "w482 (pending)", "remaining_gap": "No fully quantified all-laws or GOE theorem recovered; current full-target openness UNKNOWN.", "status": "sketch"
    },
    {
        "id": "w481.C0056.03", "kind": "conditional_reduction",
        "statement": "For fixed lambda>0 and iid uniform[-1,1] Anderson potentials on Z3, a uniform integrated expected inverse-cavity-damping bound along eta_n->0 implies pure AC restriction on a bounded open I, with E||rho_0||_2^2 <= Q/(4*pi*lambda).",
        "assumptions": "Q=sup_n integral_I E[(eta_n+Im<h,(H^(0)-E-i eta_n)^(-1)h>)^(-1)] dE < infinity; all boundary limits at fixed lambda.",
        "source": "owner-own-work; CAVITY_REDUCTION.md, saved before paired statement",
        "proof_or_counterexample": "Independent-site Schur integral gives E[(Im G00)^2|cavity]<=pi/(4 lambda b); Fatou and the L2 dual criterion exclude singular mass; countably many sites span l2.",
        "independent_reviewer": "w482 (pending)", "remaining_gap": "Q has NOT been bounded for the target; nonzero mass and GOE separate. Complete conditional derivation, review pending.", "status": "sketch"
    },
    {
        "id": "w481.C0056.04", "kind": "identity_check",
        "statement": "For all real a and positive b,lambda, integral_R [b/(pi*((lambda*v-a)^2+b^2))] log(1+b/(pi*((lambda*v-a)^2+b^2))) dv equals (2/lambda) log((1+sqrt(1+1/(pi*b)))/2).",
        "assumptions": "Whole real-line integration, normalized Poisson kernel, natural logarithm; this is not equality for a truncated uniform site law.",
        "source": "w480 statement; independent w481 derivation in PAIRED_LEMMA_INDEPENDENT_CHECK.md",
        "proof_or_counterexample": "Differentiate the normalized Cauchy integral in c=1/(pi*b), evaluate by partial fractions, and integrate from c=0. Uniform[-1,1] expectation includes a density factor 1/2 and truncation.",
        "independent_reviewer": "w482 (pending on w481 derivation)", "remaining_gap": "No algebraic gap found; source identity supported independently, but no response-side model-gate receipt.", "status": "proved special case"
    },
    {
        "id": "w481.C0056.05", "kind": "conditional_reduction",
        "statement": "For probability spectral measures mu_omega, a uniform expected integral_J f_eta_n log(1+f_eta_n), where f_eta_n is the normalized Poisson convolution and eta_n->0, implies mu_omega restricted to bounded open J is absolutely continuous almost surely.",
        "assumptions": "Deterministic eta_n sequence, positive finite probability measures, finite expected entropy bound; no site independence needed for this measure criterion.",
        "source": "owner-own-work independent null-set proof; PAIRED_LEMMA_INDEPENDENT_CHECK.md; paired w480 L2",
        "proof_or_counterexample": "Fatou selects an almost-sure bounded-entropy subsequence. Its mass on U is at most K|U|+A/log(1+K). Poisson convergence and compact null-set cutoffs, then outer/inner regularity, eliminate every singular mass.",
        "independent_reviewer": "w482 (pending)", "remaining_gap": "The entropy premise needs the still-unproved fixed-lambda infinite-volume LG estimate. Complete conditional derivation, review pending.", "status": "sketch"
    },
    {
        "id": "w481.C0056.06", "kind": "unproved_input",
        "statement": "For sufficiently small fixed nonzero uniform-disorder Anderson coupling, there is a deterministic nonempty bounded open J inside (-6,6) for which sup_{0<eta<=1} E integral_J log(1+1/b_0(E,eta)) dE is finite.",
        "assumptions": "Infinite-volume deleted-site cavity of the genuine nearest-neighbor lattice, b_0=eta+Im Sigma_0, lambda fixed before eta boundary limit.",
        "source": "w480 ATTEMPT.md (LG); ATTEMPT.md in this worker folder",
        "proof_or_counterexample": "No proof. The deterministic perturbation estimate stops at eta of order sqrt(lambda); first-moment averaging and fixed-size computations do not supply LG.",
        "independent_reviewer": "w482 (pending)", "remaining_gap": "This is the hardest missing input in this route; it remains fully unproved. GOE is another unsolved task outside the route.", "status": "conjecture"
    },
    {
        "id": "w481.C0056.07", "kind": "counterexample",
        "statement": "Divergence of integrated log(1+1/b_N(E,eta)) as eta->0 at every fixed finite cavity size N does not force successive N then eta limits: a coupled eta_N=N^(-1/4) sequence can have a uniformly bounded logarithmic integral.",
        "assumptions": "D_N diagonal midpoint grid on [-1,1], root u_N uniform unit vector, finite cavity in its orthonormal root decomposition, N>=16, J=(-1/2,1/2). Not an iid Anderson Hamiltonian.",
        "source": "owner-own-work; JOINT_LIMIT_COUNTEREXAMPLE.md",
        "proof_or_counterexample": "Riemann error |g_N-g|<=1/(N eta^2); at eta_N, Im g_N>=pi/8 and |g_N|<=C+1/4, C=(log3)/2+pi/2. Schur gives b_N>=pi/[8(C+1/4)^2]>0. At fixed N its finite spectral representation gives logarithmic divergence.",
        "independent_reviewer": "w482 (pending)", "remaining_gap": "Independent check pending. Only the claimed necessity sentence is refuted; the fixed-size theorem and conditional LG route survive.", "status": "proved special case"
    }
]
ids = {c["id"] for c in existing}
with claims_path.open("a", encoding="utf-8") as handle:
    for claim in new_claims:
        if claim["id"] not in ids:
            handle.write(json.dumps(claim, ensure_ascii=False) + "\n")

source = {"source_id": "owner-own-work:w481:C0056-core-audit-20261010", "url": None,
          "revision": "draft-2026-10-10-independent-review-pending", "license": "owner-own-work", "excerpt": None}
entries = [
    {"key": "cavity", "namespace": "probability.random-operators", "logical_name": "single-site-cavity-damping",
     "kind": "definition", "title": "DRAFT: Single-site cavity damping",
     "statement": "For a bounded self-adjoint block operator H=[[s,h*],[h,B]], its deleted-site cavity is B. At z=E+i eta with eta>0, define S(z)=<h,(B-z)^(-1)h> and b(E,eta)=eta+Im S(z)>0. For a lattice root, h contains its hopping coefficients. This definition applies to finite and infinite cavities; it does not assert any uniform small-eta lower bound.",
     "proof_text": None, "assumptions": ["H bounded self-adjoint", "eta>0"], "domain": "probability and spectral theory", "source": source},
    {"key": "annealed", "namespace": "probability.random-operators", "logical_name": "annealed-first-moment-does-not-imply-quenched-ac",
     "kind": "concept", "title": "DRAFT: Averaged first moments do not prove sample spectral purity",
     "statement": "Independent review pending. For the diagonal operator D delta_x=X_x delta_x on l2(Z3), with iid uniform[-1,1] variables, every realization has site measure delta_(X_x) and a complete eigenbasis. Yet sup_(E real,eta>0) E Im<(delta_0),(D-E-i eta)^(-1)delta_0> <= pi/2 and integral_R Im G00 dE=pi in each sample. Thus these first-moment controls do not imply quenched AC. This refutes a proof implication, not the nearest-neighbor weak-disorder Anderson conjecture.",
     "proof_text": None, "assumptions": ["Diagonal iid uniform[-1,1] model", "No hopping"], "domain": "probability and spectral theory", "source": source},
    {"key": "log-route", "namespace": "probability.random-operators", "logical_name": "uniform-anderson-log-cavity-damping-proof-obligation",
     "kind": "concept", "title": "DRAFT: Logarithmic cavity damping is an unproved Anderson input",
     "statement": "Independent review pending. For H=-A+lambda V on l2(Z3), iid uniform[-1,1] V, fixed lambda>0, and bounded open J, the infinite-volume premise sup_(0<eta<=1) E integral_J log(1+1/b_0(E,eta)) dE < infinity implies almost-sure pure AC on J. Single-site integration bounds the expected normalized Poisson entropy by (1/(2 lambda)) times that logarithmic functional; a Fatou subsequence and null-set argument exclude singular mass. The logarithmic premise is NOT proved for weak disorder. Nonzero mass and finite-volume GOE statistics are separate. No parent solution is claimed.",
     "proof_text": None, "assumptions": ["Genuine nearest-neighbor Z3 operator", "Uniform site law independent of the deleted-site cavity", "lambda fixed before eta->0", "The explicitly unproved logarithmic premise"], "domain": "probability and spectral theory", "source": source},
    {"key": "joint-limit", "namespace": "analysis.spectral-theory", "logical_name": "fixed-volume-log-divergence-allows-coupled-limits",
     "kind": "concept", "title": "DRAFT: Fixed-size divergence permits a controlled coupled limit",
     "statement": "Independent review pending. Let D_N have diagonal grid v_j=-1+(2j+1)/N, let u_N be the normalized all-ones vector, and let B_N,h_N be the cavity blocks in a basis starting with u_N. On J=(-1/2,1/2), eta_N=N^(-1/4), N>=16, the scalar resolvent g_N has Im g_N>=pi/8 and |g_N|<=C+1/4, C=(log3)/2+pi/2. Hence b_N=Im g_N/|g_N|^2>=pi/[8(C+1/4)^2]>0 and its integrated log(1+1/b_N) is uniformly bounded along eta_N. At every fixed N the same functional diverges as eta->0. Thus fixed-size divergence does not force successive limits. This is an abstract finite-cavity example, not an Anderson proof.",
     "proof_text": None, "assumptions": ["Finite deterministic midpoint-grid model", "Root u_N", "Coupled N and eta_N limits"], "domain": "spectral theory", "source": source}
]
relations = [
    {"from_key": "log-route", "to_key": "cavity", "kind": "depends_on", "rationale": "The unproved logarithmic input uses precisely the defined deleted-site damping b."},
    {"from_key": "joint-limit", "to_key": "cavity", "kind": "depends_on", "rationale": "The coupled-limit example uses the same cavity damping in a finite root decomposition."},
    {"from_key": "annealed", "to_key": "log-route", "kind": "semantic_association", "rationale": "The diagonal example rules out replacing the route's logarithmic input by an annealed first-moment bound."}
]
query = json.loads((ROOT / "STORE_TARGET_CHECK.json").read_text(encoding="utf-8"))
legacy = next(r for r in query["rows"] if r["title"] == "Open problem: Extended states for the three-dimensional Anderson model at weak disorder")
legacy_logical = json.loads(legacy["metadata_json"])["logical_id"]
relations.append({"from_key": "log-route", "to_existing_logical": legacy_logical,
                  "kind": "semantic_association", "rationale": "The conditional uniform-law logarithmic route addresses only the AC part of this existing two-part C0056 record; GOE remains outside it."})
bundle = {"spec": "mathbrain-draft-v1", "author_agent": "w481", "bundle_slug": "anderson-cavity-limits-w481-001", "entries": entries, "relations": relations}
save("bundle_001.json", bundle)
by_key = {e["key"]: e for e in entries}
support = []
for relation in relations:
    row = {**relation, "from_quote": by_key[relation["from_key"]]["statement"]}
    if "to_key" in relation:
        row["to_quote"] = by_key[relation["to_key"]]["statement"]
    else:
        row.update({"to_quote": legacy["body"], "existing_node_id": legacy["id"], "existing_node_digest": legacy["digest"]})
    support.append(row)
(ROOT / "RELATION_SUPPORT.jsonl").write_text("".join(json.dumps(r, ensure_ascii=False) + "\n" for r in support), encoding="utf-8")

claims = [json.loads(s) for s in claims_path.read_text(encoding="utf-8-sig").splitlines() if s.strip()]
required_claim = {"id", "statement", "assumptions", "source", "proof_or_counterexample", "independent_reviewer", "remaining_gap", "status"}
statuses = {"conjecture", "numerical evidence", "sketch", "proved special case", "independently checked proof"}
assert len({c["id"] for c in claims}) == len(claims)
assert all(required_claim <= c.keys() and c["status"] in statuses for c in claims)
assert all(e["kind"] in {"definition", "concept"} and e["proof_text"] is None for e in entries)
assert all(e["source"]["license"] == "owner-own-work" and e["statement"] and e["assumptions"] for e in entries)
assert all(r["from_key"] in by_key and ((r.get("to_key") in by_key) or r.get("to_existing_logical") == legacy_logical) for r in relations)
graph = {k: [] for k in by_key}
for r in relations:
    if r["kind"] == "depends_on": graph[r["from_key"]].append(r["to_key"])
def visit(k, active):
    assert k not in active, "dependency cycle"
    for other in graph[k]: visit(other, active | {k})
for k in graph: visit(k, set())
assert all(r["from_quote"] == by_key[r["from_key"]]["statement"] and r["to_quote"] == (by_key[r["to_key"]]["statement"] if "to_key" in r else legacy["body"]) for r in support)
hook = json.loads((ROOT / "HOOK_PROPOSAL.jsonl").read_text(encoding="utf-8"))
assert len(hook["text"]) <= 300 and hook["fire_when"] and hook["silent_when"]
source_status = json.loads((ROOT / "SOURCE_STATUS.json").read_text(encoding="utf-8"))
source_status["prior_work"]["store"] = "Read-only query completed; 2 relevant Anderson nodes found, plus one unrelated C0056 metadata collision. See STORE_TARGET_CHECK.json. The store records are not a proof or retirement certificate."
save("SOURCE_STATUS.json", source_status)

# Exact witness checks, not a resource-consuming mathematical experiment.
grid = [Fraction(-1) + Fraction(2*j+1,16) for j in range(16)]
assert sum(grid) == 0 and min(grid) > -1 and max(grid) < 1
assert Fraction(16,1) ** -1 / Fraction(1,2) ** 2 == Fraction(1,4)
assert math.pi/4 - 1/4 >= math.pi/8
query = json.loads((ROOT / "STORE_TARGET_CHECK.json").read_text(encoding="utf-8"))
checks = {"claim_fields_and_unique_ids": True, "allowed_statuses": True, "draft_kinds_only": True,
          "owner_source_license": True, "complete_relations": True, "acyclic_dependencies": True,
          "exact_support_quotes": True, "hook_schema_and_length": True,
          "exact_N16_midpoint_mean_zero": True, "exact_N16_Riemann_bound_one_quarter": True,
          "lower_bound_constant_check": True}
validation = {"command": "python -X utf8 ~/brain_workers/w481/prepare_packet.py", "checks": checks,
              "claim_rows": len(claims), "draft_cards": len(entries), "draft_relations": len(relations),
              "theorem_or_lemma_promotions": 0, "verified_parent_solutions": 0,
              "live_store_writes": 0, "research_compute_experiments": 0,
              "read_only_query_seconds": query["elapsed_seconds"],
              "validation_seconds": time.perf_counter()-started,
              "limits": "Structural and exact witness checks do not independently prove the mathematics or improve recall. Reviewer and served-model gates remain pending."}
save("VALIDATION.json", validation)
review_files = ["SOURCE_STATUS.json", "ATTEMPT.md", "CLAIMS.jsonl", "INDEPENDENT_OBSTRUCTION.md", "CAVITY_REDUCTION.md",
                "PAIRED_LEMMA_INDEPENDENT_CHECK.md", "JOINT_LIMIT_COUNTEREXAMPLE.md", "VERDICT_W480.md", "REVIEW_PACKET.md", "REPORT.md"]
hashes = [{"path": str(ROOT / name), "sha256": hashlib.sha256((ROOT / name).read_bytes()).hexdigest()} for name in review_files]
peer = Path("~/brain_workers/w480/ATTEMPT.md")
hashes.append({"path": str(peer), "sha256": hashlib.sha256(peer.read_bytes()).hexdigest(), "note": "Paired proof at handoff time; any later correction requires a fresh audit snapshot."})
save("REVIEW_HASHES.json", {"purpose": "Local review handoff; not a draft-bundle manifest, store seal, or mathematical proof receipt", "files": hashes})
print(json.dumps(validation, indent=2))
