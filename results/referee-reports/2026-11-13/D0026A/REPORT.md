PARTIAL

# D0026: convergence of one-dimensional FA-1f

Completed investigation, 13 November 2026. Literature was checked before the arguments below. No resolution of the full conjecture has been located. The rigorous result established here is convergence for every initial law with at least one infection when q>1/2. This does not settle the all-q conjecture. The report includes complete deductions from stated published inputs, a literature audit, and simulations.

The occupation variable eta_x is 0 for infection and 1 for healthy, p=1-q, and pi=Ber(p)^{tensor Z}. Thus pi(eta_x=0)=q. The constraint is c_x=1-eta_{x-1}eta_{x+1}. A legal rate-one clock resamples eta_x from Ber(p). In particular two infected neighbours do not double the clock rate.

The target is: for every q in (0,1), every local f, and every probability law nu with nu(eta is not identically 1)=1, nu P_t f tends to pi(f). No product, invariance, density or moment hypothesis is part of the target.

## A rigorous high-density partial result

**Theorem A.** If 1/2<q<1, then for every deterministic eta with at least one zero and every local f, P_t f(eta) tends to pi(f). For a fixed zero location z, convergence is exponentially fast, uniformly over all eta with eta_z=0. Consequently the convergence holds for every initial law nu supported on configurations with a zero, without any moment assumption.

We use the following published theorem as an input, with all its assumptions explicit: Blondel–Cancrini–Martinelli–Roberto–Toninelli (2013), Theorem 2.1, arXiv:1205.4584 PDF pp. 4–5. On Z, if q>1/2 and a law mu satisfies sup_x mu(theta^{d_x})<=K for some theta>1, then

|mu P_s f-pi(f)| <= C ||f||_infty exp(-s/C), s>=2,

where d_x is distance to the nearest zero, and C depends only on q, theta, K and the support size of f. We fix theta below; no uniformity as theta decreases to 1 is used. The dependence on theta is implicit in the published notation. This is a result about arbitrary initial laws, not only products.

Here is a full reduction from one zero to this published theorem. Write a=log(theta) and choose 1<theta<q/p. Set

lambda=(theta-1)(q/theta-p)>0, B=q/(q-p theta).

For every configuration with a zero, every x and every u>=0,

E_eta[theta^{d_x(eta(u))}] <= exp(-lambda u)theta^{d_x(eta)}+B.       (A1)

To verify this, if d_x=k>=1, its downward jump rate is at least q: a neighbour of a nearest zero at distance k-1 can become zero. Its upward jump rate is at most p. An upward jump has size at most one, since a nearest zero can heal only in the presence of a zero neighbour. If there are two nearest zeros, neither healing alone raises the distance. Thus

L theta^{d_x} <= [q(theta^{-1}-1)+p(theta-1)]theta^{d_x}=-lambda theta^{d_x}

when d_x>=1. At d_x=0, the upper bound is p(theta-1). Consequently on all configurations

L theta^{d_x} <= -lambda theta^{d_x}+q(theta-1)/theta.

Dynkin's formula and the scalar differential inequality give (A1), since [q(theta-1)/theta]/lambda=B. One rigorous way to remove unbounded-function issues is to work on finite intervals with frozen zero exterior, use the same inequality there, pass to the graphical infinite-volume limit, and apply Fatou. For a fixed x the initial distances in these approximations eventually equal d_x(eta). The constant is independent of the approximating interval.

Enclose supp(f) in [h-r,h+r], with integer r>=0. Choose

delta=lambda/[2(lambda+100a)], s=delta t, u=(1-delta)t,

and let I_t=[h-r-ceil(100s), h+r+ceil(100s)]. Run the original process to time u. Form a random configuration zeta by retaining eta(u) inside I_t and setting every site outside I_t to zero. Denote its law by mu_t. This is only an auxiliary initial law for a fresh, ordinary FA-1f process: its exterior zeros are allowed to evolve after time zero.

Suppose eta_z=0 initially. For x in I_t, setting the exterior to zero cannot increase the static distance to a zero, so (A1) gives

