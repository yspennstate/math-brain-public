import Mathlib.Analysis.SpecialFunctions.PolarCoord
import Mathlib.MeasureTheory.Function.JacobianOneDim
import Mathlib.MeasureTheory.Measure.Lebesgue.EqHaar
import Mathlib.MeasureTheory.Constructions.BorelSpace.Real
import Mathlib.LinearAlgebra.Matrix.ToLin
import Mathlib.MeasureTheory.Measure.Prod
import Mathlib.MeasureTheory.Measure.Lebesgue.Basic
import Mathlib.MeasureTheory.Measure.Typeclasses.Probability
import Mathlib.MeasureTheory.Integral.Lebesgue.Basic
import Mathlib.Analysis.SpecialFunctions.ImproperIntegrals
import Mathlib.Analysis.SpecialFunctions.Pow.NNReal
import Mathlib.Analysis.SpecialFunctions.Sqrt
import Mathlib.Analysis.Real.Pi.Bounds
import Mathlib.Tactic

/-!
Lemma 5.6 of "Quadratic forms with five large singular values have bounded densities" (repaired text,
sha256 90f859b7), the definite case, from its hypotheses: if `W = (W₁, W₂)` has independent coordinates with densities
at most one and the quadratic part of `q` is definite with `D = det B > 0`, then `E|q(W) - a|^{-1/2} ≤ 16 D^{-1/4}` for
every real `a` (`lemma56_definite_full`).

The chain is `prod_le_volume` (the joint law of two independent coordinates with densities at most one is at most
Lebesgue measure on the plane), Lemma 5.2 with `L = 1` (`lemma52`), and the bound (5.6) for a density bounded by
`π D^{-1/2}` (`lemma56_definite`, through `bounded_halfmoment`). Lemma 5.2 and its lemmas are repeated from
`FiveS5Definite.lean`, (5.6) from `FiveS5Bounded.lean`, and the last step from `FiveS5Pairhalf.lean`, so that this file
compiles on its own.
-/

open MeasureTheory Set Real
open scoped ENNReal

namespace QformFiveB

namespace DefHalf

/-- `x^{-1/2}` (in `[0, ∞]`, infinite at `0`) is the Lebesgue measure of `{s > 0 : s²x < 1}`. -/
theorem rpow_neg_half_eq_volume (x : ℝ) (hx : 0 ≤ x) :
    (ENNReal.ofReal x) ^ (-(1 / 2 : ℝ)) = volume {s : ℝ | 0 < s ∧ s ^ 2 * x < 1} := by
  rcases hx.eq_or_lt with h | h
  · subst h
    have e : {s : ℝ | 0 < s ∧ s ^ 2 * 0 < 1} = Ioi 0 := by
      ext s
      simp
    rw [e, Real.volume_Ioi, ENNReal.ofReal_zero, ENNReal.zero_rpow_of_neg (by norm_num)]
  · have hsx : 0 < Real.sqrt x := Real.sqrt_pos.2 h
    have hset : {s : ℝ | 0 < s ∧ s ^ 2 * x < 1} = Ioo 0 (1 / Real.sqrt x) := by
      ext s
      simp only [mem_setOf_eq, mem_Ioo]
      have key : s ^ 2 * x = (s * Real.sqrt x) ^ 2 := by
        rw [mul_pow, Real.sq_sqrt h.le]
      rw [key, lt_div_iff₀ hsx]
      constructor
      · rintro ⟨hs, h2⟩
        refine ⟨hs, ?_⟩
        have ht : 0 ≤ s * Real.sqrt x := mul_nonneg hs.le hsx.le
        nlinarith
      · rintro ⟨hs, h2⟩
        refine ⟨hs, ?_⟩
        have ht : 0 ≤ s * Real.sqrt x := mul_nonneg hs.le hsx.le
        nlinarith
    rw [hset, Real.volume_Ioo, sub_zero, ENNReal.ofReal_rpow_of_pos h]
    congr 1
    rw [Real.sqrt_eq_rpow, Real.rpow_neg h.le, inv_eq_one_div]

