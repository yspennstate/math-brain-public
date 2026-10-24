# F4: the general conjecture through the coordinate-restriction step

22–23 September 2026. FEI is neither proved nor refuted here.

Proved:
- FEI is equivalent to FEI for functions all of whose influences lie below any fixed threshold τ. A violation always localizes to a subcube restriction with uniformly tiny influences on which the restriction step fails at every coordinate (Theorem 2.1, Corollary 2.2).
- Exact laws for the erasure entropy and for the restriction drop under disjoint composition (Theorems 3.1, 4.1).
- Three strengthenings of the erasure route are false (Section 6).
- A refinement of Han's bound (Proposition 6.4).

Certified (outward-rounded interval arithmetic, standalone checker), on the self-compositions of Numaro's g on 324, 5832 and 104976 variables:

| variables | rho_0 = min_i Delta_i/Inf_i | B/I | min_i B_i/Inf_i |
|---|---|---|---|
| 324 | 6.3290 | 3.9674 | 3.9166 |
| 5832 | 6.8901 | 4.4074 | 4.3676 |
| 104976 | 7.0519 | 4.5388 | 4.5049 |

Previously recorded values in this repository were 6.3164 for rho_0 and 3.698 for B/I.

Numerical: along the same tower, rho_0 → 7.11162, B/I → 4.58825 and min_i B_i/Inf_i → 4.55771, while H/I → 6.52185.

Consequences:
- The potential-free restriction induction cannot give a constant below 7.05.
- A measure-only potential for that induction needs a convex corner at p = 1/2 if its constant is below 7.05.
- The erasure routes need a constant of at least 4.50.
- Nothing here changes the known bounds on the FEI constant itself.

## 0. Notation and facts used

Basic quantities:
- f: {-1,1}^n → {-1,1}, p_S = f̂(S)^2, H = Σ p_S log2(1/p_S), I = Σ|S| p_S, and Inf_i = Σ_{S∋i} p_S.
- S is the spectral sample, φ(t) = t log2(1/t), and h2 is the binary entropy.
- E(x,y) = φ(x) + φ(y) − φ(x+y). It is 1-homogeneous and nonnegative.

Coordinate quantities. Fix a coordinate i and a set T ∌ i.
- u_T = f̂(T) is a coefficient of E_i f, and v_T = f̂(T∪i) is a coefficient of D_i f.
- f_± are the restrictions x_i = ±1, with coefficients u ± v and spectra p_±.
- B_i = H(1_{i∈S} | S∖{i}) = Σ_T E(u_T^2, v_T^2), and JS_i = JS(p_+, p_−).

Identities used from solo-2026-09-17/ERASURE_REDUCTION.md, (1) and (4):
- Delta_i = H(f) − (H(f_+)+H(f_−))/2 = JS_i + B_i.
- I(f) = Inf_i + (I(f_+)+I(f_−))/2.

Further facts and definitions:
- B = Σ B_i ≤ H by Han's inequality.
- rho_0(f) is the minimum of Delta_i/Inf_i over the relevant coordinates.
- The composition identity is the one in CONTEXT.md §3.

## 1. The restriction step in sign-free form

Lemma 1.1 (proved; (b)–(c) are close to continuations/2026-09-20-concave-restriction).

(a) B_i = h2(Inf_i) − I(1_{i∈S}; S∖{i}).

(b) η_i := Σ_T min(u_T^2, v_T^2) = (1 − Σ_T √(p_+(T) p_−(T)))/2 ≤ min(Inf_i, 1/2).

(c) JS_i ≤ (2/ln 2) η_i and B_i ≤ h2(η_i).

(d) Delta_i, JS_i, B_i and η_i depend only on the pair (p_+, p_−). By contrast Inf_i = (1 − ⟨f_+, f_−⟩)/2 depends on signs:
- Inf_i = Σ_{|u|≥|v|} v^2 + Σ_{|u|<|v|} v^2;
- η_i = Σ_{|u|≥|v|} v^2 + Σ_{|u|<|v|} u^2.

