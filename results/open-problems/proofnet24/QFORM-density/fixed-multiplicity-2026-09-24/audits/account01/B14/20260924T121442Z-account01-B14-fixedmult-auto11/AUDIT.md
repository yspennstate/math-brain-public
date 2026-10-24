# account01/B14 full audit — fixed multiplicity 17

Run: `20260924T121442Z-account01-B14-fixedmult-auto11`  
Objective: `QFORM-FIXED-MULTIPLICITY-AUDIT-20260924`  
Reviewer: `account01/B14`  
Execution status: `WITHOUT_VERIFIED_BRAIN`.

## Source pin and package state

Baseline commit requested by the owner: `7c0d6e60946b19423e6400a12d34b473cf0591e2`.

The manuscript at the baseline and on fresh master has the same actual Git blob:

`183ccd294763214e6a707e8d4749ff9a8cf7006d`.

Fresh master was resolved at the start and again before writing; the latter observed head was `1dab25580592c69084c149ebc42e6d9e999acef6`. The manuscript blob was unchanged. The package/owner metadata reports SHA-256 `9f3bdec0b88debe9a66076c7b4a5cc894fb14e69b89591a4107e785340f65e69`; because `SOURCE_MANIFEST.json` is absent on current master, this run treats the Git blob above as the independently repository-verified source identity rather than claiming to have recomputed the SHA-256 externally.

Present and read in full: `manuscript.tex` (790 lines), `README.md`, `AUDIT.md`.

Requested supplementary files were not present at the package root on fresh master: `SOURCE_MANIFEST.json`, `proof_map.csv`, `verify.py`, `checks.json` all returned 404 / were absent from the directory listing. Therefore claims in README/AUDIT that those checker/manifest files are part of the canonical bundle are **GAP (packaging/provenance)**, and the advertised executable checks are **UNCHECKED** in this run. This is not a mathematical gap in the self-contained manuscript.

## Verdict

**Mathematical theorem: PASS.** I found no fatal mathematical defect in the theorem proved by the pinned 790-line manuscript: for independent real coordinates with densities bounded by `K`, arbitrary real symmetric `A` with `s_17(A)>=s>0`, and arbitrary affine terms, the quadratic polynomial has an essentially bounded density. The manuscript's stated `10000 K^2/s` bound is valid. The full three-eigenvalue problem is not proved.

**Packaging: GAP.** The four supplementary files named above are absent.

**Density-representative wording: GAP-PRESENTATION / theorem unaffected.** The hypothesis `f_i<=K` is naturally an a.e. statement, while a few inverse-branch/coarea formulas write pointwise values of density representatives. At the start one should explicitly replace every marginal density by a Borel representative equal a.e. to it and truncated pointwise into `[0,K]`. This changes no law and makes all later pointwise caps literal. The projection lemma already makes this choice locally; making it global removes the only representative ambiguity I found.

No other `FALSE` item was found.

## Complete forward review, exact source ranges

| Source range | Status | Audit conclusion |
|---|---|---|
| `manuscript.tex:L1-L40` | PASS | Preamble, notation, abstract/scope and theorem framing are consistent; no full-three claim is made. |
| `L41-L80` | PASS | Main theorem, normalization, parameter choices and proof architecture preserve arbitrary signature, arbitrary affine terms, arbitrary dimension and rough independent laws. `Y=KX` gives cap one and final density scaling `K^2/s`. |
| `L81-L160` | PASS | Plancherel/inversion/Riesz preliminaries. Gaussian regularization uses only `L1∩L2`; approximate identity convergence and weak convergence identify the limiting law without assuming a density first. Tonelli handles the nonnegative negative-half-moment representation. No moment/support bound is used. |
| `L161-L220` | PASS | Singular-value perturbation/rank estimates, Schur spectral count and strict diagonal dominance. In the singular ambient Schur proof the moving threshold is valid by continuity of the ordered eigenvalue moduli after `A+eps I`. |
| `L221-L282` | PASS | Geometric Brascamp–Lieb heat-flow proof and product projection bound. The frame identity has the correct sign; the large-time dominated limit and small-time Fatou/monotone approximation handle unbounded rough inputs. No independence after deterministic rotation is used. |
| `L283-L400` | PASS | Scalar Fourier powers, decoupling, determinant theorem and crossing-volume envelopes. Difference coordinates remain independent and cap one; all pre-estimate integrands have modulus at most one. The graph-BL scales and entropy factors cancel correctly, giving `det(I+t^2 M^TM/(pi^2 e^2))^(-1/8)`. `k=5` gives an integrable `|t|^-5/4` receiver; `k=3` is used only after the Riesz weight. |
| `L401-L526` | PASS | Scalar-square profile, definite-pair coarea, hyperbolic-pair logarithmic envelope and quarter-power concentration. Conditional statements are valid as measure domination through nonnegative test functions; null critical levels need no common pointwise conditional-density version. Hyperbolic tails use only cap and total mass, so translations/unbounded supports are harmless. |
| `L527-L651` | PASS | Disjoint volumes, volume-sampled interpolation, completion, no-pivot spectral-to-volume proposition, random cut and no-pivot analytic consequences. The bordered-minor identity, `rank R<=3r`, restricted `rank R[L,L]<=r`, and terminal diagonal-dominance constants were independently recomputed. Nonsymmetric auxiliaries are handled with singular values, as required. |
| `L652-L760` | PASS | Two singular kernels, pivot half-potential, nine-eigenvalue half-potential and main theorem. Scalar conditioning uses Tonelli domination rather than false independence; definite/indefinite pair bounds are uniform in conditioning-generated affine terms; Schur counts lose exactly the pivot dimension. All normalized main branches close. |
| `L761-L790` | PASS | Threshold accounting, limitations and acknowledgments accurately describe what was and was not proved. The manuscript explicitly does not infer bounded density from the order-three envelope and does not claim the `s_3` theorem. |

