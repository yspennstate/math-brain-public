# QFORM B15 — rough-product continuity from one physical diagonal pivot

**Programme:** `QFORM-DENSITY-3EIG-20260922`, owner revision `2026-09-22.5`  
**Worker:** `fleet03/B15`  
**Run:** `20260922T153101Z-fleet03-B15-r12`  
**Classification:** `ESSENTIAL_STEP_APPLIED / TARGET_LEVEL_CONTINUITY_REDUCTION / FULL_TARGET_OPEN`  
**Execution:** `WITHOUT_VERIFIED_BRAIN`

## 1. Exact target and result of this run

The live target is: for every dimension `n`, independent real coordinates `X_i` with probability densities `0<=f_i<=1`, and every real symmetric `A` with at least three eigenvalues of absolute value at least one, prove that `Q=X^TAX` has a density with one universal finite `L^infinity` bound, or give a valid counterexample. Continuity of the output density is a separate stronger request.

This report does **not** prove the universal height constant. It proves a new target-level continuity theorem:

> **If `rank(A)>=3` and at least one original-coordinate diagonal entry `A_jj` is nonzero, then for every product input law with one-dimensional densities bounded by one, `X^TAX` has a density in `C_0(R)`.**

Thus for the owner's target the remaining rough-input continuity gap is confined to the exceptional physical-coordinate class

`diag(A)=0`.

The theorem retains the original product structure throughout. It assumes no continuity, moment, connected-support, compact-support, Gaussian, log-concave, sign, or eigenbasis-independence hypothesis.

The central universal `L^infinity` conjecture remains open even on the nonzero-diagonal class because the explicit height constants below depend on a selected physical principal block.

## 2. Completed sources actually consumed

### Assigned partner fleet04/B15

I consumed the completed partner report

- repository/commit: `yspennstate/math-open-problems@657566d3f5026e672f5cbe6b8c03fe63766bf0fb`;
- path: `proofnet24/QFORM-density/fleet-2026-09-22/fleet04/B15/20260922T132108Z-b15-qform-separator-regularity-r2/REPORT.md`.

Its Lemma 2.2 says: a common conditional `L^infinity` density bound `C`, convolved conditionally with an independent `L^1` density and then mixed, produces an unconditional `C_0` density with the **same** height bound `C`. I apply this to an actual inequality in Section 7.

I also consumed the newer partner reduction

- repository/commit: `yspennstate/math-open-problems@07672b7beb8f867c7a7b973aa3157a42ae506460`;
- path: `proofnet24/QFORM-density/fleet-2026-09-22/fleet04/B15/20260922T152333Z-b15-qform-continuous-envelope-r3/REPORT.md`.

It proves exactly that the optimal universal interval-density constant over the full target class equals the optimal constant over target instances with `C_0` output, and also equals the optimal constant over compactly supported smooth cap-one marginals. I use this only in the final regularity ledger; it does not prove rough-input continuity.

### Local finite-dimensional inputs

I use the following completed results at their exact scopes.

1. `fleet01/B15`, repository/commit `yspennstate/math-open-problems@47dc925729bbf269333cc6e1256178a538d2f553`, path `proofnet24/QFORM-density/fleet-2026-09-22/fleet01/B15/20260922T120320Z-fleet01-B15-qform/REPORT.md`:
   - every invertible physical symmetric `3x3` block gives an affine-quadratic density bound `(2*pi+3*sqrt(3))/sigma_min(B)`;
   - every invertible physical symmetric `4x4` block gives `(4*pi+8)/sigma_min(B)`;
   - every symmetric matrix of rank at least three has an invertible principal block of order three or four, and the Schur-complement extension proof can be started from a prescribed nonsingular `1x1` principal pivot.

2. `fleet01/B11`, repository/commit `yspennstate/math-open-problems@2279571f59ade7a9ec478af1e4818f6c117ac224`, path `proofnet24/QFORM-density/fleet-2026-09-22/fleet01/B11/QFORM-B11-20260922T121344Z/REPORT.md`:
   every nondegenerate indefinite binary quadratic in two original independent cap-one coordinates has a density in `L^3`, quantitatively
   
   `||p_R||_3 <= C_bin D^(-1/3)`,
   
   where `D=a^2-alpha beta=-det(S)>0` for matrix `S=[[alpha,a],[a,beta]]`.

3. The square-density estimate used there from `fleet02/B11`, repository/commit `yspennstate/math-open-problems@ea26c080ff290b0f10ec701ec8bf8847cc84ceb6`, path `proofnet24/QFORM-density/fleet-2026-09-22/fleet02/B11/20260922T115006Z-fleet02-B11-qform-r18-7c1e/REPORT.md`:
   
   `||p_{dZ^2+uZ+v}||_(3/2) <= 2 |d|^(-1/3)`
   
   for one cap-one coordinate and `d!=0`.

