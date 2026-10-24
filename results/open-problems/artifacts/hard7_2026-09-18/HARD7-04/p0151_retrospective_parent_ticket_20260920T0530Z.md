# P0151 analytic artifact — retrospective parent-ticket exploration

This is a self-derived analytic proof artifact for `HARD7-04`. It concerns the exact sequential fixed-outdegree affine preferential-attachment model frozen in `operations/claims/P0151.md`. It proves a new lower bound for the admitted expected critical-component exponent. It does **not** identify the full critical window, prove a matching upper bound, establish `sqrt(n)/log n` scaling, or close the source problem.

## Proposition

Fix an integer `m>=2` and `delta>0`. Put

`a:=m+delta`, `A:=2m+delta`,

and let

`pi:=pi_c:=delta/[2( m a + sqrt(m(m-1)a(a+1)) )]`.

Run bond percolation with retention `pi` on Ray/Hazra--van der Hofstad--Ray sequential fixed-outdegree affine preferential attachment model (d). Let `C_max(n,pi)` be the largest percolation component and

`gamma_E:=liminf_{n->infinity} log E|C_max(n,pi)| / log n`.

The preceding HARD7-04 capped-bridge theorem gives

`gamma_E>=b6`,

where

`b2:=m(1+a pi)/A`,
`b6:=b2+m(m-1)pi^2`.

It also gives an upper first-moment coefficient for the capped connected shadow,

`b_U:=b2+2m(m-1)pi^2(A+m)/A < 1/2`.                       (P.1)

Define

`d_*:=1/2-b_U>0`,

`vartheta:=min(1, d_* A/[4(a+m)pi^3])`,                         (P.2)

`eta_R:=vartheta a^2 pi^3/A^2`,                                 (P.3)

and

`b7:=b6+eta_R`.                                                   (P.4)

Then

`gamma_E>=b7>b6`,                                                 (P.5)

and `b7<1/2`.

The new mechanism is a **two-time exploration**: when a current birth uses one edge to enter the connected shadow and another edge to capture an old outside vertex `u`, the process is allowed to inspect one previously unrevealed percolation bit on a distinguished edge from the birth of `u`. If that historical edge is retained, an auxiliary parent ticket can capture its old endpoint as well. The ticket cancels the potentially large parent degree, and the historical percolation bit is queried at most once.

---

## 1. Inputs retained from the capped-bridge construction

For an old vertex `v` at completed time `t`, write

`w_v(t):=d_v(t)+delta`.

There is a deterministic `K<infinity`, depending only on the finite initial state and `(m,delta)`, such that all denominators during birth `t+1` satisfy

`At-K <= D_{t,j} <= At+K`                                        (1.1)

for all large `t` and every edge label `j=1,...,m`, and

`T_t:=sum_{v<=t} w_v(t)=At+O(1)`.                                (1.2)

Let

`V_t:=sum_{v<=t} w_v(t)^2`,
`Z_t:=w_1(t)+w_2(t)`.

The previous proof established

`E V_t=O(t)`,                                                     (1.3)

and, with

`h:=m/A<1/2`,

`E Z_t=O(t^h)`.                                                   (1.4)

It also constructed a connected shadow `Q_t` containing only ordinary vertices `v>=3`, with attractiveness

`W_t:=sum_{v in Q_t} w_v(t)`.                                    (1.5)

The base update uses all `m` edges of the new birth. A retained edge into frozen `Q_t` is a **gate**. An outside retained target `u` is a capped bridge if an independent auxiliary mark accepts it with probability

`c(w_u)/w_u`, where `c(w):=min(w,2A)`.                            (1.6)

If a gate occurs, the new vertex and all distinct accepted bridge roots are added. For any connected shadow of this form, the preceding theorem gives the lower drift

`E[Delta_base W_t | F_t]
 >= b6 W_t/t
    -C W_t^2/t^2
    -C W_t Z_t/t^2
    -C W_t/t^2
    -C/t`,                                                        (1.7)

and the upper drift

`E[Delta_base W_t | F_t]
 <= [b_U/t+O(t^-2)]W_t+C/t`.                                     (1.8)

