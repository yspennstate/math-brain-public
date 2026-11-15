# Open problem T056: Gaboriau's fixed price problem

Statement: Every countable group Γ has fixed price: all free probability-measure-preserving actions of Γ have the same cost.

Source: D. Gaboriau, Coût des relations d'équivalence et des groupes, Invent. Math. 139 (2000)

Where it stands (checked by us, Nov 2026): Fixed price holds for amenable groups (cost 1), free groups, and many classes closed under products and commensurability (Gaboriau 2000); higher-rank semisimple Lie groups and their lattices have fixed price 1 (Fraczyk–Mellick–Wilkens, arXiv:2307.01194, via Poisson–Voronoi tessellations). Open in general.

Earlier work: a previous worker spent one session on this problem. Its folder is ~/codex_op_1114/briefs/T056 (read it,
never edit it). Its REPORT.md is copied below. Read its REPORT.md, LOG.md, PROOF.md and scripts before you start.

Later work: a round 3 worker built on that session. Its folder is ~/codex_op_1114r3/briefs/T056 (read it,
never edit it). Its REPORT.md is copied below. Read its REPORT.md, LOG.md, PROOF.md and scripts before you start.

Later work: a round 4 worker built on that session. Its folder is ~/codex_op_1114r4/briefs/T056 (read it,
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
VERDICT: PARTIAL proof audit of the Bernoulli-to-finite-model transfer inequality

[PROOF.md](PROOF.md) proves the next step named by round 3:

\[
d_X\geq\limsup_k\frac{\operatorname{rk}(D_{V_k})}{|V_k|}
\]

for every asymptotically free sequence of finite exact right A-sets. This verifies Proposition `models:transfer` in **OpenAI**, *A group without fixed price* (5 October 2026), [finite-models.tex](https://github.com/openai/math/blob/main/preprints/A-group-without-fixed-price-October-5-2026/build/finite-models.tex). It is an audit of an existing proposition, not a solution of the general fixed-price problem. No arXiv identifier for this manuscript was verified.

New beyond round 3: a complete transfer proof, including the group-label cocycle, inverse-domain tests, exact equivariance of label configurations, and generation of every x_v. It also records the finite estimate

\[
\frac{\operatorname{rk}(D_V)}{|V|}
\leq C(\mathcal E)+p+
\sum_{\ell\in I}(1+m_\ell)\Delta_\ell
+(|I|+1)\beta_V(F).
\]

Here p is uncovered path measure, Delta_l is cylinder-approximation error, m_l counts path occurrences, and beta_V(F) is the fraction of sources with coordinate collisions. These quantities are defined in PROOF.md. The estimate exposes the limit order and needs no concentration argument.

The earlier deployment result rechecks correctly. A separate saved-cost ledger and an invariant C_n-k(S_n) both give the residual cost c-1+k(S_n); normal-form recovery and the infinite-J limit also survive inspection. There were no earlier mathematical scripts to rerun. Both earlier folders were read without modification.

Validation: the weighted approximation error and collision coefficient were each derived two ways. An explicit inverse path with g=b_1 a^{-1} checks the source vg^{-1}. The trivial one-point action gives D_V cyclic of order 100 and configurations with colliding coordinates; this checks why endpoint pairs cannot replace group labels and why a collision error is needed. Stabilizers, repeated vertices, nontransitive finite actions, and configurations outside the original free conull subset cause no gap in the argument. No flaw was found in the selected proposition.

The literature search took under five minutes and found no later established resolution beyond the manuscript already reported. Ali Khezeli's [arXiv:2509.08325v4](https://arxiv.org/abs/2509.08325) was opened to check its metadata; the product theorem does not settle all groups. The bounded search does not certify absence of other work.

Commands and source reads are in [LOG.md](LOG.md). Local commands were small text reads and inventories, with `OMP_NUM_THREADS=1 nice -n 15`; final checks used `cat` and `wc -l` on the deliverables. No mathematical computation was needed. The sandbox consistently printed `nice: setpriority: Operation not permitted`, so requested priority was not established; no numerical workload was launched. No subagents, git, external writes, or background processes were used.

What failed: one guessed source path, actions.tex, returned 404; the directory listing supplied group-actions.tex. One log-append patch had mismatched context and was corrected. No proof attempt failed. The expanding-sequence construction and positive normalized-rank bound remain unaudited. This session establishes no positive cost gap and does not certify the proposed counterexample.

Next worker: audit Proposition `models:sequence` in the same finite-models.tex, especially simultaneous asymptotic freeness, the expansion union bound, and the nonidentity words detecting row overlaps. Then audit the deterministic rank estimate and its coefficient-sensitive planar lemma in rank-surgery.tex and planar.tex. A positive rank bound is still needed before inferring d_X>0.

Task: “take the NEXT checkable step on this problem, building on that work” — 15 November 2026, 04:27 Asia/Tbilisi (work-start clock; exact prompt-arrival time unavailable).
