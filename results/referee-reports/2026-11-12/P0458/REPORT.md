Overall verdict: SOUND

I found no false theorem, missing probabilistic argument, or incorrect constant in the supplied source. I checked the conditioning, the dependence through shared edges, the error bounds, and the moment arguments independently. Exact calculations and simulations support the stated results. This verdict concerns `PAPER.tex` and the supplied files; it does not certify the contents or theorem numbering of external references, which were not available here. No browsing was used, and none of the authors' programs was executed or imported.

Line numbers below refer to `PAPER.tex`. There is a numbering discrepancy in the request: because the Gini remark uses the shared theorem counter, the source numbers it **Remark 7.2** and numbers `cor:ck` **Corollary 7.3**, rather than Corollary 7.2. Both are reviewed below.

## Theorem 2.1 — SOUND

Lines 70–79 and 187–198. The hypotheses imply

$$
s_n^2\ge \tfrac12\min(k,n-k)\longrightarrow\infty.
$$

Lemmas 2.4 and 2.5 give, respectively, an error tending to zero in $L^2$ after division by $s_n$, and convergence of the conditional mean in law and in its first two moments. In particular, writing $A_n=H/s_n$ and $B_n=kq_n(X)/s_n$,

$$
\|A_n-B_n\|_2\to0,\qquad \sup_n\|B_n\|_2<\infty.
$$

Consequently the means differ by $o(1)$, and

$$
|\mathbb E A_n^2-\mathbb E B_n^2|
\le\|A_n-B_n\|_2(\|A_n\|_2+\|B_n\|_2)\to0.
$$

Thus the passage from conditional means to unconditional second moments is justified; convergence in distribution alone is not being used to infer moment convergence. The positive variance constant justifies standardization by the actual finite-$n$ variance. Since $D=k-H$, the minus sign in the limiting standardized degree is correct.

The calculation of the normal constants is correct. The two positive parts have marginal variance 2 and correlation $1/2$, so the factor of 2 in their product moment is necessary and is present. Independent 60-digit quadrature confirms both moments and the variance; see the checks below.

## Section 2 representation of $H$ — SOUND

Lines 81–92. The cutoff is the **$(k+1)$st**, not the $k$th, root order statistic. Its law is $\mathrm{Beta}(k+1,n-k-1)$. Conditioning on this cutoff and the preferred vertex set makes the $k$ labelled scores below the cutoff independent uniforms on $(0,X)$. Edges away from the root retain their original independent laws.

The $k$th order statistic among the other $n-2$ edges at a candidate has law $\mathrm{Beta}(k,n-k-1)$. Its comparison with the root edge correctly decides rejection. Averaging a uniform score on $(0,x)$ gives

$$
q_n(x)=\mathbb P(U>T\mid X=x)=\frac{\mathbb E(x-T)_+}{x}.
$$

The notation for a vertex in the random set $S$ is understood after conditioning on its membership. Removing the conditioning on $S$ introduces no extra term: the conditional means and joint laws in use are invariant under the choice of $S$. The excluded case $k=n-1$ is handled separately.

## Lemma 2.2 — SOUND

Lines 96–115. Given $X,S,W$, the two rejection decisions use disjoint remaining edge sets and independent root scores. Edges to a common third vertex are distinct independent edges; a common endpoint does not make them dependent. Averaging over $S$ preserves the asserted conditional independence because the two conditional probabilities depend only on $X,W$.

With $N_u\sim\mathrm{Bin}(n-3,u)$, rejection requires $N_u+\mathbf1_{\{w<u\}}\ge k$. The difference between the two binomial tails is exactly the mass at $k-1$. The density identity

$$
\mathbb P(N_u=k-1)=f_T(u)/(n-2)
$$

is correct, including $k=1$ and $k=n-2$. Integration over $u\in(0,x)$ yields the displayed $p_x(w)$. Conditioning on $W$ then gives the covariance as a variance, hence its nonnegative sign. Popoviciu's inequality applies to an interval of length $F_T(x)/((n-2)x)$, giving the stated factor $1/4$.

The independent exact polynomial checks verify the conditional mean identity and the resulting variance calculation for every $3\le n\le12$, $1\le k\le n-2$.

## Lemma 2.3 — SOUND

Lines 117–132. There are $k(k-1)$ ordered distinct pairs in the variance of a sum. This coefficient is correct. Applying total variance gives the last term $k^2\operatorname{Var}q_n(X)$, not $k\operatorname{Var}q_n(X)$. The upper bound follows by discarding $1-q_n(X)\le1$ and replacing $k(k-1)$ by $k^2$.

