SIGNED IN - working on `QFORM-FIXED-MULTIPLICITY-AUDIT-20260924`, account account03, slot B16, 2026-09-24T14:52:40Z.

# account03/B16 r48 — complete baseline audit refresh plus lower-threshold relay

Execution/memory status: **WITHOUT_VERIFIED_BRAIN**.

## Source pins and scope

I read the fresh owner control before selecting work. The current objective supersedes the older projection-product-only assignment for this invocation while retaining QFORM exclusivity and mathematical-integrity rules.

Pinned mathematical baseline:

- repository: `yspennstate/math-open-problems`
- branch: `master`
- initial source commit: `7c0d6e60946b19423e6400a12d34b473cf0591e2`
- source path: `proofnet24/QFORM-density/fixed-multiplicity-2026-09-24/manuscript.tex`
- source blob: `183ccd294763214e6a707e8d4749ff9a8cf7006d`
- SHA-256 from `SOURCE_MANIFEST.json`: `9f3bdec0b88debe9a66076c7b4a5cc894fb14e69b89591a4107e785340f65e69`
- source size: 47,883 bytes / 790 lines.

The source blob is unchanged from the pinned candidate. I read the entire source in this invocation and separately read `README.md`, `AUDIT.md`, `proof_map.csv`, `verify.py`, `checks.json`, `SOURCE_MANIFEST.json`, and `DELIVERY_STATUS.md`.

## Baseline verdict

**PASS for the stated seventeen-eigenvalue candidate theorem.** I found no fatal mathematical gap and no unchecked source region in the 790-line baseline during this audit. This is one independent worker audit, not formal verification or journal peer review. The theorem audited is exactly:

> independent real coordinate densities bounded by `K`; arbitrary real symmetric `A` with `s_17(A)>=s>0`; arbitrary affine `b,c`; then `X^TAX+b^TX+c` has an essentially bounded density with `||p||_infinity<=10000 K^2/s`.

The theorem does **not** assert global continuity and does **not** solve the unrestricted three-eigenvalue conjecture.

### End-to-end source ledger

- **Lines 1--90 — PASS.** Definitions, quantifiers, normalization/scaling and theorem statement retain arbitrary dimension, signs, remaining spectrum, affine terms and rough product laws. The `K^2/s` rescaling is dimensionally and algebraically correct.
- **Lines 91--160 (`lem:fourier`, `lem:envelope`, `lem:riesz`) — PASS.** Fourier normalization is internally consistent; Gaussian/Fresnel identities and the negative-half-moment representation use the stated transform convention. Full versus truncated half potentials are not conflated here.
- **Lines 169--217 (`lem:rank`, `lem:schur`, `lem:dd`) — PASS.** Singular-value rank perturbation is valid for nonsymmetric auxiliaries. The Schur spectral-count proof treats singular pivots by approximation and loses at most the pivot dimension. Strict row diagonal dominance is used only as a rank certificate.
- **Lines 221--255 (`thm:bl`) — PASS.** The rank-one geometric Brascamp--Lieb heat-flow argument, regularization and limiting passage are sufficient for bounded measurable input densities; no Gaussian extremizer is imported as an unproved premise.
- **Lines 258--282 (`lem:projection`) — PASS.** The product-projection bound uses only original product coordinates. A wording concern from an earlier B16 audit is resolved on rereading: after zero-`b_i` factors are dropped from the product, the final entropy sum may include those rows because `-b log b=0` at `b=0`; including all rows gives `sum_i(1-b_i)=d`. Equivalently the retained-row sum is at most `d`. Either reading gives the displayed bound.
- **Lines 284--301 (`lem:scalar-fourier`) — PASS.** Fourier-power constants and exponent range are sufficient for every downstream use.
- **Lines 310--400 (`lem:decoupling`, `thm:determinant`, `cor:vol-fourier`) — PASS.** Independent copies are introduced only in literal original-coordinate banks. The graph Jacobian, weights, trace identity and regularizer produce the determinant exponent `-1/8`. Order five is genuinely integrable for density; order three is used only after multiplication by the half-Riesz weight.
- **Lines 404--525 (`lem:square`, `lem:definite`, `lem:hyperbola`, `lem:quarter`) — PASS.** Square inverse branches are measure domination statements. The definite-plane argument integrates a joint projected density without asserting rotated independence. The hyperbolic envelope tracks the moving critical level and is integrated by Tonelli. No forbidden pointwise rough quadratic-phase estimate appears.
- **Lines 528--580 (pivot/volume definitions, `lem:sampling`, `lem:completion`) — PASS.** Ordered disjoint-minor multiplicities and bordered determinant identities agree. The interpolation `P=A[:,T]B^{-1}A[S,:]` may be nonsymmetric; this is harmless because the rank arguments are singular-value arguments. The completion has `rank R<=3r` globally, `rank R[L,L]<=r` on the seed complement, `E` zero diagonal, and `D` vanishing on the seed.
- **Lines 582--645 (`prop:volume`, `lem:cut`, `cor:no-pivot`) — PASS.** The spectral-to-volume contradiction forces its heavy diagonal coordinates inside `L` before invoking the restricted rank bound. It does not incorrectly use the global `3r` rank where the `r` bound is needed. Random coordinate cutting preserves original-coordinate product provenance.
- **Lines 654--724 (`lem:kernels`, `prop:pivot-H`, `prop:nine`) — PASS.** Kernel integrals, scalar/definite/indefinite pivot alternatives, conditional Tonelli, and the distinction between truncated and full half potentials close as stated. The outside `|Q-a|>1` contribution is separately bounded when promoting a truncated estimate to a full half potential.
- **Lines 726--790 (main proof, constants, discussion) — PASS.** The no-pivot branch spends order-five crossing volume; the scalar pivot invokes the nine-direction half-potential child after losing one Schur direction; two-coordinate pivots are separately paid. The largest displayed branch is below the theorem's rounded `10000` constant. No continuity claim is silently added.

