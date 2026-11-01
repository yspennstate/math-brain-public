# fleet03/B07 independent fixed-multiplicity audit r1

Objective: `QFORM-FIXED-MULTIPLICITY-AUDIT-20260924`.

Pinned theorem source: `yspennstate/math-open-problems@7c0d6e60946b19423e6400a12d34b473cf0591e2`, `proofnet24/QFORM-density/fixed-multiplicity-2026-09-24/manuscript.tex`.
Git blob: `183ccd294763214e6a707e8d4749ff9a8cf7006d`.
Advertised SHA-256: `9f3bdec0b88debe9a66076c7b4a5cc894fb14e69b89591a4107e785340f65e69` (not independently recomputed in this connector-only run).
Reviewer lens: B07 ordered minors, bordered determinants, and sampling multiplicities; fleet03 emphasis on exact identities and alternative derivations.

## Verdict

**PASS for the 17-eigenvalue theorem as a complete textual proof audit in this run; no fatal mathematical gap found.** This is one worker review, not the two-independent-review release gate and not a proof of the unrestricted three-eigenvalue conjecture.

There is one **repository-package GAP**: on the master snapshots inspected in this run the manuscript root contained `manuscript.tex`, `README.md`, `AUDIT.md`, and audit/improvement directories, while `README.md` names `SOURCE_MANIFEST.json`, `proof_map.csv`, `verify.py`, and `checks.json` as canonical package members. Direct fetch of `proof_map.csv` returned 404, and code search found peer reports recording the same absence. This is a reproducibility/documentation gap, not a theorem dependency, because the mathematical argument is self-contained in `manuscript.tex`.

## End-to-end audit table

| Source range | Status | Independent check | Downstream impact |
|---|---|---|---|
| lines 1–120: definitions, theorem, scaling architecture, Gaussian/Fourier setup | PASS | Quantifiers match arbitrary independent real coordinate densities `<=K`, arbitrary symmetric `A`, arbitrary `b,c`; normalized `K=s=1` reduction and final `K^2/s` scaling are dimensionally correct. Gaussian inversion is used only with its integrability hypotheses. | Main statement scope preserved. |
| lines 121–300: Fourier envelope, Riesz half-potential, rank perturbation, Schur count, BL heat flow, projection density, scalar Fourier powers | PASS | Re-derived the `12 sqrt(u/(2pi))` half-potential constant; checked the singular-value rank inequality orientation; checked the Schur complement count by applying principal-compression interlacing to `A^{-1}` and `-A^{-1}`, including the singular limit; checked the BL normalization `sum c_i=d` and the projection scaling. | Analytic inputs used later have the stated hypotheses. |
| lines 301–400: decoupling and regularized determinant | PASS | `|phi|^4` follows from Jensen after the first Cauchy–Schwarz decoupling. In the BL determinant calculation, the `d_i^{-d_i/2}` factor cancels the `sqrt(d_i)` in the scalar Fourier-power bound, while `prod c_j^{-c_j/2} <= e^{theta/2}` upgrades `(2pi sqrt(e))^theta` to `(2pi e)^theta`; with `alpha=(2pi e)^2` the residual scalar factor is exactly one. Fourth roots therefore give determinant exponent `-1/8`. | Order-five crossing volume gives an integrable `|t|^{-5/4}` envelope; order three gives the weighted half-potential envelope only. |
| lines 401–527: scalar/definite/hyperbolic pivots and quarter-power concentration | PASS | Conditioning is only on original coordinates. The deterministic orthogonal changes are inside two-dimensional integrals and never assert rotated independence. The hyperbolic coarea Jacobian is `1/(2 sqrt D)`; the tail argument uses one original coordinate at a time and only the cap/mass constraints. Quarter-power concentration correctly separates the diagonal and off-diagonal cases. | Pivot branches remain valid for rough, unbounded-support laws. |
| lines 528–651: `V_r`, `lem:sampling`, `lem:completion`, `prop:volume`, random cut, no-pivot consequences | PASS | This was the primary audit. The bordered determinant identity, ordered-pair multiplicity, nonsymmetric interpolation support, global rank `<=3r`, restricted rank `<=r`, seed-zero diagonal `D`, diagonal-dominance contradiction, and `4^{-k}` random-cut factor all check exactly. A sharper exact multiplicity identity is proved below. | The no-pivot `s_9` half-potential and `s_17` density branches close as written. |
| lines 652–790: singular kernels, pivot half-potential, nine-eigenvalue half-potential, main case split and general scaling | PASS | Full versus truncated half potentials are not conflated: `H(Q)<=600` plus the outside kernel bound `<=1` gives the full `<=601`. Scalar Schur leaves 16 directions and only nine are needed; pair Schur leaves 15 and only one is used for the logarithmic potential. Final normalized branch maxima are below `10^4`; rescaling gives `10^4 K^2/s`. | Candidate theorem closes. |
| bibliography attribution | UNCHECKED (non-proof) | I did not independently re-run a primary-source literature audit of BCCT/Rudelson–Vershynin in this B07 run. The manuscript explicitly reproves the specialized inequalities it uses, so no theorem step depends on those citations. | No mathematical downstream effect. |

## B07 exact refinement: deletion-multiplicity identity

For disjoint `(r+1)`-sets `U,V`, define

`m_A(U,V) = #{(u,v) in U x V : det A[U\{u}, V\{v}] != 0}`.

