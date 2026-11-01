import Init

namespace A083Stage20

def act (s : Fin 8) : Fin 8 :=
  match s.val with
  | 0 => 0
  | 1 => 2
  | 2 => 4
  | 3 => 6
  | 4 => 7
  | 5 => 5
  | 6 => 3
  | _ => 1

def xor8 (a b : Fin 8) : Fin 8 :=
  ⟨Nat.xor a.val b.val % 8, Nat.mod_lt _ (by decide)⟩

-- The actual matrix columns are 2,4,7. This certificate rules out
-- using an arbitrary permutation as an invertible physical linear map.
theorem structure_certificate :
    (∀ s : Fin 8, act (act (act (act s))) = s) ∧
    (∀ a b : Fin 8, act (xor8 a b) = xor8 (act a) (act b)) ∧
    (act 0 = 0) ∧ (act 1 = 2) ∧ (act 2 = 4) ∧
    (act 4 = 7) ∧ (act 7 = 1) := by
  decide

end A083Stage20
