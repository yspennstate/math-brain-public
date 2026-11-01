# fleet01/B03 r29 addendum — row-marginal-free arbitrary-rank rank-three crossing compiler

Status: `NEW SUPPORTING THEOREM / ANALYTIC CROSSBLOCK GATE REMOVED / FULL_QFORM_OPEN`.

This addendum strengthens `REPORT.md`. It uses the weighted-subset Fourier lemma from `math-open-problems@4f92aeb74083c6f95cb314a11fed1b812eacef9a`, `proofnet24/QFORM-density/interactive/20260923T164118Z-full-proof-paper/NEW_PROJECTED_CROSSING.md`, and the row-marginal-free one-hub theorem proved in this run. The partner dependency inside the heavy branch remains fleet02/B03 `math-open-problems@c3bba054c20287883c43303711eec7eefc05d46e`.

## Theorem — `QFORM-ROW-MARGINAL-FREE-3VOLUME-CROSSBLOCK-v1`

Let the original independent cap-one coordinates be split into two nonempty banks `I,J`. Write the quadratic polynomial as

`Q=F(X_I)+2 X_I^T B X_J+G(X_J)`,

where `F,G` are arbitrary quadratic-plus-affine functions on their own banks and `B=A_{I,J}` is an arbitrary real matrix, of any rank. Let its row vectors be `b_i`, `i in I`, and define the total squared physical three-volume

`Z_3 = sum_{i<j<k}|b_i wedge b_j wedge b_k|^2
     = e_3(BB^T)`.

If `Z_3>0`, then Q has a continuous `C_0` density and

`||p_Q||_infinity
 <= C_cross Z_3^(-1/6)`,

with

`C_cross = 3*2^(3/2)*exp(1/2)
         = 13.989863889582747...`.

Thus every interval K satisfies

`P(Q in K) <= C_cross Z_3^(-1/6)|K|`.

No volume-row-marginal assumption and no exact-rank assumption on B is required.

Moreover, for an independent copy Q', retaining the scalar copy difference intact,

`int_R |t|^(-1/2)|phi_Q(t)|^2 dt
 <= C_time Z_3^(-1/12)`,

where

`C_time=(24/5)*2^(3/4)*sqrt(pi)*exp(1/4)
      =18.372247652462104...`,

and hence

`E|Q-Q'|^(-1/2)
 <=7.329466374573101... Z_3^(-1/12)`.

### Proof

Let

`alpha_i = Z_3^(-1) sum_{j<k, j,k != i}|b_i wedge b_j wedge b_k|^2`.

Then `sum_i alpha_i=3`.

### Diffuse case: every alpha_i<=1/2

Use the source weighted-subset Fourier lemma with no conditioning projection (`k=0`) and `ell=3`. This zero-dimensional specialization is immediate from the displayed lemma: the auxiliary variable `MD` and probability density kappa disappear, while all remaining steps are unchanged.

For completeness, the same estimate follows directly. Apply Cauchy-Schwarz in the I-bank:

`|phi_Q(t)|^2
 <= E_{X_J,X_J'} prod_{i in I}|psi_i(2t <b_i,X_J-X_J'>)|`,

where `psi_i` is the characteristic function of the original physical coordinate `X_i`. The difference coordinates in `D_J=X_J-X_J'` are independent with densities at most one. The weighted-subset lemma gives

`|phi_Q(t)|^2
 <= min{1,
   [2^(9/2) pi^3 exp(3/2)]/[sqrt(Z_3)|t|^3]}`.

Therefore

`|phi_Q(t)|
 <=min{1,
   K_0 Z_3^(-1/4)|t|^(-3/2)}`,

with

`K_0=2^(9/4)pi^(3/2)exp(3/4)
   =56.074209607569024...`.

Integrating this `L^1_t` envelope yields

`||p_Q||infinity
 <=3*2^(3/2)exp(1/2)Z_3^(-1/6)`.

Fourier inversion gives a continuous `C_0` density.

### Heavy case: some alpha_i>1/2

Fix such an i and promote the genuine physical coordinate `X_i` to a hub. Put `m=b_i`, project every other row orthogonally away from m,

`c_j=b_j(I-P_m)`,

and let

`Z_2'=sum_{j<k, j,k!=i}|c_j wedge c_k|^2`.

The exact exterior-algebra identity is

`||m||^2 Z_2'
 =sum_{j<k, j,k!=i}|m wedge b_j wedge b_k|^2
 =alpha_i Z_3`.                                               (A.1)

Thus the one-hub aggregate from `REPORT.md` is

`V_3'=||m||^2Z_2'=alpha_i Z_3 > Z_3/2`.

Apply `QFORM-ONE-HUB-ROW-MARGINAL-FREE-2VOLUME-v1` from this run:

`||p_Q||infinity
 <=C_* (V_3')^(-1/6)
 < C_* 2^(1/6) Z_3^(-1/6)`

`=10.550168831164775... Z_3^(-1/6)`,

which is strictly smaller than `C_cross Z_3^(-1/6)`. The heavy theorem gives a continuous `C_0` density.

Its characteristic-function coefficient is at most

`K_* 2^(1/4)Z_3^(-1/4)
 =2^2 pi^(3/2)exp(1/2)Z_3^(-1/4)`,

which is also strictly below the diffuse coefficient `K_0 Z_3^(-1/4)`. Hence the diffuse envelope dominates both cases globally.

Squaring that envelope and integrating with weight `|t|^(-1/2)` gives

`int |t|^(-1/2)|phi_Q(t)|^2 dt
 <=(24/5)K_0^(1/3)Z_3^(-1/12)`

`=(24/5)2^(3/4)sqrt(pi)exp(1/4)Z_3^(-1/12)`.

The copy-Riesz bound follows from

`int |t|^(-1/2)|phi_Q(t)|^2 dt
 =sqrt(2pi) E|Q-Q'|^(-1/2)`.

No coordinate sum/difference pair is separated or assigned a conditional density cap. QED.

## Singular-value corollary

If the cross block B has at least three positive singular values `s_1>=s_2>=s_3>0`, then

`Z_3=e_3(s_1^2,s_2^2,...)
    >=s_1^2s_2^2s_3^2`.

Therefore

`||p_Q||infinity
 <=13.9898638896 (s_1s_2s_3)^(-1/3)
 <=13.9898638896 s_3(B)^(-1)`.

So ANY physical coordinate cut with `s_3(A_{I,J})>=c` is now paid by `13.99/c`, irrespective of volume leverage, exact rank, extra crossing directions, internal quadratic curvature, or dimension.

This removes the analytic row-marginal gate from the rank-three cross-block branch. The remaining debt for the full conjecture is structural: from `s_3(A)>=1`, produce a cut with `s_3(A_{I,J})` or aggregate `Z_3` at universal scale, or route matrices with no such cut into the already-paid diagonal/pivot/grouped-hub/low-cross-rank packets. Diagonal matrices show that no universal cross-cut theorem can hold without such an alternative.
