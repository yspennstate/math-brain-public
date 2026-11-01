# P0151 analytic artifact — incidence-strengthened historical-parent ticket

This is a self-derived analytic proof artifact for `HARD7-04`. It concerns the exact sequential fixed-outdegree affine preferential-attachment model frozen in `operations/claims/P0151.md`. It proves a strict new lower bound for the expected size exponent of the largest component at the exact critical retention probability. It does **not** determine the full critical window, prove a matching upper bound, establish `sqrt(n)/log n` scaling, or produce a scaling-limit law.

No finite/exhaustive claim is made, so there is no finite checker in place of the proof. The theorem-sized claim is proved on the page.

---

## Proposition

Fix `m>=2` and `delta>0`. Put

`a:=m+delta`, `A:=2m+delta=a+m`,

and

`pi:=pi_c:=delta/[2( m a + sqrt(m(m-1)a(a+1)) )]`.

For bond percolation at `pi_c` on Ray / Hazra--van der Hofstad--Ray model (d), let

`gamma_E:=liminf_{n->infinity} log E|C_max(n,pi_c)| / log n`.

The preceding HARD7-04 theorem introduced

`b2:=m(1+a pi)/A`,

`b6:=b2+m(m-1)pi^2`,

`b_U:=b2+2m(m-1)pi^2(A+m)/A<1/2`,

`d_*:=1/2-b_U`,

`vartheta:=min(1, d_* A/[4(a+m)pi^3])`,

`kappa_1:=2 vartheta(a+m)pi^3/A`,

`d_7:=1/2-(b_U+kappa_1)`,

`lambda:=min(1, d_7 A/[4(m-1)(a+m)pi^3])`,

`S:=vartheta+(m-1)lambda`,

and proved

`gamma_E>=b9`,

where

`b9:=b6+a^2 pi^3 S/A^2`.

Define instead

`eta_10:=a(a+1)pi^3 S/A^2`,

`b10:=b6+eta_10`.                                                  (P.1)

Then

`gamma_E>=b10>b9`,                                                 (P.2)

and in fact

`b10<1/2`.                                                         (P.3)

The improvement is elementary but was invisible in the previous inverse-weight ticket: a historical parent is not a generic ordinary vertex. By the very edge that makes it a parent, it has already received at least one post-birth degree increment. Thus every nonseed historical parent has current attractiveness at least `a+1`, not merely `a`. That one irreversible incidence allows the ticket numerator to increase from `a` to `a+1`. The lower drift improves strictly, while the old reserved second-moment margin is large enough to absorb the corresponding upper-drift increase uniformly for every `m>=2`, `delta>0`.

---

## 1. Inherited exploration and estimates

Write `w_v(t):=d_v(t)+delta`. The preceding parallel-historical-parent construction supplies a connected shadow `Q_t`, its attractiveness

`W_t:=sum_{v in Q_t}w_v(t)`,

seed attractiveness `Z_t`, square-attractiveness budget

`V_t:=sum_v w_v(t)^2`,

and the repeated-parent count `N_t^rep`, with

`E V_t=O(t)`,                                                      (1.1)

`E Z_t=O(t^h)`, `h:=m/A<1/2`,                                    (1.2)

`E N_t^rep=O(log t)`.                                             (1.3)

The capped bridge profile is

`c(w):=min(w,2A)`.                                                 (1.4)

Let `S_t` be the old roots outside `Q_t` whose `m` historical parents are ordinary, outside `Q_t`, and pairwise distinct. The previous proof gives the deterministic supply estimate

`sum_{u in S_t} c(w_u(t))
 >= a t-(1+a)W_t-aZ_t-2A N_t^rep-C`.                              (1.5)

On a designated current retained gate into `Q_t` and a designated current retained capped bridge to `u in S_t`, the `m` historical percolation bits of `u` remain fresh and mutually independent Bernoulli(`pi`) variables by deferred decisions.

The previous ticket strengths are retained unchanged:

`q_1:=vartheta`,

`q_j:=lambda`, `j=2,...,m`,                                      (1.6)

so their total strength is `S`.

The base process before the historical-parent reward obeys

`E[Delta W_t|F_t]
 >= b6 W_t/t
    -C W_t^2/t^2
    -C W_t Z_t/t^2
    -C W_t/t^2
    -C/t`.                                                        (1.7)

The base upper first-moment coefficient is `b_U<1/2`.

---

## 2. B13 — the irreversible incidence raises the historical-parent floor

Let `u>=3` be an ordinary vertex and let `v=p_j(u)>=3` be one of its historical parents. At the birth of `v`, its degree is exactly `m`, so its birth attractiveness is `a=m+delta`. The historical edge `(u,v)` is then attached at the later birth of `u`; regardless of whether that edge survives bond percolation, its creation increases the graph degree of `v` by one. Degrees never decrease. Therefore, deterministically for every later completed time `t>=u`,

