import Bench.E548.Words
set_option autoImplicit true
set_option relaxedAutoImplicit true
set_option maxHeartbeats 4000000

open SimpleGraph

/- Exact cardinalities of permutation words and marked prefixes. -/
namespace Erdos548
attribute [local instance] Classical.propDecidable

noncomputable def permutationWords {α : Type*} [DecidableEq α] (l : List α) :
    Finset (List α) := l.permutations.toFinset

lemma mem_permutationWords {α : Type*} [DecidableEq α] (l q : List α) :
    q ∈ permutationWords l ↔ q.Perm l := by
  simp only [permutationWords,List.mem_toFinset,List.mem_permutations]

lemma permutationWords_card {α : Type*} [DecidableEq α] (l : List α) (hl : l.Nodup) :
    (permutationWords l).card=l.length.factorial := by
  rw [permutationWords,List.toFinset_card_of_nodup (List.nodup_permutations l hl),
    List.length_permutations]

lemma markedEnd_take_succ {α : Type*} (N : α → Prop) (l : List α) (i : ℕ)
    (hi : i < l.length) : MarkedEnd N (l.take (i+1)) ↔ N l[i] := by
  rw [List.take_succ_eq_append_getElem hi]
  simp only [MarkedEnd,List.getLast?_concat,Option.some.injEq]
  constructor
  · rintro ⟨a,he,ha⟩
    exact he.symm ▸ ha
  · intro h
    exact ⟨l[i],rfl,h⟩

lemma markedEnd_take_pos {α : Type*} {N : α → Prop} {l : List α} {k : ℕ}
    (h : MarkedEnd N (l.take k)) : 0 < k := by
  by_contra hn
  have hk : k=0 := by omega
  rw [hk,List.take_zero] at h
  exact markedEnd_not_nil h rfl

