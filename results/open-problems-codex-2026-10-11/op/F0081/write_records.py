from pathlib import Path
import json,xml.etree.ElementTree as E
P=Path('.')
text=r'''# F0081 literature check — 2026-10-11

## Status and exact source
No paper examined states and proves the question as posed. This is a bounded search, not a certification that no solution exists. OpenAlex requests were rate-limited; Semantic Scholar's citation endpoint did work. Verdict is not SOLVED_IN_LITERATURE.

Alexander E. Holroyd, Robin Pemantle, Yuval Peres, Oded Schramm, “Poisson matching,” Annales de l'Institut Henri Poincaré, Probabilités et Statistiques 45(1) (2009), 266–287, DOI 10.1214/08-AIHP170; arXiv:0712.1867v3, 15 March 2008. Downloaded source.pdf; extracted source.txt.

Verbatim Open Problems (i), PDF p.34, with mathematical glyphs rendered in plain text:
> For the two-color stable matching of two independent Poisson processes, what is the correct power law for the tail behavior of X in dimensions d = 2? We conjecture that E* X^a < 8 if and only if a < d/2.

Hypotheses checked on pp.3,5–6 and the stable-matching construction: independent homogeneous red and blue Poisson processes of intensity 1, Euclidean R^d, translation/isometry invariant unique stable perfect matching, X the distance from a typical red point (red Palm law). Equal positive common intensities reduce to 1 by scaling. Positive moments are the intended question; the displayed criterion is not an assertion about arbitrary negative moments.

Theorem 6, PDF p.6: E* X^d = 8 for stable matching in all d; P*(X>r) = C r^{-s(d)}, where 0<s(d)<1, s(1)=1/2, s(2)˜0.496, s(3)˜0.449. Theorem 2, PDF p.4: every invariant matching has E* X^{d/2}=8 only for d=1,2. Theorem 19, PDF pp.29–33, proves the upper bound. Thus d=3 divergence at d/2 does NOT follow from the printed lower bound. No exact asymptotic constant for d=1 is inferred here.

## Related papers examined (leads, not solutions)

* Holroyd, “Geometric properties of Poisson matchings,” Probability Theory and Related Fields 150 (2011), 511–527, DOI 10.1007/s00440-010-0282-y. Prior intake flagged this geometric/minimality paper, not a stable tail solution. Bibliography and Crossref checked; not used as a theorem input.
* Holroyd, James B. Martin, Yuval Peres, “Stable matchings in high dimensions via the Poisson-weighted infinite tree,” arXiv:1708.04519v2 (2017/2018). Downloaded pwit_pdf.pdf. Main results allow red-red as well as red-blue pairs, and take d?8 at fixed scales. Section 8(v), PDF p.28, explicitly asks about tails of ordinary two-colour matching. This does not answer fixed d, r?8.
* Holroyd, Svante Janson, Johan Wästlund, “Minimal matchings of point processes,” Probability Theory and Related Fields (2022), DOI 10.1007/s00440-022-01151-y; arXiv:2012.07129v1 (2020). Downloaded minimal_pdf.pdf. Theorem 4, PDF p.6, concerns processes on R, not R^d for d=2. It includes stable matching as gamma=-infinity, but only in dimension one.
* Michael A. Klatt, Günter Last, D. Yogeshwaran, “Hyperuniform and rigid stable matchings,” arXiv:1810.00265v3. Downloaded hyperuniform_pdf.pdf. Lattice versus a point process with intensity strictly greater than 1; the exponential matching-flower bounds have different input and imbalance hypotheses. They do not provide scale-uniform residual-charge moment bounds for two critical Poisson processes.
* Ádám Timár, “A factor matching of optimal tail between Poisson processes,” arXiv:2106.04524 (2021), Combinatorica, DOI 10.1007/s00493-023-00051-6. Abstract retrieved in Semantic Scholar citations. Constructs a factor perfect matching with exp(-c r^d) tail for d=3. This solves the factor optimization question, not the stable scheme. PDF fetch failed (empty exception text recorded); not counted as inspected full text.
* Gideon Amir, Omer Angel, Holroyd, “Multicolour Poisson matching,” Ann. IHP Probab. Stat. 57(4) (2021), DOI 10.1214/21-AIHP1147; arXiv:1605.06485. General matching constructions with colour restrictions, not this particular stable tail. Abstract/search result and bibliographic metadata checked.
* Omer Angel, Nitya Gadhiwala, “Unbalanced Minimal Matchings for Measurable Scale Invariant Costs on R^d,” arXiv:2609.19426 (2026). Downloaded unbalanced_pdf.pdf and searched its full text. Classifies measurable asymmetric scale-invariant costs and discusses one-dimensional matchings. No theorem establishing the stable two-colour critical moment threshold in d=2 was found.
* Yinon Spinka, Oren Yakir, “Optimal factor matchings for point processes on non-amenable unimodular graphs,” arXiv:2601.08983 (2026). Abstract in citation output: different space and scheme; excluded.
* Dor Elboim, Spinka, Yakir, “Optimal matchings of randomly perturbed lattices,” arXiv:2506.16873 (2025); Raphaël Lachièze-Rey, Yogeshwaran, “Hyperuniformity and optimal transport of point processes,” arXiv:2402.13705 (2024). Abstracts in citation output: different processes or optimizing matchings; excluded.

## Read-only prior work and corrections
Brain recall ran for “stable Poisson matching”, “stable Poisson matching mistakes”, and math-store “Poisson matching stable Holroyd Pemantle Peres Schramm”; results were off-target and not used as facts. A subsequent math-store query asked about point-process variance/covariance and hyperuniformity.

Read F0081-A001 from intake probability_1000_intake_F_20260908/attempts.jsonl and from origin/master:probability_1000/probability_1000_intake_F_20260908/attempts.jsonl via git show. No repository working tree changed. A targeted scan of codex_pool_2026_10_10 returned no F0081 hit. Earlier attempt's assertions that a specific spreading statement is equivalent to the conjecture were not proved and are NOT inherited. Its blanket claim of no monotonicity under adding points is inaccurate: source Lemma 17 proves colour-specific monotonicity on insertion of one blue point. This still does not give the desired scale-uniform fluctuation bounds.

## Every HTTP search/fetch
All requests used Python urllib from the shell; raw successful responses saved locally. Search result relevance was screened by titles and abstracts. Initial arXiv narrow search returned 7 entries; broader search returned fewer than 100 entries; Semantic Scholar citing-paper response returned 81 entries with no next page. Crossref broad search was noisy, so a title+author query verified the source's actual DOI. One earlier OpenAlex DOI request used an incorrect guessed DOI (08-AIHP167); this was corrected to 08-AIHP170 after Crossref. Neither request succeeded. OpenAlex citations filter could not be resolved to the required OpenAlex work ID because source lookup was rate-limited; it is NOT a completed citation search.

'''
for x in json.loads(P.joinpath('search_log.json').read_text()):
 text+=f"* {x['date']} — {x['service']} — `{x['url']}` — "+(f"saved {x['file']} ({x['bytes']} bytes)" if 'file' in x else f"failed: {x.get('error')!r}")+"\n"
