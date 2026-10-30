SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet02, slot B01, 2026-09-24T13:05:58Z.
attacking: theorem quantifiers, scaling and dependency closure for the fixed-multiplicity manuscript, with counterexample stress tests and a complete threshold reduction only after the baseline is independently secured.

# fleet02/B01 independent end-to-end fixed-multiplicity audit

Run: `20260924T130558Z-fleet02-B01-fixedmult-r11`  
Owner objective: `QFORM-FIXED-MULTIPLICITY-AUDIT-20260924`  
B01 lens: theorem quantifiers, scaling, dependency closure.  
Fleet02 lens: counterexamples / failure modes.

## Source pin and review boundary

The mathematical baseline audited here is immutable:

- repository: `yspennstate/math-open-problems`
- initial source commit: `7c0d6e60946b19423e6400a12d34b473cf0591e2`
- path: `proofnet24/QFORM-density/fixed-multiplicity-2026-09-24/manuscript.tex`
- git blob: `183ccd294763214e6a707e8d4749ff9a8cf7006d`
- SHA-256: `9f3bdec0b88debe9a66076c7b4a5cc894fb14e69b89591a4107e785340f65e69`
- bytes: 47,883; lines: 790.

The live `master` observed during this review advanced through `8a2a3a4bfcb01b398f35ee2db350a6188bf2395c`; these later commits did not change the baseline manuscript blob/hash. The current root support package (`SOURCE_MANIFEST.json`, `proof_map.csv`, `verify.py`, `checks.json`) was read after it appeared. The checker is treated only as a finite diagnostic, never as proof.

## Overall verdict

**Baseline 17-eigenvalue theorem: PASS in this independent mathematical review.** I found no fatal mathematical defect and no hidden weakening of the stated quantifiers. The statement really covers arbitrary independent real coordinates with densities bounded by `K`, arbitrary real symmetric `A`, arbitrary affine `b,c`, all signatures and remaining spectrum, and gives an essential density bound `10000 K^2/s` under `s_17(A)>=s>0`.

**Package/reproducibility: PASS at the current live root, with one historical limitation.** At the first source observation several README-advertised support files had not yet reached `master`; they were subsequently added and read. The historical self-audit's older finite-test counts remain **UNCHECKED** as historical claims because the newly supplied checker explicitly does not reproduce that older suite. The new checker itself is **PASS within its stated finite scope**.

**No FALSE item was found.** One wording point in the projection proof is editorial only: after dropping rows with `b_i=0`, the displayed estimate may be read as if `sum(1-b_i)=d` were taken only over retained rows. The needed inequality is `sum_{b_i>0}(1-b_i)<=sum_i(1-b_i)=d`; the final bound is unchanged.

## Exhaustive source coverage, lines 1--790

Every manuscript line is covered below either by a labeled statement/proof row or by an explicit connective-prose row. `PASS` means I independently reconstructed the stated implication and checked all hypotheses at later invocations; it is not inherited from the author self-audit.

