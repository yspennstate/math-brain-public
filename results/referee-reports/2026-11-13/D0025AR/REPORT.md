MINOR

The central theorem survives the audit. For the departure-site, state-independent clock model in Problem 4, the finite-K comparison is valid and proves

\[
f_K(\rho)=rM_K\quad\text{for}\quad
|\rho-K/2|\le \bigl(1/r-\mathbb E[1/\alpha_0]\bigr)rM_K.
\]

Here \(M_K=\max H_K=H_K(K/2)\) is the homogeneous rate-one flux maximum. The displayed quantity is the guaranteed **half-width**, not necessarily the actual critical half-width. I found no fatal mathematical gap. The requested revision is a literature correction: Bahadoran–Bodineau explicitly discuss extending their method to K-exclusion, which the claim's literature table omits. Neither that remark nor the other sources checked states the full all-laws finite-K theorem above. K=1 is already Sly's theorem; the finite-K argument is a valid extension of his method, with priority unverified.

The independent computations support central flattening on finite rings. They do not measure the infinite-volume plateau level or optimal endpoints. All retained sources are plain text, and all new code was written without reading, importing or running claim_files/code.

## Errors or gaps requiring correction

1. **Incomplete account of finite-K prior work.** Location: claim_files/REPORT.md:48, the Bahadoran–Bodineau row, and the literature conclusion at line 63. In [Bahadoran–Bodineau, arXiv:1602.06718v4](https://arxiv.org/abs/1602.06718), Section 3.2, PDF p. 13, the paragraph after Theorem 3.4 explicitly says that their approach applies to other column-disordered LPP models, including K-exclusion. Add this statement and its location. Their numbered plateau theorem is for K=1 with finite-box hypothesis (H) and sufficiently dilute disorder; the extension remark does not state or prove the all-laws finite-K interval claimed here. Thus the correction limits a priority assessment, rather than invalidating Theorem A. The claim already disclaims novelty, appropriately.

No additional substantive error was found in Theorem A, its proof, or the stated interpretation of its simulations. Two technical conventions must remain explicit in any shortened version: all weight independence is **conditional on the environment**, and the hydrodynamic flux is normalized by actual integrated current. The submitted proof supplies these conventions.

## Source statements and model

I independently downloaded [Seppäläinen, arXiv:math/9906194v1](https://arxiv.org/abs/math/9906194) and [Sly, arXiv:1609.06589v1](https://arxiv.org/abs/1609.06589). Their complete pdftotext extractions are [sources/seppalainen_1999.txt](sources/seppalainen_1999.txt) and [sources/sly_2016.txt](sources/sly_2016.txt). PDF bytes were processed in memory; no PDF or page image was written. The provenance and hashes are in [data/source_manifest.jsonl](data/source_manifest.jsonl).

Problem 4, Section 4, PDF p. 9, exactly, with line breaks and the line-end hyphen in “welcome” normalized:

> Problem 4. For the disordered TASEP, any new rigorous results would be welcome. For example, is there a phase transition similar to the one for disordered ZRP? Does the flux function f_K(ρ) have a flat segment on an interval around ρ = K/2?

The extraction preserving the original line breaks is [sources/problem4_exact.txt](sources/problem4_exact.txt).

Sly's Theorem 1, PDF p. 1, exactly, with mathematical typography normalized:

> Theorem 1. With disorder α and μ = 1/r − E[1/α(i)] for all ρ ∈ [1/2 − (1/4)μr, 1/2 + (1/4)μr],
>
> f(ρ) = r/4.

The preceding paragraph assumes a positive, nonconstant i.i.d. rate distribution with essential infimum \(r>0\). It has no dilution or endpoint-tail hypothesis. The notation is transcribed in [sources/sly_theorem1_exact.txt](sources/sly_theorem1_exact.txt).

Seppäläinen's generator (3.1), p. 8, is

\[
L^\alpha F(\eta)=\sum_x\alpha_x
\mathbf1\{\eta(x)\ge1,\ \eta(x+1)\le K-1\}
\bigl[F(\eta^{x,x+1})-F(\eta)\bigr].
\]

There is one departure clock of rate \(\alpha_x\), independent of the number of particles whenever the jump is allowed. Neither \(\eta(x)\) nor \(K-\eta(x+1)\) multiplies the clock rate. The source's environment is i.i.d. and bounded away from zero; its lower-bound letter is \(c\). The claim's \(r\) is the essential infimum. This is site/bond disorder for right jumps, not particle-label disorder.

## Sly's K=1 proof

The proof on pp. 2–4 checks out after reading its independence statements conditionally on \(\alpha\). Its two-edge wedge LPP has steps \((1,0),(-1,1)\) and rate-\(\alpha_i\) exponentials in column \(i\). The shape/current duality comes from Seppäläinen's hydrodynamics. Slow stretches give \(f\le r/4\).

The coupling adds \(U=\operatorname{Ber}(1-r/\alpha_i)\operatorname{Exp}(r)\) to each disordered exponential \(Y\). Conditional on \(\alpha\), \(U\) is independent of \(Y\), \(Y+U\sim\operatorname{Exp}(r)\), and \(\mathbb E[U\mid\alpha,Y]=1/r-1/\alpha_i\). Selecting a maximizing **Y-path** before averaging U is legitimate. Every path crosses the intermediate columns, so the mean subtraction is at least \(\mu|i|\). The resulting cusp in the passage shape gives the interval in Theorem 1.

The specifically K=1 ingredients are the two-edge graph, the explicit shape
\(r^{-1}(\sqrt{x+y}+\sqrt y)^2\), reflection about density 1/2, and its central value \(4/r\), whose reciprocal is \(r/4\). The exponential addition identity and mandatory-column argument do not require K=1.

There are harmless errors of notation in Sly's source: p. 2 writes \(\mathbb EY_{ij}=\mu\) where it means \(\mathbb EU_{ij}=\mu\); its displayed homogeneous \(k(v)\) has incorrect speed cutoffs for general r and omits the zero branch. The correct branches are \((r-v)^2/(4r)\) for \(|v|\le r\), \(-v\) for \(v\le-r\), and 0 for \(v\ge r\). The proof uses the passage shape and is unaffected. The negative-x intermediate-column sum on p. 3 also needs its evident reversed indexing. The submitted finite-K proof avoids these issues.

## Finite-K proof, checked in order

The following locations refer to the submitted REPORT.md and its equation numbers. I checked the underlying graph against [Seppäläinen's notes](https://people.math.wisc.edu/~tseppalainen/excl-book/ajo.pdf), independently extracted as [sources/seppalainen_notes.txt](sources/seppalainen_notes.txt). The original Annals article, DOI [10.1214/aop/1022677266](https://doi.org/10.1214/aop/1022677266), was not accessible through the endpoints tried; I do not claim to have checked unlocated theorem numbers in it.

### Growth graph and site rates: lines 109–163, (1)–(6)

Put \(\eta_i=h_i-h_{i-1}\). An allowed departure reduces \(h_i\) by one. To complete the cell at level h, the three prerequisites are its own preceding cell \((i,h+1)\), the left cell \((i-1,h)\), and the right cell \((i+1,h+K)\). Thus

\[
T(i,h)=Y_{i,h}+\max\{T(i,h+1),T(i-1,h),T(i+1,h+K)\}.
\]

This is precisely the predecessor rule in the notes, (9.40)–(9.44), pp. 148–150. Once eligible, a cell stays eligible until the clock at its site rings. The strong Markov/inductive proof of Lemma 9.11 works equally with fixed unequal rates: the relevant fresh waiting time is exponential of rate \(\alpha_i\). Hence the service times are mutually independent conditional on \(\alpha\). They are generally not independent after averaging over the column environment.

Changing the vertical sign gives steps

\[
(0,1),\quad(1,0),\quad(-1,K),\qquad
C_K=\{y\ge0,\ y+Kx\ge0\}.
\]

The source cell is at \((0,-1)\) in the notes' height convention. Moving it to the origin and omitting its weight changes the passage value by just that common initial service time, and the coordinate by one vertical unit. These differences vanish after scaling. The grading \(2j+Ki\) increases along every edge. There are finitely many paths to a fixed endpoint.

The vertical edge can be removed for K=1: replace it by east followed by northwest, adding a positive intermediate weight. This replacement does not work for K>1. The submitted proof **retains** the vertical edge and therefore uses the right graph.

The passage shape, inverse wedge-current shape \(k\), and flux satisfy

\[
k(v)=\inf\{y\ge b(v):\tau_\alpha(v,y)>1\},\quad
b(v)=\max(0,-Kv),\quad
f_K(\rho)=\inf_v\{k(v)+v\rho\}.
\]

These are the height/passage forms of the hydrodynamic result, with the boundary inverse interpreted continuously. The submitted paragraph at line 145 explains how to recover the height limit from the survey's density theorem by anchoring in the empty region. The right edge is dominated by a rate-one Poisson advance; bounded occupations permit approximating interval indicators by the continuous test functions in Theorem 3. Inversion at strictly interior levels then gives passage-time convergence in probability. The exponential path tail bound supplies uniform integrability and convergence of expectations. No stationary product law for K>1 is imported.

For the tail bound, if a,b,c count vertical, east and northwest steps, then \(j=a+Kc\), \(i=b-c\), and the path length is bounded by \(|i|+2j\). At most exponentially many paths and rate-r exponential domination give an exponential upper tail for \(T/n\) above a fixed constant on each ray. Independence along a path is conditional on the rates; the uniform rate-r bound makes the annealed tail estimate valid too.

### Homogeneous symmetry and the maximum: lines 165–183, (7)

The map

\[
S(x,y)=(-x,y+Kx)
\]

exchanges east and northwest edges, fixes vertical edges, and preserves \(C_K\). Homogeneous i.i.d. weights are invariant in law. Concavity and homogeneity give

\[
\tau_1(x,y)=\tau_1(S(x,y))
\le\tau_1(0,y+Kx/2)
=(y+Kx/2)\tau_1(0,1).
\]

The inequality has the correct direction. This does not assume differentiability or an explicit flux formula. Equivalently, the homogeneous flux is concave and symmetric under \(\rho\mapsto K-\rho\), so it attains its maximum at K/2. The notes' Theorem 9.5, p. 141, states this symmetry and positivity. Neither uniqueness of the maximizer nor strict concavity is needed or established.

Set

\[
J=rM_K,\qquad A=\tau_1(0,1)/r=1/J.
\]

The homogeneous central current/passage-time reciprocity is consistent with the current normalization, not an analogy replacing 1/4 by an arbitrary constant.

### Exponential addition and path selection: lines 185–233, (8)–(11)

For \(s\ge0\), the conditional transform is exactly

\[
\frac{\alpha_i}{\alpha_i+s}
\left[\frac r{\alpha_i}+
\left(1-\frac r{\alpha_i}\right)\frac r{r+s}\right]
=\frac r{r+s}.
\]

Consequently the entire field \(Z=Y+U\) is i.i.d. Exp(r) even after averaging the environment: its conditional joint law is a product that does not depend on \(\alpha\). It is not necessary that Z be independent of Y.

Choose the maximizing Y-path using only \((\alpha,Y)\). All three types of step change the column by at most one. Thus every path to column i visits columns 1 through i if i>0, or i through −1 if i<0. Since \(d_i=1/r-1/\alpha_i\ge0\),

\[
\mathbb E\sum_\gamma U
=\mathbb E\sum_\gamma d_i
\ge |i|\mu.
\]

The path's repeated visits and its dependence on the environment cause no selection error: the mandatory columns already give a deterministic lower bound before averaging. The uniform-integrability estimate just checked allows the expectation limits. Therefore

\[
\tau_\alpha(x,y)\le\tau_r(x,y)-\mu|x|
\le A(y+Kx/2)-\mu|x|. \tag{R1}
\]

This step survives for every finite K.

### Slow strips and the upper current bound: lines 235–261, (12)–(14)

Weight domination immediately gives \(\tau_\alpha(0,1)\le A\). The reverse inequality needs more than the assertion that slow stretches exist. The submitted diamond construction supplies the missing quantitative connection.

Fix m and ε first. Almost surely an interval of length \(2m+1\) with all rates at most \(r+\varepsilon\) exists. Choose it using only \(\alpha\). A path from \((a,b)\) to \((a,b+m)\) lies in that strip. Successive translated diamonds have disjoint weighted vertex sets once each starting vertex is omitted: on their shared horizontal row the earlier diamond lies to the left of column a and the later one to its right. Only the connecting vertex is common, and it is counted once.

The homogeneous diamond values are therefore i.i.d. copies of \(V_m\). Connect the origin to the selected strip and eventually back to column zero; both connectors have fixed height cost after m, ε and the strip are fixed. Their weights are nonnegative. A conditional strong law yields

\[
\liminf_{n\to\infty}\frac{T_\alpha(0,n)}n
\ge\frac{\mathbb EV_m}{m(r+\varepsilon)}.
\]

Convergence in probability to the deterministic shape suffices to transfer this lower bound to \(\tau_\alpha(0,1)\); almost-sure shape convergence is not needed. Taking m to infinity and then ε to zero gives

\[
\tau_\alpha(0,1)=A,\qquad
\max_\rho f_K(\rho)=k(0)=1/A=rM_K. \tag{R2}
\]

The order of limits is correct. The distance to a rare strip can be enormous but is fixed before n tends to infinity. No macroscopic slow interval is assumed in a typical finite ring. The argument covers continuous rate laws and atoms at r alike.

### Lower current bound and the width: lines 263–274, (15)

For \(|\rho-K/2|\le\mu/A\), apply (R1) on \(y=J-\rho x\):

\[
\tau_\alpha(x,J-\rho x)
\le1+A(K/2-\rho)x-\mu|x|\le1.
\]

If this line is below the cone boundary at v, \(k(v)\ge b(v)\) already implies \(k(v)+\rho v\ge J\). Otherwise monotonicity and the inverse relation give the same conclusion. Taking the infimum over v yields \(f_K(\rho)\ge J\). Combine with (R2).

Thus the half-width is **derived** as \(\mu/A=\mu rM_K\). The argument requires neither the explicit K=1 shape nor smoothness of the K>1 shape. Nonconstancy gives \(\mu>0\), and the homogeneous result gives \(M_K>0\). The interval lies inside [0,K]: use \(M_K\le1\) for K≥2 and \(M_1=1/4\) for K=1.

## Is this the flux in Problem 4?

Yes. Survey Theorem 3, pp. 8–9, treats exactly generator (3.1), fixed arbitrary finite K, and i.i.d. site rates. It gives quenched Euler-scale convergence for initial data satisfying (A.5), with a concave flux \(f_K\). Formula (3.2) identifies its conjugate with the associated growth shape.

A density conservation law alone only determines a flux up to an additive constant. Here the integrated-current/height construction fixes that constant, with \(f_K(0)=f_K(K)=0\). The sign convention is also consistent: a departure reduces h, \(h_t=-f_K(h_x)\), and \(k=-f_K^*\). Biconjugacy gives precisely the displayed infimum formula. Consequently (R1) and (R2) concern the source's physical current, rather than a differently normalized PDE flux or a zero-range particle speed.

Theorem 3 by itself does not prove a plateau. The new content is the finite-K exponential comparison together with the slow-strip capacity argument. The resulting theorem says nothing about uniqueness of a finite-ring condensate, relaxation times, interface fluctuations, or the optimal plateau endpoints.

## Independent numerical experiment

The experiment and analysis are in [code/ring_ctmc.cpp](code/ring_ctmc.cpp), [code/run_experiment.py](code/run_experiment.py), [code/run_long_checks.py](code/run_long_checks.py), and [code/analyze_experiment.py](code/analyze_experiment.py). Raw results, including all time-block currents, are in [data/ring_results.jsonl](data/ring_results.jsonl) and [data/ring_long.jsonl](data/ring_long.jsonl). The standalone plot is [data/current_density.svg](data/current_density.svg).

Each fixed-time window of length T uses a Poisson(nT) number of candidate events. Each event selects a site uniformly; an eligible jump is accepted with probability 1 at a fast site and 1/2 at a slow site. This is exact continuous-time uniformization, with no time-step error. Counting accepted events and dividing by nT estimates physical current per bond. The generator has exactly one eligible departure clock per site. Every window checks conserved total mass, occupation bounds, and, over measurement, the identity

\[
\eta_i(t_1)-\eta_i(t_0)=N_{i-1}-N_i.
\]

The rings have n=10,000, K=1 or 2, and disorder \(0.1\delta_{0.5}+0.9\delta_1\). The main environment has 1,006 slow sites and a longest slow run of six; a second sampled environment is a sensitivity check. Initial sweeps use burn/measurement 10,000/20,000 for disorder and 2,000/8,000 for homogeneous controls. Central endpoint/center follow-ups use 200,000/200,000, with separate packed-state runs at the center. “Random” means uniformly selecting occupied capacity slots at the prescribed total mass; it is not assumed stationary for K>1.

For this law, E[1/alpha]=1.1 and mu=0.9 (also checked with exact fractions). The homogeneous K=2 run estimates M_2=0.419204850; it is a finite-size, finite-time estimate. Its eight-block standard deviation is 0.000539, not a confidence interval.

| K | Infinite-volume level r M_K | Guaranteed half-width mu r M_K | Guaranteed interval |
|---|---:|---:|---|
| 1 | 0.125000000 | 0.112500000 | [0.387500000, 0.612500000] |
| 2 | 0.209602425 | 0.188642183 | [0.811357818, 1.188642182] |

The K=2 entries use the estimated M_2; only the K=1 level and interval are exact numerical values. Long runs on the same sampled environment give:

| K | Density | Initial state | Current | Block SD | Across-bond current range |
|---|---:|---|---:|---:|---|
| 1 | 0.3875 | random | 0.152217837 | 0.000795 | 0.152085–0.152325 |
| 1 | 0.5000 | random | 0.152424610 | 0.000919 | 0.152290–0.152545 |
| 1 | 0.6125 | random | 0.152715946 | 0.000966 | 0.152585–0.152820 |
| 2 | 0.8115 | random | 0.243175604 | 0.001512 | 0.242915–0.243625 |
| 2 | 1.0000 | random | 0.243685634 | 0.001508 | 0.243530–0.243855 |
| 2 | 1.1885 | random | 0.244171567 | 0.000950 | 0.244055–0.244300 |
| 1 | 0.5000 | packed | 0.152905396 | 0.001153 | 0.152765–0.153055 |
| 2 | 1.0000 | packed | 0.243798642 | 0.000569 | 0.243610–0.244075 |

For K=1, the long random-state currents span 0.152217837–0.152715946. The center exceeds the proposed thermodynamic level by 21.9%. The short random-state center was 0.169206295.
For K=2, the long random-state currents span 0.243175604–0.244171567. The center exceeds the proposed thermodynamic level by 16.3%. The short random-state center was 0.273258740.

Block standard deviations describe temporal variation, not independent-sample errors or disorder uncertainty. Across-bond agreement and packed/random agreement are equilibration diagnostics, not proofs of stationarity. The sampled longest slow run is six; the second environment has only three and gives substantially higher short-run center currents. Finite-size capacity and time-to-equilibrium therefore matter separately. These experiments exhibit a nearly flat central finite-ring curve but do not verify the infinite-volume plateau height, its exact half-width, or the true endpoints. Being above r M_K at finite n is compatible with (R2), whose rare-strip limit takes place on the infinite lattice. A wider observed flat interval would also be compatible, because the theorem provides a guaranteed subinterval.

Small-ring validation independently enumerated all states at fixed mass and solved stationary balance; a second solver used exact rational Gaussian elimination. Results are in [data/small_ring_validation.json](data/small_ring_validation.json) and [data/rational_validation.json](data/rational_validation.json).

| Model | Exact current | Simulated current |
|---|---:|---:|
| n=6, K=1, mass 3, all rates 1 | 0.300000000000 | 0.299969916667 |
| n=6, K=1, mass 3, rates (1,1,.5,.5,.5,1) | 0.186102428468 | 0.186112666667 |
| n=5, K=2, mass 5, rates (1,1,.5,.5,.5) | 0.281937662865 | 0.281607900000 |
| n=5, K=2, mass 5, all rates 1 | 0.488658852185 | 0.488549000000 |

The rational solver verifies normalization and all balance equations exactly. The homogeneous K=1 value was also checked against \(m(n-m)/(n(n-1))\). The numerical balance residuals were below \(6\times10^{-17}\). This validates clock rates and current normalization, not an infinite-volume phase transition.

The separate [growth audit](code/check_growth.py) checked 1,291 endpoints for K=1,...,7, reflection, mandatory columns, diamond disjointness, and the redundancy of K=1 vertical edges. The transform identity was also checked with exact fractions. Finite checks supplement the arguments above.

## Literature and value

The search was performed on 13 November 2026. I inspected the full texts listed below except where a limitation is stated. Searching titles, K-exclusion/flat-segment/plateau terms, and Sly's citation neighborhood found no explicit published all-laws theorem for every finite K. This is a bounded literature finding, not a certificate of priority.

| Work | What was verified | Effect on this claim |
|---|---|---|
| Seppäläinen, survey math/9906194; Ann. Probab. 27 (1999), 361–415 | Survey Eq. (3.1), Theorem 3, Problem 4; notes Theorems 9.3–9.5 and Lemma 9.11. Original Annals full text inaccessible at tried endpoints. | Site-disordered finite-K hydrodynamics and growth framework; does not itself give the plateau answer. |
| [Sly, arXiv:1609.06589](https://arxiv.org/abs/1609.06589) | Theorem 1 and entire four-page proof. | Exactly the claimed K=1 conclusion, already public in 2016. It does not state the finite-K theorem. |
| [Bahadoran–Bodineau, EJP 23 (2018), paper 44](https://doi.org/10.1214/18-EJP137), arXiv:1602.06718v4 | Proposition 2.1; Theorems 2.4/2.6; (H); Remark 2.5; K-exclusion extension paragraph on p. 13. | Dilute K=1 plateau under (H), with stronger quantitative dilute-limit information. General K-extension of their approach is explicitly acknowledged in print. This is not the all-laws finite-K theorem proved here. |
| [Bahadoran–Bodineau, BJPS 29 (2015), 282–312](https://doi.org/10.1214/14-BJPS277) | Author institution's bibliographic record and abstract; full PDF retrieval unsuccessful. | Equivalence of flux formulations and heuristic phase transition; not verified as a finite-K plateau theorem. |
| [Bahadoran–Guiol–Ravishankar–Saada, AIHP 50 (2014), 403–424](https://arxiv.org/abs/1201.2160) | Theorem 2.1 and flux definition. | General quenched hydrodynamics in random environments; existence of a flux is not its plateau identification. Guiol, not Mountford, is an author here. |
| [Bahadoran–Mountford–Ravishankar–Saada, Ann. Probab. 48 (2020), 404–444](https://arxiv.org/abs/1801.01654) | Theorem 2.1 and the model/flux definitions. | Condensation-regime site-disordered zero-range hydrodynamics, without a finite receiving capacity; not this K-exclusion theorem. |
| [Basu–Sidoravicius–Sly, arXiv:1408.3464](https://arxiv.org/abs/1408.3464) | Theorem 2 and defect-line model. | A single slow bond reduces maximal K=1 current. Different environment; neither its capacity nor its conclusion is the i.i.d. finite-K result. |
| [Emrah–Janjigian–Seppäläinen, EJP 26 (2021), paper 33](https://arxiv.org/abs/1908.09319) | Model definition, Section 2.4, Theorem 3.10, Sly citation. | Additively separable row/column rates, corresponding to particle/hole disorder; spatial site disorder is diagonal in those coordinates. Does not supply this theorem. |
| [Emrah–Janjigian–Seppäläinen, Anomalous geodesics, CMP (2025)](https://doi.org/10.1007/s00220-025-05470-8), arXiv:2408.13382v2 | Model, introduction, bibliography. | Related integrable inhomogeneous LPP and queues, not finite-K site disorder; still cites Sly's arXiv note. |

OpenAlex's citation endpoint for Sly returned four records: two versions of Bahadoran–Bodineau and the 2021/2025 Emrah–Janjigian–Seppäläinen papers. The raw response is [data/sly_citations_openalex.json](data/sly_citations_openalex.json). This identified no additional 2016–2026 finite-K theorem; it is not an exhaustive census of all citations. Semantic Scholar's API returned 429. Direct searches also produced no additional matching finite-K theorem.

**Publication status of Sly's note:** I found it as the 2016 arXiv preprint, not a verified journal article. The arXiv record has one version and no journal reference; OpenAlex labels the work a preprint, Crossref title search found no matching journal publication, and the inspected 2025 bibliography cites the arXiv version. Thus it should be cited as an arXiv preprint unless a journal reference is supplied. An arXiv DOI is not evidence of journal publication.

**Value:** the mathematical claim is correct in the exact finite-K site model. K=1 has no novelty. For K>1 the proof supplies a valid extension of Sly's coupling, using an established three-edge growth graph and symmetry in place of the explicit integrable shape. I did not locate the precise extension and interval already stated in print; I cannot certify originality. The result proves a nondegenerate central plateau for every nonconstant i.i.d. law with positive essential infimum, its height \(rM_K\), and the stated guaranteed interval. It does not compute \(M_K\) explicitly for K>1 or locate the true endpoints.

## Reproduction and constraints

Build with `clang++ -O3 -std=c++17 code/ring_ctmc.cpp -o code/ring_ctmc`. From a shell already at nice 10, run `python3 code/run_experiment.py`, then `python3 code/run_long_checks.py`. The runners append records, so use new output filenames for a repeat. For small checks, build the same source as `code/ring_check`, run `python3 code/check_small_rings.py`, then `python3 code/rational_balance.py`. Run `python3 code/check_growth.py` and `python3 code/analyze_experiment.py` for the graph audit and figures. NumPy and Matplotlib are needed only for validation/analysis; numerical-library thread limits are set to one in those scripts.

One large-ring simulation worker ran sequentially at nice 10. Small finite-state checks used one additional worker while the large-ring job ran; total computation stayed below four threads and far below 4 GB. Source extraction and compilation were local. No source PDFs, scans or page images were retained; no publication or push occurred. The input claim files were left unchanged.

Task: “Break it if it is wrong” — independent referee audit of D0025, received 13 November 2026 at 11:51 +04.
