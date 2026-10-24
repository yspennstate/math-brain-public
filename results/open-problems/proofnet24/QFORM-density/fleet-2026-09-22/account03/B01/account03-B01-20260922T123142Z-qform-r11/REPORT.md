# QFORM account03/B01 — averaged Fourier ladder at rank two

Programme: `QFORM-DENSITY-3EIG-20260922`  
Owner control revision consumed: `2026-09-22.5`  
Run: `account03-B01-20260922T123142Z-qform-r11`  
Assignment: `Oscillatory replacement`  
Status: `PROVED_SUPPORTING_THEOREM / FULL_TARGET_OPEN / WITHOUT_VERIFIED_BRAIN`

## 1. Target and correction-aware scope

The full target is the following: for arbitrary independent real random variables `X_i` with probability densities `0<=f_i<=1`, and every real symmetric matrix `A` having at least three eigenvalues of modulus at least one, prove one dimension- and law-independent finite bound on the density of `X^T A X`, or give a valid counterexample.

The full conjecture is **not** proved here. In particular, this report does not assume that a spectral rotation preserves independence, and it does not use the refuted law-uniform pointwise one-variable estimate `|E exp(i t X^2)| <= C |t|^{-1/2}`.

The current corrections `QFORM-CROSSMINOR-ALONE-FALSE`, `QFORM-UNIVERSAL-PI-FALSE-AND-DIFFUSE-BRANCH`, and `QFORM-TWOSHEET-XRAY-ONLY-FALSE` are also respected. The theorem below retains product structure through a Brascamp--Lieb/Hausdorff--Young argument and gives an **averaged-frequency replacement** in exactly the rank-two logarithmic regime where pointwise time integrability fails.

The phase-aligned density counterexample remains intact: for a prescribed frequency one may place a density-1 indicator on a finite union of intervals where the quadratic phase is almost constant, so no positive law-uniform pointwise decay exponent is available from the one-dimensional density cap alone. The present result avoids that premise entirely.

## 2. Source theorem being extended

A fresh supporting result, `QFORM-DIFFUSE-SEPARABLE-PHASE-v1`, proves the following for rank `r>=3`. Let `U` be `n x r` with orthonormal columns, rows `u_i^T`, and row leverages `c_i=||u_i||_2^2 <= 1/2`. Let `Lambda` be invertible symmetric and let `V_i` be arbitrary measurable real functions. For

`T=(U^T X)^T Lambda (U^T X)+sum_i V_i(X_i)`,

put `B(U)=prod_{c_i>0}(1-c_i)^(-(1-c_i)/2)`, `Delta=|det Lambda|`.

Its proof establishes *before using r>=3* the characteristic-function estimate

`|phi_T(t)| <= min(1, K |t|^{-r/2})`,

where `K=B(U) pi^(r/2) Delta^(-1/2)`.

That estimate comes from complex product amplitudes `h_{i,t}=f_i exp(i t V_i)`, geometric rank-one Brascamp--Lieb, Hausdorff--Young for each coordinate amplitude, and exact Gaussian evaluation of the quadratic kernel. The leverage assumption is used only to keep the coordinate Fourier exponents at least two. The source then takes `r>=3` so the envelope is in `L^1(dt)` and obtains an `L^infinity` output density.

Canonical source: `yspennstate/math-open-problems@773b7fb6f0e6a8142066f0bac08d228dfc164fdb:proofnet24/QFORM-density/interactive/20260922T120815Z-separable-perturbations/REPORT.md`.

## 3. New theorem: the full Hausdorff--Young ladder

### Theorem QFORM-DIFFUSE-AVERAGED-LP-v1

Let `r>=2`. Let `X_1,...,X_n` be independent real random variables with probability densities `0<=f_i<=1`. Let `U` be an `n x r` real matrix with orthonormal columns and rows `u_i^T`, and assume `c_i=||u_i||_2^2 <= 1/2` for every `i`.

Let `Lambda` be an invertible real symmetric `r x r` matrix, let `V_i` be arbitrary real-valued measurable functions finite almost surely, and set

`T=(U^T X)^T Lambda(U^T X)+sum_i V_i(X_i)`.

Define `B(U)=prod_{c_i>0}(1-c_i)^(-(1-c_i)/2)`, `Delta=|det Lambda|`.

For every `q in [1,2]` satisfying `r q>2`, with conjugate exponent `p=q/(q-1)` (and `p=infinity` when `q=1`), the law of `T` has a density in `L^p` and

`||p_T||_p <= [r q/(r q-2)]^(1/q) B(U)^(2/(r q)) Delta^(-1/(r q)).`    (3.1)

