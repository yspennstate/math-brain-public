# account01/B13 r3 — complete fixed-multiplicity audit

Run: `20260924T143122Z-account01-B13-fixedmult-audit-r3`  
Objective: `QFORM-FIXED-MULTIPLICITY-AUDIT-20260924`  
Execution status: `WITHOUT_VERIFIED_BRAIN`

## Source pin and scope

- Owner-pinned baseline source commit: `7c0d6e60946b19423e6400a12d34b473cf0591e2`.
- Canonical source: `proofnet24/QFORM-density/fixed-multiplicity-2026-09-24/manuscript.tex`.
- Git blob read in full: `183ccd294763214e6a707e8d4749ff9a8cf7006d`.
- Recorded source SHA-256: `9f3bdec0b88debe9a66076c7b4a5cc894fb14e69b89591a4107e785340f65e69`.
- Source length: 790 lines / 47,883 bytes as recorded by the source manifest.
- Fresh `master` was resolved repeatedly during this run; immediately before this immutable report it was `4335ca25ed47bbaf02045553f59b8d52d9322228`. The manuscript blob remained the pinned baseline blob. Concurrent peer audit/improvement commits were not treated as modifications of the baseline source.

I read fresh `math-research-brain/main/AGENTS.md` and `scheduled_tasks/CURRENT_OBJECTIVE.md`, then read the complete package required by the objective: `README.md`, `DELIVERY_STATUS.md` (required by README), `AUDIT.md`, `proof_map.csv`, `SOURCE_MANIFEST.json`, `verify.py`, `checks.json`, and all 790 lines of `manuscript.tex`.

The theorem audited is exactly the candidate arbitrary-law statement

\[
s_{17}(A)\ge s>0,\qquad 0\le f_i\le K\quad\Longrightarrow\quad
\|p_{X^TAX+b^TX+c}\|_\infty\le 10^4 K^2/s,
\]

with arbitrary dimension, signature, remaining spectrum and affine terms. This audit does **not** claim the unrestricted three-eigenvalue conjecture.

## Verdict

**PASS for the mathematical 17-eigenvalue theorem in this independent B13 reconstruction.** I found no theorem-breaking `FALSE` statement and no fatal mathematical `GAP` in the pinned manuscript. No mathematical source range remains `UNCHECKED` in my line-by-line pass.

There is one nonfatal presentation repair and one reproducibility item I mark separately:

1. **GAP-PRESENTATION, theorem unaffected — density representatives.** The theorem assumes `f_i<=K` almost everywhere, while several inverse-branch formulas later write pointwise values of chosen density versions. One global sentence should say: choose Borel versions and redefine them on null sets so that `0<=f_i<=K` everywhere. This changes no law. The projection lemma already makes this choice locally. The hyperbolic-tail argument is also safe a.e. because its chosen original coordinate is monotone on each tail, but the global convention is cleaner.
2. **UNCHECKED diagnostic execution only.** I read `verify.py` completely and checked that its assertions match the manuscript invariants. I read `checks.json`, which records `PASS`, 534 exact interpolation seeds, 18 exact volume-comparison cases, 9 strict sampling cases, 240 floating Schur cases, 30 graph-weight cases and exact diagonal-dominance slack `297/2800`. I did not independently re-run the repository script from raw private bytes in this invocation and therefore do not promote those recorded counts to an independent computational rerun. Likewise, I pin the exact git blob and the manifest's SHA-256 but did not independently recompute the SHA-256 from a separately materialized raw file.

These two items do not alter the mathematical verdict.

## B13 starting lens — definite pair

Source: `manuscript.tex` lines 401–434, especially `lem:definite`.

**PASS.** After conditioning on all other original coordinates, the selected physical pair still has joint density at most one. A deterministic translation completes the square; a deterministic orthogonal change of integration coordinates diagonalizes a definite `2x2` matrix with eigenvalues `mu_1,mu_2>0`. The parametrization

\[
w=w_0+\sqrt{\delta/\mu_1}\cos\theta\,e_1+
\sqrt{\delta/\mu_2}\sin\theta\,e_2
\]

has absolute Jacobian

\[
\left|\det\frac{\partial w}{\partial(\delta,\theta)}\right|
=\frac1{2\sqrt{\mu_1\mu_2}}=\frac1{2\sqrt{|\det B|}}.
\]

Integrating a joint density bounded by `M` over `0<=theta<2pi` gives

\[
\|p_q\|_\infty\le \pi M/\sqrt{|\det B|}.
\]

The rotation is only a deterministic two-dimensional change of variables. No independence of rotated random coordinates is asserted or needed.

## B13 starting lens — indefinite pair, both level-set signs

Source: lines 437–482, `lem:hyperbola`.

