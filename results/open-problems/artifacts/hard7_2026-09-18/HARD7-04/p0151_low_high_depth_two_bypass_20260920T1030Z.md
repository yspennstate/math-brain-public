Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — this is not GPT-6 at maximum, and I do not claim otherwise.**

# P0151 analytic artifact — low/high depth-two bypass

This is a self-derived theorem-sized proof artifact for `HARD7-04`. It concerns the exact sequential fixed-outdegree affine preferential-attachment model frozen in `operations/claims/P0151.md`. It strengthens the current one-sided lower bound on the expected largest critical-component exponent. It does **not** determine the critical window, prove a matching upper bound, establish `sqrt(n)/log n` scaling, or identify a scaling-limit law.

No finite or exhaustive claim is made here, so no finite checker substitutes for the proof.

---

## Proposition

Fix an integer `m>=2` and `delta>0`. Put

`a:=m+delta`, `A:=2m+delta=a+m`, `pi:=pi_c`,

where

`pi_c:=delta/[2( m a + sqrt(m(m-1)a(a+1)) )]`.

For bond percolation at `pi_c` on Ray / Hazra--van der Hofstad--Ray model (d), define

`gamma_E:=liminf_{n->infinity} log E|C_max(n,pi_c)| / log n`.

Inherit from the preceding HARD7-04 theorem

`b2:=m(1+a pi)/A`,

`b6:=b2+m(m-1)pi^2`,

`b_U:=b2+2m(m-1)pi^2(A+m)/A<1/2`,

`d_*:=1/2-b_U`,

`vartheta:=min(1,d_*A/[4(a+m)pi^3])`,

`kappa_1:=2vartheta(a+m)pi^3/A`,

`d_7:=1/2-(b_U+kappa_1)`,

`lambda:=min(1,d_7A/[4(m-1)(a+m)pi^3])`,

`S:=vartheta+(m-1)lambda`,

`eta_10:=a(a+1)pi^3S/A^2`,

`kappa_10:=2(A+1)pi^3S/A`,

`b10:=b6+eta_10`, `U_10:=b_U+kappa_10<1/2`,

`M_10:=1/2-U_10`,

`rho:=min(1,M_10/[2kappa_10])`,

`b11:=b10+rho eta_10`, `U_11:=U_10+rho kappa_10<1/2`.

Let

`M_11:=1/2-U_11>0`,

and define the new depth-two throttle

`sigma:=min(1, M_11 A/[4(A+1)pi^3])`.                            (P.1)

Set

`eta_12:=sigma a(a+1)pi^4/A^2`,                                  (P.2)

`kappa_12:=2sigma(A+1)pi^3/A`,                                   (P.3)

and

`b12:=b11+eta_12`.                                                 (P.4)

Then

`gamma_E>=b12>b11`,                                               (P.5)

and in fact `b12<1/2`.

The mechanism is a one-step depth-two bypass. For each simple-good bridge root, choose its **oldest historical parent** `v`. If `v` is high-attractiveness, use the failure half of the existing parent ticket for one additional inverse-weight attempt on `v`. If `v` is low-attractiveness, either it has a fresh ordinary grandparent outside the shadow, which can be harvested through a two-edge retained path, or its failure to have such a grandparent is itself sparse and can be charged to the current shadow/seed degree mass. Marking a low parent spent after its first depth-two inspection makes the grandparent percolation bit fresh without imposing a global depth-two independence assumption.

---

## 1. Inherited exploration facts

At completed time `t`, write

`w_x(t):=d_x(t)+delta`.

The inherited process maintains a shadow `Q_t` all of whose marked vertices lie in one true percolation component and has attractiveness

`W_t:=sum_{x in Q_t} w_x(t)`.

The global quantities

`V_t:=sum_x w_x(t)^2`,

`Z_t:=w_1(t)+w_2(t)`,

and the repeated-historical-parent count `N_t^rep` satisfy

`E V_t=O(t)`,                                                     (1.1)

`E Z_t=O(t^h)`, `h:=m/A<1/2`,                                   (1.2)

`E N_t^rep=O(log t)`.                                            (1.3)

The capped bridge profile is

`c(w):=min(w,2A)`.                                                (1.4)

Let `S_t` be the inherited simple-good outside roots: their `m` historical parents are ordinary, outside `Q_t`, and pairwise distinct. The deterministic capped-mass supply is

`sum_{u in S_t} c(w_u(t))
 >= a t-(1+a)W_t-aZ_t-2A N_t^rep-C`.                             (1.5)

For historical label `j`, the existing forward parent-ticket strength is

`q_1:=vartheta`, `q_j:=lambda` for `j>=2`,                        (1.6)

so `0<q_j<=1` and `sum_j q_j=S`.

A historical parent `v=p_j(u)` satisfies

