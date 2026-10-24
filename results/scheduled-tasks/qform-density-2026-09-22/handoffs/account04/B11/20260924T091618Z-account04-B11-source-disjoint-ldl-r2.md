SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account04, slot B11, 2026-09-24T09:16:18Z.
attacking: the source-disjoint third-curvature branch of the nonzero-pivot LDL/two-sheet collar.

# B11 handoff: source-disjoint LDL third curvature

Source control: math-research-brain main read with OWNER CONTROL revision 2026-09-22.15; canonical login committed at 73a958794014fdd97397bf324d6c2fde3490a8d4.

Mathematical sources:
- account01/B11 QFORM-LDL-FULL-TWOJACOBIAN-NONZERO-v1 at math-open-problems@339d40cb2285b8d51cf07423514354bdd702833f.
- account01/B05 QFORM-RANK2-INDEPENDENT-SQUARE-BRIDGE-v1 at math-open-problems@4971375a7b03b979ca3bb1c6b31e4af71f7a1276.

New theorem:
If an exact-rank-three LDL form splits in original-coordinate source as
\[
Q=R(Z,Y)+d(W+\theta)^2,
\]
where \(R\) is the rank-two block, \(W\) is normalized and carried by a disjoint source bank, and the three nonzero eigenvalues have modulus at least \(s\), then
\[
p_Q\in C_0,\qquad \|p_Q\|_\infty\le128\sqrt2/s.
\]
If \(W\) has density cap one, the constant improves to \(128/s\).

The account01/B11 two-Jacobian is applied at the actual inequalities
\[
\Pr(J_2F\le\tau)\le\min(1,\pi\tau^2/(2s^2)),\qquad
E[J_2F^{-1}]\le\sqrt{2\pi}/s.
\]
These are not used as an arbitrary-joint coarea shortcut; the density conclusion uses genuine disjoint-bank independence.

Concrete two-sign target family:
\[
Q_{\varepsilon,\sigma}=\sigma\varepsilon H^2+2\sqrt{1+\varepsilon}HV+W^2
\]
has spectrum \(\{1+\varepsilon,-1,1\}\) or \(\{1,-(1+\varepsilon),1\}\), and satisfies \(p_Q\in C_0\), \(\|p_Q\|_\infty\le128\) uniformly through \(\varepsilon\downarrow0\).

Full report: https://github.com/yspennstate/math-open-problems/blob/494e4a18bff08cc3fbc9ba668ba14a3983e51da6/proofnet24/QFORM-density/fleet-2026-09-22/account04/B11/20260924T091618Z-account04-B11-source-disjoint-ldl-r2/REPORT.md

Remaining first gap: shared-source third curvature. The independent-square convolution disappears there, while the two-Jacobian budget cannot be promoted after forgetting product provenance. Arbitrary additional spectrum and full-target continuity also remain open.

Full QFORM remains OPEN.
