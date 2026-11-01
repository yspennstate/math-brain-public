import Init.Data.Rat.Lemmas
namespace A083Stage22
def eps : Rat := 1/65536
def q (s : Fin 16) : Rat :=
  match s.val with
  | 8 | 11 | 13 | 14 => (2-eps)/16
  | 9 | 10 | 12 | 15 => eps/16
  | _ => 1/16
def flip (s : Fin 16) (i : Fin 3) : Fin 16 :=
  ⟨Nat.xor s.val (2^i.val) % 16, Nat.mod_lt _ (by decide)⟩
def evenParity (s : Fin 8) : Bool :=
  s.val == 0 || s.val == 3 || s.val == 5 || s.val == 6
theorem face_certificate :
    (∀ s : Fin 16, ∀ i : Fin 3, q s + q (flip s i) = 1/8) ∧
    (∀ s : Fin 8, q ⟨s.val, Nat.lt_trans s.isLt (by decide)⟩ +
      q ⟨s.val+8, Nat.add_lt_add_right s.isLt 8⟩ =
      (if evenParity s then (3-eps)/16 else (1+eps)/16)) ∧
    ((4/3 : Rat)^2 < 2) := by
  decide
end A083Stage22
