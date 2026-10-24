# account02/B09 r13 — fixed-multiplicity end-to-end audit and spectral-rank reconstruction

Objective: `QFORM-FIXED-MULTIPLICITY-AUDIT-20260924`.

## Pins and scope

Fresh brain-main control used for this invocation: `bcf828c173f6d4aeafa0623cc868b3946efbe504`, refreshed before publication with the same current objective still present. The fixed-multiplicity package was read from `yspennstate/math-open-problems` master as observed at `b2aa8c2d89e668f703b095754abf4a43c93945de`; subsequent peer commits changed only audit/improvement material, not the pinned manuscript source used here.

Pinned baseline mathematical source:

- initial source commit `7c0d6e60946b19423e6400a12d34b473cf0591e2`;
- `manuscript.tex` git blob `183ccd294763214e6a707e8d4749ff9a8cf7006d`;
- SHA-256 `9f3bdec0b88debe9a66076c7b4a5cc894fb14e69b89591a4107e785340f65e69`;
- 47,883 bytes, 790 lines.

I read the entire 790-line manuscript plus `README.md`, `SOURCE_MANIFEST.json`, `AUDIT.md`, `proof_map.csv`, `verify.py`, `checks.json`, and `DELIVERY_STATUS.md`. The support package is now present. This report is an independent mathematical review, not formal verification or journal peer review.

## Baseline verdict

**PASS** for the stated seventeen-eigenvalue candidate theorem. I found no fatal gap and no manuscript source region left unchecked. Precisely: for independent real coordinates with densities bounded by `K`, arbitrary real symmetric `A`, arbitrary affine `b,c`, and `s_17(A)>=s>0`, the manuscript proves an essential density bound `||p_Q||_infty <= 10000 K^2/s`. It does not prove global continuity and does not solve the unrestricted three-eigenvalue conjecture.

| Source range / label | Status | Independent check, impact, next obligation |
|---|---|---|
| 1–90, theorem statement, normalization, architecture | PASS | Quantifiers retain arbitrary dimension/sign/remaining spectrum/affine terms/rough product laws. The `Y=KX`, `A/s` normalization gives the required `K^2/s` scaling. No hidden continuity claim. |
| 91–120 `lem:fourier` | PASS | Plancherel normalization, Gaussian regularization, weak-limit identification and the `L^1` inversion statement are consistent with the transform convention. |
| 122–130 `lem:envelope` | PASS | Exact envelope integral is `2ap/(p-1)` and inversion gives `ap/[pi(p-1)]`. |
| 132–160 `lem:riesz` | PASS | Gamma representation and Gaussian inversion give the displayed `1/sqrt(2pi)` coefficient; the `3/4` envelope contributes exactly `12 sqrt(u)`. |
| 161–181 conventions + `lem:rank` | PASS | The singular-value approximation formula gives both perturbation and rank-shift inequalities for nonsymmetric auxiliaries. No eigenvalue statement is made about `A-E`. |
| 183–207 `lem:schur` | PASS | For invertible `A`, `S^{-1}` is a principal compression of `A^{-1}` and positive/negative interlacing separately gives the absolute spectral count. The singular case follows by an admissible `A+eps I` sequence and continuity. |
| 209–217 `lem:dd` | PASS | Strict row diagonal dominance proves injectivity without symmetry. |
| 221–255 geometric rank-one BL | PASS | Heat-flow derivative has the correct sign from the Parseval frame, Gaussian tails justify integration by parts, and Fatou/monotone convergence cover rough nonnegative inputs. |
| 258–282 product projections | PASS | Only original product coordinates are used. The `b_i=0` factors are dropped harmlessly; the entropy sum over retained rows is at most `d` (equivalently one may include zero rows to write the displayed `d`). No rotational independence is assumed. |
| 284–301 scalar Fourier powers | PASS | `m=floor(p/2)>=p/4`, Plancherel makes the even power integrable, and the one-dimensional projection cap yields `2pi sqrt(2e/p)`. |
| 303–324 decoupling | PASS | Copies are introduced only in the literal `J` bank. Cauchy–Schwarz/Jensen produce powers two/four exactly; difference coordinates remain independent with density cap one. |
| 326–373 regularized determinant | PASS | The whitened graph rows form an identity decomposition, BL exponents are in `[0,1]`, scalar Fourier powers cancel the row weights, and `alpha=(2pi e)^2` gives determinant exponent `-1/8`. |
| 375–400 crossing volumes / envelopes | PASS | Cauchy–Binet coefficients are correct. `k=5` gives an integrable `5/4` characteristic exponent; `k=3` is used only with the Riesz `|t|^{-1/2}` weight. |
| 402–414 scalar square | PASS | Branch Jacobians and the inverse-image length bound are correct; the conditional use is a measure-domination statement. |
| 416–434 definite pair | PASS | Elliptic polar Jacobian is `1/(2 sqrt(det B))`; only the joint density cap is used after deterministic rotation. |
| 436–482 hyperbolic pair | PASS | Hyperbolic Jacobian, two-tail monotonicity, half-line rearrangement and `Lambda>=2/sqrt(D)` give the displayed logarithmic envelope. Exceptional critical level is handled through test functions/Tonelli. |
| 484–525 quarter-power concentration | PASS | The large-diagonal branch and random-sign crossing branch are exhaustive. The determinant receiver gives the `1/4` Fourier exponent; Gaussian smoothing and layer cake yield the atom-free/log-potential bounds. |
| 527–543 no-pivot entry bounds / volumes | PASS | From absence of a principal determinant pivot, `|a_ij|^2<eta+eta^2<1/49`; ordered disjoint-minor convention is consistent downstream. |
| 545–564 `lem:sampling` | PASS | Bordering identity is exact; a disjoint `(r+1,r+1)` extension is counted at most `(r+1)^2` times. Singular seeds can only make the average inequality strict. |
| 566–580 `lem:completion` | PASS | `D` vanishes on `S union T`; `E` has zero diagonal; `R_LL=P_LL`. Support of `R-P` is contained in rows `T` or columns `S`, giving global rank `<=3r` and restricted rank `<=r`. |
| 582–619 `prop:volume` | PASS | Rebuilt below in detail. The argument correctly uses the global `3r` loss only before selecting large diagonal sites and the restricted `r` rank only after those sites are forced into `L`. |
| 621–630 random cut | PASS | Each ordered disjoint minor survives a fair literal cut with probability `4^{-k}`. |
| 632–645 no-pivot analytic consequences | PASS | `Z_k^{-1/(2k)}<=160`; constants `12 sqrt(80e)<200` and `800e<2400` are valid. |
| 647–674 singular kernels | PASS | The near/far split in `J(d)` and interval-overlap proof of the logarithmic kernel are valid with the stated slack. |
| 676–714 pivot half-potential | PASS | Scalar, definite and indefinite alternatives use their exact hypotheses. The scalar child has a surviving unit eigenvalue; the logarithmic critical-value dependence is averaged by Tonelli rather than treated as independent. |
| 716–724 nine-eigenvalue half-potential | PASS | Pivot and no-pivot branches give truncated `<=600`; the tail contributes at most one, yielding the full `<=601`. |
| 726–749 main theorem | PASS | No-pivot branch uses `s_17`; scalar pivot loses one Schur direction but still has `s_9`; pair pivots are separately paid. Largest baseline branch is `6010<10000`. General scaling is correct. |
| 751–790 threshold/limitations/bibliography | PASS | The stated dependency map accurately separates full `3r` and restricted `r` rank losses; the text explicitly leaves the three-eigenvalue problem open and does not claim global continuity. |

