# account02/B17 — full fixed-multiplicity audit, run 20260924T144432Z

Objective: `QFORM-FIXED-MULTIPLICITY-AUDIT-20260924`.

## Source pin and review boundary

I resolved the source repository `yspennstate/math-open-problems` on `master` before this review at commit

`0aa54bd634644b2922e9faecd003692d7f29e61e`.

At that commit the package file `proofnet24/QFORM-density/fixed-multiplicity-2026-09-24/manuscript.tex` has git blob

`183ccd294763214e6a707e8d4749ff9a8cf7006d`,

exactly the blob pinned by the package manifest to the original manuscript commit

`7c0d6e60946b19423e6400a12d34b473cf0591e2`.

The package-declared SHA-256 is

`9f3bdec0b88debe9a66076c7b4a5cc894fb14e69b89591a4107e785340f65e69`.

I independently checked the Git object identity/current-master equality through the connector. I did **not** independently recompute the SHA-256 from locally materialized raw bytes in this run, so the SHA-256 recomputation itself is `UNCHECKED`; the exact git blob identity is checked. The source commit exists and its diff is the 790-line manuscript.

I read in full: `README.md`, `SOURCE_MANIFEST.json`, `manuscript.tex` lines 1--790, `AUDIT.md`, `proof_map.csv`, `verify.py`, and `checks.json`; I also read `DELIVERY_STATUS.md` because the package README designates it as current delivery metadata.

## Overall mathematical verdict

**PASS** for the literal pinned 17-eigenvalue theorem:

> independent real coordinates with density caps `K`; arbitrary real symmetric `A`; arbitrary affine terms; if `s_17(A)>=s>0`, then `X^TAX+b^TX+c` has a density with essential supremum at most `10000 K^2/s`.

I found no mathematical `FALSE` statement and no unresolved mathematical `GAP` in the 790-line proof. The unrestricted three-eigenvalue theorem is not claimed and remains open. Continuity of the full theorem is not claimed.

The only `UNCHECKED` items in this audit are non-proof items: (i) independent recomputation of the package SHA-256 from raw bytes, (ii) independent execution of the historical/current numerical checker suite, and (iii) exhaustive bibliographic priority/completeness. None is used as a proof step.

## End-to-end line audit

The status table below is exhaustive over the mathematical source ranges. A range marked PASS means I checked every definition/equation/invocation in that range against the stated hypotheses, not merely the named headline lemma.

### Lines 1--46 — front matter, definitions in abstract, scope

**PASS.** The abstract matches the theorem eventually proved. It does not introduce hidden moments/support/log-concavity or a rotated-product assumption. The auxiliary nonsymmetric matrices are advertised only for deterministic algebra, consistently with their later use.

### Lines 47--80 — theorem, normalization, proof architecture

**PASS.** `s_j(A)` is correctly interpreted as ordered absolute eigenvalues for symmetric `A`. The density statement and interval formulation are equivalent. The scaling is later performed by `Y=KX`, `A -> A/s`; cap one is preserved and density rescaling contributes exactly `K^2/s`. The fixed parameters are

`eta=1/100`, `kappa=1/80^2`.

The accounting `9=4*3-3`, `17=4*5-3` is used exactly in the later volume propositions.

### Lines 81--120 — Fourier convention, Gaussian regularization, inversion

**PASS.** With `hat f(t)=int e^{itx}f(x)dx`, Plancherel carries the `2*pi` factor stated. Gaussian regularization is valid for rough laws. The use of monotone convergence on `e^{-eps t^2}|hat f|^2` and uniform convergence under an `L^1` characteristic function correctly produces a bounded continuous density in the places where `L^1` Fourier control is available. No continuity is propagated into branches that only have measure domination.

### Lines 122--130 — power envelope

**PASS.** The integral

`int min(1,(a/|t|)^p) dt = 2 a p/(p-1)`

is exact for `p>1`; Fourier inversion gives `a p/[pi(p-1)]`.

### Lines 132--160 — negative half moments / Riesz kernel

