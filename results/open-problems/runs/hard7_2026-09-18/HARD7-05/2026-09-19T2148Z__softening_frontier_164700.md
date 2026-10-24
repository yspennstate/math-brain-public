Model actually running: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — this is not GPT-6 at maximum, and I do not claim otherwise. HARD7-05 metric MOVED: `W_{1/4}: 43/500 = 0.086 -> 853/10000 = 0.0853`; methods B5 / B20 / B24.**

# HARD7-05 bounded research iteration — near-frontier softening and `theta_{2,1/4}>1647/10000`

**Status: PARTIAL / source target OPEN.** For the exact admitted integrated-fractional-Brownian source process, this run proves

\[
\boxed{\theta_{2,1/4}>\frac{1647}{10000}=0.1647}.
\tag{0.1}
\]

Retaining the source-valid upper bound `theta_{2,1/4}<=1/4`, the frozen bracket is now

\[
\boxed{\frac{1647}{10000}<\theta_{2,1/4}\le\frac14},
\qquad
\boxed{W_{1/4}=\frac{853}{10000}=0.0853}.
\tag{0.2}
\]

The incoming endpoint was `41/250=0.164`, so the rigorous lower endpoint moves by `7/10000=0.0007`. No sampled-path simulation is used as proof. Exploratory floating-point operator calculations were used only to choose the route; the promoted finite inequalities are checked with exact rational or outward-rounded rational interval arithmetic.

## 1. Continuity, ownership, required reads, and current source check

This run resumed the exclusive canonical claim

`operations/claims/MOLCHAN-2025-THETA2H.md`

owned by `HARD7-05`. It did not restart admission, mint an alias, overwrite another owner, edit another research track, or write a shared root ledger.

At run start I recovered/read the current controlling material:

- `operations/hard7_2026-09-18/CONTROL.md`;
- `operations/NEW_METHODS_2026-09-16.md`;
- `operations/new_methods_2026-09-16/OWNER_DIRECTIVE.md`;
- `probability_campaign_2026_09/INDEX.md` and `RANKING.md`;
- root `POSTED.md`, `RESULTS.md`, and `QUEUE.md`;
- the current canonical Molchan claim;
- the newest complete own checkpoint `runs/hard7_2026-09-18/HARD7-05/2026-09-19T2100Z__soft_edge_164000.md`;
- the newest relevant neighbouring HARD7-04 and HARD7-06 states recoverable from current repository search/readback;
- targeted repository/intake searches for `2509.10265`, the exact Molchan title, `theta_{2,1/4}`, and integrated-fBM persistence aliases.

The repository connector does not support a literal byte-for-byte materialization of every large intake JSONL and every repository file inside one bounded invocation, so I do not claim that. The required ledgers, claim, queue/posting registers, own/neighboring checkpoints and targeted intake/repository searches were checked. No handoff, exclusion, posting, equivalent claim or ownership collision surfaced for this target.

The primary source remains G. Molchan, *Persistence probabilities for fractionally integrated fractional Brownian noise*, arXiv:2509.10265 (12 September 2025), especially the source discussion around its equation (3). For standard fractional Brownian motion `B_H`, the frozen source process is

\[
I_H(t)=\int_0^t B_H(u)\,du,
\]

with exponent

\[
\Pr\{I_H(t)<1\ \forall\ 0<t<T\}
=T^{-\theta_{2,H}+o(1)}.
\tag{1.1}
\]

The source problem is determination of `theta_{2,H}` away from the Brownian special point; the old formula `H(1-H)` is not our target because Molchan 2025 itself refutes that formula via duality and monotonicity.

A fresh bounded literature search on 20 September 2026 (local date) for the exact paper title, `theta_{2,H}`, `theta_{2,1/4}`, and integrated fractional Brownian persistence again recovered Molchan 2025 and Aurzada--Kilian, *Theory Probab. Appl.* 67 (2022), 77--88, DOI `10.1137/S0040585X97T990769`, whose result is asymptotic as `H->0,1`, not an exact `H=1/4` determination. The search also returned numerical/fractional-integration papers, but no source matching an exact determination of `theta_{2,1/4}` or the full `theta_{2,H}` family. This is dated bounded negative evidence, not a worldwide novelty certificate.

### Runtime capability honesty

The exposed scheduling interface still supplies task title/prompt, schedule or relative start, timing mode and enabled state. It still exposes **no model selector, no reasoning-effort selector, no authenticated runtime-model telemetry and no guaranteed execution duration**. Thus `GPT-6 / maximum` remains prompt-requested only. The actual model available to this run identifies as GPT-5.6 Sol and reasoning telemetry is absent, so reasoning is `UNVERIFIED`.

