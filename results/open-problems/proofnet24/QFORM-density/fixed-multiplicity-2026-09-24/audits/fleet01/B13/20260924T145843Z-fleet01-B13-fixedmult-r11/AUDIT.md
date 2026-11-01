# fleet01/B13 end-to-end audit — fixed-multiplicity manuscript

Run: `20260924T145843Z-fleet01-B13-fixedmult-r11`  
Objective: `QFORM-FIXED-MULTIPLICITY-AUDIT-20260924`  
Pinned source commit: `7c0d6e60946b19423e6400a12d34b473cf0591e2`  
Pinned manuscript git blob: `183ccd294763214e6a707e8d4749ff9a8cf7006d`  
Pinned source SHA-256 (manifest/checker): `9f3bdec0b88debe9a66076c7b4a5cc894fb14e69b89591a4107e785340f65e69`  
Current `master` manuscript blob observed in this run: `183ccd294763214e6a707e8d4749ff9a8cf7006d` (same pinned source).

## Verdict

**PASS as a complete mathematical audit of the pinned 17-eigenvalue argument.** I found no fatal mathematical defect in the theorem as stated: independent arbitrary real coordinate densities bounded by `K`, arbitrary real symmetric `A` with `s_17(A)>=s>0`, arbitrary affine terms, and essential density bound `<=10000 K^2/s`. This report does **not** self-award release status, journal peer review, formal verification, or validation of the unrestricted three-eigenvalue conjecture.

Every line of `manuscript.tex` was read in this run, together with `README.md`, `DELIVERY_STATUS.md`, `AUDIT.md`, `proof_map.csv`, `SOURCE_MANIFEST.json`, `verify.py`, and `checks.json`. The mathematical source is fully checked below. The only deliberately `UNCHECKED` items are external prior-art/priority attribution and independent recompilation/rendering of the PDF binary; neither is a proof dependency.

## B13 starting lens: definite pair and hyperbolic envelope

### Lines 423–434 — `lem:definite`: PASS

After completion of the square, deterministic orthogonal diagonalization is used only inside the two-dimensional integral. For eigenvalues `mu_1,mu_2>0`, the map

`w=w0+sqrt(delta/mu1) cos(theta)e1+sqrt(delta/mu2) sin(theta)e2`

has absolute Jacobian `1/(2 sqrt(det B))` in `(delta,theta)`. Integrating a joint density bounded by `M` over `theta in [0,2pi)` gives `pi M/sqrt(|det B|)`. Rotation does not invoke independence; Lebesgue density cap is preserved by an orthogonal change of deterministic integration variables. The negative-definite case is obtained by negating the form. Hypotheses and conclusion match every later invocation.

### Lines 437–482 — `lem:hyperbola`: PASS

I rederived both signs of the level set. For `delta=z-v>0`, with eigenvalues `mu_+>0>mu_-`, the two branches

`w_epsilon(t)=epsilon sqrt(delta/mu_+) cosh(t)e_+ + sqrt(delta/|mu_-|) sinh(t)e_-`

cover the noncritical level and the `(delta,t)` Jacobian has absolute value `1/(2 sqrt(D))`, `D=|det B|`. Writing each branch as `u e^t+w e^-t`, orthogonality gives

`|u|=|w|=sqrt(delta Lambda)/2`, `Lambda=mu_+^-1+|mu_-|^-1`.

On the positive tail, an original coordinate can be chosen with `|u_i|>=|u|/sqrt(2)`. For `t>=(3/4)log 2`, the growing exponential dominates, the coordinate is monotone, and

`|x_i'(t)| >= |x_i(t)|/3` after translation relative to the quadratic center. Choosing the cutoff so the relative coordinate modulus is at least one gives

`int_tail f_1 f_2 dt <= 3 int_{one sign, |y|>=1} f_i(y)/|y| dy <=3 log 2`,

using only `0<=f_i<=1` and total mass one. The negative tail is identical using `w`. The middle interval has length at most

`(3/2)log 2 + log_+(32/(delta Lambda))`.

