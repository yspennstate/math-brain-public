# C0120: independent boundary work and adversarial audit

The recovered source concerns the maximum M_n of sums of iid standard Gaussian vertex weights over all n-vertex up/right paths from the origin in the plane, with free endpoint. The operational power goal is Var(M_n)<=C n^(1-epsilon), for some fixed 0<epsilon<1 and all n>=2. The precise question, locators, and short source quote are recorded in SOURCE_STATUS.json. Current openness and novelty are UNKNOWN. No parent solution is claimed.

## Independent work before the paired proof

INDEPENDENT_BOUNDARY_20261010.md and INDEPENDENT_ZERO_TEMPERATURE_20261010.md were saved before w498's ATTEMPT.md was read. The Gaussian layer-average decomposition gives exactly Var(M)=sum_t 1/m_t+Var(M(residual)), when each deterministic path uses one site from each finite layer of independent unit Gaussians. For the source convention m_t=t+1, t=0,...,n-1, this gives the floor H_n. A fixed-width restriction has a linear variance floor. The normalized positive-temperature functional has the same floor; unnormalized log Z has beta^2 times that floor. Eighty arithmetic checks verify the factorization, not the mathematical proof or parent conjecture.

## Audit of w498's most consequential step

w498 L1/L1M: KEEP for the stated Gaussian layered domain. All means are independent of the entire residual vector by joint Gaussianity and zero cross-covariance. Independence across layers is explicit; no conditional per-row multiplication occurs. Finite maxima and log-sum-exp have finite second moments. H_n uses n vertices including the origin.

w498 L2: KEEP for the diagonal strip |x-y|<=1 from (0,0) to (r,r). There are r+1 forced diagonal sites and r independent two-site choices. For iid X,Y, max(X,Y)=(X+Y)/2+|(X-Y)/2|, with independent N(0,1/2) terms. Its variance is 1-1/pi; hence total variance is (2-1/pi)r+1. This does not provide a variance comparison for unrestricted paths.

w498 L3: KEEP for its expressly limited auxiliary implication. For OU correlation rho=e^(-s), the Gaussian angle argument gives q=arccos(rho)/pi. The original/perturbed pairs for distinct diamonds use disjoint Gaussian variables, so B~Binomial(r,q) is justified unconditionally. Vertex overlap is 2r+1-B; equality probability is (1-q)^r. For s=r^(-alpha), 0<alpha<2, rq tends to infinity and q tends to zero. Thus path replacement with high probability and overlap fraction tending to one coexist. Integrating actual expected overlap against e^(-s) gives (2r+1)-r/pi, because integral_0^1 arccos(u)du=1, matching L2. This checks the covariance-relevant statistic independently.

No substantive gap was found in these scoped proofs. The peer's artifact ends with an orphaned fragment and a repeated NEXT line; clean that presentation before freezing a release. These KEEP verdicts concern mathematical content only: response-side served-model and independent-login evidence have not been supplied, so no campaign promotion gate is claimed satisfied.

## B2: stronger counterexample, retaining a logarithmic variance premise

This new result uses a complete layered graph, not the source's nearest-neighbor planar lattice. It refutes only a uniform auxiliary bridge over deterministic Gaussian layered path families, even if that bridge assumes an O(n/log n) variance bound.

For each integer N>=3, take a fixed origin o with weight G_0~N(0,1), and N layers with N sites in each layer. Join o to every site of layer one and consecutive layers by all possible edges. All site weights and their fresh OU copies are independent standard Gaussians. A path has n=N+1 vertices, one per layer plus o, with a free endpoint. Its maximum is

M_N=G_0+sum_{k=1}^N T_{N,k},

where T_{m,k} are independent copies of T_m=max_{1<=j<=m} X_j for iid standard normals. Let I_m and I_m^s be the maximizing indices before and after X_j^s=e^(-s)X_j+sqrt(1-e^(-2s))X'_j, and q_m(s)=P(I_m != I_m^s).

We prove, with positive constants independent of m and all sufficiently large m,

(A) c/log m <= Var(T_m) <= C/log m.

(B) For s=m^(-1/2), c m^(-1/2)log m <= q_m(s) <= C m^(-1/4)log m+2m^(-3).

It follows that Var(M_N)=1+N Var(T_N)=Theta(N/log N). For every fixed epsilon>0 its ratio to (N+1)^(1-epsilon) diverges. But q_N(s_N)->0 and N q_N(s_N)->infinity at s_N=N^(-1/2). Independence across disjoint layers gives

P(entire maximizing path unchanged)=(1-q_N)^N ->0,

E[common vertices]/(N+1)=1-N q_N/(N+1) ->1.

The overlap fraction also tends to one in probability by Markov's inequality applied to the number of changed layers. Every maximum is almost surely unique since there are finitely many continuous Gaussian coordinates in each layer.

### Proof of (A): elementary Gaussian extremes, including moment control

Write phi for standard Gaussian density and barPhi=1-Phi. Define a=a_m by m barPhi(a)=1. For sufficiently large m, a>=1, and Gaussian Mills bounds

x phi(x)/(x^2+1) <= barPhi(x) <= phi(x)/x, x>0,

imply a^2~2 log m. The lower Mills bound follows by integration by parts and bounding the remainder integral by barPhi(x)/x^2; thus no extreme-value theorem or unproved moment convergence is needed.