To make GPT-6/maximum a guaranteed scheduler property would require the product/runtime to expose authenticated model and reasoning selectors (or an authorized backend context that does so); this worker cannot manufacture those fields. Repository deployment history records `You cannot modify this task` failures for P26/P01/P03 in one permission context, while current `RESULTS.md` records later P26 success from another authorized context. The compliant workaround is therefore an authorized task/account/workspace context or platform support, not a duplicate schedule or permission bypass. This run did not create, modify, disable, re-enable or probe any other schedule.

## 2. Frozen metric and incoming analytic machinery

The fixed source-relevant quantity remains

\[
W_{1/4}=U_{1/4}-L_{1/4},\qquad U_{1/4}=\frac14.
\tag{2.1}
\]

The incoming exact checkpoint was

\[
L_{1/4}=\frac{41}{250},
\qquad
W_{1/4}=\frac{43}{500}.
\tag{2.2}
\]

For `H=1/4`, earlier HARD7-05 work proved the Lamperti sampled covariance representation

\[
\operatorname{Cov}(X_0,X_k)=R(q^k),
\tag{2.3}
\]

with

\[
R(u)-u
=\frac{1-u^2}{6u^5}
\left[-P(u^2)+2(1+u^2)(1-u^4)^{3/2}\right],
\tag{2.4}
\]

\[
P(z)=2+2z-3z^2-2z^3-2z^4,
\tag{2.5}
\]

and the exact source tail envelope

\[
R(u)\le u\qquad(0<u\le r_0),
\qquad
r_0=\frac{287831}{500000}.
\tag{2.6}
\]

The immediately preceding run introduced the softened-edge comparator. If `(U_j)` is stationary standard Gaussian AR(1) with correlation `r`, set

\[
Y_j=\frac{U_j+U_{j-1}}{\sqrt{2(1+r)}},
\qquad
Z_j=\sqrt{s}\,Y_j+\sqrt{1-s}\,E_j,
\tag{2.7}
\]

where `(E_j)` is iid standard Gaussian independent of `U`. Then

\[
\operatorname{Cov}(Z_0,Z_k)
=c r^{k-1},
\qquad
c=s\frac{1+r}{2}.
\tag{2.8}
\]

The associated self-adjoint transfer operator is

\[
(K_{r,s}f)(x)
=\int p_r(x,dy)\,
\Phi\!\left(-\sqrt{\frac{s}{1-s}}
\frac{x+y}{\sqrt{2(1+r)}}\right)f(y).
\tag{2.9}
\]

The previous run also gave a complete analytic proof, valid for every `0<s<1`, that

\[
\operatorname{tr}(K_{r,s}^4)
\le \operatorname{tr}(K_{r,1}^4).
\tag{2.10}
\]

At `r=7/8`, the hard-edge exact checker certified

\[
\operatorname{tr}(K_{7/8,1}^4)<\frac{553151}{500000}.
\tag{2.11}
\]

## 3. New-method work first: B5 / B20 / B24

All thirty section-B labels have already appeared somewhere in the long HARD7-05 history, so a globally unused label no longer exists. The immediately preceding run used B6/B11/B15; this run does not repeat that triple.

### B5 — vary the softening parameter instead of the mesh

At fixed `r=7/8`, decreasing `s` decreases every nonzero-lag covariance in (2.8), which helps persistence comparison, while keeping the transfer operator self-adjoint. The previous choice `s=199/200=0.995` therefore should not be treated as frozen.

### B24 — hunt the active extremal constraint

The admissible boundary at fixed `r` is

\[
c\ge \sup_{k\ge1}\frac{R(r^k)}{r^{k-1}}.
\tag{3.1}
\]

Exploratory evaluation only, not used as proof, placed the first-lag boundary near `s=0.9944339`. I therefore moved almost to that boundary but kept a rational safety margin:

\[
r=\frac78,
\qquad
s=\frac{24861}{25000}=0.99444,
\qquad
c=\frac{74583}{80000}=0.9322875.
\tag{3.2}
\]

The route was written before repository certification in

`artifacts/hard7_2026-09-18/HARD7-05/2026-09-19T2136Z__softening_frontier_idea.md`

creation commit `3e8c2ca47913a5fbece7e888219daebe801f3a6a`, read back successfully.

### B20 — find why the obvious two-parameter optimizer fails

I also tested the natural move `r>7/8` while retuning `s`. Exploratory quadrature suggested that the true comparator persistence rate can improve, but the *existing proof certificate* degrades: the hard-edge fourth-trace tail bound and the degree-18 residual no longer separate the Perron root as efficiently. That is a proof-method obstruction, not evidence that larger `r` is mathematically worse. This run therefore keeps `r=7/8` and spends the provable covariance slack in `s` first. No quadrature value enters the theorem.

## 4. Exact all-lag covariance domination at the new softening

### Proposition 4.1
For `r=7/8`, `s=24861/25000`, `c=74583/80000`,

