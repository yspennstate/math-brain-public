# account01/B20 r12 — release-gate audit and threshold accounting

Objective: `QFORM-FIXED-MULTIPLICITY-AUDIT-20260924`  
Run: `20260924T132100Z-account01-B20-fixedmult-r12`  
Pinned baseline source commit: `7c0d6e60946b19423e6400a12d34b473cf0591e2`  
Pinned manuscript git blob: `183ccd294763214e6a707e8d4749ff9a8cf7006d`  
Pinned manuscript SHA-256: `9f3bdec0b88debe9a66076c7b4a5cc894fb14e69b89591a4107e785340f65e69`  
Fresh-master manuscript blob read in this run: `183ccd294763214e6a707e8d4749ff9a8cf7006d`.

## Release-gate verdict

**PASS for the mathematical 17-eigenvalue theorem in this independent B20 reconstruction.** I read the complete 790-line source and reconstructed the dependency chain rather than adopting the authoring self-audit or peer PASS labels. I found no fatal or repair-requiring mathematical gap in the pinned manuscript.

The exact theorem audited is

\[
s_{17}(A)\ge s>0
\quad\Longrightarrow\quad
\|p_{X^TAX+b^TX+c}\|_\infty\le10^4K^2/s
\]

for arbitrary dimension, arbitrary real symmetric `A`, arbitrary signature and remaining spectrum, arbitrary affine terms, and independent arbitrary real coordinate densities bounded by `K`. No moment, iid, compact-support, log-concavity, smoothness, Gaussianity, or rotated-independence hypothesis is introduced.

The unrestricted three-eigenvalue conjecture remains **OPEN**. The manuscript's global conclusion is essential boundedness; only the no-pivot Fourier-inversion branch automatically gives a continuous density.

## Package and finite-check status

The package gap reported by some earlier workers is now resolved on fresh `master`: `SOURCE_MANIFEST.json`, `proof_map.csv`, `verify.py`, and `checks.json` are present together with `README.md`, `AUDIT.md`, and the unchanged manuscript. `SOURCE_MANIFEST.json` records the same 47,883-byte / 790-line source and the same blob/SHA pin above. The delivered `checks.json` reports PASS for 534 exact interpolation seeds, 18 exact volume-sampling cases, 9 strict-sampling cases, exact diagonal-dominance slack `297/2800`, plus 240 floating Schur diagnostics and 30 floating graph-weight diagnostics. I inspected `verify.py`; those checks are correctly scoped as finite reproducibility diagnostics, not proof certificates.

## Reconciliation of the singular-Schur disagreement

An earlier account01/B18 review labeled the singular limiting paragraph of `lem:schur` (source lines 205--207) a GAP because its threshold is `t-|epsilon|`. I independently reconstructed this point and **reject that GAP diagnosis**. The baseline moving-threshold argument is valid; no eigenvalue convergence rate is needed.

Let

\[
m=\max\{N_A(t)-k,0\}.
\]

Choose a sequence `epsilon -> 0` for which both `A+epsilon I` and the pivot block `B+epsilon I` are invertible. The Schur complements `S_epsilon` converge to `S`. For every eigenvalue `lambda` of `A` with `|lambda|>=t`,

\[
|\lambda+\epsilon|\ge t-|\epsilon|,
\]

so

\[
N_{A+\epsilon I}(t-|\epsilon|)\ge N_A(t).
\]

The already-proved invertible case therefore gives

\[
N_{S_\epsilon}(t-|\epsilon|)\ge m,
\]

or equivalently, when `m>0`,

\[
s_m(S_\epsilon)\ge t-|\epsilon|.
\]

Ordered singular values/eigenvalue moduli are continuous under matrix convergence, hence

\[
s_m(S)=\lim_{\epsilon\to0}s_m(S_\epsilon)\ge t.
\]

Thus `N_S(t)>=m=N_A(t)-k` whenever the latter is positive, proving the lemma. The concern that an eigenvalue could approach the threshold at speed `C|epsilon|` is irrelevant because the conclusion follows from the lower bound on the *ordered m-th modulus*, not from tracking individual threshold crossings. A fixed-`delta` rewrite is a permissible clarity improvement, but it is not required to repair correctness.

This reconciliation matters downstream: the scalar-pivot half-potential, scalar-pivot main branch, and indefinite-pair main branch use `lem:schur`; all are valid from the baseline proof as written.

