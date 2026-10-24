# account01/B08 — diffuse eigenvector case: separable-phase Fourier–Brascamp–Lieb extension

**Run:** `20260922T114116Z-account01-B08-qform-r11`  
**Programme:** `QFORM-DENSITY-3EIG-20260922`, owner revision `2026-09-22.5`  
**Assignment:** diffuse eigenvector case  
**Outcome:** `ESSENTIAL_STEP_APPLIED / DIFFUSE-SEPARABLE-PHASE-CERTIFICATE`  
**Execution:** `WITHOUT_VERIFIED_BRAIN`; `full_brain_connected=false`  
**Full conjecture:** **OPEN / NOT PROVED / NOT DISPROVED**.

## 1. Fresh state and dependencies

The current owner order supersedes FEI and every earlier research assignment. The target is the universal bounded-density conjecture for `Q=X^TAX` with independent coordinate densities `0<=f_i<=1` and at least three eigenvalues of `A` of magnitude at least one.

Current source control used before publication: `yspennstate/math-research-brain@fdd695485b7ac3ec1371ae2f9111f2821dee39eb`, owner revision `2026-09-22.5`. The current corrections are respected: law-uniform pointwise one-dimensional Fresnel decay is false; a two-dimensional spectral-fiber supremum can lose dimension; and diagonalizing `A` does not preserve independence.

Named partner result actually consumed and extended: account02/B08, `QFORM-DIFFUSE-RANK3-BL-v1`, canonical report `yspennstate/math-open-problems@0b5925a458d36c1ec1cf8ab344c9676260a97c8a`, path `proofnet24/QFORM-density/fleet-2026-09-22/account02/B08/B08-20260922T113624Z-qform11/REPORT.md`. That report proves the exact-rank diffuse theorem with constant `3e` using sharp Hausdorff–Young, geometric rank-one Brascamp–Lieb, and Fresnel inversion.

A second OTHER-account dependency used as a stress test is account02/B05, `yspennstate/math-open-problems@63ae1057b5ad8a5bc3c764d733de79e5c917b752`, path `proofnet24/QFORM-density/fleet-2026-09-22/account02/B05/20260922T112240Z-b05-qform-9d86c905/REPORT.md`. It proves that taking a spectral-fiber amplitude supremum can lose a factor `Theta(n)` and records the diffuse Walsh obstruction to fixed-size coordinate extraction.

The pointwise-decay correction and the complete diagonal `C=pi` theorem are independently available from account03/B17 at `yspennstate/math-open-problems@c64fcff680b0a252a3c92002c60eedba02bbb9ec`, path `qform/fleet-2026-09-22/account03/B17/account03-B17-20260922T112131Z/REPORT.md`.

Classical analytic inputs:

- William Beckner, *Inequalities in Fourier Analysis on R^n*, Proc. Natl. Acad. Sci. USA 72 (1975), 638–641, DOI `10.1073/pnas.72.2.638`: sharp Hausdorff–Young.
- H. J. Brascamp and E. H. Lieb, *Best constants in Young's inequality, its converse, and its generalization to more than three functions*, Adv. Math. 20 (1976), 151–173, DOI `10.1016/0001-8708(76)90184-5`: the rank-one geometric Brascamp–Lieb inequality used below.

## 2. New theorem

### Theorem `QFORM-DIFFUSE-SEPARABLE-PHASE-v1`

Let `X_1,...,X_n` be independent real random variables with probability densities `f_i` satisfying `0<=f_i<=1`. Let `U in R^{n x k}` have orthonormal columns, write `u_i^T` for row `i`, and set

`c_i=||u_i||_2^2`.

Assume

`k>=3`, `c_i<=1/2` for every `i`,

and let `Lambda=diag(lambda_1,...,lambda_k)` with `|lambda_j|>=1`. Let `V_i:R->R` be arbitrary measurable functions. Then

`Y = sum_i V_i(X_i) + (U^T X)^T Lambda (U^T X)`

has a bounded continuous density and

`||p_Y||_infinity <= e k/(k-2) <= 3e`.

In particular, every quadratic form

`A = D + U Lambda U^T`

with `D` diagonal and the above diffuse-frame conditions satisfies the same universal density bound, with no restriction on the diagonal entries of `D`.

The case `V_i=0` recovers the partner's exact-rank theorem. The extension to arbitrary coordinate-separable phases is the new point of this report.

## 3. Proof

Fix `t in R`. Absorb the separable perturbation into one-dimensional complex amplitudes

`a_{i,t}(x)=f_i(x) exp(i t V_i(x))`.

Then

`|a_{i,t}(x)|=f_i(x)`, `||a_{i,t}||_1=1`, and `||a_{i,t}||_p<=1` for every `p>=1`.

Let `mu_t` be the pushforward under `x -> U^T x` of the finite complex measure with density `prod_i a_{i,t}(x_i)`. Its Fourier transform factorizes exactly:

`hat mu_t(xi)=prod_i hat a_{i,t}(<u_i,xi>)`.

Ignore zero rows. Put `v_i=u_i/sqrt(c_i)`. Since `U^TU=I_k`,

`sum_i c_i v_i v_i^T=I_k`, `sum_i c_i=k`.

For each row set `q_i=1/c_i>=2` and `p_i=q_i/(q_i-1)=1/(1-c_i) in [1,2]`. The sharp one-dimensional Hausdorff–Young inequality in the convention

`hat a(s)=int exp(-isx)a(x)dx`

gives

`||hat a_{i,t}||_{q_i}
 <= (2pi)^{c_i}(1-c_i)^{-(1-c_i)/2} c_i^{c_i/2} ||a_{i,t}||_{p_i}`

