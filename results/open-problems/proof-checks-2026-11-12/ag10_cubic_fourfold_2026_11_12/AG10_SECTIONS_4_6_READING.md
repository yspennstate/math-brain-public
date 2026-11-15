# AG10: Sections 4 to 6 of the OpenAI cubic-fourfold preprint, read step by step (an agent)

Source: lit/openai/main_c.txt in 06_math_research/ag10_cubic_fourfold_agent_2026_11_12 (compact text, 2802 lines).
Each entry: the lines read, every step re-derived, and a verdict (no gap / gap / not checked, with the reason).

## Where large d enters (orientation, lines 1-150, 224-377)
The smooth side (Prop. 3.10) gives cu(f) = 1 for ANY rational X with rank T_X = 21, End_Hdg = Q, d > 2. That includes
very general Pfaffian cubics (d = 14), which are rational, and the whole of C26, C38, C42 (Russo-Stagliano). So the
Sarkisov side (cu(f) = 0) must fail for those d; the only place it can use d is the degree thresholds of Section 4
(bounded data exclude K3 tests of large degree). A reading of Sections 4-6 should therefore find, for each link type,
the exact bounded object whose K3 degree is capped. If some step closes for every d, the argument would also "prove"
that Pfaffian cubics are irrational, so that step is wrong. This is the smell test to apply at every step.

## 4.1 Elementary exclusions (lines 915-1086): no gap
- Lemma 4.1. F = pi^*(nL) - sum m_i E_i^*, K_Y = sum E_i^*, F^2 = 0 gives sum m_i^2 = n^2 d; adjunction gives
  2g - 2 = K_Y.F = sum m_i; m_i >= 0 integers so (sum m_i)^2 >= sum m_i^2, hence 2g - 2 >= n sqrt(d). Checked.
  (With Pic = ZL ample a pencil always has base points, so some m_i > 0; consistent.)
- Lemma 4.2. A = mu^*B - sum a_i E_i^*, a_i = A.E_i^* > 0, B = mu_*A ample (Nakai), B = kL, k >= 1, so
  d <= B^2 = A^2 + sum a_i^2 <= A^2 + (A.K_Y)^2. Checked. Threefold case: the uniruled locus of a smooth projective
  family is the stable union of the open images U_D of free-curve loci (noetherian); a free curve of degree <= D through
  a very general point lies in an MRC fibre, which is a P^1, so the fibre has H-degree <= D; the fibres form a Hilbert
  component birational to S, a component of a fibre of a finite-type scheme, so bounded models exist and (4.1) applies.
  Checked.
- Theorem 4.3. (i) = Lemma 4.2. (ii) Riemann-Hurwitz 2g' - 2 <= e(2g_A - 2) + (e - 1) r; the pulled-back general
  hyperplane section is smooth (Bertini away from the pencil's base points, which are chosen off D where the cover is
  etale), so its components have genus <= G and Lemma 4.1 gives sqrt d <= 2G - 2. (iii) same estimate on the geometric
  generic fibre. (iv) if f were not constant on MRC fibres, (r, f) : T -> S x C is generically finite and a uniruled
  surface would dominate a K3 surface; so f = h o r, a component P of the fibre dominates the pencil fibre Gamma, and
  g(Gamma) <= q(P), bounded. Checked.

Next: 4.2 central models (lines 1087-1271).

## 4.2 Central models (lines 1087-1271): no gap
Smell test: nothing here uses d, and nothing here should - it is MMP/Sarkisov bookkeeping that produces the bounded
objects; no step concludes anything about cu(f). So there is no all-d closure to worry about in 4.2.
- Lemma 4.4, transfer of epsilon-lc from W to N. (4.4): W -> N is a log terminal model of K_W + Theta_i for interior
  Theta_i, so the exceptional difference is >= 0; coefficients are linear in the boundary, limit gives E_Theta >= 0.
  (4.5): D = p^*A - q^*A_N is q-exceptional (no extraction, so q_* p^* A = A_N) and q-nef (p^*A nef, q^*A_N zero on
  q-curves), so D <= 0 by negativity (KM 3.39). Subtracting (A = Theta - Phi): p^*(K_W+Phi) - q^*(K_N+Phi_N) =
  E_Theta - D >= 0, hence a(F,N,Phi_N) >= a(F,W,Phi) >= eps for every valuation. Checked. Extension to any small
  Q-factorial N' over Q: N -> N' is crepant for K+Theta (pulled back from Q), same argument. Checked.
- Fano type of N/Q (K+Theta trivial over Q, Theta big over Q, perturb) and -(K_N+Phi_N) == A_N over Q. A_N in the
  interior of Mov(N/Q) (perturb A in a basis pushed from W; no fixed divisor since nothing is extracted). MMP for A_N
  on a Mori dream space has only flips (a divisorial step would fix its exceptional divisor), ends nef and semiample
  on N^c; the contraction is small because a nef class zero on curves covering a divisor is on the boundary of Mov.
  K+Phi = -A is crepant for N^c -> Z^c, so Z^c is eps-lc. N^c -> N_i small, then N_i -> V_i -> B_i -> Q. Checked.
