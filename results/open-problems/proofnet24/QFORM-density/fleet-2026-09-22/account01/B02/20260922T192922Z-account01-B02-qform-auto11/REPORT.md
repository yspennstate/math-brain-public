SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account01, slot B02, 2026-09-22T19:29:22Z.
attacking: integrated Fourier / fractional-trace endpoint cascade; combine account02/B02's pair fractional-trace transducer with a product-preserving affine-hyperbolic residual, and remove the determinant loss from that branch.

# account01/B02 — sharp affine-hyperbolic fractional trace and determinant-free pair endpoint

Run: `20260922T192922Z-account01-B02-qform-auto11`.
Programme: `QFORM-DENSITY-3EIG-20260922`.
Status: **ESSENTIAL_STEP_APPLIED / FULL TARGET OPEN / WITHOUT_VERIFIED_BRAIN**.

## 1. Exact target and correction discipline

The target remains the full arbitrary-product-law conjecture: independent real coordinates `X_i` with one-dimensional probability densities bounded by one, arbitrary dimension, and arbitrary real symmetric `A` with at least three eigenvalues of modulus at least one. No Gaussian, moment, support, log-concavity, connected-support, diagonal-basis, or post-rotation-independence assumption is used.

I do not use the refuted law-uniform pointwise quadratic-phase decay, the arbitrary-joint rank-three coarea claim, the positive conditional-projection-density moment, a fixed-good-minor exhaustion, or the false same-square absorption step. The full unweighted criterion `integral |phi_Q(t)| dt < infinity` remains open; no target-valid counterexample to that stronger criterion is claimed here.

The useful route in this run is a direct fractional trace. It is compatible with the live correction `QFORM-ONE-HEAVY-ROW-SAME-SQUARE-ABSORPTION-FALSE-v1` because the hyperbolic variable below is genuinely affine on its own independent bank: no hidden `U`-dependent curvature is allowed inside `H`.

## 2. Source-pinned completed partner result actually applied

I apply the designated partner account02/B02 completed theorem `QFORM-PAIR-FRACTIONAL-TRACE-TRANSDUCER-v1`, source repository `yspennstate/math-open-problems`, commit `853a4e86c7ff9789891c473905eeb57b13f615ed`, path `proofnet24/QFORM-density/fleet-2026-09-22/account02/B02/20260922T190827Z-account02-B02-40617e89/REPORT.md`.

Let an invertible indefinite original-coordinate physical pair have principal block `B`, put `D=|det B|`, `kappa=sigma_min(B)`, and after completing that pair let `R` denote the residual scalar random variable, with arbitrary residual-dependent translation of the pair permitted. For `H_alpha(R)=sup_s E |R-s|^(-alpha)`, `0<alpha<=1/2`, account02/B02 proves

`||p_Q||_infinity <= C_alpha D^(alpha-1/2) kappa^(-alpha) H_alpha(R)`,       (2.1)

where `C_alpha = 2^alpha exp(-1+2sqrt(2)alpha)/alpha` for `0<alpha<=1/(2sqrt(2))`, and `C_alpha=2^(alpha+3/2)` for `1/(2sqrt(2))<=alpha<=1/2`. In particular

`||p_Q||_infinity <=4 kappa^(-1/2) H_(1/2)(R)`.                            (2.2)

The main point of the present run is that exact product provenance gives a sharper fractional trace directly, including the critical half-Riesz endpoint.

## 3. Sharp one-dimensional bathtub potential

### Lemma 3.1

Let `Y` be a real random variable with probability density `g` satisfying `0<=g<=M`, and let `0<alpha<1`. Then

`sup_c E |Y-c|^(-alpha) <= [2^alpha/(1-alpha)] M^alpha`.                    (3.1)

The constant is sharp.

### Proof

For fixed `c`, the kernel `|y-c|^(-alpha)` is symmetric decreasing about `c`. Among densities of mass one and cap `M`, the bathtub/rearrangement principle puts all available mass at height `M` on the centered interval of length `1/M`. Therefore

`E |Y-c|^(-alpha)`
` <= M int_{-1/(2M)}^(1/(2M)) |u|^(-alpha) du`
` = [2^alpha/(1-alpha)] M^alpha`.

Equality holds for the uniform density `M 1_{[-1/(2M),1/(2M)]}` at `c=0`. For a cap-one probability density `f`, this gives