`w_v(t)>=a+1`                                                     (1.7)

because the edge `(u,v)` itself gives `v` one post-birth degree increment.

The inherited forward current event is

`E_12(u)={label 1 is a retained gate into Q_t; label 2 is a retained accepted capped bridge to u}`.

For every simple-good outside root,

`P(E_12(u)|F_t)
 >= pi^2 W_t c(w_u(t))/(At+K)^2`.                               (1.8)

Under `E_12(u)`, the root `u` joins the same underlying percolation component as `Q_t`. The existing forward historical rule then reveals the percolation mark of each `(u,p_j(u))` and, if retained, accepts parent `p_j(u)` with probability

`q_j(a+1)/w_{p_j(u)}(t)`.                                        (1.9)

The immediately preceding bidirectional theorem adds the disjoint reverse orientation and proves `gamma_E>=b11` while retaining the upper coefficient `U_11<1/2` and `E W_t^2=O(t)`.

---

## 2. B23 — assume the depth-two obstruction dominates

The unresolved route after the previous runs was a global statement saying that a linear amount of historical-parent mass has a fresh outside grandparent. Instead of assuming such a supply lemma, suppose the opposite obstruction is common.

For each `u in S_t`, let `v=o(u)` be the historical parent of `u` with smallest birth label, hence the oldest of the `m` pairwise distinct parents. Then every historical parent `g` of `v` is older than `v`, so

`g` cannot be any other historical parent of `u`.                 (2.1)

This removes one entire family of same-root collisions for free.

The key question is now local: when `v` is low-attractiveness, can it fail to have an ordinary historical parent outside the frozen shadow? If it does fail, then all `m` birth edges of `v` end in `Q_t` or in the two initial seed vertices. That obstruction uses `m` genuine degree incidences into a set whose total degree is controlled by `W_t+Z_t`. Thus an abundance of obstructed low parents would force the shadow/seed degree mass itself to be abundant. This converts the putative obstruction into an error term rather than a missing lemma.

**B23 outcome:** successful. The negation of the desired outside-grandparent property is degree-chargeable; it need not be ruled out by an independent branching approximation.

---

## 3. B8 — discretize the intermediate parent into high and low states

Use the deterministic threshold

`L:=2(a+1)`.                                                      (3.1)

For `u in S_t`, with oldest parent `v=o(u)`, split into:

- **HIGH:** `w_v(t)>=L`;
- **LOW:** `w_v(t)<L`.

The split is designed so that each side has a different exact resource.

### 3.1 HIGH: reuse the failure half of the existing ticket

Let `j(u)` be the historical-edge label with parent `v`. Conditional on retention of `(u,v)`, the inherited forward ticket probability is

`r_old=q_{j(u)}(a+1)/w_v(t)<=1/2`                                (3.2)

because `q_j<=1` and `w_v>=2(a+1)`.

If the inherited ticket fails, make one new independent ticket attempt with probability

`sigma(a+1)/w_v(t)`.                                              (3.3)

This is valid by (1.7). Ignoring same-birth duplicate capture for the moment, the **additional** frozen attractiveness obtained from `v`, conditional on `E_12(u)`, has expectation at least

`pi (1-r_old) [sigma(a+1)/w_v] w_v
 >= pi sigma(a+1)/2.`                                             (3.4)

Since the threshold formula gives `pi<1/2`,

`pi sigma(a+1)/2 >= pi^2 sigma(a+1)`.                            (3.5)

Thus every HIGH root carries a uniform extra conditional reward at least the smaller quantity on the right of (3.5).

### 3.2 LOW: expose exactly one fresh grandparent edge

For LOW `v`, declare `v` **spent** immediately after its first depth-two inspection. A spent low vertex is never depth-two-inspected again.

If `v` has an ordinary historical parent `g` outside `Q_t`, choose one deterministically (for example, the smallest birth label among such parents). Because `g` is a historical parent of `v`,

`w_g(t)>=a+1`.                                                     (3.6)

Under `E_12(u)`, use the same percolation bit of `(u,v)` already exposed by the inherited historical rule. If it is retained, expose the as-yet-unrevealed percolation bit of `(v,g)`. If both edges are retained, accept `g` with probability

`sigma(a+1)/w_g(t)`.                                              (3.7)

The bit on `(v,g)` is fresh: an unspent low `v` is outside `Q_t`; the inherited parent rule reveals the edge into `v`, not `v`'s own birth-edge bits. If `v` had earlier been captured as a bridge root, it would already lie in `Q_t`; if an earlier depth-two attempt had inspected its birth edges, it would be spent.

The retained path `Q_t -- (current gate) -- u -- v -- g` certifies that `g` lies in the same true percolation component even when the auxiliary process did not previously mark `v`. Therefore the extra frozen reward, conditional on `E_12(u)`, is exactly

