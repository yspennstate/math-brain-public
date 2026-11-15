ACCEPT

The argument in `claim_files/REPORT.md` proves the stated assertion under exactly (IID) and (EL), including arbitrary infinite stacks. I found no substantive mathematical error after checking the conditional laws, the source lemmas, the counting argument, and the last zero-one-law reduction. In fact, the argument proves zero vector speed on the non-transient event. The twenty-minute provenance warrants scrutiny but does not supply a mathematical objection.

This is essentially Zerner's 2002 method transferred to cookie walks. The finite consumption-history estimate is the new ingredient; the deterministic counting lemma is already in print. Dimension one is already covered by Amir–Berger–Orenshtein (2016). I did not find a published resolution for arbitrary dimension in the primary literature examined through 13 November 2026. That is a qualified literature finding, not a certificate of priority.

Numbered error/gap list:

1. No substantive error or missing hypothesis was found. No mathematical repair is required.
2. Minor clarification, submitted report lines 102–108: explicitly write $L>c$, the domain used in the finite-history estimate. The limiting argument uses arbitrarily large $L$ for each fixed $c$, so omitting the finitely many smaller widths changes nothing. I read this domain restriction as inherited from lines 58–60, rather than as an assertion of an estimate at undefined parameters.
3. Minor clarification, line 112: “all coordinate hitting times” means the nonnegative levels $T_m$ in the chosen coordinate. Positive limsup does not imply hitting every negative level. Every hitting time used in the proof has the required nonnegative index.

What follows records the verification, including attacks that did not produce a gap. Line numbers refer to the submitted report, whose SHA-256 is `9e11361b10c86d17f67e9e5369d886305e385009935fa84d4bc3ae30c3784bfb`.

