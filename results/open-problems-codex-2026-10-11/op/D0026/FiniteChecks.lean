import Mathlib.Data.Finset.Basic

/- In this file membership means infection (spin 0).
   These are finite combinatorial certificates, not the convergence theorem. -/

def fewer : Finset (Fin 3) := {1}
def more : Finset (Fin 3) := {0, 1}
def facilitatedMiddle (s : Finset (Fin 3)) : Prop := 0 ∈ s ∨ 2 ∈ s

instance (s : Finset (Fin 3)) : Decidable (facilitatedMiddle s) :=
  inferInstanceAs (Decidable (0 ∈ s ∨ 2 ∈ s))

theorem orderWitness : fewer ⊆ more ∧ 1 ∈ fewer ∧ 1 ∈ more ∧
    ¬ facilitatedMiddle fewer ∧ facilitatedMiddle more := by
  decide +kernel

theorem healingPreservesAnInfection {α : Type*} [DecidableEq α]
    (s : Finset α) (x y : α) (hxy : x ≠ y) (hy : y ∈ s) :
    (s.erase x).Nonempty := by
  exact ⟨y, Finset.mem_erase.mpr ⟨Ne.symm hxy, hy⟩⟩
