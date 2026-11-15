# Open problem T073: Phase transition of the noisy majority vote process on Z^2

Statement: In the majority vote process on Z^2 (each site, at rate one, adopts the majority opinion of its four neighbours with probability 1 − ε and the minority with probability ε, ties broken at random), for ε small enough there are at least two distinct stationary measures.

Caveat: The exact update rule used in the literature (neighbourhood, tie-breaking) is to verify.

Source: T. M. Liggett, Interacting Particle Systems (Springer, 1985); L. F. Gray, The positive rates problem for attractive nearest neighbor spin systems on Z, Z. Wahrsch. Verw. Gebiete 61 (1982)

Where it stands (checked by us, Nov 2026): In one dimension attractive nearest-neighbour systems with positive rates are ergodic (Gray 1982). Toom's anisotropic north-east-centre rule is non-ergodic at low noise (Toom 1980). The general positive-rates conjecture fails (Gács, arXiv:math/0003117, J. Stat. Phys. 103 (2001)). On infinite regular trees the noisy majority vote process has several stationary measures at low noise: Bramson and Gray (2021) for degree at least 5, Ding and Huang (arXiv:2501.16202) for degree at least 3; De Gaspari (arXiv:2508.06935) extends this to graphs with suitable expansion. These arguments use expansion and do not reach Z^2. Open for the symmetric majority rule on Z^2.

Earlier work: a previous worker spent one session on this problem. Its folder is ~/codex_op_1114/briefs/T073 (read it,
never edit it). Its REPORT.md is copied below. Read its REPORT.md, LOG.md, PROOF.md and scripts before you start.

Later work: a round 3 worker built on that session. Its folder is ~/codex_op_1114r3/briefs/T073 (read it,
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
VERDICT: PARTIAL strictly improved high-noise uniqueness criterion for the continuous-time fair-tie process on Z^2

The earlier result holds. Independently re-derived its stationary last-ring
argument and checked all 81 ordered local pairs, its integral, its endpoint
value, and its exact root bracket with verify_previous.py.

The new result is uniqueness of the stationary measure whenever

\[
(2-4\varepsilon)(1-\varepsilon^3/2)
 -\frac{17}{630}\varepsilon^4(1/2-\varepsilon)^4<1,
\qquad 0\le\varepsilon\le1/2.
\]

Its threshold is approximately 0.248076820004086075039, compared with the
earlier 0.248076921333013. The improvement is approximately 1.01328926e-7.
In particular, the whole interval [0.24807685,0.5] is now covered. At its
left endpoint the new contraction factor is approximately
0.99999987814192776, whereas the earlier factor is
1.00000028978957623. Thus this is a strict extension of the preceding
result, although a small one. The low-noise coexistence problem remains
unresolved by this work.

The new ingredient is a stationary three-neighbor disagreement bound.
Writing a=1/2-epsilon and d for the disagreement density in the ordered
stationary coupling, every triple A of neighbors of x satisfies

\[
\mathbb E\prod_{y\in A}D_y
 \ge\frac{17}{1260}\varepsilon^4a^3d.
\]

A disagreement at x is held while four diagonal sites are forced to
alternating common values. Each selected neighbor then has one common 0,
one common 1, the disagreeing center, and an arbitrary ordered axial input.
Its last update produces a disagreement with conditional probability at
least a. The required seven-clock partial order has 272 linear extensions;
its last-source-ring integral contributes 272/8!. Iterated conditional
expectation handles dependence among the selected updates. Counting the
unused local slack when three or four neighbors disagree then yields the
subtracted term above. The complete, self-contained proof is in
[PROOF.md](PROOF.md).

Reproduce from this folder:

```sh
OMP_NUM_THREADS=1 nice -n 15 python3 -I -B verify_previous.py
OMP_NUM_THREADS=1 nice -n 15 python3 -I -B audit.py
```

Both commands exited 0 in under one second. The second saves
[audit_output.json](audit_output.json). It checks all 81 ordered local
pairs, reconstructs the update rule independently, checks all three axial
input cases and the rotated helper geometry, counts 272 by three methods,
and verifies the clock integral and all numerical claims by exact rational
arithmetic. Factored and expanded contraction formulas agree. Exact root
bounds are

\[
\frac{146438707495522750369}{590295810358705651712}
 < e_1 <
\frac{1171509659964182002953}{4722366482869645213696},
\]

with width 1/4722366482869645213696. Independent decimal-grid sign checks
also bracket the root. Measured peak memory was approximately 16 MB, with
one thread and a 30-second CPU limit. The worker inherited nice 20; the
requested nice prefix prints `setpriority: Operation not permitted` on this
Mac because priority is already 20. Both scripts check actual nice >=15
before the audit.

The initial literature check finished within five minutes. No solution
changing the earlier picture was located. Opened the arXiv pages and full
texts of Jian Ding and Fenglin Huang, *Non-ergodicity for the noisy majority
vote process on trees*, [arXiv:2501.16202](https://arxiv.org/abs/2501.16202),
and Damiano De Gaspari, *Fredrickson Andersen Model and Noisy Majority Vote
Process on Nonamenable Graphs*,
[arXiv:2508.06935](https://arxiv.org/abs/2508.06935). The pages still list
only their 2025 first versions. Their results concern trees and suitable
expansion, respectively. Also opened G. Gielis, C. Maes, K. Vande Velde,
*Randomly interacting particle systems: The uniqueness regime*, Annales
de l'I. H. P., section A 70 (1999), 445–472,
[full text](https://www.numdam.org/item/AIHPA_1999__70_5_445_0.pdf).
The short check did not establish a directly comparable numerical bound
for the exact homogeneous continuous-time fair-tie rule. No assertion of
literature novelty or optimality is made.

Failures and uncertainty: no audit assertion failed. A speculative v2 URL
for De Gaspari returned 404. Requiring all four neighboring disagreements
gave a weaker local correction; the saved proof uses triples. The audit
cannot formally verify the infinite-volume or conditional-probability
arguments; these are proved in writing and challenged in
[LOG.md](LOG.md). No low-noise coexistence proof, conclusion at the new
threshold, or result for retained ties was obtained. The brief literature
check cannot establish the absence of a solution or of stronger published
high-noise bounds.

The next worker should first check whether published uniqueness criteria
already imply this interval for exactly rule (1). Within this local method,
the remaining two-disagreement slack is a concrete next target: when two
neighbors disagree and the other two are common and equal, the local gap
is a. Seek a dependence-correct lower bound for that event weighted by
disagreement. The present coefficient also leaves half the three-neighbor
slack unused. Improving these local bounds would still address high-noise
uniqueness; low-noise coexistence requires a different argument controlling
large error clusters on Z^2.

Task: “take the NEXT checkable step on this problem, building on that work”
— 2026-11-15, 01:09 +04 (Asia/Tbilisi).
