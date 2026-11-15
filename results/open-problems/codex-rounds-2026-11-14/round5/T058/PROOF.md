# Disjoint independent sets below phase 2/3

All logarithms without subscripts are natural. Put
\[
 f(n)=2\log_2 n-2\log_2\log_2 n+2\log_2(e/2)+1,
 \qquad k=\lfloor f(n)\rfloor,\quad t=\{f(n)\},
 \qquad q=2^{-\binom k2},\quad \mu=\binom nk q.
\]
Let \(X=X_k\) count independent \(k\)-sets in \(G(n,1/2)\), and let
\(M=M_k\) be the maximum number of pairwise vertex-disjoint independent
\(k\)-sets. Let \(Y\) count unordered pairs of distinct independent
\(k\)-sets whose vertex sets intersect.

**Theorem.** For every fixed \(0<a<b<1\), uniformly over integers with
\(a\le t\le b\),
\[
 \mathbb EY=(1+o(1))\frac{\mu^2 k^2}{2n}.                 \tag{1}
\]
Moreover \(0\le X-M\le Y\) for every graph. Consequently, for every
fixed \(0<a<b<2/3\),
\[
 \mathbb E\frac{X-M}{\sqrt\mu}
 \le (1+o(1))\frac{\mu^{3/2}k^2}{2n}
 \le n^{3b/2-1+o(1)}=o(1).                              \tag{2}
\]
In particular \(X-M=o_p(\sqrt\mu)\), uniformly on this band.

Write \(\mu_{k-1}=\mathbb EX_{k-1}\). The joint count limit proved in
[round 4](../../../codex_op_1114r4/briefs/T058/PROOF.md), independently
rechecked in LOG.md, then gives
\[
 \left(\frac{M-\mu}{\sqrt\mu},
       \frac{X_{k-1}-\mu_{k-1}}{\sqrt{\mu_{k-1}}}\right)
 \xrightarrow{d}N(0,I_2).                               \tag{3}
\]
The first coordinate may instead be centered at \(\mathbb EM\).
This concerns a packing statistic; it is not a concentration bound for
the chromatic number.

## 1. Deterministic deletion bound

Form a graph \(F\) whose vertices are the independent \(k\)-sets of the
given graph, joining two vertices when the corresponding sets intersect.
It has \(X\) vertices and \(Y\) edges. Its largest independent vertex
set has size \(M\). While an edge remains, delete one of its endpoints.
Each deletion removes at least one of the original edges, so the number
of deletions is at most \(Y\). The remaining vertices form an independent
set in \(F\). Thus \(M\ge X-Y\). Since also \(M\le X\),
\[
 0\le X-M\le Y.                                         \tag{4}
\]
The argument covers \(X=0\) and the case \(Y>X\).

## 2. Uniform sizes of the parameters

Let \(L=\log n\), \(\ell=\log2\), and \(c=2/\ell\). The definition of
\(f\) gives
\[
 k=c(L-\log L+1+\log\ell)-1-t=cL+O(\log L),             \tag{5}
\]
and exactly
\[
 2^k=\frac{e^2}{2}2^{-t}\frac{n^2}{(\log_2 n)^2}.        \tag{6}
\]
Expanding the product in \(\binom nk\) and using
\(\log k!=k\log k-k+O(\log k)\) yields
\[
 \log\mu=k[L-\ell(k-1)/2-\log k+1]+O(\log k+k^2/n).
\]
Substitution from (5) makes the bracket exactly
\(\log(cL/k)+\ell t/2\). The first term multiplied by \(k\) is
\(O(\log L)\); the second is \(tL+O(\log L)\). Hence
\[
 \mu=n^{t+o(1)},\qquad k=\Theta(\log n),\qquad
 n2^{-k}=\Theta((\log n)^2/n),                           \tag{7}
\]
with errors and constants uniform for \(0\le t<1\). In particular
\(\mu\ge n^{a+o(1)}\) on the theorem's band.

## 3. Exact pair expectation, including one-vertex intersections

