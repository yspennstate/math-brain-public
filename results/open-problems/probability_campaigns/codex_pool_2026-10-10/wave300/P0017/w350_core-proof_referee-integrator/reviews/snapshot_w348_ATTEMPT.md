# P0017: tensor recovery and an all-degree special case

2026-10-10, w348. Prover-written proof, awaiting w349 adversarial check and w350 independent review. No full KLS proof or novelty clearance is claimed.

## Target, sources and prior attempts

The exact target and independent challenge are in STATEMENT_FIRST.md. The September ranking says attempted_un; the October 4 primary papers arXiv:2610.05474v1 and arXiv:2610.01447v2 now report a full resolution. This packet checks a precise part of the mathematics and produces a proved special case of its analytic input. It does not certify either paper's complete proof. A primary-source statement is evidence of the authors' claim, not independent verification.

Bizeul--Klartag--Lehec (BKL), Lemma 2.2, states a recovery factor 4^d for a tensor symmetric in blocks of d and 2d indices. Its own proof already gives binom(2d,d); replacing 4^d by that number is not a new result. Here the incidence identity is proved for arbitrary block lengths p <= q, and sharpness, approximate symmetry, and a missing-assumption counterexample are supplied explicitly.

BKL Theorem 3.1 gives a route from uniform Hilbert--Schmidt Taylor bounds for every L2 tilt-average to a Poincare bound. That theorem remains an externally supplied reduction in this packet. The single hardest remaining input is the universal all-degree Taylor bound for arbitrary centered regular log-concave measures of covariance <= I. Proving a tensor inequality does not discharge it.

Read-only population-store recovery found the exact older cards: problem node claim_d2e9e3d859a16e515c09803220b9b26608e8a6b5a6ce584d2e99cf6613f89694 names Randomstrasse101: Open Problems of 2025, Entry 13, Conjecture 30. Attempt node claim_fbc7554cdcce8efc8484f98a5982f7add13464aa5d5d53dfb9ca2710fc43e19f proves the Gaussian special case by Hermite expansion, with optimal constant 1, then states the unresolved obstruction: a general isotropic log-concave law has no such diagonal Hermite generator. It is labeled author-checked only, with no independent review. No targeted P0017 row was found in the named H/I attempts or Lean records beyond the annotated ranking; this bounded search does not certify absence of other owner work. The new product-exponential proof uses support orthogonality rather than silently extending the Gaussian eigenbasis argument.

The recall call was cut off at 60 seconds. Targeted fallback read the scar perceptron_proof_open_gaps_fleet_2026_07_12: a successful component and a green runner did not close other proof gaps. The same discipline is used here: exact arithmetic checks and source checks are separate from mathematical proof and independent review.

## L1. Sharp recovery from partial symmetrization

Let H and W be finite-dimensional real Hilbert spaces. Let 1 <= p <= q and N=p+q. A tensor T in H^(tensor N) tensor W is invariant under permutations of positions 1,...,p and, separately, positions p+1,...,N. Write P_q for the orthogonal projection averaging permutations of the first q positions. Then

    ||T|| <= b ||P_q T||,     b = binom(q,p).

The constant is optimal for dim H >= 2 and W nonzero. W can absorb any untouched trailing tensor indices.

Proof of the bound. For every p-subset F of Omega={1,...,N}, let T_F be the permutation of T placing its first block into F and its second block into Omega\F. Block symmetry makes this independent of the chosen within-block order; every ||T_F|| equals ||T||. For each q-subset E, put U_E=sum_{F subset E, |F|=p} T_F. Each U_E is a permutation of b P_q T.

For any Hilbert-space-valued family v_F, the exact identity is

    sum_{|E|=q} ||sum_{F subset E, |F|=p} v_F||^2
      = sum_{s=0}^p binom(q-p,p-s)
          sum_{|S|=s} ||sum_{F superset S, |F|=p} v_F||^2.       (I)

Binomial coefficients outside their usual range are zero. To verify (I), expand both sides into ordered inner products <v_F,v_G>. If r=|F intersection G|, the left coefficient counts q-subsets containing F union G and is binom(q-p+r,p). The right coefficient is sum_s binom(r,s)binom(q-p,p-s), the same number by Vandermonde's identity. Since q-p >= 0 every right coefficient is nonnegative, and its s=p term is exactly sum_F ||v_F||^2. Applying this to T_F, and using binom(N,q)=binom(N,p), proves the bound after canceling the common number of subsets. This is an exact finite identity, with no independence or stochastic assumption.

