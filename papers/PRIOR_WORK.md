# Prior work behind each paper

For every paper in `public/`, its abstract and the works its text cites most often. The citation counts are a rough measure of whose results each paper rests on; the introduction and bibliography of each paper give the full account. This page is generated from the papers' own source files by `prior_work.py` in `framework/scripts`.

110 papers, 105 with an abstract found, 105 with cited works matched to the bibliography.

### Heat across an edge of an arc-transitive graph

Folder: [arc-transitive-edge-heat](public/arc-transitive-edge-heat) (source `public/arc-transitive-edge-heat/paper/main.tex`)

What the paper claims: Aldous and Fill ask whether random walk on an arc-transitive graph has some monotonicity property stronger than the inequality $P_i(X_{2t}=j)\le P_i(X_{2t}=i)$ that holds for every symmetric chain (Open Problem 7.30 of their monograph). We show that on every finite connected $1$-walk-regular graph, and so on every finite connected arc-transitive graph and every distance-regular graph, the ratio $H_t(x,y)/H_t(x,x)$ of the continuous-time heat kernel is strictly increasing in $t$ for every edge $xy$. Its derivative is the variance of the Laplacian eigenvalue under the exponentially tilted spectral measure of $x$, and its distance from $1$ is pinned between the spectral gap and the largest eigenvalue times $1-1/(nH_t(x,x))$. The same holds for the lazy walk in discrete time. The hypothesis cannot be weakened to regularity: on the $4$-regular graph of Regev and Shinkar the ratio across an edge exceeds $1$ and then decreases, although on every regular graph its average over the neighbours of $x$ is increasing.

Most cited in the text:

- D. Aldous and J. A. Fill, Reversible Markov Chains and Random Walks on Graphs, unfinished monograph, 2002, recompiled 2014, https://www.stat.berkeley.edu/ aldous/RWG/book.html. (cited 4 times)
- O. Regev and I. Shinkar, A counterexample to monotonicity of relative mass in random walks, Electron. Commun. Probab. 21 (2016), paper no. 11; arXiv:1506.08631. (cited 3 times)
- S. Liu and H. Zhang, Monotonic normalized heat diffusion for distance-regular graphs with classical parameters of diameter $3$, arXiv:2505.04314. (cited 2 times)
- A. E. Brouwer, A. M. Cohen and A. Neumaier, Distance-Regular Graphs, Springer, Berlin, 1989. (cited 1 time)


### Arc-transitive graphs that mimic the cycle

Folder: [arc-transitive-graphs-that-mimic-the-cycle](public/arc-transitive-graphs-that-mimic-the-cycle) (source `public/arc-transitive-graphs-that-mimic-the-cycle/paper/arc_transitive_cycle.tex`)

What the paper claims: Aldous and Fill ask (Open Problem 7.27 of Reversible Markov Chains and Random Walks on Graphs) whether, over arc-transitive graphs other than the cycles, the maximal mean commute time of simple random walk is $O(n\log n)$, the relaxation time is $O(n)$, and the ratio of the maximal mean commute time to twice the average hitting time tends to one. The answer to all three questions is no. Replacing every vertex of the $m$-cycle by $r\ge2$ pairwise non-adjacent copies gives a connected arc-transitive graph of degree $2r$ on $n=rm$ vertices whose mean hitting times are $j(m-j)+(r-1)m$ at cycle-distance $j\ge1$ and $rm$ between copies of the same vertex; its maximal mean commute time and its relaxation time are of order $n^2$, and the ratio tends to $3/2$. More generally, for any connected regular graph $H$ on $N$ vertices and $r\ge2$ the blow-up $H[\Kbar_r]$ has mean hitting times $\E_uT_v+(r-1)N$, average hitting time $\tau_0(H)+(r-1)N$ and relaxation time $\max(\tau_2(H),1)$, and every arc-transitive graph is such a blow-up of a twin-free arc-transitive graph. For bounded $r$ the three properties therefore pass between a graph and its twin-free quotient, so the question of Aldous and Fill, with the blow-ups of cycles excluded, is equivalent to its restriction to twin-free arc-transitive graphs, where it remains open. The arithmetic identities behind the formulas are checked in Lean 4.

Most cited in the text:

- D. Aldous and J. A. Fill, Reversible Markov Chains and Random Walks on Graphs, unfinished monograph, 2002 (recompiled 2014; the numbering is that of the online edition), https://www.stat.berkeley.edu/ aldous/RWG/book.html. (cited 12 times)
- R. Hammack, W. Imrich and S. Klavzar, Handbook of Product Graphs, 2nd ed., CRC Press, 2011. (cited 2 times)
- P. Potocnik and S. Wilson, Recipes for edge-transitive tetravalent graphs, Art Discrete Appl. Math. 3 (2020), P1.08. (cited 2 times)
- G. Sabidussi, Vertex-transitive graphs, Monatsh. Math. 68 (1964), 426--438. (cited 2 times)


### A tree automaton with infinitely many rogue fixed points under every supercritical offspring law

Folder: [automaton-fixed-simplex](public/automaton-fixed-simplex) (source `public/automaton-fixed-simplex/paper.tex`)

What the paper claims: Johnson, Podder and Skerman asked whether a tree automaton with finitely many, but at least three, states can have infinitely many fixed points of its automaton distributional map. Under binary branching an example with three states is implicit in earlier work of Rozikov and Zada on quadratic stochastic operators. We show that the phenomenon holds for every supercritical offspring law, Poisson laws included. For every $k\ge2$ there is an automaton on $k+1$ states whose fixed points, for an offspring law with generating function $G$ and mean greater than one, are one point mass together with the $(k-1)$-dimensional simplex of laws that give the distinguished state mass $s_*$, where $G'(s_*)=1$. Every point of the simplex is rogue, with no moment assumption on the offspring law; for the points other than the $k$ vertices this has a short self-contained proof.

Most cited in the text:

- Johnson, Tobias and Podder, Moumanti and Skerman, Fiona, Random tree recursions: which fixed points correspond to tangible sets of trees? (2020) (cited 28 times)
- Aldous, David J. and Bandyopadhyay, Antar, A survey of max-type recursive distributional equations (2005) (cited 1 time)
- Ganikhodzhaev, Rasul and Mukhamedov, Farrukh and Rozikov, Utkir, Quadratic stochastic operators and processes: results and open problems (2011) (cited 1 time)
- Holroyd, Alexander E. and Martin, James B., Galton--Watson games (2021) (cited 1 time)


### The drawn length of the critical beta-splitting tree grows linearly

Folder: [beta-splitting-drawn-length](public/beta-splitting-drawn-length) (source `public/beta-splitting-drawn-length/paper/main.tex`)

What the paper claims: In the critical beta-splitting model of a random binary tree with $n$ leaves, a clade of $m$ leaves splits into clades of $i$ and $m-i$ leaves with probability proportional to $1/(i(m-i))$. Aldous and Janson asked for a proof that the expected drawn length $L_n$ of the cladogram of this tree grows roughly like $n\log^4 n$. We show that $L_n/n$ converges to the finite constant $\lambda=\sum_{m\ge2}a(m)c_m/m$, where $a(m)=6h_{m-1}/(\pi^2(m-1))$ is the limiting probability that a uniformly chosen leaf lies in a clade of exactly $m$ leaves and $c_m$ is the expected contribution of the root of a tree with $m$ leaves to the drawn length. Numerically $\lambda\approx4.88$, and $4.80<\lambda<5.38$. The proof combines an exponential moment bound for the height with a bound, uniform in $n$, on the time the harmonic descent chain spends in a dyadic block. A deterministic comparison with the sum of the leaf depths gives the weaker bound $L_n=O(n\log^2n)$ directly. The prediction $n\log^4n$ comes from a heuristic in which the expected number of clades of size $m$ is taken to be $na(n,m)$ instead of $(n/m)a(n,m)$.

Most cited in the text:

- D. J. Aldous and S. Janson, The critical beta-splitting random tree II: overview and open problems, arXiv:2303.02529v3, 2025. (cited 16 times)
- D. J. Aldous, S. Janson and X. Li, The harmonic descent chain, Electron. Commun. Probab. 29 (2024), 1--10. (cited 2 times)
- D. J. Aldous and B. Pittel, The critical beta-splitting random tree: heights and related results, Ann. Appl. Probab. 35 (2025), 158--195. (cited 2 times)
- A. Brandenberger, B. Chin and E. Mossel, Asymptotics for the harmonic descent chain and applications to critical beta-splitting trees, arXiv:2505.24821v3. (cited 2 times)


### Correlation of leaf heights at mesoscopic separation in the critical beta-splitting tree

Folder: [beta-splitting-leaf-correlation](public/beta-splitting-leaf-correlation) (source `public/beta-splitting-leaf-correlation/paper/main.tex`)

What the paper claims: In the critical beta-splitting random tree on $n$ leaves, in its interval-splitting form with the interval closed into a cycle, let $D^{(1)}_n$ and $D^{(2)}_n$ be the continuous heights of a uniformly random leaf and of the leaf $r$ places further round the cycle. We show that, uniformly in $1\le r\le n/2$, $\Cov\bigl(D^{(1)}_n,D^{(2)}_n\bigr)=\sigma^2\log(n/r)+O\bigl(\sqrt{\log n}\bigr),\qquad \Var(D_n)=\sigma^2\log n+O\bigl(\sqrt{\log n}\bigr),$ with $\sigma^2=2\zeta(3)/\zeta(2)^3$. Hence the correlation coefficient equals $1-\log r/\log n+O((\log n)^{-1/2})$, and it tends to $1-\alpha$ whenever $\log r_n/\log n\to\alpha\in[0,1]$. This answers Open Problem 1 of Aldous and Janson. The proof follows a positional potential of each leaf, which decreases at rate $\zeta(2)$ up to errors that are square integrable along the whole path, and compares the two martingales it produces through their bracket up to the separation of the two leaves.

Most cited in the text:

- D. J. Aldous and S. Janson, The critical beta-splitting random tree II: overview and open problems, arXiv:2303.02529v3 (2025). (cited 4 times)
- D. J. Aldous and B. Pittel, The critical beta-splitting random tree I: heights and related results, Ann. Appl. Probab. 35 (2025), 158--195. Theorem 1.1 is cited in the numbering of arXiv:2302.05066v4. (cited 3 times)
- D. J. Aldous and S. Janson, The critical beta-splitting random tree IV: Mellin analysis of leaf height, Electron. J. Probab. 30 (2025), Paper No. 69, 39 pp. (cited 2 times)
- D. Aldous, Probability distributions on cladograms, in Random Discrete Structures, IMA Vol. Math. Appl., Springer, New York, 1996, 1--18. (cited 1 time)


### The connectivity window of bilateral preference random graphs

Folder: [bilateral-preference-connectivity-window](public/bilateral-preference-connectivity-window) (source `public/bilateral-preference-connectivity-window/paper/main.tex`)

What the paper claims: In the bilateral preference random graph $LK(n,k)$ of La and Kabkab, independent uniform scores are placed on the edges of $K_n$, each vertex prefers its $k$ incident edges of smallest score, and an edge is kept when both of its endpoints prefer it. Dabirian and Subramanian showed that $LK(n,k)$ is connected with high probability when $k\ge\log n+t\log\log n\sqrt{\log n}$ with $t>1/2$ and disconnected when $t<-1/2$, and left the window between these two conditions open. We show that for every fixed $C$, uniformly over integers $k$ with $|k-\log n|\le C$, the number of isolated vertices is asymptotically Poisson with mean $ne^{-k}$ in total variation and the probability that $LK(n,k)$ is connected is $\exp(-ne^{-k})+o(1)$. Consequently $LK(n,k)$ is connected with high probability if and only if $k-\log n\to\infty$, and disconnected with high probability if and only if $k-\log n\to-\infty$. The main estimate is that a fixed set of $r$ vertices is isolated with probability $e^{-rk}(1+o(1))$; it comes from an exact integral formula for the rejections at one vertex and a direct count of the few edges through which the vertices of the set can interact.

Most cited in the text:

- H. Dabirian and V. Subramanian, Connectivity of a family of bilateral preference random graphs, J. Appl. Probab. 63 (2026), 552--579. Also arXiv:2209.05677. (cited 3 times)
- P. Balister, B. Bollobas, A. Sarkar and M. Walters, Connectivity of random $k$-nearest-neighbour graphs, Adv. in Appl. Probab. 37 (2005), 1--24. (cited 1 time)
- P. Billingsley, Probability and Measure, 3rd ed., Wiley, New York, 1995. (cited 1 time)
- C. Cooper and A. Frieze, On the connectivity of random $k$-th nearest neighbour graphs, Combin. Probab. Comput. 4 (1995), 343--362. (cited 1 time)


### Degree fluctuations in bilateral preference random graphs

Folder: [bilateral-preference-degree-limits](public/bilateral-preference-degree-limits) (source `public/bilateral-preference-degree-limits/paper/main.tex`)

What the paper claims: In the bilateral preference random graph $LK(n,k)$ of La and Kabkab, independent uniform scores are placed on the edges of $K_n$, each vertex prefers its $k$ incident edges of smallest score, and an edge is kept when both of its endpoints prefer it. Dabirian and Subramanian asked for the limiting distribution of the standardized degree $(D-\E D)/\sqrt{\Var D}$ of a vertex. We show that if $k\to\infty$ and $n-k\to\infty$, then $(k-D)/s_n$, where $s_n^2=k(n-k)/n$, converges in distribution and in its first two moments to $\phi(Z)+Z\Phi(Z)$ with $Z$ standard normal. Consequently $\E D=k-s_n/\sqrt\pi+o(s_n)$, $\Var D=(1/3+(\sqrt3-2)/(2\pi))s_n^2+o(s_n^2)$, and the standardized degree converges to an explicit law that is bounded above, hence not normal. If instead $r=n-1-k\ge1$ is fixed, then $k-D$ converges in distribution and in all moments to a mixed Poisson variable whose mean is an explicit function of a gamma variable with shape $r$. These limits depend on $r$ and, after standardization, converge to the interior law as $r\to\infty$. Together with the Erlang weighted tree of Moharrami, Subramanian, Liu and Sundaresan for fixed $k$, this identifies every subsequential limit of the standardized degree; no single law serves for all sequences $k(n)$. We also show that $\E(k-D)$ takes the same value at the budgets $k$ and $n-1-k$ for every $n$.

Most cited in the text:

- H. Dabirian and V. Subramanian, Connectivity of a family of bilateral preference random graphs, J. Appl. Probab. 63 (2026), 552--579. Theorems 7 and 8 there are Theorems 6.1 and 6.2 of arXiv:2209.05677v3. (cited 10 times)
- M. Moharrami, V. Subramanian, M. Liu and R. Sundaresan, The Erlang weighted tree, a new branching process, Random Structures Algorithms 64 (2024), 537--624. Theorem numbers as in arXiv:2002.03993v5. (cited 7 times)
- P. Billingsley, Probability and Measure, 3rd ed., Wiley, New York, 1995. (cited 2 times)
- C. Cooper and A. Frieze, On the connectivity of random $k$-th nearest neighbour graphs, Combin. Probab. Comput. 4 (1995), 343--362. (cited 1 time)


### The giant component of bilateral preference graphs with random budgets

Folder: [bilateral-preference-giant-component](public/bilateral-preference-giant-component) (source `public/bilateral-preference-giant-component/paper/main.tex`)

What the paper claims: Place independent and identically distributed continuous costs on the edges of $K_n$, give each vertex $i$ an independent budget $D_i$ with law $P$ on the positive integers, let $i$ prefer its $D_i$ cheapest incident edges, and keep an edge when both endpoints prefer it. Moharrami, Subramanian, Liu and Sundaresan showed that the local limit of this graph is the Erlang weighted tree, so that the fraction of vertices in the largest component is asymptotically at most the survival probability $\rho(P)$ of that tree, and asked whether the reverse inequality holds. We prove that it does whenever $P$ has a finite mean: the largest component contains $(\rho(P)+o(1))n$ vertices with probability tending to one. The same holds for deterministic budget arrays whose empirical laws converge weakly to $P$. The proof runs the graph in cost time, shows that every large component of the graph built from edges of cost at most $t$ contains many vertices that can still accept edges, and joins these components by the edges arriving shortly after $t$. It remains to show that the survival probability of the tree with its edges above cost $t$ removed tends to $\rho(P)$. This is done through a return process to a compact set of types, whose mean operator is self-adjoint in a weighted space.

Most cited in the text:

- M. Moharrami, V. Subramanian, M. Liu and R. Sundaresan, The Erlang weighted tree, a new branching process, Random Structures Algorithms 64 (2024), 537--624. Also arXiv:2002.03993. (cited 7 times)
- D. Aldous and J. M. Steele, The objective method: probabilistic combinatorial optimization and local weak convergence, in Probability on Discrete Structures, Encyclopaedia Math. Sci., Springer, Berlin, 2004, 1--72. (cited 1 time)
- S. Boucheron, G. Lugosi and P. Massart, Concentration Inequalities: A Nonasymptotic Theory of Independence, Oxford University Press, Oxford, 2013. (cited 1 time)
- H. Dabirian and V. Subramanian, Connectivity of a family of bilateral preference random graphs, J. Appl. Probab. 63 (2026), 552--579. Also arXiv:2209.05677. (cited 1 time)


### A homogeneous space with no nonconstant quasiharmonic functions

Folder: [bjorklund-star-quotient](public/bjorklund-star-quotient) (source `public/bjorklund-star-quotient/paper/main.tex`)

What the paper claims: Bjorklund asked for a countable measured group $(G,\mu)$ and a subgroup $H$ of infinite index such that the homogeneous space $G/H$ carries no nonconstant left $\mu$-harmonic or $\mu$-quasiharmonic functions, bounded or not. We give such an example. The group is the group of finitely supported permutations of $\N_0=\{0,1,2,\dots\}$, the subgroup is the stabiliser of $0$, and $\mu$ is any probability measure that charges every transposition $(0\ n)$, $n\ge1$, and nothing else. The induced walk on $G/H\cong\N_0$ is a star with infinitely many leaves. The equation at a leaf $k$ forces a quasiharmonic function with defect $c$ to satisfy $u(k)=u(0)-c/\mu((0\ k))$, and the equation at the centre then forces $c=0$ and $u$ constant. The argument uses only the convergence of the single series that defines the equation at the centre.

Most cited in the text:

- M. Bjorklund, Five remarks about random walks on groups, preprint, 2014, arXiv:1406.0763v2. (cited 3 times)
- M. Bjorklund and T. Hartnick, Biharmonic functions on groups and limit theorems for quasimorphisms along random walks, Geom. Topol. 15 (2011), 123--143. (cited 1 time)
- J. Frisch, Y. Hartman, O. Tamuz and P. Vahidi Ferdowsi, Choquet--Deny groups and the infinite conjugacy class property, Ann. of Math. (2) 190 (2019), 307--320; arXiv:1802.00751. (cited 1 time)
- V. A. Kaimanovich and A. M. Vershik, Random walks on discrete groups: boundary and entropy, Ann. Probab. 11 (1983), 457--490. (cited 1 time)


### The mode of classical and free Brownian motion with an initial distribution at large time

Folder: [brownian-mode-location](public/brownian-mode-location) (source `public/brownian-mode-location/paper/main.tex`)

What the paper claims: Let $\mu$ be a probability measure on the real line with mean $m$ and finite variance $v$. We show that the density of $\mu*N(0,t)$ has a unique global maximizer for $t\ge 600v$ and that the density of the free convolution $\mu\boxplus S(0,t)$ with the semicircle law of variance $t$ has a unique global maximizer for $t>7(7+4\sqrt2)v$. Both maximizers converge to $m$ as $t\to\infty$, with explicit bounds of order $t^{-1/2}$, and of order $t^{-1}$ when the third absolute moment is finite. If the seventh moment is finite, the maximizers are $m-\frac{\mu_3}{2t}+\frac{\mu_5-6v\mu_3}{8t^2}+O(t^{-3})\qquad\text{and}\qquad m-\frac{3\mu_3}{t}+\frac{5\mu_5-22v\mu_3}{t^2}+O(t^{-3})$ respectively, where $\mu_k$ is the $k$th central moment of $\mu$. This gives an answer to a problem of Hasebe and Ueda on the position of the mode of classical and free Brownian motion with an initial distribution.

Most cited in the text:

- T. Hasebe and Y. Ueda, Large time unimodality for classical and free Brownian motions with initial distributions, ALEA Lat. Am. J. Probab. Math. Stat. 15 (2018), 353--374. https://doi.org/10.30757/ALEA.v15-15doi:10.30757/ALEA.v15-15; arXiv: (cited 16 times)
- P. Biane, On the free convolution with a semi-circular distribution, Indiana Univ. Math. J. 46 (1997), no. 3, 705--718. https://doi.org/10.1512/iumj.1997.46.1467doi:10.1512/iumj.1997.46.1467. (cited 2 times)
- A. Nica and R. Speicher, Lectures on the Combinatorics of Free Probability, London Mathematical Society Lecture Note Series 335, Cambridge University Press, Cambridge, 2006. https://doi.org/10.1017/CBO9780511735127doi:10.1017/CBO97805117351 (cited 2 times)
- H. Bercovici and D. Voiculescu, Free convolution of measures with unbounded support, Indiana Univ. Math. J. 42 (1993), no. 3, 733--773. https://doi.org/10.1512/iumj.1993.42.42033doi:10.1512/iumj.1993.42.42033. (cited 1 time)


### A Brownian piece in front of a process absolutely continuous with respect to Brownian motion

Folder: [brownian-prefix-filling](public/brownian-prefix-filling) (source `public/brownian-prefix-filling/paper/main.tex`)

What the paper claims: Burdzy and Scheutzow asked whether, for every process $(X_t)_{t\ge0}$ whose law is equivalent to Wiener measure, one can put a random piece of path in front of $X$ so that the new process is a Brownian motion. We show that the answer is yes, and that absolute continuity suffices: on an extension of the probability space there are a Brownian motion $B$ and an almost surely finite random integer $N\ge0$ with $X_t=B_{N+t}-B_N$ for all $t\ge0$, so that $(B_t)_{0\le t\le N}$ is the required piece. The proof is Rost's filling scheme for the unit shift of two-sided Brownian motion. We give it in the form of a criterion for an invertible measure-preserving map $\theta$ and a target law $fP$: a randomized forward shift $\theta^N$ carries $P$ to $fP$ if and only if $\E[f\mid\I]=1$, where $\I$ is the invariant $\sigma$-field. The time $N$ cannot in general be a stopping time for $B$, and the auxiliary randomness cannot be dropped from the criterion.

Most cited in the text:

- K. Burdzy and M. Scheutzow, Forward Brownian motion, Probab. Theory Related Fields 160 (2014), 95--126. (cited 5 times)
- J. Pitman and W. Tang, Patterns in random walks and Brownian motion, in Seminaire de Probabilites XLVII, Lecture Notes in Math. 2137, Springer, Cham, 2015, 49--88. (cited 3 times)
- R. V. Chacon and D. S. Ornstein, A general ergodic theorem, Illinois J. Math. 4 (1960), 153--160. (cited 2 times)
- C. Dellacherie and P.-A. Meyer, Probabilities and Potential C, North-Holland Mathematics Studies 151, North-Holland, Amsterdam, 1988. (cited 2 times)


### Double times on slices of the Brownian sheet in dimensions four and five

Folder: [brownian-sheet-slice-double-times](public/brownian-sheet-slice-double-times) (source `public/brownian-sheet-slice-double-times/paper/main.tex`)

What the paper claims: Let $B$ be a $d$-dimensional Brownian sheet. For $s>0$ the slice $t\mapsto B(s,t)$ is a multiple of $d$-dimensional Brownian motion, so for $d\ge4$ a fixed slice has no double points, while for $d\in\{4,5\}$ there are random exceptional slices that have them. Khoshnevisan asked whether, outside a single null set, the set of double times of every slice has Hausdorff dimension zero when $d\in\{4,5\}$. We prove that it does: almost surely, for every $s>0$ the set of pairs $u\ne v$ with $B(s,u)=B(s,v)$ has Hausdorff dimension zero, and its part in a product of two disjoint compact intervals has upper box dimension zero. For $d=5$ both statements also follow from the finiteness of these sets stated by Chen; the new case is $d=4$. The proof bounds high moments of the number of near-coincidences on a grid, using a conditional variance estimate obtained from Brownian bridges, and then takes a union over a grid of slices whose cost is absorbed by the choice of the moment.

Most cited in the text:

- D. Khoshnevisan, Slices of a Brownian sheet: new results and open problems, in Seminar on Stochastic Analysis, Random Fields and Applications V, Progr. Probab. 59, Birkhauser, Basel, 2008, 135--174. 10.1007/978-3-7643-8458-6_9. Equation and (cited 8 times)
- K. Chen, Uniform dimension results of level-sets of stable sheets, doctoral thesis no. 11211, EPFL, Lausanne, 2026. 10.5075/epfl-thesis-11211 (cited 4 times)
- D. Khoshnevisan, D. Wu and Y. Xiao, Sectorial local non-determinism and the geometry of the Brownian sheet, Electron. J. Probab. 11 (2006), paper no. 32, 817--843. 10.1214/EJP.v11-353 (cited 4 times)
- T. J. Lyons, The critical dimension at which quasi-every Brownian path is self-avoiding, Adv. in Appl. Probab. 18 (1986), suppl. Analytic and Geometric Stochastics, 87--99. (cited 2 times)


### The binary and ternary harmonic measures of the Cantor set are mutually singular

Folder: [cantor-harmonic-codings-singular](public/cantor-harmonic-codings-singular) (source `public/cantor-harmonic-codings-singular/paper/main.tex`)

What the paper claims: Let $E$ be the middle-thirds Cantor set and, for an integer $b\ge 2$, let $\nu_b$ be the measure on $E$ obtained by pushing forward the harmonic measure of simple random walk on the tree of $b$-adic intervals that meet $E$. The measure $\nu_3$ is the Cantor measure. Lyons and Peres asked whether $\nu_2$ and $\nu_3$ are mutually singular. We show that they are. The proof compares the conditional splits of the two measures on dyadic cells through Hellinger affinities. At one explicit dyadic cell, whose intersection with $E$ is a single ternary cylinder, the Cantor measure splits evenly while the harmonic measure, computed as an electrical current, does not; an exact computation with rational arithmetic bounds the harmonic split away from $1/2$, and the discrepancy persists for all nearby positions and scales of the cylinder. A Fourier argument resting on Stewart's theorem on digit changes in the bases $2$ and $3$ then shows that, if the two measures were not singular, such cells would carry a fixed share of their overlap at infinitely many levels, which is incompatible with the summability of the Hellinger losses.

Most cited in the text:

- R. Lyons and Y. Peres, Probability on Trees and Networks, Cambridge Series in Statistical and Probabilistic Mathematics 42, Cambridge University Press, New York, 2016. Page numbers refer to the version of 19 August 2026 at https://rdlyons.p (cited 10 times)
- D. Allen, S. Chow and H. Yu, Dyadic approximation in the middle-third Cantor set, Selecta Math. (N.S.) 29 (2023), Paper No. 11; arXiv:2005.09300. (cited 2 times)
- C. L. Stewart, On the representation of an integer in two different bases, J. Reine Angew. Math. 319 (1980), 63--72. (cited 2 times)
- Y. Bugeaud, M. Cipu and M. Mignotte, On the representation of Fibonacci and Lucas numbers in an integer base, Ann. Math. Que. 37 (2013), 31--43. (cited 1 time)


### An improved lower bound for the card-cyclic-to-random shuffle

Folder: [card-cyclic-lower-bound](public/card-cyclic-lower-bound) (source `public/card-cyclic-lower-bound/main.tex`)

What the paper claims: In the card-cyclic-to-random shuffle of $n$ cards, the cards labelled $1,\dots,n$ are removed in turn, cyclically, and each is reinserted at a uniformly random position. Morris, Ning and Peres proved that the mixing time is of order $n\log n$, with a lower bound of $c\,n\log n$ for every $c<1/(2+2a)$, where $-a+ib$ is a root of $e^{-z}=1-z$ and $a$ is about $2.089$. We raise the lower constant from about $0.162$ to $1/(2a)$, about $0.239$. On functions of the relative order of pairs of cards the chain acts as the exterior square of an explicit $n\times n$ matrix. Two eigenvectors of that matrix give an exact eigenfunction of the chain, with eigenvalue of modulus $1-a/n+O(n^{-2})$, and a second-moment argument finishes the proof. Whether the shuffle has cutoff remains open.

Most cited in the text:

