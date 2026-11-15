COUNTEREXAMPLE

# Trajectories of bistochastic quadratic stochastic operators

For every $m\geq4$, there is a genuinely nonlinear extreme bistochastic quadratic stochastic operator with interior two-cycles. An open dense set of its interior trajectories fails to converge. Every trajectory of every bistochastic quadratic stochastic operator, in every finite dimension, nevertheless approaches a single finite periodic cycle and has a convergent Cesàro average. Indeed, the latter assertion holds for every continuous map that decreases majorisation.

These conclusions settle the convergence-versus-ergodicity alternative in the question. They do not constitute a new solution of an open ergodicity problem: ergodicity and finite limit sets occur in the earlier literature, and the cited 2016 paper already contains a non-permutation linear example with interior two-cycles. The nonlinear extreme family below has a complete coefficient certificate and a complete description of its interior dynamics. No novelty claim is made for that family or for the auxiliary structural results.

The coefficient analysis is exact, but the requested complete classification of extreme points for $m=4,5$ is not obtained. Section 5 gives an exact finite copositivity description of the full class, the exact linear description for $m=3$, and an explicit distinction between necessary outer polytopes and certified subclasses in higher dimensions. The single-output subset inequalities must not be used as an exact parametrisation when $m\geq4$.

## 1. Definitions and the general trajectory theorem

Write

\[
S^{m-1}=\{x\in\mathbb R_+^m:\mathbf1^Tx=1\},\qquad
s_r(x)=\sum_{i=1}^r x_{[i]},\quad 1\leq r\leq m,
\]

where $x_{[1]}\geq\cdots\geq x_{[m]}$. The relation $y\prec x$ means $s_r(y)\leq s_r(x)$ for $r<m$, with equal total sums. An operator is bistochastic if $Vx\prec x$ everywhere. A QSO has symmetric coefficients $p_{ij,k}\geq0$ satisfying $\sum_kp_{ij,k}=1$, and

\[
(Vx)_k=\sum_{i,j}p_{ij,k}x_ix_j.
\]

Here a trajectory is called asymptotically periodic if there are a positive integer $q$ and distinct points $y_0,\ldots,y_{q-1}$ such that $Vy_j=y_{j+1\pmod q}$ and

\[
\lim_{n\to\infty}V^{nq+j}x=y_j,\qquad0\leq j<q.
\]

**Theorem 1.** Let $V:S^{m-1}\to S^{m-1}$ be continuous and satisfy $Vx\prec x$. Every trajectory is asymptotically periodic. If $v=\lim_n(V^nx)_\downarrow$, then

\[
\omega(x)=\{y_0,\ldots,y_{q-1}\}\subseteq\{Pv:P\text{ a coordinate permutation}\},
\qquad
q\leq\frac{m!}{\prod_a\nu_a!},
\]

where $\nu_a$ are the multiplicities of the distinct coordinate values of $v$. Moreover, for every continuous $f:S^{m-1}\to\mathbb R$,

\[
\lim_{N\to\infty}\frac1N\sum_{n=0}^{N-1}f(V^nx)
=\frac1q\sum_{j=0}^{q-1}f(y_j).
\tag{1}
\]

In particular, the vector Cesàro averages converge to $q^{-1}\sum_jy_j$, and the empirical probability measures converge weakly to $q^{-1}\sum_j\delta_{y_j}$.

*Proof.* For each $r<m$, $s_r(V^nx)$ is non-increasing and bounded below. Let its limit be $b_r$, and put $b_0=0,b_m=1$. Since

\[
(V^nx)_{[r]}=s_r(V^nx)-s_{r-1}(V^nx),
\]

the decreasing rearrangements converge to $v=(b_1-b_0,\ldots,b_m-b_{m-1})$. Rearrangement is continuous, so every accumulation point has rearrangement $v$. Compactness therefore makes $F=\omega(x)$ a nonempty finite subset of the permutation orbit of $v$.

Continuity gives $V(F)\subseteq F$. Conversely, for $z\in F$, choose $n_k\to\infty$ with $V^{n_k}x\to z$. A subsequence of $V^{n_k-1}x$ converges to some $w\in F$, and continuity gives $Vw=z$. Thus $V(F)=F$, and $V|_F$ is a permutation of the finite set $F$.

It remains to prove that $F$ consists of one cycle and that the phases converge. If $|F|=1$, this follows immediately from compactness. Otherwise let $d>0$ be the minimum distance between distinct points of $F$. Choose $0<\varepsilon<d/3$ so small that

\[
\|u-z\|<\varepsilon,\ z\in F
\quad\Longrightarrow\quad
\|Vu-Vz\|<d/3.
\]

The distance from $V^nx$ to $F$ tends to zero; otherwise a subsequence staying a positive distance away would have an accumulation point outside $F$. For all sufficiently large $n$, there is a unique $z_n\in F$ within $\varepsilon$ of $V^nx$. The preceding inequality and the separation of the points of $F$ imply $z_{n+1}=Vz_n$: any other label would have distance less than $d/3+\varepsilon<d$ from $Vz_n$. Hence the labels eventually follow one cycle. Their distances from the actual trajectory tend to zero. No point of another cycle can be an accumulation point, proving both assertions about $F$ and the stated phase convergence.

For each residue class modulo $q$, continuity gives $f(V^{nq+j}x)\to f(y_j)$. Taking Cesàro means in each residue class, and observing that the finitely many initial terms and the incomplete final block contribute (o(1)), proves (1). The permutation-orbit count is the usual multinomial count. ∎

**Corollary 1.1.** Such an operator is regular, meaning every trajectory converges, if and only if it has no periodic points of period greater than one. The same assertion applies to interior initial points if there are no nontrivial interior periodic points.

