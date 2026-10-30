SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet02, slot B15, 2026-09-24T10:01:00Z.
attacking: full-law rough regularity on the diffuse rank-three Fresnel chamber, including the complementary two-sheet side; then the ruled one-sheet rough-input bridge.

# fleet02/B15 — diffuse full-law submass and target-uniform rough-law stability

Programme: `QFORM-DENSITY-3EIG-20260922`.
Status: `NEW SUPPORTING THEOREM / FULL_QFORM_OPEN`.

## 1. First unpaid implication

The full conjecture remains open. This run removes a regularity debt in the exact/diffuse rank-three chamber, including the convex/two-sheet side: the first unpaid implication is now structural. One still needs a product-preserving aggregate reduction from the bare hypothesis `s_3(A)>=1` into either (i) a diffuse rank-three/diagonal Fresnel chamber, or (ii) one of the already-paid localized, physical-pair, grouped-crossing, or hub receivers, without reciprocal-minor or worst-fibre losses. Higher-rank and twisted/localized carrier configurations are not covered by the theorem below.

The live corrections remain binding: no post-rotation independence, no arbitrary-joint coarea shortcut, no generic two-sheet X-ray argument, and no assumption that a small matrix perturbation is a small random quadratic perturbation for arbitrary unbounded inputs.

## 2. Source inputs actually used

Required fixed source:

`yspennstate/math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837`
`proofnet24/QFORM-density/interactive/20260922T211500Z-decoupling-brascamp-lieb/`

I read `RESULTS.md`, `FOURIER_ROUTE_REPORT.md`, and `COUNTEREXAMPLE_SEARCH.md`. The completed input used below is Theorem F (Fresnel–Brascamp–Lieb): for

`A = D + R Lambda R^T`, `R^T R=I_3`, `D` diagonal,

with row leverages `c_i=|R_{i,*}|^2<=1/2`, arbitrary deterministic affine terms, and arbitrary independent cap-one probability marginals,

`|phi(t)| <= (4 pi)^(3/2) |t|^(-3/2) |lambda_1 lambda_2 lambda_3|^(-1/2)`

and hence

`||p_Q||_infinity <= 12 |lambda_1 lambda_2 lambda_3|^(-1/3)`.

I also use the completed ruled one-sheet Theorem C from the same source only in its stated one-sheet scope.

Latest designated partner actually consumed:

`yspennstate/math-open-problems@b8cb4aa22c840d8f4fc76bcca6d0cb49d4aeb9f9`
`proofnet24/QFORM-density/fleet-2026-09-22/fleet03/B15/20260924T092642Z-fleet03-B15-qform-auto11/REPORT.md`.

Its fixed-Hessian theorem says every rank-at-least-three affine quadratic under arbitrary rough cap-one product inputs has a canonical `C_0` density, and its regularity conclusion is downstream of height. I apply that theorem below after an independent interval-height payment for a concrete diffuse-bank family.

## 3. New theorem: full-law submass gain inside Theorem F

### Theorem 1 — `QFORM-FRESNEL-SUBMASS-2OVER3-v1`

Let `R` be an `n x 3` matrix with orthonormal columns, let

`Lambda=diag(lambda_1,lambda_2,lambda_3)`, `lambda_k !=0`,

put

`L=|lambda_1 lambda_2 lambda_3|`, `c_i=|R_{i,*}|^2`,

and assume `max_i c_i<=1/2`. Let `D` be arbitrary diagonal and let `b,c` be arbitrary deterministic affine data. All original coordinates are independent and all factors except one are cap-one probability densities. Replace coordinate `j` by a subdensity `g`,

`0<=g<=1`, `int g=m<=1`.

Let `nu_g` be the finite output submeasure of

`Q(X)=X^T(D+R Lambda R^T)X+b^T X+c`.

Then `nu_g` has an `L^infinity` density. If `c_j>0`,

`boxed( ||d nu_g/dt||_infinity <= 12 L^(-1/3) (2 sqrt(c_j))^(-2c_j/3) m^(1-2c_j/3). )`   (3.1)

For `c_j=0`, the limiting bound is

`boxed( ||d nu_g/dt||_infinity <= 12 L^(-1/3) m. )`                  (3.2)

In particular, uniformly for `0<=c_j<=1/2`,

`boxed( ||d nu_g/dt||_infinity <= 12 exp(1/(12e)) L^(-1/3) m^(2/3). )` (3.3)