Its square-jump estimate can be written

`E[(Delta_base W_t)^2 | F_t] <= C(1+V_t/t)`                     (1.9)

up to a change of `C`. These estimates depend only on connectivity, exclusion of vertices `1,2`, the cap `c<=2A`, and the deterministic denominator bounds, so they remain valid when the shadow is enlarged by the additional connected captures below.

---

## 2. Distinguished historical edges and deferred decisions

For every ordinary vertex `u>=3`, designate once and for all edge label `1` from the birth of `u`, and let

`p(u)<u`

be its old endpoint. The attachment target `p(u)` is part of the already generated graph and is therefore known. The bond-percolation retention bit on this distinguished edge is exposed lazily.

### Lemma 2.1 — freshness of the historical retention bit

Suppose at completed time `t>=u` that

`u notin Q_t` and `p(u) notin Q_t`.                               (2.1)

Then the retention bit of the distinguished historical edge `(u,p(u))` can be kept unexposed, and conditional on the exploration history used below it is still an independent Bernoulli(`pi`) bit.

**Proof.** At the birth of `u`, the target `p(u)` was outside the then-current shadow because the shadow only grows and `p(u) notin Q_t`. Hence this distinguished edge could not itself have been a gate. If some *other* edge of the birth of `u` had been a gate, then the base rule would have added the newborn `u`, contradicting `u notin Q_t`. Thus no gate occurred at that birth, and no outside bridge-retention bit was needed to update the shadow. At later times the base exploration only uses edges of later newborns, not the old outgoing edge `(u,p(u))`. In the augmented exploration below, the historical bit is queried only after a current gate-and-bridge event has already captured `u`; therefore it is queried at most once. By deferred decisions for independent bond percolation, under (2.1) it remains a fresh Bernoulli(`pi`) bit. `square`

This lemma is the reason the extra factor `pi` below is legitimate despite the adaptive exploration.

---

## 3. A deterministic supply of usable historical parents

Define the frozen good-root set

`G_t:={u in {3,...,t}: u notin Q_t, p(u)>=3, p(u) notin Q_t}`.     (3.1)

Every ordinary vertex has `w_u(t)>=a`, hence `c(w_u(t))>=a`.

The number of ordinary roots already in the shadow is at most

`|Q_t|<=W_t/a`.                                                   (3.2)

The number of distinguished edges from vertices `u<=t` whose endpoint lies in `Q_t` is at most the total graph degree of `Q_t`, hence at most `W_t`. The number whose endpoint is one of the two excluded seed vertices is at most their total degree, hence at most `Z_t`. Therefore

`|G_t| >= t - W_t/a - W_t - Z_t - C`,                            (3.3)

and consequently

`S_t:=sum_{u in G_t} c(w_u(t))
 >= a t -(1+a)W_t-aZ_t-C`.                                       (3.4)

No stochastic degree-distribution approximation is used in (3.3)--(3.4).

---

## 4. The retrospective parent ticket

Use the first two current edge labels; this is why only `m>=2` is needed.

- Current edge `1` is required to be a gate into frozen `Q_t`.
- Current edge `2` is required to be a retained capped bridge to some `u in G_t`, using the already defined acceptance probability `c(w_u)/w_u`.

When both events occur, the base construction has already connected the newborn to `Q_t` and captured `u`. Now reveal the fresh historical retention bit on `(u,p(u))`. If it is retained, draw an independent auxiliary parent ticket and accept with probability

`vartheta a/w_{p(u)}(t)`.                                        (4.1)

This is at most one because `p(u)>=3` implies `w_{p(u)}(t)>=a`. If accepted and `p(u)` has not already been captured by another bridge in the same current birth, add `p(u)` to the shadow. Connectivity is automatic: `Q_t` -- current newborn -- `u` -- `p(u)` is a retained path.

Let `B_t` denote the **additional** final-time-`t+1` attractiveness added by this parent step, with `B_t=0` if the parent was already present or simultaneously captured by the base step. Then the exact augmented increment is

`Delta W_t=Delta_base W_t+B_t`.                                  (4.2)

---

