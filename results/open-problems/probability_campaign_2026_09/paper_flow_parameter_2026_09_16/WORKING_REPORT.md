# Aldous–Fill Open Problem 4.49(ii) fails for every constant

**Summary.** Open Problem 4.49(ii) of Aldous and Fill asks whether their inequality $\inf_{\mathbf f}\psi(\mathbf f)\le K\tau_2\log n$ (their (4.49)) remains true with the diameter $\Delta$ in place of $\log n$. It does not, for any constant $K$. For the simple random walk on the cone $K_1\vee H$ over a $d$-regular Ramanujan graph $H$ on $n$ vertices one has $\Delta=2$, $\tau_2\le(d+1)/(d+1-2\sqrt{d-1})<3.5$, and $\inf_{\mathbf f}\psi(\mathbf f)\to2(d+1)$ as $n\to\infty$, so that
$$\liminf_{n\to\infty}\frac{\inf_{\mathbf f}\psi(\mathbf f)}{\tau_2\,\Delta}\ \ge\ d+1-2\sqrt{d-1}\ \xrightarrow[d\to\infty]{}\ \infty .$$
The proof is short and self-contained apart from the existence of expander families with second eigenvalue $O(\sqrt d)$ (Lubotzky–Phillips–Sarnak, Morgenstern, Friedman). The same family defeats the length-weighted (Diaconis–Stroock/Sinclair) variant of the flow parameter, and the ratio is unbounded already on graphs of diameter two, so there is no finite sharp constant even there. What survives is $\inf_{\mathbf f}\psi(\mathbf f)\le 65\,\tau_2\,\Delta\log D$, $D$ the maximum degree, which follows from lemmas already in the book; the cones show that the factor $\log D$ cannot be lowered below $c\log D/\log\log D$.

---

## 1. The statement in the book

All quotations are from the online edition of D. Aldous and J. A. Fill, *Reversible Markov Chains and Random Walks on Graphs* (Chapter 3 dated September 10, 2002; Chapter 4 dated October 11, 1994; LaTeXML rendering of June 2, 2014), pages `Book_Ralph/Ch3.S3.html`, `Ch3.S7.html`, `Ch4.S3.html`, `Ch4.S4.html`, `Ch4.S7.html` at `stat.berkeley.edu/~aldous/RWG/`.

**Flows** (Chapter 3, §3.3.1). "A flow $\mathbf f=(f_{ij})$ on a graph is required only to satisfy the conditions
$$f_{ij}=\begin{cases}-f_{ji}&\text{if $(i,j)$ is an edge}\\ 0&\text{if not.}\end{cases}$$
So the net flow out of $i$ is $f_{(i)}:=\sum_{j\ne i}f_{ij}$, and by symmetry $\sum_i f_{(i)}=0$."

**Unit flow to a distribution** (Chapter 3, §3.7.2, (3.98)). "Given a probability distribution $\rho$ on vertices, a unit flow from $a$ to $\rho$ is a flow $f$ satisfying
$$f_{(i)}=1_{(i=a)}-\rho_i\quad\text{for all }i.\tag{3.98}$$"
The special flow $\mathbf f^{a\to\pi}$ of (3.99) is the mean net transition count of the chain started at $a$; the book notes that it is a unit flow from $a$ to $\pi$.

**The flow parameter** (Chapter 4, §4.3.5, Lemma 4.21). "Consider a family $\mathbf f=(\mathbf f^{(a)})$, where, for each state $a$, $\mathbf f^{(a)}$ is a unit flow from $a$ to the stationary distribution $\pi$. Define
$$\psi(\mathbf f)=\max_{\text{edges }(i,j)}\ \sum_a \pi_a\frac{|f^{(a)}_{ij}|}{\pi_i p_{ij}}$$
in discrete time, and substitute $q_{ij}$ for $p_{ij}$ in continuous time. Let $\mathbf f^{a\to\pi}$ be the special flow induced by the chain. Then
$$\psi(\mathbf f^{a\to\pi})\le\tau_1^{(4)}\le\Delta\,\psi(\mathbf f^{a\to\pi})$$
where $\Delta$ is the diameter of the transition graph."

So $\psi$ is a plain, length-free congestion: the load of the family on the directed edge $(i,j)$ measured against the stationary flow rate $\pi_ip_{ij}$ of that edge. No path lengths $|\gamma|$ enter. The setting is an arbitrary finite reversible chain; there is no regularity, bounded-degree or vertex-transitivity hypothesis in §4.3.5 or in the Notes.

**Relaxation time** (Chapter 4, §4.4). "$\tau_2=(1-\lambda_2)^{-1}$ in discrete time, $=\lambda_2^{-1}$ in continuous time", where in discrete time $1=\lambda_1>\lambda_2\ge\dots\ge\lambda_n\ge-1$ are the eigenvalues of $P$ (Chapter 3, §3.4). Note that $\lambda_2$ is the second largest eigenvalue, not the second largest in absolute value.

**The inequality and the problem** (Chapter 4, Notes on §4.3.5). "Sinclair [307] points out that 'hard' results of Leighton and Rao [224] on multicommodity flow imply
$$\inf_{\mathbf f}\psi(\mathbf f)\le K\tau_2\log n.\tag{4.49}$$
This follows from Corollary 4.22 and Lemma 4.23 when $\pi$ is uniform, but Sinclair posed

