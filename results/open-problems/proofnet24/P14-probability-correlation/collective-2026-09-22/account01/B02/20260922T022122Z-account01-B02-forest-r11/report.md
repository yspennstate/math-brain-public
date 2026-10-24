# FOREST / account01 B02 — independent switching audit of the complete-graph candidate

**Run:** `20260922T022122Z-account01-B02-forest-r11`  
**Directive:** `COLLECTIVE-OPEN-PROBLEMS-20260921T234023Z`  
**Assignment:** construct a forest-pair injection or signed switching identity for the lead's exact Rayleigh difference, with multiplicities and acyclicity proved.  
**Outcome:** **ESSENTIAL_STEP_APPLIED**  
**Parent target:** still **OPEN pending the collective review gate**.  
**Execution context:** `WITHOUT_VERIFIED_BRAIN`.

## 1. Exact candidate reviewed and cross-account result applied

I read the latest complete lead report, account01/B01 run `20260922T012234Z-account01-B01-forest-r11`, candidate `FOREST-KN-HERMITE-REDUCTION-v1`. Its proposed end-to-end chain is:

1. prove the unit uniform-all-forests Rayleigh inequality on every complete graph `K_n`;
2. use the published Cocks fixed-graph implication, as recorded in the final Semple--Welsh paper, to infer that `M(K_n)` is independence correlated for every positive weighting;
3. use Semple--Welsh Proposition 3.5, minor closure of independence-correlated matroids;
4. every finite simple `n`-vertex graph is obtained from `K_n` by edge deletions;
5. specialize the surviving weights to one.

I also consumed the named OTHER-account report account03/B03 `account03-b03-20260922T015800Z-forest-r11`, blob `e76cd27787722e1b80e6e5edb657f45ebe50ec49`. Its Section 4 proves a useful theta-gadget realization theorem for one positive virtual boundary-edge weight, and its Section 2 imports account02/B03's exact one-boundary-edge discriminant identity (report commit `a3561e0038110a04e5f932995ed4bb24ec9bec46`). I retain both algebraic identities. However, that account03/B03 report says the fixed-graph Cocks implication is not justified by the cited sources. I checked the exact final Semple--Welsh source and this particular source-scope objection is not sustained: their closing note explicitly states that Cocks showed that **if Conjecture 1.1 holds for a graph G, then M(G) is independence correlated**. Proposition 3.5 in the same paper explicitly states that independence-correlated matroids are closed under minors. Thus, at the level of the published statement cited by the lead, the fixed-graph step is exactly the implication needed for `K_n`.

I did not obtain the full primary Cocks proof itself in this runtime, so this is a source-statement validation, not a fresh proof of Cocks's theorem. That distinction remains in the review ledger.

## 2. Multiplicity-one marked-edge switchings on `K_n`

Let

`R(z)=sum_{m>=1} m^(m-1) z^m/m!`, so `R=z exp(R)`,

`T(z)=R-R^2/2`, `F(z)=exp(T(z))`, and `A(z)=T'(z)=exp(R)`.

`F` is the labelled-forest EGF, and `A` is the EGF of a tree carrying one prescribed distinguished vertex. The lead's four coefficient formulas can be proved by literal reversible edge-deletion switchings; this supplies the requested multiplicity and acyclicity proof rather than treating the species product as formal shorthand.

### 2.1 One marked edge

Fix `e={1,2}`. For every forest containing `e`, delete `e`. Since every edge of a forest is a bridge in its tree component, exactly two components result from that component, one containing vertex 1 and one containing vertex 2. The other forest components are untouched. Hence the image is uniquely an ordered pair of one-rooted trees plus an arbitrary forest on the remaining labels.

Conversely, from any such pair of disjoint rooted trees and remaining forest, add `12`. The added edge joins two distinct components, so it cannot create a cycle. Deletion recovers the input. Thus the map is a bijection with multiplicity one and

`E_n:=Z_e=(n-2)! [z^(n-2)] F A^2`.

### 2.2 Adjacent marked pair

Fix `e={1,2}`, `f={1,3}`. Delete both marked edges from a forest containing them. Their common tree component splits into exactly three components containing 1,2,3 respectively. Conversely add `12` and `13` to three distinct rooted components. The component-level graph is the two-edge tree `2-1-3`, so no cycle is introduced, and deletion is the inverse. Hence multiplicity is one and

