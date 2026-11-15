Verdict: SOUND WITH GAPS

The main theorem survives this audit. I found no invalid step in the convergence proof, no circular use of an interior limit, and no model mismatch that would invalidate the counterexample. The reverse-loop-erased rule is KMS's rule. Its reinforced edge set has the same conditional law as the forward-loop-erased rule, with spanning-tree probability proportional to the product of **conductances**, exactly as used here. The claimed positive limiting rung weight for every integer ell >= 2 follows from the proof and contradicts KMS Conjecture 1.1(1) as stated in the supplied source.

There is one false mathematical statement outside the proof: lines 243–245 omit two boundary equilibria when describing the zeros of the drift. There are also minor wording/numerical issues and an unresolved documentary gap: the Aletti survey is not supplied, so its wording, problem order, and bibliographic details cannot be certified under the prohibition on browsing. “SOUND WITH GAPS” reflects those manuscript/documentary issues; it does not mean that I found a missing argument in Theorem main.

All references below are to the original, unchanged PAPER.tex. Source references mean the local files `sources/kms/fourmis_arxiv.tex` and `sources/am/FLE_solution_draft.tex`, not a downloaded or published version independently obtained during this audit. No internet access, other agents, pushes, or modifications outside this folder were used. The manuscript and the author's programs/data were left unchanged.

## Findings and corrected text

### F1. Error: the stated list of positive-rung equilibria is incomplete

**PAPER.tex 243–245.** The statement that the displayed diagonal points “are thus the zeros of the drift with h > 0” is false on the closed state space. There are also

```
(a,c,h) = (0,1,1), (1,0,1).
```

At either point Q = ell > 0 and all three drift coordinates vanish. At the first point q4 = 1; at the second q3 = 1. These are feasible boundary limits of states consisting entirely of one of the two non-geodesic paths. They cannot be dismissed as singularities of the formula. `audit_symbolic.py` verifies both substitutions exactly.

Indeed, vanishing of the first two drifts requires either a = c or both ab = cd = 0. The latter possibility gives the two opposite corners above when h > 0. In the interior, a = c and the stated diagonal curve is the complete list for ell >= 2.

**Corrected text:**

> In the region $0<a,c<1$, $h>0$, the zeros of the drift for $\ell\ge2$ are exactly the points $a=c=p$, $h=(1-1/\ell)p(1-p)$, $0<p<1$. There are also boundary equilibria $(a,c,h)=(0,1,1)$ and $(a,c,h)=(1,0,1)$. Lemma away excludes convergence to the boundary for the process considered here.

**Effect:** none on the proof of the theorem. Lemma away is proved independently of this informal equilibrium description and excludes both omitted points.

### F2. Citation gap: the Aletti survey attribution cannot be checked from this deposit

**PAPER.tex 65–67, 537–540.** Neither the survey nor an excerpt of its open problems is supplied. Neither supplied bibliography contains an entry that supplies the claimed passage. Consequently I cannot establish that this is its *first* open problem, that the paraphrase gives its actual formulation, or that the bibliographic year/pages/author list are correct. This is an unresolved verification issue, not evidence that the attribution is false. It must not be reported as a verified quotation.

**Corrected text that is fully supported by the available sources:** replace the survey sentence with

> KMS leave the loop-erased process on general finite graphs open.

If the survey attribution is retained, provide the local source, exact problem number, page, and wording before treating it as checked. No change to the mathematical argument is needed: its target is the directly checked KMS conjecture, not the survey paraphrase.

### F3. Imprecision: unqualified “simplest graph outside this class”

**PAPER.tex 61–63.** KMS say “one of the simplest” at source lines 233–236; the manuscript changes this to “the simplest.” No criterion of simplicity or minimality is given. The class here is the class of two-terminal series-parallel networks with the specified N and F, not merely the usual unmarked graphs with no K4 minor. If unused branches are allowed, the graph with edges NF and Nz is already outside the specified two-terminal class on three vertices: every edge of such a series-parallel network belongs to some simple terminal-to-terminal path, and Nz does not. Even in a reduced-network class, the manuscript does not prove a minimality assertion.

**Corrected text:**

> For a basic graph outside this two-terminal class, the losange with vertices $N,u,v,F$ and edges $Nu,Nv,uv,uF,vF$, they prove the corresponding statement for the uniform-geodesic rule.

The separate assertion at lines 119–120 is correct: G2 is the smallest counterexample **within the stated family**, with six vertices and seven edges.

### F4. Imprecision: rounded numerical descriptions should be marked approximate

**PAPER.tex 479–483.** The displayed rounded differences are consistent with the data, but the literal descriptions of the last ratios and of the range of reciprocal increments are not exact. From the supplied five-decimal output, the last two ell = 2 residual ratios are approximately 0.55383 and 0.55912. For ell = 1 the four reciprocal increments are approximately 4.36354, 4.36829, 4.11999, 4.42635; the last exceeds the stated upper endpoint 4.4. These are small rounding issues, not evidence against the asymptotic interpretation.

