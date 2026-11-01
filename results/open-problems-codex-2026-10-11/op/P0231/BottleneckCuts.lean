import Mathlib.Data.Set.Basic

namespace P0231SecondAttempt

inductive Route {V : Type*} (E : V → V → Prop) : V → V → Prop
  | refl (v : V) : Route E v v
  | snoc {a b c : V} : Route E a b → E b c → Route E a c

theorem route_stays_in_closed_set {V : Type*} {E : V → V → Prop}
    (S : Set V) (closed : ∀ x y, E x y → x ∈ S → y ∈ S)
    {a b : V} (p : Route E a b) : a ∈ S → b ∈ S := by
  induction p with
  | refl => exact fun ha => ha
  | snoc p h ih =>
    intro ha
    exact closed _ _ h (ih ha)

-- Apply E to edges with interface dimension strictly greater than a threshold.
-- This is the finite/path algebra, not an assertion about Poisson geometry.
theorem no_route_iff_closed_separating_cut {V : Type*}
    (E : V → V → Prop) (r b : V) :
    (¬ Route E r b) ↔
      ∃ S : Set V, r ∈ S ∧ b ∉ S ∧
        ∀ x y, E x y → x ∈ S → y ∈ S := by
  constructor
  · intro h
    refine ⟨{x | Route E r x}, Route.refl r, h, ?_⟩
    intro x y hxy hx
    exact Route.snoc hx hxy
  · intro h p
    obtain ⟨S, hr, hb, closed⟩ := h
    exact hb (route_stays_in_closed_set S closed p hr)

end P0231SecondAttempt
