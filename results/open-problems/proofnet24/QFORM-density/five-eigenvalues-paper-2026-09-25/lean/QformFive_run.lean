import Mathlib.Tactic
import Mathlib.Analysis.Complex.ExponentialBounds
import Mathlib.Analysis.Real.Pi.Bounds
import Mathlib.Analysis.SpecialFunctions.Pow.Real
import Mathlib.Analysis.SpecialFunctions.Sqrt

/-!
Formal checks of the numerical constants of "Quadratic forms with five large eigenvalues have
bounded densities" (Sections 6, 7 and Remark 8.2). Each theorem names the statement it checks.
-/

open Real

namespace QformFive

/-! ## Section 6: eta = 1/12, zeta = 1/256, a_0 = 5/48 -/

/-- (6.2): eta^2 + zeta = 25/2304 = a_0^2. -/
theorem small_entry_bound : (1/12 : ℝ)^2 + 1/256 = 25/2304 ∧ (25/2304 : ℝ) = (5/48)^2 := by
  constructor <;> norm_num

/-- Proposition 6.4: (1 - eta - sqrt 2 a_0 k)/2 = (44 - 5 sqrt 2 k)/96 for every k. -/
theorem gamma_identity (k : ℝ) :
    (1 - 1/12 - Real.sqrt 2 * (5/48) * k) / 2 = (44 - 5 * Real.sqrt 2 * k) / 96 := by
  ring

