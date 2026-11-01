# fleet01/B08 — fractional-frame Brascamp–Lieb certificate for diffuse/heavy mixtures

**Run:** `20260922T133421Z-fleet01-B08-qform-r12`  
**Programme:** `QFORM-DENSITY-3EIG-20260922`, owner revision `2026-09-22.5`  
**Assignment:** diffuse eigenvector case  
**Classification:** `ESSENTIAL_STEP_APPLIED / QFORM-FRACTIONAL-FRAME-BL-v1`  
**Execution:** `WITHOUT_VERIFIED_BRAIN`; `full_brain_connected=false`  
**Full conjecture:** **OPEN / NOT PROVED / NOT DISPROVED**.

## 1. Exact scope and dependencies

The target is: for independent real `X_i` with densities `0<=f_i<=1` and symmetric `A` having at least three eigenvalues of absolute value at least one, prove a universal `L^infinity` bound for the density of `X^T A X`, with continuity tracked separately.

Fresh source control was read from `yspennstate/math-research-brain` main at commit `b68908e363f0ce9338a1cdf1996653ae5f699876`, owner revision `2026-09-22.5`. The live corrections consumed include the false law-uniform pointwise Fresnel decay, fiber-sup dimension loss, loss of independence after rotation, `QFORM-CROSSMINOR-ALONE-FALSE`, `QFORM-UV-CONDITIONAL-CAP-FALSE`, `QFORM-CONDITIONAL-CAP-NOT-INDEPENDENCE-v1`, and `QFORM-LOCAL-CROSS-RANK3-DICHOTOMY-FALSE`. None is used as a premise.

The named partner result actually applied is fleet02/B08 `QFORM-WHITENED-PHYSICAL-BLOCK-v1`, canonical report

`yspennstate/math-open-problems@84657e690f8411d99602ddc772b622686c3874ed:proofnet24/QFORM-density/fleet-2026-09-22/fleet02/B08/B08-20260922T124007Z-r11/REPORT.md`.

That theorem proves the principal-block estimate when the whitened row leverages themselves are all at most `1/2`. The present argument keeps the same whitening/conditioning mechanism but replaces the canonical leverage weights by a different half-capped isotropic weighting. This strictly enlarges the certified class.

## 2. Conditional end-to-end route

For a physical coordinate block `I`, suppose

`A_{I,I}=D+R Lambda R^T`,

with `D` diagonal, `R` full column rank `r>=3`, and `Lambda` real symmetric invertible. Put

`M=R^T R`, `W=R M^(-1/2)`,

so `W^T W=I_r`. Conditioning on `X_{I^c}` turns all outside and cross-block contributions into coordinate-separable linear potentials, while `D` is already coordinate-separable. Thus it is enough to control

`Y=(W^T X_I)^T B (W^T X_I)+sum_i V_i(X_i)`,

where `B=M^(1/2) Lambda M^(1/2)` and the `V_i` are arbitrary measurable real functions finite almost surely.

The first missing implication in the previous partner theorem was that one particular row leverage `c_i=||w_i||^2` larger than `1/2` prevents the canonical Brascamp–Lieb/Hausdorff–Young choice. The key observation below is that the Brascamp–Lieb weights need not equal the canonical leverages if the normalized row directions admit another isotropic decomposition.

## 3. Main theorem: half-capped fractional frame scaling

### Theorem 3.1 — `QFORM-FRACTIONAL-FRAME-BL-v1`

Let `W` be an `m x r` real matrix with orthonormal columns, `r>=3`. For every nonzero row `w_i`, set

`c_i=||w_i||^2`, `v_i=w_i/sqrt(c_i)`.

Assume there exist numbers `theta_i in [0,1/2]` such that rows with `theta_i>0` have `c_i>0` and

`sum_i theta_i v_i v_i^T = I_r`.                                            (3.1)

Define

`B_theta(W) = product_{theta_i>0} [ (theta_i/c_i)^(theta_i) (1-theta_i)^(-(1-theta_i)) ]^(1/2)`.   (3.2)

Let `X_i` be independent real variables with densities `0<=f_i<=1`, let `V_i` be arbitrary measurable real functions, and let `Lambda` be any real symmetric invertible `r x r` matrix. Then

`T=(W^T X)^T Lambda (W^T X)+sum_i V_i(X_i)`

