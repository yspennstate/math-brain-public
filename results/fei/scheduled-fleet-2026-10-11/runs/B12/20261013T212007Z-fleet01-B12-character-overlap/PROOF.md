# Exact character-overlap composition and a shared-potential obstruction

All logarithms are base two.  For a real function `f` on a cube, write

\[
 \mathcal E(f)=\sum_S\widehat f(S)^2
 \log_2\frac1{\widehat f(S)^2}.
\]

For Boolean `f`, this is `H(f)`.

## 1. Character shifts and disjoint products

If `chi_R` is a Fourier character, multiplication by `chi_R` sends
`fhat(S)` to `fhat(S triangle R)`.  It only permutes the spectral law, so

\[
 H(\chi_R f)=H(f).                                           \tag{1}
\]

If Boolean `f_1,...,f_m` live on pairwise disjoint coordinate blocks, their
product has the tensor spectral law.  Therefore

\[
 H\!\left(\prod_{j=1}^m f_j\right)=\sum_{j=1}^mH(f_j),
 \qquad
 I\!\left(\prod_{j=1}^m f_j\right)=\sum_{j=1}^mI(f_j).       \tag{2}
\]

These statements are exact, including constant factors.

## 2. Arbitrary character-only physical overlap

Let `Y` be a shared physical coordinate block.  Let `X_1,...,X_m` be
pairwise disjoint residual blocks, also disjoint from `Y`.  Choose arbitrary
sets `R_j subseteq Y` and arbitrary Boolean signs `f_j` on `X_j`.  Define

\[
 g_j(y,x_j)=\chi_{R_j}(y)f_j(x_j),\qquad
 F=\prod_{j=1}^m g_j.                                       \tag{3}
\]

The same physical coordinate of `Y` may occur in any number of factors.
Let

\[
 R_\triangle=R_1\triangle\cdots\triangle R_m.
\]

Because characters square to one,

\[
 F=\chi_{R_\triangle}\prod_{j=1}^m f_j.                     \tag{4}
\]

Equations (1)--(2) now give the exact overlap laws

\[
 \boxed{H(F)=\sum_{j=1}^mH(f_j)},                            \tag{5}
\]

\[
 \boxed{I(F)=|R_\triangle|+\sum_{j=1}^mI(f_j)}.             \tag{6}
\]

Thus even overlap multiplicities cancel and odd multiplicities leave one
physical character cost.  There is no charge proportional to the total
number of appearances of a reused coordinate.

**FEI closure.**  If `H(f_j)<=C I(f_j)` for every residual factor, then

\[
 \boxed{H(F)\le C I(F)}.                                    \tag{7}
\]

The constant is preserved exactly.  It is independent of the number of
factors, total dimension, overlap count, reuse multiplicity, composition
depth, and the number of pairwise cancellations.

The two-factor selector form is worth isolating.  For antipodal endpoints
`a=0`, let

\[
 b=\chi_Q b_0,\qquad h=\chi_Rh_0,
\]

where `b_0,h_0` use disjoint residual blocks.  Although the source and
activation reuse every coordinate in `Q cap R`,

\[
 F=hb=\chi_{Q\triangle R}b_0h_0,
\]

and (5)--(7) apply.  This is a genuine overlapping-input composition, not a
fresh-selector theorem.

## 3. Why the natural shared Doob correction fails

For disjoint source and activation blocks, the preceding A057 potential is

\[
 \mathcal J(a,b;h)=\mathcal E(a+hb)-\|b\|_2^2H(h).
\]

Tensor additivity gives

\[
 \mathcal E(hb)=\mathcal E(b)+\|b\|_2^2H(h),
\]

so the representation-invariant-looking extension to shared coordinates is

\[
 \widetilde{\mathcal J}(a,b;h)
 =\mathcal E(a+hb)-\mathcal E(hb)+\mathcal E(b).             \tag{8}
\]

It agrees exactly with `J` in the disjoint case and correctly removes a
source spectrum that cancels inside the physical product `hb`.

For a coordinate `i`, let

\[
 D_i(g)=\mathcal E(g)-\frac{\mathcal E(g|_{i=-1})+
                                  \mathcal E(g|_{i=+1})}{2}.
\]

The shared-coordinate decrement of (8) is exactly

\[
 \Delta_i\widetilde{\mathcal J}
 =D_i(a+hb)-D_i(hb)+D_i(b).                                 \tag{9}
\]

Unlike the disjoint activation decrement, (9) need not be nonnegative.

### Exact three-bit Boolean witness

In lexicographic binary truth-table order, take

\[
\begin{aligned}
 u&=(-1,-1,-1,-1,-1,1,-1,-1),\\
 v&=( 1, 1, 1,-1, 1,1, 1, 1),\\
 h&=(-1, 1,-1, 1,-1,1,-1,-1),
\end{aligned}
\]

and set `a=(u+v)/2`, `b=(v-u)/2`, `F=a+hb`.  Query the third bit.
The exact Walsh spectra give

\[
 D_3(F)=D_3(a)=D_3(b)=0,                                   \tag{10}
\]

whereas

\[
 D_3(hb)=\frac54-\frac9{16}\log_2\frac{16}{9}
 =0.7830828133113008\ldots>\frac{11}{16}.                  \tag{11}
\]

Indeed `hb` has squared spectral masses
`1/4,1/4,1/16,1/16,1/16,1/16`, while each restriction has masses
`9/16,1/16,1/16,1/16`.  Therefore

\[
 \boxed{\Delta_3\widetilde{\mathcal J}
 =-\left(\frac54-\frac9{16}\log_2\frac{16}{9}\right)<0.}  \tag{12}
\]

Since both `D_3(a)` and `D_3(b)` vanish, adding any fixed linear combination
of the separate raw endpoint entropies `E(a),E(b)` cannot repair this witness.
The failure is a genuine four-channel shared-coordinate effect, not a dummy
cylinder or a non-Boolean prefix law.

## 4. Exact boundary of the result

The positive theorem permits unlimited physical reuse when every shared
dependence is a character.  It includes arbitrary cancellation patterns and
unbounded compositional depth with no growth in the FEI constant.

The witness shows that once one shared coordinate changes a non-character
activation mask and source sign simultaneously, the natural gauge-corrected
Doob potential can increase under restriction.  A general A058 theorem must
retain a signed four-channel collision credit or introduce a joint potential
that sees `a,b,h` together; separate endpoint entropies are insufficient.

This result does not prove universal overlap closure or full FEI.

