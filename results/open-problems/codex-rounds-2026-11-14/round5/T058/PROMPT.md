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
VERDICT: PARTIAL proved a joint Gaussian limit for adjacent independent-set counts on fixed interior phase bands

The round 3 moment result holds. Its main asymptotics were re-derived,
and an independent orthogonal expansion in edge variables reproduces its
exact covariance numerators and largest numerical sample.

The new result upgrades those moments to a joint distributional limit.
Write

\[
 f(n)=2\log_2n-2\log_2\log_2n+2\log_2(e/2)+1,
 \qquad k=\lfloor f(n)\rfloor.
\]

Let X_j count independent j-sets and let mu_j be its mean. For each fixed
0<delta<1/2, uniformly over integers with delta<={f(n)}<=1-delta,

\[
 \left(\frac{X_k-\mu_k}{\sqrt{\mu_k}},
       \frac{X_{k-1}-\mu_{k-1}}{\sqrt{\mu_{k-1}}}\right)
 \xrightarrow{d} N(0,I_2).
\]

[PROOF.md](PROOF.md) proves this with an explicit characteristic-function
bound, of size at most n^(-delta/2+o(1)) at bounded arguments. The proof
uses a monotone size-biased coupling for each marginal and positive
association to bound the joint dependence. It includes both arguments
in full. [AUDIT.md](AUDIT.md) gives a second proof of the joint-independence
step using the nonnegative threshold-covariance kernel and Fatou's lemma.

This resolves the joint-Gaussian question left open in the preceding
local report. It proves no new concentration bound for chi. Neither a
conditional law for chi given the counts nor a sensitivity estimate
relating chi to them is established. No literature-novelty claim is made;
the marginal Poisson behaviour is already discussed by Annika Heckel and
Oliver Riordan in [*How does the chromatic number of a random graph vary?*,
arXiv:2103.14014](https://arxiv.org/html/2103.14014).

Reproduce the checks from this folder:

```sh
OMP_NUM_THREADS=1 nice -n 15 python3 recheck_moments.py
OMP_NUM_THREADS=1 nice -n 15 python3 verify_joint.py
```

Both passed. The first compares exact integer numerators from two
different expansions. At n approximately 2^320.255384, k=625 and phase
.75, it reproduces Var(X_(k-1))/mu_(k-1)-1 =
5.108702812850075e-13 and Cov/(k mu_k)-1 =
8.200165028651807e-16. It also reproduces the earlier slow-convergence
example near 2^80. The run took 15.311 seconds and 25.2 MB peak RSS.

The second enumerates every graph on five and six vertices. It verifies
the entire size-biased distribution, the exact forcing-increment
identities, nonnegativity and normalization of the covariance kernel,
and the characteristic-function inequalities at 49 argument pairs per
joint distribution. Those final complex-number checks use floating
arithmetic; the distributional and kernel checks are exact. The run took
0.111 seconds and 17.3 MB peak RSS. Both scripts report actual nice=20,
despite the inherited-priority launcher diagnostic. Full outputs are in
recheck_moments.json and joint_verification.json; commands and relevant
values are in [LOG.md](LOG.md).

No mathematical check failed. One malformed documentation patch was
rejected before changing files and was reapplied. The finite checks do
not certify an asymptotic cutoff. The theorem concerns weak convergence
on fixed interior bands, not total-variation independence of the raw
counts or endpoint phases. Its error rate concerns characteristic
functions, not Kolmogorov distance.

The bounded literature check found no full solution. A new concrete lead
beyond the earlier report is Robert Morris and Oliver Riordan,
[*Random cliques in random graphs revisited*, arXiv:2504.00964](https://arxiv.org/html/2504.00964v1).
Section 1.3 and Theorem 1.4 describe almost-maximal clique families with
an overlap correction; this is a rigorous ingredient relevant to the
2025 cube-root announcement, but does not give its chromatic
concentration theorem. The precise statement and proof behind that
announcement remain to be obtained. The original brief's density-one
exponent 1/2 still differs from the published phase-dependent Zigzag
Conjecture, as established in the first session.

For a concrete next lemma on the present route, let M_k be the maximum
number of pairwise vertex-disjoint independent k-sets. Try to show
X_k-M_k=o_p(sqrt(mu_k)) on fixed phase bands lying below 2/3. Counting
intersecting pairs is a possible route, but it must include one-vertex
intersections, which do not appear in the covariance calculation. Such
a lemma would transfer the Gaussian fluctuations to a packing statistic;
a further relation to chi would still be needed.

Task: “take the NEXT checkable step on this problem, building on that work” — 15 November 2026, first explicitly recorded local clock 04:30:05 +04.
