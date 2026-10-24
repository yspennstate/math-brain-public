# C0109: what moment truncation does and does not prove

Label: two proved audit lemmas, pending w347. No optimal circular-law rate is claimed.

For eps>0, R>0 and M=E|X|^(2+eps)<infinity,

    E[|X|^2 * 1_{|X|>R}] <= M*R^(-eps),
    P(|X|>R) <= M*R^(-(2+eps)).

These follow pointwise from |X|^2<=R^(-eps)|X|^(2+eps) on the tail, and Markov's inequality. At R=n^r the first bound is M*n^(-r*eps). It bounds a truncation error; it is not a lower bound for the error of the original matrix's empirical eigenvalue law.

The power eps in the scalar tail envelope cannot be uniformly increased under the same moment assumption. Take a symmetric law with total probability q_j=c*2^(-(2+eps)*j)/j^2 at the two atoms +/-2^j, j>=1, and remaining mass at zero, choosing c>0 sufficiently small. It has mean zero, positive finite variance and finite (2+eps)-moment c*sum_j j^(-2). At R=2^m, its missing variance is

    c*sum_{j>m} 2^(-eps*j)/j^2.

The first summand gives a lower bound; a geometric series after replacing j by m gives an upper bound. For m>=1 this quantity lies between positive constants times 2^(-eps*m)/m^2. Thus it is not O(R^(-eps-eta)) for any eta>0 along dyadic cutoffs. Rescaling by its standard deviation preserves the tail exponent. This sharpness statement concerns a scalar truncation envelope and does not prove a moment-dependent circular-law lower bound.

A second trap is to transfer a rank perturbation estimate from Hermitian matrices to nonnormal eigenvalue laws. Let J_n have ones on its superdiagonal and zeros elsewhere, and C_n=J_n+e_n e_1^T. Their difference has rank one. J_n is nilpotent and all eigenvalues are zero; C_n is a cyclic permutation matrix and has every nth root of unity as an eigenvalue. For the bounded 1-Lipschitz radial test f(z)=min(|z|,1), their empirical laws differ by exactly one. Hence a rank/n eigenvalue-discrepancy bound is false for this nonnormal family. This is a deterministic obstruction; it is not itself an iid random-matrix lower bound.

Proof of the spectrum: J_n^n=0. For z^n=1, the vector (1,z,...,z^(n-1)) is a C_n eigenvector of eigenvalue z. The n roots are distinct, exhausting its spectrum. The test is zero on J_n's spectrum and one on C_n's.

The prior attempt calls its proposed scaling a heuristic, but its key-identity line says the truncation error "caps delta(eps)". An upper bound for one proof's discarded variance does not supply that optimality conclusion. A full rate claim still needs a specified metric, mode of convergence, quantitative moment bound, Hermitization control, and a matching lower example in the same matrix class.

Checks: exact dyadic tail sums and bounds; the rank-one perturbation; nilpotence and root-of-unity eigenvectors; a fixed bounded Lipschitz separating test; preservation of the distinction between scalar tails and iid matrix rates.
