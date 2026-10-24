# account01/B02 r13 — complete independent audit

Objective: `QFORM-FIXED-MULTIPLICITY-AUDIT-20260924`  
Run: `20260924T142019Z-account01-B02-fixedmult-audit-r13`  
Reviewer: `account01/B02`  
Starting lens: scalar Fourier powers, convolution, product-projection constants, and exact Fourier normalizations; this report nevertheless audits the full proof end to end.

## 0. Source pin and verdict

Pinned baseline source commit: `7c0d6e60946b19423e6400a12d34b473cf0591e2`.  
Source path: `proofnet24/QFORM-density/fixed-multiplicity-2026-09-24/manuscript.tex`.  
Git blob: `183ccd294763214e6a707e8d4749ff9a8cf7006d`.  
Pinned SHA-256: `9f3bdec0b88debe9a66076c7b4a5cc894fb14e69b89591a4107e785340f65e69`.  
The same manuscript blob was re-read from current master immediately before publication; concurrent peer commits were not overwritten.

**Overall mathematical verdict on the written 17-direction theorem: PASS.** I found no FALSE statement and no fatal mathematical GAP in the 790-line source. Every mathematical source range is checked below. The theorem proved by the pinned manuscript is exactly the stated one: for independent arbitrary real coordinate laws with densities at most `K`, arbitrary real symmetric `A`, arbitrary affine `b,c`, and `s_17(A)>=s>0`, the output has an essentially bounded density with height at most `10000 K^2/s`. The manuscript does not prove the unrestricted three-direction theorem and does not claim global continuity.

**Package status: PASS with one explicitly UNCHECKED non-mathematical item.** `README.md`, `AUDIT.md`, `proof_map.csv`, `SOURCE_MANIFEST.json`, `verify.py`, `checks.json`, and `DELIVERY_STATUS.md` are now present and were read in full. The earlier missing-support-file issue is therefore closed. I checked the checker source and the internal consistency of the saved counts, but did not independently rerun the historical local LaTeX/PDF rendering or the saved Python execution environment in this invocation; those build/execution-history claims are **UNCHECKED_BY_THIS_RUN** and are not dependencies of the mathematical proof.

No previous worker PASS was used as a substitute for the reasoning below.

## 1. Line/range audit

### A01 — lines 1–46, preamble, abstract, notation and scope — PASS

The abstract matches the theorem actually proved. The use of singular values for symmetric matrices is equivalent to ordered absolute eigenvalues. No independence after spectral rotation, moment, support, log-concavity, iid, or signature assumption is inserted. The manuscript consistently claims an essential density bound, not continuity, in the pivot branches.

### A02 — lines 47–90, main statement and architecture — PASS

The quantifiers are complete: arbitrary dimension, arbitrary real symmetric `A`, arbitrary `b,c`, and independent—not identically distributed—coordinates with densities `<=K`. The normalization `K=s=1` and parameters `eta=1/100`, `kappa=1/80^2` are used consistently. The counts `9=4*3-3` and `17=4*5-3` agree with the later interpolation proposition.

### A03 — lines 91–160, `lem:fourier`, `lem:envelope`, `lem:riesz` — PASS

With the convention `hat f(t)=int exp(itx)f(x)dx`, Plancherel is

`int |hat f|^2 = 2*pi int |f|^2`,

and inversion is `(2*pi)^(-1) int exp(-itx)hat f(t)dt`. For

`g_epsilon(x)=(4*pi*epsilon)^(-1/2) exp(-x^2/(4 epsilon))`,

one has `hat g_epsilon(t)=exp(-epsilon t^2)`. The Gaussian identity in (2.3) therefore has the correct factor `1/(2 sqrt(pi v))` and exponent `-t^2/(4v)`.

For the Riesz estimate, the gamma representation and the substitution `w=t^2/(4v)` give

`int_0^infinity v^(-5/4) exp(-t^2/(4v)) dv = sqrt(2) Gamma(1/4)|t|^(-1/2)`.

After the Gaussian Fourier prefactor and `Gamma(1/4)` cancellation, the coefficient is exactly `1/sqrt(2*pi)`. The weighted envelope integral is exactly `12 sqrt(u)`. The power-envelope inversion constant is also correct: the `L^1` envelope is `2ap/(p-1)`, hence the density cap `ap/[pi(p-1)]`.

