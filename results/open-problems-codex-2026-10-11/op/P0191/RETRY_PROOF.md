# A stronger special case at the constant term

Second attempt, 2026-10-11. Normalization and Lemma 1 are as in ATTEMPT.md. All matrix norms without a subscript are operator norms. Matrix-space least singular values use the Frobenius norm, not the operator norm on individual matrices.

## Theorem

Let X,Y,Z_1,...,Z_m be independent normalized N by N complex Ginibre matrices. Fix an integer k>=1 and any holomorphic polynomial Q involving X and the Z's but not Y. Set

    p(X,Y,Z)=X^k Y+Y X^k+Q(X,Z).

Put gamma=16-4 log 9>0. For every N>=1 and epsilon>0,

    P(s_min(p(X,Y,Z)-Q(0)I)<=epsilon)
      <= (64k+83) N^4 epsilon^(2/(k+3)) + exp(-gamma N).

In particular k=2 gives a cubic repeated-generator sum with exponent 2/5 and leading constant 211. No small-coefficient assumption is made. This is a source-type bound at the exact constant term. It is a special case, not a solution for arbitrary p.

## Lemma A: truncated eigenvector-overlap moment

If X is normalized complex Ginibre with spectral projections P_i for its almost-surely simple eigenvalues lambda_i, then

    E sum_(|lambda_i|<=R) ||P_i||^2 <= N^3 (R+1)^2

for every R>=0.

Proof. Simplicity holds almost surely: the characteristic-polynomial discriminant is an ordinary nonzero polynomial in the matrix entries, as seen by evaluation at a diagonal matrix with distinct entries; its zero set is null by the polynomial-zero-set proof in ATTEMPT.md, Proposition 6. For a fixed simple-spectrum matrix A, near lambda_i the resolvent has the Laurent expansion

    (A-zI)^(-1)=-P_i/(z-lambda_i)+H_i(z),

where H_i is analytic and bounded in a sufficiently small disk. To verify the expansion, diagonalize A=V diag(lambda_j) V^(-1) and separate the i-th summand; all other denominators are bounded away from zero in that disk. Let B_i bound ||H_i|| there. Then

    ||(A-zI)^(-1)|| >= ||P_i||/|z-lambda_i|-B_i.

For sufficiently small epsilon>0, the disk of radius

    r_i(epsilon)=epsilon ||P_i||/(1+epsilon B_i)

centered at lambda_i lies in {z:s_min(A-zI)<=epsilon}; at its center singularity gives the same inclusion. For every lambda_i of modulus <=R, these finitely many disks are pairwise disjoint and contained in {|z|<R+1} once epsilon is sufficiently small (the threshold may depend on A). Therefore, writing A_epsilon(A) for the planar area of the latter disk intersected with its closed epsilon-pseudospectrum,

    liminf_(epsilon down to 0) A_epsilon(A)/(pi epsilon^2)
       >= sum_(|lambda_i|<=R) ||P_i||^2.

The sum is measurable: on the open simple-spectrum locus the spectral projections can be ordered continuously in small neighbourhoods, and their unordered truncated sum is Borel; on the null complement assign zero. Apply Fatou along epsilon=1/j and then Tonelli:

    E sum_(|lambda_i|<=R) ||P_i||^2
      <= liminf_j E A_(1/j)(X)/(pi/j^2)
      = liminf_j (j^2/pi) integral_(|z|<R+1)
             P(s_min(X-zI)<=1/j) d^2z
      <= N^3 (R+1)^2.

The last bound is Lemma 1 of ATTEMPT.md, valid uniformly for every deterministic z with a=1 and D=-zI. No interchange of an unbounded resolvent expectation or uniform-in-A asymptotic is used; Fatou is in the correct direction. QED.

## Lemma B: a matrix-space similarity bound

For a simple-spectrum matrix A, set W(A)=N sum_i ||P_i||^2. If h is any polynomial in two commuting scalar variables and T=h(L_A,R_A) is its action on matrices, where L_A(H)=AH and R_A(H)=HA, then

    s_min(T) >= min_(i,j)|h(lambda_i,lambda_j)| / W(A).