For an odd function η_i = Delta_i = 0 at every coordinate.

Proof.
- (a) This is the definition of mutual information, since H(1_{i∈S}) = h2(Inf_i).
- (b) We have ||u+v| − |u−v|| = 2 min(|u|,|v|), so min(u^2,v^2) = (|α|−|β|)^2/4 with α = u+v and β = u−v. Summing gives (Σα^2 + Σβ^2 − 2Σ|αβ|)/4 = (1 − Σ√(p_+ p_−))/2. Also η_i ≤ Σv^2 = Inf_i, and 2η_i ≤ Σ(u^2+v^2) = 1.
- (c) The first inequality is (2) of ERASURE_REDUCTION. For the second, write B_i = Σ_T m_T h2(q_T) with m_T = u_T^2 + v_T^2 and q_T = min(u_T^2,v_T^2)/m_T. Here m is a probability vector and the m-mean of q is η_i; now use the concavity of h2.
- (d) As unordered pairs, {u^2, v^2} = {(|α|+|β|)^2/4, (|α|−|β|)^2/4}. ∎

Lemma 1.2.
- If Inf_i ≤ 1/2, then Delta_i ≤ (2/ln 2 + log2(e/Inf_i))·Inf_i.
- If Inf_i > 1/2, then Delta_i ≤ (2/ln 2 + 2)·Inf_i.

Proof. By Lemma 1.1, Delta_i ≤ (2/ln 2)η_i + h2(η_i).
- If Inf_i ≤ 1/2, then h2(η_i) ≤ h2(Inf_i) ≤ Inf_i log2(e/Inf_i), because (1−x) log2(1/(1−x)) ≤ x log2 e.
- Otherwise h2(η_i) ≤ 1 < 2 Inf_i. ∎

Proposition 6.2 attains this bound up to O(Inf_i), so no per-step bound of Han's type can be improved coordinate by coordinate.

## 2. FEI reduces to functions with small influences (proved)

Theorem 2.1. Fix τ ∈ (0, 1/2] and K ≥ 0.

(i) Suppose every Boolean g all of whose influences are below τ has a coordinate i with Delta_i(g) ≤ K·Inf_i(g). Then H(f) ≤ max(K, 2/ln 2 + log2(e/τ))·I(f) for every Boolean f.

(ii) Conversely, if H ≤ C·I on a class of functions, then every member of the class has a coordinate with Delta_i ≤ (C + 2/ln 2)·Inf_i.

(iii) Hence, if H(g) ≤ C_τ I(g) whenever max_i Inf_i(g) < τ, then H(f) ≤ (2/ln 2 + max(C_τ, log2(e/τ)))·I(f) for all f.

Proof. We argue by induction on the number of relevant variables; constants are trivial. Let f be nonconstant and put C* = max(K, 2/ln 2 + log2(e/τ)).
- If some Inf_i ≥ τ, Lemma 1.2 gives Delta_i ≤ C*·Inf_i. This uses that log2(e/x) is decreasing and that log2(e/τ) > 2.
- Otherwise the hypothesis gives an i with Delta_i ≤ K·Inf_i.
- In either case the restrictions f_± have fewer relevant variables. Then H(f) = Delta_i + avg H(f_±) ≤ C* Inf_i + C*·avg I(f_±) = C* I(f).

For (ii), B(g) = Σ_i H(S_i | S_{−i}) ≤ Σ_i H(S_i | S_{<i}) = H(g) ≤ C·I(g). So some relevant coordinate has B_i ≤ C·Inf_i, and then Delta_i = JS_i + B_i ≤ (C + 2/ln 2)·Inf_i. Part (iii) combines (i) and (ii) with K = C_τ + 2/ln 2. ∎

Corollary 2.2 (where a violation lives). Let C > 2/ln 2 + 2 and suppose H(f) > C·I(f). Then some restriction g of f to a subcube satisfies all of the following:
- H(g) − C·I(g) ≥ H(f) − C·I(f);
- Delta_i(g) > C·Inf_i(g) at every relevant coordinate, so rho_0(g) > C;
- max_i Inf_i(g) < e·2^−(C−2/ln 2).

