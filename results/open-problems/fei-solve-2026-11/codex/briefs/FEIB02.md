disk: small

Read ~/fei_solve_agent/NOTES.md first (notation A, B, Gamma, Theorem 1, Proposition 4).

Task: symmetric Boolean functions (f depends on the Hamming weight only). FEI is proved for them with constant
4.650431 (public repo yspennstate/symmetric-fei-constant; `python3 ~/.claude/dreaming/brain.py recall "symmetric FEI
constant 4.650431 level weights Bessel"` gives the method). Here the goal is the three new functionals.
1. Closed forms. With W_k the weight on level k: mu(S) = W_k / C(n,k) for |S| = k and
   up(S) = sum_{j >= k} W_j C(j,k) / C(n,k). So A = sum_k W_k log( C(n,k) / sum_{j>=k} W_j C(j,k) ) and
   B = sum_k W_k log( sum_{j>=k} W_j C(j,k) / W_k ). Derive the analogous closed forms for Gamma and P (c_S(z)
   depends on the weight of z only; it is a Krawtchouk-type sum of the value vector).
2. Exact numerics: for every symmetric function on n <= 24 variables (2^(n+1) value vectors) compute A/I, B/I,
   Gamma/I, and for balanced ones the same over I-1. Report the suprema by n and the extremal value vectors. Then
   n up to 2000 for threshold functions (all thresholds), majority, parity-of-threshold, and hill-climbing over value
   vectors. Use exact integers or mpmath where cancellation matters and say how you know the digits are right.
3. Prove B <= c I (or A <= c I, Gamma <= c I separately) for all symmetric Boolean functions with an explicit c, as
   small as you can make it, by a direct argument on the closed forms. A proof with c = 3 that is two pages beats a
   numerical c = 1.6. If Theorem 1 then gives H <= 2B + 2I with a constant below 4.650431, say so loudly and check it
   three ways; if it cannot (because sup B/I on symmetric functions is above 1.33), say that with the witness.
4. What do the extremal symmetric functions for B and for Gamma look like? One paragraph each.
Deliverables: PROOFS.md, scripts with outputs, RESULTS.md table by n, REPORT.md.
Memory: keep each process under 3 GiB, at most 2 threads, nice 10.
