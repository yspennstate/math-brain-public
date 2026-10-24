import Mathlib.Data.Real.Basic
import Mathlib.Tactic.Ring
import Mathlib.Tactic.Linarith

set_option autoImplicit false

theorem cauchy_square_identity (u v p q : ℝ) :
    (u^2+v^2)*(p^2+q^2) - (p*u+q*v)^2 = (p*v-q*u)^2 := by
  ring

theorem cauchy_square_bound (u v p q : ℝ) :
    (p*u+q*v)^2 ≤ (u^2+v^2)*(p^2+q^2) := by
  have h := sq_nonneg (p*v-q*u)
  rw [← cauchy_square_identity u v p q] at h
  linarith

theorem cycloid_speed_identity (H c s : ℝ) (hcs : c^2+s^2=1) :
    (H/2*(1-c))^2 + (H/2*s)^2 = H*(H/2*(1-c)) := by
  have hzero : (H/2*(1-c))^2 + (H/2*s)^2 - H*(H/2*(1-c)) = 0 := by
    calc
      _ = H^2/4*(c^2+s^2-1) := by ring
      _ = 0 := by rw [hcs]; ring
  linarith
