/-
Multilevel banded constant `∏_j (d_j - 2 w_j) / d_j ≥ (1/2)^r`.

This file formalizes the constant tracked through Lemma `lem:bandml` (the
multilevel / tensor-product finite-section bound) in
`paper12/matrix_spencer_lifts.tex`.

Setting: there are `r` axes `j`. On axis `j` the section has length `d_j > 0`
and half-bandwidth `w_j`, and the one-dimensional finite-section bound
contributes the ratio of interior rows to all rows,

  (d_j - 2 w_j) / d_j   =   1 - 2 w_j / d_j.

Under the design choice `d_j ≥ 4 w_j` on every axis (each band occupies at most
a quarter of its section), this ratio is at least `1/2`, so the multilevel
constant — the product over the `r` axes — is at least `(1/2)^r`:

  ∏_j (d_j - 2 w_j) / d_j   ≥   (1/2)^r.

This is the real-valued companion of `MultilevelInteriorCount.lean`, which
counts the fully-interior multi-indices exactly (`∏_j (d_j - 2 w_j)` over `ℕ`);
here we record the `r`-uniform lower bound on the *normalized* product that
enters the operator-norm estimate.

The argument is a per-axis bound followed by a product of `r` factors:

* each factor satisfies `(d_j - 2 w_j) / d_j ≥ 1 / 2` — for `d_j ≥ 4 w_j` this
  is `4 w_j ≤ d_j` divided through by `d_j > 0` (and the factor stays in
  `[1/2, 1]`, in particular nonnegative);
* there are `r` factors, so `∏_j (d_j - 2 w_j) / d_j ≥ ∏_j (1/2) = (1/2)^r`
  via `Finset.prod_le_prod` against the constant `1/2`.

The main statement `band_const_ge` indexes over `Fin r` so the exponent is
literally `r`. A version `band_const_ge_finset` over an arbitrary `Finset`
(with the exponent its cardinality) is also given.

Compiles against `mathlib` (see `README.md`).
-/

import Mathlib.Algebra.Order.BigOperators.Ring.Finset
import Mathlib.Algebra.Order.Field.Basic
import Mathlib.Data.Real.Basic
import Mathlib.Tactic

open Finset

namespace MultilevelBandConstant

/-! ### The per-axis bound -/

/-- **Per-axis banded factor bound.**
Fix a section length `d > 0` and half-bandwidth `w : ℕ`.  If the band occupies
at most a quarter of the section, `4 w ≤ d`, then the normalized interior ratio
on this axis is at least `1/2`:

  `(d - 2 w) / d ≥ 1 / 2`.

(The ratio is also `≤ 1`, but only the lower bound is needed downstream.)
The proof divides `4 w ≤ d`, i.e. `2 w ≤ d / 2`, through by `d > 0`. -/
theorem factor_ge
    (d w : ℝ) (hd : 0 < d) (hband : 4 * w ≤ d) :
    1 / 2 ≤ (d - 2 * w) / d := by
  rw [le_div_iff₀ hd]
  -- goal: `1 / 2 * d ≤ d - 2 * w`, i.e. `4 w ≤ d` after rearranging.
  linarith

/-- The banded factor is nonnegative under the same hypothesis (a consequence
of `factor_ge`, recorded for the product bound). -/
theorem factor_nonneg
    (d w : ℝ) (hd : 0 < d) (hband : 4 * w ≤ d) :
    0 ≤ (d - 2 * w) / d :=
  le_trans (by norm_num) (factor_ge d w hd hband)

/-! ### The product over `Fin r` -/

/-- **Multilevel banded constant bound (`lem:bandml`, normalized constant).**
With `r` axes `j : Fin r`, section lengths `d j > 0`, and half-bandwidths
`w j : ℕ`, suppose each axis satisfies the quarter-band design choice

  `4 * (w j) ≤ d j`.

