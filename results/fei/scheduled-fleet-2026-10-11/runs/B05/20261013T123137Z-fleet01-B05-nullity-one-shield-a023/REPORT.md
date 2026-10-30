# B05 / A023 — nullity-one shielding of arbitrary coherent cores

## Outcome

**AUTHOR_PROVED_PENDING_INDEPENDENT_REVIEW.**  The accepted full-column-rank
arbitrary-core shield extends across one lost rank.  Let
\[
P(x,y)=(-1)^{x^TMy+a\cdot x+b\cdot y+c}D(y),
\]
where \(D\) is an arbitrary Boolean function and
\(\operatorname{rank}M=m-1=:r\).  For every physical orientation of the
one-dimensional kernel, the squared Fourier law is uniform on exactly
\(2^{2r}\) atoms.  Therefore
\[
H(P)=2r,\qquad U(P)\le2r,
\qquad I_x(P)\ge r/2,\qquad I_y(P)\ge r/2.
\]
Every adaptive or pruned physical restriction tree on the shield variables,
with an arbitrary common disjoint Boolean terminal core \(h\), satisfies
\[
U(Ph)-\sum_\ell w_\ell U(P_\ell h)
\le4I_x(P)
\quad\text{and}\quad
U(Ph)-\sum_\ell w_\ell U(P_\ell h)
\le2I(P).
\]
The constants are independent of dimension, kernel orientation, core bias or
complexity, defect count and overlap, tree depth, reveal order, leaf rarity,
and the disjoint terminal core.

Full FEI remains **OPEN**.

## Primary packet and frozen objective

- Stream: B05; packet: A023 (amortized rarity budget).
- Attempt: `B05-A023-NULLITY-ONE-SHIELD-08`.
- Stable gap: `B05_RARE_REFUNDS`.
- Objective: remove the first rank hypothesis from the independently
  accepted arbitrary-core full-rank shield, without changing physical
  coordinates or paying an exceptional layer once per descendant.

## Precise class extension

The preceding accepted theorem covered arbitrary \(D\) only for full-column-
rank \(M\).  B19 accepted the author constant four and independently derived
the sharper control-only constant two for that full-rank class; that
reviewer strengthening awaits a fresh review.

This run covers every matrix with \(\operatorname{rank}M=m-1\), hence every
two-point Fourier fiber, for arbitrary \(D\).  It is not restricted to a
coordinate-aligned kernel, a point defect, or finitely many defect cylinders.
Together with the prior result it gives a uniform retained-credit theorem
whenever \(\operatorname{rank}M\ge m-1\).

The new constants are:

- control-only payment: \(4I_x\);
- total physical payment: \(2I\).

No parameter dependence remains within this class.  The control-only
constant two seen in the finite scan is recorded only as a numerical
candidate; it is not used in the theorem.

## Proof mechanism

For each admissible \(\alpha\), orthogonality in \(x\) reduces the Fourier
coefficient to the signed sum of \(D\) over one fiber of \(M\).  When
\(\ker M=\langle v\rangle\), the fiber is \(\{y_0,y_0+v\}\), and the sum is
\[
D(y_0)(-1)^{(b+\beta)\cdot y_0}
\bigl[1+\eta(y_0)(-1)^{(b+\beta)\cdot v}\bigr],
\quad \eta(y_0)\in\{-1,1\}.
\]
Exactly one parity class of \(\beta\cdot v\) survives, and every surviving
coefficient has magnitude \(2^{-r}\).  This is an exact physical-basis
calculation; no invertible coordinate change is used.

There are at least \(r\) nonzero physical rows and columns of \(M\).  Each
corresponding \(x\)- or \(y\)-coordinate is pivotal on half of the cube,
regardless of \(D\).  Thus the root reservoir \(U(P)\le2r\) is paid once by
\(4I_x\), or by \(2(I_x+I_y)\).  The complete signed node sum telescopes to
the root minus the weighted leaves.  Nonnegativity of leaf \(U\) closes the
payment, while disjoint tensor additivity cancels terminal \(U(h)\) exactly
once.

The full proof is in `PROOF.md`.

## Verification

`CHECK_NULLITY_ONE_SHIELD.py` uses exact integer Walsh numerators.  It passed:

- all 372 binary matrices of rank \(m-1\) with \(1\le m\le3\) and
  \(m-1\le s\le3\);
- all 86,556 matrix/core instances in that range;
- 1,378,380 exact nonzero Fourier atoms;
- 852 independent direct truth-table/Walsh reconstructions with nontrivial
  affine phases.

Every checked spectrum had exactly \(2^{2r}\) atoms of the asserted common
magnitude.  The largest sampled \(U/I_x\) was 2 and the largest sampled
\(U\) divided by the proved physical-influence lower bound was 1.  These
smaller observed ratios do not replace the written constants.

## Why the next rank loss is different

Nullity one is special because every Boolean function on a two-point fiber
is affine and has one nonzero fiber-Walsh coefficient.  At nullity two, a
four-point restriction of \(D\) can have multiple unequal Walsh masses.
Flatness can fail, so the root entropy has an additional conditional
fiber-spectrum packet not controlled by the present selector-only argument.

The exact next target is the general fiber decomposition
\[
H(P)=2r+\mathbb E_{\alpha}H(\widehat{D|_{y_\alpha+\ker M}}^{,2}),
\]
and a single-use payment of the conditional fiber term by physical data-core
influence plus retained terminal \(U\), uniformly in nullity and without a
physical basis change.  A fixed-nullity calculation with a growing constant
would not close the universal gap.

## Source pins and status separation

- Control revision `2026-10-12.1`, commit
  `40210272c19f43fed84f6a67653f9a04b0e11e28`.
- Assignment: `reports/fei-2026-10-11/assignments/B05.json`.
- Author full-rank source: B05 run
  `20261013T113053Z-fleet01-B05-full-rank-shield-a023`, report blob
  `64497190e19ad5268ad085ce5a76ac3f0e579599`, proof blob
  `1c636e8625bd3facf8425939622a925dbd6cbfa4`.
- Independent acceptance: B19 run
  `20261013T115004Z-fleet01-B19-full-rank-shield-review-a094`, report blob
  `26bb661e6073f446f8ef5edfeb2ed359fb2336ee`.
- Complementary special-core result: B01 run
  `20261013T111215Z-fleet01-B01-positive-codimension-gu-a003`, proof blob
  `4c5cf5492818ba0aba3a23d1bef02b1cba3184dd`; it handles one point defect
  at arbitrary codimension, whereas the present result handles arbitrary
  cores at codimension one.

The current theorem is an author proof awaiting A087/A094 or B19 review.  No
packet completion, independent acceptance, native ingestion or full-FEI
settlement is claimed.
