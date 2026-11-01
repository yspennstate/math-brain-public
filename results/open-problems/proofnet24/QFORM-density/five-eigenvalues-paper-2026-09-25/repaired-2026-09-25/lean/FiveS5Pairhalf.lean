import Mathlib.MeasureTheory.Measure.Prod
import Mathlib.MeasureTheory.Measure.Lebesgue.Basic
import Mathlib.MeasureTheory.Measure.WithDensity
import Mathlib.MeasureTheory.Measure.Typeclasses.Probability
import Mathlib.MeasureTheory.Measure.Typeclasses.NoAtoms
import Mathlib.MeasureTheory.Group.Measure
import Mathlib.MeasureTheory.Constructions.BorelSpace.Order
import Mathlib.MeasureTheory.Integral.Lebesgue.Basic
import Mathlib.MeasureTheory.Integral.IntervalIntegral.FundThmCalculus
import Mathlib.MeasureTheory.Function.JacobianOneDim
import Mathlib.Analysis.SpecialFunctions.ImproperIntegrals
import Mathlib.Analysis.SpecialFunctions.Pow.NNReal
import Mathlib.Analysis.SpecialFunctions.Pow.Continuity
import Mathlib.Analysis.SpecialFunctions.Sqrt
import Mathlib.Analysis.SpecialFunctions.Log.Deriv
import Mathlib.Analysis.SpecialFunctions.Log.NegMulLog
import Mathlib.Analysis.Real.Pi.Bounds
import Mathlib.Analysis.Complex.ExponentialBounds
import Mathlib.Tactic

/-!
Lemma 5.6 of "Quadratic forms with five large singular values have bounded densities" (repaired text, sha256 90f859b7):
for independent `W₁, W₂` with densities at most one and a quadratic `q` on `ℝ²` whose quadratic part has determinant of
modulus `D > 0`, `sup_a E|q(W) - a|^{-1/2} ≤ 16 D^{-1/4}`, given the density bounds of Lemmas 5.2 and 5.3.

The definite case: a density bounded by `M = π D^{-1/2}` gives `E|q(W) - a|^{-1/2} ≤ 2√(2M) = 2√(2π) D^{-1/4}
< 6 D^{-1/4}` by (5.6) (`lemma56_definite`, through `bounded_halfmoment`). The indefinite case: `Y = (q(W) - v)/√D` has a
density bounded by `h(y) = 6 + log₊(16/|y|)` with `h(0) = ∞` (`hY`); split `E|Y - b|^{-1/2}` at `|Y - b| = δ = 1/64`,
bound the far part by `δ^{-1/2} = 8` and the near part by `∫_{|y-b| ≤ δ} h(y) |y - b|^{-1/2} dy`, which the
rearrangement inequality (5.5) moves to `b = 0` (`rearrange`, with `h` and `|u|^{-1/2} 1{|u| ≤ δ}` even and
nonincreasing on `[0, ∞)`), where it equals `4√δ(8 + log(16/δ)) = 4 + 5 log 2` (`kernel_integral`, from the
antiderivative `2√y(8 + log(16/y))`, written as `Fk` to be continuous at `0`). So `E|Y - b|^{-1/2} ≤ 12 + 5 log 2 < 16`
(`pairhalf_indefinite`), and `E|q(W) - a|^{-1/2} = D^{-1/4} E|Y - (a - v)/√D|^{-1/2}` (`lemma56_indefinite`).

The layer-cake formula, the rearrangement inequality, the bound (5.6) and the fundamental theorem of calculus in
`[0, ∞]` are repeated from `FiveS5Rearrange.lean`, `FiveS5Bounded.lean` and `FiveS5Kernel.lean`, so that this file
compiles on its own.
-/

open MeasureTheory Set
open scoped ENNReal

namespace QformFiveB

namespace Pairhalf

/-! ### Repeated: the rearrangement inequality -/

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

/-! ### Repeated: display (5.6) -/

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

/-! ### Repeated: the fundamental theorem of calculus in `[0, ∞]` -/

