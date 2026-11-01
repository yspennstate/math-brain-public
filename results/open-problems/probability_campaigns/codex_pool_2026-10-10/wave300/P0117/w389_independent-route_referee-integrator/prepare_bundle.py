"""Prepare and validate a draft locally; never invoke the live integrator."""
import difflib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent
NAMESPACE = "probability.fpp"
EXISTING_PARENT = "math:probability.core:open-problem-p0117-absence-of-bi-infinite-geodesics-in-planar-iid-fpp"
EXISTING_ATTEMPT = "math:probability.core:attempt-p0117-absence-of-bi-infinite-geodesics-in-planar-iid-fpp"


def source(claim):
    return {"source_id": "owner-probability-campaign:w389:" + claim,
            "url": "urn:owner:probability:P0117:w389:" + claim,
            "revision": "author-checked-draft-2026-10-10",
            "license": "owner-own-work (independent audit pending)", "excerpt": None}


def entry(key, name, kind, title, statement, assumptions, claim):
    return {"key": key, "namespace": NAMESPACE, "logical_name": name,
            "kind": kind, "title": title, "statement": statement,
            "proof_text": None, "assumptions": assumptions,
            "domain": "probability theory; planar first-passage percolation",
            "source": source(claim)}


def validate(bundle):
    required = {"key", "namespace", "logical_name", "kind", "title", "statement",
                "proof_text", "assumptions", "domain", "source"}
    allowed = {"depends_on", "defines", "proves", "refutes", "generalizes",
               "specializes", "analogous_to", "cites", "semantic_association"}
    entries = bundle["entries"]
    keys = {value["key"] for value in entries}
    if len(keys) != len(entries) or len(entries) > 200:
        raise ValueError("Duplicate keys or entry bound violated")
    graph = {key: [] for key in keys}
    for value in entries:
        if required - value.keys():
            raise ValueError("Missing entry fields")
        if value["kind"] not in {"definition", "concept"} or value["proof_text"] is not None:
            raise ValueError("Unreviewed own work must stay concept/definition material")
        if not value["source"]["license"].startswith("owner-own-work"):
            raise ValueError("Wrong owner source license tag")
        if not value["statement"] or not value["assumptions"]:
            raise ValueError("Missing mathematical statement or assumptions")
    for relation in bundle["relations"]:
        if relation["kind"] not in allowed or relation["from_key"] not in keys:
            raise ValueError("Invalid relation kind or source")
        if "to_key" in relation:
            if relation["to_key"] not in keys:
                raise ValueError("Missing relation endpoint")
            if relation["kind"] == "depends_on":
                graph[relation["from_key"]].append(relation["to_key"])
        elif relation.get("to_existing_logical") not in {EXISTING_PARENT, EXISTING_ATTEMPT}:
            raise ValueError("Unverified existing endpoint")
    active, finished = set(), set()

    def visit(key):
        if key in active:
            raise ValueError("Dependency cycle")
        if key in finished:
            return
        active.add(key)
        for target in graph[key]:
            visit(target)
        active.remove(key)
        finished.add(key)

    for key in graph:
        visit(key)


