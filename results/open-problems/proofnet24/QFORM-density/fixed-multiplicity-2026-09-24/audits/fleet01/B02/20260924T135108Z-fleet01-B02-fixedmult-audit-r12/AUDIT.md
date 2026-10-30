# fleet01/B02 r12 — independent end-to-end fixed-multiplicity audit

Run: `20260924T135108Z-fleet01-B02-fixedmult-audit-r12`  
Objective: `QFORM-FIXED-MULTIPLICITY-AUDIT-20260924`  
Lens: scalar Fourier powers, convolution, projection-density constants, exact Fourier/Riesz normalizations, then full dependency reconstruction.

## Source pin

Baseline source commit: `7c0d6e60946b19423e6400a12d34b473cf0591e2`.  
Fresh `master` observed immediately before this report's writes: `bf6bca17d08ea3cb9a20110f7fafc54886294e70`.  
Canonical path: `proofnet24/QFORM-density/fixed-multiplicity-2026-09-24/manuscript.tex`.  
Git blob at the fresh master snapshot: `183ccd294763214e6a707e8d4749ff9a8cf7006d`.  
Manifest SHA-256: `9f3bdec0b88debe9a66076c7b4a5cc894fb14e69b89591a4107e785340f65e69`.  
Manifest length: 790 lines / 47,883 bytes.

I read in full the current `README.md`, `DELIVERY_STATUS.md`, `AUDIT.md`, `proof_map.csv`, `SOURCE_MANIFEST.json`, `verify.py`, `checks.json`, and all 790 source lines of `manuscript.tex`. The support files advertised by the README are now present; the earlier package-absence issue from a prior B02 run is therefore resolved.

## Urgent verdict

**PASS for the mathematical 17-eigenvalue theorem.** I found no `FALSE` statement, no theorem-breaking `GAP`, and no mathematical source range left `UNCHECKED` in the 790-line manuscript. The literal theorem audited is

\[
s_{17}(A)\ge s>0
\quad\Longrightarrow\quad
\|p_{X^TAX+b^TX+c}\|_\infty\le 10^4K^2/s
\]

for arbitrary real symmetric `A`, arbitrary affine terms `b,c`, and independent real coordinate densities bounded by `K`.

This PASS concerns the fixed-multiplicity theorem only. It is not a proof of the unrestricted three-eigenvalue conjecture. Globally the source proves an essentially bounded density; continuity is explicitly obtained only in Fourier-integrable subbranches.

## File/package ledger

- `README.md`: **PASS.** Its source pin, theorem scope, and package description agree with the files now present.
- `DELIVERY_STATUS.md`: **PASS as status metadata.** It correctly distinguishes the 790-line immutable mathematical source from later audits/improvements.
- `AUDIT.md`: **PASS as historical self-audit, not independent validation.** Its finite-test counts are historical. I did not rerun the old historical checker binary; those historical execution instances remain **UNCHECKED**, but they are not proof dependencies.
- `proof_map.csv`: **PASS.** Its label/range map agrees with the source ranges reconstructed below.
- `SOURCE_MANIFEST.json`: **PASS.** It records the source blob/hash/length used here.
- `verify.py`: **PASS for its stated finite regression scope.** It is not a proof engine and does not claim to be one.
- `checks.json`: **PASS as the current recorded execution result** for the scoped finite diagnostics: 534 exact interpolation seeds, 18 exact volume comparisons, 240 Schur-threshold numerical cases, and 30 graph-weight cases. I do not promote these finite checks to theorem proof.

## Complete mathematical source ledger

### Lines 1–83 — statement, quantifiers, normalization: PASS

The theorem retains arbitrary dimension, signs, remaining spectrum, rough independent cap-`K` laws, and arbitrary affine terms. The scaling target `K^2/s` is dimensionally correct. The text does not claim the three-eigenvalue theorem or global continuity.

### Lines 84–168 — Fourier, Gaussian inversion, envelopes, Riesz: PASS

