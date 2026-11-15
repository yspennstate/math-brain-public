# Underoccupied regions in the hard-sphere Gibbs model

Distinct centers have distance at least one. Let d>=2, let z>0 be the activity, and put

\[
v_d=\frac{\pi^{d/2}}{\Gamma(1+d/2)}.
\]

All logarithms are natural. A box will be called underoccupied when its particle count is at most a specified number r. The estimates below allow particles throughout the region; no vacant strip is assumed.

## 1. Protected insertion balls

Fix a box side length ell and a radius 0<a<1/2. Suppose the reference box [0,ell)^d contains m_0>=1 open radius-a balls with the following properties:

1. Every point in each ball has distance greater than one from the box complement.
2. Every point in one ball has distance greater than one from every point in a different ball.

Write b=v_d a^d and v=ell^d. One explicit choice is the grid with spacing h=1+2a and coordinates

\[
1+a+jh,\qquad 0\leq j<k,\qquad
k=\max\left\{0,1+\left\lfloor
\frac{\ell-2(1+a)}{1+2a}\right\rfloor\right\}.
\tag{1}
\]

When k>=1 this gives m_0=k^d balls. The last coordinate is at most ell-1-a by (1). Subtracting a from each boundary margin proves property 1, with a strict inequality since the balls are open. Distinct grid centers have distance at least 1+2a; subtracting two open radii proves property 2.

Translate this same family into every half-open box

\[
Q_j=\ell\bigl(j+[0,1)^d\bigr),\qquad j\in\mathbb Z^d.
\]

Balls in different boxes are mutually compatible: every point of the other box lies in the first box's complement, so property 1 applies. The half-open convention makes the boxes a disjoint partition. It does not change their volumes or their insertion margins.

## 2. A bound for a prescribed collection of boxes

For r>=0 and T>0 define

\[
H_r(T)=
\begin{cases}
0,&r=0,\\
T,&r>0\text{ and }T\leq r,\\
r[1+\log(T/r)],&r>0\text{ and }T>r.
\end{cases}
\tag{2}
\]

Set

\[
\tau(z)=m_0\log(1+zb)-H_r(zv).
\tag{3}
\]

Let C be any nonempty finite subset of Z^d, let n=|C|, and let U_C be the union of its boxes. If N(U_C) counts the centers there, then

\[
\boxed{\quad
\Pr\{N(U_C)\leq rn\}\leq
\min\{1,\exp[-n\tau(z)]\}.
\quad}
\tag{4}
\]

This holds under the conditional hard-sphere Gibbs distribution in U_C with every admissible exterior, in every finite-volume Gibbs distribution whose sampling region contains U_C, and in every infinite-volume Gibbs measure. No connectivity assumption on C is needed in (4).

To prove this, fix an admissible exterior eta. The conditional partition function is

\[
Z_{U_C}^{\eta}(z)=\sum_{s=0}^{\infty}\frac{z^s}{s!}
\int_{U_C^s}\mathbf 1\{\eta\cup\{x_1,\ldots,x_s\}
\text{ is an admissible packing}\}\,dx_1\cdots dx_s.
\tag{5}
\]

There are m_0 n protected insertion balls in U_C. Restrict (5) to configurations containing zero or one point in each such ball and no points elsewhere. For an occupied subset J of s balls the s! assignments of the labeled coordinates cancel the factor 1/s!, leaving weight (zb)^s. All selected configurations are compatible with eta and with each other. Therefore

\[
Z_{U_C}^{\eta}(z)\geq(1+zb)^{m_0n}.
\tag{6}
\]

The unnormalized numerator for N(U_C)<=rn is at most

\[
E_{\lfloor rn\rfloor}(zvn),\qquad
E_K(t)=\sum_{s=0}^{K}\frac{t^s}{s!},
\tag{7}
\]

since the integral in each sector is at most |U_C|^s=(vn)^s. All displacement variables of the particles in this event are integrated in (7).

For 0<u<=1 and s<=floor(rn), one has u^{-s}<=u^{-rn}. Thus

\[
E_{\lfloor rn\rfloor}(zvn)
\leq u^{-rn}\sum_{s=0}^{\infty}\frac{(uzvn)^s}{s!}
=\exp\{n[uzv-r\log u]\}.
\tag{8}
\]

