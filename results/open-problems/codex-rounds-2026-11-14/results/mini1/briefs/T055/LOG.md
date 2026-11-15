# T055 work log

Task received: 2026-11-14, session start recorded at 20:47:15 +04:00.
Task: “Dimensional reduction for lattice trees and lattice animals”; push the
problem forward by one checkable piece.

## 1. Orientation and initial literature search (20:47–20:50)

All writes are confined to this folder. The later task-specific restriction
precludes the global instructions' mesh/checklist/brain writes outside it; those
services were not mutated. Read the brain navigation index and the compute state.
Compute status was `ok`, mode `owner_away_open`. No workers were spawned.

Commands so far were short read-only Python snippets, invoked as
`OMP_NUM_THREADS=1 nice -n 15 python3 ...`. macOS reports
`nice: setpriority: Operation not permitted`: inspection with
`os.getpriority(os.PRIO_PROCESS, 0)` returned **20**. The runner already has lower
priority than requested; changing it to 15 is disallowed. Computations will retain
that inherited niceness of 20 and explicitly use the requested nice wrapper.

Web queries:

- `lattice animals lattice trees dimensional reduction critical exponents rigorous 2024 2025 2026`
- `Parisi Sourlas lattice animals two dimensions exponent theta 1 proof open problem`
- `"lattice animals" "dimensional reduction" "2026"`
- `"lattice animals" "dimensional reduction" "2025"`
- `"lattice trees" "two dimensions" rigorous exponents dimensional reduction`

Opened arXiv pages 2412.05491 and 1905.02785. The first concerns spread-out
models above dimension eight, not the requested low-dimensional result. Further
inspection pending. An attempted Annals URL (`2003/158-3/p01`) was the wrong
article and is not used as a reference. No proof in dimensions two or three
found in these initial searches.

## 2. Literature decision and choice of piece (before computation)

Literature search used less than ten minutes. Additional queries were
`"lattice animals" "critical exponents" "2026" proof`,
`"lattice animals" "Parisi" "2025" rigorous`, and the title of Brydges–Imbrie.
No low-dimensional lattice solution was found. This is a bounded search, not
proof that none exists. High-dimensional advances do not settle T055, so they
do not trigger the solved-elsewhere stopping branch.

Papers actually opened:

- Yucheng Liu and Gordon Slade, *Near-critical and finite-size scaling for
  high-dimensional lattice trees and animals*, arXiv:2412.05491, revised 2025;
  J. Stat. Phys. 192, 32 (2025). https://arxiv.org/abs/2412.05491 . Spread-out
  models in d > 8: correlation length exponent 1/4 and torus scaling bounds.
- Robert Fitzner and Remco van der Hofstad, *NoBLE for lattice trees and lattice
  animals*, arXiv:1905.02785. https://arxiv.org/abs/1905.02785 . Nearest-neighbor
  high-dimensional mean-field results; not a d = 2, 3 dimensional reduction.
- Gill Barequet, Neal Madras, Johann Peters, *On t-fold Totally-Concave
  Polyominoes*, CCCG 2025, pp. 92–98.
  https://cccg-wads-2025.eecs.yorku.ca/cccg-papers/34.pdf . The introduction
  describes the lack of rigorous low-dimensional asymptotic geometry; its
  concavity result is not the exponent theorem in T055.
- David C. Brydges and John Z. Imbrie, *Branched Polymers and Dimensional
  Reduction*, arXiv:math-ph/0107005; Ann. Math. 158 (2003), 1019–1039.
  https://arxiv.org/abs/math-ph/0107005 . Exact continuum reduction.

**Chosen piece:** enumerate the joint distribution of induced edge excess
`k = e - n + 1` and spanning-tree multiplicity `tau` for translation classes of
site animals in Z² through n = 8 and Z³ through n = 7. Find and certify the
first size at which the same `(n,k)` has different `tau` values. Give the exact
tree-to-site-animal identity and explicit witnesses for the resulting
obstruction to correcting that identity by a weight depending only on size and
number of contacts.

