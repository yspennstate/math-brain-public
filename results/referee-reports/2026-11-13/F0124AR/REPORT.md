ACCEPT

The submitted partial theorem is correct: for independent fair two-colour scenery, the bilateral reduced process has an everywhere continuous conditional-probability version when $27/28<p\leq1$. I found no load-bearing error in the proof. In particular, its treatment of negative time, interval activities, independent domination, and the central-block swap is valid. This accepts the partial theorem, not a solution of Conjecture 2.16 or a claim of priority.

No printed statement of this particular bilateral bound was located in the literature search described below. That is a bounded search result. The published 2011 theorem explicitly concerns one-sided conditioning. The remaining bilateral good range $4/5<p\leq27/28$, the all-bad assertion for $1/2\leq p<4/5$, and the critical parameter are not resolved by the submission.

Errors or proof gaps requiring correction: none found. The numbered observations below record the limits that matter to the verdict.

1. **Sharpness is unestablished.** Location: submitted REPORT.md, equations (5), (8)–(11), numerical discussion, and final paragraph. The constant $27/28$ is sufficient. The data do not establish necessity, and the displayed continuity modulus is ineffective at the computed horizons. Fix if stronger claims are contemplated: do not describe $27/28$ as a transition or infer badness below it. The submission already observes this restriction.
2. **Priority is unverified.** Location: submitted REPORT.md, opening paragraph and literature section. Neither the citation search nor author bibliographies prove absence of prior results, including consequences of general regularity theorems. Fix: retain the explicit no-priority claim and report “not located,” rather than “new” or “never proved.” No change to the mathematical theorem is needed.
3. **The 2020 reference is not an independent bilateral theorem.** Location: submitted REPORT.md, reference 7. Steif's Question B is useful evidence that a phase diagram remained a research question, but its brief summary refers back to the 2011 paper without restating the conditioning convention. Fix: continue to use the 2011 paper's explicit definition to determine its scope. The submitted report does this; the 2020 contribution must not be used to upgrade that theorem to a bilateral statement.

The source definitions and setting were checked independently. Let $\Lambda_n=[-n,n]\cap\mathbb Z$, and, for a stationary sign-valued process $W$, set

\[
Q_m^\eta=P(W_0\in\cdot\mid W=\eta\text{ on }\Lambda_m\setminus\{0\}).
\]

The survey's definition, with all its quantifiers and its inequality unchanged, is

\[
\eta\text{ bad for }W_0
\iff
\exists\epsilon>0\ \forall n\in\mathbb N\ \exists m\in\mathbb N,
\ m\geq n,\ \exists\delta\in\{-1,+1\}^{\mathbb Z\setminus\{0\}}:
\quad \delta|_{\Lambda_n\setminus\{0\}}=\eta|_{\Lambda_n\setminus\{0\}},
\quad\|Q_m^\eta-Q_m^\delta\|_{\rm TV}\geq\epsilon.
\]

