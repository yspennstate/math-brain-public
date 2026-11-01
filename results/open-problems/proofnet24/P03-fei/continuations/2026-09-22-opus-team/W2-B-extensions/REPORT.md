# The entropy-influence inequality for Boolean functions of halfspaces and for block-separable threshold functions

Group W2-B, 23 September 2026.

What is proved, numerical and open.

- Proved, a criterion: F5's rank argument becomes a localization criterion on the derivatives (Theorem 1).
- Proved, closure under Boolean combinations: the criterion survives Boolean combinations at a cost of a factor sqrt(k)·Σ_l β_l (Proposition 2, a round-robin interleaving of the orders).
- Proved, which functions satisfy it: every threshold of a block-separable function sgn(Σ_u P_u(x_u) − θ), and functions F(Q_1, ..., Q_m) of block sums on disjoint groups that change value at most κ times along each axis line (Proposition 3).
- Halfspaces (Corollary 5): every Boolean function of k linear threshold functions satisfies H(f) ≤ C_k I(f), with no condition on the weights; C_2 = 17.715, C_3 = 19.698, C_16 = 27.622, and C_k = 3 log2 k + log2 ln k + O(1). This covers intersections of k halfspaces, depth-two threshold circuits with k bottom gates, and linear decision trees with k nodes.
- PTFs (Corollary 6): a polynomial threshold function whose monomials fall into disjoint groups of at most d variables satisfies H ≤ C I, with C = 16.402, 18.152, 19.715 for d = 2, 3, 4 and C = O(d).
- Limits: the method cannot remove the dependence on k (recursive majority, Proposition 7); removing it at all would prove FEI for every junta.
- F5's Lemma 5: the scalar inequality there was only checked on a grid; it has a two-line proof by concavity (Lemma D).
- Numerical, degree-2 PTFs look like threshold functions: the rank-localization index Φ = min_r Σ_r/I never exceeded 0.755 on general degree-2 PTFs (n ≤ 20); the per-coordinate quantity of Lemma B never exceeded 1.40, against 0.68 for threshold functions. Nothing seen contradicts an extension of the method.
- Numerical, pointwise localization is weaker at small n: with the influence order the pointwise constant reaches 2.24, against 0.87 for threshold functions; the averaged constant stays at most 1.41.
- Numerical, these classes have sharp constants above 4: read-once 2-CNFs are degree-2 PTFs and intersections of halfspaces, and have H/I → 4.8677. F5 conjectured 4 for single threshold functions.
- Open: FEI for general degree-2 PTFs is not proved; Section 6 says where the argument breaks.
- F5 check: no error found in F5's proof; two small points are in Section 7.

## 0. Notation

f: {−1,1}^n → {−1,1}, f = Σ_S f̂(S)χ_S. The spectral sample S has Pr[S = A] = f̂(A)². H(f) = H(S) in bits, I(f) = E|S|, Inf_i(f) = Pr[i ∈ S] = E|D_i f|, where D_i f(x) = (f(x^{i→1}) − f(x^{i→−1}))/2 and D_i f = Σ_{S∋i} f̂(S)χ_{S∖{i}}. sgn(t) = 1 for t > 0 and −1 for t ≤ 0. log is log2, ln is natural.

Units and unit noise. A unit partition 𝒰 of [n] has units of size at most d; u(i) is the unit containing i. For a set P of units and η ∈ [0,1], the noise N_{P,η} maps x to y as follows: independently for each u ∈ P, with probability η, replace x_u by a fresh uniform element of {−1,1}^u; copy all other coordinates. For x uniform:

    (0.1)  E[g(x)g(y)] = Σ_T ĝ(T)² (1−η)^{b_P(T)},   b_P(T) = #{u ∈ P : u ∩ T ≠ ∅}.

