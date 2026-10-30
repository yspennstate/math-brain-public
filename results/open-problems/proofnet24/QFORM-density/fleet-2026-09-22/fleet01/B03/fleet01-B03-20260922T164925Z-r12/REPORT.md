# B03 report: fractional ridge potentials and a conditional-projection falsifier

Run: `fleet01-B03-20260922T164925Z-r12`  
Programme: `QFORM-DENSITY-3EIG-20260922`  
Assignment: `Decoupled time integral`  
Status: **ESSENTIAL_STEP_APPLIED / FULL TARGET OPEN**  
Execution context: `WITHOUT_VERIFIED_BRAIN`

## 1. Exact target and source pins

The target remains: for every dimension, independent real coordinates `X_i` with probability densities `0<=f_i<=1`, and every real symmetric `A` with at least three eigenvalues of absolute value at least one, prove that `Q=X^T A X` has a universally bounded density, or give a valid counterexample. No moment, compact-support, connected-support, log-concavity, Gaussianity, or independence after spectral rotation is assumed.


The main analytic dependency is the ridge characteristic-function theorem in

- `yspennstate/math-open-problems@9c1167db05c7b0f520f060796fde921ed769a4e7`, `proofnet24/QFORM-density/interactive/20260922T151048Z-ridge-window/REPORT.md`.


The named partner result actually used below is fleet02/B03:

- `yspennstate/math-open-problems@33cd6fae4e8adb85cf1ee43a244f628e563f1cbf`, `proofnet24/QFORM-density/fleet-2026-09-22/fleet02/B03/20260922T161346Z-fleet02-B03-QFORM-r12/REPORT.md`.

That partner proves a translation-uniform two-variable indefinite small-ball bound and, in particular, the half-Riesz estimate

`sup_z E |z-q(X,Y)|^(-1/2) <= 16 sqrt(2) Delta^(-1/4)`

for independent cap-one variables and an indefinite binary quadratic whose discriminant is `Delta=b^2-ac>0`.

Corrections used include the false pointwise Fresnel decay, the false conditional sum/difference cap, the false fixed rank-three-cut/local-minor dichotomies, the false one-triple aggregate determinant payment, and the fiber-sup dimension-loss warning. No refuted premise is used below.

## 2. Conditional end-to-end route and first missing implication

A physical scalar pivot gives the exact form

`Q = d (Z+H(W))^2 + R(W)`,

where `d!=0`, `Z` is one original coordinate with density cap one, and `W` consists of the other original independent coordinates. Conditional on `W`, the density of the square obeys

`p_{Q|W}(y) <= |d|^(-1/2) |y-R(W)|^(-1/2)`.

Therefore

`||p_Q||_infinity <= |d|^(-1/2) sup_y E |y-R|^(-1/2)`.             (2.1)

Thus the first analytic obligation in any pivot branch is not an `L^1` characteristic function bound for `R`; it is a **half-Riesz potential bound**. The ridge Fourier theorem already gives a frequency envelope below the direct density threshold. The first purpose of this run is to integrate that envelope against the exact Riesz multiplier, without conditioning a sum/difference variable and without losing the dependence within an independent-copy pair.

## 3. Fractional ridge-potential theorem

Let `R` be an arbitrary quadratic form in independent original coordinates with densities bounded by one. Let `I,J` be disjoint original-coordinate sets and put `B=A_R[I,J]`. For `gamma>0`, define

`K = B B^T (gamma^2 I + B B^T)^(-1)`,

`theta = tr K`,

`D = det(I + B B^T/gamma^2)`.

Let `1<=q<=2` and assume

`max_i K_ii <= q/2`.                                               (3.1)

For `0<s<1`, assume further

`theta > 2 q s`.                                                   (3.2)

Then

`sup_z E |z-R|^(-s)`

` <= [2 Gamma(1-s) sin(pi s/2)/(pi s)]`

`    * [theta/(theta-2 q s)]`

`    * [L_q/(2 gamma)]^s D^(-s/(2 theta)),`                        (3.3)

where

`L_q = pi e sqrt(2/q)`.

