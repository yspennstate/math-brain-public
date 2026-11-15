# Open problem T053: Diffusion in the random Lorentz gas at fixed density

Statement: A point particle moving at unit speed with specular reflection among fixed hard balls of radius r centred at the points of a Poisson process in R^d (d ≥ 2, fixed density and radius below the threshold at which the vacant set stops percolating, the particle started with a random direction in the unbounded component of the vacant set) behaves diffusively: X_t/√t converges to a non-degenerate Gaussian. In d = 2 the motion is recurrent.

Caveat: Started anywhere outside the balls the statement is false: with positive probability the origin lies in a bounded vacant cavity and the particle stays bounded (w672 audit, 14 Oct). Annealed or quenched limit to be fixed.

Source: H. A. Lorentz, The motion of electrons in metallic bodies, Proc. Amsterdam Acad. 7 (1905); H. Spohn, Large Scale Dynamics of Interacting Particles (Springer, 1991)

Where it stands (checked by us, Nov 2026): In the Boltzmann–Grad limit the motion becomes a Markov flight process (Gallavotti 1969; Spohn 1978; Boldrighini–Bunimovich–Sinai 1983); diffusion under a joint Boltzmann–Grad and diffusive scaling, past the kinetic time scale (Lutsko–Tóth, arXiv:1812.11325). Periodic scatterers: CLT with finite horizon (Bunimovich–Sinai 1981), √(t log t) with infinite horizon (Szász–Varjú 2007). Open at fixed density, including recurrence in d = 2.

Earlier work: a previous worker spent one session on this problem. Its folder is ~/codex_op_1114/briefs/T053 (read it,
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
VERDICT: PARTIAL substantial post-2020 advances verified; fixed-density T053 not solved

The literature check found two omitted advances, recorded with exact hypotheses and links in SOLVED_ELSEWHERE.md: Matthies–Winter (arXiv:2506.18539) improves the three-dimensional annealed time window by one logarithm; Tóth (arXiv:2501.00519) proves a semi-quenched joint-limit result. The task explicitly requires stopping after a substantial advance is found. No original proof or simulation was attempted.

Audit: the improved time condition was checked against both the published Theorem 3.1 and the arXiv theorem; the old condition against the original arXiv:1812.11325 page. Theorem 2 versus Theorem 3 in Tóth was checked in both full-text versions, including the subsequence and angular averaging restrictions. His journal article number is 397, verified on its own publication page; the Matthies–Winter bibliography instead prints 1053 for this reference.

Independent scale check: with L=|log r| and T=r^(-2)L^(-3/2), the new smallness product is L^(-1/2), while the old one is L^(1/2). Equivalently, setting r=exp(-s) gives products s^(-1/2) and s^(1/2). Thus the enlargement is strict. At fixed r in (0,1), the new product diverges as T grows, so this theorem cannot yield the fixed-density long-time limit by keeping its parameters fixed.

Commands: literature used the web search/open/find tools, with exact queries and opened URLs in LOG.md. Local standard-library reads and file writes used `OMP_NUM_THREADS=1 nice -n 15 python3 -`. Priority was checked with `os.getpriority(os.PRIO_PROCESS, 0)` and returned 20. No numerical experiment was run. The final file audit command and output are in LOG.md.

Limitations: this was a short literature verification, not a complete proof audit of either paper. PMC access failed with a browser challenge; the publisher and arXiv supplied full text. Neither almost-sure convergence at a single fixed density nor planar recurrence was established. The search found no fixed-density solution; that is not a proof of its absence.

Next worker: update the problem's status paragraph with both results, fix the intended annealed/quenched formulation, and then choose a fixed-density lemma. Do not infer a fixed-density theorem by combining the two joint-limit results.

Task: “Diffusion in the random Lorentz gas at fixed density” — 14 November 2026, 20:46 +04:00 (session receipt time).
