import Bench.E548.Involution
set_option autoImplicit true
set_option relaxedAutoImplicit true
set_option maxHeartbeats 4000000

open SimpleGraph

/- Rooted graph copies in permutation-word prefixes, and a verified leaf-root
extension by an involution on the full words. -/
open SimpleGraph
namespace Erdos548

/-- A rooted copy supported on the root image and the displayed outer set. -/
def RootedWordFamily {U V : Type*} [DecidableEq V]
    (S : SimpleGraph U) (r : U) (G : SimpleGraph V) (b : V) (X : Finset V) : Prop :=
  ∃ f : S.Copy G, f r=b ∧ ∀ x, f x ∈ insert b X

noncomputable def rootedWordCount {U V : Type*} [DecidableEq V]
    (S : SimpleGraph U) (r : U) (G : SimpleGraph V) (l₀ : List V) : ℕ :=
  fullWordCount l₀ G.Adj (RootedWordFamily S r G)

lemma rootedWordFamily_mono {U V : Type*} [DecidableEq V]
    (S : SimpleGraph U) (r : U) (G : SimpleGraph V) (b : V) {X Y : Finset V}
    (hXY : X ⊆ Y) : RootedWordFamily S r G b X → RootedWordFamily S r G b Y := by
  rintro ⟨f,hfr,hspan⟩
  exact ⟨f,hfr,fun x => (Finset.insert_subset_insert _ hXY) (hspan x)⟩

lemma rooted_word_leaf_move_step {U V : Type*} [DecidableEq V]
    (S : SimpleGraph U) (r : U) (G : SimpleGraph V) (l : List V) (hl : l.Nodup)
    (k : ℕ) (hk : k<l.length)
    (hs : FullWordQualifies G.Adj (RootedWordFamily S r G) l k)
    (j : ℕ) (hjk : j<k)
    (hj : FullWordQualifies G.Adj (RootedWordFamily S r G) l j) :
    FullWordQualifies G.Adj (RootedWordFamily (attachLeaves S r 1) (Sum.inr 0) G)
      (reverseWordAt l (k+1)) k := by
  classical
  obtain ⟨b,q,rfl,hm,_⟩ := hs
  have hkq : k ≤ q.length := by simpa only [List.length_cons,Nat.lt_add_one_iff] using hk
  have hj' := (fullWordQualifies_cons G.Adj (RootedWordFamily S r G) b q j).mp hj
  obtain ⟨f,hfr,hspan⟩ := hj'.2
  obtain ⟨w,hw,hbw⟩ := hm
  obtain ⟨p,hp⟩ := List.getLast?_eq_some_iff.mp hw
  let z := q.drop k
  have hq : q=p++w::z := by
    have he := List.take_append_drop k q
    rw [hp] at he
    simpa only [List.append_assoc,List.singleton_append] using he.symm
  have hpk : p.length+1=k := by
    have he := congrArg List.length hp
    simp only [List.length_take,List.length_append,List.length_singleton] at he
    omega
  have hjp : j ≤ p.length := by omega
  have htakej : q.take j=p.take j := by
    rw [hq,List.take_append_of_le_length hjp]
  have hnq : q.Nodup := (List.nodup_cons.mp hl).2
  have hnd : (p++w::z).Nodup := hq ▸ hnq
  have hwP : w ∉ p := by
    intro hh
    exact (List.disjoint_left.mp hnd.disjoint) hh List.mem_cons_self
  have hfree : w ∉ Set.range f := by
    rintro ⟨x,hx⟩
    have hh := hspan x
    rw [hx] at hh
    rcases Finset.mem_insert.mp hh with he | he
    · exact hbw.ne he.symm
    · rw [htakej] at he
      exact hwP (List.mem_of_mem_take (List.mem_toFinset.mp he))
  obtain ⟨F,hF,hFw⟩ := attach_single_leaf_copy S G r f w (by rw [hfr]; exact hbw) hfree
  have hrev : reverseWordAt (b::q) (k+1)=w::(p.reverse++b::z.reverse) := by
    rw [hq,← hpk]
    simpa only [Nat.add_assoc] using reverseWordAt_decomposition b w p z
  have hnewtake : (p.reverse++b::z.reverse).take k=p.reverse++[b] := by
    have he : p.reverse++b::z.reverse=(p.reverse++[b])++z.reverse := by
      simp only [List.append_assoc,List.singleton_append]
    have hlen : (p.reverse++[b]).length=k := by
      simp only [List.length_append,List.length_reverse,List.length_singleton]
      exact hpk
    rw [he,← hlen,List.take_left]
  rw [hrev]
  apply (fullWordQualifies_cons G.Adj _ _ _ _).mpr
  constructor
  · rw [hnewtake]
    exact ⟨b,List.getLast?_concat,hbw.symm⟩
  · refine ⟨F,hFw,?_⟩
    rintro (x | x)
    · rw [hF x,hnewtake]
      apply Finset.mem_insert_of_mem
      have hh := hspan x
      rcases Finset.mem_insert.mp hh with hx | hx
      · rw [hx]
        exact List.mem_toFinset.mpr (List.mem_append_right _ (List.mem_singleton_self _))
      · rw [htakej] at hx
        apply List.mem_toFinset.mpr
        apply List.mem_append_left
        exact List.mem_reverse.mpr (List.mem_of_mem_take (List.mem_toFinset.mp hx))
    · have hx : x=0 := Subsingleton.elim _ _
      subst x
      rw [hFw]
      exact Finset.mem_insert_self _ _

