import Mathlib.MeasureTheory.Integral.DominatedConvergence
import Mathlib.Analysis.SpecialFunctions.Exp
import Mathlib.Tactic.NormNum
import Mathlib.Tactic.Linarith
import Mathlib.Tactic.FieldSimp
import Mathlib.Tactic.Ring

/-!
Measure-theoretic and algebraic components of the critical Allen--Cahn note.
This file is NOT a formalization of Brownian motion, Ito's formula, the Bessel
construction, or the source SPDE. Its hypotheses are displayed explicitly.
No source open problem is declared solved by this file.
-/

open MeasureTheory Filter
open scoped Topology

namespace CriticalAllenCahn

/-- A strict loss of expectation prevents an integrable common dominator.
For the paper, F n is a stopped reciprocal-square Bessel process at a fixed time.
The stochastic construction of these hypotheses is outside this file. -/
theorem no_integrable_dominator_of_expectation_defect
    {Ω : Type*} [MeasurableSpace Ω] {μ : Measure Ω}
    (F : ℕ → Ω → ℝ) (f M : Ω → ℝ) (c : ℝ)
    (hF : ∀ n, AEStronglyMeasurable (F n) μ)
    (hbound : ∀ n, ∀ᵐ ω ∂μ, ‖F n ω‖ ≤ M ω)
    (hlim : ∀ᵐ ω ∂μ, Tendsto (fun n => F n ω) atTop (𝓝 (f ω)))
    (hint : ∀ n, ∫ ω, F n ω ∂μ = c)
    (hdefect : ∫ ω, f ω ∂μ < c) : ¬ Integrable M μ := by
  intro hM
  have hconv := tendsto_integral_of_dominated_convergence M hF hM hbound hlim
  have hc : Tendsto (fun n : ℕ => ∫ ω, F n ω ∂μ) atTop (𝓝 c) := by
    simpa only [hint] using (tendsto_const_nhds :
      Tendsto (fun _ : ℕ => c) atTop (𝓝 c))
  have heq : (∫ ω, f ω ∂μ) = c := tendsto_nhds_unique hconv hc
  exact (ne_of_lt hdefect) heq

/-- Nonintegrability transfers from a measurable nonnegative lower bound. -/
theorem nonintegrable_of_nonnegative_lower_bound
    {Ω : Type*} [MeasurableSpace Ω] {μ : Measure Ω} {M Z : Ω → ℝ}
    (hM : AEStronglyMeasurable M μ)
    (hnonneg : ∀ᵐ ω ∂μ, 0 ≤ M ω)
    (hdom : ∀ᵐ ω ∂μ, M ω ≤ Z ω)
    (hnot : ¬ Integrable M μ) : ¬ Integrable Z μ := by
  intro hZ
  exact hnot (hZ.mono_nonneg hM hnonneg hdom)

/-- The Gaussian reciprocal-square formula has a strictly positive defect. -/
theorem gaussian_expectation_defect (r S : ℝ) (hr : 0 < r) (_hS : 0 < S) :
    (1 - Real.exp (-(r ^ 2 / (2 * S)))) / r ^ 2 < 1 / r ^ 2 := by
  apply (div_lt_div_iff_of_pos_right (sq_pos_of_pos hr)).2
  have he := Real.exp_pos (-(r ^ 2 / (2 * S)))
  linarith

/-- Exact defect identity; the Gaussian integral itself is not formalized here. -/
theorem gaussian_defect_identity (r S : ℝ) :
    1 / r ^ 2 - (1 - Real.exp (-(r ^ 2 / (2 * S)))) / r ^ 2 =
      Real.exp (-(r ^ 2 / (2 * S))) / r ^ 2 := by ring

/-- Scalar critical coercivity: A=I, F(v)=2v-v^3, G(v)=sqrt(2)v^2. -/
theorem critical_coercivity_identity (v : ℝ) :
    v * (v - (2 * v - v ^ 3)) - (1 / 2 : ℝ) * (Real.sqrt 2 * v ^ 2) ^ 2 =
      -(v ^ 2) := by
  rw [mul_pow, Real.sq_sqrt (show (0 : ℝ) ≤ 2 by norm_num)]
  ring

theorem critical_coercivity_bound (v : ℝ) :
    v * (v - (2 * v - v ^ 3)) - (1 / 2 : ℝ) * (Real.sqrt 2 * v ^ 2) ^ 2 ≥
      v ^ 2 - 2 * v ^ 2 - 2 := by
  rw [critical_coercivity_identity]
  linarith

theorem critical_interpolation_indices :
    (1 / 2 : ℝ) < 2 / 3 ∧ (2 / 3 : ℝ) < 1 ∧
      (2 * (2 / 3 : ℝ) - 1) * (2 + 1) = 1 := by norm_num

/-- Ito algebra for Y=1/U; this is not an invocation of Ito's theorem. -/
theorem reciprocal_ito_coefficients (u : ℝ) (hu : u ≠ 0) :
    (-(1 / u ^ 2)) * (u - u ^ 3) +
      (1 / 2 : ℝ) * (2 / u ^ 3) * (Real.sqrt 2 * u ^ 2) ^ 2 =
      -(1 / u) + 3 * u := by
  rw [mul_pow, Real.sq_sqrt (show (0 : ℝ) ≤ 2 by norm_num)]
  field_simp [hu]
  ring

/-- A finite-time stopping identity yields a two-sided hitting bound. -/
theorem finite_time_hitting_bounds (p b r e S : ℝ)
    (hb : 0 < b) (_hr : 0 < r) (he0 : 0 ≤ e)
    (he : e ≤ (1 - Real.exp (-(r ^ 2 / (2 * S)))) / r ^ 2)
    (hid : p / b ^ 2 = 1 / r ^ 2 - e) :
    b ^ 2 * (Real.exp (-(r ^ 2 / (2 * S))) / r ^ 2) ≤ p ∧ p ≤ b ^ 2 / r ^ 2 := by
  have hb2 := sq_pos_of_pos hb
  have hp : p = b ^ 2 * (1 / r ^ 2 - e) := by
    exact (div_eq_iff (ne_of_gt hb2)).mp hid |>.trans (mul_comm _ _)
  constructor
  · rw [hp]
    apply mul_le_mul_of_nonneg_left _ (le_of_lt hb2)
    have hi := gaussian_defect_identity r S
    linarith
  · rw [hp]
    calc
      b ^ 2 * (1 / r ^ 2 - e) ≤ b ^ 2 * (1 / r ^ 2) :=
        mul_le_mul_of_nonneg_left (sub_le_self _ he0) (le_of_lt hb2)
      _ = b ^ 2 / r ^ 2 := by ring

end CriticalAllenCahn

#print axioms CriticalAllenCahn.no_integrable_dominator_of_expectation_defect
#print axioms CriticalAllenCahn.nonintegrable_of_nonnegative_lower_bound
#print axioms CriticalAllenCahn.gaussian_expectation_defect
#print axioms CriticalAllenCahn.gaussian_defect_identity
#print axioms CriticalAllenCahn.critical_coercivity_identity
#print axioms CriticalAllenCahn.critical_coercivity_bound
#print axioms CriticalAllenCahn.critical_interpolation_indices
#print axioms CriticalAllenCahn.reciprocal_ito_coefficients
#print axioms CriticalAllenCahn.finite_time_hitting_bounds
