# D0051: second serious attempt, 2026-10-12

## Two approaches not tried in the first attempt

1. **Gaussian variational occupation transform.** At finite regularization, mark a geodesic by its normalized length occupation and study the Laplace transform of the field sampled from that occupation. Weyl response / Gaussian integration by parts might produce a tilted field law, hence a length-typical thickness. The obstacle is the variation of the optimizing path; the brain recalls a response-defect measure precisely encoding near ties. A first derivative envelope identity alone cannot determine the mark law. This differs from applying independent KPZ but risks recreating the unresolved neighboring metric-exponent problem.

2. **Frostman disintegration and thickness bands.** Choose Frostman measures on the geodesic, push them forward by the source-limsup thickness beta, and localize dimension to shrinking thickness intervals. This may prove an attained local spectrum even without a fixed-level lower bound. Then use the previous annulus and ambient-tail bounds to constrain any such maximizing thickness. Check whether an atom / dimension-conservation theorem can upgrade a shrinking-band maximizer to the original fixed-alpha problem.

Pursue approach 2: it offers a concrete lower-bound target using already verified inputs and cleanly exposes whether disintegration can close the uncountable-union gap. No claim about the original optimizer is made at this checkpoint.

## Brain consultation

math_recall.py queried with the occupation gap and Gaussian integration-by-parts / Weyl / Frostman keywords. Returned the standard Gaussian integration-by-parts card and an explicitly unresolved LFPP response-defect measure card. These are hints only. A second query asks specifically for Frostman / disintegration / dimension conservation. Recall outputs will be saved locally. The occupation response approach is retained as an alternative, not treated as solving the gap.

## H. A rigorous band-spectrum lower-bound reduction

Fix subcritical gamma and work on the probability-one event used in the first attempt. For a nonconstant finite geodesic P set Delta_E=dim_E P and Delta_D=1. The source-limsup thickness beta is in [-2,2] at every point, almost surely: the HMP circle-average limsup-at-least sets are empty above 2, for h and -h; intersect over rational thresholds above 2 and local domains. This also bounds liminf below -2. Thus beta is finite everywhere. It is Borel: for fixed positive lower radius, circle averages are jointly continuous; suprema over rational radii equal suprema over all radii, and the limsup is a countable infimum of these suprema. All band preimages are Borel.

For m equal to E or D define

    F_m(a)=inf_{delta>0} dim_m(P intersect {|beta-a|<delta}), a in [-2,2].

The infimum is the decreasing-neighborhood limit. This is a REGULARIZED spectrum, not the fixed-level spectrum in the problem.

**Theorem H1.** F_m is upper semicontinuous, max_a F_m(a)=Delta_m, and K_m={a:F_m(a)=Delta_m} is nonempty compact. Moreover

    dim_m(P intersect {|beta-a|<delta})=Delta_m

for every a in K_m and every delta>0. This supplies an attained shrinking-band maximizing thickness in each metric.

Proof of existence without any conditional GFF law. Start with J_0=[-2,2], whose preimage is all of P and has dimension Delta_m. Bisect J_0 into two closed intervals. Their preimages cover P, so at least one has dimension Delta_m: dimension of a union of two sets is their maximum, by Hausdorff-measure subadditivity and monotonicity. Choose such a child and repeat. We obtain nested closed intervals J_n of length 4*2^(-n), each with preimage dimension Delta_m. Their common intersection is one real number a*: the left endpoints increase, the right endpoints decrease, their difference tends to zero, and completeness gives their shared limit. For every delta>0, J_n is contained in (a*-delta,a*+delta) for sufficiently large n. Its preimage is a subset of the band preimage, so the latter has dimension Delta_m. This proves F_m(a*)=Delta_m. Conversely every band is a subset of P, hence F_m<=Delta_m.

To prove upper semicontinuity, suppose F_m(a)<u. Choose delta with the corresponding band dimension <u. If |b-a|<delta/2, the delta/2 band around b is contained in the delta band around a. Thus F_m(b)<u. The strict sublevel set {F_m<u} is relatively open. Consequently K_m={F_m>=Delta_m} is relatively closed in the compact interval, and is nonempty by the construction. For a in K_m, every band dimension is at least its infimum Delta_m and at most Delta_m, hence equals Delta_m. This proof works for both metrics separately; it does not assert the same a works for both.