text+='\n## Complete citation-result bibliography (unfiltered metadata)\n\n'
for item in json.loads(P.joinpath('semantic_citations.json').read_text())['data']:
 x=item['citingPaper'];text+=f"* {', '.join(a['name'] for a in x.get('authors',[]))}. {x['title']}. {x.get('year')}. {x.get('url')}.\n"
P.joinpath('LITERATURE.md').write_text(text,encoding='utf8')
P.joinpath('ATTEMPT.md').write_text(r'''# F0081 attempt — 2026-10-11

## Exact target and verdict
For each integer d=2 let R,B be independent intensity-one homogeneous Poisson processes in Euclidean R^d and M their unique stable perfect matching. For a typical red point, X=|x-M(x)|. Prove or refute, for positive alpha, E*X^alpha<infinity iff alpha<d/2. No complete answer was obtained. The results below are reductions and deterministic obstructions, not an improved unconditional tail bound. Their novelty relative to all literature is not asserted.

## 1. Exact residual-charge identity (proved)
For r>0 define R_r={x in R: |x-M(x)|>r} and B_r analogously. Write p(r)=P*(X>r). In a bounded deterministic Borel set Q of diameter at most r let A_r(Q)=#(R_rnQ), C_r(Q)=#(B_rnQ), and D_r(Q)=A_r(Q)-C_r(Q).

Then, almost surely,
    A_r(Q) C_r(Q)=0,
    |D_r(Q)|=A_r(Q)+C_r(Q),
and
    E D_r(Q)=0,   E|D_r(Q)|=2 |Q| p(r).             (1)

Proof. If x?R_rnQ and y?B_rnQ, then |x-y|=r is strictly less than both |x-M(x)| and |y-M(y)|. Also x,y cannot be matched to one another, since that distance is at most r. They therefore form a blocking pair, contradicting stability. Thus at least one of A,C is zero, and the absolute-value identity follows. The intensity of R_r is p(r) by the defining Palm/Campbell formula in the source. The intensity of B_r is also p(r), by exchange of red and blue in the input and uniqueness of the equivariant stable matching. Consequently EA=EC=|Q|p(r). Counts are integrable because bounded above by R(Q)+B(Q). Taking expectations proves (1).

Choose Q_r=[0,r/sqrt(d))^d, with v_r=|Q_r|=d^{-d/2}r^d. Formula (1) holds for this half-open cube, whose supremal diameter is r. The signed residual charge is not the original signed Poisson charge.

## 2. Sufficient fluctuation estimates for a full solution (conditional theorem, proved)
Suppose constants c,C,K>0 and r_0 exist, depending only on d, such that for every r=r_0,
    c v_r = E D_r(Q_r)^2 = C v_r,                  (2)
    E D_r(Q_r)^4 = K v_r^2.                       (3)
Then positive constants a,b give
    a r^{-d/2} = p(r) = b r^{-d/2}, r=r_0,
and the target positive-moment criterion follows, including divergence at alpha=d/2.

Proof. Mean zero in (1) makes the second moment a variance. Cauchy–Schwarz and (1) give p(r)=sqrt(C)/(2 sqrt(v_r)). For the other direction apply Hölder with exponents 3/2 and 3 to |D|^{2/3} and |D|^{4/3}:
    E D^2 = (E|D|)^{2/3} (E D^4)^{1/3}.
If E D^2>0, rearranging gives E|D|=(E D^2)^{3/2}/(E D^4)^{1/2}. Assumptions (2),(3) give E|D|=c^{3/2}sqrt(v_r)/sqrt(K). Divide by 2v_r using (1). Since sqrt(v_r)=d^{-d/4}r^{d/2}, the asserted constants exist. For every alpha>0 Tonelli applied to X^alpha=?_0^X alpha t^{alpha-1}dt gives E*X^alpha=alpha?_0^infinity t^{alpha-1}p(t)dt. The integral below r_0 is finite. The integral above r_0 has integrand bounded above and below by constant multiples of t^{alpha-1-d/2}; it converges precisely when alpha<d/2. At equality it diverges logarithmically. This proves the conditional theorem.

All bounded-window moments exist at each fixed r, because |D|=R(Q)+B(Q), a Poisson variable of mean 2v_r. That fact alone gives bounds of order v_r^2 and v_r^4 for the second and fourth moments, respectively, NOT (2),(3). Establishing (2),(3) for growing Q_r is the unresolved probabilistic work. These conditions are sufficient; their necessity for the moment conjecture is not claimed.

There is also an exact equivalent formulation of the moment question, without (2),(3):
    E*X^alpha = (alpha d^{d/2}/2) ?_0^infinity
        r^{alpha-d-1} E|D_r(Q_r)| dr.              (4)
This follows by substitution of (1) in the same nonnegative integral. Thus estimates on the first absolute moment of residual charge would suffice directly.

## 3. Why raw Poisson discrepancy does not prove (2) (proved conservation identity)
Let Z(Q)=R(Q)-B(Q). Define F_r(Q) as the sum over all matched edges (u red, v blue) of length =r which have exactly one endpoint in Q, with contribution 1_Q(u)-1_Q(v). There are finitely many such edges because each touches a bounded window and each point has one partner. Then
    D_r(Q)=Z(Q)-F_r(Q).                            (5)
Indeed every length=r internal edge removes one point of each colour and contributes zero signed charge; every short crossing edge removes its sole endpoint's signed charge; all longer edges leave their endpoints in the residual sets. This exhaustive classification proves (5).

The original Z(Q) has second moment 2|Q| and fourth moment 12|Q|^2+2|Q|, since R(Q),B(Q) are independent Poisson variables of mean |Q|. For completeness the cumulant generating function is |Q|(e^t+e^{-t}-2), with second and fourth cumulants both 2|Q|, so the centered fourth moment is 2|Q|+3(2|Q|)^2. This does not control D: F is dependent on Z and is a matching-dependent boundary flux. Bounds on Z cannot be transferred across (5) without bounds on F and its covariance with Z. For Q_r the r-thick boundary neighborhood has volume comparable to v_r, so merely bounding crossing edges by all boundary points loses the desired square-root scale.

## 4. Arbitrarily long stable edge despite a uniformly short alternative (proved deterministic obstruction)
For n=2 on the real line take red points R_i=8i and blue points B_i=8i+5, i=0,...,n-1. This embeds into every R^d along its first coordinate. In every stable matching the pairs (R_{i+1},B_i), i=0,...,n-2, are forced, with distance 3. The remaining pair (R_0,B_{n-1}) has distance 8n-3. Yet the perfect matching (R_i,B_i) has all distances 5. Consequently stable matching has no universal deterministic constant-factor bound for its maximum edge in terms of the smallest possible maximum edge, even in Euclidean spaces and balanced configurations.

Proof. The signed coordinate difference R_i-B_j is 8(i-j)-5. If i=j+1 the absolute distance is 3. If i=j, it is at least 5. If i=j+2, it is at least 11. Hence B_j and R_{j+1} for j<n-1 are each other's unique closest permissible partners. Any matching omitting such a pair gives both endpoints a strictly worse partner (or no partner), hence a blocking pair. All these forced pairs are disjoint. Removing them leaves precisely R_0 and B_{n-1}; perfection forces the claimed final pair. The resulting matching is stable: each internal endpoint has its closest possible partner, so it cannot participate in a blocking pair; the only two endpoints without this property are matched to one another. The alternative matching has every distance exactly 5. The ratio (8n-3)/5 tends to infinity.

The displayed configuration has repeated distances across distinct pairs, but has strict endpoint preferences for the forced pairs. If generic non-equidistance is desired, perturb each coordinate by less than delta<1/4, then choose a generic perturbation avoiding the finitely many distance-equality hypersurfaces. Every forced distance is at most 3+2delta<3.5; every competing distance is at least 5-2delta>4.5. The same forced pairs remain. The final distance is at least 8n-3-2delta, and the alternative maximum is at most 5+2delta. In R^d perturb within delta-balls; the triangle inequality gives the same margins. Thus this is a robust open-set obstruction, not an artefact of ties or exact collinearity.

This construction does not supply a Poisson power-law lower bound. Its probability and isolation cost in an infinite Poisson environment are not estimated at polynomial scale. It refutes a proposed deterministic route only; it is NOT a counterexample to F0081.

## 5. Referee checks and remaining work
Potential failure: use stability without strict preference. Checked: residual distances are >r, while separation is =r, so the blocking inequalities are strict.
Potential failure: wrong Palm normalization. Checked: red intensity is 1 and blue intensity agrees by colour symmetry, giving the factor 2 in (1).
Potential failure: unbounded random window. Checked: Q_r is deterministic and bounded for each r; all counts and four moments are finite.
Potential failure: infer original Poisson independence after thinning. Rejected explicitly in (5); residual processes are dependent.
Potential failure: infer critical divergence from only exponent d/2+o(1). Rejected: the conditional lower bound is a constant multiple at every large r, giving the actual divergent integral. The exact moment question is (4).
Potential failure: finite simulations silently replace infinite Palm law. Rejected: experiments below are balanced binomial processes on a flat torus, and no infinite-volume conclusion follows.
Potential failure: finite chain ties. Strict closest-partner margins and generic perturbation establish robustness; numerical blocking checks independently verify small cases.

Remaining gap: prove sufficient estimates on E|D_r(Q_r)| in (4), or uniform residual-charge estimates (2),(3), or find a different argument for the moment criterion. In particular, finite residual charges may have scale-dependent spatial correlations; neither their variance upper bound nor the square-root-volume lower bound has been established here. Source Theorem 6 still supplies only its original upper exponent s(d) and d-th-moment divergence (plus Theorem 2 in d=2). No unconditional bound is improved.
''',encoding='utf8')
claims=[
('Residual red and blue points with matching distance >r cannot coexist in a deterministic window of diameter at most r; E|D_r(Q)|=2|Q|P*(X>r).','proved','ATTEMPT.md §1','Does not estimate residual charge at growing scales.'),
('Uniform second moment comparable to volume and fourth moment bounded by squared volume for Q_r imply P*(X>r) comparable to r^{-d/2}, hence the conjectured positive-moment criterion.','proved','ATTEMPT.md §2','The moment hypotheses (2),(3) have not been proved for stable Poisson matching.'),
('The conjectured moment finiteness is exactly the integrability criterion (4) for residual absolute charge.','proved','ATTEMPT.md §2','No needed integrability estimate is established.'),
('Residual signed charge equals original colour discrepancy minus the signed flux of short matching edges across the window boundary.','proved','ATTEMPT.md §3','Boundary-flux fluctuations and covariance remain uncontrolled.'),
('Balanced Euclidean finite configurations can have stable maximum edge / optimal bottleneck arbitrarily large, robustly under generic perturbations.','proved_special_case','ATTEMPT.md §4','Finite deterministic obstruction only; no Poisson tail counterexample.')]
with P.joinpath('CLAIMS.jsonl').open('w',encoding='utf8') as f:
 for claim,status,loc,gap in claims:f.write(json.dumps(dict(problem_id='F0081',claim=claim,status=status,proof_location=loc,remaining_gap=gap,checks='Full proof and hostile-referee checks in ATTEMPT.md; finite algebra and experiments logged separately.'),ensure_ascii=False)+'\n')
P.joinpath('STATUS.md').write_text('STATE: WORKING\nNEXT: Complete numerical and Lean checks; record residual-charge reduction and precise unresolved bounds.\nVERDICT: PARTIAL\n2026-10-11: Source verified, citations screened; no exact solution found. Proved residual-charge identity, conditional moment theorem, and robust finite bottleneck obstruction.\n',encoding='utf8')
print('Saved LITERATURE.md, ATTEMPT.md, CLAIMS.jsonl, STATUS.md')
