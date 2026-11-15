# Open problem T116: Worst-case trace reconstruction

Statement: An unknown binary string x of length n is observed through independent traces, each obtained by deleting every bit independently with probability q ∈ (0, 1). Determine the order of the number of traces needed to reconstruct every x with high probability; in particular decide whether polynomially many traces suffice.

Caveat: For a uniformly random x far fewer traces are needed, exp(O(log^{1/3} n)) (Holden–Pemantle–Peres–Zhai 2020); for the worst case the gap is now between polynomial and quasipolynomial bounds.

Source: T. Batu, S. Kannan, S. Khanna and A. McGregor, Reconstructing strings from random traces, Proc. SODA 2004; F. Nazarov and Y. Peres, Trace reconstruction with exp(O(n^{1/3})) samples, Proc. STOC 2017

Where it stands (checked by us, Nov 2026): exp(O(n^{1/3})) traces suffice (De–O'Donnell–Servedio 2017; Nazarov–Peres 2017), improved to exp(Õ(n^{1/5})) (Chase 2021) and then to quasipolynomially many, for every retention probability at least 1/polylog n (Burudgunte–Valiant–Wang, arXiv:2607.04073). The best lower bound is Ω̃(n^{3/2}) (Chase, Ann. Inst. Henri Poincaré Probab. Stat. 57 (2021)), after n^{5/4} (Holden–Lyons, Ann. Appl. Probab. 30 (2020)). Whether polynomially many traces suffice is open.

Earlier work: a previous worker spent one session on this problem. Its folder is ~/codex_op_1114/briefs/T116 (read it,
never edit it). Its REPORT.md is copied below. Read its REPORT.md, LOG.md, PROOF.md and scripts before you start.

Later work: a round 3 worker built on that session. Its folder is ~/codex_op_1114r3/briefs/T116 (read it,
never edit it). Its REPORT.md is copied below. Read its REPORT.md, LOG.md, PROOF.md and scripts before you start.

Later work: a round 4 worker built on that session. Its folder is ~/codex_op_1114r4/briefs/T116 (read it,
never edit it). Its REPORT.md is copied below. Read its REPORT.md, LOG.md, PROOF.md and scripts before you start.

Later work: a round 5 worker built on the latest of these. Its folder is ~/codex_op_1114r5/briefs/T116 (read it, never
edit it). Its REPORT.md is copied below. Read its REPORT.md, LOG.md, PROOF.md and scripts before you start.

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
VERDICT: PARTIAL independently audited the common-reference testing step in the reported resolution

The earlier literature result holds as a report of OpenAI's September 24, 2026 preprint: it claims a superpolynomial worst-case sample lower bound at every fixed deletion probability. SOLVED_ELSEWHERE.md records its precise scope and identifier status. The exact order remains unsettled. The literature-stop branch applies; no separate research extension was attempted.

New beyond round 4: opened the actual Testing, Restoration and Induction modules. The implementation handles arbitrarily small fixed success using an injective family close to one common law; this differs from the manuscript's posterior-factorization argument. PROOF.md independently proves its elementary testing inequality in two ways and checks degenerate cases. AUDIT.md identifies the relevant source locations and the common deletion kernel. This closes a narrow final-inference audit, conditional on the construction's estimates, not the full verification gap.

Commands: web searches and opened primary sources are in LOG.md. Local Python checks use `OMP_NUM_THREADS=1 nice -n 15 python3 -B`; effective nice is 20. No numerical computation, Lean build, git, subagents, messages or writes outside this folder.

Failures and uncertainties: the pinned-source URL and two incorrectly prefixed module URLs failed; corrected moving-main paths work. No arXiv identifier or immutable source revision established. Neither dependency closure nor accepted axioms were checked. Hard-family existence and its quantitative estimates remain unverified; the proof here assumes them.

Next worker: obtain an immutable release snapshot and check the quantitative construction and comparator in a resource-compliant environment. The elementary common-reference testing lemma is now checked; repeating only the literature search or comparator statement audit adds little.

Task: “take the NEXT checkable step on this problem, building on that work.” — T116, November 15, 2026, 08:22 Asia/Tbilisi.