**Open Problem 4.49** (i) Is there a simple proof of (4.49) in general? (ii) Does (4.49) hold with the diameter $\Delta$ in place of $\log n$?"

Here $n$ is the number of states. Part (ii) asks whether there is a universal constant $K$ with
$$\inf_{\mathbf f}\psi(\mathbf f)\ \le\ K\,\tau_2\,\Delta\qquad\text{for every finite reversible chain.}\tag{Q}$$
Everything below concerns the simple random walk on a finite connected simple graph $G=(V,E)$, $|E|=m$: a reversible chain with $\pi_x=\deg(x)/2m$ and $\pi_xp_{xy}=1/2m$ on every edge. A counterexample in this class refutes (Q) as stated. Write
$$F(G):=\inf_{\mathbf f}\psi(\mathbf f)=2m\ \inf_{\mathbf f}\ \max_{e\in E}\ \sum_{a\in V}\pi_a|f^{(a)}_e| ,$$
the infimum over all families $\mathbf f=(\mathbf f^{(a)})_{a\in V}$ of unit flows from $a$ to $\pi$. Since $|f^{(a)}_{ij}|=|f^{(a)}_{ji}|$ and $\pi_ip_{ij}=\pi_jp_{ji}$, the maximum over directed edges is a maximum over undirected edges.

---

## 2. A lower bound on $F(G)$ from edge lengths

For $\ell:E\to[0,\infty)$ let $d_\ell$ be the shortest-path metric of the edge lengths $\ell$.

**Lemma 1.** For every $\ell:E\to[0,\infty)$ with $\sum_e\ell_e>0$,
$$F(G)\ \ge\ \frac{2m\sum_{a,v\in V}\pi_a\pi_v\,d_\ell(a,v)}{\sum_{e\in E}\ell_e}.$$

*Proof.* Fix $a$ and a unit flow $\mathbf f$ from $a$ to $\pi$, and put $\varphi(v)=d_\ell(a,v)$; then $\varphi(a)=0$ and $|\varphi(i)-\varphi(j)|\le\ell_{ij}$ for every edge. Using $f_{(v)}=1_{(v=a)}-\pi_v$ and antisymmetry,
$$\sum_v\pi_v\varphi(v)=-\sum_v f_{(v)}\varphi(v)=-\sum_{v}\sum_{j}f_{vj}\varphi(v)=\tfrac12\sum_{v,j}f_{vj}\bigl(\varphi(j)-\varphi(v)\bigr)\le\tfrac12\sum_{(v,j)}|f_{vj}|\,\ell_{vj}=\sum_{e\in E}|f_e|\,\ell_e .$$
Multiply by $\pi_a$, sum over $a$, and use $\sum_a\pi_a|f^{(a)}_e|\le\psi(\mathbf f)\,\pi_ip_{ij}=\psi(\mathbf f)/2m$ on each edge:
$$\sum_{a,v}\pi_a\pi_v d_\ell(a,v)\le\sum_e\ell_e\sum_a\pi_a|f^{(a)}_e|\le\frac{\psi(\mathbf f)}{2m}\sum_e\ell_e .$$
Take the infimum over $\mathbf f$. $\square$

Lemma 1 is the weak-duality half of linear-programming duality for the maximum concurrent flow problem with demand $\pi_a\pi_v$ between each ordered pair and capacity $1/2m$ on each edge (Shahrokhi–Matula; Leighton–Rao). Strong duality, not needed for the theorem, says the right-hand side is attained: $F(G)=\max_\ell 2m\sum_{a,v}\pi_a\pi_vd_\ell(a,v)/\sum_e\ell_e$. The linear programs of §5 compute this optimum.

Taking $\ell$ to be the indicator of the edges of a cut $(A,A^c)$ gives $F(G)\ge2\pi(A)\pi(A^c)/Q(A,A^c)$, i.e. $F(G)\ge2\tau_c$ in the notation of §4.5 of the book; since $\tau_c\le\tau_2$, this cut bound alone can never contradict (Q). The certificates below are not cut certificates.

---

## 3. Cones over regular graphs

Let $H$ be a connected $d$-regular graph on $n$ vertices, $d\ge3$, $n\ge d+2$ (so $H$ is not complete). Let $G=K_1\vee H$ be the cone: $V(G)=V(H)\cup\{h\}$, the hub $h$ adjacent to every vertex of $H$. Then $G$ has $n+1$ vertices and
$$m=\tfrac{nd}2+n=\tfrac{n(d+2)}2,\qquad \deg h=n,\quad \deg v=d+1\ (v\in V(H)),$$
$$\pi_h=\frac1{d+2},\qquad \pi_v=\frac{d+1}{n(d+2)},\qquad \pi_B:=\pi(V(H))=\frac{d+1}{d+2}.$$
Write $\mu_1=d\ge\mu_2\ge\dots\ge\mu_n$ for the adjacency eigenvalues of $H$.

**Lemma 2 (diameter and spectrum).** $\Delta(G)=2$. The eigenvalues of the transition matrix $P$ of the simple random walk on $G$ are
$$1,\qquad -\frac1{d+1},\qquad \frac{\mu_i}{d+1}\ (i=2,\dots,n),$$
so $\lambda_2(P)=\mu_2/(d+1)$ and
$$\tau_2(G)=\frac{d+1}{d+1-\mu_2(H)} .$$

