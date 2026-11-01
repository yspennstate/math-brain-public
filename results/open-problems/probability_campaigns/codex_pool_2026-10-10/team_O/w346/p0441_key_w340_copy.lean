import Mathlib

theorem w340_delayedoff_wait_identity (l m t p : ℝ)
    (hl : l ≠ 0) (hm : m ≠ 0) (hv : m - l ≠ 0)
    (hp : 1 + l * t * p ≠ 0) :
    ((m / (m - l)^2 *
       (1 + m * t * p + l * (m - l) * t^2 * p / 2)) /
       (m / (l * (m - l)) * (1 + l * t * p))) / l - 1 / m =
      l / (m * (m - l)) + t * (1 + l * t / 2) * p / (1 + l * t * p) := by
  field_simp [hl, hm, hv, hp]
  <;> ring