**Theorem H2.** The regularized spectra satisfy

    F_E(a) <= min(Delta_E, 2-a^2/2, xi(Q-a)),
    F_D(a) <= min(1, F_E(a)/c), c=xi(Q-2)>0.

Proof. The first bound Delta_E is monotonicity. For sufficiently small delta and a nonzero, every point in the band has positive-sign thickness at least a-delta if a>0, or reflected limsup thickness at least |a|-delta if a<0 (the original negative-limsup identity gives a reflected liminf, which implies that limsup bound). The HMP upper-tail theorem then bounds the Euclidean band dimension by 2-(|a|-delta)^2/2. Let delta decrease to zero. At a=0 the ambient bound two suffices. Every band is a subset of S_{a-delta}; Theorem A bounds its Euclidean dimension by xi(Q-a+delta). Again take the limit. The Holder dimension-transfer proof B3 applies to each band, so its metric dimension is at most its Euclidean dimension divided by c. Taking both monotone limits proves the metric bound. These are simultaneous statements in a, using the earlier countable rational-threshold event.

**Corollary H3.** With Delta=Delta_E, every a in K_E obeys

    -sqrt(4-2Delta) <= a <= sqrt(4-2Delta),
    a <= Q-Delta/xi.

Indeed H2 gives a^2<=4-2Delta and xi(Q-a)>=Delta. Delta<=2 and xi>0 justify the square root and division. At gamma=sqrt(8/3), Delta>=1, so

    K_E subset [-sqrt(2), -1/sqrt(6)].

This is stronger than the previous collective beta<0 conclusion: there exists a fixed negative a in this compact range for which EVERY open thickness band has the full Euclidean geodesic dimension. It is still not a fixed-level lower bound. Also K_D lies strictly inside [-2,2], since H2 yields |a|<=sqrt(4-2c) for any a in K_D. The latter formula is meaningful because K_D is nonempty and hence c<=2; alternatively the usual subcritical parameter bounds already give c<2.

The endpoints F_E(+-2)=F_D(+-2)=0 follow immediately from H2, so both regularized maximizing sets avoid the endpoint thicknesses.

## I. Hostile test of the exact-level upgrade: explicit counterexample

This is a counterexample to a proposed deterministic implication, NOT to D0051 and NOT a GFF model.

For each integer n>=1 put q_n=n/(n+1), r_n=2^(-1/q_n), and let C_n be the two-map Cantor set generated by x->r_n*x and x->1-r_n+r_n*x. Since 0<r_n<1/2, its two first-generation intervals are disjoint. Define

    E_n=2^(-n)+2^(-n-2)*C_n,
    E={0} union union_{n>=1} E_n.

E is compact: E_n is compact, E_n lies in [2^(-n), (5/4)*2^(-n)], these intervals are pairwise disjoint, and any sequence visiting unbounded n tends to 0. A sequence visiting bounded n has a subsequence in one of finitely many compact components. This establishes sequential compactness in R.

We verify dim_H C_n=q_n in full rather than assuming it. Write r=r_n, q=q_n. At depth k, 2^k closed intervals of length r^k cover C_n. For s>q their s-cost is (2*r^s)^k, which tends to zero because 2*r^q=1. Thus dim<=q. Give each cylinder probability 2^(-k), the pushforward of fair independent binary digits under the coding map; denote the probability by nu. The depth-k intervals are separated by gaps at least g*r^(k-1), g=1-2r>0. If an interval J has length rho with r^k<=rho<r^(k-1), it can meet at most a constant M_r independent of k such cylinders: their left endpoints are separated by at least g*r^(k-1), and any intersecting cylinder has its left endpoint in an interval of length at most rho+r^k<(1+r)*r^(k-1). For example M_r=3+ceil((1+r)/g) suffices. Hence nu(J)<=M_r*2^(-k)=M_r*(r^k)^q<=M_r*rho^q. Covering C_n by arbitrary sets and replacing each by an interval of the same diameter gives total q-cost at least 1/M_r. Singletons have nu mass zero, since their enclosing cylinder masses tend to zero. Thus H^q(C_n)>0 and dim>=q. The constants may depend on n; no uniformity in n is claimed or needed.

