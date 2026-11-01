# Independent end-to-end audit — fleet01/B16 — 20260924T130832Z-r11

Objective: `QFORM-FIXED-MULTIPLICITY-AUDIT-20260924`.

## Source pin and independence

I reconstructed the proof from `manuscript.tex` before using any peer verdict. The source fetched from current `master` has git blob
`183ccd294763214e6a707e8d4749ff9a8cf7006d`, exactly the blob recorded for baseline commit
`7c0d6e60946b19423e6400a12d34b473cf0591e2`; fetching the baseline commit directly returned the same blob. The recorded SHA-256 is
`9f3bdec0b88debe9a66076c7b4a5cc894fb14e69b89591a4107e785340f65e69`, 47883 bytes, 790 lines. Thus this review is of the pinned baseline mathematical source, not a later modified manuscript.

Materials read in full: `README.md`, `SOURCE_MANIFEST.json`, `AUDIT.md`, `proof_map.csv`, `verify.py`, `checks.json`, and all 790 lines of `manuscript.tex`. I independently re-derived the proof chain and numerical constants rather than accepting the author self-audit as evidence.

## Overall verdict

**PASS for the written 17-eigenvalue theorem.** I found no fatal mathematical gap in the baseline theorem

\[
 s_{17}(A)\ge s>0,\quad \|f_i\|_\infty\le K
 \quad\Longrightarrow\quad
 \|p_{X^TAX+b^TX+c}\|_\infty\le 10^4 K^2/s.
\]

This is one independent audit, not the two-review release gate. It does **not** validate the unrestricted three-eigenvalue conjecture and does **not** prove that 17 is optimal.

Continuity is correctly kept separate: the no-pivot branch has an integrable characteristic function and hence a continuous density; the pivot branches prove only absolute continuity plus an essential `L^infinity` bound. The manuscript makes no stronger global continuity claim.

## End-to-end reconstruction

### 1. Normalization and theorem quantifiers

Lines 47–61: **PASS.** The theorem quantifies arbitrary dimension, independent real coordinates with density caps `K`, arbitrary real symmetric `A`, arbitrary affine `b,c`, and uses singular values with zeros appended. The scaling at lines 742–748 is exact: with `Y=KX`,
\[
 \widetilde Q=Y^T(A/s)Y+(K/s)b^TY+(K^2/s)c,
 \qquad Q=(s/K^2)\widetilde Q,
\]
so the normalized density bound scales to `10000 K^2/s`. The 33-eigenvalue corollary follows from `s_17>=s_33`.

### 2. Fourier and negative-half-moment preliminaries

Lines 81–120 (`lem:fourier`): **PASS.** The heat-kernel proof of Plancherel uses an `L^2` approximate identity and monotone convergence. The `L^1` characteristic-function inversion is proved via Gaussian regularization and weak convergence. The Gaussian identity has the correct normalization.

Lines 122–130 (`lem:envelope`): **PASS.** The envelope integral is
`2a+2a^p*a^(1-p)/(p-1)=2ap/(p-1)`, giving `ap/(pi(p-1))` after Fourier inversion.

Lines 132–160 (`lem:riesz`): **PASS.** The gamma representation is correct; after Gaussian inversion the inner integral equals
`sqrt(2) Gamma(1/4)|t|^{-1/2}`, leaving coefficient `1/sqrt(2pi)`. For the `3/4` envelope the weighted integral is exactly `12 sqrt(u)`.

### 3. Spectral algebra

Lines 169–181 (`lem:rank`): **PASS.** Both singular-value perturbation and the rank-shift inequality follow from the best low-rank approximation formula and do not require symmetry.

Lines 183–207 (`lem:schur`): **PASS.** For invertible `A`, the complementary principal block of `A^{-1}` is `S^{-1}`. Positive and negative compression/interlacing applied to `A^{-1}` gives
`N_S(t)>=N_A(t)-k`. The singular case is legitimately obtained from `A+epsilon I`: the principal pivot remains invertible for small epsilon, the Schur complement converges, and `N_{A+epsilon I}(t-|epsilon|)>=N_A(t)`.

Lines 209–217 (`lem:dd`): **PASS.** Standard maximum-coordinate proof; nonsymmetry is harmless.

