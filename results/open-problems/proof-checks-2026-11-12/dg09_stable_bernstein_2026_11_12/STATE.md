# DG09 state

12 Nov 2026. Checked at outline level; note DG09_CHECK.md, test dg09_check.py, output dg09_check.out.

Result: claimed solved by one 85-page computer-assisted preprint (Hong, Li, Wang, arXiv 2609.15720);
Section 13 and its constants verified; the rest unread; no independent confirmation found.

On disk under lit/ (the PDF and text are not pushed): 2609.15720/paper_c.txt (3,511 lines);
repo_listing/tree.json and README.md of github.com/wgaom/stable-bernstein-R7 at commit
619b75d41555b1eafdb0db03439cdb15af82d9c5.

Next step if someone goes further: build the Lean folder of that repository on a Mac mini (inspect
lakefile and lake-manifest first; it needs elan and the mathlib cache), confirm
R7.Paper.scalar_bound and R7.Paper.spectral_bound and their axiom lists, then compare
lean/R7/Definitions.lean with Appendices A to C of the paper. After that, Sections 11 to 14 (critical
energies and rigidity) are the shortest route through the geometry.
