# B19 / A094 independent review — B01 bent nullity-two GU witness

## Verdict

The exact finite claim `B01_A003_BENT_NULLITY_TWO_GU_LOWER_v1` is
**ACCEPTED AT ITS DECLARED FINITE SCOPE**.

For the displayed ten-variable Boolean shield, an independent direct Walsh
reconstruction proves

\[
 H=10,\qquad U=I=5,\qquad 2.974<G/I<2.975.
\]

Hence every inequality `G<=aI+bU` valid on a class containing this function
must satisfy `a+b>2.974`. This improves the earlier exact calibration
`277/96=2.885416...`.

The broader extracted pattern needs a scope correction: the statement that
rank `m-2` plus nonzero rows and columns makes the parent bent and gives
`U=I=m-1` is false when the shield has more than `m-2` physical `x`
variables. A duplicated-row five-variable example has all rows and columns
nonzero and bent two-bit fiber cores, but is plateaued rather than bent and
has

\[
 H=4,\qquad U=2,qquad I=5/2.
\]

The corrected all-parameter statement requires `s=rank(M)=m-2` (equivalently,
exactly `m-2` independent shield variables). Under that hypothesis, bentness
of every two-dimensional kernel fiber does imply that the full parent is bent,
and then `H=2m-2` and `U=I=m-1`. Because this review supplied the correction,
the corrected general statement needs fresh A085/A090 review if registered as
a separate theorem.

The phrase “nearly sharp constant 3” must remain interpretive: `G<=3I` is
still open for arbitrary nullity-two shields. What is rigorously established
is only the lower obstruction `G/I>2.974`, i.e. proximity to the **proposed**
constant 3.

Full FEI remains **OPEN**.

## Target and sources

Primary packet: `A094` (proof-chain challenger). Target packet: B01/A003,
claim `B01_A003_BENT_NULLITY_TWO_GU_LOWER_v1`.

Reviewed original package:

* repository `yspennstate/math-open-problems`;
* finalized commit `addf01f7987afb3d29f6284565843eb5c0b862b2`;
* package commit `92b9dd65273085c6cfa2c3ba69fa624b248e2959`;
* path `reports/fei-2026-10-11/runs/B01/20261013T162335Z-fleet01-B01-bent-nullity-two-gu-a003/`.

The predecessor nullity-two theorem was read from commit
`f108d34dd304d03aae2d28c5160c4a32a45758d3`, package commit
`99c60c7a5554f2a435016ad100ccb5d2d10a6bd0`.

## Independent reconstruction

The review checker was written independently and does not import the author's
checker. It uses a direct `O(4^n)` character sum, not FWHT, for the parent and
all restrictions.

For

\[
 M=(31,52,7,34),\qquad
 D_{+}=13594860716390676976,
\]

it verifies:

1. binary rank `rank(M)=4=6-2` and all physical rows/columns nonzero;
2. all 1024 parent Walsh sums have magnitude 32;
3. all ten coordinate influences equal `1/2` by direct edge counting;
4. each of the twenty restrictions has exactly 256 nonzero Walsh sums, all
   of magnitude 32;
5. the independently reconstructed upper-set-count histogram matches the
   source histogram exactly;
6. exact rational atanh-tail intervals give `2.974<G/I<2.975`;
7. the Boolean exponent has algebraic degree 5, so this witness is genuinely
   nonquadratic and is not contained in the earlier quadratic-phase theorem.

The exact formula checked is

\[
G=50-\frac1{512}\sum_cN_c\log_2c.
\]

No floating-point quantity controls an assertion.

## Corrected bent-fiber derivation

Let `M` be an `(m-2) x m` full-row-rank matrix and `K=ker M`, so
`dim K=2`. If the restriction of the signed core to every affine coset of
`K` is bent, its unnormalized two-bit Walsh sums all have magnitude 2.
Summing first in `x`, each parent coefficient therefore has magnitude

\[
 2^{-m}\cdot2=2^{-(m-1)}=2^{-(2m-2)/2}.
\]

Thus the parent on `2m-2` variables is bent. Its spectral law is uniform on
the full cube, hence

\[
H=2m-2,\qquad U=\mathbb E_S(2m-2-|S|)=m-1.
\]

Every nonzero derivative of a bent function is balanced, so each physical
coordinate has influence `1/2` and `I=m-1`. No separate nonzero-column
hypothesis is needed under this corrected square-in-the-row-rank setup.

If instead `s>m-2`, the Fourier support occupies only the rank-compatible
`x` frequencies. The parent is generally plateaued rather than bent, and
dependent nonzero physical rows each add influence. The scope checker takes
`m=3`, `s=2`, duplicate rows `(111,111)`, and core phase `y1*y2`. It verifies
the displayed `H,U,I` values and refutes the overbroad wording exactly.

## Literature scope

Potapov's 18 September 2026 preprint proves FEI for Boolean plateaued
functions and gives sharp FEI constants for plateaued and partially bent
classes. That concerns `H/I`; it does not state this upper-set restriction
charge `G`, its child-support histogram, or the lower constraint on `a+b`.
The present finite certificate therefore does not conflict with that result,
but no novelty/priority claim is made for the GU obstruction.

## Mathematical delta and next unpaid step

Accepted delta: the lower obstruction for GU' on arbitrary nullity-two
shields increases from `277/96` to above `2.974`, with a nonquadratic genuine
Boolean witness.

Rejected wording: bentness and `I=m-1` do not extend to shields with extra
dependent physical `x` inputs merely because all rows are nonzero.

Still unpaid: a dimension-independent lower bound on the aggregate child
upper-set logarithms imposed by dual-bent derivatives, sufficient for
`G<=3I`, or a rigorous larger-width counterexample crossing 3. Neither the
finite witness nor plateaued FEI supplies that payment.

