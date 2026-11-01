# One original account funds every adaptive continuation of the finite interface

All logarithms are base two. This is a finite theorem, conditional on the specified original surplus having no previous expenditure beyond the stated bookings. No universal FEI premise is assumed.

## Statement and initial condition

For every labelled Boolean function v on three bits, set F(x,a,b,y)=-1 on x=0,a=1, v(y) on x=1,b=1, and +1 otherwise. The original canonical reference M has M(empty)=P(empty) and its conditional nonempty distribution is the matched-marginal maximum-entropy occupancy law. Write A=KL(P||M). Query a, coherently transport M and convert the two actual child references to their actual spectral products. The signed root debit is d_a=O_a+mean TC(F_a)-A. The same fixed canonical reference, fair extension on source-zero rows, and d_a are those of A064's two-conversion claim, independently reconstructed by A061; the exact imported d_a intervals are an explicit dependency below.

Let S=mean_a(4I(F_a)-H(F_a)). It is strictly positive for every one of the 256 cores, certified independently here from exact Walsh spectra and physical edges. It is one original EXPECTED account, not two available copies of child certificates. Suppose it has not otherwise been spent. Thereafter permit any adaptive policy: at every actual history stop, or query any remaining physical coordinate; each query explicitly converts the coherently transported incoming product reference to the children's actual products. Branches may choose different coordinates and different stopping depths. At most five further coordinates remain. No further occupancy restart is admitted.

There is a nonnegative reference potential R on every reached history, common to all these policies, with initial value

    R_root = A + W,       0 <= W < S/20.

For every such policy and every stopping cut tau,

    E R_tau + E sum_{queried nodes before tau} O_node <= A+W < A+S/20,
    E CE(P_tau, reference_tau) + E sum O_node
        <= A+W+E H(F_tau).

At the root-stopping cut the reference remains M, so its boundary bill is H(F)+A, rather than a free root product. At every later stopping history the product boundary KL TC is retained, plus the unspent worst-continuation reserve specified below. At a full coordinate completion H=TC=reserve=0. Zero influence/dummy coordinates are allowed. Every reference-only row participates in predictions, including rows with source mass zero. The root bank is never renewed. The strict numerical constant 1/20 is a rigorous finite certificate, not an assertion for arbitrary-dimensional cores.

## Product-query quantities and source support

For any actual reached function g write p for its squared Fourier distribution and d_j=Inf_j(g). Its incoming reference is exactly Q=product Bernoulli(d_j), and K(g)=KL(p||Q)=sum_j h2(d_j)-H(g). This reference contains source support: if d_j=0 or 1 then every source atom has that forced indicator. At a query i, q(T)=p(T)+p(T+i). Set k(b|T)=p_b(T)/(2q(T)) if q(T)>0, and k=1/2 otherwise. Erase Q to Q_e, and let r_b=sum_T Q_e(T)k(b|T). Since Q_e supports q and the actual child has total mass one, r_b>0. Both r_b sum to one even when Q_e has reference-only rows. The actual physical outcome remains fair. Define

    O(g,i) = KL((1/2,1/2)||(r_0,r_1)) = -log2(4r_0r_1)/2,
    D(g,i) = O(g,i) + (K(g_0)+K(g_1))/2 - K(g).

The actual Bayes normalization and conditional KL are included in D. The existing common-kernel chain identity gives D=sigma-E; neither erasure credit nor conditional KL is dropped. A distinct expression used to audit the implementation is

    D = O + B_i + JS_i - h2(d_i)
        - sum_(j!=i) [h2(d_j)-mean_b h2(d_j(g_b))].

This follows by substituting K=sum h2-H in the definition and using H-mean H_child=B_i+JS_i. Each remaining d_j is the mean of its two child influences, so the final bracket sum is nonnegative. This formula is an audit identity, not an unproved local price bound.

## Coverage of every adaptive policy

Define T(g)=0 in dimension zero. In every other dimension define

    T(g)=max(0, max_i( [D(g,i)]_+ + (T(g_0)+T(g_1))/2 )).

