# Subsequence complete condensation for arbitrary zero-radius weights

Date: 17 September 2026. Source target: Janson Problem 18.40 (F0060).

**Status:** complete written proofs of Theorems A and B below, not independently audited. The unrestricted source problem remains **PARTIAL / OPEN** in this report. Independent end-to-end audits: **0/2**. Publication novelty: **UNVERIFIED**. This is an immutable direct-session contribution, not a change to a scheduled assignment or a shared results ledger.

## 1. Source question and precise contribution

Svante Janson, *Simply generated trees, conditioned Galton--Watson trees, random allocations and condensation*, Probability Surveys 9 (2012), 103--252, arXiv:1112.0510, Section 18.6, Problem 18.40, asks whether the largest box divided by the number of boxes can converge to zero throughout a sequence with positive limiting density and zero-radius weights. The displayed question and its neighboring sparse-support example were checked against PDF page 122 (one-based) of the arXiv source.

The allocation model is

$$
 Z(m,n)=\sum_{y_1+\cdots+y_n=m}\prod_{i=1}^n w_{y_i},
 \qquad
 \mathbb P_w(Y=y)=Z(m,n)^{-1}\prod_{i=1}^n w_{y_i},
$$

where one fixed sequence satisfies $w_0>0$, $0\le w_j<\infty$, and

$$
 \rho=0\quad\Longleftrightarrow\quad
 \limsup_{j\to\infty}w_j^{1/j}=\infty.
 \tag{1}
$$

Only pairs with $Z(m,n)>0$ are considered. Write $Y_{(1)}=\max_iY_i$. Multiplying every weight by $1/w_0$ changes no allocation law, so henceforth $w_0=1$.

### Theorem A: the tree case, with no further assumptions on the weights

For every fixed weight sequence satisfying (1), there is an increasing sequence of admissible integers $n_r$ for which

$$
 \frac{Y_{(1)}(n_r-1,n_r)}{n_r-1}
 \xrightarrow{\mathbb P}1.
 \tag{2}
$$

Consequently the limsup of $\mathbb E[Y_{(1)}(n-1,n)/n]$, over admissible $n$, is exactly $1$. The maximum outdegree of the corresponding simply generated plane tree has the same conclusion.

### Theorem B: bounded upward increments, at any positive finite density

Let $(n_j,m_j)$ be admissible pairs, with strictly increasing integer $n_j$, such that

$$
 n_j\to\infty,\qquad m_j/n_j\to\lambda\in(0,\infty),
 \qquad m_{j+1}-m_j\le L
 \tag{3}
$$

for one fixed finite integer $L\ge1$ and all sufficiently large $j$. Negative increments need not be bounded. Then there is a subsequence $j_r$ such that

$$
 \frac{Y_{(1)}(m_{j_r},n_{j_r})}{m_{j_r}}
 \xrightarrow{\mathbb P}1,
 \qquad
 \limsup_j\mathbb E\frac{Y_{(1)}(m_j,n_j)}{n_j}=\lambda.
 \tag{4}
$$

The support may be sparse or periodic. No full-support, ratio-growth, log-convexity, or regular-variation hypothesis is imposed. Standard lattice-adjusted totals with bounded rounding increments are covered.

The new mechanism is a polynomially penalized record tilt, followed by an upward-crossing argument that retains the small-box contribution. A finite collection of small boxes handles bounded overshoots. The resulting denominator is compared with a truncated exponential-moment bound, not with a single all-in-one-box configuration.

## 2. A one-sided truncation comparison

This point is essential when the chosen total $m$ is larger than the record size $k$.

Fix $k$ and $\tau>0$, and define

$$
 q_\ell=w_\ell\tau^\ell\quad(0\le\ell\le k),\qquad
 A=\sum_{\ell=0}^kq_\ell,\qquad p_\ell=q_\ell/A.
$$

Let $X_i$ be independent with law $p$, and put $S_n=\sum_{i=1}^nX_i$. For an integer $u<k$ and a positive truncated denominator,

