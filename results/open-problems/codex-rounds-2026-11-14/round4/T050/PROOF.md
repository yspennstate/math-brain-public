# A finite-range potential for approximately local increments

Let \((\eta_z)_{z\in\mathbb Z^d}\) be independent random elements on a
probability space. Other randomness may be present on that space. For a
finite set \(I\), write \(\mathcal F_I=\sigma(\eta_z:z\in I)\), with
\(\mathcal F_\varnothing\) trivial, and set
\[
 Q_a(z)=\{u\in\mathbb Z^d:\|u-z\|_\infty\le a\}.
\]
All norms on random variables below are \(L^1\) norms.

## Theorem

Fix \(d\ge2\), an integer \(H\ge2\), and a label set \(\Lambda\) with a
distinguished element \(0\). Suppose \(V_{z,\lambda}\) is integrable for
each \(z,\lambda\). Assume that for every ordered pair
\((z,\lambda),(z',\lambda')\) with \(\|z'-z\|_1\le1\), there is an
integrable \(\mathcal F_{Q_H(z)}\)-measurable random variable \(E\) such that
\[
 \|E-(V_{z',\lambda'}-V_{z,\lambda})\|_1\le\varepsilon.       \tag{1}
\]
The case \(z'=z\) is included, so (1) includes changes of label at one site.

Put
\[
\begin{split}
 m&=(2H+1)^d, & R&=3H+1, & L&=R+2H=5H+1,\\
 N&=(2R+1)^d\,2^{(4H+1)^d},
 &J&=(d+3)R+2,
 &C_{d,H}&=2+2NJ2^m.
\end{split}                                                   \tag{2}
\]
Then there are integrable \(\mathcal F_{Q_L(z)}\)-measurable variables
\(g_{z,\lambda}\) with
\[
 \mathbb E g_{z,\lambda}=\mathbb E V_{z,\lambda},\qquad
 \|g_{z',\lambda'}-g_{z,\lambda}
       -V_{z',\lambda'}+V_{z,\lambda}\|_1
       \le C_{d,H}\varepsilon.                              \tag{3}
\]
The radius and error constant are independent of the label set and of the
number or distribution of variables inside each cell.

The construction also preserves translation covariance. More precisely,
suppose there are invertible measure-preserving shifts \(\theta_a\) with
\(\eta_z\circ\theta_a=\eta_{z+a}\), all increments of \(V\) commute with
these shifts, and \(\mathbb EV_{z+a,\lambda}=\mathbb EV_{z,\lambda}\).
Then versions of the gauges satisfy
\(g_{z+a,\lambda}=g_{z,\lambda}\circ\theta_a\) almost surely for each
fixed collection of indices and labels.

## Proof

### Finite projections

For each nonempty finite \(S\subset\mathbb Z^d\) and each integrable \(F\),
define
\[
 \Pi_S F=\sum_{I\subset S}(-1)^{|S|-|I|}
                    \mathbb E[F\mid\mathcal F_I].             \tag{4}
\]
Every term is \(\mathcal F_S\)-measurable. Conditional expectation is an
\(L^1\) contraction, so
\[
 \|\Pi_S F\|_1\le2^{|S|}\|F\|_1,\qquad \mathbb E\Pi_S F=0.    \tag{5}
\]
If \(F\) is \(\mathcal F_A\)-measurable for a finite \(A\), independence
gives
\(\mathbb E[F\mid\mathcal F_I]=\mathbb E[F\mid\mathcal F_{I\cap A}]\).
When \(S\not\subset A\), choose a point of \(S\setminus A\). Pairing each
subset not containing that point with the subset containing it cancels (4).
Consequently
\[
 \Pi_S F=0\quad(S\not\subset A).                              \tag{6}
\]
For finite \(A\), summing (4) over all \(S\subset A\), including the empty
set with \(\Pi_\varnothing F=\mathbb EF\), leaves only
\(\mathbb E[F\mid\mathcal F_A]\). Indeed, the coefficient of
\(\mathbb E[F\mid\mathcal F_I]\) is
\(\sum_{I\subset S\subset A}(-1)^{|S|-|I|}\), which is zero unless
\(I=A\). In particular, if \(F\) is \(\mathcal F_A\)-measurable, then
\[
 F-\mathbb EF=\sum_{\varnothing\ne S\subset A}\Pi_S F.         \tag{7}
\]
These are finite identities in \(L^1\); no expansion of a nonlocal variable
over infinitely many sets is required.

### Construction and locality

Let \(\mathscr S\) consist of the nonempty finite sets \(S\) satisfying
\(|S|\le m\) and \(\operatorname{diam}_\infty S\le2H\). Let \(k(S)\) be
the lexicographically least point of \(S\), and set
\[
 U_S=Q_R(k(S)),\qquad a(S)=k(S)+(R+1)e_1.
\]
Define
\[
 g_{z,\lambda}=\mathbb EV_{z,\lambda}
  +\sum_{\substack{S\in\mathscr S\\z\in U_S}}
       \Pi_S\big(V_{z,\lambda}-V_{a(S),0}\big).                \tag{8}
\]
For fixed \(z\), the possible \(k(S)\) belong to \(Q_R(z)\). Each
\(S\) is contained in \(Q_{2H}(k(S))\). There are at most
\((2R+1)^d\) possible first points and at most \(2^{(4H+1)^d}\) subsets
for each. Thus (8) has at most \(N\) terms. Every such \(S\) lies in
\(Q_{R+2H}(z)\), so (4) proves the required locality, even though the
variables inside the projection may be nonlocal. Integrability follows
from the finite sum and (5), and its expectation is \(\mathbb EV_{z,\lambda}\).

### The boundary estimate

Suppose \(u\in U_S\) has a nearest neighbor outside \(U_S\). Then
\(\|u-k(S)\|_\infty=R\). There is a nearest-neighbor path from \(u\) to
\(a(S)\) with at most \((d+3)R+1\) steps such that every departure site
\(b\) satisfies \(\|b-k(S)\|_\infty\ge R\).

Here is an explicit path, after translating \(k(S)\) to zero. If an extreme
coordinate of \(u\) has index \(j\ne1\), hold that coordinate fixed while
moving coordinate 1 to \(R\), at cost at most \(2R\). Hold coordinate 1
fixed and set all other coordinates to zero, at cost at most \((d-1)R\).
If \(u_1=R\), only the latter moves are needed. The remaining case has
\(u_1=-R\). First set coordinate 2 to \(R\), at cost at most \(2R\);
then set coordinate 1 to \(R\), at cost \(2R\); then set the other
coordinates to zero, at cost at most \((d-1)R\). These operations remain
on the cube boundary. Finally take one step from \(Re_1\) to
\((R+1)e_1\). This proves the length and location claims and uses \(d\ge2\).

Every \(S\in\mathscr S\) lies in \(Q_{2H}(k(S))\). For a departure site
\(b\) on the constructed path,
\[
 \|b-k(S)\|_\infty-H\ge R-H=2H+1>2H,
\]
so \(Q_H(b)\cap S=\varnothing\). The same holds at \(u\).
Make an initial label change from \(\lambda\) to \(0\) at \(u\), followed
by the path with label \(0\). There are at most \(J\) comparisons in all.
Each local comparison has zero \(\Pi_S\) projection by (6), and each
error in (1) has projection norm at most \(2^m\varepsilon\). Telescoping
the true increments therefore gives
\[
 \big\|\Pi_S(V_{u,\lambda}-V_{a(S),0})\big\|_1
        \le J2^m\varepsilon.                               \tag{9}
\]
The sign introduced by reversing the telescoped difference has no effect
on this estimate. A label change is unnecessary if \(\lambda=0\).

### Recovery of each increment

Fix a pair in (1), write
\(W=V_{z',\lambda'}-V_{z,\lambda}\), and choose its local comparison
\(E\). Let
\[
 \mathscr A_z=\{S\in\mathscr S:z\in U_S\},\quad
 \mathscr B=\mathscr A_z\cap\mathscr A_{z'},\quad
 \mathscr D=\mathscr A_z\mathbin\triangle\mathscr A_{z'}.
\]
Each nonempty \(S\subset Q_H(z)\) belongs to \(\mathscr B\). It has at
most \(m\) points and diameter at most \(2H\), while its first point has
distance at most \(H\) from \(z\) and at most \(H+1\le R\) from \(z'\).
It follows from (6) and (7) that
\[
 \sum_{S\in\mathscr B}\Pi_SE=E-\mathbb EE.                  \tag{10}
\]
Subtract the two instances of (8). A set in \(\mathscr B\) contributes
\(\Pi_SW\), because the reference term cancels. A set in \(\mathscr D\)
contributes, with a sign, one boundary term from (9). Indeed its included
endpoint has a nearest neighbor outside \(U_S\); if \(z'=z\), there are
no such sets. Thus
\[
\begin{split}
 &(g_{z',\lambda'}-g_{z,\lambda})-W\\
 &\quad=\mathbb EW+E-\mathbb EE-W
       +\sum_{S\in\mathscr B}\Pi_S(W-E)
       +\sum_{S\in\mathscr D}\text{signed boundary term}.     \tag{11}
\end{split}
\]
The first term on the right is \((E-W)-\mathbb E(E-W)\), whose norm is
at most \(2\varepsilon\). Each summand in the second sum is bounded by
\(2^m\varepsilon\), and each in the last sum by
\(J2^m\varepsilon\). The union of the two endpoint families has at most
\(2N\) members. Since \(J\ge1\), (11) is bounded by
\((2+2NJ2^m)\varepsilon\), proving (3).

For covariance, translating \(S\) translates its lexicographic first point,
cutoff cube and reference site. Measure preservation gives
\(\Pi_{S+a}(F\circ\theta_a)=(\Pi_SF)\circ\theta_a\).
Apply this identity to the differences in (8), using the assumed covariance
of those differences and invariance of their deterministic means. This
proves the covariance assertion.

## Independent checks and the dimension restriction

There is a second verification of the projection identities. On functions
of a finite collection of independent cells, let \(A_i\) integrate out
coordinate \(i\). The operators commute, and each has norm at most one.
The identity
\[
 \prod_{i\in A}\big(A_i+(I-A_i)\big)=I
\]
expands into (7). A term indexed by \(S\subset A\) is exactly (4), since
it integrates out \(A\setminus S\) and centers each coordinate in \(S\).
An extra coordinate outside the support is killed by its centering factor.
This verifies both the support cancellation and the norm bound \(2^{|S|}\)
without the subset-pairing proof.

The geometric clearance also follows from distance between sets:
\[
 \operatorname{dist}_\infty\big(b,Q_{2H}(k(S))\big)
      \ge R-2H=H+1.
\]
Thus a radius-\(H\) support cannot meet \(S\). Both calculations give
one lattice unit of strict clearance. Counting the moves separately gives
\(2R+2R+(d-1)R+1\) spatial steps in the worst case, and one label change,
which is precisely \(J\). Finally (11) counts each set once: members of
\(\mathscr B\) and \(\mathscr D\) partition the endpoint union. There is
no factor depending on how many labels exist.

The assertion with fixed finite locality radius cannot hold on \(\mathbb Z\).
Let \((\xi_i)_{i\in\mathbb Z}\) be independent symmetric signs and define
\[
 V_0=0,\qquad V_n=\sum_{i=1}^n\xi_i\ (n>0),\qquad
 V_n=-\sum_{i=n+1}^0\xi_i\ (n<0).
\]
Then \(V_{n+1}-V_n=\xi_{n+1}\), which is measurable in \(Q_H(n)\) for
\(H\ge1\). Thus the local approximation error is exactly zero.
If finite-radius gauges had exactly these increments, choose an integer
\(N_0>2L+2\) and an index \(j\) with \(L<j<N_0-L\). Locality and
independence would give
\[
 \mathbb E[(g_{N_0}-g_0)\xi_j]=0.
\]
Telescoping the required increments instead gives
\[
 \mathbb E[(g_{N_0}-g_0)\xi_j]
       =\mathbb E\left[\left(\sum_{i=1}^{N_0}\xi_i\right)\xi_j\right]=1,
\]
a contradiction. Products are integrable because \(\xi_j\) is bounded.
Even if only positive \(\varepsilon\) are allowed in a proposed theorem,
the same example defeats a fixed constant \(C\): telescoping errors bounded
by \(C\varepsilon\) would give \(1\le N_0C\varepsilon\), impossible for
sufficiently small \(\varepsilon\). This does not assume stationarity of
the proposed gauges.

## Relation to first-passage percolation

This proves the finite-cell localization step used in Lemma 10.2 of OpenAI,
*Strict convexity and differentiability of the planar exponential
first-passage limit shape* (September 24, 2026),
[manuscript](https://mathcommunity.github.io/oai-math-revised/papers/Strict-convexity-and-differentiability-of-the-planar-exponential-first-passage-limit-shape-September-24-2026/main.pdf).
In two dimensions the locality radius here is \(5H+1\), compared with
\(10H+20\) there. The result also permits every \(d\ge2\).
The constants are not optimized. All estimates are for each specified
increment; they do not give a supremum over arbitrary labels. No road
geometry in higher dimensions, contraction estimate, or strict-convexity
theorem follows from this lemma alone.
