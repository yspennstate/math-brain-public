# B12 / A058 — signed-ensemble gluing and symmetry split

## Outcome

**PROVED a universal, depth-free signed gluing ledger; REFUTED its projection
to a prescribed sign.  Independent review pending.**

For arbitrary real functions `b_1,\ldots,b_k` with pairwise disjoint physical
supports, define

\[
 b_\varepsilon=\sum_j\varepsilon_jb_j,
 \qquad\varepsilon\in\{-1,1\}^k.
\]

Then

\[
 \boxed{\mathbb E_\varepsilon\mathcal E(b_\varepsilon)
 \le\sum_j\mathcal E(b_j),}
\qquad
 \boxed{\mathbb E_\varepsilon\mathcal I(b_\varepsilon)
 =\sum_j\mathcal I(b_j).}
\]

There is no loss in dimension, number of pieces, densities, Fourier overlap,
or gluing depth.  The theorem retains all coherent collisions: averaging the
relative signs kills cross terms only after the complete target functions
have been formed.

For two pieces this is the signed companion ledger

\[
 \mathcal E(b_0+b_1)+\mathcal E(b_0-b_1)
 \le2\mathcal E(b_0)+2\mathcal E(b_1),
\]

with exact equality for the corresponding influence sum.

## Boolean bridge

For any Boolean `f` and Hamming-cube isometry `\tau`, let

\[
 a=(f+f\circ\tau)/2,\qquad b=(f-f\circ\tau)/2.
\]

These are disjoint ternary agreement/disagreement masks, and the signed
ledger gives

\[
 \boxed{H(f)\le\mathcal E(a)+\mathcal E(b),\qquad
 I(f)=\mathcal I(a)+\mathcal I(b).}
\]

Therefore, if both masks are covered by the preceding affine-cylinder
theorem with fiber constant `C`, then

\[
 \boxed{H(f)\le\max\{C,4\}I(f).}
\]

This is the requested two-piece Boolean gluing theorem: the binary label is
paid once, with no piece-count or hierarchy-depth recharge.

## Exact obstruction to a fixed-sign projection

The stronger inequality

\[
 \mathcal E(b_0+b_1)\le\mathcal E(b_0)+\mathcal E(b_1)
\]

is false.  A three-bit exact witness is

\[
 b_0=(1,1,1,1,1,1,1,0),\quad
 b_1=(0,0,0,0,0,0,0,-1).
\]

Here `b_0+b_1` is a one-point defect, while `b_0-b_1` is constant, and

\[
 \mathcal E(b_0+b_1)-\mathcal E(b_0)-\mathcal E(b_1)
 =0.515679411089406\ldots>0.
\]

The sign is certified exactly by

\[
 7^{98}>2^{128}3^{72}.
\]

Thus the companion signing is essential.  A proof for a prescribed physical
sign must produce a symmetry, activation witness, or terminal reserve linking
that sign to the ensemble.

## Verification

The checker exhaustively tested all 377,504 nontrivial disjoint two-piece
ternary decompositions in dimension three.  It found 2,048 failures of
single-sign subadditivity and no failure of the signed-pair theorem or exact
influence identity.  Another 1,014 deterministic multi-piece cases through
dimension six verified the full ensemble theorem.

## Remaining universal gap

The theorem proves that no combinatorial factor in piece count or depth is
intrinsic: the complete sign ensemble is already uniformly paid.  The sole
remaining step in this mechanism is to control the correlation gap between
the actual physical signing and its ensemble average.  The next attempt is a
posterior activation witness or a symmetry pairing over an adaptive hierarchy,
tested against X007, the signed-mask tensor family, rare switches, and
whole-set addressing.

Full FEI remains **OPEN**.

