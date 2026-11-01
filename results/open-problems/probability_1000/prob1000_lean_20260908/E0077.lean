import Mathlib

/-!
# The squared coefficient of variation of a stationary Cox process is at least one

Asanjarani and Nazarathy, *Stationary Markovian arrival processes: results and open
problems* (arXiv:1905.01736, ANZIAM J.), Conjecture 4.1: for an irreducible MMPP the
event-stationary inter-event time has `c² ≥ 1`.  Their earlier arXiv:1802.08400 §4 states the
same for a general Cox process on the line and remarks that a proof "would clearly use
different methods than the matrix analytic methods".

The method is Jensen's inequality.  Conditional on the directing measure, the process is
Poisson, so the time-stationary void probability is `S(t) = E[exp(-Λ(0,t])]`; by convexity of
`exp` and `E Λ(0,t] = λ* t` (stationarity), `S(t) ≥ exp(-λ* t)`; integrating,
`E[T^π] ≥ 1/λ* = E[T^α]`; the Palm inversion `E[T^π] = λ* E[(T^α)²]/2` then gives `c² ≥ 1`.

What is proved in Lean below: the Jensen step, the integral comparison, the algebraic step
from Palm inversion to `c² ≥ 1`, their assembly, and the two matrix identities that give
the MMPP form `c² = 2 λ* π(−C)⁻¹1 − 1`.  The probabilistic representation facts (Cox
conditioning, stationarity of the directing measure, Palm inversion, survival integrating to
the mean) enter as hypotheses of the assembly theorem; they are textbook.
-/

open MeasureTheory Real Set Filter

namespace CoxSCV

/-- Jensen for `exp` on a probability space: `exp (E Z) ≤ E (exp Z)`. -/
theorem exp_integral_le {Ω : Type*} [MeasurableSpace Ω] (μ : Measure Ω)
    [IsProbabilityMeasure μ] (Z : Ω → ℝ) (hZ : Integrable Z μ)
    (hexp : Integrable (fun ω => exp (Z ω)) μ) :
    exp (∫ ω, Z ω ∂μ) ≤ ∫ ω, exp (Z ω) ∂μ :=
  convexOn_exp.map_integral_le continuous_exp.continuousOn isClosed_univ
    (Eventually.of_forall fun _ => mem_univ _) hZ hexp

/-- The void probability of a Cox process dominates that of the Poisson process with the same
mean measure: `E[exp(-Λ)] ≥ exp(-E Λ)`. -/
theorem void_prob_ge {Ω : Type*} [MeasurableSpace Ω] (μ : Measure Ω)
    [IsProbabilityMeasure μ] (Λ : Ω → ℝ) (hΛ : Integrable Λ μ)
    (hexp : Integrable (fun ω => exp (-(Λ ω))) μ) :
    exp (-(∫ ω, Λ ω ∂μ)) ≤ ∫ ω, exp (-(Λ ω)) ∂μ := by
  have h := exp_integral_le μ (fun ω => -(Λ ω)) hΛ.neg hexp
  simpa [integral_neg] using h

/-- `∫₀^∞ exp(-(r t)) dt = 1/r`. -/
theorem integral_exp_neg_mul_Ioi_zero {r : ℝ} (hr : 0 < r) :
    ∫ t in Ioi (0:ℝ), exp (-(r * t)) = 1 / r := by
  have h := integral_comp_mul_left_Ioi (fun x : ℝ => exp (-x)) 0 hr
  simp only [mul_zero] at h
  rw [h, integral_exp_neg_Ioi_zero, smul_eq_mul, mul_one, one_div]

/-- A survival function dominating `exp(-(r t))` on `(0,∞)` integrates to at least `1/r`. -/
theorem integral_ge_inv {r : ℝ} (hr : 0 < r) (f : ℝ → ℝ) (hf : IntegrableOn f (Ioi 0))
    (hle : ∀ t ∈ Ioi (0:ℝ), exp (-(r * t)) ≤ f t) :
    1 / r ≤ ∫ t in Ioi (0:ℝ), f t := by
  rw [← integral_exp_neg_mul_Ioi_zero hr]
  have hi : IntegrableOn (fun t : ℝ => exp (-(r * t))) (Ioi 0) := by
    have := exp_neg_integrableOn_Ioi 0 hr
    simpa [neg_mul] using this
  exact setIntegral_mono_on hi hf measurableSet_Ioi hle