## Rough-law / measurability audit

The following compiler justifies every conditional density use without choosing conditional densities on a common exceptional-free set.

**Integrated conditional domination lemma.** Let `nu` be a finite positive measure on an environment space, `mu_y` a measurable probability/subprobability kernel on `R`, and `k(y,z)>=0` jointly Borel. If for `nu`-a.e. `y` and every nonnegative Borel `h`,

`int h(z) mu_y(dz) <= int h(z) k(y,z) dz`,

then the mixture `mu(B)=int mu_y(B)nu(dy)` is dominated by `K(z)dz`, where `K(z)=int k(y,z)nu(dy)`. This is immediate from Tonelli. In particular an a.e. bound `K<=C` yields an essentially bounded output density `<=C`.

This applies directly to all three pivot receivers:

1. scalar pivot: `k(y,z)=|a|^(-1/2)|z-R(y)|^(-1/2)` after discarding the favorable one-sided indicator;
2. definite pair: `k=pi/sqrt(|det B|)`;
3. indefinite pair: `k(y,z)=D^(-1/2)[6+log_+(16sqrt(D)/|z-R(y)|)]`, allowing `+infinity` on the null critical graph.

All `R(y)` are Borel quadratic polynomials in original coordinates. The quarter-power lemma supplies the only required logarithmic integrability. Thus arbitrary translations, disconnected/unbounded supports, absence of moments, and conditioning-generated affine terms remain inside the proof.

## Reverse dependency review (second complete pass; same reviewer, not independent validation)

I separately traced the proof backward from the main conclusion.

- Main no-pivot density branch needs order-five crossing volume; Corollary `vol-fourier` supplies it from the determinant theorem; the random cut supplies physical cross volume from `V_5`; Proposition `volume` supplies `V_5>=kappa^5` from no pivot plus `s_17>=1`.
- Main scalar-pivot branch reduces to a Schur complement with at least sixteen large directions; only nine are required by Proposition `nine`; that proposition reduces either to the pivot truncated half-potential or the no-pivot order-three/Riesz receiver.
- Main definite pair is a direct two-dimensional coarea bound uniform in all affine terms.
- Main indefinite pair leaves a Schur remainder with at least one large spectral direction; quarter-power concentration controls its logarithmic potential, which is exactly the singularity in the hyperbolic conditional density.
- Every Fourier/conditional transition above was rechecked for `sigma`-finiteness, nonnegative Tonelli or bounded-integrand Fubini. No step needs finite moments or bounded support.

This reverse pass produced the same mathematical verdict: **PASS**. Since both passes were performed by `account01/B14`, they count as one reviewer for the owner's independent-validation requirement; this report does not self-certify the manuscript as independently validated by two reviewers.

## Items not independently verified here

- `proof_map.csv`, `SOURCE_MANIFEST.json`, `verify.py`, `checks.json`: **UNCHECKED / absent**.
- The README/AUDIT claims that those finite scripts/checks ran successfully: **UNCHECKED**, because the artifacts are absent.
- A fresh LaTeX compile of `manuscript.tex`: **UNCHECKED** in this run; the mathematical source was read directly and no syntax issue material to the proof was found.
- Bibliographic metadata beyond what is needed for the self-contained argument: **UNCHECKED**; no external theorem from the bibliography is being used without a proof in the manuscript except standard background formulations already reproved where needed.

## Fatal-gap check

No fatal mathematical gap was found. The only repository-level defect found promptly is the absent advertised audit/checker package. The only proof-presentation patch recommended is the global bounded Borel representative convention. Neither changes the 17-direction theorem.
