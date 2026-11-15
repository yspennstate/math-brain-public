Open problem E0055. Source: A. S. Bandeira, "Ten lectures and forty-two open problems in the mathematics of data science" (2015
lecture notes; check the exact title, version and arXiv/URL), Open Problem 10.1, PDF p. 133: the projected power method (or the
power-type iteration stated there) for the spiked Wigner model / synchronization problem as stated in that section; the question is
the threshold on the signal-to-noise ratio above which the method converges to a point correlated with the planted signal (or to
the MLE), from the stated initialisation. State the exact model, iteration, initialisation and question from the source.

Do this, in order, saving as you go:
1. Literature first. Get the source into sources/ as plain text; state Open Problem 10.1 exactly, with page numbers. Search
   2015-2026 work: Boumal ("Nonconvex phase synchronization", SIAM J. Optim. 2016), Zhong-Boumal 2018, Chen-Candes ("The projected
   power method", CPAM 2018), Ling ("Near-optimal performance bounds for orthogonal and permutation group synchronization", "On the
   exactness of SDP relaxation for synchronization"), Montanari et al. (approximate message passing for spiked models, Deshpande-
   Abbe-Montanari), Liu-Yue-So, Zhang-Zhou, Javanmard-Montanari-Ricci-Tersenghi, "projected power method" "spiked Wigner",
   "generalized power method" "Z2 synchronization" "optimal threshold". If a printed result settles the question (fully or for a
   stated parameter range or initialisation), give the theorem and page and stop with RESOLVED_IN_LITERATURE (or PARTIAL).
2. Otherwise attempt a proof of convergence above the conjectured threshold (or a counterexample below it, or a sharper partial
   threshold than in print), with every step checked; state precisely what remains.
3. Compute (evidence only): simulate the method for n up to a few thousand, several SNRs around the threshold, from the stated
   initialisation; report the empirical transition.
Write REPORT.md. Its first line is exactly one of PROVED, COUNTEREXAMPLE, PARTIAL, NO_PROGRESS, RESOLVED_IN_LITERATURE.
Then the statement, the proof, what was checked and how, and the literature result with exact theorem numbers and pages.
Keep LOG.md as you go. Code in code/, data in data/. Source texts may go in sources/ as plain text only; no PDFs kept, no
page images or scans of any paper or book anywhere in this folder. Work only in this directory. At most 4 threads, under
4 GB, nice 10. No publication anywhere, no pushes.
