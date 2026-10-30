# B05 / A023 — aligned kernel width four and the exact width barrier

## Outcome

**AUTHOR_PROVED_PENDING_INDEPENDENT_REVIEW.**  The arbitrary-core bilinear
shield now has a complete retained-\(U\) payment for every coordinate-aligned
kernel of width at most four, with exact constants.  More generally, width
\(t\) has constant \(K_t=\max\{2,C_t\}\), where \(C_t\) is the exact
ordinary \(t\)-bit FEI constant.

For

\[
P(x,u,z)=(-1)^{x^TM_0u+\text{affine}}D(u,z),
\]

where \(M_0\) has full column rank and the physical \(z\)-block has size
\(t\le4\), every finite adaptive/pruned tree on the shield variables and
every arbitrary common disjoint terminal core \(h\) satisfy

\[
\boxed{U(Ph)-\sum_\ell w_\ell U(P_\ell h)\le K_t I(P).}
\]

The exact constants are

\[
K_t=2\ (t\le2),\quad
K_3=\frac73+\frac34\log_2\frac{16}{9},\quad
K_4=\frac{45}{16}+\frac{49}{32}\log_2\frac{64}{49}.
\]

Numerically, \(K_3=2.955889582251598\ldots\) and
\(K_4=3.402475551198587\ldots\).  The constants have no dependence on
shield rank, core bias, defect count, address count, overlap, tree depth,
reveal order, or dyadic activation probability.

Full FEI remains **OPEN**.

## Primary packet and frozen objective

- Stream: B05; packet: A023 (amortized rarity budget).
- Attempt: `B05-A023-ALIGNED-WIDTH-FOUR-09`.
- Stable gap: `B05_RARE_REFUNDS`.
- Objective: extend the nullity-one complete-tree payment to genuinely
  nonflat changing fibers, calculate the exact finite-width constant, and
  determine whether removing width is an auxiliary lemma or the original
  conjecture.

## Mathematical delta

The preceding B05 theorem covered arbitrary one-dimensional kernels in every
physical orientation; its flat two-point fibers give retained loss at most
\(2I\).  B01 subsequently derived the exact coordinate-aligned fiber
decomposition and covered width two with constant two.

This run adds two new points.

1. It proves the full general pattern
   \[
   H(P)=2r+\mathbb E_uH(D_u),\qquad
   I(P)\ge r+\mathbb E_uI(D_u),
   \]
   and hence a signed complete-tree payment with the exact finite-width FEI
   constant.
2. It rigorously certifies the next nonflat widths three and four.  The first
   growing constant appears at width three, and one-point defects are exact
   maximizers through width four.

This is a proper unbounded, restriction-compatible class: shield rank and
tree size are arbitrary and the Boolean fibers may change independently for
all \(2^r\) values of \(u\).  It is not a finite numerical survival claim;
the finite computation identifies the exact fiber constant, while the proof
handles arbitrary rank and arbitrary adaptive trees.

## Proof mechanism

Orthogonality in the shield variable \(x\) leaves a unique \(u\) for each
admissible Fourier frequency.  The squared spectrum is therefore the exact
mixture obtained by choosing \((u,\gamma)\) uniformly and then sampling the
Fourier law of the Boolean fiber \(D_u\).  This gives the entropy identity.

The full-rank bilinear block forces at least \(r/2\) influence in physical
\(x\)-coordinates and exactly \(r/2\) in the \(u\)-coordinates.  Physical
\(z\)-influence is the average fiber influence.  Applying the exact
\(t\)-bit FEI constant to each fiber yields \(H(P),U(P)\le K_tI(P)\).

The complete signed node sum telescopes to root \(U\) minus nonnegative leaf
\(U\).  A disjoint terminal core cancels exactly by tensor additivity.  No
nodewise positivity is required, so coherent descendants do not spend the
same root packet repeatedly.

The complete proof is in `PROOF.md`.

## Exact verification

`CHECK_ALIGNED_WIDTH.py` uses exact integer Walsh transforms and exact
`Fraction` influence arithmetic.  Logarithms are enclosed by a 48-term
positive atanh series after binary range reduction; the remainder is bounded
explicitly, and interval division uses the appropriate denominator corners.

It exhausts every truth table modulo global output sign through four bits:

- dimension 1: 2 representatives, 1 nonconstant profile;
- dimension 2: 8 representatives, 3 nonconstant profiles;
- dimension 3: 128 representatives, 10 nonconstant profiles;
- dimension 4: 32,768 representatives, 47 nonconstant profiles.

The certified width-four interval has width below \(1.04\times10^{-48}\).
The runner-up upper endpoint is the exact width-three constant, leaving a
rigorous gap greater than \(0.4465\).  The checker also reconstructs 65,810
aligned shield instances directly from truth tables and verifies both the
spectral product law and physical influence lower bound.

## Exact universal boundary

The dependence on \(C_t\) cannot be removed by refining only this fiberwise
argument.  Fix the nontrivial one-pair shield \(q(x,u)=(-1)^{xu}\).  A
width-uniform bound applied to \(qg^{\otimes N}\) gives

\[
2+NH(g)\le C(1+NI(g)).
\]

Letting \(N\to\infty\) proves \(H(g)\le CI(g)\) for every Boolean \(g\).
Thus the all-width aligned-shield endpoint is full-FEI-hard even with shield
rank one.  The next unpaid step is exactly a dimension-independent fiber
payment; another fixed-width case cannot close it.

## Scope and mandatory falsifiers

- The theorem requires the kernel to be spanned by physical coordinates.
  A dense kernel orientation can mix the fiber coordinates, and influence is
  not invariant under a general linear basis change.  Width one was handled
  in arbitrary orientation by the predecessor theorem; width at least two in
  arbitrary orientation remains open.
- All rare leaf probabilities generated by uniform physical restrictions are
  included.  An external continuously biased restriction model is not
  claimed.
- Point defects are not merely tests here: they attain the exact constants in
  widths two through four.
- Near tensors are the sharp universal obstruction: the rank-one shield of
  \(g^{\otimes N}\) proves the hardness statement.
- Shared-variable interference is present through arbitrary \(D(u,z)\); the
  coordinate alignment is the surviving structural hypothesis.

## Sources and status separation

- Control revision `2026-10-12.1`, commit
  `40210272c19f43fed84f6a67653f9a04b0e11e28`.
- B05 assignment blob:
  `05447e6d999437bb82a266b427bd76a4b37266b6`.
- B05 nullity-one predecessor: run
  `20261013T123137Z-fleet01-B05-nullity-one-shield-a023`, proof blob
  `d3b79b8a3e4c485b9f693ec22be4e9210b637738`; later B19 review accepted that
  stated theorem.
- B01 aligned-nullity-two input: report blob
  `68fb2ff39906172775587475ebc4915dfd06e08f`, proof blob
  `08f2c10f87123f2bf2e9d5c243910203de52eab8`; its claim is an author proof
  pending independent review and was rederived here before use.

The current width-three/four theorem is an author proof awaiting A087/A094 or
B19 review.  No packet completion, native ingestion, full-FEI proof, or
counterexample is claimed.

## Next action

Freeze the remaining orientation problem at width two: for a dense
two-dimensional kernel, express the induced two-bit fiber influences in
physical coordinates and prove a dimension-independent comparison to the
root physical influence, or produce a Boolean counterfamily showing that an
additional retained interaction credit is necessary.  This changes the
mechanism from fixed-width enumeration to physical-basis stability.

