# F0084 — critical stable Poisson allocation

## Superseding second attempt

The second attempt resolved the explicitly requested upper-bound question in the literature. Holroyd–Pemantle–Peres–Schramm's *Poisson Matching*, Theorem 6(ii) and its explicit extension on printed pp.269–270 (arXiv PDF pp.6–8), gives polynomial upper tails for this exact critical stable allocation. See LITERATURE.md for exact quotations and hypothesis mapping, SECOND_ATTEMPT.md for the two new approaches, and SOLUTION.md for an independent complete proof of P(X>r)<=K_d r^(-1/(4d)), d>=2. The remaining-gap statements below are the historical state of the FIRST attempt; their claim that no critical upper bound was established is superseded. Determining the sharp tail is not settled by the cited theorem or by this attempt.

## Exact question and source verification

Centres are a homogeneous Poisson process of intensity 1 on R^d, and every centre has appetite 1. Use the almost surely unique translation-equivariant stable allocation. Put X=|Psi(0)|, with unclaimed sites assigned distance infinity. At criticality almost every site is claimed, so X is almost surely finite. The requested result is a quantitative upper bound tending to zero for P(X>r), for every d>=2, or a fuller description of that tail.

The source PDF, page 31, Open problems (ii), says exactly: “Critical tail behavior. What is the tail behavior of X for the critical Poisson model? In particular, give any quantitative upper bound for d ≥ 2.” The heading is `Open problems` following Section 9 in the fetched version, not Section 12. Page 30, Theorem 32, states: “Let Π be ergodic and insertion-tolerant and let λα = 1. For any d ≥ 1, we have EX^d = ∞.” This is the SITE distance. Page 31, Theorem 33, separately treats the Palm CENTRE territory radius. The prior intake confused that distinction. Page 6, Theorem 7, also gives E X^(d/2)=infinity for d=1,2. A conjecture P(X>r)=r^(-d/2+o(1)) is not proved here; diverging moments alone do not establish pointwise polynomial lower bounds.

## Proven reduction to bounds uniform near criticality

Fix d. For 0<beta<1 let X_beta be the distance at the origin for the SAME Poisson configuration with appetite beta. Write X_1 for the critical distance. Define

M_beta(c) = E[exp(c X_beta^d) 1{X_beta<infinity}].

For every beta<1, the noncritical theorem provides some c_beta>0 with M_beta(c_beta)<infinity. Then for all r>=0,

P(X_1>r) <= (1-beta) + M_beta(c_beta) exp(-c_beta r^d).                 (1)

This is a reduction, not a quantitative solution: neither c_beta nor M_beta is controlled here as beta increases to 1.

### Complete proof of (1)

Use the site-optimal allocations, which agree almost surely with the unique allocations of the stationary Poisson model. Source Proposition 22(i), PDF page 21, gives |x-Psi_1(x)|<=|x-Psi_beta(x)| for Lebesgue-almost every x in almost every configuration. To transfer to the deterministic origin, let B be any bounded positive-volume box. Fubini gives the integral over B of the probability of failure as zero. Translation covariance and stationarity make this probability independent of x; hence it is zero at 0. Therefore X_1<=X_beta almost surely for each fixed beta. A simultaneous coupling over uncountably many beta is not needed.

The subcritical phase theorem says all centres are sated. We prove P(X_beta<infinity)=beta rather than assuming it. Let Q=[0,1)^d. Tonelli and the Campbell–Palm formula give

E integral_Q 1{Psi_beta(x) is a centre} dx
= E sum_{xi in Pi} integral_Q 1{Psi_beta(x)=xi} dx
= integral_{R^d} E^0 integral_Q 1{Psi_beta^0(x-y)=0} dx dy
= E^0 integral_{R^d} 1{Psi_beta^0(z)=0} dz
= beta.

The third equality is Palm translation covariance at intensity 1. In the fourth, for each fixed z, the y that put z+y in Q have volume 1; all integrands are nonnegative. Satedness holds for the Palm centre as well, since the expected number of nonsated centres in Q is zero and Campbell's formula identifies this expectation with its Palm probability. Stationarity makes the first expression equal to P(X_beta<infinity). Thus P(X_beta=infinity)=1-beta.

