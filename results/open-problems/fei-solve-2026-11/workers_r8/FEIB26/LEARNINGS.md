# Local memory handoff

Status: verified mathematical derivation, with checked numerical witnesses; no novelty claim. The launching session may record this in the shared brain after review. This worker has not written outside its folder.

- FEIB26 found an explicit transitive, monotone function with minimum coordinate erasure/influence above 4.50504996749762. It is seven bottom-to-top gates N,M,N,M,N,M,N, where M is PM(K33) on nine edge variables and N=-M. It has 4,782,969 leaves. The finite value is enclosed by ninety-digit outward intervals in interval_witness.json. PM term incidence is explicitly isomorphic to the six-row/column DNF in pm_isomorphism.json.
- The period [N,M] has limiting G about 4.50501525844266655425; the ordinary PM9 self-tower has limit about 4.474150253077977. Finite G can exceed its limit.
- For unbalanced disjoint composition, empty-block contributions interfere as amplitudes. Use biased outer Fourier coefficients, then sample nonempty centered inner blocks. The exact normalized residual R=(E-Phi(c²,s²))/delta grows monotonically along towers, although G need not.
- PROOFS.md sections 4 and 6 give convergence for every fixed transitive base and an explicit finite-gate tail bound using O'Donnell–Tan's biased composition theorem. These depend on existing finite-gate FEI and do not prove a constant for all transitive functions.
- A balanced entropy-amplification seed need not be transitive. The supplied 18-variable record helper has influence types 1/256 and 57/256. Its computed H/(I-1) matches 6.5218457109230465; the transitive 9-variable host is unbalanced.
- Hod already documents that the displayed original O'Donnell–Tan six-variable base is biased. His balanced replacement reconstructs the 6.278 entropy amplification. Its minimum tower erasure ratio needs minimization over every leaf path; the DP here gives about 3.6848626341, less than every constant-coordinate-path limit.
- The exact size-biased deletion law and a rational-root obstruction to nontrivial product spectral laws are written in PROOFS.md. Neither settles general FEI. General transitive erasure remains open.

Evidence: REPORT.md, PROOFS.md, RESULTS.md, interval_witness.json, periodic_audit.json, pm_audit.json, pm_isomorphism.json, ot_tower_dp.json, verification.json.
Task: the author's 9 Nov 2026 22:20 ask, “solve the Fourier Entropy-Influence conjecture”; FEIB26.
