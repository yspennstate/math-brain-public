# Lean formalization — paper12 (`matrix_spencer_lifts`)

Machine-checked companion lemmas for elementary arithmetic and index facts from
`../matrix_spencer_lifts.tex`.

## Files

- `EntropyObstruction.lean` — the algebraic core of Proposition `prop:obstruct`
  ("Entropy obstruction for the full matrix algebra"):
  - `sq_sum_le_max_mul_sum`: for nonnegative reals `r α` over a finite set `s`
    and any upper bound `M ≥ r α`,
    `∑_α (r α)² ≤ M · ∑_α r α`;
  - `entropy_ge_of_dim_ge`: if `D² ≤ ∑_α (r α)²` then `D² ≤ M · ∑_α r α`
    (the dimension lower bound `dim B ≥ D²` propagates to the entropy lower
    bound `Ent(B) ≥ D²`);
  - `sq_sum_le_sup'_mul_sum` / `entropy_ge_of_dim_ge_sup'`: the same two
    statements with the genuine maximum `Finset.sup'` over a nonempty index set,
    i.e. literally `(max_α r α)`;
  - `sq_sum_le_max_mul_sum_nat` / `entropy_ge_of_dim_ge_nat`: natural-number
    versions (block sizes `r α : ℕ`, so nonnegativity is automatic).

- `BandedInterior.lean` — the counting identity behind Lemma `lem:band`
  ("Finite-section lower bound for banded symbols"):
  - `card_interiorRows`: the interior rows `w ≤ r < d - w` of a `d × d` banded
    section number exactly `d - 2w` when `2w ≤ d`;
  - `mem_interiorRows_iff_le`: this matches the paper's index range
    `w ≤ r ≤ d - 1 - w`;
  - `card_interiorRows_pos`: the count is positive when `2w < d` (the
    hypothesis `d > 2w` of the lemma).

- `MultilevelInteriorCount.lean` — the multilevel (tensor-product) interior
  count behind Lemma `lem:bandml`. For a box `∏_j [0, d_j)` of multi-indices
  with per-axis half-bandwidth `w_j` and `d_j > 2 w_j`, a multi-index is
  *fully interior* when it is interior in every coordinate
  (`w_j ≤ m_j ≤ d_j - 1 - w_j`, equivalently `w_j ≤ m_j < d_j - w_j`):
  - `interiorIndices`: the set of fully-interior multi-indices, defined as the
    dependent product (`Fintype.piFinset`) of the per-axis interior-row sets
    `BandedInterior.interiorRows (d j) (w j)`;
  - `mem_interiorIndices` / `mem_interiorIndices_iff_le`: membership unfolds to
    "interior in every coordinate", in the `w_j ≤ m_j < d_j - w_j` form and in
    the paper's `w_j ≤ m_j ≤ d_j - 1 - w_j` form;
  - `card_interiorIndices`: when `2 w_j ≤ d_j` on every axis, the count is
    exactly `∏_j (d_j - 2 w_j)` — proved by reducing through
    `Fintype.card_piFinset` to the one-dimensional
    `BandedInterior.card_interiorRows`, which it reuses verbatim;
  - `card_interiorIndices_pos`: the count is positive when `2 w_j < d_j` on
    every axis (the hypothesis `d_j > 2 w_j` of the lemma);
  - `card_interiorIndices_fin` / `card_interiorIndices_fin_pos`: the same two
    results specialized to `ι := Fin r`, i.e. the paper's `r`-fold box
    `∏_{j : Fin r} [0, d_j)`.

  This file imports `BandedInterior` as a module, so check it after building
  `BandedInterior.olean` (see below).

- `GridNorming.lean` — the arithmetic core of Lemma `lem:grid`
  ("Grid norming"). With `r` axes `j`, grid sizes `G j > 0`, and point counts
  `N j : ℕ`, the design choice `G j ≥ 8 r (N j)` (when `N j ≥ 1`) forces the
  total normalized count below `1/8` (the paper's `π/8`, stated without the
  `π`):
  - `term_le`: the one-axis bound `(N j : ℝ) / G j ≤ 1 / (8 r)`, obtained from
    `8 r (N j) ≤ G j` (and `0 ≤ 1 / (8 r)` in the degenerate case `N j = 0`);
  - `grid_sum_le`: for axes indexed by `Fin r`,
    `∑_{j : Fin r} (N j : ℝ) / G j ≤ 1 / 8` — the `r` per-axis bounds summed
    via `Finset.sum_le_sum` and `Finset.sum_const`, giving `r · (1 / (8 r))`;
  - `grid_sum_le_finset`: the same telescoping inequality over an arbitrary
    finite index set `s`, with `r := s.card`.