**PASS.** The Gamma representation and Gaussian inversion yield

`E|Z-a|^{-1/2} <= (2*pi)^(-1/2) int |t|^{-1/2}|phi_Z(t)| dt`.

For `min(1,(u/|t|)^(3/4))`, the weighted integral is `12 sqrt(u)`, giving the displayed constant. All Tonelli uses are on nonnegative quantities.

### Lines 161--181 — perturbation and rank

**PASS.** Both singular-value inequalities follow from the best low-rank approximation formula and require no symmetry; this is essential because the interpolation correction used later is nonsymmetric.

### Lines 183--207 — principal Schur spectral count, including singular ambient matrices

**PASS.** For invertible ambient `A`, `S^{-1}` is the complementary principal block of `A^{-1}` and Cauchy interlacing, applied separately to positive/negative eigenvalues, gives `N_S(t)>=N_A(t)-k`. For singular ambient `A`, apply the invertible statement to `A+eps I` at threshold `t-|eps|`. If `m=N_A(t)-k>0`, then `S_eps` has at least `m` singular/eigenvalue moduli at least `t-|eps|`; the pivot stays invertible for small `eps`, `S_eps -> S`, and continuity of the ordered singular values gives `s_m(S)>=t`. Thus the moving-threshold limit is valid as written; no fixed-delta repair is required.

### Lines 209--217 — strict diagonal dominance

**PASS.** The row argument works for the nonsymmetric restriction used later: a nonzero kernel vector with maximal coordinate contradicts strict row diagonal dominance.

### Lines 218--255 — geometric Brascamp--Lieb heat flow

**PASS.** The frame identity makes the derivative term nonnegative because the analysis map is contractive. The heat-flow limit gives the product of masses. Gaussian tails/Fatou justify the rough limiting step at the constants claimed. No external BL theorem is used as a hidden dependency.

### Lines 258--282 — product-projection densities

**PASS.** Orthogonal completion plus geometric BL gives the joint projection density bound `e^(d/2)`. The factors `b_i^{-1/2}` and `prod b_i^{-b_i/2}` are controlled using `-b log b <= 1-b` and `sum(1-b_i)=d`. The one-dimensional scaled corollary has the stated coefficient. Orthogonal maps here are deterministic Jacobian devices; they do not assert independence of rotated coordinates.

### Lines 284--301 — scalar Fourier powers

**PASS.** Taking `m=floor(p/2)>=p/4`, Plancherel turns `|hat f|^(2m)` into the density at zero of a sum of `m` independent differences. The scalar product-projection cap for that literal independent sum yields

`int |hat f|^p <= 2*pi*sqrt(2e)/sqrt(p)`.

All exponents and constants check.

### Lines 302--324 — decoupling

**PASS.** The duplicate is taken only in a literal product bank. Pure same-bank phases cancel under the square; the difference vector retains independent coordinates with convolution densities bounded by one. Jensen/Cauchy--Schwarz give the fourth-power reduction stated. No arbitrary rotated copy or false conditional independence is inserted.

### Lines 326--373 — regularized determinant Fourier estimate

**PASS.** With `H=alpha I+a^2 M^T M`, `alpha=(2*pi*e)^2`, the geometric-frame construction is exact. After the `H^{-1/2}` change of variables, the determinant factor and BL exponents cancel as stated. The scalar Fourier-power constants cancel the chosen `alpha`; Cauchy--Binet gives

`det(I+t^2 M^T M/(pi^2 e^2))^{-1/8}`

after the fourth root. The entropy-type `c_i` factor is bounded by `e^(theta/2)` exactly as used.

### Lines 374--400 — disjoint crossing volumes and Fourier receivers

**PASS.** The Cauchy--Binet identity for `Z_k` is correct. Retaining the order-`k` determinant term gives the stated `u_k`; for `k=5` Fourier inversion gives the density constant used later, and for `k=3` the Riesz integral gives the half-potential constant. Dimensions and powers of `Z_k` are consistent.

### Lines 401--414 — scalar square profile

