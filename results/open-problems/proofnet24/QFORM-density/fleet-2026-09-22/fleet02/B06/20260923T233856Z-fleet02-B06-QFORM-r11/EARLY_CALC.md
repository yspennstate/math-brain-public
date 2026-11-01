# fleet02/B06 r11 early calculation — anchored square / shear-flat 3-minor factor

Programme `QFORM-DENSITY-3EIG-20260922`. Full target remains OPEN. This note records the first unpaid implication early; no full-QFORM claim is made.

## 1. Source-valid square + E2 receiver

Let `h` be one literal original coordinate and let `I,J` be disjoint original-coordinate banks avoiding `h`. Write the corresponding rectangular coefficient block as

`A[{h}∪I,{h}∪J] = [[a,q^T],[p,M]]`, with `a=A_hh != 0`.

After completing the square in `X_h`, the Schur-complement cross block between `I,J` is

`M' = M-pq^T/a`.

The pinned proved square peel in `math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837:.../FOURIER_ROUTE_REPORT.md`, Lemma 4.2, gives

`D(Q) <= |a|^(-1/2) H_(1/2)(A/h)`.

The already proved fleet02/B06 theorem `QFORM-E2-HALFRIESZ-ROW-GATE-FREE-v1`, canonical commit `b38a9627f059b13d532f5c208c30579ec2d2d362`, applied to the literal cross block `M'`, gives

`H_(1/2)(A/h) <= 8 e^(1/4) e_2((M')^T M')^(-1/8)`.

For every two-row set `P⊂I` and two-column set `R⊂J`, Schur determinant identity gives

`det A[{h}∪P,{h}∪R] = a det M'[P,R]`.

Hence with the aggregate anchored 3-minor currency

`W_h(I,J) := sum_(|P|=|R|=2) det A[{h}∪P,{h}∪R]^2`,

we have the exact identity

`W_h(I,J)=a^2 e_2((M')^T M')`.

Therefore

`D(Q) <= 8 e^(1/4) |a|^(-1/4) W_h(I,J)^(-1/8)`.          (1.1)

No individual minor is inverted and all same-bank curvature and outside couplings survive inside the Schur complement.

## 2. Exact partner-r47 shear-flat factorisation

The designated partner fleet03/B06 r47 has the shear-flat residual

`S = D + E^T T E`,

where `D=diag(d_1,...,d_m)`, `E` is a physical `2×m` frame with columns `e_j`, and `T=T^T` is `2×2`. Fix `h`; take disjoint `I,J` avoiding `h`. For `P={p,q}⊂I`, `R={r,s}⊂J`, direct Schur factorisation (or polynomial continuation if `S_hh=0`) yields

`det S[{h}∪P,{h}∪R]
 = d_h det(T) det(e_p,e_q) det(e_r,e_s)`.                 (2.1)

Indeed, for `a_h=S_hh !=0`, the post-`h` rank-two coefficient is

`T_h=T-(T e_h)(T e_h)^T/a_h`,

and the matrix determinant lemma gives

`det T_h = det T * d_h/a_h`.

Multiplying the `2×2` cross determinant by the Schur pivot `a_h` proves (2.1). Both sides are polynomial, so the identity extends through `a_h=0`.

Summing squares gives the exact aggregate identity

`W_h(I,J)=d_h^2 det(T)^2 W_I W_J`,                       (2.2)

where `W_I=det(E_I E_I^T)=sum_(P⊂I,|P|=2) det(E_P)^2` and similarly for `J`.

Thus whenever `a_h=S_hh !=0`, equation (1.1) pays this partner subbranch with

`D(S) <= 8 e^(1/4) |a_h|^(-1/4)
        [d_h^2 det(T)^2 W_I W_J]^(-1/8)`.                (2.3)

This identifies an exact new route: the square pivot is useful precisely through the *diagonal twist* `d_h` times the residual pair-area packet; the apparent rank-two pivot contribution `e_h^TTe_h` cancels from the anchored determinant.

## 3. Product-weighted partition form

Let `G=EE^T` and let partner-r47 leverage be `alpha_h=e_h^T G^(-1)e_h`. If `alpha_h<1`, then

`L_h := det(E_{-h}E_{-h}^T)=det(G)(1-alpha_h)`.

Normalize squared pair areas on pairs avoiding `h`, and let `Omega_h` be the probability that two iid sampled pairs are disjoint. Under a fair random bipartition of the remaining physical coordinates,

`E[W_I W_J]=L_h^2 Omega_h/16`.

So some cut obeys

`W_IW_J >= det(G)^2(1-alpha_h)^2 Omega_h/16`,

and (2.3) becomes

`D(S) <= 8 sqrt(2) e^(1/4) |a_h|^(-1/4)
 [|d_h det(T)| det(G)(1-alpha_h)]^(-1/4) Omega_h^(-1/8)`. (3.1)

Partner r47 gives a heavy coordinate `alpha_h>3/5` when its global pair-law overlap `Omega<1/256`. Equation (3.1) therefore pays the heavy-hub branch unless one of the now-explicit currencies collapses: `a_h`, `d_h`, `1-alpha_h`, or the conditioned disjoint-pair probability `Omega_h`. That is a strictly narrower debt than an uncontrolled curved-fiber supremum.

Finite algebra check (1000 random symmetric `T`, random `E,D`, fixed disjoint pairs) gave maximum absolute error `4.98e-14` in (2.1); 200 aggregate tests gave maximum relative error `8.56e-14` in (2.2). These are sanity checks, not proof.

Next: compose (3.1) with the existing indefinite outer-pair receiver in r47 and classify the collapse cases, especially the zero-diagonal endpoint where a square pivot is unavailable.
