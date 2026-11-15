# Open problem T049: Number of components of the minimal spanning forest on Z^d

Statement: The minimal spanning forest of Z^d with iid uniform edge weights (free and wired coincide on Z^d) is a single tree for d < 8 and has infinitely many components for d > 8.

Source: C. M. Newman and D. L. Stein, Spin-glass model with dimension-dependent ground state multiplicity, Phys. Rev. Lett. 72 (1994); R. Lyons, Y. Peres and O. Schramm, Minimal spanning forests, Ann. Probab. 34 (2006)

Where it stands (checked by us, Nov 2026): A single tree on Z^2 (Alexander 1995). On amenable transitive graphs the free and wired forests agree (Lyons–Peres–Schramm, arXiv:math/0412263). Open for every d ≥ 3.

Earlier work: a previous worker spent one session on this problem. Its folder is ~/codex_op_1114/briefs/T049 (read it,
never edit it). Its REPORT.md is copied below. Read its REPORT.md, LOG.md, PROOF.md and scripts before you start.

Later work: a round 3 worker built on that session. Its folder is ~/codex_op_1114r3/briefs/T049 (read it,
never edit it). Its REPORT.md is copied below. Read its REPORT.md, LOG.md, PROOF.md and scripts before you start.

Later work: a round 4 worker built on that session. Its folder is ~/codex_op_1114r4/briefs/T049 (read it,
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
VERDICT: PARTIAL a stronger local connectivity bound from every seven-edge detour

The earlier result holds. Fresh exact recursions reproduce all eleven
reported square probabilities, all 33 six-vertex probabilities, and all
eleven connectivity bounds for d=2,...,12.

The new result adds every seven-edge simple detour around a fixed lattice
edge to the three-edge and five-edge certificates. There are fifteen
induced graphs up to reversal of the specified path. PROOF.md gives their
complete chord lists, multiplicities in every d>=2, and an exact finite
rational formula for each probability. The total number of new paths is

    28(d-1)+496 binomial(d-1,2)+1296 binomial(d-1,3)
      = 4(d-1)(54d^2-208d+207).

In d=3 there are 552 new paths, and their total certified probability is

    146118665900743508898613/56120415572268307260000000
      = 0.002603663290992226709... .

Thus the nearest-neighbor connectivity bound increases from
0.376452665460605... to

    21272798694838039662654613/56120415572268307260000000
      = 0.379056328751598078021... .

The new bound is 0.582979463810902... in d=2 and 0.276251488917593... in
d=4. Exact results for d=2,...,12 are in extension.json. The proof gives
a strict improvement in every d>=2. These remain local lower bounds;
the component problem is unresolved by this work.

Reproduce inside this folder, in order:

```
env OMP_NUM_THREADS=1 nice -n 15 python3 seven.py recheck > recheck.txt
env OMP_NUM_THREADS=1 nice -n 15 python3 seven.py enumerate > enumeration.txt
env OMP_NUM_THREADS=1 nice -n 15 python3 seven.py extend > extension.txt
env OMP_NUM_THREADS=1 nice -n 15 python3 audit.py > audit.txt
env OMP_NUM_THREADS=1 nice -n 15 python3 final_check.py > final_check.txt
```

The first script reads earlier JSON results for comparison but imports or
executes no earlier code. Its probability calculations separately recurse
on successful partitions and sum over fixed final trees. All 158 active
new probabilities agree exactly between these methods. The independent
audit constructs closed direction multisets, without the reachability
recursion, and reproduces every induced-graph count in d=2,3,4,5. It checks
all 179700 pairs of the 600 paths of lengths 3,5,7 in d=3 for a cycle in
their union. For each of the fifteen d=3 graph types it also evaluates all
322560 ordered-simplex integrals from the MST cycle criterion. All three
probability methods agree. Integer LCM/GCD arithmetic independently confirms
every final rational addition. No sampling or box-limit extrapolation is used.

All numerical runs finished in under four seconds each and used less than
28 MB peak RSS. They used one thread, the standard library, actual nice 20,
and a 600-second alarm. The relative nice wrapper warns because the
inherited priority is already 20; each script checks the actual priority.
Memory usage is measured, with bounded small state spaces; it is not an
operating-system hard memory limit. Earlier files were never edited.

No geometry or probability comparison failed. The final document audit
caught an incorrect common-denominator multiplier in a proof draft;
integer division corrected it to 60858172908000. The saved probabilities,
gain and bound were already correct. A case needing extra care was a
degree-four vertex in several planar graphs: its spoke multiplicity is
zero in d=2, so the earlier implementation's strictly-positive-spoke
assumption cannot be carried over. The present formulas allow zero spokes.
Every induced chord is retained, including all four chords in the cube
graphs. Signs, path orientation and overlapping paths are checked explicitly.

The literature search, completed within five minutes, found no later
solution on full Z^d. This is a bounded search. Opened Russell Lyons,
Yuval Peres and Oded Schramm, *Minimal spanning forests*,
[arXiv:math/0412263](https://arxiv.org/abs/math/0412263) and its
[full paper](https://rdlyons.pages.iu.edu/pdf/AOP0151.pdf);
Charles M. Newman, Vincent Tassion and Wei Wu, *Critical Percolation and
the Minimal Spanning Tree in Slabs*,
[arXiv:1512.09107](https://arxiv.org/abs/1512.09107);
T. S. Jackson and N. Read, *Theory of minimum spanning trees I: Mean-field
theory and strongly disordered spin-glass model*,
[arXiv:0902.3651](https://arxiv.org/abs/0902.3651);
Shirshendu Chatterjee, Yang Chen and Grigory Terlov, *β-Skewed Maximal
Spanning Forests*, [arXiv:2609.11845](https://arxiv.org/abs/2609.11845);
and Luca Makowiec, *Fixed forests in the minimum spanning tree and cubic
volume growth*, [arXiv:2608.10654](https://arxiv.org/abs/2608.10654).
The last four arXiv pages were checked at abstract level. The slab theorem,
the dimension-six scaling proposal, weighted forests, and complete-graph
asymptotics do not resolve the full lattice question. No
SOLVED_ELSEWHERE.md is appropriate.

The next worker can extend the same enumeration to nine-edge detours;
closing to a ten-cycle uses at most four transverse axes, so dimensions
2 through 5 suffice for support coefficients. This would remain a local
improvement. To address the original question, a new argument must control
connections on arbitrarily large scales. Enlarging wired regions around
fixed paths is another direction, but events certifying the same path can
overlap and must be combined by a union calculation. Novelty of the local
bound relative to published work is not established.

Task: “take the NEXT checkable step on this problem, building on that work” —
T049, received 15 November 2026 at approximately 04:25 Asia/Tbilisi.
