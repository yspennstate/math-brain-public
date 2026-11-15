# A restriction on competing infinite-chain ground states

## Statement and external premise

Let \(\mathfrak A\) be the quasi-local observable algebra of a chain with a finite-dimensional space at each site, and let \(\tau\) be translation by one site. For a translation-invariant finite-range interaction, let \(G\) be its set of algebraic ground states. The ground-state condition used here is

\[
 \rho\bigl(B^*[H,B]\bigr)\geq0
 \quad\text{for every local }B.
 \tag{1}
\]

The commutator is a finite sum over interaction terms meeting the support of \(B\). Thus (1) makes sense without defining an infinite sum as an observable.

Assume that \(G\) has exactly one translation-invariant member \(\omega\), and that \(\omega\) is pure on \(\mathfrak A\). These are external premises for the spin-1 application: see Hal Tasaki, *On the uniqueness of translation-invariant ground states of the S=1 Heisenberg and J–D antiferromagnetic chains*, [arXiv:2610.34330v2, Theorem 2.1](https://arxiv.org/html/2610.34330v2). The finite numerical premises of that theorem are not verified here.

For a finite interval \(I\), write \(\rho_{I,x}\) for the density matrix on \(\mathfrak A_I\) defined by

\[
 \operatorname{Tr}(\rho_{I,x}A)=\rho(\tau^x(A)),\qquad A\in\mathfrak A_I,
\]

and write \(\omega_I\) for the corresponding density matrix of \(\omega\). Trace norm is used without a factor of \(1/2\).

**Proposition.** For every finite \(I\) and every \(\epsilon>0\),

\[
 \lim_{N\to\infty}\ 
 \sup_{\rho\in G}\sup_{m\in\mathbb Z}
 \frac1N\#\left\{m\leq x<m+N:
       \|\rho_{I,x}-\omega_I\|_1\geq\epsilon\right\}=0.
 \tag{2}
\]

Moreover,

\[
 \lim_{N\to\infty}\sup_{\rho\in G,m\in\mathbb Z}
 \frac1N\sum_{x=m}^{m+N-1}\|\rho_{I,x}-\omega_I\|_1=0.
 \tag{3}
\]

Every ground state with a finite translation period equals \(\omega\). More generally, a competing state cannot have a local discrepancy of fixed size on a set of positive upper Banach density. Here upper Banach density means the limit superior, as \(N\to\infty\), of the largest fraction of such positions in any interval of length \(N\).

## Proof

### 1. Compactness and translation averages

The state space of \(\mathfrak A\) is weak-* compact. It is metrizable because the union of local matrix algebras has a countable norm-dense subset. For each local \(B\), the observable in (1) is fixed and local. The requirement that its expectation is real and nonnegative is weak-* closed and convex. Intersecting these requirements shows that \(G\) is closed and convex, hence compact. Translation invariance of the interaction shows that \(\rho\circ\tau^x\in G\) for every \(\rho\in G\) and \(x\in\mathbb Z\).

Put

\[
 M_{N,m}(\rho)=\frac1N\sum_{x=m}^{m+N-1}\rho\circ\tau^x\in G.
\]

For any observable \(A\), cancellation of the common terms gives

\[
 \left|M_{N,m}(\rho)(\tau A)-M_{N,m}(\rho)(A)\right|
 =\frac1N\left|\rho(\tau^{m+N}A)-\rho(\tau^m A)\right|
 \leq\frac{2\|A\|}{N}.
 \tag{4}
\]

Consequently, for any sequence \(N_k\to\infty\), any \(m_k\), and any \(\rho_k\in G\), every convergent subsequence of \(M_{N_k,m_k}(\rho_k)\) has a translation-invariant limit in \(G\). By the uniqueness premise this limit is \(\omega\). Compactness then implies that the whole sequence converges to \(\omega\): otherwise there is a neighborhood of \(\omega\) missed along a subsequence, which has a further convergent subsequence and contradicts the preceding conclusion. In particular, for every fixed observable \(A\),

\[
 \sup_{\rho\in G,m\in\mathbb Z}
 \left|M_{N,m}(\rho)(A)-\omega(A)\right|\longrightarrow0.
 \tag{5}
\]

Indeed, failure of (5) supplies exactly a sequence contradicting that conclusion.

### 2. Purity prevents cancellation of local discrepancies

Fix a self-adjoint local observable \(A\) and a number \(t>0\). We show that the fraction of positions with

