# fleet01/B19 — independent end-to-end fixed-multiplicity audit

Run: `20260924T135026Z-fleet01-B19-fixed-mult-audit`  
Objective: `QFORM-FIXED-MULTIPLICITY-AUDIT-20260924`  
Reviewer: `fleet01/B19`  
Model: GPT-5.6 Sol; effort exposure: `UNKNOWN`  
Execution/memory receiver status: `WITHOUT_VERIFIED_BRAIN`.

## Source pin

Pinned baseline source commit: `7c0d6e60946b19423e6400a12d34b473cf0591e2`.  
Fresh `math-open-problems/master` observed at sign-in: `7be6bf95889a7665c9b18182bcaedce473a75131`; fresh master observed immediately before publication: `ac4ae48ed0c94bb984c524e8c73c7fed5bacb5c6`.  
The manuscript remained byte-identical to the baseline throughout this audit: git blob `183ccd294763214e6a707e8d4749ff9a8cf7006d`, manifest SHA-256 `9f3bdec0b88debe9a66076c7b4a5cc894fb14e69b89591a4107e785340f65e69`, 47,883 bytes, 790 lines.

I read all 790 source lines in this invocation and also read the current `README.md`, `AUDIT.md`, `proof_map.csv`, `SOURCE_MANIFEST.json`, `verify.py`, `checks.json`, and `DELIVERY_STATUS.md`. The four support files that had been missing in an earlier repository state are now present. I did not substitute any peer PASS report for the reconstruction below.

## Fatal issues first

**No fatal mathematical defect found.**

Canonical-source verdict for the 17-eigenvalue theorem: **PASS** in this independent B19 reconstruction. This is one audit, not a project-level independent-validation certificate, and it does not prove the unrestricted three-eigenvalue conjecture.

### Reconciliation of the fresh concurrent `lem:schur` dispute

A fresh fleet01/B08 report labels source lines 205–207 a repairable GAP because the singular-case proof uses the moving threshold `t-|epsilon|`. I independently rechecked the exact source and classify that GAP assertion as **FALSE**: the written limiting argument is already valid.

Indeed choose any sequence `epsilon_m -> 0` such that `A+epsilon_m I` is invertible; since the pivot `B` is invertible, `B+epsilon_m I` is automatically invertible for all sufficiently large `m`. Let `S_m` be the corresponding Schur complement. Put `q=N_A(t)-k`. The source proves

`N_{A+epsilon_m I}(t-|epsilon_m|) >= N_A(t)`.

Applying the already proved invertible case at the same threshold gives

`N_{S_m}(t-|epsilon_m|) >= q`.

If `q>0`, equivalently

`s_q(S_m) >= t-|epsilon_m|`.

But `S_m -> S`, hence ordered singular/eigenvalue moduli are continuous and

`s_q(S)=lim_m s_q(S_m) >= lim_m (t-|epsilon_m|)=t`.

Therefore `N_S(t)>=q`. The elementary implication `x_m>=a_m`, `x_m->x`, `a_m->a` implies `x>=a` is exactly what is needed; no comparison of convergence rates is required. The fixed-`delta` argument in the B08 report is also valid, but it is an optional rewrite, not a repair of a defective proof.

## Complete mathematical audit, source lines 1–790

Every source line is covered. `PASS` means the displayed argument was reconstructed with its actual hypotheses, not inherited from a peer verdict.

