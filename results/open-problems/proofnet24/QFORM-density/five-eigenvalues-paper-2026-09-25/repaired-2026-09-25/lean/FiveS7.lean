import Mathlib.Analysis.SpecialFunctions.Pow.Real
import Mathlib.Analysis.SpecialFunctions.Sqrt
import Mathlib.Analysis.SpecialFunctions.Log.Basic
import Mathlib.Analysis.Real.Pi.Bounds
import Mathlib.Analysis.Complex.ExponentialBounds
import Mathlib.Tactic

/-!
Section 7 of "Quadratic forms with five large singular values have bounded densities" (repaired text,
sha256 90f859b7): the constants of Propositions 7.1 and 7.2 and of the proof of Theorem 1.1, the scaling to
general `K` and `s`, and Remark 7.3.

* `gamma_bounds`: `γ₁ > 0.38`, `γ₂ > 0.237`, `γ₃ > 0.09` for `γ_m = (44 - 5√2(2m-1))/96`.
* `nopivot_density`, `nopivot_half`: Proposition 7.1 (a) `< 167` and (b) `< 26`.
* `halfpotential_pair`, `halfpotential_diag`, `halfpotential_total`, `halfpotential_L0`: Proposition 7.2.
* `main_diag`, `main_definite`, `logplus_div_sqrt_le`, `main_indefinite`, `main_indefinite_num`, `main_cases`:
  the four cases of the proof of Theorem 1.1, each below `269`.
* `main_scaling`, `main_density_scaling`, `remark73_scaling`: the reduction to `K = s = 1` and Remark 7.3.
-/

open Real

namespace QformFiveB

/-- `γ_m = (44 - 5√2 (2m - 1))/96` (Proposition 6.4). -/
noncomputable def gammaM (m : ℕ) : ℝ := (44 - 5 * √2 * (2 * (m : ℝ) - 1)) / 96

theorem sqrt2_lt : √2 < 1.4143 := by
  rw [show (1.4143 : ℝ) = √(1.4143 ^ 2) from (Real.sqrt_sq (by norm_num)).symm]
  exact Real.sqrt_lt_sqrt (by norm_num) (by norm_num)

/-- `γ₁ > 0.38`, `γ₂ > 0.237`, `γ₃ > 0.09`, from `√2 < 1.4143`. -/
theorem gamma_bounds : 0.38 < gammaM 1 ∧ 0.237 < gammaM 2 ∧ 0.09 < gammaM 3 := by
  have h := sqrt2_lt
  have e1 : gammaM 1 = (44 - 5 * √2) / 96 := by unfold gammaM; push_cast; ring
  have e2 : gammaM 2 = (44 - 15 * √2) / 96 := by unfold gammaM; push_cast; ring
  have e3 : gammaM 3 = (44 - 25 * √2) / 96 := by unfold gammaM; push_cast; ring
  rw [e1, e2, e3]
  refine ⟨by linarith, by linarith, by linarith⟩

/-- **Proposition 7.1(a).** `E₃ > γ₃⁶` with `γ₃ > 0.09` and `C₃ < 15` give `C₃ E₃^{-1/6} < 15 · 100/9 < 167`. -/
theorem nopivot_density (E γ C : ℝ) (hC : C < 15) (hC0 : 0 ≤ C) (hγ : 0.09 < γ) (hE : γ ^ 6 < E) :
    C * E ^ (-(1 / 6 : ℝ)) < 167 := by
  have hγ0 : 0 < γ := by linarith
  have hE0 : 0 < E := lt_trans (by positivity) hE
  have h1 : γ < E ^ (1 / 6 : ℝ) := by
    have h := Real.rpow_lt_rpow (by positivity) hE (show (0 : ℝ) < 1 / 6 by norm_num)
    have e : (γ ^ 6) ^ (1 / 6 : ℝ) = γ := by
      rw [show (1 / 6 : ℝ) = ((6 : ℕ) : ℝ)⁻¹ by norm_num]
      exact Real.pow_rpow_inv_natCast hγ0.le (by norm_num)
    rwa [e] at h
  have hpos : 0 < E ^ (1 / 6 : ℝ) := Real.rpow_pos_of_pos hE0 _
  have h2 : E ^ (-(1 / 6 : ℝ)) < 100 / 9 := by
    rw [Real.rpow_neg hE0.le, inv_lt_comm₀ hpos (by norm_num)]
    have : (100 / 9 : ℝ)⁻¹ = 0.09 := by norm_num
    rw [this]; linarith
  have h3 : 0 ≤ E ^ (-(1 / 6 : ℝ)) := (Real.rpow_pos_of_pos hE0 _).le
  calc C * E ^ (-(1 / 6 : ℝ)) ≤ 15 * E ^ (-(1 / 6 : ℝ)) := mul_le_mul_of_nonneg_right hC.le h3
    _ < 15 * (100 / 9) := mul_lt_mul_of_pos_left h2 (by norm_num)
    _ < 167 := by norm_num

