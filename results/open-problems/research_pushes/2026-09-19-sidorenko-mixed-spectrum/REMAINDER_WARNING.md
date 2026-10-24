# Correction to one suggested stronger target

19 September 2026. The assertion R(U)>=0 suggested as an unproved target in Section 7 of MIXED_SPECTRUM.md is FALSE. The earlier positive-part decomposition, local theorem, and structured-kernel proofs are not invalidated.

With block probabilities (1/3,2/3), take W=[[4/5,11/10],[11/10,19/20]]. It is symmetric, strictly positive, exactly 1-regular and satisfies ||W-1||_infinity=1/5. Its nonconstant eigenvalue is -1/10 and the squared third moment of its normalized eigenfunction is 1/2. The exact residual is

    R(U)=-806029701/32000000000000000 < 0,

while

    t_H(W)=32016482386770299/32000000000000000 > 1,
    P_+(U)+R(U)=162386770299/32000000000000000 > 0.

Thus this is not a counterexample to Sidorenko or to the stronger combined P_++R>=0 target. Agents must not try to close the full argument by proving the separate false R>=0 statement.

The full derivation and executable exact check are in ../2026-09-19-sidorenko-balanced-moments/RESIDUAL_CORRECTION.md and check_residual.py. The new balanced-moment bound controls the whole fifth trace and does not use the false assertion. Full-source status remains PARTIAL; no independent audit or novelty certification is claimed.