**Corrected text at 480:**

> The last two decade ratios are approximately (0.554) and (0.559), compared with $10^{-1/4}\simeq0.562$.

**Corrected text at 482–483:**

> Using the stored five-decimal values, the increments of $1/h_n$ are approximately (4.364,4.368,4.120,4.426) over the four decades, while $\log 10/Q_n\simeq4.391$ at the last observation.

The rate assertions at 477–483 are already phrased as heuristics (“suggests”, “should”). They are not proved by the theorem and must remain heuristics.

## Exact comparison of the models and cited results

### KMS: definitions and numbering

The source uses one theorem counter, reset by section, shared by conjectures, definitions, and theorems. Thus the conjecture is 1.1, the series-parallel definition is 1.2, and the two main results are Theorems 1.3 and 1.4. The manuscript's numbers are correct.

* **PAPER 26–28, 44–54 versus KMS 141–165.** KMS start with unit weights; an ant starts at N, is killed on first hitting F, and uses transition probability $W_{\{x,y\}}/\sum_{z\sim x}W_{\{x,z\}}$. Weights are frozen during that walk. On the return, the earliest forward entrance into the present vertex is chosen; each return edge is reinforced once. This is precisely chronological loop-erasure of the reversed trajectory and precisely the manuscript's rule. The source's remark at line 160 contains an endpoint typo, writing its terminal gamma as F although the preceding operational construction explicitly goes F to N. That typo is in KMS, not an error in the manuscript. The source also has an indexing slip in its update at 165; the manuscript gives the consistent indexing.
* **PAPER 56–59 versus KMS 183–194, Conjecture 1.1(1).** The exact load-bearing statement is almost-sure convergence $W_e(n)/n\to\chi_e$ on every finite graph, with $\chi_e\ne0$ almost surely **if and only if** e belongs to at least one N–F geodesic. The manuscript faithfully reproduces this. KMS part (2) is about the uniform-geodesic rule and uses **only if** instead; this paper does not claim to refute part (2).
* **PAPER 61–62 versus KMS 220–224, Theorem 1.3.** KMS prove that conjecture for the LE process on series-parallel networks with source N and sink F. The terminal qualification is present in both papers and matters. Correct attribution.
* **PAPER 63–65, 117–118 versus KMS 240–246, Theorem 1.4.** KMS's theorem is explicitly for the **uniform-geodesic** process on the five-edge losange. Its conclusion is convergence of all normalized weights, matching shares on the two edges of each side, both side shares strictly between zero and one, and normalized middle-edge weight zero. The manuscript accurately says it obtains that conclusion for a different rule; it does not falsely attribute a loop-erased proof to KMS.
* **PAPER 64–65 versus KMS 233–237 and 252–265.** KMS explicitly say they cannot prove convergence for LE on the losange, believe the same limiting statement, and leave it open. They distinguish vanishing of the normalized middle edge from establishing a polynomial rate, which they say might fail. The manuscript's description is correct. Its logarithmic-rate discussion is heuristic and does not claim a proved rate.

The spelling/title/journal/year/volume/pages of KMS in PAPER 548–549 agree with AM's `KMS1` bibliography entry. The supplied TeX alone does not independently authenticate the arXiv identifier or establish identity with every detail of the final journal version; the mathematical comparison here is to the source the user supplied.

### AM: definitions, theorem, and open convergence question

AM use the same section-based shared theorem counter. The main theorem at source lines 206–212 is Theorem 1.1.

* **PAPER 72–74, 157–164 versus AM 155–180.** AM's LE rule is erasure of the time-reversed trajectory, while FLE is erasure of the trajectory itself. Both reinforce afterward, with unit initial weights. The definitions match exactly. “Forward” specifies which trajectory is erased, not that reinforcement occurs during exploration.
* **PAPER 73–75, 124–128 versus AM 185–188, 206–213.** AM's theorem concerns a finite simple graph with no NF edge and k length-two N–F paths (distance two). Let S be the union of those paths. It states (a) $|\widehat W_{Ni}-\widehat W_{iF}|\to0$ for each intermediate i and (b) $\widehat W_e\to0$ for e outside S, almost surely. Here $\widehat W_e=W_e/(n+n_e)$, with fixed positive $n_e$, equivalent to normalization by n for these claims. The paper correctly quotes the consequence for non-geodesic edges; it does not claim AM prove convergence of every surviving coordinate.
* **PAPER 75 versus AM 121–124.** AM conjecture shortest-path finding on all finite graphs. Their definition at 185–187 is vanishing of normalized weights on edges belonging to no geodesic. Correct paraphrase.
* **PAPER 125–126 versus AM 215–221.** AM explicitly leave full convergence of the FLE process under their theorem's assumptions open. The manuscript correctly states this is a general open problem and solves the losange case, not the whole problem.
* **PAPER 124–128.** G1 has distance two; G2 has distance three. Thus a positive non-geodesic rung limit on G2 defeats extending AM's conclusion to all graphs of distance three. This is a counterexample to that extension, not a contradiction of AM's distance-two theorem. It also contradicts AM's general shortest-path conjecture.
* **PAPER 76–80, 130–131, 157–164 versus AM 568–578.** AM already explicitly define the tree weight as $\prod_{e\in T}w_e$ and state the FLE/tree-path link, citing Lyons–Peres Corollary 4.3. The manuscript calls the link classical and cites Wilson, so it does not improperly claim that forward link as new. An additional citation to AM Section 2.5 at line 160 would make the relationship to the immediately preceding paper more explicit, but its absence is not a proof gap or a false attribution. AM's assertion that the tree connection is unique to FLE (source 69, 195–196) does not invalidate the reverse-rule argument; see the direct proof and exact checks below.