This is uniform in all same-side quadratic terms, linear terms, and outside couplings that are retained by the ridge theorem.

### Proof

The cited ridge theorem gives, under (3.1),

`|phi_R(t)| <= min(1,(t0/|t|)^beta)`,                              (3.4)

where

`beta = theta/(2q)`,

`t0 = [L_q/(2 gamma)] D^(-1/(2 theta))`.                           (3.5)

The proof of (3.4) is the dependence-safe independent-copy/graph argument: one first obtains an estimate for `|phi|^(2q)` by Cauchy-Schwarz and an independent copy, then applies the regularized Brascamp-Lieb/Hausdorff-Young estimate to the original-coordinate cross block. No conditional density cap for a conjugate sum/difference is used.

For `0<s<1`, in the Fourier convention `hat h(t)=int exp(i t x) h(x) dx`,

`hat{|x|^(-s)}(t) = 2 Gamma(1-s) sin(pi s/2) |t|^(s-1)`.          (3.6)

To avoid any unproved regularity of the law of `R`, convolve it with a centered Gaussian of variance `epsilon`; apply Fourier inversion to the smoothed finite Riesz potential; the additional factor `exp(-epsilon t^2/2)` is at most one. Then let `epsilon` decrease to zero. Lower semicontinuity of `|z-x|^(-s)` and Portmanteau/Fatou give the same upper bound for the original law.

Consequently

`E |z-R|^(-s)`

` <= [Gamma(1-s) sin(pi s/2)/pi]`

`    * int_R |t|^(s-1) |phi_R(t)| dt`.                            (3.7)

By (3.4), and because `beta>s` is exactly (3.2),

`int_R |t|^(s-1) min(1,(t0/|t|)^beta) dt`

` = 2 t0^s [1/s + 1/(beta-s)]`

` = 2 t0^s beta/[s(beta-s)]`

` = (2/s) t0^s theta/(theta-2qs)`.                               (3.8)

Substituting (3.5) into (3.7)-(3.8) proves (3.3). QED.

### Half-Riesz specialization

For `s=1/2`, the threshold becomes only

`theta > q`,                                                        (3.9)

and (3.3) simplifies exactly to

`sup_z E |z-R|^(-1/2)`

` <= 2^(5/4) sqrt(e) q^(-1/4) gamma^(-1/2)`

`    * [theta/(theta-q)] D^(-1/(4 theta)).`                        (3.10)

Since `log D >= theta`, one also has the coarser determinant-free estimate

`sup_z E |z-R|^(-1/2)`

` <= 2^(5/4) e^(1/4) q^(-1/4) gamma^(-1/2) theta/(theta-q)`.       (3.11)

This directly lowers the ridge effective-dimension threshold from `theta>2q` for density by direct Fourier inversion to `theta>q` when one independent physical square remains available.

## 4. Pivot plus ridge: linear small-ball scaling

Combining (2.1) and (3.10) yields the following complete scoped theorem.

Suppose an original physical coordinate gives

`Q=d(Z+H(W))^2+R(W)`, `d!=0`,

and some original-coordinate cross block of the Schur remainder `R` satisfies (3.1) and `theta>q`. Then `Q` has an essentially bounded density and

`||p_Q||_infinity`

` <= 2^(5/4) sqrt(e) q^(-1/4) |d|^(-1/2) gamma^(-1/2)`

`    * [theta/(theta-q)] D^(-1/(4 theta)).`                        (4.1)

Thus the associated interval small-ball estimate is linear:

`P(Q in I) <= ||p_Q||_infinity |I|`.                               (4.2)

The theorem does **not** assert continuity. Direct ridge inversion with `theta>2q` gives a continuous `C_0` density, but the square-potential transducer only proves absolute continuity/essential boundedness in the intermediate range `q<theta<=2q`.

### Exact-rank limit

If `B` has exact rank `r`, nonzero singular-value product

`Delta_r(B)=prod_{j=1}^r sigma_j(B)`,

and the orthogonal range projection satisfies `max_i P_ii<=q/2`, then letting `gamma` decrease to zero in (3.10) gives, for `r>q`,