and therefore, because `||a_{i,t}||_{p_i}<=1`,

`||hat a_{i,t}||_{q_i}
 <= (2pi)^{c_i}(1-c_i)^{-(1-c_i)/2} c_i^{c_i/2}.`                 `(3.1)`

Apply the geometric rank-one Brascamp–Lieb inequality to

`h_i(s)=|hat a_{i,t}(sqrt(c_i)s)|^{1/c_i}`.

It yields

`||hat mu_t||_1
 <= prod_i c_i^{-c_i/2} ||hat a_{i,t}||_{1/c_i}`

`<= (2pi)^k prod_i (1-c_i)^{-(1-c_i)/2}.`                       `(3.2)`

For `0<=c<1`,

`-(1-c)log(1-c)<=c`.

Using `sum_i c_i=k` in (3.2),

`boxed{ ||hat mu_t||_1 <= (2pi)^k e^{k/2}. }`                    `(3.3)`

This bound is uniform in `t`, in all measurable `V_i`, in `n`, and in the input laws. The key observation is that multiplication by the coordinate phase `exp(itV_i)` changes none of the one-dimensional `L^p` norms needed by Hausdorff–Young.

Because the Fourier transform of the finite complex measure `mu_t` is integrable, `mu_t` has a bounded continuous density `g_t`. The characteristic function of `Y` is

`phi_Y(t)=int_{R^k} exp(it z^T Lambda z) g_t(z) dz`.              `(3.4)`

For rigor, multiply the integrand by `exp(-epsilon |z|^2)` and use Fourier inversion for `g_t`. The resulting Fresnel-Gaussian kernel has modulus bounded by

`pi^{k/2}|t|^{-k/2}|det Lambda|^{-1/2}
 <= pi^{k/2}|t|^{-k/2}`.                                         `(3.5)`

Combining (3.3) with (3.5), then taking `epsilon downarrow0`, gives

`boxed{ |phi_Y(t)| <= (pi e/|t|)^{k/2}. }`                       `(3.6)`

Together with `|phi_Y(t)|<=1`,

`|phi_Y(t)|<=min(1,(pi e/|t|)^{k/2}).`                           `(3.7)`

For `k>=3` this is integrable. The crossover is `t_0=pi e`, and

`int_0^infinity |phi_Y(t)|dt
 <= pi e + (pi e)^{k/2} int_{pi e}^infinity t^{-k/2}dt`

`= pi e [1+2/(k-2)] = pi e k/(k-2).`                             `(3.8)`

Hence

`||phi_Y||_1 <= 2 pi e k/(k-2)`

and Fourier inversion gives a bounded continuous density satisfying

`boxed{ ||p_Y||_infinity <= e k/(k-2) <= 3e. }`                  `(3.9)`

This proves the theorem.

## 4. Exact quadratic corollary and diffuse stress test

Taking `V_i(x)=d_i x^2` proves the stated matrix corollary for

`A=D+U Lambda U^T`

with arbitrary diagonal `D`. Thus diagonal residual curvature, including indefinite or very large diagonal terms, costs nothing in this diffuse Fourier–Brascamp–Lieb argument.

The theorem directly handles the Walsh rank-three stress family recorded by account02/B05/account02-B07. If the three orthonormal eigenvectors have entries of modulus `1/sqrt(n)`, then every row leverage is

`c_i=3/n`.

For `n>=6`, `c_i<=1/2`, so with three eigenvalues of magnitude at least one the exact rank-three form has

`||p_Q||_infinity<=3e`.

This demonstrates a genuinely global aggregation mechanism: every fixed-size coordinate compression can be tiny while the output density remains uniformly controlled. It avoids the `Theta(n)` fiber-supremum loss because it never replaces the product density by a fiberwise supremum.

## 5. Why this does not prove the full conjecture

Given an arbitrary target matrix, choose three large eigenvectors and write spectrally

`A=U Lambda U^T + C`, `CU=0`.

Even if `U` is diffuse, the residual term `x^T Cx` is generally **not** coordinate-separable. Absorbing it into the amplitude creates

`exp(it x^T Cx) prod_i f_i(x_i)`,

whose projection Fourier transform no longer factorizes into one-dimensional factors. Therefore (3.2) cannot be applied. Treating `x^TCx` as independent noise is also invalid after rotation.

The theorem closes the exact-rank diffuse branch and, more strongly, all diffuse low-rank-plus-diagonal/separable perturbations. It does not close an arbitrary spectral complement.

## 6. First essential unpaid implication

`QFORM-DIFFUSE-RESIDUAL-COUPLING-v1`:

> Let `A=U Lambda U^T+C` with `U^TU=I_k`, `k>=3`, `max_i ||u_i||^2<=1/2`, `|lambda_j|>=1`, and `CU=0`. Prove a dimension-free replacement for (3.3) or an equivalent small-ball/coarea inequality that survives the nonseparable residual phase `exp(itx^TCx)`, uniformly over arbitrary symmetric `C` on `range(U)^perp`.

A proof of this implication, together with a localized/heavy-row mechanism for `max_i||u_i||^2>1/2`, would bridge the present diffuse theorem toward the full conjecture. The exact-rank heavy/light problem identified by account02/B08 remains a separate geometric boundary.

## 7. Status

This is a rigorous supporting theorem with an explicit universal constant. It uses the partner result in an actual derivation and strengthens its scope from exact-rank forms to arbitrary coordinate-separable perturbations. It is **not** a proof of the full conjecture, and no statement here promotes full target status.
