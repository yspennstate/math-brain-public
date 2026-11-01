"""Prepare and validate a small draft; never ingest or mutate the live store."""
import json
from pathlib import Path
import os

root = Path(__file__).resolve().parent
claims = [json.loads(line) for line in (root / "CLAIMS.jsonl").read_text(encoding="utf-8").splitlines() if line.strip()]
claim_by_id = {claim["id"]: claim for claim in claims}
cards = json.loads((root / "MATH_BRAIN_CARDS.json").read_text(encoding="utf-8"))
measurements = json.loads((root / "MEASUREMENTS.json").read_text(encoding="utf-8"))
theorem_id = "claim_c83c8a10ed54143e4ef3f372de021aed7fa80a9a7c8a05662da7b7c61b5a7615"
theorem = next(card for card in cards["cards"] if card["id"] == theorem_id)

def entry(key, name, title, statement, assumptions, source_file="ATTEMPT.md"):
    return {"key": key, "namespace": "probability.percolation", "logical_name": name,
            "kind": "concept", "title": title,
            "statement": "DRAFT; independent check pending from w431. " + statement,
            "proof_text": None, "assumptions": assumptions,
            "domain": "probability: nearest-neighbour percolation and dependent-site renormalization",
            "source": {"source_id": "owner-own-work:w430:C0023:" + key,
                       "url": (root / source_file).as_uri(), "revision": "2026-10-10",
                       "license": "owner-own-work (campaign deductions; cited literature attributed)",
                       "excerpt": None}}

entries = []
definitions = [
    ("001", "pointwise-limit-obstruction", "critical-percolation-pointwise-limit-obstruction", "Draft obstruction: subcritical pointwise decay does not pass to criticality", "ATTEMPT.md"),
    ("002", "uniform-exponential-obstruction", "critical-percolation-uniform-exponential-rate-obstruction", "Draft obstruction: no uniform positive exponential rate up to criticality", "ATTEMPT.md"),
    ("003", "coarsened-dependent-field", "dependent-site-percolation-square-coarsening-criterion", "Draft criterion: polynomial dependence-range threshold by whole-square coarsening", "REVIEW_PACKET.md"),
    ("004", "comparison-parameter-gap", "critical-percolation-green-magnetization-parameter-gap", "Draft obstruction: comparison parameter stays below criticality at positive density", "ATTEMPT.md"),
]
for suffix, key, name, title, file in definitions:
    claim = claim_by_id["w430-C0023-" + suffix]
    entries.append(entry(key, name, title, claim["statement"], claim["assumptions"], file))

old_statement = (
    "Let d>=2 and integer r>=0. Let X be a {0,1}-valued field on Z^d whose sigma-fields "
    "on any two vertex sets at infinity-norm distance greater than r are independent. "
    "If P(X_x=0)<=64^(-(r+1)^2) for every x, the origin has positive probability of "
    "belonging to an infinite nearest-neighbour good component. This is w429 L2, "
    "the conservative parity-color and bad-star-contour criterion; it assumes setwise "
    "independence, not merely pairwise independence. Independent review is pending."
)
old = entry("fixed-range-contour", "dependent-site-percolation-fixed-range-contour-criterion",
            "Draft reference criterion: fixed-range coloring and contours", old_statement,
            ["d>=2", "integer r>=0", "Setwise sigma-field independence at distances >r", "Uniform bad marginals"],
            "REVIEW_PACKET.md")
old["source"]["source_id"] = "owner-own-work:w429:C0023:L2:attributed-by-w430"
old["source"]["url"] = Path("~/brain_workers/w429/ATTEMPT.md").as_uri()
entries.append(old)

