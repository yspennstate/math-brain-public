import Mathlib.Analysis.SpecialFunctions.Pow.Real
import Mathlib.Analysis.SpecialFunctions.Sqrt
import Mathlib.Analysis.Complex.ExponentialBounds
import Mathlib.Tactic

/-!
Corollary 4.4 of "Quadratic forms with five large singular values have bounded densities" (repaired text,
sha256 90f859b7): the constants.

With `β_ℓ = ((√2 π e)^ℓ ω(ℓ)^{1/2})^{1/2}`, `ω(3) = 9/2`, `ω(2) = 2`:
* `cor44_a_identity`: `3 β_3^{2/3}/π = C_3 = 3√2 e (9/2)^{1/6}` (Lemma 2.2 with `p = 3/2` gives `3a/π`), checked through
  sixth powers: both sides have sixth power `26244 e^6`.
* `cor44_b_beta2`, `cor44_b_identity`: `β_2 = 2^{3/4} π e` and `8 (β_2/(2π))^{1/2} = C_2 = 8 e^{1/2} 2^{-1/8}`, checked
  through eighth powers: `8388608 e^4`.
* `C3_lt_15`, `C2_lt`: repair 19's comparisons `26244 (11/4)^6 < 15^6` and `8388608 (11/4)^4 < (61/5)^8`, with `e < 11/4`.
-/

open Real

namespace QformFiveB

/-- `C_3 = 3√2 e (9/2)^{1/6}`. -/
noncomputable def C3 : ℝ := 3 * √2 * exp 1 * (9 / 2 : ℝ) ^ (1 / 6 : ℝ)

/-- `C_2 = 8 e^{1/2} 2^{-1/8}`. -/
noncomputable def C2 : ℝ := 8 * exp (1 / 2) * (2 : ℝ) ^ (-(1 / 8 : ℝ))

/-- `β_3 = ((√2 π e)^3 ω(3)^{1/2})^{1/2}` with `ω(3) = 27/3! = 9/2`. -/
noncomputable def beta3 : ℝ := √((√2 * π * exp 1) ^ 3 * √(9 / 2))

/-- `β_2 = ((√2 π e)^2 ω(2)^{1/2})^{1/2}` with `ω(2) = 4/2! = 2`. -/
noncomputable def beta2 : ℝ := √((√2 * π * exp 1) ^ 2 * √2)

theorem omega_three_two : (3 : ℝ) ^ 3 / (Nat.factorial 3 : ℝ) = 9 / 2 ∧ (2 : ℝ) ^ 2 / (Nat.factorial 2 : ℝ) = 2 := by
  constructor <;> norm_num [Nat.factorial]

theorem sqrt2_pow_six : √2 ^ 6 = 8 := by
  have h : √2 ^ 2 = 2 := Real.sq_sqrt (by norm_num)
  calc √2 ^ 6 = (√2 ^ 2) ^ 3 := by ring
    _ = 8 := by rw [h]; norm_num

theorem C3_pow_six : C3 ^ 6 = 26244 * exp 1 ^ 6 := by
  unfold C3
  have h1 : ((9 / 2 : ℝ) ^ (1 / 6 : ℝ)) ^ 6 = 9 / 2 := by
    rw [← Real.rpow_natCast, ← Real.rpow_mul (by norm_num)]; norm_num
  calc (3 * √2 * exp 1 * (9 / 2 : ℝ) ^ (1 / 6 : ℝ)) ^ 6
      = 3 ^ 6 * √2 ^ 6 * exp 1 ^ 6 * ((9 / 2 : ℝ) ^ (1 / 6 : ℝ)) ^ 6 := by ring
    _ = 26244 * exp 1 ^ 6 := by rw [sqrt2_pow_six, h1]; ring