Under the sampling law of Lemma `lem:sampling` (a nonsingular disjoint `r x r` seed `(S,T)` chosen with probability `det(A[S,T])^2 / V_r(A)`), the proof actually gives the exact identity

`E ||off(A[L,L]-P[L,L])||_F^2`
` = (1/V_r(A)) * sum_{U,V disjoint, |U|=|V|=r+1} m_A(U,V) det(A[U,V])^2.`

**Proof.** For a sampled nonsingular seed `(S,T)` and distinct `ell,m` in the complement, the bordered determinant formula is

`det A[S∪{ell}, T∪{m}]^2 = det(A[S,T])^2 |A_ell,m-P_ell,m|^2`.

Multiplying by the sampling weight cancels the seed determinant. Regroup the resulting sum by the extension `(U,V)=(S∪{ell},T∪{m})`. A deletion `(u,v)` contributes exactly when the deleted seed is nonsingular, and each such deletion is represented once. This gives the displayed identity. Since `m_A(U,V) <= (r+1)^2`, Lemma `lem:sampling` follows immediately.

This makes precise why the manuscript correctly has an inequality rather than an equality with `(r+1)^2 V_{r+1}`: singular deleted seeds simply do not occur in the sampling law even when their extension is nonsingular.

### Sharpness of the combinatorial factor

The factor `(r+1)^2` cannot be replaced by a smaller universal deletion-count constant. Take any nonsingular `(r+1)x(r+1)` matrix `C` all of whose `r x r` cofactors are nonzero (for example a generic Cauchy matrix), choose disjoint coordinate sets `U,V`, and embed it in the symmetric matrix with cross block `A[U,V]=C`, `A[V,U]=C^T`. For this extension every one of the `(r+1)^2` row/column deletions is a nonsingular seed, so `m_A(U,V)=(r+1)^2`.

Therefore any threshold improvement from this part of the proof must use additional algebra/spectral structure, not merely a better universal counting constant in Lemma `lem:sampling`.

## B07 exact saturation of both interpolation rank bounds

The two rank estimates in Lemma `lem:completion` are simultaneously sharp, even with `E=0`. Consider

`A0 = [[-3, 1,-3,-3],`
`      [ 1,-3,-3,-3],`
`      [-3,-3,10, 9],`
`      [-3,-3, 9, 9]]`,

with seed `S={1}`, `T={2}`, so `B=[1]` and `L={3,4}`. Then

`P=A[:,T] B^{-1} A[S,:]`
` = [[-3, 1,-3,-3],`
`    [ 9,-3, 9, 9],`
`    [ 9,-3, 9, 9],`
`    [ 9,-3, 9, 9]].`

On `L x L`, `A0-P = [[1,0],[0,0]]`, hence the off-diagonal error `F` is zero and the completion has `E=0`,

`D=diag(0,0,1,0)`,

`R=A0-D`
` = [[-3, 1,-3,-3],`
`    [ 1,-3,-3,-3],`
`    [-3,-3, 9, 9],`
`    [-3,-3, 9, 9]].`

Exact integer elimination gives

`rank(R)=3`, `rank(R[L,L])=1`, `rank(D)=1`, `rank(D+R)=rank(A0)=4`, and `det(A0)=144`.

Direct sums of `r` copies, with the global seed taking the first coordinate of each copy into `S` and the second into `T`, give simultaneously

`rank(R)=3r`, `rank(R[L,L])=r`, `rank(D)=r`, `rank(D+R)=4r`.

So the rank-only step in Proposition `prop:volume` genuinely needs **one more** large diagonal direction than `r`: with only `r` such directions, the global `3r` carrier plus the diagonal can have rank `4r` without contradicting the restricted rank `r`. This is not a counterexample to any lower multiplicity theorem, because this witness does not satisfy the manuscript's no-pivot small-entry regime. It is an exact obstruction to lowering `4r+1` to `4r` by bookkeeping alone.

## Threshold consequence

This audit does **not** lower 17. It does establish where a B07-side improvement cannot come from:

1. the deletion-count factor `(r+1)^2` is universally sharp;
2. the simultaneous global/restricted rank pair `(3r,r)` is algebraically sharp;
3. the `4r+1` contradiction cannot be changed to `4r` using only those rank inequalities and the same diagonal-residual argument.

A rigorous reduction below 17 must therefore introduce genuinely new information: e.g. a structural relation between the large diagonal residuals and the seed/cross volume, a lower-order analytic receiver stronger than the present order-five `L^1` Fourier route, or a different interpolation whose error is controlled while its global rank is strictly below `3r` in the relevant no-pivot regime.

## Review status and next obligation

- Mathematical status of pinned 17-eigenvalue manuscript in this review: **PASS**.
- Independent-validation gate: **NOT SATISFIED BY THIS FILE ALONE**.
- Unrestricted three-eigenvalue conjecture: **OPEN**.
- Next B07 obligation: seek a new structural identity that couples the same-index bordered determinants `det A[S∪{ell},T∪{ell}] = det(B)(A_ell,ell-P_ell,ell)` to disjoint `(r+1)`-minor mass, because those same-index determinants are exactly the diagonal residuals not seen by `V_{r+1}`. A successful dimension-free conversion of that overlap-one mass into disjoint volume is a concrete route that could beat the `4r+1` barrier; mere resampling cannot.
