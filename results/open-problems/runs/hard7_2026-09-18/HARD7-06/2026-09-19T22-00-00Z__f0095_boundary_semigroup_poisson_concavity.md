Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — this is not GPT-6 maximum, and I do not claim otherwise. NO FIXED-METRIC MOVEMENT: `W_3: 0.6565076260769 -> 0.6565076260769`; methods actually used: B1 / B13 / B29.**

# HARD7-06 run 26 — multiplicative cavity semigroup, two-boundary support, and strict Poisson concavity

Status: **F0095 OPEN / HARD7-06 PARTIAL.** The source-level constant-location problem for ordinary sparse Erdos--Renyi 3-colourability remains open. This run does not shave another decimal from the certified upper endpoint. It instead proves three structural facts about the Ayre--Coja-Oghlan--Greenhill (ACG) variational route isolated in run 25:

1. **B1:** the exactly-two-input cavity rule is multiplication after a linear rescaling, and therefore every nontrivial cavity fixed point has infinite support accumulating at zero;
2. **B29:** the opposite endpoint `1/3` is never an atom of a cavity fixed point but is necessarily a support accumulation point, with an explicit positive lower bound on every sufficiently high endpoint collar;
3. **B13:** the Poisson vertex term is strictly concave in active intensity for every nontrivial finite active shape, and the neutral-atom quotient ratio `D_b(lambda)/lambda` is strictly decreasing from infinity to a limit below one. Hence every fixed active shape has a **unique** active-intensity feasibility crossing `D_b(lambda)=lambda`.

These are theorem-sized analytic statements, not simulation claims. They materially constrain both branches left by the previous finite-support/contact versus distributional-fixed-point analysis. Novelty of the exact formulations is **UNVERIFIED**; cavity fixed-point machinery itself is established prior art and is not claimed as new.

Repository / branch: private `yspennstate/math-open-problems` / `master`.

## 1. Continuity, ownership, required reads, and capability honesty

I resumed the canonical create-only claim `operations/claims/F0095.md`, owned by HARD7-06. I did not reopen random 3-SAT/F0097, the exhausted regular-hypergraph predecessor, the stale negative-margin-perceptron title, resolved SK AT work, or any posted/owned equivalent.

The retained external source is Alan Frieze's ICM 2014 chromatic-number conjecture, frozen at `k=3`: there should be a constant average-degree location for the ordinary sparse Erdos--Renyi 3-colourability transition. The target is convergence of the threshold location, not merely Achlioptas--Friedgut sharpness around an `n`-dependent threshold sequence.

At run start I reread/recovered the controlling HARD7 policy, the latest `operations/NEW_METHODS_2026-09-16.md`, `operations/new_methods_2026-09-16/OWNER_DIRECTIVE.md`, campaign `INDEX.md` and `RANKING.md`, root `POSTED.md`, `RESULTS.md`, and `QUEUE.md`, the F0095 claim and intake provenance, the newest HARD7-06 checkpoint, and current neighboring random-graph/configuration-model state. In particular, the newest HARD7-04 checkpoint has moved onto a heavy-tailed configuration-model MST collar/MD5 route, and the newest R14 checkpoint is the distinct van-der-Hofstad configuration-model duality problem; neither collides with F0095. Large registries/intake files are connector-truncated, so I used canonical-ID/source/alias targeted recovery and do not represent that as a byte-for-byte scan of every large file. No conflicting owner, release, posted equivalent, or source closure surfaced.

The scheduler/control surface still exposes title, prompt, schedule/timing mode and enabled state, but **no model-family selector, reasoning-effort selector, authenticated runtime telemetry, or guaranteed execution duration**. GPT-6/maximum therefore remains prompt-requested only. Changing the actual runtime model/reasoning requires the platform to expose those controls in the authorized task/workspace context; a GitHub edit cannot do it.

The policy records historical `You cannot modify this task` denials for protected task IDs including P26 in some contexts, while later repository evidence records successful P26 modification from another authorized context. The compliant workaround for a denied task is the authorized owning account/workspace task interface or platform support, never permission bypass or duplicate scheduling. I did not probe, create, reactivate, or modify any other schedule.

## 2. Fresh bounded literature/status check

A bounded current search during this run (19 September 2026 UTC / 20 September local) again recovered:

