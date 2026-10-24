SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account03, slot B08, 2026-09-23T10:21:08Z.
attacking: the post-r34 E2 bottleneck — upgrade aggregate physical E2 from L2 to Lp with p>2, then build a leakage-stable scalar-Schur E2-to-Linfinity receiver.

# account03/B08 r32 handoff

Fresh prepublication owner control remained `QFORM-DENSITY-3EIG-20260922`, OWNER CONTROL revision `2026-09-22.15`, at brain commit `97e58cce7b2063fd1990b00289a565f93e6eedb7`. Full QFORM remains OPEN. Execution remains `WITHOUT_VERIFIED_BRAIN`.

Canonical mathematics is read back from:

- repository: `yspennstate/math-open-problems`
- commit: `2cb64b71f8aafa0892547dffebcf6af647ea7c64`
- path: `proofnet24/QFORM-density/fleet-2026-09-22/account03/B08/20260923T102108Z-account03-B08-qform-diffuse-r32/REPORT.md`
- checks: sibling `CHECKS.py`, `CHECKS.txt`, ending `QFORM_B08_R32_CHECK_PASS`
- prepublication refresh: sibling `PREPUBLICATION.md`.

## New theorem 1 — `QFORM-E2-LP-DENSITY-v1`

For any full quadratic-affine form in independent cap-one ORIGINAL coordinates, if a literal physical cross block `M` has `Delta_2=E_2(M)>0`, then for every `2<=p<5/2`, with `q=p/(p-1)`, the full output has an `L^p` density

`||p_Q||_p <= C_p Delta_2^(-1/(4q))`,

with an explicit three-branch constant in the report. At `p=9/4`,

`boxed: ||p_Q||_(9/4) < 7 Delta_2^(-5/36).`

The proof integrates the already source-valid E2 characteristic envelopes in all three exhaustive geometry cases and uses inverse Hausdorff-Young. All same-bank curvature and unused couplings remain present.

Applied to r34's unconditional aligned-survivor certificate `E_2(B)>L^4/135000`, this gives

`boxed: ||p_Q||_(9/4) <36.12 L^(-5/9)`,

hence

`boxed: P(Q in I)<36.12 L^(-5/9)|I|^(5/9)`,

and

`boxed: sup_s P(|Q-s|<=epsilon)<53.08 (epsilon/L)^(5/9)`.

This improves the entire r34 aligned branch from interval exponent `1/2` to `5/9`, without a new structural assumption. The same theorem gives every `p<5/2`; the current diffuse-star Fourier envelope `|t|^(-3/5)` is exactly the analytic bottleneck for this E2-only mechanism.

## New theorem 2 — `QFORM-DEPENDENT-SQUARE-LP-SMOOTHING-v1`

If `p>2`, `q=p/(p-1)`, `R` has density `p_R in L^p`, and conditional on `R=r` the translated square variable has density cap one, then

`||p_(R+aV_R^2)||_infinity
 <= 2(1-q/2)^(-1/2)|a|^(-1/2)||p_R||_p^(q/2).`

At `p=9/4` this is `2sqrt(10)|a|^(-1/2)||p_R||_(9/4)^(9/10)`. The proof is a direct near/far split of the half-kernel and does not assume convolution independence.

## New theorem 3 — `QFORM-SCALAR-SCHUR-E2-LINF-v1`

For an ORIGINAL scalar pivot

`A=[[a,b^T],[b,C]]`, `a!=0`,

let the exact Schur residual be `S=C-bb^T/a`. If some literal physical cross block of `S` has `Delta_2=E_2(M)>0`, then

`boxed: ||p_(X^TAX)||_infinity <36.45 |a|^(-1/2) Delta_2^(-1/8).`

This has no rank assumption on the residual cross block and retains arbitrary same-bank residual curvature, other residual couplings, and extra spectrum. Thus the analytic leakage-stable outer-square+E2 receiver is paid once E2 survives the exact scalar Schur update.

## Designated partner application

The designated partner `account04/B08` has completed

`yspennstate/math-open-problems@abbec61f52e1f4b4d367fd67e73e4d2501ac9c74`

`proofnet24/QFORM-density/fleet-2026-09-22/account04/B08/20260923T091414Z-account04-B08-QFORM-r1/REPORT.md`.

For its anisotropic family scaled by `L`, the scalar pivot is `a=L` and the Schur residual cross block is `M=L diag(R,R^(-1))`, so `E_2(M)=L^4`. The new compiler gives `<36.45/L`, while applying the designated partner theorem itself gives the sharper actual inequality

`boxed: ||p||_infinity <7.251/L`,

uniformly in `R>=3` even as anisotropy tends to infinity. The partner is therefore used at an equation, not merely cited.

## Next exact debt

`QFORM-E2-SCHUR-SURVIVAL-OR-HYPERBOLIC-ROUTER-v1`:
starting from r34's **pre-Schur** physical certificate `E_2(B)>L^4/135000`, prove that some quantitatively nonzero original-coordinate scalar pivot leaves `E_2` at scale `L^4` in its exact Schur residual, OR route simultaneous Schur cancellation into a zero/small-diagonal hyperbolic / grouped-anchor configuration already payable by pair-log or grouped-product machinery. A rank-one Schur update can cancel E2, so no free survival claim is made.

Full universal essential boundedness remains OPEN. Global continuity remains OPEN; the new E2 theorem proves absolute continuity in `L^p`, while the scalar-Schur branch proves an essential bound but not continuity.