lemma markedEnd_take_iff {α : Type*} (N : α → Prop) (l : List α) (k : ℕ)
    (hk : k ≤ l.length) :
    MarkedEnd N (l.take k) ↔ ∃ h : 0<k, N (l[k-1]'(by omega)) := by
  constructor
  · intro h
    have hp := markedEnd_take_pos h
    refine ⟨hp,?_⟩
    have hh := (markedEnd_take_succ N l (k-1) (by omega)).mp
      (show MarkedEnd N (l.take ((k-1)+1)) from by simpa only [Nat.sub_add_cancel hp] using h)
    exact hh
  · rintro ⟨hp,h⟩
    have hh := (markedEnd_take_succ N l (k-1) (by omega)).mpr h
    simpa only [Nat.sub_add_cancel hp] using hh

lemma marked_prefix_card {α : Type*} [DecidableEq α] (N : α → Prop)
    (l : List α) (hl : l.Nodup) :
    (Finset.filter (fun k => MarkedEnd N (l.take k)) (Finset.range (l.length+1))).card =
      (l.toFinset.filter N).card := by
  classical
  let F := Finset.filter (fun k => MarkedEnd N (l.take k)) (Finset.range (l.length+1))
  have hk : ∀ k ∈ F, k ≤ l.length := by
    intro k hk
    exact Nat.le_of_lt_succ (Finset.mem_range.mp (Finset.mem_filter.mp hk).1)
  have hp : ∀ k ∈ F, 0 < k := fun k hk => markedEnd_take_pos (Finset.mem_filter.mp hk).2
  let f : (k : ℕ) → k ∈ F → α := fun k h => l[k-1]'(by have := hk k h; have := hp k h; omega)
  apply Finset.card_bij f
  · intro k h
    refine Finset.mem_filter.mpr ⟨List.mem_toFinset.mpr (List.getElem_mem _),?_⟩
    exact ((markedEnd_take_iff N l k (hk k h)).mp (Finset.mem_filter.mp h).2).2
  · intro k h j hj he
    have hh : k-1=j-1 := hl.getElem_inj_iff.mp he
    have := hp k h
    have := hp j hj
    omega
  · intro a ha
    obtain ⟨haL,haN⟩ := Finset.mem_filter.mp ha
    obtain ⟨i,hi,hia⟩ := List.mem_iff_getElem.mp (List.mem_toFinset.mp haL)
    have hm : MarkedEnd N (l.take (i+1)) := (markedEnd_take_succ N l i hi).mpr (hia.symm ▸ haN)
    have hF : i+1 ∈ F := Finset.mem_filter.mpr
      ⟨Finset.mem_range.mpr (by omega),hm⟩
    refine ⟨i+1,hF,?_⟩
    simpa only [f,Nat.add_sub_cancel] using hia

lemma goodWordCuts_true_card {α : Type*} [DecidableEq α]
    (W : Finset (List α)) (m : ℕ) (N : α → Prop)
    (hlen : ∀ l ∈ W, l.length=m) (hnodup : ∀ l ∈ W, l.Nodup) :
    (goodWordCuts W m N (fun _ => True)).card =
      ∑ l ∈ W, (l.toFinset.filter N).card := by
  classical
  unfold goodWordCuts
  rw [Finset.card_filter,Finset.sum_product]
  apply Finset.sum_congr rfl
  intro l hl
  simp only [and_true]
  rw [← Finset.card_filter,← hlen l hl,marked_prefix_card N l (hnodup l hl)]

lemma allowedWordCuts_card {α : Type*} [DecidableEq α]
    (W : Finset (List α)) (m : ℕ) (N : α → Prop) :
    (allowedWordCuts W m N).card = W.card+(goodWordCuts W m N (fun _ => True)).card := by
  classical
  let E := W.image (fun l => (l,0))
  have hdis : Disjoint E (goodWordCuts W m N (fun _ => True)) := by
    apply Finset.disjoint_left.mpr
    rintro p hp hgood
    obtain ⟨l,_,rfl⟩ := Finset.mem_image.mp hp
    simp only [goodWordCuts,Finset.mem_filter] at hgood
    have hm := hgood.2.1
    simp only [List.take_zero] at hm
    exact markedEnd_not_nil hm rfl
  have he : allowedWordCuts W m N = E ∪ goodWordCuts W m N (fun _ => True) := by
    ext p
    simp only [allowedWordCuts,goodWordCuts,Finset.mem_filter,Finset.mem_product,
      Finset.mem_range,Finset.mem_union,and_true]
    constructor
    · rintro ⟨⟨hl,hk⟩,he | hm⟩
      · exact Or.inl (Finset.mem_image.mpr ⟨p.1,hl,Prod.ext rfl he.symm⟩)
      · exact Or.inr ⟨⟨hl,hk⟩,hm⟩
    · rintro (hp | hp)
      · obtain ⟨l,hl,rfl⟩ := Finset.mem_image.mp hp
        exact ⟨⟨hl,by omega⟩,Or.inl rfl⟩
      · exact ⟨hp.1,Or.inr hp.2⟩
  rw [he,Finset.card_union_of_disjoint hdis]
  congr 1
  exact Finset.card_image_of_injective _ (fun _ _ h => congrArg Prod.fst h)

end Erdos548

/- Full permutation words, grouped by their first letter. -/
namespace Erdos548
attribute [local instance] Classical.propDecidable

/-- The first letter is a distinguished root, and a marked cut is taken in
the remaining word. The family is allowed to depend on that root. -/
def FullWordQualifies {α : Type*} [DecidableEq α]
    (N : α → α → Prop) (A : α → Finset α → Prop) (l : List α) (k : ℕ) : Prop :=
  ∃ b q, l=b::q ∧ MarkedEnd (N b) (q.take k) ∧ A b (q.take k).toFinset

lemma fullWordQualifies_cons {α : Type*} [DecidableEq α]
    (N : α → α → Prop) (A : α → Finset α → Prop) (b : α) (q : List α) (k : ℕ) :
    FullWordQualifies N A (b::q) k ↔
      MarkedEnd (N b) (q.take k) ∧ A b (q.take k).toFinset := by
  constructor
  · rintro ⟨b',q',he,hm,hA⟩
    obtain ⟨rfl,rfl⟩ := List.cons.inj he
    exact ⟨hm,hA⟩
  · rintro ⟨hm,hA⟩
    exact ⟨b,q,rfl,hm,hA⟩

noncomputable def fullGoodWordCuts {α : Type*} [DecidableEq α]
    (l₀ : List α) (N : α → α → Prop) (A : α → Finset α → Prop) : Finset (List α × ℕ) :=
  (permutationWords l₀ ×ˢ Finset.range l₀.length).filter
    (fun p => FullWordQualifies N A p.1 p.2)

noncomputable def fullWordCount {α : Type*} [DecidableEq α]
    (l₀ : List α) (N : α → α → Prop) (A : α → Finset α → Prop) : ℕ :=
  (fullGoodWordCuts l₀ N A).card

lemma mem_fullGoodWordCuts {α : Type*} [DecidableEq α]
    (l₀ : List α) (N : α → α → Prop) (A : α → Finset α → Prop) (l : List α) (k : ℕ) :
    (l,k) ∈ fullGoodWordCuts l₀ N A ↔ l.Perm l₀ ∧ k<l₀.length ∧ FullWordQualifies N A l k := by
  simp only [fullGoodWordCuts,Finset.mem_filter,Finset.mem_product,mem_permutationWords,
    Finset.mem_range,and_assoc]

lemma fullWordCount_eq_sum {α : Type*} [DecidableEq α]
    (l₀ : List α) (N : α → α → Prop) (A : α → Finset α → Prop) :
    fullWordCount l₀ N A = ∑ b ∈ l₀.toFinset,
      (goodWordCuts (permutationWords (l₀.erase b)) (l₀.length-1) (N b) (A b)).card := by
  classical
  let F := fun b => goodWordCuts (permutationWords (l₀.erase b)) (l₀.length-1) (N b) (A b)
  let E := fun b => (F b).image (fun p => (b::p.1,p.2))
  have he : fullGoodWordCuts l₀ N A = l₀.toFinset.biUnion E := by
    ext p
    rcases p with ⟨l,k⟩
    rw [mem_fullGoodWordCuts,Finset.mem_biUnion]
    constructor
    · rintro ⟨hl,hk,b,q,rfl,hm,hA⟩
      obtain ⟨hb,hq⟩ := List.cons_perm_iff_perm_erase.mp hl
      refine ⟨b,List.mem_toFinset.mpr hb,Finset.mem_image.mpr ⟨(q,k),?_,rfl⟩⟩
      have hn : 0 < l₀.length := by have := List.length_pos_of_mem hb; omega
      exact Finset.mem_filter.mpr ⟨Finset.mem_product.mpr
        ⟨(mem_permutationWords _ _).mpr hq,Finset.mem_range.mpr (by omega)⟩,hm,hA⟩
    · rintro ⟨b,hb,hp⟩
      obtain ⟨⟨q,j⟩,hq,heq⟩ := Finset.mem_image.mp hp
      have hword : b::q=l := congrArg Prod.fst heq
      have hj : j=k := congrArg Prod.snd heq
      subst l
      subst j
      obtain ⟨hbase,hm,hA⟩ := Finset.mem_filter.mp hq
      obtain ⟨hq,hk⟩ := Finset.mem_product.mp hbase
      have hbL := List.mem_toFinset.mp hb
      have hn := List.length_pos_of_mem hbL
      refine ⟨List.cons_perm_iff_perm_erase.mpr ⟨hbL,(mem_permutationWords _ _).mp hq⟩,
        by have := Finset.mem_range.mp hk; omega,b,q,rfl,hm,hA⟩
  have hd : (l₀.toFinset : Set α).PairwiseDisjoint E := by
    intro b hb c hc hbc
    apply Finset.disjoint_left.mpr
    rintro p hp hq
    obtain ⟨⟨q,k⟩,_,he₁⟩ := Finset.mem_image.mp hp
    obtain ⟨⟨r,j⟩,_,he₂⟩ := Finset.mem_image.mp hq
    have hword := congrArg Prod.fst (he₁.trans he₂.symm)
    exact hbc (List.cons.inj hword).1
  unfold fullWordCount
  rw [he,Finset.card_biUnion hd]
  apply Finset.sum_congr rfl
  intro b hb
  apply Finset.card_image_of_injective
  rintro ⟨q,k⟩ ⟨r,j⟩ h
  have hq := (List.cons.inj (congrArg Prod.fst h)).2
  have hk : k=j := congrArg Prod.snd h
  exact Prod.ext hq hk

/-- Sum of the numbers of outer words: exactly one full word for every
choice of its head and its outer permutation. -/
lemma sum_outer_words_card {α : Type*} [DecidableEq α] (l₀ : List α) (hl : l₀.Nodup)
    (hne : l₀ ≠ []) :
    (∑ b ∈ l₀.toFinset, (permutationWords (l₀.erase b)).card) = (permutationWords l₀).card := by
  classical
  have hn : 0 < l₀.length := List.length_pos_iff.mpr hne
  have he : ∀ b ∈ l₀.toFinset,
      (permutationWords (l₀.erase b)).card=(l₀.length-1).factorial := by
    intro b hb
    rw [permutationWords_card _ (hl.erase b),List.length_erase_of_mem (List.mem_toFinset.mp hb)]
  rw [Finset.sum_congr rfl he]
  simp only [Finset.sum_const,nsmul_eq_mul,List.toFinset_card_of_nodup hl,
    permutationWords_card l₀ hl,Nat.cast_id]
  simpa only [Nat.sub_add_cancel hn] using (Nat.factorial_succ (l₀.length-1)).symm

/-- Root-dependent gluing, summed over ALL full permutation words. -/
lemma full_word_gluing_count {α : Type*} [DecidableEq α]
    (l₀ : List α) (hl : l₀.Nodup) (hne : l₀ ≠ [])
    (N : α → α → Prop) (A B C : α → Finset α → Prop)
    (hCA : ∀ b X, C b X → A b X)
    (hglue : ∀ b R X, Disjoint R X → A b R → B b X → C b (R ∪ X)) :
    fullWordCount l₀ N A + fullWordCount l₀ N B ≤
      fullWordCount l₀ N (fun _ _ => True) + (permutationWords l₀).card + fullWordCount l₀ N C := by
  classical
  have hh : ∀ b ∈ l₀.toFinset,
      (goodWordCuts (permutationWords (l₀.erase b)) (l₀.length-1) (N b) (A b)).card +
        (goodWordCuts (permutationWords (l₀.erase b)) (l₀.length-1) (N b) (B b)).card ≤
      (goodWordCuts (permutationWords (l₀.erase b)) (l₀.length-1) (N b) (fun _ => True)).card +
        (permutationWords (l₀.erase b)).card +
        (goodWordCuts (permutationWords (l₀.erase b)) (l₀.length-1) (N b) (C b)).card := by
    intro b hb
    have he := marked_word_gluing_count (permutationWords (l₀.erase b)) (l₀.length-1) (N b)
      (A b) (B b) (C b)
      (fun q hq => ((mem_permutationWords _ _).mp hq).length_eq.trans
        (List.length_erase_of_mem (List.mem_toFinset.mp hb)))
      (fun q hq => ((mem_permutationWords _ _).mp hq).nodup_iff.mpr (hl.erase b))
      (fun q hq q' hp => (mem_permutationWords _ _).mpr
        (hp.trans ((mem_permutationWords _ _).mp hq))) (hCA b) (hglue b)
    rw [allowedWordCuts_card] at he
    omega
  have hs := Finset.sum_le_sum hh
  simp only [Finset.sum_add_distrib] at hs
  rw [sum_outer_words_card l₀ hl hne] at hs
  simpa only [fullWordCount_eq_sum] using hs

end Erdos548
