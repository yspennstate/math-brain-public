# B05 / A023 — dense-nullity-two retained-\(U\) tree payment

## Outcome

**AUTHOR_PROVED_PENDING_INDEPENDENT_REVIEW.**  The coordinate-alignment
hypothesis has been removed from the complete retained-credit theorem at
kernel width two.

Let \(M\in\mathbb F_2^{s\times m}\) have rank \(m-2\), let \(D\) be
an arbitrary Boolean function, and set
\[
 P(x,y)=(-1)^{x^TMy+a\cdot x+b\cdot y+c}D(y).
\]
For every finite adaptive or pruned physical restriction tree querying
only \(P\)-coordinates, and every arbitrary Boolean terminal core \(h\) on
a common disjoint block,
\[
 \boxed{
 U(Ph)-\sum_\ell w_\ell U(P_\ell h)\le2I(P).}
\]
The constant is independent of dimension, bias, dense kernel orientation,
fiber variation, tree depth, reveal order, pruning, leaf rarity, and the
dimension or spectrum of \(h\).

Full FEI remains **OPEN**.

## Complete signed ledger

The root proof is reconstructed in `PROOF.md`.  Exact Fourier coset
decomposition and physical influence accounting give
\[
 U(P)\le H(P)\le2I(P)
\]
for every physical rank-\((m-2)\) shield, including dense kernels.

At every internal node the complete charge is retained:
\[
 \Delta_iU=B_i-\Gamma_i+K_i.
\]
Summation over the tree cancels all internal potentials, while disjoint
tensor additivity cancels the terminal \(U(h)\) packet exactly once:
\[
 \sum_vw_v(B_{i_v}-\Gamma_{i_v}+K_{i_v})
 =U(P)-\sum_\ell w_\ell U(P_\ell)\le U(P)\le2I(P).
\]
No local charge is assumed nonnegative and no KL credit is dropped.

The stronger terminal ledger is
\[
 \sum_vw_v\Delta_vU
 \le2\sum_vw_v\operatorname{Inf}_{i_v}(P_v)
 +\sum_\ell w_\ell[2I(P_\ell)-U(P_\ell)].
\]
This records every physical pivotal event at its first query and retains the
unspent influence and terminal upper-set packet with their signs.

## Ordering comparison and exact boundary

Data-coordinate restrictions delete columns and preserve kernel dimension
at most two.  Shield-control restrictions delete rows and can raise the
kernel dimension to three.  The explicit suspension
\[
 M=\begin{pmatrix}1&1&0&0\\0&0&1&0\end{pmatrix},\qquad
 D(y)=-1\Longleftrightarrow y_1=y_3=y_4=0
\]
has nullity two at the root, but restricting the second control creates the
known nullity-three point-defect child, where
\[
 H-2I=-\frac14+\frac9{16}\log_2\frac{16}{9}>0.
\]
Thus control-first descent cannot reissue the root coefficient-two entropy
certificate node by node.  Nevertheless the complete control-first and
data-first signed \(U\) ledgers both telescope to the same root value
\(U(P)=2.286560156295072\) in the checker.  Their level charges differ,
which directly isolates the global debt/refund that survives ordering.

## Case-extension record

| Field | Record |
|---|---|
| Starting class | Coordinate-aligned width-two shields |
| New class | Every physical rank-\((m-2)\) shield, including dense kernels |
| Fibers | Arbitrary and independently changing Boolean four-point fibers |
| Tree | Finite, adaptive or pruned; physical coordinates may recur on incomparable branches |
| Terminal core | Arbitrary common disjoint Boolean \(h\) |
| Previous bound | Retained loss \(\le2I(P)\) with aligned kernel |
| New bound | Retained loss \(\le2I(P)\) without alignment |
| Parameter dependence | None in dimension, orientation, depth, rarity, bias or core complexity |
| First failed extension | Local coefficient-two entropy certificate after a rank-essential control restriction creates nullity three |
| Universal gap | Changing higher-nullity coherent cores through an arbitrary hierarchy |

## Verification

`CHECK_DENSE_NULLITY_TWO_TREE.py` passed:

- 2,576 direct root cases;
- every rank-one orientation on three \(y\)-bits and every Boolean core
  modulo output complement;
- every rank-two \(2\times4\) orientation with deterministic random cores;
- 4,368 adaptive/pruned tree instances;
- 120 direct disjoint-terminal cancellation checks;
- complete control-first and data-first ordering ledgers for the
  nullity-three suspension;
- exact influence telescopes for both complete orders.

The largest sampled root \(U/I\) and retained-loss ratio were both 1.
This suggests a possible sharper \(U\le I\) theorem for the class, but no
such analytic claim is made here.

## Source pins and status

The live control revision is `2026-10-12.1`, source commit
`40210272c19f43fed84f6a67653f9a04b0e11e28`.  The preceding B05 aligned
width-four package is pinned at canonical commit
`09fe8877f0362b6b46361d2e5acbcb10f8dc5dd9`.  The dense-nullity-two root
input was read at canonical finalized commit
`f108d34dd304d03aae2d28c5160c4a32a45758d3`; its proof was reconstructed
inside this package rather than imported from a status label.

This class theorem is pending A087/A094 review.  It does not prove a
dimension-independent payment for arbitrary nullity or full FEI.

## Next unpaid step

Test and attempt the sharper affine-coset statement \(U(P)\le I(P)\) for
arbitrary-orientation nullity two.  A proof would improve the complete-tree
constant to one and may expose the exact upper-set symmetry needed at
nullity three.  Any extension must retain the control-first terminal
deficit above rather than recharging the released core at each descendant.
