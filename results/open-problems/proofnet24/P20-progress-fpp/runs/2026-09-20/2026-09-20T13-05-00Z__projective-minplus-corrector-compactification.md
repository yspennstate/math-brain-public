Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — no authenticated applied reasoning-effort receipt is exposed, so I do not claim a specific effort setting or GPT-6 maximum.**

# P20 T10 — projective min-plus compactification and a finite-net Bellman certificate

Date: 2026-09-20 UTC.  
Repository / branch: private `yspennstate/math-open-problems` / `master`.  
Controlling policy: `operations/PROGRESS20_2026-09-20.md`.  
Canonical parent: `operations/claims/PROB10-10.md`.  
Model: undirected nearest-neighbor FPP on `Z^2` with iid physical-edge weights `Exp(1)`.  
Status: **PARTIAL / OPEN** for strict convexity. The theorem arguments newly proved below are **CANDIDATE_PROVED pending later independent review**. No completed certification or novelty claim is made.

## 1. Source, continuity, ownership, and source-level before/after

The exact source remains Auffinger--Damron--Hanson, *50 years of first passage percolation*, arXiv:1511.03262, Question 4 in the limit-shape discussion: prove strict convexity for continuous passage-time laws. The canonical repository specialization is iid `Exp(1)` undirected nearest-neighbor FPP on `Z^2`.

Write `mu` for the deterministic time-constant norm and

`Delta_12 := 2 mu(e1)-mu(1,1) >= 0`.

The frozen source-facing metric is the largest rigorously proved `c>=0` with `Delta_12>=c`.

- **before:** `c_*=0`;
- **after:** `c_*=0`.

So this run does **not** prove the axis/diagonal strict triangle inequality and does not close ADH strict convexity.

The demonstrated mechanism gain is separate: the asynchronous diagonal-band state can be controlled directly in its continuous projective geometry. The min-plus block operator is nonexpansive in oscillation, resets every finite incoming profile to a random bounded-span set in one block, and admits the coercive corrector `h_kappa(y)=kappa span(y)`. This reduces the unbounded Bellman verification to a compact set. A deterministic `delta`-net of that compact set then has an explicit interpolation loss `(1+3 kappa) delta`. Unlike the newly canonical conservative-rounding architecture, this route does **not** discretize or delete the evolving profile. It therefore gives a complementary unrounded certificate mechanism.

## 2. Essential state consumed and collision correction during this run

I consumed only the essential current state:

1. `operations/PROGRESS20_2026-09-20.md` and the LIVE20 pairing `P04 <-> P20` on T10;
2. `operations/claims/PROB10-10.md` and root `POSTED.md` exclusions;
3. P20's preceding report `2026-09-20T11-15-00Z__jacquet-backtrack-residual-collapse.md`;
4. P04's current T10 width-7 undirected moving-slab report at commit `ab1c4bd3b662dfe712acae1193e41d2f102dddb1`;
5. the canonical same-source reset `runs/prob10_2026-09-20/PROB10-10/20260920T1018Z__hard-cone-reset-first-moment-barrier.md`;
6. the newest canonical asynchronous-carry development created while this run was in progress, in particular commit `96f76b3399ffefe3178f3be0531a22e8e09dcfab` and its screen output commit `c6d5dc13d7ff79b8ca555e11c308f646eaad8c06`;
7. R08's preserved failure history and axis-bound history.

This collision matters. The canonical owner has now independently proved the **conservative upward-projection / finite-state Bellman compiler** for the asynchronous antidiagonal carry. I therefore do **not** claim that projection theorem as a new P20 result. The P20 result below is the distinct continuous-state/projective compactification and finite-net interpolation theorem. It can be used with the same block decomposition while avoiding a projected Markov chain and its full transition kernel.

The canonical current rigorous auxiliary axis lower certificate is

`mu(e1) >= b := 3002823/10000000 = 0.3002823`,

so the direct diagonal target is

`mu(1,1) < 2b = 3002823/5000000 = 0.6005646`.              (2.1)

