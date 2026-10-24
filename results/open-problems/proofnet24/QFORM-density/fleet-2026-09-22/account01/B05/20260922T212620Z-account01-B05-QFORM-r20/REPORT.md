# account01/B05 — joint radial coarea closure for the hyperbolic-square core

Run: `20260922T212620Z-account01-B05-QFORM-r20`

Programme: `QFORM-DENSITY-3EIG-20260922`; fresh OWNER CONTROL read during this run: revision `2026-09-22.15`.

Classification: `ESSENTIAL_STEP_APPLIED / SUPPORTING_THEOREM_PROVED / PRECISE_REMAINING_FACTOR_IDENTIFIED`.

Full QFORM remains OPEN. Essential boundedness is proved only in the stated independent three-scalar core and perturbative partner scope below. Continuity is not proved here.

Execution label for native learned-memory purposes: `WITHOUT_VERIFIED_BRAIN` (authenticated repository retrieval occurred, but repository transport is not native learned-memory ingestion).

## 1. Conditional end-to-end picture and the step attacked

The B05 coarea route previously reached the canonical curvature-sector integral

`p(q) = (1/2) integral_R J_rho(q) d rho`,

where, in the normalized hyperbolic-square core,

`J_rho(q) = integral_R f_X(q/(2y) - sigma rho^2 y/2) f_Y(y) f_Z(rho y) dy`, `sigma in {+1,-1}`.

A previous B05 run proved that no law-independent integrable pointwise envelope `J_rho(q) <= w(rho)` can exist: a moving stationary ridge can have height comparable to `1/rho` on a narrow rho-window. The missing implication was therefore to control the rho integral jointly, before taking a pointwise radial majorant.

This report closes that implication completely for three genuinely independent cap-one scalar inputs. The proof is elementary and product-preserving. It also explains the compensation: the product variable has only a logarithmic density singularity, and convolution with a square variable integrates that logarithm uniformly in the output translation.

The global full-matrix debt remains the extraction of such an independent three-scalar interface, or a coarea estimate that tolerates the residual within-bank quadratic dependence jointly.

## 2. Product-density envelope

### Lemma 2.1 — logarithmic product envelope

Let `X,Y` be independent real random variables with probability densities `f_X,f_Y` satisfying `0<=f_X,f_Y<=1`. Let `W=XY`. Then `W` has a density `h_W`, and for every `w != 0`,

`h_W(w) <= 4 asinh(1/(2 sqrt(|w|))).`                                      (2.1)

#### Proof

For `w>0`, split the density formula

`h_W(w)= integral_R f_X(x) f_Y(w/x) dx/|x|`

into the two same-sign quadrants. On the positive quadrant write

`x=sqrt(w) e^s`, `w/x=sqrt(w)e^{-s}`,

and put

`H(s)=f_X(sqrt(w)e^s) f_Y(sqrt(w)e^{-s})`.

Then `0<=H<=1`, and

`sqrt(w) integral e^s H(s) ds <= 1`,

because the left-hand side is at most `integral_{x>0} f_X(x) dx`. By the symmetric change of variables through `y=w/x`, also

`sqrt(w) integral e^{-s} H(s) ds <= 1`.

Hence

`integral 2 cosh(s) H(s) ds <= 2/sqrt(w).`                       (2.2)

For fixed mass `m=integral H`, the left-hand side of (2.2) is minimized, under `0<=H<=1`, by filling the centered interval `[-m/2,m/2]` where `2cosh s` is smallest (the one-dimensional bathtub principle). Therefore

`4 sinh(m/2) <= 2/sqrt(w)`,

so

`m <= 2 asinh(1/(2sqrt(w))).`

The negative-negative quadrant satisfies the same bound, giving (2.1) for `w>0`. For `w<0`, use the positive-negative and negative-positive quadrants, with `|w|` in place of `w`. QED.

### Corollary 2.2

For `U=2XY`,

`h_U(u) <= H(u):=2 asinh((2|u|)^(-1/2))`, `u!=0`.                (2.3)

