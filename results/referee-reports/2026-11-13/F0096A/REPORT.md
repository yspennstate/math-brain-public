PARTIAL

# Hamiltonicity of \(G_{n,m;3}\)

No new fixed interval of Hamiltonicity is proved here, and no counterexample to the conjecture is obtained. The results below establish an exact sampling identity, exact moment formulas, and an exponential second-moment obstruction for the **unweighted** Hamilton-cycle count. The obstruction holds for typical fixed degree sequences at every fixed \(c>3/2\), including after conditioning on simplicity. It explains why a direct extension of the cubic small-subgraph-conditioning calculation does not give the requested interval. No novelty is claimed for the qualitative failure of the second-moment method in irregular graphs.

Statements with \(m=cn\) concern admissible integers, or \(m=\lfloor cn\rfloor\). The cubic endpoint uses even \(n\). The existence of \(L_c\) is not assumed outside the ranges where convergence is known.

## 1. Literature through 13 November 2026

The best result located for the precise model in the question is Michael Anastos and Alan Frieze, *Hamilton cycles in random graphs with minimum degree at least 3: An improved analysis*, **Random Structures & Algorithms 57(4) (2020), 865–878**, [DOI 10.1002/rsa.20978](https://doi.org/10.1002/rsa.20978), [arXiv:1906.01433](https://arxiv.org/abs/1906.01433). Theorem 1.1 states its sufficient condition as \(c>2.662\ldots\). It is unconditional.

The precise expansion threshold invoked in §2.3 is defined in Alan Frieze and Boris Pittel, *On a sparse random graph with minimum degree three: Likely Pósa sets are large*, **Journal of Combinatorics 4(2) (2013), 123–156**, Theorem 1.1, [author PDF](https://www.math.cmu.edu/~af1p/Texfiles/Posa.pdf). Put
\[
 f_j(x)=\sum_{r\ge j}\frac{x^r}{r!},\qquad
 x_*^3 f_1(x_*)=f_2(x_*)^2,\qquad
 c_*=\frac{x_*f_2(x_*)}{2f_3(x_*)}.
\]
The relevant positive root and threshold are
\[
 x_*=4.789767955881252\ldots,\qquad
 c_*=2.661565207802424\ldots.
\]
The defining equation and strict condition \(c>c_*\) specify the threshold in the expansion theorem. Anastos–Frieze identifies its bound with this one; its other path-cover estimate, Lemma 5.2, applies for all fixed \(c>3/2\). Thus \(c>c_*\) is the threshold supplied by combining these printed arguments; \(c\ge2.662\) is a conservative numerical sufficient condition. No assertion is made at \(c=c_*\). This identification comes from the proof's parameters, rather than a new improvement of its bound. The decimals were checked by root finding and independent bisection at 70-digit precision. The published Frieze–Pittel PDF and the author versions are archived in sources/.

| Source | Proved range or model | Consequence here |
|---|---|---|
| Robinson–Wormald, *Almost all cubic graphs are Hamiltonian*, RSA **3 (1992), 117–125**, [DOI](https://doi.org/10.1002/rsa.3240030202) | Uniform simple cubic graphs | \(c=3/2\). The cubic theorem is from 1992; the 1984 paper gave a positive lower bound, and the 1994 paper covers other fixed regular degrees. |
| Frieze, *On a greedy 2-matching algorithm and Hamilton cycles in random graphs with minimum degree at least three*, RSA **45(3) (2014), 443–497**, [DOI](https://doi.org/10.1002/rsa.20482) | \(G_{n,cn;3}\), \(c\ge10\) | First published online in December 2012. |
| Anastos–Frieze (2020), above | \(G_{n,cn;3}\), bound described above | Best general constant located. |
| Krivelevich–Lubetzky–Sudakov, *Cores of random graphs are born Hamiltonian*, PLMS **109 (2014), 161–188**, [arXiv:1303.3524](https://arxiv.org/abs/1303.3524) | Nonempty \(k\)-cores from birth, \(k\ge15\) | Does not include the 3-core. |
| Anastos, *Packing Hamilton Cycles in Cores of Random Graphs*, [arXiv:2107.03527](https://arxiv.org/abs/2107.03527), downloaded manuscript dated 27 November 2024 | Main Theorems 1.2–1.3 require \(k\ge4\): \(G_{n,cn;4}\) is Hamiltonian for fixed \(c>2\), and the 4-core is Hamiltonian from birth | Does not settle the minimum-degree-three window. The author's publication list lists it as a manuscript. |
| Nenadov–Steger–Trujić, *Resilience of Perfect Matchings and Hamiltonicity in Random Graph Processes*, [arXiv:1710.00799](https://arxiv.org/abs/1710.00799) | Hamiltonicity and resilience of the 2-core at \(m\ge(1/6+o(1))n\log n\) | Density grows with \(n\); this does not address fixed \(c\). |
| Cooper–Frieze, *Edge disjoint Hamilton cycles in random digraphs of constant minimum degree*, 13 April 2026, [arXiv:2604.11633](https://arxiv.org/abs/2604.11633), [author PDF](https://www.math.cmu.edu/~af1p/Texfiles/Dham%2Bk.pdf) | Directed model at sufficiently large constant density | Its introduction still states the undirected conjecture and cites the Anastos–Frieze bound. |

Seven complete arXiv API searches are saved in sources/arxiv_*.xml, with titles and abstracts in sources/arxiv_index.json: minimum-degree/Hamilton (172 records), “minimum degree three”/Hamilton (2), “minimum degree at least 3”/Hamilton (1), 2-core or 3-core/Hamilton (1), cores/Hamilton (111), Anastos/Hamilton (13), and k-core/Hamilton (3). The Anastos and Frieze publication lists were also checked. No later paper settling the full conjecture or lowering the constant for this precise model was located. This is a search conclusion, not a guarantee of bibliographic completeness.

The remaining fixed-density window is \(3/2<c\le c_*\), with the cubic endpoint settled. A theorem for minimum degree four, or for a 2-core at logarithmic density, does not fill that window.

## 2. Sampling and simulations

**Proposition 2.1 (sampling identity).** Let \(D_1,\ldots,D_n\) be independent with
\[
 \Pr(D_i=j)=\frac{\lambda^j}{j!f_3(\lambda)},\quad j\ge3.
\]
Condition on \(\sum_iD_i=2m\), take a uniform configuration pairing, and condition the entire experiment on simplicity. The graph has exactly the law \(G_{n,m;3}\). Any \(\lambda>0\) gives the same conditioned law. Choosing \(\lambda f_2(\lambda)/f_3(\lambda)=2m/n\) improves rejection efficiency. At \(2m=3n\), take every degree equal to 3.

*Proof.* On the fixed-sum event a degree sequence \(d\) has mass \(K/\prod_i d_i!\), where \(K\) is independent of \(d\). There are \((2m-1)!!\) pairings, and a fixed simple graph with degrees \(d\) has \(\prod_i d_i!\) pairing realizations. Its mass is therefore \(K/(2m-1)!!\), independent of the graph. Conditioning on simplicity gives uniformity. ∎

The implementation redraws the degree sequence after **every rejected pairing**. Keeping a sequence fixed until a simple pairing appears would change the distribution of degree sequences.

Conditioning on the exact sum is also essential. Independent truncated-Poisson degrees without that conditioning are not contiguous to a model with exactly \(m\) edges: the event that the stub sum differs from \(2m\) has probability tending to one under the former and zero under the latter. Proposition 2.1 is an exact reduction with both conditionings specified.

The C++ sampler in code/sim.cpp generates multinomial degree counts, rejects the wrong total, uniformly permutes the accepted degrees, and pairs shuffled stubs. Its Pósa heuristic stores the path in an implicit treap, permitting suffix reversals in logarithmic time. It extends either endpoint, opens a closed nonspanning cycle at an edge to an unused vertex, and searches for closure of a spanning path. Limits are \(200n\) iterations or 30 seconds per graph. The independent Python program code/verify.py checks the saved graph and every edge of each saved cycle.

The ideal-arithmetic sampler is exact. Its implementation uses floating-point binomial probabilities and degrees 3 through 255. For \(c\le2.5\), \(\lambda\le5\), and
\[
 \Pr(D\ge256)\le
 \frac{6\,5^{253}}{256!}\frac1{1-5/257}<5\cdot10^{-330}.
\]
The probability lost before conditioning is at most \(10^5\) times this bound at the largest size. Floating-point arithmetic is a separate numerical limitation; the statistical check below does not establish machine-level exact uniformity.

There are ten independent samples per cell. Seeds, rejection counts, runtimes and artifact paths are in data/sweep.csv.

| $c$ | $n=1000$ | $n=10000$ | $n=100000$ | Mean solve time at $n=100000$ (s) | Largest observed degree |
|---:|---:|---:|---:|---:|---:|
| 1.50 | 10/10 (1.00) | 10/10 (1.00) | 10/10 (1.00) | 1.867 | 3 |
| 1.55 | 10/10 (1.00) | 10/10 (1.00) | 10/10 (1.00) | 2.217 | 8 |
| 1.60 | 10/10 (1.00) | 10/10 (1.00) | 10/10 (1.00) | 2.061 | 9 |
| 1.75 | 10/10 (1.00) | 10/10 (1.00) | 10/10 (1.00) | 1.849 | 11 |
| 2.00 | 10/10 (1.00) | 10/10 (1.00) | 10/10 (1.00) | 1.984 | 14 |
| 2.25 | 10/10 (1.00) | 10/10 (1.00) | 10/10 (1.00) | 2.077 | 16 |
| 2.50 | 10/10 (1.00) | 10/10 (1.00) | 10/10 (1.00) | 1.529 | 17 |

All 210 cycles passed independent verification. There were no heuristic failures, disconnected samples, bridges, articulation vertices, or degree-3 triples sharing an identical neighborhood. No failure structure was therefore observed. Ten samples per cell provide modest finite-size evidence: even 10/10 successes give only a 0.741 one-sided 95% lower confidence bound on that finite-size success probability, with no simultaneous coverage claim. They do not establish an asymptotic limit.

The serial sweep took 520.9 seconds. Maximum simulator RSS was 61.8 MiB; the independent verifier used 148.9 MiB. Both are well below 4 GB. The longest solver run took 3.157 seconds; sample-generation time is recorded separately and increases substantially with density.

Unsuccessful heuristic runs would be reported as unresolved, not as non-Hamiltonian graphs. Structural checks include components, bridges, articulation vertices, and triples of degree-3 vertices with identical neighborhoods.

As a distributional check, all 537 eligible simple labeled graphs for \(n=6,m=10\) were enumerated. A separate 20,000-sample configuration experiment gave Pearson statistic 496.3234 on 536 degrees of freedom (\(p=0.8893\)); direct \(G(6,10)\) rejection sampling gave 554.5879 (\(p=0.2804\)). Full frequencies are in data/sampler_check.json; code is code/sampler_check.py. These tests support, but do not replace, Proposition 2.1.

## 3. Exact moments for a fixed degree sequence

Let \(d=(d_1,\ldots,d_n)\), \(d_i\ge3\), \(D=\sum_i d_i\) even, and let \(P_d\) be the uniform pairing law. Count Hamilton cycles with their actual stub-pair edges: choices among parallel edges are distinct. On simple graphs this is the ordinary count \(H\). Define
\[
 q_D(t)=\prod_{j=0}^{t-1}(D-2j-1)^{-1}
\]
for \(2t\le D\), and \(q_D(t)=0\) otherwise.

**Proposition 3.1 (finite moments).** For \(n\ge3\),
\[
 \mathbb E_dH=\frac{(n-1)!}{2}\prod_{v=1}^n(d_v)_2\,q_D(n).                 \tag{3.1}
\]
Let \(\mathcal C_n\) be the unoriented Hamilton cycles of \(K_n\). For \(C,C'\in\mathcal C_n\) and \(A\subseteq E(C)\cap E(C')\), let \(a_v\) be the number of edges of \(A\) incident to \(v\). Then
\[
 \mathbb E_dH^2=
 \sum_{C,C'\in\mathcal C_n}
 \sum_{A\subseteq E(C)\cap E(C')}
 q_D(2n-|A|)\prod_v(d_v)_{4-a_v}.                                       \tag{3.2}
\]
Here \((b)_t=0\) for \(t>b\).

*Proof.* An unoriented cyclic ordering has \((n-1)!/2\) possibilities. Assign its two distinct incident stubs at \(v\) in \((d_v)_2\) ways. The \(n\) resulting prescribed pairs occur with probability \(q_D(n)\), proving (3.1).

For an ordered pair of realized cycles, \(A\) is exactly the set of shared stub-pair edges. Only edges of both underlying vertex cycles can belong to \(A\). Their union uses \(4-a_v\) distinct stubs at \(v\), assignable in \((d_v)_{4-a_v}\) ways. A common vertex edge outside \(A\) uses different stubs in the two cycles, so represents parallel edges. The falling factorial enforces that distinction. There are \(2n-|A|\) prescribed pairs in the union, with probability \(q_D(2n-|A|)\). Every ordered pair is counted once. ∎

The formulas were checked against enumeration of **all** pairings with rational arithmetic in code/moments.py:

| Degrees | Pairings | \(\mathbb EH\) | \(\mathbb EH^2\) |
|---|---:|---:|---:|
| \(3,3,3,3\) | 10,395 | \(432/385\) | \(144/35\) |
| \(3,3,4,4\) | 135,135 | \(1728/1001\) | \(39744/5005\) |
| \(4,4,4\) | 10,395 | \(192/77\) | \(5312/385\) |

**Corollary 3.2 (first-moment rate).** If \(D/n\to\mu>2\) and \(n^{-1}\sum_v\log(d_v(d_v-1))\to b\), then
\[
 \frac1n\log\mathbb E_dH\longrightarrow
 b+\frac{(\mu-2)\log(\mu-2)-\mu\log\mu}{2}.                              \tag{3.3}
\]

*Proof.* Stirling's formula gives \(n^{-1}\log((n-1)!/2)=\log n-1+o(1)\). Also
\[
 n^{-1}\log q_D(n)=-\log n-\int_0^1\log(\mu-2t)\,dt+o(1).
\]
The integral equals \([\mu\log\mu-(\mu-2)\log(\mu-2)-2]/2\). Substitute in (3.1). ∎

## 4. An exponential second-moment obstruction

Let \(Q_d\) be the planted-cycle law: choose a uniform Hamilton stub embedding and pair all residual stubs uniformly. Each embedding has the same extension probability. Consequently
\[
 \frac{dQ_d}{dP_d}=W:=\frac{H}{\mathbb E_dH}.                            \tag{4.1}
\]

**Theorem 4.1 (separation by degree-3 edges).** Suppose \(D/n\to\mu>3\) and \(u/n\to p>0\), where \(u=|\{v:d_v=3\}|\). Put \(R=D-2n\) and
\[
 \Delta=\frac{p^2(\mu-3)^2}{\mu(\mu-2)}>0.
\]
Then
\[
 \liminf_{n\to\infty}\frac1n\log
 \frac{\mathbb E_dH^2}{(\mathbb E_dH)^2}
 \ge\frac{\Delta^2}{32\mu}>0.                                         \tag{4.2}
\]
No maximum-degree hypothesis is required.

*Proof.* Let \(S=\{v:d_v=3\}\), and let \(X\) count pairing edges within \(S\), including loops. Under \(P_d\),
\[
 a_n:=\mathbb E_{P_d}X=\frac{3u(3u-1)}{2(D-1)}.
\]
Under \(Q_d\), the Hamilton cycle contributes \(u(u-1)/(n-1)\). There is one residual stub per vertex in \(S\), so
\[
 b_n:=\mathbb E_{Q_d}X=
 \frac{u(u-1)}{n-1}+\frac{u(u-1)}{2(R-1)}.
\]
Thus \(g_n=b_n-a_n=n\Delta+o(n)\), using
\[
 1+\frac1{2(\mu-2)}-\frac9{2\mu}
 =\frac{(\mu-3)^2}{\mu(\mu-2)}.
\]

Generate a pairing by permuting its stubs uniformly and pairing consecutive positions. Transposing two positions changes \(X\) by at most 2. Under successive exposure, conditional completions for two choices of the next entry couple by one transposition. Thus every Doob martingale increment has absolute value at most 2. Azuma's inequality gives
\[
 P_d(X-a_n\ge t)\le e^{-t^2/(8D)}.
\]
For \(Q_d\), use an independent uniform vertex permutation for the Hamilton order and a uniform permutation of the \(R\) residual stubs. Residual membership in \(S\) is fixed by the degrees, independently of which stubs the Hamilton embedding chose. A transposition of Hamilton positions changes at most four edges; a residual transposition changes at most two. Applying the same argument with bound 4 for all \(n+R\) exposures gives
\[
 Q_d(X-b_n\le-t)\le e^{-t^2/(32(n+R))}.
\]
For large \(n\), \(g_n>0\). Set \(A_n=\{X\ge(a_n+b_n)/2\}\). Then
\[
 P_d(A_n)\le e^{-g_n^2/(32D)},\qquad
 Q_d(A_n)\ge1-e^{-g_n^2/(128(n+R))}.
\]
By (4.1) and Cauchy–Schwarz,
\[
 \mathbb E_dW^2\ge\frac{Q_d(A_n)^2}{P_d(A_n)}
 \ge\big(1-e^{-g_n^2/(128(n+R))}\big)^2 e^{g_n^2/(32D)}.
\]
Taking logarithms and dividing by \(n\) proves (4.2). ∎

**Corollary 4.2 (conditioning on simplicity).** If \(P_d(\mathrm{simple})\) and \(Q_d(\mathrm{simple})\) are bounded below by positive constants, (4.2) holds for moments conditional on simplicity as well.

*Proof.* The conditioned laws have density ratio \(H/\mathbb E_{P_d}[H\mid\mathrm{simple}]\). The upper tail bound under \(P_d\) increases by at most \(1/P_d(\mathrm{simple})\); the lower-tail error under \(Q_d\) increases by at most \(1/Q_d(\mathrm{simple})\). Their logarithms are \(O(1)\), so the same argument gives the same exponential rate. ∎

This separation is an obstruction for the counting variable, not a counterexample to Hamiltonicity. Even with degrees fixed, the unweighted planted law has a different macroscopic pattern of edges between degree classes.

## 5. Cycle corrections

The classical conditioning framework and regular-graph count distributions are treated in Svante Janson, *Random Regular Graphs: Asymptotic Distributions and Contiguity*, **Combinatorics, Probability and Computing 4(4) (1995), 369–405**, [DOI 10.1017/S0963548300001735](https://doi.org/10.1017/S0963548300001735). The following calculation determines the correction parameters for the present fixed irregular degrees; it does not assume that the regular-graph conditioning theorem applies.

Consider deterministic degree sequences with minimum degree 3, maximum degree \(O((\log n)^2)\), and empirical moments of every fixed order converging to those of a distribution \(p_j\). Let \(Z\) have this distribution, with mean \(\mu\). Define
\[
 \rho=\mu-2,\quad v=\operatorname{Var}Z,\quad
 \nu=\frac{\mathbb E[Z(Z-1)]}{\mu},\quad
 a=\frac{\mathbb E[(Z-2)(Z-3)]}{\rho},\quad
 M=\begin{pmatrix}1&\rho\\2&a\end{pmatrix}.
\]
Let \(X_k\) count cycles of length \(k\), with loops counted by \(X_1\) and unordered pairs of parallel edges counted by \(X_2\).

**Proposition 5.1 (mixed cycle moments).** For each fixed \(k\),
\[
 \mathbb E_{P_d}X_k\to\lambda_k=\frac{\nu^k}{2k},\qquad
 \frac{\mathbb E_{P_d}(HX_k)}{\mathbb E_{P_d}H}
 \to\lambda_k^H=\frac{\operatorname{tr}(M^k)-1}{2k}.                     \tag{5.1}
\]
For each fixed finite collection of lengths, joint factorial moments under each law converge to those of independent Poisson variables with these respective means. Thus
\[
 1+\delta_k=\frac{\operatorname{tr}(M^k)-1}{\nu^k}.                      \tag{5.2}
\]

*Proof.* In the ordinary pairing model, enumerate cyclically ordered distinct vertices, choose two ordered stubs at each vertex, prescribe their pairs and divide by \(2k\). The leading contribution is \((\sum_i(d_i)_2/D)^k/(2k)\). The diagonal terms omitted in replacing distinct-vertex sums by products are \(o(1)\), by the bounds on fixed empirical moments and maximum degree. For several vertex-disjoint cycles the same enumeration factors. Any overlapping union of distinct cycles has more edges than vertices and contributes an additional inverse power of \(n\); its fixed-order degree factors and polylogarithmic bounds make that contribution \(o(1)\). This proves the factorial-moment assertion under \(P_d\), including the loop and double-edge conventions.

Under \(Q_d\), color the Hamilton edges red and residual edges blue. The two degrees at vertex \(i\) are \(2\) and \(r_i=d_i-2\). The transition factor from color \(A\) to color \(B\) in a cyclic color sequence is
\[
 \frac{\sum_i d_{A,i}(d_{B,i}-\mathbf1_{A=B})}{\sum_i d_{A,i}},
\]
whose limit is \(M_{AB}\). Multiplying and summing closed color sequences gives \(\operatorname{tr}(M^k)/(2k)\) if the red edges are generated by a degree-2 configuration.

To pass to a uniform red Hamilton cycle, a fixed proper collection of red path components has the same leading probability in the two models. Indeed, a collection with \(\ell\) red edges and \(b\) nontrivial path components is contained in a uniform vertex Hamilton cycle with probability \(2^b(n-\ell-1)!/(n-1)!\); assigning its incident red stubs contributes \(2^{-(\ell+b)}\), giving \((2n)^{-\ell}(1+O(1/n))\), the pairing probability. The all-red \(k\)-cycle is forbidden for fixed \(k<n\); its degree-2-configuration contribution \(1/(2k)\) must be subtracted. This also removes the red loop or double edge at \(k=1,2\).

Disjoint colored cycles factor by the same path enumeration. Overlapping unions contribute \(o(1)\) by the preceding bounds, and any union containing a red cycle is forbidden. This proves the assertion for \(Q_d\). Finally \(\mathbb E(HX_k)/\mathbb EH=\mathbb E_{Q_d}X_k\) by (4.1). ∎

**Proposition 5.2 (failure of the finite correction sum).** If \(v>0\), then
\[
 \sum_{k\ge3}\lambda_k\delta_k^2=+\infty.                               \tag{5.3}
\]
For a constant degree \(d\ge3\), instead,
\[
 \delta_k=\frac{(-1)^k-1}{(d-1)^k},\qquad
 \sum_{k\ge1}\lambda_k\delta_k^2=\log\frac d{d-2}.                       \tag{5.4}
\]

*Proof.* Let \(\alpha\) and \(\beta\) be the larger and smaller eigenvalues of \(M\). Its positive off-diagonal entries and its positive first diagonal entry imply \(\alpha>|\beta|\). Direct calculation gives
\[
 a=\rho-1+v/\rho,\qquad \nu=\rho+1+v/(\rho+2),
\]
and
\[
 (\nu-1)(\nu-a)-2\rho
 =-\frac{2v^2}{\rho(\rho+2)^2}<0.
\]
Thus \(\alpha>\nu\ge2\). Consequently
\[
 \lambda_k\delta_k^2=
 \frac{(\alpha^k+\beta^k-1-\nu^k)^2}{2k\nu^k}
 \sim\frac1{2k}\left(\frac{\alpha^2}{\nu}\right)^k,
\]
whose terms tend to infinity. In the regular case the eigenvalues are \(d-1,-1\), yielding (5.4) by summing \(2/[k(d-1)^k]\) over odd \(k\). ∎

There is therefore no **finite** identity of the form
\[
 \frac{\mathbb EH^2}{(\mathbb EH)^2}
 \longrightarrow\exp\left(\sum_k\lambda_k\delta_k^2\right)
\]
required by ordinary small-subgraph conditioning at a fixed nondegenerate truncated-Poisson law. Theorem 4.1 gives a stronger exponential lower bound for the ratio itself. At cubicity, the unconditioned correction sum is \(\log3\). Removing loops and double edges removes the \(k=1\) term 1 and the \(k=2\) term 0, leaving \(\log3-1\), consistent with the classical simple-cubic second-moment ratio \(3/e\). No derivation of that classical full asymptotic from (3.2) is claimed here.

The factorial-moment calculation also gives
\[
 P_d(\mathrm{simple})\to e^{-\nu/2-\nu^2/4},\qquad
 Q_d(\mathrm{simple})\to e^{-a/2-\rho-a^2/4}>0,                          \tag{5.5}
\]
since simplicity is exactly \(X_1=X_2=0\). These formulas justify Corollary 4.2 under the stated hypotheses. The joint Poisson limits also show that (5.1) for \(k\ge3\), and hence (5.3), survive conditioning on simplicity.

## 6. High degrees and the near-cubic limit

**Proposition 6.1 (typical degrees).** Fix \(c>3/2\), and choose the positive \(\lambda\) with mean \(2c\). Independent truncated-Poisson degrees conditioned on their sum \(2cn+O(1)\) have convergent empirical moments of each fixed order and, with probability tending to one,
\[
 \max_iD_i\le\left\lceil\frac{3\log n}{\log\log n}\right\rceil.
\]
These conclusions persist after conditioning the full configuration experiment on simplicity. Theorem 4.1 and Propositions 5.1–5.2 consequently apply to typical degree sequences at every fixed \(c>3/2\).

*Proof.* The degree law has span one, positive variance \(\sigma^2\), and finite moments of all orders. Fourier inversion gives
\[
 \Pr\!\left(\sum_iD_i=2cn+O(1)\right)
 =(1+o(1))(2\pi n\sigma^2)^{-1/2}
\]
at the chosen admissible target. To justify this local estimate, its characteristic function near zero is \(e^{2cit}(1-\sigma^2t^2/2+O(|t|^3))\). Its modulus is strictly less than one away from zero in \([-\pi,\pi]\), because the support contains consecutive integers. Splitting the inversion integral into a shrinking neighborhood of zero, the remainder of a fixed small neighborhood, and its complement gives respectively the Gaussian integral, a negligible quadratic tail, and an exponentially small remainder. An \(O(1)\) displacement of the target leaves the leading term unchanged.

For each fixed empirical moment, unconditional Chebyshev bounds are \(O(n^{-1})\). Dividing by the conditioning probability gives \(O(n^{-1/2})\), proving conditional convergence. The same argument applies to the degree-3 proportion and the mean of \(\log(D_i(D_i-1))\).

The factorial tail bound is \(\Pr(D_i\ge t)\le\exp(-t\log t+O(t))\). A union bound followed by conditioning bounds the maximum-degree tail by \(O(n^{3/2})\exp(-t\log t+O(t))\). At the displayed cutoff this is \(n^{-3/2+o(1)}\). Finally (5.5), applied to sequences with the empirical moment and degree bounds just proved, gives a positive limiting probability of simplicity. Conditioning on this event preserves the high-probability conclusions. ∎

No high-degree vertices are deleted in these arguments. A growing cutoff as above is legitimate. A fixed cutoff is not a coupling that preserves the entire graph: its limiting tail is positive, so the number of vertices above it is linear in \(n\). Reinserting such vertices into a Hamilton cycle would need a separate proof.

If \(c=3/2+\varepsilon\), expansion of the defining series gives
\[
 \lambda=8\varepsilon+O(\varepsilon^2),\quad
 p_3=1-2\varepsilon+O(\varepsilon^2),\quad
 p_4=2\varepsilon+O(\varepsilon^2),\quad
 \sum_{j\ge5}p_j=O(\varepsilon^2).
\]
Therefore \(\Delta=4\varepsilon^2/3+O(\varepsilon^3)\), and the lower bound on the exponential rate in (4.2) equals \(\varepsilon^4/54+O(\varepsilon^5)\). The obstruction is present for every fixed sufficiently small positive \(\varepsilon\). Taking the cubic limit after \(n\to\infty\) does not recover a finite second-moment ratio.

The following numerical values concern the limiting degree law, not empirical Hamiltonicity. Values and the first 20 cycle corrections are saved in data/moments.json.

| \(c\) | \(\lambda\) | \(p_3\) | First-moment log rate (3.3) | \(\alpha-\nu\) | \(\Delta\) |
|---:|---:|---:|---:|---:|---:|
| 1.50 | 0 | 1 | 0.143841 | 0 | 0 |
| 1.55 | 0.377903 | 0.907366 | 0.158429 | 0.000687820 | 0.00241441 |
| 1.60 | 0.718035 | 0.827322 | 0.173404 | 0.00253319 | 0.00712980 |
| 1.75 | 1.578046 | 0.640651 | 0.220293 | 0.0120017 | 0.0195445 |
| 2.00 | 2.687999 | 0.437334 | 0.302895 | 0.0293683 | 0.0239076 |
| 2.25 | 3.576930 | 0.307690 | 0.388067 | 0.0409363 | 0.0189346 |
| 2.50 | 4.340315 | 0.219895 | 0.473462 | 0.0463745 | 0.0128944 |

A separate audit in code/planted_check.py used 100 ordinary and 100 planted pairings for each of two saved degree sequences at \(n=100000\). These configurations were not conditioned on simplicity, as required for the finite expectations in Theorem 4.1:

| \(m/n\) | Expected ordinary \(X\) | Observed mean (standard error) | Expected planted \(X\) | Observed mean (standard error) |
|---:|---:|---:|---:|---:|
| 1.55 | 119522.089 | 119525.46 (4.55) | 119763.445 | 119764.63 (4.28) |
| 1.75 | 52787.882 | 52802.46 (10.78) | 54742.764 | 54742.32 (9.15) |

These observations are archived in data/planted_check.json and are excluded from the Hamiltonicity success table.

## 7. Algorithmic bottleneck and what remains

Anastos–Frieze's Lemma 5.2 already gives a spanning path cover with at most \(2n^{0.4+2\eta}\) paths for every fixed \(c>3/2\), with their \(\eta=10^{-9}\). The edge reservoir has size \(n^{1/2-o(1)}\). The density restriction enters through expansion property P3 of Lemma 2.1, which makes the rotation endpoint sets large enough to close the paths using that reservoir. With endpoint sets of size \(n^\beta\), its sufficient budget is of order \(n^{2-2\beta}|\mathcal P|\log^2 n\). The existing cover and reservoir require \(\beta>0.95+\eta\); the paper uses \(0.99\). A sharper greedy-cover estimate alone does not remove the expansion threshold.

In the Frieze–Pittel sufficient criterion, \(x^3f_1(x)/f_2(x)^2\) must cross 1. It tends to 4 as \(x\downarrow0\), leaving a fixed gap at the cubic boundary. More precision in the root calculation cannot extend that criterion to the near-cubic window.

Theorem 4.1 suggests correcting for degree-dependent edge mixing before attempting another counting proof. One possible variable is a sum over cycles weighted by factors depending on the two endpoint degrees of each cycle edge. Weights depending only on vertex degrees cannot help: their product is constant over all Hamilton cycles. No weights, overlap saddle-point bounds, or conditioning theorem giving a positive interval are established here.

In particular, **no positive explicit \(\varepsilon_0\)** is proved. Formula (3.2) is a complete finite second-moment expression, independently checked on small instances; its full large-\(n\) asymptotic is not evaluated. Theorem 4.1 supplies an exponential lower bound instead. The desired Hamiltonicity window and any improvement of the printed expansion bound remain open in this report.

## 8. Reproduction and artifacts

Run from this folder, with single-thread BLAS settings for the Python numerical programs:

    clang++ -std=c++17 -O3 -Wall -Wextra code/sim.cpp -o code/sim
    python3 code/run_sweep.py
    OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python3 code/verify.py
    clang++ -std=c++17 -O3 -Wall -Wextra code/sim.cpp -o code/sim_check
    OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python3 code/sampler_check.py
    OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python3 code/moments.py
    OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python3 code/planted_check.py
    python3 code/literature_search.py
    python3 code/finalize.py

The sweep uses one worker and no thread pool. Its inherited nice value is 15. The sandbox denies priority changes, but this inherited value already exceeds 10. Setting a 3.5 GB address-space ceiling also failed, so no enforced ceiling is claimed. Observed resident memory and timings are in data/sweep_resources.json, data/verification_resources.json and data/planted_check.json.

Saved graphs have a native-endian int32 header \((n,m)\), followed by \(m\) int32 endpoint pairs. Files ending in .cycle contain zero-based cyclic vertex orderings. The seeds reproduce the experiment with the same C++ standard library; different standard-library implementations can generate different pseudorandom sequences. All code and data are local. There are no subagents, downloaded solver binaries, or external writes.

Four pilot graphs have names beginning with pilot_ and are excluded from the 210-sample sweep table. The artifact checksum list is data/SHA256SUMS.json. The experimental environment is recorded in data/environment.txt.

Task: “Open problem F0096: Hamiltonicity of G_{n,cn;3} for c >= 3/2”, received 13 November 2026, approximately 03:41 Asia/Tbilisi.
