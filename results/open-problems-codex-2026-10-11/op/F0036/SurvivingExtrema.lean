import Mathlib.Data.Real.Basic

-- The canonical bounds preserve a strict gap on the whole survival interval.
theorem surviving_extrema (l f g r : ℝ → ℝ) (a b : ℝ)
    (left_bound : ∀ t, a < t → t < b → l t ≤ f t)
    (ordered : ∀ t, a < t → t < b → f t < g t)
    (right_bound : ∀ t, a < t → t < b → g t ≤ r t) :
    ∀ t, a < t → t < b → l t < r t := by
  intro t hat htb
  exact lt_of_le_of_lt (left_bound t hat htb)
    (lt_of_lt_of_le (ordered t hat htb) (right_bound t hat htb))
