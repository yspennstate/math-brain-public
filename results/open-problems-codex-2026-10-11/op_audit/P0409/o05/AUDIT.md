VERDICT: PASS (correct and complete)

# Independent hostile audit of P0409

Audit date: 2026-10-12. Claimant files read, without modification: STATUS.md, ATTEMPT.md, CLAIMS.jsonl, and LITERATURE.md in `~/brain_workers/TRIO_1011/op/P0409`. All audit artifacts are in this audit directory. References to line numbers below refer to the ATTEMPT.md read during this audit.

## Exactly what is claimed, and whether it answers the question

The claim is an exact integral characterization of the joint distribution of the entire unordered neighboring-vertex configuration under the vertex Palm law of the hyperbolic ideal Poisson–Voronoi tessellation, in curvature -1 and every integer dimension d >= 2. It is not restricted to the plane or to a symmetric incident configuration.

Write p = d-1 and let sigma be normalized spherical measure. The claimed construction is:

1. Sample the d+1 labeled incident ideal directions theta with density D(theta)/Z_d, where D is the absolute affine determinant of the rows (1,theta_j).
2. For each omitted direction i, orient the normal u_i to the affine span of the retained d directions so their common dot product a_i exceeds theta_i dot u_i.
3. Define H_i(phi;t_i) = [(1-a_i tanh(t_i))/(1-(phi dot u_i)tanh(t_i))]^p and A_theta(t) = integral max(0,H_0-1,...,H_d-1) sigma(dphi).
4. The joint edge-length survivor, conditional on theta, is (1+A_theta(t))^(-(d+1)). The neighboring coordinates are (cosh(T_i),sinh(T_i)u_i) in the hyperboloid model, or tanh(T_i/2)u_i in the Poincare ball. Finally forget labels.

These formulas specify a full distribution: upper rectangles, including thresholds zero for unused coordinates, determine all subcollection survivors and hence the multivariate distribution by inclusion-exclusion. The deterministic coordinate map then determines the entire neighboring point configuration. Integrating the stated angular density eliminates the latent incident directions. An elementary density is not required by the source question.

I independently downloaded https://arxiv.org/pdf/2303.16831, a 51-page PDF, into source.pdf and extracted source.txt. PDF page 48 contains Question 7.3 exactly as quoted: “What is the joint distribution of the neighboring vertices of a typical vertex?” Proposition 4.4 on PDF page 29 explicitly uses vertex Palm expectation and gives Gamma(d+1) for the exponential separation. Thus the claim addresses the correct notion of typical vertex, rather than a zero cell or a fixed-point conditioning. The source's normalization and d >= 2 scope agree with the attempt.

## Issues found

**One harmless source-reference error:** ATTEMPT.md line 69, Proof Step 1, attributes local finiteness and normality to “Theorem 1.3 and Proposition 3.8.” The precise proposition is **Proposition 3.7**, on PDF pages 17–18. Proposition 3.8 is “Tail bounds for crowding.” Theorem 1.3 is already correctly cited and states the needed tessellation properties, and the attempt gives a direct endpoint argument. Correct the proposition number. This is a bibliographic slip, not a missing mathematical hypothesis or a proof gap; no change to the result is needed.

I found no failing inequality, missing Palm bias, missing dependence term, dimensional restriction concealed as a general result, or unproved endpoint identification in the mathematical argument. The limitations below must nevertheless be retained: priority is not established, the formula is not an elementary joint density, and the whole probability theorem has not been formally verified.

## Independent proof checks

### Step 1: corona and score, lines 55–69

The source's Theorem 1.2, equations (3.2)–(3.3), Lemma 3.3, and equation (3.7) give normalized intensity sigma(dphi)dR and score R[|z-phi|^2/(1-|z|^2)]^p. Substitution of X_0=(1+|z|^2)/(1-|z|^2), X_vec=2z/(1-|z|^2) gives exactly R[X_0-X_vec dot phi]^p. The denominator and score base are positive throughout hyperbolic space. Taking p-th roots is legitimate for all d >= 2.

I also checked the hyperplane assertion: for two distinct directions, the Lorentz square of the difference of weighted null normals is -2kl(1-phi dot psi) < 0, where k,l > 0 are the p-th roots of the radii. Its zero set is therefore a genuine hyperbolic hyperplane. There is no exponent or factor-of-two error in the conversion.

### Step 2: full marked vertex Palm law, lines 71–110

This is the most consequential step, and I re-derived it rather than treating Proposition 4.4 as a proof of the stronger conditional environment statement.

