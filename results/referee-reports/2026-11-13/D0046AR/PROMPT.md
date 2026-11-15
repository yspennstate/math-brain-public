You are an independent referee. Claim under review (files in claim_files/: REPORT.md, LOG.md, code/, data/ of another run):
open problem D0046, Question 8 (Dynamics) of B. Virag, "Operator limits of random matrices" (arXiv:1804.06953, PDF p. 25): are
there operator limits of matrix-valued (Hermitian) Brownian motion? The claim is PARTIAL. It proves that an explicit stationary,
reversible, continuous Markov process on tridiagonal matrices with exactly the GUE one-time law has a CONSTANT edge process in its
scaling limit on the Dyson Brownian motion clock (uniformly on compact time intervals in mean square, for each fixed number of top
eigenvalues), so it cannot produce the Airy line ensemble; it says the proof extends to reversible tridiagonal diffusions whose
entry covariance matrices are uniformly bounded. It also states that canonical Lanczos tridiagonalization of invariant Hermitian
Brownian motion is Markov on the cyclic locus as an orbit quotient.

Break it if it is wrong.
1. Get arXiv:1804.06953 into sources/ as plain text and state Question 8 exactly. Check the claim does not overstate what it
   rules out.
2. Check the obstruction theorem line by line: the construction of the process, its stationarity and GUE marginal, the time
   normalisation (what "DBM clock" means for the edge: edge eigenvalues of DBM move on time scale n^{-1/3} in the right units -
   check the scales), and the mean-square estimate showing the top eigenvalues do not move on that scale. Then check the claimed
   extension to all reversible tridiagonal diffusions with uniformly bounded entry covariances: is it really proved, or only
   asserted?
3. Check the Markov-quotient statement for Lanczos tridiagonalization (orbit argument, cyclic locus, measurability).
4. Write your own independent code (do not reuse claim_files/code) simulating the claimed tridiagonal process for n up to a few
   thousand and showing the edge eigenvalue increments over DBM-edge time are negligible, against matrix Hermitian Brownian motion
   where they are not.
5. Literature: Allez-Guionnet, Holcomb-Paquette ("Tridiagonal models for Dyson Brownian motion"), Edelman-Dumitriu, Corwin-Hammond
   (Airy line ensemble), Landon-Sosoe-Yau, recent work 2018-2026 on "dynamical stochastic Airy operator", "operator limit of Dyson
   Brownian motion". Is Question 8 answered in print, positively or negatively?
6. Verdict on value: correct or not, novel or not, exactly what is proved.
Write REPORT.md. Its first line is exactly one of ACCEPT, MINOR, MAJOR, WRONG. Then: summary verdict, a numbered list of every
error or gap with location and fix, what you verified and how, and the literature result. Keep LOG.md as you go. Source texts
may go in sources/ as plain text only; no PDFs kept, no page images or scans anywhere in this folder. Work only in this
directory. At most 4 threads, under 4 GB, nice 10. No publication anywhere, no pushes.
