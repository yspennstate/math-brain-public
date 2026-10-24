# P0151 analytic artifact — serial historical fallback across all birth edges

This is a self-derived analytic proof artifact for `HARD7-04`. It concerns the exact sequential fixed-outdegree affine preferential-attachment model frozen in `operations/claims/P0151.md`. It proves a strict further lower bound for the admitted expected critical-component exponent. It does **not** identify the full critical window, prove a matching upper bound, establish `sqrt(n)/log n` scaling, or close the source problem.

## Proposition

Fix an integer `m>=2` and `delta>0`. Put

`a:=m+delta`, `A:=2m+delta`,

and

`pi:=pi_c:=delta/[2( m a + sqrt(m(m-1)a(a+1)) )]`.

Run bond percolation with retention `pi` on Ray/Hazra--van der Hofstad--Ray sequential fixed-outdegree affine preferential-attachment model (d). Let `C_max(n,pi)` be the largest percolation component and

`gamma_E:=liminf_{n->infinity} log E|C_max(n,pi)| / log n`.

The preceding retrospective-parent theorem gives

`gamma_E>=b7`,

with a connected shadow `Q_t`, attractiveness

`W_t:=sum_{v in Q_t}(d_v(t)+delta)`,

and constants `b7`, `b_U'` satisfying

`b7<b_U'<1/2`.                                                   (P.1)

More precisely, if

`b2:=m(1+a pi)/A`,
`b6:=b2+m(m-1)pi^2`,
`b_U:=b2+2m(m-1)pi^2(A+m)/A`,
`d_*:=1/2-b_U`,
`vartheta:=min(1,d_* A/[4(a+m)pi^3])`,
`eta_R:=vartheta a^2 pi^3/A^2`,
`b7:=b6+eta_R`,
`kappa_1:=2 vartheta(a+m)pi^3/A`,
`b_U':=b_U+kappa_1`,

then the previous theorem proves (P.1), the lower/upper one-step drift bounds stated below, and a linear second-moment bound.

Set

`d_7:=1/2-b_U'>0`,                                                (P.2)

`lambda:=min(1, d_7 A/[4(m-1)(a+m)pi^3])`,                       (P.3)

and

`eta_F:= [a^2 pi^2/A^2] (1-pi vartheta)
         [1-(1-pi lambda)^(m-1)]`.                               (P.4)

Define

`b8:=b7+eta_F`.                                                   (P.5)

Then

`gamma_E>=b8>b7`,                                                 (P.6)

and in fact `b8<1/2`.

The new mechanism uses **all historical out-edges of a captured root, but serially**. The naive simultaneous version is not additive when historical parents repeat. Instead, after the already-used first historical certificate fails, labels `2,...,m` are tried in order and the procedure stops at the first raw certificate success. This removes duplicate-parent overcounting while retaining a strictly positive geometric fallback reward.

---

## 1. Inputs from the preceding connected-shadow theorem

Write

`w_v(t):=d_v(t)+delta`,
`V_t:=sum_{v<=t}w_v(t)^2`,
`Z_t:=w_1(t)+w_2(t)`,
`h:=m/A<1/2`.

There is a deterministic `K<infinity` such that all attachment denominators during birth `t+1` lie in `[At-K,At+K]` for all large `t`. The preceding construction uses the cap

`c(w):=min(w,2A)`                                                 (1.1)

and gives

`E V_t=O(t)`,                                                     (1.2)

`E Z_t=O(t^h)`.                                                   (1.3)

Let `Delta_7 W_t` denote the complete increment of the shadow under the preceding capped-bridge plus first historical-parent rule. Its established estimates are

`E[Delta_7 W_t | F_t]
 >= b7 W_t/t
    -C W_t^2/t^2
    -C W_t Z_t/t^2
    -C W_t/t^2
    -C/t`,                                                        (1.4)

`E[Delta_7 W_t | F_t]
 <= [b_U'/t+O(t^-2)]W_t+C/t`,                                    (1.5)

and

`E[(Delta_7 W_t)^2 | F_t] <= C(1+V_t/t)`.                        (1.6)

The shadow is connected in the actual percolated graph. The first historical label of any captured root `u` is used by the preceding rule with ticket strength `vartheta a/w_{p_1(u)}(t)`.

We augment this process monotonically; none of the old lower bounds is discarded.

---

## 2. Why the simultaneous all-parent idea is invalid

For an old ordinary vertex `u`, write

`p_j(u)<u`, `j=1,...,m`,

for the endpoint of historical out-edge label `j` from the birth of `u`.

