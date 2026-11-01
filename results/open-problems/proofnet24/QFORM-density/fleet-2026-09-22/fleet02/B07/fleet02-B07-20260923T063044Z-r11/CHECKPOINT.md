SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account 02, slot B07, 2026-09-23T06:30:44Z.
attacking: the partner r26 edge-plus-E2 survivor; lift aggregate second-compound mass through a physical scalar edge without selecting one 2x2 minor, and isolate the exact cancellation geometry.

# Early substantive checkpoint

Programme: `QFORM-DENSITY-3EIG-20260922`.
Status: supporting calculation only; full QFORM remains OPEN.
Execution: `WITHOUT_VERIFIED_BRAIN`.

Incoming partner: fleet03/B07 r26, brain handoff `20260923T060629Z-fleet03-B07-qform-r26.md`, canonical math-open-problems commit `86ff1278a9b52d8a2736c340b7f54893c6b8c267`. In its E2 branch the residual physical cross block N has `E2(N)>=3||N||_F^4/16`, nested inside an edge-star-core packet `|e|||s||||N||_F > theta F^3/(36sqrt(2))`.

For an actual physical augmented cross block

    B = [ b  u^T ]
        [ v   N  ]

let H be the matrix of all 3x3 minors containing the anchor row and anchor column. The exterior identity already proved in this slot's earlier O1 work applies verbatim as a rectangular physical identity:

    H = b C_2(N) - K,    K = W_v N iota_u.

Hence

    |b| sqrt(E2(N)) <= ||H||_HS + ||K||_HS,

so either `||H||_HS >= |b|sqrt(E2(N))/2`, or `||K||_HS >= |b|sqrt(E2(N))/2`.

New calculation: color the residual physical row and column coordinates independently into two colors. On a coloring, restrict K to row pairs and column pairs that are rainbow. Its expected squared norm is one quarter of `||K||_HS^2`, hence one coloring has rainbow norm at least `||K||_HS/2`. Expanding a rainbow K-entry gives four product tensors. Triangle inequality therefore forces one of the four literal disjoint-bank products

    ||v_Ra||_2 ||u_Cb||_2 ||N[R_(1-a),C_(1-b)]||_F

(at the matching orientation dictated by the expansion) to be at least `||K||_HS/8`.

Thus the partner E2 branch has a dimension-free aggregate alternative before reciprocal localization:

(A) an anchored third-volume packet of HS norm at least `|b|sqrt(E2(N))/2`, or
(B) three mutually disjoint physical coefficient banks with product at least `|b|sqrt(E2(N))/16`.

On the r26 parent scale, each of `|b|, ||s||, G=||N||_F` exceeds `theta F/(36sqrt(2))`, so

    |b|sqrt(E2(N)) > sqrt(6) theta^3 F^3 / 746496.

Therefore (A) has norm > `sqrt(6) theta^3 F^3 / 1492992`, while (B) has product > `sqrt(6) theta^3 F^3 / 11943936`.

Exact cancellation is genuinely possible and must not be discarded. For even m let U have the two flat orthonormal columns `q0_j=1/sqrt(m)`, `q1_j=(-1)^j/sqrt(m)`, put P=UU^T, and form the target matrix

    A_m = [0 P; P 0].

Its nonzero spectrum is `{1,1,-1,-1}`. Every entry of P is 0 or 2/m, so for m>=24 this lies in N3(1/128): all physical diagonals vanish and every 2x2 principal determinant has magnitude at most 4/m^2<1/128. At a same-parity anchor, `b=2/m`; deleting its row and column gives N with singular values `1` and `1-2/m`, so `E2(N)=(1-2/m)^2`. Yet rank(P)=2, hence every anchored 3x3 minor vanishes: `H=0` exactly. The full quantity `b C2(N)` is canceled by K.

This is not a QFORM counterexample. The required e5 source theorem F applies directly to A_m: its rank-four eigenspace has physical leverage `2/m<=1/2`, all four nonzero eigenvalues have modulus one, and so `|phi(t)| <=16 pi^2 |t|^-2`; integrating `min(1,16 pi^2/t^2)` gives `||p_Q||_infinity<=8` for every admissible product law.

Next: write the full proof of the coloring lemma, verify constants/construction exactly, and integrate the alternative with the partner's anchored-volume recursion without claiming the remaining arbitrary-curvature three-link packet is paid.
