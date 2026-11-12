/-
The deterministic statements of Section 2 of "The drawn length of the critical
beta-splitting tree grows linearly".

For a finite rooted binary tree T with n(T) leaves, height h(T) (a leaf has height 0),
drawn length l(T) defined by the recursion

    l(leaf) = 0,    l(T) = l(L) + l(R) + 2 + |h(L) - h(R)|,

and S(T) the sum of the depths of its leaves, we prove

    l(T) = (sum of h(T_v) over the internal vertices v) + h(T),
    S(T) = sum of n(T_v) over the internal vertices v,
    h(T) + 1 <= n(T),
    2 (n(T) - 1) <= l(T) <= S(T).

Core Lean 4 only (no Mathlib). On natural numbers `a - b + (b - a)` is |a - b|.
-/

inductive Tree where
  | leaf : Tree
  | node : Tree → Tree → Tree

namespace Tree

/-- Number of leaves. -/
def leaves : Tree → Nat
  | leaf => 1
  | node l r => leaves l + leaves r

/-- Height; a leaf has height 0. -/
def height : Tree → Nat
  | leaf => 0
  | node l r => max (height l) (height r) + 1

/-- Drawn length of the cladogram. -/
def drawn : Tree → Nat
  | leaf => 0
  | node l r => drawn l + drawn r + 2 + (height l - height r + (height r - height l))

/-- Sum of the depths of the leaves. -/
def depthSum : Tree → Nat
  | leaf => 0
  | node l r => depthSum l + depthSum r + leaves l + leaves r

/-- Sum of the heights of the subtrees rooted at internal vertices. -/
def internalHeights : Tree → Nat
  | leaf => 0
  | node l r => internalHeights l + internalHeights r + height (node l r)

/-- Sum of the numbers of leaves of the subtrees rooted at internal vertices. -/
def internalLeaves : Tree → Nat
  | leaf => 0
  | node l r => internalLeaves l + internalLeaves r + leaves (node l r)

/-- Number of internal vertices. -/
def internal : Tree → Nat
  | leaf => 0
  | node l r => internal l + internal r + 1

theorem leaves_pos : ∀ t : Tree, 1 ≤ leaves t
  | leaf => by simp [leaves]
  | node l r => by
      have h1 := leaves_pos l
      have h2 := leaves_pos r
      simp only [leaves]
      omega

theorem internal_eq : ∀ t : Tree, internal t + 1 = leaves t
  | leaf => by simp [internal, leaves]
  | node l r => by
      have h1 := internal_eq l
      have h2 := internal_eq r
      simp only [internal, leaves]
      omega

theorem height_lt_leaves : ∀ t : Tree, height t + 1 ≤ leaves t
  | leaf => by simp [height, leaves]
  | node l r => by
      have h1 := height_lt_leaves l
      have h2 := height_lt_leaves r
      have h3 := leaves_pos l
      have h4 := leaves_pos r
      simp only [height, leaves]
      omega

theorem drawn_eq : ∀ t : Tree, drawn t = internalHeights t + height t
  | leaf => by simp [drawn, internalHeights, height]
  | node l r => by
      have h1 := drawn_eq l
      have h2 := drawn_eq r
      simp only [drawn, internalHeights, height]
      omega

theorem depthSum_eq : ∀ t : Tree, depthSum t = internalLeaves t
  | leaf => by simp [depthSum, internalLeaves]
  | node l r => by
      have h1 := depthSum_eq l
      have h2 := depthSum_eq r
      simp only [depthSum, internalLeaves, leaves]
      omega

theorem two_mul_le_drawn : ∀ t : Tree, 2 * (leaves t - 1) ≤ drawn t
  | leaf => by simp [drawn, leaves]
  | node l r => by
      have h1 := two_mul_le_drawn l
      have h2 := two_mul_le_drawn r
      have h3 := leaves_pos l
      have h4 := leaves_pos r
      simp only [drawn, leaves]
      omega

theorem drawn_le_depthSum : ∀ t : Tree, drawn t ≤ depthSum t
  | leaf => by simp [drawn, depthSum]
  | node l r => by
      have h1 := drawn_le_depthSum l
      have h2 := drawn_le_depthSum r
      have h3 := height_lt_leaves l
      have h4 := height_lt_leaves r
      have h5 := leaves_pos l
      have h6 := leaves_pos r
      simp only [drawn, depthSum]
      omega

end Tree

#print axioms Tree.internal_eq
#print axioms Tree.height_lt_leaves
#print axioms Tree.drawn_eq
#print axioms Tree.depthSum_eq
#print axioms Tree.two_mul_le_drawn
#print axioms Tree.drawn_le_depthSum
