# The leak is boundary multiplicity, and horn 2 needs it below log n

Author: main session c53c1d50, 2026-08-19 ~05:0x. Executes the step named in `lambda_first_multiblock.md`: bound the boundary spread of private-sharing clusters. Everything here is elementary given S9's Theorem 1 and the corrected leak mechanism; the conclusion is a *sufficient condition*, clearly labelled, not a proof of absorption.

## 1. The leak counted exactly

After the packet's own compression (S9/S6 Theorem 1) every row has the form `q_a(x_C) + λ_a·x_{j(a)}` — **at most one private coordinate per row**. So each residual's private part is supported on a single coordinate `j(a)`, and the corrected mechanism (`lambda_first_multiblock.md`: a leak arises when rows sharing a private part have different boundary parts) becomes a count:

> **Cluster the rows by their private coordinate `j`. Let `d_j` be the number of DISTINCT residual boundary parts among the rows in cluster `j`. Then**
>   **`λ ≤ Σ_j (d_j − 1)`.**

Each cluster's dependencies are spanned by differences of its members, and a difference's boundary image is nonzero exactly when the two boundary parts differ; a cluster with `d_j` distinct boundary parts contributes at most `d_j − 1` independent such images.

Checks on the campaign's two worked families:
- **NAE star** (three rows, one private `q`, boundary partners `z_1, z_2, z_3` all distinct): `d = 3`, bound `λ ≤ 2` — matching the certificate I computed by hand, and consistent with the exhaustive optimum `λ = 1` (one of the two dependencies happens to kill the boundary as well).
- **NAE path child** (two rows, one private, *identical* residual `a + b_{2i−1}`): `d = 1`, bound `λ ≤ 0` — matching the exact computation.

## 2. Combining with the packet's own core bound

S9's Theorem 1 puts every residual's private projection inside `span Q_{C∪N₀}` with `|C ∪ N₀| ≤ (2κ+1)L`. That is exactly the number of private coordinates available to be cluster labels. Writing `D := max_j d_j` (the **boundary multiplicity** — the largest number of distinct boundary partners any one private coordinate carries):

  **`λ ≤ Σ_j (d_j − 1) ≤ (D − 1)·(2κ + 1)·L`.**

So, immediately:

> **On horn 2 (bounded congestion, `κ = O(1)`): `λ = O(D·L)`.**
> **Absorption therefore follows from a bounded boundary multiplicity — a checkable structural hypothesis — replacing a clause the packet proved underivable from sparsity, bounded support, or bounded incidence degree (S9 §5).**

Combined with the second-horn reduction (`second_horn_reduction.md`), horn 2 closes as soon as `D = O(1)`; and under the campaign's scoped coefficient relief (W1, which needs only `o(log n)`), it closes as soon as **`D = o(log n)`**.

## 3. Where this lands — the same threshold, a fourth time

The dossier's class definition excludes blocks with an "`o(log n)` ordinary star core" (S6 p.123). A star core is *precisely* one private coordinate carrying many distinct boundary partners — i.e. large `D`. **So the class's own exclusion clause is a lower bound on boundary multiplicity: class members may have `D ≥ log n`, and are excluded when `D = o(log n)`.**

Read against §2 this is exact rather than suggestive:
- `D = o(log n)` ⟹ `λ = o(log n)·L` ⟹ horn 2 closes by W1.
- The class is *defined* to exclude exactly that regime.

**So horn 2's entire difficulty is boundary multiplicity at or above `log n`**, and the packet's star-core exclusion is not a technical convenience — it is the exclusion of the regime where absorption is provable. This is the fourth independent appearance of the `log n` threshold in this campaign (the transfer lane's W1; the rank lane's forced support-rank deficit; the Layer-III margin ratio; now boundary multiplicity), and the first time it has been located inside clause (ii) rather than clause (i).

## 4. Honest status

- §1's count is elementary but is an **upper bound**: `λ` can be strictly smaller when a cluster's dependencies also annihilate the boundary (the star's exhaustive optimum 1 versus the bound 2 is exactly that). So `D = O(1)` is **sufficient**, not necessary.
- §2 uses S9's Theorem 1 as a black box — proved in the dossier, and re-derived in structure by the rank lane (R3), but its constant is theirs.
- Everything is conditional on the second-horn reduction, which is conditional on **T1a, still unrefereed**. That chain is now three links long and the campaign's rule against building on T1a applies with more force, not less.
- Nothing here bears on horn 1, where the forced `Θ(log n)` rank deficit stands, nor on the block-internal certificate for dense connector-incoherent cores. The conjecture is OPEN.

**Next concrete step:** decide whether a *residual-class* block can actually have `D ≥ log n` while satisfying its other defining conditions — in particular whether high boundary multiplicity is compatible with `corank ≥ 5` and with the singleton-layer condition, or whether the class's clauses conflict here. That is a structural question about the class definition itself, answerable without the missing tree, and it is the same "is the class inhabited?" question the campaign keeps arriving at from new directions.