/-- `∫_{(c, ∞)} K s^{-2} ds = K/c` for `c > 0`, `K ≥ 0`. -/
theorem lintegral_Ioi_div_sq (c K : ℝ) (hc : 0 < c) (hK : 0 ≤ K) :
    ∫⁻ s in Ioi c, ENNReal.ofReal (K / s ^ 2) = ENNReal.ofReal (K / c) := by
  have hint : IntegrableOn (fun s : ℝ => K * s ^ (-2 : ℝ)) (Ioi c) :=
    (integrableOn_Ioi_rpow_of_lt (by norm_num) hc).const_mul K
  have heq : ∀ s ∈ Ioi c, ENNReal.ofReal (K / s ^ 2) = ENNReal.ofReal (K * s ^ (-2 : ℝ)) := by
    intro s hs
    have hs0 : 0 < s := hc.trans hs
    rw [Real.rpow_neg hs0.le, Real.rpow_two, div_eq_mul_inv]
  rw [setLIntegral_congr_fun measurableSet_Ioi heq,
    ← ofReal_integral_eq_lintegral_ofReal hint
      (ae_restrict_of_forall_mem measurableSet_Ioi
        (fun s hs => mul_nonneg hK (Real.rpow_nonneg (hc.trans hs).le _))),
    integral_const_mul, integral_Ioi_rpow_of_lt (by norm_num) hc]
  congr 1
  have e : (-2 : ℝ) + 1 = -1 := by norm_num
  rw [e, Real.rpow_neg_one]
  field_simp

/-- `√(2M) + 2M/√(2M) = 2√(2M)`. -/
theorem bounded_half_value' (M : ℝ) (hM : 0 < M) :
    Real.sqrt (2 * M) + 2 * M / Real.sqrt (2 * M) = 2 * Real.sqrt (2 * M) := by
  have hs : 0 < Real.sqrt (2 * M) := Real.sqrt_pos.mpr (by positivity)
  have h : Real.sqrt (2 * M) * Real.sqrt (2 * M) = 2 * M := Real.mul_self_sqrt (by positivity)
  field_simp
  linarith