Why: forgetting the bonds of a lattice tree weights a site animal by its number
of spanning trees, not uniformly. This is a concrete model-comparison issue on
the lattice. A finite certificate can rule out an overly simple bridge without
making an unjustified claim about critical exponents. No novelty claim is made
for the spanning-tree identity itself.

Plan for independent checks: generate animals by canonical growth, then by a
lexicographic-root exclusion recursion; compare complete shape sets at each
size. Compute `tau` by exact Laplacian cofactors, and independently by exhaustive
spanning-tree edge subsets on every shape. Bound time and memory; reduce the
range if needed. Keep rotations and reflections distinct; identify translations
only. All counts are by occupied vertices, not by bonds.

## 3. Enumeration implementation and run

Added `enumerate_animals.py` (Python standard library only). The generator based
on adding all boundary sites and deduplicating translations is checked against
an exclusion recursion that fixes the lexicographically least vertex at the
origin and generates each animal once. An all-pairs Manhattan-distance test
constructs the graph independently of the growth-neighbor function.

Exact command:

```sh
OMP_NUM_THREADS=1 nice -n 15 python3 -B enumerate_animals.py --d2 8 --d3 7 --output data | tee enumeration_output.txt
```

The script has a 1100-second CPU limit and 1190-second wall alarm. Output reports
niceness 20 and one OMP thread. The square-lattice run finished in 0.145 seconds;
3792 animals agreed shape-by-shape between the two generators and between
integer Laplacian determinants and explicit spanning-tree edge subsets.
The first collision is n = 7, excess = 2, with multiplicities 15 and 16.
The three-dimensional run and its final output are recorded next.

Final enumeration output: Z³ finished in 0.984 seconds, checking 27622 animals.
First collision: n = 6, excess = 1, multiplicities 4 and 6. Peak RSS reported by
macOS: 47,316,992 bytes (< 1 GB). `ALL_ASSERTIONS_PASSED`.
Complete stdout is in `enumeration_output.txt`; each shape and its exact
statistics are in `data/shapes_d2.jsonl` and `data/shapes_d3.jsonl`. Joint
histograms are in `data/histogram_d2.csv` and `data/histogram_d3.csv`.

| d | n | site animals | bond trees | induced site trees |
|---|---|---|---|---|
| 2 | 1 | 1 | 1 | 1 |
| 2 | 2 | 2 | 2 | 2 |
| 2 | 3 | 6 | 6 | 6 |
| 2 | 4 | 19 | 22 | 18 |
| 2 | 5 | 63 | 87 | 55 |
| 2 | 6 | 216 | 364 | 174 |
| 2 | 7 | 760 | 1574 | 570 |
| 2 | 8 | 2725 | 6986 | 1908 |
| 3 | 1 | 1 | 1 | 1 |
| 3 | 2 | 3 | 3 | 3 |
| 3 | 3 | 15 | 15 | 15 |
| 3 | 4 | 86 | 95 | 83 |
| 3 | 5 | 534 | 678 | 486 |
| 3 | 6 | 3481 | 5229 | 2967 |
| 3 | 7 | 23502 | 42464 | 18748 |

Shape-certificate SHA-256 digests:

```text
d2 5765460b6f56077545350872dbaa05b823bec61a675543b834335dfb37d50a83
d3 fa2ac5bef0bd7d6ae03e3e5ddfb102f0f1187fe9aee6cba092ae9ed4b326d0ed
```

## 4. Strengthening the same obstruction

The finite witnesses can be joined by bridges. Choose matching left/right
ports, translate the two planar gadgets by 4j along the first coordinate, and
insert one connector vertex between each pair. For r gadgets, the two shapes
have n = 8r − 1 and excess = 2r, but tree multiplicities 15^r and 16^r.
For cubic gadgets the analogous spacing is 3j: n = 7r − 1, excess = r, and
multiplicities 4^r and 6^r. This would rule out even uniformly subexponential
shape-by-shape correction by a function of `(n, excess)` alone. This does not
rule out exponent universality or a relation that holds only after summation.
The explicit ports, unintended-contact checks, and multiplicative formulas
are being independently audited before treating this as proved.