Proof. While the current function has a coordinate with Delta_i ≤ C·Inf_i, restrict it. Since H − C·I = (Delta_i − C·Inf_i) + avg(H − C·I)(children), some child has excess at least as large; keep that child. The descent stops at a nonconstant g with rho_0(g) > C. Lemma 1.2 then gives the bound on the influences; the case Inf_i > 1/2 is excluded because C > 2/ln 2 + 2. ∎

The readonce REPORT §6 already observes that a potential-free restriction induction can only fail through coordinates of small influence; Theorem 2.1 is the exact form of that observation. The small-influence class is therefore the whole problem rather than a stepping stone, and Section 6 shows that the per-coordinate form fails on it.

## 3. Erasure under disjoint composition (proved; brute force on 250 balanced and 286 biased coordinate cases, maximum error 4.4e-16)

Theorem 3.1. Let f = G(g_1,…,g_k) with the g_j on disjoint variable sets. Write:
- μ_j = E g_j and V_j = 1 − μ_j^2 > 0;
- Ĝ_μ for the coefficients of G in the product basis with input means μ;
- It_j = Σ_{U∋j} Ĝ_μ(U)^2;
- c_w = ĝ_j({w}) for a variable w of g_j.

Then

  B_w(f) = (It_j/V_j)[B_w(g_j) − E(μ_j^2, c_w^2)] + Σ_{U∌j} E(Ĝ_μ(U)^2, (c_w^2/V_j) Ĝ_μ(U∪j)^2),
  Inf_w(f) = (It_j/V_j)·Inf_w(g_j).

Special cases:
- If the inner functions are balanced, then B_w(f) = Inf_j(G)·B_w(g_j) + Ξ_j(c_w^2), where Ξ_j(c^2) := Σ_{T∌j} E(Ĝ(T)^2, c^2 Ĝ(T∪j)^2).
- A fresh input z of G keeps B_z(f) = B_z(G) and Inf_z(f) = Inf_z(G).

Proof. We have f̂(∪_{j∈U} S_j) = Ĝ_μ(U) ∏_{j∈U} ĝ_j(S_j)/√V_j for nonempty S_j, with U = {j: S_j ≠ ∅}. Split the pairs (S, S∪w) with w ∉ S into two cases.

- Case S_j ≠ ∅. Both sets of the pair have the same U. By homogeneity the pair contributes λ·E(ĝ_j(S_j)^2, ĝ_j(S_j∪w)^2), where λ = Ĝ_μ(U)^2 ∏_{l∈U∖j}(ĝ_l(S_l)^2/V_l)/V_j. Summing over the S_l with l ≠ j gives 1; summing over U ∋ j gives It_j/V_j; summing over S_j gives B_w(g_j) minus its S_j = ∅ term, which is E(μ_j^2, c_w^2).
- Case S_j = ∅. The pair is (Ĝ_μ(U)^2 Π, Ĝ_μ(U∪j)^2 (c_w^2/V_j) Π) with Π = ∏_{l∈U} ĝ_l(S_l)^2/V_l. Summing over the S_l gives the second term.

The influence formula follows by summing f̂(S)^2 over the S with w ∈ S_j. For a fresh input, μ = 0, B = 0 and c = 1. ∎

## 4. The restriction drop through a balanced block (proved; 16-variable brute force gives rho_0 3.5661656266226016, recursion 3.5661656266226007)

Theorem 4.1. Let f = G(g_1,…,g_k) with every g_l balanced and on disjoint variables. Let w be a variable of g_j with c = ĝ_j({w}), and let Ht_G(j, μ) be the spectral entropy of G when input j has mean μ and the other inputs are uniform. Then

  Delta_w(f) = Inf_j(G)[Delta_w(g_j) + h2(c^2)] + H(G) − (Ht_G(j,c) + Ht_G(j,−c))/2,  Inf_w(f) = Inf_j(G)·Inf_w(g_j).

