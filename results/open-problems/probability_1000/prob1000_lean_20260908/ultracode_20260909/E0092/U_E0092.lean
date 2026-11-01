import Mathlib

/-!
# Total variation is controlled by the collision probability

Diaconis, *Some things we've learned (about Markov chain Monte Carlo)* (Bernoulli 2013,
arXiv:1309.7754), Question 1: an explicit generating set achieving Wilson's mixing bound
on `Z_2^n` with `N = 2n` generators.

The memo reduces the block-level mixing bound to the quantity
`Q = m * Σ f(x)^2 - 1`, where `f` is the law of the image of a weight shell under the
generator matrix and `m = 2^d` is the size of the block's state space.  The one algebraic
step everything rests on is

  `(Σ_x |f x - 1/m|)^2 ≤ m * Σ_x (f x)^2 - 1`   whenever `Σ_x f x = 1`,

i.e. `TV(f, uniform) ≤ sqrt(Q) / 2`.  It is Cauchy–Schwarz on the finite set of states,
and it holds for every function `f` summing to one, no positivity needed.
-/

open Finset

theorem tv_sq_le_collision {X : Type*} [Fintype X] [Nonempty X]
    (f : X → ℝ) (hf : ∑ x, f x = 1) :
    (∑ x, |f x - 1 / (Fintype.card X : ℝ)|) ^ 2
      ≤ (Fintype.card X : ℝ) * ∑ x, (f x) ^ 2 - 1 := by
  have hmpos : (0 : ℝ) < (Fintype.card X : ℝ) := by exact_mod_cast Fintype.card_pos
  have hmne : (Fintype.card X : ℝ) ≠ 0 := hmpos.ne'
  have cs := sum_mul_sq_le_sq_mul_sq (univ : Finset X)
    (fun x => |f x - 1 / (Fintype.card X : ℝ)|) (fun _ => (1 : ℝ))
  simp only [mul_one, one_pow, sum_const, card_univ, nsmul_eq_mul] at cs
  have key : ∑ x, |f x - 1 / (Fintype.card X : ℝ)| ^ 2
      = ∑ x, (f x) ^ 2 - 1 / (Fintype.card X : ℝ) := by
    have h1 : ∀ x, |f x - 1 / (Fintype.card X : ℝ)| ^ 2
        = (f x) ^ 2 - (2 / (Fintype.card X : ℝ)) * f x + 1 / (Fintype.card X : ℝ) ^ 2 := by
      intro x; rw [sq_abs]; ring
    simp_rw [h1]
    rw [sum_add_distrib, sum_sub_distrib, ← mul_sum, hf, sum_const, card_univ, nsmul_eq_mul]
    field_simp
    ring
  rw [key] at cs
  calc (∑ x, |f x - 1 / (Fintype.card X : ℝ)|) ^ 2
      ≤ (∑ x, (f x) ^ 2 - 1 / (Fintype.card X : ℝ)) * (Fintype.card X : ℝ) := cs
    _ = (Fintype.card X : ℝ) * ∑ x, (f x) ^ 2 - 1 := by field_simp

/-- The form used in the memo: `TV ≤ sqrt Q / 2` with `TV = (1/2) Σ |f x - 1/m|`. -/
theorem tv_le_half_sqrt_collision {X : Type*} [Fintype X] [Nonempty X]
    (f : X → ℝ) (hf : ∑ x, f x = 1) :
    (1 / 2 : ℝ) * ∑ x, |f x - 1 / (Fintype.card X : ℝ)|
      ≤ Real.sqrt ((Fintype.card X : ℝ) * ∑ x, (f x) ^ 2 - 1) / 2 := by
  have h := tv_sq_le_collision f hf
  have hnn : 0 ≤ ∑ x, |f x - 1 / (Fintype.card X : ℝ)| :=
    sum_nonneg (fun x _ => abs_nonneg _)
  have := Real.le_sqrt_of_sq_le h
  linarith

#print axioms tv_sq_le_collision
#print axioms tv_le_half_sqrt_collision
