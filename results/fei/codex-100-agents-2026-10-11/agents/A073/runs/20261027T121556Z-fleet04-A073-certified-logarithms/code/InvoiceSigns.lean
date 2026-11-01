-- Concrete AND2 sign controls; no imports, no logarithm approximation.
theorem negative_neighbor : 27 * (50464827764806005:Nat) * (3*288230376151711744-4*50464827764806005)^2 < 25*(288230376151711744:Nat)^3 := by decide
theorem positive_neighbor : 25*(288230376151711744:Nat)^3 < 27 * (50464827764806006:Nat) * (3*288230376151711744-4*50464827764806006)^2 := by decide
#print axioms negative_neighbor
#print axioms positive_neighbor
