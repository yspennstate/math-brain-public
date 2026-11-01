# P0151 analytic artifact — parallel historical-parent recovery after sparse-repeat deletion

This is a self-derived analytic proof artifact for `HARD7-04`. It concerns the exact sequential fixed-outdegree affine preferential-attachment model frozen in `operations/claims/P0151.md`. It proves a new lower bound for the expected largest critical component. It does **not** identify the critical-window width, prove a matching upper bound, establish the conjectural `sqrt(n)/log n` scale, or close the source problem.

No finite/exhaustive claim is made in this artifact, so no finite checker is substituted for the proof. Every new theorem-sized assertion used below is proved on the page.

---

## Proposition

Fix an integer `m>=2` and `delta>0`. Consider Ray / Hazra--van der Hofstad--Ray model (d): each arriving vertex has exactly `m` sequential edges to older vertices; an old target is selected with probability proportional to its **current** degree plus `delta`, including within-birth degree updates; self-loops of the new vertex are excluded; after the graph is generated, each edge is retained independently with probability `pi`.

Put

`a:=m+delta`, `A:=2m+delta=a+m`,

and work at the exact critical retention probability

`pi:=pi_c:=delta/[2( m a + sqrt(m(m-1)a(a+1)) )]`.

Let

`gamma_E:=liminf_{n->infinity} log E|C_max(n,pi_c)| / log n`.

The preceding HARD7-04 chain established the following constants. First

`b2:=m(1+a pi)/A`,

`b6:=b2+m(m-1)pi^2`.

The capped-bridge upper coefficient is

`b_U:=b2+2m(m-1)pi^2(A+m)/A < 1/2`.

Let

`d_*:=1/2-b_U`,

`vartheta:=min(1, d_* A/[4(a+m)pi^3])`,

`kappa_1:=2 vartheta(a+m)pi^3/A`,

`b_U':=b_U+kappa_1<1/2`,

`d_7:=1/2-b_U'`,

and

`lambda:=min(1, d_7 A/[4(m-1)(a+m)pi^3])`.

The previous serial historical-fallback theorem then gave

`b7:=b6+vartheta a^2 pi^3/A^2`,

`b8:=b7+[a^2 pi^2/A^2](1-pi vartheta)
                 [1-(1-pi lambda)^(m-1)]`,

and proved

`gamma_E>=b8`,

while its upper coefficient was

`b_U'':=b_U+kappa_1+kappa_F<1/2`,

where

`kappa_F:=2(m-1)lambda(a+m)pi^3/A`.

Define the conserved historical-ticket mass

`S:=vartheta+(m-1)lambda`,

and the new coefficient

`eta_P:=a^2 pi^3 S/A^2`,

`b9:=b6+eta_P`.                                                    (P.1)

Then

`gamma_E>=b9>b8`,                                                  (P.2)

and

`b9<1/2`.                                                          (P.3)

The new ingredient is to abandon the previous serial first-success rule on almost all roots. We show that births with repeated historical parents have only logarithmic expected count. After deleting those exceptional roots, all `m` historical parents are distinct and can be harvested **in parallel**. Parallelization uses exactly the same total ticket strength `S` and exactly the same upper first-moment budget as the previous serial construction, but it removes the serial reach-loss and therefore gives a strictly larger certified lower drift.

---

## 1. Inherited estimates, stated precisely

For a vertex `u` present at completed time `t`, write

`w_u(t):=d_u(t)+delta`.

There is a fixed finite `K=K(m,delta,initial graph)` such that each denominator for the `j`th edge of birth `t+1` lies in

`At-K <= D_{t,j} <= At+K`.                                        (1.1)

The total attractiveness is

`T_t:=sum_{u<=t}w_u(t)=At+O(1)`.                                  (1.2)

Let

`V_t:=sum_{u<=t} w_u(t)^2`.                                       (1.3)

The standard square-attractiveness recurrence, already proved in the capped-bridge artifact, is

`E V_t=O(t)`.                                                      (1.4)

