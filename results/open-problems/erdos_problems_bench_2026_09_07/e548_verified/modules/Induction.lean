import Bench.E548.TreeStruct
set_option autoImplicit true
set_option relaxedAutoImplicit true
set_option maxHeartbeats 4000000

open SimpleGraph

/- The rooted word-count bound for every finite tree. -/
open SimpleGraph
namespace Erdos548
set_option maxHeartbeats 1000000

lemma rooted_word_tree_bound_aux (t : ℕ) :
    ∀ (U V : Type) [Fintype U] [DecidableEq V]
      (T : SimpleGraph U) (r : U) (_hT : T.IsTree) (_ht : Fintype.card U=t) (_ht2 : 2 ≤ t)
      (G : SimpleGraph V) (l₀ : List V) (_hl : l₀.Nodup) (_hne : l₀ ≠ []),
      fullWordCount l₀ G.Adj (fun _ _ => True) ≤
        rootedWordCount T r G l₀ + (t-2)*(permutationWords l₀).card := by
  induction t using Nat.strong_induction_on with
  | h t ih =>
    intro U V _ _ T r hT ht ht2 G l₀ hl hne
    classical
    by_cases htbase : t=2
    · have hcard2 : Fintype.card U=2 := ht.trans htbase
      simpa only [htbase,Nat.sub_self,Nat.zero_mul,Nat.add_zero] using rooted_word_count_base T r hcard2 G l₀
    have ht3 : 3 ≤ t := by omega
    haveI : Nontrivial U := Fintype.one_lt_card_iff_nontrivial.mp (by omega)
    obtain ⟨s,hrs⟩ := hT.isConnected.preconnected.exists_adj_of_nontrivial r
    by_cases hleaf : ∀ z, T.Adj r z → z=s
    · have hdeg : T.degree r=1 := degree_eq_one_iff_existsUnique_adj.mpr ⟨s,hrs,hleaf⟩
      let A : Set U := {r}ᶜ
      let a : A := ⟨s,hrs.ne.symm⟩
      have hTA : (T.induce A).IsTree :=
        ⟨hT.isConnected.induce_compl_singleton_of_degree_eq_one hdeg,hT.IsAcyclic.induce A⟩
      have hcard : Fintype.card A=t-1 := by
        simp only [A,Fintype.card_compl_set,Fintype.card_unique,ht]
      have hsmall : Fintype.card A<t := by omega
      have htwo : 2 ≤ Fintype.card A := by omega
      have hbound := ih (Fintype.card A) hsmall A V (T.induce A) a hTA rfl htwo G l₀ hl hne
      have hmove := rooted_word_leaf_move_count (T.induce A) a G l₀ hl
      have hiso := rootedWordCount_iso (leafRestoreIso T r s hrs hleaf) (Sum.inr 0) G l₀
      rw [leafRestoreIso_inr] at hiso
      change rootedWordCount T r G l₀ = rootedWordCount (attachLeaves (T.induce A) a 1) (Sum.inr 0) G l₀ at hiso
      rw [← hiso] at hmove
      have hcoeff : Fintype.card A-2+1=t-2 := by omega
      have hcost := congrArg (fun j => j*(permutationWords l₀).card) hcoeff
      simp only [Nat.add_mul,Nat.one_mul] at hcost
      omega
    · push_neg at hleaf
      obtain ⟨z,hrz,hzs⟩ := hleaf
      obtain ⟨A,hr,hA,hB,hA2,hB2,hAlt,hBlt,hcard,hsep⟩ :=
        tree_root_partition T hT r s z hrs hrz hzs.symm
      simp only [Nat.card_eq_fintype_card,ht] at hAlt hBlt hcard
      simp only [Nat.card_eq_fintype_card] at hA2 hB2
      have hboundA := ih (Fintype.card A) hAlt A V (T.induce A) ⟨r,hr⟩ hA rfl hA2 G l₀ hl hne
      have hboundB := ih (Fintype.card (Aᶜ ∪ {r} : Set U)) hBlt (Aᶜ ∪ {r} : Set U) V
        (T.induce (Aᶜ ∪ {r})) ⟨r,Or.inr rfl⟩ hB rfl hB2 G l₀ hl hne
      have hglue := rooted_word_branch_gluing_count T G A r hr hsep l₀ hl hne
      have hcoeff : (Fintype.card A-2)+(Fintype.card (Aᶜ ∪ {r} : Set U)-2)+1=t-2 := by omega
      have hcost := congrArg (fun j => j*(permutationWords l₀).card) hcoeff
      simp only [Nat.add_mul,Nat.one_mul] at hcost
      omega

