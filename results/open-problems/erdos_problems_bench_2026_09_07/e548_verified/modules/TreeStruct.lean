import Bench.E548.Rooted
set_option autoImplicit true
set_option relaxedAutoImplicit true
set_option maxHeartbeats 4000000

open SimpleGraph

namespace Erdos548

lemma tree_edge_partition {U : Type} (T : SimpleGraph U) (hT : T.IsTree)
    (r s : U) (hrs : T.Adj r s) :
    ∃ A : Set U, r ∈ A ∧ s ∉ A ∧ (T.induce A).IsTree ∧ (T.induce Aᶜ).IsTree ∧
      ∀ x ∈ A, ∀ y ∉ A, T.Adj x y → x=r ∧ y=s := by
  classical
  let D := T \ fromEdgeSet {s(r,s)}
  have hno : ¬D.Reachable r s := by
    have hbr := isBridge_iff.mp ((isAcyclic_iff_forall_adj_isBridge.mp hT.isAcyclic) hrs)
    simpa only [D,SimpleGraph.deleteEdges] using hbr
  have hdeleted : ∀ {x y}, T.Adj x y → ¬D.Adj x y →
      (x=r ∧ y=s) ∨ (x=s ∧ y=r) := by
    intro x y hxy hn
    have he : s(x,y)=s(r,s) := by
      by_contra he
      apply hn
      exact ⟨hxy,by simp [fromEdgeSet_adj,he]⟩
    exact Sym2.eq_iff.mp he
  have hwalk : ∀ {x y} (p : T.Walk x y),
      (D.Reachable r y ∨ D.Reachable s y) → (D.Reachable r x ∨ D.Reachable s x) := by
    intro x y p
    induction p with
    | nil => exact fun h => h
    | @cons x y z hxy p ih =>
      intro h
      have hy := ih h
      by_cases he : D.Adj x y
      · exact hy.elim (fun h => Or.inl (h.trans he.symm.reachable))
          (fun h => Or.inr (h.trans he.symm.reachable))
      · rcases hdeleted hxy he with ⟨rfl,_⟩ | ⟨rfl,_⟩
        · exact Or.inl Reachable.rfl
        · exact Or.inr Reachable.rfl
  have hcover : ∀ x, D.Reachable r x ∨ D.Reachable s x := by
    intro x
    obtain ⟨p⟩ := hT.isConnected.preconnected x r
    exact hwalk p (Or.inl Reachable.rfl)
  let A := (D.connectedComponentMk r).supp
  have hmem : ∀ x, x ∈ A ↔ D.Reachable r x := by
    intro x
    simp only [A,ConnectedComponent.mem_supp_iff,ConnectedComponent.eq,D.reachable_comm]
  have hrA : r ∈ A := (hmem r).mpr Reachable.rfl
  have hsA : s ∉ A := fun h => hno ((hmem s).mp h)
  have hAc : Aᶜ=(D.connectedComponentMk s).supp := by
    ext x
    simp only [Set.mem_compl_iff,ConnectedComponent.mem_supp_iff,ConnectedComponent.eq]
    constructor
    · intro hx
      exact ((hcover x).resolve_left (fun h => hx ((hmem x).mpr h))).symm
    · intro hx hxa
      exact hno (((hmem x).mp hxa).trans hx)
  have hAconn : (T.induce A).Connected :=
    Connected.mono (show D.induce A ≤ T.induce A from fun _ _ h => h.1)
      (D.connectedComponentMk r).connected_toSimpleGraph
  have hAcconn : (T.induce Aᶜ).Connected := by
    rw [hAc]
    exact Connected.mono (show D.induce (D.connectedComponentMk s).supp ≤
      T.induce (D.connectedComponentMk s).supp from fun _ _ h => h.1)
      (D.connectedComponentMk s).connected_toSimpleGraph
  refine ⟨A,hrA,hsA,⟨hAconn,hT.IsAcyclic.induce A⟩,
    ⟨hAcconn,hT.IsAcyclic.induce Aᶜ⟩,?_⟩
  intro x hx y hy hxy
  have hn : ¬D.Adj x y := by
    intro h
    exact hy ((hmem y).mpr (((hmem x).mp hx).trans h.reachable))
  rcases hdeleted hxy hn with h | ⟨rfl,rfl⟩
  · exact h
  · exact (hsA hx).elim

end Erdos548

/- A nonleaf root splits a finite tree into two smaller rooted trees. -/
open SimpleGraph
namespace Erdos548

