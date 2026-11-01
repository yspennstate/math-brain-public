Independent C0023 renormalisation obstruction, 2026-10-10. Derived after reading only w420's STATUS.md, before its proof.

Claim. For every integer d>=1 and every epsilon>0 there is a stationary site field on Z^d, determined by independent local Bernoulli seeds, such that (i) sites at l-infinity distance greater than 2(R+1) have independent underlying determining sets, (ii) each site is good with probability at least 1-epsilon, and (iii) every nearest-neighbour good component is finite. The radius R depends on epsilon. This does not contradict domination theorems with a fixed dependence range.

Construction. Mark each site s independently as a seed with probability q in (0,1). For v, look only at seeds in B_R(v)={s:||s-v||_infinity<=R}. If none exist set L(v)=bottom. Otherwise let L(v) be a nearest seed in l-infinity distance, resolving ties by lexicographic order of the seed coordinates. This tie rule is preserved by translation. Declare v good iff L(v) is not bottom and L(u)=L(v) for every nearest neighbour u of v.

Finite components. Adjacent good vertices have the same seed label. Along any good path the label is constant, say s. Every vertex with label s lies in B_R(s). Thus a good component has at most (2R+1)^d vertices, for EVERY seed configuration. No infinite-volume probabilistic limit is used in this conclusion.

Dependence and stationarity. The good indicator at v uses only seeds in B_{R+1}(v). The determining sets for two collections of sites separated by l-infinity distance greater than 2(R+1) are disjoint; independence of the seeds gives independence of the collections of indicators. Translation preserves distances and lexicographic comparisons, so the indicator field is stationary. This is finite dependence, not independence of adjacent indicators.

High density. Write b_r=(2r+1)^d for r>=0 and b_{-1}=0, and s_r=b_r-b_{r-1}. If the nearest seed to v has distance r<=R-1 and it is the only seed in B_{r+2}(v), all neighbours of v select that same seed: its distance from each neighbour is at most r+1, while every other seed has distance at least r+2 from that neighbour. Hence v is good.

Consequently
P(v is bad) <= (1-q)^(b_{R-1})
  + q^2 sum_{r=0}^{R-1} s_r (b_{r+2}-b_{r-1}) (1-q)^(b_{r-1}).                 (1)

For the second term, if the nearest seed is at radius r and uniqueness through radius r+2 fails, choose an ordered pair of distinct seeds, the first in the radius-r shell and the second in B_{r+2}\B_{r-1}. There are at most s_r(b_{r+2}-b_{r-1}) such pairs. Requiring no seeds in B_{r-1} is independent of the two selected seeds; the union bound proves (1). Counting a few impossible pairs only enlarges this upper bound. No conditional probability products or independence of the pair-events are asserted.

For r>=1, b_{r-1}>=(r)^d, and for r>=0
s_r(b_{r+2}-b_{r-1}) <= C_d (r+1)^(2d-2),
where C_d=12 d^2 21^(d-1) is sufficient, including r=0. With m=2d-2,
sum_{r>=1} r^m exp(-q r^d)
 <= integral_1^infinity x^m exp(-q x^d/2^d) dx
 <= (2^(2d-1)/d) Gamma(2-1/d) q^(-(2-1/d)).
The first inequality follows pointwise on each [r,r+1], since x>=r and x<=2r. Also (r+1)^m<=2^m r^m for r>=1. Since q^2<=q^(1/d) for 0<q<=1, (1) gives
P(v is bad) <= exp(-q (2R-1)^d) + K_d q^(1/d),                            (2)
where K_d=C_d[1+2^(4d-3) Gamma(2-1/d)/d].

Choose q so that K_d q^(1/d)<epsilon/2, then R>=1 large enough that exp(-q(2R-1)^d)<epsilon/2. This proves the claim. Alternatively q=R^(-d/2), R>=2, makes the bound tend to zero as R tends to infinity. The sharper explicit choice q=(log R)/R^d, R>=2, gives P(v bad)<=[1+K_d(log R)^(1/d)]/R, which also tends to zero while every good component remains finite.

Relevance. A block argument cannot infer percolation solely from errors tending to zero when its dependence range also grows. The missing estimate must place its error BELOW a percolating threshold for that same range. Ergodicity and uniqueness may give convergence of an anchor event with fixed inner box, but an outer radius chosen after the error tolerance can destroy the required dependence bound.

Scope. This field is correlated site percolation generated from iid seeds; it is not iid Bernoulli bond percolation and is not a counterexample to C0023. This is a rigorous candidate obstruction awaiting independent referee check, with no novelty claim.

NEXT: Referee the exact constants and determining radius; compare this obstruction with w420's finite-dependent criterion.
