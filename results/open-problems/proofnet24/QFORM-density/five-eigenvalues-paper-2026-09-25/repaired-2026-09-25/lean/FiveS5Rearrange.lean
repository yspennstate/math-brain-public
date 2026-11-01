import Mathlib.MeasureTheory.Measure.Prod
import Mathlib.MeasureTheory.Measure.Lebesgue.Basic
import Mathlib.MeasureTheory.Measure.WithDensity
import Mathlib.MeasureTheory.Group.Measure
import Mathlib.MeasureTheory.Constructions.BorelSpace.Order
import Mathlib.Tactic

/-!
The rearrangement inequality (5.5) of Lemma 5.5 of "Quadratic forms with five large singular values have bounded
densities" (repaired text, sha256 90f859b7): if `g, h : ℝ → [0, ∞]` are even and nonincreasing on `[0, ∞)`, then
`∫ g(y) h(y - b) dy ≤ ∫ g(y) h(y) dy` for every real `b`.

The superlevel sets `{g > σ}` and `{h > τ}` contain, with each point, every point of smaller modulus (`Centred`);
two such sets are nested (`Centred.subset_or_subset`), so the intersection of one with a translate of the other is no
larger than the intersection of the two (`centred_translate_le`), which is the paper's comparison of interval lengths.
The layer-cake formula `∫ F dμ = ∫_0^∞ μ{F > τ} dτ` is proved by Tonelli (`lintegral_layer`) and is used twice, first
for `g` against the measures with densities `h(· - b)` and `h`, then for `h` on each superlevel set of `g`. Measurability
of `g` and `h` is not assumed: centred sets are order-connected, hence Borel (`measurable_of_centred`).
-/

open MeasureTheory Set
open scoped ENNReal

namespace QformFiveB

/-- A set of reals is centred when it contains, with each point, every point of smaller modulus. -/
def Centred (S : Set ℝ) : Prop := ∀ x y : ℝ, |x| ≤ |y| → y ∈ S → x ∈ S

/-- Two centred sets are nested. -/
theorem Centred.subset_or_subset {S T : Set ℝ} (hS : Centred S) (hT : Centred T) : S ⊆ T ∨ T ⊆ S := by
  by_cases h : S ⊆ T
  · exact Or.inl h
  · right
    obtain ⟨s, hsS, hsT⟩ := not_subset.1 h
    intro t htT
    rcases le_total |t| |s| with hts | hst
    · exact hS t s hts hsS
    · exact absurd (hT s t hst htT) hsT

/-- A centred set is order-connected. -/
theorem Centred.ordConnected {S : Set ℝ} (hS : Centred S) : S.OrdConnected := by
  refine ⟨fun x hx y hy z hz => ?_⟩
  rcases le_or_gt 0 z with h0 | h0
  · refine hS z y ?_ hy
    rw [abs_of_nonneg h0, abs_of_nonneg (h0.trans hz.2)]
    exact hz.2
  · refine hS z x ?_ hx
    rw [abs_of_neg h0, abs_of_neg (hz.1.trans_lt h0)]
    linarith [hz.1]

/-- A function whose superlevel sets are centred is measurable. -/
theorem measurable_of_centred (g : ℝ → ℝ≥0∞) (hc : ∀ c, Centred {y | c < g y}) : Measurable g :=
  measurable_of_Ioi (fun c => (hc c).ordConnected.measurableSet)

/-- An even function nonincreasing on `[0, ∞)` is nonincreasing in the modulus. -/
theorem abs_anti_of_even (g : ℝ → ℝ≥0∞) (hev : ∀ y, g (-y) = g y)
    (han : ∀ x y, 0 ≤ x → x ≤ y → g y ≤ g x) : ∀ x y, |x| ≤ |y| → g y ≤ g x := by
  have habs : ∀ y, g y = g |y| := by
    intro y
    rcases le_or_gt 0 y with h | h
    · rw [abs_of_nonneg h]
    · rw [abs_of_neg h, hev]
  intro x y hxy
  rw [habs x, habs y]
  exact han |x| |y| (abs_nonneg x) hxy

/-- The superlevel sets of such a function are centred. -/
theorem centred_superlevel (g : ℝ → ℝ≥0∞) (hg : ∀ x y, |x| ≤ |y| → g y ≤ g x) (c : ℝ≥0∞) :
    Centred {y | c < g y} :=
  fun x y hxy hy => lt_of_lt_of_le hy (hg x y hxy)

