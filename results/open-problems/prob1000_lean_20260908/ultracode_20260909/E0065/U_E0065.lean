import Mathlib

/-!
# Regularity thresholds for quadratic stochastic operators (Rozikov, Problem 12)

Convention of the source (arXiv 0902.4207, eq. (4)-(5)): `V(x)_k = ∑_{i,j} P_{ij,k} x_i x_j`, sum over
all ordered pairs, `P_{ij,k} = P_{ji,k} ≥ 0`, `∑_k P_{ij,k} = 1`.  `α_m` is the smallest number such that
`P_{ij,k} > α_m` for all `i,j,k` forces every trajectory to converge.

Three algebraic facts are certified here.

* `m2_slope_bound`: on `S^1` write `f(p) = a p^2 + 2 b p (1-p) + c (1-p)^2` with
  `a, b, c ∈ [α, 1-α]`.  If a fixed point `p` has `f'(p) ≤ -1`, then `8α^2 - 12α + 1 ≥ 0`, i.e.
  `α ≤ (3-√7)/4`.  (A real quadratic has a 2-cycle inside an invariant interval iff some fixed point in
  it has multiplier `< -1`, and an interval map is regular iff it has no 2-cycle, so this is the upper
  half of `α_2 = (3-√7)/4`; the lower half is the operator `a = b = α, c = 1-α`.)

* `m3_two_cycle_identity` and `m3_two_cycle_exists`: for `m = 3` the operator with
  `P_{22,1} = P_{23,1} = P_{11,2} = P_{13,2} = P_{12,3} = P_{33,3} = 1 - 2α` and all other entries `α`
  (so `V(x)_1 = α + (1-3α)(x_2^2 + 2 x_2 x_3)`, `V(x)_2 = α + (1-3α)(x_1^2 + 2 x_1 x_3)`,
  `V(x)_3 = α + (1-3α)(2 x_1 x_2 + x_3^2)`) satisfies `V(x_1,x_2,x_3) = (x_2,x_1,x_3)` for the explicit
  point with `x_1 + x_2 = (1-6α)/(1-3α)`, `x_1 x_2 = α/(1-3α)`, `x_3 = 3α/(1-3α)`, and that point exists
  with `x_1 ≠ x_2` whenever `0 < α < 1/12`.  Hence `α_3 ≥ 1/12`.
-/

namespace QSOThreshold

/-- m = 2: a fixed point with multiplier `≤ -1` forces `8α² - 12α + 1 ≥ 0`. -/
theorem m2_slope_bound (a b c p α : ℝ) (hα : 0 < α)
    (ha1 : α ≤ a) (ha2 : a ≤ 1 - α) (hb1 : α ≤ b) (hb2 : b ≤ 1 - α)
    (hc1 : α ≤ c) (hc2 : c ≤ 1 - α) (hp0 : 0 ≤ p) (hp1 : p ≤ 1)
    (hfix : a * p ^ 2 + 2 * b * p * (1 - p) + c * (1 - p) ^ 2 = p)
    (hslope : 2 * ((a - b) * p + (b - c) * (1 - p)) ≤ -1) :
    8 * α ^ 2 - 12 * α + 1 ≥ 0 := by
  -- column-mixture form of the fixed point equation
  have h1 : (a * p + b * (1 - p)) * p + (b * p + c * (1 - p)) * (1 - p) = p := by
    linear_combination hfix
  have hq : 0 < 1 - p := by
    by_contra h
    push_neg at h
    have hp : p = 1 := by linarith
    subst hp
    nlinarith
  have hst : (a * p + b * (1 - p)) - (b * p + c * (1 - p)) ≤ -1 / 2 := by nlinarith [hslope]
  -- s ≤ (3p-1)/2
  have hs : a * p + b * (1 - p) ≤ (3 * p - 1) / 2 := by
    nlinarith [mul_le_mul_of_nonneg_left hst hq.le, h1]
  -- t ≥ 3p/2
  have ht' : (1 - p) * ((b * p + c * (1 - p)) - 3 * p / 2) ≥ 0 := by
    nlinarith [mul_le_mul_of_nonneg_left hs hp0, h1]
  have ht : b * p + c * (1 - p) ≥ 3 * p / 2 := by
    by_contra h
    push_neg at h
    nlinarith [mul_pos hq (by linarith : (0:ℝ) < 3 * p / 2 - (b * p + c * (1 - p)))]
  -- the shared coefficient b is squeezed from both sides
  have hb_up : b * (1 - p) ≤ (a * p + b * (1 - p)) - α * p := by
    nlinarith [mul_le_mul_of_nonneg_right ha1 hp0]
  have hb_lo : (b * p + c * (1 - p)) - (1 - α) * (1 - p) ≤ b * p := by
    nlinarith [mul_le_mul_of_nonneg_right hc2 hq.le]
  have hG : p * ((3 * p - 1) / 2 - α * p) - (1 - p) * (3 * p / 2 - (1 - α) * (1 - p)) ≥ 0 := by
    nlinarith [mul_le_mul_of_nonneg_left ht hq.le, mul_le_mul_of_nonneg_left hs hp0,
      mul_le_mul_of_nonneg_left hb_lo hq.le, mul_le_mul_of_nonneg_left hb_up hp0]
  -- the fixed point is confined to an interval
  have hp_lo : (2 * α + 1) / 3 ≤ p := by
    nlinarith [mul_le_mul_of_nonneg_right hb1 hq.le, hb_up, hs]
  have hp_hi : p ≤ 2 * (1 - α) / 3 := by
    nlinarith [mul_le_mul_of_nonneg_right hb2 hp0, hb_lo, ht]
  have hpq : ((2 * α + 1) / 3) * ((2 - 2 * α) / 3) ≤ p * (1 - p) := by
    nlinarith [mul_nonneg (sub_nonneg.2 hp_lo) (sub_nonneg.2 hp_hi)]
  have h1a : 0 < 1 - α := by linarith
  have hfin : (1 - α) * (8 * α ^ 2 - 12 * α + 1) ≥ 0 := by
    nlinarith [hG, mul_le_mul_of_nonneg_left hpq (by linarith : (0:ℝ) ≤ 4 - 2 * α)]
  by_contra hneg
  push_neg at hneg
  nlinarith [mul_pos h1a (by linarith : (0:ℝ) < -(8 * α ^ 2 - 12 * α + 1))]

