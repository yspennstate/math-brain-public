# Second serious attempt at D0064 — 11 October 2026

## The gap being attacked

The first attempt proved a clustered atomic solution at gamma=0, alpha=1/2 with summable bounded-window mixing. It did not check the source's unspecified stronger dependence condition. For positive gamma it did not prove that an arbitrary solution is conditionally independently scattered stable chaos, nor uniqueness of an arbitrary critical directing measure.

## Two approaches not previously tried

1. **Use finite-range dependence to classify the whole zero-intermittency boundary.** Require independence of random-measure restrictions to bounded sets separated by a fixed cutoff L. Exact deterministic dilation then sends any two positively separated bounded sets beyond L. This might force independently scattered increments. Stationarity plus independent increments yields a volume-linear Laplace exponent; exact dilation should force that exponent to be a pure alpha power. This would identify precisely an extra hypothesis that repairs the paired-cluster obstruction, without assuming finite mean or a stable representation in advance. The neighbouring theory is positive independently scattered Levy random measures / stable subordinators. Start in dimension one, then inspect whether the proof extends to general d.

2. **Recover a directing measure from the tail counts of atoms for positive gamma.** For a stable Cox measure, suitably normalized counts of atoms above a small mass threshold converge to the directing measure. Under star weights, atom masses multiply pointwise, suggesting a recovered measure transforms with exp(alpha omega). Try to derive regular variation and conditional Poisson statistics from the fixed-point identity and decay of dependence, rather than assuming stable subordination. Test this on the paired-cluster example: tail counts may recover a deterministic intensity while retaining double clusters, so tail convergence alone cannot imply the required conditional Poisson property. The missing theorem would have to rule out persistent atom decorations for positive gamma.

I will pursue approach 1 first because every proposed implication can be proved or falsified directly, and it treats an unclassified assumption-free-in-moment special case. Approach 2 remains a potential route for positive gamma, but has an explicit conditional-independence obstacle.

## Work in progress

Brain recalls were requested using the gap's words: independently scattered random measure, Levy basis, stable subordinator, Laplace exponent; and star-scale uniqueness, finite range, Cox directing measure. Returned cards are hints only.

Both recalls completed. The first returned the Levy process/Levy triplet cards, the Pitman--Yor stable-subordinator source, and a Cox-compensator card. The second returned general GMC construction/interpolation, stable-distribution, and irrelevant finite-range/percolation cards; none supplied a fixed-point classification. I read the Cox-compensator card in full (claim_55e8e09f5c49b2cbb66486d438868e84fb01a1a1343ae43fbfc159ed85f2a1e6). Its compensator description is not a theorem deriving conditional Poisson scattering from recovered intensity. The final arguments below are proved directly; no card is used as a verdict or unverified hypothesis transfer.

## Stronger result from approach 1: uniform mixing, not just a cutoff

The finite-range assumption can be weakened. Define

    eta(R)=sup |P(E intersection F)-P(E)P(F)|,

where the supremum ranges over bounded Borel sets A,B at distance at least R and events E,F measurable from the restrictions of M to A,B respectively. Crucially the diameters and volumes of A,B are unrestricted. Assume eta(R)->0. Finite-range independence is a special case. This is stronger than fixed-window mixing with a bound depending on the volumes.

**Theorem (complete classification of a strengthened zero-gamma special case).** Let d>=1, 0<alpha<=1, and let M be a stationary nonzero nonnegative random Radon measure on R^d. Suppose

    [M(A)]_A =law [epsilon^(d/alpha) M(A/epsilon)]_A

for every 0<epsilon<=1, and eta(R)->0 as above. Then there is a deterministic c>0 such that

    E exp(-integral f dM)=exp(-c integral f(x)^alpha dx)

for every nonnegative bounded compactly supported Borel f. For alpha=1, M=c dx almost surely. For 0<alpha<1, M is the independently scattered positive alpha-stable random measure with Lebesgue control c dx, and is purely atomic. No moment assumption or preassigned conditional stable representation is used. These are exactly the zero-intermittency candidates in cases (1) and (3).

