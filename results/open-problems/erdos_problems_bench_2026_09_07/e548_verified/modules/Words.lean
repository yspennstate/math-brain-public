import Mathlib
set_option autoImplicit true
set_option relaxedAutoImplicit true
set_option maxHeartbeats 4000000

open SimpleGraph

/- Reversible prefix-block rotation for finite marked-word counting.
No graph-density statement is assumed in this file. -/
namespace Erdos548

/-- A nonempty marked last letter. -/
def MarkedEnd {α : Type*} (N : α → Prop) (l : List α) : Prop :=
  ∃ a, l.getLast? = some a ∧ N a

lemma markedEnd_not_nil {α : Type*} {N : α → Prop} {l : List α}
    (h : MarkedEnd N l) : l ≠ [] := by
  rintro rfl
  obtain ⟨a,ha,_⟩ := h
  simp at ha

lemma markedEnd_append_right {α : Type*} {N : α → Prop} {r x : List α}
    (h : MarkedEnd N (r++x)) (hx : x ≠ []) : MarkedEnd N x := by
  obtain ⟨a,ha,hN⟩ := h
  have hn : x.getLast? ≠ none := fun he => hx (List.getLast?_eq_none_iff.mp he)
  cases he : x.getLast? with
  | none => exact (hn he).elim
  | some b =>
    rw [List.getLast?_append,he] at ha
    change some b = some a at ha
    have hba := Option.some.inj ha
    subst b
    exact ⟨a,he,hN⟩

/-- The displayed word is the first qualifying prefix of any extension. -/
def FirstPrefix {α : Type*} (P : List α → Prop) (r : List α) : Prop :=
  P r ∧ ∀ j < r.length, ¬P (r.take j)

lemma firstPrefix_unique {α : Type*} {P : List α → Prop} {r y r' y' : List α}
    (hr : FirstPrefix P r) (hr' : FirstPrefix P r') (he : r++y=r'++y') :
    r=r' ∧ y=y' := by
  have hlen : r.length=r'.length := by
    by_contra hn
    rcases lt_or_gt_of_ne hn with h | h
    · have hh := congrArg (List.take r.length) he
      rw [List.take_left,List.take_append_of_le_length h.le] at hh
      exact hr'.2 r.length h (hh ▸ hr.1)
    · have hh := congrArg (List.take r'.length) he
      rw [List.take_append_of_le_length h.le,List.take_left] at hh
      exact hr.2 r'.length h (hh.symm ▸ hr'.1)
  exact ⟨List.append_inj_left he hlen,List.append_inj_right he hlen⟩

