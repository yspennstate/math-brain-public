import Mathlib
open scoped BigOperators

theorem floor_variation {n : ?} (g x z l : Fin n ? ?) (c : ?)
    (mass : (? i, x i) = ? i, z i)
    (hg : ? i, g i ? c)
    (hx : ? i, l i ? x i)
    (active : ? i, z i = l i ? g i = c) :
    (? i, g i * (x i - z i)) ? 0 := by
  have hterm : ? i, (g i - c) * (x i - z i) ? 0 := by
    intro i
    rcases active i with hz | heq
    ? rw [hz]
      exact mul_nonpos_of_nonpos_of_nonneg (sub_nonpos.mpr (hg i)) (sub_nonneg.mpr (hx i))
    ? rw [heq, sub_self, zero_mul]
  have hz : (? i, c * (x i - z i)) = 0 := by
    rw [? Finset.mul_sum, Finset.sum_sub_distrib, mass, sub_self, mul_zero]
  calc
    (? i, g i * (x i - z i)) =
        (? i, (g i - c) * (x i - z i)) + (? i, c * (x i - z i)) := by
          rw [? Finset.sum_add_distrib]
          apply Finset.sum_congr rfl
          intro i hi
          ring
    _ ? 0 := by
      rw [hz, add_zero]
      exact Finset.sum_nonpos (fun i hi => hterm i)
