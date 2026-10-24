# P0286 — attempt, 12 October 2026

**Further-attempt update:** `SECOND_ATTEMPT.md` records two new approaches and the pursued Darboux/big-q-Hermite route. It resolves the sharp general-ASEP infinite-line decay and fixed-theta infinite-line closing-density-gap scaling left open in this first attempt, and adds the literal exclusive-color near-half limit. The original proof below is retained as a record of that first stage; its former line-specific gaps are now closed by (S5), (S9)-(S13) in the supplement. The overall problem is still PARTIAL because canonical-ring transfer, compensation shape, and critical finite-size scaling remain unresolved.

## Exact scope and source

The workshop PDF, Section 5, page 3, asks:

> Within the known stationary measures of ASEP, can we investigate correlations? Consider the asymmetric simple exclusion process (ASEP) on a large ring with two particle colors, with particle densities ρ1 and ρ2. Define ηi(x) as the indicator for the presence of a particle of color i at site x under stationarity. A key question is to understand how the covariance between particle occupations decays with increasing spatial separation. When densities are close to 1/2, one could leverage the convergence to Brownian motions with drift and known stationary horizon properties to conjecture explicit forms for the correlation decay. For general densities, connections with known ASEP or TASEP analogues, such as speed processes or hidden invariances, may provide valuable insights.

The PDF does not specify rates, a joint limit, whether “near 1/2” refers to exclusive or cumulative densities, or which covariance entry. Thus this attempt fixes the conventional priority model explicitly. Colors are 1,2, and holes are 3. Adjacent decreasing pairs exchange at rate 1, increasing pairs at rate θ, where 0≤θ<1. This is Martin's left-moving convention. Reversing spatial coordinates gives the right-moving convention and transposes the directed cross-covariances below. Write a=ρ1, b=ρ1+ρ2, δ=b−a, and assume 0<a<b<1 unless a boundary case is stated. Covariances concern a single time, not time decay.

We prove an infinite-line ASEP exponential bound and exact covariance reduction, an explicit infinite-line TASEP asymptotic and closing-gap limit, and a quantitative canonical-ring transfer for TASEP. These are special cases/reductions, not a full solution to the source's ring question. No novelty claim is made.

## 1. Finite-ring identities and boundary cases

Let N≥3, let counts k1,k2,k3 be fixed, and put ρi=ki/N. Under any translation-invariant distribution with these fixed counts, define Cij(x)=Cov(ηi(0),ηj(x)). Then

    Σx Cij(x)=0;
    Cii(0)=ρi(1−ρi), Cij(0)=−ρiρj (i≠j).

Proof: sum the second covariance argument to the constant count kj. At a single site, indicators are idempotent and indicators for different colors have zero product. Translation invariance gives the means. This proves every formula.

For symmetric exchange (θ=1), every allowed swap has the same reverse rate, so the uniform fixed-count distribution is reversible. Sampling without replacement gives, for x≠0,

    Cii(x)=−ρi(1−ρi)/(N−1),
    Cij(x)=ρiρj/(N−1), i≠j.

Indeed P(ηi(0)=ηi(x)=1)=ki(ki−1)/[N(N−1)], while for i≠j the joint probability is kikj/[N(N−1)]. Subtracting products of means proves the assertions. They cancel the zero-site values when summed over x.

For arbitrary θ, the projections X=η1 and Y=η1+η2 are ordinary binary ASEPs. Their canonical stationary laws are uniform: for a binary cyclic word the number of 01 bonds equals the number of 10 bonds, so its total incoming and outgoing rates agree. Uniformity is stationary, and binary irreducibility identifies the stationary projection. Consequently for x≠0,

    C11(x)=−a(1−a)/(N−1),
    C11(x)+C12(x)+C21(x)+C22(x)=−b(1−b)/(N−1).

