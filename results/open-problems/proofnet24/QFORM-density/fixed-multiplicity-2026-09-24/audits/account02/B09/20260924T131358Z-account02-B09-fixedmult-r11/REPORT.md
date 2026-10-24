# account02/B09 — independent fixed-multiplicity audit

Run: `20260924T131358Z-account02-B09-fixedmult-r11`  
Objective: `QFORM-FIXED-MULTIPLICITY-AUDIT-20260924`  
B09 lens: spectral rank perturbation and diagonal-dominance contradiction; account02 counterexample emphasis.

## Source pin and verdict

Pinned baseline source commit: `7c0d6e60946b19423e6400a12d34b473cf0591e2`  
Pinned manuscript SHA-256 from `SOURCE_MANIFEST.json`: `9f3bdec0b88debe9a66076c7b4a5cc894fb14e69b89591a4107e785340f65e69`  
Manuscript git blob independently observed on fresh master: `183ccd294763214e6a707e8d4749ff9a8cf7006d`  
Fresh package head during this audit: `3e27a438cd8beb580ca1951cb5fd264ad0241486`; the manuscript blob there is still exactly `183ccd294763214e6a707e8d4749ff9a8cf7006d`.

**Baseline mathematical verdict: PASS.** I read all 790 source lines and the full package (`README.md`, `SOURCE_MANIFEST.json`, `AUDIT.md`, `proof_map.csv`, `verify.py`, `checks.json`) and independently reconstructed the proof chain. I found no fatal mathematical gap in the candidate

\[
s_{17}(A)\ge s>0\Longrightarrow
\|p_{X^TAX+b^TX+c}\|_\infty\le 10^4K^2/s
\]

for arbitrary real symmetric `A`, arbitrary affine terms, and arbitrary independent real coordinate densities bounded by `K`. This is an independent review, not formal verification or journal peer review. The unrestricted three-eigenvalue conjecture is not proved here.

## Complete source ledger