This logarithmic singularity is locally integrable and, for `|u|>=1`,

`H(u) <= H(1)=2 asinh(1/sqrt(2)) < sqrt(2).`                    (2.4)

For `0<|u|<1`, since `asinh x <= log(1+2x)` and `log(1+sqrt(2))<0.9`,

`H(u) <= 1.8 + log(1/|u|).`                                     (2.5)

Consequently

`integral_{-1}^1 H(u)^3 du`
` <= 2 integral_0^1 (1.8+log(1/u))^3 du`
` = 2(1.8^3 + 3*1.8^2 + 6*1.8 + 6)`
` < 64.71.`                                                       (2.6)

The identity uses `integral_0^1 log(1/u)^k du=k!` for `k=0,1,2,3`.

## 3. Uniform convolution with one square

### Theorem 3.1 — `QFORM-HYPERBOLIC-SQUARE-JOINT-RADIAL-TRACE-v1`

Let `X,Y,Z` be independent real random variables with probability densities bounded by one. Let `sigma in {+1,-1}` and

`Q_0 = 2XY + sigma Z^2`.

Then `Q_0` has an essentially bounded density and

`||p_{Q_0}||_infinity < 14`.                                     (3.1)

#### Proof

For `V=Z^2`, its density `g` on `(0,infinity)` satisfies

`g(v)=(f_Z(sqrt(v))+f_Z(-sqrt(v)))/(2sqrt(v)) <= v^(-1/2)`,      (3.2)

and `integral_0^infinity g=1`. For `sigma=-1`, reflect this density to the negative half-line; the argument is identical, so take `sigma=+1`.

By independence,

`p_{Q_0}(q)= integral_0^infinity h_U(q-v) g(v) dv`.

Use (2.3). Split into `|q-v|>=1` and `|q-v|<1`.

On the far part, (2.4) and `integral g=1` give a contribution `<sqrt(2)`.

On the local part, if `q>=2`, then `v>=1`, so `g(v)<=1` and

`integral_{|q-v|<1} H(q-v)g(v)dv <= integral_{-1}^1 H(u)du < infinity`.

For the only potentially worse range `-1<q<2`, the local integration lies in `0<v<3`. Holder with exponents `3/2` and `3`, together with (3.2) and (2.6), gives

`integral_{|q-v|<1} H(q-v)g(v)dv`
` <= (integral_0^3 v^(-3/4)dv)^(2/3) (integral_{-1}^1 H(u)^3du)^(1/3)`
` < (4*3^(1/4))^(2/3) * 64.71^(1/3)`
` < 12.3.`

If `q<=-1`, the local set is empty. Therefore every `q` satisfies

`p_{Q_0}(q) < 12.3 + sqrt(2) < 14`.

This proves (3.1). QED.

## 4. Scaling and arbitrary affine terms

### Corollary 4.1

Let `beta,gamma` be nonzero and put `m=min(|beta|,|gamma|)`. For arbitrary real `a,b,c,d`,

`Q = 2 beta XY + gamma Z^2 + aX+bY+cZ+d`

has

`||p_Q||_infinity < 14/m`.                                      (4.1)

Indeed, translate `X,Y,Z` coordinatewise to remove all three linear terms:

`2 beta XY+aX+bY = 2 beta (X+b/(2beta))(Y+a/(2beta)) + constant`,

`gamma Z^2+cZ = gamma (Z+c/(2gamma))^2 + constant`.

Translations preserve independence and density caps. Next set

`X_1=sqrt(|beta|/m) X`, `Y_1=sqrt(|beta|/m)Y`, `Z_1=sqrt(|gamma|/m)Z`.

Each rescaled density is still bounded by one, and after harmless sign reflections

`Q = m(2X_1Y_1 +/- Z_1^2)+constant`.

Apply Theorem 3.1 and the output scaling rule.

## 5. Exact coarea/radial consequence

For the canonical `Q_0=2XY+sigma Z^2`, integrate first in `x` and then set `z=rho y`. For almost every `q`,

