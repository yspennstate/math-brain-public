# Full-star point-defect GU' theorem

All Boolean variables below are written in \(\{0,1\}\), with Walsh characters
\(\chi_S(x)=(-1)^{\sum_{j\in S}x_j}\).  Put
\[
 d_n(x)=1-2\mathbf 1_{\{x=0\}},\qquad
 F_n(z,x)=(-1)^{z(x_1+\cdots+x_n)}d_n(x).
\]
For a Boolean function \(f\), write \(p_S=\widehat f(S)^2\),
\(\pi(S)=\sum_{T\supseteq S}p_T\),
\[
 U(f)=\sum_Sp_S\log_2\frac{\pi(S)}{p_S},\qquad
 G(f)=\sum_i\left(U(f)-\mathbb E_bU(f\mid x_i=b)\right).
\]

## Theorem

Let \(\mathcal C_*\) be the smallest class containing, for every \(n\ge1\),

1. \(F_n\), \(d_n\), and \(\chi_{[n]}d_n\);
2. every affine-quadratic phase \((-1)^{Q(x)}\);
3. every product \(q(y)g(x)\) on disjoint variable blocks, where \(q\) is
   an affine-quadratic phase and \(g\) is one of the functions in items 1--2;

and closed under restrictions and global sign.  Then for every
\(f\in\mathcal C_*\),
\[
                         G(f)\le 8I(f).                 \tag{1}
\]
Consequently restriction induction gives \(U(f)\le8I(f)\), and the standard
upper-set entropy inequality \(H(f)\le2I(f)+2U(f)\) gives
\[
                         H(f)\le18I(f).                \tag{2}
\]
The constants are independent of \(n\), the rank of the disjoint quadratic
factor, and the total dimension.

This is a genuine non-disjoint extension of the earlier quadratic-seed
transfer: inside \(F_n\), the point defect and the quadratic star share all
\(n\) data variables and the selector \(z\) is not a fresh tensor factor.

## 1. Exact spectrum and physical influences of \(F_n\)

Put \(\delta=2^{-n}\).  The defect has
\[
 \widehat d_n(\varnothing)=1-2\delta,\qquad
 \widehat d_n(S)=-2\delta\quad(S\ne\varnothing).
\]
Averaging first in \(z\) gives
\[
 \widehat F_n(a,S)=\frac12\left(
   \widehat d_n(S)+(-1)^a\widehat d_n(S\triangle[n])
 \right).
\]
Hence the nonzero squared coefficients are exactly
\[
 \frac14,\frac14,
 \alpha_n,\alpha_n,
 \underbrace{\varepsilon_n,\ldots,\varepsilon_n}_{2^n-2},
 \qquad
 \alpha_n=(\tfrac12-2\delta)^2,quad
 \varepsilon_n=4\delta^2.                              \tag{3}
\]

The selector \(z\) is pivotal exactly when the parity of \(x\) is odd, so
\(\operatorname{Inf}_z(F_n)=1/2\).  For a data coordinate \(x_j\), the
quadratic star is pivotal on the \(z=1\) slice.  On the unique undirected edge
\(0\leftrightarrow e_j\), however, the defect changes sign: it creates a
pivotal edge on the \(z=0\) slice and cancels the star on the \(z=1\) slice.
Thus, with full physical-input accounting,
\[
 \operatorname{Inf}_{x_j}(F_n)
 =\tfrac12(2^{1-n})+\tfrac12(1-2^{1-n})=\tfrac12,
 \qquad I(F_n)=\frac{n+1}{2}.                           \tag{4}
\]

Since \(U\le H\), (3) yields a uniform crude bound sufficient for GU'.  On
\([0,1/4]\), \(x\log_2(1/x)\le1/2\), so the two \(\alpha_n\) atoms contribute
at most 1.  The two \(1/4\) atoms contribute 1.  The dust contributes
\[
 (2^n-2)4\delta^2(2n-2)\le \frac{8(n-1)}{2^n}\le2.
\]
Therefore \(U(F_n)\le H(F_n)\le4\).  Every restriction loss is at most the
parent \(U\), because child \(U\ge0\).  With \(n+1\) coordinates,
\[
 G(F_n)\le(n+1)U(F_n)\le4(n+1)=8I(F_n).                \tag{5}
\]

