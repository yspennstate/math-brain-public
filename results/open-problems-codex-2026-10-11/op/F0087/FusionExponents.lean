import Mathlib.Data.Real.Basic
import Mathlib.Tactic.Linarith

-- q=s^2 and n is the number of insertions of each sign.
theorem fused_diagonal_volume_exponent_positive (q n : Real)
    (hq : q < 1/4) (hn : 2 ≤ n) :
    0 < 4*(n-1) - 2*n*q := by
  have hn0 : 0 < n := by linarith
  have hmul : n*q < n*(1/4) := mul_lt_mul_of_pos_left hq hn0
  nlinarith

-- Charge reduction produces t; this is the irrational-case divergent exponent.
theorem fused_alias_exponent_positive (q n t : Real)
    (hnq : 1/4 < n*q) (ht : t^2 < 1/4) :
    0 < 2*n*q - 2*t^2 := by
  linarith

-- An allowed higher-integrability exponent for the corrected nearest-neighbor bound.
theorem holder_exponent_allowed (q : Real) (hq1 : q < 1) :
    0 < (1-q)/2 ∧ q + (1-q)/2 < 1 := by
  constructor <;> linarith

-- Nonnegativity of a two-edge probability supplies the entire local lower bound.
theorem local_fusion_mean_lower_bound (c : Real) (hc : c^2 ≤ 1/16) :
    1/4 ≤ 7/16 + c/2 - c^2 := by
  have hcl : -(1/4 : Real) ≤ c := by
    nlinarith [sq_nonneg (c + 1/4)]
  nlinarith

#print axioms local_fusion_mean_lower_bound
#print axioms fused_diagonal_volume_exponent_positive
#print axioms fused_alias_exponent_positive
#print axioms holder_exponent_allowed