`w_v(t)>=a+1`.                                                     (2.1)

This is stronger than the generic ordinary-vertex floor `w_v(t)>=a` used in the preceding ticket construction.

Consequently, for historical label `j` we may replace the auxiliary ticket probability

`q_j a/w_v(t)`

by

`q_j (a+1)/w_v(t)`.                                               (2.2)

By (2.1) and `0<q_j<=1`, (2.2) is always in `[0,1]`.

**B13 outcome:** succeeded. The parent relation itself carries a conserved, irreversible one-unit degree increment that can be converted into a larger inverse-weight ticket without changing the underlying percolated graph.

---

## 3. B15 — break the generic-vertex symmetry

The old historical ticket deliberately treated every ordinary parent as though its only guaranteed attractiveness were its birth value `a`. That symmetry is unnecessarily pessimistic: a vertex under consideration here is known to be the endpoint of a specific historical child edge.

On the event that current label `1` is a retained gate, current label `2` is an accepted capped bridge to `u in S_t`, and historical edge `j` is retained, accept `v=p_j(u)` with the new ticket (2.2).

Because the `m` historical endpoints are pairwise distinct on `S_t`, the frozen attractiveness rewards from different successful labels correspond to distinct new vertices. For label `j`, conditional on `u` and the exploration sigma-field, the expected frozen reward is exactly

`pi * [q_j(a+1)/w_v(t)] * w_v(t)
 =pi q_j(a+1)`.                                                    (3.1)

Summing over labels gives the exact raw historical reward per designated bridged root

`R_10=pi(a+1)S`.                                                   (3.2)

The designated current gate/bridge probability for a root `u` is bounded below by

`pi^2 W_t c(w_u(t))/(At+K)^2`.                                   (3.3)

Multiplying (3.2), summing (3.3) over `u in S_t`, and applying (1.5), gives

`E[P_t^raw|F_t]
 >= eta_10 W_t/t
    -C W_t^2/t^2
    -C W_tZ_t/t^2
    -C W_tN_t^rep/t^2
    -C W_t/t^2`,                                                  (3.4)

where

`eta_10=a(a+1)pi^3S/A^2`.                                        (3.5)

As in the preceding parallel-parent proof, collisions with other current-birth bridge targets cost only `O(W_t/t^2+1/t^2)`: the capped bridge probability of any prescribed old vertex is `O(1/t)`, there are only fixed `m` current labels, and the historical ticket multiplier is bounded by one.

Thus the connected shadow satisfies

`E[Delta W_t|F_t]
 >= b10 W_t/t
    -C W_t^2/t^2
    -C W_tZ_t/t^2
    -C W_tN_t^rep/t^2
    -C W_t/t^2
    -C/t`,                                                        (3.6)

with `b10` from (P.1).

Since `a>0`, `pi>0`, and `S>0`,

`b10-b9
 =a pi^3 S/A^2
 >0`.                                                             (3.7)

**B15 outcome:** succeeded. Distinguishing historical parents from generic outside vertices yields a strict source-metric improvement without adding a generation to the exploration.

---

## 4. B4 — close the one-generation strengthening completely before recursing deeper

A larger two-generation ancestral cascade is tempting, but it introduces a new supply problem: after capturing a parent, one must control how often its own parents have already entered the shadow. Rather than leave that gap implicit, this run closes the one-generation incidence strengthening for the full parameter range.

The only issue not already handled by the preceding proof is whether the stronger ticket destroys the second-moment margin.

### 4.1 Upper first moment with the stronger ticket

Fix one historical label with strength `q`. On ticket success, its parent has frozen weight `w>=a+1`; during the current birth its final attractiveness is at most `w+m`. Hence, after historical retention and the new ticket,

`E[final captured attractiveness | parent v]
 <= pi * q(a+1)/w * (w+m)
 <= pi q(a+1+m)
 =pi q(A+1)`.                                                      (4.1)

Combining this with the same designated gate and capped-bridge upper bounds as before gives the historical-label upper contribution

`[2q(A+1)pi^3/A] W_t/t
 +O(W_t/t^2)+O(1/t)`.                                             (4.2)

Summing ticket strengths, define

`kappa_10:=2(A+1)pi^3 S/A`.                                      (4.3)

Thus the total upper drift coefficient is

`U_10:=b_U+kappa_10`.                                              (4.4)

We now prove uniformly that `U_10<1/2`.

### 4.2 The old deliberately reserved margin absorbs the `+1`

Because `a+m=A`, the preceding ticket budget was

`kappa_P:=2(a+m)pi^3S/A=2pi^3S`.                                 (4.5)

Its two stages were

