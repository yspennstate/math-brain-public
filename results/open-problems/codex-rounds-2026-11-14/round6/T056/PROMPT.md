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

Later work: a round 5 worker built on the latest of these. Its folder is ~/codex_op_1114r5/briefs/T056 (read it, never
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
VERDICT: PARTIAL proof audit of expanding asymptotically free finite models

[PROOF.md](PROOF.md) establishes Proposition `models:sequence` in **OpenAI**, *A group without fixed price* (5 October 2026), [finite-models.tex](https://github.com/openai/math/blob/main/preprints/A-group-without-fixed-price-October-5-2026/build/finite-models.tex). This is the next dependency named by round 4, following its Bernoulli-to-finite-model transfer. It is an audit of an intermediate proposition, not a solution of fixed price. No arXiv identifier for that manuscript was verified.

New beyond round 4: a complete construction of one sequence of finite exact A-actions that is asymptotically free, satisfies |N(T)|>96|T| for every 1<=|T|<=alpha*n, and has o(n) bad rows. The proof includes the free-basis substitution, inverse permutation exposure, nonidentity overlap certificates including u_0=1, and simultaneous choice of all constraints.

The audit also gives quantitative bounds beyond the source's qualitative existence argument. For its random n-point models,

\[
\Pr(\text{expansion fails})\le\frac{52K}{n^3},
\qquad
\mathbb E b(V)\le\frac{10Qn}{n-3},
\quad Q=100\cdot99+100^4,
\]

where K=e^96*96^99/95^95, n>=4, and the source's parameter assumptions hold. Thus the expected number of bad rows is bounded as n grows. Equation (4) combines these bounds with any finite list of fixed-word constraints; (17) gives an explicit sufficient size for simultaneous success. No computation is needed.

Round 4's main transfer inequality rechecks correctly. A single generating-list counting function recovers its finite error estimate, with the correct inverse source and collision word. The derivation and limit order are recorded in [LOG.md](LOG.md). All three earlier folders were read without modification; none contains mathematical scripts, and the first has no PROOF.md.

Validation: the expansion exponent and constant were checked by separate counts. The cubic geometric-series sum was derived two ways; at q=1/2 its falling-factorial contributions are 24+24+4=52. Overlap nonidentity was checked both by reduced-word uniqueness and by the zero-index cases. Word exposure, sufficient size conditions, repeated columns, nontransitive actions and growing word lengths on the diagonal were checked separately. No flaw was found in the selected proposition.

The literature check took less than five minutes and found no later established resolution beyond the manuscript already reported. The bounded search does not certify absence of other work. No new SOLVED_ELSEWHERE.md is warranted. The claimed counterexample remains unaudited at its rank/planar step.

Commands and source reads are in LOG.md. Shell reads used `OMP_NUM_THREADS=1 nice -n 15`; the sandbox consistently printed `nice: setpriority: Operation not permitted`, so requested priority was not established. No numerical workload, subagent, git command, background process or external write was used. All deliverables are in this folder.

What failed: a guessed parameters.tex source path was unavailable. No mathematical argument failed. What remains uncertain: the deterministic rank lower bound and coefficient-sensitive planar lemma. The proof's certificate-count constant Q is intentionally coarse; optimizing it would not resolve those dependencies.

Next worker: audit Theorem `rank:main` in [rank-surgery.tex](https://github.com/openai/math/blob/main/preprints/A-group-without-fixed-price-October-5-2026/build/rank-surgery.tex), especially its use of Lemma `planar:main` in [planar.tex](https://github.com/openai/math/blob/main/preprints/A-group-without-fixed-price-October-5-2026/build/planar.tex). Check the coefficient-group embedding, extraction of a long matching segment with equal coefficient gaps, and the graph-shortening move. The present sequence eventually meets alpha*n>=1 and 100b<=alpha*n, so model existence is no longer the missing hypothesis. A rank bound still must be proved before inferring d_X>0.

Task: “take the NEXT checkable step on this problem, building on that work” — 15 November 2026, 07:45 Asia/Tbilisi (work-start clock; exact prompt-arrival time unavailable).
