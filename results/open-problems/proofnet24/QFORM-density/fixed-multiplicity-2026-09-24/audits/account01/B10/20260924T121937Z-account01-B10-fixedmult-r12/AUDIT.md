# account01/B10 complete audit — QFORM-FIXED-MULTIPLICITY-AUDIT-20260924

Run: `20260924T121937Z-account01-B10-fixedmult-r12`  
Reviewer: `account01/B10`  
Lens: exact constants, rational slack, checker coverage, adversarial finite examples, singular seeds.  
Objective: `QFORM-FIXED-MULTIPLICITY-AUDIT-20260924`.

## Source pin and immediate verdict

Pinned baseline source commit: `7c0d6e60946b19423e6400a12d34b473cf0591e2`.  
Current `master` snapshot observed immediately before publication: `0e09d541a8749be0b70a595cb5abaa4ab7559b2d`.  
The manuscript blob on current `master` is unchanged from the baseline: `183ccd294763214e6a707e8d4749ff9a8cf7006d`.  
Advertised source SHA-256: `9f3bdec0b88debe9a66076c7b4a5cc894fb14e69b89591a4107e785340f65e69` (not independently recomputed in this connector-only run).

**Fatal mathematical gaps found: NONE.** I read all 790 lines of `manuscript.tex` and independently reconstructed every proof step used by the candidate theorem. My mathematical verdict is **PASS** for the theorem

`||p_(X^T A X+b^T X+c)||_infinity <= 10000 K^2/s` under `s_17(A)>=s>0`, arbitrary symmetric `A`, arbitrary affine terms, and arbitrary independent real coordinate densities bounded by `K`.

This is one worker's end-to-end review, not a self-awarded release certificate and not a solution of the unrestricted three-eigenvalue conjecture.

**Repository-package GAP (non-mathematical):** `README.md` and root `AUDIT.md` are present, but direct reads of `proof_map.csv`, `SOURCE_MANIFEST.json`, `verify.py`, and `checks.json` returned 404 on the current tree. Consequently the advertised finite diagnostic suite is **UNCHECKED / not reproducible from the root as delivered**. This does not create a proof dependency gap because the specialized mathematics is proved in `manuscript.tex`.

## End-to-end source audit

