# Finite polynomial certificates for complete bipartite graphs

## Statement and scope

The exact integer certificates below verify the following proposition for

\[
G\in\{K_{3,3},K_{3,4},K_{4,4},K_{5,5}\}.
\]

Fix distinct edges \(e,f\). Give \(e\) activity \(x>0\), give \(f\) activity
\(y>0\), and give every other edge the same activity \(w>0\). Under the
random-cluster measure

\[
\mu(S)=Z^{-1}q^{k(S)}\prod_{g\in S}x_g,
\qquad 0<q<1,
\]

the indicators of \(e\) and \(f\) have strictly negative covariance.
The same strict inequality holds for the weighted forest measure and the
weighted connected-spanning-subgraph measure with these activities.
At \(q=1\) the covariance is zero.

In particular, taking \(x=y=w\) gives pairwise negative correlation for
each of these measures with a common activity on every edge. The assertion
with two exceptional activities concerns the specified pair \(e,f\).
It does not assert pairwise negative correlation for every pair under an
arbitrary assignment of activities to all edges.

This is a finite computer-assisted verification. The coefficient lists
are in `extended_certificates.json`; the independent audit is
`verify_certificates.py`. No assertion for unbounded part sizes follows.

## 1. The four sectors and the covariance

Put \(N=|V(G)|\). For \(i,j\in\{0,1\}\), define

\[
S_{ij}(q,w)=\sum_{\substack{U\subseteq E(G)\\
 {\bf1}_{e\in U}=i,\ {\bf1}_{f\in U}=j}}
 q^{k(U)}w^{|U|-i-j}.
\]

Write \(A=S_{00}, B=S_{10}, C=S_{01}, D=S_{11}\). Then

\[
Z=A+xB+yC+xyD.
\]

The probabilities of \(e\), \(f\), and their joint inclusion are

\[
\mu(e)=\frac{x(B+yD)}Z,\quad
\mu(f)=\frac{y(C+xD)}Z,\quad
\mu(e,f)=\frac{xyD}Z.
\]

Multiplying and subtracting gives exactly

\[
\mu(e)\mu(f)-\mu(e,f)=\frac{xy}{Z^2}(BC-AD).       \tag{1}
\]

Thus only the sign of \(\Delta=BC-AD\) needs checking. In particular its
sign is independent of the two marked activities \(x,y\).

Label the left vertices \(0,\ldots,m-1\) and the right vertices
\(0,\ldots,n-1\), and take \(e=(0,0)\). There are three possible pair
types: \(f=(0,1)\), \(f=(1,0)\), and \(f=(1,1)\). Independent permutations
within the two parts carry every distinct pair to one of these. A
transposition of the two parts identifies the first two types when \(m=n\).
All three types were nevertheless computed in every case.

## 2. Exact computation of the sectors

The first enumeration visits every edge subset and counts its connected
components by union-find. For the three smaller graphs this visits at most
\(2^{16}\) subsets per pair type. A second enumeration uses the following
vertex-subset recurrence and agrees coefficient by coefficient.

For a nonempty vertex set \(T\), let \(c_T(w)\) count connected spanning
subgraphs of the induced graph, and let

\[
a_T(w)=(1+w)^{|E(G[T])|}.
\]

Fix a vertex \(v\in T\). Decomposing a subgraph according to the component
\(U\) containing \(v\) yields

\[
c_T=a_T-\sum_{\substack{v\in U\subsetneq T}} c_Ua_{T\setminus U}.
                                                        \tag{2}
\]

Indeed, all crossing edges between \(U\) and its complement are absent;
the graph on \(U\) is connected and the graph on the complement is arbitrary.
Every disconnected subgraph is counted exactly once in the sum.
Consequently the complete random-cluster polynomial on a vertex set obeys

\[
Z_\varnothing=1,\qquad
Z_T=\sum_{\substack{v\in U\subseteq T}}q c_U Z_{T\setminus U}.       \tag{3}
\]

Apply (2)–(3) to each of \(G,G-e,G-f,G-\{e,f\}\), temporarily giving
every available edge activity \(w\). Inclusion-exclusion gives

\[
\begin{split}
A&=Z_{G-\{e,f\}},\\
B&=(Z_{G-f}-A)/w,\\
C&=(Z_{G-e}-A)/w,\\
D&=(Z_G-Z_{G-e}-Z_{G-f}+A)/w^2.
\end{split}                                                     \tag{4}
\]

The divisions are exact because their numerators count subgraphs containing
the corresponding marked edges.

