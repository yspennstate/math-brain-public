# Signed-ensemble gluing for disjoint physical pieces

All logarithms are base two.  For a real function `u`, write

\[
 \mathcal E(u)=\sum_S\widehat u(S)^2
   \log\frac1{\widehat u(S)^2},\qquad
 \mathcal I(u)=\sum_S|S|\widehat u(S)^2.
\]

## Theorem: arbitrary finite signed ensemble

Let `b_1,\ldots,b_k` be real functions on the same Boolean cube with
pairwise disjoint physical supports.  For
`\varepsilon\in\{-1,1\}^k`, put

\[
 b_\varepsilon=\sum_{j=1}^k\varepsilon_jb_j.
\]

Then

\[
 \boxed{\mathbb E_\varepsilon\mathcal E(b_\varepsilon)
        \le\sum_{j=1}^k\mathcal E(b_j),}
\tag{1}
\]

and

\[
 \boxed{\mathbb E_\varepsilon\mathcal I(b_\varepsilon)
        =\sum_{j=1}^k\mathcal I(b_j).}
\tag{2}
\]

There is no dependence on dimension, number of pieces, piece densities,
overlap of their Fourier spectra, or a gluing-tree depth.

### Proof of (1)

Let

\[
 p_j=\|b_j\|_2^2,\quad p=\sum_jp_j,
 \quad P_j(S)=\frac{\widehat b_j(S)^2}{p_j},
 \quad \theta_j=\frac{p_j}{p},
\]

omitting zero pieces.  Physical disjointness implies
`\|b_\varepsilon\|_2^2=p` for every sign vector.  Thus

\[
 Q_\varepsilon(S)
 =\frac1p\left|\sum_j\varepsilon_j\widehat b_j(S)\right|^2
\]

is a probability law.  Averaging the Rademacher signs kills all cross terms:

\[
 \mathbb E_\varepsilon Q_\varepsilon(S)
 =\sum_j\theta_jP_j(S)=:R(S).
\tag{3}
\]

Shannon concavity and the standard entropy bound for a mixture give

\[
 \mathbb E_\varepsilon H(Q_\varepsilon)
 \le H(R)
 \le H(\theta)+\sum_j\theta_jH(P_j).
\tag{4}
\]

Since

\[
 \mathcal E(b_\varepsilon)=p\log\frac1p+pH(Q_\varepsilon)
\]

and

\[
 \sum_j\mathcal E(b_j)
 =p\log\frac1p+pH(\theta)+p\sum_j\theta_jH(P_j),
\]

(1) follows.

### Proof of (2)

For each Fourier coordinate,

\[
 \mathbb E_\varepsilon
 \left|\sum_j\varepsilon_j\widehat b_j(S)\right|^2
 =\sum_j\widehat b_j(S)^2.
\]

Multiply by `|S|` and sum.

## Two-piece signed ledger

For two disjoint pieces, let `b_+=b_0+b_1` and `b_-=b_0-b_1`.
The four sign vectors reduce, up to a global sign, to these two functions.
Hence

\[
 \boxed{\mathcal E(b_+)+\mathcal E(b_-)
 \le2\mathcal E(b_0)+2\mathcal E(b_1),}
\tag{5}
\]

\[
 \boxed{\mathcal I(b_+)+\mathcal I(b_-)
 =2\mathcal I(b_0)+2\mathcal I(b_1).}
\tag{6}
\]

Consequently, if every piece satisfies FEI with constant `C`, then

\[
 \mathbb E_\varepsilon
 [\mathcal E(b_\varepsilon)-C\mathcal I(b_\varepsilon)]\le0.
\tag{7}
\]

At least one signing is therefore good with the same constant.  Selecting a
specified physical signing is exactly the remaining activation-witness
problem; (7) introduces no piece-count or depth loss.

## Boolean symmetry-split corollary

Let `f` be Boolean and let `\tau` be a Hamming-cube isometry.  Put

\[
 a=\frac{f+f\circ\tau}{2},\qquad
 b=\frac{f-f\circ\tau}{2}.
\tag{8}
\]

Pointwise, `a,b\in\{-1,0,1\}` and their supports are disjoint.  Moreover

\[
 f=a+b,\qquad f\circ\tau=a-b.
\]

Cube isometries preserve Fourier entropy and influence.  Applying (5)--(6),

\[
 \boxed{H(f)\le\mathcal E(a)+\mathcal E(b),}
 \qquad
 \boxed{I(f)=\mathcal I(a)+\mathcal I(b).}
\tag{9}
\]

Thus any uniform payments
`\mathcal E(a)\le C\mathcal I(a)` and
`\mathcal E(b)\le C\mathcal I(b)` prove FEI for `f` with the same `C`.

Combining (9) with the preceding affine-cylinder theorem yields a new Boolean
class: if the agreement and disagreement masks in (8) are both payable
affine cylinders with fiber constant `C`, then

\[
 \boxed{H(f)\le\max\{C,4\}I(f).}
\tag{10}
\]

This is a physical two-piece gluing theorem with no recharge.  The Fourier
spectra of `a` and `b` may overlap; only their physical supports are disjoint.

## Averaging is necessary

Single-sign subadditivity is false even in dimension three.  In lexicographic
truth-table order take

\[
 b_0=(1,1,1,1,1,1,1,0),\qquad
 b_1=(0,0,0,0,0,0,0,-1).
\]

Then `b_+=b_0+b_1` is the one-point-defect Boolean function and
`b_-=b_0-b_1\equiv1`.  Their squared Walsh-numerator histograms are

\[
\begin{array}{c|c}
 b_0&\{1:7,49:1\}\\
 b_1&\{1:8\}\\
 b_+&\{4:7,36:1\}\\
 b_-&\{64:1\}.
\end{array}
\]

Direct evaluation gives

\[
 \mathcal E(b_+)-\mathcal E(b_0)-\mathcal E(b_1)
 =\frac{11}{32}
  +\frac9{16}\log\frac{16}{9}
  -\frac{49}{64}\log\frac{64}{49}
 =0.515679411089406\ldots>0.
\tag{11}
\]

Multiplying (11) by `64` and exponentiating shows that its sign is exactly

\[
 7^{98}>2^{128}3^{72},
\]

an integer comparison.  Hence neither (1) nor (5) can be projected onto an
arbitrarily prescribed sign without an additional witness or reserve.

## Scope

The ensemble theorem is universal for disjoint physical pieces and survives
X007, rare activation, near tensors, and addressing because it uses only
Rademacher cancellation and normalized probability laws.  It does not by
itself prove FEI for the one fixed signing supplied by an arbitrary Boolean
function.  Full FEI remains open.

