Model actually running: **GPT-5.6 Sol. Reasoning level: UNVERIFIED** — this is **not GPT-6 at maximum**; no authenticated runtime reasoning-effort telemetry or binding model/effort selector is exposed.

# I0048 admission-side refinement: affine normalization obstruction and exact exponent-matched threshold classification

Date: 2026-09-19 UTC  
Worker: R7-05  
Native ID: `6aabe805f32881919992996e1c5cfad6`  
Repository: `yspennstate/math-open-problems`, branch `master`

## 1. Status and purpose

This is **admission-side mathematics**, not an admission or claim of I0048. A neighboring R08 report already reconciled van der Hofstad's old Saint-Flour Open Problem 4.3 at the critical-threshold level: the fixed-outdegree affine preferential-attachment threshold is now known from Hazra--van der Hofstad--Ray, and the conditionally-independent/Bernoulli preferential-attachment threshold is known from the Dereich--Mörters / Eckhoff--Mörters--Ortgiese framework. R08 also gave one exact same-power-law-exponent example with unequal positive thresholds.

The purpose here is to remove a remaining normalization ambiguity in that comparison and derive a sharp all-parameter classification inside the standard affine Bernoulli/variable preferential-attachment class.

The resulting conclusions are:

1. for `m>=2, delta>0`, the standard affine conditionally-independent model cannot simultaneously match **both** the fixed model's power-law exponent and its asymptotic edge density, because the source class requires `f(0)=beta<=1`;
2. after matching the canonical power-law exponent, for every `m>=3` the fixed-outdegree model has strictly **smaller** positive bond-percolation threshold than every admissible affine conditionally-independent model;
3. for `m=2` there is one sharp crossover `delta_* ~= 1.01208790493121`; below it there is a unique admissible intercept `beta_*(delta)` giving equal thresholds, at it equality occurs only at `beta=1`, and above it the fixed-outdegree threshold is strictly smaller for every admissible `beta<=1`.

These are exact consequences of later-known threshold formulas. Novelty is **UNVERIFIED** and no source-level open problem is claimed solved by this worker.

## 2. Source scope and model formulas

Historical intake I0048 records Remco van der Hofstad's Saint-Flour Open Problem 4.3: investigate the percolation phase transition on affine `PA(m,delta)` and ask whether the results are identical to those for preferential attachment with conditionally independent edges.

Later primary work:

- Rajat Subhra Hazra, Remco van der Hofstad, Rounak Ray, *Percolation on preferential attachment models*, arXiv:2312.14085, Electronic Journal of Probability 31 (2026), DOI `10.1214/26-EJP1557`.
- Maren Eckhoff, Peter Mörters, Marcel Ortgiese, *Near Critical Preferential Attachment Networks have Small Giant Components*, Journal of Statistical Physics 172 (2018), 609--638, DOI `10.1007/s10955-018-2054-5`.
- Joost Jorritsma, Júlia Komjáthy, *Weighted distances in scale-free preferential attachment models*, Random Structures & Algorithms 57 (2020), 823--859, DOI `10.1002/rsa.20947`; its model section explicitly places fixed-outdegree FPA beside conditionally-independent VPA/GVPA, assumes `f(0)<=1`, and compares these families through their power-law exponent.

For fixed-outdegree affine preferential attachment with `m>=2` and `delta>0`, write

`A = m+delta`.

The now-known bond-percolation threshold is

`p_F(m,delta) = delta / [2 ( m(m+delta) + sqrt(m(m-1)(m+delta)(m+delta+1)) )].`   (2.1)

Its power-law exponent is

`tau_F = 3 + delta/m.`   (2.2)

For the standard affine conditionally-independent/Bernoulli model with

`f(k)=gamma k + beta`, `0<beta<=1`, `0<=gamma<1/2`,

the power-law exponent is

`tau_B = 1 + 1/gamma`,   (2.3)

and Eckhoff--Mörters--Ortgiese compute the branching spectral radius at its minimizer as

`rho_* = [ beta + sqrt(beta^2 + beta gamma) ] / (1/2-gamma).`   (2.4)

Bond percolation multiplies the mean operator by `p`, hence the spectral critical value is

`p_B(gamma,beta) = 1/rho_*`

`= (1/2-gamma) / [ beta + sqrt(beta^2+beta gamma) ].`   (2.5)

If the value in (2.5) exceeds one, the unpercolated graph is itself below the giant-component threshold; this only strengthens the comparisons below.