### A04 — lines 161–217, singular values, Schur spectral count, diagonal dominance — PASS

The approximation-number proof of the singular-value perturbation and rank shift is valid for nonsymmetric matrices. In `lem:schur`, for invertible `A`, the complementary block of `A^{-1}` is `S^{-1}`. Principal-compression interlacing applied separately to `A^{-1}` and `-A^{-1}` gives the count of inverse eigenvalues of absolute value `>t^{-1}`, which is precisely the count of original eigenvalues of modulus `<t`; therefore `N_S(t)>=N_A(t)-k`. The singular case is correctly obtained by an `A+epsilon I` approximation while retaining pivot invertibility along a sequence. Strict row diagonal dominance proves invertibility without symmetry.

### A05 — lines 218–301, geometric Brascamp–Lieb, product projections, scalar Fourier powers — PASS

The heat-flow calculation gives

`partial_t F-Delta F = F[sum c_i v_i^2-|sum c_i u_i v_i|^2] >=0`

because the frame matrix with columns `sqrt(c_i)u_i` is a contraction. The heat-kernel tail bounds justify integration by parts, and the `t->infinity` limit is the product of one-dimensional masses because `sum c_i=d` and `sum c_i(u_i dot z)^2=|z|^2`. The `t downarrow 0` Fatou step is legitimate almost everywhere.

For the projection lemma, if `U^T U=I_d` and `W` is an orthogonal complement, the row quantities `b_i=|w_i|^2=1-|U^T e_i|^2` form the required rank-one frame. Brascamp–Lieb gives the factor `prod b_i^(-b_i/2)`; `-b log b<=1-b` and `sum_i(1-b_i)=d` yield the cap `e^(d/2)`. Scaling the one-dimensional unit projection gives `sqrt(e)/|a|`.

For `lem:scalar-fourier`, `m=floor(p/2)>=p/4`, and `|hat f|^p<=|hat f|^(2m)`. The latter is the characteristic function of a sum of `m` independent differences. It is integrable because it is bounded by `|hat f|^2`. The sum has a density at zero bounded by the projection lemma applied to `2m` original signed coordinates, whose coefficient norm is `sqrt(2m)`. Thus

`int |hat f|^p <= 2*pi*sqrt(e)/(sqrt(2m)) <= 2*pi*sqrt(2e)/sqrt(p)`.

The convolution difference density satisfies `f*tilde f<=1` pointwise. No sharp Hausdorff–Young or extremizer theorem is being assumed.

### A06 — lines 302–400, decoupling, regularized determinant, crossing volumes — PASS

The two-copy decoupling is correctly done across original-coordinate banks. The difference coordinates remain independent and cap one. Jensen changes the squared bound into the fourth-power bound without changing product provenance.

For the regularized determinant, setting `a=2t`, `alpha=(2*pi*e)^2`, and `H=alpha I+a^2 M^T M` gives the exact frame

`sum_j alpha H^(-1/2)e_j e_j^T H^(-1/2) + sum_i a^2 H^(-1/2)m_i m_i^T H^(-1/2)=I`.

The Brascamp–Lieb weights are `c_j=alpha e_j^T H^-1 e_j` and `d_i=a^2m_i^T H^-1m_i`. The coordinate changes contribute `alpha^(c_j/2)c_j^(-c_j/2)` and `d_i^(-d_i/2)` exactly. `g_j<=1` gives `||g_j||_(1/c_j)<=1`, while the scalar Fourier-power lemma at `p=2/d_i` gives `(2*pi*sqrt(e d_i))^(d_i)` after taking the appropriate norm. The `d_i` powers cancel. The inequality `prod c_j^(-c_j/2)<=e^(theta/2)` supplies the remaining factor needed to cancel `sqrt(alpha)^theta= (2*pi*e)^theta`. Fourth roots then yield

`|phi_Z(t)| <= det(I+t^2 M^T M/(pi^2 e^2))^(-1/8)`.