`pi^2 [sigma(a+1)/w_g]w_g
 =pi^2 sigma(a+1)`.                                                (3.8)

This matches the common lower reward selected in (3.5).

**B8 outcome:** successful. The high state supplies unused ticket failure probability; the low state has bounded incidence and can afford one controlled grandparent inspection.

---

## 4. B26 — the only low sporadic exceptions have small capped mass

Two low-parent exceptions must be removed from the root supply.

### 4.1 Low-bad parents

Call a LOW parent `v` **bad** if it has no ordinary historical parent outside `Q_t`. Then every one of the `m` birth edges of `v` ends in `Q_t` or one of the two initial seed vertices. Counting those edge incidences at time `t`,

`m #Bad_t <= deg(Q_t)+d_1(t)+d_2(t) <= W_t+Z_t`.                 (4.1)

A LOW vertex has bounded degree:

`d_v(t)<L-delta<2(a+1)`.                                         (4.2)

Hence a fixed LOW `v` can occur as a historical parent of only `O_{m,delta}(1)` later roots. Since `c(w_u)<=2A`, the total capped mass of simple-good roots whose oldest parent is LOW-bad is

`O(W_t+Z_t)`.                                                     (4.3)

### 4.2 Low-spent parents

Each first inspection of an unspent LOW parent occurs only after a previously outside bridge root `u` satisfies `E_12(u)`, so that root is newly attached to the shadow. There is at most one newly spent parent per such root. Consequently

`#Spent_t <= |Q_t|+C <= W_t/a+C`.                                (4.4)

Again using (4.2), each spent LOW parent is historical parent to only `O_{m,delta}(1)` roots. Therefore the capped mass of simple-good roots whose oldest parent is LOW-spent is

`O(W_t+1)`.                                                       (4.5)

Let `E_t` be the simple-good roots remaining after these two exclusions. From (1.5), (4.3), and (4.5),

`sum_{u in E_t} c(w_u(t))
 >= a t-CW_t-CZ_t-2A N_t^rep-C`.                                (4.6)

For every `u in E_t`, either HIGH gives (3.5), or LOW has a fresh ordinary outside grandparent and gives (3.8).

**B26 outcome:** successful. The sporadic no-grandparent and already-inspected low states cost only existing lower-order shadow/seed errors; they do not consume a linear fraction of the root supply.

---

## 5. Lower drift and the new exponent

For every `u in E_t`, combine (1.8) with the common conditional extra reward `pi^2 sigma(a+1)` from (3.5)/(3.8). Before same-birth duplicate suppression,

`E[R_t^new|F_t]
 >= [pi^4 sigma(a+1) W_t/(At+K)^2]
      sum_{u in E_t} c(w_u(t))`.                                 (5.1)

Using (4.6),

`E[R_t^new|F_t]
 >= eta_12 W_t/t
    -C W_t^2/t^2
    -C W_t Z_t/t^2
    -C W_t N_t^rep/t^2
    -C W_t/t^2
    -C/t`,                                                       (5.2)

where `eta_12` is (P.2).

### Same-birth duplicate suppression is lower order

To ensure the new reward is not double-counted, suppress it if its candidate vertex (`v` in HIGH or `g` in LOW) is captured by another current-birth rule. It is enough to charge the event that one of the remaining `m-2` current labels targets that candidate.

For HIGH roots, using `c(w_u)<=2A` and charging each root-parent incidence once,

`sum_u c(w_u)w_{o(u)} <= C sum_x d_x(t)w_x(t) <= C(V_t+t)`.       (5.3)

For LOW roots, each low intermediate has bounded degree by (4.2), and each chosen grandparent edge is an actual incidence; hence likewise

`sum_u c(w_u)w_{g(u)} <= C(V_t+t)`.                              (5.4)

The extra target probability costs another factor `O(w/t)`. Therefore the conditional loss is at most

`C W_t(V_t+t)/t^3`.                                              (5.5)

Since deterministically `W_t<=At+O(1)` and `E V_t=O(t)`, the expected collision loss is `O(1/t)`. It is absorbed by the final term in (5.2). This suppression preserves every inherited lower-bound contribution, rather than counting one vertex twice.

Adding (5.2) to the inherited `b11` recurrence yields

`E[Delta W_t|F_t]
 >= b12 W_t/t
    -C W_t^2/t^2
    -C W_t Z_t/t^2
    -C W_t N_t^rep/t^2
    -C W_t/t^2
    -C/t`.                                                       (5.6)

Thus the only remaining task is to verify that the new rule does not destroy the sub-square-root upper budget.

---

## 6. Uniform upper first moment remains below `1/2`

For a HIGH candidate of frozen weight `w>=a+1`, the second ticket contributes final current-birth attractiveness at most