Proof. Restricting w turns g_j into g_j^± with means ±c, and V = 1 − c^2.
- By the composition identity, H(f) = H(G) + Σ_l Inf_l(G)·H(g_l).
- Likewise H(f^±) = Ht_G(j,±c) + Σ_{l≠j} It_l^±·H(g_l) + (It_j^±/V)·(H(g_j^±) − h2(V)).
- With one biased input, Ĝ_μ(U) = Ĝ(U) + μĜ(U∪j) for j ∉ U, and Ĝ_μ(U) = √V·Ĝ(U) for j ∈ U. Hence It_j^±/V = Inf_j(G). For l ≠ j, the sign-average of It_l^± is Inf_l(G), because the cross terms cancel and c^2 + V = 1.
- Subtract the average of H(f^±) from H(f) and use h2(V) = h2(c^2). ∎

## 5. The amplification tower of Numaro's g

The tower and its recursions. Let G_1 = g and G_k = g(G_{k−1},…,G_{k−1}); this is monotone and balanced, on 18^k variables. A leaf w of G_k is a path of positions (j_1,…,j_k), and Inf_w(G_k) = ∏ Inf_{j_l}(g), which also equals the level-1 coefficient at w. With j = j_1 and c the influence of the rest of the path, Theorems 3.1 and 4.1 give:
- B_w(G_k)/Inf_w(G_k) = B_w(G_{k−1})/Inf_w(G_{k−1}) + Ξ_j(c^2)/(Inf_j·c);
- Delta_w(G_k)/Inf_w(G_k) = Delta_w(G_{k−1})/Inf_w(G_{k−1}) + [Inf_j·h2(c^2) + H(g) − avg_± Ht_g(j,±c)]/(Inf_j·c);
- B(G_k) = I(g)·B(G_{k−1}) + Σ_j Σ_{leaves w of G_{k−1}} Ξ_j(Inf_w(G_{k−1})^2);
- I(G_k) = I(g)^k and H(G_k) = H(g) + I(g)·H(G_{k−1}).

Numaro's g as the seed. The influences are 57/256 on the nine core coordinates and 1/256 on the nine auxiliary ones. The table matches the published truth-table SHA-256 f8a7bb2c738d86368305111633376b1a3a83d8ee1f1abcc9a37d841b0f9c7839. Because only two influence values occur, the minima and sums reduce to dynamic programmes over the numbers of core and auxiliary positions.

Table 5.1. Depths 1–4 are certified by `code/certify_tower.py`, with interval widths below 1e-9. Depths 5–10 are numerical, from `code/tower_stable.py`.

| k | variables | H/I | B/I | min_i B_i/Inf_i | rho_0 |
|---|---|---|---|---|---|
| 1 | 18 | 3.323393 | 2.687345 | 2.630462 | 4.552315 |
| 2 | 324 | 4.953256 | 3.967379 | 3.916552 | 6.329015 |
| 3 | 5832 | 5.752576 | 4.407414 | 4.367641 | 6.890112 |
| 4 | 104976 | 6.144579 | 4.538835 | 4.504879 | 7.051853 |
| 5 | 1.9e6 | 6.336826 | 4.575286 | 4.543631 | 7.096061 |
| 6 | 3.4e7 | 6.431108 | 4.584946 | 4.554084 | 7.107728 |
| 8 | 1.1e10 | 6.500022 | 4.588053 | 4.557517 | 7.111492 |
| 10 | 3.6e12 | 6.516597 | 4.588245 | 4.557710 | 7.111618 |
| limit | | 6.521846 | | | |

Numerical safeguards for depths 5–10. The formulas are cancellation-free (log1p forms, plus a Taylor enclosure for the two-sided average). They agree with the plain formulas to 1e-11 at depths up to 6, and with the certified intervals at depths up to 4. At sample points they agree with 50-digit arithmetic to 15–16 digits: Ξ_0 at c^2 = 1e-20 and Ξ_12 at c^2 = 3e-12 are both correct to 15–16 digits, and the gate increment at c = 1e-9 agrees in all printed digits (7.308252150465396e-21). Every Delta increment is positive (the smallest is 2.4e-20), so rho_0(G_k) is nondecreasing in k.