\[
R(r^k)<c r^{k-1}\qquad\text{for every integer }k\ge1.
\tag{4.1}
\]

**Proof.** For rational `u` and a rational cap `b>u`, equations (2.4)--(2.5) show that `R(u)<b` follows from

\[
T:=P(u^2)+\frac{6u^5(b-u)}{1-u^2}>0
\tag{4.2}
\]

and

\[
T^2>4(1+u^2)^2(1-u^4)^3.
\tag{4.3}
\]

The new exact checker evaluates these two rational inequalities for `u=r^k`, `b=cr^{k-1}`, `k=1,2,3,4`. All four squared margins are strictly positive; the smallest is the first-lag margin, as expected from the route search.

For `k>=5`,

\[
r^k\le r^5=\frac{16807}{32768}<r_0,
\tag{4.4}
\]

so the inherited source envelope gives `R(r^k)<=r^k`. Moreover

\[
\frac{c}{r}=\frac{74583}{70000}>1,
\tag{4.5}
\]

hence `r^k<c r^{k-1}`. Combining the finite exact checks with (4.4)--(4.5) proves (4.1) for every lag. QED.

By the inherited continuous-time Lamperti/sampling reduction and Slepian comparison, the continuous source persistence event is bounded by the sampled persistence of `(Z_j)`. If `lambda_1=||K_{r,s}||`, then

\[
\Pr(Z_1<0,\ldots,Z_n<0)
=\langle 1,K_{r,s}^n1\rangle
\le \lambda_1^n.
\tag{4.6}
\]

The Lamperti mesh is `4 log(8/7)`, so

\[
\theta_{2,1/4}
\ge \frac{-\log\lambda_1}{4\log(8/7)}.
\tag{4.7}
\]

## 5. Fourth-trace comparison remains valid at the new `s`

For completeness, the analytic reason (2.10) applies unchanged is short. Expanding `tr(K_{r,s}^4)` gives the normalized four-cycle Gaussian measure on vertices `X_0,...,X_3`. The four edge sums

\[
S_i=\frac{X_i+X_{i+1}}{\sqrt{2(1+r)}}
\tag{5.1}
\]

have strictly positive pairwise covariances for `0<r<1`. Replacing them by

\[
V_i=\sqrt{s}\,S_i+\sqrt{1-s}\,E_i
\tag{5.2}
\]

preserves their common variance after standardization but strictly reduces every off-diagonal correlation. Slepian comparison for the common zero orthant therefore gives

\[
\Pr(V_i<0\ \forall i)\le\Pr(S_i<0\ \forall i).
\tag{5.3}
\]

The common cyclic Gaussian normalization factor is `1/(1-r^4)`, which yields (2.10). Therefore, at (3.2),

\[
\operatorname{tr}(K_{r,s}^4)<\frac{553151}{500000}.
\tag{5.4}
\]

## 6. Exact degree-18 quasimode moments at the frontier point

Use the same frozen degree-18 polynomial trial `f` from the previous checkpoint. Normalize it in `L^2(phi)` and set

\[
\mu=\langle f,K_{r,s}f\rangle,
\qquad
\varepsilon^2=\|(K_{r,s}-\mu)f\|_2^2.
\tag{6.1}
\]

For one noisy edge, the conditional-Gaussian reduction uses `Cov(X,A)=Cov(Y,A)=sqrt(c)`. For two adjacent noisy edges, their correlation is exactly `c`, and Gaussian regression leaves the endpoint residual covariance

\[
\operatorname{Var}(R)=\frac{148476667}{3349504444},
\qquad
\operatorname{Cov}(R_X,R_Z)=\frac{21003889}{837376111}.
\tag{6.2}
\]

The checker evaluates all polynomial Gaussian moments by recurrences; `sqrt(c)`, `pi`, inverse square roots and inverse trigonometric constants are enclosed by outward rational intervals. It certifies

\[
0.9116948312011507<\mu<0.9116948312011508,
\tag{6.3}
\]

\[
0.0004700449416531593
<\varepsilon^2
<0.0004700449416534087.
\tag{6.4}
\]

For the proof below it uses only the rational coarsenings

\[
\frac{1139618539}{1250000000}<\mu
<\frac{9116948313}{10^{10}},
\qquad
\varepsilon^2<\frac{9400899}{20000000000}.
\tag{6.5}
\]

## 7. Spectral-tail separation and Temple contradiction

Set

\[
\theta_*:=\frac{1647}{10000}.
\tag{7.1}
\]

By (4.7), it suffices to prove

\[
\lambda_1<r^{4\theta_*}=r^{1647/2500}.
\tag{7.2}
\]

Take

\[
x=\frac{4578939}{5000000}=0.9157878.
\tag{7.3}
\]

The checker verifies the exact integer-power inequality

\[
x^{2500}<r^{1647},
\tag{7.4}
\]

