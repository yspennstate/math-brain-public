# (I3) is the unconditioned DEP sum plus a local variance; the variance is controlled at full strength off the attractive configurations and at n^{1-1/21} everywhere

Date: 2026-08-22, lane P9_i3 (30-hour campaign).
Target: P1's open input (I3), the NEIGHBOR-CONDITIONED squared-influence sum, named in
`SINGLE_EDGE_SLACK_PIVOTAL_20260822.md` section 7(3) (canonical copy, SHA-256
`6e0b0d48a34993b3e6c201e2d8004ef6c7031815d764366138efc236a35783ba`, recomputed today and
matching P1's header).
Status: four complete results (Theorems 1, 2, 5 and the reduction Proposition 3), all
consuming only the campaign's standing hypotheses plus the referee-verified
Dembin-Elboim-Peled Corollary 1.3; one conditional route (Section 6) to the full
n^{2/3+o(1)} target with its single missing input isolated and named; the obstruction to
every measure-change approach localized to ONE set of ball configurations (Observation 8).
No counterexample: (I3) is not refuted, and the labeled heuristic of Section 7 says it is
expected to hold with n^{1/3} of room. chi = 1/3 UNMOVED. No variance bound is improved.
Falsifier: `lanes/P9_i3/p9_checks.py` (10 checks, all passing, ~5 s, BelowNormal; exact
integer enumeration of all 3^12 environments on the 3x3-vertex lattice as the primary
instrument, Dijkstra on 5x5/7x7 secondary).
Copies: lane copy `12_cognitive_architecture/brain_improvement/campaign_2026-08-22_30h/lanes/P9_i3/P9_FIRE_20260822.md`;
(filed under mesh claim clm-bc9c6ea52a); the two are byte-identical.

## 0. Scars (checked before starting; nothing below re-opens them)

From `brain.py recall "FPP refuted routes chi variance"`, P1's section 0, the referee's
fire-89 qualifier, and P7's list:

1. (L1') is the wall; the variance-ratio induction does not start; the two-sided sandwich
   core stands (fires 77-81). This note works strictly BELOW the wall, on one named input
   of the single-edge ledger. Nothing here touches (L1').
2. Doubling is wall-equivalent only in the referee's qualified form (ratio core at the
   sum-carrying blocks; near band and M-to-2 descent open). Not consumed.
3. Monotonicity has no consumer; the continuity bootstrap's base case is constant-A
   doubling. Neither is touched.
4. rho = Q^2/D retired; ledger is (L1') wall / (L2') shape / (L3) one power. (L2') kurtosis
   measurements deflated; no kurtosis here. Efron-Stein granularity not laptop-measurable;
   no such simulation here.
   around Thread B. This note does not claim one. Where full-strength (I3) needs an input,
   Section 6 and 8 show the input is Thread-B-shaped (point-conditioning at the weight
   minimum; translate-occupation under shared local conditioning) - consistent with P1.
   Mermin-Wagner tool used below is DEP's Lemma 2.1, a pure change-of-measure bound for
   deterministic shifts; no free-endpoint small-ball statement is claimed.
   displayed at its point of use; the one hypothesis NEW relative to the arc's standing set
   (an upper density bound, (H_M)) is flagged where it enters (Theorem 2 only).
8. Two scars generated INSIDE this unit and recorded so nobody retreads them: (a) the
   "max-over-ball" relaxation `T_e <= T_e^max` is the (I1') wall in disguise - it moves all
   smallness into an O(1)-additive slack window, exactly P1's 7(1); (b) a KPZ heuristic
   with the deterministic parabola applied inside the stochastic zone predicted a
   fattened-geodesic width of sqrt(n) and would have "refuted" (I3) by contradicting the
   trivial bound sum_e E[Q_e^2] <= E|gamma|; the corrected local profile is Brownian, the
   O(1)-slack tube is O(1) wide, and (I3) is consistent. Section 7 records the correction;
   Section 9 lists it as the audit that caught it.

## 1. The target, verbatim, and the verified external input

**(I3), quoted from P1 section 7(3):**

> `(I3)` for the exceptional-set route: with `E_e` a radius-1 ball of pair coordinates
> around `e`, write `W_nbr` for the OLD weights of the ball's edges other than `e` itself
> (the replacement half of those pairs never enters `z_e`, and `w_e` stays integrated).
> Given `W_nbr`, the conditional survival `q^{nbr}(t) = P(T_e > t | W_nbr)` is still
> decreasing, so the sharp monotone kernel lemma applies conditionally and, after taking
> expectations,
>
> `(E z_e)^2 + Var(E[z_e | Y_{E_e}]) <= (1/(9 alpha^2)) E[ P(e in gamma | W_nbr)^2 ].`
>
> So the new obligation is the NEIGHBOR-CONDITIONED squared influence sum
> `sum_e E[P(e in gamma | W_nbr)^2]` at `n^{2/3+o(1)}` - a two-replica statement (two
> environments sharing only the ball around `e` both route through `e`) that is strictly
> more local than block chaos. Open; named here so it stops being assumed.

The referee (P3_VERDICTS, item P1.H) confirmed the display as a correct conditional
application of the 1/9 lemma. This note takes the display as given and works on the sum.

**DEP Corollary 1.3 at beta = 2, as verified verbatim by P3 against arXiv 2307.01162v2:**
under assumption (1.4) there (law supported on `[a,b] subset (0,infinity)`, absolutely
continuous, density `>= alpha` a.e.),

`sum_e P(e in gamma(0,v))^2 <= C ||v||^{2/(d+1)} (log ||v||)^d.`      (DEP)

(From today's reading of the paper: its Theorem 1.2 is the level-set count
`#{e : P(e in gamma) >= eps} <= C eps^{-2d/(d-1)} (log||v||)^{d(d+1)/(d-1)}`, and the
beta = 2 corollary is that count summed dyadically against `sum_e p_e = E|gamma| <= Cn`.)

**Standing hypotheses** (P1 section 3, identical to DEP (1.4) plus the campaign's
`d >= 2`, target `d = 2`): iid edge weights `t_e` with density `rho` on `[a,b]`,
`0 < a < b < infinity`, `rho >= alpha > 0` a.e.; endpoints `0, v`, `|v| = n`;
`X = T(0,v)`; a.s.-unique geodesic `gamma`. NOTE: no upper bound on `rho` is in the
standing set; where one is used it is displayed as (H_M): `rho <= M` a.e.

**Notation.** `N(e) := {f != e : f shares a vertex with e}`, `K := |N(e)| = 2(2d-1)`
(`K = 6` in `d = 2`); `W_e := (t_f)_{f in N(e)}` is P1's `W_nbr` for the line-graph
radius-1 ball; `Nbar(e) := N(e) cup {e}`. Every argument below uses only that the ball is a
fixed finite edge set not containing `e`, so if P1's `E_e` is a different finite ball the
statements hold with its own `K`. `X_e := 1_{e in gamma}`, `p_e := P(e in gamma)`,
`Q_e := P(e in gamma | W_e) = q_e(W_e)`, and the target sum is

`S := sum_e E[Q_e^2]`,  with the trivial bounds `sum_e p_e^2 <= S <= sum_e p_e = E|gamma| <= (b/a) d n`

(the last by the deterministic length bound `|gamma| <= T(0,v)/a <= b|v|_1/a`). The slack
`T_e = C_e - B_e` and the pinned identity `X = min(B_e + t_e, C_e)`, `{e in gamma} =
{t_e < T_e}` are consumed from SINGLE_EDGE_GAP_COLLISION via P1 (referee-confirmed); so
is P1's Lemma B(ii): `T_e` is 1-Lipschitz in every single weight other than `t_e`.

## 2. Theorem 1: (I3) is exactly (DEP) plus a sum of local variances

**Theorem 1** (complete proof). For every edge `e`, with the ball coordinates listed in any
fixed order `f_1, ..., f_K` and `F_k := sigma(t_{f_1}, ..., t_{f_k})`,

`E[Q_e^2] = p_e^2 + sum_{k=1}^{K} || E[X_e | F_k] - E[X_e | F_{k-1}] ||_2^2 .`

Hence `S = sum_e p_e^2 + sum_e Var(Q_e)` and, under (DEP),

`(I3) at n^{2/3+o(1)}  <=>  sum_e Var(Q_e) <= n^{2/3+o(1)}`  (d = 2).

Proof. `(E[X_e | F_k])_{k=0..K}` is a Doob martingale with `F_0` trivial and `F_K =
sigma(W_e)`, so `E[X_e|F_0] = p_e`, `E[X_e|F_K] = Q_e`, and the increments are orthogonal
in `L^2`: `||Q_e||_2^2 = p_e^2 + sum_k ||Delta_k||_2^2`. QED

Reading. The delta between (I3) and the verified (DEP) is PRECISELY the local variance
`sum_e Var(Q_e)`: how much the membership probability of `e` moves when its `K` neighbor
weights are revealed, summed over the lattice. Each increment `Delta_k` is a one-coordinate
exposure, and `|Delta_k| <= P(flip_{e,f_k} | F_k, t'_{f_k})` where `flip` is the event that
resampling `t_{f_k}` flips `X_e`; by P1's Lemma B(iii) a flip forces `|T_e - t_e| <=
|t_{f_k} - t'_{f_k}|` and `f_k` onto a restricted geodesic. So `sum_e Var(Q_e)` is a sum of
`K` conditional near-tie probabilities squared - the object P7's Thread B lane owns, at
single-coordinate granularity. This is the interface, not a theorem: Theorem 1 does not
bound the variance, it isolates it. Falsifier A2 checks the identity exactly (rational
arithmetic, all twelve edges of the 3x3 lattice, all 3^12 environments).

## 3. Proposition 3: (I3) reduces to a ball-robust influence bound

Write `s_e := esssup_w q_e(w)` for the ROBUST influence (the adversary fixes the ball).
Since `p_e = E[q_e(W_e)] <= s_e`,

**Lemma 2** (complete). `E[Q_e^2] <= p_e s_e` for every `e`. Proof: `Q_e^2 <= s_e Q_e` a.s.
and `E[Q_e] = p_e`. QED

**Lemma 3** (deterministic local length; complete). For every vertex `z`, radius `r >= 1`,
and every environment, `|gamma cap E(B_infty(z,r))| <= 2d (b/a) r`.
Proof. All edges of `gamma` inside the ball lie on the segment of `gamma` between its first
entry `x` and last exit `y`, both in `B_infty(z,r)`. A subpath of a geodesic is a geodesic,
so the segment costs `T(x,y) <= b |x-y|_1 <= 2dbr`, and with every weight `>= a` its length
is `<= 2d(b/a) r`. QED (Falsifier B2; worst observed ratio to the bound 0.50.)

**Proposition 3** (complete). Let `r_e := min(dist_infty(e,0), dist_infty(e,v))`.
(i) If `s_e <= C_0 r_e^{-c}` for all `e` with `r_e >= 1` and some `c in (0,1)`, then
    `S <= C(d, b/a, C_0, c) n^{1-c}`.
(ii) If `#{e : s_e >= eps} <= Phi(eps)` with `Phi(eps) = C eps^{-2d/(d-1)} L`, `L` a
    polylogarithm of `n`, then `S <= C' n^{2/(d+1)} L'` - the (DEP) exponent.
Proof. (i): by Lemma 2, `S <= sum_e p_e s_e`. Dyadically in `j >= 0`, the edges with
`r_e in [2^j, 2^{j+1})` lie in `E(B_infty(0, 2^{j+1}+1)) cup E(B_infty(v, 2^{j+1}+1))`,
so by Lemma 3 their `p`-mass is `<= 2 * 2d(b/a)(2^{j+1}+1) <= 12 d (b/a) 2^j`; the edges
incident to `0` or `v` carry `p`-mass `<= 2`. Every edge with `p_e > 0` lies on a
geodesic of length `<= (b/a) d n`, so `r_e <= (b/a) d n` and
`S <= 2 + sum_{j <= log_2((b/a) d n) + 1} C_0 2^{-jc} 12 d (b/a) 2^j <= C n^{1-c}`.
(ii): split at `eps_0`: edges with `s_e <= eps_0` contribute `<= eps_0 sum_e p_e <= eps_0
(b/a) d n`; on the level `s_e in (2^{-k-1}, 2^{-k}]` each term is `p_e s_e <= s_e^2 <=
2^{-2k}`, so the level contributes `<= 2^{-2k} Phi(2^{-k-1})`. Summing `k < k_0` with
`eps_0 = 2^{-k_0}` and balancing (`2^{3k_0} = n` in `d = 2`) gives `n^{2/3} L'`; in general
`d` the same balance as DEP's own Corollary 1.3 calculus gives `n^{2/(d+1)} L'`. QED

So (I3) at full strength follows from a DEP-type statement about the robust influence
`s_e` in place of `p_e`. Section 6 examines what in DEP's proof survives that replacement.

## 4. Theorem 2: an unconditional bound strictly below the trivial one

**Theorem 2** (complete proof; uses (H_M): `rho <= M` a.e., NEW relative to the standing
set). For every `delta in (0, b-a]` and a.e. ball configuration `w`,

`q_e(w) <= (alpha delta)^{-K} p_e + M K delta,`                                (4.1)

hence `E[Q_e^2] <= (alpha delta)^{-K} p_e^2 + M K delta p_e` and

`S <= (alpha delta)^{-K} sum_e p_e^2 + M K delta sum_e p_e .`                   (4.2)

With (DEP) and `sum_e p_e <= (b/a) d n`, optimizing `delta = (sum p^2 / sum p)^{1/(K+1)}`:

`S <= C(alpha, M, K, d, b/a) n^{1 - (d-1)/((d+1)(K+1))} (log n)^{d/(K+1)} ,`

i.e. in the campaign's `d = 2`, `K = 6`: `S <= C n^{20/21} (log n)^{2/7}`.

Proof of (4.1). Fix `w` and a box `Q = prod_i I_i` with each `I_i` an interval of length
`delta` inside `[a,b]` containing `w_i` (possible since `delta <= b-a`). For `w' in Q`,
`||w - w'||_1 <= K delta`. By P1's Lemma B(ii) applied to each ball coordinate in turn and
telescoped, `|T_e^{(w)} - T_e^{(w')}| <= ||w - w'||_1`, where `T_e^{(w)}` is the slack
with the ball frozen at `w` (a function of the remaining weights). Since `t_e` is
independent of everything else, `q_e(w) = E[F(T_e^{(w)})]` with `F` the weight c.d.f.,
which is `M`-Lipschitz under (H_M); so `|q_e(w) - q_e(w')| <= M K delta` on `Q`. Finally
`p_e = int q_e rho^{otimes K} >= int_Q q_e rho^{otimes K} >= (alpha delta)^K (q_e(w) - M K
delta)`, which is (4.1). The rest is Lemma 2, summation, and the displayed optimization
(the exponent identity `(2/(d+1) + K)/(K+1) = 1 - (d-1)/((d+1)(K+1))` is a two-line
check). QED

Without (H_M): `F` is uniformly continuous on `[a,b]`, so with the modulus `omega_G(h) :=
sup_t G([t, t+h])` the same proof gives `q_e(w) <= (alpha delta)^{-K} p_e + omega_G(K
delta)` and `S <= (alpha delta)^{-K} C n^{2/(d+1)} (log n)^d + omega_G(K delta) (b/a) d n =
o(n)` along `delta = delta_n -> 0` slowly. So under the bare standing hypotheses (I3)'s
sum is `o(E|gamma|)`; under (H_M) it is a fixed power below.

What Theorem 2 is and is not. It is the first bound on (I3)'s sum below the trivial
`O(n)`, and it is unconditional given (DEP). It is NOT a step toward `n^{2/3}` by this
method: the exponent `1 - (d-1)/((d+1)(K+1))` is the exact price of pure measure-theoretic
robustness (a `delta`-box in the `K`-dimensional ball against an absolute Lipschitz
constant), and no rearrangement of the same two ingredients beats it. Falsifier B1 checks
the Lipschitz input on random continuous instances (worst excess `2e-15`); the box step is
measure theory and is not numerically checkable at laptop sizes (the bound is vacuous
there), which is stated rather than faked.

## 5. Theorem 5: full strength off the attractive configurations

The bottleneck of Theorem 2 is the Lipschitz term. It disappears if one uses a MONOTONE
event in place of membership.

**Lemma 4** (complete). Let `V_e := {gamma cap Nbar(e) != emptyset}` (the geodesic visits
the ball). (i) For fixed outside weights and fixed `t_e`, the event `V_e(w)` is decreasing
in the ball configuration `w` (coordinatewise). (ii) For a.e. `w`,

`q_e(w) <= P(V_e(w)) <= P(V_e) / prod_{i=1}^{K} G([a, w_i]) <= P(V_e) / prod_i (alpha (w_i - a)).`

(iii) `P(V_e) <= sum_{f in Nbar(e)} p_f`.
Proof. (i): a.s. `V_e(w) = {through-Nbar cost < avoid-Nbar cost}`; the through cost is
nondecreasing in every ball weight, the avoiding cost does not read the ball. (ii): the
first inequality is `{e in gamma} subseteq V_e`. For the second, let `W` be an
independent copy of the ball law; by (i), on `{W <= w}` (coordinatewise) and with the same
outside weights, `1_{V_e(w)} <= 1_{V_e(W)}`; integrating first over the outside weights and
then over `W` conditionally on `{W <= w}` gives `P(V_e(w)) <= P(V_e(W) | W <= w) <= P(V_e)
/ P(W <= w)`, and `P(W <= w) = prod_i G([a,w_i])`. (iii) is a union bound. QED

**Theorem 5** (complete). Let `A_eta := {w : min_i w_i <= a + eta}` (some neighbor weight
within `eta` of the minimum - the ATTRACTIVE configurations). Then for every `eta > 0`,

`sum_e E[ Q_e^2 ; W_e notin A_eta ] <= (K+1) (alpha eta)^{-K} sum_e p_e^2
   <= C (K+1) (alpha eta)^{-K} n^{2/(d+1)} (log n)^d`   (by (DEP)).

Proof. For `w notin A_eta`, Lemma 4(ii) gives `q_e(w) <= (alpha eta)^{-K} P(V_e)`, so
`E[Q_e^2 ; notin A_eta] <= (alpha eta)^{-K} P(V_e) E[Q_e] = (alpha eta)^{-K} P(V_e) p_e`. By
Lemma 4(iii) and `xy <= (x^2+y^2)/2`, `sum_e p_e sum_{f in Nbar(e)} p_f <= (1/2)[(K+1)
sum_e p_e^2 + sum_f p_f^2 #{e : f in Nbar(e)}] = (K+1) sum_e p_e^2`, since every `f` lies
in `Nbar(e)` for exactly `K+1` edges `e`. QED

Consequences. (a) `eta` may depend on `n`: with `eta = 1/log n` the constant is
`(alpha)^{-K} (log n)^K` and the non-attractive part of (I3) is `n^{2/(d+1)} (log n)^{d+K}`
- the full (DEP) exponent. (b) Under (DEP), therefore,

`(I3) at n^{2/3+o(1)}  <=  sum_e E[ Q_e^2 ; min_{f in N(e)} t_f <= a + 1/log n ] <= n^{2/3+o(1)}` ,

the ATTRACTIVE RESIDUAL. (c) The residual's trivial bound is `sum_e P(e in gamma, min_{N(e)}
t_f <= a + eta) = E #{e in gamma : a neighbor weighs <= a + eta}`, which is rigorously
`<= E|gamma| <= (b/a) d n` and heuristically of order `eta n` (the geodesic prefers cheap
edges, and a fraction of its neighbors proportional to `eta` is near-minimal) - with
`eta = 1/log n` that is `n / log n`, not `n^{2/3}`. So Theorem 5 does not finish (I3); it
localizes ALL of its remaining content to the configurations where the adversary has put
a near-minimal weight next to `e`.
Falsifiers A4-A7 check Lemma 4(i),(ii) pathwise on every environment and every ball
configuration of the 3x3 instance, and Theorem 5's display per edge, in exact arithmetic.

Remark (Theorem 2 versus Theorem 5). On `A_eta` Theorem 2's box bound still applies, but
combining the two does not improve Theorem 2's exponent: the attractive set's `p`-mass is
not small (consequence (c)), so the Lipschitz term is still paid at scale `sum p_e`.

Remark (for P1's exceptional-set route; a suggestion, not a result). The attractive
residual is only half of a single coordinate away from the controlled part: on `A_eta` the
minimum is attained at one neighbor `f`, and the other `K-1` coordinates are handled by
Lemma 4 at the price `(alpha eta')^{-(K-1)}`. So what (I3) still needs is the ONE-coordinate
statement `sup_{x in [a, a+eta]} P(e in gamma | t_f = x) <= C p_e` for `f` adjacent to `e`
("a nearly free neighbor boosts membership by a constant factor"). If the exceptional-set
route can afford to condition on `Y_{E_e}` only on `{W_e notin A_eta}` and pay the
attractive configurations' mass (`<= K G([a, a+eta])`) elsewhere in its ledger, Theorem 5
already supplies its (I3) input at the (DEP) scale.

## 6. The DEP route to full strength: what survives the ball, what breaks, and the one input

DEP prove (DEP) through Proposition 4.1 of 2307.01162: for any `q : E(Z^d) -> [0,inf)`
that is smooth in the logarithmic scale (`0.1 <= q_e / q_{e'} <= 10` for `||e-e'|| <= 2 log n`),

`(sum_e q_e p_e)^d <= C (sum_e q_e^2)^{(d-1)/2} sum_e q_e .`                     (6.1)

Its proof, as read today: perturb with `tau_e = q_e / ||q||_2` through the Mermin-Wagner
maps of Lemma 2.1 (`t_e -> g^+_{tau_e}(t_e)`, `w <= g^+_tau(w) <= w + C_0 tau`, `g^+_tau(w)
>= w + delta tau` on a good set `B_delta` with `G(B_delta) -> 1`; for DETERMINISTIC `tau`,
`P(g(X) in A) >= exp(-p||tau||^2/(2(p-1))) P(X in A)^p`); a global event `Omega` (every path
of length `>= log n` in the box has half its weights in `B_{delta_0}`; union bound) plus the
log-smoothness (Claim 4.2) give, PATHWISE, that the raise along the perturbed geodesic is
`>= c delta_0 sum_{e in gamma^+} tau_e`; a level pigeonhole (4.15) and the Mermin-Wagner
the Lipschitz comparison `T_h <= T_0 + 2b||h||_1` pushes the raise to all translates
`||h|| <= r := c_1 3^k mu`, forcing `E sum_{e in gamma_h} tau_e >= c (3/8)^k mu` (4.17); and
the sum over translates is closed by

`sum_{||h|| <= r} sum_e tau_e p_{e-h} = sum_e tau_e E|gamma cap Lambda_e(r)| <= C r sum_e tau_e`  (4.18)

(Lemma 3 above is exactly this local-length input). Assembling, `mu^d <= C (8/3^d)^k sum
tau_e`, which is (6.1).

For (I3) the natural weight is the RANDOM, locally determined field `Q_e` (or its
log-scale smoothing `qt_e := sup_{e'} Q_{e'} exp(-||e-e'||/log n)`, which is automatically
smooth, dominates `Q_e`, and inflates `sum qt^2` and `sum qt` by at most `C (log n)^d`):
then `E sum_{e in gamma} qt_e >= sum_e E[Q_e X_e] = sum_e E[Q_e^2] = S` by the tower
property, so the analogue of `mu` IS the target. Survive/break table for the six steps:

| step of DEP's proof | with a random, locally determined `tau` |
|---|---|
| Lemma 2.1 measure change | BREAKS as stated (needs deterministic `tau`); SURVIVES for `tau` measurable w.r.t. the coordinates NOT perturbed (Proposition 6 below) |
| `Omega` union bound | SURVIVES verbatim (a property of the environment) |
| Claim 4.2 (raise pathwise from log-smoothness) | SURVIVES for a log-smoothed field; BREAKS if `tau` is supported on one color class only (paths can avoid a class), unless patched (Route 7) |
| level pigeonhole (4.15) | SURVIVES (needs only `E f(gamma) = mu`) |
| translation `T_h <= T_0 + 2b||h||_1` | SURVIVES (pathwise, law-free) |
| (4.18) `sum_e tau_e E|gamma cap Lambda_e|` | BREAKS: with random `tau_e`, `E[tau_e N_e(r)]` no longer factorizes (`N_e(r) := #{h : ||h|| <= r, e in gamma(h, v+h)}`); needs (CORR') |

**Proposition 6** (conditional Mermin-Wagner; complete given Lemma 2.1). Let `F` be a
sigma-field independent of the coordinates `(X_i)_{i in I}` to be perturbed, `tau = (tau_i)`
`F`-measurable with `||tau||_2 <= 1` a.s., and `A` an event. Then `P((g^+_{tau_i}(X_i))_i
in A) >= exp(-p/(2(p-1))) P(A)^p` for every `p > 1`.
Proof. Conditionally on `F` the vector `tau` is deterministic and the `X_i` are iid with
law `G`, so Lemma 2.1 applies conditionally; take expectations and use Jensen
(`E[Y^p] >= (EY)^p`). QED
For FPP: color the edges of `Z^d` with `D = 2d` classes so that each class is a matching
(direction and parity); for a class `c`, every ball `N(e)` of a class-`c` edge contains
no class-`c` edge, so any `tau` built from `(Q_{e'})_{e' in E_c}` is measurable w.r.t. the
non-class-`c` weights and Proposition 6 applies to perturbing class `c` alone.

**Route 7** (conditional DEP; ROUTE MAP with the anchors above, NOT a theorem). Fix the
class `c` with `S_c := sum_{e in E_c} E[Q_e^2] >= S/D`; let `qt^{(c)}_e := sup_{e' in E_c}
Q_{e'} exp(-||e-e'||/log n)` (smooth, non-class-`c`-measurable, `>= Q_e` on `E_c`),
`tau_e := t qt^{(c)}_e 1_{e in E_c} 1_H / R` with `R^2 := 4 C (log n)^d S_c` and `H :=
{sum_{e in E_c} (qt^{(c)}_e)^2 <= R^2}` (so `||tau||_2 <= t`, `P(H^c) <= 1/4` by Markov
since `E sum (qt^{(c)})^2 <= C (log n)^d S_c`). Perturb class `c` only. The raise along
`gamma^+` is `>= delta_0 sum_{e in gamma^+ cap E_c} tau_e 1_{t_e in B_{delta_0}}`; Claim 4.2
must be replaced by: on `Omega_c := {every path of length L = C log n in the box with
>= theta L class-c edges has at least half of them in B_{delta_0}}` (still a union bound,
`P(Omega_c^c) <= n^{-10}` for a constant `theta` and `G(B_{delta_0}^c)` small enough
depending on `d`), blocks of `gamma^+` with fewer than `theta L` class-`c` edges carry
class-`c` `tau`-mass `<= theta e f_all(block)`, so on the DOMINANT-CLASS event
`{f_c(gamma^+) >= f_all(gamma^+)/(2D)}` (which some fixed class satisfies with `E[f_c 1]
3^k mu}`) the good class-`c` mass is `>= f_c(gamma^+) (1 - 2 D theta e)/(2e) >= f_c(gamma^+)
/ (4e)` for `theta <= 1/(4De)`. Translation is pathwise. The assembly then reads
`c r^d (3/8)^k mu <= sum_{e in E_c} E[tau_e N_e(r)]`, and closes to
`S_c^{(d+1)/2} <= n^{1+o(1)}`, i.e. `S <= n^{2/(d+1)+o(1)}`, IF

`(CORR')   sum_{e in E_c} E[ tau_e N_e(r) ] <= C r^{1+o(1)} (log n)^C sum_e E[tau_e]`   for all `r >= 1`.

Status of (CORR'). Its unconditional-average version is Lemma 3 plus translation
invariance: `E N_e(r) = E|gamma cap Lambda_e(r)| <= C r`. Its content is that the
`tau`-weighting - which favors ball configurations making `e` locally likely for the
`(0,v)` geodesic - does not correlate with `e` being a hub for the translates
`(h, v+h)`. By the tower property it is the two-replica statement `sum_h P(e in gamma^1(0,v),
e in gamma^2(h, v+h)) <= r^{1+o(1)} p_e` with the replicas sharing only the local balls: the
two-endpoint-pair COUSIN of (I3) itself, needing only an `r^{o(1)}` loss and only on
average over `h`. It is not easier in kind, and this note does not claim it; it is the
single input separating Route 7 from a theorem. Everything else in Route 7 is either
verified above (Proposition 6, Lemma 3, the pathwise steps) or is bookkeeping whose shape
I checked against DEP's own text but have NOT written out line by line - so Route 7 is
labeled a route map with proved anchors, not a conditional theorem with a complete proof.

**Observation 8** (why every measure-change approach stops at the same place; complete as
a statement about the methods). Any increasing bijection `g` of `[a,b]` with `g >= id`
fixes `a`, so Mermin-Wagner shifts vanish at the weight minimum: the good sets `B_delta`
exclude a neighborhood of `a`. The box argument of Theorem 2 pays `(alpha delta)^{-K}` for
the same reason a point `w` cannot be reached from the law; the monotone argument of
Theorem 5 pays `prod_i G([a,w_i])^{-1}`, which blows up exactly on `A_eta`. The robust
occupation needed for (CORR') is blocked by the same configurations (a ball frozen near
`a` is the one a shift cannot produce from a typical ball). So the attractive residual of
Theorem 5, the point-conditioning in Proposition 3, and (CORR') are three faces of ONE
missing estimate: the membership (or visit) probability given a ball configuration at
the bottom of the weight support, compared with its unconditional value. That estimate is
Thread-B-shaped (it is a conditional anticoncentration of the slack `T_e` at an attractive
local configuration), in agreement with P1's classification and the tasking's warning.

## 7. Heuristic size of the sum (LABELED HEURISTIC; nothing below is used in Sections 2-6)

In the KPZ picture for `d = 2` (`xi = 2/3`, `chi = 1/3`), `p_e ~ r_e^{-2/3}` in the tube and
`sum_e p_e^2 ~ n^{1/3}`; (DEP)'s `n^{2/3} log^2 n` is an upper bound with `n^{1/3}` of room.
For (I3): revealing `K` weights of bounded range changes the slack `T_e` by `O(1)`
additively, and the relevant question is how many geodesic-adjacent sites sit within
parabolic cost `x^2/n` to a transverse offset `x` gives the wrong answer `x ~ sqrt(n)`,
hence "`P(attractive ball is visited) ~ n^{-1/6}`" and `E[Q_e^2] >~ n^{-1/3}` per tube edge,
which would make `S >~ n^{4/3} > E|gamma|` - impossible. The mistake is that inside the
fluctuation zone `|x| << n^{2/3}` the slack profile across the geodesic is locally
Brownian in the transverse coordinate (scale check: offset `n^{2/3}` costs `n^{1/3}`),
so slack `s` corresponds to offset `s^2 = O(1)`: an `O(1)`-attractive ball boosts `Q_e` by a
CONSTANT factor, `Var(Q_e) ~ p_e^2`, and `S ~ C sum p_e^2 ~ n^{1/3}`. Conclusion of the
heuristic: (I3) as stated is expected TRUE with `n^{1/3}` of room, and a counterexample is
not the right target. Datum from the exact 3x3 enumeration (falsifier A8, no inference
drawn from one lattice size): `sum_e E[Q_e^2] / sum_e p_e^2 = 1.351`.

## 8. Standing and labels

* COMPLETE PROOF: Theorem 1; Lemma 2; Lemma 3; Proposition 3 (i),(ii); Theorem 2 (under
  (H_M); modulus version under the bare standing set); Lemma 4; Theorem 5; Proposition 6
  (given DEP Lemma 2.1 as the referee-verified paper states it); Observation 8 as a
  statement about the three methods.
* CONDITIONAL on (DEP) (referee-verified, so not a live condition): the numerical
  exponents in Theorem 2, Theorem 5 and Proposition 3(ii).
* ROUTE MAP WITH PROVED ANCHORS, NOT A THEOREM: Route 7; its single unproved input is
  (CORR').
* HEURISTIC: Section 7 entirely.
* NUMERICAL DATUM: falsifier A8's ratio 1.351.
* OPEN: the attractive residual `sum_e E[Q_e^2 ; min_{N(e)} t_f <= a + 1/log n]` at
  `n^{2/3+o(1)}`; equivalently (Observation 8) the point-conditioned membership at
  attractive balls; equivalently (CORR'). (I3) at full strength is NOT proved here.
* chi = 1/3 UNMOVED. No variance bound is improved.

Deliverable hierarchy of the tasking, answered: no unconditional full-strength bound;
no counterexample (and the heuristic argues against one); a precise reduction of (I3) to
named DEP-style statements with the delta isolated (Proposition 3, Route 7/(CORR'),
Observation 8); plus, beyond the hierarchy, the two complete partial theorems (Theorem 2:
`n^{20/21+o(1)}` everywhere; Theorem 5: `n^{2/3+o(1)}` off the attractive configurations).

## 9. Break checks

1. Falsifier (`p9_checks.py`, 10/10, 5.2 s): A1 the enumerated geodesic selection is a
   minimizer on all 531,441 environments (ties occur on 31 percent of them - discrete
   weights tie whenever two paths use the same multiset of levels, so a.s. uniqueness is
   unavailable at this instrument; every identity checked holds for any fixed measurable
   selection, which is what is checked); A2 Theorem 1 exact; A3 Lemma 2 exact; A4 Lemma
   4(i) pathwise on every environment and ball coordinate, for the SELECTED geodesic (the
   proof needs it only a.s. under the density hypothesis); A5 Lemma 4(ii) on every ball
   configuration; A6 Theorem 5 per edge (worst LHS/RHS 0.048 - the constant is loose, as
   expected); A7 the neighbor AM-GM; B1 Lemma B(ii) single and l1 (worst excess 2e-15);
   B2 Lemma 3 (worst ratio 0.50); B3 the pinned identity `X = min(B_e + t_e, C_e)`.
2. My first draft of the falsifier claimed tie-freeness from the weight VALUES; the
   enumeration refuted that (A1 failed with up to 6 minimizers) and the claim was
   withdrawn - it was a claim about the instrument, not about any theorem.
3. The slack routine of the first draft computed through-`e` legs in the full graph; a
   simple through-path cannot reuse `e`, so both legs must be computed with `e` deleted.
   Fixed before any number was read; B3 now checks the pinned identity on the fixed
   routine.
4. Theorem 2's `(H_M)`: the standing set has no upper density bound; the statement is
   given in both forms. Note DEP's (1.4) likewise has no upper bound, so (DEP) is not
   weakened by (H_M)'s absence.
5. Theorem 5's constant `(alpha eta)^{-K}` comes from `G([a, w_i]) >= alpha (w_i - a)`; the
   proof never uses an upper density bound.
6. Proposition 3(ii)'s balance reproduces DEP's own beta = 2 calculus, so a robust count
   with DEP's exponent gives exactly DEP's polylog exponent; no sharper constant is claimed.
   against the trivial bound `S <= E|gamma| <= (b/a) d n` and failed it; the heuristic was
   re-derived (Section 7) before anything was written down as a finding.
8. Route 7's bookkeeping: the constants `theta <= 1/(4De)`, the union-bound exponent, the
   truncation `H`, and the dominant-class pigeonhole were each worked once by hand, not
   twice; this is why Route 7 is a route map.

## 10. Honesty block

THE SINGLE HARDEST OPEN STEP, confirmed with my own eyes before writing this: bounding
`P(e in gamma | W_e = w)` for ball configurations `w` with a coordinate near the weight
minimum `a` - the attractive residual of Theorem 5. Theorem 2 reaches such `w` only with
the absolute term `M K delta`; Theorem 5's monotone coupling has zero measure below them;
Mermin-Wagner shifts fix `a` (Observation 8). No estimate on file, DEP's included,
compares a point-conditioned membership probability at the support bottom with its
unconditional value. Everything that would finish (I3) at `n^{2/3+o(1)}` - (CORR'), the
robust count of Proposition 3(ii), the residual - passes through it.

STRONGEST CASE THAT THE MAIN CLAIM IS WRONG (or hits the same wall in disguise). The
main structural claim is that (I3)'s whole difficulty lives on `A_eta`. It would be wrong
as a guide if the non-attractive part were NOT where I put it: Theorem 5 bounds
`E[Q_e^2; notin A_eta]` through the VISIT probability `P(V_e)`, and the visit event is
larger than membership by the neighbor sum `sum_{Nbar(e)} p_f`; if the neighbors'
influences were systematically larger than `p_e` (a geodesic that brushes `e`'s endpoints
but avoids `e`), the AM-GM step would hide a loss - it does not, since it is symmetric in
`e` and `f` and each `f` has exactly `K+1` owners, but that symmetry is the one thing the
reader should re-check. The deeper way it could hit the same wall: the attractive
residual may be NOT a technical artifact but the genuine locus of Thread B at single-edge
granularity, in which case Theorem 5 has merely moved the problem to where P7 already
stands, and the campaign should read "(I3) off `A_eta`" as a bookkeeping result only.

THE ONE CONCRETE CHECK THAT WOULD CONFIRM IT: compute, on P7's exact 4x4-vertex
instrument (184-path enumeration, continuous weights), the conditional membership
probability `q_e(w)` of an interior edge on a grid of ball configurations `w`, and plot
`q_e(w) / p_e` against `min_i w_i - a`. If the ratio stays bounded as `min_i w_i -> a`
(constant-factor attraction, the Section 7 heuristic), the residual is an artifact and a
direct comparison argument should be sought on `A_eta` at the lattice level; if the ratio
grows without bound as the minimum neighbor weight approaches `a` even at fixed small size,
the attractive residual is real and Theorem 5 has only relocated Thread B.

(This was your 19:06-campaign ask for lane P9_i3: attack P1's open input (I3), the
neighbor-conditioned squared-influence sum, under the standing hypotheses - prove a
nontrivial bound, or a conditional theorem, or a counterexample, or a precise reduction to
a named DEP-style statement with the delta isolated; falsifier script; campaign-format fire
note in the lane dir.)
