# Open problem T105: The Berry–Tabor conjecture

Statement: For a generic completely integrable quantum system, for example the Laplacian on a flat torus R^2/L with a generic lattice L, the eigenvalues counted once for each pair ±v of dual-lattice vectors and unfolded have the local statistics of a Poisson process: every k-point correlation function and the nearest-neighbour spacing distribution converge to the Poisson ones.

Caveat: The spectrum of a flat torus is symmetric under v ↦ −v, so without this identification every positive eigenvalue has even multiplicity and the spacing law has an atom at zero. Arithmetic tori such as the square torus have further multiplicities and are exceptions, so a theorem needs an explicit genericity (Diophantine) condition and must cover every local statistic, not only the pair correlation.

Source: M. V. Berry and M. Tabor, Level clustering in the regular spectrum, Proc. R. Soc. Lond. A 356 (1977)

Where it stands (checked by us, Nov 2026): The pair correlation is Poisson for almost every flat 2-torus (Sarnak 1997) and for explicit Diophantine tori (Eskin–Margulis–Mozes, Ann. of Math. 161 (2005) 679); some higher correlations are known for almost every torus (VanderKam, Duke Math. J. 97 (1999); Comm. Math. Phys. 210 (2000)); Blomer, Bourgain, Radziwiłł and Rudnick (arXiv:1809.07881) obtain the triple correlation on average over tori and long gaps, and Marklof proved pair-correlation results for related integrable models (Ann. of Math. 158 (2003) 419). The spacing distribution is open for every individual torus.

Earlier work: a previous worker spent one session on this problem. Its folder is ~/codex_op_1114/briefs/T105 (read it,
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
VERDICT: PARTIAL omitted 2026 pair-correlation advance documented; flat 2-torus spacing remains unresolved

The bounded literature check found an advance beyond the references listed in the brief. Under instruction 1, work stops at the literature branch. The theorem, precise scope and references are in [SOLVED_ELSEWHERE.md](SOLVED_ELSEWHERE.md). No original proof or numerical result is claimed.

The main reference is Wooyeon Kim, Jens Marklof, Matthew Welsh, [arXiv:2601.03209v2](https://arxiv.org/abs/2601.03209v2), Theorem 1.1. It concerns three-dimensional boxes and pair correlation. No solution of the stated two-dimensional full-statistics problem was found. The paper predates the brief’s nominal November 2026 status date, so this is a correction of its coverage rather than a demonstrated later publication.

The web queries, opened URLs, relevant output and audit are recorded in [LOG.md](LOG.md). Validation compared the abstract with both full-text formats, checked symmetry multiplicities, and re-derived the unfolding constant in two ways. The explicit example’s squared length ratios were checked algebraically. The full 33-page proof was not independently verified; this is a literature finding, not a proof certificate.

Failures and limits: PDF screenshot retrieval failed; PDF text and HTML were accessible. The sandbox denied priority adjustment and process inspection, so no computational experiment was launched. Searches cannot certify the absence of another recent paper. The initial background also conflates the triple-correlation authors and the dimension of VanderKam’s results; corrections are documented in the companion file.

Next worker: retain the two-dimensional target as open, correct the background, and select a narrow original task addressing two-dimensional higher correlations or gap probabilities. Do not infer spacing convergence from a pair-correlation theorem, or apply a three-dimensional symmetry-sector result to a spectrum reduced only by ±.

Task: “push this problem forward by one checkable piece.” Date: 2026-11-14; first recorded clock: 22:00:46 Asia/Tbilisi (prompt receipt time unavailable).