For the two finite seed vertices put

`Z_t:=w_1(t)+w_2(t)`.

Then, with

`h:=m/A<1/2`,

`E Z_t=O(t^h)`.                                                    (1.5)

The capped connected-shadow process uses

`c(w):=min(w,2A)`                                                  (1.6)

as its accepted-bridge numerator. Its base drift theorem gives, for its shadow attractiveness `W_t`,

`E[Delta W_t|F_t]
 >= b6 W_t/t
    -C W_t^2/t^2
    -C W_t Z_t/t^2
    -C W_t/t^2
    -C/t`,                                                         (1.7)

before any historical-parent bonus is added. The same base construction has an upper drift coefficient `b_U<1/2` and square-jump estimate controlled by `1+V_t/t`.

The preceding serial historical construction also proved a deterministic supply estimate that will be reused. If `p_j(u)` denotes the endpoint of historical birth-edge label `j` of an ordinary old root `u`, define

`G_t^(m):={u>=3: u notin Q_t,
                 p_j(u)>=3 and p_j(u) notin Q_t for every j=1,...,m}`.

Then

`sum_{u in G_t^(m)} c(w_u(t))
 >= a t-(1+a)W_t-aZ_t-C`.                                        (1.8)

The reason (1.8) has no factor `m` loss is edge-incidence counting: roots already in the shadow cost at most `W_t/a`, while all historical incidences landing in the shadow are collectively bounded by the shadow degree and hence by `W_t`, irrespective of which birth-edge labels carry those incidences.

All new work below starts from (1.1)--(1.8), and proves the additional repeat-count, parallel-reward, drift, second-moment, and bootstrap steps explicitly.

---

## 2. B28 — replace “every root is simple” by “all but a logarithmic exceptional set”

The previous simultaneous-parent idea failed because two historical edges of the same root may have the same endpoint. Requiring distinct historical parents for **every** root is false. What matters for an expectation lower bound, however, is the size of the exceptional set.

For an ordinary birth `s`, let `R_s` be the indicator that two of its `m` historical edge labels choose the same old endpoint. Put

`N_t^rep:=sum_{s<=t}R_s`.                                         (2.1)

### Lemma 2.1 — repeated-parent births are logarithmically sparse

There is a constant `C<infinity` such that

`E N_t^rep <= C log t`.                                           (2.2)

### Proof

Fix a birth `s` and labels `i<j`. Condition at the completed state immediately before the birth. If edge `i` chooses an old vertex `v` of attractiveness `w_v`, then before edge `j` is drawn the attractiveness of `v` is at most `w_v+m`, since only the fixed `m` within-birth edges can increment it. By (1.1), for all sufficiently large `s`,

`P(p_i(s)=p_j(s)=v | F_{s-1})
 <= w_v(s-1)[w_v(s-1)+m]/(As-K)^2`.

Summing over `v`,

`P(p_i(s)=p_j(s) | F_{s-1})
 <= [V_{s-1}+mT_{s-1}]/(As-K)^2`.                                (2.3)

There are only `binom(m,2)` pairs of labels. Hence by a union bound, (1.2), and (1.4),

`P(R_s=1)
 <= C E[V_{s-1}+T_{s-1}]/s^2
 <= C/s`.                                                         (2.4)

Summing (2.4) over `s<=t` proves (2.2). `square`

Now define the **simple-good** root set

`S_t:= {u in G_t^(m): p_1(u),...,p_m(u) are pairwise distinct}`.  (2.5)

Since `c(w)<=2A`, removing every repeated-parent birth from the good-root set costs at most `2A N_t^rep` in capped mass. Thus (1.8) gives the deterministic bound

`sum_{u in S_t}c(w_u(t))
 >= a t-(1+a)W_t-aZ_t-2A N_t^rep-C`.                              (2.6)

**B28 outcome.** Successful. The duplicate-parent obstruction need not be solved pointwise. It is confined to an exceptional set whose expected size is only `O(log t)`, and the cap converts that exceptional count directly into a lower-order drift error.

