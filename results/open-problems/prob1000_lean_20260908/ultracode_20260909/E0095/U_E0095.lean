import Mathlib

/-!
E0095 (Diaconis, Question 4 of "Some things we've learned (about MCMC)").
Load-bearing algebraic step of Theorem 1 in the memo: if `φ` is a Fiedler vector of a
`d`-regular graph that takes the same value `a i` at both ends of each of the `r` added
edges, then the stationary variance of the shifted test vector `φ - c·1` for the new walk is
  `d‖φ‖² + 2 Σ a_i² - 4 (Σ a_i)² / N`,  `N = n d + 2 r` the total degree of the new graph,
and this is at least `d‖φ‖²`.  The inequality below is exactly that last step.
-/

theorem E0095_variance_step {r : ℕ} (a : Fin r → ℝ) (N : ℝ) (hN : 2 * (r : ℝ) ≤ N)
    (hNpos : 0 < N) :
    0 ≤ 2 * (∑ i, a i ^ 2) - 4 * (∑ i, a i) ^ 2 / N := by
  have hcs : (∑ i, a i) ^ 2 ≤ (r : ℝ) * ∑ i, a i ^ 2 := by
    have h := sq_sum_le_card_mul_sum_sq (s := (Finset.univ : Finset (Fin r))) (f := a)
    simpa using h
  have hsum : 0 ≤ ∑ i, a i ^ 2 := Finset.sum_nonneg (fun i _ => sq_nonneg _)
  rw [sub_nonneg, div_le_iff₀ hNpos]
  calc 4 * (∑ i, a i) ^ 2 ≤ 4 * ((r : ℝ) * ∑ i, a i ^ 2) := by gcongr
    _ = (2 * (r : ℝ)) * (2 * ∑ i, a i ^ 2) := by ring
    _ ≤ N * (2 * ∑ i, a i ^ 2) := by gcongr
    _ = (2 * ∑ i, a i ^ 2) * N := by ring

/-- Consequence used in the memo: the shifted variance dominates `d‖φ‖²`. -/
theorem E0095_variance_dominates {r : ℕ} (a : Fin r → ℝ) (N d s : ℝ) (hN : 2 * (r : ℝ) ≤ N)
    (hNpos : 0 < N) :
    d * s ≤ d * s + 2 * (∑ i, a i ^ 2) - 4 * (∑ i, a i) ^ 2 / N := by
  have := E0095_variance_step a N hN hNpos
  linarith

#print axioms E0095_variance_step
#print axioms E0095_variance_dominates
