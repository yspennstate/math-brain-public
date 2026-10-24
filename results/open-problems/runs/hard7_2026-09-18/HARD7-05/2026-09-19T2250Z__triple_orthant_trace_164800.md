Model actually running: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — this is not GPT-6 at maximum, and I do not claim otherwise. HARD7-05 metric MOVED: `W_{1/4}: 853/10000 = 0.0853 -> 213/2500 = 0.0852`; methods B1 / B4 / B25.**

# HARD7-05 bounded research iteration — exact trivariate projection of the softened four-cycle and `theta_{2,1/4}>103/625`

**Status: PARTIAL / source target OPEN.** For the exact admitted integrated-fractional-Brownian source process, this run proves

\[
\boxed{\theta_{2,1/4}>\frac{103}{625}=0.1648}.
\tag{0.1}
\]

Keeping the source-valid upper bound `theta_{2,1/4}<=1/4`, the frozen source bracket is now

\[
\boxed{\frac{103}{625}<\theta_{2,1/4}\le \frac14},
\qquad
\boxed{W_{1/4}=\frac{213}{2500}=0.0852}.
\tag{0.2}
\]

The incoming lower endpoint was `1647/10000=0.1647`, so the rigorous lower endpoint moves by `1/10000`. This is a continuous-path persistence bound obtained through the already proved Lamperti/sampling/Slepian reduction; no finite path simulation is promoted to a theorem.

## 1. Continuity, ownership, source status, and required reads

This run resumed the exclusive canonical claim

`operations/claims/MOLCHAN-2025-THETA2H.md`

owned by `HARD7-05`. It did not restart admission, mint an equivalent alias, overwrite another owner, or edit another track.

At run start I recovered/read the governing and fleet state relevant to this worker:

- `operations/hard7_2026-09-18/CONTROL.md`;
- `operations/NEW_METHODS_2026-09-16.md`;
- `operations/new_methods_2026-09-16/OWNER_DIRECTIVE.md`;
- `probability_campaign_2026_09/INDEX.md` and `RANKING.md`;
- root `POSTED.md`, `RESULTS.md`, and `QUEUE.md`;
- `operations/claims/MOLCHAN-2025-THETA2H.md`;
- the newest complete own checkpoint `runs/hard7_2026-09-18/HARD7-05/2026-09-19T2148Z__softening_frontier_164700.md`;
- current neighbouring HARD7-04 and HARD7-06 states recoverable from repository search;
- source/alias-targeted searches through the intake/repository material for integrated fractional Brownian persistence, `2509.10265`, `theta_{2,H}`, and the exact canonical claim.

The connector cannot literally render every large `probability_1000_intake_*/problems.jsonl` file byte-for-byte inside one bounded invocation, so I do not claim a literal full-file reread. The targeted intake/claim/source searches found no release, duplicate owner, posted equivalent, canonical collision, or repository closure marker for the present source statement.

The external source remains G. Molchan, *Persistence probabilities for fractionally integrated fractional Brownian noise*, arXiv:2509.10265, with the current source version previously verified by this track as v11 (revised 4 July 2026). For standard fractional Brownian motion `B_H`, the frozen process is

\[
I_H(t)=\int_0^t B_H(u)\,du,
\]

and the source exponent is defined by

\[
\Pr\{I_H(t)<1\ \forall\ 0<t<T\}
=T^{-\theta_{2,H}+o(1)}.
\tag{1.1}
\]

The admitted problem is the determination of `theta_{2,H}` for `0<H<1`, `H!=1/2`; the old formula `H(1-H)` is not this track's conjecture because the source itself refutes that formula using duality and monotonicity.

A bounded current-literature search on 20 September 2026 for the exact Molchan title, `theta_{2,H}`, integrated-fBM persistence and exact `H=1/4` values again recovered Molchan's source and Aurzada--Kilian's asymptotic endpoint work, together with adjacent Gaussian-persistence papers, but no exact solution of `theta_{2,1/4}` or the full source family. This is dated bounded negative evidence, not a worldwide novelty certificate.

### Runtime capability honesty

The exposed scheduler interface still offers title, prompt, schedule/relative start, timing mode and enabled state. It exposes **no model selector, no reasoning-effort selector, no authenticated runtime-model telemetry and no guaranteed run duration**. Thus GPT-6/maximum remains prompt-requested only. The model actually available in this run identifies as GPT-5.6 Sol; reasoning telemetry is absent, hence `UNVERIFIED`.

To make GPT-6/maximum a guaranteed scheduled property would require a product/runtime interface exposing authenticated model and reasoning selectors, or an authorized backend context that exposes them. Earlier deployment records contain `You cannot modify this task` for P26/P01/P03 in one permission context, while the current root ledger records a later successful P26 update from another authorized context. The compliant workaround is an authorized account/workspace/task context or platform support, not a duplicate schedule or a permission bypass. This run did not create, modify, disable, re-enable or probe another schedule.