`p_{Q_0}(q)`
` = (1/2) integral_R integral_R`
` f_X(q/(2y)-sigma rho^2 y/2) f_Y(y) f_Z(rho y) dy d rho`.

Thus, with

`J_rho(q)=integral_R f_X(q/(2y)-sigma rho^2 y/2) f_Y(y) f_Z(rho y)dy`,

Theorem 3.1 gives the genuinely joint radial estimate

`sup_q integral_R J_rho(q) d rho < 28`.                          (5.1)

This is exactly the compensation missing from any law-independent pointwise radial envelope: large moving-ridge slices are permitted, but their total rho-integral at each fixed output level is uniformly bounded.

## 6. Named partner result applied to an actual inequality

I consumed account02/B05 run `20260922T202100Z-b05-qform-47d9c1a2`, canonical commit

`a31006ef311ca9e937f37c62d602d21ada3b1139`, theorem `QFORM-THREE-BANK-GENERAL-CORE-v1`.

It proves for three independent cap-one scalar inputs `Y in R^3` and arbitrary affine terms that

`sigma_min(M)>=s  ==>  ||p_{Y^T M Y + ell.Y+c}||_infinity <36/s`. (6.1)

Apply (6.1) to the canonical hyperbolic-square matrix

`M_0=[[0,1,0],[1,0,0],[0,0,sigma]]`,

for which `sigma_min(M_0)=1`, recovering the independent check `||p||_infinity<36`.

More substantively, for every symmetric perturbation `E` with `||E||_op<=1/2`, Weyl's inequality gives

`sigma_min(M_0+E)>=1/2`,

and the partner theorem yields the robust neighborhood estimate

`||p_{Y^T(M_0+E)Y+ell.Y+c}||_infinity <72`.                     (6.2)

Thus the joint-radial closure proved here is not a fragile zero-pattern phenomenon at the scalar-bank level: the completed partner theorem pays all scalar-core perturbations once the three independent banks have been obtained with a uniformly nonsingular density-normalized compressed core.

## 7. What is paid and the first unpaid implication

Paid in this run:

1. the previous B05 `QFORM-STATIONARY-RIDGE-JOINT-RADIAL-TRACE` debt is closed for the true independent three-scalar hyperbolic-square core;
2. there is no need for an integrable pointwise radial envelope;
3. the exact joint coarea integral is uniformly `<28` in normalized coordinates;
4. arbitrary affine terms and coefficient scales are handled by product-preserving translations/dilations;
5. the account02/B05 general-core theorem extends the result to a full operator-norm neighborhood and, in fact, all uniformly nonsingular independent three-scalar cores.

The first unpaid global implication is now exactly the partner's extraction/leakage debt:

`QFORM-INDEPENDENT-TRIBANK-EXTRACTION-OR-JOINT-RESIDUAL-COAREA-v1`.

From an arbitrary original-coordinate symmetric `A` with at least three singular/eigenvalue magnitudes >=1, one must either

- produce three disjoint original-coordinate scalar aggregates with independent laws and controlled density caps whose density-normalized compressed quadratic core has uniformly positive smallest singular value, while all omitted terms are independent direct sums or only affine after conditioning; or
- prove a coarea/small-ball inequality that keeps the remaining within-bank quadratic residual dependence jointly with the three aggregate coordinates; or
- route the matrix to an already-completed physical-pair, ridge/diffuse, grouped-star or other dependence-safe branch.

The missing factor is therefore not the radial integration of a genuine three-scalar core. It is preserving or replacing that independent three-scalar interface in the presence of the full residual quadratic leakage.

## 8. Integrity and scope

No Gaussianity, log-concavity, moments, compact support, connected support, diagonal-basis independence, pointwise Fresnel decay, arbitrary-joint coarea bound, or conditional-density supremum is used. The proof keeps the original scalar independence throughout.

This is a supporting theorem, not the full QFORM solution. Essential boundedness is proved in the stated scope; continuity is not established. No numerical experiment is used as proof; the displayed decimal inequalities only simplify explicit analytic constants.
