import Mathlib.Data.Real.Basic
import Mathlib.Tactic.Linarith

/- The weighted-volume version of the point matching proof's key inequality. -/
theorem exclusive_flow_bound (a b qout qin z : ℝ)
    (ha : a ≤ qout) (hb : b ≤ qin) (balance : qout = qin + z)
    (exclusive : a = 0 ∨ b = 0) : a + b ≤ qin + max z 0 := by
  rcases exclusive with hz | hz
  · have hm : 0 ≤ max z 0 := le_max_right z 0
    linarith
  · have hm : z ≤ max z 0 := le_max_left z 0
    linarith

/- Finite induction used after proving the analytic tail recurrence. -/
theorem dyadic_contraction_bound (f : ℕ → ℝ) (a b k : ℝ)
    (ha : 0 ≤ a) (budget : a * k + b ≤ k)
    (initial : f 0 ≤ k)
    (step : ∀ n, f (n + 1) ≤ max (f n) (a * f n + b)) :
    ∀ n, f n ≤ k := by
  intro n
  induction n with
  | zero => exact initial
  | succ n ih =>
    apply le_trans (step n)
    apply max_le ih
    have hmul : a * f n ≤ a * k := mul_le_mul_of_nonneg_left ih ha
    linarith
