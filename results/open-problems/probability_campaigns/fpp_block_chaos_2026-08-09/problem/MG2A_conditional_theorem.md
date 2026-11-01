# A conditional variance theorem for Z² first-passage percolation (campaign document MG2-A)

Status: VERIFIED ASSEMBLY, 2026-08-09. Hostile referee (iteration 30): Theorem A correctly deduced from the verified engine; every load-bearing step re-derived by hand and computationally (200,000-trial halving-algebra check, 221,858-combination ladder check, zero failures); five literature attributions confirmed at stated scales; overclaim sweep clean; one bookkeeping staleness found (two P-a1 status lines) and fixed in place; one minor technicality (rho sup domain) made explicit in Remark 2.1 per the referee's note. The kappa* = 1/max(2, ceil(4C1)) padding was ruled a genuine improvement over the engine's bare choice (which could exit (0,1) at small C1). This document proves nothing new. It assembles the campaign's conditional main theorem from three inputs, states every unproved hypothesis in exact form, and records the present status of each hypothesis on Z². Its verified content is inherited entirely from:

- [ENGINE] = problem/MG2B_framework_lemma_draft.md. The lattice block-chaos framework lemma: the unconditional sharp engine inequality (its Theorem 8.1) and the conditional halving deduction (its Section 9). VERIFIED 2026-08-09: machine checks C1-C7 re-run by the author; hostile referee with an independent zero-shared-code implementation confirmed its attack list A1-A8 with nothing refuted.
- [CRUX] = problem/CRUX_iteration_arithmetic.md. The iteration arithmetic (its §1) and the quantified smallness requirement (its §2). Elementary and line-checkable. Its §5 occupation lemma (P-a1) was PENDING REFEREE at assembly time; the referee has since CONFIRMED it (sharp constant (b/a)(n+W), tight at a=b) after catching and repairing two draft defects (a false O(1)-hop claim; a one-sided A2 reading corrected to the two-sided form via the resampled geodesic's occupation). Status lines below updated accordingly.

The source paper is Basu-Sidoravicius-Sly, arXiv 2604.01214 (April 2026), cited as [BSS26]; its companion estimate package, their reference [8], is arXiv 2312.14143, cited as [BSS-8].

Standing honesty scope. Nothing below is labeled proved unless it cites [ENGINE] or standard literature. The hypotheses H1-H4 and (M1)(M2)(M3)(CH) are open on Z² today. No unconditional improvement of the lattice variance bound is claimed anywhere in this document, and nothing here bears on χ = 1/3 except conditionally.

## 1. Setting

Bond first-passage percolation on Z². E is the edge set of Z²; μ is a probability law on [a, b] with 0 < a ≤ b < ∞, nondegenerate, atoms allowed; (w_e)_{e ∈ E} are iid with law μ. For a lattice path π, T(π) := Σ_{e ∈ π} w_e, and for x, y ∈ Z², T(x, y) := inf{T(π) : π a path from x to y}. Geodesics exist, are self-avoiding, and no uniqueness is assumed ([ENGINE] Lemma 2.1; ties from atoms are handled by the fixed selection below).

Fix the direction e := e1. For r ≥ 1 and a unit vector u write T_r(u) := T(0, [ru]), where [·] is a fixed rounding to the nearest lattice point; the object of the theorem is

  X_n := T(0, (n, 0)),  D_n := Var(X_n).

g denotes the time-constant norm, g(x) = lim_k T(0, [kx])/k (Cox-Durrett 1981); g is a norm on R², convex, with the symmetries of Z².

Blocks, resampling, selection (all constructed and verified in [ENGINE] §§1-5; recalled here so the document is self-contained). For a scale pair (s, n) with ratio r := n/s ∈ [M, M+1], set W_s := ⌈√(s Q_s)⌉ (Q is the envelope of H1 below) and tile the edge set by the s × W_s blocks Λ_ij := {e : midpoint(e) ∈ [(i−1)s, is) × [(j−1)W_s, jW_s)}; the blocks partition E ([ENGINE] Def 3.1). Each block carries an independent same-law reservoir w'_Λ and an independent uniform label τ_Λ ([ENGINE] Def 3.2). X := X_n; X^Λ is X evaluated after resampling block Λ from its reservoir; γ_can is the canonical (α-minimal) geodesic of X, a fixed measurable selection valid with atoms and ties ([ENGINE] Def 2.4, Prop 2.5, Lemma 2.6); U_Λ := {γ_can uses an edge of Λ}; F_t is the pair-revealing filtration of [ENGINE] Def 3.4. The engine quantities at the pair (s, n) are

  A2(s, n) := Σ_Λ E[1(U_Λ)(X^Λ − X)²],
  A4(s, n) := Σ_Λ E[1(U_Λ)((X^Λ − X)⁺)⁴],
  P̄_{s,n}(κ) := Σ_Λ E[P(U_Λ | F_{1−κ})²].

Because the U-events depend on the selection rule, every quantitative hypothesis below is asserted for this fixed α-minimal selection ([ENGINE] Rem 4.4).

## 2. The hypothesis set

### 2.1 Base facts (established; no hypothesis content)

(B1) iid weights in [a, b], atoms allowed; (B2) finite-block edge partition; (B3) same-law reservoirs, uniform labels, pair-revealing filtrations; (B4) fixed measurable geodesic selection. All four are constructed and verified unconditionally in [ENGINE] §§1-5 and listed in its §12(a). The further facts the transplanted construction may consume are free on Z² and standard: localization and boundedness ([ENGINE] Lemma 1.1), subadditivity and the shape theorem (Cox-Durrett 1981), the Harris-FKG inequality for monotone functionals of iid weights (Harris 1960), spatial independence across disjoint edge sets, and the reflection symmetries of Z² about the e1-axis. This list is the axiom H5 of [MG1] ("H5-free": bookkeeping facts, nothing to prove).

### 2.2 The directional package H1-H4 (open hypotheses; exact forms)

These are the lattice forms of the estimate package that [BSS26] imports from [BSS-8], as catalogued by [MG1]: isotropy enters the source only through this package, at every scale but only inside an o(1) angular window around the reference direction; the multiscale machinery itself is symmetry-free. Fix the integer M ≥ 2 of Theorem A.

(H1) Fluctuation envelope with directional window. There exist an envelope Q: [1, ∞) → (0, ∞) with Q_r ≤ C√r, an exponent θ ∈ (0, 1], constants c, C > 0, a truncation level s_r with (br)² exp(−s_r^θ) ≤ Q_r² for all large r, and a window half-width ω_r ≥ C_M √(Q_r / r) with C_M polynomial in M (note √(Q_r/r) = W_r/r for W_r = √(r Q_r), the slope scale [MG1] records as O(poly(M) W_r/r)), such that for all large r and every unit u with angle(u, e) ≤ ω_r:

 (H1a) concentration: P(|T_r(u) − E T_r(u)| ≥ σ Q_r) ≤ C exp(−σ^θ) for 0 < σ ≤ s_r;
 (H1b) alignment: |E T_r(u) − r g(u)| ≤ C Q_r;
 (H1c) wandering: for 1 ≤ σ ≤ s_r, with probability ≥ 1 − C exp(−σ^θ) every geodesic from 0 to [ru] stays within distance σ W_r of the segment {t r u : 0 ≤ t ≤ 1}; and W_r ≤ C r^{3/4} (which follows from Q_r ≤ C√r).

 Correspondence: (H1a) is the lattice form of the curvature-centered concentration of [BSS-8] (its Thm 2.1, Props 2.2 and 2.9, Lemma 2.3); (H1c) of its wandering package (Thm 2.4, Lemmas 2.5, 2.10, 2.11); (H1b) of the Alexander-type alignment recorded by [MG1].

(H2-pointwise) Newman curvature at the direction e only. Let h(φ) := g(u_φ), u_φ the unit vector at angle φ from e. There exist δ > 0 and 0 < c₋ ≤ c₊ < ∞ with

  c₋ φ² ≤ h(φ) − h(0) − h'(0) φ ≤ c₊ φ²  for |φ| ≤ δ.

 For e = e1 the reflection symmetry of Z² forces h'(0) = 0. Why the pointwise form suffices: MG2-C's audit ([LOG] iteration 17) read the spans of [BSS26] not covered line-by-line by [MG1] (the §3 proofs, the middles of §§6-8, §9 pp. 85-94, Appendices A-C) and tabulated every consumption of directional input. Verdict WINDOW-o(1): every load-bearing consumption sits at angular slope O(n^{β−1/4}) from the reference direction, with β < 1/4 the source's own standing constraint, so the window of consumed directions shrinks to zero with the scale; the roughly 2700 lines of the source's §§6 and 8 cite none of the tracked imports. Curvature is therefore only ever evaluated at directions converging to e, and the pointwise two-sided form above, paired with H1's window, covers every located use. Arc-uniform curvature is not required by anything located. The residual instantiation obligations are (C1) and (C2) in §2.4.

(H3) Two-sided Q-ratio scaling. There exist exponents 0 < α₋ ≤ α₊ < 1, an integer K₀ ≥ 2, and c, C > 0 such that for all large r and all integers K ≥ K₀:

  c K^{α₋} ≤ Q_{Kr} / Q_r ≤ C K^{α₊}.

 The lower inequality (polynomial growth of the envelope, the "χ > 0 surrogate") is the load-bearing side: [MG1] records it as consumed for dyadic summability in the source's §9 (pp. 88-92) and Appendix B. It is the single most restrictive axiom of the set ([LOG] iteration 3), a judgment the arithmetic of §5 sharpens.

(H4) Anti-concentration at envelope scale. There exist c₄ ∈ (0, 1) and δ₄ > 0 such that for all large r, every unit u with angle(u, e) ≤ ω_r, and every interval I ⊂ R with |I| ≤ δ₄ Q_r:

  P(T_r(u) ∈ I) ≤ 1 − c₄.

Remark 2.1 (H4 pins the variance floor). If H4 holds then for all large s, D_s ≥ (c₄ δ₄²/4) Q_s², hence

  ρ := sup_s Q_s²/D_s ≤ 4/(c₄ δ₄²) < ∞.

Proof. Take I := [E X_s − δ₄ Q_s/2, E X_s + δ₄ Q_s/2]. By H4, P(|X_s − E X_s| > δ₄ Q_s/2) ≥ c₄, so D_s = E(X_s − E X_s)² ≥ (δ₄ Q_s/2)² c₄. ∎ (H4 holds for all large r, so the sup defining ρ is taken over s ≥ n₀ with n₀ chosen inside H4's regime — which is also the only range where ρ is consumed, in ε₀ for (CH); referee note, made explicit.)

This three-line observation is the only derivation this document adds; everything else is cited. It matters because ρ < ∞ is exactly the absorption input (CH.c) below, the quantity [CRUX] §2 identifies as the wall.

### 2.3 The block-level hypotheses (M1)(M2)(M3)(CH) and the eight spot-imports

These are the lattice analogues of [BSS26] Propositions 2.15 and 2.17, in the form consumed by the verified halving deduction [ENGINE] §9. They are asserted for every scale pair (s, n) with s ≥ n₀ and ratio r = n/s ∈ [M, M+1], with constants uniform in the pair. ([ENGINE] states them at the exact ratio r = M with a free scale parameter V; the assembly takes V = D_s, the source's own choice, [ENGINE] Rem 9.2, and lets the ratio move in [M, M+1] so that integer scales can be chained in §4. The proofs in [ENGINE] §9 use M only as a bookkeeping constant, so this widening changes nothing.)

(M1) Second-moment bound at variance scale: A2(s, n) ≤ C1 r D_s.
(M2) Fourth-moment bound at envelope scale: A4(s, n) ≤ C2 r Q_s⁴. A stretched-exponential tail form suffices; [ENGINE] Rem 9.3 converts it with an explicit constant.
(M3) Column-count square tail (carried): Σ_i E[(Σ_j 1(U_ij))²] ≤ C3 r, the square sitting on the per-column sum (the forced reading of the source's third estimate; [ENGINE] audit (c5)). The engine does not consume (M3) ([ENGINE] Rem 9.4); it is consumed inside the source's proof of the chaos bound, i.e. en route to (CH), and is carried here for fidelity.
(CH) Block chaos at fixed κ. Set κ* := 1/max(2, ⌈4 C1⌉) and ε₀ := 1/(16 C2 ρ²) with ρ from Remark 2.1. Then

  P̄_{s,n}(κ*) ≤ ε₀ r.

 Equivalent disorder-chaos form: Σ_Λ P[U_Λ ∩ U'_Λ] ≤ ε₀ r, where U'_Λ is the same event for the fully resampled field ([ENGINE] Rem 9.5).

The eight spot-imports. [ENGINE] §12(b) names the ingredient-level estimates the source consumes to prove its Propositions 2.15/2.17 — exactly what a lattice verification of (M1)-(CH) must replace. As named sub-hypotheses:

 (M1.a) fluctuation-scale concentration at block scale — the [BSS-8]-package analogue feeding the first estimate of Prop 2.15;
 (M1.b) transversal control — geodesic confinement in W-tubes; the quantitative consumption of (H1c);
 (M1.c) local-variance comparison — the second moment of a one-block increment compared against D_s;
 (M2.a) fourth-moment, or stretched-exponential tail, bound for block influences at envelope scale;
 (M3.a) square-integrable column-count tail — the (M3) display;
 (CH.a) the multiscale chaos construction of [BSS26] §§4-9 run on the lattice — consumes H1, H2-pointwise and H4 inside the o(1) window ([MG1]; [LOG] iteration 17), plus Harris-FKG and reflection symmetry from the H5 list;
 (CH.b) the two-sided Q-ratio scale relations for dyadic summability — H3, with the polynomial lower ratio load-bearing;
 (CH.c) the absorption input ρ = sup_s Q_s²/D_s < ∞ — in the source this is its Theorem 2.1, consumed but uncited at the absorption step ([ENGINE] audit (c3)); here it follows from H4 by Remark 2.1.

### 2.4 Instantiation caveats (from MG2-C; explicit numbered sub-hypotheses)

Any lattice instantiation of the construction behind (CH.a) carries two obligations, both found and independently double-discovered by MG2-C ([LOG] iteration 17):

 (C1) Axis-respecting corner argument. The corner-case proof of the source's Lemma 2.8, at its display (96), rotates a box — a rotation-invariance-flavored step at micro-scale. The lattice instantiation must replace it with an axis-respecting argument. This is a sub-question strictly narrower than H2.

 UPDATE (campaign iterations 43-50). The C1 analysis has now been refereed: MAJOR REVISION, construction sound, bookkeeping not. The three items below are RESTATED in their post-referee form; the pre-referee wording (which said (C1) reduces to a single clause and remains "narrower than H2") was wrong on both counts and is superseded here.
 (i) (C1) is not vacuous on the lattice and does not shrink there — the DIRECTION of this inversion is referee-confirmed. Lemma 2.8's two displays split along the source's two devices: (87) is the environment/independence branch, which the lattice's edge-partitioned iid weights make a tautology, while (96) sits in the (93) confinement branch. The campaign's earlier expectation (that free block independence might make the corner argument unnecessary) was wrong, informatively. MAGNITUDE CORRECTED: (C1) does NOT become "the whole of Lemma 2.8" — the residue after (96) is (96) + (97) + the Theorem-2.4 gluing event; (98) is genuinely free on Z^2 by the lattice reflection x -> n-x.
 (ii) H1 AS STATED ABOVE IS INCOMPLETE, in TWO distinct ways, both referee-confirmed.
   (a) WINDOW TOO NARROW FOR ITS OWN CONSUMPTION: this document's H2 paragraph already records consumption at angular slope O(n^{β−1/4}), i.e. n^β·W_r/r, while H1 guarantees only ω_r ≥ C_M·W_r/r with C_M polynomial in M, not in n. FIX: H1 should read ω_r ≥ C_M n^β W_r / r (still o(1) since β < 1/4). This is a live defect in THIS document, found by the C1 work and confirmed by its referee.
   (b) DIRECTIONS: the corner box realises every direction, so (C1) is not implied by H1 at all. The correct reduction is to H1a (concentration), H1b (alignment) AND H1c (wandering), each with its angular window removed, at scales up to n^{2(β+(1+α)/2)/(3−α)}. The earlier wording here — reduction to a single H1c-micro clause, with the scale cap treated as a weakening — was wrong on both counts: the model is scale-free, so capping the scale buys nothing.
   (c) STRENGTH, CORRECTED: (C1) is NOT "strictly narrower than H2". Not consuming curvature in a derivation says nothing about hypothesis strength, and all-direction wandering has, under every published route, been proved only under curvature on an ARC. On present evidence (C1) is plausibly STRONGER than H2-pointwise. The (C1) entry in §5 and the "sub-question strictly narrower than H2" phrasing above are hereby withdrawn.
 (iii) A threshold appears that is invisible at Kesten scale, and it is WORSE than first computed. The proposed axis-respecting construction closes only above an envelope-exponent threshold: α > 1/3 IF one assumes alignment at the envelope scale, but that assumption is itself open whenever Q_r << √r; on Alexander's PUBLISHED bound (C√s log s) the criterion becomes α² + 2α − 1 > 0, i.e. α > √2 − 1 ≈ 0.414. So the workable window on known inputs is (0.414, 1/2], and the conjectured envelope α = 1/3 fails by a wide margin rather than marginally. Whether α = 1/3 then forces an arc-curvature obligation is SPECULATION and is labelled as such — the failure is a gap in this route, not a proof that every route fails.
 (C2) Pin ε* < 1/4. In the source's §9.4 the constraint ε* < 1/4 is idiom rather than pinned text. Very likely benign, but the lattice analogue of §9.4 must fix ε* explicitly and verify the constraint at each point of consumption.

Bookkeeping note (assembler's, not a numbered caveat): [MG1] located four body invocations of reflection symmetry in the source (its pp. 77, 84, 103, 107). At e = e1 the lattice supplies reflection about the axis; an instantiation of (CH.a) should check that each of the four is about a line Z² respects. Recorded so the list of instantiation obligations is complete.

## 3. The theorem

Theorem A (conditional). Fix μ nondegenerate on [a, b] with 0 < a ≤ b < ∞ (atoms allowed), the direction e = e1, an integer M ≥ 2, and n₀ ≥ 2M². Assume:

 (i) the directional package H1, H2-pointwise, H3, H4 of §2.2, with H1's window accommodating M;
 (ii) the block-level hypotheses (M1), (M2), (M3), (CH) of §2.3, with uniform constants, for every scale pair (s, n) with s ≥ n₀ and n/s ∈ [M, M+1].

Then, with ε'_M := log 2 / log(M+1) and B := max{D_m : n₀ ≤ m < M n₀},

  D_n ≤ B (n / n₀)^{1 − ε'_M}  for every integer n ≥ n₀,

and along the geometric family n = M^k m, m ∈ [n₀, M n₀) ∩ Z, the sharper exponent holds:

  D_{M^k m} ≤ (M/2)^k D_m = D_m (n/m)^{1 − ε_M},  ε_M := log 2 / log M.

In the phrasing of [CRUX] §1: Var(X_n) = O(n^{1−ε}) with ε = log 2 / log M − o(1), the o(1) absorbing the constant prefactor and, if every integer n is insisted on, the rounding loss from M to M+1, which vanishes as M grows.

Remark 3.1 (architecture: what is proved, what is assumed, and what each hypothesis does). The implication [(M1) and (M2) and (CH) with the stated smallness] ⇒ [per-scale halving] is proved: it is [ENGINE] §9, whose deduction the hostile referee confirmed. The implication [H1-H4] ⇒ [(M1)-(CH)] is NOT proved here and is not claimed: it is the source's route (its proofs of Props 2.15/2.17), which [MG1] showed consumes directional input only inside an o(1) window and [LOG] iteration 17 showed needs curvature only pointwise at e. Accordingly the theorem assumes both layers, and the H-package does three jobs: H1 defines the envelope Q that (M2), (CH) and H4 are written against; H4 supplies the absorption input ρ < ∞ (Remark 2.1), which makes (CH)'s demand a constant ε₀ rather than an n-decaying one — without it the theorem's hypothesis set would be vacuous in the sense of [CRUX] §2; and H1-H4 jointly are the raw material any BSS-route verification of (M1)-(CH) would consume, which is what makes those hypotheses believable rather than arbitrary.

Remark 3.2 (which M). ε_M decreases in M, so one wants the smallest M the hypotheses support; the source needs M ≥ M₀ for its chaos bound, and that trade-off reappears here inside the constants C1, C2, ε₀. Consistency check against the conjectured exponent: if Var(X_n) is really of order n^{2/3}, the package can hold with uniform constants only for M ≥ 8, since n^{1−ε_M} ≥ n^{2/3} forces ε_M = log 2/log M ≤ 1/3. The method saturates at the conjectured exponent as M decreases to 8.

Remark 3.3 (what Theorem A does not say). It does not produce any unconditional bound: every clause of (i)-(ii) is open on Z² today (§5). It does not touch χ = 1/3: the conclusion is an upper bound n^{1−ε_M} with ε_M ≤ 1/3 (Remark 3.2), and an upper bound at or above the conjectured order n^{2/3} proves neither the existence of χ nor its value.

## 4. Proof of Theorem A (reduction to the verified engine)

Step 0 (constructions; nothing new). Localization, the canonical selection γ_can, the block tiling, reservoirs, labels, filtrations, off-geodesic monotonicity, the freezing lemmas, the order-averaged variance identity, the sharp per-block bound E[H²] ≤ E[G²], and the time split are [ENGINE] §§1-7, verified unconditionally on Z² with iid bounded weights, atoms allowed, no uniqueness, no FKG, no isotropy.

Step 1 (engine inequality). For every κ ∈ (0,1) and every pair (s, n) as in (ii):

  Var(X_n) ≤ κ A2(s, n) + √(A4(s, n) · P̄_{s,n}(κ)).

This is [ENGINE] Theorem 8.1, with sharp constant 1 via its Lemma 7.2. (Under the source's own printed factor-2 route the same chain runs with (κ, ε) → (κ/2, ε/4), [ENGINE] Rem 8.2; nothing below depends on the difference beyond constants.)

Step 2 ((M1) enters). κ* A2 ≤ κ* C1 r D_s ≤ (1/4) r D_s, by the choice κ* = 1/max(2, ⌈4C1⌉) ≤ 1/(4C1). This is the first half of the smallness pair [ENGINE] (9.2); with V = D_s it is exactly the source's κ = 1/⌈4C1⌉ ([ENGINE] Rem 9.1 — available at this sharpness only through the constant-1 engine; the printed factor-2 route would need 1/⌈8C1⌉).

Step 3 ((M2) and (CH) enter). A4 ≤ C2 r Q_s⁴ and P̄(κ*) ≤ ε₀ r give

  √(A4 P̄) ≤ r Q_s² √(C2 ε₀) = r Q_s² / (4ρ) ≤ (1/4) r D_s,

using ε₀ = 1/(16 C2 ρ²) and Q_s² ≤ ρ D_s (definition of ρ; finite by Remark 2.1 from H4). This is the second half of [ENGINE] (9.2), and it is exactly where the quantitative crux lives: the demand ε₀ ≤ D_s²/(16 C2 Q_s⁴) = 1/(16 C2 ρ_s²) is [CRUX] §2's inequality, and §5 records why no unconditional input can meet it today.

Step 4 (halving). Summing Steps 2-3 in Step 1:

  Var(X_n) ≤ (1/2) r Var(X_s),  r = n/s ∈ [M, M+1].

At r = M this is [ENGINE] (9.3), the conditional halving, whose deduction the referee confirmed; the ratio-window form is the same arithmetic verbatim.


Step 5 (iteration; [CRUX] §1 plus integer rounding). For n ∈ [n₀, M n₀) the claim is D_n ≤ B, immediate from the definition of B. For n ≥ M n₀, set s_0 := n and s_{j+1} := ⌊s_j / M⌋ while s_j ≥ M n₀; the terminal value m := s_k satisfies n₀ ≤ m < M n₀ (upper by stopping; lower because s_{k−1} ≥ M n₀ gives m ≥ ⌊M n₀/M⌋ = n₀). Every rung's lower scale s_{j+1} is therefore ≥ n₀, inside the range of hypothesis (ii), and since s_j ≥ M n₀ ≥ M² + M, each ratio r_j := s_j / s_{j+1} lies in [M, M+1]. Step 4 at every rung gives

  D_n ≤ (Π_j r_j / 2) D_m = (n/m) 2^{−k} D_m.

From r_j ≤ M+1: n/m ≤ (M+1)^k, i.e. k ≥ log(n/m)/log(M+1), hence 2^{−k} ≤ (n/m)^{−ε'_M} and

  D_n ≤ D_m (n/m)^{1−ε'_M} ≤ B (n / n₀)^{1−ε'_M},

using m ≥ n₀ and D_m ≤ B. Along the exact geometric family n = M^k m, m ∈ [n₀, M n₀) ∩ Z, every ratio is exactly M, so Π r_j/2 = (M/2)^k and the sharper display of the theorem holds; that computation is [CRUX] §1 verbatim, including (M/2)^k = (n/m)^{1−log 2/log M}. ∎

Where each hypothesis enters, tabulated. (M1): Step 2. (M2): Step 3, left factor. (CH): Step 3, right factor, at the κ* fixed in Step 2. H4: Step 3, through ρ < ∞ (Remark 2.1). H1: defines Q_s (hence the scales of (M2), (CH), H4) and the window every directional statement is quantified over. H2-pointwise, H3, (M3), and the H5 facts are not consumed by Steps 1-5 at all; they are consumed by any verification of (M1)-(CH) along the source's route — H2 and H4 inside the multiscale construction (CH.a), H3 in its dyadic summability (CH.b), (M3) inside the proof of the chaos bound ([ENGINE] Rem 9.4), FKG and reflection symmetry as (CH.a) bookkeeping — under the obligations (C1), (C2).

Provenance note, recorded once: the transplant that produced [ENGINE] also surfaced two typo-level defects in the source's pp. 15-19 (a printed inequality which at t = 1 would force Var = 0 against the source's own Theorem 2.1, and an internal factor-2 inconsistency whose endpoint (14) is nevertheless true); both are harmless downstream and are repaired exactly by the sharp constant-1 inequality of [ENGINE] Lemma 7.2 — see [ENGINE] §12(c). The source's Theorem 2.13 is unaffected.

## 5. Hypothesis ledger: status on Z² today

The convention: PROVED HERE means proved in [ENGINE] and referee-verified; KNOWN means available in the standard literature with the citation given; OPEN means exactly that. (P-a1, initially carried as PENDING REFEREE under the standing rule, has since been REFEREED AND CONFIRMED; its entries below reflect that.)

Engine inequality (Step 1). PROVED HERE, unconditional: [ENGINE] Theorem 8.1 on Z², iid bounded weights, atoms allowed, no uniqueness assumed, no FKG, no isotropy.

Halving deduction (Steps 2-4 given the hypotheses). PROVED HERE as a deduction: [ENGINE] §9.

Base facts (B1)-(B4), H5. PROVED HERE ([ENGINE] §§1-5, §12(a)) and KNOWN: Harris 1960 (FKG), Cox-Durrett 1981 (shape theorem); localization is [ENGINE] Lemma 1.1.

H1. OPEN as a package at every envelope below the Kesten scale — and, because of (H1c), open as a package even at it. Component status: (H1a) concentration is KNOWN at Q_r = Θ(√r) (Kesten 1993; Talagrand 1995) and at Q_r = Θ(√(r/log r)) (Benaim-Rossignol 2008; Damron-Hanson-Sosoe 2014); (H1b) alignment is KNOWN at C√r·log r (Alexander 1997), a log factor above the Kesten envelope; (H1c) quantitative wandering at W_r = √(r Q_r) is OPEN unconditionally at every polynomial scale — bounds of the type ξ ≤ 3/4 are known only under curvature hypotheses (Newman-Piza 1995; Licea-Newman-Piza 1996). In the continuum family, [BSS-8] proves the entire package from isotropy; that contrast is the content of [MG1].


H3. OPEN, both sides, as a statement about the true envelope. The lower ratio (polynomial growth, the χ > 0 surrogate) is the hardest single axiom of the set ([LOG] iteration 3; [MG1]): today's only unconditional variance divergence is D_n ≥ c log n (Newman-Piza 1995, under mild conditions on μ), which is divergence, not a ratio bound, and lives at logarithmic, not polynomial, scale.

H4. OPEN at envelope scale for every polynomial envelope. Nothing anti-concentrates X_n at any polynomial scale today; the Newman-Piza floor gives spread at √(log n) scale only. Note the overlap made explicit by Remark 2.1: H4 at scale Q_n contains the variance floor D_n ≥ c Q_n², so the wall below wears H4's clothes as well as H3's.

(M1). OPEN at variance scale (V = D_s). At coarser scales: the classical per-edge machinery gives Kesten's Var = O(n) but does not regroup to blocks without an occupation input ([CRUX] §4); the deterministic worst-case occupation lemma P-a1 ([CRUX] §5, REFEREED AND CONFIRMED, sharp constant (b/a)(s+W), two-sided consequence) gives A2 ≤ C r s(s+W) unconditionally — a factor (s+W) above even the Kesten-scale target, so (M1) at variance scale remains open.

(M2). OPEN at envelope scale Q_s⁴. Same worst-case remark: the refereed P-a1 gives A4 ≤ C r s(s+W)³ unconditionally, far above the target.

(M3). OPEN at the stated strength. The refereed P-a1 yields the crude deterministic version (each column count is bounded by occupation), not the square-tail form.

(CH). OPEN on Z². Qualitative disorder chaos on the lattice is KNOWN (Ahlberg-Deijfen-Sfragara, arXiv 2302.11367); the quantitative block form — constant ε₀ at fixed κ*, summed over blocks — is not provided by any lattice argument today. In the continuum family it is KNOWN under isotropy ([BSS26] Prop 2.17 and §§4-9). Any lattice instantiation of that construction carries (C1) and (C2).

(C1), (C2). OPEN but narrow: (C1) is a lemma to write (axis-respecting replacement for the corner case of the source's Lemma 2.8, display (96)); (C2) is a parameter to pin (ε* < 1/4 in the §9.4 analogue). Both are strictly smaller questions than H2 ([LOG] iteration 17).

The wall, quantified ([CRUX] §2 — the arithmetic this ledger hangs on). The halving at scale s needs ε₀ ≤ 1/(16 C2 ρ_s²), ρ_s := Q_s²/D_s. In the source, ρ_s = Θ(1) (its Theorem 2.1: the envelope IS the standard deviation), so a small constant chaos estimate suffices, and that is what its §§4-9 deliver. On Z² today the best unconditional pair is Q_s² ≤ C s/log s against D_s ≥ c log s, so ρ_s can be as large as order s/log² s, and the required chaos strength becomes ε_s ≲ log⁴ s / s² — while every construction of the source's type produces a constant, not anything decaying in s. The shortfall is a factor of order s²/log⁴ s. Conclusion, stated plainly: with today's unconditional lattice inputs the engine cannot iterate even once at large s. H1 with H3-lower (equivalently, an envelope at the true fluctuation scale with its matching floor — the pair that H4 encodes at that scale) is not one hypothesis among several; it is the wall, and (CH) is reachable only after it.

## 6. Relation to known results

The unconditional lattice record is Var(X_n) = O(n/log n), proved by Benjamini-Kalai-Schramm (2003) for two-valued weights and extended to general classes by Benaim-Rossignol (2008) and Damron-Hanson-Sosoe (2014); Theorem A is a conditional statement strictly beyond it, and nothing here improves on n/log n unconditionally. Ahlberg-Deijfen-Sfragara (arXiv 2302.11367) establish qualitative disorder chaos for lattice FPP and pose the quantitative variance-via-chaos question as open; Theorem A is a priced, conditional answer to the shape of that question — it says exactly what a chaos route must pay (a block-level estimate at constant strength, after an envelope with matched floor makes constant strength sufficient). Basu-Sidoravicius-Sly (arXiv 2604.01214) prove the unconditional continuum counterpart for rotationally invariant FPP; the campaign's audit ([MG1]) located isotropy's entry entirely inside the imported estimate package of arXiv 2312.14143, consumed in an o(1) angular window, and the engine beneath their Theorem 2.13 transplants to Z² and is verified ([ENGINE]) — so Theorem A isolates that package as the entire lattice-missing content. Nguyen (arXiv 2602.01036) treats chemical distance for lattice Bernoulli percolation with edge-level resampling and degenerate weights — different resampling granularity and weight class. Per the campaign's literature recon ([LOG] iteration 16), the reduction is new in this specific form, not new in kind: the Gaussian ancestor of the chaos-variance link is Chatterjee's superconcentration-chaos duality (arXiv 0810.4221; Superconcentration and Related Topics, 2014), and no prior work combines Z² bond FPP, bounded iid weights, block-level resampling, and the unconditional two-term inequality. (Recon caveats stand: no MathSciNet access; an arXiv math.PR sweep of May-August 2026 is owed before this attribution appears in print-bound text.)

## 7. What would make Theorem A unconditional

The three doors of [CRUX] §2, ranked here by whether a working precedent exists, whether the statement is believed as posed, and the quantitative distance to it. Labels (i)-(iii) are the crux note's.

First door — (iii): an envelope at the true fluctuation scale. Prove H1 for a Q genuinely at the fluctuation scale, with H3's two-sided ratio; by the arithmetic above this is (i) plus concentration at that scale, and it is what [BSS-8] proves from isotropy in the continuum. Ranked first because it is the only door with a working instance (the continuum), and it is exactly the H1+H3 pair Theorem A consumes.

Second door — (i): the matched variance floor. Prove D_n ≥ c Q_n² for the same envelope concentration provides ("χ exists" in disguise; believed). Ranked second: it is the load-bearing half of the first door, but taken alone at today's envelope it would assert Kesten-scale variance — so it is only coherent jointly with an envelope improvement, and no mechanism for it exists at any polynomial scale (the Newman-Piza floor is logarithmic).

Third door — (ii): super-strong chaos. Prove (CH) with ε decaying like log⁴ n/n², beating the required 1/(16 C2 ρ_n²) at today's ρ_n. Ranked last: the crux note rules it unrealistic as a target — constructions of the source's type produce constants, and the gap is a factor of order n², up to logarithms.

The campaign's unconditional stock, for contrast, sits before these doors, not through them: the engine inequality is proved and verified ([ENGINE] Thm 8.1), and the occupation lemma P-a1 is now REFEREED AND CONFIRMED ([CRUX] §5), upgrading the engine to a usable unconditional weak-form reduction: any block-chaos estimate of strength o(1) at Kesten-scale envelopes forces Var(X_n) = o(n(n+W)) - unconditional, but weaker than the BKS record unless the chaos strength decays. Neither opens a door; the doors are H1, H3, H4 at scales nobody can reach today, and (CH) behind them.

## References

Campaign documents (this directory):
[ENGINE] problem/MG2B_framework_lemma_draft.md (VERIFIED 2026-08-09).
[CRUX] problem/CRUX_iteration_arithmetic.md (its §5 occupation lemma REFEREED AND CONFIRMED, sharp form).

Literature:
K. Alexander, Approximation of subadditive functions and convergence rates in limiting-shape results, Ann. Probab. 25 (1997) 30-55.
D. Ahlberg, M. Deijfen, M. Sfragara, arXiv 2302.11367 (2023). [ADS23]
R. Basu, V. Sidoravicius, A. Sly, arXiv 2604.01214 (2026). [BSS26]
R. Basu, V. Sidoravicius, A. Sly (companion estimate package), arXiv 2312.14143. [BSS-8]
M. Benaim, R. Rossignol, Exponential concentration for first passage percolation through modified Poincare inequalities, Ann. Inst. H. Poincare Probab. Stat. 44 (2008) 544-573.
I. Benjamini, G. Kalai, O. Schramm, First passage percolation has sublinear distance variance, Ann. Probab. 31 (2003) 1970-1978. [BKS03]
S. Chatterjee, arXiv 0810.4221; Superconcentration and Related Topics, Springer (2014).
J. T. Cox, R. Durrett, Some limit theorems for percolation processes with necessary and sufficient conditions, Ann. Probab. 9 (1981) 583-603.
M. Damron, J. Hanson, P. Sosoe, Subdiffusive concentration in first-passage percolation, Electron. J. Probab. 19 (2014), no. 109; and Sublinear variance in first-passage percolation for general distributions, Probab. Theory Related Fields 163 (2015) 223-258.
T. E. Harris, A lower bound for the critical probability in a certain percolation process, Proc. Cambridge Philos. Soc. 56 (1960) 13-20.
H. Kesten, On the speed of convergence in first-passage percolation, Ann. Appl. Probab. 3 (1993) 296-338.
C. Licea, C. M. Newman, M. S. T. Piza, Superdiffusivity in first-passage percolation, Probab. Theory Related Fields 106 (1996) 559-591.
C. M. Newman, M. S. T. Piza, Divergence of shape fluctuations in two dimensions, Ann. Probab. 23 (1995) 977-1005.
V. H. Nguyen, arXiv 2602.01036 (2026).
M. Talagrand, Concentration of measure and isoperimetric inequalities in product spaces, Inst. Hautes Etudes Sci. Publ. Math. 81 (1995) 73-205.

---
SUPERSESSION POINTER (added iter 67, 2026-08-09 22:3x). This document mentions the claim that the
corner route's exponent window and the wall's requirement are DISJOINT. That claim is UNDER CHALLENGE
as of iteration 66 and must not be quoted from here. Read CRUX_iteration_arithmetic.md section 7,
which argues the disjointness may be an artifact of substituting the conjectured KPZ variance into an
argument that only needs the weaker variance being proved - and which also carries the strongest case
that the challenge is empty. A referee is deciding it. Separately, sections 6, 6b and 6c of that same
document are WITHDRAWN as a contribution per the referee verdict recorded in section 6d; the one
surviving result from them is the positive-part correction now recorded in section 5.

RESOLUTION (iter 68) to the supersession pointer above: the challenge to the disjointness was
refereed and REFUTED. The disjointness stands and is wider than first claimed - the wall's admissible
set is the interval (0, chi], not the point 1/3, because constant-strength chaos needs alpha <= chi
while concentration at scale Q forces alpha >= chi, pinning alpha = chi. BUT it is CONDITIONAL on
chi <= sqrt(2)-1 = 0.4142 (true variance exponent <= 0.8284), which is unproved; nothing
unconditional excludes chi in (0.414, 1/2]. Never state the disjointness flatly. The withdrawal of
CRUX sections 6, 6b and 6c is unaffected and still stands.
