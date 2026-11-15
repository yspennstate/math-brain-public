# Referee report on P6, "Erasure entropies of sparse linear DNFs" (an agent, 11 Nov 2026 01:3x)

Read: `fei_papers_agent/p6/main.tex` (385 lines), all of it, read-only. The check below was written from the
paper's statements alone, without opening `p6/code`: `code/referee_p6_check.py`, output `code/referee_p6_check_out.txt`.

## Verdict

The mathematics is correct. Every lemma, the proposition and both theorems hold line by line, and every number in the
paper reproduces. There is one wrong justification (the conclusion it supports is still true), one literature
attribution that should change, a missing citation, and an abstract/theorem mismatch in the hypothesis. None of these
affects a result. Recommended fixes are at the end, in order of weight.

## Line-by-line

**Setup (lines 97-118).** h = (f^(0) - f^(1))/2 = F^(1) - F^(0) is the pivotal indicator, so E h^2 = E h = Inf_i and
hhat(empty) = delta. g = N + M - 1 = 2N - 1 - h. Checked; the script also asserts hhat(T) = fhat(T+i) and
ghat(T) = 2Nhat(T) - hhat(T) for T non-empty on every example.

**Prop 2 (lines 120-164).** Correct.
- On Omega: d/du Phi(u^2, b^2) = 2u log2(1 + b^2/u^2), and |u| ln(1 + b^2/u^2) <= 2b by ln(1+t^2) <= 2t. Moving u
  from -hhat to ghat costs 2|Nhat|, and Phi(q,q) = 2q, so |Phi(p,q) - 2q| <= (8/ln2)|hhat||Nhat|. Cauchy-Schwarz with
  sum_Omega hhat^2 <= delta gives the delta sqrt(kappa) term. Since the empty set is outside Omega it is counted in
  the eps hypothesis, which is what makes sum_Omega q >= (1-eps)delta. Fine.
  Optional: ln(1+t^2) <= t also holds (derivative 2t/(1+t^2) <= 1), which halves the constant 8/ln2 to 4/ln2
  everywhere. Not needed.
- Off Omega: p <= 8Nhat^2 + 2hhat^2, so P <= 8 Var N + 2 eps delta (the sum of Nhat^2 over non-empty T is Var N).
  Jensen with weights q/Q is applied correctly; terms with q = 0 contribute Phi(p,0) = 0. Q log2(e c/Q) has
  derivative log2(c/Q) >= 0 on (0,c], and Q <= eps delta <= c. Fine.
- Empty set: p <= 1, q = delta^2. Fine.
- Measured: the proposition's two-sided bound, with eps and kappa set to the measured values, holds at all 1122
  (coordinate, k) pairs of the test family.