| Source range / label | Verdict | Independent check, downstream impact, next obligation |
|---|---|---|
| 1--46, front matter, abstract, notation | PASS | Claims match the theorem actually proved. Nonsymmetric `R,E` are explicitly auxiliary; no random quadratic form is replaced by them. No continuity claim is silently added. |
| 47--57 `thm:main` | PASS | Quantifiers are complete: independent cap-`K` coordinates, arbitrary symmetric `A`, arbitrary affine `b,c`, `s_17(A)>=s>0`. Dimension/sign/other spectrum are unrestricted. Interval domination is equivalent to an `L^infty` density bound. |
| 59--61 `cor:33` | PASS | Immediate since `s_17(A)>=s_33(A)`. |
| 62--90 architecture/parameters | PASS | `eta=1/100`, `kappa=1/80^2`; pivot/no-pivot split is exhaustive. Counts `9=4*3-3`, `17=4*5-3` match later uses. No rotated-independence premise. |
| 91--120 `lem:fourier` | PASS | Fourier convention, Plancherel factor `2pi`, Gaussian regularization and inversion checked. Approximate-identity and weak-limit arguments are valid for rough `L^1 cap L^2` densities; Gaussian identity needs no moments. |
| 122--130 `lem:envelope` | PASS | Integral of `min(1,(a/|t|)^p)` is `2ap/(p-1)`; inversion gives `ap/[pi(p-1)]`. |
| 132--160 `lem:riesz` | PASS | Gamma representation and Gaussian inversion produce coefficient `1/sqrt(2pi)`; weighted envelope integral is `12 sqrt(u)`. Extended-value Tonelli handles atoms correctly. |
| 161--168 connective spectral notation | PASS | `N_A(t)` and singular-value conventions are used consistently with `>=t`. |
| 169--181 `lem:rank` | PASS | SVD approximation formula gives both Lipschitz perturbation and rank-shift inequality for nonsymmetric matrices. This is exactly the form needed for `A-E=D+R`. |
| 183--207 `lem:schur` | PASS | For invertible `A`, complementary compression of `A^{-1}` is `S^{-1}`; positive and negative interlacing bound eigenvalues outside `(-1/t,1/t)`, yielding `N_S(t)>=N_A(t)-k`. For singular `A`, `A+eps I` with moving threshold `t-|eps|` and continuity gives the non-strict endpoint. No inertia-only shortcut is used. |
| 209--217 `lem:dd` | PASS | Standard maximal-coordinate proof works without symmetry, exactly as required for `R[H,H]`. |
| 218--255 `thm:bl` | PASS | Heat kernel convention satisfies `partial_t f=partial_s^2 f`; frame identity makes `partial_t F-Delta F>=0`; integration by parts and Gaussian tails are adequate; large-time scaling gives product masses; Fatou plus monotone truncation closes rough inputs. |
| 256--282 `lem:projection` | PASS (editorial clarification) | Original-coordinate product density is integrated only after a deterministic orthogonal coordinate change. Geometric BL gives `prod b_i^{-b_i/2}`. The correct last step is `sum_{b_i>0}(1-b_i)<=d`; this is enough for `e^{d/2}`. Scalar scaling is correct. No post-rotation independence is asserted. |
| 284--301 `lem:scalar-fourier` | PASS | `m=floor(p/2)>=p/4`, `|hat f|<=1`, and Plancherel make `|hat f|^{2m}` integrable. Fourier inversion at zero plus the projection lemma for the `2m` signed coordinates yields `2pi sqrt(2e)/sqrt(p)`. Difference density is cap one by convolution. |
| 302--324 `lem:decoupling` | PASS | Cauchy--Schwarz is taken before expanding an independent copy of the `J` bank; same-bank phases have modulus one after expansion, and integrating original independent `I` coordinates gives the product Fourier factors. `D=X_J-X'_J` remains a product law with cap-one coordinates. No conditional marginal cap is assumed. |
| 326--373 `thm:determinant` | PASS | Frame vectors from `H=alpha I+a^2M^TM` sum to identity. BL exponents `c_j,d_i` are in `[0,1]`; `sum d_i=sum(1-c_j)`. The scalar Fourier-power factor cancels `d_i^{-d_i/2}`; `prod c_j^{-c_j/2}<=e^{theta/2}` and `alpha=(2pi e)^2` cancel the remaining graph factor. Fourth root gives exponent `-1/8` with denominator `pi^2 e^2`. |
| 374--400 crossing volumes and `cor:vol-fourier` | PASS | Cauchy--Binet identifies `Z_k=e_k(M^TM)`. Retaining the order-`k` determinant term gives exponent `k/4`; `k=5` is integrable and yields `5e Z_5^{-1/10}`, while `k=3` is used only with the Riesz weight and yields the displayed half-potential. **Counterexample check:** an order-two/hyperbolic form such as `2XY` with uniform cap-one inputs has a logarithmic density singularity, so no illicit rank-two density conclusion is hidden here. |
| 401--421 `lem:square` and conditional profile | PASS | Monotone inverse branches give the square-root envelope and interval preimage bound. Conditional application is a measure-domination/Tonelli statement; it never claims independence between the completed square and Schur remainder. |
| 423--434 `lem:definite` | PASS | Completing the square and diagonalizing only the deterministic integral gives Jacobian `1/(2 sqrt(det B))`; integration over angle yields `pi M/sqrt(|det B|)`. |
| 435--482 `lem:hyperbola` | PASS | Hyperbolic parametrization Jacobian is `1/(2sqrt D)`. The original-coordinate tail choice is legitimate despite spectral rotation; monotone tail substitution uses only one original marginal cap and total mass. Cutoffs give the stated logarithmic envelope; `Lambda>=2/sqrt D` closes the determinant scaling. |
| 483--525 `lem:quarter` | PASS | Large diagonal branch uses the scalar interval bound. Otherwise random signs extract a literal cross block with norm at least `L/4`; the determinant theorem supplies `|t|^{-1/4}`. Gaussian smoothing gives the quarter small-ball bound, hence atomlessness; layer cake gives `L_0=4+4log16`. This is not a forbidden law-uniform pointwise scalar quadratic-phase estimate. |
| 526--543 definitions/no-pivot entry bound | PASS | Pivot definition is exhaustive. With no pivot, `|a_ij|^2<=|a_ii a_jj|+|a_ii a_jj-a_ij^2|<eta^2+eta<1/49`; the strict `1/7` bound is valid. `V_r` orientation/disjointness matches the random-cut formula later. |
| 545--564 `lem:sampling` | PASS | Bordered determinant identity is exact. Determinant-squared sampling counts each disjoint `(r+1)` pair at most `(r+1)^2`; singular seeds can have nonsingular extensions, so the manuscript correctly states an inequality, not equality. `P` interpolates rows `S` and columns `T`. |
| 566--580 `lem:completion` | PASS | `E` is exactly the off-diagonal `LxL` residual; `D` is diagonal and zero on the seed; `R[L,L]=P[L,L]` has rank `<=r`. `R-P` is supported only in rows `T` or columns `S`, so global `rank R<=3r`. Nonsymmetry is harmless because all subsequent uses are rank/singular-value estimates. |
| 582--619 `prop:volume` | PASS | Telescoping selects `r<=k-1`. For `r=0`, `||A||<eta+sqrt(kappa)<1`. For `r>=1`, `eps<=(r+1)/80<=1/16`; rank shift gives at least `r+1` large entries of `D`, all in `L`. On the selected `H`, `|R_ii|>=371/400`, while each off-diagonal is `<1/7+1/16`; for `r<=4`, row sum `<23/28`, leaving exact slack `297/2800>0`. Strict diagonal dominance contradicts `rank R[L,L]<=r`. Index inequality `4k-3>=4r+1` is exact at the terminal seed. |
| 621--630 `lem:cut` | PASS | Each ordered disjoint `(S,T)` survives a fair cut with probability `4^{-k}`; expectation and existence statements follow. |
| 632--645 `cor:no-pivot` | PASS | At `k=3,5`, random cut gives `Z_k^{-1/(2k)}<=160`. Constants are `12sqrt(80e)<200` for the full half-potential and `800e<2400` for density. All affine and same-bank terms stay inside the full quadratic crossing theorem. |
| 646--674 `H` and `lem:kernels` | PASS | Truncation is explicit. The `J(d)` near/far split has an integrable near constant and logarithmic far tail. The log-kernel bound follows from interval-superlevel rearrangement and equals `8` at the centered worst case. |
| 676--714 `prop:pivot-H` | PASS | Scalar pivot plus Schur count leaves a nonzero spectral direction, so quarter concentration/log control applies; conditional profile integrates to `J(R-a)`. Definite pair and indefinite pair branches retain arbitrary conditioning shifts. `sup D^{-1/2}log_+D=2/e`; all three branches are <600. |
| 716--724 `prop:nine` | PASS | Pivot branch gives truncated `H<=600`; outside `|Q-a|<=1`, the kernel is at most one, so the full half-potential is `<=601`. No-pivot branch already controls the full potential. This distinction is used correctly later. |
| 726--749 proof of `thm:main` | PASS | No-pivot: order five gives <2400. Scalar pivot: Schur count leaves 16 directions, hence the nine-direction full half-potential and `6010`. Definite pair is direct; indefinite pair needs only one surviving Schur direction for the log potential and has 15. All conditioning is on original coordinates. |
| 740--749 scaling and interval equivalence | PASS | With `Y=KX`, each `Y_i` has density <=1. `A/s` has `s_17>=1`; `Q=(s/K^2) Qtilde`, hence density scaling gives exactly `K^2/s`. Affine coefficients transform to `(K/s)b` and `(K^2/s)c` as written. Interval domination extends to Borel domination and hence the essential density bound. |
| 750--790 threshold accounting, limitations, bibliography | PASS | Dependency table matches actual proof. The paper explicitly disclaims the three-eigenvalue theorem and global continuity. Bibliographic references are attribution only; every specialized ingredient actually used is proved in the manuscript. |

