# Open problem T086: Small ball probabilities for the Brownian sheet in dimension three and higher

Statement: For the Brownian sheet W on [0, 1]^d with d ≥ 3, −log P(sup_{t ∈ [0,1]^d} |W(t)| ≤ ε) is of order ε^{−2} (log(1/ε))^{2d−1} as ε → 0.

Caveat: The exponent 2d − 1 is the conjectured one; it matches Talagrand's d = 2 answer.

Source: M. Talagrand, The small ball problem for the Brownian sheet, Ann. Probab. 22 (1994); D. Bilyk, M. Lacey and A. Vagharshakyan, On the small ball inequality in all dimensions, J. Funct. Anal. 254 (2008)

Where it stands (checked by us, Nov 2026): d = 2: ε^{−2}(log 1/ε)^3 (Talagrand 1994). For d ≥ 3 an upper bound with exponent 2d − 1 (Dunker–Kühn–Lifshits–Linde 1998) and a lower bound with exponent 2d − 2, improved by a small power of the logarithm (Bilyk–Lacey, arXiv:math/0609815, Duke Math. J. 2008, in d = 3; Bilyk–Lacey–Vagharshakyan, arXiv:0705.4619, J. Funct. Anal. 2008, in d ≥ 4). Open.

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
- Work only inside this folder (~/brain-repo/12_cognitive_architecture/codex_local_1108/briefs/OP14_T086). Read anything, but never edit files elsewhere, never use git, never push, post, email or
  create accounts. Nothing you write leaves this folder except when the coordinating agent copies it.
- Compute: every program you run stays under 1 GB of RAM, one thread (set OMP_NUM_THREADS=1), runs at below-normal priority,
  and finishes within 20 minutes per run. No GPU, no torch, no training. This laptop is the author's working computer; never fill its memory and never open a visible window.
- Literature: use the web search tool. Cite only papers you actually opened, with the authors exactly as on the paper or
  its arXiv page. Never invent a reference, a number or a step.
- Save as you go: append to LOG.md after every step (what you did, the command, the output that matters). The account's
  weekly allowance runs out within hours and the session may stop at any moment; LOG.md is what survives.
- Write plainly, like a working mathematician: no hype, no talk about yourself or the process inside PROOF.md.