No law-uniform pointwise oscillatory decay is used.

## 3. A finite-block theorem

Let `d in {3,4}`. Let `Y=(Y_1,...,Y_d)` have independent cap-one probability densities. Let `B` be invertible symmetric `dxd`, and suppose one physical diagonal entry of `B` is nonzero. After permuting coordinates, write

`B = [[C,a],[a^T,b]]`,  with `b!=0`,

where `C` is `(d-1)x(d-1)` and `a` is a column vector. Put

`S = C - a a^T/b`,  `v=a/b`.

Because `det(B)=b det(S)`, the Schur complement `S` is invertible.

Consider the general affine quadratic

`T(Y)=Y^T B Y + 2 ell^T Y + c`.

Translate each original coordinate by the corresponding component of `B^{-1}ell`. Conditional deterministic coordinate translations preserve independence and the cap one. Up to an output translation, it is enough to study the homogeneous form. Writing `Y=(U,Z)` gives the exact identity

`Y^T B Y = R(U) + b (Z+M(U))^2`,

where

`R(U)=U^T S U`,  `M(U)=v^T U`.

The key is to prove enough regularity of the pair `(R,M)` without claiming a false conditional density cap.

## 4. The Schur residual always has an `L^3` density

Write `m=d-1`.

### Case d=3: binary residual

Here `m=2` and `S` is invertible.

- If `S` is indefinite, fleet01/B11 gives
  
  `||p_R||_3 <= C_bin |det S|^(-1/3)`.

- If `S` is definite, the standard two-variable definite quadratic estimate gives
  
  `||p_R||_infinity <= pi/sqrt(|det S|)`.
  
  Since `p_R` is a probability density,
  
  `||p_R||_3 <= ||p_R||_infinity^(2/3) <= (pi/sqrt(|det S|))^(2/3)`.

### Case d=4: ternary residual

Here `m=3`. The fleet01/B15 three-variable affine theorem applied to `S` gives

`||p_R||_infinity <= C_3/sigma_min(S)`,  `C_3=2*pi+3*sqrt(3)`.

Hence

`||p_R||_3 <= (C_3/sigma_min(S))^(2/3)`.

In every case define one valid finite bound `M_3(S)` by

`M_3(S) = C_bin |det S|^(-1/3)` if `d=3` and `S` is indefinite,

`M_3(S) = (pi/sqrt(|det S|))^(2/3)` if `d=3` and `S` is definite,

`M_3(S) = (C_3/sigma_min(S))^(2/3)` if `d=4`.

Then

`||p_R||_3 <= M_3(S) < infinity`.

These are physical-coordinate statements. No diagonalization of the input law occurs.

## 5. Coupled pivot: the joint map (R,M) is absolutely continuous

Assume now `a!=0`, equivalently `v!=0`. Define

`Psi: R^m -> R^2`,  `Psi(u)=(R(u),M(u))=(u^T S u, v^T u)`.

Its differential has row vectors

`2Su` and `v`.

The differential has rank less than two exactly when `Su` is parallel to `v`. Since `S` is invertible, this critical set is the one-dimensional subspace

`S^(-1)(span(v))`.

For `m=2` or `3` that set has `m`-dimensional Lebesgue measure zero. On the complement the two-dimensional Jacobian `J_2 Psi` is positive.

Let `N subset R^2` be Lebesgue-null and set

`E_k={u: |u|<=k, J_2 Psi(u)>=1/k}`.

The coarea formula gives

`integral_{E_k cap Psi^(-1)(N)} J_2 Psi(u) du = integral_N H^(m-2)(E_k cap Psi^(-1)(y)) dy = 0`.

Therefore `Leb_m(E_k cap Psi^(-1)(N))=0`. The union of the `E_k`, together with the null critical set, covers `R^m` up to a null set. Since the product law of `U` is absolutely continuous, `(R,M)` is absolutely continuous on `R^2`.

Let `H(r,m)` be a joint density. Then for almost every `r`,

`H_r(m):=H(r,m) in L^1(dm)`,

and

`integral H(r,m) dm = p_R(r)`.

This is the point at which original product structure is spent quantitatively; we do **not** assert that an arbitrary conditional density of `M` given `R` is bounded.

## 6. Adding the independent pivot coordinate creates a continuous conditional kernel

Let `f_Z` be the density of the independent pivot coordinate `Z`; `0<=f_Z<=1` and `f_Z in L^1`.

Set

`V=Z+M`.

Then `(R,V)` has joint density

`K(r,z)=integral H(r,m) f_Z(z-m) dm`.

For almost every `r`, `K(r,.)` is the convolution of two `L^1` functions, so

`K(r,.) in C_0(R)`.

Also the cap on `f_Z` gives the exact envelope

