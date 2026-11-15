# Referee report on P5, "A filtration bound for the erasure entropies of Boolean functions" (an agent, 11 Nov 00:3x)

Text read: fei_papers_agent/p5/main.tex as of 00:3x (368 lines, with the bent-point paragraph). Every proof re-derived
by hand. Numbers re-computed with my own code, code/referee_p5_check.py (written without reading p5/code; conditional
expectations, W and V are computed by averaging on the cube, not from Fourier sums), output
code/referee_p5_check_out.txt: 60 random functions n = 3..7 at biases 1/2, 0.2, 0.05, every coordinate, every order for
n <= 6 and 40 random orders at n = 7 (13,720 coordinate-order pairs); 112 compositions; 46 private ANDs.

## Verdict
The mathematics is correct. No errors in Theorem 1 (a)-(c), Lemma 2, Theorem 3, the coarse-chain remark, Proposition 5,
Proposition 6 or the window ladder, and every table entry reproduces to four places. Four things to fix (items 1-4);
the rest are small.

## Checked, correct
- Thm 1(a): L = H(1[i in U] | lab), lab a function of U \ {i}. E - L <= 1.1e-16, L <= h2(Inf) exactly.
- Phi: d/da Phi = log2((a+b)/a) >= 0; concave and 1-homogeneous, hence superadditive. Right.
- Thm 1(b): martingale form agrees with increments computed by averaging out the unrevealed coordinates, error 0.
- Thm 1(c): DP = minimum over all orders exactly (n <= 6), DP <= every sampled order at n = 7.
- Lemma 2: Phi <= b/ln2 + psi, psi = b log2(1 + a/b) is the perspective of log2(1 + a), so concave, 1-homogeneous and
  increasing in both arguments (d/db = log2(1+x) - x/((1+x) ln 2) >= 0, x = a/b). On G_j: A_{G_j} < 2^{j+1} M delta,
  B_{G_j} <= 2^{-j} delta, and 1 + 2^{2j+1} M <= 2^{2j}(1 + 2M). Sum gives 1/ln2 + 4 + 2 log2(1+2M). Right; minimum
  slack 0.20 delta on the sample.
- Thm 3: both identities hold exactly against cube resampling; the K = 0 product is (1-delta) fhat(i)^2 <= delta^2 (max
  ratio seen 0.969). The coarse-chain remark: for k in block s, R_k contains R'_{s+1} and R_{k-1} lies in R'_s; right.
- The V formula in the monotone paragraph: V = (1/2) E (g(x) - g(x^R))^2 gives Pr[x in D, x^R not in D] + 4 Pr[x in L,
  x^R in H]. Right.
- Conj 4 => FEI with c + 2/ln2 via Thm 1(a), [Shm1] and closure under restriction. Right.
- Prop 5: fhat(T1 u T2) = [T1 = 0] F0hat(T2) + ghat(T1) F1hat(T2); formula holds to 1.1e-16, influence identity exact.
- Prop 6: coefficients, delta = 2^k sum p_V = 2^{-k} Pr[c != 0], the 2^{r-1} count, P = 1 - 2 delta + 2^{-k} delta, and
  Phi(P,Q) <= Q log2(e/Q). All right; the bracket holds on every sample. AND_n is the case v empty: AND_10 has
  F = 2.0340568 against the upper bound 2.0340678, so the bound is nearly attained.