| Source lines / item | Status | Independent check | Impact / next obligation |
|---|---|---|---|
| 1–83: definitions, theorem/corollary, normalization, architecture | PASS | Singular values are used consistently as eigenvalue moduli for symmetric `A`; theorem quantifiers retain arbitrary dimension/signature/remaining spectrum, affine terms, and rough product laws. The `K,s` normalization later gives exactly `K^2/s`. | Target is coherent. |
| 84–120: Fourier convention, Plancherel/inversion/Gaussian identity | PASS | Constants agree with the convention `fhat(t)=∫e^{itx}f(x)dx`; mollification plus weak convergence identifies the law when `phi∈L1`. | Later inversion constants valid. |
| 121–160: power envelope and negative-half-moment/Riesz estimate | PASS | Envelope integral is `2ap/(p-1)`. The gamma/Gaussian calculation gives the factor `(2π)^(-1/2)` and the weighted `3/4` envelope integral is `12 sqrt(u)`. | Full/truncated half-potential uses are normalized. |
| 161–181: norms and `lem:rank` | PASS | Approximation numbers prove both `|s_j(T)-s_j(U)|≤||T-U||` and `s_{j+q}(D+R)≤s_j(D)` for nonsymmetric matrices. | Legitimately applies to `A-E`, `D+R`, although `E,R` need not be symmetric. |
| 183–207: principal Schur spectral count | PASS | In the invertible case `S^{-1}` is the complementary principal compression of `A^{-1}`; positive and negative interlacing separately give the absolute-eigenvalue count. The `A+εI` limiting argument preserves the `≥t` conclusion. | Pivot Schur counts are sound, including singular `A`. |
| 209–217: strict diagonal dominance | PASS | Maximum-coordinate proof requires no symmetry. | Applies to nonsymmetric `R[H,H]`. |
| 221–255: geometric rank-one Brascamp–Lieb | PASS | Frame identity cancels the Hessian terms in heat flow; the column operator is a contraction, yielding monotonicity. Compact-support heat tails justify differentiation; large-time Gaussian limit and monotone approximation are valid. | Self-contained analytic input closes. |
| 258–282: product projection density | PASS | Orthogonal completion plus geometric BL gives the cap. For dropped `b_i=0` factors, extending `-b log b` continuously by zero and then bounding by `1-b` gives the stated `e^{d/2}` constant. | No rotated-coordinate independence assumption. |
| 284–301: scalar Fourier powers | PASS | `m=floor(p/2)` and `|fhat|≤1` reduce to an even power. The even power is the characteristic function of a sum of independent differences and is integrable by Plancherel; product-projection density at zero gives the constant. | Correct input to graph BL. |
| 310–324: decoupling | PASS | Copy only the `J` bank after Cauchy–Schwarz in `X_I`; original-coordinate integration produces the scalar Fourier product. Difference coordinates are independent and cap one. | No hidden conditional cap. |
| 326–373: regularized crossing determinant | PASS | `H=αI+a^2M^TM` produces an exact rank-one frame. Scale factors in geometric BL are correct; `α=(2πe)^2` cancels the entropy term; fourth roots give determinant exponent `-1/8`. | Main cross-block Fourier estimate valid. |
| 375–400: crossing volumes and envelopes | PASS | Cauchy–Binet expansion is exact. Retaining order `k` gives exponent `k/4`; `k=5` is `L1`, `k=3` is used only after the Riesz weight. | No order-3 density shortcut is made. |
| 404–434: square profile and definite pair | PASS | Inverse branches and polar Jacobian are correct. Conditional statements are measure dominations, not independence claims. | Pivot endpoints valid. |
| 437–482: hyperbolic pair | PASS | Hyperbolic coordinates have Jacobian `1/(2sqrt D)`; original-coordinate tail monotonicity plus mass one yields the log envelope; the critical level is handled in test-function/Tonelli form. | Indefinite pair endpoint valid for rough laws. |
| 485–525: quarter-power concentration/log potential | PASS | If no large diagonal exists, the sign cut gives a physical cross block of norm at least `L/4`; determinant Fourier plus Gaussian smoothing yields the `rho^(1/4)` estimate. Layer cake gives `4+4 log16`. | One surviving eigenvalue is enough for the later logarithmic average. |
| 528–544: pivot volume and no-pivot entry bounds | PASS | `|a_ij|^2≤eta^2+eta<2eta`, hence `|a_ij|<1/7`; principal determinant definition is used with the correct strict inequalities. | Entrywise bounds used in diagonal dominance are justified. |
| 545–564: volume-sampled interpolation | PASS | Bordered determinant identity is exact; sorting signs disappear after squaring. Singular seeds can have nonsingular extensions, so the aggregate is correctly an inequality. Row-`S`/column-`T` interpolation is exact. | Sampling step valid. |
| 566–580: completion/rank/support | PASS | With the stated `D,E,R`, `R[L,L]=P[L,L]`; `R-P` is supported only in rows `T` or columns `S`, giving global rank `≤3r`, while the restricted block has rank `≤r`; `D` vanishes on the seed and `diag E=0`. | Sensitive nonsymmetric support chain is correct. |
| 582–619: no-pivot spectral-to-volume proposition | PASS | Rebuilt in detail below. The singular-value perturbation, global `3r` loss, `D` seed-zero property, and restricted `r` contradiction all line up. Exact diagonal-dominance slack is `297/2800>0`. | This is the algebraic source of `4k-3`. |
| 621–645: random cut and no-pivot consequences | PASS | Every ordered disjoint `k`-minor survives with probability `4^{-k}`. `Z_k^{-1/(2k)}≤160`; constants `12sqrt(80e)<200`, `800e<2400` are correct. | Gives the baseline no-pivot analytic branches. |
| 654–674: singular kernels | PASS | Near/far split in `J(d)` and interval-overlap argument for the translated log kernel give the displayed bounds. | Pivot half-potential integration valid. |
| 676–714: pivot truncated half potential | PASS | Scalar pivot uses the exact profile and one surviving Schur direction; definite and indefinite pair branches are uniform in conditioning variables. Full and truncated potentials are not conflated. | Bound `H(Q)≤600` valid. |
| 716–724: nine-eigenvalue full half potential | PASS | Pivot branch uses the preceding proposition; no-pivot branch uses the proved order-three Riesz bound; outside distance one contributes at most one. | Full half potential `≤601` valid. |
| 726–772: main theorem and scaling | PASS | No-pivot `s17` branch is `<2400`; scalar pivot leaves at least 16 Schur directions, so the nine-direction half-potential theorem applies and gives `6010`; definite and indefinite pairs are smaller. `Y=KX` yields exactly `Q=(s/K^2)Qtilde`. | Candidate 17 theorem closes. |
| 773–790: threshold accounting, limitations, attribution-only bibliography | PASS for mathematical statements; UNCHECKED for priority/attribution completeness | The manuscript correctly says the proof does not settle multiplicity three or optimality and does not claim global continuity. The two citations are not used as black-box proof steps. | No theorem impact from unreviewed bibliographic priority. |

No mathematical source line remains UNCHECKED in this review; only bibliographic priority/completeness is outside the mathematical proof audit.

## B09 reconstruction of the spectral/rank contradiction

Let a bad sampled ratio occur at order `1≤r≤k-1≤4`. The completion gives

\[
A=D+R+E,\quad \operatorname{rank}R\le3r,\quad
\operatorname{rank}R_{L,L}\le r,\quad
\epsilon:=\|E\|_F\le(r+1)/80\le1/16.
\]

Put `m=4k-3`. Since `s_m(A)≥1`, singular-value perturbation gives

\[
s_m(D+R)=s_m(A-E)\ge1-\epsilon.
\]

The rank-`3r` shift then gives

\[
s_{m-3r}(D)\ge1-\epsilon.
\]

Because `r≤k-1`,

