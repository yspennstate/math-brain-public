# account01/B09 r12 — complete fixed-multiplicity baseline audit

Run: `20260924T144758Z-account01-B09-FIXMULT-auto11-r12`  
Objective: `QFORM-FIXED-MULTIPLICITY-AUDIT-20260924`  
Pinned baseline commit: `7c0d6e60946b19423e6400a12d34b473cf0591e2`  
Pinned manuscript blob: `183ccd294763214e6a707e8d4749ff9a8cf7006d`  
Pinned manuscript SHA-256 from `SOURCE_MANIFEST.json`: `9f3bdec0b88debe9a66076c7b4a5cc894fb14e69b89591a4107e785340f65e69`  
Source path: `proofnet24/QFORM-density/fixed-multiplicity-2026-09-24/manuscript.tex`

## Verdict

**PASS** for the complete 790-line baseline theorem as written. I found no fatal or theorem-changing mathematical gap in

\[
s_{17}(A)\ge s>0
\quad\Longrightarrow\quad
\|p_{X^TAX+b^TX+c}\|_\infty\le 10^4K^2/s
\]

for arbitrary real symmetric `A`, arbitrary independent real coordinate laws with densities bounded by `K`, arbitrary signs and remaining spectrum, and arbitrary affine `b,c`.

This is one worker audit, not formal verification, not journal peer review, and not a solution of the unrestricted three-eigenvalue problem. The manuscript proves an essentially bounded density globally; continuity is asserted/proved only in branches where an integrable characteristic-function majorant is available.

## End-to-end line audit

The line ranges are those in the pinned 790-line source and `proof_map.csv`.

| Lines / statement | Verdict | Reasoning / exact check |
|---|---|---|
| 1–89, theorem/corollary and architecture | PASS | Quantifiers are consistent: product laws only in original coordinates; no moments/support/log-concavity; symmetric `A`; affine terms arbitrary. Normalized proof plan correctly separates the order-3 half-potential and order-5 density uses. |
| 91–120, `lem:fourier` | PASS | Gaussian regularization, Plancherel normalization and inversion constants agree with the convention `hat f(t)=int e^{itx}f(x)dx`. Weak convergence plus uniform convergence identifies the density. |
| 122–160, `lem:envelope`, `lem:riesz` | PASS | Envelope integral is `2ap/(p-1)`. The Gaussian/Gamma representation yields the stated Riesz factor and the `12 sqrt(u)` weighted integral. Tonelli is used only on nonnegative majorants. |
| 163–217, singular values / Schur / diagonal dominance | PASS | The rank inequality is singular-value based and does not require symmetry. The Schur count uses `S^{-1}` as a principal compression of `A^{-1}` and handles singular `A` by a moving-threshold perturbation. Strict row diagonal dominance is valid for nonsymmetric matrices. |
| 219–255, geometric rank-one Brascamp–Lieb | PASS | The heat-flow derivative has the correct sign from the frame identity; Gaussian tails justify differentiation/integration by parts; trace gives `sum c_i=d`; the large-time limit and small-time Fatou step are valid. |
| 257–301, product projections and scalar Fourier powers | PASS | Orthogonal completion is used only in a deterministic change of variables. Dropped `b_i=0` factors are harmless; the inequality `-b log b<=1-b` may be summed over all rows (at `b=0`, left side is interpreted as zero), giving `d/2`. The scalar Fourier-power argument uses an integrable even power and the projection bound at zero. |
| 303–400, decoupling / regularized crossing determinant / volume envelopes | PASS | The two-copy decoupling keeps all same-bank phases as modulus-one factors. Jensen gives the fourth-power form. The regularized frame weights, Jacobian, Fourier `L^p` factors, determinant exponent `-1/8`, and order-5 / order-3 exponents are consistent. No pointwise quadratic-phase decay is assumed. |
| 402–525, scalar/definite/indefinite coordinate changes and quarter-power concentration | PASS | Square-profile domination is measure-theoretic and conditioning-safe. Definite-pair rotation occurs only in a deterministic integral. The hyperbolic parametrization and logarithmic tail estimate retain original-coordinate density caps. The quarter-power argument uses a physical coordinate cut and the regularized determinant theorem; no rotated independence is asserted. |
| 527–580, `def:pivot-volume`, `lem:sampling`, `lem:completion` | PASS | Ordered disjoint-minor counting is an inequality because singular seeds may have nonsingular extensions. The interpolant can be nonsymmetric. `R-P` is supported in rows `T` or columns `S`, giving global rank `<=3r`; on `L x L`, `R=P`, giving rank `<=r`. `D` vanishes on `S union T`, and `E` has zero diagonal. |
| 582–619, `prop:volume` — B09 primary lens | PASS | This chain is valid for the nonsymmetric auxiliary. From `||E||<=epsilon` and `s_m(A)>=1`, `s_m(D+R)>=1-epsilon`; global rank `<=3r` gives `s_{m-3r}(D)>=1-epsilon`. Since `m=4k-3>=4r+1`, at least `r+1` diagonal entries of `D` are large. They lie in `L` because `D=0` on the seed. On the selected block, `|R_ii|>=371/400`, while each off diagonal is `<1/7+1/16`; with `r<=4` the row sum is `<23/28`. Exact strict slack is `371/400-23/28=297/2800>0`. Hence the `(r+1)x(r+1)` block is invertible, contradicting `rank R[L,L]<=r`. |
| 621–645, random cut and no-pivot consequences | PASS | Each ordered disjoint order-`k` minor crosses a fair physical cut with probability `4^{-k}`. Constants `Z_k^{-1/(2k)}<=160`, half-potential `<200`, and density `<2400` follow from the preceding envelopes. |
| 647–724, kernel bounds / pivot half-potential / nine-direction half-potential | PASS | The singular-integral bounds are used only under Tonelli domination. Scalar, definite-pair and indefinite-pair pivot alternatives exhaust the pivot definition. The distinction between truncated `H(Q)` and the full half-potential is handled explicitly by adding at most one outside distance one. |
| 726–749, proof of `thm:main` | PASS | No-pivot branch uses order five. Scalar pivot loses one Schur direction and then invokes the nine-direction full half-potential. Definite and indefinite pairs are conditioned in original coordinates. Scaling `Y=KX`, `tilde Q=(K^2/s)Q` gives exactly the `K^2/s` factor. |
| 751–790, threshold accounting, limitations, bibliography | PASS | The limitations accurately distinguish continuous no-pivot output from merely essentially bounded pivot branches and explicitly do not claim the three-eigenvalue conjecture. |

