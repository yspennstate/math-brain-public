# A condition on the kink directions of a margin-stationary score

Let \(\rho(z)=\max\{z,0\}\). Consider finite networks

\[
 f_\theta(x)=\sum_{j=1}^m a_j\rho(w_j^Tx),\qquad
 J(\theta)=\frac12\sum_{j=1}^m(a_j^2+\|w_j\|^2),
 \tag{1}
\]

with both layers trainable and no biases. For a fixed sample
\((X_i,Y_i)\in\mathbb R^d\times\{-1,1\}\), the margin problem is

\[
 \min_\theta J(\theta)\quad\text{subject to}\quad
 Y_i f_\theta(X_i)\ge1\quad(1\le i\le n).
 \tag{2}
\]

Here generalized KKT stationarity permits independent numbers
\(\xi_{ij}\in[0,1]\) at every zero preactivation. At positive and negative
preactivations they are respectively 1 and 0. The equations are

\[
 a_j=\sum_i\lambda_iY_i\rho(w_j^TX_i),\qquad
 w_j=a_j\sum_i\lambda_iY_i\xi_{ij}X_i,
 \tag{3}
\]

where \(\lambda_i\ge0\), together with feasibility and complementary
slackness. Allowing independent derivatives includes any more restrictive
choice of generalized gradients. The obstruction below already rules out
(3) with arbitrary real common coefficients \(c_i=\lambda_iY_i\), without
using their signs or complementary slackness.

## 1. Consequences of per-neuron stationarity

For any real coefficients \(c_i\), put

\[
 D(u)=\sum_i c_i\rho(u^TX_i),\qquad
 P(u)=\sum_{i:u^TX_i>0}c_iX_i.
 \tag{4}
\]

Suppose (3) holds with \(c_i\) in place of \(\lambda_iY_i\).
Taking the inner product of its second equation with \(w_j\), and
using \(\xi_{ij}w_j^TX_i=\rho(w_j^TX_i)\), gives

\[
 \|w_j\|^2=a_j\sum_i c_i\rho(w_j^TX_i)=a_j^2.
 \tag{5}
\]

If either \(a_j\) or \(w_j\) is zero, both are zero: this also follows
directly from (3). Every retained neuron is therefore balanced. With
\(u=w_j/\|w_j\|\) and \(s=\operatorname{sign}(a_j)\), its first equation
gives

\[
 D(u)=s\in\{-1,1\}.
 \tag{6}
\]

In particular, all retained neurons on the same oriented line have
the same output sign. Their normalized coefficients
\(a_j\|w_j\|\) cannot cancel. If \(u^TX_i\ne0\) for every sample,
the second equation gives the further identity

\[
 P(u)=s u.
 \tag{7}
\]

All these statements allow arbitrary additional neurons elsewhere.

Suppose a unit direction \(z\) belongs to the closure of the activation
cell containing such a direction \(u\). This means that whenever
\(z^TX_i\ne0\), its sign agrees with that of \(u^TX_i\). Terms with
\(z^TX_i=0\) vanish in (4), so

\[
 D(z)=P(u)^Tz=s u^Tz.
 \tag{8}
\]

If \(z\ne u,-u\), then \(|u^Tz|<1\), by strictness in the
Cauchy--Schwarz inequality. Equations (6) and (8) imply that no neuron
of this stationary representation can have direction \(z\).
This conclusion does not depend on derivatives chosen at its zero
preactivations.

## 2. Hyperplanes forced by equality of scores

Assume \(d\ge2\). For distinct unoriented unit normals \(u_k\), let

\[
 f(x)=v^Tx+\sum_{k=1}^K\beta_k|u_k^Tx|,
 \qquad \beta_k\ne0.
 \tag{9}
\]

Every finite ReLU representation of this score, with equality on all
of \(\mathbb R^d\), must have aggregated coefficients \(b_k^+,b_k^-\)
on directions \(u_k,-u_k\) satisfying

\[
 b_k^++b_k^-=2\beta_k.
 \tag{10}
\]