**PASS.** Write the two eigenvalues as `mu_+>0>-nu`, `D=mu_+ nu`, `Lambda=mu_+^{-1}+nu^{-1}`. For `delta=z-v>0`, the two connected components of the level set are

\[
w_\epsilon(t)=\epsilon\sqrt{\delta/\mu_+}\cosh t\,e_+
+\sqrt{\delta/\nu}\sinh t\,e_-,\qquad \epsilon=\pm1.
\]

A direct determinant calculation gives

\[
\left|\det\frac{\partial w_\epsilon}{\partial(\delta,t)}\right|
=\frac1{2\sqrt D}.
\]

Writing one branch as `u e^t+w e^{-t}` gives

\[
|u|=|w|=\rho_0=\frac12\sqrt{\delta\Lambda}.
\]

Choose an **original physical coordinate** `i` with `|u_i|>=rho_0/sqrt(2)`. Since `|w_i|<=rho_0`, for

\[
T_1=\frac34\log2
\]

and `t>=T_1` one has

\[
|w_i|e^{-t}\le |u_i|e^t/2,
\]

hence the coordinate is monotone, stays on one sign, and satisfies

\[
\frac12|u_i|e^t\le |w_{\epsilon,i}(t)|\le\frac32|u_i|e^t,
\qquad |w'_{\epsilon,i}(t)|\ge |w_{\epsilon,i}(t)|/3.
\]

With

\[
T=\max\{T_1,\log(2/|u_i|)\},
\]

the entry magnitude at the tail is at least one. The proof then uses the two rough-law hypotheses exactly where required:

- the pointwise cap gives `f_1 f_2<=f_i` along the tail;
- the unit mass of `f_i` on the relevant half-line lets the decreasing weight `1/|y|` be maximized by filling the length-one interval nearest to the threshold.

Thus the positive tail contributes at most `3 log2`. The negative tail is identical after choosing an original coordinate where `w` is large. The two cutoff lengths obey

\[
T,T'\le\frac34\log2+\frac12\log_+\frac{32}{\delta\Lambda},
\]

so each branch integral is at most

\[
\frac{15}{2}\log2+\log_+\frac{32}{\delta\Lambda}
<6+\log_+\frac{32}{\delta\Lambda}.
\]

Summing the two branches cancels the `1/2` in the Jacobian. Since `Lambda>=2/sqrt(D)`, the stated envelope follows:

\[
p_q(v+\delta)\le D^{-1/2}
\left(6+\log_+\frac{16\sqrt D}{\delta}\right).
\]

For `delta<0`, applying the identical calculation to `-B` swaps the positive and negative eigendirections without changing `D` or any original-coordinate density hypothesis. The critical level `delta=0` is one output point and is handled only through the later nonnegative test-function/Tonelli formulation. Thus both signs and the exceptional critical value are covered.

## B13 starting lens — logarithmic critical-value averaging

Source: lines 646–714 and 726–749.

**PASS.** After conditioning on the complement of an indefinite physical pair and completing the square, its critical value is a quadratic polynomial `R` in the untouched original coordinates. The Schur complement loses at most two threshold-scale eigenvalues, so in the main 17-direction theorem `R` has at least one unit-scale quadratic direction. `lem:quarter` therefore gives uniformly in `a`

\[
\mathbb E\log_+\frac1{|R-a|}\le L_0=4+4\log16.
\]

The elementary inequality

\[
\log_+\frac{16\sqrt D}{|z-R|}
\le \log_+(16\sqrt D)+\log_+\frac1{|z-R|}
\]

then pays the random critical value. All averaging is performed with nonnegative test functions/Tonelli, so no common pointwise version of a rough conditional density is selected across exceptional slices.

The truncated-half-potential branch uses

\[
\int_{-1}^1 |x|^{-1/2}\log_+\frac1{|x-a|}\,dx\le8,
\]

whose layer-cake proof is valid because the two superlevel sets are intervals and their overlap is maximized when centered together.

## Complete forward source audit

