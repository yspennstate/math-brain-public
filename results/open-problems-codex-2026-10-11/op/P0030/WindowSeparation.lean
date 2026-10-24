import Mathlib.Data.Real.Basic
import Mathlib.Tactic.Linarith

-- The Brownian windows supporting H_k in ATTEMPT.md, Theorem A,
-- have length 2*M+1. A separation by at least q leaves disjoint windows.
theorem brownian_windows_disjoint (M q k l : ℝ)
    (hq : 2 * M + 1 < q) (hkl : k + q ≤ l) :
    k + 2 * M + 1 < l := by
  linarith

-- The finite cancellation bound used when translating bounded averages:
-- dividing by R preserves the deterministic endpoint-error bound.
theorem normalized_translation_error (err K c R : ℝ)
    (hR : 0 < R) (herror : err ≤ 2 * K * c) :
    err / R ≤ (2 * K * c) / R := by
  exact (div_le_div_iff_of_pos_right hR).2 herror
