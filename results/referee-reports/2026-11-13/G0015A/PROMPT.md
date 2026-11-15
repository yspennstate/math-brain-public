Open problem G0015. Source: Kumar and Dudeja, a 2026 paper on threshold cascades with a continuous type (source id
kumar_dudeja_threshold_cascades_2026; find it on arXiv by those author names and words "threshold", "cascade"), Conjecture 7.2,
Section 7, PDF p. 8: under the hypotheses of Theorem 6.1 at criticality rho(K) = 1, with an exponential-moment hypothesis on the
offspring count, the critical cluster conditioned on {|S| = n}, with graph distance rescaled by Sigma_c / sqrt(n), converges in
the Gromov-Hausdorff-Prokhorov sense to Aldous' Continuum Random Tree, with an explicit constant Sigma_c built from sigma^2_off
and the tilted stationary law varpi*. The source's Programme 7.3 says the obstacle is that the type space is Polish (R or D x R),
not finite, so Miermont's finite-type invariance principle does not apply directly. Read the source for the exact wording and
every hypothesis (the kernel K, its spectral radius, Harris/positivity conditions, moment conditions).

Do this, in order, saving as you go:
1. Literature first. Get the source into sources/ (plain text only). State Theorem 6.1, Conjecture 7.2 and Programme 7.3
   exactly. Search: Miermont ("Invariance principles for spatial multitype Galton-Watson trees", 2008), de Raphelis (multitype
   trees with infinitely many types, "Scaling limit of multitype Galton-Watson trees with infinitely many types", AIHP 2017),
   Stephenson, Abraham-Delmas-Hoscheit, Haas-Miermont (Markov branching trees), Janson (simply generated trees), Kesten-Stigum
   for general type spaces, Athreya-Ney, Marzouk, and 2017-2026 work on GW trees with countable or continuous types. If a printed
   theorem already covers this setting (for example de Raphelis' infinite-type result under a uniform ergodicity condition),
   give the theorem and page, check every hypothesis against the source's model, and stop with RESOLVED_IN_LITERATURE only if it
   applies as stated.
2. Understand the gap: what a reduction to a single-type tree by stopping at returns to a small set (regeneration, Harris
   chain atom or Nummelin splitting) needs, and why the exponential moment and the tilted law varpi* enter Sigma_c.
3. Prove what you can, with complete proofs: the conjecture under an added hypothesis (for instance a Doeblin / small-set
   minorisation on the type kernel, or bounded density ratios), via a reduced tree with i.i.d.-like structure and a known
   single-type or finite-type CRT theorem, identifying Sigma_c; or tightness of the height process in that setting.
4. Compute (evidence only): simulate the critical cascade conditioned on size n for a concrete continuous-type kernel from the
   source, compare height and width statistics with the CRT prediction for the conjectured Sigma_c, for n up to 10^5.
Write REPORT.md. Its first line is exactly one of PROVED, COUNTEREXAMPLE, PARTIAL, NO_PROGRESS, RESOLVED_IN_LITERATURE.
Then the statement, the proof, what was checked and how, and the literature result with exact theorem numbers and pages.
Keep LOG.md as you go. Code in code/, data in data/. Source texts may go in sources/ as plain text only; no PDFs kept, no
page images or scans of any paper or book anywhere in this folder. Work only in this directory. At most 4 threads, under
4 GB, nice 10. No publication anywhere, no pushes.
