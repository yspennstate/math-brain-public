import Mathlib.MeasureTheory.Measure.Prod
import Mathlib.MeasureTheory.Measure.Lebesgue.Basic
import Mathlib.MeasureTheory.Measure.Typeclasses.Probability
import Mathlib.MeasureTheory.Group.Measure
import Mathlib.MeasureTheory.Integral.Lebesgue.Basic
import Mathlib.MeasureTheory.Constructions.Pi
import Mathlib.Topology.Instances.Matrix
import Mathlib.Data.Matrix.Mul
import Mathlib.Analysis.SpecialFunctions.ImproperIntegrals
import Mathlib.Analysis.SpecialFunctions.Sqrt
import Mathlib.Analysis.SpecialFunctions.Log.Basic
import Mathlib.Tactic

/-!
Lemma 5.4 of "Quadratic forms with five large singular values have bounded densities" (repaired text, sha256 90f859b7),
the diagonal case of (5.2) from its hypotheses: `X` has independent coordinates with densities bounded by one, and
`R = XᵀSX + bᵀX + c`. If `|S_ii| ≥ L/2` for some `i`, condition on the other coordinates: `R` becomes a quadratic
polynomial in `X_i` with leading coefficient `S_ii`, and `P(|R - a| < ρ) ≤ 2√(2ρ/|S_ii|) ≤ 4√(ρ/L)`.

* `quad_split`: `R(y eᵢ + w) = S_ii y² + β y + γ`;
* `insertNth_eq`, `betaC`, `gammaC`: the coordinates other than `i` fixed;
* `lemma54_diag_pi`: the product law `Measure.pi μ` splits as `μ i ⊗ Measure.pi (μ ∘ i.succAbove)`
  (`measurePreserving_piFinSuccAbove`), and the one-coordinate bound `lemma54_diag_prob` applies;
* `lemma54_diag_case`: with `|S_ii| ≥ L/2`, the bound `4√(ρ/L)`.

Lemma 5.1 (second assertion) and `lemma54_diag_prob`, `lemma54_diag_const` are repeated from `FiveS5Concentration.lean`.
-/

open MeasureTheory Set Matrix
open scoped ENNReal

namespace QformFiveB

namespace Reduce


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


/-! ### The one-coordinate reduction -/

/-- `R(y eᵢ + w) = S_ii y² + β y + γ`: `R = xᵀSx + bᵀx + c` is a quadratic polynomial in the `i`-th coordinate. -/
theorem quad_split {n : ℕ} (S : Matrix (Fin (n + 1)) (Fin (n + 1)) ℝ) (b : Fin (n + 1) → ℝ) (c : ℝ)
    (i : Fin (n + 1)) (y : ℝ) (w : Fin (n + 1) → ℝ) :
    (y • (Pi.single i (1 : ℝ) : Fin (n + 1) → ℝ) + w) ⬝ᵥ (S *ᵥ (y • (Pi.single i (1 : ℝ) : Fin (n + 1) → ℝ) + w)) + b ⬝ᵥ (y • (Pi.single i (1 : ℝ) : Fin (n + 1) → ℝ) + w) + c
      = S i i * y ^ 2
        + ((Pi.single i (1 : ℝ) : Fin (n + 1) → ℝ) ⬝ᵥ (S *ᵥ w) + w ⬝ᵥ (S *ᵥ (Pi.single i (1 : ℝ) : Fin (n + 1) → ℝ)) + b ⬝ᵥ (Pi.single i (1 : ℝ) : Fin (n + 1) → ℝ)) * y
        + (w ⬝ᵥ (S *ᵥ w) + b ⬝ᵥ w + c) := by
  have hii : (Pi.single i (1 : ℝ) : Fin (n + 1) → ℝ) ⬝ᵥ (S *ᵥ (Pi.single i (1 : ℝ) : Fin (n + 1) → ℝ)) = S i i := by
    simp [dotProduct, Matrix.mulVec, Pi.single_apply]
  simp only [Matrix.mulVec_add, Matrix.mulVec_smul, dotProduct_add, add_dotProduct, dotProduct_smul,
    smul_dotProduct, smul_eq_mul, hii]
  ring

/-- Inserting `y` as the `i`-th coordinate is `y eᵢ` plus the insertion of `0`. -/
theorem insertNth_eq {n : ℕ} (i : Fin (n + 1)) (y : ℝ) (z : Fin n → ℝ) :
    (Fin.insertNth i y z : Fin (n + 1) → ℝ) = y • (Pi.single i (1 : ℝ) : Fin (n + 1) → ℝ) + (Fin.insertNth i (0 : ℝ) z : Fin (n + 1) → ℝ) := by
  funext k
  rcases Fin.eq_self_or_eq_succAbove i k with h | ⟨j, h⟩
  · rw [h]
    simp
  · rw [h]
    simp [Fin.succAbove_ne]

