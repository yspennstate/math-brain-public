# account02/B13 — fixed-multiplicity audit, fresh full pass

Run: `20260924T145501Z-account02-B13-fixedmult-auto11b`  
Objective: `QFORM-FIXED-MULTIPLICITY-AUDIT-20260924`  
Execution status: `WITHOUT_VERIFIED_BRAIN`.

## Source pin and package coverage

Pinned mathematical baseline:

- source commit `7c0d6e60946b19423e6400a12d34b473cf0591e2`;
- source blob `183ccd294763214e6a707e8d4749ff9a8cf7006d`;
- recorded SHA-256 `9f3bdec0b88debe9a66076c7b4a5cc894fb14e69b89591a4107e785340f65e69`;
- `manuscript.tex`: 47,883 bytes, 790 lines.

Fresh master before publication was `bd68752b06ae4a64ddaadc4b580edfa11946651a`; concurrent audit/improvement commits do not modify the pinned baseline manuscript. I read `README.md`, `SOURCE_MANIFEST.json`, every line 1--790 of `manuscript.tex`, `AUDIT.md`, `proof_map.csv`, `verify.py`, and `checks.json`. I also read the current complete threshold-nine replacement and a separate complete review only after independently securing the baseline verdict.

The baseline theorem audited is exactly

\[
s_{17}(A)\ge s>0,\quad 0\le f_i\le K
\quad\Longrightarrow\quad
\|p_{X^TAX+b^TX+c}\|_\infty\le 10^4K^2/s,
\]

for arbitrary independent rough coordinate laws, arbitrary real symmetric `A`, arbitrary dimension/signature/remaining spectrum, and arbitrary affine `b,c`. This review does **not** claim the unrestricted three-eigenvalue conjecture.

## Verdict

**PASS for the mathematical 17-eigenvalue theorem in this fresh B13 reconstruction.** I found no theorem-breaking FALSE statement and no fatal mathematical GAP. No manuscript source range is UNCHECKED.

Two nonfatal audit annotations remain:

1. **GAP-PRESENTATION, no theorem impact.** The theorem states density caps almost everywhere, while some inverse-branch formulas later write pointwise values. A global convention choosing Borel density representatives and redefining them on null sets so `0<=f_i<=K` everywhere would make the presentation uniform. The laws are unchanged, and the existing test-function/Tonelli arguments already make the substantive claims representative-independent.
2. **UNCHECKED-COMPUTATION only.** I read `verify.py` completely and checked its asserted invariants against the proof. I read `checks.json`, which records PASS with 534 exact interpolation seeds, 18 exact volume comparisons, 9 strict-sampling cases, exact diagonal-dominance slack `297/2800`, 240 Schur diagnostics, and 30 graph-weight diagnostics. I did not independently re-run that finite checker in this invocation. This is not an unchecked mathematical source range.

The historical `AUDIT.md` has different finite-test counts from the new checker. README/SOURCE_MANIFEST explicitly disclose that the current checker is a new suite and does not reproduce the historical suite. I mark that as a documentation/reproducibility note, not a mathematical defect.

## Full line-range audit ledger

