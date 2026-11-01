# P0151 analytic artifact — all-gate distinct-bridge ticket lemma

This is an analytic proof artifact for HARD7-04. It is **not** a finite certificate and it does not close the source critical-window problem.

## Frozen model and notation

Fix the sequential fixed-outdegree affine preferential-attachment model `PA_n^(m,delta)(d)` with fixed `m>=2`, `delta>0`, and independent bond retention `pi`. Put

- `a := m+delta`,
- `A := 2m+delta`,
- at criticality
  `pi=pi_c := delta/[2(ma+s)]`, where `s:=sqrt(m(m-1)a(a+1))`.

Use the ticket-thinned connected exploration from the preceding HARD7-04 run. At the start of birth `t+1`, `Q_t` is a connected set contained in one true percolation component and each `u in Q_t` has frozen ticket mass `ell_u(t)` satisfying `0<=ell_u(t)<=d_u(t)+delta`. Let

`S_t := sum_{u in Q_t} ell_u(t)`, `N_t:=|Q_t|`.

Every admitted vertex carries at least base ticket mass `a`, so `N_t <= S_t/a + C_0`. Source-model attachment denominators satisfy `At-K <= D_{t,j} <= At+K` for a fixed `K` and all large `t`, uniformly in edge label `j=1,...,m`.

For each birth edge `j`, a **gate hit** means: the edge targets `u in Q_t`, its independent ticket-thinning uniform accepts with probability `ell_u(t)/(d_u+delta)` using the frozen ticket, and the percolation mark is retained. Thus, conditional on the past and on any previous outcomes in the birth,

`P(G_j=1 | birth history) = pi S_t/D_{t,j}`.

Fix `rho in (0,1)` and the recent block

`R_t(rho)={ceil((1-rho)t),...,t}`.

For `u in R_t(rho)\Q_t`, define an **external base-ticket bridge hit** on edge `j` by accepting a target `u` with auxiliary probability `a/(d_u+delta)` and requiring the edge retained. Because every old vertex has attractiveness at least `a`, this is a valid thinning. If `M_t:=|R_t(rho)\Q_t|`, then, conditional on arbitrary earlier outcomes,

`P(B_j=1 | birth history)=pi a M_t/D_{t,j}`.

Moreover for a specified `u in R_t(rho)\Q_t`,

`P(B_j(u)=1 | birth history)=pi a/D_{t,j}`.

The cancellation remains valid if the same `u` was hit earlier in the birth, because the thinning uses the updated current attractiveness in the denominator.

Let `G:=sum_j G_j`, `L:=sum_j B_j`. If `G>=1`, the new vertex is connected to `Q_t`; therefore every distinct target of a `B`-edge is also connected through that new vertex. Let `D` be the number of distinct `B`-targets and capture all of them, assigning each captured old vertex base ticket mass `a` exactly once. This preserves ticket domination. The birth increment is bounded deterministically by

`0 <= Delta_t:=S_{t+1}-S_t <= m + a + a(m-1)=:B_*`,

because at most `m-1` bridge targets can coexist with at least one gate edge.

## Exact combinatorial lower bound for all gates

Because a single edge cannot be both a gate and an outside bridge,

`GL = sum_{j != k} G_j B_k`.

For integers `G,L in {0,...,m}`,

`L 1_{G>=1} >= GL - m binom(G,2)`.

Indeed, for `G=0,1` this is equality; for `G>=2`,

`GL-L=(G-1)L <= m(G-1) <= m binom(G,2)`.

Let `C_same` be the number of unordered pairs of bridge-success edges that hit the same outside vertex. Since multiplicity `r` contributes `r-1` to `L-D` and `binom(r,2)>=r-1`,

`D >= L-C_same`.

Hence pointwise

`D 1_{G>=1} >= GL - m binom(G,2) - C_same`.                     (1)

Now condition on `F_t`. Set

`p_-:=pi S_t/(At+K)`, `p_+:=pi S_t/(At-K)`,
`q_-:=pi a M_t/(At+K)`.

For every ordered pair `j != k`, regardless of which label occurs first, the frozen ticket thinnings give

`P(G_j B_k | F_t) >= p_- q_-`.

Therefore

`E[GL|F_t] >= m(m-1)p_-q_-`.                                      (2)

Also

`E[binom(G,2)|F_t] <= binom(m,2) p_+^2 = O(S_t^2/t^2)`.           (3)

For bridge collisions, for each unordered edge pair and each fixed outside recent vertex,

`P(B_j(u)B_k(u)|F_t) <= (pi a)^2/(At-K)^2`.

Summing over at most `t` candidate vertices gives

`E[C_same|F_t] <= C/t`.                                           (4)

Since `|R_t(rho)| >= rho t-C` and `N_t<=S_t/a+C_0`,

`M_t >= rho t-N_t-C`.

Using `(x)_+>=x`, (1)--(4) imply