\[
m-3r=4k-3-3r\ge r+1.
\]

Thus `D` has at least `r+1` entries of modulus at least `1-epsilon`. Because `D=0` on `S∪T`, all lie in `L`. For an `(r+1)`-set `H` of such coordinates,

\[
|R_{ii}|\ge1-1/16-1/100=371/400,
\]

and, for `i≠j`,

\[
|R_{ij}|\le |A_{ij}|+|E_{ij}|<1/7+1/16=23/112.
\]

Each row has only `r≤4` off-diagonal entries, so

\[
\sum_{j\ne i}|R_{ij}|<4(23/112)=23/28.
\]

The exact slack is

\[
\frac{371}{400}-\frac{23}{28}=\boxed{\frac{297}{2800}}>0.
\]

Therefore `R[H,H]` is invertible of rank `r+1`, contradicting `rank R[L,L]≤r`. Every inequality uses the correct strict/non-strict direction. Symmetry is used only for the original `A` and the no-pivot entry estimate, not for `D+R` or `R[H,H]`.

### Why the `+1` is real for this argument

At the terminal baseline chamber `k=5,r=4`, `m=17` gives `m-3r=5=r+1`. With only `m=16`, rank subtraction guarantees only four large diagonal entries, compatible with restricted rank four. Thus the displayed contradiction cannot simply replace 17 by 16.

A concrete exact family also shows both completion rank constants are simultaneously sharp. With

\[
C=\begin{pmatrix}0&1&1\\1&0&1\\1&1&1\end{pmatrix},\qquad
A_r=10^{-3}(I_r\otimes C),
\]

choose, in each 3-coordinate block, the first coordinate for `S`, the second for `T`, and the third for `L`. Then the interpolation has `F=E=D=0`, so `R=A_r`, while

\[
\operatorname{rank}R=3r,\qquad \operatorname{rank}R[L,L]=r.
\]

All physical diagonal entries are below `eta=10^{-2}` and every principal two-coordinate determinant is below `eta`, so this lies in the no-pivot regime. Hence neither `3r→2r` nor `r→r-1` follows from the completion/no-pivot hypotheses alone. This is a counterexample to those tempting proof strengthenings, not to the density theorem.

## Independent finite stress diagnostics

These computations are diagnostics only, not proof certificates.

- `19,142` random nonsymmetric low-rank perturbation comparisons of `s_{j+q}(D+R)≤s_j(D)`: **0 violations**.
- `38,500` random singular-value Lipschitz comparisons `|s_j(T)-s_j(U)|≤||T-U||`: **0 violations**.
- `2,504` exact SymPy completion instances from independent random symmetric integer matrices in dimensions 4–8 and seed orders 1–3: **0 violations** of global rank `≤3r`, restricted rank `≤r`, `R[L,L]=P[L,L]`, seed-zero `D`, or zero-diagonal `E`. The global/restricted rank bounds were simultaneously attained in `1,556` of those instances.
- Exact symbolic check of the one-block sharpness family above gives `rank R=3`, `rank R[L,L]=1`, `F=E=D=0`, and `det C=1`; direct sums give every `r=1,2,3,4` saturation.

## Package audit

| Package item | Status | Reason / limitation |
|---|---|---|
| `README.md` | PASS | Current package description matches the 17-candidate theorem and correctly distinguishes self-audit from independent validation. |
| `SOURCE_MANIFEST.json` | PASS for metadata consistency | It pins baseline commit, blob, SHA-256, sizes, support-file hashes and explicitly says the GitHub root does not store the compiled PDF. I independently observed the git blob but did not independently recompute the 47,883-byte source SHA-256 from connector bytes. |
| `AUDIT.md` | PASS as historical self-audit; historical test-count reproduction UNCHECKED | Its proof summary is consistent with the manuscript. It explicitly distinguishes historical finite counts from the new reproducibility suite. |
| `proof_map.csv` | PASS | Statement/proof ranges agree with the source read and were used for this ledger. |
| `verify.py` | PASS static audit | The code checks source pin, exact diagonal slack, interpolation/support/rank identities, volume-sampling inequality, numerical Schur count and graph weights. It makes no formal-verification claim. |
| `checks.json` | PASS for consistency with the current checker; independent exact rerun UNCHECKED | It records PASS with 534 interpolation seeds, 18 volume cases, 9 strict cases, 240 Schur threshold cases and 30 graph cases. My independent diagnostics above use a different generator and therefore do not purport to reproduce those counts. |

## Baseline conclusion and next obligation

The pinned 17-eigenvalue manuscript is mathematically PASS in this independent audit. Its spectral/rank step is not the place to lower the theorem by merely retuning constants or replacing the two rank bounds. A lower threshold needs a different analytic endpoint or a genuinely new structural use of the terminal seed. A separate improvement artifact from this run reviews the complete nine-eigenvalue replacement now present in the repository and isolates the exact eight-direction survivor.