The bounded current-literature check still found no unconditional theorem closing ordinary iid Exp(1), nearest-neighbor, undirected `Z^2` strict convexity. Jacquet's pattern theorem remains applicable to Exp(1) and was used in the preceding P20 run, but it does not itself turn common local calibration into a same-quadrant triangle defect.

## 3. Binding failures retained

Nothing below resets the old failures.

1. Shared bypasses defeat naive multiplication of local surgery gains.
2. Positive-probability finite cylinder events can have exact finite triangle equality, so pointwise finite strict saving is false.
3. Fixed-corner exact blocks did not meet the diagonal threshold in the retired R08 route.
4. Directed integrable models and unrestricted-versus-directed comparisons do not establish the required undirected same-quadrant defect.
5. The preceding P20 Jacquet attack proves linearly many true-geodesic U-backtracks, but under flatness their diagonal-target residual can collapse on a positive-density subfamily. That is a co-calibration rigidity statement, not yet a contradiction.
6. The canonical owner has also proved that the current first-moment weighted-SAW/Chernoff architecture cannot reach the diagonal at the retained scale because the monotone E/N path family already defeats its union bound.

The present attack is therefore genuinely different from both local residual multiplication and all-path first-moment counting: it works with the exact asynchronous min-plus boundary operator and a deterministic Bellman corrector.

## 4. General finite-block min-plus setup

Fix one finite connected block graph. Let `I={1,...,m}` be its input boundary and `O={1,...,r}` its output boundary. For a realized block environment `omega`, let

`d_omega(i,j)`

be the shortest passage time inside the block from input `i` to output `j`. For a finite input arrival vector `y in R^m`, define

`F_omega(y)_j := min_i { y_i + d_omega(i,j) }`.             (4.1)

Normalize by

`g_omega(y) := min_j F_omega(y)_j`,

`Phi_omega(y) := F_omega(y)-g_omega(y) 1`.                 (4.2)

Thus `min Phi_omega(y)=0`. Write

`span(v):=max_i v_i-min_i v_i`,

and `osc(v)` for the same seminorm when differences may have either sign.

Translation equivariance is exact:

`F_omega(y+c1)=F_omega(y)+c1`,
`g_omega(y+c1)=g_omega(y)+c`,
`Phi_omega(y+c1)=Phi_omega(y)`.                             (4.3)

The statements below are deterministic for each fixed block environment before expectations are taken.

## 5. Projective nonexpansiveness

### P20-FPP-MINPLUS-PROJECTIVE-NONEXPANSIVENESS-35 — CANDIDATE_PROVED

For any finite input vectors `y,z`, put

`a=min_i(y_i-z_i)`, `b=max_i(y_i-z_i)`.

Then for every output coordinate `j`,

`a <= F_omega(y)_j-F_omega(z)_j <= b`.                     (5.1)

Consequently

`osc(F_omega(y)-F_omega(z)) <= osc(y-z)`,                  (5.2)

and

`osc(Phi_omega(y)-Phi_omega(z)) <= osc(y-z)`.              (5.3)

Moreover

`|g_omega(y)-g_omega(z)| <= ||y-z||_infinity`.             (5.4)

If `min y=min z=0` and `||y-z||_infinity<=epsilon`, then

`||Phi_omega(y)-Phi_omega(z)||_infinity <= 2 epsilon`.      (5.5)

#### Proof

From `y_i>=z_i+a` for every `i`,

`y_i+d(i,j) >= z_i+d(i,j)+a`.

Taking minima in `i` gives the lower inequality in (5.1). The upper inequality follows from `y_i<=z_i+b`. Equation (5.2) follows because every coordinate of `F(y)-F(z)` lies in `[a,b]`.

Subtracting a constant vector does not change oscillation, so

`osc(Phi(y)-Phi(z))`
`=osc(F(y)-F(z)-(g(y)-g(z))1)`
`=osc(F(y)-F(z))`,

which proves (5.3).

