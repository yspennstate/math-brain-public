import Mathlib.Tactic

theorem fallback_variance_ownership (p n z : ℝ)
    (hp : 0 ≤ p) (hp' : p ≤ 1) (hn : -1 ≤ n) (hn' : n ≤ 1) :
    (1-p)*(1-z^2) ≤ 1-(p*n+(1-p)*z)^2 := by
  have hv : 0 ≤ 1-n^2 := by nlinarith
  have ht : 0 ≤ p*(1-n^2) := mul_nonneg hp hv
  have hs : 0 ≤ p*(1-p)*(n-z)^2 :=
    mul_nonneg (mul_nonneg hp (by linarith)) (sq_nonneg (n-z))
  have he : 1-(p*n+(1-p)*z)^2-(1-p)*(1-z^2) =
      p*(1-n^2)+p*(1-p)*(n-z)^2 := by ring
  linarith