`J_adj,n:=Z_ef=(n-3)! [z^(n-3)] F A^3`.

### 2.3 Disjoint marked pair: different original tree components

Fix `e={1,2}`, `f={3,4}`. If the two marked edges lie in different tree components, deleting them gives four distinct rooted components, carrying 1,2,3,4. Conversely adding `12` and `34` joins them in two disjoint component-level edges, hence is acyclic and uniquely reversible. Contribution:

`(n-4)! [z^(n-4)] F A^4`.

### 2.4 Disjoint marked pair: same original tree component

If the two marked edges lie in the same tree, deleting them gives exactly three components. Exactly one is the middle component in the component-level path determined by the two deleted edges, and it contains one endpoint of `e` and one endpoint of `f`. There are exactly four possible endpoint pairs for this middle component. Once that pair is specified, the two remaining endpoints lie in the two outer rooted components.

The middle component is a tree with two prescribed distinguished vertices and is counted by `T''(z)`. Since

`T''=A'=A^2/(1-R)`,

the contribution is

`4 (n-4)! [z^(n-4)] F A^2 T'' = 4 (n-4)! [z^(n-4)] F A^4/(1-R)`.

There is no hidden multiplicity: after deletion, the middle component and its two marked endpoints are determined by the forest itself. Conversely, adding the two marked edges makes the component-level graph a three-vertex path, so acyclicity is automatic and deletion is the inverse.

Therefore

`J_dis,n=(n-4)! [z^(n-4)] F A^4 (1+4/(1-R))`.

This is a genuine forest-pair switching certificate for every coefficient used by the lead.

## 3. Independent exact reduction of the Rayleigh difference

For `a>0`, put

`C_m(a)=m![z^m] exp(aR-R^2/2)`.

Lagrange inversion gives

`C_m(a)=He_m(m+a)-m He_(m-1)(m+a)`,

where `He_m` is the probabilists' Hermite polynomial. The Cauchy change of variable `z=u exp(-u)` also gives

`m![z^m] exp(aR-R^2/2)/(1-R)=He_m(m+a)`.

All four marked counts above are therefore evaluated at the common Hermite argument `x=n+1`. Set `k=n-4`, `H_j=He_j(n+1)`, and `D_j=H_j-jH_(j-1)`. Then

`Z_n=D_n`, `E_n=D_(n-2)`, `J_adj,n=D_(n-3)`,

`J_dis,n=D_k+4H_k=5H_k-kH_(k-1)`.

The Hermite recurrence gives

`J_adj,n=4H_k-kH_(k-1)`,

hence the exact signed identity

`J_dis,n-J_adj,n=H_k>0`,

and consequently

`Delta_adj,n = Delta_dis,n + Z_n H_k`.

Thus the disjoint orbit is the unique harder complete-graph orbit.

For `n>=4`, write `a=H_k` and

`s=kH_(k-1)/H_k=H_k'(n+1)/H_k(n+1)`.

Direct recurrence reduction gives

`J_dis=a(5-s)`,
`J_adj=a(4-s)`,
`E=a(2n+6-3s)`,
`Z=a(n^2+3n+10-(n+4)s)`.

Therefore

`Delta_dis/a^2 = G_n(s)`

with

`G_n(s)=(5-n)s^2+(n^2-4n-6)s-n^2+9n-14`.

I independently recomputed this symbolic identity exactly.

## 4. Positivity check without numerical approximation

For `n>=6`, `k=n-4>=2` and `x=n+1=k+5`. The roots `lambda_i` of `He_k` are real and symmetric. Via the standard symmetric Jacobi matrix, `|lambda_i|<2sqrt(k)<x`, hence `H_k(x)>0` and

`s=sum_i 1/(x-lambda_i)`.

Pairing `+/-lambda` gives

`1/(x-lambda)+1/(x+lambda)=2x/(x^2-lambda^2) >= 2/x+2lambda^2/x^3`.

Using `sum_i lambda_i^2=k(k-1)` yields

`s >= k/x+k(k-1)/x^3 =: L_n`

where

`L_n=(n-4)(n-1)(n+4)/(n+1)^3`.

Also `D_k=H_k-kH_(k-1)>0`, because it is the positive coefficient `k![z^k]FA^4`; since `H_k>0`, this gives `s<1`. Thus `s in [L_n,1)`.

For `n>=6`,

`G_n'(s)=2(5-n)s+n^2-4n-6 >= G_n'(1)=n^2-6n+4>0`,

