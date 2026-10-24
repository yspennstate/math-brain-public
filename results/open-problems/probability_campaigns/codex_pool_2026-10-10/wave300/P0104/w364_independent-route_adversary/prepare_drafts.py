"""Stage and validate reviewable artifacts, entirely within this worker folder."""
import argparse
import difflib
import itertools
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent
BRAIN_TARGET = "~/math-brain-inbox/w364/bundle_001.json"
HOOK_TARGET = "~/primary_directive/hooks1000/proposals/math-w364.jsonl"
TARGET_LOGICAL = "math:probability.core:open-problem-p0104-subdiffusive-and-kpz-passage-time-fluctuation-exponents"
SOURCE_TAG = {
    "source_id": "owner-own-work:fpp-boundary-profile-audit",
    "url": "urn:math:fpp:boundary-profile-audit:2026-10-10",
    "revision": "draft-2026-10-10",
    "license": "owner-own-work (campaign derivation; independent review pending)",
    "excerpt": None,
}


def entry(key, logical, title, statement, assumptions):
    return {
        "key": key, "namespace": "probability.firstpassage",
        "logical_name": logical, "kind": "concept", "title": title,
        "statement": "Draft audit concept; independent review pending. " + statement,
        "proof_text": None, "assumptions": assumptions,
        "domain": "probability theory", "source": dict(SOURCE_TAG),
    }


def bundle():
    claims = [json.loads(line) for line in (ROOT / "CLAIMS.jsonl").read_text(encoding="utf-8").splitlines()]
    by_id = {c["id"]: c for c in claims}
    es = [
        entry("boundary-matching", "fpp-scalar-block-minima-matching-obstruction",
              "Boundary matching for optimized block passage costs",
              by_id["P0104-W364-C02"]["statement"], by_id["P0104-W364-C02"]["assumptions"]),
        entry("forced-low-pivotality", "fpp-integer-forcing-all-geodesics-criterion",
              "Single-edge forcing and tied minimizing paths",
              by_id["P0104-W364-C05"]["statement"], by_id["P0104-W364-C05"]["assumptions"]),
        entry("centered-error-transfer", "fpp-centered-matching-error-variance-transfer",
              "Variance transfer through a centered matching error",
              by_id["P0104-W364-C03"]["statement"], by_id["P0104-W364-C03"]["assumptions"]),
    ]
    # Spell out the edge labels in the self-contained boundary statement.
    es[0]["statement"] = es[0]["statement"].replace(
        "where A1,A2 are the weights to the two common neighbors and B1,B2 the weights from them to the target",
        "where A1=w((0,0),(1,0)), A2=w((0,0),(0,1)), B1=w((1,0),(1,1)) and B2=w((0,1),(1,1))",
    )
    return {
        "spec": "mathbrain-draft-v1", "author_agent": "w364",
        "bundle_slug": "probability-fpp-boundary-profile-audit-001",
        "entries": es,
        "relations": [
            {"from_key": "centered-error-transfer", "to_key": "boundary-matching",
             "kind": "semantic_association",
             "rationale": "The finite counterexample exhibits an endpoint-matching penalty; the conditional L2 statement specifies sufficient centered-error control to transfer a variance exponent in a sequence of such decompositions."},
            {"from_key": "forced-low-pivotality", "to_key": "boundary-matching",
             "kind": "semantic_association",
             "rationale": "The same positive integer-weight square has tied optimal routes, so preserving the common boundary endpoint and distinguishing all minimizers from a selected minimizer are both necessary audit checks on optimized passage costs."},
            {"from_key": "boundary-matching", "to_existing_logical": TARGET_LOGICAL,
             "kind": "semantic_association",
             "rationale": "The explicit failure of scalar block composition obstructs a candidate method for controlling point-to-point variance exponents; it does not refute the exponent conjecture."},
        ],
    }


def hook():
    return {
        "id": "fpp-boundary-w364-01", "area": "math", "event": "stage-start",
        "cue": "A proof replaces min_y(A(y)+B(y)) by min_y A(y)+min_y B(y), or adds optimized slab variances without retaining the shared boundary endpoint.",
        "fire_when": "In the iid {1,2} square, A=(1,2), B=(2,1): separate block minima give 2 but the actual passage time is 3.",
        "silent_when": "The proof composes min_y(A(y)+B(y)) with the same y, or explicitly keeps and controls the centered matching penalty; slab restrictions are justified.",
        "text": "Before adding optimized block costs, retain the common boundary endpoint and justify the path restriction. Independent edge sets do not make separate minimizers compatible. Check the centered matching error and its covariance before transferring a variance bound.",
        "evidence": "~/brain_workers/w364/measurements/exact_boundary_counterexample.json: 2/16 scalar-stitch errors; Cov(L,T-L)=-1/16. Scar: proof_steps_need_derived_joint_structure_2026_09_09.",
        "proposer": "w364",
    }


def new_file_diff(text, target):
    # The unified headers identify the requested live destination; no live file is opened.
    return "".join(difflib.unified_diff(
        [], text.splitlines(keepends=True),
        fromfile="a/" + target, tofile="b/" + target,
    ))


