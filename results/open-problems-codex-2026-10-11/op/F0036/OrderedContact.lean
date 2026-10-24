import Mathlib.Data.Real.Basic

-- A fixed pair of tails can have at most one first ordered contact after s.
theorem ordered_contact_unique (f g : ℝ → ℝ) (s t u : ℝ)
    (hst : s < t) (hsu : s < u)
    (ht : f t = g t) (hu : f u = g u)
    (before_t : ∀ v, s < v → v < t → f v < g v)
    (before_u : ∀ v, s < v → v < u → f v < g v) :
    t = u := by
  rcases lt_trichotomy t u with h | h | h
  · exact False.elim ((ne_of_lt (before_u t hst h)) ht)
  · exact h
  · exact False.elim ((ne_of_lt (before_t u hsu h)) hu)
