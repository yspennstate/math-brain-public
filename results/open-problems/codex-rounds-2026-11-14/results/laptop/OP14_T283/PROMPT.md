# Open problem T283: Uniformly samplable counterexamples to polynomial-time low-degree prediction

Statement: For every fixed integer r>=3, can Mao’s arXiv:2607.20318 counterexample be made uniformly randomized-polynomial-time samplable, without advice? Seek vertex-permutation-invariant planted graph laws P_n whose marginals on every set of at most Theta((log n)^{r-1}) edges are uniform, against Q_n=G(n,1/2), yet which a uniform polynomial-time test strongly distinguishes from Q_n even after independent edge resampling at some fixed positive rate eta_r. The sampler, not merely the distinguisher, must be uniform.

Caveat: This is a named remaining explicitness question, not a claim that all low-degree conjectures are false or a newly established repaired conjecture. The large-noise version and natural structural repairs remain separate questions. The integrator must approve this replacement of the old general conjecture by its precise remaining question.

Source: Mao, arXiv:2607.20318, Section 4 Explicitness; Buhai-Hsieh-Jain-Kothari, arXiv:2505.17360.

Where it stands (checked by us, Nov 2026): 2505.17360 refutes the older quasi-polynomial form. Mao gives polynomial-time binary counterexamples at sufficiently small positive noise but its planted sampler uses advice; Section 4 explicitly leaves a uniform polynomial-time sampler open.

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
- Work only inside this folder (~/brain-repo/12_cognitive_architecture/codex_local_1108/briefs/OP14_T283). Read anything, but never edit files elsewhere, never use git, never push, post, email or
  create accounts. Nothing you write leaves this folder except when the coordinating agent copies it.
- Compute: every program you run stays under 1 GB of RAM, one thread (set OMP_NUM_THREADS=1), runs at below-normal priority,
  and finishes within 20 minutes per run. No GPU, no torch, no training. This laptop is the author's working computer; never fill its memory and never open a visible window.
- Literature: use the web search tool. Cite only papers you actually opened, with the authors exactly as on the paper or
  its arXiv page. Never invent a reference, a number or a step.
- Save as you go: append to LOG.md after every step (what you did, the command, the output that matters). The account's
  weekly allowance runs out within hours and the session may stop at any moment; LOG.md is what survives.
- Write plainly, like a working mathematician: no hype, no talk about yourself or the process inside PROOF.md.
