MINOR

The mathematical claims (A), (B), and the source correction (C) withstand this review. I found no incorrect limit, lost lattice factor, invalid replacement of first-hit weights, or missing uniform-integrability argument. The bridge proof establishes an exact leading equivalent for every fixed real endpoint parameter. The first-passage proof establishes order n log n, thereby proving the published Peres order conjecture, but does not determine a first-passage leading constant. Its PARTIAL label is appropriate for the two-part problem.

The requested minor revision concerns the literature record, not the proofs. The continuum integrals are old results of Shepp; the bridge weak convergence at endpoint zero is already in Pitman–Tang. The additional discrete mean convergence and the first-passage order proof were not found stated in the literature checked here. This is evidence about the checked sources, not a certificate of worldwide priority.

Errors and gaps requiring attention:

1. **Missing literature document.** Claim REPORT.md §2, line 113, and §7, line 550, refer to LITERATURE.md, which is absent from the supplied claim_files packet. Several claims about access limitations and prior work consequently cannot be audited from that citation. Fix: supply the bibliography/search record, or incorporate it into the report, distinguishing full texts inspected from metadata-only records. My independent literature audit is given below. No mathematical repair to (A) or (B) is needed.

No further error or proof gap was found in the assertions actually made. In particular, the absent sharp FP equivalent is explicitly acknowledged rather than silently assumed.

## Source, definitions, and exact scope

