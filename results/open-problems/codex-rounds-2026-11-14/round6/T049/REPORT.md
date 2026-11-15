VERDICT: PARTIAL a stronger local connectivity bound using both endpoint neighborhoods

The earlier result holds. Independent tree-route integration reproduces all
202 earlier path probabilities and their bound sums in d=2,...,12. It also
reproduces every partial one-end square enlargement in d=2,3, including the
latest dimension-three value and bound.

The new step adds every exterior neighbor of the other endpoint to each
enlarged square region. The region has 4d vertices. All induced edges are
retained, including the 2d-3 edges between matched neighbors of the two
endpoints. PROOF.md proves a strict improvement for every d>=2 and gives
an exact finite rational recurrence. The new probabilities are evaluated
in d=2 and d=3; higher dimensions are not evaluated here.

In d=3 the new square probability is

    106821527499174906671287753163603/8994156750072383564239397632800000.

Replacing the four previous square terms adds

    191866255331224667993946415505833/24733931062699054801658343490200000
      = 0.007757208300001121523... .

The nearest-neighbor connection bound increases from
0.385261731637275377254... to

    265115546365736108233965694737821273/674561756255428767317954822460000000
      = 0.393018939937276498777... .

In d=2 the new square probability is 1434277211177/33731641944000.
The gain is 4129009763/344200428000, and the bound becomes
84815746280753023/140256167203152000
= 0.604720262731141741422... . Exact data and geometry are in extension.json.

Reproduce from this folder:

```
env OMP_NUM_THREADS=1 nice -n 15 python3 recheck.py > recheck.txt
env OMP_NUM_THREADS=1 nice -n 15 python3 both_ends.py --last 3 > extension.txt
env OMP_NUM_THREADS=1 nice -n 15 python3 audit.py > audit.txt
env OMP_NUM_THREADS=1 nice -n 15 python3 adversarial.py > adversarial.txt
env OMP_NUM_THREADS=1 nice -n 15 python3 final_check.py > final_check.txt
```

The main probability calculation conditions on accepted-edge partitions.
Its dimension-three graph has 236,132 visited states. An independent
calculation enumerates the possible final spanning trees and integrates
their MST cycle inequalities. There are 128 tree shapes in d=2 and 12,288
in d=3, grouped into 64 and 1,296 equal-integral classes. All probabilities
agree exactly.

An additional audit tests all 792 candidate edge subsets in d=2 and all
497,420 candidates in d=3, without the branch classification. It recovers
every tree and every symmetry multiplicity. Lattice constructions check
all 132 square orientations in d=2,...,12, all incident-edge counts, and
explicit positive-probability strict-inclusion witnesses. Counterexamples
also verify that deleting a matched-neighbor edge can create a false
certificate. Integer LCM/GCD arithmetic independently confirms the gains
and final bounds. No earlier Python implementation is imported or executed.

The four mathematical runs took respectively 1.65, 8.45, 31.70 and 1.58
seconds, with at most 115,720,192 bytes peak RSS. They used one thread,
the standard library, actual nice 20, and alarms of at most 900 seconds.
The relative-nice wrapper warns because inherited nice is already 20.
Memory is measured; state and RSS guards bound the main calculation.
An OS-enforced hard memory cap is not claimed.

No arithmetic or geometry comparison failed. The central hazard was the
new induced edges: the previous independent-branch reduction cannot be
reused unchanged. The full graph is used here. Certificates for the same
path are replaced by their enlargement, not summed as disjoint events.
The final document check caught an omitted d=2 gain fraction in this
report; it has been inserted. No computed value changed.

The bounded literature check found no later resolution on full Z^d.
Opened Russell Lyons, Yuval Peres and Oded Schramm,
[*Minimal spanning forests*](https://arxiv.org/abs/math/0412263);
Charles M. Newman, Vincent Tassion and Wei Wu,
[*Critical Percolation and the Minimal Spanning Tree in Slabs*](https://arxiv.org/abs/1512.09107);
Shirshendu Chatterjee, Yang Chen and Grigory Terlov,
[*β-Skewed Maximal Spanning Forests*](https://arxiv.org/abs/2609.11845);
and Luca Makowiec,
[*Fixed forests in the minimum spanning tree and cubic volume growth*](https://arxiv.org/abs/2608.10654).
These pages were checked at abstract/metadata level. The latter three
concern slabs, weighted forests and complete graphs; they do not announce
a solution of the full-lattice question. This was a search under five
minutes, not a definitive bibliographic exclusion.

The component problem remains unresolved. Novelty of this local bound
relative to published work is not established. A next worker can compress
the direct recursion by the local states of exchangeable matched pairs,
preserving their correlations through both endpoints and the root. This
could make d>=4 evaluations feasible without the present large labelled
partition space. A global argument controlling arbitrarily large scales
would still be needed for the original problem.

Task: “take the NEXT checkable step on this problem, building on that work” —
T049, received 15 November 2026 at approximately 10:03 Asia/Tbilisi.