def main():
    entries = [
        entry("centered-certificate", "planar-fpp-centered-two-arm-geodesic-certificate", "definition",
              "Centered two-arm finite geodesic certificate",
              "For a finite nonnegative edge-weight field on nearest-neighbor Z^2, H_m(v) is the event that there is a self-avoiding finite path (z_-m,...,z_m) with z_0=v, consecutive vertices adjacent, and total cost equal to the infimum over ALL finite lattice paths between z_-m and z_m. The two arms each have m edges. Minimize in the entire lattice; confined shortest paths are not this certificate.",
              ["m>=1", "finite nonnegative edge weights", "nearest-neighbor Z^2", "global minimization and simple path witnesses"], "C02-definition"),
        entry("occupation-density", "stationary-planar-fpp-boundary-geodesic-occupation-density-draft", "concept",
              "DRAFT P0117: stationary boundary-geodesic occupation density",
              "AUTHOR-CHECKED DRAFT for P0117; w392 independent audit pending; no novelty or solution claim. For stationary measurable finite nonnegative edge weights on nearest-neighbor Z^2, let B_n=[-n,n]^2 intersect Z^2, A be the vertices on self-avoiding bigeodesics, and D_n be the vertices in B_n on ANY self-avoiding globally minimizing finite path with endpoints on the vertex boundary of B_2n. Paths may leave B_2n, and all geodesics are included if ties occur. Let H_n(0) mean existence of a self-avoiding globally minimizing path (z_-n,...,z_n) with z_0=0 and adjacent consecutive vertices. Then P(0 in A)<=E|D_n|/|B_n|<=P(H_n(0)). Centered-prefix compactness gives P(H_n(0)) decreasing to P(0 in A); hence the expected occupation density tends to P(0 in A). Almost-sure absence of ALL bigeodesics is equivalent to E|D_n|=o(n^2). This iid decay estimate is not proved here.",
              ["translation stationarity", "finite nonnegative edge weights", "global, self-avoiding geodesics", "union over all finite geodesics with the specified endpoints"], "C02"),
        entry("shell-lower-bound", "infinite-geodesic-ray-shell-incidence-positive-lower-bound-draft", "concept",
              "DRAFT P0117 audit scar: an infinite ray must cross every shell",
              "AUTHOR-CHECKED DRAFT for P0117; w392 independent audit pending. Let T_0 be the union of all infinite simple nearest-neighbor paths from 0 in Z^2 whose every finite segment globally minimizes passage time, q(x)=P(x in T_0), and S_n={x:||x||_infinity=n}. Every such ray hits S_n, so sum_{x in S_n}q(x)=E|T_0 intersect S_n|>=P(T_0 nonempty). If a ray exists almost surely, the sum is at least 1 for every n and sup_{x in S_n}q(x)>=1/(8n). Thus vanishing raw forward-ray shell incidence and the uniform rate o(1/n) are impossible in this setting. This concerns forward rays and does not imply a bigeodesic exists.",
              ["n>=1", "simple infinite nearest-neighbor rays from 0", "P(T_0 nonempty)=1 for the numerical lower bound 1"], "C03"),
        entry("refuted-shell-route", "planar-fpp-vanishing-forward-ray-shell-sum-refuted-route", "concept",
              "REFUTED closing step: make forward-ray shell incidence vanish",
              "AUTHOR-CHECKED AUDIT SCAR; w392 independent review pending; not a theorem proving absence. A proposed route defines T_x as the union of all infinite geodesic rays from x and uses the valid stationary inequality P(bigeodesic through 0)<=one-half times sum_{x in S_n}P(-x in T_0). Its proposed closing estimate, that this raw shell sum vanishes along a subsequence or that the shell maximum is o(1/n), is unattainable whenever a ray exists from 0 almost surely: every ray crosses every surrounding shell and the sum is always at least 1. Keep the counting inequality; replace the closing quantity by genuinely two-sided extension witnesses or full boundary-geodesic occupation. The parent P0117 conjecture remains unresolved in this packet.",
              ["translation-stationary nearest-neighbor FPP", "simple geodesic rays", "P(T_0 nonempty)=1", "S_n is the vertex boundary of [-n,n]^2"], "R03-C03"),
    ]
    relations = [
        {"from_key": "occupation-density", "to_key": "centered-certificate", "kind": "depends_on",
         "rationale": "The density sandwich uses centered globally minimizing simple paths; a finitely branching prefix tree identifies their intersection with a bigeodesic through the center. Author-checked draft; independent audit pending."},
        {"from_key": "shell-lower-bound", "to_key": "refuted-shell-route", "kind": "refutes",
         "rationale": "The lower-bound card gives shell sum >=1 when a ray exists almost surely. The refuted route proposes that exactly this raw forward-ray shell sum tend to zero. These two numerical assertions are incompatible. Independent audit pending."},
        {"from_key": "occupation-density", "to_key": "refuted-shell-route", "kind": "semantic_association",
         "rationale": "Occupation by all long boundary-to-boundary finite geodesics is an attainable equivalent target for bigeodesic absence, while the raw forward-ray shell sum cannot vanish. No proof of occupation decay is supplied."},
        {"from_key": "occupation-density", "to_existing_logical": EXISTING_PARENT, "kind": "semantic_association",
         "rationale": "The existing P0117 concept asks for absence of bi-infinite geodesics under continuous iid planar weights. This stationary occupation reduction expresses that absence as a precise subquadratic expected occupation estimate without importing an unproved directional regularity condition."},
        {"from_key": "centered-certificate", "to_existing_logical": EXISTING_ATTEMPT, "kind": "semantic_association",
         "rationale": "The existing attempt warns that unanchored opposite-endpoint geodesics can escape each fixed ball. The certificate explicitly requires the center and two arms of growing length, which supplies an anchor for compactness; it does not show such certificates occur or disappear."},
    ]
    bundle = {"spec": "mathbrain-draft-v1", "author_agent": "w389",
              "bundle_slug": "p0117-occupation-and-impossible-shell-closure-20261010",
              "entries": entries, "relations": relations}
    validate(bundle)
    drafts = ROOT / "drafts"
    drafts.mkdir(exist_ok=True)
    temporary = drafts / "bundle_001.part"
    final = drafts / "bundle_001.json"
    temporary.write_text(json.dumps(bundle, indent=2) + "\n", encoding="utf-8")
    temporary.replace(final)

    live = json.loads((ROOT / "live_store_check.json").read_text(encoding="utf-8"))
    existing = {}
    for database in live:
        for row in database.get("target_rows", []):
            logical = row.get("metadata", {}).get("logical_id")
            if logical:
                existing[logical] = row["body"]
    evidence = []
    statements = {value["key"]: value["statement"] for value in entries}
    for position, relation in enumerate(relations, 1):
        target = relation.get("to_key", relation.get("to_existing_logical"))
        target_statement = statements[target] if "to_key" in relation else existing[target]
        evidence.append({"row": "S1.P0117.w389.E" + str(position), "relation": relation,
                         "from_statement_quote": statements[relation["from_key"]],
                         "to_statement_quote": target_statement,
                         "review_status": "DRAFT; independent relation audit pending",
                         "source_proof": "ATTEMPT.md C02/C03; REVIEWS.jsonl R02/R03; live_store_check.json"})
    (ROOT / "RELATIONS_EVIDENCE.jsonl").write_text("".join(json.dumps(value) + "\n" for value in evidence), encoding="utf-8")

    validation = {"command": "python -X utf8 prepare_bundle.py", "schema_checks": "PASS",
                  "entries": len(entries), "relations": len(relations),
                  "new_theorem_or_lemma_entries": 0, "license_prefix_checks": "PASS",
                  "dependency_dag_check": "PASS", "relation_end_statements_saved": len(evidence),
                  "mathematical_proof_certificate": False,
                  "live_integrator_run": False, "own_claim_audit": "PENDING w392"}
    (ROOT / "bundle_validation.json").write_text(json.dumps(validation, indent=2) + "\n", encoding="utf-8")

    before = "Therefore vanishing shell sum along any deterministic subsequence n_j->infinity suffices to exclude every bigeodesic; the stronger rate sup_(x in S_n)q(x)=o(1/n) suffices as well. The published q(x)->0 has no stated rate that yields either premise. Its sublinear expected number of tree exit points is compatible with a constant number of exit points caused by a two-ended path. The single hardest remaining piece for this route is proving vanishing shell incidence, not proving compactness or invoking sublinearity again.\n"
    after = "The incidence inequality is correct, but its proposed vanishing right-hand side is unattainable. Every infinite simple ray from 0 hits S_n, so sum_(x in S_n)q(x)>=P(T_0 nonempty)=1 in the standard iid setting. Thus the shell maximum is at least 1/(8n), and neither a vanishing shell sum nor an o(1/n) maximum can hold. Retain this inequality as an audit scar; use genuinely two-sided extension witnesses or full boundary-geodesic occupation for the unresolved closing estimate.\n"
    patches = ROOT / "patches"
    patches.mkdir(exist_ok=True)
    patch = difflib.unified_diff(before.splitlines(True), after.splitlines(True),
                                 fromfile="a/~/brain_workers/w388/ATTEMPT.md",
                                 tofile="b/~/brain_workers/w388/ATTEMPT.md")
    (patches / "01_shell_decay_correction.diff").write_text("".join(patch), encoding="utf-8")
    print(json.dumps(validation))


if __name__ == "__main__":
    main()