| Source range | Object | Status | Reasoning / downstream impact |
|---|---|---|---|
| 1–46 | title, definitions, abstract, proof architecture | PASS | Quantifiers match the later proof. The distinction between singular values and signed eigenvalues is explicit. No moment/support/log-concavity/rotated-independence assumption is inserted. |
| 47–61 | `thm:main`, `cor:33` | PASS | Exact claim is `s_17>=s`, density `<=10^4 K^2/s`; `s_17>=s_33` makes the 33 statement a genuine corollary. |
| 62–87 | normalized parameters and branch plan | PASS | `eta=1/100`, `kappa=1/80^2`; the pivot/no-pivot split is exhaustive. |
| 88–120 | Fourier conventions, Gaussian regularization, inversion | PASS | Constants are consistent with `hat f(t)=int e^{itx}f(x)dx`. Gaussian regularization avoids assuming an output density before inversion. |
| 122–130 | power envelope | PASS | `int min(1,(a/|t|)^p)=2ap/(p-1)` and the `1/(2pi)` inversion factor give the displayed bound. |
| 132–160 | negative half moments | PASS | Gamma/Tonelli/Gaussian calculation produces coefficient `1/sqrt(2pi)`; the weighted `3/4` envelope integral is `12 sqrt(u)`. |
| 161–181 | singular-value perturbation and rank | PASS | Approximation-number proof applies to nonsymmetric matrices, exactly as later needed for `A-E=D+R`. |
| 183–207 | Schur spectral count | PASS | For invertible ambient `A`, `S^{-1}` is a principal compression of `A^{-1}`; signwise interlacing for `A^{-1}` and `-A^{-1}` yields the absolute-value count. The singular ambient case is obtained with `A+eps I`, threshold `t-|eps|`, and continuity of the ordered eigenvalue moduli. Invertibility of the pivot is essential. |
| 209–217 | strict diagonal dominance | PASS | Standard nonsymmetric row argument. |
| 218–255 | geometric rank-one Brascamp–Lieb | PASS | Heat-flow derivative has the correct sign from the exact frame contraction; compact-support tails justify integration by parts; large-time Gaussian limit and small-time Fatou step close the rough-input proof. |
| 258–282 | product projections | PASS | The orthogonal complement is used only in deterministic integration. The BL weights are `b_i=1-|U^T e_i|^2`; `-b log b<=1-b` yields `e^{d/2}`. No projected-coordinate independence is claimed. |
| 284–301 | scalar Fourier powers | PASS | Plancherel gives integrability; `m=floor(p/2)>=p/4`; inversion of the iid-difference sum at zero plus the scalar projection bound gives `2pi sqrt(2e)/sqrt(p)`. |
| 302–324 | cross-block decoupling | PASS | Cauchy–Schwarz is applied before the independent copy; pure phases are discarded only after modulus. Difference coordinates remain independent cap-one. Exponents two and four are correct. |
| 326–373 | regularized crossing determinant | PASS | The regularized vectors form an exact Parseval frame. `alpha=(2pi e)^2` cancels the entropy factor, and the fourth root produces determinant exponent `-1/8` and coefficient `t^2/(pi^2 e^2)`. |
| 374–400 | crossing volumes and volume envelopes | PASS | Cauchy–Binet expansion is exact. Order five yields characteristic exponent `5/4>1` and a density; order three yields exponent `3/4`, used only after the Riesz weight. |
| 401–422 | scalar square and conditional profile | PASS | Inverse branches and interval-preimage constant are correct. The displayed profile is a conditional measure domination statement, not an independence assertion. |
| 423–434 | definite pair | PASS | Exact Jacobian checked above. Deterministic rotation only. |
| 437–482 | hyperbolic pair | PASS with presentation repair | Both signs, original-coordinate tails, cap/mass use, logarithmic envelope and critical level checked above. Add the global pointwise density-version convention for cleanliness. |
| 485–525 | quarter-power concentration and logarithmic potential | PASS | Large diagonal uses scalar square. Otherwise random signs expose a physical cross block of norm at least `L/4`; determinant bound gives `|t|^-1/4`. Gaussian smoothing and layer cake give the stated constants and no atoms. |
| 528–543 | pivot volume and no-pivot entry bound | PASS | Absence of scalar and principal-pair pivots gives the stated entry bounds. |
| 545–564 | volume-sampled interpolation | PASS | Bordered determinant identity is exact. Ordered disjoint extensions are overcounted by at most `(r+1)^2`; singular seeds justify inequality rather than equality. `P` may be nonsymmetric and interpolates rows `S` and columns `T`. |
| 566–580 | diagonal plus interpolation | PASS | `E` has zero diagonal, `D` vanishes on the seed, `R_LL=P_LL` and has rank at most `r`; globally `R-P` is supported on rows `T` or columns `S`, giving `rank R<=3r`. |
| 582–619 | no-pivot spectral-to-volume proposition | PASS | Telescoping/first-zero choice of a bad ratio is exhaustive. For `r>=1`, perturbation plus global `3r` rank forces `r+1` large entries of `D` in `L`; their block has diagonal lower bound `371/400` and off-diagonal row sum below `23/28`, with exact positive slack `297/2800`, contradicting restricted rank `<=r`. |
| 621–645 | random cut and no-pivot analytic consequences | PASS | An ordered disjoint `k`-minor crosses a fair cut with probability exactly `4^-k`; hence `Z_k^-1/(2k)<=160`. Constants `<200` and `800e<2400` follow. |
| 646–674 | two singular kernel integrals | PASS | Direct splitting / layer cake is valid; constants are deliberately coarse but correct. |
| 676–714 | pivot truncated-half-potential proposition | PASS | Scalar branch combines Schur survivor + logarithmic critical-value control; definite branch is direct; indefinite branch uses the checked hyperbolic envelope and logarithmic kernel. All induced affine terms are allowed. |
| 716–724 | nine-direction half-potential | PASS | Pivot branch gives truncated `<=600`; no-pivot order-three gives full `<200`; outside the unit window the half-kernel is at most one, so the full potential is `<=601`. |
| 726–749 | theorem proof and `K,s` scaling | PASS | Four cases exhaust the normalized proof. Scalar Schur leaves 16 directions, definite pair is direct, indefinite pair leaves 15 and needs only one. For general scale, `Y=KX`, matrix `A/s`, and output relation `Q=(s/K^2)Qtilde` give exactly `K^2/s`. |
| 750–790 | accounting, limitations, acknowledgments, references | PASS | Manuscript correctly does not claim `s_3` sufficiency or global continuity. The order-three and order-five analytic conclusions are not conflated. |

