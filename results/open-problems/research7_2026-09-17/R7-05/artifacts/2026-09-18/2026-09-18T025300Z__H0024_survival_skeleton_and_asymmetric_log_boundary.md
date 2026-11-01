Model actually running: **GPT-5.6 Sol. Reasoning level: UNVERIFIED** — this is **not GPT-6 at maximum**; GPT-6 / maximum reasoning was requested, but no authenticated runtime reasoning-effort telemetry or binding model/effort selector is exposed.

# H0024 — survival skeleton, asymmetric logarithmic boundary, and the exact scale-gluing obstruction

Target: `H0024`, Gustavo Oshiro de Carvalho, Fábio Prates Machado, José Hermenegildo Ramírez-González, *Extinction and Survival in an Interval-Activation Frog Model on Z with Random Survival Parameters and Symmetric Random Walks*, arXiv:2607.27082v1, Theorem 3.5(ii) / Remark 3.6.

Status after this note: **PARTIAL / OPEN** for the full source phase diagram. The frozen source metric `G_crit` was already moved to the optimal strict-constant value `1`; this note does not redefine it. It gives three new structural results for the unresolved equality regime. No numerical evidence is used.

## 1. Setup carried forward

Let `((L_x,R_x))_{x in Z}` be iid almost surely finite nonnegative integer-valued directed interval marks. When site `x` is activated it activates

`J_x=[x-L_x,x+R_x] cap Z`.

For a seed `x`, let `H(x)` denote its final activation hull. The hull is an interval, finite or infinite. A finite interval `I` is **closed** when `J_y subseteq I` for every `y in I`. A finite `H(x)` is closed, and a closed interval containing a seed traps its activation cluster.

For `n>=0`,

`p_n := P([0,n] is closed)`.

Writing

`F(u,v)=P(L<=u,R<=v)`,                                              (1.1)

site independence gives

`p_n=prod_{k=0}^n F(k,n-k)`.                                       (1.2)

The preceding R7-05 run proved that

`sum_{n>=0}(n+1)p_n < infinity`                                    (1.3)

implies positive-probability survival. The point of the present note is to identify the exact random object behind (1.3), determine the correct asymmetric second-order functional, and explain why the old fixed-scale second-moment proof stops at equality.

# 2. B12 — find what is conserved: the stationary survival skeleton

Define the survival set

`S := {x in Z : H(x) is infinite}`

and

`theta := P(0 in S)`.

Because `S` is a translation-equivariant measurable factor of the iid mark field, it is stationary and ergodic.

Also define

`N_0 := # { finite closed intervals containing 0 }`.                (2.1)

The previous first-moment argument used only `E N_0`. In fact there is an exact almost-sure dichotomy.

### Theorem 2.1 (closed-hull count exactly detects survival)

For the iid directed interval process,

`theta=0  <=>  N_0=infinity almost surely`,                         (2.2)

and

`theta>0  <=>  N_0<infinity almost surely`.                         (2.3)

#### Proof

Assume first `theta=0`. By translation invariance, `P(x in S)=0` for every fixed `x`; countability of `Z` implies that almost surely `S` is empty. Thus every `H(x)` is finite and closed.

Start with `I_0=H(0)=[a_0,b_0]`. Given a finite closed interval `I_k=[a_k,b_k]`, the hull `H(b_k+1)` is finite and closed and contains `b_k+1`. Hence `I_k` and `H(b_k+1)` overlap or are adjacent, so their union is again an interval. It is closed because every site in the union already has its mark trapped in one of the two constituent closed intervals. Put

`I_{k+1}=I_k union H(b_k+1)`.

Its right endpoint is at least `b_k+1`, so the intervals are strictly increasing. Therefore infinitely many distinct finite closed intervals contain zero, and `N_0=infinity` almost surely.

Now assume `theta>0`. Ergodicity gives asymptotic density `theta` for `S`, hence almost surely there are points of `S` arbitrarily far in both directions. A finite closed interval cannot contain a point `s in S`: if it did, the process started from `s` would remain trapped in that finite interval, contradicting `s in S`.

If `0 in S`, then `N_0=0`. Otherwise let `s_-<0<s_+` be the nearest survival sites to the left and right. Every finite closed interval containing zero must lie inside `[s_-+1,s_+-1]`. There are only finitely many such intervals, so `N_0<infinity`. This proves (2.2)-(2.3). QED.

### Consequence 2.2 — why divergence of the old series is not a converse

Translation invariance gives

`E N_0=sum_{n>=0}(n+1)p_n`.                                        (2.4)

