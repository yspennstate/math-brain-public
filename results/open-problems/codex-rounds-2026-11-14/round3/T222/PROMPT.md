# Open problem T222: Steele's variance-limit conjecture for the planar Euclidean traveling salesman problem

Statement: Let X_1,...,X_n be independent uniform points in [0,1]^2 and let L_n be the length of the shortest closed Euclidean tour through them. Prove that Var(L_n) converges to a constant as n tends to infinity, and identify that constant if possible.

Caveat: The variance here is unscaled, for the total tour length in the fixed unit square. This is a fluctuation question, distinct from T156, which asks for the constant in the first-order law L_n/sqrt(n). It is not the mean-field traveling salesman model with independent edge costs, and it is not a variance statement about an approximation algorithm. A central limit theorem alone without variance control would not establish the assertion.

Source: S. Chatterjee, A general method for lower bounds on fluctuations of random variables, arXiv:1706.04290, Section 3, open problem (2)

Where it stands (checked by us, Nov 2026): The opened source explains that upper fluctuation bounds are well understood and recalls Rhee's lower bound of the correct order in dimension two. It still poses variance convergence explicitly. The inspected recent papers on finite-temperature mean-field optimization, one-dimensional bipartite tours and neural tour solvers do not establish this planar zero-temperature variance limit. No closing theorem was found in the recorded current-status searches. Open.

Earlier work: a previous worker spent one session on this problem. Its folder is ~/codex_op_1114/briefs/T222 (read it,
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
VERDICT: PARTIAL quantitative finite-order reduction of the planar TSP variance-limit conjecture

The conjecture is not proved and its constant is not identified. The
completed piece is a reduction, with explicit errors, for the exact optimal
closed tour through uniform points in the fixed unit square.

Let V_{n,j} be the sum of squared norms of the order-j Hoeffding components
of L_n, defined explicitly in PROOF.md. The proof establishes

\[
 \operatorname{Var}(L_n)=\sum_{j\ge1}V_{n,j},\qquad
 \sum_{j\ge1}jV_{n,j}\le8,\qquad
 \limsup_{n\to\infty}\sum_{j\ge1}jV_{n,j}\le\frac4\pi.
\]

Thus the variance contributed by orders greater than m is at most
8/(m+1) for every n, and its limit superior is at most 4/[pi(m+1)].
Variance cannot escape to interaction orders tending to infinity.
If each fixed-order V_{n,j} converges to v_j, then the conjectured variance
limit exists and equals sum_j v_j, with sum_j j v_j <= 4/pi. No
fixed-order convergence is proved here.

An alternative sufficient condition uses coupled optimal tours. Independently
retain each point with probability rho and otherwise replace it uniformly,
and write C_n(rho) for the covariance of the original and modified tour
lengths. Then

\[
 C_n(\rho)=\sum_j\rho^jV_{n,j},\qquad
 0\le\operatorname{Var}(L_n)-C_n(\rho)\le8(1-\rho).
\]

It suffices to establish convergence of C_n(rho_r) for each member of any
fixed sequence rho_r increasing to one. The proof also expresses V_{n,j}
by binomial inversion of covariances of two n-point tours sharing exactly
k points, for k <= j. These are standard product-space tools applied with
explicit geometric bounds; no novelty claim for the decomposition or
improvement of known variance upper bounds is made.

The geometric input was checked independently: insertion costs at most
twice the nearest-neighbor distance, E[R^2] <= 2/n uniformly up to the
square's boundary, and n E[R^2] -> 1/pi after averaging the inserted point.
PROOF.md gives all steps. AUDIT.md checks the constants a second way,
checks the identities on exact two-site Euclidean tours, and gives
oscillating examples showing why the bounds alone do not prove convergence.

The literature search used the web search tool and ended within ten
minutes. Opened sources were Sourav Chatterjee,
[*A general method for lower bounds on fluctuations of random variables*](https://arxiv.org/html/1706.04290v3),
arXiv:1706.04290; Zhuolun Dong and Junyu Cao,
[*New Bounds for the Euclidean TSP Constant*](https://arxiv.org/abs/2610.02809),
arXiv:2610.02809; and Julia Gaudio and Charlie K. Guan,
[*An Improved Upper Bound for the Euclidean TSP Constant Using Band Crossovers*](https://arxiv.org/abs/2602.11250),
arXiv:2602.11250. The latter two concern the first-order constant. No
closing theorem was found in the recorded searches; this is not a claim of
an exhaustive literature review. No SOLVED_ELSEWHERE.md was warranted.

No numerical computation or simulation was run. The checks are exact
analytic calculations, so there is no generated numerical dataset or
script command to reproduce. LOG.md records the web queries and shell
reads. The principal read-back command was:

```sh
env OMP_NUM_THREADS=1 nice -n 15 /bin/sh -c '
wc -l LOG.md PROOF.md AUDIT.md
sed -n "1,110p" PROOF.md
sed -n "240,390p" PROOF.md
cat ~/.claude/compute/compute_state.json
'
```

The sandbox printed `nice: setpriority: Operation not permitted`; process
inspection was denied too. Consequently no priority setting is claimed as
verified. Only short file reads were executed. All artifacts were written
inside this folder, without git, external writes, or subagents.

What failed or remains uncertain: no stabilization theorem for optimal
tour insertion costs was obtained; neither fixed-order nor fixed-noise
convergence was established; no limiting constant, positivity result, or
rate of variance convergence follows. Ordinary local convergence of the
input point process does not establish the missing statements. In the
shared-point covariance formula, a factor binom(n,j) amplifies errors, so
unscaled covariance convergence alone is insufficient. An attempted SSRN
open was denied and was not used. The reduction's novelty relative to the
full existing literature has not been established.

Next worker: choose one of the two remaining geometric limits. A concrete
starting target is V_{n,1}=n Var(E[L_n|X_1]); analyze its dependence on the
location of the conditioned point, including the boundary. Alternatively,
seek a covariance limit for two tours at a fixed positive resampling
fraction. The explicit uniform errors above justify the final truncation
or zero-noise passage once those limits are available. Do not assume that
a nearby insertion competitor implies local rearrangement of the optimum.

Task: "push this problem forward by one checkable piece" — T222,
2026-11-14 approximately 21:20 Asia/Tbilisi.
