# Fixed-radius bounds on vacant straight segments

Let d >= 2, lambda > 0 and r > 0 be fixed. Let Pi be a homogeneous Poisson process of intensity lambda on R^d. Write

\[
\mathcal O=\bigcup_{z\in\Pi}\overline B(z,r),\qquad
V=\mathbb R^d\setminus\mathcal O,\qquad
\kappa_j=\frac{\pi^{j/2}}{\Gamma(1+j/2)},\qquad
a=\lambda\kappa_{d-1}r^{d-1}.
\]

The union defining O is locally finite almost surely, and therefore closed. For R > 0 define

\[
M_R=\sup\bigl(\{0\}\cup\{|x-y|:x,y\in\overline B(0,R),\ [x,y]\subset V\}\bigr).
\]

The ball is convex, so every segment in this definition lies in the ball. This is a measurable random variable: every compact segment in the open set V has positive distance from O; approximating its endpoints by rational points inside the ball preserves vacancy and approximates its length. Thus the same supremum can be taken over a countable family of rational endpoint pairs.

The maximum is over the whole vacant set. No percolation assumption is made here.

## Finite-scale bounds

For L > 0, let

\[
A=2R/\sqrt d,\qquad
N(R,L)=\left\lfloor\frac{A}{L+3r}\right\rfloor
        \left\lfloor\frac{A}{3r}\right\rfloor^{d-1},
\qquad
p(L)=\exp\{-\lambda\kappa_dr^d-aL\}.
\]

Then

\[
\mathbb P(M_R<L)\le (1-p(L))^{N(R,L)}
                       \le \exp\{-N(R,L)p(L)\}.                 \tag{1}
\]

For 0 < eta < r and L >= eta, put

\[
K_d=d\,2^d(5/4)^{d-1},\qquad
U(R,L,\eta)=
\left(\frac{2R\sqrt d}{\eta}+3\right)^d
K_d\left(\frac{2L}{\eta}\right)^{d-1}
\exp\{-\lambda\kappa_d(r-\eta)^d
       -\lambda\kappa_{d-1}(r-\eta)^{d-1}L\}.
\]

Then

\[
\mathbb P(M_R>L)\le \min\{1,U(R,L,\eta)\}.                  \tag{2}
\]

### Sausage volume and the Poisson void formula

For a segment S of length L and s > 0, its closed s-neighborhood is a cylinder of length L and (d-1)-dimensional cross-section volume kappa_(d-1) s^(d-1), together with two hemispherical caps. Their interiors are disjoint. Consequently

\[
|S+\overline B(0,s)|=\kappa_{d-1}s^{d-1}L+\kappa_ds^d.       \tag{3}
\]

The segment S is contained in V exactly when Pi has no point in its closed r-neighborhood. A Poisson count in a deterministic measurable set E of finite volume has mean lambda |E| and probability exp(-lambda |E|) of being zero. Applying this fact to (3) gives p(L). Boundaries of these deterministic sausages have zero volume.

### Proof of (1)

The cube Q=[-R/sqrt(d),R/sqrt(d)]^d is contained in the closed ball of radius R. Starting from its lower corner, place a rectangular array of cells, of side length L+3r in the first coordinate and 3r in all other coordinates. Use floor(A/(L+3r)) cells in the first direction and floor(A/(3r)) in each other direction. There are N(R,L) cells.

In each cell choose a length L segment parallel to the first coordinate. Its initial first coordinate is 3r/2 beyond the cell's lower first face; its other coordinates are at the centers of their respective intervals. Its closed r-neighborhood stays at least r/2 from every face of the cell: in the first coordinate the neighborhood occupies [r/2,L+5r/2] relative to the lower face, and in each other coordinate it occupies [r/2,5r/2]. Thus these neighborhoods are pairwise disjoint and all segments lie in Q.

The corresponding Poisson void events are independent, each with probability p(L). If any occurs, M_R >= L. Hence {M_R<L} implies failure of all N events and has probability at most (1-p(L))^N. The inequality 1-u <= exp(-u) for 0 <= u <= 1 proves (1), also when N=0.

### Proof of (2)

First construct two deterministic nets. A cubic lattice of spacing h=eta/sqrt(d) has a nearest point q within distance eta/2 of every x. For x in the ball of radius R each coordinate of q lies between -R-h/2 and R+h/2. The number of such lattice points is at most

\[
(2R/h+3)^d=(2R\sqrt d/\eta+3)^d.                           \tag{4}
\]

Set alpha=eta/(2L) <= 1/2. Take a maximal alpha-separated collection D on the unit sphere, using Euclidean distance. Its alpha-neighborhood covers the sphere. The open Euclidean balls of radius alpha/2 around its points are disjoint and lie in the shell with radii 1-alpha/2 and 1+alpha/2. Therefore

\[
|D|(\alpha/2)^d
\le (1+\alpha/2)^d-(1-\alpha/2)^d
\le d\alpha(1+\alpha/2)^{d-1}
\le d\alpha(5/4)^{d-1}.
\]

The middle bound follows by integrating the derivative d t^(d-1) over that interval. Thus

\[
|D|\le K_d\alpha^{1-d}=K_d(2L/\eta)^{d-1}.                 \tag{5}
\]

Such a finite maximal collection exists by the same packing bound: greedily adding points must terminate after finitely many additions.

Suppose M_R > L. Some vacant segment contains a subsegment S={x+tu:0<=t<=L}, with x in the ball and |u|=1. Choose a lattice point q with |q-x|<=eta/2 and v in D with |v-u|<=alpha. For S'={q+tv:0<=t<=L},

