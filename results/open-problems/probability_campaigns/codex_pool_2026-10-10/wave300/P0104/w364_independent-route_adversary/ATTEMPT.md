# P0104: independent boundary-profile route and obstruction

Saved 2026-10-10 before reading the paired prover's ATTEMPT.md or CLAIMS.jsonl. The paired worker's STATUS.md names a spectral/resampling route; this route instead uses exact path composition and endpoint-selection costs. The recorded historical P0104 attempt only distinguishes logarithmic variance improvement from a polynomial exponent.

## Independent route

Try to control passage-time fluctuations through random boundary cost profiles, rather than replacing each spatial block by its scalar minimum. In a genuinely layered path class with disjoint slab environments and exactly one crossing of each interface, composition is min-plus: the same interface vertex must be used by both adjacent pieces. Independence holds for the environments; it does not remove this matching constraint. In undirected FPP, a geodesic can cross an interface repeatedly, so a formula using restricted half-space passages first requires a justified path restriction. Alternatively, full-metric triangle decomposition is exact but its two profiles need not use independent environments.

The immediate question is whether scalar block minima can stand in for those profiles. The following exact counterexample settles that proposed simplification negatively, even inside iid planar FPP.

## Exact four-edge obstruction

Let every nearest-neighbor edge of Z^2 have an independent weight uniform on {1,2}. Take s=(0,0), t=(1,1), u=(1,0), v=(0,1). Write A1=w(s,u), A2=w(s,v), B1=w(u,t), B2=w(v,t). All four variables are independent.

The two length-two paths give T=min(A1+B1,A2+B2)<=4. Any other simple s-t path has at least four edges and cost at least 4. Positive weights allow loops to be removed. Thus this is the exact unrestricted infinite-lattice passage time, not merely a graph approximation. The passage times to and from each intermediate vertex equal the indicated direct edge weights, since an alternative path between neighbors has at least three edges.

The scalar relaxation is L=min(A1,A2)+min(B1,B2). Its two terms are independent. Define the matching penalty G=T-L. Pointwise G>=0, but G=1 in precisely two of the sixteen equally likely configurations: (A1,A2,B1,B2)=(1,2,2,1) or (2,1,1,2). Otherwise G=0. Both blocks can attain their own minimum, yet their unique minimizing vertices can differ.

Exact laws, in units of 1/16:

| value | T counts | L counts |
| --- | ---: | ---: |
| 2 | 7 | 9 |
| 3 | 8 | 6 |
| 4 | 1 | 1 |

E[T]=21/8, Var(T)=23/64; E[L]=5/2, Var(L)=3/8. Also E[G]=1/8, Var(G)=7/64 and Cov(L,G)=-1/16. Therefore Var(T)=Var(L)+Var(G)+2Cov(L,G)=23/64. The scalar stitching error is not independent of the scalar minimum. Even its sign gives no monotonicity of variance.

This refutes scalar composition or a variance-convolution inference made from slab independence alone. It does not refute the KPZ conjecture and does not establish an asymptotic exponent from n=1.

## Hardest remaining piece

A block route must quantitatively control the random matching penalty and its covariance with accumulated costs at all scales, under the actual FPP law and directions. A path restriction must also control excursions and repeated interface crossings. For a decomposition T_n=L_n+G_n, a sufficient error-transfer estimate is ||G_n-EG_n||_2=o(n^(1/3)) together with separately established two-sided order n^(2/3) for Var(L_n); the L2 triangle inequality then transfers the exponent. Neither premise is proved here. Setting G_n=0 or declaring it independent discards the very effect the four-edge example exhibits.

For an upper-bound route alone, the corresponding L2 bound only transfers an upper bound. It cannot supply the lower bound required to identify chi=1/3. No novelty or complete-proof claim is made.

## Review boundary

Ask w365 to check the unrestricted-lattice reduction, all sixteen configurations, and the covariance value independently. The next adversarial step is to read the paired proof and determine whether any path-composition or profile-independence premise is actually present; do not attribute this failed scalar reduction to a proof that never uses it.

## Saved after the independent derivation: forcing under ties

The paired saved approach proposes to connect discrete gradients to geodesic membership under single-edge forcing. For {1,2}-valued weights the exact criterion is membership in every forced-low minimizing path. With other weights fixed, let A be the minimum cost excluding the tested edge among paths using it and B the minimum cost of paths avoiding it. Then T_e(a)=min(A+a,B), and integer costs give T_e(2)-T_e(1)=1 exactly when A+1<B. A minimizing avoiding path makes the difference zero, even if a chosen tied geodesic uses the edge.

All four square weights equal to 1 give an explicit counterexample to using a chosen geodesic: each single-edge increment is zero, while any chosen geodesic contains two edges. This event has probability 1/16 in the stated iid law. The exact reproduction passed all 64 single-edge forcing checks across the 16 configurations and found 12 chosen-geodesic membership false positives. These are 64 checks with repeated low/high forcings, not 64 independent random observations.

For general endpoints the lower weight bound and a Manhattan route of cost at most twice its length reduce all optimal paths to a deterministic finite set. The criterion applies without assuming uniqueness. This is an audit condition for the paired route, not an accusation that its proof uses an incorrect tie convention.

## Brain-connected prior-work check

The guarded recall returned fpp_width3_strip_time_constant_solved_2026_07_12. Reading that named memory identifies the owner's reported directed fixed-width time-constant calculation and a finite interface-state method. This is a distinct observable and geometry; its memory status is not a newly audited proof of unrestricted planar fluctuations. It suggests retaining profiles rather than scalar minima, but a fixed-width calculation supplies no growing-width matching-error estimate. The two other returned snippets concern lecture delivery and node deduplication; they supply no mathematical premise here.

NEXT: Independently check the saved all-forced-low-minimizers criterion and matching-error covariance, then seek a quantitative centered matching-error bound for growing interfaces. The scalar comparison's two-sided variance bound is a separate unproved premise.
