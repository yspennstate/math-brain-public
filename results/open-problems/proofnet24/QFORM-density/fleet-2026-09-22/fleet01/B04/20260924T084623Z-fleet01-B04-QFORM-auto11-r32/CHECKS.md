# Deterministic checks — fleet01/B04 r32

Marker: `QFORM_B04_R32_SQUARE_RANK2_CHECK_PASS`

All symbolic identities below are exact; decimals are only evaluations.

## A. Rearrangement/Hölder constants

For `1<p<2`, put `q=p/(p-1)` and `Gamma=sqrt(M_R M_C)`.

Square bound:

`||h||_p^p <= 2^(p-1)/(2-p)`.

Rank-two crossing envelope:

`m_K(t)=min(1,K/|t|)`, `K=pi Gamma P^(-1/2)`.

Exact integral:

`||m_K||_p^p = 2Kp/(p-1)`.

Combining `(2pi)^(-1)`, Hausdorff-Young factor `(2pi)^(1/q)`, the square `L^p` factor, and the crossing factor gives

`C_p = [2^(p-1) Gamma p/((2-p)(p-1))]^(1/p)`

and

`||p_Q||_infinity <= C_p |b|^(-(p-1)/p) P^(-1/(2p))`.

For universal product projection caps `M_R,M_C<=2`, `Gamma<=2`, hence

`C_p <= 2[p/((2-p)(p-1))]^(1/p)`.

At `p=3/2`, `Gamma=1`,

`C_(3/2)=(6sqrt(2))^(2/3)=4.160167646103808...`.

## B. Five-dimensional exact-three-large-eigenvalue carrier

`D=[[1/4,1/16],[1/16,1/4]]` has eigenvalues `5/16,3/16` on the symmetric/antisymmetric vectors.

`N=[[5/4,3/4],[3/4,5/4]]` has singular/eigenvalues `2,1/2`, hence `P=1`.

For the active block `[[D,N],[N,D]]`, symmetric/antisymmetric bank combinations reduce it to `D+N` and `D-N`. Therefore its exact eigenvalues are

`37/16, 11/16, -27/16, -5/16`.

After adjoining the source-separated coefficient `b=1`,

`spec(A_5)={37/16,11/16,1,-5/16,-27/16}`.

Exactly three have absolute value at least one: `37/16`, `1`, `-27/16`.

Both rank-two banks are exactly two original physical coordinates, so their orthogonal projected joint density caps are at most one. With `p=3/2`,

`bound=(6sqrt(2))^(2/3)=4.160167646103808...`.

## C. Partner r21 splice arithmetic

For partner matrix `A_*`, choose physical rows `R={1,3}` and columns `C={2,4,5,6}`. The crossing is

`N_*=[[1,1/10,1/10,1/10], [1/5,199/200,199/200,199/200]]`.

Then

`N_* N_*^T = [[103/100,997/2000],[997/2000,120403/40000]]`.

Its determinant is

`(103/100)(120403/40000)-(997/2000)^2 =4563/1600`.

Thus the singular product is

`P_*=sqrt(4563/1600)=sqrt(4563)/40=1.6887495373796555...`.

The row bank has exactly two original coordinates (`M_R<=1`), while the other projected two-plane has `M_C<=2`, hence `Gamma<=sqrt(2)`. At `p=3/2`,

`bound=12^(2/3) P_*^(-1/3)=4.401483549380131...`.

The completed partner bound is

`3sqrt(pi)=5.317361552716548...`,

so the improvement factor on `[1] direct_sum A_*` is

`3sqrt(pi)/4.401483549380131...=1.208083931942766...`.

## D. Critical small-square stress

For the fleet02/B04 r22 early stress, `b=1/192`, `P=4`, and because the left bank consists of two original coordinates while the right projected two-plane has the universal cap two, `Gamma<=sqrt(2)`.

At rational exponent `p=19/16`, the theorem gives

`10.772087181930972...`.

Direct one-variable minimization of the explicit displayed theorem RHS gives approximately

`p=1.17730586`, `bound=10.75729089`.

The numerical optimization is only a check; the rigorous stated inequality uses the exact rational exponent when needed.

## E. Logarithmic corollary algebra

In the universal-cap case define `R=sqrt(P)/|b|` and `L=log R>1`. With `p=1+1/L`,

`(p-1)/p=1/(L+1)`,

`p/((2-p)(p-1))=L(L+1)/(L-1)`,

`R^((p-1)/p)=exp(L/(L+1))`.

Therefore the selected-exponent bound is exactly

`(2/sqrt(P)) [e L(L+1)/(L-1)]^(L/(L+1))`,

which is asymptotic to `(2e/sqrt(P)) log R`.