### 4. Geometric Brascamp–Lieb and projection density

Lines 221–255 (`thm:bl`): **PASS.** For heat evolutions `f_i`, differentiation gives
\[
 \partial_tF-\Delta F
 =F\left(\sum_i c_i v_i^2-\left|\sum_i c_i u_i v_i\right|^2\right)\ge0,
\]
because the matrix with columns `sqrt(c_i)u_i` is a contraction. The large-time limit has the right Gaussian factor because `sum c_i=d` and `sum c_i(u_i dot z)^2=|z|^2`. The rough-function limit uses Lebesgue points, Fatou, and monotone truncation correctly.

Lines 258–282 (`lem:projection`): **PASS.** The orthogonal-complement rows satisfy
`sum b_i v_i v_i^T=I`, `b_i=1-|U^Te_i|^2`. Applying the previous theorem to `f_i^(1/b_i)` is legitimate because `0<=f_i<=1`. The entropy bound
`-b log b<=1-b` yields `exp(d/2)`. The scalar rescaling gives `sqrt(e)/|a|`.

Lines 284–301 (`lem:scalar-fourier`): **PASS, with one implicit one-line justification.** For `m=floor(p/2)`, `|hat f|^p<=|hat f|^(2m)`. The latter is integrable because `|hat f|<=1` and `|hat f|^(2m)<=|hat f|^2`, while Plancherel already gives `hat f in L^2`. This justifies the manuscript sentence “It is integrable”; inversion at zero is then valid. Projection of the `2m` independent signed coordinates gives the stated constant.

### 5. Decoupling and regularized determinant

Lines 310–324 (`lem:decoupling`): **PASS.** Conditioning first on one original-coordinate bank, Cauchy–Schwarz, an independent copy, and then integration over the other product bank give the exact product of scalar Fourier transforms. Jensen gives the fourth-power form. The difference coordinates remain independent and have densities capped by one.

Lines 326–373 (`thm:determinant`): **PASS.** With
`H=alpha I+a^2M^TM`, `alpha=(2pi e)^2`, the vectors
`sqrt(alpha)H^{-1/2}e_j` and `aH^{-1/2}m_i` form a Parseval frame. Their squared norms are `c_j,d_i in [0,1]` and
`theta=sum d_i=sum(1-c_j)`. After `x=H^{-1/2}z`, geometric Brascamp–Lieb gives the displayed graph product. The scalar Fourier bound contributes `(2pi sqrt(e d_i))^{d_i}`; the `d_i` powers cancel the frame Jacobian, while `prod c_j^{-c_j/2}<=e^{theta/2}`. The choice of `alpha` cancels the remaining entropy factor exactly. Taking fourth roots yields
\[
 |\phi_Z(t)|\le\det\!\left(I+\frac{t^2}{\pi^2e^2}M^TM\right)^{-1/8}.
\]
No rank, leverage, or signature hypothesis is smuggled in.

Lines 375–400 (`Z_k`, determinant expansion, `cor:vol-fourier`): **PASS.** Cauchy–Binet gives the coefficient identity. Keeping the order-`k` term gives exponent `k/4`; for `k=5` Fourier inversion is integrable and gives `5e Z_5^{-1/10}`; for `k=3` the negative-half-moment lemma gives `12 sqrt((e/2)Z_3^{-1/6})`.

### 6. Coordinate pivots

Lines 404–420 (`lem:square` and profile): **PASS.** The two inverse branches give the correct square-root profile. The inverse image of an output interval of length `2rho` has length at most `2sqrt(2rho/|a|)`. Conditional completion of the square produces the Schur complement, and the stated domination is a Tonelli measure-domination statement, not an independence claim.

Lines 423–434 (`lem:definite`): **PASS.** Translation and deterministic orthogonal diagonalization preserve the joint density cap. Elliptic polar coordinates have Jacobian `1/(2sqrt(|det B|))`, yielding `pi M/sqrt(|det B|)`.