Which leaves are extremal. The minimizing leaves are the all-core paths. The auxiliary coordinates of g are flip coordinates: D_j g lives on the inputs whose core lies in one of the two host cells of j, a set of density 1/256. At depth 1 they already have B/Inf = 5.930 and Delta/Inf = 8.391.

Corollary 5.1.
(i) The potential-free restriction induction (at each function pick a coordinate with Delta_i ≤ C·Inf_i) works only if C ≥ sup_f rho_0(f). Hence it needs C ≥ 7.0518 (certified); numerically the bound is 7.1116. This exceeds the best lower bound on the FEI constant, 6.5218.
(ii) The existential erasure route needs K ≥ 4.5049 (certified; 4.5577 numerically). The summed route B ≤ K·I needs K ≥ 4.5388 (certified; 4.5882 numerically).

Proposition 5.2 (measure-only potentials). Suppose Γ and C are such that every f has a coordinate i with

  Delta_i ≤ C·Inf_i + (Γ(p_+) + Γ(p_−))/2 − Γ(p_f),

where p = Pr[f true]. Then for each k there is c ≤ (57/256)^k with

  (Γ(1/2 + c/2) + Γ(1/2 − c/2))/2 − Γ(1/2) ≥ (rho_0(G_k) − C)·c.

Proof. Restricting a leaf w of the balanced monotone G_k gives measures (1 ∓ Inf_w)/2 with Inf_w ≤ (57/256)^k. At every leaf, Delta_w ≥ rho_0(G_k)·Inf_w. ∎

Consequences for Γ. By the certified value rho_0(G_4) ≥ 7.0518: if C < 7.05, then Γ must gain at the midpoint at some scale at most 0.0025. By the numerical limit, lim sup over c → 0 of gain/c is at least 7.1116 − C, so Γ has a convex corner at 1/2. The read-once potential has a concave cusp there instead.

Remark 5.3. The excess is not universal. Take the balanced monotone 4-variable seed [1,1,1,−1,1,1,−1,−1,1,−1,1,−1,1,−1,−1,−1], which has H = 3, I = 3/2 and amplification limit 6. At depth 9 its tower gives B/I 3.507, min_i B_i/Inf_i 3.269 and rho_0 5.075, all below its limit.

## 6. Refuted selectors (proved)

Proposition 6.1 (per-coordinate erasure fails for monotone functions). For odd n, let y* have (n−1)/2 ones, and set F_n(y,z) = Maj_n(y) ∨ (z ∧ [y = y*]); F_n is monotone. Then Inf_z = 2^−n and B_z/Inf_z ≥ (n − 3 log2 n)/2 for n ≥ 11.

Proof.
- The two restrictions differ only at y*, so v_T = ±2^−n χ_T(y*) and u_T = Maĵ(T) ∓ 2^−n χ_T(y*).
- For |T| = k odd, |Maĵ(T)| = M_k := 2^{1−n} C(2m,m) C(m,j)/C(2m,2j) with m = (n−1)/2 and j = (k−1)/2. This closed form was checked against the Walsh transform for n ≤ 15.
- Log-concavity gives C(2m,2j) ≤ (m+1)·C(m,j)^2, and C(2m,m) ≥ 4^m/(2√m). Hence M_k ≥ 2^−n·2^m/(√m (m+1)). For n ≥ 11 this is at least 2^{1−n}, so 4^n u_T^2 ≥ 2^n/n^3.
- Since E(r,s) ≥ s log2(1 + r/s), we get B_z ≥ Σ_{T odd} 4^−n log2(4^n u_T^2) ≥ 2^{−n−1}(n − 3 log2 n). ∎