This does not make the full three-state law uniform. With N=3 and one of each type, word 123 has one decreasing and two increasing bonds, while its incoming edges have the reversed counts. Uniform incoming/outgoing imbalance is 1−θ, nonzero for θ≠1. Exact enumeration below verifies the actual nonuniform law. If any color count is zero, the remaining model is binary and the preceding uniform formulas apply; with no holes, η2=1−η1 and all covariances follow from the binary formula. These boundary laws are different from a positive-density infinite-line correlation tail.

## 2. Infinite-line queue reduction for general ASEP

External input: Martin, *Stationary distributions of the multi-type ASEP*, EJP 25 (2020), paper 36, Theorem 3.1 (arXiv PDF p.19), and its one-type projection/Burke property. It identifies the following queue output with the ergodic stationary two-type ASEP law on Z. The marginals D and S are Bernoulli product processes of densities a and b. The queue construction, rather than a uniform multispecies assumption, is essential.

Use independent Bernoulli arrivals At of parameter a and services St of parameter b, indexed in the direction of the queue. At=St=1 yields a departure. At=1,St=0 adds one customer. At=0,St=1 serves one of k waiting customers with probability 1−θ^k, otherwise the service is unused. Auxiliary choices are independent over sites. Put

    p=a(1−b), q=(1−a)b, r=p/q<1, h=1−p−q.

The stationary queue Q after each site has transition kernel

    P(k,k+1)=p,
    P(k,k−1)=q(1−θ^k), k≥1,
    P(k,k)=h+qθ^k, k≥0.

At θ=0, interpret θ^0=1 and θ^k=0 for k≥1. Its reversible probability is

    πk=Z^−1 r^k/dk,
    dk=∏j=1..k (1−θ^j), d0=1,
    Z=Σk≥0 r^k/dk.

Proof: dk stays between L=∏j≥1(1−θ^j)>0 and 1 (L=1 if θ=0). Positivity of L follows from summability of θ^j, using log(1−u)≥−2u for u≤1/2 and retaining the finitely many earlier factors. Thus Z is finite. Direct substitution gives πkp=πk+1q(1−θ^(k+1)), proving detailed balance. It gives a stationary probability; irreducibility identifies it uniquely. Its geometric tail also implies finite mean.

Here is a direct proof of the departure product property used below, so it need not be assumed separately. Given the queue after a site is k, a departure at that site could have come from a queue of size k+1 by a downward step, or from size k by a simultaneous arrival/service. Their reverse conditional probabilities are respectively πk+1 q(1−θ^(k+1))/πk=p and ab. Thus the reverse conditional departure probability is p+ab=a for every k. The stationary process of queue transitions with their departure labels is Markov also when reversed: its reverse transition-and-label kernel is the forward one multiplied by the stationary endpoint ratio. Conditional on the current reverse queue state and all previously exposed reverse labels, the next departure therefore has probability a. Iterating conditional probabilities proves that any finite consecutive departure string has the Bernoulli-a product distribution. Summing over skipped indices proves the same for any finite set of sites. S is a Bernoulli-b product process by construction. This supplies all marginal product claims in Section 2.

Let Ut be the unused-service indicator, i.e. color 2; let Dt=St−Ut be color 1. Conditional on Q before a site being k, an unused service has probability qf(k), where f(k)=θ^k, and leaves Q unchanged. Stationary zero drift gives

    p=q Eπ[1−f(Q)], so Eπ f=1−r and E U=q−p=δ.

For n≥1, the first unused service leaves the queue at k, the intervening n−1 sites evolve it by P^(n−1), and the last unused service contributes qf at that state. Hence exactly

    C22(n)=q² ⟨f,P^(n−1)f⟩π−δ²
           =q² ⟨f−Eπf,P^(n−1)(f−Eπf)⟩π.                 (2.1)

The output D0 depends only on Q before 0 and the independent inputs at sites ≤0. Sn for n>0 is independent of these. Therefore Cov(D0,Sn)=0. Since D is Bernoulli product, C11(n)=0; expanding S=D+U gives C12(n)=0. Likewise S is product, so expansion of Cov(S0,Sn)=0 gives C21(n)=−C22(n). Thus, in the queue direction,

    (Cij(n))i,j=1,2 = [[0,0],[−C22(n),C22(n)]], n≥1.    (2.2)

