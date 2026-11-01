# Dense-nullity-two retained-credit theorem

All vector spaces are over \(\mathbb F_2\), logarithms are base two, and
\(U\) is computed in the original physical Fourier basis.

## 1. Class and root reservoir

Let \(M\in\mathbb F_2^{s\times m}\) have rank \(r=m-2\), and put
\[
 P(x,y)=(-1)^{x^TMy+a\cdot x+b\cdot y+c}D(y),              \tag{1}
\]
where \(D\) is an arbitrary Boolean function.  No linear change of the
physical \(y\)-coordinates is allowed.  Thus \(\ker M\) may be dense.

Write \(K=\ker M\), and let \(Z=\{j:Me_j=0\}\), \(k=|Z|\le2\).  Summing
the Fourier coefficient first over \(x\) decomposes the spectrum into the
\(2^r\) affine cosets of \(K\).  If \(E_\alpha\) is the Boolean two-bit
fiber on the coset indexed by \(\alpha\), then
\[
 H(P)=2r+\mathbb E_\alpha H(E_\alpha).                     \tag{2}
\]

Every nonzero row of \(M\) contributes physical influence \(1/2\), and
rank supplies at least \(r\) such rows.  Every nonzero column also
contributes \(1/2\), because its derivative contains a nonconstant
character of \(x\).  For a zero column, the influence is the average fiber
influence in the corresponding physical direction.  Hence, with
\[
 J=\mathbb E_\alpha\sum_{j\in Z}\operatorname{Inf}_{e_j}(E_\alpha),
\]
\[
 I(P)\ge {r\over2}+{m-k\over2}+J.                          \tag{3}
\]

Every two-bit Boolean function is affine or bent.  Therefore, in any \(k\)
specified independent physical directions,
\[
 H(E)\le2-k+2\sum_{j\in Z}\operatorname{Inf}_{e_j}(E).     \tag{4}
\]
Using \(m=r+2\), equations (2)--(4) give the physical-basis root reservoir
\[
 \boxed{U(P)\le H(P)\le2I(P).}                             \tag{5}
\]
This reproduces the needed input directly rather than treating the B01
status label as proof evidence.

## 2. Complete signed node charge

Let \(h\) be an arbitrary Boolean function on a disjoint physical block.
Let \(\mathcal T\) be any finite deterministic adaptive or pruned
restriction tree querying only coordinates of \(P\).  A coordinate may be
queried at incomparable nodes, but not twice on one root-to-leaf path.  For
an internal node \(v\), let \(i_v\) be its query, \(w_v\) its uniform-cube
probability, and
\[
 \Delta_vU=U(P_vh)-\frac{U(P_{v,0}h)+U(P_{v,1}h)}2.
\]
The exact local identity is
\[
 \Delta_vU=B_{i_v}(P_vh)-\Gamma_{i_v}(P_vh)+K_{i_v}(P_vh), \tag{6}
\]
including the empty-set term and the full binary-KL asymmetry \(K_i\).
No sign is discarded.

Summing (6) over the tree makes all internal child potentials cancel:
\[
 \sum_{v\in\mathcal T^\circ}w_v\Delta_vU
 =U(Ph)-\sum_{\ell}w_\ell U(P_\ell h).                    \tag{7}
\]
Disjoint tensor additivity gives \(U(P_vh)=U(P_v)+U(h)\), so the arbitrary
terminal core cancels exactly once, not once per ancestor:
\[
 U(Ph)-\sum_\ell w_\ell U(P_\ell h)
 =U(P)-\sum_\ell w_\ell U(P_\ell).                        \tag{8}
\]
Since every leaf upper-set potential is nonnegative, (5) proves
\[
 \boxed{
 \sum_{v\in\mathcal T^\circ}w_v
   [B_{i_v}-\Gamma_{i_v}+K_{i_v}]
 \le2I(P).}                                                \tag{9}
\]
The constant is independent of dimension, kernel orientation, bias,
fiber variation, tree depth, pruning policy, restriction order, and dyadic
leaf rarity.

Equation (9) is genuinely nonlocal.  Individual \(K_i\)'s are not bounded
by a fixed multiple of the corresponding local influence; positive and
negative signed node charges are retained until the terminal boundary.

## 3. First-revelation and terminal ledger

The ordinary influence telescope is
\[
 I(P)=\sum_{v\in\mathcal T^\circ}w_v
       \operatorname{Inf}_{i_v}(P_v)
      +\sum_\ell w_\ell I(P_\ell).                         \tag{10}
\]
Combining (7)--(10) yields the stronger signed terminal form
\[
 \boxed{
 \sum_v w_v\Delta_vU
 \le 2\sum_vw_v\operatorname{Inf}_{i_v}(P_v)
   +\sum_\ell w_\ell[2I(P_\ell)-U(P_\ell)].}              \tag{11}
\]
The terminal bracket is retained with its sign; it is not silently assumed
nonnegative after a control restriction.  Thus each physical pivotal event
is spent only at its first query, while all unqueried influence and terminal
\(U\) remain at the leaves.

If only \(y\)-coordinates are restricted, deletion of a matrix column
cannot increase nullity above two, so every descendant remains in the same
class and its bracket in (11) is nonnegative.  If an \(x\)-coordinate is
restricted, deletion of a rank-essential row can raise nullity from two to
three.  The coefficient-two fiber lemma may then fail locally.  This is why
(9) is charged from the root reservoir and not reapplied independently at
every descendant.

## 4. Control-first versus data-first

The first higher-nullity child is explicit.  Take
\[
 M=\begin{pmatrix}1&1&0&0\\0&0&1&0\end{pmatrix},
 \qquad D(y)=-1\Longleftrightarrow y_1=y_3=y_4=0.           \tag{12}
\]
The root has nullity two.  Restricting the second \(x\)-coordinate deletes
the second row and produces the nullity-three point-defect shield in one
child (up to an affine character in the other).  Its entropy satisfies
\[
 H-2I=-{1\over4}+{9\over16}\log_2{16\over9}>0.             \tag{13}
\]
Thus a control-first proof cannot reissue a fresh coefficient-two entropy
certificate at that child.  By contrast, data-first restrictions preserve
nullity at most two.  Nevertheless, for every complete order both signed
ledgers in (7) telescope to the same root \(U(P)\); the checker records the
different level charges and their identical total.  This isolates the
global refund: it is the terminal upper-set potential plus unspent physical
influence, not a local fixed-price \(K_i\) estimate.

## 5. Scope

The theorem covers arbitrary changing four-point fibers behind every
physical rank-\((m-2)\) shield and arbitrary common disjoint terminal cores.
It strictly removes the coordinate-alignment hypothesis from the preceding
B05 fixed-width theorem.

It does not cover nullity growing with dimension, querying variables of the
arbitrary terminal core, or a hierarchy in which a different nonflat core is
introduced after each activation.  A width-uniform extension already
contains arbitrary Boolean tensor factors and is full-FEI strength.  Full
FEI therefore remains open.
