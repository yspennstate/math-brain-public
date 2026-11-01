# Independent derivation checkpoint (2026-10-10)

Saved before reading w564's proof. C0029 is the iid uniform {-1,+1} n by n bound P(s_min(B)<=epsilon/sqrt(n)) <= epsilon + C exp(-c n), uniformly epsilon>=0 with fixed C,c>0. The primary 2025 result supplies (1+O((log n)^(-1/16)))epsilon + exponential error, which does not imply exact coefficient one.

Let A be a real (n-1) by n matrix of full row rank, with right singular vectors u_1,...,u_(n-1), positive singular values d_i, and a unit kernel vector v. For a new row X, put z_i=<X,u_i>, z_0=<X,v>, B=[A;X]. For 0<t<min_i d_i,

s_min(B)<=t iff z_0^2 <= t^2 (1+sum_i z_i^2/(d_i^2-t^2)).

Proof: in this orthonormal basis B^T B-t^2 I is diag(d_i^2-t^2,-t^2)+zz^T. Its top block is positive definite. Its Schur complement equals z_0^2/(1+sum_i z_i^2/(d_i^2-t^2))-t^2, by the rank-one inverse formula. Positive definiteness is equivalent to positive Schur complement, hence complementing gives the stated <= event including equality. At t=0, s_min(B)=0 iff z_0=0. If A has rank <=n-2 then B is singular. If A has full row rank and t>=min_i d_i then rank-one interlacing gives s_min(B)<=t automatically.

This reduction has no probability independence assumption. If A and X are independent Bernoulli rows, independence permits conditioning on A; it does not make z_0 and the random radius independent.

Remaining hardest input: an averaged upper bound by epsilon+exponential error for this dependent random-radius event (including the low-rank/low-d_i branch). It is unproved here. No parent conjecture solved claim.

Additional independent obstruction: for n=2^k, let H_n be the Sylvester Hadamard matrix (H_2=[[1,1],[1,-1]], H_(2m)=[[H_m,H_m],[H_m,-H_m]]). Delete its last row to obtain A. All n-1 positive singular values of A equal sqrt(n), and its unit kernel vector has every coordinate of absolute value 1/sqrt(n). Nevertheless, for an independent Rademacher row X, P_X(s_min([A;X])=0 | A)=binom(n,n/2)/2^n >=1/(n+1). The equality follows by counting the signs of <X,v>; the lower bound follows because the central binomial coefficient is the largest of the n+1 coefficients whose sum is 2^n. Hence a uniform conditional coefficient-one plus exponential-error bound fails even with optimal flatness and a large spectral gap. This particular ordered A occurs with probability 2^(-n(n-1)), so it does not refute the averaged conjecture.

Additional independent dependence counterexample: take the first three rows of H_4 as A, t=3/4, and X uniform in {-1,+1}^4. Let z=<X,v> with v the omitted row divided by 2. Then z^2 takes values 0,1,4 with probabilities 6/16,8/16,2/16. The exact squared radius is r_t(X)^2=9(119-16z^2)/880. Thus P(z^2<=r_t(X)^2)=7/8. Replacing X inside the radius with an independent X' gives P(z(X)^2<=r_t(X')^2)=13/16. Independent replacement UNDERestimates by 1/16. Orthogonal linear coordinates of X have zero covariance, yet the radius and z are dependent. Here epsilon=t*sqrt(4)=3/2; this refutes the general dependence inference, not a conjecture counterexample in its nontrivial epsilon range.

Additional independent quantifier obstruction: set delta_n=(log n)^(-1/16) and let F_n(epsilon)=min(1,(1+delta_n)*epsilon), epsilon>=0. This is the CDF of a uniform random variable on [0,1/(1+delta_n)] and satisfies the published-form upper bound with zero additive error. At epsilon_n=exp(-sqrt(n)), F_n(epsilon_n)-epsilon_n=delta_n*exp(-sqrt(n)) for all sufficiently large n. Its logarithm divided by n tends to zero, so no constants C,c>0 bound the excess by C exp(-c n). A multiplicative asymptotic coefficient alone does not imply the exact coefficient-one claim. This is a counterexample to a logical implication between bounds, not a Bernoulli-matrix counterexample.

NEXT: Run exact finite checks, freeze this independent checkpoint, then inspect the paired proof's corresponding step.
