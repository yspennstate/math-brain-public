Overall verdict: SOUND WITH GAPS

The main asymptotic conclusions survive this audit. I found a false counting sentence in Proposition 3.1 that needs the qualification given below, and a reproducible numerical error in Section 6. The counting repair preserves the proof and all its powers of k and n. I did not find a counterexample to Theorem 1.1, a missing range of component sizes, or an invalid extension of the bounded-window theorem in Corollary 1.2. The earlier connectivity bounds are not needed to prove that corollary.

Line numbers below refer to the supplied PAPER.tex. I read the supplied programs and their outputs but did not execute or import the authors' programs. All new programs, binaries, raw samples, and outputs are in this directory. No browsing, other agents, pushes, visible windows, or writes outside this directory were used. Shared-brain/checklist/mesh writes were omitted because this run expressly forbids writes outside this folder.

## Theorem 1.1 — SOUND, with the local repair in Proposition 3.1

Lines 51–58 and 272–278. Proposition 3.3 proves the first assertion, uniformly for fixed C. Total variation controls the event Z_n=0, so P(Z_n=0)=exp(-lambda_n)+o(1). For n at least 2, connectivity implies Z_n=0. Every disconnected graph without isolates has a component of size in [2,n/2]. Thus the difference of the two probabilities is nonnegative and is bounded by the exceptional threshold event plus the component bounds.

There is no missing component-size interval: Lemma 4.2 covers 2–6, the first part of Lemma 4.1 covers 7–12, and its geometric sum covers 13 through floor(n/2). Although Lemma 4.1's statement concerns a union of events, its proof actually bounds the sum of their probabilities, as needed in line 275. The exceptional event G^c is charged once, not once per size or vertex set.

The uniformity is valid: all auxiliary constants depend only on fixed C, fixed r, or fixed omission budgets. No argument substitutes a growing C into an estimate proved only for fixed C. The conclusion supplies no useful small finite-n error bound: some displayed upper bounds decay extremely slowly.

## Corollary 1.2 — SOUND

Lines 60–62 and 280–288. The extension to sequences with unbounded |k-log n| really follows, but it requires the monotone coupling used explicitly at line 281. It would not follow merely by substituting those sequences into Theorem 1.1.

Use the same independent scores for every budget. Each preference list increases with k, so every retained edge remains retained and connectivity is increasing. For fixed L>0, choose q_n=ceil(log n+L). Then q_n-log n lies in [L,L+1), and q_n<=k eventually if k-log n tends to positive infinity. Applying the theorem with the fixed constant C=L+1 gives

    liminf P(connected at k) >= exp(-exp(-L)).

First let n tend to infinity, then L tend to infinity. For k-log n tending to negative infinity, q_n=floor(log n-L) is eventually at least k, its offset lies in (-L-1,-L], and

    limsup P(connected at k) <= exp(-exp(L)).

The integer rounding directions in the paper are correct. Both comparison budgets are in [1,n-1] eventually for each fixed L. The finite-offset subsequence assertion follows directly from Theorem 1.1 and continuity of the Poisson law in its mean.

The “if and only if” wording in the abstract and at line 285 is also justified for oscillatory sequences. Failure of convergence of k-log n to positive infinity gives a bounded-above subsequence; a further subsequence converges to a finite c or to negative infinity. Its connectivity probability cannot tend to one. For the other equivalence use a bounded-below subsequence and a finite limit or positive infinity. This also handles sequences whose absolute offset is unbounded but whose sign changes.

Dabirian–Subramanian is not invoked in this proof and is not needed. The paper uses those bounds as historical context and to describe the improvement. Monotonicity is needed and is used correctly.

## Lemma 2.1 — SOUND

Lines 82–99, displays (2.1) and (2.2). The density of X_k is

    (m)_k x^(k-1) (1-x)^(m-k)/(k-1)!.

Conditional on X_k=x, the unordered lower observations are k-1 independent Uniform[0,x] points. This does not assert independence of their ordered versions. For d=0 the conditional product has mean g(x)(G(x)/x)^(k-1). Integration by parts uses (G^k)'=k g G^(k-1) almost everywhere, G(0)=0, and m>k to kill the boundary at 1. The resulting coefficient is (m)_k(m-k)/k!=(m)_(k+1)/k!, with exponent m-k-1 as printed.

