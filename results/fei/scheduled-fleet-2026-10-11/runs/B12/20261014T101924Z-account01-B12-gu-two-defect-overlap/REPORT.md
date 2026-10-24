# B12 / A058 — two-nonterminal two-defect overlap

**Run:** `20261014T101924Z-account01-B12-gu-two-defect-overlap`  
**Stable gap:** `B12-A058-SHARED-COORDINATE-OVERLAP`  
**Attempt:** `A058-GU-TWO-DEFECT-OVERLAP-14`  
**Status:** new two-nonterminal overlap class PROVED pending independent
review; universal GU OPEN.

## Frozen candidate and implication

For distinct cube points `z_0,z_1`, a parity mask `A`, and a global sign,
consider

\[
f(x)=\sigma\chi_A(x)
 \left(1-2\mathbf1_{x=z_0}-2\mathbf1_{x=z_1}\right).\tag{1}
\]

The mask and both defects use the same physical variables.  Coordinates on
which `z_0,z_1` differ have **two nonterminal children**: each restriction is
a parity-masked point defect.  Thus the previous terminal-character shortcut
does not apply on those coordinates.

The frozen pair was

\[
\boxed{G(f)\le32I(f)}\qquad(a,b)=(32,0).\tag{2}
\]

Equation (2) is proved for every function (1), and for arbitrary disjoint
products of one-defect factors, two-defect factors, and characters.  This
generated class is restriction closed, so

\[
U(f)\le32I(f),\qquad H(f)\le66I(f)\tag{3}
\]

on the class.  If (2) held for every Boolean function, (3) would be the
universal GU/FEI implication.  No such universal claim is made here.

## Exact parity-coset kernel

Let `D=z_0 xor z_1`, `d=|D|`, `N=2^n`,
`p=(1-4/N)^2`, and `q=16/N^2`.  Put

\[
E_D=\{R:|R\cap D|\text{ is even}\}.
\]

The squared Fourier law is

\[
p_f(A)=p,qquad
p_f(T)=q\quad(T\ne A,\ T\triangle A\in E_D),\tag{4}
\]

and is zero otherwise.  Its complete upper-set mass is

\[
\boxed{\pi_f(S)=qC_{A,D}(S)+(p-q)\mathbf1_{S\subseteq A}},\tag{5}
\]

where

\[
C_{A,D}(S)=
\begin{cases}
2^{n-|S|-1},&D\nsubseteq S,\\
2^{n-|S|},&D\subseteq S\text{ and }d\equiv|A\cap D|\pmod2,\\
0,&\text{otherwise}.
\end{cases}\tag{6}
\]

This is an exact coherent posterior kernel, not a raw entropy proxy.

If `V_{n,d,r,t}` denotes the resulting `U`, with
`r=|A|`, `t=|A cap D|`, and `P_{m,s}` is the parity-masked one-defect `U`,
physical restriction gives

\[
\begin{aligned}
G={}&nV_{n,d,r,t}
-tP_{n-1,r-1}-(d-t)P_{n-1,r}\\
&-\frac{r-t}{2}V_{n-1,d,r-1,t}
-\frac{n-d-r+t}{2}V_{n-1,d,r,t}.
\end{aligned}\tag{7}
\]

Terms having zero multiplicity are omitted.  The first line of (7) is the
new two-nonterminal payment: both physical signs retain one defect, with the
actual mask update and no favorable-sign choice.

## Bounds

For the unmasked family `A=empty`, exact summation proves

\[
G(f)\le\kappa_{pd}I(f),\qquad
\kappa_{pd}=\frac14+\frac94\log_2\frac{16}{9}
=2.1176687467547968\ldots.\tag{8}
\]

The constant is sharp for the complete class, attained at `(n,d)=(4,1)`;
that endpoint is a three-variable point defect with a dummy direction.
For every genuinely separating type `d>=2`, the proof contains an explicit
nonpositive correction to the point-defect ratio.

For nonempty masks, `I>=p`, while `G<=nU<=nH(p_f)`.  The spectral entropy in
(4) satisfies `nH(p_f)<=32p`: the cases `n<=3` are immediate, and for
`n>=4`, writing `rho=4/N`,

\[
H(p_f)\le\rho(4n-5),
\]

with `n rho(4n-5)` decreasing from 11 while `32p>=18`.  This proves (2)
without dependence on dimension, Hamming separation, mask weight, defect
locations, sign, factor count, or depth.

## Verification and remaining gap

The checker exhausts all masks and unordered point pairs through dimension
five: 18,040 exact parity-coset kernels and physical recurrences.  Together
with higher-dimensional representatives it checks 18,500 two-defect cases,
the unmasked scalar law through dimension 50, the entropy envelope through
dimension 100, and tensor closure.  Maximum recurrence error was
`1.78e-15`.

This removes the one-terminal-child hypothesis for every separating
coordinate of a two-defect Boolean function.  It does not cover an arbitrary
defect set, where both children can retain unrelated multi-defect geometries.
The next step is the three-defect split (one defect versus two defects), then
the normalized arbitrary-set recursion needed for universal GU.

Independent review and native Brain ingestion are not observed.  Universal
GU and full FEI remain **OPEN**.