| source lines | item | status | independent check / impact |
|---|---|---|---|
| 1--46 | preamble, notation, abstract | PASS | Definitions and advertised scope agree with theorem; no hidden regularity/support assumptions. |
| 47--90 | main theorem, scaling architecture, parameters | PASS | Quantifiers are arbitrary product densities, symmetric `A`, affine terms; `s_j` means singular values. Architecture distinguishes pivot and no-pivot branches correctly. |
| 91--120 | Fourier identities | PASS | Fourier convention, Plancherel factor `2pi`, Gaussian inversion, weak-limit density argument checked. |
| 122--130 | power envelope | PASS | Integral of `min(1,(a/|t|)^p)` is `2ap/(p-1)` and inversion constant is correct. |
| 132--160 | Riesz half-potential | PASS | Gamma representation, two Tonelli steps and `1/sqrt(2pi)` constant checked; weighted exponent `3/4` gives `12 sqrt(u/(2pi))`. |
| 161--217 | singular values, Schur count, diagonal dominance | PASS | Nonsymmetric singular-value perturbation is valid. Schur count loses at most pivot size; singular `A` perturbation is legitimate. Strict row diagonal dominance needs no symmetry. |
| 221--255 | geometric rank-one BL | PASS | Heat-flow sign follows from frame contraction; compact-support differentiability and large-time limit are sufficient; truncation handles rough nonnegative inputs. |
| 258--282 | product projection | PASS | Original-coordinate product structure is retained. Orthogonal completion is deterministic integration geometry, not rotated independence. Endpoint `d=n` handled. |
| 284--301 | scalar Fourier powers | PASS | Difference density cap, Plancherel and projection-density evaluation at zero give stated `p>=2` bound. |
| 303--324 | cross-form and decoupling | PASS | Conditioning order and independent copy are correct; arbitrary same-bank phases remain modulus one; difference coordinates remain independent cap-one. |
| 326--373 | regularized crossing determinant | PASS | Frame weights, BL scales, Fourier powers, entropy-like `c_j` factor and fourth root reproduce determinant exponent `-1/8`. Zero rows are harmless. |
| 374--400 | crossing volumes / order 3 and 5 envelopes | PASS | Cauchy--Binet coefficients and powers checked; order five is integrable for density, order three only after Riesz weight. |
| 401--422 | scalar square profile and conditional profile | PASS | Two inverse branches give square-root envelope; conditional domination is via test functions/Tonelli, not false independence. |
| 423--434 | definite pair | PASS | Reconstructed below in detail; determinant alone pays, no minimum-singular-value floor and no post-rotation independence. |
| 435--482 | hyperbolic pair | PASS | Reconstructed below in detail, including both level-set signs, tail monotonicity in an original coordinate, rough fragmented/unbounded inputs, and exceptional critical value. |
| 485--525 | quarter-power concentration and log potential | PASS | Diagonal versus off-diagonal split, physical crossing determinant bound, Gaussian smoothing and layer cake checked. |
| 528--544 | pivot/volume definitions and no-pivot entry gate | PASS | Ordered disjoint minor convention and entry estimate from absent principal pair pivot are correct. |
| 545--564 | volume-sampled interpolation | PASS | Bordered determinant identity, sorted-sign cancellation after squaring, singular seed inequality and interpolation support checked. |
| 566--580 | diagonal plus nonsymmetric interpolation | PASS | `rank R<=3r` globally and `rank R[L,L]<=r` are distinct and both valid; `D=0` on seed and `E` has zero diagonal. |
| 582--619 | no-pivot spectral-to-volume | PASS | Telescoping bad-ratio selection, singular-value rank subtraction, location of large diagonals in `L`, and `r<=4` diagonal-dominance contradiction checked. |
| 621--645 | random cut and no-pivot analytic consequences | PASS | Every ordered disjoint `k`-minor crosses with probability `4^-k`; constants `160`, `<200`, `800e<2400` check. |
| 646--674 | truncated half potential / kernel integrals | PASS | Both singular kernels are integrable at exactly the strengths later used. I retain the sharper pre-relaxation form of `J(d)` below for a new constant improvement. |
| 676--714 | pivot half potentials | PASS | Scalar, definite-pair and indefinite-pair alternatives exhaust pivots. Schur hypotheses and full/truncated distinction are correct. |
| 716--724 | nine-eigenvalue half potential | PASS | Pivot branch gives truncated `H`, no-pivot branch gives full half-potential; outside-unit tail costs at most one. |
| 726--749 | main proof | PASS | No-pivot, scalar, definite and indefinite pivot branches all meet exact hypotheses; final `K,s` scaling is correct. |
| 750--790 | threshold accounting, limitations, bibliography | PASS | Correctly says order-three does not by itself give density, global continuity is not asserted, and the three-eigenvalue problem remains open. |