- Windows: L_window(1) = L, L_window(m) = E, nonincreasing in r, never below E. The derivative identity is right
  (D_K h has coefficient hhat(T' u K) at T').
- Table: all twelve columns reproduce (AND 2.2922 / 2.1048 / 2.0341; MAJ 1.0000 / 1.5204 / 1.7848 / 1.9578 / 2.0844 with
  E = 0; TRIBES 2.3160 / 3.0428 / 3.3892 / 2.5474, F = min E/Inf). Bent point k = 2, 4, 6, 8 reproduces (2.672/2.950/0.891,
  5.224/5.351/1.699, 7.387/7.426/1.929, 9.429/9.439/1.983); k = 10 not run.

## Must fix
1. Abstract, the resampling sentence. "the probability that resampling the not yet revealed coordinates preserves the
   pivotality of i" reads as the conditional probability Pr[x^R in D | x in D] = W/delta. The theorem uses the joint
   quantity W(R) = Pr[i in U, U n R = 0], which for monotone f is Pr[i pivotal at x and at x^R] (for general f a signed
   correlation). With the conditional reading the condition is off by a factor delta. Suggest: "the probability that i
   is pivotal both before and after the not yet revealed coordinates are resampled, times the block influence of those
   coordinates, is O(Inf_i^2)".
2. Abstract vs Prop 6, the constant. The abstract states 2 + 2^{-k}(2k + 1 + log2(1/rho)); Prop 6 gives
   2 + 2^{-k}(2k + log2 e - 2 + log2(1/rho)). Both are true, but since log2 e - 2 < 0 the abstract can state the simpler
   and stronger 2 + 2^{-k}(2k + log2(1/rho)), which follows directly (checked on all 46 samples, slack >= 0.07).
3. Tribes, Section 3: "the order that reveals the other tribes first and the mates of i last satisfies it" is asserted
   without proof, and M is not uniform in the width without a condition. Two lines do it with the coarse chain
   R_* > mates > 0: W(mates) = P0 4^{1-w} with P0 = Pr[no other tribe satisfied], delta = P0 2^{1-w}, V <= 1, so the
   first product is at most delta^2 / P0; and V(mates) <= Pr[x in D] = delta because a jump from L to H needs another
   tribe to change, so the second product is at most delta^2. Hence M <= 1/P0, bounded in the usual regime where P0 is
   about 1/2. Numerically M = 0.82 (2x3, 2x4, 2x5), 0.71 (3x3), 0.50 (4x2), 0.82 (3x4), and this order attains F in the
   table.
4. Bent-point paragraph. (a) "y != 0" and "f(0, x_i)" are undefined on {-1,1}^k: name the point (y = (1,...,1), the
   point where every 0/1 bit is 0) and write b in +-1 form. (b) The paragraph gives numbers but not their reading; one
   clause: the new coordinate has E_i/Inf_i growing about linearly in k while every coordinate of y stays below 2, so the
   choice of i in Conjecture 4 cannot be dropped. (c) It sits between the table and the sentence "On AND and tribes ...",
   which comments on the table; move it after that paragraph.

## Small
5. Thm 3: "R_k = R_* \ S_k the set of coordinates revealed after step k" can be misread as "revealed later"; write
   "not yet revealed after step k".
6. Section 6, last sentence: Conjecture 4 is by definition window 1, so "or whether Conjecture 4 holds with window 1" is
   redundant; say "whether Conjecture 4 holds, or holds with some fixed window r in place of 1".
7. Section 3, monotone paragraph: the V formula holds for every Boolean f (proof above); only the W formula uses
   monotonicity. One clause.
8. Abstract, "is a sum over the steps of a martingale of a two-variable entropy function": hard to parse. Suggest "is a
   sum, over the steps of the Doob martingales of E_i f and D_i f, of a two-variable entropy of their squared increments".
9. Section 7 could note that AND_n is Prop 6 with v empty and sits just under its upper bound (2.034057 against 2.034068
   at n = 10).
10. Funding block cites the Google education credit by number, as in P4; the author's call, not a math issue.

All citations resolve (GMP and Han are in). No sentence about the writing process in the body; the AI declaration is
factual. Voice is fine.

## Re-check of the posted text (11 Nov 01:1x)
Items 1-9 applied and read correctly: abstract joint pivotality and constant 2k+log2(1/rho); tribes proof (delta = P0 2^{1-w}, W(Q) = P0 4^{1-w} = delta^2/P0, M = 1/P0); bent point in +-1 form after the table comment, with its reading; "not yet revealed"; window sentence; V formula for every Boolean f; AND_n note. The new k = 10 bent-point values reproduce with code/referee_p5_check.py: E/Inf 11.439, min L/Inf 11.442, y coordinates 1.996. Item 10 (funding line) left to the author.
