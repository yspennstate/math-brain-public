# FOREST B03 — aggregate conditioning/reconnection budget after paying the contraction debt

Outcome: **ESSENTIAL_STEP_APPLIED**. Parent FOREST target remains **OPEN**. Context: **WITHOUT_VERIFIED_BRAIN**.

Run: `20260922T025058Z-b03-forest-r11`  
Account/slot: `account01/B03`  
Owner campaign: `COLLECTIVE-OPEN-PROBLEMS-20260921T234023Z`  
Role: conditioning/reconnection estimate for overlapping cycles, with disconnected forests and boundary cases retained.

## Inputs actually consumed

Lead version: account01/B01 `FOREST-KN-HERMITE-REDUCTION-v1`, shared handoff blob `cad5f1b8546f44f200d441b71095a9fde4a20d4b`. Its end-to-end route is `K_n` Hermite theorem -> fixed-graph weighted upgrade -> minor/deletion closure. This report stays on the assigned local conditioning route and does not re-prove the Hermite calculation.

Named OTHER-account result applied: **account02/B01**, run `B01-20260922T021602Z-forest-r12`, report blob `59fb19252eaa411eb1d321035e40721a15c6477f`. That report proves the previously unpaid contraction-side implication in a lexicographically minimal simple counterexample: after conditioning on a third edge `g` and contracting it, parallel classes have multiplicity at most two; simplifying gives a strictly smaller simple graph with activities in `{1,2}`. Using its source-checked fixed-graph upgrade on that smaller graph gives the conditional marked gap `D_1(g)>=0`. It also gives `D_0(g)>=0` by deletion/minimality and the signs `Cov(X,T_g),Cov(Y,T_g)<0`.

The theorem below is algebraically independent of how `D_0,D_1>=0` are discharged: those endpoint signs can be treated as hypotheses. Thus any later source-scope correction to the partner theorem would change only the application, not the new estimate itself.

## 1. Exact overlap setup

Let `G` be a hypothetical lexicographically minimal simple counterexample, with marked distinct edges `e,f`, and put `G0=G-{e,f}`. Let `H` be uniform over **all** forests of `G0`; no connectedness or size conditioning is imposed. Define

- `X=1{H+e is a forest}`;
- `Y=1{H+f is a forest}`;
- `S=1{H+e+f is a forest}`;
- `Q=XY-S`.

Thus `Q=1` precisely when `e,f` are individually addable but their simultaneous addition creates a cycle. This definition handles disjoint or adjacent marked edges uniformly. Write

`x=E X`, `y=E Y`, `r=E S`, `q=E Q`,

`D=xy-r`, and, for a violation, `delta=-D>0`.

Since `S=XY-Q`,

`D=q-Cov(X,Y)`, hence

`Cov(X,Y)=q+delta`.                                                     (1)

For each third edge `g in E(G0)`, let `T_g=1{g in H}`, `p_g=E T_g`, `v_g=Var(T_g)`. Empty and singleton forests show `0<p_g<1`, so `v_g>0`, even when `G0` is disconnected.

Let `D_0(g),D_1(g)` be the same normalized gap `xy-r` under the conditional laws `T_g=0,1`. Exact two-component mixture algebra gives

`D=(1-p_g)D_0(g)+p_gD_1(g)-Cov(X,T_g)Cov(Y,T_g)/v_g`.                 (2)

Under minimality plus the account02/B01 contraction result,

`D_0(g)>=0`, `D_1(g)>=0`,

and deletion in `G-f` and `G-e` gives

`a_g:=-Cov(X,T_g)>=0`, `b_g:=-Cov(Y,T_g)>=0`.                         (3)

Define the nonnegative endpoint surplus

`h_g=(1-p_g)D_0(g)+p_gD_1(g)`, `Hsum=sum_g h_g`.

Then (2) is the exact per-edge identity

`a_g b_g/v_g = delta+h_g`.                                           (4)

If `k=|E(G0)|`, summing gives

`M:=sum_g a_g b_g/v_g = k delta + Hsum`.                              (5)

This is the point at which the paid contraction endpoint enters the overlap calculation.

## 2. One-sided Bessel lemma for negatively correlated edge coordinates

Because `G0` is a proper deletion of the minimal counterexample, all its edge pairs have nonpositive covariance:

`Cov(T_g,T_h)<=0` for `g!=h`.                                         (6)

Lemma. Let `A` be any square-integrable variable for which `c_g=-Cov(A,T_g)>=0`. Then

`sum_g c_g^2/v_g <= Var(A)`.                                          (7)

Proof. Put `w_g=c_g/v_g` and `L=sum_g w_g(T_g-p_g)`. By (6) and `w_g>=0`,

`Var(L)<=sum_g w_g^2 v_g = R`, where `R=sum_g c_g^2/v_g`.

Also `Cov(A,L)=-R`. Cauchy-Schwarz yields `R^2<=Var(A)Var(L)<=Var(A)R`; if `R>0`, divide by `R`, and if `R=0` the claim is trivial. QED.

Applying (7) to `X`, `Y`, and to `X+alpha Y` for every `alpha>0`, set