- `TensorReversal.lean` - the finite-index arithmetic behind the
  Hankel-to-Toeplitz part of Lemma `lem:tensorrev`; the matrix-level
  orthogonality/symmetry of `\mathbf J_\Lambda` is handled separately in
  `ReversalSymmetry.lean`:
  - `rev_involutive`: one-dimensional reversal `j -> d - 1 - j` is an
    involution on `Fin d`;
  - `hankel_to_toeplitz_index`: after reversal, a Hankel sum index becomes the
    fixed anti-diagonal center plus a Toeplitz lag,
    `i + (d - 1 - j) = (d - 1) + (i - j)`;
  - `revIndex_involutive` / `tensor_hankel_to_toeplitz_index`: the same
    statements coordinatewise on a multilevel box;
  - `centeredHankelBand_iff_lagInBand`: centered Hankel bandedness is exactly
    Toeplitz lag bandedness after subtracting the anti-diagonal center.

- `ReversalSymmetry.lean` — the matrix-level half of Lemma `lem:tensorrev` that
  `TensorReversal.lean` leaves out: the reversal `J_Λ` (the exchange matrix
  `i ↦ d - 1 - i`) is a symmetric orthogonal involution. It imports
  `TensorReversal` and reuses its involution lemmas:
  - `revIdx_symm`: the index equivalence `i = revIdx j ↔ j = revIdx i`
    (`revIdx i = d - 1 - i`), i.e. the `(i, j)` entry of the reversal matrix
    equals its `(j, i)` entry — the elementary symmetry behind everything else;
  - `revPerm`: the reversal packaged as an `Equiv.Perm (Fin d)` via
    `Function.Involutive.toPerm` of `TensorReversal.rev`, with
    `revPerm_symm_apply` restating `revIdx_symm` on the permutation;
  - `revPerm_symm` / `revPerm_inv` / `revPerm_mul_self`: `J` is its own inverse,
    `J.symm = J`, `J⁻¹ = J`, `J * J = 1` (the involution as a group element);
  - `transpose_permMatrix_revPerm`: over any `R` with `0, 1` the permutation
    matrix is **symmetric**, `Jᵀ = J`, and
    `transpose_permMatrix_revPerm_eq_inv` gives **orthogonality** `Jᵀ = J⁻¹`,
    both read off from mathlib's `Matrix.transpose_permMatrix`;
  - `revIndexPerm` / `revIndexPerm_inv` / `transpose_permMatrix_revIndexPerm`:
    the same for the coordinatewise tensor reversal `⨂_a J` on a finite box.

  Like `MultilevelInteriorCount.lean`, this file imports the `TensorReversal`
  module, so check it after building `TensorReversal.olean` (see below).

- `MultilevelBandConstant.lean` — the normalized constant tracked through Lemma
  `lem:bandml`. With `r` axes, section lengths `d_j > 0` and half-bandwidths
  `w_j`, the quarter-band design choice `d_j ≥ 4 w_j` keeps each interior ratio
  `(d_j - 2 w_j)/d_j` at or above `1/2`, so the multilevel constant stays above
  `(1/2)^r`. This is the real-valued companion of `MultilevelInteriorCount.lean`
  (which counts the interior multi-indices exactly):
  - `factor_ge` / `factor_nonneg`: the one-axis bound
    `1/2 ≤ (d - 2 w)/d` (and `0 ≤ (d - 2 w)/d`) from `4 w ≤ d` and `d > 0`;
  - `band_const_ge`: over `r` axes `j : Fin r`,
    `(1/2)^r ≤ ∏_{j} (d_j - 2 w_j)/d_j`, lifting the per-axis bound to the
    product against the constant `1/2` via `Finset.prod_le_prod`;
  - `band_const_ge_finset`: the same over an arbitrary index `Finset s`, with
    the exponent `s.card`;
  - `band_const_ge_nat`: the `Fin r` statement with natural-number
    half-bandwidths `w_j : ℕ`, so the hypothesis is the integer band condition
    `4 w_j ≤ d_j`.

