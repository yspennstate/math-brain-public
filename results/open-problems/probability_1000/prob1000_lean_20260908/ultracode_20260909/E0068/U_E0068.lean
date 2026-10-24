import Mathlib

/-!
E0068 (Rozikov, Problem 21): QSOs with V^r = V.
The load-bearing algebraic step of the structural theorem: on an edge [e_i, e_j] a
permutation-times-Volterra QSO acts by the real polynomial t ↦ t + a t (1 - t), and the
(r-1)-fold composition of such edge maps along an orbit is the identity polynomial. Since
natDegree is multiplicative under composition over ℝ, every factor has degree 1, i.e.
every coefficient a vanishes. This file certifies exactly that.
-/

open Polynomial

/-- The edge map of a Volterra QSO: t ↦ t + a·t·(1 - t), as a real polynomial. -/
noncomputable def edgeMap (a : ℝ) : ℝ[X] := X + C a * (X * (1 - X))

lemma edgeMap_zero : edgeMap 0 = X := by
  simp [edgeMap]

lemma edgeMap_natDegree {a : ℝ} (ha : a ≠ 0) : (edgeMap a).natDegree = 2 := by
  have h : edgeMap a = C (-a) * X ^ 2 + C (1 + a) * X + C 0 := by
    unfold edgeMap
    rw [C_neg, C_add, C_1, C_0]
    ring
  rw [h, natDegree_quadratic (neg_ne_zero.mpr ha)]

/-- If p.comp q = X over ℝ then both p and q have natDegree 1. -/
lemma natDegree_eq_one_of_comp_eq_X {p q : ℝ[X]} (h : p.comp q = X) :
    p.natDegree = 1 ∧ q.natDegree = 1 := by
  have h1 : p.natDegree * q.natDegree = 1 := by
    rw [← natDegree_comp, h, natDegree_X]
  constructor
  · first
      | exact Nat.eq_one_of_mul_eq_one_right h1
      | exact (Nat.mul_eq_one.mp h1).1
      | exact (Nat.mul_eq_one_iff.mp h1).1
      | exact (mul_eq_one.mp h1).1
  · first
      | exact Nat.eq_one_of_mul_eq_one_left h1
      | exact (Nat.mul_eq_one.mp h1).2
      | exact (Nat.mul_eq_one_iff.mp h1).2
      | exact (mul_eq_one.mp h1).2

/-- The composite edge map along a list of coefficients: g_{a₁} ∘ g_{a₂} ∘ ⋯ ∘ g_{a_k}. -/
noncomputable def chain : List ℝ → ℝ[X]
  | [] => X
  | a :: as => (edgeMap a).comp (chain as)

/-- If the composite edge map is the identity polynomial, every coefficient is zero. -/
theorem chain_eq_X_all_zero : ∀ (as : List ℝ), chain as = X → ∀ a ∈ as, a = 0
  | [], _, a, ha => by simp at ha
  | a :: as, h, b, hb => by
    simp only [chain] at h
    obtain ⟨h1, _⟩ := natDegree_eq_one_of_comp_eq_X h
    have ha0 : a = 0 := by
      by_contra hne
      rw [edgeMap_natDegree hne] at h1
      norm_num at h1
    have hchain : chain as = X := by
      rw [ha0, edgeMap_zero, X_comp] at h
      exact h
    rcases List.mem_cons.mp hb with rfl | hb'
    · exact ha0
    · exact chain_eq_X_all_zero as hchain b hb'

#print axioms chain_eq_X_all_zero
#print axioms edgeMap_natDegree
#print axioms natDegree_eq_one_of_comp_eq_X
