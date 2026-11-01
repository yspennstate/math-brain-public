# fleet01/B04 fixed-multiplicity audit r12

Run id: `20260924T144124Z-fleet01-B04-fixedmult-audit-r12`

## Source pin and status

- Baseline source commit requested by owner: `7c0d6e60946b19423e6400a12d34b473cf0591e2`.
- `master` observed immediately before this immutable write: `1b5ca30ed88b6cefed3a064db71a35798da6473a`.
- Audited manuscript path: `proofnet24/QFORM-density/fixed-multiplicity-2026-09-24/manuscript.tex`.
- Audited manuscript git blob: `183ccd294763214e6a707e8d4749ff9a8cf7006d`.
- Audited manuscript SHA-256: `9f3bdec0b88debe9a66076c7b4a5cc894fb14e69b89591a4107e785340f65e69`.
- Audited manuscript length: 790 lines, 47883 bytes.

The theorem is treated only as a **candidate**. This report is one worker's audit, not independent validation, and it does not concern the full three-eigenvalue conjecture.

## Package audit

I read in full `README.md`, `AUDIT.md`, `proof_map.csv`, `SOURCE_MANIFEST.json`, `verify.py`, `checks.json`, and all 790 source lines of `manuscript.tex` from fresh `master`.

The package-level missing-file concern recorded in my preceding B04 run is **RESOLVED**: `proof_map.csv`, `SOURCE_MANIFEST.json`, `verify.py`, and `checks.json` are now present. `checks.json` records a PASS for its delivery-reproducibility suite, including 534 interpolation seeds, 18 volume-sampling cases, 9 strict-sampling cases and exact diagonal-dominance slack `297/2800`. I inspected the support code and recorded output, but I did **not** independently execute `verify.py` in this run. Therefore the proposition "the stored `checks.json` was produced by executing this exact `verify.py` in this run" is **UNCHECKED** here. None of the mathematical PASS judgments below relies on that proposition.

## Verdict

**PASS (mathematical audit of the pinned 790-line manuscript).** I found no FALSE assertion and no proof GAP in the written 17-eigenvalue argument. All source lines, displayed equations, definitions and proofs were checked in this run. There are no manuscript regions marked UNCHECKED.

This PASS is deliberately narrower than validation: the candidate still requires genuinely separate end-to-end reviews under the owner gate.

## Complete source coverage

The following gives exact source ranges and verdicts. Interstitial prose/equations inside the listed ranges were checked together with the named result; the remaining front matter, notation, section transitions and final discussion were also read line by line.

