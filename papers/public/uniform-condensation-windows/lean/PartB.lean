/-
Part B: the geometric sums of Sections 4 and 6.
Every closed form printed in the manuscript is restated here and proved.
-/
import Mathlib.Analysis.SpecificLimits.Normed

open Filter Topology

namespace Condensation

variable {a : ℝ}

private lemma inv_lt_one_of_one_lt (ha : 1 < a) : a⁻¹ < 1 := by
  rw [inv_lt_one_iff₀]; right; exact ha

private lemma inv_nonneg_of_one_lt (ha : 1 < a) : (0:ℝ) ≤ a⁻¹ := by
  have : (0:ℝ) < a := by linarith
  positivity

private lemma sub_one_ne (ha : 1 < a) : a - 1 ≠ 0 := ne_of_gt (by linarith)

private lemma one_sub_inv (ha : 1 < a) : (1 - a⁻¹) = (a - 1) / a := by
  have ha0 : (0:ℝ) < a := by linarith
  field_simp

/-- `T_L = \sum_{j\ge L} a^{1-j} = a^{2-L}/(a-1)`, written with nonnegative
exponents.  Section 6, the display defining `T_L`. -/
theorem T_closed (ha : 1 < a) (L : ℕ) :
    ∑' j : ℕ, a * (a⁻¹) ^ (j + L) = a ^ 2 * (a⁻¹) ^ L / (a - 1) := by
  have ha0 : (0:ℝ) < a := by linarith
  have hgeo : ∑' j : ℕ, (a⁻¹) ^ j = (1 - a⁻¹)⁻¹ :=
    tsum_geometric_of_lt_one (inv_nonneg_of_one_lt ha) (inv_lt_one_of_one_lt ha)
  have hre : ∑' j : ℕ, a * (a⁻¹) ^ (j + L) = a * (a⁻¹) ^ L * ∑' j : ℕ, (a⁻¹) ^ j := by
    rw [← tsum_mul_left]; congr 1; funext j; rw [pow_add]; ring
  rw [hre, hgeo, one_sub_inv ha]
  have h2 : ((a - 1) / a)⁻¹ = a / (a - 1) := by
    rw [inv_div]
  rw [h2]
  field_simp
  ring

/-- `U_L = \sum_{j\ge L} j a^{1-j} = a^{2-L}\bigl(L/(a-1)+1/(a-1)^2\bigr)`.
Section 6, the display defining `U_L`. -/
theorem U_closed (ha : 1 < a) (L : ℕ) :
    ∑' j : ℕ, ((j + L : ℕ) : ℝ) * (a * (a⁻¹) ^ (j + L))
      = a ^ 2 * (a⁻¹) ^ L * ((L : ℝ) / (a - 1) + 1 / (a - 1) ^ 2) := by
  have ha0 : (0:ℝ) < a := by linarith
  have ha1 : a - 1 ≠ 0 := sub_one_ne ha
  have hlt : a⁻¹ < 1 := inv_lt_one_of_one_lt ha
  have hnn : (0:ℝ) ≤ a⁻¹ := inv_nonneg_of_one_lt ha
  have hnorm : ‖a⁻¹‖ < 1 := by rwa [Real.norm_eq_abs, abs_of_nonneg hnn]
  have hgeo : ∑' j : ℕ, (a⁻¹) ^ j = (1 - a⁻¹)⁻¹ := tsum_geometric_of_lt_one hnn hlt
  have hgeo2 : ∑' j : ℕ, (j : ℝ) * (a⁻¹) ^ j = a⁻¹ / (1 - a⁻¹) ^ 2 :=
    tsum_coe_mul_geometric_of_norm_lt_one hnorm
  have hsum : Summable fun j : ℕ => (a⁻¹) ^ j := summable_geometric_of_lt_one hnn hlt
  have hsum2 : Summable fun j : ℕ => (j : ℝ) * (a⁻¹) ^ j := by
    have h := summable_norm_pow_mul_geometric_of_norm_lt_one (R := ℝ) 1 hnorm
    simpa using h.of_norm
  have hsplit : ∀ j : ℕ, ((j + L : ℕ) : ℝ) * (a * (a⁻¹) ^ (j + L))
      = (a * (a⁻¹) ^ L) * ((j : ℝ) * (a⁻¹) ^ j)
        + ((L : ℝ) * (a * (a⁻¹) ^ L)) * (a⁻¹) ^ j := by
    intro j; push_cast; rw [pow_add]; ring
  rw [tsum_congr hsplit, (hsum2.mul_left _).tsum_add (hsum.mul_left _),
      tsum_mul_left, tsum_mul_left, hgeo, hgeo2, one_sub_inv ha]
  have h2 : ((a - 1) / a)⁻¹ = a / (a - 1) := by rw [inv_div]
  rw [h2]
  field_simp
  ring

/-- Section 4, the coefficient computed inside the contractive kernel lemma:
`(D-1)` lags of size `a^{1-D}/(a-1)` plus the geometric tail
`\sum_{t\ge D} a^{-t}/(a-1)` total `a^{1-D}\bigl((D-1)/(a-1)+1/(a-1)^2\bigr)`. -/
theorem kernel_coeff_sum (ha : 1 < a) (D : ℕ) :
    ((D : ℝ) - 1) * (a * (a⁻¹) ^ D / (a - 1)) + (∑' t : ℕ, (a⁻¹) ^ (t + D)) / (a - 1)
      = a * (a⁻¹) ^ D * (((D : ℝ) - 1) / (a - 1) + 1 / (a - 1) ^ 2) := by
  have ha0 : (0:ℝ) < a := by linarith
  have ha1 : a - 1 ≠ 0 := sub_one_ne ha
  have hlt : a⁻¹ < 1 := inv_lt_one_of_one_lt ha
  have hnn : (0:ℝ) ≤ a⁻¹ := inv_nonneg_of_one_lt ha
  have hgeo : ∑' j : ℕ, (a⁻¹) ^ j = (1 - a⁻¹)⁻¹ := tsum_geometric_of_lt_one hnn hlt
  have htail : ∑' t : ℕ, (a⁻¹) ^ (t + D) = (a⁻¹) ^ D * (1 - a⁻¹)⁻¹ := by
    rw [← hgeo, ← tsum_mul_left]; congr 1; funext t; rw [pow_add]; ring
  rw [htail, one_sub_inv ha]
  have h2 : ((a - 1) / a)⁻¹ = a / (a - 1) := by rw [inv_div]
  rw [h2]
  field_simp
  ring

/-- Section 4, equation for `Θ`: multiplying that coefficient by `C_a = 2a^2`
gives the manuscript's `Θ(a,D) = 2a^{3-D}((D-1)/(a-1) + 1/(a-1)^2)`. -/
theorem Theta_eq (a : ℝ) (D : ℕ) :
    2 * a ^ 2 * (a * (a⁻¹) ^ D * (((D : ℝ) - 1) / (a - 1) + 1 / (a - 1) ^ 2))
      = 2 * a ^ 3 * (a⁻¹) ^ D * (((D : ℝ) - 1) / (a - 1) + 1 / (a - 1) ^ 2) := by
  ring

end Condensation

#print axioms Condensation.T_closed
#print axioms Condensation.U_closed
#print axioms Condensation.kernel_coeff_sum
#print axioms Condensation.Theta_eq
