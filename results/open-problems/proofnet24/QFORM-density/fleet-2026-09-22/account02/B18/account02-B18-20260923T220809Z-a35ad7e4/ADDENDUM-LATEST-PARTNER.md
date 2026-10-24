# Addendum — latest account03/B18 auto12 compatibility check

After REPORT.md was written, a fresher designated-partner handoff appeared: account03/B18 `QFORM-FRESH-WEDGE-ZEROPIVOT-v1`, canonical mathematics `math-open-problems@2520c97fceee8f0451dc6df967c47b2632ff220c`.

That theorem is source-valid and stronger than the previous private-cross estimate on its exact scope. It assumes pairwise disjoint original source sets `J,{i},K`, with

`S=a·X_J`, `W=X_i+ell·X_K`, `B=beta·X_K`,

and a nonsingular 3x3 active matrix whose S-S entry is zero. Deterministic whitening plus Livshyts--Paouris--Pivovarov gives

`||p_(W,B)||inf <= 2/[||beta|| sqrt(1+||P_(beta^perp)ell||^2)]`,

and the account04/B18 zero-pivot receiver yields

`||p_Q||inf <= 12 |pdet A|^(-1/3) <= 12/s`

for exact rank three with all three nonzero eigenvalue moduli at least `s`; continuity holds. No projected-coordinate independence is asserted.

This theorem does **not** subsume the stress family in REPORT.md,

`Q_{m,eta}=2 X0 G+2 eta G V+(b0 C+rho B)^2`,

because the square direction `b0 C+rho B` has a nonzero component `b0 C` on the same original J-bank that generates the scalar direction `G`. Therefore the scalar bank is not source-disjoint from the full square statistic required as `B` in the fresh-wedge representation. Conditioning out `C` would return to exactly the conditional-private-bank interface disproved in REPORT.md and would not satisfy the partner theorem's genuine scalar-versus-pair independence.

Accordingly the report's obstruction remains live, but its scope is sharpened: the near-parallel collar is already paid whenever a fresh-coordinate wedge plus an independent scalar bank can be exposed. The surviving obligation is the **fully source-entangled near-parallel collar**, in which the square direction shares original-source support with the scalar bank and no equivalent source-disjoint fresh-wedge factorization has been established.

No claim is made that the displayed family admits no other algebraic representation whatsoever; the proved statement is only that the natural null-hub decomposition used in REPORT.md fails the exact source-disjoint hypothesis of auto12. A future compiler may still reroute it by a different product-preserving representation.

Full QFORM remains OPEN.