With `\hat f(t)=\int e^{itx}f(x)dx`, Plancherel is `\int|\hat f|^2=2\pi\int|f|^2` and inversion carries `1/(2\pi)`. The Gaussian approximate identity and weak identification argument work for rough probability laws. Direct integration of `min(1,(a/|t|)^p)` gives the stated `2ap/(p-1)`. The half-Riesz representation has coefficient `1/\sqrt{2\pi}` and is used only under a nonnegative integrable majorant, so Tonelli is legitimate.

### Lines 169–217 — singular values, Schur count, diagonal dominance: PASS

The approximation-number formula proves both perturbation and rank-shift inequalities without symmetry. For the Schur lemma, the invertible congruence and inverse-compression argument are correct. In the singular ambient case, the moving-threshold statement is equivalently an ordered singular-value inequality for `S_\varepsilon`; operator-norm convergence of `S_\varepsilon` yields the closed endpoint inequality at `t`. Strict row diagonal dominance implies invertibility without symmetry and is used only for a rank contradiction.

### Lines 218–255 — geometric Brascamp–Lieb: PASS

Differentiation of the heat-flow product gives

`\partial_tF-\Delta F=F(\sum c_iv_i^2-|\sum c_iu_iv_i|^2)>=0`

because the frame operator is an isometry. The trace identity `\sum c_i=d`, Gaussian large-time limit, integration by parts, Lebesgue-point/Fatou step and final truncation/monotone-convergence step are all valid.

### Lines 256–282 — product projection density: PASS

The orthogonal completion is only a deterministic change of integration variables; no rotated random coordinates are asserted independent. For `b_i=1-|U^Te_i|^2`, geometric BL gives the product `\prod b_i^{-b_i/2}`. The entropy inequality `-b\log b<=1-b` gives `e^{d/2}`. When `b_i=0` factors are dropped, re-inserting their nonnegative `1-b_i` terms on the upper-bound side is legitimate; the source compresses one harmless `<=` into the displayed sum. The scalar consequence is `\sqrt e/|a|`.

### Lines 283–301 — integrated scalar Fourier powers: PASS

For `p>=2`, `m=floor(p/2)>=p/4` and `|\hat f|^p<=|\hat f|^{2m}`. The even power is the characteristic function of a sum of `m` independent differences; each difference density is `f*\tilde f<=1`. Fourier inversion at zero is legitimate because the even power is integrable, and the projection lemma on the `2m` signed original coordinates gives density at zero at most `\sqrt e/\sqrt{2m}`. Hence

\[
\int|\widehat f(t)|^pdt\le2\pi\sqrt{2e}/\sqrt p.
\]

No moment assumption or spectral-coordinate independence is hidden.

### Lines 302–400 — decoupling, regularized determinant, crossing volumes: PASS

Expanding the `X_J` square uses one genuine independent copy, so `D=X_J-X'_J` has independent cap-one coordinates. Jensen correctly promotes the second-power inequality to the fourth-power inequality. In the determinant proof, with `a=2t`, `\alpha=(2\pi e)^2`, and `H=\alpha I+a^2M^TM`, the coordinate and row vectors form an exact geometric rank-one frame. The scalar Fourier-power factor cancels the row Jacobian powers, and the coordinate entropy factor cancels the remaining regularizer exactly. Taking fourth roots yields

\[
|\phi_Z(t)|\le\det\!\left(I+\frac{t^2}{\pi^2e^2}M^TM\right)^{-1/8}.
\]

Cauchy–Binet gives the `Z_k` coefficients. The `k=5` tail is integrable and gives `5eZ_5^{-1/10}`; `k=3` is used only after the `|t|^{-1/2}` Riesz weight, not incorrectly as an `L^\infty` endpoint.

### Lines 401–525 — scalar/pair profiles and weak concentration: PASS

