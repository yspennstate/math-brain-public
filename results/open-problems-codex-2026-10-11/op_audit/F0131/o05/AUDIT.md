VERDICT: PASS

# Independent audit of F0131

Audit date: 2026-10-11. Claimant: `~/brain_workers/TRIO_1011/op/F0131`. I read STATUS.md, ATTEMPT.md, CLAIMS.jsonl and LITERATURE.md without modifying them. All audit artifacts were written in this audit folder.

## Exact claim and scope

ATTEMPT.md lines 3, 123, 127 and 129 claim a **negative answer**, not a construction of the conjectured polygon: for every integer H >= -1, no nondegenerate scalar-rescaled subsequential Hausdorff limit of the fired sets can be a regular (4H+12)-gon. H=0 alone refutes the proposed universal answer to Question 6.2. H=-2 retains the previously known square. The assertion concerns the usual four-neighbour conservative sandpile with initial height -H+n delta_0, and the set of sites that fired, rather than the final positive-height set or a divisible sandpile.

This answers the regular-polygon question as stated. It does **not** prove existence of a limiting fired domain for H>-2, identify its actual shape, or resolve the suggested D_(4H+12) symmetry. Those omissions are correctly stated at lines 156-158 and do not undermine a negative answer. The exclusion applies to subsequences as well as a full-sequence limit.

I found no failing mathematical step and no repair necessary to the main proof. This is acceptance of a written mathematical argument using published convergence results, not a claim of formal verification or an exhaustive novelty check.

## Step-by-step checks

1. **Finite sandpile facts, lines 11-21.** I re-derived the first-excess argument for least action. At the first site where a legal odometer would exceed a stabilizing integer competitor, its current height is at most 3, contradicting a legal firing. A lower bound on the competitor's proposed heights is not needed. Transport under signed coordinate permutations gives uniqueness and D4 symmetry; pointwise comparison of starting heights gives monotonicity. First firing times give connectivity because the background height is at most 2. Summing the finitely supported discrete Laplacian proves conservation. After a site's final legal firing its height is nonnegative. The warning about possibly negative shifted heights when H<0 is correct.

2. **Reflection comparison, Lemma 1, lines 43-47.** I checked the minimum construction against every neighbour case. At a site retaining u, all neighbours decrease or remain fixed. At a far-side site choosing reflected u, neighbours on that side lie below the reflected values. For even k, a neighbour on the reflection plane is fixed by reflection. For odd k, the crossing edge endpoints are interchanged and the minimum choice supplies precisely the needed inequality on the retained endpoint. The original source is on the retained side; the reflected source makes the Laplacian smaller by n, so it causes no violation. Thus the candidate stabilizes, least action forces equality, and k=2x_1-1 yields coordinate monotonicity. There is no unproved higher rotational symmetry in this argument.

3. **Interior filling, Lemma 2, lines 51-53.** For each interior x, a small displacement away from both coordinate axes still belongs to K. A nearby fired approximant dominates a whole coordinate rectangle containing a neighbourhood of x. Absolute-coordinate downward closure fills every lattice site there. A finite cover supplies the result for a compact interior subset. This closes the potential gap between Hausdorff set convergence and dense microscopic firing. The lemma applies to arbitrary polygon orientations. The phrase at line 51 about compact subsets consisting of fired lattice sites is read, as its proof explicitly does, as a statement about the rescaled lattice sites in those subsets, not about all real points being lattice points.

4. **Density bound, Lemma 3, lines 57-68.** I independently ordered sites by final firing time. Each internal edge delivers at least one chip to its earlier endpoint after that endpoint's final firing. This proves sum_A eta >= |E(A)|. With nonnegative weights the earlier endpoint's weight is at least the minimum of the two weights. On the degree-four lattice,

       sum_edges min(phi_x,phi_y)
         = 2 sum_x phi_x - (1/2) sum_edges |phi_x-phi_y|.

   The identity includes edges from the weighted support to zero weights. For smooth compactly supported rescaled weights there are O(epsilon^-2) relevant edges, with O(epsilon) variation on each, so the error after multiplying by epsilon^2 is O(epsilon). Thus the limiting final-height density is at least 2 on the filled interior. This is a weak density statement; individual fired sites need not have height at least 2.