lemma rooted_word_leaf_move_count {U V : Type*} [DecidableEq V]
    (S : SimpleGraph U) (r : U) (G : SimpleGraph V) (l₀ : List V) (hl : l₀.Nodup) :
    rootedWordCount S r G l₀ ≤
      rootedWordCount (attachLeaves S r 1) (Sum.inr 0) G l₀ + (permutationWords l₀).card := by
  apply full_word_transfer_count
  intro l hlp k hk hs j hjk hj
  exact rooted_word_leaf_move_step S r G l (hlp.nodup_iff.mpr hl) k
    (by rwa [hlp.length_eq]) hs j hjk hj

end Erdos548

/- Rooted copies on two branches meeting at one root, and the corresponding
exact permutation-word counting inequality. -/
open SimpleGraph
namespace Erdos548

lemma rootedWordFamily_iso_iff {U W V : Type*} [DecidableEq V]
    {S : SimpleGraph U} {T : SimpleGraph W} (e : S ≃g T) (r : U)
    (G : SimpleGraph V) (b : V) (X : Finset V) :
    RootedWordFamily T (e r) G b X ↔ RootedWordFamily S r G b X := by
  constructor
  · rintro ⟨f,hfr,hspan⟩
    exact ⟨f.comp e.toCopy,hfr,fun x => hspan (e x)⟩
  · rintro ⟨f,hfr,hspan⟩
    refine ⟨f.comp e.symm.toCopy,?_,fun x => hspan (e.symm x)⟩
    simpa using hfr

lemma rootedWordCount_iso {U W V : Type*} [DecidableEq V]
    {S : SimpleGraph U} {T : SimpleGraph W} (e : S ≃g T) (r : U)
    (G : SimpleGraph V) (l₀ : List V) :
    rootedWordCount T (e r) G l₀=rootedWordCount S r G l₀ := by
  have he : RootedWordFamily T (e r) G=RootedWordFamily S r G := by
    funext b X
    exact propext (rootedWordFamily_iso_iff e r G b X)
  unfold rootedWordCount
  rw [he]

lemma rootedWordFamily_restrict {U V : Type*} [DecidableEq V]
    (T : SimpleGraph U) (G : SimpleGraph V) (A : Set U) (r : U) (hr : r ∈ A)
    (b : V) (X : Finset V) : RootedWordFamily T r G b X →
      RootedWordFamily (T.induce A) ⟨r,hr⟩ G b X := by
  rintro ⟨f,hfr,hspan⟩
  exact ⟨f.comp (Copy.induce T A),hfr,fun x => hspan x.val⟩

