# FOREST B03 — continued-fraction strengthening of the complete-graph reduction

Run: `20260922T031602Z-b03-forest-r12`  
Outcome: **ESSENTIAL_STEP_APPLIED**.  
Context: **WITHOUT_VERIFIED_BRAIN**.  
Parent target: not publicly promoted; the team currently has an internal `FULL_PROOF_CANDIDATE` with two independent end-to-end review passes, but external priority/novelty remains unverified.

## 1. Controls and exact scope

Fresh start controls were read at main `e661d70e7469376d8e47acc24428bdecfbc13979`; pre-publication refresh was main `4c0d86cc5585faaa81e99166dbec429086e67391`. Active OWNER CONTROL is `2026-09-22.2`, directive `COLLECTIVE-OPEN-PROBLEMS-20260921T234023Z`. This slot is FOREST research: for every finite simple graph, uniform over all unrooted acyclic edge subsets, prove pairwise negative edge correlation. New brain-installation and benchmark work remained stopped.

Mandatory source/control blobs at the fresh read included README `3d4a9372c87802ab734141a3374d04c8823372e3`, ORDER `a70e03208ae00795ca7c6cdf9b7dbce854347138`, TARGETS `a8cafa98cdb074ed15d0e214f8f54ee514c500df`, ASSIGNMENTS `fe144a4be3522d57f8cb2dc40b1fc57df7c7f7da`. The assigned role is exact graph adversaries to separator/counting lemmas, especially overlaps and contraction-created parallel intermediates, then corrected sufficient statements.

## 2. Exact peer/version use

Latest complete campaign lead consumed: account01/B01 `FOREST-KN-HERMITE-REDUCTION-v1`, shared handoff blob `cad5f1b8546f44f200d441b71095a9fde4a20d4b`.

Named OTHER-account partner consumed and directly applied: account03/B01 second independent review, blob `ebc7fb763974ac1d5afea8e4f4c2fc2dc1e403bc`. That review independently accepted the lead's EGF/Hermite count formulas, the fixed-graph Cocks bridge, the minor-closure step, and singled out the Hermite lower bound as a load-bearing point. This run replaces that spectral/root-moment lower bound by a stronger elementary continued-fraction bound.

Local prior adversary retained: account02/B03 sharp book/parallel obstruction, blob `b0da7d6c5dcc5496d9b100a6315555f0531ed384`. It proves that contraction-created parallel classes must retain summed weights and marked-member derivative semantics and that the all-response separator envelope is sharp. Nothing below invalidates that result; the complete-graph/minor route simply bypasses the separator bottleneck.

Also consumed account01/B03 aggregate-overlap-budget handoff blob `224b6c313cff2cedc570c6133861a2d3a4a55549`, which gives a genuine source-law counterexample to the tempting unconditional closure `Hsum >= q`. That failure reinforces that the separator route should not be silently substituted for the lead's current complete-graph route.

## 3. Conditional end-to-end chain

The lead's compact source-valid chain is:

1. prove unit-weight pairwise forest negative correlation on every complete graph `K_n`;
2. use Cocks's fixed-graph theorem: if Conjecture 1.1 holds for a graph `G`, then its graphic matroid `M(G)` is independence correlated for all positive weights;
3. use Semple--Welsh Proposition 3.5: independence-correlated matroids are closed under minors;
4. every finite simple `n`-vertex graph is obtained from `K_n` by edge deletion, and isolated vertices do not alter the edge-subset forest law;
5. specialize the inherited positive weights back to unit weights.

The final published Semple--Welsh paper explicitly records the fixed-graph Cocks implication in its Section 5 Note and proves minor closure in Proposition 3.5. Thus the only mathematical content needed inside this run is a reliable all-`n` proof for `K_n`.

## 4. Exact labelled-forest formulas

Let `R = z exp(R)`, `T = R - R^2/2`, `F = exp(T)`, and `A = T' = exp(R)`. For a fixed edge and the two edge-pair orbits of `K_n`, labelled decomposition gives

`Z_n = n! [z^n] F`,

`E_n = (n-2)! [z^(n-2)] F A^2`,

`J_adj = (n-3)! [z^(n-3)] F A^3`,

`J_dis = (n-4)! [z^(n-4)] F A^4 (1 + 4/(1-R))`.

For the disjoint same-tree term, deleting the two marked edges leaves three components; there are four choices of which endpoint pair lies in the middle doubly distinguished tree, whose EGF is `T''=A^2/(1-R)`.

Under the formal Cauchy substitution `z = u exp(-u)`, if `He_j` are probabilists' Hermite polynomials and `x=n+1`, define

`H_j = He_j(x)`, `D_j = H_j - j H_(j-1)`.

Then

`Z_n=D_n`, `E_n=D_(n-2)`, `J_adj=D_(n-3)`,

and, with `k=n-4`,

`J_dis=D_k+4H_k=5H_k-kH_(k-1)=J_adj+H_k`.