`kappa_1=2vartheta pi^3`,

`kappa_F=2(m-1)lambda pi^3`,

so `kappa_P=kappa_1+kappa_F`.

By the definitions of `vartheta` and `lambda`,

`kappa_1<=d_*/2`,                                                 (4.6)

and with `d_7=d_*-kappa_1`,

`kappa_F<=d_7/2`.                                                  (4.7)

Therefore the old unused margin after both historical stages is

`M_old:=1/2-(b_U+kappa_P)
      =d_7-kappa_F
      >=d_7/2
      >=d_*/4`.                                                    (4.8)

The stronger `a+1` ticket increases the upper coefficient by exactly

`Delta_U:=kappa_10-kappa_P
        =2pi^3S/A
        =kappa_P/A`.                                               (4.9)

From (4.8), `kappa_P<=3d_*/4`. Since `m>=2`, `delta>0`,

`A=2m+delta>4`.

Hence

`Delta_U
 <=3d_*/(4A)
 <3d_*/16
 <d_*/4
 <=M_old`.                                                        (4.10)

So

`U_10=b_U+kappa_P+Delta_U<1/2`.                                  (4.11)

This is a strict all-parameter inequality; no numerical sampling is used.

### 4.3 Square jump and bootstrap

The square-jump argument from the preceding parallel-parent theorem is unchanged up to constants. Under the new ticket, for a parent of weight `w>=a+1`,

`[q(a+1)/w](w+m)^2 <= C(w+m)`,                                   (4.12)

with `C=C(m,delta)`. Summing historical parent incidences is therefore again controlled by `V_t`, and

`E[(Delta W_t)^2|F_t]<=C(1+V_t/t)`.                              (4.13)

Together with (4.11) and `E V_t=O(t)`, the standard recurrence gives

`E W_t^2=O(t)`.                                                    (4.14)

Taking expectations in (3.6), using (1.2)--(1.3), (4.14), and the deterministic bound `W_t<=Ct`, yields

`mu_{t+1}
 >=[1+b10/t-C/t^2]mu_t
   -C/t-Ct^(h-1)-C log(t)/t`,                                    (4.15)

where `mu_t:=E W_t`.

The inherited gate-only seed has exponent

`b1:=[m+a(1-(1-pi)^m)]/A>h`.                                     (4.16)

Divide (4.15) by the comparison product `Theta(t^b10)`. After a deterministic start time `T`, the normalized negative tails are

`O(T^-b10)`, `O(T^(h-b10))`, and `O(T^-b10 log T)`,               (4.17)

while the positive seed is `Omega(T^(b1-b10))`. Since `b1>h` and `b1>0`, one sufficiently large fixed `T` makes the seed dominate all three tails. Therefore

`E W_n>=c n^b10`.                                                  (4.18)

Future retained gate activations imply `E|Q_n|>=c'n^b10`; `Q_n` lies in one true percolation component. Thus

`gamma_E>=b10`.                                                    (4.19)

Finally, the historical lower coefficient is strictly below its upper counterpart:

`eta_10/kappa_10
 =[a(a+1)]/[2A(A+1)]<1/2`,                            (4.20)

and `b6<b_U`, so (4.11) also implies `b10<1/2`.

**B4 outcome:** succeeded. The full one-generation strengthening closes with the same second-moment architecture; the deeper-ancestry route remains a separate future method rather than an unproved step hidden in this theorem.

---

## 5. Exact before/after source metric

Before this run:

`gamma_E>=b9
 =b6+a^2pi^3S/A^2`.

After this run:

`gamma_E>=b10
 =b6+a(a+1)pi^3S/A^2`,

with

`b10-b9=a pi^3S/A^2>0`.

Thus the source-relevant metric moves strictly.

For orientation only, not as part of the proof, at `m=2`, `delta=1`, the previously defined ticket strengths equal one, so `S=2`, and

`pi_c≈0.04587585476806849`,

`b9≈0.4593297298598153`,

`b10≈0.4593529018720591`.

No simulation or finite-size fit is used.

---

## 6. What this still does not prove

The source target remains open. This proposition does not establish:

- `gamma_E=1/2`;
- any matching upper bound for `|C_max|`;
- the expected `sqrt(n)/log n` critical size scale;
- a `(log n)^(-2)` critical window for the fixed-outdegree sequential model;
- tightness or a component scaling-limit law;
- a transfer theorem from the independently attached-edge growing-graph model.

The most immediate mathematically new continuation suggested by this proof is to exploit the same incidence floor recursively: a captured historical parent has its own historical parents, but a second-generation theorem needs a new quantitative supply lemma controlling the mass of parents whose own ancestry already intersects the shadow. That is the exact missing lemma for a genuine depth-two cascade; it is not assumed here.
