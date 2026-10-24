# HARD7-03 idea before code — exact target-domination order cones

New route before any checker: the previous triple-slack correction only counted small sufficient events that force one layer-two endpoint to dominate all predecessors. Replace those sufficient subevents by the **full target-domination event** required for the same max-plus collapse.

For the edge correction `d=2`, the previous event `{A_1>=A_0, B_2>=B_1}` is only sufficient for `Y_2>=Y_1`. The exact useful event is simply `Y_2>=Y_1`. For `d=1`, the exact useful event is `Y_1>=max(Y_{-1},Y_0,Y_2)`. For `d=0`, it is `Y_0>=max(Y_{-2},Y_{-1},Y_1,Y_2)`.

Conditional on the first-layer `A` variables, every `Y_j` is a shifted exponential `u_j+B_j`. For a target `i`, the weighted target-max probability has the exact inclusion-exclusion formula

`E[e^{theta Y_i} 1{Y_i=max_j Y_j} | u] = e^{u_i} sum_{S subset competitors} (-1)^|S| e^{sum_{j in S}u_j} e^{-(1-theta+|S|)M}/(1-theta+|S|)`,

where `M=max_j u_j`.

The remaining `A`-integral can be split into the six ordering cones of `(A_{-1},A_0,A_1)`. On each cone all `u_j` and `M` are one of the ordered coordinates `x_1<=x_2<=x_3`, so every term is an elementary rational integral. This should strictly enlarge every old domination correction while remaining exact at rational `theta`.

Methods: **B8** (discretize the continuous first layer into six order cones), **B18** (rewrite the max-plus correlation as a shifted-exponential order-statistic problem), **B25** (count the target-max event twice: by the max-plus event and by inclusion-exclusion over competitor CDFs).