`0 <= K(r,z) <= integral H(r,m) dm = p_R(r)`

for almost every `(r,z)`.

This envelope is the substitute for the false generic statement that conditioning preserves the original marginal density cap.

## 7. Exact density formula, height bound, and assigned-partner application

Put `a_0=|b|` and `sigma=sign(b)`. For

`T=R+bV^2`,

one-dimensional change of variables in `V` gives, for almost every `t`,

`p_T(t) = (1/(2 sqrt(a_0))) integral_{sigma(t-r)>0}`

`  [ K(r, sqrt(|t-r|/a_0)) + K(r,-sqrt(|t-r|/a_0)) ] / sqrt(|t-r|) dr.`

Consequently

`p_T(t) <= a_0^(-1/2) integral_{sigma(t-r)>0} p_R(r) |t-r|^(-1/2) dr.`

Let `M=||p_R||_3`. Split the integral at distance `L>0`. Holder with exponents `3` and `3/2` gives

`near <= M (integral_0^L s^(-3/4) ds)^(2/3)`

`     = 4^(2/3) M L^(1/6)`.

The far part is at most `L^(-1/2)||p_R||_1=L^(-1/2)`. Choosing

`L=(4^(2/3) M)^(-3/2)=1/(4 M^(3/2))`

makes both pieces equal `2 M^(3/4)`. Therefore

`boxed( ||p_T||_infinity <= 4 |b|^(-1/2) ||p_R||_3^(3/4) )`

and hence, on the coupled branch,

`boxed( ||p_T||_infinity <= 4 |b|^(-1/2) M_3(S)^(3/4). )`

This is finite but matrix-dependent.

### Uncoupled branch and the assigned fleet04/B15 inequality

If `a=0`, then `M=0` and `R(U)` is independent of `bZ^2`. The square-density estimate gives `p_{bZ^2} in L^(3/2)` and Young gives directly

`||p_T||_infinity <= 2 |b|^(-1/3) ||p_R||_3`.

There is also an exact place where the assigned partner result fleet04/B15 improves and regularizes an actual inequality. In the `d=4`, `a=0` branch, `R` is a three-variable quadratic with

`||p_R||_infinity <= C_3/sigma_min(S)`.

The square `bZ^2` has an `L^1` probability density and is independent of `R`. Applying fleet04/B15 Lemma 2.2 with no external conditioner yields

`boxed( p_T in C_0(R),  ||p_T||_infinity <= C_3/sigma_min(S). )`

Thus the completed partner theorem is used on the actual QFORM height inequality without any loss in the constant.

## 8. New point: the fully coupled branch is also continuous

The bound in Section 7 alone gives only essential boundedness. The joint kernel `K`, however, supplies the missing scale coherence.

Assume first `b>0`; reflection handles `b<0`. Let `t_n -> t` and fix `delta>0`.

### Far from the moving square-root endpoint

On `r<=t-delta`, for all sufficiently large `n` we have `t_n-r>=delta/2`. For almost every fixed `r`, the function `K(r,.)` is continuous, hence the integrand defining `p_T(t_n)` converges to the integrand defining `p_T(t)`. It is dominated by a constant depending only on `delta` times `p_R(r)`, which is integrable. Dominated convergence therefore proves convergence of the far pieces.

### Near the endpoint

The union of the near pieces for `t_n` and `t` lies, for large `n`, inside an interval of `r`-length at most `3 delta/2`. The envelope from Section 7 and Holder give a uniform error at most

`|b|^(-1/2) 4^(2/3) ||p_R||_3 (3 delta/2)^(1/6)`

for each near contribution, up to an inessential factor two when comparing both endpoints. This tends to zero as `delta -> 0`.

First let `n->infinity` at fixed `delta`, then let `delta->0`. Hence `p_T` has a continuous representative.

### Vanishing at infinity

For any fixed `L>0`, split the envelope again into distances at most `L` and greater than `L`. The far part is at most `|b|^(-1/2)L^(-1/2)`. The near part is bounded by

`|b|^(-1/2) 4^(2/3) ||p_R 1_[t-L,t]||_3 L^(1/6)`

for `b>0` (with the reflected interval for `b<0`). Because `p_R^3 in L^1`, that local `L^3` norm tends to zero as `|t|->infinity`. Then let `L->infinity`. Thus

`p_T(t)->0` as `|t|->infinity`.

Therefore the fully coupled finite-block output satisfies

`boxed( p_T in C_0(R). )`

This is stronger than the earlier fleet01/B11 dependent-square theorem, which established the height bound on the fully coupled branch but did not claim continuity there.

## 9. Finite-block regularity theorem

### Theorem — `QFORM-NONZERO-DIAGONAL-BLOCK-C0-v1`

