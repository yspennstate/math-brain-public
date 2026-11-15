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
