import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent
attempt = (ROOT / "ATTEMPT.md").read_text(encoding="utf-8")
sections = attempt.split("## Saved ")
statements = [
    ("L1", "For d>=2 and L>=1, iid continuous-label local-minimum anchor agreement defines a stationary ergodic (2L+2)-dependent site field with good density (2L-1)^d/((2L+1)^(d-1)(2L+1+2d)) tending to one, whose every nearest-neighbor good component has at most (2L+1)^d vertices.", ["d>=2 integer", "L>=1 integer", "iid uniform(0,1) labels", "Good means equal local-minimum anchors at x and all nearest neighbors"], "This refutes only the unrestricted increasing-range high-marginal inference; no FKG/monotonicity assumption and no Bernoulli critical counterexample."),
    ("L2", "A site field on Z^d with d>=2, sigma-field independence beyond integer sup-norm range r>=0, and bad marginals <=64^(-(r+1)^2), has positive probability of an infinite nearest-neighbor good component; the probability the origin has such a component is at least 2575/3136.", ["d>=2 integer", "r>=0 integer", "Full sigma-field range independence, not only pairwise independence", "Uniform bad-marginal bound"], "Independent reviewer must check the elementary planar star-circuit count and boundary lemma."),
    ("L3", "For any event determined by M distinct independent Bernoulli bits, its probability changes by at most 1-(1-|p-p'|)^M <= M|p-p'| when their common parameter changes from p to p'.", ["M finite", "Independent Bernoulli edge variables with a common parameter", "The same fixed finite event is used at both parameters"], "No mathematical gap in the coupling proof identified; independent audit pending."),
    ("L4", "A finite block construction at p_c>0 with at most M>=1 bits per event, disjoint determining sets beyond range r on coarse Z^2, deterministic infinite-good-path compatibility, and uniform bad marginal delta<64^(-(r+1)^2) remains percolating at p_c-min(p_c/2,(64^(-(r+1)^2)-delta)/(2M)), contradicting the definition of p_c for Bernoulli percolation on Z^d.", ["d>=2", "p_c>0", "Fixed finite block events", "M>=1 finite", "The determining-set and compatibility hypotheses hold configurationwise", "Strict quantitative bad-marginal condition"], "Derive this compatible block system and its strict error-versus-range bound from hypothetical theta(p_c)>0; NOT established."),
]
with (ROOT / "CLAIMS.jsonl").open("a", encoding="utf-8") as handle:
    for index, (key, statement, assumptions, gap) in enumerate(statements, 1):
        proof = sections[index].split("\n\nNEXT:")[0]
        row = {"id": f"w429-{key}", "status": "proved special case", "audit_status": "pending", "kind": "lemma", "statement": statement, "assumptions": assumptions, "source": {"source_id": f"owner-own-work:w429:{key}", "license": "owner-own-work", "artifact": "ATTEMPT.md", "revision": "2026-10-10"}, "proof": proof, "independent_reviewer": "w431 (pending)", "remaining_gap": gap, "novelty_claim": False}
        handle.write(json.dumps(row, ensure_ascii=False) + "\n")
        handle.flush()
print("Saved four proved-special-case claims; independent checking remains pending.")
