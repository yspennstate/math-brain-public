VERDICT: PASS

# Independent audit of D0019

The verdict SOLVED_IN_LITERATURE is correct for the source's intended question: a two-parameter, d-dimensional Brownian sheet with d in {2,3}, its zero set at strictly positive parameters, and orthogonal projections onto lines. Almost surely, every such projection has Hausdorff dimension 2-d/2, simultaneously. Thus a direction chosen randomly from the sheet cannot be exceptional. No original solution by the claimant is asserted or certified.

## Exact claim and quantifiers

ATTEMPT.md lines 5-7 and CLAIMS.jsonl entry 1 claim that, for Z = { (s,t) in (0,infinity)^2 : B(s,t)=0 }, there is one probability-one event on which every orthogonal line projection preserves dim_H Z = 2-d/2. ATTEMPT.md line 19 and CLAIMS.jsonl entry 2 then specialize this simultaneous conclusion to any sheet-dependent random line. These claims answer the random-projection question, rather than merely proving a fixed-direction special case.

## Independently fetched evidence

I read STATUS.md, ATTEMPT.md, CLAIMS.jsonl and LITERATURE.md from the claimant's directory without changing them. I independently downloaded the following through Python urllib, without using built-in web search:

- https://arxiv.org/pdf/math/0510518, saved here as source.pdf and extracted as source.txt.
- https://arxiv.org/pdf/2405.20019v2, saved here as resolver.pdf and extracted as resolver.txt.
- https://api.crossref.org/works/10.1007/s10959-024-01399-1, saved as crossref.json.
- A fresh arXiv API search for Brownian sheet and projection or Marstrand, saved as arxiv_search.xml.

All four requests succeeded with HTTP 200; URLs and byte counts are in fetch_log.json. PDF text was extracted using PyMuPDF.

Keming Chen and Guillaume Woessner, Zeros of the Brownian Sheet, arXiv:2405.20019v2 (31 May 2024), page 2, states:

?Theorem 1.2 (Open problem). For N = 2 and d = 2 or 3, almost surely, for any non-zero linear map p : R^2 -> R, dim_H[p(Z)] = dim_H(Z).?

The preceding sentence expressly says this answers Open Problem 4. The following paragraph expressly distinguishes the simultaneous almost-sure statement from a family of fixed-map almost-sure statements. Proposition 1.1 on the same page gives dim_H Z = (N-d/2)^+ almost surely. These verify the inputs in ATTEMPT.md line 13 exactly, including the crucial order of quantifiers.

The full paper contains Section 2, ?Proof of Theorem 1.2,? pages 4-7. Page 7, Step 3, explicitly addresses uniformity over angles; the theorem is not merely an abstract announcement. Crossref independently identifies the same authors and title, Journal of Theoretical Probability 38 (2025), article 33, publication date 6 February 2025, DOI 10.1007/s10959-024-01399-1. I verified the theorem in the arXiv version, not in a journal PDF.

The fresh arXiv search returned this direct resolver and Boundary Non-Crossings of Additive Wiener Fields. The latter concerns an RKHS projection, not projections of this zero set, and supplies no competing resolution. This was a bounded search, not an exhaustive literature review.

## Hypothesis and deduction checks

1. ATTEMPT.md lines 5, 23-24: the covariance in the source, page 2 equation (1.1), agrees with the covariance and independent-coordinate construction on resolver page 1. There is no switch to fractional Brownian motion, a different number of parameters, or a different random set.

2. ATTEMPT.md line 9: source page 34, Section 8.3, asks exactly whether a random orthogonal projection can have dimension different from 2-d/2. It does not repeat a restriction on d. Source page 3, equation (1.7) and the ensuing discussion, singles out d=2,3 for equality of the zero-set and line-image dimensions; Remarks 1.3 call these the only interesting dimensions. Thus the claimant's restriction follows the intended context. A claim for d=1 with target 3/2 would be false because a subset of a line has dimension at most 1; the claimant explicitly does not make that claim.

3. ATTEMPT.md lines 9, 23: the positive-parameter convention is essential, not cosmetic. Including the deterministic axes changes the d=3 zero-set dimension to at least 1. Source equation (1.3) and its slice results concern positive times. Resolver page 4 localizes to [1,2]^2 and then [a,b]^2 with 0<a<b. Its notation R_+ is not explicitly disambiguated at the definition, but its dimension formula and localization concern the interior zero set. The claimant states this necessary convention openly; no gap in the intended application results.

4. ATTEMPT.md lines 15-17: independently, for a unit vector u spanning L, p_u(x)=<x,u> is a nonzero linear functional, J_u(r)=ru satisfies |J_u(r)-J_u(s)|=|r-s|, and P_L(x)=J_u(p_u(x)). Therefore dim_H P_L(Z)=dim_H p_u(Z). Intersecting the two probability-one events supplied by the cited theorem and proposition gives exactly 1 when d=2 and 1/2 when d=3. This deduction needs no numerical approximation.

5. ATTEMPT.md line 19: for each outcome in that common event, the identity holds for every line. Substituting L=L(omega) is therefore legitimate even with dependence on the sheet. There is no uncountable intersection of separately obtained fixed-direction events. Projection onto an affine line differs by translation, which also preserves dimension.

## Issues and limits

No correctness or completeness issue requiring a fix was found in the claimant's application. The dimension restriction and exclusion of the axes are material interpretation points, both already addressed at ATTEMPT.md line 9; the PASS applies to the source's intended formulation, not an unrestricted literal variant.

ATTEMPT.md lines 31 and 35 correctly limit the claim to an application of published results. This audit verifies those results' actual statements, their exact applicability, the presence of their proof, and the complete application argument. It does not certify every estimate in Chen-Woessner's proof independently, nor provide a new proof or formalization. The SOLVED_IN_LITERATURE branch does not require such a reconstruction. The simultaneous projection-preservation result is a stated literature theorem, not a conjecture or an unsupported claimant sketch.
