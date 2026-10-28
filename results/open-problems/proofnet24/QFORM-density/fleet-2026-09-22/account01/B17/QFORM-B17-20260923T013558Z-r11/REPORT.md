# QFORM B17 — positive-heavy K0/sinc no-escape theorem

Run: `QFORM-B17-20260923T013558Z-r11`

Status: `SUPPORTING_SHARP-WITNESS_THEOREM / FULL_QFORM_OPEN / CONTINUITY_SEPARATE / WITHOUT_VERIFIED_BRAIN`.

The full arbitrary-matrix quadratic-form conjecture is **not proved** here. This report proves a new sharp-witness exclusion for a source-valid rank-three family in which an arbitrary finite collinear physical bank occupies one positive spectral direction and the other positive and negative directions are diffuse. The key point is a Gaussian comparison for a K0 functional that is valid whenever every leverage square is at most `4/9`.

## 1. Statement

Let `a=(a_1,...,a_r)` be finite with

`sum_i a_i^2=1`, `max_i a_i^2 <= 4/9`.                              (1.1)

Let `X_i` be independent real random variables with densities bounded by one, and let `G_+,G_-` be independent `N(0,1/12)`, independent of the `X_i`. Put

`S=sum_i a_i X_i`,
`Q_infty=S^2+G_+^2-G_-^2`.                                          (1.2)

Then the central density obeys

`p_Qinfty(0) < 3 sqrt(2)`.                                          (1.3)

More precisely, among all cap-one laws of the `X_i`, the left side is maximized by iid centered unit intervals `U_i~Unif[-1/2,1/2]`, and for those intervals it is strictly below `3sqrt(2)` for every fixed finite vector `a` satisfying (1.1).

If the `X_i` are centered unit intervals, then the completed account02/B17 symmetric-unimodal theorem applies and upgrades (1.3) to the global statement

`||p_Qinfty||_infinity=p_Qinfty(0)<3sqrt(2)`.                        (1.4)

There is also an exact finite original-coordinate target family converging locally to (1.2). In that family the partner theorem puts the density maximum at zero for every finite bank size, and therefore every fixed `a` satisfying (1.1) has

`lim_m ||p_Qm||_infinity = ||p_Qinfty||_infinity < 3sqrt(2)`.        (1.5)

Thus no fixed finite positive-direction collinear leverage pattern with `max a_i^2<=4/9` can beat the known `3sqrt(2)` obstruction by coupling it to two diffuse opposite-sign banks.

## 2. Exact central-density kernel and extremization over cap-one laws

Standardize the diffuse Gaussians. Let

`H=sqrt(12) S`, `Z_+,Z_- iid N(0,1)`.

Then `12 Q_infty = H^2+Z_+^2-Z_-^2`. The difference `Z_+^2-Z_-^2` has density

`d(t)=(1/(2pi)) K_0(|t|/2)`,                                       (2.1)

where `K_0` is the modified Bessel function. Hence

`p_Qinfty(0)=(6/pi) E K_0(6 S^2)`.                                 (2.2)

The kernel `k(x)=K_0(6x^2)` is even and strictly decreasing in `|x|` away from zero, with only an integrable logarithmic singularity at zero.

For independent cap-one densities `f_i`, one-dimensional Brascamp--Lieb--Luttinger/Riesz rearrangement, followed by coordinatewise bathtub, gives

`E k(sum_i a_i X_i) <= E k(sum_i a_i U_i)`,                         (2.3)

where the `U_i` are iid `Unif[-1/2,1/2]`. To justify the logarithmic singularity, first replace `k` by `min(k,M)`, apply rearrangement, and let `M` increase to infinity by monotone convergence. Signs of the `a_i` are absorbed by reflecting the corresponding input. After symmetric decreasing rearrangement, fixing all but one coordinate leaves an even decreasing convolution kernel in the remaining coordinate; among probability densities bounded by one, bathtub fills the centered interval of length one. Iterating proves (2.3).

Consequently it suffices to bound the centered-interval functional.

## 3. Exact Gaussian Laplace comparison at leverage `4/9`

Let

`V_i=sqrt(12) U_i ~ Unif[-sqrt(3),sqrt(3)]`,
`T_a=sum_i a_i V_i`.

Then `Var(T_a)=1`. Define

`L_a(c)=E exp(-c T_a^2)`, `c>=1/2`.                                 (3.1)

### Lemma `QFORM-POSITIVE-COLLINEAR-LAPLACE-4/9-v1`

Under (1.1),

