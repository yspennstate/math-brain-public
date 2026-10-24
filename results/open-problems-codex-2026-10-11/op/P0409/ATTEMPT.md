# P0409: an integral formula for the full neighboring-vertex law

Date: 2026-10-12. Model: hyperbolic space of curvature -1, dimension d>=2. All surface measures below are probability measures. The result is an explicit compact-domain integral characterization, rather than an elementary joint density.

## Exact source and scope

D'Achille, Curien, Enriquez, Lyons and ?nel, *Ideal Poisson?Voronoi tessellations on hyperbolic spaces*, arXiv:2303.16831v3; Ann. Probab. 54(2), 846?891 (2026), DOI 10.1214/25-AOP1781. Question 7.3, PDF p.48, says:

> Question 7.3 (Typical neighboring vertices). What is the joint distribution of the neighboring vertices of a typical vertex?

?Typical? is the vertex Palm law of Section 4, not the zero cell. Proposition 4.4, PDF p.29, says:

> Proposition 4.4 (Typical separation). The separation of a typical vertex of V_d to its corresponding d + 1 ideal nuclei follows a Gamma(d + 1) distribution.

We determine the law of the unordered d+1 neighbors after moving the Palm vertex to the origin, up to the natural rotational ambiguity; a frame chosen independently and uniformly gives the isotropic version below. Randomly label the d+1 incident nuclei. This induces labels on outgoing edges, each edge omitting the corresponding nucleus. Forgetting those labels gives exactly the requested unordered law.

## Formula

Put p=d-1 and let sigma be uniform measure on S^(d-1). For theta=(theta_0,...,theta_d) in (S^(d-1))^(d+1), define

    D(theta) = |det M|,     M_j = (1, theta_j^T),
    Z_d = integral D(theta) sigma^(d+1)(dtheta).

The constant Z_d is finite and strictly positive. Sample theta with probability density D/Z_d. Almost surely theta is affinely independent. For each i let u_i be the unit normal to the affine hyperplane containing {theta_j : j != i}, oriented away from theta_i. Equivalently, all theta_j dot u_i, j != i, equal a_i and

    a_i > theta_i dot u_i.

For t_i in [0,infinity), set q_i=tanh(t_i), and define the explicit nonnegative integrand

    H_i(phi;t_i) = ((1-a_i q_i)/(1-(phi dot u_i)q_i))^p,
    A_theta(t_0,...,t_d)
       = integral max(0, H_0-1,...,H_d-1) sigma(dphi).

Every denominator is positive at finite t_i. The full conditional joint law of the positive, finite edge lengths T_0,...,T_d is specified by

    P(T_i>t_i for every i | theta)
       = [1+A_theta(t_0,...,t_d)]^(-(d+1)).             (J)

In the hyperboloid model H^d={X=(X_0,X_vec): X_0^2-|X_vec|^2=1, X_0>0}, the neighbors are

    V_i = (cosh T_i, sinh T_i u_i).                   (N)

In the Poincare ball, equivalently, V_i = tanh(T_i/2) u_i. Thus (J), the density D/Z_d and the deterministic map (N) give the joint distribution of all neighboring vertex coordinates in every dimension d>=2. There is no unevaluated random tessellation or residual Poisson process in this formula.

More directly, for any measurable angular event B,

    P(theta in B, T_i>t_i for all i)
       = (1/Z_d) integral_B D(theta)
           [1+A_theta(t)]^(-(d+1)) sigma^(d+1)(dtheta).

These upper rectangles determine the length law: set unused thresholds to zero to obtain every subcollection survivor, then apply finite inclusion-exclusion to obtain the joint distribution function. The resulting joint coordinate law follows by measurable pushforward. Conditioning on theta is allowed even though theta is additional latent information; integration eliminates it completely.

## Proof

### 1. Corona model and linear comparisons

The source's Theorem 1.2, equations (3.2), (3.3), (3.7), and Lemma 3.10 identify the ideal nuclei with a Poisson process on S^(d-1) x (0,infinity) having intensity sigma(dphi) dR. In the Poincare ball the exponential separation is

    R (|z-phi|^2/(1-|z|^2))^p.

