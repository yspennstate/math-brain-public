PARTIAL

For the bilateral reduced random walk in independent fair two-colour scenery, every exterior configuration is good when

\[
p>p_0=\frac{27}{28}=0.964285714\ldots.
\]

A complete proof is given below. This establishes an explicit subrange of the good half, not the conjectured threshold. Neither the remaining interval \(4/5<p\le27/28\) nor the bilateral all-bad half is settled here. No counterexample to the bilateral conjecture was found. The literature search located a substantial **one-sided** theorem, which must not be substituted for a bilateral result. I do not claim priority for the argument below.

## Setting and source correction

Let \((X_t)_{t\in\mathbb Z}\) be independent with \(P(X_t=1)=p\), \(P(X_t=-1)=q=1-p\). Put \(S_0=0\), \(S_t-S_{t-1}=X_t\) for every integer \(t\). Thus \(S_{-k}=-\sum_{j=-k+1}^0X_j\); the negative-time arm has the opposite spatial drift when followed backwards. Independently, let \((C_x)_{x\in\mathbb Z}\) be independent fair signs, and put \(Y_t=C_{S_t}\). Only \(Y\), not \(X\), is observed.

For an exterior record \(\eta\), write

\[
g_m(\eta)=P(Y_0=1\mid Y_t=\eta_t,
                 \ 0<|t|\le m).
\]