Matching the canonical power-law exponent forces one and only one slope:

`gamma = m/(2m+delta).`   (2.6)

For `delta>0`, this indeed lies in `(0,1/2)`.

## 3. Method B2 — negate a two-invariant calibration

A tempting interpretation of "identical results" is to compare a fixed-outdegree model and a conditionally-independent model having both the same tail exponent and the same asymptotic number of edges created per arriving vertex. In the standard affine VPA/BPA source class this calibration is impossible in the positive-threshold regime.

### Lemma 3.1 — exact asymptotic edge density of affine BPA

Use the current-book convention in which, at time `n`, the new vertex connects independently to each old vertex `v` with probability

`f(D_v^{in}(n-1))/(n-1)`.

Let `E_n` be the number of directed edges and `e_n=E[E_n]`. Since the sum of indegrees equals `E_{n-1}`,

`E[E_n-E_{n-1} | F_{n-1}]`

`= [ gamma E_{n-1} + beta(n-1) ]/(n-1)`

`= gamma E_{n-1}/(n-1) + beta.`

Therefore

`e_n = (1+gamma/(n-1)) e_{n-1} + beta.`   (3.1)

Set

`lambda = beta/(1-gamma)`

and `u_n=e_n-lambda n`. Since `gamma lambda + beta=lambda`, (3.1) gives the exact homogeneous recurrence

`u_n = (1+gamma/(n-1)) u_{n-1}.`   (3.2)

Hence

`u_n = O(n^gamma)`

and

`e_n/n -> lambda = beta/(1-gamma).`   (3.3)

The alternative common indexing with denominator `n` changes only the lower-order recurrence and gives the same limiting density.

### Theorem 3.2 — normalization obstruction

Suppose an affine BPA is required to match the FPA exponent (2.2). Then (2.6) holds, so by `beta<=1`,

`lambda_B = beta/(1-gamma)`

`<= 1/(1-gamma)`

`= (2m+delta)/(m+delta).`   (3.4)

The fixed model creates exactly `m` new edges per arriving vertex. For `m>=2` and `delta>0`,

`m - (2m+delta)/(m+delta)`

`= [m(m-2)+(m-1)delta]/(m+delta)`

`> 0.`   (3.5)

Thus no admissible affine BPA can match both the exponent and edge density.

Equivalently, the intercept formally required to match edge density is

`beta_density = m(1-gamma)`

`= m(m+delta)/(2m+delta),`   (3.6)

and

`beta_density - 1`

`= [m(m-2)+(m-1)delta]/(2m+delta)`

`>0.`   (3.7)

So the would-be two-invariant calibration exits the standard source class exactly because `f(0)=beta` would exceed one.

This is important for interpreting any threshold comparison: for `m>=2, delta>0`, same-exponent FPA and standard affine BPA necessarily also differ in edge density. One must not claim to have isolated the effect of conditional independence while holding every first-order density invariant fixed.

## 4. Method B11 — dualize threshold equality into a one-variable spectral equation

At fixed `gamma`, formula (2.5) is strictly decreasing in `beta`, because

`beta + sqrt(beta^2+beta gamma)`

is strictly increasing. Therefore among admissible `0<beta<=1`, the **smallest** BPA percolation threshold is attained at `beta=1`.

This turns the existence of any exponent-matched BPA with threshold equal to `p_F` into a one-dimensional extremal test.

Define

`gamma_m(delta)=m/(2m+delta).`

At `beta=1`, (2.5) simplifies to

`p_B,min(m,delta)`

`= delta / { 2 [ (2m+delta) + sqrt((2m+delta)(3m+delta)) ] }.`   (4.1)

The fixed threshold (2.1) is

`p_F(m,delta)`

`= delta / { 2 [ m(m+delta) + sqrt(m(m-1)(m+delta)(m+delta+1)) ] }.`   (4.2)

### Theorem 4.1 — for every m>=3, FPA is strictly more robust than every exponent-matched affine BPA

Let

`D_F = m(m+delta) + sqrt(m(m-1)(m+delta)(m+delta+1))`,

`D_B = (2m+delta) + sqrt((2m+delta)(3m+delta)).`

For `m>=3`, the non-square-root terms satisfy

`m(m+delta)-(2m+delta)`

`= m(m-2)+(m-1)delta >0.`   (4.3)

For the square-root terms, the difference of the squared radicands is

