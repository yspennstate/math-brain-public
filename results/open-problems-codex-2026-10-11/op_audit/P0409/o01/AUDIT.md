VERDICT: PASS (correct and complete)

Independent audit of P0409, 12 October 2026.

## What is claimed and what is proved

I read the claimant's STATUS.md, ATTEMPT.md, CLAIMS.jsonl and LITERATURE.md without modifying its folder. The substantive claim is the following, for every integer d >= 2 in curvature -1 hyperbolic space, under the vertex Palm distribution, with an independent uniform frame and uniformly labeled incident nuclei.

Write p=d-1 and let sigma be normalized sphere measure. The incident directions theta=(theta_0,...,theta_d) have density D(theta)/Z_d with respect to sigma^(d+1), where D is the absolute determinant with rows (1,theta_j). The root separation S is independent of theta and has Gamma(d+1, rate 1) law. For the outgoing direction u_i normal to the facet omitting theta_i, oriented so that its retained common dot product a_i exceeds theta_i dot u_i, define

    A_theta(t) = integral max(0, H_0(phi;t_0)-1,...,H_d(phi;t_d)-1) sigma(dphi),
    H_i(phi;t_i) = [(1-a_i tanh(t_i))/(1-(phi dot u_i)tanh(t_i))]^p.

Then the complete conditional joint survivor is

    P(T_i > t_i for all i | theta) = (1+A_theta(t))^(-(d+1)),

and the neighboring vertices are V_i=(cosh(T_i),sinh(T_i)u_i). Forgetting the labels and integrating theta yields the requested unordered configuration law.

This is a full integral characterization of the joint distribution in all the dimensions of the source, rather than merely a planar answer, a marginal, or a simulation recipe requiring an unknown tessellation. Upper rectangles, including zero thresholds for unused coordinates, determine the entire length distribution; the coordinate map determines the configuration distribution. Question 7.3 does not require an elementary density. The root is the vertex Palm root, not the fixed-point zero cell.

## Independent source verification

I fetched https://arxiv.org/pdf/2303.16831 directly with Python urllib and extracted the 51-page v3 PDF with PyMuPDF. The saved source.pdf and source.txt are independent downloads in this audit folder.

- PDF p.48, Question 7.3: "What is the joint distribution of the neighboring vertices of a typical vertex?"
- PDF pp.24-26 define the hyperbolic Palm distribution by averaging over the stabilizer frame; k=0 is explicitly the typical vertex.
- PDF p.29, Proposition 4.4 gives Gamma(d+1) separation at that vertex.
- PDF p.4, Theorems 1.2 and 1.3 give the sphere-times-radius Poisson model, normality, face-to-face structure and isometry invariance.
- PDF p.13, (3.2)-(3.3), and p.15, Lemma 3.3 and (3.7), give intensity sigma(dphi)dR and score R[(|z-phi|^2)/(1-|z|^2)]^(d-1).
- PDF p.20, (3.10) and Lemma 3.10 give the separation-preserving corona action and invariant intensity measure.

These are the hypotheses used in ATTEMPT.md, and they apply to all d >= 2. I did not infer the stronger angular/residual Palm law solely from Proposition 4.4; I checked the claimant's separate derivation of it.

## Proof audit, with locations

1. **ATTEMPT.md, Proof Step 1 (linear comparisons).** Independently substituting the Poincare-to-hyperboloid coordinates gives |z-phi|^2/(1-|z|^2)=X_0-X_vec dot phi. This bracket is positive. Taking the p-th root therefore gives the linear comparisons stated. The exponent is p, with no missing factor of two.

