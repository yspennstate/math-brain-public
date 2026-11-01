import Mathlib.Analysis.SpecialFunctions.Gaussian.FourierTransform
import Mathlib.Analysis.SpecialFunctions.Gaussian.GaussianIntegral
import Mathlib.Analysis.SpecialFunctions.ImproperIntegrals
import Mathlib.Analysis.SpecialFunctions.Integrals.Basic
import Mathlib.Analysis.SpecialFunctions.Pow.Real
import Mathlib.Analysis.SpecialFunctions.Sqrt
import Mathlib.Analysis.SpecificLimits.Basic
import Mathlib.MeasureTheory.Integral.Prod
import Mathlib.MeasureTheory.Integral.IntervalIntegral.Basic
import Mathlib.MeasureTheory.Integral.Lebesgue.Add
import Mathlib.MeasureTheory.Measure.Lebesgue.Integral
import Mathlib.MeasureTheory.Measure.Typeclasses.Probability
import Mathlib.MeasureTheory.Measure.Regular
import Mathlib.MeasureTheory.Function.JacobianOneDim
import Mathlib.Topology.Semicontinuity.Basic
import Mathlib.Topology.Instances.ENNReal.Lemmas
import Mathlib.Order.LiminfLimsup
import Mathlib.MeasureTheory.Measure.CharacteristicFunction.TaylorExpansion
import Mathlib.Analysis.Complex.ExponentialBounds
import Mathlib.Tactic

/-!
Corollary 4.4 (a) and (c) of "Quadratic forms with five large singular values have bounded densities" (repaired text,
sha256 90f859b7), from the bound of Theorem 4.1.

* (a) `cor44a`: if `|φ_Q(t)|² ≤ (√2 π e)³ ω(3)^{1/2} E₃^{-1/2} |t|^{-3}` for all `t ≠ 0` (Theorem 4.1 with `ℓ = 3`,
  `ω(3) = 9/2`), then `Q` has a density bounded by `C₃ E₃^{-1/6}` with `C₃ = 3√2 e (9/2)^{1/6} < 15`, through
  Lemma 2.2 with `p = 3/2` and `a = β₃^{2/3} E₃^{-1/6}`, as in the paper.
* (c) `cor44c`: Theorem 4.1 with `ℓ = 1` is `|φ_Q(t)| ≤ (√2 π e/(‖M‖_F |t|))^{1/2}`.

Lemma 2.2 (with the Gaussian-smoothing proof of the density bound of Lemma 2.1(b)) and the constants of Corollary 4.4
are repeated from `FiveS2Smooth.lean` and `FiveS4Cor.lean`, so that this file compiles on its own.
-/

open MeasureTheory Set
open scoped ENNReal

namespace QformFiveB

namespace CorA

section Fourier

open Complex

/-- `∫ c F = c ∫ F` for complex constants, stated with the instances of `ℂ` so that it rewrites. -/
theorem cintegral_const_mul {α : Type*} [MeasurableSpace α] (μ : Measure α) (c : ℂ) (F : α → ℂ) :
    ∫ x, c * F x ∂μ = c * ∫ x, F x ∂μ := integral_const_mul c F

/-- The characteristic function `φ(t) = ∫ e^{itz} dμ(z)`. -/
noncomputable def chf (μ : Measure ℝ) (t : ℝ) : ℂ := ∫ z, cexp (((t * z : ℝ) : ℂ) * I) ∂μ

/-- The Gaussian Fourier integral with `b = 1/(4v)`: `∫ e^{ixt} e^{-t²/(4v)} dt = 2√(πv) e^{-v x²}`. -/
theorem gauss_fourier (v : ℝ) (hv : 0 < v) (x : ℝ) :
    ∫ t : ℝ, cexp (((x * t : ℝ) : ℂ) * I) * ((Real.exp (-(1 / (4 * v)) * t ^ 2) : ℝ) : ℂ)
      = ((2 * Real.sqrt (Real.pi * v) : ℝ) : ℂ) * ((Real.exp (-(v * x ^ 2)) : ℝ) : ℂ) := by
  have hb : 0 < (((1 / (4 * v) : ℝ)) : ℂ).re := by rw [ofReal_re]; positivity
  have h := fourierIntegral_gaussian hb (x : ℂ)
  have hcongr : (fun t : ℝ => cexp (((x * t : ℝ) : ℂ) * I) * ((Real.exp (-(1 / (4 * v)) * t ^ 2) : ℝ) : ℂ))
      = fun t : ℝ => cexp (I * (x : ℂ) * t) * cexp (-(((1 / (4 * v) : ℝ)) : ℂ) * t ^ 2) := by
    funext t
    rw [ofReal_exp]
    congr 1
    · congr 1; push_cast; ring
    · congr 1; push_cast; ring
  rw [hcongr, h]
  have hv' : (v : ℂ) ≠ 0 := by exact_mod_cast hv.ne'
  congr 1
  · have h1 : (Real.pi : ℂ) / (((1 / (4 * v) : ℝ)) : ℂ) = ((4 * Real.pi * v : ℝ) : ℂ) := by
      push_cast
      rw [div_div_eq_mul_div, div_one]
      ring
    rw [h1, show (1 / 2 : ℂ) = ((1 / 2 : ℝ) : ℂ) by norm_num, ← ofReal_cpow (by positivity),
      ← Real.sqrt_eq_rpow]
    congr 1
    rw [show (4 : ℝ) * Real.pi * v = 2 ^ 2 * (Real.pi * v) by ring, Real.sqrt_mul (by positivity),
      Real.sqrt_sq (by norm_num)]
  · rw [ofReal_exp]
    congr 1
    push_cast
    field_simp
    try ring

