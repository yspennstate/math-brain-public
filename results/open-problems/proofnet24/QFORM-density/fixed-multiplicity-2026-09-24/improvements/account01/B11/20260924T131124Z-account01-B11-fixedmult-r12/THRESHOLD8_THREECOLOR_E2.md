# account01/B11 r12 — three-color extraction from the eight-direction two-sided collar

Run: `20260924T131124Z-account01-B11-fixedmult-r12`  
Objective: `QFORM-FIXED-MULTIPLICITY-AUDIT-20260924`  
Status: **NEW SUPPORTING CONSEQUENCE / EIGHT-DIRECTION DENSITY STILL OPEN**.

This note continues the same actual B11 invocation after the complete baseline audit and the complete nine-eigenvalue replacement proof. It does not alter either immutable artifact.

The input is the source-matched account03/B04 terminal-collar theorem in

`proofnet24/QFORM-density/fixed-multiplicity-2026-09-24/improvements/account03/B04/20260924T124904Z-account03-B04-fixedmult-audit-r2/REPORT.md`, blob `851e0ae9c78a4d9a49f60a1cc5f0026b734579e6`.

For a symmetric matrix `A`, define its ordered two-sided pair collar

`Xi_2(A)=sum_{S,H,T} det(A[S,H])^2 det(A[H,T])^2`,

where `S,H,T` are pairwise disjoint two-element sets and the triple is ordered. The cited terminal theorem proves that, in the no-pivot branch under `s_8(A)>=1`, either the third disjoint volume is already large and the completed `E_3` density receiver closes the branch, or

`Xi_2(A) >= (delta_*^2/2) kappa^2`,

with

`kappa=1/6400`,

`delta_*=(1-3sqrt(2)/80-1/100)^2-(sqrt((1/100)^2+1/100)+3sqrt(2)/80)^2`

`=0.8543351401911337...`.

The result below shows that this collar already forces a dimension-free *literal physical* second-crossing volume. Thus the remaining eight-direction obstruction is not absence of `E_2`; it is specifically the failure of order-two half-potential control by itself to imply an `L^infinity` density bound.

## Theorem — `QFORM-EIGHT-COLLAR-THREECOLOR-E2-v1`

For every real symmetric matrix `A`, there is an ordered partition of the original coordinate set into three (possibly empty) banks

`[n]=L disjoint_union M disjoint_union R`

such that, for the literal cross block

`B=A[M,L union R]`,

one has

`boxed: E_2(B) >= (2/27) sqrt(Xi_2(A)).`                         (1)

Here

`E_2(B)=e_2(BB^T)=sum_{|H|=2, |U|=2} det(B[H,U])^2`.

Consequently, in the unresolved terminal branch of the cited `s_8` theorem,

`boxed: E_2(B) >= (sqrt(2) delta_*/27) kappa
                 =6.99196957216563e-6... .}`                    (2)

Applying the already-proved marginal-free order-two product-Fourier receiver from this B11 run gives the full quadratic form the uniform half-potential estimate

`boxed: sup_a E|Q-a|^(-1/2)
        <= C_2 [(sqrt(2) delta_*/27)kappa]^(-1/8)
        <53.338,}`                                               (3)

where

`C_2=8 sqrt(e) 2^(-1/8)=12.095072570796...`.

Equation (3) retains arbitrary same-bank quadratic terms, arbitrary affine terms, all remaining spectrum and the original independent cap-one product law.

### Proof of (1)

Color each original coordinate independently with one of the three ordered colors `L,M,R`, each with probability `1/3`. For a fixed ordered pairwise-disjoint triple `(S,H,T)` of two-sets, the event

`S subset L, H subset M, T subset R`

has probability `3^(-6)`. Therefore some deterministic three-coloring satisfies

`Xi(L,M,R)
 :=sum_{H subset M, |H|=2}
      [sum_{S subset L, |S|=2} det A[S,H]^2]
      [sum_{T subset R, |T|=2} det A[H,T]^2]
 >=3^(-6) Xi_2(A).`                                             (4)

For a middle pair `H`, set

`L_H=sum_{S subset L, |S|=2} det A[S,H]^2`,

`R_H=sum_{T subset R, |T|=2} det A[H,T]^2`.

Then `Xi(L,M,R)=sum_H L_H R_H`.

Now form `B=A[M,L union R]`. Cauchy--Binet gives

`E_2(B)=sum_{H subset M, |H|=2}
             sum_{U subset L union R, |U|=2} det A[H,U]^2`.

The terms with `U subset L` equal `L_H` because `A` is symmetric, and the terms with `U subset R` equal `R_H`; mixed `L-R` column pairs are nonnegative extra terms. Hence

`E_2(B)>=sum_H(L_H+R_H)`

`       >=2 sum_H sqrt(L_H R_H)`

`       >=2 sqrt(sum_H L_H R_H)`

`       =2 sqrt(Xi(L,M,R))`

`       >=2*3^(-3) sqrt(Xi_2(A)).`

This is (1).

### Terminal numerical consequence

In the terminal eight-direction collar,

`sqrt(Xi_2(A)) >= delta_* kappa/sqrt(2)`.

Substitution in (1) gives

`E_2(B)>= (2/27)(delta_* kappa/sqrt(2))
         =(sqrt(2)delta_*/27)kappa`,

which is (2).

The order-two receiver proved in the main B11 improvement artifact says for every literal physical cross block `B` of the full quadratic form,

`sup_a E|Q-a|^(-1/2) <= C_2 E_2(B)^(-1/8)`.

Substituting (2) gives (3).

## What this does and does not close

This does **not** prove the eight-eigenvalue density theorem. Rank-two indefinite smoothing is genuinely borderline: an order-two crossing controls a half-potential but, without another product-preserving smoothing direction, does not imply a universal bounded density. The standard opposite-sign rank-two logarithmic example is the local warning.

The new reduction makes the missing implication sharper. In the only unresolved `s_8` branch, one now has simultaneously:

1. the account03/B04 overlap-one/two-sided collar (`Omega_1` and `Xi_2` bounded below), and
2. a literal physical cut with a dimension-free `E_2` packet and full half-potential `<53.338`.

Therefore an eight-direction proof must spend the *two-sided/overlap provenance* before collapsing everything to the scalar half-potential (3), or combine (3) with a new physical smoothing channel that remains uniform when all relevant scalar diagonals vanish. Merely improving constants in the existing `E_2` receiver cannot close the density endpoint.

No claim below multiplicity nine is made in this run. The unrestricted three-eigenvalue problem remains open.