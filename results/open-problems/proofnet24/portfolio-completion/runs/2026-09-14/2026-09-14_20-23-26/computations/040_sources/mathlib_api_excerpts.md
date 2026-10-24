# Exact Mathlib API excerpts

Revision: 8f9d9cff6bd728b17a24e163c9402775d9e6a365 (v4.28.0).

## Basic.lean

Blob: b4a3bb880efeea0a75a112e95d31fce9c59ea203
Source: https://github.com/leanprover-community/mathlib4/blob/8f9d9cff6bd728b17a24e163c9402775d9e6a365/Mathlib/Combinatorics/SimpleGraph/Basic.lean

```lean
90: -/
91: @[ext, aesop safe constructors (rule_sets := [SimpleGraph])]
92: structure SimpleGraph (V : Type u) where
93:   /-- The adjacency relation of a simple graph. -/
94:   Adj : V → V → Prop
95:   symm : Symmetric Adj := by aesop_graph
96:   loopless : Std.Irrefl Adj := by aesop_graph
97: 
98: initialize_simps_projections SimpleGraph (Adj → adj)
99: 
100: /-- Constructor for simple graphs using a symmetric irreflexive Boolean function. -/
101: @[simps]
102: def SimpleGraph.mk' {V : Type u} :
```

## Copy.lean

Blob: 68c75ab781e6e47003cb269244f5a3f645f99197
Source: https://github.com/leanprover-community/mathlib4/blob/8f9d9cff6bd728b17a24e163c9402775d9e6a365/Mathlib/Combinatorics/SimpleGraph/Copy.lean

```lean
83: 
84: /-- The type of copies as a subtype of *injective* homomorphisms. -/
85: structure Copy (A : SimpleGraph α) (B : SimpleGraph β) where
86:   /-- A copy gives rise to a homomorphism. -/
87:   toHom : A →g B
88:   injective' : Injective toHom
89: 
90: /-- An injective homomorphism gives rise to a copy. -/
91: abbrev Hom.toCopy (f : A →g B) (h : Injective f) : Copy A B := .mk f h
92: 
93: /-- An embedding gives rise to a copy. -/
94: abbrev Embedding.toCopy (f : A ↪g B) : Copy A B := f.toHom.toCopy f.injective
95: 
235: 
236: This is equivalent to the existence of an isomorphism from `A` to a subgraph of `B`. -/
237: abbrev IsContained (A : SimpleGraph α) (B : SimpleGraph β) := Nonempty (Copy A B)
238: 
239: @[inherit_doc] scoped infixl:50 " ⊑ " => SimpleGraph.IsContained
240: 
241: /-- A simple graph contains itself. -/
242: @[refl] protected theorem IsContained.refl (G : SimpleGraph V) : G ⊑ G := ⟨.id G⟩
243: 
244: protected theorem IsContained.rfl : G ⊑ G := IsContained.refl G
245: 
246: /-- A simple graph contains its subgraphs. -/
247: theorem IsContained.of_le (h : G₁ ≤ G₂) : G₁ ⊑ G₂ := ⟨.ofLE G₁ G₂ h⟩
```

## Acyclic.lean

Blob: c0e5dd07a404c01136e4e4d789d92157176fbbd5
Source: https://github.com/leanprover-community/mathlib4/blob/8f9d9cff6bd728b17a24e163c9402775d9e6a365/Mathlib/Combinatorics/SimpleGraph/Acyclic.lean

```lean
56: /-- A *tree* is a connected acyclic graph. -/
57: @[mk_iff]
58: structure IsTree : Prop where
59:   /-- Graph is connected. -/
60:   protected isConnected : G.Connected
61:   /-- Graph is acyclic. -/
62:   protected IsAcyclic : G.IsAcyclic
63: 
64: variable {G G'}
65: 
66: @[simp] lemma isAcyclic_bot : IsAcyclic (⊥ : SimpleGraph V) := fun _a _w hw ↦ hw.ne_bot rfl
67: 
68: /-- A graph that has an injective homomorphism to an acyclic graph is acyclic. -/
```

## Connectivity/Connected.lean

Blob: 87e75862e31ff02be535b1eb24297c340aaee0fe
Source: https://github.com/leanprover-community/mathlib4/blob/8f9d9cff6bd728b17a24e163c9402775d9e6a365/Mathlib/Combinatorics/SimpleGraph/Connectivity/Connected.lean

```lean
735:     Sym2.lift ⟨fun v w => ¬(G \ fromEdgeSet {e}).Reachable v w, by simp [reachable_comm]⟩ e
736: 
737: theorem isBridge_iff {u v : V} :
738:     G.IsBridge s(u, v) ↔ G.Adj u v ∧ ¬(G \ fromEdgeSet {s(u, v)}).Reachable u v := Iff.rfl
739: 
740: theorem reachable_delete_edges_iff_exists_walk {v w v' w' : V} :
741:     (G \ fromEdgeSet {s(v, w)}).Reachable v' w' ↔ ∃ p : G.Walk v' w', s(v, w) ∉ p.edges := by
742:   constructor
743:   · rintro ⟨p⟩
744:     use p.map (.ofLE (by simp))
745:     simp_rw [Walk.edges_map, List.mem_map, Hom.ofLE_apply, Sym2.map_id', id]
746:     rintro ⟨e, h, rfl⟩
747:     simpa using p.edges_subset_edgeSet h
```