/-- **Lemma 2.1(c).** `E e^{-v(Z-a)²} = (2√(πv))^{-1} ∫ e^{-t²/(4v)} e^{-ita} φ_Z(t) dt`. -/
theorem lemma21c (μ : Measure ℝ) [IsProbabilityMeasure μ] (a v : ℝ) (hv : 0 < v) :
    ((∫ z, Real.exp (-(v * (z - a) ^ 2)) ∂μ : ℝ) : ℂ)
      = ((1 / (2 * Real.sqrt (Real.pi * v)) : ℝ) : ℂ) *
        ∫ t : ℝ, ((Real.exp (-(1 / (4 * v)) * t ^ 2) : ℝ) : ℂ) * cexp (-(((t * a : ℝ) : ℂ) * I)) * chf μ t := by
  have hc : (2 * Real.sqrt (Real.pi * v)) ≠ 0 := by positivity
  have hpt : ∀ z : ℝ, ((Real.exp (-(v * (z - a) ^ 2)) : ℝ) : ℂ)
      = ((1 / (2 * Real.sqrt (Real.pi * v)) : ℝ) : ℂ) *
        ∫ t : ℝ, cexp ((((z - a) * t : ℝ) : ℂ) * I) * ((Real.exp (-(1 / (4 * v)) * t ^ 2) : ℝ) : ℂ) := by
    intro z
    rw [gauss_fourier v hv (z - a), ← mul_assoc, ← ofReal_mul, one_div_mul_cancel hc, ofReal_one, one_mul]
  have hint : Integrable (Function.uncurry fun (z t : ℝ) =>
      cexp ((((z - a) * t : ℝ) : ℂ) * I) * ((Real.exp (-(1 / (4 * v)) * t ^ 2) : ℝ) : ℂ)) (μ.prod volume) := by
    have hg : Integrable (fun p : ℝ × ℝ => Real.exp (-(1 / (4 * v)) * p.2 ^ 2)) (μ.prod volume) :=
      (integrable_exp_neg_mul_sq (by positivity : (0 : ℝ) < 1 / (4 * v))).comp_snd μ
    refine hg.mono' ?_ ?_
    · exact Continuous.aestronglyMeasurable (by fun_prop)
    · refine Filter.Eventually.of_forall (fun p => ?_)
      rcases p with ⟨z, t⟩
      simp only [Function.uncurry_apply_pair]
      rw [norm_mul, norm_exp_ofReal_mul_I, one_mul, Complex.norm_of_nonneg (Real.exp_pos _).le]
  rw [← integral_complex_ofReal]
  simp_rw [hpt]
  rw [cintegral_const_mul, integral_integral_swap hint]
  congr 1
  refine integral_congr_ae (Filter.Eventually.of_forall (fun t => ?_))
  have hsplit : ∀ z : ℝ, cexp ((((z - a) * t : ℝ) : ℂ) * I) * ((Real.exp (-(1 / (4 * v)) * t ^ 2) : ℝ) : ℂ)
      = (((Real.exp (-(1 / (4 * v)) * t ^ 2) : ℝ) : ℂ) * cexp (-(((t * a : ℝ) : ℂ) * I))) *
        cexp (((t * z : ℝ) : ℂ) * I) := by
    intro z
    have e : cexp ((((z - a) * t : ℝ) : ℂ) * I)
        = cexp (-(((t * a : ℝ) : ℂ) * I)) * cexp (((t * z : ℝ) : ℂ) * I) := by
      rw [← Complex.exp_add]
      congr 1
      push_cast
      ring
    rw [e]
    ring
  simp only [hsplit]
  rw [cintegral_const_mul]
  rfl

/-- **Lemma 2.1(c), the bound used later.** `E e^{-v(Z-a)²} ≤ (2√(πv))^{-1} ∫ e^{-t²/(4v)} |φ_Z(t)| dt`. -/
theorem lemma21c_bound (μ : Measure ℝ) [IsProbabilityMeasure μ] (a v : ℝ) (hv : 0 < v) :
    ∫ z, Real.exp (-(v * (z - a) ^ 2)) ∂μ
      ≤ (1 / (2 * Real.sqrt (Real.pi * v))) * ∫ t : ℝ, Real.exp (-(1 / (4 * v)) * t ^ 2) * ‖chf μ t‖ := by
  have h := congrArg (fun w : ℂ => ‖w‖) (lemma21c μ a v hv)
  simp only at h
  have hE : 0 ≤ ∫ z, Real.exp (-(v * (z - a) ^ 2)) ∂μ := integral_nonneg (fun z => (Real.exp_pos _).le)
  have hc : 0 ≤ 1 / (2 * Real.sqrt (Real.pi * v)) := by positivity
  rw [Complex.norm_of_nonneg hE, norm_mul, Complex.norm_of_nonneg hc] at h
  rw [h]
  gcongr
  refine (norm_integral_le_integral_norm _).trans (le_of_eq ?_)
  congr 1
  funext t
  have hphase : ‖cexp (-(((t * a : ℝ) : ℂ) * I))‖ = 1 := by
    rw [← neg_mul, ← ofReal_neg, norm_exp_ofReal_mul_I]
  rw [norm_mul, norm_mul, Complex.norm_of_nonneg (Real.exp_pos _).le, hphase, mul_one]

end Fourier

section Envelope

open Real

/-- **Lemma 2.2, the envelope integral.** `∫_ℝ min{1, (a/|t|)^p} dt = 2ap/(p-1)`. -/
theorem envelope_integral (a p : ℝ) (ha : 0 < a) (hp : 1 < p) :
    ∫ t : ℝ, min 1 ((a / |t|) ^ p) = 2 * a * p / (p - 1) := by
  have hsym := integral_comp_abs (f := fun s : ℝ => min 1 ((a / s) ^ p))
  simp only at hsym
  rw [hsym]
  have hg1 : ∀ x ∈ Ioc (0 : ℝ) a, min 1 ((a / x) ^ p) = 1 := by
    intro x hx
    have h1 : 1 ≤ a / x := by rw [le_div_iff₀ hx.1]; linarith [hx.2]
    exact min_eq_left (one_le_rpow h1 (by linarith))
  have hg2 : ∀ x ∈ Ioi a, min 1 ((a / x) ^ p) = a ^ p * x ^ (-p) := by
    intro x hx
    have hx0 : 0 < x := lt_trans ha hx
    have h1 : a / x ≤ 1 := by rw [div_le_one hx0]; exact le_of_lt hx
    rw [min_eq_right (rpow_le_one (by positivity) h1 (by linarith)), div_rpow ha.le hx0.le,
      rpow_neg hx0.le, div_eq_mul_inv]
  have hint1 : IntegrableOn (fun x : ℝ => min 1 ((a / x) ^ p)) (Ioc 0 a) :=
    IntegrableOn.congr_fun (integrableOn_const (C := (1 : ℝ))
      (by rw [Real.volume_Ioc]; exact ENNReal.ofReal_ne_top)) (fun x hx => (hg1 x hx).symm) measurableSet_Ioc
  have hint2 : IntegrableOn (fun x : ℝ => min 1 ((a / x) ^ p)) (Ioi a) :=
    IntegrableOn.congr_fun (Integrable.const_mul (integrableOn_Ioi_rpow_of_lt (by linarith : -p < -1) ha)
      (a ^ p)) (fun x hx => (hg2 x hx).symm) measurableSet_Ioi
  rw [← Ioc_union_Ioi_eq_Ioi ha.le, setIntegral_union Ioc_disjoint_Ioi_same measurableSet_Ioi hint1 hint2,
    setIntegral_congr_fun measurableSet_Ioc hg1, setIntegral_congr_fun measurableSet_Ioi hg2,
    setIntegral_const, volume_real_Ioc_of_le ha.le, integral_const_mul,
    integral_Ioi_rpow_of_lt (by linarith) ha]
  have key : a ^ p * a ^ (-p + 1) = a := by
    rw [← rpow_add ha, show p + (-p + 1) = 1 by ring, rpow_one]
  have e : a ^ p * (-a ^ (-p + 1) / (-p + 1)) = -(a ^ p * a ^ (-p + 1)) / (-p + 1) := by ring
  rw [e, key, smul_eq_mul, mul_one, sub_zero]
  have hp1 : (-p + 1) ≠ 0 := by linarith
  have hp2 : p - 1 ≠ 0 := by linarith
  field_simp
  ring

