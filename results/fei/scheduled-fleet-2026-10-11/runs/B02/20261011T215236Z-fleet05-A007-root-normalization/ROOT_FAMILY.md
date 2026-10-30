# Shared conjunction with heterogeneous petals

Let C be r>=1 fresh fair coordinates, p=2^(-r), and A_r their positive conjunction. Let b_l be arbitrary nonzero indicators on a data cube, with rho_l=E b_l, and let B=OR_l b_l be nonconstant. Set g=2B-1 and F=2 A_r B-1. The actual overlapping gates are h_l=2 A_r b_l-1, with supports C union supp(b_l). Fix positive lambda_l with sum lambda_l<=1, independent of the sampled spectral set. All incidence constraints hold, and pi_l=p rho_l.

The new root-normalization conclusion applies even when the private gate supports overlap and g is an arbitrary Boolean seed: the extra cost of the common core, after retaining the negative normalization, is at most (log_2 e) I(F). This is a component theorem, not a full cost bound or a new FEI class.

An explicit heterogeneous test family takes b_l as conjunctions on pairwise disjoint blocks of widths w_l>=1. These gates overlap in the r core coordinates, with unbounded read m. Put Q=product_l(1-2^(-w_l)) and b=1-Q. A canonical forest has one root whenever the Fourier set meets C, and otherwise one root per touched private block. Its exact excess-root expectation is

    E K - Var(F) = 4 p^2 Q [sum_l 2^(-w_l) - (1-Q)].

Thus multiple-root cancellation is not exact for m>=2, but its remaining rarity cost is paid uniformly. A006 already handled r=1 and all w_l=1 using the complete posterior cost. This run extends the normalization mechanism to arbitrary r, heterogeneous petals, and arbitrary data events, while leaving the remaining costs explicitly unpaid.