`pi [sigma(a+1)/w](w+m)
 <= pi sigma(A+1)`                                                (6.1)

conditional on the current bridge event. A LOW grandparent uses two retained historical edges, hence its corresponding upper reward is no larger than

`pi^2 sigma(A+1)<=pi sigma(A+1)`.                                (6.2)

For the forward event, `c<=2A` and there are at most `t+O(1)` possible roots, so the additional upper first-moment coefficient is at most

`kappa_12=2sigma(A+1)pi^3/A`.                                    (6.3)

By (P.1),

`kappa_12<=M_11/2`.                                               (6.4)

Therefore

`U_12:=U_11+kappa_12
 <=1/2-M_11/2
 <1/2`.                                                          (6.5)

The lower coefficient is strictly smaller than the corresponding upper allowance because

`eta_12/kappa_12
 =a(a+1)pi/[2A(A+1)]<1`.                                         (6.6)

Since `b11<U_11`, (6.5)--(6.6) also imply `b12<U_12<1/2`.

---

## 7. Square-jump closure

The new mechanism adds at most one extra marked vertex for each forward `E_12` root. Its inverse-weight form keeps its square cost within the already available global `V_t` budget.

For HIGH roots, conditional on `E_12(u)`, the squared final-weight reward of the extra ticket is bounded by

`C [sigma(a+1)/w_v](w_v+m)^2 <= C(w_v+m)`.                       (7.1)

Summing over root-parent incidences and using `c<=2A`,

`sum_{u:HIGH} c(w_u)(w_{o(u)}+m)
 <= C(V_t+t)`.                                                    (7.2)

For LOW roots, each low intermediate is parent to only `O(1)` candidate roots, and the chosen grandparent relation is an actual edge incidence. Hence

`sum_{u:LOW} c(w_u)(w_{g(u)}+m)
 <= C(V_t+t)`.                                                    (7.3)

The current forward event supplies a factor `O(W_t/t^2)`. Thus

`E[(R_t^new)^2|F_t]
 <= C W_t(V_t+t)/t^2
 <= C(1+V_t/t)`,                                                 (7.4)

where the last inequality uses the deterministic `W_t=O(t)`. Duplicate suppression only decreases this square cost.

Combining (7.4) with the inherited square-jump estimate and `E V_t=O(t)`, while using the strict upper coefficient `U_12<1/2`, gives the same linear second-moment bound

`E W_t^2=O(t)`.                                                   (7.5)

Indeed the square recurrence has leading multiplier `1+2U_12/t+O(t^-2)` and an `O(1)` forcing term, and `2U_12<1`.

---

## 8. Mean bootstrap and component conversion

Let `mu_t:=E W_t`. Taking expectations in (5.6) and using (1.1)--(1.3) and (7.5) yields

`mu_{t+1}
 >=[1+b12/t-C/t^2]mu_t
   -C/t-C t^(h-1)-C log(t)/t`.                                  (8.1)

The inherited gate-only seed exponent is

`b1=[m+a(1-(1-pi)^m)]/A>h`.                                     (8.2)

Exactly as in the preceding bootstraps, normalize (8.1) by the comparison product `Theta(t^b12)`. After a sufficiently large deterministic starting time, the normalized negative tails are dominated by the positive inherited seed because `b1>h`. Therefore

`E W_n>=c n^b12`.                                                 (8.3)

Every marked shadow vertex lies in one true percolation component. The inherited activation/component-size conversion therefore gives

`E|C_max(n,pi_c)|>=c' n^b12`,                                   (8.4)

which proves (P.5).

Strictness is immediate from `sigma>0`, `a>0`, `pi>0`:

`b12-b11=sigma a(a+1)pi_c^4/A^2>0`.                             (8.5)

For orientation only, at `m=2, delta=1`, the definitions give approximately

`b11=0.4594455899210341`,

`b12=0.4594477159927709`.

This numerical value is not used in the proof.

---

## 9. Scope and remaining obligation

This is **PARTIAL / SOURCE OPEN**. The proved statement is only a strict improvement of the expected largest-component lower exponent at the exact critical threshold. It does not prove

- `gamma_E=1/2`;
- a matching upper bound;
- `sqrt(n)/log n` critical component size;
- a `(log n)^(-2)` finite-size critical window for the exact fixed-`m` sequential model;
- tightness or a scaling-limit law;
- a transfer theorem from independently attached growing random graphs.

The main conceptual gain is that a **global depth-two ancestral supply lemma is unnecessary for one further strict step**: low-intermediate failures can be charged to degree incidence, while high intermediates have an unused ticket-failure half. Going materially beyond this step requires either a multi-generation version of the low/high charging scheme with a nondepleting margin, or a direct finite-to-Pólya-point-tree critical-window coupling.