For r>0, choose u=1 if zv<=r and u=r/(zv) otherwise. The exponent is n H_r(zv). For r=0 the numerator is exactly one. Dividing (7)–(8) by (6) proves (4) for fixed eta. The extra upper bound one is automatic.

In a larger finite sampling region, condition on all centers outside U_C. Almost surely the resulting exterior is admissible, and the same bound holds independently of that exterior. Averaging proves (4). The DLR equation gives the identical conditional kernel in every infinite-volume Gibbs measure, so the same argument proves that case as well. No invariance or uniqueness hypothesis is used.

For a second derivation of (8), let Y have the Poisson distribution with mean zvn. Then E_K(zvn)=exp(zvn) Pr(Y<=K). For theta>=0, exponential Markov gives

\[
\Pr(Y\leq rn)
\leq e^{\theta rn}\mathbb E e^{-\theta Y}
=\exp\{n[\theta r+zv(e^{-\theta}-1)]\}.
\]

Choosing theta=max{0,log(zv/r)} for r>0 recovers (8) and (2), with the same signs and factors n.

If 0<=r<m_0, then tau(z) tends to infinity as z tends to infinity. More precisely, for r>0,

\[
\tau(z)=(m_0-r)\log z
+m_0\log b-r[1+\log(v/r)]+o(1).
\tag{9}
\]

For r=0, tau(z)=m_0 log(1+zb). Equation (9) describes the bound, not an asserted exact asymptotic probability.

## 3. Counting connected underoccupied regions

Declare j underoccupied if N(Q_j)<=r. Join two indices when their difference is one of the 2d signed coordinate unit vectors. Let K(j) be the connected component of underoccupied indices containing j, with K(j) empty when j is not underoccupied. Define

\[
B=(2d)^2,\qquad q(z)=B e^{-\tau(z)}.
\]

In every infinite-volume Gibbs measure, for every index j and integer n>=1,

\[
\boxed{\quad
\Pr\{|K(j)|\geq n\}
\leq \min\{1,B^{n-1}e^{-n\tau(z)}\}
=\min\{1,q(z)^n/B\}.
\quad}
\tag{10}
\]

For a finite-volume Gibbs law, the same bound holds for components in the graph induced by the boxes wholly contained in its sampling region. Exterior boxes are excluded from those components.

Indeed, fix j and a connected set C of n indices containing j. If every index of C is underoccupied, then N(U_C)<=rn, so (4) bounds its probability by exp[-n tau(z)].

There are at most (2d)^{2(n-1)} such C. To see this, fix an ordering of the coordinate directions. For each C choose a spanning tree by deterministic breadth-first exploration from j, and traverse this tree depth first in the fixed direction order. The resulting walk has 2(n-1) signed coordinate steps. Its visited vertices are exactly C, so two different C cannot have the same step word. There are (2d)^{2(n-1)} possible words.

If |K(j)|>=n, graph exploration of its component supplies a connected n-element subset containing j, including when the component is infinite. Taking a union bound over these subsets proves (10). Independence of box occupations is neither assumed nor needed.

Whenever tau(z)>2 log(2d), one has q(z)<1. Letting n tend to infinity in (10) shows that j belongs to no infinite underoccupied component almost surely. Taking the countable union over j shows that no such component exists anywhere, in any Gibbs measure. At fixed ell,a and r<m_0 this condition holds for all sufficiently large z by (9).

## 4. Explicit examples with particles present

Take ell=4 and a=1/4. The grid coordinates in each direction are 5/4 and 11/4. Thus

\[
m_0=2^d,\quad v=4^d,\quad
b=\begin{cases}\pi/16,&d=2,\\\pi/48,&d=3.\end{cases}
\]

Choose r=m_0/2. An underoccupied box may contain up to two centers in d=2 and four centers in d=3. These are positive-volume particle sectors, not just empty boxes.

For zv>=r, use log(1+zb)>=log(zb) in (3) to obtain

\[
\tau(z)\geq r\log\left(\frac{z b^2 r}{e v}\right).
\tag{11}
\]

Substituting the displayed constants gives

\[
e^{-\tau(z)}\leq
\begin{cases}
\left(\dfrac{2048e}{\pi^2 z}\right)^2,&d=2,\\[4pt]
\left(\dfrac{36864e}{\pi^2 z}\right)^4,&d=3.
\end{cases}
\tag{12}
\]