It is tempting, once a current birth gates into `Q_t` and captures `u`, to expose all `m` historical edge bits and sum all successful parent rewards. That sum is **not** a valid lower bound for newly added attractiveness: the endpoints `p_j(u)` need not be distinct, and a parent may also be captured by a current bridge. The same actual vertex cannot be rewarded repeatedly. This is a genuine obstruction to an additive all-label estimate.

The repair is to impose a stopping rule: retain the preceding label-1 mechanism, and only if its *raw* historical certificate fails, try labels `2,...,m` in order; stop forever at the first raw success. Thus at most one fallback parent is proposed. Endpoint repetitions are harmless under this serial rule.

---

## 3. A deterministic supply of roots with all historical parents fresh

Define

`G_t^(m):={u in {3,...,t}: u notin Q_t,
           p_j(u)>=3 and p_j(u) notin Q_t for every j=1,...,m}`.   (3.1)

The requirement that **all** `m` historical parents avoid the shadow does not cost an extra factor `m` in the deterministic root count.

Indeed, roots already in `Q_t` number at most `W_t/a`. For a root outside `Q_t` that fails (3.1) because some historical edge ends in `Q_t`, choose one such bad edge. Distinct bad roots give distinct actual edge incidences, so the number of these roots is at most the total graph degree of `Q_t`, hence at most `W_t`. Likewise, roots failing because some historical edge ends at seed `1` or `2` number at most the total degree of the seeds, hence at most `Z_t`. Up to the fixed initial state,

`|G_t^(m)| >= t-W_t/a-W_t-Z_t-C`.                                (3.2)

Every ordinary vertex has `w_u(t)>=a`, and therefore `c(w_u(t))>=a`. Consequently

`S_t^(m):=sum_{u in G_t^(m)}c(w_u(t))
 >= a t-(1+a)W_t-aZ_t-C`.                                        (3.3)

This incidence double count is the key reason the all-label fallback remains macroscopic.

---

## 4. Freshness of every historical bit on a good root

### Lemma 4.1

Conditional on the exploration history up to completed time `t`, if `u in G_t^(m)`, then all `m` percolation-retention bits on historical edges `(u,p_j(u))`, `j=1,...,m`, may be kept unexposed and are mutually independent Bernoulli(`pi`) bits.

### Proof

Fix `j`. Since `p_j(u) notin Q_t` and the shadow is increasing, `p_j(u)` was outside the shadow at the birth of `u`. Thus historical edge `j` could not have been a gate then. Moreover `u notin Q_t`; hence **no** edge of the birth of `u` produced a retained gate into the then-current shadow, for otherwise the newborn `u` would have entered the shadow permanently. When there is no gate, retention bits on edges whose endpoints are outside the shadow are unnecessary for the shadow update and can be deferred. Later births do not require the old outgoing edge `(u,p_j(u))`. The preceding historical-parent rule only queries label `1`, and it does so only after `u` is captured; before the current capture all labels remain untouched. Independent bond percolation therefore leaves the `m` historical bits mutually independent Bernoulli(`pi`) variables at the moment the serial historical test begins. `square`

Parallel historical edges to the same endpoint cause no problem: they are distinct graph edges and have independent bond-retention bits.

---

## 5. Serial fallback rule

Use current birth-edge label `1` as a retained gate into frozen `Q_t` and current label `2` as a retained capped bridge to some `u in G_t^(m)`. Sequential attachment conditioning gives

`P(current 1 is a gate and current 2 is an accepted bridge to u | F_t)
 >= pi^2 W_t c(w_u(t))/(At+K)^2`.                                (5.1)

After the base current-birth processing, run the historical tests using weights frozen at time `t`.

1. Historical label `1` uses the preceding ticket strength `vartheta a/w_{p_1(u)}(t)`. A **raw label-1 success** means that its historical edge is retained and its independent ticket succeeds. If this raw success occurs, perform the preceding label-1 rule and do not run a fallback test.
2. If raw label `1` fails, inspect historical labels `j=2,...,m` serially. At label `j`, if its edge is retained, accept an independent fallback ticket with probability

   `lambda a/w_{p_j(u)}(t)`.                                     (5.2)

   Stop at the first raw fallback success. Its parent is the unique fallback candidate.
3. Add the candidate only if it was not already captured by the base current-birth bridges. If a raw success collides with such a base capture, add nothing and do not resume the serial search.

Let `F_t` (hereafter the random variable, not the sigma-field `mathcal F_t`) denote the **extra attractiveness actually added by this fallback layer only**.

The ticket in (5.2) is valid because every good parent has weight at least `a`.

---

## 6. Uniform fallback reward after one current gate-and-bridge event

A raw label-1 success has conditional probability