## Complete proof-map ledger

Every source line belongs to one of the following ranges or connective/presentation text between them. `PASS` below means I reconstructed the displayed statement and its invocation independently in this run.

| Source range / label | Status | Reconstruction and downstream check |
|---|---|---|
| 1--46, metadata/definitions/architecture | PASS | Macros do not hide hypotheses. The theorem architecture distinguishes pivot/no-pivot and full/truncated potentials correctly. |
| 47--57 `thm:main` | PASS | Quantifiers and scaling target are exactly arbitrary product densities `<=K`, symmetric `A`, arbitrary `b,c`, `s_17>=s`. |
| 59--61 `cor:33` | PASS | Immediate from monotonicity of ordered singular values. |
| 81--120 `lem:fourier` | PASS | Fourier convention, Plancherel factor `2pi`, inversion factor `(2pi)^-1`, Gaussian inversion and rough-law weak limit are consistent. |
| 122--130 `lem:envelope` | PASS | Envelope integral is exactly `2ap/(p-1)` and inversion gives `ap/[pi(p-1)]`. |
| 132--160 `lem:riesz` | PASS | Gamma representation, Tonelli order, Gaussian inversion and weighted integral give coefficient `1/sqrt(2pi)` and the stated `12 sqrt(u/(2pi))`. |
| 169--181 `lem:rank` | PASS | Approximation-number proof works for nonsymmetric matrices; both perturbation and rank-shift forms are used in correct directions. |
| 183--207 `lem:schur` | PASS | Invertible compression argument is valid; singular moving-threshold limit is valid by the ordered-modulus argument written above. |
| 209--217 `lem:dd` | PASS | Strict row diagonal dominance implies invertibility without symmetry. |
| 221--255 `thm:bl` | PASS | Heat-flow derivative has correct sign from the frame contraction. Differentiation/IBP, large-time Gaussian limit, small-time Fatou and truncation are justified. |
| 258--282 `lem:projection` | PASS with nonfatal wording issue | Marginal/change-of-variables and BL scaling are correct; no rotated independence is asserted. If the entropy sum is read only over retained `b_i>0`, the text should write `sum(1-b_i)<=d`; equality holds if zero-`b_i` indices are included. Needed bound unchanged. |
| 284--301 `lem:scalar-fourier` | PASS | Difference density cap, even-power inversion, projection coefficient norm and `p>=2` rounding are correct. |
| 310--324 `lem:decoupling` | PASS | Cauchy--Schwarz eliminates same-bank phases and differences retain independent cap-one coordinate densities. |
| 326--373 `thm:determinant` | PASS | Frame weights, Jacobian, `L^{1/c}` scaling, scalar Fourier exponents, entropy term, `alpha=(2pi e)^2`, and fourth-root exponent `-1/8` all rederive exactly. |
| 386--400 `cor:vol-fourier` | PASS | Cauchy--Binet order-k term yields exponent `k/4`; k=5 is integrable and k=3 combines with the Riesz weight only. |
| 404--414 `lem:square` | PASS | Two inverse branches and interval inverse-image length are correct; later use is conditional measure domination, not independence. |
| 423--434 `lem:definite` | PASS | Deterministic 2D polar/elliptic change gives `pi M/sqrt(|det B|)`; rotations are not used to transfer product independence. |
| 437--482 `lem:hyperbola` | PASS | Hyperbolic parameterization, Jacobian, original-coordinate tail choice, bathtub bound, middle interval and `Lambda>=2/sqrt D` close for rough laws through test-function/Tonelli formulation. |
| 485--525 `lem:quarter` | PASS | Sign cut gives a physical cross block with norm `>=L/4`; determinant envelope, Gaussian smoothing power, Gamma factor and layer-cake log potential are correct. |
| 528--535 pivot/volume definition | PASS | Ordered disjoint-pair convention matches later Cauchy--Binet/random-cut counting. |
| 545--564 `lem:sampling` | PASS | Bordered determinant identity is correct after sorting; extensions are counted at most `(r+1)^2`; singular seeds justify inequality rather than equality. |
| 566--580 `lem:completion` | PASS | `E` is zero-diagonal, `D` vanishes on `S union T`, `R_LL=P_LL`; support of `R-P` is rows `T` or columns `S`, yielding global rank `<=3r` and restricted rank `<=r`. |
| 582--619 `prop:volume` | PASS | Ratio selection is exhaustive, r=0 closes by operator norm, r=1..4 retain the actual nonzero `E`; global rank forces `r+1` large D entries, seed vanishing puts them in `L`, and DD contradicts restricted rank. |
| 621--630 `lem:cut` | PASS | Each ordered disjoint k-minor crosses a fair cut with exact probability `4^-k`. |
| 632--645 `cor:no-pivot` | PASS | `Z_k^{-1/(2k)}<=160`; k=3 gives full half-potential `<200`, k=5 gives density `800e<2400`. |
| 654--674 `lem:kernels` | PASS | Both singular kernels are integrated in valid directions; centered-overlap argument for logarithm is sound. |
| 676--714 `prop:pivot-H` | PASS | Scalar pivot uses surviving Schur spectrum and log potential; definite and indefinite pairs are conditional measure bounds uniform in induced affine terms. |
| 716--724 `prop:nine` | PASS | Pivot branch proves truncated `H<=600`; no-pivot k=3 is already full; outside unit window contributes at most one, giving full `<=601`. |
| 726--749 main proof | PASS | Cases are exhaustive. Scalar pivot leaves at least 16 spectral directions, enough for `prop:nine`; definite pair is direct; indefinite pair leaves at least one unit direction for quarter/log control. |
| 750--790 scaling/accounting/remarks | PASS | `Y=KX`, `tilde Q=(K^2/s)Q` and scalar density scaling produce `K^2/s`. Limitations correctly keep the unrestricted three-eigenvalue theorem and global continuity open. |

