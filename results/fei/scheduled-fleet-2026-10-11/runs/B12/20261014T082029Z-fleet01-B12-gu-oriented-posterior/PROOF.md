# Oriented two-sign posterior decomposition and rare-activation separation

All logarithms are base two.  Let `f_+,f_-` be arbitrary genuine Boolean
functions on the same finite uniform cube.  Use

\[
p_\pm(S)=\widehat f_\pm(S)^2,
\quad \pi_\pm(S)=\sum_{T\supseteq S}p_\pm(T),
\quad q=\frac{p_++p_-}{2},
\quad m=\frac{\pi_++\pi_-}{2}.
\]

The preceding run proved that the sign-blind center is `M-K`, where

\[
M=\sum_Sq(S)\log\frac{m(S)}{q(S)}
\]

and `K` is the binary posterior KL.  This note identifies the missing
orientation exactly and tests whether the branchwise posterior can pay it.

## 1. Exact oriented kernel

Whenever the denominators are nonzero, put

\[
t_S=\frac{p_+(S)-p_-(S)}{p_+(S)+p_-(S)},
\qquad
u_S=\frac{\pi_+(S)-\pi_-(S)}{\pi_+(S)+\pi_-(S)}.
\tag{1.1}
\]

Thus the exact-set sign posterior is `((1+t)/2,(1-t)/2)` and the upper-cone
posterior is `((1+u)/2,(1-u)/2)`.  Define

\[
\Omega(t,u;L)=tL+
\frac{1+t}{2}\log\frac{1+u}{1+t}
-\frac{1-t}{2}\log\frac{1-u}{1-t},
\tag{1.2}
\]

with the continuous endpoint convention, and

\[
Z_U(f_+,f_-)=\sum_Sq(S)\Omega\!\left(
t_S,u_S;\log\frac{m(S)}{q(S)}\right).
\tag{1.3}
\]

Direct substitution of `p_+=q(1+t)` and `pi_+=m(1+u)` gives

\[
\boxed{Z_U(f_+,f_-)=\frac{U(f_+)-U(f_-)}2.}
\tag{1.4}
\]

The KL kernel is

\[
k(t,u)=\frac{1+t}{2}\log\frac{1+t}{1+u}
       +\frac{1-t}{2}\log\frac{1-t}{1-u}.
\tag{1.5}
\]

Under exchange of the signs, `(t,u)` becomes `(-t,-u)`.  Hence `k` is even
and `Omega` is odd.  This is the exact algebraic reason that `M,K`, and every
restriction-tree functional formed only from them cannot select a prescribed
physical sign.

Combining (1.4) with the previous center theorem yields

\[
\boxed{U(f_\pm)=M-K\pm Z_U.}
\tag{1.6}
\]

Let `L` denote the complete physical restriction Laplacian.  Applying (1.6)
at the root and all children gives

\[
\boxed{G(f_\pm)=LM-LK\pm LZ_U.}
\tag{1.7}
\]

Also set

\[
\overline I=\frac{I(f_+)+I(f_-)}2,
\qquad
Z_I=\frac{I(f_+)-I(f_-)}2
   =\sum_S|S|q(S)t_S.
\tag{1.8}
\]

For `D_{a,b}=G-aI-bU`, equations (1.6)--(1.8) give the complete exact
decomposition

\[
\boxed{
D_{a,b}(f_\pm)=\mathcal C_{a,b}\pm\mathcal O_{a,b},}
\tag{1.9}
\]

where

\[
\mathcal C_{a,b}=LM-a\overline I-bM+bK-LK,
\tag{1.10}
\]

\[
\mathcal O_{a,b}=LZ_U-aZ_I-bZ_U.
\tag{1.11}
\]

Thus one dimension-free sufficient condition for universal GU is the
following.  Fix `a>=0, 0<=b<1`.  If every Boolean function can be paired with
a Boolean companion on the same cube so that

