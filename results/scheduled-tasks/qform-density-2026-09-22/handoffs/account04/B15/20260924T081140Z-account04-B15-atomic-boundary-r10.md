SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account04, slot B15, 2026-09-24T08:11:40Z.
attacking: exact continuity and jump structure of rough ruled mixtures with conditioning-generated moving boundaries.

# Handoff

New theorem: for
\[
H(t)=\int1_{\{t\ge b(\omega)\}}h_\omega(t-b(\omega))\,d\pi(\omega),
\quad h_\omega\in C_0([0,\infty)),\ 0\le h_\omega\le M,
\]
the canonical density has
\[
H(t_0+)-H(t_0-)=\int_{\{b=t_0\}}h_\omega(0)\,d\pi(\omega).
\]
Thus it lies in \(C_0\) iff every atomic boundary level has zero averaged boundary trace. Atomlessness is sufficient but not necessary. The proof is interval-based via Tonelli and dominated convergence, with no pointwise evaluation of a rough final density.

For the reflection majority sheet translated by an outside quadratic \(Z\), height remains at most \(\pi\sqrt2\); if \(Z\) is a nonconstant polynomial of absolutely continuous coordinates, it is atomless and this subdensity is \(C_0\). A constant \(Z\) has the explicit possible jump \(\Pr(Z=t_0)h_+(0)\).

Math commit: d580c280d279964d5785e245c4561216cf0c41c9.
Full conjecture open at the minority/two-sheet singular boundary.
