"""Batch C006 of the Claude intake: C0158-C0160 from Haggstrom and Jonasson, 'Uniqueness and non-uniqueness in
percolation theory', Probability Surveys 3 (2006) (source haggstrom_jonasson_uniqueness_2006)."""
from intake_tools import append, now, HERE

P = HERE / "problems.jsonl"; A = HERE / "attempts.jsonl"; rows = []
H = "haggstrom_jonasson_uniqueness_2006"


def prob(pid, title, locator, statement, current, result, note="", dedup=None):
    rows.append(("p", {"schema": "probability-problem.v1", "problem_id": pid, "title": title, "source_id": H, "locator": locator,
                       "statement": statement, "historical_status": "source_says_open", "current_status": current, "result_status": result,
                       "admitted": True, "dedup_key": dedup or pid, "status_search": note, "verification": "unreviewed", "intake": "claude_20260907", "recorded_at": now()}))


def att(pid, method, result, key_identity="", check="", obstruction=""):
    rows.append(("a", {"schema": "probability-attempt.v1", "attempt_id": f"{pid}-A001", "problem_id": pid, "recorded_at": now(), "substantive": True,
                       "method": method, "result": result, "key_identity": key_identity, "independent_check": check, "obstruction": obstruction,
                       "author": "claude-probability-1000-continue-0907"}))


prob("C0158", "Number of infinite clusters at the uniqueness threshold p_u on nonamenable transitive graphs", "Section 3, p. 13 (PDF)",
     "Determine, for nonamenable transitive graphs with p_c < p_u < 1, whether the number of infinite clusters at p = p_u is 1 or infinity. Known: infinity on T_d x Z (Schonmann) and on products G x H with a nonamenable factor (Peres); 1 on planar nonamenable one-ended graphs (Benjamini-Schramm).",
     "unverified", "attempted_unsolved")
att("C0158", "Look for the invariant that separates the product case from the planar case.",
    "In the planar one-ended case uniqueness at p_u comes from duality: non-uniqueness at p would put infinitely many infinite dual clusters at 1 - p, and the planar argument shows the two cannot coexist at the threshold, forcing N(p_u) = 1. In the product case Peres's argument uses that G x H contains many disjoint copies of a nonamenable graph along which connectivity decays, and the key quantity is the connection probability tau_p(x,y) as |x - y| -> infinity: at p_u uniqueness holds iff inf tau_{p_u}(x,y) > 0 (Lyons-Schramm characterisation), and for products the decay of tau at p_u is inherited from the factor. A candidate general criterion: N(p_u) = 1 iff p -> inf_{x,y} tau_p(x,y) is continuous from the left at p_u, i.e. iff the uniqueness phase is 'closed'. This reformulation is exact by Lyons-Schramm (for unimodular transitive graphs) but only moves the question to left-continuity of the two-point infimum at p_u, which is again a critical-behaviour question with no general tool; the planar case has it by duality and the product case fails it by factor decay. Rigorous partial: on unimodular transitive graphs, N(p_u) = 1 iff liminf_{p decreasing to p_u} ... no: iff inf_{x,y} tau_{p_u}(x,y) > 0, by the Lyons-Schramm theorem applied at p_u itself; so the classification is the classification of graphs whose two-point infimum is positive at the uniqueness threshold.",
    key_identity="Unimodular transitive: N(p_u) = 1 <=> inf_{x,y} P_{p_u}(x <-> y) > 0 (Lyons-Schramm at p = p_u).",
    obstruction="Positivity of the two-point infimum exactly at p_u has no general criterion; known only via duality (planar) or factor decay (products).")
prob("C0159", "Cluster repulsion for nonunimodular transitive graphs", "Section 6, p. 20-21 (PDF)",
     "Does every transitive graph exhibit cluster repulsion, i.e. two distinct infinite clusters at level p almost surely do not come within bounded distance of each other along an infinite set of sites (Haggstrom-Peres-Schonmann conjecture)? Timar proved it for unimodular transitive graphs by mass transport; the nonunimodular case is open.",
     "unverified", "attempted_unsolved")
