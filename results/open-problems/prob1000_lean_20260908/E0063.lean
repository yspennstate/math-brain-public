import Mathlib

/-!
# xi-quadratic stochastic operators converge to the empty body (Rozikov, Problem 10)

Let the population be split into `q` blocks with masses `e 1, …, e q ≥ 0`, and let `x₀` be the
mass of the empty body, `x₀ + ∑ e = 1`.  A xi-QSO sends every same-block pair and every pair
containing the empty body to the empty body, so the new empty-body mass satisfies
`x₀' ≥ x₀² + 2 x₀ (1 - x₀) + ∑ e_p²`.  Cauchy–Schwarz gives `∑ e_p² ≥ (1 - x₀)²/q`, hence
`1 - x₀' ≤ (1 - 1/q)(1 - x₀)²`.  Iterating: `y (n+1) ≤ c y n ^ 2 ≤ c y n` with `c = 1 - 1/q`,
so `y n ≤ c ^ n` and the empty body is the unique fixed point.  Both steps are certified here.
-/

open Finset BigOperators

namespace XiQSO

/-- The one-step contraction of the off-empty mass. -/
theorem one_step {q : ℕ} (hq : 0 < q) (e : Fin q → ℝ) (he : ∀ p, 0 ≤ e p)
    (x₀ x₀' : ℝ) (hsum : x₀ + ∑ p, e p = 1)
    (hstep : x₀ ^ 2 + 2 * x₀ * (1 - x₀) + ∑ p, e p ^ 2 ≤ x₀') :
    1 - x₀' ≤ (1 - 1 / (q : ℝ)) * (1 - x₀) ^ 2 := by
  have hcs : (∑ p, e p) ^ 2 ≤ (q : ℝ) * ∑ p, e p ^ 2 := by
    have := sq_sum_le_card_mul_sum_sq (s := (univ : Finset (Fin q))) (f := e)
    simpa using this
  have hq' : (0 : ℝ) < q := by exact_mod_cast hq
  have hE : ∑ p, e p = 1 - x₀ := by linarith
  rw [hE] at hcs
  have hsq : (1 - x₀) ^ 2 / (q : ℝ) ≤ ∑ p, e p ^ 2 := by
    rw [div_le_iff₀ hq']; linarith
  have h1 : 1 - x₀' ≤ (1 - x₀) ^ 2 - (1 - x₀) ^ 2 / (q : ℝ) := by nlinarith [hstep, hsq]
  have h2 : (1 - 1 / (q : ℝ)) * (1 - x₀) ^ 2 = (1 - x₀) ^ 2 - (1 - x₀) ^ 2 / (q : ℝ) := by ring
  rw [h2]; exact h1

/-- Iterating a contraction `y (n+1) ≤ c * y n ^ 2` with `0 ≤ y n ≤ 1` and `0 ≤ c`. -/
theorem iterate_bound (c : ℝ) (hc0 : 0 ≤ c) (y : ℕ → ℝ) (hy0 : ∀ n, 0 ≤ y n) (hy1 : ∀ n, y n ≤ 1)
    (hrec : ∀ n, y (n + 1) ≤ c * y n ^ 2) : ∀ n, y n ≤ c ^ n * y 0 := by
  intro n
  induction n with
  | zero => simp
  | succ n ih =>
    have h1 : y (n + 1) ≤ c * y n ^ 2 := hrec n
    have h2 : y n ^ 2 ≤ y n := by nlinarith [hy0 n, hy1 n]
    have h3 : c * y n ^ 2 ≤ c * y n := mul_le_mul_of_nonneg_left h2 hc0
    have h4 : c * y n ≤ c * (c ^ n * y 0) := mul_le_mul_of_nonneg_left ih hc0
    calc y (n + 1) ≤ c * y n ^ 2 := h1
      _ ≤ c * y n := h3
      _ ≤ c * (c ^ n * y 0) := h4
      _ = c ^ (n + 1) * y 0 := by ring

/-- A fixed point of the contraction with `c < 1` has zero off-empty mass. -/
theorem fixed_point_zero (c : ℝ) (hc0 : 0 ≤ c) (hc1 : c < 1) (y : ℝ) (hy0 : 0 ≤ y) (hy1 : y ≤ 1)
    (hfix : y ≤ c * y ^ 2) : y = 0 := by
  have h2 : y ^ 2 ≤ y := by nlinarith
  have : y ≤ c * y := by nlinarith [mul_le_mul_of_nonneg_left h2 hc0]
  nlinarith

end XiQSO

#print axioms XiQSO.one_step
#print axioms XiQSO.iterate_bound
#print axioms XiQSO.fixed_point_zero