For a retained rank set A={a_1<...<a_(k-d)}, a_i<=i+d. Monotonicity therefore bounds its product by the product at the largest k-d ranks. That last product is the largest among the nonnegative subset products of the unordered lower points, so it is bounded by their sum. There are binom(k-1,d) terms, each with conditional mean (G/x)^(k-1-d). This proves the omission inequality with the stated x^d and factorials. The proof needs no differentiability of g; monotonicity gives measurability and absolute continuity of G suffices.

Independent exact symbolic integrations for g(x)=x^2, m=7, k=3 agree with the equality and verify several nontrivial omissions; outputs are recorded below.

## Lemma 2.2 — SOUND

Lines 101–137. The order-statistic/binomial identity uses B~Beta(k,N-k+1), with mean k/(N+1) and the printed variance. Q(x)=E(x-B)_+ and its convexity are correct.

The lower bound is exact before asymptotics: Jensen gives Q>=(x-mu)_+, and the beta integral in (2.3) equals (1-mu)^m. The two approximation errors are m mu-k=O(k^2/n) and m mu^2=O(k^2/n), uniformly when m and N differ from n by O(k). Thus this lower bound is e^(-k)(1+o(1)).

I checked each part of the upper bound:

- On x<=mu, Q<=sigma. Dropping (1-x)^(m-k-1)<=1 gives the bound at line 124. Its logarithm relative to e^(-k) is -k log k/2+O(k), tending to negative infinity.
- For 0<=a=x-mu<=a_1=mu k^(-1/3), Q<=a_1+sigma<=2mu k^(-1/3) eventually. The line-128 bound has logarithm relative to e^(-k) equal to -k log k/3+O(k), also tending to negative infinity.
- On a>a_1 the change of measure is exactly zeta~Beta(k+1,m-k). The normalization is (1-mu)^m. There is no missing factor in this density transformation.
- For a_1<a<mu/2, (y-a)_+<=y^2/(4a) is valid also for y<a. It gives rho<=k^(-1/3)/4. The beta lower tail is a binomial upper tail with m trials and cutoff k+1, mean k/2+O(k^2/n). Its exponential cost dominates exp(k^(2/3)/4). The weaker exponent -k phi(2)/3 used in the paper is valid eventually.
- For a>=mu/2, the size-biased beta identity is correct: t f_(k,N-k+1)(t)=mu f_(k+1,N-k+1)(t). The latter beta survival probability at 3mu/2 is P(Bin(N+1,3mu/2)<=k), with mean exactly 3k/2. Its Chernoff exponent is gamma k, where gamma=log(2/3)+1/2=0.09453489189...>0. Hence k rho tends to zero uniformly on this entire region.

The estimates require k to tend to infinity, which is ensured throughout the stated window. They do not silently assume m=N. The distinction between the auxiliary M and the actual isolation probability matters: M is an exact integral for a product of marginal refusal probabilities, not an exact finite-n isolation formula. Proposition 3.1 supplies the dependence comparison needed for the graph.

## Lemma 2.3 — SOUND

Lines 141–158. For x>=3mu/2, Q>=x-mu>=x/3, so the integrand defining J_d is at most 3^d times that for J_0. Below 3mu/2, convexity gives the monotonicity of Q/x and

    Q/x <= theta=(1+2/sqrt(k))/3.

The remaining factor is the normalized X_k density; its integral is at most one. Therefore J_d<=3^d M+theta^(k-1-d). For fixed D,

    theta^(k-1-d) <= 3^(D+1) exp(-k log 3+2 sqrt(k)) = o(e^(-k)).

The final binomial coefficient is at most k^d, giving (3k)^d e^(-k)(1+o(1)). Fixed D is essential and is respected in all uses. Uniformity over retained rank sets follows from the extremal-rank argument in Lemma 2.1; no averaging over omitted positions is assumed.

## Proposition 3.1 — GAP: repair one false counting sentence

Lines 162–208. The probability assertions are supported by the proof once the following local sentence is corrected. At line 198 the claim “at most 2 Lambda occurrences have a label on a light edge” is false without qualification. A label u can occur in three stars; one light edge incident to u then touches three occurrences, although Lambda=1. Such configurations are allowed when r>=3.

The required replacement is:

> At most 2c occurrences have a repeated label. Among occurrences with unrepeated labels, at most 2 Lambda have a label on a light edge. Consequently at most 2c+2 Lambda occurrences are not clean.

Indeed, a label of multiplicity h>=2 accounts for h occurrences and h-1 coincidences, and h<=2(h-1). After those occurrences are removed, each endpoint of a light edge accounts for at most one occurrence. The display at line 202 already excludes repeated occurrences separately. Thus this repair leaves every subsequent bound intact; it does not introduce an additional k, r, or n factor.