`E |X|^(-alpha) <= 2^alpha/(1-alpha)`.                                  (3.2)

## 4. New theorem: sharp affine-hyperbolic fractional trace

### Theorem 4.1 — `QFORM-AFFINE-HYPERBOLIC-FRACTIONAL-TRACE-SHARP-v1`

Let `X,U` be independent real random variables, let `V` be any further random element independent of `(X,U)`, and assume `X` has a probability density bounded by one, `U` has a probability density bounded by `M`, `a!=0`, and `H(x,v)` is arbitrary measurable and has no `U` dependence. Put

`R=2 a X U + H(X,V)`.                                                   (4.1)

Then for every `0<alpha<1`,

`H_alpha(R) <= [2^alpha/(1-alpha)^2] (M/|a|)^alpha`.                    (4.2)

The numerical constant in (4.2) is sharp within this class.

### Proof

Fix a target value `s`. Condition on `(X,V)=(x,v)`. For `x!=0`, Lemma 3.1 and scaling give

`E_U |2 a x U + H(x,v)-s|^(-alpha)`
` <= |2ax|^(-alpha) [2^alpha/(1-alpha)] M^alpha`
` = [M^alpha/((1-alpha)|a|^alpha)] |x|^(-alpha)`.                 (4.3)

The set `x=0` has probability zero because `X` has a density. Average (4.3) over `(X,V)` and use (3.2):

`E |R-s|^(-alpha)`
` <= [2^alpha/(1-alpha)^2](M/|a|)^alpha`.

This is uniform in `s`, proving (4.2).

For sharpness take `X~Uniform[-1/2,1/2]`, `U~Uniform[-1/(2M),1/(2M)]` with density `M`, `H=0`, `s=0`. Independence and exact evaluation give equality in (4.2).

At `alpha=1/2`,

`H_(1/2)(R) <= 4sqrt(2) sqrt(M/|a|)`.                                  (4.4)

This is finite precisely because the `U` bank is genuinely affine and independent. It does not contradict the live same-square correction: if `U^2` or other `U`-curvature is hidden inside `H`, the conditioning argument is invalid and the half-Riesz endpoint can diverge.

## 5. Main partner cascade: the pair determinant disappears at the endpoint

Combine Theorem 4.1 with the account02/B02 partner theorem (2.1).

### Theorem 5.1 — `QFORM-PAIR-HYPERBOLIC-FRACTIONAL-CASCADE-v1`

Under the pair hypotheses of (2.1), assume the completed Schur residual has the exact product-preserving form `R=2aXU+H(X,V)` from Theorem 4.1. Then for every `0<alpha<=1/2`,

`||p_Q||_infinity <= A_alpha D^(alpha-1/2) kappa^(-alpha) (M/|a|)^alpha`,  (5.1)

where `A_alpha = C_alpha 2^alpha/(1-alpha)^2`. At the critical endpoint `alpha=1/2`,

`||p_Q||_infinity <= 16sqrt(2) sqrt(M/(kappa |a|))`.                    (5.2)

The determinant `D=|det B|` has vanished completely.

At `alpha=1/4`, the exact coefficient is

`(64sqrt(2)/9) exp(-1+1/sqrt(2)) < 7.504`,

so

`||p_Q||_infinity < 7.504 D^(-1/4) kappa^(-1/4)(M/|a|)^(1/4)`.          (5.3)

This improves the previous partner coefficient `14.197` in the same exact product-hyperbolic branch.

The structural gain in (5.2) is significant: the incoming partner state required a lower bound on `D*kappa*|a|/M`; the critical endpoint requires only `kappa*|a|/M`. A tiny pair determinant no longer has to be paid if the residual contains a genuine affine hyperbolic packet.

## 6. Immediate improvement of the square-plus-one-hyperbolic branch

The completed account03/B02 theorem at commit `056867164c939f4e70988e762258f2542e32fd75` proved, for

`Q=d(Z+eta(X,U,V))^2 + 2aXU + H(X,V)`,

with `Z,X,U` mutually independent, `V` independent of them, cap-one `Z,X`, cap-`M` `U`, and no hidden `U`-curvature in `H`, the bound `||p_Q||_infinity <=8sqrt(2) sqrt(M/(|ad|))`.

Its valid square-fiber estimate is

`p_Q(y)<=|d|^(-1/2) H_(1/2)(R)`.                                  (6.1)

Substituting the sharp endpoint (4.4) improves that result to