`pi vartheta a/w_{p_1(u)}(t) <= pi vartheta`,                     (6.1)

so the probability of reaching fallback label `2` is at least `1-pi vartheta`.

For each fallback label `j>=2`, conditional on reaching it, raw success probability is

`pi lambda a/w_{p_j(u)}(t) <= pi lambda`,                        (6.2)

and its reward, if successful and before base-collision deletion, is at least `w_{p_j(u)}(t)`. Thus its conditional expected raw reward is exactly bounded below by

`pi lambda a`.                                                    (6.3)

Because each new historical edge bit and each auxiliary ticket is fresh at the instant it is queried, the probability of reaching label `j` is at least

`(1-pi vartheta)(1-pi lambda)^(j-2)`.                            (6.4)

Summing (6.3)--(6.4) from `j=2` to `m`, the expected **raw fallback reward** conditional on the current gate-and-bridge event is at least

`R_F
 := pi lambda a(1-pi vartheta)
    sum_{k=0}^{m-2}(1-pi lambda)^k`

` = a(1-pi vartheta)[1-(1-pi lambda)^(m-1)]`.                    (6.5)

This quantity is strictly positive: `m>=2`, `lambda>0`, `pi>0`, and `pi vartheta<1`.

---

## 7. Lower drift and the new exponent coefficient

Multiply (5.1) by (6.5), sum over `u in G_t^(m)`, and use (3.3). Before deleting current-birth collisions,

`E[F_t^raw | F_t]
 >= [pi^2 W_t/(At+K)^2] S_t^(m) R_F`

` >= eta_F W_t/t
    -C W_t^2/t^2
    -C W_t Z_t/t^2
    -C W_t/t^2`,                                                  (7.1)

where exactly

`eta_F=[a^2 pi^2/A^2](1-pi vartheta)
       [1-(1-pi lambda)^(m-1)]`.                                 (7.2)

A fallback parent lies outside `Q_t`; current edge `1` ends in `Q_t` and current edge `2` ends at the strictly younger root `u`, so neither can already capture that parent. Only current labels `3,...,m` can create a base collision. For any prescribed old parent, the probability that one such label is an accepted capped bridge is at most

`pi c(w)/(At-K) <= C/t`,                                         (7.3)

uniformly in the parent weight. There are only `m-2` labels. Conditional on the raw fallback candidate, (7.3) therefore gives

`E[F_t^raw-F_t | F_t] <= C W_t/t^2+C/t^2`.                      (7.4)

Hence

`E[F_t | F_t]
 >= eta_F W_t/t
    -C W_t^2/t^2
    -C W_t Z_t/t^2
    -C W_t/t^2
    -C/t`.                                                        (7.5)

Adding (7.5) to the preceding lower drift (1.4) gives

`E[Delta_8 W_t | F_t]
 >= b8 W_t/t
    -C W_t^2/t^2
    -C W_t Z_t/t^2
    -C W_t/t^2
    -C/t`,                                                        (7.6)

with `b8=b7+eta_F>b7`.

---

## 8. Upper drift keeps a strict half-exponent margin

For an upper bound, ignore the serial stopping conditions and sum the possible contribution of all fallback labels `2,...,m`.

The current label-1 gate probability is at most

`[pi/(At-K)](W_t+m)`.                                             (8.1)

The total probability that current label `2` is an accepted capped bridge is at most

`[pi/(At-K)]sum_{u<=t}c(w_u(t)) <= 2pi+O(t^-1)`.                 (8.2)

For a fallback historical parent of frozen weight `w>=a`, at most `m` current edges can raise its weight during the current birth. Historical retention and the ticket in (5.2) therefore have expected final reward at most

`pi [lambda a/w](w+m) <= pi lambda(a+m)`.                        (8.3)

Summing over `m-1` fallback labels yields

`E[F_t | F_t]
 <= [kappa_F/t+O(t^-2)]W_t+C/t`,                                 (8.4)

where

`kappa_F:=2(m-1)lambda(a+m)pi^3/A`.                              (8.5)

By (P.3),

`kappa_F<=d_7/2`.                                                 (8.6)

Thus the new upper coefficient

`b_U'':=b_U'+kappa_F
 <= b_U'+d_7/2
 = (b_U'+1/2)/2
 <1/2`.                                                           (8.7)

Also, by `1-(1-x)^(m-1)<=(m-1)x`,

`eta_F
 <= (m-1)lambda a^2 pi^3/A^2
 < 2(m-1)lambda(a+m)pi^3/A
 = kappa_F`,                                                      (8.8)

because `a^2<2A(a+m)`. Since the preceding theorem has `b7<b_U'`, (8.8) implies

