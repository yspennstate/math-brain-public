Model actually running: **GPT-5.6 Sol. Reasoning level: UNVERIFIED** — this is **not GPT-6 at maximum**; no authenticated runtime model/effort telemetry or binding selector is exposed.

# C0117 — sharp mean cover-time asymptotics and geometric-mean saturation

## 1. Scope and recovered inputs

Repository: `yspennstate/math-open-problems`, branch `master`.

Opening/captured master for the delivery phase: `caa07f0e469c9e3301c39f0233608d9ca784271c`.

Canonical target: `C0117`, Ding–Lee–Peres, *Cover times, blanket times, and majorizing measures*, Annals of Mathematics 175 (2012), Section 5, Question 5.2.  The source asks, in the regime `t_cov/t_hit -> infinity`, whether cover-time standard deviation is universally bounded on the `t_hit` scale and whether the centered cover time has constant-rate exponential decay on that scale.

Current R7-03 construction: for `k>=3`, let `G_k` consist of

- a center `s`;
- `k` pendant leaves `a_1,...,a_k` adjacent to `s`;
- a clique `Q={g,q_2,...,q_k}` of size `k`;
- one bridge edge `s--g`.

The previous immutable report

`research7_2026-09-17/R7-03/runs/2026-09-19/2026-09-19T042246Z__report.md`

at creation commit `bc734508acda2b06a7fa82f1956923bca39e3b7a` established the following ingredients, which are reused rather than reproved from zero here:

1. exact maximal hitting time
   
   `h_k := t_hit(G_k) = 2 k^2 + k + 1`;

2. for every starting sequence `x_k`,
   
   `Var_{x_k}(tau_cov)/(h_k^2 log k) -> 1/2`;

3. for every starting sequence `x_k`,
   
   `(tau_cov-t_cov)/(h_k sqrt((log k)/2)) => N(0,1)`;

4. from `s`, if `Lambda_k` is the time until all `k` leaves have been visited, then
   
   `E Lambda_k = (k^2+k+2) H_k - 1`;

5. if `D_k := tau_cov-Lambda_k` is the residual time after all leaves are collected, then
   
   `P(D_k>0)=O(log k/k)`
   
   and the prior fresh-cover second-moment argument yields
   
   `E D_k^2 <= 24 P(D_k>0) t_cov(G_k)^2`;

6. Matthews' bound and the exact `h_k` give
   
   `t_cov(G_k)=O(k^2 log k)`.

The new work below converts these ingredients into the full first two asymptotic orders of the mean cover time and shows that the already-proved fluctuation theorem exactly saturates the geometric-mean scale `sqrt(t_hit t_cov)`.

## 2. Method B4 — prove a weaker quantity completely: the residual after leaf collection is `o(k^2)` in mean

Start the walk at `s`.  Since `D_k>=0`, Cauchy–Schwarz and the recovered second-moment estimate give

`E_s D_k <= sqrt(E_s D_k^2)`

`<= sqrt(24 P_s(D_k>0)) t_cov(G_k)`.

Using

`P_s(D_k>0)=O(log k/k)`

and

`t_cov(G_k)=O(k^2 log k)`, 

we obtain

`E_s D_k = O(k^2 log k sqrt(log k/k))`

`= O(k^(3/2) (log k)^(3/2))`

`= o(k^2)`.

Therefore

`E_s tau_cov`

`= E_s Lambda_k + E_s D_k`

`= (k^2+k+2) H_k - 1 + o(k^2)`.                        (2.1)

This is stronger than the previous `Theta(k^2 log k)` statement and is the key input for locating the worst start to second order.

## 3. A sharp sandwich for `t_cov`

Let `q` be any non-gateway clique vertex.  The previous exact hitting-time calculation gives

`E_q T_s = k^2`.                                           (3.1)

No leaf can be visited before the first hit on `s`, because every path from the clique to a leaf passes through `s`.  At time `T_s`, all `k` leaves are therefore still unvisited.  By the strong Markov property, the future time required merely to visit every leaf has the same law as `Lambda_k` started from `s`, independently of the pre-`T_s` history.  Covering the whole graph cannot occur before all leaves have been visited, so pathwise

`tau_cov >= T_s + Lambda_k'`,

where `Lambda_k'` is an independent post-`T_s` copy of the leaf-completion clock.  Hence

`E_q tau_cov >= k^2 + E Lambda_k`

`= k^2 + (k^2+k+2)H_k - 1`.                              (3.2)

Because `t_cov=max_x E_x tau_cov`, this is a lower bound for `t_cov`.

For the upper bound, fix an arbitrary starting vertex `x`.  Stop at `T_s`.  Whatever vertices have already been visited can only reduce the remaining cover obligation.  Thus, conditionally on the history through `T_s`, the expected additional time to cover the graph is at most the fresh cover expectation from `s`.  Therefore

`E_x tau_cov <= E_x T_s + E_s tau_cov`.

The exact hitting-time table from the previous package gives

`max_x E_x T_s = k^2`,

attained by each non-gateway clique vertex.  Taking the maximum over `x` and then using (2.1),

`t_cov <= k^2 + E_s tau_cov`

`= k^2 + (k^2+k+2)H_k - 1 + o(k^2)`.                    (3.3)

Combining (3.2) and (3.3) proves the sharp sandwich

`0 <= t_cov - [k^2 + (k^2+k+2)H_k - 1] <= o(k^2)`,

hence the theorem

