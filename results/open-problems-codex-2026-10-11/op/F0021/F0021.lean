import Mathlib.Data.Real.Basic
import Mathlib.Tactic.Linarith
import Mathlib.Tactic.Positivity

-- Real exponents in the union bound, checked without axioms added here.
theorem union_exponents_negative (q : ℝ) (hq : 5 < q) :
    1 - q / 3 < 0 ∧ (5 - q) / 3 < 0 := by
  constructor <;> linarith

-- Positive partition functions: retaining restricted paths gives a ratio bound.
theorem restricted_mass_transfer (A B R q : ℝ)
    (hA : 0 < A) (hR : R ≤ B) (hB : B ≤ A) (heq : R = q * A) :
    q ≤ B / A ∧ B / A ≤ 1 := by
  constructor
  · apply (le_div_iff₀ hA).2
    linarith
  · apply (div_le_iff₀ hA).2
    simpa using hB

-- Threshold 5 from entropy-corrected single-site balancing.
theorem balanced_exponent_below_kpz (a : ℝ) (ha : 5 < a) :
    3 / (2 * a - 1) < (1 : ℝ) / 3 := by
  have hd : 0 < 2 * a - 1 := by linarith
  apply (div_lt_iff₀ hd).2
  linarith

-- An explicit nonempty interval for the tube-cap exponent.
theorem tube_cap_interval (a xi : ℝ) (ha : 0 < a)
    (hxi : 1 + xi < a / 3) :
    ∃ k : ℝ, (1 + xi) / a < k ∧ k < (1 : ℝ) / 3 := by
  have h : (1 + xi) / a < (1 : ℝ) / 3 := by
    apply (div_lt_iff₀ ha).2
    linarith
  exact ⟨(((1 + xi) / a) + (1 : ℝ) / 3) / 2, by linarith, by linarith⟩