The map `g=min_j min_i(y_i+d(i,j))` is a minimum of functions that are each 1-Lipschitz in sup norm, giving (5.4). For normalized `y,z`, `osc(y-z)<=2||y-z||_infinity`; each coordinate of `Phi(y)-Phi(z)` differs from another by at most this oscillation and both output vectors have minimum zero, which gives (5.5). QED.

### Interpretation

The correct state space is the quotient by additive constants. The exact block operator is nonexpansive in the Hilbert/oscillation seminorm on that quotient. This is the structural reason asynchronous labels can be carried without synchronization: profile errors do not amplify projectively from block to block.

## 6. One-block span reset independent of the incoming profile

For outputs `j,k in O`, let `d_omega(j,k)` denote the shortest within-block distance between the two output vertices, and define

`D_omega := max_{j,k in O} d_omega(j,k)`.                  (6.1)

Also define

`H_omega := max_{i in I} min_{j in O} d_omega(i,j)`.       (6.2)

### P20-FPP-MINPLUS-OUTPUT-SPAN-RESET-36 — CANDIDATE_PROVED

For every finite normalized input profile `y` with `min y=0`,

`span(Phi_omega(y)) <= D_omega`,                           (6.3)

and

`g_omega(y) <= H_omega`.                                  (6.4)

#### Proof

Fix outputs `j,k`, and choose an input `i_*` attaining `F(y)_k`. Concatenating a shortest `i_*`-to-`k` path with a shortest `k`-to-`j` path gives

`F(y)_j <= F(y)_k+d_omega(k,j)`.

Interchanging `j,k` yields

`|F(y)_j-F(y)_k| <= d_omega(j,k) <= D_omega`.

Taking the maximum over `j,k` proves (6.3); subtracting `g` does not change span.

Choose an input `i_0` with `y_{i_0}=0`. Then

`g(y) <= min_j { y_{i_0}+d(i_0,j) }`
`      = min_j d(i_0,j) <= H_omega`,

proving (6.4). QED.

### Explicit finiteness for the diagonal bands

For the canonical rotated diagonal band of thickness `2L` and half-width `W`, every input has a fixed `2L`-edge forward zig-zag to an output with the same transverse offset. If `m=|D_W|`, then the crude deterministic-path estimate gives

`E H_omega <= 2Lm`.                                       (6.5)

Adjacent output offsets can be connected through the previous antidiagonal by a two-edge V. Chaining these V's across the output boundary uses at most `2W` edges, so

`E D_omega <= 2W`.                                        (6.6)

Sharper finite-block values can of course replace these crude universal bounds. The point is that one block sends every finite incoming profile, no matter how spread out, into a random profile whose span is controlled independently of that incoming spread.

## 7. A coercive span corrector compactifies the Bellman problem

Fix `kappa>0` and define on finite normalized profiles

`h_kappa(y):=kappa span(y)`.                               (7.1)

Define its one-block Bellman residual

`B_kappa(y)`
` := E[ g_omega(y)+h_kappa(Phi_omega(y)) ]-h_kappa(y)`
`  = E[ g_omega(y)+kappa span(Phi_omega(y)) ]`
`    -kappa span(y)`.                                      (7.2)

### P20-FPP-SPAN-CORRECTOR-COMPACTIFICATION-37 — CANDIDATE_PROVED

If `E H_omega<infinity` and `E D_omega<infinity`, then for every finite normalized profile `y`,

`B_kappa(y)`
` <= E H_omega + kappa E D_omega-kappa span(y)`.           (7.3)

Consequently, for any proposed average-cost bound `lambda`, every state with

`span(y) >= R(lambda,kappa)`
` := [E H_omega+kappa E D_omega-lambda]/kappa`             (7.4)

(alternatively any larger nonnegative `R`) automatically satisfies

`B_kappa(y)<=lambda`.                                      (7.5)

#### Proof

Insert (6.3)--(6.4) into (7.2) and take expectations. QED.

### Why this matters

The continuous boundary state space was previously unbounded. Equation (7.3) supplies a Lyapunov/Bellman drift with the correct sign at large projective span. Therefore a uniform Bellman inequality needs to be checked only on the compact normalized set

