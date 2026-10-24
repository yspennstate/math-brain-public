import Mathlib.Data.Real.Basic
import Mathlib.Tactic.Linarith
import Mathlib.Tactic.Ring

-- Finite-interval harmonic uniqueness; probability proof is in ATTEMPT.md.
theorem finite_harmonic_profile (L : Nat) (hL : 0 < L) (f : Nat -> Real)
    (h0 : f 0 = 0) (hb : f L = 1)
    (hr : forall k : Nat, k + 2 <= L -> f (k + 2) - f (k + 1) = f (k + 1) - f k) :
    forall n : Nat, n <= L -> f n = (n : Real) / (L : Real) := by
  have hd : forall n : Nat, n + 1 <= L -> f (n + 1) - f n = f 1 - f 0 := by
    intro n
    induction n with
    | zero => intro _; simp
    | succ n ih =>
      intro hn
      have hp : n + 1 <= L := Nat.le_trans (Nat.le_succ (n + 1)) hn
      have hi := ih hp
      have hh := hr n hn
      change f (n + 2) - f (n + 1) = f 1 - f 0
      linarith
  have hl : forall n : Nat, n <= L -> f n = f 0 + (n : Real) * (f 1 - f 0) := by
    intro n
    induction n with
    | zero => intro _; simp
    | succ n ih =>
      intro hn
      have hp : n <= L := Nat.le_trans (Nat.le_succ n) hn
      have hi := ih hp
      have hh := hd n hn
      simp only [Nat.cast_add, Nat.cast_one]
      linarith
  have hs : (L : Real) * (f 1 - f 0) = 1 := by
    have hh := hl L (Nat.le_refl L)
    rw [h0, hb] at hh
    rw [h0]
    linarith
  have hne : Not ((L : Real) = 0) := by exact_mod_cast (Nat.ne_of_gt hL)
  intro n hn
  apply (eq_div_iff hne).2
  rw [hl n hn, h0]
  calc
    (0 + (n : Real) * (f 1 - 0)) * (L : Real) =
        (n : Real) * ((L : Real) * (f 1 - f 0)) := by rw [h0]; ring
    _ = (n : Real) := by rw [hs]; ring

-- The two-sided length constraint for a returning ballistic excursion.
theorem returning_excursion_gap (s n t R e : Real)
    (hout : e * n - R <= n - s) (hback : e * n - R <= t - n) :
    2 * e * n - 2 * R <= t - s := by linarith