Scaling and translating preserve dimension, so dim E_n=q_n. Countable stability gives dim E=sup_n q_n=1. Define the continuous injective label b:E->R by b(z)=z. Every exact b-level has at most one point and therefore dimension zero. Nevertheless its band spectrum has a UNIQUE maximizer at 0 with value one: every neighbourhood of 0 contains all sufficiently large E_n, whose dimensions approach one. For any a>0 choose delta<a/2; the corresponding band can intersect only finitely many E_n, so its dimension is at most a finite maximum of q_n, strictly below one. For a<0 a sufficiently small band misses E entirely. Thus the unique full-dimensional shrinking-band label has an exact fiber of dimension zero.

Even continuity, injectivity, compactness, a unique band maximizer, and a full-dimensional Frostman family do not justify the desired upgrade. Affinely relabeling b(z) as -1+z/10 gives a unique band maximizer -1 instead, and puts every label in [-1,-15/16], a negative range compatible with the Brownian upper envelopes for dimension-one sets. This still is not a geodesic or a GFF counterexample.

The missing step is dimension continuity under decreasing thickness-band intersections. Hausdorff dimension has no such continuity property; the construction demonstrates the failure exactly. The LQG model may supply extra structure, but we have not proved it.

## J. What Frostman disintegration actually proves

Let s<Delta_E be positive. By Frostman's finite-energy criterion on the compact geodesic P (already verified in GPS Lemma 1.6, PDF p.5), there is a probability nu_s on P with finite s-energy I_s(nu_s)=integral integral |z-w|^(-s) dnu_s(z)dnu_s(w). Let rho_s=beta_*nu_s.

**Atom criterion.** If rho_s({a})>0, then dim_E(P intersect T_h^a)>=s.

Proof. Restrict nu_s to the Borel fiber beta^(-1)({a}) and normalize by its positive mass. The resulting probability sigma has finite s-energy, since restriction can only decrease the double energy integral before normalization. By Fubini its potential U(x)=integral |x-y|^(-s) dsigma(y) is finite for sigma-almost every x. For some M<infinity, A_M={x:U(x)<=M} has positive sigma mass. For any cover set V meeting A_M choose x in V intersect A_M. All y in V have |x-y|<=diam V, so sigma(V)<=M*(diam V)^s. Therefore sigma|A_M(V)<=M*(diam V)^s. For any countable cover of A_M, summing gives sum (diam V)^s >=sigma(A_M)/M>0. It follows that H^s(A_M)>0, hence the fiber has dimension at least s. This proof avoids assigning positive mass to fibers by disintegration alone.

Consequences: a common atom at the SAME a for Frostman measures at exponents s increasing to Delta_E would prove an exact level of dimension Delta_E. Atoms at varying a would only show that the supremum of the fixed-level spectrum is Delta_E, not that it is attained. No such atoms have been established. In the Cantor construction beta is injective, and all finite positive-energy measures are nonatomic; their label laws are nonatomic too. Their conditional measures on exact labels are Dirac masses, explicitly exhibiting why disintegration does not preserve the ambient energy lower bound.

For the metric problem, take nu_D to be normalized D_h-arclength on P. If beta_*nu_D has an atom at a, then that fiber has positive interval Lebesgue measure under the isometric arclength parameterization, and consequently D_h-Hausdorff dimension one: every interval cover of the positive-Lebesgue-measure parameter fiber has sum of diameters at least its measure, so its Hausdorff 1-measure is positive; its dimension is at most one because it is a subset of [0,L]. The geodesic isometry transfers both bounds. This is a sufficient condition for a full-dimensional metric level. It is NOT necessary: a Lebesgue-null subset of an interval can have Hausdorff dimension one. Likewise, multiple atoms would allow multiple full-dimensional metric levels, so an atom by itself proves no uniqueness.

Remaining concrete occupation input: prove existence of an atom in the length-occupation thickness law, or a common atom in near-optimal Euclidean Frostman thickness laws, or an LQG-specific substitute that preserves dimension through shrinking bands. Neither zero-one laws nor the annulus lower bound supply this input. The alternative variational response approach would have to determine this label law, including the near-tie/optimizer variation; a one-point expectation or first derivative is insufficient.

## K. A second obstruction inside the same construction

