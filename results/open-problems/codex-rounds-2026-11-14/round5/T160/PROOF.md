# Localization of the exterior response by one active component

All percolation below is independent Bernoulli bond percolation on the
nearest-neighbor cubic lattice at a fixed parameter \(0<p<1\).
The estimates hold at every such parameter. Their vanishing-error
consequence assumes \(\theta(p)=0\). In particular that consequence applies
to the unresolved extinction case of T160.

## 1. Definitions and statement

Write \(B_j=[-j,j]^3\cap\mathbb Z^3\), \(S_j=\partial B_j\),
\(F_j=E(B_j)\), and

\[
G_{m,j}=F_j\setminus F_m,\qquad
H_{m,j}=\{S_m\leftrightarrow S_j\text{ using }G_{m,j}\},\qquad
b_{m,j}=\mathbb P_p(H_{m,j}).
\tag{1}
\]

Fix integers \(m<R<n\), with \(m\ge1\). All probabilities can be taken
on the finite product space of edges \(G_{m,n}\).
In the open graph using \(G_{m,R}\), a component is called active if it
meets both \(S_m\) and \(S_R\). No boundary vertices are wired in defining
these components. Let \(N_{m,R}\) count them.

For a configuration on \(G_{m,n}\), let \(\xi_{m,n}\) be its partition
of \(S_m\cup\{*\}\): retain exterior connectivity between vertices of
\(S_m\) and wire all vertices of \(S_n\) to the extra terminal \(*\).
This is the marked exterior partition in the preceding report.

Define a partition \(L_{m,R}\) from \(G_{m,R}\) alone. First partition
\(S_m\) by its ordinary open connectivity in \(G_{m,R}\). If
\(N_{m,R}=1\), join \(*\) to precisely the vertices of \(S_m\) in that
active component. If there are several active components, mark the one
containing the lexicographically smallest vertex of \(S_m\) among them.
If there are none, make \(*\) a singleton. This last convention merely
defines \(L_{m,R}\) on every configuration.

**Theorem.** For every integer \(k\ge1\),

\[
\mathbb P_p(N_{m,R}\ge k\mid H_{m,n})
       \le b_{m,R}^{\,k-1}.
\tag{2}
\]

Moreover

\[
\begin{split}
\mathbb P_p(\xi_{m,n}\ne L_{m,R}\mid H_{m,n})&\le b_{m,R},\\
\left\|\mathcal L_p(\xi_{m,n}\mid H_{m,n})
       -\mathcal L_p(L_{m,R}\mid H_{m,n})\right\|_{\rm TV}
       &\le b_{m,R}.
\end{split}
\tag{3}
\]

Here total variation is \(\sup_A|P(A)-Q(A)|\).
Both bounds are uniform in the distant radius \(n>R\).

## 2. Disjoint crossing witnesses

We use the BK inequality for increasing events in a finite Bernoulli
product space: if \(A\circ B\) denotes the existence of disjoint sets of
open edges witnessing \(A\) and \(B\), then

\[
\mathbb P_p(A\circ B)\le\mathbb P_p(A)\mathbb P_p(B).
\tag{4}
\]