## Package audit

Read in this invocation: `README.md`, `DELIVERY_STATUS.md`, `AUDIT.md`, `proof_map.csv`, `SOURCE_MANIFEST.json`, `verify.py`, and `checks.json`. The support package is now present. `checks.json` records `PASS` for 534 exact interpolation seeds, 18 volume-sampling cases, 9 strict-sampling cases, 240 floating Schur threshold cases and 30 graph-weight cases, with exact diagonal-dominance slack `297/2800`.

**UNCHECKED in this worker run:** I did not locally rerun `verify.py`; I read the script and its recorded output. I also did not independently rebuild or visually inspect the 16-page PDF. Those are reproducibility/presentation checks, not missing steps in the self-contained symbolic proof.

## Threshold status encountered during this audit

The repository now contains complete nine-eigenvalue replacement proofs preserving all quantifiers. In particular account02/B16 commit `00043d234457291849302da1ad049b554662a513` states and proves

\[
s_9(A)\ge s>0\implies \|p_Q\|_\infty<5338K^2/s,
\]

using marginal-free order-three density and order-two half-potential receivers. This B09 report does not self-award an owner release certificate for that result; it uses only a scoped compiler from that proof in the accompanying new improvement.

Multiplicity eight remains open in the freshest source material. The exact obstruction has been narrowed to a robust physical two-anchor pair with large outside cross determinant and a small/near-singular principal self-block; positive order-two crossing volume alone is known not to be a density endpoint when both banks retain arbitrary curvature.

## New B09 improvement in this run

See the sibling improvement `LOW_LEVERAGE_ROBUST_PAIR.md`. It proves that the remaining robust two-anchor `s_8` endpoint is already a bounded **continuous** density branch whenever every physical complement coordinate has row-space leverage at most `2/3`. Quantitatively the resulting density bound is `<23.48` in the normalized cap-one/unit-scale setting. Hence any still-unpaid robust-pair endpoint must contain a literal complement coordinate of leverage `>2/3`; there are at most two such coordinates. If there are two, their literal two-column cross determinant already carries more than one third of the robust cross Gram determinant.

## Final status

- Baseline `s_17` manuscript: **PASS** in this complete B09 audit.
- Full package: read; local rerun/build: **UNCHECKED** as stated above.
- `s_9` replacement: complete proofs exist in the repository; this run did not claim release authority.
- `s_8`: **OPEN**, but the remaining robust-pair endpoint is reduced further by the new low-leverage closure.
- unrestricted `s_3`: **OPEN**.
