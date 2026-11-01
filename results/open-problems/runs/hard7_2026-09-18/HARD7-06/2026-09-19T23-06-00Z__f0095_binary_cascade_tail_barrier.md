Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — this is not GPT-6 maximum, and I do not claim otherwise. NO FIXED-METRIC MOVEMENT: `W_3: 0.6565076260769 -> 0.6565076260769`; methods actually used: B16 / B23 / B25.**

# HARD7-06 run 27 — an exact binary-cascade lower-tail barrier for the cavity fixed point

Status: **F0095 OPEN / HARD7-06 PARTIAL.** The source-level constant-location problem for ordinary sparse Erdos--Renyi 3-colourability remains open. This run does not shave another decimal from the current Ayre--Coja-Oghlan--Greenhill (ACG) variational upper endpoint. Instead it proves a new quantitative obstruction on the infinite-support cavity branch: at the current degree, any nontrivial cavity fixed point is forced onto the large positive-mass branch and its exact two-input multiplicative sector forces a lower-tail cascade exponent

`5.03 < beta_bin < 5.04`,

with every negative moment of order `s>beta_bin` infinite. In particular the `126/25=5.04` negative moment is infinite. This is a theorem about the exact distributional fixed-point branch, not a simulation or a claim that such a branch is globally variationally optimal.

Repository / branch: private `yspennstate/math-open-problems` / `master`.

## 1. Continuity, ownership, exclusions, and required reads

I resumed canonical create-only claim `operations/claims/F0095.md`, owned by HARD7-06. I did not reopen random 3-SAT/F0097, the exhausted regular-hypergraph predecessor, the active negative-margin perceptron, resolved SK AT work, or any posted/owned equivalent.

The source remains Alan Frieze's ICM 2014 chromatic-number conjecture, frozen at `k=3`: there should be a constant average-degree location for the ordinary sparse Erdos--Renyi 3-colourability transition. This is the constant-location question, not merely Achlioptas--Friedgut sharpness around an `n`-dependent threshold sequence.

At run start I reread/recovered the controlling HARD7 policy, `operations/NEW_METHODS_2026-09-16.md`, `operations/new_methods_2026-09-16/OWNER_DIRECTIVE.md`, campaign `INDEX.md` and `RANKING.md`, root `POSTED.md`, `RESULTS.md`, and `QUEUE.md`, the F0095 claim/intake provenance, the newest HARD7-06 checkpoint, and current neighboring random-graph state. Large registries/intake files are connector-truncated, so I used canonical-ID/source/alias targeted recovery and do not represent that as a byte-for-byte scan of every large file. No conflicting owner, release, posted equivalent, or source closure surfaced.

Repository searches found no earlier F0095 section headings for the new triple **B16/B23/B25**. The immediately preceding run used B1/B13/B29.

### Capability honesty

The exposed task-control surface still provides title/prompt/schedule-timing/enabled controls but no model-family selector, reasoning-effort selector, authenticated runtime telemetry, or guaranteed duration. GPT-6/maximum therefore remains prompt-requested only. Changing the actual runtime model/reasoning requires the platform to expose those controls in the authorized task/workspace context; a GitHub edit cannot do it.

The repository policy records historical `You cannot modify this task` denials for protected task IDs including P26 in some contexts and later successful modification from a different authorized context. The compliant workaround for any denied task remains the authorized owning account/workspace interface or platform support, never permission bypass or a duplicate schedule. I did not probe, create, reactivate, or modify any other schedule.

## 2. Fresh bounded literature/status check

A bounded current search on 19 September 2026 UTC / 20 September local again found no source-matching resolution of fixed ordinary `G(n,d/n)` 3-colourability threshold-location convergence.

