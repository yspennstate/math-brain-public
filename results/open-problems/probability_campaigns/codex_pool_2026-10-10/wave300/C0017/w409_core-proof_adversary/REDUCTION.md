# Deterministic contour reduction (independent derivation)

Saved before reading the paired prover's proof. This is a conditional analytic reduction, not a proof of C0017. Independent mathematical review by w410 is pending.

Let Omega be an open subset of C and delta_n tend to zero. Let f_n be complex functions on Omega intersected with delta_n Z^2. Suppose there is a continuous f on Omega such that, for every compact K contained in Omega,

sup{|f_n(v)-f(v)|: v in K intersected with delta_n Z^2} tends to zero.

For an oriented nearest-neighbor grid edge [u,v], set I_n([u,v])=(f_n(u)+f_n(v))(v-u)/2. Reversing the edge reverses I_n. For each mesh cell c whose closure is in Omega, let D_n(c) be the sum of I_n over its counterclockwise boundary.

Fix any axis-aligned rectangle R with closure in Omega. Take grid rectangles R_n with sides converging to those of R; for sufficiently large n their closures are in one fixed compact subset of Omega. Assume

sum{D_n(c): c is a mesh cell of R_n} tends to zero.

If this holds for every such R, then f is holomorphic on Omega.

Proof. Interior edges of the cells cancel exactly, so the sum is the trapezoidal boundary integral of f_n on R_n. Replacing f_n by sampled f changes this integral by at most perimeter(R_n) times the compact uniform error. This tends to zero. The trapezoidal integrals for continuous f converge to its integral on the boundary of R: uniform continuity handles quadrature and movement of the four sides, and the perimeters stay bounded. Therefore the integral of f around every interior axis-aligned rectangle is zero.

For completeness, rectangular contour vanishing implies holomorphicity without assuming any derivatives of f. Inside any smaller open rectangle, define a primitive G by integrating f from a fixed point along horizontal then vertical segments. Vanishing rectangle integrals make this equal to the integral along vertical then horizontal segments. Consequently the partial derivatives exist and are G_x=f and G_y=i f; they are continuous because f is continuous. The real differentiability of G and these relations imply that G is complex differentiable with G'=f. A complex derivative of a holomorphic function is holomorphic. This is a local statement, so it holds throughout Omega.

For a rectangle with O(delta_n^-2) cells, either sum |D_n(c)|=o(1) or max |D_n(c)|=o(delta_n^2) is sufficient. Neither is necessary: signed cancellation alone suffices. A bound O(delta_n^2) per cell is insufficient, as shown by f_n(v)=conjugate(v), for which every D_n(c)=2i delta_n^2 and the outer unit-square contour integral is 2i.

## The missing probabilistic input

To use this reduction for square-bond percolation, one must construct the actual event observable with the required boundary interpretation, establish its precompactness and boundary limits, and derive the signed summed-defect estimate for that same observable. The hard input in this analytic lane is the latter estimate; the reduction does not prove it or imply that it follows from RSW.

The primary model-specific distinction is visible in Beffara, arXiv:0708.3908v1, equations (3.2)-(3.4), PDF pp. 18-19: the relevant discrete contour is rewritten as a sum of geometric coefficients times event-change probabilities plus a vanishing remainder. Exact geometric cancellation works for the standard triangular embedding. The notes leave their extension to other geometries as a route requiring new input. The square-bond section uses a different mixed site model, so the triangular formula cannot simply be declared valid for a square-bond observable. Source: https://arxiv.org/pdf/0708.3908.

NEXT: Test the paired martingale proof's measure-level identification premise, keeping the summed-defect lemma as a separate, unresolved analytic route.
