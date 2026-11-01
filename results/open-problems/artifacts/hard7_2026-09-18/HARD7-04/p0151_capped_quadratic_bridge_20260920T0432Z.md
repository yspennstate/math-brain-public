# P0151 analytic artifact — capped-quadratic bridge amplification

This is a self-derived analytic proof artifact for `HARD7-04`. It concerns the exact sequential fixed-outdegree affine preferential-attachment model already frozen in `operations/claims/P0151.md`. It is **not** a finite certificate, does **not** identify the full critical window, and has not received the two independent audits required for source closure.

## Proposition

Fix an integer `m>=2` and `delta>0`. Consider Ray/Hazra--van der Hofstad--Ray model (d): each new vertex has exactly `m` sequential edges to older vertices, a current old vertex `u` is selected with probability proportional to `d_u+delta`, within-birth degree updates are included, self-loops are excluded after the finite initial graph, and after graph generation every edge is retained independently with probability `pi`.

Put

`a:=m+delta`, `A:=2m+delta=a+m`,

and at the exact bond-percolation threshold

`pi=pi_c:=delta/[2( m a + sqrt(m(m-1)a(a+1)) )]`.

Let `C_max(n,pi_c)` be the largest percolation component and

`gamma_E:=liminf_{n->infinity} log E|C_max(n,pi_c)| / log n`.

The preceding HARD7-04 theorem gives

`gamma_E>=b5`,

where

`b2:=m(1+a pi_c)/A`,

`b5:=b2+m(m-1)pi_c^2 a/A`.

Define

`eta_*:=m(m-1)pi_c^2`,

`b6:=b2+eta_*`.                                                   (P.1)

Then

`gamma_E>=b6>b5`,                                                 (P.2)

and in fact

`b6<1/2`.                                                         (P.3)

The improvement comes from replacing the previous constant bridge thinning `a/w` by a bounded, degree-sensitive acceptance profile

`c(w)/w`,  where  `c(w):=min(w,2A)`.                              (P.4)

The cap keeps the square-increment argument finite while the quadratic lower envelope

`w c(w)>=2A w-A^2`                                                (P.5)

recovers more of the outside attractiveness than the constant-thinning proof.

---

## 1. Deterministic denominators and two global budgets

For an old vertex `u` at completed time `t`, write

`w_u(t):=d_u(t)+delta`.

There is a fixed `K<infinity`, depending only on the finite initial graph and `(m,delta)`, such that every denominator used by the `j`th edge of birth `t+1` satisfies

`At-K <= D_{t,j} <= At+K`                                       (1.1)

for all large `t` and all `j=1,...,m`. The total attractiveness is deterministic up to the same finite offset:

`T_t:=sum_{u<=t} w_u(t)=At+O(1)`.                                (1.2)

The two initial vertices are excluded from bridge capture below because ordinary noninitial vertices are born with attractiveness at least `a`. Write

`Z_t:=w_1(t)+w_2(t)`,

`V_t:=sum_{u<=t} w_u(t)^2`.                                      (1.3)

We use the following two standard one-step estimates, included here for completeness.

### Lemma 1.1 — square-attractiveness budget

`E V_t=O(t)`.                                                     (1.4)

**Proof.** During one attachment edge, if the selected old vertex has current attractiveness `w`, the old-vertex square sum rises by

`(w+1)^2-w^2=2w+1`.

Conditioned on the current within-birth state, the selected vertex is size-biased by attractiveness, so the conditional mean of `w` is the current square-attractiveness sum divided by `D_{t,j}`. Iterating across the fixed `m` edges and then adding the new vertex's `a^2` contribution gives

`E[V_{t+1}|F_t] <= [1+2m/(At)+O(t^-2)] V_t + C`                  (1.5)

for a deterministic constant `C`. Since `2m/A<1` exactly because `delta>0`, choose `r` with `2m/A<r<1`; for large `t`,

`E V_{t+1} <= (1+r/t) E V_t+C`.

A linear induction gives `E V_t<=C' t`.  `square`

### Lemma 1.2 — finite-seed attractiveness

With

`h:=m/A<1/2`,