Split {X_beta>r} into {X_beta=infinity} and {r<X_beta<infinity}. On the second event exp(c_beta X_beta^d)>=exp(c_beta r^d). Markov's inequality therefore bounds its probability by M_beta(c_beta)exp(-c_beta r^d). Combine this with X_1<=X_beta. This proves (1).

For each epsilon>0, choose beta=1-epsilon/2 and then a sufficiently large r to make the second term at most epsilon/2. This recovers qualitative tail convergence. The dependence of that r on epsilon remains unbounded by any explicit function in this attempt.

### A precise sufficient nearcritical estimate (conditional implication)

Suppose there were constants C,c0,b>0, a>=0 and delta0 in (0,1) such that for every 0<delta<=delta0 one could choose c_(1-delta)>=c0 delta^b and M_(1-delta)(c_(1-delta))<=C delta^(-a). Then (1) would give

P(X_1>r) <= r^(-d/(2b)) + C r^(ad/(2b)) exp(-c0 r^(d/2))

for every r with r^(-d/(2b))<=delta0. Proof: set delta=r^(-d/(2b)) in (1); then delta^b r^d=r^(d/2) and delta^(-a)=r^(ad/(2b)). The exponential term is eventually at most r^(-d/(2b)): taking logarithms reduces this to log C + ((a+1)d/(2b)) log r <= c0 r^(d/2), which holds because log r/r^(d/2) tends to zero. Thus the hypothetical estimates imply P(X_1>r)<=2r^(-d/(2b)) for sufficiently large r. This proves an implication only. The displayed assumptions have NOT been established for the stable Poisson allocation.

## A rigorous obstruction to inferring a rate from pointwise noncritical theorems

The coupling, exact missing mass and individual exponential moments above do not, by themselves, imply a specified critical decay rate. Here is a complete abstract counterexample to that inference (not a counterexample to the Poisson problem).

Let h:[0,infinity)->(0,1] be continuous and strictly decreasing, h(0)=1, and h(r)->0. There is a nonnegative finite random variable D with P(D>r)=h(r): its continuous distribution function is F(r)=1-h(r), a genuine distribution function with limit 1. For beta in (0,1), let q_beta be the unique finite solution F(q_beta)=beta. Define Y_beta=D if D<=q_beta and Y_beta=infinity otherwise; put Y_1=D.

Because q_beta increases with beta, Y_beta decreases pointwise as beta increases: a value changes only from infinity to D. We have P(Y_beta=infinity)=1-beta by the definition of q_beta. For EVERY c>0 and every fixed d>=1,

E[exp(c Y_beta^d) 1{Y_beta<infinity}] <= beta exp(c q_beta^d) < infinity.

Nevertheless P(Y_1>r)=h(r). For example h(r)=1/log(e+r) decays more slowly than every negative power of r. Iterated logarithms make it slower still. Given any proposed vanishing rate g, a continuous decreasing h can be chosen to dominate g along arbitrarily large radii (for monotone continuous positive g, take a suitably normalized square root). Hence no universal rate follows from these abstract hypotheses alone. Spatial stability supplies additional information that a successful argument would have to use.

For the explicit logarithmic choice, every positive moment of D is infinite: the tail integral s integral_0^infinity r^(s-1)/log(e+r) dr diverges for every s>0, since for large r, log(e+r)<=r^(s/2). Consequently the critical moment-divergence facts in the source do not exclude this abstract slow-tail obstruction either.

## Geometric check of the earlier discrepancy route

If X_1>r and xi is a centre with |xi|<r, the origin desires xi. Stability forces xi to be sated and to have no allocated site farther from xi than |xi|. Thus its territory is contained, up to a null set, in the closed ball centred at xi of radius |xi|. Otherwise xi covets 0 and the pair blocks. Consequently, for every finite S subset of Pi intersect B(0,r),