Cauchy–Binet gives the stated `Z_k` coefficients. Retaining the order-`k` term produces exponent `k/4`; for `k=5`, inversion gives `5e Z_5^(-1/10)`, and for `k=3`, the Riesz estimate gives `12 sqrt((e/2) Z_3^(-1/6))`.

### A07 — lines 401–525, square, definite pair, hyperbolic pair, quarter-power concentration — PASS

The scalar-square density and interval-preimage length are correct after completing the square. The conditional profile

`p_Q(z)<=|a|^(-1/2) E|z-R|^(-1/2)`

is a measure-domination statement and does not assert independence between the square center and `R`.

For a definite two-coordinate quadratic, deterministic orthogonal diagonalization is used only inside the two-dimensional integral; the Jacobian in `(delta,theta)` is `1/(2 sqrt(det B))`, giving the `pi M/sqrt(det B)` density cap.

For an indefinite pair, the hyperbolic parametrization has Jacobian `1/(2 sqrt(D))`. The tail argument uses one original coordinate at a time and only its cap/mass, not independence after eigenvector rotation. The middle interval and tail cutoffs give the displayed logarithmic envelope; `Lambda>=2/sqrt(D)` has the correct direction.

For `lem:quarter`, either a large original-coordinate diagonal gives a square-root small-ball bound, or a random sign partition extracts a literal original-coordinate cross block of norm at least `L/4`. Retaining one singular value in the determinant theorem gives `|phi_R(t)|<=(4*pi*e/(L|t|))^(1/4)`. Gaussian smoothing at `v=1/8` yields the coefficient

`2^(5/8) pi^(-1/4) e^(3/8) Gamma(3/8)`,

and the manuscript's elementary estimate really gives the stronger bound `<40/3<16`. Layer cake gives `4+4 log 16` as written. No atoms follow by sending the small-ball radius to zero.

### A08 — lines 526–645, disjoint minors, interpolation, completion, spectral-to-volume, random cut — PASS

No pivot implies `|a_ii|<eta` and `|a_ij|^2<eta^2+eta<1/49`, hence `|a_ij|<1/7`. In `lem:sampling`, the bordered determinant formula is exact. Singular seeds are omitted from the probability law but can have nonsingular extensions, so the aggregate count is correctly an inequality. Each ordered disjoint `(r+1)` pair is counted at most `(r+1)^2` times.

In `lem:completion`, `E` is supported on the off-diagonal part of `LxL`, `D` is diagonal and vanishes on the seed, and `R_LL=P_LL`, so `rank R_LL<=r`. Globally `R-P` is supported in rows `T` or columns `S`; splitting those two supports gives `rank R<=3r`. Symmetry of `R,P,E` is neither stated nor needed.

In `prop:volume`, a bad volume ratio gives `||E||<=||E||_F<=(r+1)/80<=1/16`. With `m=4k-3>=4r+1`, rank subtraction through the global `3r` bound forces at least `r+1` large diagonal entries of `D`; they lie in `L`. On those indices, the diagonal entries of `R` are at least `371/400`, whereas each off-diagonal is `<1/7+1/16`. Since `r<=4`, the off-diagonal row sum is `<23/28<371/400`, so the `(r+1)x(r+1)` restricted block is invertible, contradicting `rank R_LL<=r`. The `r=0` branch also closes because `||diag A||+||off A||_F<1`.

The fair coordinate cut includes an ordered disjoint `k,k` minor with probability exactly `4^(-k)`, so `E Z_k=4^(-k)V_k`.

### A09 — lines 646–724, kernels, pivot half-potentials, nine-direction half-potential — PASS

For `J(d)`, the near region scales to the explicitly evaluated beta/hyperbolic integral `<8`; on the far region `|x-d|>=|x|/2`, giving the stronger bound `2 sqrt(2) log_+(1/(2|d|))`, hence the manuscript's rounded `3 log_+(1/|d|)`. The logarithmic kernel is maximized by aligning the interval superlevel sets at zero and equals at most `8`.

For a scalar pivot in `prop:pivot-H`, Schur leaves one large direction. The conditional square profile followed by Tonelli produces `E J(R-a)`. The quarter-power lemma excludes the singular atom and controls its logarithm. Definite and indefinite pair pivots have the stated conditional bounds. The scalar, definite, and indefinite cases exhaust the pivot definition.