2. **Proof Step 2 (Palm law and Jacobian).** At the root, holding global boundary directions fixed, R_j=s[sqrt(1+|v|^2)-v dot phi_j]^(-p), hence dR_j=ds+ps phi_j dot dv. The absolute radial determinant is (ps)^d D. The full angular/radial Jacobian is triangular at v=0: radial derivatives in angular coordinates vanish there, and the angular diagonal map is identity. Thus angular dependence on the center does not supply an extra factor. The invariant corona action and hyperbolic volume extend this centered calculation to arbitrary centers.

   The d linear difference constraints have a one-dimensional kernel in the nondegenerate case, with at most one point on the future unit hyperboloid. This prevents multiplicity in the tuple parametrization. Counting unordered inserted tuples supplies 1/(d+1)!. The excluded region has measure s, so its void probability is exp(-s); Slivnyak-Mecke leaves the residual process independent above s. The resulting marked intensity is proportional to s^d exp(-s)D(theta). Its normalization gives Gamma(d+1), independence, and the asserted truncated residual Poisson law. In particular, integrating over s gives vertex intensity p^d Z_d/(d+1).

3. **Proof Step 2, final paragraph (no convex-hull indicator).** An affinely independent inscribed simplex need not contain the origin. Nevertheless, for each j, the linear system (theta_k-theta_j) dot v=-1 has a solution, providing a small region in which nucleus j is strictly minimal. Residual candidates in a fixed small ball have bounded radii and are finite in number, allowing a common neighborhood where they stay worse. The inserted tuple really produces a vertex. Restricting to simplices containing the origin would be erroneous; the claimant does not make that restriction.

4. **Proof Step 3 (edge rays).** The retained d directions have d-1 independent differences; their common equality set through the root is exactly the indicated geodesic. On the positive ray, the omitted root nucleus has larger root score by s^(1/p)sinh(t)(a_i-theta_i dot u_i)>0. The negative ray is invalid. Affine independence prevents two facet directions from coinciding. The local simplex comparison cones give precisely d+1 edges, consistent with source normality.

5. **Proof Step 4 (blocking and dependence).** Direct comparison gives R<sH_i. With b=phi dot u_i, differentiating (1-aq)/(1-bq) gives (b-a)/(1-bq)^2. For b<=a a residual radius R>s cannot block; for b>a the threshold is strictly increasing. Thus endpoint avoidance is equivalent to avoiding the whole preceding segment. All radial blocking intervals begin at the same s. Their union has measure s times the sphere integral of their maximum excess, not their sum. The common-process joint void probability exp(-sA_theta) is correct. Denominators are strictly positive for every finite threshold; tie boundaries at prescribed thresholds have zero intensity.

6. **Proof Step 5 (actual finite neighbors).** On any compact segment, every potential blocker has R<=s exp(2pL), so only finitely many are relevant. Their initial strict inequalities give a positive initial edge length. The retained points are distinct, so a_i<1. For q=1-epsilon, the cap |phi-u_i|<=sqrt(epsilon) has measure bounded below by a positive constant times epsilon^(p/2), while H_i is bounded below there by a positive constant times epsilon^(-p). Consequently its integrated positive excess diverges and each edge ends at finite distance almost surely.

   Finite windows make the first crossing a minimum, rather than an unattained infimum. Independent continuous radii give distinct crossing times almost surely. The first new equality is transverse to the retained equality geodesic; together the constraints have rank d. At that point precisely the retained d nuclei and one new nucleus are minimal. The omitted root nucleus remains strictly worse. The preceding open segment contains no vertex. This proves adjacency, not just an encounter with some score-equality surface. Distinct ray directions imply distinct neighboring vertices.

7. **Proof Step 6 and Formula (J)-(N).** Integrating exp(-sA) against s^d exp(-s)/d! gives (1+A)^(-(d+1)). Positivity and consistency of this multivariate survivor follow from the actual common Poisson construction; they are not assumed from an arbitrary proposed formula. The hyperboloid and Poincare coordinate maps are correct.

8. **Optional planar normalization.** Fixing one labeled angle and ordering the others produces uniform simplex gaps of sum 2pi. The determinant is the positive sum of their sines, or equivalently 4 times the product of their half-gap sines. The gap density is (1/pi)(1-g/(2pi)); integrating sin(g) gives 1/pi. Hence Z_2=3/pi and intensity 1/pi, including triangles outside the center-containing class.