To prove this, normalize each nonzero input weight and aggregate its
output coefficient times its original input norm. The contribution
from one normal line is

\[
 b^+\rho(u^Tx)+b^-\rho(-u^Tx)
 =\frac{b^++b^-}{2}|u^Tx|+rac{b^+-b^-}{2}u^Tx.
 \tag{11}
\]

Choose a point of the hyperplane \(u^Tx=0\) outside all other
hyperplanes occurring in either finite representation. Such a point
exists: its intersections with the other hyperplanes are finitely many
proper subspaces of this \((d-1)\)-dimensional space. In a neighborhood
of this point all other terms are linear. The gradient jump across
this hyperplane is \((b^++b^-)u\). For (9) it is \(2\beta_k u_k\)
on a listed hyperplane, and zero on an additional one. Equality of the
scores proves (10), and also proves that extra groups have zero sum.

Thus a nonzero kink forces at least one retained neuron on its normal
line. At a stationary representation, (6) also prevents cancellations
within either orientation, including at a center normal lying on a
sample hyperplane.

## 3. The angular-bisector condition

Let \(u_-,u_0,u_+\) be distinct unit normals, with none equal up to sign.
Suppose all three lines are forced kinks of the score, and the two
edge coefficients \(\beta_-,\beta_+\) have the same nonzero sign.
Assume neither edge normal is orthogonal to a sample. Suppose also
that for each \(\varepsilon\in\{-1,1\}\), the direction
\(\varepsilon u_0\) belongs to the closure of the activation cell of
each \(\varepsilon u_-\) and \(\varepsilon u_+\).

**Lemma 1.** Any finite representation of this score satisfying (3)
necessarily obeys

\[
 \boxed{u_-^Tu_0=u_+^Tu_0.}
 \tag{12}
\]

**Proof.** By (10), a center neuron exists. Choose its orientation
\(-\varepsilon u_0\). If any edge neuron had direction
\(-\varepsilon u_-\) or \(-\varepsilon u_+\), (8) would imply
\(|D(-\varepsilon u_0)|<1\), contradicting (6) for that center neuron.
Consequently all edge neurons must use directions
\(\varepsilon u_-\) and \(\varepsilon u_+\).

Both edge lines have nonzero coefficient, so both orientations just
specified occur. By (8) applied to either edge, a center neuron cannot
have direction \(\varepsilon u_0\). Hence only
\(-\varepsilon u_0\) occurs at the center. This also shows that the
preceding orientation conclusion does not depend on which initial
center neuron was chosen.

Only one orientation occurs at each edge, so (10) says its aggregate
coefficient is \(2\beta_-\) or \(2\beta_+\). By (6), all individual
coefficients in each aggregate have the same sign. Their common sign
is therefore \(s=\operatorname{sign}(\beta_-)=
\operatorname{sign}(\beta_+)\). Applying (8) twice gives

\[
 D(\varepsilon u_0)=s u_-^Tu_0=s u_+^Tu_0.
\]

Since \(s\ne0\), this proves (12). Extra directions, arbitrary
splitting of coefficients, and all allowed center derivatives are
already included in the argument. \(\square\)

## 4. Application to the earlier slope-symmetric tents

Write \(q(r)=e_2-r e_1\) and \(L(r)=\sqrt{1+r^2}\). Suppose
\(U_i=(X_i)_1\ne0\), the slopes \(T_i=(X_i)_2/U_i\) are distinct,
and \(h_i>0\) obey \(h_i\le\Delta_i/3\), where
\(\Delta_i=\min_{j\ne i}|T_i-T_j|\). For \(n=1\) any finite
positive width is permitted. Put

\[
 H_{t,h}(x)=\frac{|q(t-h)^Tx|-2|q(t)^Tx|+|q(t+h)^Tx|}{2h},
 \qquad f_h(x)=v^Tx+\sum_i A_i H_{T_i,h_i}(x).
 \tag{13}
\]

