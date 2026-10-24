# P0151 analytic artifact — full-attractiveness bridge lower exponent

This is an analytic proof artifact for `HARD7-04`. It is **not** a finite certificate, does not identify the critical window, and does not close the source problem. The argument below is self-derived and has not received the two independent audits required for closure.

## Proposition

Fix the sequential fixed-outdegree affine preferential-attachment model `PA_n^(m,delta)(d)` of Hazra--van der Hofstad--Ray, with fixed integer `m>=2`, fixed `delta>0`, exactly `m` sequential out-edges per arriving vertex, no self-loops after the finite initial graph, and independent bond retention `pi`. Put

`a := m+delta`, `A := 2m+delta`.

At the exact threshold

`pi=pi_c := delta / [2( m a + sqrt(m(m-1)a(a+1)) )]`,

let `C_max(n,pi_c)` be the largest percolation component and

`gamma_E := liminf_{n->infinity} log E|C_max(n,pi_c)| / log n`.

Write

`b2 := [m + a m pi_c]/A`,

`eta_0 := m(m-1)(a pi_c/A)^2`,

`b4 := b2 + eta_0`,

so `b4` is the preceding HARD7-04 all-gate/base-ticket bound. Define instead

`eta_F := m(m-1) pi_c^2 a/A`,

`b5 := b2 + eta_F`.                                                (P.1)

Then

`gamma_E >= b5 > b4`.                                              (P.2)

Moreover `b5<1/2` for every `m>=2`, `delta>0`.

The mechanism is different from the preceding constant-base-ticket bridge argument: an old bridge root is admitted with its **full pre-birth attractiveness**, and the unbounded score increments are controlled by the global square-attractiveness budget of the preferential-attachment graph.

---

## 1. Deterministic denominators and global attractiveness quantities

For an old vertex `u` at time `t`, write

`w_u(t):=d_u(t)+delta`.

In model (d), the source denominator for the `j`th edge of vertex `t+1` is deterministic up to the fixed initial-graph offset. Hence there is a fixed `K<infinity` such that for all large `t` and all `j=1,...,m`,

`At-K <= D_{t,j} <= At+K`.                                        (1.1)

The total attractiveness is deterministic:

`T_t:=sum_{u<=t} w_u(t)=At+O(1)`.                                  (1.2)

The two initial vertices can have attractiveness below `a`, so bridge thinning below excludes them. Let

`Z_t:=w_1(t)+w_2(t)`                                               (1.3)

and let

`V_t:=sum_{u<=t} w_u(t)^2`.                                       (1.4)

Two elementary moment estimates will replace the bounded-increment argument used in the preceding base-ticket route.

### Lemma 1 (square-attractiveness budget)

`E V_t = O(t)`.                                                     (1.5)

**Proof.** During one attachment edge, if the selected old vertex currently has attractiveness `w`, then the old-vertex square sum rises by

`(w+1)^2-w^2=2w+1`.

Conditioned on the current within-birth state, the selected vertex has law proportional to its current attractiveness, so the conditional mean of `w` is the current old-vertex square sum divided by `D_{t,j}`. Iterating over the fixed `m` edges and finally adding the new vertex's square attractiveness `a^2` gives

`E[V_{t+1}|F_t]
 <= [1 + 2m/(At) + O(t^-2)] V_t + C`.                              (1.6)

Since `2m/A<1` exactly when `delta>0`, choose `c` with `2m/A<c<1`. For large `t`,

`E V_{t+1} <= (1+c/t) E V_t + C`,

and a one-line induction gives `E V_t<=C't`. `square`

### Lemma 2 (finite-seed attractiveness)

With

`h:=m/A<1/2`,

`E Z_t = O(t^h)`.                                                   (1.7)

**Proof.** The seed set receives no new vertices. During each new birth, its attractiveness rises by one exactly when an attachment chooses one of the two seed vertices. The same sequential conditioning as above gives

`E[Z_{t+1}|F_t]
 <= [1 + m/(At) + O(t^-2)] Z_t`,                                   (1.8)

and iteration yields `E Z_t=O(t^{m/A})`. `square`

---

## 2. The full-attractiveness connected shadow

Start at any fixed non-initial vertex, say `Q_3={3}`. Inductively, `Q_t` will be a connected vertex set inside one true percolation component.

At the start of birth `t+1`, freeze `Q_t` and set

