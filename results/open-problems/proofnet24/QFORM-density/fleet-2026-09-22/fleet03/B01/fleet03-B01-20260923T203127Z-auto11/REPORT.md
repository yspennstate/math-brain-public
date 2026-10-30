SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet03, slot B01, 2026-09-23T20:31:27Z.
attacking: remove the small-positive projected-crossing interpolation gap by combining the fleet04/B01 W2 scalar-pivot identity with the global quarter-Riesz theorem before averaging the translated scalar-square singularity.

# fleet03/B01 — determinant-free W2 quarter-Riesz compiler

Programme: `QFORM-DENSITY-3EIG-20260922`  
Run: `fleet03-B01-20260923T203127Z-auto11`  
Role: oscillatory replacement / quantitative inequalities  
Status: **NEW SUPPORTING TARGET-LEVEL THEOREM; SMALL-POSITIVE-GAMMA1 GAP PAID; FULL QFORM OPEN**  
Execution: `WITHOUT_VERIFIED_BRAIN`

## 1. Target and correction boundary

The target remains the unrestricted statement: for every finite n, every family of independent real random variables with probability densities bounded by one, and every real symmetric A with at least three eigenvalues of modulus at least one, prove that Q=X^TAX has an essentially bounded density with one universal bound, or exhibit a valid counterexample. No moment, support, Gaussian, log-concavity, connected-support, centering, identical-law, or diagonal-basis hypothesis may be inserted.


The following live corrections are preserved:

* bounded density does not imply any law-uniform pointwise positive-power decay for one-dimensional quadratic phases;
* rotations of the independent physical coordinates do not preserve independence;
* arbitrary bounded projection density does not by itself control an indefinite quadratic pushforward;
* small matrix coefficients cannot be deleted as small random perturbations without moment/support assumptions;
* the corrected fleet04/B01 random-coloring step yields only a product-bank lower bound, not identical lower bounds for each bank. The present proof does not use that corrected-away statement.

The phase-aligned fragmented-support obstruction is retained explicitly in Section 7.

## 2. Source-pinned inputs actually used

### 2.1 Designated partner fleet04/B01: exact scalar-pivot W2 identity

Source:
`yspennstate/math-open-problems@8410ab9d8238baa40c033f83dbae6af44b0b2582`,
`proofnet24/QFORM-density/fleet-2026-09-22/fleet04/B01/20260923T131003Z-fleet04-B01-singular-star-routing-r2/REPORT.md`.

For a literal physical pair S={X,Y} with

`B=[[a,b],[b,c]]`, `a!=0`,

complete only the literal original coordinate X. Put

`delta=c-b^2/a`,
`ell=v-(b/a)u`,
`M=C-a^{-1}uu^T`,

where u,v are the physical pair-to-leaf rows and C is the physical leaf block. The partner proves, for the overlap-two exterior-star currency,

`W2(S)=a^2 sum_(k!=l) (delta M_kl-ell_k ell_l)^2`.                (2.1)

This exact identity is the partner result applied at the essential equation below. No use is made of the partner report's subsequently corrected individual-bank corollary.

### 2.2 Global off-diagonal quarter-Riesz theorem

Completed source:
`yspennstate/math-open-problems@21cf221fb1e8b99c99298fb11a0d5a41a8382aba`,
`proofnet24/QFORM-density/fleet-2026-09-22/fleet01/B01/20260923T054511Z-fleet01-B01-qform-auto11b/REPORT.md`.

For every symmetric matrix S in literal original coordinates, every affine term, and independent cap-one scalar inputs Z_i, if

`F(S)=sum_(k!=l) S_kl^2>0`,

then

`H_1/4(Z^T S Z + affine)
 :=sup_w E|Z^T S Z + affine-w|^(-1/4)
 <= C_off F(S)^(-1/8)`,                                          (2.2)

with

`C_off=5.095453495355205...`.                                    (2.3)

The theorem retains arbitrary diagonal quadratic phases and does not rotate the input law.

### 2.3 Translated scalar-quadratic kernel

Source:
`yspennstate/math-open-problems@e542b1a6ef471b329e4e88a6553e1aacb45acc1a`,
`proofnet24/QFORM-density/interactive/20260922T161801Z-rank-two-fusion/REPORT.md`.

