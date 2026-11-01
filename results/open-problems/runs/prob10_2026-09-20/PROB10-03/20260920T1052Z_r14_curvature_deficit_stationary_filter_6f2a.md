Runtime model: **GPT-5.6 Sol**. Requested GPT-6/maximum is not a configurable native setting here; reasoning-effort telemetry is **UNVERIFIED**.

# PROB10-03 — R14 bounded substantive iteration: curvature-deficit stationary filter

Repository / branch: private `yspennstate/math-open-problems` / `master`.  
Status: **OPEN / PARTIAL / SOURCE BRACKET UNCHANGED / NEW EXACT THIRD-FULL FEASIBILITY FILTER**.

## 1. Contract, continuity, ownership, and consumed state

I first read the controlling `operations/PROB10_2026-09-20.md`, root `POSTED.md`, the current R14/perceptron history, and the newest relevant own/neighbor reports. Pre-write `master` was observed at `6763f6b3b7fece7e7a0a30675805c4cdce449da6`; all writes below are create-only, so no concurrent file was overwritten.

Continuity preserved:

- `operations/claims/I0089.md` (blob `0df4adc0fd8ee99edeb4890de3d5e9e076a1edd0`) records the older negative-margin R14 attempts/failures and is not reset;
- `operations/claims/CAMPBELL-OROURKE-2022-Q1.8.md` (blob `d8fe3a276b9c59d4608a113c0d77ba5b5dc8717d`) remains untouched;
- the immutable actual-successor handoff `artifacts/prob10_2026-09-20/PROB10-03/20260919T2354Z_campbell_q18_r14_handoff.md` (blob `edaa787e384c28a4b5a658dbba80f664cde75882`) remains the R14 history link and explicitly preserves navigation point `3846db33296cfb6eea59ff7c488929087c7b62a2`;
- newest preceding own report consumed: `runs/prob10_2026-09-20/PROB10-03/20260920T0953Z_r14_variance_matched_entropy_cage_c4f7.md` (blob `a4d12d3ca001373c7abde8c827e40b9aec3e1315`);
- newest relevant companion reports consumed include `proofnet24/NM13-07/progress-perceptron/runs/2026-09-20/2026-09-20__t03-entropy-dissipation-sharp-microextend.md`, `.../2026-09-20__t03-posgap4d-certified-microextend-1231963484.md`, and `proofnet24/NM13-03/progress-perceptron-theory/runs/2026-09-20/2026-09-20__t03-curvature-overlap-alpha1228722223.md`, all as present on the above current-master snapshot.

`POSTED.md` still explicitly separates the owner's zero-margin/Ising perceptron work from this negative-margin continuous exact-sphere target.

No canonical claim, peer report, scheduler/cadence/enabled state, workflow, permission, email, Drive object, public posting, or existing file was modified.

## 2. Exact source target and probability convention

Freeze

`M=floor(alpha N)`, `g_a iid N(0,I_N)`, `||sigma||_2=sqrt(N)` exactly,

and require

`<g_a,sigma> >= -sqrt(N)` for every `a<=M`.

A rigorous lower endpoint means the SAT probability tends to one as `N->infinity` at fixed `alpha`; a rigorous upper endpoint means the SAT probability tends to zero. Smaller-radius constructions, Ising restrictions, finite-lift floating-point stationary values, or replica/full-RSB numerics are not source endpoints.

The entering repository-supported bracket is

`alpha_L = 6.30297437506`,

`alpha_U = 12.3196348278`,

`W = alpha_U-alpha_L = 6.01666045274`.

The strict latest movement to `12.3196348278` belongs to NM13-07 and was already consumed by the preceding R14 report.

## 3. Source-scope refresh

A bounded fresh check of the requested sources and current follow-up did not supply a certified numerical exact-radius `kappa=-1` threshold that supersedes the repository task.