*Proof.* A nontrivial periodic trajectory cannot converge. In the other direction apply Theorem 1. For an interior initial point, majorisation gives

\[
\min_i(V^nx)_i\geq\min_i x_i>0,
\]

so its entire limit cycle is interior. ∎

**Proposition 1.2.** The centre $c=(1/m,\ldots,1/m)$ is fixed. Every continuous Schur-convex function decreases along trajectories and is constant on each limit cycle. In particular,

\[
L(x)=\sum_i x_i^2,\qquad L(Vx)\leq L(x),
\]

with equality if and only if $Vx$ is a coordinate permutation of $x$.

*Proof.* The centre is the unique point majorised by $c$, so $Vc=c$. The monotonicity assertion is the definition of Schur convexity; boundedness on the compact simplex gives a limit. To check strictness for $L$, use the classical majorisation identity $y\prec x\iff y\in\operatorname{conv}\{Px\}$. If $y=\sum_P\lambda_PPx$, then

\[
\sum_P\lambda_P\|Px\|_2^2-\Big\|\sum_P\lambda_PPx\Big\|_2^2
=\frac12\sum_{P,Q}\lambda_P\lambda_Q\|Px-Qx\|_2^2.
\]

Equality holds exactly when all positively weighted permutation vectors coincide, in which case $y$ is a permutation of $x$. ∎

Thus all sorted partial sums, rather than the quadratic Lyapunov function alone, identify the limiting multiset of coordinates. Their common level set is exactly a finite permutation orbit. A two-cycle necessarily consists of two permutations of one vector. Non-ergodic orbits are impossible in this finite-dimensional bistochastic class.

## 2. A nonlinear extreme counterexample in every $m\geq4$

Let $\tau$ exchange coordinates 1 and 2 and fix the others. Define

\[
W(x)=(1-x_1)x+x_1\tau x,
\]

and let $P$ exchange coordinates 1 and 3, and coordinates 2 and 4, fixing the remaining coordinates. Set $V=P\circ W$. On the simplex,

\[
\begin{aligned}
(Vx)_1&=x_3,\quad &(Vx)_2&=x_4,\\
(Vx)_3&=x_1-x_1^2+x_1x_2,
&(Vx)_4&=x_2+x_1^2-x_1x_2,\\
(Vx)_k&=x_k &&(k\geq5).
\end{aligned}
\tag{2}
\]

Linear terms in (2) are homogenised by multiplying by $\sum_i x_i$.

**Theorem 2.** For every $m\geq4$, (2) is a genuinely nonlinear extreme point of the convex set of bistochastic QSOs. Its interior periodic points are exactly

\[
\mathcal M=\{x\in\operatorname{int}S^{m-1}:x_1=x_2,\ x_3=x_4\}.
\]

Such a point is fixed if $x_1=x_3$, and otherwise has least period two. For every interior initial point, put

\[
s=x_1+x_2,\quad t=x_3+x_4,\qquad
y=(s/2,s/2,t/2,t/2,x_5,\ldots,x_m).
\]

Then

\[
V^{2n}x\longrightarrow y,\qquad V^{2n+1}x\longrightarrow Py.
\tag{3}
\]

Consequently the trajectory converges if and only if $s=t$. The set $s\ne t$ is open and dense in the relative interior, and all of its trajectories are non-convergent. Their Cesàro limit is

\[
((s+t)/4,(s+t)/4,(s+t)/4,(s+t)/4,x_5,\ldots,x_m).
\tag{4}
\]

*Proof: coefficients and bistochasticity.* Write $q_{ij}\in\mathbb R^m$ for the coefficient vector of $W$. They are symmetric, and are given completely by

\[
\begin{aligned}
q_{11}=q_{22}&=e_2,&q_{12}&=e_1,\\
q_{1j}&=(e_1+e_j)/2,&q_{2j}&=(e_2+e_j)/2\quad(j\geq3),\\
q_{ij}&=(e_i+e_j)/2&& (i,j\geq3).
\end{aligned}
\tag{5}
\]

Every vector in (5) is nonnegative with total one; the coefficients of $V$ are $p_{ij}=Pq_{ij}$. Expanding (5) gives the displayed formula for $W$, and hence (2). For any output set $K$ of cardinality $r$, the sum of coordinates in $K$ of either $x$ or $\tau x$ is at most $s_r(x)$. Their convex combination therefore satisfies $Wx\prec x$. Output permutation preserves this relation, so $Vx\prec x$. On the edge $x_3=\cdots=x_m=0$, $(Vx)_3=2x_1x_2$, which is not affine on that edge. Thus $V$ is genuinely nonlinear.

*Proof: extremality.* First observe the following rigidity fact. Suppose $A,B$ are bistochastic QSOs and

\[
\tfrac12(A_j(x)+B_j(x))=x_j\quad\text{for all }x\in S^{m-1}.
\]

On the nonempty relatively open set where $x_j$ is the unique largest coordinate, both $A_j(x)$ and $B_j(x)$ are at most $x_j$. They must both equal $x_j$ there. A polynomial vanishing on a relatively open subset of the simplex vanishes on its affine hull, so $A_j=B_j=x_j$ throughout the simplex. Their homogeneous coefficients are also identical: homogenising $x_j$ gives $x_j\sum_i x_i$, and a homogeneous polynomial that vanishes on the simplex vanishes on the whole positive cone, hence identically.

