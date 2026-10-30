SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet03, slot B06, 2026-09-23T17:19:37Z.
attacking: the ultra-thin near-rank-two survivor; convert low determinant-pair disjointness into a single physical row and column carrying a majority of the dominant two-dimensional singular planes, before any reciprocal-minor payment.

# Early calculation: pair-law intersection forces a single heavy vertex

Let mu be any probability law on two-element subsets of an arbitrary index set. Write alpha_i=P(i in S), m=max_i alpha_i, and delta=P(S cap S'=empty) for independent S,S'~mu.

Choose an edge {a,b} in the support whose disjoint mass C=P(S cap {a,b}=empty) is at most delta. Decompose

x=mu({a,b}), p_u=mu({a,u}), q_u=mu({b,u}),
A=sum_u p_u, B=sum_u q_u.

Then 1=x+A+B+C. Since alpha_a=x+A<=m and alpha_b=x+B<=m,

A,B >= 1-C-m.

The ordered disjoint pairs consisting of one a-star edge and one b-star edge alone contribute

2(AB-sum_u p_u q_u)

to delta. For every u, p_u+q_u<=alpha_u<=m, so

p_u q_u <= (p_u+q_u)^2/4 <= m(p_u+q_u)/4.

Hence

delta >= 2[(1-C-m)^2 - m(1-C)/4].                         (E1)

At d=1/256, if m<=3/5 and C<=delta<d, the right side is minimized by C=d and m=3/5 (both monotonicities have the required sign on this rectangle), where it equals

2[(255/256-3/5)^2-(3/5)(255/256)/4]
= d + 9049/819200 > d,

contradicting delta<d. Therefore

    delta<1/256  ==>  max_i alpha_i>3/5.                     (E2)

Application target for this run: in the r39 ultra-thin physical cross block N, apply (E2) separately to the determinant-squared row-pair and column-pair marginals. The next step is to use the fact that >99% of e_2(N^T N) comes from the first two singular directions to convert alpha_i>3/5 into >19/32 physical leverage in the dominant two-plane.

Status: early substantive calculation only; full proof and constants follow in REPORT.md. Full QFORM remains open.
