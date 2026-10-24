import Mathlib.Data.Real.Basic
import Mathlib.Tactic.FieldSimp
import Mathlib.Tactic.Ring
import Mathlib.Tactic.Linarith

theorem threshold_identity (D l p : Real) (hp : 0 < p) :
    (D * (1 - 1 / p) - l) * p = D * (p - 1) - l * p := by
  have hn : Not (p = 0) := ne_of_gt hp
  field_simp
  <;> ring

theorem threshold_equivalence (D l p : Real) (hp : 0 < p) :
    0 <= D * (p - 1) - l * p ↔ l <= D * (1 - 1 / p) := by
  have hid := threshold_identity D l p hp
  constructor
  · intro h
    by_contra hn
    have hh : D * (1 - 1 / p) - l < 0 := by linarith
    have hm := mul_neg_of_neg_of_pos hh hp
    linarith
  · intro h
    have hh : 0 <= D * (1 - 1 / p) - l := by linarith
    have hm := mul_nonneg hh (le_of_lt hp)
    linarith

theorem source_rate_threshold (p : Real) :
    2 * (1 - 1 / p) = 2 - 2 / p := by ring

theorem three_pulse_kernel (v1 v2 v3 k1 k2 k3 : Real)
    (h : k1*v1 + k2*v2 + k3*v3 = 0) :
    -(k3*v3) = k1*v1 + k2*v2 := by linarith
