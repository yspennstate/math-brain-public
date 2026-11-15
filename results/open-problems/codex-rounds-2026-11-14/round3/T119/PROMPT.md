# Open problem T119: The independence ratio of random cubic graphs

Statement: Determine the constant α_3 such that the independence number of a uniformly random 3-regular graph on n vertices, divided by n, converges in probability to α_3.

Caveat: The limit exists (Bayati–Gamarnik–Tetali 2013). The one-step replica-symmetry-breaking prediction is α_3 ≈ 0.4509 (Barbier–Krzakala–Zdeborová–Zhang, J. Phys. Conf. Ser. 473 (2013), the value 0.45086).

Source: N. C. Wormald, Models of random regular graphs, in Surveys in Combinatorics 1999 (Cambridge Univ. Press, 1999) 239–298; J. Ding, A. Sly and N. Sun, Maximum independent sets on random regular graphs, Acta Math. 217 (2016)

Where it stands (checked by us, Nov 2026): Bounds: α_3 ≥ 0.44533 (Csóka, arXiv:1602.02747, a local algorithm on large-girth graphs) and α_3 ≤ 0.45537 (McKay, Ars Combin. 23A (1987)). The one-step formula is proved for all d ≥ d_0 with d_0 large (Ding–Sly–Sun, arXiv:1310.4787), which does not reach d = 3. d = 3 is open.

Earlier work: a previous worker spent one session on this problem. Its folder is ~/codex_op_1114/briefs/T119 (read it,
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
VERDICT: PARTIAL substantial published improvement located; exact constant unresolved

The literature check found [Viktor Harangi, arXiv:2204.01353v4](https://arxiv.org/abs/2204.01353v4),
published in 2023. The supplied status omits its improved upper bounds.
See [SOLVED_ELSEWHERE.md](SOLVED_ELSEWHERE.md) for the precise statement and
reference. No new mathematical result is claimed.

Search queries, opened sources and verification details are in
[LOG.md](LOG.md). Used the web tool to search, open, find and inspect the PDF.
No numerical computation was performed. A read-only orientation command's
`nice -n 15` request failed with `setpriority: Operation not permitted`;
no computational experiment followed.

The bound was checked across the paper's tables, theorem and published
version; its numerical evaluation was not independently reproduced.
The lower bound in the brief was not audited. No exhaustive claim about the
latest literature is made: the substantial advance already triggers step 1's
instruction to stop.

Next worker: update the brief, then independently certify the explicit
four-atom witness with interval arithmetic before attempting a new bound.

Task: “push this problem forward by one checkable piece.” Session opened
14 November 2026, approximately 22:00 Asia/Tbilisi (first recorded shell
clock: 22:01:17).
