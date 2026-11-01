import Mathlib.Analysis.SpecialFunctions.PolarCoord
import Mathlib.MeasureTheory.Function.JacobianOneDim
import Mathlib.MeasureTheory.Measure.Lebesgue.EqHaar
import Mathlib.MeasureTheory.Constructions.BorelSpace.Real
import Mathlib.LinearAlgebra.Matrix.ToLin
import Mathlib.MeasureTheory.Integral.IntervalIntegral.FundThmCalculus
import Mathlib.Analysis.SpecialFunctions.Integrals.Basic
import Mathlib.Analysis.SpecialFunctions.Log.Basic
import Mathlib.Analysis.SpecialFunctions.Sqrt
import Mathlib.Analysis.SpecialFunctions.Pow.Real
import Mathlib.Analysis.SpecialFunctions.ExpDeriv
import Mathlib.Analysis.Calculus.Deriv.MeanValue
import Mathlib.Analysis.Complex.ExponentialBounds
import Mathlib.Tactic

/-!
Lemma 5.3 of "Quadratic forms with five large singular values have bounded densities" (repaired text,
sha256 90f859b7), the estimate along one branch of the hyperbola.

Along the branch `τ ↦ u e^τ + u' e^{-τ}` in `ℝ²`, with `|u| = |u'| = ρ₀`, the proof bounds
`∫_ℝ f₁(w₁(τ)) f₂(w₂(τ)) dτ` for densities `0 ≤ f_j ≤ 1` by `6 log 2 + (3/2) log 2 + log⁺(32/(δΛ))`, where
`32/(δΛ) = 8/ρ₀²`.

* `bathtub_inv`: for `0 ≤ f ≤ 1` with `∫_{[m,∞)} f ≤ 1`, `∫_{[m,∞)} f(y)/y dy ≤ log(1 + 1/m)` (the indicator of the unit
  interval next to `m` is the extremal function).
* `tail_small`, `curve_tail`: for `p > 0`, `|p'| ≤ √2 p` and `τ ≥ T ≥ (3/4) log 2`, `y(τ) = p e^τ + p' e^{-τ}` satisfies
  `y ≥ p e^τ/2` and `y' ≥ y/3`, and `∫_T^∞ g(y(τ)) dτ ≤ 3 ∫_{[m,∞)} g(y)/y dy` with `m = p e^T/2`.
* `tail_log2`: with `T = max((3/4) log 2, log(2/|p|))`, so that `m ≥ 1`, the tail is at most `3 log 2`, for either sign
  of `p`.
* `branch_bound`: the per-branch bound `∫ f₁ f₂ dτ ≤ 6 + log⁺(8/ρ₀²)`.
-/

open MeasureTheory Set Real
open scoped ENNReal

namespace QformFiveB

namespace Hyper

/-- **The bathtub bound on a half-line.** If `0 ≤ f ≤ 1` and `∫_{[m,∞)} f ≤ 1` with `m > 0`, then
`∫_{[m,∞)} f(y) y⁻¹ dy ≤ log(1 + m⁻¹)`. -/
theorem bathtub_inv (f : ℝ → ℝ) (hf : Measurable f) (hf0 : ∀ y, 0 ≤ f y) (hf1 : ∀ y, f y ≤ 1)
    (m : ℝ) (hm : 0 < m) (hint : ∫⁻ y in Ici m, ENNReal.ofReal (f y) ≤ 1) :
    ∫⁻ y in Ici m, ENNReal.ofReal (f y * y⁻¹) ≤ ENNReal.ofReal (Real.log (1 + m⁻¹)) := by
  have hm1 : 0 < m + 1 := by linarith
  set g : ℝ → ℝ := fun y => y⁻¹ - (m + 1)⁻¹ with hg
  have hpt : ∀ y ∈ Ici m, ENNReal.ofReal (f y * y⁻¹)
      ≤ (Icc m (m + 1)).indicator (fun y => ENNReal.ofReal (g y)) y
        + ENNReal.ofReal ((m + 1)⁻¹) * ENNReal.ofReal (f y) := by
    intro y hy
    have hy' : m ≤ y := hy
    have hypos : 0 < y := lt_of_lt_of_le hm hy'
    by_cases h : y ∈ Icc m (m + 1)
    · have h1 : (m + 1)⁻¹ ≤ y⁻¹ := inv_anti₀ hypos h.2
      rw [indicator_of_mem h, ← ENNReal.ofReal_mul (inv_nonneg.2 hm1.le),
        ← ENNReal.ofReal_add (by simp only [hg]; linarith) (mul_nonneg (inv_nonneg.2 hm1.le) (hf0 y))]
      apply ENNReal.ofReal_le_ofReal
      have h2 : 0 ≤ (1 - f y) * (y⁻¹ - (m + 1)⁻¹) := mul_nonneg (by linarith [hf1 y]) (by linarith)
      simp only [hg]
      nlinarith [h2]
    · rw [indicator_of_notMem h, zero_add, ← ENNReal.ofReal_mul (inv_nonneg.2 hm1.le)]
      apply ENNReal.ofReal_le_ofReal
      have hy2 : m + 1 < y := by
        by_contra hc
        push_neg at hc
        exact h ⟨hy', hc⟩
      have h1 : y⁻¹ ≤ (m + 1)⁻¹ := inv_anti₀ hm1 hy2.le
      rw [mul_comm ((m + 1)⁻¹)]
      exact mul_le_mul_of_nonneg_left h1 (hf0 y)
  have hgm : Measurable g := by
    simp only [hg]
    fun_prop
  have hmeas_ind : Measurable ((Icc m (m + 1)).indicator (fun y => ENNReal.ofReal (g y))) :=
    (ENNReal.measurable_ofReal.comp hgm).indicator measurableSet_Icc
  have hcont : ContinuousOn g (Icc m (m + 1)) := by
    apply ContinuousOn.sub _ continuousOn_const
    exact continuousOn_inv₀.mono (fun x hx => ne_of_gt (lt_of_lt_of_le hm hx.1))
  have hIcc : ∫⁻ y in Ici m, (Icc m (m + 1)).indicator (fun y => ENNReal.ofReal (g y)) y
      = ENNReal.ofReal (Real.log (1 + m⁻¹) - (m + 1)⁻¹) := by
    rw [lintegral_indicator measurableSet_Icc, Measure.restrict_restrict measurableSet_Icc,
      inter_eq_left.2 Icc_subset_Ici_self]
    rw [← ofReal_integral_eq_lintegral_ofReal (hcont.integrableOn_compact isCompact_Icc)]
    · congr 1
      rw [integral_Icc_eq_integral_Ioc, ← intervalIntegral.integral_of_le (by linarith)]
      simp only [hg]
      rw [intervalIntegral.integral_sub, integral_inv_of_pos hm hm1, intervalIntegral.integral_const]
      · have e : (m + 1) / m = 1 + m⁻¹ := by field_simp
        rw [e, smul_eq_mul]
        ring
      · apply ContinuousOn.intervalIntegrable
        apply continuousOn_inv₀.mono
        intro x hx
        rw [uIcc_of_le (by linarith)] at hx
        exact ne_of_gt (lt_of_lt_of_le hm hx.1)
      · exact intervalIntegrable_const
    · filter_upwards [ae_restrict_mem measurableSet_Icc] with y hy
      have hypos : 0 < y := lt_of_lt_of_le hm hy.1
      have := inv_anti₀ hypos hy.2
      simp only [Pi.zero_apply, hg]
      linarith
  have hlog : (m + 1)⁻¹ ≤ Real.log (1 + m⁻¹) := by
    have h := Real.one_sub_inv_le_log_of_pos (show (0 : ℝ) < 1 + m⁻¹ by positivity)
    have e : 1 - (1 + m⁻¹)⁻¹ = (m + 1)⁻¹ := by field_simp; ring
    linarith
  calc ∫⁻ y in Ici m, ENNReal.ofReal (f y * y⁻¹)
      ≤ ∫⁻ y in Ici m, ((Icc m (m + 1)).indicator (fun y => ENNReal.ofReal (g y)) y
          + ENNReal.ofReal ((m + 1)⁻¹) * ENNReal.ofReal (f y)) := setLIntegral_mono' measurableSet_Ici hpt
    _ = (∫⁻ y in Ici m, (Icc m (m + 1)).indicator (fun y => ENNReal.ofReal (g y)) y)
          + ENNReal.ofReal ((m + 1)⁻¹) * ∫⁻ y in Ici m, ENNReal.ofReal (f y) := by
        have hmf : Measurable fun y => ENNReal.ofReal (f y) := ENNReal.measurable_ofReal.comp hf
        rw [lintegral_add_left hmeas_ind, lintegral_const_mul _ hmf]
    _ ≤ ENNReal.ofReal (Real.log (1 + m⁻¹) - (m + 1)⁻¹) + ENNReal.ofReal ((m + 1)⁻¹) * 1 := by
        rw [hIcc]
        gcongr
    _ = ENNReal.ofReal (Real.log (1 + m⁻¹)) := by
        rw [mul_one, ← ENNReal.ofReal_add (by linarith) (inv_nonneg.2 hm1.le)]
        congr 1
        ring

/-- `e^{2τ} ≥ 2√2` for `τ ≥ (3/4) log 2`. -/
theorem exp_two_mul_ge (τ : ℝ) (hτ : 3 / 4 * Real.log 2 ≤ τ) : 2 * √2 ≤ Real.exp (2 * τ) := by
  have h1 : Real.log (2 * √2) = 3 / 2 * Real.log 2 := by
    rw [Real.log_mul (by norm_num) (by positivity), Real.log_sqrt (by norm_num)]
    ring
  have h2 : Real.log (2 * √2) ≤ 2 * τ := by
    rw [h1]
    linarith
  calc 2 * √2 = Real.exp (Real.log (2 * √2)) := (Real.exp_log (by positivity)).symm
    _ ≤ Real.exp (2 * τ) := Real.exp_le_exp.2 h2

