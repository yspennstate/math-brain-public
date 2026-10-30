# T228_B_v1 section 4: self-audit against ABB (src/ABB.txt), agent AF, 21 Oct 2026 19:4x

Review point 1 (does ABB use continuity of Psi beyond existence?) checked line by line on the pdftotext of arXiv 2102.02299v2.

- "continu"/"Feller" applied to Psi occurs at: line 9 (abstract), 45-55 (assumption (1), "by (1), has the Feller property"),
  482 (an example IFS), 2576 (Prop 9.1: "Since (X_n) is also a Feller chain ... Krylov-Bogoliubov"). Nowhere else.
- Lines 1760-2540 (rest of the proof of Thm 2.1, Sections 6-8, Prop 8.1 and Lemmas 8.2-8.4): no occurrence of
  "continu" or "Feller" at all (awk scan).
- The other hits are not about Psi: 821-851 continuity of rho(theta) (Lemma 4.2); 1508/1555 a.e. continuity of a dRi g.
- Lemma 3.1 (30)-(32): induction on (4) and Lip(Lambda) only.
- Lemma 5.1 (moments of R): Lemma 3.1 + (69)-(70) + R stationary; no continuity.
- Lemma 5.2 (dRi of h): (4), (67), (68), moments (71); phi in C_c, Psi only through (4).
- Proof of Thm 2.1: R ~ nu stationary, independent of (Psi, Lambda); identity (76) is a telescoping of
  E phi(e^{-t} Psi(R)) - E phi(e^{-t} Lambda(R)) along the MRW, which needs Psi(R) =d R, i.e. invariance of nu, nothing else.
- Prop 9.1 is the only place continuity enters, and T228_B section 3 replaces it by Harris recurrence.

Verdict on review point 1: holds. The jump of Psi at 0 is never used by Thm 2.1 or Prop 8.1. Goldie fallback not needed.
Points 2-4 still with the reviewer (agent H). Not an acceptance: a self-audit only.
