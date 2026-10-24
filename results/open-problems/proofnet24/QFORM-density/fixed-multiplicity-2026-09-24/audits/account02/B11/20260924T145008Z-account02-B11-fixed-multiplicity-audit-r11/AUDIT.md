# account02/B11 r11 — full fixed-multiplicity audit and Schur sharpness

Objective: `QFORM-FIXED-MULTIPLICITY-AUDIT-20260924`  
Run: `20260924T145008Z-account02-B11-fixed-multiplicity-audit-r11`  
Role/lens: full end-to-end independent review, with account02 counterexample emphasis and B11 Schur-complement spectral counts (singular and near-singular cases).

## 0. Pins, scope, and verdict

Fresh brain control was resolved before work and refreshed before publication. The current objective remained `QFORM-FIXED-MULTIPLICITY-AUDIT-20260924`; no later stop or incompatible correction was found.

Canonical baseline reviewed:

- repository: `yspennstate/math-open-problems`, branch `master`;
- package: `proofnet24/QFORM-density/fixed-multiplicity-2026-09-24/`;
- initial manuscript source commit: `7c0d6e60946b19423e6400a12d34b473cf0591e2`;
- manuscript git blob: `183ccd294763214e6a707e8d4749ff9a8cf7006d`;
- manifest-recorded SHA-256: `9f3bdec0b88debe9a66076c7b4a5cc894fb14e69b89591a4107e785340f65e69`;
- source size: 47,883 bytes, 790 lines.

At the invocation read, `master` was `acb9d0fff6440b29746cb89d6876e3d570631d67`; at the prepublication refresh it was `5327ab7b161c004851cf59f4c4295822e9ab39db`. In both repository states the canonical manuscript blob is the pinned blob above. I read `README.md`, `DELIVERY_STATUS.md`, `SOURCE_MANIFEST.json`, all 790 lines of `manuscript.tex`, `AUDIT.md`, `proof_map.csv`, `verify.py`, and `checks.json`.

**Baseline mathematical verdict: PASS in this independent review.** I found no fatal defect in the stated theorem

\[
s_{17}(A)\ge s>0\quad\Longrightarrow\quad
\|p_{X^TAX+b^TX+c}\|_{\infty,\mathrm{ess}}
\le 10^4 K^2/s
\]

for arbitrary independent real coordinate densities bounded by `K`, arbitrary real symmetric `A`, arbitrary affine `b,c`, all dimensions/signatures/remaining spectrum, and rough laws.

**Current fixed-multiplicity improvement: PASS at multiplicity 9 after reconstruction.** The complete grouped-product Fourier replacement already present in the package gives

\[
\boxed{s_9(A)\ge s>0\Longrightarrow
\|p_Q\|_\infty\le(2010+1200\log16)K^2/s<5338K^2/s.}
\]

I rechecked its compiler, promotion, Schur, and assembly dependencies below. I do not claim multiplicity eight: current `s_8` work supplies strong terminal structure and overlap-one third-volume currency but not a complete dependence-safe density receiver. The unrestricted three-eigenvalue conjecture remains OPEN.

The manifest's SHA-256 is source-pinned and `verify.py` itself guards that value. I did not perform a separate raw-byte SHA-256 computation outside the connector in this run; that narrow reproducibility item is therefore **UNCHECKED independently**, while the git blob identity and source contents were read directly.

## 1. Package-level audit

| Item | Status | Reasoning / impact / next obligation |
|---|---|---|
| `README.md` | PASS | Correctly states the 17-eigenvalue candidate, non-optimality, required package files, and that the unrestricted three-eigenvalue problem is not solved. |
| `DELIVERY_STATUS.md` | PASS as delivery metadata | Correctly distinguishes the committed 790-line source from the conversation-delivered PDF and finite checks from mathematical proof. PDF binary/render is not independently checked here because it is not in this GitHub root. |
| `SOURCE_MANIFEST.json` | PASS for repository metadata; raw SHA recomputation UNCHECKED | Blob/bytes/lines agree with the repository file. SHA-256 is pinned by the manifest/checker but not separately recomputed from raw bytes in this run. |
| `AUDIT.md` | PASS as historical self-report; old finite counts UNCHECKED | It explicitly labels itself a self-audit. Its older counts (504/10/192/800/1040/160) are not reproduced by the newer checker and are not used in the proof. |
| `proof_map.csv` | PASS | Statement/proof ranges agree with the 790-line source and cover every specialized lemma/proposition used by the main proof. |
| `verify.py` | PASS by static review | Correctly pins the source SHA, checks exact interpolation/support/rank/bordered-minor identities and arithmetic, and performs numerical Schur/graph diagnostics. These tests do not substitute for proof. |
| `checks.json` | PASS as finite diagnostic | Reports 534 exact interpolation seeds, 18 volume cases, 9 strict cases, exact slack `297/2800`, 240 Schur threshold cases, and 30 graph cases. I independently re-derived the checker logic and counts from its deterministic loops; no theorem step relies on them. |