`R_X=sum a_g^2/v_g`, `R_Y=sum b_g^2/v_g`, `V_X=Var(X)`, `V_Y=Var(Y)`, `C=Cov(X,Y)`.

Then

`R_X+2 alpha M+alpha^2 R_Y <= V_X+2 alpha C+alpha^2 V_Y`.              (8)

In particular `R_X<=V_X`, `R_Y<=V_Y`. Put `U=V_X-R_X>=0`, `V=V_Y-R_Y>=0`. Optimizing (8) over positive `alpha` gives

`M-C <= sqrt(UV)`.                                                     (9)

The elementary identity

`(sqrt(V_X V_Y)-sqrt(R_X R_Y))^2-(V_X-R_X)(V_Y-R_Y)
 = (sqrt(V_X R_Y)-sqrt(V_Y R_X))^2 >=0`

gives `sqrt(UV)<=sqrt(V_XV_Y)-sqrt(R_XR_Y)`, while Cauchy gives `M<=sqrt(R_XR_Y)`. Therefore

`2M <= C+sqrt(V_X V_Y)`.                                              (10)

This is the new aggregate reconnection estimate.

## 3. Exact NC-plus-overlap budget

Insert (1) and (5) into (10):

**`(2k-1) delta + 2 Hsum <= q + sqrt(Var(X)Var(Y)).`**                 (11)

Consequences:

`k delta + Hsum <= sqrt(Var(X)Var(Y)) <= 1/4`,                        (12)

and, discarding the nonnegative surplus,

`(2k-1)delta <= q+sqrt(Var(X)Var(Y))`.                                (13)

Unlike the earlier per-edge inequality, (11) simultaneously charges every third-edge Simpson term against one global covariance budget. It is valid with disconnected base forests and with adjacent marked edges. No sectorwise connectivity-Rayleigh assertion is used.

In raw four-state counts, let `N` be the number of forests of `G0`, let `n_ij=#\{X=i,Y=j\}`, and let `Qcount=#\{Q=1\}`. Then

`delta=(n_00 n_11-n_10 n_01-N Qcount)/N^2`.

Thus any minimal counterexample must have a **positive integer count deficit** but still satisfy the severe aggregate budget (11). The remaining local closure problem is no longer the contraction sign; it is to extract enough graphic reconnection surplus from `Hsum` and/or the overlap-cycle reservoir `q` to force `delta<=0`.

## 4. A natural universal overlap-charge is false

The tempting next statement `Hsum>=q` would turn (11) into a substantially sharper charge. It is false even for an ordinary finite simple graph under the exact source law.

Take vertices `{0,1,2,3,4,5}` and

`E(G)={03,04,12,13,15,23,25,34,35,45}`,

with marked edges `e=03`, `f=12`. For the uniform law on all forests of `G0=G-{e,f}` exact enumeration gives

`N=162`, `x=19/27`, `y=47/81`, `r=11/27`,

`q=1/81`, `Cov(X,Y)=25/2187`, `delta=Cov(X,Y)-q=-2/2187`.

All eight endpoint conditional gaps are nonnegative and both covariance sign families in (3) are nonpositive, but

`Hsum=211/17496 < 216/17496 = q`.

So a proof cannot simply charge each overlap state once into the sum of conditional minor gaps. This is a genuine source-valid graph counterexample to that **auxiliary universal charge**, not to FOREST itself (indeed `delta<0` here).

## 5. Exact regression

A native exact-rational enumeration independently checked, over every simple graph on at most five vertices and every marked edge pair (11,766 marked instances total), the identities `D=q-Cov(X,Y)`, (2), the one-sided Bessel inequalities for `X` and `Y`, and inequality (10) whenever the required covariance signs hold. There were zero failures. A separate exact enumeration produced the six-vertex witness in Section 4. These computations are regression only; (7)--(11) are proved algebraically above.

## 6. Conditional end-to-end route and first remaining implication

For this assigned mechanism the corrected chain is now:

1. minimal simple counterexample -> deletion endpoint `D_0(g)>=0` and edge-edge NC in `G0`;
2. account02/B01 contraction simplification + fixed-graph weighted upgrade on the smaller graph -> `D_1(g)>=0`;
3. exact mixture identity -> `a_g b_g/v_g=delta+h_g`;
4. one-sided Bessel aggregation -> the global overlap budget (11);
5. **first still-unpaid local implication:** prove a graphic-specific lower bound on the total endpoint surplus / overlap-cycle switching contribution strong enough, together with (11), to exclude `delta>0` in the remaining 3-connected core.

The naive universal candidate `Hsum>=q` is refuted above, so the next switching bound must use the violation hypothesis and/or the geometry of the unique cycle created on `Q`, rather than only unconditional overlap counting.

Honest run status: **ESSENTIAL_STEP_APPLIED**. The parent theorem is not promoted by this report.

No benchmark gold, credentials, scheduler identifiers, machine paths, unrelated private data, email, Drive, public posting, paid API/model call, remote workflow, permission change, or brain installation appears here.
