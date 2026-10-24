import Mathlib.Algebra.Order.BigOperators.Group.Finset
import Mathlib.Data.Real.Sqrt
import Mathlib.Tactic.Nlinarith
import Mathlib.Tactic.Ring
import Mathlib.Tactic.NormNum


-- Algebraic certificate for B=c*v*v^T, v=(sqrt(3)/2,1/2),
-- and the rational peak P=[[2,1],[1,1]]. Geometry is proved in ATTEMPT.md.
theorem irrational_face_certificate (t c : ℝ)
    (ht : 0 ≤ t) (htsq : t * t = 3) (hc : c * (5 - 2*t) = 4) :
    2 < c ∧ c < 3 ∧
    (2 - 3*c/4)*(1-c/4) - (1-c*t/4)^2 = 0 ∧
    (3*c/4)*(c/4) - (c*t/4)^2 = 0 ∧
    0 < 2-3*c/4 ∧ 0 < 3-c := by
  have htlo : 3/2 < t := by
    by_contra h
    have hn : t ≤ 3/2 := le_of_not_gt h
    have hp := mul_nonneg (sub_nonneg.mpr hn) (show 0 ≤ 3/2+t by linarith)
    nlinarith [hp]
  have hthi : t < 7/4 := by
    by_contra h
    have hn : 7/4 ≤ t := le_of_not_gt h
    have hp := mul_nonneg (sub_nonneg.mpr hn) (show 0 ≤ t+7/4 by linarith)
    nlinarith [hp]
  have hd : 0 < 5-2*t := by nlinarith
  have hcp : 0 < c := by
    by_contra h
    have hn : c ≤ 0 := le_of_not_gt h
    have hp := mul_nonpos_of_nonpos_of_nonneg hn (le_of_lt hd)
    nlinarith [hp]
  have hclo : 2 < c := by
    by_contra h
    have hn : c ≤ 2 := le_of_not_gt h
    have hp := mul_le_mul_of_nonneg_right hn (le_of_lt hd)
    nlinarith [hp]
  have hcup : c < 8/3 := by
    by_contra h
    have hn : 8/3 ≤ c := le_of_not_gt h
    have hp := mul_le_mul_of_nonneg_right hn (le_of_lt hd)
    nlinarith [hp]
  have hc3 : c < 3 := by linarith
  have hs : (c*t)*(c*t) = 3*c*c := by
    calc
      (c*t)*(c*t) = (c*c)*(t*t) := by ring
      _ = 3*c*c := by rw [htsq]; ring
  refine ⟨hclo,hc3,?_,?_,?_,by linarith⟩
  · nlinarith [hc,hs]
  · nlinarith [hs]
  · linarith

theorem sqrt_three_certificate :
    let t := Real.sqrt 3
    let c := (20+8*t)/13
    2 < c ∧ c < 3 ∧
    (2 - 3*c/4)*(1-c/4) - (1-c*t/4)^2 = 0 ∧
    (3*c/4)*(c/4) - (c*t/4)^2 = 0 ∧
    0 < 2-3*c/4 ∧ 0 < 3-c := by
  dsimp
  apply irrational_face_certificate
  · exact Real.sqrt_nonneg 3
  · nlinarith [Real.sq_sqrt (show (0:ℝ) ≤ 3 by norm_num)]
  · nlinarith [Real.sq_sqrt (show (0:ℝ) ≤ 3 by norm_num)]



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
