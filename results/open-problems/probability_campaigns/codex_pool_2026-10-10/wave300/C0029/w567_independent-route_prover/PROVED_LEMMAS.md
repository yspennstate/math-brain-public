# C0029: scoped proofs for review

All results below are self-contained elementary results, not a proof of the parent conjecture. Author: w567. Independent mathematical reviewer: w569, pending. No formal-check receipt is claimed.

## L1: singularity floor

For n>=2, if B has independent uniform sign entries, then P(s_min(B)=0)>=2^(1-n). Conditional on its first row r, the independent second row is uniform on 2^n vectors; exactly r and -r are proportional to r. Either makes B singular. No product of conditional bounds is used.

## L2: arithmetic gap

For every nonsingular n by n sign matrix B, n>=2,

s_min(B) >= alpha_n := 2^(n-1) ((n-1)/n^2)^((n-1)/2).

Subtract row 1 from every other row. Every entry of those n-1 rows is even, so factoring 2 from each proves det(B) is divisible by 2^(n-1). A nonzero such integer has absolute value at least 2^(n-1). Order the singular values s_1>=...>=s_n>0. Their squared sum is ||B||_F^2=n^2. Thus, by AM-GM,

product_{i<n} s_i <= ((sum_{i<n} s_i^2)/(n-1))^((n-1)/2) <= (n^2/(n-1))^((n-1)/2).

Since product_i s_i=|det(B)|, dividing gives the assertion. Hence for 0<=epsilon<sqrt(n)alpha_n, the event s_min(B)<=epsilon/sqrt(n) is exactly the event det(B)=0. The strict upper endpoint is deliberate. The cutoff has log(sqrt(n)alpha_n)=-(n/2)log n+n log 2+O(log n); it is superexponential, so the unsolved window remains.

## L3: exact sign normalization and bordered inverse

For iid uniform sign B of size n>=2, there are diagonal sign matrices D_r,D_c such that C=D_r B D_c has first row and column identically 1 and can be written

C = [[1, 1^T], [1, J-2H]],

where H is (n-1) by (n-1) with iid uniform {0,1} entries. B and C have exactly the same singular values. Conditional on the entire first row and column of B, the entries of the lower-right block of B remain independent uniform signs. Put (D_c)_{jj}=B_{1j} and (D_r)_{ii}=B_{i1}B_{11}. Then C_{1j}=C_{i1}=1 and for i,j>1,

C_{ij}=B_{i1}B_{11}B_{ij}B_{1j}.

The conditioned boundary only multiplies each independent interior sign by a fixed sign. Therefore the conditional joint law of C's interior is the uniform product law and does not depend on the boundary. Set H_{i-1,j-1}=(1-C_{ij})/2. Orthogonal diagonal multiplications preserve singular values.

Subtracting the first row from the others gives det(C)=(-2)^(n-1)det(H). In particular, B is nonsingular if and only if H is. For nonsingular H, the exact inverse is

C^(-1) = [[1-(1/2)1^T H^(-1)1, (1/2)1^T H^(-1)], [(1/2)H^(-1)1, -(1/2)H^(-1)]].

This follows either by direct block multiplication or by the Schur complement S=J-2H-11^T=-2H. Consequently the parent conjecture is equivalent, away from singular H, to an upper-tail estimate for the operator norm of this displayed inverse. The border terms and their dependence on H cannot be dropped.

## L4: exact row-crossing criterion (audit aid)

Let R be a real (n-1) by n matrix of full row rank. Let v be a unit kernel vector and u_1,...,u_{n-1} orthonormal right singular vectors with positive squared singular values d_i. For any row x and any 0<=t<min_i sqrt(d_i), put a=<x,v>, b_i=<x,u_i>, and A=[R;x]. Then

s_min(A)<=t iff a^2<=t^2(1+sum_i b_i^2/(d_i-t^2)).

For t>0, express A^T A-t^2 I in the basis (v,u_1,...,u_{n-1}). Its lower-right block is D+bb^T, where D=diag(d_i-t^2)>0. Its Schur complement is

a^2-t^2-a^2 b^T(D+bb^T)^(-1)b = a^2/(1+b^T D^(-1)b)-t^2.