| Source range / label | Verdict | Independent reconstruction |
|---|---|---|
| 1–35 metadata/macros | **PASS** | No mathematical premise is hidden in the setup. |
| 36–83 abstract, `thm:main`, `cor:33`, architecture | **PASS** | Quantifiers are arbitrary dimension/signature/remaining spectrum, arbitrary affine `b,c`, independent non-iid rough densities capped by `K`; conclusion is essential boundedness, not global continuity. Scaling target is `K^2/s`. |
| 84–120 `lem:fourier` | **PASS** | With `hat f(t)=int e^{itx}f(x)dx`, Plancherel is `2pi`, inversion is `1/(2pi)`, Gaussian transform is `e^{-epsilon t^2}`. The `L^2` approximate-identity and weak-limit arguments justify rough laws. |
| 122–130 `lem:envelope` | **PASS** | Integrating `min(1,(a/|t|)^p)` gives `2ap/(p-1)` and hence the displayed density constant. |
| 132–160 `lem:riesz` | **PASS** | Gamma representation, Gaussian inversion, Tonelli and the substitution in `v` yield coefficient `1/sqrt(2pi)`; the `3/4` envelope gives weighted integral `12 sqrt(u)`. |
| 162–181 norms and `lem:rank` | **PASS** | Best-rank approximation gives both nonsymmetric singular-value perturbation and rank shift exactly as used later. |
| 183–207 `lem:schur` | **PASS** | Invertible case follows from `S^{-1}` as a principal compression of `A^{-1}`, separately for positive and negative tails. The singular moving-threshold limit is valid by the explicit `s_q(S_epsilon)>=t-|epsilon|` argument above. |
| 209–217 `lem:dd` | **PASS** | Maximum-coordinate kernel-vector contradiction; symmetry unnecessary. |
| 221–255 geometric Brascamp–Lieb | **PASS** | Heat-flow differentiation gives `partial_t F-Delta F=F(sum c_i v_i^2-|sum c_i u_i v_i|^2)>=0` from the Parseval frame. Gaussian tails justify integration by parts; large-time normalization, Fatou and monotone truncation close the general nonnegative case. |
| 258–282 `lem:projection` | **PASS** | Orthogonal completion is used only in a deterministic marginal integral. Geometric BL with `b_i=1-|U^Te_i|^2` gives `prod b_i^{-b_i/2}<=e^{d/2}`. No rotated-coordinate independence is asserted. |
| 284–301 scalar Fourier powers | **PASS** | `m=floor(p/2)>=p/4`; `|hat f|^{2m}` is the integrable characteristic function of a sum of independent differences, whose density at zero is bounded via the product-projection lemma. Constants and scaling are correct. |
| 303–324 `lem:decoupling` | **PASS** | Cauchy–Schwarz in the first bank, an independent copy in the second bank, and Jensen produce the powers two and four. Difference coordinates remain independent with density cap one. Same-bank phases disappear only after legitimate modulus operations. |
| 326–373 `thm:determinant` | **PASS** | Reconstructed the regularized Parseval frame, weights `c_j,d_i`, Jacobian, graph BL application, scalar Fourier exponent `2/d_i`, cancellation of `d_i` powers, entropy-free `prod c_j^{-c_j/2}` bound and `alpha=(2pi e)^2`; fourth root gives exponent `-1/8` and argument `t^2/(pi^2 e^2)`. |
| 375–400 crossing volumes / `cor:vol-fourier` | **PASS** | Cauchy–Binet gives the elementary symmetric singular-value expansion. Order five yields integrable exponent `5/4` and `5e Z_5^{-1/10}`; order three is used with the Riesz weight and not mistaken for a direct density bound. |
| 404–414 `lem:square` and conditional profile | **PASS** | Two inverse branches give the square-root profile; interval preimage length is correct. Conditional use is measure domination via nonnegative test functions/Tonelli, not independence of the square and remainder. |
| 423–434 `lem:definite` | **PASS** | Completing the square and deterministic orthogonal diagonalization in the two-dimensional integral gives Jacobian `1/(2 sqrt(|det B|))`, hence `pi M/sqrt(|det B|)`. |
| 437–482 `lem:hyperbola` | **PASS** | Hyperbolic parametrization has absolute Jacobian `1/(2sqrt D)`. The physical-coordinate tail is monotone after the stated cutoff, the half-line rearrangement gives `3 log 2`, the middle length is controlled, and `Lambda>=2/sqrt D` yields the stated envelope. Rough densities are handled by test-function change of variables. |
| 485–525 `lem:quarter` | **PASS** | Large diagonal uses the square small-ball estimate. Otherwise random physical signs produce a cross block with norm at least `L/4`; one singular factor of the determinant theorem gives the `|t|^{-1/4}` envelope. Gaussian smoothing and layer cake give the quarter small-ball and `L_0=4+4 log16`. |
| 528–543 pivot/volume definitions and no-pivot entry bound | **PASS** | Failure of scalar and principal-pair pivots gives `|a_ii|<eta` and `|a_ij|^2<eta^2+eta<2eta`; symmetry is used exactly here. |
| 545–564 `lem:sampling` | **PASS** | The bordered determinant identity is exact. Weighting nonsingular seeds by determinant square and summing extensions counts each ordered disjoint `(r+1)` pair at most `(r+1)^2`; singular deleted seeds explain why this is an inequality. `P` has rank `<=r` and interpolates rows `S`, columns `T`. |
| 566–580 `lem:completion` | **PASS** | `E` is only the off-diagonal `LxL` residual, `D` is physical diagonal and vanishes on `S union T`, `R[L,L]=P[L,L]` has rank `<=r`. `R-P` is supported in rows `T` or columns `S`, so its rank is `<=2r` and global `rank R<=3r`. Nonsymmetry is explicitly allowed. |
| 582–619 `prop:volume` | **PASS** | Telescoping gives a bad ratio. For `r=0`, diagonal plus off-diagonal operator bounds contradict `s_m>=1`. For `1<=r<=4`, `||E||_F<=(r+1)/80<=1/16`; global rank leaves at least `r+1` diagonal entries `>=1-epsilon` in `L`; on that set `R` has diagonal `>=371/400` and each row has at most four off-diagonals `<1/7+1/16`, whose sum is `<23/28`; strict diagonal dominance contradicts `rank R[L,L]<=r`. |
| 621–645 random cut / no-pivot consequences | **PASS** | Each ordered disjoint `k`-minor survives with probability `4^{-k}`. The resulting `Z_k^{-1/(2k)}<=160` gives the stated `<200` full half-potential at order three and `<2400` density at order five. |
| 654–674 singular kernels | **PASS** | The split near `0,d` and far region yields `J(d)<=8+3 log_+(1/|d|)`; the shifted logarithmic kernel is maximized at coincident centers and integrates to 8. Tonelli applies to nonnegative kernels. |
| 676–714 `prop:pivot-H` | **PASS** | Scalar pivot: Schur retains one large direction, profile + `J` + log potential yields the displayed finite truncated half-potential. Definite pair is direct. Indefinite pair integrates the hyperbolic envelope and uses `sup D^{-1/2}log_+D=2/e`. The three pivot types are exhaustive. |
| 716–724 `prop:nine` | **PASS** | Pivot branch uses only two large directions and the preceding proposition; no-pivot branch already controls the full half-potential. Outside the truncated interval the kernel is at most one. |
| 726–749 main proof / `cor:33` | **PASS** | No-pivot `s_17` uses order five. Scalar pivot Schur retains at least 16 large directions, hence the nine-direction half-potential. Definite pair is direct; indefinite pair Schur retains at least 15 and only needs one. Normalization `Y=KX` and `Q=(s/K^2) Qtilde` gives exactly `10000 K^2/s`. |
| 751–790 threshold accounting, limitations, bibliography | **PASS mathematical / UNCHECKED priority** | The stated proof limitations are accurate, including no full-three-eigenvalue claim and no global continuity claim. Comprehensive novelty/priority is not a premise and was not re-searched in this audit. |

