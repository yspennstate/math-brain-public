Model actually running: GPT-5.6 Sol. Reasoning level: UNVERIFIED; GPT-6/maximum was requested in prompt text, but this runtime exposes no authenticated GPT-6/maximum selector or reasoning telemetry. HARD7-05: **no movement** in the frozen source metric `W_{1/4}=1/8 -> 1/8`; methods tried: **B6 / B17 / B30**.

# HARD7-05 run 2 — exact tangent at the integrated-Brownian point and a low/high-frequency split

## 1. Continuity, ownership, and current-status check

This run resumed the exclusive claim `operations/claims/MOLCHAN-2025-THETA2H.md` and the previous report `2026-09-18T2041Z_admission_and_slepian_barrier.md`; it did not restart admission. The frozen source remains G. Molchan, *Persistence probabilities for fractionally integrated fractional Brownian noise*, arXiv:2509.10265v1 (12 September 2025), with target the exact one-sided integrated-fBM exponents `theta_{2,H}` for `0<H<1`, `H != 1/2`.

A fresh bounded web search on 2026-09-18/19 checked the exact title, `theta_{2,H}`, integrated-fBM persistence, and 2026 follow-ups. It again recovered Molchan 2025, Aurzada--Kilian 2022, and adjacent newer work including Zhang, arXiv:2604.01701 (Chung-type LIL/small-ball results for weighted integrated fractional processes) and Bundiuk--Mishura--Pirozzi (published 23 December 2025, prediction formulas for integrated fBM). None of the material found in this bounded search gives an exact determination of the source function `H -> theta_{2,H}`. This is negative evidence only, not a proof of worldwide openness. Repository search still finds this claim and this HARD7-05 run only; no collision was found.

The scheduler capability statement remains unchanged: prompt text can request GPT-6/maximum, but the available automation interface exposes title/prompt/schedule/timing/enabled fields, not a model or reasoning selector or guaranteed run duration. Actual model/reasoning is therefore reported above rather than inferred.

## 2. Frozen metric

The retained source-valid bracket at the tracked point is still

\[
\frac18\le \theta_{2,1/4}\le \frac14,
\qquad W_{1/4}=\frac18.
\]

No endpoint moved this run, so the metric is honestly `1/8 -> 1/8`. The work below is a structural perturbation theorem at the exactly solved anchor `H=1/2`; it does **not** by itself improve the `H=1/4` bracket and is therefore PARTIAL only.

## 3. B6 — exact first variation of the full Lamperti covariance at `H=1/2`

From run 1, with `p=2H`, `T=e^t>=1`, the variance-one Lamperti correlation is

\[
R_H(t)=\frac{p+2}{2(p+1)}T^{-(p+2)/2}
\left[
T^{p+1}+T-\frac{T^{p+2}+1-(T-1)^{p+2}}{p+2}
\right]. \tag{1}
\]

At `H=1/2` (`p=1`) this reduces to the integrated-Brownian correlation

\[
R_{1/2}(t)=\frac12\left(3e^{-t/2}-e^{-3t/2}\right)
=\frac{3T-1}{2T^{3/2}}. \tag{2}
\]

Differentiate (1) with respect to `H` and then set `H=1/2`. Exact simplification gives

\[
\boxed{
D(t):=\left.\partial_H R_H(t)\right|_{H=1/2}
=\frac{(T-1)^2}{2T^{3/2}}
\left[1-(T-1)\log\frac{T}{T-1}\right].
} \tag{3}
\]

This is not a numerical finite difference. The symbolic identity is independently checked in the archived exact checker.

### Proposition 1 — the covariance tangent is strictly positive at every nonzero lag

For every `t>0`,

\[
\boxed{D(t)>0.} \tag{4}
\]

**Proof.** Put `y=T-1>0`. The bracket in (3) is

\[
1-y\log(1+1/y).
\]

Since `log(1+x)<x` for every `x>0`, taking `x=1/y` gives `y log(1+1/y)<1`. Every other factor in (3) is positive. QED.

Thus increasing `H` through the Markov point `1/2` increases the normalized Lamperti covariance at every fixed positive lag to first order. This is stronger information than the run-1 tail exponent alone: the sign holds at **all fixed scales**, not merely asymptotically at zero or infinity.

### Proposition 2 — sharp relative size of the tangent

For every `t>0`,

