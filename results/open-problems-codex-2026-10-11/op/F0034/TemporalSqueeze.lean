import Mathlib.Data.Real.Basic
import Mathlib.Order.Monotone.Basic

/- The algebraic temporal squeeze for an inverse bubble chain.
   The Brownian geometry supplying these hypotheses is proved separately. -/
theorem inverse_chain_cross_order
    (a b : ℕ → ℝ)
    (ha : Monotone a) (hb : Antitone b)
    (hgap : ∀ n, a n < b n) (n m : ℕ) : a n < b m := by
  exact lt_of_le_of_lt (ha (Nat.le_max_left n m))
    (lt_of_lt_of_le (hgap (max n m)) (hb (Nat.le_max_right n m)))

theorem inverse_chain_finite_window
    (a b : ℕ → ℝ)
    (ha : Monotone a) (hb : Antitone b)
    (hgap : ∀ n, a n < b n) (n : ℕ) :
    a 0 ≤ a n ∧ a n < b n ∧ b n ≤ b 0 := by
  exact ⟨ha (Nat.zero_le n), hgap n, hb (Nat.zero_le n)⟩
