# Direct comparison upper-rate derivation, 2026-10-11

Candidate, not yet recorded as proved:
For e=min(eps,1), p=2+e, compare regularized potentials
 F_eta=(1/(2n))logdet((A-z)(A-z)*+eta^2 I)
and regularized small-singular counts
 V_eta=(1/n)sum eta^2/(s_i^2+eta^2)
to a Gaussian iid law having the same real two-coordinate covariance.

Hermitian dilation resolvent gives kth one-entry derivative bounds
C_k/(n eta^k) times the kth power of normalized entry change, k<=3.
Second-order Lindeberg with the min(second,third) remainder then gives
uniform expectation errors C M n^(-e/2) eta^(-p) for both functions.

Gaussian V_eta should have expectation <=C(eta+1/n), uniformly in
the deterministic shift, from row deletion and the negative-second-
moment identity; check this independently using conditional Gaussian
distances to complex subspaces, including real or degenerate covariance.

For s_min>=n^-B,
 .5 log(1+eta^2/s^2) <=C_B log n * eta^2/(s^2+eta^2).
Thus removing regularization costs C log n V_eta, with the exceptional
z set handled by the earlier L2 potential bound and Tao–Vu Theorem 2.5.

Replacing one row changes V_eta by <=1/n. Clipped F_eta changes by
<=C log n/n. McDiarmid therefore gives overwhelming-probability
concentration of their integrated functionals without higher moments.
Upper clipping affects only a polynomially small event by second moments.

Balance eta=n^-gamma, gamma=e/(2(p+1))=e/(6+2e), yielding an integrated
log-potential comparison to the mean Gaussian potential of order
n^-gamma log n. Compact smoothed southwest rectangles cost h^-2;
choose h=n^-gamma/3. The Gaussian law has a fixed all-moments W_1 rate.
This would give source-metric rate n^-beta log n, beta=e/(18+6e),
with overwhelming probability and hence almost surely eventually.
This is nonoptimal and remains a candidate until all steps are written.
