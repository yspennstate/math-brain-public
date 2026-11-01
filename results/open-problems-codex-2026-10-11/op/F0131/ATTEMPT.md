# F0131: negative answer (2026-10-11)

**Verdict: SOLVED by counterexample to the proposed universal regular-polygon shape.** The case H=0 cannot have a regular dodecagon limit; the same proof excludes the proposed regular (4H+12)-gon for every integer H>=-1. H=-2 retains the known square. This is a deduction here, not a theorem located in print. The complete proof is in the section "Counterexample" below. Neither the actual shape nor the suggested extra dihedral symmetry is identified.

## Statement and conventions

For integer H >= -2 put eta_0(x)=-H+n*1_{x=0} on Z^2. A legal firing at a site of height at least 4 subtracts four there and adds one at each nearest neighbour. Write u_{n,H}(x) for the number of firings, eta=eta_0+Delta u for the stable height, and S_{n,H}={u>0}. The target is a regular (4H+12)-gon as n tends to infinity, including existence of an appropriately rescaled limiting fired set. The source is Holroyd et al., Question 6.2, PDF page 29. Its discussion of H approaching infinity is a different limit from n approaching infinity at fixed H.

## Proved finite facts

All facts below apply to a finite legal stabilization, whose existence for these backgrounds is part of the source setting.

**Least action and uniqueness.** Suppose v:Z^2 -> nonnegative integers has finite support and eta_0+Delta v <=3 pointwise; its proposed heights need not be bounded below. In any legal firing sequence let w be the current firing counts. If a firing would first make w exceed v, it occurs at z with w(z)=v(z), while w(y)<=v(y) at every neighbour. Thus the current height at z is eta_0(z)-4v(z)+sum_{y~z}w(y) <= eta_0(z)+Delta v(z)<=3, contradicting legality. Hence w<=v throughout. Apply this with v the firing counts of another legal stabilization to obtain inequalities in both directions and uniqueness. In particular u is the pointwise least nonnegative integer finite-support stabilizing function.

**Symmetry.** Every signed permutation g of the two coordinates preserves neighbour relations and eta_0. Transporting a legal stabilization by g gives another legal stabilization. Uniqueness gives u(gx)=u(x), eta(gx)=eta(x), and gS=S. This proves D_4 symmetry, using D_m for the group with m rotations and m reflections. Any Hausdorff limit of scalar-rescaled sets inherits this symmetry: for compact sets K_j converging to K and an isometry g, d_H(gK_j,gK)=d_H(K_j,K), so gK=K. This does not supply the additional rotations in D_{4H+12}.

**Monotonicity.** Increasing n, or decreasing H, increases eta_0 pointwise. The odometer v for the larger configuration is also stabilizing for the smaller one since adding Delta v preserves the pointwise comparison. Least action therefore gives u_small<=u_large and inclusion of their fired sets.

**Connectivity.** If z!=0 fires for the first time, its initial height -H<=2 is insufficient for firing. It must have received a chip from a previously fired neighbour. Induction on first firing time supplies a nearest-neighbour path of fired sites from z to 0. The origin must be the first site to fire. Thus every nonempty S is connected.

**Conservation and lower height bound.** Firing preserves the sum of height changes from the background. Since u has finite support, sum_x Delta u(x)=0, by exchanging the finite neighbour sums. Consequently sum_x(eta(x)+H)=n. A site that fires finishes each legal firing at height >=0 and only gains chips between firings. Sites that never fire have height >=-H. Hence eta>=min(-H,0), while stability gives eta<=3. Conservation does NOT imply a bound n >= (H+constant)|S| for all H, since eta+H may be negative when H<0.

## Computation

sandpile_experiment.py uses an integer FIFO queue and batches floor(height/4) consecutive legal firings. Such a batch is legal: before its j-th firing, height is at least 4 for every j<=floor(height/4). A flag prevents duplicate queue entries. A job raises an error if any border site would fire. Checks compare eta to eta_0+Delta u exactly, verify stability, mass conservation, zero boundary odometer and all square symmetries. Arrays use int64; the tested sizes cannot overflow. These are computations, not asymptotic theorems. Saved arrays and JSON logs are in experiments/.