PAPER 541 matches the title and authors in AM source 41–42. Its arXiv identifier is supplied in the task/deposit, not independently checked online.

### Survey and other introductory citations

The survey attribution is unresolved as specified in F2. The primary texts of KMS2, MV, LGR, EFR, GSGC, Aldous, Broder, Wilson, Lyons–Peres, and Robbins–Siegmund are not in this deposit. I have not pretended to verify their full texts or all their bibliographic metadata. AM 192–193 corroborate the broad description of KMS2 at PAPER 68–69; AM 236–237 corroborate the two-nest description at PAPER 67–68. The shared KMS/KMS2/MV/LGR/EFR bibliographic entries agree with the supplied bibliographies. The proof below uses standard precisely stated probability results; not having those books/papers locally is distinct from finding a mathematical gap in their application.

## Independent derivation and exact checks of the path law

### Why reverse erasure is legitimate

For each visited x other than N, write $\sigma_x$ for its first entrance time and $p(x)=X_{\sigma_x-1}$. The last occurrence of x in the reversed trajectory is at $K-\sigma_x$; its successor is p(x). Therefore reverse erasure follows the parent chain from F down to N. First-visit times strictly decrease along that chain, so it cannot cycle. Continuing the *same, unabsorbed weighted walk* after its first visit to F until it covers the graph completes this partial parent structure to the first-entrance spanning tree rooted at N. No edge on the already determined F–N parent chain is changed by that continuation.

The weighted Aldous–Broder theorem gives the conductance-weighted spanning-tree law for this first-entrance tree. Wilson rooted at F gives the same tree law, with its first branch the forward loop-erasure from N to F. Thus the reinforced edge-set laws agree conditionally on every positive weight vector. Equal kernels and equal initial weights imply equality of the full weight-process laws and of the associated reinforced-path sequences. They do not imply equality of the return paths on each sampled outward trajectory.

For example, the possible trajectory $N,u,v,N,v,F$ has forward erasure $N,v,F$, whereas reversing the reverse erasure gives $N,u,v,F$. This example is compatible with, and does not refute, equality in distribution.

The weighting is correct. If $c(x)=\sum_{y\sim x}w_{xy}$, orient a tree toward a fixed root r. The product of parent transition probabilities is

\[
\prod_{x\ne r}p(x,\operatorname{parent}(x))
=\frac{\prod_{e\in T}w_e}{\prod_{x\ne r}c(x)}.
\]

The denominator is independent of T. One must use the inward parent orientation here; multiplying transitions on outward first-entrance edges naively would not give a tree-independent denominator. Undirected conductances and reversibility are essential to this reasoning. The manuscript uses the correct undirected model.

### Independent exact method

`audit_exact.py` imports no author code and uses `fractions.Fraction` throughout.

1. For forward erasure, it enumerates all reachable transient simple stacks. A move to a vertex already on the stack truncates the stack there; a new vertex is appended. Reaching F absorbs. It solves the finite rational system $(I-P)H=B$ for the entire absorption law. This sums walks of every possible length, not a finite walk-length truncation.
2. For reverse erasure, it tracks the original walk's first-entrance parent tree. Before every discovery, it sums all excursions in the visited set by rational inversion of its killed transition matrix, obtaining the law of the outward discovery edge. At first discovery of F it reads the parent path to N. This calculation uses no spanning-tree probability formula.
3. Independently, it enumerates all subsets of (|V|-1) edges, tests connectivity, extracts the N–F tree path, and accumulates $\prod w_e$. It then normalizes these masses.

All three laws agree as exact rational dictionaries in each test below. Labels are 0=N, 1=u, 2=v, 3=F, with the other labels internal or pendant vertices.

| Graph/weights | Forward transient stacks | Reverse visited sets | Trees | Result |
|---|---:|---:|---:|---|
| G1, $A,B,C,D,R$=(2,3,1,4,2) | 5 | 4 | 8 | All three exact laws equal |
| G2, (2/3,7/5,3/2,11/7,5/4) | 9 | 9 | 14 | All three exact laws equal |
| K4 on N,u,v,F, plus a leaf at u; all seven weights unequal | 7 | 6 | 16 | All three exact laws equal |