At the origin, fixing global boundary directions and solving for their radii at common separation s gives R_j = s[sqrt(1+|v|^2)-v dot theta_j]^(-p). Its differential at v=0 is ds+ps theta_j dot dv, so the radial Jacobian is p^d s^d D(theta). The angular derivative of these radii vanishes there. Thus replacing global angles by angles centered at the equality point introduces no omitted angular cross-term in this Jacobian. Hyperbolic volume equals dv at the origin. The corona action preserves intensity and separation by the source's Lemma 3.10 on PDF page 20, so the centered computation extends to arbitrary equality points.

The equality point is unique for a nondegenerate tuple: the d independent homogeneous linear differences have a one-dimensional common kernel, meeting the positive unit hyperboloid at most once. Conversely, an affinely independent equal-separation tuple with no smaller nucleus is genuinely a vertex. For each inserted direction j, solving (theta_k-theta_j) dot v=-1 makes its linearized score strictly smaller than all other inserted scores. Only finitely many residual nuclei can compete near the origin, so their strictly positive score margins persist in a common neighborhood. This verifies all d+1 local cell cones and rules out an extra convex-hull condition. In particular, a simplex not containing the Euclidean origin is not to be discarded.

Slivnyak–Mecke then supplies the factor 1/(d+1)! for unordered tuples. The forbidden region has intensity s, giving exp(-s). Poisson independence on disjoint restrictions gives the unmodified residual PPP on R>s, even for bounded measurable functions of that residual process. The marked Campbell measure is consequently

    [p^d/(d+1)!] s^d exp(-s) D(theta) dVol(x) ds sigma^(d+1)(dtheta).

Normalization gives precisely independent Gamma(d+1,1) separation and D/Z_d incident angles, with the claimed residual conditional law. Integrating gives I_(d,0)=p^d Z_d/(d+1). Hadamard's row-norm bound and an open neighborhood of an inscribed nondegenerate simplex establish finiteness and strict positivity of Z_d. The proof uses the correct Palm measure, not an illicit conditioning of a deterministic point to be a vertex.

### Step 3: all outgoing rays, lines 112–125

The retained d directions impose d-1 independent spatial differences, leaving the line spanned by u_i. Along its positive geodesic ray the omitted score exceeds every retained score by s^(1/p)sinh(t)(a_i-theta_i dot u_i)>0. The orientation in the attempt is therefore correct. Coincident outgoing directions would make all d+1 angular points lie in one affine hyperplane, contradicting affine independence. The local gradient simplex has exactly d+1 one-dimensional cones. Thus these are all outgoing edges, not merely candidate directions.

### Step 4: first competitors and joint dependence, lines 127–149

Direct score comparison yields exactly R<sH_i(phi;t). For b=phi dot u_i and h(q)=(1-aq)/(1-bq), I independently obtained

    h(q)-1 = (b-a)q/(1-bq),
    h(r)-h(q) = (b-a)(r-q)/[(1-br)(1-bq)].

All denominators are positive for 0 <= q <= r < 1. A residual radius R>s can block only if b>a; its blocking threshold then increases strictly along the ray. These identities verify both the derivative and the nesting assertion, including the b<=a case. A competitor cannot appear and subsequently disappear before the endpoint.

For each fixed phi, the union of the blocking intervals is exactly the interval from s to s max(1,H_0,...,H_d). Its intensity is sA_theta(t), rather than the sum of separate intensities. The conditional joint void probability exp(-sA_theta(t)) follows. This handles both overlapping blockers and the shared root separation; it does not assume independence of the outgoing lengths.

### Step 5: actual finite adjacent vertices, lines 151–172

On a segment of length L, H_i is bounded by [(1+tanh L)/(1-tanh L)]^p = exp(2pL). Only finitely many residual nuclei can influence any such segment. Since every residual radius exceeds s, the initial segment has positive length.

The retained d distinct directions imply a_i<1. For epsilon=1-tanh(t), the cap |phi-u_i|<=sqrt(epsilon) has normalized measure of order epsilon^(p/2), b>=1-epsilon/2, denominator at most 3epsilon/2, and numerator at least (1-a_i)/2 for sufficiently small epsilon. Hence the positive blocking integral grows at least as a positive constant times epsilon^(-p/2), after subtracting the negligible cap-measure term. It diverges in every d >= 2, proving finite first crossing almost surely.

Finite restrictions imply the first crossing is attained. Continuous radii and the strictly monotone radius-to-crossing map exclude simultaneous blockers, by a countable union of bounded-window arguments. The newly active equality is transverse along the retained common geodesic, so together with the d-1 retained differences it has full tangent rank d. At that point exactly the retained d nuclei and one new nucleus are minimal. The omitted root nucleus remains strictly worse. Thus the endpoint is a vertex and the preceding open segment is an edge with no intermediate vertex. Distinct rays give distinct neighbors. The proof does not confuse a crossing of nonminimal scores with a vertex of the tessellation.

