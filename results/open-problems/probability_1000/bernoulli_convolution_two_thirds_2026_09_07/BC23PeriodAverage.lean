import Mathlib.Analysis.SpecialFunctions.Complex.Circle
import Mathlib.Analysis.SpecialFunctions.Trigonometric.Basic
import Mathlib.Algebra.BigOperators.Ring.Finset
import Mathlib.Algebra.Field.GeomSum
import Mathlib.Data.Fintype.BigOperators
import Mathlib.Algebra.BigOperators.Fin
import Mathlib.Tactic.Common
import Mathlib.Tactic.Linarith
import Mathlib.Tactic.NormNum
import Mathlib.Tactic.Ring

/-!
# The exact full-period average

Let `n : Fin (K+1) → ℤ` be frequencies and `N` a modulus. Expanding
`∏ i, (1 + e(k n i / N) / 2 + e(-k n i / N) / 2)` into characters and averaging over a full period
leaves exactly the terms whose frequency `∑ i, eps i * n i` is divisible by `N`.

For `n i = 2^i 3^(K-i)` and `N = 3^(K+1)` the dissociateness lemma of `BC23Dissociate` says only
`eps = 0` survives, so the average is `1`; dividing by `2^(K+1)` gives the average of
`∏ cos²(π k 2^i / 3^(i+1))` as `2^(-K-1)` exactly.

This file carries the expansion step; orthogonality is in `BC23Orthogonality`.
-/

open Finset Complex

namespace BC23

noncomputable def ee (t : ℝ) : ℂ := Complex.exp (2 * Real.pi * Complex.I * t)

lemma ee_add (s t : ℝ) : ee (s + t) = ee s * ee t := by
  unfold ee
  rw [← Complex.exp_add]
  push_cast
  ring_nf

lemma ee_zero : ee 0 = 1 := by simp [ee]

/-- `1 + cos θ` as the three characters `1`, `e(θ)/2`, `e(-θ)/2`. -/
lemma one_add_cos (t : ℝ) :
    (1 : ℂ) + Real.cos (2 * Real.pi * t) = 1 + ee t / 2 + ee (-t) / 2 := by
  unfold ee
  set w : ℂ := ((2 * Real.pi * t : ℝ) : ℂ) with hw
  have h2 : 2 * Complex.cos w = Complex.exp (w * Complex.I) + Complex.exp (-w * Complex.I) :=
    Complex.two_cos w
  have hcast : ((Real.cos (2 * Real.pi * t) : ℝ) : ℂ) = Complex.cos w := by
    rw [hw, Complex.ofReal_cos]
  have hL : (2 : ℂ) * Real.pi * Complex.I * (t : ℝ) = w * Complex.I := by
    rw [hw]; push_cast; ring
  have hR : (2 : ℂ) * Real.pi * Complex.I * ((-t : ℝ) : ℂ) = -w * Complex.I := by
    rw [hw]; push_cast; ring
  rw [hcast, hL, hR]
  linear_combination h2 / 2

/-- The three-term expansion of a product of `1 + cos` factors, as a sum over sign patterns. -/
theorem prod_one_add_cos (K : ℕ) (θ : Fin (K + 1) → ℝ) :
    (∏ i, ((1 : ℂ) + Real.cos (2 * Real.pi * θ i)))
      = ∑ s ∈ Fintype.piFinset (fun _ : Fin (K + 1) => ({-1, 0, 1} : Finset ℤ)),
          ∏ i, (if s i = 0 then (1 : ℂ) else ee ((s i : ℝ) * θ i) / 2) := by
  have hfac : ∀ i : Fin (K + 1),
      ((1 : ℂ) + Real.cos (2 * Real.pi * θ i))
        = ∑ j ∈ ({-1, 0, 1} : Finset ℤ), (if j = 0 then (1 : ℂ) else ee ((j : ℝ) * θ i) / 2) := by
    intro i
    have hm : ((-1 : ℤ) : ℝ) * θ i = -θ i := by push_cast; ring
    have hp : ((1 : ℤ) : ℝ) * θ i = θ i := by push_cast; ring
    rw [show ({-1, 0, 1} : Finset ℤ) = insert (-1 : ℤ) (insert (0 : ℤ) {(1 : ℤ)}) from rfl,
      Finset.sum_insert (by decide), Finset.sum_insert (by decide), Finset.sum_singleton]
    simp only [if_neg (by decide : (-1 : ℤ) ≠ 0), if_neg (by decide : (1 : ℤ) ≠ 0),
      if_pos]
    rw [one_add_cos (θ i), hm, hp]
    ring
  rw [Finset.prod_congr rfl (fun i _ => hfac i)]
  exact Finset.prod_univ_sum _ _

end BC23

#print axioms BC23.one_add_cos
#print axioms BC23.prod_one_add_cos