**Connection with the Gaussian equation.** When gamma=0, each weight has zero variance, and alpha-normalization forces its deterministic mean to be (d/alpha)log(epsilon). For jointly measurable versions, independence from M^epsilon justifies replacing the weight by this constant in the integral, even if the field initially has exceptional random spatial points: condition on M^epsilon, and Tonelli on each compact shows integral 1_{omega(x) differs from its mean} M^epsilon(dx)=0 almost surely, because the pointwise exceptional probabilities are zero. Thus the theorem's deterministic scaling hypothesis follows from the zero-gamma star equation in its usual measurable formulation.

### Proof, step 1: independence for separated sets

Fix bounded sets A,B with distance r>0. Exact scaling gives equality of the joint laws of the restrictions, after the deterministic invertible map that dilates locations by epsilon and multiplies masses by epsilon^(d/alpha). Thus every pair of events from M|A,M|B has the same joint and marginal probabilities as some pair of events from M|(A/epsilon),M|(B/epsilon). Their dependence is bounded by eta(r/epsilon), which tends to zero. Hence the two restriction sigma fields are independent.

For finitely many pairwise positively separated sets A_i this gives mutual independence, not merely pairwise independence: A_1 is positively separated from the union of the other sets, so its sigma field is independent of their joint sigma field. Repeat by induction.

### Proof, step 2: deterministic Lebesgue-null sets have zero mass

Let N be a fixed bounded Lebesgue-null Borel set. For a fixed bounded translation box T of positive volume, Tonelli gives, for every realization of the Radon measure,

    integral_T M(N+a) da
      =integral M(dx) integral_T 1_N(x-a) da =0.

The inner integral is zero for every x, since x-N is Lebesgue-null. The identity is valid without any finite-mean assumption. It follows that integral_T min(1,M(N+a)) da=0. Taking expectation and using stationarity gives |T| E[min(1,M(N))]=0, hence M(N)=0 almost surely. In particular every deterministic rectangular boundary has zero mass almost surely. This does not claim that a random atom location has zero mass.

### Proof, step 3: independent masses for disjoint boxes, including touching boxes

Let Q_1,...,Q_n be disjoint bounded half-open axis-parallel boxes with positive side lengths. Shrink each box on all faces by an amount tending to zero. The resulting closed boxes lie in their interiors and are pairwise at positive distance for each sufficiently small shrinkage. Step 1 makes their masses mutually independent. Their masses increase almost surely to the masses of the interiors by continuity from below. Step 2 makes each boundary null, so these limits equal M(Q_i). For q_i>=0, dominated convergence applied to the joint Laplace transform preserves the product factorization. Therefore the limiting vector has independent components. The joint Laplace uniqueness argument in REDUCTIONS.md justifies the last conclusion. Zero-volume boxes have zero mass by step 2.

### Proof, step 4: Laplace exponent proportional to volume

For q>=0 and a box Q set L_q(Q)=-log E exp(-q M(Q)). It is finite because M(Q)<infinity almost surely, making the expectation strictly positive; it is nonnegative. It is translation invariant, additive across box partitions by step 3, and monotone with set inclusion. Let psi(q)=L_q([0,1)^d).

Partition [0,1)^d into n^d translates of [0,1/n)^d. Additivity gives L_q([0,1/n)^d)=psi(q)/n^d. A box with positive rational side lengths m_i/n is tiled by product_i m_i such small cubes, so its exponent is its volume times psi(q). Translation invariance removes restrictions on its origin. For arbitrary positive real side lengths choose increasing rational lengths from below, keeping the lower corner fixed. The corresponding boxes increase to the box, so continuity from below of M and dominated convergence of its Laplace transform extend the formula to all side lengths. Thus L_q(Q)=|Q|psi(q).

### Proof, step 5: exact dilation forces a pure power

Apply scaling to the unit cube. Step 4 yields

    psi(q)=epsilon^(-d) psi(q epsilon^(d/alpha)).

