import Init

-- Exact rational certificate: (1+1/14+4/279)/(2*(56/81)) < 4/5.
-- The positive denominators are justified in PROOF.md; this is only its integer sign.
theorem gamma_coarse_price : 5 * (4241 * 81) < 4 * (3906 * 112) := by decide

#print axioms gamma_coarse_price
