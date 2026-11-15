VERDICT: PARTIAL a stronger local connectivity bound from enlarged square regions

The earlier result holds. An independent cycle-integral calculation
reproduces all 202 earlier finite probabilities and every reported bound
for d=2,...,12. Coordinate enumeration also reproduces every seven-edge
graph multiplicity in d=2,3,4,5.

The new step implements the earlier report's suggestion to enlarge wired
regions. For each square through a fixed edge, add every exterior neighbor
of one fixed endpoint. The enlarged region has 2d+2 vertices. Its MST
still certifies the same three-edge detour. These enlarged events replace
the earlier square events and remain incompatible with the earlier
five-edge and seven-edge path events.

PROOF.md proves inclusion of the earlier events by finite-cut monotonicity,
and strict inclusion by an explicit positive-probability label event.
It gives an exact finite rational formula in every d>=2 using a
series/parallel reduction and a signed exponential expansion.

In d=3 the enlarged square probability is

    7175020914436910477/722017042450235532000.

Replacing all four square terms adds

    1120101659682220157/180504260612558883000
      = 0.006205402885677299232... .

The nearest-neighbor connection bound therefore increases from
0.379056328751598078021... to

    237831533319331629226140743/617324571294951379860000000
      = 0.385261731637275377254... .

The new bounds in d=2 and d=4 are respectively
0.592724316686007828922... and 0.280202821595373250359... .
Exact fractions for all d=2,...,12 are saved in extension.json.

Reproduce from this folder:

```
env OMP_NUM_THREADS=1 nice -n 15 python3 recheck.py > recheck.txt
env OMP_NUM_THREADS=1 nice -n 15 python3 enlarge.py --last 12 > extension.txt
env OMP_NUM_THREADS=1 nice -n 15 python3 audit.py > audit.txt
env OMP_NUM_THREADS=1 nice -n 15 python3 final_check.py > final_check.txt
```

The main calculation agrees exactly with a separate Kruskal recursion
for all 143 partial enlargements, k=0,...,2d-2. The audit also works on
the unreduced graph in d=2,3 and integrates every cycle-inequality simplex
for all its final tree shapes: 11,520 integrals in d=2 and 3,225,600 in
d=3. Integer LCM/GCD arithmetic independently confirms every final sum.
No earlier Python implementation is imported or executed.

The three mathematical computation runs took less than three seconds each
and used at most 32,030,720 bytes peak RSS, one thread and actual nice 20.
The nice wrapper warns because the inherited priority is already 20.
Deadlines are at most 900 seconds. Memory is measured, with bounded small
state spaces; it is not an OS-enforced hard memory limit.

No mathematical comparison failed. The main pitfalls checked were extra
induced edges, distinct spokes with a common exterior endpoint, negative
coefficients in the survival expansion, and overlapping certificates
for the same path. Only one enlarged region per square is counted;
enlargements of the same path are not summed as disjoint events.

The bounded literature check found no later solution of the full-lattice
problem. Opened Russell Lyons, Yuval Peres and Oded Schramm,
*Minimal spanning forests*, [arXiv:math/0412263](https://arxiv.org/abs/math/0412263)
and its [full paper](https://rdlyons.pages.iu.edu/pdf/AOP0151.pdf);
Charles M. Newman, Vincent Tassion and Wei Wu, *Critical Percolation and
the Minimal Spanning Tree in Slabs*, [arXiv:1512.09107](https://arxiv.org/abs/1512.09107);
Shirshendu Chatterjee, Yang Chen and Grigory Terlov, *β-Skewed Maximal
Spanning Forests*, [arXiv:2609.11845](https://arxiv.org/abs/2609.11845);
and Luca Makowiec, *Fixed forests in the minimum spanning tree and cubic
volume growth*, [arXiv:2608.10654](https://arxiv.org/abs/2608.10654).
The last three were checked at abstract level. Their slab, weighted-forest
and complete-graph results do not resolve the stated question.

The component problem remains unresolved. Novelty of this local bound
relative to published work is not established. A next worker can enlarge
the region at the other endpoint as well, retaining every induced edge:
leaves added at opposite endpoints can be adjacent, so the present
independent-branch reduction cannot be carried over unchanged. Alternatively,
enlarge the five-edge regions and replace their existing contributions.
Neither direction supplies the missing control on arbitrarily large scales.

Task: “take the NEXT checkable step on this problem, building on that work” —
T049, received 15 November 2026 at approximately 07:40 Asia/Tbilisi.
