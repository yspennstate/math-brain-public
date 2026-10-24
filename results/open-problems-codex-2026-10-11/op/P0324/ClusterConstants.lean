import Mathlib.Data.Real.Basic
import Mathlib.Tactic.Linarith
import Mathlib.Tactic.NormNum

-- Rational cutoff used after the tree majorant and geometric summation.
theorem cluster_cutoff (b : ℝ) (hb : 0 <= b) (hmax : b <= 1/128) :
    0 < 1-10*b := by
  linarith

theorem cluster_root_bound (b : ℝ) (hb : 0 <= b) (hmax : b <= 1/128) :
    100*b/(1-10*b) <= 50/59 := by
  have hd : 0 < 1-10*b := cluster_cutoff b hb hmax
  apply (div_le_iff₀ hd).2
  nlinarith

theorem cluster_root_strict : (50 : ℝ)/59 < 1 := by
  norm_num