Thus each branch contributes less than `6+log_+(32/(delta Lambda))`; summing two branches against the Jacobian yields the stated `D^-1/2` envelope. AM–GM gives `Lambda>=2/sqrt(D)`, converting the logarithm to `log_+(16 sqrt(D)/delta)`. For `delta<0`, negate the form and exchange the positive/negative eigendirections; the same proof applies. The critical level `delta=0` is a union of one-dimensional lines in the two-dimensional anchor plane, hence has conditional input probability zero because the product law has a Lebesgue density. The manuscript's nonnegative-test-function/Tonelli formulation correctly avoids selecting rough density values on this exceptional level.

No rotated-coordinate independence is used. The only places product structure enters are the original-coordinate bounds `f_1 f_2<=f_i` on the tails and the original marginal mass/cap.

### Lines 682–714 and 726–749 — critical-value averaging: PASS

For an indefinite principal pair, conditioning is on the complement in original coordinates. The hyperbolic critical value is a quadratic polynomial `R` in those complementary coordinates. The logarithmic envelope is averaged by

`E log_+(1/|z-R|)`,

and `lem:quarter` supplies a uniform logarithmic-potential bound whenever the Schur complement retains one unit-scale eigenvalue. This is exactly what the Schur spectral-count lemma provides: at least one direction in the pivot-half-potential proposition and at least fifteen directions in the main theorem. The dependence of the critical value on the conditioning variables causes no exceptional-slice error because the conditional measure domination is integrated through Tonelli.

## Full source audit by line range

