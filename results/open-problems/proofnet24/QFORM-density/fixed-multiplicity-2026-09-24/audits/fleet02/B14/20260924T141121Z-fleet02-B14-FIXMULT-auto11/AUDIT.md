# fleet02/B14 full audit — baseline 17 and rough-law review of the threshold-nine replacement

Run: `20260924T141121Z-fleet02-B14-FIXMULT-auto11`  
Objective: `QFORM-FIXED-MULTIPLICITY-AUDIT-20260924`  
Master observed during final source refresh: `0aa54bd634644b2922e9faecd003692d7f29e61e`.  
Pinned manuscript baseline: initial source commit `7c0d6e60946b19423e6400a12d34b473cf0591e2`; git blob `183ccd294763214e6a707e8d4749ff9a8cf7006d`; SHA-256 `9f3bdec0b88debe9a66076c7b4a5cc894fb14e69b89591a4107e785340f65e69`; 47,883 bytes; 790 lines. The manuscript blob is unchanged on the refreshed master.

## Verdict

**Baseline 17-eigenvalue manuscript: PASS.** I reread the complete 790-line source and all supplied package files independently. I find no fatal mathematical gap in the theorem: independent real coordinate densities bounded by `K`, arbitrary real symmetric `A` with `s_17(A)>=s>0`, and arbitrary affine `b,c` imply an essentially bounded output density. The stated `10000 K^2/s` constant is valid. This is an audit report, not a formal certificate or journal peer review.

**Package support status: PASS / previous packaging gap resolved.** `SOURCE_MANIFEST.json`, `proof_map.csv`, `verify.py`, and `checks.json` are now present. The manifest source hash agrees with the manuscript blob. `verify.py` correctly pins the source SHA and its stated finite checks; `checks.json` records a successful run (534 exact interpolation seeds, 18 volume cases, 240 numerical Schur-threshold cases, 30 graph-weight cases). I audited the checker source and output but did not treat finite execution as a substitute for the analytic proof.

**Rough-law representative issue: GAP-PRESENTATION, repaired with zero theorem impact.** The theorem assumes caps only a.e., while a few inverse-branch formulas write density values pointwise. Fix once and for all a Borel representative of each marginal, equal a.e. to the original density and clipped pointwise into `[0,K]`. This leaves every law unchanged and makes every later pointwise cap literal. More importantly, the conditional pivot arguments should be read as domination of measures against nonnegative Borel test functions, not as a choice of pointwise conditional-density versions. The compiler below makes this explicit.

**Threshold reduction: a complete multiplicity-nine proof is available after an explicit B14 regularization repair.** I independently checked the fleet02/B17 grouped physical-product Fourier argument. Its sentence leading to its displayed equation (3) compresses the mollification/Plancherel step too aggressively; as written it does not specify the probability density `rho` or the limiting argument. This is a proof-presentation gap, not a false inequality. The exact Gaussian regularization proof is supplied in the companion improvement artifact for this run. With that repair, the grouped compiler, the `E_3` density receiver, the `E_2` full half-potential receiver, and the resulting `s_9` theorem are PASS. Combining them with the sharper scalar-pivot arithmetic already present in the baseline proof yields the explicit constant

`C_9 = 2010 + 1200 log 16 = 5337.106466687737... < 5610`.

No multiplicity-eight theorem is proved here, and the unrestricted three-eigenvalue QFORM conjecture remains open.

## End-to-end source status by line range / statement

The ranges below cover the complete mathematical source. `PASS` means I reconstructed the stated implication with its exact hypotheses; `GAP-PRESENTATION` means a repair is given and no theorem hypothesis changes; `UNCHECKED` means nonlogical attribution rather than a proof dependency.