\[
|(q+tv)-(x+tu)|\le\eta/2+L\alpha=\eta.                    \tag{6}
\]

If a Poisson center z were at distance at most r-eta from S', then (6) would place it at distance at most r from S. This contradicts S being contained in V. Hence the closed (r-eta)-neighborhood of S' is empty of centers.

For each deterministic pair (q,v), the probability of this emptiness event is the exponential in U, by (3). A union bound over (4) and (5) proves (2). No independence of the net events is used. In particular, the direction of the original segment may depend arbitrarily on the environment.

## Sharp almost-sure asymptotic

For all fixed lambda,r > 0 and d >= 2,

\[
\boxed{\displaystyle
\lim_{R\to\infty}\frac{M_R}{\log R}
     =\frac{d}{\lambda\kappa_{d-1}r^{d-1}}
\quad\text{almost surely}.}                              \tag{7}
\]

Take first c > d/a. Since lambda kappa_(d-1)(r-eta)^(d-1) increases to a as eta decreases to zero, choose fixed eta in (0,r) such that

\[
b=\lambda\kappa_{d-1}(r-\eta)^{d-1},\qquad bc>d.
\]

For R_n=2^n and L_n=c log R_n, (2), for sufficiently large n, gives

\[
\mathbb P(M_{R_n}>c\log R_n)
\le C R_n^{d-bc}(\log R_n)^{d-1}
\le C'2^{-n(bc-d)}n^{d-1}.
\]

The constants depend only on fixed parameters and c,eta. The series converges. The first Borel--Cantelli lemma gives M_(R_n)<=c log R_n eventually, almost surely. For R_n<=R<=R_(n+1), monotonicity yields

\[
\frac{M_R}{\log R}\le
\frac{M_{R_{n+1}}}{\log R_n}
\le c\frac{n+1}{n}
\]

eventually. Taking c through a countable sequence decreasing to d/a proves limsup <= d/a.

For the reverse bound fix 0 < c < d/a, use the same R_n and L_n, and write delta=d-ac>0. If x>=2, floor(x)>=x/2. Since R/log R tends to infinity, both floor arguments in N(R,c log R) eventually exceed 2. Thus

\[
N(R,c\log R)\ge
\frac{(2R/\sqrt d)^d}{2^d(c\log R+3r)(3r)^{d-1}}
\ge C\frac{R^d}{\log R},                                  \tag{8}
\]

where C>0 and R is sufficiently large. Also p(c log R)=exp(-lambda kappa_d r^d) R^(-ac). Equation (1) consequently gives

\[
\mathbb P(M_{R_n}<c\log R_n)
\le\exp\{-C'R_n^{\delta}/\log R_n\}.
\]

This is summable: 2^(n delta)/n eventually exceeds n, so its terms are eventually bounded by a summable exponential in n. Borel--Cantelli gives M_(R_n)>=c log R_n eventually. For R_n<=R<=R_(n+1),

\[
\frac{M_R}{\log R}\ge
\frac{M_{R_n}}{\log R_{n+1}}\ge c\frac{n}{n+1}.
\]

A countable sequence c increasing to d/a proves liminf >= d/a and completes (7). All uses of Borel--Cantelli are its first, independence-free implication.

## Consequence for billiard flights

Consider any well-defined unit-speed billiard path X starting at the origin in V. Let G(T) be the supremum of the lengths of its collision-free time intervals contained in [0,T]. The speed bound gives |X(t)|<=t<=T. In the interior of each free interval, X traces a straight segment in V. Trimming an arbitrarily small time from each end produces a compact segment counted by M_T. Taking the supremum over these trimmed segments proves

\[
G(T)\le M_T,\qquad
\limsup_{T\to\infty}\frac{G(T)}{\log T}\le\frac d a.         \tag{9}
\]

The probability-one environment event in (7) works simultaneously for all such paths and directions. If the path has a finite number N_X(T) of collisions on each bounded time interval, its at most N_X(T)+1 free intervals partition [0,T]. Their lengths sum to T, whence

\[
T\le(N_X(T)+1)G(T)\le(N_X(T)+1)M_T,
\qquad
\liminf_{T\to\infty}\frac{N_X(T)\log T}{T}\ge\frac a d.     \tag{10}
\]

This corollary assumes the indicated regular billiard path exists; it does not establish almost-everywhere global existence at singular boundary configurations.

For conditioning, let H={0 lies in an unbounded component of V} and suppose theta=P(H)>0. Every probability-one environment statement above also has probability one under P(.|H), since P(E^c|H)<=P(E^c)/theta=0. Every finite-scale upper bound transfers with an additional factor theta^(-1). In particular (9)--(10) hold under this conditional law. The lower bound in (7) still concerns all of V: the independently constructed vacant segments need not belong to the component containing the origin. No matching lower bound for G(T) is claimed.

These geometric estimates do not control correlations between successive collisions, prove a central limit theorem, or prove planar recurrence.

## Relation to existing visibility results

Yingxin Mu and Artem Sapozhnikov, *On the maximum visibility in a ball through the vacant set of Poissonian obstacles*, [arXiv:2609.11690v1](https://arxiv.org/abs/2609.11690v1), Theorem 1.1 and Remark 1.2, include the constant in (7) and deviation estimates which imply its almost-sure fixed-radius specialization. The proof above uses only Poisson void probabilities, deterministic nets, and independent disjoint sausages. No novelty over that paper is claimed for (7).