/-- For centred `S`, `T`: `|S ∩ (T + b)| ≤ |S ∩ T|`. -/
theorem centred_translate_le {S T : Set ℝ} (hS : Centred S) (hT : Centred T) (b : ℝ) :
    volume ((fun y => y - b) ⁻¹' T ∩ S) ≤ volume (T ∩ S) := by
  have htr : volume ((fun y : ℝ => y - b) ⁻¹' T) = volume T := by
    have e : (fun y : ℝ => y - b) ⁻¹' T = (fun y => y + -b) ⁻¹' T := by
      ext y
      simp [sub_eq_add_neg]
    rw [e, measure_preimage_add_right]
  rcases hS.subset_or_subset hT with h | h
  · rw [inter_eq_right.2 h]
    exact measure_mono inter_subset_right
  · rw [inter_eq_left.2 h, ← htr]
    exact measure_mono inter_subset_left

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

/-- On a centred measurable set, translating a function with centred superlevel sets does not increase its
integral. -/
theorem setLIntegral_translate_le (h : ℝ → ℝ≥0∞) (hh : Measurable h) (hT : ∀ c, Centred {y | c < h y})
    (S : Set ℝ) (hS : Centred S) (b : ℝ) :
    ∫⁻ y in S, h (y - b) ≤ ∫⁻ y in S, h y := by
  have hhb : Measurable (fun y => h (y - b)) := hh.comp (measurable_id.sub_const b)
  rw [lintegral_layer _ _ hhb, lintegral_layer _ _ hh]
  apply lintegral_mono
  intro τ
  dsimp only
  rw [Measure.restrict_apply (measurableSet_lt measurable_const hhb),
    Measure.restrict_apply (measurableSet_lt measurable_const hh)]
  exact centred_translate_le hS (hT _) b

/-- **Lemma 5.5, (5.5).** If `g, h : ℝ → [0, ∞]` are even and nonincreasing on `[0, ∞)`, then for every real `b`,
`∫ g(y) h(y - b) dy ≤ ∫ g(y) h(y) dy`. -/
theorem rearrange (g h : ℝ → ℝ≥0∞) (hg_even : ∀ y, g (-y) = g y) (hh_even : ∀ y, h (-y) = h y)
    (hg_anti : ∀ x y, 0 ≤ x → x ≤ y → g y ≤ g x) (hh_anti : ∀ x y, 0 ≤ x → x ≤ y → h y ≤ h x) (b : ℝ) :
    ∫⁻ y, g y * h (y - b) ≤ ∫⁻ y, g y * h y := by
  have hg_abs := abs_anti_of_even g hg_even hg_anti
  have hh_abs := abs_anti_of_even h hh_even hh_anti
  have hg_c := centred_superlevel g hg_abs
  have hh_c := centred_superlevel h hh_abs
  have hg : Measurable g := measurable_of_centred g hg_c
  have hh : Measurable h := measurable_of_centred h hh_c
  have hhb : Measurable (fun y => h (y - b)) := hh.comp (measurable_id.sub_const b)
  have e1 : ∫⁻ y, g y * h (y - b) = ∫⁻ y, g y ∂(volume.withDensity (fun y => h (y - b))) := by
    rw [lintegral_withDensity_eq_lintegral_mul _ hhb hg]
    apply lintegral_congr
    intro y
    simp only [Pi.mul_apply]
    ring
  have e2 : ∫⁻ y, g y * h y = ∫⁻ y, g y ∂(volume.withDensity h) := by
    rw [lintegral_withDensity_eq_lintegral_mul _ hh hg]
    apply lintegral_congr
    intro y
    simp only [Pi.mul_apply]
    ring
  rw [e1, e2, lintegral_layer _ _ hg, lintegral_layer _ _ hg]
  apply lintegral_mono
  intro σ
  dsimp only
  have hSm : MeasurableSet {y | ENNReal.ofReal σ < g y} := measurableSet_lt measurable_const hg
  rw [withDensity_apply _ hSm, withDensity_apply _ hSm]
  exact setLIntegral_translate_le h hh hh_c _ (hg_c _) b

end QformFiveB