## B13 lens: definite physical pair

Let a conditioned original-coordinate pair `W in R^2` have joint density at most `M`, and let its quadratic part `B` be definite. After deterministic translation and deterministic orthogonal diagonalization, write the positive-definite case with eigenvalues `mu_1,mu_2>0` as

\[
w=w_0+\sqrt{\delta/\mu_1}\cos\theta\,e_1
 +\sqrt{\delta/\mu_2}\sin\theta\,e_2.
\]

The absolute Jacobian is

\[
\left|\det\frac{\partial w}{\partial(\delta,\theta)}\right|
=\frac1{2\sqrt{\mu_1\mu_2}}
=\frac1{2\sqrt{|\det B|}}.
\]

Integrating the joint density around `0<=theta<2pi` gives

\[
\boxed{\ \|p_q\|_\infty\le \pi M/\sqrt{|\det B|}.\ }
\]

This is determinant-only: there is no hidden `sigma_min(B)` gate. The rotation is only a change of variables inside a deterministic two-dimensional integral; no independence of the rotated coordinates is used.

## B13 lens: complete hyperbolic envelope under rough inputs

Let `B` be indefinite with eigenvalues `mu_+>0>mu_-`, put

\[
D=|\det B|,\qquad \Lambda=\mu_+^{-1}+|\mu_-|^{-1}.
\]

For `delta=z-v>0`, the two branches are

\[
w_\varepsilon(t)=\varepsilon\sqrt{\delta/\mu_+}\cosh t\,e_+
 +\sqrt{\delta/|\mu_-|}\sinh t\,e_-,
\qquad\varepsilon=\pm1.
\]

Direct differentiation gives the exact absolute Jacobian

\[
\left|\det\frac{\partial w_\varepsilon}{\partial(\delta,t)}\right|
=\frac1{2\sqrt D}.
\]

Write a branch as `u e^t+w e^{-t}`. Orthogonality gives

\[
|u|=|w|=\rho_0=\frac12\sqrt{\delta\Lambda}.
\]

Choose an **original physical coordinate** `i` with `|u_i|>=rho_0/sqrt2`. With `T_1=(3/4)log2`, for `t>=T_1` the decreasing exponential is at most half the increasing one, so that coordinate is monotone, remains on one sign, and

\[
\tfrac12|u_i|e^t\le |w_i(t)|\le\tfrac32|u_i|e^t,
\qquad |w_i'(t)|\ge |w_i(t)|/3.
\]

Choose `T=max(T_1,log(2/|u_i|))`; then the tail starts at magnitude at least one. Along this tail `f_1 f_2<=f_i` because every density is at most one. Changing the monotone original coordinate gives

\[
\int_T^\infty f_1(w_1(t))f_2(w_2(t))\,dt
\le3\int_{\{|y|\ge m,\,\text{one sign}\}}\frac{f_i(y)}{|y|}\,dy
\le3\log(1+1/m)\le3\log2.
\]

The middle inequality uses only `0<=f_i<=1` and total mass at most one on that half-line: a decreasing weight is maximized by filling the unit-length interval nearest the threshold. Hence disconnected, arbitrarily fragmented and unbounded supports are allowed. The negative tail is identical using a physical coordinate where the `w` vector is large. The two cutoffs obey

\[
T,T'\le\frac34\log2+\frac12\log_+\frac{32}{\delta\Lambda}.
\]

The middle integrand is at most one. Summing both branches cancels the `1/2` in the Jacobian; `Lambda>=2/sqrt D` then gives

\[
\boxed{\ p_q(z)\le D^{-1/2}
\left(6+\log_+\frac{16\sqrt D}{|z-v|}\right)\ }
\]

for almost every `z!=v`. For `delta<0`, apply the same calculation after negating the form. The critical level is one output point; all later conditioning uses nonnegative test functions and Tonelli, so no exceptional conditional slice is selected.

### Counterexample stress test: the logarithm is necessary

