import Mathlib.Data.Set.Basic
import Mathlib.Order.MinMax
import Mathlib.Order.Monotone.Basic

/- Exact branching membership identity used to derive
   a = (t*a + 2*a*b - a*a)/2 in SECOND_ATTEMPT.md.
   This theorem concerns the set-valued image, not physical feasibility. -/
theorem min_image_membership {State : Type} [LinearOrder State]
    (A B : Set State) (t : State) :
    (∃ x ∈ A, ∃ y ∈ B, min x y = t) ↔
      ((t ∈ A ∧ ∃ y ∈ B, t ≤ y) ∨
       (t ∈ B ∧ ∃ x ∈ A, t ≤ x)) := by
  constructor
  · rintro ⟨x, hx, y, hy, hxy⟩
    by_cases h : x ≤ y
    · have hxEq : x = t := by simpa [min_eq_left h] using hxy
      subst x
      exact Or.inl ⟨hx, y, hy, h⟩
    · have h' : y ≤ x := le_of_not_ge h
      have hyEq : y = t := by simpa [min_eq_right h'] using hxy
      subst y
      exact Or.inr ⟨hy, x, hx, h'⟩
  · rintro (⟨ht, y, hy, h⟩ | ⟨ht, x, hx, h⟩)
    · exact ⟨t, ht, y, hy, min_eq_left h⟩
    · exact ⟨x, hx, t, ht, min_eq_right h⟩

/- Key order argument for Proposition H. -/
theorem antitone_fixed_points_comparable {State : Type} [PartialOrder State]
    (f : State → State) (hf : Antitone f) {x y : State}
    (hx : f x = x) (hy : f y = y) (h : x ≤ y) : x = y := by
  apply le_antisymm h
  simpa [hx, hy] using hf h
