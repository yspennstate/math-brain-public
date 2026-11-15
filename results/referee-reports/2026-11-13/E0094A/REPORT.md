PARTIAL

# Adding one generator or one edge to accelerate a random walk

Theorem 1 gives the universal obstruction for E0094. Theorem 2 gives an explicit added generator with mixing time $O(n\log^3 n)$, improving the original $\Theta(n^3\log n)$ by a power of $n$. Consequently the optimal polynomial exponent is one, but the optimal order, including logarithmic factors, is not determined here:
$$
 \Omega(n\log n)\ \le\ \inf_{\sigma\in S_n}t_{\mathrm{mix}}(\varepsilon)
 \ \le\ O\bigl(n\log^2 n[\log n+\log(1/\varepsilon)]\bigr).
$$
Here and below fixed-error assertions mean fixed $0<\varepsilon<1$.

For E0095, an antipodal chord is exactly optimal on an even cycle for the ordinary random-walk gap; its addition preserves the original gap. This result already appears in the author's November 2026 preprint and is attributed below. The order of the best perfect matching is already settled in print, even for arbitrary bounded-degree connected base graphs, by Hermon–Sly–Sousi (2022). Theorem 5 supplies a general obstruction to improvement by a single edge, and Proposition 7 disproves the proposed Fiedler-extrema rule with a certified ten-vertex cubic example. The exact optimizing edge or matching for a general finite regular graph is not characterized.

## Literature and scope

The source is P. Diaconis, *Some things we've learned (about Markov chain Monte Carlo)*, Bernoulli **19** (2013), 1294–1305, Questions 3 and 4 on PDF p. 9, [arXiv:1309.7754](https://arxiv.org/abs/1309.7754). *The Markov chain Monte Carlo revolution* is a different Diaconis article. The question numbers used here refer to the 2013 paper.

The following sources were checked before the proofs and computations.