$$
 \mathbb P_w(Y_{(1)}\le u)
 \le
 \frac{\mathbb P_p(S_n=m,\ \max_iX_i\le u)}
      {\mathbb P_p(S_n=m)}.
 \tag{5}
$$

Indeed, the original numerator uses only weights with index at most $u$, and is therefore unchanged by truncating at $k$. The original denominator is at least the truncated denominator. Multiplication by $\tau^m/A^n$ gives (5). In general there is **no equality** between the original conditional allocation and the truncated conditional iid law when $m>k$; weights above $k$ may be arbitrarily large. They only improve (5).

## 3. Proof of Theorem A

### 3.1. Record tilt

Fix $b>3$. For supported positive integers set

$$
 a_j=(j^bw_j)^{1/j}.
$$

By (1), the successive prefix-record values are unbounded. Along record indices $k$, set $\tau=a_k^{-1}$. Then $k\to\infty$, $\tau\to0$, and

$$
 q_\ell\le\ell^{-b}\quad(1\le\ell\le k),\qquad
 q_k=k^{-b}.
 \tag{6}
$$

Dominated convergence, applied to the sequences extended by zero beyond $k$, yields

$$
 A\to1,\qquad \mu:=\mathbb E_pX\to0,\qquad
 \mathbb E_pX^2\le V_b:=\sum_{\ell\ge1}\ell^{2-b}<\infty.
 \tag{7}
$$

Only the limsup in (1) was used. The individual weights need not increase.

### 3.2. Finding a bulk sum with sufficient probability

For the fixed auxiliary law at record $k$, use a single iid sequence and define

$$
 T_N=N-S_N,\qquad
 K=k+\lceil k\sqrt\mu\rceil+\lceil\sqrt k\rceil.
$$

Here $T_0=0$ and every upward increment of $T_N$ is at most one. Also $K/k\to1$. Markov's inequality gives

$$
 \mathbb P(T_K<k)
 \le\frac{K\mu}{K-k}\longrightarrow0.
$$

On the complementary event, this integer-valued path hits $k$ at some $N\in[k,K]$. Thus

$$
 \sum_{N=k}^{K}\mathbb P(S_N=N-k)\ge1-o(1).
$$

For all sufficiently large records there is a deterministic $N\in[k,K]$ with

$$
 \mathbb P(S_N=N-k)\ge\frac1{2k}.
 \tag{8}
$$

Set $m=N$, $n=N+1$. Then $m/k\to1$ and $n/k\to1$. In particular $m<2k$ eventually. The events that a specified coordinate is $k$ and the other $N$ coordinates sum to $N-k$ are disjoint for different specified coordinates. Therefore

$$
 \mathbb P_p(S_n=m)
 \ge n p_k\mathbb P_p(S_N=N-k)
 \ge c_0 k^{-b}
 \tag{9}
$$

with $c_0>0$ fixed. This also proves admissibility of the selected pairs. No assertion that $m$ visits every record integer has been made: the hitting argument deliberately allows $m=k+o(k)$.

### 3.3. Configurations with no nearly total box

Fix $c\in(0,1)$. Choose $b>3$ sufficiently large that $b(1-c)>2$, and then choose

$$
 b<a<(b-2)/c.
 \tag{10}
$$

The record construction above is performed with this fixed $b$. Put

$$
 s=a\log k/k,\quad J=\lfloor k/(\log k)^2\rfloor,\quad
 M_k=\mathbb E_p[e^{sX}\mathbf1_{\{X\le ck\}}].
$$

For $X\le J$, Taylor's inequality and $sJ\to0$ give the upper bound $1+s\mu+C s^2V_b$ after summation. For the remaining terms, (6) gives

$$
 \sum_{J<\ell\le ck}p_\ell e^{s\ell}
 \le C k^{ac+1-b}(\log k)^{2(b-1)}.
$$

Since $n=O(k)$ and $ac+2-b<0$,

$$
 n\log M_k\le n(M_k-1)=o(\log k)
 \quad\hbox{as an upper bound}.
$$

Exponential Markov's inequality and $m/k\to1$ now imply

$$
 \mathbb P_p(S_n=m,\ \max_iX_i\le ck)
 \le e^{-sm}M_k^n\le k^{-a+o(1)}.
 \tag{11}
