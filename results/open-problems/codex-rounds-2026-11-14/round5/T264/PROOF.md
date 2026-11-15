# A close pair with any fixed number of observations in one hemisphere

Let \(\sigma(t)=\max(t,0)\). For \(d\ge2\), consider networks
\[
 f(x)=\sum_{j=1}^m c_j\sigma(w_j\cdot x),\qquad
 Q(c,w)=\frac12\sum_j(c_j^2+\|w_j\|^2).
\]
There are no biases, linear skips, or output intercepts. Width is unrestricted,
or fixed at any \(m\ge n\), where \(n\) is the number of observations.
An interpolant of minimum parameter norm minimizes \(Q\) subject to the
interpolation constraints. Test inputs are uniform on \(S^{d-1}\), with
normalized surface measure. The regression function is zero, and
\(R(f)=\mathbb E_X f(X)^2\) denotes conditional excess squared risk.

Fix orthonormal \(e_1,e_2\). Write
\[
 a=\cos(\theta/2),\quad b=\sin(\theta/2),\quad s=\sin\theta=2ab,
 \qquad x_1=ae_1+be_2,\quad x_2=ae_1-be_2.
\]
Their labels are \((1,-1)\). Let \(k=n-2\ge1\) further observations be
\((z_i,\tau_i)_{i=1}^k\), with \(z_i\in S^{d-1}\).

## Theorem 1: finitely many additional constraints

Suppose the \(z_i\) are distinct and, for one \(\epsilon\in\{-1,1\}\),
\(\epsilon z_i\cdot e_2>0\) for every \(i\). For bounded labels
\(|\tau_i|\le H<\infty\), every minimum-\(Q\) interpolant satisfies
\[
 \sup_{\|x\|\le1}
 \left|\theta f_\theta(x)+2\epsilon
       \sigma(-\epsilon e_2\cdot x)\right|\longrightarrow0,
 \qquad
 \theta^2R(f_\theta)\longrightarrow\frac2d.                 \tag{1}
\]
These limits are uniform over the labels and over all minimizers. They are
also uniform over each of the compact sets
\[
 \mathcal K_{\delta,\rho}^{\epsilon}
 =\left\{(z_1,\ldots,z_k):
 \epsilon z_i\cdot e_2\ge\delta\ (1\le i\le k),\quad
 \|z_i-z_j\|\ge\rho\ (i\ne j)\right\},                    \tag{2}
\]
where \(\delta,\rho>0\). For \(k=1\) the separation condition is vacuous.
The constants and the small-angle threshold may depend on \(k,d,\delta,\rho,H\).

## Theorem 2: every fixed sample size

Let \(n\ge3\) be arbitrary but fixed. Let the training inputs be iid uniform
on \(S^{d-1}\), and let their labels be iid Rademacher variables independent
of the inputs. Let \(f_n\) be any measurable choice of minimum-\(Q\)
interpolant, and put \(R_n=\mathbb E_X f_n(X)^2\). Then
\[
 \mathbb E[R_n^r]=\infty\qquad\text{for every }r\ge\frac{d-1}{2}. \tag{3}
\]
More precisely, with
\[
 \alpha=\frac{d-1}{2},\qquad
 C_d=\frac{\Gamma(d/2)}{\sqrt\pi\,\Gamma((d-1)/2)},
\]
one has
\[
 \liminf_{t\to\infty}t^\alpha\mathbb P(R_n>t)
 \ge\frac{2^{2-n}C_d}{d-1}\left(\frac2d\right)^\alpha.      \tag{4}
\]
The bound uses only the designated pair of observations 1 and 2. No matching
upper bound or finiteness of lower-order moments is asserted.

In particular, \(\mathbb E R_n=\infty\) for every \(n\ge3\) when
\(d=2\) or \(d=3\). Thus, for this model, the sequence of expected excess
risks has extended-real limit \(+\infty\). This does not imply divergence
in probability of the conditional risks \(R_n\).