Theorem 2.1 says extinction is an **almost-sure infinitude** statement about `N_0`, not an expectation statement. Under survival, `N_0` is finite almost surely but may still have infinite mean. Therefore

`sum (n+1)p_n=infinity`

cannot by itself be promoted to extinction. This is the exact logical obstruction to reversing the previous theorem.

## 2.1 The conserved gap mass

Suppose `theta>0`. For `d>=1`, define

`g_d := P(0 in S, S cap {1,...,d-1}=empty, d in S)`.                (2.5)

Thus `g_d` is the intensity of survival points whose next survival point to the right is at distance `d`.

Two identities are exact:

`sum_{d>=1} g_d = theta`,                                          (2.6)

and

`sum_{d>=1} d g_d = 1`.                                            (2.7)

For (2.7), each survival point sends one unit of mass to every site in the half-open gap from itself up to, but not including, the next survival point. Every integer receives exactly one unit from the unique survival point immediately to its left (or itself). Translation-invariant mass transport equates mean mass sent from zero with mean mass received at zero, giving (2.7).

There is also a deterministic bridge from survival gaps to closed hulls.

### Lemma 2.3 (gaps between consecutive survival sites are closed)

On the event counted by `g_d`, with `d>=2`, the whole interval `[1,d-1]` is closed. Consequently

`g_d <= p_{d-2}`.                                                   (2.8)

#### Proof

For every `x in {1,...,d-1}`, `x` is not a survival site, so `H(x)` is finite. Since `H(x)` is an interval containing `x`, it cannot contain or cross `0` or `d`; otherwise it would contain a survival site inside a finite closed hull, impossible. Thus

`H(x) subseteq [1,d-1]`.

In particular `J_x subseteq H(x) subseteq[1,d-1]` for every interior site, so `[1,d-1]` is closed. Translation gives probability at most `p_{d-2}`. QED.

Combining (2.7) and (2.8), for every integer `M>=1`,

`1 = sum_d d g_d
   <= M theta + sum_{d>M} d p_{d-2}`.                              (2.9)

Hence the quantitative lower bound

`theta >= (1/M) [1-sum_{d>M} d p_{d-2}]_+`.                        (2.10)

Whenever the closed-hull intensity has a tail smaller than one, survival probability is explicitly positive. This recovers the previous finite-intensity theorem but exposes the conserved object: **unit spatial mass is partitioned among gaps of the survival skeleton**.

# 3. B15 — break left/right symmetry: the second-order parameter is additive

The source is symmetric, but symmetry can conceal which boundary statistic is actually controlling the hull series. So allow different marginal tails

`q_n^L=P(L>n)`, `q_n^R=P(R>n)`,                                   (3.1)

and define

`A_L(n)=prod_{k=0}^n(1-q_k^L)`,
`A_R(n)=prod_{k=0}^n(1-q_k^R)`.                                   (3.2)

Assume `P(L=0,R=0)>0` and the critical logarithmic expansions

`q_n^L = (1/n)(1+a_L/log n+O(1/(log n)^2))`,                       (3.3)

`q_n^R = (1/n)(1+a_R/log n+O(1/(log n)^2))`.                       (3.4)

The dependence between `L` and `R` at the same site remains arbitrary.

### Theorem 3.1 (dependence-robust two-boundary hull asymptotic up to constants)

Under (3.3)-(3.4),

`p_n asymp A_L(n) A_R(n)`                                         (3.5)

and therefore

`p_n asymp 1/[n^2 (log n)^(a_L+a_R)]`.                            (3.6)

#### Proof: upper bound

For every `u,v`,

`F(u,v)<=P(L<=u)=1-q_u^L`,
`F(u,v)<=P(R<=v)=1-q_v^R`.

Split the product (1.2) at `m=floor(n/2)`. Use the left inequality for `k<=m` and the right inequality for `k>m`. Then

`p_n <= A_L(m) A_R(n-m-1)`.                                       (3.7)

The critical expansions imply, by summing logarithms,

`A_L(n) asymp n^-1 (log n)^(-a_L)`,
`A_R(n) asymp n^-1 (log n)^(-a_R)`.                               (3.8)

Replacing `n` by `n/2` changes these products only by bounded factors, so (3.7) is at most a constant times `A_L(n)A_R(n)`.

#### Proof: lower bound

Let

`j(u,v)=P(L>u,R>v)`.

Then

`F(u,v)=1-q_u^L-q_v^R+j(u,v)
       >= (1-q_u^L)(1-q_v^R)-q_u^L q_v^R`.                         (3.9)