has a bounded continuous density and

`||p_T||_infinity <= [r/(r-2)] B_theta(W)^(2/r) |det Lambda|^(-1/r)`.          (3.3)

More generally, for the physical block `D+R Lambda R^T` above,

`||p_Q||_infinity <= [r/(r-2)] B_theta(W)^(2/r) [det(M)|det Lambda|]^(-1/r)`,  (3.4)

uniformly over arbitrary outside blocks and cross couplings.

### Proof

Fix the Fourier variable `t`. Absorb every coordinate-separable term into

`h_{i,t}(x)=f_i(x) exp(i t V_i(x))`.

Then `|h_{i,t}|=f_i`, `||h_{i,t}||_1=1`, and `||h_{i,t}||_q<=1` for every `q>=1` because `0<=f_i<=1`.

Let `g_t` be the (possibly complex) pushforward density of the product amplitude `prod_i h_{i,t}` under `x -> W^T x`. As in the reviewed partner theorem,

`hat g_t(xi)=product_i hat h_{i,t}(w_i dot xi)`.

For `theta_i=0`, use `|hat h_{i,t}|<=||h_{i,t}||_1=1` and discard that factor. For `theta_i>0`, write `w_i=sqrt(c_i) v_i`. The rank-one geometric Brascamp–Lieb inequality applied to (3.1) gives

`||hat g_t||_1`
` <= product_i [ int_R |hat h_{i,t}(sqrt(c_i) s)|^(1/theta_i) ds ]^(theta_i)`
` = product_i c_i^(-theta_i/2) ||hat h_{i,t}||_{1/theta_i}`.                 (3.5)

Because `theta_i<=1/2`, `p_i=1/theta_i>=2`; its conjugate exponent is `q_i=1/(1-theta_i)<=2`. Sharp Hausdorff–Young, with Fourier convention `hat h(xi)=int e^{-i xi x}h(x)dx`, yields

`||hat h_{i,t}||_{1/theta_i}`
` <= (2pi)^(theta_i) theta_i^(theta_i/2) (1-theta_i)^(-(1-theta_i)/2) ||h_{i,t}||_{1/(1-theta_i)}`
` <= (2pi)^(theta_i) theta_i^(theta_i/2) (1-theta_i)^(-(1-theta_i)/2)`.      (3.6)

Taking traces in (3.1) gives `sum_i theta_i=r`. Multiplying (3.5)-(3.6),

`||hat g_t||_1 <= (2pi)^r B_theta(W)`.                                      (3.7)

The Gaussian-regularized Fresnel inversion used in the independently reviewed separable-phase proof is therefore unchanged except for replacing the old entropy factor by `B_theta(W)`. Consequently

`|phi_T(t)| <= min(1, pi^(r/2) B_theta(W) |det Lambda|^(-1/2) |t|^(-r/2))`.  (3.8)

The right side is integrable for `r>2`. Setting

`T_0=pi B_theta(W)^(2/r)|det Lambda|^(-1/r)`

and integrating the two pieces exactly gives

`(1/(2pi)) int_R |phi_T(t)| dt`
` <= [r/(r-2)] B_theta(W)^(2/r)|det Lambda|^(-1/r)`,

which proves (3.3). Since `phi_T in L^1`, Fourier inversion gives a bounded continuous density vanishing at infinity.

For a nonorthonormal physical factor `R`, whiten exactly as in fleet02/B08: `R=W M^(1/2)` and replace `Lambda` by `M^(1/2)Lambda M^(1/2)`, whose determinant has absolute value `det(M)|det Lambda|`. Conditioning on outside original coordinates only creates linear coordinate-separable phases, so the same bound is uniform in the conditioning value. Averaging proves (3.4) and continuity. `QED`.

## 4. Entropy/KL form of the certificate

The new factor has a useful information-theoretic upper bound. Put

`p_i=theta_i/r`, `q_i=c_i/r`.

Both are probability vectors because `sum theta_i=sum c_i=r`. From `-(1-theta)log(1-theta)<=theta`,

`log B_theta(W)`
` <= (1/2) sum_i theta_i log(theta_i/c_i) + r/2`
` = (r/2) [ D(p||q)+1 ]`.

Hence

`||p_T||_infinity <= [e r/(r-2)] exp(D(p||q)) |det Lambda|^(-1/r)`.          (4.1)

