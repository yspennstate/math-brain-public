# P0288: recheck of the existing killed-walk candidate

Status: a proof and independent recheck of an existing campaign candidate, pending w347. This is not a novelty or literature-status certificate. The cached primary source is Phil Pollett, *Quasi-stationary distributions for queueing and other models*, arXiv:2202.05428 (2022), Section 2. Its conjecture (ii) is the rank-one assertion. Foley and McDonald, *Yaglom limits can depend on the starting state*, arXiv:1709.07578v1, 22 September 2017, is the existing prior-art lead; its cached abstract concerns a discrete R-transient example, not this continuous-time formula.

On the transient labels Z, jump to each nearest neighbor at rate one, kill at rate kappa>0 everywhere and at extra rate v>0 at lattice zero, into a separate cemetery state. The full generator is conservative, bounded-rate, nonexplosive and has an irreducible transient class. Uniform killing ensures almost sure absorption. Put K=-Delta+v|0><0|, where Delta f(i)=f(i+1)+f(i-1)-2f(i); then p_t(i,j)=exp(-kappa t)<delta_i,exp(-tK)delta_j>.

For s>0, set D=sqrt(s(s+4)) and r=(s+2-D)/2. The free resolvent is r^|i-j|/D: substitution in its second-order recurrence and decay at both ends determine it. The rank-one perturbation identity gives

R_s(i,j)=[r^|i-j|-v r^(|i|+|j|)/(D+v)]/D.

Write a=|i-j|, b=|i|+|j| and q=sqrt(s). Expanding D=2q+q^3/4+O(q^5), log r=-q+q^3/24+O(q^5), and v/(D+v)=1-2q/v+4q^2/v^2+O(q^3), gives

R_s(i,j)=(b-a)/2+1/v-L_ij sqrt(s)+O(s), where L_ij=(b^2-a^2)/4+b/v+2/v^2=max(ij,0)+(|i|+|j|)/v+2/v^2.

For rigor in passing to time, use the explicit spectral boundary values rather than an off-diagonal Tauberian claim. At s=-E+i0 for 0<E<4, D=i sqrt(E(4-E)), r=1-E/2-i sqrt(E(4-E))/2. Near zero the boundary value is analytic in sqrt(E), so Stieltjes inversion gives spectral density (L_ij/pi) sqrt(E)+O(E^(3/2)). There is no atom at zero because sR_s(i,j) tends to zero. The remainder of the finite spectral measure, supported above any fixed positive epsilon, contributes exponentially little. Laplace integration of the density therefore gives

lim_{t->infinity} t^(3/2) exp(kappa t) p_t(i,j)=C_ij=L_ij/(2 sqrt(pi)).

In particular, C_ij is strictly positive, the decay parameter is lambda=kappa, and the integrated exp(lambda t) kernel is (b-a)/2+1/v, which is finite. Thus the chain satisfies the source's lambda-transience and absorption hypotheses. Define h_+(i)=max(i,0)+1/v and h_-(i)=max(-i,0)+1/v. These are distinct positive K-harmonic functions and L_ij=h_+(i)h_+(j)+h_-(i)h_-(j). The leading kernel has rank exactly two; its minor on labels {0,1} is 1/(4*pi*v^2)>0. No rank-one factorization can have that minor.

Independent checks: checks.py evaluated 784 resolvent recurrences in exact fractions, 72 harmonic recurrences and four exact rank/minor checks. Independent integration of the spectral density at t=20,80,320 gave maximum absolute errors 0.06132234, 0.01689538, 0.00433960 against the scaled limits. These numerical results support, rather than replace, the spectral proof. A proof audit must check the branch convention, absence of a zero atom, signed off-diagonal inversion, positivity, and all source hypotheses. Novelty remains unestablished.

Local primary passages: Downloads/Probability_1000_20h_20260906/sources/queues_qsd_pollett_2022/text.txt:15-32,122-127; prior-art abstract: sources/foley_mcdonald_yaglom_2017/text.txt:3-16. Existing brain target: math:probability.open-problems:p0288-pollett-rank-two-limit-kernel-refuted, whose current title says CANDIDATE REFUTATION.