## Literature implications and remaining gaps

Theorem 6.1 of the source (Fey-den Boer--Redig) proves that S_{n,-2} is a lattice square at every nonempty stage. After normalization by its coordinate radius, its union of unit cells tends in Hausdorff distance to [-1,1]^2: each cell edge differs from the normalized coordinate extent by 1/(2r), and the grid spacing is 1/r. Here r tends to infinity: if the monotone square radii were bounded, all mass changes would be confined to a fixed finite set S plus its neighbours, with uniformly bounded heights, contradicting sum(eta+H)=n. This is the square special case, not a solution for H>-2. No assertion about the limiting constant r/sqrt(n) is made here.

Theorem 9.2 of Bou-Rabee's Convergence of the random Abelian sandpile (arXiv:1909.07849), PDF page 28, gives local uniform odometer convergence away from the source for stationary ergodic bounded backgrounds <=2d-2. A constant background is such a law. This is a scaling-limit lead and does not state regular polygonality. Uniform convergence of odometers alone also needs a positivity/nondegeneracy argument to give convergence of their supports.

The earlier intake's proposed irrational-normal obstruction is not established: rational peak matrices can dominate matrices with irrational entries, and a cone boundary contains irrational matrices. An explicit refutation of the rank-one premise is being checked and will be recorded below.

This was the gap at the first partial checkpoint. The counterexample argument below now closes the regular-polygon question; it does not identify the actual domain or settle its higher dihedral symmetry.

## Counterexample: the proposed regular polygon is impossible for H>=-1

The argument below disproves the proposed shape already at H=0. Its analytic inputs are the established local uniform odometer convergence of Pegden--Smart and elementary local Poisson regularity. It does not infer polygonality from a plot or rationality of a Hessian.

### Lemma 1: coordinate monotonicity

For any integer k>=1 reflect the lattice by rho(x_1,x_2)=(k-x_1,x_2). Define v=u on x_1<=k/2 and v=min(u,u o rho) on x_1>k/2. It is nonnegative, integer-valued and finitely supported. We show eta_0+Delta v<=3.

At a retained site, v=u there and all neighbour values were decreased or retained, so Delta v<=Delta u. At a far-side site where v=u the same argument applies. At a far-side site where v=u o rho, every far-side neighbour has v<=u o rho. A neighbour on the reflection plane (when k is even) has equal original and reflected values. The only other possibility is a crossing edge when k is odd; then rho interchanges its endpoints x,y, and the choice v(x)=u(rho x)=u(y)<=u(x) implies v(y)=u(y)<=u(rho y)=u(x). Thus again Delta v(x)<=Delta(u o rho)(x). The original source is on the retained side, so eta_0(x)=-H at such a far-side site; the reflected odometer satisfies -H+Delta(u o rho)<=3 everywhere, including the reflected source, where its Laplacian is decreased by n. This proves stability of v. Least action gives u<=v; since v<=u we get equality and u(x)<=u(rho x) on the far side.

Taking k=2x_1-1 proves u(x_1,x_2)<=u(x_1-1,x_2) for every x_1>=1. Coordinate interchange proves the other direction. Together with sign symmetry, S is an order ideal in absolute coordinates: if x is fired and |y_i|<=|x_i| for i=1,2, then y is fired.

### Lemma 2: Hausdorff convergence to a solid convex set gives interior filling

Suppose epsilon_j S_j converges in Hausdorff distance to a compact convex set K with nonempty interior, and each S_j is the order ideal from Lemma 1. Then every compact subset of int K consists entirely of fired lattice sites for sufficiently large j.