1. Exact question and assumptions, lines 7–15.

   I downloaded [arXiv:1204.1895v2](https://arxiv.org/pdf/1204.1895), the [journal survey](https://www.math.sinica.edu.tw/bulletins/20131/2013106.pdf), and [Zerner (2002)](https://www.maths.tcd.ie/EMIS/journals/EJP-ECP/article/download/1060/1060-3485-1-PB.pdf) independently into `sources/`, and read the relevant statements with their surrounding arguments. Problem 4.7 is on arXiv PDF page 19 and journal printed page 132, PDF page 28. The event has a complement: $N=\{|X_n|\to \infty \}^{c}$.

   The model is nearest-neighbor on $\mathbb Z^d$. Independence and identical distribution apply to entire site stacks $(\omega (x,a,i))_{a,i}$, indexed by $x$. EL requires every direction probability at every finite visit index to be positive almost surely. Countability makes these positivity statements simultaneous on a full-measure set. There is no lower bound uniform in site or visit index, no independence within a stack, no eventual-placebo requirement, and no moment or drift-sign assumption. The submitted theorem respects this class.

   The surrounding survey distinguishes regeneration and an existing directional LLN on $A_\ell$ from the unanswered behavior on $N$. Theorem 4.8 retains extra directional-transience assumptions because of this problem. The nearby discussion of whether regeneration times have finite mean concerns positivity of speed on directional escape; it is not an explanation of the difficulty of Problem 4.7. The survey does not give a specific failed proof of 4.7. The relevant obstruction in transferring the older proof is that position alone no longer determines the future law.

2. Non-transience reduction, lines 27–35.

   Pathwise, $N=\bigcup_{x\in\mathbb Z^d}\{X_n=x\text{ infinitely often}\}$. Failure to tend to infinity means that some fixed finite ball is visited infinitely often; one of its finitely many vertices is then visited infinitely often. The converse is immediate. Thus the liminf of the norm divided by time is zero on $N$. This alone proves neither existence of the speed nor a bound on its limsup.

   The report correctly distinguishes finite-cookie exhaustion in each fixed recurrent box from control of excursions outside that box. It also correctly avoids propagating recurrence to all sites under EL alone. Its summable-error two-site trapping example is admissible. I recomputed its probability both by multiplication and by summing logarithms: (0.04242660227895439). This agrees with the reported value.

3. Published inputs and their hypotheses, lines 39–47 and 138.

   Survey Theorem 2.5 assumes IID and EL and gives an almost-sure finite-range/infinite-range dichotomy for the environment law. In the finite-range case speed is trivially zero. It is therefore legitimate to handle the infinite-range case separately without conditioning the environment law on the event $N$.

   Survey Lemma 3.18 assumes IID, positive expectations of all first-cookie direction probabilities, and almost-sure infinite range. EL implies the required positive expectations. For $u<w$, it rules out infinitely many visits with $X_n\cdot \ell \ge  u$ while all positions satisfy $X_n\cdot \ell \le  w$. Apply it to $-e$, with $u=-b,w=-a$, and take the countable union over integer $a<b$. This proves equation (1): a coordinate bounded below must tend to $+\infty$, outside a null event. No UEL assumption enters. I also read the lemma's proof, including its treatment of finitely many repeatedly visited slab sites; it does not assume every neighboring transition sum diverges.

   Survey Theorem 3.16 assumes IID and EL and gives $P_0(A_e\cup  A_{-e})\in\{0,1\}$. It does not assert the individual directional zero-one law $P_0(A_e)\in\{0,1\}$, which the submitted proof does not use.

4. Finite-prefix consumption and change of law, lines 53–73.

   The definition $k_p(x)=\#\{t<s:p_t=x\}$ counts departures, including earlier visits to the endpoint, while leaving the cookie for its next departure unconsumed. This is the right residual environment. There are finitely many possible paths of length at most a fixed $c$, including transverse moves and excursions into the old half-space.

   For each fixed $p$, the original quenched probability $w_p$ of that finite prefix is strictly positive by EL. No uniform lower bound is needed. Concatenating $p$ with the continuation defining $q_\infty ^p$ gives a coordinate-bounded-below path. The slab conclusion applies to this event under the original path law. Consequently, when $P_0(A_e)=0$,

   $$
   0\le  \mathbb E[w_pq_\infty ^p]\le  P_0(A_e)=0.
   $$

   Nonnegativity and $w_p>0$ imply $q_\infty ^p=0$ almost surely. Bounded convergence for each $p$, followed by a finite sum, gives $a_L(c)\to 0$. An infinite-stack shift may have a singular distribution relative to the original stack law; the proof never assumes otherwise. This is a valid finite-likelihood argument, not a restart from an allegedly pristine environment.

5. Fresh hyperplane and exact conditional factorization, lines 77–98.

   Fix a finite arrival history $\eta$ ending at $x=X_{T_m}$. Nearest-neighbor motion implies that every departure in $\eta$ came from a site with coordinate strictly less than $m$. The endpoint has just been reached and has supplied no departure. Thus the likelihood of $\eta$ involves only stacks strictly left of the hyperplane. Under the product site law, conditional on $\eta$, the entire half-space at and to the right of $m$ still has its original product law. Randomness of the arrival time and transverse endpoint causes no problem: one first fixes $\eta$, then uses spatial translation invariance.

   Partition $B_{m,L,c}$ by the unique last visit to level $m$ before $T_{m+L}$. Its time relative to arrival is some $s\le c$, and its prefix is some $p\in \Pi _c$. Since $L>c$, this prefix could not already have reached the target hyperplane. Given the full environment and both histories, the continuation law follows directly from the cookie transition rule with the recorded departure counts. On a successful continuation it uses only sites on or to the right of level $m$. All earlier departures there are exactly those in $p$. Departures in the old half-space may have arbitrarily large prior counts; none of those counts affects this successful continuation.

   This proves the stated quenched identity with the factors $W_\eta ^p(\omega )q_L^p(\theta _x\omega )$ kept together. They need not be independent. Dropping $W_\eta ^p\le 1$ pointwise, and only then averaging the pristine half-space, gives

   $$
   P_0(B_{m,L,c}\mid \mathcal F_{T_m})\le
   \sum _{p\in \Pi _c}\mathbb E[q_L^p]=a_L(c).
   $$

   There is no strong-Markov assertion for position alone. One can equivalently construct independent uniforms for every site and departure index and reveal them as used; the unrevealed instructions, conditional on the full stacks and history, give exactly the same formula.

6. Frequency estimate and infinite stopping times, lines 100–108.

   Along a residue class modulo $L$, $B_{m,L,c}$ is measurable at $T_{m+L}$. The centered indicators are bounded martingale differences for $\mathcal G_k=\mathcal F_{T_{r+kL}}$. The martingale strong law therefore gives the asserted frequency bound. If a hitting time is infinite, subsequent success indicators vanish; the stopped sigma-field convention handles this case. Combining finitely many residue classes and intersecting countably many $(c,L)$ events is legitimate. Crucially, the martingale statement is under the original annealed law, with no conditioning on future recurrence.

7. Zerner's Lemma 3 and the replacement counting proof, lines 110–129.

   The published lemma assumes only a fixed infinite nearest-neighbor path in $\mathbb Z^d$, starting at zero, a coordinate unit vector $e$, and $\limsup  X_n\cdot  e/n>0$. Its conclusion is

   $$
   \sup _{c\ge 0}\inf _{L\ge 1}\limsup _{M\to \infty }F_{M,L}(c)>0.
   $$

   It assumes no random environment, ellipticity, transience, or Markov property. These path hypotheses hold on precisely the positive-limsup event considered. Positive limsup ensures all nonnegative coordinate levels are reached. On that event the report's $I,h,F$ agree with Zerner's definitions. Its convention $h=\infty$ for an unreached target is irrelevant there. The lemma therefore applies verbatim.

   I also checked the report's independent reproof. At the selected times $n_k$, $M_k=\lfloor \delta  n_k/2\rfloor$ gives $T_{M_k+L}\le  n_k$ eventually for every fixed $L$. The sets of visit times belonging to different levels are disjoint. The second sum is bounded by telescoping $T_{m+L}-T_m$ along residues, giving at most $Ln_k$. Since $n_k/(M_k+1)<2/\delta$, the looser constant $C=3/\delta$ is valid.

   In the contradiction construction, Markov's inequality bounds the fraction with $h_{m,L_i}\ge \lceil 4CL_i\rceil$ by (1/4); the chosen next width makes the fraction with small $h_{m,L_{i+1}}$ less than (1/4). Thus more than half the levels have strictly increased diameter. The visit sets are nested in width, and their minimum is always $T_m$, so every such strict increase adds a visit. Taking a finite $q>2C$ and then one sufficiently large common $k$ contradicts the first counting bound. There is no exchange of an uncontrolled infinite family of limits.

8. Full convergence on $N$, lines 129–140.

   The counting lemma requires some fixed $c$ whose positive frequency survives arbitrarily large widths. The martingale bound and $a_L(c)\to 0$ exclude exactly that conclusion. Hence $P_0(A_e)=0$ implies $\limsup  X_n\cdot  e/n\le 0$ almost surely. Applying the argument in the opposite direction bounds the liminf below by zero when both directional escape probabilities vanish.

   If $P_0(N)>0$, then $N\subset (A_{e_j}\cup  A_{-e_j})^c$, so Theorem 3.16 forces both directional probabilities to vanish for each coordinate. Apply the preceding result to the finitely many signed coordinate directions. This gives $X_n/n\to 0$ almost surely for this law, in particular on $N$. If $P_0(N)=0$, the requested restricted assertion is vacuous. Every real direction follows from vector convergence. This controls the full limsup and liminf, not merely returns or selected excursions.

9. Tests against other environment classes.

   For RWRE, stack entries are constant in the visit index. Consuming $p$ does not change them; the argument reduces to Zerner's theorem. This is a consistency check, not an unintended contradiction. It proves neither deterministic nonzero velocity nor an individual directional zero-one law in general dimension.

   Without IID, the target is false in general, even under strict ellipticity. Here is an explicit test. Prescribe a nearest-neighbor path on the horizontal axis making excursions $0\to 2^k e_1\to 0$, for $k=1,2,\ldots$. At the $i$-th departure from site $z$, favor the direction prescribed by this path, with probability $1-3\varepsilon _{z,i}$, and give the other three directions probability $\varepsilon _{z,i}=2^{-(|z|_1+i+8)}$. Assign any favored direction for site-index pairs unused by the path. This is a fixed, spatially nonhomogeneous elliptic cookie environment.

   The sum of error probabilities over all site-index pairs is $3(3^2)/256=27/256<1$. By a union bound on independent instruction errors, the probability of following the entire prescribed path is at least $229/256>0$. On that event the origin is visited infinitely often, but the $k$-th peak occurs at time $3\cdot2^k-4$, so the coordinate limsup speed is (1/3) and its liminf is zero. The submitted proof cannot be applied: the fresh half-space no longer has a common translated stack law, and its IID zero-one/slab inputs are unavailable. This example is not a claim about stationary ergodic environments.

10. Independent numerical verification.

   I wrote `code/audit_checks.py`, `code/adversarial.py`, and `code/simulate.py` independently, with no imports or reused implementation from `claim_files/code`. The finite-history check averages complete path likelihoods over two latent stack types per site, with correlated cookie entries within each stack. Six cases, including two different old-half-space histories, agree with the grouped factorization to within $4\times 10^{-16}$. The intentionally incorrect product of separate prefix and continuation averages fails: one direct probability is (0.3414146515625), whereas that product prescription gives (0.33799216328125). The correct unweighted bound holds. Exhaustive projected-path enumeration checks 8,426 paths and 23,552 slab-width cases, including nesting and both counting sums. These are finite bookkeeping checks, not proofs of an infinite-horizon theorem.

   For the requested two-dimensional infinite-stack experiment, each site receives an independent fair sign $\sigma _x$. Cookie drifts alternate in paired blocks of lengths $16,16,32,32,64,64,\ldots$. If the current block sign is $s_i$, departure probabilities in directions $+e_1,-e_1,+e_2,-e_2$ are

   $$
   (0.4+0.36\sigma _xs_i, 0.4-0.36\sigma _xs_i, 0.1, 0.1).
   $$

   Thus individual cookies have horizontal drift magnitude (0.72), while blocks reverse it. Stacks are IID over sites, infinite, and uniformly elliptic. Recurrence of this particular block model is not assumed or established.

   Let $R_n$ denote a visit to the fixed ball $\{|x|_1\le4\}$ at some time in $[n/2,n]$. Among 192 trajectories followed to 262,144 steps, the following are finite-horizon measurements. The speed column is the mean **absolute** endpoint horizontal speed among trajectories satisfying $R_n$, avoiding cancellation of opposite signs.

   | $n$ | Long-block $R_n$ count | Frequency | Mean absolute horizontal speed on $R_n$ |
   |---:|---:|---:|---:|
   | 4,096 | 39/192 | 0.2031 | 0.005246 |
   | 16,384 | 25/192 | 0.1302 | 0.002412 |
   | 65,536 | 24/192 | 0.1250 | 0.001033 |
   | 262,144 | 15/192 | 0.0781 | 0.000573 |

   The last frequency has a 95% Wilson interval approximately $[0.0479,0.1249]$, for $P(R_n)$. It is not an interval for $P(N)$. At the last horizon, 7/192 trajectories returned to the origin during the second half. Endpoint speed on $R_n$ is likewise not speed conditional on the infinite event $N$.

   To assess this limitation, I simulated two controls. For planar simple random walk, $P(N)=1$, yet only 21/192 runs satisfied the last-horizon $R_n$ proxy. For an IID summable-trap law, each site has an independent uniform favorite direction, given probability $1-3\cdot 2^{-i-6}$ at departure $i$. All other directions receive $2^{-i-6}$. Every nonempty orthogonal direction set has positive probability of finite total transition mass, because the favorite lies outside it with positive probability. Survey Theorem 2.5 therefore gives finite range almost surely: here $P(N)=1$, and the actual limiting speed on $N$ is zero without using the claimed theorem. The observed last-horizon frequencies were 54/192 for an origin return and 172/192 for $R_n$; median range was four sites. The mean absolute horizontal speed among $R_n$ paths was $3.726\times 10^{-6}$.

   Consequently no defensible numerical estimate of $P(N)$ for the long-block law is available from these runs. Both controls have known $P(N)=1$, but return proxies substantially below one. Reporting the long-block proxy as an estimate of $P(N)$, or its selected speeds as conditional speeds on $N$, would be misleading. The numerical evidence is consistent with the proof and supplies no counterexample.

   Raw trajectories at four horizons and summaries are in `data/walks.csv` and `data/simulation.json`, with seed 71332026. The trap simulation truncates errors after departure 48; a worst-case omitted-error coupling bound across all 192 trap runs is $8.39\times 10^{-9}$, apart from ordinary floating-point sampling error. All numerical work used one worker at inherited nice 15, which is more yielding than nice 10. The simulation took 92.15 seconds and peak RSS was 70,369,280 bytes. macOS rejected the attempted virtual-address-space limit; the bounded-horizon dictionaries and measured RSS remained far below 4 GB. No publication, push, or subagent was used. I separately checked the submitted numerical table against its CSV; the counts and displayed values agree.

11. Literature and the extent of the contribution.

   The primary sources examined support the following distinctions:

   | Work | Relevant result and limitation |
   |---|---|
   | Zerner, ECP 7 (2002), 191–197 | Theorem 1 gives coordinate speed zero when neither direction is transient for IID elliptic RWRE. Lemma 3 is exactly the pathwise counting input. Cookie consumption prevents copying the probabilistic restart verbatim. |
   | Amir–Berger–Orenshtein, AIHP 52 (2016), 47–57, [Theorem 1.3](https://arxiv.org/pdf/1304.7287) | A deterministic speed exists for stationary ergodic elliptic cookie stacks on $\mathbb Z$, allowing infinite stacks. The fixed-site-return subsequence forces that speed to be zero on $N$. Thus the entire one-dimensional part is already in print. |
   | Holmes, *Excited against the tide*, AIHP 48 (2012), 745–773, [Theorem 2.1]$https://www.numdam.org/item/AIHPB_2012__48_3_745_0.pdf$ | Infinite IID cookie stacks are allowed, but the transverse coordinates are simple random walk and the general LLN uses $d\ge6$. This does not cover arbitrary cookies in arbitrary dimension. |
   | Holmes–Salisbury, [RWRE paper](https://arxiv.org/pdf/1105.5105), Theorems 1.3–1.5; [arrow-system paper](https://arxiv.org/pdf/1105.5157) | The former extends zero-one and LLN results to degenerate IID RWRE, with kernels fixed across visits. The latter gives principally one-dimensional arrow comparisons. Neither supplies the cookie-stack estimate audited here. |
   | Holmes–Sun, [1005.0927](https://arxiv.org/pdf/1005.0927); Pham, EJP 20 (2015), paper 72, [Theorem 1.1](https://arxiv.org/pdf/1311.6158) | Cut-time LLNs require a suitable transient projection; Pham's cookie model has simple transverse coordinates and dimension at least six. |
   | Menshikov–Popov–Ramírez–Vachkovskaia, AOP 40 (2012), 2106–2130, [Theorems 1.1–1.2](https://arxiv.org/pdf/1001.1741) | Bounded jumps, suitable uniform ellipticity, uniformly positive first-visit directional drift, and zero drift on revisits yield ballisticity. The non-transient event has probability zero in this class. |
   | Zerner, ECP 11 (2006), 118–128, [Theorem 1](https://arxiv.org/pdf/math/0601233) | Directional transience under nonnegative directional cookie drifts, positive expected total drift, and UEL; no general arbitrary-sign conclusion. The broader slab/zero-one facts used here are the survey's statements. |
   | Bérard–Ramírez, ECP 12 (2007), 303–314, [Theorem 1](https://arxiv.org/pdf/0705.0658) | LLN/CLT and positive speed for the once-excited model in $d\ge2$; no general infinite-stack recurrent-event theorem. |
   | Kosygina–Peterson, AIHP 53 (2017), 1458–1497, [1504.06280](https://arxiv.org/pdf/1504.06280); [1604.03153](https://arxiv.org/pdf/1604.03153) | Markovian and periodic infinite-stack results on $\mathbb Z$, including recurrent scaling limits. These extend one-dimensional structure rather than resolve general dimension. |
   | Travers, EJP 23 (2018), paper 43, [1611.01681](https://arxiv.org/pdf/1611.01681); Letterhos, [2103.05570](https://arxiv.org/pdf/2103.05570) | Respectively spatial Markov dependence with bounded cookies, and identical infinite stacks with finite total drift, on $\mathbb Z$. |
   | Pham's low-dimensional regularity [1501.04499](https://arxiv.org/pdf/1501.04499); Kosygina–Mountford–Peterson's 2023 scaling paper [2208.02589](https://arxiv.org/pdf/2208.02589) | Special bias families or one-dimensional self-interacting scaling problems, rather than the arbitrary-stack zero-speed-on-$N$ statement. |
   | Qin, September 2026, [2609.30045](https://arxiv.org/abs/2609.30045); Bou-Rabee–Nguyen–Peres–Singh, October 2026, [2610.10162](https://arxiv.org/abs/2610.10162) | Balanced-cookie recurrence/range results and centrally directed shape results, respectively. Balanced bounded-increment coordinates already have zero speed by martingale estimates; central drift depends on position. Neither is a general answer to 4.7. These are preprints, not evidence of a printed general resolution. |

   I independently rediscovered the survey's two OpenAlex records, fetched citations dated 2012–2026 with pagination, and screened all 45 distinct returned work IDs: 37 citations to one record and 23 to the other, with overlaps and duplicate versions. Raw results, DOI/title/URL table, and manifests are saved in `sources/`. I also searched exact problem-number variants, non-transient/nontransient and zero-speed terms, recent ERW LLNs, and author publication lists. The additional Qin preprint illustrates that forward-citation indexing is incomplete. Papers with an ERW-related title were checked for model scope; unrelated growth/tree/rotor models do not resolve this question.

   Relative to these sources, the contribution is precisely the extension from fixed RWRE kernels and previously treated cookie subclasses to arbitrary IID elliptic site stacks in $d\ge2$. More technically, it establishes equation (4) after arbitrary fresh-level arrival histories by enumerating the finitely many possible consumption prefixes and using their strictly positive original likelihoods. Zerner's path lemma, the martingale strong law, and the survey's range/slab/zero-one theorems supply the rest. No new deterministic counting principle is being proved.

   Zerner wrote the 2002 paper and coauthored the survey; the survey explicitly points from 4.7 to that theorem. Thus the authors certainly knew the intended RWRE analogy. Whether they considered this exact bounded-prefix argument cannot be inferred from the publications. Their posing the problem makes a literal “already follows verbatim” attribution untenable, but it is not an objection to a correct short transfer. The appropriate novelty claim is this specific extension and estimate, subject to normal bibliographic priority checking, not a new general methodology or a new one-dimensional theorem.

Reproduction: `python3 code/audit_checks.py`, `python3 code/adversarial.py`, and `python3 code/simulate.py`. Source URLs and SHA-256 hashes are in the three manifests under `sources/`; the unrelated PDF from one incorrect guessed identifier is explicitly excluded in its manifest. `LOG.md` records the audit as it proceeded. All deliverables are confined to this directory, and `claim_files/` was left unchanged.

Task: “You are an independent referee.” Asked 2026-11-13 04:57, Asia/Tbilisi.
