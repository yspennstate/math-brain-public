Open problem I0072. Source: A. Agresti and M. Veraar, the survey "Nonlinear SPDEs and maximal regularity" (NoDEA, DOI
10.1007/s00030-025-01090-2; arXiv:2501.18561v5), Problem 8 "Reaction-diffusion with quadratic growth": let O be T^d or R^d and
l >= 2; for the reaction-diffusion system (8.14) with transport noise coefficients (b_{n,i}) in C^gamma(O; l^2), gamma > 0, does
global well-posedness hold under (1) nonnegative data, (2) g_i globally Lipschitz and vanishing on {u_i = 0}, (3) quasi-positivity
f_i(u) >= 0 on {u_i = 0}, (4) mass control sum_j f_j(u) <= K_0 + K_1 sum_j u_j, (5) quadratic growth of the local Lipschitz
constant of f? Then: does it hold with g_i of superlinear growth, and with the optimal growth h = 3/2 in Assumption 8.4(3)?
Plain text of the survey (survey_published.txt, survey_v5.txt) and of Agresti-Germ-Veraar arXiv:2606.07417 (reaction_2026*.txt,
"An optimal local theory for reaction-diffusion equations driven by non-trace-class noise") is in sources/ (copied from an
earlier run; check them yourself). State (8.14), Assumption 8.4, conditions (1)-(5) and every hypothesis (spaces, d, the noise,
boundary conditions) exactly, and what "global well-posedness" means there (solution class, initial-data space).

Do this, in order, saving as you go:
1. Literature first. Read the survey around (8.14), Assumption 8.4, Problems 7 and 8, and the results it cites for the
   mass-controlled and coercive cases (Agresti-Veraar reaction-diffusion with transport noise papers). Read the deterministic
   quadratic theory the problem mirrors: Caputo-Goudon-Vasseur (4-species quadratic, all d), Souplet (2018), Fellner-Morgan-Tang
   (global classical solutions to quadratic systems with mass control, all d), Pierre-Suzuki-Yamada (dissipative quadratic
   systems). Then search for 2025-2026 stochastic work: D. Milesis and M. Salins arXiv:2604.06645 (triangular control of mass),
   Agresti-Germ-Veraar arXiv:2606.07417 every version, and any paper citing the survey's Problem 8 or treating stochastic
   reaction-diffusion with quadratic growth and mass control. Compare hypotheses line by line with Problem 8: noise type
   (transport versus Nemytskii, white or coloured), domain, d, growth of f and g, solution class. If a printed result answers
   Problem 8 (or one of its two follow-up questions) as posed, report RESOLVED_IN_LITERATURE with exact theorem numbers and
   pages; if it answers only part, say exactly which part.
2. Otherwise attack the gap. The deterministic routes are the improved duality estimate (L^{2+eps} from mass control) and the
   De Giorgi / L^p-energy bootstrap of Caputo-Goudon-Vasseur and Fellner-Morgan-Tang; run one of them inside the stochastic
   maximal regularity framework and the blow-up criteria of the survey (Theorem 5.1 and its variants), with the transport-noise
   Ito correction absorbed by the parabolicity condition and the g_i term handled by its Lipschitz bound. A complete answer under
   the source's hypotheses is PROVED; a proof under one extra natural hypothesis (d <= some bound, a restriction on b or g) not
   already in print is PARTIAL with substance; blow-up with positive probability is COUNTEREXAMPLE. Check every step and every
   exponent, in particular that the duality estimate survives the stochastic integral (moments, stopping times, the sign of the
   Ito correction).
3. Compute only if a numerical check makes sense. No simulation stands in for a proof.
Write REPORT.md. Its first line is exactly one of PROVED, COUNTEREXAMPLE, PARTIAL, NO_PROGRESS, RESOLVED_IN_LITERATURE.
Then the statement, the proof, what was checked and how, and the literature results with exact theorem numbers and pages.
Keep LOG.md as you go. Code in code/, data in data/. Source texts may go in sources/ as plain text only; no PDFs kept, no
page images or scans of any paper or book anywhere in this folder. Work only in this directory. At most 4 threads, under
4 GB, nice 10. No publication anywhere, no pushes.