/-- Palm inversion `E[T^π] = λ* E[(T^α)²]/2` and `E[T^α] = 1/λ*` turn `E[T^π] ≥ 1/λ*` into
`c² = E[(T^α)²]/E[T^α]² − 1 ≥ 1`. -/
theorem scv_ge_one {lam m2 ETpi : ℝ} (hlam : 0 < lam)
    (hpalm : ETpi = lam * m2 / 2) (hge : 1 / lam ≤ ETpi) :
    1 ≤ m2 / (1 / lam) ^ 2 - 1 := by
  subst hpalm
  have hne : lam ≠ 0 := hlam.ne'
  have key : 2 ≤ lam ^ 2 * m2 := by
    rw [div_le_iff₀ hlam] at hge
    nlinarith [hge, hlam]
  have hrw : m2 / (1 / lam) ^ 2 = lam ^ 2 * m2 := by
    field_simp
  rw [hrw]
  linarith

/-- **Main theorem (Cox process form).**  With `Λ t` the directing mass of `(0,t]`, `S` the
time-stationary void probability, `lam` the intensity, `m2` the second Palm moment and
`ETpi` the mean forward recurrence time: `c² ≥ 1`. -/
theorem cox_scv_ge_one {Ω : Type*} [MeasurableSpace Ω] (μ : Measure Ω)
    [IsProbabilityMeasure μ] (Λ : ℝ → Ω → ℝ) (lam m2 ETpi : ℝ) (hlam : 0 < lam)
    (hint : ∀ t, Integrable (Λ t) μ)
    (hexp : ∀ t, Integrable (fun ω => exp (-(Λ t ω))) μ)
    (hmean : ∀ t, ∫ ω, Λ t ω ∂μ = lam * t)
    (S : ℝ → ℝ) (hS : ∀ t, S t = ∫ ω, exp (-(Λ t ω)) ∂μ)
    (hSint : IntegrableOn S (Ioi 0))
    (hET : ETpi = ∫ t in Ioi (0:ℝ), S t) (hpalm : ETpi = lam * m2 / 2) :
    1 ≤ m2 / (1 / lam) ^ 2 - 1 := by
  apply scv_ge_one hlam hpalm
  rw [hET]
  apply integral_ge_inv hlam S hSint
  intro t _
  rw [hS t, ← hmean t]
  exact void_prob_ge μ (Λ t) (hint t) (hexp t)

/-! ## The MMPP form -/

/-- With `πQ = 0` and `A = (D − Q)⁻¹`: `p D A = p`. -/
theorem vecMul_D_A {n : ℕ} (p : Fin n → ℝ) (Q D A : Matrix (Fin n) (Fin n) ℝ)
    (hpQ : Matrix.vecMul p Q = 0) (hA : (D - Q) * A = 1) :
    Matrix.vecMul p (D * A) = p := by
  have h : D * A = (D - Q) * A + Q * A := by rw [sub_mul, sub_add_cancel]
  rw [h, Matrix.vecMul_add, hA, Matrix.vecMul_one, ← Matrix.vecMul_vecMul, hpQ,
    Matrix.zero_vecMul, add_zero]

/-- The event-stationary phase law is `θ = πD/λ*`; its PH moments give
`c² = M₂/M₁² − 1 = 2 λ* (p A 1) − 1`, i.e. `c² ≥ 1 ⟺ p A 1 ≥ 1/λ* = E[T^α]`. -/
theorem mmpp_scv_formula {n : ℕ} (p : Fin n → ℝ) (Q D A : Matrix (Fin n) (Fin n) ℝ)
    (hpQ : Matrix.vecMul p Q = 0) (hA : (D - Q) * A = 1)
    (hp1 : dotProduct p 1 = 1) (lam : ℝ) (hlam : lam ≠ 0)
    (M1 M2 : ℝ)
    (hM1 : M1 = dotProduct (Matrix.vecMul ((1 / lam) • Matrix.vecMul p D) A) 1)
    (hM2 : M2 = 2 * dotProduct (Matrix.vecMul ((1 / lam) • Matrix.vecMul p D) (A * A)) 1) :
    M2 / M1 ^ 2 - 1 = 2 * lam * dotProduct (Matrix.vecMul p A) 1 - 1 := by
  have hDA := vecMul_D_A p Q D A hpQ hA
  have e1 : Matrix.vecMul ((1 / lam) • Matrix.vecMul p D) A = (1 / lam) • p := by
    rw [Matrix.smul_vecMul, Matrix.vecMul_vecMul, hDA]
  have e2 : Matrix.vecMul ((1 / lam) • Matrix.vecMul p D) (A * A)
      = (1 / lam) • Matrix.vecMul p A := by
    rw [Matrix.smul_vecMul, Matrix.vecMul_vecMul, ← mul_assoc, ← Matrix.vecMul_vecMul, hDA]
  rw [hM1, hM2, e1, e2, smul_dotProduct, smul_dotProduct, hp1, smul_eq_mul,
    smul_eq_mul, mul_one]
  field_simp

end CoxSCV

#print axioms CoxSCV.cox_scv_ge_one
#print axioms CoxSCV.mmpp_scv_formula
#print axioms CoxSCV.void_prob_ge
#print axioms CoxSCV.integral_ge_inv
#print axioms CoxSCV.scv_ge_one