The remainder of the dependence argument checks out:

- (F1) holds because the stars use disjoint unordered edge sets from R to V'. Within each star, the rank labels form a uniform sample without replacement, independent of its ordered scores. Stars at different vertices remain independent even if their endpoint labels coincide: the underlying edges are different.
- (F2) conditions only each root's first k external edges and their identities. Unrevealed external edges at that root are independent Uniform[T_a,1] variables; all other unrevealed edges stay independent Uniform[0,1]. This is a regular conditional statement, not independence of different refusal events.
- If c=0, edges from distinct labels in S to W are distinct. Conditional refusal counts are then independent Bin(n-r-rk,X_(a,j)). Taking their product and using independence of labels and scores gives the lower bound with m=n-r and N=n-r-rk, both within O(k) of n. The collision union bound is O(k^2/n).
- With B=2r+6, B-1-log B>=B/2=r+3>r+1. Consequently the discarded event T>Bk/n has probability o(e^(-rk)), which is the required relative scale. Merely proving it o(1) would not have sufficed.
- Given the stars, the edges in I are independent and each is light with probability at most 2tau. The binomial/union bound (3.1) with at most 4r^2 k^2 candidate edges is valid. It does not assume I is independent of the stars.
- The sequential collision bound (3.2) accounts for sampling without replacement within each star. Its denominator n-r-k is a valid lower bound for the remaining label pool. A union over possible repeat positions gives the printed bound.
- The discarded events Lambda>=r+1 and c>=r+1 have total probability O(k^(3r+3)n^(-r-1))=o(e^(-rk)), since k-log n is bounded and r is fixed.
- For a clean occurrence, all other edges to R union S are nonstar, nonlight edges. In particular a root v_b different from its own root cannot have a star edge to that unique label. These edges cannot help reject a star score <=tau. The only remaining contributors are the edges to W.
- Conditional on the stars and the light-edge pattern, clean occurrences use distinct labels and disjoint edge sets to W. Those counts are independent; domination by Bin(n-r,x) is in the direction needed for the upper bound.
- Maximizing over the possible dirty positions does not justify multiplying arbitrary dependent probabilities. The paper correctly replaces every retained rank set by the largest ranks first. For fixed labels the repeated counts g_a are fixed, and the omission-count vectors f_a have at most (2ell+1)^r possibilities. Lemma 2.3 then bounds each integrated score product. There is no missing binom(k,d) sum beyond the factor already in that lemma.
- The total number of omissions is at most re+2gamma+2ell. A collision therefore costs at most O(k^4/n), and a light-edge contribution at most O(k^5/n), relative to the leading omission bound. Summing over fixed ell,gamma<=r makes every nonzero-interaction term negligible. The zero-interaction term is bounded by M_1^r for e=0, and by (3k)^(re)e^(-rk)(1+o(1)) in general.

This explicitly handles the shared edges and shared endpoint labels. It does not make an unsupported near-independence assertion about the original isolation indicators. Here and in applications, r and e are fixed nonnegative integer parameters (r>=1); the event at k-e is used only when that rank is positive, eventually automatic.

## Corollary 3.2 — SOUND, with Proposition 3.1 repaired

Lines 211–223. On D, the k external star edges are exactly each root's preferred edges, and internal edges are preferred by neither root. Hence I intersect D equals A_R(k) intersect D. Without D, at most r-1 preferred edges can lie inside R, so I is contained in A_R(k-r+1).

Edges inside R are independent of all edges used by A_R(p), conditionally on the stars as well as before conditioning. Given the stars, P(D^c)<=r^2 T is a valid union bound. Truncating T at tau permits multiplication by the deterministic r^2 tau. It would be wrong to replace that step by unconditional independence of D and A_R(p); the paper does not do that.

For the upper bound, split I according to D. The part on D is contained in A_R(k); the part on D^c is bounded using A_R(k-r+1), the conditional r^2 tau bound, and P(T>tau). Proposition 3.1 gives O(k^(r(r-1)) e^(-rk)) for the truncated event. Multiplication by tau=O(k/n) is negligible. The paper's O(k^(r^2+1)/n) relative bound is looser but valid. All tail errors are already o(e^(-rk)). The claimed uniform e^(-rk)(1+o(1)) follows.

## Proposition 3.3 — SOUND

