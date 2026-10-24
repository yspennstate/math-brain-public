import Mathlib.Data.Real.Basic
import Mathlib.Tactic.Ring
import Mathlib.Tactic.Positivity
import Mathlib.Tactic.NormNum
import Mathlib.Tactic.Linarith

-- The two-coordinate prefix identity in dimension four, including zeros.
theorem prefix_two_identity (a b c d e f x y z w : ℝ) :
    x * (1 + a*y + b*z + c*w) + y * (1 - a*x + d*z + e*w)
      - (x+y) = b*x*z + c*x*w + d*y*z + e*y*w := by
  ring

theorem prefix_two_nonnegative (b c d e x y z w : ℝ)
    (hb : 0 ≤ b) (hc : 0 ≤ c) (hd : 0 ≤ d) (he : 0 ≤ e)
    (hx : 0 ≤ x) (hy : 0 ≤ y) (hz : 0 ≤ z) (hw : 0 ≤ w) :
    0 ≤ b*x*z + c*x*w + d*y*z + e*y*w := by
  positivity

theorem balanced_product_identity (α x y z w : ℝ) :
    (x*(1+α*(y-w)))*(z*(1-α*(y-w))) =
      x*z*(1-α^2*(y-w)^2) := by
  ring

theorem balanced_difference_identity (α x y z w : ℝ) :
    x*(1+α*(y-w))-z*(1-α*(y-w)) =
      (x-z)+α*(x+z)*(y-w) := by
  ring

-- Pair cancellation is the only algebra used in the general prefix proof.
theorem skew_pair_cancels (a x y : ℝ) : a*x*y + (-a)*y*x = 0 := by
  ring

theorem cycle_pfaffian_identity (a b c d : ℝ) :
    a^2*c^2 - 2*a*b*c*d + b^2*d^2 = (a*c-b*d)^2 := by
  ring

-- Exact expansion behind the new sparse cyclic convergence theorem.
theorem alternating_product_identity (a b c d u v : ℝ) :
    (1+a*u-d*v)*(1-b*u+c*v)-1 =
      (a-b-a*b)*u+(c-d-c*d)*v + a*b*u*(1-u) + c*d*v*(1-v)
      + (a*c+b*d)*u*v := by
  ring

theorem alternating_remainder_nonnegative (a b c d u v : ℝ)
    (ha : 0 ≤ a) (hb : 0 ≤ b) (hc : 0 ≤ c) (hd : 0 ≤ d)
    (hu : 0 ≤ u) (hv : 0 ≤ v) (hu1 : u ≤ 1) (hv1 : v ≤ 1) :
    0 ≤ a*b*u*(1-u) + c*d*v*(1-v) + (a*c+b*d)*u*v := by
  have h1u : 0 ≤ 1-u := sub_nonneg.mpr hu1
  have h1v : 0 ≤ 1-v := sub_nonneg.mpr hv1
  positivity

-- Exact numerical certificate for the rational example's strict gap.
example : (0:ℝ) < (9/10:ℝ)-(1/10:ℝ)-(9/10:ℝ)*(1/10:ℝ) := by
  norm_num

theorem alternating_increment_bound (a b c d u v κ : ℝ)
    (ha : 0 ≤ a) (hb : 0 ≤ b) (hc : 0 ≤ c) (hd : 0 ≤ d)
    (hu : 0 ≤ u) (hv : 0 ≤ v) (hu1 : u ≤ 1) (hv1 : v ≤ 1)
    (hk1 : κ ≤ a-b-a*b) (hk2 : κ ≤ c-d-c*d) :
    κ*(u+v) ≤ (1+a*u-d*v)*(1-b*u+c*v)-1 := by
  apply sub_nonneg.mp
  have h1u : 0 ≤ 1-u := sub_nonneg.mpr hu1
  have h1v : 0 ≤ 1-v := sub_nonneg.mpr hv1
  have hgap1 : 0 ≤ a-b-a*b-κ := sub_nonneg.mpr hk1
  have hgap2 : 0 ≤ c-d-c*d-κ := sub_nonneg.mpr hk2
  rw [show (1+a*u-d*v)*(1-b*u+c*v)-1-κ*(u+v) =
    (a-b-a*b-κ)*u+(c-d-c*d-κ)*v + a*b*u*(1-u) + c*d*v*(1-v)
      + (a*c+b*d)*u*v by ring]
  positivity

#print axioms alternating_increment_bound
#print axioms balanced_product_identity

theorem cyclic_rate_identity (g h q1 q2 q3 q4 : ℝ) :
    q1*(g*q2-h*q4)+q2*(g*q3-h*q1)+q3*(g*q4-h*q2)+q4*(g*q1-h*q3) =
      (g-h)*(q1*q2+q2*q3+q3*q4+q4*q1) := by
  ring

theorem rate_complementarity_forces_independent_support (g h q1 q2 q3 q4 : ℝ)
    (hg : g < h) (hq1 : 0 ≤ q1) (hq2 : 0 ≤ q2) (hq3 : 0 ≤ q3) (hq4 : 0 ≤ q4)
    (hr1 : q1*(g*q2-h*q4) = 0) (hr2 : q2*(g*q3-h*q1) = 0)
    (hr3 : q3*(g*q4-h*q2) = 0) (hr4 : q4*(g*q1-h*q3) = 0) :
    q1*q2 = 0 ∧ q2*q3 = 0 ∧ q3*q4 = 0 ∧ q4*q1 = 0 := by
  have heq : (g-h)*(q1*q2+q2*q3+q3*q4+q4*q1) = 0 := by
    rw [← cyclic_rate_identity, hr1, hr2, hr3, hr4]
    ring
  have hne : g-h ≠ 0 := ne_of_lt (sub_neg.mpr hg)
  have hsum : q1*q2+q2*q3+q3*q4+q4*q1 = 0 :=
    (mul_eq_zero.mp heq).resolve_left hne
  have hp12 : 0 ≤ q1*q2 := mul_nonneg hq1 hq2
  have hp23 : 0 ≤ q2*q3 := mul_nonneg hq2 hq3
  have hp34 : 0 ≤ q3*q4 := mul_nonneg hq3 hq4
  have hp41 : 0 ≤ q4*q1 := mul_nonneg hq4 hq1
  constructor
  · linarith
  constructor
  · linarith
  constructor <;> linarith

#print axioms rate_complementarity_forces_independent_support

theorem weighted_product_payoff_cancellation (a b c d u v : ℝ) :
    b*(a*u-d*v)+a*(-b*u+c*v) = (a*c-b*d)*v := by
  ring

theorem other_weighted_product_payoff_cancellation (a b c d x z : ℝ) :
    d*(-a*x+b*z)+a*(d*x-c*z) = (b*d-a*c)*z := by
  ring

theorem weighted_cyclic_rate_identity
    (ga ha gb hb gc hc gd hd z1 z2 z3 z4 : ℝ) :
    z1*(ga*z2-hd*z4)+z2*(gb*z3-ha*z1)+z3*(gc*z4-hb*z2)+z4*(gd*z1-hc*z3) =
      (ga-ha)*z1*z2+(gb-hb)*z2*z3+(gc-hc)*z3*z4+(gd-hd)*z4*z1 := by
  ring

#print axioms weighted_cyclic_rate_identity