att("C0159", "Check whether the mass-transport step can be replaced on nonunimodular graphs by a tilted transport.",
    "Timar's argument transports mass from each site of cluster C_1 that is adjacent (in the graph) to a site of C_2 to the nearest such neighbour and uses the mass-transport principle to show the expected received mass is bounded, forcing finitely many 'touching' pairs per site on average, hence no strongly neighbouring pair of infinite clusters with positive density; unimodularity enters exactly in the equality of sent and received mass. On nonunimodular transitive graphs the tilted mass-transport principle (received mass weighted by the modular function) holds instead, and the touching set can have a nonunimodular structure: sites in the 'heavy' direction can receive unboundedly from many light sites. A counterexample would need two infinite clusters touching along a set of sites all in the same modular class; on the grandparent graph of T_d (the standard nonunimodular example) two infinite clusters could plausibly run 'parallel' along the height direction, touching at each level, since connectivity in the light direction is easy. I could not build the configuration with positive probability under i.i.d. percolation (independence resists the needed alignment), nor rule it out. Recorded: the nonunimodular case is a genuine question whose natural test bed is the grandparent graph.",
    obstruction="Tilted mass transport does not bound received mass; the grandparent graph is the test case in both directions.")
prob("C0160", "Continuity of the uniqueness threshold in the retention parameter: is N(p) monotone in p on transitive graphs?", "Section 3, p. 12 (PDF)",
     "For i.i.d. bond percolation on a transitive graph, show that the number of infinite clusters N(p) cannot switch back and forth between infinity and 1 as p increases: the set of p with uniqueness is an interval [p_u, 1] (proved for transitive graphs by Haggstrom-Peres and Schonmann; the survey records the general question for quasi-transitive and for non-unimodular graphs as settled only in the transitive case).",
     "unverified", "attempted_unsolved",
     note="The survey states uniqueness monotonicity for transitive graphs (Haggstrom-Peres 1999, Schonmann 1999); the admitted residual question is the quasi-transitive and general invariant-percolation setting. Bounded reading of the survey only.")
att("C0160", "Trace the transitive proof and mark where transitivity is used.",
    "Haggstrom-Peres prove uniqueness monotonicity for transitive graphs via the simultaneous uniqueness of the standard coupling: if the p_1-cluster is unique then each p_2-cluster, p_2 > p_1, contains a p_1... more precisely each infinite p_2-cluster contains an infinite p_1-cluster (the 'no new infinite clusters at higher p' statement), which uses transitivity through the two-point-infimum characterisation of uniqueness and its monotonicity in p. Quasi-transitivity (finitely many orbits) is enough for the two-point infimum argument with a finite set of base points, so the monotonicity transfers to quasi-transitive graphs with the same proof, which I believe is stated in Lyons-Peres. For general invariant percolation processes (not i.i.d.) monotone couplings need not exist (Mester's example on T_3 x Z, quoted in Pete's notes), and there uniqueness monotonicity can fail as a question about couplings; so the real open content in the survey's framing is for non-i.i.d. dependent percolation families with a monotone parameter, where the two-point argument still works whenever the family is monotone in p and satisfies the finite-energy and insertion-tolerance conditions used by Lyons-Schramm. Reduction: uniqueness monotonicity holds for any monotone insertion-tolerant invariant family on a quasi-transitive unimodular graph; the nonunimodular dependent case is the residual.",
    key_identity="Uniqueness at p iff inf_{x,y} tau_p(x,y) > 0, and the infimum is nondecreasing in p under a monotone coupling; hence the uniqueness set is an up-set.",
    obstruction="Nonunimodular dependent families: the Lyons-Schramm characterisation needs unimodularity.")

for kind, r in rows:
    append(P if kind == "p" else A, r)
print("written", sum(1 for k, _ in rows if k == "p"), "problems and", sum(1 for k, _ in rows if k == "a"), "attempts")