def validate(data, proposal):
    assert data["spec"] == "mathbrain-draft-v1"
    assert 0 < len(data["entries"]) <= 200
    required = {"key", "namespace", "logical_name", "kind", "title", "statement", "proof_text", "assumptions", "domain", "source"}
    keys = {e["key"] for e in data["entries"]}
    assert len(keys) == len(data["entries"])
    for e in data["entries"]:
        assert required <= e.keys()
        assert e["kind"] == "concept" and e["proof_text"] is None
        assert e["source"]["license"].startswith("owner-own-work")
        assert "independent review pending" in e["statement"]
        public_math = json.dumps({k: e[k] for k in ("title", "statement", "assumptions")})
        assert "C:/" not in public_math and "C:\\\\" not in public_math
        assert "w364" not in public_math and "Yitzchak" not in public_math
    allowed = {"depends_on", "defines", "proves", "refutes", "generalizes", "specializes", "analogous_to", "cites", "semantic_association"}
    for rel in data["relations"]:
        assert rel["from_key"] in keys and rel["kind"] in allowed
        if "to_key" in rel:
            assert rel["to_key"] in keys
        else:
            assert rel["to_existing_logical"] == TARGET_LOGICAL
    assert {"id", "area", "event", "cue", "fire_when", "silent_when", "text", "evidence", "proposer"} == proposal.keys()
    assert len(proposal["text"]) <= 300
    measurements = json.loads((ROOT / "measurements/exact_boundary_counterexample.json").read_text(encoding="utf-8"))
    assert measurements["status"] == "passed"
    assert measurements["before_scalar_stitch"]["wrong_predictions"] == 2
    assert measurements["after_matched_boundary_composition"]["wrong_predictions"] == 0
    assert measurements["single_edge_forcing_checks"] == 64
    assert measurements["chosen_geodesic_membership_false_positives"] == 12
    return {"status": "passed", "draft_entries": len(data["entries"]), "relations": len(data["relations"]), "hook_text_characters": len(proposal["text"]), "independent_review": "pending", "live_ingestion": False, "command": "python -X utf8 prepare_drafts.py --validate-only"}


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--validate-only", action="store_true")
    args = parser.parse_args()
    if args.validate_only:
        data = json.loads((ROOT / "drafts/bundle_001.json").read_text(encoding="utf-8"))
        proposal = json.loads((ROOT / "drafts/math-w364.jsonl").read_text(encoding="utf-8"))
    else:
        data, proposal = bundle(), hook()
    receipt = validate(data, proposal)
    if not args.validate_only:
        for name in ("drafts", "patches", "review_packet", "measurements"):
            (ROOT / name).mkdir(exist_ok=True)
        bundle_text = json.dumps(data, indent=2, ensure_ascii=False) + "\n"
        hook_text = json.dumps(proposal, ensure_ascii=False) + "\n"
        (ROOT / "drafts/bundle_001.json").write_text(bundle_text, encoding="utf-8")
        (ROOT / "drafts/math-w364.jsonl").write_text(hook_text, encoding="utf-8")
        (ROOT / "patches/01_fpp_boundary_bundle.diff").write_text(new_file_diff(bundle_text, BRAIN_TARGET), encoding="utf-8")
        (ROOT / "patches/02_fpp_boundary_hook.diff").write_text(new_file_diff(hook_text, HOOK_TARGET), encoding="utf-8")
        quotes = {e["key"]: e["statement"] for e in data["entries"]}
        # Use the two grep-located cards only, stopping at the last required line.
        export = Path("~/math-brain-build/export/population/nodes.jsonl")
        existing = None
        with export.open(encoding="utf-8") as handle:
            for number, line in enumerate(itertools.islice(handle, 1823), 1):
                if number == 1823:
                    row = json.loads(line)
                    metadata = json.loads(row["metadata_json"])
                    assert metadata["logical_id"] == TARGET_LOGICAL
                    existing = {"node_id": row["id"], "logical_id": TARGET_LOGICAL, "statement": row["body"]}
        assert existing
        rows = []
        for i, rel in enumerate(data["relations"], 1):
            end = {"key": rel["to_key"], "statement": quotes[rel["to_key"]]} if "to_key" in rel else existing
            rows.append({"row": "S1.w364.edge" + str(i), "kind": rel["kind"], "from": {"key": rel["from_key"], "statement": quotes[rel["from_key"]]}, "to": end, "rationale": rel["rationale"], "status": "draft", "independent_reviewer": "w365", "reviewed": False})
        (ROOT / "review_packet/RELATIONS.jsonl").write_text("".join(json.dumps(r, ensure_ascii=False) + "\n" for r in rows), encoding="utf-8")
        controls = [
            {"id": proposal["id"], "case": "fire", "input": proposal["fire_when"], "expected": "fire", "author_verdict": "KEEP", "reason": "The two block minima require different vertices and underestimate passage time by one.", "review_state": "pending"},
            {"id": proposal["id"], "case": "silent", "input": proposal["silent_when"], "expected": "silent", "author_verdict": "KEEP", "reason": "Shared-endpoint composition or explicit centered-error control preserves the required matching constraint.", "review_state": "pending"},
        ]
        (ROOT / "review_packet/HOOK_CONTROLS.jsonl").write_text("".join(json.dumps(r) + "\n" for r in controls), encoding="utf-8")
    (ROOT / "measurements/draft_validation.json").write_text(json.dumps(receipt, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(receipt, indent=2))


if __name__ == "__main__":
    main()