Proof. Fix x in int K. Choose signs sigma_i with sigma_i x_i=|x_i| (either sign when x_i=0). For some delta>0, p=x+delta(sigma_1,sigma_2) belongs to int K. Hausdorff convergence supplies p_j in epsilon_j S_j with p_j->p. For large j, |(p_j)_i|>|x_i|+delta/2 in both coordinates. Every lattice point z with |epsilon_j z_i|<|x_i|+delta/2 is then fired by the order-ideal property; in particular this includes a neighbourhood of x. A finite subcover proves the assertion for compact subsets. Outer containment in every fixed neighbourhood of K follows directly from Hausdorff convergence. This also applies to the union of unit cells, since replacing sites by cells changes Hausdorff distance by at most epsilon_j/sqrt(2).

### Lemma 3: density at least two in any fully fired region

Let A be any finite set all of whose sites have fired. Order A by the times of their last firings, with ties impossible in a sequential legal schedule. At the last firing of x its remaining height is nonnegative. For every neighbour y in A whose last firing occurs later, x subsequently receives at least one chip. Thus eta(x)>=the number of neighbours in A with later last firing. Summing counts each undirected internal edge once, proving

    sum_{x in A} eta(x) >= |E(A)|.

The weighted version, for nonnegative weights phi supported on fired sites, is

    sum_x eta(x) phi(x) >= sum_{edges {x,y}} min(phi(x),phi(y))
                              = 2 sum_x phi(x) - (1/2) sum_edges |phi(x)-phi(y)|.

To prove the inequality use the same last-firing order on the finite support of phi; an edge contributes the weight of its earlier endpoint, at least the minimum of its endpoint weights. Edges meeting a zero weight contribute zero to the right side. For the equality use min(s,t)=(s+t-|s-t|)/2 and degree four. This argument uses nonnegativity of the final height at fired sites, which was proved above.

Take phi(x)=phi_cont(epsilon x) for a smooth nonnegative function supported compactly inside a limiting fired domain. Lemma 2 ensures all its support sites are fired. After multiplication by epsilon^2, the edge variation error is O(epsilon): there are O(epsilon^-2) relevant edges and each weight difference is O(epsilon). The upper bound eta<=3 holds pointwise. Consequently every weak limit of final heights has density between 2 and 3 inside the limiting domain.

### Lemma 4: continuum consequences if H=0 had a polygon limit

Let epsilon=n^-1/2 and U_n(x)=n^-1 u_n([sqrt(n)x]). Pegden--Smart, Theorem 4.2 and the fundamental-solution convergence used there, give local uniform convergence away from 0 to a nonnegative continuous U. The discrete conservation equation tested against any smooth compactly supported test function away from 0 gives

    Delta U = g

in distributions, where 0<=g<=3 locally. Indeed, summation by parts converts epsilon^2 sum eta(x)phi(epsilon x) into epsilon^2 sum (u(x)/n)[epsilon^-2 Delta_discrete phi(epsilon x)], and the bracket converges uniformly to Delta phi. Standard Riemann sums and local uniform convergence finish the passage. The source term vanishes for these tests. The heights have weak-* subsequential limits by their boundedness; the displayed identity identifies the limit uniquely as Delta U.

If epsilon S_n has a convex polygon Hausdorff limit K, then U=0 outside K by outer containment and local uniform convergence. Continuity gives U=0 on its boundary. Lemmas 2 and 3 give 2<=g<=3 almost everywhere inside K. Outside K, U=0 on an open set, so g=0 there; the boundary of K has area zero. Thus near a non-source vertex, Delta U is a bounded nonnegative function, lies in [2,3] in the interior sector, and vanishes outside it. No boundary measure can occur, because Delta U was obtained as a weak limit of bounded height functions on the entire neighbourhood.

### Lemma 5: the corner inequality

Suppose u is continuous and nonnegative in a disk about 0, u(0)=0, and Delta u=g is a bounded function. Suppose near 0, u vanishes outside a sector -alpha/2<theta<alpha/2, with pi/2<alpha<pi, and

    a <= g <= b inside the sector,    g=0 outside,

