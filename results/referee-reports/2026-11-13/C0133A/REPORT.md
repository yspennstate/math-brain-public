PROVED

# C0133: zero speed on the event of non-transience

Yes. In the survey's full setting, including arbitrary infinite stacks, $X_n/n\to0$ almost surely on $N=\{|X_n|\not\to\infty\}$. In particular, $X_n\cdot\ell/n\to0$ there for every $\ell$. The proof below combines a finite-history bound at fresh hyperplanes with Zerner's deterministic counting argument. No published resolution in arbitrary dimension was identified in the search; dimension one was already settled in print.

## Exact setting and numbering

At visit $i$ to $x\in\mathbb Z^d$, the walk takes step $a\in E=\{\pm e_1,\ldots,\pm e_d\}$ with probability $\omega(x,a,i)$. Whole site stacks are iid. Every transition probability at every finite visit index is strictly positive almost surely. There is no uniform lower bound, drift-sign restriction, within-stack independence, or finite-stack assumption. Infinitely many non-placebo cookies per site are allowed.

With $P_0=\mathbb E[P_{0,\omega}]$ and $N=\{|X_n|\not\to\infty\}$, the question is whether

$$P_0\left(N\cap\left\{X_n\cdot\ell/n\not\to0\right\}\right)=0\qquad(\ell\ne0).$$

The downloaded [arXiv v2](sources/1204.1895.pdf) has Problem 4.7 on PDF page 19. The [journal version](sources/kosygina-zerner-2013-journal.pdf), *Bull. Inst. Math. Acad. Sin. (N.S.)* **8** (2013), 105–157, has the same number and hypotheses on PDF page 28, printed page 132. Download addresses and SHA-256 hashes are in [manifest.json](sources/manifest.json).

## Literature first

