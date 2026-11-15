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
VERDICT: PARTIAL improved high-noise uniqueness by bounding the two-disagreement slack

The round 3 result holds. Re-derived its local inequality, stationary
last-ring argument, and dependence calculation, and independently checked
all 81 ordered local pairs, the 272 clock orders, the coefficient
17/1260, and its exact threshold bracket with verify_previous.py.

The new result is uniqueness of all stationary probability measures for
the continuous-time four-neighbor process with fairly resampled ties when

\[
(2-4\varepsilon)(1-\varepsilon^3/2)
-\frac{17}{630}\varepsilon^4a^4
-\frac4{15}\varepsilon^5a^3
-\frac{16}{81}\varepsilon^6a^3<1,
\qquad a=1/2-\varepsilon,\quad 0\le\varepsilon\le1/2.
\]

The sufficient threshold is approximately 0.24807565273432671232676944,
compared with round 3's 0.248076820004086075039. The decrease is about
0.00000116726975936. In particular, the whole interval [0.248076,1/2]
is covered. At its left endpoint the new contraction factor is
0.999998589222393672254804273783232806, while the round 3 factor is
1.000003331257626955193313049185227268. This is a strict extension of
the preceding result. The original low-noise coexistence problem is
unresolved by this work.

The new ingredient is exactly the two-disagreement event proposed in
the preceding report. For an unordered pair A of neighbors of x, let E_A
mean that those two sites disagree in the stationary ordered coupling,
while the other two neighbors are common and equal. With disagreement
density d, the new estimates are

\[
\mathbb P(E_A)\ge
\begin{cases}
\varepsilon^5a^2d/15,& A\text{ consists of adjacent compass directions},\\
8\varepsilon^6a^2d/81,& A\text{ consists of opposite directions}.
\end{cases}
\]

Hold a disagreement at the center, use opposite-valued diagonal helpers
to transmit it to the two selected neighbors, and force the remaining
neighbors to a common value. Adjacent and opposite pairs require three
and four helpers respectively. Their admissible last-ring clock counts
are 672 and 4480; integration over the last source ring gives 1/60 and
1/81. Summing four adjacent and two opposite pair bounds accounts for
the two new terms. Their local slack does not overlap the previous
triple correction. The complete proof is in [PROOF.md](PROOF.md).

Reproduce from this folder:

```sh
OMP_NUM_THREADS=1 nice -n 15 python3 -I -B verify_previous.py
OMP_NUM_THREADS=1 nice -n 15 python3 -I -B audit.py
```

Both commands exit 0 in under one second. The latter saves
[audit_output.json](audit_output.json), including exact arithmetic,
all 81 local cases, all six pair geometries, twelve receiver-input
checks, clock counts by independent methods, polynomial multiplication,
root signs and memory use. Every load-bearing constant has two or more
derivations. The final run used approximately 16.2 MB peak RAM, one thread,
inherited nice 20 and a 30-second CPU limit. The requested nice prefix
prints `setpriority: Operation not permitted` because priority is already
20; each script verifies actual nice >=15 before computing.

The exact root bounds are

\[
\frac{38387847911459845608705571}{154742504910672534362390528}
<\varepsilon_2<
\frac{9596961977864961402176393}{38685626227668133590597632},
\]

with width 1/154742504910672534362390528. Independent decimal-grid
signs also bracket it between 0.2480756 and 0.2480757.

The initial literature check ended within five minutes and found no
later solution changing the picture. Opened the arXiv pages and full
texts of Jian Ding and Fenglin Huang, *Non-ergodicity for the noisy
majority vote process on trees*, [arXiv:2501.16202](https://arxiv.org/abs/2501.16202),
and Damiano De Gaspari, *Fredrickson Andersen Model and Noisy Majority
Vote Process on Nonamenable Graphs*, [arXiv:2508.06935](https://arxiv.org/abs/2508.06935).
Both histories still list only the 2025 v1. Their results concern trees
or expansion, and De Gaspari's introduction describes the Euclidean
equilibrium question as open. Their synchronous retained-tie rule is
different from the present continuous-time fair-tie rule. Also opened
G. Gielis, C. Maes, K. Vande Velde, *Randomly interacting particle systems:
The uniqueness regime*, [full text](https://www.numdam.org/item/AIHPA_1999__70_5_445_0.pdf).
This bounded check did not establish a directly comparable published
homogeneous uniqueness bound. No literature novelty or optimality is
claimed.

What failed: the first extension audit caught three incorrectly combined
coefficients in the independent hand expansion. Corrected these; the
factored criterion, event bounds and clock constants were unaffected.
The corrected expansion agrees with independent coefficient multiplication
and exact rational evaluations. The De Gaspari HTML URL returned 404;
the PDF was used. Details and outputs are in [LOG.md](LOG.md).

Uncertainty: the finite audit does not formally verify the probabilistic
or infinite-volume arguments. Those are written out and challenged in
the proof and log. No result is obtained at the new threshold, for
retained ties, or for positive-noise coexistence. The short search cannot
establish absence of a solution or stronger published uniqueness bounds.

Next: the remaining local gap is exactly (a/2)1_{M_x=3}, after subtracting
the preceding triple correction and the new pair correction. Adapt the
triple-broadcast event by forcing the omitted neighbor to be common;
this would bound exactly three disagreements, rather than at least
three, and could use that residual gap without double counting. This
continues the local high-noise method. Low-noise coexistence requires
control of large error clusters beyond these events.

Task: “take the NEXT checkable step on this problem, building on that work”
— 2026-11-15, 04:36 +04 (Asia/Tbilisi).
