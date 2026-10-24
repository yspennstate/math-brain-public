"""Build worker-local drafts, exact relation receipts and reviewable new-file diffs."""
import difflib
import json
import shutil
from pathlib import Path

ROOT = Path(__file__).resolve().parent
proof = (ROOT / "BRIDGE_PROOF.md").read_text(encoding="utf-8")
claims = [json.loads(line) for line in (ROOT / "CLAIMS.jsonl").read_text(encoding="utf-8-sig").splitlines() if line.strip()]
by_id = {claim["id"]: claim for claim in claims}
cards = json.loads((ROOT / "brain_cards.json").read_text(encoding="utf-8"))
existing = {card["metadata"]["logical_id"]: card for group in cards["groups"] for card in group["cards"]}


def section(begin: str, end: str) -> str:
    return proof.split(begin, 1)[1].split(end, 1)[0].strip()


def entry(key: str, logical: str, kind: str, title: str, statement: str, assumptions: list[str], proof_text: str | None) -> dict:
    return {
        "key": key,
        "namespace": "probability.pointprocesses",
        "logical_name": logical,
        "kind": kind,
        "title": title,
        "statement": ("DRAFT; one independent conditional KEEP from w551, further admission pending. " if key in {"lem-shield", "lem-covariance", "lem-polynomial"} else "DRAFT; author-proved special case, independent audit pending. " if kind == "lemma" else "DRAFT; independent review pending. ") + statement,
        "proof_text": proof_text,
        "assumptions": assumptions,
        "domain": "probability theory; planar point processes",
        "source": {
            "source_id": "owner-probability-campaign-20261010:w549:"+key,
            "url": "urn:owner:probability-campaign:20261010:w549:"+key,
            "revision": "worker-draft-2026-10-10-partial-independent-audit",
            "license": "owner-own-work (campaign auxiliary proof or refuted route; DRAFT)",
            "excerpt": None,
        },
    }