`E Z_t=O(t^h)`.                                                   (1.6)

**Proof.** The seed set receives no new vertices. Its attractiveness rises by one exactly when a new edge attaches to one of the two seed vertices. Sequential conditioning and (1.1) give

`E[Z_{t+1}|F_t] <= [1+m/(At)+O(t^-2)] Z_t`,

and product asymptotics yield (1.6).  `square`

---

## 2. B2 negation attack: why the uncapped bridge is not a uniform proof

The most aggressive variant would capture every retained outside target whenever the same birth has a gate into the current shadow. For a target of attractiveness `w`, the weighted bridge contribution then carries a factor `w^2`, and the square of a bridge jump naturally brings in cubic-weight sums (or equivalent mixed quantities).

The available all-`delta>0` global estimate is Lemma 1.1, namely `E sum w_u^2=O(t)`. It does **not** by itself close those cubic/mixed error terms uniformly over the full source range `delta>0`. Thus the no-thinning attack does not presently justify the second-moment bootstrap needed for an exponent theorem. This is a failure of this proof route, not a counterexample to the source problem.

The repair is to cap the accepted target numerator at a deterministic constant while choosing the cap by an extremal calculation rather than reverting to the previous constant numerator `a`.

---

## 3. B24 extremal bridge profile: the sharp quadratic envelope at the mean scale

For a parameter `s>0`, the profile

`c_s(w):=min(w,2s)`

has the pointwise inequality

`w c_s(w)>=2s w-s^2`                                              (3.1)

for every `w>=0`: if `w<=2s`, this is `(w-s)^2>=0`; if `w>=2s`, it is immediate.

Suppose only that at time `t` there are at most `t+O(1)` eligible outside vertices and their total attractiveness has leading order `At`. Summing (3.1) gives a leading deterministic lower coefficient

`2sA-s^2=A^2-(s-A)^2`.                                           (3.2)

Within this one-parameter capped-quadratic relaxation, the unique maximizing choice is therefore

`s=A`, hence `c(w)=min(w,2A)`,                                    (3.3)

and the leading lower coefficient becomes exactly `A^2`.

This is the only extremality claimed here: (3.2) optimizes this explicit capped-quadratic first-moment relaxation. No claim is made that (3.3) is optimal among all conceivable explorations.

---

## 4. The capped connected shadow

Start at one fixed ordinary noninitial vertex, say vertex `3`. Inductively construct a connected set `Q_t` contained in one true percolation component. Freeze at the start of birth `t+1`

`W_t:=sum_{u in Q_t} w_u(t)`.                                    (4.1)

A **gate** is a birth edge that is retained and whose target belongs to the frozen old set `Q_t`.

For an old vertex `u notin Q_t`, `u>=3`, define a **capped bridge certificate** on an edge targeting `u` by additionally accepting, independently, with probability

`c(w_u(current))/w_u(current)`,  `c(w):=min(w,2A)`.               (4.2)

The ratio is in `[0,1]`. Conditional on the complete earlier within-birth history, the target-weight factor cancels and

`P(B_j(u)=1 | history)=pi c(w_u(current))/D_{t,j}`.               (4.3)

If at least one gate occurs during the birth, add the new vertex to `Q` and also add every distinct capped-bridge target from that birth. Every added old bridge root is joined by a retained edge to the new vertex, while the new vertex is joined by a retained gate to `Q_t`; hence `Q_{t+1}` remains connected in the true percolated graph.

Let

- `H_t` be the number of the `m` birth edges targeting `Q_t`;
- `I_t` be the indicator that at least one gate occurs;
- `J_t` be the sum of the **final** time-`t+1` attractivenesses of the distinct newly captured old bridge roots.

Then exactly

`W_{t+1}-W_t=H_t+a I_t+J_t`.                                     (4.4)

The first term counts all degree increments received by old shadow vertices, the activated new vertex has final attractiveness `a`, and `J_t` adds the newly captured old roots.

---

## 5. B3 stronger lower drift: the capped bridge contributes `eta_*`

### 5.1 The outside quadratic mass

For each frozen eligible outside root use its completed-time weight `w_u:=w_u(t)`. By (3.1) with `s=A`,

