C0033F second check (an agent, Claude Opus 5.5, 14 Nov 2026 05:0x-05:3x laptop time; not the writer of C0033F,
which is Codex GPT-6.1 on Mac mini 1). Verdict on what was checked: Theorem 1 CONFIRMED (numerically, and the proof of the
bound (5) re-derived by hand). The status of C0033 stays PARTIAL, as the report says: full three-point concavity is open.

Method (c0033f_check.py, written from REPORT.md's statements only; the true margin uses c0033e_core.py, the code of the
independent C0033E check, not any script of the run). The true margin m = det(-D^2 H)/det(J) of the 3x3 matrix
Q_x = [[a, sqrt(x) v*], [sqrt(x) v, C]] at x = 1e-60 (mpmath, 250 digits, all nine ambient directions), against
formula (4) m0 = (1 + K/det W * eta^T N_C^{-1} eta)^{-1}, with F_C, N_C, W, eta built from the two-point atoms of C in
the basis E22, E33, E23+E32, i(E23-E32). The identity -D^2 H = J - d z z^T held entrywise (relative error < 3e-72), and
the two expressions for W in (3) and (15) agree to 1e-249.

Theorem 1, formula (4): six cases, (a; b, c, r; phase of C23; v):
  (0.3; 0.4, 0.6, 0.2; 0; complex v)     m = 0.739785698409053, (4) = 0.739785698409183
  (0.8; same block and v)                m = 0.739785698409236, same (4)  (independence of a)
  (0.5; 0.1, 0.85, 0.25; 0; complex v)   m = 0.527265041733329, (4) = 0.527265041733315
  (same, phase 0.9 on C23)               m = 0.544722609592213, (4) = 0.544722609592247  (complex block)
  (0.05; 0.02, 0.03, 0.015; 0; complex)  m = 0.905686205479024, (4) = 0.905686205479018  (small block)
  (0.6; 0.97, 0.5, 0.1; 0; v = e_2)      m = 0.455090141686561, (4) = 0.455090141686582  (one connection zero)
Agreement is 6e-15 to 1.3e-13 in every case. The residual is the finite-difference error of my margin code (the two values
of a differ from each other by the same amount), not the O(x) remainder of (7).

Bound (5) m0 >= 1/(2K+3): 4000 random strict blocks (eigenvalues uniform, or within 1e-1..1e-8 of 0, of 1, or of both;
random rotation; random complex unit v), 90 digits. No violation. The smallest m0*(2K+3) is 1.529, at small K (0.03). So
the constant in (5) is not sharp; the data are consistent with m0 >= 1.5/(2K+3).

By hand: Lemma 3.1 (the three eigenvalue identities from (12), lambda^2 <= P/B0 <= 1/(4(e^K - 1)), e^K - 1 >= K^2,
s2 <= 1/(2(e^K - 1)) + (p+q)/2, the eigenbasis inequality behind (14)), the identification of W with the Fisher operator of
A0 = Re(vv*) (Jacobi's formula D pi_T[A] = pi_T tr(M_T^{-1} A)), F_C(A0, A0) >= 2, and the chain
K/det W * eta^T N^{-1} eta <= 4 K s2 <= 2(K + 1) giving (5). All correct.

Also read: the global search (data/global_optimization.json) gives Lambda*m = 0.5224, 0.5056, 0.5022 at Lambda = 20.7,
80.2, 200; no negative margin anywhere. The report body has no section for this search (its task 2); the numbers are only
in the data file.

Not checked: the constants 10^30 and mu^15 of Theorem 2 (7)-(9) (only that the leading term is right), Proposition 3's
interval cover, the boundary classification of Section 6 beyond reading it (Lemma 6.1's proof was read and is correct).