`K_R={ y in [0,R]^m : min_i y_i=0 }`.                      (7.6)

This is not a probabilistic truncation and does not discard any FPP environment. Large-span profiles are paid for analytically by the `-kappa span(y)` corrector.

## 8. Explicit finite-net interpolation error

### P20-FPP-FINITE-NET-BELLMAN-CERTIFICATE-38 — CANDIDATE_PROVED

Let `y,z` be finite normalized profiles with

`||y-z||_infinity<=epsilon`.

Then

`|B_kappa(y)-B_kappa(z)| <= (1+3kappa) epsilon`.            (8.1)

Therefore let `N_delta` be any `delta`-net of `K_R` in sup norm. If

1. the outer-span condition (7.5) holds for every `span(y)>=R`; and
2. every net point `z in N_delta` satisfies the rigorous finite-block inequality

`B_kappa(z) <= lambda-(1+3kappa)delta`,                    (8.2)

then

`B_kappa(y)<=lambda`                                       (8.3)

for **every finite normalized profile** `y`.

#### Proof

By (5.4),

`|E g(y)-E g(z)|<=epsilon`.                                (8.4)

For any vectors `u,v`,

`|span(u)-span(v)|<=osc(u-v)`.                             (8.5)

Using (5.3) and `osc(y-z)<=2epsilon`,

`|span(Phi(y))-span(Phi(z))|<=2epsilon`.                   (8.6)

Since `min y=min z=0`,

`|span(y)-span(z)|=|max y-max z|<=epsilon`.                (8.7)

Combining (8.4), `kappa` times (8.6), and `kappa` times (8.7) proves (8.1). For a state inside `K_R`, choose a net point within `delta` and use (8.1)--(8.2); states outside `K_R` are covered by (7.5). QED.

### Comparison with the canonical projected finite-state route

The canonical owner now has a different valid discretization: round the actual state upward to a finite alphabet, prove path dominance, and solve a finite-state average-cost Bellman inequality. The theorem above instead leaves the stochastic process **unrounded** and uses a net only to verify a Lipschitz Bellman inequality. This removes the need to compute the entire projected transition kernel `p(y,y')`: only a scalar expected Bellman expression is required at each verification point.

## 9. Scalar first/last-output evaluation

At a fixed normalized input profile `y`, let

`t_first(y,omega):=min_j F_omega(y)_j=g_omega(y)`,

`t_last(y,omega):=max_j F_omega(y)_j`.

Then exactly

`g_omega(y)+kappa span(Phi_omega(y))`
` = (1-kappa)t_first(y,omega)+kappa t_last(y,omega)`.        (9.1)

For `0<kappa<=1`, both coefficients are nonnegative. Thus a rigorous upper enclosure of the two scalar expectations

`E t_first(y,omega)`, `E t_last(y,omega)`                  (9.2)

at each net state is enough to verify (8.2). One does **not** need a rigorous enclosure of every projected-state transition probability.

For Exp(1) edges there is a natural finite continuous-time evaluation: source boundary vertices become active at their deterministic offsets `y_i`, and between scheduled activations the Richardson/Dijkstra exploration evolves by exponential races. If an active edge survives to the next scheduled source activation, memorylessness leaves its residual clock Exp(1). A rigorous implementation can therefore recurse on finite infection states plus the index of the next source activation, with interval/rational outward rounding. This is an implementation target, not claimed completed in this report.

The combination (7.3), (8.1), and (9.1) is the main new variational mechanism of this run.

## 10. Source-facing compiler with controlled error

The canonical owner has already proved the exact asynchronous antidiagonal carry and finite-to-infinite implication. I consume that compiler rather than duplicate ownership.

There is one small initialization point for the unrounded span corrector: the source boundary state has one zero coordinate and `+infinity` elsewhere, so `h_kappa` is not finite there. Handle the first band separately. After one connected finite block, every output arrival label is finite and (6.3) gives

`span(Y_1)<=D_{omega_0}`.                                  (10.1)

For blocks `j>=1`, if (8.3) holds then conditioning on the past gives

