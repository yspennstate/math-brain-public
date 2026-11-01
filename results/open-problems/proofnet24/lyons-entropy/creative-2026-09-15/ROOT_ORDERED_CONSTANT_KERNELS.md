# Explicit complex constant-upper-entry kernels in the count-uniform class

Coordinator corollary of C074, 15 September 2026. This is an explicit family inside C074's already established theorem, not an additional universal concavity result or a claim of historical novelty.

For real a and complex z, let T_n(a,z) have diagonal a, every strictly upper entry z, and every strictly lower entry conjugate(z). Every principal submatrix of order m is exactly T_m(a,z) after preserving the coordinate order. Consequently all principal minors depend only on their order, and the occupation atom probabilities depend only on cardinality.

C074 therefore proves the full Hermitian entropy Hessian is nonpositive at every strict contraction T_n(a,z), and negative definite whenever z is nonzero and n>=2. This permits arbitrary real and imaginary parts of z; it includes both the real exchangeable and the purely imaginary ordered families. The entropy law is permutation invariant even though a general complex kernel here is not invariant under arbitrary coordinate permutations.

## Closed atom formula

Write D_m=det T_m(a,z), D_0=1. Consecutive row differences give

    D_m=(a-z) D_(m-1)+z(a-conjugate(z))^(m-1).

For nonreal z, summing this geometric recurrence yields

    D_m=[z(a-conjugate(z))^m-conjugate(z)(a-z)^m]/[z-conjugate(z)].

The formula includes D_0=1 and D_1=a. Inclusion-exclusion then gives the probability of EACH specified atom S of size k:

    p_k = [z(a-conjugate(z))^k(1-a+conjugate(z))^(n-k)
           -conjugate(z)(a-z)^k(1-a+z)^(n-k)]/[z-conjugate(z)].

This is real, and nonnegative on the contraction domain. Its binomially weighted sum over k equals one. The real-z case follows by continuity. If z=x is real and s=a-x lies strictly between zero and one, the limit is

    p_k=s^k(1-s)^(n-k) [1+x(k/s-(n-k)/(1-s))].

Boundary cases are interpreted by the polynomial limit. At z=ib the formula reduces to Re[(a+ib)^k(1-a-ib)^(n-k)], agreeing with C074.

## Gauge-circulant form and eigenvalues

For Im(z)>0, write z=x+iy=|z| exp(i phi), with 0<phi<pi. Let D_jj=exp(-2i phi j/n), j=0,...,n-1. Then D* T_n(a,z) D is circulant: the lower-entry wrap identity follows from exp(-2i phi)=conjugate(z)/z. Its first-row displacement-d entry is z exp(-2i phi d/n).

The Fourier geometric sum gives the n real eigenvalues

    lambda_k=a-x+y cot((phi+pi k)/n),   k=0,...,n-1.

They are distinct and strictly decreasing with k. The exact strict contraction domain is therefore

    0<a-x+y cot((phi+(n-1)pi)/n),
    a-x+y cot(phi/n)<1.

Negative imaginary parts follow by entrywise conjugation, which preserves eigenvalues and measured entropy. For real z the eigenvalues are a+(n-1)z once and a-z with multiplicity n-1. Thus this is a three-real-parameter explicit family of count-uniform bases, and the C074 theorem controls every ambient Hermitian direction at every physical point, including phases with both nonzero real and imaginary parts. Arbitrary circulant kernels are not asserted to have a count-uniform law.
