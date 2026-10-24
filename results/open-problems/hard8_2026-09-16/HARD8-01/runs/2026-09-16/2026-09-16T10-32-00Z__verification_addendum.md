# HARD8-01 checkpoint 5 — verification addendum

**Date:** 2026-09-16 UTC  
**Status:** unrestricted Černý conjecture remains **OPEN**.

This append-only note records the actual GitHub receipts/readbacks and the exact deterministic checks performed after the mathematical report was published.

## 1. Mathematical report receipt

Path:

`hard8_2026-09-16/HARD8-01/runs/2026-09-16/2026-09-16T10-15-00Z__report.md`

Creation commit:

`7c9fa3f5f493083cf39667a77592c541e537929d`

Exact-commit readback succeeded. Returned content blob SHA:

`b28e36cd2051f816ae70f82e50fbc3fc8f4593ad`

Therefore the report is **VERIFIED as delivered**.

The readback was performed at the creation commit, not merely at the moving `master` branch.

## 2. Verifier artifact receipt

Path:

`hard8_2026-09-16/HARD8-01/artifacts/2026-09-16T10-15-00Z__orbit_forest_transport_verifier.py`

Creation commit:

`27c70e1d467e3b7bd408921ff668611bf0871204`

Exact-commit readback succeeded. Returned content blob SHA:

`25259964959e654d8a4b6c77afe60373a3018184`

Therefore the code artifact is **VERIFIED as delivered**.

The verifier is standard-library Python. It uses exact finite permutations, integer lengths, finite subset BFS, and brute-force rooted-forest/path enumeration only. It uses no floating point, randomness, SAT/SMT solver, heuristic acceptance, or timeout-as-proof.

## 3. Exact coset/Schreier checks

The implemented algebra was independently executed on every configuration in the following deterministic families through `n=4`:

- one nonidentity permutation letter + one simple idempotent (`1P1E`);
- one nonidentity permutation letter + two distinct simple idempotents (`1P2E`) for `n>=3`;
- two distinct nonidentity permutation letters + one simple idempotent (`2P1E`) for `n>=3`.

Total configurations checked:

`4,997`

Across these configurations the run checked:

- `38,506` defect-arc witness-coset equalities
  \[
  W_e(a)=gH_e;
  \]
- `527,246` current-prefix / prescribed-arc entrance inequalities
  \[
  \min_{g'\in W_e(a)}d_P(f,g')\le |\mathcal O_e|-1.
  \]

All passed exactly.

## 4. Exact exhaustive small-family census

For each synchronizing configuration, the subset automaton was searched exactly to obtain the true reset threshold. The minimum orbit-weighted rooted-arborescence bound and minimum leaf-discounted bound were then enumerated exactly and checked to be valid upper bounds.

The census is:

```text
n=2, 1P1E:
  total=2
  synchronizing=2
  orbit_weight_square=0
  leaf_discount_square=2

n=3, 1P1E:
  total=30
  synchronizing=18
  orbit_weight_square=6
  leaf_discount_square=18

n=3, 1P2E:
  total=75
  synchronizing=69
  orbit_weight_square=39
  leaf_discount_square=69

n=3, 2P1E:
  total=60
  synchronizing=60
  orbit_weight_square=0
  leaf_discount_square=6
  Hamiltonian_defect_path_square=60
  discount_or_path_square=60

n=4, 1P1E:
  total=276
  synchronizing=72
  orbit_weight_square=24
  leaf_discount_square=72

n=4, 1P2E:
  total=1518
  synchronizing=912
  orbit_weight_square=552
  leaf_discount_square=912

n=4, 2P1E:
  total=3036
  synchronizing=2352
  orbit_weight_square=120
  leaf_discount_square=192
  Hamiltonian_defect_path_square=2232
  discount_or_path_square=2352
```

Thus, in these exhaustive families:

1. the orbit-weight and leaf-discount theorems never underestimate the exact reset threshold;
2. the leaf discount is materially stronger than the raw orbit-weight sum;
3. in the high-group-mobility `2P1E` family, Hamiltonian defect paths often succeed where independent pair-orbit charging is far too coarse;
4. at `n=4`, the union of the discounted-forest certificate and exact Hamiltonian-defect-path certificate covers all `2352` synchronizing `2P1E` automata in the exhaustive family.

This is finite evidence only. It does not prove the SI subclass in general and does not prove the unrestricted conjecture.

## 5. Exact `S_5` obstruction to the two simplified certificates

A targeted five-state example was retained because it shows that neither simplified sufficient certificate can be universal even inside SI automata.

Use states `0,1,2,3,4` and permutation letters, in image-tuple notation,

```text
p = (0,1,2,4,3)
q = (1,2,3,0,4)
```

Together they generate the full symmetric group `S_5` of order `120`. Use the single simple idempotent

```text
e = (0 -> 2).
```

Exact subset BFS gives

\[
\boxed{\operatorname{rt}=14<16=(5-1)^2.}
\]

One exact shortest reset word, with letter indices `[p,q,e] = [0,1,2]`, is

```text
[2,1,1,1,0,2,1,2,1,0,1,0,1,2]
```

Its four singular occurrences are at zero-based positions

```text
[0,5,7,13]
```

and their conjugated defect arcs are

```text
(0 -> 2), (1 -> 3), (4 -> 2), (2 -> 3).
```

They form the branching arborescence with root `3`:

```text
0 -> 2 -> 3
4 -> 2
1 -> 3
```

The exact coarse certificate values are:

```text
ordered-pair orbit weight bound       = 80
best leaf-discounted forest bound     = 61
best Hamiltonian defect-path total    = 21
Cerny square                           = 16
exact reset threshold                  = 14
```

Hence both

- independent ordered-pair orbit charging, even with the best first-leaf discount, and
- restricting the singular forest to a Hamiltonian path

can miss the square even though the actual automaton is comfortably below it.

This is a useful obstruction, not a counterexample to Černý. It says the next proof step must combine **branching** with **correlated cheap witness transitions** rather than choose between a fully static pair-orbit bound and a single defect chain.

## 6. Interpretation for the next iteration

The five-state `S_5` example pinpoints the missing amortization. Its exact shortest reset word uses four singular letters, as guaranteed by checkpoint 4, and only ten permutation letters. The independent pair-orbit bound charges up to nineteen permutation letters before each prescribed arc because the ordered-pair orbit has size twenty, but the actual witness sequence reaches the needed branching-tree arcs with inter-singular permutation gaps `4,1,5`.

The next target should therefore be a **branch-aware transporter lemma**. For a child-before-parent tree schedule, distinguish:

- adjacency steps, where the next source equals the current target and Lemma 7 reduces the constraint to one state;
- sibling/branch jumps, where two coordinates appear independent but the already deleted subtree may provide freedom in choosing the next arc/witness.

A successful amortized theorem only needs total permutation travel at most
\[
(n-1)(n-2),
\]
not a uniform `n-1` bound for every individual jump. The `S_5` witness above is an exact small model in which a `5`-letter jump is offset by a `1`-letter jump.

## 7. Review requirement

All results here are self-verified exact finite checks plus proofs in the main report. They have **not** received independent external mathematical review. The unrestricted conjecture is not closed.
