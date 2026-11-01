# T228 B v1, self-audit 2: review point 1 (continuity of Psi in ABB)

agent AF, 21 Oct 2026 20:5x. A reading of the arXiv v2 text (src/ABB.txt, 2,824 lines). This is my own check,
not the outside review; agent H's verdict is still owed.

Every occurrence of "continu" or "Feller" in the text:
- line 9 and (1) at line 45-47: the standing hypothesis; line 55 draws the Feller property from it.
- line 482: example 2.1.3 (IFS on the unit interval), not used later.
- line 600: Lipschitz continuity of a test function f, not of Psi.
- Lemma 4.2 (line 821-851): continuity of the spectral radius in theta.
- lines 1508, 1555: continuity of a directly Riemann integrable g.
- line 2576, Prop. 9.1: "(X_n) is also a Feller chain", used for Krylov-Bogoliubov existence.

How sections 5 and 8 touch Psi:
- Lemma 5.1 writes P[|R| > t] = P[|Psi_1 o ... o Psi_n(R)| > t] (stationarity of nu, R independent of the maps) and
  bounds it with Lemma 3.1, which rests on (4) alone.
- Lemma 5.2 and the renewal step evaluate phi(e^{-x} Psi(R)) for phi in C_c(R): continuity is required of phi, and
  Psi(R) enters only through (4), (67), (68) and the bound M <= |Lambda(R)| + B.
- Prop. 8.1 uses Z_n = Psi_1 o ... o Psi_n(X_0) with X_0 ~ nu and Lip(Lambda_n) = |A^-_n| v |A^+_n|; again (4) and the
  linear part only.

Reading: outside Prop. 9.1, the paper needs Psi to be measurable, to satisfy (4), and to have a stationary law nu given
by some other means. In T228 that law comes from Harris recurrence (section 3 of v1), so the jump of Psi at 0 is never
used. The constant formula (82) evaluates Psi at R ~ pi, and pi({0}) = 0, so the value gamma = sigma'(0) cannot enter.

What would break this reading: a step in sections 6-8 that I read only by search (no "continu" hit) using weak
convergence of the chain's transition kernel (Feller in disguise). I found no "weak" or "in distribution" in sections
3-8 applied to the chain. The Goldie fallback in v1 section 4 stands regardless.