## 5. Lower drift: a strictly positive new exponent coefficient

For `u in G_t`, current edge `1` targeting frozen `Q_t` cannot change the current weight of `u`. Sequential conditioning and (1.1) therefore give

`P(edge 1 is a gate AND edge 2 is an accepted bridge to u | F_t)
 >= pi^2 W_t c(w_u(t))/(At+K)^2`.                                (5.1)

Conditional on this event, Lemma 2.1 makes the historical retention bit a fresh Bernoulli(`pi`) bit. If the parent is not otherwise captured in this birth, the ticket (4.1), multiplied by the parent's current attractiveness, has conditional expected reward exactly

`pi * [vartheta a/w_p(t)] * w_p(t)=pi vartheta a`.                (5.2)

Summing the raw reward over `u in G_t` and using (3.4) gives

`E[B_t^raw|F_t]
 >= pi^3 vartheta a W_t S_t/(At+K)^2`

` >= eta_R W_t/t
    -C W_t^2/t^2
    -C W_tZ_t/t^2
    -C W_t/t^2`,                                                   (5.3)

with

`eta_R=vartheta a^2 pi^3/A^2`.                                   (5.4)

The only possible overcount in this fixed `(edge 1,edge 2)` construction is that the historical parent `p(u)` is captured as a base bridge by one of the later current edge labels `3,...,m`. For any prescribed old parent, the capped bridge probability of one such later edge is at most

`pi c(w_p)/(At-K) <= C/t`.                                       (5.5)

There are only `m-2` such labels. Multiplying this extra `O(1/t)` factor into the raw parent-certificate expectation shows

`E[B_t^raw-B_t | F_t] <= C W_t/t^2+C/t^2`.                       (5.6)

Thus

`E[B_t|F_t]
 >= eta_R W_t/t
    -C W_t^2/t^2
    -C W_tZ_t/t^2
    -C W_t/t^2
    -C/t`.                                                         (5.7)

Combining with (1.7),

`E[Delta W_t|F_t]
 >= b7 W_t/t
    -C W_t^2/t^2
    -C W_tZ_t/t^2
    -C W_t/t^2
    -C/t`,                                                         (5.8)

where `b7=b6+eta_R>b6` because every factor in `eta_R` is strictly positive.

---

## 6. Upper drift and why the second moment still closes

The extra gain must not push the square-moment growth exponent to `1/2`.

For an upper bound, current edge `1` is a gate with probability at most

`[pi/(At-K)](W_t+m)`.                                             (6.1)

The total probability that current edge `2` is an accepted capped bridge is at most

`[pi/(At-K)] sum_{u<=t} c(w_u) <= 2pi+O(t^-1)`.                  (6.2)

Given a candidate parent with current attractiveness `w>=a`, historical retention plus the ticket has expected **final** reward at most

`pi [vartheta a/w](w+m) <= pi vartheta(a+m)`.                     (6.3)

Therefore

`E[B_t|F_t]
 <= [kappa_U/t+O(t^-2)]W_t+C/t`,                                 (6.4)

where

`kappa_U:=2 vartheta(a+m)pi^3/A`.                                 (6.5)

By the definition (P.2) of `vartheta`,

`kappa_U <= d_*/2`.                                               (6.6)

Hence the augmented upper coefficient

`b_U':=b_U+kappa_U <= b_U+d_*/2=(b_U+1/2)/2 <1/2`.               (6.7)

### Square of the parent jump

Ignore the gate requirement, which can only increase an upper bound. If edge `2` is an accepted bridge to `u`, the conditional squared reward from the historical parent certificate is at most a constant times

`vartheta a [w_{p(u)}(t)+1]`.                                    (6.8)

Since `c<=2A`, summing over possible roots gives

`E[B_t^2|F_t]
 <= C/t * [ sum_{u=3}^t w_{p(u)}(t) + t ]`.                      (6.9)

Each distinguished edge is an actual graph edge incident to its endpoint. Therefore the number of distinguished children pointing to a vertex `v` is at most `d_v(t)`, and