gap_statement = (
    "In nearest-neighbour Bernoulli bond percolation on Z^d, d>=2, let p_c in (0,1). "
    "Suppose there are fixed events G_z, z in a coarse Z^2, each determined by at most "
    "M>=1 bond bits. For coarse index sets at infinity-norm distance >integer r>=0, "
    "assume the unions of their determining edge sets are disjoint. Assume every infinite "
    "nearest-neighbour collection of good indices yields an infinite physical open cluster "
    "for every configuration. If P_(p_c)(G_z fails)<=delta<epsilon_r=64^-4/(r+1)^2 uniformly "
    "in z, then eta=min(p_c/2,(epsilon_r-delta)/(2M))>0 preserves bad marginals below epsilon_r "
    "at p'=p_c-eta, giving percolation below p_c by the candidate square-coarsening criterion, "
    "a contradiction. The unproved premise for C0023 is existence, from hypothetical "
    "theta(p_c)>0, of such fixed local compatible blocks with this quantitative margin. "
    "Qualitative density tending to one with uncontrolled r does not establish it."
)
entries.append(entry("critical-block-gap", "critical-percolation-polynomial-block-margin-gap",
                     "Draft conditional bridge and unresolved critical block construction", gap_statement,
                     ["The square-coarsening criterion remains independently unchecked",
                      "Fixed local determining sets at both p_c and p'",
                      "Configuration-wise deterministic compatibility", "Uniform delta margin"],
                     "REVIEW_PACKET.md"))

relations = [
    {"from_key": "coarsened-dependent-field", "to_key": "fixed-range-contour", "kind": "depends_on",
     "rationale": "Whole-good squares of side r+1 form a setwise 1-dependent field on a coordinate plane, with bad marginal <=(r+1)^2 delta. The fixed-range criterion at r=1 requires bad marginal <=64^-4. Adjacent fully good squares connect through their faces."},
    {"from_key": "critical-block-gap", "to_key": "coarsened-dependent-field", "kind": "depends_on",
     "rationale": "A coupling changes any fixed M-bit event probability by at most M*eta. The stated strict margin keeps the same compatible block field under the candidate criterion at p_c-eta. This relation does not assert existence of the blocks."},
    {"from_key": "comparison-parameter-gap", "to_existing_logical": theorem["metadata"]["logical_id"], "kind": "cites",
     "rationale": "The retrieved comparison theorem uses q=p(1-m_h(p)), h>0. The new deduction expands the omitted magnetization definition and shows q_h->p_c requires theta(p_c)=0; it cites and does not refute the comparison theorem."},
    {"from_key": "comparison-parameter-gap", "to_key": "uniform-exponential-obstruction", "kind": "analogous_to",
     "rationale": "These are distinct endpoint obstructions: a hypothetical positive critical density prevents the comparison parameter approaching p_c, while the finite-set threshold prevents any uniformly positive exponential rate across all p just below p_c."},
]
bundle = {"spec": "mathbrain-draft-v1", "author_agent": "w430",
          "bundle_slug": "critical-percolation-quantitative-bridge-w430-001",
          "entries": entries, "relations": relations}

allowed_kinds = {"definition", "lemma", "theorem", "concept"}
allowed_relations = {"depends_on", "defines", "proves", "refutes", "generalizes", "specializes", "analogous_to", "cites", "semantic_association"}
by_key = {e["key"]: e for e in entries}
assert len(by_key) == len(entries) <= 200
assert all(e["kind"] in allowed_kinds and e["kind"] == "concept" and e["proof_text"] is None for e in entries)
assert all(e["source"]["license"].startswith("owner-own-work") for e in entries)
assert all(e["statement"].startswith("DRAFT;") for e in entries)
assert all(r["kind"] in allowed_relations and r["from_key"] in by_key for r in relations)
assert all((r.get("to_key") in by_key) or r.get("to_existing_logical") == theorem["metadata"]["logical_id"] for r in relations)
dependencies = {key: [] for key in by_key}
for relation in relations:
    if relation["kind"] == "depends_on":
        dependencies[relation["from_key"]].append(relation["to_key"])
def visit(key, stack):
    assert key not in stack, "Cyclic depends_on relation"
    for target in dependencies[key]:
        visit(target, stack + [key])
for key in by_key:
    visit(key, [])

