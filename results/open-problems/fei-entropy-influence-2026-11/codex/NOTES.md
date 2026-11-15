# FEI up-ratio notes (shared by the FEIB workers; written 9 Nov 2026 by an agent)

Conjecture (Fourier Entropy-Influence, Friedgut-Kalai 1996): there is a universal C with H(f) <= C I(f) for every
f: {-1,1}^n -> {-1,1}, where mu(S) = fhat(S)^2, H = sum_S mu(S) log2(1/mu(S)), I = sum_S |S| mu(S).
Best known lower bound on C: 6.5218 (balanced functions, score H/(I-1)). Best general upper bounds are of the form
H <= C (I + sum_i I_i log(1/I_i)) and spectral concentration on 2^{O(I log I)} characters (Kelman, Kindler, Lifshitz,
Minzer, Safra 2020). Logs are base 2 unless stated.

## Notation
For S a subset of [n] and z an assignment to the coordinates outside S, c_S(z) is the S-Fourier coefficient of the
restriction of f to the subcube {x_S free, rest = z}. It is an integer multiple of 2^{1-|S|} with |c_S(z)| <= 1.
  fhat(S) = E_z c_S(z),      up(S) = E_z c_S(z)^2 = sum_{U contains S} mu(U) = Pr_{U~mu}[U contains S],
  abs1(S) = E_z |c_S(z)|,    p(S) = Pr_z[c_S(z) != 0].
  A     = sum_S mu(S) log(1/up(S))            containment: E_{S~mu} log 1/Pr_U[U contains S]
  B     = sum_S mu(S) log(up(S)/mu(S))        dispersion:  E_{S~mu} log 1/Pr_U[U = S | U contains S]
  Gamma = sum_S mu(S) log(abs1(S)/|fhat(S)|)  sign cancellation of the restricted coefficient
  P     = sum_S mu(S) log(1/p(S))
  Var   = 1 - mu(empty).
H = A + B exactly.

## Proved (elementary; checked on all 65,536 functions of 4 variables and all 2^31 of 5 variables for Theorem 1)
THEOREM 1.  A <= B + 2I - 2Var, hence H <= 2B + 2I - 2Var.
  Proof. |c_S(z)| <= 2^{|S|-1} c_S(z)^2 pointwise (granularity), so |fhat(S)| <= E|c_S| <= 2^{|S|-1} up(S) for S
  nonempty; then log(1/up(S)) <= 2(|S|-1) + log(up(S)/mu(S)); sum against mu.
  Consequence: FEI holds if and only if B <= C' I for every Boolean f (C <= 2C' + 2, C' <= C).
PROPOSITION 4.  B <= (I - Var) + P + 2 Gamma <= (I - Var) + A + 2 Gamma,  and Gamma <= B/2,  P <= A.
  Proof. log(up/mu) = log(E c^2/(E|c|)^2) + 2 log(E|c|/|E c|). Since |c| <= 1, E c^2 <= E|c|, and E|c| >= 2^{1-|S|} p(S);
  so the first term is at most (|S|-1) + log(1/p(S)), and p(S) >= up(S). Cauchy-Schwarz gives Gamma <= B/2.
  Consequence: FEI holds if and only if BOTH
     (A-conjecture, containment)   A <= C I       and
     (Gamma-conjecture, cancellation)   Gamma <= C I.
LEMMA 2 (coding). For 0 < lam < 1 put up_lam(S) = sum_{U contains S} lam^{|U - S|} mu(U). Then
  B <= B_lam + I log(1/(1-lam)),  B_lam = E_{S~mu} log(up(S)/up_lam(S)) = E_S log 1/E[lam^{|U-S|} | U contains S].
  (nu(S) = (1-lam)^{|S|} up_lam(S) is a probability measure; Gibbs.) Jensen on B_lam is false by sqrt(n) on majority.
  More generally any kernel r(U,S) >= 0 with sum_{S subset U} r(U,S) = 1 gives B <= E_S log 1/E[r(U,S) | U contains S].
LEMMA 3 (recursion). For real g and a coordinate i, a = E_i g, d = D_i g (so g = a + x_i d):
  B(g) = B(a) + B(d) + J_i(g),  J_i(g) = sum_{S not containing i} ahat(S)^2 log(1 + up_d(S)/up_a(S)),
  and up_g(S) = up_a(S) + up_d(S) for i not in S, up_g(S + i) = up_d(S).
  Composition: for balanced g on disjoint blocks, B(f o g) = B(f) + I(f) B(g) (same law as H).

## Numbers so far
All 5-variable functions (2^31 with f(0)=+1): max B/I = 1.4795382825 (truth table 0x0000000e), max H/I = 3.6237404
(AND_5), balanced max B/(I-1) = 2.1537593748 (0x008eeeee), balanced max H/(I-1) = 6 (0x00aaeeee, H 3, B 1, I 1.5).
All 4-variable functions: sup A/I 1.9375, sup B/I 1.4650, sup Gamma/I 0.375; balanced sup A/(I-1) = 4, B/(I-1) = 2,
Gamma/(I-1) = 0.517, H/(I-1) = 6 (attained with Gamma = 0, A = 2, B = 1).
AND_n: B = I(1+o(1)), H = 4I(1+o(1)). Majority: A ~ (1/2) log n, B and Gamma of order sqrt(n) ~ I.
Truth table convention of the C census: bit x of tt set means f(x) = -1, x in {0..2^n-1}.

## Known dead routes (do not repeat)
Plain restriction induction on H (needs a constant >= 7.05 that grows with n); restricting the most influential
coordinate (fails by composition); monotone shifting; per-coordinate payment for H (the sharp per-coordinate bound is
I_i ln(e/I_i)); local payment of the J term by ||D_i g||^2 alone (unbounded: a = level-1 mass spread over N
coordinates, d = parity of those N gives J/||d||^2 ~ log N).

## Rules for these briefs
Proofs are written out in full; a numerical statement names the script and the output file. A claimed theorem is
tested by a script that tries to break it (all functions on n <= 4 at least, random and structured ones beyond).
If you find a counterexample to anything in this file, say so first, with the function. Do not report "likely true".
Code in this folder: verify_forms.py, check_2B.py, check_gamma.py (numpy), census5.c (exhaustive 5-variable census).