No baseline source line is `GAP`, `FALSE`, or `UNCHECKED` in this review.

## B09 reconstruction: spectral perturbation and diagonal dominance

For a sampled seed of order `r>=1`, write `A=D+R+E` with `rank R<=3r`, `rank R_LL<=r`, `D=0` on the `2r` seed coordinates, `diag E=0`, and `epsilon=||E||_F<=(r+1)/80<=1/16`. If `m=4k-3`, `r<=k-1`, and `s_m(A)>=1`, then

` s_m(D+R)=s_m(A-E)>=1-epsilon `

and the rank-shift inequality gives

` s_{m-3r}(D)>=s_m(D+R)>=1-epsilon. `

Since `m-3r>=r+1`, a diagonal `D` has at least `r+1` entries with modulus at least `1-epsilon`; because `D` vanishes on the seed, all lie in `L`. On any resulting `(r+1)`-set `H subset L`,

`|R_ii| >= 1-1/16-1/100 = 371/400`,

while for `i!=j`,

`|R_ij| <= |A_ij|+|E_ij| < 1/7+1/16 = 23/112`.

There are only `r<=4` off-diagonal competitors in a row, so

`sum_{j!=i}|R_ij| < 4(23/112)=23/28`,

and the exact dominance slack is

`371/400 - 23/28 = 297/2800 > 0`.

Thus `R_HH` is invertible of rank `r+1`, contradicting `rank R_LL<=r`. Every index and inequality survives the fact that `R,E` may be nonsymmetric.

## Counterexample stress: the two rank charges are simultaneously sharp

I independently reconstructed the exact no-pivot family, for arbitrary `r>=1` and `0<delta<1/10`, on three disjoint `r`-sets `S,T,L`:

`A = [[0, delta^2 I, delta I], [delta^2 I, 0, delta I], [delta I, delta I, 0]].`

Take seed `B=A[S,T]=delta^2 I`. The manuscript interpolation and completion are

