import Mathlib.Algebra.Order.BigOperators.Group.Finset
import Mathlib.Tactic.Nlinarith
import Mathlib.Tactic.NormNum


open scoped BigOperators

-- Formal scope: the scalar sign and finite summation steps used by
-- the corner obstruction. The PDE and convergence proof is in ATTEMPT.md.

theorem weighted_last_firing_sum
    {V E : Type*} [Fintype V] [Fintype E]
    (height weight outgoing : V → ℝ) (edge_min : E → ℝ)
    (hweight : ∀ v, 0 ≤ weight v)
    (hheight : ∀ v, outgoing v ≤ height v)
    (horientation : (∑ e, edge_min e) ≤ ∑ v, outgoing v * weight v) :
    (∑ e, edge_min e) ≤ ∑ v, height v * weight v := by
  apply le_trans horientation
  apply Finset.sum_le_sum
  intro v hv
  exact mul_le_mul_of_nonneg_right (hheight v) (hweight v)

theorem corner_projection_positive
    (k s P N : ℝ) (hk : 0 < k) (hs : 1 < k*s)
    (hP : k-1 ≤ P) (hN : -k*(1-s) ≤ N) :
    0 < P+N := by
  nlinarith

theorem dodecagon_projection_positive (P N : ℝ)
    (hP : 2 ≤ P) (hN : -(3/2) ≤ N) :
    (1/2) ≤ P+N := by
  linarith

-- The corner inequality with sin(5*pi/6)=1/2 contradicts a=2, b=3.
theorem dodecagon_corner_contradiction :
    ¬ ((2:ℝ) ≤ 3*(1-(1/2))) := by
  norm_num