Use the same compact E, but label every point of E_n by 1/n and label 0 by 0. This label map is continuous on E: each E_n is separated from the other components, and labels tend to zero along components accumulating at 0. Its range is countable. The exact levels have dimensions q_n=n/(n+1), or zero at label 0 (or empty). The exact-level supremum is one but is NOT attained. The shrinking-band maximizer is again uniquely 0: its neighbourhoods contain a tail of components with dimensions approaching one; a neighbourhood of any nonzero label intersects only finitely many components and has dimension below one.

Thus even countable-range labeling does not prove existence of an exact maximizer. In this variant any pushforward probability is purely atomic, yet its atoms can sit at levels of increasing, nonattained dimensions. This is why the common-atom qualification in the Euclidean Frostman criterion is essential. This remains an abstract counterexample rather than a construction for the LQG field.

## L. Hostile referee audit and formalization scope

1. Do not substitute band spectra for the source spectrum. Theorem H1 concerns F_m, explicitly a different object; constructions I and K demonstrate why this distinction is decisive.
2. The nested-band proof chooses FULL-dimensional children by a finite union only. It never applies dimension continuity to their intersection; it uses only eventual containment in each open neighbourhood.
3. Measurability of beta follows from circle-average continuity at positive radii and countable rational suprema; normalization logs are restricted to sufficiently small radii. Boundedness is supplied by the actual HMP high-thickness emptiness result for both field signs, not assumed from a typical-point statement.
4. Upper semicontinuity uses open bands and the triangle inequality for their labels. It does not assert continuity of beta itself for the GFF.
5. For negative bands the reflected limsup is at least the reflected liminf, which is why the HMP upper tail applies despite the source convention. Both band limits are monotone infima, so the Holder inequality passes to the limit in the correct direction.
6. The maximizing-set bounds require Delta_E>=1 only at the Brownian specialization and positive xi. They do not require knowledge of the exact Euclidean geodesic dimension.
7. Finite-energy restriction is valid only on a POSITIVE-mass exact fiber. Zero-mass disintegration conditionals need not inherit finite energy; the injective Cantor example has Dirac conditionals.
8. Cantor cylinder mass estimates have constants depending on n; no uniform bound as n increases is used. The countable union dimension computation is exact and separate from finite numerical checks.
9. The conditional occupation atom result proves metric dimension one, but establishes neither uniqueness nor atom existence. A nonatomic occupation law also would not imply all its exact fibers have dimension below one.
10. BandReduction.lean checks only finite maximum-child selection and the Brownian feasibility inequalities. The GFF facts, band compactness proof, Frostman theorem, Cantor dimensions, and occupation claims are written proofs with stated published inputs, not formalized in Lean.

Finite check script check_band_counterexample.py verified 10,180 adjacent Cantor-cylinder gaps at five parameter values and depths 1–10, the exact separation of 99 component intervals, and the finite scaling identities. These checks exercise explicit construction formulas; they do not simulate a GFF, estimate a spectrum, or replace the proof. No job exceeded 1 GB memory or needed a long numerical run.

## M. Remaining gap after the second attempt

The new result guarantees attained regularized band maximizers and bounds their location, with rigorous sufficient exact-level atom criteria. It does not prove ANY new non-endpoint exact-level dimension value or fixed-alpha lower bound for LQG. The gap is now sharply isolated: an LQG-specific dimension-preservation or common-atom property when shrinking thickness bands are collapsed to a fiber. General Frostman disintegration, compactness, continuity of a label, uniqueness of the band maximizer, and even atomic pushforward laws do not supply that property. Explicit constructions disprove the corresponding deterministic shortcuts. The Gaussian-response alternative would require quantitative optimizer/near-tie control to determine occupation thickness, which the brain itself records as unresolved. No proof of uniqueness, counterexample for the actual LQG model, or critical/supercritical completion has been found.

## Final second-attempt verdict

VERDICT: PARTIAL. H1-H3 and the sufficient atom criteria are proved; I and K are explicit counterexamples to deterministic shortcut implications, not to D0051. BandReduction.lean passed with exit code 0 in 152.57 seconds, with the standard axioms propext, Classical.choice, and Quot.sound and no sorry/native_decide. Only its three stated finite/algebraic lemmas are formalized. The exact source spectra and unique maximizing thickness remain unsolved.