**PASS.** Completing the square in a literal original coordinate and bounding the preimage of an interval under a parabola gives the measure domination used later. No independence between the completed square and the Schur remainder is asserted.

### Lines 415--434 — definite two-coordinate pivot

**PASS.** Conditional on the remaining original coordinates, an orthogonal change is used only inside the deterministic two-dimensional integral. The joint density cap is preserved by Jacobian one; polar/elliptic coordinates give `pi M/sqrt(det)` as claimed.

### Lines 437--482 — indefinite/hyperbolic pivot envelope

**PASS.** The hyperbola parametrization, coarea Jacobian `1/(2 sqrt D)`, central/tail split and original-coordinate tail bound are consistent. The chosen coordinate has coefficient at least `rho_0/sqrt2`; along each tail the derivative dominates the coordinate by the stated constant, and the cap-one bathtub integral gives at most `log 2`. The middle interval gives the logarithmic term. Both signs of the level and exceptional levels are covered in the measure formulation.

### Lines 485--525 — quarter-power weak concentration / logarithmic potential

**PASS.** If a diagonal is large, the square-profile small ball gives the required `rho^(1/4)` bound. Otherwise the off-diagonal part has norm at least `L/2`; random signs produce a physical crossing block of norm at least `L/4`. Retaining the largest singular factor in the determinant estimate gives the `|t|^{-1/4}` envelope. Gaussian smoothing and the Gamma integral yield the quarter-power small-ball estimate. Layer cake gives `L_0=4+4 log 16`. No atom is left at a critical level.

### Lines 526--535 — pivot/volume definitions

**PASS.** In the no-pivot chamber, `|A_ii|<eta` and every principal `2x2` determinant has modulus below `eta`. Hence

`|A_ij|^2 < eta+eta^2 < 2 eta`,

so with the chosen constants `|A_ij|<1/7`; this is the entry bound used later.

### Lines 545--564 — determinant-weighted sampling/interpolation

**PASS.** For a nonsingular disjoint seed `B=A[S,T]`, the exact bordered determinant identity is

`det A[S+h,T+k]^2 = det(B)^2 (A_hk-P_hk)^2`.

Summing over possible deleted row/column choices gives the `(r+1)^2` multiplicity upper bound. Omitting singular seeds only weakens the inequality in the correct direction. The sampled interpolant exactly matches the seed rows/columns needed later.

### Lines 566--580 — completion and both rank bounds

**PASS.** With `E` the off-diagonal interpolation error on `LxL` and `D` the diagonal error, `D` vanishes on the seed. The remainder `R=A-D-E` satisfies

`rank R <= 3r`, `rank R[L,L] <= r`.

The first comes from the interpolant plus row/column supported pieces; the second is the exact `P[L,L]` restriction. No symmetry of `R` is assumed or needed.

### Lines 582--619 — spectral-to-volume conversion

**PASS.** If `V_k<kappa^k`, a first small ratio occurs at some `r<=k-1`. Sampling gives `||E||` small. Rank perturbation yields at least `r+1` large diagonal entries of `D` because

`(4k-3)-3r >= r+1` for `r<=k-1`.

They lie in the seed complement. On an `(r+1)`-set, the diagonal entries of `R` dominate the row sums using the exact constants (`371/400 > 23/28` in the worst `r<=4` case), so `R[L,L]` would have rank at least `r+1`, contradicting `rank R[L,L]<=r`. The `r=0` case separately contradicts `||A||>=1`.

### Lines 621--645 — random coordinate cut and no-pivot consequences

**PASS.** Each ordered disjoint `k`-minor crosses a fair two-color cut with probability `4^{-k}`, so some deterministic cut has `Z_k>=4^{-k}V_k`. With `kappa=80^{-2}`, the manuscript's `k=3` half-potential and `k=5` density constants are numerically below `200` and `2400` respectively.

### Lines 646--674 — singular kernels

**PASS.** The square-root/log kernel estimates are correct. For the shifted `J(d)` kernel, splitting at `2|d|` and using the cap-one bathtub bound controls the near and far parts. The centered log-kernel integral is maximized by the bathtub/centering argument and equals the stated finite constant.