- Achlioptas--Friedgut, *A Sharp Threshold for k-Colorability*, Random Structures & Algorithms 14 (1999), first published 7 January 1999, proves an `n`-dependent threshold location for fixed `k>=3`, not convergence of the `k=3` location to a constant: `https://onlinelibrary.wiley.com/doi/abs/10.1002/(SICI)1098-2418(1999010)14:1%3C63::AID-RSA3%3E3.0.CO;2-7`.
- Ayre--Coja-Oghlan--Greenhill, *Lower bounds on the chromatic number of random graphs*, arXiv:1812.09691 / Combinatorica 42 (2022), remains the interpolation/variational upper-bound engine used by this track: `https://arxiv.org/abs/1812.09691`.
- Mizgerd--Perkins--Wang, *On the Chromatic Number of Random Triangle-Free Graphs*, Random Structures & Algorithms 68 (2026), first published 6 June 2026, proves scaling windows for a different triangle-free conditioned model at a different density scale: `https://doi.org/10.1002/rsa.70081`.

Searches for ordinary random-graph `3-colorability threshold`, `k=3 threshold convergence`, and 2025--2026 follow-ups did not recover a source-matching closure. This is bounded negative evidence, not a worldwide openness or novelty certificate. F0095 remains **OPEN**.

## 3. Frozen metric: second no-movement run after the last endpoint improvement

The fixed source-relevant quantity remains

`W_3 := U_3-L_3`,

with

`L_3=4.03`, `U_3<=4.6865076260769`.

Therefore

`W_3 <= 0.6565076260769`.

This run changes neither endpoint:

`W_3: 0.6565076260769 -> 0.6565076260769`.

This is the **second** unchanged run after the run-25 endpoint movement. Section I's three-consecutive-run stuck trigger therefore does not fire yet. The new `beta_bin` below is an auxiliary structural quantity and is not substituted for the frozen `W_3` metric.

## 4. Carry-in exact cavity representation

Use the established coordinate

`t=(1-x)/3 in [0,1/3]`.

For a finite multiset `N={t_i}`, set

`A=prod_i(1-t_i)`, `B=prod_i(1-2t_i)`, `C=prod_i(1-3t_i)`,

and

`R(N)=(A-2B+C)/(3A-3B+C)`.

For a probability law `a` on `[0,1/3]`, let `N_a` be a Poisson point process of intensity `d a` and let `C_d(a)=Law(R(N_a))`. The previous contact-analyticity argument reduced every nontrivial infinite-support stationary branch to the exact fixed-point equation

`a=C_d(a)`.

Run 26 proved the two-input identity

`R({s,t})=2st`.

Introduce the rescaled message

`Y=2T in [0,2/3]`.

Then on exactly two positive inputs,

`Y_out=Y_1 Y_2`.                                                   (4.1)

This exact multiplicative sector is the sole input needed for the main theorem below.

## 5. B16 — exact small-count atlas

For completeness, the first active-input sectors are now explicit:

- zero or one positive input: `R=0`;
- exactly two positive inputs: `R({s,t})=2st`;
- exactly three positive inputs:

`R({s,t,u}) = 2(st+su+tu-6stu)/(1-6stu)`.                         (5.1)

Indeed direct expansion gives

`A-2B+C = 2(st+su+tu-6stu)`,

`3A-3B+C = 1-6stu`.

Equation (5.1) shows why the two-input sector is exceptional: after the linear rescaling `Y=2T` it is an exact product with no denominator or correction term. That makes it possible to propagate a rigorous lower-tail recursion through arbitrarily many generations.

## 6. Current-degree scalar branches and re-exclusion of the small one

Let

`q=P(Y>0)`

under a nontrivial cavity fixed point. Because `R(N)=0` iff the number of positive incoming messages is at most one, Poisson thinning gives the exact scalar equation

`q = 1-exp(-dq)(1+dq)`.                                           (6.1)

Put

`h(q)=1-q-(1+dq)exp(-dq)`.

Then

`h'(q)=d^2 q exp(-dq)-1`.

The function `q exp(-dq)` increases up to `1/d` and decreases thereafter, so `h'` has at most two zeros. Hence, besides `q=0`, equation (6.1) has at most two positive roots. At the current exact degree

`d=46865076260769/10^13=4.6865076260769`,

the exact Taylor-enclosure certificate proves

`h(0.138)<0<h(0.139)`,

`h(0.9319)>0>h(0.932)`.

Thus these are the two nonzero scalar branches.

The earlier small-branch exclusion was certified at the preceding, slightly larger decimal degree. This run does **not** silently transfer it: the exact checker re-runs the degree-dependent inequalities at the current `d`.

