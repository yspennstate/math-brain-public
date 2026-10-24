P0321: Delaunay bond localization and a necessary dependence bound

Status: G1-G6 independently kept by w551 and w550 as a conditional bridge; final admission pending. This is a general point-process implication, not a proof of a Riesz hexatic phase. No novelty claim.

Definitions and assumptions

Let Phi be a stationary, almost surely nonempty, simple locally finite point process in R^2. Assume every Voronoi cell is bounded, no four points are cocircular, no three points collinear, and a fixed deterministic observation point almost surely has a unique nearest nucleus. These deliberately strong geometric hypotheses avoid degeneracies; the theorem does not assert them for a Riesz Gibbs state. For each observation point x let p_x be its nearest nucleus. Join nuclei if their Voronoi cells share an edge. Let N(p_x) be the finite nonempty set of these Delaunay neighbors and define

F_6(x) = |N(p_x)|^(-1) sum_{q in N(p_x)} ((q-p_x)/|q-p_x|)^6,

identifying R^2 with C. Thus |F_6| <= 1. Let C_6(x,y) = E[F_6(x) conjugate(F_6(y))] - E[F_6(x)] E[conjugate(F_6(y))]. This is a spatial nearest-cell mark; it is not a Palm mark at two conditioned particles.

Write V(t) = P(Phi intersect B(0,t) is empty), and let alpha(A,B) = sup |P(E intersect H)-P(E)P(H)| over events measurable from restrictions of Phi to A and B respectively. We use open disks; point-on-boundary null events may instead be handled with consistent closed disks. For stationary processes deterministic circle boundaries have zero expected counts when intensity is finite. Add finite positive intensity to the assumptions.

Lemma G1 (deterministic shield).

For r>0, assume the seven disks B(x,r/8) and B(x+(r/2)u_j,r/32), j=0,...,5, with u_j=exp(ij*pi/3), each contain a point. Then the Voronoi cell of p_x is inside B(x,r), and both that cell and all of its Delaunay neighbors are determined by Phi restricted to B(x,3r).

Proof. Translate x to 0. The central disk gives |p_x|<r/8. Given z with |z|=t>=r, choose j with angle(z,u_j)<=pi/6 and a shield point q in its disk. Since cos(pi/6)>=3/4,

z dot (q-p_x) >= t(3r/8-r/32-r/8) = 7tr/32.

Also |q|<17r/32. Hence

|z-p_x|^2-|z-q|^2 = 2 z dot(q-p_x)+|p_x|^2-|q|^2
 >= (7/16)tr - (289/1024)r^2
 >= (159/1024)r^2 > 0.

Thus no such z belongs to the cell, even when the cell is computed using only the seven witness points and p_x. For z inside B(0,r), any point outside B(0,3r) is at distance >=2r from z, whereas |z-p_x|<9r/8. Outside points cannot cut this already shielded cell. Its local and global versions coincide. A neighbor q has a shared-edge point z with |z|<r and |q-z|=|p_x-z|<9r/8, hence |q|<17r/8<3r. General position identifies the same edge-neighbor set in both diagrams. This proves the complete mark, including its random degree, is local on the shield event.

Lemma G2 (local approximants).

There is an F_6^(r)(x) measurable from Phi restricted to B(x,3r), bounded by one, such that E|F_6(x)-F_6^(r)(x)| <= 7V(r/32).

Proof. Use the local-diagram mark on the shield event, and zero otherwise. G1 proves equality on that event. Its complement is a union of seven empty-disk events. Stationarity gives six probabilities V(r/32), and the central probability V(r/8)<=V(r/32). The union bound gives a failure probability <=7V(r/32). Because the approximant is zero off the shield, the pointwise error there is at most one. No independence of disk events is used.

Theorem G3 (quantitative covariance bridge).

For any deterministic x,y and r>0,

|C_6(x,y)| <= 16 alpha(B(x,3r),B(y,3r)) + 28 V(r/32).

Proof. For real random variables f,g with values in [-1,1] measurable in the two regions, the indicator layer-cake formula over [-1,1]^2 gives |Cov(f,g)|<=4alpha. For complex variables of modulus <=1, expand the real and imaginary parts into four such covariances; the triangle inequality gives <=16alpha. Apply this to the two local approximants. Replacing the two factors in their joint expectation costs at most two expected approximation errors. Replacing the two factors in the product of means costs at most two more. G2 therefore bounds the total replacement error by 28V(r/32). All expectations are of bounded variables, so no integrability beyond the stated assumptions is needed.

Corollary G4 (exponential or stretched exponential process mixing excludes algebraic bond order).

Let D=|x-y| and r=D/12. If alpha(B(x,D/4),B(y,D/4)) <= A_m exp(-b(D/2)^mu) and V(t)<=A_v exp(-a t^nu) for sufficiently large D,t with a,b,mu,nu>0, then

|C_6(x,y)| <= 16A_m exp(-b(D/2)^mu)+28A_v exp(-a(D/384)^nu).

In particular no eventual lower bound c D^(-eta), c,eta>0, is possible. This requires mixing for windows whose radii grow with separation; mixing for each fixed window without uniform size control is insufficient.

Corollary G5 (polynomial mixing preserves the exponent up to logarithms).

Suppose uniformly in x,y and r>=r_0 with D>6r,

alpha(B(x,3r),B(y,3r)) <= A_m(1+r)^kappa (1+D-6r)^(-p),
V(t) <= A_v exp(-a t^nu) for t>=t_0,

where p,nu,a>0 and kappa>=0. Choose r_D=32[((p+1)/a) log(2+D)]^(1/nu); for sufficiently large D this satisfies r_D>=r_0, r_D/32>=t_0, and 6r_D<=D/2. G3 then gives

|C_6(x,y)| <= 16A_m(1+r_D)^kappa (1+D/2)^(-p) + 28A_v(2+D)^(-(p+1))
 = O(D^(-p) (log D)^(kappa/nu)).

Consequently an eventual algebraic lower bound cD^(-eta) requires p<=eta if this uniform mixing hypothesis is to hold. For p>eta the ratio of the upper bound to the lower bound tends to zero. This explicitly identifies the hypothesis that a successful hexatic construction must violate, while allowing summable density pair correlations.

Corollary G6 (necessary block dependence).

If |C_6(x,y)| >= cD^(-eta) and 28V(D/384)<= (c/2)D^(-eta), then alpha(B(x,D/4),B(y,D/4)) >= (c/32)D^(-eta), by rearranging G3 with r=D/12.

If Phi is also rotation invariant, stationarity and F_6(R_phi Phi;0)=exp(6i phi)F_6(Phi;0) imply E F_6=0, so the covariance is the two-point orientational moment. This does not make the two-point moment vanish.

What this closes and what it does not

The shield closes the measurability gap in applying local mixing to Delaunay bond marks; a Delaunay neighbor is not automatically determined by a fixed-radius window. G3 supplies an exact error term, and G5 specifies how window-size dependence affects the correlation exponent. A bound only for the truncated particle-density two-point function supplies neither alpha nor the needed uniform growing-window control.

Single hardest remaining gap: establish a nonzero algebraic lower bound for the actual microscopic Delaunay six-fold observable in an infinite-volume Riesz Gibbs state, simultaneously with rapid positional decorrelation, without assuming the orientational conclusion. No result here provides that lower bound. Further Palm/spatial observable equivalence, void bounds for the chosen Riesz state, and defect/limit control are also unproved. Successful arithmetic checks and source checks cannot close this gap.

NEXT: Referee checks G1's outside-point exclusion and G3's complex covariance constant; attack a microscopic orientational lower bound only after choosing its exact Gibbs specification.
