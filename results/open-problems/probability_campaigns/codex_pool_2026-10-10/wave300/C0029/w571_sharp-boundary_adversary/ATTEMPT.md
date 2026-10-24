# C0029 independent sharp-boundary derivation

Saved before reading any paired prover proof, 2026-10-10.

The target is an iid Rademacher square matrix, with unnormalised entries of variance one. The primary 2025 manuscript, arXiv:2405.20308v2, equation (2), states the coefficient-one bound for every epsilon >= 0; Theorem 1.1 gives coefficient 1+O_xi((log n)^(-1/16)). Recovering the original 2002 formulation and local prior records is still in progress.

## Boundary B01: exact two-dimensional distribution

For M in {-1,1}^{2x2} with independent uniform entries, its two columns are proportional with probability 1/2. Otherwise they are orthogonal, each of norm sqrt(2). Thus sqrt(2)*s_min(M) is zero or two, each with probability 1/2. Its CDF equals 1/2 on [0,2) and one on [2,infinity). This checks the closed endpoint convention and shows why a singularity remainder is indispensable. It is not a novelty claim.

## Bridge obstruction B02: multiplicative universality does not remove its own error

Define H(t)=1-exp(-t-t^2/2) for t>=0, the real Gaussian hard-edge limiting CDF. Independently of that interpretation, H is a valid explicit CDF. Its derivative g(t)=(1+t)exp(-t-t^2/2) is nonnegative, and g'(t)=-t(t+2)exp(-t-t^2/2)<=0. Therefore H is concave, H(0)=0, and H(a*t)<=a*H(t) for a>=1.

Also (t+2)exp(-t-t^2/2)<=2: its logarithmic derivative 1/(t+2)-1-t is negative and its value at zero is two. Consequently -g'(t)<=2t, g(t)>=1-t^2, and H(t)>=t-t^3/3 for every t>=0.

For n>=1 set delta_n=(log(n+e))^(-1/16), p_n=exp(-n), and

    F_n(t)=p_n+(1-p_n) H((1+delta_n)t), t>=0;
    F_n(t)=0, t<0.

This is a genuine CDF with atom p_n at zero. For all t>=0,

    H(t) <= F_n(t) <= (1+delta_n)H(t)+p_n.

Thus it has an exponentially small singular atom, the same limiting CDF H, and a uniform two-sided relative comparison error at most delta_n plus an exponential additive error.

Nevertheless, at t_n=sqrt(delta_n)/2, since 0<delta_n<1,

    F_n(t_n)-t_n
      >= H((1+delta_n)t_n)-t_n
      >= delta_n^(3/2) [1/2-(1+delta_n)^3/24]
      >= delta_n^(3/2)/6.

The last lower bound is (log(n+e))^(-3/32)/6, which is not bounded by C exp(-c n) for any fixed positive C,c for all sufficiently large n. Hence even a uniform multiplicative comparison to the Gaussian limiting CDF, plus the correct size of the atom and the correct weak limit, cannot logically imply an exact coefficient-one bound with exponential remainder.

Scope: F_n is a synthetic scalar distribution, not the least-singular-value law of an iid Rademacher matrix. This disproves only the abstract transfer implication. It does not disprove Theorem 1.2's comparison with the finite-n Gaussian law, nor C0029. A Rademacher-specific sign or exponentially small excess estimate remains necessary.

## Bridge obstruction B03: full row rank and perfect flatness leave an atom

Let n>=2 be even. The balanced sign rows (each has exactly n/2 positive entries) span the hyperplane V={x:sum x_i=0}. Indeed, for every i!=j choose a set S of n/2-1 coordinates excluding i,j. The sign rows positive on S union {i} and S union {j} differ by 2(e_i-e_j). These differences span V. Hence one can select n-1 linearly independent balanced sign rows as a deterministic (n-1)x n matrix A. It has rank n-1 and unit kernel vector v=(1,...,1)/sqrt(n), with the smallest possible infinity norm 1/sqrt(n).

For an independent iid Rademacher row X, dist(X,rowspan(A))=|<X,v>|. At zero its small-ball probability is

    P_X(dist(X,rowspan(A))=0)=binom(n,n/2)/2^n.

This atom is at least 1/(n+1), because the central binomial coefficient is the largest of n+1 coefficients whose sum is 2^n. It cannot be bounded by C exp(-c n) for any fixed C,c>0 as n tends through even integers. Thus neither full row rank nor perfect coordinate flatness suffices for a pointwise conditional Gaussian small-ball bound at exponential scales.

Concrete n=4 witness:

    A = [[1,1,-1,-1], [1,-1,1,-1], [1,-1,-1,1]].

Its Gram matrix AA^T is 4I_3, its kernel vector is (1,1,1,1)/2, and exactly 6 of the 16 possible rows X have zero projection. This is a legitimate iid sign-matrix row-block realization, with probability 2^(-12) for this one ordered block. No multiplication of conditional bounds is used.

Scope: this refutes a conditional bound asserted uniformly over all full-rank flat row blocks. These row blocks can be rare, so it does not refute an averaged estimate or C0029. The missing premise must control additive/arithmetic structure of v or the weighted probability of bad row blocks. No claimed novelty.

Independent review: pending w572. Numerical cross-check: pending. No parent-problem solved or novelty claim.

## Source correction B04: the hard-edge limit is not the finite-n Gaussian CDF

The local C0029-A001 attempt and exported attempt claim cbd6e1bc44ea67c88a3ad2112abab63bbfcf63f991be2eeccb063fdba514f1fa state the Gaussian identity without an n->infinity limit. This wording is false for finite n. For n=1 the scaled least singular value is |Z|, Z standard normal. Its CDF is erf(t/sqrt(2)), with right derivative sqrt(2/pi) at zero, whereas H(t)=1-exp(-t-t^2/2) has right derivative one. At t=1 these are approximately 0.6826894921 and 0.7768698399.

Correct the identity to the limiting law as n tends to infinity. Keep the separate finite-n Gaussian upper bound P(sqrt(n)*s_min(G_n)<=t)<=t and keep the finite-n Gaussian CDF in comparisons such as Theorem 1.2. The explicit formula H must not silently replace that finite-n CDF.

## Paired prover read and adversarial findings

After saving B01-B03 independently, read w570/ATTEMPT.md. P1-P4 concern projective collisions and a noncolliding singular construction, so our flat-normal and scalar-CDF obstructions are disjoint. P1's row/column joint probability correctly accounts for dependence. P4's T block has rank three and kernel (1,-1,-1,1); adjoining identity blocks and a border proves its stated corank-one obstruction. No coefficient-one complement estimate is supplied, and w570 explicitly records that gap.

One boundary premise needs stating: P2's support-at-most-two witness equivalence for 0<=epsilon<sqrt(2n) requires n>=2. For n=1, B=[1] and epsilon=1 satisfy the interval and have a one-coordinate witness, despite no column-pair collision. This does not affect P2's collision formula or P3/P4, which have their own valid n ranges.

NEXT: Obtain the source's explicit limiting-law statement, finish the scoped w570 audit and draft bundle, and leave the coefficient-one complement gap for independent review.
