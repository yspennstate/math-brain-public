Open problem C0097. Source: R. Bauerschmidt, H. Duminil-Copin, J. Goodman, G. Slade, "Lectures on self-avoiding walks"
(Clay Math. Proc. 15, 2012), arXiv:1206.2092, Section 1.5, pp. 4-5: the connective constant mu(d) of Z^d has an asymptotic
expansion in powers of 1/(2d), known to order 11 (Hara-Slade; Clisby-Liang-Slade), whose coefficients grow rapidly; prove
that the expansion has radius of convergence zero (expected but unproved). Read the source for the exact statement.

Do this, in order, saving as you go:
1. Literature first. Read arXiv:1206.2092 Section 1.5 and find: Hara-Slade (1995) "The self-avoiding-walk and percolation
   critical points in high dimensions"; Clisby, Liang, Slade (2007) "Self-avoiding walk enumeration via the lace expansion"
   (the 1/d coefficients to order 11 and their growth); Graham's Borel summability work (B. Graham, "Borel-type bounds for
   the self-avoiding walk connective constant", J. Phys. A 2010, arXiv:0911.5163) and any 2010-2026 result on the nature of
   the 1/d series (Borel summability, factorial growth bounds, non-analyticity at d = infinity, analogous divergence for
   percolation p_c(d) or lattice trees). If divergence is proved in print, give the exact reference and theorem and stop
   with REPORT.md first line RESOLVED_IN_LITERATURE. Graham proved Borel-type upper bounds on the coefficients; say exactly
   what is and is not known (upper bounds on growth do not prove divergence; a lower bound on infinitely many
   coefficients of the form |a_n| >= c^n n! or anything super-geometric would).
2. Attack. Divergence needs a lower bound on the coefficients, or an argument that a convergent expansion would force
   analyticity of mu in 1/d on a disc, contradicting some property (e.g. behaviour of mu(d) for d continued to small or
   complex values, a natural boundary, or the known low-dimensional values mu(1)=1, mu(2)~2.638). Consider whether any
   rigorous statement of that kind is within reach, or prove a weaker theorem: e.g. divergence of the analogous 1/d series
   for a simpler model (memory-tau walks, the bubble diagram, the simple random walk return probability expansion, lattice
   trees or animals), or a rigorous super-geometric lower bound for a family of coefficients of a related lace-expansion
   quantity. Be honest about what is proved.
3. Compute. Reproduce the known coefficients from the literature (do not recompute the lace expansion unless cheap) and
   analyse their growth (ratio tests, Borel transform), only as evidence.
Write REPORT.md. Its first line is exactly one of PROVED, COUNTEREXAMPLE, PARTIAL, NO_PROGRESS, RESOLVED_IN_LITERATURE.
Then the statement, the proof, what was checked and how, and the literature result with exact theorem numbers and pages.
Keep LOG.md as you go. Code in code/, data in data/. Source texts may go in sources/ as plain text only; no PDFs kept, no
page images or scans of any paper or book anywhere in this folder. Work only in this directory. At most 4 threads, under
4 GB, nice 10. No publication anywhere, no pushes.