Moreover `B(U)<=exp(r/2)`. In the endpoint `r>=3,q=1`, (3.1) recovers the existing bounded-continuous-density theorem. The new case is `r=2`, where `q=1` is forbidden but every `q>1` is allowed.

In particular, for `r=2`, choosing `q=3/2`, `p=3`, gives

`||p_T||_3 <= (3 B(U))^(2/3) Delta^(-1/3) <= (3e)^(2/3) Delta^(-1/3) < 4.052 Delta^(-1/3).`    (3.2)

Thus a genuinely rotated **rank-two** quadratic component can retain its logarithmic point singularity while still obeying a universal `L^3` density estimate, provided its original-coordinate frame has leverage at most `1/2`. This is the exponent needed to be smoothed to `L^infinity` by one independent square direction.

### Proof

The complex-amplitude Brascamp--Lieb/Gaussian-kernel argument from the source theorem is valid verbatim for every `r>=2` through the characteristic-function estimate

`|phi_T(t)| <= min(1,K|t|^{-r/2})`,

with `K=B(U) pi^(r/2) Delta^(-1/2)`. No one-dimensional law-uniform Fresnel estimate occurs here. The dependence of the projected spectral coordinates is retained inside the pushforward complex density.

Fix `q in [1,2]` with `r q>2`. Put `t_0=K^(2/r)`. Using the preceding envelope,

`int_R |phi_T(t)|^q dt <= 2 int_0^infinity min(1,K^q t^(-r q/2)) dt`

`=2[t_0+K^q int_(t_0)^infinity t^(-r q/2)dt]`

`=2 K^(2/r)[1+2/(r q-2)]`

`= [2 r q/(r q-2)] K^(2/r).`                           (3.3)

Therefore

`||phi_T||_q <= [2 r q/(r q-2)]^(1/q) K^(2/(r q)).`    (3.4)

Use the Fourier convention `hat h(xi)=int exp(-i xi x)h(x)dx`. The nonsharp Hausdorff--Young inequality obtained by interpolation between `L^1 -> L^infinity` and Plancherel is

`||hat h||_p <= (2pi)^(1/p)||h||_q`, `1<=q<=2`, `p=q/(q-1)`.

Since `p_T(x)=(2pi)^(-1) hat(phi_T)(-x)`, (3.4) yields

`||p_T||_p <=(2pi)^(-1/q)[2 r q/(r q-2)]^(1/q) B(U)^(2/(r q)) pi^(1/q) Delta^(-1/(r q))`

`=[r q/(r q-2)]^(1/q) B(U)^(2/(r q)) Delta^(-1/(r q)).`

This proves (3.1). The elementary bound `-(1-c)log(1-c)<=c`, `0<=c<1`, combined with `sum_i c_i=r` gives `B(U)<=exp(r/2)`.

For `r=2,q=3/2`, `r q=3`, so (3.1) becomes `||p_T||_3 <= 3^(2/3) B(U)^(2/3) Delta^(-1/3)`, which is (3.2). QED.

## 4. Why this is the correct averaged replacement at rank two

For `r=2`, the characteristic-function estimate gives only `|phi(t)| <= min(1,K/|t|)`. This is not in `L^1(dt)`, exactly matching the fact that an indefinite rank-two quadratic may have a logarithmically divergent density. But it lies in every `L^q(dt)` with `q>1`; Hausdorff--Young converts that averaged time-frequency information into finite output `L^p` norms for every finite `p>2`.

The `p=3` choice is structurally distinguished because a one-dimensional square has a universal `L^(3/2)` density bound, and `1/3+2/3=1` is exactly Young's convolution endpoint for an `L^infinity` result.

This makes the rank-two logarithmic singularity a usable intermediate object instead of trying to suppress it with a false pointwise decay theorem.

## 5. Three-direction corollary: diffuse hyperbolic plane plus a disjoint square

### Corollary QFORM-DIFFUSE-RANK2-PLUS-SQUARE-v1

Assume the hypotheses of the theorem with `r=2`. Suppose there is an additional original coordinate `j` with `u_j=0`, independent of the variables entering the rank-two projection, and the corresponding separable term is `S=d X_j^2+a X_j+b`, `d!=0`.

Put all remaining coordinate-separable terms into `R`, so `T=R+S` and `R` is independent of `S`. Then

`||p_T||_infinity <= 2 (3B(U))^(2/3) (Delta |d|)^(-1/3) <= 2(3e)^(2/3)(Delta |d|)^(-1/3) < 8.103 (Delta |d|)^(-1/3).`    (5.1)

