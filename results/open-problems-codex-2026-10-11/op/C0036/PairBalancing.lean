import Mathlib.Tactic.Linarith
import Mathlib.Data.Real.Basic

-- The nontrivial algebra in the two-Bernoulli geometric-mean smoothing step.
-- This does not formalize determinantal laws or their stochastic coupling.
theorem pair_sum_ge (u v p : ℝ) (hu : 0 ≤ u) (hv : 0 ≤ v)
    (hp : 0 ≤ p) (hprod : p * p = u * v) : 2 * p ≤ u + v := by
  apply le_of_not_gt
  intro h
  have hneg : u + v - 2 * p < 0 := by linarith
  have hpos : 0 < u + v + 2 * p := by linarith
  have hmul := mul_neg_of_neg_of_pos hneg hpos
  nlinarith [sq_nonneg (u - v)]

theorem pair_tail_balancing (u v p : ℝ) (hu : 0 ≤ u) (hv : 0 ≤ v)
    (hp : 0 ≤ p) (hprod : p * p = u * v) :
    (2 * p - p * p ≤ u + v - u * v) ∧ (p * p = u * v) := by
  constructor
  · have h := pair_sum_ge u v p hu hv hp hprod
    nlinarith
  · exact hprod