`sup_z E |z-R|^(-1/2)`

` <= 2^(5/4) sqrt(e) q^(-1/4) [r/(r-q)] Delta_r(B)^(-1/(2r)).`     (4.3)

For `r=2,q=1`, the numerical constant in front of `Delta_2^(-1/4)` is

`2^(9/4) sqrt(e) = 7.842684263091678...`.

This exact-rank limit is mainly a consistency check; the new content is the regularized effective-dimension regime `q<theta<2q`.

## 5. Named-partner application: singleton plus two banks

Consider the correction family

`A_m = [1] direct_sum J_m/m direct_sum (-J_m/m)`,                  (5.1)

whose nonzero spectrum is exactly `{1,1,-1}`. This family has no rank-three original-coordinate cross cut, so it is a mandatory control for any proposed global structural reduction.

Pivot the singleton coordinate, so `d=1`. For `m>=3`, split each of the positive and negative banks into a left set of size

`a=ceil(m/2)`

and a right set of size

`b=floor(m/2)`.

The Schur-remainder cross block between the two left pieces and the two right pieces has exactly two singular values

`sigma_m = sqrt(a b)/m`.                                           (5.2)

Set

`gamma=sigma_m/sqrt(3)`, `q=1`.

Then the two nonzero ridge eigenvalues are `3/4`, hence

`theta=3/2`, `D=16`,

and each left coordinate has ridge leverage `(3/4)/a<=3/8<1/2`. Thus (4.1) applies and gives

`||p_Q||_infinity <= 9.75325637240399... sigma_m^(-1/2)`.          (5.3)

For `m>=3`, `sigma_m>=sqrt(2)/3`, so

`||p_Q||_infinity < 14.206`.                                      (5.4)

This already covers all `m>=3` by the new fractional ridge integral.

For `m=2`, the balanced 1+1 cut has two equal cross singular values but any ridge parameter satisfying the row cap has `theta<=1`, so the strict half-Riesz ridge threshold cannot hold. Here the named partner fleet02/B03 theorem supplies the endpoint.

Let the two independent bank sums, normalized to unit coefficient, be

`Y=(X_1+X_2)/sqrt(2)`, `Z=(X_3+X_4)/sqrt(2)`.

Young's inequality gives density caps `||p_Y||_infinity,||p_Z||_infinity<=sqrt(2)`. Rescaling the partner's cap-one indefinite-binary theorem therefore yields

`sup_t E |t-(Y^2-Z^2)|^(-1/2)`

` <= 16 sqrt(2) (sqrt(2)*sqrt(2))^(1/2) = 32`.                   (5.5)

The singleton physical square then gives

`||p_Q||_infinity <=32`.                                          (5.6)

For `m=1`, (5.1) is diagonal and the known diagonal theorem gives `||p_Q||_infinity<=pi`.

Hence the new ridge half-Riesz mechanism plus the named fleet02/B03 endpoint theorem gives a uniform bound

`||p_{Q_m}||_infinity <=32`                                       (5.7)

for every member of this hard family. This is not a proof of the full conjecture, but it shows that the `theta>q` pivot-ridge threshold genuinely reaches a structural family that defeats fixed rank-three cross-cut arguments.

## 6. Source-valid falsifier to the new conditional rank-three projection shortcut


Take `n=4` and let `X_1,...,X_4` be independent `Uniform[0,1]`. Put

`v=(1,1,1,1)/2`,

and extend `v` to an orthonormal basis so that an orthogonal map sends

`X -> (Y_1,Y_2,Y_3,Z)`, with `Z=v dot X=(X_1+X_2+X_3+X_4)/2`.

The joint density in `(Y,Z)` coordinates is the indicator of a rotated unit cube. For `0<z<1/2`, the slice `Z=z` is

`x_i>=0`, `sum_i x_i=2z`;                                         (6.1)

the upper constraints `x_i<=1` are automatic. The Euclidean three-volume of this simplex slice is

`V(z)=(2z)^3/3 = 8 z^3/3`.                                       (6.2)