\[
\boxed{
0<\frac{D(t)}{R_{1/2}(t)}<\frac16,
\qquad
\lim_{t\to\infty}\frac{D(t)}{R_{1/2}(t)}=\frac16.
} \tag{5}
\]

**Proof.** With `y=T-1` and `x=1/y`,

\[
\frac{D}{R_{1/2}}
=\frac{y^2\{1-y\log(1+1/y)\}}{3y+2}
=\frac{x-\log(1+x)}{x^2(3+2x)}.
\]

The upper bound is equivalent to

\[
F(x):=x^2(3+2x)-6\{x-\log(1+x)\}>0.
\]

Now `F(0)=0` by continuity and

\[
F'(x)=\frac{6x^2(x+2)}{x+1}>0
\]

for `x>0`. Hence `F(x)>0`. The limit in (5) follows from the Taylor expansion of `log(1+x)` at `x=0`. QED.

A useful rigorous corollary is compact-lag covariance ordering: for every `0<a<b<infinity`, continuity of `partial_H R_H(t)` and the positive minimum of `D` on `[a,b]` imply the existence of `epsilon(a,b)>0` such that

\[
R_{1/2+delta}(t)>R_{1/2}(t)
\quad(a\le t\le b,\ 0<delta<epsilon(a,b)). \tag{6}
\]

I do **not** extend (6) to all `t>=0`: uniform control in the simultaneous regimes `t downarrow 0`, `t to infinity`, `delta downarrow0` is exactly what would be required before invoking Slepian for a finite parameter interval. A first derivative at one parameter is not enough for that global conclusion.

## 4. B17 — the solved Markov anchor and what a perturbation theory would have to perturb

At `H=1/2`, let Brownian motion be `B` and define

\[
X(t)=\sqrt3\,e^{-3t/2}\int_0^{e^t}B(s)\,ds,
\qquad
Z(t)=e^{-t/2}B(e^t).
\]

Then `(X,Z)` is a stationary two-dimensional Gaussian Markov process satisfying

\[
dX_t=\left(-\frac32X_t+\sqrt3 Z_t\right)dt,
\qquad
dZ_t=-\frac12 Z_t\,dt+dW_t. \tag{7}
\]

Its generator is

\[
\mathcal L_0=
\left(-\frac32x+\sqrt3 z\right)\partial_x
-\frac12z\partial_z+\frac12\partial_{zz}. \tag{8}
\]

Killing at the boundary `x=0` is the Markov spectral formulation behind the exact integrated-Brownian persistence exponent `1/4`.

Equation (3) now supplies an exact covariance tangent for deforming away from this solvable anchor. The important obstruction is equally explicit: for `H != 1/2`, `(I_H,B_H)` is not a finite-dimensional Markov diffusion. Therefore an eigenvalue derivative of the two-dimensional killed generator (8) cannot simply be differentiated in `H`; the perturbation includes a memory kernel/infinite-dimensional Gaussian state. A successful B17 route must either produce such a Markov lift or prove a comparison/variational principle that bypasses it. This prevents a misleading finite-dimensional `generator derivative = exponent derivative` calculation.

## 5. B30 — exact low/high-frequency information in the tangent

Under the Fourier convention

\[
f(\lambda)=\frac1{2\pi}\int_{\mathbb R}R(t)e^{-i\lambda t}\,dt,
\]

the solved `H=1/2` density from (2) is rational:

\[
\boxed{
f_{1/2}(\lambda)=
\frac{3}{2\pi(\lambda^2+1/4)(\lambda^2+9/4)}.
} \tag{9}
\]

The tangent (3) has two exact scale identities.

### Low frequency: spectral density increases at zero

Set `u=e^{-t}`. The positive bracket in (3) has the convergent expansion

\[
1+\frac{1-u}{u}\log(1-u)
=\sum_{k\ge1}\frac{u^k}{k(k+1)}.
\]

Consequently

\[
\int_0^\infty D(t)\,dt
=\sum_{k\ge1}
\frac1{k(k+1)(k-1/2)(k+1/2)(k+3/2)}. \tag{10}
\]

Partial fractions give

\[
\frac1{k(k+1)(k-1/2)(k+1/2)(k+3/2)}
=\frac{4}{3(2k+3)}+\frac8{2k+1}+\frac{4}{3(2k-1)}
-\frac8{3(k+1)}-\frac8{3k}.
\]

Summing to `N` and using `H_{2N}-H_N -> log 2` yields