`W_t:=sum_{u in Q_t} w_u(t)`.                                     (2.1)

During the `m` new attachment trials define a **gate** to be an edge that is retained by percolation and targets `Q_t`. If at least one gate occurs, add the new vertex `t+1` to `Q`.

For every non-initial old vertex `u notin Q_t`, define a **bridge certificate** on edge `j` as follows. If edge `j` targets `u`, independently accept it with probability

`a / w_u(current)`

and also require its percolation mark to be retained. This is a valid thinning because every non-initial vertex is born with degree `m`, hence has attractiveness at least `a` forever. Conditional on arbitrary earlier outcomes in the same birth,

`P(B_j(u)=1 | birth history)=pi a/D_{t,j}`.                        (2.2)

Thus bridge certificates are uniform over non-initial target labels after thinning, despite preferential attachment.

If at least one gate occurs, capture every distinct bridge-certificate target. Every such old vertex is connected to the new vertex by a retained edge, while the new vertex is connected to `Q_t` by a retained gate, so the enlarged set remains connected in the true percolated graph.

Let

- `H_t` be the number of current birth edges whose target lies in the frozen old set `Q_t`;
- `I_t` be the indicator that at least one gate occurs;
- `J_t` be the sum of the **final** attractivenesses at time `t+1` of the distinct captured old bridge roots.

Then the actual-attractiveness score satisfies the exact identity

`W_{t+1}-W_t = H_t + a I_t + J_t`.                                 (2.3)

Indeed, `H_t` counts all new degree increments received by old tracked vertices, the activated new vertex has final attractiveness `a`, and `J_t` adds the full final attractiveness of every newly captured old vertex.

The construction has no bounded-increment property: a captured old root can have large degree. Lemma 1 is what will replace bounded increments.

---

## 3. Base drift: the tangent coefficient remains available

Because the attractiveness of `Q_t` can only increase during the birth,

`m W_t/(At+K)
 <= E[H_t|F_t]
 <= m(W_t+m)/(At-K)`.                                              (3.1)

For gate activation, conditional on no earlier gate, the next trial is a gate with probability at least

`pi W_t/(At+K)`.

Hence

`P(I_t=1|F_t)
 >= 1-(1-pi W_t/(At+K))^m
 >= m pi W_t/(At+K) - C W_t^2/t^2`,                               (3.2)

where the last step is the second Bonferroni inequality. Conversely,

`P(I_t=1|F_t) <= m pi (W_t+m)/(At-K)`.                             (3.3)

Thus the ordinary target-hit plus activation part has the same first-order coefficient

`b2=[m+a m pi]/A`.                                                  (3.4)

At `pi=pi_c`, this is the preceding tangent coefficient.

---

## 4. B11 duality: full outside mass turns the bridge term into `W(T-W)`

The key change from the base-ticket argument is to keep the full frozen attractiveness of a captured old bridge root.

For bridge edge `k`, let its frozen bridge weight be `w_u(t)` when `B_k(u)=1`, and put

`Y_t:=sum_{k=1}^m sum_{u notin Q_t, u>=3} B_k(u) w_u(t)`.           (4.1)

Let `G_t` be the number of gate edges. For the distinct frozen captured mass `J_t^0` (the sum of `w_u(t)` over distinct captured roots), pointwise

`J_t^0
 >= Y_t 1_{G_t>=1} - C_same
 >= G_t Y_t - Y_t binom(G_t,2) - C_same`,                          (4.2)

where `C_same` is the weighted duplicate-target correction

`C_same:=sum_{k<ell} sum_u B_k(u)B_ell(u) w_u(t)`.                 (4.3)

The first inequality only removes repeated bridge hits on the same old root. The second uses

`1_{G>=1} >= G-binom(G,2)`

for every integer `G>=0`.

For every ordered pair of distinct edge labels `j!=k` and every eligible outside vertex `u`, sequential conditioning and (2.2) give

`P(G_j B_k(u)|F_t)
 >= [pi W_t/(At+K)] [pi a/(At+K)]`.                               (4.4)

Since `Q_t` never contains the two initial vertices (they are excluded as bridge roots and the process starts at vertex 3),

`sum_{u notin Q_t, u>=3} w_u(t)=T_t-Z_t-W_t`.                     (4.5)

Therefore

`E[G_tY_t|F_t]
 >= m(m-1) pi^2 a W_t (T_t-Z_t-W_t)/(At+K)^2`.                    (4.6)