| Source range | Item | Verdict | Independent reasoning / dependency check |
|---|---|---|---|
| 1–46 | metadata, abstract, setup | PASS | Abstract matches the theorem actually proved and does not claim the unrestricted three-eigenvalue result or continuity in every branch. |
| 47–80 | `thm:main`, `cor:33`, architecture, parameters | PASS | Quantifiers are full arbitrary-law/sign/dimension/affine scope. `eta=1/100`, `kappa=1/80^2`; threshold accounting `9=4*3-3`, `17=4*5-3` matches later proof. |
| 81–120 | Fourier convention and `lem:fourier` | PASS | Gaussian regularization gives Plancherel with the stated `2pi` convention; `phi in L1` inversion and the Gaussian expectation identity have the correct constants. |
| 122–130 | `lem:envelope` | PASS | Envelope integral is `2ap/(p-1)`; division by `2pi` gives `ap/[pi(p-1)]`. |
| 132–160 | `lem:riesz` | PASS | Gamma representation plus Gaussian inversion yields coefficient `1/sqrt(2pi)`; weighted envelope integral is exactly `12 sqrt(u)`. Tonelli is used only on nonnegative majorants. |
| 161–181 | norms and `lem:rank` | PASS | Approximation-number formula proves singular-value Lipschitzness and rank perturbation without symmetry. |
| 183–207 | `lem:schur` | PASS | For invertible `A`, `(A^-1)_{CC}=S^-1`; positive and negative interlacing for principal compressions gives the absolute spectral count. The singular case is obtained by `A+epsilon I` at threshold `t-|epsilon|` and ordered-eigenvalue continuity. |
| 209–217 | `lem:dd` | PASS | Standard strict row diagonal-dominance contradiction works for nonsymmetric matrices. |
| 221–255 | geometric rank-one BL proof | PASS | Heat-flow derivative is nonnegative by the frame contraction; trace gives `sum c_i=d`; Gaussian asymptotics and truncation/monotone convergence justify endpoints. No imported theorem is needed for correctness. |
| 258–282 | `lem:projection` | PASS | Orthogonal completion and BL produce `prod b_i^{-b_i/2}<=e^{d/2}`. Orthogonal deterministic coordinates do not assert stochastic independence. Scalar scaling gives `sqrt(e)/|a|`. |
| 284–301 | scalar Fourier powers | PASS | With `m=floor(p/2)`, `2m<=p` and `m>=p/4`; the even Fourier power is the density at zero of a normalized linear form in `2m` independent coordinates. Constant `2pi sqrt(2e)/sqrt(p)` is correct. |
| 303–324 | cross form and decoupling | PASS | Cauchy–Schwarz duplicates only the `J` bank; averaging the untouched independent `I` coordinates gives the Fourier product. Difference coordinates remain independent with density cap one. No moments are used. |
| 326–373 | regularized crossing determinant | PASS | Frame weights `c_j,d_i` sum correctly; BL scalings were recomputed. Scalar Fourier exponents `2/d_i>=2` are legal. `prod c_j^{-c_j/2}<=e^{theta/2}` and `alpha=(2pi e)^2` cancel the prefactor. Fourth-rooting gives exactly `det(I+t^2 M^TM/(pi^2e^2))^-1/8`. |
| 375–400 | crossing volumes and `cor:vol-fourier` | PASS | Cauchy–Binet expansion is correct. Retaining the order-`k` term gives exponent `k/4`; `k=5` yields `5e Z_5^-1/10`; `k=3` yields the stated full negative-half moment. |
| 401–421 | scalar square profile and conditional domination | PASS | Inverse-branch density and interval preimage length are correct. Conditional Tonelli yields the profile without falsely asserting independence of square and remainder. |
| 423–434 | definite pair | PASS | See detailed B13 check above. |
| 437–482 | hyperbolic pair | PASS | See detailed B13 check above; both level-set signs, tails, mass/cap use, logarithmic factor, and critical level were rederived. |
| 485–525 | quarter-power concentration/log potential | PASS | Diagonal case uses scalar interval length. Off-diagonal random sign cut gives a physical cross block of norm at least `L/4`; the determinant theorem gives the `|t|^-1/4` envelope. Gaussian smoothing constant is `<16`; layer cake gives `L0=4+4log16`. |
| 528–543 | pivot/volume definitions and no-pivot entry bound | PASS | From no diagonal or principal-pair pivot, `|a_ij|^2<eta^2+eta<2eta`, hence `|a_ij|<1/7`. Ordered-pair convention is used consistently. |
| 545–564 | volume-sampled interpolation | PASS | Bordered-minor identity is exact for nonsingular seeds. Each ordered extension is counted at most `(r+1)^2`; singular seeds can only make the comparison an inequality. `P` interpolation and rank are exact. |
| 566–580 | completion and rank bounds | PASS | `E` is the off-diagonal `LxL` residual, `D` is diagonal and zero on the seed. `R_LL=P_LL` has rank `<=r`; globally `R-P` is supported in rows `T` or columns `S`, giving rank `<=2r`, hence `rank R<=3r`. No symmetry of the auxiliaries is used. |
| 582–619 | no-pivot spectral-to-volume proposition | PASS | Telescoping/singular-volume case finds a small ratio. For `r=0`, operator norm is `<1`. For `r>=1`, subtracting rank `3r` forces `r+1` large diagonal entries in `L`; strict diagonal dominance of the corresponding `(r+1)` block contradicts `rank R_LL<=r`. Exact slack is `297/2800>0`. |
| 621–645 | random cut and no-pivot analytic consequences | PASS | Every ordered disjoint pair crosses a fair cut with probability `4^-k`. `Z_k^-1/(2k)<=160`; constants recompute to `12sqrt(80e)=176.959...<200` and `800e=2174.625...<2400`. |
| 646–674 | truncated half potential and two singular kernels | PASS | The near part of `J(d)` is `2 asinh(sqrt2)+pi+2 acosh(sqrt2)=7.19677...<8`; far part gives the logarithm. Rearrangement/overlap argument gives log-kernel integral `<=8`. |
| 676–714 | pivot half-potential proposition | PASS | Scalar pivot: Schur leaves one unit direction and kernel/log estimates give `<560`. Definite pair gives `<160`. Indefinite pair: hyperbolic envelope plus log-kernel and `sup D^-1/2 log_+D=2/e` gives `<444`. All conditional bounds are uniform in affine terms. |
| 716–724 | nine-eigenvalue full half-potential | PASS | Pivot branch gives truncated `<=600` plus tail `<=1`; no-pivot branch already controls the full half potential `<200`. |
| 726–749 | main theorem and scaling | PASS | No pivot uses order five. Scalar pivot leaves sixteen directions, enough for the nine-direction half-potential theorem; density `<=6010`. Definite and indefinite pair branches are below this. With `Y=KX`, `Q=(s/K^2)Qtilde`, giving the required `K^2/s` scaling. |
| 751–780 | threshold accounting and limitations | PASS | Description matches the actual proof: order five for density, order three for half potential; no claim of `s_3` theorem or global continuity. |
| 781–789 | bibliography/prior-art attribution | UNCHECKED | Attribution is not a logical dependency because the specialized inequalities used in the proof are reproved. I did not conduct a fresh literature/priority audit in this B13 run. |
| 790 | document closure | PASS | No mathematical content. |