For every probability density f<=1, define

`Psi(s)=1+log(1/|s|)` for `0<|s|<=1`,
`Psi(s)=|s|^(-1/4)` for `|s|>=1`.

Then

`int f(y)|s-y^2|^(-1/2)dy <=8 Psi(s)`.                            (2.4)

The shift of y may be arbitrary, because translation preserves the density cap.

### 2.4 Designated partner fleet04/B01: exact signed-Fejer equivalence

Source:
`yspennstate/math-open-problems@a3693ed6d50e8e4143b2f33bf997c5de2cb52d79`,
`proofnet24/QFORM-density/fleet-2026-09-22/fleet04/B01/20260922T141507Z-b01-qform-fejer-r1/REPORT.md`.

For a probability law mu, with the nonnegative triangular Fejer average

`D_T mu(y)=(1/(2pi)) int_(-T)^T (1-|t|/T)
 Re(e^(-ity) phi_mu(t)) dt`,                                     (2.5)

one has

`||p_mu||_infinity = sup_(T>0,y) D_T mu(y)`                      (2.6)

whenever either side is finite, in the bounded-density sense. Thus every bound below is automatically an averaged-frequency estimate; absolute Fourier L1 control is not asserted.

## 3. Scalar-completed model

After completing only X, all affine terms retained, the full form can be written

`Q=a(X+h(Y,Z))^2+R(Y,Z)`,                                       (3.1)

where X, Y and the leaf bank Z are disjoint literal original-coordinate variables and hence X is independent of (Y,Z). The residual is

`R=delta Y^2+2Y(ell^T Z+beta)+Z^T M Z+q^T Z+d`.                 (3.2)

The constant beta absorbs every scalar affine Y coefficient.

For fixed (Y,Z), the conditional pushforward of X by `a(X+h)^2+R` has density bounded by

`|a|^(-1/2)|t-R|^(-1/2)`.                                      (3.3)

Indeed the two inverse branches each contribute at most `1/(2 sqrt(|a||t-R|))`. Therefore, if

`H_1/2(R)=sup_t E|R-t|^(-1/2)`,                                 (3.4)

then every interval I satisfies

`P(Q in I)<=|I| |a|^(-1/2) H_1/2(R)`,                           (3.5)

and hence

`||p_Q||_infinity<=|a|^(-1/2)H_1/2(R)`                          (3.6)

whenever the right side is finite.

The previous B01 run paid Gamma1=0 by classifying M as diagonal plus an aligned rank-one square, and paid Gamma1>0 by a crossing estimate that deteriorated like Gamma1^(-1/4). The aim here is to remove Gamma1 entirely.

## 4. Complete Y and identify the exact surviving Schur curvature

Assume first `delta!=0`. Complete Y in (3.2):

`R=delta (Y+g(Z))^2+W(Z)`,                                      (4.1)

where g is affine and

`W(Z)=Z^T S Z+r^T Z+d0`,
`S=M-delta^(-1) ell ell^T`.                                    (4.2)

Thus, for each off-diagonal k!=l,

`delta S_kl=delta M_kl-ell_k ell_l`.                            (4.3)

Now apply the designated fleet04/B01 identity (2.1) at this exact equation:

`W2(S_pair)=a^2 delta^2 sum_(k!=l) S_kl^2
           =a^2 delta^2 F(S)`.                                  (4.4)

Therefore, whenever W2>0,

`F(S)=W2/(a^2 delta^2)>0`.                                      (4.5)

This is the key bridge. A tiny nonzero scalar Schur coefficient delta does not make the surviving critical-value curvature small; W2 fixes its exact compensating scale.

## 5. The quarter-Riesz exponent cancels delta exactly

Fix t. Conditional on Z, translate the cap-one law of Y and use (2.4):

`E_Y |R-t|^(-1/2)
 <=8 |delta|^(-1/2)
     Psi((t-W)/delta)`.                                         (5.1)

The special exponent 1/4 is exactly what is needed. For every nonzero s,

`Psi(s)<=c_Psi |s|^(-1/4)`,                                     (5.2)

where the optimal constant for this elementary comparison is

`c_Psi=4 e^(-3/4)=1.8894662109640588...`.                       (5.3)