/-- **Proposition 7.1(b).** `E₂ > γ₂⁴` with `γ₂ > 0.237` and `C₂ < 12.2` give `C₂ E₂^{-1/8} < 12.2 · 2.055 < 26`. -/
theorem nopivot_half (E γ C : ℝ) (hC : C < 12.2) (hC0 : 0 ≤ C) (hγ : 0.237 < γ) (hE : γ ^ 4 < E) :
    C * E ^ (-(1 / 8 : ℝ)) < 26 := by
  have hγ0 : 0 < γ := by linarith
  have hE0 : 0 < E := lt_trans (by positivity) hE
  have h1 : √γ < E ^ (1 / 8 : ℝ) := by
    have h := Real.rpow_lt_rpow (by positivity) hE (show (0 : ℝ) < 1 / 8 by norm_num)
    have e : (γ ^ 4) ^ (1 / 8 : ℝ) = √γ := by
      rw [Real.sqrt_eq_rpow, ← Real.rpow_natCast, ← Real.rpow_mul hγ0.le]; norm_num
    rwa [e] at h
  have hsγ : √(0.237 : ℝ) < √γ := Real.sqrt_lt_sqrt (by norm_num) hγ
  have hlow : 1 / 2.055 < √(0.237 : ℝ) := by
    rw [Real.lt_sqrt (by norm_num)]; norm_num
  have hpos : 0 < E ^ (1 / 8 : ℝ) := Real.rpow_pos_of_pos hE0 _
  have h2 : E ^ (-(1 / 8 : ℝ)) < 2.055 := by
    rw [Real.rpow_neg hE0.le, inv_lt_comm₀ hpos (by norm_num)]
    have : (2.055 : ℝ)⁻¹ = 1 / 2.055 := by norm_num
    rw [this]; linarith
  have h3 : 0 ≤ E ^ (-(1 / 8 : ℝ)) := (Real.rpow_pos_of_pos hE0 _).le
  calc C * E ^ (-(1 / 8 : ℝ)) ≤ 12.2 * E ^ (-(1 / 8 : ℝ)) := mul_le_mul_of_nonneg_right hC.le h3
    _ < 12.2 * 2.055 := mul_lt_mul_of_pos_left h2 (by norm_num)
    _ < 26 := by norm_num

/-- `log 19 < 3`. -/
theorem log19_lt_three' : log 19 < 3 := by
  rw [log_lt_iff_lt_exp (by norm_num)]
  have h := exp_one_gt_d9
  have h3 : (2.7182818283 : ℝ) ^ 3 < exp 1 ^ 3 := by gcongr
  have e : exp 1 ^ 3 = exp 3 := by rw [← Real.exp_nat_mul]; norm_num
  calc (19 : ℝ) < 2.7182818283 ^ 3 := by norm_num
    _ < exp 1 ^ 3 := h3
    _ = exp 3 := e