> **Theorem 3.1 (sharp mean asymptotic).**
> 
> `t_cov(G_k) = k^2 + (k^2+k+2) H_k - 1 + o(k^2)`.

Since

`H_k = log k + gamma + O(1/k)`,

where `gamma` is Euler's constant, this is equivalently

`boxed: t_cov(G_k) = k^2 log k + (1+gamma) k^2 + o(k^2).` (3.4)

In particular, because

`h_k=2k^2+k+1`,

we obtain the two-term normalized expansion

`boxed: t_cov(G_k)/h_k = (1/2) log k + (1+gamma)/2 + o(1).` (3.5)

A further byproduct is that a non-gateway clique start is asymptotically worst through `o(k^2)`: from (3.2)--(3.3),

`0 <= t_cov - E_q tau_cov <= o(k^2)`.

No assertion of an exact worst start for finite `k` is needed.

## 4. Method B7 — take the limit in the natural geometric-mean normalization

The preceding run proved

`Var_{x_k}(tau_cov)/(h_k^2 log k) -> 1/2`

uniformly with respect to the choice of starting sequence in the sense that the same asymptotic holds for every `x_k`.

By (3.5),

`t_cov/(h_k log k) -> 1/2`.

Therefore

`Var_{x_k}(tau_cov)/(h_k t_cov)`

`= [Var_{x_k}(tau_cov)/(h_k^2 log k)] / [t_cov/(h_k log k)]`

`-> (1/2)/(1/2)=1`.                                      (4.1)

Thus

`boxed: SD_{x_k}(tau_cov)/sqrt(t_hit t_cov) -> 1.`        (4.2)

The same substitution sharpens the CLT.  The ratio of the previous CLT denominator to the geometric-mean denominator is

`[h_k sqrt((log k)/2)] / sqrt(h_k t_cov)`

`= sqrt( [(h_k log k)/2] / t_cov )`

`-> 1`

by (3.5).  Slutsky's theorem therefore gives

> **Theorem 4.1 (geometric-mean CLT).** For every sequence of starting vertices `x_k`,
> 
> `boxed: (tau_cov-t_cov)/sqrt(t_hit(G_k) t_cov(G_k)) => N(0,1).`

This identifies not only the order but the asymptotic variance constant on the geometric-mean scale.

## 5. Method B24 — identify the extremal object for the interpolation exponent

For `beta in [1/2,1]`, define the interpolation denominator

`D_beta(k) = h_k^beta t_cov^(1-beta)`.

Using (4.2),

`SD/D_beta`

`~ sqrt(h_k t_cov) / [h_k^beta t_cov^(1-beta)]`

`= (t_cov/h_k)^(beta-1/2)`.

By (3.5),

`boxed: SD/D_beta ~ ((log k)/2)^(beta-1/2).`              (5.1)

Consequences:

- if `beta=1/2`, the ratio tends to `1`;
- if `beta>1/2`, the ratio diverges to `infinity`;
- formally, for `beta<1/2` the ratio tends to `0`.

Thus this single elementary unweighted graph family places the transition exactly at `beta=1/2`.  It does not merely show that the pure `t_hit` endpoint `beta=1` fails: it proves that **every** interpolation exponent strictly above `1/2` fails and that the geometric-mean exponent itself is attained at constant order, with limiting standard-deviation ratio one.

For the R7-03 frozen metric `beta_cert`, this means that the persistent value `1/2` is not an artifact of a stalled proof search.  The family itself certifies that no universal source-compatible theorem can have a larger exponent.

## 6. Relation to the source question and literature

The source question is therefore mathematically refuted more strongly than in the earlier reports:

1. `t_cov/t_hit = (1/2) log k + O(1) -> infinity`, exactly the source regime;
2. `SD/t_hit ~ sqrt((log k)/2) -> infinity`, so no universal `O(t_hit)` fluctuation bound exists;
3. the previously proved CLT supplies positive upper-tail mass at deviations of order `sqrt(log k) t_hit`, ruling out universal constant-rate exponential decay on the `t_hit` scale;
4. the same family has `SD ~ sqrt(t_hit t_cov)`, showing that the geometric-mean scale is asymptotically exact here.

Fresh literature screening on 2026-09-19 rechecked:

- Ding–Lee–Peres (2012), Annals of Mathematics, Question 5.2;
- Alex Zhai, *Exponential concentration of cover times* (EJP 2018 / arXiv:1407.7617), whose abstract states a general GFF-based concentration estimate asymptotically sharp when `t_hit/t_cov -> 0`;
- Jonathan Hermon's 2020 spectral characterization of qualitative cover-time concentration under structural hypotheses;
- Berestycki–Hermon–Teyssier work on vertex-transitive cover-time fluctuations and refined hitting-time approximations, including 2026 updates.

No retrieved source states this unrestricted `G_k` counterexample or the asymptotic identities (3.4)--(5.1).  That is bounded negative evidence only and is **not** a novelty certificate.

## 7. Audit and closure status

Mathematical source status: **REFUTED**.

Protocol closure status: **INCOMPLETE**.  Repository search on this run found no actual `P26-AUDIT-C0117...=PASS` record and no distinct OTHER-track full-proof PASS.  The existing

`research7_2026-09-17/R7-03/paper_C0117_cover_time_counterexample/AUDIT_REQUEST.md`

is only a passive request and counts as neither audit.  The self-contained paper package and dated prior-art file already exist, but the two required independent audits are absent.

This artifact is a mathematical strengthening, not an independent audit and not a public-posting claim.