Thus the canonical leverage condition `c_i<=1/2` is only the zero-relative-entropy choice `theta_i=c_i`; more generally, any half-capped isotropic reweighting at bounded KL cost gives a dimension-free certificate.

When `theta_i=c_i`, formula (3.2) reduces exactly to the partner factor

`B(W)=product_i (1-c_i)^(-(1-c_i)/2)`,

so Theorem 3.1 strictly contains `QFORM-WHITENED-PHYSICAL-BLOCK-v1` on its common scope.

## 5. Exact heavy-row example missed by both canonical diffuse tests

Take `r=3`, `m=6`, and rows

`w_1=sqrt(4/5)e_1`, `w_2=sqrt(1/5)e_1`,
`w_3=w_4=(1/sqrt2)e_2`,
`w_5=w_6=(1/sqrt2)e_3`.

Then `W^T W=I_3` but `c_1=4/5>1/2`, so the unconditioned partner theorem does not apply. If one conditions the heavy coordinate `1`, then

`M=I-w_1w_1^T=diag(1/5,1,1)`

and the residual whitened leverage of row `2` is exactly

`(1/5)/(1/5)=1`,

so the partner's one-heavy-row corollary also does not apply.

Nevertheless set

`theta_1=...=theta_6=1/2`.

The normalized row directions are `e_1,e_1,e_2,e_2,e_3,e_3`, hence

`sum_i theta_i v_i v_i^T=I_3`.

Moreover

`product_i c_i=(4/5)(1/5)(1/2)^4=1/100`,

and because every `theta_i=1/2`, (3.2) gives

`B_theta(W)=(product_i c_i)^(-1/4)=sqrt(10)`.

Therefore for arbitrary independent input densities bounded by one, arbitrary coordinate-separable perturbations, and every symmetric invertible `Lambda`,

`||p_T||_infinity <= 3 * 10^(1/3) * |det Lambda|^(-1/3) < 6.464 |det Lambda|^(-1/3)`.   (5.1)

In particular if the three eigenvalues have absolute value at least one, the density bound is `<6.464` on this genuinely heavy/diffuse mixed frame. The density is continuous. This is a strict extension of both canonical diffuse checks, not a relabeling of the same hypothesis.

## 6. What this does and does not solve

This theorem remains a supporting branch, not the full target. It handles arbitrary diagonal/separable terms and arbitrary outside/cross couplings once a physical low-rank factorization has a whitened frame admitting (3.1). It does **not** absorb a genuinely off-diagonal residual inside the same physical block. Therefore it does not by itself treat an arbitrary spectral split

`A=U Lambda U^T + C`, `CU=0`,

when `C` is nonseparable on the chosen coordinates.

The first new unpaid implication is:

**`QFORM-FRACTIONAL-SCALING-OR-LOCALIZATION-v1`.** Prove a dimension-free structural dichotomy for the large-eigenvector frame: either a localized-coordinate mechanism controls the form, or after a permitted physical conditioning/whitening there exists a half-capped isotropic scaling `theta` satisfying (3.1) with bounded `D(theta/r || c/r)`; then combine this with the full-spectrum cross-block determinant theorem to absorb the nonseparable remainder. A counterexample frame showing that every such scaling has unbounded entropy cost would also be decisive for this route.

The recently supplied regularized cross-block determinant theorem retains arbitrary self blocks and small eigenvalues, so the natural next attempt is to use the fractional scaling certificate on the large spectral frame to manufacture a coordinate partition with three controlled cross directions, rather than demanding a rank-three cross block from a single local cut. The live correction `QFORM-LOCAL-CROSS-RANK3-DICHOTOMY-FALSE` shows why this must be an aggregated/fractional construction.

## 7. Verification notes

The heavy-row example was checked exactly: `W^T W=I_3`; the alternative weights give `sum theta_i v_i v_i^T=I_3`; after conditioning row one the residual whitened leverage of row two is `1`; `product c_i=1/100`; and the displayed constant is `3*10^(1/3)`.

No Monte Carlo or asymptotic heuristic is used. No pointwise law-uniform one-dimensional oscillatory decay is asserted. No independence after spectral rotation is asserted. The output is a proved scoped theorem with continuity, not a full solution of QFORM.
