RESOLVED_IN_LITERATURE

# I0006: lower tails and the finite-time divisible sandpile

The cited companion paper already answers the question for a broad natural class. Under the source's moment assumptions, if

\[
c_1t^\gamma\le -\log\mathbb P(\eta(0)<-t)\le C_1t^\gamma
\quad(t\ge t_0),\qquad 1\le\gamma<\infty,\quad\gamma\ne d/2,
\]

then, for fixed integer \(d\ge5\),

\[
\boxed{\mathbb Eu_n(0)\asymp(\log n)^{1/\min\{\gamma,d/2\}}.}
\]

This is Bou-Rabee–Panagiotis, *Quantitative explosion and percolation of the divisible sandpile*, arXiv:2609.02829v1, Theorem 1.3(iii)(b), p. 6. The proof is Proposition 6.3, p. 53, and Theorem 6.6, pp. 55–56. Constants depend on the fixed law, dimension, and tail comparison constants; they do not depend on n. Here and below \(\asymp\) means two-sided bounds by positive constants, not convergence of a ratio to one.

The classification refers to this literature resolution, not a solution for every possible tail. The companion explicitly excludes \(\gamma=d/2\) (p. 10). Polynomial tails and \(0<\gamma<1\) violate the two-sided exponential-moment assumption in the question's quoted theorem. These distinctions must not be suppressed.

## Source and exact model

The arXiv listing identifies the source as Ahmed Bou-Rabee and Christoforos Panagiotis, *Sharpness and critical scaling of parking*, arXiv:2609.02820v1, submitted **Wed, 2 Sep 2026 17:08:08 UTC**. The listing has only v1; it describes 43 pages and 2 figures. The companion is by the same authors, arXiv:2609.02829v1, submitted **Wed, 2 Sep 2026 17:14:34 UTC**, 82 pages and 3 figures. Thus the relevant resolution is a same-day companion, already cited by the source, rather than an unidentified later development.

Sources: https://arxiv.org/abs/2609.02820 and https://arxiv.org/abs/2609.02829 . Local plain texts: sources/2609.02820v1.txt and sources/2609.02829v1.txt. Page references are the printed PDF page numbers, matching the form-feed-separated text pages.

The lowercase \(u_n\) is the **synchronous divisible sandpile odometer on all of \(\mathbb Z^d\)**. It records the total mass emitted from a site during the first n parallel rounds. Initially site x has signed mass \(\eta(x)\); in each round a positive site distributes its entire positive mass equally among its 2d nearest neighbors. Negative sites absorb arriving mass. Equivalently, write physical mass \(\sigma(x)=1+\eta(x)\) and retain mass one at an unstable site. Signed physical masses are allowed when eta is unbounded below.

With \(Pf(x)=(2d)^{-1}\sum_{y\sim x}f(y)\),

\[
u_0(x)=0,\qquad u_{n+1}(x)=(\eta(x)+Pu_n(x))_+.
\]

Here **n is time**, not a box side length. There is no finite box, torus, sink, or imposed boundary condition. At finite time the recursion depends on only a finite neighborhood. A finite cube appears in the proof as a rare-event construction, not as the domain of the process.

Source Theorem 3.4, p. 14, assumes real-valued i.i.d. eta, \(\mathbb E\eta(0)=0\), \(0<\operatorname{Var}\eta(0)<\infty\), and \(\mathbb Ee^{\theta|\eta(0)|}<\infty\) for some \(\theta>0\). Mean zero is criticality, equivalent to mean physical mass one. Integer values are not required for this divisible sandpile theorem. The uppercase \(U_n\) counts particle departures in the parking/particle–hole process; it is a different odometer. For example, critical parking has eta equal to ±1 with equal probabilities; the particle–hole model has eta equal to particle count minus one and hence eta ≥ −1. Neither identification changes which lowercase odometer is in the question.