*Proof.* Every vertex is adjacent to $h$, so any two vertices are at distance at most $2$; since $H$ is not complete, some two base vertices are non-adjacent, so $\Delta=2$. For an eigenvector $z\perp\mathbf 1$ of $A_H$ with eigenvalue $\mu$, extend $z$ by $0$ at $h$: at a base vertex $v$, $(Pz)_v=\frac1{d+1}\bigl(\sum_{w\sim_H v}z_w+z_h\bigr)=\frac{\mu}{d+1}z_v$, and $(Pz)_h=\frac1n\sum_vz_v=0$. This gives $n-1$ independent eigenvectors with eigenvalues $\mu_i/(d+1)$, $i\ge2$. On the complementary two-dimensional space of vectors constant on $V(H)$, $P$ acts, in the basis (value at $h$, value on the base), by $\begin{pmatrix}0&1\\ \frac1{d+1}&\frac d{d+1}\end{pmatrix}$, with eigenvalues $1$ and $-\frac1{d+1}$. Since $H$ is not complete it has two non-adjacent vertices, and Cauchy interlacing with that induced subgraph gives $\mu_2\ge0>-1$; hence the second largest eigenvalue of $P$ is $\mu_2/(d+1)$. $\square$

**Lemma 3 (routing through the hub).** $F(G)\le 2(d+1)\bigl(1-\pi_v\bigr)=2(d+1)\Bigl(1-\frac{d+1}{n(d+2)}\Bigr)<2(d+1)$.

*Proof.* Take the family in which every unit of flow travels through the hub: for a base vertex $a$, $f^{(a)}_{ah}=1-\pi_a$ and $f^{(a)}_{hw}=\pi_w$ for base $w\ne a$; for the hub, $f^{(h)}_{hw}=\pi_w$; all other values are $0$ or forced by antisymmetry. Each $\mathbf f^{(a)}$ is a unit flow from $a$ to $\pi$ (for $a\ne h$ the net outflow at $h$ is $(1-\pi_a-\pi_h)-(1-\pi_a)=-\pi_h$). Base edges carry nothing. On the spoke $\{h,v\}$ the load is
$$\sum_a\pi_a|f^{(a)}_{hv}|=\pi_v(1-\pi_v)+\pi_h\pi_v+\sum_{w\ne v,\ w\ne h}\pi_w\pi_v=2\pi_v(1-\pi_v),$$
so $\psi(\mathbf f)=2m\cdot2\pi_v(1-\pi_v)=2(d+1)(1-\pi_v)$, using $2m\pi_v=\deg v=d+1$. $\square$

**Lemma 4 (a two-length certificate).** For an integer $r\ge1$ put
$$B_r:=d+d(d-1)+\dots+d(d-1)^{r-2}=\frac{d\bigl((d-1)^{r-1}-1\bigr)}{d-2}\qquad(B_1=0).$$
Then
$$F(G)\ \ge\ V_r:=2L\Bigl[\pi_h\pi_B+\pi_v^2\sum_{u\ne v\in V(H)}\min\Bigl(\frac{\mathrm{dist}_H(u,v)}r,1\Bigr)\Bigr],\qquad L:=\frac{(d+2)\,r}{r+d},$$
and
$$F(G)\ \ge\ 2(d+1)\cdot\frac r{r+d}\cdot\Bigl(1-\frac{1+B_r}n\Bigr).$$

*Proof.* Give every base edge the length $b=2L/r=2(d+2)/(r+d)$ and every spoke the length $L$. Then $\sum_e\ell_e=\frac{nd}2b+nL=nL\bigl(\frac dr+1\bigr)=n(d+2)=2m$, so Lemma 1 reads $F(G)\ge\sum_{a,v}\pi_a\pi_vd_\ell(a,v)$. A path from $h$ to a base vertex starts with a spoke, so $d_\ell(h,v)=L$. A path between base vertices $u,v$ either stays in $H$, with length at least $b\,\mathrm{dist}_H(u,v)$, or passes through $h$, with length at least $2L$; both bounds are attained, so $d_\ell(u,v)=\min(b\,\mathrm{dist}_H(u,v),2L)=2L\min(\mathrm{dist}_H(u,v)/r,1)$. Summing over ordered pairs gives $V_r$.

For the second bound, in a graph of maximum degree $d$ the number of vertices at distance between $1$ and $r-1$ from a given vertex is at most $B_r$, so at least $n(n-1)-nB_r$ ordered pairs $(u,v)$ of distinct base vertices have $\mathrm{dist}_H(u,v)\ge r$. Hence
$$V_r\ge2L\bigl[\pi_h\pi_B+\pi_v^2\,n(n-1-B_r)\bigr]=2L\pi_B\Bigl[\pi_h+\pi_B-\pi_B\frac{1+B_r}n\Bigr]\ge2L\pi_B\Bigl(1-\frac{1+B_r}n\Bigr),$$
and $L\pi_B=(d+1)r/(r+d)$. $\square$

**Theorem 5.** Let $d\ge3$ and let $H$ be a connected $d$-regular graph on $n\ge d+2$ vertices with second adjacency eigenvalue $\mu_2$. For the simple random walk on $G=K_1\vee H$, $\Delta(G)=2$, $\tau_2(G)=(d+1)/(d+1-\mu_2)$, and for every integer $r\ge1$
$$2(d+1)\,\frac r{r+d}\Bigl(1-\frac{1+B_r}n\Bigr)\ \le\ F(G)\ \le\ 2(d+1)\Bigl(1-\frac{d+1}{n(d+2)}\Bigr).$$
Consequently
$$\frac{F(G)}{\tau_2(G)\,\Delta(G)}\ \ge\ (d+1-\mu_2)\cdot\frac r{r+d}\cdot\Bigl(1-\frac{1+B_r}n\Bigr).\tag{5.1}$$