## 1. Atomic normalization

For \(w_j\ne0\), put \(u_j=w_j/\|w_j\|\) and
\(\gamma_j=c_j\|w_j\|\). Discard zero units. Homogeneity and the
arithmetic-geometric mean inequality give
\[
 f(x)=\sum_j\gamma_j\sigma(u_j\cdot x),\quad \|u_j\|=1,
 \qquad T:=\sum_j|\gamma_j|\le Q.                          \tag{5}
\]
Conversely, a unit atom with coefficient \(\gamma\) is realized at cost
\(|\gamma|\) by
\(c=\operatorname{sign}(\gamma)\sqrt{|\gamma|}\),
\(w=\sqrt{|\gamma|}u\). Thus a feasible representation with at most \(n\)
atoms is a competitor for either width convention in the theorems.

## 2. The correction lemma

Suppose \(z_1,\ldots,z_k\) are distinct unit vectors with
\(z_i\cdot e_2>0\). The response vectors
\[
 A(u)=\big(\sigma(u\cdot z_1),\ldots,\sigma(u\cdot z_k)\big),
 \qquad \|u\|=1,\quad u\cdot e_1<0,                       \tag{6}
\]
span \(\mathbb R^k\).

To prove this, suppose \(\lambda\in\mathbb R^k\) annihilates all vectors
in (6). Homogeneity extends the identity to the open cone
\(\{u:u\cdot e_1<0\}\). Fix \(i\). The orthogonal projection of
\(-e_1\) onto \(z_i^\perp\) is
\(v=-e_1+(e_1\cdot z_i)z_i\), and
\[
 v\cdot e_1=-1+(e_1\cdot z_i)^2<0.                        \tag{7}
\]
Strictness holds because \(z_i\cdot e_2>0\). Thus the relatively open
halfspace \(\{u\in z_i^\perp:u\cdot e_1<0\}\) is nonempty.

No other \(z_j\) is parallel to \(z_i\): equal directions are excluded,
and antipodal directions cannot both have positive second coordinate.
Consequently \(z_i^\perp\cap z_j^\perp\) is a proper linear subspace of
\(z_i^\perp\). A finite union of proper linear subspaces cannot contain a
nonempty relatively open set. For example, choose for each subspace a nonzero
linear functional vanishing on it; the product of these functionals is a
nonzero polynomial, and cannot vanish on an open set. Choose \(u_0\) in the
halfspace above and outside all these subspaces. Then
\[
 u_0\cdot z_i=0,\quad u_0\cdot e_1<0,\quad
 u_0\cdot z_j\ne0\quad(j\ne i).                           \tag{8}
\]
This argument includes \(d=2\): the perpendicular space is a line and
its intersections with other perpendicular spaces consist only of zero.

For sufficiently small real \(t\), \(u(t)=u_0+t z_i\) remains in the
open cone, so
\[
 0=\sum_j\lambda_j\sigma(u(t)\cdot z_j).
\]
For \(j\ne i\), the sign of \(u(t)\cdot z_j\) is fixed near zero;
the corresponding summand is affine in \(t\). The \(i\)-th summand is
\(\lambda_i\sigma(t)\), since \(\|z_i\|=1\). The difference between
its right and left derivatives is \(\lambda_i\). The identically zero
sum has derivative jump zero. Hence \(\lambda_i=0\). Doing this for every
\(i\) proves the spanning claim.

Select \(k\) such directions \(u_1,\ldots,u_k\) for which the matrix
\[
 M(Z)_{ij}=\sigma(u_j\cdot z_i)                            \tag{9}
\]
is invertible. Let
\(\eta=\min_j(-u_j\cdot e_1)>0\). If
\(0<\theta\le\min(1,\eta)\), then \(a\ge3/4\) and
\(b\le\theta/2\le\eta/2\), so
\[
 u_j\cdot x_\ell\le-a\eta+b\le-\eta/4<0
 \quad(\ell=1,2).                                        \tag{10}
\]
All selected correction atoms vanish at both pair observations.