## 2. Frozen metric and incoming proof machinery

The fixed source metric remains

\[
W_{1/4}=U_{1/4}-L_{1/4},\qquad U_{1/4}=\frac14.
\tag{2.1}
\]

The incoming exact checkpoint was

\[
L_{1/4}=\frac{1647}{10000},
\qquad
W_{1/4}=\frac{853}{10000}.
\tag{2.2}
\]

For `H=1/4`, earlier HARD7-05 work established a Lamperti sampled covariance `R(r^k)` and, at

\[
r=\frac78,\qquad s=\frac{24861}{25000},\qquad c=s\frac{1+r}{2}=\frac{74583}{80000},
\tag{2.3}
\]

the all-lag domination

\[
R(r^k)<c r^{k-1}\qquad(k\ge1).
\tag{2.4}
\]

The comparator is generated from stationary standard Gaussian AR(1) variables `(U_j)` with correlation `r` by

\[
Y_j=\frac{U_j+U_{j-1}}{\sqrt{2(1+r)}},
\qquad
Z_j=\sqrt{s}\,Y_j+\sqrt{1-s}\,E_j,
\tag{2.5}
\]

where `(E_j)` is iid standard Gaussian and independent. Its self-adjoint killed transfer operator is denoted `K_{r,s}` and has Perron eigenvalue/operator norm `lambda_1`. The already proved continuous-time reduction gives

\[
\theta_{2,1/4}
\ge \frac{-\log \lambda_1}{4\log(8/7)}.
\tag{2.6}
\]

The previous exact degree-18 quasimode certificate supplies

\[
\frac{9116948312}{10^{10}}<\mu<\frac{9116948313}{10^{10}},
\qquad
\varepsilon^2<\frac{47004495}{10^{11}},
\tag{2.7}
\]

where, for the normalized trial vector `f`,

\[
\mu=\langle f,K_{r,s}f\rangle,
\qquad
\varepsilon^2=\|(K_{r,s}-\mu)f\|_2^2.
\tag{2.8}
\]

The previous run bounded the softened fourth trace by the hard-edge fourth trace,

\[
\operatorname{tr}(K_{r,s}^4)
<\frac{553151}{500000}=1.106302.
\tag{2.9}
\]

The mathematical aim of this run was to remove most of that hard-edge loss without changing the comparator or shaving `s` again.

## 3. New-method work first: B1 / B4 / B25

The immediately preceding run used B5/B20/B24, so this run deliberately changed the triple.

### B1 — change category: from operator trace to Gaussian cycle geometry

Instead of estimating `K_{r,s}` directly, write its fourth trace as a Gaussian four-cycle orthant probability. The four-cycle representation preserves exact rational covariance data at `r=7/8`, so a lower-dimensional projection can be certified with elementary Gaussian sign identities.

The route was written before checker construction in

`artifacts/hard7_2026-09-18/HARD7-05/2026-09-19T2240Z__triple_orthant_trace_idea.md`

creation commit

`31de090ace9ce34af7202f20c43e8c89e932295c`,

and was read back successfully.

### B4 — prove something weaker, completely

A full quadrivariate orthant formula is unnecessary for progress. The four-dimensional event is contained in a three-coordinate event. The latter has a closed exact formula in terms of three pairwise arcsines. This loses one inequality but is already substantially sharper than replacing the softened trace by the hard-edge trace.

### B25 — count the same object twice

The normalized Gaussian four-cycle is counted once as an orthant representation of `tr(K^4)` and again as the spectral fourth moment `sum_j lambda_j^4`. The resulting trace improvement feeds directly into the existing spectral-tail + Temple contradiction.

## 4. Exact Gaussian four-cycle representation

Consider the stationary AR(1) transition density with correlation `r`, and expand the trace of four transitions around a cycle. After normalizing by the unrestricted four-cycle partition function

\[
\operatorname{tr}(P_r^4)=\sum_{n\ge0}r^{4n}=\frac1{1-r^4},
\tag{4.1}
\]

the four cycle vertices `(X_0,X_1,X_2,X_3)` form a centered unit-variance Gaussian vector with cyclic covariance

\[
a:=\operatorname{Cov}(X_i,X_{i+1})
=\frac{r+r^3}{1+r^4},
\qquad
b:=\operatorname{Cov}(X_i,X_{i+2})
=\frac{2r^2}{1+r^4}.
\tag{4.2}
\]

At `r=7/8`, exact simplification gives

