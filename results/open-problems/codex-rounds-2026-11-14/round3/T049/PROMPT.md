# Open problem T049: Number of components of the minimal spanning forest on Z^d

Statement: The minimal spanning forest of Z^d with iid uniform edge weights (free and wired coincide on Z^d) is a single tree for d < 8 and has infinitely many components for d > 8.

Source: C. M. Newman and D. L. Stein, Spin-glass model with dimension-dependent ground state multiplicity, Phys. Rev. Lett. 72 (1994); R. Lyons, Y. Peres and O. Schramm, Minimal spanning forests, Ann. Probab. 34 (2006)

Where it stands (checked by us, Nov 2026): A single tree on Z^2 (Alexander 1995). On amenable transitive graphs the free and wired forests agree (Lyons–Peres–Schramm, arXiv:math/0412263). Open for every d ≥ 3.

Earlier work: a previous worker spent one session on this problem. Its folder is ~/codex_op_1114/briefs/T049 (read it,
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
VERDICT: PARTIAL an explicit finite-plaquette lower bound for nearest-neighbor MSF connectivity

For every d>=2 and neighboring u,v, with e={u,v}, proved

    P(u and v are in the same MSF tree) >= 1/d + 2(d-1)a_(2d-2),

where a_m is the exactly computable probability that the MST of a four-cycle
with m independent parallel spokes from each vertex to a wired root contains
the three-edge alternate path around e. `PROOF.md` gives a 96-term formula
for all m, grouped into 14 terms, and proves the infinite-volume implication.

For d=3 the bound is

    P(0 connected to e_1) >= 120767/329175 = 0.366877800562...,

including a contribution of at least 11042/329175 from configurations where
the edge {0,e_1} is absent. The edge-inclusion probability alone is 1/3.
This is a local quantitative bound. It does not settle any d>=3 case of
T049, exclude a finite number of components, or establish dimension eight.
Its novelty relative to existing elementary bounds has not been established.

Reproduce with:

```
env OMP_NUM_THREADS=1 nice -n 15 python3 verify.py > verification.txt
```

Exact data for d=2,...,12 are in `data.json`; full output is in
`verification.txt`. A Kruskal partition recursion and integration of the MST
cycle inequalities agree in all 11 dimensions. A third check enumerates all
40320 edge orders on the auxiliary m=1 graph, finding 3344 successes. Explicit
lattice coordinates independently check all incident-edge counts and every
pair of plaquette paths. Box edge counts and the d=3 arithmetic are also
re-derived in the proof. No sampling or infinite-volume extrapolation is used.

The final run took 0.088 seconds according to the execution tool and used
15,499,264 bytes peak RSS. It ran with OMP_NUM_THREADS=1, inherited nice level
20, no numerical libraries, and a 120-second alarm. The relative `nice`
wrapper prints a setpriority warning because the process is already at nice
20. Attempts to impose AS and RSS hard limits were rejected by the platform;
these failed before calculation. Actual measured usage was below 1 GB.

The bounded literature check found no post-status resolution for full Z^d.
It did find an older special-case extension omitted from the brief:
Charles M. Newman, Vincent Tassion and Wei Wu, *Critical Percolation and the
Minimal Spanning Tree in Slabs*,
[arXiv:1512.09107](https://arxiv.org/abs/1512.09107).
Theorem 2.5 proves a single tree on Z^2 times {0,...,k}; Remark 2.6 extends
the argument to Z^2 times any finite connected graph. The
[accepted manuscript](https://wrap.warwick.ac.uk/id/eprint/114352/1/WRAP-critical-percolation-minimal-spanning-tree-slabs-Wu-2020.pdf)
was opened and checked. This predates November 2026 and does not prove
connectivity on full Z^3.

Also opened Russell Lyons, Yuval Peres and Oded Schramm, *Minimal spanning
forests*, [arXiv:math/0412263](https://arxiv.org/abs/math/0412263), and its
[full paper](https://rdlyons.pages.iu.edu/pdf/AOP0151.pdf), for the cycle
definition and the free/wired setting. The recent search hit Shirshendu
Chatterjee, Yang Chen and Grigory Terlov, *Beta-Skewed Maximal Spanning
Forests*, [arXiv:2609.11845](https://arxiv.org/abs/2609.11845), concerns
weighted forests and nonunimodular percolation in its abstract; it announces
no solution of this lattice component problem. Only its arXiv page was
checked. Search queries and timing are in `LOG.md`; the search is not a
proof that no later paper exists.

The next worker could extend the same certificate calculation to longer
simple u-v paths that avoid e. Wire the complement of the path's vertex set,
and calculate the probability its finite MST contains every path edge.
Distinct certified simple paths are incompatible in the infinite forest,
because two distinct simple paths between the same endpoints contain a
cycle. Their probabilities can therefore be added without assuming
independence. Any such extension should be assessed as a local bound; a new
argument would still be required to obtain the claimed component transition.

Task: “push this problem forward by one checkable piece” — T049, received
14 November 2026 at approximately 20:45 Asia/Tbilisi.
