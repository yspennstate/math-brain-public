# STRAT19 log

Task received 2026-11-13 18:16 +04: STRAT19 T104 split 3+5, isolates then arbitrary lower components; 4+5 if time remains.

2026-11-13 18:20 +04 — Read STRAT18 RESULT.md in full and the inherited formulas. Copied proof sources byte-identically to inherited18; hashes recorded in source_hashes.json. Parent owns the workspace mesh claim; no shared coordination database writes. No subagents.

OPEN: connected 3+5 signs and maximal lower endpoints. Checking a comparison to the proved 2+5 endpoint before constructing new SOS certificates.

Development step — PROVED (transfer35.py): rank(A5)<=3 transfers from the inherited 2+5 theorem at k=5 to 3+5 at k=6. Additional rational margins are 1/20 at the three-path corner and 73/675 at the balanced triangle. All 24 path Bernstein controls are positive. Inverse-padding derivative is <=-17/15 throughout this domain. The first development run caught an incorrect coefficient in the auxiliary derivative identity; corrected from 76/9 to 58/9 and reran successfully.

PROVED (tree35.py): six connected triangle/five-tree isolate numerators have only positive coefficients in the positive fluxes and z=k-6. Their maximal-lower-trace numerators also have only positive coefficients in z=k-8. Exact inverse-padding derivative endpoints have nonnegative coefficients. Isolate coefficient counts: 858,609,705,5982,4239,4911. Lower counts: 858,609,705,6006,4263,4935.

PROVED (lower35.py): all top pairs satisfy F_k(k-7)>=F_6(0)+1/4, k>=8 and infinity. Twelve degree-two Bernstein controls have positive rational coefficients in k-8; no isolate margin is spent.

NUMERICAL: one compute process at a time in development, single-thread library limits; no solver. The sandbox rejected changing niceness, so no priority change was available. All work remains in STRAT19; copied proof inputs total under 1 MB.

PROVED (symbolic35.py): all twelve new tree-pair numerators agree universally with the direct 8x8 selected-projector construction; all three-path moment identities hold after clearing denominators.

PROVED (audit35.py): twelve rational fixtures agree with the original centered definition, including feasible lower edges. The first development audit caught Python's 0/2 default becoming a float; sympification now precedes division, and the functional explicitly rejects all SymPy Float values. Corrected audits pass exactly.

PROVED (symmetric35.py): K3+K5 has T*_N8=56/135, T*_infinity=4, and maximal-lower F_8(1)=95/96. Original-matrix replay independently gives normalized endpoint T=95/1176. All six equal-flux tree-pair margins and their lower endpoints are recorded.

PROVED (setup45.py): separate four/five concavity and exact lower-trace interpolation are set up at k=7, with lower trace cap k-8 at k>=9. OPEN: 24 connected endpoint types and their lower endpoints.

Full 39-stage replay launched. RESULT.md now contains the 3+5 proof, equality argument, margin tables, 4+5 ledger and remaining disconnected-D=2 scope. No counterexample found; all candidate checks used exact arithmetic.

PROVED (replay_all.py): 39 stages PASS. NUMERICAL runtime 101.78110945801018 seconds; aggregate peak upper bound 120930304 bytes.

2026-11-13T18:32:32+04:00 — Final audit: all 82 proof-input hashes and 5 certificate-receipt hashes match replay. All 71 pinned copies match the unchanged read-only source bytes. NUMERICAL total workspace 1069754 bytes. PROVED (replay_all.py): 3+5 closed; OPEN: remaining disconnected D=2 splits 4+5 and 5+5 outside inherited special subcases.
