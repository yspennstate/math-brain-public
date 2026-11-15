# Open problem T243: Optimal rates in the Gaussian-process limit of wide random networks

Statement: Let f_n be a depth-L fully connected network with hidden widths n, iid N(0, C_W/fan-in) weights and a fixed Lipschitz activation, viewed as a random field on a compact input set K ⊂ R^d. f_n converges in law to the neural-network Gaussian process (NNGP) as n → ∞. Determine the optimal rate of this convergence in a functional metric (e.g. Wasserstein-2 distance between laws on C(K), or total variation of k-point marginals), including the dependence on L, k and the activation; in particular decide whether the rate is n^{-1/2} or n^{-1} for smooth test functions.

Caveat: Rates for a fixed finite set of inputs in Wasserstein distance are known (several 2022-24 papers); the question asks for functional (sup-norm) rates and sharp depth dependence.

Source: J. Lee et al., Deep Neural Networks as Gaussian Processes, arXiv:1711.00165 (2017); A. G. de G. Matthews et al., Gaussian Process Behaviour in Wide Deep Neural Networks, arXiv:1804.11271 (2018); B. Hanin, Random Neural Networks in the Infinite Width Limit as Gaussian Processes, arXiv:2107.01562 (2021)

Where it stands (checked by us, Nov 2026): Finite-dimensional quantitative CLTs known (Basteri–Trevisan; Favaro et al.; Balasubramanian et al.; Trevisan 2023, to verify). Sharp functional rates open as far as the writer knows.

Your job for this session: push this problem forward by one checkable piece.
1. Ten minutes at most: search whether it was solved or substantially advanced after what "where it stands" says. If it
   was, write SOLVED_ELSEWHERE.md (reference, arXiv id, what exactly is proved). Stop only if the WHOLE problem as stated is settled; otherwise go on to step 2 on the part that is still open. A literature update alone is not this session's piece.
2. Choose ONE concrete piece you can finish: a special case, a finite computation that settles small cases, a sharper
   bound, a counterexample search, a reduction to a cleaner statement. Write the choice and why in LOG.md first.
3. Do it. A proof goes in PROOF.md with every step written out. A computation is a script in this folder; put the exact
   command and its output in LOG.md and the data in a file.
4. Try to break your own result: re-derive every load-bearing number a second, independent way; look for the case your
   argument misses. Record what you checked.
5. Finish with REPORT.md: first line exactly one of  VERDICT: PROVED <what> | VERDICT: PARTIAL <what> | VERDICT: COMPUTED
   <what> | VERDICT: NO PROGRESS <why> . Then what was proved or computed, the commands, what failed, what you are unsure
   of, and what the next worker should do. An honest NO PROGRESS is worth more than a claim that does not hold.

Rules (the author's standing laws):
- Work only inside this folder (~/brain-repo/12_cognitive_architecture/codex_local_1108/briefs/OP14_T243). Read anything, but never edit files elsewhere, never use git, never push, post, email or
  create accounts. Nothing you write leaves this folder except when the coordinating agent copies it.
- Compute: every program you run stays under 1 GB of RAM, one thread (set OMP_NUM_THREADS=1), runs at below-normal priority,
  and finishes within 20 minutes per run. No GPU, no torch, no training. This laptop is the author's working computer; never fill its memory and never open a visible window.
- Literature: use the web search tool. Cite only papers you actually opened, with the authors exactly as on the paper or
  its arXiv page. Never invent a reference, a number or a step.
- Save as you go: append to LOG.md after every step (what you did, the command, the output that matters). The account's
  weekly allowance runs out within hours and the session may stop at any moment; LOG.md is what survives.
- Write plainly, like a working mathematician: no hype, no talk about yourself or the process inside PROOF.md.
