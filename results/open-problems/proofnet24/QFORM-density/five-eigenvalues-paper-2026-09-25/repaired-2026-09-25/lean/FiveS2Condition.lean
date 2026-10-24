import Mathlib.MeasureTheory.Measure.Prod
import Mathlib.MeasureTheory.Measure.WithDensity
import Mathlib.MeasureTheory.Measure.Lebesgue.Basic
import Mathlib.MeasureTheory.Integral.Lebesgue.Map
import Mathlib.MeasureTheory.Measure.Decomposition.RadonNikodym
import Mathlib.MeasureTheory.Function.AEEqOfLIntegral
import Mathlib.Tactic

/-!
Lemma 2.4 of "Quadratic forms with five large singular values have bounded densities" (repaired text,
sha256 90f859b7): let `U` and `V` be independent random elements, `h` and `g` measurable, and suppose that for almost every
`v`, `P(h(U,v) ∈ B) ≤ ∫_B g(z,v) dz` for every Borel set `B`. Then `Q = h(U,V)` has a density `p_Q` with
`p_Q(z) ≤ E g(z,V)` for almost every `z`, and `E k(Q) ≤ ∫ k(z) E g(z,V) dz` for every Borel `k ≥ 0`.

Independence means that the joint law is the product `μU ⊗ μV`; the law of `Q` is its image under `h`.

* `lemma24_le`: the law of `Q` is at most Lebesgue measure with density `E g(·,V)` (Tonelli on the product).
* `lemma24_ac`: the law of `Q` is absolutely continuous, so `Q` has a density.
* `lemma24_density`: that density (the Radon-Nikodym derivative) is at most `E g(·,V)` almost everywhere.
* `lemma24_expect`: `E k(Q) ≤ ∫ k(z) E g(z,V) dz` for measurable `k ≥ 0`.
-/

open MeasureTheory ENNReal

namespace QformFiveB

variable {𝒰 𝒱 : Type*} [MeasurableSpace 𝒰] [MeasurableSpace 𝒱]

/-- **Lemma 2.4, the law of `Q`.** `Law(h(U,V)) ≤ Leb.withDensity (E g(·,V))`. -/
theorem lemma24_le (μU : Measure 𝒰) (μV : Measure 𝒱) [SFinite μU] [SFinite μV]
    (h : 𝒰 → 𝒱 → ℝ) (hh : Measurable (Function.uncurry h))
    (g : ℝ → 𝒱 → ℝ≥0∞) (hg : Measurable (Function.uncurry g))
    (hyp : ∀ᵐ v ∂μV, ∀ B : Set ℝ, MeasurableSet B → μU {u | h u v ∈ B} ≤ ∫⁻ z in B, g z v) :
    (μU.prod μV).map (Function.uncurry h) ≤ volume.withDensity (fun z => ∫⁻ v, g z v ∂μV) := by
  rw [Measure.le_iff]
  intro B hB
  rw [Measure.map_apply hh hB, withDensity_apply _ hB, Measure.prod_apply_symm (hh hB)]
  have hswap : ∫⁻ v, (∫⁻ z in B, g z v) ∂μV = ∫⁻ z in B, ∫⁻ v, g z v ∂μV := by
    have hm : AEMeasurable (Function.uncurry fun (v : 𝒱) (z : ℝ) => g z v) (μV.prod (volume.restrict B)) :=
      (hg.comp measurable_swap).aemeasurable
    exact lintegral_lintegral_swap hm
  calc ∫⁻ v, μU ((fun u => (u, v)) ⁻¹' (Function.uncurry h ⁻¹' B)) ∂μV
      ≤ ∫⁻ v, (∫⁻ z in B, g z v) ∂μV := lintegral_mono_ae (hyp.mono (fun v hv => hv B hB))
    _ = ∫⁻ z in B, ∫⁻ v, g z v ∂μV := hswap

/-- **Lemma 2.4, existence of the density.** The law of `Q` is absolutely continuous. -/
theorem lemma24_ac (μU : Measure 𝒰) (μV : Measure 𝒱) [SFinite μU] [SFinite μV]
    (h : 𝒰 → 𝒱 → ℝ) (hh : Measurable (Function.uncurry h))
    (g : ℝ → 𝒱 → ℝ≥0∞) (hg : Measurable (Function.uncurry g))
    (hyp : ∀ᵐ v ∂μV, ∀ B : Set ℝ, MeasurableSet B → μU {u | h u v ∈ B} ≤ ∫⁻ z in B, g z v) :
    (μU.prod μV).map (Function.uncurry h) ≪ volume :=
  (Measure.absolutelyContinuous_of_le (lemma24_le μU μV h hh g hg hyp)).trans
    (withDensity_absolutelyContinuous _ _)

/-- **Lemma 2.4, the density bound.** `p_Q ≤ E g(·,V)` almost everywhere, with `p_Q` the Radon-Nikodym derivative. -/
theorem lemma24_density (μU : Measure 𝒰) (μV : Measure 𝒱) [IsFiniteMeasure μU] [IsFiniteMeasure μV]
    (h : 𝒰 → 𝒱 → ℝ) (hh : Measurable (Function.uncurry h))
    (g : ℝ → 𝒱 → ℝ≥0∞) (hg : Measurable (Function.uncurry g))
    (hyp : ∀ᵐ v ∂μV, ∀ B : Set ℝ, MeasurableSet B → μU {u | h u v ∈ B} ≤ ∫⁻ z in B, g z v) :
    ((μU.prod μV).map (Function.uncurry h)).rnDeriv volume ≤ᵐ[volume] fun z => ∫⁻ v, g z v ∂μV := by
  have hle := lemma24_le μU μV h hh g hg hyp
  have hac := lemma24_ac μU μV h hh g hg hyp
  refine ae_le_of_forall_setLIntegral_le_of_sigmaFinite (Measure.measurable_rnDeriv _ _) (fun s hs _ => ?_)
  rw [← withDensity_apply _ hs, Measure.withDensity_rnDeriv_eq _ _ hac, ← withDensity_apply _ hs]
  exact hle s

/-- **Lemma 2.4, expectations.** `E k(Q) ≤ ∫ k(z) E g(z,V) dz` for measurable `k ≥ 0`. -/
theorem lemma24_expect (μU : Measure 𝒰) (μV : Measure 𝒱) [SFinite μU] [SFinite μV]
    (h : 𝒰 → 𝒱 → ℝ) (hh : Measurable (Function.uncurry h))
    (g : ℝ → 𝒱 → ℝ≥0∞) (hg : Measurable (Function.uncurry g))
    (hyp : ∀ᵐ v ∂μV, ∀ B : Set ℝ, MeasurableSet B → μU {u | h u v ∈ B} ≤ ∫⁻ z in B, g z v)
    (k : ℝ → ℝ≥0∞) (hk : Measurable k) :
    ∫⁻ p, k (Function.uncurry h p) ∂(μU.prod μV) ≤ ∫⁻ z, (∫⁻ v, g z v ∂μV) * k z := by
  have hF : Measurable (fun z => ∫⁻ v, g z v ∂μV) := hg.lintegral_prod_right'
  rw [← lintegral_map hk hh]
  calc ∫⁻ q, k q ∂((μU.prod μV).map (Function.uncurry h))
      ≤ ∫⁻ q, k q ∂(volume.withDensity (fun z => ∫⁻ v, g z v ∂μV)) :=
        lintegral_mono' (lemma24_le μU μV h hh g hg hyp) le_rfl
    _ = ∫⁻ z, (∫⁻ v, g z v ∂μV) * k z := lintegral_withDensity_eq_lintegral_mul _ hF hk

end QformFiveB
