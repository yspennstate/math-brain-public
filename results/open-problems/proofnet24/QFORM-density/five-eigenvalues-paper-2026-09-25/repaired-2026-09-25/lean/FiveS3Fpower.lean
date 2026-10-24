import Mathlib.Analysis.SpecialFunctions.Gaussian.FourierTransform
import Mathlib.Analysis.SpecialFunctions.Gaussian.GaussianIntegral
import Mathlib.Analysis.SpecialFunctions.Pow.Real
import Mathlib.Analysis.SpecialFunctions.Sqrt
import Mathlib.Analysis.SpecificLimits.Basic
import Mathlib.MeasureTheory.Integral.Prod
import Mathlib.MeasureTheory.Measure.Lebesgue.Integral
import Mathlib.MeasureTheory.Measure.Typeclasses.Probability
import Mathlib.MeasureTheory.Measure.CharacteristicFunction.TaylorExpansion
import Mathlib.MeasureTheory.Group.Convolution
import Mathlib.Order.LiminfLimsup
import Mathlib.Tactic

/-!
Lemma 3.3 of "Quadratic forms with five large singular values have bounded densities" (repaired text,
sha256 90f859b7), with the law of `Z = Σ_{j ≤ m} (Y_j - Y_j')` built as a convolution power.

* `int_chf_le`: if `Law(Z) ≤ K · Lebesgue` and `φ_Z` is real and nonnegative, then `∫ φ_Z ≤ 2πK`. The paper reads this
  off the value at `0` of the continuous density of Lemma 2.1(b); here it follows from Lemma 2.1(c) at `a = 0`,
  `∫ e^{-t²/(4v)} φ_Z(t) dt = 2√(πv) E e^{-vZ²} ≤ 2√(πv) K √(π/v) = 2πK`, and Fatou's lemma as `v → ∞`. No
  integrability of `φ_Z` is assumed, so the Plancherel step `∫|f̂|^{2m} ≤ ∫|f̂|² = 2π‖f‖₂²` of the paper is not needed.
* `dlaw μ = μ ∗ μ∘(x ↦ -x)`, the law of `Y - Y'`; `zlaw μ m`, its `m`-fold convolution power, the law of `Z`;
  `chf_zlaw`: `φ_Z = |φ_μ|^{2m}`.
* `lemma33`: for every real `p ≥ 2`, `∫ |φ_μ|^p ≤ 2π √(2e) / √p`, given the conclusion of Lemma 3.2 for `Z`, namely
  `Law(Z) ≤ (√e / √(2m)) · Lebesgue` (`Z` is the linear form with coefficient vector of length `√(2m)` in the `2m`
  independent variables `Y_j`, `-Y_j'`, whose densities are at most one).

The first assertion of Lemma 3.3 (`Y - Y'` has density at most one) is `FiveS3Diff.lean`. The Fourier block is repeated
from `FiveS2Fourier.lean`, so that this file compiles on its own.
-/

open MeasureTheory Set
open scoped ENNReal

namespace QformFiveB

namespace Fpower

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

/-! ### The integral of a nonnegative characteristic function -/

section Integral

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

theorem chf_continuous (μ : Measure ℝ) [IsProbabilityMeasure μ] : Continuous (chf μ) := by
  have h : chf μ = charFun μ := funext (chf_eq_charFun μ)
  rw [h]
  exact continuous_charFun

/-- `E e^{-vZ²} ≤ K √(π/v)` when `Law(Z) ≤ K · Lebesgue`. -/
theorem gauss_moment_le (μ : Measure ℝ) [IsProbabilityMeasure μ] (K : ℝ) (hK : 0 ≤ K)
    (hμ : μ ≤ ENNReal.ofReal K • volume) (v : ℝ) (hv : 0 < v) :
    ∫ z, Real.exp (-(v * (z - 0) ^ 2)) ∂μ ≤ K * √(π / v) := by
  have hint : Integrable (fun z => Real.exp (-(v * (z - 0) ^ 2))) μ := by
    refine Integrable.mono' (integrable_const (1 : ℝ))
      (by fun_prop : Measurable fun z : ℝ => Real.exp (-(v * (z - 0) ^ 2))).aestronglyMeasurable
      (Filter.Eventually.of_forall (fun z => ?_))
    rw [Real.norm_eq_abs, abs_of_pos (Real.exp_pos _)]
    exact Real.exp_le_one_iff.2 (neg_nonpos.2 (mul_nonneg hv.le (sq_nonneg _)))
  have hgauss : ∫⁻ z : ℝ, ENNReal.ofReal (Real.exp (-v * z ^ 2)) = ENNReal.ofReal (√(π / v)) := by
    rw [← ofReal_integral_eq_lintegral_ofReal (integrable_exp_neg_mul_sq hv)
      (Filter.Eventually.of_forall (fun z => (Real.exp_pos _).le)), integral_gaussian]
  have h : ENNReal.ofReal (∫ z, Real.exp (-(v * (z - 0) ^ 2)) ∂μ) ≤ ENNReal.ofReal (K * √(π / v)) := by
    rw [ofReal_integral_eq_lintegral_ofReal hint (Filter.Eventually.of_forall (fun z => (Real.exp_pos _).le))]
    calc ∫⁻ z, ENNReal.ofReal (Real.exp (-(v * (z - 0) ^ 2))) ∂μ
        ≤ ∫⁻ z, ENNReal.ofReal (Real.exp (-(v * (z - 0) ^ 2))) ∂(ENNReal.ofReal K • volume) :=
          lintegral_mono' hμ le_rfl
      _ = ENNReal.ofReal K * ∫⁻ z : ℝ, ENNReal.ofReal (Real.exp (-v * z ^ 2)) := by
          rw [lintegral_smul_measure]
          congr 1
          apply lintegral_congr
          intro z
          rw [sub_zero, neg_mul]
      _ = ENNReal.ofReal (K * √(π / v)) := by rw [hgauss, ENNReal.ofReal_mul hK]
  exact (ENNReal.ofReal_le_ofReal_iff (by positivity)).1 h