For later uniformity, (9) remains invertible in a neighborhood of \(Z\),
by continuity of its determinant. Its inverse entries are continuous there,
so after shrinking this neighborhood one has a finite bound on
\[
 B(M):=\sum_{i,j}|(M^{-1})_{ji}|.                          \tag{11}
\]
The directions and their strictly positive \(\eta\) are unchanged.
Every nonempty compact set \(\mathcal K_{\delta,\rho}^{+}\) has a finite
cover by such neighborhoods. Choose the minimum of their \(\eta\)'s
and the maximum of their inverse-entry bounds. Both are finite, and the
minimum is positive. For each configuration use any member of the cover
containing it. This proves uniform constants on (2).

Here is a concrete construction on a full-measure subset. Write
\(p_i=z_i\cdot e_1\), \(q_i=z_i\cdot e_2>0\), and suppose the ratios
\(r_i=p_i/q_i\) are distinct. Reorder the observations so
\(r_1<\cdots<r_k\). For \(j<k\), choose
\(t_j=(r_j+r_{j+1})/2\), and choose \(t_k=r_k+1\). Take
\[
 u_j=\frac{-e_1+t_j e_2}{\sqrt{1+t_j^2}}.
\]
Then
\[
 M_{ij}=\frac{q_i(t_j-r_i)_+}{\sqrt{1+t_j^2}}.              \tag{12}
\]
This is upper triangular with positive diagonal, hence invertible. For iid
uniform points, a ratio equals any given real number only on a spherical
hyperplane of surface measure zero. Thus distinct ratios hold almost surely.
The general argument above also covers ratio ties, which are possible for
distinct points when \(d\ge3\).

## 3. A competitor using at most n units

First assume all \(q_i=z_i\cdot e_2\ge\delta>0\). Let
\(p_i=z_i\cdot e_1\), \(v=be_1-ae_2\), and set
\[
 F_0(x)=\frac1a\sigma(e_1\cdot x)
        -\frac1{ab}\sigma(v\cdot x).                     \tag{13}
\]
The two atoms have pair response vectors \((a,a)\) and \((0,s)\).
Therefore \(F_0(x_1)=1\), \(F_0(x_2)=-1\).
For \(0<\theta\le\delta/2\),
\[
 aq_i-bp_i\ge a\delta-b\ge\delta/2>0,
\]
so the second atom in (13) vanishes at every \(z_i\) and
\(F_0(z_i)=\sigma(p_i)/a\).

Use the correction directions from Section 2 and put
\[
 h_i=\tau_i-\sigma(p_i)/a,\quad c=M^{-1}h,\qquad
 F(x)=F_0(x)+\sum_{j=1}^k c_j\sigma(u_j\cdot x).           \tag{14}
\]
Equations (9), (10) prove every interpolation constraint. Since \(1/a\le2\),
\(|h_i|\le H+2\), and (11) gives
\[
 \sum_j|c_j|\le B(M)(H+2).
\]
Balancing yields a network with \(k+2=n\) units and cost
\[
 Q(F)\le\frac1a+\frac1{ab}+B(M)(H+2)
       \le\frac2s+K,\qquad K=2+B(M)(H+2).                 \tag{15}
\]
On each compact set (2), \(K\) and the permissible small-angle threshold
can be chosen uniformly by the finite-cover argument. For a single fixed
configuration, take \(\delta=\min_i q_i\); the same construction applies.

