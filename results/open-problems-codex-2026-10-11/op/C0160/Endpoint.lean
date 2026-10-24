import Mathlib.Order.Bounds.Basic

open scoped Classical

-- The formalized step is order-theoretic, not a formalization of percolation.
theorem upper_set_above_glb {α : Type*} [LinearOrder α] (U : Set α) (a b : α)
    (hglb : IsGLB U a)
    (hup : ∀ x ∈ U, ∀ y : α, x ≤ y → y ≤ b → y ∈ U)
    {p : α} (hap : a < p) (hp : p ≤ b) : p ∈ U := by
  by_contra hnot
  have hlower : p ∈ lowerBounds U := by
    intro x hx
    by_contra hpx
    have hxp : x ≤ p := le_of_lt (lt_of_not_ge hpx)
    exact hnot (hup x hx p hxp hp)
  have hpa : p ≤ a := hglb.2 hlower
  exact (not_lt_of_ge hpa) hap

theorem upper_set_interval {α : Type*} [LinearOrder α] (U : Set α) (a b : α)
    (hglb : IsGLB U a) (hbound : ∀ x ∈ U, x ≤ b)
    (hup : ∀ x ∈ U, ∀ y : α, x ≤ y → y ≤ b → y ∈ U) :
    U = Set.Ioc a b ∪ (if a ∈ U then {a} else ∅) := by
  classical
  apply Set.ext
  intro x
  constructor
  · intro hx
    have hax : a ≤ x := hglb.1 hx
    by_cases heq : x = a
    · subst x
      exact Or.inr (by simp [hx])
    · exact Or.inl ⟨lt_of_le_of_ne hax (Ne.symm heq), hbound x hx⟩
  · intro hx
    rcases hx with hx | hx
    · exact upper_set_above_glb U a b hglb hup hx.1 hx.2
    · by_cases ha : a ∈ U
      · have heq : x = a := by simpa [ha] using hx
        simpa [heq] using ha
      · simp [ha] at hx

theorem missing_endpoint_prevents_closed_interval {α : Type*} [LinearOrder α]
    (U : Set α) (a b : α)
    (ha : a ≤ b) (hnot : a ∉ U) : U ≠ Set.Icc a b := by
  intro heq
  apply hnot
  rw [heq]
  exact ⟨le_refl a, ha⟩