For indices bounded away from the two endpoints, factor the right-hand side as

`(1-q_u^L)(1-q_v^R)(1-r_{u,v})`,

where

`r_{u,v}=q_u^L q_v^R/[(1-q_u^L)(1-q_v^R)]`.                       (3.10)

The critical tails imply

`sum_{k=K}^{n-K} r_{k,n-k}=O((log n)/n)=o(1)`                      (3.11)

for a fixed sufficiently large `K`. Thus the product of the interior factors `(1-r)` is bounded below by a positive constant (indeed tends to one).

The finitely many endpoint ratios are also bounded below for all large `n`: for fixed `k`,

`F(k,n-k) -> P(L<=k)`,

and the assumption `P(L=0,R=0)>0` makes the relevant marginal distribution functions positive; the same argument applies at the right endpoint.

Multiplying (3.9) over `k=0,...,n` yields

`p_n >= c A_L(n)A_R(n)`                                           (3.12)

for some `c>0` and all large `n`. Together with the upper bound this proves (3.5). Equation (3.6) follows from (3.8). QED.

### Corollary 3.2 (asymmetric logarithmic survival region)

If

`a_L+a_R>1`,                                                       (3.13)

then the directed interval process survives with positive probability.

Indeed, by (3.6),

`sum_n (n+1)p_n <= C sum_n 1/[n(log n)^(a_L+a_R)] < infinity`,

so Theorem 2.1 / the preceding finite-intensity theorem applies.

Thus the second-order boundary statistic exposed by the two-sided hull mechanism is

`a_L+a_R`,                                                         (3.14)

not `max(a_L,a_R)` and not `min(a_L,a_R)`. In the symmetric case `a_L=a_R=a`, condition (3.13) is exactly

`a>1/2`,                                                           (3.15)

which explains the one-half threshold found in the preceding source-valid H0024 equality family.

This does **not** prove extinction when `a_L+a_R<=1`; it identifies the sharp convergence boundary of the rigorous closed-hull survival mechanism.

# 4. B30 — one logarithmic scale at a time: where the pieces fail to glue

Let

`A := a_L+a_R`.

By (3.6), the expected number of closed intervals containing zero whose span lies in the exponential shell

`e^m <= i+j < e^(m+1)`                                             (4.1)

is

`E W_m
 = sum_{e^m<=n<e^(m+1)} (n+1)p_n
 asymp m^(-A)`.                                                     (4.2)

Hence

`sum_m E W_m < infinity  <=>  A>1`.                               (4.3)

For `A<=1`, expected hull count diverges. Theorem 2.1 shows exactly why that does not finish the problem: survival allows `N_0<infinity` almost surely together with `E N_0=infinity` through a sufficiently heavy survival-gap distribution. The missing step is therefore not another first-moment estimate; it is control of the **dependence of nested hull events across logarithmic scales**.

## 4.1 Failure of the strict-regime second moment at equality

The earlier sharp strict-extinction proof considered

`Z_N = # { (i,j): N<=i,j<=2N and [-i,j] is closed }`.              (4.4)

At the logarithmic critical scale, Theorem 3.1 gives

`E Z_N asymp (log N)^(-A)`.                                        (4.5)

For two candidate intervals, write `d` and `e` for the differences of their left and right endpoints. If both intervals are closed, their intersection core is closed. The excess left wing obeys only left-boundary constraints, and the excess right wing obeys only right-boundary constraints. These live on disjoint site sets. Therefore the same core-plus-wings argument as in the strict proof gives

`P(I and I' closed)
 <= p_core A_L(d-1) A_R(e-1)`.                                    (4.6)

Summing over candidate pairs yields

`E Z_N^2
 <= E Z_N
    + C N^2 p_{Theta(N)}
      (sum_{d<=N}A_L(d-1))(sum_{e<=N}A_R(e-1))`.                   (4.7)

In the symmetric unresolved H0024 regime, `a_L=a_R=a<=1/2`, so

`A_L(d) asymp A_R(d) asymp 1/[d(log d)^a]`,                        (4.8)

and

`sum_{d<=N} A_L(d) asymp (log N)^(1-a)`,                           (4.9)

with the same estimate on the right. Since

`p_{Theta(N)} asymp N^-2 (log N)^(-2a)`,                           (4.10)

(4.7) gives

`E Z_N^2 <= C (log N)^(2-4a) + E Z_N`.                             (4.11)

Meanwhile

`(E Z_N)^2 asymp (log N)^(-4a)`.                                  (4.12)