$$

Combining (5), (9), and (11) proves

$$
 \mathbb P_w(Y_{(1)}\le ck)\le Ck^{b-a+o(1)}\longrightarrow0.
 \tag{12}
$$

For a prescribed $\varepsilon>0$, choose $c>1-\varepsilon$. Since $m/k\to1$, eventually $(1-\varepsilon)m\le ck$. Hence (12) gives infinitely many admissible pairs on which $Y_{(1)}/m>1-\varepsilon$ with probability approaching one. A diagonal choice for $\varepsilon=1/r$, with failure probability below $1/r$ and strictly increasing sizes, proves (2). The expectation assertion follows from $0\le Y_{(1)}/m\le1$.

### 3.4. Plane-tree interpretation

A plane tree with $n$ vertices has a depth-first outdegree sequence of total $n-1$. For any sequence of nonnegative integers of that total, exactly one of its $n$ cyclic rotations is a valid tree sequence: apply the usual minimum-of-partial-sums argument to the increments $y_i-1$, whose total is $-1$. The rotations are distinct, since a nontrivial period would force that total to be a multiple of an integer larger than one. Product weight and maximum coordinate are invariant under rotation. Grouping allocation sequences into these orbits shows that the maximum allocation coordinate has exactly the same law as the maximum simply generated tree outdegree. This establishes the tree conclusion without an asymptotic transfer assumption.

## 4. Finite supported reservoirs for Theorem B

First divide supported sizes and admissible totals by

$$
 d=\gcd\{\ell\ge1:w_\ell>0\}.
$$

The new weights still have zero radius, the density becomes $\lambda/d$, the upward-increment bound remains finite, and $Y_{(1)}/m$ is unchanged. It suffices to treat span one.

There is a finite subset of the positive support having gcd one. Its nonnegative additive semigroup contains every integer above a threshold $h$. For completeness, choose an element $a$ of that finite subset. The residues generated modulo $a$ form all of $\mathbb Z/a\mathbb Z$; a finite semigroup in a finite group is a subgroup. Choose a nonnegative representable integer in each residue class. Every larger integer with that residue is obtained by adding copies of $a$.

For each

$$
 r\in\{h,h+1,\ldots,h+L-1\},
$$

fix a representation by supported positive sizes, padding it with zeros to a common fixed number $B\ge1$ of coordinates. Write the chosen entries as $z_1(r),\ldots,z_B(r)$ and set

$$
 M=h+L,\qquad
 \gamma=\min_r\prod_{i=1}^B w_{z_i(r)}>0.
 \tag{13}
$$

All constants here are fixed before choosing records. Under any sufficiently small tilt with $A\le2$, the probability of this particular reservoir configuration is at least

$$
 \frac{\gamma\tau^r}{A^B}\ge\gamma 2^{-B}\tau^M.
 \tag{14}
$$

Zeros are allowed because $w_0=1$. This handles sparse support without assuming $w_1>0$.

## 5. Shifted records and the general denominator

Fix an integer $R\ge1$ and $b>3$, to be selected in Section 6. For supported $j>R$, use prefix records of

$$
 a_j=(j^bw_j)^{1/(j-R)}.
$$

Their values are unbounded by (1). At such a record $k$, set $\tau=a_k^{-1}$ and use the same truncated auxiliary law as in Section 2. Now

$$
 q_\ell\le\tau^R\ell^{-b}\quad(R<\ell\le k),\qquad
 q_k=\tau^Rk^{-b}.
 \tag{15}
$$

The finitely many indices at most $R$ have $q_\ell=w_\ell\tau^\ell$. Again

$$
 A\to1,\qquad\mu\to0,\qquad\mathbb E_pX^2\le V<\infty.
 \tag{16}
$$

For a common iid sequence with this auxiliary law, consider

$$
 T_j=m_j-S_{n_j-B-1}
$$

after discarding a finite initial segment where its subscript might be negative. Since $n_j$ is increasing and the $X_i$ are nonnegative,

$$
 T_{j+1}-T_j\le m_{j+1}-m_j\le L.
 \tag{17}
