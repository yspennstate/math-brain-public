# fleet01/B06 independent end-to-end audit — nine-eigenvalue candidate

Run: `20260924T153355Z-fleet01-B06-fixedmult-audit-r12`
Objective: `QFORM-FIXED-MULTIPLICITY-AUDIT-20260924`
Worker: fleet01/B06
Model self-report: GPT-5.6 Sol
Reasoning effort / provider counters: UNKNOWN / not exposed
Brain status: WITHOUT_VERIFIED_BRAIN

## Source pin

Latest candidate source audited in full:

- repository: `yspennstate/math-open-problems`
- branch: `master`
- source path: `proofnet24/QFORM-density/fixed-multiplicity-2026-09-24/improvements/interactive/20260924T145418Z-nine-400/paper.tex`
- source commit: `eeb752c8943536541b34b42b8bf48e924f4d3d2f`
- git blob: `19fb119877426b640b2c0dae19ec2f78a399fe11`
- SHA-256 supplied by the package: `bf1caf6ae4b4bc33992f501c169b5dc6c795db757b0f6089eff9991391effdf3`
- length: 955 source lines

I also read in full the package `README.md`, `NINE_400_AND_OVERLAP.md`, `AUDIT_NEW.md`, `MANIFEST.json`, `proof_map.csv`, `verify_new.py`, and `checks_new.json` at package commit `af592913ccfc4a87dfbf7c3a49bf2c5d4bbae359`. The authoring self-audit was treated only as a checklist, not as evidence for this verdict.

## Verdict

**PASS** for the mathematical candidate actually written in `paper.tex`:

> For arbitrary independent real coordinate densities bounded by `K`, arbitrary real symmetric `A`, arbitrary affine terms `b,c`, and `s_9(A)>=s>0`, the law of `X^TAX+b^TX+c` has an essentially bounded density with `||p||_infinity <= 400 K^2/s`.

I found no FALSE statement and no unresolved mathematical GAP in the 955-line paper. No paper range remains UNCHECKED in this review. This report is one genuinely separate worker reconstruction; it is **not** by itself the two-review independent-validation gate and it is not a claim about the unrestricted three-eigenvalue conjecture.

## Line-by-line range ledger

| Source lines | Status | Independent check |
|---|---|---|
| 1–46 | PASS | Front matter and abstract match the proved scope; no hidden smoothness, support, sign, moment, iid, exact-rank, or rotational-independence assumption is introduced. |
| 47–75 | PASS | Theorem quantifiers, interval formulation, normalization parameters, and architecture are consistent. The final `K^2/s` scaling is checked again below. |
| 76–164 | PASS | Fourier convention, Gaussian regularization, Plancherel/inversion, power envelope, and Riesz half-potential constants follow from the displayed Gaussian/gamma calculations and Tonelli. |
| 165–214 | PASS | Singular-value perturbation/rank inequality, Schur spectral count (including the singular limiting argument), and strict diagonal dominance are valid with the stated strict/non-strict thresholds. |
| 215–252 | PASS | Geometric rank-one Brascamp–Lieb heat-flow proof: the sign of `partial_t F-Delta F`, contraction from the Parseval frame, large-time Gaussian normalization, small-time Fatou step, and truncation/monotone convergence are correct. |
| 253–297 | PASS | Product-projection density and integrated scalar Fourier-power estimate preserve original-coordinate independence; the `e^(d/2)` and `2*pi*sqrt(2e)/sqrt(p)` constants check. |
| 298–396 | PASS | **B06 starting lens fully checked.** Decoupling, graph determinant theorem, change-of-variable Jacobian, geometric weights, trace identity, exponent `-1/8`, and regularizer `alpha=(2*pi*e)^2` are all correct; detailed derivation below. Crossing-volume expansion and the order-5 density/order-3 half-potential consequences are correct. |
| 397–488 | PASS | Grouped mollified-`L^2` argument: the image complex measure is dominated by a bounded ordinary projection density; Jensen is applied before the `delta->0` limit; weighted Holder is valid for the finite non-normalized kernel measure; row-Gram determinant and entropy factors are correct. |
| 489–527 | PASS | Heavy-row promotion uses exact Gram–Schmidt incident-volume identities and only literal original-coordinate hubs. The `q=3` density and `q=2` full half-potential constants follow from the stated envelopes; no marginal or rotated-independence assumption is smuggled in. |
| 528–610 | PASS | Scalar-square profile, definite-pair coarea calculation, and indefinite hyperbolic envelope are correct. In the hyperbolic proof the phrase “orthogonality gives `|u|=|w|`” refers to the eigenvectors; `u,w` themselves need not be orthogonal, and the proof does not require them to be. Tail monotonicity and the `6+log_+` constant close. |
| 611–662 | PASS | Quarter-power concentration: the random-sign cut gives a cross block of norm at least `||S||/4`; determinant decay, Gaussian smoothing, gamma bound, and logarithmic layer cake are correct. |
| 663–742 | PASS | Disjoint-minor sampling and nonsymmetric completion: bordered determinant counting gives the expected Frobenius error; `rank R<=3r`, `rank R_LL<=r`, and `D=0` on the seed are exact. The no-pivot spectral-to-volume contradiction has positive diagonal-dominance margins for `r=1,2`. |
| 743–766 | PASS | Fair cut has expectation `4^{-k}V_k`; the resulting five-eigenvalue half-potential and nine-eigenvalue no-pivot density bounds use the correct powers of `kappa`. |
| 767–811 | PASS | Scalar convolution kernel and full two-coordinate half-potential are correct. The definite case uses the full layer-cake tail; the indefinite case scales by `D^{1/2}` and gives `D^{-1/4}`, not `D^{-1/2}`. |
| 812–860 | PASS | Five-eigenvalue half-potential proposition and main theorem close every pivot/no-pivot case. Scalar Schur counts leave enough large directions; the indefinite-pair random critical value is controlled by the quarter-power logarithmic potential. Scaling with `Y=KX` gives exactly `400K^2/s`. |
| 861–928 | PASS | Spectral-tail/overlap theorem: `D` diagonal and `E` zero diagonal are Frobenius-orthogonal; rank-`3r` best approximation gives the spectral tail; same-index bordered minors give the `W` term; singular seeds are correctly excluded from that equality. The eight-eigenvalue corollary is only algebraic support, as stated. |
| 929–955 | PASS | Threshold accounting, limitations, acknowledgment, and bibliography do not overclaim eight or three eigenvalues. |

