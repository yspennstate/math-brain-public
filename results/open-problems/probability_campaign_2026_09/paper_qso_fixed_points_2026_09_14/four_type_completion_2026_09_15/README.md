# Four-type strictly non-Volterra QSO paper

Author: Yitzchak Shmalo. Prepared 15 September 2026.

`QSO_four_types.pdf` is the full manuscript. `QSO_four_types.tex` is its standalone LaTeX source. Build with `pdflatex QSO_four_types.tex` twice. The manuscript includes complete proofs of uniqueness, averaged contraction, stability, local analytic dependence, continuous dynamics, and exact polynomial-bit-complexity approximation.

Run `python3 qso_exact_solver.py` to reproduce `example_results.json`. The implementation uses exact integers and fractions only. Its residual is checked independently by direct Fraction evaluation in the example runner. The code illustrates and applies the mathematical theorem; it is not a formal verification of the general theorem.

## Acknowledgement source and scope

The latest ResearchGate DOI-assignment notice found is dated 14 September 2026, for *The Sharp Diameter Threshold for Unimodality of Free Brownian Motion*, DOI 10.13140/RG.2.2.29198.32327, publication 414295277. ResearchGate blocked this session's browser with an unusual-network-activity restriction. Its corresponding manuscript was read from the author's GitHub source at `probability_campaign_2026_09/paper_free_unimodality_2026_09_14/free_unimodality_sharp.tex`. Thus the acknowledgement was adapted from that identified paper's archived source; byte identity with the currently posted ResearchGate PDF was not verified.

The declaration preserves the author's explicit distinction between directing/releasing the research and personally carrying out its mathematics, coding, or writing. It lists the actual contributions relevant to this paper and does not import unrelated model claims, funding claims, formal-verification claims, or human-review claims from the other manuscript.

## Mathematical scope and prior work

Every nonnegative four-type coefficient tensor satisfying parent symmetry, stochasticity and strict parental exclusion has a unique simplex fixed point. Allowed coefficients may vanish. This addresses the four-type uniqueness clause of Ganikhodzhaev--Rozikov (2009), Problem 11. It does not claim the entire multi-clause source problem has been solved. Jamilov (2016), DOI 10.5890/DNC.2016.09.006, reports a four-type uniqueness result for a symmetric class. Its complete hypotheses remain unavailable in this session, so worldwide novelty is not asserted. Jamilov's five-type counterexample is credited as prior work.

The source proof campaign is preserved at commit 3810dc7f5ca7df1f6f4637f4628304161efa34e0 in yspennstate/math-open-problems, under proofnet24/portfolio-completion/runs/2026-09-14/2026-09-14_20-23-26/. The new 100-agent creative Lyons campaign is a separate task and is not evidence for the QSO theorem.