The scalar-square density and interval-preimage estimate are correct branchwise changes of variables. The conditional profile is a domination statement, not an independence assertion. The definite-pair Jacobian is `1/(2\sqrt{|det B|})`. For the indefinite pair, the hyperbolic parametrization has the displayed Jacobian and the tail estimates use an original coordinate, preserving the product structure. The quarter-power concentration proof correctly splits into a large physical diagonal or a physical crossing block with norm at least `L/4`; Gaussian smoothing then gives the `1/4` small-ball exponent. Layer cake yields `4+4\log16` for the logarithmic potential. Rough-density exceptional slices are handled through nonnegative test functions/Tonelli.

### Lines 526–630 — disjoint minors, interpolation, spectral-to-volume: PASS

The volume-sampled bordered determinant identity is exact. An ordered disjoint `(r+1)` minor is counted at most `(r+1)^2` times, giving the expected Frobenius error. The interpolant is intentionally nonsymmetric; the completion has global rank at most `3r`, restricted rank at most `r`, zero `E` diagonal, and `D=0` on the seed. In the spectral-to-volume proposition, rank subtraction forces `r+1` large entries of the diagonal remainder; they lie outside the seed. The no-pivot entry bound plus the Frobenius error makes the corresponding restricted `R` block strictly diagonally dominant, contradicting restricted rank `r`. The random-cut survival probability is exactly `4^{-k}`.

### Lines 632–724 — analytic no-pivot and pivot synthesis: PASS

The order-three and order-five random-cut constants follow from `Z_k^{-1/(2k)}<=2\kappa^{-1/2}=160`. The two singular-kernel estimates are valid; the logarithmic kernel is maximized by centering the interval superlevel sets. In the pivot proposition, a scalar pivot leaves one spectral direction for the quarter/logarithmic estimate, a definite pair gives a direct conditional density cap, and an indefinite pair is controlled by the hyperbolic logarithm and the universal logarithmic potential. Under `s_9>=1`, either the pivot proposition controls the truncated half potential or the no-pivot order-three result controls the full half potential; adding the outside tail costs at most one.

### Lines 726–790 — main theorem, scaling, scope: PASS

A scalar pivot from `s_17>=1` leaves at least sixteen Schur directions, enough for the nine-direction half-potential proposition. Definite and indefinite pair pivots are paid directly. The no-pivot branch uses the order-five density receiver. The scaling `Y=KX`, `A/s`, and `Q=(s/K^2)\widetilde Q` gives exactly `K^2/s`. The interval/density equivalence is standard measure regularity. The limitations section accurately states that the proof does not reach three eigenvalues and does not establish global continuity.

## Independent review status and threshold work

The baseline 17-direction source therefore receives a full B02 mathematical PASS in this invocation. Separately, I reconstructed the newer threshold-nine compiler at `improvements/fleet03/B04/20260924T121940Z-fleet03-B04-fixedmult-audit-r1/REPORT.md`: its grouped product-Fourier estimate, row-promotion identities, marginal-free `E_3` density receiver and `E_2` half-potential receiver are correct. Two genuinely separate complete PASS reconstructions already exist in the repository: fleet01/B16 and fleet03/B10 (fleet03/B10 also records fleet03/B08). Thus the mathematical threshold-nine reduction satisfies the owner's two-review condition, although release/baseline promotion remains an owner decision.

I found no complete eight-direction theorem. The current eight-direction work reduces the no-pivot endpoint to a quantitative overlap-one/two-sided physical collar, but its dependence-safe density receiver is still missing. Therefore the lowest rigorously closed multiplicity I can support in this run is **9**, not 8.

A new B02 constant/parameter improvement for that nine-direction theorem is saved separately under this run's `improvements/fleet01/B02/.../IMPROVEMENT.md`. It is new and must itself receive two separate complete reviews before being called validated.

## Labels summary

- `PASS`: all mathematical source ranges 1–790 and all stated theorem dependencies.
- `GAP`: none in the baseline theorem.
- `FALSE`: none found.
- `UNCHECKED`: no mathematical source range; only historical finite-test executions mentioned in the legacy self-audit were not independently rerun, and they are not proof dependencies.

Model: `GPT-5.6 Sol`. Provider effort/reasoning telemetry: `UNKNOWN / not exposed`.