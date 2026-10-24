SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account02, slot B14, 2026-09-23T19:38:35Z.
attacking: Fisher-information localization without fragment normalization—prove exact convex/translation mixture homogeneity for the newest projected-information theorem, then test whether rough finite-fragment extremes can enter that class with a uniform information budget.

# Early substantive checkpoint

Programme: `QFORM-DENSITY-3EIG-20260922`. Full target remains OPEN.

Let the Fisher action of a nonnegative finite subdensity `rho` be

`J(rho)=integral_{rho>0} |rho'|^2/rho = 4 ||(sqrt rho)'||_2^2`.

For positive subdensities `rho_j`, pointwise Cauchy--Schwarz gives

`|sum_j rho_j'|^2/(sum_j rho_j) <= sum_j |rho_j'|^2/rho_j`,

hence

`J(sum_j rho_j) <= sum_j J(rho_j)`.

Also `J(m f)=m I(f)` and translations leave `J` invariant. Therefore if a probability marginal is decomposed as `f=sum_j m_j f_j`, then

`I(f) <= sum_j m_j I(f_j)`.

This is the exact full-mass homogeneity needed for positive translation mixtures: arbitrary countable remote translations of a fixed Fisher-regular kernel have no fragment-number, location, support-diameter, or moment tax. The aggregate marginal must be paid before any active-fragment normalization.

The scale obstruction is exact. Use the cap-one probability kernel

`g(x)=cos^2(pi x/2) 1_{[-1,1]}(x)`, `I(g)=pi^2`.

For arbitrary disjoint centers `a_1,...,a_N`, put

`eta_{j,N}(x)=g(N(x-a_j))`, `f_N=sum_{j=1}^N eta_{j,N}`.

Each `eta_{j,N}` has mass `1/N` and cap one. Thus `f_N` is a cap-one probability density. Because the supports are disjoint,

`J(eta_{j,N})=N pi^2`,

and hence exactly

`I(f_N)=N^2 pi^2`.

Taking, for example, `a_j=4^j` retains arbitrarily distant fragments while keeping the same calculation. For the exact target `A=I_3`, the projected Fisher budget is `J_E=3 pi^2 N^2`, so the cap-improved Fisher theorem gives the certificate

`||p_Q||_inf <= 3 D_3/4 + [pi sqrt(3D_3)/4] N`
`             = 11.6933312691... + 5.3714186617... N`,

where `D_3=6(4pi/3)^(2/3)`.

But the completed fixed-source Theorem A at `math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837`, `COUNTEREXAMPLE_SEARCH.md`, applies to the SAME `A=I_3` law and gives

`||p_Q||_inf <= 6 sqrt(pi)`

uniformly in `N` and all fragment locations. Thus Fisher regularity itself is not the missing rough-law closure mechanism: even smooth cap-one finite-fragment laws can have exact projected information growing like `N^2` while the true source-valid QFORM bound stays constant.

First unpaid implication: obtain a cap/product estimate for the signed score term that aggregates active fragments before the absolute Fisher norm, or force a whole-law volume/hub/pair/ridge certificate before any scale-normalized localization.