/-- Lemma 2.2's constant: `(2π)^{-1} · 2ap/(p-1) = ap/(π(p-1))`. -/
theorem envelope_density_constant (a p : ℝ) (hp : 1 < p) :
    (2 * π)⁻¹ * (2 * a * p / (p - 1)) = a * p / (π * (p - 1)) := by
  have hp2 : p - 1 ≠ 0 := by linarith
  have hpi : π ≠ 0 := pi_ne_zero
  field_simp

end Envelope

/-! ### The Gaussian kernel -/

/-- The Gaussian density of variance `σ²`. -/
noncomputable def gk (σ u : ℝ) : ℝ := 1 / (Real.sqrt (2 * Real.pi) * σ) * Real.exp (-(u ^ 2 / (2 * σ ^ 2)))

theorem gk_nonneg (σ u : ℝ) (hσ : 0 < σ) : 0 ≤ gk σ u := by
  unfold gk
  positivity

theorem gk_le (σ u : ℝ) (hσ : 0 < σ) : gk σ u ≤ 1 / (Real.sqrt (2 * Real.pi) * σ) := by
  unfold gk
  have h0 : 0 ≤ u ^ 2 / (2 * σ ^ 2) := by positivity
  have h1 : Real.exp (-(u ^ 2 / (2 * σ ^ 2))) ≤ 1 := Real.exp_le_one_iff.2 (by linarith)
  have h2 : 0 ≤ 1 / (Real.sqrt (2 * Real.pi) * σ) := by positivity
  calc 1 / (Real.sqrt (2 * Real.pi) * σ) * Real.exp (-(u ^ 2 / (2 * σ ^ 2)))
      ≤ 1 / (Real.sqrt (2 * Real.pi) * σ) * 1 := mul_le_mul_of_nonneg_left h1 h2
    _ = 1 / (Real.sqrt (2 * Real.pi) * σ) := mul_one _

theorem gk_continuous (σ : ℝ) : Continuous (gk σ) := by
  unfold gk
  fun_prop

theorem gk_eq (σ u : ℝ) (hσ : 0 < σ) :
    gk σ u = 1 / (Real.sqrt (2 * Real.pi) * σ) * Real.exp (-(1 / (2 * σ ^ 2)) * u ^ 2) := by
  unfold gk
  congr 2
  ring

theorem integrable_gk (σ : ℝ) (hσ : 0 < σ) : Integrable (gk σ) := by
  have h : Integrable (fun u : ℝ => 1 / (Real.sqrt (2 * Real.pi) * σ) * Real.exp (-(1 / (2 * σ ^ 2)) * u ^ 2)) :=
    (integrable_exp_neg_mul_sq (by positivity)).const_mul _
  refine h.congr (Filter.Eventually.of_forall (fun u => ?_))
  exact (gk_eq σ u hσ).symm

/-- `∫ g_σ = 1`. -/
theorem integral_gk (σ : ℝ) (hσ : 0 < σ) : ∫ u, gk σ u = 1 := by
  have hfun : gk σ = fun u => 1 / (Real.sqrt (2 * Real.pi) * σ) * Real.exp (-(1 / (2 * σ ^ 2)) * u ^ 2) :=
    funext (fun u => gk_eq σ u hσ)
  rw [hfun, integral_const_mul, integral_gaussian]
  have hs : 0 < Real.sqrt (2 * Real.pi) := Real.sqrt_pos.2 (by positivity)
  have e : Real.pi / (1 / (2 * σ ^ 2)) = (Real.sqrt (2 * Real.pi) * σ) ^ 2 := by
    rw [mul_pow, Real.sq_sqrt (by positivity)]
    field_simp <;> ring
  rw [e, Real.sqrt_sq (by positivity)]
  exact one_div_mul_cancel (by positivity)

theorem lintegral_gk (σ : ℝ) (hσ : 0 < σ) : ∫⁻ u, ENNReal.ofReal (gk σ u) = 1 := by
  rw [← ofReal_integral_eq_lintegral_ofReal (integrable_gk σ hσ)
    (Filter.Eventually.of_forall (fun u => gk_nonneg σ u hσ)), integral_gk σ hσ, ENNReal.ofReal_one]

/-- `σ g_σ(σ y) = g_1(y)`. -/
theorem gk_scale (σ y : ℝ) (hσ : 0 < σ) : σ * gk σ (σ * y) = gk 1 y := by
  unfold gk
  have e : (σ * y) ^ 2 / (2 * σ ^ 2) = y ^ 2 / (2 * 1 ^ 2) := by
    field_simp <;> ring
  rw [e]
  have hs : 0 < Real.sqrt (2 * Real.pi) := Real.sqrt_pos.2 (by positivity)
  field_simp <;> ring

/-! ### The smoothed density -/

/-- The smoothed density `p_σ(x) = E g_σ(x - Z)` is at most `(2π)^{-1} ∫ e^{-σ²t²/2} |φ(t)| dt`, from Lemma 2.1(c). -/
theorem smoothed_le (μ : Measure ℝ) [IsProbabilityMeasure μ] (σ x : ℝ) (hσ : 0 < σ) :
    ∫ z, gk σ (x - z) ∂μ ≤ (2 * Real.pi)⁻¹ * ∫ t : ℝ, Real.exp (-(σ ^ 2 / 2) * t ^ 2) * ‖chf μ t‖ := by
  have hv0 : 0 < 1 / (2 * σ ^ 2) := by positivity
  have h := lemma21c_bound μ x (1 / (2 * σ ^ 2)) hv0
  have hs : 0 < Real.sqrt (2 * Real.pi) := Real.sqrt_pos.2 (by positivity)
  have e1 : ∫ z, gk σ (x - z) ∂μ
      = 1 / (Real.sqrt (2 * Real.pi) * σ) * ∫ z, Real.exp (-(1 / (2 * σ ^ 2) * (z - x) ^ 2)) ∂μ := by
    rw [← integral_const_mul]
    congr 1
    funext z
    unfold gk
    congr 2
    ring
  have e2 : 1 / (4 * (1 / (2 * σ ^ 2))) = σ ^ 2 / 2 := by
    field_simp <;> ring
  have hsq : Real.sqrt (Real.pi * (1 / (2 * σ ^ 2))) = Real.sqrt (2 * Real.pi) / (2 * σ) := by
    rw [show Real.pi * (1 / (2 * σ ^ 2)) = (Real.sqrt (2 * Real.pi) / (2 * σ)) ^ 2 by
      rw [div_pow, Real.sq_sqrt (by positivity)]
      field_simp <;> ring, Real.sqrt_sq (by positivity)]
  have e3 : 1 / (Real.sqrt (2 * Real.pi) * σ) * (1 / (2 * Real.sqrt (Real.pi * (1 / (2 * σ ^ 2)))))
      = (2 * Real.pi)⁻¹ := by
    rw [hsq]
    have h2 : Real.sqrt (2 * Real.pi) ^ 2 = 2 * Real.pi := Real.sq_sqrt (by positivity)
    conv_rhs => rw [← h2]
    field_simp <;> ring
  have hc : 0 ≤ 1 / (Real.sqrt (2 * Real.pi) * σ) := by positivity
  rw [e1]
  calc 1 / (Real.sqrt (2 * Real.pi) * σ) * ∫ z, Real.exp (-(1 / (2 * σ ^ 2) * (z - x) ^ 2)) ∂μ
      ≤ 1 / (Real.sqrt (2 * Real.pi) * σ) * ((1 / (2 * Real.sqrt (Real.pi * (1 / (2 * σ ^ 2))))) *
          ∫ t : ℝ, Real.exp (-(1 / (4 * (1 / (2 * σ ^ 2)))) * t ^ 2) * ‖chf μ t‖) :=
        mul_le_mul_of_nonneg_left h hc
    _ = (2 * Real.pi)⁻¹ * ∫ t : ℝ, Real.exp (-(σ ^ 2 / 2) * t ^ 2) * ‖chf μ t‖ := by
        rw [e2, ← mul_assoc, e3]