*Proof.* Lemmas 2, 3 and 4. $\square$

**Corollary 6.** Let $(H_k)$ be connected $d$-regular graphs on $n_k\to\infty$ vertices with $\mu_2(H_k)\le\beta$ for all $k$. Then $F(K_1\vee H_k)\to2(d+1)$ and
$$\liminf_{k\to\infty}\frac{F(K_1\vee H_k)}{\tau_2\,\Delta}\ \ge\ d+1-\beta .$$

*Proof.* In (5.1) let $r=r_k\to\infty$ so slowly that $(d-1)^{r_k}=o(n_k)$; then $B_{r_k}/n_k\to0$ and $r_k/(r_k+d)\to1$. The convergence $F\to2(d+1)$ uses only the two-sided bound of Theorem 5 and holds for every $d$-regular sequence. $\square$

**Theorem 7 (answer to Open Problem 4.49(ii)).** For every $K<\infty$ there is a finite connected simple graph $G$ of diameter $2$ whose simple random walk satisfies
$$\inf_{\mathbf f}\psi(\mathbf f)\ >\ K\,\tau_2\,\Delta .$$
Hence (4.49) does not hold with $\Delta$ in place of $\log n$ for any universal constant, not even for simple random walks on graphs of diameter two, and $\sup_G F(G)/(\tau_2\Delta)=\infty$.

*Proof.* Let $p\equiv1\pmod 4$ be prime. For every prime $q\equiv1\pmod4$, $q\ne p$, Lubotzky, Phillips and Sarnak construct a connected $(p+1)$-regular Cayley graph $X^{p,q}$ of $\mathrm{PSL}_2(\mathbb F_q)$ (when $p$ is a quadratic residue modulo $q$; then $X^{p,q}$ is not bipartite and has $q(q^2-1)/2$ vertices) or of $\mathrm{PGL}_2(\mathbb F_q)$ (otherwise; bipartite, $q(q^2-1)$ vertices), all of whose eigenvalues other than $\pm(p+1)$ satisfy $|\mu|\le2\sqrt p$. By Dirichlet's theorem there are infinitely many primes $q\equiv1\pmod{4p}$, and for these $p$ is a residue modulo $q$ by quadratic reciprocity. Apply Corollary 6 to the non-bipartite graphs $X^{p,q}$, $q\to\infty$, with $d=p+1$ and $\beta=2\sqrt p$:
$$\liminf_{q\to\infty}\frac{F(K_1\vee X^{p,q})}{\tau_2\Delta}\ \ge\ p+2-2\sqrt p=(\sqrt p-1)^2+1\xrightarrow[p\to\infty]{}\infty .$$
Given $K$, choose $p$ with $(\sqrt p-1)^2+1>K$ and then $q$ large. Morgenstern's graphs give the same for every prime power $p$. Alternatively, by Friedman's theorem a uniformly random $d$-regular graph on $n$ vertices ($nd$ even) has all eigenvalues other than $d$ of absolute value at most $2\sqrt{d-1}+\varepsilon$ with probability tending to $1$ as $n\to\infty$; such a graph is connected and non-bipartite, and Corollary 6 applies with $\beta=2\sqrt{d-1}+\varepsilon$. $\square$

An explicit form of the quantifiers: with $r=3d$ and $n\ge2(1+B_{3d})$, (5.1) gives $F/(\tau_2\Delta)\ge\frac38(d+1-\mu_2)$; so for $p=101$, $d=102$, any Ramanujan $H$ on $n\ge2(1+B_{306})$ vertices gives a ratio above $\frac38(103-2\sqrt{101})>30$.

**Remarks.**

1. *No hidden hypothesis is being violated.* $G$ is a finite connected simple graph, the chain is the simple random walk, $\pi_xp_{xy}=1/2m$, the flows are unit flows from $a$ to $\pi$ in the sense of (3.98), $\psi$ is the quantity of Lemma 4.21, $\tau_2=(1-\lambda_2)^{-1}$, and $\Delta$ is the diameter of the transition graph. The general-chain form (Q) is refuted a fortiori. In continuous time $q_{ij}=p_{ij}$, $\psi$ and $\tau_2$ are unchanged, and so is the counterexample.

2. *Absolute spectral gap.* With non-bipartite $H$ as in the proof, all eigenvalues of $P$ other than $1$ lie in $[-\frac1{d+1},\frac{2\sqrt{d-1}}{d+1}]$ (or with $+\varepsilon$), so the conclusion also holds if $\tau_2$ is replaced by the absolute relaxation time $(1-\max(\lambda_2,|\lambda_{\min}|))^{-1}$. (For bipartite $H$ the eigenvalue $-d/(d+1)$ would make the absolute version of order $d$, which is why the non-bipartite graphs are chosen.)

