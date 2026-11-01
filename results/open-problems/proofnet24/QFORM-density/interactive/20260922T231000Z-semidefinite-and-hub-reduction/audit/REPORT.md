## Summary

**Audit status: complete.** None of the results labelled PROVED in RESULTS.md, GEOMETRIC_ROUTE_REPORT.md or FOURIER_ROUTE_REPORT.md is false. Every proof was checked, every constant recomputed, and 12 numerical checks were run. The findings are:
- one scope restriction (Theorem C),
- the pointwise reading of Rudelson–Vershynin's Lemma 3.1, which is false and which no audited proof uses,
- one overstated remark,
- several constants and rigour points.

**Findings, by severity**

1. **Fatal if anyone uses it (no audited proof does).** Rudelson–Vershynin's Lemma 3.1, read as a pointwise bound on |ψ(s)|, is false.
   - The lemma bounds the decreasing rearrangement |ψ|*.
   - Counterexample: let X be uniform on the union of the intervals [2πk/s0 − 1/(2M), 2πk/s0 + 1/(2M)], k = 1..M. Then ψ(s0) = sin(s0/2M)/(s0/2M). At s0 = 100, M = 1000 this is 0.99958, where the claimed bound is 0.25.
   - The correct usable forms are Lemma 1, or |{s : |ψ(s)| > τ}| ≤ 2π/τ² (Plancherel plus Chebyshev).

2. **Fixable scope problem in Theorem C.** The proof only works when Q is a function of Y = RᵀX, that is, when b lies in the range of A.
   - If b has a component outside the range, Q = q(Y) + βY₄. The level sets are then not hyperboloids and there is no "one-sheet side".
   - So Theorem C is not uniform in linear terms. It cannot feed Theorem 5.2 and cannot be used after conditioning.
   - Rigour point: the bound "line integral ≤ 2" holds only for almost every line. The fix is to smooth X_i to X_i + εG_i and pass to the limit through P(Q ∈ (s1,s2)) ≤ liminf P(Q_ε ∈ (s1,s2)).
   - The parametrisation, the normal N = (b, −a, −t), ∇q = 2N and the Jacobian 1/2 are all correct. The formula matches Monte Carlo in three configurations.

3. **Overstated remark (GEOM, Remark 2 after Prop 5.5).** The claim that a small nonzero hub diagonal creates a √(|a|u)/|w| small-ball term needs a remainder that cancels the random centre.
   - The explicit witness has rank one: A = (1/a)(a,w)(a,w)ᵀ.
   - For the pure hub the density is only log-singular and does not depend on a: the log coefficient stays at ρ_L(0) ≈ 1.38 from a = 0.2 down to 0.01.
   - Proved replacement: take Q = G(X_h, X_K) + ⟨2X_h w + b, X_S⟩ with {h}, S, K disjoint and G arbitrary (any hub diagonal, anything on K). Then α₂(Q) ≤ (2√2/|w|)(1 + log₊(|w|/(2√2))). The bound is attained numerically.
   - For two hubs the same argument gives density ≤ √(2π)/σ_min(A_{S,H}) for any hub block, provided A_SS = A_SK = 0.

4. **Cosmetic.**
   - **Theorem 5.2:** the two level-3 steps also need rewriting in β-form: p ≤ |a|^{−1/2}(1 + β₂(ξ)) and p ≤ K(1 + β₁(ξ)). The supremum over all s is legitimate because the relevant functions are lower semicontinuous.
   - **Esseen steps:** no constants are written anywhere. P(|Z−s| ≤ u) ≤ 1.0877·u·∫_{|t|≤1/u}|φ|, which gives α₁ ≤ 4.36B when |φ| ≤ B|t|^{−1/2} and α₂ ≤ 2.18·max(B,1) when |φ| ≤ B/|t|.
   - **Theorem 3.1:** the indefinite 2×2 level-1 constant is 4.93·D^{−1/4}, not 49.6·D^{−1/4}. The composition rule (C1) holds with 4 in place of 8.
   - **Theorem 2.1:** the constant 9.34 is really 9.3405; the final 10.83 is unaffected.
   - **Theorem 3.2:** "≤ 4.5·10³ for n ≤ 6" follows from the intermediate bound 246n√(7.2 + log n), not from 250n(8 + log n), which is 14,690 at n = 6.
   - **GEOM table:** the entry "K₃(1) ≈ 91" is the value of one branch; K₃(1) itself is 349.
   - **Prop 5.3:** the constant 2 + 2√2/|w| suffices.
   - **Lemma 3:** "for every s" should read "for a.e. s".

5. **Scope flags for anyone building on these.**
   - Prop 5.4 is not uniform in linear terms outside span(w, v).
   - Theorems H and MF need the non-hub block to be exactly low rank plus diagonal.
   - Theorem D's Remark (iv) concerns only Z; a perturbation can move the marginals.

**Verdicts**

Correct as stated:
- **Lemma 1; Lemma 2 and (3.1).**
- **Theorem F; Theorem H** (A_HH really is arbitrary; the pointwise bound is sharp to about a factor 2).
- **Theorems D, D′ and D_k.** We checked Lieb's normalisation, Cauchy–Binet, the weighted AM–GM step, and the case β_j = 1 (it needs the diagonal-plus-PSD determinant expansion).
- **Lemmas 3–4 and 1.5.** The singular-matrix limit via (A + εI)/(1 − ε) is right.
- **Lemma 1.4 and its sublevel form.** An adversarial search reached at most 0.58 of the bound.
- **Theorem 2.1 and Corollary 2.2; Theorem 3.1 with rules C1–C6; Theorem 3.2; Props 4.1–4.2.**
- **Theorems 5.1–5.2.** Every composition needs only the centre's small-ball function. Every centre is again a quadratic in original coordinates, with the Schur complement as its matrix and arbitrary linear terms.
- **Props 5.3–5.5.**
- **The other FOURIER items:** Prop 2.5, Prop H, Lemmas 4.1–4.3, Cor 4.4, Prop 5.1.

Correct with a scope restriction: Theorem C.

Not audited, because they depend on other records: the pair theorem and the ρ^{1/4} small-ball bound behind "Physical blocks".

**Key new idea:** condition on the hub coordinate rather than on its leaves. When the leaves carry nothing else, this removes the hub diagonal from the problem completely.

**Most useful next step:** correct two statements before they are used in the no-pivot programme. The Rudelson–Vershynin line should say "rearrangement", and Theorem C should carry the hypothesis b ∈ range(A).
