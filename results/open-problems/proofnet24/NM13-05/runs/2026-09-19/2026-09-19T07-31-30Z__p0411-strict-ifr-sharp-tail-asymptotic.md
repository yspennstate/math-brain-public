Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — not GPT-6 maximum. NO METRIC MOVEMENT: `d_bad = +infinity -> +infinity`; Section-B methods #3 PROVE SOMETHING STRONGER, #18 SAY IT IN ANOTHER LANGUAGE, and #29 ADD THE POINTS AT INFINITY were genuinely attempted, and they yielded a stronger strict-IFR / sharp-tail theorem.**

# NM13-05 — P0411 strict increasing-hazard theorem and sharp all-dimensional tail

Repository / branch: private `yspennstate/math-open-problems` / `master`  
Worker / namespace: `NM13-05` / `proofnet24/NM13-05/`  
Canonical source claim: `P0411`  
Category: **CLOSABLE OUTSIDE**  
Canonical dedup key: `boundary-hole_monotonicity_and_coefficient_positivity_for_ideal_cells`  
Shard: `4 mod 13`  
Run date: 2026-09-19 UTC

## 1. Runtime truth and control-plane status

The prompt requests GPT-6 with maximum reasoning, but this invocation actually runs as **GPT-5.6 Sol**. Authenticated reasoning-effort telemetry is not exposed, so the reasoning level is **UNVERIFIED**. I do not claim GPT-6, maximum reasoning, an hour-long execution, or a support escalation.

The exposed scheduled-task control surface still offers task title/prompt, schedule/start configuration, timing mode, enabled state, and ordinary update controls. It exposes **no bindable model-family selector, no bindable reasoning-effort selector, and no authenticated applied-runtime receipt**. Thus GPT-6/maximum remains prompt text only. Making it binding would require an authorized product/workspace/API/admin surface that persists those fields into inference routing and returns trustworthy applied-runtime metadata.

The historical P26 `You cannot modify this task` event is an authorization-context boundary. Repository continuity records a later successful P26 update from another authorized context. If such a refusal recurs, the compliant remedy is the task-owning or otherwise authorized account/workspace/API/admin context, ownership repair/transfer, or authorized platform support for that same task — never cloning the task or bypassing access controls. No schedule or permission was modified in this invocation.

## 2. Authoritative continuity recovered

I continued from the immutable NM13-05 report

`proofnet24/NM13-05/runs/2026-09-19/2026-09-19T06-40-00Z__p0411-admission-density-monotonicity-all-d.md`

created at commit `ccff76ac21582e0d0ee779f9f942c9ccf4e4c453`.

Its preserved state is:

- P0411 is lawfully and exclusively claimed by `proofnet24/NM13-05` as **MANUALLY ADMITTED / CLOSABLE OUTSIDE**;
- frozen marginal family `R_d := d_H(o, partial C_d)`, `d>=2`, with survival `H_d(u)=P(R_d>=u)`;
- frozen metric `d_bad := min{d>=2 : g_d=-H_d' is not nonincreasing}`, with `+infinity` if no such dimension exists;
- previous certified metric movement `UNMEASURED -> +infinity` via a complete all-dimensional proof that `g_d'(u)<0`;
- previous methods #2 ATTACK THE NEGATION FIRST, #8 DISCRETIZE, #11 DUALIZE are spent and were not reused as this run's named methods;
- the archived campaign result `P0411-A001` remains prior work, including the exact d=2 negative sixth Maclaurin coefficient for the literal even-dimensional positive-power-series clause; it is not NM13-05 progress;
- P26 and NM13-06 audits were still absent, so fleet closure was false.

Before new mathematics I reread/recovered the required current surfaces: `FLEET_RULES.md`; `operations/new_methods_2026-09-16/OWNER_DIRECTIVE.md`; `operations/NEW_METHODS_2026-09-16.md`; later owner-authorized `operations/NM13_DEPLOYMENT_2026-09-17T203709Z.md`; root `QUEUE.md`, `POSTED.md`, `RESULTS.md`; campaign `INDEX.md` and `RANKING.md`; the current P0411 claim; the prior `P0411-A001` attempt record and proof packet; the newest neighboring NM13-04 and NM13-06 reports; current P26 audit activity; and current primary/follow-up literature.

