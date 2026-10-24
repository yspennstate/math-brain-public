# Source-bound scope correction to B11's near-tensor inference

Source: claude/B11/STREAM_NOTES.md v2, 2026-10-11 23:3xZ, A053 target: "prove continuity of phi under one-point surgery with explicit remainder, so near-tensors inherit phi <= H/I from R6." Related REPORT.md changed conclusion: "hidden tensor structure is not where block descent can fail."

The exact-product statement CLAUDE-B11-R6@1 remains valid. Independently reconstruct its factor-ratio clause: querying every physical coordinate of one factor leaves +/-the other factor in every branch. The average surviving entropy is the other factor's entropy, so L_A is precisely the queried factor's entropy and I_A its influence. Querying a proper subblock of a factor likewise retains exactly the factor's decrement. Entropy and influence are additive over disjoint products; the root H/I is the influence-weighted factor average. This gives the full R6 inequality when both factor phi values are defined; for a one-coordinate factor interpret the unavailable internal-block minimum as +infinity or use only the always-defined factor-ratio clauses. No substantive repair to those clauses is supplied.

The proposed transition to surgery needs a strict-slack hypothesis or an additive remainder. A053's new self-contained theorem provides both. At equality, F_n=chi_[n] has phi=H/I=0, and its one-point surgery G_n=chi_[n](1-2*1_0) satisfies phi(G_n)>H(G_n)/I(G_n) for EVERY n>=2. This is an actual Boolean family, with all original influences one and defect density 2^-n. Every proper block violates descent at the new own ratio by the exact positive residual 2(n-|A|)2^-n(R_n-R_(n-|A|)), where R_n is the strictly increasing point-defect H/I ratio. Thus the failure cannot be attributed to unhealthy influence denominators in this family. phi and H/I both tend to zero, so no fixed positive universal descent bound or full FEI is refuted.

The surviving version is:

    phi(surgery)<=phi(seed)+eps_phi;
    if R(seed)-phi(seed)>eps_phi+eps_R, then phi(surgery)<R(surgery).

The eps values explicitly retain the influence denominator and block-child error. A fixed entropy-positive tensor core with a fresh sign has strict slack and eventually satisfies the exact inequality. A parity core does not. The lead's exact R6 claim should remain intact; only its unversioned qualitative inference to all near-tensor surgeries is narrowed. No shared source, index, or another agent's file was edited. Supervisor and B11 lead should consume this saved source-bound correction, with A090/A094 independently checking the new proof.

The family also distinguishes averaged and individual criticality tests. Every averaged proper-block test at C=H(G_n)/I(G_n) passes strictly, while for n>=3 the two-bit edited descendant has ratio 2>H(G_n)/I(G_n). A test that certifies nonpositive average terminal deficits cannot be promoted to nonpositive deficit of every terminal child without a separate proof.
