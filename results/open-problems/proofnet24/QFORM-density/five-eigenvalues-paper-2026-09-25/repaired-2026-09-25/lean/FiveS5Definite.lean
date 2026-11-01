import Mathlib.Analysis.SpecialFunctions.PolarCoord
import Mathlib.MeasureTheory.Function.JacobianOneDim
import Mathlib.MeasureTheory.Measure.Lebesgue.EqHaar
import Mathlib.MeasureTheory.Constructions.BorelSpace.Real
import Mathlib.LinearAlgebra.Matrix.ToLin
import Mathlib.Tactic

/-!
Lemma 5.2 of "Quadratic forms with five large singular values have bounded densities" (repaired text,
sha256 90f859b7): if `W ∈ ℝ²` has a density bounded by `L` and `q` is a quadratic polynomial on `ℝ²` whose quadratic part
has a definite symmetric matrix `B`, then `q(W)` has a density bounded by `π L / √(det B)`.

The density is stated as a measure inequality, `Law(q(W)) ≤ (π L / √(det B)) · Lebesgue`. The proof uses the level-set
area in place of the paper's density formula: after completing the square and a linear change of variables with
determinant `√(det B)`, the set `{w : q(w) ∈ S}` becomes `{u : |u|² ∈ S - v}`, whose area is `π |(S - v) ∩ (0, ∞)|` by
polar coordinates (`volume_sq_norm_mem`), so `P(q(W) ∈ S) ≤ L |{q ∈ S}| ≤ π L |S| / √(det B)`.

* `volume_sq_mem_half`: `|A ∩ (0, ∞)| = 2 ∫_0^∞ r 1_A(r²) dr` (the substitution `δ = r²`).
* `volume_sq_norm_mem`: `|{u ∈ ℝ² : |u|² ∈ A}| = π |A ∩ (0, ∞)|`.
* `volume_quad_mem`: for `a > 0` and `ac - b² > 0`, `|{w : a w₁² + 2b w₁w₂ + c w₂² ∈ A}| = π |A ∩ (0, ∞)| / √(ac - b²)`.
* `quad`, `quad_expand`: the quadratic polynomial `a w₁² + 2b w₁w₂ + c w₂² + d w₁ + e w₂ + f` and its expansion about a
  point, used to complete the square.
* `lemma52_pos`, `lemma52`: Lemma 5.2, for a positive definite and for a definite quadratic part.
-/

open MeasureTheory Set Real
open scoped ENNReal

namespace QformFiveB

namespace Definite

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

end Definite

end QformFiveB