geometry = ["stationary simple locally finite planar point process of finite positive intensity", "bounded Voronoi cells and finite nonempty edge-neighbor sets", "no four points cocircular, no three collinear, unique nearest nuclei at deterministic observation points", "spatial nearest-cell field, without Palm conditioning"]
field = "For a simple locally finite planar point configuration with unique nearest nucleus p_x to a deterministic observation point x and finite nonempty Delaunay edge-neighbor set N(p_x), identify R^2 with C and set F6(x)=|N(p_x)|^(-1) sum_{q in N(p_x)} ((q-p_x)/|q-p_x|)^6. Here two nuclei are neighbors when their Voronoi cells share an edge. This bounded complex spatial mark satisfies |F6|<=1 and differs from a mark evaluated at Palm-conditioned particles."
alpha = "For a point process Phi and Borel regions A,B, define alpha_Phi(A,B)=sup |P(E intersect H)-P(E)P(H)| over all events E measurable from Phi restricted to A and H from Phi restricted to B. This is a dependence coefficient of entire local event sigma fields, not a particle-density pair covariance. A bound for growing regions must state uniform dependence on their sizes; a fixed-pair qualitative dynamical mixing limit is a different condition."
g1 = by_id["w549-P0321-G1"]
g3_statement = "Let Phi be a stationary simple locally finite planar point process with finite positive intensity, bounded Voronoi cells, finite nonempty edge-neighbor sets, no four cocircular points, no three collinear points, and almost surely unique nearest nuclei p_x at deterministic observation points. Define F6(x) as the mean of ((q-p_x)/|q-p_x|)^6 over its Delaunay edge-neighbors. Put C6(x,y)=E[F6(x)conjugate(F6(y))]-E[F6(x)]E[conjugate(F6(y))], V(t)=P(Phi intersect B(0,t) is empty), and alpha(A,B)=sup |P(E intersect H)-P(E)P(H)| over events of the restrictions to A and B. Then for every r>0 and deterministic x,y, |C6(x,y)| <=16alpha(B(x,3r),B(y,3r))+28V(r/32). No independence of empty-disk events is needed."
g5_statement = g3_statement.split("Then for every", 1)[0] + "Suppose for D=|x-y|>6r and r>=r0, uniformly in x,y,r, alpha(B(x,3r),B(y,3r))<=Am(1+r)^kappa(1+D-6r)^(-p), and V(t)<=Av exp(-a t^nu) for t>=t0, with p,a,nu>0, kappa>=0, and finite Am,Av. Then |C6(x,y)|=O(D^(-p)(log D)^(kappa/nu)). Thus an eventual lower bound cD^(-eta), c,eta>0, is impossible when p>eta. This is a conditional correlation-transfer result and does not construct a Riesz Gibbs phase."
k1 = by_id["w549-P0321-K1"]
bad_route = "INVALID GENERAL INFERENCE: decay of centered particle-density or coordinate pair correlations is sufficient by itself to infer decay of dependence between every local event or every nonlinear bond observable. The pair-correlation hypotheses omit higher-order joint information. The shared-parity-block counterexample has all distinct variable pairs independent but whole-block dependence alpha=1/4 at every separation. This diagnostic refutes the general probabilistic inference; it asserts no Riesz point-process realization."
retrieval_gap = "A measure-preserving map T is dynamically mixing when mu(T^(-n)A intersect B) tends to mu(A)mu(B) for each fixed event pair. That condition supplies no rate, no growing-window size control, no planar Delaunay stabilization, and no empty-disk estimate. It cannot by itself be used as the quantitative point-process alpha hypothesis of a Delaunay covariance bridge. A Bernoulli shift illustrates the quantifier distinction: for an event B of probability 1/2 and A_n=T^nB, the unrestricted event covariance equals 1/4 for every n despite fixed-event mixing. This does not deny independence of separated finite Bernoulli windows."
entries = [
    entry("def-spatial-sixfold", "spatial-nearest-cell-delaunay-sixfold-bond-mark", "definition", "Spatial nearest-cell Delaunay six-fold bond mark", field, geometry[1:], None),
    entry("def-local-alpha", "local-event-alpha-dependence-for-point-process-windows", "definition", "Local event alpha dependence for point-process windows", alpha, ["a point process and two Borel regions"], None),
    entry("lem-shield", "seven-disk-shield-for-delaunay-bond-localization", "lemma", "Seven-disk shield for Delaunay bond localization", g1["statement"], g1["assumptions"], section("Lemma G1 (deterministic shield).", "Lemma G2 (local approximants).")),
    entry("lem-covariance", "delaunay-sixfold-covariance-localization-with-void-error", "lemma", "Delaunay six-fold covariance localization with void error", g3_statement, geometry, section("Lemma G2 (local approximants).", "Corollary G4 (exponential or stretched exponential process mixing excludes algebraic bond order).")),
    entry("lem-polynomial", "delaunay-bond-polynomial-mixing-transfer-up-to-logarithms", "lemma", "Delaunay bond polynomial mixing transfer up to logarithms", g5_statement, geometry+["uniform window-size dependence Am(1+r)^kappa and spatial rate p", "stretched exponential empty-disk bound with constants a,nu>0"], section("Corollary G5 (polynomial mixing preserves the exponent up to logarithms).", "Corollary G6 (necessary block dependence).")),
    entry("lem-parity", "shared-parity-blocks-with-pair-independence-and-long-range-event-dependence", "lemma", "Shared parity blocks: independent pairs and persistent event dependence", k1["statement"], k1["assumptions"], (ROOT / "REASONING_FAILURE.md").read_text(encoding="utf-8").split("Measurement:", 1)[0]),
    entry("route-pair-mixing", "invalid-pair-decorrelation-to-local-event-mixing-inference", "concept", "Invalid pair-decorrelation to local-event-mixing inference", bad_route, ["general probabilistic inference; no Riesz-specific extra theorem supplied"], None),
    entry("gap-mixing-scope", "dynamical-mixing-card-missing-quantitative-growing-window-hypotheses", "concept", "Dynamical mixing misses quantitative growing-window hypotheses", retrieval_gap, ["fixed-event qualitative mixing is the only supplied dynamical hypothesis"], None),
]
relations = [
    {"from_key": "lem-covariance", "to_key": "lem-shield", "kind": "depends_on", "rationale": "The shield says 'determined by the restriction to B(x,3r)'; the covariance bridge uses '28V(r/32)' as its localization error."},
    {"from_key": "lem-covariance", "to_key": "def-spatial-sixfold", "kind": "depends_on", "rationale": "Both ends explicitly define F6 from the Delaunay neighbors of the nearest spatial nucleus, so the theorem matches this observable."},
    {"from_key": "lem-covariance", "to_key": "def-local-alpha", "kind": "depends_on", "rationale": "The conclusion uses '16alpha(B(x,3r),B(y,3r))'; the definition takes the supremum over 'entire local event sigma fields'."},
    {"from_key": "lem-polynomial", "to_key": "lem-covariance", "kind": "depends_on", "rationale": "The polynomial transfer substitutes explicit size and void bounds into '|C6(x,y)| <=16alpha+28V'."},
    {"from_key": "lem-parity", "to_key": "route-pair-mixing", "kind": "refutes", "rationale": "The lemma has 'Every distinct variable pair is independent' but 'strong event-mixing coefficient ... equals 1/4'; this refutes the route that pair decay alone implies full local-event decay."},
]
target = "math:probability.core:open-problem-p0321-existence-of-a-hexatic-phase-for-two-dimensional-riesz-gases"
prior = "math:probability.core:attempt-p0321-existence-of-a-hexatic-phase-for-two-dimensional-riesz-gases"
mixing = "math:dynamics.ergodic:mixing-definition"
if target in existing:
    relations.append({"from_key": "lem-polynomial", "to_existing_logical": target, "kind": "semantic_association", "rationale": "The target requires orientational order with absent crystalline positional order; the conditional transfer identifies uniform local-event mixing that would exclude a slower algebraic orientational lower bound. It does not prove or refute phase existence."})