The exact 40-digit values of this lower-bound sum at n = 5, 9, 17, …, 1025 are 2.29, 3.97, 7.54, 15.04, 30.54, 62.04, 125.5, 253.0, 508.5. The float values of B_z/Inf_z at n = 3, 5, …, 17 are 3.52, 4.24, 4.99, 5.78, 6.62, 7.48, 8.37, 9.27. The majority coordinates of F_n have B/Inf → 0 numerically, so the existential selector is unaffected.

Proposition 6.2 (maximal influence; small influences). Let m ≥ 4 be even, b the inner-product bent function on m variables, and F_m(y,z) = b(y) for z = 0 and b(y)(1 − 2[y = y*]) for z = 1. Then:
- Inf_z(F_m) = 2^−m and B_z(F_m) ≥ (m − 2)·2^−m.
- Let G = F_m(Maj_k(w^1),…,Maj_k(w^m), z) with k odd and ι_k = C(k−1,(k−1)/2)·2^{1−k} < 2^−m. Then z is the unique coordinate of maximal influence of G, every influence of G is at most 2^−m, and B_z(G)/Inf_z(G) ≥ m − 2.

Proof. For the flip coordinate, v_T^2 = 4^−m and |u_T| ≥ 2^−m/2 − 2^−m, hence B_z ≥ 2^−m log2(2^m (1 − 2^−m/2)^2) ≥ (m − 2)·2^−m. For the composed function, Maj_k is balanced and odd, so B_w(Maj_k) = 0, and its level-1 coefficient is ι_k; Theorem 3.1 then gives B_z(G) = B_z(F_m), Inf_z(G) = 2^−m and Inf_w(G) = Inf_{y_j}(F_m)·ι_k < 2^−m. ∎

Consequences:
- No constant K gives B_{i*} ≤ K·Inf_{i*} at a maximal-influence coordinate i*.
- For no τ and K does "all influences < τ" imply B_i ≤ K·Inf_i at every coordinate.
- The existential selector survives: B_w(G)/Inf_w(G) ≤ ι_k[log2 e + log2(1 + 1/(ι_k^2 Inf_{y_j}(F_m)))] → 0.

Remark 6.3 (the pair (Inf_i, η_i) cannot decide goodness). In Proposition 6.2, η_z = Inf_z = x while B_z ≥ x(log2(1/x) − 2), so any bound on B_i in terms of (Inf_i, η_i) alone must allow Φ(x, x) ≥ x(log2(1/x) − 2). Width-2 tribes have equivalent coordinates, B_i/Inf_i ≤ 6.4573 by the read-once theorem, and Inf_i → 0; their ratio η_i/Inf_i is at least 0.9995 for s = 4..8 (numerical). So a selector based on (Inf_i, η_i) certifies no coordinate of large tribes.