## Support-file audit

- `README.md`: **PASS** as package description. It accurately labels the 17-eigenvalue result a candidate and the full three-eigenvalue theorem unsolved.
- `DELIVERY_STATUS.md`: **PASS as read metadata, operational inventory UNCHECKED**. I did not independently reproduce its scheduler-count inventory or local PDF rendering; those are not proof dependencies.
- `AUDIT.md`: **PASS as historical self-report, zero independent-validation weight**. Its older test counts differ from the newly delivered checker, and the package explicitly says the suites are different.
- `proof_map.csv`: **PASS**. Labels and line/proof ranges match the source read in this run.
- `SOURCE_MANIFEST.json`: **PASS** for source identification. It reports 790 lines/47,883 bytes, blob `183ccd...`, and the SHA-256 above. I independently observed the same git blob on both the pinned commit and current master. I did not independently rebuild the binary PDF.
- `verify.py`: **PASS as a finite diagnostic only**. Its exact interpolation tests check the nonsymmetric support/rank identities and bordered minors against the pinned source hash; numerical Schur/graph checks are deterministic diagnostics, not a universal certificate.
- `checks.json`: **PASS as an execution record** for the current suite: 534 exact interpolation seeds, 18 volume cases, 240 numerical Schur threshold cases, 30 graph-weight cases. It explicitly disclaims formal verification.

## Exact arithmetic spot checks

Recomputed independently during the audit:

- diagonal-dominance slack: `(1-1/16-1/100)-4(1/7+1/16)=297/2800=0.1060714285...`;
- no-pivot nine half-potential: `12 sqrt(80e)=176.959336...`;
- no-pivot seventeen density: `800e=2174.625463...`;
- scalar-pivot truncated half-potential bound: `10(20+12 log16)=532.710647...`;
- quarter-power Gaussian coefficient: `3.995259362...<16`;
- singular-kernel near-region constant: `7.196771497...<8`;
- final scalar branch: `6010<10000`.

## Review A — forward end-to-end review

I read the proof in source order and rederived each analytic transformation at the place it is introduced. The critical dependency chain is closed:

`Fourier/Gaussian/Riesz -> geometric BL -> projection/scalar powers -> decoupling/determinant -> crossing-volume envelopes -> pivot kernels -> interpolation/rank -> no-pivot consequences -> pivot half-potential -> main theorem`.

Result: **PASS**. No hidden use of post-rotation independence, moment assumptions, smooth densities, or an independent spectral remainder was found.

## Review B — reverse dependency reconstruction

Starting from the four final branches of Theorem 1, I reconstructed only the hypotheses actually needed upstream:

1. no-pivot density branch needs `s_17>=1 -> V_5>=kappa^5 -> Z_5>=4^-5 kappa^5 -> integrable exponent 5/4`;
2. scalar pivot needs Schur count `16`, then the independently proved `s_9` full half-potential and the original-coordinate square profile;
3. definite pair needs only the joint density cap of the two original coordinates and its deterministic Jacobian;
4. indefinite pair needs the original-coordinate hyperbolic envelope and one surviving Schur eigenvalue to average the moving logarithmic critical value.

I then traced each of those inputs back to its proof and checked all rank/count/constants. Result: **PASS**. This is a second end-to-end pass by the same worker, not a second independent worker review; therefore it does not by itself satisfy the owner's independent-validation release gate.

## Baseline conclusion

The pinned 17-eigenvalue manuscript passes this B13 mathematical audit. No fatal defect was found. External attribution/priority and binary-PDF rebuild are explicitly `UNCHECKED`, but neither affects the theorem proof. Independent-validation/release status remains a separate fleet gate.
