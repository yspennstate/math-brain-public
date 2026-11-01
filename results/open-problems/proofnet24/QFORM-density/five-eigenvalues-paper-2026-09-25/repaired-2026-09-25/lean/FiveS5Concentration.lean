import Mathlib.MeasureTheory.Measure.Prod
import Mathlib.MeasureTheory.Measure.Lebesgue.Basic
import Mathlib.MeasureTheory.Measure.Typeclasses.Probability
import Mathlib.MeasureTheory.Group.Measure
import Mathlib.MeasureTheory.Integral.Lebesgue.Basic
import Mathlib.Analysis.SpecialFunctions.ImproperIntegrals
import Mathlib.Analysis.SpecialFunctions.Sqrt
import Mathlib.Analysis.SpecialFunctions.Log.Basic
import Mathlib.Analysis.Complex.ExponentialBounds
import Mathlib.Tactic

/-!
Lemma 5.4 of "Quadratic forms with five large singular values have bounded densities" (repaired text, sha256 90f859b7),
the parts that do not use the Fourier bound: for `R = XᵀSX + bᵀX + c`,

* the diagonal case of (5.2): if `|S_ii| ≥ L/2`, then conditionally on the other coordinates `R` is a quadratic in `X_i`
  with leading coefficient `S_ii`, and `P(|R - a| < ρ) ≤ 2√(2ρ/|S_ii|) ≤ 4√(ρ/L)` (`lemma54_diag_prob`,
  `lemma54_diag_const`), by Lemma 5.1 for each value of the other coordinates and Tonelli;
* (5.3): if `P(|R - a| < ρ) ≤ 19√(ρ/L)` for all `ρ > 0` and `L ≥ 1`, then `E log₊(1/|R - a|) ≤ L₀ = 2 + 2 log 19 < 8`
  (`lemma54_logmoment`, `L0_lt_eight'`), with `log₊(1/|0|) = ∞` as in the paper, by the layer-cake formula:
  `E log₊(1/|R - a|) = ∫_0^∞ P(|R - a| < e^{-τ}) dτ ≤ ∫_0^∞ min{1, 19 e^{-τ/2}} dτ = 2 log 19 + 2`.

The second assertion of Lemma 5.1 and the layer-cake formula are repeated from `FiveS5Square.lean` and
`FiveS5Rearrange.lean`.
-/

open MeasureTheory Set
open scoped ENNReal

namespace QformFiveB

namespace Concentration

/-! ### Repeated: Lemma 5.1, second assertion -/

/-- `√(x + δ) ≤ √x + √δ` for `x, δ ≥ 0`. -/
theorem sqrt_add_le_add (x δ : ℝ) (hx : 0 ≤ x) (hδ : 0 ≤ δ) :
    Real.sqrt (x + δ) ≤ Real.sqrt x + Real.sqrt δ := by
  rw [Real.sqrt_le_left (by positivity)]
  have h1 := Real.sq_sqrt hx
  have h2 := Real.sq_sqrt hδ
  nlinarith [Real.sqrt_nonneg x, Real.sqrt_nonneg δ, mul_nonneg (Real.sqrt_nonneg x) (Real.sqrt_nonneg δ)]