For a fixed \(k\)-set \(A\), the number of \(k\)-sets \(B\) with
\(|A\cap B|=j\) is \(\binom kj\binom{n-k}{k-j}\).
The constraints that both sets be independent concern
\(2\binom k2-\binom j2\) distinct edges. Thus their joint probability is
\(q^2 2^{\binom j2}\). Counting ordered pairs and dividing by two gives
\[
 \mathbb EY=\frac\mu2\sum_{j=1}^{k-1}h_j,\qquad
 h_j=\binom kj\binom{n-k}{k-j}2^{-\binom k2+\binom j2}.
                                                               \tag{8}
\]
The upper endpoint is \(k-1\): \(j=k\) would count a set paired with
itself. The lower endpoint is 1: although such pairs have independent
independence indicators, their vertex sets cannot both belong to a packing.

Let \(Y_1\) count pairs with intersection size exactly 1. Equation (8)
and \(\binom nk k/n=\binom{n-1}{k-1}\) show
\[
 \frac{\mathbb EY_1}{\mu^2k^2/(2n)}
 =\frac{\binom{n-k}{k-1}}{\binom{n-1}{k-1}}
 =\prod_{i=0}^{k-2}\left(1-\frac{k-1}{n-1-i}\right).
                                                               \tag{9}
\]
For sufficiently large \(n\), all factors are in \([0,1]\). The elementary
inequality \(\prod_i(1-x_i)\ge1-\sum_i x_i\), for \(x_i\in[0,1]\),
gives the explicit bounds
\[
 1-\frac{(k-1)^2}{n-k+1}
 \le\frac{\mathbb EY_1}{\mu^2k^2/(2n)}\le1.             \tag{10}
\]
By (7), this ratio tends uniformly to 1.

## 4. All larger intersections