### Lines 676--714 — full versus truncated half-potential in pivot branches

**PASS.** The proposition first controls the truncated singular kernel in each scalar/definite/indefinite pivot branch and then adds at most one from `|R-a|>1`, correctly converting truncated to full half-potential. The worst scalar bound is below `600` in the displayed rounded constants. Definite and indefinite pair estimates are smaller. The proof uses only the exact spectral directions stated for the Schur remainder.

### Lines 716--724 — nine-direction half-potential proposition

**PASS.** If a pivot exists, the previous proposition applies. If no pivot and `s_9>=1`, order-three spectral-to-volume plus a fair cut gives the `k=3` half-potential under `200`; adding the tail produces the stated full bound. This proposition is a half-potential theorem, not a nine-eigenvalue density theorem by itself.

### Lines 725--749 — main 17-eigenvalue theorem

**PASS.** The four exhaustive physical-coordinate branches close:

1. no pivot: `s_17` -> order-five volume -> density `<2400`;
2. scalar pivot: Schur retains at least 16 unit directions, hence in particular nine; full half-potential `<=601`, square profile factor at most `10`, so `<=6010`;
3. definite principal pair: direct `<=10*pi`;
4. indefinite principal pair: Schur retains at least 15 directions, in particular nonzero norm, and the hyperbolic/log-potential calculation gives `<251`.

All conditioning is on literal original coordinates. The largest normalized bound is below `10000`.

### Lines 750--770 — scaling, 33-direction corollary, threshold accounting

**PASS.** With `Y=KX`,

`Qtilde = Y^T(A/s)Y + (K/s)b^T Y +(K^2/s)c = (K^2/s)Q`.

Thus the normalized `10000` bound rescales exactly to `10000 K^2/s`. The 33-direction statement is an immediate stronger-hypothesis corollary. The threshold-accounting discussion accurately describes the proof, not an optimality theorem.

### Lines 771--790 — limitations and references

**PASS** for mathematical scope/limitations. The manuscript correctly disclaims optimal threshold, full QFORM, extra regularity, and hidden distributional assumptions. **UNCHECKED** only for exhaustive bibliographic priority/completeness; the proof is self-contained and does not depend on an unproved external theorem.

## Package/support-file audit

- `README.md`: **PASS**. It accurately identifies the 17-eigenvalue theorem and pinned source.
- `SOURCE_MANIFEST.json`: **PASS** for internal consistency and git-blob/source-commit data; raw-byte SHA-256 recomputation is `UNCHECKED` as noted above.
- `AUDIT.md`: **PASS as author self-audit metadata**, not treated as independent evidence.
- `proof_map.csv`: **PASS**. Every listed theorem/lemma range matches the actual source range and proof dependency.
- `verify.py`: **PASS by code audit**. It hashes source bytes, checks exact rational/algebraic constants and executes finite numerical diagnostics; it does not purport to prove the theorem.
- `checks.json`: **PASS as a record of the current checker output** and internally consistent with the script: source bytes/lines/hash, 534 exact interpolation seeds, 18 exact volume comparisons, 9 strict sampling cases, 240 numerical Schur-threshold cases, 30 graph-weight cases, and exact diagonal-dominance slack. **UNCHECKED** for an independent re-execution in this run.
- compiled PDF binary/hash/render: **UNCHECKED** because the package keeps the source as the mathematical release object and the binary is not present for byte-level inspection here.

## Downstream threshold status from this audit

The 17-eigenvalue baseline is secure enough to serve as a dependency. A complete nine-eigenvalue replacement with explicit constant `6010 K^2/s` is available in this worker's earlier immutable B17 improvement and has since received a genuinely separate complete PASS reconstruction in account02/B18. I independently rechecked its branch requirements during this run; the lowest complete full theorem I certify remains multiplicity **9**. Multiplicity 8 remains open and is addressed by the companion improvement/counterexample artifact for this run.

No statement here claims the unrestricted three-eigenvalue QFORM theorem.