No range remains `UNCHECKED` in this B20 mathematical reconstruction.

## Release-status synthesis

A genuinely separate account04/B15 report also records a complete end-to-end mathematical PASS on the same pinned source, including the singular-Schur moving-threshold argument. This B20 reconstruction and account04/B15 are distinct worker reviews. Therefore the owner's numerical condition of **two distinct complete mathematical reviews is now supported by repository evidence** for the baseline 17-eigenvalue proof. I do not overwrite global release/status metadata or call this formal verification or journal peer review; any release label should preserve the exact source pin and the nonfatal projection wording clarification above.

Older reports that called the support bundle missing are stale with respect to current `master`; the files now exist. Older B18's proposed fixed-`delta` Schur rewrite may still be adopted for exposition, but should not be described as repairing a false theorem step.

## Threshold reduction achieved in this run

No same-scope `s_16` density theorem is claimed. I did, however, prove a new exact localization of the only unpaid `s_16` no-pivot branch, saved in the sibling improvement artifact `S16_THREE_BANK_SATURATION.md`.

Briefly: if `s_16(A)>=1` and there is no pivot, then either `V_5>=kappa^5` and the full density is already paid by `<2400`, or the `r=4` interpolation saturates. In the latter case there are three disjoint physical four-coordinate banks `S,T,H`, the sampled crossing `A[S,T]` is invertible, the rank-four carrier on the seed complement has an invertible `H x H` block with

\[
s_4(P_{H,H})>\frac{109}{700},
\]

and both `A[H,T]` and `A[S,H]` are invertible with

\[
|\det A[H,T]|\,|\det A[S,H]|
>
\left(\frac{109}{700}\right)^4 |\det A[S,T]|.
\]

This converts the vague `m=16` saturation into a quantitative, product-preserving **three-bank rank-four collar**. The remaining `17 -> 16` obligation is analytic/geometric: exploit those two additional physical crossings to force a leverage gap/transverse fifth direction or prove a direct three-bank endpoint bound. The bare order-four determinant envelope remains the critical `|t|^{-1}` endpoint, so no unsupported threshold reduction is declared.

## Status

- 17-eigenvalue candidate, pinned source: **PASS in this B20 reconstruction**.
- Two distinct full-review evidence: **present** (account04/B15 plus this B20), but not formal verification or journal review.
- Projection entropy wording: **nonfatal presentation GAP**; replace restricted-index equality by `<=d` or sum over all indices.
- Singular Schur baseline paragraph: **PASS**; earlier GAP diagnosis rejected with proof above.
- Package files: **present on fresh master**.
- Same-scope threshold 16: **OPEN**, with new three-bank saturation reduction proved.
- Full three-eigenvalue conjecture: **OPEN**.
- Global continuity under the 17-eigenvalue theorem: **not claimed**.
- Brain receiver status: `WITHOUT_VERIFIED_BRAIN`.
