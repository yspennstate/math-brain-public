/-
Entropy obstruction for the full matrix algebra.

This file formalizes the elementary algebraic core of Proposition
`prop:obstruct` in `paper12/matrix_spencer_lifts.tex`.

Setting: a finite block algebra `B = ⨁_α M_{r_α}(ℂ)` has

  dim B   = ∑_α r_α²      (sum of squares of the block sizes),
  Ent(B)  = (max_α r_α) · (∑_α r_α).

The whole content of the obstruction is the inequality

  ∑_α r_α² ≤ (max_α r_α) · (∑_α r_α),

together with its immediate corollary: if a `D × D` matrix algebra is hit by a
linear surjection from `B`, then `dim B = ∑ r_α² ≥ D²`, hence
`Ent(B) = (max_α r_α)(∑_α r_α) ≥ D²`.

We give two formulations of the key inequality:

* `sq_sum_le_max_mul_sum`     — with an explicit upper bound `M` for the block
                                sizes (the most reusable form: `M` plays the
                                role of `max_α r_α`);
* `sq_sum_le_sup'_mul_sum`    — using `Finset.sup'`, i.e. the genuine maximum
                                over a nonempty index set.

and the two corollaries

* `entropy_ge_of_dim_ge`      — `D² ≤ ∑ r_α²  →  D² ≤ M · ∑ r_α`;
* `entropy_ge_of_dim_ge_sup'` — the same with the genuine maximum.

The statements are given over `ℝ` (with a nonnegativity hypothesis, since the
`r_α` are real block dimensions). Natural-number versions, where
nonnegativity is automatic, are recorded at the end.

Compiles against `mathlib` (see `README.md`).
-/

import Mathlib.Algebra.Order.BigOperators.Ring.Finset
import Mathlib.Algebra.Order.BigOperators.Group.Finset
import Mathlib.Algebra.BigOperators.Ring.Finset
import Mathlib.Data.Real.Basic
import Mathlib.Data.Finset.Lattice.Fold
import Mathlib.Tactic

open Finset

namespace EntropyObstruction

/-! ### The key inequality, with an explicit upper bound `M` -/

/-- **Entropy obstruction, core inequality.**
For nonnegative reals `r α` indexed by a finite set `s`, if `M` dominates every
`r α` (think `M = max_α r_α`), then

  `∑_{α ∈ s} (r α)² ≤ M · ∑_{α ∈ s} r α`.

Proof: termwise, `(r α)² = r α * r α ≤ M * r α` because `r α ≤ M` and
`0 ≤ r α`; then sum and pull `M` out of the sum. -/
theorem sq_sum_le_max_mul_sum
    {ι : Type*} (s : Finset ι) (r : ι → ℝ) (M : ℝ)
    (hr : ∀ α ∈ s, 0 ≤ r α) (hM : ∀ α ∈ s, r α ≤ M) :
    (∑ α ∈ s, (r α) ^ 2) ≤ M * ∑ α ∈ s, r α := by
  -- Bound each summand `(r α)^2` by `M * r α`.
  have hterm : ∀ α ∈ s, (r α) ^ 2 ≤ M * r α := by
    intro α hα
    have h1 : (r α) ^ 2 = r α * r α := by ring
    rw [h1]
    -- `r α * r α ≤ M * r α` from `r α ≤ M` and `0 ≤ r α`.
    exact mul_le_mul_of_nonneg_right (hM α hα) (hr α hα)
  calc
    (∑ α ∈ s, (r α) ^ 2) ≤ ∑ α ∈ s, M * r α := Finset.sum_le_sum hterm
    _ = M * ∑ α ∈ s, r α := by rw [Finset.mul_sum]