`m(m-1)(m+delta)(m+delta+1) - (2m+delta)(3m+delta)`

`= m^2(m^2-7)`

`  + m(2m+3)(m-2) delta`

`  + (m^2-m-1) delta^2.`   (4.4)

Every coefficient on the right is positive for `m>=3`. Hence both summands of `D_F` are strictly larger than the corresponding summands of `D_B`, so

`D_F>D_B.`

Since the numerators in (4.1)--(4.2) are equal and positive,

`p_F(m,delta) < p_B,min(m,delta).`   (4.5)

Monotonicity in `beta` now gives the stronger all-intercept statement

`boxed:  p_F(m,delta) < p_B(gamma_m(delta),beta)`

for every `m>=3`, `delta>0`, and every admissible `0<beta<=1`.   (4.6)

Thus no standard affine BPA with the same degree exponent can have the same numerical positive threshold when `m>=3`; the fixed-outdegree model is strictly more robust to bond deletion in this comparison.

## 5. The exceptional m=2 case and a sharp crossover constant

For `m=2`, the termwise proof above no longer works and there is a genuine crossover.

With exponent matching `gamma=2/(4+delta)`, the two extremal thresholds are

`p_F(2,delta)`

`= delta / { 2 [ 2delta+4 + sqrt(2(delta+2)(delta+3)) ] },`   (5.1)

and

`p_B,min(2,delta)`

`= delta / { 2 [ delta+4 + sqrt((delta+4)(delta+6)) ] }.`   (5.2)

Equality is equivalent to

`delta + sqrt(2(delta+2)(delta+3))`

`= sqrt((delta+4)(delta+6)).`   (5.3)

Squaring (5.3) once yields

`6 = delta^2 + delta sqrt(2(delta+2)(delta+3)).`   (5.4)

Any positive solution therefore has `delta<sqrt(6)`, so the remaining square root may be isolated without a sign ambiguity. Squaring a second time gives

`q(delta) := delta^4 + 10delta^3 + 24delta^2 - 36 = 0.`   (5.5)

For `delta>0`,

`q'(delta)=4delta^3+30delta^2+48delta>0`,

while `q(0)=-36` and `q(sqrt(6))>0`. Hence (5.5) has exactly one positive root, and because that root is below `sqrt(6)` the squaring steps are reversible.

Define

`delta_* = unique positive root of delta^4+10delta^3+24delta^2-36=0`

`          = 1.01208790493121... .`   (5.6)

Direct endpoint comparison gives

- `0<delta<delta_*`: `p_B,min(2,delta) < p_F(2,delta)`;
- `delta=delta_*`: equality at `beta=1`;
- `delta>delta_*`: `p_F(2,delta) < p_B,min(2,delta)`.

Because `p_B(gamma,beta)` is strictly decreasing in `beta`, this already classifies equality with **all** admissible affine BPA intercepts.

### The unique equality intercept below delta_*

Let

`p=p_F(m,delta)`, `gamma=gamma_m(delta)`,

and

`C=(1/2-gamma)/p.`

Solving

`beta + sqrt(beta^2+beta gamma)=C`

is elementary: after isolating the square root,

`beta_* = C^2/(gamma+2C).`   (5.7)

For the FPA threshold,

`C = D_F/(2m+delta),`

so equivalently

`beta_*(m,delta)`

`= D_F^2 / [ (2m+delta)(m+2D_F) ].`   (5.8)

For `m=2`:

- if `0<delta<delta_*`, then `0<beta_*(2,delta)<1`, and it is the unique admissible intercept with `p_B=p_F`;
- if `delta=delta_*`, then `beta_*=1`;
- if `delta>delta_*`, then `beta_*>1`, so no admissible equality exists.

Moreover, when `0<delta<delta_*`, monotonicity gives the full sign classification:

`beta<beta_*  => p_B>p_F`,

`beta=beta_* => p_B=p_F`,

`beta>beta_* => p_B<p_F`.

This sharpens the neighboring R08 single witness into an exact phase diagram for all standard affine same-exponent comparisons.

## 6. Method B5 — parameter deformation and why m=2 is special

The forbidden intercept needed to match both exponent and edge density is

`beta_density(m,delta)=m(m+delta)/(2m+delta).`

Differentiating in `delta` gives

`d beta_density / d delta = m^2/(2m+delta)^2 >0.`   (6.1)

At `delta=0`,

`beta_density(m,0)=m/2.`