\[
 \rho(\tau^x A)-\omega(A)\geq t
 \tag{6}
\]

goes to zero uniformly over \(\rho\in G\) and intervals of length \(N\).

If not, there are \(\delta>0\), \(N_k\to\infty\), states \(\rho_k\in G\), intervals \(J_k=[m_k,m_k+N_k-1]\cap\mathbb Z\), and subsets \(E_k\subset J_k\) such that (6) holds at every \(x\in E_k\) and

\[
 p_k=|E_k|/N_k\geq\delta.
\]

Define

\[
 \sigma_k=\frac1{|E_k|}\sum_{x\in E_k}\rho_k\circ\tau^x\in G.
\]

If \(E_k\ne J_k\), let \(\eta_k\in G\) be the corresponding average over the complement. If \(E_k=J_k\), put \(\eta_k=\omega\). Then

\[
 M_{N_k,m_k}(\rho_k)=p_k\sigma_k+(1-p_k)\eta_k,
 \qquad \sigma_k(A)\geq\omega(A)+t.
 \tag{7}
\]

By compactness, after taking a subsequence we have \(p_k\to p\in[\delta,1]\), \(\sigma_k\to\sigma\in G\), and \(\eta_k\to\eta\in G\). Equations (5) and (7) give

\[
 \omega=p\sigma+(1-p)\eta,
 \qquad \sigma(A)\geq\omega(A)+t.
 \tag{8}
\]

If \(p=1\), the first equality says \(\sigma=\omega\), contrary to the second inequality. If \(0<p<1\), purity of \(\omega\) means that it is an extreme point of the full state space, so the first equality again forces \(\sigma=\eta=\omega\), a contradiction. This proves the assertion for (6). Applying it to \(-A\) proves the assertion for negative discrepancies as well. Taking the union of the two exceptional sets gives

\[
 \sup_{\rho\in G,m\in\mathbb Z}\frac1N
 \#\{m\leq x<m+N:|\rho(\tau^x A)-\omega(A)|\geq t\}
 \longrightarrow0.
 \tag{9}
\]

Purity is used for states on the full algebra in (8). No finite-block density matrix is assumed to be pure.

### 3. From finitely many observables to trace norm

Let \(d\) be the Hilbert-space dimension of block \(I\). Choose matrix units \(E_{ij}\) on that block and the following \(d^2\) self-adjoint observables of operator norm one:

\[
 P_i=E_{ii},\quad
 R_{ij}=E_{ij}+E_{ji},\quad
 T_{ij}=\mathrm i(E_{ij}-E_{ji})\quad(i<j).
\]

For a Hermitian matrix \(D\), write \(a_F=\operatorname{Tr}(DF)\) for each of these observables. Its diagonal entries are \(a_{P_i}\), while

\[
 2|D_{ij}|\leq |a_{R_{ij}}|+|a_{T_{ij}}|.
\]

Since a matrix unit has trace norm one, the triangle inequality applied to \(D=\sum_{ij}D_{ij}E_{ij}\) gives

\[
 \|D\|_1\leq\sum_{ij}|D_{ij}|
 \leq\sum_F|a_F|\leq d^2\max_F|a_F|.
 \tag{10}
\]

For \(D=\rho_{I,x}-\omega_I\), each \(a_F\) is \(\rho(\tau^xF)-\omega(F)\). Thus a position counted in (2) is counted in at least one of the \(d^2\) exceptional sets in (9), with \(t=\epsilon/d^2\). The union bound and (9) prove (2).

The trace norm distance of two density matrices is at most two. Splitting an interval into positions with distance less than \(\epsilon\) and its complement therefore gives

\[
 \frac1N\sum_x\|\rho_{I,x}-\omega_I\|_1
 \leq\epsilon+\frac2N\#\{x:\|\rho_{I,x}-\omega_I\|_1\geq\epsilon\}.
\]

Taking suprema, then the limit superior in \(N\), and finally \(\epsilon\downarrow0\), proves (3).

### 4. Finite translation periods

Suppose \(\rho\circ\tau^p=\rho\) for an integer \(p\geq1\). If \(\rho\ne\omega\), norm density of local observables supplies a local self-adjoint \(A\) with \(\rho(A)\ne\omega(A)\). Set \(t=|\rho(A)-\omega(A)|>0\). At every position divisible by \(p\), the discrepancy in (9) equals \(t\). Their density is \(1/p\), contradicting (9).

