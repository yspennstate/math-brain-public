# Open problem T056: Gaboriau's fixed price problem

Statement: Every countable group Γ has fixed price: all free probability-measure-preserving actions of Γ have the same cost.

Source: D. Gaboriau, Coût des relations d'équivalence et des groupes, Invent. Math. 139 (2000)

Where it stands (checked by us, Nov 2026): Fixed price holds for amenable groups (cost 1), free groups, and many classes closed under products and commensurability (Gaboriau 2000); higher-rank semisimple Lie groups and their lattices have fixed price 1 (Fraczyk–Mellick–Wilkens, arXiv:2307.01194, via Poisson–Voronoi tessellations). Open in general.

Earlier work: a previous worker spent one session on this problem. Its folder is ~/codex_op_1114/briefs/T056 (read it,
never edit it). Its REPORT.md is copied below. Read its REPORT.md, LOG.md, PROOF.md and scripts before you start.

Later work: a round 3 worker built on that session. Its folder is ~/codex_op_1114r3/briefs/T056 (read it,
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
VERDICT: PARTIAL independent proof audit of the relative-cost deployment estimate

The next checkable piece is complete: [PROOF.md](PROOF.md) proves

\[
 \operatorname{Cost}(R_{A*_J B})\ge 1+d_X,
 \qquad d_X=\inf\{C(F):R_J\vee F=R_A,\ F\subset R_A\},
\]

for a free pmp action when J is infinite and A*_J B is finitely generated. This verifies the first link in the lower-bound argument of **OpenAI**, *A group without fixed price* (5 October 2026), [deployment proposition](https://github.com/openai/math/blob/main/preprints/A-group-without-fixed-price-October-5-2026/build/deployment.tex). It is an audit of an existing proposition, not an original solution of fixed price.

What is new beyond the earlier report: the earlier worker checked source statements and the conditional separation of two cost bounds. This session supplies a complete proof of the compression and deployment estimate, with the treatment of finite and infinite supplied-relation classes, subdivisions, noninjective projections, and all limiting steps. The proof also gives an explicit counterexample if the infinite-J hypothesis is removed.

The earlier result rechecks correctly at its stated level. Ali Khezeli's *Products of Infinite Countable Groups Have Fixed Price One*, [arXiv:2509.08325v4](https://arxiv.org/html/2509.08325v4), states the product theorem in Theorem 1.1. The OpenAI manuscript's displayed bounds imply strict separation for suitable parameters; this was re-derived with a different alpha and integer M. Neither the earlier report nor this one verifies the unrestricted direct-product proof from scratch. There was no earlier PROOF.md or mathematical script to rerun.

The literature search lasted about one minute, within the five-minute limit. It found no new resolution beyond the two previously reported items. The OpenAI manuscript remains a claimed solution whose remaining lower-bound arguments have not been certified here. No arXiv identifier for it was verified. A theorem about products alone does not settle the general problem, so the earlier report's broader literature-stop rationale was not used to stop this session.

Validation: derive the cost account first by telescoping and then by subtracting saved component mass directly. Both yield c-1+k(S_n). A finite atomic class independently checks the signs and exact amount of the correction. The proof also checks S=T, infinite S-classes, duplicate edge instances, inverse orientations, atoms, nonergodicity, coincident sheet images, and finite J. No flaw was found in the selected estimate.

Commands and source access are recorded in [LOG.md](LOG.md). Local orientation used `pwd`, `rg --files`, and file reads. Final verification used `OMP_NUM_THREADS=1 nice -n 15 /usr/bin/wc -l LOG.md PROOF.md REPORT.md` and the same wrapper for `cat REPORT.md`. No mathematical computation, subagent, git command, or external mutation was used. All deliverables are in this folder; the earlier folder was read only.

What failed: an initial raw-web fetch of the title-page TeX failed; the read-only GitHub connector opened it. The initial PROOF.md read confirmed that the earlier file does not exist. No attempted proof step failed. These access issues do not affect the estimate.

Runtime limitation: the final text-read commands exited zero but `nice` printed `setpriority: Operation not permitted`. Requested priority could not be established; no mathematical computation was launched.

What remains uncertain: the Bernoulli-to-finite-model transfer and the deterministic rank estimate, including the planar lemma, were opened to locate the dependency chain but were not independently verified. Consequently d_X>0 for the manuscript's Bernoulli action and the proposed counterexample remain unproved by this session.

Next worker: audit Proposition `models:transfer` in the manuscript's [finite-models.tex](https://github.com/openai/math/blob/main/preprints/A-group-without-fixed-price-October-5-2026/build/finite-models.tex). In particular, check equivariance of the finite label configurations, inverse-step domain tests, and the assertion that the selected cocycle values generate every x_v. If that holds, the deterministic rank theorem and its coefficient-sensitive planar lemma remain the final link. Do not infer d_X>0 from the deployment estimate alone.

Task: “take the NEXT checkable step on this problem, building on that work” — 15 November 2026, 01:01 Asia/Tbilisi (work-start clock; exact prompt-arrival time unavailable).