`sum_{u=3}^t w_{p(u)}(t)
 <= sum_{v<=t} d_v(t) w_v(t)
 <= sum_{v<=t} w_v(t)^2
 =V_t`.                                                           (6.10)

Consequently

`E[B_t^2|F_t] <= C(1+V_t/t)`.                                   (6.11)

Together with (1.9) and `(x+y)^2<=2x^2+2y^2`,

`E[(Delta W_t)^2|F_t] <= C(1+V_t/t)`.                           (6.12)

Using (1.3), (6.4), and the deterministic bound `W_t<=At+O(1)`, the standard square expansion yields

`E W_{t+1}^2
 <= [1+2b_U'/t+O(t^-2)] E W_t^2+C`.                            (6.13)

Because `2b_U'<1`, a linear induction gives

`E W_t^2=O(t)`.                                                   (6.14)

This is the only role of the safety thinning `vartheta`: it preserves a strict half-exponent margin without needing a new global inequality for all `(m,delta)`.

---

## 7. Mean bootstrap to exponent `b7`

Take expectations in (5.8). From (6.14), `W_t<=At+O(1)`, and (1.4),

`E[W_t^2]/t^2=O(t^-1)`,

`E[W_t Z_t]/t^2 <= C E Z_t/t=O(t^{h-1})`.                        (7.1)

Thus, with `mu_t:=E W_t`,

`mu_{t+1}
 >= [1+b7/t-C/t^2]mu_t-C/t-Ct^{h-1}`.                           (7.2)

The augmented process contains the old base process, so the previous gate-concavity seed remains valid:

`mu_t>=c t^{b1}`                                                  (7.3)

for a fixed `b1>h`. Also `b7>b6>b2>h`.

Let `P_{T,t}:=prod_{s=T}^{t-1}(1+b7/s-C/s^2)`, so `P_{T,t}=Theta((t/T)^b7)` for fixed large `T`. Divide (7.2) by `P_{T,t+1}` and sum from `T` to infinity. The normalized negative tails are

`O(T^{-b7})+O(T^{h-b7})`,                                        (7.4)

whereas the normalized seed from (7.3) is `Omega(T^{b1-b7})`. Since `b1>h` and `b1>0`, choosing one fixed sufficiently large `T` makes the seed dominate the entire future error tail. Therefore

`E W_n>=c' n^{b7}`.                                               (7.5)

---

## 8. Convert attractiveness growth to component-size growth

At every later birth, the event that current edge `1` alone is a retained gate into the shadow has conditional probability at least

`pi W_t/(At+K)`.                                                  (8.1)

On this event the newborn itself is added, so if `N_t:=|Q_t|`,

`E[N_{t+1}-N_t | F_t] >= pi W_t/(At+K)`.                         (8.2)

Summing (8.2) and using (7.5),

`E N_n >= c sum_{t<=n} t^{b7-1} >= c' n^{b7}`.                  (8.3)

The construction preserves connectivity in the **actual percolated graph**, hence `Q_n` is contained in one true component and

`E|C_max(n,pi_c)|>=E N_n>=c'n^{b7}`.                             (8.4)

This proves `gamma_E>=b7`.

Finally, `eta_R<kappa_U` because `a/A<1` and the lower coefficient uses one factor `a/A` more, while `b6<b_U`. Thus

`b7<b_U+kappa_U=b_U'<1/2`,                                       (8.5)

which proves the remaining assertion.

---

## 9. Scope and unpaid source obligation

The theorem moves the frozen expected-size lower exponent, but it remains strictly below `1/2`. It does not establish a critical-window width, the `sqrt(n)/log n` scale, tightness, surplus laws, or a scaling-limit object.

The strongest separate operator result from the preceding spectral run remains

`1-r(pi_c T_L)=C_spec/L^2+O(L^-3)`.

The source-level gap is still the finite-graph transfer at `(log n)^-2` precision. The present parent-ticket theorem shows that the exact sequential graph contains additional exploitable historical connectivity beyond a one-generation Pólya-point-tree exploration; it does **not** show that this correction is negligible at the true critical-window scale.

Status of this artifact: **analytic self-check / PARTIAL**, no independent audit.