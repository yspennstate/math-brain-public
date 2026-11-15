# T045 verification

Checked November 14, 2026. **NOT-THIS for all three candidates.** None claims (a), (b), or a new special case of either. This compares statements; it does not certify proof correctness.

## Our statement

On the infinite nearest-neighbour ferromagnetic Ising lattice $\mathbb Z^d$, start with independent spins of plus density $p$ and run zero-temperature Glauber dynamics with fair random tie breaking.

- (a) For every fixed integer $d\ge2$ and every $p>1/2$, almost surely every site is eventually plus forever.
- (b) At $p=1/2$ and every integer $d\ge3$, almost surely every site flips infinitely often.

In (a), each site's fixation time may depend on the site. These are long-time trajectory statements, not finite-size mixing estimates.

## Candidate 1: A typical-start upper bound for low-temperature SK Glauber dynamics

Author exactly as on the manuscript: **OpenAI**. Date: **September 24, 2026**.

Opened the actual [build/paper.tex](https://github.com/openai/math/blob/main/preprints/A-typical-start-upper-bound-for-low-temperature-SK-Glauber-dynamics-September-24-2026/build/paper.tex), [build/introduction.tex](https://github.com/openai/math/blob/main/preprints/A-typical-start-upper-bound-for-low-temperature-SK-Glauber-dynamics-September-24-2026/build/introduction.tex) and [build/sections/mixing.tex](https://github.com/openai/math/blob/main/preprints/A-typical-start-upper-bound-for-low-temperature-SK-Glauber-dynamics-September-24-2026/build/sections/mixing.tex). Theorem 1, “Mixing from a typical Gibbs state,” states exactly, in the original LaTeX:

~~~latex
\begin{theorem}[Mixing from a typical Gibbs state]\label{thm:main}
For every fixed $\beta>1$, there is $c_\beta\in(0,1)$ such that
\[
 \mathbb P_{J,\,\sigma_0\sim\pi_{n,\beta}^J}
 \left\{T_{n,\beta}^J(\sigma_0)
       \le\exp\bigl(n^{1-c_\beta}\bigr)\right\}
 \longrightarrow1
 \qquad\text{as }n\longrightarrow\infty.
\]
The exponent is independent of $n$ and of the realized disorder.
The proof permits $c_\beta=1/40000000$ for every fixed $\beta>1$.
\end{theorem}
~~~

The model has $n$ spins and independent standard Gaussian pair couplings:
\[
 H_n^J(\sigma)=\frac1{\sqrt n}\sum_{i<j}J_{ij}\sigma_i\sigma_j,
 \qquad \pi_{n,\beta}^J(\sigma)\propto e^{\beta H_n^J(\sigma)}.
\]
Each site has a rate-one heat-bath clock. $T_{n,\beta}^J(\sigma)$ is the first time the transition law from the fixed configuration $\sigma$ is within total-variation distance $1/4$ of $\pi_{n,\beta}^J$. The Gibbs configuration is sampled once and held fixed before evaluating that distance.

| Requirement in T045 | Actual theorem |
| --- | --- |
| Nearest-neighbour Ising ferromagnet | Gaussian SK spin glass, with signed interactions between every pair |
| Infinite $\mathbb Z^d$, fixed $d\ge2$ or $d\ge3$ | Finite $n$-spin system with $n\to\infty$; no lattice dimension |
| Zero temperature | Each fixed finite inverse temperature $\beta>1$; no $\beta=\infty$ assertion |
| Iid starting spins with plus density $p$ | An interacting equilibrium Gibbs sample; no density parameter $p$ |
| Eventually plus forever | Upper bound on mixing to equilibrium |
| Every site flips infinitely often | No zero-temperature temporal flip-count assertion |
| Almost-sure long-time conclusion | Joint disorder/start probability tending to one with system size |

The bound is subexponential, not an exact mixing-time asymptotic. Spin-flip symmetry makes the one-site Gibbs marginals fair, but does not make the spins independent. No zero-temperature or infinite-lattice conclusion follows simply by taking a limit in this fixed-temperature finite-system statement. **T045 coverage: neither (a) nor (b).**

## Candidate 2: All-temperature pressure for orthogonally invariant Ising spin glasses

Author exactly as on the manuscript: **OpenAI**. Date: **September 25, 2026**.

Opened the actual [build/invariant-sk.tex](https://github.com/openai/math/blob/main/preprints/All-temperature-pressure-for-orthogonally-invariant-Ising-spin-glasses-September-25-2026/build/invariant-sk.tex), containing the model and Theorem 1.1, “Limiting pressure.” The theorem states exactly:

~~~latex
\begin{theorem}[Limiting pressure]\label{thm:main}
Let $\Lambda_N$ be deterministic real diagonal matrices whose empirical
spectral measures converge weakly to a compactly supported probability
law $\mu$. Assume that their smallest and largest eigenvalues converge
to the respective edges of $\supp\mu$. Let $U_N$ be Haar distributed
on $O(N)$, and define $P_N$ using the uniform spin probability in
Equation~\eqref{eq:pressure}. With $S$ and $G_1$ as in
Equations~\eqref{eq:S}--\eqref{eq:G},
\begin{equation}
 \lim_{N\to\infty}\E P_N
 =\lim_{N\to\infty}P_N
 =\mathcal F(\mu)
 :=\inf_{p\in\cP}\{S(p)+G_1(p)\},
 \label{eq:variational}
\end{equation}
where the second limit holds almost surely. No independence of the
matrices $U_N$ across dimensions is required.
\end{theorem}
~~~

The source defines
\[
 P_N=\frac1N\log\left[2^{-N}\sum_{\sigma\in\{-1,1\}^N}
 \exp\left\{\tfrac12\sigma^{\mathsf T}U_N^{\mathsf T}\Lambda_NU_N\sigma\right\}\right].
\]
Temperature is absorbed into $\Lambda_N$. The trial class $\mathcal P$ consists of nondecreasing measurable paths $p:(0,1)\to[0,1]$, identified almost everywhere. This $p$ is not an initial spin density. $S$ is the Gaussian-recursion one-site variational functional defined immediately before the theorem; with the paper's edge-extended spectral transform $R$,
\[
 D_p(r)=1-r-\int_0^1(p(s)-r)_+\,ds,\qquad
 G_1(p)=\frac12\int_0^1R(D_p(r))\,dr.
\]
The full definitions and original equation labels are preserved in sources/pressure-main.tex.

| Requirement in T045 | Actual theorem |
| --- | --- |
| Nearest-neighbour ferromagnet on $\mathbb Z^d$ | Haar-rotated random-matrix interaction with a deterministic spectral limit |
| Each fixed lattice dimension | Matrix size $N\to\infty$; no lattice dimension |
| Zero-temperature Glauber evolution | No evolution or update rule |
| Iid initial spins with density $p$ | No starting configuration or initial density |
| Fixation / infinite flipping | Convergence of equilibrium pressure to a variational value |
| Pathwise late-time statement | Expectation and almost-sure thermodynamic limits |

This is an equality for a limiting quantity, but the quantity is static pressure. The advertised zero-temperature consequence concerns maximum energy in this random-matrix model, not whether a Glauber trajectory reaches a ground state. **T045 coverage: neither (a) nor (b).**

## Candidate 3: The sharp factor-of-IID threshold for the free Ising model on regular trees

Author exactly as on the manuscript: **OpenAI**. Date: **September 26, 2026**.

Opened the actual [build/main.tex](https://github.com/openai/math/blob/main/preprints/The-sharp-factor-of-IID-threshold-for-the-free-Ising-model-on-regular-trees-September-26-2026/build/main.tex) and [build/sections/01-introduction.tex](https://github.com/openai/math/blob/main/preprints/The-sharp-factor-of-IID-threshold-for-the-free-Ising-model-on-regular-trees-September-26-2026/build/sections/01-introduction.tex). Theorem 1.1 states exactly:

~~~latex
\begin{theorem}\label{thm:main}\label{thm:sharp}
For every integer $d\ge3$ and every $\beta\ge0$, the free zero-field
Ising law $\mu_{d,\beta}$ is a factor of IID in the sense of
\eqref{eq:equivariance} if and only if
\[
                         \tanh\beta\le(d-1)^{-1/2}.
\]
In this range the factor can be chosen to commute with every
automorphism on every label input.
\end{theorem}
~~~

The referenced equivariance condition means $\Phi(gU)=g\Phi(U)$ almost surely for each fixed tree automorphism $g$, with iid uniform input labels $U_v$. The free Ising law can be described using a fair root spin and edge transmissions with agreement probability $(1+\tanh\beta)/2$; its law is independent of the auxiliary root.

| Requirement in T045 | Actual theorem |
| --- | --- |
| $\mathbb Z^d$ | Infinite $d$-regular tree |
| $d$ is lattice dimension, with $2d$ neighbours | $d$ is degree; its range $d\ge3$ is not the dimension range in T045 |
| Zero-temperature Glauber trajectory | Static free Gibbs measure at finite $\beta\ge0$ |
| Iid starting spins with density $p$ | Iid uniform labels used to generate a correlated equilibrium spin law |
| Eventually plus forever for $p>1/2$ | Existence of an automorphism-equivariant measurable coding |
| Infinite flips from fair iid spins | No temporal flip-count conclusion |
| All strict initial biases | Sharp temperature/degree coding criterion |

The equality case is the endpoint of a coding threshold, not the unbiased initial condition in T045. The Gaussian observation processes used in the proof are not Glauber dynamics. For $d\ge3$, $(d-1)^{-1/2}<1$, so the positive construction does not even extend to the limit $\tanh\beta\to1$. **T045 coverage: neither (a) nor (b).**

## Follow-ups found and opened

### SK

Opened the [community record](https://mathcommunity.github.io/oai-math-revised/papers/A-typical-start-upper-bound-for-low-temperature-SK-Glauber-dynamics-September-24-2026/), then the actual [Hexagon record](https://hexagonmath.org/abs/2610.00402v1) and [PDF](https://hexagonmath.org/pdf/2610.00402v1) of **P. M. Aronow and Patrick Lopatto**, *Lower and Upper Bounds for Glauber Dynamics from Typical States of the Low-Temperature Sherrington–Kirkpatrick Model*, version 1, **October 20, 2026**. The PDF title page confirms these author names. Its abstract claims, for each fixed $\beta>1$ and fixed $\omega\in(0,1/4)$, with probability tending to one,
\[
 A_\beta n^{7/30}<\log T^J(X_0)\le n^{1-\omega}.
\]
It strengthens the OpenAI typical-start bounds while following their proof architectures. It is still about finite-temperature SK mixing and asserts neither T045 part. Hexagon describes the text as primarily AI-generated with partial human understanding; this is not a referee report.

Opened the follow-up's [repository](https://github.com/pmaronow/fluctuations-palomar) and actual [README](https://github.com/pmaronow/fluctuations-palomar/blob/main/README.md). It reports Lean coverage of the continuous-time upper bound for $0<\omega<1/4$, excluding the endpoint. The README distinguishes historical verification receipts from pending fresh Comparator and three-kernel replay after a Corollary 1.7 interface change; it asserts no registry acceptance. These are the source's reports, not independently replayed checks.

Opened OpenAI's [scope note 227](https://github.com/openai/math/blob/main/lean/docs/227.md) and formalization catalogue. The note lists high-temperature, critical and typical-start **lower-bound** companions; it does not list this typical-start upper-bound title. An exact-title catalogue search also found no entry for that upper-bound paper. A family-level Lean link therefore cannot be treated as formalization of this candidate's own theorem.

Opened [Latent Seminar's SK exposition](https://lowrank.github.io/latent-seminar/OpenAI-Math/227-sk-dynamics), dated October 6, 2026. It separates typical Gibbs starts from iid quenches and explicitly disclaims independent verification of the complete proofs.

### Pressure

Opened the [community record](https://mathcommunity.github.io/oai-math-revised/papers/All-temperature-pressure-for-orthogonally-invariant-Ising-spin-glasses-September-25-2026/), [Latent Seminar exposition](https://lowrank.github.io/latent-seminar/OpenAI-Math/234-invariant-spin-glasses), [scope note 234](https://github.com/openai/math/blob/main/lean/docs/234.md), [comparator statement](https://github.com/openai/math/blob/main/lean/ComparatorChallenges/InvariantIsing.lean), [configuration](https://github.com/openai/math/blob/main/lean/ComparatorChallenges/InvariantIsing.json), and actual [solution module](https://github.com/openai/math/blob/main/lean/OAI/Probability/InvariantIsing/Unconditional.lean).

The scope note covers pressure, external fields, ground states, random spectra and Gaussian-pattern specializations. The configuration points to OAI.Probability.InvariantIsing.Unconditional; that module derives its displayed conclusions from imported theorems and proved inputs. The comparator challenge's deliberate sorry placeholders specify statements; they are not the separate solution. No compilation or transitive dependency audit was performed. No later paper, candidate-specific correction, refutation or named expert endorsement was located in the searches below.

### Tree

Opened the [community record](https://mathcommunity.github.io/oai-math-revised/papers/The-sharp-factor-of-IID-threshold-for-the-free-Ising-model-on-regular-trees-September-26-2026/), [Latent Seminar exposition](https://lowrank.github.io/latent-seminar/OpenAI-Math/236-tree-ising-factors), [scope note 236](https://github.com/openai/math/blob/main/lean/docs/236.md), [comparator statement](https://github.com/openai/math/blob/main/lean/ComparatorChallenges/FreeIsing.lean), [configuration](https://github.com/openai/math/blob/main/lean/ComparatorChallenges/FreeIsing.json), and actual [solution module](https://github.com/openai/math/blob/main/lean/OAI/Probability/FreeIsing/Main.lean).

The scope is the tree factor threshold, including equality, with almost-sure equivariance for each fixed automorphism; no finitary coding or coding-radius bound is included. The manuscript additionally claims an everywhere-equivariant version, beyond the chosen statement's formulation. The configuration names OAI.Probability.FreeIsing.Main, whose exported theorem invokes imported positive-direction and converse results. The catalogue lists that module. No compilation or imported-chain audit was performed. No later paper, candidate-specific correction, refutation or named expert endorsement was located.

### Search record and limits

Used the web search tool for all exact titles, title plus arxiv/error/proof, arxiv.org-restricted title queries, and GitHub issue/error/gap variants. The arXiv-restricted exact-title queries returned no results. The SK follow-up was found on Hexagon, not as an arXiv version.

Opened the release [README](https://github.com/openai/math/blob/main/README.md), [CONTENTS.md](https://github.com/openai/math/blob/main/CONTENTS.md), [history](https://github.com/openai/math/blob/main/history.md), all three manuscript READMEs, [Lean README](https://github.com/openai/math/blob/main/lean/README.md), [catalogue](https://github.com/openai/math/blob/main/lean/formalization.yaml) and [Comparator instructions](https://github.com/openai/math/blob/main/lean/ComparatorChallenges/README.md). The inspected history and candidate READMEs contain no revision or withdrawal notice for these titles. Searching CONTENTS.md for fixation and zero-temperature Glauber wording found no T045 entry. A read-only GitHub issue search for “repo:openai/math Ising” returned an empty issues list.

The community pages mark their automatically collected notes as unreviewed; they serve as discovery records. The opened Latent Seminar expositions explicitly disclaim complete independent proof verification. No referee report or independent expert correctness assessment specific to these three candidates was found. These bounded searches do not establish that no other commentary exists.

All supplied GitHub folder URLs were attempted through the web tool and returned cache misses; their listings and actual source files were then opened successfully through the read-only GitHub connector. Root paper.tex guesses returned 404. The slatinwine pressure exposition could not be opened and is not used as evidence. An initially guessed Latent Seminar pressure URL failed; the linked 234-invariant-spin-glasses URL opened successfully. Search-result-only leads from DiscoverIA and Plectis Atlas are not treated as opened-paper evidence.

For background, opened **Robert Morris**, [*Zero-temperature Glauber dynamics on Z^d*, arXiv:0809.0353](https://arxiv.org/abs/0809.0353), whose abstract confirms $p_c(\mathbb Z^d)\to1/2$; and **Daniel Stein**, [*Predictability in Nonequilibrium Discrete Spin Dynamics*, 2018 Rutgers lecture](https://cmsr.rutgers.edu/images/pdf/120/Daniel%20Stein.pdf), which presents the two-dimensional symmetric infinite-flipping result and calls the higher-dimensional question open at that time. The Fontes–Schonmann–Sidoravicius [mp_arc listing](https://web.ma.utexas.edu/mp_arc-bin/mpa?yn=01-287) was also opened; its original full paper was not used as a newly audited reference. These older sources are not a November 2026 literature census.

Opened-source snapshots are indexed in [SOURCES.md](SOURCES.md). Successive checks and failed opens are recorded in [LOG.md](LOG.md).

## Recommended new “where it stands” text

The recorded partial results remain applicable: infinite flipping for $p=1/2$ in dimension two, fixation for $p$ close to one, and fixation thresholds tending to $1/2$ as dimension grows. OpenAI's *A typical-start upper bound for low-temperature SK Glauber dynamics* (September 24, 2026), *All-temperature pressure for orthogonally invariant Ising spin glasses* (September 25, 2026), and *The sharp factor-of-IID threshold for the free Ising model on regular trees* (September 26, 2026) concern different models or quantities and claim neither part of this problem. On the evidence checked here, fixation for every $p>1/2$ in each fixed $d\ge2$ and infinite flipping at $p=1/2$ for $d\ge3$ remain open.



## Spot check

Selected one lemma from the closest candidate: **“Pruning and averaged mixing”**, in [SK sections/mixing.tex](https://github.com/openai/math/blob/main/preprints/A-typical-start-upper-bound-for-low-temperature-SK-Glauber-dynamics-September-24-2026/build/sections/mixing.tex), label lem:pruning. This is the final bridge from the paper's balanced-flow estimates to its main typical-start mixing claim. The earlier SK-specific flow and proposal estimates are not checked here.

Its hypotheses are a finite reversible continuous-time chain, a strictly positive stationary law $\pi$, total exit rates at most $R$, and
\[
 Q(S,S^{\rm c})>B\quad\text{if }\varepsilon\le\pi(S)\le1-\varepsilon,
 \qquad 0<\varepsilon<1/3.
\]
Its conclusion is
\[
 \sum_x\pi(x)\|P_T(x,\cdot)-\pi\|_{\rm TV}
 \le \frac{\sqrt{2R H(\pi)}}{B\sqrt T}+2\varepsilon,
 \qquad H(\pi)=-\sum_x\pi(x)\log\pi(x).
\]

The proof's constants and use of stationarity can be checked directly.

1. Remove a set $U$ from the current retained set $C$ only when $\pi(U)\le\pi(C)/2$ and $Q(U,C\setminus U)<B\pi(U)$. If $A$ is the union removed, every edge crossing from $A$ to its present complement was counted at its first removal, so $Q(A,A^{\rm c})<B\pi(A)$. At the first crossing of mass $\varepsilon$, the preceding mass $a<\varepsilon$ gives $\pi(A)\le(1+a)/2<(1+\varepsilon)/2<1-\varepsilon$. The balanced-cut hypothesis then gives the contradiction $Q(A,A^{\rm c})>B>B\pi(A)$. Thus $\pi(C^{\rm c})<\varepsilon$.

2. The terminal set has $Q(U,C\setminus U)\ge B\pi(U)$ for its smaller halves. Coarea applied to the square of each positive or negative median part of $u$ gives
\[
 B\sum_C\pi w^2
 \le\Big(\sum_{\{x,y\}\subset C}q(x,y)(w(x)-w(y))^2\Big)^{1/2}
       \Big(2R\sum_C\pi w^2\Big)^{1/2},
\]
where $q(x,y)=\pi(x)c(x,y)$. Dividing, squaring, and adding the two parts yields
\[
 \sum_C\pi(u-\bar u_C)^2\le (2R/B^2)\mathfrak D(u).
\]
Using unordered edges is consistent with this factor $2R$.

3. For $f_t^x(y)=P_t(x,y)/\pi(y)$, differentiating relative entropy with unordered-edge sums and using
$(a-b)(\log a-\log b)\ge4(\sqrt a-\sqrt b)^2$
gives
\[
 \int_0^T\sum_x\pi(x)\mathfrak D(\sqrt{f_t^x})\,dt\le H(\pi)/4.
\]
Hence at some common time $t\le T$, the squared deviations $r_x^2$ of $\sqrt{f_t^x}$ from their $\pi$-means on $C$ satisfy
\[
 \sum_x\pi(x)r_x^2\le RH(\pi)/(2TB^2).
\]
The source's regularization by a positive constant covers vanishing densities.

4. Cauchy–Schwarz on $C$ gives $\sum_C\pi|f_t^x-a_x^2|\le2r_x$, since $a_x^2\pi(C)\le1$. Normalization then gives
\[
 \|P_t(x,\cdot)-\pi\|_{\rm TV}
 \le2r_x+\sum_{C^{\rm c}}\pi(y)(f_t^x(y)+1).
\]
The last term has $\pi$-average exactly $2\pi(C^{\rm c})$ by stationarity, even when trajectories leave $C$. Another Cauchy–Schwarz inequality produces precisely the lemma's displayed constant; total-variation contraction passes from $t$ to $T$.

The final application also has the stated sign and scale: with $B=\exp(-n^{1-b/20})$ and $T=\exp(n^{1-b/40})$,
\[
 \log\frac{n}{B\sqrt T}
 =\log n+n^{1-b/20}-\tfrac12n^{1-b/40}\longrightarrow-\infty
\]
because $1-b/40>1-b/20$ for the fixed positive $b$. The identity $b/40=1/40000000$ gives $b=1/1000000$. Markov's inequality at the distance threshold $1/4$ then bounds the bad Gibbs mass by four times the averaged distance.

**Finding:** no gap found in this finite-chain lemma or in that final conversion, under its stated hypotheses. This does not check the SK-specific estimates supplying those hypotheses, and gives no evidence for T045.

