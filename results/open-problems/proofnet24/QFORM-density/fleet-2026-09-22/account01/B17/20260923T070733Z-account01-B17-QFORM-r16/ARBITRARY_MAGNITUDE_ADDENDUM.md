# QFORM-CENTERED-BOX-INDEFINITE-3D-ARBITRARYMAG-NOESCAPE-v1

This strengthens the same run's equal-magnitude theorem before handoff. Full QFORM remains open.

## Theorem

Let `X_i~Unif[-L_i/2,L_i/2]` independently, with `L_i>=1`. Let `A` be any real symmetric **indefinite** `3x3` matrix whose three eigenvalues all have absolute value at least one. Then

\[
\boxed{
\|p_{X^TAX}\|_\infty
\le {\pi\over\sqrt2}
{\sqrt{L_1^2+L_2^2+L_3^2}\over L_1L_2L_3}
\le \pi\sqrt{3/2}
<3\sqrt2 .
}
\tag{A.1}
\]

The estimate is independent of the orthogonal eigenbasis and of the three eigenvalue magnitudes. It also survives arbitrary independent block-diagonal quadratic tails by convolution.

## Proof

After replacing `A` by `-A` if necessary and permuting spectral coordinates, write

\[
A=O^T\operatorname{diag}(\alpha,\beta,-\gamma)O,
\qquad \alpha,\beta,\gamma\ge1,
\]

and assume without loss of generality that `alpha<=beta`. As in the main report, `Y=OX` has density `m1_K`,

\[
m=(L_1L_2L_3)^{-1},\qquad
K\subset B_R(0),\qquad
R={1\over2}\sqrt{L_1^2+L_2^2+L_3^2}.
\]

Hence the desired pushforward is dominated, as a measure, by `m` times the pushforward of ball Lebesgue measure under

\[
q(x,y,z)=\alpha x^2+\beta y^2-\gamma z^2.
\]

Let `H(t)` be the latter density. Fix `z`. On the whole `(x,y)` plane the pushforward of Lebesgue measure under `alpha x^2+beta y^2` has density exactly

\[
{\pi\over\sqrt{\alpha\beta}}1_{u>0}.
\tag{A.2}
\]

Restricting to the disk `x^2+y^2<=R^2-z^2` can only decrease this density. Moreover a nonzero restricted contribution at output `t` requires

\[
0\le u:=t+\gamma z^2
\le \beta(R^2-z^2),
\tag{A.3}
\]

because `alpha<=beta` implies
`alpha x^2+beta y^2<=beta(x^2+y^2)`.

### Positive output

If `t>=0`, (A.3) implies

\[
z^2\le {\beta R^2-t\over\beta+\gamma}.
\]

Thus the admissible `z`-set has length at most

\[
2\sqrt{{\beta R^2-t\over\beta+\gamma}},
\]

and (A.2) yields

\[
H(t)
\le {2\pi\over\sqrt{\alpha\beta}}
\sqrt{{\beta R^2-t\over\beta+\gamma}}
\le {2\pi R\over\sqrt{\alpha(\beta+\gamma)}}
\le \pi\sqrt2R.
\tag{A.4}
\]

The last step uses `alpha>=1` and `beta+gamma>=2`.

### Negative output

Let `t=-s<0`. Conditions (A.3) give

\[
{ s\over\gamma}\le z^2\le {\beta R^2+s\over\beta+\gamma}.
\]

Therefore

\[
H(-s)
\le {2\pi\over\sqrt{\alpha\beta}}
\left[
\sqrt{{\beta R^2+s\over\beta+\gamma}}
-\sqrt{{s\over\gamma}}
\right].
\tag{A.5}
\]

The bracket is strictly decreasing for `s>0`, since its derivative is

\[
{1\over2\sqrt{(\beta+\gamma)(\beta R^2+s)}}
-{1\over2\sqrt{\gamma s}}<0;
\]
indeed `gamma s < (beta+gamma)(beta R^2+s)`. Hence (A.5) is maximized at `s=0`, where it equals the first upper bound in (A.4). Thus

\[
\boxed{\sup_t H(t)\le\pi\sqrt2R.}
\tag{A.6}
\]

Measure domination now gives

\[
\|p_{X^TAX}\|_\infty
\le m\pi\sqrt2R
={\pi\over\sqrt2}
{\sqrt{L_1^2+L_2^2+L_3^2}\over L_1L_2L_3}.
\]

As in the main report, `L_i>=1` implies the final ratio is at most `sqrt(3)`, and `pi^2<12` gives the strict comparison with `3sqrt(2)`.

## Scope consequence

The stronger conclusion is that **no three-physical-coordinate centered product-box witness with an indefinite three-large-eigenvalue matrix can reach the current `3sqrt(2)` lower obstruction, regardless of rotation or unequal eigenvalue magnitudes**. Any sharp or super-`3sqrt(2)` witness must leave this entire finite three-coordinate centered-box architecture (or exploit cross-coupled additional coordinates rather than an independent block-diagonal tail).

No arbitrary-law reduction to centered boxes is claimed. No continuity claim for the unrestricted target is made.
