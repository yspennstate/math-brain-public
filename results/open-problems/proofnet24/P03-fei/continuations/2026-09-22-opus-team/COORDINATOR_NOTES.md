# Coordinator's notes: routes tried and closed, 23 September 2026

Short records of ideas for the full conjecture that were tested and did not survive, so they are not tried again,
and two reformulations that are equivalent to FEI (useful as restatements, not as progress). Scripts:
`audit/creative/` (copied from the coordinator's scratch folder).

## 1. Reducing FEI to monotone functions by compressions (REFUTED as a local lemma)

The i-compression C_i sorts every edge {x, x^i} so that the function becomes monotone in x_i. It never increases total
influence. If every compression satisfied H(f) - H(C_i f) <= K (I(f) - I(C_i f)), iterating compressions would reduce
FEI for all functions to FEI for monotone functions. Exhaustively over all 65,536 functions of four variables and all
four coordinates (`compress_test.py`, `compress_test2.py`):

- whenever the compression lowers the total influence, the entropy lost is at most 4 times the influence lost, and 4 is
  attained;
- but some compressions leave the total influence unchanged and lower the entropy by one bit, and 1,536
  (function, coordinate) pairs do so in both directions (up and down compression), so no choice of direction helps.
  Example: the function whose true set is {3, 5, 6, 8} (bit i of the index is x_i), coordinate 3: H = 3, I = 2 before;
  H = 2, I = 2 after either compression (`compress_example.py`).

These functions are far from extremal (H/I = 1.5), so the obstruction is to the local lemma, not to a monotone reduction
in some other form; a reduction would need a potential that pays for influence-neutral entropy loss.

## 2. The spectral sample and the sensitive set (REFUTED)

Coupling the spectral sample S with the set Sens(x) of sensitive coordinates at a uniform point x would help only if
H(Sens(x)) <= C E|Sens(x)| = C I. For the function that is true at one point, Sens(x) is empty except at that point
(all n coordinates) and at its n neighbours (one coordinate each), so H(Sens) is about n^2 2^-n while I = 2n 2^-n:
the ratio grows like n/2.

## 3. A per-coordinate form (REFUTED) and why the weighting matters

Writing H = sum_S fhat(S)^2 log2(1/fhat(S)^2) and distributing each term evenly over the elements of S gives the exact
identity

    H(f) = phi(fhat(empty)^2) + sum_i Inf_i Q_i(f),   Q_i(f) = E[ log2(1/fhat(S)^2) / |S| | i in S ],

with phi(t) = t log2(1/t) (the empty-set term is at most (log2 e)(1 - fhat(empty)^2) <= (log2 e) I),

where the conditional law of S minus i given i in S is the normalised spectrum of the derivative D_i f, a
{0, +1, -1}-valued function. A uniform bound Q_i <= C would imply FEI, but it fails: for f = x_1 ? Maj(x_2..x_n) : c the
level-one part of the majority gives Q_1 of order log n. FEI survives there only because the other coordinates carry
influence of order sqrt n. Any per-coordinate statement has to be weighted, which is the whole difficulty.

## 4. A metric relaxation (REFUTED)

The autocorrelation R(A) = E f(x) f(x xor A) is the Fourier transform of the spectral law, 1 - R is twice a
subadditive "cut" semimetric d(A) = P(f(x) != f(x xor A)), and I = sum_i d(e_i). Keeping only positive definiteness of
R and subadditivity of d is too weak: d(A) = |A|/n is such a semimetric (the uniform law on singletons), with entropy
log n and I = 1. Booleanity has to be used through more than the metric structure of d.

## 5. Two reformulations equivalent to FEI (not progress, recorded for use)

(a) Local log-ratio form. Splitting the erasure entropy B = sum_i H(1[i in S] | S minus i) edge by edge, the upward
part is at most (log2 e) I, so FEI is equivalent, up to additive changes of the constant, to

    E_{S ~ fhat^2} sum_{i in S} log2(1 + fhat(S minus i)^2 / fhat(S)^2) <= K E|S| :

a typical spectral set is, on the log scale and on average over its elements, not much lighter than its lower
neighbours. (The equivalence uses the erasure reduction, solo-2026-09-17/ERASURE_REDUCTION.md, and B <= H.)

(b) Complementary supports. For Boolean f and each i, E_i f = (f_0 + f_1)/2 and D_i f = (f_0 - f_1)/2 are
{0, +1, -1}-valued with disjoint supports and (E_i f)^2 + (D_i f)^2 = 1; the i-th erasure term compares the spectra of
this complementary pair on the same set T. The flip coordinates of bent-plus-flip and of Numaro's function are exactly
the coordinates where the pair's spectra have very different scales.

## Two quick conjectures about threshold functions, both false (23 September)

Script: audit/creative/ltf_vs_chain.py (17,125 threshold functions, n from 3 to 14, five weight families, seed 1).

1. "Among threshold functions of the same bias P, the AND/OR chain minimizes the defect D = 4I - H." If true, the chain theorem would give H <= 4I for every threshold function. It fails. With weights (1, 2, 4, 8, 16, 32, 64, 86) and threshold 106, P = 0.5078125 and D = 3.4547, which is 0.4417 below the chain value at the same P. The function's H/I is only 1.894, so this says nothing against H <= 4I. It only rules out a proof that runs through a potential depending on the bias alone.
2. "Balanced threshold functions satisfy H <= 4(I - 1)." This fails at n = 8. With weights (1000, 693, 480, 333, 231, 160, 111, 76) and threshold 1535, the function is balanced and has H/(I - 1) = 4.5336. Amplification does not turn this into anything about threshold functions, because the O'Donnell-Tan tower of a threshold function is not a threshold function. So H <= 4I for threshold functions stays open, and the sharp amplification value for balanced threshold functions is at least 4.53.

## AND-run amplification: a necessary condition for H <= 4I, and it holds on threshold functions (23 September)

For any g and fresh variables, the one-step identity iterates to D(AND_l ∧ g) = 2^(-l) [D(g) + 2 S_l(p)] and
I(AND_l ∧ g) = 2^(-l) [I(g) + 2 l p], where p = Pr[g = 1] and S_l(p) = Σ_{i<l} 2^i ε(2^(-i) p). For l ≥ 1 the partial sums S_l decrease to
E(p) = Σ_{i≥0} 2^i ε(2^(-i) p), because every term after the first has an argument below 1/2. The same holds with 1 - p
for OR runs. Threshold functions are closed under both operations, so H <= 4I on threshold functions requires

  D(g) + 2 min(0, E(p)) >= 0   and   D(g) + 2 min(0, E(1 - p)) >= 0   for every threshold function g.

E(1/2) = -1/ln 2 exactly. This follows from the closed form of AND_n, where 2^n D(AND_n) → 8 - 4/ln 2. So a balanced member of any class
closed under these operations must satisfy 4I - H >= 2/ln 2 = 2.885 before H <= 4I can hold on the whole class. The test is much more
sensitive than H/I itself, because the amplification turns a small shortfall into an actual violation. On 44,000 cases (random
threshold functions with n from 3 to 14, both sides) the condition held, with minimum +1.4e-4 at a nearly constant function
(audit/creative/and_amplify.py). One case was checked directly (audit/creative/verify_ltf4.py): g = [w·x >= 921] with
w = (1000, 595, 354, 211, 125, 75, 44, 26, 15, 9, 5, 3, 1, 1), p = 0.66656, D(g) = 2.16480. Exact Walsh sums for AND_l ∧ g,
l = 1..8, give 4I - H = 2.163, 0.830, 0.277, 0.0883, 0.0279, 0.00898, 0.00303, 0.00109 and H/I = 3.977 at l = 8. The limit of
2^l D is D(g) + 2E(p) = +0.145, so this g stays below 4.

Two numerical traps, both hit here. (1) ε(p) computed from the closed form with log2(1/w) loses all its digits for p below about
2^(-40), because two O(p) terms cancel to O(p^2); summed with weights 2^i over 80 terms the error reaches order 1 (it produced E(1/2) = 0).
Write the two terms with log1p. (2) For p > 1/2 the term φ((1-2p)^2)/2 is not zero; it uses |1-2p| = 2p-1. Dropping it made E(0.667) wrong by
0.18 and produced a false "violation", which the direct computation above refuted.

## A potential that depends only on the bias is not enough (23 September)

Let Λ(p) = max(0, -2E(p), -2E(1-p)). The amplification condition above says D(f) >= Λ(Pr[f = 1]) for every threshold function if
H <= 4I holds on the class. Numerically it does hold (minimum D - Λ = +5.4e-4 over the functions tested; audit/creative/lambda_induct.py).
To prove it by induction on the number of variables, one would restrict a variable i, with f0 and f1 again threshold functions with the same
weights, and need Q_i = (Λ(p0) + Λ(p1))/2 + [D(f) - (D(f0) + D(f1))/2] - Λ(p) >= 0 for some i. That fails. With weights (1, 2, 5, 8, 11)
and threshold 16 (p = 0.406) the best variable gives Q = -0.092, and splitting on the heaviest variable can give -0.160
(weights (18, 19, 26, 30, 4), threshold 31). So an inductive proof of H <= 4I for threshold functions along restrictions needs a
potential that depends on more than the bias, for example on the bias and the total influence, or on the whole threshold profile
t -> [w·x >= t] of the weight vector. The chain proof avoided this because a chain's restriction to its outermost variable always has a
constant branch.

Mixed extensions add nothing. Allowing any finite mixture of AND and OR steps with fresh variables on top of g, the least admissible
defect M(p) satisfies M(p) = max(0, 2(M(p/2) - ψ(p/2)), 2(M((1+p)/2) - ψ((1+p)/2))). Unrolled to depth 12 with Λ at the leaves, it
equals Λ at every point tested (p = 1/2, 1/4, 3/4, 1/8, 3/8, 0.406, 0.667, 0.9, 0.99; audit/creative/bellman_ext.py). This fits the
recursion E(p) = ε(p) + 2E(p/2). So D(g) >= Λ(Pr[g = 1]) is the whole content of "no chain extension of g exceeds 4I", and
M(1/2) = Λ(1/2) = 2/ln 2 = 2.885.