The exact formula agrees with a separate two-root-edge integration and with exhaustive enumeration at $n=4,5$. For example,

$$
\mathbb ED_{5,2}=52/35,\qquad
\operatorname{Var}D_{5,2}=4889/11025.
$$

## Lemma 2.4 — SOUND

Lines 136–154. The lower-cutoff event is the stated binomial upper tail. The exponential bound using $t=\log2$ actually gives the slightly stronger $2^{-k-1}e^{k/2}$, so the advertised constant is valid.

On $G_n$, the covariance contribution is at most $n^2/(n-2)^2\le4$. The variables $X,T$ in the estimate for $\mathbb E|X-T|$ are independent, as stipulated earlier. Their variances are each bounded by $2s_n^2/n^2$, and their mean difference is at most $1/n$. These give $4s_n+2$ for the mean contribution. On the complement, the crude bound $\operatorname{Var}(H\mid X)\le k^2$ suffices. The total is precisely $6+4s_n+k^2e^{-ck}$.

The final little-$o$ assertion remains valid near the dense boundary. If $k\le n/2$, divide the exponential term by $s_n^2\ge k/2$; if $k>n/2$, its numerator is at most $n^2e^{-cn/2}$. Thus there is no unhandled assumption that $k/n$ stays away from 1.

## Lemma 2.5 — SOUND

Lines 158–185. The rescaling factor in (2.4), $k/(nX)$, is correct.

For both beta variables the binomial order-statistic identity gives a triangular-array binomial CLT. The variance tends to infinity, so bounded threshold/mean shifts disappear. The two ratios controlling whether $p_n+\sigma_nu$ lies inside $(0,1)$ tend to zero under the stated hypotheses. This works even when $k/n\to0$ or 1.

The beta variance ratios tend to 1. The centered-to-uncentered shifts, $1/s_n$ and $k/((n-1)s_n)$, tend to zero. The kurtosis expression and bound are correct, implying bounded fourth moments of $U_n,V_n$ and their limits 3.

The Skorokhod coupling is used only to compare the **deterministic functions** $g_n,g$. Bounded second moments imply uniform integrability of the coupled absolute differences, so their expected absolute difference tends to zero. The Lipschitz estimate is uniform over all real $u$. No independence between that coupling and $U_n$ is needed. Tightness gives $k/(nX)\to1$ in probability, completing the distributional argument.

The uniform-integrability argument for the squares is sufficient. On $G_n$ there is a fourth-moment majorant. On $G_n^c$ the expected square tends to zero. A sequence of nonnegative integrable variables whose expectations tend to zero is uniformly integrable after including its finitely many initial terms. Thus this last step is not merely a small-probability assertion; the potentially large values are controlled in expectation. First and second moment convergence follow.

## Remark 2.6 — SOUND

Lines 200–202. The estimate $\sqrt{k}-s_n\le k^{3/2}/n\to0$ is valid in the stated regime. The remark claims only agreement at the first-order deficit scale, not recovery of the $k^{-1/2}$ correction in the cited expansion. That distinction is correct.

## Section 3, displays (3.1)–(3.2) and tail assertions — SOUND

Lines 204–214. The map $g$ is strictly increasing from 0 to infinity because $g'=\Phi>0$. The standardized degree is a decreasing transform of $Z$, which explains the $1-\Phi$, rather than $\Phi$, in its CDF. Differentiation gives the displayed density with denominator $\Phi(y_x)$.

Mills' ratio gives the divergent density at the finite upper endpoint. At the other end, $g(y)-y$ decays faster than any inverse power as $y\to\infty$; the stated Gaussian lower-tail description follows. The exact endpoint is $1.0464333934\ldots$, and the law is nonnormal.

## Lemma 4.1 — SOUND

Lines 230–239. The external-edge counts have $n-1-j$ trials and use disjoint sets of edges for different candidates, so they really are independent. Adding the internal candidate edges can only prevent rejection. This gives the direction $Q_n\le\prod\beta_n$.

For a pair, an edge has no effect on either decision when its score is at most $1-\max(y_a,y_b)/n$. The probability of failure is $max(y_a,y_b)/n$, not the sum of the two thresholds. A union bound gives exactly the claimed upper error. The proof uses no false independence of the internal edges' effects on their two endpoints.

## Theorem 4.2 — SOUND

