# Exact GU factorization under reused character cores

All logarithms are base two.  For a Boolean function `f` let

\[
p_f(S)=\widehat f(S)^2,\qquad
\pi_f(S)=\sum_{T\supseteq S}p_f(T),
\]

\[
U(f)=\sum_Sp_f(S)\log_2\frac{\pi_f(S)}{p_f(S)},
\qquad
G(f)=\sum_i\left[U(f)-\frac{U(f_{i,+})+U(f_{i,-})}{2}\right].
\]

Zero-mass summands are zero.

## 1. Frozen candidate and GU implication

Let `Y` be a shared physical block.  Let `X_1,...,X_m` be pairwise disjoint
blocks, all disjoint from `Y`.  For arbitrary `R_j subseteq Y` and arbitrary
Boolean `f_j` on `X_j`, define

\[
g_j(y,x_j)=\chi_{R_j}(y)f_j(x_j),\qquad
F=\prod_{j=1}^m g_j,qquad
R=R_1\triangle\cdots\triangle R_m.                    \tag{1}
\]

The exact candidate is

\[
\boxed{U(F)=\sum_jU(f_j),\qquad G(F)=\sum_jG(f_j)}       \tag{2}
\]

together with the already established influence law

\[
\boxed{I(F)=|R|+\sum_jI(f_j).}                           \tag{3}
\]

Consequently, for every fixed `a>=0` and `0<=b<1`, if

\[
G(f_j)\le aI(f_j)+bU(f_j)\quad\text{for every }j,       \tag{4}
\]

then

\[
\boxed{G(F)\le aI(F)+bU(F).}                            \tag{5}
\]

If the residual class is restriction-closed and satisfies (4), the reviewed
GU induction applies throughout the generated character-overlap class and
gives

\[
U(F)\le\frac{a}{1-b}I(F),\qquad
H(F)\le\left(2+\frac{2a}{1-b}\right)I(F).               \tag{6}
\]

Thus proving (2) removes physical disjointness for arbitrarily reused
character cores without changing the candidate GU pair.

## 2. Upper-set factorization

Equation (1) collapses pointwise to

\[
F=\chi_R\prod_jf_j.                                      \tag{7}
\]

Write a Fourier set in the support of `F` uniquely as

\[
S=R\cup T_1\cup\cdots\cup T_m,
\qquad T_j\subseteq X_j.
\]

Every supported Fourier set contains exactly the same core `R`, and no
supported set contains a coordinate of `Y\setminus R`.  Fourier
factorization on the residual blocks therefore gives

\[
p_F(S)=\prod_jp_{f_j}(T_j).                              \tag{8}
\]

For a supported `S`, all supported supersets also have core exactly `R`.
Hence the upper-set mass factorizes with no core term:

\[
\pi_F(S)=\prod_j\pi_{f_j}(T_j).                          \tag{9}
\]

Taking the `p_F`-expectation of the logarithm of (9)/(8) proves

\[
U(F)=\sum_jU(f_j).                                       \tag{10}
\]

This is stronger than entropy invariance under a character shift: it uses
the deterministic-core support geometry of every upper set.

## 3. Complete physical restriction decrement

Consider first a residual coordinate `i in X_j`.  Restricting it changes only
`f_j`; the fixed core remains `R`, and all other residual factors are
unchanged.  Applying (10) to both children gives

\[
\Delta_iU(F)
=U(f_j)-\frac{U((f_j)_{i,+})+U((f_j)_{i,-})}{2}
=\Delta_iU(f_j).                                         \tag{11}
\]

Now let `i in Y`.  If `i notin R`, the realized product is independent of
`i`, so `Delta_i U(F)=0`.  If `i in R`, its two restrictions are

\[
F_{i,+}=\chi_{R\setminus\{i\}}\prod_jf_j,qquad
F_{i,-}=-\chi_{R\setminus\{i\}}\prod_jf_j.
\]

Both have the same `U` as `F` by (10), since the remaining core is still
deterministic and a global sign does not change squared Fourier masses.
Thus again

\[
\Delta_iU(F)=0.                                          \tag{12}
\]

Summing (11)--(12) over every physical coordinate proves the second identity
in (2).  The complete signed coherent remainder of every reused core query is
exactly zero; its only surviving reserve is the nonnegative influence
`|R|` in (3).

Finally, summing (4) and using (2)--(3),

\[
G(F)\le a\sum_jI(f_j)+b\sum_jU(f_j)
=a(I(F)-|R|)+bU(F)\le aI(F)+bU(F),
\]

which proves (5).  The restriction-closed implication (6) is exactly the
reviewed GU-to-`U/I` induction followed by the reviewed inequality
`H<=2(I-Var)+2U<=2I+2U`.

## 4. Scope and remaining gap

The theorem allows:

- any number of factors and shared core coordinates;
- arbitrary reuse multiplicities, including even cancellations;
- arbitrary selector bias and Fourier complexity inside each residual;
- arbitrary depth obtained by iterating the construction; and
- the same admissible pair `(a,b)` with no accumulated tax.

It does not cover a shared coordinate whose dependence is non-character in
one of the factors.  There the Fourier core is no longer deterministic and
the upper-set cone does not split as (9).  The previously certified
four-channel witness shows that separate endpoint potentials cannot repair
that general case.  The next step is therefore to replace deterministic
core membership by a two-point posterior core law and bound its signed
correlation term once, without projecting to a fixed sign or to an unsigned
indicator payment.

Universal GU and full FEI remain open.

