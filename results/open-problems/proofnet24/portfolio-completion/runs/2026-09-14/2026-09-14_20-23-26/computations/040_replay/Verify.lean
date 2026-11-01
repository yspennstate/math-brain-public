import E548

/- Independent replay surface. No local compilation occurred in worker 040.
The base module is the exact public source blob
393c2e60a872d00f4a9df6b40fbb2a518eff18dc at
tadamcz/erdos548@82ffb751f3d37768927df9239ed08439bbe0dd09.
-/ 

#print axioms Erdos548.rooted_word_tree_bound
#print axioms Erdos548.tree_free_edge_bound
#print axioms Erdos548.erdos_548

example :
    ∀ (n k : ℕ), k + 1 ≤ n → ∀ G : SimpleGraph (Fin n),
      ((k : ℚ) - 1) / 2 * n + 1 ≤ (G.edgeSet.ncard : ℚ) →
        ∀ T : SimpleGraph (Fin (k + 1)), T.IsTree → T.IsContained G :=
  Erdos548.erdos_548

namespace Erdos548

/-- The exact strict threshold for trees of order at least two.
For integer edge counts this includes the parity case omitted by
the benchmark's rational lower bound with an additional 1.
This corollary has NOT been compiled by worker 040. -/
theorem tree_contained_of_strict_edge_bound
    {U V : Type} [Fintype U] [Fintype V]
    (T : SimpleGraph U) (hT : T.IsTree) (ht : 2 ≤ Fintype.card U)
    (G : SimpleGraph V) (hn : 0 < Fintype.card V)
    (he : (Fintype.card U - 2) * Fintype.card V < 2 * G.edgeSet.ncard) :
    T.IsContained G := by
  classical
  by_contra hfree
  have hb := tree_free_edge_bound T hT ht G hn hfree
  exact (not_lt_of_ge hb) he

end Erdos548

#print axioms Erdos548.tree_contained_of_strict_edge_bound