| Source | Relevant conclusion and limitation |
|---|---|
| Diaconis–Saloff-Coste, *Comparison techniques for random walk on finite groups*, Ann. Probab. **21** (1993), 2131–2156, [paper](https://www2.stat.duke.edu/~scs/Courses/Stat376/Papers/ConvergeRates/DiaconisSCosteCompareAAP1993.pdf) | Supplies the Dirichlet-form and eigenvalue comparison used below; treats the original cycle-and-transposition walk. |
| Wilson, *Mixing time of the Rudvalis shuffle*, Electron. Commun. Probab. **8** (2003), 77–85, [arXiv:math/0210469](https://arxiv.org/abs/math/0210469) | Establishes matching lower bounds for the symmetrized cycle-and-transposition model and two related shuffles. |
| Hildebrand, *A survey of results on random random walks on finite groups*, Probab. Surveys **2** (2005), 33–63, [paper](https://arxiv.org/abs/math/0401189) | Concerns random choices of driving permutations; it does not identify an optimal addition to the fixed pair in E0094. |
| Helfgott–Seress–Żuk, *Random generators of the symmetric group: diameter, mixing time and spectral gap*, J. Algebra **421** (2015), 349–368, [paper](https://arxiv.org/abs/1311.6742) | Gives $O(n^3(\log n)^C)$ mixing for a random generating pair, rather than an optimal augmentation of the prescribed pair. |
| Babai–Kantor–Lubotzky, *Small-diameter Cayley graphs for finite simple groups*, European J. Combin. **10** (1989), 507–522, §2, [paper](https://pages.uoregon.edu/kantor/PAPERS/BKL.pdf) | Uses binary affine maps to obtain short transpositions for other small generating sets. This is prior art for the binary-word method, not a mixing theorem for the exact fixed pair here. |
| Bollobás–Chung, *The diameter of a cycle plus a random matching*, SIAM J. Discrete Math. **1** (1988), 328–333, [paper](https://fanchung.ucsd.edu/mypaps/fanpap/104cyclematch.pdf) | Establishes near-optimal diameter. Diameter alone does not establish a constant spectral gap. |
| Friedman, *A proof of Alon's second eigenvalue conjecture and related problems*, Mem. Amer. Math. Soc. **195** (2008), no. 910, [paper](https://arxiv.org/abs/cs/0405020) | Establishes asymptotically optimal spectral bounds for several random regular graph models. Applying a theorem about an unspecified regular-graph model directly to a fixed cycle plus matching would require a model-transfer argument. |
| Hermon–Sly–Sousi, *Universality of cutoff for graphs with an added random matching*, Ann. Probab. **50** (2022), 203–240, Theorem 1.1 and Proposition 1.2, [paper](https://doi.org/10.1214/21-AOP1532), [preprint](https://arxiv.org/abs/2008.08564) | Settles the matching-order question for bounded-degree base graphs: logarithmic mixing, cutoff, and a constant absolute gap with high probability. This part is treated as settled, with no claim of a new solution. |
| Ghosh–Boyd, *Growing well-connected graphs*, CDC 2006, 6605–6611, [paper](https://web.stanford.edu/~boyd/papers/growing_fast_graphs.html) | The Fiedler-vector selection rule is a heuristic for algebraic connectivity, not an exact finite-edge theorem. |
| Mosk-Aoyama, *Maximum algebraic connectivity augmentation is NP-hard*, Oper. Res. Lett. **36** (2008), 677–679, [paper](https://cs.stanford.edu/people/damonma/papers/algconnaug.pdf) | Hardness concerns a variable budget of edges and the combinatorial Laplacian. It does not make a single-edge search NP-hard and does not identify the ordinary-walk optimizer. |
| the author, *Which chord of an even cycle preserves its spectral gap*, posted November 2026, [source](https://github.com/yspennstate/one-chord-even-cycle-spectral-gap/blob/main/paper/main.tex) | Already proves Theorem 3 below, including positive chord weights, and a separate Metropolis result. It is a public preprint, not a peer-reviewed publication. |

Chatterjee–Diaconis, [*Speeding up Markov chains with deterministic jumps*](https://arxiv.org/abs/2004.11491), PTRF **178** (2020), 1193–1214, permits permutations of the entire state space. On state space $S_n$, an arbitrary such permutation need not be right multiplication by one $\sigma\in S_n$, so that result does not directly answer E0094.

No settlement of the optimal mixing order for the prescribed E0094 augmentation was located in these sources or the targeted follow-up searches. This is a bounded literature search, not a priority claim for Theorem 2. Source PDFs, extracted text, and the prior cycle manuscript are saved under `sources/`.

## Conventions

Products of permutations are compositions acting on the rightmost argument first. Relabel the $n$ letters by $\mathbb Z/n\mathbb Z$, so $c(x)=x+1$ and $\tau=(0,1)$. For a symmetric set $T$ of distinct nonidentity permutations, use
$$
 P_T=\tfrac12 I+\frac1{2|T|}\sum_{s\in T}R_s,
 \qquad R_sf(g)=f(gs).
$$
The base set is $\{\tau,c,c^{-1}\}$. For the explicit construction there are five distinct moves. The stationary measure is uniform, and left translation makes the total-variation distance independent of the starting state.

For a graph with conductance matrix $A$, degrees $D=\operatorname{diag}(d_i)$, and $L=D-A$, the ordinary-walk gap is
$$
 \gamma=1-\lambda_2(D^{-1}A)
 =\inf_{f\not\equiv\mathrm{constant}}
 \frac{\sum_{\{i,j\}}A_{ij}(f_i-f_j)^2}
 {\min_b\sum_i d_i(f_i-b)^2}.
$$
This is the second generalized eigenvalue of $Lf=\gamma Df$, not necessarily the absolute spectral gap of a nonlazy walk. Making the walk half-lazy divides this gap by two and removes periodicity. Single-edge additions change the stationary measure to the new degree measure. Matchings in the finite searches consist entirely of missing edges, so the augmented graph is simple and $(d+1)$-regular. Complete graphs have no admissible addition.

## E0094: a universal lower bound

**Theorem 1.** Let $n\ge3$, $\sigma\in S_n$, and let $B(r)$ be a radius-$r$ ball in the undirected Cayley graph generated by $\tau,c,c^{-1},\sigma,\sigma^{-1}$, after coincidences and identity moves are removed. Then
$$
 |B(r)|\le 1+5\sum_{j=0}^{r-1}4^j=\frac{5\,4^r-2}{3}.
$$
Consequently its diameter is at least
$$
 \left\lceil\log_4\frac{3n!+2}{5}\right\rceil,
$$
and every walk supported on these moves and the identity satisfies
$$
 \|P^t(e,\cdot)-U\|_{\rm TV}
 \ge 1-\frac{5\,4^t-2}{3n!}.
$$
For the half-lazy walks specified above, uniformly in $\sigma$,
$$
 t_{\rm mix}(\varepsilon)\ge(2-o(1))\frac{\log(n!)}{\log4}
 =(2-o(1))\frac{n\log n}{\log4}.
$$

**Proof.** The graph has degree at most five because $\tau=\tau^{-1}$. A shortest nonempty word has at most five choices for its first letter and at most four for each subsequent letter: an immediate inverse pair can be deleted. Counting such words proves the ball bound, whether or not additional relations identify words. A ball containing every element has size at least $n!$, which proves the diameter claim. The support at time $t$ lies in $B(t)$. Applying the definition of total variation to this event proves the displayed distance bound.

For the stronger lazy bound, put $R_n=\log_4(n!)$. Fix $0<\delta<1$, let $t=\lfloor(2-\delta)R_n\rfloor$, and set $r=\lfloor(1-\delta/4)R_n\rfloor$. The number $K_t$ of nonholding moves is binomial with parameters $t,1/2$; if a listed move is the identity it is stochastically smaller. Its mean is at most $(1-\delta/2)R_n$. Chebyshev's inequality, using $\operatorname{Var}(K_t)\le t/4$, gives $\mathbb P(K_t>r)=o(1)$, uniformly in the generators. Hence $P^t(e,B(r))=1-o(1)$, whereas
$$
 U(B(r))\le(5\,4^r-2)/(3n!)=o(1).
$$
The distance tends to one. Since $\delta$ is arbitrary, the asserted lower bound follows, with Stirling's formula giving the final expression. ∎

For three unrestricted generators the analogous degree-six counting bound has branching factor five, as in the question. The involution in the prescribed pair improves five to four. A diameter bound by itself does not supply a mixing upper bound.

## E0094: an explicit faster addition

**Theorem 2.** For every odd $n\ge5$, let
$$
 \sigma(x)=2x\pmod n,
 \qquad T=\{\tau,c,c^{-1},\sigma,\sigma^{-1}\},
 \qquad h=\lceil\log_2 n\rceil,
 \qquad A_*=720h^2.
$$
Every transposition has a $T$-word of length at most $12h$. The half-lazy walk $P_T$ satisfies, for $0<\varepsilon<1$,
$$
 t_{\rm mix}(\varepsilon)\le
 \left\lceil A_*(n-1)
 \left[2\log n+\log\left(1+\frac1{4\varepsilon^2}\right)\right]\right\rceil.
$$
In particular $t_{\rm mix}(1/4)=O(n\log^3 n)$, and this Cayley graph has diameter $\Theta(n\log n)$.

**Proof of the word bound.** Oddness makes $\sigma$ invertible and gives
$$
 \sigma c\sigma^{-1}=c^2.
$$
For $0\le i<n$, the binary recurrence
$$
 c^{2q+b}=\sigma c^q\sigma^{-1}c^b,\qquad b\in\{0,1\},
$$
constructs a word for $c^i$ of length at most $3h-2$ when $i>0$, and zero when $i=0$.

Let $1\le d<n$, and write
$$
 d=2^{j_1}+\cdots+2^{j_r},\qquad
 0\le j_1<\cdots<j_r\le h-1.
$$
Set $a_\ell=\sum_{u<\ell}2^{j_u}$, $A_\ell=c^{a_\ell}\sigma^{j_\ell}$, and
$$
 e_\ell=A_\ell\tau A_\ell^{-1}
 =(a_\ell,a_\ell+2^{j_\ell}).
$$
These are the consecutive edge transpositions along the simple path with partial sums $0,2^{j_1},\ldots,d$. Thus
$$
 (0,d)=e_1\cdots e_{r-1}e_re_{r-1}\cdots e_1=B\tau B^{-1},
 \qquad B=e_1\cdots e_{r-1}A_r.
$$
For $\ell<r$,
$$
 A_\ell^{-1}A_{\ell+1}
 =\sigma^{-j_\ell}c^{2^{j_\ell}}\sigma^{j_{\ell+1}}
 =c\sigma^{j_{\ell+1}-j_\ell}.
$$
Consequently the factors in $B$ telescope to a word of length
$$
 |B|\le j_r+2(r-1)\le3h-3.
$$
It follows that $(0,d)$ has length at most $6h-5$. Conjugating by the binary word for $c^i$ gives $(i,i+d)$ in length at most $12h-9\le12h$. Residues $i+d$ are interpreted modulo $n$. ∎

**Proof of the comparison and mixing bound.** Write $N=n!$ and
$$
 D_s(f)=\frac1N\sum_g(f(gs)-f(g))^2.
$$
Let $Q$ be the half-lazy random-transposition walk: it holds with probability $1/2$ and otherwise chooses one of the $M=\binom n2$ transpositions uniformly. Then
$$
 \mathcal E_{P_T}(f,f)=\frac1{20}\sum_{s\in T}D_s(f),
 \qquad \mathcal E_Q(f,f)=\frac1{4M}\sum_{u\text{ transposition}}D_u(f).
$$
For a chosen word $u=s_1\cdots s_\ell$, telescoping and Cauchy–Schwarz, followed by translation of the uniform summation variable, give
$$
 D_u(f)\le\ell\sum_{j=1}^{\ell}D_{s_j}(f)
 \le(12h)^2\sum_{s\in T}D_s(f).
$$
Therefore
$$
 \mathcal E_Q\le5(12h)^2\mathcal E_{P_T}=A_*\mathcal E_{P_T}.
$$
The min–max principle implies that the ordered nonzero eigenvalues of $I-P_T$ are at least $1/A_*$ times the corresponding eigenvalues of $I-Q$.

Here is a quantitative heat-trace bound for $Q$, included to specify precisely the comparison input. The classical decomposition of the regular representation of $S_n$ indexes its irreducibles by partitions $\lambda\vdash n$, with dimension $d_\lambda$ and multiplicity $d_\lambda$. The transposition character ratio is
$$
 r_\lambda=\frac{\sum_i\lambda_i^2-\sum_j(\lambda'_j)^2}{n(n-1)}.
$$
These standard identities, also used in the cited comparison literature, give the $I-Q$ eigenvalue $\mu_\lambda=(1-r_\lambda)/2$. If $j=n-\lambda_1$, then
$$
 \sum_i\lambda_i^2\le n\lambda_1,\qquad
 \sum_j(\lambda'_j)^2\ge n,\qquad
 \mu_\lambda\ge\frac j{2(n-1)}.
$$
Removing the first row from a standard tableau gives
$$
 d_\lambda\le\binom nj d_{\bar\lambda},\qquad
 \sum_{\lambda:\lambda_1=n-j}d_\lambda^2
 \le\binom nj^2 j!\le n^{2j},
$$
where $\sum_{\nu\vdash j}d_\nu^2=j!$. The tableau inequality follows by choosing the $j$ labels below the first row and their standard tableau; the remaining labels have a unique increasing order in the first row. The column restrictions can only reduce the number of choices.

Both walks have nonnegative spectrum by laziness. Transitivity and reversibility give
$$
 \chi^2(P_T^t(e,\cdot),U)=\operatorname{tr}(P_T^{2t})-1.
$$
The eigenvalue comparison and $1-x\le e^{-x}$ therefore imply
$$
 \chi^2(P_T^t(e,\cdot),U)
 \le\sum_{\lambda\ne(n)}d_\lambda^2e^{-2t\mu_\lambda/A_*}
 \le\sum_{j=1}^{n-1}\left(n^2e^{-t/[A_*(n-1)]}\right)^j.
$$
For the claimed time, the quantity in parentheses is at most
$4\varepsilon^2/(1+4\varepsilon^2)$, so the sum is at most $4\varepsilon^2$. Cauchy–Schwarz gives $\|P_T^t-U\|_{\rm TV}\le\tfrac12\sqrt{\chi^2}\le\varepsilon$.

Finally every permutation is a product of at most $n-1$ transpositions. The word bound gives diameter at most $12h(n-1)$; Theorem 1 supplies the matching order lower bound. ∎

Theorem 2 determines the best possible power of $n$, not the exact optimal mixing order. In particular, a diameter of $\Theta(n\log n)$ has not been substituted for a mixing theorem.

## E0095: one chord of an even cycle

The following theorem is already in the author's cited November 2026 preprint. Its proof is reproduced to make the answer self-contained; it is not claimed as a new result of this task.

**Theorem 3 (the author).** Let $n=2m\ge4$, give the edges of $C_n$ conductance one, and add a chord $\{0,k\}$ of conductance $w>0$, where $2\le k\le m$. Put $a=1-\cos(2\pi/n)$. Then
$$
 \gamma(C_n+w\{0,m\})=a,
$$
whereas for $2\le k<m$,
$$
 \gamma(C_n+w\{0,k\})
 \le\frac a{1+\frac{2w}{n+w}\cos^2(\pi k/n)}<a.
$$
Thus antipodal chords, and only those, maximize the ordinary-walk gap. No single chord increases it.

**Proof.** First, for $g_0=g_m=0$, the path Dirichlet inequality is
$$
 \sum_{i=0}^{m-1}(g_{i+1}-g_i)^2
 \ge2a\sum_{i=1}^{m-1}g_i^2.
$$
Indeed the matrix on the interior vertices has diagonal two and neighboring entries minus one, with sine eigenvectors $\sin(\pi ji/m)$ and eigenvalues $2-2\cos(\pi j/m)$.

For the antipodal chord, the half-turn $Tf(i)=f(i+m)$ preserves both the energy form and the degree inner product. Decompose $f=f_++f_-$, with $Tf_\pm=\pm f_\pm$. The two subspaces are orthogonal for both forms, and $f_-$ has degree-weighted mean zero.

For $f_+$, put $t=f_+(0)=f_+(m)$ and $g=f_+-t$. On both arcs from 0 to $m$, $g$ vanishes at their endpoints. The path inequality gives energy at least $2a\sum_i g_i^2$, whereas its degree variance is at most $\sum_i d_i g_i^2=2\sum_i g_i^2$. The chord contributes no energy.

For $f_-$, write $s=f_-(0)=-f_-(m)$. Its unweighted mean is zero. The cycle Poincaré inequality and the chord energy give
$$
 \mathcal E(f_-)\ge2a\sum_i f_-(i)^2+4ws^2
 \ge a\left(2\sum_i f_-(i)^2+2ws^2\right)
 =a\sum_i d_i f_-(i)^2,
$$
since $a\le1$. Adding the orthogonal pieces proves $\gamma\ge a$. The function $f(i)=\sin(2\pi i/n)$ vanishes at both chord endpoints and has degree-weighted mean zero, with $Lf=aDf$. It proves the reverse inequality.

For a nonantipodal chord set $\theta=2\pi/n$, $b=\cos(\pi k/n)>0$, and $f(i)=\cos(\theta(i-k/2))$. Its endpoint values are equal to $b$, its unweighted mean is zero, and $\sum_i f(i)^2=n/2$. The chord has zero energy, so $\mathcal E(f)=na$. Direct minimization over the additive constant gives
$$
 \operatorname{Var}_D(f)
 =n+2wb^2-\frac{(2wb)^2}{2n+2w}
 =n\left(1+\frac{2wb^2}{n+w}\right).
$$
Its Rayleigh quotient is the claimed strict upper bound. ∎

For comparison, the second eigenvalue of the **combinatorial** Laplacian remains exactly $2-2\cos(2\pi/n)$ for every single chord and every positive weight. Edge addition is positive semidefinite, giving the lower bound. The original second eigenspace has dimension two, so it contains a nonzero function equal at the two chord endpoints; its Rayleigh quotient gives the upper bound. Thus every chord ties for that different objective.

The prior preprint also shows that Metropolizing the augmented ordinary walk to restore the uniform stationary measure strictly lowers the gap for every chord. That is a different kernel from the ordinary walk analyzed above.

## E0095: perfect matchings, a settled order question

**Theorem 4 (consequence of Hermon–Sly–Sousi).** For any sequence of connected simple $d$-regular graphs of even order $n\to\infty$, with $d\ge2$ bounded independently of $n$, there are perfect matchings consisting of missing edges for which the augmented ordinary walk has a gap bounded below by a positive constant and mixing time $\Theta(\log n)$. A uniform matching conditioned to avoid the original edges has these properties with probability tending to one. Consequently the optimal gap is $\Theta(1)$ and the optimal fixed-error mixing time is $\Theta(\log n)$, both on $C_n$ and on all such base graphs.

**Justification and transfer to missing edges.** The cited Theorem 1.1 gives logarithmic mixing and cutoff; Proposition 1.2 gives a constant absolute gap for an unconditioned uniform matching. Their hypotheses allow every bounded-degree base graph whose connected components have at least three vertices, so connected regular graphs here qualify.

To pass to matchings avoiding the base edges, let $X_n$ count overlaps. For fixed $k$, the number of $k$-edge matchings within the base graph is
$$
 (dn/2)^k/k!+O_{d,k}(n^{k-1}).
$$
This follows by choosing $k$ distinct edges, then subtracting choices containing an incident pair. The probability that a uniform perfect matching contains any prescribed $k$ disjoint edges is
$$
 [(n-1)(n-3)\cdots(n-2k+1)]^{-1}.
$$
Hence $\mathbb E\binom{X_n}{k}\to(d/2)^k/k!$. The finite Bonferroni bounds for $\mathbb P(X_n=0)$, followed by increasing the truncation order, give $\mathbb P(X_n=0)\to e^{-d/2}>0$. Conditioning on an event of probability bounded away from zero preserves any high-probability conclusion. If $d$ varies in a fixed finite set, the same conclusion holds along every constant-$d$ subsequence.

For optimality in order, the gap of a half-lazy walk is at most one. The augmented simple graph has degree $d+1$, so its radius-$t$ ball contains at most $1+(d+1)\sum_{j=0}^{t-1}d^j$ vertices. Uniform stationarity and the support argument in Theorem 1 give an $\Omega(\log n)$ mixing lower bound. ∎

The general theorem's published proof is not re-proved here; this is precisely the subquestion that is already settled in print. The conditioning and optimal-order deductions above are supplied in full. The exact finite optimizer is not given by that theorem. For a deterministic specification achieving these orders, one may enumerate complement perfect matchings and select the one with maximal gap; existence follows above. This is not asserted to be an efficient construction.

In particular, adding the entire antipodal matching is **not** optimal in order. Its circulant adjacency eigenvalues are
$$
 2\cos(2\pi j/n)+(-1)^j,\qquad0\le j<n.
$$
For all sufficiently large even $n$, the $j=2$ eigenvalue gives ordinary gap $(2/3)(1-\cos(4\pi/n))=\Theta(n^{-2})$. An optimal matching has constant gap.

## E0095: structural statements and a counterexample

**Theorem 5.** Let $G$ be a connected $d$-regular graph and let the second eigenvalue $\alpha$ of its combinatorial Laplacian have multiplicity at least two. Adding one edge of any positive conductance cannot increase its ordinary-walk gap $\alpha/d$. The inequality is strict if its Fiedler eigenspace contains a vector $f$ with $f(u)=f(v)\ne0$ at the new edge endpoints.

**Proof.** In the Fiedler eigenspace, the equation $f(u)-f(v)=0$ imposes at most one linear condition. Choose a nonzero solution, and write $f(u)=f(v)=b$. It has unweighted mean zero. Adding conductance $w$ does not alter its energy, which is $\alpha\|f\|_2^2$. Its new degree variance is
$$
 d\|f\|_2^2+2wb^2-\frac{4w^2b^2}{nd+2w}
 =d\|f\|_2^2+\frac{2wnd}{nd+2w}b^2
 \ge d\|f\|_2^2.
$$
The variational formula proves the assertion, strictly when $b\ne0$. ∎

**Proposition 6 (infinitesimal edge selection).** Suppose the ordinary gap $\gamma$ of a connected $d$-regular graph is simple, and let $f\perp\mathbf1$ be its Euclidean-unit Fiedler vector. If edge $\{u,v\}$ is added with conductance $w$, then
$$
 \left.\frac{d\gamma(w)}{dw}\right|_{w=0}
 =\frac{(f(u)-f(v))^2-\gamma(f(u)^2+f(v)^2)}d.
$$
For the combinatorial Laplacian the derivative is instead $(f(u)-f(v))^2$. Thus the extremal-value rule maximizes the latter first derivative when the extremal pair is admissible; it need not maximize a finite unit-edge improvement.

**Proof.** Simplicity gives a differentiable local generalized eigenpair $L(w)f(w)=\gamma(w)D(w)f(w)$. Differentiate and multiply on the left by $f(0)^T$. Symmetry and the original eigenvalue equation cancel the terms involving $f'(0)$, leaving
$$
 \gamma'(0)=\frac{f^T(L'-\gamma D')f}{f^TDf}.
$$
Here $L'=(e_u-e_v)(e_u-e_v)^T$, $D'=e_ue_u^T+e_ve_v^T$, and $D=dI$. This gives the formula. The ordinary symmetric eigenproblem with $D=I$ gives the final assertion. ∎

**Proposition 7 (finite-edge counterexample).** A best added unit edge need not join vertices with maximal and minimal Fiedler-vector entries, even when the base graph is connected and cubic and its Fiedler eigenvalue is simple.

**Proof and exact certificate.** Use vertices $0,\ldots,9$, with edge set
$$
\begin{split}
 \{&04,06,07,15,17,18,25,28,29,\\
   &36,38,39,47,49,56\}.
\end{split}
$$
It is cubic; a traversal from 0 reaches every vertex. Let $z\in(1879/1000,1880/1000)$ be the root of $z^3-3z-1=0$. An adjacency eigenvector with eigenvalue $z$ is
$$
 f=(2,\ z^2-z-2,\ 2-z^2,\ -1,\ z,\ -1,\ 0,\ z,\ 2-z^2,\ z^2-z-2).
$$
Substitution at each vertex verifies the equation modulo $z^3-3z-1$. The combinatorial-Laplacian characteristic polynomial is
$$
 x(x-5)(x-2)(x^3-9x^2+24x-17)
 (x^4-14x^3+69x^2-141x+101).
$$
Sturm's rule gives exactly one nonzero root below $6/5$, namely $3-z\in(1.120,1.121)$; it is simple. Thus $f$ is the Fiedler vector. Its unique maximum is at 0 and its minima are exactly at 2 and 8: the bounds on $z$ give
$$
 2-z^2<-1<z^2-z-2<0<z<2.
$$
The only extremal pairs are therefore $02$ and $08$, both missing edges.

For an augmented adjacency matrix $A'$, the positive roots of $\det(L'-xD')$, or equivalently of the primitive characteristic polynomial of $D'^{-1}L'$, are its ordinary-walk gaps and higher normalized eigenvalues. For either extremal pair that primitive polynomial is $x(x-1)F(x)$, where
$$
\begin{split}
F(x)={}&104976x^8-944784x^7+3615111x^6-7663977x^5\\
 &+9825705x^4-7789311x^3+3726108x^2-983400x+109696.
\end{split}
$$
For the competing edge $24$ it is $xH(x)$, with
$$
\begin{split}
H(x)={}&104976x^9-1049760x^8+4559895x^7-11274714x^6\\
 &+17461899x^5-17544330x^4+11423646x^3\\
 &-4645620x^2+1070515x-106528.
\end{split}
$$
The exact Sturm variation counts for the polynomial after its factor $x$ is removed are:

| Added edge | $l$ | $u$ | $V(0)$ | $V(l)$ | $V(u)$ |
|---|---:|---:|---:|---:|---:|
| $02$, $08$ | 47694/100000 | 47695/100000 | 9 | 9 | 8 |
| $24$ | 48117/100000 | 48118/100000 | 9 | 9 | 8 |

There is no positive root below $l$, and exactly one in ($l,u$), in each row. Consequently both extremal choices have gap below 0.47695, whereas edge $24$ has gap above 0.48117. This proves the strict counterexample. The exact polynomial expansion, eigenvector identities, and Sturm checks are reproduced by `code/certify_counterexample.py`, with rational output in `data/counterexample_exact.json`. The exhaustive certificate additionally verifies that $24$ and its tied alternatives are globally optimal for this graph. ∎

## Computations

All searches use one thread per process and no worker pool. Heavy jobs inherit Unix nice level at least 10. The full-state walk executable rejects principal-array allocation plans above 3.5 GB and checks the resident-memory high-water mark during propagation. macOS rejected `RLIMIT_AS`; no address-space enforcement is claimed. The actual runs peaked at 1.44 GB. No state transition matrix of dimension $(n!)^2$ is formed.

### Total-variation curves

`code/exact_walk.cpp` enumerates all $n!$ permutations by lexicographic rank, stores three or five `uint32_t` successor arrays, and propagates two double-precision probability vectors. At every integer time it sums
$$
 \tfrac12\sum_{g\in S_n}|p_t(g)-1/n!|.
$$
These are deterministic full-state computations, not empirical histogram estimates or projected-TV lower bounds. “Exact” here refers to retaining the entire state space; the probabilities are floating point. CSV files retain every time step through distance 0.01.

For odd $n$, the added generator is exactly the one in Theorem 2. To include the requested even sizes, for even $n$ the numerical generator doubles modulo $n-1$ on $0,\ldots,n-2$ and fixes $n-1$. Those rows are separate exploratory examples; they are not covered by Theorem 2's proof.

<!-- WALK_TABLE -->

| n | base t(0.25) | added t(0.25) | ratio | base t(0.01) | added t(0.01) |
|---:|---:|---:|---:|---:|---:|
| 5 | 29 | 13 | 2.231 | 92 | 44 |
| 6 | 58 | 17 | 3.412 | 170 | 46 |
| 7 | 103 | 42 | 2.452 | 281 | 113 |
| 8 | 168 | 49 | 3.429 | 433 | 126 |
| 9 | 254 | 74 | 3.432 | 633 | 171 |
| 10 | 368 | 74 | 4.973 | 887 | 164 |
| 11 | 512 | 102 | 5.020 | 1203 | 213 |

<!-- END_WALK_TABLE -->

The curves are in `data/walk_n{n}_{base,double}.csv`; figures are `data/tv_curves.pdf` and `data/tv_curves.png`. Exact integer path counts for the first twenty steps, independently implemented in `code/audit_walk.py` for $n=5,6,7$, check the propagation and TV normalization. The same audit checks mass and monotonicity for every curve. Numerical errors and measured memory are recorded in `data/walk_audit.json` and the per-run `.stderr` files.

The raw state-array budget at $n=11$ is 1,437,004,800 bytes for five successor arrays and two probability vectors. The measured peak during propagation was 1,438,400,512 bytes (1.44 GB). The largest mass discrepancy was $1.18\times10^{-10}$; the largest error against exact integer path counts was $1.26\times10^{-14}$. Standard IEEE double rounding also gives a conservative absolute TV error below $10^{-6}$ for the reported runs: nonnegative updates have a bounded number of operations per coordinate, their accumulated $\ell^1$ error grows by $O(tu)$, and the final sum contributes at most $O(n!u)$, where $u=2^{-53}$. This bound is deliberately loose. Thresholds in the table are numerical crossings; the curves do not establish an asymptotic exponent by themselves.

### Even cycles

`code/cycles.py` checks every chord distance for even $4\le n\le40$ and weights $0.01,1/2,1,5,1000$. For $n\le16$, weights $1/2,1,5$, it additionally computes rational normalized characteristic polynomials, certifies the second-root bracket by exact inertia, and verifies divisibility by the minimal polynomial of $1-\cos(2\pi/n)$ for antipodal chords. Outputs are `data/cycle_chords.csv` and `data/cycle_exact.json`.

<!-- CYCLE_TABLE -->

| n | admissible matchings | best matching gap | antipodal matching gap |
|---:|---:|---:|---:|
| 4 | 1 | 1.333333333 | 1.333333333 |
| 6 | 4 | 1.000000000 | 1.000000000 |
| 8 | 31 | 0.666666667 | 0.666666667 |
| 10 | 293 | 0.479482396 | 0.460655337 |
| 12 | 3326 | 0.489303705 | 0.333333333 |
| 14 | 44189 | 0.528595479 | 0.251006799 |

<!-- END_CYCLE_TABLE -->

For the matching table, the search excludes original cycle edges. All matchings through $n=14$ were enumerated. Values for $n\le10$ are also covered by the exact rational optimizer certificates of the regular-graph census. The additional $n=12,14$ rows are exhaustive floating-point searches, not certified algebraic optimizations. Witness matchings are in `data/cycle_matchings.json`. They are illustrative finite optima; the settled asymptotic theorem is Theorem 4.

### Exhaustive regular-graph census

`nauty` 2.8.9 `geng -c -d{d} -D{d} n` generates one representative of every connected simple $d$-regular graph in the stated range. Input graph6 files are preserved in `data/regular_n{n}_d{d}.g6`. Every missing edge and every perfect matching of the complement was considered for all even orders $2\le n\le10$. This range is explicit; no enumeration of larger general regular graphs is claimed.

<!-- REGULAR_TABLE -->

| n | d : number of connected graphs | total | simple-Fiedler failures |
|---:|---|---:|---:|
| 2 | 1 : 1 | 1 | 0 |
| 4 | 2 : 1, 3 : 1 | 2 | 0 |
| 6 | 2 : 1, 3 : 2, 4 : 1, 5 : 1 | 5 | 0 |
| 8 | 2 : 1, 3 : 5, 4 : 6, 5 : 3, 6 : 1, 7 : 1 | 17 | 0 |
| 10 | 2 : 1, 3 : 19, 4 : 59, 5 : 60, 6 : 21, 7 : 5, 8 : 1, 9 : 1 | 167 | 7 |

<!-- END_REGULAR_TABLE -->

There are 192 base graphs, 3,876 candidate edges, and 8,690 candidate matchings. The floating-point Fiedler-vector search identifies seven failures of the extremal-entry rule with numerically simple Fiedler eigenvalue: one cubic graph, two 4-regular graphs, and four 5-regular graphs, all on ten vertices. Proposition 7 certifies the cubic example completely, including its eigenvector extrema and simplicity. The other six Fiedler-vector diagnoses are numerical; the gap optimization for every graph is nevertheless certified exactly. Repeated Fiedler eigenvalues are excluded from this diagnostic count; no claim about a canonical vector in a multidimensional eigenspace is made.

The optimization certificates are exact despite using LAPACK to propose root locations. For each candidate, `code/exact_spectra.py` applies fraction-free Bareiss elimination to the integer symmetric matrices $qL-pD$, at rational endpoints bracketing the proposed gap. Successive leading-minor signs give the inertia. Exactly one negative eigenvalue at the lower endpoint and at least two at the upper endpoint certify the gap bracket. If a leading minor vanishes, the endpoint is moved and the check repeated. Nonoverlapping brackets prove strict ordering. For overlapping top brackets, rational characteristic-polynomial gcds and exact root counts certify equality with the chosen optimizer. Thus no unresolved numerical tie is silently declared optimal.

`data/regular_exact_certificates.json` stores every bracket and every optimizing edge/matching. `data/regular_graphs.csv` gives readable numerical values and representative optimizers. `data/fiedler_counterexamples.json` contains all seven examples. Exact verification has not been extended to all choices of arbitrary positive edge weight, to all mixing-time objectives, or to larger graph orders.

## Reproduction and audit

From this directory, with Python 3, NumPy, SciPy, NetworkX, SymPy, Matplotlib, and a C++17 compiler:

```sh
export OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 MKL_NUM_THREADS=1
clang++ -O3 -std=c++17 code/exact_walk.cpp -o code/exact_walk
python3 code/run_walks.py
python3 code/words.py
python3 code/regular_graphs.py
python3 code/certify_counterexample.py
python3 code/cycles.py
python3 code/audit_walk.py
python3 code/audit_graphs.py
python3 code/audit_heat_trace.py
python3 code/make_tables.py
```

The downloaded nauty source archive, build output, and `geng` binary are saved locally. A fresh build is described in `code/REPRODUCE.md`. No network access is needed to rerun the mathematics after dependencies are installed. There is no need to run more than one of these commands at a time.

Two independent checks support the main calculations: exact permutation evaluation verifies all 168,663 constructed transposition words in the recorded test range; integer path counts independently check the walk engine. Graph eigenvalue estimates are checked through exact rational inertia, with the counterexample checked a second way by characteristic polynomials and Sturm sequences. An independent symmetric-normalization calculation checks all 12,566 rational spectral brackets; an atlas comparison checks completeness at orders 2, 4, and 6. Exact hook-length calculations verify the heat-trace dimension bounds through degree 20. These audits are in `data/graph_audit.json` and `data/heat_trace_audit.json`. The heat-trace normalization and the distinction between the two Laplacians are derived explicitly above.

## What remains open

1. The exact asymptotic value of $\inf_\sigma t_{\rm mix}(\varepsilon)$ for E0094. The present bounds leave a factor $O(\log^2 n)$; neither $\Theta(n\log n)$ optimality nor cutoff for the doubling construction is proved.
2. Whether the particular doubling walk admits a sharper mixing bound than Theorem 2, and which other single generators minimize finite-$n$ mixing.
3. A structural characterization of the exact best finite edge or perfect matching for an arbitrary regular graph. Theorem 4 settles the order for bounded degree but does not specify that optimizer. Mosk-Aoyama's variable-budget hardness theorem does not settle this single-edge problem.
4. Optimal choices for unbounded degree, weighted additions under a budget, or Metropolis kernels with a prescribed invariant measure. These are different optimization problems.

Task: “Open problems E0094 and E0095: which generator or edge to add to speed up a random walk.” First recorded session clock: 2026-11-13 02:23:47 +04 (Asia/Tbilisi).