- El Alaoui--Sellke, `https://arxiv.org/abs/2010.15811`, formulate the full radius-`sqrt(N)` spherical perceptron, but for negative margin their algorithm uses the conjectured FRSB/Parisi structure and returns a vector on radius `sqrt(qbar N)` with `qbar<1`; this is not the exact-radius source closure required here.
- Stojnic, `https://arxiv.org/abs/1306.3980`, gives rigorous negative-margin random-duality capacity bounds rather than the requested exact numerical threshold.
- Stojnic, `https://arxiv.org/abs/2312.16531`, fits the negative spherical perceptron into complete stationarized fully lifted RDT and describes the capacity through that machinery, while explicitly noting that making fl-RDT practically operational requires substantial numerical work. The repository therefore continues to require a proved stationary reduction plus outward-certified realization before treating a displayed finite-lift number as its source endpoint.
- Annesi--Malatesta--Zamponi, `https://arxiv.org/abs/2410.06717`, compute the SAT/UNSAT transition under a full-RSB ansatz; this is structural guidance rather than the directed rigorous endpoint required here.
- Huang--Sellke--Sun, `https://arxiv.org/abs/2608.29416` (29 August 2026), exactly characterize a dimension-free Lipschitz **algorithmic** projection-pursuit class and explicitly distinguish the non-algorithmic feasible-projection problem.

This is bounded dated source evidence, not a worldwide novelty certificate.

## 4. Three materially different attacks

### Attack A — curvature-deficit information projection: successful exact theorem

The previous R14 report produced a variance-matched KL/Fisher cage, but it still needed the tilted variance itself. The new idea is to bound that variance deficit directly from the relative-score variance and a curvature cap.

For `d nu/d gamma = exp(phi)/Z`, `gamma=N(0,1)`, with concave `phi`, put

`r=phi'`, `t=-r'`, `0<=t<=K`,

`mu=E X`, `v=Var X`, `R=Var(r)`, `D=KL(nu||gamma)`.

A complete proof is in

`artifacts/prob10_2026-09-20/PROB10-03/20260920T1050Z_r14_curvature_deficit_entropy_filter.md`.

The key exact integration-by-parts identity is

`1-v = E t - R`.                                             (4.1)

Brascamp--Lieb for the strongly log-concave potential `x^2/2-phi(x)` gives

`R <= E[t^2/(1+t)] <= K/(1+K) E t`.                         (4.2)

Combining (4.1)--(4.2) yields

`1-v >= R/K`.                                                (4.3)

With `psi(z)=-z-log(1-z)`, the variance-matched information projection then gives the **sharp** lower bound

`D >= mu^2/2 + psi(R/K)/2`.                                 (4.4)

For a family of tilts sharing `K`, convexity of `psi` gives

`E D >= (1/2)E mu^2 + (1/2)psi(E R/K)`.                     (4.5)

This is an exact theorem, not a numerical ansatz.

#### Third-full consequence

Use

`m=c3/c2`, `d^2=p2-p3`, `s^2=1-p2`,

`C=4B^2 M_B=c2^2/alpha`,

`L=2B/(1+2Bs^2)`.

The exact score-overlap and entropy-stationarity identities already proved in the current repository turn (4.5) into

`t_U = m C(q2-q3)/L`,

`A_c3 >= d^2 q3/2 + psi(t_U)/(2m^2 C)`,                     (4.6)

and for the inner H tilt

`t_H = C(1-q2)/(2B)`,

`A_c2 >= s^2 q2/2 + psi(t_H)/(2C)`.                         (4.7)

The theorem itself guarantees `0<=t_U,t_H<1` at a genuine strict stationary point.

Because `psi(t)>=t^2/2`, this has the particularly cheap interval-filter corollary

`boxed: A_c3 >= d^2 q3/2 + C(q2-q3)^2/(4L^2)`,              (4.8)

`boxed: A_c2 >= s^2 q2/2 + C(1-q2)^2/(16B^2)`.              (4.9)

Unlike the old lower cage proved automatic in projective coordinates, (4.8)--(4.9) contain the actual score normalization and kernel-curvature scale. They are therefore genuine stationary feasibility restrictions and can reject boxes before expensive nested KL integration.

### Attack B — try to strengthen the new inequality universally: rigorous obstruction

The negation/equality analysis shows exactly where this route stops. For the quadratic tilt

`phi(x)=-a x^2/2+b x`, `a>0`,

`nu` is Gaussian with

`v=1/(1+a)`, `K=a`, `R=a^2/(1+a)`,

and therefore

`1-v=R/K`.

The variance-matched KL lower bound is also equality because `nu` already is its matched Gaussian. Hence (4.4) is **sharp among all statements that know only `(mu,R,K)`**. There is no everywhere-stricter universal replacement using only those three statistics.

