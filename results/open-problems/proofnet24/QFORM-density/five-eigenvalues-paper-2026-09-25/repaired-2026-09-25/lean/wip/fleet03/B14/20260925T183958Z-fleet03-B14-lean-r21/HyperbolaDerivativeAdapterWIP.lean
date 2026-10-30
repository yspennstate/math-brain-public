import Mathlib.MeasureTheory.Function.Jacobian
import Mathlib.MeasureTheory.Measure.Prod
import Mathlib.Analysis.SpecialFunctions.Sqrt
import Mathlib.Analysis.SpecialFunctions.Trigonometric.DerivHyp
import Mathlib.LinearAlgebra.Matrix.Basis
import Mathlib.Tactic

/- fleet03/B14 UNCOMPILED WIP for repaired Lemma 5.3.
Exact paper source blob: 98e45d53d106db9a205051a4dd4917fc39dc2e3a.
No theorem here receives verification credit until an actual pinned Lean build
and the #print axioms output succeed. -/

open Real Set MeasureTheory
open scoped ENNReal MeasureTheory

namespace QformFiveB

def hyperbolaParamDomainB14 : Set (ℝ × ℝ) := Set.Ioi 0 ×ˢ Set.univ

noncomputable def hyperbolaBranchB14 (μp μm ε : ℝ) (p : ℝ × ℝ) : ℝ × ℝ :=
  (ε * √(p.1 / μp) * cosh p.2, √(p.1 / μm) * sinh p.2)

theorem hyperbolaBranch_level_B14_wip
    (μp μm δ τ ε : ℝ) (hp : 0 < μp) (hm : 0 < μm)
    (hδ : 0 ≤ δ) (hε : ε ^ 2 = 1) :
    μp * (hyperbolaBranchB14 μp μm ε (δ, τ)).1 ^ 2 -
      μm * (hyperbolaBranchB14 μp μm ε (δ, τ)).2 ^ 2 = δ := by
  have h1 : √(δ / μp) ^ 2 = δ / μp := Real.sq_sqrt (div_nonneg hδ hp.le)
  have h2 : √(δ / μm) ^ 2 = δ / μm := Real.sq_sqrt (div_nonneg hδ hm.le)
  have hc := cosh_sq_sub_sinh_sq τ
  simp only [hyperbolaBranchB14]
  have e : μp * (ε * √(δ / μp) * cosh τ) ^ 2 -
      μm * (√(δ / μm) * sinh τ) ^ 2 =
      ε ^ 2 * (μp * √(δ / μp) ^ 2) * cosh τ ^ 2 -
      (μm * √(δ / μm) ^ 2) * sinh τ ^ 2 := by ring
  rw [e, h1, h2, hε, mul_div_cancel₀ δ hp.ne', mul_div_cancel₀ δ hm.ne']
  linear_combination δ * hc

