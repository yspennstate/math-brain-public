# Finite cascade trials are invariant kernel laws

Fix an integer d>=3 and beta>0. Limits in n are along dn even.
All logarithms are natural. Write c_d for the limiting maximum cut
per vertex of the uniform simple d-regular graph.

The external input is Theorem 2.7 and general equation (2.12) of
Amin Coja-Oghlan and Will Perkins,
[*Spin systems on Bethe lattices*, arXiv:1808.03440v1](https://arxiv.org/html/1808.03440v1).
In the scalar antiferromagnetic specialization checked in round 4,
this says that the normalized pressure is the minimum of V below
over laws invariant under the finite cavity row tilts. That theorem
is used as an external result. The inclusion of finite cascade trials
in this invariant class is proved here.

## 1. Normalization and the precise claim

Put t=exp(-beta), a=(1+t)/2 and b=(1-t)/(1+t). For u,v in [-1,1], set

\[
 D(\sigma,u)=a(1-b\sigma u),\qquad Q(u,v)=a(1-buv).
\tag{1}
\]

For a measurable kernel m(s,x) with values in [-1,1], define

\[
 A_m(s;X)=\frac12\sum_{\sigma=\pm1}
                    \prod_{j=1}^d D(\sigma,m(s,X_j)),\qquad
 B_m(s;Y)=Q(m(s,Y_1),m(s,Y_2)).
\tag{2}
\]

All column samples are uniform and independent of the kernel. Products
of finitely many A and B factors define positive row tilts z(s).
Replacing row measure ds by z(s)ds/int z is equivalent to the quantile
reparametrization in round 4. Let D* be the laws on weak kernels invariant
under these operations. Weak kernels identify kernels after
measure-preserving row and column reparametrizations, and then identify
any remaining pairs at cut distance zero.

For pi in D*, the functional and its minimum are

\[
 V(\pi)=\mathbb E\log\int A_m(s;X)\,ds
              -\frac d2\mathbb E\log\int B_m(s;Y)\,ds,
 \qquad \Phi_d(\beta)=\min_{\pi\in D^*}V(\pi).
\tag{3}
\]

The external input, with the strictly subunit weight scaling already
checked in round 4, gives

\[
 p_d(\beta):=\lim_n\frac1n\mathbb E\log
                 \sum_\sigma e^{\beta\operatorname{Cut}(\sigma)}
       =\log2+\frac{\beta d}{2}+\Phi_d(\beta),
 \qquad
 0\le \frac{p_d(\beta)}\beta-c_d\le\frac{\log2}\beta.
\tag{4}
\]

Choose r>=1, parameters 0<zeta_0<...<zeta_{r-1}<1, and a measurable
h:[0,1]^r -> [-1,1]. Let (V_alpha) be the normalized Ruelle cascade
on leaves alpha in N^r, with these parameters. For each nonroot tree
vertex gamma and each input label j, let U_gamma^j be independent
uniform variables, independent of the cascade. Put

\[
 m_\alpha^j=h(U_{\alpha|1}^j,\ldots,U_{\alpha|r}^j),
 \qquad C(u,v)=e^\beta Q(u,v).
\]

Define

\[
 H_{d,\beta}(r,\boldsymbol\zeta,h)=\log2+
  \mathbb E\log\sum_\alpha V_\alpha
      \frac12\sum_{\sigma=\pm1}\prod_{j=1}^d C(m_\alpha^j,\sigma)
 -\frac d2\mathbb E\log\sum_\alpha V_\alpha C(m_\alpha^1,m_\alpha^2),
 \qquad J_d(\beta)=\inf_{r,\boldsymbol\zeta,h}H_{d,\beta}.
\tag{5}
\]

Each expectation can use fresh input labels. Every logarithm is
bounded at fixed beta,d.

**Claim.** Every trial in (5) has an associated law pi_h in D*, and

\[
 H_{d,\beta}(r,\boldsymbol\zeta,h)
       =\log2+\frac{\beta d}{2}+V(\pi_h).
\tag{6}
\]

Consequently

\[
 p_d(\beta)\le J_d(\beta),\qquad
 c_d\le \frac{J_d(\beta)}\beta
       \le \frac{H_{d,\beta}(r,\boldsymbol\zeta,h)}\beta.
\tag{7}
\]

No reverse inequality in the first part of (7) is asserted.

## 2. A marked Poisson calculation

For 0<q<1, let (x_i) be a Poisson point process on (0,infinity) of
intensity q x^(-1-q) dx, listed in decreasing order. Attach independent
marks Z_i with law rho. If f is measurable and 0<l<=f<=u<infinity, put
c=(E f(Z)^q)^(1/q). Then the points

\[
 y_i=x_i f(Z_i)/c
\tag{8}
\]

form a Poisson point process of the same intensity. Indeed, the marked
process has intensity q x^(-1-q) dx rho(dz). Substitution
x=yc/f(z) shows that its image intensity is

\[
 q y^{-1-q}\,dy\int(f(z)/c)^q\,\rho(dz)
          =q y^{-1-q}\,dy.
\]

Counts in disjoint image sets are independent since their preimages
are disjoint sets of the marked Poisson process. Thus the image is
the claimed Poisson process. There are almost surely no ties. Sorting
therefore defines a permutation of the countably many points.

The same statement holds conditionally on any previously exposed
variables: if f depends on them and c is the corresponding conditional
power mean, the conditional distribution of the sorted y process is
constant. It follows that this process is independent of those variables.
The transformed marks themselves need not retain law rho.

## 3. Cascades under a general bounded hierarchical tilt

At each vertex gamma of depth k-1, independently put a Poisson process
(x_gamma,n) of intensity zeta_{k-1} x^(-1-zeta_{k-1}) dx on its
outgoing edges. For a leaf alpha define

\[
 v_\alpha=\prod_{k=1}^r x_{\alpha|k},\qquad
 T=\sum_{\alpha\in\mathbb N^r}v_\alpha,\qquad V_\alpha=v_\alpha/T.
\tag{9}
\]

Here x_{gamma,n} is also denoted by x_{(gamma,n)}. The variables T
are positive and finite almost surely. The following argument records
the needed existence fact. For a Poisson process of exponent q, its
sum S has Laplace transform

\[
 \mathbb E e^{-\lambda S}
 =\exp\{-K_q\lambda^q\},\qquad
 K_q=q\int_0^\infty(1-e^{-u})u^{-1-q}\,du\in(0,\infty).
\tag{10}
\]

The integral converges at both endpoints. The Laplace transform tends
to one as lambda decreases to zero, so S is finite almost surely;
it is positive since the process has points almost surely. For 0<p<q,
the identity

\[
 s^p=\frac{p}{\Gamma(1-p)}
          \int_0^\infty(1-e^{-\lambda s})\lambda^{-1-p}\,d\lambda
\]

follows by substitution and integration by parts. Tonelli and (10)
then give E S^p<infinity: near zero the integrand is O(lambda^(q-p-1)),
and near infinity it is O(lambda^(-p-1)). If the points x_i carry
independent positive subtree sums S_i, their product sum has Laplace
transform exp{-K_q E S_i^q lambda^q}, whenever E S_i^q<infinity.
This follows by the same marked Poisson integral and Tonelli.
Starting at the bottom, the strict inequalities between successive
zeta parameters give exactly the moment needed at the next level.
Induction proves the assertion about T and all subtree sums.

Independently attach to every nonroot vertex gamma a mark Z_gamma
with law rho, all independent. A finite vector of uniforms is an
allowed mark. Let w(z_1,...,z_r) be measurable with 0<l<=w<=u<infinity,
and set W_alpha=w(Z_{alpha|1},...,Z_{alpha|r}). Define functions
w^(r)=w and, for k=r,...,1,

\[
 w^{(k-1)}(z_1,\ldots,z_{k-1})=
 \left[\mathbb E_{Z_k}
       w^{(k)}(z_1,\ldots,z_{k-1},Z_k)^{\zeta_{k-1}}
       \right]^{1/\zeta_{k-1}}.
\tag{11}
\]

All these functions lie in [l,u], and w^(0) is deterministic.

**Cascade tilt lemma.** There is a random tree automorphism theta
(a permutation of the children separately at each vertex) such that
the reweighted masses

\[
 \widetilde V_\alpha=
           \frac{V_\alpha W_\alpha}{\sum_\delta V_\delta W_\delta}
\tag{12}
\]

when indexed as (tilde V_{theta(alpha)}) have the law of (V_alpha),
with the whole hierarchy retained.

To prove it, first work at depth r. Conditional on all earlier marks
and point processes, replace each terminal point by

\[
 x_{\alpha|r}
 \frac{w^{(r)}(Z_{\alpha|1},\ldots,Z_{\alpha|r})}
      {w^{(r-1)}(Z_{\alpha|1},\ldots,Z_{\alpha|r-1})}.
\tag{13}
\]

The marked Poisson calculation shows that, after sorting, these are
independent standard processes at depth r, independent of all earlier
marks and points. The assertion is joint over the countable set of
parents: it holds first for any finite set by conditional independence,
and hence for the whole collection by its finite-dimensional laws.

The only remaining multiplier in each parent subtree is
w^(r-1) evaluated at its ancestral marks. At depth r-1, therefore,
replace its outgoing points by the analogous ratio w^(r-1)/w^(r-2)
and sort. The already standardized descendant processes are independent
of everything used to select this permutation, so reindexing them
preserves their independent standard laws. Repeat this operation at
depths r-2,...,1. At every step the conditional distribution of the
standardized points is constant; it is not necessary to assume that
the transformed marks remain unbiased.

The permutations compose to theta. The new sorted point processes
at all vertices are independent and have the original intensities.
Along any old path the successive multipliers telescope:

\[
 \prod_{k=1}^r y_{\alpha|k}
       =v_{\theta(\alpha)}
              W_{\theta(\alpha)}/w^{(0)}.
\tag{14}
\]

In (14), y denotes the sorted, reindexed edge points. Normalizing
over leaves cancels w^(0). Equations (9) and (14) prove the lemma.

## 4. Realizing the columns and removing the relabeling

Let I be the countable set of all nonroot tree vertices. Use the
column probability space X=[0,1]^I with product Lebesgue measure,
and write x_gamma for its coordinate functions. This nonatomic
standard probability space can be identified with [0,1] modulo null
sets. One explicit construction splits the independent binary digits
of one uniform variable into countably many infinite subsequences;
the resulting coordinate variables are independent uniform variables.
Interleaving the digits gives the inverse outside the null set of
ambiguous binary expansions.

For deterministic weights v=(v_alpha) of total one, partition the
row interval into intervals I_alpha of lengths v_alpha, using any
fixed enumeration of N^r. Define

\[
 m_{v,h}(s,x)=h(x_{\alpha|1},\ldots,x_{\alpha|r})
                       \quad\hbox{for }s\in I_\alpha.
\tag{15}
\]

This is measurable since there are countably many leaves. One may
choose a Borel representative of h; changing h on a null set changes
neither the kernel modulo null sets nor the countable sampled arrays
almost surely. The map from the weight sequence to the kernel class
is measurable: row endpoints are partial sums of weights, and finite
row truncations are measurable kernels; their omitted row masses tend
to zero. Take pi_h to be the law of its weak-kernel class when v is
the cascade V.
There is no extra random column function in this construction.

For any tree automorphism theta, the kernels with weights v and
with weights v'_alpha=v_{theta(alpha)} are equivalent after matching
the row intervals and permuting column coordinates. Explicitly, let R
send the new row interval alpha to the old row interval theta(alpha)
by translation, and set (P_theta x)_delta=x_{theta^(-1)(delta)}.
The coordinate permutation P_theta preserves product Lebesgue measure.
Since theta(alpha)|k=theta(alpha|k),

\[
 m_{v,h}(R(s),P_\theta x)=m_{v',h}(s,x).
\]

The row map R is measure preserving because each matched pair of
intervals has equal length. The countable piecewise translations
therefore give exact equivalence modulo null sets, stronger than
equivalence at cut distance zero.

Now sample any finite number q of independent columns X^1,...,X^q.
The vectors

\[
 Z_\gamma=(X_\gamma^1,\ldots,X_\gamma^q),\qquad \gamma\in I,
\tag{16}
\]

are independent uniform vectors, independent of V. For any fixed
measurable F:[-1,1]^q -> (0,infinity) bounded above and bounded away
from zero, the row tilt

\[
 z(s)=F(m_{V,h}(s,X^1),\ldots,m_{V,h}(s,X^q))
\tag{17}
\]

is constant on each leaf interval. On leaf alpha it equals

\[
 W_\alpha=w(Z_{\alpha|1},\ldots,Z_{\alpha|r}),\quad
 w(z_1,\ldots,z_r)=
 F\big(h(z_1^1,\ldots,z_r^1),\ldots,
       h(z_1^q,\ldots,z_r^q)\big).
\tag{18}
\]

Reweighting row measure changes the interval masses to (12), while
leaving the row functions in (15) unchanged. Equivalently the quantile
map replaces each leaf interval by one of that new length; within an
interval the tilt is constant, so its inverse is linear. The cascade
tilt lemma gives a tree reindexing after which the new masses have
their original joint law. The coordinate permutation just proved
removes that reindexing from the row functions. It is allowed to
depend on the realization: weak-kernel equivalence is checked for
each pair of realized kernels.

It follows that the law of the reweighted weak kernel is pi_h.
Notice what is not being asserted: the sampled marks in (16) after
reweighting are not claimed independent or uniform. They are used to
choose a tree permutation. That permutation acts on the entire column
space and preserves its measure for every fixed realization.

All finite cavity products in (2) have the form (17). Indeed,
exp(-beta)<=D,Q<=1 gives exp(-beta*d)<=A<=1, and a product of N site
and M edge factors lies in [exp(-beta*(d*N+M)),1]. Reusing a sampled
column in several factors also gives a function F of finitely many
columns, so it is included. The case N=M=0 is the identity tilt.
Thus pi_h belongs to D*, proving the invariant-law part of the claim.

## 5. Functional identity and the remaining gap

Under (15), integration in s is exactly summation against V_alpha.
Independent sampled columns give exactly the message arrays in (5).
Replacing Q by C=e^beta Q multiplies a site factor by exp(beta*d)
and an edge factor by exp(beta). Their logarithmic shifts in the
site-minus-d/2-edge functional are beta*d-(d/2)*beta=beta*d/2.
Adding log 2 gives (6). The minimum in (3) is at most each of these
admissible trial values. Equations (4) and (6), followed by the
infimum over trials, prove (7).

In particular, no independent regular-graph interpolation theorem is
needed for this deduction once the invariant-law theorem is accepted.
The general regular finite-RSB upper bound is already stated in
Viktor Harangi, [*RSB bounds on the maximum cut*, arXiv:2506.21296v1,
Theorem 3.2](https://arxiv.org/html/2506.21296v1).
The contribution here is the explicit inclusion in the round 4 trial
space and its exact normalization, proved by the marked Poisson argument.

For clarity about the unsolved direction, put
Delta_d(beta)=J_d(beta)-p_d(beta). We have proved Delta_d(beta)>=0.
Equation (4) yields

\[
 \frac{\Delta_d(\beta)}\beta
 \le \frac{J_d(\beta)}\beta-c_d
 \le \frac{\Delta_d(\beta)}\beta+\frac{\log2}\beta.
\tag{19}
\]

Thus J_d(beta)/beta -> c_d holds if and only if
Delta_d(beta)=o(beta). Controlling this nonnegative gap requires a
reverse comparison. It does not follow from the cascade invariance
proved above, and is not proved here.

## 6. Checks of the cascade exponents and normalization

The tilt lemma also yields the nested power-mean identity directly,
without assuming any independence between old and new total masses:

\[
 \mathbb E\log\sum_\alpha V_\alpha W_\alpha=\log w^{(0)}.
\tag{20}
\]

Indeed, (14) says that the unnormalized tilted total T_W divided by
w^(0) has the distribution of T. These totals have integrable
logarithms. To check this, the construction in Section 3 gives T a
Laplace transform exp(-K lambda^(zeta_0)) for some K>0. A positive
moment of any order less than zeta_0 is finite by the argument after
(10). For any q>0, the identity

\[
 s^{-q}=\frac1{\Gamma(q)}
           \int_0^\infty\lambda^{q-1}e^{-\lambda s}\,d\lambda
\]

and Tonelli show E T^(-q)<infinity; the integral converges at zero
and infinity after inserting the Laplace transform. These two moment
bounds imply E|log T|<infinity. The bounds l*T<=T_W<=u*T give the
same for T_W. Taking logarithms in
sum V_alpha W_alpha=T_W/T and then expectations proves (20).

For r=1, (20) is (1/zeta_0) log E W^(zeta_0), as also follows by
applying the intensity change in (8) once. For r=2 it is

\[
 \frac1{\zeta_0}\log\mathbb E_{Z_1}
      \left(\mathbb E_{Z_2}w(Z_1,Z_2)^{\zeta_1}
                           \right)^{\zeta_0/\zeta_1}.
\tag{21}
\]

In the separable case w=f(Z_1)g(Z_2), this becomes
(1/zeta_0)log E f^(zeta_0)+(1/zeta_1)log E g^(zeta_1).
Independently, marking the terminal process by g and the top process
by f produces precisely those two scale factors. This checks both
the order of integration and the two distinct exponents.

For comparison with the nested-power convention of Harangi's
Theorem 3.2, set m_1=zeta_(r-1) and, for 2<=k<=r,
m_k=zeta_(r-k)/zeta_(r-k+1). Then all m_k lie in (0,1) and their
product is zeta_0. Successive unrooted expectations of powers m_k
give an operator T_r satisfying log w^(0)=(1/zeta_0)log T_r W.
This follows by substituting (11) successively: the adjacent powers
cancel, leaving the stated ratios. Its star factor is 2A, and its
edge factor is B. Multiplying an input by 2 multiplies T_r by
2^(m_1...m_r), so its star contribution adds exactly log 2.
The extra conversion from uncut to cut pressure adds beta*d/2.
Thus its bound agrees with (6) and (7), checking the normalization
through a separate published upper-bound expression.

Finally, a deliberately asymmetric endpoint example tests the
dangerous mark-bias step. Take r=1, zeta_0=1/2, and h(U)=+1 for
U<=1/3, h(U)=-1 otherwise. For the general tilt F(v)=2+v, the
multipliers are 3 and 1. Their scale is
c=((sqrt(3)+2)/3)^2. After marking, the +1 probability in the
transformed mark law is sqrt(3)/(sqrt(3)+2), rather than 1/3:
the joint intensity weights each mark by F(v)^(1/2). Nevertheless
the sorted point process has its original intensity after division
by c, and its coordinate relabeling is measure preserving. This
example verifies why invariance of the weak kernel does not require
unbiased sampled marks. No assumption of spin-flip symmetry was used.