| Source lines / label | Status | Independent reasoning | Downstream impact / next obligation |
|---|---|---|---|
| 1–83: preamble, definitions, `thm:main`, `cor:33`, architecture | PASS | Quantifiers preserve arbitrary dimension, signature, remaining spectrum, affine `b,c`, and arbitrary independent density-cap laws. Zero padding makes `s_17` meaningful in every dimension. The theorem claims essential boundedness, not continuity. | Statement scope is coherent. |
| 84–151: Fourier convention, Gaussian regularization/inversion, power envelope, Riesz half-potential | PASS | With `hat f(t)=int exp(itx)f(x)dx`, Plancherel has factor `2 pi`, inversion `1/(2 pi)`, and Gaussian smoothing is normalized consistently. The envelope integral is `2ap/(p-1)`. The gamma/Gaussian computation gives `(2 pi)^(-1/2)` and the weighted `3/4` envelope integral is exactly `12 sqrt(u)`. | Fourier constants used later are consistent. |
| 152–220: singular-value perturbation, Schur spectral count, row diagonal dominance | PASS | Approximation numbers justify both nonsymmetric singular-value inequalities. For invertible `A`, `S^{-1}` is the complementary principal block of `A^{-1}`; positive and negative interlacing bound the absolute-value spectral count. The `A+epsilon I` argument correctly handles singular `A`. Strict row diagonal dominance requires no symmetry. | Schur and nonsymmetric rank steps are valid. |
| 221–300: geometric BL heat flow, projection density, scalar Fourier powers | PASS | The heat-flow sign is correct: `partial_t F-Delta F = F(sum c_i v_i^2-|sum c_i u_i v_i|^2)>=0` by the Parseval frame contraction. The large-time Gaussian limit uses `sum c_i=d`. Product projection is a deterministic integral change, not rotated probabilistic independence. The even-power Fourier argument uses independent differences and inversion at zero only after integrability gives a continuous version. | Analytic product-measure inputs close. |
| 301–400: decoupling, regularized crossing determinant, crossing volumes | PASS | The fourth-power inequality follows from Jensen after the first Cauchy–Schwarz decoupling. In the graph-BL step the `d_i^{-d_i/2}` factor cancels the scalar Fourier `sqrt(d_i)` factor, while `prod c_j^{-c_j/2}<=e^(theta/2)` upgrades `(2 pi sqrt(e))^theta` to `(2 pi e)^theta`; `alpha=(2 pi e)^2` cancels the residual multiplier exactly. Fourth roots give determinant exponent `-1/8`. Order five gives `|t|^{-5/4}` and order three is used only with the half-Riesz weight. | No hidden phase-decay assumption. |
| 401–500: scalar square, definite pair, hyperbolic pair | PASS | Scalar change of variables gives the exact inverse-square-root profile. The definite pair uses only a deterministic orthogonal parametrization of the integral. For the indefinite pair the hyperbolic Jacobian is `1/(2 sqrt D)`; the tail monotonicity cutoff `(3/4)log 2`, cap-one/mass-one bathtub bound, and `Lambda>=2/sqrt D` all have the stated direction. | Pair pivots are valid for rough laws without rotated independence. |
| 501–535: quarter-power concentration | PASS | If no diagonal is large, random signs extract a physical cross block with norm at least `L/4`. Retaining one singular factor in the determinant theorem gives the `|t|^{-1/4}` envelope; Gaussian smoothing yields the `rho^{1/4}` small-ball bound, then layer cake gives `L0=4+4 log 16`. | One surviving direction controls the logarithmic kernel. |
| 536–600: `V_r`, no-pivot entry bounds, `lem:sampling`, `lem:completion` | PASS | `|a_ij|<1/7` follows from `a_ij^2<eta^2+eta`. The bordered determinant identity is correct and sorting signs disappear after squaring. Singular deleted seeds can only reduce the count, hence the sampling estimate is an inequality. For `P=A[:,T]B^{-1}A[S,:]`, `P[S,:]=A[S,:]`, `P[:,T]=A[:,T]`; with the given `D,E,R`, `D` vanishes on `S union T`, `diag E=0`, `R[L,L]=P[L,L]`, `rank R<=3r`, `rank R[L,L]<=r`. | Most sensitive nonsymmetric support/rank claims pass. |
| 601–630: `prop:volume` | PASS | Bad ratio gives `epsilon<=(r+1)/80<=1/16`. With `m=4k-3` and `r<=k-1`, `m>=4r+1`; after global rank loss `3r`, at least `r+1` entries of `D` have modulus `>=1-epsilon`, all in `L`. On `H`, `|R_ii|>=371/400`; each off-diagonal is `<23/112`; for `r<=4` row sum `<23/28`. Exact slack is `371/400-23/28=297/2800>0`, contradicting `rank R[L,L]<=r`. The `r=0` case gives `||A||<1`. | Spectral-to-volume step is sound. |
| 631–660: random cut and no-pivot analytic consequences | PASS | Every ordered disjoint `k`-minor survives a fair cut with probability `4^{-k}`. Hence `Z_k^{-1/(2k)}<=160`. The resulting constants are `12 sqrt(80e)<200` for `k=3` and `800e<2400` for `k=5`. | Nine-direction full half-potential and seventeen-direction density branches close. |
| 661–730: truncated half-potential, kernel integrals, `prop:pivot-H` | PASS | `J(d)` is controlled by an exact near-region beta/hyperbolic integral plus a logarithmic far tail. The log-kernel bound is an interval-overlap rearrangement. Scalar pivot uses Schur + quarter-power; definite/indefinite pairs condition only original coordinates. The scalar bound is actually `200+120 log 16`, definite `<40 pi`, indefinite `<=10(32+4 log16)+4/e`. | Pivot truncated half-potential bound `<=600` is conservative. |
| 731–790: `prop:nine`, main theorem, scaling, limitations, bibliography | PASS mathematically; bibliography priority UNCHECKED | Pivot/no-pivot is exhaustive. A scalar main pivot leaves at least 16 Schur directions and only nine are needed; definite pair is immediate; indefinite pair leaves at least 15 but only one surviving direction is used. `Y=KX` has density cap one and `Q=(s/K^2) Qtilde`, giving the exact `K^2/s` scaling. | Candidate theorem closes. Comprehensive novelty/priority search not performed here. |

