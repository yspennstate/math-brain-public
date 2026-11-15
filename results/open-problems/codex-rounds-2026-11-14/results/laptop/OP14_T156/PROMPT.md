# Open problem T156: The value of the Beardwood–Halton–Hammersley constant

Statement: If X_1, X_2, … are independent uniform points in the unit square and L_n is the length of the shortest closed tour through X_1, …, X_n, then L_n/√n → β almost surely (Beardwood, Halton and Hammersley 1959). Determine β; numerically β ≈ 0.7124.

Caveat: No closed form for β is known or conjectured, so the row asks for the value, or for any description of β beyond simulation. In dimension d the analogous constants are predicted to satisfy β_d ~ √(d/(2πe)) as d → ∞ (Percus–Martin, Phys. Rev. Lett. 76 (1996) 1188–1191).

Source: J. Beardwood, J. H. Halton and J. M. Hammersley, The shortest path through many points, Proc. Cambridge Philos. Soc. 55 (1959) 299–327; J. M. Steele, Probability Theory and Combinatorial Optimization, SIAM (1997)

Where it stands (checked by us, Nov 2026): Beardwood, Halton and Hammersley proved 0.625 ≤ β ≤ 0.92116; later work (Steinerberger, Adv. Appl. Probab. 47 (2015); Gaudio–Jaillet, Oper. Res. Lett. 48 (2020) for the lower bound) brought this to 0.6277 ≤ β ≤ 0.90367, the best bounds before 2026 as stated in the abstract of arXiv:2610.02809, and Dong and Cao (arXiv:2610.02809, October 2026) prove 0.6421 ≤ β ≤ 0.8810, with 0.6536 ≤ β ≤ 0.8749 holding with probability at least 1 − 2·10⁻⁴ over their importance-sampling procedure (a randomized bound, not a deterministic one). Simulations give β ≈ 0.712 (Johnson–McGeoch–Rothberg 1996: 0.7124; Percus–Martin 1996: 0.7120). Open.

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
- Work only inside this folder (~/brain-repo/12_cognitive_architecture/codex_local_1108/briefs/OP14_T156). Read anything, but never edit files elsewhere, never use git, never push, post, email or
  create accounts. Nothing you write leaves this folder except when the coordinating agent copies it.
- Compute: every program you run stays under 1 GB of RAM, one thread (set OMP_NUM_THREADS=1), runs at below-normal priority,
  and finishes within 20 minutes per run. No GPU, no torch, no training. This laptop is the author's working computer; never fill its memory and never open a visible window.
- Literature: use the web search tool. Cite only papers you actually opened, with the authors exactly as on the paper or
  its arXiv page. Never invent a reference, a number or a step.
- Save as you go: append to LOG.md after every step (what you did, the command, the output that matters). The account's
  weekly allowance runs out within hours and the session may stop at any moment; LOG.md is what survives.
- Write plainly, like a working mathematician: no hype, no talk about yourself or the process inside PROOF.md.
