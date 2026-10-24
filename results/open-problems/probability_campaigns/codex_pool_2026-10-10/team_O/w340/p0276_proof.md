# P0276: checking the previously proposed Abelian Cayley construction

Label: proof of the explicitly stated construction, pending w346 and exact source-scope reconciliation. The original candidate was already in the campaign; this is a reconstructed proof, not a claim of priority or an audited solution of the source question.

For integer d tending to infinity, put N=2^d, m=max(2,floor(N log(d)/4)), and D=d(m-1)+N-1. On the Abelian group (Z/2Z)^d times Z/mZ, use the symmetric generator set

S={(e_i,a): 1<=i<=d, a!=0} union {(h,0): h!=0}.

The sets are disjoint, have no identity, contain no repetitions, and are closed under inversion. They generate the group: all (h,0) are available, and (e_i,a)+(e_i,0)=(0,a). The resulting graph is simple, connected, undirected, unweighted, and D-regular. Consider its continuous-time simple random walk with rate one.

Write alpha=d(m-1)/D and gamma=N/D. The cube projection is the sum of independent coordinate-flip dynamics at total rate alpha and jumps uniformly to a different cube point at rate (N-1)/D. The latter generator equals gamma(Pi-I), where Pi is uniform averaging, and commutes with coordinate flips. Consequently

Law(cube at t)=exp(-gamma t) Q_(alpha t)+(1-exp(-gamma t)) pi_cube,

where Q_u is rate-one coordinate-flip walk on the d-cube from the origin. Its distance from uniform is exactly exp(-gamma t) d_cube(alpha t).

The auxiliary coordinate changes only at coordinate-flip events. Conditional on their number k and on every cube increment, its k increments are independent uniform nonzero elements of Z/mZ. For k>=1 the distance of their sum from uniform is (m-1)^(1-k)/m <= 1/m; this follows by Fourier inversion, since every nontrivial auxiliary Fourier coefficient equals (-1/(m-1))^k. For k=0 its distance is at most one. Since k is Poisson(alpha t),

0 <= d_full(t)-exp(-gamma t)d_cube(alpha t) <= exp(-alpha t)+1/m.

The lower bound is projection; the upper bound compares the joint distribution with the product of its cube marginal and auxiliary uniform law, conditioning on the entire cube event history. This handles possible dependence between the two coordinates.

For a cube character of Hamming weight k and an auxiliary character j, the eigenvalues of I-P are:

* 0 for k=0,j=0;
* [2k(m-1)+N]/D for k>=1,j=0, multiplicity binomial(d,k);
* dm/D for k=0,j!=0, multiplicity m-1;
* [dm+N-2k]/D for k>=1,j!=0, multiplicity (m-1)binomial(d,k).

These exhaust Nm characters. The nonzero minimum is asymptotic to 2/d; the auxiliary eigenvalues tend to one. Therefore t_rel is asymptotic to d/2.

For coordinate flips, each spin has mean exp(-2u/d), independently. Its chi-square distance is (1+exp(-4u/d))^d-1. Thus at u=s d log(d)/4 it tends to zero for s>1. For s<1 the magnetization has mean d exp(-2u/d) and variance at most d, while its stationary mean is zero and variance d. Chebyshev's inequality at half its mean gives d_cube(u)>=1-8/(d exp(-4u/d)), which tends to one. The same conclusions hold with u=alpha s d log(d)/4 because alpha=1-O(1/(d log d)).

Put T=d log(d)/4. Then gamma T tends to one and alpha T tends to infinity. The full distance therefore converges to exp(-s) for 0<s<1 and to zero for s>1. No value at s=1 is needed. Monotonicity and bracketing on either side of the thresholds show

t_mix(3/4)/T -> log(4/3), and t_mix(1/4)/T -> 1.

Hence t_mix(3/4)/t_mix(1/4) tends to log(4/3), rather than one, whereas t_mix(1/4)/t_rel is asymptotic to log(d)/2 and diverges. This family has the spectral product condition and no total-variation cutoff for rate-one continuous-time simple random walk. The precise source may restrict its generating sets or use another convention; check that scope before describing P0276 as answered.
