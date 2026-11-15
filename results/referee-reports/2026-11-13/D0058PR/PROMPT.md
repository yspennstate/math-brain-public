You are a referee for a probability journal. You did not write the paper in paper/ (main.tex, main.pdf, 10 pages): "Survival and
moments in critical Derrida--Retaux recursions". Nobody will answer questions; decide for yourself. Source texts are in sources/ as
plain text (Chen-Derrida-Hu-Lifshits-Shi arXiv:1705.04787 v1 and v2, Chen-Hu-Shi arXiv:2108.05610 and others the author used); two
earlier papers by the same author are in posted/ (survival_constant_main.tex, heavy_tail_main.tex). Use them to check every cited
statement; fetch any cited source that is missing (plain text only, no PDFs kept).

Do this, in order, saving as you go:
1. Read main.pdf from page 1 to the end before anything else. Write in REFEREE.md what pages 1-3 alone say the theorems are, what is
   known (the source's conjectures and its integrability remark; the first-moment link in the source; the two posted papers), what
   is new here, and whether the paper anywhere presents the corollary as a refutation of the finite-third-tilted-moment conjecture.
2. Check the proofs independently, every load-bearing step, with line numbers: the path/tree bound (disjointness of the events at
   their lowest common ancestor, independence used only within an event), the positivity of the infinite product, the
   identification of the conditional law, the uniform tail bound and why it gives convergence of every positive moment and of the
   exponential moments for 1 < s < m, the equivalence theorem and each direction of it (Conjecture 1, the first moment, all
   moments; what is and is not claimed for Conjecture 2 and Conjecture 4), and the corollary from Theorem 1.1 of the
   survival-constant paper. Try to break each statement: a law, an m, or a b for which a step fails. If a step is wrong and cannot
   be fixed, say so plainly.
3. Check each citation against its source: title, authors, journal, year, volume, pages, DOI or arXiv id, and that the theorem,
   conjecture or page cited says what the paper says. Flag anything attributed wrongly or claimed as new when it is in print.
4. Voice and form: no sentence about how the paper was written, searched, checked or revised; no filler; every symbol defined at
   first use; the end sections (acknowledgements and funding, competing interest, AI declaration, data availability) present.
First line of REFEREE.md is exactly one of ACCEPT, MINOR, MAJOR, REJECT. Then the findings, each with a line number and the fix.
Do not edit the paper. Keep LOG.md. Work only in this directory. At most 2 threads, nice 10. No publication anywhere, no pushes,
no uploads.
