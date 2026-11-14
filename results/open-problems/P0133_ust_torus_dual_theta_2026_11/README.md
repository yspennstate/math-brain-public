# The dual theta graph of a uniform spanning tree on a torus (Schramm, Problem 6.2)

Status: open. This folder records numerical evidence, not a proof, and the numerics have not been independently
audited.

## The problem and where it comes from

Oded Schramm, in his 2006 ICM address (*Conformally invariant scaling limits: an overview and a collection of
problems*, Proceedings of the ICM, Madrid 2006, Vol. I, 513-543; arXiv:math/0602151), asked for the scaling limit of
the topological data of a uniform spanning tree on a torus (Problem 6.2). For a fine discretization of the torus
C / <1, tau>, the edges outside the tree, read in the dual graph, have a core that is almost always a theta graph,
and the homology classes of its three cycles form a superbase {v1, v2, v3} of the lattice Z + tau Z with
v1 + v2 + v3 = 0. The question is what the law of this random superbase is in the limit and how it depends on tau.

The work this rests on:

- **Wilson's algorithm** (D. B. Wilson, *Generating random spanning trees more quickly than the cover time*,
  STOC 1996) samples the tree exactly. Every sampler here is Wilson's algorithm; the only new part is how it is laid
  out on a GPU.
- **Conformal invariance of the UST and loop-erased random walk** (G. F. Lawler, O. Schramm, W. Werner, Ann. Probab.
  32 (2004) 939-995) is the reason a scaling limit is expected to exist and to depend on the conformal modulus tau
  alone. Finding 2 below is a numerical check of that expectation for this particular observable.
- **Kenyon's work on the dimer model and spanning trees on the torus** (R. Kenyon, *Long-range properties of
  spanning trees*, J. Math. Phys. 41 (2000) 1338-1363, and later papers) computes related topological quantities
  exactly; a closed form for the superbase law, if one exists, would most likely come from that direction.

## What is new here

1. A GPU sampler (`ust_metal.swift`): Wilson's algorithm on the sheared torus Z^2 / <(n1, 0), (s, n2)>, one tree per
   GPU thread, with the walk and both retrace passes written as one loop. It produces about 4,800 trees a second at
   160x160 on an Apple M-series GPU (10^6 trees in 206 s), roughly three orders of magnitude faster than the numba
   CPU sampler `ust_torus_shear.py`, and its output law matches the CPU sampler within two standard errors on every
   superbase tested.
2. The figure-eight core (only two classes occur) disappears in the limit: its frequency on the square torus falls
   from 0.026 at n = 8 to 0.0005 at n = 64.
3. The superbase law converges and depends on tau only: two meshes of the same modulus agree within sampling error on
   five moduli, and tori placed at an angle to the lattice give the PSL2(Z)-transformed law.
4. Limit values to about three digits (for instance 0.475 for each of the two top superbases of the square torus).
5. The law is close to, but measurably not equal to, C exp(-0.9 (|v1|^2 + |v2|^2 + |v3|^2) / Im tau). A polynomial
   fit of the log-weight in the shape needs degree four on a 49-modulus grid and predicts held-out meshes well; no
   short closed form was found.

`NOTE.md` has the numbers, tables and the tests behind each item; `STATUS.md` is the one-paragraph summary.

## Running it

    swiftc -O ust_metal.swift -o ust_metal          # macOS with Metal
    ./ust_metal <n1> <n2> <s> <samples> <seed> out.tsv 4096
    python ust_torus_shear.py ...                   # the CPU sampler (numba), same output format
    python classify.py out.tsv                      # tally of superbases ordered by |a + b tau|
    python mesh_table.py ...                        # the law by mesh for one modulus

`data/p0133_samples_2026_11_14.tar.gz` holds the 53 sample tables (mesh pairs, rotation tests, a check table) used
for findings 2 and 3. The million-sample runs and the 49-modulus grid of finding 5 are not in this folder.

## Credit

The problem is Schramm's. The sampler is Wilson's algorithm; the expectation that the limit is conformally invariant
comes from Lawler, Schramm and Werner. The code, the GPU layout and the measurements were produced with AI
assistance (Claude) and have not been checked by a person.
