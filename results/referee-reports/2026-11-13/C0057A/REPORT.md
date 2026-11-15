PARTIAL

# C0057: exhaustion of critical Boltzmann maps

The general assertion is neither proved nor disproved here. The partial result is a sufficient random-walk criterion with a proof that does not assume regular variation:

> For every starting half-perimeter, if the conditioned perimeter walk satisfies
> \[
> \sum_{n\geq0}P_n\nu(-P_n)=\infty\quad\text{almost surely},\tag{R}
> \]
> then every continuing, adapted, filled-in peeling algorithm exhausts the infinite Boltzmann map.

The comparison between this series and a boundary-swallowing hazard holds for **every** critical bipartite weight sequence. Establishing (R) from criticality alone remains the gap. An explicit critical family with non-regularly-varying tails is constructed below. No member of that family is shown to be a counterexample.

## Source, scope, and literature finding

The text matching the question's numbering is [Curien's Peccot preprint](https://www.imo.universite-paris-saclay.fr/~nicolas.curien/cours/peccot.pdf), saved in `sources/curien_peccot.txt`. Corollary 27, its entire proof, and the question are on **PDF page 61, printed page 57**. The exact question is:

> Is the last corollary true for any critical weight sequence?

The current teaching page links the Saint-Flour text through Dropbox. That link returned HTML, and its direct-content URL returned 404. Thus the saved lecture text is the accessible older preprint with exactly the specified corollary, not a verified copy of the Saint-Flour/book version. The 2023 book has different theorem numbering. This is a limitation of the source retrieval, not evidence that the question changed.

No general resolution was found in the literature searched through 13 November 2026. The strongest explicit status statement located is Cyril Marzouk's *A few aspects of large random maps*, HDR, 1 December 2022, printed/PDF p. 66, “More general models”: it states that eventual discovery by every peeling algorithm is unknown for all critical maps. See [the author's text](https://cmarzouk.perso.math.cnrs.fr/Articles/HDR_Marzouk.pdf). This is a dated statement; the search does not certify the absence of all later work.

The following are the specific results checked. PDF-page references refer to the exact saved extraction; journal pages are given where checked against the published text.

| Reference | Exact result and location checked | Bearing on C0057 |
|---|---|---|
| T. Budd, *The peeling process of infinite Boltzmann planar maps*, Electronic J. Combin. **23** (2016), P1.28; [arXiv:1506.01590](https://arxiv.org/abs/1506.01590) | Theorem 2, saved preprint p. 13; Proposition 4, p. 11; Lemma 4, pp. 16–17; Proposition 5, p. 18 | General critical perimeter law and oscillation; the scaling result requires the extra moment \(L_\nu<\infty\). A perimeter description is not itself arbitrary-algorithm exhaustion. |
| T. Budd and N. Curien, *Geometry of infinite planar maps with high degrees*, Electron. J. Probab. **22** (2017), paper 35, [DOI](https://doi.org/10.1214/17-EJP55) | Proposition A, p. 7; Proposition 3.2, p. 16 | Criticality/harmonicity correspondence; stable scaling under power-tail hypotheses. |
| T. Budd, N. Curien and C. Marzouk, *Infinite random planar maps related to Cauchy processes*, J. Éc. polytech. Math. **5** (2018), 749–791, [DOI](https://doi.org/10.5802/jep.82) | Theorem 1, saved preprint p. 9; assumption (1), p. 2 | Treats the type-2/Cauchy regime beyond the older notes' one explicit example, but still imposes tail asymptotics. |
| N. Curien and C. Marzouk, *How fast planar maps get swallowed by a peeling process*, Electron. Commun. Probab. **23** (2018), paper 18, [DOI](https://doi.org/10.1214/18-ECP123) | Theorem 1.1, p. 2 of the saved preprint | Quantitative swallowing for bounded face degrees; not the general case. |
| N. Curien and C. Marzouk, *Markovian explorations of random planar maps are roundish*, Bull. Soc. Math. France **148** (2020), 709–732, [published text](https://cmarzouk.perso.math.cnrs.fr/Articles/Roundish.pdf) | Definition of types on p. 710; Theorem 1.1, p. 711 (PDF pp. 4–5) | Proves more than exhaustion under its stable hypotheses. Its \(a=5/2\) case includes finite-variance offspring laws, without exponential regularity. The published definition corrects a parameter typo in the early arXiv version. |
| T. Budd and N. Curien, *Simple peeling of planar maps with application to site percolation*, Canadian J. Math. **74** (2022), 907–941, [DOI](https://doi.org/10.4153/S0008414X21000146) | Theorem 1, saved preprint p. 4; Proposition 14, p. 20 | General critical half-plane maps with simple boundaries. Proposition 14 constructs a map with a particular metric algorithm; it does not prove plane exhaustion for every lazy algorithm. |
| N. Curien and L. Richier, *Duality of random planar maps via percolation*, Ann. Inst. Fourier **70** (2020), 2425–2471, [DOI](https://doi.org/10.5802/aif.3369) | Propositions 2.4–2.5, journal pp. 2438–2439 | Separates criticality from stable attraction, including slowly varying corrections. Not a general exhaustion theorem. |
| T. Budzinski, *Local limits of random bipartite maps in high genus: the general case*, 17 June 2024, [author's preprint](https://perso.ens-lyon.fr/thomas.budzinski/papers/bipartite_general.pdf) | Theorems 1–2, p. 2 | Removes face-tail restrictions for a local-limit problem. Those statements do not assert exhaustion by arbitrary peeling. |
| E. Kammerer, *Gaskets of O(2) loop-decorated random planar maps*, [arXiv:2411.05541v2](https://arxiv.org/abs/2411.05541v2), revised 7 December 2025 | Theorems 1.1–1.2, p. 4 | Gives slowly varying type-2 asymptotics under additional loop-model/comparison hypotheses, not all critical laws. |
| E. Kammerer, *Scaling limit of first passage percolation geodesics on planar maps*, [arXiv:2412.02666v3](https://arxiv.org/abs/2412.02666v3), revised 12 September 2025 | Type assumptions, pp. 2–3; Theorem 1.1, p. 6 | Still works with type assumptions. |
| J. Ambjørn, T. Budd and Y. Makeenko, *Generalized multicritical one-matrix models*, Nuclear Phys. B **913** (2016), 357–380, [DOI](https://doi.org/10.1016/j.nuclphysb.2016.09.013) | Sections 2–3, saved preprint pp. 3–9 | Provides heavy-tail matrix-model families, not a theorem about all adapted filled-in explorations. |

Searches also covered the Budzinski–Curien–Petri work on random surfaces in unconstrained genus and the current Curien, Budzinski and Budd publication listings. These concern different limit/geometry questions or supplied no later exhaustion theorem. Their listings were saved as text where available. Broad searches containing “exhaust” returned substantial unrelated material; negative search results were not treated as mathematical evidence. The literature evidence above is based on reading the cited statements.

## Definitions that affect the question

These are bipartite maps: a face of degree \(2k\) has weight \(q_k\); the external/root face has prescribed degree \(2\ell\) and is not included in that product. Put

\[
f_q(x)=\sum_{k\geq1}\binom{2k-1}{k-1}q_kx^{k-1}.
\]

Admissibility means that \(f_q(x)=1-1/x\) has a positive solution; \(Z\) is the smallest solution and \(c=4Z\). Criticality means \(Z^2 f'_q(Z)=1\); subcriticality means strict inequality. Regularity means \(f_q(Z+\epsilon)<\infty\) for some \(\epsilon>0\), hence an exponential positive tail for the perimeter increment law. Generic finite-variance criticality can be broader than regular criticality.

The older notes use “type \(5/2\)” for regular critical sequences, “type \(3/2\)” for regular **subcritical** sequences, and power asymptotics for the intermediate types. Their type \(2\) is one particular explicit sequence. Consequently the corollary's displayed interval \([3/2,5/2]\) must be read together with the definition of \(\mathbb P_\infty^{(\ell)}\), which in these notes requires criticality: the subcritical endpoint does not define another instance of the plane assertion. The text explicitly says the positive conditioned process is not defined in that subcritical case. Later articles use broader stable-type definitions.

The infinite map of the plane is a locally finite, one-ended local limit of critical Boltzmann maps conditioned to have many vertices (Curien, Theorem 8, printed p. 44). A filled-in exploration keeps the unique infinite component unexplored and immediately fills each finite component cut off by a peeling step.

Here “peeling” means lazy/edge peeling: a newly seen polygon is attached without immediately making every identification with the existing boundary. The active boundary is simple in the abstract explored map, but its image in the final map need not be simple. Simple/face peeling handles these identifications differently and must not be substituted without argument.

An algorithm selects an active edge using only the revealed map/history. Independent external randomness is allowed by conditioning on it. We consider algorithms that continue selecting edges on the infinite hole; choosing the cemetery state and stopping is not a counterexample. The notes explicitly exclude repeated idle steps caused by peeling finite, already-filled holes.

Exhaustion is \(\bigcup_n\bar e_n=\mathfrak m\) as explored submaps, including the necessary identifications. Equivalently, every fixed finite neighbourhood is eventually in the interior of the explored region. Since the map is locally finite, this is equivalent to finiteness almost surely of the time needed to swallow each fixed-radius ball. The assertion is for each chosen adapted algorithm, not a simultaneous probability-one assertion over uncountably many algorithms.

## The walk and what the original proof uses

Write \(W^{(j)}\) for the unpointed partition function with boundary degree \(2j\). Then

\[
\nu(k)=q_{k+1}c^k\quad(k\geq0),\qquad
\nu(-m)=2W^{(m-1)}c^{-m}\quad(m\geq1).
\]

Set

\[
d(p)=4^{-p}\binom{2p}{p}\ (p\geq0),\qquad
h(p)=2p\,d(p)\ (p\geq1),
\]

with \(d(p)=0\) for \(p<0\), and \(h(p)=0\) for \(p\leq0\). Thus \(h(1)=1\), \(d(0)=1\), and \(h(p)\sim2\sqrt{p/\pi}\). The two functions have different boundary values at zero.

Admissibility gives \(d\)-harmonicity on the positive integers. Criticality is equivalent to \(h\)-harmonicity there, in particular

\[
\sum_{k\geq0}\nu(k)h(k+1)=1.\tag{1}
\]

The unconditioned walk oscillates in the critical case. The infinite-map half-perimeter satisfies

\[
\Pr(P_{n+1}=p+k\mid\mathcal F_n)
 =\nu(k)\frac{h(p+k)}{h(p)},\qquad p+k\geq1.\tag{2}
\]

Its law does not depend on the algorithm. Conditional on a negative step \(-m\), the finite swallowed region is on either side with probability \(1/2\). Its boundary degree is \(2(m-1)\), not \(2m\); the half-perimeter drops by \(m\).

In Corollary 27, a fixed boundary vertex has a one-step swallowing probability of order \(p^{1-a}\). Proposition 26 supplies the conditioned stable scaling \(P_n/n^{1/(a-1)}\). A Jeulin argument then proves \(\sum_n P_n^{1-a}=\infty\). Thus that proof uses tail asymptotics **and** distributional control of the conditioned walk. Harmonicity alone supplies (2), but not the displayed stable scaling.

## A critical-law parametrization and an exact negative kernel

The following calculation isolates the irregular cases without guessing an arbitrary step distribution and calling it critical.

Let \(r=(r_K)_{K\geq1}\) be a probability distribution with \(r_1<1\). Define

\[
\mu(K)=\frac{r_K}{K}\quad(K\geq1),\qquad
\mu(0)=1-\sum_{K\geq1}\frac{r_K}{K},\quad Z=\mu(0)^{-1},
\]
\[
q_K=\frac{\mu(K)}{Z^{K-1}\binom{2K-1}{K-1}}.\tag{3}
\]

Then \(\mu\) is a probability law with mean one and \(\mu(0)>0\). Direct substitution gives

\[
f_q(Z)=1-\frac1Z,\qquad
Z^2f'_q(Z)=Z\sum_K(K-1)\mu(K)=1.
\]

The function \(f_q(x)-1+1/x\) is strictly convex on its positive domain, so this tangent zero is the smallest positive solution. Hence (3) is admissible and critical. Conversely every critical sequence gives this \(\mu\), with \(r_K=K\mu(K)\). A mass at \(K=1\) is simply a holding component.

For \(m\geq1\), the associated increment law has the exact formula

\[
\boxed{\quad
\nu(-m)=\frac{d(m-1)}{2m}\sum_{K\geq1}r_K\frac{K-1}{m+K-1}.
\quad}\tag{4}
\]

To derive it, use the integrated pointed partition function, Curien (5.3), printed p. 50. Let

\[
G(t)=Z\left(t-\sum_{K\geq1}\mu(K)t^K\right),\quad 0\leq t\leq1.
\]

Then \(G(0)=0\), \(G(1)=1\), and \(G'(t)=Z(1-\sum_Kr_Kt^{K-1})\geq0\). In the vertex-weight interpolation, \(t\) is the normalized pointed resolvent parameter. Consequently

\[
\nu(-m)=\frac{d(m-1)}2\left(\frac1m-\sum_K\frac{r_K}{m+K-1}\right),
\]

which is (4). Termwise integration is justified by nonnegativity, or by monotone convergence from \(t<1\).

Also \(\nu(K-1)=r_K/h(K)\). Thus \(\nu\) is a convex mixture, with weights \(r_K\), of the critical pure \(2K\)-angulation step laws

\[
\nu_K(K-1)=\frac1{h(K)},\qquad
\nu_K(-m)=\frac{d(m-1)}{2m}\frac{K-1}{m+K-1}.\tag{5}
\]

For \(K=1\), take \(\nu_1=\delta_0\). Because each component has the same harmonic function, the Doob transform also commutes with this mixture. This is useful both for the proof and for simulation. Formula (4) is a bipartite specialization of the positive-to-negative kernel relations in Budd's Lemma 4; no priority claim is made for it.

## Proof of the partial exhaustion criterion

For integer \(p\geq32\), define

\[
H_\nu(p)=\frac12\sum_{m=\lceil3p/4\rceil}^{\lfloor7p/8\rfloor}
 \nu(-m)\frac{h(p-m)}{h(p)}.\tag{6}
\]

**Hazard lemma.** Whatever active edge an adapted algorithm selects, each specified vertex on that boundary has conditional probability at least \(H_\nu(p)\) of becoming interior at the next step.

Indeed, the boundary has \(2p\) edges. On the two sides of the selected edge, its vertices split into two blocks of \(p\) vertices. A step \(-m\) on a specified side makes the \(2m-1\) intermediate corners interior and identifies the two outer endpoints. In (6), \(2m-1>p\). At least one side therefore contains the chosen vertex strictly inside the swallowed arc. Its transition probability is the corresponding half of (2). Summing over \(m\) proves the bound. Multiple future identifications of boundary images can only help swallow the represented vertex; the argument is on the abstract active contour.

**Comparison lemma.** There are absolute constants \(0<c_0<C_0<\infty\) such that, for every critical sequence and \(p\geq32\),

\[
c_0p\nu(-p)\leq H_\nu(p)\leq C_0p\nu(-p).\tag{7}
\]

For a proof, write (4) as \(\nu(-m)=w(m)A(m)\), where

\[
w(m)=d(m-1)/(2m),\qquad
A(m)=\sum_Kr_K(K-1)/(m+K-1).
\]

For \(p/2\leq m\leq p\), termwise comparison gives

\[
1\leq A(m)/A(p)\leq p/m.
\]

The central-binomial formula gives \(w(m)/w(p)\) bounded above and below by absolute constants on this interval. In (6), \((p-m)/p\in[1/8,1/4]\), so \(h(p-m)/h(p)\) has analogous bounds. There are order \(p\) summands. This proves (7), without regular variation or a moment assumption.

**Proposition.** If (R) holds for every initial state of (2), every continuing adapted filled-in algorithm exhausts the map almost surely.

Fix a boundary vertex at a deterministic exploration time. Let \(Z_n\) indicate that its boundary representative has survived until time \(n\), propagating identifications in the usual way. Define \(H_\nu(p)=0\) for \(p<32\). The hazard lemma gives

\[
\mathbb E[Z_{n+1}\mid\mathcal F_n]\leq Z_n(1-H_\nu(P_n)).
\]

Hence \(Z_N/\prod_{n<N}(1-H_\nu(P_n))\) is a nonnegative supermartingale. On perpetual survival and divergence of \(\sum_nH_\nu(P_n)\), it would tend to infinity, contradicting supermartingale convergence. The positive conditioned walk is transient (Curien, Proposition 13, printed p. 37), so it eventually leaves every bounded set. By (7), (R) implies the required divergence. The vertex is therefore eventually interior almost surely.

There are finitely many boundary vertices at each finite time and countably many such times. Applying the argument to all of them shows that every revealed boundary is eventually swallowed. Induction through adjacent faces then discovers every finite dual neighbourhood of the root; local finiteness gives every fixed primal neighbourhood as well. Equivalently, the time to swallow each fixed ball is finite almost surely. This proves the proposition.

This is a **sufficient** perimeter-only reduction. The perimeter alone does not determine which vertex or ball was swallowed; an exact formulation needs the cyclic boundary with marked vertices and the algorithm's edge choice. In particular, convergence of (R) would not prove failure: smaller swallowed arcs might still remove every mark.

## Critical sequences of no stable type

Take \(0<\beta<1\), \(t=2^{-\beta}\), and

\[
r_{2^j}=(1-t)t^{j-1},\quad j\geq1,
\qquad r_K=0\text{ otherwise}.
\tag{8}
\]

Construction (3) gives an explicit critical sequence, with \(Z=2-t\), supported on face half-degrees \(2,4,8,16,\ldots\). The offspring law has infinite variance because

\[
\sum_KK^2\mu(K)=\sum_KKr_K
 =2(1-t)\sum_{j\geq1}(2t)^{j-1}=\infty.
\]

It has no regularly varying positive tail. Here is a proof at the level of the perimeter law, not merely an observation that some point probabilities vanish. Let \(T(x)=\nu([\lceil x\rceil,\infty))\). For large \(n\), with \(x_n=(9/8)2^n\) and \(\lambda=4/3\), both thresholds lie in the same gap between consecutive possible positive jumps, so

\[
T(\lambda x_n)/T(x_n)=1.
\]

For \(y_n=(7/4)2^n\), multiplying by \(\lambda\) crosses exactly one jump size. Since \(h(2^j)\sim2\sqrt{2^j/\pi}\), the successive tail masses have ratio tending to \(t/\sqrt2\), and therefore

\[
T(\lambda y_n)/T(y_n)\longrightarrow t/\sqrt2<1.
\]

Thus regular variation fails. The same gap argument applies to the offspring tail, whose successive masses have ratio \(t/2\). For normal attraction, check the truncated second moment separately: at x=2^n it is 2(1-t)((2t)^n-1)/(2t-1), whose ratio under doubling tends to 2t>1. It is therefore not slowly varying. These facts exclude all the stable offspring classes used in the cited exhaustion results, including normal attraction. It also excludes regularity and the old power-type definitions.

Equation (4) nevertheless yields two-sided bounds

\[
\nu(-m)\asymp m^{-(\beta+3/2)},\qquad
p\nu(-p)\asymp p^{-(\beta+1/2)}.\tag{9}
\]

To check these bounds, split the sum in (4) at \(2^j\approx m\). Above that threshold, the factor \((2^j-1)/(m+2^j-1)\) is bounded below, and the geometric tail is order \(m^{-\beta}\). Below it, the sum is bounded by \(m^{-1}\sum_{2^j<m}r_{2^j}2^j\), also order \(m^{-\beta}\). Multiply by \(w(m)\asymp m^{-3/2}\).

This shows that “every critical sequence” has substantive content even beyond slowly varying extensions: valid critical examples have genuinely non-regularly-varying tails. For (8), it would suffice to prove almost-sure divergence of \(\sum_n P_n^{-(\beta+1/2)}\). This report does not prove that assertion.

For comparison, if \(\sum_Kr_K(K-1)<\infty\), dominated convergence in (4) gives

\[
\nu(-m)\sim\frac{\sum_Kr_K(K-1)}{2\sqrt\pi}\,m^{-5/2}.
\]

Budd's Proposition 5 and the Jeulin argument recover exhaustion in this finite-variance class. This extension beyond exponential regularity is already covered by the published Curien–Marzouk theorem; it is not a new resolution of C0057. Criticality does not force this moment condition, as (8) demonstrates.

## What was computed and checked

`code/perimeter.py` simulates (2) by first drawing a component \(K\) from \(r\), then its pure-component Doob kernel (5). The negative proposal is the Sibuya distribution

\[
\Pr(M=m)=d(m-1)/(2m).
\]

It is sampled as a geometric random variable with success parameter sampled from \(\operatorname{Beta}(1/2,1/2)\). Rejection by \((K-1)/(m+K-1)\,h(p-m)/h(p)\), combined with the positive atom, gives exactly the desired discrete kernel up to floating-point arithmetic. No weight sequence or jump tail is truncated. Large central-binomial values use a controlled Stirling expansion; this is numerical evidence, not exact-arithmetic sampling.

The simulation starts at \(P_0=8\), corresponding to a root/external face with 16 boundary corners. It uses uniform active-edge selection, marks all initial corners, propagates their identifications, and records when all those vertices become interior. At that time the root face's incident-vertex neighbourhood has been exposed. No finite Boltzmann fillings are generated: their internal geometry is unnecessary for this boundary absorption event. The experiment does not measure general graph-ball radii or explore adversarial algorithms.

There are 80 seeded paths per law, a 2,000-step limit, and a limit of 20,000 active boundary edges. Reaching a cap is right censoring, not non-exhaustion. The medians below use completed paths only and must not be interpreted as unconditional medians.

| Law | Root-corner absorption observed | All root-face corners absorbed | Time-censored | Edge-cap-censored | Median all-corner time among completions |
|---|---:|---:|---:|---:|---:|
| Critical quadrangulations, \(r_2=1\) | 80/80 | 80/80 | 0 | 0 | 173.5 |
| Critical octangulations, \(r_4=1\) | 80/80 | 79/80 | 1 | 0 | 93 |
| Infinite dyadic law (8), \(\beta=0.80\) | 79/80 | 70/80 | 6 | 4 | 172 |
| Infinite dyadic law (8), \(\beta=0.35\) | 61/80 | 42/80 | 0 | 38 | 74.5 |

The dyadic laws really are the infinite critical laws (8); the edge cap stops a path rather than deleting or resampling a large jump. The dense example often hits that cap, so its completion fraction and conditional median have especially limited interpretability. None of these finite experiments distinguishes almost-sure exhaustion from a small positive probability of failure.

Validation and resource evidence:

- `code/audit_exact.py` checks both harmonic identities with rational arithmetic for 128 pairs \((p,K)\), and checks criticality of a rational two-component mixture independently of the sampler.
- `code/verify.py` checks 16 floating-point kernels (maximum normalization error \(5.66\times10^{-13}\)), four elementary cyclic-boundary updates, and 30,000 draws per law at fixed perimeter. The largest standardized frequency discrepancy is 1.95.
- Simulation totals were re-aggregated from the saved CSV independently of its summary JSON. Every path is classified as completed or censored, and root absorption precedes full marked-boundary absorption when both are observed.
- The simulation took 4.16 seconds and reported maximum RSS 28,655,616 bytes, with one native thread at inherited nice 15. A requested explicit address-space limit was rejected by the macOS sandbox; boundary arrays and the harmonic cache are bounded. No substantial sweep was run.
- Source PDFs were fetched into memory and only their extracted text was saved. Oldstyle digit glyph names were normalized and non-text control bytes removed. No PDFs, scans or page images were saved anywhere in this directory. No publishing, pushes, subagents or external writes were performed.

To reproduce from this directory, under nice at least 10:

```sh
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python3 code/audit_exact.py
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python3 code/verify.py
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python3 code/simulate.py 80
```

The numerical scripts use only the Python standard library. `code/get_source.py`, used only for source retrieval, needs the already available `requests` and `pypdf`. Provenance and PDF hashes are in `data/source_manifest.jsonl`; paths, summaries and audits are in `data/`.

## Remaining mathematical issue

The exact harmonic identity holds for all critical laws, and (4) controls the spatial shape of their negative tails even when those tails have no power asymptotic. What is still missing is a time-occupation estimate for the **conditioned** walk strong enough to force (R). The original stable scaling argument supplies it in its own regimes. Neither unconditioned oscillation nor \(P_n\to\infty\) supplies it by itself. No inference from a finite expected/observed hazard to almost-sure divergence has been used.

Task: “Open problem C0057” — received in the session beginning 2026-11-13 06:52 +04 (Asia/Tbilisi).
