import Mathlib.Tactic.Ring
import Mathlib.Tactic.Linarith
import Mathlib.Data.Real.Basic

-- Algebraic part of the mean-field saddle calculation only.
theorem colicin_determinant (a b g x y : ℝ) :
    (-a*x)*(-b*y)-(-a*x)*(-(b+g)*y) = -a*g*x*y := by
  ring

-- Strict pair balance forces the explicit contact-process lower bound.
theorem pair_balance_bound (a D rho q : ℝ)
    (ha : 0 ≤ a) (hr : 0 < rho) (hD : 1 < D)
    (hbalance : rho = a * (rho-q))
    (hstrict : rho < D*q)
    (hupper : a*(D-1) ≤ D) : False := by
  have hdiff : 0 < rho-q := by
    by_contra hn
    have hle : rho-q ≤ 0 := le_of_not_gt hn
    have hm : a*(rho-q) ≤ 0 := mul_nonpos_of_nonneg_of_nonpos ha hle
    linarith
  have hscaled : (D-1)*rho = (D-1)*(a*(rho-q)) :=
    congrArg (fun z : ℝ => (D-1)*z) hbalance
  have hm : 0 ≤ (D-a*(D-1))*(rho-q) :=
    mul_nonneg (sub_nonneg.mpr hupper) (le_of_lt hdiff)
  have hz : (D-1)*rho-(D-1)*(a*(rho-q)) = 0 := sub_eq_zero.mpr hscaled
  have hi : (D-a*(D-1))*(rho-q) =
      (rho-D*q)+((D-1)*rho-(D-1)*(a*(rho-q))) := by ring
  rw [hi, hz, add_zero] at hm
  linarith