/-- m = 3: the point with the stated sum, product and third coordinate is mapped to its swap. -/
theorem m3_two_cycle_identity (α x1 x2 x3 : ℝ) (h3 : 1 - 3 * α ≠ 0)
    (hS : (1 - 3 * α) * (x1 + x2) = 1 - 6 * α)
    (hP : (1 - 3 * α) * (x1 * x2) = α)
    (hx3 : (1 - 3 * α) * x3 = 3 * α) :
    α + (1 - 3 * α) * (x2 ^ 2 + 2 * x2 * x3) = x2 ∧
    α + (1 - 3 * α) * (x1 ^ 2 + 2 * x1 * x3) = x1 ∧
    α + (1 - 3 * α) * (2 * x1 * x2 + x3 ^ 2) = x3 ∧
    x1 + x2 + x3 = 1 := by
  refine ⟨?_, ?_, ?_, ?_⟩
  · linear_combination x2 * hS - hP + 2 * x2 * hx3
  · linear_combination x1 * hS - hP + 2 * x1 * hx3
  · linear_combination 2 * hP + (x3 - 1) * hx3
  · have h : (1 - 3 * α) * (x1 + x2 + x3 - 1) = 0 := by linear_combination hS + hx3
    rcases mul_eq_zero.1 h with h' | h'
    · exact absurd h' h3
    · linarith

/-- m = 3: for `0 < α < 1/12` two distinct positive roots with that sum and product exist. -/
theorem m3_two_cycle_exists (α : ℝ) (h0 : 0 < α) (h : α < 1 / 12) :
    ∃ x1 x2 : ℝ, x2 < x1 ∧ 0 < x2 ∧
      (1 - 3 * α) * (x1 + x2) = 1 - 6 * α ∧ (1 - 3 * α) * (x1 * x2) = α := by
  have hDpos : 0 < 48 * α ^ 2 - 16 * α + 1 := by
    nlinarith [mul_pos (by linarith : (0:ℝ) < 1 - 12 * α) (by linarith : (0:ℝ) < 1 - 4 * α)]
  set D := 48 * α ^ 2 - 16 * α + 1 with hD
  have hsq : Real.sqrt D ^ 2 = D := Real.sq_sqrt hDpos.le
  have hsqpos : 0 < Real.sqrt D := Real.sqrt_pos.2 hDpos
  have h3 : 0 < 1 - 3 * α := by linarith
  have h3' : (1 - 3 * α) ≠ 0 := ne_of_gt h3
  have h2 : (2 * (1 - 3 * α)) ≠ 0 := ne_of_gt (by linarith)
  have hlt : Real.sqrt D < 1 - 6 * α := by
    rw [Real.sqrt_lt' (by linarith)]
    nlinarith [mul_pos h0 h3]
  have key : ((1 - 6 * α) + Real.sqrt D) * ((1 - 6 * α) - Real.sqrt D) = 4 * α * (1 - 3 * α) := by
    linear_combination (-1 : ℝ) * hsq
  refine ⟨((1 - 6 * α) + Real.sqrt D) / (2 * (1 - 3 * α)),
          ((1 - 6 * α) - Real.sqrt D) / (2 * (1 - 3 * α)), ?_, ?_, ?_, ?_⟩
  · apply div_lt_div_of_pos_right _ (by linarith)
    linarith
  · apply div_pos _ (by linarith)
    linarith
  · field_simp
    ring
  · rw [div_mul_div_comm, key]
    field_simp
    ring

end QSOThreshold

#print axioms QSOThreshold.m2_slope_bound
#print axioms QSOThreshold.m3_two_cycle_identity
#print axioms QSOThreshold.m3_two_cycle_exists