/-! ### From the smoothed densities to the law -/

/-- A lower semicontinuous function does not jump up along a convergent sequence. -/
theorem lsc_le_liminf (h : ℝ → ℝ≥0∞) (hh : LowerSemicontinuous h) (u : ℕ → ℝ) (z : ℝ)
    (hu : Filter.Tendsto u Filter.atTop (nhds z)) :
    h z ≤ Filter.liminf (fun n => h (u n)) Filter.atTop := by
  refine le_of_forall_lt (fun c hc => ?_)
  obtain ⟨c', hc1, hc2⟩ := exists_between hc
  have hev : ∀ᶠ n in Filter.atTop, c' < h (u n) := hu.eventually (hh z c' hc2)
  exact lt_of_lt_of_le hc1 (Filter.le_liminf_of_le (h := hev.mono (fun n hn => hn.le)))

/-- The substitution `x = z + σ y`. -/
theorem lintegral_shift_scale (h : ℝ → ℝ≥0∞) (σ z : ℝ) (hσ : 0 < σ) :
    ∫⁻ y, h (z + σ * y) * ENNReal.ofReal (gk 1 y) = ∫⁻ x, h x * ENNReal.ofReal (gk σ (x - z)) := by
  have himg : (fun y => z + σ * y) '' univ = univ := by
    rw [image_univ]
    ext x
    simp only [mem_range, mem_univ, iff_true]
    exact ⟨(x - z) / σ, by field_simp; ring⟩
  have hinj : InjOn (fun y => z + σ * y) univ := by
    intro a _ b _ hab
    have hab' : z + σ * a = z + σ * b := hab
    exact mul_left_cancel₀ hσ.ne' (by linarith)
  have hd : ∀ y ∈ univ, HasDerivWithinAt (fun y => z + σ * y) (σ * 1) univ y :=
    fun y _ => ((hasDerivAt_id' (x := y)).const_mul σ).const_add z |>.hasDerivWithinAt
  have h1 := lintegral_image_eq_lintegral_abs_deriv_mul (f' := fun _ => σ * 1) MeasurableSet.univ hd hinj
    (fun x => h x * ENNReal.ofReal (gk σ (x - z)))
  rw [himg, Measure.restrict_univ] at h1
  rw [h1]
  apply lintegral_congr
  intro y
  simp only [mul_one, abs_of_pos hσ]
  rw [show z + σ * y - z = σ * y by ring, mul_left_comm, ← ENNReal.ofReal_mul hσ.le, gk_scale σ y hσ]

/-- If every smoothed density is at most `K`, then `∫ h dμ ≤ K ∫ h` for every lower semicontinuous `h ≥ 0`, by Fatou's
lemma twice along `σ = 1/(n+1)`. -/
theorem lintegral_le_of_smoothed_le (μ : Measure ℝ) [IsProbabilityMeasure μ] (K : ℝ)
    (hK : ∀ σ : ℝ, 0 < σ → ∀ x, ∫⁻ z, ENNReal.ofReal (gk σ (x - z)) ∂μ ≤ ENNReal.ofReal K)
    (h : ℝ → ℝ≥0∞) (hh : LowerSemicontinuous h) (hm : Measurable h) :
    ∫⁻ z, h z ∂μ ≤ ENNReal.ofReal K * ∫⁻ x, h x := by
  have hσpos : ∀ n : ℕ, 0 < 1 / ((n : ℝ) + 1) := fun n => by positivity
  have hσlim : Filter.Tendsto (fun n : ℕ => 1 / ((n : ℝ) + 1)) Filter.atTop (nhds 0) :=
    tendsto_one_div_add_atTop_nhds_zero_nat
  have hjoint : ∀ n : ℕ, Measurable (fun p : ℝ × ℝ => h p.2 * ENNReal.ofReal (gk (1 / ((n : ℝ) + 1)) (p.2 - p.1))) :=
    fun n => (hm.comp measurable_snd).mul
      (ENNReal.measurable_ofReal.comp ((gk_continuous _).measurable.comp (measurable_snd.sub measurable_fst)))
  have hF_meas : ∀ n : ℕ, Measurable (fun z => ∫⁻ x, h x * ENNReal.ofReal (gk (1 / ((n : ℝ) + 1)) (x - z))) :=
    fun n => (hjoint n).lintegral_prod_right'
  have hg1 : Measurable (fun y : ℝ => ENNReal.ofReal (gk 1 y)) :=
    ENNReal.measurable_ofReal.comp (gk_continuous 1).measurable
  have step1 : ∀ z, h z ≤ Filter.liminf
      (fun n : ℕ => ∫⁻ x, h x * ENNReal.ofReal (gk (1 / ((n : ℝ) + 1)) (x - z))) Filter.atTop := by
    intro z
    have e : ∀ n : ℕ, ∫⁻ x, h x * ENNReal.ofReal (gk (1 / ((n : ℝ) + 1)) (x - z))
        = ∫⁻ y, h (z + 1 / ((n : ℝ) + 1) * y) * ENNReal.ofReal (gk 1 y) :=
      fun n => (lintegral_shift_scale h _ z (hσpos n)).symm
    simp_rw [e]
    calc h z = ∫⁻ y, h z * ENNReal.ofReal (gk 1 y) := by
          rw [lintegral_const_mul _ hg1, lintegral_gk 1 one_pos, mul_one]
      _ ≤ ∫⁻ y, Filter.liminf (fun n : ℕ => h (z + 1 / ((n : ℝ) + 1) * y) * ENNReal.ofReal (gk 1 y))
            Filter.atTop := by
          apply lintegral_mono
          intro y
          have hlsc : LowerSemicontinuous (fun u => h u * ENNReal.ofReal (gk 1 y)) :=
            (ENNReal.continuous_mul_const ENNReal.ofReal_ne_top).comp_lowerSemicontinuous hh
              (fun a b hab => mul_le_mul_right' hab _)
          have hu : Filter.Tendsto (fun n : ℕ => z + 1 / ((n : ℝ) + 1) * y) Filter.atTop (nhds z) := by
            have := (hσlim.mul_const y).const_add z
            simpa using this
          exact lsc_le_liminf _ hlsc _ z hu
      _ ≤ Filter.liminf (fun n : ℕ => ∫⁻ y, h (z + 1 / ((n : ℝ) + 1) * y) * ENNReal.ofReal (gk 1 y))
            Filter.atTop :=
          lintegral_liminf_le (fun n => (hm.comp (measurable_const.add (measurable_const.mul measurable_id))).mul hg1)
  have step2 : ∀ n : ℕ, ∫⁻ z, (∫⁻ x, h x * ENNReal.ofReal (gk (1 / ((n : ℝ) + 1)) (x - z))) ∂μ
      ≤ ENNReal.ofReal K * ∫⁻ x, h x := by
    intro n
    rw [lintegral_lintegral_swap (hjoint n).aemeasurable]
    calc ∫⁻ x, ∫⁻ z, h x * ENNReal.ofReal (gk (1 / ((n : ℝ) + 1)) (x - z)) ∂μ
        = ∫⁻ x, h x * ∫⁻ z, ENNReal.ofReal (gk (1 / ((n : ℝ) + 1)) (x - z)) ∂μ := by
          apply lintegral_congr
          intro x
          have hmz : Measurable (fun z : ℝ => ENNReal.ofReal (gk (1 / ((n : ℝ) + 1)) (x - z))) :=
            ENNReal.measurable_ofReal.comp ((gk_continuous _).measurable.comp (measurable_const.sub measurable_id))
          rw [lintegral_const_mul _ hmz]
      _ ≤ ∫⁻ x, h x * ENNReal.ofReal K := by
          apply lintegral_mono
          intro x
          exact mul_le_mul_left' (hK _ (hσpos n) x) _
      _ = ENNReal.ofReal K * ∫⁻ x, h x := by
          rw [lintegral_mul_const _ hm, mul_comm]
  calc ∫⁻ z, h z ∂μ
      ≤ ∫⁻ z, Filter.liminf
          (fun n : ℕ => ∫⁻ x, h x * ENNReal.ofReal (gk (1 / ((n : ℝ) + 1)) (x - z))) Filter.atTop ∂μ :=
        lintegral_mono step1
    _ ≤ Filter.liminf
          (fun n : ℕ => ∫⁻ z, (∫⁻ x, h x * ENNReal.ofReal (gk (1 / ((n : ℝ) + 1)) (x - z))) ∂μ) Filter.atTop :=
        lintegral_liminf_le hF_meas
    _ ≤ ENNReal.ofReal K * ∫⁻ x, h x :=
        Filter.liminf_le_of_frequently_le' (Filter.Frequently.of_forall step2)

/-- **The smoothing principle.** If every smoothed density `E g_σ(x - Z)` is at most `K`, then the law of `Z` is at
most `K` times Lebesgue measure: first on open sets (their indicators are lower semicontinuous), then on every set by
outer regularity of Lebesgue measure. -/
theorem measure_le_of_smoothed_le (μ : Measure ℝ) [IsProbabilityMeasure μ] (K : ℝ)
    (hK : ∀ σ : ℝ, 0 < σ → ∀ x, ∫⁻ z, ENNReal.ofReal (gk σ (x - z)) ∂μ ≤ ENNReal.ofReal K) :
    μ ≤ ENNReal.ofReal K • volume := by
  have hopen : ∀ U : Set ℝ, IsOpen U → μ U ≤ ENNReal.ofReal K * volume U := by
    intro U hU
    have h1 := lintegral_le_of_smoothed_le μ K hK (U.indicator fun _ => (1 : ℝ≥0∞))
      (hU.lowerSemicontinuous_indicator (zero_le _)) (measurable_const.indicator hU.measurableSet)
    rwa [lintegral_indicator_const hU.measurableSet, lintegral_indicator_const hU.measurableSet, one_mul,
      one_mul] at h1
  rw [Measure.le_iff']
  intro B
  rw [Measure.smul_apply, smul_eq_mul]
  have key : ∀ r, ENNReal.ofReal K * volume B < r → μ B < r := by
    intro r hr
    rcases eq_or_ne (ENNReal.ofReal K) 0 with hK' | hK'
    · have h1 := hopen univ isOpen_univ
      rw [hK', zero_mul, measure_univ] at h1
      exact absurd (le_antisymm h1 (zero_le _)) one_ne_zero
    · have hKtop : ENNReal.ofReal K ≠ ⊤ := ENNReal.ofReal_ne_top
      have hlt : volume B < r / ENNReal.ofReal K := by
        rw [ENNReal.lt_div_iff_mul_lt (Or.inl hK') (Or.inl hKtop), mul_comm]
        exact hr
      obtain ⟨U, hBU, hU, hUr⟩ := Set.exists_isOpen_lt_of_lt B _ hlt
      calc μ B ≤ μ U := measure_mono hBU
        _ ≤ ENNReal.ofReal K * volume U := hopen U hU
        _ < r := by
            have := ENNReal.mul_lt_of_lt_div hUr
            rwa [mul_comm] at this
  exact le_of_not_gt (fun hlt => lt_irrefl _ (key _ hlt))

/-! ### Lemmas 2.1(b) and 2.2 -/

theorem integrable_gk_shift (μ : Measure ℝ) [IsProbabilityMeasure μ] (σ x : ℝ) (hσ : 0 < σ) :
    Integrable (fun z => gk σ (x - z)) μ := by
  refine Integrable.mono' (integrable_const (1 / (Real.sqrt (2 * Real.pi) * σ)))
    ((gk_continuous σ).measurable.comp (measurable_const.sub measurable_id)).aestronglyMeasurable
    (Filter.Eventually.of_forall (fun z => ?_))
  rw [Real.norm_eq_abs, abs_of_nonneg (gk_nonneg σ _ hσ)]
  exact gk_le σ _ hσ

/-- The smoothed density in `[0, ∞]`. -/
theorem lintegral_gk_shift (μ : Measure ℝ) [IsProbabilityMeasure μ] (σ x : ℝ) (hσ : 0 < σ) :
    ∫⁻ z, ENNReal.ofReal (gk σ (x - z)) ∂μ = ENNReal.ofReal (∫ z, gk σ (x - z) ∂μ) :=
  (ofReal_integral_eq_lintegral_ofReal (integrable_gk_shift μ σ x hσ)
    (Filter.Eventually.of_forall (fun z => gk_nonneg σ _ hσ))).symm

/-- **Lemma 2.1(b), in the form used.** If `φ_Z` is integrable, then `Z` has a density bounded by
`(2π)^{-1} ‖φ_Z‖₁`. -/
theorem lemma21b (μ : Measure ℝ) [IsProbabilityMeasure μ] (hφ : Integrable (fun t => ‖chf μ t‖)) :
    μ ≤ ENNReal.ofReal ((2 * Real.pi)⁻¹ * ∫ t, ‖chf μ t‖) • volume := by
  apply measure_le_of_smoothed_le μ
  intro σ hσ x
  rw [lintegral_gk_shift μ σ x hσ]
  apply ENNReal.ofReal_le_ofReal
  refine (smoothed_le μ σ x hσ).trans ?_
  apply mul_le_mul_of_nonneg_left _ (by positivity)
  refine integral_mono_of_nonneg (Filter.Eventually.of_forall (fun t => by positivity)) hφ
    (Filter.Eventually.of_forall (fun t => ?_))
  have h1 : Real.exp (-(σ ^ 2 / 2) * t ^ 2) ≤ 1 := Real.exp_le_one_iff.2 (by
    have : 0 ≤ σ ^ 2 / 2 * t ^ 2 := by positivity
    linarith)
  calc Real.exp (-(σ ^ 2 / 2) * t ^ 2) * ‖chf μ t‖ ≤ 1 * ‖chf μ t‖ :=
        mul_le_mul_of_nonneg_right h1 (norm_nonneg _)
    _ = ‖chf μ t‖ := one_mul _

/-- **Lemma 2.2.** If `|φ_Z(t)| ≤ min{1, (a/|t|)^p}` for all `t ≠ 0`, with `a > 0` and `p > 1`, then `Z` has a density
bounded by `ap/(π(p-1))`. -/
theorem lemma22 (μ : Measure ℝ) [IsProbabilityMeasure μ] (a p : ℝ) (ha : 0 < a) (hp : 1 < p)
    (henv : ∀ t : ℝ, t ≠ 0 → ‖chf μ t‖ ≤ min 1 ((a / |t|) ^ p)) :
    μ ≤ ENNReal.ofReal (a * p / (Real.pi * (p - 1))) • volume := by
  have hval : ∫ t : ℝ, min 1 ((a / |t|) ^ p) = 2 * a * p / (p - 1) := envelope_integral a p ha hp
  have hEint : Integrable (fun t : ℝ => min 1 ((a / |t|) ^ p)) := by
    apply Integrable.of_integral_ne_zero
    rw [hval]
    have : 0 < 2 * a * p / (p - 1) := by
      apply div_pos (by positivity) (by linarith)
    exact this.ne'
  have hne : ∀ᵐ t ∂(volume : Measure ℝ), t ≠ 0 := by
    rw [ae_iff]
    simp
  apply measure_le_of_smoothed_le μ
  intro σ hσ x
  rw [lintegral_gk_shift μ σ x hσ]
  apply ENNReal.ofReal_le_ofReal
  refine (smoothed_le μ σ x hσ).trans ?_
  rw [← envelope_density_constant a p hp, ← hval]
  apply mul_le_mul_of_nonneg_left _ (by positivity)
  refine integral_mono_of_nonneg (Filter.Eventually.of_forall (fun t => by positivity)) hEint ?_
  filter_upwards [hne] with t ht
  have h1 : Real.exp (-(σ ^ 2 / 2) * t ^ 2) ≤ 1 := Real.exp_le_one_iff.2 (by
    have : 0 ≤ σ ^ 2 / 2 * t ^ 2 := by positivity
    linarith)
  calc Real.exp (-(σ ^ 2 / 2) * t ^ 2) * ‖chf μ t‖ ≤ 1 * ‖chf μ t‖ :=
        mul_le_mul_of_nonneg_right h1 (norm_nonneg _)
    _ = ‖chf μ t‖ := one_mul _
    _ ≤ min 1 ((a / |t|) ^ p) := henv t ht

section Constants

open Real

/-- `C_3 = 3√2 e (9/2)^{1/6}`. -/
noncomputable def C3 : ℝ := 3 * √2 * exp 1 * (9 / 2 : ℝ) ^ (1 / 6 : ℝ)

/-- `C_2 = 8 e^{1/2} 2^{-1/8}`. -/
noncomputable def C2 : ℝ := 8 * exp (1 / 2) * (2 : ℝ) ^ (-(1 / 8 : ℝ))

/-- `β_3 = ((√2 π e)^3 ω(3)^{1/2})^{1/2}` with `ω(3) = 27/3! = 9/2`. -/
noncomputable def beta3 : ℝ := √((√2 * π * exp 1) ^ 3 * √(9 / 2))

/-- `β_2 = ((√2 π e)^2 ω(2)^{1/2})^{1/2}` with `ω(2) = 4/2! = 2`. -/
noncomputable def beta2 : ℝ := √((√2 * π * exp 1) ^ 2 * √2)

theorem omega_three_two : (3 : ℝ) ^ 3 / (Nat.factorial 3 : ℝ) = 9 / 2 ∧ (2 : ℝ) ^ 2 / (Nat.factorial 2 : ℝ) = 2 := by
  constructor <;> norm_num [Nat.factorial]

theorem sqrt2_pow_six : √2 ^ 6 = 8 := by
  have h : √2 ^ 2 = 2 := Real.sq_sqrt (by norm_num)
  calc √2 ^ 6 = (√2 ^ 2) ^ 3 := by ring
    _ = 8 := by rw [h]; norm_num

theorem C3_pow_six : C3 ^ 6 = 26244 * exp 1 ^ 6 := by
  unfold C3
  have h1 : ((9 / 2 : ℝ) ^ (1 / 6 : ℝ)) ^ 6 = 9 / 2 := by
    rw [← Real.rpow_natCast, ← Real.rpow_mul (by norm_num)]; norm_num
  calc (3 * √2 * exp 1 * (9 / 2 : ℝ) ^ (1 / 6 : ℝ)) ^ 6
      = 3 ^ 6 * √2 ^ 6 * exp 1 ^ 6 * ((9 / 2 : ℝ) ^ (1 / 6 : ℝ)) ^ 6 := by ring
    _ = 26244 * exp 1 ^ 6 := by rw [sqrt2_pow_six, h1]; ring

theorem C2_pow_eight : C2 ^ 8 = 8388608 * exp 1 ^ 4 := by
  unfold C2
  have h1 : ((2 : ℝ) ^ (-(1 / 8 : ℝ))) ^ 8 = 1 / 2 := by
    rw [← Real.rpow_natCast, ← Real.rpow_mul (by norm_num)]
    rw [show (-(1 / 8 : ℝ)) * ((8 : ℕ) : ℝ) = -1 by norm_num, Real.rpow_neg_one]; norm_num
  have h2 : exp (1 / 2) ^ 8 = exp 1 ^ 4 := by
    rw [← Real.exp_nat_mul, ← Real.exp_nat_mul]; norm_num
  calc (8 * exp (1 / 2) * (2 : ℝ) ^ (-(1 / 8 : ℝ))) ^ 8
      = 8 ^ 8 * exp (1 / 2) ^ 8 * ((2 : ℝ) ^ (-(1 / 8 : ℝ))) ^ 8 := by ring
    _ = 8388608 * exp 1 ^ 4 := by rw [h1, h2]; ring

theorem C3_pos : 0 < C3 := by unfold C3; positivity

theorem C2_pos : 0 < C2 := by unfold C2; positivity

/-- `e < 11/4`. -/
theorem exp_one_lt_eleven_quarters : exp 1 < 11 / 4 := by
  have := exp_one_lt_d9; norm_num at this ⊢; linarith

/-- **Corollary 4.4(a), the constant.** `C_3 < 15`, from `26244 (11/4)^6 < 15^6`. -/
theorem C3_lt_15 : C3 < 15 := by
  apply lt_of_pow_lt_pow_left₀ 6 (by norm_num : (0 : ℝ) ≤ 15)
  rw [C3_pow_six]
  have he := exp_one_lt_eleven_quarters
  have hep : 0 < exp 1 := exp_pos 1
  have h6 : exp 1 ^ 6 < (11 / 4) ^ 6 := by gcongr
  calc 26244 * exp 1 ^ 6 < 26244 * (11 / 4) ^ 6 := by linarith
    _ < 15 ^ 6 := by norm_num

/-- **Corollary 4.4(b), the constant.** `C_2 < 12.2`, from `8388608 (11/4)^4 < (61/5)^8`. -/
theorem C2_lt : C2 < 61 / 5 := by
  apply lt_of_pow_lt_pow_left₀ 8 (by norm_num : (0 : ℝ) ≤ 61 / 5)
  rw [C2_pow_eight]
  have he := exp_one_lt_eleven_quarters
  have hep : 0 < exp 1 := exp_pos 1
  have h4 : exp 1 ^ 4 < (11 / 4) ^ 4 := by gcongr
  calc 8388608 * exp 1 ^ 4 < 8388608 * (11 / 4) ^ 4 := by linarith
    _ < (61 / 5) ^ 8 := by norm_num

/-- **Corollary 4.4(a), the identity.** `3 β_3^{2/3}/π = C_3`: both are positive and have sixth power `26244 e^6`. -/
theorem cor44_a_identity : 3 * beta3 ^ (2 / 3 : ℝ) / π = C3 := by
  have hpi : 0 < π := pi_pos
  have hb0 : 0 ≤ beta3 := Real.sqrt_nonneg _
  have hX : 0 ≤ (√2 * π * exp 1) ^ 3 * √(9 / 2) := by positivity
  have hb2 : beta3 ^ 2 = (√2 * π * exp 1) ^ 3 * √(9 / 2) := Real.sq_sqrt hX
  have hs : √(9 / 2 : ℝ) ^ 2 = 9 / 2 := Real.sq_sqrt (by norm_num)
  have hpow : (beta3 ^ (2 / 3 : ℝ)) ^ 6 = (beta3 ^ 2) ^ 2 := by
    rw [← Real.rpow_natCast, ← Real.rpow_mul hb0]
    rw [show (2 / 3 : ℝ) * ((6 : ℕ) : ℝ) = ((4 : ℕ) : ℝ) by norm_num, Real.rpow_natCast]
    ring
  have hL : (3 * beta3 ^ (2 / 3 : ℝ) / π) ^ 6 = 26244 * exp 1 ^ 6 := by
    have e : (3 * beta3 ^ (2 / 3 : ℝ) / π) ^ 6 = 3 ^ 6 * (beta3 ^ (2 / 3 : ℝ)) ^ 6 / π ^ 6 := by ring
    rw [e, hpow, hb2]
    have e2 : ((√2 * π * exp 1) ^ 3 * √(9 / 2)) ^ 2 = √2 ^ 6 * π ^ 6 * exp 1 ^ 6 * √(9 / 2 : ℝ) ^ 2 := by ring
    rw [e2, sqrt2_pow_six, hs]
    field_simp
    ring
  have hLpos : 0 ≤ 3 * beta3 ^ (2 / 3 : ℝ) / π := by positivity
  have := C3_pos
  rw [← C3_pow_six] at hL
  exact (pow_left_inj₀ hLpos this.le (by norm_num : (6 : ℕ) ≠ 0)).mp hL

/-- **Corollary 4.4(b)**, `β_2 = 2^{3/4} π e`: both sides are positive with fourth power `8 π^4 e^4`. -/
theorem cor44_b_beta2 : beta2 = (2 : ℝ) ^ (3 / 4 : ℝ) * π * exp 1 := by
  have hpi : 0 < π := pi_pos
  have hX : 0 ≤ (√2 * π * exp 1) ^ 2 * √2 := by positivity
  have hb2 : beta2 ^ 2 = (√2 * π * exp 1) ^ 2 * √2 := Real.sq_sqrt hX
  have hs2 : √2 ^ 2 = 2 := Real.sq_sqrt (by norm_num)
  have h34 : ((2 : ℝ) ^ (3 / 4 : ℝ)) ^ 4 = 8 := by
    rw [← Real.rpow_natCast, ← Real.rpow_mul (by norm_num)]; norm_num
  have hL : beta2 ^ 4 = 8 * π ^ 4 * exp 1 ^ 4 := by
    have e : beta2 ^ 4 = (beta2 ^ 2) ^ 2 := by ring
    rw [e, hb2]
    have e2 : ((√2 * π * exp 1) ^ 2 * √2) ^ 2 = (√2 ^ 2) ^ 3 * π ^ 4 * exp 1 ^ 4 := by ring
    rw [e2, hs2]; norm_num
  have hR : ((2 : ℝ) ^ (3 / 4 : ℝ) * π * exp 1) ^ 4 = 8 * π ^ 4 * exp 1 ^ 4 := by
    have e : ((2 : ℝ) ^ (3 / 4 : ℝ) * π * exp 1) ^ 4 = ((2 : ℝ) ^ (3 / 4 : ℝ)) ^ 4 * π ^ 4 * exp 1 ^ 4 := by ring
    rw [e, h34]
  rw [← hR] at hL
  exact (pow_left_inj₀ (Real.sqrt_nonneg _) (by positivity) (by norm_num : (4 : ℕ) ≠ 0)).mp hL

/-- **Corollary 4.4(b), the identity.** `8 (β_2/(2π))^{1/2} = C_2`: both are positive with square `64 e 2^{-1/4}`. -/
theorem cor44_b_identity : 8 * √(beta2 / (2 * π)) = C2 := by
  have hpi : 0 < π := pi_pos
  have hq : beta2 / (2 * π) = (2 : ℝ) ^ (-(1 / 4 : ℝ)) * exp 1 := by
    rw [cor44_b_beta2]
    have e : (2 : ℝ) ^ (3 / 4 : ℝ) = 2 * (2 : ℝ) ^ (-(1 / 4 : ℝ)) := by
      rw [show (3 / 4 : ℝ) = 1 + (-(1 / 4)) by norm_num, Real.rpow_add (by norm_num), Real.rpow_one]
    rw [e]; field_simp
  rw [hq]
  unfold C2
  have h1 : √((2 : ℝ) ^ (-(1 / 4 : ℝ)) * exp 1) = (2 : ℝ) ^ (-(1 / 8 : ℝ)) * exp (1 / 2) := by
    rw [Real.sqrt_mul (by positivity), Real.sqrt_eq_rpow, Real.sqrt_eq_rpow, ← Real.rpow_mul (by norm_num),
      ← Real.exp_one_rpow, ← Real.rpow_mul (exp_pos 1).le, Real.exp_one_rpow]
    norm_num
  rw [h1]; ring

end Constants

/-! ### Corollary 4.4 (a) and (c) from Theorem 4.1 -/

section Corollary

open Real

theorem chf_eq_charFun (μ : Measure ℝ) (t : ℝ) : chf μ t = charFun μ t := by
  rw [charFun_apply_real]
  unfold chf
  congr 1
  funext z
  rw [Complex.ofReal_mul]

theorem chf_norm_le_one (μ : Measure ℝ) [IsProbabilityMeasure μ] (t : ℝ) : ‖chf μ t‖ ≤ 1 := by
  rw [chf_eq_charFun]
  exact norm_charFun_le_one t

/-- **Corollary 4.4(a).** If Theorem 4.1 holds with `ℓ = 3`, that is
`|φ_Q(t)|² ≤ (√2 π e)³ ω(3)^{1/2} E₃^{-1/2} |t|^{-3}` for `t ≠ 0` with `ω(3) = 27/3! = 9/2`, then `Q` has a density
bounded by `C₃ E₃^{-1/6}`, `C₃ = 3√2 e (9/2)^{1/6} < 15`: `|φ_Q| ≤ min{1, (a/|t|)^{3/2}}` with `a = β₃^{2/3} E₃^{-1/6}`,
and Lemma 2.2 with `p = 3/2` gives the bound `3a/π`. -/
theorem cor44a (μ : Measure ℝ) [IsProbabilityMeasure μ] (E3 : ℝ) (hE : 0 < E3)
    (hdecay : ∀ t : ℝ, t ≠ 0 → ‖chf μ t‖ ^ 2
      ≤ (√2 * π * exp 1) ^ 3 * √(9 / 2) * E3 ^ (-(1 / 2 : ℝ)) * |t| ^ (-(3 : ℝ))) :
    μ ≤ ENNReal.ofReal (C3 * E3 ^ (-(1 / 6 : ℝ))) • volume := by
  have hb0 : 0 < beta3 := Real.sqrt_pos.2 (by positivity)
  have hb2 : beta3 ^ 2 = (√2 * π * exp 1) ^ 3 * √(9 / 2) := Real.sq_sqrt (by positivity)
  have hbound : ∀ t : ℝ, t ≠ 0 → ‖chf μ t‖ ≤ beta3 * E3 ^ (-(1 / 4 : ℝ)) * |t| ^ (-(3 / 2 : ℝ)) := by
    intro t ht
    have hat : 0 < |t| := abs_pos.2 ht
    have h1 : (E3 ^ (-(1 / 4 : ℝ))) ^ 2 = E3 ^ (-(1 / 2 : ℝ)) := by
      rw [← Real.rpow_natCast, ← Real.rpow_mul hE.le]
      norm_num
    have h2 : (|t| ^ (-(3 / 2 : ℝ))) ^ 2 = |t| ^ (-(3 : ℝ)) := by
      rw [← Real.rpow_natCast, ← Real.rpow_mul hat.le]
      norm_num
    have key : (beta3 * E3 ^ (-(1 / 4 : ℝ)) * |t| ^ (-(3 / 2 : ℝ))) ^ 2
        = (√2 * π * exp 1) ^ 3 * √(9 / 2) * E3 ^ (-(1 / 2 : ℝ)) * |t| ^ (-(3 : ℝ)) := by
      rw [mul_pow, mul_pow, hb2, h1, h2]
    calc ‖chf μ t‖ = √(‖chf μ t‖ ^ 2) := (Real.sqrt_sq (norm_nonneg _)).symm
      _ ≤ √((beta3 * E3 ^ (-(1 / 4 : ℝ)) * |t| ^ (-(3 / 2 : ℝ))) ^ 2) :=
          Real.sqrt_le_sqrt (by rw [key]; exact hdecay t ht)
      _ = beta3 * E3 ^ (-(1 / 4 : ℝ)) * |t| ^ (-(3 / 2 : ℝ)) := Real.sqrt_sq (by positivity)
  have ha : 0 < beta3 ^ (2 / 3 : ℝ) * E3 ^ (-(1 / 6 : ℝ)) := by positivity
  have e1 : (beta3 ^ (2 / 3 : ℝ)) ^ (3 / 2 : ℝ) = beta3 := by
    rw [← Real.rpow_mul hb0.le]
    norm_num
  have e2 : (E3 ^ (-(1 / 6 : ℝ))) ^ (3 / 2 : ℝ) = E3 ^ (-(1 / 4 : ℝ)) := by
    rw [← Real.rpow_mul hE.le]
    norm_num
  have henv : ∀ t : ℝ, t ≠ 0 →
      ‖chf μ t‖ ≤ min 1 ((beta3 ^ (2 / 3 : ℝ) * E3 ^ (-(1 / 6 : ℝ)) / |t|) ^ (3 / 2 : ℝ)) := by
    intro t ht
    have hat : 0 < |t| := abs_pos.2 ht
    have e : (beta3 ^ (2 / 3 : ℝ) * E3 ^ (-(1 / 6 : ℝ)) / |t|) ^ (3 / 2 : ℝ)
        = beta3 * E3 ^ (-(1 / 4 : ℝ)) * |t| ^ (-(3 / 2 : ℝ)) := by
      rw [Real.div_rpow ha.le hat.le, Real.mul_rpow (by positivity) (by positivity), e1, e2,
        Real.rpow_neg hat.le, div_eq_mul_inv]
    rw [e]
    exact le_min (chf_norm_le_one μ t) (hbound t ht)
  have h := lemma22 μ _ (3 / 2) ha (by norm_num) henv
  have hpi : π ≠ 0 := Real.pi_ne_zero
  have hc : beta3 ^ (2 / 3 : ℝ) * E3 ^ (-(1 / 6 : ℝ)) * (3 / 2) / (π * (3 / 2 - 1)) = C3 * E3 ^ (-(1 / 6 : ℝ)) := by
    rw [← cor44_a_identity]
    field_simp <;> ring
  rwa [hc] at h

/-- **Corollary 4.4(c).** Theorem 4.1 with `ℓ = 1`, where `ω(1) = 1` and `E₁ = ‖M‖_F²`, reads
`|φ_Q(t)| ≤ (√2 π e/(‖M‖_F |t|))^{1/2}`. -/
theorem cor44c (φ MF t : ℝ) (hMF : 0 < MF) (ht : t ≠ 0) (hφ0 : 0 ≤ φ)
    (hdecay : φ ^ 2 ≤ (√2 * π * exp 1) ^ 1 * √1 * (MF ^ 2) ^ (-(1 / 2 : ℝ)) * |t| ^ (-(1 : ℝ))) :
    φ ≤ √(√2 * π * exp 1 / (MF * |t|)) := by
  have h1 : (MF ^ 2) ^ (-(1 / 2 : ℝ)) = MF⁻¹ := by
    rw [← Real.rpow_natCast, ← Real.rpow_mul hMF.le]
    norm_num [Real.rpow_neg_one]
  have h2 : |t| ^ (-(1 : ℝ)) = |t|⁻¹ := Real.rpow_neg_one _
  have e : (√2 * π * exp 1) ^ 1 * √1 * (MF ^ 2) ^ (-(1 / 2 : ℝ)) * |t| ^ (-(1 : ℝ))
      = √2 * π * exp 1 / (MF * |t|) := by
    rw [pow_one, Real.sqrt_one, mul_one, h1, h2, div_eq_mul_inv, mul_inv]
    ring
  calc φ = √(φ ^ 2) := (Real.sqrt_sq hφ0).symm
    _ ≤ √(√2 * π * exp 1 / (MF * |t|)) := Real.sqrt_le_sqrt (by rw [← e]; exact hdecay)

end Corollary

end CorA

end QformFiveB