3. *Why the answer is $2(d+1)$.* The spokes carry total stationary flow rate $n/2m=\pi_h=1/(d+2)$, and all traffic to or from a base vertex must leave it along its single spoke or along one of its $d$ base edges. The base has $d/2$ times the total capacity of the spokes, but in a $d$-regular graph on $n\gg(d-1)^r$ vertices almost all pairs are at distance $\ge r$, so base routing costs at least $r$ units of capacity per unit of demand against $2$ units through the hub; when $r\gg d$ the base is useless for typical pairs and the spokes are a bottleneck at every base vertex, with congestion $2(d+1)$. The cut bound sees none of this: the cut $\{h\}$ versus $V(H)$ gives only $2\pi_h\pi_B/(n/2m)=2(d+1)/(d+2)$, and $\tau_c(G)\le\tau_2(G)$ stays bounded.

4. *Ceiling of the construction.* By the Alon–Boppana bound, $\mu_2(H)\ge2\sqrt{d-1}-o(1)$ for $d$-regular graphs with $n\to\infty$, so within cones over $d$-regular graphs the limiting ratio cannot exceed $d+1-2\sqrt{d-1}$; Ramanujan bases are optimal for this family. For $d=3,4,5,6,7,10,17$ the limits are $1.17,\ 1.54,\ 2,\ 2.53,\ 3.10,\ 5,\ 10$. The projective-plane cones $K_1\vee\mathrm{Inc}(\mathrm{PG}(2,t^2))$ of the earlier record, whose bases have diameter three, give $5/2$ in the limit; the expander cones pass them from $d=6$ on.

5. *The length-weighted parameter.* For a family presented as path flows $\{f^{(a)}(\gamma)\}$ (each $\mathbf f^{(a)}$ decomposed into $a\to v$ paths carrying total $\pi_v$), the variant used by Diaconis–Stroock and Sinclair is $\bar\rho(\mathbf f)=\max_e\frac1{\pi_ip_{ij}}\sum_a\pi_a\sum_{\gamma\ni e}|\gamma|\,f^{(a)}(\gamma)$. Since $|\gamma|\ge1$, $\bar\rho(\mathbf f)\ge\psi(\mathbf f)\ge F(G)$ for every path family, while the hub routing of Lemma 3 uses paths of length at most $2$ and has $\bar\rho\le2\psi<4(d+1)$. So on the cones $\inf\bar\rho$ lies between $F(G)$ and $4(d+1)$, and $\inf\bar\rho/(\tau_2\Delta)\to\infty$ as well: the answer to (ii) is negative in either normalisation.

---

## 4. What remains true, and what remains open

**Proposition 8.** For every finite reversible discrete-time chain,
$$\inf_{\mathbf f}\psi(\mathbf f)\ \le\ \frac{16e}{e-1}\ \tau_2\Bigl(1+\tfrac12\log\frac1{\pi_*}\Bigr),\qquad \pi_*=\min_i\pi_i .$$
For the simple random walk on a connected simple graph with maximum degree $D\ge3$ and diameter $\Delta$,
$$\inf_{\mathbf f}\psi(\mathbf f)\ \le\ 65\ \tau_2\,\Delta\,\log D .$$

*Proof.* Chain the book's lemmas: $\inf_{\mathbf f}\psi(\mathbf f)\le\psi(\mathbf f^{a\to\pi})\le\tau_1^{(4)}$ (Lemma 4.21), $\tau_1^{(4)}\le4\tau_1^{(3)}$ (Lemma 4.13), $\tau_1^{(3)}\le\tau_1^{(2)}$ (Lemma 4.12), and $\tau_1^{(2)}\le\frac{4e}{e-1}\tau_2(1+\frac12\log\frac1{\pi_*})$ in discrete time (Lemma 4.23). For a graph of maximum degree $D\ge3$ and diameter $\Delta$, $n\le1+D\bigl((D-1)^\Delta-1\bigr)/(D-2)\le4D^\Delta$ and $1/\pi_*=2m/\delta_{\min}\le nD\le4D^{\Delta+1}$, so $1+\frac12\log\frac1{\pi_*}\le1+\log2+\frac12(\Delta+1)\log D\le\bigl(1+\frac{1.7}{\log3}\bigr)\Delta\log D\le2.55\,\Delta\log D$, and $\frac{16e}{e-1}\cdot2.55<65$. $\square$

So the diameter form of (4.49) holds with a constant depending on the maximum degree, $K(D)=O(\log D)$; in particular the answer to (ii) is affirmative on any class of graphs of bounded degree. The first inequality of Proposition 8 is the elementary route the book mentions for uniform $\pi$, with $\log(1/\pi_*)$ in place of $\log n$. Theorem 5 shows that the dependence on $D$ is nearly sharp: the cone $K_1\vee H$ has $D=n$, and with $r=3d$, $n=2(1+B_{3d})$ one has $\log n\le3d\log d+3$, hence $d\ge c\log n/\log\log n$ and
$$\frac{F(K_1\vee H)}{\tau_2\Delta}\ \ge\ \frac38\bigl(d+1-2\sqrt{d-1}\bigr)\ \ge\ c'\,\frac{\log D}{\log\log D}$$
for Ramanujan $H$. Closing the gap between $\log D/\log\log D$ and $\log D$ is open.

Two restrictions of (ii) remain open as far as I can tell: **regular graphs** and **vertex-transitive graphs**. The mechanism of §3 needs one vertex of degree comparable to $n$ next to vertices of bounded degree. In a regular graph of diameter two every degree is at least $\sqrt{n-1}$ (Moore bound), so no vertex can have most of its edges leading into a "useless" sparse part; whether some other mechanism makes $F/(\tau_2\Delta)$ unbounded on regular graphs is not settled here.

