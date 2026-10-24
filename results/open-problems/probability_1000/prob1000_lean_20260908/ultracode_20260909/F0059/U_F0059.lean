/-
F0059 (Janson, Problem 18.39). The deterministic record-gap lemma behind the memo.

Setting: b_i are the record scales of h(k) = log(k w_k rho^k)/k, u i = h(b_i) < 0,
u i -> 0 (limsup h = 0 along the support), and b_{i+1} >= 2 b_i (sparse support).
If every consecutive record gap is at most c / b_i from some index i0 on, then
h(b_{i0}) >= -2c / b_{i0}.  Consequently b_{i0} w_{b_{i0}} >= e^{-2c} for every
large i0, contradicting  sum_k k w_k rho^k < infinity  (nu < infinity).
So for every c > 0 infinitely many record gaps exceed c / b_i.
-/
import Mathlib

open Filter Topology

/-- Finite telescoping bound: `u (i0+N) - u i0 ≤ 2c/B i0 - 2c/B (i0+N)`. -/
theorem F0059_telescope (u B : ℕ → ℝ) (c : ℝ) (i0 : ℕ)
    (hc : 0 ≤ c) (hB0 : 0 < B i0)
    (hB : ∀ i, 2 * B i ≤ B (i + 1))
    (hu : ∀ i, i0 ≤ i → u (i + 1) - u i ≤ c / B i) :
    ∀ N : ℕ, 0 < B (i0 + N) ∧ u (i0 + N) - u i0 ≤ 2 * c / B i0 - 2 * c / B (i0 + N) := by
  intro N
  induction N with
  | zero => simp [hB0]
  | succ N ih =>
    obtain ⟨hpos, hle⟩ := ih
    have hpos' : 0 < B (i0 + (N + 1)) := by
      have := hB (i0 + N)
      have h2 : 0 < 2 * B (i0 + N) := by positivity
      rw [show i0 + (N + 1) = i0 + N + 1 by ring]
      linarith
    refine ⟨hpos', ?_⟩
    have hstep := hu (i0 + N) (by omega)
    -- 2c / B(i0+N+1) ≤ c / B(i0+N)  because B(i0+N+1) ≥ 2 B(i0+N)
    have hkey : 2 * c / B (i0 + (N + 1)) ≤ c / B (i0 + N) := by
      rw [show i0 + (N + 1) = i0 + N + 1 by ring] at hpos' ⊢
      have h1 := hB (i0 + N)
      rw [div_le_div_iff₀ hpos' hpos]
      nlinarith [mul_nonneg hc hpos.le]
    have : u (i0 + (N + 1)) - u i0 = (u (i0 + N + 1) - u (i0 + N)) + (u (i0 + N) - u i0) := by
      rw [show i0 + (N + 1) = i0 + N + 1 by ring]; ring
    rw [this]
    have e0 : 2 * c / B i0 = 2 * (c / B i0) := by ring
    have e1 : 2 * c / B (i0 + N) = 2 * (c / B (i0 + N)) := by ring
    have e2 : 2 * c / B (i0 + (N + 1)) = 2 * (c / B (i0 + (N + 1))) := by ring
    rw [e0, e1] at hle
    rw [e2] at hkey
    rw [e0, e2]
    linarith

/-- The bound without the (nonnegative) correction term. -/
theorem F0059_bound (u B : ℕ → ℝ) (c : ℝ) (i0 : ℕ)
    (hc : 0 ≤ c) (hB0 : 0 < B i0)
    (hB : ∀ i, 2 * B i ≤ B (i + 1))
    (hu : ∀ i, i0 ≤ i → u (i + 1) - u i ≤ c / B i) :
    ∀ N : ℕ, u (i0 + N) - u i0 ≤ 2 * c / B i0 := by
  intro N
  obtain ⟨hpos, hle⟩ := F0059_telescope u B c i0 hc hB0 hB hu N
  have : 0 ≤ 2 * c / B (i0 + N) := by positivity
  linarith

/-- With `u → 0`, the record value at `i0` is at least `-2c / b_{i0}`. -/
theorem F0059_limit (u B : ℕ → ℝ) (c : ℝ) (i0 : ℕ)
    (hc : 0 ≤ c) (hB0 : 0 < B i0)
    (hB : ∀ i, 2 * B i ≤ B (i + 1))
    (hu : ∀ i, i0 ≤ i → u (i + 1) - u i ≤ c / B i)
    (hlim : Tendsto u atTop (𝓝 0)) :
    -(2 * c / B i0) ≤ u i0 := by
  have hshift : Tendsto (fun N => u (i0 + N)) atTop (𝓝 0) := by
    have h := hlim.comp (tendsto_add_atTop_nat i0)
    exact h.congr (fun N => by simp [Function.comp, add_comm])
  have hle : ∀ N, u (i0 + N) ≤ 2 * c / B i0 + u i0 := by
    intro N; have := F0059_bound u B c i0 hc hB0 hB hu N; linarith
  have := le_of_tendsto' hshift hle
  linarith

#print axioms F0059_telescope
#print axioms F0059_bound
#print axioms F0059_limit
