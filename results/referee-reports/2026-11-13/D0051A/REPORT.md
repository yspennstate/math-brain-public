PARTIAL

# D0051: thickness on LQG geodesics

The spectrum and uniqueness of its maximiser are not determined here. The literature search through 13 November 2026 found no complete answer. The rigorous result below is an explicit upper-bound curve, valid for the **limsup convention actually printed in Problem 5.3**, together with a proof and its maximiser. It recovers the known general rectifiable-path dimension bound in the subcritical phase; it is not claimed as a new sharp geodesic theorem. Numerical evidence will be reported separately below.

## Statement and conventions

Let h be the whole-plane GFF with h_1(0)=0, normalized so that circle-average variance grows as log(1/r). Write

\[
 E_\alpha=\{z:\limsup_{r\downarrow0}h_r(z)/\log(1/r)=\alpha\},\qquad
 F_\alpha=\{z:\lim_{r\downarrow0}h_r(z)/\log(1/r)=\alpha\}.
\]

The source's \(T_h^\alpha\) is \(E_\alpha\). The distinction \(F_\alpha\subset E_\alpha\) is essential. Both differ from the metric-thickness sets defined by the exponent of the D_h-diameter of a Euclidean ball. No equality between these three definitions is assumed.

Let \(\xi>0\), and let \(Q=Q(\xi)>0\) be defined by the LFPP normalization \(a_\varepsilon=\varepsilon^{1-\xi Q+o(1)}\). Let P be a nonconstant, finite-length D_h-geodesic between nonsingular points. Put

\[
 A(\alpha)=2-\frac{\alpha^2}{2},\qquad b(\alpha)=\xi(Q-\alpha).
\]

Almost surely, simultaneously for such geodesics and \(\alpha\in[-2,2]\), the following upper bounds hold:

\[
 \boxed{\dim_{\rm E}(P\cap E_\alpha)\le
 U_{\rm E}(\alpha):=\min\{A(\alpha),b(\alpha)\}\quad(\alpha<Q).} \tag{1}
\]

\[
 \boxed{\dim_{D_h}(P\cap E_\alpha)\le
 U_D(\alpha):=\min\left\{1,\frac{A(\alpha)}{b(\alpha)}\right\}\quad(\alpha<Q).} \tag{2}
\]

If \(Q\in[-2,2]\), \(\dim_{\rm E}(P\cap E_Q)=0\); its D_h-dimension is at most 1. If \(\alpha>Q\), \(P\cap E_\alpha=\varnothing\). Zero Hausdorff dimension in these statements does **not** assert emptiness. We use dimension zero for the empty set as well.

These inequalities also apply to every finite D_h-rectifiable path, with its image in place of P. All claims concern finite geodesic segments; a ray is treated as a countable union of finite segments.

In the subcritical phase \(0<\xi<\xi_{\rm crit}=2/d_2\), there is \(\gamma\in(0,2)\) such that

\[
 \xi=\gamma/d_\gamma,\qquad Q=2/\gamma+\gamma/2>2,
 \qquad d_\gamma=\dim_{D_h}\mathbb C>2.
\]

At criticality \(Q=2\), \(\gamma=2\), \(\xi=2/d_2\). For \(\xi>\xi_{\rm crit}\), \(0<Q<2\); the metric has singular points at infinite distance from every other point. One must work on its nonsingular locus. There is no real \(\gamma\in(0,2]\) solving \(Q=2/\gamma+\gamma/2\) in this phase, so a subcritical d_gamma formula cannot simply be continued there. The central-charge notation is \(c_M=25-6Q^2\). These conventions are in DDG Sections 2.1–2.3, PDF pp. 5–13. In particular, Q is not an arbitrary independent parameter.

For the exact-limit sets there is a stronger **existing** relation, Pfeffer, Theorem 1.16, PDF p. 10:

\[
 \dim_{D_h}(P\cap F_\alpha)
 =\frac{\dim_{\rm E}(P\cap F_\alpha)}{\xi(Q-\alpha)},\quad\alpha<Q. \tag{3}
\]

This theorem allows sets depending on h. It converts one unknown spectrum to the other; it does not determine either spectrum. Relation (3) is not asserted for E_alpha.

