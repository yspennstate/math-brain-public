# LO05: the modularity of r_2 without [49] (12 Nov 2026; route checked against LO05 and the published statements)

LO05 Section 4.7 (lines 1635-1680 of lit/openai_oct6/paper_c.txt) uses [49, Theorem 1.1], Fontaine-Mazur at 2
with no residual-image hypothesis, once: to show that the 2-adic representation r_2 is the representation of a
weight-two newform f. [49] is a new, long (about 2,400 lines) and unrefereed proof. The representation it is
applied to is of a special kind, and its modularity appears to follow from results established since 2009.

Setting (LO05 4.6-4.7). A is a principally polarized abelian surface over a number field L with
End_L'(A) tensor Q = B, B the indefinite quaternion algebra of discriminant 210. For g in G_Q there is a
quasi-isogeny mu_g: gA -> A commuting with B; the defect of g -> mu_g is a sign cocycle eps, corrected by a
cochain beta with values in mu_2m (Tate's vanishing of H^2(G_Q, Q-bar^*) in the form LO05 uses). Then
R_l(g) = beta(g) mu_g o g is a representation of G_Q on V_l(A), commuting with B, and R_l = r_l + r_l.

Route.
1. The family (r_l) is compatible. beta takes values in mu_2m and does not depend on l; at a good prime q the
   trace of R_l(Frob_q) is beta(Frob_q) times the trace of mu_g o Frob_q on the good special fiber, an algebraic
   number independent of l. This is the argument of LO05 Lemma 4.6, which carries it out for l = 2 and 3; it uses
   nothing about those two primes. Since R_l = r_l + r_l in characteristic zero, tr r_l = tr R_l / 2 is
   independent of l as well.
2. Each r_l is odd, absolutely irreducible, has Hodge-Tate exponents 0, 1, and is unramified outside T and l
   (LO05's own checks, which do not use l = 2). For l outside T, A has good reduction above l over L', so r_l is
   potentially Barsotti-Tate at l.
3. Big residual image. If A has CM over Q-bar, r_l is induced from a Hecke character of an imaginary quadratic
   field and is modular by Hecke's theta series. Otherwise, by Ohta's theorem for QM abelian surfaces, the image of
   G_L' on the Tate module is open in (B tensor Q_l)^* = GL_2(Q_l) and, for all but finitely many l, contains
   SL_2(Z_l) up to the identification. So for a large prime l the residual representation of r_l restricted to
   G_Q(zeta_l) is absolutely irreducible.
4. Fix such an l >= 5. Serre's conjecture (Khare-Wintenberger, with Kisin) makes the residual representation
   modular; Kisin's modularity lifting theorem for potentially Barsotti-Tate representations at an odd prime makes
   r_l modular, of weight two after the Tate twist fixed by the exponents 0, 1.
5. r_2 has the same Frobenius traces as r_l at almost all primes (step 1); both are semisimple, so by
   Chebotarev and Brauer-Nesbitt r_2 is the 2-adic representation of the same newform f. The same comparison gives
   r_3, which is what LO05 Lemma 4.6 needs.

An equivalent formulation: (A, mu, beta) is a building block in Ribet's sense, a Q-bar factor of an abelian
variety of GL_2-type over Q (Ribet, Pyle); such varieties are modular by Ribet's reduction to Serre's conjecture
and Khare-Wintenberger.

Checked against LO05 itself:
- Lemma 4.6 (lines 1686-1712) defines alpha_q = (1/2) beta(g) a_g Tr(u_q) with u_q = red(mu_g) o Frob in End^0
  of the special fiber and states that its characteristic polynomial is rational and independent of the
  coefficient prime (Mumford/Milne [40, I, Thm 10.9, Prop 10.20]); nothing in it is special to 2 or 3. Step 1 holds.
- The CM case does not arise at the modularity step: fibers with extra endomorphisms (C_B = k, A ~ E^2 with E a CM
  curve) are bounded separately by class-number growth (lines 1112-1124, 1492-1502), and Section 4.7 treats only
  the other fibers, where End_Q-bar(A) tensor Q = B. So step 3 needs only the non-CM QM case.

Checked against the sources (12 Nov 2026):
- Jacobson-Ohta, as stated in Dieulefait-Rotger, The arithmetic of QM-abelian surfaces through their Galois
  representations (arXiv math/0303162), Theorem 1.4, citing M. Ohta, J. Fac. Sci. Univ. Tokyo 21 (1974) 299-308, and
  M. Jacobson, Uspekhi Mat. Nauk 29 (1974): for A/K with QM by a maximal order O in a division quaternion algebra,
  and H = Gal(Q-bar/L) for the field L of definition of the endomorphisms, rho_l|H = sigma_l + sigma_l with
  sigma_l: H -> Aut_O(T_l(A)) = (O tensor Z_l)^*, and sigma_l is surjective for almost every prime l. LO05's order
  need not be maximal, but an isogeny over L' moves A to a surface with a maximal order; that changes T_l for finitely
  many l and leaves V_l unchanged. For l outside disc(B) = 210 and the exceptional set, (O tensor Z_l)^* = GL_2(Z_l),
  so the residual image of G_L' is GL_2(F_l), and on G_L'(zeta_l), the kernel of det, it is SL_2(F_l). On an open
  subgroup r_l agrees with sigma_l up to the finite character beta, so for l >= 5 its residual representation is
  absolutely irreducible on G_Q(zeta_l), and so on G_Q(sqrt(l*)), l* = (-1)^((l-1)/2) l. Step 3 holds.
- Kisin, Moduli of finite flat group schemes, and modularity, Ann. of Math. 170 (2009) 1085-1180, the theorem of the
  introduction: p > 2, rho: G_Q,S -> GL_2(O_E) continuous with det = cyclotomic times a finite character;
  (1) rho-bar absolutely irreducible on Q(sqrt(p*)), (2) rho-bar modular, (3) rho potentially Barsotti-Tate at p;
  then rho is modular (Corollary 3.5.8 states it over E). For r_l at the l of step 3: det r_l is a character of
  G_Q that is Hodge-Tate of weight one and unramified outside T and l, so it is the cyclotomic character times a
  finite character; (1) holds by step 3; (3) holds because A has good reduction above l over L' and beta has finite
  order. (2) is Khare-Wintenberger (Serre's conjecture, Invent. Math. 178 (2009)) for the odd, absolutely
  irreducible rho-bar; oddness is LO05's own check (step 2). Step 4 holds.

So [49] is not needed for LO05: the one use of it in Section 4.7 follows from Jacobson-Ohta, Khare-Wintenberger
and Kisin. The inputs in step 2 (oddness, ramification, Hodge-Tate exponents) are LO05's own and were checked in
the Section 4 read.

What this changes: LO05 does not depend on [49]. The unrefereed parts of the proof are LO05 itself and [48], both
now read once with no gap. The second independent audit is still open, so LO05 stays REPORTED_SOLVED.