mu_t(theta^{d_x}) <= B+exp[a(|h-z|+r+1)+100as-lambda u]
                    = B+exp[a(|h-z|+r+1)-lambda t/2].               (A2)

For x outside I_t, the moment equals 1. Therefore, whenever t>=2a(|h-z|+r+1)/lambda, the global supremum of these moments is at most K=B+1, independent of t and of eta. Apply the published theorem separately to each mu_t, with this same K and theta, for time s. We get

|mu_t P_s f-pi(f)| <= C ||f||_infty exp(-s/C).                     (A3)

Couple the auxiliary process and the true process after time u by the same clocks and coins. They agree initially on I_t. A disagreement can reach supp(f) by time s only if there is a time-ordered nearest-neighbour clock path of at least ceil(100s) steps. The graphical union bound gives

P(disagreement reaches supp(f)) <= |supp(f)| sum_{n>=ceil(100s)} (2s)^n/n!
                                 <= C_f exp(-c_0 s), s>=1.       (A4)

For example n!>=(n/e)^n makes the tail geometric with ratio bounded by 2e/100. This argument depends on locality, not on attractiveness. The Markov property and (A3)–(A4) prove the theorem for deterministic eta, with constants uniform over eta_z=0 and a time threshold linear in |z-h|+r+1. Increasing the prefactor covers the bounded initial time interval. For a general nu, integrate the pointwise convergence and use |P_t f-pi(f)|<=2||f||_infty and bounded convergence. Every configuration in the support has some finite zero location; no measurable choice of z is needed for this last argument. QED.

This is a deduction from an existing theorem, and no novelty claim is made.

## Bilateral spreading for finite initial infections, q>1/2

**Proposition B.** For a nonempty finite initial infection set and q>1/2, its extreme infections L(t),R(t) satisfy, almost surely,

2q-1 <= liminf R(t)/t <= limsup R(t)/t <= q,
-q <= liminf L(t)/t <= limsup L(t)/t <= -(2q-1).

Proof. The number of infected sites remains finite at finite times by the graphical propagation bound. The last zero cannot heal, so L and R are defined. The right front advances one step at rate q, and retreats one step at rate p times 1_{eta_{R-1}=0}. It has no other jumps. Therefore

R(t)-R(0)=M(t)+integral_0^t [q-p 1_{eta_{R(v)-1}(v)=0}]dv,

where M is a martingale with unit jumps and predictable quadratic variation at most t. Doob's L2 inequality on [0,2^{n+1}] and Borel–Cantelli show M(t)/t->0 almost surely: the probabilities of sup|M|>epsilon 2^n are O(2^{-n}). The drift lies between 2q-1 and q. Reflect the lattice to obtain the assertion for L. QED.

These are positive linear lower and upper bounds, not a claim that the limiting front speeds exist for every q>1/2. Combined with Theorem A they answer both spreading and local convergence for a single infection in this parameter range.

## An all-q class controlled directly by the spectral gap

**Proposition C.** Fix q in (0,1). If nu is absolutely continuous with respect to pi, then nu P_t f->pi(f) for every bounded local f. If g=dnu/dpi belongs to L2(pi), the error is at most ||g-1||_2 sqrt(Var_pi(f)) exp(-gap(q)t).

Proof. The positive infinite-volume L2(pi) spectral gap of FA-1f gives ||P_t(f-pi(f))||_2<=exp(-gap(q)t)||f-pi(f)||_2. Pair with g-1 and apply Cauchy–Schwarz. For an arbitrary L1 density g, set g_N=min(g,N), a_N=pi(g_N), h_N=g_N/a_N (for N with a_N>0). Then h_N is an L2 probability density and ||g-h_N||_1<=2(1-a_N)->0. Since |P_t f|<=||f||_infty, first take t->infinity for h_N, then N->infinity. QED.