No failed identity, missing hypothesis, missing dimension, wrong Palm bias, or unproved adjacency claim was found in these steps.

## Issues found

There is one harmless citation imprecision in **ATTEMPT.md, Proof Step 1**, the sentence citing "Theorem 1.3 and Proposition 3.8" for "local finiteness and normality." Proposition 3.8 is the crowding bound; the direct normality argument is in Proposition 3.7's proof, while Theorem 1.3 explicitly states normality. Name Proposition 3.7 for that attribution. Since Theorem 1.3 is already correctly cited and the needed theorem was verified, this is an editorial issue, not a gap in the result.

The literature and numerical qualifications in **Remaining gap and interpretation** and **Referee audit and computational checks** are appropriate. The result does not establish priority, an elementary closed-form density, or a machine-checked proof of the full theorem. The Lean claims were not rerun in this audit and are not needed for this verdict; the rational inequalities were checked directly above.

## Independent computations

I wrote and ran independent_checks.py rather than reusing the claimant's programs or saved results. It evaluates the original hyperboloid scores of a finite Poisson sample. The radial cutoff s exp(2p max(t_i)) rigorously includes every possible blocker at the tested thresholds. Gamma root marks are integrated by sampling. I also independently solve each score equality for q=tanh(t) and compare crossings with the direct score decisions.

| Dimension | Formula prediction | Direct-score frequency | Binomial SE | Trials |
|---|---:|---:|---:|---:|
| 2 | 0.541569 | 0.538615 | 0.006180 | 6500 |
| 3 | 0.337490 | 0.341231 | 0.005865 | 6500 |
| 4 | 0.091462 | 0.091538 | 0.003575 | 6500 |
| 5 | 0.043373 | 0.043231 | 0.002527 | 6500 |

The dimension-2 directions all lie in one open semicircle. Its sphere integral was evaluated by adaptive quadrature. For d=3,4,5 the integral used 180,000 independent sphere samples; estimated SEs of A were 0.000465, 0.001003 and 0.001477 respectively, additional to the binomial errors shown. All 26,000 score/crossing comparisons agreed. Finite-difference Jacobian relative errors in d=2,3,4,5 were respectively 2.77e-10, 2.96e-11, 1.14e-10 and 2.55e-10.

An independent planar angular sample gave Z_2=0.952911 with SE 0.001981 versus 3/pi=0.954930. Numerical integration of the gap identity gave 0.31830988618379075 versus 1/pi=0.3183098861837907. Full parameters and output are saved in independent_checks.json. These computations corroborate individual formulas; the preceding proof audit, not Monte Carlo agreement, supports the verdict.

## Bounded independent literature search

I queried arXiv and OpenAlex through Python HTTP requests and saved responses/statuses in literature_results.json. The arXiv API query and the three initial OpenAlex queries returned HTTP 429. An OpenAlex retry also returned 429; no successful OpenAlex search is claimed.

The ordinary arXiv HTML search for "ideal Voronoi" succeeded, as did a Crossref query and direct arXiv abstract fetches for 2606.26049, 2606.30517, 2602.06906, 2609.10007, 2408.10009 and 2412.00822. Responses are saved in literature_followup.json and the corresponding text files. The inspected abstracts concern face volumes, convergence on other spaces/graphs, Laguerre limits, random horoball polyhedra, cell indistinguishability, and product hyperbolic spaces. None of those abstracts asserts this full vertex-Palm neighbor law. The source v3 itself explicitly retains Question 7.3.

This bounded search identified neither an earlier exact solution nor a known counterexample. Follow-up abstracts and a limited search cannot exclude a theorem elsewhere in those papers or in unsearched literature. Novelty is therefore unestablished. That limitation does not undermine the independently verified mathematical characterization claimed here.