The conversion X_0=(1+|z|^2)/(1-|z|^2), X_vec=2z/(1-|z|^2) gives exactly

    s_(phi,R)(X) = R [X_0-X_vec dot phi]^p.           (1)

This agrees with R at the origin o=(1,0). The bracket is strictly positive throughout H^d, because X_0>|X_vec|. Taking p-th roots preserves all comparisons. Therefore comparisons are between restrictions of homogeneous linear forms

    f_(phi,R)(X)=R^(1/p)[X_0-X_vec dot phi].

Their equalities are hyperbolic hyperplanes, and cells are intersections of hyperbolic halfspaces. The source proves local finiteness and normality (Theorem 1.3 and Proposition 3.8). In particular, vertices have exactly d+1 incident cells and d+1 outgoing edges. We also establish below directly that the edge endpoints used in the formula are finite and nondegenerate.

### 2. Palm law of the complete root environment

We prove the strengthened version of Proposition 4.4 needed here: under vertex Palm,

* S has density s^d exp(-s)/d!;
* the randomly labeled incident directions have density D/Z_d and are independent of S;
* given S=s and theta, the other nuclei are an independent Poisson process of intensity sigma(dphi) dR restricted to R>s.

Use the (d+1)-fold Slivnyak?Mecke formula to count vertices by their unordered tuples of incident nuclei. The factor is 1/(d+1)! if tuples are integrated in ordered form. Each nondegenerate tuple can produce at most one equality point in H^d: the d linear differences f_j-f_0 have rank d, their common nullspace is a line in R^(d+1), and such a line meets the positive sheet of the unit hyperboloid in at most one point. Tuples of deficient rank, or having additional ties with other nuclei, have zero intensity. For rank at a generated vertex this is also clear from the nonzero determinant below. Nondegeneracy for actual vertices follows from source normality.

Parametrize a tuple with an equality point by that point x, its common separation s, and the incident angles as seen from x. We compute the local Jacobian at o. Temporarily hold global boundary angles phi_j fixed and use spatial hyperboloid coordinates v=X_vec; then X_0=sqrt(1+|v|^2). Equation (1) requires

    R_j = s [sqrt(1+|v|^2)-v dot phi_j]^(-p).

At v=0, R_j=s and the differential is

    dR_j = ds + ps phi_j dot dv.

Thus the absolute radial Jacobian with columns (s,v_1,...,v_d) is

    (ps)^d |det[(1,phi_j^T)]| = p^d s^d D(phi).     (2)

At v=0 hyperbolic volume is dv. Replacing global angles by angles as seen from x does not change (2) at o: at x=o the angular map is the identity; also the radial derivatives with respect to angles vanish there, since all R_j=s independently of the angles. The full derivative has block form with zero upper-right block and identity angular diagonal block. The angular-x derivatives therefore do not affect its determinant.

The source's corona action preserves sigma(dphi) dR, separations, and hyperbolic volume (Lemma 3.10). Move any x to o by this action. Consequently the same Jacobian in centered angular coordinates holds at every x. Local smooth inverse charts with D>0 and the uniqueness just proved justify ordinary change of variables without multiplicity. Frame changes only rotate the angles and preserve D and sigma. This yields tuple measure

    p^d s^d D(theta) dVol(x) ds sigma^(d+1)(dtheta).

At o the excluded region is {R<s}, whose intensity is s. Its Poisson void probability is exp(-s). Conditional on the void, the process on R>s is unaffected and independent, since Poisson restrictions to disjoint sets are independent. Insertion of the tuple itself does not alter that remaining process by Mecke. Therefore the marked vertex intensity, including any bounded measurable functional of the centered residual process, is obtained by integrating

    [p^d/(d+1)!] s^d exp(-s) D(theta)
         dVol(x) ds sigma^(d+1)(dtheta)

against the law of the residual Poisson process on R>s. This is the refined Campbell characterization of vertex Palm. Normalizing gives the asserted three bullet points, and also

    vertex intensity I_(d,0) = p^d Z_d/(d+1).

