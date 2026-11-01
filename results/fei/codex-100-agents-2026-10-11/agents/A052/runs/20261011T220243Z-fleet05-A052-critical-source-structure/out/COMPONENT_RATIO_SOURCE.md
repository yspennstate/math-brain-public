# Actual connected components do not preserve maximum raw Fourier ratio

1 October 2026. Natural logarithms throughout. **Unrestricted uniform-cube FEI remains open.** No novelty, formal-verification, or universal-entropy-payment claim is made. This package is local and unpublished, pending independent review.

## Result and its precise scope

There is an exact seven-dimensional indicator whose two actual Hamming-connected components both have smaller raw Fourier entropy / indicator Dirichlet-energy ratio than their union. Thus the surviving unrestricted component-pruning claim

    R(1_A + 1_B) <= max(R(1_A), R(1_B))

is false, even for exactly two actual connected components with minimum distance three. The witness is a smaller parameter specialization of the already archived star-times-cube plus opposite-singleton construction. This is a new checked scope rejection within this research pass, not a claim that the construction or theorem is new in the literature.

The result does **not** refute strict physical-ratio-criticality implying connected support. An explicit proper physical restriction has larger ratio than the witness, so that hypothesis fails. The Boolean-middle lifetime and actual source-sensitive entropy-transfer obligations are untouched.

## 1. Conventions and statement

Use the uniform binary cube {0,1}^7, written (y,x), with y in {0,1}^4 and x in {0,1}^3. For a real function h,

    hhat(S) = 2^-7 sum_z h(z) (-1)^(S dot z),
    Hraw(h) = sum_S hhat(S)^2 ln(1/hhat(S)^2),
    E(h) = sum_i E_z [(h(z)-h(z xor e_i))/2]^2
         = sum_S |S| hhat(S)^2.

Include the empty coefficient in Hraw; every zero term contributes zero. R(h)=Hraw(h)/E(h) is used only when E(h)>0. These are unnormalized squared coefficients of indicators, not a probability-law entropy. All physical restrictions inherit the same 0/1 orientation.

Set

    A = {y: wt(y)<=1} times {0,1}^3,
    B = {(1111,000)},
    a = 1_A, b = 1_B, g = a+b.

Then

    E(a)=3/8,  E(b)=7/256,  E(g)=103/256,
    R(a) < R(b)=4 ln2 < R(g).

The exactly enclosed ratios are

    2.752783270380521 <= R(a) <= 2.752783270380522,
    2.772588722239781 <= R(b) <= 2.772588722239782,
    2.775426599558637 <= R(g) <= 2.775426599558638.

In particular R(g)-max(R(a),R(b)) > 0.0028. The displayed decimal endpoints are rational numbers certified by exact arithmetic, not floating estimates.

## 2. These are exactly the actual connected components

The four-dimensional star {0000,1000,0100,0010,0001} is connected. Its Cartesian product with a full three-dimensional cube is connected, so A is connected and has 5*8=40 points. B is a singleton. Every point of A is at Hamming distance at least three from B; the minimum three is attained at any data leaf of the star with control label 000. Consequently no edge joins A to B, and A,B are exactly the two connected components of A union B. Their union has 41 points. This is not merely an arbitrary partition into graph-separated subsets.

## 3. Fourier numerators and exact raw entropies

Write a Fourier label as (T,U), where T is a subset of the four data coordinates and U is a subset of the three controls. Put k=|T| and N=128. Summing over the controls gives

    N ahat(T,U) = 8(5-2k) if U is empty, and 0 otherwise,
    N bhat(T,U) = (-1)^k for every U.

Indeed, the data-star character sum is 1+sum_{j=1}^4 (-1)^(1_{j in T})=5-2k. B has all data bits one and all control bits zero. Thus, at U empty, g has signed integer numerators

    41, 23, 9, -9, -23

for k=0,1,2,3,4, with binomial multiplicities 1,4,6,4,1. The seven nonempty control labels contribute 7*16=112 further numerators of absolute value one. The absolute numerator histograms are

    a: 40 once, 24 five times, 8 ten times, 0 112 times,
    b: 1 128 times,
    g: 41 once, 23 five times, 9 ten times, 1 112 times.

Their squared numerator sums are respectively 5120,128,5248, equal to N times the support sizes and consistent with Parseval. For any of these histograms,

    Hraw(h) = [14 ln2 sum_S W_S^2 - 2 sum_{W_S !=0} W_S^2 ln|W_S|]/16384.