This is a useful obstruction rather than a failed checker: the next improvement must exploit the perceptron-specific nonconstant curvature `u_xx`, not merely rerun stronger generic entropy inequalities. That points directly to the complementary NM13-03 curvature-overlap theorem, which retains the distribution of `u_xx` rather than only its supremum `L`.

### Attack C — direct root-box pruning at the positive-gap waypoint: useful but insufficient

I tested the new exact feasibility filters against the archived strict positive-gap `delta=10^-3` third-full waypoint near

`alpha ~= 12.3164333569308`.

The executed checker gives

outer c3 sector:

`old lower = 0.042547244702661434`,

`quadratic new lower = 0.04362056612920202`,

`full psi lower = 0.04366007033384754`,

`A_c3 ~= 0.06754502594496141`;

inner c2 sector:

`old lower = 0.01027322762668804`,

`quadratic new lower = 0.0103406837413211`,

`full psi lower = 0.010343442445016742`,

`A_c2 ~= 0.012015975514895874`.

Thus the new filter is genuinely stricter but the numerical candidate remains well inside it. In particular, **the filter alone cannot certify the root**. The remaining non-algebraic work is still a directed enclosure of the nested score/KL moment map. The best nonduplicating route is now a hybrid subdivision: use (4.8)--(4.9) as cheap c-sector rejection tests, use NM13-03's independent curvature-overlap sandwich as a q-gap rejection test, and invoke full outward nested integration only on boxes surviving both.

This is materially different from the exhausted old algebraic transport cage and from complete-second digit shaving.

## 5. Executed checks

The proof was written before code in

`artifacts/prob10_2026-09-20/PROB10-03/20260920T1050Z_r14_curvature_deficit_entropy_filter.md`.

Then I executed the exact/symbolic checker archived as

`artifacts/prob10_2026-09-20/PROB10-03/20260920T1051Z_r14_curvature_deficit_checker.py`,

with actual output in

`artifacts/prob10_2026-09-20/PROB10-03/20260920T1051Z_r14_curvature_deficit_checker.out`.

It verifies the information-projection algebra, the Brascamp--Lieb rearrangement, exact sharpness for quadratic Gaussian tilts, the complete-third substitutions, and the numerical-only waypoint falsification. The output ends

`ALL_SELF_CHECKS_PASS`.

These are self-checks, not independent audits.

## 6. Source metric before/after and auxiliary movement

### Source-level metric

Before:

`[6.30297437506, 12.3196348278]`, width `6.01666045274`.

After:

`[6.30297437506, 12.3196348278]`, width `6.01666045274`.

**Source movement: none.** No conditional `12.287...` or `12.316...` number is promoted.

### Auxiliary/mechanism movement

1. Proved a sharp curvature-deficit KL lower bound for strongly log-concave Gaussian tilts.
2. Compiled it into two strict complete-third stationary feasibility inequalities, including log-free quadratic forms (4.8)--(4.9) suitable for directed box pruning.
3. Proved a sharpness obstruction: no universal method using only `(mean, score variance, uniform curvature cap)` can improve this theorem everywhere.
4. Falsification at the `delta=10^-3` waypoint shows the new filter is nontrivial but insufficient by itself, isolating the residual need for perceptron-specific variable-curvature/nested-moment control.

## 7. Remaining full-scope gap

The exact `kappa=-1` capacity problem remains **OPEN / PARTIAL** under the repository closure standard.

The next source-moving obligation is a genuine outward four-dimensional inclusion for a strict positive-gap complete-third point, preferably the existing `delta=10^-3` waypoint or a nearby easier waypoint. The efficient rigorous compiler is now:

- algebraic q-sector and positive-gap reconstruction;
- cheap rejection by (4.8)--(4.9);
- independent rejection by the NM13-03 curvature-overlap sandwich;
- outward two-dimensional `U,V` integration only for surviving boxes, with the H integral already closed analytically;
- weighted Krawczyk/contraction inclusion for the four overlap residuals.

Only after such a root certificate, the exact source-matched fl-RDT implication, and the required independent validation may a third-full value move the rigorous source endpoint. No ansatz, simulation, or floating-point stationary point is an endpoint here.
