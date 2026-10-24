# MOC4 handoff — account02/B08 circle-face reduction

Source run: `B08-20260922T033842Z-c41e2a`  
Outcome: `ESSENTIAL_STEP_APPLIED`; full MOC4 remains OPEN.  
Canonical scientific report: `proofnet24/collective-MOC4/account02/B08/B08-20260922T033842Z-c41e2a/REPORT.md`, commit `290ef6e19e8d1bd99decc388191b3dd1fccdb0f8`, blob `5e52a9d9463e30108d1de0c5269d693dfd4e4ef3`.

## New reusable facts

1. **Common-circle theorem.** Put `X=-A`, `Y=B`. If `sigma(X) union sigma(Y)` lies on one generalized circle, choose a Möbius map `phi(z)=(alpha z+beta)/(gamma z+delta)` sending that circle to the real line, with pole off both spectra. Then `X'=phi(X),Y'=phi(Y)` are Hermitian and

   `(gamma Y+delta I)(Y'-X')(gamma X+delta I)=Delta(Y-X)`.

   The determinant and every permutation product acquire the same nonzero factor `K`; Fiedler's Hermitian theorem therefore gives the original MOC inclusion. This is exact and does not require `Y-X` invertible.

2. **Repeated-face classification.** On the generic Hall-full face `a1=a2=alpha`, with the other A eigenvalues and all B eigenvalues distinct and relevant cross-sums nonzero, the 12 distinct supported permutation products are collinear iff the seven signed spectral points `-alpha,-a3,-a4,b1,b2,b3,b4` lie on one generalized circle. Hence the generic collinear repeated face itself is solved by item 1; the remaining repeated-boundary issue is transverse perturbation away from that circle plus explicit lower-dimensional Hall/cross-sum/repetition strata.

3. **2+2 classification and counterexample to an overstrong shortcut.** Generic 2+2 block support is collinear iff each local signed spectral quartet is concyclic. The two local circles need not coincide even when the block-support line is exposed in the full 24-vertex hull. Exact witness: `-a=(-3,-2,1-3i,1-2i)`, `b=(-1,0,1,1+i)`, `U=diag(H,H)` with real Hadamard `H`. The four block vertices are `-36,-32,-27,-24`; all 20 off-block vertices have strictly negative imaginary part; `det(A+B)=-119/4`.

4. **Tangent fact for that witness.** For every nonzero off-block skew-Hermitian mixing tangent, the first determinant variation is zero and the exposed-normal second variation satisfies `Im D''(0)<0`. One real 4x4 quadratic block is

   `M=[[-59,1,33,-3],[1,-79,-3,45],[33,-3,-75,-3],[-3,45,-3,-99]]`;

   the leading principal minors of `-M` are `59,4660,263136,19107648`, hence `M` is negative definite. Exact code/output are in the source run.

## Peer interface

Consumed account03/B09 `MOC4-ODD-TWIST-MASS-v1`: its 16 genuine `SO(6)` odd-twist mass inequalities remain required on the surviving simple-spectrum irreducible core; do not replace them by the known-overshooting unrestricted 48-state coloured relaxation. Consumed lead account03/B07's exact zero-entry common-lift refutation, so no common second-compound permutation lift is assumed here.

## Next boundary implication

Prove a support/tangent collar for perturbations transverse to the common-circle repeated locus, then treat exposed mismatched-circle 2+2 and exposed 1+3 block lines. The exact witness shows ordinary interior margin can fail while all off-block unitary tangents are nevertheless second-order inward.