Factoring the integer numerators yields

    Hraw(a) = [40960 ln2 - 5760 ln3 - 3200 ln5]/16384,
    Hraw(b) = 1792 ln2/16384 = (7/64) ln2,
    Hraw(g) = [73472 ln2 - 3240 ln3 - 5290 ln23 - 3362 ln41]/16384.

These formulas are also independently reconstructed by the direct-Walsh checker from the 128-point truth tables; the histograms are asserted against the direct transform rather than used as its input.

## 4. Exact energies and ratio comparisons

For an indicator on this cube, every undirected boundary edge contributes 1/(2N)=1/256 to E: both endpoints have derivative magnitude 1/2. Each of the four data leaves of A has three outgoing data edges, and there are eight copies under the control cube. Hence A has 4*3*8=96 boundary edges and E(a)=96/256=3/8. B has seven boundary edges. Since there is no cross edge, the union has 103 boundary edges, proving the stated energies and exact additivity.

The singleton formula gives R(b)=4 ln2. The two required signs have particularly short exact integer certificates:

    4 ln2 E(a) - Hraw(a)
      = [45 ln3 + 25 ln5 - 128 ln2]/128 > 0,

because 3^45*5^25 > 2^128; and

    Hraw(g) - 4 ln2 E(g)
      = [47104 ln2 - 3240 ln3 - 5290 ln23 - 3362 ln41]/16384 > 0,

because

    2^23552 > 3^1620 * 23^2645 * 41^1681.

The checker performs these comparisons directly with Python arbitrary-precision integers. No floating logarithm is needed to prove the counterexample.

For explicit enclosures, the checker separately uses rational logarithm intervals. For p/q>=1, put z=(p-q)/(p+q). For m>=1,

    L_m = 2 sum_{j=0}^{m-1} z^(2j+1)/(2j+1),
    L_m <= ln(p/q) <= L_m + 2 z^(2m+1)/[(2m+1)(1-z^2)].

The remainder follows by replacing each omitted denominator by its first possible value and summing a geometric series. Range reduction writes ln p = k ln2 + ln(p/2^k), k=floor(log2 p); the latter atanh argument lies in [0,1/3]. All 32-term sums, tail bounds, and sign-sensitive linear combinations are Fraction arithmetic. They certify

    0.002837877318856 <= R(g)-R(b) <= 0.002837877318857,
    0.019805451859259 <= R(b)-R(a) <= 0.019805451859260.

For comparison with the already rejected additive claim,

    0.008568846649731 <= Hraw(g)-Hraw(a)-Hraw(b)
                      <= 0.008568846649732.

The ratio comparison is strictly stronger than merely finding this positive raw entropy excess: here the energy-weighted margin over the larger component ratio is also positive.

## 5. Strict physical-criticality explicitly fails

Fix two of the data bits to zero, leaving the other two data bits and all three control bits free. B disappears. The remaining indicator is the complement of one point on the two free data coordinates, with controls irrelevant. Its support on that two-cube is {00,01,10}, so it is the reflected OR2 indicator. Its ratio is

    rho_desc = 12 ln2 - (9/2) ln3 = 3.3740108677... .

The restriction is NAND2 in the displayed binary coordinates, and is OR2 after reflecting both remaining input bits. No output complement is taken. The exact checker certifies rho_desc-R(g)>0.59. This is a proper nonconstant physical restriction with larger ratio, which proves that g is neither a strict core nor a non-strict all-descendant raw-ratio maximizer. No status of its complement is substituted for the inherited orientation.

Thus the unrestricted component-ratio-max shortcut is rejected, but a proof restricted to actual all-descendant physical-critical indicators needs a different argument and remains unrefuted by this example. Components are not themselves generally physical restrictions.

## 6. Tensor amplification preserves this scoped obstruction

For every m>=1, form G_m=product_{j=1}^m g(z_j) on disjoint seven-coordinate blocks. Its support is (A union B)^m. The 2^m Cartesian products obtained by independently choosing A or B in each factor are exactly its connected components: each product is connected, and any edge stays within its factors' original connected components.

For any nonzero indicators u,v of means p_u,p_v, direct coefficient factorization proves

    Hraw(u v) = p_v Hraw(u) + p_u Hraw(v),
    E(u v) = p_v E(u) + p_u E(v).