Lines 218–228 and 241–283. The upper-tail coordinates, the gamma shape $r$, and the rejection threshold “at most $r-1$” are correct.

For an ordered tuple of $j$ candidates, the root prefers all of them precisely when at least $r$ **other** root coordinates lie below their minimum. Conditional on their $y_a$'s, this event uses only root edges, whereas their rejections use only non-root edges. This proves the factorization $P_nQ_n$. The factorial coefficient $(n-1)_j/n^j$ includes the coordinate densities correctly.

The pointwise limit of $Q_n$ follows from Lemma 4.1. For the dominating function, if $n\ge2(r+j)$ and $i\le r-1$, then

$$
n-1-j-i\ge n-j-r\ge n/2.
$$

Thus each binomial mass is bounded by $y^ie^{-y/2}/i!$. Extending the integrand by zero outside $(0,n)^j$ makes dominated convergence on the fixed space $(0,\infty)^j$ immediate. The product bound is integrable. Tonelli/Fubini then gives $\mathbb E\Lambda_r(A_r)^j$. In particular, the preceding Poisson-process description is backed by a proof of the count law and is not an unsupported independent-marking assumption.

Since $0\le\Lambda_r\le r$, the limiting mixed Poisson law has a finite MGF for every positive argument and is moment determinate. Convergence of factorial moments gives convergence of every integer moment through the Stirling-number identities, and the method of moments gives distributional convergence. Uniform integrability of any fixed power can also be obtained from convergence/boundedness of a higher integer moment. Even if “all moments” is interpreted to include every positive real power, that conclusion follows by this higher-moment bound.

The generating function, the extra Poisson contribution $\mu_r$ to the variance, and both gamma-integral moment sums are correct. Omitting that Poisson variance term would give a false answer; the paper includes it. Positive $\mu_r$ ensures positive limiting variance, so the displayed standardized limit is valid.

## Proposition 4.3 — SOUND

Lines 285–304. For independent equal-shape gamma variables, $S=A+G$ and $B=A/S$ are independent, with laws $\Gamma(2r,1)$ and $\mathrm{Beta}(r,r)$. Symmetry gives $\mathbb E(G-A)_+=\frac12\mathbb E|G-A|$. The transformed beta density and the integration of $|1-2B|$ give the displayed factor $1/(r2^{2r-1}B(r,r))$. The factor $r$ cancels as claimed. The duplication formula gives the gamma-ratio expression.

Independent exact arithmetic confirms the finite-sum and closed-form means for $r=1,\ldots,60$. The values $(\mu_1,M_{2,1},\nu_1)=(1/2,1/3,7/12)$ and $(\mu_2,M_{2,2},\nu_2)=(3/4,22/27,433/432)$ are correct. The endpoint squares $3/7$ and $243/433$ differ. Both endpoints are atoms with positive probability, so this does distinguish the two laws.

## Theorem 5.1 — SOUND

Lines 308–318. The conditional mean satisfies $\Lambda_r(A_r)/\sqrt r=h_r(U_r)$ exactly. The gamma CLT and bounded second moments give uniform convergence of the deterministic functions $h_r$ by the same Lipschitz/coupling argument as before. The limit is $g(-Z)$, which has the same law as $g(Z)$; there is no sign error.

The bound $h_r(u)\le|u|+1$, together with $\mathbb E U_r^4=3+6/r$, gives uniform integrability of the squared conditional means. Hence $\mu_r=O(\sqrt r)$. Conditional Poisson variance then implies

$$
\mathbb E(H_r-\Lambda_r(A_r))^2/r=\mu_r/r\to0.
$$

This proves both moment convergence claims as well as weak convergence. Standardization follows because the limiting variance constant is positive.

## Proposition 6.1 — SOUND

Lines 324–340. Removing the $k-1$ internal candidate edges leaves $n-1-k$ external edges at each candidate. These external sets are disjoint. The event that all internal scores exceed $X$ makes their removal harmless, and its failure probability is at most $\binom{k}{2}\mathbb E X=\binom{k}{2}(k+1)/n$.

The binomial-to-Poisson total-variation bound is valid with the displayed constants. Integrating $y^2/n+(k+1)y/n$ over $0<y<nX$ and dividing by $nX$ gives exactly the error $(nX)^2/(3n)+(k+1)nX/(2n)$. Tightness of $nX\Rightarrow\Gamma(k+1,1)$ makes that error vanish in probability. Continuity of $q_\infty$ and bounded binomial mass functions identify the mixture law.