### Step 6 and planar normalization, lines 174–186

The Gamma integral is

    (1/d!) integral_0^infinity s^d exp[-(1+A)s] ds = (1+A)^(-(d+1)).

It uses the root shape d+1, not the fixed-point shape 1. At zero thresholds the survivor is 1, and the underlying Poisson construction guarantees multivariate consistency. Its lengths are positive and finite by Step 5.

For d=2, the labeled circular gaps have marginal density (1/pi)(1-g/(2pi)). Direct integration yields E[sin g]=1/pi. The determinant identity sin g_1+sin g_2+sin g_3 = 4 product sin(g_j/2) is positive for gaps summing to 2pi. Thus Z_2=3/pi and I_(2,0)=1/pi. This calculation correctly includes triangles whose convex hull excludes the center.

## Independent computational checks

I wrote and ran independent_checks.py with seed 1040905; results are in checks.json. I did not use the claimant's simulation output as evidence of independent verification.

For nonsymmetric incident tuples in dimensions 2, 3, and 4, centered finite-difference Jacobians agreed with (ps)^d D to relative errors 1.61e-12, 8.10e-10, and 1.33e-10, respectively. The dimension-4 tuple has all third coordinates negative, so its convex hull excludes the origin; this also exercises that important part of the claimed domain.

For each dimension, 250,000 independent sphere samples evaluated the angular integral. Separately, 15,000 independent Gamma-mixed PPP realizations tested the full joint survivor. The PPP radial window was bounded by s exp(2p max_i t_i), which includes every possible blocker at the prescribed thresholds, so this test has no omitted-tail bias.

| d | Formula prediction | Independent PPP estimate | Binomial standard error |
|---|---:|---:|---:|
| 2 | 0.622749 | 0.620400 | 0.003962 |
| 3 | 0.088540 | 0.086600 | 0.002296 |
| 4 | 0.020992 | 0.021600 | 0.001187 |

The angular integrals also have Monte Carlo uncertainty, recorded separately in checks.json. All comparisons agree within one listed binomial standard error even before accounting for that additional uncertainty. They are corroboration, not a substitute for the proof.

Independent ball-versus-hyperboloid scores agreed within 8.89e-16. I solved the crossing equation independently as q=(w-1)/(wb-a), with w=(R/s)^(1/p), requiring b>a and 0<q<1. Comparing these crossings against the proposed threshold criterion produced zero mismatches; checking nested thresholds produced zero violations.

For d=2 I also evaluated three single-ray spherical-cap integrals by adaptive quadrature and an independently integrated elementary antiderivative, with both negative and positive a. Absolute discrepancies were at most 1.95e-16. No computational check showed a counterexample.

The claimant's Lean compilation and historical simulation claims were not independently rerun. They are not needed for this verdict. The independently verified mathematical argument establishes more than the two rational inequalities reportedly formalized in Lean; no whole-theorem formal verification is asserted here.

## Bounded literature check and limits of the verdict

I made fresh HTTP requests through Python urllib, without built-in web search. The exact request URLs and returned abstracts are preserved in literature.json; raw arXiv feeds are in arxiv_ideal_voronoi.txt and arxiv_neighbors.txt. The arXiv searches were `all:"ideal" AND all:"Voronoi"` (30 results) and `all:"hyperbolic" AND all:"Voronoi" AND (all:"neighboring" OR all:"Palm")` (20-result limit, eight returned). OpenAlex searches for ideal Poisson Voronoi, hyperbolic Voronoi neighboring vertices, and citations of W4361807156 all returned HTTP 429. Those are unsuccessful searches and furnish no negative evidence.

I inspected the returned abstracts of the source and relevant follow-ups:

- arXiv:2408.10009v3 resolves cell indistinguishability, not the neighboring-vertex law.
- arXiv:2412.00822v1 concerns an L1 product of two hyperbolic planes and unbounded equal-separation loci.
- arXiv:2606.26049v1 gives face volume densities and typical face volumes, not a stated joint configuration law.
- arXiv:2606.30517v2 concerns convergence and general metric spaces, especially Diestel–Leader graphs.
- arXiv:2511.23317v1 concerns percolation uniqueness thresholds in products.

None of those abstracts states a solution to this exact question or a counterexample to the proposed formulas. This was an abstract-level bounded follow-up check, not a full-text exclusion of every theorem in those papers, and it is not a novelty or priority certificate. The independently fetched source itself still poses Question 7.3.

What stands is the exact full-dimensional vertex Palm integral law in ATTEMPT.md, conditional on the standard corona representation and invariance established in the source. An elementary closed-form joint density, worldwide novelty, and whole-theorem Lean certification are not established. There is no remaining mathematical conjecture needed for the stated integral characterization.
