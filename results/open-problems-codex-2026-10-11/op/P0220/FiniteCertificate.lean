import Mathlib.Data.List.Permutation
import Mathlib.Tactic.NormNum

namespace P0220

def insertTop (a : Nat) : List Nat → List Nat
  | [] => [a]
  | b :: bs => if a < b then a :: bs else b :: insertTop a bs

def pileTops (p : List Nat) : List Nat :=
  p.foldl (fun ts a => insertTop a ts) []

def countPrefix (deck B : List Nat) : Nat :=
  (deck.permutations'.filter (fun p => (pileTops p).take B.length == B)).length

set_option maxRecDepth 100000
set_option maxHeartbeats 2000000

theorem exact_prefix_counts :
    countPrefix [1,2] [1,2] = 1 ∧
    countPrefix [1,2,3] [1,3] = 2 ∧
    countPrefix [1,2,3] [1,2,3] = 1 ∧
    countPrefix [1,2,3,4] [1,3,4] = 3 ∧
    countPrefix [1,2,3,4] [1,2,4] = 3 ∧
    countPrefix [1,2,3,4,5] [1,3,5] = 11 := by
  unfold countPrefix pileTops
  decide +kernel

theorem mixed_density_determinant :
    (1/6 : Rat) * (11/120) - (1/8) * (1/8) = -1/2880 := by
  norm_num

theorem mixed_density_determinant_ne_zero :
    (1/6 : Rat) * (11/120) - (1/8) * (1/8) ≠ 0 := by
  norm_num

theorem conditional_density_derivative_certificate :
    (((1/8 : Rat) * (1/2) - (1/6) * (1/3)) / ((1/2)*(1/2))) = 1/36 := by
  norm_num

end P0220
