# fleet02/B19 — independent end-to-end audit, fixed-multiplicity baseline

Run: `20260924T150913Z-fleet02-B19-fixedmult-r11`  
Owner objective: `QFORM-FIXED-MULTIPLICITY-AUDIT-20260924`  
Pinned mathematical baseline: `7c0d6e60946b19423e6400a12d34b473cf0591e2`  
Pinned manuscript blob: `183ccd294763214e6a707e8d4749ff9a8cf7006d`  
Pinned manuscript SHA-256: `9f3bdec0b88debe9a66076c7b4a5cc894fb14e69b89591a4107e785340f65e69`  
Fresh master snapshot used for package/support-file reads at audit start: `e8370a03c655a2dcd76906089f81eec9565ee028`.

## Verdict

**Baseline mathematical verdict: PASS.** I read all 790 source lines and reconstructed the proof end-to-end before using later improvement artifacts. I found no fatal mathematical gap in the stated theorem

\[
 s_{17}(A)\ge s>0\quad\Longrightarrow\quad
 \|p_{X^TAX+b^TX+c}\|_\infty\le 10^4K^2/s
\]

for arbitrary independent real coordinate densities bounded by `K`, arbitrary real symmetric `A`, arbitrary signs and remaining spectrum, and arbitrary affine `b,c`.

This is an independent worker audit, not formal verification or journal peer review. It does not solve the unrestricted three-eigenvalue QFORM conjecture.

## Full source-line audit

| Source lines | Label / content | Verdict | Independent check, impact, next obligation |
|---|---|---|---|
| 1–46 | setup, definitions, abstract | PASS | Singular-value convention, essential-supremum convention, scope and stated lack of hidden regularity assumptions are consistent with later proof. |
| 47–90 | `thm:main`, `cor:33`, architecture/parameters | PASS | Quantifiers are complete; normalization target is exactly `K=s=1`; threshold accounting `9=4·3-3`, `17=4·5-3` matches later uses. |
| 91–120 | `lem:fourier` | PASS | Fourier convention, Plancherel factor `2π`, Gaussian inversion prefactor and `L^1` inversion are consistent. Approximate-identity and rough-law limiting steps are sufficient. |
| 122–130 | `lem:envelope` | PASS | Envelope integral is `2ap/(p-1)`, hence density cap `ap/[π(p-1)]`. |
| 132–160 | `lem:riesz` | PASS | Gamma/Gaussian calculation gives the stated `1/sqrt(2π)` coefficient; weighted envelope integral is exactly `12 sqrt(u)`. Tonelli uses nonnegative majorants. |
| 161–181 | singular values / `lem:rank` | PASS | Approximation-number proof works for nonsymmetric matrices and yields both perturbation and rank-shift inequalities used later. |
| 183–207 | `lem:schur` | PASS | Invertible case via inverse principal compression is valid for positive and negative thresholds; the `A+εI` passage handles singular matrices without changing the pivot in the limit. |
| 209–217 | `lem:dd` | PASS | Standard strict row diagonal dominance argument; symmetry is not needed. |
| 219–255 | `thm:bl` | PASS | Heat-flow derivative has the correct sign from the frame contraction; Gaussian tails justify integration by parts; large-time limit and small-time Fatou/monotone approximation cover rough nonnegative inputs. |
| 256–282 | `lem:projection` | PASS | Product density is integrated only in original coordinates. BL frame weights `b_i=1-|U^Te_i|^2` and `-b log b<=1-b` give cap `e^{d/2}`. No rotated-coordinate independence is asserted. |
| 284–301 | `lem:scalar-fourier` | PASS | `m=floor(p/2)>=p/4`; inversion of the `2m`-coordinate signed sum plus the projection lemma yields `2π sqrt(2e)/sqrt(p)`. Difference density cap `<=1` is correct. |
| 303–324 | `lem:decoupling` | PASS | Cauchy–Schwarz, independent copy and Jensen give powers two/four; difference coordinates remain independent and cap one. Arbitrary same-bank/affine phases are harmless. |
| 326–373 | `thm:determinant` | PASS | Checked frame identity, Jacobians, weights `c_j,d_i`, scalar Fourier exponent `2/d_i`, cancellation of `d_i`, entropy bound for `c_j`, regularizer `α=(2πe)^2`, and final determinant exponent `-1/8`. No leverage or rank assumption is smuggled in. |
| 375–400 | crossing volumes / `cor:vol-fourier` | PASS | Cauchy–Binet expansion is correct. Retaining order `k` gives exponent `k/4`; `k=5` gives `5e Z_5^{-1/10}`, `k=3` gives the stated full half-potential bound. |
| 401–422 | `lem:square` and conditional profile | PASS | Two inverse branches give the square-root profile; interval preimage length bound is correct. Conditional use is a measure-domination/Tonelli statement, not an independence claim. |
| 423–434 | `lem:definite` | PASS | Deterministic orthogonal diagonalization and polar Jacobian produce `πM/sqrt(|det B|)`; no random rotation is used. |
| 435–482 | `lem:hyperbola` | PASS | Hyperbolic coordinates have Jacobian `1/(2 sqrt D)`; tail cutoffs and one-coordinate rearrangement give the logarithmic envelope. Exceptional critical level is handled measure-theoretically. |
| 483–525 | `lem:quarter` | PASS | Diagonal branch and sign-cut cross block exhaust cases. Determinant theorem gives the quarter-power characteristic envelope; Gaussian smoothing and layer cake yield the stated concentration/log-potential constants and atomlessness. |
| 526–564 | `def:pivot-volume`, `lem:sampling` | PASS | No-pivot entry bound is correct. Bordered-minor identity is exact for nonsingular seeds. Counting extensions gives an inequality, correctly allowing singular seeds with nonsingular borders. |
| 566–580 | `lem:completion` | PASS | `D` vanishes on seed, `E` has zero diagonal, `R_LL=P_LL`, `rank R_LL<=r`, and support of `R-P` in rows `T` or columns `S` gives global `rank R<=3r`. Nonsymmetry is explicitly retained. |
| 582–619 | `prop:volume` | PASS | Telescoping/first-zero ratio is exhaustive. For `r=0` operator norm is `<1`. For `r>=1`, singular-value rank shifting forces `r+1` large diagonal entries in `L`; diagonal dominance contradicts restricted rank. Exact slack is `371/400-23/28=297/2800>0`. |
| 621–645 | `lem:cut`, `cor:no-pivot` | PASS | Every ordered disjoint `(S,T)` survives fair cut with probability `4^{-k}`. Constants are `12 sqrt(80e)=176.959...<200` and `800e=2174.625...<2400`. |
| 646–674 | `lem:kernels` | PASS | Near/far split for `J(d)` and centered-interval rearrangement for logarithmic kernel are valid nonnegative-Tonelli arguments. |
| 676–714 | `prop:pivot-H` | PASS | Scalar pivot uses Schur count plus quarter-power logarithmic potential; definite/indefinite pair branches are uniform in conditional affine terms. Truncated half-potential constant `<=600` is safe. |
| 716–724 | `prop:nine` | PASS | Pivot/no-pivot dichotomy is exhaustive; the outside-unit kernel contributes at most one, giving full half potential `<=601`. |
| 726–749 | proof of `thm:main` | PASS | No-pivot branch `<=2400`; scalar-pivot Schur leaves at least 16 directions and uses `prop:nine`, giving `6010`; definite pair `<40`; indefinite pair `<251`. Scaling `Y=KX`, `Q=(s/K^2) Q_tilde` gives exactly `10^4K^2/s`. |
| 750–790 | threshold accounting, limitations, references | PASS | Dependency summary accurately separates order-three half-potential from order-five density. Manuscript explicitly does not claim `s_3` or optimality/continuity. Bibliographic citations are antecedents only, not hidden proof dependencies. |