`E[D 1_{G>=1}|F_t]
 >= [m(m-1) pi^2 a rho/A^2] S_t/t
    - C S_t^2/t^2 - C S_t/t^2 - C/t`.                            (5)

After multiplying by the base ticket mass `a`, the bridge contribution has first-order coefficient

`eta_rho := m(m-1)a^2 pi^2 rho/A^2`.                              (6)

This is the all-gate gain. It replaces the preceding run's fixed-gate coefficient

`(a pi/A)[1-(1-rho a pi/A)^(m-1)]`.

## Upper drift and self-consistent second moment

The old-ticket hit count `K_t` and activation indicator `I_t` satisfy

`E[K_t|F_t] <= m S_t/(At-K)`,
`E[I_t|F_t] <= m pi S_t/(At-K)`.

For the capture term, `D 1_{G>=1} <= L 1_{G>=1} <= GL`, so the same ordered-pair sum gives

`E[D 1_{G>=1}|F_t]
 <= m(m-1) [pi S_t/(At-K)] [pi a t/(At-K)]`.                     (7)

Thus at `pi=pi_c`,

`E[Delta_t|F_t] <= [b4+O(1/t)] S_t/t`,                            (8)

where

`b2 := [m+a m pi_c]/A`,
`b4 := b2 + m(m-1)(a pi_c/A)^2`.                                  (9)

The crucial point is `b4<1/2`. To prove it exactly, put

`r:=s/a=sqrt(m(m-1)(a+1)/a)`, `x:=a pi_c=delta/[2(m+r)]`.

Then

`1/2-b4
 = [delta/2-mx-m(m-1)x^2/A]/A
 = x[r-m(m-1)x/A]/A`.                                             (10)

Since `x<delta/(2m)`,

`m(m-1)x/A < (m-1)delta/(2A) < (m-1)/2`,

while

`r>sqrt(m(m-1))>(m-1)/2`.

Therefore (10) is strictly positive.

With `Delta_t<=B_*`, (8) yields, for `Y_t=E S_t^2` and any `c` with `2b4<c<1`,

`Y_{t+1} <= (1+c/t)Y_t + C`

for all large `t`; induction gives

`E S_t^2=O(t)`.                                                     (11)

## Lower drift and exponent

Bonferroni for the `m` retained gate hits gives

`P(I_t=1|F_t) >= m pi S_t/(At+K)-C S_t^2/t^2`.

Together with the lower target-hit drift and (5), at `pi=pi_c`,

`E[Delta_t|F_t]
 >= [b_rho/t-C/t^2]S_t - C S_t^2/t^2 - C/t`,                     (12)

where

`b_rho := b2 + eta_rho`.

Taking expectations and using (11),

`mu_{t+1} >= [1+b_rho/t-C/t^2]mu_t-C/t`, `mu_t:=E S_t`.            (13)

A positive polynomial seed is available without bridges: the global chord

`1-(1-pi x)^m >= [1-(1-pi)^m]x`

gives `mu_t >= c t^{b1}` for

`b1=[m+a(1-(1-pi)^m)]/A>0`.

Let `H_t` solve `H_{t+1}=H_t[1+b_rho/t-C/t^2]`. Then `H_t=Theta(t^{b_rho})`. After division by `H_{t+1}`, the error tail in (13) is `O(T^{-b_rho})`, while the normalized seed at time `T` is `Omega(T^{b1-b_rho})`; their ratio is `Omega(T^{b1}) -> infinity`. Choosing one fixed large `T` closes the bootstrap and gives

`E S_n >= c_rho n^{b_rho}`.                                      (14)

Finally the ordinary activation probability still obeys the global chord lower bound

`E[I_t|F_t] >= q(pi) S_t/(At+K)`, `q(pi)=1-(1-pi)^m>0`.

Since every activation adds a new vertex to `Q`, summing this bound with (14) gives

`E|Q_n| >= c'_rho n^{b_rho}`.

Because `Q_n` lies in one true percolation component,

`gamma_E := liminf_{n->infinity} log E|C_max(n,pi_c)|/log n >= b_rho`.

This holds for every fixed `rho<1`; letting `rho↑1` yields

`gamma_E >= b4
 = [m+a m pi_c]/A + m(m-1)(a pi_c/A)^2`.                        (15)

## Strict movement over the previous HARD7-04 bound

Write `z:=a pi_c/A in (0,1)`. The preceding run proved

`b3=b2+z[1-(1-z)^(m-1)]`.

Since `1-(1-z)^(m-1) <= (m-1)z`,

`b3-b2 <= (m-1)z^2 < m(m-1)z^2=b4-b2`.

Thus `b4>b3` for every `m>=2`, `delta>0`.

The result remains PARTIAL: it is an expected-size lower exponent, not a matching upper bound, critical-window width, tightness statement, or scaling limit.