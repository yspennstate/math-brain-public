# I0008 research attempt ? 2026-10-12

## Verified target
The fetched source is Adhikari?Gheissari?Peled, arXiv:2609.01499v2 (7 October 2026), Section 2.4, printed/PDF p.14. It studies integer heights on Z^d (d >= 1), translation-invariant nearest-neighbor directional potentials V_i: Z -> R union {infinity}, convex on a nonempty interval of finite values and coercive at both ends. The non-crossing example separately relaxes coercivity in one direction. A gradient measure is a law of heights modulo additive constants, equivalently a curl-free edge field. Ergodic means translation invariant and ergodic for the full Z^d action. A finite slope means all coordinate increments are integrable. S consists of s for which both V_i(floor(s_i)) and V_i(ceil(s_i)) are finite. Minimality is SFE(mu)=tau(s), where tau is the infimum over all translation-invariant gradient laws of slope s, not just Gibbs laws.

The two questions are: (F) every ergodic gradient Gibbs measure with slope in int(S) has finite SFE; (M) every such measure with finite SFE is minimal. Neither has been settled here in this full class. Sheffield's original conjectures are broader (perturbed simply attractive potentials); this attempt uses the integer-valued directional setup of the current source.

## Results proved and audited
1. Integrable gradients imply finite finite-volume gradient entropy with a bound proportional to volume.
2. In the integer-valued coercive setup, integrable gradients have finite SFE exactly when each directional potential has finite expectation.
3. Both (F) and (M) for potentials finite on all integers, coercive, convex, and with bounded discrete derivatives; an independent boundary-entropy proof is written in Section 3 and audited in Section 5. These include anisotropic linear SOS interactions, but are a special case and fall within the bounded-comparability perturbed-isotropic regime of Sheffield. No novelty claim.
4. Second attempt: a universal exponential bound for single-site thermal excess, a reduction to expected local minimum energy, a valid nonergodic DLR negative control, and the full one-dimensional convex case (Sections 8-14).

## History warning
The read-only origin/master I0008 terminal report of 17 September 2026 records a failed deterministic anisotropic shell interpolation route; its no-go statement is a lead, not a checked theorem in this attempt. It does not refute either conjecture. The old report's operational instructions are not instructions for this new task.


## 1. Countable entropy lemma (proved)
Use natural logarithms. If Y is integer valued and M=E|Y|<infinity, then

    H(Y) <= 1 + log(3(M+1)).                                      (E1)

Proof. Put a=1/(M+1), and q(k)=exp(-a|k|)/Z_a. Since exp(-at) is decreasing,
Z_a=1+2 sum_{k>=1} exp(-ak) <= 1+2/a <= 3(M+1).
The countable Gibbs inequality gives H(Y)<=E[-log q(Y)]=aM+log Z_a. For completeness, this inequality also follows without assuming entropy finite: partition Z into {-N,...,N} and its complement, apply the finite Gibbs inequality to this finite partition, and observe that the coarse reference self-information on the complement is at most -log q(k) for each k in it. The entropies of these successively refined partitions increase to H(Y). Thus the bound holds by monotone convergence. Since aM<=1, (E1) follows.

For a connected finite vertex box Lambda and its internal gradient vector G_Lambda, choose any spanning tree T. The increments on T determine all heights modulo a constant, and hence determine G_Lambda. Conversely G_Lambda determines T. They therefore have equal entropy. Subadditivity gives

    H(G_Lambda) <= sum_{e in T} H(eta_e) <= (|Lambda|-1) C_mu,      (E2)

where C_mu=max_i {1+log(3(E|eta_i|+1))}<infinity for an invariant measure with integrable coordinate gradients. Reversing an edge does not change this bound. No independence or Gibbs property was used.

## 2. Exact energy-integrability reduction (proved)
Suppose the directional potentials are convex and coercive on nonempty integer intervals, and mu is an invariant gradient law with integrable gradients. In the source convention for SFE, then

    SFE(mu)<infinity  iff  E_mu V_i(eta_i)<infinity for all i.    (R)

Here use the existence and finite lower bound of the SFE limit proved in Sheffield, Lemma 2.3.4 and its following discussion, as cited in source Section 2.3. This is an imported theorem, not an independently proved existence assertion.

Proof. Each V_i is bounded below by a finite constant m_i: coercivity reduces the search for its minimum to a finite nonempty set. For Lambda_n=[-n,n]^d and N_n=(2n+1)^d the internal energy expectation is exactly

    E H_free = [2n(2n+1)^(d-1)] sum_i E V_i(eta_i).               (R1)

If every expectation is finite, (E2) gives a finite lower bound per volume, and H>=0 gives a finite upper bound per volume, for E H_free-H(G_Lambda). Thus the existing SFE limit is finite. If one expectation is infinite, E H_free=infinity in every n>=1, while (E2) makes H(G_Lambda) finite. Every finite-volume free energy is then infinity, so SFE=infinity. There is no infinity-minus-infinity cancellation. This proves (R).

Consequently, if every V_i has a linear upper bound A_i+B_i|k| on all Z, every integrable-slope invariant gradient law has finite SFE; ergodicity and DLR are unnecessary for this finiteness conclusion. Hard constraints with infinity outside an interval require separate admissibility and are not included in this upper-bound hypothesis.