Minimum-\(Q\) interpolants therefore exist in fixed width \(m\ge n\)
for these small angles: the feasible set is nonempty, interpolation is closed,
and bounded parameter sublevels are compact. In unrestricted width,
let \(A(u)\in\mathbb R^n\) collect all training responses and let
\(C=\operatorname{conv}\{\pm A(u):\|u\|=1\}\).
Any convex combination in \(\mathbb R^n\) can be reduced to at most
\(n+1\) terms: if there are more, affine dependence allows a change of
coefficients preserving their sum and represented point until one coefficient
is zero. Iterating gives the claim. Thus \(C\) is compact, as a continuous
image of the compact set of \(n+1\) atoms and simplex coefficients.
The least \(T\) with the label vector in \(TC\) is attained: use a feasible
upper bound on \(T\), compactness, and the lower bound \(T\ge1\) from the
first label and the fact that every response is at most one in magnitude.
An attained representation is finite and can be balanced, proving existence
also in unrestricted width. This existence argument need not identify the
minimum width. Every minimum in either convention satisfies (15).

## 4. Localization, with the cost constant left arbitrary

Consider any interpolant with \(Q\le2/s+K\), not necessarily a minimizer.
Use (5), and put \(t_j=\operatorname{sign}(\gamma_j)\). For a unit \(u\),
define
\[
 g(u)=\frac{\sigma(u\cdot x_1)-\sigma(u\cdot x_2)}s.
\]
If \(q=u\cdot e_2\ge0\), ReLU monotonicity and its Lipschitz constant one
give \(0\le g(u)\le q/a\); if \(q\le0\), they give
\(q/a\le g(u)\le0\). For \(t\in\{-1,1\}\), if \(tq\ge0\), then
\[
 \|u-te_2\|^2=2(1-tq)\le2(1-atg(u))\le4(1-atg(u)).
\]
The last quantity is nonnegative since \(atg(u)\le tq\le1\).
If \(tq<0\), then \(tg(u)\le0\), and
\(\|u-te_2\|^2\le4\le4(1-atg(u))\). Hence always
\[
 \|u-te_2\|^2\le4(1-atg(u)).                              \tag{16}
\]

Write
\[
 M_\theta=\theta\sum_j|\gamma_j|,
 \quad A_\theta=\theta\sum_{\gamma_j>0}\gamma_j,
 \quad B_\theta=\theta\sum_{\gamma_j<0}|\gamma_j|.
\]
Pair interpolation gives \(\sum_j\gamma_jg(u_j)=2/s\). Multiplying
(16) by \(\theta|\gamma_j|\) and summing yields
\[
 \sum_j\theta|\gamma_j|\|u_j-t_je_2\|^2
 \le4(M_\theta-2a\theta/s)=4(M_\theta-\theta/b).            \tag{17}
\]
In particular, with \(U_\theta=2\theta/s+K\theta\),
\[
 2\le\theta/b\le M_\theta=A_\theta+B_\theta\le U_\theta.
\]
Let
\[
 G_\theta(x)=A_\theta\sigma(e_2\cdot x)
             -B_\theta\sigma(-e_2\cdot x),\qquad
 E_\theta=2\sqrt{U_\theta(U_\theta-\theta/b)}.
\]
The Lipschitz bound and Cauchy--Schwarz, followed by (17), give
\[
 \|\theta f-G_\theta\|_{\infty,\{\|x\|\le1\}}
 \le2\sqrt{M_\theta(M_\theta-\theta/b)}\le E_\theta.        \tag{18}
\]
The product increases for \(M_\theta\ge\theta/b\). Furthermore
\[
 U_\theta-\theta/b
 =K\theta+\frac\theta b\frac{1-a}a=O_K(\theta),            \tag{19}
\]
so \(E_\theta=O_K(\sqrt\theta)\).

At any one of the extra observations with \(q_i\ge\delta\), (18) implies
\[
 A_\theta\delta\le A_\theta q_i
 \le\theta H+E_\theta.
\]
Since \(B_\theta=M_\theta-A_\theta\) and the two hemispherical ReLUs have
disjoint positive supports, the uniform error from the asserted limit is at most
\[
 \begin{split}
 \|\theta f+2\sigma(-e_2\cdot x)\|_\infty
 &\le E_\theta+A_\theta+M_\theta-2\\
 &\le (1+\delta^{-1})E_\theta+\theta H/\delta+U_\theta-2
 =:\xi_\theta\longrightarrow0.                           \tag{20}
 \end{split}
\]
Uniform \(K,\delta\) give uniform convergence. For a negative hemisphere,
replace \(e_2\) by \(-e_2\), exchange the pair samples, and replace \(f\)
and all labels by their negatives. This preserves the objective and reduces
to the positive case. It gives exactly the sign in (1).