For n<0 use Cij(−n)=Cji(n). This relation follows by translation invariance and symmetry of scalar covariance. The actual direction of movement is opposite the queue direction in the right-moving convention of Ferrari–Gernholt.

An additional exact check is C22(1)=(1−θ)δp. For θ>0, evaluate the stationary drift of f(Q)=θ^Q:

    0=p(θ−1)E f + q(θ^−1−1)(E f−E f²).

Solving gives E f²=(1−θr)E f; substitute E f=1−r into (2.1) with n=1 to obtain the formula. For θ=0, f is the zero-state indicator, so E f²=E f=1−r and the same formula follows directly. This check confirms the simultaneous-arrival convention and the absence of an extra one-site transition in (2.1).

## 3. An explicit exponential bound for general ASEP on the line

For gθ=Lq(1−√r)²>0 and n≥1, we prove

    0≤C22(n)≤q² Varπ(f) (1−gθ)^(n−1).                 (3.1)

This is a bound, not the exact decay exponent for θ>0.

First prove a Poincaré inequality for νk=(1−r)r^k and the constant-rate reflected queue. For a finitely supported function v, write ei=v(i+1)−v(i). Cauchy–Schwarz gives

    (v(k)−v(0))² ≤ (Σi<k r^(−i/2))(Σi<k r^(i/2)ei²)
                 ≤ r^(-(k−1)/2)/(1−√r) Σi<k r^(i/2)ei².

Multiply by (1−r)r^k and sum k≥1. Interchange nonnegative sums. The coefficient of ei² is at most (1−r)r^(i+1)/(1−√r)². Therefore

    Varν(v)≤Eν[(v−v(0))²]
           ≤[q(1−√r)²]^−1 Σi≥0 νi p ei².

The same estimate extends by approximation to every L²(ν) function; the chain's bounded Dirichlet form is continuous in that norm. Since c≤πk/νk≤c/L for c=1/[Z(1−r)],

    Varπ(v)≤(c/L)Varν(v),
    Eπ(v,v)=Σπi p ei²≥c Eν(v,v).

Combining them gives Eπ(v,v)≥gθ Varπ(v). This is the centered spectral-gap bound for I−P.

We also need P to have no negative spectrum. Under the unitary map from L²(π) to ordinary ℓ², it is the real symmetric Jacobi matrix J with diagonal h+qθ^k≥h and adjacent entries √[pq(1−θ^(k+1))]≤√(pq). For finite vectors w, using 2|wkwk+1|≤|wk|²+|wk+1|² gives

    ⟨w,Jw⟩≥(h−2√(pq))||w||²≥0,

because h−2√(pq)=(√(ab)−√((1−a)(1−b)))². Density extends the bound to ℓ². Markov contraction puts the full spectrum in [0,1], and the Poincaré inequality puts the centered spectrum in [0,1−gθ]. The spectral theorem applied to (2.1) proves both the lower and upper bounds in (3.1). By (2.2), this bounds every off-site color covariance.

### Exact integrated covariance for general ASEP

There is also an exact identity, independent of θ:

    Σn≥1 C22(n)=p=a(1−b),
    Σn∈Z C22(n)=δ(1−δ)+2a(1−b).                      (3.2)

Proof: Q is in L²(π) by its geometric tail. Its one-step drift gives

    (I−P)Q=δ−qf=−q(f−Eπf).

Thus on the centered subspace (I−P)^−1(f−Eπf)=−(Q−EπQ)/q. This inverse exists by Section 3's strictly positive gap; summing (2.1), an absolutely convergent series, yields Σn≥1 C22(n)=−q Covπ(f,Q). The stationary family π depends only on r (and fixed θ). Differentiating Eπ f=1−r with respect to r gives Covπ(f,Q)/r=−1. The differentiation of the series is justified locally in r∈(0,1) by a geometric envelope times k, since dk≥L. Therefore the sum is qr=p. Reflection of the scalar covariance and C22(0)=δ(1−δ) give the two-sided identity. This identifies the line susceptibility, but not the compensating shape on a canonical ring where the total covariance must instead be zero.