\[
a=\frac{6328}{6497},
\qquad
b=\frac{6272}{6497}.
\tag{4.3}
\]

Set

\[
A_i=\frac{X_i+X_{i+1}}{\sqrt{2(1+r)}}.
\tag{4.4}
\]

Then the exact cycle covariances are

\[
\operatorname{Var}(A_i)=\frac{6840}{6497},
\tag{4.5}
\]

\[
\operatorname{Cov}(A_i,A_{i+1})=\frac{6780}{6497},
\qquad
\operatorname{Cov}(A_i,A_{i+2})=\frac{6720}{6497}.
\tag{4.6}
\]

To represent the soft killing probability, adjoin independent standard Gaussians `E_i` and define

\[
V_i=\sqrt{s}\,A_i+\sqrt{1-s}\,E_i.
\tag{4.7}
\]

Conditioned on the cycle vertices, `1_{V_i<0}` has precisely the softened one-edge killing probability appearing in `K_{r,s}`. Therefore

\[
\boxed{
\operatorname{tr}(K_{r,s}^4)
=\frac1{1-r^4}
\Pr(V_0<0,V_1<0,V_2<0,V_3<0).
}
\tag{4.8}
\]

The common variance is

\[
\operatorname{Var}(V_i)
=\frac{170952323}{162425000},
\tag{4.9}
\]

and the two relevant correlations simplify exactly to

\[
\rho_{\rm adj}
=\frac{168557580}{170952323},
\qquad
\rho_{\rm opp}
=\frac{167065920}{170952323}.
\tag{4.10}
\]

The exact determinant of the normalized `(V_0,V_1,V_2)` correlation matrix is positive; the checker verifies this before invoking any orthant formula.

## 5. Three-coordinate orthant projection and rigorous trace cap

Dropping the fourth inequality gives

\[
\Pr(V_0,V_1,V_2,V_3<0)
\le \Pr(V_0,V_1,V_2<0).
\tag{5.1}
\]

For any centered nondegenerate trivariate Gaussian `(G_0,G_1,G_2)`, expand

\[
1_{\{G_i<0\}}=\frac{1-\operatorname{sgn}(G_i)}2.
\tag{5.2}
\]

Global sign symmetry kills the one-sign and three-sign expectations, while the bivariate Gaussian sign identity

\[
\mathbb E[\operatorname{sgn}(G_i)\operatorname{sgn}(G_j)]
=\frac2\pi\arcsin(\rho_{ij})
\tag{5.3}
\]

yields

\[
\Pr(G_0,G_1,G_2<0)
=\frac18+rac{\arcsin\rho_{01}+\arcsin\rho_{02}+\arcsin\rho_{12}}{4\pi}.
\tag{5.4}
\]

Thus in the cyclic case

\[
\Pr(V_0,V_1,V_2<0)
=\frac18+rac{2\arcsin(\rho_{\rm adj})+\arcsin(\rho_{\rm opp})}{4\pi}.
\tag{5.5}
\]

Machin's formula for `pi`, integer-square-root bracketing and alternating rational `arctan` series give outward rational intervals for every irrational quantity. The exact checker certifies

\[
\boxed{
\operatorname{tr}(K_{r,s}^4)
<\frac{110273}{100000}=1.10273.
}
\tag{5.6}
\]

The outward interval upper display is approximately `1.1027265797639016`, leaving a rigorous cap margin exceeding `3.42e-6`. The decimal is explanatory only; the sign decision is exact interval/rational arithmetic.

This is strictly stronger than (2.9) and required neither a four-dimensional numerical orthant routine nor any new sampling approximation.

## 6. Spectral-tail separation at the new target

Set

\[
\theta_*:=\frac{103}{625}=0.1648.
\tag{6.1}
\]

By (2.6), it is enough to prove

\[
\lambda_1<r^{4\theta_*}=r^{412/625}.
\tag{6.2}
\]

Take

\[
x=\frac{183147}{200000}=0.915735.
\tag{6.3}
\]

The checker verifies the exact integer-power inequality

\[
x^{625}<r^{412},
\tag{6.4}
\]

so `x<r^{412/625}`.

Assume for contradiction that

\[
\lambda_1\ge r^{412/625}.
\tag{6.5}
\]

Then `lambda_1>x`. Since `K_{r,s}` is compact self-adjoint,

\[
\operatorname{tr}(K_{r,s}^4)=\sum_j\lambda_j^4.
\tag{6.6}
\]

Combining (5.6) with `lambda_1>x`, every non-Perron spectral point satisfies

\[
|\lambda_j|^4
<\frac{110273}{100000}-x^4.
\tag{6.7}
\]

Choose

\[
\beta=\frac{4969}{6250}=0.79504.
\tag{6.8}
\]

