SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet03, slot B11, 2026-09-24T12:10:16Z.
attacking: current owner objective QFORM-FIXED-MULTIPLICITY-AUDIT-20260924 through the B11 Schur-complement spectral-count lens, followed by an independent end-to-end proof audit and threshold accounting.

# fleet03/B11 full audit — Schur complement spectral counts and end-to-end check

Run: `20260924T121016Z-fleet03-B11-fixedmult-audit-auto11`  
Current objective: `QFORM-FIXED-MULTIPLICITY-AUDIT-20260924`  
Pinned baseline source: `yspennstate/math-open-problems@7c0d6e60946b19423e6400a12d34b473cf0591e2`  
Pinned `manuscript.tex` blob: `183ccd294763214e6a707e8d4749ff9a8cf7006d`  
Pinned source SHA-256 reported by the manuscript package: `9f3bdec0b88debe9a66076c7b4a5cc894fb14e69b89591a4107e785340f65e69`.

## Verdict

**PASS as one independent complete textual audit of the written 17-eigenvalue theorem.** I found no FALSE mathematical statement and no theorem-breaking GAP in the 790-line baseline proof. This is one worker review only; it is not a self-awarded release/peer-review certificate, and it does not prove the unrestricted three-eigenvalue conjecture.

There is one repository/reproducibility GAP, not a proof gap: at the current-master snapshots inspected during this run, the root contains `README.md`, `AUDIT.md`, `manuscript.tex`, `audits/`, and `improvements/`, but the README-referenced `SOURCE_MANIFEST.json`, `proof_map.csv`, `verify.py`, and `checks.json` are absent. The mathematical argument is self-contained in `manuscript.tex`, so these missing supplementary files do not enter the proof.

## B11 result: exact Schur-count theorem, singular case included

The manuscript lemma states: for

\[
A=\begin{pmatrix}B&C\\C^T&D\end{pmatrix},\qquad B=B^T\in\mathbb R^{k\times k},\quad \det B\ne0,
\]
with Schur complement
\[
S=D-C^TB^{-1}C,
\]
then for every `t>0`,
\[
\boxed{N_S(t)\ge N_A(t)-k},\qquad N_T(t)=\#\{j:|\lambda_j(T)|\ge t\}.
\]
This is correct, including singular `A`.

### Independent derivation for invertible A

Block elimination gives
\[
LAR=\operatorname{diag}(B,S),
\]
so when `A` is invertible, `S` is invertible and the lower-right principal block of `A^{-1}` is exactly `S^{-1}`. For a Hermitian principal compression `H_0` of a Hermitian matrix `H`, Cauchy interlacing separately implies
\[
\#\{\lambda(H_0)>a\}\le\#\{\lambda(H)>a\},\qquad
\#\{\lambda(H_0)<-a\}\le\#\{\lambda(H)<-a\}.
\]
Adding the two inequalities with `H=A^{-1}`, `H_0=S^{-1}`, and `a=t^{-1}` gives
\[
\#\{|\lambda(S^{-1})|>t^{-1}\}
\le
\#\{|\lambda(A^{-1})|>t^{-1}\}.
\]
For an invertible matrix the left side is `(n-k)-N_S(t)` and the right side is `n-N_A(t)`, because strict `|lambda^{-1}|>t^{-1}` is equivalent to `|lambda|<t`. Rearrangement gives the displayed count inequality with the manuscript's inclusive `>=t` convention exactly, including eigenvalues on the threshold.

### Singular A

