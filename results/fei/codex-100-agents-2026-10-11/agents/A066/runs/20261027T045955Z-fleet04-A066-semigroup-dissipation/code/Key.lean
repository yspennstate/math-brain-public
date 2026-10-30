import Mathlib

theorem rank_one_involution {M : Type*} [AddCommGroup M] [Module (ZMod 2) M]
    (l : M →ₗ[ZMod 2] ZMod 2) (d x : M) (hd : l d = 0) :
    (x + l x • d) + l (x + l x • d) • d = x := by
  have he : l (x + l x • d) = l x := by simp [hd]
  rw [he, add_assoc, ← add_smul]
  have hh : ∀ a : ZMod 2, a + a = 0 := by decide
  rw [hh, zero_smul, add_zero]
