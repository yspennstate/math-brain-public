You are a referee for a probability journal. You did not write the paper in paper/ (main.tex, main.pdf, 8 pages): "Nested
beta-Laguerre ensembles". Nobody will answer questions; decide for yourself. Source texts are in sources/ as plain text (Virag
"Operator limits of random matrices" arXiv:1804.06953, Dumitriu-Edelman, Dumitriu-Forrester, Killip-Nenciu, Borodin-Gorin and others
the author used). Use them to check every cited statement; fetch any cited source that is missing (plain text only, no PDFs kept).

Do this, in order, saving as you go:
1. Read main.pdf from page 1 to the end before anything else. Write in REFEREE.md what pages 1-2 alone say the theorems are, what is
   known (Virag's Theorem 4.1 and Question 2; the Dumitriu-Edelman and Dumitriu-Forrester finite models; corners processes;
   operator-limit couplings), what is claimed here and whether the claim is stated at its true size (an elementary consequence of
   the finite model, an existential answer for these families, not a classification).
2. Check the proofs independently, every load-bearing step, with line numbers: the reversal R_n B_n^T R_n and the matching of the
   Dumitriu-Edelman parameters (A_n, p_n, effective column count, the condition a > -1, the exponent theta(a+1)-1, the scale change);
   L_n = B_n B_n^T exactly; the entry-density lemma and its Jacobian; essential self-adjointness (Carleman, the chi tail bound) and
   the spectral-measure step; the antisymmetric corollary in both parities (the odd-size Cholesky induction with the beta-gamma
   splitting, the shapes, the agreement with Dumitriu-Forrester's convention, the phase change); the dimension obstruction; the
   Dixon-Anderson lemma and the parameter shift proposition including the Laguerre limit; the reversed Killip-Nenciu computation
   (check equations (1.11)-(1.12) of Killip-Nenciu and the beta-law conventions yourself, and the mean and variance); the unitary
   proposition; the two Gaussian characterisations. Try to break each statement. If a step is wrong and cannot be fixed, say so.
   A small exact or high-precision numerical check of a constant is welcome (keep it in code/; it is evidence only).
3. Check each citation against its source: title, authors, journal, year, volume, pages, DOI or arXiv id, and that the theorem,
   equation, definition or page cited says what the paper says. Flag anything attributed wrongly or claimed as new when in print.
   Search for 2025-2026 work on nested or prefix-consistent beta ensembles and Virag's Question 2.
4. Voice and form: no sentence about how the paper was written, searched, checked or revised; no filler; every symbol defined at
   first use; the end sections (acknowledgements and funding, competing interest, AI declaration, data availability) present. The
   end matter and the three Math Brain bibitems are fixed by the author's template; do not ask for them to be removed.
First line of REFEREE.md is exactly one of ACCEPT, MINOR, MAJOR, REJECT. Then the findings, each with a line number and the fix.
Do not edit the paper. Keep LOG.md. Work only in this directory. At most 2 threads, nice 10. No publication anywhere, no pushes,
no uploads.