- Achlioptas--Friedgut, *A Sharp Threshold for k-Colorability*, Random Structures & Algorithms 14 (1999), first published 7 January 1999, DOI `10.1002/(SICI)1098-2418(1999010)14:1<63::AID-RSA3>3.0.CO;2-7`. Its abstract explicitly gives an `n`-dependent location `d_k(n)` for fixed `k>=3`; that is not constant-location convergence.
- Ayre--Coja-Oghlan--Greenhill, *Lower bounds on the chromatic number of random graphs*, arXiv:1812.09691 / Combinatorica 42 (2022), the interpolation/variational upper-bound engine used by the current certified endpoint: `https://arxiv.org/abs/1812.09691`.
- Mizgerd--Perkins--Wang, *On the Chromatic Number of Random Triangle-Free Graphs*, Random Structures & Algorithms 68 (2026), first published 6 June 2026, DOI `10.1002/rsa.70081`. It proves scaling windows for a **triangle-free conditioned model** at a different density scale, not the ordinary `G(n,d/n)` fixed-`q=3` source problem.
- Current searches for ordinary `G(n,d/n)` / fixed-3-colourability threshold-location convergence did not recover a 2025--2026 source-matching resolution.

This is bounded negative evidence only, not a worldwide openness or novelty certificate. F0095 remains **OPEN**.

## 3. Frozen source-relevant metric: first no-movement run after a moving checkpoint

The fixed metric remains

`W_3 := U_3 - L_3`, with `L_3=4.03`.

Run 25 certified

`U_3 <= 4.6865076260769`, hence `W_3 <= 0.6565076260769`.

This run does not change either endpoint:

`W_3: 0.6565076260769 -> 0.6565076260769`.

This is the **first** unchanged run after the run-25 movement, so Section I's three-run stuck trigger does not fire. The choice not to chase another `10^-13` decimal is deliberate under the owner's 90-percent rule: the run attacks the geometry and intensity structure of the variational optimizer instead.

## 4. Carry-in cavity representation from run 25

Use the run-25 coordinate

` t=(1-x)/3 in [0,1/3] `.

For a finite multiset `N={t_i}`, set

`A(N)=prod_i(1-t_i)`, `B(N)=prod_i(1-2t_i)`, `C(N)=prod_i(1-3t_i)`,

and

`S(N)=3A(N)-3B(N)+C(N)`.

The exact outgoing cavity message is

`R(N)=[A(N)-2B(N)+C(N)]/[3A(N)-3B(N)+C(N)]`.

Run 25 proved `0<=R(N)<=1/3` and the exact insertion identity

`F(N+delta_u)-F(N)=log(1-3u R(N))`, where `F=log S`.

For a probability law `a` on `[0,1/3]`, let `N_a` be a Poisson point process of intensity `d a` and define

`C_d(a)=Law(R(N_a))`.

The exact contact residual is the logarithmic-transform discrepancy between `C_d(a)` and `a`; therefore any stationary law whose support has an accumulation point must satisfy the distributional fixed-point equation

`a=C_d(a)`.

The present run studies this fixed-point equation and then feeds the resulting monotonicity back into the finite active-shape quotient.

## 5. B1 — the exactly-two-input rule is a multiplicative semigroup

### Lemma 5.1 — exact two-message product rule

For `s,t in [0,1/3]`,

`R({s,t})=2st`.

### Proof

For two messages,

`A=(1-s)(1-t)`, `B=(1-2s)(1-2t)`, `C=(1-3s)(1-3t)`.

Direct expansion gives

`A-2B+C=2st`,

while

`3A-3B+C=1`.

Substitution into the definition of `R` proves the claim. The exact polynomial identities are independently self-checked by the artifact in Section 10. QED.

In the rescaled coordinate `y=2t in [0,2/3]`, Lemma 5.1 is simply

`y_out=y_1 y_2`.

Thus the exactly-two-positive-input sector is a literal multiplicative semigroup rather than merely an approximate small-message rule.

### Theorem 5.2 — no nontrivial cavity fixed point has finite support

Let `a` be a nontrivial probability law on `[0,1/3]` satisfying `a=C_d(a)`. Then `supp(a)` is infinite and has `0` as an accumulation point.

### Proof

Choose any `s in supp(a) cap (0,1/3]`. I first show that

`2s^2 in supp(a)`.

Let `V` be any neighborhood of `2s^2`. By continuity of `(u,v) -> 2uv`, there is a neighborhood `U` of `s`, separated from zero, such that `2uv in V` whenever `u,v in U`. Since `s` is in the support, `a(U)>0`.

Let `q=a((0,1/3])`. In the Poisson cloud, the event

