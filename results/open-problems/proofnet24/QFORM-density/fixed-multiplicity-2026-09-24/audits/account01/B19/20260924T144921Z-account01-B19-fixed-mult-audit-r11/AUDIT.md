# account01/B19 independent end-to-end audit — r11

Run: `20260924T144921Z-account01-B19-fixed-mult-audit-r11`  
Objective: `QFORM-FIXED-MULTIPLICITY-AUDIT-20260924`  
Baseline commit requested by owner: `7c0d6e60946b19423e6400a12d34b473cf0591e2`  
Pinned source blob actually audited: `183ccd294763214e6a707e8d4749ff9a8cf7006d`  
Pinned source SHA-256 from manifest: `9f3bdec0b88debe9a66076c7b4a5cc894fb14e69b89591a4107e785340f65e69`  
Fresh master observed at start: `30525aa82e000f8673dc62e0cd000ed6c9770da4`; master advanced concurrently during the audit, but a final readback confirmed the manuscript blob was still `183ccd294763214e6a707e8d4749ff9a8cf7006d`.

## Fatal gaps first

**No fatal mathematical gap found in the 17-eigenvalue baseline.** My independent verdict on the mathematical theorem represented by the pinned 790-line source is **PASS**. This is one complete B19 review, not a project-level independent-validation certificate, not journal peer review, and not a proof of the unrestricted three-eigenvalue conjecture.

The finite checker file is present and internally consistent with `checks.json`, but I did **not** independently execute it in this invocation; the repository-recorded checker execution is therefore **UNCHECKED as my own computation**. Novelty/priority is also **UNCHECKED** and is not a proof premise.

## Source/package integrity

- `manuscript.tex`: **PASS**. Read in full, lines 1--790. Current master still returns git blob `183ccd294763214e6a707e8d4749ff9a8cf7006d`, matching the pinned baseline.
- `README.md`: **PASS** for current package inventory. It now accurately lists the support files that were missing in an earlier repository state.
- `AUDIT.md`: **PASS as historical self-audit evidence only**; not counted as independent validation.
- `proof_map.csv`: **PASS**. The listed theorem/lemma source ranges agree with the source.
- `SOURCE_MANIFEST.json`: **PASS** for the source blob/hash/line/byte metadata and support-file inventory.
- `verify.py`: **PASS on code inspection for its stated finite scope**; **UNCHECKED** as an independently executed test suite in this run.
- `checks.json`: **PASS as a recorded output file**, **UNCHECKED** as an independent rerun. It records 534 exact interpolation seeds, 18 exact volume-sampling cases, 240 floating Schur-threshold cases and 30 graph-weight cases.
- `DELIVERY_STATUS.md`: **PASS as delivery/status metadata only**; its worker-count and build reports are not used as proof evidence.

## End-to-end mathematical audit by exact source range

### Lines 1--90: definitions, theorem, architecture — PASS

The singular-value convention, essential-supremum convention and theorem quantifiers are coherent. The theorem allows arbitrary dimension, signature, remaining spectrum, affine terms and independent rough coordinate laws with density cap `K`. The normalization plan `K=s=1` and parameters `eta=1/100`, `kappa=1/80^2` are consistent with the final scaling. The architecture correctly distinguishes the order-three half-potential use from the order-five integrable Fourier use.

A minor presentation improvement would be to state once, globally, that each a.e.-bounded density is replaced by a Borel representative bounded by the same cap everywhere before any pointwise formula is written. The proof already makes this choice where needed and all final statements are law-level/Tonelli statements; this is **not a gap**.

### Lines 91--160: Fourier inversion, power envelope, Riesz half potential — PASS

Plancherel normalization is consistent with `hat f(t)=int exp(itx)f(x)dx`: `int |hat f|^2=2pi int|f|^2`. Gaussian inversion has the factor `1/(2 sqrt(pi v))`. The Riesz derivation via the gamma representation and Gaussian inversion gives the coefficient `1/sqrt(2pi)`. The weighted integral under the `3/4` envelope is exactly `12 sqrt(u)`, producing the displayed `12 sqrt(u/(2pi))`. All Tonelli applications are to nonnegative majorants and require no moments.

### Lines 161--217: singular-value perturbation, Schur count, diagonal dominance — PASS