`w_u c(w_u)>=2A w_u-A^2`.                                        (5.1)

Because `Q_t` excludes the two initial vertices,

`sum_{u notin Q_t,u>=3} w_u=T_t-Z_t-W_t`.                         (5.2)

There are at most `t+O(1)` eligible outside vertices. Therefore

`F_t:=sum_{u notin Q_t,u>=3} w_u c(w_u)`

satisfies

`F_t >= A^2 t-2A(W_t+Z_t)-C`.                                    (5.3)

Indeed, `2A T_t-A^2 t=A^2 t+O(1)` by (1.2).

### 5.2 Gate--bridge pairing

Let `G_t` be the number of gates. Define the frozen weighted accepted-bridge sum

`Y_t:=sum_{k=1}^m sum_{u notin Q_t,u>=3} B_k(u) w_u(t)`.           (5.4)

Let `D_t` be the frozen attractiveness mass of **distinct** captured bridge roots. Repeated accepted hits can only overcount `Y_t`; pointwise,

`D_t >= Y_t 1_{G_t>=1}-C_same`

`    >= G_t Y_t-Y_t binom(G_t,2)-C_same`,                         (5.5)

where

`C_same:=sum_{k<ell} sum_u B_k(u)B_ell(u) w_u(t)`.                (5.6)

The second inequality uses `1_{G>=1}>=G-binom(G,2)` for every nonnegative integer `G`.

For every ordered pair of distinct edge labels `j!=k` and every eligible outside `u`, sequential conditioning, monotonicity of `c`, (1.1), and (4.3) give

`E[ 1_{gate j} B_k(u) w_u(t) | F_t ]
 >= pi^2 W_t w_u(t)c(w_u(t))/(At+K)^2`.                           (5.7)

Summing over `m(m-1)` ordered pairs and using (5.3),

`E[G_tY_t|F_t]
 >= m(m-1)pi^2 W_t [A^2 t-2A(W_t+Z_t)-C]/(At+K)^2`

` >= eta_* W_t/t
    -C W_t^2/t^2
    -C W_t Z_t/t^2
    -C W_t/t^2`,                                                   (5.8)

where

`eta_*:=m(m-1)pi^2`.                                               (5.9)

The two overcount corrections are lower order. First, because `c<=2A`, two accepted bridge hits on the same prescribed old root have conditional probability `O(t^-2)`; hence

`E[C_same|F_t] <= C t^-2 sum_u w_u(t)=O(t^-1)`.                   (5.10)

Second, every nonzero monomial in `Y_t binom(G_t,2)` contains one accepted outside bridge and two distinct gate labels. Each gate probability is at most `C(W_t+m)/t`, while the accepted bridge probability to a prescribed root is at most `C/t`. Summing the frozen reward over old roots gives `O(t)`, so

`E[Y_t binom(G_t,2)|F_t] <= C(W_t^2+1)/t^2`.                      (5.11)

Since final captured attractiveness dominates frozen captured attractiveness, `J_t>=D_t`. Combining (5.5)--(5.11),

`E[J_t|F_t]
 >= eta_* W_t/t
    -C W_t^2/t^2
    -C W_t Z_t/t^2
    -C W_t/t^2
    -C/t`.                                                         (5.12)

### 5.3 Add the ordinary target-hit and activation drift

The ordinary two terms in (4.4) satisfy

`E[H_t|F_t] >= m W_t/(At+K)`,                                     (5.13)

and Bonferroni over retained shadow hits gives

`E[I_t|F_t]
 >= m pi W_t/(At+K)-C(W_t^2+1)/t^2`.                              (5.14)

Thus, with

`b2:=m(1+a pi)/A`,

`b_*:=b2+eta_*`,                                                   (5.15)

we obtain

`E[W_{t+1}-W_t|F_t]
 >= b_* W_t/t
    -C W_t^2/t^2
    -C W_t Z_t/t^2
    -C W_t/t^2
    -C/t`.                                                         (5.16)

At `pi=pi_c`, `b_*=b6` from (P.1).

---

## 6. The cap is strong enough for the second-moment bootstrap