All moments converge because the degrees are bounded by the fixed integer $k$. The stated conditional-variance lower bound is strictly positive since $0<q_\infty(x)<1$ for every positive $x$. Consequently standardizing the fixed-$k$ limit is legitimate. This is a self-contained proof, independently of the EWT citation.

## Theorem 6.2 — SOUND

Lines 342–355, with the usual asymptotic interpretation $n\to\infty$. The extraction argument covers the potentially troublesome oscillating cases:

1. If $k$ has a bounded infinite subsequence, one integer value occurs infinitely often; extract that constant value. Otherwise extract $k\to\infty$.
2. On the latter subsequence, if $r=n-1-k$ has a bounded infinite subsequence, extract one constant $r\ge0$. For $r\ge1$, Theorem 4.2 applies. For $r=0$, the degree is deterministic and standardization is undefined.
3. Otherwise extract $r\to\infty$, so both $k\to\infty$ and $n-k=r+1\to\infty$; Theorem 2.1 applies.

Thus bounded but nonfixed $k$, and bounded but nonfixed $r$, do not create additional laws. To see that **every already existing weak subsequential limit** is covered, apply these extractions inside its convergent subsequence. Every further subsequence still has that same limit, and one of the displayed results identifies it. No assertion of uniformity in fixed-$r$ or fixed-$k$ asymptotics is needed for this argument.

The alternating $r=1,2$ example has different limits as claimed. The $k=n-1$ case is correctly excluded from statements about a defined standardized random variable.

## Proposition 7.1 — SOUND

Lines 359–371. Under simultaneous score reversal, every vertex's preferred $k$-set is the complement of its preferred $r=n-1-k$-set. The identity

$$
D_{n,k}=k-I'+D'
$$

holds for each realization with distinct scores, not just in expectation. Hence $H_{n,k}\overset d=I_{n,r}-D_{n,r}$. Exchangeability of the neighbors gives $\mathbb E I_{n,r}=r$, proving the mean symmetry. It is important that the joint pair $(I_{n,r},D_{n,r})$, not independent copies of its marginals, occurs on the right; the paper uses the joint pair correctly.

Independent rational integration verifies all budgets through $n=9$. Exhaustive score-order enumeration at $n=4,5$ also verifies the stronger equality in law. A larger-$n$ mean-symmetry simulation is recorded below.

## Remark 7.2 — SOUND

Lines 373–383. The beta-density change of measure has the correct constant $n-1$. For independent identically distributed continuous variables on $[0,1]$,

