PROVED

# First-passage pattern waiting time

**Theorem 1.** Fix \(\lambda<0\). Let \(a_n=-\lambda_n\), where \(\lambda_n\) is the parity-adjusted endpoint in the question, and let \(T_n\) be the first **ending time** of an admissible window. There are constants \(0<c_\lambda<C_\lambda<\infty\) and \(n_\lambda\) such that
\[
 c_\lambda n\log n\ \leq\ \mathbb E T_n\ \leq\ C_\lambda n\log n,
 \qquad n\geq n_\lambda.
\tag{1}
\]
In particular, \(\mathbb E T_n/n\to\infty\), and the polynomial exponent is exactly \(1\), with a logarithmic correction.

More precisely, put \(m=\lfloor n/2\rfloor\), and let \(q_n\) be the probability of an admissible window whose starting time belongs to \(\{0,\ldots,m\}\). Then
\[
 \frac{c_\lambda}{\log n}\leq q_n\leq\frac{C}{\log n}.
\tag{2}
\]
The upper constant in (2) is absolute, uniformly over every prescribed integer endpoint \(-a<0\), not just endpoints of order \(\sqrt n\). Moreover, for all integers \(h\geq0\),
\[
 \mathbb P(T_n\leq n+h)
 \leq \frac{C(1+h/n)}{\log n},
\tag{3}
\]
and
\[
 \mathbb P\bigl(T_n>k(n+m)\bigr)
 \leq \exp\{-c_\lambda k/\log n\},\qquad k\geq0.
\tag{4}
\]
Thus \(T_n/n\to\infty\) in probability as well.