/-- **Lemma 3.3, the Fourier step.** If `Law(Z) ≤ K · Lebesgue` and `φ_Z = φ` is real and nonnegative, then
`∫ φ ≤ 2πK`. -/
theorem int_chf_le (μ : Measure ℝ) [IsProbabilityMeasure μ] (K : ℝ) (hK : 0 ≤ K)
    (hμ : μ ≤ ENNReal.ofReal K • volume) (φ : ℝ → ℝ) (hφ : ∀ t, chf μ t = (φ t : ℂ)) (hφ0 : ∀ t, 0 ≤ φ t) :
    ∫⁻ t, ENNReal.ofReal (φ t) ≤ ENNReal.ofReal (2 * π * K) := by
  have hφre : φ = fun t => (chf μ t).re := funext (fun t => by rw [hφ t, Complex.ofReal_re])
  have hφm : Measurable φ := by
    rw [hφre]
    exact Complex.measurable_re.comp (chf_continuous μ).measurable
  have hφle : ∀ t, φ t ≤ 1 := fun t => by
    have h := chf_norm_le_one μ t
    rw [hφ t, Complex.norm_real, Real.norm_eq_abs] at h
    exact (le_abs_self _).trans h
  -- for every `v > 0`: `∫ e^{-t²/(4v)} φ ≤ 2πK`
  have hstep : ∀ v : ℝ, 0 < v →
      ∫⁻ t, ENNReal.ofReal (Real.exp (-(1 / (4 * v)) * t ^ 2) * φ t) ≤ ENNReal.ofReal (2 * π * K) := by
    intro v hv
    have hid := lemma21c μ 0 v hv
    have hpt : ∀ t : ℝ, ((Real.exp (-(1 / (4 * v)) * t ^ 2) : ℝ) : ℂ) * Complex.exp (-(((t * 0 : ℝ) : ℂ) * Complex.I))
        * chf μ t = ((Real.exp (-(1 / (4 * v)) * t ^ 2) * φ t : ℝ) : ℂ) := by
      intro t
      rw [hφ t, mul_zero, Complex.ofReal_zero, zero_mul, neg_zero, Complex.exp_zero, mul_one, Complex.ofReal_mul]
    simp only [hpt] at hid
    rw [integral_complex_ofReal, ← Complex.ofReal_mul] at hid
    have hreal := Complex.ofReal_injective hid
    have hint : Integrable (fun t : ℝ => Real.exp (-(1 / (4 * v)) * t ^ 2) * φ t) := by
      refine Integrable.mono' (integrable_exp_neg_mul_sq (by positivity : 0 < 1 / (4 * v)))
        ((by fun_prop : Measurable fun t : ℝ => Real.exp (-(1 / (4 * v)) * t ^ 2)).mul hφm).aestronglyMeasurable
        (Filter.Eventually.of_forall (fun t => ?_))
      rw [Real.norm_eq_abs, abs_mul, abs_of_pos (Real.exp_pos _), abs_of_nonneg (hφ0 t)]
      exact mul_le_of_le_one_right (Real.exp_pos _).le (hφle t)
    have hE := gauss_moment_le μ K hK hμ v hv
    have hs : 0 < √(π * v) := Real.sqrt_pos.2 (by positivity)
    have hJ : ∫ t : ℝ, Real.exp (-(1 / (4 * v)) * t ^ 2) * φ t
        = 2 * √(π * v) * ∫ z, Real.exp (-(v * (z - 0) ^ 2)) ∂μ := by
      rw [hreal]
      field_simp
    have hpp : √(π * v) * √(π / v) = π := by
      rw [← Real.sqrt_mul (by positivity), show π * v * (π / v) = π ^ 2 by field_simp,
        Real.sqrt_sq Real.pi_pos.le]
    rw [← ofReal_integral_eq_lintegral_ofReal hint
      (Filter.Eventually.of_forall (fun t => mul_nonneg (Real.exp_pos _).le (hφ0 t)))]
    apply ENNReal.ofReal_le_ofReal
    rw [hJ]
    calc 2 * √(π * v) * ∫ z, Real.exp (-(v * (z - 0) ^ 2)) ∂μ ≤ 2 * √(π * v) * (K * √(π / v)) :=
          mul_le_mul_of_nonneg_left hE (by positivity)
      _ = 2 * (√(π * v) * √(π / v)) * K := by ring
      _ = 2 * π * K := by rw [hpp]
  -- `v = n + 1 → ∞`
  have hmeas : ∀ n : ℕ, Measurable (fun t : ℝ =>
      ENNReal.ofReal (Real.exp (-(1 / (4 * ((n : ℝ) + 1))) * t ^ 2) * φ t)) := fun n =>
    ENNReal.measurable_ofReal.comp
      ((by fun_prop : Measurable fun t : ℝ => Real.exp (-(1 / (4 * ((n : ℝ) + 1))) * t ^ 2)).mul hφm)
  have hlim : ∀ t : ℝ, Filter.Tendsto (fun n : ℕ =>
      ENNReal.ofReal (Real.exp (-(1 / (4 * ((n : ℝ) + 1))) * t ^ 2) * φ t)) Filter.atTop
      (nhds (ENNReal.ofReal (φ t))) := by
    intro t
    apply ENNReal.tendsto_ofReal
    have h0 : Filter.Tendsto (fun n : ℕ => (-(t ^ 2 / 4)) * (1 / ((n : ℝ) + 1))) Filter.atTop
        (nhds ((-(t ^ 2 / 4)) * 0)) := tendsto_one_div_add_atTop_nhds_zero_nat.const_mul _
    rw [mul_zero] at h0
    have h1 : Filter.Tendsto (fun n : ℕ => -(1 / (4 * ((n : ℝ) + 1))) * t ^ 2) Filter.atTop (nhds 0) := by
      refine h0.congr (fun n => ?_)
      field_simp
    have h2 := ((Real.continuous_exp.tendsto 0).comp h1).mul_const (φ t)
    rw [Real.exp_zero, one_mul] at h2
    exact h2
  calc ∫⁻ t, ENNReal.ofReal (φ t)
      = ∫⁻ t, Filter.liminf (fun n : ℕ =>
          ENNReal.ofReal (Real.exp (-(1 / (4 * ((n : ℝ) + 1))) * t ^ 2) * φ t)) Filter.atTop := by
        apply lintegral_congr
        intro t
        exact ((hlim t).liminf_eq).symm
    _ ≤ Filter.liminf (fun n : ℕ => ∫⁻ t,
          ENNReal.ofReal (Real.exp (-(1 / (4 * ((n : ℝ) + 1))) * t ^ 2) * φ t)) Filter.atTop :=
        lintegral_liminf_le hmeas
    _ ≤ ENNReal.ofReal (2 * π * K) :=
        Filter.liminf_le_of_frequently_le' (Filter.Frequently.of_forall (fun n => hstep _ (by positivity)))

