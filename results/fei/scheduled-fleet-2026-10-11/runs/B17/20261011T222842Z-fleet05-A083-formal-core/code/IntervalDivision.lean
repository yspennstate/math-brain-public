import Mathlib.Algebra.Order.GroupWithZero.Basic
import Mathlib.Algebra.Field.Basic

/- A signed numerator must use all four corners. No entropy assumptions. -/
namespace FEICertificate

variable {K : Type*} [Field K] [LinearOrder K] [IsStrictOrderedRing K]

theorem positive_denominator_enclosure
    {a b c d x y L U : K}
    (hc : 0 < c) (hcy : c ≤ y) (hyd : y ≤ d)
    (hax : a ≤ x) (hxb : x ≤ b)
    (hLac : L ≤ a / c) (hLad : L ≤ a / d)
    (hUbc : b / c ≤ U) (hUbd : b / d ≤ U) :
    L ≤ x / y ∧ x / y ≤ U := by
  have hy : 0 < y := lt_of_lt_of_le hc hcy
  have hd : 0 < d := lt_of_lt_of_le hy hyd
  by_cases hx : 0 ≤ x
  · constructor
    · exact le_trans hLad (le_trans ((div_le_div_iff_of_pos_right hd).2 hax)
        (div_le_div_of_nonneg_left hx hy hyd))
    · exact le_trans (div_le_div_of_nonneg_left hx hc hcy)
        (le_trans ((div_le_div_iff_of_pos_right hc).2 hxb) hUbc)
  · have hnx : 0 ≤ -x := neg_nonneg.mpr (le_of_not_ge hx)
    have hneg1 : x / c ≤ x / y := by
      have h := div_le_div_of_nonneg_left hnx hc hcy
      simpa only [neg_div, neg_le_neg_iff] using h
    have hneg2 : x / y ≤ x / d := by
      have h := div_le_div_of_nonneg_left hnx hy hyd
      simpa only [neg_div, neg_le_neg_iff] using h
    exact ⟨le_trans hLac (le_trans ((div_le_div_iff_of_pos_right hc).2 hax) hneg1),
      le_trans hneg2 (le_trans ((div_le_div_iff_of_pos_right hd).2 hxb) hUbd)⟩

theorem four_corner_enclosure
    {a b c d x y : K} (hc : 0 < c) (hcy : c ≤ y) (hyd : y ≤ d)
    (hax : a ≤ x) (hxb : x ≤ b) :
    min (min (a / c) (a / d)) (min (b / c) (b / d)) ≤ x / y ∧
    x / y ≤ max (max (a / c) (a / d)) (max (b / c) (b / d)) := by
  apply positive_denominator_enclosure hc hcy hyd hax hxb
  · exact le_trans (min_le_left _ _) (min_le_left _ _)
  · exact le_trans (min_le_left _ _) (min_le_right _ _)
  · exact le_trans (le_max_left _ _) (le_max_right _ _)
  · exact le_trans (le_max_right _ _) (le_max_right _ _)

#print axioms positive_denominator_enclosure
#print axioms four_corner_enclosure
end FEICertificate