/-- **Proposition 7.2, the pair case.** `16 ζ^{-1/4} = 64` at `ζ = 1/256`. -/
theorem halfpotential_pair : 16 * (1 / 256 : ℝ) ^ (-(1 / 4 : ℝ)) = 64 := by
  have e : (1 / 256 : ℝ) = (1 / 4) ^ (4 : ℕ) := by norm_num
  rw [e, ← Real.rpow_natCast, ← Real.rpow_mul (by norm_num),
    show ((4 : ℕ) : ℝ) * (-(1 / 4)) = -1 by norm_num, Real.rpow_neg_one]
  norm_num

/-- **Proposition 7.2, the diagonal case.** `π + 4 log 2 + 2 L₀ = π + 4 + 4 log 2 + 4 log 19` with
`L₀ = 2 + 2 log 19`, and `η^{-1/2} = √12` at `η = 1/12`. -/
theorem halfpotential_L0 :
    π + 4 * log 2 + 2 * (2 + 2 * log 19) = π + 4 + 4 * log 2 + 4 * log 19 ∧
      (1 / 12 : ℝ) ^ (-(1 / 2 : ℝ)) = √12 := by
  refine ⟨by ring, ?_⟩
  rw [Real.rpow_neg (by norm_num), ← Real.inv_rpow (by norm_num), Real.sqrt_eq_rpow]
  norm_num

/-- `√12 (π + 4 + 4 log 2 + 4 log 19) < 76`, through `π < 3.1416`, `log 2 < 0.6932`, `log 19 < 3`
(the bracket is below `21.92`) and `√12 < 3.465`. -/
theorem halfpotential_diag : √12 * (π + 4 + 4 * log 2 + 4 * log 19) < 76 := by
  have hpi := pi_lt_d4
  have hl2 := log_two_lt_d9
  have hl19 := log19_lt_three'
  have hbr : π + 4 + 4 * log 2 + 4 * log 19 < 21.92 := by norm_num at hpi hl2 ⊢; linarith
  have hbr0 : 0 < π + 4 + 4 * log 2 + 4 * log 19 := by
    have := pi_pos; have := log_pos (show (1 : ℝ) < 2 by norm_num)
    have := log_pos (show (1 : ℝ) < 19 by norm_num); linarith
  have hs : √12 < 3.465 := by
    rw [show (3.465 : ℝ) = √(3.465 ^ 2) from (Real.sqrt_sq (by norm_num)).symm]
    exact Real.sqrt_lt_sqrt (by norm_num) (by norm_num)
  calc √12 * (π + 4 + 4 * log 2 + 4 * log 19) < 3.465 * 21.92 :=
        mul_lt_mul'' hs hbr (Real.sqrt_nonneg _) hbr0.le
    _ < 76 := by norm_num

/-- **Proposition 7.2.** The part `{|Q - a| ≤ 1}` contributes less than `76` and the rest at most `1`. -/
theorem halfpotential_total : √12 * (π + 4 + 4 * log 2 + 4 * log 19) + 1 < 77 := by
  linarith [halfpotential_diag]

/-- **Theorem 1.1, diagonal pivot.** `√12 · 77 < 267`. -/
theorem main_diag : √12 * 77 < 267 := by
  have h : √12 < 3.4642 := by
    rw [show (3.4642 : ℝ) = √(3.4642 ^ 2) from (Real.sqrt_sq (by norm_num)).symm]
    exact Real.sqrt_lt_sqrt (by norm_num) (by norm_num)
  linarith

/-- **Theorem 1.1, definite pair.** `π ζ^{-1/2} = 16π < 51`. -/
theorem main_definite : π * (1 / 256 : ℝ) ^ (-(1 / 2 : ℝ)) = 16 * π ∧ 16 * π < 51 := by
  constructor
  · have e : (1 / 256 : ℝ) = (1 / 16) ^ (2 : ℕ) := by norm_num
    rw [e, ← Real.rpow_natCast, ← Real.rpow_mul (by norm_num),
      show ((2 : ℕ) : ℝ) * (-(1 / 2)) = -1 by norm_num, Real.rpow_neg_one]
    norm_num; ring
  · have := pi_lt_d2; norm_num at this; linarith

