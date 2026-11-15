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
VERDICT: PROVED adjacent-interval incompatibility of the scalar extremizer and a positive separation G >= G* + 1/1944 in the strengthened moment relaxation

The round-3 scalar result holds. Its moment witnesses and threshold were independently re-derived. What is new is the proposed next step: its extremizer F* fails the adjacent-interval constraints already for lengths a=1 and b=1/4.

For nonnegative integer counts A,B and T=A+B, the pointwise inequality

1_{A>0}+2·1_{T>0} >= 2T−T(T−1)/2−B(B−1)/2

implies, under the specified Poisson moments,

F(a)+2F(a+b) >= 2(a+b)−(a+b)²/2−b²/2.

At the selected lengths F* gives 79/48, while the right side is 81/48: an exact contradiction of margin 1/24. A second proof uses the scalar equality support {0,2,3}. The certificate also holds directly for finite spectral counts and tolerates small moment errors; no convergence of count laws is used.

Adding only this one joint law to the scalar relaxation forces its support endpoint to satisfy G >= G*+1/1944. Here G* is the preceding report's exact root near 2.00636. The proof converts the certificate's positive deficit into excess area above the scalar CDF envelope. This is a necessary bound for a strengthened relaxation, not its optimum and not an improved flat-torus gap theorem. The complete proof and exact constant audit are in [PROOF.md](PROOF.md); commands, source checks and intermediate results are in [LOG.md](LOG.md).

The under-five-minute web check found no solution of the two-dimensional target. Opened primary sources include Christoph Aistleitner, Valentin Blomer, Maksym Radziwiłł, [*Triple correlation and long gaps in the spectrum of flat tori*, arXiv:1809.07881](https://arxiv.org/abs/1809.07881), and its [publisher text](https://ems.press/content/serial-article-files/31432). Their averaged triple theorem must not be replaced by pointwise triple convergence. The already-recorded [Kim–Marklof–Welsh result](https://arxiv.org/html/2601.03209v2) remains a three-dimensional Dirichlet-box pair-correlation theorem. No SOLVED_ELSEWHERE.md is warranted by this check.

Validation: the incompatibility was proved by two independent arguments; the envelope was checked by CDF and density integration; all rational margins, area and slope estimates, root signs, large-endpoint comparisons, error coefficients, and ordered-count factors were checked separately. No numerical program was run. Read commands used `OMP_NUM_THREADS=1 nice -n 15 /bin/cat` and `/bin/ls`; the sandbox continued to deny priority adjustment. Writes used apply_patch and stayed in this folder. No git or subagents were used.

What failed and what remains uncertain: F* cannot be jointly realized under these moments. No optimal joint threshold or finite-endpoint realization was found. The new bound has not been transferred through the averaged torus theorem. The literature check is bounded, and no global priority claim is made for the elementary inequality or its use here.

Next worker: start with the exact finite-count inequality (20) in PROOF.md. Combine its two triple terms with the scalar long-gap inequalities using nonnegative weights, and prove the needed common-subsequence upper bound through the published density-point/averaging argument. Establish that quantifier step before announcing any improved torus gap constant.

Task: “take the NEXT checkable step on this problem, building on that work.” First recorded clock: 2026-11-15 04:54:16 Asia/Tbilisi; prompt receipt time unavailable.