Finiteness of Z_d follows from Hadamard's inequality, D <= 2^((d+1)/2). Positivity follows by choosing d+1 vertices of a nondegenerate inscribed simplex and a small open neighborhood of those directions. Every proper subset of an affinely independent tuple is affinely independent, so the edge normals below are well defined outside a Palm null set.

There is no hidden condition that the origin lie in the convex hull of the theta_j. Here is a direct local verification, needed for counting inserted tuples as vertices. For any j, the d vectors theta_k-theta_j (k != j) are linearly independent. Solve (theta_k-theta_j) dot v=-1 for all k != j. For sufficiently small epsilon>0, at X=(sqrt(1+epsilon^2|v|^2),epsilon v), nucleus j has strictly smaller separation than every other inserted nucleus, by (1). Thus every inserted nucleus has a nonempty open local cell cone. Under the void R<s, the residual process stays strictly worse in a sufficiently small neighborhood: in a ball of any fixed small radius, every potentially competitive radius is bounded above by a deterministic multiple of s, leaving only finitely many residual nuclei; each is strictly worse at the origin, so continuity gives a common neighborhood where all remain worse. Consequently exactly the d+1 inserted local cell cones meet at the isolated equality point, and it is a vertex. This matters, since restricting to simplices containing the origin would give the wrong Palm law.

### 3. Identify the outgoing rays

Fix s and an affinely independent theta. Remove theta_i. The d-1 differences theta_j-theta_k among the retained d points span a subspace of dimension d-1. Their orthogonal complement is a line. Either unit vector on this line has common retained dot product a_i. Affine independence ensures the omitted point has a different dot product. The specified sign is therefore unique.

The common-equality locus of the retained d nuclei is the geodesic through o in that line:

    X_i(t)=(cosh t,sinh t u_i), t in R.

Indeed, their equal separations are s[cosh t-a_i sinh t]^p. At t>0 the omitted incident nucleus has larger p-th-root separation, since

    f_i(X_i(t))-f_j(X_i(t))
       = s^(1/p) sinh t (a_i-theta_i dot u_i)>0.

Thus precisely t>=0 is the locally valid outgoing ray for that retained tuple. The d+1 choices give distinct rays: coincidence of two u_i would force all theta_j to have the same dot product along a nonzero vector, contradicting affine independence. These are all outgoing edges, either by normality or by the d+1 one-dimensional cones dual to facets of the affine gradient simplex. For completeness, equality of d minimal forms restricts a local edge to one of these lines; fewer than d equalities has local dimension at least two, and d+1 gives the vertex. Hence no extra edge is omitted.

### 4. First competitor and nested blocking sets

Let (phi,R) be a residual nucleus, with R>s, and let b_i=phi dot u_i. It beats the retained d nuclei at X_i(t) if and only if

    R < s [(cosh t-a_i sinh t)/(cosh t-b_i sinh t)]^p
      = s H_i(phi;t).                              (3)

All bases are positive. Write q=tanh t. For 0<=q<1,

    h(q)=(1-a_i q)/(1-b_i q),
    h'(q)=(b_i-a_i)/(1-b_i q)^2.

If b_i<=a_i, then h(q)<=1 and the nucleus with R>s never blocks this ray. If b_i>a_i, h increases strictly from 1. A nucleus that blocks at one time continues to block at all later times. This monotonicity is the step that allows us to replace avoidance along the whole segment by avoidance at its endpoint.

Define T_i as the first blocking time. For finite t_i, the set of residual nuclei that can block by time t_i is

    B_i(t_i)={(phi,R): s<R<s H_i(phi;t_i)}

with an empty radial interval wherever H_i<=1. Boundary ties have zero probability at any prescribed finite t_i. The union over i consists, at each phi, of the single interval from s to s max(1,H_0,...,H_d). Its intensity is exactly s A_theta(t). It follows that

    P(T_i>t_i for all i | S=s,theta)=exp[-s A_theta(t)]. (4)

