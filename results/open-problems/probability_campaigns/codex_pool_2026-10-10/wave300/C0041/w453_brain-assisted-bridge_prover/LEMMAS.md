L1. A bound from spatial range to elapsed time, including random times that are not stopping times (own conditional result; independent review pending).

Let X be a nearest-neighbor walk on Z^d, d>=1, in any fixed environment with every transition probability at least kappa, where 0<kappa<=1/(2d). Start at 0. Let T be ANY N union {infinity}-valued random variable on the path probability space (additional randomness is allowed), and let R_T=sup_{0<=n<=T} ||X_n||_infinity. For every integer r,t>=0, with m=r+1,

  P_(0,omega)(T>t) <= P_(0,omega)(R_T>r) + (1-kappa^m)^floor(t/m).

The same inequality holds annealed in any law of such environments. No independence between T, R_T, and omega is assumed. If P denotes either original law and A is ANY event with alpha=P(A)>0, the conditional form is

  P(T>t | A) <= P(R_T>r | A) + alpha^(-1)(1-kappa^m)^floor(t/m).

This does not assert a uniform ellipticity bound for the walk under P(.|A).

Proof. Let sigma_r be the first exit from [-r,r]^d. From any point x inside the box, take consecutive steps along coordinate 1 in the sign of x_1 (positive when x_1=0). This exits in r+1-|x_1|<=m steps with conditional probability at least kappa^m. At each deterministic time jm, conditional on the path up to jm in the fixed environment, the chance of exiting in the next m steps is at least kappa^m on {sigma_r>jm}. Iterated conditional expectation gives P_(0,omega)(sigma_r>jm)<=(1-kappa^m)^j. This is a conditional bound at successive blocks, not multiplication of independent events. The pathwise inclusion {T>t,R_T<=r} subset {sigma_r>t} gives the result. Integrate over the environment for the annealed version. For the conditional form, intersect that same inclusion with A, drop A only from the box-exit term, and divide the resulting probability bound by alpha. No Markov or fresh-environment property under P(.|A) is invoked. Notice that no stopping property of T was used.

L2. A sufficient quantitative range condition for an integrable clock (proved special case; independent review pending).

In L1's setup suppose under the original law P, or under P(.|A) for a specified event A of positive P-probability, that the spatial-range tail is at most C exp(-lambda r) for all integers r>=0, with finite C and lambda>log(1/kappa). Then the expectation of T under that same law is finite. Use the original-law box tail in both cases; the conditional case includes alpha^(-1).

Proof. Choose a with 1/lambda<a<1/log(1/kappa), and put r=floor(a log(t+1)). The range term is at most C exp(lambda)(t+1)^(-lambda a), a summable sequence. For sufficiently large t, floor(t/(r+1))>=t/(2(r+1)); and kappa^(r+1)>=kappa(t+1)^(-a log(1/kappa)). Thus the remaining term in L1 is at most exp(-c t^(1-a log(1/kappa))/log(t+1)) for some c>0, also summable. In the conditional case multiply only that summable box term by the finite constant alpha^(-1). Finally use the tail-sum identity under the relevant law by Tonelli. All constants are explicit except the harmless finite initial segment.

Application to C0041: take T=tau_1, the first directional regeneration time, P=P_0, and A={D=infinity}, with D=inf{n>=0:X_n.l<0}. In the standard renewal construction P_0(A)>0 under directional transience. L1's conditional form is applicable even though tau_1 depends on the infinite future. Directional transience supplies finite tau_1 and hence finite R_(tau_1) almost surely; it supplies no exponential range tail under P_0 or P_0(.|A). A sufficiently fast range tail under the conditional law would imply finite E_0[tau_1|D=infinity] by L2. L2 is therefore a conditional bridge, not a solution of C0041. In particular lambda>log(1/kappa) is an added hypothesis and is not claimed to follow from (T'), let alone from transience. A weaker spatial tail might still give integrability by a sharper, dimension-sensitive argument; L1 does not exclude that.

SINGLE HARDEST GAP: deduce finite mean regeneration duration from only d>=2, i.i.d. site rows, uniform ellipticity, and almost-sure directional transience. The particular range route above leaves the stronger sufficient bound P(R_(tau_1)>r)<=C exp(-lambda r), lambda>log(1/kappa), entirely unproved. No claim that this stronger bound is necessary is made.

L3. Uniform ellipticity and an unspecified exponential spatial tail do not suffice for a general random clock (own countermodel; independent review pending).

On Z set omega(x,+1)=1/4 for x>0, 3/4 for x<0, and 1/2 for x=0; use the complementary probability for -1. This fixed environment is uniformly elliptic with kappa=1/4. Independently select a positive integer R with P(R=r)=2^(-r), r>=1. Let T be the first exit from [-R,R], with R available at time zero. Then T is a stopping time in the enlarged filtration and is finite almost surely. Its path range R_T=R+1 has an exponential tail and every finite polynomial moment, but E[T]=infinity.

Proof. For a fixed r, |X| is a birth-death chain on {0,...,r+1}: from zero it moves to one, and at positive states it moves outward with probability 1/4 and inward with probability 3/4. Let u_i be the finite mean hitting time of r+1 from i (finiteness follows directly from L1's box bound), and delta_i=u_i-u_(i+1). The first-step equations give delta_0=1 and delta_i=4+3 delta_(i-1), whence delta_i=3^(i+1)-2. Thus

  E[T | R=r] = u_0 = (3/2)(3^(r+1)-1)-2(r+1).

Summing against 2^(-r) diverges. Meanwhile R_T=R+1, so P(R_T>r)=2^(1-r) for integers r>=1 and P(R_T>0)=1. This proves the assertion.

Scope: this is NOT a counterexample to C0041. The environment is not i.i.d. across sites, the walk is not directionally transient, d=1, and T is a random-box exit time, not a directional regeneration time. It refutes only the dimension-blind rule 'uniform ellipticity plus some exponential range tail implies a finite mean random clock.' It also explains why a numerical tail exponent is a load-bearing assumption in L2.