theorem hyperbolaBranch_injOn_B14_wip
    (μp μm ε : ℝ) (hp : 0 < μp) (hm : 0 < μm) (hε : ε ^ 2 = 1) :
    Set.InjOn (hyperbolaBranchB14 μp μm ε) hyperbolaParamDomainB14 := by
  intro p hpdom q hqdom hpq
  have hpL := hyperbolaBranch_level_B14_wip μp μm p.1 p.2 ε hp hm hpdom.1.le hε
  have hqL := hyperbolaBranch_level_B14_wip μp μm q.1 q.2 ε hp hm hqdom.1.le hε
  have hδ : p.1 = q.1 := by
    calc p.1 = μp * (hyperbolaBranchB14 μp μm ε p).1 ^ 2 -
          μm * (hyperbolaBranchB14 μp μm ε p).2 ^ 2 := hpL.symm
      _ = μp * (hyperbolaBranchB14 μp μm ε q).1 ^ 2 -
          μm * (hyperbolaBranchB14 μp μm ε q).2 ^ 2 := by rw [hpq]
      _ = q.1 := hqL
  have hsnd := congrArg Prod.snd hpq
  simp only [hyperbolaBranchB14] at hsnd
  rw [hδ] at hsnd
  have hsqrt : 0 < √(q.1 / μm) := Real.sqrt_pos.mpr (div_pos hqdom.1 hm)
  have hsinh : sinh p.2 = sinh q.2 := (mul_left_cancel₀ hsqrt.ne') hsnd
  exact Prod.ext hδ (Real.sinh_injective hsinh)

noncomputable def fderivHyperbolaBranchB14
    (μp μm ε : ℝ) (p : ℝ × ℝ) : (ℝ × ℝ) →L[ℝ] (ℝ × ℝ) :=
  (Matrix.toLin (.finTwoProd ℝ) (.finTwoProd ℝ)
    !![ε * cosh p.2 / (2 * √(p.1 * μp)),
       ε * √(p.1 / μp) * sinh p.2;
       sinh p.2 / (2 * √(p.1 * μm)),
       √(p.1 / μm) * cosh p.2]).toContinuousLinearMap

theorem abs_det_fderivHyperbolaBranchB14_wip
    (μp μm ε : ℝ) (p : ℝ × ℝ)
    (hp : 0 < μp) (hm : 0 < μm) (hδ : 0 < p.1) (hε : ε ^ 2 = 1) :
    |(fderivHyperbolaBranchB14 μp μm ε p).det| = 1 / (2 * √(μp * μm)) := by
  unfold fderivHyperbolaBranchB14
  simp only [LinearMap.det_toContinuousLinearMap, LinearMap.det_toLin,
    Matrix.det_fin_two_of]
  have e1 : √(p.1 / μm) / √(p.1 * μp) = 1 / √(μp * μm) := by
    rw [Real.sqrt_div hδ.le, Real.sqrt_mul hδ.le, Real.sqrt_mul hp.le]
    have : 0 < √p.1 := Real.sqrt_pos.mpr hδ
    have : 0 < √μp := Real.sqrt_pos.mpr hp
    have : 0 < √μm := Real.sqrt_pos.mpr hm
    field_simp
  have e2 : √(p.1 / μp) / √(p.1 * μm) = 1 / √(μp * μm) := by
    rw [Real.sqrt_div hδ.le, Real.sqrt_mul hδ.le, Real.sqrt_mul hp.le]
    have : 0 < √p.1 := Real.sqrt_pos.mpr hδ
    have : 0 < √μp := Real.sqrt_pos.mpr hp
    have : 0 < √μm := Real.sqrt_pos.mpr hm
    field_simp
  have key :
      (ε * cosh p.2 / (2 * √(p.1 * μp))) * (√(p.1 / μm) * cosh p.2) -
      (ε * √(p.1 / μp) * sinh p.2) * (sinh p.2 / (2 * √(p.1 * μm))) =
      ε * (cosh p.2 ^ 2 * (√(p.1 / μm) / √(p.1 * μp)) -
        sinh p.2 ^ 2 * (√(p.1 / μp) / √(p.1 * μm))) / 2 := by
    field_simp
  rw [key, e1, e2]
  have hc := cosh_sq_sub_sinh_sq p.2
  have hεabs : |ε| = 1 := by
    have hs : |ε| ^ 2 = 1 := by rw [sq_abs]; exact hε
    nlinarith [abs_nonneg ε]
  rw [show ε * (cosh p.2 ^ 2 * (1 / √(μp * μm)) -
      sinh p.2 ^ 2 * (1 / √(μp * μm))) / 2 =
      ε * ((cosh p.2 ^ 2 - sinh p.2 ^ 2) / (2 * √(μp * μm))) by field_simp, hc]
  rw [abs_mul, hεabs, one_mul, abs_of_pos (by positivity)]

theorem lintegral_hyperbolaBranch_B14_wip
    (μp μm ε : ℝ) (hp : 0 < μp) (hm : 0 < μm) (hε : ε ^ 2 = 1)
    (hder : ∀ p ∈ hyperbolaParamDomainB14,
      HasFDerivWithinAt (hyperbolaBranchB14 μp μm ε)
        (fderivHyperbolaBranchB14 μp μm ε p) hyperbolaParamDomainB14 p)
    (g : ℝ × ℝ → ℝ≥0∞) :
    ∫⁻ y in hyperbolaBranchB14 μp μm ε '' hyperbolaParamDomainB14, g y ∂volume =
      ∫⁻ p in hyperbolaParamDomainB14,
        ENNReal.ofReal (1 / (2 * √(μp * μm))) *
          g (hyperbolaBranchB14 μp μm ε p) ∂volume := by
  rw [lintegral_image_eq_lintegral_abs_det_fderiv_mul volume
      (measurableSet_Ioi.prod measurableSet_univ) hder
      (hyperbolaBranch_injOn_B14_wip μp μm ε hp hm hε)]
  refine setLIntegral_congr_fun
    (measurableSet_Ioi.prod measurableSet_univ) (fun p hpdom => ?_)
  rw [abs_det_fderivHyperbolaBranchB14_wip μp μm ε p hp hm hpdom.1 hε]

#print axioms QformFiveB.hyperbolaBranch_level_B14_wip
#print axioms QformFiveB.hyperbolaBranch_injOn_B14_wip
#print axioms QformFiveB.abs_det_fderivHyperbolaBranchB14_wip
#print axioms QformFiveB.lintegral_hyperbolaBranch_B14_wip

end QformFiveB