Proof. Choose right eigenvectors v_i of norm one as the columns of V, so A=V Lambda V^(-1). The i-th row w_i* of V^(-1) satisfies P_i=v_i w_i* and hence ||P_i||=||w_i||, by the rank-one operator norm formula. Thus ||V||_F^2=N and ||V^(-1)||_F^2=sum_i ||P_i||^2. Since operator norm is at most Frobenius norm,

    kappa(V)^2=||V||^2 ||V^(-1)||^2 <= W(A).

The map S(H)=V^(-1) H V has norm at most kappa(V) on Frobenius space, as does its inverse, by ||BHC||_F<=||B|| ||C|| ||H||_F. In the orthonormal matrix-unit basis, h(L_Lambda,R_Lambda) is diagonal with entries h(lambda_i,lambda_j). Thus T=S^(-1) h(L_Lambda,R_Lambda) S, and its least singular value is at least min|h|/(||S|| ||S^(-1)||), proving the bound. This is the square of the diagonalizer condition number, not its first power. QED.

On ||X||<=8 every eigenvalue has modulus <=8. Lemma A and Markov consequently give, for every M>0,

    P(W(X)>M, ||X||<=8) <=81 N^4/M.

## Known input C: exact Ginibre correlations

The classical complex Ginibre eigenvalue law gives, with respect to planar Lebesgue measure, the determinantal correlation kernel

    K_N(z,w)=(N/pi) exp(-N(|z|^2+|w|^2)/2)
              sum_(j=0)^(N-1) (N z conjugate(w))^j/j!.

Here R_1(z)=K_N(z,z) counts eigenvalues and

    R_2(z,w)=K_N(z,z)K_N(w,w)-|K_N(z,w)|^2

counts ordered pairs of distinct eigenvalues. These are the standard exact finite-N Ginibre formulas, not a universality assumption or a conjecture. Reference: Jean Ginibre, *Statistical Ensembles of Complex, Quaternion, and Real Matrices*, Journal of Mathematical Physics 6 (1965), 440--449, DOI 10.1063/1.1704292. Equivalently the joint density is the normalized squared Vandermonde times exp(-N sum |lambda_i|^2), and the kernel follows by orthogonalizing the monomials: integral_C |z|^(2j) exp(-N|z|^2) d^2z=pi j!/N^(j+1), by polar coordinates. The determinantal integration identity yields the displayed one- and two-point correlations.

All estimates from this input are derived below. Since the finite exponential sum on the diagonal is bounded by the full exponential,

    R_1(z)<=N/pi,    R_2(z,w)<=N^2/pi^2.

## Lemma D: avoidance of the power-sum zero set

Let delta_k(X)=min_(i,j)|lambda_i^k+lambda_j^k|. For every s>0,

    P(delta_k(X)<=s, ||X||<=8)<=(64k+1)N^2 s^(2/k).

Proof. For i=j the expression is 2lambda_i^k. An eigenvalue with modulus at most (s/2)^(1/k) has expected count at most (N/pi) times the disk area, namely N(s/2)^(2/k)<=N s^(2/k). This estimate does not need the norm restriction.

For i!=j, on the norm event both eigenvalues lie in the disk of radius 8. For fixed w, the monic polynomial z^k+w^k factors as product_(ell=1)^k (z-rho_ell), with repetitions allowed. If its modulus is at most s, at least one factor has modulus at most s^(1/k); otherwise the product is strictly larger than s. The planar area of such z, even before restricting to the radius-8 disk, is therefore at most k pi s^(2/k). Integrate w over the radius-8 disk, of area 64pi, and use R_2<=N^2/pi^2. The expected number of bad ordered distinct pairs is at most 64k N^2 s^(2/k). Markov for the count (or a union bound expressed through correlations), together with the diagonal estimate and N>=1, proves the lemma. Including i=j is necessary; treating only R_2 would miss the event of an eigenvalue close to zero. QED.

## Lemma E: conditional full Gaussian channel

Let T be a deterministic complex-linear operator on N by N matrices with Frobenius s_min(T)>=m>0, and let Y be normalized Ginibre. For any deterministic matrix D,

    P(s_min(T(Y)+D)<=epsilon)<=N^3 epsilon^2/m^2.

