import Mathlib.Analysis.SpecialFunctions.Log.Basic
import Mathlib.Analysis.SpecialFunctions.Pow.Real
import Mathlib.Analysis.SpecialFunctions.Sqrt
import Mathlib.Analysis.SpecialFunctions.Gaussian.GaussianIntegral
import Mathlib.LinearAlgebra.Matrix.Trace
import Mathlib.LinearAlgebra.Matrix.Determinant.Basic
import Mathlib.MeasureTheory.Group.Integral
import Mathlib.MeasureTheory.Measure.Haar.NormedSpace
import Mathlib.MeasureTheory.Measure.Lebesgue.Integral
import Mathlib.Algebra.Order.Chebyshev
import Mathlib.Tactic

/-!
Section 3 of "Quadratic forms with five large singular values have bounded densities" (repaired text,
sha256 90f859b7): the finite and one-variable steps.

Theorem 3.1 (the heat-flow proof of geometric Brascamp-Lieb):
* `frame_trace`: `Σ c_i u_i u_iᵀ = I_d` with `|u_i| = 1` gives `Σ c_i = d`.
* `frame_quadratic`: the same identity gives `Σ c_i (u_i·x)² = |x|²`.
* `bl_pointwise`: `|Σ c_i v_i u_i|² ≤ Σ c_i v_i²` (the inequality `(∂_τ F - ΔF)/F ≥ 0`).
* `bl_heat_algebra`: with `a_i = f_i''/f_i` and `v_i = f_i'/f_i`, `Σ c_i a_i - (Σ c_i (a_i - v_i²) + |Σ c_i v_i u_i|²)`
  equals `Σ c_i v_i² - |Σ c_i v_i u_i|²` (the direct computation, given the formulas for the derivatives).
* `gaussian_normalization`: `(4π)^{-1/2} ∫ e^{-x²/4} dx = 1` (the limit `τ → ∞`, one coordinate).

