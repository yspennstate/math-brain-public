import Mathlib

/-!
# E0110 (Tang, arXiv:1806.03755, Conjecture 1.5): the transport identities behind the
# relaxation time of the feed-forward GRBM

For the GRBM  dX_i = (μ_i + U'(X_i) − U'(X_{i−1})) dt + dB_i  (U'(X_0) := 0), two solutions
driven by the same Brownian motion have a difference Δ = X − X' solving the linear ODE
  Δ_i' = −a_i Δ_i + a_{i−1} Δ_{i−1},   a_0 = 0,   a_i ≥ 0  (divided differences of U'),
so the ℓ¹ coupling mass is dissipated only through the last coordinate.  Freezing the rates at
their stationary means m_i = Σ_{k≤i}|μ_k| gives a pure-birth chain; when m_i = iθ the mass
left at time t is 1 − (1 − e^{−θt})^d ≤ d e^{−θt}, and the mean transit time is
Σ 1/(iθ) ≤ (1 + log d)/θ.  When all rates equal a, Δ_{k}(t) = e^{−at} Σ_{j<k} (at)^j/j!.
Certified below: the telescoping identity, the Bernoulli bound and the harmonic bound.
(The constant-rate closed form Δ_k(t) = e^{−at} Σ_{j<k} (at)^j/j! is checked numerically, not here.)  The probabilistic parts (order
preservation, the stationary identity E U'(X_i) = m_i) are not formalised.
-/

open Finset

/-- Mass identity: with a_0 = 0, the sum over i = 1..d of (−a_i Δ_i + a_{i−1} Δ_{i−1}) equals
−a_d Δ_d.  Indexing: term i+1 for i ∈ range d. -/
theorem mass_leaks_only_through_last (a Δ : ℕ → ℝ) (h0 : a 0 = 0) (d : ℕ) :
    ∑ i ∈ range d, (-(a (i+1) * Δ (i+1)) + a i * Δ i) = -(a d * Δ d) := by
  induction d with
  | zero => simp [h0]
  | succ n ih => rw [sum_range_succ, ih]; ring

/-- Bernoulli: the mass left in the pure-birth chain with rates iθ, namely
1 − (1 − e^{−θt})^d, is at most d e^{−θt}. -/
theorem mass_left_le_d_exp (d : ℕ) (x : ℝ) (_hx0 : 0 ≤ x) (hx1 : x ≤ 1) :
    1 - (1 - x) ^ d ≤ d * x := by
  have h := one_add_mul_le_pow (a := -x) (by linarith) d
  have : 1 + (d : ℝ) * (-x) ≤ (1 - x) ^ d := by simpa [sub_eq_add_neg] using h
  linarith

theorem mass_left_exp (d : ℕ) (θ t : ℝ) (hθ : 0 ≤ θ) (ht : 0 ≤ t) :
    1 - (1 - Real.exp (-(θ * t))) ^ d ≤ d * Real.exp (-(θ * t)) :=
  mass_left_le_d_exp d _ (Real.exp_pos _).le
    (by rw [Real.exp_le_one_iff]; nlinarith)

/-- Mean transit time with rates iθ: Σ_{i<d} 1/((i+1)θ) ≤ (1 + log d)/θ. -/
theorem transit_time_le_log (d : ℕ) (θ : ℝ) (hθ : 0 < θ) :
    ∑ i ∈ range d, (((i : ℝ) + 1) * θ)⁻¹ ≤ (1 + Real.log d) / θ := by
  have hH : ((harmonic d : ℚ) : ℝ) = ∑ i ∈ range d, ((i : ℝ) + 1)⁻¹ := by
    simp [harmonic]
  have hlog : ((harmonic d : ℚ) : ℝ) ≤ 1 + Real.log d := by
    exact_mod_cast harmonic_le_one_add_log d
  have hsum : ∑ i ∈ range d, (((i : ℝ) + 1) * θ)⁻¹
      = θ⁻¹ * ∑ i ∈ range d, ((i : ℝ) + 1)⁻¹ := by
    rw [mul_sum]; refine sum_congr rfl fun i _ => ?_; rw [mul_inv]; ring
  rw [hsum, ← hH, div_eq_inv_mul]
  exact mul_le_mul_of_nonneg_left hlog (inv_nonneg.mpr hθ.le)

#print axioms mass_leaks_only_through_last
#print axioms mass_left_le_d_exp
#print axioms mass_left_exp
#print axioms transit_time_le_log