In the companion use \(\zeta=\eta/(2d)\), \(\sigma=1+2d\zeta\), and let v denote its odometer, which records emission **per neighbor**. Then

\[
v_{n+1}=(\zeta+Pv_n)_+,\qquad u_n=2dv_n.
\]

Thus this normalization changes constants only. The source explicitly explains it on p. 13 and before Theorem 3.4 on p. 14.

## Where the stated results are proved

Source Theorem 3.4 (p. 14) **quotes**, rather than proves, the estimates. Its citation names the companion's Theorem 1.3, Corollary 6.2, Theorem 6.6, and equation (94).

| Claim for d ≥ 5 | Exact primary location, arXiv:2609.02829v1 |
|---|---|
| \(\mathbb Ev_n\ge c(\log n)^{2/d}\), with concentration | Theorem 6.1, pp. 51–52; bound (88), proof via (90) |
| Universal lower bound for every nondegenerate integrable mean-zero i.i.d. law | Corollary 6.2(i), pp. 52–53 |
| \(\mathbb Ev_n\le C\log(n+2)\) under the exponential moment | Equation (94), p. 55, inside the proof of Theorem 6.6; its proof does not use the additional refined-tail hypothesis |
| Bounded-below sharp order \((\log n)^{2/d}\) | Theorem 6.6 plus (88), explicitly stated immediately after its proof, p. 56 |
| Two-sided Weibull-type answer above | Theorem 1.3(iii)(b), p. 6; Proposition 6.3, p. 53; Lemmas 6.4–6.5, pp. 53–54; Theorem 6.6, pp. 55–56 |

The finite-time optimal-stopping representation is source Lemma 3.1, p. 13. Its cited primary result is Bou-Rabee, Peres, and Sava-Huss, *Divisible sandpiles via random walks in random scenery*, arXiv:2604.13968v1, Theorem 3.2. In the companion it is Theorem 2.2. A page-precise background bibliography and the proof audit follow below.

## Proof audit of the literature result

For clarity this section uses the companion's normalization v and zeta. Let \(m_n=\mathbb Ev_n(0)\), \(g_k(x,y)=\sum_{j<k}P^j(x,y)\), and \(G=\sum_{j\ge0}P^j\). All constants below are positive finite constants for the fixed dimension and law; c and C may change between inequalities. These are the estimates in the printed proof, with the integrations and dimension-dependent exponents checked independently.

**1. Reflection creates the mean.** Stationarity, mean zero, and \(r_+=r+(-r)_+\) give exactly

\[
m_{n+1}-m_n=\mathbb E(-\zeta(0)-Pv_n(0))_+.
\tag{A}
\]

This is companion (86), p. 51. The odometer is increasing in time and in every scenery coordinate. The walk representation gives coordinate Lipschitz constants at most \(g_n(0,y)\le G(0,y)\). Since \(G(0,y)\le C(1+|y|)^{2-d}\) and \(\sum_yG(0,y)^2<\infty\) for d > 4, the product-law concentration lemma (Lemma 3.2) gives uniformly in n

\[
\mathbb P(|v_n(x)-m_n|\ge s)\le C\exp[-c\min\{s^2,s\}].
\tag{B}
\]

Theorem 6.1, p. 51, proves this before the lower-bound argument.

**2. The fixed negative region explains 2/d.** Choose \(a,q>0\) with \(\mathbb P(\zeta\le-a)\ge q\). Take an integer \(R\asymp\sqrt{m_n+1}\), large enough that \(aR^2/2\ge2m_n+1\), and require

\[
E=\{\zeta\le-a\text{ on }Q_R\}\cap
\{v_n\le2m_n+1\text{ on }\partial Q_R\}.
\]

Here \(Q_R=[-R,R]^d\cap\mathbb Z^d\); the boundary is the nearest-neighbor exterior boundary. Markov's inequality gives probability at least 1/2 for each boundary constraint. All events are decreasing functions of independent scenery, so positive association gives