## 2. Boundary families

For \(d_n\), (3) without the star gives the exact upper-set functional
\[
 U_n=(1-2\delta)^2\log_2\frac1{(1-2\delta)^2}
       +4\delta^2n(2^{n-1}-1)=:L_n+T_n.                \tag{6}
\]
Each coordinate restriction has one child \(d_{n-1}\) and one constant child,
while each coordinate influence is \(2\delta\).  Hence
\[
 G(d_n)=n(U_n-	frac12U_{n-1}),\qquad I(d_n)=2n\delta. \tag{7}
\]
For \(n\ge2\),
\[
 T_n-	frac12T_{n-1}=2\delta+(4n-8)\delta^2\le3\delta,
\]
and
\[
 L_n\le\frac{1-(1-2\delta)^2}{\ln2}\le\frac{4\delta}{\ln2}.
\]
Dropping the nonpositive term \(-L_{n-1}/2\) proves
\(G(d_n)<9n\delta<8I(d_n)\).  The case \(n=1\) is immediate.

For \(\chi_{[n]}d_n\), the spectral probabilities are merely permuted, so
\[
 H\le\frac1{e\ln2}+\frac{8(n-1)}{2^n}<3.              \tag{8}
\]
Every coordinate has influence \(1-2\delta\).  For \(n\ge2\),
\(I\ge n/2\), whence
\[
 G\le nU\le nH<3n\le6I<8I.                            \tag{9}
\]
For \(n=1\) this function is constant.

## 3. Restriction closure

The closure is explicit:

- \(F_n\mid z=0=d_n\) and \(F_n\mid z=1=\chi_{[n]}d_n\);
- \(F_n\mid x_j=0=F_{n-1}\);
- \(F_n\mid x_j=1=(-1)^{z(1+\sum_{k\ne j}x_k)}\), an affine-quadratic phase;
- restricting either defect boundary stays in the same boundary list, up to an
  affine character or a constant;
- restricting an affine-quadratic phase again gives an affine-quadratic phase.

The source theorem `B01_ALL_QUADRATIC_GU_v1` gives \(G(q)\le3I(q)\) for every
affine-quadratic phase.  Equations (5), (7), and (9) therefore prove (1) on
the base closure.

For disjoint products, Fourier probabilities and upper-set masses factor.
Consequently
\[
 U(qg)=U(q)+U(g),\quad G(qg)=G(q)+G(g),\quad I(qg)=I(q)+I(g).
\]
Thus multiplying by an arbitrary disjoint affine-quadratic phase preserves
the constant \(\max\{3,8\}=8\).  This is precisely the previously proved
quadratic-seed transfer, now applied to a base class with genuine internal
quadratic/defect overlap.

## 4. Restriction induction and exact scope

Suppose every proper restriction in this class satisfies \(U\le8I\).  Since
\(G(f)\le8I(f)\), summing the restriction inequalities over all \(m\)
coordinates gives
\[
 mU(f)\le\sum_i\mathbb E_bU(f\mid x_i=b)+8I(f)
       \le8(m-1)I(f)+8I(f)=8mI(f).
\]
The base case is constant.  Hence \(U\le8I\), proving (2).

This theorem does **not** prove universal GU' or full FEI.  It covers one
expanding restriction-closed shared-variable family.  Its crude proof spends
one full parent \(U(F_n)\) at every coordinate; this works only because (3)
keeps \(U(F_n)=O(1)\) while \(I(F_n)=\Theta(n)\).  The unpaid universal step
is a dimension-free control of the aggregate upper-set asymmetry mismatch
when coherent cores change through an arbitrary hierarchy and neither bounded
parent \(U\) nor linear total influence is available a priori.