Lines 437–482 (`lem:hyperbola`): **PASS.** The hyperbolic parametrization has Jacobian `1/(2sqrt D)`. On each tail one original coordinate is monotone with `|y'|>=|y|/3`; using only its one-dimensional density cap and mass gives a tail integral at most `3 log2`. The middle interval has length bounded by `3/2 log2+log_+(32/(delta Lambda))`. Since `Lambda>=2/sqrt D`, the final envelope is exactly of the stated form. The critical level is null and the proof can be interpreted through nonnegative test functions, so rough representatives do not create an exceptional-slice gap.

Lines 485–525 (`lem:quarter`): **PASS.** A large diagonal entry gives the square-root small-ball bound. Otherwise sign randomization isolates a bipartite cross block with operator norm at least `L/4`; retaining its top singular value in the determinant theorem gives a `|t|^{-1/4}` characteristic-function envelope. Gaussian smoothing with `v=1/8` gives coefficient
`3.99525936158...<16`. Layer cake then yields `L_0=4+4log16`.

### 7. Disjoint-minor interpolation skeleton

Lines 528–543 (`def:pivot-volume` and small-entry bound): **PASS.** With no pivot, `|a_ii|<eta` and
`a_ij^2<eta^2+eta<1/49`, hence `|a_ij|<1/7`.

Lines 545–564 (`lem:sampling`): **PASS.** Volume sampling is normalized by `V_r`. For a nonsingular seed, the bordered determinant identity is exact. Squaring removes ordering signs. Each ordered disjoint `(r+1)`-minor is generated at most `(r+1)^2` times; singular seeds can have nonsingular extensions, so the correct relation is an inequality. This proves the Frobenius residual bound. `P` is genuinely allowed to be nonsymmetric.

Lines 566–580 (`lem:completion`): **PASS.** `E` is the off-diagonal residual on `LxL`; `D` is the diagonal residual on `L` and vanishes on the seed. Thus `R_LL=P_LL`. The support of `R-P` is confined to rows `T` or columns `S`, so it is the sum of two rank-`r` matrices; with `rank P<=r`, `rank R<=3r`, while the restricted block still has rank at most `r`.

Lines 582–619 (`prop:volume`): **PASS.** Failure of the order-`k` volume bound gives some ratio `V_{r+1}/V_r<kappa`. For `r=0`, `||A||<eta+sqrt(kappa)<1`, contradiction. For `1<=r<=4`, the completion has
`||E||<=||E||_F<=(r+1)sqrt(kappa)<=1/16`. If `m=4k-3`, singular-value perturbation and `rank R<=3r` force at least `m-3r>=r+1` diagonal entries of `D` of size at least `1-epsilon`; they lie in `L`. On these indices `R` has diagonal at least `371/400` and each off-diagonal at most `1/7+1/16`, so the row off-sum is at most `23/28<371/400`. Hence an `(r+1)x(r+1)` subblock of `R_LL` is invertible, contradicting `rank R_LL<=r`. This is the crucial 17-direction step and it is valid for nonsymmetric auxiliaries because only singular values/ranks are used.

Lines 621–630 (`lem:cut`): **PASS.** Each ordered disjoint minor survives the fair cut with probability `4^{-k}`.

Lines 632–645 (`cor:no-pivot`): **PASS.** The cut gives `Z_k^{-1/(2k)}<=160`. For `k=3`, the full half-potential bound is `12 sqrt(80e)=176.959...<200`; for `k=5`, the density bound is `800e=2174.625...<2400`.

### 8. Singular kernels and pivot completion

Lines 654–674 (`lem:kernels`): **PASS.** The near part of `J(d)` is scale invariant and equals at most
`2 asinh(sqrt2)+pi+2 acosh(sqrt2)=7.196771...<8`; outside `2|d|`, the kernel is at most `sqrt2/|x|`, giving the logarithmic tail. The translated logarithmic kernel is maximized when the centered interval superlevel sets align, yielding exactly `8`.

Lines 676–714 (`prop:pivot-H`): **PASS.** Scalar pivot: Schur leaves one spectral direction and the quarter-power lemma supplies the logarithmic expectation; the constant is `532.710...<600`. Definite pair: the conditional density bound gives a truncated half-potential below `160`. Indefinite pair: the hyperbolic envelope plus the logarithmic-kernel lemma gives
`D^{-1/2}(32+4log_+(16sqrt D))`; using `D>=eta` and `sup D^{-1/2}log_+D=2/e` gives `432.375...<444<600`.

