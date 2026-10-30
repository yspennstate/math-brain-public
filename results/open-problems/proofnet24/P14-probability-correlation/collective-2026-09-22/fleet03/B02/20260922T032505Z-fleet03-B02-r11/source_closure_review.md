# FOREST / fleet03 B02 — source-closure review of the complete-graph reduction

**Run:** `20260922T032505Z-fleet03-B02-r11`  
**Outcome:** `FULL_PROOF_CANDIDATE` under the collective internal gate; **not** an external solved-problem, novelty, or priority claim.  
**Context:** `WITHOUT_VERIFIED_BRAIN`.

## Assignment and peer consumed

The live fleet03/B02 assignment is to attack a genuinely unresolved universal obstruction for the uniform-all-forests pairwise negative-correlation problem, with partner `fleet04/B03`.

Named OTHER-account result consumed and applied: fleet04/B03 handoff `fleet04-B03-20260922T030927Z-full-candidate-integration.md`, blob `27dfbf71a18abf0c89d52c8aaaf11d6c037d2d19`. That partner integrated the lead complete-graph/Hermite candidate, the two independent existing-worker reviews, and the multigraph positive-weight lift. Its earliest remaining diligence item was direct source scrutiny of the Cocks fixed-graph upgrade.

Because that later compatible full candidate removes the previously unpaid three-connected obstruction, this run did not manufacture a duplicate minimal-counterexample lemma. It attacked the first remaining universal dependency: whether the all-graphs transfer really has the exact fixed-graph weighted theorem and minor-closure hypotheses it needs.

## Direct source verification

I independently retrieved the final author-hosted Semple--Welsh paper:

Charles Semple and Dominic Welsh, *Negative Correlation in Graphs and Matroids*, Combinatorics, Probability and Computing 17 (2008), 423--435, DOI `10.1017/S0963548307008978`, author PDF `https://www.math.canterbury.ac.nz/~c.semple/papers/SW07.pdf`.

The exact source facts needed by the candidate are present in the final paper:

1. Its definition of **independence correlated** quantifies the independent-set Rayleigh inequality over **all positive real edge weightings**, not merely unit weights.
2. Proposition 3.5 states and proves that independence-correlated matroids are closed under minors, using the limits `epsilon -> 0+` for deletion and `epsilon -> infinity` for contraction.
3. Section 5 question (3) asks whether a graph can satisfy Conjecture 1.1 while `M(G)` is not independence correlated. The post-submission Note then explicitly records Cocks's stronger fixed-graph result: if Conjecture 1.1 holds for a graph `G`, then `M(G)` is independence correlated.

This is exactly the pointwise implication required by the lead reduction; it is not the older class-level parallel-copy converse that earlier workers correctly rejected as insufficient.

I also independently checked the published Cocks bibliographic record:

Clifford C. Cocks, *Correlated Matroids*, Combinatorics, Probability and Computing 17(4) (2008), 511--518, DOI `10.1017/S0963548308009152`. Cambridge's abstract says the paper proves equivalences between the Grimmett--Winkler/Pemantle graph conjectures and correlated graphic-matroid statements and answers the Semple--Welsh open questions. The full article body was not openly retrievable in this run, so I do not claim a line-by-line audit of Cocks's proof itself.

## Source-closed logical transfer

The candidate transfer is now independently source-checked end to end.

For a finite simple graph `G` on `n` vertices:

1. The internally reviewed labelled-forest/Hermite argument proves the unit Conjecture 1.1 inequality on `K_n` for every distinct edge pair.
2. The fixed-graph Cocks theorem recorded in the final Semple--Welsh Note upgrades that unit statement on this same `K_n` to independence correlation of `M(K_n)` for every positive edge weighting.
3. Semple--Welsh Proposition 3.5 passes independence correlation to every deletion minor.
4. `G` is obtained from `K_n` by deleting exactly its nonedges; isolated vertices do not change the graphic matroid or any edge-subset forest count.
5. Setting every surviving weight to one gives exactly the uniform law on **all** acyclic edge subsets of `G`, including the empty forest, disconnected forests, and every forest size.

Therefore there is no missing universal implication in the all-graphs transfer, conditional only on correctness of the internally reviewed `K_n` Hermite theorem.

## Targeted re-audit of the complete-graph theorem

I rechecked the fragile algebra rather than inheriting the prior PASS blindly. With `k=n-4`, `x=n+1`, `H_j=He_j(x)`, and `s=k H_(k-1)/H_k`, the exact counts reduce to

`J_dis = H_k(5-s)`, `J_adj = H_k(4-s)`,

so the disjoint orbit is indeed harder by exactly `Z_n H_k>0` for `n>=4`.

The disjoint gap is `H_k^2 G_n(s)` with

`G_n(s)=(5-n)s^2+(n^2-4n-6)s-n^2+9n-14`.

Hermite root symmetry plus `sum lambda_i^2=k(k-1)` yields

`s >= L_n=(n-4)(n-1)(n+4)/(n+1)^3`,

and positivity of `H_k-kH_(k-1)=k![z^k]F A^4` gives `0<=s<1`. For `n>=6`, `G_n` is increasing on `[0,1]` because `G_n'(1)=n^2-6n+4>0`. Exact algebra gives

`(n+1)^6 G_n(L_n)=2n^6+70n^5-33n^4+185n^3+1369n^2-3147n+1170`.

After substituting `n=t+6`, this is

`2t^6+142t^5+3147t^4+33233t^3+187651t^2+551661t+666396`,

with every coefficient positive. The prior exact small cases `K_3,K_4,K_5` therefore complete the all-`n` argument. This re-audit found no new mathematical gap.

## Classification and next recipient

**Classification: `FULL_PROOF_CANDIDATE`.** The candidate has all source quantifiers and the collective two-independent-review gate already recorded by the lead and partner. This run independently closes the specific source-attribution uncertainty that remained in the partner handoff.

This still is not permission to announce the Grimmett--Winkler conjecture as established. The remaining work is ordinary publication-grade scrutiny: ideally obtain the full published Cocks article and line-check its proof, then subject the Hermite derivation and source transfer to external expert review. If the original Cocks paper contradicts the final Semple--Welsh fixed-graph attribution, demote immediately and restore the weighted-complete bridge as unpaid.

Recipient: FOREST lead `fleet01/B01` and assigned partner `fleet04/B03`. Under the owner rule against duplicating a source-matching completed scope, the lead should propose a comparably substantial successor only after owner approval; fleet03/B02 should not silently switch targets.

No scheduler mutation, email/Drive/public posting, remote workflow, paid model/API/Codex call, cross-account native change, credential access, private-transcript publication, or brain activation occurred.
