import Bench.E548.Counting
set_option autoImplicit true
set_option relaxedAutoImplicit true
set_option maxHeartbeats 4000000

open SimpleGraph

/- An involution on permutation words: reverse the initial block through a
cut and also reverse the remaining block. -/
namespace Erdos548

def reverseWordAt {α : Type*} (l : List α) (c : ℕ) : List α :=
  (l.take c).reverse ++ (l.drop c).reverse

lemma reverseWordAt_perm {α : Type*} (l : List α) (c : ℕ) : (reverseWordAt l c).Perm l := by
  have h := (List.reverse_perm (l.take c)).append (List.reverse_perm (l.drop c))
  simpa only [reverseWordAt,List.take_append_drop] using h

lemma reverseWordAt_involutive {α : Type*} (l : List α) (c : ℕ) :
    reverseWordAt (reverseWordAt l c) c=l := by
  by_cases hc : c ≤ l.length
  · have hrlen : (l.take c).reverse.length=c := by simp only [List.length_reverse,List.length_take]; omega
    have ht : (reverseWordAt l c).take c=(l.take c).reverse := by
      simpa only [reverseWordAt,hrlen] using
        (List.take_left (l₁:=(l.take c).reverse) (l₂:=(l.drop c).reverse))
    have hd : (reverseWordAt l c).drop c=(l.drop c).reverse := by
      simpa only [reverseWordAt,hrlen] using
        (List.drop_left (l₁:=(l.take c).reverse) (l₂:=(l.drop c).reverse))
    rw [reverseWordAt,ht,hd,List.reverse_reverse,List.reverse_reverse,List.take_append_drop]
  · have hlc : l.length ≤ c := by omega
    have he : reverseWordAt l c=l.reverse := by
      simp [reverseWordAt,List.take_of_length_le hlc,List.drop_eq_nil_of_le hlc]
    have hrc : l.reverse.length ≤ c := by simpa using hlc
    rw [he]
    simp [reverseWordAt,List.take_of_length_le hrc,List.drop_eq_nil_of_le hrc]

def reverseCutPair {α : Type*} (p : List α × ℕ) : List α × ℕ :=
  (reverseWordAt p.1 (p.2+1),p.2)

lemma reverseCutPair_involutive {α : Type*} : Function.Involutive (@reverseCutPair α) := by
  rintro ⟨l,k⟩
  exact Prod.ext (reverseWordAt_involutive l (k+1)) rfl

lemma reverseCutPair_injective {α : Type*} : Function.Injective (@reverseCutPair α) :=
  reverseCutPair_involutive.injective

lemma reverseWordAt_decomposition {α : Type*} (b w : α) (p q : List α) :
    reverseWordAt (b::(p++w::q)) (p.length+2) = w::(p.reverse++b::q.reverse) := by
  have he : b::(p++w::q) = (b::(p++[w]))++q := by simp only [List.cons_append,List.append_assoc,List.nil_append]
  have hlen : (b::(p++[w])).length=p.length+2 := by simp
  rw [he,← hlen,reverseWordAt,List.take_left,List.drop_left]
  simp only [List.reverse_cons,List.reverse_append,List.cons_append,
    List.nil_append,List.append_assoc,List.reverse_nil]