Proof. Column-major vectorization of Y has covariance I/N and zero pseudocovariance. T(Y) thus has covariance TT*/N, which is at least m^2 I/N, since T is square and its least singular value is at least m. On an auxiliary probability space let G be normalized Ginibre and let U be an independent centered proper complex Gaussian with covariance (TT*-m^2I)/N. This is positive semidefinite and is realized by its Hermitian square root applied to independent standard complex Gaussians. Then mG+U has the same covariance, zero mean and zero pseudocovariance as T(Y), hence the same Gaussian law. The real covariance/characteristic-function verification is given explicitly in ATTEMPT.md, Proposition 7. Condition on U and apply Lemma 1 with a=m and deformation U+D, then integrate. There is no assumption that nonunitary conjugation preserves independent entries. QED.

## Proof of the theorem

It suffices to treat 0<epsilon<=1: if epsilon>1 the displayed right side is at least 1. Write b=2/(k+3), set s=epsilon^(k/(k+3)), and M=epsilon^(-b). Outside a bad event of probability at most

    exp(-gamma N)+(64k+1) N^2 epsilon^b+81 N^4 epsilon^b,

we have ||X||<=8, delta_k(X)>s, and W(X)<=M. The norm estimate is proved in ATTEMPT.md, Proposition 7; the other two are Lemmas D and B. On this good event Lemma B with h(u,v)=u^k+v^k yields

    s_min(T_X)>s/M=epsilon^((k+2)/(k+3)),
    T_X(H)=X^k H+H X^k.

Condition on X and all Z's. They determine the good event, T_X, and D=Q(X,Z)-Q(0)I, while Y remains independent Ginibre. Lemma E with m=epsilon^((k+2)/(k+3)) bounds the conditional least-singular-value probability by

    N^3 epsilon^2/m^2=N^3 epsilon^(2/(k+3))=N^3 epsilon^b.

Add the bad-event probabilities and use N>=1:

    (64k+1)N^2+81N^4+N^3 <=(64k+83)N^4.

This proves the claim for every epsilon>0 with fixed exponents independent of N. The proof makes no claim about an error term merely polynomial in N independent of epsilon: both conditioning obstructions are explicitly controlled at epsilon-dependent thresholds. QED.

## Extension: arbitrary one-generator bimodule coefficients

Let h(u,v)=sum_(r,s) a_(r,s) u^r v^s be a fixed scalar polynomial of total degree D>=1, and assume g(z)=h(z,z) is not identically zero. Let Q(X,Z) be any holomorphic polynomial not using Y. Define

    p(X,Y,Z)=sum_(r,s) a_(r,s) X^r Y X^s+Q(X,Z).

There exists an explicit finite C_h depending on the coefficients of h such that, for every N>=1 and epsilon>0,

    P(s_min(p(X,Y,Z)-Q(0)I)<=epsilon)
       <= (C_h+82)N^4 epsilon^(2/(D+3))+exp(-gamma N).

We prove the required coefficient sublevel bound completely, including nonconstant leading coefficients.

**Sublevel lemma.** For 0<s<=1 and delta_h=min_(i,j)|h(lambda_i,lambda_j)|,

    P(delta_h<=s, ||X||<=8)<=C_h N^2 s^(2/D).

Expand h(u,v)=sum_(j=0)^r a_j(v)u^j, with a_r nonzero. Its degree in v is ell. For r>=1 and ell=0, let c=a_r be the nonzero constant. Fix v. Factoring the degree-r polynomial in u shows that |h(u,v)|<=s implies u is within (s/|c|)^(1/r) of one of its r roots. The u-area is at most r pi |c|^(-2/r)s^(2/r). Integrating v over the radius-8 disk and applying R_2 gives the off-diagonal expected count bound

    64r |c|^(-2/r) N^2 s^(2/r)
       <=64r |c|^(-2/r) N^2 s^(2/D).

For r>=1 and ell>=1, let c be the leading coefficient of a_r(v), and put eta=s^(ell/(r+ell)). Factoring a_r shows that the v-area of {|a_r(v)|<=eta} is at most ell pi |c|^(-2/ell) eta^(2/ell). On this set bound the allowed u-area by 64pi. On its complement h(u,v) has degree r with leading coefficient of modulus >eta, so its u-sublevel area is at most r pi (s/eta)^(2/r). Integrating this over v-area at most 64pi gives, after using R_2,

    64[ell |c|^(-2/ell)+r] N^2 s^(2/(r+ell)).