For G1, the path probabilities in the paper's order $(\pi_1,\pi_2,\pi_3,\pi_4)$ are

\[
(9/50,\ 3/5,\ 4/25,\ 3/50).
\]

For G2 with those rational weights they are

\[
(2886,\ 4928,\ 1100,\ 2205)/11119.
\]

For the third graph, edge weights on $Nu,Nv,NF,uv,uF,vF,uz$ are respectively

\[
2/3,\ 3/4,\ 5/7,\ 7/5,\ 11/9,\ 13/8,\ 17/6.
\]

Its probabilities on $NuF,NvF,NuvF,NvuF,NF$ are respectively

\[
(23254,\ 30303,\ 11466,\ 9702,\ 56460)/131185.
\]

No N–F simple path can use the leaf. Its excursions were nevertheless included in both walk calculations.

### Lemma law: independent tree enumeration and derivation

The graph is a theta network between u and v with three paths: the rung, u–N–v, and the two legs joined through F. A tree must cut two different theta paths, once each. There are $2+2\ell+4\ell=2+6\ell$ trees. The following are their masses after division by $C^{\ell-1}D^{\ell-1}$:

| Deleted edges | Multiplicity | N–F path | Mass of each tree |
|---|---:|---|---|
| rung, Nu | 1 | pi2 | BCD |
| rung, Nv | 1 | pi1 | ACD |
| rung, one u-leg edge | ell | pi2 | ABD |
| rung, one v-leg edge | ell | pi1 | ABC |
| Nu, one u-leg edge | ell | pi2 | BRD |
| Nu, one v-leg edge | ell | pi4 | BRC |
| Nv, one u-leg edge | ell | pi3 | ARD |
| Nv, one v-leg edge | ell | pi1 | ARC |

Summing gives exactly

\[
m_1=AC(D+\ell B+\ell R),\quad
m_2=BD(C+\ell A+\ell R),\quad
m_3=\ell ARD,\quad m_4=\ell BRC,
\]

and

\[
Z=CD(A+B)+\ell AB(C+D)+\ell R(A+B)(C+D).
\]

`audit_exact.py` checks the **unnormalized masses**, including the common factor, at 12 independent pseudorandom rational vectors for each ell = 1,2,3,4, using seed 20261112. All 48 tests pass; the respective tree counts are 8,14,20,26. The author's separate symbolic enumeration also passes for ell = 1,...,5. Numerical testing is corroboration, not a substitute for the enumeration argument.

## Line-by-line audit of the lemmas and theorem

### Lemma ust and the following paragraph, PAPER 140–164

* **141–144:** correct statement for a finite connected undirected graph with positive conductances. The tree measure is $\prod w_e/Z$.
* **147–150:** the first-entrance parent identity is exact. For the last reversed occurrence of x, the successor is its first forward predecessor. It is legitimate to terminate on first reaching N; p(N) is never needed.
* **150–154:** continuing after hitting F means removing the killing rule for this auxiliary construction, keeping the same weights. Weighted Aldous–Broder applies from the deterministic initial vertex N. The first-entrance edges of already visited vertices remain fixed; coverage cannot change the F–N path.
* **157–160:** Wilson rooted at F gives the forward branch law. The argument does not incorrectly regard a reversed killed trajectory as an ordinary fresh walk from F stopped at N.
* **161–164:** equality of reinforced edge-set kernels implies equality of the weight Markov chains. This is sufficient for all transferred results. No equality of raw trajectories or pathwise coupling is claimed.

### Path reduction and Lemma law, PAPER 166–205

* **166–172:** there are exactly four simple terminal paths; the edge-set convention fixes the orientation discrepancy between F-to-N gamma and N-to-F pi.
* **173–181:** a simple path uses exactly one entire leg, so equal initial leg weights remain equal. It also uses exactly one of Nu,Nv and exactly one terminal leg. Thus $A+B=C+D=n+2$, including the initial two units.
* **185–191:** the masses and normalizer agree with the independent derivation above, for arbitrary positive A,B,C,D,R; no normalization constraint is needed in this lemma.
* **194–204:** the graph counts, number of trees, all eight deletion classes, and each class's path/mass are correct, also at ell = 1. No class is missing or counted twice.

### Lemma drift, PAPER 209–245

* **209–218:** dividing the cubic masses by $S^3$ and using a+b=c+d=1 gives the four q's and $Q=\ell ab+cd+\ell h$. Correct.
* **219–221:** $0<h<1$, since $1\le R_n\le n+1<S_n=n+2$. The upper bound $Q\le(5\ell+1)/4$ follows from $ab,cd\le1/4$ and h<1. Correct.
* **225–231:** the identities are exactly

