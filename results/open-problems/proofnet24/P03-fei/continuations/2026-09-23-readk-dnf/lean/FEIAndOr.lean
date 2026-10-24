import Mathlib

/-!
The inequality behind the sharp constant `2 + 4 log₂ e` for OR, AND and XOR gates under product measures
(Lemma 5.5 of the paper): for `a₁, …, a_m ∈ (0, 1]` with `Z = ∏ aⱼ`,

  `Φ(a) = ∑ⱼ (aⱼ - Z) log (1/aⱼ) ≤ 2 R(a)`,  `R(a) = ∑ⱼ (1 - aⱼ) - 1 + Z`.
-/

open Real

namespace FEIAndOr

/-- `t log(1/t) ≤ 1 - t` for `t > 0`. -/
theorem tlog_le (t : ℝ) (ht : 0 < t) : t * Real.log (1 / t) ≤ 1 - t := by
  have h := Real.one_sub_inv_le_log_of_pos ht
  have h2 : t * (1 - t⁻¹) ≤ t * Real.log t := mul_le_mul_of_nonneg_left h ht.le
  have h3 : t * (1 - t⁻¹) = t - 1 := by field_simp
  rw [one_div, Real.log_inv, mul_neg]
  linarith

noncomputable def S1 (l : List ℝ) : ℝ := (l.map (fun a => a * Real.log (1 / a))).sum
noncomputable def S2 (l : List ℝ) : ℝ := (l.map (fun a => Real.log (1 / a))).sum
noncomputable def D (l : List ℝ) : ℝ := (l.map (fun a => 1 - a)).sum
/-- `Φ(a) = ∑ⱼ (aⱼ - Z) log(1/aⱼ)`, written as `S1 - Z * S2`. -/
noncomputable def Phi (l : List ℝ) : ℝ := S1 l - l.prod * S2 l
noncomputable def R (l : List ℝ) : ℝ := D l - 1 + l.prod

theorem sum_sub_mul (l : List ℝ) (Z : ℝ) :
    (l.map (fun a => a * Real.log (1 / a))).sum - Z * (l.map (fun a => Real.log (1 / a))).sum
      = (l.map (fun a => (a - Z) * Real.log (1 / a))).sum := by
  induction l with
  | nil => simp
  | cons b t ih =>
    simp only [List.map_cons, List.sum_cons]
    linear_combination ih

/-- `Φ` is the sum in the statement of the lemma. -/
theorem Phi_eq (l : List ℝ) :
    Phi l = (l.map (fun a => (a - l.prod) * Real.log (1 / a))).sum := by
  unfold Phi S1 S2
  exact sum_sub_mul l l.prod

theorem prod_pos_le_one : ∀ l : List ℝ, (∀ a ∈ l, 0 < a ∧ a ≤ 1) → 0 < l.prod ∧ l.prod ≤ 1
  | [], _ => by simp
  | b :: t, h => by
    have hb := h b (by simp)
    have ht := prod_pos_le_one t (fun a ha => h a (by simp [ha]))
    rw [List.prod_cons]
    constructor
    · exact mul_pos hb.1 ht.1
    · nlinarith [hb.1, hb.2, ht.1, ht.2]

theorem S2_eq : ∀ l : List ℝ, (∀ a ∈ l, 0 < a ∧ a ≤ 1) → S2 l = Real.log (1 / l.prod)
  | [], _ => by simp [S2]
  | b :: t, h => by
    have hb := h b (by simp)
    have ht := fun a ha => h a (List.mem_cons_of_mem b ha)
    have ih := S2_eq t ht
    have hP := (prod_pos_le_one t ht).1
    unfold S2 at ih ⊢
    rw [List.map_cons, List.sum_cons, ih, List.prod_cons]
    rw [← Real.log_mul (one_div_ne_zero hb.1.ne') (one_div_ne_zero hP.ne')]
    congr 1
    first
      | rw [one_div_mul_one_div]
      | field_simp
      | ring

theorem Phi_le_two_R : ∀ l : List ℝ, (∀ a ∈ l, 0 < a ∧ a ≤ 1) → Phi l ≤ 2 * R l
  | [], _ => by simp [Phi, R, S1, S2, D]
  | b :: t, h => by
    have hb := h b (by simp)
    have ht := fun a ha => h a (List.mem_cons_of_mem b ha)
    have ih := Phi_le_two_R t ht
    have hPP := prod_pos_le_one t ht
    have hS2 := S2_eq t ht
    set P := t.prod with hPdef
    have h1 : b * Real.log (1 / b) ≤ 1 - b := tlog_le b hb.1
    have h2 : P * Real.log (1 / P) ≤ 1 - P := tlog_le P hPP.1
    have h1' : b * Real.log (1 / b) * (1 - P) ≤ (1 - b) * (1 - P) :=
      mul_le_mul_of_nonneg_right h1 (by linarith [hPP.2])
    have h2' : P * Real.log (1 / P) * (1 - b) ≤ (1 - P) * (1 - b) :=
      mul_le_mul_of_nonneg_right h2 (by linarith [hb.2])
    unfold Phi R S1 S2 D at ih ⊢
    simp only [List.map_cons, List.sum_cons, List.prod_cons]
    unfold S2 at hS2
    rw [← hPdef] at *
    rw [hS2] at ih ⊢
    nlinarith [ih, h1', h2']

end FEIAndOr
