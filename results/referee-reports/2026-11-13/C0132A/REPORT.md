PARTIAL

# Balanced excited walks M(d₁,d₂): literature, range estimates, and a return criterion

## Statements and scope

Let $W_n=(X_n,Y_n)$ start at the origin of $\mathbb Z^{d_1}\times\mathbb Z^{d_2}$, with every site initially unvisited. On its first departure from a site it takes a uniform nearest-neighbour step in $X$; on subsequent departures it takes such a step in $Y$. Put

\[
 R_n=\#\{W_0,\ldots,W_n\},\qquad
 A_n=\sum_{j=0}^{n-1}\mathbf1_{\{W_j\notin\{W_0,\ldots,W_{j-1}\}\}},
 \qquad B_n=n-A_n.
\]

An empty set in the indicator at $j=0$ makes the origin fresh. Thus $A_n$ counts first departures, rather than arrivals.

**Published theorem (Peres–Schapira–Sousi, 2016, Theorem 1.1).** For $M(1,2)$,
\[
 \|W_n\|\longrightarrow\infty\quad\text{almost surely}.
\]
This is an existing theorem; its proof is in the [published article](https://math.univ-lyon1.fr/~schapira/articlespdf/AIHP.2%2B1.pdf). Its first coordinate and last two coordinates are permuted relative to that article's notation.

**Theorem A (range estimate).** For $M(2,1)$, let $T_0=0$ and
\[
 T_m=\inf\{n\geq0:A_n=m\}\quad(m\geq1).
\]
There is a finite constant $C$ such that, for all $m\geq1$,
\[
 \mathbb E T_m\leq C m[\log(m+2)]^2. \tag{1}
\]
Consequently,
\[
 \mathbb P(R_n<m)\leq\frac{C m[\log(m+2)]^2}{n},\qquad n\geq1, \tag{2}
\]
and, for every $\varepsilon>0$, there is a deterministic $c_\varepsilon>0$ such that almost surely, for all sufficiently large $n$,
\[
 R_n\geq c_\varepsilon\frac{n}{(\log n)^{3+\varepsilon}}.
 \quad\text{In particular,}\quad
 \lim_{n\to\infty}\frac{\log R_n}{\log n}=1\quad\text{a.s.} \tag{3}
\]

**Theorem B (exact return criterion).** For $M(p,1)$, $p\in\{1,2\}$, enumerate the successive entries into the column $X=0$, excluding the initial position. At entry $k$, let $q_k$ be the conditional probability, given the history through that entry, of hitting the origin before the next departure from that column. Then, up to a null event,
\[
 \{W_n=0\text{ infinitely often}\}
 =\left\{\sum_{k=1}^\infty q_k=\infty\right\}. \tag{4}
\]
Formula (11) below computes each $q_k$ from the entry height and the connected component of consumed sites containing the origin. For $M(1,1)$, the published all-or-empty recurrent-set theorem makes (4) also a criterion for recurrence at every vertex.

Complete proofs of Theorems A and B follow. No novelty claim is made for these auxiliary observations. Neither transience of $M(2,1)$ nor recurrence of $M(1,1)$ is proved here.

## Literature audit, through 13 November 2026

In the three-parameter notation used in later papers, the present $M(a,b)$ is $M(a+b,a,b)$, also written $M_{a+b}(a,b)$.

| Requested case | Status found | Author, publication, and exact relevant assertion |
|---|---|---|
| $M(1,2)$ | Settled in print: transient | Yuval Peres, Bruno Schapira, Perla Sousi, *Martingale defocusing and transience of a self-interacting random walk*, Ann. Inst. Henri Poincaré Probab. Statist. **52**(3) (2016), 1009–1022, [DOI](https://doi.org/10.1214/14-AIHP667), [arXiv:1403.1571](https://arxiv.org/abs/1403.1571). Theorem 1.1 asserts almost-sure escape of the norm to infinity for one-dimensional first departures and two-dimensional subsequent departures. |
| $M(2,1)$ | No settlement located; transience remains the open target | Camarena–Panizo–Ramírez explicitly list $M_3(2,1)$ as open in their overview, [arXiv:2002.05750v2, introduction](https://arxiv.org/html/2002.05750v2). The 2016 paper's Section 4 explains the obstruction to reversing the roles of the projections. Searches through the audit date found no later proof. |
| $M(1,1)$ | No recurrence proof located; conjectural | Omer Angel, Mark Holmes, Alejandro Ramírez, *Balanced excited random walk in two dimensions*, Ann. Probab. **51**(4) (2023), 1421–1448, [DOI](https://doi.org/10.1214/23-AOP1622). Their recurrent-set and range results are stated below; they do not prove recurrence. Shuo Qin's [September 2026 preprint, introduction](https://arxiv.org/html/2609.30045v1) explicitly still calls recurrence of $M(2,1,1)$ conjectural. |

The introductory claim in the question is correct: Itai Benjamini, Gady Kozma, Bruno Schapira, *A balanced excited random walk*, C. R. Math. Acad. Sci. Paris **349** (2011), 459–462, [Theorem 1](https://math.univ-lyon1.fr/~schapira/articlespdf/CRAS.2%2B2.pdf), proves transience of $M(2,2)$.

The source survey is Elena Kosygina and Martin P. W. Zerner, *Excited random walks: results, methods, open problems*, 2012 preprint, published in Bull. Inst. Math. Acad. Sin. (N.S.) **8**(1) (2013), 105–157; [arXiv:1204.1895](https://arxiv.org/abs/1204.1895). Remark and Problem 3.22 gives precisely the three conjectural classifications in the question. The author PDF places it on page 16.

### Why the 2013 theorem does not settle the singular models

Yuval Peres, Serguei Popov, Perla Sousi, *On recurrence and transience of self-interacting random walks*, Bull. Braz. Math. Soc. (N.S.) **44** (2013), 841–867, [DOI](https://doi.org/10.1007/s00574-013-0036-4), [accepted manuscript](https://api.repository.cam.ac.uk/server/api/core/bitstreams/84df9135-4b97-4b22-b3a4-ca962f747975/content), Theorem 1.2, proves transience under every adapted selection of two mean-zero **d-dimensional** laws in dimension $d\geq3$, with a finite $2+\beta$ moment for some $\beta>0$. The definition on page 2 requires each law to have invertible covariance.

For the present $M(2,1)$, the two covariances are
\[
 \operatorname{diag}(1/2,1/2,0),\qquad\operatorname{diag}(0,0,1).
\]
Both are singular. Having supports whose union spans three dimensions does not satisfy that hypothesis. Theorem 1.3's strict trace condition cannot rescue this application either: any nonzero positive semidefinite matrix of rank at most two has trace at most twice its largest eigenvalue, and a linear map cannot increase rank.

### Exact planar results and the 2026 distinction

In the [Angel–Holmes–Ramírez author preprint](https://researchers.ms.unimelb.edu.au/~mholmes1@unimelb/BERW_main.pdf), Theorem 1.1 says that the random set $D$ of infinitely visited vertices satisfies
\[
 \mathbb P(D\in\{\varnothing,\mathbb Z^2\})=1.
\]
It does not assert that either alternative has probability one. Theorem 1.5 gives, for every $a_n\to\infty$,
\[
 \mathbb P\!\left(R_n>\frac{na_n}{\sqrt{\log\log n}}\right)\to0,
 \qquad
 \mathbb P\!\left(R_n\geq\frac{n^{4/7}}{(\log n)^2}\right)\to1. \tag{5}
\]
Theorem 4.2 also gives $\mathbb E R_n=O(n/\sqrt{\log\log n})$. Coordinate orientation is reversed in that paper. The publisher metadata confirms the 2023 publication; theorem numbering and displayed formulas here were checked in the accessible 2021 author preprint. Access to the final journal PDF was blocked, so its numbering was not independently checked.

Daniel Camarena, Gonzalo Panizo, Alejandro F. Ramírez, *An overview of the balanced excited random walk*, in *In and Out of Equilibrium 3*, Progress in Probability **77** (2021), 207–217, [preprint](https://arxiv.org/abs/2002.05750), treats overlapping coordinates as well. Its transience theorem concerns $d\geq4$ and does not settle either remaining case here.

Shuo Qin, *Recurrence and range of the balanced excited random walk M(2,1,2)*, [arXiv:2609.30045](https://arxiv.org/abs/2609.30045), submitted 24 September 2026, is a preprint. Its Theorem 1.1 proves recurrence and $R_n\log n/n\to\pi$ for horizontal first departures followed by **planar** steps. In the question's model subsequent departures are vertical. In Qin's cookie parametrization the latter would require strength (-1) on every subsequent visit, an infinite negative budget, outside his finite-budget recurrence theorem. Thus this recent result does not settle $M(1,1)$.

The audit used the named papers, their references, author publication lists, title searches, and arXiv-restricted searches for “balanced excited random walk”, “M(1,2)”, and “M(2,1)”, including the three-parameter variants and 2024–2026 searches. The absence of a located result is a literature-search conclusion, not a theorem that no result exists. Source files and retrieval metadata are in [sources/manifest.json](sources/manifest.json); search scope is recorded in [sources/search_log.json](sources/search_log.json).

## Projection clocks

**Lemma 1.** There are independent simple random walks $U$ on $\mathbb Z^{d_1}$ and $V$ on $\mathbb Z^{d_2}$ such that
\[
 W_n=(U_{A_n},V_{B_n}),\qquad
 R_n=A_n+I_n, \tag{6}
\]
where $I_n$ is the indicator that $W_n$ is fresh. Moreover,
\[
 A_n\to\infty,
 \qquad\liminf_{n\to\infty}\frac{B_n}{n}\geq\frac1{6d_1}
 \quad\text{a.s.} \tag{7}
\]
The processes $\|X_n\|^2-A_n$, $\|Y_n\|^2-B_n$, and $\|W_n\|^2-n$ are martingales.

**Proof.** Supply two independent infinite sequences of uniform nearest-neighbour increments, and read the next unused increment from the appropriate sequence at each departure. The rule uses only increments already read. This constructs the required law and proves the first identity in (6). Each distinct vertex other than a possibly fresh current vertex has contributed exactly one first departure, proving the second identity.

At every physical step the sum of all coordinates changes by an independent symmetric sign: conditional on the entire past, either sign has probability $1/2$. This sum is therefore a one-dimensional simple random walk and is unbounded almost surely. Hence $R_n\to\infty$, and (6) gives $A_n\to\infty$.

In any block of three steps, conditional on its initial history, the probability of at least one revisit departure is at least $1/(2d_1)$. Indeed, if the initial vertex is old there is such a departure immediately. If it is fresh and the next vertex is old, the next departure suffices. Otherwise the first two departures use the first block of coordinates; with probability $1/(2d_1)$ the second step reverses the first, so that the third departure is from an old vertex. For disjoint three-step blocks let $J_k$ indicate the presence of a revisit departure. The bounded martingale differences $J_k-\mathbb E(J_k\mid\mathcal F_{3k})$ have averages tending to zero almost surely, by Azuma's inequality and Borel–Cantelli. Since $B_{3m}\geq\sum_{k<m}J_k$, (7) follows, first at multiples of three and then at all times by monotonicity.

Every increment has conditional mean zero and squared length one in its chosen block. Expanding each squared norm proves the three martingale assertions. ∎

Independence of $U$ and $V$ in (6) does **not** imply independence conditional on $A_n$. The clock is a function of both paths. In particular, (6) does not justify multiplying the two deterministic-time return probabilities and then substituting $A_n\approx R_n$.

## Proof of Theorem A

Let $U$ be the two-dimensional walk of Lemma 1 and define its local times by
\[
 L_m(u)=\sum_{i=0}^{m-1}\mathbf1_{\{U_i=u\}}.
\]
At time $T_j$, the first projection is $U_j$. In a fixed column $u$, the number of distinct vertices whose first departure has occurred is exactly $L_j(u)$: the first departure indexed $i+1$ occurs in column $U_i$, and no vertex has two first departures.

Condition on the entire path $U$. Given the history through $T_j$, if the current vertex is fresh, its next departure is immediate and $T_{j+1}-T_j=1$. Otherwise let $[a,b]\cap\mathbb Z$ be the component of consumed sites in column $U_j$ containing the current height $y$. Until reaching $a-1$ or $b+1$, the walk uses only unused increments of $V$. At that first exit it reaches a fresh site, whose next departure advances $U$.

For one-dimensional simple random walk, the expected time $H$ to exit $[a,b]$ from $y$ is
\[
 \mathbb E_y H=(y-a+1)(b+1-y)
 \leq\frac{(b-a+2)^2}{4}. \tag{8}
\]
The displayed expression solves $h(y)=1+(h(y-1)+h(y+1))/2$ with zero boundary values at $a-1,b+1$, which proves (8) by the finite absorbing-chain equations. In particular exit occurs almost surely. The component contains at most $L_j(U_j)$ sites, so
\[
 \mathbb E(T_{j+1}-T_j\mid U,\mathcal F_{T_j})
 \leq 1+\tfrac14(L_j(U_j)+1)^2. \tag{9}
\]
Conditioning on all of $U$ is legitimate here: it reveals no unused $V$-increments. The vertical index at $T_j$ is a stopping time for the revealed vertical increments with this additional independent information. Induction using (8) also proves $T_j<\infty$ almost surely for every $j$.

For $j<m$, $L_j(U_j)+1\leq L_m(U_j)$. Summing (9) and taking conditional expectations gives
\[
 \mathbb E(T_m\mid U)
 \leq m+\tfrac14\sum_{j<m}L_m(U_j)^2
 =m+\tfrac14\sum_u L_m(u)^3. \tag{10}
\]
Write $p_r=\mathbb P(U_r=0)$, $p_0=1$, and $G_m=\sum_{r=0}^{m-1}p_r$. Ordering the three indices in the expansion of the cubic local time and using independent increments yields
\[
 \mathbb E\sum_u L_m(u)^3
 =\sum_{i,j,k<m}\mathbb P(U_i=U_j=U_k)
 \leq6\sum_{0\leq i\leq j\leq k<m}p_{j-i}p_{k-j}
 \leq6mG_m^2.
\]
For planar simple random walk,
\[
 p_{2r}=\left(\frac{\binom{2r}{r}}{4^r}\right)^2,
 \qquad p_{2r+1}=0.
\]
For example, this follows by applying the invertible coordinate transformation $(x,y)\mapsto(x+y,x-y)$, under which the two increments are independent symmetric signs. The central-binomial bound, or Stirling's formula, gives $p_{2r}\leq C/(r+1)$. Thus $G_m\leq C\log(m+2)$. Taking expectations in (10) proves (1).

If $R_n<m$, then $A_n<m$, hence $T_m>n$. Markov's inequality proves (2). Fix $\varepsilon>0$. By (1), for $k\geq1$,
\[
 \mathbb P\{T_{2^k}>2^k k^{3+\varepsilon}\}
 \leq C k^{-1-\varepsilon}.
\]
Borel–Cantelli implies $T_{2^k}\leq2^k k^{3+\varepsilon}$ eventually almost surely. For a large $n$, choose $k$ with
\[
 2^k k^{3+\varepsilon}\leq n
 <2^{k+1}(k+1)^{3+\varepsilon}.
\]
Then $R_n\geq A_n\geq2^k\geq c_\varepsilon n/(\log n)^{3+\varepsilon}$. Together with $R_n\leq n+1$, this proves (3). ∎

The same argument also gives $\mathbb P\{R_n<n/(\log n)^{2+\varepsilon}\}\to0$, with integer rounding understood. These bounds control a clock, not the joint distribution of position and clock.

## Proof of Theorem B

Call a site **consumed** at time $t$ if its first departure occurred strictly before $t$. Consider the column $X=0$. After the initial departure the origin is consumed. At every later entry time $\sigma_k$, let $y_k=Y_{\sigma_k}$, and let $[a_k,b_k]\cap\mathbb Z$ be the component containing zero of the consumed heights in this column. It is a finite interval, even though the full set of consumed heights may be disconnected. Define
\[
 q_k=
 \begin{cases}
 1,&y_k=0,\\
 \dfrac{b_k+1-y_k}{b_k+1},&1\leq y_k\leq b_k,\\
 \dfrac{y_k-a_k+1}{1-a_k},&a_k\leq y_k\leq-1,\\
 0,&y_k\notin[a_k,b_k].
 \end{cases} \tag{11}
\]

If an entry is at a fresh site, the next step leaves the column immediately. If it is in a consumed component not containing zero, vertical motion encounters a fresh boundary site before reaching zero, and the next step again leaves the column. In either case the success probability is zero. Within the component containing zero, the vertical motion is simple random walk until reaching a fresh boundary site. For $y_k>0$, the probability of reaching zero before $b_k+1$ is $(b_k+1-y_k)/(b_k+1)$, the unique affine solution of the two-boundary hitting problem. The case $y_k<0$ is identical. Arrival at zero is already a success. This proves (11) as a conditional probability given $\mathcal F_{\sigma_k}$.

Every column episode ends almost surely in finite time: an old starting site belongs to a finite consumed component, and (8) applies; a fresh starting site leaves in one step. Lemma 1 gives $A_n\to\infty$. Since $U$ is recurrent for $p=1,2$, it returns to zero infinitely often, so there are infinitely many finite entry times $\sigma_k$.

Let $E_k$ be the event of success in episode $k$, $Z_k=\mathbf1_{E_k}$, and $\mathcal G_k=\mathcal F_{\sigma_k}$. The outcome $Z_k$ is known before $\sigma_{k+1}$, and
\[
 \mathbb E(Z_k\mid\mathcal G_k)=q_k.
\]
For completeness, the needed conditional Borel–Cantelli argument is as follows. Write $Q_k=\sum_{i\leq k}q_i$, $Q_0=0$. The process
\[
 N_n=\sum_{k\leq n}\frac{Z_k-q_k}{1+Q_k}
\]
is a martingale, with the filtrations indexed so that its $k$-th difference is revealed in $\mathcal G_{k+1}$. Its predictable sum of conditional variances is at most
\[
 \sum_k\frac{q_k}{(1+Q_k)^2}
 \leq\sum_k\int_{Q_{k-1}}^{Q_k}\frac{dx}{(1+x)^2}\leq1.
\]
It is therefore bounded in $L^2$ and converges almost surely. On $Q_k\to\infty$, Kronecker's lemma, equivalently summation by parts applied to this convergent series, gives
\[
 \frac{\sum_{k\leq n}(Z_k-q_k)}{1+Q_n}\to0.
\]
Consequently $\sum_{k\leq n}Z_k\sim Q_n\to\infty$.

For the converse, fix an integer $r\geq1$. Since $\{Q_{k-1}\leq r\}\in\mathcal G_k$,
\[
 \mathbb E\sum_k Z_k\mathbf1_{\{Q_{k-1}\leq r\}}
 =\mathbb E\sum_k q_k\mathbf1_{\{Q_{k-1}\leq r\}}\leq r+1.
\]
Thus the sum on the left is finite almost surely. On $\{Q_\infty\leq r\}$ it is the full sum of the $Z_k$. Taking the union over $r$ proves that $\sum q_k<\infty$ implies only finitely many successes.

Each episode contains finitely many steps, and every origin visit after the initial departure lies in a column-zero episode. Infinitely many origin visits are therefore equivalent to infinitely many successful episodes. The two implications just proved establish (4). ∎

### The interval obstruction in the previous note

The following legal path for $M(1,1)$ has probability $2^{-10}$:
\[
\begin{split}
 (0,0)&\to(1,0)\to(2,0)\to(1,0)\to(1,1)\to(2,1)\\
 &\to(3,1)\to(2,1)\to(2,2)\to(1,2)\to(0,2).
\end{split}
\]
At its endpoint, the visited heights in column zero are $\{0,2\}$; height (1) has not been visited. The entry at height (2) has $q=0$, since its first departure is horizontal. One further step to $(1,2)$ leaves the **consumed** heights in column zero equal to $\{0,2\}$ as well. The path and all its allowed departures are checked in [code/verify.py](code/verify.py).

Even when an entry is in the origin's component, (11) depends on its distance from the exit boundary. A probability comparable to reciprocal interval length requires an additional restriction on entry depth. Component length alone, and still less the total number of visited sites in the column, supplies no such estimate.

## Numerical results

The two open cases were each run for 128 seeds, numbered 0–127, to $10^7$ steps: $2.56\times10^9$ transitions in total. Cases and seeds ran sequentially, using one thread and inherited nice value 20. The largest measured child RSS was 135,544,832 bytes (129.27 MiB). The hash table occupies exactly 128 MiB; no trajectories or worker pools are retained. The runner's attempted address-space limit is unavailable in this macOS sandbox; measured RSS, the fixed table allocation, and the saved resource records supply the memory check. See [data/resources.json](data/resources.json).

Two independently initialized SplitMix64 streams supply the projection increments. Seed initialization constants and packing bounds are in [code/simulate.cpp](code/simulate.cpp). A second implementation uses Python's MT19937, an ordinary set of coordinate tuples, and seeds 100000–100015, each to $10^6$ steps. This checks the simulation with a different RNG and representation; its results are in [data/independent.csv](data/independent.csv).

At $10^6$ steps the independent implementation gives mean ranges $83{,}779.4\pm3{,}547.5$ for $M(1,1)$ and $607{,}400.2\pm675.1$ for $M(2,1)$ (mean ± SE over 16 seeds), consistent with the main simulation. Its complete summaries are in [data/independent_summary.csv](data/independent_summary.csv).

“Origin visits” below counts visits at times $1,\ldots,n$, excluding time zero. A late return means at least one origin visit in $(\lfloor n/2\rfloor,n]$. Each probability interval is a pointwise 95% Wilson interval across 128 seed indicators; steps within a trajectory are not treated as independent samples. SE denotes the sample standard deviation across seeds divided by $\sqrt{128}$. These are Monte Carlo summaries, not certified bounds on the infinite-time walk.

| Case | n | Mean range ± SE | Origin visits ± SE | Late-return seeds | Late-return probability (95% Wilson) |
|---|---:|---:|---:|---:|---:|
| M(1,1) | 1,000 | 298.7 ± 6.0 | 2.930 ± 0.405 | 8/128 | 0.0625 (0.0320, 0.1185) |
| M(1,1) | 10,000 | 1,794.7 ± 33.4 | 5.383 ± 0.958 | 10/128 | 0.0781 (0.0430, 0.1378) |
| M(1,1) | 100,000 | 11,829.5 ± 225.8 | 8.844 ± 1.572 | 7/128 | 0.0547 (0.0267, 0.1086) |
| M(1,1) | 1,000,000 | 81,748.4 ± 1,255.5 | 11.648 ± 2.078 | 2/128 | 0.0156 (0.0043, 0.0552) |
| M(1,1) | 10,000,000 | 589,396.4 ± 8,549.2 | 19.945 ± 4.220 | 4/128 | 0.0312 (0.0122, 0.0776) |
| M(2,1) | 1,000 | 635.3 ± 4.0 | 0.695 ± 0.125 | 1/128 | 0.0078 (0.0014, 0.0429) |
| M(2,1) | 10,000 | 6,140.2 ± 20.6 | 0.734 ± 0.126 | 0/128 | 0.0000 (0.0000, 0.0291) |
| M(2,1) | 100,000 | 60,954.4 ± 81.0 | 0.750 ± 0.128 | 0/128 | 0.0000 (0.0000, 0.0291) |
| M(2,1) | 1,000,000 | 607,446.8 ± 250.6 | 0.750 ± 0.128 | 0/128 | 0.0000 (0.0000, 0.0291) |
| M(2,1) | 10,000,000 | 6,073,117.3 ± 890.9 | 0.750 ± 0.128 | 0/128 | 0.0000 (0.0000, 0.0291) |

| Case | Interval | Effective range exponent | Paired bootstrap 95% interval |
|---|---:|---:|---:|
| M(1,1) | 1,000–10,000 | 0.7788 | (0.7569, 0.8013) |
| M(1,1) | 10,000–100,000 | 0.8190 | (0.8006, 0.8372) |
| M(1,1) | 100,000–1,000,000 | 0.8395 | (0.8208, 0.8583) |
| M(1,1) | 1,000,000–10,000,000 | 0.8579 | (0.8410, 0.8752) |
| M(2,1) | 1,000–10,000 | 0.9852 | (0.9800, 0.9909) |
| M(2,1) | 10,000–100,000 | 0.9968 | (0.9943, 0.9994) |
| M(2,1) | 100,000–1,000,000 | 0.9985 | (0.9975, 0.9995) |
| M(2,1) | 1,000,000–10,000,000 | 0.9999 | (0.9996, 1.0002) |

| Case | n | Mean column entries | Fraction with q=0 | Mean Q | Mean completed successes | Mean origin-component size |
|---|---:|---:|---:|---:|---:|---:|
| M(1,1) | 100,000 | 97.85 | 0.9507 | 2.1804 | 2.0938 | 14.30 |
| M(1,1) | 1,000,000 | 261.56 | 0.9797 | 2.3706 | 2.2734 | 19.62 |
| M(1,1) | 10,000,000 | 637.62 | 0.9906 | 2.6379 | 2.5703 | 27.48 |
| M(2,1) | 100,000 | 3.59 | 0.7778 | 0.5582 | 0.5859 | 2.19 |
| M(2,1) | 1,000,000 | 4.13 | 0.8072 | 0.5582 | 0.5859 | 2.19 |
| M(2,1) | 10,000,000 | 5.20 | 0.8468 | 0.5582 | 0.5859 | 2.19 |

The effective exponent in the second table is
\[
 \widehat\alpha(n_1,n_2)
 =\frac{\log(\overline R_{n_2}/\overline R_{n_1})}{\log(n_2/n_1)}.
\]
Its intervals use 4,000 paired bootstrap resamples of entire seeds. They measure sampling uncertainty and do not include finite-time bias. In particular, the increasing planar slopes do not establish an asymptotic exponent; fitting one power law over these scales is not justified. The nearly constant $R_n/n\approx0.6073$ for $M(2,1)$ supports transience as the proof target, while the planar data remain compatible with very sparse recurrence.

The column table records $Q=\sum q_k$ over entries begun by time $n$, successes over completed episodes, and the size of the consumed component containing zero. The last episode may be censored. At $10^7$ steps, 99.06% of planar column-zero entries have $q=0$. The mean total number of consumed sites in that column is 638.63, while the mean origin-component size is only 27.48. These quantities should not be identified.

For $M(2,1)$, no late hits at $10^7$ steps means 0/128 observed successes, not zero return probability; the one-sided 95% binomial upper limit for that finite-horizon event is $1-0.05^{1/128}=0.02313$. For $M(1,1)$, origin-visit counts at that horizon have median 3 and maximum 339, against mean 19.95. The returns are strongly clustered. The mean occupation density in the last half-window, estimating the average of $\mathbb P(W_t=0)$ over that window, is $2.703125\times10^{-5}$, $1.296875\times10^{-6}$, and $2.90625\times10^{-7}$ for $M(1,1)$ at $n=10^5,10^6,10^7$, respectively. The corresponding $M(2,1)$ estimates are all zero; these share the finite-sample limitation of the late-hit counts.

![Range growth, range fraction, and late-return probabilities](data/range_returns.png)

Raw seed data are [data/m11.csv](data/m11.csv) and [data/m21.csv](data/m21.csv). Derived machine-readable tables are [data/summary.csv](data/summary.csv), [data/growth.csv](data/growth.csv), and [data/columns.csv](data/columns.csv); the exportable figure is also available as [SVG](data/range_returns.svg).

### Reproduction and verification

From this directory:

```sh
clang++ -std=c++17 -O3 -Wall -Wextra -pedantic code/simulate.cpp -o code/simulate
python3 code/verify.py
python3 code/check_formulas.py
python3 code/run_suite.py
python3 code/independent.py
MPLCONFIGDIR=/private/tmp/c0132a-matplotlib OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 python3 code/analyze.py
```

The suite checks the governor before each case and refuses to start on a distress report; it requires or sets nice at least 10. The independent replay checks 120,000 transitions against departure counts, including range, both clocks, origin counts, late-return indicators, and conditional column probabilities. The analysis checks all 1,280 production checkpoint rows. Verification output is in [data/verification.txt](data/verification.txt). Mathematical identities (6) and the component hitting formulas are checked independently of the packed hash implementation. A separate exact rational solution of finite absorbing-chain systems checks 432 exit-time and hitting-probability values; see [code/check_formulas.py](code/check_formulas.py) and [data/formula_checks.txt](data/formula_checks.txt).

## Remaining proof obligations

For **$M(2,1)$**, Theorem A controls the first clock almost up to logarithmic factors. Transience would follow from a sufficiently strong bound on simultaneous returns at the adapted times, or from $\sum q_k^{(w)}<\infty$ almost surely for every target $w$, using the translated version of Theorem B. Neither conclusion follows from (1)–(3). A route through first-projection return epochs must control the vertical exit heights conditional on the planar path; their jumps have history-dependent scales. This is the obstacle identified in the 2016 paper.

For **$M(1,1)$**, recurrence would follow from $\sum q_k=\infty$ almost surely. The known recurrent-set theorem would then give infinitely many visits to every vertex. Required estimates must jointly control component growth and entry depths, including the probability of entering a different component. Bounds on the global range alone, including (5), do not do this.

A direct radial potential does not close either gap. For the planar walk, the leading drift of $\log\sqrt{x^2+y^2}$ under a first, horizontal departure is
\[
 \frac{y^2-x^2}{2(x^2+y^2)^2},
\]
while under a vertical departure its sign reverses. It therefore has no uniform supermartingale sign over the two laws. For $M(2,1)$, $f(w)=\|w\|^{-\alpha}$, $\alpha>0$, has positive leading drift under a first planar step when $y=0$, and under a vertical revisit step when $x=0$. Indeed the respective leading terms are $\alpha^2\|w\|^{-\alpha-2}/4$ and $\alpha(\alpha+1)\|w\|^{-\alpha-2}/2$, with symmetric-step remainders $O(\|w\|^{-\alpha-4})$. A useful potential must incorporate the visited configuration or a further estimate on where the two departure types occur.

The requested classification is therefore only partly settled: $M(1,2)$ is transient by the published 2016 theorem; the two remaining classifications are not resolved by this report.

Task: “Open problem C0132: transience and recurrence of the balanced excited random walks M(d1,d2)” — 2026-11-13 approximately 03:24 Asia/Tbilisi, first observed task time.