The relevant paper is Jim Pitman and Wenpin Tang, [Patterns in random walks and Brownian motion, arXiv:1411.0041v3](https://arxiv.org/abs/1411.0041v3), revised 10 September 2015. The [published chapter](https://www.columbia.edu/~wt2319/Patterns.pdf) is in *In Memoriam Marc Yor—Séminaire de Probabilités XLVII*, LNM 2137 (2015), pp. 49–88, DOI 10.1007/978-3-319-18585-9_4. Independently downloaded, page-delimited plain texts are sources/pitman_tang_arxiv.txt and sources/pitman_tang_published.txt. No PDF was saved to disk. The published text has some defective font mappings; the arXiv extraction supplies the unambiguous notation.

Let X_i be independent signs with probabilities 1/2 and S_j=Σ_{i=1}^j X_i, S_0=0. SW(n) comprises paths w(0)=0 with n increments in {−1,+1}. With α denoting the source's λ, set

    a_n = floor(α sqrt(n)) if that integer has parity n,
          floor(α sqrt(n))+1 otherwise.

The definitions on arXiv pp. 5–6 are exactly

    BR_{α,n} = {w in SW(n): w(n)=a_n},                       α real,
    FP_{α,n} = {w in SW(n): w(i)>w(n)=a_n, 0≤i<n},          α<0.

Thus α is a fixed endpoint in diffusive units, not a fixed unscaled endpoint and not a linear drift αn. The FP endpoint is a strict minimum relative to *every* preceding position, including position zero. For small n a rounded FP endpoint can be zero or unattainable; asymptotic assertions concern sufficiently large n, when a_n<0 and |a_n|≤n.

For either family A, define

    F_n = inf{s≥0: (S_{s+j}−S_s, 0≤j≤n) belongs to A},
    T(A) = n+F_n.

This is the completion time of the first occurrence of ANY member of the family, allowing overlapping windows. It is neither a cover time nor the average waiting time for a uniformly selected word. The source explicitly confirms T(BR_{0,n})=F_n+n on arXiv p. 14 / published p. 67. The claim uses exactly these conventions. Odd n at α=0 has endpoint +1, not an empty bridge family; the same limit still follows.

For distinct length-n words A_1,...,A_k, the source's matching matrix is

    ε_l(A_i,A_j) = 1{prefix_{n−l}(A_i)=suffix_{n−l}(A_j)},
    M_ij = Σ_{l=0}^{n−1} 2^(−l) ε_l(A_i,A_j).

Rows are possible future target words; columns are the word just completed. The matrix need not be symmetric.

The following gives the mathematical content of Theorem 2.1, arXiv p. 7, retaining its printed notation. M is invertible; its displayed equations are

    (1/E T(A_1),...,1/E T(A_k))^T = 2^(−n) M^(−1) 1,      (2.3)
    1/E T(A) = Σ_i 1/E T(A_i)
             = 2^(−n) 1^T M^(−1) 1.                     (2.4)

There is a genuine notation/interpretation problem here: the components in (2.3) cannot be reciprocals of the ordinary standalone word means. For {+−,−+}, both standalone means are 4, while the family mean is 3 and 2^(−n)M^(−1)1=(1/6,1/6). The correct components are π_i/E T(A), where π_i is the probability that A_i is the first family word. The final family formula in (2.4) is correct. The claim identifies and avoids this problem. Published numbering is Theorem 6, p. 57, equations (8)–(9).

Theorem 1.8, arXiv p. 6, asserts, with finite strictly positive constants:

    (1) E T(E^{2n}) ~ C_E n^(3/2),
    (2) E T(M^{2n+1}) ~ C_M n,
    (3) c_BR^λ n ≤ E T(BR^{λ,n}) ≤ C_BR^λ n,
    (4) c_FP^λ n ≤ E T(FP^{λ,n}) ≤ C_FP^λ n^(5/4), λ<0.

Here E^{2n} consists of positive excursions with first return to zero at 2n; M^{2n+1} consists of walks strictly positive at steps 1,...,2n+1. These are the theorem's other two families, not additional restrictions on BR or FP. The published counterpart is Theorem 5, pp. 55–56. In particular, (4) has exponent 5/4 in its upper bound, exactly as the claim says.

Open problem 2.3, arXiv p. 13, asks for exact asymptotics of E T(BR^{λ,n}) for λ∈R and of E T(FP^{λ,n}) for λ<0, using the matching-matrix method of Theorem 2.1. Its published counterpart is Open Problem 1, p. 65. The published page additionally states Peres's Conjecture 1, equation (30): two positive λ-dependent constants bound the FP mean above and below by n ln n. The arXiv and published discussions differ; the Peres conjecture must be attributed to the published text.

## Audit of (A)

**Matching system: claim (3)–(7), §§1–2.** Put C=2^n M. Starting a fair unit-stake gambling team for each target word gives

    Cπ=e1,      1^Tπ=1,      e=E T(A).

The overlap of length n−l contributes 2^(n−l), so both orientation and normalization agree with the source. Consequently

    e = 1/(1^T C^(−1)1) = 2^n/(1^T M^(−1)1).

At a bounded stopping time the fair-capital identity is elementary. For the unbounded first occurrence, total surviving capital for a target is bounded by Σ_{r=1}^n 2^r, while e is finite by independent length-n trials. This justifies the passage to the limit. Summing over target rows gives, with k=|A|,

    (k/2^n)e = E_π C_n(W),      C_n(w_j)=Σ_i M_ij.

This is a first-hit-weighted column average. The use of π, rather than a uniform word, is essential and is maintained throughout the claim.

Let p_l(b)=2^(−l) binom(l,(l+b)/2), with unattainable values zero and p_0(0)=1. Directly completing the suffix of a current word w yields

    C_n^BR(w) = Σ_{l=0}^{n−1} p_l(w(l)),
    C_n^FP(w) = 1+Σ_{l=1}^{n−1} 1{w(l)<0} f_l(−w(l)),
    f_l(b) = (b/l)p_l(b), b>0.

For BR, the l fresh signs must sum to w(l). For FP, the old endpoint is already a forbidden earlier minimum unless w(l)<0; in that case the appended signs must first reach w(l) at their final step. These arguments prove the column identities exactly. My independent matrices check them for every word in all 52 computed families.

**First-hit path convergence: claim §3.1, (11).** The n-window sum at consecutive starting indices changes by 0 or ±2. It has the same parity as a_n. A change from below the target to above therefore cannot skip the target. The hitting time of the linearly interpolated moving sum is exactly F_n/n. Donsker convergence on compact intervals gives the limiting process

    Z(t)=B(t+1)−B(t),      F_α=inf{t≥0: Z(t)=α}.

On a unit interval, conditional on Z at its two endpoints x,y, Z is a variance-2 Brownian bridge from x to y. Both endpoint densities are strictly positive, so its unconditional law is mutually absolutely continuous with a variance-2 Brownian motion with a nondegenerate normal starting value. Brownian immediate crossing after a level hit transfers to Z. Taking countably many unit intervals suffices; integer-time hits have probability zero. Also Z(0),Z(1),... are independent standard normals, giving F_α<∞ almost surely. These facts justify the hitting-time continuity argument and the joint convergence of the first-hit word path. No strong Markov assertion about the non-Markov process Z is needed or made.

**Convergence of means: claim (12).** Set q_n=P(S_n<a_n), r_n=P(S_n>a_n). If F_n>kn, the independent windows at starts 0,n,...,kn are all strictly on the same side of a_n. Hence

    P(F_n>kn) ≤ q_n^(k+1)+r_n^(k+1).

For each fixed α, q_n→Φ(α), r_n→1−Φ(α), both below one. Thus F_n/n has a uniform geometric tail for all sufficiently large n. This proves uniform integrability, not merely tightness or bounded first moments. Therefore

    E T(BR_{α,n})/n → 1+E F_α.

The constants in this tail argument are not uniform as |α|→∞; the claim correctly fixes α.

**Local limit and overlap scaling: claim §3.2, (13)–(15).** The correct span-2 limit is

    sqrt(n)p_n(a_n) → 2φ(α),
    sqrt(n)p_l(b) = 2φ_{l/n}(b/sqrt(n))+o(1), δn≤l≤n,

uniformly over attainable b. The binomial central bound p_l(b)≤C/sqrt(l) is enough for the boundary layer. Stirling's formula on |b|≤K sqrt(l), followed by the binomial Gaussian bound outside that range, gives the asserted uniform local limit. There is no missing parity factor.

For w_n/sqrt(n)→w uniformly on the n-mesh,

    C_n^BR(w_n)/sqrt(n) → K(w)=2∫_0^1 φ_t(w(t))dt.

The short-shift contribution is bounded, independently of the word and therefore independently of π, by

    1/sqrt(n)+(C/sqrt(n))Σ_{1≤l<δn}l^(−1/2)
       ≤ 1/sqrt(n)+2C sqrt(δ).

The limiting integral has the same O(sqrt(δ)) bound. On [δ,1] the integrand is continuous and bounded. In particular, shifts near n are harmless: l/n is bounded away from zero, and the probability in this column formula involves l fresh signs, not n−l fresh signs. The full normalized column sum is bounded deterministically. Thus the expectation passage under the first-hit law is justified, without any unproved assertion about the density of that law.

The weighted identity then gives

    lim E T(BR_{α,n})/n
       = E K(W*)/(2φ(α))
       = E[∫_0^1 φ_t(W*(t))dt]/φ(α),

where W*(u)=B(F_α+u)−B(F_α). This agrees with 1+E F_α. An ordinary Brownian bridge is a different law: at α=0 its substitution gives π/2 instead. That substitution is not used. As an additional bound, 1<c_BR(α)≤2 exp(α²/2), and c_BR(α)=c_BR(−α).

**Explicit series: claim (9)–(10), §3.3.** I re-derived its normalization from Brownian pieces rather than trusting its citation. For t=m+θ, 0<θ<1, put x_i=B(i)+ih, y_i=B(i+θ)+ih, x_0=0. The event B(s)−B(s+1)<h for 0≤s≤t requires the m+2 paths on [0,θ] and the m+1 paths on [θ,1] to preserve their order. Their respective noncollision densities are

    det[φ_θ(y_j−x_i)]_{i,j=0}^{m+1},
    det[φ_{1−θ}(x_{j+1}−h−y_i)]_{i,j=0}^{m}.

Integrating their product over

    0<x_1<...<x_{m+1},     y_0<...<y_{m+1}

gives exactly the claimed H_h(m+θ). There are 2m+3 integration variables before θ is integrated. The determinants already include the unconditional Gaussian endpoint densities; no additional φ(x_1−h), factorial, or conditioning factor is missing. Ordered Brownian transition densities are nonnegative. The second duration is 1−θ, and the sign of h is correct.

By continuity, a path avoiding α stays on one side of it. Symmetry gives

    P(F_α>t)=H_α(t)+H_{−α}(t),
    c_BR(α)=1+Σ_{m≥0}∫_0^1[H_α(m+θ)+H_{−α}(m+θ)]dθ.

This is equation (10). Its convergence is rigorous: H_h(t)≤Φ(h)^(floor(t)+1). This yields a summable geometric bound for every fixed finite h. Strict positivity of E F_α follows because Z starts off the level almost surely and has continuous paths. Finiteness follows from that geometric bound.

I also checked the sharper truncation bound. With

    r_h=H_h(1)=Φ(h)^2−hφ(h)Φ(h)−φ(h)^2,

independence on [0,1],[2,3],... gives H_h(t)≤r_h^floor((t+1)/2). Summing this bound over omitted integer slabs gives exactly claim (17). The numerical estimate and this one-sided omitted-tail bound must remain separate from quadrature uncertainty, as they are in the claim.

## Audit of (B), including constants

Write a=−a_n>0, m=floor(n/2), and κ_α=2|α|φ(α)>0. The ballot formula and the span-2 local limit give

    P(A_s)=f_n(a) ~ κ_α/n,

for an FP occurrence A_s at start s. This verifies claim (18), including its α dependence.

There is a simpler independent proof of the claimed upper bound. Binomial unimodality gives (b+1)p_l(b)≤1: the b+1 attainable lattice values from −b through b each have mass at least p_l(b). Consequently f_l(b)≤1/l, for all attainable b>0. From the weighted matching identity,

    E T(FP) ≤ (1+H_{n−1})/f_n(a),
    limsup E T(FP)/(n log n) ≤ 1/κ_α.

For example C_α=4/κ_α works for all sufficiently large n: choose n≥8 and large enough that f_n(a)≥κ_α/(2n). Thus the upper bound has no unexplained dependence on α. The claim's block argument is also valid: E N≥κ_α/4 eventually, and the expected number of successes after the first in the block is at most 1+H_m. Hence its block success probability q is at least a positive α-dependent multiple of 1/log n; independent pieces of length n+m give the stated upper bound.

The lower bound is the substantial step. For independent walks X,Y starting at zero, let a record mean a *strict* descending record of Y, including time zero. The return potential in claim (19) has the exact identity

    g_j = (1/j)Σ_{b>0} b p_j(b)^2
        = 4^(−j) binom(j−1,floor(j/2))^2,
    G_m=1+Σ_{j=1}^m g_j ~ (log m)/(2π).

To verify it, write b=2k−j and use

    (2k−j)binom(j,k)^2
      =j[binom(j−1,k−1)^2−binom(j−1,k)^2].

The sum telescopes. This independently checks the parity and the coefficient 1/(2π) without invoking a Riemann approximation. For explicit bounds, g_j≥1/(8j) for every j≥1. Indeed g_{2r}=g_{2r+1}=(1/4)[binom(2r,r)/4^r]^2, and binom(2r,r)/4^r≥1/(2sqrt(r)) follows by induction. Thus G_m≥log(m+1)/8.

Let R_m be the number of distinct values X_j−Y_j sampled at those records up to m; V_L is the number of records up to L. The first record at which a value z is attained is a joint stopping time. From that time the increments are fresh, and being a record resets the record condition relative to the current minimum. The expected number of subsequent visits to that same z at records during the next m steps, including the current visit, is G_m. Every counted visit is a record by time 2m, and visits associated with different z cannot be the same visit. Therefore

    G_m E R_m ≤ E V_{2m} ≤ 4sqrt(m),
    E R_m ≤ 32sqrt(m)/log(m+1).

This step does not assume independence of visits, independence of the record clock and X−Y, or a uniform first-hit FP word.

For the original walk, split it into X_s=S_s, s≤m; D=S_n−S_m; and Y_s=S_{n+s}−S_n, s≤m. These three objects are independent. An occurrence at start s≤m necessarily has s a descending record of Y and

    D=X_s−Y_s−X_m−a.

Conditional on X,Y, this supplies at most R_m possible values of D. The point masses of D are at most 1/sqrt(n−m). Thus

    q=P(∪_{s=0}^m A_s)
      ≤ 32/log(m+1) ≤ 64/log n,        n≥4.

This is the mechanism forcing the logarithm: a block has order-one expected count of occurrences but only O(1/log n) chance of containing any, because occurrences form clusters at records with logarithmically many returns.

For fully explicit conservative lower constants, take K=floor(log n/256). For log n≥512, K≥log n/512 and a union bound over K+1 blocks of starts gives P(F_n≤Km)≤3/8. Since m≥n/3,

    E T(FP)≥E F_n≥Km/2≥n log n/3072.

This bound is deliberately loose; its enormous sufficient threshold is irrelevant to the asserted order. After also requiring a_n<0 and the above ballot local-limit bound, one admissible pair is

    c_α=1/3072,     C_α=4/κ_α,

for all sufficiently large n depending on α. The lower constant can be universal; the upper constant and the onset depend on the fixed endpoint parameter. The claim's less explicit constants are therefore justified.

Because log n/n^(1/4)→0, this result is compatible with the source's n^(5/4) upper bound. It forces E T(FP)/n→∞. It gives neither convergence of E T(FP)/(n log n) nor its value. The uniform-word average in claim (28) cannot supply that missing constant: the matrix identity uses the actual first-hit law. The claim correctly stops short of making that substitution.

I also checked §5's auxiliary uniform-word calculation. For a uniform FP word U_n and 1≤b<a, reflection and the ballot formula give

    P(U_n(l)=−b)
      =[p_l(b)−p_l(2a−b)] f_{n−l}(a−b)/f_n(a).

On l≤δn, b≤K sqrt(l), the likelihood multiplier tends to one as δ decreases, after n grows; a is of order sqrt(n), so the reflected contribution is exponentially small there. The Gaussian binomial bound controls b>K sqrt(l), and f_l≤1/l bounds the whole range l≥δn by O(log(1/δ)). This proves the stated uniform-column equivalent (log n)/(2π). It also confirms why that equivalent alone cannot evaluate the inverse-matrix sum. The formal FP continuum integrand has expected size 1/(2πt) near zero; the bridge O(sqrt(δ)) domination has no FP counterpart.

## Independent computations

The implementations in code/independent_exact.py and code/independent_integrals.py were written for this review; no claim code was imported, copied, or executed. The exact solver enumerates signs, constructs the integer overlap matrix C, and performs fraction-free Bareiss elimination for rational results. It separately constructs an Aho–Corasick prefix chain and solves its mean absorption equations with transitions to completed patterns killed. The initial state is the empty prefix, so its answer directly includes the n initial signs.

There are 52 cases, including odd n, α=0,0.5,1 for BR and α=−1,−2 for FP. Thirty-five are rational calculations (n≤8); 45 also have prefix-chain checks (n≤12). Larger matching systems reach n=14 for BR and n=17 for FP. All binomial/ballot family counts, all overlap column identities, and nonnegativity of the solution weights passed. The maximum matching-system residual is 5.38e−14; the largest prefix/matrix mean difference is 2.42e−13. These are numerical residuals, not rational certificates for the larger cases.

Selected results (completion times):

| Family | n | endpoint | E T | E T/n | E T/(n log n) |
|---|---:|---:|---:|---:|---:|
| BR, α=0 | 2 | 0 | 3, exact | 1.500000 | — |
| BR, α=0 | 4 | 0 | 85/14, exact | 1.517857 | — |
| BR, α=0 | 6 | 0 | 836953/91448, exact | 1.525371 | — |
| BR, α=0 | 8 | 0 | 4610050917991422781/376756741306885616, exact | 1.529518 | — |
| BR, α=0 | 12 | 0 | 18.407555805 | 1.533963 | — |
| BR, α=0 | 14 | 0 | 21.494087783 | 1.535292 | — |
| BR, α=0.5 | 14 | 2 | 24.398665559 | 1.742762 | — |
| BR, α=1 | 14 | 4 | 35.126980737 | 2.509070 | — |
| FP, α=−1 | 4 | −2 | 34/3, exact | 2.833333 | 2.043818 |
| FP, α=−1 | 6 | −2 | 296/17, exact | 2.901961 | 1.619615 |
| FP, α=−1 | 8 | −2 | 68202/2819, exact | 3.024211 | 1.454338 |
| FP, α=−1 | 12 | −4 | 43.516365096 | 3.626364 | 1.459356 |
| FP, α=−1 | 16 | −4 | 55.738238447 | 3.483640 | 1.256458 |
| FP, α=−1 | 17 | −5 | 66.586359109 | 3.916845 | 1.382474 |

The BR zero-endpoint values approach the integral constant from below. For nonzero α, endpoint rounding changes a_n/sqrt(n) substantially at these small sizes; monotone convergence should not be expected. The FP ratios at these sizes do not establish an eventual constant on either scale. The proof, rather than these small systems, establishes the order and divergence.

For (10), I used a different importance distribution: condition each full unit Brownian increment to exceed −h, restoring its probability Φ(h)^(m+1), then sample the intermediate Brownian bridge endpoints. Two determinant ratios give the conditional noncollision probabilities. A Monge row/column scaling keeps all determinant entries at most one; its factors cancel exactly. This evaluates the continuous-time integrals, rather than simulating hits on a time grid. Each slab uses eight independent scrambled Sobol runs with 32768 points each, separately for the two signs.

| α | slabs | estimate of c_BR(α) | scramble standard error | bound on omitted positive tail |
|---:|---:|---:|---:|---:|
| 0 | 12 | 1.54387082 | 0.00004226 | 0.000001349 |
| 0.5 | 18 | 1.73240451 | 0.00006874 | 0.000003182 |
| 1 | 28 | 2.41376668 | 0.00013358 | 0.000031870 |

The first and third estimates agree with the claim within its reported numerical uncertainty. Symmetry supplies the same constants at −0.5 and −1. These are estimates, not certified decimal enclosures. The omitted-tail column does not cover quadrature error.

As an independent check, for 0<t≤1, write v=(Z(0)+Z(t))/2 and d=(Z(t)−Z(0))/2. They are independent normals of variances (2−t)/2 and t/2. The variance-2 bridge reflection formula gives

    H_h(t)=∫_{−∞}^h exp(−v²/(2−t))/sqrt(π(2−t))
             ×[erf((h−v)/sqrt(t))
               −2(h−v)/sqrt(πt) exp(−(h−v)²/t)] dv.

Ordinary one-dimensional adaptive quadrature in v and then t gives first-slab totals 0.4316901138162094, 0.4909824759512382, 0.6351140304003369 at α=0,0.5,1. They agree with the randomized determinant integrals. At zero the value also equals 3/4−1/π exactly. The independent potential calculation gives 65536 g_65536=0.1591537288406774, tending to 1/(2π)=0.1591549430918953.

Final validation in data/independent_validation.json also compares all 27 common finite-family rows to the supplied data: all 21 common rational answers are identical, and the maximum floating mean difference is 4.27e−14. Stable determinant scaling was separately checked against raw Gaussian determinant ratios, with maximum discrepancy 6.67e−16.

Complete results: data/independent_exact.csv, data/independent_constants.csv, data/independent_slabs.csv, and data/independent_potential.csv. Commands, from this directory:

    python3 code/independent_exact.py
    python3 code/independent_integrals.py

The processes inherit nice=10 and set numerical thread counts to one. Peak recorded RSS was 0.874 GB for the matrix run and 0.750 GB for the quadrature run, together well below 4 GB. No subagents, publication, pushes, PDFs, paper images, or scans were created by this review.

## Literature findings and value

The distinction between a known continuum formula, a discrete asymptotic theorem, and an unproved novelty claim matters here.

- **Pitman–Tang (2015), arXiv and published chapter:** the open problems remain printed. ArXiv Proposition 2.4 / published Proposition 1 already proves the zero-endpoint first-hit path convergence. The paragraph after it explicitly records only a liminf for the means, not convergence of the means. The geometric-tail argument in the claim closes that particular gap and extends to every real endpoint. Published p. 65 states Peres's FP order conjecture, rather than its proof.
- **Shepp (1971), First passage time for a particular Gaussian process, Ann. Math. Statist. 42, 946–951:** inspected the [original text](https://faculty.wharton.upenn.edu/wp-content/uploads/2012/04/First-passage-time_.pdf), especially equations (2.15)–(2.16), p. 949, and (2.25)–(2.26), p. 950. Equation (10) is the integrated, unconditional, two-sided use of these known determinant formulas. Its continuum probability formula is not new.
- **Pitman–Tang, The Slepian zero set ... (2015), arXiv:1411.0040:** inspected the full text. Equations (3.2)–(3.4) already describe the zero-level continuum first-hit distribution through Shepp integrals. Its displayed noninteger formula (3.3) has typographical problems, including the second time parameter; the original Shepp formula and the independent path-ordering derivation support the claim's 1−θ kernel. This paper does not supply the discrete mean equivalent or the FP n log n proof.
- **Guibas–Odlyzko (1981):** the [publisher record](https://doi.org/10.1016/0097-3165(81)90005-4) and Odlyzko's bibliography identify the classical correlation/generating-function theory. The full original text was not obtained here. These general finite-family identities are background, not a verified prior solution of the growing bridge/FP families.
- **Li (1980), Ann. Probab. 8, 1171–1176, DOI 10.1214/aop/1176994578; Gerber–Li (1981), SPA 11, 101–108, DOI 10.1016/0304-4149(81)90025-9:** original full texts were not accessible in this run. I checked the family mean and first-hit systems against the full author-hosted [Pozdnyakov–Glaz–Kulldorff–Steele scan-statistics paper](https://vladimir-pozdnyakov.github.io/papers/scan.pdf), §2.1, Theorems 2.1–2.2. Its overlap matrix is transposed relative to the claim's convention, but the scalar inverse formula is identical. The gambler argument and independent finite systems also verify the formula without relying on an inaccessible theorem.
- **Chen–Zame (1979), On fair coin-tossing games:** the [University of Miami record](https://scholarship.miami.edu/esploro/outputs/journalArticle/On-fair-coin-tossing-games/991031577078202976) and publisher metadata concern fair-coin pattern races. I did not obtain the full paper and do not claim an exhaustive exclusion of its contents. No verified BR/FP asymptotic theorem was found there.
- **Nielsen (1973), On the expected duration of a search for a fixed pattern in random data, IEEE IT 19, 702–704:** inspected the [full text](https://backend.orbit.dtu.dk/ws/files/4640102/PNielsen.pdf). Its theorem concerns a fixed word and its bifixes; it does not state these family asymptotics.
- **Banjević (1996), Recursive relations for the distribution of waiting times in a Markov chain, JAP 33, 48–56:** checked the [publisher abstract](https://doi.org/10.2307/3215263) and metadata. The work gives Markov sequence recurrences; full text was unavailable. It is not a verified prior resolution of (A) or (B).
- **Ostaszewska–Zajkowski, On the waiting time till some patterns occur in i.i.d. sequences, arXiv:1302.4859:** inspected the full text, especially Theorem 2.3 and Corollaries 2.4–2.5. It supplies general finite-pattern probabilities and means, not the BR/FP growing-family asymptotics.
- **Later citing works:** an independent OpenAlex DOI query returned four records: the 2015 Slepian paper; Evans–Pitman–Tang, *The spans in Brownian motion* (2017); Tang's 2017 thesis; and Pitman–Tang, *The argmin process of random walks, Brownian motion and Lévy processes* (2018). The spans and argmin full texts were inspected and contain no resolution of these discrete mean questions. The thesis download was blocked; its indexed primary-source passage still states the n log n result as Conjecture 2.5.2. OpenAlex's four records are not an exhaustive census of citations through 2026. The lookup responses are preserved in data/.
- **Additional 2019–2021 Slepian/moving-sum literature:** Noonan and Zhigljavsky's [linear-barrier paper, arXiv:1904.07227](https://arxiv.org/abs/1904.07227), and [moving-sum boundary-crossing paper](https://doi.org/10.1007/s11009-019-09769-7) develop continuum formulas and approximations for boundary crossings and mean run lengths. Their full texts were checked. Their first passage is crossing a threshold of the moving sum, not requiring a window path to first reach a prescribed endpoint at its final step. They do not state the two-sided Bernoulli exact-level equivalent (A) or the path-family order result (B).

Searches also used the paper title with dates through 2026, Peres/first-passage/logarithm, bridge-pattern waiting times, and family-of-patterns/Brownian-bridge combinations; no additional printed resolution was located. The literature conclusion is necessarily bounded by the access and indexing limitations just stated.

**Value and scope:** (A) is a correct exact equivalent with a computable, convergent integral expression for its leading constant. Its new content relative to the inspected literature is the discrete mean limit, the extension to arbitrary fixed α, and the justified first-hit-weighted matching limit; it is not a new Shepp formula. Part (1) of Open problem 2.3 can be called solved in this sense. The authors' additional wish for a wholly discrete matching-matrix analysis is not fulfilled; the claim is candid that its weights are identified through a scaling limit. (B) correctly proves the published Peres order conjecture, credited here to the reconstructed internal E0081 argument. It does not solve the exact-equivalent request in part (2). No sharp FP leading constant, or proof that such a constant exists, has been established in this packet.

Task: “You are an independent referee … Break it if it is wrong.” Received 13 November 2026, approximately 11:10 Asia/Tbilisi; the request supplied no seconds.