The lower block is positive definite. By congruence, the full matrix is positive definite, positive semidefinite with a zero eigenvalue, or has a negative eigenvalue according as this scalar is positive, zero, or negative. This proves the weak-inequality equivalence, including equality. At t=0, both sides say a=0, equivalent to singularity of A. The formula is undefined at or above the lower rectangular singular-value threshold, and must not be used there. No independence among a and the b_i is claimed for a Rademacher row. Indeed at n=2, v=(1,1)/sqrt(2), u=(1,-1)/sqrt(2), these two projections have product zero and are not independent.

## L5: flatness and conditioning cannot give a uniform conditional bound

For every n=2^k, k>=1, let Q_n be the Sylvester sign Hadamard matrix, so Q_n Q_n^T=n I and its first row is all 1. Let R be Q_n with its first row removed. Then all n-1 positive singular values of R equal sqrt(n) and the unit kernel vector v=n^(-1/2)(1,...,1) is perfectly flat. For an independent iid sign row x,

P(s_min([R;x])=0 | R)=P(sum_j x_j=0)=binom(n,n/2)/2^n >= 1/(n+1).

The matrix is singular exactly when the new row is orthogonal to the one-dimensional kernel of R. The sum vanishes exactly for n/2 positive signs. The central binomial coefficient is the largest of the n+1 binomial coefficients, whose sum is 2^n, proving the lower bound. The construction exists for every power of two by Q_2=[[1,1],[1,-1]] and Q_{2m}=[[Q_m,Q_m],[Q_m,-Q_m]]. Thus no fixed C,c>0 can give a bound epsilon+C exp(-c n) conditional on every block with these spectral and flatness properties: at epsilon=0, 1/(n+1)>C exp(-c n) for all sufficiently large n. This does not refute the unconditional conjecture; the iid rectangular block rarely equals this structured witness. It refutes only that proposed uniform conditional step.

## L6: exact proportional-row collision floor and the sharp exponential base

Let n>=2, q=2^(n-1), and m=binom(n,2). For iid sign B,

P(B singular) >= p_n := 1-product_{j=0}^{n-1}(1-j/q) >= m/q-binomial(m,2)/q^2.

Moreover p_n=(1+o(1))n(n-1)2^(-n). In particular there is no absolute C such that P(B singular)<=C 2^(-n) for every sufficiently large n. This does not rule out (1/2+o(1))^n or an arbitrary fixed exponential base greater than 1/2.

Normalize each row by its first entry. Its remaining n-1 entries form an iid uniform vector in a set of q sign vectors; normalized rows are independent across rows. Two original rows are proportional precisely when their normalized vectors coincide. Given the first j distinct vectors, the next independent uniform vector avoids them with probability 1-j/q. Iterating this conditional probability along the filtration generated by the exposed rows gives the displayed product for no collision. This multiplication is justified by the proved conditional probability; it does not assume independence of collision events.

For the lower bound, apply Bonferroni to the m pair-collision events. Each has probability 1/q. Any two distinct pairs, whether disjoint or sharing a row, both collide with probability 1/q^2, since they impose two equality constraints on iid uniform vectors. Thus their union has probability at least m/q-binomial(m,2)/q^2 and at most m/q. Since m/q tends to zero, the two bounds are asymptotic. A row collision forces singularity, finishing all claims.

## C1: finite Gaussian law correction

For an iid standard-real-Gaussian matrix G_n, the formula F(t)=1-exp(-t-t^2/2) describes the limit of P(sqrt(n)s_min(G_n)<=t) as n tends to infinity at fixed t>=0. It is not the finite-n exact law. A counterexample is n=1: the actual CDF is P(|g|<=t)=sqrt(2/pi) integral_0^t exp(-u^2/2)du, so its derivative at zero is sqrt(2/pi). F'(0)=1. Primary sources: Tao-Vu, arXiv:0903.0614, Theorem 1.1 (Edelman limiting law) and Theorem 1.3 (universality). The local C0029-A001 calls the limit an exact law twice; the supplied patch corrects both occurrences without altering its unsolved verdict.

## Single hardest gap

Prove, for the iid {0,1} H above, a sharp upper-tail bound for the operator norm of the full bordered inverse: for all 0<epsilon<1, P(H singular or ||C(H)^(-1)||_op>=sqrt(n)/epsilon)<=epsilon+exp(-Omega(n)). The equivalence is proved in L3, but this probabilistic bound is conjectural. L2 resolves only the much smaller arithmetic plateau. A Gaussian comparison with a multiplicative o(1) loss cannot close the remaining coefficient-one obligation.