`P=[[0,delta^2 I,delta I],[0,0,0],[0,delta I,I]]`,

`E=0`, `D=diag(0_S,0_T,-I_L)`, `R=A-D`.

For each scalar three-coordinate component, `det R_0=delta^4`, `rank P_0=1`, and `rank(R_0-P_0)=2`. Hence simultaneously

`rank P=r`, `rank(R-P)=2r`, `rank R=3r`, `rank R_LL=r`.

Every diagonal of `A` is zero and every principal two-coordinate determinant has modulus at most `delta^2<eta`, so the family is genuinely no-pivot. Because it is a direct sum of `r` three-coordinate components, every disjoint minor of order `r+1` vanishes: `V_{r+1}=0`. I rechecked these identities exactly for `r=1,2,3` with rational `delta=1/20`; all ranks and volumes match the formulas.

This is a **source-valid counterexample to improving the completion bookkeeping by replacing `3r` or `r` with smaller generic rank charges**, not a counterexample to a spectral density theorem: for small `delta` the original `A` does not have the required large spectrum. At `r=2` it exhibits the exact algebraic `s_8` saturation pattern (`rank R=6`, `rank R_LL=2`, two unit entries in `D`, `V_3=0`) and shows why the ninth direction cannot be removed by rank/support arithmetic alone.

## Support-package audit

`SOURCE_MANIFEST.json` pins the same 790-line source and correctly distinguishes the compiled PDF from the GitHub source. `proof_map.csv` agrees with all statement/proof ranges above. `verify.py` first checks the manuscript SHA-256, then performs exact interpolation/support/rank/volume tests and floating Schur/graph diagnostics; I found no logical mismatch between the code and the claims it reports. `checks.json` records `PASS`, 534 exact interpolation seeds, 18 volume-sampling cases, 240 Schur-threshold diagnostics and 30 graph-weight diagnostics. I inspected the code and stored result but did **not** represent the stored run as a fresh execution by this invocation; fresh full checker execution is therefore `UNCHECKED` operationally, with no mathematical consequence because the symbolic proofs above were reconstructed independently.

## Lower-threshold replacement independently reconstructed in this run

After the baseline passed, I independently reconstructed the complete multiplicity-nine replacement recorded separately in this run's improvement artifact. It preserves every baseline quantifier and gives

`||p_Q||_infty < 5338 K^2/s` whenever `s_9(A)>=s>0`.

The new ingredients are a grouped product-Fourier lemma, a marginal-free order-three density receiver with constant

`C3=3 sqrt(2) e (9/2)^(1/6)=14.818337662843...`,

and a marginal-free order-two **full half-potential** receiver

`C2=8 sqrt(e) 2^(-1/8)=12.095072570796...`.

No-pivot `s_9` gives `V_3>=kappa^3`, hence a literal cut with `E_3^{-1/6}<=160` and density `<2371`. In the scalar-pivot branch, the Schur complement retains eight unit directions. If it has a pivot, the exact baseline truncated-half-potential constants give full half potential at most `533.7106467`; if it has no pivot, `s_5` plus the order-two receiver gives only `152.991912`. Multiplying by the outer `eta^{-1/2}=10` gives the dominant `5337.106467<5338`. Pair-pivot branches remain `<32` and `<251`. Scaling gives `K^2/s`.

I checked the new grouped-Fourier proof independently: the complex pushforward densities are controlled in `L^2` by product-projection caps; Gaussian regularization makes the conditional Plancherel step legitimate; determinant-weighted Holder uses row marginals `alpha_i<=1/2`; the scalar Fourier-power integral is used only at exponent `1/alpha_i>=2`; and entropy subadditivity for a uniformly ordered random `ell`-subset gives

`H(w)+sum_i alpha_i log alpha_i <= ell log ell - log(ell!)`.

Promotion of any row carrying more than half the determinant mass terminates after at most three literal rows, so no leverage assumption remains. The resulting theorem is a complete replacement proof, not a Gaussian/diagonal/exact-rank special case.

A still newer peer artifact advertises a smaller constant at the same threshold; that numerical sharpening was not independently reconstructed here and is `UNCHECKED` in this report. It does not affect the threshold-nine conclusion.

## Threshold frontier and next obligation

The best complete threshold I can justify end-to-end in this invocation is **nine**. Multiplicity eight remains open in the current route. Fresh peer work narrows one important `s_8` no-pivot survivor to a strong literal two-anchor crossing together with four unit outside spectral directions; a sufficient next lemma is a product-preserving uniform `L^2` density bound for the joint map

`(CY+u, Y^T D Y+v^T Y+w)`

under that robust two-anchor currency. The exact rank-sharp family above shows that generic improvements of the manuscript's `3r/r` bookkeeping cannot close this frontier.

The unrestricted three-eigenvalue QFORM conjecture remains **OPEN**.