Now suppose $W=(A+B)/2$. Since $W_j(x)=x_j$ for $j\geq3$, the preceding argument fixes every coefficient of these output coordinates in both $A$ and $B$. Every zero coefficient of $W$ is a zero coefficient of $A$ and $B$, by nonnegativity. For parent pairs $11,22,12$, the output vector of $W$ is a unit vector, so normalisation fixes that pair completely. For a pair (1j), $j\geq3$, its $j$-th output coefficient is already (1/2), every output other than 1 and $j$ is zero, and normalisation forces the first coefficient to be (1/2). The pairs (2j) are treated identically. For pairs $i,j\geq3$, all coefficients have already been fixed by the fixed output coordinates and the zeros. Thus $A=B=W$. Midpoint indecomposability is equivalent to extremality in a convex set. Finally, output permutation is an affine bijection of the bistochastic class, so $V=PW$ is extreme.

*Proof: equality and periodic points.* The elementary two-vector variance identity gives, since $P$ is an isometry,

\[
L(x)-L(Vx)=2x_1(1-x_1)(x_1-x_2)^2.
\tag{6}
\]

At an interior periodic point, $L$ is constant along the cycle. Since $0<x_1<1$, (6) forces $x_1=x_2$. Applying the same conclusion to $Vx$, whose first coordinates are $x_3,x_4$, forces $x_3=x_4$. Conversely, both equalities imply $Wx=x$, $Vx=Px$, and $V^2x=x$. The fixed-point and least-period assertions follow.

*Proof: convergence of the phases.* Put $a_n=(V^nx)_1-(V^nx)_2$ and $b_n=(V^nx)_3-(V^nx)_4$. Formula (2) gives

\[
a_{n+1}=b_n,\qquad b_{n+1}=(1-2(V^nx)_1)a_n.
\tag{7}
\]

The pair sums $s,t$ exchange at every step, and all coordinates beyond the fourth are fixed. Let $\delta=\min_i x_i>0$, $M=\max_i x_i<1$, and

\[
\rho=\max\{|1-2\delta|,|1-2M|\}<1.
\]

Majorisation keeps every coordinate in $[\delta,M]$. Applying (7) twice yields

\[
|a_{2n}|\leq\rho^n|a_0|,\qquad
|b_{2n}|\leq\rho^n|b_0|.
\]

It follows that

\[
\|V^{2n}x-y\|_\infty\leq\tfrac12\rho^n\max(|a_0|,|b_0|),
\tag{8}
\]

and the same bound holds for $\|V^{2n+1}x-Py\|_\infty$, by (7). This proves (3), the convergence criterion, and (4). ∎

For $m=4$ an exact interior cycle is

\[
(1/3,1/3,1/6,1/6)
\ \longleftrightarrow\ 
(1/6,1/6,1/3,1/3).
\tag{9}
\]

For $m>4$, take

\[
x=(1/4,1/4,1/8,1/8,\underbrace{1/[4(m-4)],\ldots,1/[4(m-4)]}_{m-4\text{ entries}}).
\]

The first two pairs exchange and all remaining coordinates are fixed. These certificates use only rational coefficients and rational points. The coefficients and both iterates for $m=4,5,6$ are stored in `data/exact_cycles.json`.

The cycles are neutral along the family and attracting in the two transverse directions. At $x=(a,a,b,b,x_5,\ldots,x_m)\in\mathcal M$, the return map $V^2$ is the identity on the tangent space of the family, and its two transverse multipliers are (1-2a) and (1-2b), both in $(0,1)$. These follow directly by linearising the two-step version of (7). For (9) they are $1/3,2/3$. This is attraction to a family of cycles; an individual cycle does not have a whole neighbourhood converging to it.

More generally, no nontrivial periodic cycle of a continuous bistochastic map can attract a full neighbourhood of itself. If its squared norm is $R>1/m$, points obtained by taking a small convex combination of a cycle point with $c$ have smaller squared norm. Their trajectories, whose squared norm cannot increase, cannot approach that cycle.

## 3. The two-simplex, including the periodic-point hypothesis

The following scalar fact also explains the exact coefficient description in dimension three.

**Lemma 3.1.** For a symmetric nonnegative matrix $A$, the following conditions are equivalent:

\[
\sum_{i,j\in J}A_{ij}\leq |J|\quad(J\subseteq[m]),
\qquad \sum_{i,j}A_{ij}=m;
\tag{10}
\]

\[
A=(T+T^T)/2\quad\text{for a row-stochastic matrix }T.
\tag{11}
\]

They imply $\min_i x_i\leq x^TAx\leq\max_i x_i$ on the simplex. If $x$ is interior and has a unique largest coordinate $x_j$, then $x^TAx=x_j$ forces $x^TAx=x_j$ identically on the simplex. The analogous assertion holds for a unique smallest coordinate.

*Proof.* Equation (11) immediately gives (10). Conversely, regard each diagonal entry $A_{ii}$ as a demand attached only to vertex $i$, and each off-diagonal pair as a demand $2A_{ij}$ that may be assigned to either endpoint. Each vertex has capacity one. The demand of all edges and loops supported in $J$ is exactly the left side of (10), so it is at most the capacity $|J|$.

Construct a flow network with a source supplying the demand nodes, infinite-capacity arcs from each demand node to its available endpoints, and unit-capacity arcs from the vertices to the sink. In a finite cut, every demand node on the source side has all its endpoints there. If $J$ is the set of vertices on that side, the cut capacity is at least $m-d(J)+|J|\geq m$, where $d(J)=\sum_{i,j\in J}A_{ij}$. The max-flow/min-cut theorem gives a flow of value $m$. Since total capacity is $m$, every vertex receives exactly one. Let $T_{ij}$ be the part of demand $2A_{ij}$ assigned to endpoint $i$, and let $T_{ii}=A_{ii}$. This is the required row-stochastic matrix.

