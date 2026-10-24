import Init.Data.Rat.Lemmas

namespace FEICertificate

theorem pos_transport {c y : Rat} (hc : 0 < c) (hcy : c ≤ y) : 0 < y :=
  Rat.not_le.mp (fun h => Rat.not_le.mpr hc (Rat.le_trans hcy h))

theorem inv_antitone {c d : Rat} (hc : 0 < c) (hd : 0 < d) (hcd : c ≤ d) :
    d⁻¹ ≤ c⁻¹ := by
  have h := Rat.mul_le_mul_of_nonneg_left hcd (Rat.le_of_lt (Rat.inv_pos.mpr hc))
  rw [Rat.inv_mul_cancel c (Rat.ne_of_gt hc)] at h
  apply Rat.le_of_mul_le_mul_right (c := d) _ hd
  rw [Rat.inv_mul_cancel d (Rat.ne_of_gt hd)]
  exact h

theorem numerator_mono {a b y : Rat} (hy : 0 < y) (hab : a ≤ b) : a / y ≤ b / y := by
  rw [Rat.div_def, Rat.div_def]
  exact Rat.mul_le_mul_of_nonneg_right hab (Rat.le_of_lt (Rat.inv_pos.mpr hy))

theorem denominator_antitone {x c d : Rat} (hx : 0 ≤ x)
    (hc : 0 < c) (hd : 0 < d) (hcd : c ≤ d) : x / d ≤ x / c := by
  rw [Rat.div_def, Rat.div_def]
  exact Rat.mul_le_mul_of_nonneg_left (inv_antitone hc hd hcd) hx

theorem denominator_mono_negative {x c d : Rat} (hx : x ≤ 0)
    (hc : 0 < c) (hd : 0 < d) (hcd : c ≤ d) : x / c ≤ x / d := by
  have hnx : 0 ≤ -x := by simpa using Rat.neg_le_neg hx
  have h := denominator_antitone hnx hc hd hcd
  simp only [Rat.div_def, Rat.neg_mul, Rat.neg_le_neg_iff] at h
  simpa only [Rat.div_def] using h

theorem positive_denominator_enclosure
    {a b c d x y L U : Rat}
    (hc : 0 < c) (hcy : c ≤ y) (hyd : y ≤ d)
    (hax : a ≤ x) (hxb : x ≤ b)
    (hLac : L ≤ a / c) (hLad : L ≤ a / d)
    (hUbc : b / c ≤ U) (hUbd : b / d ≤ U) :
    L ≤ x / y ∧ x / y ≤ U := by
  have hy := pos_transport hc hcy
  have hd := pos_transport hy hyd
  cases Rat.le_total (a := 0) (b := x) with
  | inl hx =>
    exact ⟨Rat.le_trans hLad (Rat.le_trans (numerator_mono hd hax)
      (denominator_antitone hx hy hd hyd)),
      Rat.le_trans (denominator_antitone hx hc hy hcy)
      (Rat.le_trans (numerator_mono hc hxb) hUbc)⟩
  | inr hx =>
    exact ⟨Rat.le_trans hLac (Rat.le_trans (numerator_mono hc hax)
      (denominator_mono_negative hx hc hy hcy)),
      Rat.le_trans (denominator_mono_negative hx hy hd hyd)
      (Rat.le_trans (numerator_mono hd hxb) hUbd)⟩

theorem min_left (a b : Rat) : min a b ≤ a := by
  rw [Rat.min_def]
  split
  · exact Rat.le_refl
  · exact Rat.le_total.resolve_left (by assumption)

theorem min_right (a b : Rat) : min a b ≤ b := by
  rw [Rat.min_def]
  split
  · assumption
  · exact Rat.le_refl

theorem max_left (a b : Rat) : a ≤ max a b := by
  rw [Rat.max_def]
  split
  · assumption
  · exact Rat.le_refl

theorem max_right (a b : Rat) : b ≤ max a b := by
  rw [Rat.max_def]
  split
  · exact Rat.le_refl
  · exact Rat.le_total.resolve_left (by assumption)

theorem four_corner_enclosure
    {a b c d x y : Rat} (hc : 0 < c) (hcy : c ≤ y) (hyd : y ≤ d)
    (hax : a ≤ x) (hxb : x ≤ b) :
    min (min (a / c) (a / d)) (min (b / c) (b / d)) ≤ x / y ∧
    x / y ≤ max (max (a / c) (a / d)) (max (b / c) (b / d)) := by
  apply positive_denominator_enclosure hc hcy hyd hax hxb
  · exact Rat.le_trans (min_left _ _) (min_left _ _)
  · exact Rat.le_trans (min_left _ _) (min_right _ _)
  · exact Rat.le_trans (max_left _ _) (max_right _ _)
  · exact Rat.le_trans (max_right _ _) (max_right _ _)

#print axioms positive_denominator_enclosure
#print axioms four_corner_enclosure

theorem old_negative_rule_reverses : (-1 : Rat) / 2 > (-1 : Rat) / 1 := by decide +kernel
theorem negative_corner_regression :
    min (min ((-2 : Rat) / 1) ((-2 : Rat) / 2))
        (min ((-1 : Rat) / 1) ((-1 : Rat) / 2)) = -2 ∧
    max (max ((-2 : Rat) / 1) ((-2 : Rat) / 2))
        (max ((-1 : Rat) / 1) ((-1 : Rat) / 2)) = (-1 : Rat) / 2 := by decide +kernel
#print axioms old_negative_rule_reverses
#print axioms negative_corner_regression
end FEICertificate