For \(K_{5,5}\), a transfer on partitions of the left vertices replaces
edge-subset enumeration. Initially the five left vertices are separate
blocks. For each new right vertex choose its neighbor subset \(T\).
If \(T\) is empty, this right vertex is an isolated component, giving a
factor \(q\). Otherwise merge all current left blocks meeting \(T\).
Record selected marked edges by two bits and selected unmarked edges by
their number. At the end multiply by \(q\) for each remaining left block.
Every edge subset has a unique sequence of neighbor subsets; its final
components are precisely those left blocks and the isolated right vertices.
Thus this transfer computes exactly \(A,B,C,D\). Its coefficients agree
with (2)–(4) for every pair type.

A third count of the \(K_{5,5}\) sectors is used in the independent verifier.
For a partition \(\pi\) of the left vertices into \(b\) nonempty blocks, put
\((q)_b=q(q-1)\cdots(q-b+1)\). Then

\[
Z_G(q,\boldsymbol{x})=
\sum_{\pi}(q)_{|\pi|}
\prod_{r\in R}\left(q-|\pi|+
       \sum_{T\in\pi}\prod_{\ell\in T}(1+x_{\ell r})\right).       \tag{5}
\]

To prove (5), first let \(q\) be an integer at least \(m\). Expand
\(\sum_\sigma\prod_{uv}(1+x_{uv}{\bf1}_{\sigma(u)=\sigma(v)})\)
over edge subsets: a subset contributes its weight times \(q^{k(U)}\),
since each component must receive one color. Alternatively, partition left
vertices by equality of their colors. There are \((q)_b\) assignments of
distinct colors to its \(b\) blocks. For a right vertex, choosing one of
these colors gives the corresponding block product, while each of the
\(q-b\) unused colors gives weight one. Right vertices can then be summed
independently, proving (5) for these integers. Both sides are polynomials
in \(q\), so equality for infinitely many integers proves the identity.

There are 52 left partitions when \(m=5\). Substituting the two marked
activities and the common activity into (5), and extracting the four
marked coefficients, gives the same sectors as both previous methods.

## 3. The positive polynomial identities

For every computed case, exact multiplication and division give

\[
\Delta(q,w)=q^2w^2(1-q)H(q,w).
\]

Set \(d=2N-6\), and define the integer polynomial

\[
P(t,w)=(1+t)^dH\left(\frac{t}{1+t},w\right).                  \tag{6}
\]

The computation verifies that every nonzero coefficient of \(P\) is
positive. It also checks its degree and the following support information.

| Graph | Pair type | \(d\) | Nonzero coefficients | Minimum nonzero coefficient |
|---|---|---:|---:|---:|
| \(K_{3,3}\) | Adjacent, either side | 6 | 63 | 1 |
| \(K_{3,3}\) | Disjoint | 6 | 56 | 1 |
| \(K_{3,4}\) | Common left vertex | 8 | 117 | 1 |
| \(K_{3,4}\) | Common right vertex | 8 | 126 | 1 |
| \(K_{3,4}\) | Disjoint | 8 | 108 | 1 |
| \(K_{4,4}\) | Adjacent, either side | 10 | 220 | 1 |
| \(K_{4,4}\) | Disjoint | 10 | 198 | 1 |
| \(K_{5,5}\) | Adjacent, either side | 14 | 525 | 1 |
| \(K_{5,5}\) | Disjoint | 14 | 480 | 1 |

In each record of `extended_certificates.json`, the field
`certificates[0].polynomial` lists triples `[i,j,c]`, meaning the term
\(ct^iw^j\). Absent terms have coefficient zero. The minimum of \(i+j\)
over its support is \(d\), and there are terms with \(i=0\).

The independent verifier does not divide by \(1-q\). Instead it computes
each sector directly, defines

\[
S^*(t,w)=(1+t)^N S\left(\frac{t}{1+t},w\right),
\]

and checks the full coefficient identity

\[
B^*C^*-A^*D^*=t^2w^2(1+t)^3P(t,w).                         \tag{7}
\]

Equation (7) is equivalent to (6), because
\(2N-2-1-d=3\). It checks the supplied certificates against independently
counted sectors using dense arrays of integers, rather than the generator's
sparse multiplication and division. No floating-point arithmetic or sampled
parameter values enter the sign verification.

For \(0<q<1\), take \(t=q/(1-q)>0\). Equations (6)–(7) yield

\[
\Delta(q,w)=q^2w^2(1-q)^{d+1}
             P\left(\frac q{1-q},w\right)>0.               \tag{8}
\]