Proof of sharpness. Work in H=R^2 with orthonormal e0,e1 and W=R. For a binary tensor coordinate i=(i1,...,iN), let k be the number of ones in its first p positions. Define T_i=0 unless there are exactly p ones in total. In that case set

    T_i = (-1)^k / binom(q,p-k).

This is nonzero and has the required two block symmetries. If a coordinate contains l ones in its first q positions (and p-l in its last p), averaging the first q positions gives

    (P_q T)_i = (1/b) sum_{k=0}^l
        binom(l,k) binom(q-l,p-k) (-1)^k / binom(q,p-k)
      = (-1)^l / (b binom(q,l)).                               (II)

For the last equality, the ratio of binomials in the summand is

    binom(q-l,p-k)/binom(q,p-k)
       = (q-p+k)_(falling l) / q_(falling l).

The l-th alternating finite difference of this monic degree-l polynomial in k is (-1)^l l!. Thus the sum is (-1)^l/binom(q,l). This also covers zeros at the ends through the falling-factorial convention.

Move T's first p positions to the final p positions and its q positions to the first q positions; call the resulting permutation RT. At the same coordinate, (RT)_i=(-1)^(p-l)/binom(q,l). Equation (II) says P_q T=(-1)^p RT/b. Since R preserves norm, ||P_qT||=||T||/b, proving sharpness. Embed R^2 into a larger H and tensor with a fixed unit vector of W to obtain the same equality in every indicated dimension.

## L2. Robust recovery and a negative control

Suppose T is symmetric in its first p positions only. Let Q average permutations of its next q positions, and let delta=||T-QT||. The projections on the two disjoint original blocks commute, so QT satisfies L1. The triangle inequality and contraction of P_q give

    ||T|| <= b ||P_qT|| + (b+1) delta.                         (III)

Indeed, ||T|| <= ||QT||+delta <= b||P_qQT||+delta, and ||P_qQT|| <= ||P_qT||+delta. The error coefficient in (III) is a valid bound; its optimality is not claimed.

Without the second block symmetry and without an error term, no finite recovery constant exists, even for p=1,q=2,H=R^2: T=(e0 tensor e1 - e1 tensor e0) tensor e0 is nonzero but P_2T=0. This is a counterexample to the weakened lemma, not to KLS.

## L3. Exact all-degree tilt norm for products of centered exponentials

Let Y1,...,Yn be independent Exp(1) random variables and Xi=Yi-1. Their joint law mu is isotropic and log-concave. For f in L2(mu), define F_f(z)=E[f(X)exp(<z,X>)]/E[exp(<z,X>)] near z=0, and T_d f=(1/d!)D^dF_f(0), in the ordered-index Hilbert--Schmidt norm. For every n >= 1 and d >= 1,

    ||T_d||_(L2(mu) -> HS) = sqrt(binom(2d-2,d-1)).            (IV)

Consequently ||T_d f|| <= 2^(d-1)||f||_2 for all d, and the universal base R=2 in ||T_df|| <= R^d||f||_2 is both sufficient and optimal for this family. This is a special case of the hardest input, not a proof for general log-concave mu.

The exponential product law is nonsmooth at the support boundary and is not regular in the sense assumed by BKL Theorem 3.1. The all-degree operator calculation is direct and does not invoke that theorem for this law.

Proof. For y >= 0 set P0(y)=1 and Pj(y)=y^j/j!-y^(j-1)/(j-1)! for j>=1. The one-coordinate tilt kernel is (1-z)exp(zy)=sum_{j>=0}Pj(y)z^j. It is analytic as an L2(Exp(1)) function for |z| sufficiently small (for real z, z<1/2 suffices); finite products justify differentiation and pairing with any L2 f. Using E[Y^m]=m!, direct expansion gives

    E[Pj(Y)]=0 (j>=1),
    E[Pj(Y)Pk(Y)]=binom(j+k-2,j-1) (j,k>=1),
    E[Pj(Y)^2]=B(j-1), where B(a)=binom(2a,a).