end Integral

/-! ### The law of `Z = Σ_{j ≤ m} (Y_j - Y_j')` -/

section ZLaw

open Real

/-- The law of `Y - Y'` for independent `Y, Y'` with law `μ`. -/
noncomputable def dlaw (μ : Measure ℝ) : Measure ℝ := μ ∗ μ.map ((-1 : ℝ) * ·)

/-- The law of `Σ_{j ≤ m} (Y_j - Y_j')`, the `m`-fold convolution power of `dlaw μ`. -/
noncomputable def zlaw (μ : Measure ℝ) : ℕ → Measure ℝ
  | 0 => Measure.dirac 0
  | m + 1 => zlaw μ m ∗ dlaw μ

instance dlaw_prob (μ : Measure ℝ) [IsProbabilityMeasure μ] : IsProbabilityMeasure (dlaw μ) := by
  unfold dlaw
  haveI : IsProbabilityMeasure (μ.map ((-1 : ℝ) * ·)) :=
    Measure.isProbabilityMeasure_map (by fun_prop : Measurable ((-1 : ℝ) * ·)).aemeasurable
  infer_instance

instance zlaw_prob (μ : Measure ℝ) [IsProbabilityMeasure μ] (m : ℕ) : IsProbabilityMeasure (zlaw μ m) := by
  induction m with
  | zero => unfold zlaw; infer_instance
  | succ m ih => unfold zlaw; infer_instance