The two correction terms are lower order. For the duplicate term, (2.2) gives

`E[C_same|F_t] <= C/t`,                                            (4.7)

because `sum_u w_u(t)<=T_t=O(t)`. For the multiple-gate term, every contributing monomial contains two gate labels and one distinct bridge label. Using the upper gate probability `pi(W_t+m)/(At-K)`, the exact bridge thinning (2.2), and again `sum_u w_u(t)=O(t)`,

`E[Y_t binom(G_t,2)|F_t]
 <= C (W_t^2+1)/t^2`.                                              (4.8)

Because final captured attractiveness dominates frozen captured attractiveness, `J_t>=J_t^0`. Combining (4.5)--(4.8) and `T_t=At+O(1)` yields

`E[J_t|F_t]
 >= eta_F W_t/t
    - C W_t^2/t^2
    - C W_t Z_t/t^2
    - C W_t/t^2
    - C/t`,                                                        (4.9)

where

`eta_F:=m(m-1) pi^2 a/A`.                                         (4.10)

This is the full-attractiveness bridge coefficient.

For comparison, the preceding base-ticket route obtained

`eta_0=m(m-1) a^2 pi^2/A^2`.                                      (4.11)

Thus

`eta_F/eta_0=A/a>1`                                                (4.12)

because `A-a=m>0`.

---

## 5. B28: unbounded bridge jumps still have an `L^2` closure

We need an upper drift coefficient below `1/2` and a bounded **mean square** increment, not a bounded pointwise increment.

A captured bridge root `u` has final attractiveness at most `w_u(t)+m`. If `G_t>=1`, every captured root came from some bridge certificate. Hence, by overcounting gates, bridge labels, and duplicate roots,

`J_t
 <= G_t sum_{k,u} B_k(u)(w_u(t)+m)`.                             (5.1)

Using the upper gate probability and (2.2),

`E[J_t|F_t]
 <= [eta_U/t+O(t^-2)] W_t + C/t`,                                 (5.2)

where

`eta_U:=m(m-1) pi^2 a(A+m)/A^2`.                                  (5.3)

Together with (3.1)--(3.3),

`E[W_{t+1}-W_t|F_t]
 <= [b_U/t+O(t^-2)] W_t + C/t`,                                   (5.4)

where

`b_U:=b2+eta_U`.                                                    (5.5)

At `pi=pi_c`, one has **strictly**

`b_U<1/2`.                                                         (5.6)

Here is an exact verification. Put

`r0:=sqrt(m(m-1)(a+1)/a)`,
`x:=a pi_c=delta/[2(m+r0)]`.

Then

`1/2-b2 = x r0/A`,                                                 (5.7)

and

`1/2-b_U
 = (x/A)[ r0 - m(m-1)x(A+m)/(aA) ]`.                            (5.8)

Since `x<delta/(2m)`, `delta/a<1`, and `(A+m)/A<3/2`,

`m(m-1)x(A+m)/(aA)
 < 3(m-1)/4
 < r0`.                                                            (5.9)

This proves (5.6).

Now control the square increment. By Cauchy over at most `m` bridge labels and then the same gate--bridge pair overcount,

