You are an independent referee. Claim under review (files in claim_files/: REPORT.md, LOG.md, code/, data/ of another run):
open problem D0025, Problem 4 of T. Seppalainen, "Recent results and open problems on the hydrodynamics of disordered asymmetric
exclusion and zero-range processes" (arXiv:math/9906194, Section 4, p. 9): for the site-disordered totally asymmetric K-exclusion
process (generator (3.1), p. 8: a particle leaves site i at rate alpha_i when eta_i > 0 and eta_{i+1} < K; alpha_i i.i.d. on [r,1],
essential infimum r > 0), does the flux f_K(rho) have a flat segment around rho = K/2? The claim is PROVED. It says K = 1 is already
Theorem 1 of A. Sly, "Note on the flux for TASEP with general disorder" (arXiv:1609.06589), and proves for every finite K and every
nonconstant law: f_K(rho) = r M_K whenever |rho - K/2| <= mu r M_K, where M_K = max of the homogeneous rate-one K-exclusion flux and
mu = 1/r - E[1/alpha_0], by extending Sly's comparison to the finite-K growth (last-passage) graph.

Break it if it is wrong.
1. Get arXiv:math/9906194 and arXiv:1609.06589 into sources/ as plain text. State Problem 4 and Sly's Theorem 1 exactly. Check that
   the claim's model (rate per departure site, independent of the number of particles) is the one in the source.
2. Check Sly's K = 1 argument and then the finite-K extension line by line. Where does K = 1 structure get used in Sly's proof
   (exponential last-passage, symmetry rho <-> 1 - rho, the explicit 1/4)? For K > 1: is the homogeneous K-exclusion flux symmetric
   about K/2 with its maximum there, is the growth-graph / last-passage representation (Seppalainen's K-exclusion hydrodynamics,
   variational coupling) valid with site rates, and does the comparison giving the upper bound f_K <= r M_K and the lower bound on
   the flat interval really go through? Is the width mu r M_K derived, or only asserted by analogy?
3. Check that the concavity of f_K and the hydrodynamic limit used (Seppalainen Theorem 3, pp. 8-9) give exactly the flux the question
   asks about.
4. Write your own independent code (do not reuse claim_files/code): continuous-time site-disordered K-exclusion on rings (K = 1 and
   K = 2, n of order 10^4, a two-point rate law such as P(alpha = 0.5) = 0.1, else 1), measure current against density and compare
   the plateau level and width with r M_K and mu r M_K (estimate M_2 from a homogeneous K = 2 run).
5. Literature: is the finite-K site-disorder plateau already in print (Sly; Bahadoran-Bodineau; Bahadoran-Mountford-Ravishankar-Saada;
   Seppalainen; Basu-Sidoravicius-Sly; 2016-2026 papers citing Sly's note)? Is Sly's note published?
6. Verdict on value: correct or not, novel or not, exactly what is proved.
Write REPORT.md. Its first line is exactly one of ACCEPT, MINOR, MAJOR, WRONG. Then: summary verdict, a numbered list of every
error or gap with location and fix, what you verified and how, and the literature result. Keep LOG.md as you go. Source texts
may go in sources/ as plain text only; no PDFs kept, no page images or scans anywhere in this folder. Work only in this
directory. At most 4 threads, under 4 GB, nice 10. No publication anywhere, no pushes.
