# Independent finite LFPP derivation and obstruction

2026-10-10. Derived after reading w525/STATEMENT_FOR_ADVERSARY.md, before reading a proof or numerical validation from w525.

Let X be a centered finite Gaussian vector with positive semidefinite covariance C. Each path p in a finite nonempty family has at least one vertex and positive deterministic weights a_pv. Put f_p(y)=log sum_v a_pv exp(y_v), r_p=grad f_p, q_p=exp(-beta f_p)/sum_s exp(-beta f_s), and F_beta=-(1/beta)log sum_p exp(-beta f_p), beta>0. Path coordinates absent from p have r_pv=0. Fix 0<=a<b<infinity.

Each r_p is a probability vector. Direct differentiation gives H_p=diag(r_p)-r_p r_p^T and

grad F_beta = r_bar := sum_p q_p r_p,

Hess F_beta = sum_p q_p H_p - beta[sum_p q_p r_p r_p^T-r_bar r_bar^T].

For fixed beta all first and second derivatives are bounded. Differentiating E F_beta(xi X) is justified by the bounded gradient and E||X||<infinity. Write X=C^(1/2) Z with standard Gaussian Z, which also handles singular C. Gaussian integration by parts then gives

m_beta'(xi)=E[X dot grad F_beta(xi X)]=xi E[tr(C Hess F_beta(xi X))]=xi E[A_beta-beta B_beta].

The claimed signs hold:

A_beta = (1/2) sum_p q_p sum_ij r_pi r_pj (C_ii+C_jj-2C_ij) >= 0,

B_beta = sum_p q_p (r_p-r_bar)^T C (r_p-r_bar) >= 0.

The first summands are variances of X_i-X_j; the second are nonnegative quadratic forms. Coordinate independence is unnecessary.

For H(y)=min_p f_p(y), H-log|P|/beta <= F_beta <= H uniformly in y. Integrate the derivative first, then let beta tend to infinity. This proves

E H(bX)-E H(aX)=lim_beta integral_a^b xi E[A_beta-beta B_beta] dxi.

It does NOT prove that beta B_beta vanishes, that derivative limits exist pointwise at xi=0, or that a network-size limit can be exchanged with beta without a bound uniform in network size.

For the variance transfer, write log D_xi=H(xi C^(1/2)Z). Each path gradient in Z coordinates has squared norm xi^2 r_p^T C r_p <= xi^2 v, v=max_i C_ii, since |C_ij|<=v and sum_i r_pi=1. Each f_p(xi C^(1/2)Z), and hence their minimum, is xi sqrt(v)-Lipschitz. Gaussian Poincare applies to this Lipschitz function, even at ties, and gives Var(log D_xi)<=xi^2 v. If M is any median, |E log D_xi-M|<=sqrt(2 Var). Therefore v_n=O(L_n), L_n tending to infinity, and fixed xi imply that mean/L_n and median/L_n have the same limit whenever one exists.

Tie control: two singleton paths, unit weights, independent standard normal X_1,X_2. H(xi X)=xi min(X_1,X_2) for xi>=0, so E H(xi X)=-xi/sqrt(pi). A_beta is exactly zero, while B_beta=2q_1q_2. For fixed xi>0, beta xi E[2q_1q_2] tends to 1/sqrt(pi). At xi=0 every smooth derivative m_beta'(0) equals zero, whereas the hard-min right derivative is -1/sqrt(pi). Thus the B term survives ties and the endpoint derivative limit fails.

Uniformity obstruction C526.5: for integer n>=1 take L_n=n and N_n=2^(n^2) singleton paths. All coordinates X_i equal the same N(0,1) variable Z, so C is the PSD all-ones matrix and v_n=1. All weights equal one. Then H(xi X)=xi Z and F_beta(xi X)=xi Z-(n^2 log 2)/beta. Hard-min mean/L_n and median/L_n are zero. Yet choosing beta_n=n, which tends to infinity, yields soft-min mean/L_n=-log 2. This exactly realizes the log|P_n|/(beta_n L_n) error. A sufficient missing premise for transferring a soft-min asymptotic to the hard minimum is log|P_n|/(beta_n L_n) -> 0, or a separately proved stronger effective-entropy estimate. This counterexample satisfies w525's finite assumptions; it is not claimed to be a two-dimensional LFPP network. Its bias is independent of xi and cancels in endpoint differences: C526.5 alone is not a counterexample to the integrated difference reduction.

Stronger integrated counterexample C526.6: set L_n=beta_n=n and M_n=2^(n^2). Take M_n distinct singleton paths with deterministic centered Gaussian field zero and vertex weight exp(n). Also take one long path containing M_n independent fields sqrt(n) Z_i, Z_i standard normal, each with weight 1/M_n. This is a finite Gaussian path family with PSD diagonal covariance and v_n=n=O(L_n). Write S_n(xi)=(1/M_n) sum_i exp(xi sqrt(n) Z_i) and f_n(xi)=log S_n(xi). The hard log minimum is H_n(xi)=min(n,f_n(xi)). The soft minimum at beta_n=n is exactly

F_n(xi)=-(1/n)log(exp[-n^2(1-log 2)]+exp[-n f_n(xi)]).

At xi=0, f_n=H_n=0 and F_n(0)/n tends to zero. At xi=2, E S_n=exp(2n) and Var(S_n)/(E S_n)^2=(exp(4n)-1)/M_n. Chebyshev therefore gives

P(S_n(2)<exp(n)) <= (exp(4n)-1)/[M_n(1-exp(-n))^2] -> 0.

Jensen gives f_n(2)>=2 sqrt(n) Z_bar, with E|2 sqrt(n) Z_bar|=2 sqrt(2n/(pi M_n)). For any fixed c>0, on the event S_n(2)>=exp(n), min(c n,f_n(2))=c n whenever c<=1. Consequently

0 <= c n-E min(c n,f_n(2)) <= c n P(S_n(2)<exp(n))+2 sqrt(2n/(pi M_n)).

Use c=1 for H_n(2), giving E H_n(2)/n -> 1. Use c=1-log 2 (strictly between zero and one) for F_n(2), which differs from min(c n,f_n(2)) by at most log 2/n, giving E F_n(2)/n -> 1-log 2. The hard-min medians at xi=0 and xi=2 are exactly 0 and n for all sufficiently large n, since H_n(2)=n with probability tending to one.

Thus the normalized endpoint differences on [0,2] tend to 1 for the hard minimum and 1-log 2 for the soft minimum. By the exact fixed-n interpolation identity, the latter is also the normalized integrated response. This is a direct counterexample to removing uniform smoothing control from the conditional integrated reduction, even with the claimed covariance growth and convergent hard-min median exponents. It meets the general finite assumptions, but is not asserted to be a planar LFPP discretization. No exponentially large network was materialized or sampled; the argument is analytic. Independent check by w527 is pending.

Verdict on the statement packet: the finite identities and fixed-xi variance transfer are derivable. The hardest remaining bridge is the numerical value of the actual scale-normalized integrated A_beta-beta B_beta term in LFPP, with smoothing error uniformly controlled as the mesh vanishes. No claim to evaluate d_gamma.

NEXT: Compare w525's proof and asymptotic use with the independent derivation and the diagonal soft-min obstruction; referee w527 checks this packet.
