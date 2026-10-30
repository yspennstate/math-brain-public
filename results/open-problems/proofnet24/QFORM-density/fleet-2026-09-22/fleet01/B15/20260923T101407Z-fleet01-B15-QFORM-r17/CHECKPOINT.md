SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet01, slot B15, 2026-09-23T10:14:07Z.
attacking: target-level Poisson boundary regularity and a product-preserving fractional majority-cover inequality for the surviving rough-law/two-sheet obstruction.

# Early substantive checkpoint

Full QFORM remains OPEN.

Let `mu` be a finite positive Borel measure on R and `P_eta(x)=eta/[pi(x^2+eta^2)]`. The exact regularity hierarchy is:

1. `mu=p dx` with `p in L^infinity`, `||p||_infinity<=M`, iff `sup_{eta>0} ||P_eta*mu||_infinity<=M`.
2. `mu=p dx` with `p in C_0(R)` iff `P_eta*mu` converges in `L^infinity` as `eta downarrow 0`.

The second statement cleanly separates continuity from the central height estimate: uniform boundedness of the harmonic extension yields only the L-infinity boundary measure; norm convergence is the additional regularity input.

Using the completed fleet02/B15 rough ambient ruled theorem: for each invertible indefinite ORIGINAL-coordinate physical 3x3 block `B_j`, with `kappa_j=sigma_min(B_j)`, its majority event `M_j` obeys

`P(Q in I, M_j) <= (pi sqrt(2)/kappa_j) |I|`

for every interval `I`, with arbitrary outside quadratic terms/cross couplings and rough cap-one product marginals.

Hence any nonnegative coefficients `lambda_j` satisfying the pointwise fractional coverage

`sum_j lambda_j 1_{M_j} >= delta` a.s.

give the new direct raw-law inequality

`delta P(Q in I) <= pi sqrt(2) |I| sum_j lambda_j/kappa_j`,

so

`||p_Q||_infinity <= (pi sqrt(2)/delta) sum_j lambda_j/kappa_j`.

This is a cover-before-inversion certificate: it uses the completed partner submeasure theorem at an actual inequality, preserves original-coordinate product provenance, and avoids continuity, rotated independence, generic X-ray control, and law-uniform pointwise Fourier decay. The unpaid structural step is whether the surviving N3/full-target matrices admit a fractional majority cover whose scaled reciprocal cost `s_3(A) sum lambda_j/kappa_j / delta` is universally bounded, or whether a residual minority event must instead be controlled by another product-sensitive exit.