Reflection symmetry and \(\mathbb E X_2^2=1/d\) give
\(\mathbb E\sigma(-X_2)^2=1/(2d)\). Consequently the squared norm of
the limiting function is \(2/d\). Explicitly (20) implies
\[
 (\max\{0,\sqrt{2/d}-\xi_\theta\})^2
 \le\theta^2R(f)\le(\sqrt{2/d}+\xi_\theta)^2,              \tag{21}
\]
proving Theorem 1. Independently, the limiting function in the positive case
is \(X_2-|X_2|\); its odd and even parts are orthogonal and each has squared
norm \(1/d\). This gives the same coefficient.

## 5. Random inputs and all fixed n

Almost surely, the \(n\) random inputs are pairwise nonparallel. On such a
configuration their unrestricted atomic response vectors span \(\mathbb R^n\).
Indeed, a linear relation among all responses extends homogeneously to all
weight vectors. For each input choose a perpendicular vector that is
perpendicular to none of the others, and follow a line crossing its hyperplane.
Exactly as in (8), the derivative jump is the corresponding relation
coefficient, which must be zero. Thus \(n\) atoms can interpolate arbitrary
labels. Compact parameter sublevels give a fixed-width minimum for \(m\ge n\);
the compact convex-body argument in Section 3 gives an unrestricted-width
minimum. Every finite parameter vector has finite conditional spherical risk.

For the designated pair, outside a null event, define
\[
 \theta=\arccos(X_1\cdot X_2),\quad
 e_1=\frac{X_1+X_2}{\|X_1+X_2\|},\quad
 e_2=\frac{X_1-X_2}{\|X_1-X_2\|}.
\]
The remaining \(k=n-2\) inputs, conditional on the pair, are still iid uniform.
By rotation invariance, the probability \(p_{\delta,\rho}\) that they lie in
\(\mathcal K_{\delta,\rho}^{+}\cup\mathcal K_{\delta,\rho}^{-}\) is independent
of the pair, including its angle. As \(\delta,\rho\) decrease to zero these
events increase, apart from null equatorial or coincident configurations, to
the event that all remaining points have the same sign of their second
coordinate. Each sign is an independent fair sign, so
\[
 p_{\delta,\rho}\longrightarrow 2(1/2)^k=2^{3-n}.           \tag{22}
\]
For example one may let \(\delta=\rho=1/j\) and send the integer \(j\) to
infinity. In particular some \(p_{\delta,\rho}>0\).

Opposite labels at the designated pair have probability \(1/2\), independently
of inputs. If their orientation is \((-1,1)\), negate the function and all
labels; optimality and risk are unchanged. All extra labels then remain bounded
by \(H=1\). The uniformity over all minimizers in Theorem 1 means that no
rotation-equivariant or otherwise specific selection rule is needed.

The pair angle has density
\[
 C_d\sin^{d-2}\theta\quad (0<\theta<\pi).                  \tag{23}
\]
Spherical polar coordinates give the sine power, and its integral is
\(\sqrt\pi\Gamma((d-1)/2)/\Gamma(d/2)\), by symmetry and the beta integral.
For \(d=2\) this is the uniform density \(1/\pi\).