\[
f_a=\frac{\ell ab(c-a)}Q,\quad
f_c=\frac{cd(a-c)}Q,\quad
f_h=\frac{\ell h(g-h)}Q,
\quad g=ad+bc-ab-cd/\ell.
\]

  The probabilities for b and d are the complements. All five agree symbolically; these f's are probabilities of reinforcement minus the current normalized coordinates. The actual normalized one-step mean increments are f divided by $S_n+1$.
* **236–240:** both cancellations use the correct sum identities, and the rung identity has the correct sign and ell factor.
* **243–245:** $g(p,p)=(1-1/\ell)p(1-p)$, and at ell = 1, $g=(a-c)^2$, are correct. The description of *all* zeros is the error in F1.

### Harmonic preliminary estimates, PAPER 249–260

$\psi(k)=H_{k-1}$, $\psi(k+1)-\psi(k)=1/k$, and $0\le\psi(k)-\log k\le1$ are correct. The difference increases because $1/k-\log(1+1/k)>0$, and converges to Euler's constant. If a nondecreasing integer sequence stays bounded it eventually becomes constant, so its correction still converges; divergence has not been assumed. Each increment 0/1 visits each summation denominator at most once, giving $\sum\Delta k/k^2\le\pi^2/6$ pathwise. This fact is used correctly for every weight coordinate later.

### Lemma mart, PAPER 263–297

* **263–268:** the harmonic martingale and logarithmic coordinate are different objects. The proof correctly establishes the martingale identity for the former and only convergence for the latter.
* **275–286:** along paths pi1,pi2,pi3,pi4 the exact increments of M are respectively

\[
1/A+\ell/C,\quad -1/B-\ell/D,\quad
1/A-\ell/D,\quad -1/B+\ell/C.
\]

  Their q-weighted sum is identically zero on $A+B=C+D=S$. `audit_symbolic.py` verifies this **discrete increment identity**, not just the vanishing derivative of an ODE invariant. Equivalently, the conditional expectation is
  ${\ell(a+b)(c-a)+\ell(c+d)(a-c)}/(SQ)=0$.
* **288–290:** exactly one of A,B and one of C,D increases at each step. The harmonic-sum estimate gives $\sum U_n^2,\sum V_n^2\le\pi^2/3$. The inequality $(U+\ell V)^2\le2U^2+2\ell^2V^2$ gives the stated deterministic bound $2(1+\ell^2)\pi^2/3$. No independence of U,V is needed.
* **291–292:** orthogonality of square-integrable martingale differences and Tonelli give the uniform L2 bound, then almost-sure and L2 convergence. Every finite-time variable is integrable, since all weights are positive integers and increments are bounded.
* **294–296:** all four harmonic/log corrections converge without any assumption that their weights diverge. The bound $|M-r|\le1+\ell$ is valid: each signed *pair* is a difference of two numbers in [0,1]. Thus r has a finite limit and bounded supremum. There is no missing factor of two.

### Lemma away, PAPER 301–338

* **305–309:** the implication $a_n<\kappa\Rightarrow a_n\le c_n$ is correct. If c<a, monotonicity of logit would give $-r^*\le r<(1+\ell)\logit a$, hence a>kappa.
* **311:** $Y_n=\psi(A_n)-\log S_n$ satisfies $Y_n-1\le\log a_n\le Y_n$ with the inequalities in the stated direction.
* **313–319:** the centered harmonic increment is a true martingale difference. Its conditional variance is at most $E[I_{Nu}/A_n^2\mid\mathcal F_n]$. Summing expectations and using the pathwise harmonic-sum bound gives at most $\pi^2/6$; therefore its martingale converges and has a finite supremum almost surely. A bound on $\sum1/A_n^2$, which need not be summable, is not being assumed.
* **320–322:** subtracting $\log(1+1/S)\le1/S$ leaves the stated lower bound for the increment of Y.
* **325–332:** the last exit from a>=kappa exists because a0=1/2. On the excursion below kappa, c-a is nonnegative. The summed martingale contribution is bounded below by $-2\mathcal N^*$. At the entry step Y can fall by at most $\log(3/2)$, since S>=2 and its harmonic increment is nonnegative. The final lower bound for log a is finite, uniformly in n.
* **Random-threshold issue:** kappa depends on the entire future through r*. This causes no stopping-time error. The proof does not apply optional stopping to the last exit. It sums a pathwise increment inequality and bounds a difference of two values by a pathwise supremum. An adapted or deterministic threshold is not required.
* **333–337:** graph symmetry proves the same almost-sure lower bound assertion for b. On the intersection of these two probability-one events, logit a is bounded. Bounded r then bounds logit c, giving positive lower bounds for c and d. The minimum of the four random bounds supplies kappa0. This establishes interiority before, and independently of, convergence. No assumption about the eventual rho has entered.

### Lemma delta and Robbins–Siegmund, PAPER 342–364