One way to check the constant is coarea: for `S=sum_i X_i`, the Irwin-Hall density on `0<s<1` is `s^3/6`; because `||grad S||=2`, the hyperplane area is `2(s^3/6)=s^3/3`. Setting `s=2z` gives (6.2).

Conditional on `Z=z`, `Y` is uniform on the slice, hence

`||rho_{Y|Z=z}||_infinity = 1/V(z) = 3/(8 z^3) -> infinity`        (6.3)

as `z` decreases to zero.

To place this exactly inside the target, take the same orthogonal matrix `O` and set

`A=O^T diag(1,1,-1,0) O`.                                        (6.4)

Then `A` has exactly three eigenvalues of modulus one, and `(Y_1,Y_2,Y_3)` are precisely the three large spectral coordinates. Thus there is **no universal conditional three-dimensional projection density cap** after conditioning on the remaining spectral coordinate.

This does **not** refute QFORM and does not refute a correctly weighted rank-three coarea argument. Indeed here

`p_Z(z) ||rho_{Y|Z=z}||_infinity = 1`                             (6.5)

on the small-z slices. What fails is taking a uniform conditional supremum before averaging. More generally

`p_Z(z)||rho_{Y|Z=z}||_infinity = sup_y g(y,z)`,                  (6.6)

where `g` is the joint rotated density. Integrating (6.6) over `z` is exactly a fiber-sup quantity; the already recorded cube-projection correction shows that such quantities can grow with dimension. Therefore a successful spectral coarea proof must keep the conditioning weight and product geometry inside the same integral, rather than inserting a law-uniform conditional density cap.

This is a genuine source-valid falsifier of an **intermediate route only**, not of the original conjecture.

## 7. Relation to the independent-copy assignment

The fractional theorem is precisely an integrated independent-copy estimate. The ridge envelope (3.4) comes from the safe independent-copy identity behind `|phi(t)|^(2q)`, while (3.7)-(3.8) integrates that envelope against the Riesz multiplier required by the remaining physical square. It never conditions a difference on its conjugate sum, so the fleet02/B03 `QFORM-UV-CONDITIONAL-CAP-FALSE` correction is respected.

At `s=1/2`, the frequency weight is `|t|^(-1/2)`. This is why the required effective dimension is `theta>q`, exactly half the direct Fourier-inversion threshold `theta>2q`: the independent physical square contributes the missing half derivative through its `|x|^(-1/2)` kernel.

## 8. What remains unpaid

The full conjecture is still open. The first unpaid implication is now structural, not the time integral itself:

> Starting only from “A has at least three eigenvalues of modulus at least one,” force a dimension-free, original-coordinate, product-preserving alternative in which either (i) direct ridge inversion has `theta>2q`, (ii) a genuine physical square remains and a Schur-remainder ridge block has `theta>q`, or (iii) a completed grouped-bank/light-cone mechanism applies, with all determinant/pivot factors paid uniformly.

Known singleton-plus-two-banks and local-minor corrections rule out a fixed good-minor or rank-three-cross-cut dichotomy. The fresh conditional-projection example above also rules out replacing this structural synthesis by a uniform conditional spectral-density cap.

A promising next use of (3.3) is to allow other fractional exponents `s` when a grouped coordinate mechanism contributes a kernel `|x|^{-s}` different from one half. The exact threshold `theta>2qs` gives a continuum of effective-dimension payments that may mesh with the ridge/diffuse and grouped-bank branches.

## 9. Claim status

- `ESSENTIAL_STEP_APPLIED`: yes. A new all-`s` fractional ridge-potential theorem is proved, its half-Riesz specialization yields linear small-ball scaling after a physical square, and it is applied to a hard rank-three-spectrum family.
- `CANDIDATE_REFUTED`: the proposed universal conditional 3-D spectral projection density cap is refuted by the rotated-cube slice construction. The QFORM target is not refuted.
- Full QFORM: **OPEN**.
- Continuous density for the full target: **OPEN**. The new pivot-plus-fractional-ridge branch proves essential boundedness/absolute continuity, not continuity in the intermediate `q<theta<=2q` regime.
