from pathlib import Path
lean='''import Mathlib.Data.Fintype.BigOperators
import Mathlib.Algebra.Order.BigOperators.Group.Finset

open scoped BigOperators

theorem colour_capacity {L m : Nat} (counts : Fin L -> Nat)
    (h : forall i, counts i <= m) : (sum i, counts i) <= L * m := by
  calc
    _ <= sum i : Fin L, m := Finset.sum_le_sum (fun i _ => h i)
    _ = L * m := by simp

theorem colour_pigeonhole {L m : Nat} (counts : Fin L -> Nat)
    (htotal : L * m < (sum i, counts i)) : exists i, m < counts i := by
  classical
  apply Classical.byContradiction
  intro h
  have hm : forall i, counts i <= m := by
    intro i
    exact Nat.le_of_not_gt (fun hi => h <| Exists.intro i hi)
  exact (not_le_of_gt htotal) (colour_capacity counts hm)
'''
# ASCII keywords are valid; the sum binder needs the actual Lean big-operator token.
lean=lean.replace('sum i','∑ i')
Path('ColourCapacity.lean').write_text(lean,encoding='utf8')
