import Mathlib.Data.Set.Basic

-- Algebra used in the finite-recoloring reduction; no analytic assertion here.
theorem grouped_overlap {I A : Type*} (K : I → Set A) (c : I → Bool) :
    {x | (∃ i, c i = true ∧ x ∈ K i) ∧ (∃ j, c j = false ∧ x ∈ K j)} =
    {x | ∃ i j, c i = true ∧ c j = false ∧ x ∈ K i ∧ x ∈ K j} := by
  apply Set.ext
  intro x
  constructor
  · intro h
    obtain ⟨⟨i, hi, hxi⟩, ⟨j, hj, hxj⟩⟩ := h
    exact ⟨i, j, hi, hj, hxi, hxj⟩
  · intro h
    obtain ⟨i, j, hi, hj, hxi, hxj⟩ := h
    exact ⟨⟨i, hi, hxi⟩, ⟨j, hj, hxj⟩⟩