- Terminal case Phi = 0: a divisor P of W contracted on N: on its strict transform pick a curve in a q-fibre not
  contracted by p, where p^*A > 0 = q^*A_N; strong negativity puts that fibre in Supp(-D), so the coefficient of P in
  (4.6) is > 0 and a(P,N,0) > 1. Exceptional-over-W valuations already have a > 1 (W smooth). Checked.
- (4.7) a(F,R,Gamma) >= sum (1-b_i) ord_F(x_i): A(v) >= A of the monomial valuation in x with the same values
  (Jonsson-Mustata retraction) = sum v(x_i), minus the boundary orders. Each ord_F(x_i) >= 1. Checked.
- Lemma 4.5. Exceptional valuations on the SNC start have a >= r(1-c) >= 2(1-c) > 1 (needs only c < 1/2; the
  c < 1/4 is used later). On W': K_{W'}+Phi' = f^*(K_V+Phi_V) + E with coefficient a(F,V,Phi_V) - 1 + b, > 0 on every
  f-exceptional divisor (strict improvement for contracted divisors of W, monotonicity for divisors over W), 0 on
  divisors surviving to V. New marks sit on f-exceptional divisors, so f_*Phi' = Phi_V. The E-MMP over V contracts E
  (negativity), ends small over the Q-factorial V, hence V itself. So both endpoints stay outcomes and eps = 1 - c
  does not depend on the higher start. Terminal case: a(F,V) > 1 on f-exceptional F since V is terminal. Checked.
- Perturbations (Hacon-McKernan Lemma 4.1): Theta_i - Phi' = (A + Phi_0 - Phi') + sum H_j + F_i, ample plus nef;
  K_{V_i} + f_i*Theta_i ~ pi_i^* C_i. Standard; not re-derived beyond the displayed identities. Remark: dim W <= 3 is
  not used inside the 4.5 argument (only relative MMP existence for a birational morphism, [15] Thm 1.2); harmless.

Next: 4.3 (lines 1272-1421), where the bounded families should first appear.

## 4.3 Bounded marked pairs and contraction diagrams (lines 1272-1421): no gap
Smell test: again no d, correctly - these are family/boundedness lemmas.
- Lemma 4.6, criterion (4.8): D Q-Cartier <=> [strict transform] in pi^*N^1(Y_t)_Q + span of exceptional classes.
  Converse: on R_t, H^1(O) = 0 kills Pic^0 and numerically trivial NS classes are torsion, so the numerical relation is
  a Q-linear one; push down gives mD ~ a Cartier divisor. Checked. Membership is a statement about fixed rational
  linear data once [21, Thm 1.3] identifies the numerical spaces on a stratum, so it is constant there. Exceptional
  pullback coefficients are unique (negativity applied to E and -E), hence constant. klt = finitely many strict
  inequalities; relative ampleness open. Checked.
- Q-factoriality constructible: all Weil divisors Q-Cartier <=> the right side of (4.8) is all of N^1(R_t)_Q (forward
  by the criterion; converse because every divisor upstairs is the strict transform of its pushforward plus
  exceptional pieces). Constant on strata since N^1(R_t) = H^2(R_t, Q) there. Checked.
- Lemma 4.7: rests on Choi-Li-Zhou [21, Thms 1.4-1.7, Lemma 5.5] (not re-checked; cited family theorem). The
  finiteness-to-boundedness step (spread semiample generators and dual curve generators of each nef cone) is right.
  Non-extracting map f: Y -> Z: for H general ample missing the generic points of the centres of f-contracted divisors,
  R(Y, D) = R(Z, H): a section of O_Z(mH) is regular near those centres (normality), so order >= 0 on contracted
  primes; the other primes are common to Y and Z. Checked; so Z is the ample model of a movable system.
- Remark 4.8, the caveat to carry forward: it bounds only divisors that are irreducible components of the bounded bad
  closed preimages, not arbitrary subvarieties. In Section 5 every branch/marked divisor used must be shown to be such
  a component, otherwise the boundedness does not reach it. CHECK THIS IN SECTION 5.

Next: 4.4 Theorem 4.9 (lines 1422-1481, Birkar's boundedness applied to the central models).

## 4.4 Theorem 4.9, uniform geometric generic link diagrams (lines 1422-1481): no gap
- Central model Z = Z^c restricted to the geometric generic fibre over Fbar = alg. closure of C(Q): dim <= 4,
  -(K+Phi) ample, eps-lc (eps = 1 in (i): smooth W with Phi = 0 is 1-lc; eps = 1 - c in (ii)). Birkar BAB
  [14, Thm 1.1]: eps-lc Fano type of fixed dimension is bounded. Over Fbar rather than C: the bound is a bound on a
  very ample H (H^r and Hilbert polynomial), so every such Z is an Fbar-point of one Hilbert scheme of finite type over
  Q; the paper's "finite-data spreading plus algebraically closed base change" says this. (Also Fbar is abstractly
  isomorphic to C, transcendence degree continuum.) Checked.
