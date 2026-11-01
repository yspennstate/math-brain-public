# C0041 referee packet — 2026-10-10

Referee: w446. Scope: independent checks of w444's original L1–L3 and R1, w445's original negative control, and the new manuscript's source status. No parent-problem proof is certified.

## Exact target and source

Campos–Ramírez, *Ellipticity criteria for ballistic behavior of random walks in random environment*, Conjecture 1.1 (https://doi.org/10.1007/s00440-013-0527-7), asks whether one-direction transience implies ballisticity for iid uniformly elliptic nearest-neighbor RWRE on Z^d, d≥2. The owner intake's Drewitz–Ramírez Open Question 2.20 is the same question; its 2026-09-07 `attempted_unsolved` is only a dated search result. Guerra–Ramírez (https://arxiv.org/abs/1809.02011) settles equivalences among quantitative `(T)` conditions, not this unconditional transience implication.

A 2026-09-23 OpenAI manuscript (https://github.com/openai/math/blob/main/preprints/Directional-transience-implies-ballisticity-September-23-2026/paper.pdf) claims the full statement as Theorem 1.1. Local byte copy: `source_directional_ballisticity_20260923.pdf`, SHA256 `8B305D1FBB11B2A62D76F7DECBC45ACCF5D1C02362937D0AF5C4108DD0CC1411`. Its central assertion is estimate (5), section 2.4: for some epsilon in (0,1), the environment probability that a_N, the quenched probability of reaching level N before -1, is below N^(-epsilon) falls faster than every polynomial. Sections 3–8 claim to prove this. I have checked the statement and reduction, not those sections' complete chain. Current openness: UNKNOWN; claimed solution exists, proof not independently certified here.

The linked `lean/ComparatorChallenges/DirectionalBallisticity.lean` is a comparator. Its `MainStatement` at lines 80–84 matches the target, but theorem `directional_transience_implies_ballisticity` at lines 86–87 ends with `sorry`. This does not verify the manuscript. A formal receipt would need an actual theorem name, assumptions, dependency and trusted-axiom audit, and a successful build of a file with no admitted placeholder in the proof chain.

## w444 verdicts

**R1 — KEEP, conditional only.** If genuine iid regeneration cycles have integrable duration S and positive expected projected displacement Z·ell, their strong laws yield velocity EZ/ES. Reproduction: |Z|_1≤S gives integrability; tail-sum and Borel–Cantelli give S_k/k→0, so the unfinished cycle divided by n vanishes. This proves no cycle law or E S<∞ from C0041.

**L1 — KEEP.** For the box B(x,r), L=2r+1 consecutive +e1 steps exit from every site. Quenched conditional success at each L-step block is at least κ^L. Iterating the conditional bound gives P(T_B>mL)≤(1−κ^L)^m; tail summation gives E T_B≤Lκ^(−L). Stochastic domination by L times a geometric(κ^L) variable gives the displayed integer moments. No block independence was used.

**L2 — KEEP.** The two prescribed half-boxes have n_r=r(2r+1)^(d−1) disjoint sites each. Independence of environment rows gives probability (p_+p_−)^(n_r). Since the two signed-drift events at one site are disjoint, p_++p_−≤1 and p_+p_−≤1/4. The deterministic exit-moment bound times 4^(−n_r) is summable in r for d≥2. This concerns only the prescribed inward-drift pattern, not all traps.

**L3 — KEEP with its finite-horizon restriction.** Given the full fixed environment and F_H, the quenched Markov property bounds the remaining box-exit s-moment by the uniform L1 constant. The event that an adaptive center C satisfying |C|∞≤N has the L2 pattern lies in the union over at most (2N+1)^d deterministic centers. The union bound, with no independence assertion, gives M_r(s)min(1,(2N+1)^d4^(−n_r)). Division by P(D^ell=∞)>0 is valid for the additional conditioning. The bound deteriorates when N→∞, and H must be an actual stopping time; neither a regeneration cut nor the unrestricted elapsed regeneration duration is covered.

**Parent inference — DROP.** L1–L3 do not classify arbitrary slow regions or make the number and total cost of encountered regions integrable. Their result is a proved special-case exclusion, not C0041.

## w445 verdict

**Independent heavy-tail control — KEEP, as a counterexample to a generic inference.** With iid B_i~Bernoulli(q), iid L_i taking 2^k with probability 2^(−k−1), and N=min{i≥1:B_i=1}, N is geometric and finite almost surely. E L_i=Σ_k 1/2=∞. C=1+Σ_{i<N}L_i is finite a.s. but E C≥P(N>1)E L_1=∞, using independence. For L_i^(K)=min(L_i,2^K), E L_i^(K)=K/2+1 and E C^(K)=1+(1−q)(K/2+1)/q. This is not an RWRE counterexample. It refutes the proposed logic that a geometric attempt count plus finite individual attempts forces finite expected cost.

## Manuscript reduction: narrow FIX and remaining proof gate

Section 2.4, around local text lines 742–746, says that from x the probability of never revisiting x before exit is at least a_N(x+e1), by taking one upward step and then crossing. That route has probability **ω(x,e1) a_N(x+e1)≥κ a_N(x+e1)**. The displayed argument omits the first-step factor. The time-tail conclusion appears repairable by retaining κ in the geometric success parameter; this is a local proof correction, not a refutation of Theorem 1.1. The genuine audit gate remains estimate (5) and its Sections 3–8 derivation from one-direction transience alone.

## Route and next audit

The conditional reduction is: prove estimate (5) under exactly iid, UE, d≥2 and one-direction transience; then check Proposition 2.5's conversion to E of a genuine time-valued regeneration word <∞ and velocity. No `(T)`, `(P)_M`, neighborhood-of-directions assumption, or unstated product of conditional probabilities may enter. Next: inspect the load-bearing profile/entropy argument establishing estimate (5), especially where separate quenched two-walk comparisons become a joint tail bound. The new finite-region cost lemma and κ correction in `ATTEMPT.md` are authored by w446. **w449 independent audit requested before promotion**, particularly the visit-count stopping-time iteration and boundary-site crossing event.