* **346–351:** the normalized increment is exactly $(\xi_{n+1}-\delta_n)/(S_n+1)$. The conditional mean is $-\lambda_n\delta_n/(S_n+1)$, with $\lambda_n=(\ell a_nb_n+c_nd_n)/Q_n$. Correct sign and denominator.
* **352–354:** $|\xi-\delta|\le2$ gives the displayed conditional second-moment inequality.
* **356–357:** the version of Robbins–Siegmund needed here says: if nonnegative adapted integrable Z satisfies
  $E[Z_{n+1}\mid\mathcal F_n]\le Z_n-B_n+C_n$, with nonnegative adapted B,C and $\sum C_n<\infty$, then Z converges finitely and $\sum B_n<\infty$ almost surely. Here take

\[
Z_n=\delta_n^2,\quad
B_n=\frac{2\lambda_n\delta_n^2}{S_n+1},\quad
C_n=\frac4{(S_n+1)^2}.
\]

  All are adapted and bounded at finite time; C has a deterministic summable series. Thus all hypotheses are met. Omitting the irrelevant factor two when recording summability at 357 is legitimate.
* **357–359:** after the theorem has been applied, Lemma away gives the pathwise lower bound $\lambda_n\ge4(\ell+1)\kappa_0^2/(5\ell+1)>0$. The lower bound is random, but pathwise harmonic divergence is enough: a positive limiting delta squared would contradict the finite series. No expectation or optional stopping with kappa0 is used.
* **361–363:** on each path's compact interval of interiority, logit is uniformly continuous. Delta->0 and convergence of r give $(1+\ell)\logit a_n\to r_\infty$, hence $a_n,c_n\to\rho\in(0,1)$. Correct.

### Deterministic Lemma det, PAPER 368–391

* **369–374:** beta need not be monotone, and eta need not have summable increments. Positivity, beta->0, divergent sum, and convergence of eta are the properties used.
* **377–384:** above a fixed log(theta), theta>g*, the u increments have uniformly negative sign and magnitude at least a positive multiple of beta. Remaining there forever contradicts divergent cumulative beta and bounded eta. After the last crossing, the only upward overshoot of u is bounded by 2 beta; the change in eta between arbitrary late times is at most epsilon. This proves the upper bound, also for g*=0 by taking theta down to zero.
* **386–390:** for g*>0 the analogous lower barrier is valid, with positive u drift below log(theta), 0<theta<g*. It proves the lower bound. For g*=0 no lower-barrier assertion is needed because exponentials are nonnegative.

No stochastic-approximation black box or trap-avoidance assertion is hidden in this lemma. Its proof covers both the vanishing-rung and positive-rung cases.

### Lemma rung, PAPER 393–417

* **397:** convergence of a,c has already been established, so $g_n\to g^*=(1-1/\ell)\rho(1-\rho)\ge0$. This does not assume h converges.
* **398–401:** the exact harmonic rung mean is $1/S+\ell(g-h)/(QS)$; division by h is legitimate at every finite time because R>=1. There is no missing 1/R or ell factor.
* **403–404:** centering this harmonic increment yields a martingale whose total expected conditional variance is at most $\sum E[I_{uv}/R_n^2]\le\pi^2/6$. Hence it converges in L2 and almost surely, whether or not R tends to infinity. The same argument as in Lemma away is applicable.
* **405–407:** $e_n=1/S_n-\log(1+1/S_n)$ is nonnegative and at most $1/(2S_n^2)$, so its sum converges.
* **409–414:** the harmonic correction epsilon_n converges even if R stabilizes. Telescoping the increment identity gives exactly $\log h_n=u_n+\eta_n$ with convergent eta, including the initial Y'_0 term. The inequalities $-1/2\le g_n\le1$, $0<h_n<1$ imply the required bound by two.
* **415–416:** Lemma away bounds $Q_n\ge(\ell+1)\kappa_0^2$; the earlier deterministic upper bound gives a positive harmonic lower bound on beta. Thus beta->0 and its sum diverges pathwise. Lemma det applies to each path in the probability-one event of all preceding convergence/bound statements. At ell=1 it gives h->0; at ell>=2 it gives the strictly positive g*. Boundary h=0 is approached but is never divided by at a finite time.

### Completion, symmetry, and non-degeneracy, PAPER 419–426

* **420:** S/n->1 transfers the normalized limits to W/n on every edge.
* **421:** the automorphism interchanging the two legs preserves unit initial weights and the full transition law, so rho and 1-rho have the same distribution. Symmetric distribution alone would not prove non-degeneracy; the proof does not make that mistake.
* **422–424:** the interior lower bounds imply A,B,C,D all tend to infinity. Only now can each harmonic/log correction be replaced by Euler's constant; the signed constants cancel, giving $r_\infty=M_\infty$. The L2 convergence already proved gives $E r_\infty=0$.
* **425–426:** martingale orthogonality gives $E r_\infty^2\ge E(M_1-M_0)^2>0$. At the initial unit weights, q1=q2=(1+2ell)/(2+6ell) and q3=q4=ell/(2+6ell), so the first variance is explicitly

