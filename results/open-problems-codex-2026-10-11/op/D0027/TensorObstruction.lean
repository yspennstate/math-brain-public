import Mathlib.Data.Real.Basic
import Mathlib.Tactic.Linarith
import Mathlib.Tactic.Ring

-- Negative triple-flip coefficients with a positive center coefficient
-- force the off-diagonal conjugated constraint entry to vanish.
theorem negative_square_forces_zero (x rate : Real)
    (hr : 0 < rate) (hn : 0 <= -(x^2) * rate) : x = 0 := by
  by_contra hx
  have hp : 0 < x^2 * rate := mul_pos (sq_pos_of_ne_zero hx) hr
  linarith only [hn, hp]

-- Exact two roots in the constant-row-sum branch.
theorem constant_branch_roots (a b : Real)
    (hprod : a*b = 0) (hcomp : (1-a)*(1-b) = 0) :
    (a = 1 /\ b = 0) \/ (a = 0 /\ b = 1) := by
  rcases mul_eq_zero.mp hprod with ha | hb
  · right
    have hh : 1-b = 0 := by simpa [ha] using hcomp
    exact ⟨ha, by linarith only [hh]⟩
  · left
    have hh : 1-a = 0 := by simpa [hb] using hcomp
    exact ⟨by linarith only [hh], hb⟩

-- Exact two roots in the healthy-indicator-row-sum branch.
theorem indicator_branch_roots (d k h : Real)
    (hdiff : h-k ≠ 0) (hfirst : (1+d)*k = 0)
    (hsecond : d*h = 0) : d = 0 \/ d = -1 := by
  by_cases hd : d = 0
  · exact Or.inl hd
  · right
    have hh : h = 0 := (mul_eq_zero.mp hsecond).resolve_left hd
    have hk : k ≠ 0 := by
      intro hk0
      apply hdiff
      rw [hh, hk0]
      ring
    have hd1 : 1+d = 0 := (mul_eq_zero.mp hfirst).resolve_right hk
    linarith only [hd1]

-- The contradiction in the global parity branch is independent of q.
theorem parity_offdiag_sum (p a : Real) :
    (-1/2 + p/(4*a)) + (-1/2 - p/(4*a)) = -1 := by
  ring

-- A small rational instance checked by kernel reduction, for the q=1/2,
-- r=1 parity candidate: the two center off-diagonal entries sum to -1.
theorem rational_parity_instance :
    ((-1/2 : Rat) + (1/2)/(4*(1/2))) +
      ((-1/2 : Rat) - (1/2)/(4*(1/2))) = -1 := by
  decide +kernel