- Mark degree: -(K_Z + c D_Z) ample on the fibre gives c D_Z.H^{r-1} < -K_Z.H^{r-1}; the right side is read off the
  second Hilbert coefficient (valid for normal Z: K_Z.H^{r-1} is defined, Weil times Cartier), constant on strata of
  the bounded family. Bounded-degree reduced cycles are bounded (Chow). Splitting over Fbar keeps coefficient c and the
  total degree. Checked.
- Fano type over Q descends to every end and base B -> Q ([55] Lemma 2.8); geometric generic fibre integral (normal
  contraction, char 0) and rationally connected (Hacon-McKernan / Zhang for klt log Fano). Checked.
- Note: this is where independence from the K3 test collection and the path length is claimed; correct, since nothing
  so far depends on them.

## 4.5 Low-discrepancy extractions (lines 1482-1549): no gap
- Lemma 4.10: a non-stratum centre has some parameter with b_j = 0, so by (4.7) a >= w_j + (positive) > 1 (r >= 2).
  Stratum centres: sum (1-b_i) w_i <= 1 with all 1 - b_i > 0 (negative b_i allowed, then 1 - b_i > 1) leaves finitely
  many order vectors; the blow-up of the stratum has crepant coefficient 1 - sum(1-b_i) < 1, still klt, so the
  non-stratum exclusion repeats and the monomial subtraction terminates. Checked (this is the toroidal-valuation
  fact, cf. KM 2.36).
- Theorem 4.11: BCHM Cor. 1.4.3 extracts exactly the finite list (all a <= 1); crepant coefficient 1 - a >= 0, so
  Lambda^t >= 0 (Lambda >= 0 for a log-Fano pair); every non-extracted exceptional valuation keeps a > 1, so terminal;
  -(K+Lambda^t) = tau^*(-(K+Lambda)) nef and big, Fano type. A model T' extracting a subset has every prime among the
  primes of T^t, so T^t -> T' is non-extracting and Lemma 4.7 applies. Checked.

Section 4 so far (4.1-4.5): no gap, and no use of d - consistent with the smell test, which puts the d-dependence in
the degree thresholds that Sections 5-6 must apply to the K3 tests. Next: 4.6 (lines 1550-1621).

## 4.6 Choosing the ramification coefficient once (lines 1550-1621): no gap
- Lemma 4.12. klt: on a simultaneous log resolution the crepant coefficient of K_T + cD on an exceptional E is
  (1 - a_E) + c m_E, < 1 iff c m_E < a_E (paper asks a_E/2); strict transforms of D get c < 1. Ample: k = -K.H^{r-1}
  with mk in Z_{>0}, e = D.H^{r-1} bounded, D == (e/k)(-K), e/k <= me, so ce/k <= cme < 1/2 and
  -(K + cD) == (1 - ce/k)(-K) is ample. Base change: a geometric curve's Galois orbit is a cycle over the ground field
  and conjugates meet a ground-field divisor equally, so a numerical proportionality over F stays true over Fbar even
  if the Picard rank grows. Checked.
- Corollary 4.13. (4.3) with dim T = 3, dim Q <= 1: rho(T/Q) >= 1 forces rho(N_i/V) = 0 and rho(T/Q) = 1 (e_i the
  identity, T -> Q elementary of fibre type). Checked.
  Ramification support is bounded - this ANSWERS the Remark 4.8 caveat for D_T: if P has nonzero residue, the fibre of
  V over the generic point of P (a DVR, V flat over it) cannot be a smooth conic (a smooth conic over the DVR makes the
  class unramified at P), so P lies in the non-smooth locus of V -> T, and a prime divisor inside a proper closed set
  is one of its components; Remark 4.8 bounds those. Checked.
  rho(T_F/F) = 1: T is Q-factorial ([23] Lemma 4.6, base of an elementary contraction of a Q-factorial terminal
  source), divisors on T_F extend by closure, and a divisor numerically trivial over Q restricts to one numerically
  trivial on T_F (intersection numbers constant in the flat family of curves). -K_{T_F} ample: Fano type gives
  -K = (ample) + (effective), ample in rank one. So Lemma 4.12 applies over Fbar. Checked.
  No circularity: c* comes from the ORDINARY families of Theorem 4.9(i), and the log families of 4.9(ii) are then
  built with the fixed c < min(1/4, c*). Checked.
- Carry forward: 4.13 covers only conic ends over Q with dim Q <= 1. Sections 5-6 must handle every other link shape
  (dim Q = 2, conic bundles over a 3-fold base with Q = T, del Pezzo fibrations) by other means or show they cannot
  occur. CHECK IN SECTIONS 5-6.