`L_a(c) <= (1+2c)^(-1/2)` for every `c>=1/2`.                       (3.2)

For each fixed finite nonzero `a`, the inequality is strict for every `c>=1/2`.

### Proof

The characteristic function of `T_a` is

`phi_a(t)=product_i sinc(sqrt(3) a_i t)`,

with `sinc x=sin(x)/x`. Fourier inversion for the Gaussian kernel, followed by `x=sqrt(3)t`, gives

`L_a(c)=1/[2 sqrt(3 pi c)]
        * integral_R exp[-x^2/(12c)] product_i sinc(a_i x) dx`.      (3.3)

Set

`K=1+1/(2c)`,
`q_0=K/(K-1)=2c+1`,
`q_i=K/a_i^2` for `a_i!=0`.                                        (3.4)

Then

`1/q_0 + sum_i 1/q_i = 1`.                                         (3.5)

Because `c>=1/2`, `1<K<=2`; because `a_i^2<=4/9`, `q_i>=9/4`.

Use the sharp finite-p sinc estimate from Koenig--Koldobsky, Proposition 7, in the normalization already checked in the preceding B17 proof:

`I(p):=integral_R |sinc u|^p du <= sqrt(6pi/p), p>=9/4`,             (3.6)

with strict inequality for every finite `p>=9/4`.

Holder with the exponents in (3.4) gives

`||exp[-x^2/(12c)]||_(q_0)
   = (12pi c/q_0)^(1/(2q_0))`,                                     (3.7)

and

`||sinc(a_i x)||_(q_i)
 <= |a_i|^(-1/q_i) (6pi/q_i)^(1/(2q_i))
 = (6pi/K)^(1/(2q_i)).`                                            (3.8)

The last equality is the exact cancellation `q_i=K/a_i^2`. Also, since `c=1/[2(K-1)]` and `q_0=K/(K-1)`,

`12pi c/q_0 = 6pi/K`.                                              (3.9)

Using (3.5), all Holder factors therefore collapse to

`integral_R exp[-x^2/(12c)] product_i |sinc(a_i x)| dx
 <= sqrt(6pi/K)`.                                                   (3.10)

Substitution into (3.3) yields

`L_a(c) <= sqrt(6pi/K)/[2sqrt(3pi c)]
        = 1/sqrt(2cK)
        = 1/sqrt(1+2c)`,                                           (3.11)

which is (3.2). For finite `a`, at least one nonzero sinc exponent is finite, and (3.6) is strict, so (3.11) is strict. QED.

The number `4/9` is exact for this argument: it is the leverage threshold that guarantees `K/a_i^2>=9/4` all the way to the large-`c` endpoint `K downarrow 1`.

## 4. K0 integration gives the `3sqrt(2)` ceiling

For `z>0`,

`K_0(z)=integral_0^infinity exp[-z cosh u] du`.                     (4.1)

Therefore Tonelli and (3.2), with `c(u)=cosh(u)/2>=1/2`, give

`E K_0(T_a^2/2)
 = integral_0^infinity L_a(cosh(u)/2) du
 <= integral_0^infinity [1+cosh u]^(-1/2) du`.                      (4.2)

Since `1+cosh u = 2 cosh^2(u/2)`,

`integral_0^infinity [1+cosh u]^(-1/2) du
 = sqrt(2) integral_0^infinity sech v dv
 = pi/sqrt(2)`.                                                     (4.3)

The strictness from Section 3 holds for every `u`, hence

`E K_0(T_a^2/2) < pi/sqrt(2)`                                      (4.4)

for every fixed finite `a` satisfying (1.1).

Returning to physical scale and combining (2.2)--(2.3),

`p_Qinfty(0)
 <= (6/pi) E K_0(6(sum a_i U_i)^2)
 = (6/pi) E K_0(T_a^2/2)
 < (6/pi)*(pi/sqrt(2))
 = 3sqrt(2)`.                                                       (4.5)

This proves the central theorem, including arbitrary cap-one heavy laws.

## 5. Completed partner theorem applied to the global norm

The designated completed partner source is account02/B17:

`yspennstate/math-open-problems@84ffc0f291ae192f4d82742ae6909943f6710bc7`

`proofnet24/QFORM-density/fleet-2026-09-22/account02/B17/B17-20260922T235536Z-r12-symmetric-unimodal/REPORT.md`.

It proves that whenever independent `Y_1,Y_2,Y_3` have even densities nonincreasing on `[0,infinity)`, every

`alpha Y_1^2 + beta Y_2^2 - gamma Y_3^2`, `alpha,beta,gamma>0`,