## 2. Complete manuscript line audit

Every source line 1--790 was read. `PASS` means I checked the displayed identity/inequality, the quantifiers and the way it is invoked downstream. `UNCHECKED` is not used for any manuscript proof line in this review.

| Lines | Label / content | Status | Reasoning, impact, next obligation |
|---|---|---|---|
| 1--46 | Preamble, notation, abstract | PASS | Scope matches theorem; no hidden moment, support, log-concavity, sign, diagonal, exact-rank or post-rotation independence assumption. |
| 47--61 | `thm:main`, `cor:33` | PASS | Quantifiers are complete. The corollary uses `s_17(A)>=s_33(A)` correctly. |
| 62--90 | Architecture, `eta=1/100`, `kappa=80^-2` | PASS | Pivot/no-pivot split and counts `9=4*3-3`, `17=4*5-3` match later arguments; continuity is not silently asserted in pivot branches. |
| 91--121 | `lem:fourier` | PASS | Fourier convention, Plancherel `2pi`, inversion `1/(2pi)`, Gaussian multiplier and weak/approximate-identity passage are consistent for rough laws. |
| 122--131 | `lem:envelope` | PASS | Envelope integral is exactly `2ap/(p-1)`, hence density cap `ap/[pi(p-1)]`. |
| 132--160 | `lem:riesz` | PASS | Gamma/Gaussian calculation gives coefficient `1/sqrt(2pi)`; the `3/4` envelope contributes weighted integral `12 sqrt(u)`. Tonelli covers extended nonnegative values. |
| 161--181 | `lem:rank` | PASS | Both singular-value perturbation statements are valid for nonsymmetric auxiliaries; the later proof correctly uses singular rather than eigenvalues for `A-E`. |
| 183--207 | `lem:schur` | PASS; cleaner replacement below | The moving-threshold perturbation proof is valid even if ambient `A` is singular. A direct rank proof removes the limiting step entirely; singular-pivot counterexamples show `det B !=0` is essential. |
| 209--217 | `lem:dd` | PASS | Standard strict row diagonal dominance; later inequalities retain strict positive slack. |
| 221--255 | `thm:bl` | PASS | Heat-flow sign is correct: `partial_t F-Delta F>=0`; frame norm controls the quadratic term. Gaussian tails justify integration by parts; large-time and monotone-truncation limits handle rough inputs. |
| 258--282 | `lem:projection` | PASS | Deterministic orthogonal completion plus BL gives `e^{d/2}`; no independence after rotation is claimed. The `b_i=0` bookkeeping is harmless. |
| 284--301 | `lem:scalar-fourier` | PASS | `m=floor(p/2)>=p/4`; difference density is `<=1`; inversion at zero applies to the integrable even power and projection density. |
| 310--324 | `lem:decoupling` | PASS | Only literal independent coordinate copies are introduced. Same-bank phases are handled before modulus; no conditional density cap is inferred from an unconditional projection. |
| 326--373 | `thm:determinant` | PASS | Frame weights `c_j,d_i`, trace identity, BL factors and scalar Fourier powers cancel at `alpha=(2pi e)^2`; fourth root gives determinant exponent `-1/8`. |
| 374--400 | crossing volume, `cor:vol-fourier` | PASS | Cauchy--Binet expansion is correct. Order 5 yields exponent `5/4>1` for density; order 3 is used only with the half-Riesz weight. |
| 404--414 | `lem:square` | PASS | Two inverse branches give the stated square-root envelope; interval preimage bound is uniform in affine terms. |
| 423--434 | `lem:definite` | PASS | Elliptic polar change of variables gives `pi M/sqrt(|det B|)` without assuming rotated independence. |
| 437--482 | `lem:hyperbola` | PASS | Hyperbolic coordinates, Jacobian `1/(2sqrt D)`, tail changes of variables and middle-length estimate give the logged envelope; critical level is handled through measure domination. |
| 485--525 | `lem:quarter` | PASS | Diagonal branch gives a stronger square-root small ball; off-diagonal sign partition yields a physical cross block of norm `>=L/4`, determinant bound gives `|t|^-1/4`, Gaussian test gives constant `<16`, and layer cake yields `L0=4+4log16`. |
| 528--535 | `def:pivot-volume` and no-pivot entry bound | PASS | Absence of a principal determinant pivot implies `|a_ij|^2<eta^2+eta`, hence `|a_ij|<1/7`. |
| 545--564 | `lem:sampling` | PASS | Determinant-squared seed sampling, nonsymmetric interpolation, bordered determinant and `(r+1)^2` multiplicity are correct. Singular seeds make the aggregate relation an inequality in the correct direction. |
| 566--580 | `lem:completion` | PASS | `D` vanishes on the seed, `E` has zero diagonal, `rank R<=3r` globally, while exactly `R_LL=P_LL` gives restricted rank `<=r`. These two ranks are used in different steps downstream. |
| 582--619 | `prop:volume` | PASS | Telescoping yields a bad ratio; `r=0` operator-norm contradiction is valid. For `r>=1`, `eps<=(r+1)/80<=1/16`; `m=4k-3>=4r+1` forces `r+1` large diagonal entries in `L`; diagonal dominance (`371/400` versus `<23/28`) contradicts restricted rank. |
| 621--630 | `lem:cut` | PASS | Each ordered disjoint pair survives a fair cut with probability `4^-k`; expectation and existence follow. |
| 632--645 | `cor:no-pivot` | PASS | Cut volume gives `Z_k^{-1/(2k)}<=160`; order 3 gives full half-potential `<200`, order 5 density `<2400`. |
| 654--674 | `lem:kernels` | PASS | The near/far split in `J(d)` and centered-interval overlap proof of the log kernel are valid by Tonelli. |
| 676--714 | `prop:pivot-H` | PASS | Scalar, definite and indefinite branches meet their precise hypotheses. The proposition is intentionally truncated; scalar branch in fact gives `H<=200+120log16`. |
| 716--724 | `prop:nine` | PASS | Pivot gives truncated `<=600`; no-pivot already gives full `<200`; outside distance one, the half kernel is `<=1`, hence full `<=601`. |
| 726--749 | Main proof | PASS | No-pivot uses 17/order5. Scalar pivot loses at most one direction and leaves enough for the nine-half-potential theorem. Definite pair is direct. Indefinite pair loses at most two directions and only needs one surviving unit direction for the logarithmic potential. Tonelli handles conditional critical values. |
| 750--790 | Scaling, accounting, limitations, bibliography | PASS | `Y=KX` gives density cap one and `Q=(s/K^2)Qtilde`, hence `K^2/s`. Limitations accurately say neither 17 optimality nor the unrestricted 3-eigenvalue theorem is proved. |