SECTION 4 COMPLETE (12 Nov 17:4x): 4.1-4.6 read, every step re-derived or traced to a named standard result, no gap.
None of it uses d, which is right by the smell test. Two things to carry into 5-6: (a) the Remark 4.8 caveat for
every marked divisor other than D_T; (b) the link shapes outside Corollary 4.13. Next: Section 5 (line 1622).

## 5.1 Vertical divisors and change of base (lines 1622-1721): no gap; one misprint in (5.5)
- (5.1) v(Y/Z) as a cancelled sum: on a good open U (spread resolution of the generic fibre, flat, unique dominating
  divisor E_D with rationally connected generic fibre over D) u(E_D) = u(D) by Lemma 2.2; leftovers are components of
  Z \ U and f^{-1}(Z \ U); shrinking U adds equal pairs. Checked.
- Lemma 5.1: Fano type over Z => fibres rationally chain connected [30]; at a general e in E lying on no other
  component of f^{-1}(f(E)), the first curve of a chain from e is irreducible inside f^{-1}(f(E)) through e, so it
  lies in E. Covered by rational curves => uniruled. (i), (ii) are the dimension counts. Checked.
- (5.3) v(V/Q) = v(V/B) - h_Q(V/B) + v(B/Q): v(V/B) - h_Q keeps the terms not dominating Q; a divisor of V vertical
  over Q is vertical over B; the divisors of B vertical over Q cancel against v(B/Q). Re-derived. Checked.
- Lemma 5.2 v(B/Q) = 0: leftover divisors are uniruled (5.1) of dimension <= 2, MRC quotient dimension <= 1, test 0;
  base divisors of a Q with dim <= 2 have dimension <= 1. Checked.
- (5.4) Checked (common vertical primes cancel, signs of Lemma 2.4).
- (5.5) MISPRINT in the paper (it is in main.pdf, not an extraction error): (5.3) twice plus (5.4) gives
      cu(f) - v(V'/B') + v(V/B) = cu_hor/Q(f) - h_Q(V'/B') + h_Q(V/B),
  i.e. cu - Delta v, where the display has "- v(V/B)". HARMLESS: the introduction (cu(link) = Delta(v+s)) and the only
  later use, (6.10) "cu(link) - Delta v = H_Q = cu_hor/Q - Delta h_Q" in the proof of Theorem 6.6, carry the right
  sign. Worth one line to the authors if this is ever written up.

## 5.2 Common-base dimensions other than two (lines 1722-1773): no gap - first place d enters, correctly
- dim Q = 3, every d: bases are birational to Q, so nothing on V or B dominates Q except through closed points of the
  generic curve; normal proper curves over C(Q) are smooth, a birational map between them is an isomorphism, so
  cu_hor = 0 and h_Q = 0. Checked. (No d needed: such a link carries no surface information.)
- dim Q = 0, d > threshold: everything dominates a point, so cu = cu_hor counts exc(e_1), exc(e_2), which lie in the
  bounded diagram; h_Q = v; after cancellation the leftovers are components of the complement of a marked good open
  and its preimage, exactly the form Remark 4.8 bounds (caveat satisfied by construction). Theorem 4.3(i) (Lemma 4.2,
  d <= A^2 + (A.K)^2) kills them for d large. Checked.
- dim Q = 1, d > threshold: horizontal exceptional E has geometric generic components = uniruled surfaces exceptional
  for the generic divisorial contraction, bounded; Theorem 4.3(iv): f constant on MRC fibres, the images of the fibre
  surfaces give a pencil on S of genus <= q(P) <= G, against Lemma 4.1. Leftover P in h_Q: same. Leftover D of B
  dominant over Q with dim D = 2: u(D) = 1 means D birational to a degree-d K3, and the Stein factorization of D -> Q
  is a pencil whose general fibre (= geometric generic component, bounded genus) has genus >= 1 + sqrt(d)/2 by
  Lemma 4.1. Checked.
- Smell test: d enters only through these bounded-family exclusions, with one threshold d_vert for all S, links,
  paths; it does not touch rational cubics of small d (Pfaffian d = 14) unless d_vert < 14, which nothing here claims.

Next: 5.3 onward (line 1774), the dim Q = 2 surface links - the place where Pfaffian/C26/C38/C42 must break.

## 5.3 Reduction over a surface common base (lines 1774-1847): no gap
- Lemma 5.5: a smooth model of Q is a rationally connected surface, hence rational, k = C(x,y). Terminal fourfolds
  are smooth in codimension 2, so the singular locus (dim <= 1) misses the generic fibre; the generic surface is
  regular, hence smooth (k perfect). A small birational map of smooth proper surfaces is an isomorphism (a contracted
  curve would spread to a divisor exceptional for the small map). Ends: dim B = 2 gives a rank-one del Pezzo over k,
  dim B = 3 a conic bundle over a smooth genus-zero curve. Ranks over k (not kbar): divisors close up to Q-Cartier Weil
  divisors (surjective restriction), and classes numerically trivial over the base stay so generically (spread a
  generic curve over an open of Q, where B = Q in the del Pezzo case). rho(middle) <= 2; conic total rank 2. Checked.