\[
\mathbb P(E)\ge q^{|Q_R|}2^{-|\partial Q_R|}
\ge \exp[-C(m_n+1)^{d/2}].
\]

For \(b(x)=a|x|^2/2\), \(Pb=b+a/2\). On E, boundary monotonicity in time and induction in the recursion imply \(v_s(x)\le b(x)\) throughout the cube for every \(s\le n\): indeed \(\zeta+Pb\le b-a/2\), and \((b-a/2)_+\le b\). Thus \(Pv_n(0)\le a/2\), while \(\zeta(0)\le-a\). Equation (A) yields

\[
m_{n+1}-m_n\ge (a/2)\mathbb P(E)
\ge c\exp[-C(m_n+1)^{d/2}].
\tag{C}
\]

This is (90), p. 52. To check the inversion, let
\(F(s)=c^{-1}\int_0^s\exp[C(r+1)^{d/2}]\,dr\).
Its increasing derivative and (C) imply \(F(m_{n+1})-F(m_n)\ge1\). Consequently \(n\le F(m_n)\le C'\exp[C'(m_n+1)^{d/2}]\), after absorbing the polynomial prefactor, and \(m_n\ge c'(\log n)^{2/d}\) for all large n.

The argument is a rare negative-region/barrier argument. The cost is exponential in \(R^d\), whereas the quadratic potential scale is \(R^2\). It is not the maximum of the original eta over an n^d box. For bounded-below eta, a single negative eta cannot become arbitrarily deep at all. The proof does not require counting independent candidate holes in a specified observation box.

**3. A deeper one-site deficit can be cheaper.** By (B) and a union bound over the 2d neighbors, there is a fixed b such that

\[
\mathbb P\bigl(v_n(e)\le2m_n+b\text{ for every }e\sim0\bigr)\ge1/2.
\]

Intersect this event with \(\{\zeta(0)\le-2m_n-b-1\}\). The two events need not be independent; they are decreasing, so positive association still applies. On the intersection the deficit in (A) is at least one. Hence

\[
m_{n+1}-m_n\ge\tfrac12\mathbb P(\zeta(0)\le-2m_n-b-1).
\]

Under \(\mathbb P(\zeta<-s)\ge a_0e^{-A_0s^\gamma}\), combine this with (C), and set \(\beta=\min\{\gamma,d/2\}\). For sufficiently large \(m_n\),

\[
m_{n+1}-m_n\ge c e^{-C(m_n+1)^\beta}.
\]

The preceding integral argument proves \(m_n\ge c(\log n)^{1/\beta}\). This is Proposition 6.3, p. 53. It alone is not a matching upper bound.

**4. Green averages give the upper bound.** Lemma 6.4, pp. 53–54, proves uniformly in k

\[
\mathbb P\left(\sum_y g_k(0,y)\zeta(y)\le-s\right)
\le C e^{-cs^\beta}.
\tag{D}
\]

For \(\gamma=1\), choose a fixed small Laplace parameter and use square summability of G. For \(\gamma>1\), put \(q_*=\gamma/(\gamma-1)\). The one-site log Laplace transform is bounded by \(C\mu^2\) for \(0\le\mu\le1\) and by \(C\mu^{q_*}\) for \(\mu\ge1\). When \(\gamma<d/2\), \(q_*>d/(d-2)\), so \(\sum_yG(0,y)^{q_*}<\infty\). Splitting where \(\lambda g_k\) crosses one gives total log Laplace transform at most \(C\lambda^{q_*}\). The small-coefficient contribution has order at most \(\lambda^{d/(d-2)}\le\lambda^{q_*}\).

When \(\gamma>d/2\), split at radius \(L\asymp\lambda^{1/(d-2)}\). The inner sum is at most

\[
C\lambda^{q_*}L^{d-(d-2)q_*}=C\lambda^{d/(d-2)},
\]

and the outer sum is at most \(C\lambda^2L^{4-d}=C\lambda^{d/(d-2)}\). Thus in both regimes the log Laplace transform is at most \(C\lambda^{\beta/(\beta-1)}\). In the Chernoff bound, choose \(\lambda=b s^{\beta-1}\) with b small enough that \(Cb^{1/(\beta-1)}\le1/2\). This gives (D), adjusting constants for bounded s.

At \(\gamma=d/2\), the inner sum is at its logarithmic summability threshold. The argument just given does not remove that logarithm. Neither the theorem nor this report extends its matching-order conclusion to that case.

For the remaining nonlinear contribution, Lemma 6.5, p. 54, gives

\[
\mathbb P\{P^k(v_j-m_j)(0)\le-s\}
\le C\exp[-c\min\{s^2k^{(d-4)/2},sk^{(d-2)/2}\}].
\tag{E}
\]

Its Lipschitz kernel is bounded by \(\sum_{r\ge k}P^r\); the squared norm and supremum of this kernel give the two exponents. The crude version of (B) applied to \(\zeta(0)+Pv_n(0)-m_n\), followed by integrating its tail in (A), first gives
\(m_{n+1}-m_n\le Ce^{-cm_n}\).
A hitting-level argument then gives \(m_n\le C\log(n+2)\), which is (94), p. 55. Explicitly, on passage from R to 2R the increments are at most \(Ce^{-cR}\), and overshoots are at most \(K=\mathbb E(-\zeta)_+\); for R ≥ 2K this passage takes at least \(cR e^{cR}\) steps.

For the refined estimate fix \(m_n\le h\le\sqrt n\), choose \(k=\lfloor\epsilon h\rfloor\), and take \(\epsilon K\le1/8\). The bound \(m_{j+1}-m_j\le K\) gives \(m_n-m_{n-k}\le h/8\). Iterating \(v_{j+1}\ge\zeta+Pv_j\) gives

\[
\zeta(0)+Pv_n(0)-m_n\ge
\sum_{r=0}^{k}P^r\zeta(0)
+P^{k+1}(v_{n-k}-m_{n-k})(0)-h/8.
\]

If the left side is at most −h, one of the first two terms must be at most \(-7h/16\). Bound the first by (D). In (E), k is of order h, so both exponents have order \(h^{d/2}\); the second probability is at most \(Ce^{-ch^{d/2}}\). For h > √n use the crude exponential bound: its integrated contribution is at most \(Ce^{-c\sqrt n}\), negligible compared with \(e^{-cm_n^\beta}\) because \(m_n=O(\log n)\). Integration in (A), absorbing the integral's polynomial factor into c, yields

\[
m_{n+1}-m_n\le Ce^{-cm_n^\beta}.
\tag{F}
\]

Let \(\tau_R=\inf\{j:m_j\ge R\}\). The overshoot bound is \(m_{\tau_R}\le R+K\). For R ≥ 2K, passage to 2R requires an increase of at least R/2, at increments at most \(Ce^{-cR^\beta}\). Therefore \(\tau_{2R}-\tau_R\ge cR e^{cR^\beta}\). Taking \(R=m_n/2\) proves \(m_n\le C(\log n)^{1/\beta}\). This checks the last step of Theorem 6.6, p. 56.

If zeta is bounded below, its lower tail satisfies the upper-tail hypothesis for any finite \(\gamma>d/2\). Theorem 6.6 and the universal lower bound therefore give \(m_n\asymp(\log n)^{2/d}\).

Taken together, these arguments identify an inverse rare-deficit cost, rather than a sum of independent local deficits: for the stated class, the cost exponent at mean level m is \(\min\{m^\gamma,m^{d/2}\}\). Green-weighted collective fluctuations are essential to the upper bound. Even in the \(\gamma<d/2\) regime, the proof does not identify a single site as the actual optimal stopping target in every realization.

## Examples and scope

Under the original exponential-moment assumptions, the theorem gives:

| Lower tail, for all sufficiently large t | Order of \(\mathbb Eu_n(0)\) |
|---|---|
| \(-\log\mathbb P(\eta<-t)\asymp t\) | \(\log n\) |
| \(-\log\mathbb P(\eta<-t)\asymp t^\gamma\), \(1<\gamma<d/2\) | \((\log n)^{1/\gamma}\) |
| Gaussian lower tail, \(\gamma=2\) | \(\sqrt{\log n}\), for every d ≥ 5 |
| \(-\log\mathbb P(\eta<-t)\asymp t^\gamma\), \(\gamma>d/2\) | \((\log n)^{2/d}\) |
| eta bounded below | \((\log n)^{2/d}\) |

For example, in d = 5, the powers of log n are 1 for exponential lower tails, 1/2 for Gaussian lower tails, and 2/5 for bounded-below laws or Weibull lower tails with exponent greater than 5/2.

The strict inequality in the question and the non-strict inequality in the source do not change any displayed order: for t > 0,
\(\mathbb P(\eta<-2t)\le\mathbb P(\eta\le-2t)\le\mathbb P(\eta<-t)\le\mathbb P(\eta\le-t)\).
Applying the assumed comparisons at t and 2t transfers them in either direction, including for atomic laws.

The borderline \(\gamma=d/2\) remains outside the quoted resolution. For such a tail, the printed results do at least give a lower bound \(c(\log n)^{2/d}\) and, for every fixed \(\epsilon\in(0,d/2-1)\), an upper bound \(C_\epsilon(\log n)^{1/(d/2-\epsilon)}\), by applying Theorem 6.6 with exponent d/2 − epsilon. This does not establish a sharp order. No claim about the absence or presence of a log-log correction is made.

**An additional literature consequence for polynomial lower tails.** This requires changing the moment assumptions. Under companion Theorem 6.7(b), p. 56, the law is atomless, bounded above, mean zero, has positive finite variance, and has regularly varying lower tail with index \(-\alpha\), \(\alpha>2\). In particular, a polynomial lower tail does not satisfy the source's exponential moment.

Write \(g=G(0,0)=\sum_{j\ge0}\mathbb P_0(X_j=0)\) for the *unnormalized* simple-random-walk Green function. The proof of Proposition 6.11(b), pp. 64–66, states explicitly on p. 64, immediately after (129),

\[
\mathbb P(-g\zeta(0)>m_n)\sim\frac{g(1-1/\alpha)}{n}.
\tag{G}
\]

It also establishes (129), the increment equivalent

\[
m_{n+1}-m_n\sim\mathbb E(-\zeta(0)-m_n/g)_+.
\]

The mechanism is the odometer with a walk killed at the origin, whose incoming mass is independent of the origin's scenery. Equations (128)–(132) replace that random incoming threshold by m_n/g. Karamata's integrated-tail estimate, (127), p. 64, then gives (G). This is a statement from the published preprint's proof, not an assertion inferred only from its scaling-limit theorem.

Translating (G) back to the source's total-emission odometer, let \(M_n=\mathbb Eu_n(0)=2dm_n\). Then

\[
 n\mathbb P\bigl(\eta(0)<-M_n/g\bigr)\longrightarrow g(1-1/\alpha).
\]

Thus the mean is the lower-tail quantile at probability of order 1/n. If, specifically, \(\mathbb P(\eta(0)<-t)\sim c_0t^{-\alpha}\), then elementary inversion gives

\[
\mathbb Eu_n(0)\sim
\left(\frac{\alpha c_0g^{\alpha-1}}{\alpha-1}\,n\right)^{1/\alpha}.
\]

For regularly varying tails with a slowly varying factor, the quantile formulation is the appropriate statement; replacing it by a pure power can lose that factor. These conclusions retain the companion's atomlessness and upper-bound hypotheses. They are not asserted for every finite-variance heavy-tailed field. No fresh attack on the cases not covered by these printed results was undertaken, following the requested literature stopping rule.

## Relevant primary literature and model distinctions

The following references were checked against the primary texts saved in sources/. Page numbers in this table refer to the indicated arXiv text, not to the journal's pagination. Only the two Bou-Rabee–Panagiotis papers above prove the finite-time high-dimensional estimates in question.

| Primary paper and local text | Exact result and relevance |
|---|---|
| Levine–Peres, *Strong Spherical Asymptotics for Rotor-Router Aggregation and the Divisible Sandpile*, Potential Analysis 30 (2009), 1–27; [arXiv:0704.0688v5](https://arxiv.org/abs/0704.0688v5), sources/0704.0688.txt | Theorem 3.3, p. 12: single-source divisible-sandpile occupied set differs from a Euclidean ball by bounded radial error. Foundational model and obstacle/Green-potential methods; not an i.i.d. critical finite-time rate theorem. |
| Levine–Murugan–Peres–Ugurcan, *The divisible sandpile at critical density*, Ann. Henri Poincaré 17 (2016), 1677–1711; [arXiv:1501.07258v2](https://arxiv.org/abs/1501.07258v2), sources/1501.07258v2.txt | Theorem 1.1, p. 2: nonstabilization at mean one and positive finite variance on infinite vertex-transitive graphs. Theorem 1.2 and Proposition 1.3, p. 4: fully stabilized **torus**, recentered Gaussian masses, odometer equal in law to a membrane field minus its minimum; order \(\sqrt{\log n}\) for d ≥ 5. Lemma 7.1, pp. 21–22, gives the finite-graph Poisson equation/minimum-zero characterization. These are different from the time-n infinite-volume model. |
| Bou-Rabee–Peres–Sava-Huss, *Divisible sandpiles via random walks in random scenery* (2026); [arXiv:2604.13968v1](https://arxiv.org/abs/2604.13968v1), sources/2604.13968v1.txt | Theorem 3.2, p. 11: finite-time optimal-stopping representation, proved by dynamic programming; this is what source Lemma 3.1 uses. Companion Theorem 2.2 restates it on p. 15. |
| Cipriani–Hazra–Ruszel, *Scaling limit of the odometer in divisible sandpiles*, Probab. Theory Related Fields 172 (2018), 829–868; [arXiv:1604.03754v4](https://arxiv.org/abs/1604.03754v4), sources/1604.03754.txt | Theorem 1, p. 3, and Theorem 2, p. 4: Gaussian and general finite-variance weights on a recentered discrete **torus**, convergence to the continuum bilaplacian field against zero-mean tests. This does not identify the diverging additive mean in the question. |
| Cipriani–Hazra–Ruszel, *The divisible sandpile with heavy-tailed variables*, Stochastic Processes and their Applications 128 (2018), 3054–3081; [arXiv:1610.09863v1](https://arxiv.org/abs/1610.09863v1), sources/1610.09863.txt | Theorems 2–3, pp. 4–5: critical heavy-tail nonstabilization under their symmetry/transience assumptions. Theorem 5, p. 6: stable odometer-field limit on the torus. Different observables and assumptions; not a polynomial-tail finite-time mean theorem. |
| Alberto Chiarini–Cipriani–Hazra, *Extremes of some Gaussian random interfaces*, J. Stat. Phys. 165 (2016), 521–544; [arXiv:1509.08903v2](https://arxiv.org/abs/1509.08903v2), sources/1509.08903.txt | Theorem 1, pp. 2–3: criterion for Gumbel extrema; Section 4.1 applies it to the high-dimensional membrane model. Gaussian extreme-value background, not the universal \((\log n)^{2/d}\) mechanism for bounded-below scenery. |
| Damron–Gravner–Junge–Lyu–Sivakoff, *Parking on transitive unimodular graphs*, Ann. Appl. Probab. 29 (2019), 2089–2113; [arXiv:1710.10529v3](https://arxiv.org/abs/1710.10529v3), sources/1710.10529.txt | Theorem 1.1, p. 2, and Theorem 2.1, p. 6: parking recurrence/transience and small-density finite expectation. Open Question 1, p. 8, asks about critical **particle** visit growth; Questions 2–3, p. 9, concern subcritical expectation and nearest particle/hole. These concern uppercase U, not lowercase u. |
| Bahl–Barnet–Johnson–Junge, *Diffusion-limited annihilating systems and the increasing convex order*, Electron. J. Probab. 27 (2022), no. 84, 1–19; [arXiv:2104.12797v2](https://arxiv.org/abs/2104.12797v2), sources/2104.12797.txt | Theorem 1.3, p. 5: increasing convex order comparison for particle occupation times. Related parking comparison literature, not the divisible-sandpile mean rate. The source also cites Bahl–Barnet–Junge, *Parking on supercritical Galton–Watson trees* (2021), and Johnson–Junge–Lyu–Sivakoff, *Particle density in diffusion-limited annihilating systems* (2023); neither is the primary reference for Theorem 3.4. |

The 2026 search checked both current arXiv listings, the earlier random-scenery paper, and searches for the exact source/companion titles and for divisible-sandpile lower-tail mean rates. Both September listings showed only v1 on 13 November 2026. No later paper replacing these results was located. The decisive paper is already the explicitly cited companion, so no claim of an exhaustive absence theorem about subsequent literature is needed.

## Checks, reproducibility, and stopping point

- Both September arXiv listings were saved as plain text, including their exact version histories. The main and companion PDF responses were held in memory and piped to pdftotext; no PDFs or page images were saved.
- Read the complete high-dimensional mean-growth proof, companion pp. 51–56, including the negative-region construction, positive association, Green-average Laplace bounds, smoothing estimate, and hitting-level inversion. The independent algebra above checks the radius/volume exponent, the summability transition, the two smoothed exponents, the direction of each inversion, and the 2d normalization.
- Read the regularly varying-tail mean calculation in Proposition 6.11(b), pp. 64–66. The polynomial-tail constant was re-derived both from (G) and from (129): if \(F(t)\sim c_0t^{-\alpha}\), the total-emission increment is asymptotic to \(c_0g^{\alpha-1}M_n^{1-\alpha}/(\alpha-1)\); integrating it gives the same \(M_n^\alpha\sim\alpha c_0g^{\alpha-1}n/(\alpha-1)\).
- Ran `python3 code/check_normalization.py`. For three deterministic one-dimensional rational scenery fields and five rounds each, direct parallel signed-mass redistribution agrees exactly with the cumulative odometer recursion and with twice the per-neighbor odometer. Results are in data/normalization-check.json. This checks conventions only; it supplies no evidence for a high-dimensional asymptotic.
- Ran `python3 code/audit_artifacts.py`: 33 cited-page checks passed; 12 plain-text source files were checked, and no PDF or page-image files were present. data/source-manifest.json records the source text hashes, versions where printed in the text, page counts, and reproducible PDF URLs. The source texts are the retained artifacts; fetching them anew may depend on network availability.
- No stochastic simulations, five-dimensional box solves, numerical proof claims, publication, commits, pushes, or subagents were used. The exact check uses only small standard-library objects. The existing launcher runs this agent at nice 10; process inspection and further priority changes were sandbox-denied. There was no worker pool.

The requested literature stopping rule applies: the cited companion already proves the sharp order for the stated Weibull-type class and supplies the regularly varying-tail calculation under its separate assumptions. The borderline Weibull case and unrestricted irregular lower tails are not solved by this report.

Task: “Open problem I0006” — work began 13 November 2026, 14:57 +04 (Asia/Tbilisi); exact prompt receipt time was not provided.