## 4. Exact TASEP formula and sharp spatial asymptotic

Set θ=0 and t=√(pq), λ±=h±2t. Then 0≤λ−<λ+<1. For every integer n≥1,

    C22(n)=δ/(2π) ∫λ−^λ+ x^(n−1)
             √[4pq−(x−h)²]/(1−x) dx.                 (4.1)

In particular,

    C22(n) ~ δ√t/[2√π(1−λ+)] · λ+^(n+1/2)n^(−3/2). (4.2)

Proof of the spectral formula: the symmetric queue matrix has diagonal h on k≥1, diagonal h+q at k=0, and all adjacent entries t. Let m0(z) be the e0 resolvent of the constant-coefficient half-line tail. Removing its first coordinate gives m0=1/(z−h−t²m0). The solution tending to 1/z at infinity is

    m0(z)=[z−h−√((z−h)²−4t²)]/(2t²).

The square root is the analytic branch asymptotic to z−h at infinity. Removing coordinate 0 of J then gives its resolvent

    m(z)=1/[z−h−q−t²m0(z)]
        =2/[z−h−2q+√((z−h)²−4t²)].

Its negative imaginary part on the upper boundary of the cut, divided by π, is

    w(x)=√[4pq−(x−h)²]/[2πq(1−x)], λ−<x<λ+.

Here the simplification uses q²−q(x−h)+pq=q(1−x). The only pole off the cut is at z=1: squaring the denominator equation yields z−h=p+q, and q>p gives the required branch sign. Its residue is 1−p/q=π0. There are no endpoint poles since q≠p. The Stieltjes inversion formula, or uniqueness of the spectral measure from its resolvent, therefore gives

    P^k(0,0)=π0+∫ x^k w(x)dx.

For θ=0, f=1{0} and (2.1) becomes C22(n)=δq[P^(n−1)(0,0)−π0]. Substitution proves (4.1).

For (4.2), put y=λ+−x. Near y=0 the square root is √[y(4t−y)]~2√t√y, and 1−x→1−λ+. On any portion x≤λ+−ε, the integral is exponentially smaller than λ+^n n^−3/2; all x are nonnegative. On the edge portion, substitute y=λ+u/n, use (1−u/n)^(n−1)→e^−u, and dominate by a constant times √u e^−u/2 for n≥2. The resulting integral is Γ(3/2)=√π/2. Keeping λ+^(n−1)(λ+/n)^(3/2) proves the stated constant and power. This also justifies the sharp exponent rather than merely a logarithmic decay rate.

## 5. A precise closing-gap regime (TASEP)

Fix a→a0∈(0,1), b=a+δ, δ↓0, and integer n with nδ²→s∈(0,∞). Write v=a0(1−a0), β=1/(4v). Then

    C22(n)/δ² → √v/π ∫0∞ [√z/(β+z)]e^(−s(β+z)) dz. (5.1)

In particular for cumulative densities near a0=1/2 this limit is

    1/(2π) ∫0∞ [√z/(1+z)]e^(−s(1+z)) dz.

Proof: q−p=δ and

    1−λ+=(√q−√p)²=δ²/(√q+√p)².

Thus βδ=(1−λ+)/δ²→β and t→v. In (4.1), set λ+−x=δ²z. Exactly the rescaled integral is

    √t/π ∫0^(4t/δ²) [√z/(βδ+z)]
       √(1−δ²z/(4t)) (1−δ²(βδ+z))^(n−1) dz.

Extend the integrand by zero outside this interval. For small δ, βδ is bounded away from zero, t is bounded, and (n−1)δ²≥s/2. The power is bounded by e^(−s(βδ+z)/2), since 0≤x≤1. An integrable envelope is a constant times √z/(c+z)e^−sz/2. Dominated convergence proves (5.1).

The correlation length ξ=−1/log λ+ satisfies ξ~4vδ^−2. This is a cumulative-density closing-gap statement: exclusive color-2 density is δ→0. It must NOT be described as the two exclusive color densities both tending to 1/2. In that literal regime a≈1/2,b≈1,δ≈1/2 and the queue is not in heavy traffic. The workshop wording does not resolve this ambiguity.

