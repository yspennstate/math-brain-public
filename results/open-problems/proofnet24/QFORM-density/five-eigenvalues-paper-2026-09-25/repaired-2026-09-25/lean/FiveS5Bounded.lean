import Mathlib.MeasureTheory.Measure.Prod
import Mathlib.MeasureTheory.Measure.Lebesgue.Basic
import Mathlib.MeasureTheory.Measure.Typeclasses.Probability
import Mathlib.MeasureTheory.Integral.Lebesgue.Basic
import Mathlib.Analysis.SpecialFunctions.ImproperIntegrals
import Mathlib.Analysis.SpecialFunctions.Pow.NNReal
import Mathlib.Analysis.SpecialFunctions.Sqrt
import Mathlib.Tactic

/-!
Display (5.6) in the proof of Lemma 5.6 of "Quadratic forms with five large singular values have bounded densities"
(repaired text, sha256 90f859b7): if a random variable `Z` has a density bounded by `M`, then for every real `a`
`E|Z - a|^{-1/2} = ∫_0^∞ P(|Z - a| < s^{-2}) ds ≤ ∫_0^∞ min{1, 2M s^{-2}} ds = 2√(2M)`.

The law of `Z` is a probability measure `ν ≤ M · Lebesgue`, and the expectation is taken in `[0, ∞]` with
`|0|^{-1/2} = ∞`, as in the paper (`bounded_halfmoment`). The layer-cake formula is Tonelli on the set
`{(z, s) : s > 0, s²|z - a| < 1}`, whose `z`-sections have Lebesgue measure `|z - a|^{-1/2}`
(`rpow_neg_half_eq_volume`) and whose `s`-sections have `ν`-measure at most `min{1, 2M s^{-2}}` (`slice_le`);
the last integral splits at `√(2M)` (`layer_integral_le`).
-/

open MeasureTheory Set
open scoped ENNReal

namespace QformFiveB

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

end QformFiveB
