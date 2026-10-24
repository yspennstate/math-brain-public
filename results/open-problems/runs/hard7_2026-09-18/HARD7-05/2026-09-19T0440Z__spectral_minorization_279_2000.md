Model actually running: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — this is not GPT-6 at maximum, and I do not claim otherwise. HARD7-05 metric MOVED: `W_{1/4}: 1/8 -> 221/2000`, by improving the rigorous lower endpoint `L_{1/4}: 1/8 -> 279/2000`; methods B1 / B12 / B30.**

# HARD7-05 bounded research iteration — spectral minorization improves the `H=1/4` bracket

Status: **PARTIAL / source target OPEN.** This run gives a new rigorous lower bound for the exact source process at the frozen point `H=1/4`; it does not determine `theta_{2,H}` on the full source range and therefore is not source closure. It does **not** use Molchan v11 Statement 1.4 or any of the persistence-rate conclusions retracted in the preceding RECOVERY1 report.

## 1. Continuity, repository state, ownership, and source refresh

I resumed the exclusive canonical claim

`operations/claims/MOLCHAN-2025-THETA2H.md`

owned by `HARD7-05`, and the newest checkpoint

`runs/hard7_2026-09-18/HARD7-05/2026-09-19T0338Z__recovery1_statement14_orientation_refutation.md`.

Before new mathematics I reread the required controls and fleet state: `operations/hard7_2026-09-18/CONTROL.md`, `operations/NEW_METHODS_2026-09-16.md`, `operations/new_methods_2026-09-16/OWNER_DIRECTIVE.md`, `probability_campaign_2026_09/INDEX.md`, `RANKING.md`, root `POSTED.md`, `RESULTS.md`, `QUEUE.md`, the claim file, the complete indexed HARD7-05 checkpoint chain through RECOVERY1, and the newest neighboring HARD7-04/HARD7-06 reports. The large intake ledgers cannot be rendered byte-for-byte in one connector response, so the intake check was targeted through indexed queue/claim/source aliases rather than falsely represented as a literal full-file dump. No release, competing owner, posted equivalent, or canonical collision was found.

Primary source rechecked directly on 2026-09-19:

- G. Molchan, arXiv:2509.10265, current v11 (revised 4 July 2026), *Persistence probabilities for fractionally integrated fractional Brownian noise* / current PDF title header *Persistence probabilities for some processes related to ...*.

The current PDF still states on printed p. 3 that the values `theta_{2,H}` for `H != 1/2` remain unsolved. Its equation (3), already frozen at admission and reverified in RECOVERY1, gives at `H=1/4`

\[
\frac18\le \theta_{2,1/4}\le\frac14.
\tag{1.1}
\]

The key external comparison theorem rechecked directly is:

- N. D. Feldheim, O. N. Feldheim, S. Mukherjee, *Persistence and Ball Exponents for Gaussian Stationary Processes*, arXiv:2112.04820v3 (3 Apr 2025; published in CPAM). Theorem 3(II) states that for spectral measures `rho,nu in L`,
  \[
  \theta^{\ell}_{\rho+\nu}\ge \theta^{\ell}_{\rho},
  \]
  provided `rho in M` and `nu'(0)=0`.

A bounded current-literature search dated 2026-09-19 used the exact Molchan identifier/title, `theta_{2,1/4}`, `integrated fractional Brownian 1/4 persistence exponent spectral`, and `spectral measure integrated fractional Brownian persistence Feldheim`. It recovered Molchan, Feldheim--Feldheim--Mukherjee, Aurzada--Kilian, the older Molchan bounds, and numerical/adjacent persistence papers, but no exact value or the lower bound proved below. This is bounded negative evidence, **not** worldwide novelty certification.

The scheduler capability state is unchanged. GPT-6/maximum is requested only in prompt text. The exposed automation interface offers title, prompt, schedule/timing mode and enabled state, but no model selector, reasoning-effort selector, authenticated maximum-reasoning telemetry, or guaranteed execution duration. This invocation identifies as GPT-5.6 Sol and exposes no authenticated reasoning level, hence `UNVERIFIED`. A native task returning `You cannot modify this task` (the historical P26 case) is an account/workspace ownership or platform-authorization issue; the authorized remedy is the relevant owner/admin interface or platform support, not a repository edit, duplicate schedule, or permission bypass. No scheduler was modified here.