The density is continuous and vanishes at infinity.

### Proof

By (3.2), `||p_R||_3 <= (3B(U))^(2/3) Delta^(-1/3)`. The completed-square one-dimensional estimate, already proved in the QFORM archive, gives `||p_S||_(3/2) <= 2 |d|^(-1/3)`. Independence gives `p_T=p_R*p_S`; Young's inequality gives (5.1). Since `1<3,3/2<infinity`, translation continuity in the conjugate Lebesgue spaces gives a continuous convolution vanishing at infinity. QED.

This is a genuine three-direction bounded-density theorem: two directions may be a diffuse rotated indefinite plane rather than two physical coordinate axes. It is still only a scoped certificate because the third square direction must be carried by a disjoint original coordinate (or an equivalent product-preserving decomposition).

## 6. Application of a completed compatible peer result

The named partner for this slot is `account04/B01`. At the final pre-publication source check, that worker had created a QFORM login but had not yet published a completed QFORM handoff or mathematical report at its prescribed path. I therefore do not fabricate or attribute a partner theorem.

A completed compatible peer result was available from `account01/B11`: for two **physical independent coordinates**, every affine nondegenerate indefinite binary quadratic

`alpha X^2+2aXY+beta Y^2+rX+sY+c`, `D=a^2-alpha beta>0`,

has a universal `L^3` density bound `||p||_3 <= C_bin D^(-1/3)`.

Canonical source: `yspennstate/math-open-problems@2279571f59ade7a9ec478af1e4818f6c117ac224:proofnet24/QFORM-density/fleet-2026-09-22/account01/B11/QFORM-B11-20260922T121344Z/REPORT.md`.

Applying its inequality to an independent third square and using the same `L^(3/2)` square estimate gives the actual three-direction bound

`||p||_infinity <= 2 C_bin (D |d|)^(-1/3).`            (6.1)

Thus the current archive now controls two complementary rank-two endpoints by the same `L^3 * L^(3/2) -> L^infinity` mechanism:

- **fully localized physical binary plane:** (6.1), from account01/B11;
- **fully diffuse rotated two-frame, max leverage <=1/2:** (5.1), from this report.

The first essential missing implication is consequently sharper than before: obtain a determinant-scale `L^3` estimate for a **mixed-leverage rotated rank-two frame**, or find a product-preserving decomposition that combines the localized and diffuse mechanisms without a dimension-dependent loss. Once that rank-two interpolation is available, the remaining rank-three step is to couple it to the third spectral direction without falsely declaring post-rotation independence.

## 7. Relation to newer rank-three work

A contemporaneous rank-three conditional-subframe theorem (`account01/B02`) shows that failure of a diffuse rank-three certificate forces a bounded number of physical coordinates to carry a substantial fraction of one spectral direction. That is consistent with the residual identified above: the universal difficulty has moved into a finite-heavy/mixed-leverage interface rather than the already-controlled fully diffuse regime.

This report does **not** infer that the finite-heavy reduction itself closes the target, and it does not discard additional eigendirections of a higher-rank matrix.

## 8. Continuity, constants, and target status

- The rank-two theorem proves `L^p` densities for finite `p>2`; it does not assert rank-two `L^infinity` in the indefinite case.
- The rank-two-plus-independent-square corollary does give a bounded continuous density.
- The explicit diffuse constant in (5.1) is `<8.103` when `Delta|d|>=1`.
- The full universal three-large-eigenvalue conjecture remains **OPEN**.
- The separate full-target continuous-representative conclusion also remains **OPEN**.

## 9. Source pins and integrity

Fresh owner/control source before publication: `yspennstate/math-research-brain` owner revision `2026-09-22.5`.

Corrections consumed: baseline no-law-uniform-pointwise-decay, no-post-rotation-independence, fiber-sup dimension loss; plus `QFORM-CROSSMINOR-ALONE-FALSE`, `QFORM-UNIVERSAL-PI-FALSE-AND-DIFFUSE-BRANCH`, and `QFORM-TWOSHEET-XRAY-ONLY-FALSE`.

Primary proof dependency: `QFORM-DIFFUSE-SEPARABLE-PHASE-v1`, canonical report commit `773b7fb6f0e6a8142066f0bac08d228dfc164fdb`.

Completed compatible peer applied: account01/B11, canonical report commit `2279571f59ade7a9ec478af1e4818f6c117ac224`.

No credential, scheduler identifier, machine path, raw private transcript, email content, unrelated private data, public release, paid call, or workflow dispatch is included. Repository access in this run is not native learned-memory ingestion; execution status is `WITHOUT_VERIFIED_BRAIN`.