For a multi-index alpha of total degree d, put P_alpha(Y)=product_i P_(alpha_i)(Yi) and alpha!=product_i alpha_i!. The coefficient of z^alpha in F_f is <f,P_alpha>. There are d!/alpha! ordered tensor coordinates with that multiplicity, each equal to (alpha!/d!)<f,P_alpha>. Hence

    ||T_df||^2 = sum_{|alpha|=d} (alpha!/d!) |<f,P_alpha>|^2.    (V)

For different coordinate supports S={i:alpha_i>0}, the spans of P_alpha are orthogonal: independence lets one integrate a coordinate with Pj on one side and P0 on the other, yielding zero. This is an explicit product-law factorization, not a use of conditional independence.

Fix one support of size s<=d. The positive finite-rank frame operator for its terms in (V) has operator norm at most its trace, which is

    sum_(alpha_i>=1, sum alpha_i=d) (alpha!/d!)
       product_(i in S) B(alpha_i-1).

Vandermonde gives product B(alpha_i-1) <= B(d-s), since the product is one contribution to the central coefficient of (1+t)^(2(d-s)). Also alpha! <= (d-s+1)!: transferring a unit from any smaller positive part >1 to a largest part increases the factorial product, until all but one parts are 1. There are binom(d-1,s-1) positive compositions, so

    sum alpha!/d! <= binom(d-1,s-1)(d-s+1)!/d!
                    = (d-s+1)/(d(s-1)!) <= 1.

Thus the trace is <= B(d-s) <= B(d-1). Orthogonality across supports shows that the whole frame operator has norm <= B(d-1); it is a direct sum, so no factor equal to the number of supports occurs. This proves the upper bound in (IV).

Take f=P_d(Y1)/sqrt(B(d-1)). Its L2 norm is 1. Every term of (V) with a support containing another coordinate vanishes, and the unique term supported on {1} has squared magnitude B(d-1). This attains equality.

Finally B(d-1)<=4^(d-1), while B(d-1)>=4^(d-1)/(2d-1), as the largest coefficient among the 2d-1 coefficients of (1+t)^(2d-2). Taking (2d)-th roots proves that B(d-1)^(1/(2d)) tends to 2. Any single base R valid for all degrees must therefore be at least 2.

## L4. The second-degree obstruction in the full route

For a general centered isotropic probability mu with finite fourth moments, define the bounded quadratic-moment operator

    U_2f = (1/2) E[f(X)(X tensor X-I)].

If mu also has exponential moments in a neighborhood of zero, U_2 is the actual tilt Taylor operator T_2. Finite fourth moments alone need not define an exponential tilt near zero. The following identity only needs finite fourth moments:

Hilbert-space duality against symmetric matrices gives the exact norm identity

    ||U_2||_(L2 -> HS)
      = (1/2) sup_(A symmetric, ||A||_HS=1)
           sqrt(Var_mu(<AX,X>)).                              (VI)

Proof: pair the tensor with A, use Cauchy--Schwarz for the centered quadratic q_A-Eq_A, and interchange the two suprema defining the operator norm. Equality for each nonconstant quadratic uses f=(q_A-Eq_A)/sqrt(Var(q_A)); a zero-variance case contributes zero. The antisymmetric part of any matrix does not pair with X tensor X-I, so restricting to symmetric A loses nothing.

Thus even the d=2 universal tilt estimate requires a dimension-free quadratic-form variance estimate. The cited recent literature claims such an estimate, but its complete proof has not been audited here. L3 verifies it and every higher degree only for the independent exponential-product family. Isotropy alone, general convexity, source hashes, finite tests, or L1 do not justify replacing this missing analytic input by a universal theorem.

## Conditional route and one remaining gap

1. Under a universal all-degree Taylor bound with base R, use BKL Theorem 3.1 (externally supplied in this packet) to obtain C_P(mu)<=C R^2 for centered regular log-concave mu with Cov(mu)<=I.
2. L1--L2 rigorously control the tensor-recovery step under their precise block-symmetry hypotheses. L3 proves the all-degree bound with optimal R=2 for centered independent exponentials. L4 identifies the degree-two input exactly.
3. For the full target, the sole selected unresolved obligation is the universal all-degree bound for arbitrary regular log-concave mu; complete independent audit of the published cumulant/suspension route would be one way to discharge it. Nothing in this packet discharges it. Approximation to nonsmooth laws and the Cheeger comparison are also cited external steps if claiming the full target, and are not part of the proved special case.

NEXT: w350 checks L1 sharpness and the support-direct-sum step in L3; then an independent account audits the universal analytic input before any full KLS claim.