Every term in a_r(v)u^r has total degree at most D, so r+ell<=D. Since s<=1 the last display is at most its constant times N^2 s^(2/D). The region where the leading coefficient vanishes is included in the bad-leading-coefficient region; no degree assumption is made there.

For r=0, h depends only on v and ell>=1 (since D>=1). Its v-sublevel area is at most ell pi |c|^(-2/ell)s^(2/ell), and the u-area is at most 64pi. The off-diagonal expected count is at most 64ell |c|^(-2/ell) N^2 s^(2/D), since ell=D in this case.

For diagonal pairs let d be the degree of g(z). If d>=1 with leading coefficient b, factorization gives z-sublevel area at most d pi |b|^(-2/d)s^(2/d). Using R_1 yields at most d |b|^(-2/d) N s^(2/d)<=d |b|^(-2/d) N^2 s^(2/D), since d<=D. If d=0, g(z)=b!=0 and the diagonal count is N times 1_(s>=|b|), at most N |b|^(-2/D)s^(2/D). Adding this diagonal constant to the off-diagonal constant just derived defines a finite explicit C_h. Markov applied to the total bad-pair count proves the lemma.

Now put beta=2/(D+3), s=epsilon^(D/(D+3)), M=epsilon^(-beta), for 0<epsilon<=1. Lemmas A/B and the sublevel lemma give exceptional probability at most

    exp(-gamma N)+[C_h N^2+81 N^4]epsilon^beta.

On the complement, the Frobenius least singular value of T_X=h(L_X,R_X) is greater than s/M=epsilon^((D+2)/(D+3)). Condition on X and Z, and apply Lemma E. The conditional probability is at most N^3 epsilon^beta. Sum and use N>=1. For epsilon>1 the displayed theorem is trivial because its right side is at least 1. This completes the extended theorem. If h is a nonzero constant (D=0), the polynomial is hY+Q and is already covered by ATTEMPT.md, Proposition 2. QED.

This covers, for example, X^2Y+YX^2, Y+[X,Y], and Y+lambda XYX for any fixed lambda, with an arbitrary independent-generator remainder Q. These examples are special cases, not claims of novelty in the literature. For h(z,z) identically zero, the coefficient operator has a kernel containing V E_(i,i) V^(-1) for each i. Its output matrix may nevertheless be invertible: trace constraints and a kernel in N^2-dimensional matrix space do not imply singularity of an N-dimensional matrix. Thus the failure of the method is not a counterexample to Question 1.6.

## Further extension: the exact diagonal-kernel obstruction can be bypassed

The preceding theorem required h(z,z) not identically zero in order to obtain full Gaussian covariance. A different Gaussian baseline removes that restriction. This section proves the stronger result rather than treating singular covariance as an unresolved gap.

### Lemma F: independent off-diagonal Gaussian noise

Let N>=2, G_off be normalized Ginibre with its diagonal replaced by zero, a>0, and D any deterministic matrix. Put M=aG_off+D. For 0<t<=1 and any K>=1,

    P(s_min(M)<=t)
       <= P(||M||>K)+(4N^3 K^2+N^2)t/a^2.

Proof. As in ATTEMPT.md, Lemma 1, a small least singular value implies for some column j that dist(C_j,H_j)<=sqrt(N)t. Choose a measurable unit normal u_j to H_j, depending only on the other columns. Write delta_j=(sum_(i!=j)|(u_j)_i|^2)^(1/2). Given the other columns, u_j* C_j is a complex Gaussian of variance a^2 delta_j^2/N, plus its deterministic mean. Fix 0<v<=1/2. For delta_j>=v the conditional disk bound is N^2 t^2/(a^2 v^2). Sum over j to obtain N^3 t^2/(a^2 v^2).

For delta_j<v on ||M||<=K, use the equations u_j* C_k=0 for all k!=j. Since |(u_j)_j|=(1-delta_j^2)^(1/2), these equations, gathered as a row vector, imply

    ||(M_(j,k))_(k!=j)||_2
       <= delta_j ||M||/(1-delta_j^2)^(1/2) <=2vK.

Indeed the remainder is the row (u_j)_(i!=j)* times the submatrix with row and column j removed, whose operator norm is at most ||M||. Choose one fixed index k(j)!=j, possible since N>=2. The localization event implies |M_(j,k(j))|<=2vK. This scalar is an off-diagonal Gaussian of variance a^2/N with a deterministic mean; no conditioning on its row is performed here. Its probability is at most 4N v^2K^2/a^2. Sum over j to obtain 4N^2 v^2 K^2/a^2. This is a superset bound on the localization event, valid even though the normal itself depends on those row entries.

