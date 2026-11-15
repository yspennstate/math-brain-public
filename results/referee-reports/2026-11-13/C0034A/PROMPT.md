Open problem C0034. Source: R. Lyons, "Determinantal probability: basic properties and conjectures", Proc. ICM 2014,
arXiv:1406.2707, Question 2.8, p. 6: given H = H_1 (+) H_2 an orthogonal decomposition of a closed subspace of l^2(E)
(E finite or countable), is there a coupling of the determinantal measures P_{H_1} and P_{H_2} whose union has law P_H?
(Since |X_1| = dim H_1, |X_2| = dim H_2 and |X_1 u X_2| = dim H a.s. for finite E, such a coupling has X_1, X_2 disjoint.)

Earlier work here (numerical only): exact-LP feasibility in double precision (HiGHS, zero violation) on 1360 random
orthogonal pairs with |E| = 3..6, generic |E| = 7, 8, Fourier subspaces on cycles 5..8, and star-space splits of the K_4
edge space; the naive "condition X_2 on X_1" splitting fails. No proof, no exact certificate.

Do this, in order, saving as you go:
1. Literature first. Download arXiv:1406.2707 into sources/ (text only, no page images) and read Section 2. Search for
   later work (2014-2026): couplings of determinantal/strongly Rayleigh measures, "union of determinantal processes",
   Lyons' later papers, Borcea-Branden-Liggett strong Rayleigh, negative dependence and couplings (Lyons 2003 Theorem 6.2
   coupling for H_1 subset H, stochastic domination), Pemantle-Peres, Anari-Oveis Gharan-Vinzant, Bufetov-Qiu-Shamov
   (Lyons-Peres conjecture), Kassel-Levy, and any paper that cites Question 2.8. If it is answered in print, give the
   exact reference and theorem, and stop with REPORT.md first line RESOLVED_IN_LITERATURE.
2. Prove special cases rigorously: (a) dim H_1 = 1 (H_1 = span u): construct the coupling explicitly (e.g. choose e with
   prob |u_e|^2 and X_2 from a suitable conditional law) and prove the union law is P_H using the Cauchy-Binet /
   Plucker structure of the minors; (b) dim H = |E| - 1 or other small codimension; (c) H spanned by coordinate-
   orthogonal pieces. If (a) works, try induction on dim H_1 via H = H_1' (+) span(u) (+) H_2 and composition of couplings
   (check whether the composition preserves the needed marginals).
3. Exact certificates. For rational-kernel instances (rational orthonormal bases, e.g. from integer orthogonal matrices or
   Cayley transforms), solve the transportation feasibility LP in exact rational arithmetic (fractions / a rational
   simplex, or verify a floating solution exactly after rounding to a rational vertex) for |E| <= 7 across all splits;
   search adversarially (optimise the violation over the Grassmannian) for an infeasible instance.
4. If you find an infeasible instance, certify it with an exact Farkas dual vector. Otherwise state what you proved.
Write REPORT.md. Its first line is exactly one of PROVED, COUNTEREXAMPLE, PARTIAL, NO_PROGRESS, RESOLVED_IN_LITERATURE
(PROVED means the full question answered yes for finite E with proof). Then the statement, the proof or certificate,
what was checked and how, and the literature result. Keep LOG.md as you go. Code in code/, data in data/. Work only in
this directory. At most 4 threads, under 4 GB, nice 10. No publication anywhere, no pushes.
