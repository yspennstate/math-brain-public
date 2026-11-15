# Open problem T076: Random band matrices in dimensions two and three

Statement: For random band matrices indexed by the box {1, …, L}^d, with independent centred entries (up to symmetry) in a fixed symmetry class, H_xy = 0 unless |x − y| ≤ W, and a regular variance profile, bulk eigenvectors are delocalized with Wigner–Dyson local statistics when W ≫ √(log L) in d = 2, and for every W ≥ W_0 with W_0 fixed in d = 3; in d = 2 the localization length is of order exp(cW²).

Source: Y. V. Fyodorov and A. D. Mirlin, Scaling properties of localization in random band matrices: a σ-model approach, Phys. Rev. Lett. 67 (1991); P. Bourgade, Random band matrices, Proc. ICM 2018

Where it stands (checked by us, Nov 2026): d = 1 is settled (T035, retired). Delocalization when W is a power of L: d ≥ 7 (Xu–Yang–Yau–Yin, arXiv:2207.14533: quantum unique ergodicity for complex Gaussian entries when W ≥ L^ε, after Yang–Yau–Yin, arXiv:2104.12048, in d ≥ 8), d = 2 with W ≥ N^c (Dubova–Yang–Yau–Yin, arXiv:2503.07606) and d ≥ 3 with W ≥ N^c (Dubova–Yang–Yau–Yin, arXiv:2507.20274). In d = 2, Lai–Yang (arXiv:2609.24426) reach W ≥ (log N)^7 with localization length at least exp(W^{1/7}). The predicted exp(cW²) scale in d = 2 and bounded W in d = 3 are open.

Earlier work: a previous worker spent one session on this problem. Its folder is ~/codex_op_1114/briefs/T076 (read it,
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
VERDICT: PARTIAL substantial external advance in two-dimensional Gaussian block-band delocalization

The literature check found Lai–Yang, arXiv:2609.24426v4 (8 November 2026),
which improves the bound supplied in the brief. The exact theorem, model,
version comparison, and scale conversion are in
[SOLVED_ELSEWHERE.md](SOLVED_ELSEWHERE.md).
T076 remains open in its full stated form.

Instruction 1 requires stopping upon finding a substantial advance. Accordingly,
no independent proof or computation was attempted and no PROOF.md is supplied.

Verification used the web search tool: the two queries and opened URLs are
recorded in [LOG.md](LOG.md). The v2 and v4 records, full HTML theorem, and
PDF text were checked. The bandwidth and localization-length exponents were
also compared by algebraic inversion, with volume and side length distinguished.
This verifies the reported statement, not all steps of the paper's proof.

No numerical experiment ran. An orientation command using `nice -n 15` reported
a sandbox priority error; subsequent work used read-only document inspection.
PDF screenshots also failed; extracted PDF text remained available.

Next worker: update the problem ledger with the version-specific theorem and
its block-Gaussian restriction, then select a piece addressing the remaining
gap. No claim is made here about dimension-three progress beyond the inspected
sources or about universality at the new two-dimensional threshold.

Task: “push this problem forward by one checkable piece” — 14 November 2026,
approximately 20:52 Asia/Tbilisi.
