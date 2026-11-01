import Mathlib.Data.Nat.Choose.Basic
import Mathlib.Tactic.Linarith

-- General real-algebra step in the unimodal-mass proof.
theorem mass_bound (a p k : ℚ) (hp : 0 ≤ p)
    (hcount : a / 2 ≤ k) (hmass : k * p ≤ 1 / 2) : a * p ≤ 1 := by
  nlinarith [mul_nonneg (sub_nonneg.mpr hcount) hp]

-- Kernel-checked finite binomial instances; no native_decide.
example : ∀ (l a : Fin 13), 0 < a.val → a.val ≤ l.val →
    (l.val - a.val) % 2 = 0 →
    a.val * Nat.choose l.val ((l.val - a.val) / 2) ≤ 2 ^ l.val := by
  decide +kernel

-- The self-consistent density bound used in the logarithmic lower bound.
theorem density_lower_bound (α L r : ℚ) (hL : 0 ≤ L) (hr : 0 ≤ r)
    (h : L * (1 - α * r) ≤ α) : L / (1 + L * r) ≤ α := by
  have hpos : 0 < 1 + L * r := by
    nlinarith [mul_nonneg hL hr]
  apply (div_le_iff₀ hpos).2
  nlinarith only [h]