## Literature and difficulty

The exact question is DDG, [arXiv:2109.01252](https://arxiv.org/abs/2109.01252), Section 5, Problem 5.3, physical PDF p. 24. The full Section 5 occupies pp. 23–24 in the saved text. It asks for both dimensions, then asks whether each spectrum has a unique maximising alpha. The Euclidean and metric maximisers need not be the same.

A geodesic parametrised by D_h-length is an isometry from a real interval: for \(s<t\), \(D_h(P(s),P(t))=t-s\), since otherwise replacing that subpath by a shorter path contradicts minimality. Thus \(\dim_{D_h}P=1\). Every nondegenerate real interval has Hausdorff dimension one: equal subdivisions prove the upper bound, and its length measure gives the lower bound because a cover by sets of diameter d_j must have \(\sum d_j\ge L\).

Fan–Goswami, [arXiv:2205.00676](https://arxiv.org/abs/2205.00676), Theorem 1.1, PDF p. 3, proves \(\dim_{\rm E}P>1\) for all xi>0. This supersedes the survey's older statement that no nontrivial lower bound was available. In the subcritical phase Gwynne–Pfeffer, [arXiv:1905.11790](https://arxiv.org/abs/1905.11790), Corollary 1.10, p. 9, gives

\[
 \dim_{\rm E}P\le B:=\xi\left(Q-\xi+\sqrt{\xi^2-2\xi Q+4}\right)<2.
\]

For \(\gamma=\sqrt{8/3}\), \(d_\gamma=4\), \(\xi=1/\sqrt6\), \(Q=5/\sqrt6\), and \(B=(4+\sqrt{15})/6\approx1.312163891\). Miller–Qian's earlier Proposition 4.8, [arXiv:1812.03913](https://arxiv.org/abs/1812.03913), PDF p. 16, gives an upper Minkowski dimension strictly below two. None of these bounds is an exact Euclidean dimension.

Gwynne–Pfeffer–Sheffield, [arXiv:2010.07889](https://arxiv.org/abs/2010.07889), Theorem 1.8 and Remark 1.12, PDF pp. 6–7, establishes deterministic dimensions for geodesics from a fixed point and analogous thick-point zero-one laws. Bhatia–Kavvadias, [arXiv:2608.22693](https://arxiv.org/abs/2608.22693), Theorem 1, pp. 2–3, strengthens uniformity to every bulk segment of every subcritical geodesic. It does not compute the constants. Section 1.3, p. 4, explicitly explains why its method does not answer the typical-thickness question of DDG Problem 5.3. Its own signed liminf definition in Section 2 also requires care before identifying it with E_alpha.

For comparison, Gwynne, [arXiv:1909.08588](https://arxiv.org/abs/1909.08588), Theorem 1.2, PDF p. 6, computes the essential-supremum ball-boundary spectrum for **metric** thick points, also intersected with F_alpha:

\[
 f_{\rm E}(\alpha)=2-\alpha^2/2-\xi(Q-\alpha),\qquad
 f_D(\alpha)=\frac{2-\alpha^2/2}{\xi(Q-\alpha)}-1,
\]

on the open interval where these expressions are positive. Its endpoints are \(\xi\pm\sqrt{4-2\xi Q+\xi^2}\). The Euclidean maximiser is xi. Differentiating the second expression gives a numerator proportional to \(\alpha^2/2-Q\alpha+2\); its zero in [-2,2] is \(Q-\sqrt{Q^2-4}=\gamma\), the metric maximiser. The total boundary dimensions are \(2-\xi Q+\xi^2/2\) and \(d_\gamma-1\). Gwynne's Theorem 1.1, p. 4, initially gives essential suprema; GPS Theorem 1.7, p. 5, supplies almost sure dimensions for the boundary of a ball stopped on hitting a fixed point. These quantifiers should not be silently replaced by a theorem for every radius and every centre.

There is a genuine convention gap in the source's informal description of the solved analogue: Gwynne explicitly states on PDF p. 6 that he does not prove the upper bound for ordinary circle-average thick points alone. GPS Remark 1.12 supplies zero-one laws, not that missing upper bound. Therefore the displayed boundary spectrum is reported with the precise sets its theorem treats, not as a proved formula for E_alpha.

The boundary proof has a one-point event with two costs. Approximate alpha-thickness costs \(r^{\alpha^2/2+o(1)}\). Hitting a prescribed distance level costs an additional \(r^{\xi(Q-\alpha)+o(1)}\). A smooth bump near the ball's centre, Weyl scaling, a bounded-density estimate for the resulting distance, and a Cameron–Martin change of measure make that second cost rigorous (Gwynne, Section 2.1, Proposition 2.2, pp. 9–10). Carefully constructed multiscale events and two-point estimates give a positive-probability Frostman measure for the lower bound (Sections 3–6); GPS confluence/locality and zero-one laws upgrade the appropriate dimensions.

A geodesic is chosen by minimising distance over paths through the same field. Its visiting probability is not the prescribed-level event above. A local change of h can change which route wins. Large positive h makes local passage expensive, so the optimiser seeks thinner regions, but that observation supplies neither the probability that a square is visited nor its two-point counterpart. These missing visitation estimates are what would be needed for matching spectrum bounds. The universal length budget used below supplies an inequality only.

In particular, the independent-set KPZ equation

\[
 \dim_{\rm E}X=\xi Q\dim_{D_h}X-\tfrac12\xi^2(\dim_{D_h}X)^2
\]

is Gwynne–Pfeffer Theorem 1.4, PDF p. 7, under an explicit independence hypothesis. Substituting a geodesic into this equation is invalid. Its universal inequalities (Theorem 1.8) are valid for dependent sets, and (3) is a different, thickness-restricted theorem that is valid for dependent sets.

The requested author searches and later work are documented with locations in [sources/LITERATURE.md](sources/LITERATURE.md). They include confluence, Brownian-map geodesics, volume bounds, environment viewed from infinite geodesics, and 2025–2026 strong-confluence/zero-one-law results. The relevant roughness authors are Fan–Goswami; Fan–Sung's 2025 paper concerns SLE welding. The volume paper is Ang–Falconet–**Sun**. No exact answer was found under those author combinations.

## Proof of the upper bounds

The proof uses established GFF continuity and LQG crossing estimates, stated with their sources below. The covering, dimension bounds, one-sided extension to limsup sets, and optimisation are proved here. We do not purport to reconstruct the LQG metric or reprove its crossing estimates from first principles.

Fix a bounded square K, enlarge it by a fixed positive margin, and write r_n=2^{-n}. A dyadic square S of side r has centre v_S. Let A_S be the square annulus between the concentric squares of side 2r and 3r. A path from S to outside the outer square must cross A_S.

**Two input estimates.** First, on one probability-one event, the change in h_r(z) when z moves by at most Cr or r changes by a bounded multiplicative factor is o(log(1/r)), uniformly on K. Here C is any fixed finite constant. To justify this precise version of circle-average continuity, on a box of side r the Gaussian increments of circle averages at comparable radii have bounded variance and bounded expected supremum, uniformly in r and the box's location. These facts follow from the logarithmic covariance and its standard local canonical-metric continuity bound; see the circle-average estimates used in GP Lemmas 2.2–2.3, pp. 11–12. One can also derive the supremum bound by the Gaussian entropy integral: after rescaling the box to unit size, the canonical metric is bounded by C_eta times a positive power of spatial/radial separation, for any fixed exponent below 1/2, so its covering numbers are polynomial and the entropy integral is finite. Borell's Gaussian supremum inequality then bounds the probability that the increment supremum exceeds epsilon log(1/r) by C exp[-c epsilon² log²(1/r)]. There are O_K(r^{-2}) boxes. The union bound over them and sum over dyadic r are finite. Borel–Cantelli, followed by countably many epsilon>0, proves the stated o(log) assertion. It also permits passage between a continuous radius and a neighbouring dyadic radius. At deterministic centres, Var(h_r(v_S))=log(1/r)+O_K(1).

Second, for every eta>0, almost surely for all sufficiently large n and every S meeting K,

\[
 D_h(\text{across }A_S)\ge r^{\xi Q+\eta}e^{\xi h_r(v_S)}, \tag{4}
\]

and there exists a connected crossing network H_S in S with

\[
 \operatorname{diam}_{D_h}H_S\le C_\eta r^{\xi Q-\eta}e^{\xi h_r(v_S)}. \tag{5}
\]

One can choose the networks so that every parent's network intersects every child's. Specifically, use the four crossings of the four half-square rectangles in Pfeffer Definition 3.5; Lemma 3.6 proves this intersection property. Estimates (4)–(5) are Pfeffer Lemma 3.7, PDF pp. 41–42, with an arbitrary small change of eta and a fixed multiplicative constant absorbed. They hold for all xi>0. They follow from Proposition 1.8 (superpolynomial normalized crossing tails), Proposition 1.9 (c_r=r^{xi Q+o(1)}), a union bound over O(r^{-2}) squares, and Borel–Cantelli. In detail, choose the normalized threshold r^{-eta/2}, use any tail power p with p eta/2>3, and sum the resulting O(r^{p eta/2-2}) error over dyadic r. Only finitely many crossing templates per square are required. No independence between P and h is used.

**First moment for approximately thick squares.** For delta>0 let N_n(alpha,delta) count squares meeting K such that

\[
 h_{r_n}(v_S)/\log(1/r_n)\in[\alpha-\delta,\alpha+\delta].
\]

A centred Gaussian tail with variance log(1/r)+O(1) gives

\[
 \mathbb E N_n(\alpha,\delta)\le
 C_K r_n^{-2+(|\alpha|-\delta)_+^2/2+o(1)}. \tag{6}
\]

Indeed, the band event implies a Gaussian tail of magnitude at least (|alpha|-delta)_+ log(1/r); the Chernoff bound exp[-t²/(2 Var)] supplies its exponent. Multiplying by O_K(r^{-2}) possible squares proves (6). In particular, for
\(s>2-(|\alpha|-\delta)_+^2/2\),
\(\sum_n\mathbb E[N_n r_n^s]<\infty\).
Tonelli implies that the corresponding sum is finite almost surely and that its tails tend to zero.

Every z in E_alpha belongs to a square in such a band at arbitrarily small dyadic scales, after slightly enlarging delta. This follows directly from the definition of limsup and the first input estimate. Thus these squares, at all n>=k, cover E_alpha for every k. Their Euclidean s-content tends to zero. Send delta down to zero and exhaust K to get

\[
 \dim_{\rm E}E_\alpha\le A(\alpha). \tag{7}
\]

This argument works for negative alpha as well: it uses a **band**, not just a positive-tail event. Using only h_r>=(alpha-delta)log(1/r) would lose the Gaussian cost when alpha<0.

**Length budget at thick squares.** Let L be the length of P. For any band square S hit by P, (4) gives

\[
 D_h(\text{across }A_S)\ge r^{b(\alpha)+\xi\delta+\eta}. \tag{8}
\]

Except for a bounded number of squares whose outer squares contain an endpoint of P, the visit forces a full crossing of A_S. Colour the square lattice with finitely many colours, for example by both coordinates modulo 5. The outer squares for one colour are disjoint. Select one crossing subpath per visited square of this colour. These subpaths have disjoint parameter intervals because they lie in disjoint outer squares. Their total length is at most L. Summing (8), then summing over the colours, bounds the number of visited band squares by

\[
 C+C L r^{-b(\alpha)-\xi\delta-\eta}. \tag{9}
\]

The endpoint exception contributes at most O(1) squares per scale and has Hausdorff dimension zero. Alternatively, restrict to the part of P at Euclidean distance >=1/j from its endpoints, and then take the union over j. Since P is simple, this covers its interior.

For s>b(alpha)+xi delta+eta the sum of the s-powers of the sizes of the squares in (9), over all sufficiently fine scales, is finite. The same limsup covering argument proves

\[
 \dim_{\rm E}(P\cap E_\alpha)\le b(\alpha)
\]

when b(alpha)>=0. Let delta,eta tend to zero. Together with (7), this proves (1) and the assertion at alpha=Q.

Equations (6) and (9) can also be read as the requested combined first-moment bound: localize to L<=M and to the event that (4) holds at all scales n>=k. For any measurable choice of P, the expected number of visited band squares, apart from endpoints, is bounded by

\[
 \min\left\{C_Kr^{-2+(|\alpha|-\delta)_+^2/2+o(1)},\ CM r^{-b(\alpha)-\xi\delta-\eta}\right\}. \tag{10}
\]

This does not multiply dependent probabilities. The second term is a deterministic length bound on the localized event. Countable exhaustion in M,k removes the localization. The field counts and pathwise bound (9) also prove simultaneity for all paths without needing to select a particular geodesic measurably.

**No thickness above Q.** If z in E_alpha has alpha>Q, choose epsilon>0 with alpha>Q+3epsilon. At arbitrarily small r, h_r(z)>=(Q+2epsilon)log(1/r). For a dyadic square containing z at a comparable scale, the first input estimate transfers this lower bound with error at most epsilon log(1/r). Equation (4), with eta<xi epsilon, forces the crossing distance to diverge along this subsequence. Any path from z to a distinct point must cross these annuli. Its length is therefore infinite. In particular z is singular and cannot belong even as an endpoint to a nonconstant finite geodesic. This also reproves the direction of Pfeffer Proposition 1.11(a) used here. At equality alpha=Q the divergent-distance argument does not apply.

**A one-sided metric comparison for limsup sets.** Fix a<Q and an integer m, and let

\[
 S_{a,m}=\{z\in K:h_r(z)\le a\log(1/r)\text{ for every }0<r\le1/m\}.
\]

The first input estimate and (5) imply that for any epsilon>0, for sufficiently small dyadic squares S meeting S_{a,m},

\[
 \operatorname{diam}_{D_h}H_S\le C r^{\xi(Q-a)-\varepsilon}. \tag{11}
\]

Choose epsilon<xi(Q-a). For each such S, form the union of H_S and the networks of all its dyadic descendants which meet S_{a,m}. A branch is connected by the parent–child intersection property. Between any two branches the D_h-distance is bounded by twice the sum of the diameters along their branches, hence by

\[
 2C\sum_{j\ge0}(2^{-j}r)^{\xi(Q-a)-\varepsilon}
 \le C' r^{\xi(Q-a)-\varepsilon}. \tag{12}
\]

For every z in S intersected with S_{a,m}, nested descendants containing z supply network points converging to z in Euclidean distance. Lower semicontinuity of D_h passes (12) to these limits. Consequently

\[
 \operatorname{diam}_{D_h}(S\cap S_{a,m})\le C' r^{\xi(Q-a)-\varepsilon}. \tag{13}
\]

This is a diameter bound for the **restricted set**, not for all of S; large metric spikes elsewhere in S do not invalidate it. For any X subset S_{a,m}, cover X by Euclidean balls, replace each with O(1) dyadic squares of comparable size, and apply (13). For any t>dim_E X/[xi(Q-a)-epsilon], the sum of the t-powers of the D_h-diameters can be made arbitrarily small. Thus

\[
 \dim_{D_h}X\le\frac{\dim_{\rm E}X}{\xi(Q-a)-\varepsilon}.
\]

Let epsilon decrease to zero. For alpha<Q and delta>0 with alpha+delta<Q, E_alpha intersected with K is contained in the union over m of S_{alpha+delta,m}. Apply this inequality to P intersected with E_alpha intersected with each S_{alpha+delta,m}, use countable stability, and send delta to zero. We obtain

\[
 \dim_{D_h}(P\cap E_\alpha)
 \le \frac{\dim_{\rm E}(P\cap E_\alpha)}{b(\alpha)}
 \le\frac{A(\alpha)}{b(\alpha)}.
\]

Together with dim_D P=1 this proves (2). It proves only this direction for limsup sets, unlike the equality for exact-limit sets in (3).

All estimates above can be intersected over rational tolerances, rational field bands and a countable exhaustion of K. Every real alpha can be enclosed by these rational bands with errors tending to zero. Thus the event used does not depend on a chosen alpha or on a chosen geodesic.

## Maximising the bound, not the spectrum

In the subcritical phase \(0<\xi Q=(2+\gamma^2/2)/d_\gamma<2\). The equality A(alpha)=b(alpha) has roots

\[
 \alpha_\pm=\xi\pm\sqrt{\xi^2+4-2\xi Q}.
\]

There is exactly one negative root, alpha_- in (-2,0). On [-2,alpha_-], U_E=A is strictly increasing. On [alpha_-,0], U_E=b is strictly decreasing; on [0,2] both candidate functions are decreasing. Therefore the **upper-bound curve** U_E has the unique maximiser

\[
 \alpha_{\rm bound}=\alpha_-,\qquad
 \max U_{\rm E}=\xi(Q-\alpha_-)=B. \tag{14}
\]

This matches GP Corollary 1.10 algebraically. It does not show that the upper bound is attained there, nor that the actual spectrum has one maximiser. The total-path bound also requires control of points without an exact thickness; it is supplied directly by GP, rather than by an illicit uncountable-union argument over alpha.

For the metric upper curve U_D, its maximum is 1 on the **whole interval** [alpha_-,alpha_+]. These roots both lie in [-2,2] in the subcritical phase: A(0)>b(0) and A(±2)<b(±2). Thus this bound cannot establish uniqueness of the metric maximiser. The curve values at the roots are bounds of one, not proofs of positive length or dimension there.

More generally the Euclidean upper curve on [-2,min(2,Q)] has the same maximiser alpha_- when xi Q<2; if xi Q>=2 it has unique maximiser zero and value two. This last observation is an algebraic property of the bound, conditional on such parameters, not a claim that LQG realizes every parameter pair.

For the Brownian-map parameter, alpha_-=(1-sqrt(15))/sqrt(6) is about -1.1729. At alpha=0, (1) gives at most xi Q=5/6, whereas the whole geodesic has Euclidean dimension >1. This is consistent with a preference for thin regions, but it neither specifies a dominant thickness nor excludes nonconvergent circle-average behaviour.

A stronger existing exclusion applies to F_alpha in the interior: Pfeffer Lemma 2.25, PDF p. 30, gives a deterministic zeta<Q such that every interior geodesic point has liminf h_r/log(1/r)<=zeta. Consequently P's interior misses F_alpha for alpha>zeta. Endpoints must be omitted: a geodesic can start at an exceptional nonsingular thick point. Since a liminf bound does not bound a limsup from above, this theorem is not used to replace Q by zeta in (1)–(2) for E_alpha.

## Numerical evidence and checks

The experiment is [code/lfpp_experiment.py](code/lfpp_experiment.py); its seed is 51053. It samples zero-exterior-Dirichlet DGFFs with covariance \(2\pi(4I-\mathrm{adjacency})^{-1}\) using an orthonormal sine transform. This factor makes the variance divergence log N, matching the continuum thickness convention. Each of N=128,256,512 has 12 independent fields. The same field is reused across xi=0, 0.2, 1/sqrt(6), 0.8, giving 144 paths. The xi=0 paths are controls. Xi=0.8 is supercritical; no unknown gamma or d_gamma is assigned to it.

Paths join (N/4,N/2) to (3N/4,N/2), constrained to the central [N/8,7N/8)^2 box inside the larger sampled field. Dijkstra uses the symmetric edge cost \((e^{\xi h(u)}+e^{\xi h(v)})/2\). This has the same minimizing path as summing vertex weights for fixed endpoints. A global mesh factor changes lengths but not paths. The constraint is an internal-domain LFPP experiment; it is a finite-grid proxy, not an asserted exact discretisation theorem for the whole-plane continuum geodesic.

At circle radii r=N/16,N/32,N/64,N/128,N/256 pixels, retaining only radii >=2 pixels, bilinear interpolation and uniform angular quadrature estimate the circle averages. At N=512 the radii are 32,16,8,4,2 pixels. The raw estimator is \(h_r/\log((N+1)/r)\). An additional estimator \((h_r-h_R)/\log(R/r)\), with R=N/8-1 pixels, subtracts a macroscopic circle average to assess finite-scale bias. These are different finite-resolution statistics with the same intended limiting thickness at a point where the limit exists.

For each path and radius, data record the mean, standard deviation, 5th/50th/95th percentiles, and a 60-bin histogram, including explicit overflow mass. Sampling is either uniform on path vertices or weighted by half the costs of incident path edges. The latter approximates LFPP length sampling; neither sampling convention is a Hausdorff-dimension measurement. Straight-segment and spatially uniform controls are also recorded. Each replicate is separately normalized, and quoted standard errors use the 12 independent fields, not the correlated vertices.

For N=512 and r=4 pixels, the replicate-average raw thickness is:

| xi | Uniform path vertices, mean ± SE | LFPP-length sampling, mean ± SE | Vertex mean minus straight control, paired ± SE |
| --- | ---: | ---: | ---: |
| 0 | 0.023 ± 0.079 | 0.023 ± 0.079 | 0.000 ± 0.000 |
| 0.2 | -0.165 ± 0.072 | -0.076 ± 0.073 | -0.187 ± 0.033 |
| 1/sqrt(6) | -0.277 ± 0.063 | -0.076 ± 0.073 | -0.300 ± 0.048 |
| 0.8 | -0.359 ± 0.053 | -0.013 ± 0.075 | -0.381 ± 0.050 |

For xi=1/sqrt(6), changing the circle scale on this grid gives:

| Radius in pixels | Vertex mean raw thickness ± SE | Vertex mean increment thickness ± SE |
| --- | ---: | ---: |
| 32 | -0.087 ± 0.090 | -0.265 ± 0.096 |
| 16 | -0.166 ± 0.073 | -0.377 ± 0.070 |
| 8 | -0.222 ± 0.067 | -0.419 ± 0.058 |
| 4 | -0.277 ± 0.063 | -0.466 ± 0.050 |
| 2 | -0.322 ± 0.056 | -0.499 ± 0.040 |

The paired comparisons show selection of lower field values under uniform vertex sampling. The difference from length-weighted sampling is substantial. Scale drift is also substantial, and the smallest radii are close to the lattice cutoff. This is evidence about this discrete experiment only; there is no fitted limiting alpha, estimated Hausdorff spectrum, or identification of a histogram mode with the maximiser of (1).

The original figures are [bounds and scale dependence](data/bounds_and_evidence.svg), [thickness histograms](data/thickness_histograms.svg), and [one field with paths](data/sample_geodesics.png). Complete records are [path_statistics.csv](data/path_statistics.csv), [histograms.csv](data/histograms.csv), [summary.csv](data/summary.csv), and [paired comparisons](data/paired_geodesic_minus_straight.csv). The 36 NPZ files store the fields in float32 and all paths; calculations use float64, and the seed/code reproduce those calculations without the storage rounding.

Validation included an independent heap-based shortest-path calculation on a small random field; exact Manhattan distance and an exact straight path at xi=0; adjacency, simplicity and reconstructed path-cost checks for every path; a 10,000-draw covariance check against the independently formed inverse lattice Laplacian (relative Frobenius error 0.04388); and circle-average quadrature on a constant field. All 5,760 statistics rows are finite; histogram masses sum to one within 1.5e-14. The negative optimiser and B were checked both algebraically and by a 200,001-point grid search: alpha_bound=-1.1728905396, grid maximiser=-1.17288, B=1.3121638910. Checks and hashes are in [data/audit.json](data/audit.json).

The final experiment took about 11.3 seconds, used one numerical worker with library thread limits set to one, inherited nice 10, and peaked at 498,499,584 bytes (0.46 GiB) RSS. Metadata and progress are in [data/metadata.json](data/metadata.json) and [data/run.log](data/run.log). An initial numerical run emitted floating-point status warnings from the platform's matrix-multiplication path despite finite results. The affected reductions were rewritten as explicit sums/einsum, and the complete experiment was rerun cleanly; only that final run is reported. Font caches for figure generation are kept inside data/.

## What remains open

No matching geodesic visitation lower bound, no positive-dimensional individual thickness level established here, no exact spectrum, and no uniqueness theorem for its maximiser. Numerical histograms do not resolve any of these. The most useful missing analytic input is quantitative one- and two-point information about simultaneous thickness and passage of a globally minimizing geodesic, beyond the universal length constraint.

Primary sources and exact locations are in sources/LITERATURE.md and the page-marked source texts. Source retrieval and experiment commands are in LOG.md. No publication or pushes were made.

Task: “Open problem D0051” — received 13 November 2026, approximately 08:07 Asia/Tbilisi.