## 5. Independent audit of gadgets and bridges

Added `audit_obstruction.py`, without importing the enumeration implementation.
It uses squared Euclidean distance one to construct edges, rational Gaussian
elimination for determinants, and a reachability test on every spanning-edge
subset of each base gadget. It also finds the gadgets in the saved enumeration.
For bridge chains it checks every cross-gadget edge, deletes each proposed
bridge to verify disconnection, and compares the rational determinant with the
power formula. Checked r = 1, 2, 3, 5 for all four gadget types.

Exact command:

```sh
OMP_NUM_THREADS=1 nice -n 15 python3 -B audit_obstruction.py | tee obstruction_output.txt
```

Complete output is in `obstruction_output.txt`; data are in
`data/chain_audit.json`. Output at r = 5:

```text
d=2 A: n=39 edges=48 excess=10 tau=759375 = 15^5
d=2 B: n=39 edges=48 excess=10 tau=1048576 = 16^5
d=3 A: n=34 edges=38 excess=5 tau=1024 = 4^5
d=3 B: n=34 edges=38 excess=5 tau=7776 = 6^5
PEAK_RSS_RAW 78053376
ALL_ASSERTIONS_PASSED
```

Run time reported by the tool was 0.310 seconds. Peak RSS was 78,053,376 bytes.
The symbolic argument additionally checks the arbitrary-r construction; finite
tests are not used to infer its validity for all r.

## 6. Adversarial review and final versions

Wrote the complete proof in `PROOF.md`, including a graph-theoretic minimality
argument independent of the animal enumeration. The key small-graph constraint
is that two distinct hypercubic vertices have at most two common neighbors,
excluding K_{2,3}. Up to five vertices, the only possible multiplicities are
1 (trees) and 4 (a single square). At six vertices, a two-cycle graph must be
the theta graph with path lengths 1,3,3 and multiplicity 15. A planar induced
six-cycle is impossible because its bounding rectangle has six vertices and
the induced middle edge is a chord. A cubic induced six-cycle exists.

Two specific potential gaps were checked:

- Shared adjacency code could make the two animal generators share an error.
  Replaced the exclusion generator's adjacency with an independent Cartesian
  product of displacement vectors and reran the exact enumeration command.
  Counts and certificate digests were unchanged. Final times: d2 0.144 s,
  d3 1.015 s; final peak RSS 45,776,896 bytes.
- The small-graph proof could miss a bipartition or a second cycle arrangement.
  Extended the standalone audit to test every labeled bipartite graph on up
  to six vertices, over each possible part-size split, rejecting disconnected
  graphs and graphs with three common neighbors. The allowed (excess,tau)
  pairs were exactly (0,1), (1,4) up to five vertices, and additionally (1,6),
  (2,15) at six vertices. The audit does not assume that every surviving graph
  embeds in a lattice. Re-ran the exact obstruction command; all assertions
  passed. Its graph data are in `data/graph_classification.json`.

The proof checks cross-gadget contacts, bridge factorization, all r >= 1,
translation versus rotation conventions, singleton normalization, and the
difference between boundary bonds and distinct boundary sites. It explicitly
does not infer critical exponents from finite counts or from exceptional shape
families. A no-op patch attempt against a nonexistent log line failed without
changing any file; the actual appended audit is recorded here.

What failed: the candidate bridge using a correction that depends only on
size and contacts cannot work shape by shape, even to uniformly subexponential
accuracy. No proof of low-dimensional dimensional reduction was obtained.
Novelty of the elementary obstruction was not established by the short
literature search.

## 7. Complete final command output

Both commands below retained niceness 20. Each also emitted the already documented nice warning on stderr.