## Package/support-file audit

- `README.md`: **PASS**. It points to the complete 790-line manuscript and now lists the reproducibility files that are actually present.
- `SOURCE_MANIFEST.json`: **PASS**. It pins baseline commit/blob/SHA-256 and correctly labels the checker as a new scoped suite.
- `AUDIT.md`: **PASS as historical self-audit metadata**, not independent proof evidence. Its older finite-test counts differ from the new suite by design and the manifest says so explicitly.
- `proof_map.csv`: **PASS**. Statement/proof line ranges agree with the source read here.
- `verify.py`: **PASS (code audit)**. Its exact checks match the interpolation/rank/diagonal-dominance claims; its floating Schur/graph tests are diagnostics only. The variable/result name `strict_sampling_cases` is slightly misleading—it counts cases where the aggregate sampling inequality is strict, not literally “singular extensions”—but this has no mathematical impact.
- `checks.json`: **PASS as an execution record** for the supplied suite: source hash matches; 534 exact interpolation seeds, 18 volume cases, 240 Schur threshold diagnostics and 30 graph-weight diagnostics are recorded.
- **UNCHECKED**: I did not independently re-execute `verify.py` in this GitHub-only run. Therefore the recorded checker execution is source evidence, not a second execution by B19. This has no downstream effect on the analytic theorem because the proof was reconstructed symbolically.

The package gap from the earlier B19 audit is repaired: `SOURCE_MANIFEST.json`, `proof_map.csv`, `verify.py`, and `checks.json` are now present on master.

## Counterexample / adversarial stress conclusion

I found no counterexample to the 17-eigenvalue theorem. The most fragile algebraic step—the use of a nonsymmetric interpolation with global rank `<=3r` but restricted seed-complement rank `<=r`—survives direct reconstruction. The diagonal-dominance contradiction genuinely needs both ranks and the fact that `D` vanishes on the seed; replacing them by a single global rank would lose the threshold.

For lower multiplicity, a source-backed nine-eigenvalue replacement proof is audited separately in this run's improvement artifact. Its eight-eigenvalue frontier also supplies a concrete proof-interface counterexample: normalized conditional slices of a symmetrized pair need not retain a cap-one density, so an overlap-one argument cannot condition and renormalize those slices as if the original product cap were preserved.

## Status / next obligation

Baseline 17: **PASS** in this B19 end-to-end audit.  
Fatal baseline issues: **none found**.  
Formal verification: **not claimed**.  
Independent checker rerun: **UNCHECKED**.  
Next proof obligation after the source-backed nine-eigenvalue replacement is the dependence-safe order-two/overlap-one receiver required to reach multiplicity eight; no multiplicity-eight or unrestricted-three claim is made here.