The current claim still names NM13-05 as owner and freezes the same metric; no handoff, retirement, claim deletion, or source-scope mutation was found.

## 3. Frozen repository delta before this write

Predecessor report creation commit: `ccff76ac21582e0d0ee779f9f942c9ccf4e4c453`.  
Final frozen pre-write `master`: `6257905fe2c336832d68b41e8ab34f869b45fe86`.

Exact Git comparison reports **77 commits ahead, 0 behind, `too_large=null`**, so the changed-file set is complete. The interval adds substantial fleet work and one new canonical claim, `operations/claims/P0458.md`, but it contains no P0411 claim deletion/release, no P0411 source/attempt rewrite, and no new P0411 audit PASS. The latest visible P26 report audits the unrelated Romero split-reliability n=8 package. The newest NM13-06 report remains on successor admission and contains no P0411 proof audit.

No shared root, peer namespace, claim file, D-series file, workflow, permission, public surface, email/Drive resource, paid-compute resource, or schedule is edited by this run.

## 4. Source and bounded literature status, refreshed 2026-09-19

Primary source: Matteo D'Achille, Nicolas Curien, Nathanael Enriquez, Russell Lyons, Meltem Unel, *Ideal Poisson-Voronoi tessellations on hyperbolic spaces*, Annals of Probability 54(2) (2026), 846-891, DOI `10.1214/25-AOP1781` (publication date 2026-03-06).

The current publicly available source PDF still states Conjecture 7.5 literally in the displayed distance variable `u`: the scaled hole probability is conjectured decreasing; odd-dimensional polynomial structure is conjectured; in even dimensions `f(u)` is asserted to be an infinite power series with positive coefficients; and the density of the boundary distance is said likely decreasing, implying median below mean. Proposition 5.1 gives `H_d(u)=1/(1+I_d(u))` and the exponential sandwich `e^{-2(d-1)u} <= H_d(u) <= e^{-(d-1)u}`. Remark 5.2 gives the d=2 closed form and only the d=2 tail asymptotic `H_2(u) ~ 2e^{-2u}`.

Fresh bounded searches dated 2026-09-19 used the exact source title together with `hazard`, `increasing failure rate`, `failure rate`, `log-concave survival`, `boundary distance`, and current author/follow-up terms. They recovered the 2026 source, D'Achille-Thale's 2026 face-volume-density work, D'Achille-Khezeli's 2026 convergence work, and Mellick's resolution of the separate indistinguishability question, but no source-matching hazard/IFR theorem or all-dimensional exact boundary-distance tail constant. This is a bounded search, **not** a worldwide-openness, novelty, or priority certificate.

The preserved attempt ledger still records `P0411-A001` as partial and without independent review. Its coefficient addendum states

`[u^6](e^{-u}/H_2(u)) = 61/240 - 4/(5*pi) < 0`,

under the literal displayed variable. That prior result is not re-counted here.

## 5. Frozen metric and counters

The metric is unchanged and is not silently replaced by the stronger theorem below.

- metric: `d_bad = min{d>=2 : g_d is not nonincreasing}`, `+infinity` if empty;
- before this run: **`+infinity`**;
- after this run: **`+infinity`**;
- movement: **NO MOVEMENT** (there is no stronger value than `+infinity` for this frozen threshold);
- unchanged runs after the metric-setting run: **`0 -> 1`**;
- stuck/recovery count: **`0 -> 0`**.

This run nevertheless obtains a genuinely stronger theorem about the same frozen marginal family rather than manufacturing a checker for an already settled number.

## 6. New theorem: strict IFR, sharp hazard endpoints, and exact tail constant

Let

`n := d-1 >= 1`, `H_d(u):=P(R_d>=u)`, `J_d(u):=1/H_d(u)`, `L_d(u):=log J_d(u)`,

and define the hazard rate

`h_d(u):=-H_d'(u)/H_d(u)=L_d'(u)`.

### Theorem

For every integer `d>=2`:

1. **strict increasing failure rate:** `h_d'(u)>0` for every `u>=0`; equivalently, `H_d` is strictly log-concave;
2. **pointwise hazard sandwich:**
   `d-1 < h_d(u) < 2(d-1)` for every finite `u>=0`;