- exactly two positive points fall in `U`,
- no positive point falls outside `U`,
- any number of zero points is allowed,

has probability

`exp(-dq) (d a(U))^2/2 > 0`.

Zero messages do not change `A,B,C`, and on this event Lemma 5.1 places the output in `V`. Hence `C_d(a)(V)>0`. Since `a=C_d(a)`, `a(V)>0`. Because `V` was arbitrary, `2s^2` is in `supp(a)`.

Iterate

`s_{n+1}=2s_n^2`, `s_0=s`.

Because `0<s_n<=1/3`,

`s_{n+1}/s_n=2s_n<=2/3<1`.

Therefore the `s_n` are distinct positive support points and `s_n -> 0`. Thus the support is infinite and accumulates at zero. QED.

This is a strict strengthening of the previous fixed-point dichotomy: the nontrivial fixed-point branch can no longer hide inside a finite support.

### Corollary 5.3 — zero is also an atom

With `q=a((0,1/3])>0`, an output is zero whenever the Poisson cloud contains at most one positive message. Therefore fixed-point equality gives

`a({0}) >= exp(-dq)(1+dq) > 0`.

The earlier exact analysis sharpened this to equality and, at the current degree, excluded the small nonzero `q` branch. The new point is geometric: zero is simultaneously an atom **and** an accumulation point of positive support.

## 6. B13 — cavity monotonicity and strict log-submodularity

The multiplicative sector suggests that the full cavity map may preserve an order. It does.

### Lemma 6.1 — `R` is coordinatewise nondecreasing

For every finite background cloud and every inserted message `u in [0,1/3]`,

`R(N+delta_u) >= R(N)`.

If `u>0` and the background contains at least one positive message, the inequality is strict.

### Proof

Write the background products as `A,B,C`, and abbreviate

`N_0=A-2B+C`, `D_0=3A-3B+C`.

After inserting `u`,

`A'=(1-u)A`, `B'=(1-2u)B`, `C'=(1-3u)C`.

Exact cross-multiplication gives

`N' D_0 - N_0 D' = u(3AB-4AC+BC)`.

For every single message `t in [0,1/3]`,

`(1-3t)/(1-t) <= ((1-2t)/(1-t))^2`,

because the difference after clearing denominators is `t^2>=0`. Hence, with

`r=B/A`, `v=C/A`,

we have `0<=v<=r^2<=1`. Since the coefficient of `v` in `3r-4v+rv` is `r-4<0`,

`3r-4v+rv >= 3r-4r^2+r^3 = r(r-1)(r-3) >= 0`.

Thus `3AB-4AC+BC>=0`, proving monotonicity because the denominators are positive.

If the background has a positive message, then `0<r<1`; consequently `r(r-1)(r-3)>0`. With `u>0`, the cross-difference is strictly positive. QED.

### Theorem 6.2 — `F=log S` is submodular on finite message multisets

For every finite multiset `N` and `s,t in [0,1/3]`,

`Delta_s Delta_t F(N) <= 0`,

where `Delta_t F(N)=F(N+delta_t)-F(N)`.

If `s,t>0` and `N` contains a positive message, the inequality is strict.

### Proof

By the run-25 insertion identity,

`Delta_t F(N)=log(1-3t R(N))`.

For fixed `t>0`, the right side is strictly decreasing in `R(N)`. Lemma 6.1 says insertion of `s` can only increase `R`. Therefore

`Delta_t F(N+delta_s) <= Delta_t F(N)`,

which is exactly the submodularity inequality. The strict case follows from the strict part of Lemma 6.1. QED.

This is the useful monovariant of the run: as the cloud grows, every further vertex-log insertion has diminishing return.

## 7. Strict Poisson concavity for every finite active shape

Let `b` be a finite-support probability law on `(0,1/3]` and `N_lambda` a Poisson point process of intensity `lambda b`. Define the active vertex term

`V_b(lambda)=E F(N_lambda)`.

This is the same vertex term appearing in the run-24 neutral-atom quotient after pushing the original `x<1` active law through `t=(1-x)/3`.

### Theorem 7.1 — `V_b` is strictly concave on `(0,infinity)`

For every nontrivial finite active shape `b`,

`V_b'(lambda)<=0`,

`V_b''(lambda)<0` for every `lambda>0`.

### Proof

Because `b` has finite support, `|F(N)|=O(1+|N|)`: indeed, if `r_*<1` is the largest ratio `(1-2t)/(1-t)` over the positive support, then for any nonempty cloud