$$

At a first crossing of the integer level $k+h$, the value must therefore be $k+r$ for an $r$ in (13).

Here is a precise localization of that crossing. From (3), for each $\eta>0$ and all sufficiently large $j$,

$$
 (\lambda-\eta)n_{j+1}\le(\lambda+\eta)n_j+L.
$$

It follows that $n_{j+1}/n_j\to1$. For any fixed $\delta\in(0,1/2)$, let $j_+$ be the first index with $n_{j_+}\ge(1+\delta)k/\lambda$. Then

$$
 n_{j_+}=(1+\delta+o(1))k/\lambda,
 \quad m_{j_+}=(1+\delta+o(1))k,
 \quad\mathbb E S_{n_{j_+}-B-1}=O(k\mu)=o(k).
$$

Markov's inequality shows $T_{j_+}\ge k+h$ with probability tending to one. Conversely, all indices with $n_j\le(1-\delta)k/\lambda$ have $m_j<k+h$ for large $k$, and cannot have crossed, since $T_j\le m_j$. A deterministic diagonal choice of $\delta=\delta_k\downarrow0$ therefore puts the first crossing, with probability at least $1/2$, in a window whose indices satisfy

$$
 n_j/k\to1/\lambda,\qquad m_j/k\to1.
 \tag{18}
$$

The total number of indices in that window is at most $Ck$, since the $n_j$ are distinct integers. Taking the union over those indices and the fixed $L$ residuals, there must be a deterministic pair $(j,r)$ with

$$
 \mathbb P_p(S_{n_j-B-1}=m_j-k-r)\ge c_1/k.
 \tag{19}
$$

Choose this pair and abbreviate $n=n_j$, $m=m_j$. Eventually $m<2k$. At each of the $n$ possible giant-coordinate locations put $k$, put the prescribed reservoir of total $r$ in $B$ deterministic other coordinates, and let the remaining coordinates supply the bulk sum in (19). These $n$ events are disjoint because two coordinates equal to $k$ would exceed the total. Equations (14), (15), (18), and (19) give

$$
 \mathbb P_p(S_n=m)
 \ge c_2\tau^{R+M}k^{-b}.
 \tag{20}
$$

The small-box contribution has been retained explicitly. No unsupported lower bound on the weight of the single residual integer is needed.

## 6. A two-scale exponential bound

Fix $c\in(0,1)$. Choose fixed $b,R,a,v$ with

$$
 b>3,\quad b(1-c)>2,\quad R(1-c)>cM,
$$

and

$$
 b<a<(b-2)/c,\qquad R+M<v<R/c.
 \tag{21}
$$

Such parameters exist; in particular $R$ can be any sufficiently large integer. Construct the shifted records and selected pairs above using these parameters. Set

$$
 H=\log(1/\tau)\to\infty,\qquad
 s=(a\log k+vH)/k,\qquad
 M_k=\mathbb E_p[e^{sX}\mathbf1_{\{X\le ck\}}].
$$

We claim the upper bound

$$
 n\log M_k\le o(\log k+H).
 \tag{22}
$$

One must not assume $s\to0$, since $H$ can grow arbitrarily quickly.

**Case I: $H\le D\log k$**, where $D$ is a fixed constant chosen below. With $J=\lfloor k/(\log k)^2\rfloor$, Taylor's inequality below $J$ gives

$$
 M_k\le1+s\mu+C s^2V+
 C\tau^{R-vc}k^{ac+1-b}(\log k)^{2(b-1)}.
$$

Here $sJ\to0$. After multiplication by $n=O(k)$, the quadratic term tends to zero. The last term also tends to zero because $ac+2-b<0$ and $R-vc>0$. The linear term is $O(\mu(\log k+H))=o(\log k+H)$. This proves (22) in Case I.

**Case II: $H>D\log k$.** For the finitely many indices $1\le\ell\le R$, the inequality $e^x-1\le xe^x$, and $k>2v$, imply

$$
 n\sum_{\ell=1}^{R}p_\ell(e^{s\ell}-1)
 \le C(\log k+H)e^{-H/2}
 =o(\log k+H).
