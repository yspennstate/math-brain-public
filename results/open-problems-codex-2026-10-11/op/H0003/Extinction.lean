import Mathlib.Tactic.NormNum
import Mathlib.Tactic.Ring
import Mathlib.Tactic.Linarith
import Mathlib.Tactic.Positivity

def offspringPGF (s : ℚ) : ℚ := (1 / 4 + (3 / 4) * s)^2

theorem fixed_point_factorization (s : ℚ) :
    offspringPGF s - s = ((s - 1) * (9 * s - 1)) / 16 := by
  unfold offspringPGF
  ring

theorem only_fixed_points (s : ℚ) (h : offspringPGF s = s) :
    s = 1 ∨ s = 1 / 9 := by
  have hz : (s - 1) * (9 * s - 1) = 0 := by
    have hf := fixed_point_factorization s
    rw [h] at hf
    have : ((s - 1) * (9 * s - 1)) / 16 = 0 := by simpa using hf.symm
    exact (div_eq_zero_iff).mp this |>.resolve_right (by norm_num)
  rcases mul_eq_zero.mp hz with h1 | h2
  · left; exact sub_eq_zero.mp h1
  · right
    have : 9 * s = 1 := sub_eq_zero.mp h2
    calc s = (9 * s) / 9 := by ring
         _ = 1 / 9 := by rw [this]

theorem exact_fixed_point : offspringPGF (1 / 9) = 1 / 9 := by
  norm_num [offspringPGF]

theorem exact_survival_gap : (1 : ℚ) - 1 / 9 = 8 / 9 := by norm_num

theorem root_degree_three_extinction :
    ((1 : ℚ) / 4 + (3 / 4) * (1 / 9))^3 = 1 / 27 := by norm_num

theorem iterate_below_small_root (s : ℚ) (hs : 0 ≤ s) (ht : s ≤ 1 / 9) :
    offspringPGF s ≤ 1 / 9 := by
  unfold offspringPGF
  have h1 : 0 ≤ 1 / 4 + (3 / 4) * s := by positivity
  have h2 : 1 / 4 + (3 / 4) * s ≤ 1 / 3 := by
    exact (by linarith : 1 / 4 + (3 / 4) * s ≤ 1 / 3)
  nlinarith