Thus the available second-moment ratio loses two full logarithms:

`E Z_N^2/(E Z_N)^2 <= C (log N)^2`                                (4.13)

(up to the harmless diagonal term in the range relevant here). Paley-Zygmund therefore supplies only the vanishing lower guarantee

`P(Z_N>0) >= c/(log N)^2`,                                         (4.14)

rather than the scale-uniform positive probability used in the strict case.

This is a **failure of the present gluing argument**, not a theorem that the probability itself has order `(log N)^-2`. The old tail-zero-one upgrade needed a uniform lower bound; (4.14) tends to zero and no longer supplies one.

## 4.2 The exact unresolved object

Theorem 2.1 converts the remaining equality question into a point-process/renewal problem:

> Determine whether the survival skeleton `S` can have positive intensity while the closed-gap upper envelope `g_d<=p_{d-2}` has the critical tail `p_d asymp d^-2(log d)^(-A)`, especially for `A<=1`, under the additional dependence constraints imposed by the iid directed interval environment.

The mass identities

`sum g_d=theta`, `sum d g_d=1`, `g_d<=p_{d-2}`                     (4.15)

are necessary but not sufficient by themselves to rule this out when `A<=1`. The missing ingredient is a genuine cross-scale renewal/capacity inequality, not another local tail estimate.

# 5. Relation back to H0024

The source's interval-activation frog model is symmetric, so the sitewise left and right reach marginals agree. The preceding run constructed literal nearest-neighbour source models with

`q_n=(1/n)(1+a/log n+O(1/(log n)^2))`                              (5.1)

and proved survival for every `a>1/2` while the source first-order coefficient tends exactly to one.

Theorem 3.1 now explains this structurally: two independent spatial boundaries contribute additively to the logarithmic hull exponent, giving `A=2a`. The survival mechanism turns on exactly when `2a>1`.

What remains open in the source-valid symmetric regime includes:

- `a=1/2`;
- `a<1/2` on first-order equality;
- approaches to one from below such as `q_n=(1/n)(1-a/log n+o(1/log n))`;
- nonconvergent/oscillatory slowly varying `ell` crossing the threshold;
- an exact necessary-and-sufficient criterion for the directed pair law.

No converse, full-source closure, paper package, or audit completion is claimed.

# 6. Dated source / prior-art check (2026-09-18)

The current arXiv record for `2607.27082` still surfaces as v1, submitted 29 July 2026, and its abstract still says the critical-line sufficient conditions leave a factor-four gap. Bounded exact-title, identifier, and author-follow-up searches did not surface a later explicit resolution of Remark 3.6; this is negative evidence only, not proof of worldwide openness or novelty.

Relevant prior art remains Roy and Saha, *How Fast do Rumours Spread?*, Journal of Statistical Physics 191, 130 (2024), DOI `10.1007/s10955-024-03343-3`. Their model is a symmetric one-radius rumour process and supplies a product-series barrier criterion. The present note instead treats a directed two-boundary mark with arbitrary same-site dependence and derives the survival-skeleton mass identities directly. No publication-novelty claim is made.

# 7. Frozen metric, outcome, and next route

Frozen metric:

`G_crit = C_surv/C_ext`.

Before this run: `G_crit=1`.

After this run: `G_crit=1`.

**NO MOVEMENT.** The ordinary unchanged count therefore advances `1 -> 2`.

Methods and outcomes:

- **B12:** exact survival-skeleton dichotomy `theta=0 iff N_0=infinity a.s.`, consecutive-survival gaps are closed, and conserved gap-mass identities `sum g_d=theta`, `sum d g_d=1`, `g_d<=p_{d-2}`.
- **B15:** asymmetric critical tails give `p_n asymp n^-2(log n)^-(a_L+a_R)`; `a_L+a_R>1` implies survival. The second-order functional is additive.
- **B30:** exponential-shell expected hull count is `asymp m^-A`; the strict-regime second-moment gluing loses two logarithms at equality, isolating cross-scale renewal dependence as the missing ingredient.

A useful next nonrepeating triple is:

- **B1 — change category:** treat the survival set and maximal closed gaps as a stationary point-process / renewal-capacity object;
- **B20 — find why the algorithm fails:** iterate the maximal closed hull outward and identify the exact conditional kernel preventing a renewal proof;
- **B21 — import an analogous technique:** test cut-point, renewal-intersection, and one-dimensional long-range percolation capacity arguments against the survival-gap kernel.

The source remains **PARTIAL / OPEN**. Independent audits remain `P26 0/1` and distinct `OTHER 0/1`.