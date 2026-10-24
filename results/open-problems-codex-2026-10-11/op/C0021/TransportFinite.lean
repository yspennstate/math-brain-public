import Mathlib.Data.Fintype.Basic
import Mathlib.Tactic.NormNum

namespace C0021Transport
def low (i : Fin 4) : Nat :=
  match i.val with
  | 0 => 0
  | 1 => 1
  | 2 => 2
  | _ => 4
def high (i : Fin 4) : Nat :=
  match i.val with
  | 0 => 7
  | 1 => 5
  | 2 => 3
  | _ => 6
def bit (x j : Nat) : Nat := (x / 2^j) % 2
def ones (x : Nat) : Nat := bit x 0 + bit x 1 + bit x 2
def distance (x y : Nat) : Nat :=
  (if bit x 0 = bit y 0 then 0 else 1) +
  (if bit x 1 = bit y 1 then 0 else 1) +
  (if bit x 2 = bit y 2 then 0 else 1)
def boundedHigh (i : Fin 4) : Nat :=
  match i.val with
  | 0 => 3
  | 1 => 5
  | 2 => 6
  | _ => 7

theorem proper_outputs : ∀ i : Fin 4, ones (low i) < 2 ∧ 2 ≤ ones (high i) := by
  decide +kernel
theorem monotone_pairs : ∀ (i : Fin 4) (j : Fin 3), bit (low i) j.val ≤ bit (high i) j.val := by
  decide +kernel
theorem low_injective : ∀ i j : Fin 4, low i = low j → i = j := by
  decide +kernel
theorem high_injective : ∀ i j : Fin 4, high i = high j → i = j := by
  decide +kernel
theorem total_distance :
    distance (low 0) (high 0) + distance (low 1) (high 1) +
    distance (low 2) (high 2) + distance (low 3) (high 3) = 6 := by
  decide +kernel
theorem bounded_map_facts : ∀ i : Fin 4,
    2 ≤ ones (boundedHigh i) ∧ distance (low i) (boundedHigh i) ≤ 2 ∧
    (∀ j : Fin 3, bit (low i) j.val ≤ bit (boundedHigh i) j.val) := by
  decide +kernel
theorem bounded_map_injective : ∀ i j : Fin 4, boundedHigh i = boundedHigh j → i = j := by
  decide +kernel
theorem bounded_map_moments :
    distance (low 0) (boundedHigh 0) + distance (low 1) (boundedHigh 1) +
    distance (low 2) (boundedHigh 2) + distance (low 3) (boundedHigh 3) = 6 ∧
    (distance (low 0) (boundedHigh 0))^2 + (distance (low 1) (boundedHigh 1))^2 +
    (distance (low 2) (boundedHigh 2))^2 + (distance (low 3) (boundedHigh 3))^2 = 10 := by
  decide +kernel

theorem median_depth_three_gap :
    (257554309 : ℚ) / 16777216 - 15796051 / 1048576 = 4817493 / 16777216 := by
  norm_num
theorem median_depth_three_strictly_worse :
    (15796051 : ℚ) / 1048576 < 257554309 / 16777216 := by
  norm_num
theorem fixed_median_depth_two_strictly_worse : (393 : ℚ) / 64 < 199 / 32 := by
  norm_num
theorem local_median_regret :
    (3031947 : ℚ) / 262144 - 3028131 / 262144 = 477 / 32768 := by
  norm_num
theorem local_median_regret_positive : (0 : ℚ) < 477 / 32768 := by
  norm_num
theorem median_revealment_gap :
    ((257554309 : ℚ) / 16777216 - 15796051 / 1048576) / 27 = 535277 / 50331648 := by
  norm_num
#print axioms monotone_pairs
#print axioms total_distance
#print axioms bounded_map_moments
#print axioms median_depth_three_gap
#print axioms median_revealment_gap
end C0021Transport