For every u in (0,1], choose epsilon=u^(alpha/d), obtaining psi(qu)=u^alpha psi(q). Put q=1 for arguments <=1; for q>1 put u=1/q in the same identity. Together these prove psi(q)=c q^alpha for every q>=0, where c=psi(1)<infinity and psi(0)=0. If c=0 then E exp(-M([0,1)^d))=1 and hence that mass is zero almost surely; stationarity and countable translates covering R^d force M=0 almost surely, contrary to the assumption. Therefore c>0.

### Proof, step 6: identify the entire random measure law

For disjoint boxes Q_i and numbers q_i>=0, steps 3--5 give the joint Laplace transform exp(-c sum_i |Q_i| q_i^alpha). For alpha=1 this is the transform of the deterministic masses c|Q_i|. For 0<alpha<1 it is the transform of the Poisson atomic random measure with intensity

    dx [c alpha/Gamma(1-alpha)] z^(-1-alpha)dz,

integrated with atom mass z. Its existence, local finiteness and Laplace functional were proved in REDUCTIONS.md by the small-jump/large-jump split and Gamma integral. Countably many bounded rational half-open boxes generate the random-Radon-measure sigma field; their finite-dimensional distributions therefore determine the entire measure law. This proves equality in law with the stated canonical measure, and hence the displayed Laplace functional for all bounded compactly supported Borel f. For alpha=1 equality with a deterministic law gives M=c dx almost surely; for alpha<1 pure atomicity follows from the Poisson construction. This completes the proof.

### Why the new hypothesis excludes the old counterexample

For the paired measure, A=[0,1], B=[2,3], let U=exp(-M(A)), V=exp(-M(B)). The first attempt proved Cov(U,V)>0. For [0,1]-valued variables measurable from two restriction sigma fields, layer-cake integration bounds |Cov(U,V)| by their event mixing coefficient: express U=integral_0^1 1_{U>s}ds and likewise V, then apply the defining bound inside the double integral.

For every R>=1, use the windows RA,RB and the variables U_R=exp(-R^(-2)M(RA)), V_R=exp(-R^(-2)M(RB)). Exact scaling of the paired construction makes their joint law identical to (U,V). The windows have distance R. Consequently eta(R)>=Cov(U,V)>0 for every R>=1. Thus fixed-window O(R^-2) mixing does not imply the uniform condition needed in the theorem, and the old counterexample fails that condition sharply. In particular it has no finite independence cutoff.

### Why this does not solve positive gamma

For gamma>0 the scale factor is a spatially varying random Gaussian weight. Conditional on the weight, the scaled fine measures on separated windows may be independent; integrating over the weight reintroduces dependence through the correlated Gaussian field. The deterministic invertibility argument in step 1 is unavailable. Even with compactly supported seed covariance, a fine-scale Gaussian weight can retain correlations between sufficiently close original windows. No inference from this special-case proof to arbitrary-solution stable subordination or critical uniqueness is made.

The source does not specify a uniform mixing condition, so the theorem does not establish its conjecture under all intended hypotheses. It gives a complete all-dimensional, all-alpha zero-gamma special case under one explicit stronger decay assumption and precisely explains why the earlier counterexample is compatible with it.

## Testing approach 2: tail counts can recover the wrong amount of information

There is an exact obstruction to treating tail-count convergence as proof of stable subordination. For the paired construction from ATTEMPT.md and a bounded Borel A, let C_h(A) be the number of its atoms in A of mass greater than h>0. Almost surely different cluster endpoints never coincide: exhaust the Poisson configuration by finite-intensity strips with bounded x and z bounded above and away from zero; conditional on each finite count, the coordinates have a joint density, so each equality between endpoints of different points has probability zero. Within a cluster the endpoints are distinct because sqrt(z)>0. Countably many strips and point pairs cover the entire configuration. Thus C_h(A) is exactly the Poisson integral of

    a(x,z) 1_{z>h}, where a=1_A(x)+1_A(x+sqrt(z)).

Its expectation is

    E C_h(A)=2|A| integral_h^infinity z^(-3/2)dz
            =4 |A| h^(-1/2).

