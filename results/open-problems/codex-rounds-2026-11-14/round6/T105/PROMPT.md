# Open problem T105: The Berry–Tabor conjecture

Statement: For a generic completely integrable quantum system, for example the Laplacian on a flat torus R^2/L with a generic lattice L, the eigenvalues counted once for each pair ±v of dual-lattice vectors and unfolded have the local statistics of a Poisson process: every k-point correlation function and the nearest-neighbour spacing distribution converge to the Poisson ones.

Caveat: The spectrum of a flat torus is symmetric under v ↦ −v, so without this identification every positive eigenvalue has even multiplicity and the spacing law has an atom at zero. Arithmetic tori such as the square torus have further multiplicities and are exceptions, so a theorem needs an explicit genericity (Diophantine) condition and must cover every local statistic, not only the pair correlation.

Source: M. V. Berry and M. Tabor, Level clustering in the regular spectrum, Proc. R. Soc. Lond. A 356 (1977)

Where it stands (checked by us, Nov 2026): The pair correlation is Poisson for almost every flat 2-torus (Sarnak 1997) and for explicit Diophantine tori (Eskin–Margulis–Mozes, Ann. of Math. 161 (2005) 679); some higher correlations are known for almost every torus (VanderKam, Duke Math. J. 97 (1999); Comm. Math. Phys. 210 (2000)); Blomer, Bourgain, Radziwiłł and Rudnick (arXiv:1809.07881) obtain the triple correlation on average over tori and long gaps, and Marklof proved pair-correlation results for related integrable models (Ann. of Math. 158 (2003) 419). The spacing distribution is open for every individual torus.

Earlier work: a previous worker spent one session on this problem. Its folder is ~/codex_op_1114/briefs/T105 (read it,
never edit it). Its REPORT.md is copied below. Read its REPORT.md, LOG.md, PROOF.md and scripts before you start.

Later work: a round 3 worker built on that session. Its folder is ~/codex_op_1114r3/briefs/T105 (read it,
never edit it). Its REPORT.md is copied below. Read its REPORT.md, LOG.md, PROOF.md and scripts before you start.

Later work: a round 4 worker built on that session. Its folder is ~/codex_op_1114r4/briefs/T105 (read it,
never edit it). Its REPORT.md is copied below. Read its REPORT.md, LOG.md, PROOF.md and scripts before you start.

Later work: a round 5 worker built on the latest of these. Its folder is ~/codex_op_1114r5/briefs/T105 (read it, never
edit it). Its REPORT.md is copied below. Read its REPORT.md, LOG.md, PROOF.md and scripts before you start.

Your job for this session: take the NEXT checkable step on this problem, building on that work.
1. Five minutes at most: check whether anything after the earlier report changes the picture. If the problem was
   solved elsewhere, write SOLVED_ELSEWHERE.md (reference, arXiv id, what exactly is proved) and REPORT.md, then stop.
2. First re-check the earlier result: re-derive its main claim or re-run its computation an independent way, and
   write in LOG.md whether it holds. If it does not hold, that finding is your result.
3. Then choose ONE piece that extends it: the next step its report names, a wider special case, a sharper constant,
   more cases computed, the missing lemma. Write the choice and why in LOG.md first, then do it. A proof goes in
   PROOF.md with every step written out; a computation is a script in this folder with the command and output in LOG.md.
4. Try to break your own result: re-derive every load-bearing number a second way; look for the case you miss.
5. Finish with REPORT.md: first line exactly one of  VERDICT: PROVED <what> | VERDICT: PARTIAL <what> | VERDICT: COMPUTED
   <what> | VERDICT: NO PROGRESS <why> | VERDICT: EARLIER RESULT WRONG <what> . Then what is new beyond the earlier
   report, the commands, what failed, what you are unsure of, and what the next worker should do.

Rules (the author's standing laws):
- Work only inside this folder. Read anything, but never edit files elsewhere, never use git, never push, post, email or
  create accounts. Nothing you write leaves this folder except when the coordinating agent copies it.
- Compute: every program you run stays under 1 GB of RAM, one thread (set OMP_NUM_THREADS=1), runs under `nice -n 15`,
  and finishes within 20 minutes per run. No GPU, no MLX, no torch. This Mac is shared; never fill it.
- Literature: use the web search tool. Cite only papers you actually opened, with the authors exactly as on the paper or
  its arXiv page. Never invent a reference, a number or a step.
- Save as you go: append to LOG.md after every step (what you did, the command, the output that matters). The account's
  weekly allowance runs out within hours and the session may stop at any moment; LOG.md is what survives.
- Write plainly, like a working mathematician: no hype, no talk about yourself or the process inside PROOF.md.




----- earlier REPORT.md -----
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