No source line remains `UNCHECKED` in this B16 audit.

## Support-package review

The previously missing support files are now present. `verify.py` checks the pinned source SHA before running, performs exact interpolation/volume identities and finite floating Schur/graph diagnostics, and labels itself non-proof evidence. `checks.json` records `PASS`, 534 exact interpolation seeds, 18 volume-sampling cases, 240 Schur threshold diagnostics and 30 graph-weight diagnostics. I read the checker code and recorded output; I did **not** represent that stored finite run as a mathematical proof or as a fresh local execution in this invocation.

## Lower-threshold work completed in this run

The sibling improvement file for this run proves three new supporting facts aimed at the currently open multiplicity-eight endpoint:

1. **`QFORM-TWOANCHOR-JOINT-L2-RELAY-v1`.** If a literal independent two-coordinate bank enters as
   `Q=X^T B X+2X dot L+R` and the joint density of `(L,R) in R^3` lies in `L^2`, then
   \[
   \|p_Q\|_\infty\le3\,2^{-2/3}(\kappa_X\|p_{(L,R)}\|_2)^{2/3},
   \]
   and `p_Q in C_0`. The estimate is uniform in the full symmetric `2x2` self matrix `B`, including `det B ->0`.
2. **`QFORM-S8-STRONGPAIR-OUTSIDE-S4-v1`.** For any literal two-coordinate block decomposition `A=[[B,C],[C^T,D]]`, `s_8(A)>=1` implies `s_4(D)>=1`, because the complete two-anchor star `[[B,C],[C^T,0]]` has rank at most four.
3. In the invertible weak-self subchamber, if `P` projects onto `row(C)`, the Schur count plus another rank shift gives
   \[
   s_2((I-P)D(I-P))\ge1.
   \]
   Thus two unit quadratic Hessian directions survive on the affine fibers of the strong projection `CY`, uniformly as `det B ->0`.

Combining these with the completed account03/B15 terminal collapse localizes the remaining normalized `s_8` no-pivot obligation to a three-dimensional integrated statement: for a strong physical two-row cross map with `det(CC^T)>=0.3649442658...` and outside matrix `D` with `s_4(D)>=1`, prove a universal `L^2` density bound for

\[
(CY+u,\;Y^TDY+v^TY+w).
\]

This would close the weak-self terminal branch through the relay without ever paying `1/sqrt(|det B|)`. That joint-`L^2` theorem remains **OPEN**.

The same improvement proves an actual strict `s_8` family
\[
Q_B=X^TBX+4X\cdot Y+\sum_{j=1}^4Z_j^2,
\qquad \|B\|_{op}\le1/2,
\]
with
\[
\|p_{Q_B}\|_\infty
\le {3\pi^{1/3}\over2^{4/3}}
=1.743671027264439\ldots,
\qquad p_{Q_B}\in C_0.
\]
Its coefficient matrix has at least eight eigenvalues of modulus at least one.

## Designated account04/B16 application

I also applied the completed account04/B16 definite-plane exit to that same strict family. Conditioning on every variable except `(Z_1,Z_2)` leaves the definite plane `H=I_2`, so the partner theorem gives the independent valid bound
\[
\|p_{Q_B}\|_\infty\le2\pi.
\]
The new joint-`L^2` relay sharpens this to `1.743672` on the family. Partner source: `proofnet24/QFORM-density/fleet-2026-09-22/account04/B16/20260924T041516Z-account04-B16-QFORM-r4/REPORT.md`, blob `6373fddaeb3206e86af61fc7b48eeb6f39e34666`.

## Final status

- pinned 17-eigenvalue theorem: **PASS in this complete B16 audit**;
- support package: **present and internally consistent; finite checks remain diagnostic**;
- nine-eigenvalue replacement candidate: remains supported by earlier independent reconstructions; release/validation accounting is separate;
- general eight-eigenvalue theorem: **OPEN**;
- new two-anchor joint-`L^2` relay: **PROVED**;
- full three-eigenvalue conjecture: **OPEN / NOT PROVED / NOT DISPROVED**;
- global continuity for the unrestricted/fixed-multiplicity theorem: **not claimed**; the new relay itself yields `C_0` whenever its `L^2` joint-density hypothesis is met.

No Gaussian, log-concavity, moment, compact-support, connected-support, diagonal-basis, post-rotation independence, arbitrary-joint coarea, or false pointwise rough-phase hypothesis was introduced.
