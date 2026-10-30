# FOREST — alternate Jensen proof for the complete-graph sign

Candidate: `FOREST-KN-HERMITE-JENSEN-v1`  
Outcome: **ESSENTIAL_STEP_APPLIED / ALTERNATE_ALL-n PROOF OF THE HARDEST K_n SIGN**  
Parent status: **INTERNAL FULL-PROOF CANDIDATE EXISTS; external/source/publication scrutiny still required**  
Context: `WITHOUT_VERIFIED_BRAIN`

## 1. Exact scope and peer use

Target: for every finite simple graph `G`, uniformly over all acyclic edge subsets (including the empty forest, disconnected forests, and every forest size), prove pairwise negative correlation of distinct edges.

This run consumed the assigned OTHER-account partner result `fleet04/B01`, `FOREST-2CUT-MULTIBRIDGE-GLUING-v1`, shared handoff blob `312f5f1292906f995232fcae9d0281ba84146137`. Its exact two-terminal gluing identity is retained. The current team lead candidate is `fleet01/B01` `FOREST-KN-HERMITE-REDUCTION-v1`, blob `cad5f1b8546f44f200d441b71095a9fde4a20d4b`. Independent review blobs `b0a0f97426634919131e37b5a7bad4c4b7f8bb1e` and `ebc7fb763974ac1d5afea8e4f4c2fc2dc1e403bc` have already checked the end-to-end candidate.

The earlier objection that unit correlation for one fixed graph cannot imply weighted independence correlation has now been resolved at the source level: the published Semple–Welsh paper's Section 5 Note records Cocks's result that if Conjecture 1.1 holds for a graph `G`, then `M(G)` is independence correlated; Semple–Welsh Proposition 3.5 proves closure of independence-correlated matroids under minors. This run uses that fixed-graph statement, not the older class-level parallel-copy surrogate.

## 2. Lead complete-graph formulas

Let

`R = z exp(R)`, `T = R-R^2/2`, `F=exp(T)`, `A=T'=exp(R)`.

For a fixed edge of `K_n` and the adjacent/disjoint edge-pair orbits, the lead's labelled decomposition gives

`Z_n = n! [z^n] F`,

`E_n = (n-2)! [z^(n-2)] F A^2`,

`J_adj = (n-3)! [z^(n-3)] F A^3`,

`J_dis = (n-4)! [z^(n-4)] F A^4 (1+4/(1-R))`.

Write `H_j=He_j(n+1)` for the probabilists' Hermite polynomial and `D_j=H_j-j H_(j-1)`. Cauchy/Lagrange inversion yields

`Z_n=D_n`, `E_n=D_(n-2)`, `J_adj=D_(n-3)`, `J_dis=D_(n-4)+4H_(n-4)`.

For `k=n-4`, put `a=H_k` and

`s = k H_(k-1)/H_k`.

Then the harder disjoint Rayleigh gap is

`E_n^2 - Z_n J_dis = a^2 G_n(s)`

with

`G_n(s)=(5-n)s^2+(n^2-4n-6)s-n^2+9n-14`.

The lead proved positivity through a root-moment lower bound followed by a degree-six polynomial. The next section gives a shorter independent mechanism.

## 3. New Jensen bound

Let `lambda_1,...,lambda_k` be the real roots of `He_k`, and set `x=n+1=k+5`. Since `He'_k=k He_(k-1)`,

`s = H'_k(x)/H_k(x) = sum_i 1/(x-lambda_i)`.

Hermite root symmetry gives roots in `+/-` pairs (with a possible zero root), hence

`s = x sum_i 1/(x^2-lambda_i^2)`.

All roots satisfy `|lambda_i|<2 sqrt(k)<x`, so every denominator is positive. The coefficient of `x^(k-2)` in `He_k` and Newton's identities give the exact second moment

`sum_i lambda_i^2 = k(k-1)`.

For fixed `x`, the function `phi(u)=1/(x^2-u)` is strictly convex on `u<x^2`. Jensen therefore gives

`sum_i 1/(x^2-lambda_i^2) >= k / (x^2-(k-1))`,

and consequently

`s >= J_n := kx/(x^2-(k-1)) = (n-4)(n+1)/(n^2+n+6)`.

Also `0<s<1`: positivity is immediate from the root representation, while

`D_k=H_k-kH_(k-1)=H_k(1-s)>0`

because `D_k` is the positive labelled coefficient represented by the forest EGF and `H_k>0` for `x` above the largest root.

For `n>=6`,

`G'_n(s)=2(5-n)s+n^2-4n-6`.

Its minimum on `[0,1]` occurs at `s=1`, where

`G'_n(1)=n^2-6n+4>0`.

Thus `G_n` is increasing on `[0,1]`, so `G_n(s)>=G_n(J_n)`. Direct exact simplification gives

`G_n(J_n) = (3n^4+40n^3-59n^2+488n-280)/(n^2+n+6)^2`.

Writing `n=t+4`, the numerator becomes

`3t^4+88t^3+709t^2+2704t+4056`,

which is strictly positive for every `t>=0`. Hence the disjoint Rayleigh gap is strictly positive for every `n>=6`.

Since `J_dis=J_adj+H_k` and `Z_n,H_k>0`, the adjacent gap is even larger. The remaining complete-graph cases are exact: `K_3` adjacent gap `2`; `K_4` disjoint gap `6`; `K_5` disjoint gap `210`. `K_2` has no distinct edge pair.

Therefore every complete graph `K_n` satisfies the unit unrooted-forest pairwise negative-correlation inequality.

## 4. All-graphs implication

The source-checked fixed-graph theorem of Cocks upgrades unit Conjecture 1.1 for each `K_n` to positive-weight independence correlation of its graphic matroid `M(K_n)`. Semple–Welsh Proposition 3.5 gives minor closure. Every finite simple `n`-vertex graph is obtained from `K_n` by deleting edges, so its graphic matroid is a deletion minor of `M(K_n)`. Specializing the resulting positive weights to one gives exactly the source FOREST inequality, with disconnected forests and all forest sizes retained.

Thus the team's current chain is a full internal proof candidate. This run supplies an alternate proof of its hardest complete-graph sign and does not rely on the partner's separator reduction for global closure. The partner gluing theorem remains independently useful and consistent.

## 5. Exact regression

The accompanying standard-library checker independently:

- brute-enumerates all forests of `K_3,...,K_6` and matches the Hermite formulas exactly;
- verifies exact integer Rayleigh gaps through `n=30`;
- verifies `J_n<=s<1` and `G_n(J_n)>0` for every `6<=n<=500` using exact rational arithmetic;
- verifies the displayed rational identity for `G_n(J_n)` for every `6<=n<=500`.

Output begins:

`BRUTE_FORMULA_PASS n=3..6`  
`EXACT_GAPS_PASS n=4..30`  
`JENSEN_SIGN_PASS n=6..500`  
`RATIONAL_IDENTITY_PASS n=6..500`

The computation is regression only; the all-`n` proof is the argument above.

## 6. Status and next recipients

No source-valid counterexample was found or implied. The mathematical candidate now has two prior independent end-to-end review passes and this additional independent analytic route for the delicate complete-graph sign. This is not a public solved-problem, priority, or novelty claim. A bounded current-literature check still treats the general Grimmett–Winkler forest conjecture as open; external expert/source scrutiny is therefore the next scientific gate.

Next recipients: lead `fleet01/B01` and assigned partner `fleet04/B01`. They should integrate this Jensen proof as a shorter alternate `K_n` module and retain the existing EGF/source checks. No schedule or population state changes are requested.