No manuscript line is left mathematically UNCHECKED by this review. The only UNCHECKED items are external/reproducibility metadata explicitly identified above (raw SHA recomputation, binary PDF render, historical old finite-test counts).

## 3. B11 Schur result: direct rank proof, no ambient invertibility

The manuscript's Lemma `lem:schur` is correct, but there is a simpler dependency-closed proof that makes the singular ambient case completely transparent.

Let
\[
A=\begin{pmatrix}B&C\\C^T&D\end{pmatrix},\qquad
B=B^T,\quad \det B\ne0,\qquad
S=D-C^TB^{-1}C.
\]
Set
\[
U=\begin{pmatrix}I_k\\ C^TB^{-1}\end{pmatrix}.
\]
Then the exact identity is
\[
\boxed{
A=UBU^T+\begin{pmatrix}0&0\\0&S\end{pmatrix}.}
\tag{3.1}
\]
The first summand has rank at most `k`. Apply the manuscript's nonsymmetric rank perturbation inequality to (3.1): for `1<=j<=n-k`,
\[
s_{j+k}(A)\le s_j(S).
\tag{3.2}
\]
Therefore, for every `t>0`,
\[
\boxed{N_S(t)\ge N_A(t)-k.}
\tag{3.3}
\]
This proof neither assumes `A` invertible nor perturbs a threshold. It also shows that the correct mechanism is rank loss, not a sign/inertia heuristic.

