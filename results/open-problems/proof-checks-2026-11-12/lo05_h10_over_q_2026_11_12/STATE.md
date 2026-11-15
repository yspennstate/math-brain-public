# LO05 state (an agent, 12 Nov 2026)

Done: both versions of the OpenAI preprint fetched (identical apart from dates), introduction, proof
strategy, Section 5 and the head of Section 4 read; Sun's follow-up (arXiv 2610.20691) introduction read;
three dated searches; lo05_check.py run (under a minute), output lo05_check.out.

Result: LO05_CHECK.md. Keep REPORTED_SOLVED.

Open, in order of value:
1. Read the two cited OpenAI preprints' statements and outlines: Fontaine-Mazur modularity at the prime 2
   (openai/math tree b01dad92005597ad3c3da844f61b93ba8afd55e8) and the pointwise 2-converse
   (tree 1209ef2da6ee8e6cc395c246b660f2e93302d20f). The row depends on both.
2. Section 4.2-4.9 of the preprint (the height estimate), lines 1101-1861 of lit/openai_oct6/paper_c.txt.
3. Section 3 (pole parity), lines about 880-1100.

Not pushed: the three PDFs and their text under lit/.

12 Nov 15:14: item 1 done (LO05_CITED_INPUTS.md). Both companions fetched from openai/math (blob hashes match);
their Theorem 1.1 statements and the coefficient and weight conventions match the paper's use in Section 4.7 and
Lemma 3.4, with no hypothesis gap. Their proofs are unread. Still REPORTED_SOLVED. Next: item 2 (Sections 4.2-4.9),
then item 3. The two companion PDFs are under lit/fm2 and lit/conv2, not pushed.