This is a FULL-LAW estimate; it does not split one-sheet and two-sheet output regions.

### Proof

Write the selected twisted factor in Theorem F as

`a_j(x)=g(x) exp(i tau_j(x))`,

where `tau_j` contains the diagonal quadratic twist, affine phase, and the shift produced by conditioning/Fresnel variables. Its Fourier transform satisfies two bounds that retain the submass:

`||a_j^hat||_infinity <= ||g||_1=m`,

and, by Plancherel and `g^2<=g`,

`int |a_j^hat(s)|^2 ds = 2 pi int g(x)^2 dx <=2 pi m`.

Hence for every `p>=2`,

`int |a_j^hat(s)|^p ds <= ||a_j^hat||_infinity^(p-2) ||a_j^hat||_2^2 <=2 pi m^(p-1)`.  (3.4)

The ordinary cap-one bound from the source also remains available:

`int |a_j^hat|^p <=4 pi/sqrt(p)`.                                   (3.5)

In Theorem F's geometric Brascamp–Lieb step, the exponent for row `j` is `c_j` and `p=1/c_j`. For every probability coordinate `i!=j`, the source calculation contributes `(4 pi)^{c_i}`. For coordinate `j`, (3.4) gives instead

`[c_j^(-1/2) 2 pi m^(1/c_j-1)]^(c_j)
 = (4 pi)^(c_j) (2 sqrt(c_j))^(-c_j) m^(1-c_j).`

Therefore the entire source Fourier estimate sharpens to

`|nu_g^hat(t)| <= B_0 eta_j |t|^(-3/2)`,                            (3.6)

where

`B_0=(4 pi)^(3/2)L^(-1/2)`,

`eta_j=(2 sqrt(c_j))^(-c_j)m^(1-c_j)`.

The trivial finite-mass estimate is `|nu_g^hat(t)|<=m`. Thus

`int_R |nu_g^hat(t)| dt <= 6 (B_0 eta_j)^(2/3)m^(1/3)`.             (3.7)

Fourier inversion for this finite measure gives

`||d nu_g/dt||_infinity <= (3/pi)(B_0 eta_j)^(2/3)m^(1/3)`,

which is exactly (3.1), since `(3/pi)B_0^(2/3)=12L^(-1/3)`.

If `c_j=0`, the rank-three Fresnel phase is independent of `X_j`; retaining the separate twisted factor only costs its mass `m`, so (3.2) follows directly (and is also the continuous `c_j downarrow0` limit of (3.1)).

For (3.3), define

`a(c)=(2 sqrt(c))^(-2c/3)`.

Its logarithm is `-(2c/3)(log2+(1/2)log c)`, whose maximum on `[0,1/2]` occurs at `c=1/(4e)` and equals `1/(12e)`. Also `1-2c/3>=2/3` and `0<m<=1`. Hence (3.3).

No continuity premise was used to obtain any height bound. The `L^1` Fourier estimate happens also to provide continuity afterwards; the logical payment of essential height is already (3.7).

## 4. New theorem: dimension-free full-law stability for diffuse frames

### Theorem 2 — `QFORM-FRESNEL-DIFFUSE-L1-STABILITY-v1`

In the setting of Theorem 1, let two cap-one product laws `f=(f_i)` and `g=(g_i)` be given. Put

`delta_i=||f_i-g_i||_1`, `Delta=sum_i delta_i`.

Then the canonical output densities satisfy the coordinate-sensitive bound

`boxed( ||p_f-p_g||_infinity <= 12 L^(-1/3) sum_i c_i^(-c_i/3) delta_i^(1-2c_i/3), )` (4.1)

with the convention `0^0=1` at `c_i=0`.

If in addition `c_i<=h<=1/2` for all `i`, define

`B(h)=max_{0<=c<=h} c^(-c/3)
     = h^(-h/3)                    if h<=e^(-1),
       exp(1/(3e))                  if e^(-1)<=h<=1/2.`

Then

`boxed(
 ||p_f-p_g||_infinity
 <= 12 B(h)L^(-1/3)[ Delta + (3/h)^(2h/3) Delta^(1-2h/3) ].
)`                                                                  (4.2)

This modulus is independent of ambient dimension. At the endpoint `h=1/2`,

`boxed(
 ||p_f-p_g||_infinity
 <=12 exp(1/(3e)) L^(-1/3)[Delta+6^(1/3)Delta^(2/3)].
)`                                                                  (4.3)