theorem C2_pow_eight : C2 ^ 8 = 8388608 * exp 1 ^ 4 := by
  unfold C2
  have h1 : ((2 : ℝ) ^ (-(1 / 8 : ℝ))) ^ 8 = 1 / 2 := by
    rw [← Real.rpow_natCast, ← Real.rpow_mul (by norm_num)]
    rw [show (-(1 / 8 : ℝ)) * ((8 : ℕ) : ℝ) = -1 by norm_num, Real.rpow_neg_one]; norm_num
  have h2 : exp (1 / 2) ^ 8 = exp 1 ^ 4 := by
    rw [← Real.exp_nat_mul, ← Real.exp_nat_mul]; norm_num
  calc (8 * exp (1 / 2) * (2 : ℝ) ^ (-(1 / 8 : ℝ))) ^ 8
      = 8 ^ 8 * exp (1 / 2) ^ 8 * ((2 : ℝ) ^ (-(1 / 8 : ℝ))) ^ 8 := by ring
    _ = 8388608 * exp 1 ^ 4 := by rw [h1, h2]; ring

theorem C3_pos : 0 < C3 := by unfold C3; positivity

theorem C2_pos : 0 < C2 := by unfold C2; positivity

/-- `e < 11/4`. -/
theorem exp_one_lt_eleven_quarters : exp 1 < 11 / 4 := by
  have := exp_one_lt_d9; norm_num at this ⊢; linarith

/-- **Corollary 4.4(a), the constant.** `C_3 < 15`, from `26244 (11/4)^6 < 15^6`. -/
theorem C3_lt_15 : C3 < 15 := by
  apply lt_of_pow_lt_pow_left₀ 6 (by norm_num : (0 : ℝ) ≤ 15)
  rw [C3_pow_six]
  have he := exp_one_lt_eleven_quarters
  have hep : 0 < exp 1 := exp_pos 1
  have h6 : exp 1 ^ 6 < (11 / 4) ^ 6 := by gcongr
  calc 26244 * exp 1 ^ 6 < 26244 * (11 / 4) ^ 6 := by linarith
    _ < 15 ^ 6 := by norm_num

/-- **Corollary 4.4(b), the constant.** `C_2 < 12.2`, from `8388608 (11/4)^4 < (61/5)^8`. -/
theorem C2_lt : C2 < 61 / 5 := by
  apply lt_of_pow_lt_pow_left₀ 8 (by norm_num : (0 : ℝ) ≤ 61 / 5)
  rw [C2_pow_eight]
  have he := exp_one_lt_eleven_quarters
  have hep : 0 < exp 1 := exp_pos 1
  have h4 : exp 1 ^ 4 < (11 / 4) ^ 4 := by gcongr
  calc 8388608 * exp 1 ^ 4 < 8388608 * (11 / 4) ^ 4 := by linarith
    _ < (61 / 5) ^ 8 := by norm_num

/-- **Corollary 4.4(a), the identity.** `3 β_3^{2/3}/π = C_3`: both are positive and have sixth power `26244 e^6`. -/
theorem cor44_a_identity : 3 * beta3 ^ (2 / 3 : ℝ) / π = C3 := by
  have hpi : 0 < π := pi_pos
  have hb0 : 0 ≤ beta3 := Real.sqrt_nonneg _
  have hX : 0 ≤ (√2 * π * exp 1) ^ 3 * √(9 / 2) := by positivity
  have hb2 : beta3 ^ 2 = (√2 * π * exp 1) ^ 3 * √(9 / 2) := Real.sq_sqrt hX
  have hs : √(9 / 2 : ℝ) ^ 2 = 9 / 2 := Real.sq_sqrt (by norm_num)
  have hpow : (beta3 ^ (2 / 3 : ℝ)) ^ 6 = (beta3 ^ 2) ^ 2 := by
    rw [← Real.rpow_natCast, ← Real.rpow_mul hb0]
    rw [show (2 / 3 : ℝ) * ((6 : ℕ) : ℝ) = ((4 : ℕ) : ℝ) by norm_num, Real.rpow_natCast]
    ring
  have hL : (3 * beta3 ^ (2 / 3 : ℝ) / π) ^ 6 = 26244 * exp 1 ^ 6 := by
    have e : (3 * beta3 ^ (2 / 3 : ℝ) / π) ^ 6 = 3 ^ 6 * (beta3 ^ (2 / 3 : ℝ)) ^ 6 / π ^ 6 := by ring
    rw [e, hpow, hb2]
    have e2 : ((√2 * π * exp 1) ^ 3 * √(9 / 2)) ^ 2 = √2 ^ 6 * π ^ 6 * exp 1 ^ 6 * √(9 / 2 : ℝ) ^ 2 := by ring
    rw [e2, sqrt2_pow_six, hs]
    field_simp
    ring
  have hLpos : 0 ≤ 3 * beta3 ^ (2 / 3 : ℝ) / π := by positivity
  have := C3_pos
  rw [← C3_pow_six] at hL
  exact (pow_left_inj₀ hLpos this.le (by norm_num : (6 : ℕ) ≠ 0)).mp hL