For `prop:nine`, the no-pivot branch already has the full half-potential `<200`; the pivot branch supplies only the truncated half-potential `<=600`, and the tail `|Q-a|>1` contributes at most one. Thus the full bound is `<=601` exactly where the final scalar pivot needs it.

### A10 — lines 725–749, main theorem and scaling — PASS

No-pivot `s_17` invokes order five and gives `<2400`. A scalar pivot leaves at least sixteen large Schur directions, hence at least nine, and the full Schur half-potential bound gives `6010`. A definite pair gives `<40`; an indefinite pair leaves at least fifteen directions, so in particular its Schur complement has operator norm at least one and the logarithmic estimate gives `<251`.

For general `K,s`, `Y=KX` has coordinate densities bounded by one and

`Q=(s/K^2) [Y^T(A/s)Y+(K/s)b^T Y+(K^2/s)c]`.

Density scaling therefore gives `10000 K^2/s`. Arbitrary affine terms survive unchanged in scope.

### A11 — lines 750–790, threshold accounting, regularity remarks, bibliography — PASS

The threshold explanation correctly distinguishes global rank `<=3r` from restricted rank `<=r`. The order-five Fourier exponent `5/4` is integrable; order three has exponent `3/4` and is used only after multiplying by the Riesz weight `|t|^-1/2`. The regularity remark is accurate: the no-pivot branch has an `L^1` characteristic function and hence a continuous density, while the pivot branches establish only essential boundedness by measure domination.

## 2. Support-package audit

### P01 — `README.md` — PASS

It now accurately lists all package files and distinguishes the committed LaTeX source from the separately delivered PDF binary. It correctly states that the 17-direction result is a candidate with review gate under review, not the full three-direction conjecture.

### P02 — historical `AUDIT.md` — PASS AS SELF-REPORT ONLY

Its mathematical dependency list agrees with the source, but by its own terms it is authoring-agent evidence, not independent validation. I did not use its PASS as evidence for A01–A11.

### P03 — `proof_map.csv` — PASS

The statement/proof ranges agree with the source labels: `lem:fourier` 91–120, `lem:riesz` 132–160, `thm:determinant` 326–373, `lem:sampling` 545–564, `lem:completion` 566–580, `prop:volume` 582–619, `prop:pivot-H` 676–714, `prop:nine` 716–724, and the main proof 726–749, with the other listed ranges also matching.

### P04 — `SOURCE_MANIFEST.json` — PASS FOR SOURCE METADATA; PDF EXECUTION CLAIM UNCHECKED_BY_THIS_RUN

The manifest pins the expected baseline commit, git blob, 47,883 bytes, 790 lines, and SHA-256 stated above. The current repository copy of `manuscript.tex` has the pinned git blob. I did not independently reproduce the historical three-pass PDF build/render in this invocation.

### P05 — `verify.py` and `checks.json` — PASS FOR CODE/OUTPUT CONSISTENCY; HISTORICAL EXECUTION UNCHECKED_BY_THIS_RUN

The checker verifies the pinned source hash before tests. Its exact loops check interpolation support/ranks/bordered determinants and aggregate sampling; its numerical diagnostics check Schur counts and graph weights. The saved output counts—534 interpolation seeds, 18 aggregate volume cases, 240 Schur threshold cases and 30 graph-weight cases—are consistent with the source loops, and the exact diagonal-dominance slack is `297/2800>0`. These finite diagnostics do not replace the analytic proof. I did not independently rerun the historical Python environment in this invocation.

## 3. Urgent defects

**None found.** There is no mathematical FALSE or fatal GAP to publish from the pinned 17-direction manuscript.

## 4. Independent audit of the new nine-direction replacement proof

After completing the baseline reconstruction, I independently checked the complete threshold-nine replacement argument in `improvements/account03/B04/20260924T121940Z-account03-B04-fixedmult-audit-r1/REPORT.md`, blob `054facef834d29927713c5d42a1f09a541c5644b`.

Verdict: **PASS**.