`3(1-r_*) A <= S(N) <= 4A`,

where `A=prod(1-t_i)`. Thus the Poisson series for `V_b` and its first two derivatives converge absolutely and may be differentiated term by term.

The standard add-one Poisson identities then give, for iid `X,Y~b`, independent of `N_lambda`,

`V_b'(lambda)=E[Delta_X F(N_lambda)]`,

`V_b''(lambda)=E[Delta_Y Delta_X F(N_lambda)]`.

The first integrand is at most zero because `R>=0` in the insertion formula. The second is at most zero by Theorem 6.2.

For strictness, with positive probability `X>0`, `Y>0`, and the background Poisson cloud contains at least one positive mark. On that event Lemma 6.1 is strict, hence `Delta_Y Delta_XF<0`. Therefore the expectation is strictly negative for every `lambda>0`. QED.

### Consequence 7.2 — the secant slope is strictly decreasing

Since `V_b(0)=0` and `V_b` is strictly concave,

`lambda -> V_b(lambda)/lambda`

is strictly decreasing on `(0,infinity)`.

This is global information that was absent from the previous finite-support optimization: it does not depend on a chosen atom count or a local Hessian.

## 8. A unique feasibility crossing for the neutral-atom quotient

Recall run 24's exact neutral decomposition. In the original `x` coordinate, write

`a=m b_x +(1-m) delta_1`, `lambda=dm`.

After transforming the active shape to `t=(1-x)/3`, define

`Q_b = E log(1-3ST)`, with iid `S,T~b`.

Then

`Sigma_d(a)=V_b(lambda) - [lambda^2/(2d)] Q_b`.

For `lambda>0`, the active shape has `V_b(lambda)<0` and `Q_b<0`, so the equality degree is

`D_b(lambda)=lambda^2 Q_b/[2V_b(lambda)] > 0`.

The admissibility of the neutral mass at equality is exactly `D_b(lambda)>=lambda`.

### Theorem 8.1 — `D_b(lambda)/lambda` decreases strictly from infinity to a value below one

For every finite active shape `b` on `(0,1/3]`,

`G_b(lambda):=D_b(lambda)/lambda = Q_b/[2(V_b(lambda)/lambda)]`

is strictly decreasing. Moreover,

`lim_{lambda downarrow 0} G_b(lambda)=infinity`,

and

`lim_{lambda to infinity} G_b(lambda)=Q_b/(2a_b) in (0,1)`,

where

`a_b=E log(1-T)<0`.

Hence there exists a unique `lambda_x(b)>0` such that

`D_b(lambda_x)=lambda_x`,

and

`D_b(lambda)>=lambda  iff  0<lambda<=lambda_x(b)`.

### Proof

By Consequence 7.2, `h(lambda)=V_b(lambda)/lambda<0` is strictly decreasing. Since `Q_b<0` is constant, `Q_b/(2h)` is therefore strictly decreasing.

For the small-intensity endpoint, `F(N)=0` for zero, one, or two active messages. With three positive messages the run-24 identity gives `S<1`, hence `F<0`. The Poisson expansion therefore starts at order three:

`V_b(lambda)=-c_b lambda^3+O(lambda^4)`, with `c_b>0`.

Thus `h(lambda)->0-` and `G_b(lambda)->infinity`.

For large intensity, the finite-support bound from the proof of Theorem 7.1 yields

`F(N)=sum_{t in N} log(1-t)+O(1)`

uniformly for nonempty clouds. Poisson averaging gives

`V_b(lambda)=lambda a_b+O(1)`,

so `h(lambda)->a_b`.

It remains to locate the limiting ratio. For `s,t in (0,1/3]`,

`1-3st > (1-s)(1-t)`,

because

`[1-3st] - [(1-s)(1-t)] = s+t-4st = s(1-2t)+t(1-2s) > 0`.

Taking logs and expectations gives

`Q_b > 2a_b`.

Both sides are negative, hence

`0 < Q_b/(2a_b) < 1`.

Strict monotonicity plus the two endpoint limits gives a unique crossing with level one and the stated admissible interval. QED.

### Why Theorem 8.1 matters

For a fixed active shape, the neutral-boundary optimization no longer has an arbitrary feasibility set in `lambda`: it is a single initial interval with exactly one point where the neutral atom disappears. Any future global optimization can therefore separate **shape** from **one scalar ordered intensity coordinate**. This is more useful than another unrestricted four- or five-atom decimal search.

