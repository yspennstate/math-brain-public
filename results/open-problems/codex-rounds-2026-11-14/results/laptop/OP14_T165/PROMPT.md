# Open problem T165: Positive recurrence of semimartingale reflecting Brownian motion in four and more dimensions

Statement: Let Z be a semimartingale reflecting Brownian motion (SRBM) in the orthant R^d_+ with drift θ, nonsingular covariance matrix Σ and reflection matrix R (completely-S, so that Z exists and is unique in law). Find necessary and sufficient conditions on (θ, Σ, R) for Z to be positive recurrent, that is, for the expected time to hit any open neighbourhood of the origin to be finite from every starting state, in every dimension d ≥ 4.

Caveat: Sufficient conditions exist in every dimension, for example the fluid criterion of Dupuis and Williams (every path of the associated fluid model is attracted to the origin). In d = 3 this criterion is also necessary, but Bramson's examples in d = 6 show that it is not necessary in high dimensions, so a different kind of condition is needed.

Source: M. Bramson, J. G. Dai and J. M. Harrison, Positive recurrence of reflecting Brownian motion in three dimensions, Ann. Appl. Probab. 20 (2010) 753–783, arXiv:1009.5746

Where it stands (checked by us, Nov 2026): Settled for d = 2, and for d = 3 by Bramson, Dai and Harrison, who, building on El Kharroubi, Ben Tahar and Yaacoubi (Stochastics Stochastics Rep. 68 (2000); Math. Methods Oper. Res. 56 (2002)), give necessary and sufficient conditions that are simple to check; in d = 3 positive recurrence holds if and only if every fluid path is attracted to the origin. In d = 6 Bramson (arXiv:1010.1751) gives positive recurrent examples with a divergent linear fluid path. Recent work concerns stationary distributions in low dimension (Flin, arXiv:2604.27951, the half-plane with two-sided reflection), not the classification. Open.

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
- Work only inside this folder (~/brain-repo/12_cognitive_architecture/codex_local_1108/briefs/OP14_T165). Read anything, but never edit files elsewhere, never use git, never push, post, email or
  create accounts. Nothing you write leaves this folder except when the coordinating agent copies it.
- Compute: every program you run stays under 1 GB of RAM, one thread (set OMP_NUM_THREADS=1), runs at below-normal priority,
  and finishes within 20 minutes per run. No GPU, no torch, no training. This laptop is the author's working computer; never fill its memory and never open a visible window.
- Literature: use the web search tool. Cite only papers you actually opened, with the authors exactly as on the paper or
  its arXiv page. Never invent a reference, a number or a step.
- Save as you go: append to LOG.md after every step (what you did, the command, the output that matters). The account's
  weekly allowance runs out within hours and the session may stop at any moment; LOG.md is what survives.
- Write plainly, like a working mathematician: no hype, no talk about yourself or the process inside PROOF.md.