The new grouped product-Fourier compiler is sound. Pushing the hub phase to a physical `k`-dimensional projection gives a complex density `a_t` with `|a_t|<=p_W`, hence `||a_t||_2^2<=M_H`; Plancherel at scale `2t` gives `M_H(pi/|t|)^k`. The light-bank `L^2` square can be mollified, expanded with one independent copy of the physical `J` bank, and reduced to the product difference vector `D=X_J-X'_J`; all pure same-bank phases either cancel or have modulus one. Weighted Holder over `ell`-subsets is then applied to the original-coordinate product law. The map combining `M_JD` with the residual rows has Gram determinant `S^2 det(C_T C_T^T)`, so the baseline projection lemma gives the required density cap. Scalar Fourier powers at `p=1/alpha_i` are legal because the diffuse branch has `alpha_i<=1/2`. Zero-marginal rows may simply be omitted. The entropy inequality

`H(w)+sum_i alpha_i log alpha_i <= ell log ell-log(ell!)`

follows by uniformly ordering the sampled `ell`-subset and applying entropy subadditivity. These steps give the stated `|t|^{-(k+ell)/2}` envelope with its constants.

The row-promotion identities in the `E_3` and `E_2` receivers are exact Gram–Schmidt identities, not heuristic local-minor selections. Consequently any literal original-coordinate cross block with `E_3(M)>0` has

`||p_Q||_infinity <= C_3 E_3(M)^(-1/6)`,  
`C_3=3 sqrt(2)e(9/2)^(1/6)=14.818337662843...`,

and any such block with `E_2(M)>0` has the half-potential bound

`sup_a E|Q-a|^-1/2 <= C_2 E_2(M)^(-1/8)`,  
`C_2=8 sqrt(e)2^(-1/8)=12.095072570796...`.

With `s_9(A)>=1`, the no-pivot structural theorem at order three gives a fair-cut block with `E_3>=4^-3 kappa^3`, hence density `<160 C_3<2400`. At a scalar pivot the Schur complement retains eight directions. If it has a pivot, the baseline pivot half-potential theorem applies; if it has no pivot, `s_5>=1`, order-two structure gives `E_2>=4^-2 kappa^2`, and the new receiver gives full half-potential `<153`. Pair pivots are already paid. Thus the nine-direction theorem closes with the original `6010 K^2/s` constant, and the improvement file accompanying this audit sharpens that constant further.

A genuinely separate worker, account01/B16, previously published a complete independent reconstruction PASS for the same nine-direction candidate at commit `54ec2a651d854563f8db0d92c4c3426f76551786`. This B02 audit is a second separate complete review. Therefore the **two-independent-complete-review evidence condition is now met for the mathematical nine-direction candidate** (B16 plus this B02 report). I do not self-award a release/formal-verification certificate: owner-level reconciliation and any concurrent conflicting findings remain separate gates.

## 5. How far the multiplicity was lowered in this run

The accompanying improvement proves the stronger candidate

` s_9(A)>=s  ==>  ||p_Q||_infinity <= 4880 K^2/s.`

I did not prove an eight-direction theorem. The current exact eight-direction structural reduction shows that, in the remaining no-pivot chamber, either the order-three volume branch is already paid or one obtains a quantitative overlap-one/two-sided physical collar. A general product-preserving density receiver for that zero/near-zero common-diagonal collar is still missing. Thus **9 is the lowest complete theorem proved and fully reconstructed in this run; 8 remains an explicit unresolved receiver problem rather than a completed theorem.**

No claim about the unrestricted three-eigenvalue conjecture is made.

## 6. Review labels summary

- Baseline manuscript mathematical source, lines 1–790: **PASS**.
- Baseline theorem `s_17`: **PASS** in this independent review.
- Support files now present: **PASS** for content/source consistency.
- Saved checker historical execution and compiled-PDF render reproduction: **UNCHECKED_BY_THIS_RUN**, non-mathematical and nonessential to the proof.
- Mathematical FALSE findings: **none**.
- Fatal mathematical GAP findings: **none**.
- Nine-direction replacement proof: **PASS** in this second separate complete review.
- Eight-direction theorem: **UNCHECKED/OPEN AS A THEOREM** because the terminal collar receiver is not proved.

Model: GPT-5.6 Sol. Effort/reasoning telemetry: UNKNOWN/not exposed.