Here \(v\) and the \(A_i\) may be arbitrary. The closed slope intervals
are pairwise disjoint: \(h_i+h_j\le2|T_i-T_j|/3<|T_i-T_j|\).
For any \(A_i\ne0\), its three kink coefficients and normals are

\[
 (\beta_-,\beta_0,\beta_+)=
 \left(\frac{A_iL(t-h)}{2h},-rac{A_iL(t)}h,
                         \frac{A_iL(t+h)}{2h}\right),\quad
 (u_-,u_0,u_+)=
 \left(\frac{q(t-h)}{L(t-h)},\frac{q(t)}{L(t)},
                         \frac{q(t+h)}{L(t+h)}\right),
 \tag{14}
\]

where \(t=T_i,h=h_i\). These lines do not coincide with those of any
other nonzero tent. The edge normals have no zero sample
preactivations. For any sample other than \(i\), no slope lies
between either edge and the center, so its activation sign is
constant there. At sample \(i\), the center preactivation is zero.
The activation-cell closure assumptions of Lemma 1 therefore hold
for both orientations.

**Theorem 2.** If \(A_i\ne0\) and \(T_i\ne0\) for at least one index,
no finite representation of \(f_h\) satisfies generalized KKT
stationarity for (2). The conclusion holds for every width, every
linear baseline, arbitrary extra neuron directions, and all the
independent derivatives allowed in (3). It also holds for every
nonzero scalar multiple of \(f_h\).

**Proof.** Lemma 1 would force (12) for the normals (14). In their
two-dimensional plane, \(u_-+u_+\) and \(u_--u_+\) are nonzero and
orthogonal, because both edge normals have norm one and they are
neither equal nor opposite. Equation (12) makes \(u_0\) orthogonal
to their difference. It follows in this plane that \(u_0\) is parallel
to their sum. Taking the determinant in coordinates \((e_1,e_2)\)
then gives

\[
 0=\det(q(t),u_-+u_+)
   =h\left(\frac1{L(t+h)}-\frac1{L(t-h)}\right).
 \tag{15}
\]

Since \(h>0\), this implies \(L(t+h)=L(t-h)\). Squaring gives
\((t+h)^2=(t-h)^2\), hence \(4th=0\), contrary to \(t\ne0\).
All these vectors lie in the same plane even when \(d>2\).
Multiplication of the score by a nonzero scalar preserves the forced
lines and the equal signs of the two edge coefficients. The same
argument applies. \(\square\)

Only the absence of other sample slopes in each tent interval is
needed for Lemma 1; the one-third-gap rule is a sufficient condition
that also makes all forced lines distinct across tents.

**Corollary 3.** For every finite \(n\ge1,d\ge2\), the round 3
Gaussian-mixture interpolation score almost surely has no finite
representation satisfying (3), nor does any nonzero multiple of it.

**Proof.** The input law is a mixture of nondegenerate Gaussians with
\(\sigma>0\). Its two-dimensional projection has a density. Thus
almost surely all \(U_i\) are nonzero, all \(T_i\) are distinct, and
all \(T_i\) are nonzero. Each statement follows from a finite union
of null events; equality of independent slopes has probability zero
since the ratio law has a density.

The rule uses \(v_n=n^{-1}\sum_jY_jX_j\) and
\(A_i=(Y_i-v_n^TX_i)/|U_i|\). In particular \(A_1\ne0\) almost
surely. For each fixed binary label vector, its numerator is the
polynomial

\[
 Y_1-\frac1n\sum_jY_j X_j^TX_1.
 \tag{16}
\]

It is not the zero polynomial: at all \(X_j=0\) its value is
\(Y_1\ne0\). A nonzero polynomial has a Lebesgue-null zero set.
One elementary proof is induction on the number of variables: outside
the common zero set of its nonzero coefficient polynomials, its
one-variable fibers have finitely many roots; induction and Fubini
then give measure zero. For each fixed label vector the joint law of
the inputs and that label event is absolutely continuous in the inputs,
since it is bounded by the absolutely continuous input law. A finite
union over all label vectors shows (16) is nonzero almost surely.
Theorem 2 applies. \(\square\)

