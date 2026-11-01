import Mathlib.Algebra.Group.Basic
import Mathlib.Data.Set.Defs

-- Algebraic core of the diameter argument. No probability theorem is assumed here.
theorem boundary_eq_of_no_displacements {A : Type*} [AddCommGroup A]
    (R H : Set A)
    (hsep : ∀ x ∈ R, ∀ y ∈ R, y - x ∉ H) :
    {x | x ∈ R ∧ ∀ h ∈ H, x + h ∉ R} = R := by
  apply Set.ext
  intro x
  constructor
  · intro hx
    exact hx.1
  · intro hx
    refine ⟨hx, ?_⟩
    intro h hh hshift
    have hbad := hsep x hx (x + h) hshift
    apply hbad
    simpa only [add_sub_cancel_left] using hh
