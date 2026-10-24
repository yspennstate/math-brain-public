import Mathlib.Data.Real.Basic
import Mathlib.Algebra.Order.BigOperators.Ring.Finset
import Mathlib.Tactic.Linarith

-- Algebra used in ATTEMPT.md (3.1), not the stochastic theorem.
theorem mass_gap_bound {I : Type*} (s : Finset I) (a : I → Real) (m : Real)
    (h0 : ∀ i ∈ s, 0 ≤ a i) (hm : ∀ i ∈ s, a i ≤ m) :
    (s.sum a) * ((s.sum a) - m) ≤
      (s.sum a)^2 - s.sum (fun i => (a i)^2) := by
  have hsq : s.sum (fun i => (a i)^2) ≤ m * (s.sum a) := by
    calc
      s.sum (fun i => (a i)^2) ≤ s.sum (fun i => m * a i) := by
        apply Finset.sum_le_sum
        intro i hi
        have hnon := h0 i hi
        have hmax := hm i hi
        simpa [pow_two] using (mul_le_mul_of_nonneg_right hmax hnon)
      _ = m * (s.sum a) := (Finset.mul_sum s a m).symm
  nlinarith