lemma rooted_word_tree_bound {U V : Type} [Fintype U] [DecidableEq V]
    (T : SimpleGraph U) (r : U) (hT : T.IsTree) (ht2 : 2 ≤ Fintype.card U)
    (G : SimpleGraph V) (l₀ : List V) (hl : l₀.Nodup) (hne : l₀ ≠ []) :
    fullWordCount l₀ G.Adj (fun _ _ => True) ≤
      rootedWordCount T r G l₀ + (Fintype.card U-2)*(permutationWords l₀).card :=
  rooted_word_tree_bound_aux (Fintype.card U) U V T r hT rfl ht2 G l₀ hl hne

end Erdos548

/- Exact host counts for a word containing every vertex once. -/
open SimpleGraph
namespace Erdos548

lemma full_word_base_count {V : Type*} [Fintype V] [DecidableEq V]
    (G : SimpleGraph V) (l₀ : List V) (hl : l₀.Nodup) (hall : ∀ b, b ∈ l₀) :
    fullWordCount l₀ G.Adj (fun _ _ => True) =
      (l₀.length-1).factorial * (2*G.edgeSet.ncard) := by
  classical
  have hset : l₀.toFinset=Finset.univ := by
    ext b
    simp only [List.mem_toFinset,Finset.mem_univ,iff_true]
    exact hall b
  have hfiber : ∀ b ∈ l₀.toFinset,
      (goodWordCuts (permutationWords (l₀.erase b)) (l₀.length-1) (G.Adj b) (fun _ => True)).card =
        (l₀.length-1).factorial * G.degree b := by
    intro b hb
    have hlen : ∀ q ∈ permutationWords (l₀.erase b), q.length=l₀.length-1 := by
      intro q hq
      rw [((mem_permutationWords _ _).mp hq).length_eq,List.length_erase_of_mem (hall b)]
    have hnodup : ∀ q ∈ permutationWords (l₀.erase b), q.Nodup := by
      intro q hq
      exact ((mem_permutationWords _ _).mp hq).nodup_iff.mpr (hl.erase b)
    rw [goodWordCuts_true_card _ _ _ hlen hnodup]
    have hterm : ∀ q ∈ permutationWords (l₀.erase b), (q.toFinset.filter (G.Adj b)).card=G.degree b := by
      intro q hq
      have hp : (b::q).Perm l₀ := List.cons_perm_iff_perm_erase.mpr
        ⟨hall b,(mem_permutationWords _ _).mp hq⟩
      have he : q.toFinset.filter (G.Adj b)=G.neighborFinset b := by
        ext v
        simp only [Finset.mem_filter,List.mem_toFinset,G.mem_neighborFinset]
        constructor
        · exact And.right
        · intro hv
          constructor
          · have hm : v ∈ b::q := hp.mem_iff.mpr (hall v)
            exact (List.mem_cons.mp hm).resolve_left (fun hh => hv.ne hh.symm)
          · exact hv
      rw [he,G.card_neighborFinset_eq_degree]
    rw [Finset.sum_congr rfl hterm]
    simp only [Finset.sum_const,nsmul_eq_mul,permutationWords_card _ (hl.erase b),
      List.length_erase_of_mem (hall b),Nat.cast_id]
  rw [fullWordCount_eq_sum,Finset.sum_congr rfl hfiber,← Finset.mul_sum,hset,
    G.sum_degrees_eq_twice_card_edges]
  congr 2
  rw [edgeFinset_card,← Nat.card_eq_fintype_card]
  rfl