The rank perturbation formula is valid for nonsymmetric matrices and is used in that generality later.

The singular case of the Schur-count lemma, lines 204--207, is **PASS as written**. If `q=N_A(t)-k`, the invertible perturbations give `N_{S_epsilon}(t-|epsilon|)>=q`, equivalently `s_q(S_epsilon)>=t-|epsilon|`. Since `S_epsilon -> S` and ordered absolute eigenvalues are continuous, `s_q(S)>=t`. No rate comparison is needed. Thus the concurrent objection that the moving threshold creates a gap is **FALSE**; a fixed-delta rewrite is an optional clarification only.

Strict row diagonal dominance is correctly proved without symmetry.

### Lines 218--301: geometric Brascamp--Lieb, product projections, scalar Fourier powers — PASS

The heat-flow computation uses the frame identity `sum c_i u_i u_i^T=I`; the sign of the monotonicity term follows from the contraction `W W^T=I`. The large-time limit and the `t downarrow 0` Fatou step are adequately dominated for compactly supported approximants; monotone truncation extends to arbitrary integrable factors.

The projection-density lemma never asserts independence after rotation. It changes deterministic integration variables and applies the proved rank-one inequality to the original product density. The bound `e^(d/2)` and the scalar consequence `sqrt(e)/|a|` follow from `-b log b <=1-b`.

The scalar Fourier-power estimate has the right parity reduction and constants. The density of `X-X'` is bounded by one by convolution.

### Lines 302--400: decoupling, regularized determinant, crossing volumes — PASS

The two Cauchy--Schwarz/Jensen powers are correct. Duplication is only of an original-coordinate bank, so conditional independence remains valid for arbitrary rough product laws.

For the determinant theorem I rederived the graph weights
`c_j=alpha e_j^T H^{-1}e_j`, `d_i=a^2 m_i^T H^{-1}m_i`, the frame identity, trace identity `sum d_i=sum(1-c_j)`, the Jacobian factors, and the scalar Fourier-power input with `p=2/d_i`. With `alpha=(2 pi e)^2` the entropy factor cancels exactly and fourth roots give exponent `-1/8`. No rank/leverage condition is hidden.

Cauchy--Binet gives the stated `Z_k`, and retaining one determinant coefficient produces exponent `k/4`. The order-five density constant `5e Z_5^{-1/10}` and order-three half-potential constant are correct.

### Lines 401--525: scalar, definite-pair, hyperbolic-pair, quarter-power estimates — PASS

The scalar square profile and interval inverse-image estimate are correct. The conditional square domination is a measure/Tonelli statement and does not claim independence of the square and the Schur remainder.

The definite-pair calculation is a deterministic two-dimensional change of variables; rotation is not used to assert random-coordinate independence.

For the hyperbolic pair I checked the Jacobian `1/(2 sqrt(D))`, the tail monotonicity estimates, the one-dimensional `1/|y|` rearrangement bound, and the use of `Lambda >=2/sqrt(D)`. The exceptional critical level is handled at measure level.

The quarter-power lemma correctly uses a physical diagonal branch or a random-sign physical bipartition. The determinant theorem supplies the `|t|^{-1/4}` bound, Gaussian smoothing supplies the small-ball bound, and layer cake gives `L0=4+4 log16`. The crude gamma bound is more than sufficient.

### Lines 526--645: sampling, nonsymmetric completion, spectral-to-volume, random cut — PASS

The ordered disjoint-minor convention is consistent throughout. The no-pivot entry estimate follows from the two-by-two principal determinant bound.

The volume-sampled interpolation correctly uses the bordered determinant identity. Singular seeds can possess nonsingular extensions, so the proof properly obtains an inequality rather than an equality. Sorting signs disappear after squaring.

For completion, `R-P` is supported in rows `T` or columns `S`, yielding global rank `<=3r`; on `L x L`, `R=P`, so the sharper rank is `<=r`. The auxiliary matrices need not be symmetric. `D` vanishes on `S union T` and `E` has zero diagonal exactly.