edge_rows = []
for i, relation in enumerate(relations, 1):
    source = by_key[relation["from_key"]]
    destination = by_key.get(relation.get("to_key"))
    edge_rows.append({"id": "w430-C0023-E%02d" % i, "relation": relation,
                      "from_statement_quote": source["statement"],
                      "to_statement_quote": destination["statement"] if destination else "let q = p(1 −mh(p))",
                      "to_existing_id": None if destination else theorem_id,
                      "independent_reviewer": "w431 pending; validating coordinator handles account-separated edge audits",
                      "status": "DRAFT", "remaining_gap": "No ingestion or theorem promotion; claim checks and target block construction pending."})
(root / "EDGE_ROWS.jsonl").write_text("".join(json.dumps(row, ensure_ascii=False)+"\n" for row in edge_rows), encoding="utf-8")

retrieved_claims = [c for c in cards["cards"] if c["kind"] == "claim"]
failure = {"query": "nearest neighbour Bernoulli percolation sharpness subcritical exponential decay critical continuity",
           "command": "PYTHONPATH=~/math-brain-build/src; python -X utf8 -m math_brain.cli recall ~/math-brain-build/local/population/brain.sqlite3 <query> --limit 5",
           "hit_count": len(cards["query"]["hits"]), "claim_hit_count": len(retrieved_claims),
           "before_claim_hits_with_statement_in_cli": sum("statement" in h or "body" in h for h in cards["query"]["hits"] if h["kind"]=="claim"),
           "after_claim_bodies_resolved": len(retrieved_claims),
           "claims_with_empty_structured_assumptions": sum(not c["claim_payload"]["assumptions"] for c in retrieved_claims),
           "claims_without_fidelity_review": sum(not c["metadata"].get("statement_fidelity_reviewed", False) for c in retrieved_claims),
           "zero_warning_claim_hits": sum(h["warning_score"]==0 for h in cards["query"]["hits"] if h["kind"]=="claim"),
           "exact_card_resolution_seconds": cards["elapsed_seconds"],
           "bounded_repair_command": "python -X utf8 ~/brain_workers/w430/read_brain_cards.py",
           "bounded_repair": "Read only the returned IDs, inspect inline and structured assumptions and fidelity status, and verify missing symbol definitions against the primary source before checking applicability.",
           "specific_failure": "Theorem 2 title/score exposed neither q=p(1-m_h(p)) nor definitions; the harvested body leaves m_h and psi_n undefined. Assuming q_h->p_c at positive critical density is circular.",
           "limitation": "Local diagnostic repair, not deployed; 0->4 exposed bodies is transparency, not improved mathematical correctness or a global recall score."}
(root / "RETRIEVAL_FAILURE.json").write_text(json.dumps(failure, indent=2), encoding="utf-8")

payload = json.dumps(bundle, indent=2, ensure_ascii=False)+"\n"
(root / "bundle_001.json").write_text(payload, encoding="utf-8")
inbox = Path("~/math-brain-inbox/w430").resolve()
assert inbox.as_posix().lower() == "~/math-brain-inbox/w430"
inbox.mkdir(exist_ok=True)
target = inbox / "bundle_001.json"
part = inbox / "bundle_001.part"
if target.exists():
    assert target.read_text(encoding="utf-8") == payload, "Refuse to overwrite a different submitted draft"
else:
    assert not part.exists(), "Refuse to overwrite an existing in-progress draft"
    part.write_text(payload, encoding="utf-8")
    os.replace(part, target)

lifecycle = {"bundle": target.as_posix(), "prepared": True, "submitted": True,
             "reviewed": False, "ingested": False, "retrievable": False,
             "independent_reviewer": "w431", "entries": len(entries), "relations": len(relations),
             "local_schema_checks": "passed; required fields, kinds, source prefix, endpoint resolution, acyclic dependencies, concept-only draft labels",
             "limits": "Local schema checks are not integrator acceptance or mathematical proof; coordinator provides source/store ceremony after independent audits."}
(root / "BRAIN_LIFECYCLE.json").write_text(json.dumps(lifecycle, indent=2), encoding="utf-8")
print(json.dumps({"submission": lifecycle, "retrieval_diagnostic": failure, "r2_threshold_ratio": measurements["rows"][2]["candidate_to_old_ratio"]}, indent=2))