Now $x^TAx=x^TTx=\sum_i x_i(Tx)_i$. Each $(Tx)_i$ lies between the smallest and largest coordinate of $x$, proving the bounds. Equality at an interior point with a unique maximum $x_j$ forces every row of $T$ to be concentrated at column $j$. Then $x^TTx=x_j\sum_i x_i=x_j$ identically. The proof for the minimum is the same. ∎

**Theorem 3.2.** For $m=3$, every non-permutation bistochastic QSO has convergent trajectories from every interior initial point. Universal convergence, including all operators and boundary points, is false.

*Proof.* Set $A_k=(p_{ij,k})$. Bistochasticity implies (10) for every $A_k$: evaluate at the uniform distribution on $J$, and at $c$. Thus Lemma 3.1 applies to every output coordinate.

Suppose there is a nontrivial interior periodic orbit. Every step permutes the coordinate multiset by Proposition 1.2. If the three coordinate values are distinct, equality at the unique maximum and minimum forces two different output coordinates to be two different coordinate projections globally. The third is the remaining projection because the output sum is one. Hence $V$ is a permutation operator.

If there are exactly two values, let $i$ be the location of the singleton value and $j$ its location after one step. Equality at the unique maximum or minimum gives $V_j(z)=z_i$ identically. A nonfixed step must have $j\ne i$, since otherwise the other two equal coordinates also retain their values. At the next step, let the singleton move from $j$ to $k$. Then $V_k(z)=z_j$ identically. Necessarily $k\ne j$, since $V_j=z_i$ cannot also be $z_j$. Again there are two different output projections of two different input coordinates, so $V$ is a permutation. If all three values coincide, the point is $c$ and is fixed. This excludes nontrivial interior periodic points for every non-permutation $V$, and Theorem 1 proves convergence.

For failure of universal convergence, coordinate permutations already suffice. A genuinely nonlinear boundary example is

\[
B(x,y,z)=(y^2+2xz,\ z^2+2xy,\ x^2+2yz).
\tag{12}
\]

For each fixed parent index, the other parent is sent bijectively to the three output indices. Thus $B(x)=\sum_i x_iP_ix$ for three permutation matrices, proving bistochasticity. Every coefficient vector is a unit vector, so it is extreme even in the full QSO coefficient simplex. Its vertices form the three-cycle $e_1\mapsto e_3\mapsto e_2\mapsto e_1$. ∎