theorem measurable_insertNth0 {n : ℕ} (i : Fin (n + 1)) :
    Measurable fun z : Fin n → ℝ => (Fin.insertNth i (0 : ℝ) z : Fin (n + 1) → ℝ) := by
  have h : Measurable fun z : Fin n → ℝ =>
      (MeasurableEquiv.piFinSuccAbove (fun _ : Fin (n + 1) => ℝ) i).symm ((0 : ℝ), z) :=
    (MeasurableEquiv.piFinSuccAbove (fun _ : Fin (n + 1) => ℝ) i).symm.measurable.comp
      (measurable_const.prodMk measurable_id)
  exact h

/-- The coefficient of `X_i` once the other coordinates `z` are fixed. -/
noncomputable def betaC {n : ℕ} (S : Matrix (Fin (n + 1)) (Fin (n + 1)) ℝ) (b : Fin (n + 1) → ℝ)
    (i : Fin (n + 1)) (z : Fin n → ℝ) : ℝ :=
  (Pi.single i (1 : ℝ) : Fin (n + 1) → ℝ) ⬝ᵥ (S *ᵥ (Fin.insertNth i (0 : ℝ) z : Fin (n + 1) → ℝ))
    + (Fin.insertNth i (0 : ℝ) z : Fin (n + 1) → ℝ) ⬝ᵥ (S *ᵥ (Pi.single i (1 : ℝ) : Fin (n + 1) → ℝ)) + b ⬝ᵥ (Pi.single i (1 : ℝ) : Fin (n + 1) → ℝ)

/-- The constant term once the other coordinates `z` are fixed. -/
noncomputable def gammaC {n : ℕ} (S : Matrix (Fin (n + 1)) (Fin (n + 1)) ℝ) (b : Fin (n + 1) → ℝ) (c : ℝ)
    (i : Fin (n + 1)) (z : Fin n → ℝ) : ℝ :=
  (Fin.insertNth i (0 : ℝ) z : Fin (n + 1) → ℝ) ⬝ᵥ (S *ᵥ (Fin.insertNth i (0 : ℝ) z : Fin (n + 1) → ℝ))
    + b ⬝ᵥ (Fin.insertNth i (0 : ℝ) z : Fin (n + 1) → ℝ) + c

theorem measurable_betaC {n : ℕ} (S : Matrix (Fin (n + 1)) (Fin (n + 1)) ℝ) (b : Fin (n + 1) → ℝ)
    (i : Fin (n + 1)) : Measurable (betaC S b i) := by
  have hc : Continuous fun v : Fin (n + 1) → ℝ =>
      (Pi.single i (1 : ℝ) : Fin (n + 1) → ℝ) ⬝ᵥ (S *ᵥ v) + v ⬝ᵥ (S *ᵥ (Pi.single i (1 : ℝ) : Fin (n + 1) → ℝ)) + b ⬝ᵥ (Pi.single i (1 : ℝ) : Fin (n + 1) → ℝ) := by
    fun_prop
  exact hc.measurable.comp (measurable_insertNth0 i)

theorem measurable_gammaC {n : ℕ} (S : Matrix (Fin (n + 1)) (Fin (n + 1)) ℝ) (b : Fin (n + 1) → ℝ) (c : ℝ)
    (i : Fin (n + 1)) : Measurable (gammaC S b c i) := by
  have hc : Continuous fun v : Fin (n + 1) → ℝ => v ⬝ᵥ (S *ᵥ v) + b ⬝ᵥ v + c := by
    fun_prop
  exact hc.measurable.comp (measurable_insertNth0 i)

