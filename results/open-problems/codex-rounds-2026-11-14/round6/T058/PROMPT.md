# Open problem T058: Concentration of the chromatic number of G(n, 1/2)

Statement: Determine the width of concentration of χ(G(n, 1/2)): conjecturally, for a set of n of density one, the shortest interval containing χ(G(n, 1/2)) with probability tending to 1 has length n^{1/2+o(1)}.

Caveat: The exact form of the conjecture (most n versus all n) is to verify.

Source: E. Shamir and J. Spencer, Sharp concentration of the chromatic number on random graphs G_{n,p}, Combinatorica 7 (1987); B. Bollobás, How sharp is the concentration of the chromatic number?, Combin. Probab. Comput. 13 (2004); A. Heckel and O. Riordan, How does the chromatic number of a random graph vary?, J. London Math. Soc. 108 (2023) 1769–1815

Where it stands (checked by us, Nov 2026): Concentration on an interval of length about √n (Shamir–Spencer 1987); not concentrated on fewer than n^{1/4−ε} values for infinitely many n (Heckel, arXiv:1906.11808), improved to n^{1/2−ε} (Heckel–Riordan, J. Lond. Math. Soc. 108 (2023)). The behaviour for typical n is open.

Earlier work: a previous worker spent one session on this problem. Its folder is ~/codex_op_1114/briefs/T058 (read it,
never edit it). Its REPORT.md is copied below. Read its REPORT.md, LOG.md, PROOF.md and scripts before you start.

Later work: a round 3 worker built on that session. Its folder is ~/codex_op_1114r3/briefs/T058 (read it,
never edit it). Its REPORT.md is copied below. Read its REPORT.md, LOG.md, PROOF.md and scripts before you start.

Later work: a round 4 worker built on that session. Its folder is ~/codex_op_1114r4/briefs/T058 (read it,
never edit it). Its REPORT.md is copied below. Read its REPORT.md, LOG.md, PROOF.md and scripts before you start.

Later work: a round 5 worker built on the latest of these. Its folder is ~/codex_op_1114r5/briefs/T058 (read it, never
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
VERDICT: PARTIAL proved that maximum disjoint independent-set packings inherit the Gaussian count fluctuations below phase 2/3

Let
\[
 f(n)=2\log_2n-2\log_2\log_2n+2\log_2(e/2)+1,
 \quad k=\lfloor f(n)\rfloor,
 \quad \mu_k=\binom nk2^{-\binom k2}.
\]
Let X_k count independent k-sets, and let M_k be the maximum number of
pairwise vertex-disjoint independent k-sets. For every fixed
0<a<b<2/3, uniformly when a<={f(n)}<=b,
\[
 \mathbb E\frac{X_k-M_k}{\sqrt{\mu_k}}
 \le (1+o(1))\frac{\mu_k^{3/2}k^2}{2n}
 \le n^{3b/2-1+o(1)}=o(1).
\]
Thus the preceding joint Gaussian limit remains valid with M_k replacing
X_k. M_k may be centered at either mu_k or its own expectation, with
normalization sqrt(mu_k). [PROOF.md](PROOF.md) contains the proof;
[AUDIT.md](AUDIT.md) gives independent counts and checks.

This proves the concrete packing lemma proposed by round 4. The key new
term is one-vertex intersections, which contribute zero to the earlier
covariance but prevent disjointness. If Y counts all intersecting
unordered pairs of independent k-sets, then X_k-M_k<=Y deterministically
and EY~mu_k^2 k^2/(2n) on every fixed interior phase band. This asymptotic
and the resulting packing approximation are the extension beyond the
previous report. No literature-novelty claim is made.

The earlier joint-limit proof was independently re-derived, including
the forcing increment, characteristic-function equation, positive
threshold-covariance kernel and uniform overlap estimate. It holds.
Its exhaustive verification was also rerun successfully from this
folder, writing only local output.

Commands:

```sh
OMP_NUM_THREADS=1 nice -n 15 python3 ~/codex_op_1114r4/briefs/T058/verify_joint.py
OMP_NUM_THREADS=1 nice -n 15 python3 verify_packing.py
OMP_NUM_THREADS=1 nice -n 15 python3 audit_scales.py
```

All runs passed. The exact packing check enumerates every graph on five
and six vertices and every k=2,...,n. Two independent packing algorithms
agree throughout. Pair expectations, incidence double counts, deletion
bounds, large-n overlap recurrences and the proof's convexity bounds
also pass. The run took 153.034 seconds with 41.4 MB peak RSS. The
independent log-space diagnostic reproduces the exact normalized scales
within 3.2e-9 in log10 units and cheaply extends them through log2(n)=2560.
Every script verifies actual nice=20. Outputs are joint_verification.json,
packing_verification.json and scale_audit.json; details are in
[LOG.md](LOG.md).

No mathematical check failed. The numerical audit caught an underflowing
display of tiny error bounds; those are now recorded in logarithmic units.
One documentation patch was rejected before changing files and reapplied.
Convergence can be very slow: at phase 5/8, EY/sqrt(mu_k) is still about
20,003 near n=2^320. The proof supplies no finite cutoff. Values above
phase 2/3 test the method's limitation, not a counterexample to a packing
limit.

The bounded literature check found no full solution. Opened sources were
Annika Heckel and Oliver Riordan,
[*How does the chromatic number of a random graph vary?*, arXiv:2103.14014](https://arxiv.org/html/2103.14014),
and Robert Morris and Oliver Riordan,
[*Random cliques in random graphs revisited*, arXiv:2504.00964](https://arxiv.org/html/2504.00964v1).
The latter concerns distributions of clique families, rather than a full
chromatic concentration theorem. The 2025 cube-root announcement remains
a separate lead whose precise chromatic theorem was not obtained. As the
first local report established, the published conjecture is phase dependent.
Conjecture 10 is stated along all n, with exponent
lambda(n)=max(theta(n),1-theta(n))/2 and theta(n)=log(mu_k)/log(n).
It is not the brief's density-one exponent 1/2 formulation. This was
checked directly in the opened paper.

The chromatic concentration problem remains open in this work. The
packing covers o_p(n) vertices. Its Gaussian fluctuation says nothing
here about the chromatic cost of the remaining graph. No variance
asymptotic for M_k or result at phase 2/3 is asserted. The conflict upper
bound becomes insufficient above 2/3; this does not prove the packing
approximation false there.

Next worker: establish whether the packing loss can be replaced by a
deterministic correction with residual o_p(sqrt(mu_k)) on bands above
2/3. This requires controlling its fluctuations, rather than its mean;
counting intersecting triples or overlapping edges in the conflict graph
is a concrete first test. A separate conditional estimate for the
chromatic number of the unpacked graph is still required to reach chi.
Obtain the exact cube-root theorem before asserting a new chromatic bound.

Task: “take the NEXT checkable step on this problem, building on that work” — 15 November 2026, first recorded local clock 07:45:50 +04.
