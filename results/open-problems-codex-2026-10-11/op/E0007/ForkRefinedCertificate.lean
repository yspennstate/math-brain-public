import Mathlib.Data.Real.Basic
import Mathlib.Tactic.Ring
import Mathlib.Tactic.Linarith
import Mathlib.Tactic.NormNum

-- Exact symbolic drift, retaining the shared center-birth contribution T.
theorem refined_fork_drift_identity (b r q H U T : ℝ) :
    (b^3+7*b^2+36*b+48)*((b-1)*r-b*q)
      - (2*b*(b^2+6*b+12))*(b*r/2-(2+b/2)*q+b*U/8)
      - (b^2/2)*(6*b*q-(3+b/2)*H+T)
      - (b^2*(b+6)/4)*(H-2*U-T)
    = -(48-12*b-17*b^2)*r + (b^2*(b+4)/4)*(T-b*U) := by
  ring

theorem refined_fork_h_relation (b : ℝ) :
    (b^2/2)*(3+b/2) = b^2*(b+6)/4 := by
  ring

theorem refined_fork_lower_numerator (b : ℝ) :
    (b^3+7*b^2+36*b+48) - 2*b*(b^2+6*b+12) - 6*b^2
      = -b^3-11*b^2+12*b+48 := by
  ring

theorem refined_fork_lower_comparison (b : ℝ) :
    2*b*(b^2+6*b+12) + 6*b^2 - 3*b^2*(b+6)
      = b*(24-b^2) := by
  ring

private def b0 : ℝ := 109/80
private def P0 : ℝ := b0^3+7*b0^2+36*b0+48
private def A0 : ℝ := 2*b0*(b0^2+6*b0+12)
private def H0 : ℝ := b0^2/2
private def U0 : ℝ := b0^2*(b0+6)/4
private def Q0 : ℝ := 48-12*b0-17*b0^2
private def M0 : ℝ := P0-A0-12*H0

-- Complete rational certificate at 109/80, above the first fork threshold.
theorem refined_fork_generator_certificate (r q H U T dr dq dH dU : ℝ)
    (hr : dr = (b0-1)*r-b0*q)
    (hq : dq = b0*r/2-(2+b0/2)*q+b0*U/8)
    (hH : 6*b0*q-(3+b0/2)*H+T ≤ dH)
    (hU : H-2*U-T ≤ dU)
    (hT : T ≤ b0*U) :
    P0*dr-A0*dq-H0*dH-U0*dU ≤ -Q0*r := by
  norm_num [b0, P0, A0, H0, U0, Q0] at *
  linarith

theorem refined_fork_function_lower_bound (r q H U : ℝ)
    (hq : q ≤ r) (hH : H ≤ 12*q) (hU : U ≤ 12*(r-q)) :
    M0*r ≤ P0*r-A0*q-H0*H-U0*U := by
  norm_num [b0, P0, A0, H0, U0, M0] at *
  linarith

theorem refined_fork_function_upper_bound (r q H U : ℝ)
    (hq : 0 ≤ q) (hH : 0 ≤ H) (hU : 0 ≤ U) :
    P0*r-A0*q-H0*H-U0*U ≤ P0*r := by
  norm_num [b0, P0, A0, H0, U0] at *
  linarith

theorem refined_fork_positive_constants : 0 < Q0 ∧ 0 < M0 ∧ 0 < P0 := by
  norm_num [b0, P0, A0, H0, U0, Q0, M0]

theorem refined_fork_strict_improvement : (34/25 : ℝ) < 109/80 := by
  norm_num

-- Rational parts of the stationary endpoint extension.
theorem finite_energy_coefficient_margin : (1/50 : ℝ) < 4000/193833 := by
  norm_num

theorem finite_energy_extension_margin : (0 : ℝ) < 2/75-1/500 := by
  norm_num

theorem refined_root_upper_check : (48 : ℝ)-12*(137/100)-17*(137/100)^2 < 0 := by
  norm_num