Proof: for |s|>=1 equality holds with ratio one. For |s|<=1 put `u=log(1/|s|)>=0`. Then

`Psi(s)|s|^(1/4)=(1+u)e^(-u/4)`,

whose derivative vanishes only at u=3, where its maximum is `4e^(-3/4)`.

Average (5.1) over Z and use (5.2):

`E|R-t|^(-1/2)
 <=8 c_Psi |delta|^(-1/2)
    E |(t-W)/delta|^(-1/4)`
`=8 c_Psi |delta|^(-1/4)
    E|W-t|^(-1/4)`.                                             (5.4)

Apply the global quarter-Riesz theorem (2.2) to W:

`H_1/2(R)
 <=8 c_Psi C_off |delta|^(-1/4) F(S)^(-1/8)`.                  (5.5)

Substitute the exact partner identity (4.5):

`F(S)^(-1/8)
 =|a delta|^(1/4) W2^(-1/8)`.                                   (5.6)

The determinant-scale factor cancels exactly:

`boxed:
H_1/2(R)
 <=K_R |a|^(1/4) W2^(-1/8),`                                   (5.7)

with

`K_R=8 c_Psi C_off
    =77.02149767209895... .`                                    (5.8)

No factor involving delta, det(B), sigma_min(B), Gamma1, the support diameter, or a moment of any input remains.

Combining (3.6) and (5.7) proves the main theorem.

## 6. Main theorem — determinant-free W2 receiver

### Theorem `QFORM-SCALARPIVOT-W2-QUARTERRIESZ-v1`

Let Q=X^TAX plus arbitrary affine/constant terms, under independent scalar input densities bounded by one. Choose two literal original coordinates X,Y and assume the first physical diagonal coefficient is `a!=0`. Perform only the scalar completion described in Section 3 and define W2 by the fleet04/B01 overlap-two exterior-star identity (2.1).

If

`delta=c-b^2/a !=0`

and

`W2>0`,

then Q has an essentially bounded density and

`boxed:
||p_Q||_infinity
 <=77.022 |a|^(-1/4) W2^(-1/8).`                                (6.1)

Equivalently, by the fleet04/B01 signed-Fejer theorem,

`boxed:
sup_(T>0,y) D_T law(Q)(y)
 <=77.022 |a|^(-1/4) W2^(-1/8).`                                (6.2)

The theorem allows either sign of delta, either sign/signature of the physical pair, arbitrary dense/high-rank leaf curvature M, arbitrary affine terms, fragmented/unbounded input supports, and arbitrarily small nonzero det(B). No post-rotation independence is used.

At `delta=0`, the previously completed exact-singular arbitrary-curvature random-slope theorem already gives the stronger compatible estimate

`||p_Q||_infinity
 <=4 sqrt(2)e^(1/4)|a|^(-1/4)W2^(-1/8)
 <7.264 |a|^(-1/4)W2^(-1/8)`.                                   (6.3)

Hence for every scalar-pivot pair with `a!=0` and W2>0, both the exact singular and every nonzero near-singular state are now paid with the same scale `|a|^(-1/4)W2^(-1/8)`, with no interpolation gap as delta tends to zero.

### Scaling check

Under A -> sA,

`a -> s a`,
`W2 -> s^6 W2`.

Thus the right side of (6.1) scales as

`|s|^(-1/4) |s|^(-6/8)=|s|^(-1)`,

exactly the scale of an output density.

## 7. Phase-aligned scalar counterexample remains valid

Fix any prescribed frequency s>0 and any `0<eta<pi/2`. The set

`E={x: dist(s x^2,2pi Z)<=eta}`

has infinite Lebesgue measure. Choose a finite measurable union `E0 subset E` of total measure one and let `f=1_E0`. Then f is an admissible probability density with f<=1 and

`Re int exp(i s x^2) f(x)dx >=cos eta`.                          (7.1)

Therefore no law-uniform pointwise estimate `|E exp(isX^2)|<=C|s|^-alpha`, alpha>0, can hold. Theorem 6.1 does not contradict this: it uses a global quarter-Riesz estimate for the exact critical-value quadratic form and then the signed-Fejer/density interface. Its mechanism is averaged/distributional, not scalar pointwise van der Corput.

## 8. Small-positive Gamma1 interpolation gap is closed

