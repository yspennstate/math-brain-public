# T046: Lifshitz law for low-temperature Ising Glauber dynamics

Checked 14 November 2026. Verdict: **NOT-THIS** for all three candidates. None claims the stated two-dimensional plus-boundary mixing law, or a special case of it. This is a comparison of claims, not a judgment that the proofs are correct.

## The statement being checked

For rate-one-per-site continuous-time Glauber dynamics of the nearest-neighbour ferromagnetic Ising model on an L × L square with fixed plus boundary, at each fixed positive temperature below the critical temperature, the claim is

\[
c_\beta L^2\le t_{\mathrm{mix}}\le C_\beta L^2.
\]

Mixing time here has its usual worst-initial-state meaning. The constants may depend on temperature. Zero temperature is a separate endpoint, not a consequence of a theorem for fixed finite inverse temperature.

## Candidate 1

**OpenAI, “A typical-start upper bound for low-temperature SK Glauber dynamics,” September 24, 2026.** Opened the [22-page manuscript PDF](https://mathcommunity.github.io/oai-math-revised/papers/A-typical-start-upper-bound-for-low-temperature-SK-Glauber-dynamics-September-24-2026/paper.pdf), its [raw introduction source](https://raw.githubusercontent.com/openai/math/main/preprints/A-typical-start-upper-bound-for-low-temperature-SK-Glauber-dynamics-September-24-2026/build/introduction.tex), and its [release README](https://raw.githubusercontent.com/openai/math/main/preprints/A-typical-start-upper-bound-for-low-temperature-SK-Glauber-dynamics-September-24-2026/README.md).

The model has independent standard Gaussian couplings between every pair of n spins, with Hamiltonian

\[
H_n^J(\sigma)=n^{-1/2}\sum_{i<j}J_{ij}\sigma_i\sigma_j.
\]

Its state-specific time is the first time that the transition law from the realized, fixed configuration is within total-variation distance 1/4 of the Gibbs law. The main statement, Theorem 1 on PDF p. 2, is quoted in full below, with mathematical typesetting retained:

> **Theorem 1 (Mixing from a typical Gibbs state).** For every fixed $\beta>1$, there is $c_\beta\in(0,1)$ such that
>
> $$\mathbb P_{J,\,\sigma_0\sim\pi_{n,\beta}^J}
> \left\{T_{n,\beta}^J(\sigma_0)\le\exp\bigl(n^{1-c_\beta}\bigr)\right\}
> \longrightarrow1\qquad\text{as }n\longrightarrow\infty.$$
>
> The exponent is independent of $n$ and of the realized disorder.
> The proof permits $c_\beta=1/40000000$ for every fixed $\beta>1$.

This is an upper bound for a typical Gibbs-sampled start in a random complete-graph spin glass. It gives no worst-start bound, square-lattice result, plus-boundary result, or quadratic mixing estimate. Drawing the initial spin from equilibrium and then holding it fixed is essential: averaging it inside the transition law would make the distance identically zero.

## Candidate 2

**OpenAI, “The low-temperature Sherrington–Kirkpatrick free-energy limiting law,” September 24, 2026.** Opened the [126-page manuscript PDF](https://mathcommunity.github.io/oai-math-revised/papers/The-low-temperature-Sherrington-Kirkpatrick-free-energy-limiting-law-September-24-2026/The-low-temperature-Sherrington-Kirkpatrick-free-energy-limiting-law-September-24-2026.pdf) and [release README](https://raw.githubusercontent.com/openai/math/main/preprints/The-low-temperature-Sherrington-Kirkpatrick-free-energy-limiting-law-September-24-2026/README.md).

Here $F_n(\beta)=\log\sum_\sigma e^{\beta H_n(\sigma)}$, $s_n(\beta)^2=\operatorname{Var}F_n(\beta)$, and $X_n(\beta)=(F_n(\beta)-\mathbb EF_n(\beta))/s_n(\beta)$. The randomness is the Gaussian coupling disorder. Both principal theorems on PDF p. 3 are quoted in full:

> **Theorem 1.1 (Limiting law).** For every fixed real $\beta>1$, there is a nondegenerate Borel probability measure $\nu_\beta$ such that
>
> $$X_n(\beta)\Longrightarrow\nu_\beta\qquad\text{as }n\to\infty\text{ through all integers}.$$
>
> The measure $\nu_\beta$ has mean zero, variance one, and a finite exponential moment in a neighborhood of the origin. It is the unique probability measure with the moments specified in Proposition 1.3 below.

For the next statement, the paper defines $F_n^c=F_n(\beta)-n\log2+\zeta_n$, with independent centered Gaussian $\zeta_n$ of variance $\beta^2/2$, and $Y_n=n^{-1/6}(F_n^c-\mathbb EF_n^c)$.

> **Theorem 1.2 (Moment convergence at the fluctuation scale).** For each fixed $\beta>1$, there are real numbers $a_k=a_k(\beta)$, $k\ge1$, with the following property. For every integer $k\ge1$, there are constants $c_k>0$ and $C_k<\infty$ such that
>
> $$\left|\mathbb EY_n^k-a_k\right|\le C_kn^{-c_k},\qquad n\ge2.\tag{1.4}$$
>
> There are also constants $c>0$ and $C<\infty$, depending on $\beta$, for which
>
> $$\sup_{n\ge2}\mathbb Ee^{c|Y_n|}\le C.\tag{1.5}$$
>
> The limits satisfy $a_1=0$ and $0<a_2<\infty$.

These concern equilibrium free-energy fluctuations. Neither statement specifies a Markov chain or a mixing time. A fluctuation law in Gaussian disorder cannot be read as a coarsening or mixing law on a two-dimensional ferromagnet.

## Candidate 3

**OpenAI, “The low-temperature Sherrington–Kirkpatrick fluctuation scale,” September 24, 2026.** Opened the [actual introduction source](https://raw.githubusercontent.com/openai/math/main/preprints/The-low-temperature-Sherrington-Kirkpatrick-fluctuation-scale-September-24-2026/build/sections/introduction.tex), [main source wrapper](https://raw.githubusercontent.com/openai/math/main/preprints/The-low-temperature-Sherrington-Kirkpatrick-fluctuation-scale-September-24-2026/build/paper.tex), and [release README](https://raw.githubusercontent.com/openai/math/main/preprints/The-low-temperature-Sherrington-Kirkpatrick-fluctuation-scale-September-24-2026/README.md). The raw PDF route returned an unsupported-content-type error, but the theorem source was readable.

Here $H_n(\sigma)=\beta n^{-1/2}\sum_{i<j}g_{ij}\sigma_i\sigma_j$, $Z_n=2^{-n}\sum_\sigma e^{H_n(\sigma)}$, and $F_n=\log Z_n$. The deterministic normalization differs from Candidate 2 by $n\log2$ and does not affect centered fluctuations. The complete main theorem environment reads:

> **Theorem.** For every fixed $1<\beta<\infty$,
>
> $$\operatorname{sd}(F_n)=n^{1/6+o(1)},\qquad\operatorname{Var}(F_n)=n^{1/3+o(1)}.$$
>
> More explicitly, for every $\eta>0$ there is $n_0(\beta,\eta)$ such that
>
> $$n^{1/6-\eta}\le\operatorname{sd}(F_n)\le n^{1/6+\eta}
> \qquad(n\ge n_0(\beta,\eta)).$$
>
> Moreover, for every $\eta>0$,
>
> $$\mathbb P\!\left(n^{1/6-\eta}\le|F_n-\mathbb EF_n|
> \le n^{1/6+\eta}\right)\longrightarrow1.$$

This is an exponent claim for equilibrium disorder fluctuations. It supplies neither a constant-prefactor asymptotic nor a limiting distribution, and no dynamics result. It covers no part of the target mixing statement.

## Comparison with every clause of T046

| Clause in our statement | Typical-start dynamics paper | Limiting-law and fluctuation-scale papers |
|---|---|---|
| Ising ferromagnet with nearest-neighbour interactions | Gaussian SK spin glass; interactions between every pair, with random signs | Same Gaussian SK model |
| Two dimensions | No spatial dimension; n interacting spins on a complete graph | Same |
| L × L box | No square box or side length | Same |
| Plus boundary conditions | Zero external field; no geometric boundary | Same |
| Continuous time; rate one per site | Matches this clock convention exactly | No dynamics or clocks |
| Every fixed temperature below the Ising critical temperature | Every fixed finite SK inverse temperature beta > 1; a different model and critical threshold | Same SK range |
| Mixing time from worst initialization | Time from a Gibbs-sampled realized state, with high joint probability over state and disorder | Free-energy variance, typical magnitude, and distribution |
| Order L^2, with temperature-dependent constants | Stretched-exponential upper bound only; no quadratic conclusion | Fluctuation powers 1/6 and 1/3; no mixing bound |

Even formally setting n=L^2 would turn the first upper bound into $\exp(L^{2(1-c_\beta)})$, not $O(L^2)$, and would not change the model or the starting-state quantifier. Shared words such as “Ising,” “low temperature,” and “Glauber” do not identify the same mathematical problem.

## Follow-ups and formalization

1. Opened the primary [Hexagon record for “Lower and Upper Bounds for Glauber Dynamics from Typical States of the Low-Temperature Sherrington–Kirkpatrick Model”](https://hexagonmath.org/2610.00402?version=1), by **P. M. Aronow and Patrick Lopatto**, version 1, October 20, 2026. It claims a stronger SK typical-start upper bound $\exp(n^{1-\omega})$ for fixed $0<\omega<1/4$, and stronger lower bounds. Its provenance explicitly describes AI-generated work. This is neither a reissue of the candidates on arXiv nor a statement about two-dimensional plus-boundary mixing.

2. Opened their accompanying [fluctuations-palomar repository](https://github.com/pmaronow/fluctuations-palomar). Its README lists five formalized result groups, including the strengthened continuous-time SK upper bound and the fluctuation exponents. It expressly excludes the fluctuation limiting law and positive variance prefactor. Verification receipts refer to particular revisions, and a later strengthened interface has pending replay checks. These are recorded scope claims; no Lean build or comparator audit was run here.

3. Opened [“Free energy fluctuations of symmetric perceptron models up to and including criticality”](https://arxiv.org/abs/2610.31736), by **Hang Du, Shuyang Gong, Brice Huang, Zhangsong Li**, submitted October 22, 2026, and its [HTML manuscript](https://arxiv.org/html/2610.31736v1). Its subject is perceptron fluctuations. The community catalogue reports a citation to the SK limiting-law paper, but the citation passage was not successfully retrieved on subsequent requests; that reported citation is not used as evidence of proof validation.

4. Opened [Latent Seminar, “SK dynamics across the temperature transition”](https://lowrank.github.io/latent-seminar/OpenAI-Math/227-sk-dynamics). It is an exposition, explicitly says no Lean build or manuscript-to-formal-statement equivalence check was performed, and says the low-temperature upper-bound companion is outside the release's selected family formalizations.

5. Opened the release's [family-227 Lean scope note](https://raw.githubusercontent.com/openai/math/main/lean/docs/227.md), [formalization catalogue](https://raw.githubusercontent.com/openai/math/main/lean/formalization.yaml), [contents](https://raw.githubusercontent.com/openai/math/main/CONTENTS.md), and [history](https://raw.githubusercontent.com/openai/math/main/history.md). The scope note lists a low-temperature SK mixing obstruction, not Candidate 1's upper bound. No family-217 scope file was retrieved, and the catalogue search did not identify a formalized limiting law. The history examined did not name a correction or withdrawal of these three manuscripts.

6. Opened the release's [historical `SKFluctuations/EventuallyNatPos.lean`](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/lean/OAI/Probability/SKFluctuations/EventuallyNatPos.lean). Its declaration `main_of_positiveLaplaceWindow (hw : PositiveLaplaceWindow) : MainFluctuationStatement` explicitly assumes the positive-Laplace-window input. This file alone does not show an unconditional formalization. The external package in item 2 claims to supply that input.

7. Opened the community catalogue pages for the [dynamics candidate](https://mathcommunity.github.io/oai-math-revised/papers/A-typical-start-upper-bound-for-low-temperature-SK-Glauber-dynamics-September-24-2026/) and [limiting-law candidate](https://mathcommunity.github.io/oai-math-revised/papers/The-low-temperature-Sherrington-Kirkpatrick-free-energy-limiting-law-September-24-2026/). Their collected notes are expressly unreviewed. A further mean-bias follow-up link, Hexagon 2610.00177v1, could not be read; its reported conclusions are not adopted here.

Exact-title web searches with “error refutation arxiv” found no direct refutation, error report, referee report, or arXiv version of any of the three candidates in the returned results. No expert validation was established. These are bounded search findings, not assertions of nonexistence. The file access failures and searches are recorded in LOG.md.

## Existing Ising result and recommended row text

Opened the arXiv record for **Eyal Lubetzky, Fabio Martinelli, Allan Sly, Fabio Lucio Toninelli**, [“Quasi-polynomial mixing of the 2D stochastic Ising model with ‘plus’ boundary up to criticality”](https://arxiv.org/abs/1012.1271). Its abstract gives $L^{c\log L}$ for every fixed beta above the Ising critical point. Also opened **Reza Gheissari and Allan Sly**, [“Rapid phase ordering of Ising dynamics on $\mathbb Z^2$”](https://arxiv.org/html/2605.08052v1), May 8, 2026: its introduction calls polynomial plus-boundary mixing a longstanding open problem, and its argument uses a quasi-polynomial input. The zero-temperature arXiv records [1112.3160](https://arxiv.org/abs/1112.3160) and [1102.3466](https://arxiv.org/abs/1102.3466) were also opened; no change to that part of the supplied note is proposed.

Recommended “where it stands” text (three sentences):

The positive-temperature two-dimensional plus-boundary problem remains open in the literature checked: the established general upper bound is quasi-polynomial, and Gheissari–Sly's rapid phase ordering from sufficiently biased independent initial spins does not give worst-start polynomial mixing. OpenAI's “A typical-start upper bound for low-temperature SK Glauber dynamics” (September 24, 2026) concerns a Gaussian complete-graph spin glass and claims a subexponential typical-start bound. Its “The low-temperature Sherrington–Kirkpatrick free-energy limiting law” and “The low-temperature Sherrington–Kirkpatrick fluctuation scale” (both September 24, 2026) concern equilibrium fluctuations, so none of these preprints settles T046.

## Spot check

Selected **Lemma 8, “Pruning and averaged mixing,”** in Candidate 1, PDF pp. 19–21. It is the final essential bridge from balanced-cut flow to mixing from a typical fixed state. The check below concerns that bridge only; the difficult SK flow estimate feeding it is not verified.

Write $Q(S,S^c)=\sum_{x\in S,y\notin S}\pi(x)c(x,y)$. The hypotheses are reversibility on a finite state space with positive stationary law, total outgoing rate at most R, $0<\varepsilon<1/3$, and $Q(S,S^c)>B$ whenever $\varepsilon\le\pi(S)\le1-\varepsilon$. The claimed conclusion is

\[
\sum_x\pi(x)\|P_T(x,\cdot)-\pi\|_{\rm TV}
\le\frac{\sqrt{2R H(\pi)}}{B\sqrt T}+2\varepsilon.
\]

**Pruning.** Remove sets U from the current C when $\pi(U)\le\pi(C)/2$ and $Q(U,C\setminus U)<B\pi(U)$. For the union A of removed sets, boundary edges are included among the edges counted on removal, so $Q(A,A^c)<B\pi(A)$. At the first removal that could reach mass epsilon, the old mass a is below epsilon and the new mass is at most $(1+a)/2<(1+\varepsilon)/2<1-\varepsilon$. This would contradict the balanced-cut assumption. Thus the surviving C has mass greater than $1-\varepsilon$ and internal expansion at least B in the original, unnormalized weights. The strict inequality and the restriction epsilon < 1/3 are both used.

**Poincaré constant and rate convention.** With unordered-edge energy $D(u)=\sum_{\{x,y\}}\pi(x)c(x,y)(u(x)-u(y))^2$, integrate the expansion inequality over squared positive and negative parts around a weighted median. Cauchy–Schwarz and the outgoing-rate bound give

\[
B\sum_C\pi w^2\le
\sqrt{D_C(w)}\sqrt{2R\sum_C\pi w^2},
\qquad
\sum_C\pi(u-\bar u_C)^2\le\frac{2R}{B^2}D(u).
\]

No factor of n is inserted by this finite-state step. In its heat-bath application R=n because each of n sites has rate one.

**Entropy and the complement of C.** For $f_t^x(y)=P_t(x,y)/\pi(y)$, direct differentiation of relative entropy, using $(a-b)(\log a-\log b)\ge4(\sqrt a-\sqrt b)^2$, gives

\[
\int_0^T\sum_x\pi(x)D(\sqrt{f_t^x})\,dt\le H(\pi)/4.
\]

There is therefore one common time t at most T with mean retained-set squared deviation at most $RH(\pi)/(2TB^2)$. If $r_x$ is the square root of that deviation, comparing $f_t^x$ with its retained-set square-root mean squared gives retained-set L1 error at most $2r_x$. Normalization then bounds total L1 distance by $4r_x+2\sum_{C^c}\pi(f_t^x+1)$. The latter sum has average $2\pi(C^c)$ by stationarity. Dividing by two for total variation and using Cauchy–Schwarz gives exactly the displayed constant; contraction takes the estimate from t to T. This checks why trajectories need not be confined to C and why the result remains an average over realized fixed starts.

**Exponent substitution.** In the paper's application, $B=\exp(-n^{1-b/20})$ and $T=\exp(n^{1-b/40})$. The logarithm of the nonconstant factor $n/(B\sqrt T)$ is

\[
\log n+n^{1-b/20}-\tfrac12n^{1-b/40}\longrightarrow-\infty,
\]

since $1-b/40>1-b/20$. Thus this conversion has the stated sign. Markov's inequality turns the vanishing average distance into a vanishing Gibbs mass of states with distance greater than 1/4; it does not turn it into a worst-start bound. No discrepancy was found in this finite-state calculation. This does not certify the upstream SK estimates or either fluctuation paper.