Proposition 6.4 (Han's bound with the sprinkled mass; proved). For ε ∈ (0, 1/2], let σ_i(ε) = Σ v_T^2 over the T with |u_T| ≥ |v_T| > 0 and v_T^2/(u_T^2 + v_T^2) < ε. Then:
- B_i ≤ log2(e/ε)·Inf_i + h2(σ_i(ε));
- for any ordering of the coordinates, H(f) ≤ (2/ln 2 + log2(e/ε))·I(f) + Σ_k h2(E_x σ_k(ε; f_x^{(k)})), where f_x^{(k)} fixes the coordinates after k to x.

Proof. Split the terms of B_i = Σ m_T h2(q_T) into three groups. Up-heavy terms satisfy m·h2(q) ≤ 2v^2. Terms with q ≥ ε satisfy h2(q) ≤ q·log2(e/ε), and m·q = v^2. The remaining terms are at most h2(σ), by concavity. The chain H(f) = Σ_k E_x Delta_k(f_x^{(k)}) is Han's telescoping, arXiv:2312.08271 (3.4). ∎

Scope of Proposition 6.4. It contains Han's theorem with explicit constants; in Han's paper, I_k is the influence of coordinate k (read in full). On every family in Section 7, the sprinkled edges (ε = 2^−6) carry at most 0.575·I of B. On the flip coordinate of Proposition 6.2, all of Inf_z is sprinkled, and there the bound is attained.

## 7. Numerical survey

Exhaustive over the 65,536 functions of at most four variables (`code/sweep_n4.py`). The published maxima are reproduced: H/I 3.402476, B/I 2.704153, max_i B_i/Inf_i 3.523112, rho_0 4.867669. New maxima: max_f min_i B_i/Inf_i is 2.672489 (attained by AND3), and max_f min_i B_i/η_i is 3.609640. Lemma 1.1(c) holds on all 262,144 function-coordinate pairs.

Families (`code/families.py`, `logs/families.log`):

| family | n | H/I | B/I | max_i B_i/Inf_i | min_i B_i/Inf_i | rho_0 |
|---|---|---|---|---|---|---|
| bent+flip, m=4 | 5 | 2.2977 | 2.1922 | 5.224 | 2.084 | 3.978 |
| bent+flip, m=12 | 13 | 2.0013 | 2.0007 | 13.442 | 2.000 | 3.998 |
| Maj17 + flip (monotone) | 18 | 2.3988 | 0.0004 | 9.270 | 0.000 | 0.000 |
| one-point 16 | 16 | 3.9303 | 2.0009 | 2.001 | 2.001 | 4.001 |
| tribes w2 s8 | 16 | 4.3296 | 3.6068 | 3.607 | 3.607 | 6.004 |
| tribes w3 s6 | 18 | 3.4388 | 2.5637 | 2.564 | 2.564 | 4.603 |
| rec. Maj3 depth 2 | 9 | 2.2222 | 0 | 0 | 0 | 0 |
| addressing k=4 | 20 | 2.6667 | 1.3333 | 2.000 | 0.000 | 0.000 |
| Numaro g | 18 | 3.3234 | 2.6873 | 5.930 | 2.630 | 4.552 |

## 8. The candidate routes

1. Erasure target. It is open and equivalent to FEI. Its constant is at least 4.5388 (certified), and the existential form's is at least 4.5049. The per-coordinate form fails even for monotone functions, and neither maximal influence nor small influences rescue it.
2. Potential with a second statistic. In the uniform restriction step JS_i ≤ (2/ln 2)·η_i ≤ 2.885·Inf_i, so a ratio JS_i/Inf_i of order Inf_i^−1/2 cannot occur there; the whole obstruction is B_i. Measure-only potentials need a convex corner at 1/2 when C < 7.05. The extra statistic must grow at first order when one deep leaf of a balanced composition is fixed.
3. Han's bound plus a way to pay its excess. The per-step bound is attained, so the excess cannot be paid coordinate by coordinate. Proposition 6.4 isolates the unpaid part.
4. Gate induction on the number of inputs. Not examined here; that is group F3's area.
5. KKLMS on a structured subclass. By Theorem 2.1, the small-influence subclass is equivalent to the whole conjecture.
6. Disproof. No unbounded family appeared, and all tower quantities converge.

## 9. Files

Code (`code/`): `feilib.py` (core quantities); `sweep_n4.py` (exhaustive sweep over four variables); `families.py`, `families_lib.py` (the family survey); `candidates.py` (the sprinkled split and the candidate sums); `monotone_flip_bound.py` (Proposition 6.1); `check_composition.py`, `check_composition_biased.py` (Theorem 3.1); `check_tower_small.py`, `tower_rho0.py` (Theorem 4.1 checks); `tower_erasure.py`, `tower_stable.py`, `tower_argmin.py`, `tower_seeds.py`, `check_xi_mp.py` (Section 5); `certify_tower.py`, the standalone certificate, sha256 08d22c6025b93f64320b3ea1dedb0d19efb38cf46d5ab65f248049678cfea80f.

Logs (`logs/`): outputs of every script above; `certify_tower.log`, sha256 2c7dda8229616c5ca73ab8f0eaf4a37633791feedc5dad017f426c40d43d2872; `SUMMARY.json`.

The certificate assumes numpy's log2 and log1p are accurate to 8 ulp, the same assumption as the published read-once certificate.