- Lemma 5.6: a surviving divisorial e_i gives rho(W) = rho(S) + 1, so rho(W) = 2 and S rank one (a conic end has rank
  2, extraction from it would give rank 3). Same extremal ray: each contraction is constant on the other's connected
  fibres, so the targets (and, for conics, the pulled-back curve fields in k(W)) coincide. Distinct K-negative rays are
  the two boundary rays of the 2-dimensional NE(W), so -K_W is ample (Kleiman). Checked.

## 5.4 Finite sets on the generic surfaces, to line 1923: no gap
- (5.6), (5.7): u(K(t)) = u(K) (MRC); an orbit of size <= 2 has field k or a quadratic extension of the rational k,
  the latter with an involution, which a test K3 field (trivial Aut; birational automorphisms of a K3 are
  automorphisms) cannot have. Checked.
- Lemma 5.7: over kbar every fibre has p_a = 0 and -K degree 2; a double fibre 2R has 2p_a(R) - 2 = R^2 + K.R = -1,
  odd, impossible; two components have -K.R_i = 1, R_i^2 = -m, and 2p_a - 2 = -m - 1 >= -2 forces m = 1: two
  transverse (-1)-lines. A split component cover would give a k-divisor of fibre degree 0 that is negative on a
  vertical k-curve, against relative rank one; so each component field L is quadratic over the discriminant field K.
  Local form a x^2 + b y^2 + t c z^2 (exponent > 1 would make the total space singular at the node); quaternion
  (-ab, -act) after scaling by a; tame residue (-ab)^{v(-act)} = -ab mod squares, the field splitting the two lines.
  h_Q = u(Dtilde) - u(Delta): the singular-fibre divisor is one prime with field L(t) and u(L) = 0 by the involution of
  L/K; base points with singular fibres are not cancelled; smooth fibres cancel. So h_Q = -u(Delta). Checked.

## 5.4 (rest) and 5.5 The two-ray surface calculation (lines 1924-2130): no gap
- Def 5.8 integrality: complementing all choices is a free equivariant involution of P_Delta; a preserved orbit has a
  field involution (u = 0), the rest pair off, so u(P_Delta) is even. Checked.
- Lemma 5.9: A(S) = 5 classes (deg 5), 3 (deg 6), A2(S) = {L, 2L - E1 - E2 - E3}; one relation (both sums = -K),
  G-invariant, so Q[A] + Q[A2] = Pic_Q + Q; rank one over k (rational invariant classes descend: Brauer obstruction
  is torsion) gives 2 orbits in total, so both sets are transitive. Enumeration confirmed by brute force
  (fillq_ctl/ag10_table514.py, .out). Checked.