## Reverse dependency review (separate end-to-end pass)

I then audited the theorem backwards from each terminal branch rather than merely rereading the forward table.

1. **No pivot:** main density -> order-five volume envelope -> fair cut -> `V_5` -> sampled interpolation/completion -> nonsymmetric rank perturbation + restricted diagonal-dominance contradiction. All hypotheses close.
2. **Scalar pivot:** square profile -> full half-potential of Schur remainder -> pivot/no-pivot split for that remainder -> Schur count and quarter/log potential or order-three crossing. No independent-remainder assumption appears.
3. **Definite pair:** original-coordinate conditioning -> joint density cap -> deterministic 2D Jacobian. No rotated independence.
4. **Indefinite pair:** original-coordinate conditioning -> two-branch hyperbolic coarea -> tail estimate using original marginal cap and mass -> Schur-survivor logarithmic critical-value averaging -> Tonelli. Both output signs are covered.
5. **Crossing determinant:** Fourier envelope -> regularized graph BL -> scalar Fourier powers -> product projection -> geometric BL. Product structure is used only before deterministic integrations.
6. **Scaling:** cap normalization and output rescaling produce `K^2/s` with no change to signature or affine terms.

This reverse pass found no new gap. It is a second pass by the same worker, not a second independent peer review.

## Package audit

- `README.md`: PASS. It accurately identifies the canonical source and support package and requires `DELIVERY_STATUS.md`.
- `DELIVERY_STATUS.md`: PASS as current repository status metadata; it correctly distinguishes the immutable source from later audits/improvements.
- `SOURCE_MANIFEST.json`: PASS as metadata against the exact git blob and source size/line information read here. Independent raw-byte SHA-256 recomputation: UNCHECKED.
- `AUDIT.md`: PASS as historical self-audit, not independent proof evidence.
- `proof_map.csv`: PASS; labels and line ranges match the source read in full.
- `verify.py`: PASS source audit. Its exact checks correspond to the algebraic identities in the manuscript and its floating tests are diagnostics, not proof.
- `checks.json`: PASS as the recorded output of the repository checker; independent rerun in this invocation: UNCHECKED.

## Threshold accounting discovered after the independent baseline audit

Only after finishing the baseline reconstruction, I inspected completed threshold-improvement artifacts now present on `master`. The current repository contains a complete arbitrary-law **nine-eigenvalue replacement proof** using a grouped product-Fourier compiler and marginal-free order-three crossing receiver, together with multiple genuinely separate complete reconstructions. I independently reconstructed that improvement in the sibling improvement artifact for this run.

My result there is:

\[
\boxed{s_9(A)\ge s\quad\Longrightarrow\quad
\|p_Q\|_\infty\le(2010+1200\log16)K^2/s<5338K^2/s.}
\]

I do not lower the complete theorem below nine in this run. Current source-matched work reduces seven/eight directions to an overlap-one / multi-bank product-preserving receiver, but that receiver is not proved. The unrestricted three-eigenvalue conjecture remains open.

## Final status

- Pinned 17-eigenvalue manuscript: **PASS in this independent B13 audit**.
- Fatal mathematical defects found: **none**.
- Mathematical source ranges left `UNCHECKED`: **none**.
- Presentation repair: global pointwise density-version convention.
- Computational rerun / independent SHA-256 rehash: **UNCHECKED**, explicitly not used as proof.
- Lowest complete fixed multiplicity independently reconstructed in this run: **9**.
- Threshold 8/7: **OPEN** in this run.
- Full threshold 3 conjecture: **OPEN**.
- Global continuity: **not claimed**.

Model: GPT-5.6 Sol. Configured reasoning effort/provider thinking counters: `UNKNOWN / null / not exposed`.