Lines 225–231. This is the factorial-moment method, not Stein–Chen, so no dependency-graph or Stein–Chen hypotheses are missing. For every fixed integer r,

    E(Z_n)_r=(n)_r P(r specified vertices isolated)
              =lambda_n^r(1+o(1)).

Since lambda_n lies in the compact interval [exp(-C),exp(C)], any hypothetical sequence violating uniform convergence has a subsequence on which lambda_n converges. Along it, all factorial moments converge to the corresponding Poisson factorial moments. Ordinary moments follow by the finite Stirling-number identities, and the Poisson law is moment-determinate, for example because its moment generating function exists near zero. The usual method of moments applies; higher moment bounds also provide the uniform integrability needed in a subsequence proof.

Convergence in distribution to a distribution supported on the integers implies convergence of each integer point mass here, because every Z_n is integer valued. For a finite set of integers the mass differences tend to zero; choose that set to capture all but epsilon of the limiting Poisson mass, and bound both tails. This proves total variation convergence. The last Poisson comparison is also valid: a coupling by an independent Poisson increment gives TV(Poi(x),Poi(y))<=1-exp(-|x-y|)<=|x-y|. The contradiction establishes uniformity. No unjustified interchange of a growing moment order with n occurs.

## Lemma 4.1 — SOUND

Lines 235–256. First, the common threshold event G has the asserted high probability. For the lower threshold, Bin(n-1,ak/(n-1)) has mean ak, and the cutoff k gives exponent k(a-1-log a). For the upper threshold the mean is bk and bounding the cutoff k-1 by k gives exponent k(b-1-log b). Independently recomputed values are approximately 1.012548 and 3.543702. Multiplication by n and boundedness of k-log n give P(G^c)=O(n^(-0.0125)). No independence between different vertex thresholds is used.

On G, every edge below ak/(n-1) is retained. Thus a component vertex set S must have all s(n-s) cut edges above that threshold. A connected retained subgraph inside S has a spanning tree, and every edge of that tree is at most bk/(n-1). For sufficiently large n these thresholds lie below 1. The cut event and each internal tree event involve disjoint original edge variables, so their probabilities multiply *before* conditioning on G. The proof uses the containment in their intersection; it does not assume they remain independent after conditioning on G. Cayley's count and 1-x<=exp(-x) give (4.1) with the correct power s-1.

For each fixed 7<=s<=12, the union over all vertex sets is bounded by

    O(n^s (k/n)^(s-1) n^(-as))
      = O(n^(1-as) k^(s-1)).

At the worst exponent, s=7, 1-7a=-3/32. Summing these six sizes is bounded by O(n^(-3/32)k^11).

For every 13<=s<=n/2, including growing s, use binom(n,s)<= (en/s)^s, Cayley's s^(s-2), n-1>=n/2, and (n-s)/(n-1)>=1/2. These give the dominating series

    n/(2bk) sum_(s>=13) [2ebk exp(aC/2)n^(-a/2)]^s.

The bracket tends to zero. Its summed bound is O(n^(1-13a/2)k^12)=O(n^(-1/64)k^12), tending to zero. The exponent 13a/2=65/64 is strictly greater than one. This controls all intermediate and macroscopic component sizes; there is no implicit restriction s=O(1) in this second bound.

The extremely small exponents and large logarithmic powers mean these asymptotic estimates may be numerically useless at accessible n. That is not a failure of convergence or of uniformity.

## Lemma 4.2 — SOUND, with Proposition 3.1 repaired

Lines 258–268. For fixed 2<=s<=6, at least the first k-s+1 external edges of every vertex in S are preferred by it, eventually k>=s. If S is a component all those edges must be refused at their external endpoints, so A_S(k-s+1) is necessary. That event uses edges from S to the complement and edges with at least one endpoint outside S; it uses no edge with both endpoints in S. Therefore it is independent of the unconditioned internal low-score spanning-tree event. As in Lemma 4.1, the argument uses a necessary-event containment and does not condition the two independent events on G.

Proposition 3.1 applies with fixed r=s and e=s-1. Multiplying its bound by the tree bound gives

    O((k/n)^(s-1) k^(s(s-1)) e^(-sk))
       = O(k^(s^2-1) n^(-2s+1)).

The printed O(k^(s^2)n^(-2s+1)) is a harmless weakening. The union over at most n^s sets costs exactly the factor the paper charges, giving O(k^(s^2)n^(1-s))=o(1), including s=2. No independence between different candidate components is required.

## Section 6 and independent numerical checks — ERROR in the reported large-k integral value

### Programs, reproducibility, and resource use