```sh
OMP_NUM_THREADS=1 nice -n 15 python3 -B enumerate_animals.py --d2 8 --d3 7 --output data | tee enumeration_output.txt
```

```text
RUNTIME {"nice": 20, "OMP_NUM_THREADS": "1"}
COUNT {"bond_trees": 1, "d": 2, "induced_trees": 1, "max_tau": 1, "n": 1, "site_animals": 1}
COUNT {"bond_trees": 2, "d": 2, "induced_trees": 2, "max_tau": 1, "n": 2, "site_animals": 2}
COUNT {"bond_trees": 6, "d": 2, "induced_trees": 6, "max_tau": 1, "n": 3, "site_animals": 6}
COUNT {"bond_trees": 22, "d": 2, "induced_trees": 18, "max_tau": 4, "n": 4, "site_animals": 19}
COUNT {"bond_trees": 87, "d": 2, "induced_trees": 55, "max_tau": 4, "n": 5, "site_animals": 63}
COUNT {"bond_trees": 364, "d": 2, "induced_trees": 174, "max_tau": 15, "n": 6, "site_animals": 216}
COUNT {"bond_trees": 1574, "d": 2, "induced_trees": 570, "max_tau": 16, "n": 7, "site_animals": 760}
COUNT {"bond_trees": 6986, "d": 2, "induced_trees": 1908, "max_tau": 56, "n": 8, "site_animals": 2725}
FIRST_COLLISION {"d": 2, "examples": [{"tau": 15, "vertices": [[0, 0], [0, 1], [0, 2], [0, 3], [1, 0], [1, 1], [1, 2]]}, {"tau": 16, "vertices": [[0, 0], [0, 1], [1, -1], [1, 0], [1, 1], [2, -1], [2, 0]]}], "excess": 2, "n": 7}
AUDIT {"d": 2, "shapes_checked_by_both_methods": 3792, "sha256": "5765460b6f56077545350872dbaa05b823bec61a675543b834335dfb37d50a83", "seconds": 0.144}
COUNT {"bond_trees": 1, "d": 3, "induced_trees": 1, "max_tau": 1, "n": 1, "site_animals": 1}
COUNT {"bond_trees": 3, "d": 3, "induced_trees": 3, "max_tau": 1, "n": 2, "site_animals": 3}
COUNT {"bond_trees": 15, "d": 3, "induced_trees": 15, "max_tau": 1, "n": 3, "site_animals": 15}
COUNT {"bond_trees": 95, "d": 3, "induced_trees": 83, "max_tau": 4, "n": 4, "site_animals": 86}
COUNT {"bond_trees": 678, "d": 3, "induced_trees": 486, "max_tau": 4, "n": 5, "site_animals": 534}
COUNT {"bond_trees": 5229, "d": 3, "induced_trees": 2967, "max_tau": 15, "n": 6, "site_animals": 3481}
COUNT {"bond_trees": 42464, "d": 3, "induced_trees": 18748, "max_tau": 50, "n": 7, "site_animals": 23502}
FIRST_COLLISION {"d": 3, "examples": [{"tau": 4, "vertices": [[0, 0, 0], [0, 0, 1], [0, 0, 2], [0, 0, 3], [0, 1, 0], [0, 1, 1]]}, {"tau": 6, "vertices": [[0, 0, 0], [0, 0, 1], [0, 1, 0], [1, 0, 1], [1, 1, 0], [1, 1, 1]]}], "excess": 1, "n": 6}
AUDIT {"d": 3, "shapes_checked_by_both_methods": 27622, "sha256": "fa2ac5bef0bd7d6ae03e3e5ddfb102f0f1187fe9aee6cba092ae9ed4b326d0ed", "seconds": 1.015}
PEAK_RSS_RAW 45776896
ALL_ASSERTIONS_PASSED
```

```sh
OMP_NUM_THREADS=1 nice -n 15 python3 -B audit_obstruction.py | tee obstruction_output.txt
```