## 2. Frozen quantity — genuine movement

The fixed source metric remains

\[
W_{1/4}=U_{1/4}-L_{1/4}.
\]

After RECOVERY1 the honest verified baseline was restored to

\[
L_{1/4}=\frac18,\qquad U_{1/4}=\frac14,
\qquad W_{1/4}=\frac18.
\]

This run proves

\[
\boxed{\theta_{2,1/4}\ge \frac{279}{2000}=0.1395.}
\tag{2.1}
\]

Keeping the verified source upper bound `1/4`, the bracket becomes

\[
\boxed{\frac{279}{2000}\le\theta_{2,1/4}\le\frac14,}
\tag{2.2}
\]

and therefore

\[
\boxed{W_{1/4}:\frac18\longrightarrow\frac{221}{2000}.}
\tag{2.3}
\]

The width decreases by

\[
\frac18-\frac{221}{2000}=\frac{29}{2000}.
\]

This is a continuous-path persistence theorem. No discretely sampled path or finite-size simulation enters the proof.

## 3. B1 — change category: covariance comparison to spectral-measure comparison

The preceding route tried to compare pointwise covariances against a purported exactly soluble stationary family. RECOVERY1 showed that the required exact comparator exponent in Molchan Statement 1.4 is false as written. The new route changes category completely: compare **spectral measures**, and use Feldheim--Feldheim--Mukherjee Theorem 3 rather than Slepian covariance ordering.

For `alpha=2`, `H=1/4`, Molchan's spectral formula (current equation (6)) has `kappa=alpha+H-1=5/4`. Current Statement 1.2(a), independent of the invalid Statement 1.4 rate, identifies the source persistence exponent with that of this dual stationary process. After dividing by the density at zero, its spectral density has the exact normalized shape

\[
A(\lambda)
:=\frac{f_{2,1/4}(\lambda)}{f_{2,1/4}(0)}
=
\frac{\cosh(\pi\lambda)}{\cosh(2\pi\lambda)}
\frac{\Gamma(9/4)^2}{|\Gamma(9/4+i\lambda)|^2}.
\tag{3.1}
\]

Indeed, at `H=1/4`,

\[
\sinh^2(\pi\lambda)+\sin^2(\pi/4)
=\frac12\cosh(2\pi\lambda),
\]

and all remaining factors in Molchan's formula are independent of `lambda` and cancel in the ratio.

The comparison process is the Lamperti stationary process of integrated Brownian motion. Its variance-one covariance is

\[
J(t)=\frac{3e^{-|t|/2}-e^{-3|t|/2}}2,
\tag{3.2}
\]

whose persistence exponent is the classical `1/4`. Under time scaling `t -> c t`, its persistence exponent is `c/4`. Its spectral density is

\[
g(\lambda)=\frac{3}{2\pi(\lambda^2+1/4)(\lambda^2+9/4)},
\]

so the normalized spectral shape after time scaling is

\[
G_c(\lambda)
:=\frac{g_c(\lambda)}{g_c(0)}
=
\frac{9c^4}{(4\lambda^2+c^2)(4\lambda^2+9c^2)}.
\tag{3.3}
\]

Thus, if for some `c>1/2` we can prove

\[
A(\lambda)\ge G_c(\lambda)\qquad\forall\lambda\in\mathbb R,
\tag{3.4}
\]

then after matching the two densities at frequency zero the target spectrum is the comparator spectrum plus a nonnegative residual with zero density at the origin. That is exactly the hypothesis needed by Feldheim--Feldheim--Mukherjee.

## 4. B12 — find what is conserved: match the zero-frequency density exactly

The source spectral formula makes the right invariant visible: **the density at frequency zero**. Rather than normalize the two processes to equal variance, choose the amplitude of the Brownian comparator to match `f(0)` exactly.

Suppose (3.4) holds. Let `rho_T` be the target spectral measure with density `f_T=f_{2,1/4}`, let `rho_c` be the scaled integrated-Brownian spectral measure with density `g_c`, and define

\[
a:=\frac{f_T(0)}{g_c(0)}>0,
\qquad
\nu:=\rho_T-a\rho_c.
\tag{4.1}
\]

Then (3.4) says precisely that `nu` is a nonnegative spectral measure, and equality at `lambda=0` gives

\[
\nu'(0)=0.
\tag{4.2}
\]