/-- Two copies agree at the root. Disjoint outer supporting sets ensure that
no other images collide. -/
lemma rootedWordFamily_glue {U V : Type*} [DecidableEq V]
    (T : SimpleGraph U) (G : SimpleGraph V) (A : Set U) (r : U) (hr : r ∈ A)
    (hsep : ∀ x ∈ A, ∀ y ∉ A, T.Adj x y → x=r)
    (b : V) (R X : Finset V) (hd : Disjoint R X)
    (hf : RootedWordFamily (T.induce A) ⟨r,hr⟩ G b R)
    (hg : RootedWordFamily (T.induce (Aᶜ ∪ {r})) ⟨r,Or.inr rfl⟩ G b X) :
    RootedWordFamily T r G b (R ∪ X) := by
  classical
  obtain ⟨f,hfr,hfspan⟩ := hf
  obtain ⟨g,hgr,hgspan⟩ := hg
  let F : U → V := fun x => if hx : x ∈ A then f ⟨x,hx⟩ else g ⟨x,Or.inl hx⟩
  have hcross : ∀ x : A, ∀ y : (Aᶜ ∪ {r} : Set U), y.val ∉ A → f x ≠ g y := by
    intro x y hy he
    have hgneq : g y ≠ b := by
      intro hb
      have hy' : y=⟨r,Or.inr rfl⟩ := g.injective (hb.trans hgr.symm)
      exact hy (by simpa only [hy'] using hr)
    have hfR : f x ∈ R := (Finset.mem_insert.mp (hfspan x)).resolve_left (fun hh => hgneq (he.symm.trans hh))
    have hgX : g y ∈ X := (Finset.mem_insert.mp (hgspan y)).resolve_left hgneq
    exact Finset.disjoint_left.mp hd hfR (he.symm ▸ hgX)
  have hmap : ∀ {x y}, T.Adj x y → G.Adj (F x) (F y) := by
    intro x y hxy
    by_cases hx : x ∈ A <;> by_cases hy : y ∈ A
    · simpa only [F,dif_pos hx,dif_pos hy] using
        (show G.Adj (f ⟨x,hx⟩) (f ⟨y,hy⟩) from f.toHom.map_adj hxy)
    · have hxr := hsep x hx y hy hxy
      subst x
      have he := g.toHom.map_adj (show (T.induce (Aᶜ ∪ {r})).Adj
        ⟨r,Or.inr rfl⟩ ⟨y,Or.inl hy⟩ from hxy)
      change G.Adj (g ⟨r,Or.inr rfl⟩) (g ⟨y,Or.inl hy⟩) at he
      simpa only [F,dif_pos hr,dif_neg hy,hfr,hgr] using he
    · have hyr := hsep y hy x hx hxy.symm
      subst y
      have he := g.toHom.map_adj (show (T.induce (Aᶜ ∪ {r})).Adj
        ⟨x,Or.inl hx⟩ ⟨r,Or.inr rfl⟩ from hxy)
      change G.Adj (g ⟨x,Or.inl hx⟩) (g ⟨r,Or.inr rfl⟩) at he
      simpa only [F,dif_neg hx,dif_pos hr,hfr,hgr] using he
    · simpa only [F,dif_neg hx,dif_neg hy] using
        (show G.Adj (g ⟨x,Or.inl hx⟩) (g ⟨y,Or.inl hy⟩) from g.toHom.map_adj hxy)
  have hinj : Function.Injective F := by
    intro x y he
    by_cases hx : x ∈ A <;> by_cases hy : y ∈ A
    · have he' : f ⟨x,hx⟩=f ⟨y,hy⟩ := by simpa only [F,dif_pos hx,dif_pos hy] using he
      exact congrArg Subtype.val (f.injective he')
    · exact (hcross ⟨x,hx⟩ ⟨y,Or.inl hy⟩ hy (by simpa only [F,dif_pos hx,dif_neg hy] using he)).elim
    · exact (hcross ⟨y,hy⟩ ⟨x,Or.inl hx⟩ hx (by simpa only [F,dif_neg hx,dif_pos hy] using he.symm)).elim
    · have he' : g ⟨x,Or.inl hx⟩=g ⟨y,Or.inl hy⟩ := by simpa only [F,dif_neg hx,dif_neg hy] using he
      exact congrArg Subtype.val (g.injective he')
  refine ⟨⟨⟨F,hmap⟩,hinj⟩,?_,?_⟩
  · change F r = b
    simpa only [F,dif_pos hr] using hfr
  · intro x
    by_cases hx : x ∈ A
    · change F x ∈ _
      rw [show F x=f ⟨x,hx⟩ by simp only [F,dif_pos hx]]
      exact Finset.insert_subset_insert b Finset.subset_union_left (hfspan ⟨x,hx⟩)
    · change F x ∈ _
      rw [show F x=g ⟨x,Or.inl hx⟩ by simp only [F,dif_neg hx]]
      exact Finset.insert_subset_insert b Finset.subset_union_right (hgspan ⟨x,Or.inl hx⟩)

lemma rooted_word_branch_gluing_count {U V : Type*} [DecidableEq V]
    (T : SimpleGraph U) (G : SimpleGraph V) (A : Set U) (r : U) (hr : r ∈ A)
    (hsep : ∀ x ∈ A, ∀ y ∉ A, T.Adj x y → x=r)
    (l₀ : List V) (hl : l₀.Nodup) (hne : l₀ ≠ []) :
    rootedWordCount (T.induce A) ⟨r,hr⟩ G l₀ +
      rootedWordCount (T.induce (Aᶜ ∪ {r})) ⟨r,Or.inr rfl⟩ G l₀ ≤
      fullWordCount l₀ G.Adj (fun _ _ => True)+(permutationWords l₀).card+rootedWordCount T r G l₀ := by
  apply full_word_gluing_count l₀ hl hne
  · exact rootedWordFamily_restrict T G A r hr
  · exact rootedWordFamily_glue T G A r hr hsep

end Erdos548