This holds because the pairs (x_u, y_u) are independent over units, and E[χ_A(x_u)χ_{A'}(y_u)] = [A = A'](1−η)^{[u∈P, A≠∅]}.

The Erdős function. Erd(m) = C(m, ⌊m/2⌋)2^{−m}, with Erd(0) = 1. It is nonincreasing, and Erd(m) ≤ min(1, √(2/(πm))) ≤ (2/√π)(m+1)^{−1/2}.

Lemma 0 (Erdős). Let |b_j| ≥ β > 0 for j = 1, ..., m, and let J be an interval of length 2β that is open at one end. Then Pr[Σ b_j ε_j ∈ J] ≤ Erd(m).

Proof. Two comparable distinct sign vectors give sums at least 2β apart, and two points of J are less than 2β apart. So the sign vectors landing in J form an antichain; apply Sperner. □

Lemma 0'. If M stochastically dominates Bin(t, p) with p > 0, then E Erd(M) ≤ (2/√π)((t+1)p)^{−1/2}.

Proof. Since Erd is nonincreasing, the bound for Bin(t, p) suffices. Apply Jensen, and use E[1/(M'+1)] = (1 − (1−p)^{t+1})/((t+1)p). □

## 1. Localization implies the entropy-influence inequality

Definition 1. Let ≺ be a linear order of 𝒰. An initial segment below a unit u is the set of the first t units of ≺, for some 0 ≤ t < rank(u). A function f is β-localized with respect to (𝒰, ≺) if, for every coordinate i, every initial segment P below u(i), every x and every η ∈ (0, 1]:

    Pr_{y∼N_{P,η}(x)}[D_i f(y) ≠ 0] ≤ β (η(|P|+1))^{−1/2}.

A linear threshold function is (2/√π)-localized with respect to singleton units ordered by decreasing |w_j|. This is F5's Lemma 2, and also the case d = κ = m = 1 of Proposition 3.

Theorem 1. Let f be β-localized, with units of size at most d and β ≥ 2/√π. Put

    L = 2 ln(3√3β/2) + 2,    C = 3 + min_{a>1}[1 + ln d + ln(a/(a−1)) + aL]/ln 2   (minimiser: a(a−1) = 1/L).

Then H(f) ≤ C·I(f). For β = 2/√π and d = 1 this gives L = L1 = 4.1511069802 and C = 14.2141880860, which is F5's constant.

In what follows, N_i = rank(u(i)) and P_i denotes the N_i − 1 units before u(i).

Lemma A. Suppose Inf_i > 0, N = N_i ≥ 2 and g = D_i f. For 0 < c ≤ N,

    Σ_T ĝ(T)²(1 − c/N)^{b_{P_i}(T)} ≤ βc^{−1/2}Inf_i.

Proof. Take η = c/N in (0.1). The left side is E[g(x)g(y)] ≤ E[|g(x)| Pr[g(y) ≠ 0 | x]] ≤ β(ηN)^{−1/2}E|g| = βc^{−1/2}Inf_i. □

Lemma B. Σ_{T∌i} f̂(T+i)² ln(N_i/(b_{P_i}(T)+1)) ≤ L·Inf_i.

Proof. If N = 1, the left side is 0. Otherwise let ν(T) = f̂(T+i)²/Inf_i and b = b_{P_i}(T) ∈ [0, N−1]. For real K ≥ 1 apply Lemma A with c = N/(3K):

      ν(b ≤ K) ≤ (1 − 1/(3K))^{−K} β(3K/N)^{1/2} ≤ B_β(K/N)^{1/2},   B_β = (3√3/2)β.

The last step holds because −K ln(1 − 1/(3K)) is nonincreasing in K and equals ln(3/2) at K = 1. Since B_β > 1:

      E_ν ln(N/(b+1)) = ∫_0^{ln N} ν(b+1 < Ne^{−u}) du ≤ ∫_0^∞ min(1, B_β e^{−u/2}) du = L.  □

Lemma C. Σ(f) := E_S Σ_{i∈S} ln+(N_i/|S|) ≤ L·I.

Proof. Let i ∈ S and T = S∖{i}. Each unit of P_i met by T contains an element of T, so b_{P_i}(T) + 1 ≤ |S|; also b + 1 ≤ N_i. Hence ln+(N_i/|S|) ≤ ln(N_i/(b+1)). Sum over pairs (i, S) and apply Lemma B. □

Lemma D (O'Donnell–Wright–Zhou). H(|S|) ≤ 3I.

Proof.
1. Let ε = Var f. Then H(|S|) = h(ε) + ε·H(|S| | S ≠ ∅).
2. ε·H(|S| | S ≠ ∅) ≤ I, by Gibbs' inequality against the law 2^{−k}.
3. (1−ε)log(1/(1−ε)) ≤ ε/ln 2 < 2ε.
4. It remains to show ε log(1/ε) + 2ε ≤ 2I. Let p = min Pr[f = ±1] and u = 2p ∈ (0,1]; then ε = u(2−u). Edge isoperimetry gives I ≥ u log(2/u). After dividing by u, the claim reads ψ(u) ≥ 0 with ψ(u) = (u/2)log(1/u) + (1 − u/2)log(2−u) + u − 1.
5. ψ(0+) = ψ(1) = 0, and ψ''(u) = −(1−u)/(u(2−u)ln 2) ≤ 0. So ψ is concave and hence nonnegative on (0, 1]. □

Lemma E (rank-weighted entropy over units). For injective unit ranks ρ and a > 1:

    H(S | |S|) ≤ (1/ln 2)[ln(eda/(a−1))·E|S| + a·E Σ_{i∈S} ln+(ρ(i)/|S|)].

Proof. Follow F5's Lemma 6 with q_k(s) = min(1, (k/ρ(s))^a). Units carry at most d coordinates and their ranks are distinct, so Σ_s q_k(s) ≤ d·Σ_{t≥1} min(1,(k/t)^a) ≤ dka/(a−1). □

Proof of Theorem 1. H(f) = H(|S|) + H(S | |S|). Apply Lemma D to the first term and Lemmas E and C to the second. □

Remark 1.1. Lemma A uses the localization only through the average E_x[|D_i f(x)| Pr[D_i f(y) ≠ 0 | x]], and only for P = P_i. So Theorem 1 holds under an averaged hypothesis with any exponent γ ∈ (0,1]; then L = (ln B + 1)/γ with B = (3/2)3^γβ. The pointwise form is needed only for Proposition 2.

## 2. Boolean combinations: interleaving the orders

Proposition 2. Suppose each h_l is β_l-localized with respect to (𝒰, ≺_l), for l = 1, ..., k. Let ≺* be the round-robin interleaving: in each round, for l = 1, ..., k in turn, place the ≺_l-first unit not yet placed. Then every f = G(h_1, ..., h_k) is β*-localized with respect to (𝒰, ≺*), where β* = √k·Σ_l β_l. With a common order, the factor √k is not needed.

Proof.
1. After s complete rounds, the first s units of every ≺_l are placed. By induction: if the s-th unit of ≺_l is unplaced when l's turn comes in round s, it is the ≺_l-first unplaced unit, so l places it.
2. Let P* be an initial segment below u(i) with |P*| = t, and put s = ⌊t/k⌋. The first s rounds lie inside P*. So the first s units of each ≺_l form an initial segment P_l ⊆ P* below u(i).
3. If D_i f(y) ≠ 0, then D_i h_l(y) ≠ 0 for some l.
4. Condition on the independent noise on P* ∖ P_l. What remains is N_{P_l,η} noise started from a fixed point, so the bound is β_l(η(s+1))^{−1/2}.
5. Sum over l and use s + 1 ≥ (t+1)/k. □

## 3. Separable threshold functions are localized

Definition 3. h is (κ,m)-separable over 𝒰 if 𝒰 is split into m groups 𝒢_l, each unit u carries a real function P_u: {−1,1}^u → R, h = F(Q_1, ..., Q_m) where Q_l = Σ_{u∈𝒢_l} P_u(x_u), and every axis-line restriction t ↦ F(..., t, ...) is piecewise constant with at most κ changes of value.

The range of a unit is s(u) = max P_u − min P_u. The canonical order sorts each group's units by decreasing range, then interleaves the m groups round robin.

Examples: sgn(Σ_u P_u − θ) is (1,1)-separable, and a linear threshold function is the case d = 1; G(w·x), where G changes sign κ times, is (κ,1)-separable; sgn(P(Q_1, ..., Q_m)), where P has degree ≤ D in each variable, has κ ≤ D.

Proposition 3. A (κ,m)-separable h is β-localized with respect to its canonical order, with β = κ√m·(2/√π)·2^{(d−1)/2}.

Proof. Take u_0 = u(i) ∈ 𝒢_l and an initial segment P below u_0 with |P| = t.
1. Setup. P ∩ 𝒢_l is the first s_l ≥ ⌊t/m⌋ units of group l, and each of them has range at least s(u_0).
2. Fix everything outside group l. Condition on the noise in the other groups. This fixes φ(t) := F(..., t, ...) in position l.
3. Reduce to an interval condition. Write Q_l = P_{u_0} + R. The values a < a' of P_{u_0} at x^{i→±1} are fixed. D_i h(y) ≠ 0 means φ(R+a) ≠ φ(R+a'). Then some change point τ_j of φ separates R + a from R + a'. So R lies in one of at most κ intervals, each of length a' − a ≤ s(u_0) and open at one end: [τ_j − a', τ_j − a) or (τ_j − a', τ_j − a].
4. Mixture decomposition. A re-randomized unit u takes the value P_u(Z_u). With λ_u = 2^{1−|u|}, this equals ζ_u(c_u + (s(u)/2)ε_u) + (1−ζ_u)Ξ_u, where ζ_u ~ Bernoulli(λ_u) and ε_u is uniform on {±1}; Ξ_u has the law of P_u at a uniform point other than one maximiser and one minimiser; all of these are independent.
5. Erdős bound. Given everything except the ε_u, R is a constant plus a Rademacher sum with coefficients s(u)/2 ≥ (a'−a)/2 > 0. Lemma 0 and a union over the κ intervals give a bound of κ·E Erd(|M|).
6. Count. |M| dominates Bin(s_l, η2^{1−d}). Apply Lemma 0' and s_l + 1 ≥ (t+1)/m. □

## 4. Consequences

Theorem 4. Let h_1, ..., h_k be (κ,m)-separable over a common 𝒰 (units of size ≤ d), and let G: {−1,1}^k → {−1,1}. Then G(h_1, ..., h_k) satisfies H ≤ C·I with

    L = L1 + 3 ln k + 2 ln κ + ln m + (d−1) ln 2   and C as in Theorem 1.

With a common canonical order, 3 ln k becomes 2 ln k. If the h_l use different partitions, pass to the coarsest common coarsening.

Corollary 5 (halfspaces). For arbitrary linear threshold functions h_1, ..., h_k and any G: {−1,1}^k → {−1,1}:

    H(G(h_1, ..., h_k)) ≤ C_k·I,   C_k = 3 + min_a[1 + ln(a/(a−1)) + a(L1 + 3 ln k)]/ln 2.

This covers intersections of k halfspaces, depth-two threshold circuits with k bottom gates, linear decision trees with k nodes, and decision lists of k halfspaces. It removes the co-monotonicity assumption of F5's Corollary 2, at the cost of 3 ln k instead of 2 ln k in L.

Corollary 6 (polynomial threshold functions). Let f = sgn(p).
- (a) Block-separable. If the monomial hypergraph of p has components of at most d vertices, then L = L1 + (d−1) ln 2 (and ln d enters C). This gives C = 16.402, 18.152, 19.715, 22.557 for d = 2, 3, 4, 6.
- (b) Products of affine forms. If p = Π_{j≤D}(L_j − θ_j), then f is a Boolean function of 2D halfspaces, so C = C_{2D}.
- (c) Small vertex cover, degree 2. If every quadratic monomial meets a set of s variables, then f is a Boolean function of s + 2^s halfspaces: C = 19.698 for s = 1 and 23.019 for s = 2.
- (d) Polynomials of linear forms on disjoint variables. If p = P(L_1(x^{(1)}), ..., L_m(x^{(m)})) with disjoint variable sets and P of degree ≤ D in each variable, then L = L1 + 2 ln D + ln m. This gives C = 15.402 for sgn(L_1 L_2 − θ) and 17.715 for a disc.
- (e) A small backdoor. If deleting s variables leaves components of at most d vertices, then L = L1 + 3 ln(s + 2^s) + (d−1) ln 2.

Constants (`code/constants.py`, `logs/constants.log`):

| class | C |
|---|---|
| one halfspace (F5) | 14.2142 |
| Boolean function of k halfspaces, k = 2 / 3 / 4 / 8 / 16 / 100 / 1000 | 17.715 / 19.698 / 21.085 / 24.379 / 27.622 / 36.049 / 46.464 |
| same, co-monotone weights (reproduces F5's Corollary 2) | 16.567 / 17.909 / 18.850 / 21.085 / 23.287 / 29.003 / 36.049 |
| block-separable PTF, d = 2 / 3 / 4 / 6 / 10 | 16.402 / 18.152 / 19.715 / 22.557 / 27.700 |

## 5. Limits of the method

Proposition 7. R_m = Maj_3^{∘m} is a Boolean function of k = 3^{m−1} halfspaces (its bottom gates). For every ordering r of the coordinates,

    Σ_r/I ≥ m ln 2 − 1 − ln 2 = (ln 2/ln 3)·ln k − 1.

Proof. The automorphism group is transitive on the leaves, so Σ_r/I ≥ ln(n/e) − ln E_sb|S|, where E_sb is the size-biased law of |S| (F5, Remark 2). The spectral sample is a Galton–Watson tree with offspring 1 (probability 3/4) or 3 (probability 1/4). So E|S| = (3/2)^m and E|S|² = 2(9/4)^m − (3/2)^m, which gives E_sb|S| ≤ 2(3/2)^m. □

So the coefficient 3 on ln k is within a factor 4.75 of what the rank method can reach on this class. Separately, dictators are halfspaces, so a k-independent constant would be FEI itself. For k-juntas alone, the trivial bound (3 + log(ek))·I is better than C_k; Corollary 5 matters because the number of variables n is unrestricted.

## 6. General polynomial threshold functions

6.1 Where the argument stops. Write p = x_i q_i + r_i. Then D_i f ≠ 0 exactly when r_i ∈ (−|q_i|, |q_i|]. For threshold functions, q_i = w_i is constant, and every heavier coordinate moves r_i by at least 2|w_i|. For degree ≥ 2, the width |q_i(y)| is a random polynomial of degree d − 1, and the steps ∂_j r_i(y) also depend on y; no order makes the steps dominate the width pointwise. Meka–Nguyen–Vu-type anti-concentration works at a fixed scale; here the scale is random and correlated with the event, since conditioning on the derivative set favours large |q_i|.

Conjecture (conjectural). For degree-d PTFs, the averaged localization of Remark 1.1 holds with the influence order, with constants β_d and γ_d. By Theorem 1 this would give H ≤ C_d·I.

6.2 Numerics (numerical, exact Walsh transforms). Φ = min_r Σ_r/I is computed exactly. Σ_r is a sum of costs c_i(r(i)), with c_i(t) = Σ_{S∋i} f̂(S)² ln+(t/|S|), so minimizing over orders is an assignment problem.

| family (degree 2 unless stated) | n | Φ | Σ_{influence order}/I | H/I |
|---|---|---|---|---|
| dense Gaussian quadratics | 12 / 18 / 20 | ≤ 0.49 / ≤ 0.57 / ≤ 0.58 | within 0.01 of Φ | 2.39–3.70 |
| geometric-scale dense quadratics | 12 / 18 | ≤ 0.30 | ≤ 0.32 | 1.83–2.22 |
| cycle or path, equal weights | 12 / 18 / 20 | 0.61–0.64 / 0.747 / 0.755 | = Φ | 2.05–2.58 |
| cycle or path, Gaussian or geometric weights | 12 / 18 | ≤ 0.38 | ≤ 0.38 | 1.48–2.09 |
| random sparse (3 edges per vertex) | 12 / 18 / 20 | ≤ 0.42 / ≤ 0.42 / 0.35 | ≤ 0.42 | 1.93–2.90 |
| L_1 L_2 − θ, opposite weights | 12 / 18 | ≤ 0.30 | ≤ 0.30 | 1.99–2.43 |
| discs (opposite or rotated weights) | 12 / 18 | ≤ 0.32 | ≤ 0.32 | 2.07–2.91 |
| rank-3 quadratic forms | 12 / 18 | ≤ 0.47 | ≤ 0.47 | 2.24–2.77 |
| block-separable controls; read-once 2-CNF with m = 10 | 12–20 | ≤ 0.39; 0.862 | = Φ | up to 4.52 |
| annealing on Φ | 12 | 0.605 | 0.615 | 2.96 |
| majority (exact level formula), n = 17 / 101 / 10^6+1 | – | 0.585 / 0.749 / 0.885 | = Φ | 2.40 / 2.73 / 2.88 |

Localization with the influence order (n = 10–14; the second and third columns are the constants β from Definition 1 and Remark 1.1):

| family | max Q_i (Lemma B) | pointwise β | averaged β |
|---|---|---|---|
| threshold functions | 0.681 | 0.866 | 0.859 |
| dense quadratics | 1.095 | 2.236 | 1.057 |
| geometric-scale quadratics | 0.896 | 1.732 | 1.407 |
| x_0·(sum over K) + a small linear form | 0.946 | 1.732 | 1.214 |
| annealing maximiser of Φ | 1.397 | 1.817 | 1.162 |

A direct annealing on Q_max over dense quadratics (n = 12) found only 1.260, so that search was not strong. In a dense quadratic at n = 14, a whole 4-dimensional subcube of a coordinate's predecessors lies inside its derivative set, so the pointwise property is weaker for degree 2 than for threshold functions.

6.3 Sharp constants of these classes (exact). AND_m(OR_k) is a degree-k PTF, block-separable, and an intersection of m halfspaces. H/I from the product formula (checked against the Walsh transform for k = 2, m ≤ 10 and k = 3, m ≤ 6):

| k | m = 6 | m = 20 | m = 100 | m = 10^4 | limit |
|---|---|---|---|---|---|
| 2 | 3.97229 | 4.77507 | 4.85095 | 4.86750 | (log(4/3) + h(1/4) + ¼·log 3)/(1/3) = 4.867669 |
| 3 | 3.43877 | 4.78343 | 5.04726 | 5.07301 | 5.073268 |

So the sharp constant for degree-2 PTFs, and for intersections of halfspaces, is at least 4.8677; for degree 3 it is at least 5.0733. Annealing found H/I = 4.0112 at n = 12; the maximiser is exactly the read-once formula x_7 x_11 ¬x_0 ¬x_2 ¬x_6 ¬x_8 ¬x_9 (x_4 → x_1)(x_5 ∨ (x_10 ∧ ¬x_3)), with 15 true points (verified).

## 7. On F5's proof

Every step of F5's Theorem 1 and Corollary 2 checks out. Lemma 5 rested on a grid check of a one-variable inequality that has equality at both ends of (0, 1], so a grid cannot settle it; Lemma D above proves it. F5's majority value at n = 17 is H/I = 8.00811/3.33847 = 2.39874, not 2.3989. Theorem 4 with a common order reproduces F5's C_k exactly.

## 8. Tests of the proofs

| test | result | log |
|---|---|---|
| Proposition 2 for halfspaces: exact pointwise probabilities, 115 functions of 2–3 halfspaces with reversed or random weight orders, n = 8–14 | 4452 tests, 610 with a bound below 1, worst ratio probability/bound 0.542 | check_thmA.log |
| Adversarial annealing against that step (n = 9, 300 steps) | worst ratio 0.833 | adv_thmA_n9_s3.log |
| Lemma B / Lemma C / Corollary 5 on those functions | max Q/L = 0.184, max Σ/(L·I) = 0.106, max H/(C_k·I) = 0.204 | check_thmA.log |
| Proposition 3 (block-separable, d = 2 and 3; hyperbola, disc, annulus) and Proposition 2 on a common partition | 7092 tests, 4981 with a bound below 1, 0 violations; worst ratio 1.0000 (equality in Erdős at m = 1) | check_thmB.log |
| Lemma B / Lemma C / Theorem 4 on those classes | max Q/L = 0.202, max Σ/(L·I) = 0.090, max (H/I)/C = 0.239 | check_thmB.log |

The pointwise tests compare the exact function x ↦ Pr[D_i f(y) ≠ 0] with the bound the proof establishes before its final Jensen step. At these sizes the final bounds exceed 1 and carry no information.

## 9. Files and literature

Files in `W2-B-extensions/code/`: `fei_lib.py` (shared routines: Walsh transform, H and I, exact minimisation over orders, unit noise, round-robin order); `check_thmA.py`, `check_thmB.py`, `adv_thmA.py` (the tests in Section 8); `ptf_explore.py`, `ptf_localization.py`, `anneal_q.py`, `ptf_n20.py` (the degree-2 numerics in Section 6.2); `sym_phi.py` (majority by the exact level formula); `cnf_ratio.py` (the read-once CNFs in Section 6.3); `constants.py` (all constants); `selftest.py` (agreement with F5's values). Outputs, and the annealing maximisers (`.npz`), are in `logs/`.

Literature. Chakraborty, Kulkarni, Lokam and Saurabh: an absolute O_d(n^{1−1/(4d+6)}) entropy bound for PTFs. Chakraborty et al.: FEI for random threshold functions (arXiv:1903.11635). O'Donnell, Wright and Zhou: FEI for symmetric and d-part-symmetric functions. O'Donnell and Tan: FEI for read-once formulas. No earlier FEI result for intersections of halfspaces or depth-two threshold circuits was found, nor one stated for PTFs as a class, although some degree-2 PTFs were already covered: symmetric ones, and read-once CNFs.