## 3. Restricted theorem: bounded discrete derivatives (proved)
Assume d>=1; every V_i:Z->R is finite, convex and coercive; and

    |V_i(k+1)-V_i(k)| <= L_i for all k in Z.                    (BD)

Then every translation-invariant, Z^d-ergodic gradient Gibbs measure mu with finite slope s has finite SFE and is minimal at s. Here S=R^d, so all slopes are interior. In particular this holds for unequal directional SOS couplings V_i(k)=beta_i|k|, beta_i>0. The theorem excludes superlinear potentials, finite-domain hard constraints, and the non-coercive non-crossing direction.

### 3a. L1 sublinearity of an integrable ergodic cocycle
Write h(x)=phi(x)-phi(0), and eta_i=h(e_i). For n>0 let
A_n^i=n^(-1) sum_{k=0}^{n-1} eta_i composed with theta_(k e_i).
The L1 ergodic theorem (conditional on the e_i-invariant sigma-field; no directional ergodicity is assumed) yields A_n^i -> g_i in L1.
The cocycle identity gives, for every j,

    n(A_n^i composed with theta_ej - A_n^i)
        = eta_j composed with theta_(n ei) - eta_j.

Thus the L1 norm of this difference divided by n is at most 2 E|eta_j|/n. Taking the L1 limit shows g_i is invariant under every theta_ej. Full-group ergodicity makes g_i constant, and its expectation is s_i. Hence

    E|h(n e_i)-n s_i|=o(n).

For negative n the same bound follows by translating the reversed path. For arbitrary x, decompose its path into coordinate segments; stationarity and the triangle inequality give

    E|h(x)-s dot x| <= sum_i r_i(|x_i|),

where r_i(k)=E|h(k e_i)-k s_i| and r_i(k)=o(k), with the reversed-path convention for negative coordinates. For each fixed C,
max_{0<=k<=Cn} r_i(k)=o(n): given epsilon, take K with r_i(k)<=epsilon k for k>=K, and bound the finite set k<K by its maximum. It follows that

    sup_{|x|_infinity<=Cn} E|h(x)-s dot x|=o(n).                (SL)

The conclusion is in expected value; no unproved pointwise uniform cocycle theorem is being invoked.

### 3b. Entropy and the conditional partition function
Take Lambda_n=[-n,n]^d, and B_n its external vertex boundary. Choose a_n=(-n-1,0,...,0) in B_n, and represent heights by phi(a_n)=0. Let X_n be the vector of interior heights, and Y_n the vector of boundary heights in this representative. These are well-defined gradient observables. Write Z_n(b) for the ordinary DLR partition function with boundary vector b, using all edges touching Lambda_n.

A nearest-neighbor path from a_n to any site in Lambda_n union B_n has O(n) edges. Integrability and invariance imply E|phi(x)-phi(a_n)|<=C n, uniformly in these sites. Applying (E1) and entropy subadditivity yields

    H(Y_n)=O(n^(d-1) log(n+1)).                                (B1)

For d=1 the boundary has two sites, and the same bound is O(log(n+1)). Let G_n be the internal gradient vector. X_n is determined by G_n and one interior height X_n(0), and G_n is determined by X_n. Thus

    0 <= H(X_n)-H(G_n) <= H(X_n(0))=O(log(n+1)).                (B2)

All these entropies are finite, including H(X_n), by (E2), (E1), and (B2). Since the DLR kernel depends only on boundary height differences, conditioning on the whole outside and then using the tower property gives exactly

    Law(X_n | Y_n=b)(x)=exp(-H_n(x,b))/Z_n(b).

Conditional entropy therefore obeys

    H(X_n|Y_n) = E H_n(X_n,Y_n) + E log Z_n(Y_n).               (B3)

There are O(n^(d-1)) crossing edges. Under (BD), |V_i(k)|<=|V_i(0)|+L_i|k|, so their expected total absolute energy is O(n^(d-1)), by invariance and integrability. All energy terms are integrable. Equation (B3) involves integrable log Z: for each boundary, log Z=H(kernel)-E_kernel H_n; H_n has a deterministic lower bound proportional to the number of edges, so the positive part of log Z is bounded by H(kernel) plus that constant, and its negative part by the expected positive energy. Taking expectations proves integrability. The conditional entropy averaged over Y_n is finite since it is at most H(X_n).

Finally 0<=H(X_n)-H(X_n|Y_n)<=H(Y_n). Combining (B1)-(B3) and the crossing-edge bound gives

    [E H_free-H(G_n)]/N_n
         = -E log Z_n(Y_n)/N_n + o(1).                        (B4)

The constants may depend on the measure but not on n.