The lower drift is useful only if large shadow states do not make its quadratic error first order. We now prove `E W_t^2=O(t)` for the **new** capped process.

### 6.1 Upper first moment of a bridge jump

Using `1_{G>=1}<=G`, dropping distinctness, `c<=2A`, and the fact that a bridge root gains at most `m` during one birth,

`J_t
 <= G_t sum_{k,u notin Q_t,u>=3} B_k(u)(w_u(t)+m)`.              (6.1)

For a gate label and a distinct bridge label, an upper sequential-conditioning bound gives a factor

`[pi(W_t+m)/(At-K)] [2A pi/(At-K)]`.

Also

`sum_{u<=t}(w_u(t)+m) <= (A+m)t+O(1)`.                            (6.2)

Therefore

`E[J_t|F_t]
 <= [eta_U/t+O(t^-2)]W_t+C/t`,                                   (6.3)

where

`eta_U:=2m(m-1)pi^2 (A+m)/A`.                                    (6.4)

The ordinary terms have

`E[H_t+aI_t|F_t]
 <= [b2/t+O(t^-2)]W_t+C/t`.                                      (6.5)

Hence

`E[W_{t+1}-W_t|F_t]
 <= [b_U/t+O(t^-2)]W_t+C/t`,                                     (6.6)

with

`b_U:=b2+eta_U`.                                                   (6.7)

### 6.2 Exact check that `b_U<1/2` at `pi_c`

Put

`r0:=sqrt(m(m-1)(a+1)/a)`,

`x:=a pi_c=(a-m)/[2(m+r0)]`.                                      (6.8)

A direct rearrangement gives

`1/2-b2=x r0/A`.                                                   (6.9)

Thus `b_U<1/2` is equivalent to

`2m(m-1)pi_c(A+m)<a r0`.                                         (6.10)

After substituting `pi_c=(a-m)/[2a(m+r0)]`, (6.10) is

`m(m-1)(a-m)(A+m) < a^2 r0(m+r0)`.                               (6.11)

Using `r0^2=m(m-1)(a+1)/a`, subtract from the left the `a^2 r0^2` part of the right. It remains enough to prove

`m(m-1)[a(m-1)-2m^2] < a^2 m r0`.                                (6.12)

If the bracket is nonpositive, this is immediate. If it is positive, then it is strictly smaller than `a(m-1)`, so the left side is strictly smaller than

`ma(m-1)^2`.

But

`(m-1)^2 < a r0`,                                                  (6.13)

because `a>m`, `r0>sqrt(m(m-1))`, and

`m sqrt(m(m-1))>(m-1)^2` for every `m>=2`. Multiplying (6.13) by `am` proves (6.12), hence

`b_U<1/2`.                                                         (6.14)

In particular `b6<b_U<1/2`, proving (P.3).

### 6.3 Square jump bound

Dropping the gate requirement and distinctness gives

`J_t <= sum_{k,u} B_k(u)(w_u(t)+m)`.

At most `m` bridge labels occur, so Cauchy yields

`J_t^2 <= m sum_{k,u} B_k(u)(w_u(t)+m)^2`.                         (6.15)

Since every prescribed accepted-bridge probability is at most `C/t`,

`E[J_t^2|F_t]
 <= C [V_t+t]/t`.                                                  (6.16)

The term `H_t+aI_t` is uniformly bounded. Taking total expectations, using Lemma 1.1, and squaring (4.4) together with (6.6) gives, for `Y_t:=E W_t^2`,

`Y_{t+1}
 <= [1+2b_U/t+O(t^-2)]Y_t+C`.                                    (6.17)

Because `2b_U<1`, a linear induction gives

`E W_t^2=O(t)`.                                                    (6.18)

---

## 7. Bootstrap the mean to exponent `b6`

Let `mu_t:=E W_t`. From (5.16), Lemmas 1.2 and (6.18), and the deterministic bound `W_t<=Ct`,

`mu_{t+1}
 >= [1+b6/t-C/t^2]mu_t-C/t-C t^{h-1}`,                           (7.1)

where `h=m/A`.