This includes arbitrary finite modifications of equilibrium (even replacement of finitely many spins by fixed values): outside a fixed finite set the law remains pi, and its Radon–Nikodym derivative is bounded by the reciprocal of the least pi-probability of a pattern on that set. It does not cover a deterministic single infection, or a product law with a different density on infinitely many sites. The imported spectral-gap result is Cancrini–Martinelli–Roberto–Toninelli, PTRF 140 (2008), Theorem 6.4; BCMRT Theorem 6.1 also supplies a positive uniform finite-volume gap on the nonempty component.

## Why a zero is not a fixed boundary

A zero lineage can be followed forever: start at one zero, retain its position until that zero heals, then transfer the label to a neighbouring zero that made its healing legal. Such a label changes position at rate at most p, so it does not explode. Its site is always infected, but its position need not stay close to the observable. Conditioning on its path in FA-1f also reveals information from both sides. This does not yield the East model's conditional product law.

For comparison, in a *modified* FA-1f on a fixed finite interval of n sites with a frozen zero immediately outside an endpoint, the finite chain is irreducible, reversible for pi on that interval, and its gap is bounded below by the corresponding East gap gamma_E(q)>0. Indeed c_FA>=c_E pointwise implies the same inequality for Dirichlet forms; Cauchy–Schwarz and L2 contraction give, for a starting state omega,

|E_omega f(eta(t))-pi(f)| <= pi(omega)^{-1/2} sqrt(Var_pi(f)) exp(-gamma_E(q)t).

Irreducibility follows by moving a facilitating zero across the interval and reversing legal moves. This proves the finite pinned-boundary claim, not convergence in the original infinite process conditional on a zero happening to persist up to time t. Conditioning on persistence generally biases neighbouring clocks and states. A spatially fixed persistent infection is an extra assumption, not a property of the original single seed.

## What the existing proofs need, and what remains missing

The elementary failure of attractiveness can be seen at site 0. Let A have its only zero at 0, and let B have zeros at 0 and 1. In occupation order B<=A and the increasing observable g(eta)=eta_0 has g(A)=g(B)=0. Nevertheless Lg(A)=0 and Lg(B)=p>0, violating the necessary generator inequality for an order-preserving semigroup. More infections can enable healing. Neither freezing extra zeros nor suppressing updates gives the required stochastic comparison.

The assumptions play different roles:

- In BCMRT the usable property is a *uniform exponential moment of distance to an infection*. Product independence implies this, but is not itself needed. Their proof first cuts to a ball of radius proportional to t, partitions it into smaller blocks and restricts the chain to configurations with at least two infections per block. The distance estimate bounds exits from this good set. The restricted log-Sobolev constant scales with block length rather than the whole observation volume. A spectral gap on the full growing box alone is insufficient.
- CMST's all-q perturbative result uses domination of finite-dimensional likelihood ratios by a small exponential in box size, compared against L2 spectral-gap decay. A product law with density sufficiently close to q has that property. A deterministic single seed does not. Their stronger East result instead uses a moving distinguished zero and an exactly conditional product law behind its path. This independence is due to orientation, not merely to the zero's existence. The proof of their Lemma 3.5 and Theorem 3.1 makes that distinction explicit.
- Front proofs for FA-1f compare to a supercritical threshold contact process, produce many infections behind the front and construct repeated coupling attempts. Their renewal/restart structure supplies fresh attempts; it is not a renewal assumption on nu. The auxiliary contact process must survive, which imposes a restriction on q. Stationarity as seen from the front is also not automatically the equilibrium law at fixed lattice sites.
- The source's oriented variants use directional barriers, or East vertices shielding one side. Its branching model uses self-/quasi-duality and a parity-conditioned double-flip chain. Those are properties of different generators. A Dirichlet-form comparison with FA-1f transfers certain equilibrium inequalities, not the out-of-equilibrium local law.

**Single infection versus infinitely many.** For one infection the original zero can heal once it creates a neighbour. A surviving zero lineage may move. The all-q diameter growth theorem does not bound healthy gaps inside the two extreme infections, nor locate the origin relative to the expanding cluster. It therefore cannot be substituted for a local equilibration theorem. For q>1/2, Theorem A and Proposition B supply both missing conclusions (local convergence and bilateral expansion). For 0<q<=1/2, neither conclusion about bilateral fronts/local convergence is established here; the published all-q diameter bounds remain valid.

