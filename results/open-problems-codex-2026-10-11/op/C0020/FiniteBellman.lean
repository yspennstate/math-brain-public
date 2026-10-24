import Mathlib.Data.Nat.Basic
import Mathlib.Algebra.Order.Ring.Int

namespace C0020
abbrev State := List (Option Bool)
def value (s : State) (default : Bool) (i : Nat) : Bool :=
  ((s[i]?).getD none).getD default
-- Cross-boundary edges of the triangular rhombus: 0-1, 2-3, 2-1.
def crossing (s : State) (default : Bool) : Bool :=
  (value s default 0 && value s default 1) ||
  (value s default 2 && value s default 3) ||
  (value s default 2 && value s default 1)
def done (s : State) : Bool := crossing s false == crossing s true
def unknown (s : State) : Nat := (s.filter (fun v => v.isNone)).length
-- Integer depth sum over completions; fuel 4 suffices on valid four-bit states.
def total : Nat -> State -> Nat
  | 0, _ => 0
  | k+1, s =>
    if done s then 0 else
      2 ^ unknown s +
        ([0, 1, 2, 3].map (fun i =>
          if ((s[i]?).getD none).isNone then
            total k (s.set i (some false)) + total k (s.set i (some true))
          else 1000)).foldl Nat.min 1000

theorem two_by_two_total : total 4 [none, none, none, none] = 40 := by
  decide +kernel

theorem first_query_one_total :
    16 + total 3 [none, some false, none, none] +
      total 3 [none, some true, none, none] = 40 := by
  decide +kernel

theorem certificate_check :
    done [none, some true, some true, none] = true := by
  decide +kernel

theorem integer_gap (z k : Int) : 0 <= (z-k)*(z-(k+1)) := by
  have cases : Or (z <= k) (k+1 <= z) := by omega
  cases cases with
  | inl h => exact mul_nonneg_of_nonpos_of_nonpos (by omega) (by omega)
  | inr h => exact mul_nonneg (by omega) (by omega)
end C0020