| Source lines / label | Status | Independent check and impact |
|---|---|---|
| 1–40 front matter/macros | PASS | No mathematical hypotheses hidden in formatting or notation. |
| 41–80 statement/architecture, `thm:main`, `cor:33` | PASS | Quantifiers preserve arbitrary dimension, signature, remaining spectrum, affine terms and rough product laws. The `K,s` scaling in the final proof is dimensionally correct. |
| 81–120 `lem:fourier` | PASS | Gaussian approximate identity gives Plancherel for `L1∩L2`; inversion proceeds through convolved laws and weak convergence, so it does not presuppose an output density. |
| 122–130 `lem:envelope` | PASS | Envelope integral is `2ap/(p-1)`, hence the stated Fourier inversion constant. |
| 132–160 `lem:riesz` | PASS | Gamma representation, Gaussian inversion and both Tonelli interchanges are nonnegative/absolutely majorized. Weighted `3/4` envelope integral is exactly `12 sqrt(u)`. |
| 161–181 `lem:rank` | PASS | Nonsymmetric singular-value perturbation and rank-shift inequalities have the correct index direction. |
| 183–207 `lem:schur` | PASS | Invertible case follows from inverse principal compression. In the singular approximation, if `q=N_A(t)-k`, the q-th ordered eigenvalue modulus of `S_epsilon` is at least `t-|epsilon|`; continuity of ordered moduli gives the q-th modulus of `S` at least `t`. No hidden fixed-gap assumption is needed. |
| 209–217 `lem:dd` | PASS | Strict row diagonal dominance works without symmetry. |
| 221–255 `thm:bl` | PASS | Heat-flow sign is correct; compact support gives differentiation/integration-by-parts domination; large-time Gaussian domination and small-time Lebesgue-point/Fatou steps are valid. General inputs follow by monotone approximation. |
| 258–282 `lem:projection` | PASS with representative convention | Product projection density bound uses only original product coordinates and deterministic linear changes. Rows with zero complementary weight may be dropped after choosing pointwise bounded Borel representatives. No probabilistic rotation is asserted. |
| 284–301 `lem:scalar-fourier` | PASS | Even-power reduction, Fourier inversion at zero and projection-density cap give the stated `2pi sqrt(2e)/sqrt(p)` bound. Difference densities remain cap one. |
| 310–324 `lem:decoupling` | PASS | All pre-estimate integrands have modulus at most one, so Fubini requires no moments. Difference coordinates remain independent cap-one laws. |
| 326–373 `thm:determinant` | PASS | Frame weights `c_j,d_i`, graph Jacobians, scalar Fourier exponents and entropy/regularizer cancellation were rederived; determinant exponent `-1/8` is correct. |
| 386–400 `cor:vol-fourier` | PASS | Cauchy–Binet volumes and exponents `5/4` and `3/4` are used for the correct conclusions (density versus half-potential). |
| 404–414 `lem:square` and scalar conditional profile | PASS with measure-domination reading | Inverse branches and interval-preimage length are correct. Conditional use is a nonnegative-test-function domination, not independence of the square and Schur remainder. |
| 423–434 `lem:definite` | PASS | Deterministic two-dimensional change of variables; no rotated-coordinate independence assumption. |
| 437–482 `lem:hyperbola` | PASS with measure-domination reading | Hyperbolic Jacobian, tail monotonicity and bathtub bound check out. Exceptional critical levels are handled by test-function change of variables/Tonelli, so no common pointwise exceptional set over conditioning values is required. |
| 485–525 `lem:quarter` | PASS | Random-sign crossing extraction gives norm at least `||S||/4`; Gaussian Fourier smoothing gives the quarter-power small-ball estimate; layer cake gives `L0=4+4 log16`. No support/moment assumption. |
| 528–535 `def:pivot-volume` and small-entry consequence | PASS | No-pivot `|a_ij|<1/7` follows from the principal two-by-two determinant bound. |
| 545–564 `lem:sampling` | PASS | Bordered determinant identity exact; singular deleted seeds justify inequality rather than equality; ordered multiplicity at most `(r+1)^2`. |
| 566–580 `lem:completion` | PASS | `rank R<=3r`, `R[L,L]=P[L,L]`, `rank R[L,L]<=r`, `D=0` on the seed, `E` diagonal zero all follow from the stated support decomposition; no symmetry of auxiliaries is needed. |
| 582–619 `prop:volume` | PASS | Telescoping/bad-ratio selection, singular-value perturbation, global-rank forcing and restricted-rank contradiction are consistent. Exact diagonal-dominance slack remains positive. |
| 621–630 `lem:cut` | PASS | Each ordered disjoint pair survives the fair cut with probability `4^-k`. |
| 632–645 `cor:no-pivot` | PASS | `k=3` feeds only the Riesz half-potential; `k=5` feeds the integrable Fourier density estimate. Constants check. |
| 654–674 `lem:kernels` | PASS | Near/far decomposition and centered-interval rearrangement are nonnegative Tonelli arguments; stated constants are valid. |
| 676–714 `prop:pivot-H` | PASS | Scalar, definite and hyperbolic conditional branches meet their exact hypotheses. The scalar branch actually yields `200+120 log16`; the published `600` is only a coarse rounding. |
| 716–724 `prop:nine` (baseline half-potential, not a nine-eigenvalue density theorem) | PASS | Pivot and no-pivot cases give truncated/full half-potential as stated; outside the unit window costs at most one. |
| 726–760 main proof | PASS | Four branches close; Schur spectral losses are correct; affine terms remain unrestricted; conditional bounds average by measure domination. |
| 761–780 threshold accounting/limitations | PASS | Correctly distinguishes order-five density from order-three half-potential and explicitly does not claim `s_3`. |
| 781–790 acknowledgments/bibliography | UNCHECKED (priority attribution only) | No external theorem is used as an unproved logical dependency, so bibliographic priority/completeness has no bearing on the proof audited here. |

