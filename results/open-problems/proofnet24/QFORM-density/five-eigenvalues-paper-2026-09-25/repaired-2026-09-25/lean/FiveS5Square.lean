import Mathlib.MeasureTheory.Measure.Lebesgue.Basic
import Mathlib.MeasureTheory.Group.Measure
import Mathlib.Analysis.SpecialFunctions.Sqrt
import Mathlib.Tactic

/-!
The second assertion of Lemma 5.1 of "Quadratic forms with five large singular values have bounded densities"
(repaired text, sha256 90f859b7): for `a ≠ 0`, every interval `U` of length `2ρ` and all real `β`, `γ`, the set
`{y : a y² + β y + γ ∈ U}` has Lebesgue measure at most `2√(2ρ/|a|)`.

An interval of length `2ρ` lies in a closed interval `[c, c + 2ρ]`, so it is enough to treat those. Completing the square,
`a y² + β y + γ = a (y + y₀)² + k`, and the translation invariance of Lebesgue measure reduce the set to
`{s : a s² + k ∈ [c, c + 2ρ]} ⊆ {s : s² ∈ [u, u + δ]}` with `δ = 2ρ/|a|` (`lemma51b`). That set lies in
`[-√(u+δ), -√(max u 0)] ∪ [√(max u 0), √(u+δ)]`, of measure at most `2√δ` since `√(x + δ) - √x ≤ √δ`
(`measure_sq_mem_Icc_le`).
-/

open MeasureTheory Set

namespace QformFiveB

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

end QformFiveB