Once `H_k>0`, the disjoint orbit is strictly harder than the adjacent orbit.

## 5. New elementary continued-fraction lemma

Fix `k>=1`, put `x=k+5`, and for `1<=j<=k` define

`r_j = j H_(j-1)/H_j`, with `r_0=0`.

The Hermite recurrence

`H_j = x H_(j-1) - (j-1) H_(j-2)`

gives the exact continued fraction

`r_j = j / (x-r_(j-1))`.

Inductively, `H_j>0` and `0<r_j<1` for every `1<=j<=k`: if `0<=r_(j-1)<1`, then `x-r_(j-1)>k+4>j`, so the next denominator is positive and `r_j<1`.

Now let

`s = r_k = k H_(k-1)/H_k`.

Since `r_(k-1) >= (k-1)/x`,

`s = k/(x-r_(k-1)) >= k/(x-(k-1)/x)`

and therefore

**`s >= C_k := k(k+5)/(k^2+9k+26)`.**

For `k=1` there is equality. For `k>=2` the bound is strictly stronger than the lead's root-second-moment bound

`L_k = k((k+5)^2+k-1)/(k+5)^3`,

because

`C_k-L_k = k(k-1)^2 / ((k+5)^3 (k^2+9k+26)) >= 0`.

Thus no Hermite root location, Jacobi eigenvalue bound, root symmetry, or root second moment is needed for this step.

## 6. Positive disjoint Rayleigh gap from the new bound

Normalize by `H_k`. The Hermite recurrence gives

`D_(k+1)/H_k = 4-s`,

`D_(k+2)/H_k = 2k-3s+14`,

`D_(k+4)/H_k = k^2-ks+11k-8s+38`,

and `J_dis/H_k=5-s`.

Hence

`E_n^2-Z_n J_dis = H_k^2 G_k(s)`

with

`G_k(s) = (1-k)s^2 + (k^2+4k-6)s - k^2+k+6`.

For `k>=2`, `G_k` is increasing on `[0,1]`, since

`G_k'(s) >= G_k'(1) = k^2+2k-4 > 0`.

Using `s>=C_k`, exact substitution yields

**`G_k(C_k) = (3k^4+88k^3+709k^2+2704k+4056)/(k^2+9k+26)^2 > 0`.**

Thus the disjoint gap is positive for every `n>=6`. For `n=5` (`k=1`), `s=C_1=1/6` and the exact gap is `210`. For `K_4` the disjoint gap is `6`; for `K_3` the only pair orbit is adjacent and the gap is `2`. Since `J_dis=J_adj+H_k` with `H_k>0`, positivity of the disjoint gap implies positivity of the adjacent gap whenever both orbits exist.

This proves the complete-graph unit inequality for every `n` using a strictly simpler lower-bound mechanism than the lead version.

## 7. Exact computation used as regression, not proof

`continued_fraction_checker.py` is a standard-library exact-integer/Fraction checker. It independently brute-enumerates every edge subset of `K_3,K_4,K_5,K_6`, verifies the labelled formulas exactly, then checks the continued-fraction bound, the normalized-gap identity, the closed-form `G_k(C_k)`, and positive gaps for every `4<=n<=500`.

Executed source SHA-256: `b9be24723bd513310d9a624fdea9e69d1d9ff3a9f859957877c4ff9076fc1382` (2861 bytes).

Executed output SHA-256: `6c7e6d85e6d1922aa0fa1d081954b1936019c8f0661e5861d6509c49971a3e1c` (447 bytes).

Output ends `STATUS=PASS n=4..500, brute K3..K6`. This finite computation is only regression evidence; the all-`n` proof is the recurrence argument above.

## 8. What was refuted / preserved

No new source-graph counterexample to FOREST was found. The prior book family remains an exact counterexample to unit-simple contraction and to any strict slack below one in the all-response separator envelope. Account01/B03's six-vertex witness remains an exact counterexample to unconditional `Hsum>=q`. Those failed separator strengthenings are preserved, not overwritten.

The new complete-graph recurrence proof means those separator obligations are no longer on the shortest conditional end-to-end path. They remain useful if the Cocks/minor route is ever invalidated by source review, but should not be charged as current proof gaps.

## 9. Status and next recipient

Run label: **ESSENTIAL_STEP_APPLIED**. The essential applied step is the continued-fraction bound `s>=C_k`, which is stronger and more elementary than the Hermite-root lower bound used by the current lead and both prior reviewers.

The team already records two independent end-to-end review passes (account03/B02 and named partner account03/B01). This run provides an additional independent derivation of the complete-graph hard orbit and a direct check of the final Semple--Welsh source bridge, but it does not make a public solved-problem or novelty claim. Next recipient: account01/B01 campaign lead, for integration of the simpler bound and ordinary expert/source scrutiny.

Privacy/provenance review: PASS. No credentials, scheduler identifiers, machine paths, raw private transcripts, benchmark gold, unrelated private data, or unsafe serialized objects are present.
