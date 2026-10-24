# account01/B20 independent release-gate audit — fixed multiplicity 17

Run: `20260924T122111Z-account01-B20-fixed-multiplicity-audit-r1`

Objective: `QFORM-FIXED-MULTIPLICITY-AUDIT-20260924`.

Pinned mathematical source: `yspennstate/math-open-problems@7c0d6e60946b19423e6400a12d34b473cf0591e2`, `proofnet24/QFORM-density/fixed-multiplicity-2026-09-24/manuscript.tex`, git blob `183ccd294763214e6a707e8d4749ff9a8cf7006d`, owner-recorded SHA-256 `9f3bdec0b88debe9a66076c7b4a5cc894fb14e69b89591a4107e785340f65e69`.

## Release-gate verdict

**Mathematical verdict on the pinned 17-eigenvalue theorem: PASS in this independent B20 reconstruction.** I read the complete 790-line source end-to-end and re-derived the specialized analytic and algebraic chain. I found no fatal mathematical gap in the statement

\[
 s_{17}(A)\ge s>0
 \quad\Longrightarrow\quad
 \|p_{X^TAX+b^TX+c}\|_\infty\le 10^4 K^2/s
\]

for arbitrary independent real coordinate densities `0<=f_i<=K`, arbitrary real symmetric `A`, and arbitrary affine `b,c`.

This is one independent mathematical review, not formal verification, journal peer review, or a proof of the unrestricted three-eigenvalue conjecture. Global continuity is not part of the theorem; the no-pivot Fourier branch is continuous, while the pivot branches are proved by measure domination/essential-density bounds.

**Repository/package verdict: GAP.** On fresh master, `proof_map.csv`, `SOURCE_MANIFEST.json`, `verify.py`, and `checks.json` advertised by `README.md` were absent (direct fetches returned 404). I therefore did not count the advertised finite checks as reproduced evidence. The proof itself is self-contained in `manuscript.tex`.

**Presentation repairs, theorem unaffected:** (i) choose once and for all Borel versions of every marginal density clipped pointwise into `[0,K]`; this removes any ambiguity when rough densities are evaluated on inverse branches or level-curve parametrizations; (ii) in the product-projection proof, after dropping rows with `b_i=0`, read the entropy line as `sum_{b_i>0}(1-b_i)<=d`, or retain the sum over all rows and keep equality. Neither change alters a constant or downstream claim.

## End-to-end ledger

### Lines 41–100 — theorem, quantifiers, scaling, architecture: PASS

The normalized reduction `Y=KX`, `A -> A/s` gives `Q=(s/K^2) Qtilde`, hence the density factor `K^2/s`. No Gaussianity, moments, iid, support, log-concavity, sign restriction, or post-rotation independence is introduced. The two algebraic orders are correctly separated: order three feeds a negative-half potential and order five feeds direct Fourier inversion.

### Lines 90–170 — Fourier normalization, inversion, envelopes, Riesz half potential: PASS

With `fhat(t)=int exp(itx)f(x)dx`, Plancherel has constant `2*pi`, inversion has `1/(2*pi)`, and the Gaussian identity has `1/(2 sqrt(pi v))`. The power-envelope integral is `2ap/(p-1)`. The gamma/Gaussian computation gives

\[
E|Z-a|^{-1/2}\le (2\pi)^{-1/2}\int |t|^{-1/2}|\phi_Z(t)|dt,
\]

and a `3/4` envelope contributes the exact weighted integral `12 sqrt(u)`.

### Lines 160–220 — singular values, rank perturbation, Schur spectral counts: PASS

The approximation-number proof applies to nonsymmetric auxiliaries. In the invertible Schur case, `S^{-1}` is the complementary principal block of `A^{-1}`; positive and negative interlacing separately imply the absolute-value count. For singular `A`, the `A+epsilon I` argument at threshold `t-|epsilon|` passes to the limit by continuity of ordered eigenvalue moduli. Strict diagonal dominance is valid without symmetry.

### Lines 220–305 — geometric Brascamp–Lieb and product projections: PASS with local wording repair

The heat-flow identity

`partial_t F-Delta F = F(sum c_i v_i^2-|sum c_i u_i v_i|^2)>=0`

follows from the frame contraction. The large-time limit uses `sum c_i=d`; the small-time passage uses Lebesgue points/Fatou and monotone truncation. In the projection lemma, zero-complement-weight rows may be dropped after choosing pointwise-bounded density representatives. The entropy estimate is valid with `sum_{b_i>0}(1-b_i)<=d`; this is the only wording repair needed there. The scalar projection constant `sqrt(e)/|a|` follows by scaling.

### Lines 285–400 — scalar Fourier powers, decoupling, graph determinant, crossing volumes: PASS

For `p>=2`, `m=floor(p/2)>=p/4` and `|fhat|<=1` reduce to an integrable even power. Fourier inversion at zero plus the product-projection lemma gives `2*pi*sqrt(2e)/sqrt(p)`. In the decoupling step,

`|phi|^2<=E G` and `(E G)^2<=E G^2`