Then the multilevel constant — the product of the per-axis interior ratios —
is at least `(1/2)^r`:

  `(1 / 2) ^ r ≤ ∏_{j : Fin r} (d j - 2 * (w j)) / d j`.

Proof: each factor is `≥ 1/2 ≥ 0` by `factor_ge` / `factor_nonneg`; the product
of the `r` constant lower bounds is `∏_j (1/2) = (1/2)^r`, and
`Finset.prod_le_prod` lifts the termwise bound to the products. -/
theorem band_const_ge
    (r : ℕ) (d : Fin r → ℝ) (w : Fin r → ℝ)
    (hd : ∀ j, 0 < d j) (hband : ∀ j, 4 * w j ≤ d j) :
    (1 / 2 : ℝ) ^ r ≤ ∏ j : Fin r, (d j - 2 * w j) / d j := by
  -- Rewrite `(1/2)^r` as the product of `r` copies of the constant `1/2`.
  have hconst : (1 / 2 : ℝ) ^ r = ∏ _j : Fin r, (1 / 2 : ℝ) := by
    rw [Finset.prod_const, Finset.card_univ, Fintype.card_fin]
  rw [hconst]
  -- Termwise: `0 ≤ 1/2` and `1/2 ≤ (d j - 2 w j) / d j`.
  apply Finset.prod_le_prod
  · intro j _
    norm_num
  · intro j _
    exact factor_ge (d j) (w j) (hd j) (hband j)

/-! ### The product over an arbitrary `Finset`

Same statement with the index set an arbitrary `Finset ι`; the "number of axes"
`r` in the exponent is its cardinality. -/

/-- **Multilevel banded constant bound over a general index `Finset`.**
For a finite index set `s` with `r := s.card`, section lengths `d j > 0`, and
half-bandwidths `w j : ℕ` satisfying `4 * (w j) ≤ d j` on every axis in `s`,

  `(1 / 2) ^ (s.card) ≤ ∏_{j ∈ s} (d j - 2 * (w j)) / d j`.

The proof is identical: each factor is `≥ 1/2 ≥ 0`, and the `s.card` constant
lower bounds multiply to `(1/2)^(s.card)`. -/
theorem band_const_ge_finset
    {ι : Type*} (s : Finset ι) (d : ι → ℝ) (w : ι → ℝ)
    (hd : ∀ j ∈ s, 0 < d j) (hband : ∀ j ∈ s, 4 * w j ≤ d j) :
    (1 / 2 : ℝ) ^ s.card ≤ ∏ j ∈ s, (d j - 2 * w j) / d j := by
  have hconst : (1 / 2 : ℝ) ^ s.card = ∏ _j ∈ s, (1 / 2 : ℝ) := by
    rw [Finset.prod_const]
  rw [hconst]
  apply Finset.prod_le_prod
  · intro j _
    norm_num
  · intro j hj
    exact factor_ge (d j) (w j) (hd j hj) (hband j hj)

/-! ### Natural-number bandwidths

The bandwidths `w j` are genuine half-bandwidths `: ℕ` in the paper; the
casted form makes the design hypothesis `4 w_j ≤ d_j` read directly off the
integer band size. We record the `Fin r` statement in this form. -/

/-- The `Fin r` constant bound with natural-number half-bandwidths `w j : ℕ`
(cast into `ℝ`), so the hypothesis is the integer condition `4 * (w j) ≤ d j`
on the band size. -/
theorem band_const_ge_nat
    (r : ℕ) (d : Fin r → ℝ) (w : Fin r → ℕ)
    (hd : ∀ j, 0 < d j) (hband : ∀ j, 4 * (w j : ℝ) ≤ d j) :
    (1 / 2 : ℝ) ^ r ≤ ∏ j : Fin r, (d j - 2 * (w j : ℝ)) / d j :=
  band_const_ge r d (fun j => (w j : ℝ)) hd hband

end MultilevelBandConstant