## 6. Quantitative TASEP transfer to a canonical ring

Let a=k1/N, b=(k1+k2)/N with 0<a<b<1. Let CN be the stationary ring covariance and C∞ the line covariance with these same densities. For n≥1 and m≥0 with n+m<N, let M≤2(m+1) be the number of distinct sites in the two input windows of length m+1 ending at 0,n. Put

    Tm=2 exp[−δ²(m+1)/2]/(1−exp[−δ²/2]).

Then

    |CN22(n)−C∞22(n)| ≤ M(M−1)/N + 4Tm.              (6.1)

The bound may exceed 1 for small N or δ, but remains valid.

Proof: use Martin's ring queue law (Theorem 3.3, PDF p.22) in its deterministic θ=0 case: arrivals are a uniform k1-subset, services an independent uniform (k1+k2)-subset, and Q at a site is the maximum of 0 and all backward suffix sums of A−S up to length N. The total suffix sum is −Nδ<0, so longer suffixes cannot increase that maximum. The corresponding infinite queue is the supremum over all backward lengths. The unused service at i is Si(1−Ai)1{Qi−1=0}. Truncate Qi−1 to suffix lengths at most m. Truncation can change this indicator only if some suffix of length k≥m+1 has positive sum.

For either independent Bernoulli inputs or fixed-count sampling without replacement, each suffix of length k has arrival mean ak and service mean bk. Positive A−S implies either A−ak≥δk/2 or S−bk≤−δk/2. Hoeffding's inequality for bounded independent sampling, and its without-replacement counterpart, bounds each by exp(−δ²k/2). A union bound over k gives Tm (on the ring summing only to N is even smaller). The two indicator sites introduce at most 2Tm error in their joint occupation probability, for each of the two laws.