At zero threshold the usual congruence also gives exact inertia additivity
\[
\operatorname{Inertia}(A)=\operatorname{Inertia}(B)+\operatorname{Inertia}(S),
\]
but inertia alone does not control the magnitudes counted by `N_A(t)`; the examples below make this distinction sharp.

**Impact.** No repair of the theorem is needed; (3.1)--(3.3) are a shorter robust proof of the existing lemma and remove any concern about singular ambient matrices or endpoint continuity in the perturbative presentation.

## 4. Exact counterexamples: the Schur loss `k` is sharp even for tiny pivots

### 4.1 Singular pivot: Moore--Penrose substitution is false without a range condition

For any `k>=1`, take
\[
B=0_k,\qquad C=I_k,\qquad D=0_k,
\qquad
A=\begin{pmatrix}0&I\\I&0\end{pmatrix}.
\]
A naive pseudoinverse Schur complement is
\[
S_\dagger=D-C^TB^\dagger C=0.
\]
But `A` has `k` eigenvalues `+1` and `k` eigenvalues `-1`. Hence at `t=1`,
\[
N_A(1)=2k,\qquad N_{S_\dagger}(1)=0.
\]
The putative loss-`k` extension would require `0>=k`, false. Thus the manuscript hypothesis `det B !=0` is essential; a singular pivot cannot simply be replaced by `B^dagger`.

### 4.2 Arbitrarily near-singular invertible pivots consume all `k` directions

Let `J=diag(sigma_1,...,sigma_k)` with each `sigma_i in {+1,-1}` and `0<epsilon<1`. Define
\[
B_\epsilon=\epsilon J,\qquad
C_\epsilon=\sqrt\epsilon\,I_k,\qquad
D=J,
\]
\[
A_\epsilon=\begin{pmatrix}B_\epsilon&C_\epsilon\\C_\epsilon&D\end{pmatrix}.
\]
Since `B_epsilon^{-1}=epsilon^{-1}J`,
\[
S_\epsilon=J-C_\epsilon^TB_\epsilon^{-1}C_\epsilon=J-J=0.
\tag{4.1}
\]
After permuting coordinates, `A_epsilon` is the direct sum of the `k` matrices
\[
\sigma_i\begin{pmatrix}\epsilon&\sqrt\epsilon\\\sqrt\epsilon&1\end{pmatrix},
\]
whose eigenvalues are `sigma_i(1+epsilon)` and `0`. Therefore
\[
\operatorname{spec}(A_\epsilon)=
\{\sigma_i(1+\epsilon):1\le i\le k\}\cup\{0\}^k.
\tag{4.2}
\]
At threshold `t=1`,
\[
N_A(1)=k,\qquad N_S(1)=0,
\qquad N_{B_\epsilon}(1)=0.
\tag{4.3}
\]
Thus the full loss `k` in (3.3) is sharp even though the pivot is invertible and arbitrarily small in operator norm, has no threshold-large eigenvalues of its own, and the ambient matrix is singular. Choosing all `sigma_i=+1` gives a definite-pivot example; mixing signs gives an indefinite-pivot example. In particular, no universal improvement can replace `k` by `N_B(t)`, by a function that tends to zero with `||B||`, or by a smaller sign-dependent loss merely because the pivot is near-singular.

For the B11 pair case `k=2`, choose `J=diag(1,-1)`. Then exactly
\[
\operatorname{spec}(A_\epsilon)=\{1+\epsilon,-(1+\epsilon),0,0\},
\qquad S_\epsilon=0.
\]
One positive and one negative unit-scale direction are both consumed by an arbitrarily tiny indefinite pivot.

### 4.3 A correct singular-pivot extension requires compatibility

