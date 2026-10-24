SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account03, slot B09, 2026-09-23T16:46:04Z.
attacking: close the localized physical-hub-pair survivor by converting its anchored third volume into either a diffuse projected crossing or a literal three-hub cross block, before any reciprocal pair-core determinant.

# Early substantive checkpoint — projected-crossing closure of the localized pair

Full QFORM remains OPEN. This checkpoint proves a supporting closure theorem for the localized two-hub branch and applies two current completed sources at equations. It keeps all random variables in original coordinates and retains arbitrary same-bank quadratic curvature.

## Setup

Let `a,b` be two original coordinates and let `S,T` be disjoint original-coordinate leaf banks. Condition on every coordinate outside `{a,b} union S union T`. Put

`B=A[{a,b},T]`, assume `rank B=2`, and set

`Delta=det(B B^T)>0`.

Let `Pi` be the orthogonal projection in `R^T` onto `row(B)` and define the projected leaf crossing

`C=A[S,T](I-Pi)`, `Z=||C||_F^2`.

Define the pair-anchored physical third volume

`V=sum_{k in S} sum_{J subset T, |J|=3} det A[{a,b,k},J]^2`.

For row `d_k=A[k,T]`, Cauchy--Binet and the Gram determinant identity give

`sum_{|J|=3} det([B;d_k][:,J])^2 = det([B;d_k][B;d_k]^T)=Delta ||d_k(I-Pi)||_2^2`.

Hence the exact identity

`boxed: V=Delta Z.`

## Theorem — QFORM-TWOHUB-PROJECTED-CROSSING-CLOSURE-v1

If `V>0`, then for every admissible cap-one product input law the full quadratic form has a continuous density and

`boxed: ||p_Q||_infinity <= 3*2^(5/6) V^(-1/6) < 5.346 V^(-1/6).`

The identical coefficient gives `P{Q in L} <= 3*2^(5/6)V^(-1/6)|L|` for every interval `L`.

### Case 1: diffuse projected crossing

If every row `c_k` of `C` satisfies `||c_k||^2<=Z/2`, apply the completed grouped projected-crossing theorem `GC` from `proofnet24/QFORM-density/interactive/20260923T164118Z-full-proof-paper/NEW_PROJECTED_CROSSING.md` with two literal physical hubs (`k=2` there), split `I=S,J=T`, and `ell=1`. The hub law is exactly `(X_a,X_b)`, so its joint density cap is one. The hub-to-`T` singular-value product is `sqrt(Delta)`, and the one-volume projected crossing is `Z`. Thus

`||p_Q||_infinity <=3*2^(5/6) Delta^(-1/6) Z^(-1/6)=3*2^(5/6)V^(-1/6)`.

The source theorem gives an `L1` characteristic function, hence continuity and the direct linear interval bound.

### Case 2: concentrated projected crossing

Otherwise some physical `k in S` has `||c_k||^2>Z/2`. Promote this literal coordinate to a third hub `H={a,b,k}` and condition on the remaining coordinates in `S\{k}` and outside the displayed banks. The physical three-hub cross block into `T` is

`N=[B;d_k]`.

Its three-singular-value product `Gamma` satisfies exactly

`Gamma^2=det(NN^T)=Delta ||c_k||^2 > Delta Z/2=V/2`.

Apply the completed three-hub theorem (Claude continuation, `single_hub_core/REPORT.md`, Theorem 6.3): for three literal physical hubs with arbitrary hub block and arbitrary measurable remainder,

`||p_Q||_infinity <=3 sqrt(2) Gamma^(-1/3)`.

Therefore

`||p_Q||_infinity <3 sqrt(2) 2^(1/6)V^(-1/6)`.

Since `3 sqrt(2)2^(1/6) < 3*2^(5/6)`, the Case 1 constant dominates. The theorem follows.

No pair-core determinant is inverted. In particular the bound is uniform across zero, rank-one, definite and indefinite `A[{a,b},{a,b}]`.

## Immediate splice to account03/B09 r35

R35 supplied a localized pair with

`V_ab(S)>=27 G_*/400`.

The theorem therefore gives, with no full-range column-leverage assumption,

`boxed: ||p_Q||_infinity <=3*2^(5/6)(400/27)^(1/6) G_*^(-1/6) <8.378 G_*^(-1/6).`

Thus the r36 `high-column-leverage` survivor is eliminated: range-projection leverage is no longer part of the localized-pair proof interface. The remaining B09 issue is global scale/structural routing of `G_*`, not a near-stratum or column-leverage analytic gap.

## Required designated partner actual inequality

The completed account04/B09 physical-cross theorem gives `||p_Q||_infinity<=3|det K|^(-1/3)` for a literal invertible physical `3x3` cross block `K`, with arbitrary same-side curvature and continuous density. On the target-valid block matrix

`A_eps=[[0,M],[M,0]]`, `M=diag(1,1,1,eps)`, `0<eps<=1`,

the spectrum is `{+1,+1,+1,+eps,-1,-1,-1,-eps}`. The first three rows/columns give `K=I_3`, hence the partner theorem gives the actual uniform inequality

`boxed: ||p_(X^T A_eps X)||_infinity <=3`.

For every `eps>0` the full cross-range projection is the identity (maximum leverage one), so this is also a concrete control showing why full-range column leverage is the wrong obstruction.