On the sharp constant: there is none in any diameter class that contains the cones, i.e. already for $\Delta=2$ (Theorem 7). The largest ratios attained by graphs of computable size still come from the projective-plane cones of the earlier record ($2.07$ at $4903$ vertices, limit $5/2$), because the expander cones need $n\gg(d-1)^{3d}$ before (5.1) takes effect (§5.5).

---

## 5. Computations

All computations are in `scratch/af449/` (`af449lib.py`, `test0.py`, `test1.py`, `check_exact.py`, `rr_lp_worker.py`, `rr_dual_large.py`, `lps_cone.py`, `make_tables.py`). $F(G)$ is computed as the optimal value of the linear program
$$\min\lambda\quad\text{s.t.}\quad \sum_{j}(x^{a}_{xj}-x^{a}_{jx})=1_{(x=a)}-\pi_x\ \ (a,x\in V),\qquad \sum_a\deg(a)\,(x^a_{e^+}+x^a_{e^-})\le\lambda\ \ (e\in E),\qquad x\ge0,$$
which is the definition of $F$ after the substitution $f^{(a)}_e=x^a_{e^+}-x^a_{e^-}$ and multiplication of the congestion constraint by $2m$ (scipy `linprog`, HiGHS). Dual certificates are evaluated in exact rational arithmetic (`fractions.Fraction`; Dijkstra with integer weights for general length functions), so every certificate column below is a rigorous lower bound for the graph in question; LP values carry the solver's tolerance (about $10^{-8}$).

**5.1 Sanity checks of the LP against known exact values.** $F(K_n)=2(n-1)/n$ for $n=3,\dots,6$; the wheel $K_1\vee C_5$ gives $21/10$; the cones over the Petersen graph and the Paley graph on $13$ vertices reproduce the earlier record's formula $F(K_1\vee\mathrm{srg}(q,r,\lambda,\mu))=2(r+1)(2q-r-1)/(q(r+2))$ ($64/25$ and $133/52$). The eigenvalues of $P$ on cones over random regular graphs, over the Petersen graph and over the bipartite incidence graph of $\mathrm{PG}(2,3)$ agree with Lemma 2 to $10^{-15}$. The hub routing, built as an explicit flow family and evaluated exactly, has $\psi=2(d+1)(1-\pi_v)$ (Lemma 3). The exact Dijkstra evaluation of the two-length certificate agrees with the closed form $V_r$ of Lemma 4 and dominates the ball bound. On wheels $K_1\vee C_n$ (a base with long distances and $d=2$, outside the range $d\ge3$ of Lemma 4 but with the same certificate) the LP optimum equals the best two-length certificate exactly, $F=3.85,\ 4.37885,\ 4.80$ at $n=30,60,120$, and rises towards $2(d+1)=6$ at the rate $r/(r+d)$ that Theorem 5 predicts (`wheel_check.py`).

**5.2 The projective-plane cones of the earlier record.** The certificate of Lemma 4 with $r=3$ (spokes $3/2$ times as long as base edges), evaluated on the distance layers $1,\ s+1,\ s(s+1),\ s^2$ of $\mathrm{Inc}(\mathrm{PG}(2,s))$, coincides with the record's closed form $L(s)=(s+2)(5s^3+19s^2+13s+8)/((s+3)(s+4)(s^2+s+1))$ for $s=2,3,4,5,7,8,9,11,13,49$; at $s=49$ it is $10786653/2251652$, $\tau_2=51/44$, and the gap to $2\tau_2\Delta=51/11$ is $3818931/24768172>0$, as recorded. The LP gives the exact optimum on the small members ($\tau_2=(s+2)/(s+2-\sqrt s)$ by Lemma 2, since $\mu_2=\sqrt s$):

| $s$ | $\lvert V(G)\rvert$ | $F$ (LP) | $F$ exact $=L(s)$ | $\tau_2$ | $F/(\tau_2\Delta)$ |
|---|---|---|---|---|---|
| 2 | 15 | 2.857142857 | $20/7$ | 1.546918 | 0.9235 |
| 3 | 27 | 3.232600733 | $1765/546$ | 1.530012 | 1.0564 |
| 4 | 43 | 3.489795918 | $171/49$ | 1.500000 | 1.1633 |
| 5 | 63 | 3.678763441 | $2737/744$ | 1.469374 | 1.2518 |
| 7 | 115 | 3.940191388 | $1647/418$ | 1.416375 | 1.3909 |
| 49 | 4903 | (not run) | $\ge 10786653/2251652=4.790551$ | $51/44$ | $\ge 2.0665$ |

On these members the record's certificate is the exact value of $F$ (agreement to $10^{-9}$), and $F/(\tau_2\Delta)$ climbs slowly towards the family's limit $5/2$.

**5.3 Cones over random regular graphs (LP).** $H$ is `networkx.random_regular_graph(d,n,seed)` with the first connected seed. Columns: $\mu_2(H)$, $\tau_2=(d+1)/(d+1-\mu_2)$, diameter and mean distance of $H$, the best two-length certificate $\max_rV_r$ (exact), $F$ by LP, the hub bound of Lemma 3, the ratio $F/(\tau_2\Delta)$ with $\Delta=2$, and the value $d+1-\mu_2$ that the ratio would take if $F$ were $2(d+1)$.

