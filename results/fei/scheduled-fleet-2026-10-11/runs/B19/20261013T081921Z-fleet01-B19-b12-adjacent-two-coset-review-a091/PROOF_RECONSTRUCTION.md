# Independent reconstruction and scope separation

All logarithms in this review are natural.  Let
\(A=a+V\) and \(B=b+W\) be nonempty disjoint affine cosets in
\(G=\mathbb F_2^m\).  Write
\[
x=|A|/|G|=2^{-k_1},\quad y=|B|/|G|=2^{-k_2},\quad
L=V+W,\quad \ell=\operatorname{codim}L,
\]
and \(r=|L^\perp|=2^\ell\).  Put \(s=\mathbf1_A+\mathbf1_B\).

## 1. Spectral refund

The spectrum of \(\mathbf1_A\) is flat of magnitude \(x\) on
\(V^\perp\); similarly the spectrum of \(\mathbf1_B\) has magnitude \(y\)
on \(W^\perp\).  Their common support is \(L^\perp\).  Disjointness is
equivalent to \(t=b-a+L\ne0\) in \(G/L\).  Hence the relative phase on
\(L^\perp\) is a nontrivial character: exactly half of the common
coefficients have magnitudes \(x+y\), and half have magnitudes \(|x-y|\).

For \(\Phi(u)=u\ln(1/u)\), the normalized Hadamard rotation gives
\[
\frac{\Phi((x+y)^2)+\Phi((x-y)^2)}2
\le \Phi(x^2)+\Phi(y^2).                                 \tag{1}
\]
Indeed, after dividing the squared coordinates by
\(M=x^2+y^2\), binary entropy can increase by at most \(\ln2\); the
unnormalized factor \(\sqrt2\) subtracts exactly \(M\ln2\).  Thus common
spectral support cannot increase raw entropy.  Outside the common support
there is no collision, and therefore
\[
\mathcal E(s)\le2\ln2\,(xk_1+yk_2).                     \tag{2}
\]

## 2. Exact physical collision and rank payment

Let \(m_j\) be the number of coordinate axes outside the direction space of
the \(j\)-th coset.  A coordinate direction joins the two pieces precisely
when \(e_i+L=t\).  If there are \(q\) such coordinates, each contains
\(|V\cap W|\) cross edges, and
\[
I(s)=\frac{x m_1+y m_2}{2}-q xyr.                        \tag{3}
\]

In \(G/V\), the \(q\) joining columns all map to the same nonzero vector in
\(G/L\).  Their span has dimension at most
\(\min(q,k_1-\ell+1)\).  Since all active coordinate columns span \(G/V\),
\[
m_j\ge\max(k_j,q+\ell-1),\qquad j=1,2.                  \tag{4}
\]
Set \(\alpha=k_1-\ell\le\beta=k_2-\ell\).  In the ranges
\(q\le\alpha+1\), \(\alpha+1<q\le\beta+1\), and \(q>\beta+1\), respectively,
the elementary bound \(2^u\ge u+1\) gives
\[
2q\le2^\beta[1+(q-1-\alpha)_+]
      +2^\alpha[1+(q-1-\beta)_+].                       \tag{5}
\]
Since \((xyr)^{-1}x=2^\beta\) and
\((xyr)^{-1}y=2^\alpha\), equations (4)--(5) imply
\[
2qxyr\le x(m_1-k_1)+y(m_2-k_2)+x+y.                    \tag{6}
\]
Together with (3), this is
\[
xk_1+yk_2\le2I(s)+p,\qquad p=x+y.                      \tag{7}
\]

## 3. Local associator

For
\[
d(x,z)=\mathbf1_{\{x=-1\}}s(z),\quad a_0=x+d,\quad F=x+2d,
\]
directly pairing Fourier coefficients in the selector bit gives
\[
\Omega:=\mathcal E(F)-\mathcal E(a_0)-\mathcal E(d)
=\mathcal E(s)+C(p),                                    \tag{8}
\]
where
\[
C(p)=\Phi((1-p)^2)-3\Phi(p^2/4)-\Phi((1-p/2)^2)
     -p(1-p)\ln4.
\]
If \(f(t)=\Phi((1-t)^2)\), then \(f'(t)\le2\), so
\(f(p)-f(p/2)\le p\).  Also
\[
3\Phi(p^2/4)+p(1-p)\ln4
\ge p\ln4(1-p/4)\ge(3/4)p\ln4>p.
\]
Hence \(C(p)\le0\).  Finally tensor differentiation gives
\[
I(d)=\frac12I(s)+\frac p4.                              \tag{9}
\]
Combining (2), (7), (8), and (9) proves, for every such pair,
\[
\boxed{\Omega\le8\ln2\,I(d)}.                          \tag{10}
\]
Two point cosets have \(\mathcal E(s)\sim2pm\ln2\) and
\(I(d)\sim pm/4\), so the coefficient \(8\ln2\) is the sharp supremum.

This establishes the three local B12 claims independently.

## 4. The submitted hierarchy corollary does not follow

The report additionally asserts that, for any adaptive pathwise-nonreusing
restriction hierarchy whose reached sources are restrictions of one source
\(b\),
\[
\sum_v w_v\Omega_v\le8\ln2\,I(b).                       \tag{11}
\]
The local theorem (10) charges the **full** \(I(d_v)\) at every reached node.
A nonreusing restriction tree only makes the influence of newly queried or
otherwise explicitly owned coordinate blocks single-use.  It does not imply
\(\sum_vw_v I(d_v)\le I(b)\).

There is a literal finite counterexample.  In \(\mathbb F_2^4\), take
\(A=\{0\}\) and \(B=\{1,2\}\).  This is a disjoint affine-coset pair and
the local charge is positive:
\[
\Omega=0.507167337318501\ldots,\qquad I(d)=11/64.
\]
Adjoin two free dummy coordinates to both cosets.  Reveal the first dummy at
the root and the second dummy at both depth-one nodes.  This tree is pathwise
coordinate-nonreusing, and every reached restriction is the identical local
source.  The weighted two-level charge is
\[
2\Omega=1.014334674637002\ldots,
\]
whereas the claimed source budget is
\[
8\ln2\,I(b)=\frac{11}{8}\ln2
=0.953077373269924\ldots.
\]
Thus (11), under its stated quantifiers, is false.

A correct hierarchy transfer would require one of the following additional
inputs:

1. a directional strengthening
   \(\Omega_v\le8\ln2\,I_{B_v}(b_v)\) for explicitly owned blocks \(B_v\),
   together with the derivative nonreuse ledger; or
2. an edge-disjoint/cylinder-disjoint ownership hypothesis proving directly
   that the full local influence packets are used at most once.

Neither input appears in the submitted proof.  The local theorem remains
valid and useful; only its hierarchy extension is rejected.