Add the norm-failure event. Set v^2=t/(4K^2), which is positive and at most 1/4 because t<=1 and K>=1. The two terms become 4N^3K^2 t/a^2 and N^2t/a^2, respectively. QED. The diagonal entries of D may be arbitrary, and the lemma does not assume independence of the chosen normals from the other columns.

### Gaussian norm input with explicit error

If g has N^2 independent standard complex Gaussian entries, sum |g_i|^2 is the sum of N^2 mean-one exponential variables. Markov applied to exp((1/2)sum|g_i|^2), whose mean is 2^(N^2), gives

    P(||g||_2>2N)<=exp(-(2-log2)N^2).

Let c_chi=2-log2>0. Hence ||G_off||_F<=2sqrt(N) except with probability exp(-c_chi N^2). Further, a centered proper complex Gaussian U in matrix space with covariance at most H^2 kappa^2 I/N has ||U||_F<=2H kappa sqrt(N) except with that same probability. For the latter assertion realize its covariance square root on N^2 independent standard complex Gaussians and use its operator norm <=H kappa/sqrt(N). Degenerate covariance causes no difficulty.

### Theorem G: every nonzero scalar bimodule coefficient

Let h(u,v)=sum a_(r,s)u^rv^s be any nonzero polynomial of total degree D>=1, without a condition on h(z,z). Let

    p(X,Y,Z)=sum a_(r,s)X^rYX^s+Q(X,Z),

where X,Y,Z_1,...,Z_l are independent normalized complex Ginibre and Q excludes Y. Put beta=2/(2D+7) and c=min(16-4log9,2-log2)>0. There are explicit finite constants C_poly,C_exp depending only on h,Q,l such that, for every N>=2 and epsilon>0,

    P(s_min(p(X,Y,Z)-Q(0)I)<=epsilon)
       <=C_poly N^4 epsilon^beta+C_exp exp(-cN).

In particular this proves the source-type estimate for [X,[X,Y]], a cubic zero-abelianization polynomial, and for X^kY-YX^k at all fixed k. It still does not treat arbitrary nonlinear occurrences of both generators.

Proof. In the sublevel argument of the preceding extension retain only the distinct-pair estimate, with its explicit constant A_h (the off-diagonal constant there). It holds for every nonzero h irrespective of its diagonal restriction:

    P(min_(i!=j)|h(lambda_i,lambda_j)|<=s, ||X||<=8)
       <=A_h N^2 s^(2/D),   0<s<=1.

Define H=sum_(r,s)|a_(r,s)|8^(r+s)>0. Let C_Q be the sum over nonconstant monomials of Q of |coefficient|8^(word length). On ||X||,||Z_j||<=8, the matrix D_0=Q(X,Z)-Q(0)I has norm at most C_Q. Take 0<epsilon<=1, s=epsilon^(beta D/2), and L=epsilon^(-beta/2). Outside an event of probability at most

    (l+1)exp(-(16-4log9)N)
      +[A_h N^2+81N^4]epsilon^beta,

the matrices X,Z_j have norms at most 8, min_(i!=j)|h(lambda_i,lambda_j)|>s, and W(X)<=L^2. Here the last event is controlled by Lemma A and Markov, as in Lemma B. Choose the eigenvector matrix V with unit columns; then kappa=||V|| ||V^(-1)||<=L and kappa>=1. Write S(A)=V^(-1)AV.

In this basis the centered part of S(p-Q(0)I) is D_h S(Y), where D_h is diagonal in the matrix-unit basis with entries h(lambda_i,lambda_j). Its covariance Sigma obeys

    Sigma >= (1/(N kappa^2)) D_h D_h*,
    Sigma <= (H^2 kappa^2/N) I.

These follow because S(Y) has covariance SS*/N, and ||S||,||S^(-1)||<=kappa. In particular, if P_off is the orthogonal projection onto off-diagonal matrix entries, then

    Sigma >= (s^2/(N kappa^2))P_off.

