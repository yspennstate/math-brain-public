# THE BLOCK-CHAOS FRAMEWORK LEMMA, LATTICE VERSION (VERIFIED 2026-08-09)

Status: VERIFIED. Produced by MG2-B 2026-08-09 17:4x-18:0x; author re-ran engine_check.py 18:0x (C1-C7 pass); hostile referee (independent implementation, different 12-edge/4096-config instance, non-identical non-uniform block laws, zero shared code) returned 18:3x: attack list A1-A8 ALL CONFIRMED, no REFUTED, no UNDETERMINED. Verdicts: Sections 1-8 (unconditional sharp engine inequality on Z^2) CORRECT AS WRITTEN; Section 9 (conditional halving) CORRECTLY DEDUCED; errata (c1)+(c2) against BSS pp.15-19 SOLID TO STATE PUBLICLY as typo-level errata (the printed inequality at their lines 1104-1107 forces Var=0 against their own Theorem 2.1; harmless downstream; (14) repaired exactly by this document's sharp constant-1 inequality). Referee scripts: scratchpad referee_independent_check.py / referee_author_instance.py; referee's per-item quote checks and per-step re-derivations in the campaign transcript. Scope limits unchanged: (M1)(M2)(M3)(CH) remain unproved lattice hypotheses; nothing here solves chi=1/3 (see CRUX_iteration_arithmetic.md for the quantified wall).

### A self-contained statement and proof of the variance-reduction engine of Basu-Sidoravicius-Sly (arXiv 2604.01214, Theorem 2.13), transplanted to Z^2 first-passage percolation

Provenance conventions. Items marked READ are taken from the extracted paper text (scratchpad bss2026.txt; line numbers refer to that file). Items marked DERIVED are proved here from first principles. Square brackets [.] after a step name the model property consumed. The proof skeleton (Lemmas 6.1, 7.1, 7.2, 7.3, 4.3, 2.4 and Theorem 8.1) was machine-checked exactly (full enumeration, no Monte Carlo) on a 7-edge, 3-block FPP instance; script: engine_check.py (scratchpad). That check verifies the implementation of the general identities on one instance; it is a bug-catcher, not a proof.

## 0. What the paper does at this point (READ, for orientation)

The paper works in a rotationally invariant continuum FPP model. For the engine it uses: a "restricted" (conforming-path) distance X across columns of width n (lines 560-627); a pair of independent fields omega = (omega*, omega0) (lines 812-815); blocks Lambda+_ij of size n x W_n carrying iid uniform labels T_ij (818-820); the resampled field omega_t which replaces each block independently with probability t (821-830, their eq. (5)); X' := the distance in omega_kappa (830-831); the filtration F_t = sigma{T_ij, omega(Lambda+_ij) : T_ij <= t} (838-844); the event U_ij that the geodesic passes within distance 1 of Lambda_ij (845-851); the one-block resampled distance X^ij and the monotonicity X^ij - X <= 0 on U_ij^c (858-877, their eq. (6)). Theorem 2.13 (751-754): for M >= M0 and n large, Var(X_Mn) <= (1/2) M Var(X_n). Inputs: Proposition 2.15 (888-917; three estimates) and Proposition 2.17 (993-1002; the chaos bound E Sum P[U_ij | F_{1-kappa}]^2 <= eps M). The proof of Theorem 2.13 occupies lines 1004-1381 (pp. 15-19). The audit of that proof is Section 12(c).

Everything below is the lattice analogue, re-proved from scratch.

## 1. Setting

(S1) [DERIVED setup] Let E denote the edge set of Z^2, drawn in the plane with unit segments. Fix a probability law mu on [a, b] with 0 < a <= b < infinity; atoms are allowed. Let (w_e) be iid with law mu. For a path pi, T_omega(pi) := Sum_{e in pi} w_e. For x, y in Z^2, X_{xy}(omega) := inf { T_omega(pi) : pi a path from x to y }. Fix endpoints u != v, write X := X_{uv}, L0 := ||u-v||_1. In the application ||u-v|| ~ Mn and X = X_{Mn}; D := Var(X_n) is the variance of the same functional at scale n. Nothing in the engine uses the value of ||u-v||; the scales enter only through the hypotheses.

Lemma 1.1 (localization). [0 < a <= b < infinity; nothing random] Let R* := floor(L0(a+b)/(2a)) + 1, B* := {z : ||z-u||_1 <= R*}, Ehat := {e : both endpoints in B*}. Then for EVERY omega in [a,b]^E: (i) X(omega) <= b L0; (ii) every u-v path touching a vertex outside B* has weight > b L0; hence (iii) X is a measurable function of (w_e)_{e in Ehat} alone and every optimal path stays in B*. Same for any configuration obtained by resampling within [a,b].

Proof. (i): a monotone staircase path has L0 edges, weight <= b L0. (ii): if pi visits z with ||z-u||_1 >= R*+1 then |pi| >= 2(R*+1) - L0, so T(pi) >= a(2R*+2-L0) > b L0 by choice of R*. (iii) follows. QED

## 2. Geodesics and the canonical ("topmost") selection

Throughout, omega in [a,b]^Ehat is fixed; all statements deterministic. [No distributional assumptions; atoms and ties fully allowed.]

Lemma 2.1 (existence, self-avoidance, finiteness). [0 < a <= b < infinity] The infimum is attained; every optimal path is self-avoiding with at most bL0/a edges; Geo(omega) is nonempty and finite, contained in the finite deterministic set P* of self-avoiding u-v paths in B* with <= bL0/a edges.

Proof. A walk containing a cycle strictly exceeds its loop-erasure (cycle has >= 1 edge of weight >= a > 0); so inf over walks = inf over self-avoiding paths; any candidate with more than bL0/a edges has weight > bL0 >= X. Finite set, infimum attained, optimality forces self-avoidance. QED

Lemma 2.2 (common vertices come in the same order). [a > 0] Let gamma, gamma' in Geo(omega), p != q on both. If gamma visits p before q, so does gamma'.

Proof. Else concatenations W1 := gamma[u->p].gamma'[p->v] and W2 := gamma'[u->q].gamma[q->v] are u-v walks with T(W1), T(W2) >= X. Adding and using T_gamma(u->p)+T_gamma(q->v) = X - T_gamma(p->q), similarly for gamma', gives T_gamma(p->q) + T_gamma'(q->p) <= 0, impossible (each segment has an edge of weight >= a > 0). QED

Lemma 2.3 (bubble decomposition; mixtures are geodesics). [a > 0; NO planarity] Let gamma != gamma' in Geo(omega), common vertices u = z0, z1, ..., zk = v in shared order; sigma_m := gamma[z_m -> z_{m+1}], sigma'_m := gamma'[z_m -> z_{m+1}]. Then: (i) sigma_m, sigma'_m have no common internal vertices; either sigma_m = sigma'_m (single shared edge) or their union is a simple closed curve ("bubble"); (ii) T(sigma_m) = T(sigma'_m) for every m; (iii) every mixture (choosing sigma or sigma' per bubble) is a self-avoiding geodesic.

Proof. (i) A common internal vertex would be a common vertex of gamma, gamma' strictly between z_m, z_{m+1} in the shared order. If sigma_m = sigma'_m they share all internal vertices so have none: both are the unique edge {z_m, z_{m+1}}. (ii) Replace sigma_m by sigma'_m inside gamma: the result is self-avoiding (an internal vertex of sigma'_m on gamma would again be an out-of-order common vertex), so T >= X forces T(sigma'_m) >= T(sigma_m); symmetric. (iii) Internal disjointness of chosen arcs: same-order argument as (i)/(ii); weight = Sum T(sigma_m) = X. QED

Definition 2.4 (canonical geodesic gamma_can, "topmost"). [planarity] For a self-avoiding path gamma with vertices x0..xr let alpha(gamma) := Sum_s ((x_{s-1})_1 + (x_s)_1)/2 * ((x_s)_2 - (x_{s-1})_2) (the line integral int_gamma x dy; horizontal edges contribute 0, vertical edge at abscissa p contributes +-p). gamma_can(omega) := the unique alpha-minimizing element of Geo(omega).

Proposition 2.5 (well-definedness and extremal property). [planarity: Jordan, Green, Pick; Lemmas 2.1-2.3] The alpha-minimizer exists and is unique. For every gamma in Geo and every bubble of (gamma_can, gamma), gamma_can's arc keeps the bubble's region on its RIGHT traversed z_m -> z_{m+1} (the closed curve (gamma_can arc).(gamma arc)^{-1} is clockwise).

Proof. alpha is additive under concatenation; for two u-v paths, alpha(gamma) - alpha(gammahat) = signed area of gamma.gammahat^{-1} (Green). In a bubble, exactly one arc is the clockwise one; swapping the other for it changes alpha by -Leb(R_m); Pick gives Leb(R_m) >= 1 (lattice Jordan polygon, >= 4 boundary edges, I + B/2 - 1 >= 1). Existence: Geo finite nonempty. Uniqueness: two minimizers have a bubble; the all-clockwise mixture (a geodesic by 2.3(iii)) strictly lowers alpha below one of them. Extremal property: a non-clockwise arc of gamma_can in some bubble could be swapped to strictly lower alpha. Right-side = clockwise: interior on the right along the traversal is the negative orientation. QED

What "topmost" needs, precisely: (a) a > 0 (self-avoidance, finiteness, same-order); (b) b < infinity (localization); (c) planarity (Jordan/Green/Pick); (d) NO distributional input - atoms/ties handled; the selection is a deterministic measurable function of omega.

Honest caveat on the name: for a bubble traversed left-to-right, region-on-right is the UPPER arc, so along rightward stretches gamma_can is genuinely topmost. For right-to-left (backtracking) bubbles it is the lower arc. On the unrestricted lattice there is NO globally consistent "lies above" for backtracking paths; the paper's crossing-switch construction (READ 617-627) is for conforming (column-monotone) paths where "above" is unambiguous. The alpha-selection is the rigorous lattice surrogate and agrees with naive topmost whenever that is well-defined. The framework lemma consumes ONLY: gamma_can(omega) in Geo(omega) + measurability; any measurable selection works in Sections 3-9. The specific planar selection matters only later when proving (M1)-(CH).

Lemma 2.6 (measurability). [finiteness of P*] {gamma_can = g} = {T(g) = X} intersect Intersection_{g': alpha(g') < alpha(g)} {T(g') > X}: finite Boolean combination of measurable events. QED

## 3. Blocks, resampling, labels, filtrations

Definition 3.1 (block tiling). [nothing model-specific] Fix n, W >= 1. Lambda_ij := { e : midpoint of e in [(i-1)n, in) x [(j-1)W, jW) }. Edge midpoints have exactly one half-integer coordinate, so {Lambda_ij} PARTITIONS the edge set. (READ: paper blocks are closed rectangles, lines 451-458, 818-820, W_n = sqrt(n Q_n) 441-443. DERIVED deviation: partitioning EDGES makes "geodesic affected by resampling Lambda" EXACTLY "geodesic uses an edge of Lambda"; the paper needs a distance-1 fattening because its field is 2-dependent, READ 832-836, 845-857.) Everything works for ANY partition of E into finite blocks. B** := blocks meeting Ehat; N := |B**|.

Definition 3.2 (probability space). [iid structure enters here] Independently over blocks Lambda: w_Lambda (true weights, law mu^Lambda); w'_Lambda (independent same-law reservoir); tau_Lambda uniform[0,1] (label); all mutually independent. omega := (w_Lambda); omega' := (w'_Lambda). (READ: matches omega = (omega*, omega0) and T_ij, 812-820.)

Remark (what "iid" is actually consumed): blocks independent of one another; reservoir independent and same-law per block; labels independent uniforms independent of weights. Identical distribution ACROSS blocks is never used.

Definition 3.3 (one-block resampling; U-events). omega^Lambda := omega with w_Lambda replaced by w'_Lambda; X^Lambda := X(omega^Lambda). Fully-resampled field omega_kappa: w_Lambda if tau_Lambda <= 1-kappa else w'_Lambda; X' := X(omega_kappa). U_Lambda := {gamma_can(omega) uses an edge of Lambda}; U'_Lambda := {gamma_can(omega_kappa) uses an edge of Lambda}. Events by Lemma 2.6. (READ: U_ij 845-851; U'_ij 1394-1402.)

Definition 3.4 (filtrations - matching the paper, READ 838-844, 1016-1032). For t in [0,1]: D_Lambda(t) := (tau_Lambda, w_Lambda, w'_Lambda) if tau_Lambda <= t else a cemetery symbol. F_t := sigma(D_Lambda(t) : Lambda in B**); F_t^{-Lambda} removes block Lambda entirely; F_t^{+Lambda} := F_t^{-Lambda} join sigma(w_Lambda, w'_Lambda) (pair but not label). Monotone in t. Restriction to B** harmless (independence).

Remark 3.5 (the pair must be revealed; (CH) insensitive). The paper's omega(Lambda+_ij) must be read as the PAIR (omega*, omega0)(Lambda+_ij); with the omega*-only reading two steps of the paper's proof fail (audit (c4)); line 814 intends the pair. For the chaos quantity it makes no difference: U_Lambda is sigma(omega)-measurable and revealed reservoirs are independent of omega, so P[U_Lambda | F_{1-kappa}] is unchanged.

Definition 3.6 (per-block processes). H_Lambda(t) := E[X | F_t^{+Lambda}] - E[X | F_t^{-Lambda}]; Gtilde_Lambda(t) := E[X^Lambda - X | F_t^{+Lambda}]; Z_Lambda := 1(U_Lambda)(X^Lambda - X)^+; G_Lambda(t) := E[Z_Lambda | F_t^{+Lambda}]. All bounded (<= b L0), every interchange licensed. (READ: 1033-1036, 1049-1056.)

## 4. Exchangeability and monotonicity

Lemma 4.1 (swap symmetry). [independent blocks + same-law reservoir] S_Lambda := the involution exchanging w_Lambda <-> w'_Lambda, fixing all else. (i) S_Lambda preserves the measure [same law + independence]; (ii) X o S_Lambda = X^Lambda, X^Lambda o S_Lambda = X, 1(U_Lambda) o S_Lambda = 1(Uhat_Lambda) with Uhat_Lambda := {gamma_can(omega^Lambda) uses an edge of Lambda} [deterministic selection; no uniqueness needed]; (iii) (X, X^Lambda) exchangeable; (iv) S_Lambda^{-1} F_t^{+Lambda} = F_t^{+Lambda} and E[Y o S | F] = E[Y|F] o S for bounded Y (change of variables on the pi-system; S^2 = id).

Lemma 4.2 (splitting a square). E[(X - X^Lambda)^2] = 2 E[((X^Lambda - X)^+)^2]. [4.1]

Lemma 4.3 (off-geodesic monotonicity). [X a minimum of local path weights; gamma_can in Geo; nothing else] Pointwise on U_Lambda^c: X^Lambda <= X; equivalently (X^Lambda - X)^+ = 1(U_Lambda)(X^Lambda - X)^+ everywhere. (4.1)

Proof. On U_Lambda^c, gamma_can(omega) uses no edge of Lambda; omega^Lambda differs only there; T_{omega^Lambda}(gamma_can(omega)) = X; X^Lambda <= X. (READ: paper's (6), 870-877; the lattice needs no fattening.) QED

Remark 4.4 (ties/atoms do not break it). The comparison is of VALUES; only "some optimal path of omega avoids Lambda" is needed and gamma_can is such a path. Atoms affect WHICH selection rule realizes U_Lambda; the engine holds for every fixed measurable selection; the hypotheses (M1)(M2)(CH) are rule-dependent and must be verified for the fixed rule. Symmetrically X <= X^Lambda on Uhat_Lambda^c, so X = X^Lambda off U union Uhat (not used).

## 5. Freezing: kernel representations

For A subset of blocks write w_A; R_t^{-Lambda} := {Lambda' != Lambda : tau_{Lambda'} <= t}.

Lemma 5.1 (freezing). [mutual independence; labels independent of weights] For bounded X~ = f(omega, w'_Lambda): with kernels psi_S^{X~}(x_S, y, y') := E[X~ | w_S = x_S, w_Lambda = y, w'_Lambda = y'] and phi_S^{X~}(x_S) := E[X~ | w_S = x_S]:
 (i) E[X~ | F_t^{+Lambda}] = Sum_S 1(R_t^{-Lambda} = S) psi_S^{X~}(w_S, w_Lambda, w'_Lambda) a.s.;
 (ii) E[X~ | F_t^{-Lambda}] = Sum_S 1(R = S) phi_S^{X~}(w_S) a.s.;
 (iii) for X~ = X the kernel does not depend on y' - write psi_S(x_S, y) - and phi_S^X = integral of psi_S over y; for X~ = X^Lambda the SAME kernel with y' in the second slot.
Proof: pi-system over revealed-pattern cylinders + Fubini (labels first, then unrevealed weights). QED

Lemma 5.2 (label-split of the F_{1-kappa} second moment). [labels only] For bounded label-free Y:
 E[(E[Y|F_{1-kappa}])^2] = (1-kappa) E[(E[Y|F_{1-kappa}^{+Lambda}])^2] + kappa E[(E[Y|F_{1-kappa}^{-Lambda}])^2],
hence (1-kappa) E[(E[Y|F^{+Lambda}])^2] <= E[(E[Y|F])^2]. (5.1)
Proof: V := 1{tau_Lambda <= 1-kappa} E[Y|F^{+}] + 1{tau > 1-kappa} E[Y|F^{-}] is a version of E[Y|F_{1-kappa}] (measurability via recoverability of the pair on the revealed event; defining property checked on the two-piece pi-system; tau independent of everything else); square and factor the independent indicator. (READ: their pre-(13) display and (13), 1180-1208.) QED

## 6. The variance identity

Lemma 6.1. [independent blocks; iid uniform labels independent of weights]
 Var(X) = Sum_Lambda Integral_0^1 E[H_Lambda(t)^2] dt. (6.1)
Blocks not meeting Ehat contribute 0.
(READ: integrated form of their (10), 1037-1048, asserted there without proof; proved here without continuous-time machinery or label distinctness.)

Proof. h_{Lambda,S} := E[(E[X|w_{S+Lambda}] - E[X|w_S])^2]. (i) Deterministic enumeration pi: martingale increments D_k orthogonal, Var(X) = Sum_k h_{pi(k), S_pi(k)}. (ii) Average over all N! orders: Var(X) = Sum_Lambda Sum_S (|S|!(N-1-|S|)!/N!) h_{Lambda,S}. (6.2) (iii) By 5.1, E[H_Lambda(t)^2] = Sum_S t^{|S|}(1-t)^{N-1-|S|} h_{Lambda,S} (disjoint events kill cross terms; labels independent of weights). (iv) Beta integral int_0^1 t^s (1-t)^{N-1-s} dt = s!(N-1-s)!/N!; integrate and compare. QED
(Machine check C1: 1.1e-16 agreement.)

## 7. Per-block inequalities

Lemma 7.1 (exchangeable-bracket identity). [independence + same-law reservoir via 5.1(iii)] E[Gtilde_Lambda(t)^2] = 2 E[H_Lambda(t)^2]. (READ 1057-1067; re-derived.)
Proof. B2 := H_Lambda(t), B1 := E[X^Lambda|F^{+}] - E[X|F^{-}]. By 5.1 both are S-indexed sums with the SAME kernels psi_S, fed w_Lambda (B2) vs w'_Lambda (B1), centered by phi_S. Cross-S terms vanish; conditionally on w_S the two factors are independent with conditional mean 0; so E[B1 B2] = 0 and E[B1^2] = E[B2^2] (same law). Gtilde = B1 - B2; expand. QED

Lemma 7.2 (sharp bound). [7.1 + 4.1 + 4.3] E[H_Lambda(t)^2] <= E[G_Lambda(t)^2], (7.1) with EQUALITY at t = 1 (so the constant 1 is optimal).
Proof. P := E[(X^Lambda - X)^+ | F^{+}] = G_Lambda(t) (by (4.1) exactly); N := E[(X - X^Lambda)^+ | F^{+}]. Gtilde = P - N, PN >= 0, so Gtilde^2 <= P^2 + N^2. By 4.1(iv), N = P o S_Lambda, so E[N^2] = E[P^2]. With 7.1: 2E[H^2] = E[Gtilde^2] <= 2E[G^2].
Equality at t=1: F_1^{+Lambda} contains all weights; G(1) = Z a.s.; E[X|F_1^{-Lambda}] = E[X|w_{others}]; conditionally on w_{others}, X = f(w_Lambda) and X^Lambda = f(w'_Lambda) are iid, so E[H(1)^2] = E[Var(X|w_others)] = (1/2)E[(X - X^Lambda)^2] = E[((X^Lambda - X)^+)^2] = E[Z^2] (by 4.2 then (4.1)) = E[G(1)^2]. QED

Remark 7.2' (comparison with the paper - important). The paper's route obtains E[H^2] <= 2E[G^2] and then PRINTS (lines 1104-1105) "E[(G_ij(t))^2] >= 2E[(H_ij(t))^2]". That printed inequality is FALSE in general: at t = 1 equality E[G(1)^2] = E[H(1)^2] holds universally, so the printed claim forces E[G(1)^2] = 0 - failing whenever resampling has any effect, their own model included. (Machine check C3 exhibits a finite counterexample.) Harmless downstream: the sequel uses only Var <= 2 Sum E[G(T)^2] (their (11)), which is correct; and the sharp (7.1) proved here restores their display (14) exactly as printed - see audit (c1)-(c2).

Lemma 7.3 (time split). [filtration only] t -> E[G_Lambda(t)^2] nondecreasing; hence Integral_0^1 E[G^2] dt <= (1-kappa) E[G(1-kappa)^2] + kappa E[Z^2]. (7.2) (READ: their (12), 1149-1181.) Proof: conditional Jensen on nested filtrations. QED

## 8. The engine

Theorem 8.1 (abstract engine inequality). [all of the above; no isotropy, no FKG, no continuum]
 A2 := Sum_Lambda E[1(U_Lambda)(X^Lambda - X)^2]; A4 := Sum_Lambda E[1(U_Lambda)((X^Lambda - X)^+)^4]; Pbar(kappa) := Sum_Lambda E[P(U_Lambda | F_{1-kappa})^2].
 Then for every kappa in (0,1): Var(X) <= kappa A2 + sqrt(A4 Pbar(kappa)). (8.1)
Proof chain: (1) Var = Sum int E[H^2] [6.1]; (2) <= Sum int E[G^2] [7.2]; (3) time-split [7.3]; (4) kappa-term <= kappa A2; (5) (1-kappa)E[G(1-kappa)^2] <= E[(E[Z|F_{1-kappa}])^2] [5.2]; (6) conditional Cauchy-Schwarz: (E[Z|F])^2 <= E[1(U)((X^L-X)^+)^2 | F] P(U|F), tower; (7) pointwise Cauchy-Schwarz in Lambda; (8) outer Cauchy-Schwarz in L^2: E[sqrt(S) sqrt(P)] <= sqrt(E S) sqrt(E P) = sqrt(A4 Pbar) - correlation between the factors is fine, no independence used. QED
(Machine check C6 passes on a kappa grid.)

Remark 8.2 (paper-faithful crude version): with the factor-2 route, Var <= 2 kappa A2 + 2 sqrt(A4 Pbar); statements below hold with (kappa, eps) -> (kappa/2, eps/4).
Remark 8.3 (restricted block families): for Lambda outside a chosen family bound by E[Z^2]; this is the paper's far-block term C'' M^{-1} Q_n^2 ((7)-(8), 955-982).

## 9. THE LEMMA

Standing assumptions (S): planar Z^2 FPP, iid weights in [a,b], atoms allowed, uniqueness NOT assumed; gamma_can the canonical selection; X = X_{Mn}; blocks the n x W edge tiling; labels/reservoirs/F as above; D := Var(X_n).

Lemma (conditional variance halving). Assume constants C1, C2 > 0, parameters V, V4 > 0, kappa, eps in (0,1) with:
 (M1) Sum_ij E[1(U_ij)(X^ij - X)^2] <= C1 M V;
 (M2) Sum_ij E[1(U_ij)((X^ij - X)^+)^4] <= C2 M V4 (tail form suffices - Remark 9.3);
 (M3) column-count square tail (carried for fidelity; NOT consumed by this proof - Remark 9.4);
 (CH) Sum_ij E[P(U_ij | F_{1-kappa})^2] <= eps M.
Then Var(X_Mn) <= kappa C1 M V + M sqrt(C2 V4 eps). (9.1)
If moreover kappa <= D/(4 C1 V) and eps <= D^2/(16 C2 V4) (9.2), then Var(X_Mn) <= (1/2) M Var(X_n). (9.3)

Remark 9.1 (constant derived, not copied): with V = D the smallness reads kappa <= 1/(4C1) - exactly the paper's kappa = 1/ceil(4C1) - but ONLY via the sharp Lemma 7.2; under the paper's own printed factor-2 route one needs kappa <= 1/(8C1).
Remark 9.2: paper takes V = Var(X_n), V4 ~ Q_n^4 with Q_n = Theta(sqrt Var); then eps <= c/C2 absolute suffices. On the lattice NO fluctuation-scale lower bound Var >= c Q_n^2 is known - see 12(b)5.
Remark 9.3: tail form of (M2) integrates to the expectation form with C2 = C1 + e Gamma(1+1/theta3)/(C2')^{1/theta3}.
Remark 9.4: (M3) is not consumed by the engine; in the paper it is consumed in the PROOF of Prop 2.17 (Cauchy-Schwarz at 3418-3441, count bound (41) at 3472-3494). It belongs to the verification of (CH), not the engine.
Remark 9.5 (disorder-chaos form): (CH) <=> Sum_ij P[U_ij and U'_ij] <= eps M (conditionally iid given F_{1-kappa}; READ 1403-1414, 3452-3457, re-derived).

## 10. Machine verification (honest scope)

engine_check.py: exact enumeration, 7-edge subgraph of Z^2 ({0,1,2} x {0,1}), u=(0,0), v=(2,1), weights iid uniform on {1,2} (atoms -> ties exercised: 128 configs), 3 blocks. Verified: C1 variance identity to 1.1e-16; C2 E[Gtilde^2] = 2E[H^2]; C3 E[H^2] <= E[G^2] with max ratio 1.0000 (sharpness) AND explicit violation of the printed E[G^2] >= 2E[H^2]; C4 monotonicity for all configs/blocks/resamples; C5 uniqueness of alpha-minimizer in all 128 configs; C6 engine bound at 7 kappa values; C7 monotone E[G(t)^2]. Bug-catcher, not proof; author re-ran 2026-08-09 18:0x, all pass.

## 11. Lattice vs continuum: differences and patches

2. U-event fattening: continuum distance-1 fattening; lattice exact edge membership. PATCH SUCCESSFUL (blocks must partition EDGES).
3. Topmost geodesic: continuum asserts existence for conforming paths; lattice gets the full alpha-minimizer construction (existence, uniqueness, measurability) with the honest caveat that literal "topmost" only makes sense on rightward bubbles. PATCH SUCCESSFUL for the engine (needs only measurability + membership); order properties matter later for (CH) verification.
4. Atoms/non-uniqueness: positive-probability ties change WHICH events U_Lambda are, per selection rule; engine valid for any fixed measurable rule; hypotheses are rule-dependent. PATCH SUCCESSFUL.
5. Integrability: [a,b] + localization make everything bounded. Unbounded weights would need L^4 + localization substitutes as hypotheses.
6. No PATCH FAILS. The continuum-specific parts that do NOT transplant are exactly the unproved hypotheses (M1)-(M3), (CH) - the honest boundary of the conditional lemma.

## 12. Closing deliverables

(a) Exact lattice hypothesis list: structural H1 (iid [a,b] weights, atoms ok), H2 (finite-block edge partition), H3 (same-law reservoirs + uniform labels + the pair-revealing F), H4 (fixed measurable selection; canonically alpha-minimal) - all verified unconditionally here; quantitative (M1), (M2)[or tail form], (CH), with (M3) carried; conclusion (9.1) always, (9.3) under (9.2).

(b) What remains for unconditional: 1. (M1) lattice analogue of Prop 2.15(i) - needs fluctuation-scale concentration, transversal control, local-variance comparison (open on Z^2; Kesten-scale gives lossy V). 2. (M2) fourth-moment level (tail form ok). 3. (M3) count tail (en route to CH). 4. (CH) - the heart: the paper's multi-scale chaos construction consumes isotropy-derived scale relations throughout; open on the lattice. 5. Quantitative crux: halving needs eps <= (Var(X_n)/Q_n^2)^2 / (16 C2-const); paper has Var = Theta(Q_n^2); on Z^2 best known lower bound is ~log n, so a lattice program needs either a fluctuation-scale variance lower bound or a much stronger chaos estimate. State this trade-off up front.

(c) Errors/defects found in the original pp. 15-19 (line-by-line):
- (c1) Lines 1104-1107: printed "E[(G_ij(t))^2] >= 2E[(H_ij(t))^2]" is FALSE in general (equality E[H(1)^2] = E[G(1)^2] at t=1 is universal; finite counterexample computed). Harmless downstream: sequel uses only the correct Var <= 2 Sum E[G(T)^2].
- (c2) Display (14) (1209-1222) does not follow from their (9)+(11)+(12)+(13) as printed (internal factor-2 inconsistency); (14) IS true as printed via the sharp E[H^2] <= E[G^2] proved here; alternatively keep factor 2 and take kappa = 1/ceil(8C1). Theorem 2.13 unaffected either way.
- (c3) Final absorption step needs Var(X_n) >= c Q_n^2, available from their Theorem 2.1 but uncited at that point; implicit dependency, not an error.
- (c4) omega(Lambda_ij) in the filtrations must denote the PAIR; omega*-only reading breaks two steps; pair reading clearly intended.
- (c5) Prop 2.15 third estimate: parenthesization ambiguous; forced reading = square on the per-column sum; not used in Thm 2.13's proof at all.
- (c6) Everything else on pp. 15-19 verified correct step by step (their (9), (10) asserted-now-proved, (11), (12), pre-(13)+(13), (15), (16), (17), Cor 2.16, far-block bound, disorder-chaos equivalence).

Summary: unconditionally, the sharp engine inequality Var(X) <= kappa A2 + sqrt(A4 Pbar(kappa)) holds on Z^2 with iid bounded weights, atoms allowed, no uniqueness, canonical topmost selection constructed - consuming no isotropy, no FKG, no continuum structure, planarity only inside the selection. Conditionally on (M1), (M2), (CH) + smallness: Var(X_Mn) <= (1/2) M Var(X_n). One false printed inequality found in the source (with universal-equality disproof + finite counterexample), one internal factor-2 inconsistency whose endpoint is nevertheless correct and is rescued exactly by the sharp inequality proved here.

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