For completeness, the without-replacement concentration used here follows by comparing exponential moments to sampling with replacement: for positive numbers wi, the average product over distinct k-tuples is the kth elementary symmetric mean and is at most ((Σwi)/N)^k (Maclaurin's inequality). Apply wi=exp(t zi) to the population zi∈{0,1}, then the ordinary bounded-variable Hoeffding moment bound and Chernoff optimization. This proves both tail signs with the asserted constants.

On the M input sites, couple a uniform population permutation sample with independent uniform population labels sampled with replacement. They can agree until a repeated label appears; its probability is at most M(M−1)/(2N). Do this separately for arrivals and services. The resulting with-replacement bits are independent Bernoulli a and b, and the total disagreement probability is at most M(M−1)/N. Because n+m<N, the windows have the same overlap pattern on the line and ring. Hence the truncated joint occupation probabilities differ by at most this quantity. Combining the two truncation errors proves (6.1). Both laws have mean color-2 density δ, so subtracting δ² leaves the same estimate for covariance.

For a fixed positive density gap bounded away from zero, m of order log N yields error O((log N)²/N), with an arbitrarily small polynomial truncation error. This proves convergence to the line covariance for fixed n and gives an absolute-error mesoscopic estimate for n≤N−O(log N). It does not prove a relative asymptotic when the line covariance is smaller than that error. In particular it cannot describe the negative compensation at ring-scale distances.

It does force a quantitative conservation effect. If aN→a,bN→b with 0<a<b<1, and χ=δ(1−δ)+2a(1−b), then

    limsupN→∞ N minx≠0 CN22(x) ≤ −χ.                 (6.2)

Proof: fix an integer R≥1 and N>2R+1. By the sum rule, the sum of covariances outside the sites of circular distance at most R is minus their sum inside. At least one outside covariance is at most this outside sum divided by N−2R−1. Scalar covariance is reflection-symmetric. Section 6's fixed-distance convergence, including at zero, makes the inside sum converge to δ(1−δ)+2Σn=1..R C∞22(n). This also uses continuity of the line integral (4.1) in a,b for each fixed n; its endpoints and integrand vary continuously and stay uniformly separated from 1 in a compact neighborhood of the limiting densities. Multiply the minimum inequality by N, take limsup, and then send R→∞ using (3.2). This proves (6.2). It is an existence bound for negative compensation somewhere on the ring, not an assertion that a uniform correction −χ/N is the pointwise answer.

A restrictive but rigorous finite-ring version of (5.1) follows: if aN→a0, δN↓0, nNδN²→s>0, and

    N δN^6/[log(1/δN)]² →∞,

choose mN=⌈KδN^−2 log(1/δN)⌉ with K>8. Then M²/N=o(δN²), Tm=O(δN^(K/2−2))=o(δN²), and nN+mN<N eventually. Divide (6.1) by δN² and apply (5.1). These are sufficient conditions from a crude coupling bound, not the expected optimal finite-size regime.

## 7. Referee checks and remaining gaps

`verify.py` enumerates the canonical two-row TASEP queue at N=3,4,5,6,7. It checks the entire stationary master equation with exact rational arithmetic, and verifies the covariance sum rule. It separately constructs general-θ queue matrices, compares emission-matrix and inner-product covariance computations, checks (3.1), and compares (4.1) with queue powers. It also tests the rescaled integral in (5.1) at four shrinking gaps. Results are saved in `verification.json`. These numerical checks support proofs, and do not replace them. Matrix truncation is used only for checking, never in a proof.

`check_asymptotic.py` compares the exact integral with (4.2), dividing out its exponential factor before quadrature to avoid underflow. At n=100000 the three tested density pairs give ratios 0.999247, 0.999839, and 0.998522, approaching 1 as n increases. Results are in `asymptotic_checks.json`. An initial 1%-accuracy assertion at n=10000 failed for a=0.5,b=0.6 (ratio 0.985541): it was an overly early finite-n tolerance, not a proof failure. Increasing n and retaining all the ratios checks the actual asymptotic statement and illustrates that its convergence is not uniform as δ closes.

`Algebra.lean` checks three algebraic identities: the projected covariance constraint, q−p=b−a, and the denominator simplification in (4.1). It does NOT formalize the probability arguments, spectral theorem, or limits. The single shared-slot `lake env lean` invocation exited successfully with code 0 and no diagnostics, as recorded in `lean_result.txt`. These three identities are kernel-checked. No sorry or native_decide occurs.

Potential failure points explicitly audited: queue direction and n−1 versus n; simultaneous arrival/service being a departure; the stationary π tilt after an unused service; the sign of the spectral density; the isolated stationary atom; both endpoints of the continuous spectrum; preservation of fixed densities in the finite comparison; overlap of input windows; distinction between absolute and relative error; and exclusive versus cumulative half densities.

Another exact finite boundary check: if k2=1, for any θ and any distinct sites the two color-2 occupation indicators have zero product. Consequently CN22(n)=−1/N² for n≠0, and CN22(0)=(1/N)(1−1/N). Translation invariance alone proves this, and the enumerations with k2=1 confirm it. It illustrates the failure of a positive infinite-line tail to describe every joint ring/density regime.

Remaining gap at the end of the **first** attempt: general θ∈(0,1) canonical-ring covariance asymptotics with optimal conservation correction and ring-scale separation; exact general-ASEP spatial exponent/prefactor (the bound (3.1) need not be sharp); the general-ASEP closing-gap scaling function and optimal joint N,density,separation regimes (particularly Nδ² of order one); and a precise interpretation of the source's near-half-density request. These were the gaps used to choose the two further approaches.

**Current remaining gap after the further attempt:** The sharp fixed-theta line exponent/prefactor and fixed-theta line closing-gap scaling are now proved in `SECOND_ATTEMPT.md`. Still unresolved are canonical general-ASEP ring transfer and the conservation correction's spatial profile, ring-scale separation, Nδ² of order one, and simultaneous weak-asymmetry/closing-gap regimes. The ambiguity between exclusive and cumulative densities near one-half remains a source-statement caveat. The overall verdict remains PARTIAL.