\[
\boxed{\mathcal C_{a,b}+|\mathcal O_{a,b}|\le0,}
\tag{1.12}
\]

then both signs satisfy `G<=aI+bU`.  Consequently

\[
U(f)\le\frac{a}{1-b}I(f),\qquad
H(f)\le\left(2+\frac{2a}{1-b}\right)I(f).
\tag{1.13}
\]

No fresh-variable, overlap, activation, depth or bias hypothesis occurs in
(1.9)--(1.12).  The universal problem is precisely to pay the sign-odd
quantity (1.11), not another sign-even KL reserve.

## 2. Rare-activation family

The separation between the sign-even posterior and the oriented score is
parametric.  Let `N=2^n`, let `f_n` equal `+1` except at one point where it is
`-1`, and let the companion be the constant `1`.  Write

\[
p_0=(1-2/N)^2.
\]

The squared spectrum of `f_n` is `p_0` at the empty set and `4/N^2` at every
nonempty set.  Therefore

\[
U_n:=U(f_n)
=p_0\log\frac1{p_0}
+\frac4{N^2}\left(n2^{n-1}-n\right).
\tag{2.1}
\]

All nonempty sets have identical exact and upper sign posteriors, so the
posterior KL is supported only at the empty set:

\[
K_n=\frac12\left[
p_0\log\frac{2p_0}{1+p_0}
+\log\frac2{1+p_0}\right].
\tag{2.2}

Fixing any coordinate gives the constant pair on one face and the
`(n-1)`-dimensional pair on the other.  Hence

\[
G(f_n)=n\left(U_n-\frac12U_{n-1}\right),
\qquad
LK_n=n\left(K_n-\frac12K_{n-1}\right).
\tag{2.3}

The oriented and influence projections are

\[
Z_U=\frac{U_n}{2},\qquad
LZ_U=\frac{G(f_n)}2,
\qquad
Z_I=\frac{I(f_n)}2=\frac nN.
\tag{2.4}

Taylor expansion of (2.1)--(2.3) gives

\[
K_n=\frac{2}{\ln2}\frac1{N^2}+O(N^{-3}),
\tag{2.5}
\]

\[
Z_U=\frac{n+2/\ln2}{N}+O\left(\frac n{N^2}\right),
\tag{2.6}
\]

\[
LK_n=-\frac{2n}{\ln2}\frac1{N^2}
+O\left(\frac n{N^3}\right),
\qquad
LZ_U=\frac nN+O\left(\frac{n^2}{N^2}\right).
\tag{2.7}
\]

Consequently

\[
\frac{|Z_U|}{K_n}\sim
\left(1+\frac{n\ln2}{2}\right)N\longrightarrow\infty,
\tag{2.8}
\]

and even the complete root-plus-drift posterior has the wrong scale:

\[
\frac{|LZ_U|}{K_n+|LK_n|}
\sim\frac{\ln2}{2}\frac{n}{n+1}N\longrightarrow\infty.
\tag{2.9}
\]

Therefore no finite coefficient multiplying `K`, or `K+|LK|`, can pay the
actual sign projection uniformly.  This is stronger than the preceding
finite `K=0,P^q>0` obstruction: it exhibits the exact rare-activation scale
separation `N^{-1}` versus `N^{-2}`.

This family does not refute GU.  Indeed `Z_I=n/N` and
`LZ_U/Z_I -> 1`, so a source-influence payment remains at the correct scale.
It refutes only a posterior-only projection mechanism.

## 3. Consequence for the next mechanism

A branchwise martingale made solely from `K`, its restriction drift, or any
sign-symmetric function of the unordered pair `{f_+,f_-}` cannot control the
specified actual sign.  The next reserve must retain the oriented score
`Omega` together with source influence and the terminal companion label.  In
the product ledger this is equivalent to retaining `D(h)` jointly with the
root/child companion rather than replacing it by an unsigned posterior.

The exact decompositions are proved pending independent review.  Universal
GU and full FEI remain open.
