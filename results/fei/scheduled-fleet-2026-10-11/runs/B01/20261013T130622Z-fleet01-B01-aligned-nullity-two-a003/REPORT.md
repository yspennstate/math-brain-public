# B01 / A003 — aligned nullity-two fiber payment and hardness boundary

## Outcome

**AUTHOR_PROVED_PENDING_INDEPENDENT_REVIEW.**  The first genuinely nonflat
fiber case admits an exact dimension-independent FEI payment.

Let \(M_0\in\mathbb F_2^{s\times r}\) have full column rank, let
\(z\in\mathbb F_2^2\), and let \(D(u,z)\) be arbitrary.  Then
\[
P(x,u,z)=(-1)^{x^TM_0u+a\cdot x+b\cdot u+c\cdot z+d}D(u,z)
\]
satisfies
\[
\boxed{H(P)\le2I(P),\qquad U(P)\le2I(P).}
\]
The core may change arbitrarily with the shielded address \(u\).  The
constant is independent of dimension, core bias and complexity, affine
phase, and the physical orientation of the full-rank columns.  In matrix
language this covers nullity two when the kernel is spanned by two physical
coordinates.

Full FEI remains **OPEN**.

## Exact movement

The independently accepted B05 theorem covers arbitrary cores at nullity
one for every physical kernel orientation.  This run crosses to four-point
fibers, where unequal/nontrivial fiber spectra first occur, under the
additional hypothesis of a coordinate-aligned kernel.

Writing \(E_u(z)=(-1)^{c\cdot z}D(u,z)\), exact orthogonality gives
\[
H(P)=2r+\mathbb E_uH(E_u),\qquad
I(P)\ge r+\mathbb E_uI(E_u).
\]
Every two-bit Boolean function is affine or quadratic bent, hence
\(H(E_u)\le2I(E_u)\).  This pays the complete conditional fiber entropy,
even when affine and bent fibers are mixed arbitrarily across addresses.

The proof is in `PROOF.md`.

## Why this does not close GU'

The class is not restriction closed: fixing a shield coordinate releases
its paired address coordinate into the kernel.  More importantly, the same
decomposition exposes an exact hardness boundary.  For
\(q_r(x,u)=(-1)^{x\cdot u}\) and arbitrary Boolean \(g\),
\[
\begin{aligned}
H(q_rg)&=2r+H(g),&I(q_rg)&=r+I(g),\\
U(q_rg)&=r+U(g),&G(q_rg)&=2r+G(g).
\end{aligned}
\]
Applying a proposed uniform inequality to \(q_rg^{\otimes N}\), dividing by
\(N\), and sending \(N\to\infty\) removes the shield overhead.  Therefore:

- a uniform arbitrary-nullity fiber FEI theorem is full-FEI-hard;
- a uniform arbitrary-nullity \(U\le KI\) theorem is the universal
  \(U\)-endpoint;
- a uniform arbitrary-nullity GU' inequality is the universal GU'
  inequality with the same constants.

This precisely rejects the idea that arbitrary-nullity parameter removal is
an easier final bridge.  The next target must retain a genuine restriction
on the fiber class or prove the universal asymmetry payment itself.

## Verification

`CHECK_ALIGNED_NULLITY_TWO.py` passed:

- all 16 two-bit Boolean fibers;
- all 32,904 output-complement representatives of canonical cores for
  \(r=0,1,2\), including all 32,768 four-bit cores at \(r=2\);
- 1,312,020 directly reconstructed nonzero Walsh atoms;
- 2,184 direct upper-set endpoint checks;
- 708 noncanonical full-rank matrix/affine-phase samples;
- 8,512 direct tensor-hardness identities through four-bit seeds.

The maximum observed \(H/I\) was exactly 2.  Finite checks support but do
not replace the proof.

## Literature and scope

Potapov's 18 September 2026 manuscript proves FEI for plateaued functions
and constant 2 for partially bent functions.  The present calculation does
not claim novelty over those classes.  Mixed affine/bent fibers generally
produce two Fourier-mass levels, so the proof here is recorded at its exact
fiber-decomposition scope pending a primary-source comparison by A093/A094.

The theorem does not cover a dense two-dimensional kernel, arbitrary
nullity, the GU' aggregate on the restriction closure, or full FEI.  A
linear change of input basis is not permitted: total physical influence and
the upper-set order are basis dependent.

## Next unpaid step

Freeze a restricted fiber class that is preserved when one shield coordinate
is released, or attack the cap-posterior alignment mismatch directly.  Any
claim for arbitrary fibers of unbounded nullity must confront the exact
tensor-hardness embedding above rather than treating the conditional fiber
entropy as an auxiliary term.