\[
\frac{3\ell^3+3\ell^2+5\ell+1}{3\ell+1}>0.
\]

  In particular it is 3 at ell=1. This independently checks the strictly positive variance assertion. A finite mean-zero random variable with strictly positive second moment is not constant. Strict monotonicity of the logistic map transfers non-degeneracy to rho.

## The corollaries and the claim that the conjecture fails

**PAPER 83–87, 103–128, 428–434:** a simple path starting Nu either continues down the entire u-leg or crosses uv once and continues down the entire v-leg; the analogous alternatives hold starting Nv. A simple path cannot turn back along a leg, return to N, or cross the rung twice. Hence the four listed paths are exhaustive. The two without the rung have ell+1 edges; the two with it have ell+2. There is **no non-geodesic reinforced path that avoids uv** on this graph.

Therefore the count of non-geodesic reinforced paths among the first n ants is exactly R_n-1, not R_n. The manuscript subtracts the initial unit correctly. The limit of that count divided by n is the stated positive random quantity at ell>=2.

For the probability of a single late non-geodesic path, empirical frequency convergence alone would not suffice. The manuscript supplies the extra argument:

\[
P(\gamma_{n+1}\text{ non-geodesic}\mid\mathcal F_n)
=h_n+\frac{\ell h_n(g_n-h_n)}{Q_n}\longrightarrow g^*.
\]

The lower bound on Q is pathwise, which is sufficient for this almost-sure convergence. These conditional probabilities lie in [0,1], so bounded convergence and total expectation yield the unconditional limit. Since rho is in (0,1) almost surely, rho(1-rho)>0 almost surely and its expectation is strictly positive. Non-degeneracy of rho is not needed for that positivity.

G2 is a finite graph on which a non-geodesic edge has a strictly positive limiting normalized weight **almost surely**. This contradicts even the literal assertion that nonzero almost-sure limits occur only on geodesic edges in KMS 1.1(1). There is no ambiguity about “positive probability” versus “almost surely” that could rescue that conjecture. The paper does not disprove the conjecture's universal *convergence* component; it disproves the proposed characterization of the limit's support. It also does not disprove the uniform-geodesic conjecture.

For ell=1 the formula gives normalized rung limit zero and both side limits strictly interior. This supplies full LE/FLE convergence on the losange beyond AM's disappearance result and matches the conclusion of KMS 1.4 under a different rule. “The rung dies” in the abstract must be read as $W_{uv}(n)/n\to0$; no finite total reinforcement or eventual prohibition of rung use has been proved or claimed formally.

## Simulations and data audit

The author's C implementation was inspected: it freezes weights during each ant, stores the complete first-hit trajectory, iterates it in reverse, performs chronological stack loop-erasure, and reinforces each resulting edge once. Its reported invariants match the ones used in the proof. The finite ell=1,2,3 inputs used here are well inside its fixed graph-array sizes. It does not use a tree sampler or the closed-form q's for its dynamic runs.

Compiled exactly with:

```
cc -O2 code/sim_ants.c -o audit_sim_ants
```

Each ell=1,2,3 run was performed first to 10^7 ants and then to 10^8 ants, seed 1. The 10^8 runs took approximately 4.47, 10.63, and 19.49 seconds respectively. Jobs ran sequentially. The two fixed-weight runs used two million ants each. No computation approached five minutes.

At n=10^8 the fresh outputs are:

| ell | a_n | c_n | h_n | (1-1/ell)a_n$1-a_n$ | h_n minus target |
|---:|---:|---:|---:|---:|---:|
| 1 | 0.46134 | 0.46132 | 0.02736 | 0 | 0.02736 |
| 2 | 0.38569 | 0.38574 | 0.12126 | 0.11847 | 0.00279 |
| 3 | 0.64536 | 0.64537 | 0.15316 | 0.15258 | 0.00058 |

The code prints $h_n=W_{uv}(n)/(n+2)$, rather than Wuv/n. Their difference is at most 2/n, hence at most 2e-8 here; the displayed precision is adequate for the requested comparison. If the empirical u-entry share is $\widehat\rho_n=(A_n-1)/n$, then $|a_n-\widehat\rho_n|\le1/(n+2)$, and the corresponding target differs by at most 1/(n+2), since the target function has derivative of magnitude at most one. The u-leg empirical share instead uses $C_n-1$/n; the distinction is visible at finite n and tends to zero by Lemma delta. The paper's chosen proxy is a_n, and that is the one compared in the table.

At ell=1 a nonzero finite-time h is expected; the theorem proves its eventual vanishing, not a polynomial rate. These runs are consistent with slow decay but cannot prove almost-sure convergence or positivity/non-degeneracy of the random limit.