No assertion is made that Sigma is invertible: some diagonal directions may have zero variance. Choose a=epsilon^(beta(D+1)/2). Since kappa<=L, s/kappa>=s/L=a, so Sigma-a^2 P_off/N is positive semidefinite. On an auxiliary Gaussian space realize

    D_h S(Y) equal in distribution to a G_off+U,

with independent G_off and centered proper Gaussian U of covariance Sigma-a^2P_off/N. Equality follows from the covariance and zero pseudocovariance calculation of Lemma E. This residual covariance is at most H^2 kappa^2 I/N. It may include diagonal randomness or have zero diagonal randomness; either is allowed.

Conditional on X,Z and outside an additional U-event of probability exp(-c_chi N^2), its norm is at most 2H kappa sqrt(N). The deterministic deformation after additionally conditioning on U is U+S(D_0), with ||S(D_0)||<=kappa C_Q. The independent aG_off has norm at most 2a sqrt(N)<=2sqrt(N) outside its own event of probability exp(-c_chi N^2), since a<=1. Thus choose

    C_norm=2+2H+C_Q,    K=C_norm sqrt(N) L>=1.

On the U-good event, the conditional probability that ||aG_off+U+S(D_0)||>K is at most exp(-c_chi N^2). This conclusion is uniform over X,Z,U on their good events; we never condition G_off on its norm event before applying a density bound.

Conjugation gives s_min(p-Q(0)I)>=s_min(S(p-Q(0)I))/kappa. Therefore an original least singular value <=epsilon implies a transformed least singular value <=t=L epsilon=epsilon^(1-beta/2)<=1. Apply Lemma F conditionally with this t,K,a. Apart from the two Gaussian norm-error probabilities, its bound is

    (4N^3K^2+N^2)t/a^2
       <=5 C_norm^2 N^4 epsilon^(1-beta/2-beta-beta(D+1))
       =5 C_norm^2 N^4 epsilon^beta.

For the first inequality K^2=C_norm^2 N epsilon^(-beta), and its contribution dominates the N^2 term since N>=1,C_norm>=1,epsilon<=1. The exponent is 1-beta(D+5/2)=beta, because beta(D+7/2)=1. Thus no epsilon-independent polynomial failure term has been introduced.

Sum all exceptional events. One may take

    C_poly=A_h+81+5 C_norm^2,    C_exp=l+3.

Since exp(-c_chi N^2)<=exp(-cN) for N>=1, and exp(-(16-4log9)N)<=exp(-cN), these constants yield the theorem. For epsilon>1 the right side is at least 1 because C_poly>=81. Taking a common leading constant max(C_poly,C_exp) writes the answer exactly in the source's required form. Nonzero constant h is handled by the earlier additive-generator lemma. QED.

### Additional referee checks

There is also a separate qualitative corollary: every polynomial in Theorem G is invertible almost surely at the constant term for each fixed N>=2. For distinct eigenvalue pairs, the zero set of a nonzero h in C^2 has planar-product Lebesgue measure zero by the polynomial-zero-set induction in ATTEMPT.md; the absolutely continuous R_2 law therefore makes all h(lambda_i,lambda_j), i!=j, nonzero almost surely. For such a fixed X, use a positive covariance floor on the off-diagonal subspace with no norm truncation and decompose as aG_off+U. Conditional on U and the other generators, the determinant of aG_off+D is a nonzero polynomial in the off-diagonal Gaussian variables: the derangement pi(j)=j+1 modulo N contributes the unique degree-N monomial product_j G_(pi(j),j), with nonzero coefficient sign(pi)a^N. No other permutation gives that same monomial. Thus its zero set is null, and integrating gives almost-sure invertibility. This is a qualitative argument independent of the epsilon-dependent tail proof; it does not supply the quantitative constants for arbitrary p.

The index k(j)!=j in Lemma F is fixed in advance, and its scalar density estimate is unconditional; the random normal's dependence on that row is not ignored. The law of Y is exposed only after conditioning on independent generators. Nonunitary conjugation is accounted for twice: once in the covariance floor and again when returning the least singular value to the original basis. W controls the full diagonalizer, not only one eigenvector. The residual Gaussian U is norm-controlled before conditioning on it. Frobenius rather than operator norm is used for that bound, costing a factor sqrt(N) that is retained in K. The final exponent includes all three such losses and is explicitly balanced. N>=2 is essential for the off-diagonal baseline; at N=1 a pure commutator really vanishes. No conclusion about matrix singularity follows merely from singular covariance.