## 9. B29 — the opposite endpoint is non-atomic but unavoidable

Theorem 5.2 forces accumulation at zero. The other boundary has the complementary geometry.

### Lemma 9.1 — no finite cloud reaches `1/3`

For every finite cloud,

`R(N)<1/3`.

### Proof

Let `N_0=A-2B+C`, `D_0=3A-3B+C`. Then

`D_0-3N_0=3B-2C`.

Every factor of `B` is at least `1/3`, so `B>0`, while `0<=C<=B`. Therefore

`3B-2C >= B>0`.

Hence `3N_0<D_0`, i.e. `R(N)<1/3`. QED.

Because a Poisson cloud is finite almost surely, any fixed point satisfies

`a({1/3})=0`.

### Theorem 9.2 — every nontrivial fixed point accumulates at `1/3`

Let `a=C_d(a)` be nontrivial. Then `1/3` belongs to the closure of `supp(a)`, although it has zero mass.

### Proof

Because `a((0,1/3])>0`, choose `tau>0` with

`p:=a([tau,1/3])>0`.

Let `q=a((0,1/3])`. Consider the positive-probability Poisson event consisting of exactly `n` marks in `[tau,1/3]` and no other positive marks. Zero marks may be arbitrary and do not affect `R`.

By coordinatewise monotonicity, the output on this event is at least the value for `n` copies of `tau`:

`r_n(tau)=[(1-tau)^n-2(1-2tau)^n+(1-3tau)^n]/[3(1-tau)^n-3(1-2tau)^n+(1-3tau)^n]`.

Lemma 9.1 puts the same output strictly below `1/3`. Hence

`a([r_n(tau),1/3)) >= exp(-dq) (dp)^n/n! >0`.

Finally,

`r_n(tau) -> 1/3`,

because `(1-2tau)^n/(1-tau)^n ->0` and `(1-3tau)^n/(1-tau)^n ->0`. Thus every neighborhood below `1/3` has positive `a`-mass, proving endpoint accumulation. QED.

Together, Theorems 5.2 and 9.2 give a rigid two-boundary picture for every nontrivial cavity fixed point:

- `0` is an atom and an accumulation point of positive support;
- `1/3` is not an atom but is an accumulation point of support;
- the support is necessarily infinite.

### Theorem 9.3 — quantitative endpoint-collar mass at the current degree

There is also a source-useful quantitative version. The older equivalent cavity coordinate is

`Lambda=t/(1-t) in [0,1/2]`.

Indeed, if the present cavity output is `R`, then

`Lambda_out=R/(1-R)=(A-2B+C)/(2A-B)`,

which is exactly the earlier HARD7-06 cavity recursion. The previously proved fixed-point first-moment inequality therefore applies:

`E Lambda > 1/d^2`

for every nontrivial fixed point.

Since

`t=Lambda/(1+Lambda) >= (2/3)Lambda`,

we have

`E t > 2/(3d^2)`.

Set

`tau_d=1/(3d^2)`

and `p_d=a([tau_d,1/3])`. Since `t<=tau_d` below this set and `t<=1/3` everywhere,

`E t <= tau_d + p_d/3`.

Comparing with the strict lower bound gives

`p_d > 1/d^2`.

Therefore Theorem 9.2 sharpens to

`a([r_n(tau_d),1/3)) > exp(-d)/(d^n n!)`,  for every `n>=2`.

At the current exact certified degree

`d=46865076260769/10^13`,

our exact self-check gives

`tau_d = 0.01517679574085278177...`,

`r_200(tau_d)=0.318163347260442264... > 0.318`,

`r_400(tau_d)=0.332664571747247895... > 0.33`,

`r_800(tau_d)=0.333331993731168674... > 0.333`.

The lower probabilities are tiny, but the theorem is not a numerical-fit statement: it proves unavoidable fixed-point mass arbitrarily close to the endpoint with an explicit analytic lower bound. This is directly relevant to any rigorous quadrature/discretization theorem for the continuum branch.

## 10. Exact self-check and idea-before-code ordering

The mathematical route was checkpointed **before** code at

`artifacts/hard7_2026-09-18/HARD7-06/2026-09-19T21-45-00Z__f0095_boundary_semigroup_idea.md`

creation commit

`411e1fb3006bbdd9ffdca4c10f04ac08bcd8367e`.

Only afterward I wrote the exact finite-core self-check