## Equation/constant and adversarial checks

I separately re-derived the constants that control the dependency closure:

- `eta+sqrt(kappa)=1/100+1/80<1` (the `r=0` no-pivot contradiction).
- terminal completion error `(r+1)sqrt(kappa)<=5/80=1/16` for `r<=4`.
- diagonal-dominance slack `371/400-23/28=297/2800>0`.
- no-pivot half-potential `12sqrt(80e)<200` and density `800e<2400`.
- scalar-pivot baseline bound `10*(8+3(4+4log16))=532.71...<560`, hence the advertised `600` reserve is safe.
- main scalar branch is `10*601=6010<10000` and dominates the other normalized branches.

Counterexample/failure-mode stress tests relevant to overclaims:

1. **Do not promote order two to a density theorem.** For independent uniform variables, `2XY` has a logarithmic singularity at zero. The manuscript correctly uses second-order information only for fractional/half-potential control.
2. **Do not infer density from the baseline order-three determinant envelope alone.** Its decay exponent is `3/4`, nonintegrable without the `|t|^{-1/2}` Riesz weight. The manuscript does not make that inference.
3. **Do not symmetrize the interpolation.** The proof needs the sharper restricted rank `rank R[L,L]<=r`; replacing the auxiliary by a naive symmetric correction can destroy the rank accounting. The manuscript explicitly keeps `P,R,E` nonsymmetric and never inserts them into the random quadratic form.
4. **Do not use pointwise scalar Fresnel decay for rough laws.** No such step appears. Every Fourier gain is a joint/full-product estimate or an integrated Fourier-power estimate.

