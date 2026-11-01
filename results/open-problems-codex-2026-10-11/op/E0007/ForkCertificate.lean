import Mathlib.Data.Real.Basic
import Mathlib.Tactic.Ring
import Mathlib.Tactic.Linarith
import Mathlib.Tactic.NormNum

-- Denominator-cleared symbolic identities for all birth rates.
theorem fork_q_cancellation (b : ℝ) :
    -b * (b^3 + 9*b^2 + 44*b + 48)
      + (2*b*(b+2)*(b+6)) * (2+b/2) - 6*b*(b^2/2) = 0 := by
  ring

theorem fork_h_cancellation (b : ℝ) :
    (b^2/2)*(3+b/2) - b^2*(b+6)/4 = 0 := by
  ring

theorem fork_u_cancellation (b : ℝ) :
    -(2*b*(b+2)*(b+6))*b/8 + (b^2*(b+6)/4)*(b+2) = 0 := by
  ring

theorem fork_r_coefficient (b : ℝ) :
    (b-1)*(b^3+9*b^2+44*b+48) - (2*b*(b+2)*(b+6))*b/2
      = -(48-4*b-23*b^2) := by
  ring

theorem fork_positive_lower_numerators (b : ℝ) :
    (b^3+9*b^2+44*b+48) - 2*b*(b+2)*(b+6) - 6*b^2
      = -b^3-13*b^2+20*b+48 := by
  ring

-- Complete rational linear certificate at total birth/death ratio 34/25.
theorem fork_generator_certificate (r q H U dr dq dH dU : ℝ)
    (hr : dr = (9/25 : ℝ)*r - (34/25 : ℝ)*q)
    (hq : dq = (17/25 : ℝ)*r - (67/25 : ℝ)*q + (17/100 : ℝ)*U)
    (hH : (204/25 : ℝ)*q - (92/25 : ℝ)*H ≤ dH)
    (hU : H - (84/25 : ℝ)*U ≤ dU) :
    992202*dr - 525504*dq - 7225*dH - 26588*dU ≤ -150*r := by
  linarith

theorem fork_function_lower_bound (r q H U : ℝ)
    (hq : q ≤ r) (hH : H ≤ 12*q) (hU : U ≤ 12*(r-q)) :
    379998*r ≤ 992202*r - 525504*q - 7225*H - 26588*U := by
  linarith

theorem fork_function_upper_bound (r q H U : ℝ)
    (hq : 0 ≤ q) (hH : 0 ≤ H) (hU : 0 ≤ U) :
    992202*r - 525504*q - 7225*H - 26588*U ≤ 992202*r := by
  linarith

theorem fork_all_occupied_initial :
    (992202 : ℝ) - 525504 - 7225*12 = 379998 := by
  norm_num

theorem fork_threshold_strict_improvement : (4/3 : ℝ) < 34/25 := by
  norm_num

theorem fork_margin_positive : (48 : ℝ)-4*(34/25)-23*(34/25)^2 > 0 := by
  norm_num
