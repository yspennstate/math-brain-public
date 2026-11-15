Open problems I0013 and I0014. Source: arXiv:2609.04638, "Can we further improve the central limit theorem for stationary
rho-mixing sequences? (with related open problems)" (identify authors, date and version exactly from the arXiv listing). The paper
sharpens Peligrad's central limit theorem for strictly stationary rho-mixing sequences. Two questions it leaves:
 I0014, Remark 2.5(i): "It seems difficult to extend Corollary 2.3 (b) to the region beta in (0, 1/2)."
 I0013, Remark 2.5: "in which subspace of gamma < 2 alpha can one construct a counterexample to the CLT", noting that "in light of
   Theorem 1 and Proposition 0 of [3], the constant d appears to depend on A_j and B_tau defined therein, and a further analysis of
   these constants is required".
State both exactly: the hypotheses (rho(n) decay rate, variance growth sigma_n^2, the parameters alpha, beta, gamma, the moment
conditions), Corollary 2.3 (b) word for word, and what [3] is (likely Bradley's counterexample construction; identify it exactly).

Do this, in order, saving as you go:
1. Literature first. Get the source into sources/ as plain text; state its main theorem and Corollary 2.3 with page numbers, and the
   known results it builds on: Ibragimov's CLT for rho-mixing, Peligrad's theorem (sum of rho(2^k) finite, or the weaker
   conditions), Bradley's counterexamples to the CLT for rho-mixing sequences (identify [3] and its Theorem 1 and Proposition 0),
   Utev, Shao, Peligrad-Utev. Search for later work. If a printed result answers either question, report it.
2. I0014 first: try to extend Corollary 2.3 (b) to beta in (0, 1/2). Find exactly which step of the proof uses beta >= 1/2 (a
   blocking or Bernstein-type argument, a maximal inequality, a variance comparison). Either prove the extension, possibly under an
   extra hypothesis you state, or build a stationary rho-mixing sequence with the stated rates for some beta < 1/2 for which the
   conclusion fails, with every step checked. Then I0013: determine for which parameters below gamma < 2 alpha Bradley's
   construction (with its constants A_j, B_tau tracked explicitly) yields a counterexample, and state the region you can prove.
3. Compute only where it checks a constant or an inequality (exact or high-precision arithmetic for the counterexample's
   parameters); no simulation stands in for a proof.
Write REPORT.md. Its first line is exactly one of PROVED, COUNTEREXAMPLE, PARTIAL, NO_PROGRESS, RESOLVED_IN_LITERATURE, describing
the stronger of the two outcomes, with a separate verdict line for each of I0013 and I0014. Then the statements, the proofs, what was
checked and how, and the literature results with exact theorem numbers and pages.
Keep LOG.md as you go. Code in code/, data in data/. Source texts may go in sources/ as plain text only; no PDFs kept, no
page images or scans of any paper or book anywhere in this folder. Work only in this directory. At most 4 threads, under
4 GB, nice 10. No publication anywhere, no pushes.