`E[J_t^2|F_t]
 <= C (W_t+m)(V_t+t)/t^2.                                        (5.10)

Indeed, `sum_u(w_u(t)+m)^2 <= 2V_t+2m^2t`, while each contributing gate--bridge pair has probability at most a constant times `(W_t+m)/t^2`. Since `W_t<=T_t=O(t)`, Lemma 1 gives

`E J_t^2=O(1)`.                                                     (5.11)

The other two parts of the increment in (2.3) are uniformly bounded, so

`E(W_{t+1}-W_t)^2=O(1)`.                                           (5.12)

Let `Y_t:=E W_t^2`. Squaring (2.3), using (5.4), (5.12), and `W_t<=Ct`, gives

`Y_{t+1}
 <= [1+2b_U/t+O(t^-2)]Y_t + C`.                                   (5.13)

Because `2b_U<1`, choose `c` with `2b_U<c<1`; induction yields

`E W_t^2=O(t)`.                                                     (5.14)

This is the replacement for the bounded-increment second-moment argument. The high-degree bridge roots do not destroy the proof because the entire graph has only `O(t)` expected square attractiveness when `delta>0`.

---

## 6. Lower drift and bootstrap to `b5`

Combine the base lower drift (3.1)--(3.2) with (4.9). At `pi=pi_c`, with

`b5:=b2+eta_F`,                                                     (6.1)

we obtain

`E[W_{t+1}-W_t|F_t]
 >= [b5/t-C/t^2]W_t
    - C W_t^2/t^2
    - C W_t Z_t/t^2
    - C/t`.                                                        (6.2)

Let `mu_t:=E W_t`. From (5.14), Lemma 2, and the deterministic `W_t<=Ct`,

`E W_t^2/t^2=O(1/t)`,

`E[W_tZ_t]/t^2 <= C E Z_t/t = O(t^{h-1})`, `h=m/A`.               (6.3)

Hence

`mu_{t+1}
 >= [1+b5/t-C/t^2]mu_t - C t^{h-1}`.                              (6.4)

A positive polynomial seed is available without using any bridge term. Put

`q:=1-(1-pi_c)^m`,
`b1:=[m+a q]/A`.                                                    (6.5)

The concavity chord

`1-(1-pi_c y)^m >= q y`, `0<=y<=1`,                               (6.6)

combined with the target-hit drift gives directly

`mu_t>=c t^{b1}`                                                   (6.7)

for all large `t`. Note

`b1>h=m/A`.                                                        (6.8)

Let `R_t` solve

`R_{t+1}=R_t[1+b5/t-C/t^2]`.

Then `R_t=Theta(t^{b5})`. Divide (6.4) by `R_{t+1}`. The entire normalized error tail after time `T` is

`O(sum_{t>=T} t^{h-1-b5})=O(T^{h-b5})`,                            (6.9)

because `b5>h`. On the other hand, by (6.7), the normalized seed at time `T` is

`Omega(T^{b1-b5})`.                                                (6.10)

The ratio of (6.10) to (6.9) is `Omega(T^{b1-h}) -> infinity`. Choosing one fixed sufficiently large `T` and iterating therefore yields

`E W_n >= c n^{b5}`                                                (6.11)

for all large `n`.

---

## 7. Convert attractiveness growth to component-size growth

The same global chord (6.6) gives

`E[I_t|F_t] >= q W_t/(At+K)`.                                     (7.1)

Every activation adds a new vertex to `Q`, so (6.11) implies

`E|Q_n|
 >= c sum_{t<=n} t^{b5-1}
 >= c' n^{b5}`.                                                    (7.2)

By construction `Q_n` is contained in one true percolation component. Therefore

`E|C_max(n,pi_c)| >= E|Q_n| >= c'n^{b5}`,                          (7.3)

which proves `gamma_E>=b5`.

---

## 8. Strict movement and the remaining power gap

The preceding bound was

`b4=b2+m(m-1)a^2 pi_c^2/A^2`.

The new bridge coefficient is

`eta_F=m(m-1)pi_c^2 a/A
      = eta_0 (A/a)`.

Since `A/a>1`,

`b5>b4`                                                            (8.1)

for every `m>=2`, `delta>0`.

The new exponent is still strictly below `1/2`. With `r0,x` from (5.7),

`1/2-b5
 = (x/A)[r0-m(m-1)x/a]`.                                          (8.2)

Again `x<delta/(2m)` gives

`m(m-1)x/a < (m-1)delta/(2a) < (m-1)/2 < r0`,                     (8.3)

so (8.2) is positive.

For orientation only, not proof, at `m=2`, `delta=1`:

`pi_c ~= 0.04587585476806849`,
`b2 ~= 0.4550510257216822`,
`b4 ~= 0.4565663334381869`,
`b5 ~= 0.4575765385825233`.

Thus this route moves the frozen source-relevant lower exponent by about `0.00101020514` in that example, but it still does **not** prove the expected neighboring power `1/2`, the `sqrt(n)/log n` scale, the `(log n)^(-2)` critical window, tightness, or any scaling limit.

---

## 9. Why the tempting stronger unthinned route is not claimed

Without base thinning, a bridge target is size-biased. The first drift would then involve `sum w_u^2`, which looks stronger, but its `L^2` closure naturally exposes `sum w_u^3`. For the full source range `delta>0`, the degree law need not have a uniformly bounded third moment. The present proof therefore uses the uniformizing factor `a/w_u` deliberately: it gains the **full first attractiveness moment** while closing with only the square-attractiveness budget `E V_t=O(t)`.

This is a precise obstruction, not evidence that the unthinned route is impossible.