/-- `{s : s² ∈ [u, u + δ]}` has measure at most `2√δ`. -/
theorem measure_sq_mem_Icc_le (u δ : ℝ) (hδ : 0 ≤ δ) :
    volume {s : ℝ | s ^ 2 ∈ Icc u (u + δ)} ≤ ENNReal.ofReal (2 * Real.sqrt δ) := by
  have hsub : {s : ℝ | s ^ 2 ∈ Icc u (u + δ)}
      ⊆ Icc (-Real.sqrt (u + δ)) (-Real.sqrt (max u 0)) ∪ Icc (Real.sqrt (max u 0)) (Real.sqrt (u + δ)) := by
    intro s hs
    obtain ⟨h1, h2⟩ := hs
    have habs : |s| = Real.sqrt (s ^ 2) := (Real.sqrt_sq_eq_abs s).symm
    have hup : |s| ≤ Real.sqrt (u + δ) := by rw [habs]; exact Real.sqrt_le_sqrt h2
    have hlo : Real.sqrt (max u 0) ≤ |s| := by rw [habs]; exact Real.sqrt_le_sqrt (max_le h1 (sq_nonneg s))
    rcases le_or_gt 0 s with hs0 | hs0
    · right
      rw [abs_of_nonneg hs0] at hup hlo
      exact ⟨hlo, hup⟩
    · left
      rw [abs_of_neg hs0] at hup hlo
      exact ⟨by linarith, by linarith⟩
  have hHL : Real.sqrt (u + δ) - Real.sqrt (max u 0) ≤ Real.sqrt δ := by
    have h1 : Real.sqrt (u + δ) ≤ Real.sqrt (max u 0 + δ) := Real.sqrt_le_sqrt (by linarith [le_max_left u 0])
    have h2 := sqrt_add_le_add (max u 0) δ (le_max_right u 0) hδ
    linarith
  have hof : ENNReal.ofReal (Real.sqrt (u + δ) - Real.sqrt (max u 0)) ≤ ENNReal.ofReal (Real.sqrt δ) :=
    ENNReal.ofReal_le_ofReal hHL
  calc volume {s : ℝ | s ^ 2 ∈ Icc u (u + δ)}
      ≤ volume (Icc (-Real.sqrt (u + δ)) (-Real.sqrt (max u 0)) ∪
          Icc (Real.sqrt (max u 0)) (Real.sqrt (u + δ))) := measure_mono hsub
    _ ≤ volume (Icc (-Real.sqrt (u + δ)) (-Real.sqrt (max u 0))) +
          volume (Icc (Real.sqrt (max u 0)) (Real.sqrt (u + δ))) := measure_union_le _ _
    _ = ENNReal.ofReal (Real.sqrt (u + δ) - Real.sqrt (max u 0)) +
          ENNReal.ofReal (Real.sqrt (u + δ) - Real.sqrt (max u 0)) := by
        rw [Real.volume_Icc, Real.volume_Icc,
          show -Real.sqrt (max u 0) - -Real.sqrt (u + δ) = Real.sqrt (u + δ) - Real.sqrt (max u 0) by ring]
    _ ≤ ENNReal.ofReal (Real.sqrt δ) + ENNReal.ofReal (Real.sqrt δ) := add_le_add hof hof
    _ = ENNReal.ofReal (2 * Real.sqrt δ) := by
        rw [← ENNReal.ofReal_add (Real.sqrt_nonneg δ) (Real.sqrt_nonneg δ), two_mul]

