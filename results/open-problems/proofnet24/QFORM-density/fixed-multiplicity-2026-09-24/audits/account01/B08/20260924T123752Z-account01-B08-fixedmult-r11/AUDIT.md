# account01/B08 complete fixed-multiplicity audit — QFORM-FIXED-MULTIPLICITY-AUDIT-20260924

Run: `20260924T123752Z-account01-B08-fixedmult-r11`  
Reviewer: `account01/B08`  
Starting lens: nonsymmetric interpolation `P`, support of `R-P`, global versus restricted rank, and the seed/diagonal structure.  
Execution context: `WITHOUT_VERIFIED_BRAIN`.

## Source pin and verdict

Baseline source commit: `7c0d6e60946b19423e6400a12d34b473cf0591e2`.  
Fresh `master` snapshot observed immediately before this review write: `b5e04c2f5c0c856ed72190e7554a93650a1a22f3`.  
Current manuscript blob read back from `master`: `183ccd294763214e6a707e8d4749ff9a8cf7006d`, unchanged from the baseline.  
Advertised source SHA-256 in the owner objective/README: `9f3bdec0b88debe9a66076c7b4a5cc894fb14e69b89591a4107e785340f65e69` (not independently recomputed in this connector-only run).

**Mathematical verdict: PASS for the complete written 17-eigenvalue candidate.** I read all 790 source lines of `manuscript.tex` in this invocation and independently reconstructed every proof block used in the theorem

` s_17(A) >= s > 0  =>  ||p_(X^T A X + b^T X + c)||_infinity <= 10000 K^2/s `

for arbitrary real symmetric `A`, arbitrary independent real coordinate densities bounded by `K`, arbitrary signs/remaining spectrum, and arbitrary affine `b,c`. I found no fatal mathematical gap.

This is one worker's complete review. It is not a self-awarded release certificate, and it does not prove or claim the unrestricted three-eigenvalue conjecture.

**Package/reproducibility GAP:** direct reads of root `SOURCE_MANIFEST.json`, `proof_map.csv`, `verify.py`, and `checks.json` returned 404 on fresh `master`; `proof_map.csv` also returned 404 at the baseline commit. README/AUDIT describe these files as present. Therefore those supplementary artifacts and the advertised finite-test results are **UNCHECKED / presently unreproducible from the stated root**. This does not create a theorem-proof dependency because all specialized mathematics used by the theorem is contained in `manuscript.tex`.

## End-to-end line audit

