# T115: the Gotsman–Linial bound on average sensitivity of polynomial threshold functions

Checked 12 Nov 2026. Status of the row: **solved in its asymptotic form; the proof was read in full and holds.**

## What is claimed

OpenAI, "Average sensitivity of polynomial threshold functions", 25 September 2026, 13 pages
(repository openai/math at commit 1581d4cb, `preprints/Average-Sensitivity-of-Polynomial-Threshold-Functions-September-25-2026/main.pdf`; not on arXiv).

Theorem 1. For n ≥ 1, 1 ≤ d ≤ n, p a real multilinear polynomial of degree at most d and f = sgn(p) on {−1,1}^n
with sgn(0) = 1, the average sensitivity satisfies I(f) ≤ 8 d √n.

This is the asymptotic form I(f) = O(d √n) of the conjecture of Gotsman and Linial (Combinatorica 1994). The exact form
(the symmetric function with roots between the central levels is the maximizer) is false: Chapman 2018 (arXiv 2108.02288)
and, for quadratics with n odd, Kim–Maldonado–Wellens. The symmetric examples give I ≈ d √(2n/π) ≈ 0.80 d √n for d small
against √n, so the order is sharp and the constant lies between 0.80 and 8.

Earlier bounds: Harsha–Klivans–Meka and Diakonikolas–Raghavendra–Servedio–Tan (2009), n^{1−1/O(d)}; Kane (2012),
√n (log n)^{O(d log d)} 2^{O(d² log d)}.

## The proof, as checked

Every step of Sections 2–5 was verified by hand.

1. Lemma 2 (one-sided coupling). U, V with the same law, mean m, variance σ², and V − U ≤ a almost surely. With
   g(t) = (t − m)|t − m|/2 one has (v − u)²/4 ≤ g(v) − g(u) ≤ (v − u)(|u − m| + |v − m|)/2 for u < v. Since
   E g(U) = E g(V), E|g(V) − g(U)| = 2 E (g(V) − g(U))₊ ≤ a E(|U − m| + |V − m|) ≤ 2aσ, and (U − V)² ≤ 4|g(U) − g(V)|.
   Hence E(U − V)² ≤ 8aσ. Both increment bounds, the cancellation and the Cauchy–Schwarz step are correct.

2. Weighted grading. For a positive weight w on the cube, D = multiplication by √w, K_k = D V_k (V_k = functions of
   Fourier degree ≤ k), E_k = K_k ⊖ K_{k−1}, dim E_k = C(n,k), M = Σ (k − n/2) Π_k. Then ‖M‖²_HS = nN/4 (N = 2^n), and
   multiplication Z_i by a coordinate satisfies Π_s Z_i Π_r = 0 for |s − r| > 1 (Z_i commutes with D, raises degree by at
   most one, and is self-adjoint).

3. Lemma 3. C_i = [M, Z_i] has blocks (s − r) Π_s Z_i Π_r; the averaging Z_i ↦ (Z_i − J Z_i J)/2 with J = Σ (−1)^k Π_k
   keeps exactly the blocks with |s − r| = 1, and conjugation by W = Σ i^k Π_k turns it into i C_i, so ‖C_i‖_op ≤ 1.
   In the point basis (C_i)_{xy} = (y_i − x_i) M_{xy}, so |M_{xy}| ≤ 1/2 for x ≠ y. Also ‖C_i‖²_HS ≤ N, and summing over i
   gives Σ ρ(x,y) |M_{xy}|² ≤ nN/4 = Σ |M_{xy}|², i.e. the energy at distance ≥ 2 is at most the diagonal energy A₀.
   The total deficit of the edge entries from 1/4 is then at most 2A₀. For h a sign function, H its multiplication
   operator and T = MH + HM, T_{xy} = (h(x) + h(y)) M_{xy}, so ‖T‖²_HS ≥ 4(A₀ + A_h) and the number of ordered
   equal-sign edges satisfies |E_h| ≤ 2 ‖T‖²_HS.

