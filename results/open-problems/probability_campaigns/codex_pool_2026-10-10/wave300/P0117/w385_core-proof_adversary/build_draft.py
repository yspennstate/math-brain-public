"""Build a local review draft; do not ingest or change live recall controls."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent

def entry(key, name, kind, title, statement, assumptions):
    return {"key": key, "namespace": "probability.first-passage-percolation",
            "logical_name": name, "kind": kind, "title": title,
            "statement": statement, "proof_text": None, "assumptions": assumptions,
            "domain": "probability theory",
            "source": {"source_id": "owner-own-work:w385:P0117:" + key,
                       "url": (ROOT / ("ATTEMPT.md" if key in {"box-filtration", "box-substitution", "ladder-control"} else "INDEPENDENT.md")).as_uri(), "revision": "w385-2026-10-10-draft-v1",
                       "license": "owner-own-work (campaign draft; new reductions await independent referee)",
                       "excerpt": None}}

a1 = ["Nearest-neighbor undirected Z^2", "Iid finite nonnegative atomless edge weights",
      "E[min(t1,t2,t3,t4)^2]<infinity for four independent samples"]
pending = "DRAFT: independent verification pending. "
entries = [
    entry("bigeodesic", "injective-bigeodesic-weighted-graph-definition", "definition",
          "Injective bigeodesic in a weighted graph",
          "For a graph with finite nonnegative edge weights, let T(x,y) be the infimum of the total weights of finite walks from x to y. An injective bigeodesic is a sequence (v_i) indexed by all integers, with distinct vertices and adjacent consecutive vertices, such that the weight of the segment from v_i to v_j equals T(v_i,v_j) for every i<j.",
          ["Graph with finite nonnegative edge weights"]),
    entry("shell-reduction", "draft-bigeodesic-finite-shell-witness-reduction", "concept",
          "Draft reduction of bigeodesics to finite shell witnesses",
          pending + "On nearest-neighbor Z^2 with finite nonnegative edge weights, define S_n={x:||x||_infinity=n}. Let E_n be the existence of a simple geodesic in the full lattice, containing 0, between distinct vertices of S_n. The E_n are decreasing and their intersection is exactly the existence of an injective bigeodesic through 0. Under a translation-invariant law, absence of bigeodesics everywhere is equivalent to P(E_n)->0. This compactness reduction provides no probability decay.",
          ["Finite nonnegative edge weights on Z^2", "Simple geodesics minimize the full-lattice passage metric", "Translation invariance only for the everywhere assertion"]),
    entry("selector", "draft-adaptive-selector-probability-obstruction", "concept",
          "Draft obstruction to applying deterministic bounds to selected endpoints",
          pending + "Let U be uniform on [0,1), J_n=floor(2^n U), and A_(n,k)={J_n=k}, 0<=k<2^n. Every fixed indexed event has probability 2^(-n), while the union over k and the selected event A_(n,J_n) both have probability 1. The selectors are measurable and their partitions refine coherently. Thus a uniform bound for each deterministic endpoint or label cannot be substituted into an environment-selected endpoint or label without a justified conditional estimate or a bound on the union. This is an inference counterexample, not a FPP bigeodesic construction.",
          ["Uniform U on [0,1)", "Environment-selected index J_n"]),
    entry("max-pair", "draft-fpp-shell-midpoint-maximum-crossing-lower-bound", "concept",
          "Draft crossing lower bound blocks the maximum-pair union route",
          pending + "Under iid finite nonnegative atomless weights on nearest-neighbor Z^2 with E[min(t1,t2,t3,t4)^2]<infinity, define S_n={x:||x||_infinity=n} and q_n=max_{distinct u,v in S_n} P(0 lies on the unique full-lattice geodesic from u to v). There is an integer C>=2 such that (2n+1)q_n+2 sum_{r=n+1}^{Cn}q_r>=1-o(1). Consequently q_n is not o(1/n). The raw shell union bound min(1,binomial(8n,2)q_n) stays equal to 1 along an unbounded sequence. Seeking an o(n^-2) maximum-pair rate cannot rescue that argument. This gives no lower bound on the union event and no existence of bigeodesics.", a1),
    entry("box-filtration", "draft-bigeodesic-adapted-box-witness-reduction", "concept",
          "Draft adapted reduction using box minimizers",
          pending + "On nearest-neighbor Z^2 with finite nonnegative weights, let B_n={x:||x||_infinity<=n} and S_n its boundary. Let G_n be the existence of a simple path through 0 between distinct S_n vertices that minimizes passage time among walks restricted to B_n. G_n is measurable from edges inside B_n, is decreasing, and its intersection equals the injective bigeodesic-through-0 event. In the compactness proof every fixed competing finite path eventually lies inside each sufficiently large witnessing box. A conditional annulus survival estimate would still be a separate unproved input; raw independence of annular weights does not supply it.",
          ["Finite nonnegative weights on Z^2", "Box-restricted passage metric"]),
    entry("box-substitution", "draft-iid-fpp-box-versus-global-geodesic-counterexample", "concept",
          "Draft iid control against substituting box geodesics for global geodesics",
          pending + "For endpoints (-1,0),(1,0), require the two horizontal origin edges to have weights in [0.95,1.05], the ten other edges inside B_1=[-1,1]^2 to have weights in [9,10], and each of the ten exterior edges along (-1,0),(-2,0),(-2,1),(-2,2),(-1,2),(0,2),(1,2),(2,2),(2,1),(2,0),(1,0) to have weights in [0.05,0.1]. Under iid Uniform[0.05,10], this 22-edge cylinder has positive probability. The unique box geodesic passes through 0 with cost at most 2.1, whereas every full-lattice simple path through 0 costs at least 1.9 and an exterior competitor costs at most 1. Therefore no full-lattice geodesic for these endpoints passes through 0. The control refutes a metric substitution, not the no-bigeodesics conjecture.",
          ["Iid Uniform[0.05,10] on nearest-neighbor Z^2", "The specified finite cylinder; all other weights unrestricted"]),
    entry("direction-limit", "draft-potential-bigeodesic-arm-direction-limits", "concept",
          "Draft direction limits for potential bigeodesic arms",
          pending + "Under iid finite nonnegative atomless weights on nearest-neighbor Z^2 with E[min(t1,t2,t3,t4)^2]<infinity, Ahlberg-Hoffman's fixed differentiability-direction exclusion implies that, on one probability-one event, both arms of every potential injective bigeodesic have direction limits. Intersect exclusions over a deterministic countable dense set of differentiability directions. Each ray escapes finite balls, so angular step sizes vanish and its direction cluster set is compact, nonempty, and connected. A nonsingleton connected cluster set would contain an arc hitting that dense set. Singleton directions may still be environment-selected; neither their simultaneous exclusion nor their antipodality follows here.", a1 + ["Ahlberg-Hoffman Theorem 2.2(b)"]),
    entry("ladder-control", "draft-atomless-iid-ladder-bigeodesic-control", "concept",
          "Draft ladder control isolates the full-plane support-collapse input",
          pending + "On the nearest-neighbor ladder Z x {0,1} with iid Uniform[1,2] edge weights, almost surely a bigeodesic uses one of the two edges across the cut between columns 0 and 1. Every geodesic from (-n,0) to (n,0) crosses that finite cut; an infinite subsequence shares one cut edge, and anchored diagonal compactness yields a bigeodesic. By row symmetry each cut edge has bigeodesic probability at least 1/2. Deleting either cut edge leaves the graph connected. Its conditional deleted-edge capacity therefore exceeds the weight support infimum a=1 with positive probability. This is a control outside Z^2, showing that planarity, atomless iid weights, and properness alone cannot establish support collapse; it does not refute P0117.",
          ["Ladder graph Z x {0,1}, not the full Z^2 target", "Iid Uniform[1,2] weights", "Deleted-edge conditional capacity formula"]),
]
relations = [
    {"from_key":"shell-reduction","to_key":"bigeodesic","kind":"depends_on","rationale":"The shell compactness statement uses injective bigeodesics and finite-segment minimization."},
    {"from_key":"max-pair","to_key":"shell-reduction","kind":"semantic_association","rationale":"The crossing lower bound identifies why a raw maximum-pair union estimate cannot close the shell-witness probability decay."},
    {"from_key":"selector","to_key":"shell-reduction","kind":"semantic_association","rationale":"Shell witnesses may select endpoints from the environment; the selector example explains why fixed-pair bounds do not control their union."},
    {"from_key":"box-filtration","to_key":"bigeodesic","kind":"depends_on","rationale":"The adapted box-witness intersection is identified with the injective bigeodesic event by global finite-segment minimization."},
    {"from_key":"box-substitution","to_key":"box-filtration","kind":"semantic_association","rationale":"The local adapted reduction uses a restricted metric; the explicit iid cylinder prevents silently importing a full-lattice midpoint estimate for its minimizers."},
    {"from_key":"direction-limit","to_key":"bigeodesic","kind":"depends_on","rationale":"The direction-limit reduction concerns both escaping arms of injective bigeodesics."},
    {"from_key":"ladder-control","to_key":"bigeodesic","kind":"depends_on","rationale":"The graph-general definition makes the ladder control precise while keeping its graph scope separate from Z^2."},
    {"from_key":"max-pair","to_existing_logical":"math:probability.core:open-problem-p0117-absence-of-bi-infinite-geodesics-in-planar-iid-fpp","kind":"semantic_association","rationale":"The proposed crossing lower bound prunes a fixed-pair union argument for the existing P0117 all-bigeodesics question, in the explicit moment-restricted subcase; it does not resolve or retire the broad question."},
]
bundle = {"spec":"mathbrain-draft-v1","author_agent":"w385","bundle_slug":"p0117-adaptive-geodesic-obstructions-w385-001","entries":entries,"relations":relations}
(ROOT / "bundle_001.json").write_text(json.dumps(bundle, indent=2, ensure_ascii=False)+"\n",encoding="utf-8")
by_key={e["key"]:e for e in entries}
rows=[]
for i,r in enumerate(relations,1):
    if "to_key" in r:
        target_statement=by_key[r["to_key"]]["statement"]
        target_evidence="local bundle entry"
    else:
        snapshots=json.loads((ROOT/"STORE_SOURCE_CHECK.json").read_text(encoding="utf-8"))
        target=next(x for x in snapshots if json.loads(x["metadata_json"])["logical_id"]==r["to_existing_logical"])
        target_statement=target["statement_excerpt"]
        target_evidence="read-only STORE_SOURCE_CHECK.json; exact full target body checked in PACKET_VALIDATION.json"
    rows.append({"relation_id":f"w385-R{i}",**r,"from_statement_quote":by_key[r["from_key"]]["statement"],"to_statement_quote":target_statement,"target_evidence":target_evidence,"evidence":"INDEPENDENT.md; ATTEMPT.md","independent_reviewer":"w386 (pending)","status":"DRAFT"})
(ROOT / "RELATION_EVIDENCE.jsonl").write_text("".join(json.dumps(r,ensure_ascii=False)+"\n" for r in rows),encoding="utf-8")
assert len(entries)==8 and len(relations)==8
print(json.dumps({"bundle":"bundle_001.json","entries":len(entries),"relations":len(relations),"theorem_entries":0,"new_reductions_reviewed":False}))
