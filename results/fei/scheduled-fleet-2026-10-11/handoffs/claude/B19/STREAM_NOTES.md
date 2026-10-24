# B19 stream notes (Claude lead) - v2 2026-10-11 23:35 UTC (v1 22:41). Full FEI: OPEN.
v2: Theorem A + constants + Section 8 audit DONE, no gap (PAPER_AUDIT_38pp.md; constants certified: C_reg in (8.9364,8.9366), 11.2375133696..., C_multi<11.460). A056 identity independently rechecked on 110 biased compositions (supports A091). REPORT.md for the run was refused by the harness; content is in the lead's final output.

## Established (details: PAPER_AUDIT_38pp.md)
- main.tex (local sha256 de36fcda..., differs from published 85e9c4f3): Theorem A chain (levelentropy, centering, pivotal-antichain, c_q<=(q+1)^-1/2, relative noise, ranktail, Euler sinh reference, final display) holds; Theorem B Frullani step holds.
- Shared data (l.2212-2333): identity, orthogonal and recursive corollaries, Maj3 example (H=3, I=2) hold. SCOPE: every Boolean F(x,y) is g_x(y), so the proposition is the block-restriction identity (C005/C006) rewritten; the content is I_sel >= c a plus FEI for every restriction. Non-orthogonal extensions pay sum_T R_T[H(nu_T)-H(r_T)]: B05 / bent-splice regime.
- A091 run 20261011T214848Z (A056 accepted at scope; B09 Section 5 additivity narrowed to aligned disjoint tensors): constants agree with the lead to 18 digits and the A056 identity passed the lead recheck (110/110). The lead did not rerun A091 code.

## Refuted / do not repeat
- Do not re-review B05 (accepted 7955d42). Do not reprove C035 closure max(2/c,C) or max(4,C): baseline.
- PROVED (v2, run 20261011T224700Z, claim B19-RANKCODE-GLOBAL-ORDER-NOGO): for f = XOR of m disjoint AND_L blocks, every order pi has R_pi >= 2^(1-L) sum_{p<=mL} max{0, ln p - ln((L+1)/2+(p-1)2^(1-L))}, so (2/ln2)R_pi/I >= 2(L-1) - o(1) as m grows, while H/I < 4 for all L (L=8, mL=1e9: rank term >= 13.99997 I vs H <= 3.843 I). Theorem A's single-order rank code cannot give universal FEI; a block-adaptive reference is needed (C020 territory). Do not try "a better order".

## Targets (one each)
- A091: independent review of B09-BIASED-BLOCK-UNCERTAINTY v1 core lemma only: re-derive the biased physical block identity L_A=M_A+J_A and the Maassen-Uffink step from biased.tex/B09 REPORT; check Delta_A per coordinate at p->0,1; keep the stronger consequences (section 5(4) optimality, composition) separate. Use the repaired certificate at verification/B09_interval_repair_20261011.
- A092: finish the A046 endpoint-tax review from truth tables; then A047's "rare-selector debt coefficient <=1/2" certificates (exact rationals, state the exact refuted/proved statement).
- A093: primary-source check, dated: (i) is H(F)<=2|A|+E H(F_{A<-b}) and the one-coordinate identity (C005/C006) in OWZ11, CKLS16 (corrected version), KMS12, Han25, GMP26? (ii) overlap of Theorem A (all LTFs, constant <8.937) with CKLS16 corrected, CKKLS18, and any 2025-2026 arXiv LTF/FEI preprint. No priority claims without a read theorem statement.
- A094 (first): referee B19-RANKCODE-GLOBAL-ORDER-NOGO from CLAIMS.json of run 20261011T224700Z (re-derive the Jensen step and E[N_p | c in S] bound; try to break it with a tighter order). Then: second independent challenge of A006 (sunflower posterior optimum, residual <=43/10 I, whole cost <=25/2 I) and A007 root law: reconstruct from their statements, test arbitrary-seed tensor embeddings and the XOR-of-AND_L family above.
- A095: the reduction H <= [log2(4+e)+log2(pi^2/4)] I + (2/ln2) R_pi is now PROVED (claim B19-RANKCODE-REDUCTION). Target: a block-adaptive reference (code the occupied-block set, then rank inside each block) with cost O(I) on XOR-of-AND_L uniformly in L and m; state exactly the class where it is O(I).

## Rules
- A floating search is evidence only. Exact rationals or proved intervals for any sign. Name the exact statement refuted (local helper vs FEI).