/-- **Lemma 5.1, second assertion.** For `a ≠ 0` and `ρ ≥ 0`, `{y : a y² + β y + γ ∈ [c, c + 2ρ]}` has Lebesgue measure at
most `2√(2ρ/|a|)`. -/
theorem lemma51b (a β γ c ρ : ℝ) (ha : a ≠ 0) (hρ : 0 ≤ ρ) :
    volume {y : ℝ | a * y ^ 2 + β * y + γ ∈ Icc c (c + 2 * ρ)}
      ≤ ENNReal.ofReal (2 * Real.sqrt (2 * ρ / |a|)) := by
  have hsq : ∀ y, a * y ^ 2 + β * y + γ = a * (y + β / (2 * a)) ^ 2 + (γ - β ^ 2 / (4 * a)) := by
    intro y
    field_simp
    ring
  have hshift : {y : ℝ | a * y ^ 2 + β * y + γ ∈ Icc c (c + 2 * ρ)}
      = (fun y => y + β / (2 * a)) ⁻¹' {s : ℝ | a * s ^ 2 + (γ - β ^ 2 / (4 * a)) ∈ Icc c (c + 2 * ρ)} := by
    ext y
    simp only [mem_setOf_eq, mem_preimage, hsq]
  rw [hshift, measure_preimage_add_right]
  set k := γ - β ^ 2 / (4 * a) with hk
  have hδ : 0 ≤ 2 * ρ / |a| := by positivity
  rcases lt_or_gt_of_ne ha with hneg | hpos
  · have habs : |a| = -a := abs_of_neg hneg
    refine (measure_mono (fun s hs => ?_)).trans (measure_sq_mem_Icc_le ((c + 2 * ρ - k) / a) (2 * ρ / |a|) hδ)
    obtain ⟨h1, h2⟩ := hs
    refine ⟨?_, ?_⟩
    · rw [div_le_iff_of_neg hneg]
      linarith
    · have e : (c + 2 * ρ - k) / a + 2 * ρ / |a| = (c - k) / a := by
        rw [habs]
        field_simp
        ring
      rw [e, le_div_iff_of_neg hneg]
      linarith
  · have habs : |a| = a := abs_of_pos hpos
    refine (measure_mono (fun s hs => ?_)).trans (measure_sq_mem_Icc_le ((c - k) / a) (2 * ρ / |a|) hδ)
    obtain ⟨h1, h2⟩ := hs
    refine ⟨?_, ?_⟩
    · rw [div_le_iff₀ hpos]
      linarith
    · have e : (c - k) / a + 2 * ρ / |a| = (c + 2 * ρ - k) / a := by
        rw [habs]
        field_simp
        ring
      rw [e, le_div_iff₀ hpos]
      linarith

/-! ### Repeated: the layer-cake formula -/

/-- `c ∈ [0, ∞]` is the Lebesgue measure of `{τ > 0 : τ < c}`. -/
theorem ennreal_eq_volume (c : ℝ≥0∞) : c = volume {τ : ℝ | 0 < τ ∧ ENNReal.ofReal τ < c} := by
  rcases eq_or_ne c ⊤ with rfl | hc
  · have e : {τ : ℝ | 0 < τ ∧ ENNReal.ofReal τ < ⊤} = Ioi 0 := by
      ext τ
      simp
    rw [e, Real.volume_Ioi]
  · have e : {τ : ℝ | 0 < τ ∧ ENNReal.ofReal τ < c} = Ioo 0 c.toReal := by
      ext τ
      simp only [mem_setOf_eq, mem_Ioo]
      constructor
      · rintro ⟨h0, h1⟩
        exact ⟨h0, (ENNReal.ofReal_lt_iff_lt_toReal h0.le hc).1 h1⟩
      · rintro ⟨h0, h1⟩
        exact ⟨h0, (ENNReal.ofReal_lt_iff_lt_toReal h0.le hc).2 h1⟩
    rw [e, Real.volume_Ioo, sub_zero, ENNReal.ofReal_toReal hc]