/-- For `p > 0`, `|p'| ≤ √2 p` and `τ ≥ (3/4) log 2`: `|p' e^{-τ}| ≤ p e^τ / 2`. -/
theorem tail_small (p p' τ : ℝ) (hp : 0 < p) (hp' : |p'| ≤ √2 * p) (hτ : 3 / 4 * Real.log 2 ≤ τ) :
    |p' * Real.exp (-τ)| ≤ 1 / 2 * (p * Real.exp τ) := by
  have he := exp_two_mul_ge τ hτ
  have hE : 0 < Real.exp τ := Real.exp_pos τ
  have h2 : Real.exp (2 * τ) = Real.exp τ * Real.exp τ := by rw [two_mul, Real.exp_add]
  rw [h2] at he
  rw [abs_mul, abs_of_pos (Real.exp_pos _), Real.exp_neg, ← div_eq_mul_inv, div_le_iff₀ hE]
  have hs : 0 ≤ √2 := Real.sqrt_nonneg 2
  nlinarith [he, hp, hp']

/-- **The curve change of variables.** For `y(τ) = p e^τ + p' e^{-τ}` with `p > 0`, `|p'| ≤ √2 p`, and
`T ≥ (3/4) log 2`: `∫_T^∞ g(y(τ)) dτ ≤ 3 ∫_{[m,∞)} g(y) y⁻¹ dy` with `m = p e^T / 2`. -/
theorem curve_tail (p p' T : ℝ) (hp : 0 < p) (hp' : |p'| ≤ √2 * p) (hT : 3 / 4 * Real.log 2 ≤ T)
    (g : ℝ → ℝ) (hg : Measurable g) (hg0 : ∀ y, 0 ≤ g y) :
    ∫⁻ τ in Ici T, ENNReal.ofReal (g (p * Real.exp τ + p' * Real.exp (-τ)))
      ≤ 3 * ∫⁻ y in Ici (p * Real.exp T / 2), ENNReal.ofReal (g y * y⁻¹) := by
  have hderiv : ∀ τ, HasDerivAt (fun x => p * Real.exp x + p' * Real.exp (-x))
      (p * Real.exp τ - p' * Real.exp (-τ)) τ := by
    intro τ
    have h1 := (Real.hasDerivAt_exp τ).const_mul p
    have h2 := (((hasDerivAt_id' τ).neg).exp).const_mul p'
    convert h1.add h2 using 1
    simp only [Pi.neg_apply]
    ring
  have hbnd : ∀ τ ∈ Ici T, p * Real.exp τ / 2 ≤ p * Real.exp τ + p' * Real.exp (-τ) ∧
      (p * Real.exp τ + p' * Real.exp (-τ)) / 3 ≤ p * Real.exp τ - p' * Real.exp (-τ) := by
    intro τ hτ
    have hτ' : 3 / 4 * Real.log 2 ≤ τ := le_trans hT hτ
    have hab := abs_le.1 (tail_small p p' τ hp hp' hτ')
    constructor <;> linarith [hab.1, hab.2]
  have hypos : ∀ τ ∈ Ici T, 0 < p * Real.exp τ + p' * Real.exp (-τ) := by
    intro τ hτ
    have h := (hbnd τ hτ).1
    have hE := Real.exp_pos τ
    have : 0 < p * Real.exp τ / 2 := by positivity
    linarith
  have hy'pos : ∀ τ ∈ Ici T, 0 < p * Real.exp τ - p' * Real.exp (-τ) := by
    intro τ hτ
    have h := (hbnd τ hτ).2
    have := hypos τ hτ
    linarith
  have hmono : StrictMonoOn (fun x => p * Real.exp x + p' * Real.exp (-x)) (Ici T) := by
    apply strictMonoOn_of_deriv_pos (convex_Ici T) (fun τ _ => (hderiv τ).continuousAt.continuousWithinAt)
    intro τ hτ
    rw [interior_Ici] at hτ
    rw [(hderiv τ).deriv]
    exact hy'pos τ (mem_Ici.2 (le_of_lt (mem_Ioi.1 hτ)))
  have hcov := lintegral_image_eq_lintegral_abs_deriv_mul measurableSet_Ici
    (fun τ _ => (hderiv τ).hasDerivWithinAt) hmono.injOn (fun z => ENNReal.ofReal (3 * (g z * z⁻¹)))
  have himg : (fun x => p * Real.exp x + p' * Real.exp (-x)) '' Ici T ⊆ Ici (p * Real.exp T / 2) := by
    rintro _ ⟨τ, hτ, rfl⟩
    have h1 := (hbnd τ hτ).1
    have h2 : p * Real.exp T / 2 ≤ p * Real.exp τ / 2 := by
      have := Real.exp_le_exp.2 (show T ≤ τ from hτ)
      nlinarith
    exact le_trans h2 h1
  have hmeas3 : Measurable fun z : ℝ => ENNReal.ofReal (g z * z⁻¹) :=
    ENNReal.measurable_ofReal.comp (hg.mul measurable_inv)
  calc ∫⁻ τ in Ici T, ENNReal.ofReal (g (p * Real.exp τ + p' * Real.exp (-τ)))
      ≤ ∫⁻ τ in Ici T, ENNReal.ofReal |p * Real.exp τ - p' * Real.exp (-τ)|
          * ENNReal.ofReal (3 * (g (p * Real.exp τ + p' * Real.exp (-τ))
            * (p * Real.exp τ + p' * Real.exp (-τ))⁻¹)) := by
        apply setLIntegral_mono' measurableSet_Ici
        intro τ hτ
        rw [← ENNReal.ofReal_mul (abs_nonneg _)]
        apply ENNReal.ofReal_le_ofReal
        have h := (hbnd τ hτ).2
        have hyp := hypos τ hτ
        rw [abs_of_pos (hy'pos τ hτ)]
        have h1 : 1 ≤ (p * Real.exp τ - p' * Real.exp (-τ)) * 3 * (p * Real.exp τ + p' * Real.exp (-τ))⁻¹ := by
          rw [le_mul_inv_iff₀ hyp]
          linarith
        calc g (p * Real.exp τ + p' * Real.exp (-τ))
            = 1 * g (p * Real.exp τ + p' * Real.exp (-τ)) := (one_mul _).symm
          _ ≤ ((p * Real.exp τ - p' * Real.exp (-τ)) * 3 * (p * Real.exp τ + p' * Real.exp (-τ))⁻¹)
                * g (p * Real.exp τ + p' * Real.exp (-τ)) := mul_le_mul_of_nonneg_right h1 (hg0 _)
          _ = (p * Real.exp τ - p' * Real.exp (-τ)) * (3 * (g (p * Real.exp τ + p' * Real.exp (-τ))
                * (p * Real.exp τ + p' * Real.exp (-τ))⁻¹)) := by ring
    _ = ∫⁻ z in (fun x => p * Real.exp x + p' * Real.exp (-x)) '' Ici T, ENNReal.ofReal (3 * (g z * z⁻¹)) :=
        hcov.symm
    _ ≤ ∫⁻ z in Ici (p * Real.exp T / 2), ENNReal.ofReal (3 * (g z * z⁻¹)) := lintegral_mono_set himg
    _ = 3 * ∫⁻ z in Ici (p * Real.exp T / 2), ENNReal.ofReal (g z * z⁻¹) := by
        rw [← lintegral_const_mul _ hmeas3]
        apply setLIntegral_congr_fun measurableSet_Ici
        intro z _
        show ENNReal.ofReal (3 * (g z * z⁻¹)) = 3 * ENNReal.ofReal (g z * z⁻¹)
        rw [ENNReal.ofReal_mul (by norm_num), ENNReal.ofReal_ofNat]

/-- `∫ g(-x) dx = ∫ g(x) dx`. -/
theorem lintegral_comp_neg' (g : ℝ → ℝ≥0∞) : ∫⁻ x, g (-x) = ∫⁻ x, g x := by
  have h := lintegral_image_eq_lintegral_abs_deriv_mul MeasurableSet.univ
    (fun x _ => (hasDerivAt_neg x).hasDerivWithinAt) neg_injective.injOn g
  rw [Set.image_neg_eq_neg, Set.neg_univ, Measure.restrict_univ] at h
  simp only [abs_neg, abs_one, ENNReal.ofReal_one, one_mul] at h
  exact h.symm

/-- **One tail.** For `f` with values in `[0, 1]` and `∫ f ≤ 1`, `p ≠ 0`, `|p'| ≤ √2 |p|`, and
`T = max((3/4) log 2, log(2/|p|))`: `∫_T^∞ f(p e^τ + p' e^{-τ}) dτ ≤ 3 log 2`. -/
theorem tail_log2 (f : ℝ → ℝ) (hf : Measurable f) (hf0 : ∀ y, 0 ≤ f y) (hf1 : ∀ y, f y ≤ 1)
    (hint : ∫⁻ y, ENNReal.ofReal (f y) ≤ 1) (p p' : ℝ) (hp : p ≠ 0) (hp' : |p'| ≤ √2 * |p|) :
    ∫⁻ τ in Ici (max (3 / 4 * Real.log 2) (Real.log (2 / |p|))),
        ENNReal.ofReal (f (p * Real.exp τ + p' * Real.exp (-τ)))
      ≤ ENNReal.ofReal (3 * Real.log 2) := by
  set T := max (3 / 4 * Real.log 2) (Real.log (2 / |p|)) with hTdef
  have hT1 : 3 / 4 * Real.log 2 ≤ T := le_max_left _ _
  have hT2 : Real.log (2 / |p|) ≤ T := le_max_right _ _
  have hap : 0 < |p| := abs_pos.2 hp
  have hm1 : 1 ≤ |p| * Real.exp T / 2 := by
    have h := Real.exp_le_exp.2 hT2
    rw [Real.exp_log (by positivity)] at h
    rw [le_div_iff₀ (by norm_num : (0 : ℝ) < 2)]
    calc 1 * 2 = |p| * (2 / |p|) := by field_simp
      _ ≤ |p| * Real.exp T := mul_le_mul_of_nonneg_left h hap.le
  -- the bathtub bound with `m ≥ 1`
  have hlog : ∀ m : ℝ, 1 ≤ m → Real.log (1 + m⁻¹) ≤ Real.log 2 := by
    intro m hm
    apply Real.log_le_log (by positivity)
    have : m⁻¹ ≤ 1 := inv_le_one_of_one_le₀ hm
    linarith
  -- both signs of `p`
  have key : ∀ (h : ℝ → ℝ), Measurable h → (∀ y, 0 ≤ h y) → (∀ y, h y ≤ 1) → ∫⁻ y, ENNReal.ofReal (h y) ≤ 1 →
      ∀ q q' : ℝ, 0 < q → |q'| ≤ √2 * q → 1 ≤ q * Real.exp T / 2 →
      ∫⁻ τ in Ici T, ENNReal.ofReal (h (q * Real.exp τ + q' * Real.exp (-τ))) ≤ ENNReal.ofReal (3 * Real.log 2) := by
    intro h hh hh0 hh1 hhint q q' hq hq' hm
    have hm0 : 0 < q * Real.exp T / 2 := by linarith
    have hint' : ∫⁻ y in Ici (q * Real.exp T / 2), ENNReal.ofReal (h y) ≤ 1 :=
      le_trans (setLIntegral_le_lintegral _ _) hhint
    calc ∫⁻ τ in Ici T, ENNReal.ofReal (h (q * Real.exp τ + q' * Real.exp (-τ)))
        ≤ 3 * ∫⁻ y in Ici (q * Real.exp T / 2), ENNReal.ofReal (h y * y⁻¹) :=
          curve_tail q q' T hq hq' hT1 h hh hh0
      _ ≤ 3 * ENNReal.ofReal (Real.log (1 + (q * Real.exp T / 2)⁻¹)) := by
          gcongr
          exact bathtub_inv h hh hh0 hh1 _ hm0 hint'
      _ ≤ 3 * ENNReal.ofReal (Real.log 2) :=
          mul_le_mul_left' (ENNReal.ofReal_le_ofReal (hlog _ hm)) 3
      _ = ENNReal.ofReal (3 * Real.log 2) := by
          rw [ENNReal.ofReal_mul (by norm_num), ENNReal.ofReal_ofNat]
  rcases lt_or_gt_of_ne hp with hneg | hpos
  · -- `p < 0`: reflect
    have hfm : Measurable fun y => f (-y) := hf.comp measurable_neg
    have hint' : ∫⁻ y, ENNReal.ofReal (f (-y)) ≤ 1 := by
      rw [lintegral_comp_neg' (fun y => ENNReal.ofReal (f y))]
      exact hint
    have habs : |p| = -p := abs_of_neg hneg
    have h := key (fun y => f (-y)) hfm (fun y => hf0 _) (fun y => hf1 _) hint' (-p) (-p') (by linarith)
      (by rw [abs_neg, ← habs]; exact hp') (by rw [← habs]; exact hm1)
    have e : ∀ τ, f (-(-p * Real.exp τ + -p' * Real.exp (-τ))) = f (p * Real.exp τ + p' * Real.exp (-τ)) := by
      intro τ
      congr 1
      ring
    simp only [e] at h
    exact h
  · have habs : |p| = p := abs_of_pos hpos
    rw [habs] at hp' hm1
    exact key f hf hf0 hf1 hint p p' hpos hp' hm1


/-- The cutoff `max((3/4) log 2, log(2/|p|))` is at most `(3/4) log 2 + (1/2) log⁺(8/ρ²)` when `p² ≥ ρ²/2`. -/
theorem cutoff_le (p ρ : ℝ) (hρ : 0 < ρ) (hp : ρ ^ 2 / 2 ≤ p ^ 2) :
    max (3 / 4 * Real.log 2) (Real.log (2 / |p|)) ≤ 3 / 4 * Real.log 2 + 1 / 2 * max 0 (Real.log (8 / ρ ^ 2)) := by
  have hρp : ρ ≤ √2 * |p| := by
    refine (pow_le_pow_iff_left₀ hρ.le (by positivity) two_ne_zero).1 ?_
    rw [mul_pow, Real.sq_sqrt (by norm_num), sq_abs]
    linarith
  have hp0 : 0 < |p| := by
    have hs : 0 < √2 := by positivity
    by_contra h
    push_neg at h
    have : √2 * |p| ≤ 0 := mul_nonpos_of_nonneg_of_nonpos hs.le h
    linarith
  have h1 : 2 / |p| ≤ 2 * √2 / ρ := by
    rw [div_le_div_iff₀ hp0 hρ]
    linarith
  have h2 : Real.log (2 * √2 / ρ) = 1 / 2 * Real.log (8 / ρ ^ 2) := by
    have e : 8 / ρ ^ 2 = (2 * √2 / ρ) ^ 2 := by
      rw [div_pow, mul_pow, Real.sq_sqrt (by norm_num)]
      norm_num
    rw [e, Real.log_pow]
    push_cast
    ring
  have hlog : Real.log (2 / |p|) ≤ 1 / 2 * max 0 (Real.log (8 / ρ ^ 2)) := by
    calc Real.log (2 / |p|) ≤ Real.log (2 * √2 / ρ) := Real.log_le_log (by positivity) h1
      _ = 1 / 2 * Real.log (8 / ρ ^ 2) := h2
      _ ≤ 1 / 2 * max 0 (Real.log (8 / ρ ^ 2)) := by
          apply mul_le_mul_of_nonneg_left (le_max_right _ _) (by norm_num)
  have hl2 : 0 ≤ Real.log 2 := Real.log_nonneg (by norm_num)
  have hnn : 0 ≤ 1 / 2 * max 0 (Real.log (8 / ρ ^ 2)) :=
    mul_nonneg (by norm_num) (le_max_left _ _)
  apply max_le
  · linarith
  · linarith

/-- **The forward tail of a branch.** With `|u| = |v| = ρ`, there is a cutoff `T` between `(3/4) log 2` and
`(3/4) log 2 + (1/2) log⁺(8/ρ²)` beyond which `∫ f₁(w₁) f₂(w₂) dτ ≤ 3 log 2`, where `w_j = u_j e^τ + v_j e^{-τ}`. -/
theorem forward_tail (f₁ f₂ : ℝ → ℝ) (hf₁ : Measurable f₁) (hf₂ : Measurable f₂)
    (h0₁ : ∀ y, 0 ≤ f₁ y) (h1₁ : ∀ y, f₁ y ≤ 1) (h0₂ : ∀ y, 0 ≤ f₂ y) (h1₂ : ∀ y, f₂ y ≤ 1)
    (hi₁ : ∫⁻ y, ENNReal.ofReal (f₁ y) ≤ 1) (hi₂ : ∫⁻ y, ENNReal.ofReal (f₂ y) ≤ 1)
    (u₁ u₂ v₁ v₂ ρ : ℝ) (hρ : 0 < ρ) (hu : u₁ ^ 2 + u₂ ^ 2 = ρ ^ 2) (hv : v₁ ^ 2 + v₂ ^ 2 = ρ ^ 2) :
    ∃ T : ℝ, 3 / 4 * Real.log 2 ≤ T ∧ T ≤ 3 / 4 * Real.log 2 + 1 / 2 * max 0 (Real.log (8 / ρ ^ 2)) ∧
      ∫⁻ τ in Ici T, ENNReal.ofReal (f₁ (u₁ * Real.exp τ + v₁ * Real.exp (-τ))
        * f₂ (u₂ * Real.exp τ + v₂ * Real.exp (-τ))) ≤ ENNReal.ofReal (3 * Real.log 2) := by
  -- the two coordinates play symmetric roles
  have core : ∀ (g h : ℝ → ℝ), Measurable g → (∀ y, 0 ≤ g y) → (∀ y, g y ≤ 1) →
      ∫⁻ y, ENNReal.ofReal (g y) ≤ 1 → (∀ y, 0 ≤ h y) → (∀ y, h y ≤ 1) →
      ∀ p p' q q' : ℝ, ρ ^ 2 / 2 ≤ p ^ 2 → p' ^ 2 ≤ ρ ^ 2 →
      ∃ T : ℝ, 3 / 4 * Real.log 2 ≤ T ∧ T ≤ 3 / 4 * Real.log 2 + 1 / 2 * max 0 (Real.log (8 / ρ ^ 2)) ∧
        ∫⁻ τ in Ici T, ENNReal.ofReal (g (p * Real.exp τ + p' * Real.exp (-τ))
          * h (q * Real.exp τ + q' * Real.exp (-τ))) ≤ ENNReal.ofReal (3 * Real.log 2) := by
    intro g h hg hg0 hg1 hgi hh0 hh1 p p' q q' hp hp'
    have hp0 : p ≠ 0 := by
      intro h0
      rw [h0] at hp
      have : 0 < ρ ^ 2 / 2 := by positivity
      norm_num at hp
      linarith
    have hρp : ρ ≤ √2 * |p| := by
      refine (pow_le_pow_iff_left₀ hρ.le (by positivity) two_ne_zero).1 ?_
      rw [mul_pow, Real.sq_sqrt (by norm_num), sq_abs]
      linarith
    have hp'ρ : |p'| ≤ ρ := abs_le_of_sq_le_sq hp' hρ.le
    refine ⟨max (3 / 4 * Real.log 2) (Real.log (2 / |p|)), le_max_left _ _, cutoff_le p ρ hρ hp, ?_⟩
    calc ∫⁻ τ in Ici (max (3 / 4 * Real.log 2) (Real.log (2 / |p|))),
          ENNReal.ofReal (g (p * Real.exp τ + p' * Real.exp (-τ)) * h (q * Real.exp τ + q' * Real.exp (-τ)))
        ≤ ∫⁻ τ in Ici (max (3 / 4 * Real.log 2) (Real.log (2 / |p|))),
            ENNReal.ofReal (g (p * Real.exp τ + p' * Real.exp (-τ))) := by
          apply lintegral_mono
          intro τ
          apply ENNReal.ofReal_le_ofReal
          exact mul_le_of_le_one_right (hg0 _) (hh1 _)
      _ ≤ ENNReal.ofReal (3 * Real.log 2) := tail_log2 g hg hg0 hg1 hgi p p' hp0 (le_trans hp'ρ hρp)
  by_cases h1 : ρ ^ 2 / 2 ≤ u₁ ^ 2
  · have hv1 : v₁ ^ 2 ≤ ρ ^ 2 := by nlinarith [sq_nonneg v₂]
    exact core f₁ f₂ hf₁ h0₁ h1₁ hi₁ h0₂ h1₂ u₁ v₁ u₂ v₂ h1 hv1
  · push_neg at h1
    have h2 : ρ ^ 2 / 2 ≤ u₂ ^ 2 := by nlinarith
    have hv2 : v₂ ^ 2 ≤ ρ ^ 2 := by nlinarith [sq_nonneg v₁]
    obtain ⟨T, hT1, hT2, hT⟩ := core f₂ f₁ hf₂ h0₂ h1₂ hi₂ h0₁ h1₁ u₂ v₂ u₁ v₁ h2 hv2
    refine ⟨T, hT1, hT2, ?_⟩
    have e : ∀ τ, f₁ (u₁ * Real.exp τ + v₁ * Real.exp (-τ)) * f₂ (u₂ * Real.exp τ + v₂ * Real.exp (-τ))
        = f₂ (u₂ * Real.exp τ + v₂ * Real.exp (-τ)) * f₁ (u₁ * Real.exp τ + v₁ * Real.exp (-τ)) :=
      fun τ => mul_comm _ _
    simp only [e]
    exact hT

/-- `∫_{(-∞, -a]} g = ∫_{[a, ∞)} g(-x) dx`. -/
theorem setLIntegral_Iic_neg (g : ℝ → ℝ≥0∞) (a : ℝ) :
    ∫⁻ x in Iic (-a), g x = ∫⁻ x in Ici a, g (-x) := by
  rw [← lintegral_indicator measurableSet_Iic, ← lintegral_indicator measurableSet_Ici,
    ← lintegral_comp_neg' ((Iic (-a)).indicator g)]
  apply lintegral_congr
  intro x
  by_cases h : a ≤ x
  · have h' : -x ∈ Iic (-a) := by simp only [mem_Iic]; linarith
    rw [indicator_of_mem h', indicator_of_mem (show x ∈ Ici a from h)]
  · have h' : -x ∉ Iic (-a) := by simp only [mem_Iic]; push_neg at h ⊢; linarith
    rw [indicator_of_notMem h', indicator_of_notMem (show x ∉ Ici a from h)]

/-- **One branch.** For densities `0 ≤ f_j ≤ 1` with `∫ f_j ≤ 1`, and `u, v ∈ ℝ²` with `|u| = |v| = ρ > 0`,
`∫_ℝ f₁(u₁ e^τ + v₁ e^{-τ}) f₂(u₂ e^τ + v₂ e^{-τ}) dτ ≤ 6 + log⁺(8/ρ²)`: two tails of `3 log 2` each, a middle
interval of length at most `(3/2) log 2 + log⁺(8/ρ²)`, and `(15/2) log 2 < 6`. -/
theorem branch_bound (f₁ f₂ : ℝ → ℝ) (hf₁ : Measurable f₁) (hf₂ : Measurable f₂)
    (h0₁ : ∀ y, 0 ≤ f₁ y) (h1₁ : ∀ y, f₁ y ≤ 1) (h0₂ : ∀ y, 0 ≤ f₂ y) (h1₂ : ∀ y, f₂ y ≤ 1)
    (hi₁ : ∫⁻ y, ENNReal.ofReal (f₁ y) ≤ 1) (hi₂ : ∫⁻ y, ENNReal.ofReal (f₂ y) ≤ 1)
    (u₁ u₂ v₁ v₂ ρ : ℝ) (hρ : 0 < ρ) (hu : u₁ ^ 2 + u₂ ^ 2 = ρ ^ 2) (hv : v₁ ^ 2 + v₂ ^ 2 = ρ ^ 2) :
    ∫⁻ τ, ENNReal.ofReal (f₁ (u₁ * Real.exp τ + v₁ * Real.exp (-τ)) * f₂ (u₂ * Real.exp τ + v₂ * Real.exp (-τ)))
      ≤ ENNReal.ofReal (6 + max 0 (Real.log (8 / ρ ^ 2))) := by
  set F : ℝ → ℝ≥0∞ := fun τ => ENNReal.ofReal (f₁ (u₁ * Real.exp τ + v₁ * Real.exp (-τ))
    * f₂ (u₂ * Real.exp τ + v₂ * Real.exp (-τ))) with hF
  obtain ⟨T, hT1, hT2, hTf⟩ := forward_tail f₁ f₂ hf₁ hf₂ h0₁ h1₁ h0₂ h1₂ hi₁ hi₂ u₁ u₂ v₁ v₂ ρ hρ hu hv
  obtain ⟨T', hT'1, hT'2, hT'f⟩ := forward_tail f₁ f₂ hf₁ hf₂ h0₁ h1₁ h0₂ h1₂ hi₁ hi₂ v₁ v₂ u₁ u₂ ρ hρ hv hu
  have hl2 : 0 < Real.log 2 := Real.log_pos (by norm_num)
  have hTpos : 0 < T := by linarith
  have hT'pos : 0 < T' := by linarith
  -- the backward tail
  have hback : ∫⁻ τ in Iic (-T'), F τ ≤ ENNReal.ofReal (3 * Real.log 2) := by
    rw [setLIntegral_Iic_neg]
    have e : ∀ τ, F (-τ) = ENNReal.ofReal (f₁ (v₁ * Real.exp τ + u₁ * Real.exp (-τ))
        * f₂ (v₂ * Real.exp τ + u₂ * Real.exp (-τ))) := by
      intro τ
      simp only [hF, neg_neg]
      congr 2 <;> ring_nf
    simp only [e]
    exact hT'f
  -- the middle
  have hmid : ∫⁻ τ in Ioo (-T') T, F τ ≤ ENNReal.ofReal (T + T') := by
    calc ∫⁻ τ in Ioo (-T') T, F τ ≤ ∫⁻ τ in Ioo (-T') T, 1 := by
          apply lintegral_mono
          intro τ
          simp only [hF]
          rw [← ENNReal.ofReal_one]
          apply ENNReal.ofReal_le_ofReal
          exact mul_le_one₀ (h1₁ _) (h0₂ _) (h1₂ _)
      _ = ENNReal.ofReal (T + T') := by
          rw [setLIntegral_one, Real.volume_Ioo]
          congr 1
          ring
  -- the cover of ℝ
  have hcover : (univ : Set ℝ) ⊆ (Iic (-T') ∪ Ioo (-T') T) ∪ Ici T := by
    intro x _
    by_cases h1 : x ≤ -T'
    · exact Or.inl (Or.inl h1)
    · by_cases h2 : T ≤ x
      · exact Or.inr h2
      · push_neg at h1 h2
        exact Or.inl (Or.inr ⟨h1, h2⟩)
  have htot : ∫⁻ τ, F τ ≤ ENNReal.ofReal (3 * Real.log 2) + ENNReal.ofReal (T + T')
      + ENNReal.ofReal (3 * Real.log 2) := by
    calc ∫⁻ τ, F τ = ∫⁻ τ in univ, F τ := by rw [Measure.restrict_univ]
      _ ≤ ∫⁻ τ in (Iic (-T') ∪ Ioo (-T') T) ∪ Ici T, F τ := lintegral_mono_set hcover
      _ ≤ (∫⁻ τ in Iic (-T') ∪ Ioo (-T') T, F τ) + ∫⁻ τ in Ici T, F τ := lintegral_union_le _ _ _
      _ ≤ ((∫⁻ τ in Iic (-T'), F τ) + ∫⁻ τ in Ioo (-T') T, F τ) + ∫⁻ τ in Ici T, F τ := by
          gcongr
          exact lintegral_union_le _ _ _
      _ ≤ ENNReal.ofReal (3 * Real.log 2) + ENNReal.ofReal (T + T') + ENNReal.ofReal (3 * Real.log 2) := by
          gcongr
  have hlt : Real.log 2 < 0.6931471808 := Real.log_two_lt_d9
  have hsum : 3 * Real.log 2 + (T + T') + 3 * Real.log 2 ≤ 6 + max 0 (Real.log (8 / ρ ^ 2)) := by
    linarith
  calc ∫⁻ τ, F τ ≤ ENNReal.ofReal (3 * Real.log 2) + ENNReal.ofReal (T + T') + ENNReal.ofReal (3 * Real.log 2) := htot
    _ = ENNReal.ofReal (3 * Real.log 2 + (T + T') + 3 * Real.log 2) := by
        rw [← ENNReal.ofReal_add (by positivity) (by positivity),
          ← ENNReal.ofReal_add (by positivity) (by positivity)]
    _ ≤ ENNReal.ofReal (6 + max 0 (Real.log (8 / ρ ^ 2))) := ENNReal.ofReal_le_ofReal hsum


/-- **One branch, unequal norms.** The substitution `τ ↦ τ + t₀` with `e^{2t₀} = |v|/|u|` equalizes the two norms at
`√(|u| |v|)`, so the bound is `6 + log⁺(8/(|u| |v|))`. -/
theorem branch_bound_gen (f₁ f₂ : ℝ → ℝ) (hf₁ : Measurable f₁) (hf₂ : Measurable f₂)
    (h0₁ : ∀ y, 0 ≤ f₁ y) (h1₁ : ∀ y, f₁ y ≤ 1) (h0₂ : ∀ y, 0 ≤ f₂ y) (h1₂ : ∀ y, f₂ y ≤ 1)
    (hi₁ : ∫⁻ y, ENNReal.ofReal (f₁ y) ≤ 1) (hi₂ : ∫⁻ y, ENNReal.ofReal (f₂ y) ≤ 1)
    (u₁ u₂ v₁ v₂ : ℝ) (hu : 0 < u₁ ^ 2 + u₂ ^ 2) (hv : 0 < v₁ ^ 2 + v₂ ^ 2) :
    ∫⁻ τ, ENNReal.ofReal (f₁ (u₁ * Real.exp τ + v₁ * Real.exp (-τ)) * f₂ (u₂ * Real.exp τ + v₂ * Real.exp (-τ)))
      ≤ ENNReal.ofReal (6 + max 0 (Real.log (8 / (√(u₁ ^ 2 + u₂ ^ 2) * √(v₁ ^ 2 + v₂ ^ 2))))) := by
  set r₁ := √(u₁ ^ 2 + u₂ ^ 2) with hr₁def
  set r₂ := √(v₁ ^ 2 + v₂ ^ 2) with hr₂def
  have hr₁ : 0 < r₁ := Real.sqrt_pos.2 hu
  have hr₂ : 0 < r₂ := Real.sqrt_pos.2 hv
  have hr₁sq : r₁ ^ 2 = u₁ ^ 2 + u₂ ^ 2 := Real.sq_sqrt hu.le
  have hr₂sq : r₂ ^ 2 = v₁ ^ 2 + v₂ ^ 2 := Real.sq_sqrt hv.le
  set t₀ := Real.log (r₂ / r₁) / 2 with ht₀
  have he : Real.exp t₀ * Real.exp t₀ = r₂ / r₁ := by
    rw [← Real.exp_add, show t₀ + t₀ = Real.log (r₂ / r₁) by rw [ht₀]; ring, Real.exp_log (div_pos hr₂ hr₁)]
  have hen : Real.exp (-t₀) * Real.exp (-t₀) = r₁ / r₂ := by
    rw [Real.exp_neg, ← mul_inv, he, inv_div]
  set ρ := √(r₁ * r₂) with hρdef
  have hρ : 0 < ρ := Real.sqrt_pos.2 (mul_pos hr₁ hr₂)
  have hρsq : ρ ^ 2 = r₁ * r₂ := Real.sq_sqrt (mul_pos hr₁ hr₂).le
  have hU : (u₁ * Real.exp t₀) ^ 2 + (u₂ * Real.exp t₀) ^ 2 = ρ ^ 2 := by
    rw [hρsq]
    have e : (u₁ * Real.exp t₀) ^ 2 + (u₂ * Real.exp t₀) ^ 2 = (u₁ ^ 2 + u₂ ^ 2) * (Real.exp t₀ * Real.exp t₀) := by
      ring
    rw [e, he, ← hr₁sq]
    field_simp
  have hV : (v₁ * Real.exp (-t₀)) ^ 2 + (v₂ * Real.exp (-t₀)) ^ 2 = ρ ^ 2 := by
    rw [hρsq]
    have e : (v₁ * Real.exp (-t₀)) ^ 2 + (v₂ * Real.exp (-t₀)) ^ 2
        = (v₁ ^ 2 + v₂ ^ 2) * (Real.exp (-t₀) * Real.exp (-t₀)) := by ring
    rw [e, hen, ← hr₂sq]
    field_simp
  have hshift : ∫⁻ τ, ENNReal.ofReal (f₁ (u₁ * Real.exp τ + v₁ * Real.exp (-τ))
        * f₂ (u₂ * Real.exp τ + v₂ * Real.exp (-τ)))
      = ∫⁻ τ, ENNReal.ofReal (f₁ ((u₁ * Real.exp t₀) * Real.exp τ + (v₁ * Real.exp (-t₀)) * Real.exp (-τ))
        * f₂ ((u₂ * Real.exp t₀) * Real.exp τ + (v₂ * Real.exp (-t₀)) * Real.exp (-τ))) := by
    rw [← lintegral_add_right_eq_self (μ := volume) _ t₀]
    apply lintegral_congr
    intro τ
    have e1 : ∀ x : ℝ, x * Real.exp (τ + t₀) = x * Real.exp t₀ * Real.exp τ := by
      intro x
      rw [Real.exp_add]
      ring
    have e2 : ∀ x : ℝ, x * Real.exp (-(τ + t₀)) = x * Real.exp (-t₀) * Real.exp (-τ) := by
      intro x
      rw [show -(τ + t₀) = -τ + -t₀ by ring, Real.exp_add]
      ring
    simp only [e1, e2]
  rw [hshift]
  have hb := branch_bound f₁ f₂ hf₁ hf₂ h0₁ h1₁ h0₂ h1₂ hi₁ hi₂ (u₁ * Real.exp t₀) (u₂ * Real.exp t₀)
    (v₁ * Real.exp (-t₀)) (v₂ * Real.exp (-t₀)) ρ hρ hU hV
  rw [hρsq] at hb
  exact hb

/-- The quadratic form `a w₁² + 2b w₁w₂ + c w₂²`. -/
def Qf (a b c : ℝ) (w : ℝ × ℝ) : ℝ := a * w.1 ^ 2 + 2 * b * w.1 * w.2 + c * w.2 ^ 2

/-- Its polar bilinear form. -/
def Bf (a b c : ℝ) (w z : ℝ × ℝ) : ℝ := a * w.1 * z.1 + b * (w.1 * z.2 + w.2 * z.1) + c * w.2 * z.2

/-- **Null coordinates.** For an indefinite form (`D = b² - ac > 0`) there are `n₁, n₂` with `Q(n₁) = Q(n₂) = 0` and
`2 B(n₁, n₂) = 1`, so that `Q(s n₁ + t n₂) = st`. -/
theorem null_pair (a b c : ℝ) (hD : 0 < b ^ 2 - a * c) :
    ∃ n₁ n₂ : ℝ × ℝ, Qf a b c n₁ = 0 ∧ Qf a b c n₂ = 0 ∧ 2 * Bf a b c n₁ n₂ = 1 := by
  by_cases ha : a = 0
  · have hb : b ≠ 0 := by
      intro h
      rw [ha, h] at hD
      norm_num at hD
    refine ⟨(1, 0), (-c / (4 * b ^ 2), 1 / (2 * b)), ?_, ?_, ?_⟩
    · simp only [Qf, ha]
      ring
    · simp only [Qf, ha]
      field_simp
      ring
    · simp only [Bf, ha]
      field_simp
      ring
  · set s := √(b ^ 2 - a * c) with hs
    have hs2 : s ^ 2 = b ^ 2 - a * c := Real.sq_sqrt hD.le
    have hs0 : 0 < s := Real.sqrt_pos.2 hD
    have hk : -4 * a * (b ^ 2 - a * c) ≠ 0 := by
      apply mul_ne_zero (mul_ne_zero (by norm_num) ha) hD.ne'
    refine ⟨(-b + s, a), ((-b - s) / (-4 * a * (b ^ 2 - a * c)), a / (-4 * a * (b ^ 2 - a * c))), ?_, ?_, ?_⟩
    · simp only [Qf]
      linear_combination a * hs2
    · simp only [Qf]
      field_simp
      nlinarith [hs2]
    · simp only [Bf]
      field_simp
      nlinarith [hs2]

/-- `det(Mᵀ B M) = det(M)² det(B)` for `M = [n₁ n₂]`; with `Q(n₁) = Q(n₂) = 0` and `2B(n₁, n₂) = 1`, the determinant
`det M = n₁₁ n₂₂ - n₂₁ n₁₂` satisfies `det(M)² D = 1/4`. -/
theorem det_null_pair (a b c : ℝ) (n₁ n₂ : ℝ × ℝ) (h1 : Qf a b c n₁ = 0) (h2 : Qf a b c n₂ = 0)
    (h3 : 2 * Bf a b c n₁ n₂ = 1) :
    (n₁.1 * n₂.2 - n₂.1 * n₁.2) ^ 2 * (b ^ 2 - a * c) = 1 / 4 := by
  have key : (n₁.1 * n₂.2 - n₂.1 * n₁.2) ^ 2 * (a * c - b ^ 2)
      = Qf a b c n₁ * Qf a b c n₂ - Bf a b c n₁ n₂ ^ 2 := by
    simp only [Qf, Bf]
    ring
  have hB : Bf a b c n₁ n₂ = 1 / 2 := by linarith
  rw [h1, h2, hB] at key
  linear_combination -key

/-- Hadamard's inequality in the plane: `|det[n₁ n₂]|² ≤ |n₁|² |n₂|²`. -/
theorem hadamard2 (n₁ n₂ : ℝ × ℝ) :
    (n₁.1 * n₂.2 - n₂.1 * n₁.2) ^ 2 ≤ (n₁.1 ^ 2 + n₁.2 ^ 2) * (n₂.1 ^ 2 + n₂.2 ^ 2) := by
  nlinarith [sq_nonneg (n₁.1 * n₂.1 + n₁.2 * n₂.2)]

theorem Qf_comb (a b c s t : ℝ) (n₁ n₂ : ℝ × ℝ) :
    Qf a b c (s * n₁.1 + t * n₂.1, s * n₁.2 + t * n₂.2)
      = s ^ 2 * Qf a b c n₁ + 2 * s * t * Bf a b c n₁ n₂ + t ^ 2 * Qf a b c n₂ := by
  simp only [Qf, Bf]
  ring


/-! ### Hyperbolic coordinates and the assembly of Lemma 5.3 -/

/-- The density bound for `Y = (q(W) - v)/√D`: `h(y) = 6 + log₊(16/|y|)`, `h(0) = ∞` (the same definition as in the file
for Lemma 5.6, which consumes it). -/
noncomputable def hY (y : ℝ) : ℝ≥0∞ :=
  if y = 0 then ⊤ else ENNReal.ofReal (6 + max 0 (Real.log (16 / |y|)))

theorem hY_even (y : ℝ) : hY (-y) = hY y := by
  unfold hY
  simp only [neg_eq_zero, abs_neg]

theorem hY_pos (y : ℝ) (hy : 0 < y) : hY y = ENNReal.ofReal (6 + max 0 (Real.log (16 / y))) := by
  unfold hY
  rw [if_neg hy.ne', abs_of_pos hy]

/-- The substitution `t = δ/s` on `(0, ∞)` for fixed `s > 0`: `∫_0^∞ g(t) dt = ∫_0^∞ s⁻¹ g(δ/s) dδ`. -/
theorem lintegral_Ioi_div (s : ℝ) (hs : 0 < s) (g : ℝ → ℝ≥0∞) :
    ∫⁻ t in Ioi (0 : ℝ), g t = ∫⁻ δ in Ioi (0 : ℝ), ENNReal.ofReal s⁻¹ * g (δ / s) := by
  have hderiv : ∀ x ∈ Ioi (0 : ℝ), HasDerivWithinAt (fun δ : ℝ => δ / s) s⁻¹ (Ioi 0) x := by
    intro x _
    have h := ((hasDerivAt_id' x).div_const s).hasDerivWithinAt (s := Ioi (0 : ℝ))
    simpa [one_div] using h
  have hinj : InjOn (fun δ : ℝ => δ / s) (Ioi 0) := by
    intro x _ y _ hxy
    exact (div_left_inj' hs.ne').1 hxy
  have himage : (fun δ : ℝ => δ / s) '' Ioi 0 = Ioi 0 := by
    ext y
    constructor
    · rintro ⟨x, hx, rfl⟩
      exact div_pos hx hs
    · intro hy
      exact ⟨y * s, mul_pos hy hs, mul_div_cancel_right₀ y hs.ne'⟩
  have h := lintegral_image_eq_lintegral_abs_deriv_mul measurableSet_Ioi hderiv hinj g
  rw [himage] at h
  rw [h]
  apply setLIntegral_congr_fun measurableSet_Ioi
  intro x _
  simp only [abs_of_pos (inv_pos.2 hs)]

/-- The substitution `s = √δ e^τ` for fixed `δ > 0`: `∫_0^∞ s⁻¹ g(s) ds = ∫_ℝ g(√δ e^τ) dτ`. -/
theorem lintegral_Ioi_exp (δ : ℝ) (hδ : 0 < δ) (g : ℝ → ℝ≥0∞) :
    ∫⁻ s in Ioi (0 : ℝ), ENNReal.ofReal s⁻¹ * g s = ∫⁻ τ, g (√δ * Real.exp τ) := by
  have hsδ : 0 < √δ := Real.sqrt_pos.2 hδ
  have hderiv : ∀ x ∈ (univ : Set ℝ),
      HasDerivWithinAt (fun τ : ℝ => √δ * Real.exp τ) (√δ * Real.exp x) univ x :=
    fun x _ => ((Real.hasDerivAt_exp x).const_mul (√δ)).hasDerivWithinAt
  have hinj : InjOn (fun τ : ℝ => √δ * Real.exp τ) univ := by
    intro x _ y _ hxy
    exact Real.exp_injective (mul_left_cancel₀ hsδ.ne' hxy)
  have himage : (fun τ : ℝ => √δ * Real.exp τ) '' univ = Ioi 0 := by
    ext y
    constructor
    · rintro ⟨x, _, rfl⟩
      exact mul_pos hsδ (Real.exp_pos x)
    · intro hy
      have hy' : (0 : ℝ) < y := hy
      refine ⟨Real.log (y / √δ), mem_univ _, ?_⟩
      show √δ * Real.exp (Real.log (y / √δ)) = y
      rw [Real.exp_log (div_pos hy' hsδ), mul_div_assoc', mul_div_cancel_left₀ y hsδ.ne']
  have h := lintegral_image_eq_lintegral_abs_deriv_mul MeasurableSet.univ hderiv hinj
    (fun s => ENNReal.ofReal s⁻¹ * g s)
  rw [himage, Measure.restrict_univ] at h
  rw [h]
  apply lintegral_congr
  intro τ
  have hp : 0 < √δ * Real.exp τ := mul_pos hsδ (Real.exp_pos τ)
  rw [← mul_assoc, ← ENNReal.ofReal_mul (abs_nonneg _), abs_of_pos hp, mul_inv_cancel₀ hp.ne',
    ENNReal.ofReal_one, one_mul]

/-- **Hyperbolic coordinates on the open quadrant.** For measurable `φ` and `G`,
`∫_{s,t>0} φ(st) G(s,t) = ∫_{δ>0} φ(δ) ∫_ℝ G(√δ e^τ, √δ e^{-τ}) dτ dδ` (the Jacobian of
`(δ, τ) ↦ (√δ e^τ, √δ e^{-τ})` is `1`). -/
theorem lintegral_quadrant (φ : ℝ → ℝ≥0∞) (hφ : Measurable φ) (G : ℝ × ℝ → ℝ≥0∞) (hG : Measurable G) :
    ∫⁻ p in Ioi (0 : ℝ) ×ˢ Ioi (0 : ℝ), φ (p.1 * p.2) * G p
      = ∫⁻ δ in Ioi (0 : ℝ), φ δ * ∫⁻ τ, G (√δ * Real.exp τ, √δ * Real.exp (-τ)) := by
  have e1 : (volume : Measure (ℝ × ℝ)).restrict (Ioi (0 : ℝ) ×ˢ Ioi (0 : ℝ))
      = (volume.restrict (Ioi (0 : ℝ))).prod (volume.restrict (Ioi (0 : ℝ))) := by
    rw [Measure.prod_restrict, ← Measure.volume_eq_prod]
  have hmeas : Measurable fun p : ℝ × ℝ => φ (p.1 * p.2) * G p :=
    (hφ.comp (measurable_fst.mul measurable_snd)).mul hG
  rw [e1, lintegral_prod _ hmeas.aemeasurable]
  show ∫⁻ s in Ioi (0 : ℝ), ∫⁻ t in Ioi (0 : ℝ), φ (s * t) * G (s, t) = _
  -- the inner substitution t = δ/s
  have step1 : ∀ s ∈ Ioi (0 : ℝ), ∫⁻ t in Ioi (0 : ℝ), φ (s * t) * G (s, t)
      = ∫⁻ δ in Ioi (0 : ℝ), ENNReal.ofReal s⁻¹ * (φ δ * G (s, δ / s)) := by
    intro s hs
    have hs' : (0 : ℝ) < s := hs
    rw [lintegral_Ioi_div s hs' (fun t => φ (s * t) * G (s, t))]
    apply setLIntegral_congr_fun measurableSet_Ioi
    intro δ _
    simp only [mul_div_assoc', mul_div_cancel_left₀ _ hs'.ne']
  rw [setLIntegral_congr_fun measurableSet_Ioi step1]
  -- swap the two integrals
  have hmeas2 : Measurable (Function.uncurry fun (s δ : ℝ) => ENNReal.ofReal s⁻¹ * (φ δ * G (s, δ / s))) := by
    have h : Measurable fun p : ℝ × ℝ => ENNReal.ofReal p.1⁻¹ * (φ p.2 * G (p.1, p.2 / p.1)) :=
      (ENNReal.measurable_ofReal.comp measurable_fst.inv).mul
        ((hφ.comp measurable_snd).mul (hG.comp (measurable_fst.prodMk (measurable_snd.div measurable_fst))))
    exact h
  rw [lintegral_lintegral_swap hmeas2.aemeasurable]
  apply setLIntegral_congr_fun measurableSet_Ioi
  intro δ hδ
  have hδ' : (0 : ℝ) < δ := hδ
  have hsδ : 0 < √δ := Real.sqrt_pos.2 hδ'
  have h2 : √δ * √δ = δ := Real.mul_self_sqrt hδ'.le
  show ∫⁻ s in Ioi (0 : ℝ), ENNReal.ofReal s⁻¹ * (φ δ * G (s, δ / s))
    = φ δ * ∫⁻ τ, G (√δ * Real.exp τ, √δ * Real.exp (-τ))
  -- pull φ(δ) out, then the substitution s = √δ e^τ
  have e2 : ∫⁻ s in Ioi (0 : ℝ), ENNReal.ofReal s⁻¹ * (φ δ * G (s, δ / s))
      = φ δ * ∫⁻ s in Ioi (0 : ℝ), ENNReal.ofReal s⁻¹ * G (s, δ / s) := by
    rw [← lintegral_const_mul]
    · apply lintegral_congr
      intro s
      ring
    · exact (ENNReal.measurable_ofReal.comp measurable_inv).mul
        (hG.comp (measurable_id.prodMk (measurable_const.div measurable_id)))
  rw [e2, lintegral_Ioi_exp δ hδ' (fun s => G (s, δ / s))]
  congr 1
  apply lintegral_congr
  intro τ
  have e3 : δ / (√δ * Real.exp τ) = √δ * Real.exp (-τ) := by
    have hx : Real.exp τ ≠ 0 := (Real.exp_pos τ).ne'
    rw [Real.exp_neg, div_eq_iff (mul_pos hsδ (Real.exp_pos τ)).ne']
    calc δ = (√δ * √δ) * ((Real.exp τ)⁻¹ * Real.exp τ) := by rw [h2, inv_mul_cancel₀ hx, mul_one]
      _ = √δ * (Real.exp τ)⁻¹ * (√δ * Real.exp τ) := by ring
  rw [e3]

/-- `Q(s n₁ + t n₂) = st` for a null pair. -/
theorem Qf_null (a b c : ℝ) (n₁ n₂ : ℝ × ℝ) (h1 : Qf a b c n₁ = 0) (h2 : Qf a b c n₂ = 0)
    (h3 : 2 * Bf a b c n₁ n₂ = 1) (s t : ℝ) :
    Qf a b c (n₁.1 * s + n₂.1 * t, n₁.2 * s + n₂.2 * t) = s * t := by
  have e : Qf a b c (n₁.1 * s + n₂.1 * t, n₁.2 * s + n₂.2 * t)
      = s ^ 2 * Qf a b c n₁ + 2 * s * t * Bf a b c n₁ n₂ + t ^ 2 * Qf a b c n₂ := by
    simp only [Qf, Bf]
    ring
  have hB : Bf a b c n₁ n₂ = 1 / 2 := by linarith
  rw [e, h1, h2, hB]
  ring

/-- **The linear change of variables** `w = s n₁ + t n₂`: `∫ g = |det[n₁ n₂]| ∫ g(s n₁ + t n₂) ds dt`. -/
theorem lintegral_linear (n₁ n₂ : ℝ × ℝ) (hdet : n₁.1 * n₂.2 - n₂.1 * n₁.2 ≠ 0) (g : ℝ × ℝ → ℝ≥0∞)
    (hg : Measurable g) :
    ∫⁻ w, g w = ENNReal.ofReal |n₁.1 * n₂.2 - n₂.1 * n₁.2|
      * ∫⁻ p : ℝ × ℝ, g (n₁.1 * p.1 + n₂.1 * p.2, n₁.2 * p.1 + n₂.2 * p.2) := by
  set M : ℝ × ℝ →ₗ[ℝ] ℝ × ℝ :=
    Matrix.toLin (Module.Basis.finTwoProd ℝ) (Module.Basis.finTwoProd ℝ) !![n₁.1, n₂.1; n₁.2, n₂.2] with hMdef
  have hM : ∀ p : ℝ × ℝ, M p = (n₁.1 * p.1 + n₂.1 * p.2, n₁.2 * p.1 + n₂.2 * p.2) :=
    fun p => Matrix.toLin_finTwoProd_apply _ _ _ _ p
  have hdetM : LinearMap.det M = n₁.1 * n₂.2 - n₂.1 * n₁.2 := by
    rw [hMdef, LinearMap.det_toLin, Matrix.det_fin_two_of]
  have hmap := MeasureTheory.Measure.map_linearMap_addHaar_eq_smul_addHaar
    (μ := (volume : Measure (ℝ × ℝ))) (f := M) (by rw [hdetM]; exact hdet)
  have hMmeas : Measurable M := M.continuous_of_finiteDimensional.measurable
  have h1 : ∫⁻ p, g (M p) = ENNReal.ofReal |(LinearMap.det M)⁻¹| * ∫⁻ w, g w := by
    rw [← lintegral_map hg hMmeas, hmap, lintegral_smul_measure, smul_eq_mul]
  simp only [hM] at h1
  rw [h1, hdetM, ← mul_assoc, ← ENNReal.ofReal_mul (abs_nonneg _), ← abs_mul, mul_inv_cancel₀ hdet, abs_one,
    ENNReal.ofReal_one, one_mul]

/-- Lebesgue measure on the plane is invariant under `p ↦ -p`. -/
theorem lintegral_neg_prod (g : ℝ × ℝ → ℝ≥0∞) (hg : Measurable g) :
    ∫⁻ p : ℝ × ℝ, g (-p) = ∫⁻ p, g p := by
  have h := lintegral_linear ((-1 : ℝ), (0 : ℝ)) ((0 : ℝ), (-1 : ℝ)) (by norm_num) g hg
  rw [h]
  have e1 : |((-1 : ℝ), (0 : ℝ)).1 * ((0 : ℝ), (-1 : ℝ)).2 - ((0 : ℝ), (-1 : ℝ)).1 * ((-1 : ℝ), (0 : ℝ)).2| = 1 := by
    norm_num
  rw [e1, ENNReal.ofReal_one, one_mul]
  apply lintegral_congr
  intro p
  congr 1
  ext <;> simp

/-- `Q₃ → Q₁` by `p ↦ -p`. -/
theorem setLIntegral_Q3 (K : ℝ × ℝ → ℝ≥0∞) (hK : Measurable K) :
    ∫⁻ p in Iio (0 : ℝ) ×ˢ Iio (0 : ℝ), K p = ∫⁻ p in Ioi (0 : ℝ) ×ˢ Ioi (0 : ℝ), K (-p) := by
  have hm3 : MeasurableSet (Iio (0 : ℝ) ×ˢ Iio (0 : ℝ)) := measurableSet_Iio.prod measurableSet_Iio
  have hm1 : MeasurableSet (Ioi (0 : ℝ) ×ˢ Ioi (0 : ℝ)) := measurableSet_Ioi.prod measurableSet_Ioi
  rw [← lintegral_indicator hm3, ← lintegral_indicator hm1, ← lintegral_neg_prod _ (hK.indicator hm3)]
  apply lintegral_congr
  intro p
  by_cases hp : p ∈ Ioi (0 : ℝ) ×ˢ Ioi (0 : ℝ)
  · have hp' : -p ∈ Iio (0 : ℝ) ×ˢ Iio (0 : ℝ) := by
      simp only [mem_prod, mem_Ioi, mem_Iio, Prod.fst_neg, Prod.snd_neg] at hp ⊢
      exact ⟨by linarith [hp.1], by linarith [hp.2]⟩
    rw [indicator_of_mem hp', indicator_of_mem hp]
  · have hp' : -p ∉ Iio (0 : ℝ) ×ˢ Iio (0 : ℝ) := by
      intro h
      apply hp
      simp only [mem_prod, mem_Ioi, mem_Iio, Prod.fst_neg, Prod.snd_neg] at h ⊢
      exact ⟨by linarith [h.1], by linarith [h.2]⟩
    rw [indicator_of_notMem hp', indicator_of_notMem hp]

/-- **The two quadrants.** `{st > 0} = Q₁ ∪ Q₃`, and `Q₃` is carried to `Q₁` by `p ↦ -p`. -/
theorem lintegral_hyp_split (g : ℝ → ℝ≥0∞) (hg : Measurable g) (K : ℝ × ℝ → ℝ≥0∞) (hK : Measurable K) :
    ∫⁻ p : ℝ × ℝ, (Ioi (0 : ℝ)).indicator g (p.1 * p.2) * K p
      = (∫⁻ p in Ioi (0 : ℝ) ×ˢ Ioi (0 : ℝ), g (p.1 * p.2) * K p)
        + ∫⁻ p in Ioi (0 : ℝ) ×ˢ Ioi (0 : ℝ), g (p.1 * p.2) * K (-p) := by
  have hm1 : MeasurableSet (Ioi (0 : ℝ) ×ˢ Ioi (0 : ℝ)) := measurableSet_Ioi.prod measurableSet_Ioi
  have hm3 : MeasurableSet (Iio (0 : ℝ) ×ˢ Iio (0 : ℝ)) := measurableSet_Iio.prod measurableSet_Iio
  have hK' : Measurable fun p : ℝ × ℝ => g (p.1 * p.2) * K p :=
    (hg.comp (measurable_fst.mul measurable_snd)).mul hK
  have e1 : ∀ p : ℝ × ℝ, (Ioi (0 : ℝ)).indicator g (p.1 * p.2) * K p
      = (Ioi (0 : ℝ) ×ˢ Ioi (0 : ℝ) ∪ Iio (0 : ℝ) ×ˢ Iio (0 : ℝ)).indicator
          (fun p : ℝ × ℝ => g (p.1 * p.2) * K p) p := by
    intro p
    by_cases hp : 0 < p.1 * p.2
    · have hmem : p ∈ Ioi (0 : ℝ) ×ˢ Ioi (0 : ℝ) ∪ Iio (0 : ℝ) ×ˢ Iio (0 : ℝ) := by
        rcases lt_trichotomy p.1 0 with h | h | h
        · exact mem_union_right _ (mem_prod.2 ⟨h, show p.2 < 0 by nlinarith⟩)
        · rw [h, zero_mul] at hp
          exact absurd hp (lt_irrefl 0)
        · exact mem_union_left _ (mem_prod.2 ⟨h, show 0 < p.2 by nlinarith⟩)
      rw [indicator_of_mem (show p.1 * p.2 ∈ Ioi (0 : ℝ) from hp), indicator_of_mem hmem]
    · have hmem : p ∉ Ioi (0 : ℝ) ×ˢ Ioi (0 : ℝ) ∪ Iio (0 : ℝ) ×ˢ Iio (0 : ℝ) := by
        rintro (h | h)
        · exact hp (mul_pos (mem_prod.1 h).1 (mem_prod.1 h).2)
        · exact hp (mul_pos_of_neg_of_neg (mem_prod.1 h).1 (mem_prod.1 h).2)
      rw [indicator_of_notMem (show p.1 * p.2 ∉ Ioi (0 : ℝ) from hp), indicator_of_notMem hmem, zero_mul]
  have hdisj : Disjoint (Ioi (0 : ℝ) ×ˢ Ioi (0 : ℝ)) (Iio (0 : ℝ) ×ˢ Iio (0 : ℝ)) := by
    rw [Set.disjoint_left]
    intro p h1 h3
    exact lt_asymm (mem_Ioi.1 (mem_prod.1 h1).1) (mem_Iio.1 (mem_prod.1 h3).1)
  rw [lintegral_congr e1, lintegral_indicator (hm1.union hm3), lintegral_union hm3 hdisj,
    setLIntegral_Q3 _ hK']
  refine congrArg₂ (· + ·) rfl ?_
  apply lintegral_congr
  intro p
  simp only [Prod.fst_neg, Prod.snd_neg, neg_mul_neg]

/-- **The branch bound in terms of `δ`.** Along `w(τ) = √δ (e^τ n₁ + e^{-τ} n₂)` with `det[n₁ n₂]² D = 1/4`,
`∫ f₁(w₁) f₂(w₂) dτ ≤ 6 + log⁺(16 √D / δ)`, since `|n₁| |n₂| ≥ |det[n₁ n₂]| = 1/(2√D)`. -/
theorem branch_delta (f₁ f₂ : ℝ → ℝ) (hf₁ : Measurable f₁) (hf₂ : Measurable f₂)
    (h0₁ : ∀ y, 0 ≤ f₁ y) (h1₁ : ∀ y, f₁ y ≤ 1) (h0₂ : ∀ y, 0 ≤ f₂ y) (h1₂ : ∀ y, f₂ y ≤ 1)
    (hi₁ : ∫⁻ y, ENNReal.ofReal (f₁ y) ≤ 1) (hi₂ : ∫⁻ y, ENNReal.ofReal (f₂ y) ≤ 1)
    (D : ℝ) (hD : 0 < D) (n₁ n₂ : ℝ × ℝ) (hdet : (n₁.1 * n₂.2 - n₂.1 * n₁.2) ^ 2 * D = 1 / 4)
    (δ : ℝ) (hδ : 0 < δ) :
    ∫⁻ τ, ENNReal.ofReal (f₁ (n₁.1 * (√δ * Real.exp τ) + n₂.1 * (√δ * Real.exp (-τ)))
        * f₂ (n₁.2 * (√δ * Real.exp τ) + n₂.2 * (√δ * Real.exp (-τ))))
      ≤ ENNReal.ofReal (6 + max 0 (Real.log (16 * √D / δ))) := by
  have hdt0 : n₁.1 * n₂.2 - n₂.1 * n₁.2 ≠ 0 := by
    intro h
    rw [h] at hdet
    norm_num at hdet
  have hdtsq : 0 < (n₁.1 * n₂.2 - n₂.1 * n₁.2) ^ 2 :=
    lt_of_le_of_ne (sq_nonneg _) (Ne.symm (pow_ne_zero 2 hdt0))
  have hA : 0 ≤ n₁.1 ^ 2 + n₁.2 ^ 2 := by positivity
  have hB : 0 ≤ n₂.1 ^ 2 + n₂.2 ^ 2 := by positivity
  have hAB : 0 < (n₁.1 ^ 2 + n₁.2 ^ 2) * (n₂.1 ^ 2 + n₂.2 ^ 2) := lt_of_lt_of_le hdtsq (hadamard2 n₁ n₂)
  have hn₁ : 0 < n₁.1 ^ 2 + n₁.2 ^ 2 := by
    rcases hA.lt_or_eq with h | h
    · exact h
    · rw [← h, zero_mul] at hAB
      exact absurd hAB (lt_irrefl 0)
  have hn₂ : 0 < n₂.1 ^ 2 + n₂.2 ^ 2 := by
    rcases hB.lt_or_eq with h | h
    · exact h
    · rw [← h, mul_zero] at hAB
      exact absurd hAB (lt_irrefl 0)
  have hu : 0 < (√δ * n₁.1) ^ 2 + (√δ * n₁.2) ^ 2 := by
    have e : (√δ * n₁.1) ^ 2 + (√δ * n₁.2) ^ 2 = δ * (n₁.1 ^ 2 + n₁.2 ^ 2) := by
      rw [mul_pow, mul_pow, Real.sq_sqrt hδ.le]
      ring
    rw [e]
    exact mul_pos hδ hn₁
  have hv : 0 < (√δ * n₂.1) ^ 2 + (√δ * n₂.2) ^ 2 := by
    have e : (√δ * n₂.1) ^ 2 + (√δ * n₂.2) ^ 2 = δ * (n₂.1 ^ 2 + n₂.2 ^ 2) := by
      rw [mul_pow, mul_pow, Real.sq_sqrt hδ.le]
      ring
    rw [e]
    exact mul_pos hδ hn₂
  have hb := branch_bound_gen f₁ f₂ hf₁ hf₂ h0₁ h1₁ h0₂ h1₂ hi₁ hi₂
    (√δ * n₁.1) (√δ * n₁.2) (√δ * n₂.1) (√δ * n₂.2) hu hv
  have e : ∀ τ, ENNReal.ofReal (f₁ (n₁.1 * (√δ * Real.exp τ) + n₂.1 * (√δ * Real.exp (-τ)))
        * f₂ (n₁.2 * (√δ * Real.exp τ) + n₂.2 * (√δ * Real.exp (-τ))))
      = ENNReal.ofReal (f₁ (√δ * n₁.1 * Real.exp τ + √δ * n₂.1 * Real.exp (-τ))
        * f₂ (√δ * n₁.2 * Real.exp τ + √δ * n₂.2 * Real.exp (-τ))) := by
    intro τ
    rw [show n₁.1 * (√δ * Real.exp τ) + n₂.1 * (√δ * Real.exp (-τ))
        = √δ * n₁.1 * Real.exp τ + √δ * n₂.1 * Real.exp (-τ) by ring,
      show n₁.2 * (√δ * Real.exp τ) + n₂.2 * (√δ * Real.exp (-τ))
        = √δ * n₁.2 * Real.exp τ + √δ * n₂.2 * Real.exp (-τ) by ring]
  rw [lintegral_congr e]
  refine hb.trans (ENNReal.ofReal_le_ofReal ?_)
  -- the constant
  have hN₁ : √((√δ * n₁.1) ^ 2 + (√δ * n₁.2) ^ 2) = √δ * √(n₁.1 ^ 2 + n₁.2 ^ 2) := by
    rw [← Real.sqrt_mul hδ.le]
    congr 1
    rw [mul_pow, mul_pow, Real.sq_sqrt hδ.le]
    ring
  have hN₂ : √((√δ * n₂.1) ^ 2 + (√δ * n₂.2) ^ 2) = √δ * √(n₂.1 ^ 2 + n₂.2 ^ 2) := by
    rw [← Real.sqrt_mul hδ.le]
    congr 1
    rw [mul_pow, mul_pow, Real.sq_sqrt hδ.le]
    ring
  obtain ⟨P, hP⟩ : ∃ P, P = √(n₁.1 ^ 2 + n₁.2 ^ 2) * √(n₂.1 ^ 2 + n₂.2 ^ 2) := ⟨_, rfl⟩
  have hPpos : 0 < P := by
    rw [hP]
    exact mul_pos (Real.sqrt_pos.2 hn₁) (Real.sqrt_pos.2 hn₂)
  have hPsq : P ^ 2 = (n₁.1 ^ 2 + n₁.2 ^ 2) * (n₂.1 ^ 2 + n₂.2 ^ 2) := by
    rw [hP, mul_pow, Real.sq_sqrt hn₁.le, Real.sq_sqrt hn₂.le]
  have hsD : 0 < √D := Real.sqrt_pos.2 hD
  have hdtD : (n₁.1 * n₂.2 - n₂.1 * n₁.2) ^ 2 * (2 * √D) ^ 2 = 1 := by
    rw [mul_pow 2 (√D), Real.sq_sqrt hD.le]
    linear_combination 4 * hdet
  have hPge : 1 ≤ P * (2 * √D) := by
    have h1 : (n₁.1 * n₂.2 - n₂.1 * n₁.2) ^ 2 ≤ P ^ 2 := by
      rw [hPsq]
      exact hadamard2 n₁ n₂
    have h2 : 1 ≤ (P * (2 * √D)) ^ 2 := by
      rw [mul_pow P]
      nlinarith [hdtD, h1, sq_nonneg (2 * √D)]
    have h3 : 0 ≤ P * (2 * √D) := by positivity
    nlinarith [h2, h3]
  have hprod : √((√δ * n₁.1) ^ 2 + (√δ * n₁.2) ^ 2) * √((√δ * n₂.1) ^ 2 + (√δ * n₂.2) ^ 2) = δ * P := by
    rw [hN₁, hN₂, hP]
    have hss : √δ * √δ = δ := Real.mul_self_sqrt hδ.le
    calc √δ * √(n₁.1 ^ 2 + n₁.2 ^ 2) * (√δ * √(n₂.1 ^ 2 + n₂.2 ^ 2))
        = (√δ * √δ) * (√(n₁.1 ^ 2 + n₁.2 ^ 2) * √(n₂.1 ^ 2 + n₂.2 ^ 2)) := by ring
      _ = δ * (√(n₁.1 ^ 2 + n₁.2 ^ 2) * √(n₂.1 ^ 2 + n₂.2 ^ 2)) := by rw [hss]
  rw [hprod]
  have hlog : Real.log (8 / (δ * P)) ≤ Real.log (16 * √D / δ) := by
    apply Real.log_le_log (by positivity)
    rw [div_le_div_iff₀ (by positivity) hδ]
    nlinarith [hPge, hδ, hPpos]
  have hmax := max_le_max (le_refl (0 : ℝ)) hlog
  linarith

/-- `∫_{δ>0} φ(δ/s) (6 + log⁺(16 s/δ)) dδ = s ∫_{y>0} φ(y) h(y) dy` (the substitution `δ = s y`). -/
theorem delta_rescale (s : ℝ) (hs : 0 < s) (φ : ℝ → ℝ≥0∞) :
    ∫⁻ δ in Ioi (0 : ℝ), φ (δ / s) * ENNReal.ofReal (6 + max 0 (Real.log (16 * s / δ)))
      = ENNReal.ofReal s * ∫⁻ y in Ioi (0 : ℝ), φ y * hY y := by
  rw [lintegral_Ioi_div s hs (fun y => φ y * hY y), ← lintegral_const_mul' _ _ ENNReal.ofReal_ne_top]
  apply setLIntegral_congr_fun measurableSet_Ioi
  intro δ hδ
  have hδ' : (0 : ℝ) < δ := hδ
  show φ (δ / s) * ENNReal.ofReal (6 + max 0 (Real.log (16 * s / δ)))
    = ENNReal.ofReal s * (ENNReal.ofReal s⁻¹ * (φ (δ / s) * hY (δ / s)))
  rw [hY_pos _ (div_pos hδ' hs), div_div_eq_mul_div, ← mul_assoc, ← ENNReal.ofReal_mul hs.le,
    mul_inv_cancel₀ hs.ne', ENNReal.ofReal_one, one_mul]

/-- **One quadrant.** In the coordinates `w = s n₁ + t n₂` (with `Q(w) = st`), the open quadrant `s, t > 0`
contributes at most `√D ∫_{y>0} φ(y) h(y) dy`. -/
theorem quadrant_bound (f₁ f₂ : ℝ → ℝ) (hf₁ : Measurable f₁) (hf₂ : Measurable f₂)
    (h0₁ : ∀ y, 0 ≤ f₁ y) (h1₁ : ∀ y, f₁ y ≤ 1) (h0₂ : ∀ y, 0 ≤ f₂ y) (h1₂ : ∀ y, f₂ y ≤ 1)
    (hi₁ : ∫⁻ y, ENNReal.ofReal (f₁ y) ≤ 1) (hi₂ : ∫⁻ y, ENNReal.ofReal (f₂ y) ≤ 1)
    (D : ℝ) (hD : 0 < D) (n₁ n₂ : ℝ × ℝ) (hdet : (n₁.1 * n₂.2 - n₂.1 * n₁.2) ^ 2 * D = 1 / 4)
    (φ : ℝ → ℝ≥0∞) (hφ : Measurable φ) :
    ∫⁻ p in Ioi (0 : ℝ) ×ˢ Ioi (0 : ℝ), φ (p.1 * p.2 / √D)
        * ENNReal.ofReal (f₁ (n₁.1 * p.1 + n₂.1 * p.2) * f₂ (n₁.2 * p.1 + n₂.2 * p.2))
      ≤ ENNReal.ofReal √D * ∫⁻ y in Ioi (0 : ℝ), φ y * hY y := by
  have hsD : 0 < √D := Real.sqrt_pos.2 hD
  have hGm : Measurable fun p : ℝ × ℝ =>
      ENNReal.ofReal (f₁ (n₁.1 * p.1 + n₂.1 * p.2) * f₂ (n₁.2 * p.1 + n₂.2 * p.2)) :=
    ENNReal.measurable_ofReal.comp
      ((hf₁.comp ((measurable_fst.const_mul _).add (measurable_snd.const_mul _))).mul
        (hf₂.comp ((measurable_fst.const_mul _).add (measurable_snd.const_mul _))))
  have hφ' : Measurable fun x : ℝ => φ (x / √D) := hφ.comp (measurable_id.div_const _)
  rw [lintegral_quadrant (fun x => φ (x / √D)) hφ' _ hGm, ← delta_rescale √D hsD φ]
  apply setLIntegral_mono' measurableSet_Ioi
  intro δ hδ
  exact mul_le_mul_left' (branch_delta f₁ f₂ hf₁ hf₂ h0₁ h1₁ h0₂ h1₂ hi₁ hi₂ D hD n₁ n₂ hdet δ (mem_Ioi.1 hδ)) _

/-- **The positive half of Lemma 5.3, centred.** If `Q(s n₁ + t n₂) = st` with `det[n₁ n₂]² D = 1/4`, then
`∫ 1{Q(w) > 0} φ(Q(w)/√D) f₁(w₁) f₂(w₂) dw ≤ ∫_{y>0} φ(y) h(y) dy`. -/
theorem core_pos (f₁ f₂ : ℝ → ℝ) (hf₁ : Measurable f₁) (hf₂ : Measurable f₂)
    (h0₁ : ∀ y, 0 ≤ f₁ y) (h1₁ : ∀ y, f₁ y ≤ 1) (h0₂ : ∀ y, 0 ≤ f₂ y) (h1₂ : ∀ y, f₂ y ≤ 1)
    (hi₁ : ∫⁻ y, ENNReal.ofReal (f₁ y) ≤ 1) (hi₂ : ∫⁻ y, ENNReal.ofReal (f₂ y) ≤ 1)
    (Q : ℝ × ℝ → ℝ) (hQ : Measurable Q) (D : ℝ) (hD : 0 < D) (n₁ n₂ : ℝ × ℝ)
    (hdet : (n₁.1 * n₂.2 - n₂.1 * n₁.2) ^ 2 * D = 1 / 4)
    (hQn : ∀ s t : ℝ, Q (n₁.1 * s + n₂.1 * t, n₁.2 * s + n₂.2 * t) = s * t)
    (φ : ℝ → ℝ≥0∞) (hφ : Measurable φ) :
    ∫⁻ w : ℝ × ℝ, (Ioi (0 : ℝ)).indicator (fun x => φ (x / √D)) (Q w) * ENNReal.ofReal (f₁ w.1 * f₂ w.2)
      ≤ ∫⁻ y in Ioi (0 : ℝ), φ y * hY y := by
  have hsD : 0 < √D := Real.sqrt_pos.2 hD
  have hdt0 : n₁.1 * n₂.2 - n₂.1 * n₁.2 ≠ 0 := by
    intro h
    rw [h] at hdet
    norm_num at hdet
  have hdtD : ENNReal.ofReal |n₁.1 * n₂.2 - n₂.1 * n₁.2| * (2 * ENNReal.ofReal √D) = 1 := by
    have h2 : 0 ≤ |n₁.1 * n₂.2 - n₂.1 * n₁.2| * (2 * √D) := by positivity
    have h1 : (|n₁.1 * n₂.2 - n₂.1 * n₁.2| * (2 * √D)) ^ 2 = 1 := by
      rw [mul_pow, mul_pow, sq_abs, Real.sq_sqrt hD.le]
      linear_combination 4 * hdet
    have h3 : |n₁.1 * n₂.2 - n₂.1 * n₁.2| * (2 * √D) = 1 := by
      rw [← Real.sqrt_sq h2, h1, Real.sqrt_one]
    rw [show (2 : ℝ≥0∞) = ENNReal.ofReal 2 by norm_num, ← ENNReal.ofReal_mul (by norm_num : (0 : ℝ) ≤ 2),
      ← ENNReal.ofReal_mul (abs_nonneg _), h3, ENNReal.ofReal_one]
  have hF : Measurable fun w : ℝ × ℝ => ENNReal.ofReal (f₁ w.1 * f₂ w.2) :=
    ENNReal.measurable_ofReal.comp ((hf₁.comp measurable_fst).mul (hf₂.comp measurable_snd))
  have hφ' : Measurable fun x : ℝ => φ (x / √D) := hφ.comp (measurable_id.div_const _)
  have hind : Measurable fun x : ℝ => (Ioi (0 : ℝ)).indicator (fun x => φ (x / √D)) x :=
    hφ'.indicator measurableSet_Ioi
  have hG : Measurable fun w : ℝ × ℝ =>
      (Ioi (0 : ℝ)).indicator (fun x => φ (x / √D)) (Q w) * ENNReal.ofReal (f₁ w.1 * f₂ w.2) :=
    (hind.comp hQ).mul hF
  have hGm : Measurable fun p : ℝ × ℝ =>
      ENNReal.ofReal (f₁ (n₁.1 * p.1 + n₂.1 * p.2) * f₂ (n₁.2 * p.1 + n₂.2 * p.2)) :=
    ENNReal.measurable_ofReal.comp
      ((hf₁.comp ((measurable_fst.const_mul _).add (measurable_snd.const_mul _))).mul
        (hf₂.comp ((measurable_fst.const_mul _).add (measurable_snd.const_mul _))))
  rw [lintegral_linear n₁ n₂ hdt0 _ hG]
  have e0 : ∫⁻ p : ℝ × ℝ, (Ioi (0 : ℝ)).indicator (fun x => φ (x / √D))
        (Q (n₁.1 * p.1 + n₂.1 * p.2, n₁.2 * p.1 + n₂.2 * p.2))
        * ENNReal.ofReal (f₁ (n₁.1 * p.1 + n₂.1 * p.2, n₁.2 * p.1 + n₂.2 * p.2).1
          * f₂ (n₁.1 * p.1 + n₂.1 * p.2, n₁.2 * p.1 + n₂.2 * p.2).2)
      = ∫⁻ p : ℝ × ℝ, (Ioi (0 : ℝ)).indicator (fun x => φ (x / √D)) (p.1 * p.2)
        * ENNReal.ofReal (f₁ (n₁.1 * p.1 + n₂.1 * p.2) * f₂ (n₁.2 * p.1 + n₂.2 * p.2)) := by
    apply lintegral_congr
    intro p
    rw [hQn]
  rw [e0, lintegral_hyp_split (fun x => φ (x / √D)) hφ' _ hGm]
  have e3 : ∫⁻ p in Ioi (0 : ℝ) ×ˢ Ioi (0 : ℝ), φ (p.1 * p.2 / √D)
        * ENNReal.ofReal (f₁ (n₁.1 * (-p).1 + n₂.1 * (-p).2) * f₂ (n₁.2 * (-p).1 + n₂.2 * (-p).2))
      = ∫⁻ p in Ioi (0 : ℝ) ×ˢ Ioi (0 : ℝ), φ (p.1 * p.2 / √D)
        * ENNReal.ofReal (f₁ ((-n₁).1 * p.1 + (-n₂).1 * p.2) * f₂ ((-n₁).2 * p.1 + (-n₂).2 * p.2)) := by
    apply lintegral_congr
    intro p
    simp only [Prod.fst_neg, Prod.snd_neg, mul_neg, neg_mul]
  have hdet' : ((-n₁).1 * (-n₂).2 - (-n₂).1 * (-n₁).2) ^ 2 * D = 1 / 4 := by
    simp only [Prod.fst_neg, Prod.snd_neg, neg_mul_neg]
    exact hdet
  rw [e3]
  have hb1 := quadrant_bound f₁ f₂ hf₁ hf₂ h0₁ h1₁ h0₂ h1₂ hi₁ hi₂ D hD n₁ n₂ hdet φ hφ
  have hb2 := quadrant_bound f₁ f₂ hf₁ hf₂ h0₁ h1₁ h0₂ h1₂ hi₁ hi₂ D hD (-n₁) (-n₂) hdet' φ hφ
  calc _ ≤ ENNReal.ofReal |n₁.1 * n₂.2 - n₂.1 * n₁.2| * ((ENNReal.ofReal √D * ∫⁻ y in Ioi (0 : ℝ), φ y * hY y)
          + ENNReal.ofReal √D * ∫⁻ y in Ioi (0 : ℝ), φ y * hY y) := mul_le_mul_left' (add_le_add hb1 hb2) _
    _ = (ENNReal.ofReal |n₁.1 * n₂.2 - n₂.1 * n₁.2| * (2 * ENNReal.ofReal √D))
          * ∫⁻ y in Ioi (0 : ℝ), φ y * hY y := by ring
    _ = ∫⁻ y in Ioi (0 : ℝ), φ y * hY y := by rw [hdtD, one_mul]

/-- The coordinate axes are Lebesgue null in the plane. -/
theorem volume_axes : volume {p : ℝ × ℝ | p.1 * p.2 = 0} = 0 := by
  have hsub : {p : ℝ × ℝ | p.1 * p.2 = 0} ⊆ ({0} : Set ℝ) ×ˢ (univ : Set ℝ) ∪ (univ : Set ℝ) ×ˢ ({0} : Set ℝ) := by
    intro p hp
    rcases mul_eq_zero.1 hp with h | h
    · exact mem_union_left _ (mem_prod.2 ⟨mem_singleton_iff.2 h, mem_univ _⟩)
    · exact mem_union_right _ (mem_prod.2 ⟨mem_univ _, mem_singleton_iff.2 h⟩)
  apply measure_mono_null hsub
  apply measure_union_null
  · rw [Measure.volume_eq_prod, Measure.prod_prod, Real.volume_singleton, zero_mul]
  · rw [Measure.volume_eq_prod, Measure.prod_prod, Real.volume_singleton, mul_zero]

/-- The level set `{q = v}` of an indefinite form is Lebesgue null (it is the union of two lines). -/
theorem null_level (a b c : ℝ) (hD : 0 < b ^ 2 - a * c) : volume {w : ℝ × ℝ | Qf a b c w = 0} = 0 := by
  obtain ⟨n₁, n₂, h1, h2, h3⟩ := null_pair a b c hD
  have hdet := det_null_pair a b c n₁ n₂ h1 h2 h3
  have hdt0 : n₁.1 * n₂.2 - n₂.1 * n₁.2 ≠ 0 := by
    intro h
    rw [h] at hdet
    norm_num at hdet
  have hQm : Measurable (Qf a b c) := by
    unfold Qf
    fun_prop
  have hZ : MeasurableSet {w : ℝ × ℝ | Qf a b c w = 0} := measurableSet_eq_fun hQm measurable_const
  rw [← lintegral_indicator_one hZ, lintegral_linear n₁ n₂ hdt0 _ (measurable_one.indicator hZ)]
  have e : ∀ p : ℝ × ℝ,
      {w : ℝ × ℝ | Qf a b c w = 0}.indicator 1 (n₁.1 * p.1 + n₂.1 * p.2, n₁.2 * p.1 + n₂.2 * p.2)
        = {p : ℝ × ℝ | p.1 * p.2 = 0}.indicator (1 : ℝ × ℝ → ℝ≥0∞) p := by
    intro p
    have key : Qf a b c (n₁.1 * p.1 + n₂.1 * p.2, n₁.2 * p.1 + n₂.2 * p.2) = p.1 * p.2 :=
      Qf_null a b c n₁ n₂ h1 h2 h3 p.1 p.2
    by_cases hp : p.1 * p.2 = 0
    · rw [indicator_of_mem (show p ∈ {p : ℝ × ℝ | p.1 * p.2 = 0} from hp),
        indicator_of_mem (show (n₁.1 * p.1 + n₂.1 * p.2, n₁.2 * p.1 + n₂.2 * p.2)
          ∈ {w : ℝ × ℝ | Qf a b c w = 0} from key.trans hp)]
      simp only [Pi.one_apply]
    · rw [indicator_of_notMem (show p ∉ {p : ℝ × ℝ | p.1 * p.2 = 0} from hp),
        indicator_of_notMem (show (n₁.1 * p.1 + n₂.1 * p.2, n₁.2 * p.1 + n₂.2 * p.2)
          ∉ {w : ℝ × ℝ | Qf a b c w = 0} from fun h => hp (key.symm.trans h))]
  rw [lintegral_congr e,
    lintegral_indicator_one (measurableSet_eq_fun (measurable_fst.mul measurable_snd) measurable_const),
    volume_axes, mul_zero]

/-- `∫_{y>0} g(-y) dy = ∫_{y<0} g(y) dy`. -/
theorem setLIntegral_Ioi_neg (g : ℝ → ℝ≥0∞) :
    ∫⁻ y in Ioi (0 : ℝ), g (-y) = ∫⁻ y in Iio (0 : ℝ), g y := by
  rw [← lintegral_indicator measurableSet_Ioi, ← lintegral_indicator measurableSet_Iio,
    ← lintegral_comp_neg' ((Iio (0 : ℝ)).indicator g)]
  apply lintegral_congr
  intro y
  by_cases hy : 0 < y
  · rw [indicator_of_mem (show y ∈ Ioi (0 : ℝ) from hy),
      indicator_of_mem (show -y ∈ Iio (0 : ℝ) from neg_lt_zero.2 hy)]
  · rw [indicator_of_notMem (show y ∉ Ioi (0 : ℝ) from hy),
      indicator_of_notMem (show -y ∉ Iio (0 : ℝ) from fun h => hy (neg_lt_zero.1 h))]

/-- **Lemma 5.3, centred, in integrated form.** For densities `0 ≤ f_j ≤ 1` with `∫ f_j ≤ 1`, an indefinite form
`Q(w) = a w₁² + 2b w₁w₂ + c w₂²` (`D = b² - ac > 0`) and every measurable `φ ≥ 0`,
`∫ φ(Q(w)/√D) f₁(w₁) f₂(w₂) dw ≤ ∫ φ(y) h(y) dy` with `h(y) = 6 + log⁺(16/|y|)`. -/
theorem lemma53_centred (f₁ f₂ : ℝ → ℝ) (hf₁ : Measurable f₁) (hf₂ : Measurable f₂)
    (h0₁ : ∀ y, 0 ≤ f₁ y) (h1₁ : ∀ y, f₁ y ≤ 1) (h0₂ : ∀ y, 0 ≤ f₂ y) (h1₂ : ∀ y, f₂ y ≤ 1)
    (hi₁ : ∫⁻ y, ENNReal.ofReal (f₁ y) ≤ 1) (hi₂ : ∫⁻ y, ENNReal.ofReal (f₂ y) ≤ 1)
    (a b c : ℝ) (hD : 0 < b ^ 2 - a * c) (φ : ℝ → ℝ≥0∞) (hφ : Measurable φ) :
    ∫⁻ w : ℝ × ℝ, φ (Qf a b c w / √(b ^ 2 - a * c)) * ENNReal.ofReal (f₁ w.1 * f₂ w.2)
      ≤ ∫⁻ y, φ y * hY y := by
  have hQm : Measurable (Qf a b c) := by
    unfold Qf
    fun_prop
  have hQm' : Measurable (Qf (-a) (-b) (-c)) := by
    unfold Qf
    fun_prop
  have hneg : ∀ w, Qf (-a) (-b) (-c) w = -Qf a b c w := by
    intro w
    simp only [Qf]
    ring
  have hD' : 0 < (-b) ^ 2 - (-a) * (-c) := by
    have e : (-b) ^ 2 - (-a) * (-c) = b ^ 2 - a * c := by ring
    rw [e]
    exact hD
  obtain ⟨n₁, n₂, h1, h2, h3⟩ := null_pair a b c hD
  obtain ⟨m₁, m₂, k1, k2, k3⟩ := null_pair (-a) (-b) (-c) hD'
  have hdetn := det_null_pair a b c n₁ n₂ h1 h2 h3
  have hdetm : (m₁.1 * m₂.2 - m₂.1 * m₁.2) ^ 2 * (b ^ 2 - a * c) = 1 / 4 := by
    have h := det_null_pair (-a) (-b) (-c) m₁ m₂ k1 k2 k3
    have e : (-b) ^ 2 - (-a) * (-c) = b ^ 2 - a * c := by ring
    rw [e] at h
    exact h
  have hc1 := core_pos f₁ f₂ hf₁ hf₂ h0₁ h1₁ h0₂ h1₂ hi₁ hi₂ (Qf a b c) hQm (b ^ 2 - a * c) hD n₁ n₂ hdetn
    (Qf_null a b c n₁ n₂ h1 h2 h3) φ hφ
  have hc2 := core_pos f₁ f₂ hf₁ hf₂ h0₁ h1₁ h0₂ h1₂ hi₁ hi₂ (Qf (-a) (-b) (-c)) hQm' (b ^ 2 - a * c) hD m₁ m₂
    hdetm (Qf_null (-a) (-b) (-c) m₁ m₂ k1 k2 k3) (fun y => φ (-y)) (hφ.comp measurable_neg)
  have hF : Measurable fun w : ℝ × ℝ => ENNReal.ofReal (f₁ w.1 * f₂ w.2) :=
    ENNReal.measurable_ofReal.comp ((hf₁.comp measurable_fst).mul (hf₂.comp measurable_snd))
  have hT1 : Measurable fun w : ℝ × ℝ =>
      (Ioi (0 : ℝ)).indicator (fun x => φ (x / √(b ^ 2 - a * c))) (Qf a b c w)
        * ENNReal.ofReal (f₁ w.1 * f₂ w.2) :=
    (((hφ.comp (measurable_id.div_const _)).indicator measurableSet_Ioi).comp hQm).mul hF
  have hZ : MeasurableSet {w : ℝ × ℝ | Qf a b c w = 0} := measurableSet_eq_fun hQm measurable_const
  have hpt : ∀ w : ℝ × ℝ, φ (Qf a b c w / √(b ^ 2 - a * c)) * ENNReal.ofReal (f₁ w.1 * f₂ w.2)
      ≤ ((Ioi (0 : ℝ)).indicator (fun x => φ (x / √(b ^ 2 - a * c))) (Qf a b c w)
            * ENNReal.ofReal (f₁ w.1 * f₂ w.2)
          + (Ioi (0 : ℝ)).indicator (fun x => φ (-(x / √(b ^ 2 - a * c)))) (Qf (-a) (-b) (-c) w)
            * ENNReal.ofReal (f₁ w.1 * f₂ w.2))
        + {w : ℝ × ℝ | Qf a b c w = 0}.indicator (fun _ => ⊤) w := by
    intro w
    rcases lt_trichotomy (Qf a b c w) 0 with h | h | h
    · have h' : Qf (-a) (-b) (-c) w ∈ Ioi (0 : ℝ) := by
        rw [hneg w]
        exact neg_pos.2 h
      rw [indicator_of_mem h', indicator_of_notMem (show Qf a b c w ∉ Ioi (0 : ℝ) from not_lt.2 h.le),
        hneg w, neg_div, neg_neg, zero_mul, zero_add]
      exact le_self_add
    · have h' : w ∈ {w : ℝ × ℝ | Qf a b c w = 0} := h
      rw [indicator_of_mem h']
      simp
    · rw [indicator_of_mem (show Qf a b c w ∈ Ioi (0 : ℝ) from h)]
      exact le_self_add.trans le_self_add
  have hneg_int : ∫⁻ y in Ioi (0 : ℝ), φ (-y) * hY y = ∫⁻ y in Iio (0 : ℝ), φ y * hY y := by
    rw [← setLIntegral_Ioi_neg (fun y => φ y * hY y)]
    apply lintegral_congr
    intro y
    simp only [hY_even]
  have hsplit : (∫⁻ y in Ioi (0 : ℝ), φ y * hY y) + ∫⁻ y in Iio (0 : ℝ), φ y * hY y
      ≤ ∫⁻ y, φ y * hY y := by
    rw [← lintegral_union measurableSet_Iio
      (Set.disjoint_left.2 fun y h1 h2 => lt_asymm (mem_Ioi.1 h1) (mem_Iio.1 h2))]
    exact setLIntegral_le_lintegral _ _
  calc ∫⁻ w : ℝ × ℝ, φ (Qf a b c w / √(b ^ 2 - a * c)) * ENNReal.ofReal (f₁ w.1 * f₂ w.2)
      ≤ ∫⁻ w : ℝ × ℝ, (((Ioi (0 : ℝ)).indicator (fun x => φ (x / √(b ^ 2 - a * c))) (Qf a b c w)
            * ENNReal.ofReal (f₁ w.1 * f₂ w.2)
          + (Ioi (0 : ℝ)).indicator (fun x => φ (-(x / √(b ^ 2 - a * c)))) (Qf (-a) (-b) (-c) w)
            * ENNReal.ofReal (f₁ w.1 * f₂ w.2))
        + {w : ℝ × ℝ | Qf a b c w = 0}.indicator (fun _ => ⊤) w) := lintegral_mono hpt
    _ = (∫⁻ w : ℝ × ℝ, (Ioi (0 : ℝ)).indicator (fun x => φ (x / √(b ^ 2 - a * c))) (Qf a b c w)
            * ENNReal.ofReal (f₁ w.1 * f₂ w.2))
        + (∫⁻ w : ℝ × ℝ, (Ioi (0 : ℝ)).indicator (fun x => φ (-(x / √(b ^ 2 - a * c)))) (Qf (-a) (-b) (-c) w)
            * ENNReal.ofReal (f₁ w.1 * f₂ w.2))
        + ∫⁻ w : ℝ × ℝ, {w : ℝ × ℝ | Qf a b c w = 0}.indicator (fun _ => ⊤) w := by
      rw [lintegral_add_right _ (measurable_const.indicator hZ), lintegral_add_left hT1]
    _ ≤ (∫⁻ y in Ioi (0 : ℝ), φ y * hY y) + (∫⁻ y in Ioi (0 : ℝ), φ (-y) * hY y) + 0 := by
      rw [lintegral_indicator_const hZ, null_level a b c hD, mul_zero]
      exact add_le_add (add_le_add hc1 hc2) le_rfl
    _ ≤ ∫⁻ y, φ y * hY y := by
      rw [add_zero, hneg_int]
      exact hsplit

/-- **Lemma 5.3.** Let `W₁, W₂` be independent with densities `f₁, f₂ ≤ 1`, and `q(w) = (w - w₀)ᵀ B (w - w₀) + v`
with `B = [[a, b], [b, c]]` indefinite, `D = |det B| = b² - ac > 0`. Then `Y = (q(W) - v)/√D` has a density bounded
by `h(y) = 6 + log⁺(16/|y|)`; equivalently `q(W)` has a density bounded by `D^{-1/2}(6 + log⁺(16√D/|z - v|))`. This is
the form in which Lemma 5.6 consumes it (`ν ≤ volume.withDensity hY`). -/
theorem lemma53 (f₁ f₂ : ℝ → ℝ) (hf₁ : Measurable f₁) (hf₂ : Measurable f₂)
    (h0₁ : ∀ y, 0 ≤ f₁ y) (h1₁ : ∀ y, f₁ y ≤ 1) (h0₂ : ∀ y, 0 ≤ f₂ y) (h1₂ : ∀ y, f₂ y ≤ 1)
    (hi₁ : ∫⁻ y, ENNReal.ofReal (f₁ y) ≤ 1) (hi₂ : ∫⁻ y, ENNReal.ofReal (f₂ y) ≤ 1)
    (a b c x₀ y₀ : ℝ) (hD : 0 < b ^ 2 - a * c) :
    ((volume.withDensity fun y => ENNReal.ofReal (f₁ y)).prod
        (volume.withDensity fun y => ENNReal.ofReal (f₂ y))).map
        (fun w : ℝ × ℝ => Qf a b c (w.1 - x₀, w.2 - y₀) / √(b ^ 2 - a * c))
      ≤ volume.withDensity hY := by
  have hm₁ : Measurable fun y => ENNReal.ofReal (f₁ y) := ENNReal.measurable_ofReal.comp hf₁
  have hm₂ : Measurable fun y => ENNReal.ofReal (f₂ y) := ENNReal.measurable_ofReal.comp hf₂
  have hYm : Measurable fun w : ℝ × ℝ => Qf a b c (w.1 - x₀, w.2 - y₀) / √(b ^ 2 - a * c) := by
    unfold Qf
    fun_prop
  rw [prod_withDensity hm₁ hm₂, ← Measure.volume_eq_prod, Measure.le_iff]
  intro S hS
  rw [Measure.map_apply hYm hS, withDensity_apply _ (hYm hS), withDensity_apply _ hS,
    ← lintegral_indicator (hYm hS), ← lintegral_indicator hS]
  have e1 : ∀ w : ℝ × ℝ,
      ((fun w : ℝ × ℝ => Qf a b c (w.1 - x₀, w.2 - y₀) / √(b ^ 2 - a * c)) ⁻¹' S).indicator
          (fun z : ℝ × ℝ => ENNReal.ofReal (f₁ z.1) * ENNReal.ofReal (f₂ z.2)) w
        = S.indicator 1 (Qf a b c (w.1 - x₀, w.2 - y₀) / √(b ^ 2 - a * c))
          * ENNReal.ofReal (f₁ w.1 * f₂ w.2) := by
    intro w
    rw [ENNReal.ofReal_mul (h0₁ _)]
    by_cases hw : Qf a b c (w.1 - x₀, w.2 - y₀) / √(b ^ 2 - a * c) ∈ S
    · rw [indicator_of_mem (show w ∈ (fun w : ℝ × ℝ => Qf a b c (w.1 - x₀, w.2 - y₀) / √(b ^ 2 - a * c)) ⁻¹' S
          from hw), indicator_of_mem hw, Pi.one_apply, one_mul]
    · rw [indicator_of_notMem (show w ∉ (fun w : ℝ × ℝ => Qf a b c (w.1 - x₀, w.2 - y₀) / √(b ^ 2 - a * c)) ⁻¹' S
          from hw), indicator_of_notMem hw, zero_mul]
  have e2 : ∀ y : ℝ, S.indicator hY y = S.indicator 1 y * hY y := by
    intro y
    by_cases hy : y ∈ S
    · rw [indicator_of_mem hy, indicator_of_mem hy, Pi.one_apply, one_mul]
    · rw [indicator_of_notMem hy, indicator_of_notMem hy, zero_mul]
  have e3 : ∀ x : ℝ × ℝ,
      S.indicator 1 (Qf a b c ((((x₀, y₀) : ℝ × ℝ) + x).1 - x₀, (((x₀, y₀) : ℝ × ℝ) + x).2 - y₀)
          / √(b ^ 2 - a * c))
        * ENNReal.ofReal (f₁ (((x₀, y₀) : ℝ × ℝ) + x).1 * f₂ (((x₀, y₀) : ℝ × ℝ) + x).2)
      = S.indicator 1 (Qf a b c x / √(b ^ 2 - a * c)) * ENNReal.ofReal (f₁ (x₀ + x.1) * f₂ (y₀ + x.2)) := by
    intro x
    simp only [Prod.fst_add, Prod.snd_add, add_sub_cancel_left, Prod.mk.eta]
  have hi₁' : ∫⁻ y, ENNReal.ofReal (f₁ (x₀ + y)) ≤ 1 := by
    rw [lintegral_add_left_eq_self (fun y => ENNReal.ofReal (f₁ y)) x₀]
    exact hi₁
  have hi₂' : ∫⁻ y, ENNReal.ofReal (f₂ (y₀ + y)) ≤ 1 := by
    rw [lintegral_add_left_eq_self (fun y => ENNReal.ofReal (f₂ y)) y₀]
    exact hi₂
  calc _ = ∫⁻ w : ℝ × ℝ, S.indicator 1 (Qf a b c (w.1 - x₀, w.2 - y₀) / √(b ^ 2 - a * c))
          * ENNReal.ofReal (f₁ w.1 * f₂ w.2) := lintegral_congr e1
    _ = ∫⁻ x : ℝ × ℝ, S.indicator 1 (Qf a b c ((((x₀, y₀) : ℝ × ℝ) + x).1 - x₀,
            (((x₀, y₀) : ℝ × ℝ) + x).2 - y₀) / √(b ^ 2 - a * c))
          * ENNReal.ofReal (f₁ (((x₀, y₀) : ℝ × ℝ) + x).1 * f₂ (((x₀, y₀) : ℝ × ℝ) + x).2) :=
        (lintegral_add_left_eq_self (fun w : ℝ × ℝ => S.indicator 1 (Qf a b c (w.1 - x₀, w.2 - y₀)
          / √(b ^ 2 - a * c)) * ENNReal.ofReal (f₁ w.1 * f₂ w.2)) ((x₀, y₀) : ℝ × ℝ)).symm
    _ = ∫⁻ x : ℝ × ℝ, S.indicator 1 (Qf a b c x / √(b ^ 2 - a * c))
          * ENNReal.ofReal (f₁ (x₀ + x.1) * f₂ (y₀ + x.2)) := lintegral_congr e3
    _ ≤ ∫⁻ y, S.indicator 1 y * hY y :=
        lemma53_centred (fun y => f₁ (x₀ + y)) (fun y => f₂ (y₀ + y)) (hf₁.comp (measurable_const_add x₀))
          (hf₂.comp (measurable_const_add y₀)) (fun y => h0₁ _) (fun y => h1₁ _) (fun y => h0₂ _)
          (fun y => h1₂ _) hi₁' hi₂' a b c hD (S.indicator 1) (measurable_one.indicator hS)
    _ = _ := (lintegral_congr e2).symm



/-- The affine substitution `z = s y + v` on `ℝ` (`s > 0`): `∫ g(z) dz = ∫ s g(s y + v) dy`. -/
theorem lintegral_affine (s v : ℝ) (hs : 0 < s) (g : ℝ → ℝ≥0∞) :
    ∫⁻ z, g z = ∫⁻ y, ENNReal.ofReal s * g (s * y + v) := by
  have hderiv : ∀ x ∈ (univ : Set ℝ), HasDerivWithinAt (fun y : ℝ => s * y + v) s univ x := by
    intro x _
    have h := (((hasDerivAt_id' x).const_mul s).add_const v).hasDerivWithinAt (s := univ)
    simpa using h
  have hinj : InjOn (fun y : ℝ => s * y + v) univ := by
    intro x _ y _ hxy
    have h : s * x + v = s * y + v := hxy
    exact mul_left_cancel₀ hs.ne' (add_right_cancel h)
  have himage : (fun y : ℝ => s * y + v) '' univ = univ := by
    ext z
    simp only [mem_image, mem_univ, true_and, iff_true]
    exact ⟨(z - v) / s, by rw [mul_div_assoc', mul_div_cancel_left₀ _ hs.ne', sub_add_cancel]⟩
  have h := lintegral_image_eq_lintegral_abs_deriv_mul MeasurableSet.univ hderiv hinj g
  rw [himage, Measure.restrict_univ] at h
  rw [h]
  simp only [abs_of_pos hs]

/-- For `z ≠ v`, `D^{-1/2} h((z - v)/√D) = D^{-1/2}(6 + log⁺(16√D/|z - v|))`. -/
theorem density_value (D v z : ℝ) (hD : 0 < D) (hz : z ≠ v) :
    ENNReal.ofReal (√D)⁻¹ * hY ((z - v) / √D)
      = ENNReal.ofReal ((√D)⁻¹ * (6 + max 0 (Real.log (16 * √D / |z - v|)))) := by
  have hsD : 0 < √D := Real.sqrt_pos.2 hD
  have hne : (z - v) / √D ≠ 0 := div_ne_zero (sub_ne_zero.2 hz) hsD.ne'
  unfold hY
  rw [if_neg hne, abs_div, abs_of_pos hsD, div_div_eq_mul_div, ← ENNReal.ofReal_mul (inv_nonneg.2 hsD.le)]

/-- **Lemma 5.3 in the paper's form.** With `W₁, W₂` independent with densities `f₁, f₂ ≤ 1`, `B = [[a, b], [b, c]]`
indefinite and `D = |det B| = b² - ac > 0`, the variable `q(W) = (W - w₀)ᵀ B (W - w₀) + v` has a density bounded by
`D^{-1/2} h((z - v)/√D)`; for every `z ≠ v` this is `D^{-1/2}(6 + log⁺(16√D/|z - v|))` (`density_value`), and the
single point `z = v` is Lebesgue null. -/
theorem lemma53_paper (f₁ f₂ : ℝ → ℝ) (hf₁ : Measurable f₁) (hf₂ : Measurable f₂)
    (h0₁ : ∀ y, 0 ≤ f₁ y) (h1₁ : ∀ y, f₁ y ≤ 1) (h0₂ : ∀ y, 0 ≤ f₂ y) (h1₂ : ∀ y, f₂ y ≤ 1)
    (hi₁ : ∫⁻ y, ENNReal.ofReal (f₁ y) ≤ 1) (hi₂ : ∫⁻ y, ENNReal.ofReal (f₂ y) ≤ 1)
    (a b c x₀ y₀ v : ℝ) (hD : 0 < b ^ 2 - a * c) :
    ((volume.withDensity fun y => ENNReal.ofReal (f₁ y)).prod
        (volume.withDensity fun y => ENNReal.ofReal (f₂ y))).map
        (fun w : ℝ × ℝ => Qf a b c (w.1 - x₀, w.2 - y₀) + v)
      ≤ volume.withDensity
          (fun z => ENNReal.ofReal (√(b ^ 2 - a * c))⁻¹ * hY ((z - v) / √(b ^ 2 - a * c))) := by
  have hsD : 0 < √(b ^ 2 - a * c) := Real.sqrt_pos.2 hD
  have hYm : Measurable fun w : ℝ × ℝ => Qf a b c (w.1 - x₀, w.2 - y₀) / √(b ^ 2 - a * c) := by
    unfold Qf
    fun_prop
  have hA : Measurable fun y : ℝ => √(b ^ 2 - a * c) * y + v := by fun_prop
  have hcomp : (fun w : ℝ × ℝ => Qf a b c (w.1 - x₀, w.2 - y₀) + v)
      = (fun y : ℝ => √(b ^ 2 - a * c) * y + v)
        ∘ (fun w : ℝ × ℝ => Qf a b c (w.1 - x₀, w.2 - y₀) / √(b ^ 2 - a * c)) := by
    funext w
    simp only [Function.comp_apply]
    rw [mul_div_assoc', mul_div_cancel_left₀ _ hsD.ne']
  rw [hcomp, ← Measure.map_map hA hYm]
  refine (Measure.map_mono (lemma53 f₁ f₂ hf₁ hf₂ h0₁ h1₁ h0₂ h1₂ hi₁ hi₂ a b c x₀ y₀ hD) hA).trans ?_
  rw [Measure.le_iff]
  intro S hS
  rw [Measure.map_apply hA hS, withDensity_apply _ (hA hS), withDensity_apply _ hS,
    ← lintegral_indicator (hA hS), ← lintegral_indicator hS,
    lintegral_affine √(b ^ 2 - a * c) v hsD
      (S.indicator fun z => ENNReal.ofReal (√(b ^ 2 - a * c))⁻¹ * hY ((z - v) / √(b ^ 2 - a * c)))]
  apply le_of_eq
  apply lintegral_congr
  intro y
  by_cases hy : √(b ^ 2 - a * c) * y + v ∈ S
  · rw [indicator_of_mem (show y ∈ (fun y : ℝ => √(b ^ 2 - a * c) * y + v) ⁻¹' S from hy), indicator_of_mem hy,
      add_sub_cancel_right, mul_div_cancel_left₀ _ hsD.ne', ← mul_assoc, ← ENNReal.ofReal_mul hsD.le,
      mul_inv_cancel₀ hsD.ne', ENNReal.ofReal_one, one_mul]
  · rw [indicator_of_notMem (show y ∉ (fun y : ℝ => √(b ^ 2 - a * c) * y + v) ⁻¹' S from hy),
      indicator_of_notMem hy, mul_zero]


end Hyper

end QformFiveB