- Prop 5.10. Divisorial contraction of W: negative definite exceptional matrix, adjunction forces disjoint (-1)-curves,
  one Galois orbit (relative rank one): the blowup of one closed point. Cocycle u(E) - u(F) (E survives on S', F on S;
  Lemma 2.4 signs), not multiplied by orbit sizes. Checked.
  One divisorial end: isotropic fibre class in <H, E_Sigma> needs ae square; list (4,1), (8,2), (9,1), (9,4) -
  confirmed by brute force; |Delta| = 8 - D (contract one line per singular fibre to a ruled surface, K^2 = 8); first
  three have e <= 2 and |Delta| != 3, all terms 0; (9,4): fibre class 2L - sum E_i (conics through the 4 points),
  three reducible members = the three pair-partitions, stars and triangles give P_Delta = E u E equivariantly, so
  w(conic) = u(E) = the extraction term. Checked.
  Two conic ends: -K = (2/m)(F1+F2), D = 8/m in {8,4,2,1}, never 5, so |Delta| != 3 on either side. Checked.
  Two divisorial ends, D = 1, 2: Bertini/Geiser involution over k is -1 on K-perp, cannot fix an exceptional ray
  (lambda = 1 would put E_Sigma in QK, against E^2 < 0 < K^2), so it swaps the ends. Checked.
  D >= 3: Gram determinant D m^2 - 2efm - ef(D+e+f) = 0 re-derived; root (5.14); m/e, m/f integers, m <= ef (lines).
  The nine-row table is EXACTLY what a brute-force search gives (ag10_table514.out). Identifications: (3,2,5) and
  (3,3,3): image class (5,1,3) / (6,2,4), -K_S - C in A(S), injective, cardinalities 5 / 3, so F = A(S); (4,1,5),
  (5,1,3): image already in A(S); diagonal cases: "misses exactly one" (m/e = e - 1) is an equivariant bijection
  E = F, outputs degree 8/9; (4,2,2): Pic(S)_Q + Q[E] = Pic(S')_Q + Q[F], with (5.9) the 2-element sets give only
  1-dim pieces, the reduced rep of the transitive triple is Q-irreducible (C3 via Q(zeta3) or S3 standard), so the
  kernels agree and the transitive 3-point action of C3 / S3 is unique up to isomorphism: A(S) = A(S'). Checked.
  |Delta| <= 7 from D >= 1. Structured-isomorphism case: H_Q = 0 for any discriminant. Checked.
- Smell test: Prop 5.10 holds for EVERY d, which is right - it is a local identity cu - Delta v = Delta(w - h_Q). The
  [CORRECTED: wrong - Prop 5.4 (5.2 above) also uses large d] other place where Pfaffian (d = 14) etc. can fail is Section 6, where s = w - h_Q must be
  made independent of the surface subfield k "for uniformly large test degree". So Section 6 must contain a step that
  genuinely fails for d = 14; find it and check that it uses large d where it says.

SECTIONS 4 AND 5 COMPLETE (12 Nov 17:5x): no gap; one harmless sign misprint in (5.5). Next: Section 6 (line 2131).

## 6 The intrinsic correction (lines 2131-2475): no gap
- 6.1 (6.1)-(6.2): candidate sigma_k = u(Delta_k) + [r_k = 3] (1/2) u(P_k), intrinsic to (k in L, alpha) (unique
  genus-zero model, residues at its DVRs). Integrality: a P_k factor fixed by complementation carries a field
  involution over k, hence a nonidentity birational, so biregular, automorphism of a test K3 - excluded by the choice
  of test surfaces with trivial Aut. Checked.
- 6.2 Lemma 6.1 = ONE OF THE PLACES WHERE LARGE d ENTERS (with Prop 5.4 and Lemma 6.3; see CORRECTION at the end). Purity step: on the SNC resolution the
  coniveau complex has d^2 = 0, so at a codim-one point z of D_i off the other components the secondary residue of the
  quadratic residue a vanishes, ord_z(a) even, the double cover is unramified in codim one, and Zariski-Nagata purity
  makes it etale on the open. Degrees r_k <= 7, 2 r_k <= 14, |P_k| = 8. Hurwitz (6.3) 2g-2 <= n(2h-2) + b(n-1) with
  n <= 14 and h, b from the bounded family. Lemma 4.1 (re-derived: F = pi*(nL) - sum m_i E_i*, F^2 = 0 gives
  sum m_i^2 = n^2 d, 2g-2 = K_Y.F = sum m_i >= n sqrt d) contradicts this once d is large. Over a curve Q the same on
  geometric components, with C(Q) in k giving the map to Q. Checked.
  SMELL TEST PASSED: this is a genuine large-d step (for d = 14, sqrt 14 < 4, a bounded family easily carries genus-3
  pencils), so the Pfaffian / C26 / C38 / C42 rational cubics can fail here [CORRECTED: not only here - see CORRECTION at the end]. It is also
  consistent with Hassett-Lai's Cremona map of P^4 (blows up one degree-12 K3, contracts over a derived-equivalent
  one): both lie in the same test collection, net cu = 0, as Theorem 6.6 requires.
- 6.3 discrepancies: blow-up of a codim-l centre in r <= l components, l - 1 - cr >= l(1-c) - 1 >= 1 - 2c > 0; any
  exceptional prime a >= 2(1-c) > 1; so the log MMP outputs stay terminal pairs (epsilon-lc, epsilon >= 3/4) and the
  bounds of Thm 4.9 / 4.11 apply. (6.6): -2 + c r_k <= -2 + 7c < -1/4 since c < 1/4. Checked. The marked support in
  the 3-dim log programme is the boundary itself, so the Remark 4.8 caveat is met automatically (log boundedness of
  (Z, cD) with c fixed bounds Supp D).
- 6.4 Prop 6.2: relative MMP steps over a model of k' are absolute steps (NE(Z/S') is a face of NE(Z)), so both
  outputs are Sarkisov related (Hacon-McKernan) from the common start. A link with 2-dim common base keeps the
  embedded surface field (birational connected-fibre contractions between surfaces); first departure has dim Q <= 1,
  Thm 4.9 bounds its geometric generic diagram, ramification points on C_k are horizontal divisors, Lemma 6.1 gives
  sigma_k = 0. Checked.
