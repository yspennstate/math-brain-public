# L4: a sharper sufficient input, not the universal conjecture

Author w552, 2026-10-10. Independent referee w554, pending. This reconstructs a standard nonbacktracking path bound; novelty is not asserted.

Let G be an infinite connected simple d-regular graph, d>=3. Put b=d-1, A its adjacency operator and alpha=||A||_2. Define beta=sqrt(b) if alpha<=2 sqrt(b), and beta=(alpha+sqrt(alpha^2-4b))/2 otherwise. For Bernoulli bond percolation and 0<=p<1/beta,

||T_p||_2 <= (1-p^2)/(1+b p^2-alpha p).

In particular, on a Cayley graph, the strictly stronger input p_c beta<1 supplies the finite critical bound required by ATTEMPT.md L3. This is only a sufficient input; nonamenability by itself has not been shown to supply it.

Proof. Let B_n(x,y) count length-n nonbacktracking walks from x to y. B_0=I, B_1=A, B_2=A^2-dI. For n>=3, B_n=A B_{n-1}-b B_{n-2}: after prepending one edge, the unwanted immediate reversal has b choices once the next edge of the remaining walk is fixed. For n=2 it instead has d choices, which explains the separate initial term. Every finite self-avoiding path is nonbacktracking. Union bounding the OPEN SELF-AVOIDING paths (whose n distinct edges have probability p^n) and then increasing their counts to B_n gives T_p(x,y)<=sum_{n>=0} p^n B_n(x,y). Repeated-edge walks are never assigned probability p^n as percolation events.

To justify convergence in operator norm, set R_0=I, R_1=A and R_n=A R_{n-1}-b R_{n-2}. Then B_n=R_n-R_{n-2} for n>=2. For each real lambda in the spectrum of A, let z_+,z_- solve z^2-lambda z+b=0. Both roots have modulus at most beta: in the complex-root case their modulus is sqrt(b), and in the real-root case the maximum over |lambda|<=alpha is bounded by the displayed beta. The polynomial identity R_n(lambda)=sum_{j=0}^n z_+^{n-j} z_-^j remains valid when the roots coincide. Hence ||R_n||<=(n+1)beta^n, and the B_n series converges whenever p beta<1.

Multiply its norm-convergent generating series by I-pA+b p^2 I, using the recurrence and the exceptional B_2 term. The result is (1-p^2)I, so

sum p^n B_n = (1-p^2)(I-pA+b p^2 I)^{-1}.

The denominator is positive on the spectrum for p<1/beta. Its minimum is at the maximal spectral value, which is at most alpha; thus the norm is at most (1-p^2)/(1+b p^2-alpha p). Nonnegative entries and |f| dominate T_p quadratic forms by this bounded kernel. This proves the norm bound. Substitute p=p_c under the explicit strict assumption p_c beta<1, then use ATTEMPT.md L3.

## Proved regular-tree calibration

For the infinite d-regular tree, alpha=2 sqrt(b). For the upper bound, orient the tree toward a fixed end: every vertex has one parent and b children. The inequality 2|f(parent)f(child)| <= b^{-1/2}f(parent)^2+b^{1/2}f(child)^2, summed over edges, gives ||A||<=2 sqrt(b). For the reverse bound, fix a root and use f_N(x)=b^{-dist(root,x)/2} within its radius-N ball, zero elsewhere. Its squared norm is 1+(d/b)N and its adjacency quadratic form is (2d/sqrt(b))N, whose quotient tends to 2 sqrt(b).

On a tree B_n(x,y)=1_{dist(x,y)=n}, so the union bound is exact: T_p(x,y)=p^{dist(x,y)}. Since the spectrum has supremum alpha (by the preceding Rayleigh quotients), the resolvent norm above is exact for p<1/sqrt(b). Branching-process survival gives p_c=1/b. Therefore

M_c = (1-b^{-2})/(1-b^{-1/2})^2 < infinity, for every d>=3.

The elementary adjacency-walk condition p_c alpha<1 works only when d>=6. The nonbacktracking condition p_c beta=1/sqrt(b)<1 works for all d>=3, including d=3,4,5. This is an analytic proof for the infinite family; a finite numerical comparison merely evaluates its constants.

## Why the full target is still missing

For a nonamenable d-regular Cayley graph, alpha<d, so beta<d-1. However this does not itself upper-bound p_c by 1/beta. The general lower bound p_c>=1/(d-1) points the other way. Supplying a universal estimate p_c beta<1 would discharge this sufficient route, but is neither proved here nor asserted equivalent to C0047. The single hardest input for the broader L1-L3 route remains the uniform critical operator bound M_c<infinity.
