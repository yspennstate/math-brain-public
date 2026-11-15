NO_PROGRESS

# D0093: topplings in the fast phase of activated random walk on a cycle

No proof of a linear upper bound for the conservative cycle is obtained here, even with the weaker requirement that its probability tend to one. No counterexample to that bound is obtained either. The literature search through 13 November 2026 did not find a theorem establishing the requested bound on this graph. This is a report of an unsuccessful attempt, with a corrected diagnosis of the existing proof, rigorous limitations of two proposed approaches, and numerical evidence below.

The logarithms in the published construction are not a site union bound followed by a logarithmic number of rounds. The construction first gathers particles at sources separated by order log n. This gathering alone costs order n log² n with high probability. A second finding is that geometric domination of the actual site odometer, uniformly in cycle size, is impossible: a recent infinite-line theorem forces a stretched-exponential lower tail in a suitable large-cycle limit. Neither fact disproves a linear bound for the sum of odometers.

## 1. Exact problem, model, and source locations

The primary source is L. T. Rolla, *Activated Random Walks on Z^d*, Probability Surveys **17** (2020), 478–544, [arXiv:1906.05037v2](https://arxiv.org/abs/1906.05037v2), [journal DOI](https://doi.org/10.1214/19-PS339). The downloaded text is [sources/rolla_2020_1906.05037v2.txt](sources/rolla_2020_1906.05037v2.txt). In this version PDF page k has printed page 477+k. Theorem 6.1 and its open problems are on PDF p.30 / printed p.507.

The graph is the conservative cycle Z/nZ, with no sink. Initially the number of particles at each site is independent Poisson(ζ), and every particle is active. An active particle jumps to either nearest neighbor with probability 1/2 at total rate 1. When alone it sleeps at rate λ>0. An arrival wakes a sleeping particle immediately.

Equivalently, each site has an independent stack of instructions, with probabilities

\[
 p=\frac{\lambda}{1+\lambda}\quad\hbox{(sleep)},\qquad
 \frac1{2(1+\lambda)}\quad\hbox{(left or right)}.
\]

A legal toppling consumes one instruction at a site containing an active particle. A sleep instruction at a site with at least two particles has no effect but is counted. Let m_n(x)=m_{Z_n,η_0}(x) be the stabilizing odometer and T=Σ_x m_n(x). This counts instructions, not continuous elapsed time and not only jumps. The abelian property makes the odometer independent of the chosen complete legal order. With Poisson data the event N>n has positive probability; stabilization is then impossible and T=∞. Its probability decays exponentially for fixed ζ<1 and is allowed by the high-probability estimates.

Here is the complete mathematical content of Theorem 6.1, preserving its quantifiers and constants while restating the prose. For each 0<ζ<1:

- For sufficiently small λ, there are δ,δ'>0 such that, for all sufficiently large n,
  \[
  \mathbb P(T\ge e^{\delta'n})\ge1-e^{-\delta n}. \tag{6.2}
  \]
- For sufficiently large λ, there are δ>0 and κ<∞ such that, for all sufficiently large n,
  \[
  \mathbb P(T\le\kappa n\log^2 n)\ge1-n^{-\delta}. \tag{6.3}
  \]

The explicit regime used in the proof of the second assertion is

\[
 0<\zeta<\zeta'<\frac{\lambda}{1+\lambda}, \tag{6.4}
\]

on PDF p.32 / printed p.509. Thus, for any fixed ζ<1, λ>ζ/(1−ζ) suffices. The phrase “fast phase” in this report distinguishes this proved region from the larger subcritical region ζ<ζ_c(λ). Later work proves the n log² n estimate throughout the latter region for a uniform fixed-mass initial configuration; see below.

The second open problem after the theorem is, exactly:

> Improve the estimate (6.3) to one without the log² n term.

That is the question whether, for fixed parameters in the relevant fast regime, there exist finite C and δ>0 with P(T≤Cn)≥1−n^{-δ} for all sufficiently large n. The first open problem concerns extending the dichotomy to the entire off-critical region; it is a separate issue. The third asks for tightness of a site odometer; it is also separate.

## 2. Literature audit before attempting a new bound

The source cited for Theorem 6.1 is R. Basu, S. Ganguly, C. Hoffman and J. Richey, *Activated Random Walk on a cycle*, Ann. Inst. H. Poincaré Probab. Statist. **55** (2019), 1258–1277, [arXiv:1709.09163v2](https://arxiv.org/abs/1709.09163v2), [DOI](https://doi.org/10.1214/18-AIHP918). Its text is saved in sources/.

Its **Theorem 1, preprint p.2**, proves P(T_n>C_0 n log² n)≤n^{-b}, for every λ>0 and μ<λ/(1+λ). Its initial data are iid Bernoulli(μ), whereas the survey explicitly uses Poisson data. **Theorem 2, preprint p.3**, gives P(T_n<e^{cn})<e^{-cn} for sufficiently small λ at any fixed μ∈(0,1). The survey's fast proof handles Poisson data directly by Poisson splitting. The original preprint says on p.3 that the precise Bernoulli law is not essential. These statements do not remove logarithms.

Page numbers below refer to the saved preprint version unless journal pagination is explicitly specified. The most directly relevant subsequent papers are:

| Work and saved text | Exact result/location checked | Consequence for D0093 |
|---|---|---|
| Hoffman–Johnson–Junge, [*The density conjecture for activated random walk*](https://arxiv.org/abs/2406.01731v2), 2024; hoffman_johnson_junge_2406.01731v2.txt | Theorem 1.1, p.5, identifies four critical densities. Proposition 8.12(i), pp.67–68, gives P(τ_n>Cn log² n)≤n^{-b} and P(τ_n>C'n⁴)≤B exp(−b'n) for every ρ<ρ_c. It starts with floor(ρn) particles placed uniformly on the cycle. Part (ii) gives exponential slow behavior for ρ>ρ_c. | Extends the regime of the old bound, retaining both logarithms. The corresponding Poisson extension follows from the same source construction and Proposition 8.7; see the deduction below. |
| Johnson–Richey, [*The odometer in subcritical activated random walk*](https://arxiv.org/abs/2510.05514v3), 2025 preprint / ECP **31** (2026), paper 74, [DOI](https://doi.org/10.1214/26-ECP819); johnson_richey_2510.05514v3.txt | **Theorem 1.1, p.2/12**, for iid Bernoulli(ρ) data on **Z**, 0<ρ<ρ_c(λ): c_1 exp(−c_2√t)≤P(m_Z(0)≥t)≤c_3 exp(−c_4√t). **Corollary 1.2**, same page: E[m_Z(0)]<∞. | Establishes an integrable, sharp-order marginal tail on Z. It does not state a conservative cycle result. Its p.3 describes extension to light-tailed initial laws as something the proofs should provide; that remark is not a proved Poisson theorem. |
| Levine–Liang, [*Exact sampling and fast mixing of Activated Random Walk*](https://arxiv.org/abs/2110.14008), 2021 preprint / 2024 publication; levine_liang_2110.14008.txt | Exact stationary sampling and volume-order mixing for a driven, dissipative chain; Corollary 5, p.12 of the saved preprint, is the Euclidean-ball mixing bound. | One chain step includes adding a particle **and stabilizing it**. Linear mixing in this clock does not bound the instructions spent stabilizing a conservative initial configuration. |
| Bristiel–Salez, [*Separation cutoff for Activated Random Walks*](https://arxiv.org/abs/2209.03274), 2022 preprint / 2024 publication; bristiel_salez_2209.03274.txt | Theorem 1, p.5: relaxation time; Theorems 2–3, p.6: mixing window and mixing-time estimates, with absorption at a boundary/sink. | Same clock and model distinction. No linear conservative-cycle toppling theorem. |
| Hoffman–Johnson–Junge–Meisel, [*Cutoff for activated random walk*](https://arxiv.org/abs/2501.17938), 2025; hoffman_johnson_junge_meisel_2501.17938.txt | Theorem 1.1, p.2: driven interval chain mixes after (ρ_c+ε)n additions, with an exponential error; converse before (ρ_c−ε)n. | Linear in additions, not topplings. |
| Hoffman–Johnson–Junge–Meisel, [*Activated random walk exhibits self-organized criticality*](https://arxiv.org/abs/2605.00207), 2026; hjjm_soc_2605.00207.txt | Theorems 1–2, p.7: stationary density and volume-order mixing in the driven interval. | Does not supply the missing conservative bound. |
| Johnson–Junge–Meisel, [*Stationary activated random walk: regularity, heavy tails, and remixing*](https://arxiv.org/abs/2609.31843), September 2026; johnson_junge_meisel_2609.31843.txt | Theorems 1.1–1.3, pp.2–4: stationary interval density regularity, avalanche-area tails and remixing; driven-dissipative setup. | Different initial law and clock. |

For completeness, a Poisson version throughout ζ<ρ_c follows from the source construction: choose ζ<ζ'<ζ''<ρ_c, gather at sources with radius r as in the survey, and bound every load by 2ζ'r using Poisson concentration. For Stage 2 apply HJJ **Proposition 8.7, p.64**, to M=floor(2ζ'r) particles at each source. Choosing its ε so that ρ_c−ε=ζ'' gives a visited radius at most M/(2ζ'')<r, with error C exp(−cM)≤C exp(−c'r). Fewer particles are contained by particle monotonicity. Fresh unused stacks after gathering have their original iid law. The survey's cost argument then gives Cnr², and the same union bound with r=K log n proves the extension. This is a deduction from printed results, not a printed O(n) theorem.

Further primary papers were checked for their models and main theorems: Asselah–Rolla–Schapira ([1907.12694](https://arxiv.org/abs/1907.12694), diffusive critical-density bounds); Hoffman–Richey–Rolla ([2009.09491](https://arxiv.org/abs/2009.09491), active phase on Z); Forien–Gaudillière ([2203.02476](https://arxiv.org/abs/2203.02476), exponentially slow torus stabilization); de Lima–Rolla–Terra ([2408.07049](https://arxiv.org/abs/2408.07049), slow phase on a ring for arbitrary fixed sleep rate); Forien ([macroscopic flow, 2025](https://alea.impa.br/articles/v22/22-21.pdf), Theorems 1.3–1.5 on pp.3–4 / journal pp.559–560; and [2502.02579v2](https://arxiv.org/abs/2502.02579v2), a new proof of the density conjecture). Texts are saved for all these papers. Asselah–Forien–Gaudillière ([2210.04779v2](https://arxiv.org/abs/2210.04779v2), Theorem 1.1 on p.3) establishes ρ_c<1 for every λ and dimension, using slow torus stabilization, and also does not remove the fast-phase logarithms. None of these statements is an O(n) upper bound for the problem here.

Hoffman–Hu–Richey–Rizzolo ([2212.08293](https://arxiv.org/abs/2212.08293)) concerns the **stochastic sandpile**, rather than the present ARW model. Cairns–Ganguly–Levine's [full-density cycle manuscript](https://hannahcairns.info/files/activated-random-walk-on-full-cycle.pdf), Theorem 2.1 on p.2, concerns exactly one particle per site and a sleep rate scaling like (1/2)log n; it gives a quadratic expected fast bound and does not address fixed λ and iid Poisson density ζ<1.

The older Sidoravicius–Teixeira [1412.7098](https://arxiv.org/abs/1412.7098), published 2017, was also checked because Johnson–Richey cite its small-density quantitative bound. Theorem 2.1, p.7 of the saved preprint, bounds the number of changes at the origin by exp(−c log² t). Its finite-box results concern dissipation. It is not a printed linear-time conservative-cycle theorem. The distinction between a count of changes and a physical last-activity time must be preserved: the introduction's informal time description is not a substitute for its theorem statement.

Searches included the named authors, both spellings of stabilization/stabilisation, cycle/ring/torus, number of topplings/instructions, odometer, linear time, fast phase and fast mixing, with 2019–2026 followups. The phrase “Activated random walk on the cycle: fast mixing” did not yield a distinct relevant primary theorem; the actual fast-mixing papers above were checked. A literature search can miss a result; the claim here is what these sources establish, not a certificate that no other result exists.

Source texts retain form-feed page separators. sources/manifest.jsonl records URLs, extraction dates, PDF hashes of bytes processed **in memory**, text hashes and page counts. No PDF or page image was saved.

## 3. Audit of the proof of (6.3)

The fast proof is **Section 6.2**, PDF pp.32–35 / printed pp.509–512. Section 6.1 is the slow-phase proof. The following follows the successive paragraphs and estimates of Section 6.2.

| Location and step | Estimate or construction | Role of logarithms |
|---|---|---|
| p.509, (6.4) | Choose ζ<ζ'<p=λ/(1+λ). | A fixed parameter gap, no n-dependent loss. |
| p.509, next paragraph | Set r=floor(K log n); partition into arcs of 2r+1 sites, allowing spare sites. The midpoint is a source. | This is the single spatial scale that supplies log n. |
| p.509, Stage 1 | Force each particle, using acceptable topplings, to the first source it reaches. Sleep instructions act as lazy steps. Abort if some source receives more than 2ζ'r particles. | Distances of order r are imposed artificially. |
| p.509, Stage 2 | Legally stabilize each source population; abort if a particle leaves its arc. | No cycles of repeated rounds. |
| p.510, first paragraph | An individual lazy exit time over distance 3r is dominated by Cr²G, G geometric with mean 2. Sum at most n independent completed paths and use a Chernoff bound. | Diffusion squares r. The sum costs Cnr² with error exp(−cn), with no additional log from maximizing individual times. |
| p.510, Stage 1 cost | Every gathering path is such a stopped lazy walk. N<n on the success event. | Cost Cnr². |
| p.510, Stage 2 cost | Extend stopped particle paths with fresh randomness to independent lazy walks. Bound the intersection of containment and an excessive cost by the completed-walk tail. | Another Cnr², added to the first, not multiplied by a number of rounds. No independence conditional on containment needs to be asserted. |
| p.510, Stage 1 load | Poisson thinning: source load has mean at most 2ζr+2. Chernoff gives exp(−cr) for overload at one source. Sum over order n/r sources. | Require (n/(2r+1))exp(−cr)≤n^{-δ}; choose K large. |
| p.511, Proposition 6.5 | With m≤2ζ'r particles at one source, containment in [−r,r] fails with probability at most exp(−cr). Sum over the arcs. | The same r≥constant·log n requirement. |
| pp.511–512, proof of Proposition 6.5 | Two trap barriers approach the source. Their increments have geometric parameter p. An urn/internal-erosion argument controls imbalance; Lemma 6.7 gives failure exp(−cr). | No further log n in the cost. |
| BGHR §§3.3–3.4, pp.12–16 | Trap construction; Lemmas 3.9–3.12, geometric increments and exponential-clock coupling. The O(r) union bound internal to the concentration estimates is absorbed into exp(−c'r). | It does not create a separate global factor of log n. |

Combining the two costs and two failure bounds yields

\[
 \mathbb P(T>Cnr^2)\le C'\frac nr e^{-cr}+C'e^{-c'n},
 \qquad r=\lfloor K\log n\rfloor,
\]

after adjusting constants, for all sufficiently large n. This is (6.3). In the original paper the corresponding steps are Lemmas 3.1–3.4, pp.8–10; Proposition 3.5 and Lemma 3.6, pp.10–11; and the proof of Theorem 1, p.11. Some displayed expressions in the preprint have typographical problems, including the sign in (3.6); the relevant qualitative concentration conclusion is an exponentially small **upper** bound, as used in the argument.

## 4. Checked mathematical deductions and failed routes

### 4.1 Gathering at logarithmic spacing intrinsically costs n log² n

**Proposition.** Fix ζ>0 and finite λ>0. Place sources every L sites on a cycle with L dividing n. Let S be the instructions used to gather all iid Poisson(ζ) particles at their first source, ignoring sleep instructions as in Stage 1, without aborting at overload. Then

\[
 \mathbb E S=\frac{\zeta(1+\lambda)}6\,n(L^2-1).
 \tag{A}
\]

For L≥16,

\[
 \mathbb P\left(S<\frac{\zeta}{1024}nL^2\right)
 \le e^{-\zeta n/32}.
 \tag{B}
\]

**Proof.** Between sources identify the sites with 0,…,L. Let H_j be the number of instructions to hit {0,L} from j. Its mean solves

\[
 h_0=h_L=0,\qquad
 h_j=1+p h_j+\frac{1-p}{2}(h_{j-1}+h_{j+1}).
\]

The solution is h_j=(1+λ)j(L−j). This can also be checked by stopping the martingale associated with the potential j(L−j), whose expected decrement per instruction is 1/(1+λ). Summing over j=0,…,L−1 gives L(L²−1)/6, and multiplying by ζn/L proves (A).

For (B), at least n/3 sites have distance at least L/4 from the nearest source. Set t=floor(L²/64). For an unabsorbed lazy walk W starting at one of those sites, the displacement martingale has variance at time t at most t. Kolmogorov's maximal inequality gives

\[
 \mathbb P(\max_{s\le t}|W_s-W_0|\ge L/4)
 \le16t/L^2\le1/4.
\]

Thus each particle initially at such a site has probability at least 3/4 of requiring more than t instructions. Under the particlewise construction these walks are independent; this has the same law as exposing fresh iid site instructions in Stage 1. Independent Poisson marking shows that the number M of these long paths is Poisson with mean at least ζn/4. Its Chernoff lower tail gives P(M<ζn/8)≤exp(−ζn/32). Since t≥L²/128 for L≥16, S≥Mt gives (B). ∎

For the actual algorithm, (B) applies to the intersection of successful completion with an abnormally cheap gathering stage; the aborted cost is not asserted to satisfy (B).

**Why reducing L also fails for this algorithm.** Source populations after completed gathering are independent Poisson(ζL), by Poisson splitting and translation symmetry. If the allowed population is αL for fixed α>ζ, let q_L=P(Poisson(ζL)>αL). A single Poisson term, with k=floor(αL)+1, gives q_L≥exp(−CL) for some finite C=C(ζ,α): use k!≤k^k and k≤(α+1)L. Hence

\[
 \mathbb P(\hbox{every source meets its cap})
 =(1-q_L)^{n/L}
 \le\exp\left[-\frac nL e^{-CL}\right]. \tag{C}
\]

If L=o(log n), this probability tends to zero. To be at least 1−n^{-δ} it is necessary that

\[
 CL\ge(1+\delta)\log n-\log(2L)
\]

for large n. The survey's cap 2ζ'r is no larger than ζ'L for L=2r+1, so the same necessary scale applies. Together, (B) and (C) show that sharpening concentration or keeping this gathering/source-cap procedure cannot give n log n or n. A different stabilization order is needed. This is an obstruction to an **upper-bounding construction**, not a lower bound for the true T.

### 4.2 A geometric site-odometer bound cannot hold uniformly

The following deduction uses Johnson–Richey Theorem 1.1 as an external theorem; it is not a reproof of their theorem.

Fix survey-fast parameters 0<ζ<p, and set ρ=1−e^{-ζ}. Then 0<ρ<ζ<p≤ρ_c(λ). Couple iid Bernoulli(ρ) particles to the indicators of nonempty Poisson(ζ) sites. For every fixed finite interval V around 0, embedded in a sufficiently large cycle, legal topplings in V with particles frozen on exiting V are also a legal partial sequence on the cycle. Particle monotonicity therefore gives

\[
 m^{\rm cycle,Poi}_n(0)\ \ge_{\rm st}\ m^{\rm killed,Ber}_V(0).
\]

Increasing V to Z, the killed odometers increase to the infinite-volume odometer. Johnson–Richey's lower bound consequently implies, for integer t≥1,

\[
 \liminf_{n\to\infty}\mathbb P(m^{\rm cycle,Poi}_n(0)\ge t)
 \ge c_1e^{-c_2\sqrt t}. \tag{D}
\]

In particular there cannot be constants A,b>0 and errors ε_n→0 with

\[
 \mathbb P(m_n(0)\ge t)\le Ae^{-bt}+\varepsilon_n
 \quad\hbox{for every }n,t.
\]

Passing n→∞ and then t→∞ would contradict (D). Thus a uniform geometric domination of the **actual total uses at a site** is ruled out even in the survey's fast region. A scheme charging instructions to other random objects is not ruled out. An integrable stretched-exponential marginal tail is compatible with a linear sum.

### 4.3 The asserted equivalence with a uniform site tail is false

A uniform marginal tail, even exponential, does not alone imply a fixed C with P(Σ_x m_n(x)≤Cn)→1. For example, set all n entries equal to one common unbounded geometric random variable X. Every entry has the same exponential tail, but P(Σ_x m_n(x)>Cn)=P(X>C)>0 independently of n. This example is a statement about the proposed logical implication, not an ARW counterexample.

Conversely, placing value n at one uniformly chosen site and zero elsewhere gives Σ_x m_n(x)=n deterministically while the best uniform marginal tail is only of order 1/t. A linear sum cannot be equated with a particular light-tail bound for each site. Spatial concentration or localization is the missing condition. For the actual rotation-invariant cycle law, a linear high-probability bound does imply the weaker marginal bound

\[
 \mathbb P(m_n(0)>t)\le \mathbb P(T>Cn)+C/t,
\]

by counting sites with odometer greater than t on the event T≤Cn. This explains one direction of the intuition while distinguishing it from the false equivalence.

Nor does the infinite-line theorem itself upper-bound a cycle: killing at a cut suppresses return paths around the cycle and lowers the odometer. Finiteness of an infinite-line expectation is not automatically a finite-cycle domination or a uniform-integrability statement. The Poisson-to-Bernoulli coupling above goes in the direction useful for a lower bound, not the desired upper bound.

### 4.4 A precise sufficient localization criterion

Here is a conditional criterion specifying what a replacement method would need to establish. It is proved here, but its hypotheses are **not established for the cycle ARW**.

Suppose that, on the iid-input probability space of the cycle, there are nonnegative Y_{n,r}(x), each measurable from the initial data and instruction stacks at distance at most r from x, such that uniformly in n,x,r≤n/8,

\[
 \mathbb P(Y_{n,r}(x)\ne m_n(x))\le Ae^{-br},\qquad
 \mathbb E Y_{n,r}(x)\le\mu,\qquad
 \mathbb E Y_{n,r}(x)^2\le M<\infty.
\]

For every ε>0,

\[
 \mathbb P(T>(\mu+\varepsilon)n)
 \le nAe^{-br}+\frac{M(4r+1)}{\varepsilon^2n}. \tag{E}
\]

Indeed the union bound controls any mismatch. Variables whose centers are more than 2r apart have disjoint iid inputs and are independent. Cauchy–Schwarz bounds each remaining covariance in absolute value by M. Thus Var(Σ_xY_{n,r}(x))≤n(4r+1)M; apply Chebyshev. With r a sufficiently large multiple of log n, (E) gives error O(log n/n), hence n^{-δ} for any fixed δ<1 for sufficiently large n after adjusting constants. An integrable tail plus this quantitative local representation would suffice. The localization assertion is the substantive missing step, not a consequence of the cited marginal theorem.

### 4.5 What the new odometer theorem does imply on an interval

For comparison there is a genuine linear law in a different finite geometry. For iid Bernoulli(ρ) data on Z with 0<ρ<ρ_c(λ), let U_n be the total instructions stabilizing [1,n] with killing on exit. Then

\[
 \frac{U_n}{n}\longrightarrow \mathbb E_\rho m_Z(0)<\infty
 \quad\hbox{almost surely}. \tag{F}
\]

Here is the derivation. The infinite odometer is a translation-covariant measurable function of iid initial data and stacks, hence stationary and ergodic. Johnson–Richey give its finite mean. Domain monotonicity and the ergodic theorem give limsup U_n/n≤E m_Z(0). For a fixed R, and x at least R from the endpoints, the interval odometer is at least the odometer at x obtained by stabilizing [x−R,x+R] with killing. This latter field is stationary ergodic and integrable. Its spatial average converges almost surely to its mean, giving the corresponding lower bound for liminf U_n/n. Let R→∞ and use monotone convergence. Countably many R can be treated on a single probability-one event. The two bounds prove (F). In particular a fixed C larger than this mean works with probability tending to one for a killed interval. This is **not** the conservative cycle result and is not presented as answering D0093.

## 5. Computation (evidence only)

The simulator in [code/arw.cpp](code/arw.cpp) runs the original conservative cycle with iid Poisson initial counts. It uses a legal last-in-first-out queue of active sites and reads a fresh independent pseudorandom instruction at each toppling. A sleeping site has state −1; an arriving particle changes it to two active particles. At multiply occupied sites, ineffective sleep attempts are counted explicitly. The same event count is the survey's T. This computes the stabilizing odometer law by the abelian property; it does not emulate physical continuous time.

There are seven parameter pairs, all satisfying ζ<λ/(1+λ), and n=1,000; 3,000; 10,000; 30,000; 100,000. There are respectively 200, 200, 200, 100 and 60 independent seeded runs per parameter pair, for **5,320 runs**. The cap was 10,000n instructions. All runs stabilized before the cap, and none had more particles than sites; there are no censored observations to discard. Every seed and each raw count is retained in [data/runs.csv](data/runs.csv).

| ζ | λ | mean T/n, n=1,000 | mean T/n, n=100,000 (SE) | empirical q95, n=100,000 | max T/n, n=100,000 | mean ratio, large/small |
|---:|---:|---:|---:|---:|---:|---:|
| 0.02 | 0.1 | 0.2402 | 0.2432 (0.0010) | 0.2574 | 0.2648 | 1.012 |
| 0.08 | 0.1 | 1.3473 | 1.3583 (0.0041) | 1.4092 | 1.4267 | 1.008 |
| 0.1 | 1 | 0.2656 | 0.2628 (0.0006) | 0.2707 | 0.2723 | 0.989 |
| 0.2 | 4 | 0.5271 | 0.5235 (0.0018) | 0.5494 | 0.5582 | 0.993 |
| 0.4 | 1 | 3.0582 | 3.0376 (0.0090) | 3.1781 | 3.1916 | 0.993 |
| 0.75 | 4 | 52.4011 | 51.3056 (0.4507) | 56.8844 | 57.7731 | 0.979 |
| 0.8 | 10 | 208.0610 | 197.0065 (2.4409) | 225.5634 | 262.9737 | 0.947 |

SE is the sample standard deviation of T/n divided by the square root of the number of independent runs. Quantiles are linearly interpolated empirical quantiles; at the largest size there are only 60 observations. The complete five-size means, standard deviations, quantiles and maxima are in [data/summary.csv](data/summary.csv). [data/upper_tails.csv](data/upper_tails.csv) records exceedance counts over a grid of T/n thresholds; [data/site_tails.csv](data/site_tails.csv) records site-odometer exceedance fractions. Sites within a run are dependent, so those site fractions must not be treated as independent binomial samples.

For ζ=0.8, λ=10, the observed counts with T/n>250 were 51/200 at n=1,000, 29/200 at n=10,000 and 1/60 at n=100,000. These are exploratory upper-tail measurements, not uniform probability bounds.

The endpoint ratios of the means range from 0.947 to 1.012, whereas a pure proportional-to-log n model would predict log(100,000)/log(1,000)=5/3. The finite-size results support bounded T/n over this range, with a large parameter-dependent constant and shrinking upper quantiles. They do not prove boundedness for all n or exclude an eventual logarithmic correction. In particular, 60 runs cannot certify a failure probability n^{-δ}: even zero exceedances of a fixed threshold would have a one-sided 95% binomial upper confidence bound 1−0.05^(1/60)≈0.0487. No fitted δ is claimed.

Plots created from these simulations, rather than from any paper:

- [Instructions per site against cycle size, with approximate 95% mean intervals and empirical 95th percentiles](data/size_scaling.svg).
- [Normalized means against a pure logarithmic-growth reference](data/normalized_scaling.svg).

### Validation and reproducibility

1. **Abelian replay:** 360 small initial configurations, with λ=0.2,1,4,10 and n=7,19,53, were stabilized using three legal orders: queue, stack and random active-site choice. The per-site instruction stacks were retained and reused. Both the full odometer vector and final state agreed exactly in every case. This checks the interaction and instruction accounting, including failed sleep attempts.
2. **Exact single-particle law:** for λ=0.1,1,4, each of 100,000 independent trials must have T distributed as a geometric variable with success probability p, on {1,2,…}. The exact means are 11, 2 and 1.25; measured means were 10.9792, 1.99479 and 1.2491, respectively. Deviations were 0.63, 1.16 and 0.51 standard errors in absolute value. Every trial had exactly one successful sleep and no failed sleeps. See [data/verification.txt](data/verification.txt).
3. **Raw-count audit:** the simulator asserts conservation of mass, final stability, Σ_x m_n(x)=T and T=jumps+successful sleeps+failed sleeps. Python independently recomputed the identities in every CSV row, checked unique seeds, completion flags, monotone site-tail counts, and initial Poisson totals. Across parameter pairs, initial-mass standardized deviations were at most 1.93 and jump-probability martingale diagnostics at most 1.21 in absolute value. See [data/audit.json](data/audit.json); the latter diagnostics are checks, not an asymptotic limit theorem.
4. **Analytic constants:** [code/check_math.py](code/check_math.py) solves the finite hitting-time recurrence by exact rational tridiagonal elimination for 252 cases, independently checks the sum in (A), the source-intensity identity, and the elementary constants used in (B). All checks passed. This supplements, rather than replaces, the proofs. See [data/math_checks.txt](data/math_checks.txt).
5. **Resources:** one simulation worker and one computational thread, with inherited nice value 10 verified in both Python and C++. The C++ run took approximately 25.2 seconds and reported 17,629,184 bytes of peak resident memory on macOS. The sandbox rejected attempts to set an address-space/RSS resource limit; this is recorded in [data/simulation_metadata.json](data/simulation_metadata.json). The measured footprint is below 4 GB by a wide margin. No language-model worker or subagent was started.

Reproduction, from this directory (the wrapper requires inherited nice ≥10):

```sh
c++ -std=c++17 -O2 -Wall -Wextra -Wpedantic code/arw.cpp -o code/arw
./code/arw --verify > data/verification.txt
python3 code/check_math.py
python3 code/run_simulation.py
python3 code/analyze.py
```

The simulations use the standard C++ mt19937_64 generator; the initial Poisson variates and instruction stream have distinct deterministically derived seeds. Results are pseudorandom empirical evidence. The compiler identification is recorded in data/compiler.txt; exact standard-library Poisson output can depend on the C++ implementation. [code/fetch_text.py](code/fetch_text.py) reproduces PDF-to-text extraction through an in-memory download piped to pdftotext; it never writes a PDF.


## 6. Remaining mathematical question

No logarithm has been removed from a proved conservative-cycle upper bound here. The plausible next target is a cycle localization/renewal argument that controls spatial averages and handles wrapping, with a finite-mean cost, instead of gathering every particle over a logarithmic distance. In particular the proposed geometric site charging and the claimed equivalence with a marginal tail should not be used as premises.

Task: “Open problem D0093.” Received 13 November 2026, approximately 12:28 Asia/Tbilisi.