---

## 3. Freshness of historical percolation bits on `S_t`

The shadow is defined by deferred decisions. At the birth of an old root `u`, edge targets are known, but percolation bits of edges pointing outside the then-current shadow need not be revealed unless a retained gate has already occurred and the bridge mechanism needs them.

If `u notin Q_t`, then `u` was never activated at its birth. If in addition `p_j(u) notin Q_t` for every `j`, then monotonicity of `Q` implies each `p_j(u)` was outside the shadow at the birth of `u`. Therefore none of the historical percolation bits on the edges `(u,p_j(u))` was needed to certify a gate or a bridge that entered the shadow. They may be kept unrevealed until `u` is later captured.

Consequently, conditional on the current exploration sigma-field and on `u in S_t`, the `m` historical percolation bits are still mutually independent Bernoulli(`pi`) variables. Auxiliary ticket variables introduced below are also fresh and mutually independent.

This is only a revelation convention for independent bond percolation; it does not alter the underlying percolated graph.

---

## 4. B12 — preserve total ticket mass while removing the serial stop

Use current edge label `1` as a retained gate into the frozen shadow `Q_t`. Use current edge label `2` as a retained capped bridge to one root `u in S_t`. Exactly as in the capped-bridge proof,

`P(label 1 is a gate and label 2 is an accepted bridge to u | F_t)
 >= pi^2 W_t c(w_u(t))/(At+K)^2`.                                 (4.1)

Once this event occurs, expose **all** `m` historical percolation bits of `u` in parallel. Assign ticket strengths

`q_1:=vartheta`,

`q_j:=lambda,  j=2,...,m`.                                        (4.2)

If historical edge `j` is retained, accept its old endpoint `p_j(u)` with independent auxiliary probability

`q_j a / w_{p_j(u)}(t)`.                                         (4.3)

This is a valid probability because every parent in `S_t` is an ordinary nonseed vertex, hence `w_{p_j(u)}(t)>=a`, and `0<q_j<=1`.

Because the historical endpoints are pairwise distinct on `S_t`, every successful historical ticket corresponds to a distinct new old vertex. Before accounting for possible collisions with **other current-birth** bridges, the conditional expected frozen attractiveness harvested from historical label `j` is exactly

`pi * [q_j a/w_{p_j(u)}(t)] * w_{p_j(u)}(t)=pi q_j a`.             (4.4)

Therefore the total raw historical reward from `u` is

`R_P = pi a [vartheta+(m-1)lambda]
     = pi a S`.                                                    (4.5)

The previous serial construction used the same ticket strengths but stopped after the first raw success. The present parallel rule changes no ticket strength and introduces no larger ticket probability. It only removes the serial stopping condition on roots where all historical endpoints are distinct.

**B12 outcome.** Successful. The total ticket mass

`S=vartheta+(m-1)lambda`                                          (4.6)

is literally conserved from the previous theorem, so the old upper-budget accounting can be reused without increasing its first-order coefficient.

---

## 5. B11 — dual upper-budget view: same cost, strictly larger certified reward

The relevant upper-budget functional is linear in the ticket strengths. To see this directly, ignore all good-root, distinct-parent, reach, and collision restrictions. For one historical label of ticket strength `q`, the final attractiveness contributed after retention and inverse-weight ticketing has conditional expectation at most

`pi q(a+m)`.                                                       (5.1)

The designated current gate contributes at most `pi(W_t+m)/(At-K)`. A designated capped bridge edge chooses any prescribed old root with probability at most `2A pi/(At-K)`. Summing over the `t+O(1)` candidate roots, the historical label of strength `q` therefore contributes at most

`[2q(a+m)pi^3/A] W_t/t + O(W_t/t^2)+O(1/t)`.                     (5.2)

Summing (5.2) over (4.2) gives

`E[P_t|F_t]
 <= [kappa_P/t+O(t^-2)]W_t+C/t`,                                 (5.3)

where

`kappa_P:=2(a+m)pi^3 S/A`.                                        (5.4)