We prove
\[
 \sum_{j=2}^{k-1}h_j
 =O\left(\frac{\mu k^5}{n^2}+k^2n2^{-k}\right).         \tag{11}
\]
This also checks the overlap estimate used in the earlier count theorem.
For sufficiently large \(n\), put \(m=\lfloor k/2\rfloor\) and
\(m'=\lceil k/2\rceil\). If \(B\) is a uniformly chosen \(k\)-set, then
\[
 \mathbb P(|A\cap B|=j)
 \le\binom kj\frac{(k)_j}{(n)_j}
 \le\left(\frac{k^2}{n-k}\right)^j.
\]
The first inequality is a union bound over the \(j\)-subsets of \(A\);
\((x)_j\) denotes the falling factorial. Therefore, for \(2\le j\le m\),
\[
 h_j\le\mu v_j,\qquad
 v_j=\left(\frac{k^2}{n-k}\right)^j2^{j(j-1)/2}.
\]
The logarithm of \(v_j\), extended to real \(j\), is a convex quadratic,
so
\[
 \sum_{j=2}^{m}h_j\le\mu m\max(v_2,v_m).               \tag{12}
\]
Write \(u=\log_2 n\). By (5), \(k=2u+O(\log u)\),
\(m=u+O(\log u)\), and \(\log_2(k^2/(n-k))=-u+O(\log u)\).
It follows that
\[
 \log_2v_m=-u^2/2+O(u\log u),\qquad
 v_2=\Theta(k^4/n^2).
\]
Thus \(v_m\le v_2\) eventually, uniformly in the phase, and (12) is
\(O(\mu k^5/n^2)\).

For \(m<j<k\), set \(s=k-j\). Since \(h_k=1\), direct division gives
\[
 h_{k-s}=\binom ks\binom{n-k}s
             2^{-ks+s(s+1)/2}
 \le w_s:=(kn2^{-k})^s2^{s(s+1)/2}.                     \tag{13}
\]
The actual range \(1\le s\le k-m-1\) is contained in \([1,m']\).
Convexity again gives
\[
 \sum_{j=m+1}^{k-1}h_j\le m'\max(w_1,w_{m'}).
\]
Here \(w_1=2kn2^{-k}=\Theta((\log n)^3/n)\), whereas
\(\log_2w_{m'}=-u^2/2+O(u\log u)\). Hence \(w_{m'}\le w_1\)
eventually, and this sum is \(O(k^2n2^{-k})\). This proves (11).

Combining (8) and (11), the contribution from \(j\ge2\) is at most
\[
 O\left(\frac{\mu^2k^5}{n^2}+\mu k^2n2^{-k}\right).
\]
Its ratio to \(\mu^2k^2/(2n)\) is
\[
 O\left(\frac{k^3}{n}+\frac{n^22^{-k}}\mu\right)
 =O\left(\frac{(\log n)^3}{n}+\frac{(\log n)^2}\mu\right)=o(1),
\]
uniformly when \(t\ge a>0\). Equations (9) and (10) now prove (1).

## 5. Transfer to the maximum packing

From (1), (4), and (7),
\[
 \mathbb E\frac{X-M}{\sqrt\mu}
 \le\frac{\mathbb EY}{\sqrt\mu}
 =(1+o(1))\frac{\mu^{3/2}k^2}{2n}
 \le n^{3b/2-1+o(1)}.
\]
This tends to zero for \(b<2/3\). For every \(\varepsilon>0\), Markov's
inequality gives
\[
 \mathbb P(X-M>\varepsilon\sqrt\mu)
 \le\varepsilon^{-1}\mathbb E[(X-M)/\sqrt\mu]\longrightarrow0.
\]
This proves (2), including its uniform probabilistic consequence.

For completeness, the passage to the joint law can be made directly at
the characteristic-function level. For every real \(s,z\),
\[
 \begin{split}
 &\left|\mathbb E\exp\left(i s\frac{M-\mu}{\sqrt\mu}
                    +i z\frac{X_{k-1}-\mu_{k-1}}{\sqrt{\mu_{k-1}}}\right)
 -\mathbb E\exp\left(i s\frac{X-\mu}{\sqrt\mu}
                    +i z\frac{X_{k-1}-\mu_{k-1}}{\sqrt{\mu_{k-1}}}\right)
 \right|\\
 &\hspace{2cm}\le |s|\mathbb E[(X-M)/\sqrt\mu]=o(1).
 \end{split}                                                     \tag{14}
\]
This uses \(|e^{ix}-e^{iy}|\le|x-y|\). The previously proved joint count
characteristic function tends to \(e^{-(s^2+z^2)/2}\) on every fixed
interior band. Applying its theorem with
\(\delta=\min(a,1-b)>0\) is valid because \(a<b\) implies \(\delta<1/2\).
The continuity theorem and (14) prove (3). Also
\[
 0\le\mu-\mathbb EM=\mathbb E(X-M)=o(\sqrt\mu),
\]
so changing the first center to \(\mathbb EM\) changes that coordinate by
a deterministic quantity tending to zero.

## Scope and endpoint

Equation (1) remains valid on each fixed band strictly inside \((0,1)\).
The restriction \(b<2/3\) enters when dividing the deletion bound by
\(\sqrt\mu\): its leading scale is
\(\mu^{3/2}k^2/(2n)=n^{3t/2-1+o(1)}\). This argument does not establish
the packing approximation at or above phase \(2/3\). A large expected
number of conflicts alone would not disprove that approximation.

Neither (2) nor (3) asserts \(\operatorname{Var}M\sim\mu\); the first-moment
error bound does not imply an error bound in mean square. Most vertices
are outside this packing: for every fixed \(\varepsilon>0\),
\[
 \mathbb P(kM>\varepsilon n)\le\mathbb P(kX>\varepsilon n)
 \le\frac{k\mu}{\varepsilon n}\le n^{b-1+o(1)}\longrightarrow0
\]
on a fixed band with \(b<1\). The chromatic
cost of the remaining vertices is uncontrolled here, so no concentration
width for \(\chi(G(n,1/2))\) follows. No literature-novelty claim is made.