In the equivalent variable `Lambda=t/(1-t) in [0,1/2]`, every nontrivial full cavity fixed point has mean `m=E Lambda` satisfying

`m <= (1-exp(-dm))^2 < d^2 m^2`,

hence

`m>1/d^2`.                                                        (6.2)

On the other hand, conditioning on the number `K` of positive inputs and using coordinatewise cavity monotonicity gives the fixed-count envelope

`t_0=t_1=0`, `t_2=2/7`, `t_3=2/5`, `t_k<1/2` for `k>=4`.

Therefore, if `q<0.14`,

`m <= Mbar(0.14d)`,

where

`Mbar(a)=(2/7)P(Pois(a)=2)+(2/5)P(Pois(a)=3)+(1/2)P(Pois(a)>=4)`.

The current exact certificate proves

`Mbar(0.14d) < 0.04397661139582855...`,

while

`1/d^2 > 0.04553038722255834...`,

with strict certified margin greater than `0.0015537758267`. This contradicts (6.2). Hence the small branch is impossible at the **current** degree, and every nontrivial cavity fixed point satisfies

`0.9319 < q < 0.9320`.                                            (6.3)

## 7. B23 — assume the infinite-support branch exists and force a lower-tail cascade

Rather than trying again to rule out the surviving fixed point, assume it exists and ask what geometry it must have.

Let `mu` be its law in the `Y` coordinate and define the positive lower tail

`G(y)=mu((0,y])`, `0<y<=2/3`.

Positive incoming marks form a Poisson process of total intensity `dq`; zero marks are neutral. Restrict the output to the event of **exactly two** positive marks and no other positive marks. By (4.1), Campbell counting gives

`G(y) >= c int int 1_{uv<=y} mu(du)mu(dv)`,                      (7.1)

where the integrals are over positive messages and

`c = exp(-dq)d^2/2`.                                              (7.2)

Restricting further to `u,v<=sqrt(y)` yields the nonlinear recursion

`G(y) >= c G(sqrt(y))^2`.                                        (7.3)

Set

`y_n=(2/3)^(2^n)`.

Since `G(2/3)=q`, iteration of (7.3) gives for every `n>=0`

`G(y_n) >= c^(2^n-1) q^(2^n)`.                                  (7.4)

Define

`beta_bin := log(cq)/log(2/3)`.                                  (7.5)

Then (7.4) becomes the explicit lower-tail barrier

`G(y_n) >= c^(-1) y_n^(beta_bin)`.                               (7.6)

No power-law ansatz is used: (7.6) is an exact lower bound along a specified doubly-exponential sequence.

The zero-atom equation (6.1) removes the exponential from the cascade coefficient:

`exp(-dq)=(1-q)/(1+dq)`,

so

`cq = d^2 q(1-q)/[2(1+dq)]`.                                    (7.7)

On the large interval (6.3), the right side is strictly decreasing because its derivative has the sign of

`1-2q-dq^2<0`.

The exact rational power comparisons in the checker prove

`5.03 < beta_bin < 5.04`.                                        (7.8)

The finite-precision endpoint values printed for orientation are

`0.1296567490621902 < cq < 0.1298448250371692`.

The proof of (7.8), however, is exact: it clears the exponents and checks

`[cq(q=0.9319)]^100 < (2/3)^503`,

`[cq(q=0.9320)]^25 > (2/3)^126`

with rational arithmetic.

## 8. B25 — the same binary event forces negative-moment blow-up

For `s>0`, define the unnormalised positive-part negative moment

`M_s = E[Y^{-s};Y>0] in [0,infinity]`.

On exactly two positive inputs, (4.1) gives `Y_out^{-s}=Y_1^{-s}Y_2^{-s}`. Therefore the exact Poisson contribution of this sector is

`E[Y_out^{-s}; K_+=2] = c M_s^2`.                               (8.1)

Fixed-point equality implies

`M_s >= c M_s^2`.                                                (8.2)

If `M_s` were finite, (8.2) would force

`M_s <= 1/c`.                                                     (8.3)

But every positive message obeys `Y<=2/3`, so

`M_s >= q(3/2)^s`.                                               (8.4)

Combining (8.3)--(8.4), finiteness is impossible whenever

