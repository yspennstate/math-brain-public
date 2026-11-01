# F0059 - Janson, Problem 18.39: can the largest box be o(n) along the whole sequence when 0 < nu < lambda?

Worked 2026-09-09, about two hours. Status: partial. Nothing here settles the problem. What is new is
(a) a reduction of the question to a competition between scales of the weight sequence, made
quantitative by an exact decomposition plus a tilt criterion that I checked against exact partition
functions, (b) a deterministic "record-gap" lemma (Lean-checked) which is the rigidity input the
conjecture needs in the sparse-support case, and (c) an explanation of why the strong form of the
conjecture cannot hold with a margin: at a record scale with an O(1) gap the giant box is present with
probability strictly between 0 and 1.

## 1. The problem as the source states it

Janson, Simply generated trees, conditioned Galton-Watson trees, random allocations and condensation,
Probab. Surveys 9 (2012), arXiv 1112.0510, Section 18.6, p. 122 of the arXiv PDF:

> Problem 18.39. Is Y(1)/n -->p 0 possible when 0 < nu < lambda? Example 18.36 shows that this is
> possible for a subsequence, but we conjecture that it is not possible for the full sequence, and, a
> little stronger, that there always is some epsilon > 0 and some subsequence along which
> Y(1) >= epsilon n w.h.p.

Notation (Sections 10, 18): w = (w_k) is a weight sequence with w_0 > 0, Phi(t) = sum w_k t^k with
radius rho, Psi(t) = t Phi'(t)/Phi(t), nu = Psi(rho); B_{m,n} puts m balls in n boxes with probability
proportional to prod_i w_{Y_i}; Y(1) >= Y(2) >= ... are the ordered box counts; m/n -> lambda.
Lemma 18.31 (p. 113): for nu < lambda < infinity and any K_n -> infinity, the boxes with more than K_n
balls hold (lambda - nu) n + o_p(n) balls. Condensation to one box means (18.106)-(18.107):
Y(1) = (lambda - nu) n + o_p(n), Y(2) = o_p(n). Theorem 18.33 proves it for w_k ~ c k^{-beta}, beta > 2.
Example 18.36 (support {k_j} with k_j >= j k_{j-1}, w_k = (k+1)^{-4} on the support, m = n - 1): along
n = k_j, Y(1) <= n/j; along n = 3 k_j, w.h.p. two boxes with k_j = n/3 balls each.

The ledger row quotes the statement correctly. The direction of every claim above was checked against
the PDF text (source_text.txt in this directory, lines 6803-6900 and 7342-7510).

## 2. Finding

Take rho = 1 without loss of generality (replace w_k by w_k rho^k; the model B_{m,n} does not change).
Then Phi(1) < infinity, sum_k k w_k = nu Phi(1) < infinity, and limsup_k w_k^{1/k} = 1. Put, for k >= 1
in the support S of w,

    h(k) = log(k w_k) / k .

Two immediate facts: k w_k -> 0 (terms of a convergent series), so h(k) < 0 for all large k in S; and
limsup_{k in S} h(k) = 0 (from limsup w_k^{1/k} = 1 and (log k)/k -> 0). So the running maximum of h on
S climbs to 0 through infinitely many strict records b_1 < b_2 < ..., h(b_{i+1}) > max_{k <= b_i} h(k).