These constants can also be checked without (11). In d=2, (3) reads

\[
4\log(1+\pi z/16)-2[1+\log(8z)],
\]

whose logarithmic lower bound is 2 log[z pi^2/(2048e)]. In d=3 it reads

\[
8\log(1+\pi z/48)-4[1+\log(16z)],
\]

whose lower bound is 4 log[z pi^2/(36864e)].

The elementary inequalities pi>3 and e<3 yield fully rational bounds. The first follows by comparing a unit circle's circumference with its inscribed regular hexagon. For the second, k!>=2^{k-1} for k>=2, with strict inequality for k>=3, gives e=2+sum_{k>=2}1/k!<3.

For d=2 and z>=4096, (12) gives e^{-tau(z)}<=1/36 and q(z)<=16/36=4/9. For d=3 and z>=65536 it gives e^{-tau(z)}<=(3/16)^4=81/65536 and q(z)<=36 times 81/65536=729/16384. Consequently

\[
\Pr\{|K(j)|\geq n\}\leq
\begin{cases}
\dfrac1{16}\left(\dfrac49\right)^n,
&d=2,\ z\geq4096,\\[6pt]
\dfrac1{36}\left(\dfrac{729}{16384}\right)^n,
&d=3,\ z\geq65536.
\end{cases}
\tag{13}
\]

These activity thresholds are sufficient and are not claimed sharp. Activity is measured with exclusion distance one.

## 5. Thresholds below the optimal packing density

The same theorem permits much larger occupation thresholds if the boxes and insertion families are chosen accordingly. Let rho_* be the supremum of number densities of periodic diameter-one packings. It is positive because Z^d is a packing, and finite because disjoint radius-1/2 balls about centers in [0,L)^d fit in a cube of side L+1. This equals the unrestricted optimum: for any packing, repeat its centers in [0,L)^d with coordinate period L+1. Centers in different copies have a coordinate separation greater than one. If N_L is the original count, the resulting periodic density is N_L/(L+1)^d<=rho_*. Multiplying by ((L+1)/L)^d and passing to upper limits proves the unrestricted upper bound; periodic packings give the reverse inequality. Applying the same argument to translated cubes gives the same conclusion for that density convention as well.

Fix 0<rho<rho_*. Choose a periodic packing P of intensity rho_P>rho. Choose a>0 sufficiently small, with a<1/2, that rho_P/(1+2a)^d>rho. Put h=1+2a. A uniformly phased translate of hP has mean number of centers in the eroded reference box (1+a,ell-1-a)^d equal to

\[
\frac{\rho_P}{h^d}(\ell-2(1+a))^d
\tag{14}
\]

when ell>2(1+a). To verify the mean formula, write hP as finitely many representatives modulo its period lattice. Integrating each representative's counting sum over one lattice fundamental domain tiles R^d. Its integral is the test region's volume. Summing representatives and dividing by the fundamental volume gives intensity times volume.

Since the count is integer valued, some phase has at least

\[
m_0=\left\lfloor\frac{\rho_P}{h^d}
(\ell-2(1+a))^d\right\rfloor
\tag{15}
\]

centers in that eroded box. Put an open radius-a insertion ball at each of m_0 such centers. Their separation is at least h, and their boundary margin exceeds 1+a, so they satisfy the two properties of Section 1. Translate this one selected family into all boxes.

As ell tends to infinity, m_0/ell^d tends to rho_P/h^d>rho. Choose one finite ell large enough that m_0>rho ell^d and put r=rho ell^d. Now (4) and (10) apply to boxes with N(Q_j)<=rho ell^d. Since r<m_0, their connected-component sizes have an exponential tail at all sufficiently large activity, uniformly over all Gibbs measures. The choices of a,ell, and the activity threshold may depend on rho and P. No estimate is uniform as rho tends to rho_*.

## 6. Scope

The result suppresses prescribed and connected underoccupied regions while integrating all particle positions and summing the possible connected shapes. It extends the earlier empty-region estimate to particle-containing defects. It does not classify crystal orientations. In particular, no argument here shows that a boundary between two dense orientations contains a connected underoccupied region with the required number of boxes. Dense disordered packings, strain, and dislocations are not excluded by an occupation bound. No orientational surface tension, crystalline Gibbs state, or freezing transition follows from (4), (10), or (13).