Since `a+m=A`, and since `S=vartheta+(m-1)lambda`,

`kappa_P
 =2 vartheta(a+m)pi^3/A
  +2(m-1)lambda(a+m)pi^3/A
 =kappa_1+kappa_F`.                                                (5.5)

Thus the parallel construction spends **exactly the same certified first-order upper-drift budget** as the previous serial theorem.

This is the useful duality: the lower reward cares about how much of the ticket mass is lost to serial reach restrictions, whereas the coarse upper budget only cares about the total mass `S`. Removing the stop on the simple-good set improves the lower side while leaving the dual upper constraint unchanged.

**B11 outcome.** Successful. No new square-moment safety margin is consumed relative to the immediately preceding theorem.

---

## 6. New lower drift

Let `P_t^raw` denote the historical-parent attractiveness proposed by the parallel rule before deleting collisions with other accepted bridge targets of the same current birth.

Multiply (4.1) by the reward (4.5) and sum over `u in S_t`. By (2.6),

`E[P_t^raw|F_t]
 >= [pi^3 a S W_t/(At+K)^2]
    [a t-(1+a)W_t-aZ_t-2A N_t^rep-C]`.

Hence

`E[P_t^raw|F_t]
 >= eta_P W_t/t
    -C W_t^2/t^2
    -C W_t Z_t/t^2
    -C W_t N_t^rep/t^2
    -C W_t/t^2`,                                                   (6.1)

with

`eta_P=a^2 pi^3 S/A^2`.                                          (6.2)

### Current-birth collision deletion

No historical parent can equal the current gate target, because each historical parent lies outside `Q_t` while the gate target lies in `Q_t`. No historical parent can equal the designated bridge root `u`, because historical parents are older than `u`.

The only remaining duplication can come from one of the fixed labels `3,...,m` of the **current** birth also capturing the same historical parent through the capped bridge rule. For any prescribed old vertex `v`, the accepted capped-bridge probability of one current label is at most

`2A pi/(At-K)=O(1/t)`.                                            (6.3)

There are only `m-2` such labels. Conditional on a designated gate/bridge/root certificate, each raw historical reward has expected size bounded by a constant after inverse-weight ticketing. Therefore deleting all such current-birth collisions costs at most

`E[P_t^raw-P_t|F_t]
 <= C W_t/t^2+C/t^2`.                                             (6.4)

Combining the base capped drift (1.7), (6.1), and (6.4), the enlarged connected shadow satisfies

`E[Delta W_t|F_t]
 >= b9 W_t/t
    -C W_t^2/t^2
    -C W_t Z_t/t^2
    -C W_t N_t^rep/t^2
    -C W_t/t^2
    -C/t`,                                                         (6.5)

where `b9=b6+eta_P` as in (P.1).

Connectivity is exact: a successful historical parent is joined to `u` by its retained historical edge, `u` is joined to the current newborn by the retained designated bridge, and the newborn is joined to `Q_t` by the retained designated gate. We do not recursively expose historical parents of the newly added parents in the same step.

---

## 7. The second-moment budget remains below one half

By (5.3)--(5.5), adding the parallel historical rule to the capped base process gives upper drift coefficient

`b_U+kappa_P=b_U''<1/2`,                                          (7.1)

exactly the same coefficient already certified for the previous serial construction.

It remains to check that parallel rather than serial harvesting does not change the order of the square jump.

Conditional on a designated root `u`, write the raw historical reward as

`R_u:=sum_{j=1}^m X_j U_j w_{p_j(u)}(t)`,                         (7.2)

where `X_j` is Bernoulli(`pi`) and `U_j` is Bernoulli with mean `q_j a/w_{p_j(u)}(t)`. Since `m` is fixed,

`R_u^2 <= m sum_{j=1}^m X_j U_j w_{p_j(u)}(t)^2`.                 (7.3)

Taking conditional expectation over the historical bits/tickets,