so `G_n` is increasing throughout `[0,1]`. Hence

`G_n(s)>=G_n(L_n)=P(n)/(n+1)^6`,

where exact simplification gives

`P(n)=2n^6+70n^5-33n^4+185n^3+1369n^2-3147n+1170`.

Putting `n=t+6` gives

`P(t+6)=2t^6+142t^5+3147t^4+33233t^3+187651t^2+551661t+666396`,

whose coefficients are all strictly positive for `t>=0`. Therefore `Delta_dis>0` for every `n>=6`, and the signed identity above gives `Delta_adj>Delta_dis>0`.

The small exact cases are:

- `K_3`: `(Z,E,J_adj,Delta_adj)=(7,3,1,2)`;
- `K_4`: `(Z,E,J_adj,J_dis)=(38,14,4,5)`, gaps `(44,6)`;
- `K_5`: `(291,93,23,29)`, gaps `(1956,210)`;
- independent brute enumeration also gives `K_6`: `(Z,E,J_adj,J_dis)=(2932,822,178,226)`, gaps `(153788,13052)`.

So the complete-graph part of `FOREST-KN-HERMITE-REDUCTION-v1` survives this independent switching/algebra audit.

## 5. Application of account02/B03 and account03/B03 boundary-weight work

The account02/B03 one-boundary-edge discriminant writes, when only a virtual boundary edge has weight `w`,

`Q(w)=D_0+Mw+D_1w^2`.

The account03/B03 theta-gadget theorem then proves that if `Q(w_0)<0` for one positive `w_0`, a simple unit-weight graph counterexample can be built by replacing the virtual edge with internally disjoint equal-length paths whose exact terminal responses `k/(2^ell-1)` approximate `w_0`.

The present result changes how that work should be used. The explicit Semple--Welsh closing note supports the fixed-graph Cocks implication needed by the lead, so the weighted boundary gate is not an unpaid obstruction *if* the cited Cocks theorem is admitted. The theta realization remains independently useful as a constructive unit-weight compilation of a bad one-edge weight and as an adversarial check on future separator arguments.

## 6. Conditional end-to-end argument and remaining review obligation

The candidate now has the following compact chain:

- multiplicity-one marked-edge switchings above give the exact complete-graph coefficient formulas;
- the Hermite calculation proves `Delta_Kn(e,f)>0` for every distinct pair in every `K_n`;
- the final Semple--Welsh paper explicitly records Cocks's theorem: unit Conjecture 1.1 for a fixed graph `G` implies `M(G)` is independence correlated;
- Semple--Welsh Proposition 3.5 gives minor closure;
- every finite simple `G` is an edge-deletion subgraph of a sufficiently large complete graph;
- specialize the surviving positive weights to one.

I find no mathematical defect in this chain from the material actually checked in this run. However, under the campaign protocol I do **not** promote the parent conjecture to solved: a full candidate requires two independent existing-worker end-to-end reviews, and the primary Cocks proof itself was not retrieved here. The exact first remaining review task is therefore not another separator construction; it is an independent source-and-proof audit of Cocks's fixed-graph implication together with a second end-to-end check of the Hermite coefficient argument.

**Status:** `ESSENTIAL_STEP_APPLIED`, not automatic target closure.  
**Candidate survived this review:** yes.  
**Source disagreement resolved at published-statement level:** yes; the Semple--Welsh final note explicitly states the fixed-graph implication.  
**Primary Cocks proof independently checked here:** no.  
**Brain assistance:** none; `WITHOUT_VERIFIED_BRAIN`.

## 7. Sources checked

- C. Semple and D. Welsh, *Negative Correlation in Graphs and Matroids*, Combin. Probab. Comput. 17 (2008), 423--435. Proposition 3.5 gives minor closure; the final note reports Cocks's fixed-graph implication.
- C. C. Cocks, *Correlated Matroids*, Combin. Probab. Comput. 17 (2008), 511--518, DOI 10.1017/S0963548308009152. Abstract and bibliographic record checked; full primary proof not available in this runtime.
- G. Grimmett and S. Winkler, *Negative association in uniform forests and connected graphs*, Random Structures & Algorithms 24 (2004), 444--460, source target.
- D. Stark, *The Edge Correlation of Random Forests*, Ann. Comb. 15 (2011), 529--539, prior complete-graph sufficiently-large result; the present exact argument is stronger on that special family if correct.