When E(u v)>0, divide these identities by p_u p_v. The product ratio is the weighted average of the positive-energy factors' ratios with nonnegative weights E(u)/p_u and E(v)/p_v, at least one positive. A constant-one factor has Hraw=E=0 and contributes zero weight, so its undefined ratio is omitted. If both factors are constant one, no ratio is asserted. All A,B,g factors used below have strictly positive energy. In particular, with p_g=41/128,

    Hraw(G_m)=m p_g^(m-1) Hraw(g),
    E(G_m)=m p_g^(m-1) E(g),
    R(G_m)=R(g)>4 ln2.

Every component product has ratio at most 4 ln2, while B^m attains 4 ln2. Thus the same fixed positive failure occurs in arbitrarily large dimensions and with arbitrarily many actual components. This does not create an unbounded FEI ratio or an unbounded controlled-excess/energy ratio. The tensor argument is analytic; no tensor truth-table enumeration is claimed.

## 7. Comparison with the archived guards

- Addendum 11.44's nine-bit star-times-cube/opposite-singleton witness disproves raw entropy subadditivity, but it has R(A)<R(union)<R(B). The present choice of four data and three control bits retains the exact two-component geometry and changes the last ordering to R(A)<R(B)<R(union). The previously unrefuted unrestricted maximum-component-ratio claim is now rejected
- Addendum 11.43's finite strict-core enumeration through four bits is unchanged. This seven-bit example is not physically critical, so it does not refute the proposed universal strict-core connectivity theorem
- Addendum 11.35 proves a local decreasing-drift failure on actual Boolean-source middle histories without assuming criticality. Its address source has original influence Theta(ln N), and explicitly fails all-descendant raw-ratio criticality, so a one-time original-source payment, the integrated signed middle remainder, and a high-ratio critical/minimum-dimensional refinement remain unrefuted. The general Boolean-middle target is not asserted to require criticality. Addendum 11.36 separately extends the old supremum-variation-bank failure to genuinely all-descendant critical indicator powers, while its whole-indicator rigidity theorem and critical-source corollary retain their distinct hypotheses. The explicit OR2 restriction above likewise prevents this component-ratio witness from being mislabeled as a critical-source obstruction. The source-sensitive collective transfer and signed middle-history lifetime remain unpaid
- Addenda 11.41 and 11.42 separate the paid static anisotropic potential from entropy recovery and an all-coordinate local decrement failure. The present proof uses none of those estimates and provides no good-coordinate, adaptive-block, or global-potential result
- The whole-indicator atom-cap and mixed-derivative relaxation guards in 11.37/11.40 remain in scope. No relaxed non-Boolean law, dyadic realizability surrogate, or projection-row product rigidity is used here: the witness itself is an explicit genuine indicator

No component subadditivity or incoherent mixture is used anywhere in the argument. The union coefficients are summed with their actual signs before they are squared.

## 8. Executed verification and provenance boundary

Run python3 check_ratio_max.py and compare the result to ratio_max_results.json. The checker uses only Python's standard library, integer arithmetic, and Fraction arithmetic. It enumerates the actual supports and their connected components, computes every Walsh numerator directly, verifies the exact histograms and Parseval sums, checks boundary and Fourier energies independently, factors the entropy numerators, performs the two integer sign comparisons, encloses every displayed logarithmic comparison, and checks the explicit noncritical descendant.

The exploratory script explore_components.py was a floating diagnostic over this simple ball/cube/singleton family. It suggested this candidate only. None of its numerical output is used as a certificate. The exact checker was then written and actually executed with exit code zero; ratio_max_results.json is its observed output. A fresh author replay matched those output bytes. Independent review is tracked in the separate audit package: its author reconstructed the signed histograms and prime-log vectors, used a distinct alternating-Mercator logarithm enclosure, verified the two integer comparisons and descendant limitation, and replayed this checker byte-identically. This originating worker subsequently read that full audit report and code and replayed its independent output byte-identically. These are finite exact calculations and independent mathematical/code checking, not proof-assistant formalization. The tensor corollary is the displayed analytic factorization, not a numerical enumeration.

Sources actually read are pinned in SOURCE_PINS.json. They are exact research files and the cited scientific interfaces, not raw conversation transcripts, held evaluation banks, imported benchmark corpora, or engineering traces. The source-route navigation preface and 22-file index were checked for accurate scope; pins establish navigation/provenance rather than mathematical truth or admission. Existing source holds, scheduler assignments, movie workers, private-repository controls, and admission decisions are unchanged. No repository publication, merge, deployment, paid service, or live learned-memory-benefit claim is part of this package.
