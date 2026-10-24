SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account04, slot B09, 2026-09-23T10:16:59Z.
attacking: physical cross-bank smoothing with arbitrary dense self-couplings.

# Handoff

## New proved theorem

If two disjoint original-coordinate banks \(S,T\) have equal size \(r>2\) and the actual cross block \(C=A[S,T]\) is invertible, then, after conditioning all outside original coordinates,
\[
Q_z(x,y)=x^TB_zx+2x^TCy+y^TD_zy+a_z^Tx+b_z^Ty+c_z
\]
satisfies
\[
\|p_Q\|_\infty\le {r\over r-2}|\det C|^{-1/r}.
\]
The same-side matrices \(B_z,D_z\), outside spectrum/couplings, and affine terms are arbitrary. Proof: absorb the same-side terms into unit-modulus phases, apply Cauchy--Schwarz and Plancherel to obtain
\[
|\phi_Q(t)|\le \pi^{r/2}|t|^{-r/2}|\det C|^{-1/2},
\]
then integrate \(\min(1,\cdot)\). No rotated independence is used. This branch has a continuous density.

In particular, an actual \(3\times3\) cross minor gives
\[
\|p_Q\|_\infty\le3|\det A[S,T]|^{-1/3}.
\]

## Partner applied

Account01/B09 at commit \`6f8979f8a677663e955befaeb1b4aebb3f0b6a2b\`, blob \`cb6de49bc3f9822d3623e7026e01bfc4ff922eae\`, gives
\[
\|p_Q\|_\infty\le {5\over3}e^{3/5}
[\rho|\lambda|\Delta_\perp]^{-1/5}.
\]
For its literal three-disjoint-group family at \(m=16\), this is \(<3.157\).

## Exact residual

Combine the B07 four-bank star survivor with this theorem and the diffuse-volume branch: if every physical \(3\times3\) cross minor is small and the diffuse-volume hypotheses fail, route the remaining concentrated/low-rank cross geometry into account01/B09's quotient-frame puncture certificate. Large star norm alone does not establish such a route.

## Canonical report

- Repository: \`yspennstate/math-open-problems\`
- Commit: \`c0d3f34e557a374f41b2639994c43af4f950b682\`
- Path: \`proofnet24/QFORM-density/fleet-2026-09-22/account04/B09/20260923T101659Z-account04-B09-dense-self-cross-fourier-r1/REPORT.md\`
- Blob: \`a2292a47ee56cf3d66556e324bd8b234bd2157f1\`

Full QFORM remains open. Continuity is separate and proved only for the stated branch. Status: \`WITHOUT_VERIFIED_BRAIN\`.
