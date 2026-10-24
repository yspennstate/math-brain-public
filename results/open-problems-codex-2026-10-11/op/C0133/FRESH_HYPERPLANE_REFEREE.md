# Hostile review of the fresh-hyperplane argument

2026-10-12. This reviews the full handwritten argument in FRESH_HYPERPLANE_PROOF.md. Published inputs are treated as theorems, with their original assumptions checked against the retrieved texts. Finite computations and Lean checks do not formalize the infinite probability argument.

## Hypotheses and published inputs

Theorem 2.5 of Kosygina--Zerner, arXiv:1204.1895v2, p.7, assumes precisely (IID), (EL) and gives an unconditional finite/infinite range dichotomy. Lemma 3.18, p.14 with proof pp.14--16, assumes spatial IID, positive expected first-cookie probabilities and almost-sure infinite range. Strict ellipticity implies those expectations are positive. Theorem 3.16, p.14, assumes (IID), (EL) and gives a zero-one law for the UNION of the two directional escape events. No individual directional zero-one law is used.

Zerner's Lemma 3, printed p.193 of Electronic Communications in Probability 7 (2002), 191--197, is explicitly a lemma about a fixed nearest-neighbor path. Its quantity is the DIAMETER of the set of plane-visit times, rather than just the number of those visits. This distinction is critical: bounded diameter bounds the entire intervening history length. The exact limit order is sup_c inf_L limsup_M, as used in the proof. Its Markovian Theorem 1 is not being applied to the general excited walk.

## Attempts to break the proof

1. **Conditioning on recurrence might destroy IID.** The proof does not do that. It first splits the unconditional law using the range and directional zero-one laws. All fresh-field independence statements are under that original law, not a law conditioned on a returning path.

2. **A bounded coordinate need not force escape if the walk is trapped.** The finite-range case is removed first. In the infinite-range case Lemma 3.18, applied to -e with u=-a, w=b, gives precisely the needed conclusion. Taking integers a>=1, b>=0 supplies u<w including b=0. Countable intersection proves that any sample path bounded below is in A_e, outside one null set.

3. **Depleted stacks are not IID.** The slab lemma is never applied to a depleted field. Instead, each deterministic finite prefix is replayed in an ORIGINAL fresh environment. Its likelihood is strictly positive almost surely under (EL). A zero weighted probability therefore forces the continuation probability itself to vanish almost surely. This permits arbitrary dependence among the cookies in a stack and arbitrary cookie depths. A deterministic lower bound for the replay likelihood is unnecessary.

4. **The replay prefix might have gone left of its final plane.** That is allowed. Its full finite prefix still has a finite lower bound. The ensuing positive excursion uses only the right field, with exactly the finite departure counts deleted there. The left-field factors enter the positive replay likelihood but never change the marginal zero conclusion for the right field.

5. **Observing a prefix changes the right-field distribution.** True; the proof deliberately conditions BEFORE that prefix. Given that earlier information and a fixed right field, the joint prefix-and-continuation probability is W times f. Here W<=1, even with extensively depleted left stacks. Dropping W and integrating the originally fresh right field gives the required upper bound. There is no assertion that the posterior field after the prefix is fresh.

6. **A first hitting time might already have used frontier cookies.** For a signed unit coordinate, every departure before T_m is strictly below m. The arrival at T_m consumes no cookie there. The stopped path and uniforms are functions of the below-m field and the stopped driving sequence. Partitioning on T_m=t establishes conditional independence of the right field and unused uniforms. Fixing the countably valued arrival position allows a deterministic spatial translation.

7. **The front sigma-fields might not be nested.** At a later first front, the previously stopped uniforms/path can be reconstructed by stopping at the earlier first front. The revealed whole below-front field also increases. If either time is infinite, the earlier stopped data are still recoverable. On an infinite first-hit event the relevant future indicator is identically zero.

