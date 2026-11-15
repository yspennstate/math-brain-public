RESOLVED_IN_LITERATURE

Pete's proposed universal wired limit is false. A concrete zero-field counterexample has

\[
G=T_3,\qquad q=3,\qquad p=\frac{17}{23}.
\]

For every sequence of finite cubic graphs converging locally weakly to the 3-regular tree, the FK measures at these parameters converge locally to the **free** tree measure. In particular this holds in probability for uniformly random simple cubic graphs. Free and wired differ:

\[
\phi^{\mathrm f}_{p,3}(e\text{ open})=\frac{17}{35},\qquad
\phi^{\mathrm w}_{p,3}(e\text{ open})=\frac{113}{215},\qquad
\frac{113}{215}-\frac{17}{35}=\frac{12}{301}>0.
\]

The decisive published result is Basak–Dembo–Sly, *Potts and Random Cluster Measures on Locally Regular-Tree-Like Graphs*, Communications in Mathematical Physics **406**, article 168 (2025), **Theorem 1.12(ii), article page 8 of 58**. Proposition 1.4, pp. 4–5, supplies the Bethe pressure identity; Proposition 1.5, p. 5, describes the parameter regions. See the [published paper](https://doi.org/10.1007/s00220-025-05319-0) and [its saved text](sources/basak_dembo_sly_published.txt). The corresponding theorem is on p. 7 of arXiv:2312.16008v3. This is convergence of the entire local law, not just its edge density.

This resolves the yes/no question negatively; it does not classify every nonamenable transitive limit graph. The user's step-1 stopping rule applies, so no Swendsen–Wang or Chayes–Machta campaign was run. The proof below verifies the application of the printed theorem and supplies an explicit deterministic graph sequence.

**The source and its scope.** The live [Pete URL](https://math.bme.hu/~gabor/PGG.pdf), retrieved November 13, 2026, returned the notes dated April 3, 2024, with 243 PDF pages. Question 14.19 is on printed/PDF p. 215. Its complete text is in [sources/pete_PGG.txt](sources/pete_PGG.txt), with page delimiters, retrieval time, URL and a hash of the PDF response, which was not retained.

The question asks about all FK(p,q) models, emphasizing q>1. It does not restrict p to an ordered or percolative regime, condition on a giant component, or exclude the free measure. The following paragraph states its intent explicitly: “In the non-amenable case, the question is if the limit could be strictly dominated by the wired measure.” The question's displayed sentence does not itself say the approximating graphs are finite; finite graphs, as specified by the user, already furnish the negative answer.

Here local weak convergence of decorated graphs uses a uniformly selected root and the open/closed edge configuration in every fixed-radius neighborhood. BDS proves a stronger assertion: the finite-graph marginal around that root converges in probability, in total variation for every fixed radius, to the prescribed tree marginal. Random regular graphs involve randomness in the underlying graph as well. This is not a limit around a specially chosen vertex or a phase-conditioned finite law.

Use the normalization

\[
w=\frac p{1-p}=e^\beta-1,\qquad p=1-e^{-\beta}.
\]

The finite law is proportional to \(q^{k(A)}w^{|A|}\). The Potts β multiplies the equal-color indicator. In an Ising convention with interaction \(\beta_I\sigma_u\sigma_v\), one instead has \(\beta=2\beta_I\) and \(p=1-e^{-2\beta_I}\). All applications below have external field B=0. BDS's ghost edges are then closed and do not change the model.

**Proof.** On a finite tree with free boundary, \(k(A)=|V|-|A|\), so its FK weight factors as \(q^{|V|}\prod_e(w/q)^{1\{e\in A\}}\). The edges are independent with open probability

\[
\widehat p=\frac{w}{q+w}=\frac{p}{p+q(1-p)}.
\]

The infinite free measure has this same product law. At w=17/6, q=3 its density is 17/35.

To compute wired, let ν be a homogeneous Potts cavity message on T_d. Summing over a child spin contributes \(1+w\nu_i\) to a parent spin i. Multiplying the d−1 child factors gives the exact recursion

\[
\operatorname{BP}(\nu)_i
=\frac{(1+w\nu_i)^{d-1}}{\sum_j(1+w\nu_j)^{d-1}}.
\]

Free boundary gives the uniform message. Fixing boundary spins to color 1 gives iteration from the point mass at color 1. By symmetry the limiting coordinates are proportional to \((r,1,\ldots,1)\), with

\[
r=\left(\frac{(1+w)r+q-1}{r+w+q-1}\right)^{d-1}.
\]

For d=q=3 put r=s². The equation factors as

\[
s^3-(1+w)s^2+(w+2)s-2=(s-1)(s^2-ws+2)=0.
\]

At w=17/6 the positive roots are 1, 4/3, 3/2. The wired recursion selects the largest one, giving

\[
\nu_{\mathrm w}=(9/17,4/17,4/17),\qquad
\nu_{\mathrm f}=(1/3,1/3,1/3).
\]

Here selection of the largest root is rigorous: the map in r is increasing, since its inner ratio has derivative with positive numerator \((1+w)(w+q-1)-(q-1)\). Iteration from infinity decreases after its first finite iterate and stays above every fixed point. Its limit is consequently the largest fixed point, 9/4.

Before including the interaction of an edge, its endpoints have independent cavity messages ν. Including it gives joint weights \((1+w\mathbf1_{i=j})\nu_i\nu_j\). The Edwards–Sokal bond opens with probability p when the colors agree. Thus its density is

\[
\rho(\nu)=\frac{w\sum_i\nu_i^2}{1+w\sum_i\nu_i^2}.
\]

Fixing all boundary spins to one color has the wired FK bond marginal: the omitted factor q for the boundary cluster is constant and cancels in normalization. Taking increasing tree balls preserves that equality. Since \(\sum_i\nu_{\mathrm w,i}^2=113/289\), wired has edge density 113/215. This already proves that the two tree laws differ.

The Bethe pressure of a homogeneous message is

\[
\Phi(\nu)=\log\!\left(\sum_i(1+w\nu_i)^d\right)
-\frac d2\log\!\left(1+w\sum_i\nu_i^2\right).
\]

Free gives \(\Phi_{\mathrm f}=\log3+\tfrac32\log(35/18)\). For wired,

\[
\sum_i(1+w\nu_{\mathrm w,i})^3=(5/2)^3+2(5/3)^3=5375/216,
\qquad 1+w\sum_i\nu_{\mathrm w,i}^2=215/102.
\]

An exact rational comparison is

\[
\exp\{2(\Phi_{\mathrm f}-\Phi_{\mathrm w})\}
=\frac{14749}{14739}>1.
\]

The two messages differ and free has strictly greater pressure. BDS Proposition 1.5(ii) therefore places the parameters in \(\mathsf R_{\mathrm f}\). **Theorem 1.12(ii) then gives the free local limit.** Any cubic sequence converging locally to T_3 satisfies its uniform-sparsity hypothesis automatically. No expansion hypothesis is needed for this off-critical result. This completes the proof using the published theorem.

There is an open interval of counterexample parameters. For d=3 and integer q≥3 the same quadratic gives wired onset at \(w_{\mathrm u}=2\sqrt{q-1}\). The finite-graph transition is

\[
w_{\mathrm c}(d,q)=\frac{q-2}{(q-1)^{1-2/d}-1}-1.
\]

The latter formula is given immediately after Bencs–Borbényi–Csikvári, Theorem 1.1, published p. 205. At q=3 it is \(w_{\mathrm c}=2^{1/3}+2^{2/3}\). Hence all

\[
\frac{2\sqrt2}{1+2\sqrt2}<p<
1-\frac1{1+2^{1/3}+2^{2/3}}
\quad (0.738796125\ldots<p<0.740078950\ldots)
\]

give free finite-graph local limits strictly below wired. To verify the rational witness's position without decimals, \((17/6)^2>8\); and \(w_{\mathrm c}\) is the root above √2 of \(x^3-6x-6=0\). This polynomial is increasing there and equals −55/216 at 17/6. Thus \(w_{\mathrm u}<17/6<w_{\mathrm c}\).

An explicit deterministic sequence needs no probabilistic existence argument. Color T_3's edges with a,b,c, one of each at every vertex; identify its vertices with reduced words in \(\langle a,b,c\mid a^2=b^2=c^2=1\rangle\). For R≥2 take two copies of the radius-R ball. Define permutations s_a,s_b,s_c on their joint vertex set S_R: retain each internal edge of that color as a transposition; when a vertex is missing that color's edge, transpose it with its identical vertex in the other copy. These are involutions. Let H_R be their finite subgroup of Sym(S_R), and set

\[
G_R=\operatorname{Cay}(H_R,\{s_a,s_b,s_c\}).
\]

Every nonempty reduced word of length at most R moves the first ball's center, because its successive images follow the original tree path. No such word is the identity permutation. Thus the generators are distinct nonidentity involutions, G_R is finite, connected, simple and cubic, and its girth is greater than R. Its order tends to infinity: words of length at most R send the center to distinct vertices. For every fixed radius, all G_R neighborhoods are eventually tree neighborhoods. This proves local weak convergence to T_3. That tree is transitive and nonamenable: a finite nonempty S has at most |S|−1 internal edges, so more than |S| edges leave S. The theorem applied to G_R supplies a deterministic counterexample sequence. No large permutation group was generated computationally.

**The mechanism and the Ising comparison.** Outside a finite neighborhood, open connections induce a random partition of its boundary vertices. Long cycles in the underlying finite graph do not guarantee that these connections occur under its equilibrium FK law. For q>2, an ordered BP fixed point can exist while the disordered state has greater pressure; the finite graph then selects free. Above the pressure crossing, the ordered state is selected and the limit is wired. At a crossing, phase mixtures become possible. Existence of a fixed point alone does not establish its equilibrium dominance.

For q=2 there is no first-order gap between the appearance of order and the pressure transition. Montanari–Mossel–Sly, Theorem 2.4(I), downloaded PDF pp. 4–5, gives the balanced plus/minus spin mixture on locally regular-tree-like graphs. The Edwards–Sokal edge kernel depends only on whether endpoint spins agree and is unchanged by a global flip. Plus and minus therefore have the same wired FK marginal, and their mixture has that marginal too. This is consistent with wired; it is not a free/wired FK mixture. Below and at p=2/d the free and wired FK measures coincide; above it they differ.

“Uniqueness” in some tree papers refers to a DLR specification which identifies infinite exterior clusters at infinity. Once the free product law has multiple infinite clusters, it need not belong to that class. Uniqueness within the wired specification consequently does not say free=wired as weak limits. Pete does not exclude the free weak limit in this way. Our example lies even below the free tree percolation threshold, p=3/4, so this convention cannot remove the counterexample.

Free-boundary balls of T_3 would not be valid uniform-root counterexamples: a positive fraction of their vertices stay near the leaves. They do not converge in the Benjamini–Schramm sense to T_3. The cubic Cayley construction avoids that mistake.

The following table records the scope certified by the checked sources. Here p_u is the onset of free/wired disagreement on the tree and p_c is the finite-graph order/disorder threshold. They are different for q>2.

| Parameters | Local limit | Graph class and qualification |
|---|---|---|
| q=1, all p | Bernoulli(p), free=wired | Exact on every finite graph and hence every local graph limit. |
| q>1, free=wired on T_d | The common tree law | Local domain-Markov boundary comparison; includes p≤q/(d+q−2) for 1<q≤2. |
| q=2, p>2/d | Wired FK | MMS Theorem 2.4(I), locally tree-like d-regular sequences. Its expansion assumption is for conditioning spins on positive magnetization, not the unconditioned FK assertion. |
| Integer q≥3, d≥3, p<p_c | Free FK | BDS Theorem 1.12(i)–(ii), uniformly sparse locally T_d-like sequences, including random regular graphs. It differs from wired when p_u<p<p_c. |
| Integer q≥3, d≥3, p>p_c | Wired FK | BDS Theorem 1.12(iii), the same class, without expansion for the unconditioned limit. |
| Real q sufficiently large, d≥5, p<p_c or p>p_c | Free below, wired above | HJP Theorem 1(4)–(5), their small-set-expansion class, including random regular graphs with high probability. Already a direct earlier negative answer for p_u<p<p_c. |
| Same large-real-q setting, p=p_c, random regular graphs | Genuine free/wired phase coexistence | HJP Theorem 2: conditional local limits are free/wired, and the disordered weight converges in distribution over graphs to 1/(1+Q), with 0<Q<∞. There is no universal deterministic mixture coefficient. |
| Noninteger q>2 outside the preceding HJP range | Full pressure formula published; stronger off-critical local structure announced | BBC Theorem 1.1 is a pressure theorem. Borbényi's 2025 slides pp. 16–17 label the broader local result “BBCs ’25+”; not used here as a published theorem. |
| 1<q<2 above p_u | No complete theorem-level classification certified in this audit | Related 2025–2026 talks were located. This is a limit of this audit, not a claim that this range remains open. |

For the common-law row, the justification is elementary. Condition on the FK edges outside a tree neighborhood. They induce a boundary partition; for q≥1 its conditional law is stochastically between free and fully wired boundary laws. Enlarge the neighborhood. If the two infinite-tree limits coincide, these two bounds converge to the same local law. The proportion of roots with a non-tree neighborhood tends to zero, which proves the assertion. At the continuous critical point for 1<q≤2 the tree limits still agree.

For integer q≥3 the transition is explicitly

\[
p_c(d,q)=1-\frac{(q-1)^{1-2/d}-1}{q-2}.
\]

Its continuous q=2 limit is 2/d. It is not the percolation threshold of the free tree law.

At q>2 criticality one must not infer an always-wired limit. The HJP theorem above already disproves that. Nor does the off-critical BDS theorem give a universal critical mixture coefficient: Remark 1.15 and the figure caption specifically flag the zero-field critical point. Du–Zhou's 2025 preprint proves critical-mixture results on expanders in Theorems 1.4–1.6, p. 4, but its displayed critical line has 0<B<B_+. Its FK theorem permits real q>2. Its proof discussion on p. 12 states that the construction extends to B=0; that remark is not used here as an all-q zero-field random-regular mixture formula. Only the zero-field large-q critical statement of HJP is needed for the certified critical row.

The literature search and theorem checks were as follows; full saved source URLs and retrieval hashes are also in [data/source_manifest.json](data/source_manifest.json).

1. **Basak–Dembo–Sly (2025)**, [published paper](https://doi.org/10.1007/s00220-025-05319-0). Theorem 1.12(ii), article p. 8, is decisive. Its version of record and v3 use Proposition 1.4, pp. 4–5; the older arXiv v2 calls the pressure identity Assumption 1.4. For cubic zero-field graphs that assumption was already supplied by BBC. Definitions of local convergence and free/wired FK measures were checked, including the B=0 reduction. Theorem 1.18 on dominant-color conditioning has an expansion hypothesis; it is unnecessary here.
2. **Helmuth–Jenssen–Perkins**, [arXiv:2006.11580v2](https://arxiv.org/abs/2006.11580v2), published in *Annales IHP Probab. Stat.* **59** (2023), 817–848. **Theorem 1(4)–(5), arXiv p. 5**, gives free/wired convergence; **p. 6 explicitly states β_u<β_c**. **Theorem 2, arXiv p. 6**, gives critical coexistence and random phase weights. The result assumes d≥5, sufficiently large real q, and their expansion profile; random regular graphs belong with high probability. An author-manuscript mirror is also saved; it has an extra cover sheet, so its PDF page numbers are shifted.
3. **Bencs–Borbényi–Csikvári**, [*Random Cluster Model on Regular Graphs*](https://doi.org/10.1007/s00220-022-04552-1), CMP **399** (2023), 203–248. **Theorem 1.1 and subsequent critical formula, p. 205 (PDF p. 3)**, apply to real q≥2, w≥0 and essentially large-girth d-regular sequences. This allows a vanishing density of short cycles, rather than requiring the minimum girth to diverge, and includes random regular graphs. It supplies a pressure limit; citing it alone as a full local-law theorem would overstate its conclusion. Section 4.1, pp. 246–247, explains the difficulty for its rank-2 approximation when 1<q<2.
4. **Dembo–Montanari**, [*Ising models on locally tree-like graphs*](https://arxiv.org/abs/0804.4726). **Theorem 2.4, downloaded PDF p. 5**, establishes the Ising pressure formula under locally Galton–Watson and moment hypotheses. Theorems 2.6–2.7, pp. 7–8, treat BP/local marginals at positive field. It does not establish an always-wired Potts limit for q>2.
5. **Dembo–Montanari–Sun**, [*Factor models on locally tree-like graphs*](https://arxiv.org/abs/1110.4821). **Theorem 1.9, downloaded PDF p. 12**, extends the Ising pressure formula to its general limiting-tree framework. The paper's Potts and BP analysis is background for the later phase classification.
6. **Dembo–Montanari–Sly–Sun**, [*The replica symmetric solution for Potts models on d-regular graphs*](https://arxiv.org/abs/1207.5500). **Theorem 2, downloaded PDF p. 8**, identifies the relevant Bethe maximizers; **Theorem 3, also p. 8**, gives the Potts pressure formula for even d. The even-degree restriction must not be dropped when citing this result. BBC supplies the cubic zero-field case used here.
7. **Montanari–Mossel–Sly**, [*The weak limit of Ising models on locally tree-like graphs*](https://arxiv.org/abs/0912.0719). **Theorem 2.4(I), downloaded PDF p. 4**, is the balanced spin-mixture statement; part (II) assumes expansion for the conditional plus law. Page 5 discusses the unique-state regime.
8. **Basak–Dembo**, [*Ferromagnetic Ising measures on large locally tree-like graphs*](https://arxiv.org/abs/1205.4749), *Ann. Probab.* **45** (2017), 780–823. **Theorem 1.6, downloaded PDF p. 6**, extends the mixture result to random-tree limits at continuity points of its observable U(β,0). Those continuity and graph hypotheses cannot be omitted outside the regular-tree setting.
9. **Coja-Oghlan–Galanis–Goldberg–Ravelomanana–Štefankovič–Vigoda**, [*Metastability of the Potts ferromagnet on random regular graphs*](https://arxiv.org/abs/2202.05777). **Theorems 1.1–1.2, downloaded PDF p. 5**, concern metastability and dynamics; **Theorem 1.3, p. 6**, distinguishes the equilibrium weights. A state with a long residence time can still have exponentially small stationary probability. A sampler staying near wired below p_c would not identify the equilibrium local limit.
10. **Häggström**, [*The random-cluster model on a homogeneous tree*](https://doi.org/10.1007/BF01247839), PTRF **104** (1996), 231–253. **Theorems 1.5–1.6, p. 235 (PDF p. 5)**, distinguish continuous onset for 1<q≤2 from discontinuous onset for q>2. His forward branching parameter n is d−1 here. His uniqueness assertions use a boundary specification which must be checked before comparing them to free/wired weak limits.
11. **Lyons**, [*The Ising model and percolation on trees and tree-like graphs*](https://doi.org/10.1007/BF01217911), CMP **125** (1989), 337–353, and **Jonasson**, [*The random cluster model on a general graph and a phase transition characterization of nonamenability*](https://doi.org/10.1016/S0304-4149(98)00086-6), SPA **79** (1999), 335–354, were searched as requested. Lyons's bibliographic entry and scope were checked on [his publication page](https://rdlyons.pages.iu.edu/#ising); the attempted full-text retrieval redirected. No theorem from either is used in the counterexample. A guessed Jonasson full-text URL timed out and is not evidence. The [Häggström–Jonasson–Lyons paper](https://arxiv.org/abs/math/0008191) on isoperimetric constants and random-cluster transitions was retrieved as text; it concerns infinite-graph phase transitions rather than the finite-graph local limit used here.
12. **Can–van der Hofstad (2025)**, [*Random cluster models on random graphs*](https://arxiv.org/abs/2503.17636). **Theorem 1.11, p. 9**, gives regular-graph real-q≥2 pressure; **Theorem 1.12 and Corollary 1.15, p. 10**, concern the critical curve and the Potts Bethe identity. This explains the updated BDS proposition in its final version.
13. **Du–Zhou (2025)**, [*Characterizing the limiting critical Potts measures on locally regular-tree-like expander graphs*](https://arxiv.org/abs/2505.24283). **Theorems 1.4–1.6, p. 4**, as qualified above. It is a preprint in this audit and is not used to fill an unstated zero-field critical hypothesis.
14. **Borbényi (2025 talk)**, [*Random cluster model on locally tree-like regular graphs*](https://bencsf.github.io/cap2025slides/Borbenyi_PFW2503.pdf), saved as text only. Slides 16–17 announce a general local-structure result for q>2, with exponential concentration of local statistics, labeled “BBCs ’25+.” The title slide says ongoing work. The [author's research page](https://www.renyi.hu/~borbenyi/research.html), checked November 2026, lists related 2025–2026 talks including 1≤q≤2, but no new corresponding paper in its publication list. This does not establish absence of a paper elsewhere.
15. **Blanca–Gheissari–Park–Zhang (2026)**, [*Uniqueness and Mixing in the Low-Temperature Random-Cluster Model on Trees and Random Graphs*](https://arxiv.org/abs/2604.20693). **Theorems 1.1–1.3, p. 4**, concern a second wired-specification uniqueness threshold and low-temperature mixing. They do not assert equality with the free weak limit. Searches also found the 2020 sampling-in-uniqueness work, Blanca–Gheissari's 2021 tree-uniqueness mixing result, Galanis–Goldberg–Smolarova's 2023/2025 sampling paper, and the 2026 STACS *Planting and MCMC Sampling from the Potts Model*. These algorithmic leads are not needed after the decisive local-law theorem.

**Checks and artifacts.** [code/verify_witness.py](code/verify_witness.py) checks both BP fixed points, densities and the pressure ratio using exact fractions. It independently checks wired density by summing all nine endpoint-color weights and the pressure difference through direct logarithms. [data/witness_verification.json](data/witness_verification.json) records the results. The pressure gap is approximately 0.0003391210113723 per vertex, and the edge-density gap is 12/301, approximately 0.0398671. The exact ratio establishes the pressure sign; the small floating-point gap is not load-bearing. Monotone BP iteration agrees with the exact maximal root and serves only as an audit.

The decisive theorem was checked against the version of record, v3, and the older v2 to expose the assumption change. The zero-field FK convention and uniform-root convergence match the question. The graph construction proves its own girth bound and does not confuse a root-centered tree-ball limit with a uniform-root local limit.

All saved source files are UTF-8 text. [code/fetch_text.py](code/fetch_text.py) downloads PDF responses into memory and writes only extracted text, with URL, retrieval time and response hash. No PDF, scan or page image was written. Extraction occasionally reports rotated material or garbles mathematical typography; pivotal statements were compared with publisher/arXiv text and the necessary formulas were rederived above. The manifest is [data/source_manifest.json](data/source_manifest.json). No Monte Carlo data are claimed. No heavy graph construction, subagents, publication or pushes occurred. Shell processes inherited nice 10, as recorded by the verification program; numerical thread settings were fixed to one and at most four lightweight source fetches/extractions ran concurrently.

Task: “Open problem C0153.” Received November 13, 2026, approximately 10:34 +04 (Asia/Tbilisi).
