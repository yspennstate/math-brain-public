# Finite-temperature vacancy obstruction (C2)

This is a proved special case, pending independent review by w533. It is not a proof or disproof of P0309. The uniform bound below applies to the unpinned short-range grand-canonical Riesz specification, not automatically to long-range jellium or a canonical specification.

Let d >= 1, s > d, 0 < beta < infinity and mu in R. Put a = exp(beta*mu). Suppose P satisfies the grand-canonical DLR specification for V(x) = |x|^(-s). Conditional on the exterior eta of a bounded measurable region D, the partition function is

    Z_D(eta) = sum_{n>=0} (a^n/n!) integral_{D^n} exp[-beta H_D(y|eta)] dy,

where H_D is the sum of interior-interior and interior-exterior pair interactions, both nonnegative, and the empty configuration has H_D = 0. Thus

    1 <= Z_D(eta) <= sum_{n>=0} (a|D|)^n/n! = exp(a|D|).

The empty sector has weight exactly 1, hence

    P(N(D)=0 | exterior of D) = 1/Z_D(eta) >= exp(-a|D|).

This exterior-independent lower bound is valid for almost every exterior where the DLR equation holds. It needs no absolute convergence assertion beyond the specification's own existence, since nonnegative extended energies also obey the integrand upper bound.

Let D_1,...,D_m be pairwise disjoint fixed cells of volume at most v, and set p = exp(-a*v) > 0. For A_{m-1} = intersection_{j<m}{N(D_j)>=1}, its indicator is measurable with respect to the exterior sigma-field of D_m. The DLR bound and the tower property give

    P(A_{m-1} and N(D_m)>=1)
      = E[1_{A_{m-1}} P(N(D_m)>=1 | exterior D_m)]
      <= (1-p) P(A_{m-1}).

Induction yields

    P(N(D_j)>=1 for every j<=m) <= (1-p)^m.

For a countably infinite disjoint family of cells of uniformly bounded volume, continuity of probability for decreasing events gives probability zero that every cell is occupied. In particular, the event of exactly one point in each prescribed cell has probability zero. The product arises from a valid exterior conditioning and uniform bound, not independence.

## Boundary of the result

A crystalline *law* may have periodic, nonconstant intensity and still have vacancies. This result does not contradict that law. The vacancy bound goes to zero as beta*mu grows; it is positive for each fixed finite beta and mu. It says nothing about the zero-temperature limit taken before volume goes to infinity.

For long-range jellium, the negative point-background terms prevent H_D >= 0, and a renormalized specification must be supplied before reusing this argument. In a canonical kernel, the number of points in D may be fixed by the exterior; the empty sector need not be available. Neither regime inherits p = exp(-a*v).

If a canonical two-cell kernel has positive Lebesgue density on the collision-free configurations with fixed total count two, it assigns positive probability to moving both particles into one cell and leaving the other empty. Under this additional premise, a law supported with probability one on one particle per cell cannot be DLR. Without a uniform quantitative lower bound this observation does not by itself establish that the infinite all-cells event has probability zero.

## Source and independent work

Kernel: Lewin, arXiv:2202.09240v2, Section II.3, equation (45), and Definition 15. All inequalities and conditioning above were derived independently by w532. Source tags for campaign derivations: owner-own-work. Referee: w533, pending. Trusted assumptions: ordinary probability, exponential series, the stated DLR kernel. No formal-check receipt is claimed.

NEXT: Check whether the paired candidate needs defect-free support or instead proves a defect-tolerant local order bound uniform in volume.
