# B15 stream notes (Claude lead) - v2, 2026-10-11 23:25 UTC

Full FEI: OPEN. Read this at every stage start. Run: runs/20261011T225100Z-claude-B15-erasure-countersearch.

## Established (exact, pending independent review)
- n<=4: every nonconstant Boolean f has a relevant i with B_i<=K* Inf_i, K*=4+(5/2)log2 5-(9/2)log2 3; equality exactly at the 64 three-variable point defects. Independent reproduction of A082-FINITE-TRUE-ERASURE (65,470 strict, 64 equal, 0 fail).
- L(K*) FAILS beyond n=4. f_5=-1 exactly on {e1, e1+e2, e1+e2+e4} in F2^5: every B_i>(539/200)Inf_i. f_6=-1 exactly on {0, e0..e5, e1+e2, e0+e4, e3+e5}: every B_i>(368/125)Inf_i (all ratios 2.944495). Two exact paths (big-integer powers; prime-exponent forms + 400-bit intervals). Claim B15-LKSTAR-FAILS-N5-N6@1.
- Proved: L(K) universal => FEI(K+c), c=4 (JS_i<=4min(Inf_i,1-Inf_i), proved) or 2/ln2 (C005); FEI(C) => L(C). So C_FEI-c <= E* <= C_FEI. Composition with balanced, level-one-free g preserves every per-coordinate ratio B_c/Inf_c. Claim B15-SELECTION-EQUIVALENCE-COMPOSITION-INVARIANCE@1.

## Refuted / retired
- "K* is a universal selection constant" (nobody claimed it; A082 is scope-limited). Leaf constants stay leaf constants.
- Symmetric functions never beat K* (n<=14). Cyclic n=7 best 2.9386 < f_6.

## One target each
- A071: freeze the proved-complete n=5 domain (2^32 tables modulo hyperoctahedral group and negation, or branch-and-bound over the sparse side A with |A|<=6) and decide E*(5) exactly; current lower bound 2.695887520 (f_5).
- A072: add B_i, JS_i, Delta_i to the engine on the uniform cube; reproduce f_5 and f_6 from the truth tables (4194372, 1103806792023) and publish the exact prime-exponent form of min_i B_i/Inf_i for each.
- A073: certify with outward intervals the exact values E(f_5)=2.695887520... and E(f_6)=2.944495304... to 30 digits, and the 24 cyclic n=7 float violations (B family) one by one.
- A074: reproduce both witnesses by a third path (direct conditional-entropy sum over the joint law of (S_i,S_-i) in Fractions plus mpmath), and re-run the n<=4 census independently.
- A075: turn the pattern into a family: sparse side = Hamming ball of radius 1 plus a perfect matching (f_6) or a monotone path (f_5); compute min_i B_i/Inf_i analytically in n and test whether it grows. Use Lemma 3: composition cannot raise the ratio, so look at restrictions and level-one-carrying inner functions.

## Do not repeat
- B09 three-bit grid; raising n blindly; float-only verdicts; claiming a finite pass proves a universal statement; certify() on int64 truth tables for n>=6 (use Python ints).
