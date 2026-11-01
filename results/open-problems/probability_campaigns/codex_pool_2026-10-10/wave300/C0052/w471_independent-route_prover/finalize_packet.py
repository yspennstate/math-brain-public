"""Build explicitly unreviewed concepts; never invoke the live integrator."""
from pathlib import Path
from datetime import datetime, timezone
import hashlib
import json

HERE = Path(__file__).resolve().parent
timestamp = datetime.now(timezone.utc).isoformat()
receipt = json.loads((HERE / "LOCAL_SOURCE_RECEIPT.json").read_text(encoding="utf-8"))
status_path = HERE / "SOURCE_STATUS.json"
status = json.loads(status_path.read_text(encoding="utf-8"))
status["local_evidence"]["owner_solved_retired_check"] = (
    f"Targeted {len(receipt['intake_files_targeted'])} exact intake files and the read-only canonical store. "
    "The two matching canonical nodes are unverified concepts; no verified solved/retired status was found. "
    "This is not an exhaustive scan of the owner's work; current openness stays UNKNOWN."
)
status["local_evidence"]["canonical_receipt"] = "LOCAL_SOURCE_RECEIPT.json"
status_path.write_text(json.dumps(status, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

claims_path = HERE / "CLAIMS.jsonl"
existing_claims = [json.loads(line) for line in claims_path.read_text(encoding="utf-8").splitlines() if line.strip()]
gap_id = "w471-C0052-gap"
if gap_id not in {item["id"] for item in existing_claims}:
    gap = {
        "id": gap_id, "status": "conjecture",
        "statement": "For the subcritical nearest-neighbor ferromagnetic Ising free state on Z^3, let ell_beta be the smallest positive integer capturing at least chi(beta)/2 of the two-point susceptibility, R_beta=max(1,ceil(xi(beta)),ell_beta), S_beta the magnetization in |x|_infinity<=2R_beta, and y_beta its first imaginary block-field MGF zero. Prove liminf_{beta increasing to beta_c} sqrt(Var(S_beta))*y_beta < infinity.",
        "assumptions": ["Exact Gibbs-marginal block and dimensionless block field defined in ATTEMPT.md L2", "L2 hypotheses, with beta increasing to beta_c from below"],
        "source": "Author proposed sufficient condition for the primary target; ATTEMPT.md",
        "proof_or_counterexample": "Unproved. L2 establishes that this condition suffices for nonvanishing renormalized coupling. Lee-Yang axis location, raw thermodynamic zero limits, and finite experiments do not establish it.",
        "independent_reviewer": "w473; pending", "remaining_gap": "This exact normalized first-zero bound is the single hardest remaining gap.",
        "parent_problem_solved": False,
    }
    with claims_path.open("a", encoding="utf-8") as handle:
        handle.write(json.dumps(gap, ensure_ascii=False) + "\n")

base_source = {"source_id": "owner-own-work:w471:c0052-lee-yang-20261010",
               "url": "file:///~/brain_workers/w471/ATTEMPT.md",
               "revision": "author-derived-unreviewed-20261010-v1",
               "license": "owner-own-work", "excerpt": None}

def concept(key, logical_name, title, statement, assumptions):
    return {"key": key, "namespace": "probability.statmech", "logical_name": logical_name,
            "kind": "concept", "title": title,
            "statement": "DRAFT author-derived material; independent review pending; no novelty or parent-solved claim. " + statement,
            "proof_text": None, "assumptions": assumptions, "domain": "probability theory",
            "source": dict(base_source)}

entries = [
    concept("zero-criterion", "lee-yang-normalized-first-zero-fourth-cumulant-criterion-draft",
            "DRAFT: Normalized Lee–Yang zero and Gaussian convergence",
            "For bounded symmetric real S with variance V>0 and moment generating function having only imaginary zeros i*y_j (positive y_j with multiplicity), set X=S/sqrt(V), r=sqrt(V)*y_1 and B=3-E X^4. Hadamard factorization of F(sqrt(w)), of entire order at most 1/2, gives F(z)=product_j(1+z^2/y_j^2), V=2 sum_j y_j^-2 and kappa4(S)=-12 sum_j y_j^-4. Thus 12/r^4<=B<=6/r^2. The product yields E exp(tX)<=exp(t^2/2); hence uniform integrability of fourth powers. For a sequence obeying these hypotheses, Gaussian weak convergence to N(0,1) is equivalent to r tending to infinity. Bounded r along a subsequence forces every weak subsequential limit to be non-Gaussian. The Ising application requires zero field, ferromagnetic pair interactions, nonnegative block weights, spin-flip symmetry, and a justified Lee–Yang/Hurwitz passage to the actual Gibbs marginal.",
            ["S is bounded and symmetric", "V>0", "All MGF zeros are imaginary", "Independent review pending"]),
    concept("coupling-bridge", "ising-susceptibility-quantile-block-first-zero-coupling-bound-draft",
            "DRAFT: Susceptibility-quantile block gives g_+ >= 3/r^4",
            "Fix 0<beta<beta_c in the translation-invariant symmetric free Ising state on Z^3. Let G>=0, chi=sum G<infinity, xi the positive finite exponential correlation length, and K=-U4>=0 be summable over its last three indices. Define g_+=sum K(0,x2,x3,x4)/(chi^2 xi^3). Let ell be the smallest positive integer with sum_{|z|_infinity<=ell}G(z)>=chi/2; put R=max(1,ceil(xi),ell), Lambda={|x|_infinity<=2R}, N=(4R+1)^3, S=sum_{x in Lambda}sigma_x, V=E S^2, r=sqrt(V)*y_1, and B=-kappa4(S)/V^2. Here y_1 is the first zero of the infinite-volume Gibbs-marginal block-field MGF, not an isolated free-boundary partition function. Positivity gives -kappa4(S)<=N*g_+*chi^2*xi^3, while V>=N*chi/16 and N>=64*xi^3. Consequently g_+>=B/4>=3/r^4. Bounded r along beta_n increasing to beta_c is a sufficient condition for nonvanishing g_+. An eventual bound r<=C implies liminf g_+>=3/C^4. This does not prove such a bound or the converse implication from r escaping to g_+ vanishing.",
            ["0<beta<beta_c, nearest-neighbor ferromagnetic Ising free state on Z^3", "Translation invariance and spin-flip symmetry", "G nonnegative and chi finite", "xi positive and finite with the source's exponential definition", "-U4 nonnegative for all indices and summable", "Correct Gibbs-marginal Lee–Yang application", "Independent review pending"]),
    concept("open-zero-gap", "ising-c0052-susceptibility-block-normalized-zero-gap-draft",
            "C0052 open proof obligation: a bounded normalized first zero",
            "Unproved sufficient condition: in the subcritical nearest-neighbor Ising free state on Z^3, define ell_beta as the smallest positive integer capturing half of chi(beta), R_beta=max(1,ceil(xi(beta)),ell_beta), S_beta=sum_{|x|_infinity<=2R_beta}sigma_x, and y_beta as the first imaginary zero of E exp(h S_beta), with h a dimensionless field applied only to the block in the full Gibbs state. Prove liminf_{beta increasing to beta_c} sqrt(Var(S_beta))*y_beta < infinity. The author-derived g_+>=3/r^4 reduction makes this sufficient for the 2017 source's nonvanishing-coupling target, but the normalized zero bound is not established. Raw thermodynamic zero convergence, finite-box data, and a different boundary law cannot be substituted without additional comparison and quantitative proof. Current openness of the parent problem is UNKNOWN after a bounded source check; this campaign attempt remains incomplete.",
            ["Exact block law and length selection as stated", "beta increases to beta_c from below", "This condition is conjectural, not a theorem"]),
    concept("normalization-control", "lee-yang-raw-zero-limit-insufficient-independent-spin-control",
            "Control: raw Lee–Yang zeros alone do not exclude Gaussian limits",
            "For N independent fair signs, let S=a_N sum_{i=1}^N sigma_i with a_N>0. Its MGF is cosh(a_N h)^N, variance V=N a_N^2, and first imaginary zero y_1=pi/(2a_N). Thus r=sqrt(V)y_1=pi sqrt(N)/2, while 3-E(S/sqrt(V))^4=2/N and S/sqrt(V) converges to N(0,1). Choosing a_N=N makes y_1 tend to zero even though normalized zeros escape and the limit is Gaussian. This refutes the generic inference from axis location or raw zero collapse to non-Gaussian scaling. It is not a counterexample to critical nearest-neighbor 3D Ising.",
            ["Independent symmetric signs and a_N>0", "Control of a generic inference only"]),
]
relations = [
    {"from_key": "coupling-bridge", "to_key": "zero-criterion", "kind": "depends_on",
     "rationale": "The bridge uses B>=12/r^4 from the zero/cumulant criterion after proving g_+>=B/4 for its specified Gibbs block."},
    {"from_key": "open-zero-gap", "to_key": "coupling-bridge", "kind": "depends_on",
     "rationale": "The proposed bounded-r condition is sufficient for the target precisely because the bridge bounds g_+ below by 3/r^4; the condition remains unproved."},
    {"from_key": "normalization-control", "to_key": "zero-criterion", "kind": "semantic_association",
     "rationale": "The independent-spin control has r diverging and B vanishing, illustrating why the zero criterion uses variance-normalized rather than raw zeros."},
]
for node in receipt.get("canonical_matches", []):
    meta = json.loads(node["metadata_json"])
    if node["title"].startswith("Open problem: Non-triviality") and meta.get("logical_id"):
        relations.append({"from_key": "open-zero-gap", "to_existing_logical": meta["logical_id"],
                          "kind": "cites", "rationale": "The existing C0052 concept asks for nonvanishing renormalized coupling; this draft records an unproved sufficient condition, with no proves relation or current-openness certification."})
        break
bundle = {"spec": "mathbrain-draft-v1", "author_agent": "w471",
          "bundle_slug": "c0052-lee-yang-normalized-zero-route-001", "entries": entries, "relations": relations}

# Local schema checks only, never a store integration or correctness certificate.
keys = {entry["key"] for entry in entries}
required = {"key", "namespace", "logical_name", "kind", "title", "statement", "proof_text", "assumptions", "domain", "source"}
assert len(keys) == len(entries) <= 200
for entry in entries:
    assert required <= entry.keys()
    assert entry["kind"] == "concept" and entry["proof_text"] is None
    assert entry["source"]["license"].startswith("owner-own-work")
    assert "DRAFT" in entry["statement"]
adj = {key: [] for key in keys}
for relation in relations:
    assert relation["from_key"] in keys and relation["rationale"]
    assert relation["kind"] in {"depends_on", "defines", "proves", "refutes", "generalizes", "specializes", "analogous_to", "cites", "semantic_association"}
    assert relation["kind"] != "proves"
    if "to_key" in relation:
        assert relation["to_key"] in keys
        if relation["kind"] == "depends_on":
            adj[relation["from_key"]].append(relation["to_key"])
def walk(key, ancestors):
    assert key not in ancestors, "depends_on cycle"
    for successor in adj[key]:
        walk(successor, ancestors | {key})
for key in keys:
    walk(key, set())

inbox = Path("~/math-brain-inbox/w471")
expected = Path("~/math-brain-inbox/w471").resolve()
assert inbox.resolve() == expected and expected.name == "w471"
inbox.mkdir(parents=True, exist_ok=True)
number = 1
while (inbox / f"bundle_{number:03d}.json").exists() or (inbox / f"bundle_{number:03d}.part").exists():
    number += 1
part = inbox / f"bundle_{number:03d}.part"
final = inbox / f"bundle_{number:03d}.json"
assert part.resolve().parent == expected and final.resolve().parent == expected
with part.open("x", encoding="utf-8") as handle:
    json.dump(bundle, handle, ensure_ascii=False, indent=2)
    handle.write("\n")
part.rename(final)
state = {"timestamp": timestamp, "bundle_path": str(final),
         "submitted": {"state": "draft placed in named inbox", "confirmed": True},
         "reviewed": {"state": "pending w473; no independent KEEP", "confirmed": False},
         "ingested": {"state": "not confirmed; live integrator not invoked by author", "confirmed": False},
         "retrievable": {"state": "not checked for this new bundle", "confirmed": False},
         "entries": len(entries), "relations": len(relations),
         "local_schema_check": "PASS (including allowed kinds, owner-own-work tags and acyclic dependencies)",
         "bundle_manifest_or_digest_generated": False,
         "response_side_served_model_receipt": None}
(HERE / "BUNDLE_STATE.json").write_text(json.dumps(state, indent=2) + "\n", encoding="utf-8")

report_path = HERE / "REPORT.md"
report = report_path.read_text(encoding="utf-8").replace(
    "No before/after recall improvement is claimed because nothing is ingested yet.",
    "No before/after recall improvement is claimed; ingestion and retrieval of this draft have not been confirmed.")
report_path.write_text(report, encoding="utf-8")

# Freeze only local review documents, not a bundle source manifest/digest.
review_files = ["STATEMENT_PACKET.md", "ROUTE_PRECOMMIT.md", "ATTEMPT.md", "CLAIMS.jsonl", "SOURCE_STATUS.json", "REPORT.md", "REVIEW_PACKET.md", "check_lemmas.py", "MEASUREMENTS.json", "LOCAL_SOURCE_RECEIPT.json"]
hashes = {name: hashlib.sha256((HERE / name).read_bytes()).hexdigest() for name in review_files}
(HERE / "REVIEW_HASHES.json").write_text(json.dumps({"purpose": "local review packet freeze, not mathematical proof or bundle source ceremony", "timestamp": timestamp, "sha256": hashes}, indent=2) + "\n", encoding="utf-8")
(HERE / "HANDOFF_MESSAGES.md").write_text(
    "Statement-only handoff for w472: STATEMENT_PACKET.md; do the independent attempt before opening ATTEMPT.md.\n\n"
    "Complete handoff for w473: REVIEW_PACKET.md, ATTEMPT.md, CLAIMS.jsonl, REVIEW_HASHES.json. "
    f"ATTEMPT.md SHA256: {hashes['ATTEMPT.md']}. Disposition required per conditional lemma; parent remains unproved.\n\n"
    "Progress event staged under folder-only restrictions: w471 C0052 saved 2 conditional Lee-Yang lemmas, 23 analytical/finite controls and 8 geometry controls passed; normalized-zero bound unproved; DRAFT concepts submitted, review pending. Row S1.C0052.w471; evidence ~/brain_workers/w471/REPORT.md.\n\n"
    "NEXT: Referee audits L1/L2; prove a bounded normalized first-zero subsequence for the exact selected 3D Gibbs blocks.\n",
    encoding="utf-8")
print(json.dumps({"bundle_path": str(final), "entries": len(entries), "relations": len(relations),
                  "schema_check": "PASS", "attempt_sha256": hashes["ATTEMPT.md"], "parent_solved": False}))
