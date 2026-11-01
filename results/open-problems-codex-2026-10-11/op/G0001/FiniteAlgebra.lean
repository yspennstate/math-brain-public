import Mathlib.Algebra.Order.Field.Basic
import Mathlib.Tactic.Linarith
import Mathlib.Tactic.Ring

variable {F : Type*} [Field F] [LinearOrder F] [IsStrictOrderedRing F]

-- Algebra used by the bounded-variable argument in ATTEMPT.md.
-- t is theta; a is the probability of the upper-half-density event.
theorem density_event_lower_bound (t a : F)
    (ht : 0 < t) (ht1 : t ≤ 1)
    (h : t ≤ t / 2 + (1 - t / 2) * a) :
    t / 2 ≤ a := by
  by_contra hn
  have ha : a < t / 2 := lt_of_not_ge hn
  have hp : 0 < 1 - t / 2 := by linarith
  have hmul : (1 - t / 2) * a < (1 - t / 2) * (t / 2) :=
    mul_lt_mul_of_pos_left ha hp
  nlinarith [sq_nonneg t]

-- Conditional versions use exactly the same inequality.
theorem joint_density_lower_bound (t a b : F)
    (ht : 0 < t) (ht1 : t ≤ 1)
    (h : t ≤ t / 2 + (1 - t / 2) * a)
    (hb : t * a ≤ b) : t ^ 2 / 2 ≤ b := by
  have ha := density_event_lower_bound t a ht ht1 h
  nlinarith

-- Harris induction: covariance of the two conditional means is nonnegative.
theorem two_slice_covariance (p f0 f1 g0 g1 : F)
    (hp : 0 ≤ p) (hp1 : p ≤ 1)
    (hf : f0 ≤ f1) (hg : g0 ≤ g1) :
    ((1-p)*f0*g0 + p*f1*g1) -
      (((1-p)*f0+p*f1)*((1-p)*g0+p*g1)) ≥ 0 := by
  have h : 0 ≤ p * (1-p) * (f1-f0) * (g1-g0) :=
    mul_nonneg (mul_nonneg (mul_nonneg hp (by linarith)) (by linarith))
      (by linarith)
  have hid : ((1-p)*f0*g0 + p*f1*g1) -
      (((1-p)*f0+p*f1)*((1-p)*g0+p*g1)) =
      p * (1-p) * (f1-f0) * (g1-g0) := by ring
  rw [hid]
  exact h

-- Exact explicit d=3 parameter threshold: Delta=3^3-1=26.
theorem d3_peierls_threshold (p : F) (hp : (675:F)/676 < p) :
    26^2 * (1-p) < 1 := by nlinarith

#print axioms density_event_lower_bound
#print axioms joint_density_lower_bound
#print axioms two_slice_covariance
#print axioms d3_peierls_threshold