| Source lines / statement | Status | Independent reconstruction / check | Downstream impact |
|---|---|---|---|
| 1–83: definitions, `thm:main`, `cor:33`, architecture | **PASS** | Singular values are zero-padded; for symmetric `A` they are eigenvalue moduli. Quantifiers preserve arbitrary dimension, signature, remaining spectrum, rough product laws and affine terms. The conclusion is essential boundedness, not global continuity. | The claimed scope is coherent. |
| 84–151: Fourier convention, Gaussian inversion, `lem:envelope`, `lem:riesz` | **PASS** | With `hat f(t)=int e^{itx}f(x)dx`, Plancherel carries `2 pi` and inversion `1/(2 pi)`. Gaussian smoothing constants agree. The power-envelope integral is `2ap/(p-1)`. The gamma/Gaussian calculation gives the Riesz prefactor `1/sqrt(2 pi)` and the weighted `3/4` envelope integral is exactly `12 sqrt(u)`. | Constants and normalization used later are consistent. |
| 152–220: `lem:rank`, `lem:schur`, `lem:dd` | **PASS** | Approximation numbers give both nonsymmetric singular-value inequalities. For invertible `A`, `S^{-1}` is the complementary principal block of `A^{-1}`; applying compression interlacing separately to `A^{-1}` and `-A^{-1}` proves the absolute-value count. The `A+epsilon I` limiting argument handles singular `A`. Strict row diagonal dominance needs no symmetry. | Spectral-count and nonsymmetric-rank steps are valid. |
| 221–300: `thm:bl`, `lem:projection`, `lem:scalar-fourier` | **PASS** | The heat-flow identity has the correct sign by the Parseval-frame contraction; the large-time Gaussian limit uses `sum c_i=d`, and the rough-law endpoint follows by Fatou then monotone truncation. Product projection is a deterministic integration change only, not rotated probabilistic independence. For scalar Fourier powers, `m=floor(p/2)>=p/4`; independent differences plus the projection density and continuous Fourier-inversion representative give the stated constant. | Rough product-measure analytic inputs close. |
| 301–400: `lem:decoupling`, `thm:determinant`, crossing volumes | **PASS** | First Cauchy–Schwarz and an independent copy give the square bound; Jensen gives the fourth-power bound. In the graph-BL calculation, the `d_i^{-d_i/2}` factor cancels the scalar Fourier `sqrt(d_i)` contribution, `prod c_j^{-c_j/2}<=e^{theta/2}`, and `alpha=(2 pi e)^2` cancels the remaining multiplier. Taking fourth roots gives determinant exponent `-1/8`. Cauchy–Binet yields `Z_k`; order five gives `|t|^{-5/4}`, while order three is used only with the half-Riesz weight. | No forbidden pointwise van-der-Corput premise is used. |
| 401–500: `lem:square`, `lem:definite`, `lem:hyperbola`, start of `lem:quarter` | **PASS** | Scalar inverse branches and the interval-preimage estimate are correct. The definite pair diagonalizes only the deterministic two-dimensional integral and has Jacobian `1/(2 sqrt(det B))`. In the indefinite pair, the hyperbolic Jacobian is `1/(2 sqrt(D))`; the tail monotonicity cutoff, cap-one/mass-one rearrangement and `Lambda>=2/sqrt(D)` have the stated directions. | Pivot envelopes remain valid for rough laws without rotated independence. |
| 501–535: completion of `lem:quarter` | **PASS** | If no diagonal carries `L/2`, random signs extract a physical cross block of norm at least `L/4`. Retaining its largest singular factor in the proved determinant theorem gives a `|t|^{-1/4}` envelope; Gaussian smoothing yields the quarter-power small-ball bound, then layer cake gives `L_0=4+4 log 16`. | One surviving spectral direction controls the logarithmic kernel. |
| 536–565: `def:pivot-volume`, no-pivot entry bound, `lem:sampling` | **PASS** | `|a_ij|<1/7` follows from `eta^2+eta<1/49`. For a seed `(S,T)`, the bordered determinant identity is exact; sorting signs disappear after squaring. Sampling only nonsingular seeds can lose extensions, so the aggregate is correctly an inequality rather than equality. `P=A[:,T]B^{-1}A[S,:]` has rank at most `r`, with `P[S,:]=A[S,:]` and `P[:,T]=A[:,T]`. | Ordered-minor sampling is sound. |
| 566–600: `lem:completion` — B08 primary lens | **PASS** | With `E[L,L]=off(A[L,L]-P[L,L])`, `E` has zero diagonal. `D_ii=A_ii-P_ii` on `L` and `D=0` on `S union T`. Thus `R[L,L]=P[L,L]`, so `rank R[L,L]<=r`. Moreover `R-P` vanishes on rows `S`, columns `T`, and all of `L x L`; hence every possible nonzero lies in rows `T` or columns `S`. Splitting these two supports gives two rank-`<=r` pieces, so `rank R<=rank P+2r<=3r`. No symmetry of `P,R,E` is needed. | The manuscript's most sensitive support/rank claim passes. |
| 601–630: `prop:volume` | **PASS** | Bad ratio gives `epsilon<=(r+1)/80<=1/16`. With `m=4k-3` and `r<=k-1`, `m>=4r+1`. Global rank loss `3r` forces at least `r+1` entries of `D` of modulus `>=1-epsilon`; because `D` vanishes on the seed, they all lie in `L`. On `H`, `|R_ii|>=371/400` and each off-diagonal is `<23/112`; for `r<=4` the row sum is `<23/28<371/400`. Strict diagonal dominance contradicts `rank R[L,L]<=r`. The `r=0` branch gives `||A||<1`. | Spectral-to-volume conversion is valid. |
| 631–660: `lem:cut`, `cor:no-pivot` | **PASS** | Every ordered disjoint `k`-minor survives a fair cut with probability `4^{-k}`. Thus `Z_k^{-1/(2k)}<=160`; order three gives `12 sqrt(80e)<200`, order five gives `800e<2400`. | Nine-direction half potential and seventeen-direction no-pivot density close. |
| 661–730: `lem:kernels`, `prop:pivot-H` | **PASS** | The near part of `J(d)` is bounded by the explicit beta/hyperbolic integral, the far part by a logarithm. The log-kernel estimate follows by interval-overlap rearrangement. Scalar pivot uses Schur plus quarter-power; definite and indefinite pairs condition only on original coordinates. Tonelli/test-function formulations remove exceptional-slice ambiguity. | Pivot truncated half-potential estimate closes. |
| 731–790: `prop:nine`, proof of `thm:main`, scaling, limitations, bibliography | **PASS mathematically; priority search UNCHECKED** | Pivot/no-pivot is exhaustive. Scalar main pivot leaves at least 16 Schur directions, of which nine suffice; definite pair is immediate; indefinite pair leaves at least 15 and needs only one surviving direction. For general `K,s`, `Y=KX` has density cap one and `Q=(s/K^2) tilde Q`, giving exactly `K^2/s` scaling. The manuscript correctly distinguishes continuous no-pivot density from merely essentially bounded pivot branches. | Candidate theorem closes. Comprehensive novelty/priority verification was not part of this run. |

No mathematical source line in the 790-line manuscript remains UNCHECKED in this review. The UNCHECKED items are the missing supplementary package files/finite diagnostics and comprehensive bibliographic priority, neither of which is used as a theorem premise.