/-- sqrt 2 < 1.4143. -/
theorem sqrt_two_lt : Real.sqrt 2 < 1.4143 := by
  rw [Real.sqrt_lt' (by norm_num)]; norm_num

/-- Proposition 6.4: gamma_1 > 0.38, gamma_2 > 0.237, gamma_3 > 0.09, using sqrt 2 < 1.4143. -/
theorem gamma_bounds :
    (44 - 5 * Real.sqrt 2 * 1) / 96 > (0.38 : ℝ) ∧
    (44 - 5 * Real.sqrt 2 * 3) / 96 > (0.237 : ℝ) ∧
    (44 - 5 * Real.sqrt 2 * 5) / 96 > (0.09 : ℝ) := by
  have h := sqrt_two_lt
  refine ⟨?_, ?_, ?_⟩ <;> linarith

/-- Proposition 6.4: the three rational inequalities written in its proof. -/
theorem gamma_rational :
    (44 - 7.0715 : ℝ) / 96 > 0.38 ∧ (44 - 21.2145 : ℝ) / 96 > 0.237 ∧ (44 - 35.3575 : ℝ) / 96 > 0.09 ∧
    5 * (1.4143 : ℝ) = 7.0715 ∧ 15 * (1.4143 : ℝ) = 21.2145 ∧ 25 * (1.4143 : ℝ) = 35.3575 := by
  norm_num

/-! ## Corollary 4.4 constants (as in the nine-eigenvalue checks) -/

/-- Corollary 4.4(a): C_3 = 3 sqrt 2 e (9/2)^{1/6} < 15. -/
theorem C3_lt : 3 * Real.sqrt 2 * Real.exp 1 * (9/2 : ℝ) ^ ((1:ℝ)/6) < 15 := by
  set x := (9/2 : ℝ) ^ ((1:ℝ)/6) with hx
  have hx6 : x ^ 6 = 9/2 := by
    rw [hx, ← Real.rpow_natCast, ← Real.rpow_mul (by norm_num)]; norm_num
  have hs6 : Real.sqrt 2 ^ 6 = 8 := by
    have h2 : Real.sqrt 2 ^ 2 = 2 := Real.sq_sqrt (by norm_num)
    calc Real.sqrt 2 ^ 6 = (Real.sqrt 2 ^ 2)^3 := by ring
      _ = 8 := by rw [h2]; norm_num
  have hC6 : (3 * Real.sqrt 2 * Real.exp 1 * x)^6 = 26244 * Real.exp 1 ^ 6 := by
    rw [mul_pow, mul_pow, mul_pow, hs6, hx6]; ring
  have he6 : Real.exp 1 ^ 6 < 2.7182818286 ^ 6 := by
    gcongr; exact exp_one_lt_d9
  have hlt : (3 * Real.sqrt 2 * Real.exp 1 * x)^6 < 15^6 := by
    rw [hC6]; nlinarith [he6]
  have hpos : 0 ≤ 3 * Real.sqrt 2 * Real.exp 1 * x := by positivity
  exact lt_of_pow_lt_pow_left₀ 6 (by norm_num) hlt

/-- Corollary 4.4(b): C_2 = 8 e^{1/2} 2^{-1/8} < 12.2. -/
theorem C2_lt : 8 * Real.sqrt (Real.exp 1) * (2:ℝ) ^ (-(1:ℝ)/8) < 12.2 := by
  set y := (2:ℝ) ^ (-(1:ℝ)/8) with hy
  have hy8 : y ^ 8 = 1/2 := by
    rw [hy, ← Real.rpow_natCast, ← Real.rpow_mul (by norm_num)]; norm_num [Real.rpow_neg_one]
  have hse : Real.sqrt (Real.exp 1) ^ 8 = Real.exp 1 ^ 4 := by
    have h2 : Real.sqrt (Real.exp 1) ^ 2 = Real.exp 1 := Real.sq_sqrt (Real.exp_pos 1).le
    calc Real.sqrt (Real.exp 1) ^ 8 = (Real.sqrt (Real.exp 1) ^ 2)^4 := by ring
      _ = Real.exp 1 ^ 4 := by rw [h2]
  have hC8 : (8 * Real.sqrt (Real.exp 1) * y)^8 = 8388608 * Real.exp 1 ^ 4 := by
    rw [mul_pow, mul_pow, hse, hy8]; ring
  have he4 : Real.exp 1 ^ 4 < 2.7182818286 ^ 4 := by
    gcongr; exact exp_one_lt_d9
  have hlt : (8 * Real.sqrt (Real.exp 1) * y)^8 < (12.2:ℝ)^8 := by
    rw [hC8]; nlinarith [he4]
  have hpos : 0 ≤ 8 * Real.sqrt (Real.exp 1) * y := by positivity
  exact lt_of_pow_lt_pow_left₀ 8 (by norm_num) hlt

/-! ## Section 7 -/

/-- Proposition 7.1(a): C_3 / gamma_3 < 15 * 100/9 < 167. -/
theorem nopivot_density :
    3 * Real.sqrt 2 * Real.exp 1 * (9/2 : ℝ) ^ ((1:ℝ)/6) / ((44 - 5 * Real.sqrt 2 * 5) / 96) < 167 ∧
    1 / ((44 - 5 * Real.sqrt 2 * 5) / 96) < (100/9 : ℝ) ∧ (15 : ℝ) * (100/9) < 167 := by
  have hC := C3_lt
  have hg := (gamma_bounds).2.2
  have hg0 : (0:ℝ) < (44 - 5 * Real.sqrt 2 * 5) / 96 := by linarith
  have hinv : 1 / ((44 - 5 * Real.sqrt 2 * 5) / 96) < (100/9 : ℝ) := by
    rw [div_lt_iff₀ hg0]; linarith
  refine ⟨?_, hinv, by norm_num⟩
  have hC0 : 0 ≤ 3 * Real.sqrt 2 * Real.exp 1 * (9/2 : ℝ) ^ ((1:ℝ)/6) := by positivity
  rw [div_eq_mul_one_div]
  have h1 : 3 * Real.sqrt 2 * Real.exp 1 * (9/2 : ℝ) ^ ((1:ℝ)/6) * (1 / ((44 - 5 * Real.sqrt 2 * 5) / 96))
      ≤ 15 * (1 / ((44 - 5 * Real.sqrt 2 * 5) / 96)) := by
    apply mul_le_mul_of_nonneg_right hC.le; positivity
  have h2 : 15 * (1 / ((44 - 5 * Real.sqrt 2 * 5) / 96)) < 15 * (100/9) := by linarith
  have h3 : (15:ℝ) * (100/9) < 167 := by norm_num
  linarith

/-- Proposition 7.1(b): gamma_2^{-1/2} < 0.237^{-1/2} < 2.055 and C_2 gamma_2^{-1/2} < 12.2 * 2.055 < 26. -/
theorem nopivot_half :
    1 / Real.sqrt ((44 - 5 * Real.sqrt 2 * 3) / 96) < 2.055 ∧
    8 * Real.sqrt (Real.exp 1) * (2:ℝ) ^ (-(1:ℝ)/8) * (1 / Real.sqrt ((44 - 5 * Real.sqrt 2 * 3) / 96)) < 26 := by
  have hg := (gamma_bounds).2.1
  set g := (44 - 5 * Real.sqrt 2 * 3) / 96 with hgdef
  have hs : 1 / 2.055 < Real.sqrt g := by
    rw [Real.lt_sqrt (by norm_num)]; nlinarith
  have hs0 : 0 < Real.sqrt g := lt_trans (by norm_num) hs
  have hinv : 1 / Real.sqrt g < 2.055 := by
    rw [div_lt_iff₀ hs0]
    have := mul_lt_mul_of_pos_left hs (show (0:ℝ) < 2.055 by norm_num)
    norm_num at this ⊢; linarith
  refine ⟨hinv, ?_⟩
  have hC := C2_lt
  have hC0 : 0 ≤ 8 * Real.sqrt (Real.exp 1) * (2:ℝ) ^ (-(1:ℝ)/8) := by positivity
  have hi0 : 0 ≤ 1 / Real.sqrt g := by positivity
  have h1 := mul_le_mul hC.le hinv.le hi0 (by norm_num)
  have h2 : (12.2:ℝ) * 2.055 < 26 := by norm_num
  linarith

/-- Proposition 7.2: zeta^{-1/4} = 4, so 16 zeta^{-1/4} = 64; also zeta^{-1/2} = 16 and eta^{-1/2} = sqrt 12. -/
theorem pivot_scales :
    ((1:ℝ)/256) ^ (-(1:ℝ)/4) = 4 ∧ ((1:ℝ)/256) ^ (-(1:ℝ)/2) = 16 ∧
    ((1:ℝ)/12) ^ (-(1:ℝ)/2) = Real.sqrt 12 ∧ Real.sqrt 12 < 3.465 := by
  refine ⟨?_, ?_, ?_, ?_⟩
  · rw [show ((1:ℝ)/256) = (4:ℝ)^(-(4:ℝ)) by norm_num [Real.rpow_neg]]
    rw [← Real.rpow_mul (by norm_num)]; norm_num
  · rw [show ((1:ℝ)/256) = (16:ℝ)^(-(2:ℝ)) by norm_num [Real.rpow_neg]]
    rw [← Real.rpow_mul (by norm_num)]; norm_num
  · rw [show ((1:ℝ)/12) = (12:ℝ)^(-(1:ℝ)) by norm_num [Real.rpow_neg_one],
      ← Real.rpow_mul (by norm_num), Real.sqrt_eq_rpow]
    norm_num
  · rw [Real.sqrt_lt' (by norm_num)]; norm_num

/-- log 19 < 3 (so L_0 = 2 + 2 log 19 < 8). -/
theorem log19_lt : Real.log 19 < 3 := by
  rw [Real.log_lt_iff_lt_exp (by norm_num)]
  have he : (2.7182818283:ℝ)^3 < Real.exp 1 ^ 3 := by gcongr; exact exp_one_gt_d9
  have : Real.exp 3 = Real.exp 1 ^ 3 := by rw [← Real.exp_nat_mul]; norm_num
  rw [this]; nlinarith [he]

/-- Proposition 7.2: pi + 4 log 2 + 2 L_0 < 21.92, sqrt 12 times it is < 76, and adding the tail 1 gives < 77. -/
theorem halfpotential_constants :
    π + 4 * Real.log 2 + 2 * (2 + 2 * Real.log 19) < 21.92 ∧
    Real.sqrt 12 * (π + 4 * Real.log 2 + 2 * (2 + 2 * Real.log 19)) < 76 ∧
    Real.sqrt 12 * (π + 4 * Real.log 2 + 2 * (2 + 2 * Real.log 19)) + 1 < 77 ∧
    (26:ℝ) ≤ 77 ∧ (64:ℝ) ≤ 77 := by
  have hpi := pi_lt_d4
  have hl := log_two_lt_d9
  have h19 := log19_lt
  have hsum : π + 4 * Real.log 2 + 2 * (2 + 2 * Real.log 19) < 21.92 := by
    norm_num at hl; linarith
  have hsum0 : 0 ≤ π + 4 * Real.log 2 + 2 * (2 + 2 * Real.log 19) := by
    have := Real.pi_pos
    have h2 := Real.log_nonneg (show (1:ℝ) ≤ 2 by norm_num)
    have h19' := Real.log_nonneg (show (1:ℝ) ≤ 19 by norm_num)
    linarith
  have h12 := (pivot_scales).2.2.2
  have hs0 : 0 ≤ Real.sqrt 12 := Real.sqrt_nonneg _
  have hprod : Real.sqrt 12 * (π + 4 * Real.log 2 + 2 * (2 + 2 * Real.log 19)) < 76 := by
    nlinarith [mul_le_mul h12.le hsum.le hsum0 (by norm_num : (0:ℝ) ≤ 3.465)]
  exact ⟨hsum, hprod, by linarith, by norm_num, by norm_num⟩

/-- Theorem 1.1: diagonal pivot sqrt 12 * 77 < 267, definite pair 16 pi < 51, indefinite pair
16(8 + 4 log 2 + 2 log 19) + 1/e < 269, the no-pivot bound 167, and 269 <= 270. -/
theorem main_constants :
    Real.sqrt 12 * 77 < 267 ∧ 16 * π < 51 ∧
    16 * (8 + 4 * Real.log 2 + 2 * Real.log 19) + 1 / Real.exp 1 < 269 ∧
    (167:ℝ) < 269 ∧ (267:ℝ) < 269 ∧ (51:ℝ) < 269 ∧ (269:ℝ) ≤ 270 := by
  have h12 := (pivot_scales).2.2.2
  refine ⟨by linarith, by have := pi_lt_d4; linarith, ?_, by norm_num, by norm_num, by norm_num, by norm_num⟩
  have hl := log_two_lt_d9
  have h19 := log19_lt
  have he := exp_one_gt_d9
  have hinv : 1 / Real.exp 1 < 1 / 2.7 := by
    apply one_div_lt_one_div_of_lt (by norm_num); linarith
  norm_num at hl hinv ⊢
  linarith

/-- The indefinite pair: 6 + log 16 + L_0 = 8 + 4 log 2 + 2 log 19. -/
theorem indefinite_rewrite : 6 + Real.log 16 + (2 + 2 * Real.log 19) = 8 + 4 * Real.log 2 + 2 * Real.log 19 := by
  have h16 : Real.log 16 = 4 * Real.log 2 := by
    rw [show (16:ℝ) = 2^4 by norm_num, Real.log_pow]; norm_num
  rw [h16]; ring

/-! ## Remark 8.2 -/

/-- Every principal 2x2 minor has modulus at most 1/N, and 1/N < zeta when N > 256. -/
theorem two_star_no_pivot (N : ℕ) (hN : 256 < N) : (1:ℝ) / N < 1/256 := by
  have : (256:ℝ) < N := by exact_mod_cast hN
  exact one_div_lt_one_div_of_lt (by norm_num) this

/-- The integral of |u|^{-1/2} over [-1/2, 1/2] equals 2 * (2 sqrt(1/2)) = 2 sqrt 2. -/
theorem bathtub_value : 2 * (2 * Real.sqrt (1/2)) = 2 * Real.sqrt 2 := by
  have h : Real.sqrt (1/2 : ℝ) = Real.sqrt 2 / 2 := by
    rw [show (1/2 : ℝ) = 2 / 2^2 by norm_num, Real.sqrt_div' _ (by norm_num), Real.sqrt_sq (by norm_num)]
  rw [h]; ring

/-- sqrt(pi) e^{1/4} 2 sqrt 2 = 2 sqrt(2 pi) e^{1/4}, its square is 8 pi sqrt e, and (2 pi)^{-1} 8 pi sqrt e = 4 sqrt e. -/
theorem two_star_constants :
    Real.sqrt π * Real.exp (1/4) * (2 * Real.sqrt 2) = 2 * Real.sqrt (2 * π) * Real.exp (1/4) ∧
    (2 * Real.sqrt (2 * π) * Real.exp (1/4))^2 = 8 * π * Real.sqrt (Real.exp 1) ∧
    (8 * π * Real.sqrt (Real.exp 1)) / (2 * π) = 4 * Real.sqrt (Real.exp 1) := by
  have hpi : 0 < π := Real.pi_pos
  refine ⟨?_, ?_, ?_⟩
  · rw [Real.sqrt_mul (by norm_num)]; ring
  · have h1 : Real.sqrt (2 * π) ^ 2 = 2 * π := Real.sq_sqrt (by positivity)
    have h2 : Real.exp (1/4) ^ 2 = Real.sqrt (Real.exp 1) := by
      rw [← Real.exp_nat_mul, Real.sqrt_eq_rpow, Real.exp_one_rpow]; norm_num
    calc (2 * Real.sqrt (2 * π) * Real.exp (1/4))^2
        = 4 * Real.sqrt (2 * π) ^ 2 * Real.exp (1/4) ^ 2 := by ring
      _ = 8 * π * Real.sqrt (Real.exp 1) := by rw [h1, h2]; ring
  · field_simp; ring

end QformFive

#print axioms QformFive.small_entry_bound
#print axioms QformFive.gamma_identity
#print axioms QformFive.sqrt_two_lt
#print axioms QformFive.gamma_bounds
#print axioms QformFive.gamma_rational
#print axioms QformFive.C3_lt
#print axioms QformFive.C2_lt
#print axioms QformFive.nopivot_density
#print axioms QformFive.nopivot_half
#print axioms QformFive.pivot_scales
#print axioms QformFive.log19_lt
#print axioms QformFive.halfpotential_constants
#print axioms QformFive.main_constants
#print axioms QformFive.indefinite_rewrite
#print axioms QformFive.two_star_no_pivot
#print axioms QformFive.bathtub_value
#print axioms QformFive.two_star_constants