### 3c. Compare two ergodic Gibbs laws of the same slope
Let mu and nu be ergodic gradient Gibbs laws with finite slope s, sampled independently, and pin each at the same a_n. For each fixed interior configuration x, global Lipschitz continuity on Z (obtained by telescoping (BD)) gives

    |H_n(x,b)-H_n(x,b')|
        <= D_n(b,b') := sum_crossing_edges L_i |b(y)-b'(y)|.   (P1)

Internal edges cancel. Exponentiating and summing over all integer interior configurations gives

    exp(-D_n) Z_n(b') <= Z_n(b) <= exp(D_n) Z_n(b'),
    |log Z_n(b)-log Z_n(b')| <= D_n.                          (P2)

Both partition functions are positive and finite by coercivity (the source's admissibility criterion). Countable summation is justified by monotone convergence from finite subsets. The finite upper bound in (P2) is formalized in PartitionComparison.lean; reversing H and K yields its lower bound.

For y in B_n, stationarity allows replacing the pinned increment from a_n to y by h(y-a_n) in (SL). The deterministic mean s dot(y-a_n) cancels between the two laws. Uniformly in y,

    E|b_mu(y)-b_nu(y)|
       <= E|b_mu(y)-s dot(y-a_n)| + E|b_nu(y)-s dot(y-a_n)|
       = o(n).

Since there are O(n^(d-1)) crossing edges, E D_n=o(n^d). Thus (P2) and (B4) imply

    SFE(mu)=SFE(nu).                                         (EQ)

Both quantities are finite by (R) and (BD).

### 3d. Finish minimality
Use the existing minimal-phase existence theorem for simply attractive potentials, Sheffield Lemma 8.2.7 (printed p.107, PDF p.109) gives an ergodic gradient phase at every interior slope, and Lemma 8.2.8 (printed p.108, PDF p.110) explicitly states that this constructed phase is minimal, with SFE(mu_u)=sigma(u). Take nu to be such a phase. Its gradients are integrable by Sheffield Lemma 2.3.8. Then (EQ) gives SFE(mu)=SFE(nu)=tau(s), proving minimality.

This invokes the established existence of a minimal phase, not the conjectural converse variational principle. Alternatively, the restricted class can be placed in the perturbed ISAP class and Sheffield Theorem 6.3.1 applied directly (see below). This independently cross-checks the conclusion.

## 4. Why the restricted theorem is already compatible with known results
Convex coercive finite V_i with (BD) admit constants c>0, C<infinity, K<infinity, common to all directions, with

    c|k|-K <= V_i(k) <= C|k|+K.

The upper bound follows from (BD). For the lower bound, choose a positive discrete slope to the right and a negative discrete slope to the left, which exist by coercivity; convexity bounds the tails below by the corresponding supporting affine functions. Adjust K for the finitely many central sites and take the minimum positive slope over directions.

Add the same constant A>=K+c to each V_i, so W_i=V_i+A satisfies c(1+|k|)<=W_i(k)<=B(1+|k|) for some finite B>=c. The isotropic even potential U(k)=B(1+|k|) dominates W_i. Put Psi_i=W_i-U. Then

    |Psi_i(k)| = U(k)-W_i(k) <= (1-c/B) U(k).

Choose any theta strictly between 1-c/B and 1. The sum of perturbation absolute values over any finite set of edges is at most theta times the isotropic energy. Thus W=U+Psi is a perturbed ISAP in Sheffield's strict-domination definition (the original potentials differ only by constants per edge). Theorem 6.3.1 therefore applies in this restricted class. The boundary proof above is not a claim of previously unknown anisotropic minimality.

## 5. Hostile referee audit and exact remaining gap
- Finite slope is interpreted as integrability, not a conditionally defined or principal-value mean. Otherwise (E1) and the L1 ergodic theorem are unavailable.
- Full-group ergodicity does not imply ergodicity along an axis. Section 3a explicitly proves that the directional conditional drift is full-group invariant before making it constant.
- Gradient DLR does not provide absolute heights. Section 3b pins at an exterior site, which remains fixed under every interior update; all variables are measurable on the quotient.
- Entropies are finite before chain rules and subtraction are used. The root-height correction is O(log n), and boundary entropy is O(surface log n).
- The crucial bound (P1) is uniform in interior heights ONLY because the discrete derivatives are bounded. For V(k)=k^2, changing the boundary from 0 to 1 produces V(z)-V(z-1)=2z-1, unbounded in the interior height z. Finite SFE supplies integrability of V(eta) along actual edges, but not the uniform mismatch bound for an independently sampled boundary. This is the precise failure of the argument in the general anisotropic class.
- Statement (R) uses Sheffield's established SFE-limit theorem; all subsequent deductions from it are proved here.
- Existence of a minimal same-slope phase is imported from Sheffield's established theory, with its exact source identified, and not inferred from the conjecture.

The unresolved finiteness problem is now precisely: for general coercive convex directional V_i, does DLR plus full-group ergodicity and E|eta_i|<infinity imply E V_i(eta_i)<infinity for every i? The unresolved minimality problem is to replace (P1)-(P2), or another step, by a volume-negligible comparison for superlinear anisotropic interactions under finite SFE. No counterexample satisfying all the source hypotheses has been produced. The full problem remains open in this attempt.


## 6. Counterexample search: why the Gibbs hypothesis is indispensable
This is a counterexample to dropping DLR, not to I0008. Let xi_x be independent integer-valued heights with

    P(xi_x=k)=c/(1+|k|)^3, k in Z,

where c normalizes the summable mass function. This law is symmetric, E|xi_x|<infinity, and E xi_x^2=infinity, by comparison with sum k^(-2) and sum k^(-1), respectively. Let eta_(x,y)=xi_y-xi_x. This is a curl-free, invariant, full-group ergodic gradient field (a factor of an iid shift), with finite slope zero. Each increment is integrable. For anisotropic quadratic potentials V_i(k)=beta_i k^2, beta_i>0, it has infinite expected energy: conditioning xi_y=0, an event of positive probability independent of xi_x, already gives E(eta_(x,y)^2)=infinity. By (R), its SFE is infinite; S=R^d, so its slope is interior.

It is NOT gradient Gibbs. Here is a full check, including the quotient issue. Pin the outside at any a outside a fixed single-site region {0}. The outside height-difference field gives xi_x-xi_a for all x!=0. The spatial averages of these quantities over boxes avoiding 0 converge almost surely to -xi_a by the iid ergodic theorem, since E xi_x=0. Hence xi_a, and then every outside absolute height xi_x, are measurable from the outside gradient quotient. Conversely outside gradients are measurable from these absolute heights. Thus the two outside sigma-fields agree modulo null sets for this law. Conditional on this sigma-field, the central absolute height has the original independent polynomial-tail distribution p(k).

For the quadratic DLR kernel, its probability ratio at consecutive heights would instead be

    q(k+1)/q(k)
       = exp(-sum_i beta_i [4k+2-2(xi_ei+xi_-ei)]),

which tends to zero as k->+infinity. The independent law has p(k+1)/p(k)=((k+1)/(k+2))^3 ->1. These conditional laws disagree for every finite exterior boundary. Pinning just translates the central coordinate and does not repair this disagreement. The candidate fails DLR and is rejected.

This verifies that the integrability problem cannot be solved by invariant ergodic cocycle theory alone; the DLR equations must supply a genuinely additional constraint.

## 7. Finite and formal checks actually run
- `python -X utf8 boundary_experiment.py`: seed 8008, 100 boundary pairs on a 2x2 square, 8 exterior boundary sites, beta=(1,3), 625 interior configurations per boundary. Checked (P1) by exact integer arithmetic and (P2) for the truncated common configuration set using floating logarithms. All 62,500 configuration comparisons passed. Raw results are in experiment_results.json. This is a finite sanity check, not a numerical proof of the infinite-volume theorem.
- The same script records the exact quadratic mismatch values 1,19,199,1999 at interior heights 1,10,100,1000 for a unit boundary change. The symbolic identity 2z-1 proves unboundedness; these values only check arithmetic.
- `lake env lean ~/brain_workers/TRIO_1011/op/I0008/PartitionComparison.lean`, from ~/lean_verify, exited 0 in 78.99 seconds. The Python launcher allowed 3600 seconds for this shared-computer check. Two finite partition bounds were checked. `#print axioms` lists only propext, Classical.choice, Quot.sound; no sorry or native_decide occurs. The infinite sums, logarithms, ergodic theory and entropy proof are handwritten, not Lean-formalized. Full output is in lean_check.txt.

Final audit: all imported results are identified; all new mathematical conclusions are restricted/reduction results. Neither general conjecture is claimed proved or refuted.


# Second serious attempt ? 2026-10-12

## 8. Two new approaches and selection
**Approach A: canonical redistribution and de Finetti.** In dimension one, an interior-site update redistributes two adjacent increments while fixing their sum. The equal directional interaction makes their Gibbs weight permutation invariant. Adjacent-swap invariance may imply exchangeability of the whole increment sequence; shift ergodicity would then yield an iid law, and the Gibbs split identity an exponential tilt of exp(-V). This would handle arbitrary coercive convex one-dimensional interactions, including asymmetric superlinear tails. The obstacle to a higher-dimensional extension is that a swap of individual edges generally violates curl-free cycle constraints. This route was not used in the first attempt.

**Approach B: discrete log-concave heat-bath excess energy.** Rather than comparing partition functions for independent boundaries, normalize the actual single-site conditional Hamiltonian by its own minimum. Convexity might give a uniform exponential moment for this excess, independent of the neighboring heights and of the growth rates of V_i. Then separate infinite global energy into a locally minimizing background and thermal fluctuations. This directly addresses the DLR-to-integrability gap in every dimension and was not used in the first attempt.

I select B first: it applies to the entire coercive convex directional class, including hard constraints, and has a finite algebraic core that can be checked without assuming finite SFE. The required extra step is to turn local excess-energy control into edge-energy integrability; it is not assumed. If it fails, identify the precise obstruction and test A as a fallback special case.

Brain query on the exact gap: `DLR gradient Gibbs convex anisotropic potential energy integrability finite first moment`. The store returned de la Vallee-Poussin uniform-integrability cards and unrelated Gibbs results, not a proof. A second query targets de Finetti/canonical exponential tilts. Store hints are not treated as established applicability claims.


## 9. Uniform thermal excess bound (proved for the full convex coercive class)
Let U:Z->R union {infinity} be convex with a nonempty interval of finite values, coercive on unbounded sides, and let p(k)=exp(-U(k))/Z. Choose an integer minimizer k0 (the smallest one if there are ties), and put W(j)=U(k0+j)-U(k0). Then W>=0, W(0)=0, and its finite domain is an interval containing 0. Write Z_t=sum_j exp(-t W(j)) for t>0, with exp(-infinity)=0.

For each finite-domain j, convexity along the segment from 0 to j gives

    W(trunc(j/2)) <= W(j)/2,                                  (H1)

where trunc rounds toward zero. Indeed for j>0, put r=floor(j/2). If r=0 this is W(0)=0<=W(j)/2. If r>0, convexity gives W(r)<=(r/j)W(j)<=W(j)/2; the negative side follows after reflecting j. Convexity also guarantees that r is in the finite domain. The preimages of 0 under trunc(j/2) are {-1,0,1}, and those of each nonzero integer contain exactly two integers. Therefore summing nonnegative terms gives the sharper comparison

    Z_(1/2) <= 2 Z_1 + 1 <= 3 Z_1.                            (H2)

A missing domain point simply contributes zero. For finite-domain j, (H1) implies exp(-W(j)/2)<=exp(-W(trunc(j/2))); summing by the fibers proves (H2). The first inequality follows because the weight at 0 is exactly 1 and its fiber multiplicity is at most 3; every other fiber has multiplicity at most 2. Infinite sums are monotone limits of finite sums, so no change of sign or unproved cancellation occurs.

For X sampled from p, Delta=U(X)-min U=W(X-k0)>=0. Equations (H1)-(H2) prove

    E exp(Delta/2) = Z_(1/2)/Z_1 <= 3,
    P(Delta>=t) <= 3 exp(-t/2) for all t>=0,
    E Delta <= 2 log 3.                                      (H3)

The exponential bound first gives finite E Delta (for example integrate the tail); Jensen's inequality can then be applied to obtain the stated mean bound. This proof does not assume that E U or the unnormalized minimum is controlled uniformly over a family.

### Application to the actual DLR kernel
At site x, pin any exterior site and denote neighbor heights by b. With the orientation convention of the source,

    U_b(k)=sum_i [V_i(k-b_(x-ei)) + V_i(b_(x+ei)-k)].

It is a sum of convex functions of k, its finite domain is an interval, and for an admissible exterior it is nonempty. Under the original coercive directional assumptions it is coercive; hence an integer minimum m_x(b) exists. DLR says that the conditional law of phi(x) is exactly proportional to exp(-U_b(k)). Consequently the gradient-measurable, nonnegative variable

    Delta_x=U_b(phi(x))-m_x(b)

satisfies, conditional on every admissible exterior,

    E[exp(Delta_x/2) | outside] <= 3,
    E[Delta_x | outside] <= 2 log 3.                           (D)

Thus these bounds also hold unconditionally under ANY gradient Gibbs measure in this convex coercive class, even without invariance, ergodicity, finite slope or finite SFE. Changing the representative of heights only shifts k and the b's together and leaves Delta_x unchanged.

## 10. Exact refinement of the remaining gap (proved reduction)
Let m_i=min V_i and replace V_i by V_i-m_i>=0. This leaves every DLR kernel unchanged and shifts SFE by a finite constant. For an invariant admissible gradient Gibbs law define the local ground-state energy

    M_x=min_k sum_i [V_i(k-phi(x-ei)) + V_i(phi(x+ei)-k)] >=0.

Then pointwise, without subtracting infinities,

    U_b(phi(x))=M_x+Delta_x,
    E U_b(phi(x))=2 sum_i E V_i(eta_i),                        (G1)

where the second identity uses invariance and is valid as an identity of nonnegative extended integrals. By (D), E Delta_x<=2 log 3 is finite. Therefore

    all edge-potential expectations finite iff E M_x finite.  (G2)

For an invariant integrable-slope law, Section 2 further gives

    SFE finite iff E M_x finite.                             (G3)

This is a genuinely different DLR reduction from the previous entropy reduction: thermal fluctuations above the conditional minimizer cannot themselves cause infinite SFE. The full finiteness conjecture is reduced to controlling the locally minimizing background using ergodicity, integrable slope, and compatibility among overlapping sites.

### Hostile check: the local minimum has no linear bound in neighbor oscillation
For d=1, V(k)=k^2 and exterior values phi(-1)=0, phi(1)=2K,

    M_0=min_j [j^2+(2K-j)^2]=2K^2.

Yet the exterior oscillation is 2|K|. Hence no inequality M_0<=C(1+oscillation) can hold with a boundary-independent constant. In any dimension the affine boundary phi(x)=K dot x has local energy sum_i [V_i(K_i+t)+V_i(K_i-t)], minimized at t=0 when the V_i are even convex; its minimum can grow superlinearly while the thermal excess remains controlled by (D).

These deterministic boundaries do not refute the ergodic conjecture: their slopes vary with K. The following exact Gibbs negative control checks whether DLR alone can exclude such a divergent background.


## 11. Explicit DLR counterexample when ergodicity is removed (proved)
This improves the previous negative control: it satisfies DLR, rather than failing DLR. It is NOT a counterexample to I0008, because it is not ergodic.

Work in d=1 with the source potential V(k)=k^2. Put

    Z0=sum_(r in Z) exp(-r^2),
    p_K(k)=exp(-(k-K)^2)/Z0, K in Z.

For each fixed K let mu_K be the gradient law with iid increments p_K. Every such sequence defines heights modulo an additive constant on Z, and is translation invariant and ergodic, of slope K.

### Full DLR verification
For a finite interval of interior heights, the outside gradient quotient specifies the increments outside the interval and the sum S of the increments between its two fixed endpoints. If the interval involves q updated increments, the iid law has conditional weight

    product_j p_K(a_j)
       = Z0^(-q) exp(-sum_j a_j^2 + 2K S - qK^2).

The last two terms are constant on the event sum_j a_j=S. Thus the conditional law is exactly proportional to exp(-sum_j a_j^2), the quadratic gradient Gibbs bridge. All sums are finite and positive: any fixed endpoint difference admits integer bridges, and the unconditioned sum probability is positive. For a finite region consisting of multiple disjoint intervals, the exterior quotient fixes each endpoint sum, the iid conditional laws factor across these disjoint sets of increments, and the Gibbs Hamiltonian factors as well. This proves DLR for every finite region, not only single-site updates. The relative offset between disconnected exterior pieces belongs to the outside gradient quotient; this is essential in d=1.

Let c normalize the probability weights w_K=c/(1+|K|)^3 and form

    mu=sum_K w_K mu_K.

The set of DLR measures for a fixed specification is closed under mixtures: for a bounded measurable f, each mu_K(gamma_Lambda f)=mu_K(f); integrate this identity against w to obtain mu(gamma_Lambda f)=mu(f). Therefore mu is a gradient Gibbs measure, invariant under translations.

Writing an increment as K+R with P(R=r)=exp(-r^2)/Z0, E|K|<infinity, E K=0, and E K^2=infinity by the same convergent/divergent series as in Section 6. Hence E|eta|<infinity and slope(mu)=0, an interior slope of S=R. But

    E[eta^2 | K]=K^2+v,  v=E R^2<infinity,

so E V(eta)=infinity and SFE(mu)=infinity by Section 2.

The empirical average of increments converges to K almost surely conditional on K, by the iid strong law. Its limit is shift invariant. The event that this limit is 0 has probability w_0 strictly between 0 and 1. Thus mu is not ergodic. Its mean slope zero must not be confused with its random component slope K.

For the single-site pair with total increment S, the local minimum is

    M_0=min_j [j^2+(S-j)^2]=ceil(S^2/2).

Indeed completing the square gives S^2/2+2(j-S/2)^2, with a zero correction for even S and a 1/2 correction for odd S. Since S=2K+R_1+R_2,
E[S^2|K]=4K^2+2v, so E M_0=infinity. Meanwhile E exp(Delta_0/2)<=3 by Section 9. Thus the exact combination ?DLR + invariant + integrable interior mean slope + uniformly integrable thermal excess? still permits infinite SFE. Ergodicity must enter in controlling the locally minimizing background, rather than in the thermal estimate itself.

### Consequence for selected approach B
The local excess proof is sound but cannot alone prove (F). A proof would need an additional ergodic rigidity estimate that excludes a heavy locally minimizing background with deterministic component slope. The mixture above cannot be made ergodic by merely changing the distribution of K: K is a global invariant variable. Allowing K to vary in space destroys the fixed-sum cancellation used in the DLR proof. This identifies a precise obstruction to a tempting construction, not an assertion that all ergodic backgrounds are rigid.


## 12. Fallback approach A: full one-dimensional convex theorem (proved special case)
**Theorem.** In d=1, let V:Z->R union {infinity} be convex and coercive, with nonempty interval I of finite values. Every translation-invariant ergodic gradient Gibbs law of an integrable slope s in int(conv(I)) is an iid increment law

    p_lambda(k)=exp(-V(k)+lambda k)/Z(lambda), k in I,

for some real lambda with Z(lambda)<infinity. It has finite SFE and is minimal at s. No symmetry of V, bounded derivative, comparability of its two tails, or prior finite-SFE assumption is required. This is a classical one-dimensional canonical-ensemble mechanism; no novelty claim is made. It is a stronger special case than Section 3 because it admits arbitrary asymmetric superlinear growth.

### Step A1: adjacent redistribution yields genuine infinite exchangeability
Index increments eta_j=phi(j+1)-phi(j), j in Z. In d=1 there are no cycle constraints. Resampling height phi(j) changes only eta_(j-1),eta_j and leaves their sum fixed. Under DLR, conditional on the outside quotient, the split has probabilities proportional to

    exp(-V(a)-V(S-a)).

This distribution is symmetric under a<->S-a. Hence the law of the entire gradient sequence is invariant under transposing the adjacent coordinates j-1,j: integrate the conditional symmetry against the outside law. An actual sampled edge lies in I almost surely, because the DLR law in any finite region containing its endpoints is supported on configurations with finite local energy. Countably many such regions cover all edges.

Finite permutations of integer coordinates are generated by adjacent transpositions. Thus the entire bi-infinite sequence is exchangeable. Apply the infinite de Finetti theorem to its positive-index restriction (a countable discrete state space is Polish). It is a mixture of iid sequences, with random directing pmf P, and the empirical frequency of each integer k converges almost surely to P(k). Deleting a first term does not change the empirical limit, so P(k) is invariant under the full one-dimensional shift. Ergodicity makes each P(k) a deterministic constant p(k). There are countably many k, so these statements hold simultaneously. All positive-index finite marginals are iid p; shifting any finite set of integer indices into the positive half-line proves that all finite marginals of the bi-infinite sequence are iid p.

This uses de Finetti for an INFINITE sequence. Exchangeability of a finite bridge alone would not imply independence. The one-dimensional shift, rather than exchangeability by itself, makes the directing law constant.

### Step A2: the marginal has the full allowed support
Let J={k:p(k)>0}, a nonempty subset of I. For any a,b in J, the sum a+b has positive probability. The iid conditional split must equal the Gibbs split. All (c,d) in I^2 with c+d=a+b have strictly positive Gibbs weight; therefore c,d must lie in J.

This redistribution closure implies J is an integer interval. Indeed for a<b in J and any c between them, d=a+b-c also lies between a and b and hence in I; redistribution puts c in J. If J has at least two points and has a finite lower endpoint a strictly larger than the lower endpoint of I, then a+1 is in J and a-1 is in I. The split (a,a) can be replaced by (a-1,a+1), so a-1 must be in J, a contradiction. The same argument at the upper endpoint applies using (b,b)->(b-1,b+1). Thus a nonsingleton J must equal I. If J={m}, and m is interior to conv(I), then m-1,m+1 are in I and the split (m,m) again contradicts closure. A singleton at an endpoint would have slope at that endpoint, excluded by the theorem's interior-slope hypothesis. Therefore J=I. If I is a singleton, its interior is empty and the theorem is vacuous.

### Step A3: the split identity forces an exponential tilt
For any a,b,c,d in I with a+b=c+d, equality of iid and Gibbs conditional split laws gives

    p(a)p(b) exp(V(a)+V(b))
      = p(c)p(d) exp(V(c)+V(d)).

All factors are finite and positive by Step A2. Set L(k)=log p(k)+V(k). Taking (a,b)=(k,k) and (c,d)=(k-1,k+1) at every interior integer of I yields

    2L(k)=L(k-1)+L(k+1).

Thus consecutive differences of L are constant, and L(k)=lambda k+C on I. This includes an interval with exactly two points, on which any function is affine. Normalization now gives C=-log Z(lambda) and the asserted p_lambda. Normalizability is established by the actual pmf, not assumed from an unjustified choice of a chemical potential.

Conversely, every normalizable iid p_lambda satisfies the full DLR equations: for any finite interval the endpoint sum S is fixed and its product weight is proportional to exp(-sum_j V(a_j)+lambda S). The linear term cancels from the conditional normalization. For disjoint intervals the argument factors as in Section 11.

### Step A4: arbitrary superlinear potentials still have finite expected energy
Put W(k)=V(k)-lambda k on I. It is convex and sum_I exp(-W)<infinity. On each unbounded end, summability implies W(k)->infinity. Convexity then supplies a supporting affine lower bound with strictly positive slope toward that end: choose two finite points with increasing W on a right tail, and convexity extends their secant slope as a lower bound beyond them; reflect for the left tail. Thus there are c>0,C<infinity with W(k)>=c|k|-C on I (bounded ends are absorbed into C). In particular W has a finite minimum m, and T=W-m>=0 has sum exp(-T/2)<infinity. Because t exp(-t)<= (2/e) exp(-t/2) for t>=0,

    sum_I T(k) exp(-T(k)) < infinity.

Consequently E_p T<infinity, E_p|k|<infinity, and E_p V=E_p W+lambda E_p k is finite. Since V is bounded below this expectation is unambiguous. Section 2 proves finite SFE.

### Step A5: minimality among ALL invariant same-slope laws
Let nu be any invariant gradient law of slope s, and r its one-edge marginal. Its first absolute moment is finite by the slope convention, so H(r)<infinity by Section 1. If E_r V=infinity, Section 2 gives SFE(nu)=infinity and it cannot beat p_lambda. If E_r V is finite, r is supported on I and the countable Gibbs inequality gives

    E_r V-H(r)=lambda s-log Z(lambda)+D(r||p_lambda)
               >=lambda s-log Z(lambda).

All terms in this identity are defined: H(r) is finite, E_r V is finite, and log p_lambda=-V+lambda k-log Z has finite absolute expectation after a finite lower-bound shift. For a box with N vertices there are N-1 gradients, whose joint entropy is at most (N-1)H(r) by subadditivity. The energy expectation is (N-1)E_r V. Divide by N and take the existing SFE limit to obtain

    SFE(nu)>=E_r V-H(r)>=lambda s-log Z(lambda).

For the iid p_lambda law the joint entropy is exactly (N-1)H(p_lambda), so equality is attained:

    SFE(mu)=lambda s-log Z(lambda)=tau(s).

This proves minimality without assuming a multidimensional converse variational principle. Dependence in a competitor cannot lower its free energy by increasing entropy beyond the iid marginal bound.

### Why this does not lift to d>=2
A permutation of edge increments generally violates the curl-free constraint. For one square take vertex heights phi(0,0)=0, phi(1,0)=1, phi(0,1)=0, phi(1,1)=3. Its positively oriented bottom/right/top/left increments are 1,2,3,0, and the cycle sum is 1+2-3-0=0. Swap the parallel bottom and top increments: 3,2,1,0 now has cycle sum 4, so it is not a height-gradient configuration. An equality of Gibbs weights cannot authorize this permutation. Single-site updates change all 2d adjacent gradients in a constrained way, not an arbitrary adjacent pair. Thus no exchangeability or iid conclusion in higher dimensions follows from this proof.

## 13. Second-attempt hostile audit and final gap
1. **No finite-SFE circularity:** Section 9 derives its exponential excess bound from a fixed conditional kernel alone. Section 10 uses nonnegative extended integrals until the excess is proved finite. Section 12 derives marginal energy integrability before evaluating its SFE.
2. **Hard constraints:** the halving proof only maps finite-domain integers toward a minimizing integer, staying within the interval domain. Missing indices contribute zero; infinity is never put into real-valued Lean arithmetic. The handwritten proof covers hard constraints, whereas the finite Lean formula covers the finite real terms with explicit halving assumptions.
3. **Ground state versus fluctuation:** E Delta finite does not imply E U finite unless E M is finite. The explicit DLR mixture in Section 11 demonstrates exactly this failure with integrable mean slope; it fails ergodicity, which is required by I0008.
4. **Quotient sigma-field in d=1:** outside endpoint differences, including differences between its disconnected pieces, belong to the outside gradient quotient. Fixed endpoint sums are therefore legitimate conditioning variables. Forgetting these relative offsets would give a different specification.
5. **Infinite versus finite exchangeability:** only after invariance under every finite permutation of the entire sequence do we invoke the infinite de Finetti theorem. Empirical directing probabilities are shift invariant and ergodicity makes them deterministic.
6. **Zeros in support:** the redistribution closure is proved before logarithms are taken. It forces full interval support at interior slope; frozen boundary slopes are not silently included.
7. **Arbitrary competitor class:** minimality is proved against all invariant integrable-slope gradient laws, not just Gibbs competitors. Infinite-energy competitors are ruled out using the proved entropy reduction, rather than undefined entropy differences.
8. **Novelty:** the dyadic estimate and one-dimensional canonical ensemble argument are elementary/standard mechanisms; no new general solution or priority claim is made.

The sharpened unresolved general finiteness assertion is: for d>=2, does an ergodic invariant gradient Gibbs law of integrable interior slope necessarily have E M_0<infinity, with M_0 the conditional single-site minimum for nonnegative shifted convex directional potentials? Thermal excess has a universal exponential moment, but no ergodic rigidity estimate for M_0 was proved. The general finite-SFE minimality assertion in d>=2, outside the known comparable/perturbed-isotropic and hard-constraint classes, still lacks a volume-negligible boundary or other variational comparison. Both full-source conjectures remain unresolved in this attempt.


## 14. Second-attempt checks actually run
- `HeatBathHalving.lean`: `lake env lean` from ~/lean_verify exited 0 in 53.03 seconds, with a 3600-second launcher timeout. It checks the finite paired-tail inequality and the two-sided halving bound under explicit real halving assumptions. Axioms: propext, Classical.choice, Quot.sound. No sorry or native_decide. Discrete convexity implies these assumptions in the handwritten proof; that implication, infinite sums, Jensen, and DLR conditioning are not Lean-formalized. Output: heatbath_lean_check.txt.
- `heatbath_experiment.py`: 300 convex finite-interval Hamiltonians generated by sorted random discrete slopes, seed 8108. Each was shifted by its actual minimum. All partition ratios Z_(1/2)/Z_1 and mean excess energies satisfied the proved bounds. Largest observed ratio 1.6962276463; largest mean excess 0.7525549139. These are floating checks, not universal-constant proofs.
- The same script checked 15 quadratic bridge/tilt comparisons (5 endpoint sums, 3 component slopes); all probability discrepancies were below 1e-13 on the shared finite truncation. It also computed partial moments of the exact heavy mixture to cutoffs 10,100,1000,10000: first absolute moments approach a finite value, while second moments increase logarithmically. Divergence itself is proved by the series in Section 11, not inferred numerically.
- `heatbath_boundary_cases.py`: deliberate singleton, two-point, flat-interval, one-sided linear and asymmetric-linear domains; and six tilted asymmetric potentials V(k)=k^2 for k<0, V(k)=exp(k) for k>=0, on a fixed finite domain [-30,12]. The latter has highly noncomparable tail growth. Checked fixed-sum bridge identities numerically across five sums for each tilt. The finite domain is a sanity check only; the infinite-domain theorem is proved analytically in Section 12. Results: heatbath_experiment_results.json.

Second-pass final verdict: PARTIAL. The general gap is precisely the one recorded in Section 13.