Set Y=a(T_m-a). For z>=0, shifting the Gaussian tail gives

barPhi(a+z/a)/barPhi(a) <= exp(-z),

so P(Y>z)<=exp(-z). For 0<=z<=a^2, shifting in the other direction gives

barPhi(a-z/a)/barPhi(a) >= exp(z-z^2/(2a^2)) >= exp(z/2),

and therefore P(Y<-z)<=exp(-exp(z/2)). For z>a^2 put b=z/a-a>=0. The tail bound barPhi(b)<=2^(-1)exp(-b^2/2) gives

P(Y<-z) <= 2^(-m) exp(-m(z/a-a)^2/2).

Integrating 2z times these tail bounds proves E Y^2<=C uniformly for large m. Explicitly, the last portion is

2^(-m)[2a^3 sqrt(pi/(2m))+2a^2/m],

which is bounded, since a^2~2 log m. Thus Var(T_m)<=E(T_m-a)^2<=C/a^2.

For the lower bound, P(T_m<=a)=(1-1/m)^m>=1/4. Set b=a+1/a. Mills bounds give

m barPhi(b)>= [ab/(b^2+1)]exp(-1-1/(2a^2)) >= exp(-3/2)/5,

using a>=1 and b<=2a. Hence P(T_m>=b)>=1-exp(-exp(-3/2)/5), a positive constant. For an independent copy T'_m, Var(T_m)=E(T_m-T'_m)^2/2. The two opposite separated events at a and b give Var(T_m)>=c/a^2. This establishes (A).

### A uniform top-two gap estimate

Let D_m be the largest coordinate minus the second largest. Its density at d>=0 is

f_m(d)=m(m-1) integral_R phi(y+d)phi(y)Phi(y)^(m-2)dy.

This follows by choosing the top two labeled coordinates and requiring all remaining coordinates to be below y. We show f_m(d)<=C sqrt(log m), uniformly in d>=0, for m>=3.

Put B=2sqrt(log m). For y<0, bound phi(y+d)<=1/sqrt(2pi) and substitute u=Phi(y); this contribution is at most m 2^(-(m-1))/sqrt(2pi). For 0<=y<=B, phi(y+d)<=phi(y). Also

phi(y)<=exp(3/2)(y+1)barPhi(y),

because integrating phi on [y,y+1/(y+1)] bounds barPhi(y) below by exp(-3/2)phi(y)/(y+1). Substitution u=Phi(y), and integral_0^1 (1-u)u^(m-2)du=1/[m(m-1)], bound this portion by exp(3/2)(B+1). For y>B, phi(y+d)<=phi(B), so substitution bounds the contribution by m phi(B)=1/[sqrt(2pi)m]. These three bounds prove the asserted density estimate, hence P(D_m<=d)<=C d sqrt(log m).

### Proof of (B): a real lower event and a uniform stability upper bound

First take 0<s<=1 with a sqrt(s)<=1, set delta=sqrt(s), rho=e^(-s), and tau=sqrt(1-e^(-2s)). Consider the event that exactly two original coordinates lie in [a,a+delta] and all others lie below a. Its probability is exactly

choose(m,2) [barPhi(a)-barPhi(a+delta)]^2 Phi(a)^(m-2).

Since phi(a+delta)>=exp(-3/2)phi(a), phi(a)>=a/m by the upper Mills bound, and (1-1/m)^(m-2)>=1/4, this probability is at least c a^2 s. On this event the top-two original gap is at most delta. Conditional on all original coordinates, the fresh-noise difference of these two coordinates is normal with variance 2 tau^2. Since tau^2>=s(1-e^(-2)) for s<=1, the probability that the runner-up overtakes the old winner is bounded below by a positive constant independent of m and s. This event forces a different maximizer regardless of what the other perturbed coordinates do. Therefore q_m(s)>=c a^2 s.

For the upper bound, the event max_j |X'_j|<=sqrt(8log m) has complement probability at most 2m^(-3). On that event, if D_m>2tau sqrt(8log m)/rho, the original winner remains strictly above every competitor after perturbation. The density estimate therefore gives

q_m(s)<=C [2tau sqrt(8log m)/rho]sqrt(log m)+2m^(-3)
        <=C sqrt(s)log m+2m^(-3), 0<s<=1.

At s=m^(-1/2), the lower event's condition a sqrt(s)<=1 holds eventually, a^2~2log m, and (B) follows. Multiplication of layer equality probabilities occurs only after establishing independence of their entire original/fresh Gaussian arrays.

## Scope and the remaining proof gap

B2 uses a triangular family of complete layered graphs; its degree and layer width grow with N. It does not refute an implication restricted to a fixed nearest-neighbor planar lattice or an implication assuming quantitative decay of actual common-vertex overlap. It shows that even the logarithmic variance premise cannot turn the probability of any path replacement into the overlap estimate needed for a power improvement.

For C0120 the single hardest unresolved step remains a polynomial upper bound on the unrestricted lattice's residual variance, or an equally strong quantitative common-vertex overlap estimate. None of the constructions here supplies it.

Independent referee for B2: w500, pending. These are author proofs and scoped mathematical KEEP verdicts; promotion also requires the campaign's served-model and independent-review evidence. No formal proof checker was run.

NEXT: Have w500 independently check the uniform top-two density bound and mismatch lower event; retain B2 as draft concept material until the proof and provenance gates pass.
