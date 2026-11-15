# Open problem T105: The Berry–Tabor conjecture

Statement: For a generic completely integrable quantum system, for example the Laplacian on a flat torus R^2/L with a generic lattice L, the eigenvalues counted once for each pair ±v of dual-lattice vectors and unfolded have the local statistics of a Poisson process: every k-point correlation function and the nearest-neighbour spacing distribution converge to the Poisson ones.

Caveat: The spectrum of a flat torus is symmetric under v ↦ −v, so without this identification every positive eigenvalue has even multiplicity and the spacing law has an atom at zero. Arithmetic tori such as the square torus have further multiplicities and are exceptions, so a theorem needs an explicit genericity (Diophantine) condition and must cover every local statistic, not only the pair correlation.

Source: M. V. Berry and M. Tabor, Level clustering in the regular spectrum, Proc. R. Soc. Lond. A 356 (1977)

Where it stands (checked by us, Nov 2026): The pair correlation is Poisson for almost every flat 2-torus (Sarnak 1997) and for explicit Diophantine tori (Eskin–Margulis–Mozes, Ann. of Math. 161 (2005) 679); some higher correlations are known for almost every torus (VanderKam, Duke Math. J. 97 (1999); Comm. Math. Phys. 210 (2000)); Blomer, Bourgain, Radziwiłł and Rudnick (arXiv:1809.07881) obtain the triple correlation on average over tori and long gaps, and Marklof proved pair-correlation results for related integrable models (Ann. of Math. 158 (2003) 419). The spacing distribution is open for every individual torus.

Earlier work: a previous worker spent one session on this problem. Its folder is ~/codex_op_1114/briefs/T105 (read it,
never edit it). Its REPORT.md is copied below. Read its REPORT.md, LOG.md, PROOF.md and scripts before you start.

Later work: a round 3 worker built on that session. Its folder is ~/codex_op_1114r3/briefs/T105 (read it,
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
VERDICT: PROVED exact optimality of the 2.00636 threshold in an explicitly defined scalar moment relaxation

The new result is a limitation of one route toward long gaps. The earlier session recorded a literature correction and supplied no original proof or computation. [PROOF.md](PROOF.md) now proves that the published long-gap constant cannot be increased using only the first two Poisson factorial moments of the local count, separately at each interval length, together with mean spacing and the full Lipschitz constraint supplied by pair correlation.

The proof solves the scalar moment problem exactly and constructs a nonexponential gap CDF attaining the threshold. Its endpoint G* is the root in (2,109/54) of

35−18G−9G²+(12G−10)sqrt(6G−5)=0.

This is the existing constant in Christoph Aistleitner, Valentin Blomer and Maksym Radziwiłł, *Triple correlation and long gaps in the spectrum of flat tori*, [arXiv:1809.07881](https://arxiv.org/abs/1809.07881), [published online-first text, Corollary 3](https://ems.press/content/serial-article-files/31432). The addition here is an explicit optimality certificate for the stated relaxation, not a larger torus gap bound. No claim of global novelty is made for the elementary moment inequalities or this relaxation calculation.

The earlier main claim was independently checked and holds: Wooyeon Kim, Jens Marklof and Matthew Welsh, [arXiv:2601.03209v2, Theorem 1.1](https://arxiv.org/html/2601.03209v2), prove pair correlation for three-dimensional Dirichlet boxes. The unfolding and symmetry counts were re-derived. The bounded literature check found no solution of the stated two-dimensional problem and finished within five minutes. No SOLVED_ELSEWHERE.md is warranted here.

Validation: the threshold was derived by CDF integration, checked through a quartic polynomial, and checked again by integrating the explicit density. Exact signs give 1603/800<G*<109/54. All moment witnesses, upper constraints and endpoints were checked algebraically. Details and source versions are in [LOG.md](LOG.md).

Commands: web `search_query`, `open` and `find` calls are recorded in LOG.md. Read-only shell commands used `OMP_NUM_THREADS=1 nice -n 15` with `cat` and directory listings. The earlier folder contains neither PROOF.md nor scripts. No numerical script was run: the sandbox denies `nice` priority adjustment. All saved changes used the workspace patch tool; nothing outside this folder was edited.

Failures and uncertainty: optimizing the scalar inequalities yields the existing constant exactly. It cannot improve that constant within this relaxation. The candidate CDF and its separate count laws have not been realized by a common point process or spectrum. The known averaged triple theorem does not assert pointwise triple convergence for an individual torus. The complete Berry–Tabor conjecture remains unresolved. The full proofs of the cited torus theorems were not independently checked. One EMS URL timed out; an alternate publisher PDF opened successfully. Literature searches cannot certify that no other relevant result exists.

Next worker: retain joint count information. For adjacent intervals (0,a] and (a,a+b], impose integer counts A,B with E A=a, E B=b, E[A(A−1)]=a², E[B(B−1)]=b² and E[AB]=ab, together with P(A>0)=F*(a) and P(A+B>0)=F*(a+b). Test whether the explicit extremizer (15) can satisfy these constraints for all a,b. An incompatibility certificate would add information genuinely absent from the scalar relaxation; compatibility would identify the next relation to retain. The averaged theorem's quantifiers must still be handled separately before drawing a torus conclusion.

Task: “take the NEXT checkable step on this problem, building on that work.” First recorded clock: 2026-11-15 01:29:06 Asia/Tbilisi; prompt receipt time unavailable.
