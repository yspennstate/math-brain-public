PARTIAL

# E0086: source audit and annulus local times

For the separate annulus maximum requested in the prompt, this report proves

\[
 \frac{\max_{n^\alpha<|x|\le2n^\alpha}K(\tau_n,x)}{(\log n)^2}
 \xrightarrow{\mathbb P}\frac{4\alpha^2}{\pi},\qquad 0<\alpha<1.
 \tag{A}
\]

The proof uses the established DPRZ global thick-point theorem for its lower bound and an explicit excursion/Green-function argument for its upper bound. It works for both the source's stopping time and exterior exit. No novelty claim is made. Almost sure convergence is not proved here. For the annulus covered-disc question, a lower bound and a weaker upper bound are proved; the matching exponent is a heuristic.

The cited paper asks a different question: a maximum over a generalized boundary of the walk's range. It also contains incompatible time parameters in its displayed conjecture. Read literally, that display is false. The intended moving-pattern problem is not resolved here, which is why this report is PARTIAL.

## 1. Exact source and interpretation

[arXiv:1606.03787](https://arxiv.org/abs/1606.03787) is by **Izumi Okada**, not Hu and Shi. Sections 1–2 and Open problem 2 were read in full. The complete text is [sources/okada_2016_1606.03787.txt](sources/okada_2016_1606.03787.txt). PDF page numbers below count the first page as page 1.

The definitions on PDF pp. 2–4 are

\[
 D(x,r)=\{y\in\mathbb Z^2:|y-x|\le r\},\quad
 K(t,x)=\sum_{j=0}^t\mathbf1_{\{S_j=x\}},\quad
 \tau_n=\inf\{j\ge0:S_j\in\partial D(0,n)\},
\]

where the boundary is the **inner vertex boundary**. Thus the stopping parameter is a radius. Also

\[
 R(t)=\{S_0,\ldots,S_t\},\quad
 \partial_H R(t)=\{x\in R(t):x+H\subset R(t)^c\},\quad
 M_H(t)=\max_{x\in\partial_H R(t)}K(t,x).
 \tag{1}
\]

The admissible class \(\mathcal H(M)\), for fixed \(M\), requires

\[
 0\notin H,\quad |H|\le M,\quad
 \mathbb P(T_x<T_H)>0\quad\forall x\in H^c,
 \qquad T_A=\inf\{j\ge1:S_j\in A\}.
\]

Open problem 2, PDF p. 6, concerns patterns \(\widetilde D_n\in\mathcal H\) outside radius \(a_n\to\infty\), especially patterns contained between radii \(a_n\) and \(2a_n\), with \(a_n=n^\beta\), \(0<\beta<1/2\). The annulus contains the **forbidden offsets**, not the sites over which local time is maximized. A full annulus has unbounded cardinality and surrounds the origin, so is not an admissible pattern.

The conjectured display on that page is

\[
 M_{\widetilde D_n}(n)=\max_xK(\tau_n,x)
 \quad\text{eventually a.s.},\qquad a_n\ge n^{1/2+\varepsilon}.
 \tag{2}
\]

The left side still uses deterministic time \(n\) from (1). The covered-disc citation is source reference [7], **Dembo–Peres–Rosen (2007)**, distinct from DPRZ's 2004 torus cover-time result.

### The printed time mismatch is a contradiction

Let \(L^*(t)=\max_xK(t,x)\). Always \(M_H(n)\le L^*(n)\). DPRZ (2001), Theorem 1.1, p. 240, gives

\[
 L^*(n)/\log^2n\to1/\pi\quad\text{a.s.}
\]

Section 4 below verifies that \(L^*(\tau_n)/\log^2n\to4/\pi\) a.s. Consequently (2) is eventually impossible, for every pattern with a defined maximum.

An explicit admissible example is \(a_n=n\), \(H_n=\{(2n,0)\}\). No nearest-neighbor path of length \(n\) contains two points separated by \(2n\), so \(\partial_{H_n}R(n)=R(n)\). A singleton does not surround zero, hence belongs to \(\mathcal H(1)\). It also lies in the specified annulus and satisfies the large-offset hypothesis, for example with \(\varepsilon=1/4\).

Two possible repairs are to change the left side to time \(\tau_n\), or to change the right side to time \(n\). They are different questions, and neither repair is attributed to the author here. The latter repair at \(a_n\ge n^{1/2+\varepsilon}\) is elementary: the range diameter is \(n^{1/2+o(1)}\) a.s., so eventually all translated forbidden offsets are absent from the range. The former repair remains unproved in this report.

## 2. Literature first: findings and limits

The search began with the source, its references, and all requested titles/authors, followed by exact-ID citation searches, resolution searches, and searches for subset/annulus maxima. A relevant October 2026 preprint was found in the final search and checked before completion. See [sources/SEARCH_NOTES.md](sources/SEARCH_NOTES.md) for search scope and gaps, and [sources/manifest.json](sources/manifest.json) for source URLs, access times and hashes.

No exact theorem resolving the consistently timed moving-pattern problem was located. This is a bounded search, not a certification that no resolution exists. A complete citation census was not available. RESOLVED_IN_LITERATURE would therefore be unjustified.

| Work | Exact location checked | What it gives; limitation |
|---|---|---|
| Dembo–Peres–Rosen–Zeitouni, *Thick points for planar Brownian motion and the Erdős–Taylor conjecture on random walk*, Acta Math. **186** (2001), 239–270 | Theorem 1.1, p. 240/PDF p. 2; Theorem 5.1, p. 252/PDF p. 14 and its proof | Global local-time constant and thick-point counts. Input to (A), not a moving-pattern theorem. [Author source](https://www.math.csi.cuny.edu/~rosen/64-erdos-taylor.pdf). |
| DPRZ, *Cover times for Brownian motion and random walks in two dimensions*, Ann. Math. **160** (2004), 433–464 | Theorem 1.1, p. 434/PDF p. 2; Theorem 1.4, p. 436/PDF p. 4 | Torus cover constant \(4/\pi\); fixed-center planar disc cover law \(\mathbb P(\log C_r\le t\log^2r)\to e^{-4/t}\). [Journal source](https://annals.math.princeton.edu/wp-content/uploads/annals-v160-n2-p02.pdf). |
| DPRZ, *Late points for random walks in two dimensions*, Ann. Probab. **34** (2006), 219–263 | Theorems 1.1–1.4, arXiv PDF pp. 2–3 | Torus late-point counts/clustering; Theorem 1.2 includes a deterministic small-disc exponent. Different time scale and quantity. [arXiv:math/0303102](https://arxiv.org/abs/math/0303102). |
| **Dembo–Peres–Rosen**, *How large a disc is covered by a random walk in n steps?*, Ann. Probab. **35** (2007), 577–601 | Theorem 1.1, p. 578/PDF p. 2, equations (1.2)–(1.3); Theorem 1.2, same page; excursion discussion pp. 580–581 | Largest freely centered covered radius \(t^{1/4+o(1)}\) at time \(t\), \(r^{1/2+o(1)}\) before exit radius \(r\). Correct coverage input below. [Author source](https://www.math.csi.cuny.edu/~rosen/82-large-disc.pdf). |
| Rosen, *A random walk proof of the Erdős–Taylor conjecture*, Period. Math. Hungar. **50** (2005), 223–245 | Theorems 1.1–1.2, arXiv PDF pp. 1–2; Lemma 2.1, p. 3; successful-point construction, Lemma 3.2 | Direct excursion-counting proof. ArXiv v1 display (1.7), PDF p. 2, has a factor-two inconsistency with (1.1), (1.6), and its Green constant; do not use it to normalize the exit maximum. [arXiv:math/0503108](https://arxiv.org/abs/math/0503108). |
| Bass–Rosen, *Frequent points for random walks in two dimensions*, Electron. J. Probab. **12** (2007), paper 1, 1–46 | Theorems 1.1–1.2, arXiv PDF pp. 2–3; Green/Harnack tools | Global theory for symmetric unbounded-jump walks under hypotheses. [arXiv:math/0607636](https://arxiv.org/abs/math/0607636). |
| Csáki–Földes–Révész, *Maximal local time of a d-dimensional simple random walk on subsets*, J. Theor. Probab. **18** (2005), 687–717 | Theorem 1.2, author PDF p. 5 | For a ball of radius \(t^\beta\), \(0<\beta\le1/2\), at deterministic time \(t\), a.s. lower/upper constants \(4\beta^2/\pi\), \(2\beta/\pi\). These are bounds, not equality. [Author source](https://www.math.csi.cuny.edu/~foldes/pdf/Maximallocal.pdf). |
| Jego, *Thick points of random walk and the Gaussian free field*, Electron. J. Probab. **25** (2020), paper 32, 1–39 | Theorem 1.1.1, arXiv PDF p. 3; Theorem 3.1.1 | Global thick-point laws with finite second moments; different from the moving-pattern question. [arXiv:1809.04369](https://arxiv.org/abs/1809.04369). |
| Jego, *Planar Brownian motion and Gaussian multiplicative chaos*, Ann. Probab. **48** (2020), 1597–1643 | Theorems 1.1–1.2, arXiv PDF p. 3 | Subcritical Brownian thick-point measures. [arXiv:1812.01903](https://arxiv.org/abs/1812.01903). |
| Abe, *Second order term of cover time for planar simple random walk* | Theorem 1.1, arXiv v3 PDF p. 2 | Discrete-torus second-order cover time. [arXiv:1709.08151](https://arxiv.org/abs/1709.08151). |
| Belius–Kistler, *The subleading order of two dimensional cover times*, PTRF **167** (2017), 461–552 | arXiv v1 equation (1.2), PDF p. 1; proof overview pp. 2–4 | Brownian torus cover-time correction and traversal barriers. [arXiv:1405.0888](https://arxiv.org/abs/1405.0888). |
| Belius–Rosen–Zeitouni, *Tightness for the cover time of the two dimensional sphere* | Theorem 1.1, arXiv PDF p. 2 | Centered square-root Brownian sphere cover time. [arXiv:1711.02845](https://arxiv.org/abs/1711.02845). |
| Okada, *Frequently visited sites of the inner boundary of simple random walk range*, SPA **126** (2016), 1412–1432 | Theorems 2.1–2.2, arXiv PDF p. 3 | Ordinary inner-boundary maximum is order \(\log t\); the base result for the source's extension. [arXiv:1409.8368](https://arxiv.org/abs/1409.8368). |
| Okada, *Exponents for the number of pairs of α-favorite points of a simple random walk in Z²*, SPA **130** (2020), 108–138 | Theorems 2.1–2.2, arXiv PDF pp. 2–3 | Pair-count exponents. [arXiv:1602.05641](https://arxiv.org/abs/1602.05641). |
| Okada, *Geometric structures of late points of a two-dimensional simple random walk*, Ann. Probab. **47** (2019), 2869–2893 | Theorem 2.1, arXiv PDF p. 2 | Expected late-point tuple counts. [arXiv:1605.01158](https://arxiv.org/abs/1605.01158). |
| Okada, *Exponent for sets of frequently visited points of a simple random walk in two dimensions*, ALEA **16** (2019), 1129–1140 | Theorem 1.1, p. 1130/PDF p. 2 | Expected favorite-tuple counts. [Journal source](https://alea.math.cnrs.fr/articles/v16/16-42.pdf). |
| Comets–Popov–Vachkovskaia, *Two-dimensional random interlacements and late points for random walks*, CMP **343** (2016), 129–164 | Theorem 2.6, arXiv PDF p. 15; equation (6), p. 5 | Local vacant-set limit conditional on an avoided point at torus cover-time scale; not the desired maximum. [arXiv:1502.03470](https://arxiv.org/abs/1502.03470). |
| Hao–Li–Okada–Zheng, *Favorite sites for simple random walk in two and more dimensions*, PTRF **195** (2026), 1765–1822 | Theorems 1.1–1.2, arXiv v2 PDF p. 2 | Number of simultaneous favorite sites; a different resolved problem. [arXiv:2409.00995](https://arxiv.org/abs/2409.00995). |
| Collin–Popov, *Deviation probabilities for global events in two dimensions (I): independent excursions*, October 2026 preprint | Theorem 2.3, PDF p. 10; equation (19), p. 12; Corollary 3.10, p. 23 | For \(2\theta\log^2r\) stationary independent excursions: covered-radius exponent \((1+\sqrt\theta)/2\), maximum constant \((4/\pi)(1+\sqrt\theta)^2\). Supports the heuristic, but its model differs. [arXiv:2610.26640](https://arxiv.org/abs/2610.26640). |

The potential-kernel input is Lawler–Limic, Theorem 4.4.4, and the killed-Green identity is Proposition 4.6.2(b), equation (4.28). In the [author-hosted book draft](https://www.math.uchicago.edu/~lawler/srwbook.pdf) saved here these occur on PDF/printed pp. 88 and 97. Published-book pagination differs.

## 3. Precise annulus statements and the three regimes

Let

\[
 T_n=\inf\{j\ge0:|S_j|>n\},\quad
 A_n(\alpha)=\{x:n^\alpha<|x|\le2n^\alpha\},\quad
 Q_n(\alpha)=\max_{x\in A_n(\alpha)}K(T_n,x).
\]

For fixed \(0<\alpha<1\), the exit site is outside this annulus eventually, so including it does not change \(Q_n\). Define

\[
 C_n(\alpha)=\sup\{r\ge0:\exists z\in\mathbb Z^2,
 D(z,r)\subset A_n(\alpha)\cap R(T_n)\}.
\]

Set \(C_n=0\) if no positive-radius disc qualifies. A supremum avoids the issue that an optimal real radius of a closed lattice disc need not be attained.

**Theorem A.** For every fixed \(0<\alpha<1\),

\[
 Q_n(\alpha)/\log^2n\xrightarrow{\mathbb P}4\alpha^2/\pi.
\]

The same holds with \(T_n\) replaced by Okada's \(\tau_n\).

**Theorem B.** For these \(\alpha\) and every \(\eta>0\),

\[
 \mathbb P\{C_n(\alpha)\ge n^{\alpha/2-\eta}\}\to1,
 \qquad C_n(\alpha)\le n^{\min(\alpha,1/2)+o(1)}\quad\text{a.s.}
 \tag{B}
\]

These bounds also hold for \(\tau_n\). The matching prediction

\[
 \log(C_n(\alpha)\vee1)/\log n\xrightarrow{\mathbb P}\alpha/2
 \tag{C, heuristic here}
\]

is not proved.

| Scale | Proven local-time constant, in probability | Predicted covered-radius exponent | Upper exponent proved here |
|---|---:|---:|---:|
| \(0<\alpha<1/2\) | \(4\alpha^2/\pi\) | \(\alpha/2\) | \(\alpha\) |
| \(\alpha=1/2\) | \(1/\pi\) | \(1/4\) | \(1/2\) |
| \(1/2<\alpha<1\) | \(4\alpha^2/\pi\) | \(\alpha/2\) | \(1/2\) |

There is no transition at \(\alpha=1/2\) for this annulus local-time statistic. Indeed

\[
 Q_n(\alpha)/L^*(T_n)\xrightarrow{\mathbb P}\alpha^2<1.
\]

Thus any reinterpretation asserting eventual equality of the **annulus-site maximum** and the global maximum for \(1/2<\alpha<1\) is false. This does not disprove a consistently timed version of the different boundary-pattern conjecture. For \(\alpha\ge1\), the annulus is unvisited before exit; when the exterior exit point is counted, its maximum is at most one, and is exactly one for \(\alpha=1\).

For an arbitrary \(D_n\subset D(0,a_n)^c\), there is no universal asymptotic: it can be unreachable, can be a singleton, or can contain the whole annulus. For a singleton \(|x_n|\asymp n^\alpha\), the Green estimate below gives \(\mathbb EK(T_n,x_n)=O(\log n)\), so its maximum divided by \(\log^2n\) tends to zero in probability by Markov's inequality.

## 4. Complete derivation of the partial results

### 4.1 Established inputs and radius/time conversion

The deep local-time input is DPRZ Theorem 1.1:

\[
 L^*(t)/\log^2t\to1/\pi\quad\text{a.s.}
 \tag{3}
\]

The coverage input is DPR (2007), Theorem 1.1. These are established theorems, not new proofs claimed here. All additional steps are supplied below.

First,

\[
 \log T_r/\log r\to2\quad\text{a.s.}
 \tag{4}
\]

The martingale \(|S_j|^2-j\), stopped at \(T_r\wedge m\), gives \(\mathbb E(T_r\wedge m)\le(r+1)^2\). Monotone convergence and Markov imply

\[
 \mathbb P(T_r>r^{2+\delta})\le Cr^{-\delta}.
\]

The exponential maximal inequality for both signs of both coordinate martingales, whose increments are bounded by one, gives

\[
 \mathbb P\{\max_{j\le m}|S_j|>r\}\le4e^{-cr^2/m}.
\]

With \(m=\lfloor r^{2-\delta}\rfloor\), the lower exit-time tail is at most \(4e^{-cr^\delta}\). Both bounds are summable for \(r=2^k\). Borel–Cantelli and monotonicity interpolate between dyadic radii, giving (4) after rational \(\delta\downarrow0\). The same maximal inequality on dyadic times gives \(\max_{j\le t}|S_j|\le t^{1/2+\delta}\) eventually a.s.

Combining (3) and (4) yields

\[
 \frac{L^*(T_r)}{\log^2r}
 =\frac{L^*(T_r)}{\log^2T_r}
   \left(\frac{\log T_r}{\log r}\right)^2\to4/\pi\quad\text{a.s.}
 \tag{5}
\]

For the source stopping time, \(T_{r-2}\le\tau_r\le T_r\): inner-boundary vertices have norm greater than \(r-1\), and the walk must hit the boundary before exiting. Thus (4)–(5) also hold for \(\tau_r\). This checks the factor four independently of the source's display.

### 4.2 Green estimates at the annulus scale

Put \(a=n^\alpha\), \(g=2/\pi\), \(B=D(0,4a)\), and

\[
 G_B(z,x)=\mathbb E_z\sum_{j<T_{4a}}\mathbf1_{\{S_j=x\}}.
\]

The potential kernel \(b\), normalized by \(b(0)=0\), obeys

\[
 b(v)=g\log|v|+c_0+O(|v|^{-2}),\qquad
 G_B(z,x)=\mathbb E_zb(S_{T_{4a}}-x)-b(z-x).
 \tag{6}
\]

For \(a<|x|\le2a\), its distances from exit points of \(B\) lie between \(2a\) and \(6a+1\). Therefore

\[
 G_B(x,x)=g\log a+O(1)\quad\text{uniformly}.
 \tag{7}
\]

For \(z=0\), \(|z-x|\ge a\); for \(3a-1\le|z|\le3a\), \(|z-x|\ge a-1\). The two logarithms in (6) then differ by a bounded amount. Positivity gives

\[
 0\le G_B(z,x)\le C
 \tag{8}
\]

uniformly for these starting points and annulus points.

In the large killed disc the same identity instead gives

\[
 G_{D(0,n)}(x,x)=g\log n+O(1),\qquad
 G_{D(0,n)}(0,x)=g\log(n/|x|)+O(1)
 =g(1-\alpha)\log n+O(1).
 \tag{9}
\]

Here \(|x|/n\to0\), so all exit distances from \(x\) are \(n(1+o(1))\). The diagonal is not \(g\log(n/a)\); the \((1-\alpha)\) factor belongs to the off-diagonal function from the origin. The probability to reach \(x\) is their ratio, tending to \(1-\alpha\).

### 4.3 Exact exponential moment for one episode

For a finite killed domain, let \(L_x\) be local time, \(G=G_B(x,x)\) and \(h=G_B(z,x)/G\). Strong Markov at the first visit and successive returns shows that \(\mathbb P_z(L_x=0)=1-h\), and conditionally on a hit, \(L_x\) is geometric on \(\{1,2,\ldots\}\) with success parameter \(1/G\). Hence, whenever \((1-1/G)e^\lambda<1\),

\[
 \mathbb E_ze^{\lambda L_x}
 =1+\frac{G_B(z,x)}G\frac{e^\lambda-1}{1-(1-1/G)e^\lambda}.
 \tag{10}
\]

Fix \(\delta\in(0,1)\), and set \(\lambda=(1-\delta)/(g\log a)\). By (7), \(\lambda G=1-\delta+O(1/\log a)\). Expanding the denominator in (10) bounds it below by \(c_\delta/G\); its numerator is at most \(C/G\). Using (8) gives

\[
 \mathbb E_ze^{\lambda L_x}\le1+C_\delta/\log a
 \tag{11}
\]

uniformly for \(x\in A_n(\alpha)\) and \(z=0\) or \(3a-1\le|z|\le3a\). This small excess over one is essential; a fixed-constant bound would lose the result after many episodes.

### 4.4 Counting returns to the annulus

On the infinite recurrent walk, without killing it at \(T_n\), define

\[
 U_0=0,\ V_0=T_{4a},\quad
 U_j=\inf\{t\ge V_{j-1}:|S_t|\le3a\},\quad
 V_j=\inf\{t\ge U_j:|S_t|>4a\}\quad(j\ge1).
\]

Let \(N=\#\{j\ge1:U_j<T_n\}\). Intervening paths stay outside radius \(3a\), so every annulus visit before \(T_n\) occurs in these episodes. Eventually \(4a+1<n\), so each episode starting before \(T_n\) also ends before it.

At \(y=S_{V_j}\), where \(4a<|y|\le4a+1\), let \(q_y\) be the probability to exit radius \(n\) before returning to \(D(0,3a)\). Optional stopping of the harmonic potential kernel away from zero gives

\[
 q_y=\frac{\log(4/3)+O(a^{-1})}{\log(n/(3a))+O(a^{-1})}
 \ge c/\log n.
 \tag{12}
\]

Indeed the inner stopping radius belongs to \([3a-1,3a]\), the outer radius to \((n,n+1]\), and the initial radius to \((4a,4a+1]\). Substitute the uniform potential-kernel expansion at these three radii in the stopped identity; the constants cancel and give (12). The stopping occurs in a bounded annulus, so optional stopping is legitimate.

Strong Markov at the successive \(V_j\)'s now gives

\[
 \mathbb P(N>m)\le(1-c/\log n)^m.
 \tag{13}
\]

Choose \(m=\lceil\log n\log\log n\rceil\). This probability tends to zero, while \(m/\log a=O_\alpha(\log\log n)=o(\log n)\).

### 4.5 Sharp upper bound

Let \(L_j(x)\) count visits during \([U_j,V_j)\). Strong Markov at \(U_j\) gives the conditional bound (11) for every episode, including the initial one. Repeated conditioning yields

\[
 \mathbb E\exp\{\lambda\sum_{j=0}^mL_j(x)\}
 \le(1+C_\delta/\log a)^{m+1}
 \le\exp\{C_\delta(m+1)/\log a\}.
 \tag{14}
\]

No independence of episodes or their entrance points is assumed. Defining episodes on the infinite path means these first \(m+1\) episodes always exist, so there is no conditioning on \(N\).

On \(\{N\le m\}\), the sum in (14) dominates actual annulus local time. Since there are at most \(Ca^2\) annulus points, exponential Markov and a union bound give

\[
 \mathbb P\{Q_n(\alpha)\ge t\}\le\mathbb P(N>m)
 +Ca^2\exp\{-\lambda t+C_\delta(m+1)/\log a\}.
 \tag{15}
\]

Take \(t=2g(1+\varepsilon)\log^2a\), and then choose \(\delta>0\) with \((1-\delta)(1+\varepsilon)>1\). The logarithm of the second term is bounded by

\[
 [2-2(1-\delta)(1+\varepsilon)]\log a+O_\alpha(\log\log n)\to-\infty.
\]

Equation (13) therefore proves

\[
 \mathbb P\{Q_n(\alpha)>\tfrac4\pi(1+\varepsilon)\alpha^2\log^2n\}\to0.
 \tag{16}
\]

### 4.6 Sharp lower bound and the multiscale input

Set \(H=\inf\{t:|S_t|\ge3a/2\}\), \(z=S_H\), and \(r=\lfloor a/8\rfloor\). For large \(n\),

\[
 D(z,r+1)\subset\{x:a<|x|\le2a\}\subset D(0,n-2).
 \tag{17}
\]

The walk reaches \(H\) before either outer stopping time. Follow it from \(H\) until exit from \(D(z,r)\). By strong Markov and translation invariance, conditional on the past, this segment translated by \(-z\) is exactly an SRW started at zero and stopped at \(T_r\). It is wholly inside the annulus and ends before both \(T_n\) and \(\tau_n\).

By (5), its maximum local time divided by \(\log^2r\) tends to \(4/\pi\) in probability. The conditional law is independent of the random \(z\), so no unproved uniformity in starting points is required. Since \(\log r/\log n\to\alpha\), this proves

\[
 \mathbb P\{Q_n(\alpha)<\tfrac4\pi(1-\varepsilon)\alpha^2\log^2n\}\to0.
 \tag{18}
\]

Together (16) and (18) prove Theorem A. Its upper bound for \(\tau_n\) follows from \(\tau_n\le T_n\); the same embedded segment proves its lower bound.

The DPRZ excursion-counting second-moment method enters through the established theorem (3). A naive second moment of high-local-time indicators fails because nearby sites share outer excursions. DPRZ, and Rosen's direct random-walk proof, instead specify successful excursion-count profiles on nested circles, group pairs by their shared scale, and estimate the successful-point count by a second moment. This report uses that proved input for a fresh disc segment. It does not claim to have re-proved their entire deep theorem or to have established a new successful-point second moment for Okada's moving boundary. The additional annulus upper bound is proved in full above.

### 4.7 Covered discs

Use the same embedded segment (17). DPR (2007), Theorem 1.1, equation (1.3), gives a largest covered radius \(r^{1/2+o_{\mathbb P}(1)}\) for its translated law. All covered points of this segment lie in \(D(z,r)\). Thus every lattice point of the resulting covered disc, not just its center, lies in the annulus. Since \(\log r/\log n\to\alpha\), this proves the lower bound in (B).

For the upper bound, any lattice disc contained in \(D(0,2a)\) has radius \(O(a)\). For instance, its center has norm at most \(2a\), and if its radius exceeded \(4a+1\), a horizontal lattice point inside the claimed disc would violate containment. Hence \(C_n\le n^{\alpha+o(1)}\) deterministically. It is also at most the largest covered disc anywhere before \(T_n\), namely \(n^{1/2+o(1)}\) a.s. by DPR. Taking the smaller bound proves (B). The same segment and upper domination apply to \(\tau_n\).

### 4.8 Deterministic-time corollary

For fixed \(0<\beta<1/2\), the same argument gives

\[
 \frac{\max_{t^\beta<|x|\le2t^\beta}K(t,x)}{\log^2t}
 \xrightarrow{\mathbb P}\frac{4\beta^2}{\pi}.
 \tag{19}
\]

For the upper bound apply Theorem A with outer radius \(n=t\); pathwise \(t<T_t\). For the lower bound set \(a=t^\beta\) in (17). The expected time to reach radius \(3a/2\), followed by exit from the embedded radius-\(a/8\) disc, is \(O(a^2)\) by the stopped squared-distance martingale. The probability it has not finished by time \(t\) is therefore \(O(t^{2\beta-1})\to0\). Its local-time maximum supplies the lower bound. This proves the in-probability assertion without an almost sure sharpening of the older subset bounds.

## 5. Heuristic from excursions and coverage

Equation (9) gives mean local time \(g(1-\alpha)\log n+O(1)\) at a fixed annulus site, a geometric conditional tail of scale \(g\log n\), and a nonvanishing probability of no hit. Treating \(n^{2\alpha}\) sites as independent with that tail suggests \((4\alpha/\pi)\log^2n\). That is only a first-moment upper scale, not the typical maximum.

Equation (12) instead gives a mean number of return episodes asymptotic to

\[
 \frac{\log(n/(4a))}{\log(4/3)}
 \sim\frac{1-\alpha}{\log(4/3)}\log n.
\]

The count has geometric fluctuations, not a law of large numbers on that scale. An episode hits a particular annulus site with probability \(O(1/\log a)\); conditional on hitting, it generates \(g\log a+O(1)\) visits. Typical coarse counts are \(O(\log n)\), far below \(\log^2a\). Exceptionally many shared coarse returns inflate first moments and correlate the pointwise events; the cutoff in (13) removes them with probability tending to one.

For circles centered at a particular point \(x\) with \(|x|\asymp a\), choose \(b\to\infty\), \(\log b=o(\log a)\), and a fixed ratio \(c>1\). Count entries into \(D(x,b)\) followed by exits from \(D(x,cb)\). Each such outward episode contributes expected local time \(g\log c+O(b^{-1})\) at \(x\), by the point-centered version of (6). Every visit to \(x\) belongs to one of these episodes. Summing conditional expectations, or first summing a finite number and then using monotone convergence, therefore gives

\[
 \mathbb E N_x(b,cb)\sim\frac{(1-\alpha)\log n}{\log c}.
\]

This is an expectation, not a concentration assertion. In the DPRZ picture, a successful thick site instead has fine-scale counts of order \(2\log^2a/\log c\), together with a compatible profile at all intervening scales. The shared outer parts of those profiles explain the dependence between candidate sites. The choice \(\log b=o(\log a)\) puts these circles near the fine end of the logarithmic hierarchy; no such count profile is claimed proved here beyond the established DPRZ input.

At the fine scale, \(a^2\) candidate sites balanced against a tail cost \(e^{-u/(g\log a)}\) give

\[
 u\simeq2g\log^2a=(4/\pi)\alpha^2\log^2n,
\]

as proved. Near a true outer boundary the diagonal Green scale is instead affected by boundary distance. But for every fixed \(\alpha<1\), \(n-|x|\sim n\); no boundary change occurs at \(\alpha=1/2\).

For coverage, DPR's multiscale balance compares excursions accumulated around a candidate disc with excursions needed to visit all its smaller subdiscs. In an effective domain of radius \(a\), the one-traversal balance gives covered radius \(a^{1/2}\). The outer \(O(\log n)\) returns are negligible relative to \(\log^2a\), suggesting (C). Collin–Popov's fixed-density independent-excursion results interpolate the radius exponent as \((1+\sqrt\theta)/2\) and the maximum constant as \((4/\pi)(1+\sqrt\theta)^2\). Their small-density limit is consistent with these predictions. A fixed-\(\theta\) theorem cannot simply be substituted at a vanishing, \(n\)-dependent \(\theta\); a coupling and coverage argument remains necessary for the matching upper bound, and is not supplied here.

## 6. Simulation and audit

The simulations address the separate annulus statistics, not Okada's generalized boundary maximum. [code/srw.c](code/srw.c) generates SRW until its first step outside the closed Euclidean disc. [code/simulate.py](code/simulate.py) counts time zero, omits the exterior exit site, and measures \(\alpha\in\{0.25,0.4,0.5,0.65,0.8\}\). Five measurements from one path are dependent.

There are 120 independently seeded paths: 24 each at radii 128, 256, 512; 20 at 1024; 16 at 2048; 12 at 4096. The 600 rows in [data/simulation.csv](data/simulation.csv) record seeds, exit times, maxima, covered-disc centers/radii, and normalizations. Complete grouped statistics are in [data/summary.csv](data/summary.csv) and [data/SUMMARY.md](data/SUMMARY.md).

The covered radius is exact for integer radii and lattice centers. Form the Boolean mask of visited sites inside the annulus, padded with false entries. A Euclidean distance transform gives each center's distance to the nearest forbidden lattice point. A closed disc of integer radius \(r\) is valid exactly when \(r\) is strictly smaller than that distance. Thus the optimal integer radius is \(\max(0,\lceil d_{\max}\rceil-1)\), and \(d_{\max}\) is the real-radius supremum. This enforces containment of the whole lattice disc in the annulus.

The largest-radius summary from the saved data follows. Standard errors describe variation across the 12 paths, not an asymptotic error estimate.

| n | α | paths | mean M/log²n | standard error | limit | mean log R/log n | predicted exponent |
|---:|---:|---:|---:|---:|---:|---:|---:|
| 4096 | 0.25 | 12 | 0.3397 | 0.0447 | 0.0796 | 0.1441 | 0.125 |
| 4096 | 0.4 | 12 | 0.4722 | 0.0368 | 0.2037 | 0.2621 | 0.200 |
| 4096 | 0.5 | 12 | 0.5312 | 0.0424 | 0.3183 | 0.3044 | 0.250 |
| 4096 | 0.65 | 12 | 0.7022 | 0.0542 | 0.5379 | 0.3418 | 0.325 |
| 4096 | 0.8 | 12 | 0.9094 | 0.0657 | 0.8149 | 0.3992 | 0.400 |

 Small-\(\alpha\) annuli remain tiny: at \(n=4096\), \(n^{1/4}=8\). The local-time measurements are substantially above the asymptotic constants there. Bounded Green corrections, coarse returns and lattice effects remain large; these data do not establish convergence. Covered-disc exponents are broadly compatible with the heuristic, with visible drift. Convergence in probability alone also does not justify convergence of sample means.

Validation in [code/check_simulation.py](code/check_simulation.py) independently reproduced full C trajectories/count arrays in Python for 12 small seeded cases. Exhaustive enumeration of every center/integer radius checked the distance-transform statistic on 30 random masks. Every main simulation verified conservation of visit counts and the exterior exit condition. All checks passed; see [data/checks.json](data/checks.json).

[data/resources.json](data/resources.json) records one thread, nice 10 verified by `os.getpriority`, about 30.6 seconds simulation/analysis wall time, parent peak RSS 1,133,117,440 bytes and child peak RSS 269,811,712 bytes. Even their sum is below 1.5 GB. The parent and simulation child do not peak simultaneously. No PDFs, scans or paper page images were written: downloads were converted in memory with `pdftotext -layout - -`. Nothing was published or pushed.

Reproduction, in an already nice-10 shell (the driver checks priority):

```sh
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python3 code/fetch_sources.py
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python3 code/simulate.py
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python3 code/check_simulation.py
python3 code/summarize.py
```

## 7. Remaining questions

1. A consistently timed version of the actual moving-pattern boundary problem, including its almost sure asymptotic for offsets \(n^\beta\), \(\beta<1/2\).
2. Almost sure full-sequence convergence for the separate annulus maximum. The return-count cutoff probabilities here are not summable on geometric radii, so Borel–Cantelli does not upgrade the proof.
3. The matching annulus covered-disc upper exponent \(\alpha/2\), presently only a heuristic in this report.
4. A complete citing-literature census for 2016–2026. All specified author groups were checked, but not every citing paper is certified found.

Task: “Open problem E0086.” Received/start recorded 2026-11-13 07:32 +04 (Asia/Tbilisi).