\[
\boxed{
\int_0^\infty D(t)\,dt
=\frac{32}{3}\log2-\frac{64}{9}
=\frac{32}{9}(3\log2-2)>0.
} \tag{11}
\]

Thus the spectral-density tangent at frequency zero is

\[
\boxed{
\left.\partial_H f_H(0)\right|_{1/2}
=\frac{32(3\log2-2)}{9\pi}>0.
} \tag{12}
\]

### High frequency / local smoothness: the second spectral moment decreases

Run 1 proved

\[
\operatorname{Var}X_H'(0)=1-H^2.
\]

For the stationary spectral measure this is exactly its second moment, so

\[
\boxed{
\left.\frac d{dH}\int_{\mathbb R}\lambda^2 f_H(\lambda)d\lambda\right|_{1/2}
=-1.
} \tag{13}
\]

Equivalently, direct expansion of (3) gives

\[
D(t)=\frac12t^2+t^3\left(\frac12\log t-\frac14\right)
+O(t^4\log t), \qquad t\downarrow0. \tag{14}
\]

The zeroth spectral moment stays equal to one because all `X_H` are variance-normalized. Equations (12)--(13) therefore give a precise scale picture: increasing `H` through `1/2` moves spectral weight toward low frequencies while reducing the second moment, and simultaneously increases the covariance at every fixed lag by Proposition 1.

This is the concrete B30 conclusion; it is not merely a numerical plot.

## 6. What this run establishes and what it does not

The frozen bracket is unchanged:

\[
[1/8,1/4]\to[1/8,1/4],\qquad W_{1/4}:1/8\to1/8.
\]

The substantive new theorem is the exact all-lag first variation (3)--(5) at the solved integrated-Brownian point, together with the exact low-frequency gain (11)--(12) and second-moment loss (13). This provides a mathematically controlled deformation direction for the next run.

It would be tempting to conclude from `D(t)>0` that `theta_{2,H}<=1/4` for all `H` just to the right of `1/2`. I explicitly do **not** claim this. Such a Slepian conclusion requires a finite-parameter covariance order `R_H(t)>=R_{1/2}(t)` simultaneously for every lag, not just a positive tangent at each fixed lag. Establishing or refuting that global order is now a well-posed next subproblem.

## 7. Verification artifact

Exact symbolic checker:

`artifacts/hard7_2026-09-18/HARD7-05/2026-09-18T2138Z_tangent_covariance_check.py`

Archived output:

`artifacts/hard7_2026-09-18/HARD7-05/2026-09-18T2138Z_tangent_covariance_check.out`

Artifact commits: `123e7ca21e7fafab0de5d5cbae8f48dc9ad80201` and `13fb9aa2cb4b8dfea5d7d36ac9349467d8f7a40d`. Readback of the output ends with `ALL_EXACT_CHECKS_PASS`.

## 8. Next route; do not repeat B6/B17/B30

Suggested next triple: **B3 / B15 / B24**.

- `B3` prove a stronger statement: attempt the finite covariance order `R_H(t)>=R_{1/2}(t)` on a nontrivial one-sided `H` interval, because that would directly feed Slepian.
- `B15` deliberately break the `H=1/2` symmetry and locate the first possible `(H,t)` where the finite covariance order fails; an exact counterexample is equally useful.
- `B24` optimize the covariance defect `Delta_H(t)=R_H(t)-R_{1/2}(t)` over `t>=0` for a fixed rational `H>1/2`, using analytic endpoint bounds plus certified interval arithmetic only if a genuine interior candidate emerges.

The immediate milestone is binary and source-relevant: either prove a global covariance-dominance interval to the right of `1/2`, yielding a rigorous new Slepian upper bound there, or produce an exact lag/H counterexample and retire that finite-comparison route.

## 9. ledger_delta

```yaml
ledger_delta:
  track: HARD7-05
  source_id: MOLCHAN-2025-THETA2H
  status: PARTIAL
  metric: W_{1/4}
  before: 1/8
  after: 1/8
  movement: no movement
  methods: [B6, B17, B30]
  new_result: "Exact positive all-lag H-tangent of normalized Lamperti covariance at H=1/2; exact zero-frequency spectral-density tangent and second spectral moment derivative"
  exact_formula: "d_H R_H(t)|_{1/2} = ((T-1)^2/(2 T^(3/2)))*(1-(T-1)log(T/(T-1))), T=e^t"
  next_methods: [B3, B15, B24]
  closure: false
```
