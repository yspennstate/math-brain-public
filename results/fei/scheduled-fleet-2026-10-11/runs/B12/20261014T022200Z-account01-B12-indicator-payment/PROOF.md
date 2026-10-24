# Exact indicator-remainder tensor law and coefficient obstruction

## 1. Definitions

For a nonzero real function `q` on a uniform cube, write

\[
 p=\|q\|_2^2,\qquad
 \mathcal E(q)=\sum_S\widehat q(S)^2
       \log_2\frac1{\widehat q(S)^2},\qquad
 \mathcal I(q)=\sum_S |S|\widehat q(S)^2.
\]

Let `P_q(S)=\widehat q(S)^2/p` and define the support-normalized remainder

\[
 \Phi(q)=\mathcal E(q)-p\log_2\frac1p.
\]

Then, by direct substitution,

\[
 \boxed{\Phi(q)=pH(P_q)},\qquad
 \boxed{\mathcal I(q)=p\,\mathbb E_{P_q}|S|}. \tag{1}
\]

For an indicator `q`, `p=\mathbb E q`.

## 2. Tensor identity

Let `q_j` live on pairwise disjoint coordinate blocks and put
`q=\prod_{j=1}^m q_j`.  Fourier factorization gives

\[
 p=\prod_jp_j,\qquad P_q=\bigotimes_jP_{q_j}.
\]

Entropy and expected set size are additive under this product law, so (1)
gives the exact identities

\[
 \boxed{\frac{\Phi(q)}p=\sum_j\frac{\Phi(q_j)}{p_j}},\qquad
 \boxed{\frac{\mathcal I(q)}p=\sum_j
             \frac{\mathcal I(q_j)}{p_j}}. \tag{2}
\]

Consequently, if `K_j=\Phi(q_j)/\mathcal I(q_j)`, then the tensor ratio is
a weighted average of the `K_j`, with weights
`\mathcal I(q_j)/p_j`.  In particular, a tensor power preserves its seed's
ratio exactly.  Thus no additive support correction disappears under
tensorization: its coefficient is a genuine multiplicative requirement.

## 3. Small exact obstruction: two-bit NAND

In lexicographic integer order on `{0,1}^2`, let

\[
 r=(1,1,1,0).
\]

Its unnormalized Walsh vector is `(3,1,1,-1)`, hence its Fourier-square
masses are

\[
 \frac9{16},\frac1{16},\frac1{16},\frac1{16}.
\]

Thus `p=3/4`, `\mathcal I(r)=1/4`, and the normalized spectral law is
`(3/4,1/12,1/12,1/12)`.  Therefore

\[
 H(P_r)=2-\frac12\log_2 3,
\]

and

\[
 \frac{\Phi(r)}{\mathcal I(r)}
 =6-\frac32\log_2 3
 =3.622556248918266\ldots. \tag{3}
\]

The proposed coefficient-two estimate

\[
 \mathcal E(q)\le2\mathcal I(q)+p\log_2(1/p) \tag{4}
\]

already fails by

\[
 \Phi(r)-2\mathcal I(r)
 =1-\frac38\log_2 3
 =0.405639062229566\ldots>0. \tag{5}
\]

The sign in (5) is exact: it is equivalent to
`\log_2 3<8/3`, hence to `3^3=27<256=2^8`.

For `r_k=r^{\otimes k}`, (2) gives, for every `k>=1`,

\[
 p_k=(3/4)^k,\quad
 \mathcal I(r_k)=p_k\frac{k}{3},\quad
 \Phi(r_k)=p_k k\left(2-\frac12\log_2 3\right), \tag{6}
\]

so equality with the coefficient in (3) persists at arbitrary dimension
and composition depth.

## 4. Stronger five-bit exact seed

The deterministic search found the five-bit indicator `s` with little-endian
truth-table mask `4146264055` and values

\[
\begin{split}
(&1,1,1,0,1,1,1,1,1,1,1,0,1,1,1,1,\\
 &0,1,0,0,0,1,0,0,1,1,1,0,1,1,1,1).
\end{split}
\]

Its integer Walsh coefficients are recorded in `CHECK.out`.  Their squared
magnitudes have multiplicities

\[
 529\ (1\text{ time}),\quad25\ (5),\quad9\ (7),\quad1\ (19).
\]

Parseval and the degree-weighted square sum give exactly

\[
 p_*=\frac{23}{32},\qquad \mathcal I(s)=\frac{23}{64}.
\]

The normalized spectral law therefore has masses

\[
 \frac{529}{736},\quad 5\times\frac{25}{736},\quad
 7\times\frac9{736},\quad19\times\frac1{736}.
\]

Set

\[
 h_*=\log_2 736-
 \frac{529\log_2 529+125\log_2 25+63\log_2 9}{736}.
\]

Since `\mathcal I(s)/p_*=1/2`, the exact required coefficient is

\[
 \boxed{K_*=\frac{\Phi(s)}{\mathcal I(s)}=2h_*
 =3.921809106893846\ldots}. \tag{7}
\]

In particular, (4) fails by

\[
 \frac{23}{64}(K_*-2)
 =0.690650147789976\ldots. \tag{8}
\]

The rigorous lower bound `K_*>3.921` is equivalent, after clearing
denominators and cancelling prime powers, to the exact integer inequality

\[
 \boxed{2^{139817}>23^{20125}5^{15625}3^{7875}}, \tag{9}
\]

which `CHECK.py` verifies using integer arithmetic.

For the growing family `s_k=s^{\otimes k}`, (2) yields

\[
 p_k=(23/32)^k,\quad \mathcal I(s_k)=p_k\frac{k}{2},
 \quad\Phi(s_k)=p_k k h_*,
 \quad\frac{\Phi(s_k)}{\mathcal I(s_k)}=K_* \tag{10}
\]

for every `k`.  This is a parameter-free payment for the complete family,
but it is also a strict lower bound on any universal indicator payment of
the form `\Phi(q)\le K\mathcal I(q)`.

## 5. Genuine Boolean companions

To keep Boolean realizability explicit, set

\[
 f_k=2s_k-1\in\{-1,1\}.
\]

Let `p=p_k`, `c=2p-1`, and
`B=\log_2(32/23)`.  Since nonempty Fourier coefficients of `f_k` are twice
those of `s_k`, direct separation of the empty coefficient gives

\[
 I(f_k)=2pk,
\]

\[
 H(f_k)=c^2\log_2\frac1{c^2}
 +4\left[p k(h_*+B)-p^2\log_2\frac1{p^2}\right]
 -8p(1-p). \tag{11}
\]

Hence

\[
 \lim_{k\to\infty}\frac{H(f_k)}{I(f_k)}
 =2(h_*+B)=4.874685194779820\ldots. \tag{12}
\]

Thus this is a genuine Boolean all-depth control family, not an FEI
counterfamily: its ratio remains bounded.  It certifies only the coefficient
obstruction for the auxiliary indicator remainder.

## 6. Consequence for the B12 route

The preceding signed-ensemble theorem suggested paying agreement and
disagreement indicators separately.  A coefficient-two payment would have
combined with the two-sign ledger and Boolean edge isoperimetry to yield a
constant-four FEI route.  Equations (5)--(10) rule out that shortcut, and
show that any payment of this exact unsigned form must allow
`K>=K_*>3.921`.

This does **not** refute a finite universal `K`, and it does not refute FEI.
Indeed, a universal finite `K` here would itself be a full-FEI-strength
input.  The active B12 task therefore returns to the genuinely signed
near/separated coherent split: it must exploit the companion sign,
activation posterior, or terminal reserve rather than charge each indicator
remainder independently at coefficient two.