The order in (1) is precisely Peres's conjecture: Conjecture 1, equation (30), printed p. 65 of the [published Pitman–Tang chapter](https://www.columbia.edu/~wt2319/Patterns.pdf), and Conjecture 2.5.2, p. 18 of [Tang's 2017 dissertation](https://escholarship.org/content/qt51j6244c/qt51j6244c_noSplash_0d298bb720a71e482d931510dcf532d2.pdf). The proofs below are discrete and do not use a Brownian limiting argument. An asymptotic equivalent or leading constant is not established here.

## 1. Elementary first-passage estimates

Throughout, all logarithms are natural. A simple symmetric walk starts at zero. Write
\[
 p_s(b)=\mathbb P(S_s=b),\qquad
 f_s(b)=\mathbb P(\tau_{-b}=s),\quad
 \tau_{-b}=\inf\{t\geq0:S_t=-b\},\quad b\geq1.
\]
Incompatible parities have probability zero.

**Lemma 2.** For \(s\geq1\),
\[
 f_s(b)=\frac bs p_s(b),\qquad
 \sup_{b\geq1}f_s(b)\leq \frac{C}{s}.
\tag{5}
\]
If \(a_n/\sqrt n\to\alpha>0\) and \(a_n\equiv n\pmod2\), then
\[
 p_n^{\rm FP}:=f_n(a_n)
 \sim\frac{\kappa_\alpha}{n},\qquad
 \kappa_\alpha=\alpha\sqrt{\frac2\pi}\,e^{-\alpha^2/2}>0.
\tag{6}
\]

*Proof.* By translation, first passage to \(-b\) is first passage to zero starting at \(b\). Reflection at zero and decomposition according to the last step give
\[
 f_s(b)=\frac12\{p_{s-1}(b-1)-p_{s-1}(b+1)\}
       =\frac bs p_s(b).
\]
The usual binomial estimates, uniformly in \(b\), give absolute \(c,C>0\) such that
\[
 p_s(b)\leq Cs^{-1/2}\exp(-cb^2/s).
\tag{7}
\]
For completeness, the central binomial coefficient is \(O(2^s/\sqrt s)\) by Stirling's inequalities. For \(s=2k,b=2j\geq0\), the ratio to the central probability is
\[
 \frac{p_{2k}(2j)}{p_{2k}(0)}
 =\prod_{r=1}^{j}\frac{k-r+1}{k+r}
 \leq\exp\!\left(-\frac{j^2}{k+j}\right)
 \leq\exp(-j^2/(2k)).
\]
For \(s=2k+1,b=2j+1\), the corresponding ratio to \(p_{2k+1}(1)\) is bounded by
\[
 \exp\!\left(-\frac{j(j+1)}{k+j+1}\right).
\]
These inequalities, symmetry, and enlargement of the constants give (7), including the endpoints of the support. Substitution in the first identity of (5), followed by maximizing \(x e^{-cx^2}\), proves its second assertion. Finally, Stirling's formula on the parity lattice gives
\[
 p_n(a_n)\sim\sqrt{\frac2{\pi n}}\,e^{-\alpha^2/2},
\]
which proves (6). ∎

## 2. A range estimate at descending record times

Let \(X,Y\) be independent simple symmetric walks. A time \(s\geq1\) is a strict descending record time of \(Y\) if
\[
 Y_s<\min_{0\leq u<s}Y_u.
\]
Time zero is also counted as a record. Let \(J_s\) denote this record indicator, and define
\[
 V_L=\sum_{s=0}^L J_s,\qquad
 R_L=\{X_s-Y_s:0\leq s\leq L,\ J_s=1\}.
\]
Define the deterministic return potential
\[
 G_L=\sum_{s=0}^L\mathbb P(J_s=1,\ X_s=Y_s).
\]

**Lemma 3.** For all \(L\geq1\),
\[
 \mathbb EV_L\leq1+\sqrt L,
\tag{8}
\]
and
\[
 G_L=1+\sum_{s=1}^L4^{-s}
       \binom{s-1}{\lfloor(s-1)/2\rfloor}^{\!2}
     \sim\frac{\log L}{2\pi}.
\tag{9}
\]
Consequently,
\[
 \mathbb E|R_L|\leq\frac{\mathbb EV_{2L}}{G_L}
 \leq\frac{1+\sqrt{2L}}{G_L}
 \leq C\frac{\sqrt L}{\log(L+2)}.
\tag{10}
\]

*Proof.* A strict descending record at time \(s\) with \(Y_s=-b\) is exactly \(\{\tau_{-b}=s\}\). Thus (5) and symmetry imply
\[
 \mathbb P(J_s=1)=\sum_{b\geq1}\frac bs p_s(b)
   =\frac{\mathbb E|Y_s|}{2s}\leq\frac1{2\sqrt s}.
\]
Summation gives (8).

By independence,
\[
 g_s:=\mathbb P(J_s=1,X_s=Y_s)
     =\sum_{b\geq1}\frac bs p_s(b)^2
     =4^{-s}\binom{s-1}{\lfloor(s-1)/2\rfloor}^{\!2}.
\tag{11}
\]
To verify the last equality directly, put \(b=s-2j\), and use
\[
 \frac{s-2j}{s}\binom sj^2
 =\binom{s-1}{j}^{\!2}-\binom{s-1}{j-1}^{\!2}.
\]
The sum over \(0\leq j\leq\lfloor(s-1)/2\rfloor\) telescopes. Stirling's formula gives \(g_s\sim(2\pi s)^{-1}\), proving (9).

For each integer \(z\), let
\[
 \sigma_z=\inf\{s\geq0:J_s=1,\ X_s-Y_s=z\}.
\]
This is a stopping time for the pair \((X,Y)\). On \(\{\sigma_z<\infty\}\), \(Y_{\sigma_z}\) is the minimum of its entire past. By the strong Markov property, the shifted walks after \(\sigma_z\) are independent fresh walks. In particular,
\[
 J_{\sigma_z+u}=1
 \quad\Longleftrightarrow\quad
 Y_{\sigma_z+u}-Y_{\sigma_z}
 <\min_{0\leq v<u}(Y_{\sigma_z+v}-Y_{\sigma_z}),\quad u>0.
\]
The conditional expected number of record visits to the same value \(z\) between \(\sigma_z\) and \(\sigma_z+L\), inclusive, is therefore exactly \(G_L\).

Count these visits only for sites with \(\sigma_z\leq L\), and sum over \(z\). Every counted visit occurs by time \(2L\), and each record time contributes to at most one site. Hence, pathwise,
\[
 \sum_z\mathbf1_{\{\sigma_z\leq L\}}
       \sum_{u=0}^L
       \mathbf1_{\{J_{\sigma_z+u}=1,\ X_{\sigma_z+u}-Y_{\sigma_z+u}=z\}}
 \leq V_{2L}.
\]
Taking expectations and applying the conditional expectation just proved yields
\(G_L\mathbb E|R_L|\leq\mathbb EV_{2L}\). All sums relevant to the left side have finitely many possible sites, since \(|z|\leq2L\) at a first visit by time \(L\). Equations (8) and (9), with adjustment for bounded \(L\), prove (10). ∎

## 3. Upper bound on the probability of a hit in a block

For an integer \(a\geq1\), let
\[
 E_t=\{S_t-S_{t-n}=-a,\quad S_u>S_t\text{ for }t-n\leq u<t\},\qquad t\geq n.
\]

**Lemma 4.** Uniformly over \(a\geq1\), for \(n\geq4\) and \(m=\lfloor n/2\rfloor\),
\[
 \mathbb P\left(\bigcup_{s=0}^m E_{n+s}\right)
 \leq\frac{C}{\log n}.
\tag{12}
\]

*Proof.* Decompose the increments into three independent pieces:
\[
 X_s=S_s\ (0\leq s\leq m),\qquad
 B=S_n-S_m,\qquad
 Y_s=S_{n+s}-S_n\ (0\leq s\leq m).
\]
Thus \(B\) has the law of a walk at time \(n-m\) and is independent of \((X,Y)\).

If \(E_{n+s}\) occurs for \(1\leq s\leq m\), its strict minimum condition applies, in particular, at times \(n,n+1,\ldots,n+s-1\). Hence \(s\) is a strict descending record time of \(Y\). The displacement condition gives
\[
 X_m+B+Y_s-X_s=-a,
 \quad\text{or}\quad
 B=X_s-Y_s-X_m-a.
\]
For \(s=0\) the same necessary condition holds with the record at zero included. Consequently,
\[
 \bigcup_{s=0}^m E_{n+s}
 \ \subseteq\ \{B\in R_m-X_m-a\}.
\tag{13}
\]
Conditionally on \((X,Y)\), the set on the right has \(|R_m|\) possible values for \(B\). The central binomial bound and (10) imply
\[
 \mathbb P\left(\bigcup_{s=0}^m E_{n+s}\right)
 \leq\left(\sup_b p_{n-m}(b)\right)\mathbb E|R_m|
 \leq\frac{C}{\sqrt{n-m}}\frac{\sqrt m}{\log(m+2)}
 \leq\frac{C}{\log n}.
\]
No restriction on the initial part of the first-passage window was needed for this upper bound. ∎

## 4. Lower bound on the probability of a hit in a block

**Lemma 5 (exact conditional overlap).** Suppose the window ending at time \(t\) is a particular first-passage word \(w\) of length \(n\), with \(w(0)=0,w(n)=-a\). For \(1\leq s<n\), conditionally on the history through time \(t\),
\[
 \mathbb P(E_{t+s}\mid\mathcal F_t)
 =\mathbf1_{\{w(s)<0\}}f_s(-w(s))
 \leq\frac Cs.
\tag{14}
\]

*Proof.* The new window starts at height \(S_{t-n}+w(s)\), so its required endpoint is \(S_t+w(s)\). The old endpoint \(S_t\) lies strictly before the new endpoint time inside the new window. Therefore \(w(s)<0\) is necessary. Under this condition, all retained old heights, including \(S_t\), exceed the required new endpoint, since the old endpoint was the strict minimum of the old window. The remaining condition is exactly that the fresh \(s\) increments first hit \(w(s)\) at time \(s\). These increments are independent of \(\mathcal F_t\). Apply (5). ∎

**Lemma 6.** With \(m=\lfloor n/2\rfloor\),
\[
 \mathbb P\left(\bigcup_{s=0}^m E_{n+s}\right)
 \geq\frac{(m+1)f_n(a)}{D_m},
 \qquad D_m=1+C\sum_{s=1}^m\frac1s.
\tag{15}
\]

*Proof.* Let \(N=\sum_{s=0}^m\mathbf1_{E_{n+s}}\) and let \(\sigma\) be the first successful index in this sum, with \(\sigma=\infty\) if \(N=0\). Stationarity of the increment windows gives
\(\mathbb EN=(m+1)f_n(a)\).
On \(\{\sigma=r\}\), all events counted before \(r\) are absent. The event \(\{\sigma=r\}\) is measurable through time \(n+r\). At that time an admissible word has been observed, and (14) bounds the conditional expected number of subsequent successes by \(C\sum_{s=1}^{m-r}s^{-1}\). Thus
\[
 \mathbb EN\leq D_m\mathbb P(N>0),
\]
which is (15). ∎

Alternatively, (14) gives \(\mathbb EN^2\leq(1+2C\sum_{s=1}^m s^{-1})\mathbb EN\). The Cauchy–Schwarz bound \(\mathbb P(N>0)\geq(\mathbb EN)^2/\mathbb EN^2\) gives the same order in (15).

**Proof of Theorem 1.** Apply (6) with \(\alpha=|\lambda|\). Equations (12) and (15) imply (2).

Cover the integer starting times \(\{0,\ldots,h\}\) by at most
\(1+\lfloor h/(m+1)\rfloor\) translates of \(\{0,\ldots,m\}\). The increments are stationary, so the union bound and (12) give (3). Choose a fixed sufficiently small \(\delta>0\) and put \(h=\lfloor\delta n\log n\rfloor\). For all sufficiently large \(n\), (3) is at most \(1/2\). Therefore
\[
 \mathbb ET_n\geq h\,\mathbb P(T_n>n+h)\geq h/2,
\]
proving the lower bound in (1). For any fixed \(M\), (3), with \(h\) of order \(Mn\), also proves \(\mathbb P(T_n\leq Mn)\to0\).

For the upper bound, partition the increments into disjoint blocks of length \(\ell=n+m\). Within each block inspect the \(m+1\) windows with local starting times \(0,\ldots,m\). The block successes are independent, each with probability \(q_n\geq c_\lambda/\log n\). If \(K\) is the index, starting at one, of the first successful block, then \(K\) is geometric and \(T_n\leq\ell K\). Consequently,
\[
 \mathbb ET_n\leq\frac{n+m}{q_n}\leq C_\lambda n\log n,
\]
and \(\mathbb P(T_n>k\ell)\leq(1-q_n)^k\) gives (4). ∎

## 5. Matching-matrix consequence

In the orientation of equation (2.1) of the supplied paper, the column belonging to a word \(w\) sums to
\[
 1+\sum_{s=1}^{n-1}\mathbf1_{\{w(s)<0\}}f_s(-w(s))
 \leq1+C\sum_{s=1}^{n-1}\frac1s=O(\log n).
\tag{16}
\]
Indeed, fixing the retained suffix leaves precisely a first-passage completion of length \(s\), as in Lemma 5. This replaces the \(O(n^{1/4})\) column bound in (2.23) by \(O(\log n)\). The direct block proof above supplies the waiting-time upper bound without any assumption about signs of individual entries of the inverse matching matrix.

The source of the lower logarithm is (9)–(10): the record-time process makes only \(O(\sqrt n)\) visits in an interval of length \(n\), but its return potential is of order \(\log n\). Its expected range is therefore at most \(O(\sqrt n/\log n)\). The independent middle segment in (13) turns this range bound into the required probability bound.

## 6. Numerical verification

The numerical calculations below are supplementary; no simulation or numerical inversion is used in the proofs. All waiting times include the initial \(n\) increments, as in the question. Exact arithmetic is used only in the small matching matrices. No exact large-\(n\) computation is claimed.

`exact.py` enumerates the words, forms the matching matrix, and computes
\[
 \mathbb ET=\frac{2^n}{\mathbf1^TM^{-1}\mathbf1}
\]
by rational Gaussian elimination. Independently, it constructs the automaton whose transient states are proper prefixes of target words. Its transition on a new increment is the longest suffix that is a proper prefix, unless a target word has just been completed. Solving \(e=\mathbf1+Qe\) gives the second expectation. The empty-prefix value agrees with the rational answer to within \(3\times10^{-14}\) in the cases below. Full fractions, state counts, and differences are in `data/exact.csv`.

| \(n\) | \(a\) | Number of words | Exact \(\mathbb ET\) | Decimal |
|---:|---:|---:|---:|---:|
| 3 | 1 | 1 | 8 | 8.000000 |
| 4 | 2 | 2 | 34/3 | 11.333333 |
| 5 | 1 | 2 | 16 | 16.000000 |
| 6 | 2 | 5 | 296/17 | 17.411765 |
| 7 | 1 | 5 | 128/5 | 25.600000 |
| 8 | 2 | 14 | 68202/2819 | 24.193686 |
| 9 | 3 | 28 | 375006/12865 | 29.149320 |
| 10 | 2 | 42 | 4555029/144001 | 31.631926 |
| 11 | 3 | 90 | 317290872798/8937933785 | 35.499354 |
| 12 | 2 | 132 | 17663784686/445122589 | 39.682966 |

`simulate.cpp` detects admissible windows using the current displacement and a monotone queue for the minimum of the preceding \(n\) heights. It uses one thread, \(O(n)\) memory, uncensored independent trials, and explicitly recorded seeds. The detector agrees with direct scanning on every path through time 16 for \(n=8,a=2\). A second implementation, mode `brute`, directly scans each candidate window; with the same random streams it gives identical sample moments at \(n=100\) and \(n=1000\). The small-\(n\) Monte Carlo results also agree with the exact answers.

The following intervals are normal-approximation 95% confidence intervals for the mean, computed as sample mean \(\pm1.96\) sample standard error; they are not finite-sample coverage guarantees. The larger intervals at the largest sizes reflect the reduced replication counts. Data: `data/monte_carlo.csv`; driver: `run_numerics.py`.

<!-- MONTE_CARLO_TABLE -->

| n | a | Trials | Mean T | Approx. 95% CI | Mean / n | Mean / (n log n) |
|---:|---:|---:|---:|---:|---:|---:|
| 8 | 2 | 200,000 | 24.207 | [24.138, 24.276] | 3.0259 | 1.4551 |
| 12 | 2 | 200,000 | 39.781 | [39.664, 39.898] | 3.3151 | 1.3341 |
| 100 | 10 | 30,000 | 416.331 | [412.747, 419.915] | 4.1633 | 0.9041 |
| 200 | 14 | 30,000 | 872.536 | [864.959, 880.113] | 4.3627 | 0.8234 |
| 500 | 22 | 20,000 | 2,342.688 | [2,317.480, 2,367.895] | 4.6854 | 0.7539 |
| 1,000 | 30 | 20,000 | 4,818.209 | [4,765.957, 4,870.462] | 4.8182 | 0.6975 |
| 2,000 | 44 | 20,000 | 10,227.579 | [10,112.982, 10,342.176] | 5.1138 | 0.6728 |
| 10,000 | 100 | 8,000 | 56,062.004 | [55,063.319, 57,060.689] | 5.6062 | 0.6087 |
| 100,000 | 316 | 1,000 | 657,062.633 | [621,649.975, 692,475.291] | 6.5706 | 0.5707 |
| 1,000,000 | 1000 | 200 | 7,812,672.415 | [6,890,113.914, 8,735,230.916] | 7.8127 | 0.5655 |

<!-- END_MONTE_CARLO_TABLE -->

The ratios \(\widehat{\mathbb ET}/n\) increase slowly. The ratios to \(n\log n\) still exhibit substantial finite-size variation. These data do not establish an asymptotic constant. Comparisons of finite-range fits are recorded in `data/fits.json`.

Fitting the means for \(100\leq n\leq10^6\), with weights equal to the inverse squared standard errors, gives the following. Residual sums are \(\sum_n((\widehat{\mathbb ET}_n-\text{fitted value})/\mathrm{SE}_n)^2\).

| Model | Fitted parameters | Weighted residual sum | Residual degrees of freedom |
|---|---|---:|---:|
| \(An\) | \(A=4.55661\) | 1644.32 | 7 |
| \(An\log n\) | \(A=0.753432\) | 3306.99 | 7 |
| \(An^\beta\) | \(A=3.07809,\ \beta=1.06600\) | 7.55 | 6 |
| \(n(A+B\log n)\) | \(A=2.69926,\ B=0.315417\) | 11.30 | 6 |

A small apparent power above one is therefore compatible with the proved logarithmic order over this finite range. The poor fit of a bare multiple of \(n\log n\) is a finite-range observation; (1) does not assert an asymptotic equivalent or control the lower-order term.

The source's Table 1 reports about 179.8 at \(n=100\) and 1800.0 at \(n=1000\); these differ from the present endpoint-time simulations, even after subtracting \(n\). For an immediate convention check, (6)'s exact formula gives \(1/f_{100}(10)\approx206.3\), whereas the matching-matrix diagonal already implies \(\mathbb ET\geq1/f_n(a)\) under the endpoint-time convention. The original simulation code has not been located, so the cause of this discrepancy is unresolved. The proof of (1) does not depend on those reported simulations.

For the range in Lemma 3, the independent simulations in `data/record_range.csv` give:

<!-- RANGE_TABLE -->

| m | Trials | Mean range | Standard error | Mean record visits | Mean range × log(m) / sqrt(m) |
|---:|---:|---:|---:|---:|---:|
| 100 | 30,000 | 4.6334 | 0.0173 | 8.4727 | 2.1337 |
| 1,000 | 20,000 | 11.6648 | 0.0563 | 25.4306 | 2.5481 |
| 10,000 | 10,000 | 31.4983 | 0.2160 | 80.7557 | 2.9011 |
| 100,000 | 2,000 | 88.7340 | 1.3763 | 258.2440 | 3.2305 |

<!-- END_RANGE_TABLE -->

These observations are consistent with (10); they are not used as a lower bound or as evidence for a limiting range constant.

The independent finite checks in `audit.py` cover 453 word/shift overlap cases, 43,968 path/endpoint instances of (13), the identity (11) at 100 times, and exact enumeration of the range inequality for \(m=1,\ldots,7\). Their outputs are saved in `data/audit.json`.

Reproduction commands, run serially from this directory:

```sh
clang++ -O3 -std=c++17 simulate.cpp -o simulate
./simulate check 8 2
OPENBLAS_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 python3 exact.py --max-n 12
python3 run_numerics.py
python3 audit.py
```

The queue simulation at the largest size allocates about 20 MB of arrays; the exact calculations have at most 624 automaton states. The calculations remain well below the requested 4 GB cap and use no worker pool.

## 7. Literature check and remaining questions

The supplied [arXiv paper](https://arxiv.org/abs/1411.0041) gives the \(n\) to \(n^{5/4}\) gap. The published chapter and Tang's thesis explicitly conjecture \(n\log n\), as cited above.

An OpenAlex citation query for the chapter DOI returned four records. They were the thesis and three papers: [*The Slepian zero set, and Brownian bridge embedded in Brownian motion by a spacetime shift*](https://doi.org/10.1214/EJP.v20-3911), [*The spans in Brownian motion*](https://arxiv.org/abs/1506.02021), and [*The argmin process of random walks, Brownian motion and Lévy processes*](https://arxiv.org/abs/1610.01524). The query results and the scope of the subsequent checks are saved in `data/openalex_citations.json` and `LITERATURE.md`. No later proof of this order was located in the checked sources or targeted searches. Citation-index coverage is incomplete; this is not a claim of an exhaustive novelty search.

The order gap posed in E0081 is closed by (1). What remains undetermined here is an asymptotic equivalent, in particular whether \(\mathbb ET_n/(n\log n)\) has a limit and, if so, its dependence on \(\lambda\). A limiting law for \(T_n/(n\log n)\) is also not proved.

Task: “determine the order of E T(FP_{lambda,n}) as n -> infinity (fixed lambda < 0)” — received 2026-11-13, approximately 00:41 Asia/Tbilisi.