|S| <= volume(union_{xi in S} B(xi,|xi|)).                            (2)

Territories are disjoint and each has volume 1, which proves (2). In particular N(B(0,r))<=v_d(2r)^d. This bound is much larger than its mean v_d r^d; a typical Poisson fluctuation does not contradict it. Merely counting centres in B(0,r) cannot establish an upper tail estimate from this argument. Also a deficit in B(0,r) can be served near its boundary: it does not locate a positive volume of sites a distance r from their centres. Those two gaps invalidate the earlier informal deduction of an exponent.

At small radii, put a_d=v_d^(-1/d). If some xi has |xi|<min(r,a_d), it cannot be sated entirely inside B(xi,|xi|), whose volume is less than 1. Stability therefore implies X_1<=|xi|<r. Taking a Poisson void probability gives the elementary bound

P(X_1>r) <= exp(-v_d min(r,a_d)^d).

The reverse bound P(X_1>r)>=exp(-v_d r^d) follows because no centre in B(0,r) prevents any assignment at distance <=r (sphere events have probability zero). Thus for 0<=r<=a_d the exact identity P(X_1>r)=exp(-v_d r^d) holds. This is a proved small-distance special case, not the desired large-r tail: the displayed upper bound saturates at exp(-1).

The equivalence underlying the identity can be made explicit. For fixed 0<r<=a_d, with probability one there is no centre exactly at distance r and the origin is not an exceptional allocation site. If a centre xi exists within distance r while X_1>r, stability requires its full volume-one territory inside a ball of volume v_d|xi|^d<1, a contradiction. If there is no centre within distance r, and none on its sphere, the assigned centre cannot have distance at most r. Thus {X_1>r} agrees almost surely with the void event. At r=0 the identity follows because the process has no centre at the deterministic origin. This handles both endpoints and strict inequalities.

## First-attempt referee checks and remaining gap (historical)

The probability inequality includes the unclaimed mass; applying Markov to the extended-valued X_beta without splitting would be invalid. Monotonicity has the correct direction by Proposition 22. A deterministic origin requires the Fubini/stationarity step. Site and Palm centre quantities are distinct. Bounds for optimal or gravitational allocations do not transfer to the Euclidean stable allocation.

Historical route-specific gap: obtain explicit estimates of M_beta and c_beta sufficiently uniform as beta approaches 1. Those estimates remain unproved by this attempt, but they are not needed: the successful weighted-flow argument in SOLUTION.md proves a critical decay rate directly, and the exact published extension is quoted in LITERATURE.md. The remaining unresolved question in the present work is the sharp asymptotic tail, not the existence of an upper bound.

### Finite numerical checks completed

`finite_check.py` ran 20 seeded trials (seed 84) with 256 equally weighted sites on a two-dimensional torus of side 4, 16 uniformly random centres, and integer capacities 16 and 15. The distance matrix occupied 32,768 bytes; numerical work took approximately 0.47 seconds. `finite_results.json` contains each trial. In every trial, direct examination of every site-centre pair found no blocking pair; increasing capacities improved every site's distance; the lower capacity left exactly 16 sites unclaimed; and every site whose nearest-centre distance ball contained fewer than 16 sites was assigned to that nearest centre. These are checks of the discrete analogues, not estimates for the infinite continuum tail. Fixed centre count and site discretization prevent treating this as a Poisson critical-tail experiment.

`CapacityCheck.lean` formalizes the finite cardinality obstruction and its ordered-distance consequence, importing only `Mathlib.Data.Finset.Card`. Run from `~/lean_verify` with `lake env lean ~/brain_workers/TRIO_1011/op/F0084/CapacityCheck.lean`. The shared-machine wrapper waited 318 seconds for slot 0, then ran the check. It completed with exit code 0 and no Lean errors. Both theorems use kernel-checked proof terms; there is no `sorry`, `native_decide`, or unchecked axiom. This verifies the finite counting argument only; the continuum allocation proof and critical-tail problem are not formalized.
