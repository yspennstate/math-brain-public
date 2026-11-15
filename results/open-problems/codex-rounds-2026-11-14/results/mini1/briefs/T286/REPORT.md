VERDICT: PARTIAL literature status corrected; substantial follow-ups found, general theorem still open

The bounded literature search found a rigorous restricted quadratic follow-up and developed general-activation predictions. References, exact theorem locations and restrictions are in [SOLVED_ELSEWHERE.md](SOLVED_ELSEWHERE.md). Its filename is required by the prompt's stopping branch and does not mean the general problem is solved.

The key rigorous reference is Yizhou Xu, Antoine Maillard, Lenka Zdeborová, Florent Krzakala, [arXiv:2503.14121](https://arxiv.org/abs/2503.14121), Theorem 2.10. The principal general-activation follow-up is Jean Barbier, Francesco Camilli, Minh-Toan Nguyen, Mauro Pastore, Rudy Skerk, [arXiv:2510.24616](https://arxiv.org/abs/2510.24616), whose Remark 4 retains explicit conjectures.

No new theorem or computation was attempted after the substantial-advance finding, following instruction 1. These advances predate the supplied November 2026 status date; the search did not uncover a subsequent rigorous solution. The assertion that the general case remains open survives this check, while the quadratic caveat can be sharpened.

Verification: compared abstracts against full-text theorem statements and caveats; checked the sample scaling directly in equation (4) of 2510.24616; distinguished ADAM experiments from gradient-descent theorems, and fresh-sample online SGD from reuse of a fixed dataset. No load-bearing numerical estimates were made. Published proofs were not independently reconstructed in full.

Commands and web queries are recorded in [LOG.md](LOG.md). Shell work consisted of reading local orientation files, checking time and writing these documents. No numerical program, git operation or external write was run. Two guessed HTML version URLs returned 404; correct versions were subsequently opened.

Next worker: start with Appendix B.6 of 2510.24616v5, audit its interpolation remainder and concentration assumptions, and isolate one lemma for activations with μ₀=μ₁=μ₂=0. Keep the ReLU case separate because its second Hermite coefficient is nonzero. Neither optimizer experiments nor online-SGD timescale predictions settle the fixed-dataset gradient-descent question.

Task: “push this problem forward by one checkable piece” — session logged 14 November 2026, 22:09 Asia/Tbilisi.