The interior theorem is already Theorem 3.5 and its consequence in the [2016 paper](https://doi.org/10.1515/math-2016-0045). It removes the periodic-point hypothesis for non-permutation operators on the interior, not on the boundary and not in higher dimensions.

**Proposition 3.3.** In any dimension, if $p_{ii,k}>0$ for every $i,k$, then a bistochastic QSO has every trajectory converging to $c$.

*Proof.* The diagonal positivity makes $Vx$ interior for every $x\in S^{m-1}$. At a noncentral interior periodic point, some output coordinate equals the largest input coordinate. In the representation of Lemma 3.1, equality forces every row of the relevant $T$ to be supported on the set of maximal input coordinates. Choose an index $j$ outside that set. Then $T_{jj}=p_{jj,k}>0$, a contradiction. The same argument excludes noncentral fixed points. Theorem 1 now gives global convergence to $c$. ∎

This agrees with the regularity result under diagonal positivity in [Saburov (2017)](https://doi.org/10.1007/s00025-017-0723-3). Strictly positive coefficient tensors are covered as a special case.

## 4. Exact permutation equality loci

The necessary equality of coordinate multisets can be sharpened to linear feasibility conditions for a fixed bistochastic QSO, including on faces of the simplex.

For a permutation $\pi$, let $T_\pi$ be the integer matrix defined by

\[
(T_\pi z)_{\pi(j)}=z_j+\cdots+z_m.
\]

Thus $x=T_\pi z$, $z\geq0$, describes the chamber $x_{\pi(1)}\geq\cdots\geq x_{\pi(m)}\geq0$. Let $a_{\pi,r}=\sum_{j\leq r}e_{\pi(j)}$, and for an output subset $K$ of cardinality $r$, put

\[
Q_{\pi,K}(p)=T_\pi^T\left[
\tfrac12(a_{\pi,r}\mathbf1^T+\mathbf1a_{\pi,r}^T)
-\sum_{k\in K}A_k\right]T_\pi.
\tag{13}
\]

A symmetric matrix $Q$ is copositive if $z^TQz\geq0$ for all $z\geq0$.

**Lemma 4.1.** If $Q$ is copositive and $z\geq0$ has support $H$, then

\[
z^TQz=0\quad\Longleftrightarrow\quad Q_{HH}z_H=0.
\tag{14}
\]

*Proof.* For any vector $h$ supported in $H$, $z+th\geq0$ for all sufficiently small $|t|$. If the quadratic form vanishes at $z$, it has a local minimum there along every such line. Its first derivative is therefore zero, giving $Q_{HH}z_H=0$. The converse follows by multiplication by $z_H^T$. ∎

**Theorem 4.2.** Fix a bistochastic QSO and a coordinate permutation $\sigma$, with convention $(\sigma x)_{\sigma(i)}=x_i$. In a chamber $\pi$, put $K_r=\{\sigma(\pi(1)),\ldots,\sigma(\pi(r))\}$. Then $Vx=\sigma x$ holds exactly on the union over nonempty $H\subseteq[m]$ of the sets

\[
\begin{gathered}
x=T_\pi z,\qquad z\geq0,\quad z_{H^c}=0,\quad\mathbf1^TT_\pi z=1,\\
(Q_{\pi,K_r})_{HH}z_H=0\qquad(1\leq r<m).
\end{gathered}
\tag{15}
\]

The union over all chambers is the full equality locus. It is a finite union of polytopes, rational when the coefficients are rational. For each fixed positive integer $q$, $\operatorname{Fix}(V^q)$ is also a finite union of rational polytopes when $p$ is rational. Existence of a nontrivial periodic orbit then implies existence of one with rational coordinates.

*Proof.* For any $z\geq0$, (13) gives

\[
z^TQ_{\pi,K}z=s_r(x)\mathbf1^Tx-\sum_{k\in K}(Vx)_k,\quad x=T_\pi z.
\tag{16}
\]

Here $V$ is evaluated by its homogeneous formula off the simplex. Bistochasticity makes every matrix in (13) copositive. The identities $Vx=\sigma x$ are equivalent, by successive differences and conservation of total mass, to the vanishing of (16) for the sets $K_r$. Lemma 4.1 proves (15) for the actual support $H$. Conversely, the kernel conditions in (15) make all the quadratic forms zero, even if some coordinates indexed by $H$ vanish. This proves the equality locus description. The normalisation bounds $z$, so the sets in (15) are polytopes.

At a periodic point every step is a permutation of the initial coordinate multiset. Choose a sequence of $q$ step permutations. For this fixed sequence, impose the relevant equality locus at every step, pull it back by the preceding coordinate permutations, and impose that their product fixes $x$. These are finite unions of intersections of rational polytopes and rational linear equations. Taking the finite union over all step permutations proves the assertion about $\operatorname{Fix}(V^q)$.

If a nonfixed periodic point lies in one of these rational polytopes, rational points are dense in that polytope. The condition $Vx\ne x$ is relatively open. A nearby rational point in the same polytope remains nonfixed and periodic. ∎

This gives an exact, finite, although potentially expensive, rational linear-feasibility search for periodic points of a given certified rational bistochastic QSO. It is stronger than checking the nonlinear equations $V^qx=x$ numerically. Formula (6) provides the particularly simple equality analysis for (2).

## 5. Coefficient conditions, dimensions and extreme points

Let $\mathcal B_m$ denote the full majorisation-defined class. Define the following necessary outer polytope:

\[
\begin{split}
\mathcal O_m=\{p:\;&p_{ij,k}=p_{ji,k}\geq0,\quad\sum_kp_{ij,k}=1,\\
&\sum_{i,j}p_{ij,k}=m\quad(k\in[m]),\\
&\sum_{i,j\in J}p_{ij,k}\leq |J|\quad(\varnothing\ne J\subsetneq[m],\ k\in[m])\}.
\end{split}
\tag{17}
\]

**Theorem 5.1.** The following assertions hold.

1. $\mathcal B_m\subseteq\mathcal O_m$, with equality for $m=2,3$.
2. In every $m$, a QSO belongs to $\mathcal B_m$ if and only if all matrices $Q_{\pi,K}(p)$ in (13), for all input chambers and all nonempty proper output subsets, are copositive. These are finitely many exact coefficient conditions, linear in $p$ before imposing copositivity.
3. Both $\mathcal B_m$ and $\mathcal O_m$ have affine dimension

\[
d_m=(m-1)\left(\frac{m(m+1)}2-1\right).
\tag{18}
\]

*Proof.* For the first inclusion, evaluate $V$ at the uniform distribution on a set $J$. Its largest output coordinate is at most $1/|J|$, giving the subset inequalities. At $c$, the identity $Vc=c$ gives the total equations. For $m=3$, (17) and Lemma 3.1 give $\min x\leq(Vx)_k\leq\max x$ for every coordinate. For two probability vectors with three coordinates, these bounds are exactly the $r=1,2$ majorisation inequalities. The $m=2$ case is immediate.

For the second assertion, (16), homogeneity, and the covering of the nonnegative orthant by the chambers show equivalence to

\[
\sum_{k\in K}(Vx)_k\leq s_{|K|}(x)
\]

for every simplex point and every output subset. Maximising over $K$ gives precisely the definition of majorisation.

For the dimension, put $N=m(m+1)/2$ and regard the $Nm$ symmetric coefficients as variables. The $N$ parent-pair normalisations and $m$ centre equations have exactly one linear dependence. To see that there are no others, in a linear dependence the coefficient of $p_{ij,k}$ has the form $\alpha_{ij}+w_{ij}\beta_k=0$, where $w_{ii}=1,w_{ij}=2$ for $i<j$. It follows that every $\beta_k$ is the same scalar and $\alpha_{ij}$ is its negative times $w_{ij}$. Hence the affine solution space has dimension $Nm-N-m+1=d_m$. The tensor $p^0_{ij,k}=1/m$ satisfies every proper subset inequality strictly, so $\mathcal O_m$ has that dimension.

To see that $\mathcal B_m$ has the same affine hull, perturb $p^0$ within this affine space by $\Delta$, with $|\Delta_{ij,k}|\leq\varepsilon$. Put $u=x-c$, $M=\|u\|_\infty$, and $q_k(x)=x^T\Delta_kx$. Since $q_k(c)=0$,

\[
|q_k(x)|=|u^T\Delta_k(x+c)|\leq2m\varepsilon M.
\]

For $u\ne0$, its sorted partial sums satisfy $s_r(x)-r/m\geq M/(m-1)$. Indeed, if the largest absolute coordinate of $u$ is its maximum $a>0$, averaging the other $m-1$ coordinates gives $\sum_{j\leq r}u_{[j]}\geq(m-r)a/(m-1)$. If it is the negative of its minimum $-b$, averaging the first $m-1$ coordinates gives $\sum_{j\leq r}u_{[j]}\geq rb/(m-1)$. Therefore, for $\varepsilon<1/[2m(m-1)^2]$, every output subset sum of the perturbed operator is at most $s_r(x)$. Taking $\varepsilon<1/m$ also ensures coefficient nonnegativity. This gives a relative neighbourhood of $p^0$ inside $\mathcal B_m$, proving (18). ∎

The exact descriptions and their sizes are as follows. The inequality counts in the fourth column are raw counts, not irredundant facet counts.

| $m$ | symmetric variables | affine dimension | inequalities in (17), including nonnegativity | matrices in exact copositivity description |
|---:|---:|---:|---:|---:|
| 3 | 18 | 10 | 36 | 36 matrices of order 3 |
| 4 | 40 | 27 | 96 | 336 matrices of order 4 |
| 5 | 75 | 56 | 225 | 3,600 matrices of order 5 |

The integer systems (17) are stored as `data/m3_outer_H.json`, `data/m4_outer_H.json`, and `data/m5_outer_H.json`. Only the first is a full-class linear description. The exact general-class matrices are generated by `chamber_matrix` in `code/experiments.py`.

### Why the single-output conditions are insufficient

For $m=4$, consider the coefficient tensor whose polynomial is

\[
\begin{aligned}
F_1&=x_1^2+x_2^2+x_1x_3+x_2x_4,\\
F_2&=2x_1x_2+x_1x_3+x_2x_4,\\
F_3&=x_4^2+x_1x_4+x_2x_3+x_3x_4,\\
F_4&=x_3^2+x_1x_4+x_2x_3+x_3x_4.
\end{aligned}
\tag{19}
\]

All coefficients are $0,1/2,1$ in the symmetric convention. They satisfy every condition in (17). Indeed, each output matrix is $(T_k+T_k^T)/2$, where $T_k$ has its unit entry in row $i$ in the column prescribed by the following row-to-column lists:

\[
T_1:(1,2,1,2),\quad T_2:(2,1,1,2),\quad
T_3:(4,3,4,4),\quad T_4:(4,3,3,3).
\]

Lemma 3.1 proves the subset conditions and slice totals. These representations are independently checked in `code/audit.py`; the integer constraints are also checked in `code/experiments.py` and recorded in `data/outer_polytope_witness.json`. But

\[
x=(3/5,1/4,1/10,1/20),\qquad
Fx=(99/200,149/400,1/16,7/100),
\]

and

\[
(Fx)_1+(Fx)_2-(x_1+x_2)=7/400>0.
\tag{20}
\]

The first two output coordinates are the largest, so (20) violates majorisation. The normalisation of (19) follows also by adding the four polynomials to obtain $(\sum_i x_i)^2$. Thus $\mathcal O_4\ne\mathcal B_4$. This is a coefficient-description control, not a counterexample to the trajectory theorem, since $F$ is not bistochastic.

The issue is already present in the published [Ganikhodzhaev–Shahidi paper (2010)](https://doi.org/10.1016/j.laa.2009.07.002), in the remark following Theorem 2.6: the single-slice conditions cease to be equivalent to the stronger conditions in higher dimensions. Its [2008 preprint](https://arxiv.org/abs/0802.1100), Corollaries 4.3–4.4, should therefore not be substituted for the published higher-dimensional coefficient discussion. No claim of a new counterexample to the published theorem is intended.

### Certified parametrisations for the search

A convenient sufficient subclass is

\[
V(x)=\sum_{i=1}^m x_iD_i x,
\qquad D_i\text{ doubly stochastic},
\qquad
p_{ij,k}=\tfrac12((D_i)_{kj}+(D_j)_{ki}).
\tag{21}
\]

Every term $D_ix\prec x$, and each output subset sum is bounded by $s_r(x)$, so (21) is rigorously bistochastic. Taking each $D_i$ to be a permutation gives sparse rational examples. The family (2) is of this form. This parametrisation is not asserted to exhaust $\mathcal B_m$.

Another sufficient condition is that every sum $\sum_{k\in K}A_k$ admit a representation $(T+T^T)/2$, with $0\leq T_{ij}\leq1$ and all row sums $|K|$. Every row average against $x$ then lies between the sum of the smallest $|K|$ coordinates and $s_{|K|}(x)$; multiplying by $x_i$ and summing proves the required subset bound. For fixed $p$, these representations are linear feasibility certificates. Necessity in arbitrary dimension is not used here.

### Extreme points

For a polytope given by equalities $Ep=e$ and inequalities $Ap\leq b$, a feasible point is a vertex exactly when the equalities together with its active inequalities have full column rank. If the rank is deficient, a nonzero null direction preserves all active constraints and, for sufficiently small steps of either sign, every inactive inequality, giving a nontrivial line segment. If the rank is full, a midpoint decomposition forces both endpoints to satisfy every active equality and hence to equal the point. This proves the criterion.

For $m=3$, the complete known classification has 222 labelled vertices, or 37 classes under output permutation. They are reproduced in `data/m3_vertices.json` as integer numerators with denominator two. The enumeration in `code/experiments.py` has two parts: a halfspace-intersection computation in the ten-dimensional affine space, and an independent exhaustive check of all $3^3 6^3=5,832$ coefficient choices with unit diagonal vectors and off-diagonal vectors either unit or half the sum of two units. The grid contains 225 feasible tensors; exactly 222 have full active rank. Completeness of the half-grid uses the known three-dimensional half-integrality theorem, rather than a general claim about vertices of intersections. Every listed vertex has exact integer feasibility and rank 18 modulo the prime 1,000,003, which proves full rank over the rationals. The count agrees with the classification recalled in the [2016 article, Section 4](https://doi.org/10.1515/math-2016-0045).

For every $m$, permutation operators are extreme: if $Px$ is the average of two points majorised by $x$, the fact that $Px$ is a vertex of the permutahedron forces both points to equal $Px$, for each $x$. Operators with unit output vectors for every parent pair are extreme in the full QSO simplex, hence in the bistochastic class whenever they are bistochastic. Symmetric Latin-square tensors provide such examples in every $m$: take $p_{ij,k}=1$ when $k=i+j\pmod m$, and zero otherwise, with independent output relabelling and a common input relabelling. For each parent $i$, the map of the other parent to the output is a permutation, establishing (21).

Theorem 2 supplies nonlinear extreme operators with non-convergent interior trajectories in every $m\geq4$. As a separate finite certificate, its tensors for $m=4,5,6$ have full active rank $40,75,126$, respectively, even in the necessary outer polytopes (17). Since $\mathcal B_m\subseteq\mathcal O_m$, a feasible bistochastic point that is extreme in $\mathcal O_m$ is also extreme in $\mathcal B_m$. The proof of Theorem 2 establishes extremality for every $m$, without relying on these finite checks.

An exhaustive vertex list for $\mathcal B_4$ or $\mathcal B_5$ is not supplied. The exact conic description (13) does not by itself prove polyhedrality. Later literature often calls the full class a polytope; this report neither proves nor disproves that general assertion. In particular, the files named `outer_H` must not be presented as full-class higher-dimensional polytopes.

## 6. Reproducible numerical experiments

Run from this directory:

```sh
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 python3 code/polytope_probe.py
python3 code/experiments.py
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 python3 code/followup.py
python3 code/audit.py
```

Dependencies are Python, NumPy, SciPy and SymPy; exact versions are in `data/summary.json`. No language-model workers, subagents or numerical worker pools were launched. The main experiment sets all numerical thread caps to one. Its measured peak resident memory was 119,095,296 bytes, approximately 113.6 MiB, far below 4 GB. The main run took approximately 6.28 seconds; this is a machine-specific observation, not a benchmark claim.

The seed is 6,602,026. There are 457 operator instances and 7,705 trajectories. Every operator used in the trajectory search has an analytic bistochastic certificate: all 222 three-type extreme tensors, symmetric Latin-square extreme tensors, operators of form (21), their convex mixtures with the constant-centre operator, permutation controls, and (2). The random samples are not uniform samples of the entire class. Repeated sampled tensors are reported explicitly.

Each operator is tested from twelve Dirichlet interior starts, the centre and every vertex; the targeted family also includes its rational two-cycle point. Each trajectory has 1,024 steps. Numerical total mass is renormalised at each step to suppress the exponential amplification of scalar floating-point drift in a homogeneous quadratic evaluation. The largest mass error before this correction was $1.12\times10^{-15}$, and the largest observed majorisation violation after correction was below $6.7\times10^{-16}$. These observations are diagnostics; the rational coefficient and cycle certificates are the rigorous verification.

The table gives the smallest lag $1\leq q\leq48$ for which every applicable difference in the final 96 iterates is below $10^{-8}$ in the maximum norm. A label 0 means unresolved at this finite horizon. A finite small residual does not prove periodicity, convergence, or a rate; exact verification is supplied separately for the constructed cycles.

| m | family | operators (unique) | starts | tail period counts |
|---:|---|---:|---:|---|
| 3 | all_m3_extremes | 222 (222) | 3552 | 0: 1, 1: 3227, 2: 240, 3: 84 |
| 3 | affine_permutation_random | 24 (24) | 384 | 1: 341, 2: 25, 3: 18 |
| 3 | convex_random | 12 (11) | 192 | 1: 192 |
| 3 | permutation_controls | 4 (2) | 64 | 1: 49, 3: 15 |
| 4 | latin_extremes | 24 (19) | 408 | 1: 388, 2: 20 |
| 4 | affine_permutation_random | 24 (24) | 408 | 1: 363, 2: 26, 3: 7, 4: 12 |
| 4 | convex_random | 12 (12) | 204 | 1: 204 |
| 4 | permutation_controls | 4 (4) | 68 | 1: 8, 2: 14, 3: 30, 4: 16 |
| 4 | nonlinear_extreme_counterexample | 1 (1) | 18 | 1: 1, 2: 17 |
| 5 | latin_extremes | 24 (23) | 432 | 1: 342, 2: 40, 3: 24, 4: 16, 5: 10 |
| 5 | affine_permutation_random | 24 (24) | 432 | 1: 372, 2: 29, 3: 26, 4: 5 |
| 5 | convex_random | 12 (12) | 216 | 1: 216 |
| 5 | permutation_controls | 4 (4) | 72 | 1: 11, 2: 46, 3: 3, 6: 12 |
| 5 | nonlinear_extreme_counterexample | 1 (1) | 19 | 0: 1, 1: 2, 2: 16 |
| 6 | latin_extremes | 24 (24) | 456 | 1: 412, 2: 44 |
| 6 | affine_permutation_random | 24 (24) | 456 | 1: 384, 2: 52, 3: 4, 4: 16 |
| 6 | convex_random | 12 (12) | 228 | 1: 228 |
| 6 | permutation_controls | 4 (4) | 76 | 1: 10, 2: 4, 3: 18, 4: 32, 6: 12 |
| 6 | nonlinear_extreme_counterexample | 1 (1) | 20 | 1: 3, 2: 17 |

The two initially unresolved trajectories were rerun for 65,536 steps. The three-type case then had lag 1 residual $5.22\times10^{-15}$, and the five-type targeted case had lag 2 residual zero in double precision. `data/followup.json` records the results. They are slow transients and do not contradict the exact phase-convergence theorems. Periods greater than one in the $m=3$ rows include boundary starts and permutation operators; they do not contradict Theorem 3.2.

`code/polytope_probe.py` separately optimises one-step majorisation objectives over the necessary outer polytopes. It finds no positive violation in its 100 three-type objectives; already the second objective in each of $m=4,5,6$ finds positive violations. The recorded floating violations are approximately $0.00361591,0.00797342,0.02546633$, respectively. This search is not used to certify full-class operators. Its four-type tensor was rationalised without error and rechecked exactly in (19)–(20). The probe's HiGHS solver receives a one-thread option; its warning that the option is passed through to HiGHS is harmless and retained in the log.

The data files contain all sampled tensors (`operators.npz`), every initial point and tail result (`trajectory_details.json`), the exact cycles, outer constraints and the complete three-type vertex list. `code/audit.py` independently checks the stored rational certificates and the key identities, including the two-cycle multipliers and equality loss.

## 7. Literature audit through 13 November 2026

The search included the named authors and the terms “bistochastic”, “doubly stochastic”, “quadratic stochastic”, “ergodic”, “periodic” and “extreme”. The following distinctions determine the interpretation of the result.

- [Shahidi, *Doubly stochastic operators on a finite-dimensional simplex*, Siberian Mathematical Journal 50 (2009), 368–372](https://doi.org/10.1007/s11202-009-0042-3) is explicitly cited by the 2016 paper as the earlier ergodicity result. The publisher metadata was checked; its full text was not retrieved. Theorem 1 above is proved independently.
- [Abdulghafor–Shahidi–Zeki–Turaev (2016)](https://doi.org/10.1515/math-2016-0045), checked in full HTML, proves the interior non-permutation result on the two-simplex and gives, in Example 3.9, the linear map $((x_2+x_4)/2,(x_1+x_3)/2,(x_2+x_4)/2,(x_1+x_3)/2)$, with immediate or eventual two-cycles. Thus higher-dimensional counterexamples were already part of the user's cited source.
- [Saburov, *Dynamics of Double Stochastic Operators* (2016)](https://doi.org/10.1088/1742-6596/697/1/012014) gives regularity iff absence of nontrivial periodic points for continuous bistochastic maps. The theorem statement and proof were located in the author-uploaded text; Makhmudov also cites it. The publisher PDF could not be downloaded in this environment.
- [Saburov (2017)](https://doi.org/10.1007/s00025-017-0723-3) treats diagonal positivity; [Saburov (2018)](https://doi.org/10.1134/S0001434618010376) treats positive quadratic doubly stochastic operators. Publisher pages were checked. These additional hypotheses do not apply to the sparse counterexamples (5).
- [Makhmudov, preprint 2020, revised 2021](https://arxiv.org/abs/2001.10444), [published in 2021](https://doi.org/10.5890/DNC.2021.09.006), recalls finiteness of limit sets in Theorem 2.1 and the periodic-point criterion in Theorem 2.2. Theorem 3.3 treats strict regularity in the relative interior of the operator class. The complete preprint is saved in `sources/`; the publisher page was also checked. No claim of novelty for the general finite-cycle mechanism is supportable.
- [Zhang–Yang (2016)](https://doi.org/10.1007/s11464-016-0533-z) concerns extreme $U_1$ matrices and structural characterisations. The publisher abstract was checked, but the full paper could not be retrieved. It is not used as a complete higher-dimensional classification.
- [Jamilov–Mukhamedov–Mukhamedova–Souissi (2024)](https://doi.org/10.1002/mma.10191), checked in publisher HTML, concerns a particular regular class of nonlinear stochastic operators and associated Markov measures. It does not assert universal regularity of the present majorisation-defined class.
- [Saburov–Saburov–Saburov (2025)](https://doi.org/10.1007/978-3-032-09176-5_10), publisher abstract and references checked, studies global stability under a column-primitivity assumption on cubic doubly stochastic matrices. The full chapter was not retrieved; its exact tensor convention and hypotheses are not assumed here.
- [Azman–Wan Rozali–Mukhamedov (2026)](https://doi.org/10.11113/mjfas.v22n1.4643), checked through its journal search record and university publication page, concerns **b-bistochastic** operators and associated chains on a one-dimensional simplex. The fixed-coordinate $b$-order differs from sorted majorisation. Likewise [Saburov's 2026 historic-behaviour paper](https://doi.org/10.7868/S3034504926050134) concerns an infinite-dimensional simplex. Neither supplies a non-ergodic orbit in the finite-dimensional class studied here.
- [Shahidi–Ganikhodzhaev, arXiv:1211.5639](https://arxiv.org/abs/1211.5639) is explicitly withdrawn as of its 2018 revision. Its abstract about convergence to the centre must not be treated as an established theorem.

These checks establish that universal convergence and universal ergodicity are not unresolved alternatives as phrased in the task. They do not establish priority for every formulation in this report. No assertion is made that all relevant papers in 2016–2026 have been exhaustively retrieved.

## 8. What remains unresolved in this packet

The convergence question has a negative answer even among genuinely nonlinear extreme operators for every $m\geq4$. The Cesàro question has a positive answer for every finite $m$, with the stronger phase-convergence description in Theorem 1. A non-ergodic finite-dimensional bistochastic QSO therefore cannot exist.

The requested exhaustive higher-dimensional coefficient and extreme-point classification is unfinished. The report gives an exact copositivity parametrisation and concrete extreme families, but no full vertex count or list for $\mathcal B_4,\mathcal B_5$, no proof of their general polyhedrality, and no completeness claim for the parametrisation (21). Sharp maximal possible least periods and an efficient coefficient criterion deciding regularity throughout the full higher-dimensional class are not determined here. Theorem 4.2 supplies a finite exact periodic-point procedure for a given rational certified operator, with no claim of computational efficiency.

Task: “Open problem E0066: trajectories of bistochastic (doubly stochastic) quadratic stochastic operators” — 13 November 2026, approximately 01:35 Asia/Tbilisi; first recorded shell clock 01:36.