`cq > (2/3)^s`.                                                   (8.5)

By definition (7.5), `(2/3)^beta_bin=cq`. Since the base `2/3` is below one, (8.5) holds for every

`s>beta_bin`.

### Theorem 8.1 — binary-cascade singularity

At `d=4.6865076260769`, every nontrivial cavity fixed point satisfies (6.3), has a binary-cascade exponent obeying (7.8), and

`M_s=infinity for every s>beta_bin`.

In particular, because `beta_bin<126/25`,

`E[Y^(-126/25);Y>0]=infinity`,

and therefore also

`E[Y^-6;Y>0]=infinity`.                                          (8.6)

This is a genuine regularity obstruction on the continuum cavity branch. For example, any proposed fixed-point density/tail estimate strong enough to imply a finite `5.04`-negative moment is impossible. The theorem does **not** assert finiteness of the fifth moment, identify the actual asymptotic tail exponent, or prove that the infinite-support fixed point is a global minimizer of the ACG functional.

## 9. Why this changes the route

The preceding runs established that a nontrivial fixed point has support accumulating at both boundaries. The present theorem quantifies the difficult boundary: the small-message accumulation cannot be arbitrarily thin. The exact two-input sector alone forces a lower-tail cascade with exponent in the narrow certified interval `(5.03,5.04)`.

This suggests a materially different next route from decimal endpoint optimization: derive a second-variation or contact-integrability condition for an ACG minimizer near `Y=0` and compare its required regularity with Theorem 8.1. If such a condition forces a finite negative moment above `beta_bin`, the entire infinite-support stationary branch would be excluded, leaving only the finite/contact branch. No such implication is claimed in this run.

## 10. Exact artifact and execution record

Idea-before-code checkpoint:

- `artifacts/hard7_2026-09-18/HARD7-06/2026-09-19T22-47-00Z__f0095_binary_cascade_idea.md`
- creation commit `ff788445eda4937852ff7012fd0126282d41e9af`
- read back successfully at that commit.

Exact checker:

- `artifacts/hard7_2026-09-18/HARD7-06/2026-09-19T22-58-00Z__f0095_binary_cascade_exact.py`
- creation commit `a3730752bd3f32f8afb3832e4d13cb9d739de614`
- read back successfully at that commit.

Executed output:

- `artifacts/hard7_2026-09-18/HARD7-06/2026-09-19T22-58-00Z__f0095_binary_cascade_exact.out`
- creation commit `b71c76841b22b14d8b293c3505c36bf8331a45f4`
- read back successfully at that commit.

The output ends

`ALL_EXACT_CHECKS_PASS = True`.

The checker uses only Python integer arithmetic and `fractions.Fraction` in every assertion. Exponential signs are enclosed by positive Taylor partial sums plus a geometric bound on the positive remainder. Printed decimals are display only.

## 11. Honest status and next checkpoint

Status remains **PARTIAL / OPEN**. The source problem is not solved, and no endpoint movement is claimed. This is the second consecutive unchanged `W_3` run after a moving checkpoint, so Section I does not yet require a stuck report. If the next run also leaves the fixed metric and remaining source obligation unchanged, it must invoke the Section-I thinking-only protocol rather than simply adding another cavity lemma.

The next substantive route should not repeat B16/B23/B25. The concrete mathematical checkpoint exposed here is: determine whether measure-level local minimality/contact regularity supplies an integrability estimate incompatible with (8.6), or whether the singular fixed point survives the second variation.

### ledger_delta

```yaml
track: HARD7-06
target: F0095
status: PARTIAL
source_status: OPEN
metric: W_3 = U_3 - L_3
before: 0.6565076260769
after: 0.6565076260769
L_3: 4.03
U_3: 4.6865076260769
movement: none
unchanged_streak_after_last_move: 2
methods: [B16, B23, B25]
auxiliary_new_result:
  binary_cascade_exponent: "5.03 < beta_bin < 5.04"
  negative_moment_obstruction: "M_s=infinity for every s>beta_bin; in particular M_(126/25)=infinity"
  small_scalar_branch_at_current_degree: excluded
source_closed: false
shared_root_write_requested: false
```