`artifacts/hard7_2026-09-18/HARD7-06/2026-09-19T21-45-00Z__f0095_boundary_semigroup_exact.py`

creation commit

`94b187eb95e7493d4b998834a9d37c886b4fe8d9`,

and archived its reproduced output at

`artifacts/hard7_2026-09-18/HARD7-06/2026-09-19T21-45-00Z__f0095_boundary_semigroup_exact.out`

commit

`29fffba887f85cf60a993fcc40365ad7cde59d62`.

The script uses only standard-library `Fraction` arithmetic plus a tiny exact polynomial dictionary. It certifies the two-input polynomial identity, the insertion cross-factor identity, the strict endpoint identity, and the current-degree rational comparisons. The archived output ends

`ALL_EXACT_CHECKS_PASS = True`.

This is explicitly a **self-check**, not an independent audit. The analytic fixed-point support and Poisson-concavity theorems are proved on the page above; the checker does not substitute for them.

## 11. What moved mathematically, and what did not

The source metric did not move. The structural state did:

- possible nontrivial **finite-support cavity fixed points:** `not previously excluded -> impossible`;
- fixed-point lower-end geometry: `zero atom -> zero atom plus positive-support accumulation`;
- upper-end geometry: `unclassified -> no endpoint atom, but unavoidable support accumulation with explicit collar mass`;
- fixed active-shape intensity feasibility: `generic scalar quotient -> unique ordered crossing D_b(lambda)=lambda`;
- active Poisson vertex geometry: `no global curvature sign -> strict concavity V_b''<0`.

None of these closes F0095, proves the true threshold constant, proves that the ACG variational minimizer is a continuum fixed point, or proves global uniqueness of an ACG optimizer. A finite-support minimizer remains possible, but if it is nontrivial it cannot simultaneously be an exact cavity fixed point; its KKT contact set must remain discrete.

## 12. Next route

The new structure points to a more meaningful next target than atom-count inflation.

1. Use strict Poisson concavity plus the unique intensity crossing to derive a **one-sided quadrature/compression theorem**: approximate a continuum fixed-point law by a finite active law while preserving the sign of the contact inequality and controlling `D_b`.
2. Exploit the two boundary tails explicitly rather than truncating them silently. Any certified discretization must include a lower-end multiplicative cell and an upper-end collar approaching `1/3`.
3. If the continuum branch can be compressed with a one-sided error, feed the resulting shape into the existing exact ACG certificate machinery and ask for a source-metric movement. If not, the obstruction itself should be recorded as the next theorem target.

A different Section-B triple must be used next time.

## 13. Structured ledger delta

```yaml
ledger_delta:
  worker: HARD7-06
  lane: HARD_OUTSIDE
  target: F0095
  source_status: OPEN
  ownership: HARD7-06_EXCLUSIVE_UNCHANGED
  fixed_metric: W_3=U_3-L_3
  lower_endpoint: 4.03
  upper_endpoint_before: 4.6865076260769
  upper_endpoint_after: 4.6865076260769
  metric_before: 0.6565076260769
  metric_after: 0.6565076260769
  movement: NO_MOVEMENT_FIRST_AFTER_MOVING_CHECKPOINT
  status: PARTIAL
  methods:
    - B1_CHANGE_CATEGORY
    - B13_FIND_WHAT_ONLY_INCREASES
    - B29_ADD_POINTS_AT_INFINITY
  new_results:
    - nontrivial_cavity_fixed_point_has_infinite_support_and_accumulates_at_zero
    - cavity_fixed_point_has_no_atom_at_one_third_but_support_accumulates_there
    - explicit_endpoint_collar_mass_lower_bound
    - finite_active_vertex_term_strictly_concave_in_poisson_intensity
    - neutral_quotient_feasibility_ratio_strictly_decreasing_with_unique_crossing
  source_closed: false
  novelty: UNVERIFIED
  independent_audits: 0
  idea_commit: 411e1fb3006bbdd9ffdca4c10f04ac08bcd8367e
  exact_checker_commit: 94b187eb95e7493d4b998834a9d37c886b4fe8d9
  exact_output_commit: 29fffba887f85cf60a993fcc40365ad7cde59d62
  exact_output_terminal: ALL_EXACT_CHECKS_PASS=True
  next_route: one_sided_cavity_quadrature_or_compression_using_concavity_and_two_boundary_tails
```

No email, Drive, public posting, shared-root ledger mutation, peer-track edit, permission bypass, or scheduler mutation was performed.