**Section 3 facts (lines 177-181).** Both facts follow from linearity as stated. Harris used in the right directions
throughout (Lemma A: N decreasing vs A_s increasing, R_s decreasing vs V_s increasing; Lemma N: R' decreasing vs
AND_j Q_j increasing, and R' vs Q_j).

**Lemma A (lines 183-202).** Correct. N A_s = A_s R_s (1 - V_s), with R_s, V_s free of the mates of t_s (and of x_i),
gives Pr[N, A_s] = a Pr[R_s, not V_s]. One small gap: the step Pr[R_s](1 - L(D-1)a) >= A(1 - L(D-1)a) uses
Pr[R_s] >= A and needs 1 - L(D-1)a >= 0; when that is negative the inequality Pr[N,A_s] >= aA(1 - L(D-1)a) still holds
because the right side is negative. Worth half a clause. Bonferroni with Pr[N, A_s A_u] <= A a^2 is right, and the
algebra to d a theta A checks.

**Lemma h (lines 210-227).** Correct. h_s = A_s Psi_s with Psi_s free of the mates of t_s (the other A_u involve
disjoint mate sets); the expansion A_s = 2^{-L} sum_S (-1)^{|S|} chi_S gives weight binom(L,j) a ||h_s||^2 on sets
with exactly j mates; the d factor from Cauchy-Schwarz over s is what enters eps. Fine.

**Lemma N (lines 229-257).** Correct. Each background term holds at most one element of J, so
N = R' prod_j (1 - x_j Q_j) with R', Q_j free of J, and D_J N = R' prod_j Q_j/2 (the sign is + with the paper's
convention D_j N = (N|0 - N|1)/2; "+-" is harmless). The k chosen conjunctions are distinct terms, pairwise sharing at
most one variable, so their union has at least kL - binom(k,2) > 0 variables (k <= L). The lower bound on A via
Pr[R', x_j Q_j] = (1/2)Pr[R', Q_j] <= (1/2)Pr[R']Pr[Q_j] is right. The constant matches alpha_k binom(L,k)^{-1}.

**Theorem lin (lines 259-278).** Correct, with one wrong justification. The reduction to Prop 2 is right: eps >= d a
because gamma_k >= a and da <= 1/4; A <= delta/(d a theta) from Lemma A; Var N <= A; delta <= da <= 1/4.

The wrong step is in lines 276-277. The derivative of x log2(e[1 + x^{-2}]) is
log2(1 + x^{-2}) + log2 e (1 - 2/(1 + x^2)), and the paper bounds it below by log2 17 - log2 e * 15/17, which is its
value at x = 1/4. The first piece is decreasing in x, so log2 17 is its minimum on (0, 1/4]. But the second piece is
increasing in x: its minimum is -log2 e (as x -> 0), and -log2 e * 15/17 is its maximum. So the displayed inequality
does not follow from bounding the two pieces separately. It is true anyway (numerically the derivative's minimum on
(0, 1/4] is 2.8145, attained at x = 1/4, equal to the paper's number). Simplest fix: replace the bound by
"log2 17 - log2 e > 0".

**Proof of Theorem 1 (lines 280-291).** Correct. With k = floor(1/eta) + 1, kappa <= 2 L^k 2^{binom(k,2)} 2^{(1-k eta)L}/theta
-> 0; d gamma_k <= Da k L^{k-1} (the paper writes k L^k, weaker but fine); c = 8/(d a theta) <= 16 * 2^L once
theta >= 1/2; x log2(e[3 + c/x]) is increasing (its derivative in natural log is 1 + ln(3 + c/x) - (c/x)/(3 + c/x) > 0).
All bounds depend on L and eta only, uniformly in n, the number of terms, i and d <= D.

**Remark (lines 293-298).** kappa ~ L^k D^k 2^{-(k-1)L} (the d cancels between d alpha_k and delta >= d a theta A), so
with D = 2^{beta L} both conditions hold for k > 1/(1-beta). Fine.

## Numbers (all reproduce)

- AND of k+1 variables, k = 1..11: the formula 2(1 - 2^{-k}) + 2^k Phi((1 - 2^{-k})^2, 4^{-k}) equals the exact
  E_i/Inf_i to 10 digits, and |ratio - 2| <= 2^{-k}(2k+2) at every k (e.g. k=10: 0.01898 against 0.02148). The bound
  follows from eq. (phiq): 2^k Phi <= 2^{-k} log2(e(1 + 4^k)), and the ratio is at least 2 - 2^{1-k}.
- Table 1 (stars): all 7 rows, both Inf columns and both ratio columns, match to every printed digit.
- Rows and columns of the m x m array: 2.6293 (m=3) and 3.2454 (m=4), as stated.
- Lemmas A, h, N, Theorem lin and Prop 2 on my own family (5 stars, the 3x3 and 4x4 arrays, 14 random linear DNFs with
  w in {4,5}, D <= 4, n = 14-17): 1122 (coordinate, k) pairs, zero failures of any inequality. Theorem lin applies at
  1077 of them (theta > 0 and da <= 1/4); its left side reaches 0.146 of its right side at most. The paper's "never
  more than 0.14" is a statement about its own 17 examples and may stay, but it is not a property of the bound.

## Literature paragraph (lines 44-47)

- "It is known for symmetric functions" has no citation. The source is O'Donnell, Wright and Zhou, The Fourier
  entropy-influence conjecture for certain classes of Boolean functions, ICALP 2011 (they also prove read-once decision
  trees).
- "for read-once formulas [OT13]": O'Donnell and Tan prove FEI for read-once formulas over arbitrary gates of
  **bounded arity** (arXiv 1304.1347, abstract). Read-once AND/OR formulas of unbounded fan-in, which include the
  read-once DNFs that this paper names as the degree-one case (line 62), are due to Chakraborty, Kulkarni, Lokam and
  Saurabh, Upper bounds on Fourier entropy, Theoret. Comput. Sci. 654 (2016) (COCOON 2015), with a more elementary
  method. Suggested: "for read-once formulas [OT13, CKLS]", or "for read-once formulas over gates of bounded arity [OT13]
  and over AND and OR gates [CKLS]". Please check the CKLS bibliographic details against the journal page before
  adding them.
- "read-k decision trees with k fixed [WWW]" is accurate (WWW's constant grows with k; a later paper improves the
  dependence, but "k fixed" covers it).
- Min-entropy for read-k DNFs [Shalev, ACKSW] and Han's bound match what those papers state, as far as I can see from
  their abstracts.

## Presentation

1. Abstract (line 30) says D <= 2^{(1-eta)w}; Theorem 1 says D <= 2^{(1-eta)(w-1)}. For fixed eta the two are
   equivalent as asymptotic statements (the first class sits inside the second with eta/2 for w large), but a reader
   will see two different hypotheses. Use (w-1) in the abstract, or say "D <= 2^{(1-eta)w}" in the theorem and add one
   line in the proof.
2. Line 89 uses L in "((D-1)2^{-L})^k" before L is defined (line 168). Write 2^{-(w-1)} there, or define L in the
   introduction.
3. Lemma A: add "(if 1 - L(D-1)a < 0 the bound is trivial)".
4. Theorem lin proof, lines 276-277: the derivative bound, as above.

Checked separately: the funding and competing-interest sections are word for word those of P4; the AI declaration
names the system that found the result and states that the checks are not peer review, with no account of the writing
process. No sentence in the body is about the paper's own history.

Sources read 11 Nov: arXiv 1304.1347 (O'Donnell-Tan abstract), the OWZ ICALP 2011 abstract
(experts.illinois.edu), and arXiv 1806.03646 (Shalev, for the CKLS and read-k decision tree context).

## Re-check of the revision (11 Nov 01:4x)

All five points are fixed in the 391-line text: the abstract now reads D <= 2^{(1-eta)(w-1)}; line 90 writes 2^{-(w-1)}; Lemma A carries the trivial case (line 201); the derivative bound is log2 17 - log2 e > 0 (line 279); the literature cites OWZ for symmetric functions, OT13 for bounded arity and CKLS (TCS 654 (2016) 92-112) for AND/OR gates. Nothing further from me.