/-- `sup_{D>0} D^{-1/2} log⁺ D = 2/e`, the inequality direction: `log⁺ D / √D ≤ 2/e`. -/
theorem logplus_div_sqrt_le (D : ℝ) (hD : 0 < D) : max 0 (log D) / √D ≤ 2 / exp 1 := by
  have hs : 0 < √D := Real.sqrt_pos.mpr hD
  rcases le_or_gt (log D) 0 with h | h
  · rw [max_eq_left h, zero_div]; positivity
  · rw [max_eq_right h.le, div_le_div_iff₀ hs (exp_pos 1)]
    have hx : log D = 2 * log (√D) := by
      rw [Real.log_sqrt hD.le]; ring
    have key : log (√D) ≤ √D / exp 1 := by
      have := Real.log_le_sub_one_of_pos (show 0 < √D / exp 1 by positivity)
      rw [Real.log_div hs.ne' (exp_pos 1).ne', Real.log_exp] at this
      linarith
    rw [hx]
    have h2 := mul_le_mul_of_nonneg_right key (exp_pos 1).le
    rw [div_mul_cancel₀ _ (exp_pos 1).ne'] at h2
    linarith

/-- **Theorem 1.1, indefinite pair.** For `D ≥ ζ = 1/256`,
`D^{-1/2}(6 + log⁺(16√D) + L₀) ≤ 16(8 + 4 log 2 + 2 log 19) + 1/e`. -/
theorem main_indefinite (D : ℝ) (hD : 1 / 256 ≤ D) :
    (6 + max 0 (log (16 * √D)) + (2 + 2 * log 19)) / √D
      ≤ 16 * (8 + 4 * log 2 + 2 * log 19) + 1 / exp 1 := by
  have hD0 : 0 < D := by linarith
  have hs : 0 < √D := Real.sqrt_pos.mpr hD0
  have hs16 : 1 / 16 ≤ √D := by
    have e : (1 / 16 : ℝ) = √(1 / 256) := by
      rw [show (1 / 256 : ℝ) = (1 / 16) ^ 2 by norm_num, Real.sqrt_sq (by norm_num)]
    rw [e]; exact Real.sqrt_le_sqrt hD
  have hl16 : log 16 = 4 * log 2 := by
    rw [show (16 : ℝ) = 2 ^ 4 by norm_num, log_pow]; norm_num
  have hl2 : 0 < log 2 := log_pos (by norm_num)
  have hl19 : 0 < log 19 := log_pos (by norm_num)
  have hsplit : max 0 (log (16 * √D)) ≤ log 16 + 1 / 2 * max 0 (log D) := by
    have e : log (16 * √D) = log 16 + 1 / 2 * log D := by
      rw [Real.log_mul (by norm_num) hs.ne', Real.log_sqrt hD0.le]; ring
    rw [e]
    have h16 : 0 ≤ log 16 := by rw [hl16]; positivity
    have m1 := le_max_left (0 : ℝ) (log D)
    have m2 := le_max_right (0 : ℝ) (log D)
    apply max_le <;> linarith
  have hk := logplus_div_sqrt_le D hD0
  have hA0 : 0 ≤ 8 + 4 * log 2 + 2 * log 19 := by positivity
  have hnum : 6 + max 0 (log (16 * √D)) + (2 + 2 * log 19)
      ≤ (8 + 4 * log 2 + 2 * log 19) + 1 / 2 * max 0 (log D) := by linarith
  have h1 : (8 + 4 * log 2 + 2 * log 19) / √D ≤ 16 * (8 + 4 * log 2 + 2 * log 19) := by
    rw [div_le_iff₀ hs]
    have := mul_le_mul_of_nonneg_left hs16 hA0
    nlinarith
  have h2 : 1 / 2 * (max 0 (log D) / √D) ≤ 1 / 2 * (2 / exp 1) :=
    mul_le_mul_of_nonneg_left hk (by norm_num)
  calc (6 + max 0 (log (16 * √D)) + (2 + 2 * log 19)) / √D
      ≤ ((8 + 4 * log 2 + 2 * log 19) + 1 / 2 * max 0 (log D)) / √D := by gcongr
    _ = (8 + 4 * log 2 + 2 * log 19) / √D + 1 / 2 * (max 0 (log D) / √D) := by ring
    _ ≤ 16 * (8 + 4 * log 2 + 2 * log 19) + 1 / 2 * (2 / exp 1) := by linarith
    _ = 16 * (8 + 4 * log 2 + 2 * log 19) + 1 / exp 1 := by ring

/-- `16(8 + 4 log 2 + 2 log 19) + 1/e < 269`, through `log 2 < 0.6932`, `log 19 < 3` and `e > 2.7`. -/
theorem main_indefinite_num : 16 * (8 + 4 * log 2 + 2 * log 19) + 1 / exp 1 < 269 := by
  have hl2 := log_two_lt_d9
  have hl19 := log19_lt_three'
  have he : 2.7 < exp 1 := by have := exp_one_gt_d9; norm_num at this ⊢; linarith
  have hinv : 1 / exp 1 < 1 / 2.7 := one_div_lt_one_div_of_lt (by norm_num) he
  norm_num at hl2 hinv ⊢
  linarith

/-- **The four cases of Theorem 1.1** (with `K = s = 1`): no pivot `< 167`, diagonal `< 267`, definite pair
`< 51`, indefinite pair `< 269`; all are below `269 < 270`. -/
theorem main_cases : (167 : ℝ) < 269 ∧ √12 * 77 < 269 ∧ 16 * π < 269 ∧
    16 * (8 + 4 * log 2 + 2 * log 19) + 1 / exp 1 < 269 ∧ (269 : ℝ) < 270 := by
  refine ⟨by norm_num, by linarith [main_diag], by linarith [main_definite.2], main_indefinite_num, by norm_num⟩

/-- **The scaling step of Theorem 1.1.** With `Y = K X`, `Q̃ = Yᵀ(A/s)Y + (K/s) bᵀY + (K²/s) c` equals
`(K²/s) Q`, written with `q₂ = XᵀAX` (so `Yᵀ(A/s)Y = K² q₂/s`) and `q₁ = bᵀX`. -/
theorem main_scaling (K s q2 q1 c : ℝ) (hK : 0 < K) (hs : 0 < s) :
    s / K ^ 2 * (K ^ 2 * q2 / s + K / s * (K * q1) + K ^ 2 / s * c) = q2 + q1 + c := by
  field_simp

/-- `p_Q(z) = (K²/s) p_{Q̃}(K² z/s)` and `p_{Q̃} < 269` give `p_Q < 269 K²/s < 270 K²/s`; also
`Y = KX` has coordinate densities `f(y/K)/K ≤ 1` when `f ≤ K`. -/
theorem main_density_scaling (K s p f : ℝ) (hK : 0 < K) (hs : 0 < s) (hp : p < 269) (hf : f ≤ K) :
    K ^ 2 / s * p < 270 * K ^ 2 / s ∧ f / K ≤ 1 := by
  constructor
  · have h : 0 < K ^ 2 / s := by positivity
    calc K ^ 2 / s * p < K ^ 2 / s * 269 := mul_lt_mul_of_pos_left hp h
      _ < K ^ 2 / s * 270 := mul_lt_mul_of_pos_left (by norm_num) h
      _ = 270 * K ^ 2 / s := by ring
  · rw [div_le_one hK]; exact hf

/-- **Remark 7.3.** `Q - a = (s/K²)(Q̃ - a')` gives `|Q - a|^{-1/2} = (K/√s) |Q̃ - a'|^{-1/2}`, so the bound 77 of
Proposition 7.2 becomes `77 K/√s`. -/
theorem remark73_scaling (K s : ℝ) (hK : 0 < K) (hs : 0 < s) : (s / K ^ 2) ^ (-(1 / 2 : ℝ)) = K / √s := by
  rw [Real.rpow_neg (by positivity), ← Real.sqrt_eq_rpow, Real.sqrt_div' _ (by positivity),
    Real.sqrt_sq hK.le]
  have : 0 < √s := Real.sqrt_pos.mpr hs
  field_simp

end QformFiveB