The base measure `a rho_c` is in the Feldheim--Feldheim--Mukherjee class `M`, because its density at zero is finite and strictly positive. Both measures are in their class `L`: the target source itself gives `f_T(lambda)=O(|lambda|^{-7/2})`, while `g_c(lambda)=O(|lambda|^{-4})`; hence the required logarithmic moments are finite. Also `0 <= nu <= rho_T` density-wise, so `nu in L`.

At persistence level zero, multiplying a centered Gaussian process by the positive constant `sqrt(a)` does not change its sign event. Therefore Theorem 3(II) yields

\[
\theta_{2,1/4}
=\theta^0_{\rho_T}
\ge \theta^0_{a\rho_c}
=\theta^0_{\rho_c}
=\frac c4.
\tag{4.3}
\]

This step is independent of Molchan Statement 1.4. The only exact comparator exponent used is the classical integrated-Brownian exponent `1/4`.

For completeness, the source spectral duality also survives RECOVERY1: equation (7) gives the exact `H <-> 1-H` identity at fixed `kappa`. At the present point it implies `theta_{2,1/4}=theta_{3/2,3/4}`. By itself that duality only reproduces known monotonicity bounds; it does not produce (2.1). The useful conserved object here is instead the exactly matched zero-frequency spectral density in (4.1)--(4.2).

## 5. B30 — localize to one H and three surplus spectral factors

Set

\[
u=\lambda^2\ge0.
\]

The Euler products

\[
\cosh(\pi\lambda)
=\prod_{r\ge0}\left(1+\frac{4u}{(2r+1)^2}\right),
\]

\[
\cosh(2\pi\lambda)
=\prod_{r\ge0}\left(1+\frac{16u}{(2r+1)^2}\right),
\]

and

\[
\frac{\Gamma(9/4)^2}{|\Gamma(9/4+i\lambda)|^2}
=\prod_{n\ge0}\left(1+\frac{16u}{(4n+9)^2}\right)
\tag{5.1}
\]

turn (3.1) into an exact product comparison.

The Gamma factors cancel from the denominator of `cosh(2 pi lambda)` all odd indices

\[
9,13,17,21,\ldots.
\]

The remaining denominator indices are

\[
1,3,5,7,11,15,19,\ldots.
\]

The first two, `1` and `3`, are exactly the two denominator factors of the normalized integrated-Brownian spectrum at `c=1/2`:

\[
G_{1/2}(\lambda)=\frac1{(1+16u)(1+16u/9)}.
\tag{5.2}
\]

Everything left over can be paired into factors strictly larger than one. Define numerator parameters

\[
z_j=\frac{(2j+1)^2}{4},\qquad j\ge0.
\]

After removing the `1,3` poles, the sorted remaining denominator parameters are

\[
p_2=\frac{25}{16},\quad
p_3=\frac{49}{16},\quad
p_{j+2}=\frac{(4j+3)^2}{16}\quad(j\ge2).
\]

For every `j>=0`,

\[
p_{j+2}>z_j,
\tag{5.3}
\]

because the first two cases are `25/16>1/4`, `49/16>9/4`, and for `j>=2` this is simply `(4j+3)^2>(4j+2)^2`. Hence

\[
\boxed{
\frac{A(\lambda)}{G_{1/2}(\lambda)}
=
\prod_{j\ge0}
\frac{1+u/z_j}{1+u/p_{j+2}}
\ge1.
}
\tag{5.4}
\]

The key point is that we do not need the whole infinite surplus to push the Brownian time scale above `1/2`. Keep only its first three factors:

\[
S_3(u)=
\frac{(1+4u)(1+4u/9)(1+4u/25)}
     {(1+16u/25)(1+16u/49)(1+16u/121)}.
\tag{5.5}
\]

All omitted factors in (5.4) are `>=1`, so

\[
\frac{A}{G_c}
\ge S_3\frac{G_{1/2}}{G_c}.
\tag{5.6}
\]

Now take the exact rational scale

\[
\boxed{c=\frac{279}{500}.}
\tag{5.7}
\]

Using (3.3), inequality

\[
S_3(u)\frac{G_{1/2}(u)}{G_c(u)}\ge1
\tag{5.8}
\]

has only positive denominators. After cross multiplication, the left-minus-right polynomial is

