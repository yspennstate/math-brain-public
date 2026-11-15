Open problem E0057. Source: A. S. Bandeira, "Ten lectures and forty-two open problems in the mathematics of data science"
(lecture notes, 2015/2016; MIT course notes, find the PDF/arXiv-hosted version by title), Open Problem 10.4, PDF p. 139:
(1) Is the quasi-maximum-likelihood (or the maximum-likelihood) estimator consistent for the multireference alignment (MRA)
problem, after fixing the power spectrum appropriately? (2) For a given signal length L and noise level sigma, how large must
the number of observations n be to allow reasonably accurate recovery in MRA? Read the source for the exact model (cyclic
shifts of a signal in R^L, i.i.d. Gaussian noise, uniform or general shift distribution), the quasi-MLE it means, and what
"fixing the power spectrum" refers to.

Do this, in order, saving as you go:
1. Literature first. Get the source into sources/ (plain text only) and read Section 10 exactly. Search: Perry-Weed-Bandeira-
   Rigollet-Singer "The sample complexity of multireference alignment" (SIAM J. Math. Data Sci. 2019; n ~ sigma^6 for generic
   signals with uniform shifts, sigma^2 for non-uniform shifts), Bandeira-Rigollet-Weed "Optimal rates of estimation for
   multi-reference alignment" (Math. Stat. Learn. 2020), Abbe-Bendory-Leeb-Pereira-Sharon-Singer (dihedral MRA, non-uniform
   shift distribution), Bendory-Boumal-Ma-Zhao-Singer (bispectrum inversion), Brunel "Learning rates for Gaussian mixtures
   under group action" (consistency and rates of the MLE in MRA, COLT 2019), Fan-Sun-Wang-Wu (likelihood landscape and
   maximum likelihood for orbit recovery), Katsevich-Bandeira (likelihood maximisation and moment matching in low SNR),
   Dou-Fan-Zhou, Romanov-Bendory-Ordentlich, and 2016-2026 work. Determine for each of (1) and (2) whether it is answered in
   print, under which model assumptions, with exact theorem numbers and pages. If both are answered (for the model the source
   states), stop with REPORT.md first line RESOLVED_IN_LITERATURE; if only one or only under extra assumptions, say exactly
   what remains.
2. If anything remains open (for instance consistency of the quasi-MLE with the power spectrum fixed, which differs from the
   full MLE, or non-generic signals, or the exact constant in the sigma^6 rate): prove what you can with complete proofs, for
   instance consistency of the quasi-MLE via a Kullback-Leibler identifiability argument on the orbit space plus uniform
   convergence on a compact set, for generic signals.
3. Compute (evidence only). Simulate MRA for small L (5..15) at several sigma, run EM / the MLE and the quasi-MLE, and check
   consistency and the sigma^6 scaling numerically.
Write REPORT.md. Its first line is exactly one of PROVED, COUNTEREXAMPLE, PARTIAL, NO_PROGRESS, RESOLVED_IN_LITERATURE.
Then the statement, the proof, what was checked and how, and the literature result with exact theorem numbers and pages.
Keep LOG.md as you go. Code in code/, data in data/. Source texts may go in sources/ as plain text only; no PDFs kept, no
page images or scans of any paper or book anywhere in this folder. Work only in this directory. At most 4 threads, under
4 GB, nice 10. No publication anywhere, no pushes.