lemma tree_root_partition {U : Type} [Finite U] (T : SimpleGraph U) (hT : T.IsTree)
    (r s z : U) (hrs : T.Adj r s) (hrz : T.Adj r z) (hsz : s ≠ z) :
    ∃ A : Set U, ∃ _hr : r ∈ A,
      (T.induce A).IsTree ∧ (T.induce (Aᶜ ∪ {r})).IsTree ∧
      2 ≤ Nat.card A ∧ 2 ≤ Nat.card (Aᶜ ∪ {r} : Set U) ∧
      Nat.card A < Nat.card U ∧ Nat.card (Aᶜ ∪ {r} : Set U) < Nat.card U ∧
      Nat.card A + Nat.card (Aᶜ ∪ {r} : Set U) = Nat.card U + 1 ∧
      ∀ x ∈ A, ∀ y ∉ A, T.Adj x y → x=r := by
  classical
  obtain ⟨A,hr,hs,hA,hAc,hcut⟩ := tree_edge_partition T hT r s hrs
  have hz : z ∈ A := by
    by_contra hz
    exact hsz (hcut r hr z hz hrz).2.symm
  have hB : (T.induce (Aᶜ ∪ {r})).IsTree := by
    exact ⟨connected_induce_union hAc.isConnected.preconnected
      Preconnected.of_subsingleton hs (Set.mem_singleton r) hrs.symm,
      hT.IsAcyclic.induce _⟩
  have hA2 : 2 ≤ A.ncard := by
    have hh : ({r,z} : Set U) ⊆ A := by simpa only [Set.insert_subset_iff,Set.singleton_subset_iff] using And.intro hr hz
    simpa only [Set.ncard_pair hrz.ne] using Set.ncard_le_ncard hh
  have hB2 : 2 ≤ (Aᶜ ∪ {r}).ncard := by
    have hh : ({s,r} : Set U) ⊆ Aᶜ ∪ {r} := by
      simp only [Set.insert_subset_iff,Set.singleton_subset_iff,Set.mem_union,Set.mem_compl_iff,Set.mem_singleton_iff]
      exact ⟨Or.inl hs,Or.inr trivial⟩
    simpa only [Set.ncard_pair hrs.ne.symm] using Set.ncard_le_ncard hh
  have hAlt : A.ncard < Nat.card U := Set.ncard_lt_card (by
    intro he
    exact hs (he ▸ Set.mem_univ s))
  have hBlt : (Aᶜ ∪ {r}).ncard < Nat.card U := Set.ncard_lt_card (by
    intro he
    have hm : z ∈ Aᶜ ∪ {r} := he ▸ Set.mem_univ z
    exact hm.elim (fun hh => hh hz) hrz.ne.symm)
  have hcard : A.ncard + (Aᶜ ∪ {r}).ncard = Nat.card U+1 := by
    rw [Set.union_singleton,Set.ncard_insert_of_notMem (by simpa using hr)]
    rw [← Nat.add_assoc,Set.ncard_add_ncard_compl]
  exact ⟨A,hr,hA,hB,hA2,hB2,hAlt,hBlt,hcard,fun x hx y hy hxy => (hcut x hx y hy hxy).1⟩

end Erdos548

/- Every marked word cut supports any rooted graph of order two. -/
open SimpleGraph
namespace Erdos548

lemma rootedWordFamily_of_card_two {U V : Type*} [Fintype U] [DecidableEq V]
    (T : SimpleGraph U) (r : U) (ht : Fintype.card U = 2)
    (G : SimpleGraph V) (b w : V) (hbw : G.Adj b w) (X : Finset V) (hw : w ∈ X) :
    RootedWordFamily T r G b X := by
  classical
  have hc : Fintype.card ({r}ᶜ : Set U) ≤ 1 := by
    rw [Fintype.card_compl_set,ht]
    simp
  haveI : Subsingleton ({r}ᶜ : Set U) := Fintype.card_le_one_iff_subsingleton.mp hc
  have hnonroot : ∀ x y : U, x ≠ r → y ≠ r → x=y := by
    intro x y hx hy
    exact congrArg Subtype.val (Subsingleton.elim (⟨x,hx⟩ : ({r}ᶜ : Set U)) ⟨y,hy⟩)
  let F : U → V := fun x => if x=r then b else w
  have hinj : Function.Injective F := by
    intro x y he
    by_cases hx : x=r <;> by_cases hy : y=r
    · exact hx.trans hy.symm
    · exact (hbw.ne (by simpa only [F,if_pos hx,if_neg hy] using he)).elim
    · exact (hbw.ne.symm (by simpa only [F,if_neg hx,if_pos hy] using he)).elim
    · exact hnonroot x y hx hy
  have hadj : ∀ {x y}, T.Adj x y → G.Adj (F x) (F y) := by
    intro x y hxy
    by_cases hx : x=r <;> by_cases hy : y=r
    · exact (hxy.ne (hx.trans hy.symm)).elim
    · simpa only [F,if_pos hx,if_neg hy] using hbw
    · simpa only [F,if_neg hx,if_pos hy] using hbw.symm
    · exact (hxy.ne (hnonroot x y hx hy)).elim
  refine ⟨⟨⟨F,hadj⟩,hinj⟩,?_,?_⟩
  · change F r=b
    simp only [F,if_pos rfl]
  · intro x
    change F x ∈ _
    by_cases hx : x=r
    · simp only [F,if_pos hx,Finset.mem_insert_self]
    · simpa only [F,if_neg hx] using Finset.mem_insert_of_mem hw

