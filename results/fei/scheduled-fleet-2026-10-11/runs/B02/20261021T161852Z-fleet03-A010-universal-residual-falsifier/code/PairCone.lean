import Mathlib

theorem pair_packing_determinant (p q r : ℝ) (hp : 0 < p) (hq : 0 < q) :
    (4*r/q + 4*r/p ≤ 1) ↔ (p-4*r)*(q-4*r)-16*r^2 ≥ 0 := by
  have hid : 4*r/q + 4*r/p = 4*r*(p+q)/(p*q) := by
    field_simp [ne_of_gt hp, ne_of_gt hq]
    <;> ring
  rw [hid, div_le_iff₀ (mul_pos hp hq)]
  constructor <;> intro h <;> nlinarith

theorem asymmetric_pair_falsifier :
    (2:ℚ)/3 * (5/18) < 4*(1/18)*((2:ℚ)/3+5/18) := by
  norm_num