$$

Indeed, $\tau^\ell e^{vH\ell/k}\le e^{-H\ell/2}$ and $k^{a\ell/k}$ is bounded for these finitely many indices. For all remaining retained indices, (15) gives

$$
 n\sum_{R<\ell\le ck}p_\ell e^{s\ell}
 \le Ck^{1+ac}e^{-(R-vc)H}=o(1)
$$

provided $D>(2+ac)/(R-vc)$. Using $\log M_k\le M_k-1$ proves (22) in Case II as well.

By exponential Markov and (18),

$$
 \begin{aligned}
 \log\mathbb P_p(S_n=m,\ \max_iX_i\le ck)
 &\le-sm+n\log M_k\\
 &\le-a\log k-vH+o(\log k+H).
 \end{aligned}
 \tag{23}
$$

Divide by (20) and apply (5):

$$
 \log\mathbb P_w(Y_{(1)}\le ck)
 \le -(a-b)\log k-[v-(R+M)]H+o(\log k+H)
 \longrightarrow-\infty.
 \tag{24}
$$

Both displayed coefficients are strictly positive by (21). Finally choose $c>1-\varepsilon$, use $m/k\to1$, and diagonalize over $\varepsilon\downarrow0$, just as in Theorem A. This proves Theorem B. Restoring the lattice scaling preserves the maximum-to-total ratio. Boundedness by $m_j/n_j\to\lambda$ proves the expectation limsup in (4).

## 7. What this fixes, and what it does not prove

The earlier F0060 memo is preserved at

`probability_1000_attempts_I_20260914/Probability_F0060_Janson_problem_18_40_answered_no_2026-09-14.md`

with blob `05792fa2aaad98b3dfbf0acd4ce92e0f2f49c268`. The campaign INDEX and RANKING already withdraw its claimed closure. This report does not reuse its disputed mixed-configuration inequality.

The differences are mathematical, not a change of status terminology:

- Zero radius is used as a **limsup** condition, not a nonexistent limit of all supported roots.
- The denominator contains a random small-box bulk. It is not replaced by the weight of the exactly-one-occupied-box state.
- The hitting argument selects an admissible total near a record. It does not assert that an arbitrary total sequence visits every integer.
- The truncated iid law supplies a **one-sided** comparison, not a false conditional identity.
- The conclusion is $Y_{(1)}/m\to1$ along a subsequence, not $\mathbb P(Y_{(1)}=m)\to1$.

**Remaining source gap.** The hypothesis $m_j/n_j\to\lambda$ does not imply bounded upward increments. For example, $m_n=n+(-1)^n\lfloor\sqrt n\rfloor$ has density one and unbounded positive jumps. This is not a counterexample to condensation; it identifies a total sequence outside Theorem B. In that setting, the first-crossing overshoot can grow, and the finite reservoir proof does not supply a denominator strong enough for (24). Thus the arbitrary-total-path version of Problem 18.40 is not closed here.

No result for the positive-boundary-mean Problem 18.39 is claimed. The current sibling PROB20-20 report of 17 September at 08:29:46Z proves a different stretched-envelope/recursive-landing theorem and explicitly remains partial. Its hypotheses and conclusion are not relabeled as this contribution.

## 8. Exact computations and reproducibility

Run from this directory:

```bash
python3 check_condensation.py > checks.reproduced.json
cmp checks.json checks.reproduced.json
```

There are no third-party dependencies. All PASS assertions use integers or rational numbers. Decimal outputs are rounded displays; Boolean fields distinguish a rounded value of 1.0 from exact equality with one.

The checker independently compares a coefficient recurrence against repeated convolution in 24 finite cases, checks a finite shifted-record/reservoir/crossing certificate, verifies the strict parameter inequalities, and computes exact conditional allocation probabilities for full and sparse factorial weights. The coefficient recurrence is

$$
 m c_m=\sum_{j=1}^m((n+1)j-m)w_jc_{m-j},\qquad
 c_m=[z^m]\Big(\sum_jw_jz^j\Big)^n.
$$

It follows by equating coefficients in $F C'=nF'C$. Exact division is checked.

