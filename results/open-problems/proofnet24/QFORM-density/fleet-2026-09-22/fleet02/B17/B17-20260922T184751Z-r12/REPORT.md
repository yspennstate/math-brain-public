# fleet02/B17 — two-coordinate macroscopic no-escape barrier on the same-sign plane

**Programme:** `QFORM-DENSITY-3EIG-20260922`  
**Run:** `B17-20260922T184751Z-r12`  
**Assignment:** Sharp constant and witnesses  
**Status:** `SUBSTANTIVE_SUPPORTING_LEMMA / FULL_CONJECTURE_OPEN`  
**Execution:** `WITHOUT_VERIFIED_BRAIN`

## 1. Target and source pins

The full target remains open: for arbitrary independent real inputs with one-dimensional densities at most one and every real symmetric matrix with at least three eigenvalues of absolute value at least one, prove a universal dimension-free bound on the density of `X^T A X`, or give a valid counterexample.


The designated completed partner result actually used is fleet03/B17:

- complete mathematics `yspennstate/math-open-problems@0fe842ad60b590ca774ecfd71cf2bb9d15639f90`, path `proofnet24/QFORM-density/fleet-2026-09-22/fleet03/B17/20260922T180732Z-fleet03-B17-QFORM-r14/REPORT.md`.

That result proves (i) an exact six-variable rotated witness with zero peak `4.0630706168060372601...`, still below `3 sqrt(2)`, and (ii) that arbitrary one-coordinate fragmentation cannot improve the earlier six-variable cross witness when the other five laws remain centered intervals. I use (ii) to move to the first unexcluded coordinated two-law macroscopic deformation, rather than repeat a one-coordinate fragment search.

## 2. Exact finite source-valid stress family

Fix leverages `ell_1, ell_2 in [0,1]`. In spectral coordinates let `e_1,e_2,e_3` be the standard basis. For each positive integer `m`, construct a physical-row frame `R_m` as follows:

- one heavy row `sqrt(ell_1) e_1`;
- one heavy row `sqrt(ell_2) e_2`;
- `m` rows `sqrt((1-ell_1)/m) e_1`;
- `m` rows `sqrt((1-ell_2)/m) e_2`;
- `m` rows `m^{-1/2} e_3`.

Then exactly

`R_m^T R_m = I_3`.

With `M=diag(1,1,-1)` define

`A_m = R_m M R_m^T`.

Because `R_m` has orthonormal columns, every `A_m` has exact nonzero spectrum

`{1,1,-1}`.

Thus these are genuine finite target matrices, with no approximate spectral normalization.

Take the two heavy physical variables `X_1,X_2` independent with arbitrary probability densities bounded by one. Take every diffuse-bank variable independently `Unif[-1/2,1/2]`, independent also of the heavy variables. Writing

`S_{j,m}=m^{-1/2} sum_{k=1}^m U_{j,k}`,

the target quadratic form is exactly

`Q_m = Y_{1,m}^2+Y_{2,m}^2-Y_{3,m}^2`,

where

`Y_{1,m}=sqrt(ell_1) X_1 + sqrt(1-ell_1) S_{1,m}`,

`Y_{2,m}=sqrt(ell_2) X_2 + sqrt(1-ell_2) S_{2,m}`,

`Y_{3,m}=S_{3,m}`.

The three displayed spectral coordinates are independent because their physical coordinate banks are disjoint.

By the ordinary CLT,

`sqrt(12) S_{j,m} => G_j`,

where the `G_j` are independent standard Gaussians. Hence

`12 Q_m => R := H_1^2+H_2^2-G_3^2`,

with

`H_i=sqrt(12 ell_i) X_i+sqrt(1-ell_i) G_i`.

This is the two-macroscopic-coordinate Gaussian-completion limit of an exact finite product-source family.

## 3. A sharp square-Laplace comparison for one cap-one heavy coordinate

### Lemma
For every real random variable `X` with density at most one, every independent standard Gaussian `G`, every `ell in [0,1]`, and

`H=sqrt(12 ell) X+sqrt(1-ell)G`,

one has for every `t>=0`