3. **exact left endpoint:**
   `h_d(0)=2 Gamma(d/2)Gamma(d)/(Gamma((d-1)/2)Gamma(d-1/2))`;
4. **exact point at infinity:**
   `lim_{u->infinity} h_d(u)=2(d-1)`;
5. **sharp tail asymptotic:** with `n=d-1`,
   `H_d(u) ~ C_n e^{-2nu}` where
   `C_n = Gamma(n/2)Gamma(2n)/(Gamma(n)Gamma(3n/2))`.

Consequently, for `u>0`,

`e^{-2nu} < H_d(u) < e^{-nu}`,

and if `r_p` is the unique upper-tail quantile with `H_d(r_p)=p`, `0<p<1`, then

`(-log p)/(2n) < r_p < (-log p)/n`.

In particular

`(log 2)/(2n) < median(R_d) < (log 2)/n`

and

`1/(2n) < E[R_d] < 1/n`.

The last exponential/mean inequalities sharpen the source's non-strict stochastic sandwich; the new structural content is the strict IFR/log-concavity, pointwise hazard bounds, all-dimensional hazard endpoint, and exact all-dimensional tail constant.

### Proof, step 1: exact positive radial representation

Starting from Proposition 5.1's exact integral and using the same source-faithful radial reduction as the predecessor run, put

`q=e^{2u}`, `alpha=(n-2)/2`, `z>=1`.

The reciprocal survival is

`J_d(u) = K_n integral_1^infinity (z-1)^alpha z^{-2n} q^{n/2}(q+z)^alpha(q+2z-1) dz`,

where

`K_n = Gamma(n)/Gamma(n/2)^2 > 0`.

For completeness, the radial surface factor is

`|S^{n-1}|/c_d = 2 Gamma(n)/Gamma(n/2)^2`,

and the substitution from radial coordinate to `z` contributes the factor `1/2`, giving the displayed `K_n`. For `n=1`, `alpha=-1/2`, and the endpoint singularity `(z-1)^(-1/2)` is integrable. At infinity the kernel is `O(z^{-n-1})` after the relevant bounded factors, so the representation is finite for every `n>=1`.

Normalize the positive integrand to a probability measure `mu_u`. Its logarithmic `u`-score is

`A_n(q,z) = n + (n-2) q/(q+z) + 2q/(q+2z-1)`.

Differentiating under the integral is legitimate because the score is uniformly bounded on `z>=1` for fixed `n` (and the same integrable kernel dominates on compact `u`-intervals). Hence

`h_d(u)=L_d'(u)=E_{mu_u}[A_n(q,Z)]`.

### Proof, step 2: the hazard sandwich in every dimension

If `n>=2`, then both correction terms are nonnegative and strictly below their limiting coefficients, so pointwise

`n < A_n(q,z) < n+(n-2)+2 = 2n`.

For the exceptional `n=1`,

`A_1(q,z)=1-q/(q+z)+2q/(q+2z-1)`.

Direct algebra gives

`A_1-1 = q(q+1)/((q+z)(q+2z-1)) > 0`,

and

`2-A_1 = (3qz-2q+2z^2-z)/((q+z)(q+2z-1))`

`= (q(3z-2)+z(2z-1))/((q+z)(q+2z-1)) > 0`

for `q,z>=1`. Therefore `1<A_1<2`. Taking expectation proves for every `n>=1`

`n < h_d(u) < 2n`.

This already yields the strict survival/quantile/mean sandwich by integrating `d(log H_d)/du=-h_d` from zero, using `H_d(0)=1`.

### Proof, step 3: strict IFR for d>=3

For `n>=2`, differentiating the score gives

`partial_u A_n = 2(n-2) qz/(q+z)^2 + 4q(2z-1)/(q+2z-1)^2`.

Equivalently, writing `alpha=(n-2)/2`, this is

`4 alpha qz/(q+z)^2 + 4q(2z-1)/(q+2z-1)^2`.

It is strictly positive for every `q,z>=1`. It is also bounded above by `alpha+1=n/2`, since `4ab/(a+b)^2<=1`. Standard differentiation of a log-normalizer therefore gives

`h_d'(u)=L_d''(u)=E_{mu_u}[partial_u A_n] + Var_{mu_u}(A_n) > 0`.

