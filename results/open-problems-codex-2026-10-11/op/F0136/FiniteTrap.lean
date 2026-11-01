import Mathlib.Data.Real.Basic
import Mathlib.Tactic.Linarith
import Mathlib.Tactic.Ring

-- Algebraic steps only. The geometric counting and beta integrals
-- are proved in ATTEMPT.md, not formalized in this file.

theorem kappa_two_dimensional (s t : ℝ) :
    2 * (s + t) - max s t = s + t + min s t := by
  rcases le_total s t with h | h
  · rw [max_eq_right h, min_eq_left h]
    ring
  · rw [max_eq_left h, min_eq_right h]
    ring

theorem boundary_lower (s t R C : ℝ)
    (hs : 0 ≤ s) (ht : 0 ≤ t) (hR : 1 ≤ R) (hC : 1 ≤ C)
    (hSum : 3 ≤ R + C) :
    s + t + min s t ≤ s * R + t * C := by
  rcases le_total s t with h | h
  · rw [min_eq_left h]
    nlinarith [mul_nonneg (sub_nonneg.mpr h) (sub_nonneg.mpr hC),
      mul_nonneg hs (show 0 ≤ R + C - 3 by linarith)]
  · rw [min_eq_right h]
    nlinarith [mul_nonneg (sub_nonneg.mpr h) (sub_nonneg.mpr hR),
      mul_nonneg ht (show 0 ≤ R + C - 3 by linarith)]

theorem boundary_gap (s t R C : ℝ)
    (hs : 0 ≤ s) (ht : 0 ≤ t) (hR : 1 ≤ R) (hC : 1 ≤ C)
    (hSum : 4 ≤ R + C) :
    s + t + 2 * min s t ≤ s * R + t * C := by
  rcases le_total s t with h | h
  · rw [min_eq_left h]
    nlinarith [mul_nonneg (sub_nonneg.mpr h) (sub_nonneg.mpr hC),
      mul_nonneg hs (show 0 ≤ R + C - 4 by linarith)]
  · rw [min_eq_right h]
    nlinarith [mul_nonneg (sub_nonneg.mpr h) (sub_nonneg.mpr hR),
      mul_nonneg ht (show 0 ≤ R + C - 4 by linarith)]

theorem pair_escape_comparison (u v : ℝ)
    (hu : 0 ≤ u) (hu1 : u ≤ 1) (hv : 0 ≤ v) (hv1 : v ≤ 1) :
    (u + v) / 2 ≤ u + v - u * v ∧ u + v - u * v ≤ u + v := by
  constructor
  · nlinarith [mul_nonneg hu (sub_nonneg.mpr hv1),
      mul_nonneg hv (sub_nonneg.mpr hu1)]
  · nlinarith [mul_nonneg hu hv]

theorem weighted_isoperimetry (s t R C n : ℝ)
    (hs : 0 ≤ s) (ht : 0 ≤ t) (hn : n ≤ R * C) :
    4 * s * t * n ≤ (s * R + t * C) ^ 2 := by
  have hst : 0 ≤ s * t := mul_nonneg hs ht
  have h := mul_nonneg hst (sub_nonneg.mpr hn)
  nlinarith [sq_nonneg (s * R - t * C)]
