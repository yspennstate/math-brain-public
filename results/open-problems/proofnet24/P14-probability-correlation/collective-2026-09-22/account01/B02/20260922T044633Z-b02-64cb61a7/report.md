# FOREST account01/B02 — exact Hermite fourth-moment remainder identity and fixed-graph source stress-test

**Run:** `20260922T044633Z-b02-64cb61a7`  
**Programme:** `COLLECTIVE-OPEN-PROBLEMS-20260921T234023Z`  
**Outcome:** **ESSENTIAL_STEP_APPLIED**  
**Inherited campaign state:** `FULL_PROOF_CANDIDATE` internally; not promoted here to an established/public theorem  
**Context:** `WITHOUT_VERIFIED_BRAIN`

## 1. Exact inherited candidate and named partner input

The latest complete campaign-lead report consumed is account01/B01 run `20260922T030948Z-b01-forest-auto11`, blob `58b8b1d8ac522a4eda7479400820e590c12f22aa`, candidate `FOREST-KN-COCKS-RECONCILED-v3`.

Its end-to-end chain is:

1. prove the unit unrooted-forest Rayleigh inequality on every complete graph `K_n`;
2. apply the fixed-graph implication attributed to Cocks in the final Semple--Welsh paper: unit Conjecture 1.1 on `G` implies that `M(G)` is independence correlated for every positive edge weighting;
3. delete the nonedges of an arbitrary finite simple graph from a complete graph, using the positive-weight deletion limit;
4. set all surviving edge weights equal to one.

The named OTHER-account result consumed and applied is account02/B03 run `20260922T022013Z-b03-forest-auto11`, `FOREST-PARALLEL-AGGREGATION / exact parallel aggregation and sharp book-graph separator adversary`. It proves that contraction-created parallel classes may be aggregated only by summing class weights and tracking a marked member through the corresponding derivative; replacing a parallel class by a unit edge can reverse a load-bearing Rayleigh cross-gap. The present candidate is compatible with that correction because its final transfer is deletion-only and never contracts a marked or unmarked edge.

The prior B02 run already supplied reversible marked-edge deletion/addition decompositions with multiplicity exactly one and component-quotient acyclicity for the complete-graph coefficients. This run does not repeat that argument. Instead it replaces the only inequality-style step in the Hermite sign proof by an exact positive signed remainder identity.

## 2. Complete-graph reduction recalled

Let

`R=z exp(R)`, `T=R-R^2/2`, `F=exp(T)`, `A=exp(R)`.

For a fixed edge and the two marked-edge orbits in `K_n`, the reversible marked-edge decompositions give

`Z_n=n![z^n]F`,

`E_n=(n-2)![z^(n-2)] F A^2`,

`J_adj,n=(n-3)![z^(n-3)] F A^3`,

`J_dis,n=(n-4)![z^(n-4)] F A^4(1+4/(1-R))`.

For the disjoint pair put

`k=n-4`, `x=n+1`, `a=He_k(x)`,

`s = k He_(k-1)(x)/He_k(x) = He'_k(x)/He_k(x)`.

Cauchy/Lagrange substitution gives

`J_dis=a(5-s)`, `J_adj=a(4-s)`,

`E=a(2n+6-3s)`,

`Z=a(n^2+3n+10-(n+4)s)`.

Thus

`Delta_dis/a^2 = G_n(s)`

where

`G_n(s)=(5-n)s^2+(n^2-4n-6)s-n^2+9n-14`,

and the adjacent orbit satisfies the exact identity

`Delta_adj = Delta_dis + Z a`.

Hence the disjoint orbit is the only sign problem.

## 3. New exact Hermite remainder identity

Assume `n>=6`. Let the roots of the probabilists' Hermite polynomial `He_k` be `lambda_i`. They are real and symmetric about zero. Since `x=n+1=k+5` lies to the right of every root,

`s = sum_i 1/(x-lambda_i)`.

Also

`sum_i lambda_i^2 = k(k-1)`.

Define

`L = k/x + k(k-1)/x^3`

`  = (n-4)(n-1)(n+4)/(n+1)^3`.

Pairing each positive root `lambda` with `-lambda` gives not merely a lower bound but the exact identity

`1/(x-lambda)+1/(x+lambda)-2/x-2 lambda^2/x^3`

`    = 2 lambda^4 / [x^3 (x^2-lambda^2)]`.

A zero root, when present, contributes zero to the remainder. Therefore

**(3.1)**

`s-L = sum_(lambda>0) 2 lambda^4 / [x^3 (x^2-lambda^2)] >= 0`.

All denominators are positive: the standard Hermite Jacobi matrix gives `|lambda|<2 sqrt(k)`, while `x=k+5>2 sqrt(k)`.

Now use the exact quadratic difference

`G_n(s)-G_n(L)=(s-L) Q_n(s,L)`

with

`Q_n(s,L)=n^2-4n-6-(n-5)(s+L)`.

The already established interval `s<1` and the evident `L<1` give, for `n>=6`,

`Q_n(s,L) > n^2-6n+4 > 0`.

Direct algebra gives

**(3.2)**

`G_n(L)=P(n)/(n+1)^6`,

where

`P(n)=2n^6+70n^5-33n^4+185n^3+1369n^2-3147n+1170`.