We need a positive polynomial seed with exponent strictly larger than `h`. Such a seed is available from the same process without using any bridge term. Let

`q(pi):=1-(1-pi)^m`,

`b1:=[m+a q(pi)]/A`.                                               (7.2)

For `0<=y<=1`, concavity of `f(y)=1-(1-pi y)^m` gives `f(y)>=q(pi)y`. Conditional on `F_t`, every birth-edge gate probability after conditioning on no earlier gate is at least `pi W_t/(At+K)`. Therefore, ignoring all bridges,

`E[W_{t+1}-W_t|F_t]
 >= [m+a q(pi)]W_t/(At+K)`.                                      (7.3)

Product iteration yields

`mu_t>=c t^{b1}`                                                   (7.4)

for all sufficiently large `t`. Since `q(pi)>0`,

`b1>h`.                                                            (7.5)

Now let `G_t` be a positive comparison product satisfying

`G_{t+1}=G_t[1+b6/t-C/t^2]`                                      (7.6)

after a sufficiently large deterministic start time. Then

`G_t=Theta(t^{b6})`.                                               (7.7)

Divide (7.1) by `G_{t+1}`. The normalized tail error from `C t^{h-1}` after a start time `T` is `O(T^{h-b6})`; the normalized `C/t` tail is `O(T^{-b6})`. By (7.4), the normalized seed at time `T` is at least a constant times

`T^{b1-b6}`.

Because `b1>h`, that seed dominates both normalized error tails for one fixed sufficiently large `T`. Iterating (7.1) from that `T` therefore gives

`mu_n>=c_T n^{b6}`                                                (7.8)

for all `n>=T`.

---

## 8. Convert attractiveness growth to component-size growth

Let `N_t:=|Q_t|`. Every gate activation adds the new vertex, while bridge captures can only add more vertices, so

`N_{t+1}-N_t>=I_t`.                                               (8.1)

Again by the concavity chord for `f(y)=1-(1-pi y)^m`,

`E[I_t|F_t]
 >= q(pi) W_t/(At+K)`.                                            (8.2)

At `pi=pi_c`, (7.8) and (8.2) imply

`E[N_{t+1}-N_t]>=c t^{b6-1}`.

Summing,

`E N_n>=c' n^{b6}`.                                               (8.3)

By construction `Q_n` lies inside one true percolation component, hence

`E|C_max(n,pi_c)|>=E N_n>=c'n^{b6}`.

Therefore

`gamma_E>=b6`.                                                     (8.4)

This proves the first inequality in (P.2).

Finally,

`b6-b5
 =m(m-1)pi_c^2 [1-a/A]
 =m^2(m-1)pi_c^2/A
 >0`,                                                              (8.5)

since `A-a=m`. Thus `b6>b5`, completing (P.2).

---

## 9. Scope and remaining source gap

What is proved here is the strict source-relevant lower-bound improvement

`gamma_E >= b6
 = m(1+(m+delta)pi_c)/(2m+delta)+m(m-1)pi_c^2`.

It is a theorem for the exact fixed-outdegree sequential model under the frozen assumptions `m>=2`, `delta>0`, at the exact threshold `pi_c`.

It does **not** prove any of the following:

- `gamma_E=1/2`;
- a matching upper bound for the largest critical component;
- `|C_max|` of order `sqrt(n)/log n`;
- a `(log n)^(-2)` finite-size critical window;
- tightness or a scaling-limit law;
- transfer of the independently attached-edge growing-graph theorem to this sequential fixed-`m` model.

The remaining conceptual gap is still a finite-population/spectral transfer. The preceding HARD7-04 run proved an exact `L^-2` spectral deficit for the killed critical Pólya-point-tree operator after the `x^{-1/2}` Doob transform. The present run moves the finite-graph expected-size exponent by a different, capped bridge mechanism, but it does not yet couple the finite sequential exploration sharply enough to turn that operator law into a full critical-window theorem.

For orientation only, not as proof, at `m=2`, `delta=1`:

`pi_c≈0.0458758547681`,

`b2≈0.455051025722`,

`b5≈0.457576538583`,

`b6≈0.459260213823`.

No simulation or finite-size fit is used in any step above.
