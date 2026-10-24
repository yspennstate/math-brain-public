# account01/B09 r11 — full baseline audit

Objective: `QFORM-FIXED-MULTIPLICITY-AUDIT-20260924`  
Actual run sign-in: `2026-09-24T13:48:30Z`  
Baseline source commit: `7c0d6e60946b19423e6400a12d34b473cf0591e2`  
Pinned manuscript blob: `183ccd294763214e6a707e8d4749ff9a8cf7006d`  
Reported source SHA-256: `9f3bdec0b88debe9a66076c7b4a5cc894fb14e69b89591a4107e785340f65e69`  
Fresh live master observed before publication work: `3c07ea9e59c45aa5a2151812e932bc85d5959461`.

## Verdict

**PASS** for the complete 790-line baseline theorem:

> for independent real coordinate densities bounded by `K`, arbitrary real symmetric `A`, arbitrary affine `b,c`, and `s_17(A)>=s>0`, the law of `X^TAX+b^TX+c` has an essentially bounded density with `||p||_infinity<=10000 K^2/s`.

I found no fatal or theorem-changing mathematical gap. The full theorem asserts essential boundedness, not global continuity. The unrestricted three-eigenvalue conjecture is not proved by this manuscript.

## Line-by-line / statement audit

The complete source lines 1--790 were read in this run. `proof_map.csv` was checked against the manuscript ranges. Status by proof block:

- **PASS, lines 47--87**: theorem quantifiers, normalization architecture, pivot/no-pivot split, and the distinction between nonsymmetric deterministic auxiliaries and the original symmetric quadratic form are stated consistently.
- **PASS, lines 91--160** (`lem:fourier`, `lem:envelope`, `lem:riesz`): Fourier normalizations, Gaussian inversion, Plancherel, the power envelope, the Riesz/negative-half-moment representation and constants are correct. Tonelli is used only on nonnegative majorants where required.
- **PASS, lines 169--217** (`lem:rank`, `lem:schur`, `lem:dd`): singular-value perturbation is valid without symmetry; the Schur spectral count is valid, including the singular-matrix approximation; strict row diagonal dominance is correctly applied to nonsymmetric blocks.
- **PASS, lines 221--255** (`thm:bl`): the heat-flow Brascamp--Lieb proof has the correct sign, frame contraction, limiting Gaussian normalization, and rough-function monotone approximation.
- **PASS WITH NONFATAL WORDING ISSUE, lines 258--282** (`lem:projection`): the projection-density theorem is correct. After rows with `b_i=0` are dropped, the displayed sentence `sum_i(1-b_i)=d` is literally true only if the zero rows are included in that sum. Over the retained rows one has `sum_{b_i>0}(1-b_i)<=d`, which is sufficient for the same `e^{d/2}` bound. No downstream constant changes.
- **PASS, lines 284--301** (`lem:scalar-fourier`): convolution cap, even-power interpretation, scaling and inversion at zero are valid.
- **PASS, lines 310--400** (`lem:decoupling`, `thm:determinant`, `cor:vol-fourier`): the two/four power decoupling, determinant regularizer, Brascamp--Lieb weights, Jacobian scales, trace identity and exponent `-1/8` check. Order five gives an integrable density envelope; order three is used only with the `|t|^{-1/2}` Riesz weight.
- **PASS, lines 404--525** (`lem:square`, `lem:definite`, `lem:hyperbola`, `lem:quarter`): all changes of variables and conditioning statements retain original-coordinate independence. The hyperbolic Jacobian/tail cutoffs and quarter-power coefficient are sufficient at the stated constants; the exceptional critical level is handled measure-theoretically rather than pointwise.
- **PASS, lines 528--580** (`def:pivot-volume`, `lem:sampling`, `lem:completion`): the no-pivot entry bound is correct; the bordered-determinant identity is exact; the `(r+1)^2` multiplicity is an upper count (not a false equality when singular seeds occur); the completion has zero-diagonal `E`, `D=0` on the seed, global `rank R<=3r`, and restricted `rank R[L,L]<=r`.
- **PASS, lines 582--619** (`prop:volume`; B09 starting lens): this is the sensitive step and is correct. With `m=4k-3`, `||E||<=eps<=1/16`, nonsymmetric singular-value perturbation gives `s_m(D+R)>=1-eps`, and `rank R<=3r` gives `s_{m-3r}(D)>=1-eps`. Since `m>=4r+1`, at least `r+1` large diagonal entries of `D` exist; because `D` vanishes on the seed, all lie in `L`. On the corresponding `H`, `|R_ii|>=371/400` and `|R_ij|<1/7+1/16`; for `r<=4` the off-diagonal row sum is `<23/28`. The exact strict margin is
  `371/400-23/28=297/2800>0`,
  hence `R[H,H]` has rank `r+1`, contradicting `rank R[L,L]<=r`. This uses singular values of the nonsymmetric auxiliary exactly as required.
- **PASS, lines 621--645** (`lem:cut`, `cor:no-pivot`): ordered disjoint-minor sampling has expectation factor `4^{-k}`, and the `k=3,5` analytic consequences and constants follow.
- **PASS, lines 654--724** (`lem:kernels`, `prop:pivot-H`, `prop:nine`): the two singular kernels, scalar/definite/indefinite pivot alternatives, truncated-to-full half-potential step, Schur spectral counts and numerical constants close as written.
- **PASS, lines 726--749** (main theorem proof): no-pivot, scalar-pivot and pair-pivot branches exhaust the normalized problem. The largest displayed branch is `6010<10000`; the general scaling `Y=KX`, `Q=(s/K^2) Qtilde` yields exactly `10000 K^2/s`.
- **PASS, lines 751--790**: threshold accounting and limitations correctly state what the manuscript does and does not prove.

## Package audit

Fresh root package now contains and I read: `README.md`, `DELIVERY_STATUS.md`, `AUDIT.md`, `proof_map.csv`, `SOURCE_MANIFEST.json`, `verify.py`, `checks.json`, and the full `manuscript.tex`. `checks.json` records PASS for 534 exact interpolation seeds, 18 exact volume-sampling cases (9 strict), 240 numerical Schur-threshold cases and 30 graph-weight cases, including the exact diagonal-dominance slack `297/2800`. I read the checker source and its limitations; these finite checks are diagnostics, not proof.

## UNCHECKED / non-proof items

- I did not independently rerun the compiled-PDF build or visually inspect the binary PDF in this run; the PDF is not stored in this GitHub root. This has no effect on the mathematical source proof.
- I did not independently recompute the manifest SHA-256 from raw bytes in a local shell; the Git blob read in this run is exactly `183ccd294763214e6a707e8d4749ff9a8cf7006d`, and the manifest reports the pinned SHA-256 above.
- I did not treat BCCT/Rudelson--Vershynin priority/attribution as mathematical dependencies; every specialized input used in the proof is reproved in the manuscript.

## Threshold status discovered after baseline audit

After completing the baseline read, I read the current complete nine-direction replacement and its genuinely separate full audits. The unconditional `s_9` theorem is now supported by a complete replacement proof plus at least two separate complete reconstruction/PASS artifacts. I record the threshold synthesis separately in this run's improvement note rather than modifying the pinned 17-direction manuscript here.