$$
\mathbb E(T'-T)_+=\int_0^1F_T(t)(1-F_T(t))\,dt.
$$

The beta parameters swap under $T\mapsto1-T$, so this proves the symmetry a second way. At $k=1$, direct integration gives $(n-2)/(2n-3)$ as stated.

## Corollary 7.3 (`cor:ck`; Corollary 7.2 in the request) — SOUND

Lines 385–393. Applying the fixed-complement theorem to budget $n-1-k$, with the original fixed $k$ as its complement, is valid. First-moment convergence is available from Theorem 4.2, so the limit comparison proves $c_k=\mu_k$, given the cited earlier mean asymptotic. Independently, the two explicit expressions reduce algebraically to $(2k-1)!/((k-1)!^2,2^{2k-1})$, making the identity independent of that citation.

The subsequent distinction between complementary-budget laws is correct: the fixed-budget-1 deficit is Bernoulli with limiting parameter $1/2$, whereas the fixed-complement-1 deficit has variance $7/12$.

## Section 8 — SOUND; computational and formalization scope noted below

Lines 395–434. The independent checks reproduce all printed deterministic numerical values examined, including every row of Table 1. The supplied `checks_output.txt` contains 52 reported passes; I did not treat that transcript as independent verification or execute the authors' code. My simulations use different seeds and naturally do not reproduce their particular sample estimates.

### Independent programs and methods

All referee programs and their outputs are in this folder. They import no code from `code/`.

| Program | Output | Purpose |
|---|---|---|
| `referee_exact.py` | `referee_exact.txt`, `referee_exact.json` | Rational one-edge and two-edge integrations; small-$n$ symmetry; exact finite-$n$ moments |
| `referee_constants.py` | `referee_constants.txt` | Direct normal integrations at 60 decimal digits |
| `referee_check_lemmas.py` | `referee_check_lemmas.txt` | Exact polynomial checks of the covariance/variance formulas and auxiliary inequalities |
| `referee_enumerate.c` | `referee_enumerate_4.txt`, `referee_enumerate_5.txt` | Exhaustive enumeration of 720 and 3,628,800 score orders |
| `referee_numeric.py` | `referee_numeric.txt`, `referee_numeric.json` | Separate one-/two-edge numerical integration, including all Table 1 rows |
| `referee_pairs.c`, `referee_simulate.py` | `referee_sim_1000.txt`, `referee_sim_10000.txt`, `referee_sim_20000.txt`, matching JSON and sample NPZ files | Root-degree simulations, including all shared candidate edges |
| `referee_validate.py` | `referee_validate.txt` | Full-graph simulation cross-checks and complementary-budget simulation |
| `referee_lean_audit.py` | `referee_lean_audit.txt` | Inspect the supplied formal statements and distinguish them from a fresh Lean build |
| `referee_summary.py` | `referee_summary.txt` | Summarize the saved simulations without rerunning them |

For a method independent of the cutoff/covariance formulas, put

$$
f(u)=\mathbb P(\mathrm{Bin}(n-2,u)\le k-1).
$$

Conditioning on one root-edge score makes the endpoint decisions independent, giving

$$
\mathbb ED=(n-1)\int_0^1f(u)^2\,du,\qquad
\mathbb EH=(n-1)\int_0^1f(u)(1-f(u))\,du.
$$

For two root scores $u<v$, the probability that the root accepts both is $C(v)=\mathbb P(\mathrm{Bin}(n-3,v)\le k-2)$. Put $A(u)=\mathbb P(\mathrm{Bin}(n-3,u)\ge k)$, $B(u)=\mathbb P(\mathrm{Bin}(n-3,u)\ge k-1)$. Integrating their shared non-root edge gives joint rejection probability

$$
uB(u)B(v)+(v-u)A(u)B(v)+(1-v)A(u)A(v).
$$

Integrate this against $2C(v)$ on $0<u<v<1$ and multiply by $(n-1)(n-2)$ to obtain $\mathbb E(H)_2$. The exact code also implements the corresponding acceptance formula. These derivations do not use Lemma 2.3. The separate polynomial implementation of that lemma agrees for 55 parameter pairs.

Numerical quadrature used 192 and 320 Gauss–Legendre nodes, with explicit concentration-scale integration ranges. The largest difference between the two orders in a normalized reported moment was $7.5\times10^{-12}$. Exact anchors at $(12,4),(12,8),(40,20),(80,30),(80,78)$ agree within $7.3\times10^{-13}$ in unnormalized moments. These are numerical checks, not interval-certified integration bounds.

### Normal constants

`referee_constants.txt` gives:

```text
E g(Z)   = 0.5641895835477562869480794515607725858440506293289989
E g(Z)^2 = 0.6089977810442293580889965824898180540320265735166537
Var g(Z) = 0.2906878948604386865512290557447893299631072820357408
endpoint = 1.04643339342766910384734244302007268566320071
```

The absolute discrepancies from the three claimed exact expressions are below $4\times10^{-62}$ at working precision. This more than meets the requested 30-digit check.

### Exact mean symmetry

The following are $\mathbb EH_{n,k}$ in increasing order of $k=1,\ldots,n-2$; the omitted complete-budget value $k=n-1$ is zero in every row.

| $n$ | Exact deficits for budgets $1,\ldots,n-2$ |
|---|---|
| 3 | $1/3$ |
| 4 | $2/5, 2/5$ |
| 5 | $3/7, 18/35, 3/7$ |
| 6 | $4/9, 4/7, 4/7, 4/9$ |
| 7 | $5/11, 20/33, 50/77, 20/33, 5/11$ |
| 8 | $6/13, 90/143, 100/143, 100/143, 90/143, 6/13$ |
| 9 | $7/15, 42/65, 105/143, 980/1287, 105/143, 42/65, 7/15$ |

Every required complementary pair agrees exactly. If budget zero is defined in the natural way, both endpoint deficits are zero and the symmetry extends to that pair too.

The exhaustive enumerator found the following $n=5$ counts for $H=0,1,2,3,4$, out of 3,628,800 orders:

```text
k=1: 2073600,1555200,0,0,0
k=2: 2113920,1163520,351360,0,0
k=3: 2384640,967680,241920,34560,0
```

Each array equals the enumerated law of $I-D$ at the complementary budget. The $n=4$ checks also pass.

At $n=1000$, independent samples of 60,000 root degrees at each of budgets 250 and 749 gave deficit means 7.711233 and 7.627950. Their difference is 0.083283 with estimated standard error 0.043085, or 1.93 standard errors. The common finite-$n$ mean from integration is 7.720012. The budget-749 estimate alone is about three standard errors below that value; it is recorded rather than discarded or reseeded. This is a modest Monte Carlo fluctuation in an auxiliary check, not evidence against the exact identity.

### Simulation construction and its approximation error

For interior budgets I sample $X\sim\mathrm{Beta}(k+1,n-k-1)$. Of the $k$ independent preferred scores on $(0,X)$, I retain those above the deterministic threshold $a=\max(0,k/n-8s_n/n)$. Conditional on their number $m$, their scores are independent uniforms on $(a,X)$. At each retained endpoint, edges to the $n-1-m$ other non-root vertices give an independent binomial count. Every edge among retained endpoints is generated once and used in both endpoint decisions by `referee_pairs.c`.

This gives the exact joint rejection count on the retained vertices. The chance that the true root deficit differs is at most the expected number of omitted rejected edges, bounded by

$$
(n-1)a\,\mathbb P(\mathrm{Bin}(n-2,a)\ge k).
$$

For the nine primary interior cases the largest bound is $5.28\times10^{-12}$ per sample. When $a=0$, this sampler is exact without truncation.

For fixed complements I retain root coordinates $Y=n(1-U)\le80$, generate all their shared edges, and sample the independent external counts. The root discards the $r$ lowest coordinates. The expected number of omitted rejections is bounded by the binomial-tail integral above 80; bounding each binomial mass by $y^ie^{-(n-r-1)y/n}/i!$ gives a maximum error probability below $5.6\times10^{-29}$ per sample for the cases here.

Thus these simulations retain the dependence of actual $LK(n,k)$; they do not replace the finite graph by independent neighbor decisions or draw directly from the proposed limiting law. Full-graph simulations at $n=12$ and $n=1000$ provide additional checks on the sampling construction.

### Interior simulations and finite-size deviations

There are 20,000 independent samples per row. Parentheses give one estimated Monte Carlo standard error. “Finite” columns are the separate two-edge integration. The limit is mean 0.564189584 and variance 0.290687895. KS is the supremum CDF distance between the empirical $H/s_n$ law and the continuous law $g(Z)$, taking both sides of each empirical jump.

| $n$ | $k$ | Sample $\mathbb EH/s_n$ (SE) | Sample $\operatorname{Var}H/s_n^2$ (SE) | Finite mean ratio | Finite variance ratio | KS |
|---|---|---|---|---|---|---|
| 1000 | 250 | 0.559082 (0.003815) | 0.291056 (0.004009) | 0.563790 | 0.295891 | 0.11990 |
| 1000 | 500 | 0.567154 (0.003861) | 0.298171 (0.004190) | 0.563695 | 0.299598 | 0.10790 |
| 1000 | 31 | 0.559591 (0.003802) | 0.289096 (0.003739) | 0.561908 | 0.291130 | 0.21010 |
| 10000 | 2500 | 0.568117 (0.003856) | 0.297341 (0.004226) | 0.564150 | 0.292324 | 0.04935 |
| 10000 | 5000 | 0.561228 (0.003787) | 0.286781 (0.004258) | 0.564140 | 0.293509 | 0.04325 |
| 10000 | 100 | 0.562645 (0.003757) | 0.282262 (0.003819) | 0.563484 | 0.290570 | 0.14220 |
| 20000 | 5000 | 0.563117 (0.003826) | 0.292835 (0.004290) | 0.564170 | 0.291843 | 0.03745 |
| 20000 | 10000 | 0.573296 (0.003855) | 0.297197 (0.004282) | 0.564165 | 0.292683 | 0.03125 |
| 20000 | 141 | 0.566406 (0.003822) | 0.292176 (0.003893) | 0.563690 | 0.290566 | 0.12895 |

The actual moment deviations are much smaller than the law deviations. At $n=1000,k=n/2$, the normalized variance exceeds its limit by 0.008910, about 3.07%; by $n=20000$ the excess is 0.001995, about 0.69%. At $n=20000,k=n/4$, the excess is 0.001155, about 0.40%. For $k=141$, the mean-ratio error is about $-0.000500$, while the variance-ratio error is about $-0.000122$.

In every row, the observed KS maximum occurs at zero: the measured probabilities of $H=0$ are the KS numbers in the last column. The limit has no atom at zero. Therefore a moment match does not mean that the finite law is already close in CDF distance. In particular, at $n=20000,k=141$, about 12.9% of the samples still have zero deficit. The 95% DKW sampling-error bound for each empirical CDF is approximately 0.00960, substantially smaller than these distances. No rate of CDF convergence claimed in the paper is contradicted.

### Fixed-complement simulations

There are 100,000 samples per row. These compare unscaled $H$ with the mixed Poisson limit. The limiting mean/variance pairs are

$$
r=1:(0.5,0.5833333333),\quad
r=2:(0.75,1.0023148148),\quad
r=5:(1.23046875,2.1164842746).
$$

| $n$ | $r$ | Sample mean (SE) | Sample variance (SE) | Finite mean | Finite variance | KS to limit |
|---|---|---|---|---|---|---|
| 1000 | 1 | 0.499060 (0.002408) | 0.579845 (0.004148) | 0.499750 | 0.582833 | 0.00068 |
| 1000 | 2 | 0.750740 (0.003169) | 1.004119 (0.006938) | 0.749249 | 1.000381 | 0.00055 |
| 1000 | 5 | 1.231980 (0.004598) | 2.114266 (0.014205) | 1.227385 | 2.105521 | 0.00166 |
| 10000 | 1 | 0.498900 (0.002412) | 0.581905 (0.004192) | 0.499975 | 0.583283 | 0.00081 |
| 10000 | 2 | 0.746920 (0.003154) | 0.995060 (0.006860) | 0.749925 | 1.002122 | 0.00129 |
| 10000 | 5 | 1.230590 (0.004610) | 2.125120 (0.014396) | 1.230161 | 2.115389 | 0.00119 |
| 20000 | 1 | 0.502540 (0.002431) | 0.590919 (0.004211) | 0.499987 | 0.583308 | 0.00157 |
| 20000 | 2 | 0.753660 (0.003175) | 1.008147 (0.006933) | 0.749962 | 1.002218 | 0.00151 |
| 20000 | 5 | 1.231970 (0.004614) | 2.128821 (0.014388) | 1.230315 | 2.115937 | 0.00104 |

The CDFs of the limiting laws were computed by quadrature of the conditional Poisson CDF against the gamma density, not by another Monte Carlo sample. At $n=1000,r=5$, the deterministic finite-$n$ errors are about $-0.003084$ in mean and $-0.010964$ in variance. At $n=20000$, they are approximately $(-0.0000125,-0.0000250)$, $(-0.0000375,-0.0000965)$, and $(-0.0001538,-0.0005474)$ for $r=1,2,5$, respectively. These are mostly below the Monte Carlo resolution. All observed fixed-$r$ CDF discrepancies are below the single-row 95% DKW bound 0.00430.

Across the 18 primary simulation rows, the largest discrepancy from the finite-$n$ integrated mean is 2.37 estimated standard errors, and the largest variance discrepancy is 2.18. This provides no evidence of a failed limit or an incorrect finite-$n$ formula.

### Comparison with the paper's Section 8

The rational computations reproduce $\mathbb ED_{5,2}$, $\operatorname{Var}D_{5,2}$, and the exact $n=12$ values. At $n=12$, the independent exact pairs for $D$ are

```text
k=4: mean 3.133126934985, variance 0.914105265625
k=8: mean 7.203892083149, variance 0.987840041231
```

The independent full-graph samples of 100,000 graphs have deficit means/variances $(0.868870,0.921224)$ and $(0.795720,0.989440)$; their differences from the exact values are at most 1.66 estimated standard errors. There is no reason to expect the same unusually small deviations as the authors' particular samples.

For $r=1$, the exact values at $n=10,20,40,80$ reproduce all the printed six-decimal numbers. Independent numerical integration reproduces **every one of the twelve finite rows** in Table 1 at its printed precision, including the rows with $n=10^6$ and $10^8$. Those large sizes were integrated, not simulated. For example:

```text
n=1000,    k=500:    EH/s=0.563695498, VH/s^2=0.299598013
n=10000,   k=5000:   EH/s=0.564140213, VH/s^2=0.293508890
n=1000000, k=500000: EH/s=0.564189090, VH/s^2=0.290969995
n=10000,   k=100:    EH/s=0.563484434, VH/s^2=0.290569573
n=10^8,    k=10000:  EH/s=0.564182531, VH/s^2=0.290683886
```

The reported half-budget variance correction near $0.141/s_n$ is consistent with these calculations.

### Lean file: what is, and is not, proved

The eight theorem declarations in `code/RootDegree.lean` concern factorial/binomial identities and particular rational sums. There are no `sorry`, `admit`, new `axiom`, or `unsafe` declarations in the source inspected. The supplied build transcript reports exit 0 and only standard Lean axioms.

Specifically:

* `beta_constant` proves a rational identity involving factorials. Substituting $a=k-1,b=n-k-2$, **and separately using** the integer-argument beta formula $B(k,n-k-1)=(k-1)!(n-k-2)!/(n-2)!$, yields the constant used in Lemma 2.2. The analytic beta formula itself is not formalized here.
* `central_identity` and `mean_constants_agree` prove the all-$k\ge1$ binomial identity claimed in line 434.
* `mu_small` together with `mu_closed_small` verifies the mean-sum equality at $r=1,\ldots,6$, not for arbitrary $r$.
* `M2_small` and `values_small` verify the stated second moments, variances, and squared endpoints at $r=1,2$.

These are the algebraic checks described in Section 8, subject to the beta-formula bridge just stated. The file does **not** prove a random-graph representation, covariance lemma, asymptotic theorem, independence assertion, UI argument, or classification theorem. The paper does not claim that it does. No Lean executable is on the available PATH and the folder has no pinned Lean/Mathlib project, so I did not independently reproduce the supplied compilation. Source inspection and the supplied transcript are distinct from a fresh kernel check.

### Use of earlier results

As far as the supplied text shows, the citations are used consistently:

* La–Kabkab is credited for the model and earlier connectivity/diameter work. The source does not import an unprovided result from that paper into the degree-limit proofs.
* Dabirian–Subramanian's largest-score convention is exactly equivalent under simultaneous score reversal. Their stated mean asymptotics are used for comparison and the identification of $c_k$. The displayed $c_k$ has the claimed first-order Stirling behavior, and the corollary's explicit identity can also be proved directly.
* The Erlang weighted tree result is used for the fixed-budget interpretation and attribution. Replacing uniform by exponential costs preserves all edge rankings by a common strictly increasing transformation. Proposition 6.1 independently proves the particular fixed-$k$ root-degree law used in the classification.

The original cited papers are absent, so I cannot verify the bibliographic theorem numbers, the quotation of their exact hypotheses, or priority. No external citation is being treated as verified merely because it is printed in the source. The principal probabilistic conclusions audited here have proofs in the supplied paper.

### Reproduction and resource use

Compile the two C files with `cc -O3 -dynamiclib referee_pairs.c -o referee_pairs.so` and `cc -O3 referee_enumerate.c -o referee_enumerate`. Run `referee_exact.py` before `referee_numeric.py`, then run `referee_simulate.py --n N --reps 20000 --fixed-reps 100000` for $N=1000,10000,20000$. The other Python programs can then be run directly. Set `OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1` for Python runs. `referee_validate.py` and the simulations require the compiled shared library in the current folder.

The three primary simulation jobs took 10.55, 15.86, and 18.40 seconds; full-graph validation took 21.98 seconds. No calculation approached five minutes. No more than two computational jobs overlapped. Arrays were small: the full-graph check used $1000\times1000$ matrices, rather than matrices at $n=20000$; quadrature used at most $320\times320$ grids. No workload approached 1 GB. Attempts to request nice level 15 printed `setpriority: Operation not permitted` in this managed environment; the computations still completed, and thread counts were capped at one. No other agents, visible windows, pushes, or edits to the supplied manuscript/code were used.

## Corrections and precise scope notes

1. **Line 434, the sentence about `beta_constant`:** for formalization precision, replace “proves the identity $\binom{n-3}{k-1}B(k,n-k-1)=1/(n-2)$” with “proves its rational factorial form; the integer-argument beta formula identifies this with $\binom{n-3}{k-1}B(k,n-k-1)=1/(n-2)$.” The beta integral is not an object in that Lean theorem. This is a clarification of the formal check's scope, not a gap in Lemma 2.2.
2. **Requested result numbering, lines 373–390:** `cor:ck` is Corollary 7.3 in this source because the preceding remark is numbered 7.2. No internal cross-reference correction is needed; references in this report identify both the requested and source numbering.

No correction to a mathematical statement, covariance coefficient, error bound, limiting distribution, or moment-convergence proof is required by this audit. No result was classified GAP or ERROR.

Task: “You are refereeing a mathematical paper that has been posted.” First recorded clock check: 12 November 2026, 18:26:47, Asia/Tbilisi (+04).