| Source range | Item | Verdict | Audit reason |
|---|---|---|---|
| 1--46 | front matter, hypotheses, notation and theorem setup | PASS | Quantifiers remain arbitrary dimension, independent real coordinates with densities `<=1`, arbitrary symmetric signs/spectrum and affine terms; no rotated-independence assumption is introduced. |
| 47--57 | `thm:main` statement | PASS | Statement is the fixed-multiplicity candidate, not the three-eigenvalue conjecture. Scaling and affine quantifiers match later proof. |
| 59--61 | `cor:33` statement | PASS | Direct specialization of main theorem. |
| 62--90 | Fourier convention, density/small-ball preliminaries and notation | PASS | Fourier inversion normalization and density-versus-interval concentration usage are consistent with later `1/(2pi)` factors. |
| 91--120 | Lemma `lem:fourier`, statement 91--106, proof 107--120 | PASS | Plancherel/inversion/convolution conventions are mutually consistent. No unjustified pointwise Fourier decay is used. |
| 122--130 | Lemma `lem:envelope`, statement 122--127, proof 128--130 | PASS | Elementary integration of the power envelope is correct, including endpoint exponents. |
| 132--160 | Lemma `lem:riesz`, statement 132--143, proof 144--160 | PASS | Layer-cake/rearrangement computation has the correct exponent and handles arbitrary bounded densities without support assumptions. |
| 161--168 | transition and singular-value notation | PASS | Definitions agree with the later Weyl/rank uses. |
| 169--181 | Lemma `lem:rank`, statement 169--176, proof 177--181 | PASS | Singular-value perturbation and rank interlacing are used with correct index shifts. |
| 183--207 | Lemma `lem:schur`, statement 183--190, proof 191--207 | PASS | Congruence/Schur-complement counting is applied only where the principal pivot is invertible; signs are retained. |
| 209--217 | Lemma `lem:dd`, statement 209--212, proof 213--217 | PASS | Strict row diagonal dominance implies nonsingularity exactly as used later. |
| 218--220 | BL setup | PASS | Exponents/vectors match the geometric frame normalization. |
| 221--255 | Theorem `thm:bl`, statement 221--231, proof 232--255 | PASS | Full heat-flow proof checked separately below. |
| 258--282 | Lemma `lem:projection`, statement 258--264, proof 265--282 | PASS | Rank-one BL normalization, leverage weights and limiting regularization give the claimed product-projection density cap. |
| 284--301 | Lemma `lem:scalar-fourier`, statement 284--290, proof 291--301 | PASS | `m=floor(p/2)>=p/4`, Fourier inversion at zero and projection bound give `2pi sqrt(2e)/sqrt(p)` with correct constants. |
| 302--309 | cross-block setup | PASS | `F` and `G` retain arbitrary same-bank curvature and affine terms. |
| 310--324 | Lemma `lem:decoupling`, statement 310--317, proof 318--324 | PASS | The independent-copy expansion, Cauchy--Schwarz/Jensen powers and product Fourier factors are correct; all pre-estimate integrands have modulus at most one. |
| 326--373 | Theorem `thm:determinant`, statement 326--332, proof 333--373 | PASS | Regularized frame identity, graph BL weights, scalar Fourier exponent `2/d_i`, entropy tax and choice `alpha=(2pi e)^2` cancel correctly; fourth root yields exponent `-1/8`. |
| 374--385 | elementary-symmetric-volume definitions | PASS | Cauchy--Binet expansion of `Z_k` and determinant polynomial normalization are correct. |
| 386--400 | Corollary `cor:vol-fourier`, statement 386--397, proof 398--400 | PASS | `k=5` gives integrable Fourier decay; `k=3` gives the stated half-potential estimate; `k=4` is correctly retained only as the critical `1/|t|` endpoint. |
| 401--403 | pivot-section setup | PASS | No hidden support/moment assumptions. |
| 404--414 | Lemma `lem:square`, statement 404--411, proof 412--414 | PASS | One-dimensional square profile and scaling are correct. |
| 415--422 | two-variable setup | PASS | Conditioning variables remain original independent coordinates. |
| 423--434 | Lemma `lem:definite`, statement 423--425, proof 426--434 | PASS | Same-sign quadratic pair is handled by convolution/profile bounds with correct determinant scaling. |
| 437--482 | Lemma `lem:hyperbola`, statement 437--444, proof 445--482 | PASS | Hyperbolic linear change is used analytically, not to assert new independence; logarithmic kernel and density estimate are correctly integrated. |
| 485--525 | Lemma `lem:quarter`, statement 485--494, proof 495--525 | PASS | Quarter-power concentration, conditioning and Hölder exponents are correct; rough densities are handled through distribution-function bounds. |
| 526--544 | pivot-volume definition and no-pivot entry bounds, including `def:pivot-volume` 528--535 | PASS | Ordered disjoint minors and `|a_ij|<1/7` consequence follow from the stated `eta`; no eigenbasis rotation is made. |
| 545--564 | Lemma `lem:sampling`, statement 545--556, proof 557--564 | PASS | Volume sampling and bordered determinant identity are correct; the `(r+1)^2` multiplicity is an upper bound, as explicitly stated. |
| 566--580 | Lemma `lem:completion`, statement 566--577, proof 578--580 | PASS | Decomposition `A=D+R+E`, restricted `LxL` rank and global `rank R<=3r` follow from the interpolation support pattern. |
| 582--619 | Proposition `prop:volume`, statement 582--587, proof 588--619 | PASS | Telescoping volume ratio, perturbation, singular-value rank shift and strict diagonal-dominance contradiction are consistent; crucially the proof uses singular values for nonsymmetric `A-E`. |
| 621--630 | Lemma `lem:cut`, statement 621--627, proof 628--630 | PASS | Each ordered disjoint `(S,T)` survives a fair physical cut with probability `4^{-k}`. |
| 632--645 | Corollary `cor:no-pivot`, statement 632--640, proof 641--645 | PASS | For `k=3,5`, `Z_k^{-1/(2k)}<=160`; the half-potential and `L^infty` constants are arithmetically consistent. |
| 646--653 | pivot half-potential setup | PASS | Truncation and conditioning variables are explicit. |
| 654--674 | Lemma `lem:kernels`, statement 654--664, proof 665--674 | PASS | Both singular integrals are finite with the stated elementary bounds. |
| 676--714 | Proposition `prop:pivot-H`, statement 676--681, proof 682--714 | PASS | Diagonal-pivot and 2x2-pivot cases use the square/definite/hyperbolic profiles with correct conditioning; no rough-law continuity assumption is inserted. |
| 716--724 | Proposition `prop:nine`, statement 716--721, proof 722--724 | PASS | Combines no-pivot `s_9` half-potential and pivot half-potential with the stated universal constant. |
| 725--749 | proof of `thm:main` and `cor:33` | PASS | Main split into pivot/no-pivot cases is exhaustive; the 17 threshold corresponds to the `k=5` no-pivot volume branch, while the pivot branch uses the nine-eigenvalue half-potential after a valid Schur count. Scaling gives the stated `K^2/s` dependence. |
| 750--790 | remarks, constants, acknowledgments/references/end matter | PASS | No later prose upgrades the candidate into an independently validated theorem or the full three-eigenvalue conjecture; cited uses match the proof's actual scope. |