/-- **Corollary 4.4(b)**, `β_2 = 2^{3/4} π e`: both sides are positive with fourth power `8 π^4 e^4`. -/
theorem cor44_b_beta2 : beta2 = (2 : ℝ) ^ (3 / 4 : ℝ) * π * exp 1 := by
  have hpi : 0 < π := pi_pos
  have hX : 0 ≤ (√2 * π * exp 1) ^ 2 * √2 := by positivity
  have hb2 : beta2 ^ 2 = (√2 * π * exp 1) ^ 2 * √2 := Real.sq_sqrt hX
  have hs2 : √2 ^ 2 = 2 := Real.sq_sqrt (by norm_num)
  have h34 : ((2 : ℝ) ^ (3 / 4 : ℝ)) ^ 4 = 8 := by
    rw [← Real.rpow_natCast, ← Real.rpow_mul (by norm_num)]; norm_num
  have hL : beta2 ^ 4 = 8 * π ^ 4 * exp 1 ^ 4 := by
    have e : beta2 ^ 4 = (beta2 ^ 2) ^ 2 := by ring
    rw [e, hb2]
    have e2 : ((√2 * π * exp 1) ^ 2 * √2) ^ 2 = (√2 ^ 2) ^ 3 * π ^ 4 * exp 1 ^ 4 := by ring
    rw [e2, hs2]; norm_num
  have hR : ((2 : ℝ) ^ (3 / 4 : ℝ) * π * exp 1) ^ 4 = 8 * π ^ 4 * exp 1 ^ 4 := by
    have e : ((2 : ℝ) ^ (3 / 4 : ℝ) * π * exp 1) ^ 4 = ((2 : ℝ) ^ (3 / 4 : ℝ)) ^ 4 * π ^ 4 * exp 1 ^ 4 := by ring
    rw [e, h34]
  rw [← hR] at hL
  exact (pow_left_inj₀ (Real.sqrt_nonneg _) (by positivity) (by norm_num : (4 : ℕ) ≠ 0)).mp hL

/-- **Corollary 4.4(b), the identity.** `8 (β_2/(2π))^{1/2} = C_2`: both are positive with square `64 e 2^{-1/4}`. -/
theorem cor44_b_identity : 8 * √(beta2 / (2 * π)) = C2 := by
  have hpi : 0 < π := pi_pos
  have hq : beta2 / (2 * π) = (2 : ℝ) ^ (-(1 / 4 : ℝ)) * exp 1 := by
    rw [cor44_b_beta2]
    have e : (2 : ℝ) ^ (3 / 4 : ℝ) = 2 * (2 : ℝ) ^ (-(1 / 4 : ℝ)) := by
      rw [show (3 / 4 : ℝ) = 1 + (-(1 / 4)) by norm_num, Real.rpow_add (by norm_num), Real.rpow_one]
    rw [e]; field_simp
  rw [hq]
  unfold C2
  have h1 : √((2 : ℝ) ^ (-(1 / 4 : ℝ)) * exp 1) = (2 : ℝ) ^ (-(1 / 8 : ℝ)) * exp (1 / 2) := by
    rw [Real.sqrt_mul (by positivity), Real.sqrt_eq_rpow, Real.sqrt_eq_rpow, ← Real.rpow_mul (by norm_num),
      ← Real.exp_one_rpow, ← Real.rpow_mul (exp_pos 1).le, Real.exp_one_rpow]
    norm_num
  rw [h1]; ring

end QformFiveB