## Rough-law and measurability audit

**PASS.** Every probability operation conditions only original independent coordinates. Orthogonal transformations occur inside deterministic integrals or coefficient-space singular-value calculations. No moment, support, continuity, log-concavity or identical-distribution hypothesis is introduced. For pointwise uses of rough densities one may choose once and for all Borel representatives capped by the stated essential bound; changing a density on a null set does not change the law. The manuscript already makes this choice explicitly in the projection proof and elsewhere uses nonnegative test-function/Tonelli formulations. I recommend stating the representative convention once globally, but its absence is editorial, not a theorem gap.

## Support-package audit

- `README.md`: **PASS current inventory**. The formerly missing `proof_map.csv`, `SOURCE_MANIFEST.json`, `verify.py`, and `checks.json` are present on fresh master.
- `proof_map.csv`: **PASS** against the labels/ranges used in the full read.
- `SOURCE_MANIFEST.json`: **PASS consistency** for baseline commit, manuscript blob, source size/line count and listed support-file sizes.
- `verify.py`: **PASS code/read** as a finite diagnostic suite. Its exact interpolation and rational-slack assertions match the written algebra; its floating tests are diagnostics only.
- `checks.json`: **PASS as a recorded repository output / UNCHECKED as an independent rerun in this invocation**. I did not execute the exact packaged script from a local checkout, so I do not turn the recorded `PASS` into independent computational validation.
- Historical finite-test counts in the authoring `AUDIT.md`: **UNCHECKED** from the current smaller reproducibility suite. The current manifest and delivery note correctly disclose that the new suite does not reproduce those historical counts.

## Baseline verdict

**PASS** for the mathematical 17-eigenvalue theorem as written. No source patch is required for `lem:schur`; the concurrent moving-threshold GAP report is over-cautious and its proposed fixed-threshold argument is an optional clarification only. This B19 PASS is not formal verification or journal peer review, and it does not by itself satisfy the owner's two-separate-complete-review release gate.
