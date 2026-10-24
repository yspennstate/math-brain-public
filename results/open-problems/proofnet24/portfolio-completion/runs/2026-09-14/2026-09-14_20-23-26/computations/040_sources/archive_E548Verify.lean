import Bench.E548.Induction

/-!
Final verification of the Erdos 548 claim.
1. `#print axioms` must show ONLY propext, Classical.choice, Quot.sound.
   Any `sorryAx` means the proof is incomplete.
2. The `example` below restates the BENCHMARK statement verbatim (copied from
   Bench/E548.lean) and discharges it with the file's theorem. If the file's
   theorem were weaker or differently typed, this would not typecheck.
-/

#print axioms Erdos548.erdos_548

example :
    ∀ (n k : ℕ), k + 1 ≤ n → ∀ G : SimpleGraph (Fin n),
      ((k : ℚ) - 1) / 2 * n + 1 ≤ (G.edgeSet.ncard : ℚ) →
        ∀ T : SimpleGraph (Fin (k + 1)), T.IsTree → T.IsContained G :=
  Erdos548.erdos_548