/-- `∫_0^∞ min{1, 2M s^{-2}} ds ≤ 2√(2M)` (with equality, split at `s = √(2M)`). -/
theorem layer_integral_le (M : ℝ) (hM : 0 < M) :
    ∫⁻ s in Ioi (0 : ℝ), min 1 (ENNReal.ofReal (2 * M / s ^ 2)) ≤ ENNReal.ofReal (2 * Real.sqrt (2 * M)) := by
  have hs₀ : 0 < Real.sqrt (2 * M) := Real.sqrt_pos.2 (by positivity)
  rw [← Ioc_union_Ioi_eq_Ioi hs₀.le, lintegral_union measurableSet_Ioi Ioc_disjoint_Ioi_same]
  have h1 : ∫⁻ s in Ioc 0 (Real.sqrt (2 * M)), min 1 (ENNReal.ofReal (2 * M / s ^ 2))
      ≤ ENNReal.ofReal (Real.sqrt (2 * M)) := by
    calc ∫⁻ s in Ioc 0 (Real.sqrt (2 * M)), min 1 (ENNReal.ofReal (2 * M / s ^ 2))
        ≤ ∫⁻ _s in Ioc 0 (Real.sqrt (2 * M)), 1 := lintegral_mono (fun s => min_le_left _ _)
      _ = ENNReal.ofReal (Real.sqrt (2 * M)) := by
          rw [setLIntegral_const, one_mul, Real.volume_Ioc, sub_zero]
  have h2 : ∫⁻ s in Ioi (Real.sqrt (2 * M)), min 1 (ENNReal.ofReal (2 * M / s ^ 2))
      ≤ ENNReal.ofReal (2 * M / Real.sqrt (2 * M)) := by
    calc ∫⁻ s in Ioi (Real.sqrt (2 * M)), min 1 (ENNReal.ofReal (2 * M / s ^ 2))
        ≤ ∫⁻ s in Ioi (Real.sqrt (2 * M)), ENNReal.ofReal (2 * M / s ^ 2) :=
          lintegral_mono (fun s => min_le_right _ _)
      _ = ENNReal.ofReal (2 * M / Real.sqrt (2 * M)) := lintegral_Ioi_div_sq _ _ hs₀ (by positivity)
  calc _ ≤ ENNReal.ofReal (Real.sqrt (2 * M)) + ENNReal.ofReal (2 * M / Real.sqrt (2 * M)) := add_le_add h1 h2
    _ = ENNReal.ofReal (Real.sqrt (2 * M) + 2 * M / Real.sqrt (2 * M)) :=
        (ENNReal.ofReal_add hs₀.le (by positivity)).symm
    _ = ENNReal.ofReal (2 * Real.sqrt (2 * M)) := by rw [bounded_half_value' M hM]

/-- The `s`-section: `P(s > 0, s²|Z - a| < 1) ≤ min{1, 2M s^{-2}}` for `s > 0`, and `0` for `s ≤ 0`. -/
theorem slice_le (ν : Measure ℝ) [IsProbabilityMeasure ν] (M : ℝ) (hM : 0 < M)
    (hν : ν ≤ ENNReal.ofReal M • volume) (a s : ℝ) :
    ν {z | 0 < s ∧ s ^ 2 * |z - a| < 1}
      ≤ (Ioi (0 : ℝ)).indicator (fun s => min 1 (ENNReal.ofReal (2 * M / s ^ 2))) s := by
  rcases le_or_gt s 0 with hs | hs
  · have e : {z : ℝ | 0 < s ∧ s ^ 2 * |z - a| < 1} = ∅ := by
      ext z
      simp only [mem_setOf_eq, mem_empty_iff_false, iff_false, not_and]
      intro h
      linarith
    rw [e, measure_empty]
    exact zero_le _
  · rw [indicator_of_mem (show s ∈ Ioi (0 : ℝ) from hs)]
    refine le_min prob_le_one ?_
    have hs2 : 0 < s ^ 2 := by positivity
    have hsub : {z : ℝ | 0 < s ∧ s ^ 2 * |z - a| < 1} ⊆ Ioo (a - 1 / s ^ 2) (a + 1 / s ^ 2) := by
      intro z hz
      obtain ⟨_, h2⟩ := hz
      have h3 : |z - a| < 1 / s ^ 2 := by
        rw [lt_div_iff₀ hs2, mul_comm]
        exact h2
      rw [abs_lt] at h3
      exact ⟨by linarith, by linarith⟩
    calc ν {z : ℝ | 0 < s ∧ s ^ 2 * |z - a| < 1}
        ≤ (ENNReal.ofReal M • volume) {z : ℝ | 0 < s ∧ s ^ 2 * |z - a| < 1} := Measure.le_iff'.1 hν _
      _ = ENNReal.ofReal M * volume {z : ℝ | 0 < s ∧ s ^ 2 * |z - a| < 1} := by
          rw [Measure.smul_apply, smul_eq_mul]
      _ ≤ ENNReal.ofReal M * volume (Ioo (a - 1 / s ^ 2) (a + 1 / s ^ 2)) := by
          gcongr
      _ = ENNReal.ofReal (2 * M / s ^ 2) := by
          rw [Real.volume_Ioo, ← ENNReal.ofReal_mul hM.le]
          congr 1
          ring

/-- **Display (5.6) of Lemma 5.6.** If `Z` has a density bounded by `M`, then `E|Z - a|^{-1/2} ≤ 2√(2M)` for every
real `a`. -/
theorem bounded_halfmoment (ν : Measure ℝ) [IsProbabilityMeasure ν] (M : ℝ) (hM : 0 < M)
    (hν : ν ≤ ENNReal.ofReal M • volume) (a : ℝ) :
    ∫⁻ z, (ENNReal.ofReal |z - a|) ^ (-(1 / 2 : ℝ)) ∂ν ≤ ENNReal.ofReal (2 * Real.sqrt (2 * M)) := by
  have hq : Measurable (fun p : ℝ × ℝ => p.2 ^ 2 * |p.1 - a|) := by fun_prop
  have hE : MeasurableSet {p : ℝ × ℝ | 0 < p.2 ∧ p.2 ^ 2 * |p.1 - a| < 1} :=
    (measurableSet_lt measurable_const measurable_snd).inter (measurableSet_lt hq measurable_const)
  have h1 : ∫⁻ z, (ENNReal.ofReal |z - a|) ^ (-(1 / 2 : ℝ)) ∂ν
      = (ν.prod volume) {p : ℝ × ℝ | 0 < p.2 ∧ p.2 ^ 2 * |p.1 - a| < 1} := by
    rw [Measure.prod_apply hE]
    apply lintegral_congr
    intro z
    rw [rpow_neg_half_eq_volume _ (abs_nonneg _)]
    rfl
  rw [h1, Measure.prod_apply_symm hE]
  calc ∫⁻ s, ν ((fun z => (z, s)) ⁻¹' {p : ℝ × ℝ | 0 < p.2 ∧ p.2 ^ 2 * |p.1 - a| < 1})
      ≤ ∫⁻ s, (Ioi (0 : ℝ)).indicator (fun s => min 1 (ENNReal.ofReal (2 * M / s ^ 2))) s :=
        lintegral_mono (fun s => slice_le ν M hM hν a s)
    _ = ∫⁻ s in Ioi (0 : ℝ), min 1 (ENNReal.ofReal (2 * M / s ^ 2)) := lintegral_indicator measurableSet_Ioi _
    _ ≤ ENNReal.ofReal (2 * Real.sqrt (2 * M)) := layer_integral_le M hM

theorem measurable_sq_indicator (A : Set ℝ) (hA : MeasurableSet A) :
    Measurable fun r : ℝ => ENNReal.ofReal r * A.indicator 1 (r ^ 2) :=
  ENNReal.measurable_ofReal.mul ((measurable_one.indicator hA).comp (measurable_id.pow_const 2))

/-- The substitution `δ = r²` on `(0, ∞)`: `|A ∩ (0, ∞)| = 2 ∫_0^∞ r 1_A(r²) dr`. -/
theorem volume_sq_mem_half (A : Set ℝ) (hA : MeasurableSet A) :
    volume (A ∩ Ioi 0) = 2 * ∫⁻ r in Ioi (0 : ℝ), ENNReal.ofReal r * A.indicator 1 (r ^ 2) := by
  have hderiv : ∀ x ∈ Ioi (0 : ℝ), HasDerivWithinAt (fun r : ℝ => r ^ 2) (2 * x) (Ioi 0) x := by
    intro x _
    have h := (hasDerivAt_pow 2 x).hasDerivWithinAt (s := Ioi (0 : ℝ))
    simpa using h
  have hinj : InjOn (fun r : ℝ => r ^ 2) (Ioi 0) := by
    intro x hx y hy hxy
    exact (pow_left_inj₀ (le_of_lt hx) (le_of_lt hy) two_ne_zero).1 hxy
  have himage : (fun r : ℝ => r ^ 2) '' Ioi 0 = Ioi 0 := by
    ext y
    constructor
    · rintro ⟨x, hx, rfl⟩
      simp only [mem_Ioi] at hx ⊢
      positivity
    · intro hy
      exact ⟨√y, Real.sqrt_pos.2 hy, Real.sq_sqrt (le_of_lt hy)⟩
  have h := lintegral_image_eq_lintegral_abs_deriv_mul measurableSet_Ioi hderiv hinj (A.indicator 1)
  rw [himage] at h
  have hL : ∫⁻ x in Ioi (0 : ℝ), A.indicator 1 x = volume (A ∩ Ioi 0) := by
    rw [lintegral_indicator_one hA, Measure.restrict_apply hA]
  rw [hL] at h
  rw [h, ← lintegral_const_mul _ (measurable_sq_indicator A hA)]
  apply setLIntegral_congr_fun measurableSet_Ioi
  intro x hx
  have hx' : (0 : ℝ) < x := hx
  dsimp only
  rw [abs_of_pos (by linarith : (0 : ℝ) < 2 * x), ENNReal.ofReal_mul (by norm_num : (0 : ℝ) ≤ 2),
    ENNReal.ofReal_ofNat, mul_assoc]

/-- **Polar coordinates.** `|{u ∈ ℝ² : |u|² ∈ A}| = π |A ∩ (0, ∞)|`. -/
theorem volume_sq_norm_mem (A : Set ℝ) (hA : MeasurableSet A) :
    volume {p : ℝ × ℝ | p.1 ^ 2 + p.2 ^ 2 ∈ A} = ENNReal.ofReal π * volume (A ∩ Ioi 0) := by
  set S := {p : ℝ × ℝ | p.1 ^ 2 + p.2 ^ 2 ∈ A} with hS
  have hSm : MeasurableSet S :=
    (by fun_prop : Measurable fun p : ℝ × ℝ => p.1 ^ 2 + p.2 ^ 2) hA
  have hpt : ∀ p : ℝ × ℝ, S.indicator (1 : ℝ × ℝ → ℝ≥0∞) (polarCoord.symm p) = A.indicator 1 (p.1 ^ 2) := by
    intro p
    have hsymm : polarCoord.symm p = (p.1 * Real.cos p.2, p.1 * Real.sin p.2) := rfl
    have e : (p.1 * Real.cos p.2) ^ 2 + (p.1 * Real.sin p.2) ^ 2 = p.1 ^ 2 := by
      rw [mul_pow, mul_pow, ← mul_add, Real.cos_sq_add_sin_sq, mul_one]
    have hmem : polarCoord.symm p ∈ S ↔ p.1 ^ 2 ∈ A := by
      rw [hsymm, hS, mem_setOf_eq, e]
    by_cases h : p.1 ^ 2 ∈ A
    · rw [indicator_of_mem h, indicator_of_mem (hmem.2 h)]
      simp only [Pi.one_apply]
    · rw [indicator_of_notMem h, indicator_of_notMem (fun h' => h (hmem.1 h'))]
  have hpolar : ∫⁻ p : ℝ × ℝ, S.indicator 1 p
      = ∫⁻ p in Ioi (0 : ℝ) ×ˢ Ioo (-π) π, ENNReal.ofReal p.1 * A.indicator 1 (p.1 ^ 2) := by
    rw [← lintegral_comp_polarCoord_symm]
    apply setLIntegral_congr_fun (measurableSet_Ioi.prod measurableSet_Ioo)
    intro p _
    dsimp only
    rw [smul_eq_mul, hpt p]
  have hprod : ∫⁻ p in Ioi (0 : ℝ) ×ˢ Ioo (-π) π, ENNReal.ofReal p.1 * A.indicator 1 (p.1 ^ 2)
      = (∫⁻ r in Ioi (0 : ℝ), ENNReal.ofReal r * A.indicator 1 (r ^ 2)) * ENNReal.ofReal (2 * π) := by
    have e1 : (volume : Measure (ℝ × ℝ)).restrict (Ioi (0 : ℝ) ×ˢ Ioo (-π) π)
        = (volume.restrict (Ioi (0 : ℝ))).prod (volume.restrict (Ioo (-π) π)) := by
      rw [Measure.prod_restrict, ← Measure.volume_eq_prod]
    rw [e1]
    have e2 : (fun p : ℝ × ℝ => ENNReal.ofReal p.1 * A.indicator 1 (p.1 ^ 2))
        = fun p : ℝ × ℝ => (fun r : ℝ => ENNReal.ofReal r * A.indicator 1 (r ^ 2)) p.1
            * (fun _ : ℝ => (1 : ℝ≥0∞)) p.2 := by
      funext p
      simp only [mul_one]
    rw [e2, lintegral_prod_mul (measurable_sq_indicator A hA).aemeasurable aemeasurable_const]
    congr 1
    rw [setLIntegral_one, Real.volume_Ioo]
    congr 1
    ring
  calc volume S = ∫⁻ p : ℝ × ℝ, S.indicator 1 p := (lintegral_indicator_one hSm).symm
    _ = (∫⁻ r in Ioi (0 : ℝ), ENNReal.ofReal r * A.indicator 1 (r ^ 2)) * ENNReal.ofReal (2 * π) := by
        rw [hpolar, hprod]
    _ = ENNReal.ofReal π * volume (A ∩ Ioi 0) := by
        rw [volume_sq_mem_half A hA, ENNReal.ofReal_mul (by norm_num : (0 : ℝ) ≤ 2), ENNReal.ofReal_ofNat]
        ring

/-- **The linear change of variables.** For `a > 0` and `D = ac - b² > 0`,
`|{w : a w₁² + 2b w₁w₂ + c w₂² ∈ A}| = (π / √D) |A ∩ (0, ∞)|`: the map
`(w₁, w₂) ↦ (√a w₁ + (b/√a) w₂, √(D/a) w₂)` has determinant `√D` and turns the form into `u₁² + u₂²`. -/
theorem volume_quad_mem (a b c : ℝ) (ha : 0 < a) (hD : 0 < a * c - b ^ 2) (A : Set ℝ) (hA : MeasurableSet A) :
    volume {p : ℝ × ℝ | a * p.1 ^ 2 + 2 * b * p.1 * p.2 + c * p.2 ^ 2 ∈ A}
      = ENNReal.ofReal (π / √(a * c - b ^ 2)) * volume (A ∩ Ioi 0) := by
  set D := a * c - b ^ 2 with hDdef
  have hsa : 0 < √a := Real.sqrt_pos.2 ha
  set T : ℝ × ℝ →ₗ[ℝ] ℝ × ℝ :=
    Matrix.toLin (Module.Basis.finTwoProd ℝ) (Module.Basis.finTwoProd ℝ) !![√a, b / √a; 0, √(D / a)] with hT
  have hdetT : LinearMap.det T = √D := by
    rw [hT, LinearMap.det_toLin, Matrix.det_fin_two_of, mul_zero, sub_zero, ← Real.sqrt_mul ha.le,
      mul_div_cancel₀ _ ha.ne']
  have hTapply : ∀ p : ℝ × ℝ, T p = (√a * p.1 + b / √a * p.2, 0 * p.1 + √(D / a) * p.2) :=
    fun p => Matrix.toLin_finTwoProd_apply _ _ _ _ p
  have hset : {p : ℝ × ℝ | a * p.1 ^ 2 + 2 * b * p.1 * p.2 + c * p.2 ^ 2 ∈ A}
      = T ⁻¹' {u : ℝ × ℝ | u.1 ^ 2 + u.2 ^ 2 ∈ A} := by
    ext p
    simp only [mem_setOf_eq, mem_preimage, hTapply]
    have h1 : √a ^ 2 = a := Real.sq_sqrt ha.le
    have h2 : √(D / a) ^ 2 = D / a := Real.sq_sqrt (div_nonneg hD.le ha.le)
    have h3 : √a * (b / √a) = b := by field_simp
    have h4 : (b / √a) ^ 2 = b ^ 2 / a := by rw [div_pow, h1]
    have e : (√a * p.1 + b / √a * p.2) ^ 2 + (0 * p.1 + √(D / a) * p.2) ^ 2
        = a * p.1 ^ 2 + 2 * b * p.1 * p.2 + c * p.2 ^ 2 := by
      calc (√a * p.1 + b / √a * p.2) ^ 2 + (0 * p.1 + √(D / a) * p.2) ^ 2
          = √a ^ 2 * p.1 ^ 2 + 2 * (√a * (b / √a)) * p.1 * p.2 + (b / √a) ^ 2 * p.2 ^ 2
            + √(D / a) ^ 2 * p.2 ^ 2 := by ring
        _ = a * p.1 ^ 2 + 2 * b * p.1 * p.2 + b ^ 2 / a * p.2 ^ 2 + D / a * p.2 ^ 2 := by
            rw [h1, h3, h4, h2]
        _ = a * p.1 ^ 2 + 2 * b * p.1 * p.2 + c * p.2 ^ 2 := by
            rw [hDdef]
            field_simp
            ring
    rw [e]
  have hdet0 : LinearMap.det T ≠ 0 := by
    rw [hdetT]
    exact (Real.sqrt_pos.2 hD).ne'
  rw [hset, MeasureTheory.Measure.addHaar_preimage_linearMap (μ := volume) hdet0, volume_sq_norm_mem A hA, hdetT,
    abs_of_pos (inv_pos.2 (Real.sqrt_pos.2 hD)), ← mul_assoc,
    ← ENNReal.ofReal_mul (inv_nonneg.2 (Real.sqrt_nonneg _)), inv_mul_eq_div]

/-- The quadratic polynomial `a w₁² + 2b w₁w₂ + c w₂² + d w₁ + e w₂ + f` on `ℝ²`; its quadratic part has matrix
`B = [[a, b], [b, c]]`. -/
def quad (a b c d e f : ℝ) (w : ℝ × ℝ) : ℝ :=
  a * w.1 ^ 2 + 2 * b * w.1 * w.2 + c * w.2 ^ 2 + d * w.1 + e * w.2 + f

theorem quad_measurable (a b c d e f : ℝ) : Measurable (quad a b c d e f) := by
  unfold quad
  fun_prop

/-- The expansion of `quad` about a point `(x₀, y₀)`. -/
theorem quad_expand (a b c d e f x0 y0 : ℝ) (w : ℝ × ℝ) :
    quad a b c d e f w = a * (w.1 - x0) ^ 2 + 2 * b * (w.1 - x0) * (w.2 - y0) + c * (w.2 - y0) ^ 2
      + (2 * a * x0 + 2 * b * y0 + d) * (w.1 - x0) + (2 * b * x0 + 2 * c * y0 + e) * (w.2 - y0)
      + quad a b c d e f (x0, y0) := by
  unfold quad
  ring

/-- **Lemma 5.2, positive definite case.** -/
theorem lemma52_pos (ν : Measure (ℝ × ℝ)) (L : ℝ) (hL : 0 ≤ L) (hν : ν ≤ ENNReal.ofReal L • volume)
    (a b c d e f : ℝ) (ha : 0 < a) (hD : 0 < a * c - b ^ 2) :
    ν.map (quad a b c d e f) ≤ ENNReal.ofReal (π * L / √(a * c - b ^ 2)) • volume := by
  set D := a * c - b ^ 2 with hDdef
  have hD0 : D ≠ 0 := hD.ne'
  set x0 := (b * e - c * d) / (2 * D) with hx0
  set y0 := (b * d - a * e) / (2 * D) with hy0
  set v := quad a b c d e f (x0, y0) with hv
  have hg1 : 2 * a * x0 + 2 * b * y0 + d = 0 := by
    rw [hx0, hy0]
    field_simp
    rw [hDdef]
    ring
  have hg2 : 2 * b * x0 + 2 * c * y0 + e = 0 := by
    rw [hx0, hy0]
    field_simp
    rw [hDdef]
    ring
  have hq : ∀ w : ℝ × ℝ, quad a b c d e f w
      = a * (w.1 + -x0) ^ 2 + 2 * b * (w.1 + -x0) * (w.2 + -y0) + c * (w.2 + -y0) ^ 2 + v := by
    intro w
    rw [quad_expand a b c d e f x0 y0 w, hg1, hg2, ← sub_eq_add_neg, ← sub_eq_add_neg]
    ring
  rw [Measure.le_iff]
  intro S hS
  rw [Measure.map_apply (quad_measurable _ _ _ _ _ _) hS, Measure.smul_apply, smul_eq_mul]
  set A := (fun z : ℝ => z + v) ⁻¹' S with hAdef
  have hA : MeasurableSet A := (measurable_add_const v) hS
  have hset : quad a b c d e f ⁻¹' S
      = (fun w : ℝ × ℝ => w + (-x0, -y0)) ⁻¹' {p : ℝ × ℝ | a * p.1 ^ 2 + 2 * b * p.1 * p.2 + c * p.2 ^ 2 ∈ A} := by
    ext w
    simp only [mem_preimage, mem_setOf_eq, Prod.fst_add, Prod.snd_add, hAdef, hq w]
  have hvol : volume (quad a b c d e f ⁻¹' S) ≤ ENNReal.ofReal (π / √D) * volume S := by
    rw [hset, measure_preimage_add_right, volume_quad_mem a b c ha hD A hA]
    have h1 : volume (A ∩ Ioi 0) ≤ volume A := measure_mono inter_subset_left
    have h2 : volume A = volume S := by
      rw [hAdef]
      exact measure_preimage_add_right _ v S
    calc ENNReal.ofReal (π / √D) * volume (A ∩ Ioi 0) ≤ ENNReal.ofReal (π / √D) * volume A := by gcongr
      _ = ENNReal.ofReal (π / √D) * volume S := by rw [h2]
  calc ν (quad a b c d e f ⁻¹' S) ≤ (ENNReal.ofReal L • volume) (quad a b c d e f ⁻¹' S) := hν _
    _ = ENNReal.ofReal L * volume (quad a b c d e f ⁻¹' S) := by rw [Measure.smul_apply, smul_eq_mul]
    _ ≤ ENNReal.ofReal L * (ENNReal.ofReal (π / √D) * volume S) := by gcongr
    _ = ENNReal.ofReal (π * L / √D) * volume S := by
        rw [← mul_assoc, ← ENNReal.ofReal_mul hL]
        congr 2
        ring

/-- **Lemma 5.2.** If `Law(W) ≤ L · Lebesgue` on `ℝ²` and the quadratic part `B = [[a, b], [b, c]]` of `q` is definite
(`det B = ac - b² > 0`), then `Law(q(W)) ≤ (π L / √(det B)) · Lebesgue`. -/
theorem lemma52 (ν : Measure (ℝ × ℝ)) (L : ℝ) (hL : 0 ≤ L) (hν : ν ≤ ENNReal.ofReal L • volume)
    (a b c d e f : ℝ) (hD : 0 < a * c - b ^ 2) :
    ν.map (quad a b c d e f) ≤ ENNReal.ofReal (π * L / √(a * c - b ^ 2)) • volume := by
  have ha0 : a ≠ 0 := by
    rintro rfl
    nlinarith [sq_nonneg b]
  rcases lt_or_gt_of_ne ha0 with ha | ha
  · have hD' : 0 < (-a) * (-c) - (-b) ^ 2 := by nlinarith
    have h := lemma52_pos ν L hL hν (-a) (-b) (-c) (-d) (-e) (-f) (by linarith) hD'
    have e1 : (-a) * (-c) - (-b) ^ 2 = a * c - b ^ 2 := by ring
    rw [e1] at h
    have hq : ∀ w : ℝ × ℝ, quad a b c d e f w = -1 * quad (-a) (-b) (-c) (-d) (-e) (-f) w := by
      intro w
      unfold quad
      ring
    rw [Measure.le_iff]
    intro S hS
    set T := (fun x : ℝ => -1 * x) ⁻¹' S with hT
    have hTm : MeasurableSet T := (by fun_prop : Measurable fun x : ℝ => -1 * x) hS
    have hset : quad a b c d e f ⁻¹' S = quad (-a) (-b) (-c) (-d) (-e) (-f) ⁻¹' T := by
      ext w
      simp only [mem_preimage, hT, hq w]
    have hvolT : volume T = volume S := by
      rw [hT, Real.volume_preimage_mul_left (by norm_num : (-1 : ℝ) ≠ 0)]
      simp
    rw [Measure.map_apply (quad_measurable _ _ _ _ _ _) hS, hset,
      ← Measure.map_apply (quad_measurable _ _ _ _ _ _) hTm]
    calc (ν.map (quad (-a) (-b) (-c) (-d) (-e) (-f))) T
        ≤ (ENNReal.ofReal (π * L / √(a * c - b ^ 2)) • volume) T := Measure.le_iff.1 h T hTm
      _ = (ENNReal.ofReal (π * L / √(a * c - b ^ 2)) • volume) S := by
          rw [Measure.smul_apply, Measure.smul_apply, hvolT]
  · exact lemma52_pos ν L hL hν a b c d e f ha hD

/-- `2√(2π) < 6`. -/
theorem pairhalf_definite_const : 2 * √(2 * Real.pi) < 6 := by
  have hpi := Real.pi_lt_d2
  have h : √(2 * Real.pi) < 3 := by
    rw [show (3 : ℝ) = √9 by rw [show (9 : ℝ) = 3 ^ 2 by norm_num]; exact (Real.sqrt_sq (by norm_num)).symm]
    exact Real.sqrt_lt_sqrt (by positivity) (by norm_num at hpi ⊢; linarith)
  linarith

/-- **Lemma 5.6, the definite case, in the form used.** If `q(W)` has a density bounded by `π D^{-1/2}` (Lemma 5.2),
then `E|q(W) - a|^{-1/2} ≤ 2√(2π) D^{-1/4} < 6 D^{-1/4} ≤ 16 D^{-1/4}` for every `a`. -/
theorem lemma56_definite (μ : Measure ℝ) [IsProbabilityMeasure μ] (D a : ℝ) (hD : 0 < D)
    (hμ : μ ≤ ENNReal.ofReal (Real.pi / √D) • volume) :
    ∫⁻ z, (ENNReal.ofReal |z - a|) ^ (-(1 / 2 : ℝ)) ∂μ ≤ ENNReal.ofReal (16 * D ^ (-(1 / 4 : ℝ))) := by
  have hs : 0 < √D := Real.sqrt_pos.2 hD
  have hM : 0 < Real.pi / √D := div_pos Real.pi_pos hs
  refine (bounded_halfmoment μ _ hM hμ a).trans (ENNReal.ofReal_le_ofReal ?_)
  have hD4 : 0 < D ^ (-(1 / 4 : ℝ)) := Real.rpow_pos_of_pos hD _
  have hq : √(√D) = D ^ (1 / 4 : ℝ) := by
    rw [Real.sqrt_eq_rpow, Real.sqrt_eq_rpow, ← Real.rpow_mul hD.le]
    norm_num
  have e : √(2 * (Real.pi / √D)) = √(2 * Real.pi) * D ^ (-(1 / 4 : ℝ)) := by
    rw [← mul_div_assoc, Real.sqrt_div (show (0 : ℝ) ≤ 2 * Real.pi by positivity) (√D), hq,
      Real.rpow_neg hD.le, div_eq_mul_inv]
  rw [e]
  nlinarith [pairhalf_definite_const]

/-- Two independent coordinates with densities at most one have a joint law at most Lebesgue measure on the plane. -/
theorem prod_le_volume (μ₁ μ₂ : Measure ℝ) [SFinite μ₁] [SFinite μ₂] (h₁ : μ₁ ≤ volume) (h₂ : μ₂ ≤ volume) :
    μ₁.prod μ₂ ≤ (volume : Measure (ℝ × ℝ)) := by
  rw [Measure.le_iff]
  intro s hs
  rw [Measure.prod_apply hs, Measure.volume_eq_prod, Measure.prod_apply hs]
  calc ∫⁻ x, μ₂ (Prod.mk x ⁻¹' s) ∂μ₁ ≤ ∫⁻ x, volume (Prod.mk x ⁻¹' s) ∂μ₁ :=
        lintegral_mono (fun x => h₂ _)
    _ ≤ ∫⁻ x, volume (Prod.mk x ⁻¹' s) ∂volume := lintegral_mono' h₁ le_rfl

/-- **Lemma 5.6, the definite case, from its hypotheses.** If `W = (W₁, W₂)` has independent coordinates with densities
at most one and the quadratic part `B = [[a, b], [b, c]]` of `q` is definite (`D = ac - b² > 0`), then
`E|q(W) - a₀|^{-1/2} ≤ 16 D^{-1/4}` for every real `a₀`. -/
theorem lemma56_definite_full (μ₁ μ₂ : Measure ℝ) [IsProbabilityMeasure μ₁] [IsProbabilityMeasure μ₂]
    (h₁ : μ₁ ≤ volume) (h₂ : μ₂ ≤ volume) (a b c d e f a₀ : ℝ) (hD : 0 < a * c - b ^ 2) :
    ∫⁻ w, (ENNReal.ofReal |quad a b c d e f w - a₀|) ^ (-(1 / 2 : ℝ)) ∂(μ₁.prod μ₂)
      ≤ ENNReal.ofReal (16 * (a * c - b ^ 2) ^ (-(1 / 4 : ℝ))) := by
  have hν : μ₁.prod μ₂ ≤ ENNReal.ofReal 1 • volume := by
    rw [ENNReal.ofReal_one, one_smul]
    exact prod_le_volume μ₁ μ₂ h₁ h₂
  have h52 := lemma52 (μ₁.prod μ₂) 1 zero_le_one hν a b c d e f hD
  rw [mul_one] at h52
  haveI : IsProbabilityMeasure ((μ₁.prod μ₂).map (quad a b c d e f)) :=
    Measure.isProbabilityMeasure_map (quad_measurable a b c d e f).aemeasurable
  have h56 := lemma56_definite ((μ₁.prod μ₂).map (quad a b c d e f)) (a * c - b ^ 2) a₀ hD h52
  rw [lintegral_map (by fun_prop : Measurable fun z : ℝ => (ENNReal.ofReal |z - a₀|) ^ (-(1 / 2 : ℝ)))
    (quad_measurable a b c d e f)] at h56
  exact h56

end DefHalf

end QformFiveB