Lines 716–724 (`prop:nine`): **PASS.** Pivot and no-pivot alternatives cover all matrices. The tail of `|Q-a|^{-1/2}` outside distance one is at most one, giving the full half-potential `<=601`.

### 9. Main theorem

Lines 726–749: **PASS.** No pivot uses the order-five density result. A scalar pivot removes one coordinate and Schur leaves at least 16 large eigenvalues, hence the nine-direction half-potential theorem applies, giving `6010`. A definite pair gives `<40`. An indefinite pair leaves at least 15 large eigenvalues; its Schur complement has operator norm at least one, so quarter-power/logarithmic concentration controls the random critical value. The resulting bound is `238.997...<251`. All branch estimates are conditional on original coordinates and are averaged by Tonelli; no rotated-coordinate independence is asserted.

Lines 751–779: **PASS.** Threshold accounting accurately distinguishes order five (`5/4>1`) from order three (`3/4>1/2` only after the Riesz weight). The limitation and continuity remarks match what was actually proved.

## Numerical and finite-check audit

The repository checker is correctly labelled non-formal. Its current `checks.json` reports the pinned source hash and exact interpolation/volume diagnostics plus floating Schur/graph diagnostics. I independently recalculated the key manuscript constants:

- quarter-power coefficient `3.9952593615816134 < 16`;
- near-region kernel constant `7.196771497190057 < 8`;
- no-pivot nine-direction half potential `176.9593361872953 < 200`;
- no-pivot density `2174.625462767236 < 2400`;
- scalar-pivot truncated-half bound `532.7106466687737 < 600`;
- indefinite-pivot truncated-half bound `432.3750666542770 < 444`;
- final indefinite-pair density bound `238.9973155531606 < 251`.

These computations confirm arithmetic only; the proof verdict above comes from the symbolic reconstruction.

## Lower-threshold attempt

I tested the first possible reduction, 17 -> 16, against the exact proof mechanism. No valid full reduction was obtained this run.

The obstruction is not a matter of numerical slack. At a failure ratio of order `r`, the current interpolation only supplies
`rank R<=3r` and `rank R_LL<=r`. To force an `(r+1)`-set of large diagonal entries after removing the global rank correction, one needs
`m-3r>=r+1`, i.e. `m>=4r+1`. In the worst order-five ratio `r=4`, this is exactly `m>=17`.

The algebraic rank bounds are genuinely sharp in the sense relevant to this counting step. Already for `r=1`, with

`A=[[-2,-1,-6,-9],[-1,0,1,1],[-6,1,-8,-1],[-9,1,-1,2]]`, `S={1}`, `T={2}` (one-based indexing),

the manuscript construction gives `rank P=1`, `rank R=3`, `rank R_LL=1`, while `rank(D+R)=4`. Thus the inequalities alone cannot replace `4r+1` by `4r`; a 16-eigenvalue theorem would require a new structural or analytic input, not retuning `eta` or `kappa`.

Order four from `s_13` would only give the present characteristic-function exponent `k/4=1`, i.e. the nonintegrable endpoint `O(1/|t|)`. Therefore lowering below 17 within the present proof also requires a genuine endpoint density mechanism rather than reusing the same absolute Fourier inversion.

I do **not** claim that 16 is false, only that this complete proof does not presently certify it.

## UNCHECKED portions

1. **Bibliographic/prior-art metadata only (roughly lines 74–75 and 783–789): UNCHECKED.** I did not independently verify publication metadata, priority, or completeness of the two classical attributions. They are not mathematical dependencies because all specialized ingredients used by the theorem are reproved in the manuscript.
2. **Compiled binary PDF/render claims: UNCHECKED in this run.** The repository explicitly says the binary PDF is not stored in this root. I audited the canonical LaTeX source, not the absent binary rendering.
3. **Independent-review gate: UNCHECKED/NOT SATISFIED BY THIS FILE ALONE.** This audit is one complete review. A second genuinely separate full review is still required before independent-validation status.

No mathematical source range needed for the theorem was left unchecked.