/-- The fundamental theorem of calculus in `[0, ∞]`: if `F` is continuous on `[a, b]` with derivative `F' ≥ 0` on
`(a, b)`, then `∫_{(a,b)} F' = F b - F a`. -/
theorem lintegral_Ioo_deriv (F F' : ℝ → ℝ) (a b : ℝ) (hab : a ≤ b) (hcont : ContinuousOn F (Icc a b))
    (hderiv : ∀ x ∈ Ioo a b, HasDerivAt F (F' x) x) (hpos : ∀ x ∈ Ioo a b, 0 ≤ F' x) :
    ∫⁻ x in Ioo a b, ENNReal.ofReal (F' x) = ENNReal.ofReal (F b - F a) := by
  have hint : IntegrableOn F' (Ioc a b) := intervalIntegral.integrableOn_deriv_of_nonneg hcont hderiv hpos
  rw [← ofReal_integral_eq_lintegral_ofReal (hint.mono_set Ioo_subset_Ioc_self)
      (ae_restrict_of_forall_mem measurableSet_Ioo hpos),
    ← integral_Ioc_eq_integral_Ioo, ← intervalIntegral.integral_of_le hab,
    intervalIntegral.integral_eq_sub_of_hasDerivAt_of_le hab hcont hderiv
      ((intervalIntegrable_iff_integrableOn_Ioc_of_le hab).2 hint)]

/-! ### The indefinite case -/

/-- For `0 ≤ s ≤ t`: `t^{-1/2} ≤ s^{-1/2}` in `[0, ∞]`. -/
theorem rpow_neg_half_anti (s t : ℝ) (hst : s ≤ t) :
    (ENNReal.ofReal t) ^ (-(1 / 2 : ℝ)) ≤ (ENNReal.ofReal s) ^ (-(1 / 2 : ℝ)) := by
  rw [ENNReal.rpow_neg, ENNReal.rpow_neg]
  exact ENNReal.inv_le_inv.2 (ENNReal.rpow_le_rpow (ENNReal.ofReal_le_ofReal hst) (by norm_num))

/-- `(1/64)^{-1/2} = 8`. -/
theorem eight_eq : (ENNReal.ofReal (1 / 64)) ^ (-(1 / 2 : ℝ)) = 8 := by
  rw [ENNReal.ofReal_rpow_of_pos (by norm_num), Real.rpow_neg (by norm_num), ← Real.sqrt_eq_rpow,
    show (1 / 64 : ℝ) = (1 / 8) ^ 2 by norm_num, Real.sqrt_sq (by norm_num)]
  norm_num

/-- The density bound that Lemma 5.3 gives for `Y = (q(W) - v)/√D`: `h(y) = 6 + log₊(16/|y|)`, `h(0) = ∞`. -/
noncomputable def hY (y : ℝ) : ℝ≥0∞ :=
  if y = 0 then ⊤ else ENNReal.ofReal (6 + max 0 (Real.log (16 / |y|)))

/-- The truncated kernel `|u|^{-1/2} 1{|u| ≤ δ}` at `δ = 1/64`. -/
noncomputable def kq (u : ℝ) : ℝ≥0∞ :=
  if |u| ≤ 1 / 64 then (ENNReal.ofReal |u|) ^ (-(1 / 2 : ℝ)) else 0

theorem hY_even (y : ℝ) : hY (-y) = hY y := by
  unfold hY
  simp only [neg_eq_zero, abs_neg]

theorem hY_anti (x y : ℝ) (hx : 0 ≤ x) (hxy : x ≤ y) : hY y ≤ hY x := by
  unfold hY
  rcases hx.eq_or_lt with h0 | h0
  · subst h0
    rw [if_pos rfl]
    exact le_top
  · have hy : 0 < y := h0.trans_le hxy
    rw [if_neg hy.ne', if_neg h0.ne']
    apply ENNReal.ofReal_le_ofReal
    have hq : 16 / y ≤ 16 / x := by
      rw [div_le_div_iff₀ hy h0]
      linarith
    have hlog : Real.log (16 / |y|) ≤ Real.log (16 / |x|) := by
      rw [abs_of_pos hy, abs_of_pos h0]
      exact Real.log_le_log (by positivity) hq
    linarith [max_le_max (le_refl (0 : ℝ)) hlog]

theorem kq_even (u : ℝ) : kq (-u) = kq u := by
  unfold kq
  simp only [abs_neg]

theorem kq_anti (x y : ℝ) (hx : 0 ≤ x) (hxy : x ≤ y) : kq y ≤ kq x := by
  unfold kq
  by_cases hyδ : |y| ≤ 1 / 64
  · have hy0 : 0 ≤ y := hx.trans hxy
    have hxδ : |x| ≤ 1 / 64 := by
      rw [abs_of_nonneg hx]
      rw [abs_of_nonneg hy0] at hyδ
      linarith
    rw [if_pos hyδ, if_pos hxδ]
    apply rpow_neg_half_anti
    rw [abs_of_nonneg hx, abs_of_nonneg hy0]
    exact hxy
  · rw [if_neg hyδ]
    exact zero_le _

/-- The antiderivative `F(y) = 2√y(8 + log 16) - 4√y log √y`, continuous on `ℝ` with `F(0) = 0`; for `y > 0` it is
`2√y (8 + log(16/y))`. -/
noncomputable def Fk (y : ℝ) : ℝ := 2 * √y * (8 + Real.log 16) - 4 * (√y * Real.log √y)

theorem Fk_continuous : Continuous Fk :=
  ((continuous_const.mul Real.continuous_sqrt).mul continuous_const).sub
    (continuous_const.mul (Real.continuous_mul_log.comp Real.continuous_sqrt))

/-- On `y > 0`: `d/dy [2√y (8 + log(16/y))] = y^{-1/2} (6 + log(16/y))`. -/
theorem deriv_halfmoment_kernel (y : ℝ) (hy : 0 < y) :
    HasDerivAt (fun y => 2 * √y * (8 + Real.log (16 / y))) ((6 + Real.log (16 / y)) / √y) y := by
  have h1 : HasDerivAt (fun y => √y) (1 / (2 * √y)) y := Real.hasDerivAt_sqrt hy.ne'
  have h2 : HasDerivAt (fun y => Real.log (16 / y)) (-(1 / y)) y := by
    have hq : HasDerivAt (fun y => 16 / y) (-(16 / y ^ 2)) y := by
      have := (hasDerivAt_inv hy.ne').const_mul 16
      simpa [div_eq_mul_inv] using this
    have := hq.log (by positivity)
    convert this using 1
    field_simp
  have h3 := (h1.const_mul 2).mul (h2.const_add 8)
  convert h3 using 1
  have hs : 0 < √y := Real.sqrt_pos.mpr hy
  field_simp
  rw [Real.sq_sqrt hy.le]
  ring

theorem hasDerivAt_Fk (y : ℝ) (hy : 0 < y) : HasDerivAt Fk ((6 + Real.log (16 / y)) / √y) y := by
  refine (deriv_halfmoment_kernel y hy).congr_of_eventuallyEq
    (Filter.eventually_of_mem (Ioi_mem_nhds hy) (fun z hz => ?_))
  have hz0 : 0 < z := hz
  show Fk z = 2 * √z * (8 + Real.log (16 / z))
  unfold Fk
  rw [Real.log_div (by norm_num) hz0.ne', Real.log_sqrt hz0.le]
  ring

/-- On `(0, 1/64)` the integrand is `(6 + log(16/y))/√y`. -/
theorem integrand_eq (y : ℝ) (hy : y ∈ Ioo (0 : ℝ) (1 / 64)) :
    hY y * kq y = ENNReal.ofReal ((6 + Real.log (16 / y)) / √y) := by
  have h0 : 0 < y := hy.1
  have hlog : 0 ≤ Real.log (16 / y) := Real.log_nonneg (by rw [le_div_iff₀ h0]; linarith [hy.2])
  unfold hY kq
  rw [if_neg h0.ne', abs_of_pos h0, if_pos hy.2.le, max_eq_right hlog, ENNReal.ofReal_rpow_of_pos h0,
    ← ENNReal.ofReal_mul (show (0 : ℝ) ≤ 6 + Real.log (16 / y) by linarith)]
  congr 1
  rw [Real.rpow_neg h0.le, ← Real.sqrt_eq_rpow, div_eq_mul_inv (6 + Real.log (16 / y)) √y]

/-- Integrals of an even function over `(-c, 0)` and `(0, c)` agree. -/
theorem setLIntegral_Ioo_neg (f : ℝ → ℝ≥0∞) (hf : ∀ y, f (-y) = f y) (c : ℝ) :
    ∫⁻ y in Ioo (-c) 0, f y = ∫⁻ y in Ioo 0 c, f y := by
  have himg : Neg.neg '' Ioo (0 : ℝ) c = Ioo (-c) 0 := by
    rw [image_neg_Ioo, neg_zero]
  have h := lintegral_image_eq_lintegral_abs_deriv_mul (s := Ioo (0 : ℝ) c) (f := Neg.neg) (f' := fun _ => -1)
    measurableSet_Ioo (fun x _ => (hasDerivAt_neg x).hasDerivWithinAt) neg_injective.injOn f
  rw [himg] at h
  rw [h]
  apply lintegral_congr
  intro x
  simp only [abs_neg, abs_one, ENNReal.ofReal_one, one_mul, hf]

/-- `∫ h(y) |y|^{-1/2} 1{|y| ≤ 1/64} dy ≤ 4√δ(8 + log(16/δ)) = 4 + 5 log 2` at `δ = 1/64`. -/
theorem kernel_integral : ∫⁻ y, hY y * kq y ≤ ENNReal.ofReal (4 + 5 * Real.log 2) := by
  have hzero : ∫⁻ y in (Icc (-(1 / 64 : ℝ)) (1 / 64))ᶜ, hY y * kq y = 0 := by
    apply setLIntegral_eq_zero measurableSet_Icc.compl
    intro y hy
    have hnot : ¬ |y| ≤ 1 / 64 := by
      intro h
      exact hy ⟨by linarith [neg_abs_le y], by linarith [le_abs_self y]⟩
    simp only [kq, Pi.zero_apply]
    rw [if_neg hnot, mul_zero]
  rw [← lintegral_add_compl _ (measurableSet_Icc : MeasurableSet (Icc (-(1 / 64 : ℝ)) (1 / 64))), hzero, add_zero]
  have hsub : Icc (-(1 / 64 : ℝ)) (1 / 64) ⊆ Icc (-(1 / 64)) 0 ∪ Icc 0 (1 / 64) := by
    intro y hy
    rcases le_or_gt y 0 with h | h
    · exact Or.inl ⟨hy.1, h⟩
    · exact Or.inr ⟨h.le, hy.2⟩
  have hpos_piece : ∫⁻ y in Icc (0 : ℝ) (1 / 64), hY y * kq y = ENNReal.ofReal (2 + 5 / 2 * Real.log 2) := by
    have heq : ∀ y ∈ Ioo (0 : ℝ) (1 / 64), hY y * kq y = ENNReal.ofReal ((6 + Real.log (16 / y)) / √y) :=
      fun y hy => integrand_eq y hy
    rw [← setLIntegral_congr Ioo_ae_eq_Icc, setLIntegral_congr_fun measurableSet_Ioo heq,
      lintegral_Ioo_deriv Fk (fun y => (6 + Real.log (16 / y)) / √y) 0 (1 / 64) (by norm_num)
        Fk_continuous.continuousOn (fun y hy => hasDerivAt_Fk y hy.1)
        (fun y hy => div_nonneg (by
          have := Real.log_nonneg (show (1 : ℝ) ≤ 16 / y by rw [le_div_iff₀ hy.1]; linarith [hy.2])
          linarith) (Real.sqrt_nonneg _))]
    congr 1
    have h8 : √(1 / 64 : ℝ) = 1 / 8 := by
      rw [show (1 / 64 : ℝ) = (1 / 8) ^ 2 by norm_num]
      exact Real.sqrt_sq (by norm_num)
    have h16 : Real.log 16 = 4 * Real.log 2 := by
      rw [show (16 : ℝ) = 2 ^ 4 by norm_num, Real.log_pow]
      norm_num
    have h18 : Real.log (1 / 8) = -(3 * Real.log 2) := by
      rw [one_div, Real.log_inv, show (8 : ℝ) = 2 ^ 3 by norm_num, Real.log_pow]
      norm_num
    unfold Fk
    rw [h8, h16, h18, Real.sqrt_zero]
    ring
  have hneg_piece : ∫⁻ y in Icc (-(1 / 64 : ℝ)) 0, hY y * kq y = ENNReal.ofReal (2 + 5 / 2 * Real.log 2) := by
    rw [← setLIntegral_congr Ioo_ae_eq_Icc,
      setLIntegral_Ioo_neg (fun y => hY y * kq y) (fun y => by simp only [hY_even, kq_even]) (1 / 64),
      setLIntegral_congr Ioo_ae_eq_Icc, hpos_piece]
  have hl2 : 0 ≤ Real.log 2 := Real.log_nonneg (by norm_num)
  calc ∫⁻ y in Icc (-(1 / 64 : ℝ)) (1 / 64), hY y * kq y
      ≤ ∫⁻ y in Icc (-(1 / 64 : ℝ)) 0 ∪ Icc 0 (1 / 64), hY y * kq y := lintegral_mono_set hsub
    _ ≤ (∫⁻ y in Icc (-(1 / 64 : ℝ)) 0, hY y * kq y) + ∫⁻ y in Icc 0 (1 / 64), hY y * kq y :=
        lintegral_union_le _ _ _
    _ = ENNReal.ofReal (2 + 5 / 2 * Real.log 2) + ENNReal.ofReal (2 + 5 / 2 * Real.log 2) := by
        rw [hneg_piece, hpos_piece]
    _ = ENNReal.ofReal (4 + 5 * Real.log 2) := by
        rw [← ENNReal.ofReal_add (by positivity) (by positivity)]
        congr 1
        ring

theorem hY_abs (x y : ℝ) (hxy : |x| ≤ |y|) : hY y ≤ hY x :=
  abs_anti_of_even hY hY_even hY_anti x y hxy

theorem hY_measurable : Measurable hY :=
  measurable_of_centred hY (centred_superlevel hY hY_abs)

/-- **Lemma 5.6, the indefinite case.** If `Y` has a density bounded by `h(y) = 6 + log₊(16/|y|)`, then
`E|Y - b|^{-1/2} ≤ δ^{-1/2} + 4√δ(8 + log(16/δ)) = 12 + 5 log 2` for every `b`, at `δ = 1/64`. -/
theorem pairhalf_indefinite (ν : Measure ℝ) [IsProbabilityMeasure ν] (hν : ν ≤ volume.withDensity hY) (b : ℝ) :
    ∫⁻ y, (ENNReal.ofReal |y - b|) ^ (-(1 / 2 : ℝ)) ∂ν ≤ ENNReal.ofReal (12 + 5 * Real.log 2) := by
  have hAm : MeasurableSet {y : ℝ | |y - b| ≤ 1 / 64} := measurableSet_le (by fun_prop) measurable_const
  have hg : Measurable (fun y : ℝ => (ENNReal.ofReal |y - b|) ^ (-(1 / 2 : ℝ))) :=
    ENNReal.continuous_rpow_const.measurable.comp (ENNReal.measurable_ofReal.comp (by fun_prop))
  rw [← lintegral_add_compl _ hAm]
  have hfar : ∫⁻ y in {y : ℝ | |y - b| ≤ 1 / 64}ᶜ, (ENNReal.ofReal |y - b|) ^ (-(1 / 2 : ℝ)) ∂ν ≤ 8 := by
    calc ∫⁻ y in {y : ℝ | |y - b| ≤ 1 / 64}ᶜ, (ENNReal.ofReal |y - b|) ^ (-(1 / 2 : ℝ)) ∂ν
        ≤ ∫⁻ _y in {y : ℝ | |y - b| ≤ 1 / 64}ᶜ, (8 : ℝ≥0∞) ∂ν := by
          apply setLIntegral_mono' hAm.compl
          intro y hy
          have hy' : 1 / 64 < |y - b| := lt_of_not_ge hy
          calc (ENNReal.ofReal |y - b|) ^ (-(1 / 2 : ℝ)) ≤ (ENNReal.ofReal (1 / 64)) ^ (-(1 / 2 : ℝ)) :=
                rpow_neg_half_anti _ _ hy'.le
            _ = 8 := eight_eq
      _ = 8 * ν {y : ℝ | |y - b| ≤ 1 / 64}ᶜ := setLIntegral_const _ _
      _ ≤ 8 * 1 := by
          gcongr
          exact prob_le_one
      _ = 8 := mul_one _
  have hnear : ∫⁻ y in {y : ℝ | |y - b| ≤ 1 / 64}, (ENNReal.ofReal |y - b|) ^ (-(1 / 2 : ℝ)) ∂ν
      ≤ ENNReal.ofReal (4 + 5 * Real.log 2) := by
    calc ∫⁻ y in {y : ℝ | |y - b| ≤ 1 / 64}, (ENNReal.ofReal |y - b|) ^ (-(1 / 2 : ℝ)) ∂ν
        ≤ ∫⁻ y in {y : ℝ | |y - b| ≤ 1 / 64}, (ENNReal.ofReal |y - b|) ^ (-(1 / 2 : ℝ))
            ∂(volume.withDensity hY) :=
          lintegral_mono' (Measure.restrict_mono le_rfl hν) le_rfl
      _ = ∫⁻ y in {y : ℝ | |y - b| ≤ 1 / 64}, (hY * fun y => (ENNReal.ofReal |y - b|) ^ (-(1 / 2 : ℝ))) y :=
          setLIntegral_withDensity_eq_setLIntegral_mul _ hY_measurable hg hAm
      _ = ∫⁻ y, hY y * kq (y - b) := by
          rw [← lintegral_indicator hAm]
          apply lintegral_congr
          intro y
          by_cases hy : |y - b| ≤ 1 / 64
          · rw [indicator_of_mem (show y ∈ {y : ℝ | |y - b| ≤ 1 / 64} from hy)]
            simp only [Pi.mul_apply, kq, if_pos hy]
          · rw [indicator_of_notMem (show y ∉ {y : ℝ | |y - b| ≤ 1 / 64} from hy)]
            simp only [kq, if_neg hy, mul_zero]
      _ ≤ ∫⁻ y, hY y * kq y := rearrange hY kq hY_even kq_even hY_anti kq_anti b
      _ ≤ ENNReal.ofReal (4 + 5 * Real.log 2) := kernel_integral
  have hl2 : 0 ≤ Real.log 2 := Real.log_nonneg (by norm_num)
  calc ∫⁻ y in {y : ℝ | |y - b| ≤ 1 / 64}, (ENNReal.ofReal |y - b|) ^ (-(1 / 2 : ℝ)) ∂ν
        + ∫⁻ y in {y : ℝ | |y - b| ≤ 1 / 64}ᶜ, (ENNReal.ofReal |y - b|) ^ (-(1 / 2 : ℝ)) ∂ν
      ≤ ENNReal.ofReal (4 + 5 * Real.log 2) + 8 := add_le_add hnear hfar
    _ = ENNReal.ofReal (12 + 5 * Real.log 2) := by
        rw [show (8 : ℝ≥0∞) = ENNReal.ofReal 8 by norm_num, ← ENNReal.ofReal_add (by positivity) (by norm_num)]
        congr 1
        ring

/-- `12 + 5 log 2 < 16`. -/
theorem pairhalf_total' : 12 + 5 * Real.log 2 < 16 := by
  have := Real.log_two_lt_d9
  norm_num at this ⊢
  linarith

/-! ### Lemma 5.6 from the density bounds of Lemmas 5.2 and 5.3 -/

/-- `√(√D) = D^{1/4}` and the scaling of the half moment: `(√D x)^{-1/2} = D^{-1/4} x^{-1/2}` in `[0, ∞]`. -/
theorem scale_rpow (D x : ℝ) (hD : 0 < D) (hx : 0 ≤ x) :
    (ENNReal.ofReal (√D * x)) ^ (-(1 / 2 : ℝ))
      = ENNReal.ofReal (D ^ (-(1 / 4 : ℝ))) * (ENNReal.ofReal x) ^ (-(1 / 2 : ℝ)) := by
  have hs : 0 < √D := Real.sqrt_pos.2 hD
  rw [ENNReal.ofReal_mul hs.le, ENNReal.mul_rpow_of_ne_top ENNReal.ofReal_ne_top ENNReal.ofReal_ne_top,
    ENNReal.ofReal_rpow_of_pos hs]
  congr 2
  rw [Real.sqrt_eq_rpow, ← Real.rpow_mul hD.le]
  norm_num

/-- **Lemma 5.6, the indefinite case, in the form used.** If `Y = (q(W) - v)/√D` has a density bounded by
`6 + log₊(16/|y|)`, then for every `a`, `E|q(W) - a|^{-1/2} = E|√D Y + v - a|^{-1/2} ≤ D^{-1/4}(12 + 5 log 2)
< 16 D^{-1/4}`. -/
theorem lemma56_indefinite (ν : Measure ℝ) [IsProbabilityMeasure ν] (hν : ν ≤ volume.withDensity hY)
    (D v a : ℝ) (hD : 0 < D) :
    ∫⁻ y, (ENNReal.ofReal |√D * y + v - a|) ^ (-(1 / 2 : ℝ)) ∂ν ≤ ENNReal.ofReal (16 * D ^ (-(1 / 4 : ℝ))) := by
  have hs : 0 < √D := Real.sqrt_pos.2 hD
  have hpt : ∀ y, (ENNReal.ofReal |√D * y + v - a|) ^ (-(1 / 2 : ℝ))
      = ENNReal.ofReal (D ^ (-(1 / 4 : ℝ))) * (ENNReal.ofReal |y - (a - v) / √D|) ^ (-(1 / 2 : ℝ)) := by
    intro y
    have hc : √D * ((a - v) / √D) = a - v := by field_simp
    have e : |√D * y + v - a| = √D * |y - (a - v) / √D| := by
      rw [show √D * y + v - a = √D * (y - (a - v) / √D) by rw [mul_sub, hc]; ring, abs_mul, abs_of_pos hs]
    rw [e, scale_rpow D _ hD (abs_nonneg _)]
  have hD4 : 0 < D ^ (-(1 / 4 : ℝ)) := Real.rpow_pos_of_pos hD _
  calc ∫⁻ y, (ENNReal.ofReal |√D * y + v - a|) ^ (-(1 / 2 : ℝ)) ∂ν
      = ENNReal.ofReal (D ^ (-(1 / 4 : ℝ))) * ∫⁻ y, (ENNReal.ofReal |y - (a - v) / √D|) ^ (-(1 / 2 : ℝ)) ∂ν := by
        simp_rw [hpt]
        exact lintegral_const_mul' _ _ ENNReal.ofReal_ne_top
    _ ≤ ENNReal.ofReal (D ^ (-(1 / 4 : ℝ))) * ENNReal.ofReal (12 + 5 * Real.log 2) := by
        gcongr
        exact pairhalf_indefinite ν hν _
    _ = ENNReal.ofReal (D ^ (-(1 / 4 : ℝ)) * (12 + 5 * Real.log 2)) := (ENNReal.ofReal_mul hD4.le).symm
    _ ≤ ENNReal.ofReal (16 * D ^ (-(1 / 4 : ℝ))) := by
        apply ENNReal.ofReal_le_ofReal
        nlinarith [pairhalf_total']

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

end Pairhalf

end QformFiveB