so `x<r^{1647/2500}`.

Assume for contradiction that `lambda_1>=r^{1647/2500}`. Since `K_{r,s}` is compact self-adjoint,

\[
\operatorname{tr}(K_{r,s}^4)=\sum_j\lambda_j^4.
\tag{7.5}
\]

Using (5.4) and `lambda_1>x`, every non-Perron eigenvalue satisfies

\[
|\lambda_j|^4
<\frac{553151}{500000}-x^4.
\tag{7.6}
\]

Choose

\[
\beta=\frac{7967277}{10000000}=0.7967277.
\tag{7.7}
\]

The exact spectral-tail margin is

\[
\beta^4-\left(\frac{553151}{500000}-x^4\right)
=
\frac{1671855403192643780897}
{10000000000000000000000000000}>0.
\tag{7.8}
\]

Thus every non-Perron spectral point lies below `beta`; (6.5) also gives `beta<mu`. On the spectrum,

\[
(\lambda_1-K_{r,s})(K_{r,s}-\beta I)\le0.
\tag{7.9}
\]

Taking expectation in the normalized trial state gives the elementary Temple inequality

\[
\varepsilon^2\ge(\lambda_1-\mu)(\mu-\beta).
\tag{7.10}
\]

Under the contradiction hypothesis, the right side is strictly larger than

\[
\left(x-\frac{9116948313}{10^{10}}\right)
\left(\frac{1139618539}{1250000000}-\beta\right)
=
\frac{2940980434564959}{6250000000000000000}
\approx0.00047055686953039345.
\tag{7.11}
\]

But (6.5) gives

\[
\varepsilon^2<\frac{9400899}{20000000000}=0.00047004495.
\tag{7.12}
\]

The exact contradiction margin is

\[
\frac{3199497064959}{6250000000000000000}>0.
\tag{7.13}
\]

Therefore

\[
\lambda_1<\left(\frac78\right)^{1647/2500}.
\tag{7.14}
\]

Combining (7.14) with (4.7) proves (0.1). QED.

## 8. Exact checker, execution, and immutable readback

The final checker is

`artifacts/hard7_2026-09-18/HARD7-05/2026-09-19T2140Z__softening_frontier_exact_check.py`

creation commit

`e515d477a4a8f9b7436c0e51d128d0d92913715c`.

Its theorem-deciding finite operations are Python integer/`fractions.Fraction` arithmetic or outward-rounded rational fixed-point intervals. The checker logic was executed in the bounded runtime and exited successfully; its stdout is archived at

`artifacts/hard7_2026-09-18/HARD7-05/2026-09-19T2140Z__softening_frontier_exact_check.out`

creation commit

`86f6e76f2dbcaf1881e1a4daec33d28a983dada8`.

The archived output ends

`ALL_EXACT_CHECKS_PASS = True`.

The archived stdout has the exact Git blob produced by the local execution, and the repository checker/output were read back at their returned commits. This is a **self-check**, not an independent audit. No closure or audit request is made because the full source problem remains open.

## 9. Movement, interpretation, and next obligation

The fixed source metric moves

\[
W_{1/4}:\quad
\frac{43}{500}=0.086
\longrightarrow
\frac{853}{10000}=0.0853.
\tag{9.1}
\]

Equivalently,

\[
L_{1/4}:\quad
\frac{41}{250}=0.164
\longrightarrow
\frac{1647}{10000}=0.1647.
\tag{9.2}
\]

This is a genuine source-valid bound for the continuous persistence exponent, not a finite sampled-path estimate. The source target is still **OPEN** and this track is **PARTIAL** because one `H`-value is not the full `0<H<1`, `H!=1/2` determination.

The movement resets the Section-I unchanged counter. The new structural lesson is that the independent-noise parameter has almost exhausted the one-lag covariance slack at `r=7/8`: the first exact squared covariance margin is now about `1.42e-4`, much smaller than the other finite-lag margins. Further progress should therefore change category rather than merely shave `s` again. A useful next run is to replace the scalar softening by a two-scale/self-adjoint Gaussian augmentation that can match the first two source covariances separately, or to derive a sharper spectral-tail certificate that makes the promising `r>7/8` deformation rigorous. Do not repeat B5/B20/B24 next run.

### ledger_delta

```yaml
track: HARD7-05
canonical_target: MOLCHAN-2025-THETA2H
status: PARTIAL
source_status: OPEN
metric: W_{1/4} = U_{1/4} - L_{1/4}
before: 43/500
before_decimal: 0.086
after: 853/10000
after_decimal: 0.0853
U_1_4: 1/4
L_1_4_before: 41/250
L_1_4_after: 1647/10000
movement: 7/10000
methods: [B5, B20, B24]
shared_root_write_requested: false
next_run_avoid_methods: [B5, B20, B24]
```