## Support-file audit

- `SOURCE_MANIFEST.json`: **PASS** as a source-integrity manifest. It pins the exact baseline blob/hash and correctly says the new checks are not formal verification.
- `proof_map.csv`: **PASS**; its statement/proof line ranges match the labels in the 790-line source.
- `verify.py`: **PASS within finite scope**. It pins the source SHA, checks the exact `297/2800` slack, exact interpolation identities/ranks/volume inequality on sampled rational matrices, and floating Schur/graph diagnostics. It makes no universal-proof claim.
- `checks.json`: **PASS as an execution record**, reporting 534 exact interpolation seeds, 18 volume comparisons, 240 numerical Schur threshold cases and 30 graph-weight cases.
- historical finite-test counts in the original `AUDIT.md`: **UNCHECKED**. The current checker explicitly states that it is a new suite and does not reproduce those historical counts. This has no downstream mathematical effect because the written proof was independently checked above.

## Baseline dependency closure

The proof graph closes internally:

`BL -> projection -> scalar Fourier powers -> decoupling -> regularized determinant -> volume envelopes`,

and independently

`rank + Schur + diagonal dominance -> sampling -> completion -> spectral-to-volume -> random cut`.

The pivot branch uses

`square/definite/hyperbolic + quarter concentration + kernel bounds + Schur count -> pivot half-potential -> nine-direction full half-potential`.

The final theorem then combines `no-pivot order five` with `scalar/pair pivots`, followed by the exact `(K,s)` scaling. I found no missing imported theorem and no cycle in which the main result is assumed upstream.

## Review-state conclusion

This document is one genuinely independent fleet02/B01 end-to-end mathematical review. It does not self-award an owner-level release certificate. The pinned baseline remains preserved; any lower-threshold candidate is recorded separately under this run's `improvements/` path.