`E[g_j+h_kappa(Y_{j+1})-h_kappa(Y_j) | F_j] <= lambda`.    (10.2)

Telescoping through `N` bands yields

`E M_N`
` <= E g_0 +(N-1)lambda+kappa E D_omega`,                 (10.3)

because `h_kappa>=0`. The canonical fresh terminal staircase correction has expected cost at most `W`, so

`E T(0,(NL,NL))/(NL)`
` <= [(N-1)lambda+E g_0+kappa E D_omega+W]/(NL).           (10.4)

Letting `N->infinity`,

`boxed: mu(1,1) <= lambda/L`.                              (10.5)

Together with the retained exact axis lower bound `b`,

`boxed: Delta_12 >= 2b-lambda/L`
`                   =0.6005646-lambda/L`.                 (10.6)

Thus a finite-net certificate with

`lambda/L < 0.6005646`                                    (10.7)

would move the source metric `c_*` strictly positive. The finite-`N` error is fully explicit in (10.4); there is no per-block synchronization loss.

## 11. Essential executed sanity artifact and quantitative screen

During this run I executed and archived

`proofnet24/P20-progress-fpp/artifacts/2026-09-20/2026-09-20T12-25-00Z__rounded-minplus-bellman-check.py`

at creation commit

`5c973a682611ab375434e82e2b15f7d787545607`.

Its exact-rational finite-graph part checks:

- min-plus translation equivariance;
- inequalities (5.1)--(5.5);
- the output-span reset (6.3);
- the `H` bound (6.4);
- one-sided upward-rounding semantics;
- the exact source threshold `3002823/5000000=0.6005646`.

The archived output is

`proofnet24/P20-progress-fpp/artifacts/2026-09-20/2026-09-20T12-25-00Z__rounded-minplus-bellman-check.out`

at creation commit

`df2117a5ba7e16cb296b9444f1f4ac8c5e0c8a96`, ending its exact portion with

`EXACT_MINPLUS_CHECKS_PASS`.

The same artifact contains a fixed-seed floating screen. It is explicitly labeled

`SCREEN_ONLY_NOT_PROOF`.

It produced `0.594936602` per diagonal unit for one rounded carry at `L=7,W=49,delta=0.1,R=14`, below `0.6005646`. This is only route-selection evidence and is not used in any theorem above.

More importantly, the canonical owner independently ran the intended asynchronous carry screen and obtained, among other cases, a **projected** `L=4,W=48,eps=0.05,H=5` mean `0.595220618068`, again below the source threshold. That screen is also explicitly nonrigorous. The two screens therefore agree that there appears to be numerical room for a rigorous certificate, but **sampled numerical curvature does not move `c_*`**.

## 12. What has and has not been achieved

### Original-problem movement

`c_*: 0 -> 0`.

No strict axis/diagonal defect has been certified. No full strict-convexity claim is made.

### Demonstrated mechanism gains

1. **Projective stability:** the exact min-plus block operator is nonexpansive in oscillation, equation (5.3).
2. **One-block forgetting of huge spans:** every finite state is reset to span at most `D_omega`, equation (6.3).
3. **Coercive Bellman corrector:** `h_kappa=kappa span` analytically discharges all sufficiently large-span states, equation (7.3).
4. **Finite-net rather than finite-state verification:** a `delta`-mesh pays exactly `(1+3kappa)delta`, equation (8.1), while the actual carried process remains unrounded.
5. **Scalar expectation reduction:** for `0<kappa<=1`, verification at a mesh state needs only first/last output-arrival expectations, equation (9.1), not a full transition kernel.
6. **Controlled source compiler:** a verified `lambda/L<0.6005646` gives the explicit defect lower bound (10.6), with initialization and terminal errors `O(1/N)`.

These gains are genuinely connected to the parent problem, but the crucial numerical Bellman inequality remains uncertified.

## 13. Residual obstruction and honest failure report

The residual obstruction is now finite and explicit:

> Rigorous one-block expectation enclosures must be sharp enough on a compact projective net to prove `sup B_kappa < 0.6005646 L` for some `L,W,kappa`, after the deterministic mesh margin `(1+3kappa)delta` is paid.

The nonrigorous screens suggest room of roughly `0.004--0.008` per diagonal unit in current moderate-width regimes, but that is not a proof budget. A naive full tensor grid in `m=|D_W|` dimensions is exponentially large, so compactness alone does not make certification cheap. The missing theorem/computation is a **dimension-reduced or adaptive rigorous verification**, not an FPP dependence argument.

The preceding Jacquet co-calibration route is preserved rather than discarded: if the finite-net Bellman route ultimately fails to certify the numerical threshold, its projective nonexpansiveness may still be usable to formalize the “profiles become translates” alternative suggested by the pattern-residual collapse theorem.

## 14. Next attack

The next attack should stay on the source-facing diagonal and avoid another sampled screen.

1. Fix `0<kappa<=1` and exploit (9.1) so each verification point asks only for `E t_first` and `E t_last`.
2. Build a rigorous interval Richardson recursion for those two expectations on one modest block (`L=4` is already screened below threshold at width 48 in the canonical route).
3. Use branch-and-bound on profile boxes rather than a full tensor grid. The Lipschitz constant `(1+3kappa)` supplies a rigorous box certificate: evaluate one representative, pay the box radius, and subdivide only boxes whose upper bound remains above `lambda`.
4. Use symmetry `d -> -d`, output-span reset, and the coercive outer-span estimate before subdivision.
5. If the certified upper bound cannot beat `0.6005646 L` after two such recovery attempts, preserve the complete failure and rotate the unresolved T10 scope rather than continuing mesh refinement indefinitely.

A successful certificate would immediately yield a positive source-level `Delta_12` by (10.6). A failed certificate would still return an explicit lower bound on the Bellman supremum and identify whether the loss comes from mesh interpolation, first/last expectation bounds, or the span-only corrector.

## 15. Short cyclic-interval handoff

The displaced P20 cyclic-interval work remains preserved and is not reopened. The source-literal YES proof candidate

`P20-FOKAM-BITJOKA-CI241-SEMICIRCLE-MAJORITY-01`

and its finite sanity artifact remain on record. P26's full-proof/source-quantifier audit remains `PASS`; the last recovered certification state still lacked the second genuinely independent audit (`1/2`). No completed certification or novelty claim is implied. This run spent no research time waiting for that audit.

## 16. ledger_delta

```text
original_problem:
  metric: c_* = largest proved c with Delta_12 >= c
  before: 0
  after: 0
  source_status: OPEN / PARTIAL only