where 0<a<=b. Then necessarily

    a <= b(1-sin(alpha)).                                      (C)

Full analytic proof. Convolve u and g with a nonnegative smooth approximate identity on a slightly smaller disk. The smooth functions u_delta satisfy Delta u_delta=g_delta, with 0<=g_delta<=b, and u_delta converges locally uniformly to u. For a smooth function the divergence theorem gives M_delta'(r)=(2pi r)^-1 integral_{B(0,r)}g_delta. Integrating this identity and passing to the limit (the bound b controls the integrand at r=0) proves the mean identity below. The same calculation centered at any x gives the submean inequality when g>=0; integrating circle averages gives the ball submean inequality. This establishes subharmonicity without a separate regularity assumption. Let M(r)=(2pi)^-1 integral_0^{2pi}u(r,theta)dtheta. The mean-value identity for the Poisson equation is

    M(r)=u(0)+ integral_0^r (1/t) integral_0^t s*g_avg(s) ds dt.

It implies 0<=M(r)<=b r^2/4. For |x|<=r with 2r inside the disk, subharmonicity and nonnegativity give

    u(x) <= (pi r^2)^-1 integral_{B(x,r)}u
          <= (pi r^2)^-1 integral_{B(0,2r)}u <= 2b r^2.

Hence u=O(r^2) uniformly near the vertex.