Reformulation. B_{m,n} is the law of n i.i.d. variables xi_i with P(xi = k) = w_k/Phi(1), conditioned
on sum xi_i = m (Janson's (10.3) at tau = rho = 1). Since Phi(t) = infinity for t > 1, xi has mean nu
but no exponential moment. Problem 18.39 asks whether, conditioning such a sum on the linear deviation
sum xi_i = m ~ lambda n > nu n, the maximum summand can be o(n) in probability for every n. For
subexponential tails (regularly varying, Weibull with index below 1) the answer is the one-big-jump
principle; Janson's problem is about tails too irregular for any of that theory.

Exact decomposition and the tilt criterion. Fix a support point b and n, m. Let Z_{<b}(m', n') be the
partition function with all box sizes restricted to S cap [0, b). If no support point lies in (b, m]
(sparse support), then exactly

    Z(m, n) = sum_{i >= 0} C(n, i) w_b^i Z_{<b}(m - i b, n - i),

and P(Y(1) >= b) = 1 - Z_{<b}(m,n)/Z(m,n) = A_{>=1}/(A_0 + A_{>=1}) in Janson's notation. Writing
Z_{<b}(m', n') = Phi_{<b}(t)^{n'} t^{-m'} P_t(S_{n'} = m') for the tilt t with Psi_{<b}(t) = m'/n', and
dropping the local (polynomial) factor, the i-th term over the zeroth is

    log(A_i/A_0) ~ log C(n,i) + i log w_b + F(m - ib, n - i) - F(m, n),
    F(m',n') = n' log Phi_{<b}(t) - m' log t.

For i = 1 and n = C b this is, to first order, log n + log w_b + b log t_1 - log Phi_{<b}(t_1)
= b [ h(b) + log t_1 ] + O(1), where t_1 > 1 is the tilt the truncated system needs to absorb the excess
(lambda - nu) n - b. The box of size b appears iff h(b) + log t_1 is positive by more than O(1/b).

What sets the tilt. t_1 = 1 + epsilon solves G(epsilon) := sum_{k < b} (k - lambda'') w_k (1+epsilon)^k = 0.
G is increasing with G(0) < 0, and the k-th positive term equals exp(k (h(k) + log(1+epsilon))) up to the
factor (1 - lambda''/k), so the tilt is pinned by the scales k < b with the largest h: to leading order
log t_1 = - max_{K < k < b} h(k) - theta/a, where a is the argmax and theta = O(log N + 1) with N the number
of near-record scales k < b (those with h(k) >= h(a) - O(1/k)). Hence

    the b-box wins at n = C b   iff   b [ h(b) - h(a) ] > theta b / a + O(1),   a = argmax_{K<k<b} h(k).

A scale b hosts a giant box (a positive fraction of n) exactly when it is a record of h whose gap over
the previous best scale exceeds a constant over the previous scale, the constant being set by how many
scales sit within O(1/k) of the record level. Example 18.36 has h increasing (every scale a record, gaps
of order (log k)/k times k_j/k_{j-1} in the exponent), which is why every n = 3 k_j gives giants. The
first attempt's pairwise-merge lemma (A001) is the special case "a and b, no entropy"; the entropy
correction is exactly the log k inside h and the log N inside theta.

Record-gap lemma (deterministic; the rigidity input). Let b_1 < b_2 < ... be the records of h on S and
suppose b_{i+1} >= 2 b_i for all large i (sparse support). Then for every c > 0 there are infinitely
many i with h(b_{i+1}) - h(b_i) > c / b_i.

Proof. If h(b_{i+1}) - h(b_i) <= c/b_i for all i >= i_0, telescoping and b_{i0+l} >= 2^l b_{i0} give
h(b_{i0+N}) - h(b_{i0}) <= 2c/b_{i0} - 2c/b_{i0+N} <= 2c/b_{i0} for every N. Since h(b_i) -> 0 (the records
realise the limsup), -h(b_{i0}) <= 2c/b_{i0}, i.e. b_{i0} w_{b_{i0}} >= e^{-2c} for every i_0 >= i_0(c),
which contradicts sum_k k w_k < infinity. The telescoping inequality and the limit step are the theorems
F0059_telescope, F0059_bound, F0059_limit in U_F0059.lean; compiled clean on the second attempt (lean_compile_2.txt),
axioms propext, Classical.choice, Quot.sound only.

Bounded near-record count, sparse case. For the record a with eta = -h(a): a scale k < a with
h(k) >= h(a) - L/k has k w_k >= e^{-L} e^{-k eta}, so among k <= 1/eta at most e^{L+1} nu Phi(1) such
scales exist (again by sum k w_k < infinity); among k in (1/eta, a) a sparse support has at most
log_2(a eta) + 1 points, and a eta = log(1/(a w_a)). This is where the argument does not close cleanly:
the count of competing scales in (a/log(1/(a w_a)), a) can grow like log log(1/(a w_a)), so theta above
is O(log log log(1/(a w_a))) rather than O(1), and the record-gap lemma delivers gaps > c/b_i for every
fixed c but not for a c that grows. For supports whose a w_a decays at most doubly exponentially in the
record index this is harmless; in full generality it is a genuine gap.

Consequence for the conjecture as stated. In the sparse case (k_{j+1}/k_j -> infinity), along n_i = C b_i
for the records with gap > c/b_{i-1} the ratio A_{>=1}/A_0 has leading exponent (c - theta) b_i/b_{i-1} -> infinity; provided the local
factors of the truncated partition functions are smaller than that (item 2 below, which needs
k_j >> k_{j-1}^3 log^2 k_j on the route I sketched), the ratio tends to infinity: Y(1) >= b_i = n_i/C with probability -> 1. This is the strong form of Janson's
conjecture with epsilon = 1/C, C > 1/(lambda - nu), for every sparse weight sequence, modulo the two
points listed under "not done" (uniform control of the local factors in the truncated partition
functions, and the near-record count). At a record with gap only O(1)/b_{i-1} the giant box is present
with probability bounded away from both 0 and 1 (E3, E3b, E4 below), so the w.h.p. statement genuinely
needs the gap lemma, not merely the existence of records.

## 3. What is not done

1. No proof of either form of the conjecture for general weights. The dense-support case is untouched:
   there the competitors of a record scale b are the scales just below it, which are themselves of
   order n, and the record-gap lemma fails (records can be every integer with summable gaps that are
   not bounded below by c/b). I expect the conjecture to hold there for a different reason (the
   competitors are macroscopic), but I have no argument.
2. In the sparse case the argument is a heuristic proof: the free-energy approximation
   log Z_{<b}(m',n') = n' log Phi_{<b}(t) - m' log t + o(n') is Theorem 17.1 for a fixed truncated
   sequence, whereas here the truncation moves with n. A route around the local factors: the trivial
   upper bound Z_{<b}(m,n) <= Phi_{<b}(t)^n t^{-m} for any t; a lower bound on Z_{<b}(m-b, n-1) by the
   max-coefficient trick (some x within L sigma sqrt(n) of the tilted mean has local probability at
   least (1 - 1/L^2)/(2 L sigma sqrt(n) + 1)) and then shifting the mass to the target one small box at a
   time through the exchange identity E[N_s 1{S=x}] pi_0 = E[N_0 1{S=x-s}] pi_s at cost O(1/n) per step,
   total exp(-O(sqrt(k_{j-1} k_j) log k_j)), which is o(b_i (h(b_i) - h(a))) when k_j >> k_{j-1}^3 log^2 k_j.
   I did not write it out.
3. The near-record count in (a/log(1/(a w_a)), a): the triple-log loophole above.
4. Lean certifies only the deterministic telescoping lemma, not any probabilistic statement.

## 4. Checks

- DP for Z(m,n) (f0059_dp.py) checked against brute-force enumeration on all (n,m) with n <= 6, m <= 12
  for an irregular 4-point support: agreement to 1e-12.
- f0059_experiment.py (output in experiment_out.txt): support {0,1,2,6,24,120,720}, rho = 1, exact
  P(Y(1) >= b) at n = C b against the free-energy prediction summed over i. The test had room to fail in
  both directions and at the borderline:
  - E1, w_k = (k+1)^{-4}, lambda = 1, C = 3: exact log-odds 24.9 / 64.2 / 128.5 at b = 24 / 120 / 720,
    predicted 24.3 / 63.5 / 128.1. The i = 1 term alone gives half of it: two b-boxes fit, as in Janson's
    Example 18.36, and A_2 dominates.
  - E2, scale 120 killed (h(120) = -0.5 < h(24) = -0.40): exact log-odds -11.5 at b = 120 (P = 1e-5),
    predicted -11.8; at b = 720 (a record over a = 24) exact 545.7, predicted 545.0.
  - E3, 720 made a record with b(h(b) - h(a)) = +2 over a = 120: P(Y(1) >= 720) = 0.868, exact log-odds
    1.88, predicted 1.70. E3b (C = 2): P = 0.709, exact 0.89, predicted 0.41 (the local factors, dropped
    in the prediction, are worth about half a nat here). E4, gap -2: P = 0.100, exact -2.19, predicted -2.36.
  - E5/E6, lambda = 2, C = 2: exact 109.0 / 203.5 (E5) and -7.6 / 968.8 (E6) against predicted
    104.9 / 202.7 and -7.7 / 962.4.
  The prediction is within about one nat of the exact log-odds whenever a single i dominates, and within
  a few percent on exponents of several hundred nats. Sign and magnitude of the criterion are confirmed
  on every case, including those where the box is absent.
- The strongest case that I am wrong about the sparse-case conclusion: a sequence whose records have
  many near-record scales just below them, so that theta grows and the gap lemma's fixed c is not
  enough. I could not build an instance of that asymptotic loophole at DP-feasible sizes (n <= 3000),
  and I have not proved it cannot happen, so the sparse-case claim is stated as a heuristic argument
  with a named gap, not as a theorem.

## 5. Prior art

Web search (2026-09-09) for "Problem 18.39" Janson, and for the noun phrases ("random allocations"
condensation "largest box"; condensation simply generated trees irregular weights), plus the Semantic
Scholar citation list of arXiv 1112.0510 (270 citing papers, scanned by title; citations.json). Nothing
addresses irregular weights or the full-sequence question. Related: Kortchemski, Limit theorems for
conditioned non-generic Galton-Watson trees (AIHP 2015) and Kortchemski-Richier, Condensation in
critical Cauchy Bienayme-Galton-Watson trees (AAP 2019), regularly varying weights only; Condensation
in subcritical Cauchy Bienayme trees (arXiv 2503.07530, 2025), stable domain of attraction with a local
regularity assumption; Stufler, Gibbs partitions: a comprehensive phase diagram (arXiv 2204.06982),
regular composition schemes; Bialas-Burda-Johnston, On random allocation models in the thermodynamic
limit (arXiv 2307.14466, PRE 2023), a physics treatment of the same model with regular weights;
Armendariz-Loulakis (PTRF 2011) and Denisov-Dieker-Shneer (AoP 2008), the big-jump principle for
subexponential sums, which is the regular-weight version of the phenomenon. The problem remains open
in the literature as far as I could find. Janson's home page could not be fetched (certificate error).

## Files

memo.md (this), source_text.txt (extracted PDF), f0059_dp.py, f0059_experiment.py, experiment_out.txt,
citations.json (Semantic Scholar), U_F0059.lean (copy of ~/erdos_fc/Prob1000/U_F0059.lean),
lean_compile_*.txt.
