import Mathlib.Data.Real.Basic

-- A finite algebraic implication used to handle closed lower-tail events.
-- This checks neither singular-value theory nor the probability argument.
theorem product_threshold_two (a b u : ℝ) (hu : 0 ≤ u)
    (h : a * b ≤ u * u) : a ≤ u ∨ b ≤ u := by
  by_contra hn
  have ha : u < a := lt_of_not_ge (fun h' => hn (Or.inl h'))
  have hb : u < b := lt_of_not_ge (fun h' => hn (Or.inr h'))
  have ha0 : 0 < a := lt_of_le_of_lt hu ha
  have hlast : a * u < a * b := mul_lt_mul_of_pos_left hb ha0
  have hfirst : u * u ≤ a * u := mul_le_mul_of_nonneg_right (le_of_lt ha) hu
  exact (not_lt_of_ge h) (lt_of_le_of_lt hfirst hlast)

#print axioms product_threshold_two