Infinitely many initial infections remove neither difficulty automatically. For example zeros at plus/minus 2^(2^n), n>=1, leave arbitrarily long healthy intervals and fail the uniform moment condition. A translation-invariant ergodic law with an infection has positive infection density: if nu(eta_0=0)=0, countable subadditivity would exclude every infection, and the ergodic theorem identifies this marginal with the spatial density. But positive density says nothing about exponential gap tails. A stationary renewal process with iid integer gaps P(G=n) proportional to n^(-3) has finite mean, positive density and a size-biased residual gap with polynomial tail. No exponential distance moment exists. This explains why translation invariance alone does not supply the quantitative input of the cited block argument. Theorem A nevertheless covers such laws for q>1/2.

For all q, reducing arbitrary nu to deterministic initial configurations is exact: Dirac laws are among the requested nu, and bounded convergence proves the converse implication. A pathological mixture cannot refute the conjecture if every deterministic nonempty configuration converges. There is no rate uniform over all such initial laws: place the single seed arbitrarily far from supp(f) and use the clock-path bound before its influence can arrive.

The remaining analytic obstruction is explicit in (A1). At q<=1/2, q/theta-p<0 for every theta>1. The drift calculation then provides no decaying distance moment. The actual low-q branching/coalescing dynamics can be better than this one-step worst-case drift, but that requires a new argument. Finite-box spectral gaps remain positive; evaluating at a single initial pattern costs a factor exponential in box length. In a finite-speed observation box of length proportional to t, that cost can overwhelm spectral-gap decay. One cannot conclude from a positive gap by taking the box to infinity after t.

A useful missing input would control the probability of long healthy gaps *inside a growing cone around the initial seed*, uniformly after a long initial period, with estimates sufficient to run the restricted-block relaxation argument at small q. Diameter growth supplies only extreme positions. This report does not prove such a gap estimate, a low-q translation-invariant theorem, or a counterexample.

The related rate conjecture in the source, Conjecture 2 on PDF p. 2, assumes nu([−ell,ell] contains no infection)=O(exp(−kappa ell)). This is an origin-centred tail condition, weaker than a uniform hypothesis over all spatial centres. In particular a fixed seed at the origin satisfies it. It remains a distinct quantitative claim; no coordination with D0027 was performed.

## Literature audit and exact locations

The search date is 13 November 2026. Search strings, source URLs and retrieved text are in `sources/search_records.txt`; direct downloads have a UTC timestamp and SHA-256 in `sources/manifest.jsonl`. “PDF page” below always means the page number in the archived extraction, not an inferred journal page. This matters because preprints and published versions have different pagination and sometimes theorem numbering.