lemma rooted_word_count_base {U V : Type*} [Fintype U] [DecidableEq V]
    (T : SimpleGraph U) (r : U) (ht : Fintype.card U = 2)
    (G : SimpleGraph V) (l₀ : List V) :
    fullWordCount l₀ G.Adj (fun _ _ => True) ≤ rootedWordCount T r G l₀ := by
  classical
  apply Finset.card_le_card
  intro p hp
  obtain ⟨hl,hk,b,q,he,hm,_⟩ := (mem_fullGoodWordCuts _ _ _ _ _).mp hp
  obtain ⟨w,hw,hbw⟩ := hm
  refine (mem_fullGoodWordCuts _ _ _ _ _).mpr ⟨hl,hk,b,q,he,⟨w,hw,hbw⟩,?_⟩
  apply rootedWordFamily_of_card_two T r ht G b w hbw
  exact List.mem_toFinset.mpr (List.mem_of_mem_getLast? (by simpa only [hw] using (show w ∈ some w from rfl)))

end Erdos548

namespace Erdos548

noncomputable def leafRestoreIso {U : Type} (T : SimpleGraph U) (l p : U)
    (hlp : T.Adj l p) (honly : ∀ x, T.Adj l x → x = p) :
    attachLeaves (T.induce {l}ᶜ) ⟨p,hlp.ne.symm⟩ 1 ≃g T := by
  classical
  let f : ({l}ᶜ : Set U) ⊕ Fin 1 → U := Sum.elim Subtype.val (fun _ => l)
  let g : U → ({l}ᶜ : Set U) ⊕ Fin 1 := fun x => if hx : x = l then Sum.inr 0 else Sum.inl ⟨x,hx⟩
  have hfg : Function.RightInverse g f := by
    intro x
    by_cases hx : x = l <;> simp [f,g,hx]
  have hgf : Function.LeftInverse g f := by
    rintro (x | x)
    · have hx : x.val ≠ l := x.property
      simp only [f,Sum.elim_inl,g,dif_neg hx,Subtype.coe_eta]
    · have hx : x = 0 := Subsingleton.elim _ _
      subst x
      simp only [f,Sum.elim_inr,g,dif_pos rfl]
  refine ⟨⟨f,g,hgf,hfg⟩,?_⟩
  rintro (x | x) (y | y)
  · rfl
  · change T.Adj x.val l ↔ x = ⟨p,hlp.ne.symm⟩
    constructor
    · exact fun h => Subtype.ext (honly x.val h.symm)
    · intro h
      rw [h]
      exact hlp.symm
  · change T.Adj l y.val ↔ y = ⟨p,hlp.ne.symm⟩
    constructor
    · exact fun h => Subtype.ext (honly y.val h)
    · intro h
      rw [h]
      exact hlp
  · change T.Adj l l ↔ False
    simp

@[simp] lemma leafRestoreIso_inl {U : Type} (T : SimpleGraph U) (l p : U)
    (hlp : T.Adj l p) (honly : ∀ x, T.Adj l x → x = p) (x : ({l}ᶜ : Set U)) :
    leafRestoreIso T l p hlp honly (Sum.inl x) = x.val := rfl

@[simp] lemma leafRestoreIso_inr {U : Type} (T : SimpleGraph U) (l p : U)
    (hlp : T.Adj l p) (honly : ∀ x, T.Adj l x → x = p) :
    leafRestoreIso T l p hlp honly (Sum.inr 0) = l := rfl

end Erdos548