Every finite conditioning cylinder has positive probability, by taking a monotone walk. Total variation distance between two Bernoulli laws is \(|g-g'|\), using \(\sup_A|\mu(A)-\nu(A)|\). If total variation is instead defined as the full \(\ell^1\) norm, all displayed distance bounds acquire a factor two, with no change to continuity or badness.

The survey [1], Section 1, printed pp.53–54/PDF pp.1–2, specifies fair colours by default. Section 2.6, printed pp.60–61/PDF pp.8–9, defines badness by the existence of \(\epsilon>0\) such that, for every \(n\), some \(m\ge n\) and \(\delta=\eta\) on \([-n,n]\setminus\{0\}\) satisfy \(|g_m(\eta)-g_m(\delta)|\ge\epsilon\). Its Conjecture 2.16 is exactly the bilateral assertion in the question.

Contrary to one premise of the request, this section does **not** prove the reduced-process assertions at \(p=1/2\) or near one. Its Theorems 2.14 and 2.15 concern conditioning on the joint step-and-colour process outside zero. The reduced process is introduced separately immediately before Conjecture 2.16. In particular, recurrence results for the joint process do not settle the reduced process.

## Why the heuristic gives 4/5

For a monochromatic record of length \(N\), consider paths with an effective right-step fraction \(r\ge1/2\). A ballistic path of this type has range approximately \((2r-1)N\). The exponential walk cost and the cost of colouring its range black suggest minimizing

\[
J_p(r)=r\log\frac rp+(1-r)\log\frac{1-r}{q}
                       +(2r-1)\log2.
\]

This is a rate-function heuristic, not a proof of continuity for arbitrary records. Its derivative is

\[
J'_p(r)=\log\frac{rq}{(1-r)p}+2\log2,
\qquad J'_p(1/2)=\log\frac{4q}{p}.
\]

The minimum on \([1/2,1]\) is therefore at zero effective speed for \(p\le4/5\), and at \(r=p/(p+4q)>1/2\) for \(p>4/5\). The strict convexity check is \(J''_p(r)=1/[r(1-r)]>0\). The threshold equation is \(p=4q\), hence \(p=4/5\). Equivalently, the zero-speed walk cost is \(D(1/2\Vert p)=-\log(2\sqrt{pq})\); a walk can pay that cost to avoid continually purchasing new scenery sites. An unconditioned right-drifted walk returns from spatial distance \(h\) with probability \((q/p)^h\). Conditioning on a rare colour record can substantially offset that return penalty, which is why unconditioned transience alone is insufficient.

A distant record can reward a long excursion back through previously visited scenery. The inferred colours around the initial observation can then change. In the one-sided construction of [2], long \(WWBB\) stretches prohibit turns, while isolated pivots force successive reversals; the competition between scenery reuse and the bias again gives \(p/q=4\). This explains a mechanism, not a bilateral theorem.

The bad half is easier in its quantifiers: two suitable distant alterations suffice. The good half must control every distant alteration, including arbitrarily unlikely conditioning records. Strong drift can supply cuts separating the central observation from both tails even after conditioning. The proof below makes that uniform separation quantitative, with a deliberately coarse threshold above \(4/5\).

## Theorem and complete proof

**Theorem A.** For independent fair two-colour scenery and \(27/28<p\le1\), \(g_m\) converges uniformly to an everywhere continuous version of \(P(Y_0=1\mid(Y_t)_{t\ne0})\). In particular every configuration is good under the survey's definition.

The case \(p=1\) is immediate: \(Y\) is independent fair scenery read monotonically, so \(g_m\equiv1/2\). Assume henceforth \(27/28<p<1\).

### 1. Finite walks and positive cuts

Fix a finite chronological interval \([a,b]=[-m,m]\). We may anchor the walk at \(S_a=0\) instead of \(S_0=0\). Indeed, translate the scenery by the old \(S_a\). Conditional on all increments, this translated scenery still has the same independent law, so it is independent of those increments. Thus the finite colour-record law is unchanged.

For a finite nearest-neighbour path \(s_a,\ldots,s_b\), call the time edge \(k\in[a,b-1]\) a positive cut if

\[
\max_{a\le j\le k}s_j\le s_k,
\qquad \min_{k<j\le b}s_j>s_k.
\tag{1}
\]

The step at such an edge is rightward, and the two path pieces occupy disjoint spatial sets. Equivalently, the spatial edge \((s_k,s_k+1)\) is traversed exactly once, rightwards. To check the equivalence, a single positive crossing forces the path to start on its left and end on its right; reaching the wrong side before or after that crossing would require another traversal.

Split the time vertices at all positive cuts. This gives unique consecutive blocks \(I=[u,v]\). The intervening steps are rightward. Different blocks have disjoint spatial ranges. Inside a block there is no positive cut even when cuts are tested only on that block: its range is disjoint from the other blocks, so a local single positive crossing would also be a global one.

A block other than the first starts at its spatial minimum; a block other than the last ends at its spatial maximum. Conversely, any partition into consecutive vertex blocks with these boundary properties and with no internal positive cuts can be assembled uniquely, up to translation, into a walk: join successive blocks by one right step. Their spatial ranges are then disjoint and their separating edges are exactly the positive cuts. The first block need not start at its minimum, the last need not end at its maximum, and a block occupying the entire interval has neither restriction. These boundary cases are included throughout.

### 2. A block must contain many left steps

Let a block have \(L=v-u\ge1\) steps, \(\ell\) left steps, and displacement \(d=L-2\ell\). If \(d\le0\), then \(L\le2\ell\). If \(d>0\), each of the \(d\) spatial edges between its initial and final sites has one more positive than negative crossing. Since none is a positive cut, each must have at least one negative crossing. Consequently \(\ell\ge d\), and again

\[
L=d+2\ell\le3\ell.
\tag{2}
\]

This includes the initial, terminal and whole-interval blocks.

### 3. Exact interval factorization and its uniform bound

Prescribe any record on \([a,b]\setminus\{0\}\). Use as a reference its probability along the all-right path:

\[
B=p^{b-a}2^{-(b-a)}.
\]

There are \(b-a\) prescribed observations, since the interval has \(b-a+1\) vertices and one hole. For a proposed block \(I\), let \(h_I\) be its number of prescribed time observations. For a compatible block word \(w\), let \(r_I(w)\) be the number of distinct spatial sites carrying prescribed observations. Conflicting repeated observations give weight zero. The block's weight relative to its all-right reference is

\[
A_I(w)=\left(\frac qp\right)^{\ell(w)}
                     2^{h_I-r_I(w)}.
\tag{3}
\]

Formula (3) is exact: the walk-step ratio is \((q/p)^\ell\), and independent scenery is paid for once per distinct constrained site. If the site visited at time zero is not observed at another time, its colour is integrated out with total mass one.

Let \(R_I\) be the number of sites in the block's range and let \(e_I=1\) if the hole belongs to the block, zero otherwise. Nearest-neighbour paths visit every site in their range. Removing one time observation can leave at most one site unconstrained, so

\[
h_I=L+1-e_I,\qquad r_I\ge R_I-e_I,
\qquad R_I\ge |d|+1.
\]

It follows that

\[
h_I-r_I\le L+1-R_I\le L-d=2\ell.
\]

Set \(t=4q/p\). From (3),

\[
0\le A_I(w)\le t^{\ell(w)}.
\tag{4}
\]

For \(L\ge1\), let \(w_I\) be the sum of (3) over admissible no-cut block words, including the appropriate first/last block restrictions. Singleton blocks have weight one. By (2) and (4),

\[
w_I\le\sum_{\ell\ge\lceil L/3\rceil}\binom L\ell t^\ell.
\]

Since \(t<4/27<1/2\), put \(z=(2t)^{-1}>1\). Then

\[
w_I\le z^{-L/3}(1+tz)^L
      =\left(\frac{27t}{4}\right)^{L/3}
      =\rho^L,
\qquad \rho=\left(\frac{27q}{p}\right)^{1/3}<1.
\tag{5}
\]

After summing over block words, the exact likelihood of the prescribed record is

\[
B\sum_{\mathcal I}\prod_{I\in\mathcal I}w_I,
\tag{6}
\]

where \(\mathcal I\) ranges over collections of pairwise disjoint nonsingleton time intervals; the remaining vertices are singleton blocks. Adjacent blocks are permitted and are joined by their rightward cut step. The converse assembly in step 1 proves that (6) counts each walk exactly once. Thus the posterior block collection is a hard-core interval gas with local activities \(w_I\). There is no interaction between disjoint intervals, because their spatial ranges are disjoint.

The block words can be retained as marks with weights (3). The colour \(Y_0\) is another local mark of the block containing time zero: it is prescribed if that spatial site is observed elsewhere in the block, and is a fair coin otherwise. There is no constraint on that colour coming from any other block.

### 4. Domination by independent intervals

For a finite hard-core gas with activities \(w_I\ge0\), its interval indicators are dominated coordinatewise by independent Bernoulli indicators with parameters

\[
\theta_I=\frac{w_I}{1+w_I}.
\tag{7}
\]

Here is a proof, including the partial-conditioning detail. Under any assignment of some other interval indicators, removal of \(I\) maps every legal configuration containing \(I\) injectively to a legal configuration without it, and divides its weight by \(w_I\). It preserves the assigned indicators. Thus the conditional odds for presence of \(I\) are at most \(w_I\), and its conditional probability is at most (7). Expose indicators in any fixed order and use independent uniforms for these successive conditional probabilities and for the larger probabilities (7). This constructs the asserted domination.

Apply this independently to two posterior walks, possibly conditioned on different records, using separate dominating families. By (5), each dominating interval of \(L\) steps has parameter at most \(\rho^L/(1+\rho^L)\). We can enlarge once more to these record-independent parameters.

### 5. Shared cuts occur uniformly in long time intervals

Consider any interval \(J\) of \(r\) consecutive time edges. Choose an integer \(1\le K<r\), and choose

\[
s=\left\lfloor\frac r{K+1}\right\rfloor
\]

candidate edges inside it, spaced \(K+1\) apart. An interval of at most \(K\) steps cannot cover two candidates. For a fixed edge there are at most \(L\) intervals of \(L\) steps covering it. In the two independent dominating families, the probability that no interval of at most \(K\) steps covers a fixed candidate is at least

\[
c=\exp\left(-2\sum_{L\ge1}L\rho^L\right)
 =\exp\left(-\frac{2\rho}{(1-\rho)^2}\right)>0,
\tag{8}
\]

because \(\log(1+x)\le x\). These short-interval vacancy events are independent across the candidates: they depend on disjoint sets of independent interval indicators.

At most \(r+L\) intervals of \(L\) steps cover any edge of \(J\). A union bound for intervals longer than \(K\) in either family therefore gives

\[
P(\text{no common positive cut in }J)
 \le b_\rho(r,K)
 :=(1-c)^s+2\sum_{L>K}(r+L)\rho^L.
\tag{9}
\]

If a candidate is vacant in both dominating families, it is a cut for both actual walks. This explains the direction of the bound. Missing intervals beyond the finite horizon can only improve it, so (9) is uniform in the horizon and in both prescribed records.

For completeness the tail in (9) is

\[
\sum_{L>K}(r+L)\rho^L
=\rho^{K+1}\left[\frac{r+K+1}{1-\rho}
                    +\frac{\rho}{(1-\rho)^2}\right].
\tag{10}
\]

With \(K=\lfloor\sqrt r\rfloor\) and \(r\to\infty\), \(s\to\infty\), so both terms in (9) tend to zero. The possibly tiny value of \(c\) affects the rate, not convergence.

### 6. Switching between shared cuts proves continuity

Take two prescribed exterior records \(\eta,\delta\) on \([-m,m]\setminus\{0\}\), agreeing on \([-n,n]\setminus\{0\}\), with \(m\ge n\). Independently sample their marked block collections, including their central colours, and write these colours as \(U,V\).

Let \(G\) be the event that there is a common cut among edges \(-n,\ldots,-1\), and another among edges \(0,\ldots,n-1\). On \(G\), choose the nearest common cuts on the left and right of the central vertex. Swap the entire marked blocks between those cuts, including \(U,V\), between the two samples. All these blocks lie in \([-n,n]\). Their local records, admissibility rules and marked weights are identical in the two systems; the cuts ensure no block is split. Therefore the product weight of the pair is preserved.

This operation is an involution. In particular, the set of common cuts is unchanged when the two cut sets are exchanged inside the chosen segment, so the same cuts are selected on the second application. It also preserves \(G\). Hence

\[
E[(1_{\{U=1\}}-1_{\{V=1\}})1_G]=0.
\]

By (9), on taking \(r=n\),

\[
|g_m(\eta)-g_m(\delta)|
\le P(G^c)\le 2b_\rho(n,\lfloor\sqrt n\rfloor)
\longrightarrow0.
\tag{11}
\]

For the finitely many small \(n\) where \(K<r\) fails, use the trivial bound one. Equation (11) is uniform in \(m\ge n\) and in both exterior records. It directly rules out every bad configuration in the stated definition.

It also supplies the claimed continuous version. For \(m\ge n\), the tower property expresses \(g_n(\eta)\) as an average of \(g_m\) over extensions of its fixed inner record. Their diameter is bounded by (11), so \(|g_m(\eta)-g_n(\eta)|\) has the same bound. Thus \(g_m\) is uniformly Cauchy. Its limit is continuous, since each \(g_m\) depends on finitely many coordinates. Martingale convergence identifies that limit almost surely with the conditional expectation given all exterior observations. This completes the proof. \(\square\)

**General-colour extension.** If \(P(C_x=1)=\alpha\in(0,1)\) and \(\beta=\min(\alpha,1-\alpha)\), the same proof gives all-good configurations for

\[
p>\frac{27}{27+4\beta^2}.
\]

Indeed replace the baseline scenery factor by the product of the prescribed colour probabilities. Repeated visits can improve its ratio by at most \(\beta^{-1}\) per duplicate observation, at most \(2\ell\) duplicates per block. Thus (4) holds with \(t=q/(p\beta^2)\); (5) uses \(\rho=(27t/4)^{1/3}\). The remaining arguments are identical, and the unobserved singleton colour has prior \(\alpha\). This extension is separate from the survey's fair-colour conjecture. For monochromatic colour probability \(a\), the analogous heuristic boundary is \(p=1/(1+a^2)\), which also shows why a fair-colour threshold should not be silently asserted for general scenery laws.

## Exact computation and verification

The calculations in `code/rwrs_exact.py` integrate over both hidden ingredients. At chronological time \(-m\), anchor the walk at zero. A dynamic-programming state consists of the current position within the visited interval, the interval's length, and its colour bit string. Because the walk is nearest-neighbour, a new site can only be added at an endpoint. Matching revisits impose no further scenery cost; conflicting revisits are discarded. Spatial translation allows states with the same normalized interval to merge.

For \(p=a/b\), and a completely specified record of \(N+1\) time observations, each state carries an integer weight over the common denominator \(b^N2^{N+1}\). Each step multiplies by \(a\) or \(b-a\); a matching revisit multiplies additionally by two, and a new site by one. Run this transfer twice, filling the missing observation with each colour. If the resulting integer likelihood numerators are \(Z_+,Z_-\), then

\[
g_m=\frac{Z_+}{Z_++Z_-}.
\]

No walk is forced to be monotone in this computation. Every revisit and every compatible scenery assignment is included. The two probability fields and their absolute difference are saved as reduced fractions in `data/finite_windows.csv`; the decimal column is for reading only.

The grid is \(p=1/2,3/4,39/50,79/100,4/5,81/100,41/50,17/20,97/100,199/200\). The base exterior is black at every nonzero time. For each \(n=2,4,6\), the alterations agree with it on \([-n,n]\setminus\{0\}\). Outside that interval four choices are tested: all-white tails; repeated \(WWBB\) tails read outwards on each side; black negative and white positive tails; and period-two tails. Horizons are \(m=n,n+2,n+4,n+8,n+12,n+20,n+28\). These are fixed infinite exterior records for each \(n\) and tail choice, truncated at each horizon. There are 840 comparisons; the largest horizon is \(m=34\).

For the \(WWBB\) tails, these are the TV gaps at \(m=n+28\). All underlying values are exact fractions in the CSV.

| p | n=2, m=30 | n=4, m=32 | n=6, m=34 |
|---|---:|---:|---:|
| 0.50 | 0.239888933 | 0.086659955 | 0.035663974 |
| 0.75 | 0.203698209 | 0.086553164 | 0.042489695 |
| 0.78 | 0.221229268 | 0.099546685 | 0.052480884 |
| 0.79 | 0.226828467 | 0.103936352 | 0.055992375 |
| 0.80 | 0.232139013 | 0.108231286 | 0.059500122 |
| 0.81 | 0.237012404 | 0.112312517 | 0.062906812 |
| 0.82 | 0.241256454 | 0.116020282 | 0.066077087 |
| 0.85 | 0.247487078 | 0.122555524 | 0.072117057 |
| 0.97 | 0.066800593 | 0.014107396 | 0.003539071 |
| 0.995 | 0.010240168 | 0.000402945 | 0.000019484 |

Horizon growth is also saved, rather than only the final column. For example, at \(p=4/5,n=4\), the gaps at \(m=4,6,8,12,16,24,32\) are approximately \(0,0.044744763,0.063444426,0.082302363,0.092309452,0.102814290,0.108231286\). At \(p=0.995,n=4\), the last value is about \(0.000402945\).

These observations do not prove badness or good behaviour at \(4/5\). Badness requires a nonzero gap surviving arbitrarily large *inner* radii, with suitably chosen tails. Here the largest inner radius is six, and the selected tail patterns are not an optimization over all possible alterations. Increasing \(m\) at fixed \(n\) can increase a gap even in the all-good regime proved above. No transition location is fitted or inferred from this table.

Verification is reproducible with:

```
python3 code/rwrs_exact.py
python3 code/audit_proof.py
python3 code/run_evidence.py
```

The first run passed 417 exact checks. In particular, direct enumeration of every step word agrees with the transfer calculation for all 128 seven-observation colour words at each of three rational biases. Separate checks compare the interval partition function with direct enumeration, including a missing observation; verify colour-flip and spatial-reflection symmetries; and verify the \(p=1\) endpoint.

The additional proof audit checked all 32,767 step words of lengths zero through fourteen, comprising 58,474 blocks. It checked their cut decomposition, boundary range conditions, \(L\le3\ell\), spatial separation and the duplicate-observation bound, including holes at block endpoints. It also checked the exact interval factorization against direct enumeration for every punctured seven-time record at two biases (128 comparisons). All passed. These finite audits support the derivation; the infinite-volume conclusion comes from the proof, not extrapolation.

The binomial bound was re-derived independently by minimizing \(\log(1+tz)-(\log z)/3\), whose stationary point is \(tz=1/2\). It gives \(\rho^3=27t/4=27q/p\), hence exactly \(p>27/28\). The sign and magnitude agree with the deterministic endpoint: \(\rho\to0\) as \(p\to1\), while this bound cannot be used near \(4/5\).

The evidence run used one thread at inherited nice 10, took 47.04 seconds and had a measured peak RSS of 98,582,528 bytes (about 94 MiB). Its maximum DP dictionary had 72,147 states. A 200,000-state cap is built into the transfer code. Resource and audit summaries are in `data/computation_summary.txt` and `data/proof_audit.txt`.

## Literature result and exact references

The search was carried out on 13 November 2026. It covered the specified titles and authors, searches combining “random walk in random scenery” with “Gibbsian”, “continuity”, “quasilocality”, “4/5”, “two-sided” and “bilateral”, and targeted searches over 2006–2026. Author publication lists and the 2020 problem report were checked as well. No printed resolution of either *entire bilateral half* was located. This is a search result, not a proof that no such paper exists. The resulting status is therefore not `RESOLVED_IN_LITERATURE`.

1. F. den Hollander and J. E. Steif, *Random walk in random scenery: A survey of some recent results*, IMS Lecture Notes–Monograph Series **48** (2006), 53–65, DOI [10.1214/074921706000000077](https://doi.org/10.1214/074921706000000077), [arXiv:math/0608219v1](https://arxiv.org/abs/math/0608219). Exact source: Section 1, pp.53–54/PDF pp.1–2; Section 2.6, pp.60–61/PDF pp.8–9; **Conjecture 2.16, p.61/PDF p.9**. **Theorems 2.14–2.15**, pp.60–61, are the joint-process statements described above. Saved as `sources/survey_2006.txt`.

2. S. Blachère, F. den Hollander and J. E. Steif, *A crossover for the bad configurations of random walk in random scenery*, Annals of Probability **39**(5) (2011), 2018–2041, DOI [10.1214/11-AOP664](https://doi.org/10.1214/11-AOP664), [arXiv:1103.1780](https://arxiv.org/abs/1103.1780). Section 1.1, p.2019, expressly restricts to one-sided conditioning. **Theorem 1.3(i)–(iii), p.2022**: all-good near \((1,0)\), all-bad for \(1/2<p<4/5\) without holding, and coexistence at \(p=1/2\). Its exact no-holding sufficient bound is \(p>p_*=1/(1+5^5/12^6)=2985984/2989109\approx0.998954538\). **Conjecture 1.4, p.2022**, leaves the full one-sided good half open. The entropy calculation is Section 1.3, pp.2021–2022; the parity example is **(4.1), p.2036**, proved in Section 4.2, pp.2037–2038. **Proposition 1.2, p.2020**, relates bad points to versions of conditional probabilities. The arXiv electronic reprint has different pagination: the main theorem is on PDF p.5. Both text versions are saved. These results neither prove nor refute the bilateral conjecture.

3. F. den Hollander, J. E. Steif and P. van der Wal, *Bad configurations for random walk in random scenery and related subshifts*, Stochastic Processes and their Applications **115**(7) (2005), 1209–1232, DOI [10.1016/j.spa.2005.03.001](https://doi.org/10.1016/j.spa.2005.03.001). The accessible [EURANDOM Report 2004-037](https://www.eurandom.tue.nl/reports/2004/037-report.pdf) has **Theorem 1.2 on preprint p.6**, identifying the bad set with discontinuities of a suitable version and inclusion in the discontinuities of every version; **Theorem 1.3 on preprint p.7** classifies the probabilities of the bad sets for the joint RWRS. These page numbers refer to the preprint, not a guessed journal-page conversion. Its observed exterior consists of steps and colours, so its \(B(Y_0)\) notation does not mean badness conditional on colours alone. Raw text extraction has a broken font encoding; a glyph-name decoding was used to read the theorem labels and prose, with unrecognized mathematical glyphs treated as unknown. The survey and [2] independently corroborate the relevant scope and the version result. The extracted preprint text and its hash are saved; no page images were used.

4. C. Maes, F. Redig and A. Van Moffaert, *Almost Gibbsian versus weakly Gibbsian measures*, Stochastic Processes and their Applications **79**(1) (1999), 1–15, DOI [10.1016/S0304-4149(98)00083-0](https://doi.org/10.1016/S0304-4149(98)00083-0). The [author-hosted preprint](https://fys.kuleuven.be/english/staff/christ/files/pdf/pub/1999/spa.pdf) uses **Definition 4.4 and Proposition 4.2, preprint p.19**, for bad configurations and unavoidable discontinuities; **Proposition 4.3, preprint p.20**, gives a converse under uniform nonnullness. The published numbering is cited as Proposition 6 by [2], Proposition 1.2; I have not independently checked its published page number. This paper supplies general formalism, not the RWRS drift threshold. Its extracted text is saved as `sources/almost_gibbs_1999.txt`.

5. C. Maes, F. Redig, F. Takens, A. van Moffaert and E. Verbitski, *Intermittency and weak Gibbs states*, Nonlinearity **13**(5) (2000), 1681–1698, DOI [10.1088/0951-7715/13/5/314](https://doi.org/10.1088/0951-7715/13/5/314). **Theorem 3.5, p.1691**, and **Theorem 3.6, p.1693**, concern weak Gibbs descriptions of Manneville–Pomeau maps, not reduced RWRS. Read from the [author-hosted version](https://fys.kuleuven.be/english/staff/christ/files/pdf/pub/2000/verbit.pdf); text is saved as `sources/intermittency_2000.txt`. No claim about \(4/5\) is imported from it.

6. E. Verbitskiy, *On factors of g-measures*, Indagationes Mathematicae **22**(3–4) (2011), 315–329, DOI [10.1016/j.indag.2011.09.001](https://doi.org/10.1016/j.indag.2011.09.001). **Theorem 1.1, p.317** (PDF p.4 including the repository cover), preserves a continuous positive g-function under a one-block factor when the original g-function has summable variation. Read through the [repository text](https://pure.rug.nl/ws/portalfiles/portal/2548757/2011IndagMathVerbitskiy.pdf). Those hypotheses have not been established for the source process needed here, so this is not a shortcut to F0124. Also checked the scope of *Variational principle for fuzzy Gibbs measures*, Moscow Mathematical Journal **10**(4) (2010), 811–829, DOI [10.17323/1609-4514-2010-10-4-811-829](https://doi.org/10.17323/1609-4514-2010-10-4-811-829); its general variational principle is not a classification of RWRS bad configurations. Some repository downloads returned 403, recorded in LOG.md; their accessible indexed primary-source text was used instead.

7. J. E. Steif, *Some results and open questions concerning Gibbs states, quasilocality and bilateral determinism*, Oberwolfach Report **11/2020**, contribution pp.632–633. **Section 2 and Question B, p.632/PDF p.32**, ask for the quasilocality phase diagram and cite [2]. The [report](https://publications.mfo.de/bitstream/handle/mfo/3731/OWR_2020_11.pdf?sequence=4) provides later evidence that the phase-diagram problem remained open in that discussion. It does not turn [2]'s one-sided theorem into a bilateral one. Text saved as `sources/steif_2020.txt`.

The [den Hollander publication list](https://pub.math.leidenuniv.nl/~hollanderwtfden/PublicationsFdH.pdf), updated 14 October 2026, lists the 2011 crossover paper as item 122 (p.10) and was checked for later RWRS/Gibbs papers; its plain text is saved. Steif's [Chalmers publication list](https://research.chalmers.se/en/person/steif), including 2026 entries, was also checked. Neither author-list check yielded a later bilateral resolution.

## What remains

Theorem A supplies the requested explicit good range below one. Its constant comes from the rough universal bound that a no-positive-cut block has at least one third left steps, followed by counting *all* step words with that many left steps. This discards strong geometric constraints and is not expected to be sharp. Reaching \(4/5\) would require sharper control of the conditioned block activities, or another separation argument.

A proof that all bilateral configurations are bad below \(4/5\), including the symmetric endpoint, is not supplied. The one-sided parity exception at \(p=1/2\) is not a bilateral counterexample: extra observations from the past can change its argument. Likewise, no inference from the finite table resolves these missing cases.

Task: “Open problem F0124” — received 13 November 2026, approximately 07:18 Asia/Tbilisi (03:18 UTC; the prompt supplied no more precise timestamp).