As `h downarrow0`, (4.2) tends to a Lipschitz-type `24L^(-1/3)Delta` bound.

### Proof

Telescope the product law one original coordinate at a time. For coordinate `i`, write

`f_i-g_i=u_i-v_i`,

where `u_i,v_i` are cap-one subdensities and each has mass `delta_i/2`. Apply (3.1) to each sign and add. The powers of 2 cancel exactly:

`2 * 12 L^(-1/3)(2 sqrt(c_i))^(-2c_i/3)(delta_i/2)^(1-2c_i/3)
 =12 L^(-1/3)c_i^(-c_i/3)delta_i^(1-2c_i/3).`

Summing proves (4.1).

For (4.2), let `p_h=1-2h/3`. Because

`1-2c_i/3=(1-c_i/h)*1+(c_i/h)*p_h`,

weighted AM–GM gives

`delta_i^(1-2c_i/3)
 <=(1-c_i/h)delta_i+(c_i/h)delta_i^(p_h).`                           (4.4)

Now `sum_i c_i=3` (three orthonormal columns). With weights `w_i=c_i/3`, concavity of `x -> x^(p_h)` and `c_i<=h` give

`sum_i c_i delta_i^(p_h)
 <=3[(1/3)sum_i c_i delta_i]^(p_h)
 <=3(h Delta/3)^(p_h).`                                             (4.5)

Substituting (4.5) into (4.4) and summing gives

`sum_i delta_i^(1-2c_i/3)
 <=Delta+(3/h)^(2h/3)Delta^(1-2h/3).`                               (4.6)

Finally `c_i^(-c_i/3)<=B(h)`, proving (4.2).

This is stronger, in the diffuse Theorem-F chamber, than the latest fleet03/B15 fixed-matrix square-root modulus: here the constant and modulus are uniform over dimension, all admissible input laws, all affine terms, and all frames satisfying the quantitative leverage gate. The partner theorem is still useful downstream because it identifies canonical `C_0` representatives for arbitrary fixed rank-at-least-three Hessians, including chambers where no uniform Theorem-F gate is known.

## 5. Actual target family and completed-source application

Split `3m` original independent cap-one coordinates into three disjoint banks and set

`Y_k=m^(-1/2) sum_{r=1}^m X_{k,r}`,

`Q_m=Y_1^2+Y_2^2-Y_3^2`, `m>=2`.

The matrix has nonzero spectrum `{1,1,-1}`. Every physical row leverage in its rank-three spectral frame is exactly `1/m<=1/2`, so the completed fixed-source Theorem F applies to the ENTIRE output law, including the two-sheet side:

`boxed( ||p_{Q_m}||_infinity <=12. )`                               (5.1)

The same fixed source's ruled Theorem C separately gives the sharper one-sheet inequality

`boxed( P(Q_m in I, Q_m>=0) <= pi sqrt(2)|I|. )`                    (5.2)

There is also a stronger full-law estimate specific to this product-bank family. The one-dimensional projection theorem gives `||p_{Y_k}||_infinity<=sqrt(2)`. Hence

`p_{Y_k^2}(s)<=sqrt(2)/sqrt(s)`, `s>0`.

Therefore

`||p_{Y_1^2+Y_2^2}||_infinity
 <=2 int_0^t [s(t-s)]^(-1/2) ds
 =2 pi.`

Convolution with the independent probability law of `-Y_3^2` cannot increase `L^infinity`, so

`boxed( ||p_{Q_m}||_infinity<=2 pi. )`                              (5.3)

This is an essential-height estimate, obtained before continuity.

Now apply the latest designated fleet03/B15 partner theorem: `rank(A_m)=3`, so the arbitrary rough product input has a canonical `C_0` density. Combining that downstream regularity fact with the already-paid interval domination (5.3) yields

`boxed( p_{Q_m} in C_0(R),  0<=p_{Q_m}(t)<=2pi for every t. )`       (5.4)

Thus the partner result is used only after the height is paid; continuity does not create the bound.

The new stability theorem adds a genuinely dimension-free rough-law statement for this same exact target. If the two product inputs have total marginal `L^1` change `Delta`, then with `h=1/m`, `L=1`,

`boxed(
 ||p_f-p_g||_infinity
 <=12 B(1/m)[Delta+(3m)^(2/(3m))Delta^(1-2/(3m))].
)`                                                                  (5.5)