Fix \(\delta,\rho\) with positive event probability and
\(0<\zeta<2/d\). By (21) and compact-set uniformity there exists
\(\theta_0>0\) such that, on this event with opposite pair labels,
\[
 R_n\ge(2/d-\zeta)\theta^{-2}\quad(0<\theta<\theta_0).      \tag{24}
\]
All constants are uniform in the orientation of the frame: rotate the
coordinate-free construction, which preserves every cost and norm bound.
For sufficiently large \(t\), angles strictly below
\(\sqrt{(2/d-\zeta)/t}\) therefore imply \(R_n>t\), and
\[
 \mathbb P(R_n>t)\ge\frac12 p_{\delta,\rho}C_d
 \int_0^{\sqrt{(2/d-\zeta)/t}}\sin^{d-2}\theta\,d\theta.
\]
The integral is asymptotic to
\((2/d-\zeta)^\alpha t^{-\alpha}/(d-1)\). Take the lower limit as
\(t\to\infty\), then let \(\zeta\downarrow0\) and
\(\delta=\rho=1/j\downarrow0\). Equation (22) proves (4).
There is no exchange of the \(n\to\infty\) limit with these limits;
\(n\) has been fixed throughout.

For a separate moment proof, (24) gives, for any \(r>0\),
\[
 \mathbb E R_n^r\ge\frac12 p_{\delta,\rho}C_d(2/d-\zeta)^r
 \int_0^{\theta_0}\theta^{-2r}\sin^{d-2}\theta\,d\theta.
\]
The integrand is asymptotic to \(\theta^{d-2-2r}\), whose integral diverges
when \(d-2-2r\le-1\), equivalently \(r\ge(d-1)/2\). Equality gives a
logarithmic divergence. This proves (3). Independently, (4) implies the same
threshold by the tail identity
\(\mathbb E R_n^r=r\int_0^\infty t^{r-1}\mathbb P(R_n>t)\,dt\),
which follows from Tonelli's theorem applied to
\(R_n^r=\int_0^{R_n}rt^{r-1}\,dt\).

For \(d=2,3\), set \(r=1\). Every term \(\mathbb E R_n\), \(n\ge3\),
is infinite. Its extended-real large-sample limit is therefore infinite.
This statement concerns expectations only; rare events with decreasing
probability can keep every expectation infinite without forcing a typical
sample's risk to grow.

## 6. Checks of the hypotheses and scope

The same-hemisphere condition is essential for the sharp competitor premise
used here. If one extra point has \(z\cdot e_2\ge\delta\) and another has
\(z'\cdot e_2\le-\delta\), and both responses stay bounded, there cannot
be a family of interpolants with \(Q\le2/s+K\) for fixed \(K\).
Equations (18)--(19) would force \(A_\theta+B_\theta\to2\).
The positive response forces \(A_\theta\to0\), and the negative response
forces \(B_\theta\to0\), a contradiction. This does not rule out costs
with a different leading coefficient or determine their risks.

Distinctness of the additional points cannot be dropped for arbitrary labels:
two equal points with different labels have no interpolant. The uniform
separation in (2) prevents the correction matrices from degenerating as points
collide. Formula (12) alone does not cover equal projected ratios; the
derivative-jump proof does. In \(d=2\), all steps use one-dimensional
perpendicular spaces and remain valid.

For \(n=3\), (4) reduces to
\(C_d(2/d)^\alpha/[2(d-1)]\), exactly the preceding random-triple bound.
For \(d=2\) its value is \(2^{2-n}/\pi\); for \(d=3\) it is
\(2^{2-n}/6\). These follow directly from \(C_2=1/\pi\),
\(C_3=1/2\) and provide checks on both the label and hemisphere factors.

The results concern homogeneous two-layer minimum-parameter-norm regression
with the stated width allowance and iid spherical inputs. They do not identify
GD's selected interpolant, cover penalized biases or free skips, prove
finiteness of moments below (3), or classify convergence in probability for
any fixed dimension. The hemisphere event has probability \(2^{3-n}\);
the construction supplies no uniform-in-\(n\) lower bound on typical risk.
For \(d\ge4\), the mean-risk question is not settled by (3).
