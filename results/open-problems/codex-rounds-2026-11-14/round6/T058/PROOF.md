# Centered packing loss on every interior phase band

All logarithms without subscripts are natural. Define
\[
 f(n)=2\log_2n-2\log_2\log_2n+2\log_2(e/2)+1,\quad
 k=\lfloor f(n)\rfloor,\quad t=\{f(n)\},\quad
 q=2^{-\binom k2},\quad N=\binom nk,\quad \mu=Nq.
\]
Let \(\mathcal I\) be the family of independent \(k\)-sets in
\(G(n,1/2)\). Write \(X=|\mathcal I|\), and let \(M\) be the largest
number of pairwise vertex-disjoint members of \(\mathcal I\).

Let \(\mathcal H\) be a random family in which each of the \(N\)
possible \(k\)-sets is included independently with probability \(q\).
For any family \(F\), write \(\nu(F)\) for its maximum number of
pairwise disjoint members and \(D(F)=|F|-\nu(F)\). The deterministic
correction used below is
\[
 c_n=\mathbb E D(\mathcal H).
\tag{1}
\]
This is a finite expectation, so (1) defines it without a choice of
coupling or any random-graph conditioning.

**Theorem.** Fix \(0<a<b<1\). Uniformly over integers with
\(a\le t\le b\),
\[
 X-M-c_n=o_p(\sqrt\mu).
\tag{2}
\]
Consequently, writing \(X_{k-1}\) for the number of independent
\((k-1)\)-sets and \(\mu_{k-1}=\mathbb E X_{k-1}\),
\[
 \left(\frac{M-\mu+c_n}{\sqrt\mu},
       \frac{X_{k-1}-\mu_{k-1}}{\sqrt{\mu_{k-1}}}\right)
 \xrightarrow{d}N(0,I_2).
\tag{3}
\]
The correction satisfies the explicit bound
\[
 0\le c_n\le \frac{\mu^2k^2}{2n}.
\tag{4}
\]
No identification of \(\mu-c_n\) with \(\mathbb EM\) to error
\(o(\sqrt\mu)\) is asserted.

## 1. Parameter estimates and edge-sharing pairs

Put \(L=\log n\), \(\ell=\log2\), and \(C=2/\ell\). Directly
from the definition,
\[
 k=C(L-\log L+1+\log\ell)-1-t=CL+O(\log L),
 \qquad
 2^k=\frac{e^2}{2}2^{-t}\frac{n^2}{(\log_2n)^2}.
\tag{5}
\]
The product formula for the binomial coefficient gives
\(\log\binom nk=kL-\log k!+O(k^2/n)\): its error is
\(\sum_{i=0}^{k-1}\log(1-i/n)\), bounded in absolute value by
\(2\sum_{i=0}^{k-1}i/n\) eventually. Integral comparison yields
\(\log k!=k\log k-k+O(\log k)\). Therefore
\[
 \log\mu=k[L-\ell(k-1)/2-\log k+1]+O(\log k+k^2/n).
\]
The bracket is exactly \(\log(CL/k)+\ell t/2\), by (5).
Multiplication by \(k=CL+O(\log L)\) gives
\[
 \log\mu=tL+O(\log L),\qquad \mu=n^{t+o(1)}.
\tag{6}
\]
All these estimates are uniform for \(0\le t<1\). In particular,
\(\mu\to\infty\) and \(\mu k^2/n=o(1)\) on the theorem's band.

For two distinct \(k\)-sets meeting in \(j\) vertices, their
independence constraints share \(\binom j2\) graph edges. Their
joint probability of being independent is \(q^2 2^{\binom j2}\).
Thus the expected number \(\Delta\) of unordered pairs in
\(\mathcal I\) meeting in at least two vertices is
\[
 \Delta=\frac\mu2\sum_{j=2}^{k-1}h_j,\qquad
 h_j=\binom kj\binom{n-k}{k-j}2^{-\binom k2+\binom j2}.
\tag{7}
\]
The diagonal \(j=k\) is excluded. We now rederive the bound needed
for the whole family, rather than just a normalized covariance:
\[
 \Delta=O\left(\frac{\mu^2 k^5}{n^2}
                       +\mu k^2n2^{-k}\right)=o(1).
\tag{8}
\]