if prior in existing:
    relations.append({"from_key": "lem-covariance", "to_existing_logical": prior, "kind": "semantic_association", "rationale": "The prior warns that zero one-point orientation does not eliminate two-point order; this bridge controls the centered two-point mark covariance rather than inferring it from the mean. The prior is author-only unreviewed."})
if mixing in existing:
    relations.append({"from_key": "gap-mixing-scope", "to_existing_logical": mixing, "kind": "semantic_association", "rationale": "The retrieved definition uses a limit for each fixed measurable A,B and gives no rate. The draft scope gap distinguishes this from a supremum over spatial restriction events with growing-window control; it does not refute the definition."})

allowed_relations = {"depends_on", "defines", "proves", "refutes", "generalizes", "specializes", "analogous_to", "cites", "semantic_association"}
keys = {item["key"] for item in entries}
assert len(keys) == len(entries) <= 200
for item in entries:
    assert item["source"]["license"].startswith("owner-own-work")
    assert item["statement"] and item["kind"] in {"definition", "lemma", "theorem", "concept"}
    assert bool(item["proof_text"]) == (item["kind"] in {"lemma", "theorem"})
for relation in relations:
    assert relation["kind"] in allowed_relations and relation["from_key"] in keys
    assert relation.get("to_key") in keys or relation.get("to_existing_logical") in existing
deps = {key: [] for key in keys}
for relation in relations:
    if relation["kind"] == "depends_on":
        deps[relation["from_key"]].append(relation["to_key"])


def visit(key: str, path: tuple[str, ...] = ()) -> None:
    assert key not in path
    for child in deps[key]:
        visit(child, path+(key,))


for key in keys:
    visit(key)
bundle = {"spec": "mathbrain-draft-v1", "author_agent": "w549", "bundle_slug": "p0321-delaunay-covariance-bridge-001", "entries": entries, "relations": relations}
(ROOT / "bundle_001.json").write_text(json.dumps(bundle, ensure_ascii=False, indent=2), encoding="utf-8")
by_key = {item["key"]: item for item in entries}
relation_rows = []
for relation in relations:
    target_statement = by_key[relation["to_key"]]["statement"] if "to_key" in relation else existing[relation["to_existing_logical"]]["body"]
    relation_rows.append({**relation, "from_statement": by_key[relation["from_key"]]["statement"], "to_statement": target_statement, "review_state": "edge-specific admission pending; geometry/covariance claims conditionally kept", "independent_reviewer": "w551"})
(ROOT / "RELATIONS.jsonl").write_text("".join(json.dumps(row, ensure_ascii=False)+"\n" for row in relation_rows), encoding="utf-8")

patch_dir = ROOT / "patches"
patch_dir.mkdir(exist_ok=True)
for name, local, live in [
    ("01_bridge_hypothesis_gate.diff", ROOT/"proposed/bridge_hypothesis_gate.py", "~/math-brain-build/src/math_brain/bridge_hypothesis_gate.py"),
    ("02_probability_hook.diff", ROOT/"proposals/probability-w549.jsonl", "~/primary_directive/hooks1000/proposals/probability-w549.jsonl"),
]:
    diff = "".join(difflib.unified_diff([], local.read_text(encoding="utf-8").splitlines(keepends=True), fromfile="a/"+live, tofile="b/"+live))
    assert diff.startswith("--- a/"+live+"\n+++ b/"+live+"\n")
    (patch_dir/name).write_text(diff, encoding="utf-8")

verification = json.loads((ROOT / "verification.json").read_text(encoding="utf-8"))
assert verification["status"] == "PASS"
receipt = {"command": "python -X utf8 make_deliverables.py", "status": "PASS", "entries": len(entries), "relations": len(relations), "proof_bearing_entries": sum(e["kind"] == "lemma" for e in entries), "dependency_graph": "acyclic", "source_license_prefixes": "accepted owner-own-work tag", "cross_bundle_ends_found_in_read_only_population_store": 3, "cryptographic_manifests_computed": False, "independently_reviewed": False, "ingested": False, "retrievable_new_nodes": False}
(ROOT / "draft_validation.json").write_text(json.dumps(receipt, indent=2), encoding="utf-8")
print(json.dumps(receipt, indent=2))
