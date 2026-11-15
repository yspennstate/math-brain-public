Open problem F0124. Source: F. den Hollander and J. E. Steif, "Random walk in random scenery: a survey of some recent results"
(2006), arXiv:math/0608219, Conjecture 2.16, Section 2.6, PDF p. 9: for the reduced random walk in random scenery on Z with
steps F = {-1, +1}, P(+1) = p in [1/2, 1], and an i.i.d. two-colour scenery with values in {-1, +1}, every configuration
(Y_n)_{n != 0} is bad for Y_0 when p in [1/2, 4/5), and every configuration is good for Y_0 when p in (4/5, 1]. (Read the source
for the exact setting: the two-sided walk, the scenery law (fair or general colour probabilities), the definition of bad and good
configurations on PDF p. 8 via Lambda_n = [-n, n] and the total-variation discontinuity of the conditional law of W_0, the
Maes-Redig-Van Moffaert results, and what is already proved in Section 2.6 for p = 1/2 and for p near 1.)

Do this, in order, saving as you go:
1. Literature first. Download arXiv:math/0608219 into sources/ (plain text only) and read Sections 1 and 2.6 exactly. Search for
   later work: den Hollander-Steif-van der Wal "Bad configurations for random walk in random scenery and related subshifts"
   (Stoch. Proc. Appl. 2005); Maes-Redig-Takens-van Moffaert-Verbitski "Intermittency and weak Gibbs states" and Maes-Redig-Van
   Moffaert "Almost Gibbsian versus weakly Gibbsian measures"; Verbitskiy on non-Gibbsianness of factors; Steif and coauthors after
   2006; den Hollander's later papers; "random walk in random scenery" + "Gibbsian" / "continuity" / "4/5" in 2006-2026. If the
   conjecture (either half) is proved or refuted in print, give the exact reference and theorem and stop with REPORT.md first line
   RESOLVED_IN_LITERATURE (only if both halves are settled; otherwise record what is settled and continue).
2. Understand the threshold. Explain where 4/5 comes from (a heuristic: compare the cost of a walk visiting a far-away region to
   rewrite the scenery seen at time 0 with the entropy gained; large deviations of the drifted walk returning to the origin
   region), and which half is easier. Identify the mechanism that makes a configuration bad (a far-away pattern changes the
   inferred scenery near the origin) and why strong drift kills it.
3. Prove what you can, with complete proofs: either half of the conjecture; the good half for p above some explicit p_0 < 1 better
   than what the source has; the bad half for p in [1/2, p_1) with explicit p_1 > 1/2; or a counterexample showing the threshold
   is not 4/5 (for instance a configuration that is good for some p < 4/5, or bad for some p > 4/5), with proof.
4. Compute (as evidence only). For finite windows, compute exactly (by transfer/dynamic programming over walk paths and scenery)
   the conditional law of Y_0 given Y on Lambda_m minus {0} for two configurations agreeing on Lambda_n, and measure the
   total-variation gap as m grows, for p on a grid around 4/5. Use exact rational arithmetic or interval arithmetic where a claim
   rests on it.
Write REPORT.md. Its first line is exactly one of PROVED, COUNTEREXAMPLE, PARTIAL, NO_PROGRESS, RESOLVED_IN_LITERATURE.
Then the statement, the proof, what was checked and how, and the literature result with exact theorem numbers and pages.
Keep LOG.md as you go. Code in code/, data in data/. Source texts may go in sources/ as plain text only; no PDFs kept, no
page images or scans of any paper or book anywhere in this folder. Work only in this directory. At most 4 threads, under
4 GB, nice 10. No publication anywhere, no pushes.