Every factor is positive, and \(P\) has at least one positive term.
Equation (1) proves strict negative correlation. When \(q=1\), the
weight of a subset is simply the product of its activities, so the
indicators are independent and the covariance vanishes.

## 4. The connected-subgraph endpoint

Every sector has a factor \(q\). Its coefficient of \(q\) counts connected
spanning subgraphs with the specified marked-edge status. Divide each
sector by \(q\) and let \(q\downarrow0\). The resulting Rayleigh difference is

\[
\Delta_{\rm conn}(w)=w^2H(0,w)=w^2P(0,w).                  \tag{9}
\]

The row \(i=0\) of every supplied certificate is nonempty and positive.
Thus (9) is strictly positive for \(w>0\). The weighted connected measure
has positive normalizing constant because the full graph is connected.
Applying the same four-sector calculation as (1) proves the assertion for
that measure and arbitrary marked activities \(x,y>0\).

## 5. The forest endpoint

For a subgraph with \(k\) components, \(r\) unmarked edges, and \(s=i+j\)
marked edges, \(k+r+s\geq N\), with equality exactly when it is a forest.
Consequently, if \(F_{ij}(w)\) is the corresponding forest-sector polynomial,

\[
S_{ij}(q,qw)=q^{N-i-j}\bigl(F_{ij}(w)+O(q)\bigr).
\]

It follows by multiplication that

\[
\Delta(q,qw)=q^{2N-2}
\bigl(F_{10}F_{01}-F_{00}F_{11}+O(q)\bigr).                \tag{10}
\]

Write \(P(t,w)=\sum c_{ij}t^iw^j\). Substitute \(qw\) for \(w\) in (8).
A term on the right becomes

\[
c_{ij}q^{4+i+j}w^{2+j}(1-q)^{d+1-i}.
\]

The support has \(i+j\geq d\), and \(d+4=2N-2\). Comparing the coefficient
of \(q^{2N-2}\) with (10) gives

\[
\Delta_{\rm forest}(w)=
w^2\sum_{i+j=d}c_{ij}w^j.                                \tag{11}
\]

There is at least one term on this diagonal, and all its coefficients are
positive. Therefore (11) is strictly positive for every \(w>0\).
The forest normalizing constant is positive because the empty forest is
available. Formula (1), applied to the forest sectors, completes the proof
for arbitrary marked activities.

The verifier also constructs both endpoint Rayleigh polynomials directly
from the sector counts and checks (9) and (11) coefficient by coefficient.

For example, for a disjoint pair in \(K_{3,3}\), these are

\[
\begin{split}
\Delta_{\rm forest}(w)
 &=w^2(1+12w+65w^2+188w^3+301w^4+252w^5+81w^6),\\
\Delta_{\rm conn}(w)
 &=w^8(81+135w+85w^2+23w^3+2w^4).
\end{split}
\]

All other endpoint lists are in `extended_verified_summary.json`.

## 6. An independent magnitude check

The number of spanning trees of \(K_{m,n}\) is
\(\tau=m^{n-1}n^{m-1}\): its nonzero Laplacian eigenvalues are \(n\),
repeated \(m-1\) times, \(m\), repeated \(n-1\) times, and \(m+n\);
the matrix-tree theorem divides their product by \(m+n\).

Orient edges from left to right. Inject unit current at a left vertex
\(a\) and remove it at a right vertex \(b\). If \(U\) and \(V\) are the
average left and right potentials, the equations at a left vertex \(i\)
and a right vertex \(j\) give

\[
u_i=V+\frac{{\bf1}_{i=a}}n,\quad
v_j=U-\frac{{\bf1}_{j=b}}m,\quad
U-V=\frac1{mn}.
\]

Hence the current through edge \((i,j)\) is
\(\delta_{i,a}/n+\delta_{j,b}/m-1/(mn)\).
The transfer-current determinant for a uniform spanning tree gives its
two-edge count difference as \(\tau^2 K_{ef}^2\). Thus the coefficient of
\(w^{2N-4}\) in each forest Rayleigh polynomial must equal

\[
\frac{\tau^2}{m^2n^2}
\begin{cases}
(m-1)^2,&\text{common left vertex},\\
(n-1)^2,&\text{common right vertex},\\
1,&\text{disjoint}.
\end{cases}
\]

These values also give the lowest-degree coefficients of the connected
Rayleigh polynomials, since their lowest-degree sectors count trees.
All values match the independent coefficient audit. For \(K_{5,5}\), the
adjacent and disjoint values are respectively \(3906250000\) and
\(244140625\). This check is supplementary; (7), (9), and (11) already
establish the signs without using the transfer-current theorem.