| $d$ | $n$ | $\mu_2(H)$ | $\tau_2$ | diam $H$ | mean dist $H$ | best $V_r$ (exact) | $r$ | $F$ (LP) | hub bound | $F/(\tau_2\Delta)$ | $d+1-\mu_2$ |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 3 | 20 | 2.6659 | 2.9984 | 6 | 2.91 | 3.3600 | 4 | 4.0000 | 7.6800 | 0.667 | 1.334 |
| 3 | 40 | 2.7044 | 3.0875 | 7 | 3.60 | 3.8057 | 4 | 4.2900 | 7.8400 | 0.695 | 1.296 |
| 3 | 80 | 2.7383 | 3.1703 | 8 | 4.50 | 4.2873 | 5 | 4.4193 | 7.9200 | 0.697 | 1.262 |
| 3 | 160 | 2.7783 | 3.2741 | 9 | 5.42 | 4.6534 | 6 | 4.6978 | 7.9600 | 0.717 | 1.222 |
| 4 | 20 | 3.0224 | 2.5284 | 4 | 2.18 | 3.1726 | 3 | 3.5985 | 9.5833 | 0.712 | 1.978 |
| 4 | 40 | 3.2585 | 2.8711 | 5 | 2.73 | 3.6443 | 3 | 3.8487 | 9.7917 | 0.670 | 1.742 |
| 4 | 80 | 3.3683 | 3.0644 | 6 | 3.36 | 4.1686 | 4 | 4.2047 | 9.8958 | 0.686 | 1.632 |
| 5 | 20 | 3.1229 | 2.0854 | 3 | 1.89 | 2.9507 | 3 | 3.3673 | 11.4857 | 0.807 | 2.877 |
| 5 | 40 | 3.5751 | 2.4743 | 4 | 2.40 | 3.6048 | 3 | 3.6096 | 11.7429 | 0.729 | 2.425 |
| 5 | 80 | 3.9329 | 2.9026 | 5 | 2.90 | 4.0290 | 4 | 4.0943 | 11.8714 | 0.705 | 2.067 |
| 6 | 20 | 3.5153 | 2.0088 | 3 | 1.78 | 2.8875 | 2 | 3.0555 | 13.3875 | 0.761 | 3.485 |
| 6 | 40 | 4.2180 | 2.5162 | 4 | 2.23 | 3.5284 | 3 | 3.6462 | 13.6937 | 0.725 | 2.782 |
| 8 | 40 | 4.2066 | 1.8776 | 3 | 1.91 | 3.2302 | 3 | 3.2432 | 17.5950 | 0.864 | 4.793 |

**5.4 Larger cones (certificate only).** For $n$ beyond the reach of the LP, the table reports the exact two-length certificate (a rigorous lower bound on $F$ for that graph), the ball bound of Lemma 4 (which uses nothing about $H$ beyond $d$ and $n$), the hub bound, and the resulting rigorous lower bound on $F/(\tau_2\Delta)$. The last table does the same for the Lubotzky–Phillips–Sarnak graphs $X^{5,q}$ themselves, built from the six quaternions of norm $5$ as $2\times2$ matrices over $\mathbb F_q$; the computed $\mu_2$ confirms the Ramanujan bound $2\sqrt5$.

| $d$ | $n$ | $\mu_2(H)$ | $\tau_2$ | diam $H$ | mean dist $H$ | best $V_r$ (exact) | $r$ | ball bound | hub bound | $V_r/(\tau_2\Delta)$ | $d+1-\mu_2$ |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 3 | 1000 | 2.8230 | 3.3985 | 13 | 8.05 | 5.4276 | 8 | 4.93227(r=6) | 7.9936 | 0.799 | 1.177 |
| 3 | 4000 | 2.8237 | 3.4006 | 15 | 10.05 | 5.8205 | 10 | 5.38720(r=7) | 7.9984 | 0.856 | 1.176 |
| 3 | 16000 | 2.8260 | 3.4073 | 17 | 12.05 | 6.1214 | 11 | 5.77020(r=9) | 7.9996 | 0.898 | 1.174 |
| 4 | 1000 | 3.4472 | 3.2199 | 9 | 5.63 | 5.4871 | 6 | 4.81019(r=5) | 9.9917 | 0.852 | 1.553 |
| 4 | 4000 | 3.4603 | 3.2474 | 10 | 6.89 | 6.0004 | 7 | 5.39375(r=6) | 9.9979 | 0.924 | 1.540 |

| $p$ | $q$ | $n=\lvert V(H)\rvert$ | $d$ | simple, $6$-regular | $\mu_2(H)$ | $2\sqrt p$ | $\tau_2$ | diam $H$ | mean dist | best $V_r$ | $r$ | ball bound | hub bound | $V_r/(\tau_2\Delta)$ | $d+1-\mu_2$ |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 5 | 13 | 2184 | 6 | True | 4.2497 | 4.4721 | 2.5452 | 7 | 4.83 | 5.8695 | 5 | 5.18045(r=4) | 13.9944 | 1.153 | 2.750 |
| 5 | 17 | 4896 | 6 | True | 4.3089 | 4.4721 | 2.6012 | 9 | 5.36 | 6.2202 | 6 | 5.41285(r=4) | 13.9975 | 1.196 | 2.691 |
| 5 | 29 | 12180 | 6 | True | 4.4420 | 4.4721 | 2.7365 | 8 | 5.77 | 6.5699 | 6 | 5.93528(r=5) | 13.9990 | 1.200 | 2.558 |