Let `d in {3,4}`. Let `Y_1,...,Y_d` be independent real random variables with arbitrary probability densities bounded by one. Let `B` be an invertible real symmetric `dxd` matrix having at least one nonzero original-coordinate diagonal entry. Then every affine quadratic

`Y^T B Y + 2 ell^T Y + c`

has a density in `C_0(R)`.

Moreover the proof gives a finite bound depending only on the physical block `B` (not on the input laws or affine terms): after choosing a nonzero diagonal pivot `b` and Schur complement `S`, one may take

- `2 |b|^(-1/3) M_3(S)` if the pivot is uncoupled from the other selected coordinates;
- `4 |b|^(-1/2) M_3(S)^(3/4)` if it is coupled.

Independently, fleet01/B15 supplies the simpler common height bound `C_d/sigma_min(B)` with `C_3=2*pi+3*sqrt(3)` and `C_4=4*pi+8`.

## 10. High-dimensional target-level corollary

### Theorem — `QFORM-NONZERO-PHYSICAL-DIAGONAL-C0-v1`

Let `A` be a real symmetric `n x n` matrix with `rank(A)>=3`. Assume that `A_jj!=0` for at least one original coordinate `j`. Let `X_1,...,X_n` be independent with arbitrary probability densities bounded by one. Then

`boxed( X^T A X has a density p_Q in C_0(R). )`

### Proof

Start the principal-block extension lemma of fleet01/B15 from the nonsingular `1x1` principal block `{j}`. Because `rank(A)>=3`, after one or two Schur-complement extensions it yields an invertible principal block `B=A_{I,I}` of order `3` or `4` containing `j`. In particular, the selected block still has a nonzero physical diagonal entry.

Condition on every coordinate outside `I`. The conditional polynomial in the original independent coordinates `X_I` is an affine quadratic with fixed quadratic matrix `B`; only its affine and constant terms depend on the conditioned variables. The finite-block theorem gives a `C_0` density for every conditional law, and its displayed height bound depends only on `B`, not on those affine terms or on the conditioning value.

Choose jointly measurable conditional-density versions. The unconditional density is the mixture

`p_Q(t)=E[p_{Q|X_{I^c}}(t)]`.

If `t_n->t`, conditional continuity plus the common finite height bound gives `p_Q(t_n)->p_Q(t)` by dominated convergence. Conditional vanishing at infinity plus the same common bound gives `p_Q(t)->0` as `|t|->infinity`. Hence `p_Q in C_0(R)`. QED.

The owner's spectral hypothesis implies `rank(A)>=3`, so this theorem applies to every target matrix except possibly those with **all physical diagonal entries zero**.

## 11. Interaction with the latest fleet04/B15 extremal-envelope theorem

The latest assigned-partner result proves

`C_all = C_C0 = C_sm`

for the optimal universal density constant, including the value `+infinity`. Combining that completed theorem with this run gives a clean separation:

1. **For the central universal `L^infinity` conjecture**, there is no loss in working entirely with continuous-output or smooth-input instances, even before the zero-diagonal continuity gap is settled.
2. **For the stronger assertion that every rough target instance itself has a continuous density**, this run reduces the only remaining matrix class to `diag(A)=0`.

So a proof of rough-output continuity should now attack the all-zero-physical-diagonal class directly, while the universal height programme should not wait for that stronger regularity statement.

## 12. Exact remaining obligations

### Universal height

Still open. The finite-block constants can deteriorate with `sigma_min(B)`, `|b|`, or Schur data along valid flat/delocalized target matrices. This report does not convert three large eigenvalues into a universal block constant.

### Rough-input continuity

Reduced to:

> Prove `p_Q in C_0(R)` for target matrices with `diag(A)=0`, or construct a valid product-law target counterexample to continuity.

Because `trace(A)=0` in this exceptional class, any nonzero such matrix is indefinite, but that observation alone supplies no uniform or continuity theorem. The natural next mechanism is an off-diagonal/bilinear original-coordinate smoothing argument that retains product provenance rather than taking arbitrary projected joint densities.

## 13. Corrections respected

- No law-uniform pointwise van-der-Corput/Fresnel decay is used.
- No rotated-coordinate independence is assumed.
- No generic bounded conditional density is asserted after nonlinear conditioning; instead the joint density `K(r,z)` is constructed explicitly and only the valid envelope `K(r,z)<=p_R(r)` is used.
- No bounded projection theorem is substituted for the indefinite quadratic pushforward.
- No fixed fragment count, bounded support diameter, naive fiber supremum, or single-cross-minor dichotomy is used.
- Repeated eigenvalues are not treated as Hessian degeneracy.
- No numerical histogram is used as proof.

**Full QFORM remains OPEN / NOT PROVED / NOT DISPROVED.** No novelty or publication-priority claim is made.
