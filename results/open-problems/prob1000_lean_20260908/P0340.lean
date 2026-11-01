/-
P0340 — Aldous & Janson, "Critical beta-splitting random tree II: overview and
open problems" (arXiv:2303.02529), Open Problem 14, PDF pp. 54-55:

  "Prove that L_n grows roughly like n log^4 n"

where L_n = E[drawn length of DTCS(n)], the drawn length of a cladogram being
defined by their recursion (73)

  l(chi_m) = l(chi_i) + l(chi_{m-i}) + 2 + |h(chi_{m-i}) - h(chi_i)|

with h the tree height.  The conjectured rate is WRONG: the drawn length of ANY
full binary tree is at most its total leaf depth, and by their own Theorem 3
the expected leaf depth of DTCS(n) is ~ 3 pi^-2 log^2 n, so

  L_n <= n * E[leaf depth] = O(n log^2 n) = o(n log^4 n).

(Simulation puts the truth at L_n / n -> a constant near 4.86, i.e. Theta(n).)

This file proves the deterministic combinatorial half — the inequality and the
exact decomposition — with no `sorry` and no `native_decide`.  The probabilistic
input, E[leaf depth] ~ 3 pi^-2 log^2 n, is Aldous-Janson's published Theorem 3
and is not formalised here.
-/
import Mathlib.Tactic.Ring
import Mathlib.Tactic.Linarith

namespace P0340

/-- A full (strictly binary) tree: the shape of a cladogram. -/
inductive BT where
  | leaf : BT
  | node : BT → BT → BT
  deriving Repr

namespace BT

def leaves : BT → ℕ
  | leaf     => 1
  | node l r => leaves l + leaves r

def height : BT → ℕ
  | leaf     => 0
  | node l r => 1 + max (height l) (height r)

/-- `|a - b|` on `ℕ`, via truncated subtraction. -/
def adiff (a b : ℕ) : ℕ := (a - b) + (b - a)

/-- Aldous-Janson's recursion (73). -/
def drawn : BT → ℕ
  | leaf     => 0
  | node l r => drawn l + drawn r + 2 + adiff (height r) (height l)

/-- Sum of the depths of all leaves, measured from a root at depth `d`. -/
def sumDepth : BT → ℕ → ℕ
  | leaf,     d => d
  | node l r, d => sumDepth l (d + 1) + sumDepth r (d + 1)

/-- Sum of the heights of all internal nodes. -/
def sumHeights : BT → ℕ
  | leaf     => 0
  | node l r => sumHeights l + sumHeights r + (1 + max (height l) (height r))

theorem one_le_leaves (t : BT) : 1 ≤ leaves t := by
  induction t with
  | leaf => simp [leaves]
  | node l r ihl ihr => simp [leaves]; omega

/-- A full binary tree with `k` leaves has height at most `k - 1`. -/
theorem height_succ_le_leaves (t : BT) : height t + 1 ≤ leaves t := by
  induction t with
  | leaf => simp [height, leaves]
  | node l r ihl ihr =>
      have hl := one_le_leaves l
      have hr := one_le_leaves r
      simp only [height, leaves]
      omega

theorem sumDepth_shift (t : BT) (d : ℕ) : sumDepth t (d + 1) = sumDepth t d + leaves t := by
  induction t generalizing d with
  | leaf => simp [sumDepth, leaves]
  | node l r ihl ihr =>
      simp only [sumDepth, leaves, ihl, ihr]
      omega

/-- **The drawn length is at most the total leaf depth.**  Deterministic, for
every full binary tree. -/
theorem drawn_le_sumDepth (t : BT) : drawn t ≤ sumDepth t 0 := by
  induction t with
  | leaf => simp [drawn, sumDepth]
  | node l r ihl ihr =>
      have hl := height_succ_le_leaves l
      have hr := height_succ_le_leaves r
      have el := sumDepth_shift l 0
      have er := sumDepth_shift r 0
      simp only [drawn, sumDepth, adiff] at *
      omega

/-- **The exact decomposition**: drawn length = sum of internal subtree heights
+ the height of the whole tree. -/
theorem drawn_eq_sumHeights_add_height (t : BT) :
    drawn t = sumHeights t + height t := by
  induction t with
  | leaf => simp [drawn, sumHeights, height]
  | node l r ihl ihr =>
      have hl := height_succ_le_leaves l
      have hr := height_succ_le_leaves r
      simp only [drawn, sumHeights, height, adiff] at *
      omega

end BT
end P0340

#print axioms P0340.BT.height_succ_le_leaves
#print axioms P0340.BT.sumDepth_shift
#print axioms P0340.BT.drawn_le_sumDepth
#print axioms P0340.BT.drawn_eq_sumHeights_add_height
