SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet02, slot B20, 2026-09-23T20:58:58Z.
attacking: the newest fleet03/B20 transported-edge survivor; determine whether its large alternating transported edge is a genuine third smoothing resource or only a bank-mixing shear, and isolate the product-safe replacement.

# Early substantive calculation — transported-edge shear normal form

Newest completed designated partner consumed: fleet03/B20 `20260923T203220Z-fleet03-B20-QFORM-auto11b`, canonical math `yspennstate/math-open-problems@043b1c2c8a21e910e4d425dd78f2d9f6c947be7c`.

Its normalized 2+2+2 main cycle is

`S_D=[[0,D,I],[D^T,0,I],[I,I,0]]`,

with `D=B1^{-1} C0 B2^{-T}=T/(det(B1)det(B2))`, where `T=adj(B1)C0adj(B2)^T`. Write

`H=(D+D^T)/2`, `K=(D-D^T)/2`.

For the quadratic form

`q_D(x,y,z)=2 x^T D y+2x^Tz+2y^Tz`,

set

`u=x+y`, `v=x-y`, `zeta=z+(1/4)Hu-(1/2)Kv`.

Then, exactly,

`q_D=2u^T zeta-(1/2)v^T H v`.

Thus the skew part K disappears completely under an invertible deterministic shear; only the symmetric transported edge H creates rank beyond the two hyperbolic pairs. This is coefficient geometry only: `zeta` mixes the three original banks and MUST NOT be treated as independent of `(u,v)`.

In particular, for `D=omega J`, `J=[[0,1],[-1,0]]`, one has `H=0`, and the six-dimensional main cycle has rank exactly four for every nonzero `omega`, even though the partner's symplectic-skew scalar can be arbitrarily large. Its four nonzero eigenvalues are

`+sqrt(omega^2+2), +sqrt(omega^2+2), -sqrt(omega^2+2), -sqrt(omega^2+2)`.

Hence a large transported skew is a shear-size certificate, not by itself a fifth-volume / extra-rank certificate.

Target-valid diffuse realization: take three disjoint physical banks and orthonormal 2-frames U1,U2,V, and set all self blocks to zero while

`A[D1,D2]=U1(omega J)U2^T`,
`A[D1,K]=U1 V^T`,
`A[D2,K]=U2 V^T`,

with symmetric transposes. Then A has the spectrum above plus zeros. If each frame is the q-fold repeated coordinate basis scaled by `q^{-1/2}`, every physical row leverage is `1/q` and every physical off-diagonal entry has magnitude at most `max(1,|omega|)/q`. Thus every physical 2x2 principal determinant has magnitude at most `max(1,omega^2)/q^2`; for `q>8 max(1,|omega|)` the matrix lies in `N3(1/64)` while still having four eigenvalues of modulus at least sqrt(2).

Since the full matrix has rank four, every literal physical cross block has rank at most four, so the pinned unrestricted fifth-volume receiver has `e5=0` on every cut. This gives an exact obstruction to paying the symplectic chamber by D5 merely from `|omega|>0`.

This does not disprove QFORM. In the zero-self-block realization, split only K into two physical halves with each restricted frame Gram `(1/2)I`, take `I=D1 union K_1`, `J=D2 union K_2`, and the exact physical cross block has a 4x4 compression `[[omega J, 2^{-1/2}I],[2^{-1/2}I,0]]` with determinant `1/4` (up to the normalization convention), hence fixed rank four. A full calculation and a product-safe exact-rank crossing payment will be in REPORT.md. The live survivor differs precisely because arbitrary K-same-bank curvature can Schur-cancel this mixed cut; small coefficient tails cannot be deleted on rough laws.

Status: new exact structural obstruction/reduction; full QFORM still open.