## 5. The angularly symmetric exception can actually be stationary

The condition \(t\ne0\) cannot be discarded for arbitrary baselines.
Here is an exact KKT example for an isolated tent centered at zero.
Set

\[
 h=\frac5{12},\quad A=1,\quad v=(0,24/5),\quad
 f(x)=v^Tx+H_{0,h}(x),
 \tag{17}
\]

and use data

\[
 X_1=(1,0),\ Y_1=1;\qquad
 X_2=(-25/288,5/24),\ Y_2=1;\qquad
 X_3=(25/576,-5/24),\ Y_3=-1.
 \tag{18}
\]

Their slopes are \(0,-12/5,-24/5\). Thus the width in (17) is
less than one third of the nearest center gap, and no other sample
is inside its slope interval. Its three-neuron representation is

\[
 f(x)=\frac{13}5\rho(u_-^Tx)+\frac{13}5\rho(u_+^Tx)
                         -\frac{24}5\rho(-e_2^Tx),\qquad
 u_-=(5/13,12/13),\quad u_+=(-5/13,12/13).
 \tag{19}
\]

Both endpoint vectors have norm one. To check equality with (17),
use \(\rho(z)=(|z|+z)/2\). The absolute coefficients become
\(13/10,13/10,-12/5\), exactly those in (14), while the linear vector
is \((0,24/5)\). At \(X_1\) the tent has value one and the baseline
zero; at \(X_2,X_3\) the tent vanishes and the baseline has values
one and minus one. All margins therefore equal one.

Balance each term \(b\rho(u^Tx)\) of (19) by taking
\(a=\operatorname{sign}(b)\sqrt{|b|}\) and
\(w=\sqrt{|b|}u\). Choose positive multipliers

\[
 (\lambda_1,\lambda_2,\lambda_3)
       =(10/13,288/65,24/5).
 \tag{20}
\]

At the negative center neuron, use derivative \(\xi=13/48\) on
\(X_1\), its sole zero preactivation. All other preactivations are
nonzero. The active signed input sums are

\[
 \begin{aligned}
 P(u_-)&=\lambda_1X_1+\lambda_2X_2
                    =(5/13,12/13)=u_-,\\
 P(u_+)&=\lambda_2X_2=(-5/13,12/13)=u_+,\\
 P(-e_2)&=\lambda_1(13/48)X_1-\lambda_3X_3
                    =(0,1)=(-1)(-e_2).
 \end{aligned}
 \tag{21}
\]

In the last line \(P\) denotes the selected sum including the zero
derivative. Thus the input-weight stationarity equations hold for all
three balanced neurons. Taking the inner product of each line with
its unit direction proves \(D(u)=\operatorname{sign}(b)\); terms at
zero contribute nothing, so the output-weight stationarity equations
hold too. Feasibility, nonnegative multipliers, and complementary
slackness have already been checked. As a separate normalization
check,

\[
 J=13/5+13/5+24/5=10
  =10/13+288/65+24/5=\sum_i\lambda_i.
 \tag{22}
\]

This example has an arbitrary baseline, not the round 3 sample-mean
baseline. It demonstrates that the angular exception in Lemma 1 is
substantive. It does not contradict Corollary 3.

## 6. Scope for the benign-overfitting question

Theorem 2 strengthens the previous displayed-realization obstruction
to an obstruction for the entire score, generically and at every finite
width. For the Gaussian construction it holds almost surely, including
when \(n\ge d\) or \(n/d\) diverges. It places no new restriction on the
intrinsic path norm formula established in round 4.

These are exact finite-parameter KKT statements. They do not show that
a GD trajectory has a finite directional limit satisfying (3), or
exclude limits with diverging width, degenerating neurons, or changes
of score shape. They give no uniform lower bound on distance to
stationarity as widths shrink. They also do not exclude localized
interpolants whose edge normals are angularly symmetric about their
center normals. A GD generalization or impossibility theorem for T265
does not follow from them.