Choose `epsilon_m ->0` avoiding the finitely many forbidden values for which either `A+epsilon_m I` or `B+epsilon_m I_k` is singular, and with `|epsilon_m|<t`. Let
\[
S_m=D+\epsilon_m I-C^T(B+\epsilon_m I)^{-1}C.
\]
Then `S_m -> S`. Weyl's inequality gives
\[
N_{A+\epsilon_m I}(t-|\epsilon_m|)\ge N_A(t).
\]
Applying the invertible case at threshold `t-|epsilon_m|` therefore gives
\[
N_{S_m}(t-|\epsilon_m|)\ge N_A(t)-k.
\]
If `r=N_A(t)-k>0`, this says the `r`-th singular value of `S_m` is at least `t-|epsilon_m|`; continuity of singular values yields `s_r(S)>=t`, hence `N_S(t)>=r`. If `r<=0` the claim is trivial. This closes the singular case without an unstated invertibility hypothesis.

### Pointwise equivalent and sharpness

The count lemma is equivalently the useful pointwise family
\[
\boxed{s_j(S)\ge s_{j+k}(A),\qquad 1\le j\le n-k,}
\]
where for symmetric matrices `s_j` denotes ordered absolute eigenvalues. Indeed, use the count statement at `t=s_{j+k}(A)`.

The loss of exactly `k` directions is sharp, even allowing singular `A`. For any `r>=1`, take
\[
A=\operatorname{diag}(2tI_k,2tI_r,0),\qquad B=2tI_k,
\]
with the final zero block optional. Then `S=diag(2tI_r,0)`, so
\[
N_A(t)=k+r,\qquad N_S(t)=r=N_A(t)-k.
\]
Thus no general Schur-count improvement can come from replacing `-k` by a smaller loss.

## Exact downstream threshold accounting

The pointwise formulation makes clear that the Schur step is **not** what forces the global threshold 17.

* Scalar pivot (`k=1`): the manuscript needs the Schur remainder to satisfy `s_9(S)>=1` in order to use Proposition `prop:nine`. Therefore this entire pivot branch already closes from `s_10(A)>=1`, with the same normalized density bound `6010`.
* Definite 2-coordinate pivot: the conditional two-dimensional density bound is immediate from the pivot determinant and needs no surviving spectral direction.
* Indefinite 2-coordinate pivot (`k=2`): the logarithmic critical-value average only needs `||S||>=1`, hence `s_3(A)>=1` already guarantees this branch through `s_1(S)>=s_3(A)>=1`. The same normalized manuscript bound `<251` follows.
* Consequently the present theorem's threshold 17 comes from the **no-pivot** order-five crossing-volume/Fourier-inversion branch, not from loss in the Schur complement.

A recent source-valid supporting result from fleet02/B04 sharpens this accounting conditionally: if an order-three crossing block has maximum row leverage at most `1/2`, then
\[
\|p_Q\|_\infty\le3\sqrt2 e\,Z_3(M)^{-1/6}.
\]
The baseline no-pivot `s_9(A)>=1` volume argument gives `Z_3^{-1/6}<=160`, so on that leverage subbranch
\[
\boxed{\|p_Q\|_\infty\le480\sqrt2 e=1845.230893516376\ldots.}
\]
This does **not** prove a nine-eigenvalue theorem: the existing random-cut volume argument does not control the row leverage, and high-leverage crossings remain a genuine branch.

Likewise, the fresh fleet01/B15 endpoint theorem confirms that the baseline order-four no-pivot branch (`s_13>=1`) yields an `L^2` density and `|phi(t)|=O(1/|t|)`, but not an `L^infinity` bound. Thus no valid `17 -> 13` theorem is inferred from absolute Fourier inversion alone.

## End-to-end audit table

The ranges below are broad source ranges in the pinned 790-line file; statement labels identify the exact object checked.