give the displayed fourth-power bound without introducing a conjugate-sum independence claim.

For the regularized determinant, the `c_j,d_i` vectors form an exact frame, `theta=sum d_i=sum(1-c_j)`, the `d_i` powers cancel the one-dimensional Jacobians, and `alpha=(2*pi*e)^2` cancels the entropy factor. Since `a=2t`, the final matrix is `I+t^2 M^TM/(pi^2 e^2)` and taking fourth roots yields exponent `-1/8`. Cauchy–Binet then gives exponent `k/4`; order five is integrable and order three is used only after the Riesz weight.

### Lines 401–526 — square, definite pair, hyperbolic pair, quarter concentration: PASS

The scalar-square formula is conditional measure domination. The definite-pair calculation rotates only a deterministic two-dimensional integral and never the random product law. In the hyperbolic proof the `(delta,t)` Jacobian is `1/(2 sqrt(D))`; each tail is controlled using one original marginal with cap one and mass one, while the middle interval contributes the logarithm. The arithmetic `Lambda>=2/sqrt(D)` gives the stated envelope. A global bounded representative convention is the clean presentation repair for rough marginals.

The quarter-concentration sign split satisfies `E C_epsilon=O/2`; convexity exposes an original-coordinate crossing of norm at least `L/4`. Retaining one singular factor in the determinant theorem gives the `|t|^{-1/4}` majorant and Gaussian smoothing gives the stated `rho^{1/4}` bound. This is not the false uniform pointwise decay claim for an arbitrary single rough quadratic phase.

### Lines 527–651 — disjoint minors, nonsymmetric interpolation, completion, spectral-to-volume: PASS

The bordered determinant identity is exact; singular deleted seeds can only reduce the sampling count, hence the direction is correctly an inequality. For

`P=A[:,T] A[S,T]^{-1} A[S,:]`,

`rank P<=r`, rows `S` and columns `T` interpolate exactly. In `A=D+R+E`, `E` is supported in `LxL` with zero diagonal, `D` is diagonal and vanishes on `S union T`, `R[L,L]=P[L,L]` has rank at most `r`, and globally `R-P` is supported in rows `T` or columns `S`, hence `rank R<=3r`.

If `V_k<kappa^k`, a ratio drop occurs. For `r=0`, `||A||<eta+sqrt(kappa)<1`. For `1<=r<=4`, `||E||_F<=1/16`; `m=4k-3>=4r+1` and rank perturbation force at least `r+1` large entries of `D`, all in `L`. On those indices,

`|R_ii|>=371/400`, while each off-diagonal is `<1/7+1/16`,

so the row sum is `<23/28<371/400`. The resulting `(r+1)` block is invertible, contradicting `rank R[L,L]<=r`. The random physical cut counts each ordered disjoint `k`-minor with probability exactly `4^{-k}`.

### Lines 652–760 — kernels, pivot half potentials, nine-direction theorem, main theorem: PASS

The singular-kernel and logarithmic-kernel bounds are Tonelli-safe. At a scalar pivot, the Schur remainder keeps a large spectral direction, so the quarter-concentration logarithmic potential removes the conditional square-root singularity. Definite and indefinite pairs are averaged through conditional measure domination. The truncated potential `H` is kept distinct from the full half potential; under `s_9>=1`, the outside part costs at most one, giving `601`.

The final branches close with the displayed constants: no pivot `<2400`; scalar pivot `6010`; definite pair `<40`; indefinite pair `<251`. Scalar and pair Schur complements lose exactly one or two spectral directions, respectively, and arbitrary induced affine terms are allowed.

### Lines 761–790 — scope: PASS

The manuscript correctly states that it does not solve the `s_3` conjecture and does not prove optimality of 17. It also correctly separates the continuous no-pivot branch from the global essential-density conclusion.

## Threshold accounting after the audit

No lower multiplicity theorem is certified in this run. The present proof architecture needs order-five crossing volume for absolute Fourier inversion; order four gives the endpoint `|t|^{-1}` decay. I did, however, prove a new exact localization of the entire `s_16` no-pivot obstruction, saved separately as `S16_ENDPOINT.md`. It shows that every unpaid `s_16` no-pivot state has a physical crossing which is within Frobenius `1/64` of rank four, retains quantitative order-four volume, and simultaneously forces at least eight near-unit same-bank singular directions plus a second large physical crossing. The only remaining issue is alignment/transversality between these two physical resources. This is a genuine reduction of the next threshold obstruction, not a proof of the 16-eigenvalue theorem.

## Status summary

- 17-eigenvalue mathematical theorem: **PASS in this B20 independent reconstruction**.
- Full three-eigenvalue conjecture: **OPEN**.
- Global continuity: **not claimed**; no-pivot branch is continuous.
- Missing root supplementary files: **GAP (packaging/reproducibility)**.
- Density representative convention: **GAP-PRESENTATION / trivial repair**.
- Product-projection zero-weight sum wording: **GAP-PRESENTATION / trivial repair**.
- Certified threshold below 17: **none yet**.