8. **An excursion event might not be measurable at the next front.** Its prescribed prefix has length at most c<L, so cannot reach that front. If the front is reached, the stopped data determine whether the prefix was followed and whether the continuation stayed strictly above the initial plane. If it is not reached, the event is false by definition. Thus the indicator is measurable at H_{m+L}.

9. **The events at successive planes overlap and are dependent.** Independence is not asserted. In each residue class modulo L the centered indicators are bounded martingale differences between H_m and H_{m+L}. Azuma and Borel--Cantelli give a frequency upper bound at fixed L. Combining finitely many residues preserves the bound.

10. **A long excursion might have an unbounded history before its last departure.** The deterministic lemma gives bounded DIAMETER of all visits to its starting plane before the upper front. Its last visit is therefore at most c steps after its FIRST visit. There are finitely many possible full nearest-neighbor histories of that length. Their entire shapes, not just endpoint/cookie count, are retained in the covering union. The history family depends on c but not on L.

11. **There could be a wrong exchange of limits.** First fix integer c,L and the finite history, then average over m. Establish these frequency bounds simultaneously for all countably many parameters. Next send L to infinity for that fixed finite history family. Every term tends to zero by monotone probability continuity. This gives inf_L limsup_M F=0 for each integer c; rounding c upward covers every real c. It contradicts the exact deterministic lemma without a uniform decay rate or summability in L.

12. **Empty-plane conventions could invalidate the covering.** The proof's indicator additionally requires both hitting times to be finite. On a positive limsup-speed path all positive levels are hit, so these indicators equal the published diameter indicators. Outside that event no equality is claimed.

13. **Zero-one laws in one direction might not settle the vector statement.** If any coordinate's two-sided escape union has probability one, spatial escape has probability one and the required complement is null. Otherwise all 2d signed escape probabilities are zero, and the one-sided limsup bounds for both signs squeeze every normalized coordinate to zero. This also proves the conclusion simultaneously for every real direction.

## Exact finite checks

fresh_history_experiments.py checked all 65,536 planar eight-step paths and 108,130 finite-prefix covering cases. It also checked that every departure before the first hit of a plane lies strictly to its left. These are finite checks of the local combinatorial construction; the general construction is proved in the handwritten argument.

A dependent-cookie rational example gives fresh continuation probability 1/64, prefix-and-continuation probability 15/8192 <= 1/64, but continuation conditional on the observed prefix 5/256 > 1/64. This verifies the pre-prefix inequality and explicitly refutes the tempting posterior-freshness assertion.

A zero-weight example gives weighted continuation probability 0 and unweighted probability 1/2. It confirms that strict positivity of the replay likelihood, supplied by (EL), is essential. The checks used exact Fraction arithmetic, negligible memory, and 0.934 seconds. Raw results are in fresh_history_experiments.json.

## Final review conclusion

All thirteen possible failures above have been checked against the written construction and published inputs. No remaining mathematical gap has been identified. The corrected finite likelihood formalization passed with exit code 0. The conclusion is an original proof assembled from published inputs, not a claim that a paper already states and proves Problem 4.7. The accepted verdict is SOLVED.

FreshHistoryChecks.lean proves discard_prefix_likelihood and positive_replay_detects_zero for a finite weighted space. The final runner used lake env lean from ~/lean_verify, with a 3600-second timeout and the source file inside C0133. The printed dependencies are the standard propext, Classical.choice and Quot.sound. There is no sorry, native_decide or blanket Mathlib import. Its first run failed at parsing ASCII membership notation; the notation was corrected, and only the successful corrected source is described as checked. Raw final output is fresh_history_lean.log and fresh_history_lean_result.json. The finite checks support two local algebraic steps; the infinite measure-theoretic argument remains the full handwritten proof above.

The deterministic input was separately reconstructed with simpler constants and reviewed in DETERMINISTIC_PLANE_LEMMA.md. In particular its sets count time instants, are nested in L, and strict diameter increases require strict cardinality increases. Its counting proof takes only finitely many L values before choosing a sufficiently large path subsequence index.