Lemma 3.2:
* `beta_log_le`: `β log(1/β) ≤ 1 - β` for `0 ≤ β ≤ 1` (Lean's `log 0 = 0`, `1/0 = 0` give `0` at `β = 0`).
* `sum_beta_log_le`: `Σ β_i log(1/β_i) ≤ d` when `Σ β_i = n - d`.
* `rpow_inv_le_self`: `f^{1/β} ≤ f` for `0 ≤ f ≤ 1`, `0 < β ≤ 1`.
* `integral_rescale`: `∫ f(c + √β τ) dτ = β^{-1/2} ∫ f` for `β > 0`.
* `det_gram_svd`: `B = P Σ Uᵀ` with `P Pᵀ = I`, `Uᵀ U = I` gives `det(B Bᵀ) = det(Σ)²`.

Lemma 3.3: `fpower_floor` (`m = ⌊p/2⌋` has `1 ≤ m`, `p/4 ≤ m`, `2m ≤ p`), `pow_le_of_le_one'`
(`x^p ≤ x^{2m}` on `[0, 1]`), `fpower_constant` (`2π√e/√(2m) ≤ 2π√(2e)/√p`).
-/

open Real Matrix Finset MeasureTheory

namespace QformFiveB

section Frame

variable {d N : ℕ}

theorem trace_vecMulVec_self (u : Fin d → ℝ) : (vecMulVec u u).trace = u ⬝ᵥ u := by
  simp [Matrix.trace, Matrix.vecMulVec_apply, dotProduct]

/-- **Theorem 3.1**, first line: taking traces in the frame identity gives `Σ c_i = d`. -/
theorem frame_trace (c : Fin N → ℝ) (u : Fin N → Fin d → ℝ) (hu : ∀ i, u i ⬝ᵥ u i = 1)
    (hF : ∑ i, c i • vecMulVec (u i) (u i) = (1 : Matrix (Fin d) (Fin d) ℝ)) : ∑ i, c i = d := by
  have h := congrArg Matrix.trace hF
  rw [Matrix.trace_sum, Matrix.trace_one, Fintype.card_fin] at h
  simp only [Matrix.trace_smul, trace_vecMulVec_self, hu, smul_eq_mul, mul_one] at h
  exact h

/-- The frame identity as a quadratic form: `Σ c_i (u_i·x)² = |x|²`. -/
theorem frame_quadratic (c : Fin N → ℝ) (u : Fin N → Fin d → ℝ)
    (hF : ∑ i, c i • vecMulVec (u i) (u i) = (1 : Matrix (Fin d) (Fin d) ℝ)) (x : Fin d → ℝ) :
    ∑ i, c i * (u i ⬝ᵥ x) ^ 2 = x ⬝ᵥ x := by
  have h := congrArg (fun M : Matrix (Fin d) (Fin d) ℝ => x ⬝ᵥ (M *ᵥ x)) hF
  simp only [Matrix.one_mulVec] at h
  rw [← h, Matrix.sum_mulVec, dotProduct_sum]
  apply Finset.sum_congr rfl
  intro i _
  rw [Matrix.smul_mulVec, dotProduct_smul, smul_eq_mul]
  have e : x ⬝ᵥ (vecMulVec (u i) (u i) *ᵥ x) = (u i ⬝ᵥ x) ^ 2 := by
    simp only [dotProduct, Matrix.mulVec, Matrix.vecMulVec_apply]
    rw [sq, Finset.sum_mul_sum]
    rw [Finset.sum_comm]
    apply Finset.sum_congr rfl
    intro j _
    rw [Finset.mul_sum]
    apply Finset.sum_congr rfl
    intro k _
    ring
  rw [e]

/-- **Theorem 3.1**, the inequality `(∂_τ F - ΔF)/F ≥ 0`: for `c_i ≥ 0` and a tight frame,
`|Σ c_i v_i u_i|² ≤ Σ c_i v_i²`. -/
theorem bl_pointwise (c : Fin N → ℝ) (hc : ∀ i, 0 ≤ c i) (u : Fin N → Fin d → ℝ)
    (hF : ∑ i, c i • vecMulVec (u i) (u i) = (1 : Matrix (Fin d) (Fin d) ℝ)) (v : Fin N → ℝ) :
    (∑ i, (c i * v i) • u i) ⬝ᵥ (∑ i, (c i * v i) • u i) ≤ ∑ i, c i * v i ^ 2 := by
  set y := ∑ i, (c i * v i) • u i with hy
  have h1 : y ⬝ᵥ y = ∑ i, c i * v i * (u i ⬝ᵥ y) := by
    conv_lhs => rw [hy]
    rw [sum_dotProduct]
    apply Finset.sum_congr rfl
    intro i _
    rw [smul_dotProduct, smul_eq_mul]
  have hcs : (∑ i, c i * v i * (u i ⬝ᵥ y)) ^ 2
      ≤ (∑ i, c i * v i ^ 2) * (∑ i, c i * (u i ⬝ᵥ y) ^ 2) := by
    have := Finset.sum_mul_sq_le_sq_mul_sq Finset.univ (fun i => √(c i) * v i) (fun i => √(c i) * (u i ⬝ᵥ y))
    have e1 : ∀ i, √(c i) * v i * (√(c i) * (u i ⬝ᵥ y)) = c i * v i * (u i ⬝ᵥ y) := by
      intro i
      have := Real.mul_self_sqrt (hc i)
      calc √(c i) * v i * (√(c i) * (u i ⬝ᵥ y)) = (√(c i) * √(c i)) * v i * (u i ⬝ᵥ y) := by ring
        _ = c i * v i * (u i ⬝ᵥ y) := by rw [this]
    have e2 : ∀ i, (√(c i) * v i) ^ 2 = c i * v i ^ 2 := by
      intro i; rw [mul_pow, Real.sq_sqrt (hc i)]
    have e3 : ∀ i, (√(c i) * (u i ⬝ᵥ y)) ^ 2 = c i * (u i ⬝ᵥ y) ^ 2 := by
      intro i; rw [mul_pow, Real.sq_sqrt (hc i)]
    simp only [e1, e2, e3] at this
    exact this
  rw [frame_quadratic c u hF y, ← h1] at hcs
  have hyy : 0 ≤ y ⬝ᵥ y := Finset.sum_nonneg (fun i _ => mul_self_nonneg (y i))
  have hS : 0 ≤ ∑ i, c i * v i ^ 2 := Finset.sum_nonneg (fun i _ => mul_nonneg (hc i) (sq_nonneg _))
  rcases hyy.lt_or_eq with hpos | hzero
  · nlinarith
  · rw [← hzero]; exact hS

/-- The direct computation in Theorem 3.1, written with `a_i = f_i''/f_i` and `v_i = f_i'/f_i` (and `|u_i| = 1`):
`∂_τ F/F = Σ c_i a_i` and `ΔF/F = Σ c_i (a_i - v_i²) + |Σ c_i v_i u_i|²`, so the difference is
`Σ c_i v_i² - |Σ c_i v_i u_i|²`. -/
theorem bl_heat_algebra (c a v : Fin N → ℝ) (g : ℝ) :
    ∑ i, c i * a i - (∑ i, c i * (a i - v i ^ 2) + g) = ∑ i, c i * v i ^ 2 - g := by
  have : ∑ i, c i * (a i - v i ^ 2) = ∑ i, c i * a i - ∑ i, c i * v i ^ 2 := by
    rw [← Finset.sum_sub_distrib]; apply Finset.sum_congr rfl; intro i _; ring
  rw [this]; ring

/-- The limit `τ → ∞` in Theorem 3.1, one coordinate: `(4π)^{-1/2} ∫ e^{-x²/4} dx = 1`. -/
theorem gaussian_normalization : (√(4 * π))⁻¹ * ∫ x : ℝ, exp (-(1 / 4) * x ^ 2) = 1 := by
  rw [integral_gaussian (1 / 4)]
  have h : π / (1 / 4) = 4 * π := by ring
  rw [h]
  have hpos : 0 < √(4 * π) := Real.sqrt_pos.mpr (by positivity)
  field_simp

end Frame

section Projection

/-- **Lemma 3.2**, `β log(1/β) ≤ 1 - β` for `0 ≤ β ≤ 1`. -/
theorem beta_log_le (β : ℝ) (h0 : 0 ≤ β) (h1 : β ≤ 1) : β * log (1 / β) ≤ 1 - β := by
  rcases h0.lt_or_eq with hpos | hzero
  · have h := Real.log_le_sub_one_of_pos (show 0 < 1 / β by positivity)
    have e : β * (1 / β - 1) = 1 - β := by field_simp
    calc β * log (1 / β) ≤ β * (1 / β - 1) := mul_le_mul_of_nonneg_left h hpos.le
      _ = 1 - β := e
  · rw [← hzero]; simp

/-- **Lemma 3.2(a)**, the bound on `log p(y)`: `Σ β_i log(1/β_i) ≤ Σ (1 - β_i) = d` when `Σ β_i = n - d`. -/
theorem sum_beta_log_le {n : ℕ} (β : Fin n → ℝ) (d : ℝ) (h0 : ∀ i, 0 ≤ β i) (h1 : ∀ i, β i ≤ 1)
    (hsum : ∑ i, β i = n - d) : ∑ i, β i * log (1 / β i) ≤ d := by
  calc ∑ i, β i * log (1 / β i) ≤ ∑ i, (1 - β i) := Finset.sum_le_sum (fun i _ => beta_log_le (β i) (h0 i) (h1 i))
    _ = n - ∑ i, β i := by rw [Finset.sum_sub_distrib]; simp
    _ = d := by rw [hsum]; ring

/-- **Lemma 3.2(a)**, `f^{1/β} ≤ f` for `0 ≤ f ≤ 1` and `0 < β ≤ 1`. -/
theorem rpow_inv_le_self (f β : ℝ) (hf0 : 0 ≤ f) (hf1 : f ≤ 1) (hβ0 : 0 < β) (hβ1 : β ≤ 1) :
    f ^ (1 / β) ≤ f := by
  have hexp : 1 ≤ 1 / β := by rw [le_div_iff₀ hβ0]; linarith
  rcases hf0.lt_or_eq with hpos | hzero
  · calc f ^ (1 / β) ≤ f ^ (1 : ℝ) := Real.rpow_le_rpow_of_exponent_ge hpos hf1 hexp
      _ = f := Real.rpow_one f
  · rw [← hzero, Real.zero_rpow (by positivity)]

/-- **Lemma 3.2(a)**, the substitution: `∫ f(c + √β τ) dτ = β^{-1/2} ∫ f` for `β > 0`. -/
theorem integral_rescale (f : ℝ → ℝ) (c β : ℝ) (hβ : 0 < β) :
    ∫ τ, f (c + √β * τ) = (√β)⁻¹ * ∫ y, f y := by
  have hs : 0 < √β := Real.sqrt_pos.mpr hβ
  rw [MeasureTheory.Measure.integral_comp_mul_left (fun t => f (c + t)) √β,
    MeasureTheory.integral_add_left_eq_self (fun t => f t) c]
  rw [abs_of_pos (inv_pos.mpr hs), smul_eq_mul]

/-- **Lemma 3.2(b)**, the Jacobian: `B = P Σ Uᵀ` with `P Pᵀ = I` and `Uᵀ U = I` gives `det(B Bᵀ) = det(Σ)²`. -/
theorem det_gram_svd {d n : ℕ} (P S : Matrix (Fin d) (Fin d) ℝ) (U : Matrix (Fin n) (Fin d) ℝ)
    (hP : P * Pᵀ = 1) (hU : Uᵀ * U = 1) (hS : Sᵀ = S) :
    ((P * S * Uᵀ) * (P * S * Uᵀ)ᵀ).det = S.det ^ 2 := by
  have e : (P * S * Uᵀ) * (P * S * Uᵀ)ᵀ = P * (S * S) * Pᵀ := by
    rw [Matrix.transpose_mul, Matrix.transpose_mul, Matrix.transpose_transpose, hS]
    calc P * S * Uᵀ * (U * (S * Pᵀ)) = P * S * (Uᵀ * U) * (S * Pᵀ) := by simp only [Matrix.mul_assoc]
      _ = P * (S * S) * Pᵀ := by rw [hU, Matrix.mul_one]; simp only [Matrix.mul_assoc]
  have hdet : P.det * Pᵀ.det = 1 := by rw [← Matrix.det_mul, hP, Matrix.det_one]
  rw [e, Matrix.det_mul, Matrix.det_mul, Matrix.det_mul]
  calc P.det * (S.det * S.det) * Pᵀ.det = (P.det * Pᵀ.det) * (S.det * S.det) := by ring
    _ = S.det ^ 2 := by rw [hdet]; ring

end Projection

section FPower

/-- **Lemma 3.3**: `m = ⌊p/2⌋` has `1 ≤ m`, `p/4 ≤ m` and `2m ≤ p` for `p ≥ 2`. -/
theorem fpower_floor (p : ℝ) (hp : 2 ≤ p) :
    1 ≤ ⌊p / 2⌋₊ ∧ p / 4 ≤ (⌊p / 2⌋₊ : ℝ) ∧ 2 * (⌊p / 2⌋₊ : ℝ) ≤ p := by
  have h0 : 0 ≤ p / 2 := by linarith
  have hfl : (⌊p / 2⌋₊ : ℝ) ≤ p / 2 := Nat.floor_le h0
  have hlt : p / 2 < (⌊p / 2⌋₊ : ℝ) + 1 := Nat.lt_floor_add_one (p / 2)
  have h1 : 1 ≤ ⌊p / 2⌋₊ := by
    rw [Nat.one_le_floor_iff]; linarith
  have h1r : (1 : ℝ) ≤ ⌊p / 2⌋₊ := by exact_mod_cast h1
  refine ⟨h1, ?_, by linarith⟩
  by_cases hp4 : p < 4
  · linarith
  · push_neg at hp4; linarith

/-- **Lemma 3.3**: `x^p ≤ x^{2m}` for `0 ≤ x ≤ 1` and `2m ≤ p`. -/
theorem pow_le_of_le_one' (x p : ℝ) (m : ℕ) (hx0 : 0 ≤ x) (hx1 : x ≤ 1) (hm : 1 ≤ m) (hmp : 2 * (m : ℝ) ≤ p) :
    x ^ p ≤ x ^ (2 * m) := by
  rcases hx0.lt_or_eq with hpos | hzero
  · rw [← Real.rpow_natCast]
    exact Real.rpow_le_rpow_of_exponent_ge hpos hx1 (by push_cast; exact hmp)
  · have hm1 : (1 : ℝ) ≤ m := by exact_mod_cast hm
    have hp0 : p ≠ 0 := by linarith
    rw [← hzero, Real.zero_rpow hp0]
    positivity

/-- **Lemma 3.3**, the constant: `2π√e/√(2m) ≤ 2π√(2e)/√p` when `p/4 ≤ m`. -/
theorem fpower_constant (p : ℝ) (m : ℝ) (hp : 0 < p) (hm : p / 4 ≤ m) :
    2 * π * √(exp 1) / √(2 * m) ≤ 2 * π * √(2 * exp 1) / √p := by
  have hm0 : 0 < m := by linarith
  have h2m : 0 < √(2 * m) := Real.sqrt_pos.mpr (by positivity)
  have hsp : 0 < √p := Real.sqrt_pos.mpr hp
  rw [div_le_div_iff₀ h2m hsp, Real.sqrt_mul (by norm_num : (0 : ℝ) ≤ 2) (exp 1)]
  have key : √p ≤ √2 * √(2 * m) := by
    rw [← Real.sqrt_mul (by norm_num)]
    exact Real.sqrt_le_sqrt (by linarith)
  have hA : 0 ≤ 2 * π * √(exp 1) := by positivity
  calc 2 * π * √(exp 1) * √p ≤ 2 * π * √(exp 1) * (√2 * √(2 * m)) := mul_le_mul_of_nonneg_left key hA
    _ = 2 * π * (√2 * √(exp 1)) * √(2 * m) := by ring

end FPower

end QformFiveB
