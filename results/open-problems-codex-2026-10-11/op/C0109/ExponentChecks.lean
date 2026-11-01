import Mathlib.Tactic.Linarith
import Mathlib.Data.Real.Basic

-- Algebraic auxiliaries for DIRECT_UPPER.md; not the stochastic theorem.
theorem replacement_balance (e g : ℝ) (h : 2*(3+e)*g=e) :
    e/2-(2+e)*g=g := by nlinarith [h]

theorem gamma_bound (e g : ℝ) (he0 : 0 ≤ e) (he1 : e ≤ 1)
    (hg0 : 0 ≤ g) (h : 2*(3+e)*g=e) : g ≤ 1/8 := by
  have hprod0 : 0 ≤ e*g := mul_nonneg he0 hg0
  have hgsmall : g ≤ 1/6 := by nlinarith [h]
  have hprod : 0 ≤ (1-e)*(1-2*g) :=
    mul_nonneg (by linarith) (by linarith)
  nlinarith [h, hprod]

theorem smoothing_balance (g b : ℝ) (hb : 2*b=g) : g-b=b := by
  linarith

theorem gaussian_term_faster (g b : ℝ) (hg : g ≤ 1/8)
    (hb : 2*b=g) : b < 1/4-b := by linarith

theorem scalar_regularization (x ell : ℝ) (hx : 0 ≤ x)
    (he : ell ≤ x) : ell ≤ (1+ell)*x/(1+x) := by
  apply (le_div_iff₀ (show 0 < 1+x by linarith)).2
  nlinarith