No full resolution was found. In particular the 2026 publication [Martinelli, *Kinetically Constrained Spin Models: A Short Survey*, ICM 2026, volume 5, pp. 497–515](https://doi.org/10.1137/25M180425X), **Conjecture 2.11, printed p. 502, PDF p. 6**, still poses this exact convergence problem. It cites arXiv:2510.20461. This is affirmative evidence that it remained open in that July 2026 publication, not a guarantee that no later paper exists. Exact-arXiv-ID and 2025–2026 topic searches found no later resolving theorem. The publisher's PDF was readable through web text extraction; direct download returned 403. The extracted relevant pages are saved as `Martinelli_ICM_2026_excerpt.txt`.

| Reference | Exact result and checked pages | Relevance / limitation |
|---|---|---|
| Martinelli–Shapira–Toninelli, [arXiv:2510.20461](https://arxiv.org/abs/2510.20461) | Conjectures 1–2, PDF p. 2; Corollary 2.9, p. 7; Theorem 6.2 and proof, pp. 25–27 | Arbitrary nu. Nonempty finite infection sets have diameter and maximal absolute extent bounded above and below linearly, for every q>0. The stationary-measure classification is not a convergence theorem. |
| Blondel–Cancrini–Martinelli–Roberto–Toninelli, *Fredrickson–Andersen one spin facilitated model out of equilibrium*, MPRF 19(3) (2013), 383–406, [arXiv:1205.4584](https://arxiv.org/abs/1205.4584) | Theorem 2.1, PDF pp. 4–5; Remarks 2.3–2.4, p. 5; Proposition 3.1, p. 6; Proposition 4.1 and proof, pp. 10–11; main proof pp. 11–12; Theorem 6.1, p. 13 | q>1/2; exponential relaxation on Z under uniform exponential distance moments. Includes every nontrivial homogeneous Bernoulli product initial law and deterministic configurations with uniformly bounded gaps. Imported in Theorem A. |
| Cancrini–Martinelli–Schonmann–Toninelli, *Facilitated oriented spin models: some non equilibrium results*, JSP 138 (2010), 1109–1123, [arXiv:0810.4237](https://arxiv.org/abs/0810.4237) | Theorem 2.1 and proof, PDF pp. 4–5; East Theorems 3.1–3.2, p. 5, proofs pp. 7–8; distinguished-zero Definition 3.4 and Lemma 3.5, p. 6 | Near-equilibrium initial likelihood ratios give an all-q FA-1f result; the arbitrary-density and deterministic East results use orientation. The zero must be on the facilitating side of the observable. |
| Cancrini–Martinelli–Roberto–Toninelli, *Kinetically constrained spin models*, PTRF 140 (2008), 459–504, [arXiv:math/0610106](https://arxiv.org/abs/math/0610106) | FA-1f Theorem 6.4, PDF p. 20; East Theorem 6.1, p. 18 | Positive spectral gap for all q>0; supports Proposition C and the pinned finite-interval observation. This has Roberto, not Schonmann, among its authors. |
| Mountford–Valle, *Exponential convergence for the Fredrickson–Andersen one-spin facilitated model*, J. Theoret. Probab. 32 (2019), 282–302, [arXiv:1609.01364](https://arxiv.org/abs/1609.01364) | Theorem 1.1, PDF p. 2; Remark 1.2, p. 3; graphical coupling developed from p. 3 | Single seed and origin-centred exponential-distance-tail laws on bounded-degree graphs of suitable subexponential growth, for q sufficiently close to 1. Their facilitating spin is 1, opposite to this report. Does not resolve all q. |
| Mountford, *Exponential convergence for attractive reversible subcritical nearest particle systems*, SPA 59(2) (1995), 235–249, [DOI](https://doi.org/10.1016/0304-4149(95)00048-c) | Exact title, date and pages verified through Crossref primary metadata; full theorem text not obtained | The title in the task is abbreviated. Its attractiveness hypothesis is unavailable for FA-1f, as the generator counterexample above proves. No theorem number is invented or used as an input. |
| Ertul, *Cutoff for the Fredrickson–Andersen one spin facilitated model*, ALEA 19 (2022), 511–536, [published text](https://alea.impa.br/articles/v19/19-20.pdf) | Theorems 2.1–2.2, printed pp. 513–514 (PDF pp. 3–4); Proposition 4.1 and Corollary 4.3, p. 518 (PDF p. 8); Theorems 5.1 and 5.3, p. 519 (PDF p. 9) | Finite intervals with infected boundary, q above a contact-process threshold. The front/cutoff results are not all-q statements. |
| Hong-Quan Tran, [*Cutoff for the non reversible SSEP with reservoirs*, arXiv:2211.14687](https://arxiv.org/abs/2211.14687) | Author and abstract checked on primary arXiv record | This is not by Ertul and is not an FA-1f theorem. Exclusion, reservoirs and negative dependence do not supply the missing constrained-spin coupling. |
| Blondel, *Front progression in the East model*, SPA 123 (2013), 3430–3465, [arXiv:1212.4435](https://arxiv.org/abs/1212.4435) | Theorem 5.1, PDF p. 21; Theorem 6.1, p. 30 | Ergodicity viewed from the front and a front law of large numbers, exploiting East orientation. |
| Blondel–Deshayes–Toninelli, *Front evolution of the Fredrickson–Andersen one spin facilitated model*, EJP 24 (2019), paper 1, 32 pp., [arXiv:1803.08761](https://arxiv.org/abs/1803.08761) | Theorems 2.1–2.2, PDF p. 5; auxiliary threshold described pp. 4–5 | Correct FA-1f front title and coauthors. A front invariant law, LLN and CLT hold for q>bar q=2 lambda_c/(1+2 lambda_c), approximately 0.76 in the stated sufficient condition. This is not a rigorous numerical critical-value claim. |
| Hartarsky–Fabio Lucio Toninelli, *Kinetically constrained models out of equilibrium*, Probab. Math. Phys. 5 (2024), 461–489, [arXiv:2212.08437](https://arxiv.org/abs/2212.08437) | Theorem 3.3, PDF p. 9; background pp. 10–12 | Exponential relaxation for general models with equilibrium facilitating density sufficiently close to 1 and suitable product initial density. Broader models, same high-density restriction. |
| Hartarsky–Cristina Toninelli, *Kinetically Constrained Models*, SpringerBriefs in Mathematical Physics 53 (2025), [author text](https://www.normalesup.org/~hartarsky/files/research/publi/KCM_book.pdf) | Chapter 7; Theorems 7.19–7.21, printed p. 86 (PDF p. 96); distinguished-zero proof printed p. 84 | Modern synthesis and a check of the high-density restrictions. The two Toninelli coauthors in these two references are different people. |
| Marêché, *Exponential convergence to equilibrium in supercritical kinetically constrained models at high temperature*, MPRF 26(5) (2020), 861–884, [arXiv:1907.05844](https://arxiv.org/abs/1907.05844) | Theorem 3, PDF p. 3 | General supercritical families in d=1,2, nontrivial Bernoulli initial law; q sufficiently near 1. Not an all-q result. |
| Marêché, *Combinatorics for general kinetically constrained spin models*, SIAM J. Discrete Math. 34(1) (2020), 370–384, [arXiv:1707.06924](https://arxiv.org/abs/1707.06924) | Theorem 4 and Proposition 6, PDF p. 4 | The energy-barrier theorem excludes supercritical unrooted families; FA-1f is explicitly in that excluded class. Proposition 6 explains bounded-defect mobility there. Legal accessibility is not a probability-of-relaxation estimate. |
| Chleboun–Faggionato–Martinelli, *Mixing time and local exponential ergodicity of the East-like process in Z^d*, Ann. Fac. Sci. Toulouse 24(4) (2015), 717–743, [arXiv:1501.02240](https://arxiv.org/abs/1501.02240) | Proposition 3.1, PDF p. 5, proof p. 6; Theorems 4.3 and 4.6, pp. 10,12; Theorem 5.1, p. 15 | Conditional local stationarity and distinguished-zero trace extend the East method to oriented higher-dimensional models, not to FA-1f. |
| Pillai–Smith, *Mixing times for a constrained Ising process on the torus at low density*, [arXiv:1501.05263](https://arxiv.org/abs/1501.05263); *…on the two-dimensional torus…*, [arXiv:1708.03838](https://arxiv.org/abs/1708.03838) | Second paper Theorem 1, PDF p. 3, and proof roadmap pp. 4–5; first paper primary abstract checked | Finite tori with facilitating density c/number-of-sites, with time-normalization changes between discrete and continuous chains. This joint low-density/large-volume limit is not fixed-q infinite-volume convergence. |
| Shapira, *A note on the spectral gap of the Fredrickson–Andersen one spin facilitated model*, JSP 181 (2020), 2346–2352, [published record](https://doi.org/10.1007/s10955-020-02666-1), [arXiv:2005.13327](https://arxiv.org/abs/2005.13327) | Published Theorems 1.1–1.2; archived preprint p. 2 has Theorems 1.1–1.3 and a longer title including “in stationarity” | Spectral-gap asymptotics and finite-graph bounds. Preprint and published theorem numbering differ. No nonstationary all-q conclusion follows. |

The source's special-case proofs were checked in Sections 3–6, including the one-sided shielding in Section 3, good barriers and restricted log-Sobolev bound in Section 4, and parity/quasi-duality argument in Section 5. Those generators were not substituted for FA-1f. References used as mathematical inputs in Theorems A–C are identified explicitly; papers only checked at metadata/abstract level are identified as such.

## Simulations: finite-time evidence

The code uses exact continuous-time Gillespie sampling of *flip* events. Healthy facilitated sites flip to infected at rate q; infected facilitated sites heal at rate p. A site belongs to one active list regardless of whether it has one or two infected neighbours. Null heat-bath resamplings are omitted, which preserves the generator. Each flip changes only three active-list memberships. Both outside boundary spins are healthy. There is no time discretization.

Each of the eight main experiments used 2,000 independent paths on [-24000,24000]. The two initial laws are:

1. A single zero at 0; every other site healthy.
2. A zero at 0, and independent extra zeros at x!=0 with probability 0.04/(1+|x|/10). This density decays away from the origin. The corresponding infinite-line law has infinitely many zeros almost surely, since the probabilities have divergent sum. The origin is forced only at time 0; it is free to heal thereafter.

The observables are infection at 0, simultaneous infection at 0 and 1, and all three sites [-1,0,1] healthy. Their equilibrium means are q, q² and p³. Each standard error below is the empirical sample standard deviation divided by sqrt(2000), using independent paths. Times along a single path are correlated; no independence across times or exponential-rate fit is asserted.

For the single-seed case, the two current extreme infections R(t),L(t) measure spreading. In the sparse case, global extremes are already far away initially. We instead measure the endpoints of the connected component containing 0 in the set of sites that have *ever* been infected. This can merge with initially infected islands. It is a visited-region statistic, not a current front or a clean estimator of the single-seed front velocity. Both kinds of quantities are saved with explicit column names.

The local infinite-volume approximation is much more accurate than the Monte Carlo error. Couple to the infinite process from the same initial spins inside the interval. A boundary influence on [-1,1] requires a time-ordered clock path of at least 24000 steps. For all runs, T<=4000, and the same union bound as (A4) has logarithm at most -2365. Thus neither the occasional initially infected boundary site in sparse samples nor its later updates compromises the local measurements. For single-seed runs, no path ever infected an endpoint. The finite-volume invariant law is pi conditioned on nonemptiness, rather than pi, but its effect on local marginals is exponentially small in the interval length and is already covered by the coupling comparison to infinite volume.

| q | initial law | T | P(zero at 0)-q (SE) | P(zeros at 0,1)-q² (SE) | P(healthy -1,0,1)-p³ (SE) |
|---|---|---:|---:|---:|---:|
| 0.1 | single seed | 4000 | +0.0020 (0.0068) | -0.0025 (0.0019) | +0.0110 (0.0098) |
| 0.1 | sparse + seed | 4000 | -0.0025 (0.0066) | +0.0045 (0.0027) | +0.0160 (0.0097) |
| 0.3 | single seed | 1200 | +0.0090 (0.0103) | +0.0010 (0.0064) | +0.0030 (0.0106) |
| 0.3 | sparse + seed | 1200 | -0.0210 (0.0100) | -0.0065 (0.0062) | +0.0190 (0.0107) |
| 0.6 | single seed | 600 | +0.0060 (0.0109) | +0.0100 (0.0108) | +0.0040 (0.0056) |
| 0.6 | sparse + seed | 600 | +0.0045 (0.0109) | +0.0020 (0.0107) | +0.0005 (0.0055) |
| 0.85 | single seed | 400 | -0.0030 (0.0081) | -0.0105 (0.0101) | +0.0001 (0.0013) |
| 0.85 | sparse + seed | 400 | -0.0005 (0.0080) | -0.0040 (0.0101) | -0.0004 (0.0012) |

| q | T | E[R(T)] (SE), single seed | E[-L(T)] (SE) | late right slope | E[ever-right], sparse + seed |
|---|---:|---:|---:|---:|---:|
| 0.1 | 4000 | 22.716 (0.465) | 22.499 (0.464) | 0.00562 | 46.062 (0.684) |
| 0.3 | 1200 | 76.575 (0.468) | 76.442 (0.474) | 0.06401 | 129.029 (1.569) |
| 0.6 | 600 | 195.208 (0.491) | 195.212 (0.489) | 0.32539 | 325.632 (3.594) |
| 0.85 | 400 | 285.094 (0.446) | 286.406 (0.437) | 0.71059 | 484.452 (5.460) |

All 24 final local differences are within 2.10 estimated standard errors of zero. For q=0.1, the one-site infection probability starts at 1 and is 0.1020 at t=4000 from a single seed, versus equilibrium 0.1; the pair probability is 0.0075 versus 0.01. The low-q fronts spread much more slowly: the observed late right-front slopes are about 0.0056 at q=0.1 and 0.0640 at q=0.3. At q=0.6 and 0.85, slopes are about 0.325 and 0.711, compatible with Proposition B's lower bounds 0.2 and 0.7 and upper bounds q. These are finite-time slopes of ensemble means, not proved limiting velocities. Reflection symmetry is also consistent with the two measured mean fronts.

The data support local equilibration and bilateral spreading at the tested parameters. They cannot prove convergence as t tends to infinity, exclude rare events, or establish a rate. The graph in [data/fa1f_results.svg](data/fa1f_results.svg) shows the time dependence and pointwise error bars. Full time series are in `data/q*_mode*.csv`; final residuals, equilibrium values and errors are in `data/summary.csv`; seeds, commands, timestamps and event counts are in `data/runs.json`.

### Verification and reproducibility

Before the main runs, the simulator was compared to an independently constructed generator on five sites with healthy boundaries, q=0.3, starting from the central seed. Enumerating all 31 nonempty configurations gives a 31-by-31 matrix. Its row sums vanish to 3.89e-16; detailed balance was checked entry by entry against pi conditioned on nonemptiness, and the stationary residual is 6.94e-18. Exact transient probabilities from matrix exponentiation were independently reproduced by Poisson uniformization, differing by at most 2.23e-16. All six checked observables at six times agreed with 120,000 Monte Carlo paths within 2.21 estimated standard errors. The verification files contain the actual numerical differences, not only a pass flag. The first matrix-exponential call emitted floating-point warnings despite finite output; the independent uniformization check resolved that concern.

The C++ code also asserts active-list consistency, nonextinction and extreme-site consistency. It audits the first path every 1,000 events and every path at termination. All eight main runs finished without an assertion failure. The mathematical constants in Theorem A were checked by substitution; front rates were independently checked against the generator. The comparison source and every load-bearing theorem number/page were reread before this report was finalized.

To reproduce, from this directory:

```sh
clang++ -O2 -std=c++17 code/simulate.cpp -o code/simulate
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 python3 code/verify_simulator.py
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 python3 code/run_experiments.py
python3 code/summarize.py
python3 code/plot_results.py
```

The simulator checks inherited nice>=10 and refuses otherwise. In this session nice was already 10. Run with `nice -n 10` when starting from a normal-priority shell. Experiments are serial, one simulation process and one thread at a time. Working arrays are proportional to the 48,001 sites, not to the total number of events; no trajectories are retained in memory. Numerical Python libraries are limited to one thread. A representative 48,001-site run measured 5,423,104 bytes of peak resident memory (about 5.17 MiB), recorded by getrusage in `data/resource_probe_stdout.txt`. No publication, external writes, git commits or pushes were performed. Source downloads were converted in memory and retained as plain text; no PDF, scan or source-page image was saved anywhere in this directory.

The unresolved part of D0026 is convergence from arbitrary nonempty configurations at small q, including the deterministic single-infection law. Theorem A settles the requested high-q alternative, and Proposition C identifies a separate all-q class. Neither is a resolution of Conjecture 1.

Task: “Open problem D0026.” — 13 November 2026, 07:28 Asia/Tbilisi.