/-- The layer-cake formula `∫ F dμ = ∫_0^∞ μ{F > τ} dτ`, by Tonelli. -/
theorem lintegral_layer (μ : Measure ℝ) [SFinite μ] (F : ℝ → ℝ≥0∞) (hF : Measurable F) :
    ∫⁻ y, F y ∂μ = ∫⁻ τ in Ioi 0, μ {y | ENNReal.ofReal τ < F y} := by
  have hE : MeasurableSet {p : ℝ × ℝ | 0 < p.2 ∧ ENNReal.ofReal p.2 < F p.1} :=
    (measurableSet_lt measurable_const measurable_snd).inter
      (measurableSet_lt (ENNReal.measurable_ofReal.comp measurable_snd) (hF.comp measurable_fst))
  calc ∫⁻ y, F y ∂μ
      = ∫⁻ y, volume (Prod.mk y ⁻¹' {p : ℝ × ℝ | 0 < p.2 ∧ ENNReal.ofReal p.2 < F p.1}) ∂μ := by
        apply lintegral_congr
        intro y
        exact ennreal_eq_volume (F y)
    _ = (μ.prod volume) {p : ℝ × ℝ | 0 < p.2 ∧ ENNReal.ofReal p.2 < F p.1} := (Measure.prod_apply hE).symm
    _ = ∫⁻ τ, μ ((fun y => (y, τ)) ⁻¹' {p : ℝ × ℝ | 0 < p.2 ∧ ENNReal.ofReal p.2 < F p.1}) :=
        Measure.prod_apply_symm hE
    _ = ∫⁻ τ, (Ioi (0 : ℝ)).indicator (fun τ => μ {y | ENNReal.ofReal τ < F y}) τ := by
        apply lintegral_congr
        intro τ
        by_cases hτ : 0 < τ
        · rw [indicator_of_mem (show τ ∈ Ioi (0 : ℝ) from hτ)]
          congr 1
          ext y
          simp [hτ]
        · rw [indicator_of_notMem (show τ ∉ Ioi (0 : ℝ) from hτ)]
          have e : (fun y => (y, τ)) ⁻¹' {p : ℝ × ℝ | 0 < p.2 ∧ ENNReal.ofReal p.2 < F p.1} = ∅ := by
            ext y
            simp [hτ]
          rw [e, measure_empty]
    _ = ∫⁻ τ in Ioi 0, μ {y | ENNReal.ofReal τ < F y} := lintegral_indicator measurableSet_Ioi _

/-! ### The diagonal case of (5.2) -/

/-- **Lemma 5.4, the diagonal case of (5.2).** Let `X_i` have a density bounded by one (law `μ ≤ Lebesgue`) and be
independent of the other coordinates `V` (law `ν`). If, conditionally on `V`, `R = s X_i² + β(V) X_i + γ(V)` with `s ≠ 0`,
then `P(|R - a| < ρ) ≤ 2√(2ρ/|s|)`, by Lemma 5.1 applied for each value of `V`. -/
theorem lemma54_diag_prob {V : Type*} [MeasurableSpace V] (μ : Measure ℝ) [IsProbabilityMeasure μ]
    (hμ : μ ≤ volume) (ν : Measure V) [IsProbabilityMeasure ν] (β γ : V → ℝ) (hβ : Measurable β)
    (hγ : Measurable γ) (s a ρ : ℝ) (hs : s ≠ 0) (hρ : 0 ≤ ρ) :
    (μ.prod ν) {p : ℝ × V | |s * p.1 ^ 2 + β p.2 * p.1 + γ p.2 - a| < ρ}
      ≤ ENNReal.ofReal (2 * Real.sqrt (2 * ρ / |s|)) := by
  have hm : Measurable (fun p : ℝ × V => |s * p.1 ^ 2 + β p.2 * p.1 + γ p.2 - a|) := by fun_prop
  have hE : MeasurableSet {p : ℝ × V | |s * p.1 ^ 2 + β p.2 * p.1 + γ p.2 - a| < ρ} :=
    measurableSet_lt hm measurable_const
  rw [Measure.prod_apply_symm hE]
  calc ∫⁻ v, μ ((fun y => (y, v)) ⁻¹' {p : ℝ × V | |s * p.1 ^ 2 + β p.2 * p.1 + γ p.2 - a| < ρ}) ∂ν
      ≤ ∫⁻ _v, ENNReal.ofReal (2 * Real.sqrt (2 * ρ / |s|)) ∂ν := by
        apply lintegral_mono
        intro v
        calc μ ((fun y => (y, v)) ⁻¹' {p : ℝ × V | |s * p.1 ^ 2 + β p.2 * p.1 + γ p.2 - a| < ρ})
            ≤ volume ((fun y => (y, v)) ⁻¹' {p : ℝ × V | |s * p.1 ^ 2 + β p.2 * p.1 + γ p.2 - a| < ρ}) :=
              Measure.le_iff'.1 hμ _
          _ ≤ volume {y : ℝ | s * y ^ 2 + β v * y + γ v ∈ Icc (a - ρ) (a - ρ + 2 * ρ)} := by
              apply measure_mono
              intro y hy
              have h := abs_lt.1 (show |s * y ^ 2 + β v * y + γ v - a| < ρ from hy)
              exact ⟨by linarith [h.1], by linarith [h.2]⟩
          _ ≤ ENNReal.ofReal (2 * Real.sqrt (2 * ρ / |s|)) := lemma51b s (β v) (γ v) (a - ρ) ρ hs hρ
    _ = ENNReal.ofReal (2 * Real.sqrt (2 * ρ / |s|)) := by rw [lintegral_const, measure_univ, mul_one]

/-- With `|s| ≥ L/2`: `2√(2ρ/|s|) ≤ 4√(ρ/L)`. -/
theorem lemma54_diag_const (ρ L s : ℝ) (hρ : 0 ≤ ρ) (hL : 0 < L) (hs : L / 2 ≤ |s|) :
    2 * Real.sqrt (2 * ρ / |s|) ≤ 4 * Real.sqrt (ρ / L) := by
  have hs0 : 0 < |s| := lt_of_lt_of_le (by linarith) hs
  have h1 : 2 * ρ / |s| ≤ 4 * (ρ / L) := by
    rw [div_le_iff₀ hs0]
    have : 4 * (ρ / L) * |s| ≥ 4 * (ρ / L) * (L / 2) := by
      apply mul_le_mul_of_nonneg_left hs
      positivity
    have e : 4 * (ρ / L) * (L / 2) = 2 * ρ := by
      calc 4 * (ρ / L) * (L / 2) = 2 * ρ * (L / L) := by ring
        _ = 2 * ρ := by rw [div_self hL.ne', mul_one]
    linarith
  calc 2 * Real.sqrt (2 * ρ / |s|) ≤ 2 * Real.sqrt (4 * (ρ / L)) := by
        gcongr
    _ = 4 * Real.sqrt (ρ / L) := by
        rw [Real.sqrt_mul (by norm_num), show (4 : ℝ) = 2 ^ 2 by norm_num, Real.sqrt_sq (by norm_num)]
        ring

/-! ### The logarithmic moment (5.3) -/

/-- `log₊(1/|x|)` in `[0, ∞]`, infinite at `0`. -/
noncomputable def logpInv (x : ℝ) : ℝ≥0∞ :=
  if x = 0 then ⊤ else ENNReal.ofReal (max 0 (Real.log (1 / |x|)))

theorem logpInv_measurable (a : ℝ) : Measurable (fun z => logpInv (z - a)) := by
  unfold logpInv
  refine Measurable.ite (measurableSet_eq_fun (by fun_prop) measurable_const) measurable_const ?_
  exact ENNReal.measurable_ofReal.comp (by fun_prop)

/-- For `τ > 0`: `log₊(1/|z - a|) > τ` exactly when `|z - a| < e^{-τ}`. -/
theorem logpInv_superlevel (a τ : ℝ) (hτ : 0 < τ) :
    {z : ℝ | ENNReal.ofReal τ < logpInv (z - a)} = Ioo (a - Real.exp (-τ)) (a + Real.exp (-τ)) := by
  ext z
  simp only [mem_setOf_eq, mem_Ioo]
  have he : 0 < Real.exp (-τ) := Real.exp_pos _
  unfold logpInv
  by_cases hz : z - a = 0
  · rw [if_pos hz]
    have : z = a := by linarith
    subst this
    simp only [ENNReal.ofReal_lt_top, true_iff]
    constructor <;> linarith
  · rw [if_neg hz, ENNReal.ofReal_lt_ofReal_iff_of_nonneg hτ.le]
    have ha : 0 < |z - a| := abs_pos.2 hz
    constructor
    · intro h
      have h1 : τ < Real.log (1 / |z - a|) := by
        rcases le_or_gt (Real.log (1 / |z - a|)) 0 with h0 | h0
        · rw [max_eq_left h0] at h
          linarith
        · rwa [max_eq_right h0.le] at h
      have h1' : Real.exp τ < 1 / |z - a| := (Real.lt_log_iff_exp_lt (by positivity)).1 h1
      have h2 : |z - a| < Real.exp (-τ) := by
        rw [Real.exp_neg, lt_inv_comm₀ ha (Real.exp_pos τ), inv_eq_one_div]
        exact h1'
      rw [abs_lt] at h2
      exact ⟨by linarith [h2.1], by linarith [h2.2]⟩
    · rintro ⟨h1, h2⟩
      have h3 : |z - a| < Real.exp (-τ) := abs_lt.2 ⟨by linarith, by linarith⟩
      have h4 : τ < Real.log (1 / |z - a|) := by
        rw [Real.lt_log_iff_exp_lt (by positivity), lt_div_iff₀ ha]
        calc Real.exp τ * |z - a| < Real.exp τ * Real.exp (-τ) := by
              gcongr
          _ = 1 := by rw [← Real.exp_add, add_neg_cancel, Real.exp_zero]
      exact lt_of_lt_of_le h4 (le_max_right _ _)

/-- `∫_{(c, ∞)} 19 e^{-τ/2} dτ = 38 e^{-c/2}`. -/
theorem lintegral_Ioi_exp_half (c : ℝ) :
    ∫⁻ τ in Ioi c, ENNReal.ofReal (19 * Real.exp (-τ / 2)) = ENNReal.ofReal (38 * Real.exp (-c / 2)) := by
  have hint : IntegrableOn (fun τ : ℝ => 19 * Real.exp ((-(1 / 2 : ℝ)) * τ)) (Ioi c) :=
    (integrableOn_exp_mul_Ioi (by norm_num) c).const_mul 19
  have heq : ∀ τ ∈ Ioi c, ENNReal.ofReal (19 * Real.exp (-τ / 2))
      = ENNReal.ofReal (19 * Real.exp ((-(1 / 2 : ℝ)) * τ)) := by
    intro τ _
    congr 3
    ring
  rw [setLIntegral_congr_fun measurableSet_Ioi heq,
    ← ofReal_integral_eq_lintegral_ofReal hint
      (ae_restrict_of_forall_mem measurableSet_Ioi (fun τ _ => by positivity)),
    integral_const_mul, integral_exp_mul_Ioi (by norm_num) c]
  congr 1
  rw [show -c / 2 = (-(1 / 2 : ℝ)) * c by ring, neg_div_neg_eq]
  ring

/-- `∫_0^∞ min{1, 19 e^{-τ/2}} dτ ≤ 2 log 19 + 2`, splitting at `τ = 2 log 19`. -/
theorem layer_logmoment_le :
    ∫⁻ τ in Ioi (0 : ℝ), min 1 (ENNReal.ofReal (19 * Real.exp (-τ / 2)))
      ≤ ENNReal.ofReal (2 + 2 * Real.log 19) := by
  have hc : 0 < 2 * Real.log 19 := by
    have := Real.log_pos (show (1 : ℝ) < 19 by norm_num)
    linarith
  rw [← Ioc_union_Ioi_eq_Ioi hc.le, lintegral_union measurableSet_Ioi Ioc_disjoint_Ioi_same]
  have h1 : ∫⁻ τ in Ioc 0 (2 * Real.log 19), min 1 (ENNReal.ofReal (19 * Real.exp (-τ / 2)))
      ≤ ENNReal.ofReal (2 * Real.log 19) := by
    calc ∫⁻ τ in Ioc 0 (2 * Real.log 19), min 1 (ENNReal.ofReal (19 * Real.exp (-τ / 2)))
        ≤ ∫⁻ _τ in Ioc 0 (2 * Real.log 19), 1 := lintegral_mono (fun τ => min_le_left _ _)
      _ = ENNReal.ofReal (2 * Real.log 19) := by
          rw [setLIntegral_const, one_mul, Real.volume_Ioc, sub_zero]
  have h2 : ∫⁻ τ in Ioi (2 * Real.log 19), min 1 (ENNReal.ofReal (19 * Real.exp (-τ / 2)))
      ≤ ENNReal.ofReal 2 := by
    calc ∫⁻ τ in Ioi (2 * Real.log 19), min 1 (ENNReal.ofReal (19 * Real.exp (-τ / 2)))
        ≤ ∫⁻ τ in Ioi (2 * Real.log 19), ENNReal.ofReal (19 * Real.exp (-τ / 2)) :=
          lintegral_mono (fun τ => min_le_right _ _)
      _ = ENNReal.ofReal (38 * Real.exp (-(2 * Real.log 19) / 2)) := lintegral_Ioi_exp_half _
      _ = ENNReal.ofReal 2 := by
          congr 1
          rw [show -(2 * Real.log 19) / 2 = -Real.log 19 by ring, Real.exp_neg, Real.exp_log (by norm_num)]
          norm_num
  calc _ ≤ ENNReal.ofReal (2 * Real.log 19) + ENNReal.ofReal 2 := add_le_add h1 h2
    _ = ENNReal.ofReal (2 + 2 * Real.log 19) := by
        rw [← ENNReal.ofReal_add hc.le (by norm_num)]
        congr 1
        ring

/-- **Lemma 5.4, (5.3).** If `P(|R - a| < ρ) ≤ 19√(ρ/L)` for every `ρ > 0` and `L ≥ 1`, then
`E log₊(1/|R - a|) ≤ L₀ = 2 + 2 log 19`, by the layer-cake formula. -/
theorem lemma54_logmoment (μ : Measure ℝ) [IsProbabilityMeasure μ] (a L : ℝ) (hL : 1 ≤ L)
    (hconc : ∀ ρ : ℝ, 0 < ρ → μ (Ioo (a - ρ) (a + ρ)) ≤ ENNReal.ofReal (19 * Real.sqrt (ρ / L))) :
    ∫⁻ z, logpInv (z - a) ∂μ ≤ ENNReal.ofReal (2 + 2 * Real.log 19) := by
  rw [lintegral_layer μ _ (logpInv_measurable a)]
  refine le_trans (setLIntegral_mono' measurableSet_Ioi (fun τ hτ => ?_)) layer_logmoment_le
  have hτ0 : 0 < τ := hτ
  rw [logpInv_superlevel a τ hτ0]
  refine le_min prob_le_one ((hconc _ (Real.exp_pos _)).trans (ENNReal.ofReal_le_ofReal ?_))
  have hL0 : 0 < L := by linarith
  have h1 : Real.sqrt (Real.exp (-τ) / L) ≤ Real.sqrt (Real.exp (-τ)) :=
    Real.sqrt_le_sqrt (div_le_self (Real.exp_pos _).le hL)
  have h2 : Real.sqrt (Real.exp (-τ)) = Real.exp (-τ / 2) := by
    have e : Real.exp (-τ) = Real.exp (-τ / 2) ^ 2 := by
      rw [← Real.exp_nat_mul]
      congr 1
      push_cast
      ring
    rw [e, Real.sqrt_sq (Real.exp_pos _).le]
  linarith

/-- `L₀ = 2 + 2 log 19 < 8`. -/
theorem L0_lt_eight' : 2 + 2 * Real.log 19 < 8 := by
  have h : Real.log 19 < 3 := by
    rw [Real.log_lt_iff_lt_exp (by norm_num)]
    have := Real.exp_one_gt_d9
    calc (19 : ℝ) < 2.7182818283 ^ 3 := by norm_num
      _ < Real.exp 1 ^ 3 := by gcongr
      _ = Real.exp 3 := by rw [← Real.exp_nat_mul]; norm_num
  linarith

end Concentration

end QformFiveB