The two frozen-weight experiments reproduce the manuscript exactly:

| ell, weights $A,B,C,D,R$ | Empirical pi1,pi2,pi3,pi4 | Formula |
|---|---|---|
| 2, (2,3,1,4,2) | 0.15544, 0.60037, 0.17762, 0.06657 | 0.15556, 0.60000, 0.17778, 0.06667 |
| 3, (5,2,3,4,1) | 0.44208, 0.38081, 0.13629, 0.04083 | 0.44218, 0.38095, 0.13605, 0.04082 |

`audit_data.py` verifies every one of the manuscript's 13 table rows against the final line of its corresponding supplied data file. All 13 match, all supplied invariants are “ok”, and the maximum displayed |a-c| is 0.00021, supporting the claim “less than 0.0003.” For ell>=2 the maximum displayed |h-target| is 0.00450. Calling this “close” is qualitative; the manuscript gives the actual values and discusses slow convergence rather than pretending that they are exact equilibria.

The fresh seed-1 runs for ell=1,2,3 reproduce **every printed checkpoint through 10^8** exactly. This independently reproduces three table rows and their complete recorded trajectories of checkpoints. The other ten final rows were checked against the supplied data, not rerun. The author's exact-check output and both frozen-weight outputs also reproduce their supplied files exactly after newline normalization.

For ell=2, seed 1, the residuals from the supplied five-decimal values at n=10^4,...,10^8 are

```
0.04014, 0.01870, 0.00901, 0.00499, 0.00279.
```

These support the rounded numbers at PAPER 479–480. The linearized h derivative at the equilibrium is exactly $-(1-1/\ell)/2$, verified symbolically. The full process also contains coupled coordinates and martingale noise; the paper correctly does not present the observed power law as a proved convergence rate. For ell=1 the final stored values give log(10)/Q approximately 4.39115. F4 records the small numerical wording corrections.

## Programs, commands, and saved outputs

All programs and outputs created for this audit are in this folder. The author code is used only where explicitly identified.

| Program | Purpose | Saved output/result |
|---|---|---|
| `audit_exact.py` | Independent exact stack/discovery/tree laws; rational tree masses for ell=1,...,4 | `audit_exact.out`: all independent exact checks pass |
| `audit_symbolic.py` | Exact discrete martingale, drifts, diagonal identities, h derivative, omitted equilibria, first variance | `audit_symbolic.out`: all symbolic checks pass; both omitted equilibria printed |
| `code/check_path_law.py` | Author's symbolic tree and drift checks, rerun unchanged | `audit_author_check.out`: identical to supplied `data/check_path_law_out.txt` |
| `audit_run.py` | Sequential compilation and initial bounded runs | `audit_run.out`, `audit_compile.out`, `audit_run_l{1,2,3}_s1.out`, `audit_freeze_l{2,3}.out` |
| `audit_finish.py` | Symbolic check and sequential 10^8-ant runs | `audit_finish.out`, `audit_run_l{1,2,3}_s1_1e8.out` |
| `audit_data.py` | All table rows, fresh-run comparisons, and numerical prose checks | `audit_data.out`: all data checks pass |
| `audit_report_format.py` | One-time Markdown repair and report/artifact consistency check | `audit_report_format.out`: checks pass |

Reproduction commands:

```
python3 audit_run.py > audit_run.out 2>&1
python3 audit_finish.py > audit_finish.out 2>&1
python3 audit_data.py > audit_data.out
```

The wrappers impose a 230-second timeout on each child job and never overlap child jobs. Initial attempts to lower process priority and impose OS memory limits were rejected by the sandbox and are explicitly recorded in `audit_run.out`; those attempts did not run computations. The actual jobs use very small exact matrices (at most nine transient states in the path-law comparison), finite tree enumerations, modest SymPy expressions, and small-graph C simulations; no large-memory operation or worker pool was launched. The largest fresh simulation completed in under twenty seconds. No external task checklist or mesh was updated, respecting the instruction not to write outside this folder.

## Abstract and introduction: final assessment

PAPER 26–35 accurately summarize the defined process, the theorem's limit formula, interior non-degenerate rho, the counterexample for ell>=2, the losange corollary, and equality in law with FLE. Their “grows linearly” language is shorthand for the precise normalized limit later stated. No abstract sentence asserts a stronger probabilistic theorem than the proof establishes.

The introduction accurately separates KMS's two reinforcement rules and AM's disappearance result from full convergence. The equivalence of LE and FLE is justified, rather than merely asserted. The graph counts, terminal distances, four paths, and scope of the counterexample are correct. The exceptions needing correction/verification are F2 and F3; the explanatory drift paragraph needs F1. No additional proof step needs replacement on the evidence of this audit.

Task: “You are a hard, careful referee for a probability journal” — audit of “A non-geodesic edge that survives in the loop-erased ant process”, 12 November 2026. The originating user-message clock time was not exposed in this run; no time has been invented.