```text
RUNTIME {"nice": 20, "OMP_NUM_THREADS": "1"}
GRAPH_CLASSIFICATION {"histogram": [{"excess": 0, "graphs": 1, "tau": 1}], "labeled_bipartite_graphs": 1, "n": 2}
GRAPH_CLASSIFICATION {"histogram": [{"excess": 0, "graphs": 1, "tau": 1}], "labeled_bipartite_graphs": 1, "n": 3}
GRAPH_CLASSIFICATION {"histogram": [{"excess": 0, "graphs": 5, "tau": 1}, {"excess": 1, "graphs": 1, "tau": 4}], "labeled_bipartite_graphs": 6, "n": 4}
GRAPH_CLASSIFICATION {"histogram": [{"excess": 0, "graphs": 13, "tau": 1}, {"excess": 1, "graphs": 6, "tau": 4}], "labeled_bipartite_graphs": 19, "n": 5}
GRAPH_CLASSIFICATION {"histogram": [{"excess": 0, "graphs": 114, "tau": 1}, {"excess": 1, "graphs": 96, "tau": 4}, {"excess": 1, "graphs": 6, "tau": 6}, {"excess": 2, "graphs": 18, "tau": 15}], "labeled_bipartite_graphs": 234, "n": 6}
CHAIN {"d": 2, "edges": 8, "excess": 2, "gadget": "A", "n": 7, "r": 1, "tau": 15}
CHAIN {"d": 2, "edges": 18, "excess": 4, "gadget": "A", "n": 15, "r": 2, "tau": 225}
CHAIN {"d": 2, "edges": 28, "excess": 6, "gadget": "A", "n": 23, "r": 3, "tau": 3375}
CHAIN {"d": 2, "edges": 48, "excess": 10, "gadget": "A", "n": 39, "r": 5, "tau": 759375}
CHAIN {"d": 2, "edges": 8, "excess": 2, "gadget": "B", "n": 7, "r": 1, "tau": 16}
CHAIN {"d": 2, "edges": 18, "excess": 4, "gadget": "B", "n": 15, "r": 2, "tau": 256}
CHAIN {"d": 2, "edges": 28, "excess": 6, "gadget": "B", "n": 23, "r": 3, "tau": 4096}
CHAIN {"d": 2, "edges": 48, "excess": 10, "gadget": "B", "n": 39, "r": 5, "tau": 1048576}
CHAIN {"d": 3, "edges": 6, "excess": 1, "gadget": "A", "n": 6, "r": 1, "tau": 4}
CHAIN {"d": 3, "edges": 14, "excess": 2, "gadget": "A", "n": 13, "r": 2, "tau": 16}
CHAIN {"d": 3, "edges": 22, "excess": 3, "gadget": "A", "n": 20, "r": 3, "tau": 64}
CHAIN {"d": 3, "edges": 38, "excess": 5, "gadget": "A", "n": 34, "r": 5, "tau": 1024}
CHAIN {"d": 3, "edges": 6, "excess": 1, "gadget": "B", "n": 6, "r": 1, "tau": 6}
CHAIN {"d": 3, "edges": 14, "excess": 2, "gadget": "B", "n": 13, "r": 2, "tau": 36}
CHAIN {"d": 3, "edges": 22, "excess": 3, "gadget": "B", "n": 20, "r": 3, "tau": 216}
CHAIN {"d": 3, "edges": 38, "excess": 5, "gadget": "B", "n": 34, "r": 5, "tau": 7776}
PEAK_RSS_RAW 67960832
ALL_ASSERTIONS_PASSED
```

Final artifact audit: all 31414 shape records reconcile with both CSV histograms, JSON summary totals, induced-tree totals, and both stored SHA-256 digests. Both complete output files end in ALL_ASSERTIONS_PASSED. REPORT.md has the required verdict first line.

Finished 2026-11-14T20:56:42.196402+04:00. All created artifacts are in this folder; no git or external writes were used.