`E[R_u^2 | F_t, current target u]
 <= C sum_{j=1}^m w_{p_j(u)}(t)`.                                 (7.4)

Dropping the gate condition and the simple-good restriction can only increase the upper bound. Current label `2` is an accepted bridge to a prescribed `u` with probability at most `C/t`. Therefore

`E[P_t^2|F_t]
 <= C/t * sum_u [1+sum_{j=1}^m w_{p_j(u)}(t)]`.                   (7.5)

Every historical edge incidence ending at an old vertex `v` is counted at most `d_v(t)` times, up to a finite seed correction. Since `d_v(t)<=w_v(t)`,

`sum_u sum_{j=1}^m w_{p_j(u)}(t)
 <= sum_v d_v(t)w_v(t)+C
 <= V_t+C`.                                                        (7.6)

Thus

`E[P_t^2|F_t] <= C(1+V_t/t)`.                                    (7.7)

The base jump has the same square bound. Hence, with `Y_t:=E W_t^2`, (7.1), (7.7), and (1.4) yield

`Y_{t+1}
 <= [1+2b_U''/t+O(t^-2)]Y_t+C`.                                  (7.8)

Because `2b_U''<1`, a linear induction gives

`E W_t^2=O(t)`.                                                    (7.9)

---

## 8. Mean bootstrap with the logarithmic exceptional set

Take total expectations in (6.5). The deterministic bound `W_t<=T_t=At+O(1)` and Lemma 2.1 give

`E[W_t N_t^rep]/t^2
 <= C E N_t^rep/t
 =O(log t/t)`.                                                     (8.1)

Also, by (7.9),

`E W_t^2/t^2=O(1/t)`,                                             (8.2)

and by `W_t<=Ct` together with (1.5),

`E[W_t Z_t]/t^2=O(t^{h-1})`.                                     (8.3)

Thus, with `mu_t:=E W_t`,

`mu_{t+1}
 >= [1+b9/t-C/t^2]mu_t
    -C/t-C t^{h-1}-C log(t)/t`.                                  (8.4)

A positive polynomial seed is inherited from the gate-only part of the same shadow. Put

`q(pi):=1-(1-pi)^m`,

`b1:=[m+a q(pi)]/A`.                                               (8.5)

The concavity chord for the gate activation probability gives

`mu_t>=c t^b1`,                                                    (8.6)

and `b1>h` because `q(pi)>0`.

Let `G_t` be the positive comparison product, from a sufficiently large deterministic starting time,

`G_{t+1}=G_t[1+b9/t-C/t^2]`.

Then

`G_t=Theta(t^b9)`.                                                 (8.7)

Divide (8.4) by `G_{t+1}` and sum from a large start `T`. The three negative tails are bounded respectively by

`C T^{-b9}`,

`C T^{h-b9}`,

and

`C T^{-b9} log T`.                                                (8.8)

Meanwhile (8.6) gives the normalized positive seed

`mu_T/G_T >= c T^{b1-b9}`.                                       (8.9)

Relative to (8.9), the three error bounds in (8.8) are respectively

`O(T^{-b1})`, `O(T^{h-b1})`, and `O(T^{-b1}log T)`,                (8.10)

all tending to zero because `b1>h>=0`. Choose one fixed sufficiently large `T`. The normalized seed then dominates the entire remaining negative tail, yielding

`E W_n>=c' n^b9`                                                   (8.11)

for all large `n`.

To convert attractiveness growth to a vertex-count lower bound, use one future retained gate edge. At birth `t+1`, current label `1` hits the shadow and is retained with conditional probability at least

`pi W_t/(At+K)`.                                                   (8.12)

Such an event activates the newborn and adds a genuinely new vertex to `Q`. Summing (8.12) for `t in [n/2,n]` and using (8.11),

`E|Q_n| >= c sum_{t=n/2}^n E W_t/t
         >= c' n^b9`.                                             (8.13)

The shadow is connected in the actual percolated graph, so

`E|C_max(n,pi_c)|>=E|Q_n|>=c'n^b9`.                              (8.14)