There is a useful exact repair if one ever needs a genuinely singular principal pivot. Suppose `B=B^T` may be singular but
\[
\operatorname{range}(C)\subseteq\operatorname{range}(B).
\]
Let `X=B^dagger C`, so `BX=C`, and put
\[
S_\dagger=D-C^TB^\dagger C.
\]
Then
\[
A=
\begin{pmatrix}I\\X^T\end{pmatrix}
B
\begin{pmatrix}I&X\end{pmatrix}
+
\begin{pmatrix}0&0\\0&S_\dagger\end{pmatrix}.
\tag{4.4}
\]
The first term has rank at most `rank B<=k`, so exactly the same rank argument gives `N_{S_dagger}(t)>=N_A(t)-k`. The range hypothesis is essential, as §4.1 shows.

**Downstream impact.** These examples rule out reducing multiplicity by reclaiming Schur directions from small/singular/indefinite pivots. Any further `9 -> 8` improvement must attack the no-pivot analytic/structural endpoint, not merely sharpen the Schur charge.

## 5. Reconstruction of the complete 17 -> 9 replacement

I did not lower the threshold on the strength of a scoped special case. I rechecked the complete replacement already present in the immutable improvement artifacts. Its new ingredient is a grouped physical-product Fourier compiler retaining literal source banks.

### 5.1 Grouped compiler

For disjoint original coordinate banks `H,I,J`, let `W` be a `k`-dimensional orthogonal projection of `X_H` with density cap `M_H`, and let the promoted `J`-coefficient matrix have nonzero singular-value product `S`. Project remaining physical crossing rows orthogonally off the promoted row span, call them `C`, and choose determinant weights on `ell`-row Gram minors with inclusion marginals `alpha_i<=1/2`. With `d=k+ell`, the compiler gives
\[
|\phi_Q(t)|\le\min\{1,K_{k,\ell}|t|^{-d/2}\},
\]
\[
K_{k,\ell}=M_H^{1/2}\pi^{d/2}2^{\ell/4}e^{(k+2\ell)/4}
\left(\frac{\ell^\ell}{\ell!}\right)^{1/4}
S^{-1/2}Z_\ell^{-1/4}.
\tag{5.1}
\]
The proof is source-valid: it pushes the complex phase from `H` to `W`, uses multidimensional Plancherel; conditions on literal `I`, duplicates literal `J`, smooths the pushforward, and uses Hilbert-space Jensen/Fatou. Weighted Holder then uses scalar Fourier powers at `p=1/alpha_i` and the exact Gram determinant `S^2 det(C_TC_T^T)`. The entropy inequality
\[
H(w)+\sum_i\alpha_i\log\alpha_i
\le\ell\log\ell-\log(\ell!)
\tag{5.2}
\]
closes the weighted determinant factors. No rotated coordinates are declared independent.

For `d>2`, inversion of (5.1) gives the explicit density bound recorded in the improvement. Heavy-row promotion via exact Gram--Schmidt identities removes the marginal hypothesis and yields
\[
\|p_Q\|_\infty\le C_3 E_3(M)^{-1/6},
\qquad
C_3=3\sqrt2\,e(9/2)^{1/6}=14.818337662843\ldots,
\tag{5.3}
\]
and, at order two,
\[
\sup_a\E|Q-a|^{-1/2}\le C_2E_2(M)^{-1/8},
\qquad
C_2=8\sqrt e\,2^{-1/8}=12.095072570796\ldots.
\tag{5.4}
\]
The latter is a half-potential statement, not a rank-two density claim.

### 5.2 Nine-direction assembly

Normalize `K=s=1` and retain baseline `eta=1/100`, `kappa=80^-2`.

- **No pivot.** Baseline `prop:volume` at order 3 requires exactly `s_9>=1`, gives `V_3>=kappa^3`, and a fair cut gives `E_3^{-1/6}<=160`. Equation (5.3) yields density `<2400`.
- **Scalar pivot.** Schur loses at most one direction, so eight remain. If the residual has a pivot, rereading baseline `prop:pivot-H` gives the sharper full half-potential bound
  \[
  \sup_a\E|R-a|^{-1/2}\le201+120\log16.
  \]
  If it has no pivot, eight directions imply `s_5>=1`; baseline order-two volume plus (5.4) gives `<153`. The outer square profile contributes `eta^{-1/2}=10`, hence
  \[
  \|p_Q\|_\infty\le2010+1200\log16=5337.106466\ldots<5338.
  \]