## Geometric Brascamp--Lieb heat-flow audit (lines 221--255)

This was the starting lens and was re-derived rather than merely syntax-checked.

Let `f_i=g_t*h_i`, `v_i=(log f_i)'`, and
`F(x,t)=prod_i f_i(u_i dot x)^{c_i}` under the frame identity
`sum_i c_i u_i u_i^T=I`. The heat equation gives

`(partial_t-Delta)F = F[sum_i c_i v_i^2 - |sum_i c_i u_i v_i|^2]`.

The bracket is nonnegative because, with `w_i=sqrt(c_i)v_i` and the synthesis operator `T w=sum_i sqrt(c_i)u_i w_i`, the frame identity is `TT^*=I`; hence `||T||<=1` and `|Tw|^2<=sum_i c_i v_i^2`. Thus the derivative sign is correct.

For compact positive-time intervals, convolution with the Gaussian gives smooth positive factors with sufficient Gaussian domination after the manuscript's bounded/truncated first stage; the spatial Laplacian integrates to zero by integration by parts. Therefore the integral of `F` is monotone in time in the required direction. The `t->infinity` rescaling/Gaussian limit has the stated normalization, and the `t downarrow 0` passage uses Lebesgue points/Fatou in the correct inequality direction. Monotone truncation then extends the inequality from bounded compactly supported approximants to arbitrary nonnegative `L^1` factors. I found no derivative-sign reversal, lost boundary term, or approximation step requiring compact support of the original coordinate laws.

## Support-file status

- `proof_map.csv`: **PASS** as a map of the named theorem/lemma source ranges; the ranges agree with the audited source.
- `SOURCE_MANIFEST.json`: **PASS** for the manuscript blob/SHA/line/byte metadata and for explicitly labelling the review state as non-formal/non-independent.
- `README.md`: **PASS** as package description; it does not replace proof verification.
- `AUDIT.md`: **PASS AS HISTORICAL SELF-REPORT ONLY**. Its assertions were not used as independent evidence.
- `verify.py`: source read in full; **UNCHECKED EXECUTION IN THIS RUN**.
- `checks.json`: read in full; it records `status: PASS`, but **UNCHECKED AS A FRESH EXECUTION IN THIS RUN**. Its own limitations correctly say it is not formal verification or an independent end-to-end audit.

## New audit-derived improvement and multiplicity status

A separate immutable improvement from this run proves a packetwise Hölder--Brascamp--Lieb interpolation theorem. It strictly enlarges the order-four analytic region: an order-four crossing can be split into a rank-one packet and a rank-three packet, with unequal Hölder exponents, and becomes Fourier-integrable whenever the rank-three packet has physical row leverage strictly below one and the corresponding packet volumes are quantitative. An exact random-partition lemma guarantees a `1+3` packet split with

`Z_1(M_1) Z_3(M_2) >= (27/64) Z_4(M)`.

However this does **not** yet prove the 13-eigenvalue theorem, because the volume-good split need not have a dimension-free leverage gap below one, and the weighted currency involves `Z_1^{q-1} Z_3`, not merely `Z_1 Z_3`. Near-coloop order-four crossings remain the structural obstruction. Therefore the rigorous unconditional threshold remains 17 in this report.

## Final classification

- Manuscript mathematical audit: **PASS**.
- Fatal defect found: **none**.
- Entire manuscript checked: **yes, lines 1--790**.
- Fresh execution of `verify.py`: **UNCHECKED**.
- Independent validation gate: **not satisfied by this report**.
- Unconditional multiplicity reduction established in this run: **none**; threshold remains 17.
- New rigorous supporting improvement: packetwise Hölder--BL determinant interpolation plus the `27/64` order-four packet-split lemma.
