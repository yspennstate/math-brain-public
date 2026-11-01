# B01 / A003 — arbitrary-orientation nullity-two payment

## Outcome

**AUTHOR_PROVED_PENDING_INDEPENDENT_REVIEW.**  The coordinate-alignment
hypothesis in the preceding nullity-two theorem is unnecessary.

For every binary matrix \(M\in\mathbb F_2^{s\times m}\) of rank \(m-2\),
every affine phase, and every Boolean \(D:\mathbb F_2^m\to\{-1,1\}\),
\[
 P(x,y)=(-1)^{x^TMy+a\cdot x+b\cdot y+c}D(y)
\]
satisfies
\[
 \boxed{H(P)\le2I(P),\qquad U(P)\le2I(P).}
\]
The proof retains the original physical \(y\)-basis.  It therefore covers
dense two-dimensional kernels and is strictly broader than the accepted
coordinate-aligned case.  Full FEI remains **OPEN**.

## New physical-basis mechanism

Let \(K=\ker M\), and let \(k\) be the number of physical unit vectors in
\(K\), equivalently the number of zero columns of \(M\).  Since
\(\dim K=2\), \(k\in\{0,1,2\}\).  Exact orthogonality over the shield gives
\[
 H(P)=2r+\mathbb E_\alpha H(E_\alpha),\qquad r=m-2,
\]
where \(E_\alpha\) is the Boolean function on the two-dimensional kernel
fiber above the coset \(\alpha\).

Every nonzero physical row and every nonzero physical column of \(M\) pays
exactly \(1/2\) influence.  A zero column is an actual physical direction
inside every fiber.  The sharp two-bit directional lemma is
\[
 H(E)\le2-k+2\sum_{j:Me_j=0}\operatorname{Inf}_{e_j}(E).
\]
It follows because a two-bit Boolean function is either affine (entropy
zero) or bent (entropy two and influence \(1/2\) in every nonzero
direction).  Combining the forced influence with the directional payment
gives
\[
 H(P)\le2r+2-k+2J\le2I(P).
\]
The full derivation is in `PROOF.md`.

## Exact boundary and GU calibration

The same coefficient-two directional lemma fails immediately at nullity
three.  The genuine shield
\[
 M=(1,1,0,0),\qquad
 D(y)=-1\Longleftrightarrow y_1=y_3=y_4=0
\]
has one three-bit point defect on each kernel coset and obeys
\[
 I(P)=2,\quad
 H(P)={15\over4}+{9\over16}\log_2{16\over9},\quad
 H(P)-2I(P)\approx0.2169171867>0.
\]
This is not an FEI counterexample; it certifies the exact failure of the
constant-two extension at the next nullity.

The root endpoint also does not automatically imply GU with the same
constant.  An exact six-bit member of the nullity-two class has
\[
 H=6,\quad U=3,\quad I=3,\quad G={277\over32},\quad
 {G\over I}={277\over96}\approx2.8854167.
\]
This quadratic calibration is consistent with the earlier proved quadratic
bound \(G\le3I\), but it refutes the tempting transfer \(G\le2I\).  The
new frozen proposition
\[
 G(P)\le3I(P)
\]
for arbitrary rank-\((m-2)\) shields remains **OPEN**.  Controlling its
upper-set asymmetry mismatch, not the fiber entropy, is now the unpaid term.

## Case extension record

| Field | Record |
|---|---|
| Starting class | Rank-\((m-2)\) shields whose kernel is spanned by two physical coordinates |
| New class | Every rank-\((m-2)\) physical shield, including dense kernels and kernels with exactly one physical unit direction |
| Core | Arbitrary Boolean \(D(y)\); fibers may change independently across all cosets |
| Previous bound | \(H,U\le2I\) under coordinate alignment |
| New bound | \(H,U\le2I\), independent of dimension, bias and kernel orientation |
| GU status | \(G\le2I\) exactly falsified; \(G\le3I\) frozen and open on the enlarged class |
| Next parameter | Nullity three; coefficient two already fails by the certified point-defect shield |
| Universal gap | No \(a<\infty,b<1\) control of aggregate upper-set asymmetry is proved |

The class is not restriction closed: fixing shield coordinates can lower
rank and raise nullity.  Thus this is a direct restricted FEI/U theorem,
not a GU induction and not full FEI.

## Verification

`CHECK_ARBITRARY_NULLITY_TWO.py` passed:

- all 48 directional-lemma cases (16 two-bit functions times
  \(k=0,1,2\));
- 7,624 direct nullity-two truth-table/matrix cases, including every
  rank-one orientation on three physical \(y\)-bits and every rank-two
  \(2\times4\) orientation with deterministic structured/random cores;
- 444,448 direct truth-table atoms;
- maximum observed \(H/I=2\);
- maximum sampled \(G/I=277/96\);
- exact dyadic reconstruction of \(H=6,U=3,I=3,G=277/32\) for the GU
  calibration;
- direct Walsh reconstruction of the nullity-three witness, including the
  mass histogram \(4\times(9/64)+28\times(1/64)\).

Finite checks support but do not replace the written proof.

## Sources and scope

The live owner control is revision `2026-10-12.1` at source commit
`40210272c19f43fed84f6a67653f9a04b0e11e28`; its GU amendment and B01 row
were reread this run.  The current public-threshold mathematical baseline is
commit `d8eb4ceb7010b2bff0a2b7c403eac3e0e65c1de2`.  The preceding aligned
nullity-two result and its later independent scope review were used only at
their exact stated scope.

No literature novelty claim is made.  The contribution is the explicit
physical-basis extension, its sharp nullity-three boundary for coefficient
two, and the separation between the FEI/U payment and the still-open GU
asymmetry payment.

## Next unpaid step

Use the exact \(B_i-\Gamma_i+K_i\) identity on the frozen class claim
\(G\le3I\).  Exploit the rowspace-uniform spectral repetitions to pair the
aggregate \(K_i\) mismatch with the forced \(1/2\)-influences, while keeping
the physical upper-set order.  The six-bit \(277/96\) witness is a mandatory
calibration, and the nullity-three point defect prevents silently extending
the coefficient-two fiber ledger.