For `m>=3`, `B(1/m)=m^(1/(3m))`. As `m` grows the exponent tends to one and the coefficient tends to the finite Lipschitz limit. This is a full-law statement, so the two-sheet side has no separate rough-regularity debt in this diffuse-bank chamber.

## 6. Independent audit of the required ruled/rough-input bridge

The fixed source's one-sheet theorem is geometric. On the standard cone/hyperboloid

`q_0(z)=z_1^2+z_2^2-z_3^2`,

use

`F(theta,t)=sqrt(s)e_theta+t(e_theta^perp+e_3)`.

A direct differentiation gives

`F_theta x F_t=(1/2) grad q_0(F)`,

hence the coarea quotient is exactly

`d sigma/|grad q_0|=(1/2)dtheta dt`.                                (6.1)

After undoing spectral scaling for curvatures `(lambda_1,lambda_2,mu)`, the ruling direction is

`v_theta=(-sin(theta)/sqrt(lambda_1), cos(theta)/sqrt(lambda_2), 1/sqrt(mu)).`

The parameter `t` is not arclength. Consequently the line integral pays `1/|v_theta|`; omitting this factor is incorrect. The two-dimensional product-projection cap `2` cancels the coarea `1/2`, reproducing exactly

`C_+=(lambda_1 lambda_2 mu)^(-1/2)
      int_0^(2pi) [sin^2(theta)/lambda_1+cos^2(theta)/lambda_2+1/mu]^(-1/2)dtheta.`

In particular `C_+<=pi sqrt(2)` when all three curvature magnitudes are at least one.

For rough inputs, mollify only ORIGINAL coordinates by a nonnegative probability approximate identity:

`f_i^(eta)=f_i*rho_eta`, `0<=f_i^(eta)<=1`.

For every fixed finite active coordinate set,

`||prod_i f_i^(eta)-prod_i f_i||_1
 <=sum_i ||f_i^(eta)-f_i||_1 ->0.`                                 (6.2)

For a fixed measurable majority event `G` in original-coordinate sample space, restriction by `1_G` and deterministic quadratic pushforward both contract total variation. Therefore if the smooth positive submeasures satisfy

`nu_eta(I)<=C_+|I|`,

then taking `eta downarrow0` in (6.2) gives

`boxed( nu(I)<=C_+|I| )`                                           (6.3)

with exactly the same coefficient. There is no pointwise evaluation of a rough density on a ruling and no use of output continuity.

For an ambient invertible active physical `3x3` block `B`, conditioning on outside original coordinates gives

`Q_w(x)=x^T Bx+2d(w)^T x+c_0(w)
       =(x+B^(-1)d(w))^T B(x+B^(-1)d(w))+c(w).`

Thus the later affine-range correction is automatic in this invertible-block scope: completing the square is a deterministic translation in the original independent coordinates, not a spectral rotation. The same total-variation passage applies fibrewise and then averages in `w`.

## 7. Regularity ledger and obstruction message

1. Qualitative absolute continuity remains separate. A nonconstant affine quadratic pushforward of an absolutely continuous joint law is absolutely continuous by local coarea away from its proper affine critical set. This gives no height.
2. Essential height in Theorems 1–2 is paid by the submass Fourier integral, before any continuity statement.
3. The latest fleet03/B15 result is used downstream to identify canonical `C_0` representatives; it is not used to manufacture a universal bound.
4. The diffuse exact-rank-three complementary/two-sheet side is already paid by completed source Theorem F. The live `QFORM-TWOSHEET-XRAY-ONLY-FALSE` correction remains relevant outside this product-preserving Fourier chamber: generic line/X-ray bounds alone do not control the two-sheet trace.
5. A counterexample to full QFORM therefore cannot come from rough-input discontinuity inside the Theorem-F diffuse chamber. The unresolved target is the structural/aggregate passage from bare `s_3(A)>=1` to a paid chamber, particularly higher-rank twisted carriers and localized/diffuse mixtures where no uniformly conditioned physical block exists.

## 8. Status

New supporting theorem: full-law submass gain `m^(1-2c/3)` and dimension-free aggregate `L^1` stability in the diffuse Fresnel chamber, uniform in dimension and affine terms. Required fixed source applied to an exact owner-target family. Latest fleet03/B15 partner applied after independent height payment to obtain the canonical `C_0` representative. Ruled rough-input bridge independently checked with the exact coarea and non-arclength factors.

Full QFORM remains OPEN.