\[
\frac{4u}{72748374024474225}
\Big(
80568503468621824u^4
+720742036931717120u^3
+1509103656301109008u^2
+695401501714156620u
+36667394045343
\Big).
\tag{5.9}
\]

Every displayed coefficient is strictly positive. Thus (5.8) holds for every `u>=0`, with equality only at `u=0`. Combining (5.6) and (5.8),

\[
\boxed{A(\lambda)\ge G_{279/500}(\lambda)\qquad\forall\lambda\in\mathbb R.}
\tag{5.10}
\]

This proves the spectral domination (3.4) at `c=279/500`. Substitution in (4.3) gives

\[
\boxed{
\theta_{2,1/4}\ge \frac14\frac{279}{500}=\frac{279}{2000}.
}
\tag{5.11}
\]

Together with the verified source upper bound `1/4`, this proves (2.2)--(2.3).

### Why this is not finite sampling

The only finite computation is the exact algebraic positivity of the polynomial in (5.9). The spectral inequality is for **every real frequency** and the persistence comparison is an analytic theorem for continuous stationary Gaussian processes. No grid of frequencies or sampled trajectories is being promoted to a continuum statement.

## 6. Exact finite certificate

Checker:

`artifacts/hard7_2026-09-18/HARD7-05/2026-09-19T0440Z_spectral_minorization_check.py`

creation commit:

`0e2884ee4825d35d3764c4f32977446a48527ded`

Executed output:

`artifacts/hard7_2026-09-18/HARD7-05/2026-09-19T0440Z_spectral_minorization_check.out`

creation commit:

`a286ca9334c847e8a3b748911943e6be8cf698f9`

The script was executed before archival. It checks with exact symbolic/rational arithmetic the first three parameter inequalities, the degree-five cross-multiplied polynomial and all of its positive nonconstant coefficients, and the bracket arithmetic. The archived output ends

`ALL_EXACT_CHECKS_PASS = True`.

This is a self-check of the finite algebraic core, not an independent audit of the analytic theorem.

## 7. The three required new-method moves

- **B1 — CHANGE THE CATEGORY: succeeded.** Replacing pointwise covariance/Slepian comparison by spectral-measure addition avoids the invalid exact-rate comparator from RECOVERY1. Feldheim--Feldheim--Mukherjee Theorem 3 turns a pointwise spectral minorization into a rigorous persistence lower bound.
- **B12 — FIND WHAT IS CONSERVED: succeeded after one dead end.** The source `H <-> 1-H` spectral duality alone does not improve the frozen bracket. The useful invariant is instead the density at frequency zero: matching it exactly makes the residual spectral measure have `nu'(0)=0`, the nontrivial hypothesis in Theorem 3(II).
- **B30 — ONE SCALE / ONE DIRECTION AT A TIME: succeeded.** At the single source point `H=1/4`, the exact Euler products expose a positive infinite surplus over the `c=1/2` integrated-Brownian spectrum. Keeping only the first three surplus factors already supports `c=279/500`, and the remaining continuum claim collapses to the positive polynomial (5.9).

The previous B8/B19/B26 triple was not repeated.

## 8. Scope, prior-art, and next checkpoint

What is proved here is the restricted theorem

\[
\frac{279}{2000}\le\theta_{2,1/4}\le\frac14.
\]

The full Molchan source question remains OPEN. The old special-point equalities from runs 3--6 remain retracted; this run does not restore them. In particular, it does **not** assert `theta_{2,1/4}=1/8`.

The present spectral factorization suggests a systematic next direction. The exact quotient `A/G_{1/2}` is an infinite product of factors `>1`; retaining more than three factors can support slightly larger Brownian time scales. Any next run should first ask whether a conceptual infinite-product majorization yields the optimal spectral-minorization scale, rather than merely adding more factors and another checker. If that route stalls, a different section-B triple is required by policy.

No closure is claimed and no audit request is manufactured in this run. The source target is not Section-I stuck because the fixed metric moved.

```yaml
ledger_delta:
  track: HARD7-05
  target: MOLCHAN-2025-THETA2H
  status: PARTIAL
  metric: W_1/4
  before: 1/8
  after: 221/2000
  lower_before: 1/8
  lower_after: 279/2000
  upper: 1/4
  movement: true
  methods: [B1, B12, B30]
  source_open: true
  closure: false
  self_check: PASS
  independent_audits: 0
```