The exact checker proves

\[
\beta^4-
\left(\frac{110273}{100000}-x^4\right)>0,
\tag{6.9}
\]

with displayed margin exceeding `6.63e-6`. Therefore every non-Perron spectral point lies below `beta` in absolute value, and (2.7) gives `beta<mu`.

## 7. Temple contradiction and source movement

On the spectrum,

\[
(\lambda_1-K_{r,s})(K_{r,s}-\beta I)\le0.
\tag{7.1}
\]

Taking expectation in the normalized quasimode state gives the elementary Temple inequality

\[
\varepsilon^2\ge(\lambda_1-\mu)(\mu-\beta).
\tag{7.2}
\]

Under (6.5), equations (2.7) and (6.3) imply

\[
\varepsilon^2
>
\left(
\frac{183147}{200000}
-rac{9116948313}{10^{10}}
\right)
\left(
\frac{9116948312}{10^{10}}
-rac{4969}{6250}
\right).
\tag{7.3}
\]

The checker certifies that the right side exceeds `0.000471305197718...`, while

\[
\varepsilon^2<\frac{47004495}{10^{11}}
=0.00047004495.
\tag{7.4}
\]

The exact positive contradiction margin is displayed by the checker as greater than `1.2602e-6`; the exact `Fraction` comparison, not the decimal display, decides the sign.

Hence assumption (6.5) is impossible and

\[
\lambda_1<\left(\frac78\right)^{412/625}.
\tag{7.5}
\]

Combining with (2.6) proves

\[
\boxed{\theta_{2,1/4}>\frac{103}{625}}.
\tag{7.6}
\]

Therefore

\[
W_{1/4}:
\frac{853}{10000}=0.0853
\longrightarrow
\frac{213}{2500}=0.0852.
\tag{7.7}
\]

This is a rigorous movement of the frozen source quantity. It is still only a special-`H` partial result, so the full Molchan source problem remains **OPEN** and the track remains **PARTIAL**.

## 8. Exact checker, execution, and immutable readback

The route note was committed first, before checker construction:

`artifacts/hard7_2026-09-18/HARD7-05/2026-09-19T2240Z__triple_orthant_trace_idea.md`

commit

`31de090ace9ce34af7202f20c43e8c89e932295c`.

The exact checker is

`artifacts/hard7_2026-09-18/HARD7-05/2026-09-19T2244Z__triple_orthant_trace_exact_check.py`

creation commit

`e1e0a1743b7c5e1fbcc8326ce6d8fb4ec6987fb2`.

Its theorem-deciding operations are integer/`fractions.Fraction` arithmetic or outward rational intervals for `sqrt`, `pi`, `atan` and `asin`. It was executed successfully; stdout is archived at

`artifacts/hard7_2026-09-18/HARD7-05/2026-09-19T2244Z__triple_orthant_trace_exact_check.out`

creation commit

`18911bb7b4218fae7cb87fd572c46346d24ebac3`.

The archived output ends

`ALL_EXACT_CHECKS_PASS = True`.

The route note, checker and output were each read back at their returned commits. This is a **self-check**, not an independent audit. No closure or audit request is made because the full external source problem is not solved.

## 9. What changed structurally and the next obligation

The important gain is not the `1e-4` endpoint movement by itself. The proof identifies a previously unused exact source of spectral information: the softened four-cycle can be bounded directly at its actual covariance, rather than by reverting to the hard-edge trace. Even the crude projection from four signs to three lowers the fourth-trace cap by about `0.00357`, enough to move the source endpoint.

The obvious next mathematical question is whether one can certify the **full four-dimensional orthant probability** at the same comparator. That should retain the fourth constraint discarded in (5.1) and may substantially improve the spectral-tail separation. A useful next triple, distinct from this run, is:

- **B3:** prove the stronger exact four-coordinate trace bound;
- **B8:** reduce the resulting Plackett/conditional integral to a certified finite interval computation if a clean elementary closed form does not emerge;
- **B30:** localize the integral near the only singular spectral/endpoint scales so the interval proof remains small and rigorous.

Do not repeat B1/B4/B25 next run.

### ledger_delta

```yaml
track: HARD7-05
canonical_target: MOLCHAN-2025-THETA2H
status: PARTIAL
source_status: OPEN
metric: W_{1/4} = U_{1/4} - L_{1/4}
before: 853/10000
before_decimal: 0.0853
after: 213/2500
after_decimal: 0.0852
U_1_4: 1/4
L_1_4_before: 1647/10000
L_1_4_after: 103/625
movement: 1/10000
methods: [B1, B4, B25]
shared_root_write_requested: false
next_run_avoid_methods: [B1, B4, B25]
next_methods: [B3, B8, B30]
```