For a Poisson integral with square-integrable integrand the variance is the integral of the squared integrand. This formula follows first for disjoint simple functions from independent Poisson counts and Var(Poisson(lambda))=lambda, and then by L^2 approximation. Here a is in {0,1,2}, so a^2<=2a and both integrals are finite. Therefore

    Var(C_h(A)) <= 8 |A| h^(-1/2).

Define T_h(A)=(sqrt(h)/4) C_h(A). It follows that

    E T_h(A)=|A|,
    E[(T_h(A)-|A|)^2] <= (|A|/2) sqrt(h) ->0.

Thus normalized atom-tail counts recover deterministic Lebesgue measure in L^2, even though the original random measure has strictly dependent masses in separated windows and is not stable white noise. For any finite family of bounded sets the recovery holds jointly in L^2 coordinatewise. This disproves the proposed intermediate implication “tail-count directing measure exists, therefore conditional independent stable scattering”. A positive-gamma proof via approach 2 would need an additional argument removing persistent cluster decorations; no such argument is established here.

## Hostile-referee audit of this second attempt

- **Is uniform mixing the same assumption as earlier summable mixing?** No. The supremum ranges over every bounded-window size. Its necessity in step 1 is explicit, and the paired example fails it at every separation.
- **Only pairwise independence derived?** Independence of one window from the union of the others makes the induction valid. The proof does not replace joint independence by pairwise independence.
- **Could infinite mean invalidate the boundary-null argument?** No. Tonelli is used for nonnegative functions, the inner Lebesgue integral is identically zero, and expectations are taken only after truncating mass at 1.
- **Can touching boxes be separated without losing random atoms?** Their deterministic boundaries have zero mass by step 2. Increasing shrunken closed boxes converge to the interiors pathwise; no regularity of a random density is assumed.
- **Are arbitrary real side lengths justified by rational grids?** Rational inner boxes increase to the given half-open box. Continuity from below and bounded convergence of exp(-qM) give the required limit.
- **Does scaling hold jointly for restriction events?** The hypothesis is equality in law of random measures. Dilation and positive mass multiplication are deterministic measurable bijections on restrictions. This preserves event dependence, not merely one-set marginals.
- **Does a pure-power exponent on unit cubes identify a measure?** Independence and volume-linearity first determine every joint transform on rational boxes. That countable generating class determines the entire law.
- **Is positivity of c a hidden finite-moment argument?** No. A Laplace expectation equal to 1 for a nonnegative mass forces that mass to vanish almost surely; countable translated unit cubes then imply the measure is zero.
- **Does the stable law's existence use an unproved neighbouring theorem?** The conditional Poisson construction and Gamma integral in REDUCTIONS.md supply it. No Levy--Khintchine classification theorem is needed in the final proof.
- **Is the tail-count Poisson variance formula applicable with infinitely many tiny atoms?** At each threshold h>0 the endpoint count hitting a bounded window has finite intensity. The squared-integrand bound proves L^2 integrability. No mass second moment is assumed.
- **Does this close critical or positive-gamma uniqueness?** No. The key deterministic transport of dependence fails with a random Gaussian multiplier. The remaining general-solution representation and critical uniqueness gaps are unchanged.

## Final scope of the second attempt

Verification completed: second_numerical_results.json records all four checks true. FiniteMultiplicity.lean was compiled by `lake env lean` from ~/lean_verify; second_lean_check.txt records EXIT_CODE 0. The proof uses `decide`, is kernel evaluated, and the theorem depends on no axioms. This checks only the finite multiplicity inequality, not the entire measure-theoretic theorem.

New proved result: the full zero-gamma classification, in every dimension and for all 0<alpha<=1, under uniform mixing over all bounded-window sizes (in particular under finite-range independence), without moment hypotheses. New proved obstruction: atom-tail recovery can converge in L^2 to a deterministic control measure while conditional stable scattering fails. The overall D0064 verdict remains PARTIAL because the positive-gamma classification and the source's unspecified dependence condition have not been settled.
