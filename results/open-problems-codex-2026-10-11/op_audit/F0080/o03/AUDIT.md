VERDICT: PASS (correct and complete)

# Independent audit of F0080

Audit date: 2026-10-11. Verdict reviewed: SOLVED_IN_LITERATURE.

## Exact claim and quantifiers

ATTEMPT.md lines 15?39 and CLAIMS.jsonl claim 1 assert that for EVERY finitely generated nonamenable group ?, the expected degree ?_FMSF(?,S) is unbounded as S ranges over ordinary finite symmetric generating sets. Consequently two Cayley graphs of the SAME group have different expected degrees. Lines 43?45 and claims 2?3 assert that the expected degree is instead independent of the generating set for infinite amenable groups (value 2) and finite groups of order N (value 2?2/N).

This answers Question 6.13 as stated, rather than merely producing a multigraph variant or a statement about different groups. It also gives the amenable/nonamenable distinction: dependence is not asserted for every finitely generated group. The question concerns FMSF, not the uniform forest FSF or merely whether FMSF differs from WMSF.

## Primary-source verification

I independently downloaded the following PDFs directly from arXiv using Python urllib; I did not rely on the claimant's saved PDFs or extracted text:

- https://arxiv.org/pdf/math/0412263 (downloaded version math/0412263v5): PDF page 27 contains Question 6.13 with the statement reproduced in ATTEMPT.md lines 7?11. PDF page 18, proof of Corollary 3.24, explicitly states that in the amenable case the forests in question have expected degree 2. Proposition 3.5(c), page 9, and Theorem 3.12, pages 11?12, also support that conclusion for infinite amenable Cayley graphs.
- https://arxiv.org/pdf/1306.0303 (v1): Theorem 1, pages 2?3, states exactly 1/(4?)?1/4 ? ?_FMSF(G) ? d. Corollary 2, page 3, states unboundedness over generating MULTISETS. The following paragraph expressly identifies Question 6.13. This paper alone would leave the ordinary-set scope concern described in ATTEMPT.md line 21.
- https://arxiv.org/pdf/1306.1767 (v1): Theorem 1, page 2, explicitly supplies arbitrarily small spectral radius for finite symmetric generating SETS of every finitely generated nonamenable group. Corollary 9, page 5, explicitly states that expected FMSF degree is unbounded over these generating sets and hence depends on S. This is precisely the needed result, with no non-torsion, free-subgroup, or restricted class of nonamenable groups hypothesis.

Independent Crossref DOI requests confirmed the identities and publications of both Thom papers: Combinatorica 36(5), 591?600, DOI 10.1007/s00493-014-3160-x; and International Mathematics Research Notices, DOI 10.1093/imrn/rnu018. The latter response supplies online publication on 2014-03-02 but no volume or pagination; the claimant correctly avoids inventing them.

A fresh arXiv API search for minimal spanning forests and degree returned Thom's resolving paper and the LPS source. A fresh OpenAlex search returned HTTP 429; no successful OpenAlex search is claimed in this audit. These requests and their outcomes are preserved in independent_fetch_log.json and the corresponding response files. The literature-resolution conclusion rests on directly read primary theorems, not search snippets.

## Checks of the deduction and boundary cases

ATTEMPT.md lines 29?35: Correct. The subgraph bound gives ?(S0) ? d0. For ? < 1/(4d0+1), ?(S) < ? implies 1/(4?(S))?1/4 > d0. Thus the cited lower bound produces a strictly different expected degree, not just a potentially different value. The same reasoning works for every real target M > 0. I re-derived the inequality and checked exact rational instances d0=1,4,10,100 with ?=1/(4d0+2); the resulting lower bounds were respectively 5/4,17/4,41/4,401/4.

Lines 15?19 and 50: I also checked the relevant lower-bound proof in Thom. Conditional on a nonloop edge label t, the union bound over alternative simple paths gives a deletion probability at most ?_{n?2}(?dt)^{n?1}. Integrating the resulting survival lower bound on [0,1/(2?d)] gives (1?log 2)/(?d) ? 1/(4?d). The endpoint is within [0,1] since a graph with a nonloop edge has ?d ? 1. The loop allowance yields the stated ?1/4 correction. No independence of different cycle events is required. Numerical evaluation gives 1?log 2 = 0.3068528194 > 1/4.

Line 37: Correct removal of a possible identity generator. For the self-adjoint walk operator A with nonnegative matrix entries, |?Af,f?| ? ?A|f|,|f|?, so the top of its spectrum equals its norm. It follows that ||pI+(1?p)A|| = p+(1?p)||A||. Since ||A|| ? 1, removing the identity cannot increase spectral radius. The remaining symmetric set still generates the nonamenable group, and gives an ordinary loopless simple Cayley graph. Corollary 9 independently supplies the set conclusion anyway.

Line 39: Correct example in existence form. The standard Cayley graph of F2 is a 4-regular tree; its FMSF contains every edge and has degree 4. Choosing spectral radius below 1/17 forces expected degree greater than 4. An explicit second generating set is not claimed or needed.

Line 43: Correct with the stated infinite-group qualification; the cited amenable conclusion applies to Cayley graphs, which are transitive and unimodular.

Line 45: Correct independently of the cited infinite-graph results. Almost surely all labels on the finite graph are distinct. The finite-cycle rule gives an acyclic connected subgraph: if disconnected, a least-label edge across a component cut cannot have a lower-label alternative path, since any such path must cross the cut again. Thus it is a spanning tree with N?1 edges. Label-law invariance under Cayley translations makes all vertex expectations equal, and the degree sum gives 2(N?1)/N, including 0 at N=1.

## Issues and limits

No mathematical or scope issue requiring a fix was found in ATTEMPT.md. In particular, its explicit use of the second primary paper closes the otherwise substantive multiset/set gap.

What is established is the published answer to Question 6.13, including dependence for every finitely generated nonamenable group and invariance in the amenable cases. This audit does not establish a new theorem, give explicit numerical expected degrees for the new generating sets, or settle connectivity or the number of FMSF components. The deep spectral-radius input is verified as a published theorem and directly matching corollary; it is not represented here as a newly formalized proof of the entire paper.