- 6.5 Lemma 6.3: fixed Hilbert polynomial (a/2) m(m+1) + 2m + 2 picks out F^2 = 0, -K.F = 2 (RR re-derived), an
  open-closed proper quasi-finite, so finite etale, piece of the relative Picard scheme; fibres A(S) (5 or 3);
  bounded-cover exclusion. Checked. Prop 6.4: (6.7)-(6.8) coefficient a(F,T,cD_T) - 1 + c eps_F; E b-exceptional and
  b-nef so E <= 0 by negativity (applied to -E); hence every extracted valuation has a <= 1, which is the
  terminalization list of Thm 4.11 for the bounded klt log Fano (T, cD_T) of Cor 4.13 - this is the dim Q <= 1 conic
  end Cor 4.13 covers, so the second carry-forward is met. Non-pseudo-effectivity from a covering family of curves
  avoiding the centres; MMP over Q to a bounded Z/B; comparison by first departure (Lemma 6.1 over Q') or directly
  (B a surface with C(B) = k, C(Q) in k). Checked.
- 6.6 Thm 6.5: s is a NODE function (nonzero candidate => unique eligible field), which is what lets two adjacent
  links agree on it. Thm 6.6: H_Q = Delta s in every dim Q: dim Q <= 1 both zero; dim Q = 3 conics identified;
  dim Q = 2 case (ii) h_Q = -u(Delta_k), s = w - h_Q, so H_Q = Delta w - Delta h_Q = Delta s (k = C(Q) eligible by
  r_k = 8 - K_W^2 <= 7); case (i) s is invariant under abstract isomorphism of (L, alpha), so Delta s = 0 with no
  discriminant bound. Telescoping with Lemma 2.4: v = s = 0 over a point. d-bounds come only from the finitely many
  families fixed after (6.4). Checked.

SECTIONS 4, 5 AND 6 COMPLETE (12 Nov 18:0x), one reader (an agent): no gap; one harmless sign misprint in
(5.5). Cited inputs taken as stated: Birkar BAB (via Thm 4.9), BCHM / Hacon-McKernan Sarkisov, the terminalization
bound Thm 4.11, Hassett's lattice theorems, BLMNPS Cor 29.7. Not yet read by me: Sections 1-3 and 7 in full (Prop 3.10
smell-tested only). A second, independent reader is still needed before anything is called verified.

## 7 Cubic fourfolds of admissible discriminant (lines 2476-2636): no gap
- Prop 7.1: test collection = Picard-one K3s with T_S(-1) = T_X; trivial Aut by Lemma 3.9 needs d > 2 and the
  proof takes d0 > 2. Pic X = Z O(1), -K = 3H, so both ends are Mori fibre spaces over a point; Prop 3.10 (cu = 1)
  against Thm 6.6 (cu = 0). Checked.
- Lemma 7.2: Hodge loci of rational classes and of rational endomorphisms are closed algebraic (Cattani-Deligne-
  Kaplan) and proper because the period quadric spans P(T x C); |det T_X| = det A_X = d by the unimodular
  discriminant-group identity; simplicity from h^{3,1} = 1. Checked (standard).
- Thm 1.1 and corollaries: d = 2.7^j admissible (2.7^j = 2 mod 6, 4 and 9 do not divide, 7 = 1 mod 3); d = 2n^2+2n+2
  is 0 or 2 mod 6 (n(n+1) even) and meets Addington's (***), with F(X) birational to S^[2]; Voisin Thm 5.6
  (4 does not divide d) gives universally trivial CH_0. If the paper holds, Cor 1.4 gives irrational cubic fourfolds
  with universally trivial CH_0 - a large claim, it would be the first such cubic fourfolds. Arithmetic checked.

## 3.5 Lemmas 3.8, 3.9 and Prop 3.10 (lines 833-914): no gap GIVEN Theorem 3.3
- My worry: integral indefinite lattices have no unique orthogonal decomposition, so "the block in class [T_M]"
  could be ill defined. Lemma 3.8 avoids it: the blocks are read off the primitive central idempotents of the
  operator algebra (= Q^m on the whole summands), which Theorem 3.3 makes intrinsic and compatible with blowups in
  both directions; a removed centre is a factor Q, hence one of the historical idempotents, even when two blocks are
  Hodge isometric. The integral lattices are then the saturations of the rational subspaces. Logic checked.
- Lemma 3.9 (re-derived): p_g = 1, rank T = 21. Minimal model: K nef, Noether c2 = 24 - 12q - K^2, e = 2 - 4q + b2,
  so b2 = 22 - 8q - K^2; b2 >= 22 forces q = 0, K^2 = 0, rho = 1; kappa 2 needs K^2 > 0, kappa 1 has an isotropic
  fibre class (rho >= 2), so K3. disc NS = L^2 = |disc T|; Aut acts by +-1 on T, -1/+1 gluing needs 2-torsion
  discriminant, impossible for d > 2; Torelli. Checked.
- Prop 3.10: final transcendental structure simple (h^{3,1} = 1), so one block; additions minus removals in its
  isometry class = 1; each such centre is birational to a member of S (Lemma 3.9) and conversely; curve and point
  centres give P^2 / P^3 bundles with MRC base a curve or point, uncounted; exceptional P^1-bundles have MRC base the
  centre (Lemma 2.2). Checked.
- EVERYTHING ON THE SMOOTH SIDE NOW RESTS ON THEOREM 3.3 (the operator algebra and its blowup decomposition, built in
  3.1-3.4 from degeneration to the normal cone and local path tensors; refs [1], [3] are Gromov-Witten degeneration
  papers). Next: read 3.1-3.4 (lines 386-832). This is the place a second reader should look hardest, together with
  Lemma 6.1.