/-- **Entropy obstruction, corollary with explicit bound.**
If `D² ≤ ∑_α r_α²` (the dimension constraint coming from surjectivity onto
`M_D(ℂ)`) and `M` dominates the block sizes, then `D² ≤ M · ∑_α r_α`, i.e. the
reduced entropy is at least `D²`. -/
theorem entropy_ge_of_dim_ge
    {ι : Type*} (s : Finset ι) (r : ι → ℝ) (M D : ℝ)
    (hr : ∀ α ∈ s, 0 ≤ r α) (hM : ∀ α ∈ s, r α ≤ M)
    (hdim : D ^ 2 ≤ ∑ α ∈ s, (r α) ^ 2) :
    D ^ 2 ≤ M * ∑ α ∈ s, r α :=
  le_trans hdim (sq_sum_le_max_mul_sum s r M hr hM)

/-! ### The same statements with the genuine maximum `Finset.sup'` -/

/-- **Entropy obstruction with the genuine maximum.**
Over a *nonempty* index set `s`, with `r α ≥ 0`, the maximum
`s.sup' hs r = max_{α ∈ s} r α` satisfies

  `∑_{α ∈ s} (r α)² ≤ (max_{α ∈ s} r α) · ∑_{α ∈ s} r α`.

This is `sq_sum_le_max_mul_sum` instantiated at `M = s.sup' hs r`, whose
domination property is exactly `Finset.le_sup'`. -/
theorem sq_sum_le_sup'_mul_sum
    {ι : Type*} (s : Finset ι) (hs : s.Nonempty) (r : ι → ℝ)
    (hr : ∀ α ∈ s, 0 ≤ r α) :
    (∑ α ∈ s, (r α) ^ 2) ≤ (s.sup' hs r) * ∑ α ∈ s, r α :=
  sq_sum_le_max_mul_sum s r (s.sup' hs r) hr (fun _ hα => Finset.le_sup' r hα)

/-- **Entropy obstruction corollary with the genuine maximum.** -/
theorem entropy_ge_of_dim_ge_sup'
    {ι : Type*} (s : Finset ι) (hs : s.Nonempty) (r : ι → ℝ) (D : ℝ)
    (hr : ∀ α ∈ s, 0 ≤ r α)
    (hdim : D ^ 2 ≤ ∑ α ∈ s, (r α) ^ 2) :
    D ^ 2 ≤ (s.sup' hs r) * ∑ α ∈ s, r α :=
  le_trans hdim (sq_sum_le_sup'_mul_sum s hs r hr)

/-! ### Natural-number versions

Here the block sizes are genuine matrix dimensions `r α : ℕ`, so the
nonnegativity hypothesis is automatic and the statements are clean. -/

/-- Natural-number form of the core inequality:
`∑_α (r α)² ≤ M · ∑_α r α` whenever `r α ≤ M` for all `α ∈ s`. -/
theorem sq_sum_le_max_mul_sum_nat
    {ι : Type*} (s : Finset ι) (r : ι → ℕ) (M : ℕ)
    (hM : ∀ α ∈ s, r α ≤ M) :
    (∑ α ∈ s, (r α) ^ 2) ≤ M * ∑ α ∈ s, r α := by
  have hterm : ∀ α ∈ s, (r α) ^ 2 ≤ M * r α := by
    intro α hα
    have h1 : (r α) ^ 2 = r α * r α := by ring
    rw [h1]
    exact Nat.mul_le_mul_right (r α) (hM α hα)
  calc
    (∑ α ∈ s, (r α) ^ 2) ≤ ∑ α ∈ s, M * r α := Finset.sum_le_sum hterm
    _ = M * ∑ α ∈ s, r α := by rw [Finset.mul_sum]

/-- Natural-number form of the corollary: the dimension lower bound `D² ≤ dim B`
propagates to the entropy lower bound `D² ≤ Ent(B)`. -/
theorem entropy_ge_of_dim_ge_nat
    {ι : Type*} (s : Finset ι) (r : ι → ℕ) (M D : ℕ)
    (hM : ∀ α ∈ s, r α ≤ M)
    (hdim : D ^ 2 ≤ ∑ α ∈ s, (r α) ^ 2) :
    D ^ 2 ≤ M * ∑ α ∈ s, r α :=
  le_trans hdim (sq_sum_le_max_mul_sum_nat s r M hM)

end EntropyObstruction