In Proposition 6.4, if a volume ratio is small then `||E||<= (r+1)sqrt(kappa)<=1/16`. From `s_{4k-3}(A)>=1` and global rank `3r`, at least `r+1` large diagonal entries of `D` are forced; because `D=0` on the seed they lie in `L`. On the selected `(r+1)`-set, `R` has diagonal modulus at least `371/400` while row off-diagonal mass is strictly below `23/28`, so strict diagonal dominance gives rank `r+1`, contradicting the restricted rank `<=r`. The exact slack is `297/2800>0`.

The fair-cut identity has probability `4^{-k}` for each ordered disjoint pair. The resulting no-pivot constants at nine and seventeen directions are correct.

### Lines 646--725: singular kernels, pivot half potentials, nine-direction half potential — PASS

The kernel `J(d)` decomposition and the logarithmic-kernel rearrangement are sufficient at the displayed constants. The scalar pivot uses the Schur count and quarter-power log potential correctly. Definite and indefinite pair branches correctly preserve arbitrary induced affine terms. The truncated half-potential bound `600` is conservative.

The nine-eigenvalue proposition cleanly separates the pivot case from the no-pivot full half-potential case. Adding the outside region contributes at most one, giving `601`.

### Lines 726--749: main theorem and scaling — PASS

No-pivot `s_17` is paid by order-five crossing volume. A scalar pivot leaves at least sixteen unit-scale Schur eigenvalues, hence the nine-direction half-potential applies. A definite pair is direct. An indefinite pair leaves at least fifteen Schur eigenvalues, so in particular operator norm at least one and the log-potential argument applies. All conditional critical values are averaged through measure domination/Tonelli.

For general `K,s`, `Y=KX` has cap-one coordinate densities, `A/s` has seventeenth singular value at least one, and `Q=(s/K^2) Qtilde`; density scaling therefore gives exactly `K^2/s`.

### Lines 750--790: threshold accounting, limitations, attribution — PASS

The source accurately states what is and is not proved. It does not claim the three-eigenvalue conjecture or global continuity. The classical citations are attribution only because the needed analytic inputs are reproved in the manuscript.

## Baseline verdict table

| Range / item | Verdict | Reason / downstream effect |
|---|---|---|
| 47--57 theorem quantifiers | PASS | arbitrary product laws, signs, affine terms, dimension all preserved |
| 91--160 Fourier/Riesz | PASS | normalizations and Tonelli checked |
| 169--181 nonsymmetric singular values | PASS | supports later nonsymmetric interpolation |
| 183--207 Schur count incl. singular case | PASS | moving-threshold limit is valid; contrary gap report is FALSE |
| 221--301 BL/projection/Fourier powers | PASS | no rotated independence assumption |
| 310--400 decoupling/determinant/volumes | PASS | exponent and constants rederived |
| 404--525 pivot analytic lemmas | PASS | rough-law-safe measure domination |
| 528--645 sampling/completion/volume | PASS | global `3r`, restricted `r`, seed-zero diagonal all checked |
| 654--724 kernels/pivot-H/nine-H | PASS | full vs truncated half potentials distinguished correctly |
| 726--749 main proof | PASS | four branches exhaustive; scaling correct |
| 751--790 limitations | PASS | scope stated honestly |
| support files present/current | PASS | package now complete at read time |
| independent execution of `verify.py` | UNCHECKED | recorded result inspected, not rerun here |
| exhaustive novelty/priority | UNCHECKED | not a proof dependency |

## Guarded integration finding: multiplicity nine

After the baseline audit I independently reconstructed, rather than merely accepted, the current grouped physical-product Fourier argument in the concurrent multiplicity-nine work. The rough-law Gaussian regularization, weighted Holder identity, product-projection Jacobian, entropy cancellation, heavy-row physical promotions and constants all check out. This gives, as a mathematical theorem supported by this B19 review,

` s_9(A)>=s  =>  ||p_(X^TAX+b^TX+c)||_infinity <= (2010+1200 log16) K^2/s < 5338 K^2/s.`

The proof preserves every hypothesis of the baseline theorem. This B19 audit is one independent mathematical review of that replacement argument; owner-level release/independent-validation status still requires reconciliation with a genuinely separate complete review and must not be self-awarded here.

Multiplicity eight is not established by this audit. A separate improvement file from this run gives a new exact reduction for the current two-anchor endpoint.