# Affine-cylinder FEI lifting theorem

All logarithms are base two.  For a real function `u` on a Boolean cube set

\[
 \mathcal E(u)=\sum_S \widehat u(S)^2
       \log\frac1{\widehat u(S)^2},\qquad
 \mathcal I(u)=\sum_S |S|\widehat u(S)^2.
\]

For Boolean functions, `\mathcal E=H` is the usual spectral entropy.

## Theorem

Let the physical coordinates be partitioned as `T \sqcup M`, with
`|T|=t`, `|M|=m`.  Let `A'=a+V\subseteq\mathbb F_2^M` be affine, with
`\dim V=d`, `r=m-d`, and assume

\[
 e_j\notin V\quad (j\in M).
\tag{1}
\]

Thus every coordinate in `M` is transverse to `A'`.  Put `p=2^{-r}` and
let

\[
 b(x,y)=1_{A'}(y)g_y(x),\qquad g_y:\{-1,1\}^T\to\{-1,1\}.
\tag{2}
\]

Assume every fiber satisfies `H(g_y)\le C I(g_y)`.  Then

\[
 \boxed{\mathcal E(b)
   \le C\,\mathcal I_T(b)+4\,\mathcal I_M(b)
   \le \max\{C,4\}\mathcal I(b).}
\tag{3}
\]

The constant `4` on the transverse part is sharp, already for point
support.  No constant depends on `t,m,d,r,p`, the sign patterns, or the
number of affine labels.

## Exact spectral decomposition

Identify `A'` with `\mathbb F_2^d` by choosing a basis of `V`.  For each
`S\subseteq T`, define

\[
 c_S(y)=\widehat{g_y}(S),\qquad
 q_{S,\lambda}=\left|\widehat{c_S}^{\,V}(\lambda)\right|^2,
 \quad \lambda\in V^*.
\tag{4}
\]

Parseval in each fiber and then on `V` gives

\[
 \sum_{S,\lambda}q_{S,\lambda}=1.
\tag{5}
\]

Every character of `V` has exactly `2^r` extensions to the ambient group
on `M`.  Directly from (2), each corresponding ambient Fourier coefficient
has squared magnitude `p^2q_{S,\lambda}`.  Hence

\[
 \boxed{\mathcal E(b)=2rp+pH(Q),}
 \qquad Q=(q_{S,\lambda})_{S,\lambda}.
\tag{6}
\]

This identity retains the coherent Fourier transform across all affine
labels; no orthogonality or positive-energy hypothesis is inserted.

## Paying the joint label spectrum

Let

\[
 w_S=\sum_\lambda q_{S,\lambda}
     =\mathbb E_{y\in A'}\widehat{g_y}(S)^2.
\tag{7}
\]

Consider the classical joint law

\[
 \Pr[Y=y,S=s]=2^{-d}\widehat{g_y}(s)^2.
\tag{8}
\]

Its `S`-marginal is `w`.  Therefore the elementary entropy bound for a
mixture gives

\[
 H(w)\le H(Y)+H(S\mid Y)
      =d+\mathbb E_{y\in A'}H(g_y).
\tag{9}
\]

Conditional on `S`, the quotient frequency `\lambda` has at most `2^d`
values.  Thus

\[
 H(\Lambda\mid S)\le d.
\tag{10}
\]

Combining (9) and (10),

\[
 \boxed{H(Q)\le 2d+\mathbb E_yH(g_y)
       \le2d+C\mathbb E_y I(g_y).}
\tag{11}
\]

The two appearances of `d` have different meanings: one reveals the hidden
physical affine label in the mixture of fiber spectra, while the other pays
the quotient-frequency conditional entropy.  Both will be paid once by the
same transverse boundary budget.

## Exact influence decomposition

For `i\in T`, a physical flip remains in the same affine fiber, so

\[
 \mathcal I_T(b)=p\,\mathbb E_{y\in A'}I(g_y).
\tag{12}
\]

For `j\in M`, (1) says `A'` and `A'+e_j` are disjoint.  The squared
difference is one on their union, whose measure is `2p`; therefore

\[
 I_j(b)=\frac p2,qquad
 \mathcal I_M(b)=\frac{mp}{2}=\frac{(r+d)p}{2}.
\tag{13}
\]

Insert (11)--(13) into (6):

\[
\begin{aligned}
 \mathcal E(b)
 &\le 2rp+2dp+Cp\mathbb E_yI(g_y)\\
 &=4\mathcal I_M(b)+C\mathcal I_T(b),
\end{aligned}
\]

which proves (3).

## Sharpness

Take `T=\varnothing` and `A'` to be one point in an `m`-cube.  Then

\[
 \mathcal E(1_{A'})=2m2^{-m},\qquad
 \mathcal I(1_{A'})=m2^{-m-1},
\]

so their ratio is exactly `4` in every dimension.

## Coherent-overlap consequence

The preceding A058 affine-collision theorem applies to every affine support,
without the transversality assumption.  If `q=|b|=1_{\{-1,1\}^T\times A'}`
and a Boolean realization has the form `F=a+hb`, then

\[
 \mathcal E(hb)\le H(F)+\mathcal E(q)\le H(F)+\mathcal E(b).
\tag{14}
\]

Equation (3) now supplies a single physical source-influence payment for the
entire signed affine-cylinder term in (14).  It handles arbitrary variation
of the sign pattern across the affine labels and strictly extends the earlier
all-coordinates-transverse case.

## Restriction heredity

If the fiber class is closed under physical restrictions with the same
constant `C`, then the class above is also restriction hereditary.

- Restricting a coordinate of `T` restricts every Boolean fiber.
- Restricting a coordinate of `M` intersects `A'` with a coordinate slice
  and projects it.  A new coordinate axis in the projected direction would
  lift to an old coordinate axis in `V`, contradicting (1).

Thus neither a per-depth constant nor a per-piece affine-label charge is
introduced along an adaptive physical hierarchy.

## Scope

This is a proper-class theorem, not full FEI.  If `A'` is the whole outer
cube, then there is no transverse boundary and the statement reduces to the
assumed FEI bound for the fibers.  General non-affine supports, including the
corrected X007 support, remain outside the theorem.