**5.5 Where finite $n$ stands relative to the theorem.** The certificate needs most pairs of $H$ at distance $\ge r$ with $r$ several times $d$: (5.1) with $r=3d$ needs $n\gg B_{3d}\approx(d-1)^{3d}$, which is about $10^{2.7}$ for $d=3$, $10^{5.7}$ for $d=4$, $10^{9}$ for $d=5$ and $10^{12.6}$ for $d=6$. The LP is feasible up to a few hundred vertices, the certificate computation up to some $10^4$–$10^5$. So the numerics display the mechanism for $d=3$ and $d=4$ ($F$ and the certificate rising with $n$ towards $2(d+1)$, the ratio rising with $n$), but they cannot reach the regime in which the ratio exceeds the record's $5/2$; that regime is reached by the proof, not by computation. At the sizes in the tables the base graphs have diameter comparable to $d$, so base routing is still competitive with the hub and $F$ sits well below $2(d+1)$. Random regular graphs at these sizes also have $\mu_2$ somewhat above $2\sqrt{d-1}$, which lowers $d+1-\mu_2$ relative to the Ramanujan value.

---

## 6. Prior art

Searches performed on 2026-09-16: web searches for "Open Problem 4.49" together with Aldous–Fill, flow parameter, diameter; for Sinclair's *Improved bounds for mixing rates of Markov chains and multicommodity flow* (Combin. Probab. Comput. 1 (1992) 351–370) and its converse statements; for Kahale's *A semidefinite bound for mixing rates of Markov chains* (IPCO 1996; Random Structures Algorithms 11 (1997)); for Leighton–Rao (J. ACM 46 (1999)) flow/cut gaps with product demands; and for the phrases "flow parameter", "relaxation time", "diameter", "cannot be replaced" in the Markov-chain literature. Findings: Sinclair's paper states the partial converse that for reversible $P$ there is a flow $f$ with $\rho(f)\le c\,\tau_{\rm mix}$ and $\ell(f)\le c'\tau_{\rm mix}$ (the flow generated by the chain itself, which is the content of the book's Lemma 4.21) and derives the $\log n$ bound from Leighton–Rao; Kahale shows that his semidefinite (flow) bound is within a factor $O(\log^2n)$ of the spectral gap and that this can be tight; neither addresses the diameter question. The Leighton–Rao gap examples are expanders, on which $\log n$ and $\Delta$ are comparable, which is presumably why the diameter version looked plausible. I found no published resolution of 4.49(ii) and no earlier appearance of the cone family in this role. A negative search is not evidence of novelty: that a hub attached to an expander has bounded relaxation time and mixing time of order the base degree is folklore, and Theorem 5 is a quantitative version of that observation for the flow parameter.

---

## 7. What was checked

Exact (rational) verification: the record's $\mathrm{PG}(2,49)$ numbers ($\tau_2=51/44$, certificate $10786653/2251652$, gap $3818931/24768172$); agreement of the two-length routine with the record's closed form $L(s)$ at ten values of $s$; agreement of the generic Dijkstra dual evaluator with the closed form $V_r$; the inequality $V_r\ge$ ball bound; the hub routing's exact $\psi$. Numerical verification: Lemma 2's spectrum on three cones (error $10^{-15}$); the LP against $K_n$, $W_6$ and two strongly regular cones with known exact values; the LP against the record's certificate on five projective-plane cones (equality); the Ramanujan property of the constructed $X^{5,q}$. The weakest step of the argument is the appeal to the existence of $d$-regular expander families with $\mu_2\le2\sqrt{d-1}$ (Lubotzky–Phillips–Sarnak, Morgenstern) or $\le2\sqrt{d-1}+\varepsilon$ (Friedman); everything else is elementary and written out above. The LP values in §5.3 are floating-point optima, not proofs; the rigorous content of the tables is in the certificate columns.

**References.** D. Aldous, J. A. Fill, *Reversible Markov Chains and Random Walks on Graphs*, online, Chapters 3–4. A. Sinclair, Improved bounds for mixing rates of Markov chains and multicommodity flow, Combin. Probab. Comput. 1 (1992) 351–370. T. Leighton, S. Rao, Multicommodity max-flow min-cut theorems and their use in designing approximation algorithms, J. ACM 46 (1999) 787–832. F. Shahrokhi, D. W. Matula, The maximum concurrent flow problem, J. ACM 37 (1990) 318–334. N. Kahale, A semidefinite bound for mixing rates of Markov chains, Random Structures Algorithms 11 (1997) 299–313. A. Lubotzky, R. Phillips, P. Sarnak, Ramanujan graphs, Combinatorica 8 (1988) 261–277. M. Morgenstern, Existence and explicit constructions of $q+1$ regular Ramanujan graphs for every prime power $q$, J. Combin. Theory Ser. B 62 (1994) 44–62. J. Friedman, A proof of Alon's second eigenvalue conjecture and related problems, Mem. Amer. Math. Soc. 195 (2008). A. Nilli, On the second eigenvalue of a graph, Discrete Math. 91 (1991) 207–210 (Alon–Boppana).

*Prepared 2026-09-16.*