`E exp(-t H^2) <= (1+2t)^(-1/2)`.

If `ell>0` and `t>0`, the final comparison is strict.

### Proof
Condition on `X=x`. Gaussian integration gives

`E_G exp(-t H^2)`

`= d^(-1/2) exp(-c x^2)`,

where

`d=1+2t(1-ell)`,  `c=12 ell t/d`.

Since `x -> exp(-c x^2)` is symmetric decreasing, the cap-one bathtub principle gives

`E exp(-c X^2) <= int_{-1/2}^{1/2} exp(-c x^2) dx`.

It remains to prove, for every `c>=0`,

`int_{-1/2}^{1/2} exp(-c x^2) dx <= (1+c/6)^(-1/2)`.

Put `y=sqrt(c)/2`. The inequality becomes

`erf(y) <= (2y/sqrt(pi))/sqrt(1+2y^2/3)`.

Both sides vanish at zero. The derivative of the right side, after removing the common factor `2/sqrt(pi)`, is

`(1+2y^2/3)^(-3/2)`.

This dominates `exp(-y^2)`, because

`(3/2) log(1+2y^2/3) <= y^2`

by `log(1+z)<=z`. Therefore the error-function inequality holds. Substituting `c` gives

`d^(-1/2)(1+c/6)^(-1/2)`

`= [d+2 ell t]^(-1/2)`

`= (1+2t)^(-1/2)`.

For `ell>0,t>0`, the last scalar comparison is strict. QED.

## 4. Main theorem: coordinated two-law zero-peak barrier

### QFORM-TWO-ORTHOGONAL-SAMESIGN-HEAVY-NOESCAPE-v1
For the limiting variable

`R=H_1^2+H_2^2-G_3^2`

above, with arbitrary independent cap-one heavy laws `X_1,X_2`,

`p_R(0) <= 1/(2 sqrt(2))`.

Consequently the physical `1/12` scaling satisfies

`p_{R/12}(0) <= 3 sqrt(2)`.

If at least one of `ell_1,ell_2` is positive, the inequality is strict.

Moreover, for fixed positive leverages, the centered unit-interval laws are the joint a.e. maximizers of this limiting zero peak among all two-coordinate choices `0<=f_i<=1`, `int f_i=1`.

### Proof
Let

`S=H_1^2+H_2^2`.

The square of an independent standard Gaussian has density

`f_{G_3^2}(s)=(2 pi s)^(-1/2) exp(-s/2)`, `s>0`.

Therefore

`p_R(0)=E f_{G_3^2}(S)`.

Use the exact Laplace representation

`s^(-1/2)e^{-s/2}`

`= pi^(-1/2) int_0^infinity u^(-1/2) exp(-(u+1/2)s) du`.

Tonelli and independence give

`p_R(0)`

`=1/(pi sqrt(2)) int_0^infinity u^(-1/2)`

`   * E exp(-(u+1/2)H_1^2)`

`   * E exp(-(u+1/2)H_2^2) du`.

Apply the preceding lemma to both factors. With `t=u+1/2`,

`(1+2t)^(-1)=1/[2(1+u)]`.

Hence

`p_R(0) <= 1/(2 pi sqrt(2)) int_0^infinity u^(-1/2)/(1+u) du`

`=1/(2 sqrt(2))`,

since the beta integral equals `pi`.

If one leverage is positive, the square-Laplace comparison is strict for every `u>0`, so the integrated inequality is strict.

For the joint optimizer statement, stop one step earlier in the one-coordinate lemma. For each fixed `t>0`, the factor depending on `X_i` is an integral of its density against a strictly symmetric-decreasing Gaussian kernel. The cap-one bathtub theorem says the centered interval `[-1/2,1/2]` uniquely maximizes that factor when `ell_i>0`. The zero-density representation is a positive integral of the product of the two factors, so the two centered intervals jointly maximize the zero peak. QED.

This is a genuine two-coordinate statement: arbitrary coordinated changes of both cap-one heavy laws are allowed, although the two macroscopic spectral rows are constrained to be orthogonal and to lie in the same-sign eigenspace.