Thus the boundary distance is strictly IFR for every `d>=3`.

### Proof, step 4: strict IFR in d=2

Use the source's exact d=2 formula. Set

`B(u):=arctan(e^u)`, `x:=sinh u`, `c:=cosh u`,

`D(u):=4B(u)c^2+2x`, so `H_2(u)=pi/D(u)` and `h_2=D'/D`.

The exact derivatives are

`D'=4c(2Bx+1)`,

`D''=8(B(2x^2+1)+x)`.

Hence

`D^2 h_2' = D D''-(D')^2`

and exact simplification gives

`(D D''-(D')^2)/16 = E(x):=2B^2(1+x^2)-Bx-1`.

Use the identity

`B = pi/4 + (1/2) arctan x`,

so `dB/dx=1/(2(1+x^2))`. Then

`E(0)=pi^2/8-1>0`,

while

`E'(x)=B+4B^2x - x/(2(1+x^2))`.

For `x>=0`, `B>=pi/4` and `x/(2(1+x^2))<=1/4`, so

`E'(x) >= pi/4-1/4 >0`.

Therefore `E(x)>0` for all `x>=0`, hence `h_2'(u)>0`. This completes strict IFR in every dimension.

### Proof, step 5: add the point u=infinity and obtain the exact tail constant

Factor `q^n` from the radial representation:

`J_d(u)/q^n = K_n integral_1^infinity w_n(z) R_q(z) dz`,

where

`w_n(z)=(z-1)^alpha z^{-2n}`,

`R_q(z)=(1+z/q)^alpha (1+(2z-1)/q)`.

For each fixed `z`, `R_q(z)->1` as `q->infinity`.

For `n>=2` (`alpha>=0`), `R_q(z)` is bounded by `(1+z)^alpha(1+2z)`, and multiplication by `w_n` gives an integrable `O(z^{-n-1})` tail. For `n=1`, `(1+z/q)^(-1/2)<=1` and the bound `1+2z` gives an integrable `O(z^{-3/2})` tail, with the integrable `(z-1)^(-1/2)` singularity at one. Dominated convergence therefore yields

`lim_{u->infinity} J_d(u)/q^n`

`= K_n integral_1^infinity (z-1)^alpha z^{-2n} dz`

`= K_n B(n/2,3n/2)`

`= Gamma(n)Gamma(3n/2)/(Gamma(n/2)Gamma(2n))`.

Since `q^n=e^{2nu}`, inversion gives

`H_d(u) ~ [Gamma(n/2)Gamma(2n)/(Gamma(n)Gamma(3n/2))] e^{-2nu}`,

which is the claimed constant `C_n`. As checks, `C_1=2`, agreeing with the source's d=2 tail, and `C_2=3`, agreeing with the source's explicit d=3 formula.

Finally, strict IFR and `h_d(u)<2n` imply that `h_d` has a finite limit `ell<=2n`. But

`L_d(u)=2nu+O(1)`

from the just-proved asymptotic, while

`L_d(u)-L_d(0)=integral_0^u h_d(t)dt`.

The Cesaro mean of the increasing function `h_d` tends to its limit `ell`, whereas `L_d(u)/u->2n`. Hence `ell=2n`, proving the exact hazard endpoint.

The exact left endpoint follows from the source's Proposition 5.3 / small-radius identity

`-H_d'(0)/2 = Gamma(d/2)Gamma(d)/(Gamma((d-1)/2)Gamma(d-1/2))`.

Because `H_d(0)=1`, this is exactly the asserted formula for `h_d(0)`.

This proves the theorem. QED.

## 7. Section-B methods actually tried

### #3 PROVE SOMETHING STRONGER — success

Instead of adding another lemma to density monotonicity, I asked for a stronger structural law of the same distribution. The score representation proves strict **increasing failure rate** in every dimension, not merely decreasing density. It also produces a pointwise hazard sandwich. This route succeeded.

### #18 SAY IT IN ANOTHER LANGUAGE — success

Rewriting the boundary-distance law in reliability-theory language exposed the right object: the hazard `h=-H'/H` is a derivative of a positive log-normalizer. The covariance/score identity then makes monotonicity transparent for `d>=3`, while the d=2 source formula closes the endpoint. In this language the theorem is equivalently strict log-concavity of the survival function. This route succeeded and was more informative than another direct `g'` calculation.