4. Assembly. After adding a small positive constant p has no zero on the cube and f is unchanged. With χ the full
   parity, w = |p|, h = χ f, q = χ p = h w: the equal-sign edges of h are the sensitive edges of f, so I(f) = |E_h|/N;
   q has Fourier support in degrees ≥ n − d, which gives Π_s H Π_r = 0 for r + s < n − d; Π_s T Π_r = (s + r − n) Π_s H Π_r;
   and P(R = r, S = s) = ‖Π_s H Π_r‖²_HS / N is a probability law with both marginals Bin(n, 1/2), because H is unitary.
   With U = S, V = n − R, Lemma 2 (a = d, σ = √n/2) gives ‖T‖²_HS/N = E(R + S − n)² ≤ 4 d √n and I(f) ≤ 8 d √n.

No gap was found. Section 6 (noise sensitivity NS_η(f) ≤ 8√2 d √η by the bucketing reduction of
Diakonikolas–Raghavendra–Servedio–Tan; agnostic learning by L¹ regression): Corollary 4 read and correct given the cited
reduction; Corollary 5 read up to equation (18), the sample-complexity part not read.

## Computer tests (`t115_check.py`, `t115_check.out`)

For n ≤ 64 d² the theorem is weaker than I(f) ≤ n, so the tests target the intermediate statements. Floating point,
n = 2,…,8, 324 polynomials (Gaussian coefficients, sparse, the symmetric examples, integer coefficients with zeros on
the cube), d ≤ 4, plus 240 random positive weights with random sign functions for Lemma 3 as stated.

| statement | result |
| --- | --- |
| w ≡ 1: M = −(adjacency)/2, ‖M‖²_HS = nN/4 | to 1e-13 |
| every off-diagonal entry: \|M_xy\| ≤ 1/2 | largest 0.500000 |
| energy at distance ≥ 2 minus diagonal energy ≤ 0 | largest −1e-16 |
| \|E_h\| ≤ 2 ‖T‖²_HS | largest ratio \|E_h\|/(2‖T‖²) = 0.5000 |
| blocks with r + s < n − d vanish; marginals Bin(n,1/2) | 5e-32; 4e-16 |
| E(R + S − n)² = ‖T‖²/N ≤ 4 d √n | identity to 1e-8; largest ratio 0.272 |
| I(f) = \|E_h\|/N, computed directly from f | to 1e-9 |
| Lemma 2 on 4000 stationary chains with upward jumps ≤ a | largest ratio E(U−V)²/(8aσ) = 0.302 |

`t115_lemma3_const.py` hill-climbs over weights and sign functions on n = 2,…,5 (all sign functions for n ≤ 3):
the largest |E_h|/‖T‖²_HS found is 1.000000, attained by constant h. A search, not a proof; if the constant 2 in
Lemma 3 could be replaced by 1 the theorem would read 4 d √n.

## Formalization

`lean/ComparatorChallenges/GotsmanLinial.lean` in the same repository states the theorem for
`MvPolynomial (Fin n) ℝ`, multilinear, `totalDegree ≤ d`, sign 1 at 0, bound `8 * d * Real.sqrt n`; this matches
Theorem 1. `lean/formalization.yaml` points to `OAI/Combinatorics/GotsmanLinial/Main.lean` (22 files in that folder).
`Main.lean` contains no `sorry` and no `axiom` declaration; the other files were not fetched and nothing was compiled here.

## Reception

Chang, Slote, Tseng, Volberg, Zhang, arXiv 2604.08095v3 (26 Oct 2026) use the result: "solved by OpenAI" (abstract),
"A recent paper by OpenAI [OpenAI] proved Gotsman–Linial conjecture by showing" AS[f] ≤ 8 d √n. arXiv searches of
12 Nov 2026 (`lit/search/s1.xml`, `s2.xml`) show no paper disputing it.

## For the list

Take T115 off the problems to attack: solved (OpenAI, 25 Sep 2026; proof checked here in full, Lean formalization
published). Open next to it: the best constant in I(f) ≤ C d √n (between √(2/π) and 8); the exact maximizer for each
(n, d) after Chapman's counterexamples; dimension-free bounds for small moments of the sensitivity
(Tseng–Volberg, Chang et al.).

Reusable: the one-sided coupling lemma (equal marginals plus a one-sided bound on the displacement bound the mean square
displacement by 8aσ), and the device of grading by degree with respect to an arbitrary positive weight, whose spectrum
is fixed while only its matrix entries move.