`b8<b_U''<1/2`.                                                   (8.9)

---

## 9. Square-jump budget survives all fallback labels

The serial rule proposes at most one fallback parent. For an upper bound on its square, however, sum the mutually exclusive possible success-stage contributions over `j=2,...,m` and ignore the gate and reach restrictions.

For a fixed root `u` and historical label `j`, retention plus ticket gives squared reward at most a constant times

`[lambda a/w_{p_j(u)}](w_{p_j(u)}+m)^2
 <= C(w_{p_j(u)}+1)`.                                            (9.1)

The probability that current label `2` is an accepted capped bridge to this prescribed `u` is at most `C/t`, because `c<=2A`. Therefore

`E[F_t^2 | F_t]
 <= C/t [sum_{j=2}^m sum_{u=3}^t w_{p_j(u)}(t)+t]`.              (9.2)

Every selected historical edge `(u,p_j(u))` is an actual graph edge. The multiplicity with which a vertex `v` appears as such an endpoint, summed over `u` and `j=2,...,m`, is at most its graph degree `d_v(t)`. Hence

`sum_{j=2}^m sum_{u=3}^t w_{p_j(u)}(t)
 <= sum_{v<=t}d_v(t)w_v(t)
 <= sum_{v<=t}w_v(t)^2
 =V_t`.                                                           (9.3)

Combining (9.2)--(9.3),

`E[F_t^2 | F_t] <= C(1+V_t/t)`.                                 (9.4)

With (1.6) and `(x+y)^2<=2x^2+2y^2`, the complete new jump obeys

`E[(Delta_8 W_t)^2 | F_t] <= C(1+V_t/t)`.                       (9.5)

Using (1.2), (8.4), and the deterministic bound `W_t<=At+O(1)`, the standard square expansion gives

`E W_{t+1}^2
 <= [1+2b_U''/t+O(t^-2)] E W_t^2+C`.                          (9.6)

Since `2b_U''<1`, induction yields

`E W_t^2=O(t)`.                                                   (9.7)

---

## 10. Mean bootstrap and transfer to the largest component

Take expectations in (7.6). By (9.7), `W_t<=At+O(1)`, and (1.3),

`E[W_t^2]/t^2=O(t^-1)`,

`E[W_t Z_t]/t^2=O(t^{h-1})`.                                     (10.1)

Thus for `mu_t:=E W_t`,

`mu_{t+1}
 >= [1+b8/t-C/t^2]mu_t-C/t-Ct^{h-1}`.                           (10.2)

The augmented process contains the preceding process, so its old polynomial seed lower bound remains available. Moreover

`b8>b7>b6>b2>h`.                                                  (10.3)

Let

`P_{T,t}:=prod_{s=T}^{t-1}(1+b8/s-C/s^2)`.

For fixed sufficiently large `T`, `P_{T,t}=Theta((t/T)^b8)`. Divide (10.2) by `P_{T,t+1}` and sum. The normalized error series are dominated by

`sum_{s>=T}s^{-1-b8}`

and

`sum_{s>=T}s^{h-b8-1}`,                                          (10.4)

both convergent because `b8>h`. Choosing `T` large and using the inherited positive polynomial seed makes the normalized initial mass dominate the tails, giving

`E W_n>=c n^b8`.                                                  (10.5)

Finally, conditional on the completed shadow at time `t`, the first edge of the next newborn is a retained gate into `Q_t` with probability at least

`pi W_t/(At+K)`.                                                  (10.6)

Each such event contributes a new vertex to the connected shadow. Summing (10.6) and using (10.5),

`E|Q_n|>=c' sum_{t<=n} t^{b8-1}>=c''n^b8`.                       (10.7)

Since `Q_n` is contained in a single actual percolation component,

`E|C_max(n,pi_c)|>=E|Q_n|>=c''n^b8`.

Taking the lower logarithmic exponent proves

`gamma_E>=b8>b7`.

This proves the proposition. `square`

---

## 11. Scope and exact remaining obstruction

The gain in (P.4) is a certified asymptotic theorem for the frozen fixed-outdegree model, not simulation. It strengthens only the expected critical largest-component exponent lower bound. It still does **not** transfer the killed-Pólya-point-tree `L^-2` spectral deficit to the finite dependent exploration at `L~log n`, and it gives no matching critical upper bound or scaling law.

The finite-to-local obstruction remains precise: at the expected neighboring critical scale `sqrt(n)/log n`, repeated use of a common birth label is potentially of order `(log n)^-2`, the same order as the local killed-operator spectral loss. Any proof of the full window must compute or cancel that dependence correction rather than discard it as `o(1)`.