Put F(r)=integral_{-pi}^{pi}u(r,theta)cos(2theta)dtheta and G(r)=integral_{-pi}^{pi}g(r,theta)cos(2theta)dtheta. Test the distributional equation with psi(r)cos(2theta), for smooth psi supported in an annulus. The polar-coordinate formula for its Laplacian gives integral F(r)(psi''+psi'/r-4psi/r^2)r dr=integral G(r)psi(r)r dr. Thus Fourier projection of the Poisson equation gives

    F'' + r^-1 F' -4r^-2 F = G.

There is no angular boundary term: these integrals are over the full circle, with periodic angular test function. On the central interval (-pi/4,pi/4), cos(2theta)>=0; its integral is 1. On the rest of the sector it is nonpositive, with absolute integral 1-sin(alpha). Therefore

    G(r) >= a-b(1-sin(alpha)) =: kappa

for almost every sufficiently small r. Also |G(r)|<=2pi b and F(r)=O(r^2).

Set f(r)=F(r)/r^2. Direct differentiation, interpreted first in distributions on 0<r<r_0, yields

    (r^5 f'(r))' = r^3 G(r).

A distribution with derivative r^3 G is an absolutely continuous primitive plus a constant. Hence f is locally absolutely continuous and, because G is bounded, r^5 f'(r)=C+integral_0^r s^3 G(s)ds. If C!=0, integration makes f grow as -C/(4r^4), contradicting boundedness of f. Hence C=0. If kappa>0, this identity gives f'(r)>=kappa/(4r). Integrating from r to a fixed small r_0 gives

    f(r_0)-f(r) >= (kappa/4)log(r_0/r),

again contradicting boundedness of f as r decreases to zero. Thus kappa<=0, proving (C).

### Consequence for H=0

A regular dodecagon has interior angle alpha=5pi/6, so sin(alpha)=1/2. Lemma 4 gives a=2 and b=3 at each of its vertices. Inequality (C) would require 2<=3/2, a contradiction. Thus the proposed regular dodecagon limiting fired shape at H=0 is impossible. This disproves the universal answer proposed in Question 6.2, The checks of those lemmas are recorded below. It does not identify the actual shape.

### Extension to all H>=-1

Bou-Rabee Theorem 9.2, PDF page 28, supplies the same local uniform odometer convergence for constant background -H<=2. The weighted last-firing argument now gives H+2<=Delta U<=H+3 inside an assumed polygon limit, and Delta U=0 outside. For H>=-1 these bounds are positive, so Lemma 5 applies with a=H+2 and b=H+3. Writing k=H+3>=2, the corner of a regular 4k-gon has alpha=pi-pi/(2k). Inequality (C) would require sin(pi/(2k))<=1/k. Strict concavity of sin on [0,pi/2] gives sin(t)>2t/pi for 0<t<pi/2; taking t=pi/(2k) contradicts this. The H=-2 case has a=0, so the obstruction gives no contradiction and the known square remains consistent.

For a different scalar normalization with a nondegenerate compact polygon limit, the inner and outer ball bounds of source Theorem 6.3 (valid for H>=-1) force its scale to be comparable to sqrt(n). Pass to a subsequence of the scale ratios to get the same regular polygon, up to a fixed positive dilation, under sqrt(n) normalization. The argument above therefore also excludes such normalizations.


## Hostile-referee audit

1. **Fired set versus positive-height set.** The comparison and last-firing arguments use S={u>0} throughout. Outer support containment alone is used to set U=0 outside K. No claim identifies S with the support of final heights.
2. **Housekeeping at a reflected source.** In Lemma 1 the reflected source has Delta(u o rho)<=H+3-n, so it also satisfies the needed upper bound H+3. The original source lies on the retained side. Crossing edges are checked explicitly for both parity choices of k. Exact arrays from all 22 runs satisfy the resulting coordinate monotonicity.
3. **Convergence of sets versus interiors.** Lemma 2 establishes interior filling from Hausdorff convergence and coordinate monotonicity, rather than assuming it. It works for all orientations of the hypothetical polygon. D4 invariance centers any nondegenerate regular polygon at the origin (its unique center is fixed by the half-turn), so vertices are away from the source.
4. **Mean heights, not individual heights.** Eta need not be >=2 at every fired site. The exact last-firing inequality is weighted and its error is O(epsilon) after normalization. Thus it gives a distributional lower bound 2 in the continuum, which suffices. Numerical checks in 88 fully fired boxes obey sum eta>=internal edge count. The proof handles arbitrary weighted tests and is not based on those 88 examples.
5. **No boundary delta mass.** Distributional Delta U is a weak limit of globally bounded final heights (shifted by H), so it is an L-infinity function near each non-source vertex. An unaccounted line measure cannot invalidate the full-circle Fourier equation. For general H, the microscopic shifted heights can be negative when H=-1, but in the polygon interior the weighted lower bound is H+2, outside K the limiting Laplacian is zero, and the polygon boundary has area zero. This proves nonnegativity of the limiting Laplacian near the corner before using subharmonicity.
6. **Quadratic growth.** It follows from nonnegativity, u(0)=0, and 0<=Delta u<=b by the mean identity and ball averages; no C^{1,1} theorem is assumed. The full-circle test on annuli justifies the weak ODE; the explicit integration of that ODE supplies the required local absolute continuity.
7. **Sign of the Fourier equation.** For F=r^2 f, the operator F''+F'/r-4F/r^2 is r^2 f''+5r f'. Thus (r^5 f')'=r^3 G with the positive sign used in the proof. corner_checks.py tests this against genuine C1 wedge functions u=r^2 cos^2(pi theta/alpha), zero outside the wedge: their Fourier forcing projection is zero, and their density ranges satisfy the necessary inequality. It also checks the contradiction margin numerically for H=-1,...,100. These are corroborating computations, not substitutes for the analytic argument.
8. **Integration constant.** Bounded G makes r^5 f' have a finite limit C at 0. C!=0 implies f has a power divergence, contradicting f=O(1); after C=0, positive G forces logarithmic divergence. Both potential failure modes are treated explicitly.
9. **Asymptotic scope.** A finite nonregular aggregate is not the counterexample. The proof rules out even a subsequential nondegenerate regular-polygon Hausdorff limit at H=0 (and at every H>=-1 using the later convergence theorem). The hypothetical polygon's orientation does not enter the corner inequality: rotate the local coordinates to the vertex bisector.
10. **Scope of external results.** The H=0 disproof needs only the ordinary sandpile convergence of Pegden--Smart, not any unproved statement about the Apollonian free boundary. The extension to H>=-1 uses Bou-Rabee's stated Theorem 9.2 for constant backgrounds. The mean-value and weak-ODE identities are derived in Lemma 5; strict concavity of sine is the remaining elementary analytic input.

## Numerical summary and reproducibility

Run `python -X utf8 sandpile_experiment.py`, then `python -X utf8 larger_experiment.py`, `python -X utf8 referee_checks.py`, and `python -X utf8 corner_checks.py` from this problem folder. All 22 saved stabilizations passed the exact checks. Each run used less than 1 GB (the largest queue/height/odometer/flag allocation is about 26 MB, plus scratch arrays and compilation overhead); the longest observed stabilization was about 64 seconds. Results are exact for the chosen finite integer systems; directional support ratios are floating point diagnostics. Results from n=262144 include:

| H | axis support / sqrt(n) | 30-degree support / sqrt(n) | 45-degree support / sqrt(n) |
|---|---:|---:|---:|
| -1 | 0.466796875 | 0.491644026 | 0.466800961 |
| 0 | 0.363281250 | 0.371601986 | 0.375650478 |

These values do not establish a limiting curve and were not used to prove the counterexample.

## Remaining questions

The question as posed has a negative answer. What remains unknown here is the actual limiting fired domain and whether it has D_{4H+12} symmetry despite having no sharp regular-polygon corners. The proof does not establish the existence of the fired-set limit; it proves that any purported limit of the conjectured regular form is impossible. Odometer convergence is an established input. H=-2 is covered by the cited cube theorem and the explicit radius normalization discussed above.


## Auxiliary matrix check (not used in the counterexample)

Put t=sqrt(3), c=(20+8t)/13, v=(t/2,1/2), P=[[2,1],[1,1]], and B=c vv^T. Then 2<c<8/3<3, det(B)=0, det(P-B)=0, and the first diagonal entry of P-B is positive. Thus P-B is positive semidefinite with a nontrivial kernel, and B lies on the boundary of the matrix downset {A:A<=P}. Its normal direction is exactly 30 degrees, although P is rational. RankOneCertificate.lean checks these scalar determinant and positivity identities when completed. This illustrates why rationality of peaks alone was insufficient in the earlier intake. The actual polygon disproof above needs neither a classification of rank-one boundary matrices nor this auxiliary example.


## Additional consequence: a lower bound on the number of polygon sides

If alpha<=pi/2, cos(2theta) is nonnegative throughout the sector and its integral is sin(alpha)>0. The same ODE contradiction therefore excludes such a corner when a>0. For alpha>pi/2, Lemma 5 with a=k-1,b=k gives sin(alpha)<=1/k. Writing beta=pi-alpha, this says beta<=arcsin(1/k). A convex polygon with m genuine vertices has total exterior angle 2pi, hence necessarily

    m >= 2pi/arcsin(1/k),     k=H+3.

Since sin(pi/(2k))>1/k for k>=2, this bound is strictly larger than 4k. Thus even an irregular CONVEX polygon with only 4H+12 sides is excluded. At H=0 the lower bound is approximately 18.49, so any polygon has at least 19 sides; D4 invariance forces the number of vertices to be a multiple of four (every nonzero vertex has a four-element rotation orbit), giving at least 20 sides. This corollary does not exclude a curved domain with twelvefold symmetry.


## Verification status at completion

The complete counterexample is a written mathematical proof using published odometer convergence. The scalar/finite Lean certificate was submitted but remained queued at completion; no Lean theorem is claimed as machine checked. See LEAN_CHECK.md. The formalization is confined to finite summation and algebraic sign/determinant identities, not the convergence or Fourier argument. This pending backend check is a verification limitation, not an omitted mathematical implication in the written proof.