lemma firstPrefix_rotation_injective {α : Type*} {P : List α → Prop}
    {r x y r' x' y' : List α} (hr : FirstPrefix P r) (hr' : FirstPrefix P r')
    (he : (x++(r++y),x.length)=(x'++(r'++y'),x'.length)) :
    ((r++x)++y,r.length+x.length)=((r'++x')++y',r'.length+x'.length) := by
  have hword := congrArg Prod.fst he
  have hlen := congrArg Prod.snd he
  have hx : x=x' := List.append_inj_left hword hlen
  have hs : r++y=r'++y' := List.append_inj_right hword hlen
  obtain ⟨hrEq,hyEq⟩ := firstPrefix_unique hr hr' hs
  subst x'
  subst r'
  subst y'
  rfl

/-- Cut at the first qualifying marked prefix and rotate it past the rest of
an input prefix. Its new prefix is a disjoint difference and hence cannot
belong to the second family. -/
lemma marked_prefix_rotation_exists {α : Type*} [DecidableEq α]
    (N : α → Prop) (A B C : Finset α → Prop)
    (hglue : ∀ R X, Disjoint R X → A R → B X → C (R ∪ X))
    (l : List α) (hl : l.Nodup) (k : ℕ) (hk : k ≤ l.length)
    (hm : MarkedEnd N (l.take k)) (hA : A (l.take k).toFinset)
    (hC : ¬C (l.take k).toFinset) :
    ∃ r x y : List α,
      l=(r++x)++y ∧ k=r.length+x.length ∧
      FirstPrefix (fun q => MarkedEnd N q ∧ A q.toFinset ∧ ¬C q.toFinset) r ∧
      (x=[] ∨ MarkedEnd N x) ∧ ¬B x.toFinset := by
  classical
  let P : List α → Prop := fun q => MarkedEnd N q ∧ A q.toFinset ∧ ¬C q.toFinset
  have hex : ∃ j, j ≤ k ∧ P (l.take j) := ⟨k,le_rfl,hm,hA,hC⟩
  let j := Nat.find hex
  have hjk : j ≤ k := (Nat.find_spec hex).1
  have hjP : P (l.take j) := (Nat.find_spec hex).2
  let r := l.take j
  let x := (l.drop j).take (k-j)
  let y := l.drop k
  have hrlen : r.length=j := by simp only [r,List.length_take]; omega
  have hxlen : x.length=k-j := by
    simp only [x,List.length_take,List.length_drop]
    omega
  have hrx : r++x=l.take k := by
    dsimp only [r,x]
    rw [← List.take_add]
    congr 1
    omega
  have hword : (r++x)++y=l := by
    rw [hrx]
    exact List.take_append_drop k l
  refine ⟨r,x,y,hword.symm,by omega,⟨hjP,?_⟩,?_,?_⟩
  · intro i hi hPi
    have hij : i < j := by omega
    have hp : P (l.take i) := by
      simpa only [r,List.take_take,Nat.min_eq_left hij.le] using hPi
    exact Nat.find_min hex hij ⟨by omega,hp⟩
  · by_cases hx : x=[]
    · exact Or.inl hx
    · exact Or.inr (markedEnd_append_right (hrx.symm ▸ hm) hx)
  · intro hB
    have hnr : (r++x).Nodup := hrx.symm ▸ hl.sublist (List.take_sublist k l)
    have hd : Disjoint r.toFinset x.toFinset := by
      apply Finset.disjoint_left.mpr
      intro a ha hb
      exact (List.disjoint_left.mp hnr.disjoint) (List.mem_toFinset.mp ha) (List.mem_toFinset.mp hb)
    have hh := hglue r.toFinset x.toFinset hd hjP.2.1 hB
    apply hC
    rwa [← List.toFinset_append,hrx] at hh

/-- The relation records the reversible block rotation, without choosing a
particular implementation of the first-prefix search. -/
def PrefixRotation {α : Type*} (P : List α → Prop)
    (u v : List α × ℕ) : Prop :=
  ∃ r x y : List α, u=((r++x)++y,r.length+x.length) ∧
    v=(x++(r++y),x.length) ∧ FirstPrefix P r

lemma prefixRotation_left_unique {α : Type*} {P : List α → Prop}
    {u u' v : List α × ℕ} (h : PrefixRotation P u v) (h' : PrefixRotation P u' v) : u=u' := by
  obtain ⟨r,x,y,rfl,hv,hr⟩ := h
  obtain ⟨r',x',y',rfl,hv',hr'⟩ := h'
  exact firstPrefix_rotation_injective hr hr' (hv.symm.trans hv')

noncomputable def allowedWordCuts {α : Type*} (W : Finset (List α)) (m : ℕ)
    (N : α → Prop) : Finset (List α × ℕ) := by
  classical
  exact (W ×ˢ Finset.range (m+1)).filter (fun p => p.2=0 ∨ MarkedEnd N (p.1.take p.2))

noncomputable def goodWordCuts {α : Type*} [DecidableEq α]
    (W : Finset (List α)) (m : ℕ) (N : α → Prop) (A : Finset α → Prop) :
    Finset (List α × ℕ) := by
  classical
  exact (W ×ˢ Finset.range (m+1)).filter
    (fun p => MarkedEnd N (p.1.take p.2) ∧ A (p.1.take p.2).toFinset)

lemma goodWordCuts_subset_allowed {α : Type*} [DecidableEq α]
    (W : Finset (List α)) (m : ℕ) (N : α → Prop) (A : Finset α → Prop) :
    goodWordCuts W m N A ⊆ allowedWordCuts W m N := by
  classical
  intro p hp
  obtain ⟨hp,hm,_⟩ := Finset.mem_filter.mp hp
  exact Finset.mem_filter.mpr ⟨hp,Or.inr hm⟩

lemma goodWordCuts_mono {α : Type*} [DecidableEq α]
    (W : Finset (List α)) (m : ℕ) (N : α → Prop) (A C : Finset α → Prop)
    (hCA : ∀ X, C X → A X) : goodWordCuts W m N C ⊆ goodWordCuts W m N A := by
  classical
  intro p hp
  obtain ⟨hp,hm,hC⟩ := Finset.mem_filter.mp hp
  exact Finset.mem_filter.mpr ⟨hp,hm,hCA _ hC⟩

/-- The exact finite marked-word gluing inequality. The ambient word family
must be closed under permutation; every word is repetition-free. -/
lemma marked_word_gluing_count {α : Type*} [DecidableEq α]
    (W : Finset (List α)) (m : ℕ) (N : α → Prop) (A B C : Finset α → Prop)
    (hlen : ∀ l ∈ W, l.length=m) (hnodup : ∀ l ∈ W, l.Nodup)
    (hperm : ∀ l ∈ W, ∀ l', l'.Perm l → l' ∈ W)
    (hCA : ∀ X, C X → A X)
    (hglue : ∀ R X, Disjoint R X → A R → B X → C (R ∪ X)) :
    (goodWordCuts W m N A).card + (goodWordCuts W m N B).card ≤
      (allowedWordCuts W m N).card + (goodWordCuts W m N C).card := by
  classical
  let D := goodWordCuts W m N A \ goodWordCuts W m N C
  let E := allowedWordCuts W m N \ goodWordCuts W m N B
  let P : List α → Prop := fun q => MarkedEnd N q ∧ A q.toFinset ∧ ¬C q.toFinset
  have hex : ∀ u : ↥D, ∃ v : ↥E, PrefixRotation P u.val v.val := by
    rintro ⟨⟨l,k⟩,hu⟩
    obtain ⟨huA,huC⟩ := Finset.mem_sdiff.mp hu
    obtain ⟨hbase,hm,hA⟩ := Finset.mem_filter.mp huA
    obtain ⟨hlW,hkr⟩ := Finset.mem_product.mp hbase
    have hlm := hlen l hlW
    have hk : k ≤ l.length := by have := Finset.mem_range.mp hkr; omega
    have hC : ¬C (l.take k).toFinset := by
      intro hc
      exact huC (Finset.mem_filter.mpr ⟨hbase,hm,hc⟩)
    obtain ⟨r,x,y,hword,hcut,hr,hx,hBx⟩ :=
      marked_prefix_rotation_exists N A B C hglue l (hnodup l hlW) k hk hm hA hC
    let q := x++(r++y)
    have hqperm : q.Perm l := by
      rw [hword]
      simpa only [q,List.append_assoc] using
        (List.perm_append_comm (l₁:=x) (l₂:=r)).append_right y
    have hqW : q ∈ W := hperm l hlW q hqperm
    have hqLen : q.length=m := (List.Perm.length_eq hqperm).trans hlm
    have hxle : x.length ≤ m := by simp only [q,List.length_append] at hqLen; omega
    have htake : q.take x.length=x := List.take_left
    have hqBase : (q,x.length) ∈ W ×ˢ Finset.range (m+1) :=
      Finset.mem_product.mpr ⟨hqW,Finset.mem_range.mpr (by omega)⟩
    have hqAllowed : (q,x.length) ∈ allowedWordCuts W m N := by
      apply Finset.mem_filter.mpr
      refine ⟨hqBase,?_⟩
      rcases hx with hx | hx
      · exact Or.inl (hx ▸ rfl)
      · exact Or.inr (htake.symm ▸ hx)
    have hqNot : (q,x.length) ∉ goodWordCuts W m N B := by
      intro hh
      have hb := (Finset.mem_filter.mp hh).2.2
      rw [htake] at hb
      exact hBx hb
    refine ⟨⟨(q,x.length),Finset.mem_sdiff.mpr ⟨hqAllowed,hqNot⟩⟩,r,x,y,?_,rfl,hr⟩
    exact Prod.ext hword hcut
  choose f hf using hex
  have hi : Function.Injective f := by
    intro u u' he
    apply Subtype.ext
    apply prefixRotation_left_unique (hf u)
    rw [he]
    exact hf u'
  have hcard : D.card ≤ E.card := Finset.card_le_card_of_injective hi
  have hAC := Finset.card_sdiff_add_card_eq_card (goodWordCuts_mono W m N A C hCA)
  have hBE := Finset.card_sdiff_add_card_eq_card (goodWordCuts_subset_allowed W m N B)
  change (goodWordCuts W m N A \ goodWordCuts W m N C).card ≤
    (allowedWordCuts W m N \ goodWordCuts W m N B).card at hcard
  omega

end Erdos548