The programs written for this audit are:

- `referee_numeric.py`: 45-decimal-digit mpmath integration, independent double-precision scaled SciPy integration, exact binomial-tail recurrences for the finite-n integrand, and a reproduction of the unscaled-tolerance failure. Output: `referee_numeric.out`.
- `referee_exact.py`: exhaustive enumeration of all 720 edge orders of K_4, and exact rational/symbolic checks of Lemma 2.1. Output: `referee_exact.out`.
- `referee_sim.c`: independent exact edge-order sampler. Built as `clang -O2 -std=c11 referee_sim.c -lm -o referee_sim`. Outputs: `referee_sim_*.csv` and `referee_sim_*.out`.
- `referee_analyze.py`: independent graph-level uncertainty calculations, empirical Poisson distances, and comparisons with the paper's eight connectivity entries. Outputs: `referee_analyze.out` and `referee_tables.md`.
- `referee_verify.py`: checks the report's result coverage, numerical table against the saved sample summary, and agreement between the two integration implementations. Output: `referee_verify.out`.

The main simulation commands were `./referee_sim n T seed raw.csv [minimum_k]`, with (n,T,seed) equal to (2000,3000,4562000), (3000,10000,4563000), (10000,5000,45610000), and (50000,2500,45650000). The n=1000 comparison run used (1000,15000,4561001) with minimum_k=6 and the filename `referee_sim_1000_window.csv`. An earlier, retained n=1000 run with seed 4561000 covers k=5–8. Validation at n=4 used 200000 samples and seed 4564. Python commands were `python3 referee_numeric.py`, `python3 referee_exact.py`, and `python3 referee_analyze.py`, with stdout saved to the named output files. No author program was used as an oracle.

At most two computations ran concurrently, with one thread per computation. The largest simulation invocation took 89 seconds and reported peak RSS 73,154,560 bytes, below 70 MiB; its hash table used 64 MiB. Every invocation finished well below five minutes. The Python checks use small scalar integrals or modest sample arrays, not dense n-by-n graph matrices. The calls requested nice priority, but the sandbox printed `setpriority: Operation not permitted`; those requests did not establish a changed process priority. Resource and wall-time limits were still respected.

The sampler uses the fact that independent continuous scores induce a uniformly random permutation of the unordered edges. It repeatedly draws a uniform unordered pair, rejecting pairs seen before. Conditional on the current prefix, the next accepted edge is uniform among unseen edges. For each vertex, its first K incident edges in that order are exactly its K smallest-score edges. Sampling stops only when every vertex has at least K incidences. If an edge arrives with endpoint incident ranks i,j, it is retained at budget k exactly when max(i,j)<=k. Recording these ranks gives coupled samples for four budgets. There is no truncation in score, independent-neighbor substitution, Poisson approximation, or omission of unseen edges that could change the first K preferences. Union-find computes components of the retained graph.

### Exact small-graph and order-statistic checks

`referee_exact.out` contains:

    n=4 k=1: p1=2/5,  p2=2/15, P(Z=0)=1/5
    n=4 k=2: p1=1/15, p2=0,    P(Z=0)=11/15
    n=4 k=3: p1=0,    p2=0,    P(Z=0)=1

The independent C sampler gives P(Z=0)=0.198645, 0.733460, and 1 at those three budgets, consistent with enumeration. At k=1 the exact Z histogram is 576 orders with Z=2 and 144 with Z=0; at k=2 it is 192 orders with Z=1 and 528 with Z=0. The C histograms have precisely those supports. At k=1 no graph is connected, including graphs without isolates.

This enumeration also exposes an important distinction: for n=4,k=2, the auxiliary integral with m=n-1,N=n-2 is M=1/21, whereas the actual isolation probability is 1/15. Thus an interpretation of the paper's integral as an exact finite-n graph isolation formula would be false. The numbered Lemma 2.2 defines M as a product expectation, so it does not make that false assertion. Shared edges between the root's preferred neighbors account for the distinction, and Section 3 handles them asymptotically.

For Lemma 2.1 with m=7,k=3,g(x)=x^2, exact integrations gave:

| Retained ranks | Actual expectation | Equality/bound in Lemma 2.1 |
|---|---:|---:|
| 1,2,3 | 7/3861 | 7/3861 |
| 1,3 | 1/132 | 1/33 |
| 2,3 | 1/44 | 1/33 |
| 3 | 1/6 | 1/6 |

### High precision one-root integrals