## Detailed B06 determinant reconstruction

For lines 321–369 set

`a=2t`, `alpha=(2*pi*e)^2`, `H=alpha I+a^2 M^T M`.

With row vectors `m_i`, define

`c_j=alpha e_j^T H^{-1}e_j`, `d_i=a^2 m_i^T H^{-1}m_i`.

The vectors `sqrt(alpha) H^{-1/2}e_j` and `a H^{-1/2}m_i` form a Parseval frame, hence `0<c_j<=1`, `0<=d_i<=1`, and

`theta=sum_i d_i=sum_j(1-c_j)`.

The substitution `x=H^{-1/2}z` contributes exactly `det(H)^(-1/2)`. Normalizing the frame vectors gives the one-dimensional factors

`alpha^(c_j/2)c_j^(-c_j/2)||g_j||_{1/c_j}` and `d_i^(-d_i/2)||h_i||_{1/d_i}`.

Because `g_j<=1`, its factor has norm at most one. For `h_i=|fhat_i|^2`, the scalar Fourier-power estimate at exponent `2/d_i` gives

`||h_i||_{1/d_i} <= (2*pi*sqrt(e*d_i))^{d_i}`,

so the `d_i` powers cancel. The entropy inequality `-c log c<=1-c` contributes at most `e^(theta/2)`. Therefore all scalar multipliers combine to

`(2*pi*sqrt(e))^theta e^(theta/2) / alpha^(theta/2) = (2*pi*e/sqrt(alpha))^theta =1`.

After factoring `alpha^d` from `det H`, the fourth-power decoupling bound becomes

`|phi_Z(t)|^4 <= det(I+a^2 M^TM/alpha)^(-1/2)`.

Taking fourth roots and using `a^2/alpha=t^2/(pi^2e^2)` gives exactly

`|phi_Z(t)| <= det(I+t^2 M^TM/(pi^2e^2))^(-1/8)`.

No Jacobian, factor of two, trace term, or independence hypothesis is missing.

## Package audit

- `README.md`: PASS; source and review-status claims match the pinned files.
- `NINE_400_AND_OVERLAP.md`: PASS as a derivation/handoff; it accurately separates the nine theorem from the unresolved eight-direction analytic receiver.
- `AUDIT_NEW.md`: read in full; it is an authoring-agent self-audit and was not used as a substitute for reconstruction.
- `MANIFEST.json`: PASS as metadata; it correctly labels finite checks as non-proof.
- `proof_map.csv`: PASS; labels/line numbers checked against the 955-line source.
- `verify_new.py`: PASS as a finite checker. Its exact checks cover interpolation/rank/orthogonality/constants on sampled finite matrices; its SVD tail comparisons are explicitly floating diagnostics.
- `checks_new.json`: PASS as the recorded output of that finite suite; it is not formal verification.

## Independent improvement found during this audit

The same proof supports the stronger constant `362` at multiplicity nine after retuning the pivot parameters. A complete proof is stored separately in this run's immutable improvement folder. This does **not** lower the eigenvalue count below nine.

I also derived the exact shared-coordinate identity needed for the first eight-eigenvalue analytic step: for a shared index `h` with nonzero `a=A_hh`, a disjoint invertible 2-by-2 seed `B=A_ST`, vectors `u=A_{S,h}`, `v=A_{T,h}`, and bordered determinant `Delta=det A_{S+h,T+h}`, the scalar Schur complement has disjoint crossing block `B'=B-u v^T/a` with

`det B'=Delta/a`.

Combining the scalar profile with the paper's order-two marginal-free half-potential theorem gives

`||p_Q||_infinity <= C2 (|a Delta|)^(-1/4)`

for that single overlap witness. The current eight-eigenvalue lower bound controls `sum Delta^2` but supplies no dimension-free lower control of `|a Delta|` and allows the endpoint `a=0`; therefore this does not close multiplicity eight. The exact remaining analytic debt is a product-preserving shared-coordinate receiver at the zero/small-diagonal endpoint, preferably consuming aggregate overlap mass without selecting a largest minor.

## Final review status

- nine-eigenvalue / constant-400 paper: **PASS by fleet01/B06**.
- no mathematical source range unchecked in this review.
- second genuinely separate end-to-end review: still required before independent-validation status unless another completed current-revision report already supplies it.
- multiplicity eight: **OPEN** in this run.
- unrestricted multiplicity three: **OPEN**.