This is the increasing-event inequality of J. van den Berg and H. Kesten,
“Inequalities with Applications to Percolation and Reliability”,
Journal of Applied Probability 22 (1985), 556–569,
[original paper](https://sites.math.northwestern.edu/~auffing/papers/vBK.pdf).
Its iterated form bounds the probability of disjoint witnesses for
\(A_1,\ldots,A_k\) by \(\prod_i\mathbb P_p(A_i)\).
Indeed simultaneous disjoint occurrence is contained in
\(A_1\circ(A_2\circ\cdots\circ A_k)\); the event in parentheses is
increasing, so induction using (4) applies.

The required deterministic inclusion is

\[
H_{m,n}\cap\{N_{m,R}\ge k\}
\ \subset\
H_{m,n}\circ
\underbrace{H_{m,R}\circ\cdots\circ H_{m,R}}_{k-1\text{ witnesses}}.
\tag{5}
\]

To prove it, fix an open configuration in the event on the left. Let
\(U\) be the union of all components of the open \(G_{m,R}\) graph that
meet \(S_m\), including components that are not active. Choose a simple
open path \(\gamma\) from \(S_m\) to \(S_n\) using \(G_{m,n}\).
It starts in \(U\) and ends outside \(B_R\). Let \(v\) be its last
vertex in \(U\), and let \(C\) be the local component containing \(v\).
The next edge of \(\gamma\) cannot be an edge of \(G_{m,R}\):
otherwise its endpoint would also belong to \(C\subset U\).
An edge of \(G_{m,n}\setminus G_{m,R}\) incident to \(B_R\) can leave
that box only from \(S_R\). Thus \(v\in S_R\).
Since \(C\) meets \(S_m\), it is active.

Within \(C\) choose a simple open path from a vertex of \(S_m\) to \(v\).
Append the tail of \(\gamma\) following \(v\). This is a simple open
path witnessing \(H_{m,n}\): the prefix is contained in \(U\), and the
tail avoids \(U\). For each of \(k-1\) other active components choose
a simple open path inside that component from \(S_m\) to \(S_R\).
These paths lie in pairwise disjoint local components, are disjoint from
the prefix in \(C\), and cannot meet the tail, which avoids \(U\).
They therefore supply pairwise disjoint edge witnesses for all the events
on the right side of (5).

The argument permits arbitrary mergers outside \(B_R\). Those mergers
do not change the chosen local witnesses. It does not apply BK to the
event \(\{N_{m,R}\ge k\}\), which need not be increasing.

By (4) and (5),

\[
\mathbb P_p(H_{m,n},N_{m,R}\ge k)
      \le b_{m,n}b_{m,R}^{\,k-1}.
\tag{6}
\]

The denominator \(b_{m,n}\) is positive, since an outward axis path has
positive probability. Dividing proves (2). For \(k=1\), the bound is
also immediate: on \(H_{m,n}\), stopping a path at its first visit to
\(S_R\) shows \(N_{m,R}\ge1\).

## 3. Reconstruction of the marked partition

Suppose \(H_{m,n}\) occurs and \(N_{m,R}=1\). Write \(C\) for the unique
active local component. Every other local component meeting \(S_m\)
misses \(S_R\). Such a component cannot acquire a new connection when
the edges in \(G_{m,n}\setminus G_{m,R}\) are added: none of those edges
is incident to a vertex of \(B_R\setminus S_R\).
It remains a whole component in the larger graph.

The last-exit argument of Section 2 shows that \(C\) connects to \(S_n\).
It can absorb local components not meeting \(S_m\), but no other local
component meeting \(S_m\). Consequently the partition of \(S_m\)
does not change between radii \(R\) and \(n\), and its only block
connected to \(S_n\) is \(C\cap S_m\). Wiring all of \(S_n\) to \(*\)
therefore gives exactly \(L_{m,R}\). Thus

\[
H_{m,n}\cap\{\xi_{m,n}\ne L_{m,R}\}
\subset H_{m,n}\cap\{N_{m,R}\ge2\}.
\tag{7}
\]

Equation (2) proves the first inequality in (3). Both random partitions
are defined on the same conditioned probability space. For any partition
event \(A\), their indicators can differ only when the partitions differ.
Taking a supremum over \(A\) proves the second inequality in (3).

## 4. Consequences for the preceding response criterion

For completeness, an interior configuration on \(F_m\) determines a
partition \(\pi\) of \(S_m\cup\{0\}\) by its open connectivity. Write
\(\mathcal P_m\) for its realizable partitions and
\(a_m(\pi)=\mathbb P_p(\pi_m=\pi)\).
For partitions \(\pi\) and \(\xi\), extend both to
\(S_m\cup\{0,*\}\), and let

\[
K_m(\pi,\xi)=\mathbf1\{0\sim *\text{ in }\pi\vee\xi\}.
\tag{8}
\]

The join means transitive closure of both equivalence relations.
It retains all interior components, including those not containing the
root, so it permits any number of exterior returns through the interior.

An alternating decomposition of an open root-to-target path into its
interior and exterior portions proves that its connection indicator is
\(K_m(\pi_m,\xi_{m,n})\). Conversely a chain in the join gives an open
walk; stopping at the first target visit and removing loops gives a path.
Thus, writing \(h_{m,n}(\pi)\) for the exterior connection probability
with interior partition \(\pi\), the normalized response is

\[
r_{m,n}(\pi)=\frac{h_{m,n}(\pi)}{b_{m,n}}
  =\mathbb E_p[K_m(\pi,\xi_{m,n})\mid H_{m,n}].
\tag{9}
\]

Define its local approximation

\[
\widetilde r_{m,R,n}(\pi)
 =\mathbb E_p[K_m(\pi,L_{m,R})\mid H_{m,n}].
\tag{10}
\]

The conditioning in (10) still depends on \(n\). Equations (3) and
(8)–(10) give the simultaneous estimate

\[
\sup_{\pi\in\mathcal P_m}
  |r_{m,n}(\pi)-\widetilde r_{m,R,n}(\pi)|\le b_{m,R}.
\tag{11}
\]

In particular the weighted error is at most \(b_{m,R}\), because the
weights \(a_m(\pi)\) sum to one.

Let \(\pi_\star\) join all terminals of \(S_m\cup\{0\}\), put
\(a_\star=a_m(\pi_\star)>0\), and let
\(\nu_{m,\pi}\) be the ordinary interior law conditional on \(\pi_m=\pi\).
Both responses in (9) and (10) are in \([0,1]\) and equal one at
\(\pi_\star\), since \(H_{m,n}\) implies at least one active component.
The exact interior conditional law and its approximation are therefore

\[
\begin{split}
\mu_n|_{F_m}
 &=\sum_\pi\frac{a_m(\pi)r_{m,n}(\pi)}
                   {\sum_\sigma a_m(\sigma)r_{m,n}(\sigma)}
              \nu_{m,\pi},\\
\widetilde\mu_{m,R,n}
 &=\sum_\pi\frac{a_m(\pi)\widetilde r_{m,R,n}(\pi)}
                   {\sum_\sigma a_m(\sigma)\widetilde r_{m,R,n}(\sigma)}
              \nu_{m,\pi}.
\end{split}
\tag{12}
\]

Both denominators are at least \(a_\star\).
For response vectors \(r,s\), put \(D=\sum_\pi a_m(\pi)|r(\pi)-s(\pi)|\)
and let their normalizers be \(Z,W\). Their normalized mixture weights
have total variation at most
\[
\frac12\left(\frac{D}{Z}+\frac{|Z-W|}{Z}\right)
       \le D/a_\star,
\]
using \(|Z-W|\le D\). The mixture components have disjoint supports,
so this is also their interior total variation. Applying (11) proves

\[
\|\mu_n|_{F_m}-\widetilde\mu_{m,R,n}\|_{\rm TV}
       \le b_{m,R}/a_\star.
\tag{13}
\]

There is also a useful bound directly on the oscillation from round 4.
For \(n,\ell>R\) let
\(\lambda_{m,R,n}=\mathcal L_p(L_{m,R}\mid H_{m,n})\) and similarly
for \(\ell\). Since each \(K_m(\pi,\cdot)\) is an indicator, (11) gives

\[
\begin{split}
D_m(n,\ell)
 &=\sum_\pi a_m(\pi)|r_{m,n}(\pi)-r_{m,\ell}(\pi)|\\
 &\le 2b_{m,R}
       +\|\lambda_{m,R,n}-\lambda_{m,R,\ell}\|_{\rm TV}.
\end{split}
\tag{14}
\]

No convergence of the last term is asserted.

## 5. Vanishing error under extinction

Set \(\alpha_p(t)=\mathbb P_p(0\leftrightarrow S_t)\).
For any \(s\in S_m\), every path from \(s\) to \(S_R\) reaches
supremum-norm distance at least \(R-m\) from \(s\). Translation
invariance and a union bound consequently give

\[
b_{m,R}\le |S_m|\alpha_p(R-m)
             =(24m^2+2)\alpha_p(R-m).
\tag{15}
\]

The count is
\(|S_m|=(2m+1)^3-(2m-1)^3=24m^2+2\).
The events defining \(\alpha_p(t)\) decrease to the event that the root
cluster is infinite. Local finiteness identifies an unbounded cluster
with an infinite one. Hence \(\alpha_p(t)\downarrow\theta(p)\).
If \(\theta(p)=0\), (15) implies \(b_{m,R}\to0\) for fixed \(m\).
Equations (11) and (13) are then uniform vanishing-error
approximations as \(R\to\infty\), with \(n>R\).
No decay exponent or uniformity as \(m\to\infty\) is needed.

## 6. Structure of any subsequential cylinder limit

Assume \(\theta(p)=0\), and let \(\mu\) be any subsequential cylinder
limit of \(\mu_n=\mathbb P_p(\cdot\mid0\leftrightarrow S_n)\).
Then \(\mu\)-almost surely there is exactly one infinite open cluster,
it contains the root, and it has one end.

First,
\(\mathbb P_p(0\leftrightarrow S_n)=b_{m,n}Z_{m,n}\), where
\(Z_{m,n}=\sum_\pi a_m(\pi)r_{m,n}(\pi)\ge a_\star\).
Using (6) and containment of the root connection in \(H_{m,n}\),

\[
\mu_n(N_{m,R}\ge k)
 \le \frac{\mathbb P_p(H_{m,n},N_{m,R}\ge k)}
             {b_{m,n}Z_{m,n}}
 \le b_{m,R}^{\,k-1}/a_\star.
\tag{16}
\]

For fixed \(m,R,k\), this is a cylinder event, so (16) passes to \(\mu\).
If the infinite exterior graph with edge set \(E(\mathbb Z^3)\setminus F_m\)
has two distinct infinite open components meeting \(S_m\), then
\(N_{m,R}\ge2\) for every \(R>m\). In each such infinite component,
an open ray starting in \(S_m\) can be stopped at its first visit to
\(S_R\); distinct exterior components cannot merge in a truncation.
Thus the probability of that event is at most \(b_{m,R}/a_\star\)
for every \(R\), and is zero by Section 5. Take the countable intersection
over \(m\): for every \(m\), at most one infinite exterior component meets
\(S_m\), almost surely.

For every fixed \(j\), \(\mu_n(0\leftrightarrow S_j)=1\) when \(n>j\).
The same holds under \(\mu\); the countable intersection shows that the
root cluster is infinite.

If there were two infinite open clusters, choose \(m\) large enough that
both meet \(B_m\). Each would have an infinite exterior component meeting
\(S_m\). To see this, deleting the finitely many edges \(F_m\) from an
infinite connected locally finite graph leaves finitely many components
and at least one infinite component. A path from any of its vertices
back to \(B_m\) shows that an infinite exterior component can be chosen
to meet \(S_m\). The two original clusters cannot merge after edges are
deleted. This contradicts the preceding property.

Finally, an infinite connected locally finite graph has one end if
deleting any finite set of vertices leaves exactly one infinite component.
If deleting a finite vertex set from the root cluster left at least two
infinite components, choose \(m\) so large that it contains that set and
one vertex of each of two such components in \(B_{m-1}\). Delete \(F_m\)
as well. Each of those two components still has an infinite component
meeting \(S_m\), by the same finite-deletion argument. They remain
distinct: every edge incident to the deleted vertex set is already in
\(F_m\), so no path of the exterior graph can restore the removed
connections. This is another contradiction. At least one infinite
component survives every finite deletion by local finiteness, proving
the assertion about ends.

## 7. Remaining obstruction

The reconstruction retains the entire local partition of \(S_m\);
it does not discard finite components or replace the state by the
root-connected boundary set. Thus it is consistent with the explicit
return-path obstruction in round 4.

The local partition \(L_{m,R}\) is a finite-annulus function, but its
law in (10) is still conditioned on the distant event \(H_{m,n}\).
Neither (2) nor critical extinction forces that conditional law to
stabilize. Equation (14) leaves this precise term uncontrolled.
The earlier alternating-branch tree likewise has one-ended
subsequential laws with different weights. The structural conclusion
in Section 6 does not select a unique law.

Consequently this proves a localization estimate and a restriction on
subsequential limits, not the existence claim in T160. No literature
novelty is claimed for this application of BK.