- B. Morris, W. Ning and Y. Peres, Mixing time of the card-cyclic-to-random shuffle, Ann. Appl. Probab. 24 (2014), 1835--1849, doi:10.1214/13-AAP964; arXiv:1207.3406. (cited 8 times)
- M. Bernstein and E. Nestoridi, Cutoff for random to random card shuffle, Ann. Probab. 47 (2019), 3303--3320, doi:10.1214/19-AOP1340; arXiv:1703.06210. (cited 2 times)
- J. Jonasson, Card-cyclic-to-random shuffling with relabeling, ALEA Lat. Am. J. Probab. Math. Stat. 12 (2015), 793--810, arXiv:1501.05485. (cited 2 times)
- D. A. Levin and Y. Peres, Markov Chains and Mixing Times, second edition, American Mathematical Society, Providence, RI, 2017. (cited 2 times)


### Law-determined norm inequalities do not imply complete mixability

Folder: [complete-mixability-norm-converse](public/complete-mixability-norm-converse) (source `public/complete-mixability-norm-converse/paper/main.tex`)

What the paper claims: A law $F$ with mean $\mu$ is $n$-completely mixable if there are $n$ random variables with law $F$ whose sum is almost surely $n\mu$. Wang proved that such a law satisfies a family of inequalities between the norms of the positive and negative parts of $X-t$ and $X-s$, where $X\sim F$ and $s=(n\mu-t)/(n-1)$, for every threshold $t$ and every law-determined norm, and asked when these inequalities are also sufficient (Open Problem 4 in his 2015 survey). We show that for bounded $F$ the whole family is equivalent to the single convex-order condition $X-\mu\cx-(n-1)(X-\mu)$, and that the same holds for integrable $F$ if the norms are required to have the Fatou property. The inequalities do not imply $n$-complete mixability: for $n=3$ the analytic density $\frac1{10}+\frac{27}{10}(2x-1)^2$ on $[0,1]$ satisfies all of them and is not $3$-completely mixable, and for $n=3$ and $n=4$ there are counterexamples with densities bounded away from zero on $[0,1]$ and with $C^\infty$ densities, the one for $n=4$ not symmetric. A Bernoulli$(p)$ law satisfies the inequalities exactly when $1/n\le p\le1-1/n$, while it is $n$-completely mixable exactly when $np$ is an integer. For $n=2$ the inequalities are equivalent to symmetry, hence to $2$-complete mixability, for every integrable law. For $n=3$ the examples refine the symmetric non-mixable laws of Yin and Zhu, and the reduction explains why those laws satisfy the inequalities.

Most cited in the text:

- B. Wang and R. Wang, The complete mixability and convex minimization problems with monotone marginal densities, J. Multivariate Anal. 102 (2011), 1344--1360. https://doi.org/10.1016/j.jmva.2011.05.002 (cited 7 times)
- M. Shaked and J. G. Shanthikumar, Stochastic Orders, Springer Series in Statistics, Springer, New York, 2007. https://doi.org/10.1007/978-0-387-34675-5 (cited 6 times)
- R. Wang, Current open questions in complete mixability, Probab. Surv. 12 (2015), 13--32. https://doi.org/10.1214/14-PS250 (cited 6 times)
- G. Puccetti, B. Wang and R. Wang, Advances in complete mixability, J. Appl. Probab. 49 (2012), 430--440. https://doi.org/10.1239/jap/1339878796 (cited 5 times)


### Two giant boxes in random allocations

Folder: [condensation-two-giant-boxes](public/condensation-two-giant-boxes) (source `public/condensation-two-giant-boxes/paper/main.tex`)

What the paper claims: Let $(Y_1,\dots,Y_n)$ be the random allocation of $m$ balls into $n$ boxes in which an allocation $(y_1,\dots,y_n)$ has probability proportional to $\prod_iw_{y_i}$, for a weight sequence $(w_k)_{k\ge0}$. When $m/n\to\lambda>\nu$, where $\nu$ is determined by the weights, a positive fraction of the balls condenses into boxes whose sizes tend to infinity. For weights $w_k\sim ck^{-\beta}$ with $\beta>2$ the largest box then contains $(\lambda-\nu)n+o_p(n)$ balls and the second largest $o_p(n)$. Janson asked whether the same holds for every nonincreasing weight sequence, and for every weight sequence with $w_{k+1}/w_k\to\infty$. We show that neither condition suffices. We construct nonincreasing weights for which, for every $\lambda>\nu$ and along a sequence of pairs $(m,n)$ with $m/n\to\lambda$, each of the two largest boxes contains at least $(\lambda-\nu)n/13$ balls with probability tending to one, and weights with $w_{k+1}/w_k\ge e^k$ for which the second largest box contains more than $m/8$ balls with probability at least $1-\exp(-m^3/256)$ whenever $m\ge64$ is a power of two, $n\ge2$ and $\log(m+n)\le m^2/256$. Both constructions give simply generated random trees in which, for infinitely many $n$, two nodes have outdegree of order $n$ with probability tending to one.

Most cited in the text:

- S. Janson, Simply generated trees, conditioned Galton--Watson trees, random allocations and condensation, Probab. Surv. 9 (2012), 103--252. (cited 13 times)
- Y. Schwarzkopf, M. R. Evans and D. Mukamel, Zero-range processes with multiple condensates: statics and dynamics, J. Phys. A 41 (2008), 205001. (cited 2 times)
- G. Bennett, Probability inequalities for the sum of independent random variables, J. Amer. Statist. Assoc. 57 (1962), 33--45. (cited 1 time)
- S. Janson, T. Jonsson and S. O. Stefansson, Random trees with superexponential branching weights, J. Phys. A 44 (2011), 485002. (cited 1 time)


### One bit is optimal for cosmic coin flipping on at most nine bits

Folder: [cosmic-coin-flipping-nine-bits](public/cosmic-coin-flipping-nine-bits) (source `public/cosmic-coin-flipping-nine-bits/paper/main.tex`)

What the paper claims: In the cosmic coin flipping problem of Mossel and O'Donnell, $k$ parties receive independent $\epsilon$-noisy copies of $n$ uniform bits and each outputs a uniform bit, aiming to maximize the probability that all outputs agree. Mossel and O'Donnell asked whether, for $2\le k\le 9$, the best antisymmetric protocol is for every party to output its first bit. The cases $k\le5$ follow from work of Witsenhausen, Mossel and O'Donnell, and Yu. We prove that the answer is positive for $6\le k\le 9$ whenever $n\le 9$. By symmetrization it suffices to compare the first-bit function with the $319{,}124$ antisymmetric left-monotone functions on nine bits. After the substitution $t=2\epsilon/(1-2\epsilon)$ we show that, for every other function, the coefficients of degrees $1$ to $nk-2$ of the numerator of the difference of agreement probabilities are positive, using floating-point arithmetic with a rigorous error bound. For $n\le8$ an exact computation confirms the inequalities.

Most cited in the text:

- E. Mossel and R. O'Donnell, Coin flipping from a cosmic source: on error correction of truly random bits, Random Structures Algorithms 26 (2005), 418--436, 10.1002/rsa.20062, /0406504. (cited 12 times)
- N. J. Higham, Accuracy and Stability of Numerical Algorithms, 2nd ed., SIAM, Philadelphia, 2002, 10.1137/1.9780898718027. (cited 3 times)
- L. Yu, On the $$-stability and related conjectures, Probab. Theory Related Fields 186 (2023), 1045--1080, 10.1007/s00440-023-01209-5, 2104.08740. (cited 3 times)
- OEIS Foundation, The On-Line Encyclopedia of Integer Sequences, sequence A109456, number of Boolean functions of $n$ variables that are self-dual and regular, contributed by D. E. Knuth, accessed November 2026, https://oeis.org/A109456. (cited 2 times)


### Cover-time fluctuations beyond the maximal hitting-time scale

Folder: [cover-time-fluctuations](public/cover-time-fluctuations) (source `public/cover-time-fluctuations/paper/main.tex`)

What the paper claims: Ding, Lee and Peres asked whether the standard deviation of a graph cover time is universally bounded by the maximal hitting time, and whether the centered cover time has an exponential tail on that scale. We give negative answers even under $\tcov/\thit\to\infty$. An explicit unweighted clique--star graph satisfies $\Var_x(\taucov)\sim\thit\tcov$ and $(\taucov-\tcov)/\sqrt{\thit\tcov}\Longrightarrow\Nor(0,1)$ from every starting vertex. We obtain exact hitting times and coupon-clock transforms, two-term mean and variance expansions, a Berry--Esseen bound of order $(\log k)^{-1/2}$, and Gaussian moderate deviations. We also show that the failure is already present on trees of diameter three. More generally, attaching $k$ leaves to each vertex of a fixed connected graph yields a cover-time fluctuation limit equal to the centered maximum of a Gaussian vector with covariance twice the pseudoinverse of the core Laplacian. For the two-vertex core this is an explicit centered half-normal law. The examples show that the geometric-mean fluctuation scale cannot be replaced by any smaller interpolation power of the cover time, even though the cover time itself concentrates around its mean.

Most cited in the text:

- N. Berestycki, J. Hermon and L. Teyssier, On the universality of fluctuations for the cover time, preprint, arXiv:2202.02255. https://arxiv.org/abs/2202.02255. (cited 2 times)
- J. Ding, J. R. Lee and Y. Peres, Cover times, blanket times, and majorizing measures, Ann. of Math. (2) 175 (2012), 1409--1471. https://doi.org/10.4007/annals.2012.175.3.8doi:10.4007/annals.2012.175.3.8. (cited 2 times)
- A. Dembo and O. Zeitouni, Large Deviations Techniques and Applications, second edition, Applications of Mathematics 38, Springer, 1998; corrected printing 2010. https://doi.org/10.1007/978-3-642-03311-7doi:10.1007/978-3-642-03311-7. (cited 2 times)
- A. Zhai, Exponential concentration of cover times, Electron. J. Probab. 23 (2018), paper no. 32, 22 pp. https://doi.org/10.1214/18-EJP149doi:10.1214/18-EJP149. (cited 2 times)


### Maximal energy bounds fail for the stochastic Allen--Cahn equation with critical quadratic noise

Folder: [critical-allen-cahn-noise](public/critical-allen-cahn-noise) (source `public/critical-allen-cahn-noise/paper/main.tex`)

What the paper claims: We consider the stochastic Allen--Cahn equation $du=(\Delta u+u-u^3)\,dt+\sqrt2\,u^2\,dW$ on the one-dimensional torus, driven by a single real Brownian motion. For every positive constant initial value and every $T>0$ the solution satisfies $\E\sup_{t\le T}\|u(t)\|_{L^2}^2=\infty$, although $\E\|u(t)\|_{L^2}^2$ is finite at each fixed time. The equation satisfies the hypotheses of the global well-posedness theorem in the critical variational setting of Agresti and Veraar, and $\sqrt2$ is the largest noise constant for which it does. The example therefore answers Problems 4 and 5 of their 2025 survey in the negative: the maximal second moment is not controlled by the initial data, and the solutions started at $1/n$ converge to zero in $L^p(\Omega;L^2(0,T;H^1)\cap C([0,T];L^2))$ for every $p<2$, while their norms in $L^2(\Omega;C([0,T];L^2))$ are infinite. The solution started from a constant is $e^t/\sqrt2$ times the reciprocal of a time-changed four-dimensional Bessel process. Its squared running maximum has two-sided tail bounds of order $1/y$ with explicit constants, its maximal moments are finite exactly below order two, and its fixed-time moments are finite exactly below order four.

Most cited in the text:

- A. Agresti and M. Veraar, Nonlinear SPDEs and maximal regularity: an extended survey, NoDEA Nonlinear Differential Equations Appl. 32 (2025), Paper No. 123. https://doi.org/10.1007/s00030-025-01090-2doi:10.1007/s00030-025-01090-2; https://a (cited 23 times)
- D. Revuz and M. Yor, Continuous Martingales and Brownian Motion, third edition, Grundlehren der mathematischen Wissenschaften 293, Springer, Berlin, 1999. https://doi.org/10.1007/978-3-662-06400-9doi:10.1007/978-3-662-06400-9. (cited 3 times)
- A. Agresti and M. Veraar, The critical variational setting for stochastic evolution equations, Probab. Theory Related Fields 188 (2024), 957--1015. https://doi.org/10.1007/s00440-023-01249-xdoi:10.1007/s00440-023-01249-x. (cited 2 times)
- K. D. Elworthy, X.-M. Li and M. Yor, On the tails of the supremum and the quadratic variation of strictly local martingales, in: Seminaire de Probabilites XXXI, Lecture Notes in Math. 1655, Springer, Berlin, 1997, 113--125. https://doi.org/ (cited 2 times)


### crossing-cores-rmt

Folder: [crossing-cores-rmt](public/crossing-cores-rmt) (source `public/crossing-cores-rmt/paper/section_profiles_paper.tex`)

What the paper claims: The moment polytopes of the limiting spectral laws $\gamma_T$ and $\gamma_H$ of random symmetric Toeplitz and Hankel matrices are studied through their sections by the initial coordinate. The resulting section profile is multiplicative under concatenation of double-occurrence words, invariant under ear insertion at every position, and flattens to a constant under a nesting pair. These three rules give an exact calculus: volumes of concatenations are computed by integrating products of profiles, insertions into a gap are computed against an explicit gap marginal, and the volume of a fully crossing $r$-pair word is $2/(r+1)$ in closed form. Consequences include supermultiplicativity of pairing volumes and of the primitive core masses, an exact cluster equation exhibiting the crossing correction to the Catalan equation, and closed-form extremal families: the reduced Toeplitz cores of at least five pairs attain $4/9$ exactly on one dihedral orbit for each size, and their parity-mixing counterparts of at least seven pairs attain $1/4$. All the slab constants appearing in this circle of problems -- $2/3$, $1/2$, $2/5$, $1/3$ and the conjectural $2/7$ -- are shown to be the single family $2/(j+2)$, with the exceptional system of the fully crossing word attaining each value. Finally, exact moment data through order twenty-two gives a four-moment certificate that $\gamma_H$ is not unimodal, shows no obstruction to the unimodality of $\gamma_T$, and supports a conjectural description of $\gamma_T$ as a scale mixture of semicircle laws.

Most cited in the text:

- W. Bryc, A. Dembo and T. Jiang, Spectral measure of large random Hankel, Markov and Toeplitz matrices, Ann. Probab. 34 (2006), 1--38. (cited 4 times)
- C. Hammond and S. J. Miller, Distribution of eigenvalues for the ensemble of real symmetric Toeplitz matrices, J. Theoret. Probab. 18 (2005), 537--566. (cited 1 time)
- A. Sen and B. Virag, Absolute continuity of the limiting eigenvalue distribution of the random Toeplitz matrix, Electron. Commun. Probab. 16 (2011), 706--711. (cited 1 time)


### Non-endogenous fixed points of the discounted tree sum equation: the regular case

Folder: [discounted-tree-sums-endogeny](public/discounted-tree-sums-endogeny) (source `public/discounted-tree-sums-endogeny/paper/main.tex`)

What the paper claims: Aldous and Bandyopadhyay showed that every nonzero solution $Y$ of the homogeneous equation $Y\stackrel{d}{=}\max_i \xi_i Y_i$ produces, for each $a\ge 0$, an invariant measure $\mu_a$ of the discounted tree sum equation $X\stackrel{d}{=}\eta+\max_i \xi_i X_i$, and conjectured that for $a>0$ the invariant recursive tree process with marginal $\mu_a$ is never endogenous. We show that the conditional essential supremum of $Y$ given all the innovations is an endogenous solution of the homogeneous equation with values in $[0,\infty]$, and that $\mu_a$ fails to be endogenous as soon as this supremum is infinite with positive probability. It follows that the conjecture, for all nonzero $Y$ at once, is equivalent to the absence of a nonnull finite endogenous solution of the homogeneous equation. When the weights have a characteristic exponent, the disintegration theorem of Alsmeyer, Biggins and Meiners shows that the conditional supremum is infinite on the survival event of an endogenous fixed point of the smoothing transform, and the conjecture holds.

Most cited in the text:

- D. J. Aldous and A. Bandyopadhyay, A survey of max-type recursive distributional equations, Ann. Appl. Probab. 15 (2005), 1047--1110. (cited 13 times)
- G. Alsmeyer, J. D. Biggins and M. Meiners, The functional equation of the smoothing transform, Ann. Probab. 40 (2012), 2069--2105. (cited 8 times)
- E. Aidekon, Y. Hu and Z. Shi, Boundedness of discounted tree sums, Acta Math. Sin. (Engl. Ser.) 42 (2026), 1639--1661. arXiv:2409.01048. (cited 1 time)
- G. Alsmeyer and M. Meiners, A min-type stochastic fixed-point equation related to the smoothing transformation, Theory Stoch. Process. 15 (2009), 19--41. (cited 1 time)


### Supplementary Material for: Boundary and Interface Classes for Universal Chern Hamiltonians via Doubling and Jamming

Folder: [Doubling-and-Jamming-A-Universal-Chern-Hamiltonian-on-Triangulated-Surfaces-with-Boundary](public/Doubling-and-Jamming-A-Universal-Chern-Hamiltonian-on-Triangulated-Surfaces-with-Boundary) (source `public/Doubling-and-Jamming-A-Universal-Chern-Hamiltonian-on-Triangulated-Surfaces-with-Boundary/paper_supplement.tex`)