Therefore

`gamma_E>=b9`.                                                     (8.15)

---

## 9. Strict comparison with the preceding serial bound

Write

`R:=1-(1-pi lambda)^(m-1)`.                                      (9.1)

The preceding certified historical bonus from the serial rule was

`eta_serial
 =a^2 pi^3 vartheta/A^2
  +a^2 pi^2(1-pi vartheta)R/A^2`.                                (9.2)

The new parallel bonus is

`eta_P
 =a^2 pi^3[vartheta+(m-1)lambda]/A^2`.                         (9.3)

Hence

`eta_P-eta_serial
 =[a^2 pi^2/A^2]
   {pi(m-1)lambda-(1-pi vartheta)R}`.                             (9.4)

By the elementary union bound

`R=1-(1-pi lambda)^(m-1)
 <=(m-1)pi lambda`.                                                (9.5)

Substituting (9.5) into (9.4),

`eta_P-eta_serial
 >= a^2(m-1)pi^4 vartheta lambda/A^2
 >0`,                                                              (9.6)

because `m>=2`, `delta>0`, and the definitions give `pi,vartheta,lambda>0`.

Since `b8=b6+eta_serial`, equations (9.3)--(9.6) prove

`b9>b8`.                                                           (9.7)

For the upper location, (5.4) gives

`eta_P/kappa_P=a^2/(2A^2)<1`,                                    (9.8)

while `b6<b_U`. Therefore

`b9=b6+eta_P < b_U+kappa_P=b_U''<1/2`.                            (9.9)

This proves both (P.2) and (P.3).

---

## 10. Numerical orientation only — not part of the proof

For `m=2`, `delta=1`,

`pi_c≈0.04587585476806849`.

The preceding constants evaluate to

`vartheta=lambda=1`,

`b8≈0.45932813530601274`,

while the new bound is

`b9≈0.45932972985981530`.

The gain is about `1.5945538e-6`. These decimals are only orientation; the theorem is the symbolic all-`m>=2`, all-`delta>0` proof above.

---

## 11. What moved and what remains open

The frozen source-relevant metric moves strictly:

**Before:** `gamma_E>=b8`.

**After:**

`gamma_E>=b9
 =b6+[a^2 pi_c^3/(2m+delta)^2]
      [vartheta+(m-1)lambda]
 >b8`.                                                            (11.1)

This remains **PARTIAL / SOURCE OPEN**. It does not prove an upper exponent, `gamma_E=1/2`, a `(log n)^(-2)` window, the `sqrt(n)/log n` scale, susceptibility asymptotics, surplus scaling, tightness, or a component-sequence limit.

The mathematically important new obstruction is now sharper. The local bridge/historical-edge method can continue squeezing a lower exponent toward the square-moment barrier, but the actual source-level critical-window theorem needs a finite-graph exploration that reflects the killed Pólya-point-tree spectral loss at log-age width `L≈log n`, together with dependence errors controlled at the `L^-2` scale. The earlier operator artifact gave

`1-r(pi_c T_L)=C_spec/L^2+O(L^-3)`;

this run does not bridge that operator statement to the finite sequential graph.

---

## 12. Method accounting

- **B28 — replace “for all” by “for typical”: SUCCEEDED.** Pairwise historical-parent distinctness fails pointwise, but repeated-parent births have expectation `O(log t)`, and the cap turns them into a summable normalized drift error.
- **B12 — find what is conserved: SUCCEEDED.** The historical ticket mass `S=vartheta+(m-1)lambda` is unchanged from the serial theorem.
- **B11 — dualize: SUCCEEDED.** The coarse upper-drift cost depends only on `S`, so parallelizing on simple roots spends exactly the prior upper budget while recovering the serial reach-loss. This yields the strict increment (9.6).

No code was used to establish the theorem. There is no finite exhaustive assertion whose truth would be upgraded by a checker; the validation object is this complete analytic argument. The displayed decimal example was independently recomputed only as a sanity check and is not evidence for the asymptotic statement.
