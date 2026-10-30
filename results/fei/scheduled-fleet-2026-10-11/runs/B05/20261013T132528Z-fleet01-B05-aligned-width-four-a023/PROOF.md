# Aligned finite-width shielding and the exact width obstruction

All vector spaces are over \(\mathbb F_2\), all logarithms are base two, and
\(U\) is the campaign upper-set functional in the physical Fourier basis.

## 1. Exact fiber decomposition

Let \(M_0\in\mathbb F_2^{s\times r}\) have full column rank, let
\(D:\mathbb F_2^r\times\mathbb F_2^t\to\{-1,1\}\) be arbitrary, and put

\[
 P(x,u,z)=(-1)^{x^TM_0u+a\cdot x+b\cdot u+c\cdot z+d}D(u,z).
 \tag{1}
\]

Thus the physical \(z\)-coordinates span the kernel of the bilinear shield;
this coordinate alignment is a hypothesis, not a change of variables.  Write
\(D_u(z)=(-1)^{c\cdot z}D(u,z)\).

For physical Fourier frequencies \((\alpha,\gamma,\delta)\), summation over
\(x\) makes the coefficient vanish unless
\(M_0u+a=\alpha\).  For every admissible \(\alpha\) there is one such \(u\),
and then

\[
 \widehat P(\alpha,\gamma,\delta)
 =2^{-r}(-1)^{b\cdot u+d+\gamma\cdot u}\widehat{D_u}(\delta).
 \tag{2}
\]

Consequently the squared Fourier law is the following exact mixture: choose
\(u\) and \(\gamma\) independently and uniformly from \(\mathbb F_2^r\),
then choose \(\delta\) from the squared Fourier law of \(D_u\).  Hence

\[
 \boxed{H(P)=2r+2^{-r}\sum_u H(D_u).}                 \tag{3}
\]

Every nonzero row of \(M_0\) gives an \(x\)-coordinate of influence \(1/2\),
and full column rank forces at least \(r\) such rows.  Each \(u_j\) also has
influence \(1/2\): after flipping \(u_j\), the nonzero column
\(M_0e_j\) makes the phase derivative balanced in \(x\), independently of
the ratio of the two \(D\)-values.  Finally, a \(z\)-coordinate sees only the
corresponding derivative of \(D_u\).  Therefore

\[
 \boxed{I(P)\ge r+2^{-r}\sum_u I(D_u).}              \tag{4}
\]

The inequality can be strict only because there may be more than \(r\)
nonzero physical rows.

## 2. Exact fixed-width constant

For \(t\ge0\), define the finite-dimensional FEI constant

\[
 C_t=\max\left\{\frac{H(g)}{I(g)}:
 g:\mathbb F_2^t\to\{-1,1\},\ I(g)>0\right\},
 \qquad C_0:=0,
 \tag{5}
\]

and \(K_t=\max\{2,C_t\}\).  Dummy coordinates show that \(C_t\) is
nondecreasing.  Equations (3)--(4) give

\[
 H(P)\le2r+C_t\,2^{-r}\sum_u I(D_u)
       \le K_t I(P).                                  \tag{6}
\]

Since \(0\le U(P)\le H(P)\), also

\[
 \boxed{U(P)\le K_t I(P).}                            \tag{7}
\]

This proves a dimension-, bias-, address-, overlap- and depth-independent
bound for every fixed width.  It does not hide the width dependence: the
best constant furnished by this mechanism is exactly the ordinary
\(t\)-bit FEI constant.

## 3. Complete adaptive-tree payment

Let \(h\) be an arbitrary Boolean function on a disjoint physical block and
let \(\mathcal T\) be any finite deterministic adaptive/pruned restriction
tree querying only variables of \(P\).  A physical coordinate may occur at
incomparable nodes but is not queried twice on one path.  If \(w_\ell\) is
the uniform-cube probability of leaf \(\ell\), signed node charges telescope:

\[
 \sum_{v\in\mathcal T^\circ}w_v
 \left(U(P_vh)-\frac{U(P_{v,0}h)+U(P_{v,1}h)}2\right)
 =U(Ph)-\sum_\ell w_\ell U(P_\ell h).                 \tag{8}
\]