5. **Continuum equation and support, Lemma 4, lines 72-78.** With epsilon=n^-1/2 and U_n=u_n/n, discrete summation by parts gives, away from the source,

       epsilon^2 sum_x eta_n(x) phi(epsilon x)
         = epsilon^2 sum_x U_n(epsilon x)
             [epsilon^-2 Delta_discrete phi(epsilon x)].

   The bracket converges to the ordinary, unnormalized continuum Laplacian. Local uniform odometer convergence and Riemann sums therefore yield Delta U=g. There is no missing factor of four. Uniform boundedness of microscopic heights makes g an L-infinity function throughout a neighbourhood of a vertex, precluding a boundary line measure. Outer Hausdorff containment gives U=0 outside K, and continuity gives zero boundary values. Interior filling and the weighted inequality give 2<=g<=3 inside K when H=0. D4 invariance places the center of a hypothetical regular polygon at the origin, so every vertex is away from the source (also see line 136).

6. **Corner obstruction, Lemma 5, lines 82-119.** I re-derived the entire argument. Mollification justifies the circular mean identity with bounded g; passing to the limit is controlled by the bound on g at small radii. It gives M(r)<=b r^2/4. The ball submean inequality and nonnegativity then give u(x)<=2b r^2 for |x|<=r. No unproved C^(1,1) estimate is being used.

   Full-circle projection onto cos(2 theta) gives

       F''+F'/r-4F/r^2=G.

   Since pi/2<alpha<pi, the positive central angular integral is exactly 1 and the magnitude of the negative integral within the sector is 1-sin(alpha). Therefore G>=a-b(1-sin(alpha)). Writing F=r^2 f gives exactly

       (r^5 f')'=r^3 G.

   Boundedness of f excludes the integration constant C: its contribution would be -C/(4r^4), whereas the bounded forcing contributes at most logarithmic growth. If the displayed lower bound on G were positive, the remaining primitive would imply f'>=kappa/(4r), contradicting boundedness by logarithmic integration. The necessary inequality a<=b(1-sin(alpha)) is therefore proved. Angular boundary terms are absent because the distributional test is on the full circle, not just the sector.

7. **Contradiction and extension, lines 123-129.** At H=0, alpha=5pi/6 and sin(alpha)=1/2, giving the impossible inequality 2<=3/2. For general H>=-1, the weak limit of shifted heights is Delta U, and its interior bounds are H+2 and H+3. For H=-1 some microscopic shifted heights can be negative; nevertheless the limiting function is positive inside, zero outside, and the polygon boundary has area zero, so the subharmonicity hypothesis at the corner still holds. Setting k=H+3 reduces the required inequality to sin(pi/(2k))<=1/k. Strict concavity of sine on [0,pi/2] proves the opposite for every integer k>=2. The source's inner and outer ball bounds make any alternative nondegenerate scalar normalization comparable to sqrt(n), so passing to a scale-ratio subsequence preserves the contradiction.

8. **Square and additional corollary, lines 29 and 168-172.** The cited cube theorem gives the H=-2 square. Its radius must tend to infinity because bounded support would bound the total height change despite n tending to infinity. Radius normalization then gives the square limit. For an acute or right corner the Fourier forcing is strictly positive when a>0, excluding that corner. For obtuse convex corners, beta=pi-alpha<=arcsin(1/k). Summing exterior angles yields m>=2pi/arcsin(1/k). At H=0 this is 18.488825470..., hence at least 19 vertices, and rotation by pi/2 has four-element orbits on nonzero vertices, hence at least 20. This excludes convex polygons with only the proposed number of sides; it does not exclude a curved domain with the proposed symmetry.

9. **Auxiliary matrix calculation, line 163.** Symbolic computation confirms det(B)=det(P-B)=0. Independently, c>2 and c<8/3 follow from 3/4<sqrt(3)<11/6. The first diagonal entry of P-B is (11-6sqrt(3))/13>0, so its zero determinant makes it positive semidefinite. B has rank-one direction (sqrt(3)/2,1/2), i.e. 30 degrees. This example concerns a matrix downset, and is not evidence about a sandpile free-boundary normal. The claimant correctly does not use it in the polygon proof.

## Independently checked external inputs and literature

I retrieved the following directly with Python urllib, without a built-in web search tool. PDFs and extracted text are saved here; HTTP statuses and byte counts are in fetch_log.json.

- https://arxiv.org/pdf/0801.3306: HTTP 200. PDF pages 29-30 verify the exact fired-set definition, Question 6.2, the H=-2 cube theorem, and Theorem 6.3. In dimension two its outer bound applies for H>=-1; the constants give precisely the scale comparability used at ATTEMPT.md line 129.
- https://arxiv.org/pdf/1105.0111: HTTP 200. Theorem 4.2, PDF page 9, states local uniform convergence of the regularized odometer and weak-* convergence of final heights. Section 2.3, pages 5-6, gives convergence of the discrete fundamental solutions locally uniformly away from the origin, providing the unregularized odometer convergence used at line 72. Its Laplacian convention agrees with the claimant's.
- https://arxiv.org/pdf/1909.07849: HTTP 200. Theorem 9.2, PDF page 28, explicitly treats n chips at the origin on a stationary ergodic background bounded above by 2d-2 and below by a finite constant, and states local uniform rescaled odometer convergence away from the origin. A point mass on the constant configuration -H is stationary and ergodic and satisfies these bounds. The high-density condition used elsewhere in that paper is not an additional hypothesis of this single-source theorem.

I also made two fresh arXiv API searches: sandpile combined with polygon/holes/corner (35-result limit), and with background/convergence/shape (45-result limit). Responses are saved as search_arxiv.txt and search_arxiv_scaling.xml. The screened abstracts include ordinary and random odometer convergence, non-Abelian octagon results, leaky sandpiles, exploding sandpiles, and growth on different lattices. None of these returned abstracts establishes an earlier exact solution of Question 6.2. In particular an octagon for Zhang's non-Abelian model is not an octagon theorem for this model. The retrieved Bou-Rabee and Pegden-Smart results are proof inputs, not statements of this corner obstruction.

The fresh OpenAlex query for "sandpile holes polygon limiting shape" returned HTTP 429. I did not obtain OpenAlex results and draw no conclusion from that failed request. The literature check is bounded and cannot certify novelty or absence of a prior result.

## Independent exact computations and limitations

I wrote an independent sparse integer queue stabilizer, not a wrapper around the claimant's programs. `independent_checks.py` performed 15 stabilizations: H=-2,-1,0,1,2 and n=128,512,2048. All passed stability, mass conservation, the exact height/odometer identity, coordinate monotonicity, reflection-candidate stability for k=1,...,8, and last-firing neighbour inequalities. Twelve independent integer weight assignments per run (180 total) passed both the weighted inequality and its degree-four identity. Batch firing times retain the correct order of each site's final firing in the expanded legal sequential schedule.

SymPy independently checked the Fourier ODE transformation, the two angular integrals, and both auxiliary matrix determinant identities. Numerical checks for k=2,3,4,10,100,1000000 confirmed the strict sine inequality; its proof for all k is the concavity argument above, not those samples. Full results are saved in independent_checks.json.

ATTEMPT.md lines 25 and 147 report 22 larger runs and 88 box checks. I did not replay those exact saved runs or independently certify their timing/memory figures. They are not used to establish the asymptotic result; my independent computations test the finite identities instead. Lines 175-177 explicitly say the Lean check was still queued and do not claim completed formal certification. A queued auxiliary certificate is neither evidence of success nor a mathematical gap in the written proof.

## Issues and disposition

No substantive error, missing hypothesis, or unsupported implication was found in the negative-answer proof. The lattice-site wording at line 51 should be understood as explained above; no proof change is needed. Numerical and pending formal-verification claims have only the limited evidentiary status stated here. The original regular-polygon proposal is disproved by the argument; existence, actual shape and higher dihedral symmetry remain unproved by this submission.