Good means the negation of this condition. The survey also states the version interpretation: every conditional-probability version is discontinuous at bad points, and a version exists continuous at all good points. This is stronger than an assertion merely about almost-sure convergence of finite conditional probabilities. [Survey, Section 2.6, printed p.60/PDF p.8](https://arxiv.org/pdf/math/0608219).

Conjecture 2.16 is exactly the following assertion, where $B_p$ is that bad set for the reduced process:

\[
\begin{gathered}
F=\{-1,+1\},\quad m_F(+1)=p,\quad m_F(-1)=1-p,
\quad p\in[1/2,1],\\
\frac12\leq p<\frac45\ \Longrightarrow
B_p=\{-1,+1\}^{\mathbb Z\setminus\{0\}},\\
\frac45<p\leq1\ \Longrightarrow\ B_p=\varnothing.
\end{gathered}
\]

It makes no assertion at $p=4/5$. The scenery is independent and fair by the default assumption on printed p.54/PDF p.2. Here $Y_t=C_{S_t}$, only $Y$ is conditioned on, time is indexed by $\mathbb Z$, and $S_t-S_{t-1}=X_t$. Thus the submission's bilateral setting is precisely the conjecture's setting. The adjacent Theorems 2.14–2.15 condition on the joint step-and-colour process $Z=(X,Y)$, which is a different observation. [Survey, pp.54,60–61; Conjecture 2.16 on PDF p.9](https://arxiv.org/pdf/math/0608219).

I audited the proof against the submitted file's line numbers. The following checks cover every step used by its continuity estimate.

| Submitted REPORT.md location | Independent check and result |
|---|---|
| Lines 13–24, 52–58 | Model, conditioning, support, and endpoint: correct. A monotone walk gives positive probability to every finite colour record. At $p=1$, $g_m=1/2$. |
| Lines 60–72, equation (1) | A positive cut is exactly a spatial edge crossed once to the right. Cutting at all such edges gives disjoint spatial ranges and a unique partition into vertex blocks. Interior blocks start at their minimum and end at their maximum. The first, last, and single whole-horizon block have exactly the stated relaxed restrictions. |
| Lines 74–83, equation (2) | If $d=L-2\ell\leq0$, $L\leq2\ell$. If $d>0$, every one of the $d$ separating spatial edges has net crossing +1. Without a cut it has a negative crossing, so $\ell\geq d$ and $L=d+2\ell\leq3\ell$. This applies to boundary blocks too. |
| Lines 87–101, equation (3) | The all-right likelihood is $B=p^{b-a}2^{-(b-a)}$, because exactly one observation is missing. Dividing a compatible word's likelihood by its reference gives $(q/p)^\ell2^{h-r}$. Repeated conflicting observations have zero weight. The unobserved colour is integrated out, not charged a spurious factor $1/2$. |
| Lines 103–120, equation (4) | With hole indicator $e$, $h=L+1-e$, $r\geq R-e$, and $R\geq\lvert d\rvert+1$. Consequently $h-r\leq L+1-R\leq L-d=2\ell$, including $d<0$. Thus $A_I\leq(4q/p)^\ell$. |
| Lines 123–137, equation (5) | Summing over all words with $\ell\geq\lceil L/3\rceil$ only enlarges the activity. The Chernoff parameter and every constant were re-derived below. |
| Lines 139–148, equation (6) | The exact partition function is a gas of disjoint nonsingleton vertex intervals. All unused vertices are singleton blocks of activity one; disjoint adjacent blocks are allowed. Boundary restrictions depend on whether an interval touches the horizon, not on its neighbours. Hence they are genuine local activities. The assembly bijection leaves no hidden interaction. |
| Lines 150–161, equation (7) | Under any feasible partial assignment of other interval indicators, deleting an occupied $I$ preserves that assignment and gives an injective map of weight ratio $w_I$. Its conditional odds are at most $w_I$, hence its conditional occupancy is at most $w_I/(1+w_I)$. For $w_I=0$, occupancy is zero directly. Sequential uniforms give domination by independent indicators, even though the actual gas indicators are dependent. |
| Lines 165–179, equation (8) | An $L$-step interval covers at most $L$ possible placements over a given edge. In each independent dominating family its vacancy probability is $1/(1+\rho^L)$. For two families the product is bounded below by $c=\exp[-2\rho/(1-\rho)^2]$. Candidate edges spaced $K+1$ apart involve disjoint sets of indicators of lengths at most $K$. Their short-interval vacancy events really are independent. |
| Lines 181–201, equations (9)–(10) | At most $r+L-1\leq r+L$ intervals of length $L$ intersect an $r$-edge interval. Union bounding long intervals in both families gives exactly the displayed factor 2 and tail. The geometric-series formula is correct. Finite-horizon omissions improve the estimate. |
| Lines 205–224, equation (11) | The marked-pair swap between nearest common cuts is legal, invertible, and product-weight preserving. Common cuts remain unchanged inside the swapped segment, so selection of the two cuts is invariant. The colour difference changes sign on the preserved event $G$, giving cancellation there. A union bound over the left and right intervals gives $2b_\rho$. |
| Line 226 | The tower-property argument gives uniform Cauchy convergence, not just pointwise martingale convergence. Its continuous limit is an exterior conditional-probability version, with the required continuity at every exterior. |

For completeness, the constant was recomputed without treating the submitted algebra as evidence. Put $t=4q/p$. For $z>1$,

\[
\begin{split}
w_I&\leq\sum_{\ell\geq\lceil L/3\rceil}\binom L\ell t^\ell\\
&\leq z^{-L/3}\sum_{\ell=0}^L\binom L\ell(tz)^\ell
=z^{-L/3}(1+tz)^L.
\end{split}
\]

The minimum of $\log(1+tz)-\tfrac13\log z$ occurs at $tz=1/2$. At $z=1/(2t)$,

\[
z^{-L/3}(1+tz)^L
=(2t)^{L/3}(3/2)^L
=(27t/4)^{L/3}
=\left(27q/p\right)^{L/3}.
\]

The assumption $p>27/28$ implies $t<4/27<1/2$, so this $z$ is allowed. Separately, $\rho=(27q/p)^{1/3}<1$ is equivalent to $27(1-p)<p$, hence exactly $p>27/28$. There is no reversed inequality, missing factor of two from the two arms, or unproved equality case. The general-colour extension at lines 228–234 also has the stated algebra: $t=q/(p\beta^2)$ gives $p>27/(27+4\beta^2)$; it is not needed for the fair-colour verdict.

Some individual estimates cannot be improved in isolation: the word $(+,-,+)^k$ has no positive cut, $L=3\ell=3k$, starts at its minimum and ends at its maximum. For a completely observed monochromatic block its duplicate count is $h-r=2\ell$. The loss in the displayed threshold includes counting every word with at least $L/3$ left steps, without enforcing the geometry. These facts explain where sharpening would have to enter; they do not identify the true threshold.

The negative-time issue was checked explicitly. Under the original anchoring,

\[
S_{-k}=-\sum_{j=-k+1}^{0}X_j,
\qquad E[S_{-k}]=-k(2p-1).
\]

The backward arm has negative drift. The proof instead reads the whole window in chronological order from $-m$ to $m$, after replacing $S_t$ by $S_t-S_{-m}$. Every chronological increment still has right-step probability $p$. Conditional on all increments, translating the independent scenery by the random integer $S_{-m}$ leaves its law unchanged. This proves the reanchoring argument; it does not assume conditional independence of past and future records. The two replicas used in the swap are independent samples of entire posterior walks, not the two arms of one walk. Changes in a swapped block's displacement merely translate later spatial blocks; their colour likelihoods are unchanged.

Here is the precise continuity conclusion. Define

\[
\omega_n=2\left[(1-c)^{\lfloor n/(\lfloor\sqrt n\rfloor+1)\rfloor}
+2\sum_{L>\lfloor\sqrt n\rfloor}(n+L)\rho^L\right]
\]

for $n\geq2$. The proof gives $|g_m(\eta)-g_m(\delta)|\leq\omega_n$ for every $m\geq n$ and every pair of records agreeing through radius $n$. Both terms tend to zero. Averaging over the outer observations gives $|g_m(\eta)-g_n(\eta)|\leq\omega_n$ everywhere. Therefore $g_m\to g$ uniformly and $g$ is continuous. Martingale convergence identifies $g$ almost surely with $P(Y_0=1\mid(Y_t)_{t\ne0})$. It also follows that

\[
\sup_{\eta=\delta\text{ on }\Lambda_n\setminus\{0\}}
|g(\eta)-g(\delta)|\leq\omega_n.
\]

Thus the result is good in the source's sense, including exceptional infinite records. As usual, this asserts existence of an everywhere continuous version; arbitrary modifications on null sets need not remain continuous.

Numerical checks used [code/independent_check.py](code/independent_check.py), written independently without reading, importing, or running any submitted code. One method integrates a full colour word by transfer over the current position and a tuple of visited spatial colours. Its integer weights share the denominator $2(2b)^N$ for $N$ steps and $p=a/b$: new-site visits multiply by the step numerator, matching revisits by twice that numerator. Filling the central hole with either colour gives exact likelihoods and their conditional ratio. Separate direct enumeration uses physical coordinates and pays $2^{-r}$ once for each observed site.

Every complete seven-time word at $p=0.97,0.9,0.5$ matched direct enumeration. Every punctured seven-time record at those three biases matched an independently evaluated interval partition sum: 576 exact comparisons altogether. Another 128 comparisons anchored at $S_0=0$, generated the two arms with opposite backward drift, and matched the chronological transfer probabilities. Colour-flip and $p\leftrightarrow1-p$ checks passed as well. Two hundred exact rational checks of the Chernoff inequality passed through $L=100$, including at the boundary $t=4/27$. Geometry was checked for all 32,767 step words through length 14 and their 58,474 blocks, with every possible hole location. Sixteen compatible marked pairs checked the swap and product-weight preservation explicitly. These are finite consistency checks; the proof supplies the infinite-volume result.

The main numerical experiment contains 96 exact rational values, saved in [data/finite_windows.csv](data/finite_windows.csv). Define the base record to be black everywhere outside zero. The WWBB alteration is also black for $0<|t|\leq n$, then has W,W,B,B repeating outwards separately on both sides. Selected results are:

| $p$ | $n$ | $m$ | $g_m$, all black | $g_m$, WWBB tails | Absolute difference |
|---|---:|---:|---:|---:|---:|
| 0.97 | 2 | 26 | 0.621846134846 | 0.555045871560 | 0.066800263287 |
| 0.97 | 4 | 28 | 0.621846365371 | 0.607739111078 | 0.014107254293 |
| 0.97 | 6 | 30 | 0.621846464628 | 0.618307455355 | 0.003539009273 |
| 0.90 | 2 | 26 | 0.866822527350 | 0.653846153846 | 0.212976373503 |
| 0.90 | 4 | 28 | 0.867586601979 | 0.768774703557 | 0.098811898422 |
| 0.90 | 6 | 30 | 0.868203495194 | 0.813793989616 | 0.054409505578 |

The CSV also includes all-white tails, black-past/white-future tails, and horizons $m=n,n+4,n+12$, with all fractions retained. As small exact examples, the black-record conditionals at $m=2$ are (12412681/21333362) for $p=0.97$ and (1801/2522) for $p=0.9$.

At $p=0.97$, $\rho=0.941682345038$ and $\log_{10}c=-240.501966101429$. At these horizons the rigorous modulus is larger than the trivial probability bound; apparent numerical agreement with a useful rate is impossible. At $p=0.9$, $\rho=\sqrt[3]{3}=1.442249570307$, so the summable-tail argument fails. The displayed gaps decrease with the inner radius for these particular records at both parameters. This is consistent with the accepted theorem at 0.97 and provides no counterexample at 0.9. It does not prove continuity at 0.9 or test the worst exterior. In particular it gives no numerical evidence that $27/28$ is sharp.

The final run used one process at nice 10, peaked at 33,156 transfer states and 53,706,752 bytes RSS (about 51.2 MiB), and took about 4.12 seconds. State and RSS checks enforce conservative limits. [data/check_summary.json](data/check_summary.json) records these measurements. Reproduce with `OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python3 code/independent_check.py` from this directory; no submitted-code dependency is involved.

The principal published comparison is Blachère, den Hollander and Steif, *A crossover for the bad configurations of random walk in random scenery*, Annals of Probability 39 (2011), 2018–2041. Section 1.1, journal p.2019/arXiv PDF p.2, explicitly restricts the paper to the one-sided version. Its Definition 1.1 conditions on positive times. Theorem 1.3, journal p.2022/arXiv PDF p.5, proves all-good near $(p,\varepsilon)=(1,0)$, all-bad for $1/2<p<4/5$ without holding, and coexistence at $p=1/2$ without holding. Conjecture 1.4 leaves the full one-sided good range conjectural. [Primary arXiv text](https://arxiv.org/pdf/1103.1780), [journal text](https://gup.ub.gu.se/file/66311).

Its exact no-holding sufficient parameter is

\[
p_*=\frac1{1+5^5/12^6}
=\frac{2985984}{2989109}=0.998954537957632\ldots.
\]

The paper's printed decimal “0.997” disagrees with its exact formula; the submitted report correctly uses the formula and the recomputed decimal. This is a source typo, not an error in the submitted proof. The one-sided coexistence example at $p=1/2$ is not by itself a counterexample to the bilateral conjecture.

The 2005 paper by den Hollander, Steif and van der Wal, *Bad configurations for random walk in random scenery and related subshifts*, SPA 115, 1209–1232, concerns joint-process conditioning. Section 1.2 expressly reserves $P(Y_0\in\cdot\mid(Y_t)_{t\ne0})$ for later work. Theorem 1.2 on preprint p.6 gives the bad-point/version correspondence; Theorem 1.3 on preprint p.7 classifies joint RWRS. Their $B(Y_0)$ notation does not mean that only colours were conditioned on. [Accessible author preprint, EURANDOM 2004-037](https://www.eurandom.tue.nl/reports/2004/037-report.pdf).

I searched literature dated 2006–13 November 2026 using exact titles, reduced RWRS, good/bad configurations, two-sided/bilateral, quasilocality, g-measures, and $T,T^{-1}$, and checked both survey DOI aliases. OpenAlex returned the same survey record for the two aliases, with 34 indexed citing works in this period. The 2011 paper's indexed forward citations added three candidates. The retrieved records and screening decisions are retained in data/. This is a citation-index search supplemented with primary-source searches and author lists, not a guarantee of complete coverage.

The relevant additional checks were:

- Gallo–Garcia, *Perfect simulation for locally continuous chains of infinite order* (2013), cites the survey and the 2005 paper as examples in its introduction. Its theorems concern conditional kernels for general one-sided chains, not the missing bilateral RWRS phase diagram. [Primary text](https://arxiv.org/abs/1103.2058).
- Steif–Tykesson, *Generalized Divide and Color Models* (2019), treats reduced RWRS as a colour process and gives the same stationary negative-time convention in Section 1.3.5. Remark 7.17 describes the 2011 result as a Gibbsianness transition, but supplies no new theorem or conditioning definition; Question 7.19 asks about Gibbsian properties more generally. This abbreviated reference cannot replace the 2011 paper's explicit one-sided convention. [Journal text](https://alea.math.cnrs.fr/articles/v16/16-33.pdf).
- Dolgopyat–Dong–Kanigowski–Nándori, *Mixing properties of generalized $T,T^{-1}$ transformations* (2022), and Pène–Saussol, *Quantitative recurrence for $T,T^{-1}$ transformations* (online 2024; PTRF 192 (2025), 1245–1282), cite the survey but address mixing/limit laws and return times. These are not uniform conditional-probability continuity theorems. [Primary mixing paper](https://arxiv.org/abs/2004.07298), [recurrence paper](https://link.springer.com/article/10.1007/s00440-024-01287-z).
- Verbitskiy, *On factors of g-measures* (2011), Theorem 1.1, p.317, assumes a continuous positive g-function with summable variation. No such input representation is established for reduced RWRS by merely calling it a factor. Moreover, one-sided continuity alone is insufficient for bilateral continuity: Fernández–Gallo–Maillard, *Regular g-measures are not always Gibbsian* (2011), Theorem 3.1, supplies a counterexample. Quantitative g-measure-to-Gibbs results require their extra hypotheses to be checked; this review does not certify novelty of the qualitative near-one statement or exclude narrower corollaries of such results. [Factor theorem](https://pure.rug.nl/ws/portalfiles/portal/2548757/2011IndagMathVerbitskiy.pdf), [counterexample](https://arxiv.org/abs/1106.4188).
- Maes–Redig–Van Moffaert (1999), Definitions/Propositions in Section 4, and Maes et al. (2000), Theorems 3.5–3.6, provide general discontinuity/weak-Gibbs formalism and intermittency examples. They do not prove an RWRS drift threshold. [1999 author text](https://fys.kuleuven.be/english/staff/christ/files/pdf/pub/1999/spa.pdf), [2000 author text](https://fys.kuleuven.be/english/staff/christ/files/pdf/pub/2000/verbit.pdf).
- Steif's Oberwolfach 2020 contribution, pp.632–633, Question B, still asks for the quasilocality phase diagram and cites the 2011 theorem. Its abbreviated wording does not change the explicit one-sided scope of that theorem. Den Hollander's publication list, now dated 12 November 2026, contains the 2011 crossover paper and yielded no later resolution in this search. [2020 report](https://publications.mfo.de/bitstream/handle/mfo/3731/OWR_2020_11.pdf?sequence=4), [current bibliography](https://pub.math.leidenuniv.nl/~hollanderwtfden/PublicationsFdH.pdf).

The value supported by this audit is an explicit sufficient bilateral range with a self-contained proof. The full crossover, the rest of the good half, and the all-bad half remain outside its result. The critical value $4/5$ is not covered by the original conjecture's assertion either. No source located supplies the submitted $27/28$ theorem, and no source inspected contradicts it. There is no basis here to advertise a completed solution or certified priority.

The survey, 2005 preprint, 2011 paper, and other downloaded sources are retained only as plain text in sources/. PDF bytes were processed in memory and never saved. The 2005 custom-font decoding retains explicit markers for unknown mathematical glyphs, rather than guessing them; its scope is independently confirmed by the survey and sequel. The Verbitskiy download returned HTTP 403, but its primary repository text was read through the web tool. No page images, scans, publication, or pushes were used.

Task: “You are an independent referee. … Break it if it is wrong.” — received 13 November 2026, approximately 07:45 Asia/Tbilisi; exact message time was not supplied.