### #29 ADD THE POINTS AT INFINITY — success

I compactified the parameter by treating `u=infinity` as a genuine endpoint of the positive radial integral. Factoring `q^n` and applying dominated convergence gives the exact all-dimensional tail constant, and strict IFR then forces the hazard to converge to the sharp endpoint `2(d-1)`. This route succeeded; it also checks against the source's d=2 asymptotic and explicit d=3 formula.

These are not the previous run's #2/#8/#11 routes.

## 8. Status of the literal source conjunction

This run does **not** overwrite preserved campaign history. The earlier campaign coefficient addendum already gives an exact negative sixth Maclaurin coefficient for the literal even-dimensional clause in the displayed variable `u`. The current source PDF still literally phrases that clause as an infinite power series `f(u)` with positive coefficients; it does not insert a transformed variable in the displayed Conjecture 7.5 sentence.

Therefore the honest state is:

- literal displayed even-dimensional positive-coefficient clause: **REFUTED candidate under the literal variable, preserved prior work**;
- density-decreasing clause: **PROVED candidate for all d>=2 by the predecessor NM13-05 run**;
- stronger strict-IFR / exact-tail theorem: **PROVED candidate on this report page**;
- source-wide protocol closure: **NOT CLOSED**, because source-interpretation/prior-art review and two independent audits are still missing.

I do not call the package fleet-CLOSED and do not create a paper folder yet.

## 9. Audit / closure gates

Current repository search and neighboring-report reads recover **no P0411 source-level PASS from P26 and no P0411 PASS from NM13-06**. The newest P26 report audits `ROMERO-2025-SPLIT8`, not P0411. The newest NM13-06 report is still in successor-admission mode. Thus audit count remains `0/2` for P0411.

There is no finite core in the new IFR/tail theorem requiring a new checker: the claim is analytic and the full proof is written above. The prior exact coefficient obstruction and the predecessor symbolic density self-check remain preserved separately. Creating another certificate for an unchanged metric would violate the owner-directed 90/10 research emphasis.

Next mathematical/closure step: have an independent auditor attack the positive-integral score derivation, the d=2 IFR algebra, and the dominated-convergence tail constant; in parallel, deepen the source-interpretation/prior-art check for the even-dimensional `f(u)` clause. Do not change the frozen metric.

## 10. Structured ledger delta for P26

```yaml
ledger_delta:
  worker: NM13-05
  source_id: P0411
  claim_id: P0411
  owner: proofnet24/NM13-05
  category: CLOSABLE OUTSIDE
  canonical_residue: 4
  frozen_metric: d_bad
  metric_definition: "min d>=2 with non-nonincreasing density; +infinity if none"
  metric_before: +infinity
  metric_after: +infinity
  movement: NO_MOVEMENT
  unchanged_runs_before: 0
  unchanged_runs_after: 1
  recovery_count_before: 0
  recovery_count_after: 0
  methods: [3, 18, 29]
  method_outcomes:
    3: "SUCCESS: strict IFR/log-concave survival all dimensions"
    18: "SUCCESS: reliability-theory hazard representation exposes log-normalizer structure"
    29: "SUCCESS: exact all-dimensional tail constant and hazard endpoint at infinity"
  new_theorem:
    hazard: "strictly increasing; d-1 < h_d(u) < 2(d-1)"
    hazard_limit: "2(d-1)"
    tail_constant: "Gamma((d-1)/2) Gamma(2d-2) / [Gamma(d-1) Gamma(3(d-1)/2)]"
  literal_even_coefficient_clause: "prior campaign REFUTED candidate under literal displayed variable"
  density_clause: "PROVED candidate all d>=2"
  audits_required: [P26, NM13-06]
  audits_passed: []
  fleet_closed: false
  exact_finite_core_new_this_run: none
  prior_art_scope: "bounded 2026-09-19 exact-title/author/hazard/IFR/log-concavity/follow-up search; worldwide novelty UNVERIFIED"
  shared_root_edits: none
  peer_edits: none
  scheduler_changes: none
  next_step: "independent audit of score/IFR/tail proof plus deeper source-variable/prior-art interpretation audit"
```

End of immutable NM13-05 run report.