## 3.1-3.4 The operator algebra G_M and Theorem 3.3 (lines 378-832): no gap
- G_M = unital algebra generated by the operators A_B of all connected genus-zero descendant GW invariants with two
  transcendental variable insertions and diagonal other insertions; each A_B is a Hodge endomorphism, so G_M lies in
  End_Hdg(T_M).
- The question that matters: blowing up a K3 centre Z whose T_Z(-1) is Hodge isometric to T_M makes End_Hdg(T_Y) =
  Mat_2(Q), so a priori GW operators could MIX the two blocks and Lemma 3.8's idempotent bookkeeping would fail.
  The paper proves they do not mix:
  Lemma 3.4 (local): on the bundle pieces over Z, positive projected degree has evaluation image in curves (Z is
  not uniruled since p_g > 0), so the 2-form pulls back to zero and the tensor kills W; projected degree 0 gives a
  rational multiple of q_Z. Checked.
  Lemma 3.5 (path): side branches give diagonal outputs; Hodge difference 2 runs along the path; one mixed vertex
  kills a path. Checked.
  Lemma 3.6 (relative (Y, D), pulled-back insertions): B_abs = C B_rel + R with C a nonzero product of Hu-Li-Ruan
  fibre numbers (3.5), R earlier in a well-founded triangular order (ample degree, number of ordinary marks, list
  length, total contact, hyperplane exponents). The mixed absolute tensor is ZERO because the translated insertion
  tau(i_* delta) with delta in W has i_* W = 0 in H^6(M, Q) (Lemma 3.1). So a W class on D cannot pair with T_M,
  even when the two are Hodge isomorphic. This is the decisive step and it is sound.
  (3.6) by degenerating Y along D with exceptional insertions lifted to the zero section. Checked.
  (3.7) exceptional line, re-derived: moduli D x_Z D, expected dim (-K_Y.e = 1) 1 + 4 - 3 + 2 = 4, unobstructed
  (N = O(-1) + O^2), integral (-xi p*u)(-xi p*v) = int_Z uv; against the form -q_Z it is minus the projector on W, and
  T_M insertions restrict to 0 on D. Checked.
  Lemma 3.7 (divisor version, arbitrary insertions; r = 1 tails, weights k - 1 + codim delta, positive leading
  coefficients and divisor-equation factors) and the recovery G_M = pr_M G_Y: degenerate an M generator along Z, a
  path between two main vertices passes a boundary copy of W and dies on a mixed vertex. With (3.6) and the
  complementary projector, G_Y = G_M + Q id_W as algebras. Checked.
- Consistency: at the cubic, G_X lies in End_Hdg(T_X) = Q and contains 1, so it is Q, one block, as Lemma 3.8 needs.
- Technical inputs taken as stated: Abramovich-Fantechi degeneration formula with ordinary descendants (Thm 0.1,
  Prop 4.14, Cor 4.15), Abramovich-Marcus-Wise comparison with Jun Li, Hu-Li-Ruan's relative-to-absolute translation
  and Thm 7.1, Maulik-Pandharipande Section 2.4 Lemma 4.

## 2 Fields and the divisorial cocycle (lines 246-377): no gap
- u = 1 iff the MRC quotient is birational to a test K3 (d > 2, Pic = ZL, trivial Aut); Bir(S) = Aut(S) for K3s by
  the two-form argument; Lemma 2.2 by Graber-Harris-Starr; Lemma 2.3 (an automorphism of the field kills u); cu is
  the Lin-Shinder divisorial invariant composed with u, additive by indicator functions (Lemma 2.4); blowup values
  u(Z_i) with sign; weak factorization (AKMW) with RC intermediate fourfolds, only surface centres can count. Checked.

## CORRECTION (12 Nov 18:1x) to the 5.5 and 6.2 smell-test lines and to push 111
I wrote that large d enters the Sarkisov side only at Lemma 6.1. Wrong, and my own 5.2 entry above already said so.
Large d enters in three places:
  (a) Prop 5.4, for links whose common base is a point or a curve (Theorem 4.3(i)/(iv) with Lemma 4.1);
  (b) Lemma 6.3, for del Pezzo ends over smaller bases;
  (c) Lemma 6.1, for the conic ramification fields (used in Prop 6.2 and Prop 6.4).
For the Pfaffian (d = 14) the escape is (a): its classical birational map to P^4 blows up a K3 centre in a bounded
diagram over a point, and Lemma 4.2's bound d <= A^2 + (A.K)^2 does not exclude d = 14. So for d = 14 one gets
H_Q = 1 at that link, consistent with cu = 1 from Prop 3.10. The smell test still passes: every d-dependent step is
a bounded-family exclusion that is weak at small d, and no step claims anything for d = 14.

WHOLE PAPER READ (Sections 2-7; Section 1 is the introduction), one reader, 12 Nov 18:1x. No gap found. One harmless
sign misprint in (5.5). The two places a second reader should press hardest are Theorem 3.3 (GW operator algebra,
no-mixing via i_* W = 0, Lemma 3.6) and the boundedness chain Theorem 4.9 -> Prop 5.4 / Lemma 6.1.