Writing `n=t+6`,

`P(t+6)=2t^6+142t^5+3147t^4+33233t^3+187651t^2+551661t+666396`,

so `P(n)>0` for every `n>=6`.

Combining (3.1) and (3.2) yields the exact positive signed decomposition

**(3.3)**

`Delta_dis/a^2`

` = P(n)/(n+1)^6`

`   + Q_n(s,L) * sum_(lambda>0) 2 lambda^4 / [(n+1)^3((n+1)^2-lambda^2)]`.

Every term on the right is nonnegative and the first is strictly positive. Consequently

`Delta_dis >= a^2 P(n)/(n+1)^6 > 0`

for every `n>=6`.

Then `Delta_adj=Delta_dis+Za>0`. The finite cases `n=3,4,5` are already handled exactly in the lead candidate and the preceding independent B02 audit.

This is stronger than the preceding monotonicity argument: it exposes the complete-graph Rayleigh difference as an explicit positive base polynomial plus a positive Hermite-root fourth-moment correction. No grid, asymptotic estimate, or unproved local swap enters the sign.

## 4. Why this is a switching/signed-identity contribution rather than a census

The combinatorial coefficients feeding (3.3) come from literal reversible deletion/addition of the marked edges. In the disjoint same-tree case, deleting the two marked edges gives three components whose component quotient is a path; its unique middle component contains exactly one endpoint of each marked edge, giving exactly four recoverable endpoint choices. The inverse adds the two marked edges to that path quotient, which is acyclic. Thus every coefficient in the Hermite reduction has proved multiplicity and acyclicity.

Equation (3.3) then supplies a signed identity for the exact Rayleigh difference after those reversible forest-pair decompositions. It does not assume an injective local exchange that has not been constructed.

## 5. Partner correction applied: deletion only, no unsafe parallel simplification

Account02/B03's exact aggregation theorem says a contraction-created parallel class `C` has quotient weight `Y_C=sum_(h in C)y_h`, and a marked original member is represented by differentiation with respect to `Y_C`. Its book-graph family proves that forgetting multiplicity and replacing `Y_C=2` by `1` can reverse the relevant cross-gap.

The candidate transfer from `K_n` to a simple graph `G` does not need contraction. Assuming the Cocks fixed-graph weighted upgrade for `K_n`, assign weight `epsilon>0` to every nonedge of `G` and the desired positive weights to the edges of `G`. The weighted Rayleigh difference is a polynomial in `epsilon`, nonnegative for every `epsilon>0`, and its `epsilon -> 0+` limit is exactly the weighted Rayleigh difference of `G`. Therefore no parallel class is created and the partner's obstruction is fully respected rather than bypassed by an invalid simplification.

## 6. Fixed-graph source stress-test

The final published Semple--Welsh paper, *Negative Correlation in Graphs and Matroids*, CPC 17 (2008), Proposition 3.5 and the Section 5 Note, explicitly records that Cocks proved: if Conjecture 1.1 holds for a graph `G`, then `M(G)` is independence correlated. That wording is exactly the fixed-graph implication required above.

I also checked the accessible 2008 Erickson thesis treatment. Its gadget argument proves the global class implication by attaching graphic two-sum gadgets that simulate a dense set of positive activities: if all resulting gadget-extended graphs are unit negatively correlated, then the original graphic matroid is weighted Rayleigh. This is a different and weaker route for present purposes; by itself it does not upgrade one fixed `G` from its unit point to all positive weights. Erickson says the result was obtained independently by Cocks, which is consistent with the chronology but does not reproduce the fixed-graph proof body.

Therefore no mathematical contradiction to the lead chain was found, but the primary Cocks proof body remains the one publication-stage source item I would insist on inspecting before an external announcement. The final Semple--Welsh attribution is strong evidence that the fixed-graph theorem is intended; the accessible global gadget proof must not silently substitute for it.

## 7. Conditional end-to-end conclusion and exact remaining obligation

Conditioned only on the fixed-graph Cocks theorem having the scope stated in the final Semple--Welsh Note, the proof candidate is end-to-end:

`complete-graph reversible marked-edge identity + (3.3)`

`=> unit pNC for every K_n`

`=> weighted independence correlation for every K_n`

`=> deletion limit to every finite simple G`

`=> unit unrooted-forest pNC for every finite simple G`.

There is no remaining displayed combinatorial or Hermite implication in this chain. The first remaining obligation is source validation: inspect the primary Cocks proof (or a journal-grade reproduction of the same fixed-graph theorem). If it proves exactly the statement recorded by Semple--Welsh, this run found no unpaid mathematical step; if it proves only a class-level equivalence, the all-graphs transfer must be reopened immediately.

## 8. Honest classification

**ESSENTIAL_STEP_APPLIED.** The inherited campaign remains an internal `FULL_PROOF_CANDIDATE`, and this run strengthens its hardest complete-graph sign step by an exact positive remainder identity. I do not promote the parent conjecture to an established or public theorem because the primary Cocks proof body was not directly inspected here.

No installation/benchmark work, email, Drive, public posting, paid/remote compute, permission change, scheduler mutation, production-data mutation, or sealed-answer access was performed. Brain status remained `WITHOUT_VERIFIED_BRAIN`.