## B14 rough-law compiler used throughout

Let `nu` be a positive finite measure on an environment space, `mu_y` a measurable probability/subprobability kernel on `R`, and `k(y,z)>=0` jointly Borel. Suppose that for `nu`-a.e. `y` and every nonnegative Borel test function `h`,

`int h(z) mu_y(dz) <= int h(z) k(y,z) dz`.

Then the mixture `mu(B)=int mu_y(B)nu(dy)` is dominated by `K(z)dz`, where

`K(z)=int k(y,z)nu(dy)`.

Proof: integrate the test-function inequality in `y` and apply Tonelli to the nonnegative right side. This avoids choosing conditional density versions and avoids any requirement for a common exceptional set in `z`.

For the manuscript the kernels are respectively

- scalar pivot: `|a|^-1/2 |z-R(y)|^-1/2` after dropping the favorable one-sided indicator;
- definite pair: the constant `pi/sqrt(|det B|)`;
- indefinite pair: `D^-1/2[6+log_+(16 sqrt(D)/|z-R(y)|)]`, interpreted as `+infinity` on the critical graph.

The critical values are Borel quadratic polynomials, and the quarter-power lemma supplies exactly the logarithmic integrability needed. Hence arbitrary translations, disconnected/countably fragmented and unbounded supports, and conditioning-generated affine terms remain admissible.

## Support files

- `README.md`: PASS as package description; it correctly distinguishes the candidate theorem from independent validation and from the open three-eigenvalue problem.
- `SOURCE_MANIFEST.json`: PASS; source blob/bytes/lines/SHA agree with the source read in this run.
- `AUDIT.md`: historical author self-report only; not used as evidence of correctness. Its mathematical inventory is consistent with the independently reconstructed source.
- `proof_map.csv`: PASS; ranges agree with the corresponding source statements/proofs.
- `verify.py`: PASS as a finite diagnostic program. Its exact assertions match the manuscript constants/rank identities and its source-hash guard pins the baseline.
- `checks.json`: PASS as a recorded execution result of that diagnostic suite; not a universal proof certificate.
- `DELIVERY_STATUS.md`: PASS as current packaging/status metadata. In particular it correctly records that the supplementary files which were absent during an earlier B14 audit are now present.

## Counterexample / barrier accounting

The multiplicity-eight endpoint is not closed by the present machinery. Three exact barriers remain valid:

1. Eight large eigenvalues do not force a physical `eta`-pivot: four direct sums of `[[0,J_m/m],[J_m/m,0]]` have exactly eight unit-modulus nonzero eigenvalues and no `eta=1/100` pivot for `m>=11`.
2. The interpolation rank count is saturated at `m=8,r=2`: abstract data can have `rank R=6`, `rank R[L,L]=2`, seed-zero diagonal `D`, and only two forced large diagonal coordinates, one short of the three-coordinate contradiction.
3. Order-two crossing cannot by itself imply bounded density for rough inputs: for independent uniforms, `U^2-V^2` has a logarithmic singularity at zero. Thus the `E_2` receiver is legitimately only a half-potential tool.

These are proof-mechanism obstructions, not counterexamples to an eight-eigenvalue theorem.

## Final audit status

- Baseline `s_17` theorem: **PASS**.
- Baseline support package: **PASS**, with former missing-file packaging issue resolved.
- Borel representative convention: **GAP-PRESENTATION**, repaired above, no theorem impact.
- B17 compressed mollification sentence in the grouped compiler: **GAP-PRESENTATION**, repaired completely in this run's improvement artifact.
- Replacement `s_9` theorem after that repair: **PASS**, with `||p_Q||_infinity <= (2010+1200 log16) K^2/s < 5610 K^2/s`.
- Multiplicity eight: **GAP / OPEN** under the full hypotheses.
- Unrestricted three-eigenvalue QFORM: **OPEN**.
