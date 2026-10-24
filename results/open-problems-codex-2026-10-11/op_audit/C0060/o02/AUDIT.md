VERDICT: PASS (correct and complete)

# Independent audit of C0060

Date: 2026-10-11. Verdict audited: SOLVED_IN_LITERATURE.

## Exact claim and scope

ATTEMPT.md lines 7?11 and CLAIMS.jsonl claim that, for the infinite discrete skeleton S of the Sierpinski gasket with natural unit edge conductances, random interlacements on the nearest-neighbor Cartesian product S ? Z have vacant-set threshold u_* > 0. The threshold is defined by the vanishing probability of existence of an infinite vacant connected component. This answers the stated problem, with the correct infinite graph and model; it does not substitute a finite gasket cylinder, a Sierpinski carpet, or Gaussian free field percolation.

I read STATUS.md, ATTEMPT.md, CLAIMS.jsonl and LITERATURE.md directly from the claimant's folder without changing them. All downloaded evidence and this report are inside the audit folder.

## Independent primary-source verification

I independently fetched and extracted the complete PDFs using Python urllib and PyMuPDF:

- Original book: https://www.mi.uni-koeln.de/~drewitz/SpringerRI.pdf (saved as source.pdf and source.txt). PDF page 81 states the exact gasket-product positivity question and points to Sznitman's Remark 5.6(2). This verifies ATTEMPT.md line 11.
- Resolving paper: https://arxiv.org/pdf/1811.05970v3 (saved as geometry.pdf and geometry.txt). Its title and authors match Drewitz?Pr?vost?Rodriguez, Geometry of Gaussian free field sign clusters and random interlacements. The fetched PDF identifies itself as v3, 19 May 2024.
- Earlier paper: https://arxiv.org/pdf/1010.1490 (saved as sznitman.pdf and sznitman.txt). Remark 5.6(2), printed page 42 / PDF page 44, explicitly singles out the gasket with natural weights. Theorem 5.1 requires the additional exponent restriction ? ? 1 for positivity; it does not already settle this case.

In the resolving paper, equation (1.4), printed page 2 / PDF page 3, explicitly lists G2 = G? ? Z with G? the discrete skeleton of the Sierpinski gasket. The list is endowed with unit weights.

Theorem 1.2, printed page 6 / PDF page 7, assumes (p0), (V_alpha), (G_beta) and (WSI). It asserts a constant tilde u > 0 and, for every u in (0, tilde u], a coupling of I, V, K such that I and V have the interlacement and vacant-set marginals respectively, K is independent of I, and almost surely I intersect K contains an infinite cluster and is contained in V. The theorem explicitly concludes u_* ? tilde u > 0. This matches ATTEMPT.md lines 17?21 exactly.

Corollary 3.9, printed page 27 / PDF page 28, verifies all four hypotheses for the unit-weight graphs of (1.4), with a suitable metric, and explicitly states that Theorems 1.1 and 1.2 apply. Its gasket-product paragraph invokes Propositions 3.5 and 3.7 and verifies (WSI), as well as the volume and Green estimates. Thus ATTEMPT.md line 23 does not leave a geometric hypothesis unchecked. The discussion immediately following Theorem 1.2 also explicitly identifies the gasket and says that this resolves the earlier Remark 5.6(2).

## Check of the application and quantifiers

ATTEMPT.md line 25 is valid. For each fixed u in (0, tilde u], an infinite connected subset of I intersect K is also a connected subset of V. The vacant connected component containing it must be infinite. Passing to the vacant-set marginal gives probability one of vacant percolation at that level. At u = 0 the entire infinite connected graph is vacant. Consequently the zero-percolation set in the definition of u_* is disjoint from [0, tilde u], and its infimum is at least tilde u. Separate couplings for different u suffice; no simultaneous coupling over all levels is needed.

There is no contradiction in coupling I intersect K into V: the auxiliary I need not be the complement of the coupled V. The claimant correctly identifies this at line 34. Independence of K and I is a published property, but is unnecessary for this final inference.

I independently checked the exponent computation at line 33. With the metric of Proposition 3.5, the product has alpha = log(45)/(2 log(2)) ? 2.7459265482 and beta = log(5)/log(2) ? 2.3219280949. Their difference equals log(9/5)/(2 log(2)) ? 0.4239984533, strictly between zero and one. The factor's volume exponent is instead log(3)/log(2) ? 1.5849625007, and its walk exponent satisfies 2 ? beta < 1 + log(3)/log(2). These values agree with the corollary and explain why the older ? ? 1 result did not apply. They impose no obstruction in the newer theorem.

## Bibliography and renewed search

I fetched https://api.crossref.org/works/10.1007/s00440-024-01285-1 (crossref.json). Crossref confirms the title, all three authors, PTRF volume 192, pages 625?720, online publication 15 June 2024, and print publication June 2025. ATTEMPT.md lines 15 and 36 are accurate.

A fresh arXiv API search for the quoted phrase ?random interlacements? and ?Sierpinski? returned Windisch's 2009 cylinder-limit paper, not the resolving paper; this narrow abstract search cannot establish openness. I separately fetched the arXiv record for 1811.05970 (paper_record.xml); its abstract explicitly asserts vacant percolation at small intensities and resolution of the open problem in arXiv:1010.1490. The full theorem and exact-graph corollary, rather than a negative search or the abstract alone, establish the resolution.

## Issues and limits

No mathematical, hypothesis, quantifier, model, or bibliographic issue was found in ATTEMPT.md. No fix is required. Line 38's reference to a previous ?status-first instruction? is task-history commentary and supplies no evidence; the result is independently supported by the sources above.

What is verified: an existing published theorem settles the exact positivity question, and the claimant's full deduction from that theorem is correct. This audit does not claim a new proof, a numerical value for u_*, or an independent re-proof of the resolving paper's entire multisection argument. None of these is needed for the SOLVED_IN_LITERATURE verdict.