`||p_Q||_infinity <=4sqrt(2) sqrt(M/(|a d|))`.                         (6.2)

No new independence is assumed: the completed-square shift `eta` may depend arbitrarily on `(X,U,V)` because it disappears inside the uniform square-fiber bound. Only the residual affine-bank condition already required by the fresh correction remains.

If `U=cY+U_0` with `Y` an original cap-one coordinate independent of `U_0` and of the other active banks, then conditioning on `U_0` gives `M<=1/|c|`, so

`||p_Q||_infinity <=16sqrt(2)/sqrt(kappa |a c|)`                      (6.3)

for the pair-hyperbolic branch and

`||p_Q||_infinity <=4sqrt(2)/sqrt(|a d c|)`                           (6.4)

for the square-hyperbolic branch.

## 7. Integrated Fourier consequence actually obtained

The assignment asks first for an unweighted `L^1_t` characteristic-function estimate. I do not have a source-valid proof or counterexample for that target-wide stronger criterion in this run. The new endpoint nevertheless gives a genuine integrated Fourier estimate on the paid branch.

For `phi_Q(t)=int exp(itx) p_Q(x) dx`, Plancherel gives

`int_R |phi_Q(t)|^2 dt =2pi ||p_Q||_2^2 <=2pi ||p_Q||_infinity`,           (7.1)

because `p_Q` has mass one. Hence Theorem 5.1 implies

`int |phi_Q(t)|^2 dt <=32pi sqrt(2) sqrt(M/(kappa |a|))`.                 (7.2)

Similarly, the improved square branch (6.2) gives

`int |phi_Q(t)|^2 dt <=8pi sqrt(2) sqrt(M/(|ad|))`.                       (7.3)

These are `L^2_t`, not `L^1_t`, estimates and therefore do not by themselves prove continuity. Essential boundedness is proved on the stated branches; continuity is not established by the present argument.

## 8. Compact conditional end-to-end argument and first unpaid implication

A valid end-to-end closure would now be:

1. Apply the surviving full-matrix structural decomposition under `s_3(A)>=1`.
2. Route already-paid diffuse/ridge/exact-cross/physical-pivot/zero-internal branches to their completed theorems.
3. In any residual state exposing an invertible indefinite physical pair `B` and a genuinely affine product hyperbolic packet in its physical Schur residual, use (5.2). It is enough to force the scale-free lower bound `kappa|a|/M>=c_0>0`; the pair determinant is no longer part of this branch's structural debt.
4. If instead a scalar square pivot and one affine hyperbolic packet are exposed, use (6.2), requiring only `|ad|/M>=c_1>0`.

Thus the first unpaid implication for this B02 route is now strictly weaker than in the incoming account02/B02 state:

`QFORM-PAIR-HYPERBOLIC-ENDPOINT-EXTRACTION-v1` (OPEN): from the surviving O0/O1/O2/O3 aggregate geometry, force either an already-paid branch, or a product-preserving indefinite physical pair plus affine hyperbolic residual with `kappa|a|/M` universally bounded below, or a scalar-square plus affine-hyperbolic packet with `|ad|/M` universally bounded below.

The determinant factor `D` is not required in the first alternative. The remaining problem is structural extraction while preserving disjoint original-coordinate product provenance; raw cross rows are not automatically principal pairs and an orthogonal residual is not automatically a physical Schur complement.

## 9. Status and scope

- `QFORM-AFFINE-HYPERBOLIC-FRACTIONAL-TRACE-SHARP-v1`: **PROVED**, with sharp constant.
- `QFORM-PAIR-HYPERBOLIC-FRACTIONAL-CASCADE-v1`: **PROVED**, by actual application of the completed account02/B02 partner theorem.
- Determinant-free endpoint (5.2): **PROVED** in its exact product-preserving branch.
- account03/B02 square-plus-hyperbolic constant improved from `8sqrt(2)` to `4sqrt(2)` under the same corrected hypotheses.
- Essential bounded density: **PROVED only on the stated branches**.
- Continuous density: **NOT PROVED by this run**.
- Universal unweighted `integral |phi_Q|`: **OPEN; no valid counterexample produced**.
- Full QFORM conjecture: **OPEN / NOT PROVED / NOT DISPROVED**.

No numerical simulation is used as proof. All estimates are exact one-dimensional rearrangement, conditioning, and the source-pinned completed account02/B02 transducer.