This argument keeps the common residual process for all rays. Multiplying the separate void probabilities would be incorrect whenever the blocking sets overlap.

### 5. First crossing really is a finite adjacent vertex

For any fixed L<infinity, all nuclei that can block any outgoing segment of length L have

    R <= s max_i [(1+q)/(1-q)]^p, q=tanh L.

This follows from |a_i|<=1 and |phi dot u_i|<=1. There are only finitely many such residual nuclei almost surely. Each is strictly worse at t=0, so the first crossing is strictly positive if it is finite. Alternatively the locally finite root configuration immediately gives a positive initial edge segment.

Each T_i is finite almost surely. The retained d angles include at least two distinct points, since d>=2. Hence a_i<1: dot product 1 along u_i would force all retained points to equal u_i. Set epsilon=1-q for q approaching 1. On the spherical cap |phi-u_i|<=sqrt(epsilon), b_i>=1-epsilon/2, whence

    1-b_i q <= 3 epsilon/2,
    1-a_i q >= (1-a_i)/2

for all sufficiently small epsilon. Thus H_i >= c epsilon^(-p) on that cap, for a positive constant c depending on theta. The normalized cap measure is >= c' epsilon^(p/2). This follows directly by parametrizing a neighborhood of u_i on the sphere by its p-dimensional tangent coordinates: the area density is bounded below on a fixed sufficiently small neighborhood. Therefore

    integral (H_i-1)_+ sigma(dphi) -> infinity

at least as a positive multiple of epsilon^(-p/2). By (4), P(T_i>t | s,theta) tends to zero as t tends to infinity.

The first finite crossing is attained: on a compact segment containing it there are only finitely many possible blockers. Each blocker has at most one crossing, by strict monotonicity, and the first time is the minimum of their crossing times. Exactly one residual nucleus ties there almost surely. To justify uniqueness, condition on the finite collection of angles in a bounded radial window: their radii have continuous joint densities; for a fixed angle with b_i>a_i its finite crossing time is an injective smooth function of its radius. Equality of two crossing times therefore has zero probability. A countable union over integer windows proves the assertion globally.

At this endpoint the retained d root nuclei and this one residual nucleus are all minimal. The crossing is transverse: equality in (3) with R>s forces b_i>a_i and has a strictly positive derivative of h; after crossing the new nucleus beats the retained set. The retained equality constraints are exactly (theta_j-theta_k) dot X_vec=0. Their spatial normals span u_i-perpendicular, so their restrictions to the hyperboloid tangent space at X_i(t) have rank d-1 along the geodesic, and the new equality is independent of them because it is transverse along their common tangent. Thus this is a normal vertex with exactly d+1 incident minimal nuclei. The open segment from o to it has exactly the retained d nuclei minimal, so it is an edge interior, with no intermediate vertex. This vertex is precisely the neighbor V_i. Distinct ray directions give distinct neighbors.

### 6. Integrate the correct Palm mark

By Step 2, S is independent of theta with Gamma(d+1,rate 1) density. Integrating (4),

    P(T_i>t_i for all i | theta)
      = (1/d!) integral_0^infinity s^d exp[-(1+A)s] ds
      = (1+A)^(-(d+1)).

For the last equality substitute y=(1+A)s and use integral y^d exp(-y)dy=d!, which follows by d integrations by parts from integral exp(-y)dy=1. This proves (J), and Steps 3?5 prove (N). All variables are finite and positive; at t=0, A=0, giving survivor 1. Formula (4) is an actual Poisson void law, so (J) has the required multivariate positivity properties automatically. This completes the full distributional characterization.

## Optional planar normalization

For d=2, Z_2=3/pi, so the angular density is (pi/3)D and the vertex intensity is 1/pi. To check this without a reference, fix one labeled point at angle zero by rotational invariance and order the other two. The successive circular gaps g_1,g_2,g_3 are uniform on {g_j>0, sum g_j=2pi}. For that circular order the determinant has absolute value sin g_1+sin g_2+sin g_3 (positive because it equals 4 sin(g_1/2) sin(g_2/2) sin(g_3/2)). Each gap has density (1/pi)(1-g/(2pi)) on (0,2pi). Integration gives E sin g=1/pi, hence E D=3/pi. This includes triangles not containing the center.