## B08 independent reconstruction of the interpolation ranks

Write the seed-coordinate blocks in the order `S,T,L` as

```
A = [ C    B    G
      B^T  F    H
      G^T  H^T  J ],       B=A[S,T] invertible.
```

Then

```
P=A[:,T] B^{-1} A[S,:]
```

has

```
P[L,L]=H^T B^{-1}G,
P[S,:]=A[S,:],
P[:,T]=A[:,T].
```

The completion in the manuscript therefore has the exact block form

```
R = [ C    B    G
      B^T  F    H
      G^T  H^T  H^T B^{-1}G ].
```

After merely permuting the columns to the order `T,S,L`, the leading `S x T` block is the invertible matrix `B`. Exact block elimination gives the stronger normal-form identity

```
rank R = r + rank K,

K = [ B^T-FB^{-1}C      H-FB^{-1}G
      G^T-H^TB^{-1}C    0             ].
```

Since the top block row of `K` has at most `r` rows and the left block column has at most `r` columns, `rank K<=2r`; hence `rank R<=3r`. Separately `R[L,L]=H^TB^{-1}G` gives the sharper restricted bound `rank R[L,L]<=r`. This derivation verifies both manuscript bounds without using symmetry of `R`.

## Rank sharpness / obstruction to a bookkeeping-only threshold reduction

The coefficient `3r` is genuinely attainable even inside the local no-pivot entry class. For any `r>=1`, take the direct sum of `r` copies of

```
delta * [0 1 1
         1 0 1
         1 1 1],      delta=1/200,
```

and in each copy take the first coordinate in `S`, the second in `T`, and the third in `L`. Then `B=delta I_r`, `C=F=0`, `G=H=delta I_r`, and `J=delta I_r=P[L,L]`. Hence `D=E=0`, `R=A`,

```
rank R = 3r,          rank R[L,L]=r.
```

All diagonal entries have modulus `<eta=1/100`; every principal `2 x 2` determinant has modulus at most `delta^2=1/40000<eta`, so there is no `eta`-pivot. Thus neither `rank R<=3r` nor `rank R[L,L]<=r` can be improved from support bookkeeping alone. This witness is deliberately small-scale and is **not** a counterexample to the theorem's large-singular-value hypothesis.

For `r=1`, the normal form displays the two independent interpolation defects explicitly. With scalar blocks `b,c,f,g,h`,

```
det R = ((b g-c h)(b h-f g))/b.
```

Both factors can be nonzero, explaining why the global third rank is real rather than an artifact of a loose subadditivity estimate.

## Threshold-lowering audit

The present pipeline cannot be lowered to 13 merely by replacing order five with order four. Under the same spectral-to-volume mechanism, `k=4` would require `4k-3=13` large directions, but the determinant theorem gives only

```
|phi_Q(t)| <= min(1, u/|t|)
```

at order four. The absolute Fourier integral diverges logarithmically, so the manuscript's `L^1` inversion argument does not produce an `L^infinity` density. Higher even-power decoupling does not automatically repair this: the graph-BL step would require scalar Fourier integrability below exponent two when a leverage weight exceeds `1/2`, which is unavailable uniformly for arbitrary cap-one rough densities.

Accordingly **no lower multiplicity than 17 is claimed in this run**. A rigorous reduction needs a genuinely new order-four endpoint receiver, or an additional structural bridge that turns the same-index interpolation defects in the displayed `K` into extra disjoint crossing volume. The rank-sharpness witness above shows that a purely formal replacement of `3r` by `2r` is invalid.

## Additional rigorous improvement: final constant

The existing proof already gives a strictly better theorem constant without changing any assumption or threshold. In the scalar-pivot half-potential branch,

```
L0 = 4 + 4 log 16,
H(Q) <= 10(8+3 L0) = 200 + 120 log 16.
```

Adding the outside-tail contribution `<=1` in `prop:nine` gives

```
sup_a E|Q-a|^{-1/2} <= 201 + 120 log 16.
```

The main scalar pivot multiplies this by `eta^{-1/2}=10`, so

```
||p_Q||_infinity <= (2010 + 1200 log 16) K^2/s
                  = 5337.106466... K^2/s
                  < 5338 K^2/s.
```

All other branches in the manuscript are below `2400 K^2/s`. Thus the same proof supports the stronger constant `5338` in place of `10000`. This is a constant improvement only, not a multiplicity reduction.

## Remaining obligations

1. Restore or accurately relocate the four supplementary package files named by README/AUDIT if reproducible finite diagnostics are intended to ship with this root.
2. For multiplicity `<17`, attack the order-four endpoint or extract quantitative control of the two defect blocks `H-FB^{-1}G` and `G^T-H^TB^{-1}C` beyond support/rank bookkeeping.
3. Keep independent-review status separate from this worker's verdict; two genuinely separate complete reviews remain the release gate required by the owner objective.