- `EntropyAbsorption.lean` — the constant-absorption bookkeeping that lets the
  paper fold stray constants into the universal constant `C`. Four bookkeeping
  facts used throughout `../matrix_spencer_lifts.tex`:
  - entropy under doubling (`thm:lift`, complex case): with `Ent = h · R`,
    Hermitian dilation sends `h → 2h`, `R → 2R`, so `Ent → 4 · Ent`
    (`ent_double`), and dilation followed by realification doubles each twice,
    `Ent → 16 · Ent` (`ent_double_double`) — the verbatim "factor of four" /
    "factor of at most 16" of the proof; `ent_double_nat` /
    `ent_double_double_nat` give the natural-number forms; tensor amplification
    by `M_c` multiplies both `h` and `R` by `c`, so `Ent -> c^2 Ent`
    (`ent_tensor_amplification` / `ent_tensor_amplification_nat`);
  - direct-sum entropy warning (`direct_sum_entropy_sum_le` /
    `direct_sum_entropy_sum_le_sup` / `direct_sum_entropy_sum_lt` /
    `direct_sum_entropy_sum_eq_of_height_eq` /
    `direct_sum_entropy_sum_mono` /
    `direct_sum_entropy_sum_mono_subset` /
    `direct_sum_entropy_zero_ranks` / `direct_sum_entropy_sum_union_disjoint`):
    if every block height is at most
    `H`, then `sum_l h_l R_l <= H * sum_l R_l`, with equality when every block
    height is exactly `H`;
    specializing to `H = max_l h_l` gives the finite-maximum wrapper
    `direct_sum_entropy_sum_le_sup`, and if one positive-rank block has height
    strictly below `H`, this is strict; componentwise enlargement of heights and
    reduced dimensions, or enlargement of the finite index set, only increases
    the finite entropy sum; if all reduced dimensions vanish, the component
    entropy sum vanishes; over a disjoint union of block families, the component
    entropy sum splits additively; this is the arithmetic reason the direct-sum
    entropy is governed by the maximum block height, not generally by the sum of
    the component entropies;
  - log absorption (`log_absorb_const`): for `x ≥ 0` and `c ≥ 1`,
    `log(e + c·x) ≤ (1 + log c)·log(e + x)`, the inequality that absorbs a
    constant inside every `log(e + Ent/n)` (e.g. the `c = 16` above) at the cost
    of the leading factor `1 + log c`; proved from `e + c·x ≤ c·(e + x)`
    (`e_add_mul_le`) and `log(e + x) ≥ 1` (`one_le_log_e_add`, since
    `e + x ≥ exp 1`);
  - norming-set count (`norming_card_ge`): an injection of the `(2w+1)^r`
    multi-indices into a norming set `Q` gives `(2w+1)^r ≤ Q.card`, via
    `Fintype.card_le_of_injective` — the `|Q| ≥ (2w+1)^r` step behind the
    `log(e + (2w+1)^r / n)` lower bound.

No file uses `sorry` or `admit`.

## Toolchain status

A Lean 4 toolchain is installed on this machine via `elan`:

- `elan` 4.2.1
- Lean / Lake toolchain `leanprover/lean4:v4.29.1` (installed); `stable`
  resolves to `v4.30.0`.

A fully built `mathlib` (pinned to tag `v4.29.1`, with compiled `.olean`
files) is present locally under a sibling project, so `import Mathlib...`
resolves with no network access and no rebuild. The `lean-toolchain` here
pins `v4.29.1` to match it.

## Verification result

All eight files were compiled with `lean` against the local `mathlib` and check
clean (exit code 0, no errors, no warnings, no `sorry`). A negative control — a
false statement left as `sorry` — was confirmed to trigger the
`` declaration uses `sorry` `` warning under this same toolchain, so the clean
compile of the real files is a genuine proof-checked pass.

## How to check it yourself

### Option A — direct `lean` invocation (what was used here; no Lake needed)

Point `LEAN_PATH` at the built `mathlib` (and its dependency) `.olean`
directories and run `lean` on each file. With the sibling build at
`~\phase_retrieval_omega\lean\omega_comb` (PowerShell):

```powershell
$pkgs = "~\phase_retrieval_omega\lean\omega_comb\.lake\packages"
$dirs = "mathlib","batteries","aesop","Qq","proofwidgets","importGraph","LeanSearchClient","plausible" |
        ForEach-Object { Join-Path $pkgs "$_\.lake\build\lib\lean" }
$env:LEAN_PATH = ($dirs -join ";")
$lean = "$env:USERPROFILE\.elan\toolchains\leanprover--lean4---v4.29.1\bin\lean.exe"
& $lean .\EntropyObstruction.lean
& $lean .\BandedInterior.lean
& $lean .\GridNorming.lean
& $lean .\TensorReversal.lean
& $lean .\MultilevelBandConstant.lean
& $lean .\EntropyAbsorption.lean

# MultilevelInteriorCount.lean imports the BandedInterior module, and
# ReversalSymmetry.lean imports the TensorReversal module, so first emit those
# .oleans and put the current directory on LEAN_PATH:
& $lean -o .\BandedInterior.olean .\BandedInterior.lean
& $lean -o .\TensorReversal.olean .\TensorReversal.lean
$env:LEAN_PATH = ".;$env:LEAN_PATH"
& $lean .\MultilevelInteriorCount.lean
& $lean .\ReversalSymmetry.lean
```

A `0` exit code with no error output means the proofs check.

### Option B — a standalone Lake project with its own mathlib

If you do not have a local mathlib build, create a fresh project that
downloads it (multi-GB; needs network):

```bash
elan toolchain install leanprover/lean4:v4.29.1   # match these files' toolchain
lake new paper12_lean math                         # or add to an existing project
# in lakefile.toml: require mathlib @ "v4.29.1"
lake exe cache get                                 # fetch prebuilt mathlib oleans
# copy the .lean files into the lib source dir
lake build
```

`lakefile.toml` and `lean-toolchain` in this directory are configured for
Option A (mathlib required by local path to the sibling build); adjust the
`require` line to a git/version require for Option B.
