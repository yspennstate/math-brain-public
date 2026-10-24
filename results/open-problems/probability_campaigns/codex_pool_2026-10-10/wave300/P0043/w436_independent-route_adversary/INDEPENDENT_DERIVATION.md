# A bounded-degree critical-survival obstruction (before reading the paired proof)

Saved 2026-10-10. This is an elementary boundary example, not a counterexample to P0043 and not a claimed new theorem. No artifact from w435 or the core-proof lane has been read.

Construct a rooted spherically symmetric tree T. Each vertex at level n-1 has b_n children, where b_n=8 if n is a power of two and b_n=2 otherwise (n>=1). This is an infinite connected locally finite simple graph of maximum degree 9. The root has degree 8 and every other vertex has degree 3 or 9. Thus the root is the unique vertex of degree 8; every automorphism fixes it, and distinct distance levels give infinitely many orbits. T is not quasi-transitive.

For n>=1 put m(n)=1+floor(log_2 n). The generation size is |T_n|=2^n 4^{m(n)}. For Bernoulli bond percolation with parameter p let Z_n count root-connected vertices at level n and M_n=E_p Z_n=|T_n|p^n. Since 4^{m(n)}<=4n^2, if p<1/2 then M_n<=4n^2(2p)^n tends to zero. Markov's inequality and continuity for the decreasing events {Z_n>0} give P_p(root connects to infinity)=0. Any infinite cluster has a vertex at minimum distance from the root and therefore an infinite downward subtree. The same first-moment bound starting at each fixed vertex and countability exclude all infinite clusters for p<1/2.

At p=1/2 we have M_n=4^{m(n)}, M_0=1. Given the exploration through generation n-1, the offspring of the Z_{n-1} discovered vertices use disjoint fresh edges and are independent Binomial(b_n,p). Therefore

E[Z_n^2 | F_{n-1}] = (b_n p)^2 Z_{n-1}^2 + b_n p(1-p) Z_{n-1}.

The justified conditional second-moment recurrence, after expectation and division by M_n^2, is

R_n := E Z_n^2 / M_n^2 = R_{n-1} + (1-p)/M_n,

so R_n=1+(1-p) sum_{j=1}^n 1/M_j. Each block 2^k<=j<2^{k+1} has M_j=4^{k+1}; consequently sum_{j>=1}1/M_j=sum_{k>=0}2^k/4^{k+1}=1/2. At p=1/2, R_n<=5/4. Cauchy-Schwarz gives P(Z_n>0)>=M_n^2/E Z_n^2>=4/5. By local finiteness (Koenig's lemma) and continuity for decreasing events, theta_T(1/2)>=4/5. Hence p_c(T)=1/2 and critical survival is strictly positive.

The event that some infinite cluster exists is unchanged by changing finitely many edges: splitting an infinite locally finite cluster along finitely many edges leaves an infinite component, while merging finitely many finite clusters keeps it finite. Kolmogorov's zero-one law therefore upgrades its positive probability to probability one at p=1/2.

Audit consequence: bounded degree, independence, exponential rate lim |T_n|^{1/n}=2, and p_c<1 do not force critical extinction. A proof based only on these facts needs a further premise that rules out this tree. In particular quasi-transitivity cannot be silently replaced by bounded degree. The hardest P0043 step remains deriving an appropriate structural premise from quasi-transitivity in the general amenable case.

Independent mathematical review by w437 is pending. Arithmetic checks will corroborate the displayed recurrence and exact block sum; they are not a proof of the full conjecture.