Amir–Berger–Orenshtein, *Zero–one law for directional transience of one dimensional excited random walks*, *Ann. Inst. H. Poincaré Probab. Statist.* **52** (2016), 47–57, [DOI 10.1214/14-AIHP615](https://doi.org/10.1214/14-AIHP615), [arXiv:1304.7287v2](sources/1304.7287.pdf), Theorem 1.3, proves a deterministic speed for stationary ergodic elliptic stacks on $\mathbb Z$, including infinite stacks. Returns to one fixed site force this speed to be zero on $N$. Thus the one-dimensional part is already in print; this is not a resolution for arbitrary $d$.

Zerner, *A non-ballistic law of large numbers for random walks in i.i.d. random environment*, *Electron. Commun. Probab.* **7** (2002), 191–197, [DOI 10.1214/ECP.v7-1060](https://doi.org/10.1214/ECP.v7-1060), [PDF](sources/zerner-2002.pdf), Theorem 1, handles iid RWRE without coordinate transience. Its deterministic Lemma 3 is the counting input below. Its original strong Markov restart cannot simply be applied to the position of a cookie walk.

The forward-citation search queried both OpenAlex survey records, restricting publication dates to 2012-01-01 through 2026-11-13. It returned 37 and 23 records, or 45 distinct work IDs after merging; some represent duplicate versions. Raw JSON and the [merged TSV](sources/openalex-citations.tsv) are saved. The index is incomplete: these counts describe coverage, not bibliographic completeness. Keyword searches also covered the exact problem number, non-transient/nontransient/non-transience, recurrent-event speed, infinite stacks, and LLN through 2026. No general resolution in print was identified. The results screened are listed below.

## Reduction and the finite-cookie issue

Pathwise,

$$N=\bigcup_{x\in\mathbb Z^d}\{X_n=x\text{ infinitely often}\}.$$

Indeed, a path which fails to leave every finite ball revisits some finite ball infinitely often, hence revisits one vertex infinitely often. In particular $\liminf |X_n|/n=0$ on $N$. Any limiting speed must be zero there; existence of that limit is the issue.

If every site has finitely many non-placebo cookies, every directed neighbor-transition sum is infinite. Conditional Borel–Cantelli propagates infinite visits to each neighbor and then to every site. Each fixed finite box is eventually exhausted on $N$ and has simple symmetric departure transitions. This does not imply simultaneous exhaustion everywhere or control excursions outside that box. The proof below supplies the missing frequency argument and does not require finite cookies.

Mere ellipticity does allow finite trapping. For example, in $d=2$ give each site an iid uniform mark $a\in E$. Its $i$th cookie gives probability $1-3\varepsilon_i$ to $a$ and $\varepsilon_i=2^{-i-4}$ to each other neighbor. With positive probability the marks at $0,e_1$ point toward each other and every departure follows its mark. The corresponding infinite product is positive. This iid elliptic infinite-stack law has positive probability of permanent two-site alternation, which has speed zero. It is not a counterexample. Under EL alone, recurrence must not be identified with visiting every site infinitely often.

## Proof

Put $A_u=\{X_n\cdot u\to+\infty\}$. We use the survey's range dichotomy (Theorem 2.5), half-space/slab assertion (Lemma 3.18), and Kalikow-type zero-one law (Theorem 3.16).

### A. One-sided paths

In the almost surely infinite-range case, Lemma 3.18, applied to $-e$ for a coordinate $e$, implies

$$P_0\{\inf_n X_n\cdot e>-\infty,\ X_n\cdot e\not\to+\infty\}=0. \tag{1}$$

For a direct check, on this event choose integers $a<b$ such that the coordinate is always at least $a$ and is at most $b$ infinitely often. The reflected version of Lemma 3.18 excludes each such event; take a countable union.

### B. Keep each finite consumption history

Fix $e=e_1$ and suppose $P_0(A_e)=0$. The almost surely finite-range case already has zero speed, so suppose the range is almost surely infinite.

For an integer $c\ge0$, let $\Pi_c$ be the finite collection of nearest-neighbor paths $p=(p_0,\ldots,p_s)$, where $p_0=0$, $s\le c$ and $p_s\cdot e=0$. Write

$$k_p(x)=\#\{0\le t<s:p_t=x\},\qquad
\omega^p(x,a,i)=\omega(x,a,i+k_p(x)).$$

Only departures in the prefix have consumed instructions; the endpoint's next instruction has not been consumed. For $L>c$, set

$$q_L^p(\omega)=P_{p_s,\omega^p}\{T_L<D\},$$

where times restart at $p_s$, $T_L=\inf\{n\ge0:X_n\cdot e=L\}$, and $D=\inf\{n\ge1:X_n\cdot e\le0\}$. A successful path first steps strictly right of the initial hyperplane and stays there until reaching $L$. Thus $q_L^p$ depends only on original stacks in $\{x\cdot e\ge0\}$, even if $p$ had negative-coordinate steps.

As $L$ increases these probabilities decrease to $q_\infty^p$, the probability of staying strictly right and reaching all positive levels. Let $w_p(\omega)$ be the quenched probability of following the finite prefix $p$ from the pristine environment. Ellipticity gives $w_p>0$ almost surely. Concatenating $p$ with the event defining $q_\infty^p$ produces a path bounded below in coordinate $e$; by (1) it is in $A_e$ up to a null event. Therefore

$$0=P_0(A_e)\ge\mathbb E[w_pq_\infty^p],\qquad
q_\infty^p=0\quad\mathbb P\text{-a.s.} \tag{2}$$

Bounded convergence and finiteness of $\Pi_c$ give

$$a_L(c):=\sum_{p\in\Pi_c}\mathbb E[q_L^p]\longrightarrow0. \tag{3}$$

This retains the consumed prefix exactly. It asserts no absolute continuity between original and shifted infinite-stack laws.

### C. Conditional bound at a new hyperplane

For $m\ge0$ let $T_m=\inf\{n\ge0:X_n\cdot e=m\}$ and

$$I_{m,L}=\{n:T_m\le n<T_{m+L},\ X_n\cdot e=m\}.$$

When $T_{m+L}<\infty$, put $h_{m,L}=\max I_{m,L}-T_m$; otherwise put $h_{m,L}=\infty$. Let

$$B_{m,L,c}=\{T_{m+L}<\infty,\ h_{m,L}\le c\},\qquad
\mathcal F_n=\sigma(X_0,\ldots,X_n).$$

We claim

$$P_0(B_{m,L,c}\mid\mathcal F_{T_m})\le a_L(c)
\quad\text{on }\{T_m<\infty\}. \tag{4}$$

At first arrival at level $m$, no stack in $\{x\cdot e\ge m\}$ has supplied a step, so its iid law is unchanged and independent of the preceding path. Translate $X_{T_m}$ to $0$. On $B_{m,L,c}$ the last visit to level $m$ before $T_{m+L}$ occurs at $T_m+s$, $s\le c$. The translated prefix up to that visit belongs to $\Pi_c$. Its remaining chance of reaching $m+L$ before returning to the hyperplane is $q_L^p$ in the fresh half-space with exactly that prefix consumed. Conditional on the environment, the prefix probability is at most 1. Sum over the finitely many prefixes and average over the fresh half-space to obtain (4). Prefix probabilities may depend on both the fresh and the old half-space; dropping these factors requires no independence between them.

More formally, fix any finite path history $\eta$ ending at its first visit to level $m$, with endpoint $x$. Conditional on $\eta$ and the full environment, let $W_\eta^p$ be the probability of the next prefix $p$. Since $L>c$, no such prefix has already reached level $m+L$. Partition $B_{m,L,c}$ by its unique last visit to level $m$. This gives the exact finite-sum factorization

$$P_0(B_{m,L,c}\mid\eta,\omega)=
\sum_{p\in\Pi_c}W_\eta^p(\omega)\,q_L^p(\theta_x\omega),$$

where $(\theta_x\omega)(z,a,i)=\omega(x+z,a,i)$ and only its pristine nonnegative half-space is used in $q$. Pointwise, $0\le W_\eta^p\le1$. Under $P_0(\,\cdot\mid\eta)$ that half-space retains its original law, because the likelihood of $\eta$ contains departure probabilities only from sites strictly left of level $m$. Integrating proves (4), without conditioning the fresh stacks on the post-arrival prefix.

### D. The frequency bound

Fix $c,L$ and a residue $r\in\{0,\ldots,L-1\}$. Set $m_k=r+kL$, $\mathcal G_k=\mathcal F_{T_{m_k}}$, and $Z_k=1_{B_{m_k,L,c}}$. The variable $Z_k$ is $\mathcal G_{k+1}$-measurable. Hence $Z_k-E_0[Z_k\mid\mathcal G_k]$ is a bounded martingale difference. Azuma followed by Borel–Cantelli, or the martingale strong law, gives

$$\limsup_K\frac1K\sum_{k<K}Z_k\le a_L(c)\quad P_0\text{-a.s.}$$

If a hitting time is infinite, its stopped sigma field is $\mathcal F_\infty$ and all subsequent $Z_k$ are zero, which covers that case as well. Combine residue classes and intersect over the countably many $(c,L)$ to obtain, simultaneously,

$$\limsup_M\frac1{M+1}\sum_{m=0}^M1_{B_{m,L,c}}\le a_L(c). \tag{5}$$

### E. Deterministic counting

Here is a proof of the path ingredient, equivalent to Zerner (2002), Lemma 3. Suppose a nearest-neighbor path $x_n$ has positive $\limsup x_n\cdot e/n$. There are $\delta>0$ and $n_k\to\infty$ with $x_{n_k}\cdot e\ge\delta n_k$. Put $M_k=\lfloor\delta n_k/2\rfloor$, $C=3/\delta$. All coordinate hitting times are finite. For every fixed $L$, eventually $T_{M_k+L}\le n_k$ and

$$\frac1{M_k+1}\sum_{m\le M_k}\#I_{m,L}\le C,\qquad
\frac1{M_k+1}\sum_{m\le M_k}h_{m,L}\le CL. \tag{6}$$

The first counts disjoint sets of times before $n_k$. For the second, use $h_{m,L}\le T_{m+L}-T_m$ and telescope over residue classes modulo $L$.

Set $F_{M,L}(c)=(M+1)^{-1}\sum_{m\le M}1_{\{h_{m,L}\le c\}}$. We must have

$$\text{some integer }c\text{ with }\inf_L\limsup_M F_{M,L}(c)>0. \tag{7}$$

Otherwise choose an integer $q>2C$ and $L_0=1$. Given $L_i$, put $c_i=\lceil4CL_i\rceil$ and choose $L_{i+1}>L_i$ with $\limsup_M F_{M,L_{i+1}}(c_i)<1/4$. This is possible because the asserted infimum is zero and $F$ decreases in $L$. By (6), along $M_k$ at most $1/4$ of the levels have $h_{m,L_i}\ge c_i$, and eventually fewer than $1/4$ have $h_{m,L_{i+1}}\le c_i$. More than half therefore have $h_{m,L_i}<h_{m,L_{i+1}}$. Each strict increase adds at least one visit to level $m$. Sum over $i<q$ to get

$$\frac1{M_k+1}\sum_{m\le M_k}\#I_{m,L_q}>q/2>C,$$

contrary to (6). This proves (7).

On a sample path with positive limsup coordinate speed, all $T_m$ are finite, so (5) bounds the $F$ in (7). Equations (3) and (5) force $\inf_L\limsup_M F_{M,L}(c)=0$ for every $c$, a contradiction. We have proved

$$P_0(A_e)=0\ \Longrightarrow\
P_0\{\limsup_n X_n\cdot e/n>0\}=0. \tag{8}$$

Reflection gives the corresponding lower bound when $P_0(A_{-e})=0$.

### F. Apply the zero-one law

If $P_0(N)=0$, the requested assertion is immediate. Otherwise, for every coordinate $e_j$, the inclusion $N\subseteq(A_{e_j}\cup A_{-e_j})^c$ and Theorem 3.16 imply $P_0(A_{e_j}\cup A_{-e_j})=0$. Apply (8) in both signs of every coordinate. Then $X_n/n\to0$ almost surely, hence on $N$, and taking its scalar product with $\ell$ proves the assertion. The almost surely finite-range case was covered directly.

This covers finitely many cookies per site almost surely, without a deterministic bound or moment assumption, as well as infinite persistent or alternating stacks. No case of Problem 4.7 is left over. It does not assert a recurrence/transience dichotomy in arbitrary dimension or resolve the general directional zero-one problem for $A_\ell$ alone.

## Proof audit and numerical checks

The load-bearing points were checked separately:

- The concatenation in (2) uses a strictly positive finite path likelihood; it needs no uniform bound and makes no comparison between infinite stack laws.
- The fresh-region factorization was derived again by conditioning on a fixed finite pre-arrival history, as displayed above. The prefix has bounded length because $h_{m,L}$ measures elapsed time from the first hyperplane arrival, rather than just counting visits.
- The martingale uses the original annealed law, not a law conditioned on future recurrence. Its indicator is measurable at $T_{m+L}$, so residue classes modulo $L$ give the required adapted sequence. Infinite hitting times are explicitly covered.
- Both sums in (6) were rederived by counting disjoint visits and telescoping hitting times. [code/checks.py](code/checks.py) checked them on 100 finite paths and four slab widths (400 cases), including the strict-growth implication.
- [code/check_prefix.py](code/check_prefix.py) exhaustively enumerated finite paths through time 8 for three cookie laws, $c=0,1,2$, and two left-half-space histories: pristine or with 17 prior departures per site. All 18 cases agreed between direct enumeration and the weighted prefix factorization, within $1.12\times10^{-16}$. Every unweighted bound held. These finite checks test bookkeeping; the infinite-horizon argument is (1)–(8).

The simulations used four deterministic site-stack laws on $\mathbb Z^2$ (hence degenerate iid environments). At visit $i$, probabilities of $+e_1,-e_1,+e_2,-e_2$ were $((1+\beta_i)/4,(1-\beta_i)/4,1/4,1/4)$:

- Simple: $\beta_i=0$.
- Finite two: $\beta_1=0.8$, $\beta_2=-0.8$, then zero.
- Infinite periodic: $\beta_i=0.8(-1)^{i-1}$.
- Infinite blocks: $\beta_i=0.8(-1)^{\lfloor\log_2 i\rfloor}$.

Each had 64 independent runs of 65,536 steps. The return event below means a visit to the origin between times 32,768 and 65,536, inclusive. It is a finite-horizon observable, not an estimator of the infinite recurrence event $N$.

| Law | Runs with late return | Frequency (95% Wilson interval) | Longest completed origin excursion | Median unfinished excursion length at cutoff | Largest $|X_n\cdot e_1|/n$ during second half |
|---|---:|---:|---:|---:|---:|
| Simple | 1/64 | 0.0156 (0.0028–0.0833) | 45,852 | 65,459 | 0.0110 |
| Finite two | 0/64 | 0 (0–0.0566) | 304 | 65,536 | 0.1058 |
| Infinite periodic | 0/64 | 0 (0–0.0566) | 452 | 65,536 | 0.1770 |
| Infinite blocks | 0/64 | 0 (0–0.0566) | 398 | 65,536 | 0.1065 |

These runs neither exhibit nor exclude infinite recurrent paths with large finite excursions. In particular, a visibly nonzero displacement at this cutoff is not a counterexample to the theorem on $N$.

For the explicit iid elliptic trapping construction above, the probability of the specified $0,e_1$ alternating event is

$$p=\frac1{16}\prod_{i\ge1}(1-3\cdot2^{-i-4})^2
 =0.04242660227895439\ldots>0.$$

The product was evaluated by direct multiplication and independently by summing logarithms. Among 20,000 independent trials, 1,274 had the required mark pair and 845 followed it for 80 departures at each site: frequency 0.04225, Wilson interval 0.03955–0.04513. Given this finite alternating prefix, the probability of any later deviation is at most $6\cdot2^{-84}<3.11\times10^{-25}$. On permanent alternation all completed origin excursions have length 2 and peak distance 1, so the speed is zero. This checks a construction allowed by the precise EL setting; it is not a construction against the claimed limit.

Raw per-run data, every completed excursion, summaries, seeds, and prefix-check results are in [data/](data/). Reproduce with `python3 code/check_prefix.py` and `python3 code/checks.py`. The simulation used one process at inherited nice 15, no numerical-library workers, and peak RSS 47,841,280 bytes (about 45.6 MiB), well below 4 GB. Nice 15 is more yielding than the requested nice 10; the process did not raise its inherited priority. The scientific conclusion rests on the proof, not these finite runs.

## Other literature screened

| Work | Scope |
|---|---|
| Survey, Section 4 | Lemma 4.5 and Theorem 4.6 give regeneration and speed on $A_\ell$; Theorem 4.8 explicitly adds directional-transience assumptions because of Problem 4.7. |
| Holmes, *Excited against the tide*, AIHP 48 (2012), 745–773; [0901.4393](sources/0901.4393.pdf) | Competing drifts and high-dimensional cut-time LLN with simple transverse coordinates. |
| Holmes–Salisbury, *Random walks in degenerate random environments*, Canad. J. Math. 66 (2014), 1050–1077; [1105.5105](sources/1105.5105.pdf) | Theorems 1.3–1.5 concern zero-one laws and regeneration for RWRE, whose stacks are constant in the visit index. |
| Holmes–Salisbury, *A combinatorial result with applications to self-interacting random walks*, JCTA 119 (2012), 460–475; [1105.5157](sources/1105.5157.pdf) | Arrow-system comparisons, mainly in dimension one. |
| Menshikov–Popov–Ramírez–Vachkovskaia, *On a general many-dimensional excited random walk*, Ann. Probab. 40 (2012), 2106–2130; [1001.1741](sources/1001.1741.pdf) | Theorems 1.1–1.2 give positive speed with uniformly positive first-visit drift, zero drift on revisits, and ellipticity/bounded jumps. Their class has $P_0(N)=0$. |
| Zerner, *Recurrence and transience of excited random walks on $\mathbb Z^d$ and strips*, ECP 11 (2006), 118–128; [math/0601233](sources/math-0601233.pdf) | Nonnegative directional drift and uniform ellipticity; not arbitrary-sign stacks. |
| Bérard–Ramírez, *Central limit theorem for the excited random walk in dimension $d\ge2$*, ECP 12 (2007), 303–314; [0705.0658](sources/0705.0658.pdf) | Theorem 1 treats the original once-excited model, renewal LLN/CLT and positive speed. |
| Kozma, problem session, *Non-Classical Interacting Random Walks*, Oberwolfach Rep. 4 (2007), p. 1552; [PDF](sources/oberwolfach-2007-27.pdf) | Origin-directed and history-dependent H/Y models, outside iid site stacks. |
| van der Hofstad–Holmes, *Monotonicity for excited random walk in high dimensions*, PTRF 147 (2010), 333–348; [0803.1881](sources/0803.1881.pdf); *An expansion for self-interacting random walks*, Braz. J. Probab. Stat. 26 (2012), 1–55; [0706.0614](sources/0706.0614.pdf) | Lace expansion, LLN/CLT and speed regularity in special high-dimensional regimes. |
| Amir–Orenshtein, *Excited Mob*, SPA 126 (2016), 439–469; [1307.6052](sources/1307.6052.pdf) | Theorem 4.3 gives a one-dimensional LLN using hitting times. |
| Kosygina–Peterson, *Excited random walks with Markovian cookie stacks*, AIHP 53 (2017), 1458–1497; [1504.06280](sources/1504.06280.pdf) | Infinite Markovian stacks on $\mathbb Z$; Theorem 1.4 uses the one-dimensional LLN. |
| Kozma–Orenshtein–Shinkar, *Excited random walk with periodic cookies*, AIHP 52 (2016), 1023–1039; [1311.7439](sources/1311.7439.pdf) | Infinite periodic stacks in dimension one. |
| Pham, *Monotonicity and regularity of the speed for excited random walks in higher dimensions*, EJP 20 (2015), paper 72; [1311.6158](sources/1311.6158.pdf) | Theorem 1.1 gives LLN for $d\ge6$ with simple transverse coordinates and exchangeability. |
| Letterhos, *Recurrence/Transience criteria for excited random walks with finite-drift cookie stacks*; [2103.05570](sources/2103.05570.pdf) | Identically piled infinite stacks on $\mathbb Z$, with finite total drift. |
| Santos, *An excited random walk counter-example*, DOI 10.1007/s40863-021-00214-7; [1909.03159](sources/1909.03159.pdf) | Zero speed despite an infinite mean cookie count in a one-dimensional ergodic environment; not a counterexample here. |
| Alves–Iacobelli–Valle, *Generalized Many-Dimensional Excited Random Walk in Bernoulli Environment*, [2201.10666](https://arxiv.org/abs/2201.10666) | Withdrawn in v3 (24 March 2023); the current PDF endpoint is absent. Not used as a theorem. |
| Singh, *A shape theorem for a radially excited random walk in dimensions $d\ge2$*, [2610.12138](https://arxiv.org/abs/2610.12138); Bou-Rabee–Nguyen–Peres–Singh, *Limit shapes for centrally excited walks*, [2610.10162](https://arxiv.org/abs/2610.10162) | October 2026 preprints, the first superseded by the second. Origin-directed first-visit drift depends on position and falls outside IID. |

Task: “Open problem C0133.” Asked 2026-11-13 04:36, Asia/Tbilisi.
