# Open problem T073: Phase transition of the noisy majority vote process on Z^2

Statement: In the majority vote process on Z^2 (each site, at rate one, adopts the majority opinion of its four neighbours with probability 1 − ε and the minority with probability ε, ties broken at random), for ε small enough there are at least two distinct stationary measures.

Caveat: The exact update rule used in the literature (neighbourhood, tie-breaking) is to verify.

Source: T. M. Liggett, Interacting Particle Systems (Springer, 1985); L. F. Gray, The positive rates problem for attractive nearest neighbor spin systems on Z, Z. Wahrsch. Verw. Gebiete 61 (1982)

Where it stands (checked by us, Nov 2026): In one dimension attractive nearest-neighbour systems with positive rates are ergodic (Gray 1982). Toom's anisotropic north-east-centre rule is non-ergodic at low noise (Toom 1980). The general positive-rates conjecture fails (Gács, arXiv:math/0003117, J. Stat. Phys. 103 (2001)). On infinite regular trees the noisy majority vote process has several stationary measures at low noise: Bramson and Gray (2021) for degree at least 5, Ding and Huang (arXiv:2501.16202) for degree at least 3; De Gaspari (arXiv:2508.06935) extends this to graphs with suitable expansion. These arguments use expansion and do not reach Z^2. Open for the symmetric majority rule on Z^2.

Earlier work: a previous worker spent one session on this problem. Its folder is ~/codex_op_1114/briefs/T073 (read it,
never edit it). Its REPORT.md is copied below. Read its REPORT.md, LOG.md, PROOF.md and scripts before you start.

Later work: a round 3 worker built on that session. Its folder is ~/codex_op_1114r3/briefs/T073 (read it,
never edit it). Its REPORT.md is copied below. Read its REPORT.md, LOG.md, PROOF.md and scripts before you start.

Later work: a round 4 worker built on that session. Its folder is ~/codex_op_1114r4/briefs/T073 (read it,
never edit it). Its REPORT.md is copied below. Read its REPORT.md, LOG.md, PROOF.md and scripts before you start.

Later work: a round 5 worker built on the latest of these. Its folder is ~/codex_op_1114r5/briefs/T073 (read it, never
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
VERDICT: PARTIAL improved high-noise uniqueness using exactly three disagreements

The round 4 result holds. Independently reconstructed its local inequality,
stationary last-ring argument, all pair and triple clock constants, its
exact root bracket, and its rational endpoint value. The finite check is
in [verify_previous.py](verify_previous.py), with output in
[previous_output.json](previous_output.json).

The new result is uniqueness of all stationary probability measures for
the continuous-time four-neighbor process with fairly resampled ties when

\[
\begin{aligned}
&(2-4\varepsilon)(1-\varepsilon^3/2)
-\frac{17}{630}\varepsilon^4a^4
-\frac4{15}\varepsilon^5a^3
-\frac{16}{81}\varepsilon^6a^3
-\frac{136}{2835}\varepsilon^5a^4<1,\\
&a=1/2-\varepsilon,\qquad 0\le\varepsilon\le1/2.
\end{aligned}
\]

The last term is new. The sufficient threshold is approximately
0.24807560804638594994778149, down from round 4's
0.24807565273432671232676944, a decrease of about
4.46879407624×10⁻⁸. In particular, the whole interval [0.24807562,1/2]
is covered. At its left endpoint the new contraction factor is
0.999999951438061612953781774988235293, whereas the preceding factor is
1.000000132984221050821350907284113492. This is a strict extension of the
preceding sufficient condition. Positive-noise coexistence is unresolved
by this work.

The new ingredient is the exact-three event suggested by the preceding
report. In the stationary ordered coupling, write Dᵧ for disagreement and
d for its density. For each triple A of neighbors of x, let F_A mean that
exactly the neighbors in A disagree. Then

\[
\mathbb P(F_A)\ge\frac{68}{2835}\varepsilon^5a^3d.
\]

Hold a source disagreement at x, force four diagonal helpers to alternating
common values, and transmit disagreement at the selected last rings of the
three receivers. Also force the omitted compass neighbor to a common value.
Its clock has no precedence constraint relative to the seven existing
clocks. There are 2176 admissible orders, giving integrated clock coefficient
2176/9!=17/2835. Four forcing assignments and the conditional transmission
bound a³ yield the displayed estimate. The four F_A partition the event
of three disagreements. Their bounds use the remaining local gap a/2,
producing the new correction 136ε⁵a⁴/2835. The resulting local relation
is an exact identity in every ordered neighbor configuration.

The complete argument, including all preceding bounds needed for the new
criterion, is in [PROOF.md](PROOF.md). Dependence is handled by revealing
selected receiver marks chronologically with all other randomness fixed;
the outside axial inputs can be arbitrary ordered pairs.

Reproduce from this folder:

```sh
OMP_NUM_THREADS=1 nice -n 15 python3 -I -B verify_previous.py > previous_output.json
OMP_NUM_THREADS=1 nice -n 15 python3 -I -B audit.py > audit_stdout.json
```

Both commands exited 0 in under one second. The second also saves
[audit_output.json](audit_output.json). It checks all 81 local ordered
states, all four rotated new-event geometries, 72 transmission cases,
clock counts by permutations and independent recursion, the fence formula,
the explicit source ordering, two integral calculations, two polynomial
constructions, and two root enclosures. Peak resident memory was about
17 MB, with one thread, actual nice 20, and a 30-second CPU limit. The
nice prefix prints `setpriority: Operation not permitted` because the
inherited priority is already 20; each script checks actual nice≥15.

Exact root bounds are

\[
\frac{19193920498167976369215855}{77371252455336267181195264}
<\varepsilon_3<
\frac{38387840996335952738431711}{154742504910672534362390528},
\]

with width 1/154742504910672534362390528. A separate integer polynomial
calculation brackets it between 0.248075608046385949 and
0.248075608046385950.

The initial literature check ended within five minutes and found no later
solution changing the picture. Opened the arXiv pages and full texts of
Jian Ding and Fenglin Huang, *Non-ergodicity for the noisy majority vote
process on trees*, [arXiv:2501.16202](https://arxiv.org/abs/2501.16202),
and Damiano De Gaspari, *Fredrickson–Andersen Model and Noisy Majority Vote
Process on Nonamenable Graphs*,
[arXiv:2508.06935](https://arxiv.org/abs/2508.06935). Their pages still list
the original 2025 versions. Their tree/expansion results and synchronous
retained-tie rule do not establish coexistence for the continuous-time
fair-tie process here. The bounded search cannot establish absence of a
solution or of stronger published uniqueness criteria. No priority or
optimality claim is made.

What failed: no mathematical construction or audit assertion failed in this
extension. The only execution diagnostic was the inherited-nice message
described above. The argument proves no low-noise coexistence, no conclusion
at the sufficient threshold, and no result for retained ties. The finite
audits do not formally verify the infinite-volume or conditional-probability
arguments; those are written out and challenged in [LOG.md](LOG.md).

Next: the present one-site local decomposition has no unused deterministic
gap left. A concrete continuation is to sharpen the transmission bounds:
the axial disagreement case gives 2a rather than a. A new stationary event
bound for that axial disagreement, under the same helper clock constraints,
could improve the coefficient. Any such estimate must respect dependencies
among the selected rings. A separate useful check is whether existing
published uniqueness results already subsume this interval for exactly this
rule. Low-noise coexistence still needs a different argument controlling
large error clusters on Z².

Task: “take the NEXT checkable step on this problem, building on that work”
— 2026-11-15, approximately 07:57 +04 (Asia/Tbilisi).