lemma rooted_word_count_zero_of_not_contained {U V : Type*} [DecidableEq V]
    (T : SimpleGraph U) (r : U) (G : SimpleGraph V) (h : ¬T.IsContained G) (l₀ : List V) :
    rootedWordCount T r G l₀=0 := by
  classical
  apply Finset.card_eq_zero.mpr
  apply Finset.eq_empty_iff_forall_notMem.mpr
  rintro ⟨l,k⟩ hp
  obtain ⟨_,_,b,q,_,_,f,_,_⟩ := (mem_fullGoodWordCuts _ _ _ _ _).mp hp
  exact h ⟨f⟩

lemma tree_free_edge_bound {U V : Type} [Fintype U] [Fintype V]
    (T : SimpleGraph U) (hT : T.IsTree) (ht : 2 ≤ Fintype.card U)
    (G : SimpleGraph V) (hn : 0 < Fintype.card V) (hfree : ¬T.IsContained G) :
    2*G.edgeSet.ncard ≤ (Fintype.card U-2)*Fintype.card V := by
  classical
  let l₀ : List V := Finset.univ.toList
  have hl : l₀.Nodup := Finset.nodup_toList _
  have hlen : l₀.length=Fintype.card V := by simp only [l₀,Finset.length_toList,Finset.card_univ]
  have hne : l₀ ≠ [] := by
    intro he
    have : l₀.length=0 := by rw [he]; rfl
    omega
  have hall : ∀ b, b ∈ l₀ := by intro b; simp only [l₀,Finset.mem_toList,Finset.mem_univ]
  obtain ⟨r⟩ := hT.isConnected.nonempty
  have hb := rooted_word_tree_bound T r hT ht G l₀ hl hne
  rw [rooted_word_count_zero_of_not_contained T r G hfree l₀,Nat.zero_add,
    full_word_base_count G l₀ hl hall,permutationWords_card l₀ hl,hlen] at hb
  have hfact : (Fintype.card V).factorial=Fintype.card V*(Fintype.card V-1).factorial := by
    have he := Nat.factorial_succ (Fintype.card V-1)
    simpa only [Nat.sub_add_cancel hn] using he
  rw [hfact] at hb
  apply Nat.le_of_mul_le_mul_right (c := (Fintype.card V-1).factorial) _ (Nat.factorial_pos _)
  nlinarith only [hb]

end Erdos548

namespace Erdos548

/--
Let $n\geq k+1$. Every graph on $n$ vertices with at least $\frac{k-1}{2}n+1$ edges contains every tree on $k+1$ vertices.
-/
theorem erdos_548 :
    ∀ (n k : ℕ), k + 1 ≤ n → ∀ G : SimpleGraph (Fin n),
      ((k : ℚ) - 1) / 2 * n + 1 ≤ (G.edgeSet.ncard : ℚ) →
        ∀ T : SimpleGraph (Fin (k + 1)), T.IsTree → T.IsContained G := by
  intro n k hnk G hd T hT
  classical
  have hn : 0<n := by omega
  by_cases hk : k=0
  · subst k
    haveI : Subsingleton (Fin (0+1)) := by change Subsingleton (Fin 1); infer_instance
    let f : Fin (0+1) → Fin n := fun _ => ⟨0,hn⟩
    have hf : Function.Injective f := fun _ _ _ => Subsingleton.elim _ _
    have ha : ∀ {x y}, T.Adj x y → G.Adj (f x) (f y) := by
      intro x y hxy
      exact (hxy.ne (Subsingleton.elim _ _)).elim
    exact ⟨⟨⟨f,ha⟩,hf⟩⟩
  · by_contra hfree
    have hb := tree_free_edge_bound T hT (by simp only [Fintype.card_fin]; omega) G
      (by simpa only [Fintype.card_fin] using hn) hfree
    simp only [Fintype.card_fin] at hb
    have he : k+1-2=k-1 := by omega
    rw [he] at hb
    have hbq : (2:ℚ)*G.edgeSet.ncard ≤ ((k:ℚ)-1)*n := by
      have hh : (k:ℚ)-1=((k-1:ℕ):ℚ) := by
        rw [Nat.cast_sub (by omega)]; norm_num
      rw [hh]
      exact_mod_cast hb
    nlinarith

end Erdos548
