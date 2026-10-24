"""Prepare one labelled DRAFT bundle; publish only after a covering mesh claim."""
import argparse
from datetime import datetime, timezone
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent
TARGET = Path("~/math-brain-inbox/w438/bundle_001.json")
SOURCE = {
    "source_id": "owner-work:w438:P0043-sharp-tree-boundary:2026-10-10",
    "url": "file:///~/brain_workers/w438/ATTEMPT.md",
    "revision": "author-proof-2026-10-10-independent-review-pending",
    "license": "owner-own-work",
    "excerpt": None,
}
family = ("For a fixed real beta, let N=ceil(8(1+abs(beta))), "
          "B_n=floor(n/2+beta*log_2(1+n/N)), and let T_beta be the rooted tree "
          "with 2^(B_(n+1)-B_n) children at each vertex at depth n. ")


def entry(key, logical, title, statement, assumptions, kind="concept"):
    return {"key": key, "namespace": "probability.percolation",
            "logical_name": logical, "kind": kind, "title": title,
            "statement": statement, "proof_text": None,
            "assumptions": assumptions, "domain": "Bernoulli bond percolation on trees",
            "source": dict(SOURCE)}


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--publish", action="store_true")
    args = parser.parse_args()
    labelled = "AUTHOR PROOF DRAFT; INDEPENDENT MATHEMATICAL REVIEW PENDING. "
    entries = [
        entry("def-family", "polynomial-corrected-binary-unary-tree", "Polynomial-corrected binary/unary tree",
              family + "The root has depth zero; all edges are undirected. This defines the tree family used for the critical-survival boundary examples.",
              ["beta is real", "rooted deterministic tree", "n ranges over nonnegative integers"], "definition"),
        entry("reciprocal", "binary-unary-tree-reciprocal-survival-bound", "Reciprocal survival bound for binary/unary trees",
              labelled + "In an independent Bernoulli-p bond model on a spherically symmetric rooted tree with a_i in {1,2} children at depth i, let q_n be root connection probability to level n, m_0=1, m_j=p^j*product_(i<j)a_i, and S_n=sum_(i<n:a_i=2)1/m_i. For 0<p<=1 and finite n, 1/m_n+S_n/4 <= 1/q_n <= 1/m_n+S_n/[4(1-p/2)]. The proof telescopes the exact one- or two-child survival recursion using disjoint descendant edge sets. This is a special-case calculation, not a recursion for graphs with overlapping branches.",
              ["independent Bernoulli bonds", "deterministic a_i in {1,2}", "0<p<=1", "finite depth n"]),
        entry("threshold", "polynomial-tree-critical-survival-boundary", "Sharp polynomial boundary for critical tree survival",
              labelled + family + "T_beta has maximum degree at most 3 and p_c=1/sqrt(2). At criticality the root survival probability is positive exactly when beta>1. For beta<1, root connection probability to depth n is comparable to n^(beta-1); for beta=1 it is comparable to 1/log(n), for large n with beta-dependent constants. For beta>1, theta_o(p_c)>=(2-1/sqrt(2))/(1+N/(beta-1)); in particular theta_(T_2)(p_c)>=(2-1/sqrt(2))/25. When beta<=1 there is almost surely no infinite cluster anywhere. Each T_beta has a unique leaf, its root, and is not quasi-transitive. Thus this example does not refute critical extinction on quasi-transitive graphs.",
              ["tree family defined explicitly in this statement", "fixed real beta", "independent Bernoulli bonds"]),
        entry("local-limit", "critical-extinction-bounded-degree-local-limit-obstruction", "Critical extinction fails to pass to general local limits",
              labelled + "Let T be the rooted tree with B_n=floor(n/2+2*log_2(1+n/24)) and 2^(B_(n+1)-B_n) children at depth n. Let T^(K) use the same offspring counts for i<K and then alternate 1,2 children forever. All these connected trees have maximum degree 3 and p_c=1/sqrt(2). Each T^(K) has no infinite cluster at criticality, but T has positive critical root survival. The rooted balls of T^(K) converge to those of T. Equal critical parameters therefore do not allow critical extinction to pass to local limits of arbitrary bounded-degree rooted graphs. None of these examples is quasi-transitive.",
              ["independent Bernoulli bonds", "K is a nonnegative integer", "rooted local convergence", "no quasi-transitivity assumption"]),
        entry("quasi-isometry", "critical-extinction-equal-threshold-quasi-isometry-obstruction", "Equal-threshold quasi-isometry obstruction to critical extinction",
              labelled + family + "Contract unary corridors to the rooted binary branching skeleton. Each corridor and the initial stem have length at most 4; the resulting surjection pi obeys d_binary(pi(u),pi(v))<=d_T(u,v)<=4*d_binary(pi(u),pi(v))+8. Hence every T_beta is quasi-isometric to the rooted binary tree. T_0 and T_2 have equal critical probability 1/sqrt(2), yet only T_0 has critical extinction. Critical extinction is not a quasi-isometry invariant for arbitrary bounded-degree graphs, even with equal critical parameters. No claim is made about invariance within quasi-transitive graphs.",
              ["tree family defined explicitly in this statement", "ordinary multiplicative/additive quasi-isometry", "independent Bernoulli bonds"]),
        entry("gap", "critical-extinction-symmetry-exploration-gap", "Unproved symmetry-to-extinction exploration bridge",
              "UNPROVED ROUTE DIAGNOSIS; current openness UNKNOWN. The target is absence of all infinite critical Bernoulli bond clusters on every infinite connected locally finite quasi-transitive graph with p_c<1. A possible proof route would derive a sufficient finite-scale extinction or exploration-comparison criterion in subexponential growth. The missing step is preserving conditional exposure control when graph exploration branches overlap. A binary/unary tree survival recursion requires disjoint descendant randomness, and exponential level-growth rates alone cannot exclude polynomial corrections causing critical survival. No such comparison is proved in this packet; recent claims of the full target have not been independently audited here.",
              ["infinite connected locally finite quasi-transitive graph", "p_c<1", "independent Bernoulli bonds", "prospective route, not a theorem"]),
    ]
    relations = [
        {"from_key": "threshold", "to_key": "def-family", "kind": "depends_on", "rationale": "The threshold is stated for the explicitly defined T_beta family."},
        {"from_key": "threshold", "to_key": "reciprocal", "kind": "depends_on", "rationale": "The author proof applies the two-sided reciprocal bound at p=1/sqrt(2)."},
        {"from_key": "local-limit", "to_key": "threshold", "kind": "depends_on", "rationale": "The limit T_2 survives by the beta>1 criterion; periodic tails die by the same reciprocal bound."},
        {"from_key": "local-limit", "to_key": "reciprocal", "kind": "depends_on", "rationale": "At criticality periodic tail means are bounded and the branching reciprocal sum diverges."},
        {"from_key": "quasi-isometry", "to_key": "threshold", "kind": "depends_on", "rationale": "The two quasi-isometric examples are T_0 and T_2, with the contrasting critical survival established in the author tree proof."},
        {"from_key": "gap", "to_key": "threshold", "kind": "semantic_association", "rationale": "The bounded-degree tree example demonstrates why exponential growth rates alone are insufficient outside quasi-transitivity."},
    ]
    bundle = {"spec": "mathbrain-draft-v1", "author_agent": "w438", "bundle_slug": "p0043-sharp-tree-boundary-w438-001", "entries": entries, "relations": relations}
    keys = {x["key"] for x in entries}
    allowed_relations = {"depends_on", "defines", "proves", "refutes", "generalizes", "specializes", "analogous_to", "cites", "semantic_association"}
    for item in entries:
        assert item["kind"] in {"concept", "definition"} and item["proof_text"] is None
        assert item["source"]["license"] == "owner-own-work"
        assert item["statement"] and item["assumptions"]
    for relation in relations:
        assert relation["from_key"] in keys and relation["to_key"] in keys
        assert relation["kind"] in allowed_relations
    def visit(key, stack):
        assert key not in stack, "dependency cycle"
        for relation in relations:
            if relation["from_key"] == key and relation["kind"] == "depends_on":
                visit(relation["to_key"], stack | {key})
    for key in keys:
        visit(key, set())
    body = json.dumps(bundle, indent=2, ensure_ascii=False) + "\n"
    (ROOT / "bundle_001.json").write_text(body, encoding="utf-8")
    receipt = {"command": "python -X utf8 build_bundle.py" + (" --publish" if args.publish else ""),
               "entries": len(entries), "concepts": sum(x["kind"] == "concept" for x in entries),
               "definitions": sum(x["kind"] == "definition" for x in entries),
               "relations": len(relations), "schema_checks": "local shape/license/reference/acyclicity checks passed",
               "mathematical_validation": "author proof only; independent referee pending; finite experiments held by compute gate",
               "live_improvement": "NOT_MEASURED", "submitted": False, "reviewed": False, "ingested": False, "retrievable": False}
    if args.publish:
        if TARGET.exists():
            raise FileExistsError(f"Preserve existing draft: {TARGET}")
        TARGET.parent.mkdir(parents=True, exist_ok=True)
        part = TARGET.with_suffix(".json.part")
        if part.exists():
            raise FileExistsError(f"Preserve existing partial draft: {part}")
        part.write_text(body, encoding="utf-8")
        part.rename(TARGET)
        receipt["submitted"] = True
        receipt["submitted_path"] = str(TARGET)
        receipt["submitted_at_utc"] = datetime.now(timezone.utc).isoformat()
    (ROOT / "BRAIN_STATE.json").write_text(json.dumps(receipt, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(receipt, indent=2))


if __name__ == "__main__":
    main()
