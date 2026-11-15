# Open problem T056: Gaboriau's fixed price problem

Statement: Every countable group Γ has fixed price: all free probability-measure-preserving actions of Γ have the same cost.

Source: D. Gaboriau, Coût des relations d'équivalence et des groupes, Invent. Math. 139 (2000)

Where it stands (checked by us, Nov 2026): Fixed price holds for amenable groups (cost 1), free groups, and many classes closed under products and commensurability (Gaboriau 2000); higher-rank semisimple Lie groups and their lattices have fixed price 1 (Fraczyk–Mellick–Wilkens, arXiv:2307.01194, via Poisson–Voronoi tessellations). Open in general.

Earlier work: a previous worker spent one session on this problem. Its folder is ~/codex_op_1114/briefs/T056 (read it,
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
VERDICT: PARTIAL literature update locating a reported counterexample and an unrestricted direct-product theorem

Instruction 1 applies: substantial progress beyond the supplied status was found, so no new special case or computation was started. References and precise scopes are in [SOLVED_ELSEWHERE.md](SOLVED_ELSEWHERE.md).

Ali Khezeli's arXiv:2509.08325v4, revised 4 January 2026, states fixed price one for the product of any two infinite countable groups. The abstract and full-text Theorem 1.1 agree. This is sufficient for the requested literature-stop branch.

OpenAI's *A group without fixed price* (5 October 2026) additionally claims a finitely generated counterexample. Its primary TeX theorem and conclusion were opened and checked for agreement. The cost separation follows algebraically from the stated bounds; the difficult lower bound was not audited. No arXiv identifier was verified for this manuscript, and this report does not certify its proof.

No new theorem was proved or computation performed. Web searches and primary-source URLs, along with failed access attempts, are recorded in [LOG.md](LOG.md). Searches began at 16:47 UTC and the decisive sources were opened by about 16:50 UTC on 14 November 2026.

Local commands were read-only orientation commands (`pwd`, `rg --files`, `ls -la`, reading the memory index and compute JSON). The short Python read used `OMP_NUM_THREADS=1 nice -n 15 python3 -c ...`; nice reported `Operation not permitted`. Process inspection with `ps -o pid,ppid,ni,comm -p $$ -p $PPID` was also denied. No computational script was run. All created files are in this folder; no git or external mutations were used.

What failed: direct PDF text access and two guessed TeX paths. Listing the primary repository's directory with the read-only GitHub connector exposed the correct source paths. What remains uncertain: validity of the counterexample's full lower-bound proof and its independent review status. The next worker should audit the relative-cost compression, passage to finite permutation models, and deterministic rank estimate before declaring the general problem settled. The direct-product update should be included regardless.

Task: “push this problem forward by one checkable piece” — 14 November 2026, 20:47 Asia/Tbilisi (work-start clock; exact prompt-arrival time unavailable).
