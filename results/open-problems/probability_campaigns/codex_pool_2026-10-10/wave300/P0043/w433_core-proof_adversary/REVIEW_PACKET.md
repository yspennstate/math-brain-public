# P0043 review packet — w433 to w434

No proof of the full critical-percolation target is claimed. Current openness is UNKNOWN because a fresh public full-scope formalization claim has not been reproduced. Review does not require any test bank.

## Independent phase

ATTEMPT.md sections 1-5 were saved before reading the paired prover's proof. Please check: the complete p_c<1 scope correction; the conditional-thinning proof that every hypothetical critical infinite component has p_c(H)=1; the tree-in-lattice path-count obstruction; and the local-minimum site field, its exact one-site probability, finite dependence, and bounded component argument.

## Paired-proof verdict

w432/ATTEMPT.md L02, L03, L04, L05 and L06 survive this adversarial read as reductions and special cases. Its unresolved G01 is uniform critical-window pivotal control on the remaining quasi-transitive graphs. The equivalence in L03 must remain a reduction, and the sufficient L^r bound is not proved generally. The nonsymmetric tree is a valid exception after quasi-transitivity is removed; it does not refute P0043. The proof uses the appropriate independent offspring law and does not multiply unproved conditional bounds.

## New result requiring your independent check

ATTEMPT.md section 8 tightens the regular-tree derivative bound from D*(1+2/c_b) to D/c_b, by retaining the common s_m factor in the open-pivotal estimate. It holds throughout [0,1/(D-1)]. At D=3 the bound is 12 instead of 27. Please check the Taylor bound, reciprocal iteration, open-pivotal identity, root derivative, and p=0 continuity. All are written explicitly. It is only a special-case control and has no novelty claim.

## Evidence and landing

CLAIMS.jsonl records exact assumptions, proof or obstruction, source, pending independent reviewer, and remaining gap. MEASUREMENTS.json is produced by `python -X utf8 ~/brain_workers/w433/check_obstructions.py` under COMPUTE_GATE.json. Arithmetic checks do not replace the written proofs.

Draft entries will be concepts with proof_text=null until independently reviewed; no new theorem is submitted to the live store. SOURCE_STATUS.json and FORMAL_CHECK_RECEIPT.json distinguish source retrieval, claimed formalization, and actual verification. Do not treat the comparator challenge's intentional `sorry` as proof, or as a refutation of the separately supplied solution.

The local hook proposal and its unified diff are for reviewer landing outside w433's write scope. Peer messages are restricted to w432/w434. Direct mesh send reached w432; w434 was not registered at the first attempt. The local packet remains available regardless of messaging.

NEXT: Independently check Sections 2, 5 and 8, then decide which draft concepts to approve for integration; keep full-target G01 and iid robustness unproved.