The dimension strictly decreases, so this is a finite recursion; no limiting or uniform-integrability assumption is involved. Backward induction proves that T(g) is the largest expected sum of future positive bookings over all adaptive policies, including stopping. Indeed fixing the next coordinate leaves independent policy choices in its two physical branches; taking the supremum of their expected arithmetic mean therefore gives the mean of the two finite maxima. This is a finite decision recursion, not multiplication of conditional bounds or an independence assumption on random increments. Identical truth tables with their remaining ordered coordinates have identical quantities, so table-key memoization loses no choice. Dummy coordinates remain and are considered.

For every post-root history set R(g)=K(g)+T(g). At the original root set W=[d_a]_++mean_a T(F_a) and R_root=A+W. At a product query,

    R(g)-mean_b R(g_b)-O(g,i)
      = T(g)-mean_b T(g_b)-D(g,i) >= [D(g,i)]_+-D(g,i) >= 0.

The analogous root inequality is immediate from its definition. All potentials are nonnegative by Gibbs and the nonnegative recursion. Applying the one-step conditional inequality successively along a bounded tree proves the stopping-cut assertion. Full terminal cross-entropy is H+K, while R>=K, which proves the second inequality. These standard accounting identities are restated to delimit this new finite certificate; no new universal telescope is claimed.

The formal algebraic check uses integer-scaled values: if 2r >= max(0,2o+k0+k1-2k)+r0+r1, then 2o+(k0+r0)+(k1+r1)<=2(k+r). This is exactly the one-step inequality after clearing a common positive denominator. It does not formalize real logarithms, Gibbs, the chain identity, finite quantifier coverage, or the source root brackets.

## Exact certificate and boundaries

The source EXHAUSTIVE_CHECK.json from A061 stage6 has SHA256 6c48a94c44b030dfb851f33d99024e9fa91c7761dbfbd1bee400aa01862d2582. Its 12 root-debit records per core must agree exactly; the checker checks that agreement before importing one outward interval. All subsequent spectra, product laws, physical child functions, influences, outcome kernels, predicted probabilities, signed debits and adaptive maxima are recomputed here independently. This certificate is therefore conditional on the already reviewed canonical root transaction, not a claim to have independently recomputed that root reference. The source's stricter fixed-three-query bound is not used to bound future policies.

Integer FWHT yields rational square spectra, and direct cube-edge counting separately checks every influence. Log2 intervals use the positive atanh series on normalized arguments u in [1,2]: z=(u-1)/(u+1), sum through z^63/63 and tail at most 2z^65/(65(1-z^2)). Since 0<=z<=1/3 the denominator is positive. Every intermediate log bound is rounded outward to the 2^-96 grid. Bounds for ln2 are treated with the appropriate denominator endpoints. All positive parts, averages and maxima use interval monotonicity, so an interval for T encloses every actual policy maximum even if two candidate orders cannot be separated. Strict payment signs use rational upper/lower endpoints only. No floating sign or overlap test establishes the payment theorem; interval-overlap checks only audit identities already derived in the text.

The fixed job covers all 256 labelled cores, 12,050 memoized restrictions and 34,448 physical query candidates counted with per-core multiplicity, and 1,920 reference-only query candidates. It passes 341,120 exact assertions in 38.694323 seconds. All 256 certified upper bounds obey 20W_upper<S_lower; thus more than 19/20 of the SAME original owner remains after any admitted history. Every possible stopping boundary retains its own K and H, rather than being assigned zero at the last checked query. The largest certified W_upper/S_lower occurs at core mask194, bounded by 457878917272681913278273703463/10529204247165421408157486164012 < 1/20.

## First unsupported universal line

For an arbitrary-dimensional non-flat remaining core, there is no proof here that the original S is a nonnegative eligible previously unused bank, nor that a selected continuation has W below its remaining capacity. The theorem removes the restriction to common, fixed short query schedules in the finite three-bit interface; it does not remove that core-dimension or ownership hypothesis. The next useful action is to derive a structural estimate on actual product-query D from the signed formula above, comparing it with the one remaining ancestor account and full H+TC boundaries, or exhibit a genuine Boolean failure of that estimate. Another finite-depth extension of this already completed interface is unnecessary.