For completeness set \(m=\lfloor k/2\rfloor\) and
\(m'=\lceil k/2\rceil\). A union bound over \(j\)-subsets of a
fixed \(k\)-set shows that, for \(2\le j\le m\),
\[
 h_j\le\mu v_j,\qquad
 v_j=\left(\frac{k^2}{n-k}\right)^j2^{j(j-1)/2}.
\]
Indeed the probability a uniform \(k\)-set contains a specified
\(j\)-set is \((k)_j/(n)_j\). Summing over the
\(\binom kj\) candidates and bounding each factor gives the displayed
inequality. Here \((z)_j\) denotes a falling factorial.
The logarithm of \(v_j\) is convex, so
\(\sum_{j=2}^m h_j\le\mu m\max(v_2,v_m)\).
With \(u=\log_2n\), (5) implies \(k=2u+O(\log u)\), and hence
\[
 \log_2v_m=-u^2/2+O(u\log u),\qquad v_2=\Theta(k^4/n^2).
\]
Consequently \(v_m\le v_2\) eventually, and this part of the sum is
\(O(\mu k^5/n^2)\).

For \(m<j<k\) put \(s=k-j\). Direct substitution in (7) gives
\[
 h_{k-s}=\binom ks\binom{n-k}s2^{-ks+s(s+1)/2}
 \le w_s=(kn2^{-k})^s2^{s(s+1)/2}.
\]
The actual range of \(s\) is contained in \([1,m']\).
The logarithm of \(w_s\) is convex, with
\[
 w_1=2kn2^{-k}=\Theta((\log n)^3/n),\qquad
 \log_2w_{m'}=-u^2/2+O(u\log u).
\]
Thus \(w_{m'}\le w_1\) eventually and the large-intersection sum
is \(O(k^2n2^{-k})\). This proves the first bound in (8).
Using (5) and (6), its two terms are respectively
\(n^{2t-2+o(1)}\) and \(n^{t-1+o(1)}\), both tending uniformly
to zero for \(t\le b<1\).

## 2. Comparison of entire families

We use the following proved input from Robert Morris and Oliver Riordan,
[*Random cliques in random graphs revisited*, arXiv:2504.00964v1,
Theorem 3.1 and its Section 2 setup](https://arxiv.org/html/2504.00964v1#S3).
For a symmetric uniform family of subsets of a ground set, retain ground
elements independently with probability \(p\), and record which members
are fully retained. Put \(\pi=p^s\), where every member has size \(s\).
If \(1-\pi\) is bounded away from zero and the expected number of
distinct pairs sharing a ground element tends to zero, the recorded
family has total variation distance \(o(1)\) from independent retention
of members with probability \(\pi\).

Here the ground elements are the unordered pairs of vertices of
\([n]\), each retained when the corresponding graph edge is absent.
They are independent with \(p=1/2\). For every \(k\)-set \(A\),
the corresponding member consists of its \(\binom k2\) internal
unordered pairs. Thus \(s=\binom k2\), \(\pi=q\), and a member
is fully retained exactly when \(A\) is independent.
Vertex permutations act transitively on the \(k\)-sets, checking
the symmetry hypothesis; all members have size \(s\), checking
uniformity. Eventually \(k\ge2\) and \(1-q\ge1/2\).
Two distinct members share a ground element exactly when their
vertex sets meet in at least two vertices. Their expected number
is precisely (7), and tends to zero by (8). The theorem therefore gives
\[
 \eta_n:=d_{\mathrm{TV}}(\mathcal L(\mathcal I),
                            \mathcal L(\mathcal H))=o(1).
\tag{9}
\]
The stated uniformity follows by the sequential criterion: any sequence
of integers in the band tending to infinity satisfies all these
hypotheses and bounds. A failure of uniform convergence would provide
a contradicting sequence. Growing \(k\) is allowed in this theorem;
its ground set, uniformity parameter and family may depend on \(n\).

For any statistic \(T\) of a family and any event \(B\), the
definition of total variation gives
\[
 |\Pr(T(\mathcal I)\in B)-\Pr(T(\mathcal H)\in B)|\le\eta_n.
\tag{10}
\]
This applies to the packing loss itself, not only to the number of sets.

## 3. Variance of the independent-model loss

We prove a finite inequality valid for any independent random family
\(\mathcal H\) of \(k\)-sets with common retention probability
\(q\in(0,1)\). Set
\[
 R=\binom nk-1-\binom{n-k}k.
\]
There are exactly \(R\) possible sets other than a fixed \(A\)
that intersect \(A\); impossible binomial coefficients mean zero.
Then
\[
 \operatorname{Var}D(\mathcal H)
 \le Nq(1-q)[1-(1-q)^R]
 \le Nq^2(1-q)R
 \le \frac{\mu^2 k^2}{n}.
\tag{11}
\]

First, if \(A\notin F\), every packing in \(F\) remains available
in \(F\cup\{A\}\). A packing in the larger family contains at most
one additional member, so
\[
 0\le\nu(F\cup\{A\})-\nu(F)\le1.
\]
The difference is an integer. It follows that
\[
 \delta_A(F):=D(F\cup\{A\})-D(F)\in\{0,1\}.
\tag{12}
\]
If \(A\) is disjoint from every member of \(F\), it can be added
to a maximum packing, so \(\delta_A(F)=0\). Therefore
\[
 \delta_A(F)^2\le
 \mathbf1\{\text{some member of }F\text{ intersects }A\}.
\tag{13}
\]

Here is the product-variance inequality with its normalization made
explicit. For independent Bernoulli coordinates \(B_1,\ldots,B_N\)
of parameter \(q\) and any real function \(g\),
\[
 \operatorname{Var}g(B)\le q(1-q)\sum_i
 \mathbb E[g(B_{-i},1)-g(B_{-i},0)]^2.
\tag{14}
\]
To see this, reveal coordinates in order and decompose the variance
into the sum of squares of the Doob martingale differences. Conditional
on the first \(i-1\) coordinates, the \(i\)-th contribution is
\(q(1-q)\) times the square of the difference of the two conditional
future expectations. Jensen's inequality bounds that square by the
conditional future expectation of the squared difference with the same
future coordinates used in the two terms. Averaging and summing gives
(14). This argument holds for any finite \(N\).

Apply (14) to \(g=D\), and use (13). The probability on its right
is exactly \(1-(1-q)^R\), since the \(R\) intersecting candidates
are independently present. This proves the first inequality in (11).
The union bound gives \(1-(1-q)^R\le qR\), proving the second.
Finally, a uniform random \(k\)-set \(B\) intersects a fixed \(A\)
with probability at most
\(\sum_{v\in A}\Pr(v\in B)=k^2/n\). Consequently
\(R\le Nk^2/n\), proving the last inequality in (11).

For (4), make a conflict graph on the members of any family \(F\),
with an edge for every intersecting pair. Deleting one endpoint of a
remaining edge until no edge remains proves
\(0\le D(F)\le Y(F)\), where \(Y(F)\) is its number of edges.
For \(\mathcal H\), each candidate pair is present with probability
\(q^2\). Counting unordered pairs gives
\[
 \mathbb EY(\mathcal H)=\frac{NRq^2}{2}
 \le\frac{\mu^2k^2}{2n}.
\tag{15}
\]
Taking expectations proves (4).

## 4. Transfer and the Gaussian conclusion

Chebyshev's inequality and (11) show, for each fixed \(\varepsilon>0\),
\[
 \Pr\bigl(|D(\mathcal H)-c_n|>\varepsilon\sqrt\mu\bigr)
 \le\frac{\mu k^2}{\varepsilon^2 n}=o(1).
\]
Equations (9) and (10), applied to \(T=D\), give the more explicit
transfer bound
\[
 \Pr\bigl(|X-M-c_n|>\varepsilon\sqrt\mu\bigr)
 \le\eta_n+\frac{\mu k^2}{\varepsilon^2 n}=o(1).
\tag{16}
\]
This proves (2), including its uniformity.

The [round 4 joint count theorem](../../../codex_op_1114r4/briefs/T058/PROOF.md)
gives
\[
 \left(\frac{X-\mu}{\sqrt\mu},
       \frac{X_{k-1}-\mu_{k-1}}{\sqrt{\mu_{k-1}}}\right)
 \xrightarrow{d}N(0,I_2).
\]
Its band assumption is satisfied with
\(\delta=\min(a,1-b)>0\), which is less than \(1/2\) since
\(a<b\). Subtract the first-coordinate error
\((X-M-c_n)/\sqrt\mu=o_p(1)\), keeping the second coordinate.
Slutsky's theorem proves (3). No approximation of the entire
\((k-1)\)-set family is needed: the error event in (16) concerns
only the \(k\)-set family in the original graph.

## 5. Scope

If \(b<2/3\), (4) gives \(c_n/\sqrt\mu\le
\mu^{3/2}k^2/(2n)=o(1)\), recovering the previous centering by
\(\mu\). Above that phase, (2) controls the fluctuations of the
loss after the deterministic correction (1). The correction is not
given to additive \(o(\sqrt\mu)\) accuracy by the upper bound (4).

Total variation convergence alone does not justify transferring
expectations of an unbounded loss. Thus (2) and (3) do not assert
\(\mathbb E(X-M)=c_n+o(\sqrt\mu)\), nor a variance asymptotic
for \(M\). No endpoint band touching \(t=0\) or \(t=1\) is covered.

This packing contains at most \(kX\) vertices. For fixed
\(\varepsilon>0\), Markov's inequality gives
\(\Pr(kM>\varepsilon n)\le k\mu/(\varepsilon n)=o(1)\)
on every stated band. The chromatic cost of the remaining graph
is not bounded by this theorem. It therefore yields no concentration
width for \(\chi(G(n,1/2))\). No literature novelty is claimed.