For finite n, `referee_numeric.py` evaluates (2.1) with q(x)=P(Bin(N,x)>=k), using Q(x)=x F_B(x)-mu F_(B+)(x). It scales the integration variable to s=nx and the result by e^k before integrating. The finite binomial CDFs are evaluated by a direct recurrence at 45-digit precision, independently of the beta CDF implementation used for the double-precision cross-check. The integral above the chosen upper endpoint is bounded using Q(x)<=x and (1-x)^(m-k-1)<=exp(-(m-k-1)x); all reported scaled tail bounds are below 1.1e-81. The two evaluations agree within 2e-12 for the values below.

| n | k | M e^k, m=N=n (authors' check convention) | M e^k, m=n-1,N=n-2 (full marginal refusal convention) |
|---:|---:|---:|---:|
| 1000 | 6 | 1.076249092379 | 1.070082270005 |
| 3000 | 8 | 1.042532672588 | 1.039817337181 |
| 10000 | 9 | 1.035558112708 | 1.034642842858 |
| 50000 | 11 | 1.021856706067 | 1.021634175459 |
| 10000000 | 16 | 1.006412690550 | 1.006411084475 |

The values with m=N=n agree with the supplied `checks_out.txt` wherever the same n,k appears. These are high precision evaluations of M, not an unjustified claim of exact finite-n isolation probabilities. Actual probabilities are checked separately by exact enumeration and graph simulations.

For the Poisson-process integral I_k, the independent evaluations give:

| k | Correct I_k e^k | Supplied `simulate_out.txt` |
|---:|---:|---:|
| 6 | 1.089616178362316 | 1.08961618 |
| 8 | 1.050991722048099 | 1.05099172 |
| 10 | 1.029742993627038 | 1.02974299 |
| 20 | 1.002401097791293 | 1.00238041 |
| 25 | 1.000716673640136 | 1.00060683 |
| 30 | 1.000216941725512 | 1.00003479 |

The k=30 value at line 294 must therefore be 1.00022 at five decimal places, not 1.00003. The k=20 text rounded to 1.0024 is still correct at its stated precision, but the higher precision supplied output is not.

The failure is reproducible without executing author code. Independently evaluating the unscaled integrand with default SciPy absolute tolerance gives 1.000034787331 after multiplying by e^30, exactly the problematic value. Its returned absolute integration error is about 9.74e-14, comparable with I_30 itself. Default absolute error control does not resolve an integral on that scale. Integrating e^k times the integrand with absolute and relative tolerances 2e-12 gives 1.000216941726, agreeing with 45-digit integration. The same problem explains the k=20 and 25 discrepancies. This is a numerical error, not evidence against the saddle-point proof.

### Actual one- and two-vertex isolation probabilities

For each independent graph, I record Z and (Z)_2. Exchangeability makes

    mean(Z)/n                  an unbiased estimator of p1,
    mean(Z(Z-1))/(n(n-1))      an unbiased estimator of p2.

Standard errors below use graphs as the independent sampling units. They do not treat different vertex indicators within one graph as independent. These are actual LK(n,k) estimates, separate from M.

| n | k | p1/e^(-k), estimate ± SE | p2/e^(-2k), estimate ± SE |
|---:|---:|---:|---:|
| 1000 | 6 | 1.0740 ± 0.0054 | 1.1547 ± 0.0125 |
| 2000 | 7 | 1.0583 ± 0.0137 | 1.1027 ± 0.0317 |
| 3000 | 8 | 1.0385 ± 0.0100 | 1.0558 ± 0.0246 |
| 10000 | 9 | 1.0664 ± 0.0131 | 1.1337 ± 0.0321 |
| 50000 | 10 | 1.0153 ± 0.0134 | 1.0315 ± 0.0300 |
| 50000 | 11 | 1.0260 ± 0.0221 | 1.0417 ± 0.0560 |

Finite-n corrections are measurable, especially below the central integer budget, and the simulation noise does not resolve a monotone trend at every listed point. The paired estimate has greater relative uncertainty. These observations are compatible with the claimed limits, but do not prove them. At n=3000,k=8 the actual one-root estimate agrees closely with the finite integral's ratio 1.039817; at n=50000,k=11 it agrees with 1.021634 within sampling error. The small-graph calculation above shows why no exact equality is asserted.

### Isolate distribution and connectivity

In this table parentheses contain one graph-level standard error. The TV column is the distance between the empirical Z histogram and Poi(lambda), not the unknown population TV distance. It includes sampling error. The last column counts disconnected samples with Z=0. The complete raw data and all ratio estimates are retained in the CSV and output files.

| n | k | samples | mean Z (SE) | lambda | variance | P(conn) (SE) | exp(-lambda) | empirical TV | Z=0, disconnected |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 1000 | 6 | 15000 | 2.6623 (0.0133) | 2.4788 | 2.6622 | 0.0674 (0.0020) | 0.0838 | 0.0447 | 50 |
| 1000 | 7 | 15000 | 0.9409 (0.0079) | 0.9119 | 0.9343 | 0.3863 (0.0040) | 0.4018 | 0.0136 | 32 |
| 1000 | 8 | 15000 | 0.3408 (0.0048) | 0.3355 | 0.3403 | 0.7107 (0.0037) | 0.7150 | 0.0038 | 8 |
| 1000 | 9 | 15000 | 0.1239 (0.0029) | 0.1234 | 0.1237 | 0.8835 (0.0026) | 0.8839 | 0.0005 | 1 |
| 2000 | 6 | 3000 | 5.3473 (0.0421) | 4.9575 | 5.3185 | 0.0050 (0.0013) | 0.0070 | 0.0782 | 2 |
| 2000 | 7 | 3000 | 1.9300 (0.0250) | 1.8238 | 1.8717 | 0.1360 (0.0063) | 0.1614 | 0.0294 | 5 |
| 2000 | 8 | 3000 | 0.6737 (0.0149) | 0.6709 | 0.6667 | 0.5097 (0.0091) | 0.5112 | 0.0059 | 4 |
| 2000 | 9 | 3000 | 0.2487 (0.0091) | 0.2468 | 0.2496 | 0.7810 (0.0076) | 0.7813 | 0.0037 | 0 |
| 3000 | 7 | 10000 | 2.8959 (0.0168) | 2.7356 | 2.8247 | 0.0543 (0.0023) | 0.0649 | 0.0384 | 8 |
| 3000 | 8 | 10000 | 1.0451 (0.0101) | 1.0064 | 1.0220 | 0.3457 (0.0048) | 0.3655 | 0.0191 | 11 |
| 3000 | 9 | 10000 | 0.3775 (0.0061) | 0.3702 | 0.3776 | 0.6850 (0.0046) | 0.6906 | 0.0054 | 2 |
| 3000 | 10 | 10000 | 0.1350 (0.0037) | 0.1362 | 0.1336 | 0.8730 (0.0033) | 0.8727 | 0.0009 | 0 |
| 10000 | 8 | 5000 | 3.5378 (0.0266) | 3.3546 | 3.5317 | 0.0316 (0.0025) | 0.0349 | 0.0444 | 2 |
| 10000 | 9 | 5000 | 1.3160 (0.0162) | 1.2341 | 1.3108 | 0.2666 (0.0063) | 0.2911 | 0.0250 | 2 |
| 10000 | 10 | 5000 | 0.4726 (0.0097) | 0.4540 | 0.4713 | 0.6222 (0.0069) | 0.6351 | 0.0130 | 0 |
| 10000 | 11 | 5000 | 0.1750 (0.0059) | 0.1670 | 0.1752 | 0.8396 (0.0052) | 0.8462 | 0.0066 | 0 |
| 50000 | 9 | 2500 | 6.4488 (0.0503) | 6.1705 | 6.3195 | 0/2500 successes | 0.0021 | 0.0477 | 0 |
| 50000 | 10 | 2500 | 2.3048 (0.0304) | 2.2700 | 2.3088 | 0.0988 (0.0060) | 0.1033 | 0.0105 | 0 |
| 50000 | 11 | 2500 | 0.8568 (0.0184) | 0.8351 | 0.8494 | 0.4220 (0.0099) | 0.4338 | 0.0121 | 0 |
| 50000 | 12 | 2500 | 0.3072 (0.0113) | 0.3072 | 0.3210 | 0.7376 (0.0088) | 0.7355 | 0.0051 | 0 |

For the zero-success row, the usual plug-in standard error is misleadingly zero; the 95% Wilson interval is [0,0.001534]. Thus this sample does not measure rare connectivity accurately. At n=50000,k=11, the empirical Poisson TV is 0.0121; fitting the Poisson mean to the sample reduces it to 0.00554. At n=10000,k=9, the corresponding distances are 0.0250 and 0.0115. Variances are generally close to the empirical means. A substantial part of the finite-n departure is the correction to the isolate mean, rather than an obviously different distributional shape. This is a numerical observation, not a theorem about the optimal finite-n mean.

The connectivity correction is visible: at n=10000,k=9 the difference from exp(-lambda) is about -0.0245, and at n=50000,k=11 it is about -0.0118. Below the central budget, relative errors in rare connectivity can be larger. These are compatible with an o(1) statement, which gives no claimed finite-n accuracy.

### Comparison with the paper's simulations

All eight reported connectivity estimates are statistically compatible with these independent simulations at the precision of the paper's small samples. Using the rounded one-standard-error entries in Table 1, the largest discrepancy is about 1.54 combined standard errors (n=1000,k=9). Examples are 0.3457±0.0048 here versus 0.395±0.035 in the paper at n=3000,k=8, and 0.0543±0.0023 here versus 0.035±0.013 at n=3000,k=7. Those differences do not establish a simulation error in the paper. The exact comparisons are in `referee_analyze.out`.

The observation in line 294 that none of the authors' n=3000 samples, or their n=1000,k>=7 samples, was disconnected without isolates is a finite-sample observation, not an exact property. The larger independent runs find such graphs: 11/10000 at n=3000,k=8 and 32/15000 at n=1000,k=7, for example. Seeing none in 200 or 300 trials is unsurprising. These occurrences also explain why checking only Z=0 would have been an inadequate connectivity simulation; the independent sampler checks actual components.

## Earlier results and use of citations

No cited source text other than this manuscript was supplied, and browsing was forbidden. I therefore cannot independently authenticate the precise statements, bibliographic details, or theorem numbers of the external papers. The following judgments concern what this text says and how its proof uses those statements.

La–Kabkab is credited at lines 42 and 358–359 with introducing this bilateral model and with a multiplicative threshold conjecture. The definition in this manuscript consistently requires preference at both ends. No result from La–Kabkab is used as an unproved step in Sections 2–5.

Dabirian–Subramanian is quoted at lines 36 and 42–47 for sufficient conditions displaced by ±t log log n sqrt(log n), with t>1/2 in magnitude and the appropriate signs. As quoted, those conditions address sequences outside a much wider band and do not themselves settle slowly diverging offsets or finite offsets. The present proof neither assumes they do nor depends on them: the monotonic comparison in Corollary 1.2 supplies the missing extension. Line 288 is consistent with the quoted bounds. Verification that the external paper states exactly those conditions remains outside this no-browsing audit.

Cooper–Frieze is mentioned at line 47 for the rule retaining an edge when either endpoint prefers it. The manuscript distinguishes that union rule from the bilateral intersection rule and does not transfer a connectivity result between them. Its citation is contextual, not a load-bearing input. There is no apparent misuse of that distinction in the proof. The precise external model/statement cannot be checked from the bibliography alone.

## Corrections to make

1. **PAPER.tex line 198, Proposition 3.1:** Replace the unrestricted “at most 2 Lambda occurrences” sentence by the qualified statement about *unrepeated* occurrences quoted above, and state the total bound 2c+2 Lambda. The existing sentence is false for a label repeated in three stars. This is the local proof gap; the corrected argument proves the same proposition.

2. **PAPER.tex line 294, value of I_30 e^30:** Replace 1.00003 by 1.00022, or give 1.00021694 at eight decimal places. The displayed k=10 and rounded k=20 values can remain. Regenerate the high precision outputs for k=20,25,30; correct values appear in the integral table above.

3. **code/simulate.py, first integral loop, the unscaled `integrate.quad` call:** Integrate the ratio integrand exp(k)*f(s) directly, with explicit absolute and relative tolerances appropriate to that order-one quantity, or set an adequately small absolute tolerance on the unscaled integral. Inspect returned error estimates. Its default absolute tolerance does not justify the digits printed in `code/simulate_out.txt`. This correction is necessary to support Section 6's numerical statement.

4. **PAPER.tex lines 36 and 64–68, description of the “exact integral formula”:** Clarify that the exact formula is for the auxiliary independent-refusal product M, and that its comparison with finite-n graph isolation uses Proposition 3.1/Corollary 3.2. An unqualified identification with the exact isolation probability would be wrong: n=4,k=2 gives M=1/21 but P(isolated)=1/15. Lemma 2.2 itself defines M correctly; no change to its statement is needed.

No correction is needed to the integer rounding, monotonicity argument, the component union bounds, or the factorial-moment-to-total-variation step. External source authentication should not be described as completed by this audit.

Task: “Be a hard, independent referee” of PAPER.tex — 12 November 2026, 18:38:47 (+04), final consistency check.