has its global density maximum at zero.

Apply it here with centered unit intervals in the heavy bank. A finite convolution of centered interval densities is even and decreasing on the positive half-line, and the Gaussian densities are also even decreasing. Hence the partner theorem gives the actual inequality

`||p_Qinfty||_infinity = p_Qinfty(0) < 3sqrt(2)`.                   (5.1)

The partner theorem is essential here: (4.5) alone controls only the central output and does not rule out an off-zero spike.

## 6. Exact finite original-coordinate stress family

Fix `a` satisfying (1.1). For every integer `m`, take disjoint physical banks of iid `Unif[-1/2,1/2]` variables and define

`Y_1=sum_{i=1}^r a_i U_{1i}`,
`Y_{2,m}=m^(-1/2) sum_{k=1}^m U_{2k}`,
`Y_{3,m}=m^(-1/2) sum_{k=1}^m U_{3k}`.                              (6.1)

Let `R_m` have physical-to-spectral rows `a_i e_1` in the first bank, `m^(-1/2)e_2` in the second bank, and `m^(-1/2)e_3` in the third bank. Then exactly

`R_m^T R_m=I_3`,                                                    (6.2)

so

`A_m=R_m diag(1,1,-1) R_m^T`                                      (6.3)

has nonzero spectrum **exactly** `{1,1,-1}` for every finite `m`. Every physical input density is exactly one. Thus this is a genuine target family and not a post-rotation independence surrogate.

Each aggregate in (6.1) has an even decreasing density. The completed account02/B17 theorem therefore gives, for every finite `m`,

`||p_Qm||_infinity=p_Qm(0)`,
`Q_m=Y_1^2+Y_{2,m}^2-Y_{3,m}^2`.                                  (6.4)

The standard fixed-parameter local CLT for the two explicit normalized uniform banks, with the logarithmic square-difference singularity handled by the same BV/local-limit envelope already proved in the preceding B17 finite-bank transfer, yields

`p_Qm(0) -> p_Qinfty(0)`.                                          (6.5)

Equivalently, one can dominate the square-difference kernel by `C(1+log_+(1/|y|))`: the normalized uniform-bank densities are symmetric log-concave with a uniform one-dimensional local-CLT envelope, while the fixed heavy aggregate `Y_1` has a bounded density; the logarithm is integrable. Hence dominated convergence applies.

Combining (4.5), (6.4), and (6.5),

`lim_m ||p_Qm||_infinity = p_Qinfty(0) < 3sqrt(2)`.                 (6.6)

In particular, for every fixed leverage vector satisfying (1.1), all sufficiently large exact finite target matrices in this family have a strict global gap below `3sqrt(2)`.

## 7. Relation to the known lower bound and remaining witness frontier

The live QFORM correction state already supplies the source-valid universal lower obstruction

`C_univ >= 3sqrt(2)`                                                (7.1)

from three diffuse uniform banks converging to the Gaussian signature `(1,1,-1)` limit. Sections 1--6 show that a broad finite-fragment positive-direction perturbation cannot improve it: even arbitrary cap-one laws cannot raise the *central* Gaussian-completion peak, and centered interval laws cannot raise the *global* peak.

This complements the previous B17 results: fixed periodic diffuse frames approach `3sqrt(2)` from below; one macroscopic shared row does not escape centrally; equal-leverage two-heavy rotations are globally below `3sqrt(2)` at every angle; the entire minority-sign collinear branch is at most `3sqrt(2)` and is near-sharp only in the Lindeberg limit; and the present theorem treats an arbitrary finite positive-sign collinear bank whenever `max a_i^2<=4/9`.

The full conjecture is still open. A sharper witness, if one exists, must leave at least one of these protections: e.g. unequal non-collinear shared-coordinate heavy rows, a positive-direction bank with leverage above the present `4/9` threshold outside the already solved equal-pair cases, coupled spectral tails, finite/mesoscopic non-Gaussian residual structure, or a fragmented asymmetric law producing an off-zero peak.

## 8. Corrections and provenance


No refuted law-uniform pointwise oscillatory-decay estimate, arbitrary-joint coarea bound, post-rotation independence, conditional-cap/moment bound, fiber-supremum reduction, finite-fragment-count reduction, single-minor extraction, or cross-rank-three dichotomy is used.

External analytic input: H. Koenig and A. Koldobsky, Proposition 7 in the sinc-integral work cited and normalized in the preceding B17 report, giving (3.6) for `p>=9/4`. The completed partner theorem was read from its immutable source before use.