## Referee audit and computational checks

1. Wrong Palm bias: the Mecke Jacobian has s^d, not s^(d-1) or constant. It reproduces Proposition 4.4 exactly. The angular tilt is absolute affine determinant; no convex-hull indicator.
2. Corona score exponent: equation (1) uses p=d-1, whereas the source's ball distance comparison can also be written with exponent 1/(2p) on R. The hyperboloid conversion above verifies the score and avoids a factor-of-two error.
3. Direction sign: choose a_i>theta_i dot u_i. Step 3 explicitly checks the omitted nucleus is worse, not better.
4. Dependence: integrate the maximum of radial thresholds, rather than the sum. Formula (4) keeps overlaps of blocking sets and the single common S.
5. Possible blockers appearing before the endpoint then disappearing: impossible by Step 4's monotonicity. The rational threshold monotonicity and threshold-above-one equivalence are kernel-checked in Threshold.lean; lake env lean exited 0 (see lean_check.txt). The Lean file checks only the two real rational inequalities, not Palm calculus or the whole theorem.
6. Infinite or zero edge lengths, unrealized infima, multiple ties: Step 5 addresses each using cap bounds and finite restrictions of the Poisson process.
7. Jacobian and uniqueness: Step 2 treats angular-coordinate cross terms and excludes extra equality roots. The residual conditional process is justified by Mecke plus disjoint Poisson restrictions, rather than by conditioning a fixed point to be a vertex.
8. Conditional formulas at measure-zero symmetric theta: one may use the explicit kernel defined above; it extends to every affinely independent tuple. The regular-simplex checks test that kernel, not a positive-probability angular event.

Scripts and saved results:

* check_formula.py and checks.json: centered finite-difference radial Jacobians at regular simplices in d=2,3, relative errors 1.45e-10 and 1.23e-10. Joint-survival formula evaluated by 250,000 independent sphere samples, compared to 12,000 finite Poisson simulations each. For times (0.2,0.5,0.8), d=2 prediction 0.45905 versus simulation 0.45767 (binomial SE 0.00455). For d=3 times (0.2,0.4,0.6,0.8), prediction 0.08482 versus 0.08558 (SE 0.00254). Sphere integration error is additional, not counted in those binomial SEs.
* check_neighbors.py and neighbor_checks.json: samples D-biased angular tuples by rejection using the Hadamard bound, then generates successive finite radial Poisson blocks. Each sample is certified complete by checking that the largest possible threshold at each observed first crossing is below the final sampled radius. Thus unseen nuclei cannot alter any computed endpoint. All 3,000 trials in each d=2,3 certified, with zero budget truncations. Choose one neighbor uniformly per independent root, so KS data are independent. Neighbor separation is S[(1-a_i q_i)/sqrt(1-q_i^2)]^p. Means were 3.0685 (SE 0.0331) and 3.9425 (SE 0.0360), with Gamma(3) and Gamma(4) KS p-values 0.335 and 0.177. Numerical evidence supports the required rerooting marginal but is not used as proof.

Every job stayed well below 1 GB of arrays; the largest simulated sample had 42,529 nuclei. These checks are not a novelty certificate or an independent mathematical review.

## Remaining gap and interpretation

No mathematical gap is left in the integral characterization (J)?(N), conditional only on the standard corona representation, normality and isometry invariance proved in the source. This answers the literal request for the joint distribution; it does not claim an elementary closed-form density or independence of outgoing edges. Novelty and priority are not established by the bounded literature search. The full probability theorem has not been formalized in Lean.

Lean verification: Threshold.lean imports only Mathlib.Data.Real.Basic and Mathlib.Tactic.Linarith. Both theorems compile with exit code 0, with no sorry and no native_decide. This formalizes the algebraic nesting step only. The initial BOM-related parse failure was corrected by rewriting the file as UTF-8 without BOM before the successful run.