/-- **Lemma 5.4, the diagonal case of (5.2), from its hypotheses.** Let `X` have independent coordinates with densities
bounded by one (law `Measure.pi μ` with `μ j ≤ Lebesgue`), `R = XᵀSX + bᵀX + c` and `S_ii ≠ 0`. Conditioning on the
coordinates other than `i` (the product law splits as `μ i ⊗ Measure.pi (μ ∘ i.succAbove)`), `R` is the quadratic
`S_ii X_i² + β X_i + γ` in `X_i`, and `P(|R - a| < ρ) ≤ 2√(2ρ/|S_ii|)`. -/
theorem lemma54_diag_pi {n : ℕ} (μ : Fin (n + 1) → Measure ℝ) [∀ j, IsProbabilityMeasure (μ j)]
    (hμ : ∀ j, μ j ≤ volume) (S : Matrix (Fin (n + 1)) (Fin (n + 1)) ℝ) (b : Fin (n + 1) → ℝ) (c : ℝ)
    (i : Fin (n + 1)) (hs : S i i ≠ 0) (a ρ : ℝ) (hρ : 0 ≤ ρ) :
    (Measure.pi μ) {x : Fin (n + 1) → ℝ | |x ⬝ᵥ (S *ᵥ x) + b ⬝ᵥ x + c - a| < ρ}
      ≤ ENNReal.ofReal (2 * Real.sqrt (2 * ρ / |S i i|)) := by
  set e := MeasurableEquiv.piFinSuccAbove (fun _ : Fin (n + 1) => ℝ) i with he
  have hmp : MeasurePreserving e (Measure.pi μ) ((μ i).prod (Measure.pi fun j => μ (i.succAbove j))) :=
    measurePreserving_piFinSuccAbove μ i
  have hsymm : ∀ p : ℝ × (Fin n → ℝ), e.symm p = (Fin.insertNth i p.1 p.2 : Fin (n + 1) → ℝ) := by
    intro p
    rfl
  have hpre : e ⁻¹' (e.symm ⁻¹' {x : Fin (n + 1) → ℝ | |x ⬝ᵥ (S *ᵥ x) + b ⬝ᵥ x + c - a| < ρ})
      = {x : Fin (n + 1) → ℝ | |x ⬝ᵥ (S *ᵥ x) + b ⬝ᵥ x + c - a| < ρ} := by
    ext x
    simp only [mem_preimage, MeasurableEquiv.symm_apply_apply]
  have hset : e.symm ⁻¹' {x : Fin (n + 1) → ℝ | |x ⬝ᵥ (S *ᵥ x) + b ⬝ᵥ x + c - a| < ρ}
      = {p : ℝ × (Fin n → ℝ) | |S i i * p.1 ^ 2 + betaC S b i p.2 * p.1 + gammaC S b c i p.2 - a| < ρ} := by
    ext p
    simp only [mem_preimage, mem_setOf_eq]
    rw [hsymm p, insertNth_eq i p.1 p.2, quad_split]
    rfl
  calc (Measure.pi μ) {x : Fin (n + 1) → ℝ | |x ⬝ᵥ (S *ᵥ x) + b ⬝ᵥ x + c - a| < ρ}
      = (Measure.pi μ) (e ⁻¹' (e.symm ⁻¹' {x : Fin (n + 1) → ℝ | |x ⬝ᵥ (S *ᵥ x) + b ⬝ᵥ x + c - a| < ρ})) := by
        rw [hpre]
    _ = ((μ i).prod (Measure.pi fun j => μ (i.succAbove j)))
          (e.symm ⁻¹' {x : Fin (n + 1) → ℝ | |x ⬝ᵥ (S *ᵥ x) + b ⬝ᵥ x + c - a| < ρ}) :=
        hmp.measure_preimage_equiv _
    _ = ((μ i).prod (Measure.pi fun j => μ (i.succAbove j)))
          {p : ℝ × (Fin n → ℝ) | |S i i * p.1 ^ 2 + betaC S b i p.2 * p.1 + gammaC S b c i p.2 - a| < ρ} := by
        rw [hset]
    _ ≤ ENNReal.ofReal (2 * Real.sqrt (2 * ρ / |S i i|)) :=
        lemma54_diag_prob (μ i) (hμ i) (Measure.pi fun j => μ (i.succAbove j)) (betaC S b i) (gammaC S b c i)
          (measurable_betaC S b i) (measurable_gammaC S b c i) (S i i) a ρ hs hρ

/-- **Lemma 5.4, the diagonal case, with the paper's constant.** If `|S_ii| ≥ L/2` for some `i`, then
`P(|R - a| < ρ) ≤ 4√(ρ/L)`. -/
theorem lemma54_diag_case {n : ℕ} (μ : Fin (n + 1) → Measure ℝ) [∀ j, IsProbabilityMeasure (μ j)]
    (hμ : ∀ j, μ j ≤ volume) (S : Matrix (Fin (n + 1)) (Fin (n + 1)) ℝ) (b : Fin (n + 1) → ℝ) (c : ℝ)
    (L : ℝ) (hL : 0 < L) (i : Fin (n + 1)) (hSi : L / 2 ≤ |S i i|) (a ρ : ℝ) (hρ : 0 ≤ ρ) :
    (Measure.pi μ) {x : Fin (n + 1) → ℝ | |x ⬝ᵥ (S *ᵥ x) + b ⬝ᵥ x + c - a| < ρ}
      ≤ ENNReal.ofReal (4 * Real.sqrt (ρ / L)) := by
  have hs : S i i ≠ 0 := by
    intro h
    rw [h, abs_zero] at hSi
    linarith
  exact (lemma54_diag_pi μ hμ S b c i hs a ρ hρ).trans
    (ENNReal.ofReal_le_ofReal (lemma54_diag_const ρ L (S i i) hρ hL hSi))


end Reduce

end QformFiveB
