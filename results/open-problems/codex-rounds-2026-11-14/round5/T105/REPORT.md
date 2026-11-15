VERDICT: PROVED an improved almost-everywhere flat-torus gap limsup bound exceeding 2.008

The round-4 adjacent-count certificate holds. Its integer residuals, exact deficit 1/24, and relaxation separation 1/1944 were independently rechecked.

The new result transfers that certificate through the published averaged triple-correlation theorem. For almost every flat 2-torus, with global sign pairs identified and mean spacing one,

\[
\limsup_i(x_{i+1}-x_i)\ge G_\dagger>\frac{251}{125}=2.008.
\]

The constant is specified exactly by

\[
c_\dagger^4-4c_\dagger^3+4c_\dagger^2+24c_\dagger-40
=\frac{393}{8192},\qquad
G_\dagger=\frac{c_\dagger^2+2c_\dagger+6}{6},
\quad \frac{331}{200}<c_\dagger<\frac{53}{32}.
\]

In particular

\[
\frac{481961}{240000}<G_\dagger<\frac{12345}{6144},
\qquad G_\dagger\ge G_*+\frac{131}{73728},
\]

where G* is the preceding scalar threshold, approximately 2.00636. There are infinitely many gaps larger than 2.008; at G_dagger itself the proved assertion is a limsup bound.

The proof replaces the scalar integral on [1,33/32] and [5/4,21/16] by 1/32 times the finite joint-count certificate. Monotonicity justifies this replacement. Its exact extra area is 131/196608. Every triple-count coefficient retains the required sign. A Fatou/density lemma bounds the liminf of the entire nonnegative triple functional, giving one common subsequence. This establishes the quantifier step that round 4 left open. The complete proof, including finite boundary terms and the countable intersection over candidate gap bounds, is in [PROOF.md](PROOF.md).

The external input is Theorem 1 and the recorded almost-everywhere pair correlation in Christoph Aistleitner, Valentin Blomer and Maksym Radziwiłł, *Triple correlation and long gaps in the spectrum of flat tori*, [arXiv:1809.07881](https://arxiv.org/abs/1809.07881), [published text](https://ems.press/content/serial-article-files/31432). The result uses averaged triple convergence; it does not assume pointwise triple convergence. The full proof of that external theorem was not independently checked.

Validation: the gain was calculated by Taylor integration and direct antiderivative differences, and checked by separating pair and triple benchmarks. The baseline was checked by CDF and density integration. Polynomial elimination and rational cross multiplication independently certify the threshold and its strict improvement beyond 2.008. Early exceptional gaps and the last anchor have explicit vanishing corrections. Detailed commands and exact arithmetic are in [LOG.md](LOG.md).

Commands: the initial web search and primary-source opening finished within five minutes; later web reads examined the same published proof. Shell reads used `OMP_NUM_THREADS=1 nice -n 15 /bin/cat` and `/bin/ls`, apart from the initial discovery command. The sandbox denied priority adjustment; no numerical program was run. All authored files were saved with apply_patch in this folder. No git, subagents, or external writes were used; the three previous folders were not changed.

What failed and what remains uncertain: a symmetric-window construction was unnecessary once right-hand windows made monotonicity sufficient. Separate triple liminf bounds would not give the needed shared subsequence; the summed functional resolves that issue. The new constant is not claimed optimal or globally novel. The bounded literature check found no solution of the full two-dimensional target. Wooyeon Kim, Jens Marklof and Matthew Welsh, [arXiv:2601.03209v2](https://arxiv.org/html/2601.03209v2), still concerns three-dimensional box pair correlation. The spacing distribution, higher local statistics, and an explicit Diophantine class for this improved bound remain outside this result.

Next worker: first audit the finite inequality (24) and its single averaged functional (23). Then optimize this same nonnegative certificate: vary the two window lengths together with a,t in the adjacent-count inequality, keeping the windows disjoint and in known scalar branches. Obtain an exact rational certificate before quoting an improved decimal. The current width is convenient, not optimal; no new correlation estimate is needed for this optimization.

Task: “take the NEXT checkable step on this problem, building on that work.” First recorded clock: 2026-11-15 08:22:27 Asia/Tbilisi; prompt receipt time unavailable.