What the paper claims: This document collects the secondary results, full appendix proofs, all robustness variants, hexagonal and square benchmark symbols, the symbolic verification appendix, and the full numerical record for the main paper ``Boundary and Interface Classes for Universal Chern Hamiltonians via Doubling and Jamming''. The main results, abstract, introduction, and headline theorems are stated in the main paper; cross-references to the main paper use the M- prefix. The structure of the supplement is: full proofs of the finite-$M$ Schur-complement estimates (); the sign ledger (); two-band hexagonal and square benchmark symbols and their proofs (); the robustness variants for finite defects, finite corners, tail-split and annular families (); the Section 5 variants (); the Roe-algebra interface construction variants (); the symbolic verification appendix (); the detailed appendix proofs of every body result (); the full numerical experiments (); and the reproducibility appendix (). This supplement and the companion code are distributed through the project GitHub repository (https://github.com/yspennstate/Doubling-and-Jamming-A-Universal-Chern-Hamiltonian-on-Triangulated-Surfaces-with-Boundary).

Most cited in the text:

- N. Higson and E. Prodan, A Universal Chern Model on Arbitrary Triangulations, arXiv:2510.20862, doi:10.48550/arXiv.2510.20862. (cited 7 times)
- N. Higson and E. Prodan, Universal Chern Model on Arbitrary Triangulations, Phys. Rev. Lett. 136 (2026), no. 9, 096602, doi:10.1103/66x5-dvqq. (cited 7 times)
- E. E. Ewert and R. Meyer, Coarse geometry and topological phases, Comm. Math. Phys. 366 (2019), 1069--1098, doi:10.1007/s00220-019-03303-z. (cited 4 times)
- A. Hatcher, Algebraic Topology, Cambridge University Press, 2002. (cited 4 times)


### The stationary law of the leftmost particles in Aldous's drift-jump process

Folder: [drift-jump-leftmost-particles](public/drift-jump-leftmost-particles) (source `public/drift-jump-leftmost-particles/paper/main.tex`)

What the paper claims: In Aldous's drift-jump process, $k$ particles $0<X_1<\dots<X_k$ move to the right with velocity equal to their position, and at the events of a rate-one space-time Poisson process the nearest particle to the right of the event jumps to it. Aldous asked for a fairly explicit description of the stationary distribution. We give a self-contained proof that the stationary distribution is unique and that in stationarity $X_i=\Gamma_{\tau_i}$, where $\Gamma_1<\Gamma_2<\dots$ are the points of a rate-one Poisson process and, independently, $\tau_i$ is the first $n$ for which the longest increasing subsequence of $n$ independent uniform variables has length $i$; this is a form of a representation of Aldous and Diaconis. Equivalently, $\Pp(X_{k_1}>s_1,\dots,X_{k_r}>s_r)$ is the probability that the Poissonized longest increasing subsequence stays below $k_a$ at the times $s_a$. We evaluate every such probability as $e^{-s_r}$ times a finite determinant with Bessel-function entries, of size at most $k(k-1)$ for the first $k$ particles. For a single particle this is Gessel's Toeplitz determinant. As a consequence $\E(X_i-X_{i-1})$ is the constant $c(i)$ of Aldous and Diaconis in the logarithmic growth of the $i$-th pile in patience sorting.

Most cited in the text:

- D. Aldous and P. Diaconis, Longest increasing subsequences: from patience sorting to the Baik--Deift--Johansson theorem, Bull. Amer. Math. Soc. (N.S.) 36 (1999), 413--432. (cited 6 times)
- D. Aldous and P. Diaconis, Patience sorting, longest increasing subsequences and a continuous space analog of the simple asymmetric exclusion process, unpublished notes, 8 July 1993, https://www.stat.berkeley.edu/ aldous/Research/OP/patienc (cited 4 times)
- D. J. Aldous, A one-dimensional drift-jump particle process, open problem, posted February 2018, https://www.stat.berkeley.edu/ aldous/Research/OP/left_Hamm.html. (cited 2 times)
- D. Aldous and P. Diaconis, Hammersley's interacting particle process and longest increasing subsequences, Probab. Theory Related Fields 103 (1995), 199--213. (cited 1 time)


### Learned representations and kernel corrections for radiative-transfer emulation

Folder: [emit-oco2-kernel-emulators](public/emit-oco2-kernel-emulators) (source `public/emit-oco2-kernel-emulators/paper/emit_kernel_dnn.tex`)

What the paper claims: We compare neural networks, exact Matern kernel regression and their combinations as emulators of a six-dimensional radiative-transfer table on the 285-band EMIT grid, and we study how their forward accuracy carries over to reflectance retrieval. Over ten partitions of 23,313 states, a kernel with one length scale per input reaches $0.095\%$ mean relative radiance error and a network $0.387\%$; a kernel on the concatenated hidden features of five networks reaches $0.076\%$. Forward and inverse rankings disagree. A convex stack improves on a wide feature kernel by only $0.0006$ radiance percentage points, yet its 95th-percentile reflectance error is larger at every partition, three times larger on average. We prove that on the physical domain the constrained retrieval error is at most the retrieval-weighted component error divided by the transmission, with constant one, that the rate this implies is sharp, and that errors proportional to the transmission lose no rate. The reversal persists on the physical domain of the retrieval and when every family is retrained on physically admissible targets only; on a second radiative-transfer code, whose transmissions stay away from zero outside one opaque band, it is much weaker.

Most cited in the text:

- M. A. A. Mazid and N. Rishe. Multi-fidelity emulation of atmospheric correction coefficients with physics-guided Kolmogorov--Arnold networks. Remote Sensing, 18(11):1826, 2026. (cited 5 times)
- C. E. Rasmussen and C. K. I. Williams. Gaussian Processes for Machine Learning. MIT Press, 2006. (cited 4 times)
- A. Caponnetto and E. De Vito. Optimal rates for the regularized least-squares algorithm. Foundations of Computational Mathematics, 7(3):331--368, 2007. (cited 3 times)
- S. Fischer and I. Steinwart. Sobolev norm learning rates for regularized least-squares algorithms. Journal of Machine Learning Research, 21(205):1--38, 2020. (cited 3 times)


### Zero speed for excited random walks on the event of non-transience

Folder: [excited-walk-zero-speed-non-transience](public/excited-walk-zero-speed-non-transience) (source `public/excited-walk-zero-speed-non-transience/paper/main.tex`)

What the paper claims: An excited random walk on $\Z^d$ moves, on its $i$-th visit to a site $x$, according to the $i$-th entry of a stack of transition probabilities attached to $x$; the stacks are independent and identically distributed over the sites. Kosygina and Zerner asked whether $X_n/n\to0$ almost surely on the event that $|X_n|$ does not tend to infinity, assuming only that the stacks are i.i.d. and every entry is positive. We prove that it does, in every dimension $d\ge2$ (the case $d=1$ is due to Amir, Berger and Orenshtein) and with no further restriction on the stacks. We also prove for excited random walks the form of Zerner's theorem on random walk in random environment: if, for a coordinate direction $e$, the events $X_n\cdot e\to+\infty$ and $X_n\cdot e\to-\infty$ both have probability zero, then $X_n\cdot e/n\to0$ almost surely. Together with the directional law of large numbers of Kosygina and Zerner, this gives the almost sure convergence of $X_n/n$ under the same two assumptions. The limit takes at most two values, $v$ and $-cv$ with $c\ge0$, and for every $\ell\in\R^d\setminus\{0\}$, $X_n\cdot\ell/n\to0$ almost surely on the event that $X_n\cdot\ell$ tends neither to $+\infty$ nor to $-\infty$. The proof replaces Zerner's use of the strong Markov property at the first visit of the walk to each hyperplane $\{x:x\cdot e=m\}$ by a sum over paths of bounded length.

Most cited in the text:

- E. Kosygina and M. P. W. Zerner, Excited random walks: results, methods, open problems, Bull. Inst. Math. Acad. Sin. (N.S.) 8 (2013), 105--157, arXiv:1204.1895. (cited 15 times)
- M. P. W. Zerner, A non-ballistic law of large numbers for random walks in i.i.d. random environment, Electron. Commun. Probab. 7 (2002), 191--197, 10.1214/ECP.v7-1060. (cited 11 times)
- G. Amir, N. Berger and T. Orenshtein, Zero-one law for directional transience of one dimensional excited random walks, Ann. Inst. Henri Poincare Probab. Stat. 52 (2016), 47--57, 10.1214/14-AIHP615. (cited 3 times)
- A. Drewitz and A. F. Ramirez, Asymptotic direction in random walks in random environment revisited, Braz. J. Probab. Stat. 24 (2010), 212--225, 10.1214/09-BJPS028. (cited 3 times)


### Relaxation of the one-dimensional Fredrickson--Andersen model from a single infection at high density

Folder: [fa1f-relaxation-high-density](public/fa1f-relaxation-high-density) (source `public/fa1f-relaxation-high-density/paper/main.tex`)

What the paper claims: Consider the one-spin facilitated Fredrickson--Andersen model on $\Z$ with equilibrium density $q$ of infected sites. For $q>1/2$ we prove that, for every initial law and every local function, the difference between the expectation at time $t$ and the equilibrium mean is bounded by an exponentially small term plus the probability that the initial distance from the origin to the nearest infection exceeds a fixed multiple of $t$; the constants depend only on $q$ and the support of the function. No independence, stationarity or uniform control of the gaps between infections is assumed. Hence the two conjectures of Martinelli, Shapira and Toninelli on convergence from any law with an infection, and on exponential relaxation when the distance from the origin to the nearest infection has an exponential tail, hold for every $q>1/2$; this includes a single initial infection. The proof transfers the relaxation theorem of Blondel, Cancrini, Martinelli, Roberto and Toninelli from uniform to origin-centred hypotheses.

Most cited in the text:

- O. Blondel, N. Cancrini, F. Martinelli, C. Roberto and C. Toninelli, Fredrickson--Andersen one spin facilitated model out of equilibrium, Markov Process. Related Fields 19 (2013), no. 3, 383--406. 1205.4584 (cited 12 times)
- N. Cancrini, F. Martinelli, C. Roberto and C. Toninelli, Kinetically constrained spin models, Probab. Theory Related Fields 140 (2008), no. 3--4, 459--504. 10.1007/s00440-007-0072-3 (cited 3 times)
- N. Cancrini, F. Martinelli, R. Schonmann and C. Toninelli, Facilitated oriented spin models: some non equilibrium results, J. Stat. Phys. 138 (2010), no. 6, 1109--1123. 10.1007/s10955-010-9923-x (cited 3 times)
- F. Martinelli, A. Shapira and C. Toninelli, Long time behaviour of one facilitated kinetically constrained models: results and open problems, preprint, 2025. 2510.20461 (cited 3 times)


### Multicommodity flow, the relaxation time and the diameter

Folder: [flow-parameter-diameter](public/flow-parameter-diameter) (source `public/flow-parameter-diameter/paper/main.tex`)

What the paper claims: For a finite reversible Markov chain on $n$ states let $\inf_{\bfF}\psi(\bfF)$ be the least congestion of a family of unit flows from each state to the stationary distribution, in the normalisation of Aldous and Fill; we call it the flow parameter. Sinclair showed that it is at most a constant times the relaxation time $\tau_2$ times $\log n$. Open Problem 4.49(ii) of Aldous and Fill's Reversible Markov Chains and Random Walks on Graphs, which they attribute to Sinclair, asks whether $\log n$ can be replaced by the diameter $\Delta$ of the transition graph. For general chains the answer is negative for a simple reason: adding transitions of small probability between all pairs of states of the random walk on an expander makes $\Delta=1$, does not increase $\tau_2$, and keeps the flow parameter of order $\log n$. We show that the answer is negative also for simple random walks on graphs, for every constant and already on graphs of diameter two. For the simple random walk on the cone over a $d$-regular Ramanujan graph on $n$ vertices the diameter is $2$, the relaxation time is at most $(d+1)/(d+1-2\sqrt{d-1})$, and the flow parameter tends to $2(d+1)$ as $n\to\infty$; so the ratio of the flow parameter to $\tau_2\Delta$ is at least $d+1-2\sqrt{d-1}$ in the limit and is unbounded over $d$. The length-weighted form of the flow parameter fails as well, on these graphs and already on bounded-degree expanders. On the cones over the incidence graphs of projective planes of order $s$ the flow parameter has a closed form, and the ratio increases with $s$ to $5/2$ and exceeds $2$ exactly when $s\ge38$. For simple random walks a diameter bound does hold with a constant of order $\log D$, $D$ the maximum degree, and the cones show that this order cannot be lowered below $\log D/\log\log D$.

Most cited in the text:

- D. Aldous and J. A. Fill, Reversible Markov Chains and Random Walks on Graphs, unfinished monograph, 2002 (recompiled 2014; the numbering is that of the online edition), https://www.stat.berkeley.edu/ aldous/RWG/book.html. (cited 9 times)
- A. Sinclair, Improved bounds for mixing rates of Markov chains and multicommodity flow, Combin. Probab. Comput. 1 (1992), 351--370. (cited 3 times)
- C. Bordenave, A new proof of Friedman's second eigenvalue theorem and its extension to random lifts, Ann. Sci. Ec. Norm. Super. (4) 53 (2020), 1393--1439, arXiv:1502.04482. (cited 2 times)
- W. Feit and G. Higman, The nonexistence of certain generalized polygons, J. Algebra 1 (1964), 114--131. (cited 2 times)


### Convergence of the forward-loop-erased ants process at distance two

Folder: [forward-loop-erased-ants-convergence](public/forward-loop-erased-ants-convergence) (source `public/forward-loop-erased-ants-convergence/paper/main.tex`)

What the paper claims: In the forward-loop-erased ants process, the $n$th ant walks from a nest $N$ to a food source $F$ with transition probabilities proportional to the current edge weights, and every edge of the chronological loop erasure of its path gains weight one. Armfield and Mailler showed that when $N$ and $F$ are at distance two the ants find the shortest paths, and left open whether $W(n)/n$ converges. We show that it converges almost surely and that every path of length two keeps a positive share in the limit. The key fact is that for a common neighbour $i$ of $N$ and $F$ the relative drift of $W_{\{N,i\}}(n)W_{\{i,F\}}(n)$ is the inverse effective conductance between $N$ and $F$, the same for all $i$, up to a summable error; hence ratios of these products converge on every finite graph.

Most cited in the text:

- W. Armfield and C. Mailler, The forward-loop-erased ants walk, preprint, 2026, 2610.18453. (cited 8 times)
- D. Kious, C. Mailler and B. Schapira, Finding geodesics on graphs using reinforcement learning, Ann. Appl. Probab. 32 (2022), 3889--3929, 2010.04820. (cited 4 times)
- D. Kious, C. Mailler and B. Schapira, The trace-reinforced ants process does not find shortest paths, J. Ec. polytech. Math. 9 (2022), 505--536, 2106.10559. (cited 2 times)
- W. Armfield, An analysis of learning processes through reinforced random walks, PhD thesis, University of Bath, 2026. (cited 1 time)


### Fourier entropy of threshold functions and their compositions

Folder: [fourier-entropy-threshold-functions](public/fourier-entropy-threshold-functions) (source `public/fourier-entropy-threshold-functions/paper/main.tex`)

What the paper claims: We prove the Fourier entropy--influence inequality for every linear threshold function, with a constant below $8.937$ and no restrictions on its weights or threshold. The argument applies to regular Boolean functions and gives logarithmic bounds for their Boolean combinations and for unions with bounded variable overlap. Character multiplication preserves the estimates and yields bounds by influence minus variance. Under arbitrary product measures, symmetric thresholds satisfy the strengthened inequality needed for read-once composition, uniformly in depth and fan-in. A joint description of each Fourier set refines the overlap estimate and recovers constant bounds for addressing. Exact selector identities extend the bound to orthogonal multiplexers with shared data. Rare activation preserves the optimal constant of unrestricted FEI. The proofs combine pivotal antichains, spectral reference measures, and product-measure composition.

Most cited in the text:

- R. O'Donnell, Analysis of Boolean Functions, Cambridge University Press, Cambridge, 2014. https://www.cs.cmu.edu/ odonnell/papers/Analysis-of-Boolean-Functions-by-Ryan-ODonnell.pdfAuthor's edition. (cited 3 times)
- S. Arunachalam, S. Chakraborty, M. Koucky, N. Saurabh and R. de Wolf, Improved bounds on Fourier entropy and min-entropy, ACM Trans. Comput. Theory 13 (2021), no. 4, Article 22, 40 pp. https://doi.org/10.1145/3470860doi:10.1145/3470860. htt (cited 2 times)
- V. Lecomte and L.-Y. Tan, Sharper bounds on the Fourier concentration of DNFs, in: 2021 IEEE 62nd Annual Symposium on Foundations of Computer Science (FOCS), IEEE, 2022, 930--941. https://doi.org/10.1109/FOCS52979.2021.00094doi:10.1109/FOCS (cited 2 times)
- R. O'Donnell and L.-Y. Tan, A composition theorem for the Fourier entropy--influence conjecture, in: ICALP 2013, Lecture Notes in Comput. Sci. 7965, Springer, Heidelberg, 2013, 780--791. https://doi.org/10.1007/978-3-642-39206-1_66doi:10.10 (cited 2 times)


### The sharp diameter threshold for unimodality of free Brownian motion

Folder: [free-brownian-unimodality-sharp-constant](public/free-brownian-unimodality-sharp-constant) (source `public/free-brownian-unimodality-sharp-constant/paper/free_unimodality_sharp.tex`)

What the paper claims: Let $\mu$ be a compactly supported probability measure on $\R$ whose support has diameter $D_\mu$, and let $S(0,t)$ be the semicircle law of variance $t$. Hasebe and Ueda proved that the free Brownian motion started from $\mu$, whose law at time $t$ is $\mu\bp S(0,t)$, is unimodal for every $t\ge 4D_\mu^2$, and asked for the optimal constant $C$ in the statement ``$\mu\bp S(0,t)$ is unimodal for all $t\ge C D_\mu^2$''. We show that $C=1$: $\mu\bp S(0,t)$ is unimodal for every $t\ge D_\mu^2$, the symmetric two-point law is the only measure that is not unimodal at every earlier time, and every other measure of the same diameter becomes unimodal strictly before $t=D_\mu^2$. Two proofs are given. Both reduce the level-set criterion of Biane's density formula to measures with two atoms, one through an extreme-point decomposition, the other through a pair of moment inequalities, and both end in an explicit polynomial inequality in three variables. The same argument gives the sharp constant $D_\mu^2/4$ for classical Brownian motion and a criterion for symmetric kernels which recovers the classical two-Gaussian and two-Cauchy thresholds. The polynomial core of both proofs is verified in Lean 4, and the thresholds are computed numerically from the density itself.

Most cited in the text:

- T. Hasebe and Y. Ueda, Large time unimodality for classical and free Brownian motions with initial distributions, ALEA Lat. Am. J. Probab. Math. Stat. 15 (2018), 353--374. arXiv:1710.08240. (cited 13 times)
- J. Behboodian, On the modes of a mixture of two normal distributions, Technometrics 12 (1970), 131--139. (cited 2 times)
- P. Biane, On the free convolution with a semi-circular distribution, Indiana Univ. Math. J. 46 (1997), 705--718. (cited 2 times)
- I. Eisenberger, Genesis of bimodal distributions, Technometrics 6 (1964), 357--363. (cited 2 times)


### Free multiplicative convolution and log-unimodality: three questions of Hasebe, Ueda and Wang

Folder: [free-multiplicative-log-unimodality](public/free-multiplicative-log-unimodality) (source `public/free-multiplicative-log-unimodality/paper/main.tex`)

What the paper claims: Hasebe, Ueda and Wang proved that free multiplicative convolution with the free positive multiplicative Brownian motion $\sigma_t$ preserves log-unimodality of multiplicatively symmetric laws, and asked three questions about how far this extends. We answer all three. The free multiplicative convolution of two multiplicatively symmetric log-unimodal laws need not be log-unimodal: for $L\ge6$, the logarithm of the free multiplicative square of the log-uniform law on $[e^{-L},e^{L}]$ has a density with a strict local minimum at $0$. Compact support of $\nu$ does not make $\sigma_t\boxtimes\nu$ log-unimodal for large $t$, since for $\nu=(\delta_{1/10}+\delta_{10})/2$ it fails for every $t>0$; when $\nu$ is in addition log-unimodal and supported in $[\alpha,\beta]$, the convolution is log-unimodal for all $t\ge(\pi/2)(\beta/\alpha+\alpha/\beta)$. Finally, $\sigma_t$ is not $\boxtimes$-strongly log-unimodal for any $t>0$, which extends the small-time result of Hasebe, Ueda and Wang to all times. The numerical inequalities behind the first and third answers and the root count behind the second are verified in Lean 4 with Mathlib.

Most cited in the text:

- T. Hasebe, Y. Ueda and J.-C. Wang, Log-unimodality for free positive multiplicative Brownian motion, Colloq. Math. 169 (2022), no. 2, 209--226. https://doi.org/10.4064/cm8413-6-2021doi:10.4064/cm8413-6-2021. https://arxiv.org/abs/2009.13848 (cited 13 times)
- P. Zhong, On the free convolution with a free multiplicative analogue of the normal distribution, J. Theoret. Probab. 28 (2015), no. 4, 1354--1379. https://doi.org/10.1007/s10959-014-0556-xdoi:10.1007/s10959-014-0556-x. https://arxiv.org/ab (cited 3 times)
- H. Bercovici and D. Voiculescu, Free convolution of measures with unbounded support, Indiana Univ. Math. J. 42 (1993), no. 3, 733--773. https://doi.org/10.1512/iumj.1993.42.42033doi:10.1512/iumj.1993.42.42033. (cited 2 times)
- L. de Moura and S. Ullrich, The Lean 4 theorem prover and programming language, in: Automated Deduction -- CADE 28, Lecture Notes in Comput. Sci. 12699, Springer, Cham, 2021, 625--635. https://doi.org/10.1007/978-3-030-79876-5_37doi:10.1007 (cited 2 times)


### Free strong unimodality and a conjecture of Hasebe and Ueda

Folder: [free-strong-unimodality](public/free-strong-unimodality) (source `public/free-strong-unimodality/paper/main.tex`)

What the paper claims: A probability measure $\mu$ on $\R$ is freely strongly unimodal if $\mu\boxplus\nu$ is unimodal for every unimodal probability measure $\nu$. We prove that only point masses have this property. This answers Problem 3.11 of Hasebe and Ueda, who proved it for measures of finite variance. The witnesses are explicit and do not depend on $\mu$: if $\mu$ is not a point mass, then $\mu\boxplus\bigl(\frac1{100}\delta_0+\frac{99}{100}U[0,L]\bigr)$ is not unimodal for all large $L$. We also show that the classical half of their Conjecture 5.5 fails for one-sided stable kernels. If $0<\alpha<1$ and $S_t$ is the law at time $t$ of a positive strictly $\alpha$-stable process, then for every nonnegative Borel function $f$ there is a probability measure $\mu$ with $\int f\,d\mu<\infty$ such that $\mu\ast S_t$ is unimodal for no $t>0$. In particular, a finite moment of order $2+\alpha$, or of every order, does not give unimodality in large time.

Most cited in the text:

- T. Hasebe and Y. Ueda, Large time unimodality for classical and free Brownian motions with initial distributions, ALEA Lat. Am. J. Probab. Math. Stat. 15 (2018), 353--374. https://doi.org/10.30757/ALEA.v15-15doi:10.30757/ALEA.v15-15. (cited 11 times)
- S. T. Belinschi and H. Bercovici, A new approach to subordination results in free probability, J. Anal. Math. 101 (2007), 357--365. https://doi.org/10.1007/s11854-007-0013-1doi:10.1007/s11854-007-0013-1. (cited 2 times)
- P. Biane, Processes with free increments, Math. Z. 227 (1998), 143--174. https://doi.org/10.1007/PL00004363doi:10.1007/PL00004363. (cited 2 times)
- H. Bercovici and D. Voiculescu, Free convolution of measures with unbounded support, Indiana Univ. Math. J. 42 (1993), 733--773. https://doi.org/10.1512/iumj.1993.42.42033doi:10.1512/iumj.1993.42.42033. (cited 1 time)


### Gaussian-integer spectra of random sign matrices

Folder: [gaussian-integer-spectra](public/gaussian-integer-spectra) (source `public/gaussian-integer-spectra/main.tex`)

What the paper claims: Let $M_n$ be an $n\times n$ matrix whose entries are independent uniform signs. For every $n\geq1$, we construct $2^{\lceil n^2/2\rceil}3^{\lfloor n/2\rfloor}$ distinct sign matrices whose eigenvalues lie in $\Z[i]$. Hence $\Pp\bigl(\Spec(M_n)\subseteq\Z[i]\bigr) \geq 3^{\lfloor n/2\rfloor}2^{-\lfloor n^2/2\rfloor}.$ This contradicts Vu's Conjecture 9.5, which predicts the probability $2^{-(1+o(1))n^2}$. The construction uses block shears with triangular diagonal blocks. All matrices in the odd-dimensional family have integer spectra, as do exactly two thirds of the even-dimensional family. We do not obtain a matching upper bound.

Most cited in the text:

- S. Eberhard, The characteristic polynomial of a random matrix, Combinatorica 42 (2022), 491--527. https://doi.org/10.1007/s00493-020-4657-0doi:10.1007/s00493-020-4657-0. https://arxiv.org/abs/2008.01223arXiv:2008.01223. (cited 1 time)
- A. Ferber, V. Jain, A. Sah and M. Sawhney, Random symmetric matrices: rank distribution and irreducibility of the characteristic polynomial, Math. Proc. Cambridge Philos. Soc. 174 (2023), no. 2, 233--246. https://doi.org/10.1017/S0305004122 (cited 1 time)
- G. Martin and E. B. Wong, Almost all integer matrices have no integer eigenvalues, Amer. Math. Monthly 116 (2009), no. 7, 588--597. https://doi.org/10.1080/00029890.2009.11920976doi:10.1080/00029890.2009.11920976. https://arxiv.org/abs/0712 (cited 1 time)
- V. H. Vu, Recent progress in combinatorial random matrix theory, Probability Surveys 18 (2021), 179--200. https://doi.org/10.1214/20-PS346doi:10.1214/20-PS346. https://arxiv.org/abs/2005.02797arXiv:2005.02797. (cited 1 time)


### Every geodesic spanning tree of a Cayley graph has branching number equal to the growth rate

Folder: [geodesic-tree-branching](public/geodesic-tree-branching) (source `public/geodesic-tree-branching/paper.tex`)

What the paper claims: A spanning tree $T$ of a graph $G$, rooted at a vertex $o$, is geodesic if the distance from $o$ to every vertex is the same in $T$ as in $G$. Lyons and Peres asked whether every geodesic spanning tree of the Cayley graph of a finitely generated group of growth rate $b$ has branching number $b$; they proved this for the lexicographically minimal tree. We show that the answer is yes, and more generally that every geodesic spanning tree of an infinite, connected, locally finite, quasi-transitive graph has branching number equal to the growth rate of the graph. Consequently the critical probability of Bernoulli percolation on any such tree is $1/b$.

Most cited in the text:

- Lyons, Russell and Peres, Yuval, Probability on Trees and Networks (2016) (cited 4 times)
- Lyons, Russell, Random walks and percolation on trees (1990) (cited 3 times)
- Cleary, Sean and Taback, Jennifer, Dead end words in lamplighter groups and other wreath products (2005) (cited 1 time)
- Fekete, Michael, Uber die Verteilung der Wurzeln bei gewissen algebraischen Gleichungen mit ganzzahligen Koeffizienten (1923) (cited 1 time)


### Almost every finite Markov chain has only coalescing grand couplings

Folder: [grand-coupling-coalescence](public/grand-coupling-coalescence) (source `public/grand-coupling-coalescence/paper/main.tex`)

What the paper claims: A grand coupling of a finite Markov chain runs copies of the chain from every state by applying independent random maps with a common law; its coalescence number is the eventual number of distinct trajectories. Grimmett and Holmes asked whether, for a random transition matrix with independent uniform weights, every grand coupling has coalescence number one almost surely. We show that it does. If some grand coupling of $P$ has coalescence number $k\ge2$, then there are $k$ states $W$ and a partition $\{Z_w:w\in W\}$ of the state space with $w\in Z_w$ such that the matrix $\bigl(P(w,Z_{w'})\bigr)_{w,w'\in W}$ is doubly stochastic; for $k$ equal to the number of states this is the Birkhoff--von Neumann condition. Each such condition is a non-trivial affine equation in $P$, and there are finitely many, so the matrices with a non-coalescing grand coupling form a Lebesgue-null set.

Most cited in the text:

- G. R. Grimmett and M. Holmes, Coalescence in Markov chains, J. Theoret. Probab. 39 (2026), no. 3, 10.1007/s10959-026-01500-w, 2510.13572. (cited 12 times)
- G. R. Grimmett and M. Holmes, Non-coupling from the past, in: In and Out of Equilibrium 3: Celebrating Vladas Sidoravicius, Progress in Probability 77, Birkhauser/Springer, Cham, 2021, pp. 471--485, 10.1007/978-3-030-60754-8_22. (cited 8 times)
- K. Yano, Random walk in a finite directed graph subject to a road coloring, J. Theoret. Probab. 26 (2013), 259--283, 10.1007/s10959-011-0398-8, 1005.0079. (cited 4 times)
- G. Budzban and A. Mukherjea, A semigroup approach to the road coloring problem, in: Probability on Algebraic Structures, Contemp. Math. 261, Amer. Math. Soc., Providence, RI, 2000, pp. 195--207, 10.1090/conm/261/04141. (cited 1 time)


### Finite touching sets between percolation clusters on grandparent graphs

Folder: [grandparent-graph-cluster-repulsion](public/grandparent-graph-cluster-repulsion) (source `public/grandparent-graph-cluster-repulsion/paper/main.tex`)

What the paper claims: A transitive graph exhibits cluster repulsion at the parameter $p$ if, almost surely, any two distinct clusters of Bernoulli bond percolation with parameter $p$ are joined by only finitely many edges. Timár proved cluster repulsion for every unimodular quasi-transitive graph and every $p$, and the nonunimodular case is open. Bell, Chu, Rodgers, Terlov and Tserunyan proved that on nonunimodular graphs the touching sets have finite modular weight, which leaves open whether two light clusters can touch along infinitely many edges. We prove cluster repulsion at every $p\in[0,1]$ for the grandparent graphs $\GP$, $b\ge2$, the standard transitive nonunimodular examples, whose infinite clusters are light for $1/b<p<1$. The proof shows that every two-point function $p\mapsto\PP_p(u\leftrightarrow v)$ is continuous on $(0,1)$, by integrating out each descendant cone through an exact one-variable equation and bounding the effect of the missing ancestors uniformly in $p$, and then applies the sprinkling argument of Häggström, Peres and Schonmann.

Most cited in the text:

- S. Bell, T. Chu, O. Rodgers, G. Terlov and A. Tserunyan, Heavy repulsion of clusters in Bernoulli percolation, preprint (2025), 2509.10631. (cited 6 times)
- O. Häggström, Y. Peres and R. H. Schonmann, Percolation on transitive graphs as a coalescent process: relentless merging followed by simultaneous uniqueness, in Perplexing Problems in Probability, Progr. Probab. 44, Birkhäuser, Boston, 1999 (cited 5 times)
- L. Ménard and D. Sénizergues, Percolation on grandparent graphs of Bienaymé trees, preprint (2026), 2611.09762. (cited 2 times)
- Math Brain repository, 2026, https://github.com/yspennstate/math-brain-public. (cited 2 times)


### Conserved charges in linearly reinforced graph urns

Folder: [graph-urn-conserved-charges](public/graph-urn-conserved-charges) (source `public/graph-urn-conserved-charges/main.tex`)

What the paper claims: In the graph-based Polya urn with linear reinforcement (WARM with $\alpha=1$), every vector $\sigma$ in the kernel of the unsigned vertex--edge incidence matrix yields an exact martingale $\sum_e\sigma_e H(N_e-1)$, where $H$ is the harmonic number. These charges are the flat directions of the Lyapunov function, and they determine which equilibrium the process selects. On the even cycle $C_{L}$ the limit is $(1+u,1-u,\dots)$ with $L\,\mathrm{artanh}(u)$ equal to the terminal value of the charge, and $\sqrt{L}\,\mathrm{artanh}(u)$ converges in law to a centred Gaussian as $L\to\infty$. For large even cycles this describes the law of the random limit, in the continuous-time form of the question raised by Chen and Lucas and by Lima for the discrete-time urn.

Most cited in the text:

- R. van der Hofstad, M. Holmes, A. Kuznetsov, W. Ruszel, Strongly reinforced Polya urns with graph-based competition, Ann. Appl. Probab. 26 (2016). (cited 2 times)
- G. Aletti, A. Collevecchio, I. Crimaldi, M. Deijfen, S. Dereich, A. Ghiglietti, R. van der Hofstad, M. Holmes, D. Kious, V. Kleptsyn, B. Lodewijks, P. Morters and B. Schapira, Open problems in stochastic reinforcement models, in 2023 MATRIX (cited 1 time)
- M. Benaim, I. Benjamini, J. Chen, Y. Lima, A generalized Polya's urn with graph based interactions, Random Structures Algorithms 46 (2015), 614--634. (cited 1 time)
- M. Benaim, Dynamics of stochastic approximation algorithms, Seminaire de Probabilites XXXIII, Lecture Notes in Math. 1709, Springer (1999). (cited 1 time)


### The discrepancy of Sylvester--Hadamard matrices in odd dimension

Folder: [hadamard-discrepancy-odd](public/hadamard-discrepancy-odd) (source `public/hadamard-discrepancy-odd/paper.tex`)

What the paper claims: Let $H_k$ be the $2^k\times 2^k$ Sylvester--Hadamard matrix and let $\disc(H_k)$ be the minimum of $\|H_kx\|_\infty$ over sign vectors $x$. It is known that $\disc(H_k)=2^{k/2}$ for even $k$, and it has been conjectured that $\disc(H_k)=2^{(k+1)/2}$ for every odd $k$. We show that $\disc(H_k)=2^k-2\rho(1,k)$, where $\rho(1,k)$ is the covering radius of the first-order Reed--Muller code of length $2^k$. Known values and bounds for this covering radius then show that the conjecture holds for $k\le 7$ and fails for every odd $k\ge 9$; in fact $\disc(H_k)\le \tfrac78\,2^{(k+1)/2}$ for every odd $k\ge 9$, and $\disc(H_9)=28$ by the determination $\rho(1,9)=242$ of Wang, Lou and Wang. Determining $\disc(H_k)$ for odd $k\ge 11$ is therefore equivalent to determining $\rho(1,k)$.

Most cited in the text:

- A. S. Bandeira, A. Kireeva, A. Maillard and A. Rodder, Randomstrasse101: Open problems of 2024, arXiv:2504.20539, 2025. (cited 4 times)
- E. R. Berlekamp and L. R. Welch, Weight distributions of the cosets of the $(32,6)$ Reed--Muller code, IEEE Trans. Inform. Theory 18 (1972), 203--207. (cited 2 times)
- G. Cohen, I. Honkala, S. Litsyn and A. Lobstein, Covering Codes, North-Holland Mathematical Library 54, North-Holland, Amsterdam, 1997. (cited 2 times)
- J. J. Mykkeltveit, The covering radius of the $(128,8)$ Reed--Muller code is $56$, IEEE Trans. Inform. Theory 26 (1980), 359--362. (cited 2 times)


### Read-once formulas and a question of Han on the Fourier entropy-influence conjecture

Folder: [han-question-read-once-formulas](public/han-question-read-once-formulas) (source `public/han-question-read-once-formulas/paper/han_question_read_once_trees.tex`)

What the paper claims: For a Boolean function $f$ and a coordinate $k$, let $Q_k(f)=\sum_{S\not\ni k}|\hf(S)\hf(S\cup\{k\})|/I_k(f)$, where $I_k(f)$ is the influence of $k$. In his proof of a new bound towards the Fourier entropy-influence conjecture, Han asked whether there is a universal constant $c$ such that every Boolean function has a coordinate $k$ with $Q_k(f)\le c$, and observed that this would imply the conjecture. We show that the answer is negative. For balanced alternating read-once AND-OR formulas we compute $Q_k$ exactly by a one-step recursion over the levels of the formula; it is the same at every coordinate. Choosing the fan-ins so that every gate below the root is true with probability at most $1/4$ gives monotone read-once formulas of depth $L$ on at most $2\cdot 7^{L-1}$ variables with $Q_k(f)\ge L$ for every $k$, so $\min_k Q_k(f)$ grows at least like $\log_2 n/\log_2 7$. Depth two gives the tribes functions, for which $\min_k Q_k$ approaches $4$ but stays below it. The Fourier entropy-influence conjecture is known for these formulas, so the inequality in Han's question fails on a class where the conjecture holds. By contrast, the drop of the Fourier entropy under splitting on a coordinate is less than $5+\ln 4$ times the influence of that coordinate, for every read-once formula and every coordinate.

Most cited in the text:

- X. Han, A new bound for the Fourier-entropy-influence conjecture, Combinatorica 45 (2025), Paper No. 4; arXiv:2312.08271v2. (cited 4 times)
- M. J. Gonzalez, P. MacManus and M. C. Pereyra, Further evidence towards the Fourier entropy-influence conjecture, arXiv:2606.00246, 2026. (cited 2 times)
- R. O'Donnell and L.-Y. Tan, A composition theorem for the Fourier entropy-influence conjecture, in: Automata, Languages, and Programming (ICALP 2013), Lecture Notes in Comput. Sci. 7965, Springer, 2013, 780--791. (cited 2 times)
- E. Friedgut and G. Kalai, Every monotone graph property has a sharp threshold, Proc. Amer. Math. Soc. 124 (1996), 2993--3002. (cited 1 time)


### The dimension of harmonic measure on Galton--Watson trees increases at small bias

Folder: [harmonic-dimension-small-bias](public/harmonic-dimension-small-bias) (source `public/harmonic-dimension-small-bias/paper/harmonic_dimension_slope.tex`)

What the paper claims: Let $T$ be a Galton--Watson tree without leaves whose offspring number $N$ is not constant and has finite mean $m$, and let $d_\lambda$ be the Hausdorff dimension of the harmonic measure of the $\lambda$-biased random walk on $T$, $0\le\lambda<m$. Lyons, Pemantle and Peres asked whether $d_\lambda$ increases with $\lambda$. We prove that $\lambda\mapsto d_\lambda$ is continuously differentiable on $[0,k_0)$, where $k_0$ is the smallest value taken by $N$, and that $\frac{d}{d\lambda}d_\lambda\Big|_{\lambda=0}=-\bigl(1-\E[1/N]\bigr)\Cov\bigl(\log N,1/N\bigr)>0.$ Hence $d_\lambda$ is strictly increasing on an interval $[0,\eps]$, with $\eps>0$ depending on the offspring law. No moment assumption beyond the finite mean is needed. The proof combines the formula of Lin and Rousselin for $d_\lambda$ with a contraction estimate, uniform over trees, for the recursion satisfied by the escape probabilities and by their derivatives in $\lambda$.

Most cited in the text:

- R. Lyons, R. Pemantle and Y. Peres, Unsolved problems concerning random walks on trees, in Classical and Modern Branching Processes, IMA Vol. Math. Appl. 84, Springer, 1997, 223--237. (cited 4 times)
- S. Lin, Harmonic measure for biased random walk in a supercritical Galton--Watson tree, Bernoulli 25 (2019), 3652--3672. (cited 4 times)
- P. Rousselin, Invariant measures, Hausdorff dimension and dimension drop of some harmonic measures on Galton--Watson trees, Electron. J. Probab. 23 (2018), paper no. 46, 1--31. (cited 4 times)
- R. Lyons, R. Pemantle and Y. Peres, Ergodic theory on Galton--Watson trees: speed of random walk and dimension of harmonic measure, Ergodic Theory Dynam. Systems 15 (1995), 593--619. (cited 2 times)


### Hub paths and the largest component of the barely subcritical configuration model

Folder: [hub-paths-barely-subcritical](public/hub-paths-barely-subcritical) (source `public/hub-paths-barely-subcritical/paper/main.tex`)

What the paper claims: For the configuration model with a degree sequence whose third moment converges, write $\eps_n=1-\nu_n$, where $\nu_n\to1$ from below is the size-biased mean minus one. Van der Hofstad asked to show that in the barely subcritical regime the largest component has order $\max\{\dmax/\eps_n,\ \eps_n^{-2}\log(n\eps_n^3)\}$, and predicted that it has size $(\dmax/\eps_n)(1+o_\PP(1))$ when $\eps_n$ tends to zero sufficiently slowly. We show that neither holds in this generality. We use degree sequences with vertices of degree one and three and a polynomial number of vertices of a large common degree $d$. Paths of $K$ such hubs joined by direct edges then appear, and the component of such a path is a tree with about $Kd/\eps_n$ vertices. Taking $K=2$ gives $L_1\ge(2-\eta)\dmax/\eps_n$ with high probability, for $\eps_n$ tending to zero as slowly as we like; letting $K\to\infty$ gives $L_1/\max\{\dmax/\eps_n,\eps_n^{-2}\log(n\eps_n^3)\}\to\infty$ in probability. In all examples the degree of a uniform vertex converges in law to a variable on $\{1,3\}$ with all three moments, and $n\eps_n^3\to\infty$.

Most cited in the text:

- R. van der Hofstad, Stochastic Processes on Random Graphs, lecture notes for the 47th Summer School in Probability, Saint-Flour, 2017, version of 12 July 2017, https://www.win.tue.nl/ rhofstad/SaintFlour_SPoRG.pdf. (cited 3 times)
- M. Coulson and G. Perarnau, Largest component of subcritical random graphs with given degree sequence, Electron. J. Probab. 28 (2023), 1--28, doi:10.1214/23-EJP921. (cited 2 times)
- K. Azuma, Weighted sums of certain dependent random variables, Tohoku Math. J. 19 (1967), 357--367. (cited 1 time)
- B. Bollobas, A probabilistic proof of an asymptotic formula for the number of labelled regular graphs, European J. Combin. 1 (1980), 311--316. (cited 1 time)


### Low-intensity Voronoi limits of correlated point processes in the hyperbolic plane

Folder: [hyperbolic-voronoi-correlated-nuclei](public/hyperbolic-voronoi-correlated-nuclei) (source `public/hyperbolic-voronoi-correlated-nuclei/paper/main.tex`)

What the paper claims: The Voronoi tessellations of a Poisson process of intensity $\lambda$ on the hyperbolic plane converge, as $\lambda\to0$, to the ideal Poisson--Voronoi tessellation. D'Achille and Khezeli asked whether other point processes can produce a different random ideal Voronoi diagram in the same limit, and named the $\alpha$-hyperbolic ensemble, as $\alpha\to0$, as a natural candidate. We show that this candidate gives the ideal Poisson--Voronoi tessellation again. More generally, the limit is the ideal Poisson--Voronoi tessellation whenever the $k$-point correlation functions are bounded by $C^k\lambda^k$ and the normalized correlations $\rho_k/\lambda^k$ tend to one uniformly on configurations whose points are at mutual distance at least $2\log(1/\lambda)-L$, for every fixed $k$ and $L$. Among families satisfying the bound, a different limit therefore requires, for some $k$, a relative discrepancy of the $k$-point correlation that does not vanish at distances $2\log(1/\lambda)+O(1)$.

Most cited in the text:

- M. D'Achille and A. Khezeli, Convergence towards ideal Poisson--Voronoi tessellations with a focus on Diestel--Leader graphs, preprint (2026), 2606.30517v2. (cited 17 times)
- M. D'Achille, N. Curien, N. Enriquez, R. Lyons and M. Unel, Ideal Poisson--Voronoi tessellations on hyperbolic spaces, Ann. Probab. 54 (2026), no. 2, 846--891, 10.1214/25-AOP1781, 2303.16831. (cited 6 times)
- S. Bhupatiraju, The low-intensity limit of Bernoulli--Voronoi and Poisson--Voronoi measures, Ph.D. thesis, Indiana University, Bloomington, 2019, https://scholarworks.iu.edu/dspace/items/0af0462b-d7ff-4ef4-98b1-7f93bb59fe32. (cited 4 times)
- J. B. Hough, M. Krishnapur, Y. Peres and B. Virag, Zeros of Gaussian Analytic Functions and Determinantal Point Processes, University Lecture Series 51, American Mathematical Society, Providence, RI, 2009, 10.1090/ulect/051. (cited 4 times)


### The variance of the typical cell of a hyperbolic Poisson--Voronoi tessellation at low intensity

Folder: [hyperbolic-voronoi-typical-cell-variance](public/hyperbolic-voronoi-typical-cell-variance) (source `public/hyperbolic-voronoi-typical-cell-variance/paper/main.tex`)

What the paper claims: Let $V_d(\lambda)$ be the variance of the volume of the typical cell of the Poisson--Voronoi tessellation of the hyperbolic space $\HH^d$ with intensity $\lambda$. D'Achille, Curien, Enriquez, Lyons and Unel asked whether $\lambda V_d(\lambda)$ has a finite limit as $\lambda\to0$, equal to the expected volume of $C_d\setminus T_d(R_1)$, where $C_d$ is the zero cell of the ideal Poisson--Voronoi tessellation and $T_d(R_1)$ the set coupled with it. We show that $\lambda V_d(\lambda)\to\infty$ for every $d\ge2$ and that the expected volume of $C_d\setminus T_d(R_1)$ is infinite, growing like $\theta_d\log U$ in the window $\{|u|<U\}$ of the upper half-space model, with $\theta_2=8/\pi$. The proof couples the typical cell inside the zero cell at positive intensity and passes to the limit with Fatou's lemma. In the plane, numerical values of $\lambda V_2(\lambda)$ down to $\lambda=10^{-5}$ fit $(8/\pi)\log(1/\lambda)-6.84$.

Most cited in the text:

- M. D'Achille, N. Curien, N. Enriquez, R. Lyons and M. Unel, Ideal Poisson--Voronoi tessellations on hyperbolic spaces, Ann. Probab. 54 (2026), no. 2, 846--891, 10.1214/25-AOP1781; 2303.16831. (cited 8 times)
- T. Budzinski, N. Curien and B. Petri, On Cheeger constants of hyperbolic surfaces, Invent. Math. 242 (2025), no. 2, 511--530, 10.1007/s00222-025-01361-w. (cited 1 time)
- M. D'Achille, Ideal Poisson--Voronoi tessellations beyond hyperbolic spaces, Electron. Commun. Probab. 31 (2026), 1--12, 10.1214/26-ECP815. (cited 1 time)
- M. D'Achille and C. Thale, Face volume densities of positive-intensity and ideal Poisson--Voronoi tessellations in hyperbolic spaces, 2606.26049, 2026. (cited 1 time)


### First-order coverage asymptotics for the inertial Boolean model

Folder: [inertial-boolean-coverage](public/inertial-boolean-coverage) (source `public/inertial-boolean-coverage/main.tex`)

What the paper claims: Points of a Poisson process of intensity $\lambda$ in $\R^d$ move along straight lines with independent velocities distributed as $V$, and each carries a closed ball of radius $r$. Konstantopoulos asked for the asymptotics of the first time $C(LK)$ at which the swept region contains the dilated compact set $LK$; the Brownian case is due to Peres, Sinclair, Sousi and Stauffer. Put $a=\lambda\omega_{d-1}r^{d-1}\E\abs{V}$, with $\omega_{d-1}$ the volume of the unit ball of $\R^{d-1}$. If $d\ge2$, $0<\E\abs V<\infty$ and $K$ has nonempty interior, then $C(LK)/\log L\to d/a$ almost surely and in $L^1$; for $K$ of Minkowski dimension $\alpha>1$ the limit is $\alpha/a$, in probability and in $L^1$. Under the tail condition $(\log h)\,\E[\abs{V}\ind_{\abs{V}>h}]\to0$ this holds for every $\alpha$ and every $d\ge1$. In dimension one the condition cannot be dropped: for one speed law with finite mean, $C([0,L])/\log\log L$ converges in law to an exponential variable.

Most cited in the text:

- T. Konstantopoulos, The mobile Boolean model: an overview and further results, arXiv:1407.6834, 2014. (cited 8 times)
- Y. Peres, A. Sinclair, P. Sousi and A. Stauffer, Mobile geometric graphs: detection, coverage and percolation, Probab. Theory Related Fields 156 (2013), 273--305; theorem numbers as in arXiv:1008.0075v2. (cited 8 times)
- S. Janson, Random coverings in several dimensions, Acta Math. 156 (1986), 83--118. (cited 6 times)
- P. Hall, Introduction to the Theory of Coverage Processes, Wiley, New York, 1988. (cited 5 times)


### A joint central limit theorem for inversions and two-sided descents

Folder: [inversions-two-sided-descents-clt](public/inversions-two-sided-descents-clt) (source `public/inversions-two-sided-descents-clt/paper/main.tex`)

What the paper claims: Let $\pi$ be a uniform random permutation of $n$ elements, let $I(\pi)$ be its number of inversions and let $T(\pi)=D(\pi)+D(\pi^{-1})$ be the number of descents of $\pi$ plus the number of descents of $\pi^{-1}$. We show that $I$ and $T$, centred and scaled by their standard deviations, converge jointly to a pair of independent standard normal variables, with the Wasserstein distance of every unit linear combination to the standard normal law at most a constant times $n^{-1/2}$. The same holds with $T$ replaced by any statistic that adds a fixed function over all windows of $k$ consecutive positions of $\pi$ and of $\pi^{-1}$, provided its variance grows linearly, and the triple $(I,D(\pi),D(\pi^{-1}))$, standardized in the same way, converges to a standard normal vector in $\mathbb R^3$. Exactly, $\Cov(I,T)=(n-1)/2$. The proof replaces $I$ by its Hoeffding projection on the point process that generates $\pi$ and applies Chatterjee's normal approximation by interaction graphs, as Chatterjee and Diaconis did for $T$ alone.

Most cited in the text:

- S. Chatterjee and P. Diaconis, A central limit theorem for a new statistic on permutations, Indian J. Pure Appl. Math. 48 (2017), 561--573, 1608.01666. (cited 7 times)
- S. Chatterjee, A new method of normal approximation, Ann. Probab. 36 (2008), 1584--1610, 10.1214/07-AOP370. (cited 3 times)
- P. Dörr, Joint asymptotic normality and extremes of generalized inversions and descents, preprint, 2024; version 5, 2026, 2404.06598. (cited 2 times)
- W. Hoeffding, A class of statistics with asymptotically normal distribution, Ann. Math. Statist. 19 (1948), 293--325, 10.1214/aoms/1177730196. (cited 2 times)


### The storage capacity of the Ising perceptron: verification of the outstanding numerical conditions

Folder: [ising-perceptron-capacity](public/ising-perceptron-capacity) (source `public/ising-perceptron-capacity/paper/main.tex`)

What the paper claims: Krauth and Mezard (1989) predicted that the maximum number of storable patterns in the Ising perceptron is $M_N=\alpha_\star N + o(N)$ for an explicit constant $\alpha_\star \approx 0.833$. Ding and Sun proved the matching lower bound, and Huang recently proved the matching upper bound; each result is conditional on an outstanding numerical hypothesis about an explicit low-dimensional variational problem. Their global sign clauses were supported by ordinary floating-point computations; Ding--Sun's final hypothesis also contains curvature and endpoint-derivative clauses. Huang separately used rigorous interval arithmetic for the other numerical inputs, but inherited the Ding--Sun parameter rectangle and left open the main Condition 1.3---the nonpositivity, over the whole plane, of a two-variable rate function with a degenerate point and slowly approaching tails. That unbounded optimization is the reason the capacity upper bound remained conditional. We verify both outstanding conditions in full. Reparametrizing Huang's functional into the moment coordinates of the pair $(X,\tanh X)$ compresses the plane onto a compact convex body and turns the entropy term into a per-cell linear function by convex duality; certified sweeps then establish nonpositivity on the whole body away from a star-shaped region around the distinguished degenerate point. On the star itself no box enclosure can work---the tilted covariance $\nabla^2\Phi$ is nearly singular and its inverse loses an essential cancellation---so we certify concavity of a majorant along rays from that point, bounding the entropy Hessian by a certified majorant of $\E[ff^\top\max_{b\in L}\operatorname{sech}^2(b\cdot f)]$ over sublevel-set localizations of the dual that are themselves certified by one-dimensional sweeps; no interval enclosure of the nearly singular covariance is inverted. The same machinery, in one variable, verifies the full Ding--Sun Condition 1.2, including its strict-curvature clause at the degenerate zero and its one-sided derivative clause at the singular endpoint, and we re-establish the parameter rectangle $(\alpha_\star, q_\star, \psi_\star)$ on which both papers rest. Together these close the stated conditional reduction for the Krauth--Mezard prediction.

Most cited in the text:

- J. Ding and N. Sun, Capacity lower bound for the Ising perceptron, Probab. Theory Related Fields 193 (2025), 627--715, https://doi.org/10.1007/s00440-025-01364-x; conference version STOC 2019; extended arXiv version arXiv:1809.07742. (cited 9 times)
- B. Huang, Capacity threshold for the Ising perceptron, FOCS 2024; arXiv:2404.18902. (cited 4 times)
- S. Nakajima and N. Sun, Sharp threshold sequence and universality for Ising perceptron models, SODA 2023; arXiv:2204.03469. (cited 2 times)
- E. Abbe, S. Li and A. Sly, Proof of the contiguity conjecture and lognormal limit for the symmetric perceptron, FOCS 2021; arXiv:2102.13069. (cited 1 time)


### The Ising perceptron at nonzero margin: certified bounds along the capacity curve

Folder: [ising-perceptron-margin](public/ising-perceptron-margin) (source `public/ising-perceptron-margin/paper/main.tex`)

What the paper claims: The storage capacity of the Ising perceptron at margin $\kappa$ is predicted by a replica-symmetric variational problem whose zero-margin instance, the Krauth--Mezard constant $\alpha_\star\approx 0.833$, was recently settled: Ding and Sun proved the lower bound, Huang proved the upper bound at general margin conditionally on four numerical hypotheses, and the zero-margin instances of those hypotheses have been verified in interval arithmetic. This paper moves the verified upper bound off the point $\kappa=0$. Two elementary identities make the general-margin system as tractable as the zero-margin one: the replica-symmetric free energy is stationary in both order parameters exactly at the fixed point, so on each certified branch rectangle the threshold $\alpha_\star(\kappa)$ is the unique root of a strictly decreasing function; and $\partial R/\partial q$ collapses to a one-term integral with positive integrand, a form of the general-margin monotonicity of Ding and Sun that interval arithmetic can consume directly. Building on these we verify, in ball arithmetic over sub-slabs of the margin axis, Huang's fixed-point, AMP, and local-concavity conditions on the strip $\kappa\in[-0.65,0.19]$ ($1680$ contiguous slabs across two uniqueness lanes, the second carrying per-slab thin-rectangle contractions and, independently, Nakajima's saddle theorem under a certified premise), with $\alpha_\star(\kappa)$ located to width $2\cdot10^{-6}$ at five margins and the local maximality of the first-moment functional at its degenerate maximizer certified at six. The remaining hypothesis, the global nonpositivity of Huang's two-variable rate function, we verify at all five margins by porting the zero-margin certificate architecture to located parameter boxes: the maximizer is kept symbolic through the base-point identity $\nabla\Phi(1,0)=(\psi_0(1-q_0),q_0)$, the dual localization is evaluated through a correlated Bregman integrand that collapses algebraically, and the far-tail kernels are stabilized by classical Mills-ratio bounds. At each of the five margins all four hypotheses hold, so Huang's theorem gives unconditional capacity upper bounds, for instance $\alpha_\star(0.05)\in[0.781073068,0.781074776]$ and $\alpha_\star(-0.45)\in[1.557652103,1.557654133]$. The verification code, certificates, and replay instructions are at https://github.com/yspennstate/ising-perceptron-margin. On the lower-bound side, open at every nonzero margin, we prove that unconditioned second moments fail at every margin (with a closure over nonnegative weights for $\kappa\ge0$), derive capacity lower bounds for all $\kappa<0$ by embedding a symmetric perceptron, and verify in floating point that the general-margin form of Ding--Sun's lower-bound condition holds at all five certified margins.

Most cited in the text:

- J. Ding and N. Sun, Capacity lower bound for the Ising perceptron, STOC 2019; arXiv:1809.07742. (cited 6 times)
- B. Huang, Capacity threshold for the Ising perceptron, FOCS 2024; arXiv:2404.18902. (cited 2 times)
- W. Krauth and M. Mezard, Storage capacity of memory networks with binary couplings, J. Physique 50 (1989), 3057--3066. (cited 2 times)
- S. Li, T. Schramm and K. Zhou, Discrepancy algorithms for the binary perceptron, arXiv:2408.00796. (cited 2 times)


### The Ising perceptron at nonzero margin: certified bounds along the capacity curve

Folder: [ising-perceptron-margin-work](public/ising-perceptron-margin-work) (source `public/ising-perceptron-margin-work/paper/main.tex`)

What the paper claims: The storage capacity of the Ising perceptron at margin $\kappa$ is predicted by a replica-symmetric variational problem whose zero-margin instance, the Krauth--Mezard constant $\alpha_\star\approx 0.833$, was recently settled: Ding and Sun proved the lower bound, Huang proved the upper bound at general margin conditionally on four numerical hypotheses, and the zero-margin instances of those hypotheses have been verified in interval arithmetic. This paper moves the verified upper bound off the point $\kappa=0$. Two elementary identities make the general-margin system as tractable as the zero-margin one: the replica-symmetric free energy is stationary in both order parameters exactly at the fixed point, so on each certified branch rectangle the threshold $\alpha_\star(\kappa)$ is the unique root of a strictly decreasing function; and $\partial R/\partial q$ collapses to a one-term integral with positive integrand, a form of the general-margin monotonicity of Ding and Sun that interval arithmetic can consume directly. Building on these we verify, in ball arithmetic over sub-slabs of the margin axis, Huang's fixed-point, AMP, and local-concavity conditions on the strip $\kappa\in[-1.05,0.19]$ ($2480$ contiguous slabs across three lanes: a full-rectangle lane, and past its measured walls on either side, located-box lanes --- the positive one carrying per-slab thin-rectangle contractions and, independently, Nakajima's saddle theorem under a certified premise), with $\alpha_\star(\kappa)$ located to width $2\cdot10^{-6}$ at twelve margins and the local maximality of the first-moment functional at its degenerate maximizer certified at six. The remaining hypothesis, the global nonpositivity of Huang's two-variable rate function, we verify at all twelve margins by porting the zero-margin certificate architecture to located parameter boxes: the maximizer is kept symbolic through the base-point identity $\nabla\Phi(1,0)=(\psi_0(1-q_0),q_0)$, the dual localization is evaluated through a correlated Bregman integrand that collapses algebraically, and the far-tail kernels are stabilized by classical Mills-ratio bounds. At each of the twelve margins all four hypotheses hold, so Huang's theorem gives unconditional capacity upper bounds, for instance $\alpha_\star(0.05)\in[0.781073067,0.781074777]$ and $\alpha_\star(-0.45)\in[1.557652103,1.557654134]$. The verification code, certificates, and replay instructions are at https://github.com/yspennstate/ising-perceptron-margin. On the lower-bound side, open at every nonzero margin, we prove that unconditioned second moments fail at every margin (with a closure over nonnegative weights for $\kappa\ge0$), derive capacity lower bounds for all $\kappa<0$ by embedding a symmetric perceptron, and verify in floating point that the general-margin form of Ding--Sun's lower-bound condition holds at five of the certified margins and at zero margin.

Most cited in the text:

- J. Ding and N. Sun, Capacity lower bound for the Ising perceptron, STOC 2019; arXiv:1809.07742. (cited 6 times)
- B. Huang, Capacity threshold for the Ising perceptron, FOCS 2024; arXiv:2404.18902. (cited 2 times)
- W. Krauth and M. Mezard, Storage capacity of memory networks with binary couplings, J. Physique 50 (1989), 3057--3066. (cited 2 times)
- S. Li, T. Schramm and K. Zhou, Discrepancy algorithms for the binary perceptron, arXiv:2408.00796. (cited 2 times)


### Rare observations under lattice-sum conditioning and joint allocation extremes

Folder: [joint-allocation-extremes](public/joint-allocation-extremes) (source `public/joint-allocation-extremes/paper/main.tex`)

What the paper claims: For independent lattice-valued observations with finite positive variance, conditioning the sum in a bounded central-limit window preserves the complete indexed record of any event whose probability tends to zero, in total variation. We prove a triangular-array version and a joint extension with an additional $o(n)$-coordinate sample under finitely many lattice constraints. Consequences include approximation of every $o(n)$ upper order statistics, Poisson approximation of all rare-value counts even when their total mean diverges, and ranked outdegree comparisons for Galton--Watson trees conditioned on size and a central leaf count. The allocation results answer Janson's fixed-rank question, including its moving-tilt and weak-centering formulations. Counterexamples show that a positive fraction of ranks can retain the sum constraint and that the fixed-tilt logarithmic centering scale cannot generally be enlarged.

Most cited in the text:

- S. Janson, Simply generated trees, conditioned Galton--Watson trees, random allocations and condensation, Probab. Surv. 9 (2012), 103--252. https://doi.org/10.1214/11-PS188doi:10.1214/11-PS188. Earlier version: https://arxiv.org/abs/1112.05 (cited 6 times)
- R. Arratia, L. Goldstein and L. Gordon, Poisson approximation and the Chen--Stein method, Statist. Sci. 5 (1990), no. 4, 403--434 (with discussion). (cited 3 times)
- R. Arratia and S. Tavare, Independent process approximations for random combinatorial structures, Adv. Math. 104 (1994), no. 1, 90--154. Author version: https://arxiv.org/abs/1308.3279arXiv:1308.3279. (cited 3 times)
- A. D. Barbour and P. Hall, On the rate of Poisson convergence, Math. Proc. Cambridge Philos. Soc. 95 (1984), no. 3, 473--480. https://doi.org/10.1017/S0305004100061806doi:10.1017/S0305004100061806. (cited 2 times)


### Stationary measures of planar kinetically constrained models with bounded conditional odds

Folder: [kcm-planar-stationary-bounded-odds](public/kcm-planar-stationary-bounded-odds) (source `public/kcm-planar-stationary-bounded-odds/paper/main.tex`)

What the paper claims: Martinelli, Shapira and Toninelli conjectured that every stationary measure of a kinetically constrained spin model on $\Z^d$ is a mixture of the equilibrium product measure conditioned on the fibers of bootstrap percolation. In dimension one, and for translation invariant stationary measures in every dimension, stationarity is known to imply detailed balance. We prove that on $\Z^2$ every stationary measure whose single-site conditional probabilities are bounded away from $0$ and $1$ satisfies detailed balance, without translation invariance and although the transition rates vanish on a large set. If large boxes are also internally spanned at every positive density, such a measure is the equilibrium product measure; this applies to the one- and two-neighbour Fredrickson--Andersen models at every density. The proof adapts the entropy argument of Holley and Stroock to degenerate rates, the hypothesis on the conditional probabilities replacing a lower bound on the rates. We also record the classification of all stationary measures of the one-neighbour model on strips $\Z\times H$ with $H$ finite.

Most cited in the text:

- F. Martinelli, A. Shapira and C. Toninelli, Long time behaviour of one facilitated kinetically constrained models: results and open problems, preprint, 2025. 2510.20461 (cited 10 times)
- M. Aizenman and J. L. Lebowitz, Metastability effects in bootstrap percolation, J. Phys. A 21 (1988), no. 19, 3801--3813. 10.1088/0305-4470/21/19/017 (cited 2 times)
- R. Holley and D. W. Stroock, In one and two dimensions, every stationary measure for a stochastic Ising model is a Gibbs state, Comm. Math. Phys. 55 (1977), no. 1, 37--45. 10.1007/BF01613147 (cited 2 times)
- I. Hartarsky and C. Toninelli, Kinetically Constrained Models, SpringerBriefs in Mathematical Physics, Springer, Cham, 2025. 10.1007/978-3-031-93115-4 (cited 2 times)


### Negative edge correlation for weighted spanning forests of complete graphs

Folder: [kn-forest-negative-correlation](public/kn-forest-negative-correlation) (source `public/kn-forest-negative-correlation/paper/forests_kn.tex`)

What the paper claims: Let $\Pt$ be the arboreal gas on the complete graph $K_n$: the probability measure on acyclic edge sets $F$ proportional to $t^{|F|}$. We prove that for every $n$ and every $t>0$ any two distinct edges $e,f$ satisfy $\Pt(e,f\in F)<\Pt(e\in F)\,\Pt(f\in F)$. The case $t=1$ is due to Gupta. For two edges sharing a vertex the inequality follows from the real-rootedness of the degree polynomial of a vertex, which is the characteristic polynomial of a rank-one perturbation of a Hermite Jacobi matrix. For disjoint edges the edge marginal satisfies an explicit Riccati equation, and the covariance is controlled by a barrier argument along it.

Most cited in the text:

- R. Bauerschmidt, N. Crawford, T. Helmuth and A. Swan, Random spanning forests and hyperbolic symmetry, Comm. Math. Phys. 381 (2021), 1223--1261. (cited 1 time)
- R. Burton and R. Pemantle, Local characteristics, entropy and limit theorems for spanning trees and domino tilings via transfer-impedances, Ann. Probab. 21 (1993), 1329--1371. (cited 1 time)
- Y. Cao and H. Fu, Negative edge correlation in complete bipartite graphs, arXiv:2610.36749, 2026. (cited 1 time)
- R. A. Ciceksiz and M. Ravichandran, Negative correlation for forests and the $q<1$ random-cluster model, arXiv:2610.00549, 2026. (cited 1 time)


### Toward the log-free law of robustness: a reduction to one multiplier estimate

Folder: [law-of-robustness-two-layer](public/law-of-robustness-two-layer) (source `public/law-of-robustness-two-layer/supplement.tex`)

What the paper claims: This note accompanies the paper ``A law of robustness for two-layer neural networks with arbitrary weights''. It develops the reduction of the log-free Bubeck--Li--Nagaraj conjecture, in the critical band of widths, to a single multiplier estimate, and proves the unconditional structure surrounding that estimate, including the single-direction case for every Lipschitz activation. The estimate itself remains open.

Most cited in the text:

- R. Vershynin. High-Dimensional Probability: An Introduction with Applications in Data Science. Cambridge Series in Statistical and Probabilistic Mathematics, vol. 47, Cambridge University Press, Cambridge, 2018. DOI: 10.1017/9781108231596. (cited 3 times)
- S. Bubeck, Y. Li, and D. M. Nagaraj. A law of robustness for two-layers neural networks. In Proceedings of the 34th Conference on Learning Theory, Proceedings of Machine Learning Research, vol. 134, pp. 804--820, PMLR, 2021. arXiv:2009.1444 (cited 2 times)
- S. Bubeck and M. Sellke. A universal law of robustness via isoperimetry. J. ACM 70 (2023), no. 2, Art. 10. Conference version in Advances in Neural Information Processing Systems 34 (2021). arXiv:2105.12806. (cited 1 time)


### Moments of level widths in conditioned Galton--Watson trees

Folder: [level-width-moments](public/level-width-moments) (source `public/level-width-moments/paper/main.tex`)

What the paper claims: Let $T_n$ be a simply generated random tree with $n$ vertices, for instance a conditioned Galton--Watson tree, and let $l_k(T_n)$ be the number of vertices at distance $k$ from the root. Janson conjectured that, when the generating function of the weights has a positive radius of convergence, $\E\, l_k(T_n)^r\to\E\, l_k(\hT)^r\le\infty$ for all integers $r\ge1$ and $k\ge1$, where $\hT$ is the local limit of $T_n$, and that the same holds for non-integer $r>0$. We show that if the offspring distribution is critical and has a finite moment of order $r+1$ for a real number $r\ge1$, then the random variables $l_k(T_n)^r$, $n\ge1$, are uniformly integrable for every $k$, and $\E\, l_k(T_n)^r\to\E Z_k^{r+1}$, where $Z_k$ is the size of generation $k$ of the unconditioned Galton--Watson process. Together with the cases that follow from Fatou's lemma, this proves the conjecture for every integer $r\ge1$, and for every real $r>0$ except in the case where $0<r<1$ and the offspring distribution is critical with infinite variance and a finite moment of order $r+1$. The proof bounds the density of the law of the first $k$ generations of $T_n$ with respect to that of the unconditioned tree by means of the local limit theorem.

Most cited in the text:

- S. Janson, Simply generated trees, conditioned Galton--Watson trees, random allocations and condensation, Probab. Surv. 9 (2012), 103--252. (cited 15 times)
- S. Janson, Random cutting and records in deterministic and random trees, Random Structures Algorithms 29 (2006), no. 2, 139--179. (cited 4 times)
- R. Abraham and J.-F. Delmas, Local limits of conditioned Galton--Watson trees: the infinite spine case, Electron. J. Probab. 19 (2014), no. 2, 1--19. (cited 1 time)
- L. Addario-Berry, L. Devroye and S. Janson, Sub-Gaussian tail bounds for the width and height of conditioned Galton--Watson trees, Ann. Probab. 41 (2013), no. 2, 1072--1087. (cited 1 time)


### A Levy random drift destroys compactness for every confining power

Folder: [levy-drift-noncompact](public/levy-drift-noncompact) (source `public/levy-drift-noncompact/paper/main.tex`)

What the paper claims: Let $V$ be a two-sided semi-selfsimilar Levy process of index $\alpha\in(0,2)$ on $\R$ and let $L^{w+V}=\frac12(\Delta-\nabla(w+V)\cdot\nabla)$ act on $L^2(\R;e^{-(w+V)}\,dx)$. For $w_1=|x|^\delta$ and $w_2=-|x|^\delta$ the unperturbed semigroups are compact exactly when $\delta>1$. Shiozawa and Wang proved that the perturbed semigroups are noncompact, with bottom of the essential spectrum equal to $0$, when $\delta\le 1/\alpha$, and asked what happens when $\delta>1/\alpha$. We show that for $\delta>1/\alpha$ the bottom of the essential spectrum of $-L^{w_1+V}$ is $0$ almost surely as soon as the Levy measure of $V$ on one of the two half-lines charges $(-\infty,0)$, and that the same holds for $-L^{w_2+V}$ as soon as one of them charges $(0,\infty)$. In particular, when $V$ changes sign and either $\alpha<1$ or the jumps of $V$ go both ways, both semigroups are noncompact for every $\delta>0$. The mechanism is local: a jump of size $m$ at distance $\tau$ from the origin lowers a Rayleigh quotient by a factor $e^{-m/2}$, while the confining power costs only a factor $\tau^{2\delta-2}$, and an $\alpha$-semi-selfsimilar process has jumps of size of order $\tau^{1/\alpha}$ at every scale.

Most cited in the text:

- Y. Shiozawa and J. Wang, Essential spectrum for Brox-type diffusion processes, arXiv:2607.07410 (2026). (cited 9 times)
- K. Sato, Levy Processes and Infinitely Divisible Distributions, Cambridge Studies in Advanced Mathematics 68, Cambridge University Press, Cambridge, 1999. (cited 4 times)
- T. Brox, A one-dimensional diffusion process in a Wiener medium, Ann. Probab. 14 (1986), 1206--1218. (cited 1 time)
- M. Maejima and K. Sato, Semi-selfsimilar processes, J. Theoret. Probab. 12 (1999), 347--373. (cited 1 time)


### Sharp relaxation, cutoff, and graph diffusion for a linear-polymer chain

Folder: [linear-polymer-relaxation](public/linear-polymer-relaxation) (source `public/linear-polymer-relaxation/paper/main.tex`)

What the paper claims: Consider the finite linear-polymer chain in which each pair of clusters merges at rate $2/n$ and each internal link breaks at rate $\beta$. We give a direct proof that its spectral gap equals the gap of the cluster-count chain, an equality announced by Granovsky and Erlihson, and prove the uniform estimate $\sqrt{\beta^2+4\beta}-5/n\le\gamma_M\le \sqrt{\beta^2+4\beta}+4/n$. Together with an all-parameter comparison and a critical scaling function at $\beta\asymp n^{-2}$, this determines the relaxation asymptotics throughout the parameter range. For $\beta=b/n$, the cluster-count chain has total-variation cutoff at $\sqrt n\log n/(8\sqrt b)$ with a window of order at most $\sqrt n$. The same cutoff holds for the polymer chain started from one polymer or from all monomers. From arbitrary polymer configurations we prove a total-variation mixing bound of order $\sqrt n(\log n)^2$. Adding exclusion diffusion on any connected weighted graph gives the exact gap $\min\{\gamma_M,\eta_1+D\lambda_G\}$, where $\lambda_G$ is the one-particle graph gap and $\eta_1$ is a one-dimensional reaction eigenvalue for which we give uniform and sharp estimates. We also treat bounded inhomogeneous reactions, conservative nonreversible cut motion, and a stationary circulation that strictly accelerates the original polymer chain. The proofs use the stationary cycle representation, Boolean harmonic decomposition, positive eigenfunction comparisons, and hitting-time estimates.

Most cited in the text:

- Chen, Guan-Yu and Saloff-Coste, Laurent, Computing cutoff times of birth and death chains (2015) (cited 3 times)
- Granovsky, Boris L. and Erlihson, Michael M., On Time Dynamics of Coagulation-Fragmentation Processes (2009) (cited 3 times)
- Aldous, David, A special aggregation-fragmentation process (n.d.) (cited 2 times)
- Chafai, Djalil and Joulin, Alderic, Intertwining and commutation relations for birth--death processes (2013) (cited 2 times)


### An upper bound to second order for the longest minimum-weight path in a complete graph

Folder: [longest-geodesic-complete-graph](public/longest-geodesic-complete-graph) (source `public/longest-geodesic-complete-graph/longest_geodesic.tex`)

What the paper claims: Give the edges of the complete graph on $n$ vertices independent exponential weights and let $M_n$ be the largest number of edges of a minimum-weight path between two vertices. Addario-Berry, Broutin and Lugosi proved that $M_n/\log n\to\as$ in probability, where $\as\approx3.5911$ solves $\as\log\as-\as=1$, with the bounds $\as\log n-L\log\log n\le M_n\le\as\log n+\omega(n)$. We prove that $\Prob(M_n\ge b_n+x)\le C\as^{-x}$ for all $x\ge0$, where $b_n=\as\log n-(\log\log n)/(2\log\as)$. Hence $M_n-\as\log n\to-\infty$ in probability and $\E M_n\le b_n+O(1)$. We also find the asymptotic value of the expected number of pairs of vertices joined by a minimum-weight path of at least $k$ edges when $k=\as\log n+O(\log\log n)$, show that at $k=\lceil b_n\rceil$ the second moment of this number tends to infinity although its mean stays bounded, and prove that $\Prob(M_n=n-1)=n/(2\,(n-1)!)$ for every $n\ge2$. The lower side of the question of van der Hofstad on the fluctuations of $M_n$ stays open.

Most cited in the text:

- L. Addario-Berry, N. Broutin and G. Lugosi, The longest minimum-weight path in a complete graph, Combin. Probab. Comput. 19 (2010), 1--19. https://doi.org/10.1017/S0963548309990204doi:10.1017/S0963548309990204 (cited 4 times)
- L. Addario-Berry and K. Ford, Poisson--Dirichlet branching random walks, Ann. Appl. Probab. 23 (2013), 283--307. https://doi.org/10.1214/12-AAP840doi:10.1214/12-AAP840 (cited 3 times)
- X. Chen and H. Ma, Atypical decay rates for atypical heights in random recursive trees, preprint, 2026. https://arxiv.org/abs/2604.20139arXiv:2604.20139 (cited 3 times)
- R. T. Smythe and H. M. Mahmoud, A survey of recursive trees, Theory Probab. Math. Statist. 51 (1995), 1--27. (cited 3 times)


### A non-geodesic edge that survives in the loop-erased ant process

Folder: [loop-erased-ants-non-geodesic-edge](public/loop-erased-ants-non-geodesic-edge) (source `public/loop-erased-ants-non-geodesic-edge/loop_erased_ants.tex`)

What the paper claims: In the loop-erased ant process of Kious, Mailler and Schapira, ants walk one after another from a nest $N$ to a food source $F$ on a finite graph, each ant stepping along an edge with probability proportional to its weight and then adding one to the weight of every edge of the loop-erasure of its time-reversed trajectory. It was conjectured that the weight of an edge grows linearly exactly when the edge lies on a geodesic from $N$ to $F$. Let $G_\ell$ be the graph made of a triangle $N,u,v$ and two paths of $\ell$ edges, one from $u$ to $F$ and one from $v$ to $F$. We prove that on $G_\ell$ the normalised weights converge almost surely. The limit is $\rho$ on the edges of the path $N,u,\dots,F$, it is $1-\rho$ on the edges of the path $N,v,\dots,F$, and it is $(1-1/\ell)\rho(1-\rho)$ on the edge $uv$, where $\rho$ is a non-degenerate random variable with values in $(0,1)$. For $\ell\ge2$ the edge $uv$ lies on no geodesic and keeps a positive share of the weight, so the conjecture fails on $G_\ell$, and the proportion of ants that reinforce a path which is not a geodesic has a positive limit. For $\ell=1$ the graph is the losange of Kious, Mailler and Schapira, the edge $uv$ dies, and the theorem gives for the loop-erased rule the convergence that they proved for the uniform-geodesic rule. The forward-loop-erased ant process of Armfield and Mailler, in which the ant reinforces the loop-erasure of its trajectory instead of that of the reversed trajectory, has the same law, so all of these statements hold for it as well.

Most cited in the text:

- W. Armfield and C. Mailler, The forward-loop-erased ants walk, arXiv:2610.18453. (cited 7 times)
- D. Kious, C. Mailler and B. Schapira, Finding geodesics on graphs using reinforcement learning, Ann. Appl. Probab. 32 (2022), no. 5, 3889--3929; arXiv:2010.04820. (cited 6 times)
- R. Lyons and Y. Peres, Probability on Trees and Networks, Cambridge University Press, 2016. (cited 2 times)
- D. B. Wilson, Generating random spanning trees more quickly than the cover time, in Proceedings of the Twenty-eighth Annual ACM Symposium on the Theory of Computing, ACM, 1996, 296--303. (cited 2 times)


### Lumping and the mixing time of a reversible chain: the dependence on the number of states

Folder: [lumping-mixing-time](public/lumping-mixing-time) (source `public/lumping-mixing-time/lumping.tex`)

What the paper claims: Aldous and Fill asked whether the stopping-rule mixing time $\tmix$ of a chain obtained from a reversible Markov chain by lumping states is at most an absolute constant times that of the original chain. Hermon and Peres answered the question in the negative: for random walks on graphs of bounded degree, lumping can increase the mixing time by a factor of the order of the logarithm of the number of vertices, and by no more. We consider general reversible chains with $n$ states and show that the largest possible factor $K(n)$ satisfies $\lfloor (n-2)/2\rfloor\le K(n)\le n-1$. The upper bound follows from standard inequalities and from the inequality $\tau_2\le\tmix$ between the relaxation time and the stopping-rule mixing time, for which we give a short proof; the lower bound comes from an explicit random walk on a weighted comb. We also show that lumping increases the mean hitting time of a set $A$ by a factor of at most $n-|A|$, and that this bound cannot be improved by more than a factor of about two.

Most cited in the text:

- D. Aldous and J. A. Fill, Reversible Markov Chains and Random Walks on Graphs, unfinished monograph, 2002, recompiled 2014, https://www.stat.berkeley.edu/ aldous/RWG/book.html. (cited 13 times)
- J. Hermon and Y. Peres, On sensitivity of mixing times and cutoff, Electron. J. Probab. 23 (2018), paper no. 25, 1--34. https://doi.org/10.1214/18-EJP154doi:10.1214/18-EJP154; arXiv:1610.04357. (cited 5 times)
- D. J. Aldous, Some inequalities for reversible Markov chains, J. London Math. Soc. (2) 25 (1982), 564--576. https://doi.org/10.1112/jlms/s2-25.3.564doi:10.1112/jlms/s2-25.3.564. (cited 2 times)
- R. Lyons and Y. Peres, Probability on Trees and Networks, Cambridge Series in Statistical and Probabilistic Mathematics 42, Cambridge University Press, New York, 2016. https://doi.org/10.1017/9781316672815doi:10.1017/9781316672815. (cited 2 times)


### Maximal flow through thin boxes with heavy-tailed capacities

Folder: [maxflow-thin-boxes](public/maxflow-thin-boxes) (source `public/maxflow-thin-boxes/paper/main.tex`)

What the paper claims: Kesten's law of large numbers for the maximal flow $\Phi$ from the bottom to the top of a box $[0,k]\times[0,l]\times[0,m]$ in $\Z^3$ with i.i.d. capacities assumes a finite exponential moment, and Auffinger, Damron and Hanson ask whether the limit of $\Phi/(kl)$ exists without it. We show that without a replacement moment condition it need not. For every height function $m(N)$ with $\liminf m(N)/\log N=0$ there is a capacity law with no atom at $0$ such that $\limsup\Phi/N^{d-1}=+\infty$ almost surely in the boxes $[0,N]^{d-1}\times[0,m(N)]$ of $\Z^d$, $d\ge2$. The heights may tend to infinity, for instance as $(\log N)^{1/2}$, and so lie inside Kesten's range. For heights with $m(N)/\log N\to\infty$, Rossignol and Theret proved convergence to a finite flow constant for every capacity law; for the laws constructed here the limit therefore depends on how fast the height grows.

Most cited in the text:

- R. Rossignol and M. Theret, Existence and continuity of the flow constant in first passage percolation, Electron. J. Probab. 23 (2018), paper no. 99; arXiv:1707.08766. (cited 3 times)
- H. Kesten, Surfaces with minimal random weights and maximal flows: a higher dimensional version of first-passage percolation, Illinois J. Math. 31 (1987), 99--166. (cited 2 times)
- Y. Zhang, Limit theorems for maximum flows on a lattice, Probab. Theory Related Fields 171 (2018), 149--202; arXiv:0710.4589. (cited 2 times)
- A. Auffinger, M. Damron and J. Hanson, 50 Years of First-Passage Percolation, University Lecture Series 68, American Mathematical Society, Providence, RI, 2017; arXiv:1511.03262. (cited 1 time)


### The maximal Kemeny constant of an $n$-vertex graph

Folder: [maximal-kemeny-constant](public/maximal-kemeny-constant) (source `public/maximal-kemeny-constant/paper/main.tex`)

What the paper claims: For simple random walk on a connected simple graph with $n$ vertices, Kemeny's constant is at most $n^3/54+\frac{37}{8}n^{5/2}$. Balanced barbells show that the leading term is sharp, so the maximum of Kemeny's constant over such graphs is asymptotic to $n^3/54$. This proves the Kemeny-constant assertion of Aldous--Fill Open Problem 6.13. Since the relaxation time never exceeds Kemeny's constant, the same bound gives the relaxation-time assertion of that problem, which was proved by Aksoy, Chung, Tait and Tobin. The proof is elementary. It combines the effective-resistance formula for Kemeny's constant with a contraction of the neighbourhoods of high-degree vertices and a two-mass inequality on the edges of a spanning tree. The same argument shows that among $K_{r+1}$-free graphs, and among graphs of chromatic number at most $r$, both maxima equal $(1-1/r)n^3/54+O(n^{5/2})$. In particular the triangle-free and the bipartite constants are $1/108$.

Most cited in the text:

- D. Aldous and J. A. Fill, Reversible Markov Chains and Random Walks on Graphs, unfinished monograph, 2002; recompiled 2014. https://www.stat.berkeley.edu/ aldous/RWG/book.html. (cited 2 times)
- S. G. Aksoy, F. Chung, M. Tait and J. Tobin, The maximum relaxation time of a random walk, Adv. in Appl. Math. 101 (2018), 1--14. https://doi.org/10.1016/j.aam.2018.07.002doi:10.1016/j.aam.2018.07.002. (cited 1 time)
- J. Breen, S. Butler, N. Day, C. DeArmond, K. Lorenzen, H. Qian and J. Riesen, Computing Kemeny's constant for a barbell graph, Electron. J. Linear Algebra 35 (2019), 583--598. https://doi.org/10.13001/ela.2019.5175doi:10.13001/ela.2019.5175 (cited 1 time)
- N. Faught, M. Kempton and A. Knudson, A 1-separation formula for the graph Kemeny constant and Braess edges, J. Math. Chem. 60 (2022), 49--69. https://doi.org/10.1007/s10910-021-01294-8doi:10.1007/s10910-021-01294-8. (cited 1 time)


### The time-stationary and Palm inter-arrival times of a Markov-modulated Poisson process need not be ordered

Folder: [mmpp-stationary-order](public/mmpp-stationary-order) (source `public/mmpp-stationary-order/paper/main.tex`)

What the paper claims: For an irreducible Markov-modulated Poisson process, let $T^\pi$ be the time from a stationary instant to the next arrival and $T^\alpha$ the time from an arrival to the next one in the event-stationary version. Asanjarani and Nazarathy conjectured that $T^\pi$ is stochastically larger than $T^\alpha$, and He listed the same property among open questions on the MMPP class of phase-type distributions. The conjecture is false. The order is equivalent to the hazard rate of $T^\pi$ never exceeding the arrival rate. For a Cox process driven by a non-constant periodic intensity with uniform phase this fails on a set of positive measure. For the MMPP on the directed $n$-cycle with arrival rates $\varepsilon(1+b\cos(2\pi j/n))$ it fails for all small $\varepsilon>0$ whenever $n\ge 12$, and an explicit twelve-state MMPP with positive rational rates has $\Pp(T^\pi>19/2)-\Pp(T^\alpha>19/2)<-1/300000$, proved in exact rational arithmetic. For reversible modulators the order holds. We also show that the mean of He's MMPP-type distribution need not be convex in the speed of modulation.

Most cited in the text:

- Q.-M. He, Bounds on the mean and squared coefficient of variation of phase-type distributions, J. Appl. Probab. 58 (2021), 880--889. (cited 7 times)
- A. Asanjarani and Y. Nazarathy, Stationary Markovian arrival processes: results and open problems, ANZIAM J. 64 (2022), 54--68. (cited 6 times)
- A. Asanjarani and Y. Nazarathy, The squared coefficient of variation for MMPP is greater than unity, arXiv:1802.08400v1 (2018), withdrawn. (cited 1 time)
- A. Asanjarani and Y. Nazarathy, Stationary Markovian arrival processes, results and open problems, arXiv:1905.01736 (2019). (cited 1 time)


### Polynomial components in spectrally subcritical percolation on near-regular graphs

Folder: [near-regular-percolation-components](public/near-regular-percolation-components) (source `public/near-regular-percolation-components/paper/main.tex`)

What the paper claims: Let $G$ be a finite graph with spectral radius $\lambda$ and maximum degree $\Delta$, and keep each edge independently with probability $p=(1-\varepsilon)/\lambda$. Christoph, Morawski and Wigderson asked for the typical size of the largest component in this regime, singling out graphs that are close to regular in the sense $\Delta\le(1+\delta)\lambda$. We show that the answer depends on the product $(1-\varepsilon)(1+\delta)$. When it is less than one, a known maximum-degree argument gives components of logarithmic order. When it is greater than one, there are connected graphs with $\Delta\le(1+\delta)\lambda$ whose largest component has at least $n^c$ vertices with high probability, for a constant $c>0$, and the spectral radius can be taken of order $n^a$ for any $0\le a<1$. When it equals one, the largest component has $O((\log n)^3)$ vertices with high probability. We also sharpen the resolvent bound of Christoph, Morawski and Wigderson for graphs with bounded ratio $\Delta/\lambda$. The optimal order in the polynomial regime remains open.

Most cited in the text:

- M. Christoph, P. Morawski and Y. Wigderson, The critical probability for percolation on finite graphs, preprint (2026), 2608.19145. (cited 5 times)
- B. Bollobás, C. Borgs, J. Chayes and O. Riordan, Percolation on dense graph sequences, Ann. Probab. 38 (2010), no. 1, 150--183. 10.1214/09-AOP478 (cited 2 times)
- N. Alon, I. Benjamini and A. Stacey, Percolation on finite graphs and isoperimetric inequalities, Ann. Probab. 32 (2004), no. 3, 1727--1745. 10.1214/009117904000000414 (cited 1 time)
- S. Diskin, J. Erde, M. Kang and M. Krivelevich, Percolation on high-dimensional product graphs, Random Structures Algorithms 66 (2025), no. 1, e21268. 10.1002/rsa.21268; 2209.03722. (cited 1 time)


### Neural Means and Kernel Corrections for Operator Learning

Folder: [neural-means-kernel-corrections](public/neural-means-kernel-corrections) (source `public/neural-means-kernel-corrections/paper/main.tex`)

What the paper claims: Kernel regression can fit prediction residuals or regress targets on learned features after neural training. We compare these two approaches on structural-mechanics and OCO-2 benchmarks, using ten random seeds for the main experiments. On structural mechanics, a corrected six-member stack reaches $\errSix\pm\errSixSd\%$ mean relative test error, close to PARA-Net's published $\pubBestHi\%$. With 1250 labels, the pipeline reaches $\errBestLow\pm\errBestLowSd\%$ against a published $\pubBestLo\%$. An analysis of sixty trained predictors shows limited scope for further improvement by global convex averaging within this pool: an empirical RMS lower bound of $\saBound\%$ is close to the hindsight optimum of $\saSixtyOracleRms\%$. On the O2 band, Matern regression on raw inputs has approximately $40\%$ relative error in the reduced coordinates, compared with $4.1\%$ on frozen neural features. Coordinatewise selection gives lower ten-seed mean errors than the source emulator's stored predictions on all three bands under both criteria evaluated on the retained representation. Full-spectrum and retrieval accuracy are not evaluated. The analysis combines ensemble identities with conditional native-space error bounds. For uncertainty quantification, a constant-radius conformal set is narrower on average than a set scaled by the kernel power function.

Most cited in the text:

- de Hoop, Maarten V. and Huang, Daniel Zhengyu and Qian, Elizabeth and Stuart, Andrew M., The cost-accuracy trade-off in operator learning with neural networks (2022) (cited 10 times)
- Mora, Carlos and Yousefpour, Amin and Hosseinmardi, Shirin and Owhadi, Houman and Bostanabad, Ramin, Operator learning with Gaussian processes (2025) (cited 10 times)
- Batlle, Pau and Darcy, Matthieu and Hosseini, Bamdad and Owhadi, Houman, Kernel methods are competitive for operator learning (2024) (cited 9 times)
- Lamminpaa, Otto and Susiluoto, Jouni and Hobbs, Jonathan and McDuffie, James and Braverman, Amy and Owhadi, Houman, Forward model emulator for atmospheric radiative transfer using Gaussian processes and cross validation  (cited 5 times)


### Non-Gaussian fluctuations of degree counts in conditioned Galton--Watson trees

Folder: [non-gaussian-degree-counts](public/non-gaussian-degree-counts) (source `public/non-gaussian-degree-counts/paper/degree_counts.tex`)

What the paper claims: Let $T_n$ be a Galton--Watson tree conditioned to have $n$ vertices and let $N_A(T_n)$ be the number of its vertices whose outdegree lies in $A$. Thevenin conjectured that $(N_A(T_n)-n\mu_A)/\sqrt n$ is asymptotically normal with variance $\mu_A(1-\mu_A)$ for every subcritical offspring law $\mu$ without exponential moment and every critical law with infinite variance. We show that the conjecture fails for an explicit subcritical law with finite third moment and for a critical law with infinite variance: along a sequence of sizes the normalised number of vertices of outdegree one converges to an equal mixture of two Gaussian laws with different means. For the subcritical law the same holds for every set $A$ with $0<\mu_A<1$, in particular for the number of leaves. We also prove a joint central limit theorem for the box counts of balls-in-boxes models when the limiting density of balls is below the critical density, and at the critical density under a second moment condition when the number of balls exceeds its critical value by at most $O(\sqrt n)$. These results answer parts of Problems 21.2--21.4 in Janson's survey of simply generated trees.

Most cited in the text:

- S. Janson, Simply generated trees, conditioned Galton--Watson trees, random allocations and condensation, Probab. Surv. 9 (2012), 103--252. (cited 17 times)
- P. Thevenin, Vertices with fixed outdegrees in large Galton--Watson trees, Electron. J. Probab. 25 (2020), paper no. 64, 25 pp.; arXiv:1812.07365. (cited 6 times)
- S. Janson, Asymptotic normality of fringe subtrees and additive functionals in conditioned Galton--Watson trees, Random Structures Algorithms 48 (2016), 57--101. (cited 5 times)
- S. Janson, Moment convergence in conditional limit theorems, J. Appl. Probab. 38 (2001), 421--437. (cited 3 times)


### A birthday bound for non-backtracking walks on graphs of bounded degree ratio

Folder: [nonbacktracking-birthday-irregular](public/nonbacktracking-birthday-irregular) (source `public/nonbacktracking-birthday-irregular/paper/main.tex`)

What the paper claims: Let $G$ be a finite simple graph on $n$ vertices with minimum degree $m\ge3$ and maximum degree $M$, and put $Q=M/(m-1)$. A non-backtracking random walk of length $k$ on $G$, started along any directed edge, is vertex-simple with probability at most $256\,Q(1+Q)\,n/k^2$. Hence the conjecture of Alon and Peres, that a non-backtracking walk of length $C(\varepsilon)\sqrt n$ self-intersects with probability at least $1-\varepsilon$, holds with $C(\varepsilon)$ depending only on $\varepsilon$ and a bound for $M/m$; for regular graphs of degree at least three one may take $C(\varepsilon)=31\varepsilon^{-1/2}$ for every degree. The expected self-intersection time is at most $32\sqrt{Q(1+Q)n}+2$, which removes the logarithmic factor from the bound of Bencs et al. for graphs of minimum degree at least three and bounded maximum degree. The proof adapts Dozier's argument for regular graphs: departures are weighted by the inverse branching at their vertex, and the deviating local derangement is resampled.

Most cited in the text:

- F. Bencs, L. A. Goldberg, M. Jenssen, M. Jerrum, G. Pete, G. Regts and Y. Yin, On the self-intersection time of non-backtracking random walks, preprint, 2026, https://arxiv.org/abs/2608.09729arXiv:2608.09729. (cited 12 times)
- B. Dozier, The birthday paradox for non-backtracking walks on regular graphs, preprint, 2026, https://arxiv.org/abs/2608.26321arXiv:2608.26321. (cited 4 times)
- N. Alon, I. Benjamini, E. Lubetzky and S. Sodin, Non-backtracking random walks mix faster, Commun. Contemp. Math. 9 (2007), no. 4, 585--603. 10.1142/S0219199707002551 (cited 1 time)
- J. H. Kim, R. Montenegro, Y. Peres and P. Tetali, A birthday paradox for Markov chains with an optimal bound for collision in the Pollard rho algorithm for discrete logarithm, Ann. Appl. Probab. 20 (2010), no. 2, 495--521. 10.1214/09-AAP625 (cited 1 time)


### A nonergodic flow rule with Galton--Watson stationary measure

Folder: [nonergodic-galton-watson-flow-rule](public/nonergodic-galton-watson-flow-rule) (source `public/nonergodic-galton-watson-flow-rule/paper/main.tex`)

What the paper claims: A flow rule assigns to every infinite rooted tree a unit flow from the root to infinity, consistently with passage to the subtrees of the children of the root, and it defines a Markov chain on the space of trees that moves from a tree to the subtree of a child chosen according to the flow. Lyons, Pemantle and Peres showed that the chain is ergodic when a stationary measure absolutely continuous with respect to a Galton--Watson measure $\GW$ exists and the flow is positive on every child, and asked whether a flow rule with a stationary measure equivalent to $\GW$ must give an ergodic chain. It need not. For the Galton--Watson measure with offspring distribution $p_2=3/5$, $p_3=2/5$ there is a flow rule for which $\GW$ itself is stationary and the stationary chain has an invariant event of probability $1/2$. The rule follows a colouring of the vertices that is a measurable function of the tree, in which a vertex with two children takes the AND of their colours and a vertex with three children the OR: the flow is spread evenly over the children that have the colour of the root. The two colour classes give the ergodic decomposition of the chain.

Most cited in the text:

- R. Lyons and Y. Peres, Probability on Trees and Networks, Cambridge Series in Statistical and Probabilistic Mathematics 42, Cambridge University Press, New York, 2016. Numbering as in the corrected and updated paperback edition, version of  (cited 10 times)
- T. Johnson, M. Podder and F. Skerman, Random tree recursions: which fixed points correspond to tangible sets of trees?, Random Structures Algorithms 56 (2020), 796--837. (cited 3 times)
- R. Lyons, R. Pemantle and Y. Peres, Ergodic theory on Galton--Watson trees: speed of random walk and dimension of harmonic measure, Ergodic Theory Dynam. Systems 15 (1995), 593--619. (cited 3 times)
- D. J. Aldous and A. Bandyopadhyay, A survey of max-type recursive distributional equations, Ann. Appl. Probab. 15 (2005), 1047--1110. (cited 1 time)


### Non-normal orbit quotients that are not normal quotients

Folder: [nonnormal-orbit-quotients](public/nonnormal-orbit-quotients) (source `public/nonnormal-orbit-quotients/paper/main.tex`)

What the paper claims: Let $G$ be an infinite transitive graph, $\Gamma\le\Aut(G)$ a transitive group and $A\le\Gamma$ a subgroup. Grimmett and Li asked whether $A$ can be non-normal in $\Gamma$ with a transitive orbit quotient $G_A$ that is not isomorphic to $G_N$ for any normal subgroup $N$ of any transitive $\Gamma'\le\Aut(G)$, and whether a free action of $A$ matters. We show that for every $m\ge3$ there is an infinite, connected, locally finite, simple Cayley graph $X$ with a non-normal subgroup $B$ of $\Aut(X)$, acting freely, such that $X_B$ is the complete graph $K_m$, while no normal subgroup of any transitive subgroup of $\Aut(X)$ has $K_m$ as its orbit quotient. The graph is a graphical regular representation of the free product $F*F$, where $F$ is $S_3$ for $m=3$ and the alternating group $A_m$ for $m\ge4$, given by the theorem of Leemann and de la Salle, and $B$ is the preimage of a point stabiliser under the projection to the first factor. The quotient is finite; the question with an infinite quotient is left open.

Most cited in the text:

- G. R. Grimmett and Z. Li, Self-avoiding walks and connective constants, in: Sojourns in Probability Theory and Statistical Physics -- III, Springer Proc. Math. Stat. 300, Springer, Singapore, 2019, pp. 215--241; arXiv:1704.05884v2. (cited 4 times)
- P.-H. Leemann and M. de la Salle, Cayley graphs with few automorphisms: the case of infinite groups, Ann. H. Lebesgue 5 (2022), 73--92; arXiv:2010.06020. (cited 4 times)
- L. Babai, Infinite digraphs with given regular automorphism groups, J. Combin. Theory Ser. B 25 (1978), 26--46. (cited 1 time)
- G. R. Grimmett and Z. Li, Strict inequalities for connective constants of transitive graphs, SIAM J. Discrete Math. 28 (2014), 1306--1333; arXiv:1301.3091. (cited 1 time)


### The smallest eigenvalue of the neural tangent kernel of a deep tanh network in the ordered phase

Folder: [ntk-smallest-eigenvalue-ordered-phase](public/ntk-smallest-eigenvalue-ordered-phase) (source `public/ntk-smallest-eigenvalue-ordered-phase/paper/t249.tex`)

What the paper claims: For a fully connected tanh network of depth $L$ in the infinite-width limit, with weight variance $\sigma_w^2$ and bias variance $\sigma_b^2>0$ in the ordered phase $\chi_1<1$, we determine the smallest eigenvalue of the neural tangent kernel Gram matrix on $n$ distinct inputs of the sphere. It equals $L\chi_1^L\,(q^*+B\,T^*/\chi_1)\,\lambda_{\min}^{\perp}(-A)\,(1+O(1/L))$, where $q^*$ is the fixed-point preactivation variance, $T^*=q^*/(1-\chi_1)$, $B=\chi'(1)$, and $A$ is the matrix of limiting rescaled correlation gaps. That the non-constant eigenvalues are of order $L\chi_1^L$ is due to Xiao, Pennington and Schoenholz; the contribution here is the constant, its positivity, and the extension to inputs of unequal norm. The factor $L$ comes from a double root in the linear recursion for the kernel gap. We prove that $\lambda_{\min}^{\perp}(-A)>0$ for any distinct inputs by showing that every Taylor coefficient of the limiting gap profile is strictly positive, so the rate cannot degenerate further.

Most cited in the text:

- S. Bombari, M. H. Amani and M. Mondelli, Memorization and optimization in deep neural networks with minimum over-parameterization, Advances in Neural Information Processing Systems 35 (NeurIPS 2022), arXiv:2205.10217. (cited 1 time)
- D. Chen, V. A. Menegatto and X. Sun, A necessary and sufficient condition for strictly positive definite functions on spheres, Proc. Amer. Math. Soc. 131 (2003), 2733--2740. (cited 1 time)
- S. Hayou, A. Doucet and J. Rousseau, Exact convergence rates of the neural tangent kernel in the large depth limit, preprint, arXiv:1905.13654. (cited 1 time)
- A. Jacot, F. Gabriel and C. Hongler, Neural tangent kernel: convergence and generalization in neural networks, Advances in Neural Information Processing Systems 31 (NeurIPS 2018), 8571--8580, arXiv:1806.07572. (cited 1 time)


### Which chord of an even cycle preserves its spectral gap

Folder: [one-chord-even-cycle-spectral-gap](public/one-chord-even-cycle-spectral-gap) (source `public/one-chord-even-cycle-spectral-gap/paper/main.tex`)

What the paper claims: Add one edge of conductance $w>0$ to the cycle $C_n$, $n=2m\ge4$, and run the random walk on the resulting weighted graph. We show that the spectral gap of the walk is largest exactly when the new edge joins two antipodal vertices, and that in this case the gap equals $1-\cos(\pi/m)$, the gap of the cycle itself, for every $w$. Every other chord strictly lowers the gap, with an explicit bound. If instead the walk is Metropolized so that its stationary law stays uniform, every chord, antipodal or not, strictly lowers the gap. These are one-edge cases of questions of Diaconis about which added edges speed up a random walk most.

Most cited in the text:

- J. Deng, L. Chang and Q. Yang, Single-chord augmentation of weighted cycles for algebraic connectivity and network coherence, preprint, 2026, arXiv:2605.24479. (cited 1 time)
- P. Diaconis, Some things we've learned (about Markov chain Monte Carlo), Bernoulli 19 (2013), 1294--1305, doi:10.3150/12-BEJSP09, arXiv:1309.7754. (cited 1 time)
- R. Eldan, M. Z. Racz, T. Schramm, Braess's paradox for the spectral gap in random graphs and delocalization of eigenvectors, Random Structures Algorithms 50 (2017), 584--611, doi:10.1002/rsa.20696. (cited 1 time)
- A. Ghosh, S. Boyd, Growing well-connected graphs, in: Proc. 45th IEEE Conference on Decision and Control, 2006, 6605--6611, doi:10.1109/CDC.2006.377282. (cited 1 time)


### Partition quadratic stochastic operators converge to the empty body

Folder: [partition-qso-empty-body](public/partition-qso-empty-body) (source `public/partition-qso-empty-body/paper/main.tex`)

What the paper claims: An $F$-quadratic stochastic operator describes a population of two sexes together with an empty body $0$: parents of the same sex, or a pair containing $0$, produce $0$. Rozikov and Zhamilov proved that every such operator has the unique fixed point $e_0$ and that every trajectory converges to it exponentially fast, and Ganikhodzhaev and Rozikov asked whether the same holds when the two sexes are replaced by the blocks of an arbitrary partition. We show that it does. For a partition into $q$ blocks the mass $y$ outside the empty body satisfies $y'\le(1-1/q)\,y^2$, so every trajectory converges to $e_0$ doubly exponentially fast, and there are operators and trajectories along which this inequality is an equality at every step. The requirement that pairs containing $0$ produce $0$ cannot be dropped.

Most cited in the text:

- R. N. Ganikhodzhaev and U. A. Rozikov, Quadratic stochastic operators: results and open problems, arXiv:0902.4207 (2009). (cited 3 times)
- U. A. Rozikov and U. U. Zhamilov, $F$-quadratic stochastic operators, Math. Notes 83 (2008), 554--559. (cited 2 times)
- S. N. Bernstein, Solution of a mathematical problem connected with the theory of heredity, Ann. Math. Statistics 13 (1942), 53--61. (cited 1 time)
- R. N. Ganikhodzhaev, F. M. Mukhamedov and U. A. Rozikov, Quadratic stochastic operators and processes: results and open problems, Infin. Dimens. Anal. Quantum Probab. Relat. Top. 14 (2011), 279--335. (cited 1 time)


### Entropy and singularity of spectral and pivotal sets in planar percolation

Folder: [percolation-crossing-entropy](public/percolation-crossing-entropy) (source `public/percolation-crossing-entropy/paper/main.tex`)

What the paper claims: The spectral sample and pivotal set of a percolation crossing have the same one- and two-coordinate inclusion probabilities under the uniform product measure. We prove that both Shannon entropies are comparable to total influence for critical square-lattice bond and triangular-lattice site crossings, with matching estimates at every retained nonroot spatial resolution. The triangular entropy bounds are uniform over a class of inhomogeneous near-critical product measures. For critical triangular-site square crossings, the two laws are asymptotically mutually singular: an elementary triangular face is forbidden in the pivotal set and occurs with positive density in a large spectral sample. Every fixed face density below an explicit threshold has nonempty spectral probability comparable to $R^2\alpha_4(R)^2$, while the nonempty overlap of the two laws lies between $R^{-11/12+o(1)}$ and $R^{-1/2+o(1)}$, and equals $R^{-11/12+o(1)}$ if the Garban--Pete--Schramm bound on small spectral samples extends to pivotal sets. Their minimum expected symmetric-difference distance over all couplings is comparable to total influence. Geometric separation persists after independent thinning whenever the retention probability $\rho_R$ satisfies $\rho_R^3R^2\alpha_4(R)\to\infty$; the face detector fails when this quantity tends to zero. The proofs combine spatial encoding, arm estimates, local Fourier cancellation, and an exact six-cycle coercivity inequality preserved under exterior conditioning.

Most cited in the text:

- C. Garban, G. Pete and O. Schramm, The Fourier spectrum of critical percolation, Acta Math. 205 (2010), no. 1, 19--104. https://doi.org/10.1007/s11511-010-0051-xdoi:10.1007/s11511-010-0051-x. Corrected version https://arxiv.org/abs/0803.375 (cited 33 times)
- P. Nolin, Near-critical percolation in two dimensions, Electron. J. Probab. 13 (2008), no. 55, 1562--1623. https://doi.org/10.1214/EJP.v13-565doi:10.1214/EJP.v13-565. https://arxiv.org/abs/0711.4948arXiv:0711.4948; numbered references follo (cited 11 times)
- O. Schramm and J. E. Steif, Quantitative noise sensitivity and exceptional times for percolation, Ann. of Math. (2) 171 (2010), no. 2, 619--672. https://doi.org/10.4007/annals.2010.171.619doi:10.4007/annals.2010.171.619. https://arxiv.org/a (cited 4 times)
- S. Smirnov and W. Werner, Critical exponents for two-dimensional percolation, Math. Res. Lett. 8 (2001), no. 5--6, 729--744. https://arxiv.org/abs/math/0109120arXiv:math/0109120. (cited 3 times)


### Phi-mixing implies interlaced rho-mixing for Markov chains

Folder: [phi-mixing-interlaced-rho-mixing-markov](public/phi-mixing-interlaced-rho-mixing-markov) (source `public/phi-mixing-interlaced-rho-mixing-markov/main.tex`)

What the paper claims: We prove that every phi-mixing Markov chain is interlaced rho-mixing, giving an affirmative answer to Question 5 in Bradley's 2005 survey. The chain may be time-inhomogeneous and need not be stationary; its state space may be any standard Borel space. With Bradley's normalization, we obtain $\rho^*(n)\le \min\{1,2\sqrt{2\phi(n)}\},$ and the stronger bound $\rho^*(n)\le 2\sqrt{2\phi(n)(1-2\phi(n))}$ when $\phi(n)\le1/4$. The proof combines a transition-row estimate with Peyre's maximal-correlation tensorization under prefix conditioning. A Markov separator makes the conditional correlation matrix of an arbitrary interlacing a weighted path. We give a self-contained proof of the local channel estimate, including the passage to standard Borel spaces. An explicit six-state chain shows that the square-root dependence cannot be improved in a uniform coefficient comparison. A countably infinite reset chain shows that the corresponding loss of a factor two in the exponential rate is also unavoidable for a single stationary chain; the same chain has lower psi coefficients identically zero, so it lies outside the previously known sufficient condition. A symmetric two-state family separately shows first-order sharpness of the path amplification factor. The finite components of the argument are machine-checked in Lean 4.

Most cited in the text:

- R. C. Bradley, Basic properties of strong mixing conditions. A survey and some open questions, Probab. Surv. 2 (2005), 107--144. https://doi.org/10.1214/154957805100000104doi:10.1214/154957805100000104. (cited 8 times)
- R. Peyre, Tensorizing maximal correlations, arXiv:1004.1602v2 (2010), 128 pp. https://arxiv.org/abs/1004.1602v2. (cited 6 times)
- R. C. Bradley, Every ``lower psi-mixing'' Markov chain is ``interlaced rho-mixing'', Stochastic Process. Appl. 72 (1997), 221--239. https://doi.org/10.1016/S0304-4149(97)00090-2doi:10.1016/S0304-4149(97)00090-2. (cited 4 times)
- R. C. Bradley, A stationary rho-mixing Markov chain which is not ``interlaced'' rho-mixing, J. Theoret. Probab. 14 (2001), 717--727. https://doi.org/10.1023/A:1017545123473doi:10.1023/A:1017545123473. (cited 2 times)


### Two instability intervals for a switched planar system with one non-Hurwitz matrix

Folder: [planar-switching-two-instability-intervals](public/planar-switching-two-instability-intervals) (source `public/planar-switching-two-instability-intervals/paper/main.tex`)

What the paper claims: Let $\dot X_t=A_{I_t}X_t$ in $\R^2$, where $I$ jumps between $0$ and $1$ at rate $r$. Malrieu asked whether $A_0,A_1$ can be chosen so that the set of unstable rates is a union of several intervals. For the Hurwitz matrix $A_0=\bigl(\begin{smallmatrix}-3/4&-1 1&-3/4\end{smallmatrix}\bigr)$ and the non-Hurwitz matrix $A_1=\mathrm{diag}(5/4,-11/4)$ we prove that the top Lyapunov exponent $\lambda(r)$ is continuous, positive on $(0,1/10]$, negative on $[4.997,5.003]$ and positive on $[19.95,20.05]$, so the set of unstable rates has at least two components. The signs near $r=5$ and $r=20$ come from trigonometric polynomials with exact rational coefficients that solve the Poisson equation for the direction $X_t/|X_t|$ up to an explicit error. Numerically $\lambda$ changes sign twice, near $r=1.2228$ and $r=7.7616$. The case in which both matrices are Hurwitz, as in the example behind the question, remains open.

Most cited in the text:

- S. D. Lawley, J. C. Mattingly and M. C. Reed, Sensitivity to switching rates in stochastically switched ODEs, Commun. Math. Sci. 12 (2014), 1343--1352. https://doi.org/10.4310/CMS.2014.v12.n7.a9 (cited 9 times)
- Y. Chitour, G. Mazanti, P. Monmarche and M. Sigalotti, On the gap between deterministic and probabilistic Lyapunov exponents for continuous-time linear systems, Electron. J. Probab. 28 (2023), Paper No. 43, 1--39. https://doi.org/10.1214/23 (cited 6 times)
- F. Malrieu, Some simple but challenging Markov processes, Ann. Fac. Sci. Toulouse Math. (6) 24 (2015), 857--883. https://doi.org/10.5802/afst.1468 (cited 5 times)
- S. Meyn and R. L. Tweedie, Markov Chains and Stochastic Stability, 2nd ed., Cambridge University Press, Cambridge, 2009. (cited 4 times)


### positive-cookie-ballisticity

Folder: [positive-cookie-ballisticity](public/positive-cookie-ballisticity) (source `public/positive-cookie-ballisticity/main.tex`)


### Posterior cones and sharp reconstruction thresholds on finite-mean Galton--Watson trees

Folder: [posterior-cones-reconstruction](public/posterior-cones-reconstruction) (source `public/posterior-cones-reconstruction/paper/T067_full_proof.tex`)

What the paper claims: We study reconstruction for symmetric ferromagnetic Potts broadcasting on an observed Galton--Watson tree with arbitrary finite mean offspring. For three states we construct an explicit invariant condition on posterior laws using the polynomial $H=y-x^2/2$, where $x$ and $y$ are the quadratic and cubic centered posterior invariants. Two global inequalities, certified by exact nonnegative coefficients, preserve this condition and give strict information contraction. Combining the resulting argument with an existing four-state posterior cone proves that reconstruction occurs exactly when $d\lambda^2>1$ for both three and four states, including nonreconstruction at equality. No offspring variance or tail assumption is required. We give explicit critical decay bounds, a first-moment-only supercritical argument, and almost-sure statements conditional on survival. Exact verification programs and complete coefficient tables accompany the proof. The noiseless unary-line endpoint is classified separately.

Most cited in the text:

- OpenAI, The Reconstruction Threshold for the Ferromagnetic Four-State Potts Model, manuscript dated 5 October 2026. https://github.com/openai/math/tree/1581d4cbdd69a0faf34b2089614fe2a814316a6a/preprints/The-Reconstruction-Threshold-for-the- (cited 10 times)
- E. Mossel and Y. Peres, Information flow on trees, Ann. Appl. Probab. 13 (2003), 817--844. (cited 2 times)
- P. M. Bleher, J. Ruiz and V. A. Zagrebnov, On the purity of the limiting Gibbs state for the Ising model on the Bethe lattice, J. Stat. Phys. 79 (1995), 473--482. (cited 1 time)
- A. Decelle, F. Krzakala, C. Moore and L. Zdeborova, Asymptotic analysis of the stochastic block model for modular networks and its algorithmic applications, Phys. Rev. E 84 (2011), 066106. (cited 1 time)


### The Kesten--Stigum bound is tight for the four-state Potts model on the binary tree

Folder: [potts-four-state-binary-tree](public/potts-four-state-binary-tree) (source `public/potts-four-state-binary-tree/paper/main.tex`)

What the paper claims: Consider the broadcast of a uniformly random colour from the root of the infinite binary tree, where each edge copies its parent's colour with probability $\lambda+(1-\lambda)/4$ and otherwise chooses one of the other three colours uniformly. We prove that for $0<\lambda\le 1/\sqrt2$ the colours at depth $n$ carry asymptotically no information about the root colour. Since reconstruction is possible for $2\lambda^2>1$ by the theorem of Kesten and Stigum, the Kesten--Stigum bound is the reconstruction threshold for the ferromagnetic four-state Potts channel on the binary tree. A preprint of OpenAI establishes this threshold on every regular tree; the proof given here is different. It is computer assisted. A certified upper bound on the second moment of the root posterior, obtained from an exact finite-state upgrade of the belief-propagation recursion, places the limiting posterior law in a small neighbourhood of the uniform law; an exact polynomial certificate then shows that no nontrivial belief-propagation fixed point lies in that neighbourhood.

Most cited in the text:

- N. Bhatnagar and E. Maneva, A computational method for bounding the probability of reconstruction on trees, SIAM J. Discrete Math. 25 (2011), 854--871; arXiv:0903.4812. (cited 1 time)
- P. M. Bleher, J. Ruiz and V. A. Zagrebnov, On the purity of the limiting Gibbs state for the Ising model on the Bethe lattice, J. Stat. Phys. 79 (1995), 473--482. (cited 1 time)
- W. Evans, C. Kenyon, Y. Peres and L. J. Schulman, Broadcasting on trees and the Ising model, Ann. Appl. Probab. 10 (2000), 410--433. (cited 1 time)
- Y. Gu and Y. Polyanskiy, Non-linear log-Sobolev inequalities for the Potts semigroup and applications to reconstruction problems, Comm. Math. Phys. 404 (2023), 769--831; arXiv:2005.05444. (cited 1 time)


### potts-kesten-stigum-small-degree

Folder: [potts-kesten-stigum-small-degree](public/potts-kesten-stigum-small-degree) (source `public/potts-kesten-stigum-small-degree/paper/q3/entry_table.tex`)


### prophet-secretary-hardness

Folder: [prophet-secretary-hardness](public/prophet-secretary-hardness) (source `public/prophet-secretary-hardness/paper/prophet_secretary_hardness.tex`)


### On the regularity threshold of uniformly positive quadratic stochastic operators

Folder: [qso-regularity-threshold](public/qso-regularity-threshold) (source `public/qso-regularity-threshold/paper/main.tex`)

What the paper claims: A quadratic stochastic operator on the simplex of probability vectors in $\R^m$ is regular if all of its trajectories converge to one point. Ganikhodzhaev and Sarymsakov showed that the operator is regular when all of its heredity coefficients exceed $1/(2m)$, and Ganikhodzhaev and Rozikov asked for the least number $\lambda_m$ with this property. For $m=2$ we prove $\lambda_2=(3-\sqrt7)/4$. For every $m\ge3$ we prove that $\lambda_m$ lies between $(1-1/\sqrt{m+1})/(2m)$ and $2/(3m+2+\sqrt{m^2+12m+4})$, which is less than $1/(2m)$; in particular $2m\lambda_m\to1$. The upper bound comes from a contraction of the operator in the Fisher--Rao metric, which rests on two inequalities: the derivative of a quadratic stochastic operator at most doubles the Fisher information of a tangent vector, and the uniform-mixture map $q\mapsto\mu\mathbf 1+(1-m\mu)q$ multiplies it by at most $(1-m\mu)^2/[1-(m-2)\mu]$, where $\mu$ is the least heredity coefficient. The lower bound comes from an explicit family of operators with strictly positive coefficients and a two-cycle.

Most cited in the text:

- R. Ganikhodzhaev, F. Mukhamedov and U. Rozikov, Quadratic stochastic operators and processes: results and open problems, Infin. Dimens. Anal. Quantum Probab. Relat. Top. 14 (2011), no. 2, 279--335. 10.1142/S0219025711004365 (cited 4 times)
- R. N. Ganikhodzhaev and U. A. Rozikov, Quadratic stochastic operators: results and open problems, preprint (2009), https://arxiv.org/abs/0902.4207arXiv:0902.4207. (cited 4 times)
- D. Fasino and F. Tudisco, Ergodicity coefficients for higher-order stochastic processes, SIAM J. Math. Data Sci. 2 (2020), no. 3, 740--769. 10.1137/19M1285214 (cited 3 times)
- R. L. Dobrushin, Central limit theorem for nonstationary Markov chains. I, Theory Probab. Appl. 1 (1956), no. 1, 65--80. 10.1137/1101006 (cited 2 times)


### quantile-process-lp

Folder: [quantile-process-lp](public/quantile-process-lp) (source `public/quantile-process-lp/paper.tex`)


### Random-cluster measures with $0<q<1$ are not monotone in $p$

Folder: [random-cluster-not-monotone](public/random-cluster-not-monotone) (source `public/random-cluster-not-monotone/paper/main.tex`)

What the paper claims: For $q\ge1$ the random-cluster measure $\phi_{G,p,q}$ on a finite graph $G$ is stochastically increasing in the edge parameter $p$. We show that for every $q\in(0,1)$ there are a finite graph $G$, an edge $e$ and $p_1<p_2$ with $\phi_{G,p_1,q}(e\text{ open})>\phi_{G,p_2,q}(e\text{ open})$. In particular the measures $(\phi_{G,p,q})_{p\in[0,1]}$ admit no monotone coupling, which answers a question of Pete for $0<q<1$. The graphs are theta graphs, consisting of an edge $e=uv$ and $m$ internally disjoint paths of length $l$ from $u$ to $v$. On these graphs the probability that $e$ is open has a closed form, and it fails to be increasing in $p$ for all large $m$ exactly when $q<1-e^{1-1/l}/l$; for larger $q$ it is strictly increasing for every $m$. For the arboreal gas, the limit $q\to0$ with $p/(1-p)=\beta q$, the same computation gives a criterion in terms of the path lengths. The smallest theta graph satisfying it has ten edges, and on it the probability of $e$ increases up to $\beta^*\approx13.574$ and decreases after. If every edge of $G$ lies in at most one cycle, a monotone coupling exists for every $q>0$. The finite computations are checked in Lean.

Most cited in the text:

- G. Grimmett, The Random-Cluster Model, Grundlehren der mathematischen Wissenschaften 333, Springer, Berlin, 2006. https://doi.org/10.1007/978-3-540-32891-9doi:10.1007/978-3-540-32891-9. (cited 6 times)
- G. Pete, Probability and Geometry on Groups, lecture notes, version of April 3, 2024. http://www.math.bme.hu/ gabor. (cited 5 times)
- N. Halberstam and T. Hutchcroft, Uniqueness of the infinite tree in low-dimensional random forests, Probab. Math. Phys. 5 (2024), 1185--1216. https://doi.org/10.2140/pmp.2024.5.1185doi:10.2140/pmp.2024.5.1185; https://arxiv.org/abs/2302.122 (cited 2 times)
- V. Beffara, C. Faipeur and T. Oke, A new bound for the critical point of the FK model for $q<1$, preprint, 2025. https://arxiv.org/abs/2512.16486arXiv:2512.16486. (cited 1 time)


### The topology of the recurrent and transient sets of homogeneous random walks

Folder: [recurrent-set-topology](public/recurrent-set-topology) (source `public/recurrent-set-topology/paper/main.tex`)

What the paper claims: Each point $a$ of a simplex $A$ defines the random walk on a finitely generated abelian group that takes the $i$-th step of a fixed finite set $S$ with probability $a_i$. Li, Mossel and Weiss asked when the set $R$ of recurrent walks is path-connected or simply connected, and when the set $R^c$ of transient walks is path-connected, simply connected or convex. We answer these questions in terms of the projections $v_i$ of the steps to the free part $\Z^n$ of the group. Apart from two simple cases, in which $R$ is contractible or convex, $R$ is homotopy equivalent to a bipartite graph whose vertices are the lines and planes through the origin on which the steps balance. The set $R^c$ is empty when every $v_i$ is zero, and otherwise contractible unless $0$ lies in the relative interior of the convex hull of the $v_i$ and these vectors span a line or a plane; then it has two components or is homotopy equivalent to a circle. It is convex exactly when every recurrent walk is positive recurrent.

Most cited in the text:

- R. Li, E. Mossel and B. Weiss, Monotonicity, topology, and convexity of recurrence in random walks, Ann. Appl. Probab. 36 (2026), no. 5, 4291--4310, 10.1214/26-AAP2329. Numbered statements are cited from 2403.04108 (version 4, 2025). (cited 17 times)
- A. Hatcher, Algebraic Topology, Cambridge University Press, Cambridge, 2002. (cited 3 times)


### The relaxation time does not control the normal approximation of stationary additive functionals

Folder: [relaxation-time-normal-approximation](public/relaxation-time-normal-approximation) (source `public/relaxation-time-normal-approximation/paper/main.tex`)

What the paper claims: Let $X$ be a finite irreducible reversible Markov chain in continuous time with relaxation time $\tau_2$, started from its stationary distribution, and let $g$ be a function on its states with mean $0$ and variance $1$ under that distribution. Aldous and Fill asked whether the Kolmogorov distance between $\int_0^tg(X_u)\,du/(\sigma t^{1/2})$, where $\sigma^2$ is the asymptotic variance rate, and the standard normal law is bounded by a function of $\max|g|$ and $t/\tau_2$ alone that tends to $0$ as $t/\tau_2\to\infty$. It is not. For every $b\ge1$ and $s\ge2b$ there are a chain on four states with $\tau_2=1$ and a function $g$ of mean $0$ and variance $1$ with $\max|g|=b$ such that $\int_0^sg(X_u)\,du\le0$ with probability at least $1-4/s$, so at $t=s$ the distance is at least $1/2-4/s$ whatever positive constant the integral is divided by.

Most cited in the text:

- D. Aldous and J. A. Fill, Reversible Markov Chains and Random Walks on Graphs, unfinished monograph, 2002, recompiled version 2014, https://www.stat.berkeley.edu/ aldous/RWG/book.pdf. (cited 7 times)
- E. Bolthausen, The Berry--Esseen theorem for functionals of discrete Markov chains, Z. Wahrsch. Verw. Gebiete 54 (1980), 59--73. (cited 1 time)
- C. Kipnis and S. R. S. Varadhan, Central limit theorem for additive functionals of reversible Markov processes and applications to simple exclusions, Comm. Math. Phys. 104 (1986), 1--19. (cited 1 time)
- P. Lezaud, Chernoff and Berry--Esseen inequalities for Markov processes, ESAIM Probab. Statist. 5 (2001), 183--201. (cited 1 time)


### Global Stability of Deep Gaussian ReLU Networks

Folder: [relu-global-stability-numerics](public/relu-global-stability-numerics) (source `public/relu-global-stability-numerics/paper/main.tex`)

What the paper claims: A bias-free ReLU network of width $n$ and depth $L$ with independent $\mathcal N(0,\alpha/n)$ weights has a global Lipschitz constant $K_{n,L}(\alpha)$, the worst stretching over all pairs of inputs for one draw of the weights. We prove, for every $n$, every $L\ge2$ and every $\theta\in(0,1/4)$, $\PP\bigl(K_{n,L}(\alpha)>1\bigr)\le2\exp\!\bigl(n\,B_L(\alpha,\theta)\bigr),\qquad B_L=L\,H(1/L)+\log5+\theta\log4+L\,h_\alpha(\theta),$ with $H$ the binary entropy and $h_\alpha$ elementary, and for $\alpha>2$ the converse bound $\PP(K_{n,L}(\alpha)\le1)\le5\alpha^2L/(n(\alpha-2)^2)$. The fixed-depth threshold $\alpha_L$ therefore tends to $2$, with $\alpha_L\ge2\exp[-(\sqrt{10}+o(1))\sqrt{\log L/L}]$. The proof turns on an exact identity for realizable activation patterns: averaging over the $2^{nL}$ sign gauges, which preserve the law of the weights, turns the realizability event into a deterministic orthant count divided by $2^{nL}$. The second result ties the layers: for one matrix $W$ applied repeatedly, $x_{t+1}=\phi(Wx_t)$, and any fixed horizon $T$, $\max_{t\le T}|2^t\norm{x_t}^2-1|\le\delta$ with probability $1-Ce^{-cN}$, for every deterministic start and for almost every start of a typical matrix. Here the dependence of the trajectory on the matrix is handled by conditioning, made exact by a Gaussian innovation lemma for adaptive orthogonal queries. The two results share their object and their obstacle and resolve it in opposite ways; the paper explains why each method fits its question, and uses the second to sharpen the expansive side of the first to an exponential rate. Selected identities, bounds and norm statistics are checked numerically at small width.

Most cited in the text:

- Z. D. Bai and Y. Q. Yin, Necessary and sufficient conditions for almost sure convergence of the largest eigenvalue of a Wigner matrix, Ann. Probab. 16 (1988), 1729--1741; and Limit of the smallest eigenvalue of a large dimensional sample co (cited 1 time)
- T. M. Cover, Geometrical and statistical properties of systems of linear inequalities with applications in pattern recognition, IEEE Trans. Electronic Computers EC-14 (1965), 326--334. (cited 1 time)
- T. M. Cover and J. A. Thomas, Elements of Information Theory, 2nd ed., Wiley, 2006; the entropy bound for binomial sums. (cited 1 time)
- S. Dirksen, P. Finke, P. Geuchen, D. Stoger and F. Voigtlaender, Near-optimal estimates for the $^p$-Lipschitz constants of deep random ReLU neural networks, https://arxiv.org/abs/2506.19695v1arXiv:2506.19695v1, 2025. (cited 1 time)


### Finite-state counterexamples to Ross's second queueing conjecture

Folder: [Ross-s-second-queueing-conjecture](public/Ross-s-second-queueing-conjecture) (source `public/Ross-s-second-queueing-conjecture/main.tex`)

What the paper claims: We construct finite-state Markov arrival-rate processes for which faster modulation increases the mean stationary workload of a stable single-server queue, disproving the universal ordering in Leskela's formulation of Ross's second conjecture. A 64-state example has positive transition rates between every pair of states, independent service times uniform on $[0.99,1.01]$, and an explicit positive workload gap. A 128-state example additionally has strictly positive arrival-rate autocovariance at every lag. More generally, finite-state examples can exhibit any prescribed finite number of separated workload rises and falls. The proofs use a second-order expansion with a nonnegative, speed-uniform remainder under only a finite second service moment. We characterize the service distributions for which the second-order workload coefficient is nonincreasing for every bounded stationary environment: the function $s\mapsto\E(1-\cos(sB))/s^2$ must be nonincreasing. Mixtures of exponential service distributions satisfy this criterion. An exact Palm identity transfers the workload reversals to customer waiting times.

Most cited in the text:

- L. Leskela (2022). Ross's second conjecture and supermodular stochastic ordering. Queueing Syst. 100 213--215. https://doi.org/10.1007/s11134-022-09824-0doi:10.1007/s11134-022-09824-0. (cited 3 times)
- S. Asmussen (2003). Applied Probability and Queues. 2nd ed. Applications of Mathematics 51. Springer, New York. https://doi.org/10.1007/b97236doi:10.1007/b97236. (cited 2 times)
- F. Baccelli and P. Bremaud (2003). Elements of Queueing Theory: Palm Martingale Calculus and Stochastic Recurrences. 2nd ed. Applications of Mathematics 26. Springer, Berlin. https://doi.org/10.1007/978-3-662-11657-9doi:10.1007/978-3-662-11 (cited 2 times)
- B. Błaszczyszyn (1995). Factorial-moment expansion for stochastic systems. Stochastic Process. Appl. 56 321--335. https://doi.org/10.1016/0304-4149(94)00071-Zdoi:10.1016/0304-4149(94)00071-Z. (cited 2 times)


### rr-constant-step-log-factor

Folder: [rr-constant-step-log-factor](public/rr-constant-step-log-factor) (source `public/rr-constant-step-log-factor/paper/rr_log_factor.tex`)


### The layer distribution of the random recursive tree and the minimum of the Poisson-weighted infinite tree

Folder: [rrt-layer-tail](public/rrt-layer-tail) (source `public/rrt-layer-tail/paper/main.tex`)

What the paper claims: The layer of a vertex of a tree is the number of rounds of leaf removal after which the vertex is a leaf. Stepanyants, Krapivsky, Hartle and Krioukov computed the limiting proportion $\ell_k$ of vertices at layer $k$ in a random recursive tree as an integral of an iterated nonlinear recursion, showed $e^{-k}\lesssim\sum_{j\ge k}\ell_j\lesssim e^{-k/e}$, and conjectured that $\ell_k=\exp[-k/e-\tfrac{3}{2e}\log k-O(1)]$. We prove that $\ell_k e^{k/e}k^{3/(2e)}$ converges to a positive finite constant. The recursion is the law of the minimal position $M_k$ in generation $k$ of the Poisson-weighted infinite tree, so that $\sum_{j\ge k}\ell_j=\E e^{-M_k}$, and the asymptotics follow from the results of Addario-Berry and Ford and of Aidekon on that branching random walk. We also prove the layer half of their second conjecture: the largest layer $L_n$ of a random recursive tree on $n$ vertices equals half its diameter rounded down, and $L_n=e\log n-\tfrac32\log\log n+O_\PP(1)$.

Most cited in the text:

- L. Addario-Berry and K. Ford, Poisson--Dirichlet branching random walks, Ann. Appl. Probab. 23 (2013), 283--307. (cited 8 times)
- E. Aidekon, Convergence in law of the minimum of a branching random walk, Ann. Probab. 41 (2013), 1362--1426. (cited 8 times)
- H. Stepanyants, P. L. Krapivsky, H. Hartle and D. Krioukov, The rank and layer distributions in random recursive trees, arXiv:2608.04303v2 (2026). (cited 6 times)
- L. Addario-Berry and B. Reed, Minima in branching random walks, Ann. Probab. 37 (2009), 1044--1079. (cited 1 time)


### Fitting and choosing radiative-transfer emulators for the retrieval

Folder: [rt-emulators-for-retrieval](public/rt-emulators-for-retrieval) (source `public/rt-emulators-for-retrieval/paper/retrieval_training.tex`)

What the paper claims: Radiative-transfer emulators are fitted to a code's outputs but used through an inverse, the retrieval of surface reflectance, and here they are fitted and chosen on the retrieval error. On the EMIT table, networks trained on the square root of the retrieval weights floored at a hundredth of the median transmission lower the radiance error by $8\%$ and the 95th percentiles of the retrieval error by $32$ to $44\%$ on every one of ten splits, and they lower every tail on every split at reflectances from $0.1$ to $0.9$ with each failed inversion counted as an infinite error; a kernel fitted on learned network features keeps the lowest retrieval tails on this table. On the libRadtran benchmark of Mazid and Rishe the same weights lower the radiance error from $0.91\%$ to $0.11\%$ and the retrieval tail from $4.6$ to $0.35$ points on every one of ten seeds, at a larger error in the spherical albedo, and on states beyond the training range of aerosol and water vapour they lower the root-mean-square error as well. Two failed evaluations of the code in the EMIT table make every weighted network worse than the plain one, and refitting a convex stack on the retrieval error lowers its tail by a quarter. The theory behind these results gives the retrieval error exactly in terms of the component errors and shows that the forward and retrieval rankings of two emulators differ by a change of measure with density proportional to $t^2/q^4$. With the transmission floored, training on the retrieval error is regression under a known covariate shift whose price in effective sample size can be computed before any training; without the floor the shift is not integrable.

Most cited in the text:

- M. A. A. Mazid and N. Rishe. Multi-fidelity emulation of atmospheric correction coefficients with physics-guided Kolmogorov--Arnold networks. Remote Sensing, 18(11):1826, 2026. (cited 14 times)
- C. Ma, R. Pathak and M. J. Wainwright. Optimally tackling covariate shift in RKHS-based nonparametric regression. The Annals of Statistics, 51(2):738--761, 2023. (cited 5 times)
- H. Shimodaira. Improving predictive inference under covariate shift by weighting the log-likelihood function. Journal of Statistical Planning and Inference, 90(2):227--244, 2000. (cited 5 times)
- P. G. Brodrick, D. R. Thompson, J. E. Fahlen, M. L. Eastwood, C. M. Sarture, S. R. Lundeen, W. Olson-Duvall, N. Carmon and R. O. Green. Generalized radiative transfer emulation for imaging spectroscopy reflectance retrievals. Remote Sensing (cited 4 times)


### Good configurations of random walk in random scenery under two-sided conditioning

Folder: [rwrs-two-sided-good-configurations](public/rwrs-two-sided-good-configurations) (source `public/rwrs-two-sided-good-configurations/paper/main.tex`)

What the paper claims: Let $(S_t)_{t\in\Z}$ be a nearest-neighbour random walk on $\Z$ with $S_0=0$ and probability $p$ of a step to the right, and let $(C_x)_{x\in\Z}$ be an independent field of independent fair signs. The reduced random walk in random scenery is the colour process $Y_t=C_{S_t}$. Den Hollander and Steif conjectured that, under conditioning on the colours at all nonzero times, every configuration is bad for $Y_0$ when $1/2\le p<4/5$ and every configuration is good when $4/5<p\le1$. We prove that every configuration is good when $27/28<p\le1$. More precisely, the conditional probabilities of $Y_0$ given the colours at the times $0<|t|\le m$ converge uniformly as $m\to\infty$, with an explicit modulus, to a version of the conditional probability that is continuous everywhere. For colours with $\PP(C_x=1)=\alpha$ the same holds when $p>27/(27+4\beta^2)$, where $\beta=\min(\alpha,1-\alpha)$. The proof writes the posterior law of the walk as a gas of disjoint time intervals separated by cut times, bounds the activities of the intervals, and swaps the central part of two coupled samples between common cut times.

Most cited in the text:

- F. den Hollander and J. E. Steif, Random walk in random scenery: a survey of some recent results, in Dynamics & Stochastics, IMS Lecture Notes Monogr. Ser. 48 (2006), 53--65. 10.1214/074921706000000077 (cited 6 times)
- S. Blachere, F. den Hollander and J. E. Steif, A crossover for the bad configurations of random walk in random scenery, Ann. Probab. 39 (2011), no. 5, 2018--2041. 10.1214/11-AOP664 (cited 4 times)
- C. Maes, F. Redig and A. Van Moffaert, Almost Gibbsian versus weakly Gibbsian measures, Stochastic Process. Appl. 79 (1999), no. 1, 1--15. 10.1016/S0304-4149(98)00083-0 (cited 2 times)
- F. den Hollander, J. E. Steif and P. van der Wal, Bad configurations for random walk in random scenery and related subshifts, Stochastic Process. Appl. 115 (2005), no. 7, 1209--1232. 10.1016/j.spa.2005.03.001 (cited 2 times)


### Corner angles of sandpile aggregates on a background of holes

Folder: [sandpile-holes-corner-angles](public/sandpile-holes-corner-angles) (source `public/sandpile-holes-corner-angles/paper/main.tex`)

What the paper claims: Start the abelian sandpile on $\Z^2$ with $n$ chips at the origin, on a background in which every site absorbs the first $H$ chips it receives (for $H<0$, every site starts with $-H$ chips), and let $S_{n,H}$ be the set of sites that fire. Holroyd, Levine, Meszaros, Peres, Propp and Wilson asked whether the limiting shape of $S_{n,H}$ is a regular $(4H+12)$-gon. We show that for $H\ge-1$ every corner of a subsequential limit of $S_{n,H}$, under any rescaling, has an interior angle $\alpha$ with $\alpha>\pi/2$ and $\sin\alpha\le1/(H+3)$. The corners of a regular $(4H+12)$-gon are sharper than this, so no such limit is a regular $(4H+12)$-gon; since $S_{n,-2}$ is a square for every $n$, this answers the question for every $H\ge-2$. A limit that is a convex polygon has a number of vertices that is divisible by $4$ and at least $2\pi/\arcsin(1/(H+3))$; it has at least $12$ vertices for $H=-1$ and at least $20$ for $H=0$. The proof combines the least action principle, a reflection argument and a count of last firings with the compactness argument of Pegden and Smart, and ends with a corner lemma for the limiting equation $\Delta U=s$, in which $H+2\le s\le H+3$ on the limit set and $s=0$ outside it.

Most cited in the text:

- A. Fey, L. Levine and Y. Peres, Growth rates and explosions in sandpiles, J. Stat. Phys. 138 (2010), 143--159. (cited 9 times)
- A. E. Holroyd, L. Levine, K. Meszaros, Y. Peres, J. Propp and D. B. Wilson, Chip-firing and rotor-routing on directed graphs, in In and Out of Equilibrium 2, Progr. Probab. 60, Birkhauser, Basel, 2008, 331--364. (cited 8 times)
- W. Pegden and C. K. Smart, Convergence of the Abelian sandpile, Duke Math. J. 162 (2013), 627--642. (cited 8 times)
- L. Levine and Y. Peres, Strong spherical asymptotics for rotor-router aggregation and the divisible sandpile, Potential Anal. 30 (2009), 1--27. (cited 7 times)


### The second largest outdegree of conditioned Galton--Watson trees with infinite variance

Folder: [second-largest-degree-infinite-variance](public/second-largest-degree-infinite-variance) (source `public/second-largest-degree-infinite-variance/paper/main.tex`)

What the paper claims: Let $\xi$ be a random variable with values in $\{0,1,2,\dots\}$ and $\E\xi=1$, let $Y_{(1)}\ge Y_{(2)}\ge\dots$ be the outdegrees, in decreasing order, of a Galton--Watson tree with offspring distribution $\xi$ conditioned to have $n$ vertices, and let $\xi_{(1)}\ge\xi_{(2)}\ge\dots$ be the order statistics of $n$ independent copies of $\xi$. Janson proved that if $\xi$ has finite variance then, for every fixed $j$, $Y_{(j)}$ and $\xi_{(j)}$ have asymptotically the same distribution. He asked whether two consequences of this remain true when the variance is infinite: that $Y_{(1)}<h(n)$ with high probability when $n\Pp(\xi\ge h(n))\to0$, and that $Y_{(j)}\ge h(n)$ with high probability for every fixed $j$ when $n\Pp(\xi\ge h(n))\to\infty$. Kortchemski and Richier showed that the first can fail. We show that the second can fail as well. We construct an offspring distribution with mean $1$ and infinite variance, and integers $n_r\to\infty$ and $L_r$ with $n_r\Pp(\xi\ge L_r)\ge r$, such that with probability at least $1-1/r$ the conditioned tree with $n_r$ vertices has exactly one vertex of outdegree at least $L_r$, of outdegree $(r+\frac12)L_r$, while all other vertices have outdegree at most $L_r/(64(\log n_r)^2)$. Along $n_r$ the largest outdegree is of larger order than $\xi_{(1)}$ and the second largest is of smaller order than $\xi_{(2)}$, and each of the six conclusions of Janson's theorem fails. The same holds for the random allocation of $n-1$ balls into $n$ boxes.

Most cited in the text:

- S. Janson, Simply generated trees, conditioned Galton--Watson trees, random allocations and condensation, Probab. Surv. 9 (2012), 103--252. (cited 12 times)
- I. Kortchemski and L. Richier, Condensation in critical Cauchy Bienayme--Galton--Watson trees, Ann. Appl. Probab. 29 (2019), no. 3, 1837--1877. (cited 2 times)
- G. Bennett, Probability inequalities for the sum of independent random variables, J. Amer. Statist. Assoc. 57 (1962), 33--45. (cited 1 time)
- T. Duquesne, A limit theorem for the contour process of conditioned Galton--Watson trees, Ann. Probab. 31 (2003), 996--1027. (cited 1 time)


### The conjectured dominating pair for DP-SGD with shuffled batches is not dominating

Folder: [shuffled-ablq-dominating-pair](public/shuffled-ablq-dominating-pair) (source `public/shuffled-ablq-dominating-pair/paper/main.tex`)

What the paper claims: Chua, Ghazi, Kamath, Kumar, Manurangsi, Sinha and Zhang conjectured that the pair of Gaussian mixtures $P_{\mathcal S}=\frac1T\sum_t\N(2e_t,\sigma^2I)$, $Q_{\mathcal S}=\frac1T\sum_t\N(e_t,\sigma^2I)$ tightly dominates the adaptive batch linear query mechanism with shuffled batches, for every adaptive query method. We show that the conjecture fails for every number of steps $T\ge2$ and every batch size. The query method that breaks it answers as the conjectured worst case at every step but the last, and at the last step changes the query when the earlier outputs suggest that the differing record was in an early batch. At $T=2$, $\sigma=1$ and $\varepsilon=\frac12$ its hockey-stick divergence is $0.22323$ against $0.22127$ for the conjectured pair, and an interval-arithmetic certificate bounds the excess below by $1.04\cdot10^{-4}$. A direct analytic last-step argument gives strict failure at every $T\ge2$; a separate certificate at $T=3$ gives a quantitative bound. The same query method also beats the pair in Kullback--Leibler divergence and in Renyi divergence of every order we tested, from $\frac14$ to $5$, in both directions.

Most cited in the text:

- L. Chua, B. Ghazi, P. Kamath, R. Kumar, P. Manurangsi, A. Sinha and C. Zhang, How private are DP-SGD implementations?, Proceedings of the 41st International Conference on Machine Learning (ICML 2024); arXiv:2403.17673. (cited 3 times)
- M. van Dijk and M. B. Ertan, Trade-off functions for DP-SGD with subsampling based on random allocation: tight upper and lower bounds, arXiv:2605.06259v3 (2026). (cited 2 times)
- M. Abadi, A. Chu, I. Goodfellow, H. B. McMahan, I. Mironov, K. Talwar and L. Zhang, Deep learning with differential privacy, Proceedings of the 2016 ACM SIGSAC Conference on Computer and Communications Security (CCS 2016), 308--318. (cited 1 time)
- L. Chua, B. Ghazi, P. Kamath, R. Kumar, P. Manurangsi, A. Sinha and C. Zhang, Scalable DP-SGD: shuffling vs. Poisson subsampling, Advances in Neural Information Processing Systems 37 (NeurIPS 2024); arXiv:2411.04205. (cited 1 time)


### The length of the network spanning $k$ random points in the Poisson line SIRSN

Folder: [sirsn-k-point-span-length](public/sirsn-k-point-span-length) (source `public/sirsn-k-point-span-length/paper/main.tex`)

What the paper claims: Place $k$ independent uniform points in a square of area $k$ and join every pair by its route in a scale-invariant random spatial network. Aldous asked for a proof that the expected total length of the union of these routes is asymptotic to $\ell k$, where $\ell$ is the mean length per unit area of the network on a unit-rate Poisson process. We prove this for the network of geodesics of the planar improper Poisson line process whose line speeds have a power-law intensity with exponent $\gamma>2$. The lower bound holds for every scale-invariant random spatial network. For the upper bound we show that all geodesics between points of the unit square lie in the disc of radius $R$ about its centre outside an event of probability $O(R^{-a})$, for every $0<a<\gamma-1$. Since $\gamma-1>1$, this and a moment bound of Kahn show that for each $\delta>0$ the expected length of the union at distance more than $\delta\sqrt k$ from the square is $O(\sqrt k)$.

Most cited in the text:

- J. Kahn, Improper Poisson line process as SIRSN in any dimension, Ann. Probab. 44 (2016), 2694--2725, 10.1214/15-AOP1032; theorem and display numbers as in 1503.03976. (cited 15 times)
- D. J. Aldous, Scale-invariant random spatial networks, Electron. J. Probab. 19 (2014), 1--41, 10.1214/EJP.v19-2920; section, display and problem numbers as in 1204.0817v1. (cited 13 times)
- W. S. Kendall, From random lines to metric spaces, Ann. Probab. 45 (2017), 469--517, 10.1214/14-AOP935; theorem numbers as in 1403.1156. (cited 6 times)
- D. J. Aldous and K. Ganesan, True scale-invariant random spatial networks, Proc. Natl. Acad. Sci. USA 110 (2013), 8782--8785, 10.1073/pnas.1304329110. (cited 1 time)


### Major roads and span length in scale-invariant random spatial networks

Folder: [sirsn-major-roads-binary-hierarchy](public/sirsn-major-roads-binary-hierarchy) (source `public/sirsn-major-roads-binary-hierarchy/paper/main.tex`)

What the paper claims: We study two of Aldous's open problems on scale-invariant random spatial networks. For his binary hierarchy model we show that almost surely the set of major roads contains every road line above a fixed height. These lines form a connected grid, so the major roads have exactly one unbounded connected component, which answers Open Problem 7 of Aldous for this model. Open Problem 9 asks under what extra assumptions the subnetwork spanning $k$ uniform points in a square of area $k$ has expected length asymptotic to $\ell k$. We show, in every such network, that this holds exactly when the part of the span far from the square has expected length $o(k)$, and that it holds when the expected length of one route outside the disc of radius $t$ about an endpoint is $o(t^{-3})$. The condition is met in the binary hierarchy model, with no extra assumption, and in the planar Poisson line network when its speed exponent exceeds $5$.

Most cited in the text:

- D. J. Aldous, Scale-invariant random spatial networks, Electron. J. Probab. 19 (2014), no. 15, 1--41, 10.1214/EJP.v19-2920; arXiv version 1204.0817, 2012, with different numbering. (cited 26 times)
- J. Kahn, Improper Poisson line process as SIRSN in any dimension, Ann. Probab. 44 (2016), 2694--2725, 10.1214/15-AOP1032, 1503.03976. (cited 7 times)
- W. S. Kendall, From random lines to metric spaces, Ann. Probab. 45 (2017), 469--517, 10.1214/14-AOP935, 1403.1156. (cited 4 times)
- G. Blanc, N. Curien and J. Kahn, Geodesics in planar Poisson roads random metric, Proc. Lond. Math. Soc. 131 (2025), no. 1, e70070, 10.1112/plms.70070, 2407.07887. (cited 3 times)


### The largest box in a sparse random allocation

Folder: [sparse-allocation-largest-box](public/sparse-allocation-largest-box) (source `public/sparse-allocation-largest-box/paper/main.tex`)

What the paper claims: Let $(Y_1,\dots,Y_n)$ be the random allocation of $m$ balls into $n$ boxes in which an allocation $(y_1,\dots,y_n)$ has probability proportional to $\prod_iw_{y_i}$, for a weight sequence $(w_k)_{k\ge0}$ with $w_0>0$, and let $Y_{(1)}$ be the largest of the $Y_i$. Janson conjectured that $Y_{(1)}=o_p(\log n)$ when $m/n\to0$, provided the generating function of the weights has a positive radius of convergence. We prove an explicit tail bound for $Y_{(1)}$, valid for all $n\ge4$ and $1\le m\le cn$ with $c>0$ depending only on the weights, and deduce that $Y_{(1)}\le C+(1+o(1))\,a\log n/\log(n/m)$ with probability tending to one, where $a$ is the smallest $k\ge1$ with $w_k>0$ and $C$ depends only on the set of $k$ with $w_k>0$. This proves the conjecture. For the weights $w_k=1$ the bound is sharp: $Y_{(1)}\log(n/m)/\log n\to1$ in probability when $\log(n/m)=o(\log n)$.

Most cited in the text:

- S. Janson, Simply generated trees, conditioned Galton--Watson trees, random allocations and condensation, Probab. Surv. 9 (2012), 103--252. (cited 9 times)
- V. F. Kolchin, B. A. Sevast'yanov and V. P. Chistyakov, Random Allocations, V. H. Winston & Sons, Washington, D.C., 1978. (cited 3 times)
- Yu. L. Pavlov, Random Forests, VSP, Zeist, 2000. (cited 2 times)
- N. I. Kazimirov, On some conditions for absence of a giant component in the generalized allocation scheme, Discrete Math. Appl. 12 (2002), no. 3, 291--302. (cited 1 time)


### Poisson limits for large boxes in sparse random allocations

Folder: [sparse-allocation-poisson-limits](public/sparse-allocation-poisson-limits) (source `public/sparse-allocation-poisson-limits/paper/main.tex`)

What the paper claims: Let $(Y_1,\dots,Y_n)$ be the random allocation of $m$ balls into $n$ boxes in which an allocation $(y_1,\dots,y_n)$ has probability proportional to $\prod_iw_{y_i}$, and let $\xi_1,\dots,\xi_n$ be independent with $\Pp(\xi_i=k)$ proportional to $w_k\tau^k$, where $\tau$ is chosen so that $\E\xi_i=m/n$. Janson showed that when $m/n$ converges to a positive limit below a threshold determined by the weights, the numbers of boxes with many balls are asymptotically Poisson and the largest boxes of the allocation are close in distribution to the largest of $\xi_1,\dots,\xi_n$, and he asked whether the same holds when $m/n\to0$. Let $a$ be the least $k\ge1$ with $w_k>0$. The answer is positive for every sequence with $m\to\infty$ if every $k$ with $w_k>0$ is a multiple of $a$, for instance if $w_1>0$, and it is negative along every sequence on which $m$ is bounded. If some $k$ with $w_k>0$ is not a multiple of $a$, there are sequences with $m\to\infty$ and $m/n\to0$ along which the answer is negative. When the least such $k$, say $b$, is coprime to $a$, we characterize the sequences along which the answer is positive in terms of $n\Pp(\xi_1=b)$ and the residue of $m$ modulo $a$; when $n\Pp(\xi_1=b)$ has a positive finite limit, the number of boxes with at least $b$ balls converges to a Poisson distribution conditioned on a residue class. The proofs rest on an exact formula for the joint law of the boxes whose sizes are neither $0$ nor $a$ and on a local limit theorem for the binomial distribution with explicit constants.

Most cited in the text:

- S. Janson, Simply generated trees, conditioned Galton--Watson trees, random allocations and condensation, Probab. Surv. 9 (2012), 103--252. (cited 16 times)
- A. Chuprunov and I. Fazekas, Poisson limit theorems for the generalized allocation scheme, Annales Univ. Sci. Budapest., Sect. Comp. 49 (2019), 77--96. (cited 3 times)
- A. V. Kolchin, Limit theorems for a generalized allocation scheme, Diskret. Mat. 15 (2003), no. 4, 148--157 (Russian); English transl., Discrete Math. Appl. 13 (2003), no. 6, 627--636. (cited 2 times)
- A. D. Barbour, L. Holst and S. Janson, Poisson Approximation, Oxford University Press, Oxford, 1992. (cited 1 time)


### Opposite gaps defeat large-time unimodality for one-sided stable processes

Folder: [stable-unimodality-opposite-gaps](public/stable-unimodality-opposite-gaps) (source `public/stable-unimodality-opposite-gaps/paper/main.tex`)

What the paper claims: Hasebe and Ueda conjectured that if $S_t$ (resp. $T_t$) is the law at time $t$ of a classical (resp. free) strictly $\alpha$-stable process and the initial law $\mu$ has a finite absolute moment of order $2+\alpha$, then $\mu*S_t$ (resp. $\mu\bp T_t$) is unimodal for all large $t$. We show that this fails for every $\alpha\in(0,1)$ in both settings, for the stable laws concentrated on the positive half-line. There is one probability measure $\mu_\ast$, with $\int e^{\lambda|x|}\,d\mu_\ast(x)<\infty$ for every $\lambda>0$, such that $\mu_\ast*S^{(\alpha)}_t$ and $\mu_\ast\bp T^{(\alpha)}_t$ are not unimodal for any $\alpha\in(0,1)$ and any $t>0$. Its atoms run to $-\infty$, against the direction of the kernel, with gaps tending to infinity. In the classical case the convolution density is strictly decreasing on intervals arbitrarily far to the left; in the free case the density of the free convolution vanishes on an interval lying between two points where it is positive, which we read off from the Huang--Wang description of the support of a free convolution with a freely infinitely divisible law.

Most cited in the text:

- T. Hasebe and Y. Ueda, Large time unimodality for classical and free Brownian motions with initial distributions, ALEA Lat. Am. J. Probab. Math. Stat. 15 (2018), 353--374. (cited 11 times)
- H.-W. Huang and J.-C. Wang, Regularity results for free Levy processes, arXiv:2203.00421 (2022). (cited 6 times)
- T. Hasebe and A. Kuznetsov, On free stable distributions, Electron. Commun. Probab. 19 (2014), no. 56, 1--12. (cited 3 times)
- H. Bercovici and D. Voiculescu, Free convolution of measures with unbounded support, Indiana Univ. Math. J. 42 (1993), 733--773. (cited 2 times)


### The stationary cover time of reversible chains on three and four states

Folder: [stationary-cover-time-four-states](public/stationary-cover-time-four-states) (source `public/stationary-cover-time-four-states/paper/main.tex`)

What the paper claims: Aldous and Fill asked whether every reversible Markov chain on $n$ states, started from its stationary law, has expected cover time at least $(n-1)H_{n-1}$, the value for the simple random walk on the complete graph $K_n$. We prove this for $n=3$ and $n=4$, for all reversible chains including those with holding, and show that equality holds only for the simple random walk on $K_n$. The case $n=3$ reduces to Schur's inequality. The case $n=4$ rests on an explicit polynomial identity of degree $16$ whose numerator becomes coefficientwise nonnegative after an ordered substitution on each of $30$ cones of edge orderings. Holding is handled for every $n$ by an occupation identity: if a chain without holding satisfies the bound and $E_iC\ge (n-1)H_{n-1}/2$ for every state $i$, then the bound survives any added holding. This pointwise condition holds for $n\le 4$.

Most cited in the text:

- D. Aldous, J. A. Fill, Reversible Markov Chains and Random Walks on Graphs, unfinished monograph, recompiled 2014, https://www.stat.berkeley.edu/ aldous/RWG/book.html. (cited 2 times)
- D. J. Aldous, Lower bounds for covering times for reversible Markov chains and random walks on graphs, J. Theoret. Probab. 2 (1989), 91--100, doi:10.1007/BF01048272. (cited 1 time)
- U. Feige, A tight lower bound on the cover time for random walks on graphs, Random Structures Algorithms 6 (1995), 433--438, doi:10.1002/rsa.3240060406. (cited 1 time)
- P. Matthews, Covering problems for Markov chains, Ann. Probab. 16 (1988), 1215--1228, doi:10.1214/aop/1176991686. (cited 1 time)


### Fixed points of strictly non-Volterra quadratic stochastic operators in four or more types

Folder: [strictly-nonvolterra-qso-fixed-points](public/strictly-nonvolterra-qso-fixed-points) (source `public/strictly-nonvolterra-qso-fixed-points/paper/qso_fixed_points.tex`)

What the paper claims: A quadratic stochastic operator on the simplex of probability vectors on $m$ types is strictly non-Volterra when a pair of parents of types $i$ and $j$ never produces an offspring of type $i$ or $j$. For $m=3$, Rozikov and Zhamilov proved that every such operator has a unique fixed point, that it is not attractive, and that the operator has $2$-cycles and $3$-cycles depending on the parameters; Problem 11 of the 2009 list of open problems on quadratic stochastic operators by Ganikhodzhaev and Rozikov asks whether this holds for $m\ge4$. We settle both clauses about the fixed point. Non-attractiveness fails from $m=4$ on, by the globally attracting equiprobable operators of Jamilov, Ladra and Mukhitdinov. Uniqueness fails from $m=5$ on: a five-type operator with the two fixed points $(\frac13,\frac13,\frac13,0,0)$ and $(\frac19,\frac19,\frac19,\frac13,\frac13)$ was studied by Jamilov in 2017, and we show that it is the simplest member of a family, obtained from any three-type operator by adjoining two types that swap, in which the number of fixed points is always exactly two; for $m\ge6$ any operator with two disjoint invariant triples of types has at least two fixed points, and a six-type example carries a whole segment of them. At $m=4$ the fixed point is unique: two fixed points would differ on exactly two positive and two negative coordinates, and the mass transferred across such a cut is contracted by twice the largest coordinate, which at a fixed point is at most $3-\sqrt5<1$. So the uniqueness clause of the theorem holds exactly for $m\in\{3,4\}$ and the non-attractiveness clause exactly for $m=3$. We explain why the constructions stop at four types, and give a fixed-point index count that yields a one-paragraph proof of uniqueness for three types and shows that the four-type fixed point has positive determinant $\det(I-DV|_T)$. The finite verifications are carried out in exact arithmetic, and both they and the four-type theorem are checked in Lean 4.

Most cited in the text:

- U. U. Jamilov, Dynamics of a strictly non-Volterra quadratic stochastic operator on $S^4$, Uzbek Math. J. 2017, no. 2, 66--75. (cited 7 times)
- R. N. Ganikhodzhaev and U. A. Rozikov, Quadratic stochastic operators: results and open problems, arXiv:0902.4207 (2009). (cited 4 times)
- U. U. Jamilov, M. Ladra and R. T. Mukhitdinov, On the equiprobable strictly non-Volterra quadratic stochastic operators, Qual. Theory Dyn. Syst. 16 (2017), 645--655. (cited 2 times)
- U. U. Jamilov, On symmetric strictly non-Volterra quadratic stochastic operators, Discontinuity, Nonlinearity, and Complexity 5 (2016), 263--283. (cited 2 times)


### The local limit of sublinear preferential attachment graphs with fixed out-degree

Folder: [sublinear-attachment-local-limit](public/sublinear-attachment-local-limit) (source `public/sublinear-attachment-local-limit/sublinear_attachment.tex`)

What the paper claims: We consider the preferential attachment graph in which every new vertex sends $m\ge2$ edges to the existing vertices, the endpoints being chosen one after another with probability proportional to $f(\text{in-degree})$, where the attachment function $f$ is bounded away from zero, has bounded increments and satisfies $f(k)/k\to0$. No monotonicity or concavity is assumed. We prove that the total weight of the first $n$ vertices divided by $n$ converges almost surely to the unique solution $c_f$ of an explicit scalar equation, that the empirical in-degree distribution converges almost surely to the law of a pure birth process with rates $mf(k)/c_f$ observed at an independent exponential time, and that the graph converges locally in probability to an infinite random tree. The probability of every finite ball in the limit is given by an explicit integral over the ages of its vertices. This answers, for this class of attachment functions, a question of Deijfen and van der Hofstad on local limits beyond the affine case when the out-degree is fixed.

Most cited in the text:

- J. Choi, S. Sethuraman and S. C. Venkataramani, A scaling limit for the degree distribution in sublinear preferential attachment schemes, Random Structures Algorithms 48 (2016), 703--731; arXiv:1402.4088. (cited 3 times)
- G. Aletti, A. Collevecchio, I. Crimaldi, M. Deijfen, S. Dereich, A. Ghiglietti, R. van der Hofstad, M. Holmes, D. Kious, V. Kleptsyn, B. Lodewijks, P. Morters and B. Schapira, Open problems in stochastic reinforcement models, in 2023 MATRIX (cited 2 times)
- P. L. Krapivsky, S. Redner and F. Leyvraz, Connectivity of growing random networks, Phys. Rev. Lett. 85 (2000), 4629--4632. (cited 2 times)
- A. Rudas, B. Toth and B. Valko, Random trees and general branching processes, Random Structures Algorithms 31 (2007), 186--202. (cited 2 times)


### Supermodular ordering of speeded-up Markov chains without stochastic monotonicity

Folder: [supermodular-speed-ordering](public/supermodular-speed-ordering) (source `public/supermodular-speed-ordering/paper/main.tex`)

What the paper claims: For a stationary continuous-time Markov chain $\lambda$ with real values, let $\lambda_c(t)=\lambda(ct)$. Leskela asked whether there is a stationary ergodic chain that is not stochastically monotone but satisfies $\lambda_{c_1}\ge_\sm\lambda_{c_2}$ whenever $c_1\le c_2$, where $\ge_\sm$ is the supermodular order of processes. We show that such chains exist on three states. If $\lambda$ jumps from its smallest value to each of the other two values at arbitrary positive rates and returns from both of them at a common rate, then $\lambda_{c_1}\ge_\sm\lambda_{c_2}$ for all $c_1\le c_2$, while $\lambda$ is not stochastically monotone. The proof reduces monotonicity in each sampling gap to two finite inequalities for the conditional expectations of the test function, and proves them with a coupling and an explicit decomposition into elementary increasing differences. If the largest value returns faster than the middle one, the ordering fails already for the pairs $(\lambda(0),\lambda(t))$. For reversible three-state chains with two distinct nonzero eigenvalues, these pairs decrease in the supermodular order if and only if the slow left eigenvector does not have the same strict sign at the two extreme states, and computations suggest that this condition characterizes the ordering of the whole process.

Most cited in the text:

- N. Bauerle and T. Rolski, A monotonicity result for the workload in Markov-modulated queues, J. Appl. Probab. 35 (1998), 741--747. (cited 6 times)
- L. Leskela, Ross's second conjecture and supermodular stochastic ordering, Queueing Syst. 100 (2022), 213--215. (cited 2 times)
- S. M. Ross, Average delay in queues with non-stationary Poisson arrivals, J. Appl. Probab. 15 (1978), 602--609. (cited 2 times)
- C.-S. Chang, X. Chao and M. Pinedo, Monotonicity results for queues with doubly stochastic Poisson arrivals: Ross's conjecture, Adv. in Appl. Probab. 23 (1991), 210--228. (cited 1 time)


### Slabs are more noise stable than balls at large Gaussian measure, for every correlation

Folder: [symmetric-gaussian-noise-stability-slabs](public/symmetric-gaussian-noise-stability-slabs) (source `public/symmetric-gaussian-noise-stability-slabs/paper/main.tex`)

What the paper claims: Among symmetric subsets of $\R^n$ of prescribed Gaussian measure, which one maximizes the probability that two $\rho$-correlated standard Gaussian vectors both lie in the set? A centred ball or its complement was suggested, and Heilman showed that this fails in the plane to second order at $\rho=0$. We show that it fails for every $\rho\in(0,1)$ and every $n\ge2$: at measure close to $1$ the slab $\{|x_1|\le t\}$ is strictly more noise stable than every cylinder $B^k\times\R^{n-k}$ with $k\ge2$ and every cylinder complement, and at measure close to $0$ the complement of the slab wins. Computations in dimensions one, two and six are consistent with cylinders and their complements being the optimal sets.

Most cited in the text:

- S. Heilman, Low correlation noise stability of symmetric sets, J. Theoret. Probab. 34 (2021), no. 4, 2192--2240, 10.1007/s10959-020-01031-y; 1511.00382. (cited 4 times)
- G. Baker, Symmetric Gaussian Rearrangement with Applications to Gaussian Noise Stability, MSc thesis, Queen's University, 2018. (cited 2 times)
- F. Barthe, An isoperimetric result for the Gaussian measure and unconditional sets, Bull. London Math. Soc. 33 (2001), no. 4, 408--416, 10.1017/S0024609301008141. (cited 2 times)
- T. W. Anderson, The integral of a symmetric unimodal function over a symmetric convex set and some probability inequalities, Proc. Amer. Math. Soc. 6 (1955), no. 2, 170--176, 10.2307/2032333. (cited 1 time)


### Three problems in kernel methods: proofs and finite-size measurements

Folder: [three-problems-in-kernel-methods](public/three-problems-in-kernel-methods) (source `public/three-problems-in-kernel-methods/paper/kernel_open_problems_numerics.tex`)

What the paper claims: Three questions about kernel methods are answered here, and a fourth is measured. For the Gaussian kernel with a fixed bandwidth on the sphere, the minimum-norm interpolant of noisy labels is benign along the sequence $d_\ell=2^{2^\ell}$, $n_\ell=2^{2^{2\ell}}$: its excess risk tends to zero in probability, and almost surely along the sequence, for every fixed-degree spherical-polynomial target (Theorem ). At the exponential sample size $n=2^d$ the same interpolant is obstructed: the expected excess risk on pure noise is at least $\frac5{36}\sigma^2$ in the limit, for every fixed bandwidth (Theorem ). For ridge regression on two augmented views of each sample through a random feature map with an odd activation, the optimised objective and the clean prediction risk have the same limits in law as those of a correlated Gaussian surrogate that keeps the shared latent variable of the two views (Theorem ); the proof rests on an exact Gaussianisation of each block conditional on the feature matrix. The hard edge of the degree-two Veronese matrix remains open; the two lemmas that stand between its reduction and the hard edge are measured, and the measurements point to a sharper statement, that the leave-one-out normal has a semicircular spectrum. The proofs are accompanied by finite-size measurements of the quantities they turn on: the leverage certificate of the lower bound, the harmonic dimension gap that separates the benign regime from the obstructed one, and the leverage concentration behind the equivalence. Two further results are evaluated on data: an exact same-sample risk identity for a kernel correction fitted on top of a learned mean, on the EMIT and OCO-2 radiative-transfer emulation corpora, where its sign depends on the component being emulated and the correction fitted to out-of-fold residuals gains nothing; and the compressed-resolvent hypothesis behind growing-rank spiked singular vectors, whose compression error along rays of fixed rank-to-size ratio approaches $\sqrt{r/n}$ plus a term of order $r/n$.

Most cited in the text:

- ProofNet24 run reports, tracks P15 (kernel mean correction), P19 (kernel spectral pruning), P20 (kernel hard edge), P21 (correlated Gaussian equivalence), P22 (benign overfitting) and P23 (kernel obstruction), private repository, directory  (cited 14 times)
- K. Atkinson and W. Han, Spherical Harmonics and Approximations on the Unit Sphere: An Introduction, Lecture Notes in Mathematics 2044, Springer, 2012. (cited 4 times)
- H. Cui, B. Loureiro, F. Krzakala and L. Zdeborova, Generalization error rates in kernel regression: the crossover from the noiseless to noisy regime, in Advances in Neural Information Processing Systems 34 (2021), 10131--10143. arXiv:2105.1 (cited 4 times)
- F. Benaych-Georges and R. R. Nadakuditi, The singular values and vectors of low rank perturbations of large rectangular random matrices, J. Multivariate Anal. 111 (2012), 120--135. (cited 3 times)


### Exact higher moments of the limiting spectral distributions of random Toeplitz and Hankel matrices

Folder: [toeplitz-hankel-exact-moments](public/toeplitz-hankel-exact-moments) (source `public/toeplitz-hankel-exact-moments/paper/paper.tex`)

What the paper claims: The limiting spectral distributions $\gT$ and $\gH$ of random symmetric Toeplitz and Hankel matrices (Bryc--Dembo--Jiang, Ann. Probab. 34 (2006); Hammond--Miller, J. Theoret. Probab. 18 (2005)) have been known to exist for two decades, yet remain unidentified; their explicitly published moments stop at order eight. We compute the moments exactly through order $14$ for both ensembles, in exact rational arithmetic: $m_{10}(\gT)=415$, $m_{12}(\gT)=23840/7$, $m_{14}(\gT)=325719/10$, $m_{10}(\gH)=2717/36$, $m_{12}(\gH)=1052/3$, $m_{14}(\gH)=1331087/720$. The computation also yields $m_8(\gT)=908/15$, correcting the value $964/15$ reported by Hammond--Miller. Each moment is a sum of volumes of explicit rational polytopes indexed by pair partitions; we evaluate every volume exactly by a double-description/triangulation engine and check the results against an independent vertex enumeration, Monte Carlo integration, direct eigenvalue simulation, an exact counting route, and all previously published values. We further prove a sharp structural theorem: a pairing has volume $1$ if and only if it is non-crossing, and every crossing pairing has volume at most $2/3$ --- attained in the Toeplitz case --- in both ensembles; consequently $m_{2k}(\gT)\le \Cat_k+\tfrac23\big((2k-1)!!-\Cat_k\big)$ and $m_{2k}(\gH)\le \Cat_k+\tfrac23\big(k!-\Cat_k\big)$. The complete volume spectra are tabulated, in the paper and in the accompanying repository; they are supported on a small set of rational values, shared across the two ensembles. We close with two numerical observations: the Gaussian-deficit ratios of $\gT$ trend toward the square of the Sen--Virag spectral-norm constant, and the analogous Hankel ratios suggest a value for the (open) Hankel norm constant.

Most cited in the text:

- C. Hammond, S. J. Miller, Distribution of eigenvalues for the ensemble of real symmetric Toeplitz matrices, J. Theoret. Probab. 18 (2005), 537--566. (cited 8 times)
- W. Bryc, A. Dembo, T. Jiang, Spectral measure of large random Hankel, Markov and Toeplitz matrices, Ann. Probab. 34 (2006), 1--38. (cited 6 times)
- A. Sen, B. Virag, The top eigenvalue of the random Toeplitz matrix and the sine kernel, Ann. Probab. 41 (2013), 4050--4079. (cited 2 times)
- Z. D. Bai, Methodologies in spectral analysis of large dimensional random matrices, a review, Statist. Sinica 9 (1999), 611--677. (cited 1 time)


### Dead branches in the trace-reinforced ant process

Folder: [trace-reinforced-ants-dead-branches](public/trace-reinforced-ants-dead-branches) (source `public/trace-reinforced-ants-dead-branches/dead_branches.tex`)

What the paper claims: In the trace-reinforced ant process of Kious, Mailler and Schapira, ants walk one after another from a nest $N$ to a food source $F$ on a finite graph, and each ant adds one unit of weight to every edge it has crossed. It was conjectured that the normalised weights converge to a deterministic limit, and that this limit is positive on every edge as soon as $N$ and $F$ are at distance at least two. We show that the second statement fails. If a part of the graph hangs by a single edge from a neighbour of $F$, on the side away from $N$, then the normalised weights of all its edges tend to zero almost surely; this happens in $2$-connected graphs with $N$ and $F$ at distance two. We also show that the mean-field vector field has no equilibrium with all coordinates positive when some neighbour of $F$ is hidden from $N$ by the other neighbours of $F$, so that on such graphs, some of which are $3$-connected, the normalised weights cannot converge to a positive limit. The equilibria are described through the voltage of the unit current from $N$ to $F$. A census of the $22{,}828$ cases on connected graphs with at most seven vertices supports a corrected form of the conjecture, in which the set of edges with limit zero is given by an explicit combinatorial rule. We also give the equilibrium on a graph made of any number of parallel paths.

Most cited in the text:

- D. Kious, C. Mailler and B. Schapira, The trace-reinforced ants process does not find shortest paths, J. Ec. polytech. Math. 9 (2022), 505--536; arXiv:2106.10559. (cited 8 times)
- D. Kious, C. Mailler and B. Schapira, Finding geodesics on graphs using reinforcement learning, Ann. Appl. Probab. 32 (2022), no. 5, 3889--3929; arXiv:2010.04820. (cited 3 times)
- W. Armfield and C. Mailler, The forward-loop-erased ants walk, arXiv:2610.18453. (cited 2 times)
- G. Aletti, A. Collevecchio, I. Crimaldi, M. Deijfen, S. Dereich, A. Ghiglietti, R. van der Hofstad, M. Holmes, D. Kious, V. Kleptsyn, B. Lodewijks, P. Morters and B. Schapira, Open problems in stochastic reinforcement models, in 2023 MATRIX (cited 1 time)


### Frozen edges of stationary tridiagonal dynamics with GUE spectra

Folder: [tridiagonal-edge-freezing](public/tridiagonal-edge-freezing) (source `public/tridiagonal-edge-freezing/paper/main.tex`)

What the paper claims: Virag asked whether matrix-valued Brownian motion has an operator limit. A natural candidate is a stationary diffusion on tridiagonal matrices with the Dumitriu--Edelman law of the Gaussian unitary ensemble (GUE) at every time. We show that the simplest such diffusion, with independent Ornstein--Uhlenbeck diagonal entries and independent radial Ornstein--Uhlenbeck off-diagonal entries, has frozen edge eigenvalues on the time scale on which Dyson Brownian motion moves. For each fixed $k$ the $k$ largest edge-scaled eigenvalues converge, uniformly on compact time intervals, to a vector that does not depend on time, so they do not converge to the Airy line ensemble. The same holds for every stationary reversible tridiagonal diffusion with this invariant law whose entry noise is bounded uniformly in the dimension. An exact tridiagonal realization of Dyson Brownian motion with these marginals needs entry noise that grows with the dimension. Virag's question remains open.

Most cited in the text:

- I. Corwin and A. Hammond, Brownian Gibbs property for Airy line ensembles, Invent. Math. 195 (2014), 441--508. 10.1007/s00222-013-0462-3 (cited 3 times)
- A. Edelman, S. Jeong and R. Nissim, On the limit of the tridiagonal model for $$-Dyson Brownian motion, preprint, 2024, revised 2026. 2411.01633 (cited 3 times)
- I. Dumitriu and A. Edelman, Matrix models for beta ensembles, J. Math. Phys. 43 (2002), 5830--5847. 10.1063/1.1507823 (cited 2 times)
- B. Virag, Operator limits of random matrices, in Proceedings of the International Congress of Mathematicians, Seoul 2014, Vol. 4, 247--272. 1804.06953 (cited 2 times)


### Pair meeting times can concentrate while coalescence is slow

Folder: [two-site-trap-coalescence](public/two-site-trap-coalescence) (source `public/two-site-trap-coalescence/main.tex`)

What the paper claims: For coalescing random walks driven by a chain with uniform stationary law, Aldous asked what conditions, beyond concentration of the mean meeting times of pairs from independent uniform starts, give a mean coalescence time asymptotic to twice the stationary mean meeting time $\tau$. We study a weighted complete graph on $m$ vertices joined to a two-vertex trap with scale $r\to\infty$. The pair means concentrate exactly when $r=o(m)$, and in every fixed $L^p$ exactly when $r=m^{o(1)}$. Then $\tau\sim m$, while the coalescence time divided by $2mr$ tends to a mean-one exponential law in Wasserstein distance, with all moments. With $r=\log m$ the ratio of the mean coalescence time to $2\tau$ grows like $\log m$. Both stages of the plan Aldous proposed hold; the hand-off between them fails, because once few walkers remain, one of them sits in the trap. The worst-start mixing time is at least of order $mr$, much larger than $\tau$.

Most cited in the text:

- R. I. Oliveira, Mean field conditions for coalescing random walks, Ann. Probab. 41 (2013), 3420--3461. (cited 5 times)
- D. Aldous, Interacting particle systems as stochastic social dynamics, Bernoulli 19 (2013), 1122--1149; arXiv:1309.6766. (cited 4 times)
- J. Hermon, Some inequalities for reversible Markov chains and branching random walks via spectral optimization, arXiv:1908.08525. (cited 3 times)
- D. Aldous and J. A. Fill, Reversible Markov Chains and Random Walks on Graphs, unfinished monograph, 2002, recompiled 2014, https://www.stat.berkeley.edu/ aldous/RWG/book.html. (cited 2 times)


### Uniform condensation windows for zero-radius random allocations

Folder: [uniform-condensation-windows](public/uniform-condensation-windows) (source `public/uniform-condensation-windows/main.tex`)

What the paper claims: For any fixed nonnegative weight sequence with positive constant term and zero radius of convergence, we prove the existence of arbitrarily large intervals of total masses on which a single box carries almost all the mass, uniformly over the number of boxes at densities in a compact subset of $(0,\infty)$. Consequently every admissible full mass path of positive finite limiting density has a subsequence exhibiting complete condensation. This answers the zero-radius question in Janson's survey (Problem 19.41 in the published version, Problem 18.40 in the preprint). The argument preserves the small-box partition factor by an exact occupation-count insertion. A deterministic record-margin estimate then provides a uniform finite-size probability bound. We also show that multiplicative density of a sampled index set is necessary and sufficient for a universal subsequence-condensation statement.

Most cited in the text:

- S. Janson, Simply generated trees, conditioned Galton--Watson trees, random allocations and condensation, Probability Surveys 9 (2012), 103--252. https://doi.org/10.1214/11-PS188doi:10.1214/11-PS188. (cited 11 times)
- S. Janson, Simply generated trees, conditioned Galton--Watson trees, random allocations and condensation, preprint, December 2011. https://arxiv.org/abs/1112.0510v1arXiv:1112.0510v1. Numbering differs from the published version. (cited 4 times)
- S. Janson, T. Jonsson and S. O. Stefansson, Random trees with superexponential branching weights, Journal of Physics A: Mathematical and Theoretical 44 (2011), 485002. https://arxiv.org/abs/1104.2810arXiv:1104.2810. (cited 3 times)
- S. Grosskinsky, G. M. Schutz and H. Spohn, Condensation in the zero range process: stationary and dynamical properties, Journal of Statistical Physics 113 (2003), 389--410. https://arxiv.org/abs/cond-mat/0302079arXiv:cond-mat/0302079. (cited 1 time)


### On a contractivity question of Neri and Pinto for generalized Polya urns

Folder: [urn-euclidean-contractivity](public/urn-euclidean-contractivity) (source `public/urn-euclidean-contractivity/paper/main.tex`)

What the paper claims: Let $R$ be the replacement matrix of a balanced $d$-colour generalized Polya urn with balance $\lambda$. Neri and Pinto obtained quantitative rates in the strong law $U(n)/T(n)\to u$ whenever the quadratic form $w\mapsto\langle w(R-\lambda I),w\rangle$, restricted to vectors with coordinate sum zero, is negative definite for the Euclidean inner product on all $d$ coordinates or on the first $d-1$ of them, and they asked whether this holds for every tenable irreducible urn. We show that it holds for every irreducible urn with two colours and fails for some urn with nonnegative integer entries for every $d\ge 3$, simultaneously for both inner products and for every ordering of the colours. One of the examples has all non-principal eigenvalues of real part below $\lambda/2$. On the other hand, the Lyapunov equation on the sum-zero hyperplane gives, for every tenable irreducible urn, an inner product in which the form is negative definite, and the best constant obtainable in this way is $\lambda-\gamma$, where $\gamma$ is the largest real part of a non-principal eigenvalue of $R$. Consequently the general rate theorem of Neri and Pinto applies to every tenable irreducible urn, and their fast-rate theorem applies with such an inner product exactly when $\gamma<\lambda/2$.

Most cited in the text:

- M. Neri and P. Pinto, Quantitative limit theorems for generalized Polya urns with applications to random tree models, arXiv:2607.07309 (2026). (cited 21 times)
- K. B. Athreya and S. Karlin, Embedding of urn schemes into continuous time Markov branching processes and related limit theorems, Ann. Math. Statist. 39 (1968), 1801--1817. (cited 2 times)
- S. Janson, Functional limit theorems for multitype branching processes and generalized Polya urns, Stochastic Process. Appl. 110 (2004), 177--245. (cited 2 times)
- Z.-D. Bai and F. Hu, Asymptotics in randomized urn models, Ann. Appl. Probab. 15 (2005), 914--940. (cited 1 time)


### The variation threshold, Kemeny's constant and stationary times of reversible Markov chains

Folder: [variation-threshold-stationary-times](public/variation-threshold-stationary-times) (source `public/variation-threshold-stationary-times/paper/main.tex`)

What the paper claims: For finite reversible Markov chains, Aldous and Fill asked whether the variation threshold $\tau_1$ is at most the average hitting time $\tau_0$ (Kemeny's constant), and whether the relaxation time $\tau_2$ is at most $\tau_1^{(2)}$, the largest over initial states of the least mean of a stopping time at which the chain has its stationary distribution. The answer to the first question is no: a birth and death chain on three states with a strong drift has $\tau_1>\tau_0$, and on the analogous chains with $k+1$ states the ratio $\tau_1/\tau_0$ tends to $t_k/k$ as the drift grows, where $t_k$ is the point at which the survival function of the Gamma$(k,1)$ distribution equals $e^{-1}$; for $k=4$ this limit is $1.0879\ldots$. The answer to the second question is yes, in continuous and in discrete time.

Most cited in the text:

- D. Aldous and J. A. Fill, Reversible Markov Chains and Random Walks on Graphs, unfinished monograph, 2002, recompiled version 2014, https://www.stat.berkeley.edu/ aldous/RWG/book.pdf. (cited 15 times)
- D. J. Aldous, Some inequalities for reversible Markov chains, J. London Math. Soc. (2) 25 (1982), 564--576. (cited 1 time)
- J. Hermon, Relaxation times are stationary hitting times of large sets, preprint, 2023, arXiv:2304.05878. (cited 1 time)
- J. G. Kemeny and J. L. Snell, Finite Markov Chains, University Series in Undergraduate Mathematics, Van Nostrand, Princeton, 1960. (cited 1 time)