No mathematical source line in the 790-line manuscript remains UNCHECKED in this review. The only UNCHECKED items requested by the package are the absent root finite-check artifacts and comprehensive bibliographic priority.

## B10 exact arithmetic checks

The central rational inequalities are all strict with explicit slack:

- `sqrt(eta^2+eta)<1/7` because `eta^2+eta=101/10000<1/49`.
- At the worst sampled order `r=4`, `epsilon<=5/80=1/16`.
- Large residual diagonal: `1-1/16-1/100 = 371/400`.
- Single off-diagonal bound: `1/7+1/16 = 23/112`.
- Five-by-five contradiction row sum: `4*(23/112)=23/28`.
- Exact dominance slack: `371/400-23/28 = 297/2800 > 0`.
- The manuscript's crude comparisons `800e<2400`, `12 sqrt(80e)<200`, `10pi<40`, and `log16<3` are all more than sufficient.

A sharper constant is recorded in the improvement artifact for this run.

## Adversarial finite examples

### 1. Singular deleted seeds do not justify an equality in `lem:sampling`

Take the `2 x 2` cross block

`C=[[0,1],[1,0]]`.

Its determinant is `-1`, but among its four `1 x 1` row/column deletions two leave the zero entries. Thus a nonsingular `(r+1)` extension can have singular deleted `r`-seeds. This exactly supports the manuscript's `<= (r+1)^2` counting statement and rules out replacing it by an unconditional equality.

### 2. Simultaneous sharpness of the two interpolation rank bounds

With seed `S={1}`, `T={2}`, `L={3,4}`, let

```
A0=[[-3, 1,-3,-3],
    [ 1,-3,-3,-3],
    [-3,-3,10, 9],
    [-3,-3, 9, 9]].
```

Here `B=A0[S,T]=[1]`, the manuscript interpolation has `off(A0[L,L]-P[L,L])=0`, and the completion has `E=0`, `D=diag(0,0,1,0)`. Exact elimination gives

`det(A0)=144`, `rank(A0)=4`, `rank(R)=3`, `rank(R[L,L])=1`.

Direct sums of `r` copies simultaneously realize `rank(R)=3r`, `rank(R[L,L])=r`, and `rank(D+R)=4r`. This is not a no-pivot counterexample, but it proves that the terminal `17 -> 16` failure cannot be repaired by merely tightening the two rank inequalities.

### 3. Singular Schur boundary diagnostic

For `A=diag(1,-1,0)` with the first coordinate as the scalar pivot and threshold `t=1`, the Schur complement is `diag(-1,0)`. Thus `N_A(1)=2` and `N_S(1)=1=N_A(1)-1` even though `A` is singular; the manuscript's perturbative extension of the invertible argument has the correct boundary behavior.

These diagnostics are finite checks, not proofs. The proofs above were audited independently of them.

## Review status

- 17-eigenvalue candidate: **PASS in this complete account01/B10 review**.
- Mathematical FALSE statements found: **none**.
- Mathematical GAPs found: **none**.
- Package/reproducibility: **GAP** because four advertised root artifacts are absent.
- Full three-eigenvalue conjecture: **OPEN / not addressed by this fixed-multiplicity theorem**.
- Independent-validation status: **not self-awarded here**; release synthesis must apply the owner's separate-review rule.
- Repository transport is not native learned-memory ingestion: `WITHOUT_VERIFIED_BRAIN`.

No task identity, schedule, cadence, enabled/paused state, email/push notification, account authentication, permission, visibility, paid-call setting, public-release state, or remote workflow was changed.