No global choice of a random eigenvector basis is needed: for each fixed simple-spectrum X, choose a basis, prove the uniform conditional probability bound for Y, and then integrate the original measurable polynomial event over X,Z. The bad events involve only symmetric eigenvalue-pair quantities and W, which are Borel on the simple-spectrum locus. The covariance comparison on the off-diagonal subspace is in the Loewner order on the full matrix space, not a claim about only a compressed covariance block: Sigma >= kappa^(-2)D_hD_h*/N >= a^2 P_off/N. Thus subtracting the independent off-diagonal covariance leaves a genuinely positive semidefinite full covariance, even if the residual has correlations involving diagonal entries.

As an exact finite check, for X=diag(lambda_1,lambda_2) and arbitrary Y, [X,[X,Y]] has diagonal zero and off-diagonal entries (lambda_1-lambda_2)^2 Y_(1,2) and (lambda_1-lambda_2)^2 Y_(2,1). Its determinant is -(lambda_1-lambda_2)^4 Y_(1,2)Y_(2,1). At N=1 it is identically zero, while at N=2 the off-diagonal noise provides the needed two independent scalar directions. This confirms the dimension exception and the distinction between a covariance kernel and matrix singularity.

## Saved numerical and formal checks

`retry_checks.py` / `retry_checks.json` (seed 19102, one BLAS thread) completed 192 vectorization/similarity/diagonalizer checks and 540 explicit resolvent-disk checks at N=1,2,4,8 in 0.47 seconds. The largest positive lower-bound discrepancy was 8.88e-16 and vectorization error 9.14e-16; disk inclusion and diagonalizer inequalities had no positive discrepancy. These check algebraic bookkeeping in Lemmas A/B, not the probability theorem.

`retry_mask_checks.py` / `retry_mask_checks.json` (seed 19103) completed 96 covariance-floor and intertwining checks for power commutators, nested commutators, and variable-leading-coefficient channels at N=2,3,4,8. It also tested 44 localized-normal implications, deliberately including diagonal deformations of size 1000. All assertions passed at the specified tolerances; runtime 0.092 seconds. No empirical rare-event count is used to infer the theorem.

`RetryThreshold.lean` checks the cubic full-covariance cutoff implication and its exponent identity. Run from ~/lean_verify as `lake env lean ~/brain_workers/TRIO_1011/op/P0191/RetryThreshold.lean` with a 3600-second timeout, it exited 0 after 1304.7 seconds. Both `#print axioms` results contain only propext, Classical.choice, Quot.sound; there is no sorry or native_decide. Output is saved in retry_lean_check.txt. The sparse-channel theorem and analytic/probabilistic lemmas are written mathematical proofs and are not claimed Lean-verified.

## Precise remaining gap

An invertible linear remixing of the two generators does not bring the representative cubic into the class just proved. Indeed set X=aS+bT, Y=cS+dT with scalar complex coefficients. Expanding the free words in XYX+YXY, the coefficients of STT and TTS are bd(a+c), of TST are b^2c+d^2a, and of TTT are bd(b+d). For the resulting polynomial to be linear in T plus a polynomial independent of T, all three quantities must vanish. If b=0, the middle condition is d^2a=0, so either d=0 or a=0; in either case ad-bc=0. If d=0 the same argument gives b=0 or c=0 and again ad-bc=0. If b,d are both nonzero, the first and last conditions imply c=-a and d=-b, whence ad-bc=0. Thus every such remixing is singular. This rules out the obvious unitary Gaussian-generator rotation as a route from this cubic to Theorem G; it is a counterexample to that proposed reduction, not to P0191 itself.

The full question is not solved. The argument needs a polynomial linear in an independent Ginibre generator, with all its exterior coefficients polynomials in one other generator so that a single spectral basis controls them. The off-diagonal baseline now handles the intrinsic commutator-channel kernel, and Theorem G covers arbitrary nonzero scalar h, including zero abelianization. It cannot treat XYX+YXY, which is nonlinear in each generator, or general exterior coefficients depending noncommutatively on several generators. Neither operator scaling nor noncommutative rank has yet bridged that gap. All results here are proved special cases, using the standard exact Ginibre eigenvalue formula as an external input. No general counterexample is established.