There is also a direct proof which does not use (2): the state

\[
 \overline\rho=\frac1p\sum_{r=0}^{p-1}\rho\circ\tau^r
\]

belongs to \(G\) and is translation invariant, hence equals \(\omega\). A finite convex decomposition of a pure state has all components equal to that state. Thus \(\rho=\omega\). For \(p=1\) this follows directly from the uniqueness premise. This completes the proposition.

## Checks on the argument and its limitation

An independent check of (10) uses the Hilbert–Schmidt norm:

\[
 \|D\|_2^2=\sum_i a_{P_i}^2+
 \tfrac12\sum_{i<j}(a_{R_{ij}}^2+a_{T_{ij}}^2)
 \leq d^2\max_F |a_F|^2.
\]

Cauchy–Schwarz on the \(d\) singular values gives
\(\|D\|_1\leq\sqrt d\|D\|_2\leq d^{3/2}\max_F|a_F|\), which is even stronger than (10). The count is \(d+2\binom d2=d^2\). For the spin-1 chain and a block of \(\ell\) sites, \(d=3^\ell\); the conservative threshold used in the proof is therefore \(\epsilon/9^\ell\).

The proposition does not imply that every ground state equals \(\omega\). A local discrepancy can have zero upper Banach density, as a single defect does. The following example shows why compactness, averaging and purity alone cannot remove that possibility.

On a chain of two-level sites, let \(\omega\) be the product state with every spin in \(|0\rangle\). Let \(\rho_z\) be the product state with spin \(|1\rangle\) at site \(z\) and \(|0\rangle\) everywhere else. Let \(K\) be the weak-* closed convex hull of \(\{\omega\}\cup\{\rho_z:z\in\mathbb Z\}\). It is compact, convex and translation invariant, and contains states different from \(\omega\).

Write \(n_x=|1\rangle\langle1|_x\). For every finite set \(F\) and every \(\sigma\in K\),

\[
 \sum_{x\in F}\sigma(n_x)\leq1,
 \tag{11}
\]

because this holds for the generators of \(K\) and is preserved under convex combinations and weak-* limits. If \(\sigma\in K\) is translation invariant, then \(\sigma(n_x)=c\geq0\), independently of \(x\). Taking \(|F|\) arbitrarily large in (11) gives \(c=0\).

For a finite block \(I\), the positive matrix \(N_I=\sum_{x\in I}n_x\) has kernel spanned by \(|0\rangle^{\otimes |I|}\), and \(N_I\geq1-|0\cdots0\rangle\langle0\cdots0|\). A density matrix with zero expectation of \(N_I\) is supported on this kernel: diagonalize \(N_I\), use positivity to eliminate its positive-eigenvalue diagonal entries, and then use \(|D_{ij}|^2\leq D_{ii}D_{jj}\) to eliminate the corresponding off-diagonal entries. Hence \(\sigma_I=|0\cdots0\rangle\langle0\cdots0|\). This holds for all \(I\), so \(\sigma=\omega\).

Thus \(K\) has exactly one invariant state and that state is pure, yet \(K\ne\{\omega\}\). To check purity, any nontrivial convex decomposition of \(\omega\) into states must restrict on each finite block to a decomposition of its rank-one density matrix; positivity forces both restrictions to equal that rank-one matrix. Density of local observables then forces both full states to equal \(\omega\).

For a block with \(\ell\) sites, at most \(\ell\) translates of the block contain the single defect of \(\rho_z\). The exceptional fraction is at most \(\ell/N\), while its nonzero trace distance is exactly two: the two block vectors are orthogonal, so their density-matrix difference has eigenvalues \(1,-1\) and otherwise zero. Thus, for every interval of positions and every generator of \(K\), the sum of the block trace distances is at most \(2\ell\). Convexity of trace norm preserves this upper bound under convex combinations. Continuity of each finite-block density matrix and its trace norm preserves it under weak-* limits. Consequently the mean distance is at most \(2\ell/N\) uniformly on all of \(K\), and the exceptional fraction at threshold \(\epsilon\) is at most \(2\ell/(N\epsilon)\). Both (2) and (3) hold, without equality of states. This example is a compact set of states, not an asserted ground-state set of a Heisenberg or other finite-range Hamiltonian. Its role is to identify precisely what the averaging argument cannot prove. Excluding such a sparse discrepancy for actual Heisenberg ground states still requires a further consequence of local stability (1).