Disjoint tensor additivity gives \(U(P_vh)=U(P_v)+U(h)\), so \(U(h)\)
cancels exactly once at the terminal boundary.  Nonnegativity of leaf
\(U\), followed by (7), yields

\[
 \boxed{
 U(Ph)-\sum_\ell w_\ell U(P_\ell h)
 \le U(P)\le K_t I(P).}                              \tag{9}
\]

No individual node charge is asserted nonnegative.  The payment is the
complete signed telescope, so changing coherent fibers at descendants do not
duplicate the root reservoir.  All dyadic rare leaf probabilities arising
from physical uniform restrictions are included.

## 4. Rigorous constants through width four

The accompanying checker exhausts every Boolean truth table modulo global
output sign in dimensions \(1,2,3,4\).  Walsh numerators and influences are
integers.  Entropy ratios are enclosed using binary range reduction and the
positive series

\[
 \log q=2\sum_{j=0}^{N-1}\frac{z^{2j+1}}{2j+1}+R_N,
 \quad z=\frac{q-1}{q+1},\qquad
 0\le R_N\le
 \frac{2z^{2N+1}}{(2N+1)(1-z^2)}.                   \tag{10}
\]

It uses \(N=48\) and all quotient corners when dividing by the interval for
\(\log2\).  The resulting rigorous maxima are

\[
 C_1=0,\qquad C_2=2,
\]

\[
 C_3=\frac73+\frac34\log_2\frac{16}{9}
     =2.955889582251598\ldots,                        \tag{11}
\]

\[
 C_4=\frac{45}{16}+\frac{49}{32}\log_2\frac{64}{49}
     =3.402475551198587\ldots.                        \tag{12}
\]

For \(t=2,3,4\), the maximizing squared spectrum is that of a one-point
defect.  In dimensions three and four it has respectively the mass profiles

\[
 (9/16,1/16,\ldots,1/16),\qquad
 (49/64,1/64,\ldots,1/64),
\]

and influences \(3/4\) and \(1/2\).  Thus (9) has constants

\[
 K_t=2\quad(t\le2),\qquad K_3=C_3,qquad K_4=C_4.     \tag{13}
\]

The checker finds 47 distinct nonconstant spectrum/influence profiles in
dimension four.  The largest nonmaximal upper endpoint is \(C_3\), separated
from the lower endpoint of \(C_4\) by more than \(0.4465\).  It also directly
reconstructs 65,810 aligned shields with \(r+t\le4\), verifying (2) and (4)
from physical truth tables.

## 5. Why removing width is exactly the universal gap

The appearance of \(C_t\) is not merely a weakness of the estimate.  Fix
\(r=1\) and let \(q(x,u)=(-1)^{xu}\).  For an arbitrary Boolean \(g\), the
aligned shield \(qg\) is in (1), and disjoint tensor identities give

\[
 H(qg)=2+H(g),\qquad I(qg)=1+I(g).                    \tag{14}
\]

Suppose a constant \(C\), independent of the kernel width, bounded the
entropy of all such shields by their influence.  Apply it to
\(q\,g^{\otimes N}\):

\[
 2+NH(g)\le C(1+NI(g)).                               \tag{15}
\]

Divide by \(N\) and let \(N\to\infty\).  Then
\(H(g)\le CI(g)\) for every Boolean \(g\).  Thus a width-uniform extension
already proves full FEI.  Likewise, a width-uniform complete-tree bound that
fully restricts the kernel block would give a universal \(U\)-payment, which
combined with the campaign inequality \(H\le2I+2U\) would prove FEI.

Therefore the exact unpaid step is not another fixed-width enumeration.  It
is a dimension-independent mechanism controlling the fiber FEI/upper-set
packet itself, equivalently the current universal conjecture.  The useful
next attack must exploit interaction between changing fibers and the shield
that is absent from the disjoint tensor embedding (14), or add a genuinely
new retained credit that survives that embedding.

