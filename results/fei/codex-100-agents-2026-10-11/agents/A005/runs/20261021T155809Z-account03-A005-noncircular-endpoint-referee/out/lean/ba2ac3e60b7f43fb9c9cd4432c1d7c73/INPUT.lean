import Mathlib.Tactic.Ring
import Mathlib.Tactic.Linarith
import Mathlib.Analysis.SpecialFunctions.Log.Basic

theorem whole_sign_sum (H q b : Real) :
    (H + q + b) + (H + q - b) = 2 * H + 2 * q := by ring

theorem refund_error_upper (u I : Real) (hu : 0 < u) (hu1 : u <= 1)
    (hI : 1 - u <= I) :
    1 - u + u * Real.log u <= I ^ 2 := by
  have hlog : Real.log u <= u - 1 := Real.log_le_sub_one_of_pos hu
  have hm : u * Real.log u <= u * (u - 1) := mul_le_mul_of_nonneg_left hlog (le_of_lt hu)
  have hpos : 0 <= 1 - u := by linarith
  have hIp : 0 <= I := le_trans hpos hI
  nlinarith [sq_nonneg (I - (1-u))]
