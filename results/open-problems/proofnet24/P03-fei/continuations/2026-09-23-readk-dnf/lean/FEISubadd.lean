import Mathlib

/-!
The elementary inequality used for the sets avoiding `j₀` in the proof of the strengthened
biased inequality for threshold gates: with `φ_s(x) = x log(s/x)`, for `s > 0` and `a², b² ≤ s`,

  `φ_s((a+b)²) ≤ 2 φ_s(a²) + 2 φ_s(b²) + 2a² + 2b²`.
-/

open Real

namespace FEISubadd

noncomputable def phi (s x : ℝ) : ℝ := x * Real.log (s / x)

theorem phi_zero (s : ℝ) : phi s 0 = 0 := by
  unfold phi
  simp

/-- `log u ≤ u / e` for `u > 0`. -/
theorem log_le_div_e (u : ℝ) (hu : 0 < u) : Real.log u ≤ u / Real.exp 1 := by
  have he : 0 < Real.exp 1 := Real.exp_pos 1
  have h := Real.log_le_sub_one_of_pos (div_pos hu he)
  rw [Real.log_div hu.ne' he.ne', Real.log_exp] at h
  linarith

/-- `x log(s/x) ≤ s/e` for `x, s > 0`. -/
theorem phi_le (s x : ℝ) (hs : 0 < s) (hx : 0 < x) : phi s x ≤ s / Real.exp 1 := by
  unfold phi
  have he : 0 < Real.exp 1 := Real.exp_pos 1
  have h := log_le_div_e (s / x) (div_pos hs hx)
  have h2 : x * Real.log (s / x) ≤ x * ((s / x) / Real.exp 1) := mul_le_mul_of_nonneg_left h hx.le
  have h3 : x * ((s / x) / Real.exp 1) = s / Real.exp 1 := by
    have hxne : x ≠ 0 := hx.ne'
    have hene : Real.exp 1 ≠ 0 := he.ne'
    field_simp
  linarith

/-- `φ_s ≥ 0` on `[0, s]`. -/
theorem phi_nonneg (s x : ℝ) (_hs : 0 < s) (hx : 0 ≤ x) (hxs : x ≤ s) : 0 ≤ phi s x := by
  rcases eq_or_lt_of_le hx with h | h
  · rw [← h, phi_zero]
  · unfold phi
    apply mul_nonneg hx
    apply Real.log_nonneg
    rw [le_div_iff₀ h]
    linarith

/-- `φ_s` is nondecreasing on `(0, s/e]`, in the form needed: if `0 < x ≤ y` and `log(s/y) ≥ 1`. -/
theorem phi_mono (s x y : ℝ) (hs : 0 < s) (hx : 0 < x) (hxy : x ≤ y) (hy : 1 ≤ Real.log (s / y)) :
    phi s x ≤ phi s y := by
  unfold phi
  have hy0 : 0 < y := lt_of_lt_of_le hx hxy
  have hxne : x ≠ 0 := hx.ne'
  have hyne : y ≠ 0 := hy0.ne'
  have h1 : Real.log (s / x) = Real.log (s / y) + Real.log (y / x) := by
    rw [← Real.log_mul (div_pos hs hy0).ne' (div_pos hy0 hx).ne']
    congr 1
    field_simp
  have h2 : Real.log (y / x) ≤ y / x - 1 := Real.log_le_sub_one_of_pos (div_pos hy0 hx)
  have hmul : x * Real.log (y / x) ≤ x * (y / x - 1) := mul_le_mul_of_nonneg_left h2 hx.le
  have h3 : x * (y / x - 1) = y - x := by
    field_simp
  have hprod : 0 ≤ (y - x) * (Real.log (s / y) - 1) :=
    mul_nonneg (sub_nonneg.mpr hxy) (sub_nonneg.mpr hy)
  rw [h1]
  nlinarith [hmul, h3, hprod]

/-- `t log(s/y) ≤ t log(s/t)` for `0 ≤ t ≤ y`, `y > 0`. -/
theorem term_le (s t y : ℝ) (hs : 0 < s) (ht : 0 ≤ t) (hty : t ≤ y) (hy : 0 < y) :
    t * Real.log (s / y) ≤ t * Real.log (s / t) := by
  rcases eq_or_lt_of_le ht with h | h
  · rw [← h]; simp
  · apply mul_le_mul_of_nonneg_left _ ht
    apply Real.log_le_log (div_pos hs hy)
    exact div_le_div_of_nonneg_left hs.le h hty

theorem subadd (s a b : ℝ) (hs : 0 < s) (ha : a ^ 2 ≤ s) (hb : b ^ 2 ≤ s) :
    phi s ((a + b) ^ 2) ≤ 2 * phi s (a ^ 2) + 2 * phi s (b ^ 2) + 2 * a ^ 2 + 2 * b ^ 2 := by
  have ha0 : 0 ≤ a ^ 2 := sq_nonneg a
  have hb0 : 0 ≤ b ^ 2 := sq_nonneg b
  have pa := phi_nonneg s (a ^ 2) hs ha0 ha
  have pb := phi_nonneg s (b ^ 2) hs hb0 hb
  have hxy : (a + b) ^ 2 ≤ 2 * a ^ 2 + 2 * b ^ 2 := by nlinarith [sq_nonneg (a - b)]
  have hx0 : 0 ≤ (a + b) ^ 2 := sq_nonneg (a + b)
  rcases eq_or_lt_of_le hx0 with hx | hx
  · rw [← hx, phi_zero]
    linarith
  · have hy : 0 < 2 * a ^ 2 + 2 * b ^ 2 := lt_of_lt_of_le hx hxy
    by_cases hcase : 1 ≤ Real.log (s / (2 * a ^ 2 + 2 * b ^ 2))
    · have m := phi_mono s ((a + b) ^ 2) (2 * a ^ 2 + 2 * b ^ 2) hs hx hxy hcase
      have t1 := term_le s (a ^ 2) (2 * a ^ 2 + 2 * b ^ 2) hs ha0 (by linarith) hy
      have t2 := term_le s (b ^ 2) (2 * a ^ 2 + 2 * b ^ 2) hs hb0 (by linarith) hy
      unfold phi at m pa pb ⊢
      have e1 : (2 * a ^ 2 + 2 * b ^ 2) * Real.log (s / (2 * a ^ 2 + 2 * b ^ 2))
          = 2 * (a ^ 2 * Real.log (s / (2 * a ^ 2 + 2 * b ^ 2)))
            + 2 * (b ^ 2 * Real.log (s / (2 * a ^ 2 + 2 * b ^ 2))) := by ring
      linarith
    · push Not at hcase
      have hlt : s / (2 * a ^ 2 + 2 * b ^ 2) < Real.exp 1 := by
        have h' : Real.log (s / (2 * a ^ 2 + 2 * b ^ 2)) < Real.log (Real.exp 1) := by
          rw [Real.log_exp]; exact hcase
        exact (Real.log_lt_log_iff (div_pos hs hy) (Real.exp_pos 1)).mp h'
      have hsy : s / Real.exp 1 < 2 * a ^ 2 + 2 * b ^ 2 := by
        rw [div_lt_iff₀ (Real.exp_pos 1)]
        rw [div_lt_iff₀ hy] at hlt
        linarith
      have pl := phi_le s ((a + b) ^ 2) hs hx
      linarith

end FEISubadd

#print axioms FEISubadd.subadd
