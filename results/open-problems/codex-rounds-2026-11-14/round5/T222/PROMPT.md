# Open problem T222: Steele's variance-limit conjecture for the planar Euclidean traveling salesman problem

Statement: Let X_1,...,X_n be independent uniform points in [0,1]^2 and let L_n be the length of the shortest closed Euclidean tour through them. Prove that Var(L_n) converges to a constant as n tends to infinity, and identify that constant if possible.

Caveat: The variance here is unscaled, for the total tour length in the fixed unit square. This is a fluctuation question, distinct from T156, which asks for the constant in the first-order law L_n/sqrt(n). It is not the mean-field traveling salesman model with independent edge costs, and it is not a variance statement about an approximation algorithm. A central limit theorem alone without variance control would not establish the assertion.

Source: S. Chatterjee, A general method for lower bounds on fluctuations of random variables, arXiv:1706.04290, Section 3, open problem (2)

Where it stands (checked by us, Nov 2026): The opened source explains that upper fluctuation bounds are well understood and recalls Rhee's lower bound of the correct order in dimension two. It still poses variance convergence explicitly. The inspected recent papers on finite-temperature mean-field optimization, one-dimensional bipartite tours and neural tour solvers do not establish this planar zero-temperature variance limit. No closing theorem was found in the recorded current-status searches. Open.

Earlier work: a previous worker spent one session on this problem. Its folder is ~/codex_op_1114/briefs/T222 (read it,
never edit it). Its REPORT.md is copied below. Read its REPORT.md, LOG.md, PROOF.md and scripts before you start.

Later work: a round 3 worker built on that session. Its folder is ~/codex_op_1114r3/briefs/T222 (read it,
never edit it). Its REPORT.md is copied below. Read its REPORT.md, LOG.md, PROOF.md and scripts before you start.

Later work: a round 4 worker built on that session. Its folder is ~/codex_op_1114r4/briefs/T222 (read it,
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
VERDICT: PARTIAL a strict geometric improvement of the earlier interaction-energy bound

The variance-limit conjecture is not proved. Both earlier results check
out. The new piece uses spatial continuity of the insertion cost to
strictly improve round 3's constant kappa.

With the earlier notation E_n=sum_j j V_{n,j}, let

\[
 F(c)=c^2+\frac4\pi e^{-\pi c^2}
                  -2c\operatorname{erfc}(\sqrt\pi c),
 \qquad \kappa=F(c_*),\quad c_*=\arg\min_{c\ge0}F(c).
\]

PROOF.md establishes, for every fixed c>0,

\[
 \limsup_n E_n\le
 F(c)-\frac{\pi c^4}{256}e^{-9\pi c^2}.
\]

In particular, defining

\[
 K=\kappa-\frac{\pi c_*^4}{256}e^{-9\pi c_*^2},
\]

gives limsup E_n<=K<kappa. This also replaces kappa by K in the earlier
variance-tail and noise-covariance bounds:

\[
 \limsup_n\sum_{j>m}V_{n,j}\le\frac K{m+1},\qquad
 \limsup_n(\operatorname{Var}(L_n)-C_n(\rho))\le K(1-\rho).
\]

The improvement is explicitly positive; no claim that it is large or
that it beats the best published variance bound is made. K is an upper
bound, not a proposed limiting variance.

The extra geometric input is elementary: x->d(x;S) is 2-Lipschitz,
where d is the optimal tour's insertion cost. Near an isolated base
point, two small disks lie on opposite sides of the threshold R=c/sqrt(n)
in the earlier squared-error envelope. The envelope prefers insertion
cost zero on one disk and 2R on the other. Spatial continuity prevents
simultaneously attaining those choices. The proof quantifies the deficit
on each disk pair, then sums over disjoint neighborhoods of isolated
points. Their exact expected count supplies the factor exp(-9pi c^2).
Boundary strips are treated explicitly. No local rearrangement theorem
for optimal tours is assumed.

This does not contradict round 3's scalar sharpness theorem: that theorem
does not impose spatial continuity. Its discontinuous scalar extremizer
cannot attain the envelope on these isolated neighborhoods.

AUDIT.md rechecks the old constant from truncated exponential moments,
the energy scale with replacement pairs, spatial continuity by a second
detour argument, the local deficit by translating one disk, and the
expected count through the joint density. The translation check even
allows a larger local deficit; the stated constant is conservative and
not optimized. Endpoint fields, coincident locations, n=2, boundary
control, disjointness, and positivity of F(c)-eta(c) were checked. No
mathematical error was found. All calculations are analytic; no simulation,
numerical optimization, or numerical variance estimate was run.

The web search tool was used for a status check lasting less than five
minutes. The opened source was Sourav Chatterjee,
[*A general method for lower bounds on fluctuations of random variables*](https://arxiv.org/html/1706.04290v3),
arXiv:1706.04290v3, Section 3, problem (2). No closing theorem was found
in the recorded searches, so no SOLVED_ELSEWHERE.md was written. This is
not an exhaustive literature review or a claim of novelty relative to
all published variance bounds.

Reproduce the artifact checks with:

```sh
env OMP_NUM_THREADS=1 nice -n 15 /bin/sh -c '
cat PROOF.md AUDIT.md
head -n 1 REPORT.md
wc -l LOG.md PROOF.md AUDIT.md REPORT.md
'
```

LOG.md records the reads, searches, choice, proof, and audit. The sandbox
reports `nice: setpriority: Operation not permitted`; no verified priority
adjustment is claimed. Only short file reads were run. All writes stay
in this folder; no git, subagents, or external messages were used.

What failed or remains uncertain: no fixed-order energy convergence,
fixed-noise covariance limit, variance convergence, or value of a limiting
variance is established. Improving a limsup cannot resolve uniqueness of
subsequential limits. The present continuity argument does not bridge
that gap. No unsuccessful numerical experiments are being omitted.

Next worker: target V_{n,1}=n Var(E[L_n|X_1]), including the boundary,
or fixed-noise covariance convergence. The present lemma also supplies a
concrete spatial constraint for any attempted variational analysis of
insertion fields. Optimizing its disk constants would remain an upper-bound
improvement and would not itself address convergence.

Task: "take the NEXT checkable step on this problem, building on that work"
— T222, 2026-11-15 approximately 05:02 Asia/Tbilisi (task-start estimate).