| Source range / statement | Status | Independent check | Downstream impact |
|---|---|---|---|
| lines 1–120, theorem statement, normalization, Gaussian/Fourier conventions | PASS | Scaling `Y=KX`, `tilde Q=(K^2/s)Q` is exact; density rescales by `K^2/s`. Gaussian inversion and Plancherel constants match the Fourier convention. | Main quantifiers and final scaling sound. |
| lines 121–240, power envelope, Riesz half potential, rank perturbation, `lem:schur` | PASS | Weighted Fourier integral is `12 sqrt(u)`; rank perturbation direction is correct; Schur lemma independently reproved above, including threshold equality and singular `A`. | Pivot spectral bookkeeping sound. |
| lines 241–360, geometric rank-one BL, product projection, scalar Fourier powers, decoupling | PASS | Heat-flow sign is nonnegative from the frame contraction; the large-time Gaussian normalization uses `sum c_i=d`; projection proof rotates only deterministic integration variables, not probabilistic independence; scalar Fourier power uses genuine independent copies; decoupling conditions on original coordinate blocks only. | No hidden rotated-independence assumption. |
| lines 361–480, regularized determinant, crossing volumes, scalar/definite/hyperbolic local estimates | PASS | Frame weights and Jacobians cancel at `alpha=(2pi e)^2`; fourth root gives determinant exponent `-1/8`; `k=5` gives integrable `|t|^-5/4`, `k=3` is used only with the Riesz weight. Hyperbolic coarea Jacobian and tail monotonicity are consistent. | Fourier and local pair receivers sound. |
| lines 481–600, hyperbolic tails, quarter-power concentration, sampling, completion | PASS | Random-sign cut produces a physical crossing of norm at least `L/4`; bordered-minor counting is correctly an inequality when singular seeds are omitted; `P` exactly interpolates rows `S` and columns `T`; `R[L,L]=P[L,L]`, `rank R[L,L]<=r`, `rank R<=3r`. | Sensitive nonsymmetric interpolation chain sound. |
| lines 601–720, spectral-to-volume, random cut, no-pivot consequences, kernel bounds, pivot half potential | PASS | For bad ratio order `r`, `eps<=(r+1)/80<=1/16`; `m=4k-3>=4r+1`; after global rank loss `3r`, at least `r+1` large diagonal entries remain in `L`; strict diagonal dominance (`371/400>23/28`) contradicts restricted rank `<=r`. Kernel layer-cake and constants check. | 9-direction half-potential and 17-direction no-pivot density branches close. |
| lines 721–790, `prop:nine`, main proof, scaling, limitations | PASS | Pivot/no-pivot split is exhaustive. Branch bounds independently recompute to `6010`, `800e=2174.625...`, `<40`, and `238.997...<251`; final `10000 K^2/s` follows. Regularity is correctly limited: global theorem asserts essential boundedness, not continuity. | Candidate theorem closes as written. |
| README/AUDIT references to `SOURCE_MANIFEST.json`, `proof_map.csv`, `verify.py`, `checks.json` | GAP (repository only) | Files were absent from fresh root listings and direct path reads in this run. | Reproducibility/documentation gap; no proof dependency because manuscript is self-contained. |

## Finite diagnostics in this run

`SCHUR_VERIFY.py` is saved beside this audit. It tests the pointwise inequality `s_j(S)>=s_{j+k}(A)` on 6,000 random nonsingular symmetric block matrices and 2,700 deliberately singular matrices reconstructed from a singular Schur complement. The largest numerical excess in the singular suite is about `2.95e-15`, at roundoff scale; no positive violation occurred in the nonsingular suite. The script also prints the exact branch constants above. These computations are diagnostics only and do not replace the proof.

## Threshold-reduction conclusion

No unconditional multiplicity reduction below 17 is proved in this run. The B11 analysis rules out Schur spectral loss as the bottleneck: its `k`-direction loss is exact and already far below the global threshold in every pivot branch. The sharp next target is the no-pivot chamber, especially an order-four endpoint compiler or an aggregate order-three receiver that handles the complementary high-leverage case without selecting a dimension-losing minor. The current 17-eigenvalue theorem survives this audit; the full three-eigenvalue conjecture remains open.

Status: `WITHOUT_VERIFIED_BRAIN`. Repository retrieval/write occurred, but native authenticated brain-receiver ingestion was not exposed or verified in this run.