12 Nov 15:23: item 2 done (LO05_SECTION4_CHECK.md). Section 4 (lines 1101-1861) read line by line, every step
re-derived: genus and branch count of the quaternionic quotient, Lemma 4.1 (odd contact), Lemma 4.2 (theta and
Faltings heights), Lemmas 4.4-4.5 (field of definition, sign splitting), Lemma 4.7 (level N <= C M^2), Lemma 4.8
and the final bound h_F(A) <= C M^C. No gap found. Cited statements of Carayol, Gaudron-Remond, Javanpeykar and
Pazuki checked against the forms quoted, not against the sources. Still REPORTED_SOLVED. Next: item 3 (Section
3's other lemmas), then Section 5 and Section 2.

12 Nov 15:33: item 3 done (LO05_SECTION3_CHECK.md). Section 3 (lines 738-1100) read line by line, every step
re-derived: Lemma 3.1 (no odd poles outside S1), the weak-approximation choices and Lemma 3.2, Lemma 3.3 (the
two-Selmer count, including the 2-adic step and the matrix identities), Lemma 3.4 (rank one via [48] and
Cassels-Tate), Lemma 3.6 (one n for both twists: K# and T, the row checks of K1_B = 0, M0 nonsingular, the
J-diagonal toggles, Dirichlet). No gap found. Still REPORTED_SOLVED. Next: Section 5 (from line 1862), then
Section 2's reduction.

12 Nov 15:38: item 4 done (LO05_SECTION5_CHECK.md). Section 5 (lines 1862-1985) read against Propositions 2.1
and 2.2, arithmetic redone by hand: norm of d, class number one, the point Q (w^3 - w = -8d), |im alpha| = 8 by
signs, im alpha' = 1 (-4 = 3 not a square mod 7), rank one; the formal-logarithm valuation and truncation
bounds (2.6), (2.7). No gap found. Still REPORTED_SOLVED. Next: Section 6 (the prime patterns), then Section 2's
reduction.

12 Nov 15:47: item 5 done (LO05_SECTION6_CHECK.md). Section 6 (lines 1986-2397) read line by line: Cor 6.2, the
reduction orders and their 2-part, the catalogue, the Green-Tao-Ziegler lower bound (6.12), the Selberg sieve
Lemma 6.3 with (6.18), (6.19), the bad-prime count (6.20), the fiber sieve (6.23) and the union bound (6.24).
No gap found. Still REPORTED_SOLVED. Next: Section 2's reduction (lines about 305-737), then the companions'
proofs.

12 Nov 15:52: item 6 done (LO05_SECTION2_CHECK.md). Section 2 (lines 225-719) read line by line: the point data
and eta, Lemma 2.3 (local comparison), the theory T and its integer model, the finite tests and compactness
(Lemma 2.9), the odd-contact step (2.18), Lemma 2.10 (coarsening by J selects a tested branch), Prop 2.11, and
the height contradiction (Prop 2.12). No gap found. Every section Theorem 1.1 uses (2-6) has now had one
independent read with no gap; Section 7 is not used and was not read. Still REPORTED_SOLVED: the companions'
proofs are unread and a second independent audit is needed; asked an agent on the mesh.

12 Nov 16:05: item 7 part 1 (LO05_CONV2_CHECK_S1_S3.md). Companion [48] (pointwise 2-converse), Sections 1-3
(lines 51-938) read line by line: binary congruences by Chevalley-Warning (Lemma 3.4), the positive complex
and its residual concentration (Lemmas 3.5, 3.6), fixed-form Kato classes and unsmoothing, the local Euler
corrections, the uniform integrality (3.12), the central determinant formula (Prop 3.7), Theorems 3.1, 3.2.
No gap found. LO05 Lemma 3.4 uses [48] at corank at most one, so both halves are needed; Sections 4-9 (the
corank-1 case) and [49] are next. Still REPORTED_SOLVED.

12 Nov 16:16: item 7 part 2 (LO05_CONV2_CHECK_S4_S5.md). Companion [48], Sections 4-5 (lines 939-2531) read line
by line: ring-class interpolation (Lemmas 4.3-4.13, Prop 4.6, Thm 4.14), Kolyvagin derivatives at 2 (Lemma 5.2),
the determinant switch and rank reduction (Lemma 5.3, Props 5.5, 5.7), the central valuation formula (Prop 5.10,
with the Cassels-Tate isogeny identity), Cor 4.1, the clearing lemmas 5.11-5.15, the transfer (Lemma 5.17) and
Theorem 4.2. No gap found. Sections 6-9 and [49] are next. Still REPORTED_SOLVED.

12 Nov 16:31: item 7 part 3 (LO05_CONV2_CHECK_S6_S9.md). Companion [48], Sections 6-9 (lines 2532-5566) read line
by line: auxiliary twists (Section 6), the coefficient systems and Gross lifts (Section 7), arithmetic graphs and
the matrix-tree count (Section 8), and the assembly (Section 9: Prop 9.10, non-circular; Lemma 9.12; Prop 9.14,
the corank-one base; the proof of Theorem 1.1). No gap found. All of [48] has now had one independent read.
[49] and the second audit are still open. Still REPORTED_SOLVED.

12 Nov 16:36: item 8 part 1 (LO05_49_BYPASS.md). LO05 uses [49] once, to make r_2 modular. r_2 comes from a non-CM
abelian surface with quaternion multiplication made into a G_Q-representation by quasi-isogenies, and the family
(r_l) has l-independent traces by LO05's own Lemma 4.6. That gives a route through Ohta's open image, Khare-
Wintenberger and Kisin at a large odd l, then trace transfer to r_2, which would make [49] unnecessary. Ohta and
Kisin still to be checked against the sources. Still REPORTED_SOLVED.

12 Nov 16:45: item 8 part 2 (LO05_49_BYPASS.md, sources section). The route around [49] holds against the published
statements: Jacobson-Ohta (as stated in Dieulefait-Rotger, Theorem 1.4) gives the residual image SL_2(F_l) on
Q(zeta_l) for a large l, and Kisin's theorem in Ann. of Math. 170 (2009) (p > 2, det cyclotomic times finite,
residual absolutely irreducible on Q(sqrt(p*)), residually modular by Khare-Wintenberger, potentially Barsotti-Tate)
makes r_l modular; traces carry it to r_2. LO05 does not depend on [49]. The proof's unrefereed parts are LO05 and
[48], both read once with no gap. Second audit still open. Still REPORTED_SOLVED.