## 5. For centered heavy intervals, the entire limiting density is controlled

Assume now `X_1,X_2` are centered unit intervals. Each `H_i` has a symmetric density nonincreasing in `|x|`: it is the convolution of a centered interval density with a centered Gaussian density (with the evident degenerate endpoint interpretations).

Let `f_S` be the density of `S=H_1^2+H_2^2`. In polar coordinates,

`f_S(s)=1/2 int_0^{2pi} h_1(sqrt(s) cos theta) h_2(sqrt(s) sin theta) dtheta`.

For each `theta`, the integrand is nonincreasing in `s`, so `f_S` is nonincreasing. The density `f_{G_3^2}` is also decreasing.

For `x>=0`,

`p_R(x)=int_0^infinity f_{G_3^2}(b) f_S(x+b) db <= p_R(0)`.

For `x=-a<0`,

`p_R(-a)=int_0^infinity f_S(s) f_{G_3^2}(s+a) ds <= p_R(0)`.

Thus

`||p_R||_infinity=p_R(0) <=1/(2 sqrt(2))`,

and after physical scaling

`||p_{R/12}||_infinity <=3 sqrt(2)`.

So the centered-interval version of this two-noncollinear-heavy limit cannot hide a larger off-zero peak.

For the exact finite uniform-bank approximants, the standard local CLT gives convergence of the relevant one-dimensional bank densities to the displayed Gaussian-completion law. In particular, this theorem is an asymptotic barrier for this concrete exact-spectrum product-source architecture. It does **not** rule out a finite-`m` overshoot; that possibility remains logically distinct and is listed below.

## 6. Exact integral calibration and checks

For centered heavy intervals one can write the zero peak as a one-dimensional positive integral. Set

`d_ell(t)=1+2t(1-ell)`,

`c_ell(t)=12 ell t/d_ell(t)`,

`L_ell(t)=d_ell(t)^(-1/2) int_{-1/2}^{1/2} exp(-c_ell(t)x^2) dx`.

Then

`p_{R/12}(0)`

`=12/(pi sqrt(2)) int_0^infinity u^(-1/2) L_{ell_1}(u+1/2)L_{ell_2}(u+1/2) du`.

The checker verifies the beta constant and gives non-rigorous numerical sanity values

- `(ell_1,ell_2)=(0,0)`: `4.2426406871192851464... =3 sqrt(2)`;
- `(1/4,1/2)`: `4.0713307181519005890...`;
- `(1,1)`: `2.9642054722746982585...`.

Only the analytic inequalities above are used for the theorem; the numerical values are controls.

## 7. Application of the partner result and revised witness search

The completed fleet03/B17 result removes arbitrary **one-coordinate** fragmentation as an improving mechanism for its exact six-variable cross witness. The present theorem tests the next natural coordinated alternative and removes another substantial branch: even if **both** heavy coordinate laws are changed arbitrarily under the cap-one constraint, two orthogonal same-sign macroscopic rows with diffuse Gaussian completion cannot beat the `3 sqrt(2)` zero saddle; for centered interval heavy laws they cannot beat it at any output level in the limiting model.

Together with the partner benchmark `4.0630706168...<3 sqrt(2)`, this sharpens the next source-valid adversarial search. A witness above `3 sqrt(2)`, if it exists, must exploit at least one feature absent here, such as

- two or more **nonorthogonal** macroscopic rows;
- macroscopic rows crossing opposite spectral signs;
- a finite/mesoscopic density overshoot that disappears in the Gaussian-completion limit;
- shared-coordinate coupling among several spectral directions;
- additional large eigendirections; or
- an off-zero peak in a geometry lacking the monotone-radial argument.

This is a supporting no-escape theorem, not a proof that `3 sqrt(2)` is the universal sharp constant and not a proof of the full QFORM conjecture.

## 8. Correction status

The proof does not use the refuted arbitrary-joint coarea bound, does not condition on a rotated projection and reuse a marginal density cap, and does not assume a uniformly conditioned physical pair. It keeps the exact physical product construction until the explicit CLT limit. The live correction inbox was consumed before this report.

No novelty or publication-priority claim is made.
