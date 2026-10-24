# Dual exact-null refinement for the zero-curvature two-bank compiler

Run: `20260923T211022Z-account01-B01-qform-auto11`  
Status: supporting algebraic refinement; full QFORM remains OPEN.

This note sharpens the terminal exact obstruction in `REPORT.md` without changing its hypotheses or conclusions.

For the symmetric five-block packet

\[
K=\begin{pmatrix}
a&p^T&q^T\\
p&A&B\\
q&B^T&C
\end{pmatrix},\qquad B\in GL_2(\mathbb R),
\]

define the U-oriented quantities

\[
d_U=a-2p^TB^{-T}q+q^TB^{-1}AB^{-T}q,
\]
\[
h_U=p-AB^{-T}q,\qquad
\theta_U=h_U^TB^{-T}q,
\]
\[
w_U=(1,-B^{-T}q,0).
\]

Define symmetrically

\[
d_V=a-2q^TB^{-1}p+p^TB^{-T}CB^{-1}p,
\]
\[
h_V=q-CB^{-1}p,\qquad
\theta_V=h_V^TB^{-1}p,
\]
\[
w_V=(1,0,-B^{-1}p).
\]

The main report proves the exact identities

\[
d_U=0\implies Kw_U=(\theta_U,h_U,0),
\]
\[
d_V=0\implies Kw_V=(\theta_V,0,h_V).
\]

Hence exact failure of the quadratic-curvature and residual-linear-slope compilers in the U orientation means `Kw_U=0`, and exact failure in the V orientation means `Kw_V=0`.

## Lemma — dual exact failure is rank three or a decoupled four-dimensional core

Assume

\[
d_U=d_V=0,
\qquad h_U=h_V=0.
\]

Then:

1. If `(p,q)!=(0,0)`, the two null vectors `w_U,w_V` are linearly independent. Consequently
   \[
   \operatorname{nullity}K\ge2,\qquad \operatorname{rank}K\le3.
   \]
   In particular, if this five-dimensional packet itself has at least three eigenvalues of modulus at least `sigma>0`, then
   \[
   \operatorname{rank}K=3
   \]
   and its three nonzero eigenvalues all have modulus at least `sigma`.

2. If `p=q=0`, then `d_U=d_V=a`, so the same exact-failure assumptions force `a=0`. The scalar `X` is then a literal quadratic null coordinate and
   \[
   K=0\oplus
   \begin{pmatrix}A&B\\B^T&C\end{pmatrix}.
   \]
   Thus the only non-rank-three dual-null endpoint is the pure four-dimensional two-bank critical core.

### Proof

The exact-null identities give `Kw_U=Kw_V=0`. Suppose the two vectors are linearly dependent. Their first coordinates are both one, so dependence forces `w_U=w_V`. Comparing the U block gives

\[
B^{-T}q=0,
\]

hence `q=0`, while comparison of the V block gives

\[
B^{-1}p=0,
\]

hence `p=0`. Therefore `(p,q)!=(0,0)` implies linear independence and nullity at least two. This proves part 1.

If `p=q=0`, the definitions reduce to `d_U=d_V=a`. Exact failure forces `a=0`, and every quadratic coupling of `X` to the two banks vanishes, proving part 2. QED.

## Consequence for the routing debt

Within an invertible two-bank packet carrying the original product provenance required by `REPORT.md`, the exact terminal states are now split as follows:

- any nonzero U- or V-oriented Schur curvature is paid by the preceding B01 square-phase `L^4` compiler;
- zero curvature but nonzero residual linear kernel slope is paid by the present run's linear-phase averaged-frequency compiler;
- if both orientations fail exactly and `(p,q)!=(0,0)`, the packet is exact rank at most three (and exact rank three under a three-large-eigenvalue packet hypothesis);
- if both fail exactly and `p=q=0`, one scalar coordinate is genuinely decoupled and only the pure four-dimensional two-bank core remains.

This does **not** by itself solve either surviving case. In particular, existing exact-rank-three results still have physical-pivot/localization scope restrictions, and the pure four-dimensional two-bank form remains at the critical `|t|^{-1}` crossing threshold. The point of the lemma is to eliminate a larger nominal simultaneous-zero-curvature class without introducing any rotation of the input law.