mechanism_gain:
  P20-FPP-MINPLUS-PROJECTIVE-NONEXPANSIVENESS-35 = CANDIDATE_PROVED
  P20-FPP-MINPLUS-OUTPUT-SPAN-RESET-36 = CANDIDATE_PROVED
  P20-FPP-SPAN-CORRECTOR-COMPACTIFICATION-37 = CANDIDATE_PROVED
  P20-FPP-FINITE-NET-BELLMAN-CERTIFICATE-38 = CANDIDATE_PROVED
  interpolation_loss: (1+3*kappa)*delta
  outer_state_bound: EH + kappa*ED - kappa*span(y)
  source_compiler: Delta_12 >= 0.6005646 - lambda/L
  scalar_eval: g+kappa*span(Phi)=(1-kappa)t_first+kappa*t_last

collision_handling:
  canonical owner independently proved conservative finite-state upward projection
  P20 does not duplicate or overwrite that theorem
  new P20 scope is unrounded projective compactification + finite-net verification

failure_report:
  no rigorous lambda/L below 0.6005646 yet
  all numerical carry values remain SCREEN ONLY / nonproof
  compact profile dimension is still large

residual_obstruction:
  rigorous sharp one-block first/last-arrival expectations on an adaptive compact net

next_attack:
  interval Richardson evaluator + Lipschitz branch-and-bound finite-net certificate
  use symmetry, span reset and coercive corrector before subdivision
```

END OF P20 FPP RUN REPORT
