# Proof: parity mask and point defect on the same physical block

## 1. Class and prior boundary

Let the uniform cube be indexed by subsets of `[n]`.  Fix `z` and define
`d_z(x)=1-2 1_{x=z}`.  For `A subseteq [n]` and `sigma in {+1,-1}`, let

\[
f=\sigma\chi_A d_z.
\]

Global sign and translation of `z` do not change the squared Fourier law or
any of `U,G,I`, so take `sigma=1,z=0`.  Unlike the previous exact
character-core closure, `chi_A` and `d_0` live on the same block.  This is a
genuine upper-set collision because symmetric-difference translation of a
Fourier law does not preserve inclusion.

## 2. Fourier and upper-set laws

Write `N=2^n`, `tau=2/N`, `p=(1-tau)^2`, and `q=tau^2`.
The point defect has Fourier amplitude `1-tau` at the empty set and
amplitude of magnitude `tau` elsewhere.  Multiplication by `chi_A` shifts
indices by symmetric difference with `A`; hence

\[
p_f(T)=\begin{cases}p,&T=A,\\q,&T\ne A.\end{cases}\tag{1}
\]

For any `S`, there are `2^(n-|S|)` supersets.  The heavy atom is among them
exactly when `S subseteq A`.  Thus

\[
\pi_f(S)=q2^{n-|S|}+(p-q)1_{S\subseteq A}.\tag{2}
\]

Let `r=|A|`.  Grouping by `s=|S|` yields

\[
\begin{aligned}
U_{n,r}={}&p\log_2\frac{p+q(2^{n-r}-1)}p\\
&+q\sum_{s=0}^{r-1}{r\choose s}
 \log_2\frac{p+q(2^{n-s}-1)}q\\
&+q\sum_{s=0}^n\left({n\choose s}-{r\choose s}\right)(n-s),
\end{aligned}\tag{3}
\]

where `{r choose s}=0` for `s>r`, and zero masses use the continuous
convention.  Formula (3) includes the endpoint `n=1`.

The influence follows directly from (1):

\[
I_{n,r}=rp+q\left(\sum_T|T|-r\right)
=rp+q(n2^{n-1}-r).\tag{4}
\]

## 3. Physical restriction and the signed remainder

Fix a coordinate `i`.  Exactly one restriction contains the exceptional
point `z`; on that branch the factor remains a point defect.  The other
restriction is a pure character and has `U=0`.

If `i notin A`, the active child has parameters `(n-1,r)`.  If `i in A`,
the restricted character loses `i`, so the active child has parameters
`(n-1,r-1)`.  Global branch signs do not affect `U`.  Summing the physical
decrements gives

\[
G_{n,r}=nU_{n,r}-\frac{n-r}{2}U_{n-1,r}
-\frac r2U_{n-1,r-1}.\tag{5}
\]

There is no missing terminal term: every inactive child is a character and
has exactly zero `U`.  The active posterior weight is the actual uniform
one-half, charged once per physical coordinate.

## 4. Uniform bound for nonempty masks

Assume `r>=1`.  Every `U` is nonnegative, so (5) gives

\[
G_{n,r}\le nU_{n,r}.\tag{6}
\]

Since `pi(S)<=1`, termwise

\[
U_{n,r}\le\sum_Sp_f(S)\log_2\frac1{p_f(S)}=:H_n.\tag{7}
\]

The entropy `H_n` depends only on `n`, not on the translated heavy atom.
Also (4) gives `I_{n,r}>=rp>=p`.

It remains to prove `nH_n<=16p`.  For `n=2`, the four spectral masses are
uniform and `nH_n=4=16p`.  For `n=3`, entropy is at most three bits, so
`nH_n<=9=16(9/16)=16p`.

For `n>=4`, use `tau<=1/8` and

\[
\begin{aligned}
H_n
&=-p\log_2p-(N-1)q\log_2q\\
&\le\frac{1-p}{\ln2}+\frac2\tau\tau^2\,2(n-1)\\
&\le3\tau+4\tau(n-1)=\tau(4n-1).
\end{aligned}\tag{8}
\]

Here `-p ln p<=1-p`, `1/ln2<3/2`, and `1-p<=2tau`.
The sequence

\[
a_n=\frac{n(4n-1)}{2^{n-1}}
\]

is decreasing for `n>=4`, because

\[
2n(4n-1)-(n+1)(4n+3)=4n^2-9n-3>0.
\]

Thus `nH_n<=a_4=15/2`.  Meanwhile
`16p>=16(7/8)^2=49/4`, proving the desired inequality with strict margin.
Combining (6)--(8) and `I>=p` gives

\[
G_{n,r}\le16I_{n,r}\qquad(r>=1).\tag{9}
\]

For `n=1`, the functions are constants or characters and `G=U=0`.

## 5. Empty mask and tensor closure

For `r=0`, the earlier all-dimensional point-defect proof gives

\[
G_{n,0}\le\kappa_{pd}I_{n,0},\qquad
\kappa_{pd}=\frac14+\frac94\log_2\frac{16}{9}<16.
\]

This run imports that proved claim rather than presenting it as new.

For functions on disjoint blocks, the spectral laws and upper masses
factor.  Consequently `U`, `G`, and `I` add exactly under products.  Every
finite product of masked defects and pure characters therefore satisfies
`G<=16I`.  Its physical restrictions stay in the same generated class:
restricting a masked defect produces one smaller masked defect and one pure
character.  The class is restriction closed.

The GU induction gives `U<=16I` on this class, and the reviewed entropy
reduction `H<=2(I-Var)+2U` gives `H<=34I`.  Neither conclusion is asserted
for all Boolean functions.

## 6. What remains

The argument pays the changing activation exactly because one child is a
zero-`U` terminal character.  A general shared-coordinate collision has two
nonterminal children, and its sign-oriented `Omega` drift can no longer be
dropped as a nonnegative child term.  The next target is the two-nonterminal
analogue of (6), using source influence plus a single-use terminal oriented
reserve.