- **Definite pair.** Direct conditional density is `<=10pi<32`.
- **Indefinite pair.** Schur loses at most two directions; seven unit-scale directions remain, more than enough for the baseline quarter-power/log-potential argument; bound remains `<251`.

Rescaling exactly as in the baseline yields
\[
\boxed{
\|p_Q\|_\infty\le(2010+1200\log16)K^2/s<5338K^2/s
\quad\text{under }s_9(A)\ge s.}
\tag{5.5}
\]
All affine terms, signatures, remaining spectrum and rough independent input laws are retained. This is a complete fixed-multiplicity replacement, not a claim about three eigenvalues.

## 6. Why this run does not claim eight

The latest compatible multiplicity-eight structural work is materially stronger than the first selected-seed obstruction but still does not supply a complete density theorem.

If `s_8(A)>=1`, there is no pivot, and the order-three disjoint conclusion fails, the only failed interpolation ratio is `r=2`. One obtains a canonical completion with global rank six and restricted rank two; exactly two diagonal directions are `>=77/80`, while a third cannot exceed `519/1400`; moreover
\[
s_6(R)\ge1657/2800.
\]
All three nominal rank-two support pieces of the correction are simultaneously saturated, and three disjoint physical two-banks obey a quantitative determinant chain.

A complementary averaged theorem introduces overlap-one third volume
\[
W_{2,1}(A)=
\sum_{S,T,h}\det A_{S\cup\{h\},T\cup\{h\}}^2
\]
and proves
\[
\boxed{
W_{2,1}(A)\ge2s^2V_2(A)-12s\sqrt{V_2(A)V_3(A)}.}
\tag{6.1}
\]
Thus, in the normalized no-pivot `s_8` terminal state with `V_3<kappa^3`,
\[
W_{2,1}\ge\frac{37}{20}V_2\ge\frac{37}{20}\kappa^2.
\tag{6.2}
\]
For one overlap-one minor, the source-preserving triangular identity is
\[
q=2(X_S+Hr)^TB(X_T+Hq_0)+(2D_h-a)H^2,
\tag{6.3}
\]
with a large square coefficient on the heavy terminal directions. But the same physical coordinate `H` shears both bilinear banks and supplies the square. Conditioning on `H` preserves independence of the two original banks, while unconditionally the square and sheared bilinear term are dependent. A proof that replaces the sheared variables by independent ones, assumes a uniformly bounded shear translation, or pays only an arbitrary ambient joint-density cap is invalid.

Therefore the first unpaid fixed-multiplicity implication remains a **dependence-safe overlap-one/shared-anchor receiver** for (6.2)--(6.3), or a different complete mechanism. Schur sharpening cannot supply it: §4 proves the losses one and two are already sharp. I found no complete eight-eigenvalue replacement proof in the current source state and therefore do not lower the theorem below nine.

## 7. Audit status summary

- Pinned 17-eigenvalue manuscript: **PASS** in this independent end-to-end review.
- Schur lemma, including singular ambient matrices: **PASS**, with direct rank proof (3.1)--(3.3).
- Pseudoinverse singular-pivot extension without compatibility: **FALSE**, exact counterexample §4.1.
- Reducing Schur loss using pivot size / `N_B(t)` / near-singularity / sign: **FALSE**, sharp family §4.2.
- Singular-pivot extension under `range(C) subset range(B)`: **PASS**, proof §4.3.
- Complete multiplicity-nine replacement: **PASS** after reconstruction, explicit constant `<5338 K^2/s`.
- Multiplicity eight: **GAP / UNPROVED**; terminal structure is strong but the shared-anchor analytic receiver is missing.
- Unrestricted three-eigenvalue QFORM: **OPEN / NOT PROVED / NOT DISPROVED**.

Next exact obligation: construct a source-valid aggregate overlap-one receiver that consumes (6.2) while retaining the shared physical coordinate through the bilinear/square averaging, or provide a valid counterexample to multiplicity eight. Do not attempt to recover a direction by weakening the Schur loss; the all-`k` family (4.1)--(4.3) rules that out.
