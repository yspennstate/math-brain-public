You are an independent referee. Claim under review (files in claim_files/: REPORT.md, LOG.md, code/, data/ of another run):
open problem D0036, Question 8 of R. C. Bradley, "Basic properties of strong mixing conditions. A survey and some open
questions" (Probability Surveys 2 (2005) 107-144, arXiv:math/0511078), end of Section 6.5, journal p. 132: for a weakly stationary
second-order sequence, find a condition on the spectral density equivalent to rho*(n) -> 0 alone (Theorem 6.5 covers
rho*(1) < 1 together with rho*(n) -> 0). The claim (PARTIAL) asserts: (1) f = |P|^2 g with P a polynomial and g continuous with
min g > 0 is sufficient, with r*_g(n) <= E_{n-1}(g)/min g and an explicit bound for the interlaced coefficients; (2) in the class
of continuous densities positive except at finitely many points with two-sided asymptotics f ~ c_j |t|^{beta_j}, rho*(n) -> 0
iff every beta_j is an even integer; (3) f = (pi/4)|1 - e^{it}| is continuous, positive a.e., has summable covariances, and
rho*(n) >= 1/2 for all n; (4) the differenced white noise has rho*(1) = 1 and rho*(n) = 0 for n >= 2. It says unrestricted
necessity of (1) is open.

Break it if it is wrong.
1. Get arXiv:math/0511078 into sources/ as plain text. State Theorems 6.2-6.5 and Question 8 exactly, and check the claim's
   definitions of rho* (interlaced index sets, linear spans, complex conjugation) against the survey.
2. Check (1) line by line: the lemma r*_g(n) <= E_{n-1}(g)/min g, the passage from g to |P|^2 g (how the polynomial factor is
   absorbed when the index sets interlace), and the claimed explicit bound.
3. Check (2) in full, both directions: the odd or non-integer exponent case must give rho*(n) bounded away from 0 for every n
   (find the test arrays), and the even case must reduce to (1). Look for gaps at boundary cases (several zeros, exponents
   near an even integer, continuity of g at the zeros after division).
4. Check (3) with your own computation of the lower bound 1/2, and (4).
5. Literature: is Question 8 answered in print (Bradley's later papers and the three volumes "Introduction to Strong Mixing
   Conditions", Peller's Hankel operators book and papers on rho*-mixing, Kolmogorov-Rozanov, Ibragimov-Rozanov,
   Helson-Sarason, Sarason, Peligrad, Miller, 1992-2026)? Are (2) or (3) already printed? Say exactly what remains open.
6. Write your own independent code (do not reuse claim_files/code): estimate rho*(n) on finite windows for the densities in (2)
   and (3) (generalized eigenvalue problems on Toeplitz blocks over interlaced index sets), for several exponents, as evidence.
7. Verdict on value: correct or not, novel or not, and exactly what statement is proved.
Write REPORT.md. Its first line is exactly one of ACCEPT, MINOR, MAJOR, WRONG. Then: summary verdict, a numbered list of every
error or gap with location and fix, what you verified and how, and the literature result. Keep LOG.md as you go. Source texts
may go in sources/ as plain text only; no PDFs kept, no page images or scans anywhere in this folder. Work only in this
directory. At most 4 threads, under 4 GB, nice 10. No publication anywhere, no pushes.