For independent `X,Y` uniform on `[-1/2,1/2]`, set `Q=X^2-Y^2`. With `U=X-Y`, `V=X+Y`, the joint density is `1/2` on `|U|+|V|<=1` and `Q=UV`. Product coarea gives, for `0<|z|<1/4`,

\[
p_Q(z)=\log\frac{1+\sqrt{1-4|z|}}
{1-\sqrt{1-4|z|}}
=\log(1/|z|)+O(1).
\]

Thus no determinant-only uniformly bounded **conditional** density estimate can replace the hyperbolic logarithm, even for compact interval product laws. The manuscript correctly pays that singularity by a surviving Schur direction.

## Logarithmic averaging and determinant-only unconditional pair consequence

If the Schur critical value `R` has a quadratic direction of operator norm at least one, the quarter-power lemma gives

\[
\sup_a\mathbb E\log_+\frac1{|R-a|}\le L_0=4+4\log16.
\]

Averaging the hyperbolic envelope therefore yields

\[
\|p_Q\|_\infty
\le D^{-1/2}\bigl(6+\log_+(16\sqrt D)+L_0\bigr)
\le (10+5\log16)D^{-1/2}+e^{-1}.
\]

So under any spectral hypothesis that guarantees one surviving Schur direction, a high-density witness forces every indefinite physical pair determinant to be small. This is an unconditional *averaged* pair consequence, not the false bounded conditional estimate refuted above.

## Baseline package/checker status

`verify.py` pins the source SHA and checks the exact rank/support/bordered-minor identities used in the structural proof plus finite floating diagnostics. `checks.json` records the current suite's PASS. The suite is explicitly not a proof certificate. The baseline mathematical PASS above is from the written proof, not from these finite checks.

## Threshold reduction audit

After finishing the baseline, I independently reconstructed the current complete threshold-nine replacement. Its two genuinely new analytic endpoints are:

\[
\|p_Q\|_\infty\le C_3 E_3(M)^{-1/6},
\qquad C_3=3\sqrt2\,e(9/2)^{1/6}<14.819,
\]

and

\[
\sup_a\mathbb E|Q-a|^{-1/2}
\le C_2E_2(M)^{-1/8},
\qquad C_2=8\sqrt e\,2^{-1/8}<12.096.
\]

I checked the grouped proof rather than importing its verdict: the hub complex pushforward has `L^2` norm controlled by the projected product density; the light-bank square uses an independent copy only of the literal `J` bank; the difference coordinates remain independent cap-one; the map to `(M_JD,(<c_i,D>)_{i in T})` has squared Jacobian `S^2 det(C_TC_T^T)`; weighted Holder uses only positive marginals `alpha_i<=1/2`; and the ordered-subset entropy inequality closes the determinant geometric mean. The `k=0` endpoint is interpreted as an absent hub with empty singular product one and zero-dimensional density cap one; zero marginals are omitted before Holder.

The promotion trees then make the `E_3` density and `E_2` half-potential bounds marginal-free. Combining them with the pinned spectral-to-volume theorem gives a complete nine-direction theorem. A separate immutable improvement in this same run sharpens its constant from `6010` to `5460` without changing any hypothesis.

I do **not** claim multiplicity eight. The current exact `s_8` structural reduction leaves the no-pivot overlap-one/two-sided-collar receiver unpaid. Existing entropy accounting removes packet-cardinality loss but not the shared-anchor analytic dependence. The unrestricted three-eigenvalue conjecture remains open.

## Next obligation

`QFORM-S8-SHARED-ANCHOR-ANALYTIC-LOG-REMOVAL`: convert the quantitative overlap-one/two-sided collar at `s_8` into an integrable product-preserving Fourier or small-ball receiver, including heavy-marginal promotion cases, without a principal-pair pivot or post-rotation independence.

Manual changed-file review: this artifact contains only mathematical statements, source hashes/commits, the logical worker label, and nonsecret run metadata; no credentials, machine paths, scheduler identifiers, private personal data, email, or unrelated material.