/-- A first-state loss of at most one per full word, followed by the cut
reversal involution. This is purely finite counting. -/
lemma full_word_transfer_count {α : Type*} [DecidableEq α]
    (l₀ : List α) (N N' : α → α → Prop) (A B : α → Finset α → Prop)
    (hstep : ∀ l, l.Perm l₀ → ∀ k, k<l₀.length → FullWordQualifies N A l k →
      ∀ j, j<k → FullWordQualifies N A l j →
        FullWordQualifies N' B (reverseWordAt l (k+1)) k) :
    fullWordCount l₀ N A ≤ fullWordCount l₀ N' B + (permutationWords l₀).card := by
  classical
  let D := fullGoodWordCuts l₀ N A
  let M := D.filter (fun p => ∃ j, j<p.2 ∧ FullWordQualifies N A p.1 j)
  have hMD : M ⊆ D := Finset.filter_subset _ _
  have hfirst : (D \ M).card ≤ (permutationWords l₀).card := by
    apply Finset.card_le_card_of_injOn Prod.fst
    · intro p hp
      have hpD := (Finset.mem_sdiff.mp hp).1
      exact (mem_permutationWords _ _).mpr ((mem_fullGoodWordCuts l₀ N A p.1 p.2).mp hpD).1
    · intro p hp q hq he
      have hpD := (mem_fullGoodWordCuts l₀ N A p.1 p.2).mp (Finset.mem_sdiff.mp hp).1
      have hqD := (mem_fullGoodWordCuts l₀ N A q.1 q.2).mp (Finset.mem_sdiff.mp hq).1
      apply Prod.ext he
      by_contra hn
      rcases lt_or_gt_of_ne hn with h | h
      · apply (Finset.mem_sdiff.mp hq).2
        exact Finset.mem_filter.mpr ⟨(Finset.mem_sdiff.mp hq).1,
          p.2,h,he ▸ hpD.2.2⟩
      · apply (Finset.mem_sdiff.mp hp).2
        exact Finset.mem_filter.mpr ⟨(Finset.mem_sdiff.mp hp).1,
          q.2,h,he.symm ▸ hqD.2.2⟩
  have hmove : M.card ≤ (fullGoodWordCuts l₀ N' B).card := by
    apply Finset.card_le_card_of_injOn reverseCutPair
    · rintro ⟨l,k⟩ hp
      obtain ⟨hpD,j,hjk,hj⟩ := Finset.mem_filter.mp hp
      obtain ⟨hl,hk,hs⟩ := (mem_fullGoodWordCuts l₀ N A l k).mp hpD
      exact (mem_fullGoodWordCuts l₀ N' B _ _).mpr
        ⟨(reverseWordAt_perm l (k+1)).trans hl,hk,hstep l hl k hk hs j hjk hj⟩
    · exact fun _ _ _ _ h => reverseCutPair_injective h
  have he := Finset.card_sdiff_add_card_eq_card hMD
  change D.card ≤ (fullGoodWordCuts l₀ N' B).card + (permutationWords l₀).card
  omega

end Erdos548

namespace Erdos548

/-- Attach a set of new leaves to a fixed vertex. -/
def attachLeaves {V : Type*} (S : SimpleGraph V) (r : V) (s : ℕ) :
    SimpleGraph (V ⊕ Fin s) where
  Adj
    | .inl a, .inl b => S.Adj a b
    | .inl a, .inr _ => a = r
    | .inr _, .inl b => b = r
    | .inr _, .inr _ => False
  symm := by
    constructor
    rintro (a | a) (b | b) h <;> first | exact h.symm | exact h
  loopless := by constructor; rintro (a | a) <;> simp

end Erdos548

namespace Erdos548

lemma attach_single_leaf_copy {U V : Type*} (S : SimpleGraph U) (G : SimpleGraph V)
    (r : U) (f : S.Copy G) (w : V) (hw : G.Adj (f r) w) (hfree : w ∉ Set.range f) :
    ∃ F : (attachLeaves S r 1).Copy G,
      (∀ x, F (Sum.inl x) = f x) ∧ F (Sum.inr 0) = w := by
  classical
  let F : U ⊕ Fin 1 → V := Sum.elim f (fun _ => w)
  have hadj : ∀ x y, (attachLeaves S r 1).Adj x y → G.Adj (F x) (F y) := by
    rintro (x | x) (y | y) h
    · exact f.toHom.map_adj h
    · have he : x = r := h
      subst x
      exact hw
    · have he : y = r := h
      subst y
      exact hw.symm
    · exact h.elim
  have hinj : Function.Injective F := by
    rintro (x | x) (y | y) h
    · exact congrArg Sum.inl (f.injective h)
    · exact (hfree ⟨x,h⟩).elim
    · exact (hfree ⟨y,h.symm⟩).elim
    · exact congrArg Sum.inr (Subsingleton.elim _ _)
  exact ⟨⟨⟨F,fun {x y} h => hadj x y h⟩,hinj⟩,fun _ => rfl,rfl⟩


end Erdos548
