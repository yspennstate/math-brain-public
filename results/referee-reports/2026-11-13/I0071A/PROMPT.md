Open problem I0071. Source: A. Agresti and M. Veraar, the survey "Nonlinear SPDEs and maximal regularity" (NoDEA, DOI
10.1007/s00030-025-01090-2; arXiv:2501.18561v5), Problem 7 "Reaction-diffusion with triangular structure" (published p. 131):
let O be T^d or R^d and l >= 2; for the reaction-diffusion system (8.14) with transport noise coefficients (b_{n,i}) in
C^gamma(O; l^2), does global well-posedness hold under conditions (1)-(6) (nonnegative data, quasi-positivity, polynomial growth
of order h, mass control, triangular control Rf(y) <= [1 + sum y_i]^r with R lower triangular invertible, nonnegative)? Plain text
of the survey (survey_published.txt, survey_v5.txt) and of Agresti-Germ-Veraar arXiv:2606.07417 is in sources/ (copied from an
earlier run; check them yourself). State (8.14), conditions (1)-(6) and every hypothesis (spaces, h, r, d, the noise, boundary
conditions) exactly, and what "global well-posedness" means there (which solution class, which initial-data space).

Do this, in order, saving as you go:
1. Literature first. Read the survey around (8.14) and Problem 7, and the results it cites for the coercive and the
   mass-controlled cases (Agresti-Veraar, reaction-diffusion with transport noise papers; their Brusselator/Lotka-Volterra
   results). Then get and read D. Milesis and M. Salins, "Global in time solutions to stochastic reaction-diffusion systems with
   superlinear reactions satisfying a triangular control of mass", arXiv:2604.06645 (2026), every version; and search for any
   2025-2026 paper citing the survey's Problem 7 or the deterministic triangular theory (Pierre; Fellner-Morgan-Tang; Morgan;
   Souplet) in the stochastic setting. Compare hypotheses line by line with Problem 7: noise type (transport versus additive or
   multiplicative Nemytskii, space-time white or coloured), domain, dimension, h and r, solution class. If a printed result answers
   Problem 7 as posed, report RESOLVED_IN_LITERATURE with exact theorem numbers and pages. If it answers only part (other noise,
   restricted d, h or r), say exactly which part.
2. Otherwise attack the gap that remains. The natural route is the deterministic duality / L^p-energy bootstrap along the
   triangular structure (estimate u_1, then u_1 + u_2, ... in L^p for growing p), run inside the stochastic maximal regularity
   framework and the blow-up criteria of the survey (Theorem 5.1 and its variants), with transport noise contributing an
   It\^o correction absorbed by the parabolicity condition. A complete answer under the source's hypotheses is PROVED; a proof under
   one extra natural hypothesis (d <= 3, r < some bound, h small, a restriction on b) that is not already in print is PARTIAL with
   substance. A counterexample (blow-up with positive probability) is COUNTEREXAMPLE. Check every step and every exponent.
3. Compute only if a numerical check makes sense. No simulation stands in for a proof.
Write REPORT.md. Its first line is exactly one of PROVED, COUNTEREXAMPLE, PARTIAL, NO_PROGRESS, RESOLVED_IN_LITERATURE.
Then the statement, the proof, what was checked and how, and the literature results with exact theorem numbers and pages.
Keep LOG.md as you go. Code in code/, data in data/. Source texts may go in sources/ as plain text only; no PDFs kept, no
page images or scans of any paper or book anywhere in this folder. Work only in this directory. At most 4 threads, under
4 GB, nice 10. No publication anywhere, no pushes.