The preceding B01 run defined

`Gamma1=max_i ||ell_(J_i)|| ||M[i,J_i](I-P_(ell_(J_i)))||`

and had two separate estimates:

* exact `Gamma1=0`: an aligned-rank-one theorem with constant about 101.462 at nonzero delta;
* `Gamma1>0`: a crossing theorem `8|a|^(-1/2)Gamma1^(-1/4)`, which diverges as Gamma1->0+.

Theorem 6.1 is independent of Gamma1. Thus, throughout the partner leakage state W2>0 and delta!=0,

`||p_Q||_infinity
 <=min{8|a|^(-1/2)Gamma1^(-1/4),
       77.022|a|^(-1/4)W2^(-1/8)}`                              (8.1)

whenever Gamma1>0, while the second term remains valid at Gamma1=0 as well. There is no longer any analytic discontinuity at Gamma1=0.

This also strictly improves the previous aligned nonzero-delta constant 101.462 and removes its structural hypothesis `M=D+tau ell ell^T`.

## 9. Concrete target-valid stress family

Take three leaf coordinates and parameters

`delta=10^(-2)`, `epsilon=10^(-8)`,

with physical matrix

`A=
[[1,0,0,0,0],
 [0,delta,1,1,0],
 [0,1,0,0,epsilon],
 [0,1,0,0,0],
 [0,0,epsilon,0,0]].`                                           (9.1)

Here `a=1`, `b=0`,

`ell=(1,1,0)`,

and the leaf residual has only `M_13=M_31=epsilon` off the diagonal. Directly,

`Gamma1=epsilon=10^(-8)`,                                      (9.2)

while the partner identity gives

`W2=2(1+delta^2 epsilon^2)=2+2*10^(-20)`.                       (9.3)

The eigenvalues are approximately

`-1.4092402, -0.0000000071, +0.0000000071, 1, 1.4192400`

at epsilon=10^(-8) to displayed precision in the tiny pair, so at least three eigenvalues have modulus >=1 (the exact eigenvalue 1 plus the two roots continuously perturbing the ±sqrt(2) pair). The committed checker uses direct double-precision eigensolving and verifies the three-large-eigenvalue condition.

The previous positive-Gamma1 receiver gives

`8 Gamma1^(-1/4)=800`,                                         (9.4)

whereas Theorem 6.1 gives

`77.0214976721 * W2^(-1/8)
 <70.629025`.                                                    (9.5)

As epsilon->0+ with delta fixed, the old crossing estimate diverges while (9.5) remains unchanged. This is exactly the interpolation defect the present theorem removes. The tiny nonzero M entry is retained throughout; it is never discarded as a small random error.

## 10. Continuity and remaining implication

The theorem proves absolute continuity and an essential L-infinity bound by the linear interval estimate (3.5). It does **not** prove that the density is continuous. The quarter-Riesz and correlated outer-square argument do not produce an absolute-L1 Fourier majorant or a local-uniform Fejer limit.

The first B01 debt is no longer `small-positive Gamma1 interpolation`. It is now upstream/structural:

`QFORM-SCALARPIVOT-W2-OR-OTHER-EXIT-v1`:

> Starting from the bare three-large-eigenvalue hypothesis, force either (i) a literal scalar-pivot pair with `a` and W2 quantitatively large enough for (6.1), (ii) one of the already-paid definite pair / fixed-pair aggregate-three-volume / three-hub / projected-crossing / ridge / grouped-square / diffuse-window branches, or (iii) classify the W2=0 and zero-diagonal physical-pair endpoints without asserting a uniformly good fixed minor.

The theorem here removes determinant and near-singular conditioning from branch (i); the remaining problem is selecting or aggregating the branch at universal scale.

## 11. Status

New proved result: `QFORM-SCALARPIVOT-W2-QUARTERRIESZ-v1`.

It applies the designated fleet04/B01 W2 identity at the exact Schur equation and the designated fleet04/B01 signed-Fejer theorem to the final inequality. The full unrestricted QFORM conjecture remains OPEN. Independent end-to-end review of this new compiler has not yet occurred.

Brain status remains `WITHOUT_VERIFIED_BRAIN`: repository source retrieval and writeback are genuine; authenticated native receiver-memory ingestion was not established.