For full factorial weights, always using the correct tree total $m=n-1$:

| $n$ | $\mathbb P(Y_{(1)}\ge\lceil0.9m\rceil)$ | $\mathbb P(Y_{(1)}=m)$ |
|---:|---:|---:|
| 20 | 0.6297886205 | 0.3148943103 |
| 40 | 0.9628995588 | 0.3466635660 |
| 80 | 0.9999567765 | 0.3580513826 |
| 120 | 0.9999999922 | 0.3614766767 |

This directly illustrates why near-total condensation does not imply literal all-in-one-box concentration. For weights $w_k=k!$ supported on zero and the factorial integers, the probability in the middle column is exactly zero at $n=24$ and $n=120$, but is approximately $0.9999999551$ at $n=25$. At $n=121$ it rounds to 1.0 but is not exactly one. These observations illustrate oscillation; they do not prove the asymptotic theorems.

The synthetic rational reservoir certificate checks an upward-step bound of four, a shifted record envelope, the first-crossing union inequality, and the disjoint-giant denominator lower bound. It is not represented as a test of an infinite weight law.

Executed result: **ALL_EXACT_CHECKS_PASS**. Finite tests and self-review do not count as independent proof audits.

SHA-256 of the accompanying files:

```text
3e01930b1eae6f73631d878ede8fad455d0137d1ae1284e2a1e9c89278b1b4c4  check_condensation.py
e2b59fa7e74665ace332082d0dc69cf26ec43c219bd128502ed37aa72f664aa2  checks.json
```

## 9. Sources, prior-art boundary, and handoff

Primary references:

1. S. Janson (2012), *Simply generated trees, conditioned Galton--Watson trees, random allocations and condensation*, Probability Surveys 9, 103--252, DOI 10.1214/11-PS188, arXiv:1112.0510. Source question and allocation conventions; PDF page containing Problem 18.40 visually checked.
2. B. Stufler, *Local limits of large Galton--Watson trees rerooted at a random vertex*, arXiv:1611.01048v3 (8 February 2018), published in Annales de l'Institut Henri Poincare, Probabilites et Statistiques 55 (2019). The introduction distinguishes arbitrary type-III local large-degree behavior from complete-condensation regimes and discusses factorial-power weights. Its local-limit conclusions are not claimed as new here.
3. S. Janson, T. Jonsson, and S. O. Stefansson (2011), *Random trees with superexponential branching weights*, J. Phys. A 44, 485002, arXiv:1104.2810. Abstract and bibliographic record checked; full-text access attempts were unsuccessful in this session, so its complete theorem scope has not been cleared against Theorems A and B.

A bounded search on 17 September 2026 included exact Problem 18.40/18.39 searches and searches for superexponential-weight subsequence condensation. It did not locate a later exact resolution of the source question. That negative search is not a novelty certificate, and this report does not assert priority for Theorems A or B.

Repository evidence consulted: root POSTED, RESULTS and QUEUE; probability campaign INDEX and RANKING; intake F0059/F0060; the withdrawn F0060 memo; and the latest recovered sibling PROB20-20 recursive-reservoir report. No posted result was reassigned. No shared ledger, peer file, native schedule, or historical proof was edited.

Suggested ledger delta, **not applied to shared ledgers**:

```text
source: F0060 / Janson Problem 18.40
parent_status: PARTIAL / OPEN
contribution: complete written subsequence-condensation proofs for the tree total
              and all admissible bounded-upward-increment positive-density paths
weight_scope: every fixed nonnegative zero-radius sequence with w_0 > 0
restricted_metric: limsup E[Y_max/n] = lambda under Theorem B hypotheses
independent_audits: 0/2
novelty: UNVERIFIED
remaining_gap: arbitrary total paths with unbounded upward increments
checker: ALL_EXACT_CHECKS_PASS; finite evidence only
```

For an end-to-end audit, the key obligations are (5), the first-crossing localization (18)--(19), the disjoint events in (20), the two regimes in (22), and the fixed-parameter-then-diagonal order of quantifiers. The simple tree proof in Section 3 stands on its own and does not depend on the more elaborate reservoir extension.