theorem charFun_dlaw (μ : Measure ℝ) [IsProbabilityMeasure μ] (t : ℝ) :
    charFun (dlaw μ) t = ((‖charFun μ t‖ ^ 2 : ℝ) : ℂ) := by
  unfold dlaw
  rw [charFun_conv, charFun_map_mul, neg_one_mul, charFun_neg, Complex.mul_conj, Complex.normSq_eq_norm_sq]

theorem charFun_zlaw (μ : Measure ℝ) [IsProbabilityMeasure μ] (m : ℕ) (t : ℝ) :
    charFun (zlaw μ m) t = ((‖charFun μ t‖ ^ (2 * m) : ℝ) : ℂ) := by
  induction m with
  | zero => simp [zlaw, charFun_dirac]
  | succ m ih =>
    rw [zlaw, charFun_conv, ih, charFun_dlaw, ← Complex.ofReal_mul, ← pow_add]
    ring_nf

/-- `φ_Z = |φ_μ|^{2m}`. -/
theorem chf_zlaw (μ : Measure ℝ) [IsProbabilityMeasure μ] (m : ℕ) (t : ℝ) :
    chf (zlaw μ m) t = ((‖chf μ t‖ ^ (2 * m) : ℝ) : ℂ) := by
  rw [chf_eq_charFun, chf_eq_charFun, charFun_zlaw]

end ZLaw

/-! ### Lemma 3.3 -/

section Lemma33

open Real

/-- **Lemma 3.3.** Let `μ` be the law of `Y`, and suppose that for every `m ≥ 1` the law of
`Z = Σ_{j ≤ m} (Y_j - Y_j')` has density at most `√e / √(2m)` (Lemma 3.2, which needs the density of `Y` to be at most
one). Then `∫ |φ_Y|^p ≤ 2π √(2e) / √p` for every real `p ≥ 2`. -/
theorem lemma33 (μ : Measure ℝ) [IsProbabilityMeasure μ]
    (hZ : ∀ m : ℕ, 1 ≤ m → zlaw μ m ≤ ENNReal.ofReal (√(exp 1) / √(2 * (m : ℝ))) • volume)
    (p : ℝ) (hp : 2 ≤ p) :
    ∫⁻ t, ENNReal.ofReal (‖chf μ t‖ ^ p) ≤ ENNReal.ofReal (2 * π * √(2 * exp 1) / √p) := by
  set m := ⌊p / 2⌋₊ with hm
  have hm1 : 1 ≤ m := by
    rw [hm]
    apply Nat.le_floor
    push_cast
    linarith
  have hmr : (1 : ℝ) ≤ m := by exact_mod_cast hm1
  have hm2 : 2 * (m : ℝ) ≤ p := by
    have := Nat.floor_le (by positivity : 0 ≤ p / 2)
    rw [← hm] at this
    linarith
  have hm4 : p ≤ 4 * (m : ℝ) := by
    have h1 := Nat.lt_floor_add_one (p / 2)
    rw [← hm] at h1
    rcases le_or_gt 4 p with h4 | h4
    · linarith
    · linarith
  have hZm := int_chf_le (zlaw μ m) (√(exp 1) / √(2 * (m : ℝ))) (by positivity) (hZ m hm1)
    (fun t => ‖chf μ t‖ ^ (2 * m)) (fun t => chf_zlaw μ m t) (fun t => by positivity)
  calc ∫⁻ t, ENNReal.ofReal (‖chf μ t‖ ^ p)
      ≤ ∫⁻ t, ENNReal.ofReal (‖chf μ t‖ ^ (2 * m)) := by
        apply lintegral_mono
        intro t
        apply ENNReal.ofReal_le_ofReal
        rw [← Real.rpow_natCast]
        push_cast
        exact Real.rpow_le_rpow_of_exponent_ge' (norm_nonneg _) (chf_norm_le_one μ t) (by positivity) hm2
    _ ≤ ENNReal.ofReal (2 * π * (√(exp 1) / √(2 * (m : ℝ)))) := hZm
    _ ≤ ENNReal.ofReal (2 * π * √(2 * exp 1) / √p) := by
        apply ENNReal.ofReal_le_ofReal
        have hpos2m : 0 < √(2 * (m : ℝ)) := Real.sqrt_pos.2 (by positivity)
        have hposp : 0 < √p := Real.sqrt_pos.2 (by linarith)
        rw [mul_div_assoc]
        apply mul_le_mul_of_nonneg_left _ (by positivity)
        rw [div_le_div_iff₀ hpos2m hposp, ← Real.sqrt_mul (exp_pos 1).le, ← Real.sqrt_mul (by positivity)]
        apply Real.sqrt_le_sqrt
        nlinarith [exp_pos 1]

end Lemma33

end Fpower

end QformFiveB