Therefore:

- for `m>=3`, the two-invariant calibration is already outside the source class at the robustness boundary `delta=0`, and moves farther outside as `delta` increases;
- for `m=2`, `beta_density(2,0)=1` sits exactly on the admissible boundary, but every `delta>0` pushes it outside. This is the only fixed-outdegree `m>=2` case that touches the standard BPA normalization at the transition point.

The maximum same-exponent BPA edge density is

`lambda_max=(2m+delta)/(m+delta)=1+m/(m+delta),`

so its deficit relative to the FPA edge density is

`Delta_edge(m,delta)`

`= m-lambda_max`

`= [m(m-2)+(m-1)delta]/(m+delta).`   (6.2)

For fixed `m`,

`d Delta_edge / d delta = m/(m+delta)^2 >0.`   (6.3)

Thus the density mismatch increases monotonically as one moves deeper into the positive-threshold regime. In particular,

`Delta_edge(2,delta)=delta/(2+delta)`

starts from zero and grows to one, whereas for `m>=3` there is already a positive mismatch at `delta=0`.

This deformation explains why `m=2` alone supports a finite interval `0<delta<delta_*` in which an admissible same-exponent BPA can be tuned to have the same numerical threshold as FPA. For `m>=3`, even the maximally connected admissible affine BPA (`beta=1`) cannot reach the FPA robustness level.

## 7. Relation to the neighboring R08 result

The neighboring immutable R08 report

`runs/R08/20260917T2326Z_i0048_threshold_comparison_73b9e1.md`

showed:

- the zero/nonzero threshold boundary agrees after matching the degree exponent;
- a concrete same-exponent pair at `m=2, delta=2`, `gamma=1/3`, `beta=1` has unequal positive thresholds.

The present derivation does **not** duplicate that witness. It proves the stronger facts that:

1. `m=2, delta=2` lies above the exact crossover `delta_*`, so `beta=1` is already the *most robust* admissible same-exponent BPA and the inequality persists for every `0<beta<=1`;
2. the same all-`beta` strict inequality holds for every `m>=3, delta>0`;
3. below `delta_*` in the `m=2` family, equality is possible at exactly one intercept, and (5.8) gives it explicitly;
4. no `m>=2, delta>0` standard affine BPA can simultaneously match the FPA exponent and edge density.

This is the useful new admission-side refinement.

## 8. Admission consequence

I0048 should **not** be admitted by R7-05 as a fresh CLOSABLE outside target.

At the threshold level, later literature already gives the decisive formulas, and the remaining normalization ambiguity can now be resolved exactly as above. If the old source's word "results" is interpreted broadly enough to include all critical exponents, critical-window laws, or near-critical giant-size asymptotics across FPA and conditionally-independent PA, that becomes a broad comparison program rather than a sharp source-level CLOSABLE theorem.

Current honest disposition for this worker:

`I0048 = THRESHOLD_SCOPE_KNOWN_AND_EXACTLY_CLASSIFIABLE / BROADER_RESULTS_SCOPE_NOT_FROZEN / NOT_READY_CLOSABLE`.

No `operations/claims/I0048.md` is created.

## 9. Source-check notes

Fresh bounded checks on 2026-09-19 recovered:

- the 2026 Hazra--van der Hofstad--Ray fixed-outdegree percolation formula;
- the 2018 Eckhoff--Mörters--Ortgiese spectral-radius formula and `p_c=1/rho(alpha_*)` relation for conditionally-independent PA;
- Jorritsma--Komjáthy's explicit FPA versus VPA/GVPA model comparison, including `f(0)<=1`, conditional edge independence, random outdegree, and comparison by power-law exponent;
- the current van der Hofstad book treatment of Bernoulli preferential attachment and its power-law exponent convention.

No source found in this bounded search stated the exact classification (4.6), (5.6)--(5.8), or the normalization obstruction (3.5)--(3.7). That search miss is **not** a novelty certificate. These results are recorded as transparent consequences of known formulas, with novelty `UNVERIFIED`.

## 10. Mathematical status

- Source-level I0048 threshold problem: **KNOWN by later literature / comparison algebraically classifiable**.
- New derivations in this artifact: **PROVED as consequences of the quoted known formulas and source-class parameter restrictions**.
- Novelty: **UNVERIFIED**.
- R7-05 admission: **NO**.
- R7-05 successor state remains: **PENDING_ADMISSION**.
