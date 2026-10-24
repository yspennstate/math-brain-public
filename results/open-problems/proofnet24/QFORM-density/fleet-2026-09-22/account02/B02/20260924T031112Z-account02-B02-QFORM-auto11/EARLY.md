# account02/B02 auto11 — early calculation: punctured internal-curvature exterior lift

Programme: `QFORM-DENSITY-3EIG-20260922`  
Run: `20260924T031112Z-account02-B02-QFORM-auto11`  
Role: Integrated Fourier estimate / complementary constructions and source-valid counterexamples.

The full unrestricted QFORM target remains OPEN. This calculation uses only literal original-coordinate cuts. Singular vectors below are coefficient-only bookkeeping; no rotated random variables are asserted independent.

## 1. Live input

Use the live account01/B02 low-E3 packet: for a physical full-partition crossing `M=A[S,T]`, one survivor has

`x1*x2 > 247/576`,

where `x1>=x2>=...` are the squared singular values, together with a retained small transverse tail. The preceding B02 full-cut lift pays transverse OUTSIDE escape. The remaining obligation is same-side/internal curvature aligned with the two robust crossing directions.

## 2. Punctured same-side aggregate

Let `B=A[S,S]`. For each `k in S`, delete physical row `k` and put

`M^(k)=M[S\{k},T]`,
`b_k=B[S\{k},k]`.

Define

`W_k := sum_{R subset S\{k}, |R|=3} sum_{C subset T, |C|=2}
          det([ M[R,C] , b_k[R] ])^2`,

and `W_S=sum_k W_k`.

Equivalently, `W_k` is exactly the part of `E3([M^(k),b_k])` using two columns from `M^(k)` and the appended physical internal-curvature column `b_k`.

## 3. Random physical split turns W_S into genuine D' currency

Choose a subset `L subset S` by independent fair Bernoulli labels and form the literal physical cross block

`C_L = A[L, T union (S\L)] = [ M[L,T], B[L,S\L] ]`.

Every determinant counted in `W_k` uses three distinct row coordinates `R subset S\{k}` and the distinct internal column coordinate `k`. It occurs as a literal `3x3` minor of `C_L` whenever `R subset L` and `k notin L`, an event of probability `1/16`. All squared minors are nonnegative. Therefore

`E_L E3(C_L) >= W_S/16`,

so some deterministic original-coordinate split satisfies

`boxed: E3(C_L) >= W_S/16.`

Applying the completed marginal-free physical-E3 sharp-HY/D' compiler gives

`||p_Q||_infinity <= C3 (W_S/16)^(-1/6),`
`C3=10.3450832321475...`,

and genuine unweighted Fourier L1. On the same actual physical block the reviewed D5 estimate is simultaneously available:

`||p_Q||_infinity <= (5e/sqrt(2)) E5(C_L)^(-1/10)`

whenever its fifth exterior volume is positive.

Thus `W_S>=2^-18` already pays the ambient law by

`||p_Q||_infinity <= C3*2^(22/6) <131.375`,

with a continuous C0 density.

## 4. What failure of this exit means geometrically

Let `M=U diag(s_j)V^T` and let `u_1,u_2` be the first two left singular vectors. Write

`ell_k=u_1(k)^2+u_2(k)^2`,

and let `U_2^(-k)` be their restrictions to `S\{k}`. Put

`d_k = dist(b_k, span(U_2^(-k)))`.

Right-orthogonally rotating the `T` columns preserves the aggregate over physical column pairs. Retaining only the pair of top singular columns in the resulting nonnegative wedge sum gives the exact lower bound

`boxed: W_k >= x1*x2 (1-ell_k) d_k^2.`

Indeed

`||s1 u_1^(-k) wedge s2 u_2^(-k)||^2
 =x1*x2 det(I_2-r_k r_k^T)
 =x1*x2(1-ell_k),`

where `r_k=(u_1(k),u_2(k))`, and wedging with `b_k` multiplies by the squared distance from the punctured two-plane.

Hence on the live packet

`boxed:
 W_S >= (247/576) sum_(k in S) (1-ell_k)d_k^2.}`

If there is no top-two near-coloop on the S side, say `ell_k<=3/4` for every k, then

`sum_k d_k^2 <= [4/(x1*x2)] W_S < (2304/247) W_S.`

So failure of the D' exit at `W_S<2^-18` forces the entire punctured off-diagonal internal curvature on S to lie, in squared aggregate, within

`(2304/247)2^-18 <3.56e-5`

of the physical crossing's two-dimensional left carrier, unless a physical near-coloop exists. The transposed statement holds on T.

This converts the broad phrase “rank-two crossing plus arbitrary same-bank curvature” into a quantitative physical dichotomy: transverse same-side curvature creates a real D' cross cut; failure leaves only a punctured carrier-aligned two-sided curvature packet or a near-coloop.

## 5. Correction boundary

The fresh account03/B16 correction `QFORM-MIXED-PLUCKER-ABSOLUTE-TTSTAR-BARRIER-v1` is respected. Nothing here replaces missing per-bank projection control by total mixed Pluecker mass inside the refuted absolute kernel. The construction first creates a literal physical cross block and only then invokes the proved D'/D5 Fourier receivers.
