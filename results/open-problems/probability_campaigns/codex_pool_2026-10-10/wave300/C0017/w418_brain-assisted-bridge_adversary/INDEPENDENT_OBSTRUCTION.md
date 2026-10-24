# Independent derivation saved before reading the paired proof

2026-10-10. Worker w418. This is a deterministic obstruction to a proposed inference, not a counterexample to square-bond conformal invariance or to the actual percolation observable. Referee: w419, pending.

Let delta>0. At every interior vertex v=(j delta,k delta) of a square grid, consider complex numbers attached to horizontal and vertical edge midpoints. Use the local weak contour identity

    F_E(v)-F_W(v) + i [F_N(v)-F_S(v)] = 0.           (WCR)

Define F(e)=conjugate(z_e) on horizontal edges and F(e)=z_e on vertical edges, where z_e is the midpoint in C. Then F_E-F_W=delta and F_N-F_S=i delta. Hence (WCR) holds exactly at every interior vertex, for every delta. In each orientation separately the fields are restrictions of a 1-Lipschitz smooth function, uniformly bounded on bounded domains.

Nevertheless, the two orientation limits are conjugate(z) and z. They disagree whenever Im z != 0. The natural vertex average A_delta=(F_E+F_W+F_N+F_S)/4 equals Re z exactly and is not holomorphic on any open subset of C. For example, its integral over a positively oriented axis-aligned rectangle is i times the rectangle's area, not zero.

Thus the weak edge identity and bounds/equicontinuity within each orientation do not imply holomorphicity of the averaged field or a common scalar limit. The missing premise for the standard Morera route is coherence of orientations after whatever normalization/phase convention the source specifies: sup on each compact set of |F_H-F_V| must tend to zero, or another relation that identifies the actual contour field must be proved. Equicontinuity of the combined field over ALL edge midpoints would imply such coherence and would rule out this example; the example does not refute a proof supplying that stronger estimate.

Positive conditional bridge. If the edge data approach a common continuous f locally uniformly over ALL edge midpoints and satisfy (WCR), summing (WCR) over the vertices in a rectangle cancels interior horizontal and vertical edges. Multiplication by i delta gives a midpoint approximation of integral f dz around the dual rectangle. It vanishes. Passage to the limit gives zero contour integrals on all interior axis-aligned rectangles, and the rectangle form of Morera's theorem makes f holomorphic. Quantifier: this must hold for every compact subset of the domain along the same subsequence. Boundary identification and percolation-specific coherence remain separate obligations.

Primary-source alignment: Duminil-Copin, arXiv:1208.3787, Definition 3 and Proposition 4, uses F(NW)-F(SE)=i[F(NE)-F(SW)]. Rotate the geometry by -pi/4 so NW becomes N, SE becomes S, NE becomes E, and SW becomes W. The source relation becomes F_N-F_S=i(F_E-F_W), equivalent to (WCR). The source's vertex observable uses one half of the sum instead of one quarter; our example then gives 2 Re z and remains nonholomorphic. The source's phase convention is F(e)=E[exp(i sigma W_gamma(e,e_b)) 1_{e in gamma}], sin(sigma pi/2)=sqrt(q)/2, sigma in [0,1]. Hence q=1 gives sigma=1/3.

The common-limit premise is a sufficient route, not a necessary condition for every possible observable proof. A direction-dependent phase adjustment changes the local equation; verify the transformed equation explicitly before applying the Morera lemma. Multiplication of all edge values by one common scalar preserves (WCR).

NEXT: Verify the primary source's edge equation and phase conventions; compare this missing premise with the brain-returned theorem and w417's actual bridge.
