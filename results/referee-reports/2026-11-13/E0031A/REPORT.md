PARTIAL

# E0031: variance of one-colour Euclidean minimum matching

The uniform-cube problem in dimensions d >= 2 is not solved here. No checked source supplies the requested all-n lower bound. The proved partial results below are an all-n bound of order n^(1-3/d), a target-order lower bound on an infinite subsequence in every d >= 2, an exact solution in d=1, and a weaker all-n anti-concentration scale n^(-1/d). None reaches Chatterjee's requested anti-concentration scale in d >= 2. Numerical work is separate evidence.

## Source and precise question

Sourav Chatterjee, “A general method for lower bounds on fluctuations of random variables,” *Annals of Probability* **47** (2019), no. 4, 2140–2171, DOI [10.1214/18-AOP1304](https://doi.org/10.1214/18-AOP1304). The author's [publication list](https://souravchatterjee.su.domains/publications.html) confirms these bibliographic details. The version actually read is [arXiv:1706.04290v3](https://arxiv.org/abs/1706.04290v3), revised 26 July 2018; v1 was submitted 14 June 2017. It has 32 PDF pages. The full page-labelled text is in sources/chatterjee_1706.04290v3.txt. PDF page numbering here is one-based. The journal PDF endpoint returned HTML, so journal page locations must not be inferred merely by adding 2139 to the preprint page number.

Section 3, item (3), PDF/printed preprint p.27, says exactly:

> Prove a tight lower bound for the fluctuations of the length of the minimal matching when the points are uniformly distributed in [0,1]^d.

For even n, let X_1,...,X_n be independent uniform points in Q=[0,1]^d and set

\[
 M_n=\min_{\mathcal P}\sum_{\{i,j\}\in\mathcal P}|X_i-X_j|,
\]

where P ranges over all partitions of {1,...,n} into pairs. This is a **non-bipartite (one-colour), perfect matching**, with distance power **p=1**, total cost, Euclidean norm, and ordinary cube boundaries. There is one sample, not two colour classes. Section 2.1, p.10, explicitly mentions even n and homogeneity r=1. The intended nontrivial dimensional setting is fixed d >= 2, as in Corollary 2.2 (p.11) and Theorem 2.3 (p.12); item (3) itself places no explicit restriction on d. The elementary case d=1 is treated separately below.

The target scale is n^(1/2-1/d) for fluctuations, corresponding to

\[
 c_d n^{1-2/d}\leq\operatorname{Var}M_n\leq C_d n^{1-2/d}.
\]

Thus the proposed variance order is 1 in d=2, n^(1/3) in d=3, and n^(1/2) in d=4. These statements concern total cost; dividing M_n by n divides its variance by n^2.

There are two necessary qualifications. First, Definition 1.1, p.3 (with the preceding discussion on p.2), requires that **every** interval of sufficiently small multiple of n^(1/2-1/d) have probability bounded away from one. A variance lower bound alone is weaker. Second, Chatterjee's statement after Corollary 2.2, p.12, reports matching known upper bounds, citing Steele. The upper-bound bibliography needs care: Talagrand's actual 1995 bounds have logarithmic losses, and a November 2026 preprint identifies a possible exponent typo in Steele. See the literature audit below; the intended sharp exponent is unambiguous, but the historical assertion about an already established exact upper bound should not be repeated without qualification.

## Proofs obtained here

Write mu_n=E M_n, mu_0=0, and V_n=Var M_n. All n below are even. Points at identical locations retain distinct labels.

### Lemma 1: two deterministic metric identities

For any even finite list S and any x,

\[
 M(S,x,x)=M(S).
\]

Pairing the duplicates together proves <=. Conversely, if the duplicates are paired to distinct a,b in S, replace those two edges by the duplicate pair and the edge {a,b}. The triangle inequality |a-b| <= |a-x|+|x-b| does not increase the cost. Removing the duplicate pair gives a matching of S. This proves >= as well.

Changing a single labelled point x to y changes the optimum by at most |x-y|: reuse its old partner and apply the triangle inequality, then reverse x and y. In particular M_n and all the conditional means used below are continuous and 1-Lipschitz separately in each point. Also |M(S,x,y)-M(S)| <= |x-y|, by adding {x,y} for the upper inequality and reconnecting their partners for the lower inequality.

### Theorem A: an explicit variance inequality

For every d >= 1 and even n >= 2,

\[
 \boxed{\quad V_n\ \geq\ {\binom n2\over4(4\sqrt d)^d}
          |\mu_n-\mu_{n-2}|^{d+2}.\quad} \tag{A}
\]

Proof. Define continuous conditional means

\[
 g(x)=E M_n(x,X_2,...,X_n),\qquad
 f(x,y)=E M_n(x,y,X_3,...,X_n),
\]

and the second-order centred kernel

\[
 h(x,y)=f(x,y)-g(x)-g(y)+\mu_n.
\]

Integrals without an indicated measure are Lebesgue integrals on Q, which has volume one. Then int h(x,y)dy=0 for every x. By Lemma 1,

\[
 \int_Q h(x,x)\,dx=\mu_{n-2}-\mu_n=-\Delta_n.
\]

The Lipschitz constant of h in either argument is at most 2. Put J=int_(QxQ) h^2. Distinct terms in U=sum_(i<j) h(X_i,X_j) are orthogonal, including terms sharing a single index, because the kernel has conditional mean zero. Consequently Var U=binom(n,2)J. Conditioning M_n on X_i,X_j shows Cov(M_n,h(X_i,X_j))=J. Hence Cov(M_n,U)=binom(n,2)J, and Cauchy–Schwarz gives V_n >= binom(n,2)J. If J=0 this remains valid without division.

Let delta=|Delta_n|. The case delta=0 is trivial. The last identity in Lemma 1 implies delta <= sqrt(d). Set r=delta/(4 sqrt(d)), so 0<r<=1/4. Draw x uniformly in Q and y uniformly in Q intersect (x+[-r,r]^d). This joint probability measure T has density at most r^(-d) relative to dx dy, since the intersection volume is at least r^d. Its first marginal is uniform, even near the boundary. Therefore

\[
 \left|E_T h(x,y)-\int_Q h(x,x)dx\right|\leq2\sqrt d\,r=\delta/2.
\]

Thus |E_T h|>=delta/2. Jensen and the density bound imply delta^2/4 <= E_T h^2 <= r^(-d)J. Inserting r proves (A). No stabilization, Poissonization, or asymptotic expansion of mu_n was used. □

### Theorem B: target-order variance along an infinite subsequence, d >= 2

For each fixed d >= 2 there are c_d>0 and R_d<infinity such that every sufficiently large even N has an even n in [N/R_d,N] with

\[
 V_n\geq c_d n^{1-2/d}. \tag{B}
\]

In particular limsup_(n even -> infinity) V_n/n^(1-2/d)>0. This is a subsequence statement, not the missing uniform lower bound.

Proof of the only mean estimate needed. Put a=1-1/d>0. Let v_d be the unit-ball volume and t=(2 v_d n)^(-1/d). For each point, a union bound gives probability at least 1/2 that its nearest other sample point is farther than t. Every matching length is at least half the sum of these nearest-neighbour distances. Thus

\[
 \mu_n\geq A_d n^a,\qquad A_d={1\over4}(2v_d)^{-1/d}>0. \tag{1}
\]

For a deterministic upper bound, set k=ceil(log_2(n)/d). First pair points within each of the 2^(kd) dyadic cells of side 2^(-k), leaving at most one per cell. Pass remaining points up the dyadic tree, pairing leftovers at each parent. At the root no point remains because n is even. The first-stage cost is at most (sqrt(d)/2)n 2^(-k). At level j, 0<=j<k, each parent receives at most 2^d leftovers; pairing costs at most sqrt(d)2^(-j)2^(d-1) per parent, and there are 2^(jd) parents. Therefore

\[
 M_n\leq {\sqrt d\over2}n2^{-k}
       +\sqrt d\,2^{d-1}\sum_{j=0}^{k-1}2^{j(d-1)}
 \leq B_d n^a, \tag{2}
\]

where, for example, B_d=sqrt(d)/2+sqrt(d)2^(2d-2)/(2^(d-1)-1) suffices. This also proves integrability without appealing to a law of large numbers.

Choose an integer q >= 2 with B_d q^(-a)<=A_d/2. For sufficiently large even N let m be the largest even integer <=N/q. Then

\[
 \sum_{n=m+2,m+4,...,N}\Delta_n
       =\mu_N-\mu_m\geq(A_d/2)N^a.
\]

There are at most N/2 summands, so some even n in this range has Delta_n>=A_d N^(-1/d). For N>=4q we have n>=N/(2q), so Delta_n>=A_d(2q)^(-1/d)n^(-1/d). Substitution into (A), and binom(n,2)>=n^2/4, proves (B), with R_d=2q and a positive explicit constant. □

Corollary using a checked first-order theorem: Yukich's Theorem 8.1 (printed p.249, PDF p.11) applies to MM and gives mu_n~beta_d n^a, beta_d>0; the deterministic bound (2) permits passage from the first-order length limit to its expectation. For large N divisible by four,

\[
 \mu_N-\mu_{N/2}\geq {\beta_d\over2}(1-2^{-a})N^a.
\]

There are N/4 even increments in this telescope. Some n in (N/2,N] therefore has Delta_n>=2 beta_d(1-2^(-a))N^(-1/d), which is at least 2 beta_d(1-2^(-a))2^(-1/d)n^(-1/d). Inserting this into (A) proves a target-order lower bound **somewhere in every sufficiently large dyadic block**. The completely self-contained result (B) did not need this first-order limit.

### Theorem C: an all-n, weaker variance lower bound, d >= 2

For every fixed d >= 2 there is b_d>0 such that

\[
 V_n\geq b_d n^{1-3/d}\quad\hbox{for every even }n\geq2. \tag{C}
\]

Proof. Let g(x)=E[M_n|X_1=x] and u=g-mu_n. The function M_n is globally Lipschitz on configurations. It is homogeneous of degree one, so Euler's identity sum_i X_i dot grad_i M_n=M_n holds almost everywhere, by differentiating the scaling identity at differentiability points. Integration by parts on Q^n is valid for Lipschitz functions. Since x_j=0 on a lower face and x_j=1 on an upper face, symmetry gives

\[
 \mu_n=n\left\{\sum_{j=1}^d\int_{[0,1]^{d-1}}g(x_{-j},1)dx_{-j}-d\mu_n\right\}.
\]

Thus the average upper-face integral of u equals B=mu_n/(dn)>0. The same identity follows by differentiating the integral over [0,t]^(dn), providing a separate derivation without gradients of the minimizing matching.

For 0<t<=1, 1-Lipschitz continuity gives, for each face,

\[
 \int u(x_{-j},1)dx_{-j}
 \leq {1\over t}\int_{x_j\in[1-t,1]}u(x)dx+{t\over2}
 \leq \sqrt{\|u\|_2^2/t}+{t\over2}.
\]

Average over j. Since mu_n <=n sqrt(d)/2, B<=1/(2 sqrt(d))<1. Take t=B to obtain ||u||_2^2>=B^3/4. First-order projections g(X_i)-mu_n are orthogonal and each has covariance ||u||_2^2 with M_n. The same Cauchy–Schwarz argument as above yields V_n>=n||u||_2^2>=n B^3/4. Apply (1) to finish, with b_d=A_d^3/(4d^3). □

This gives n^(-1/2) in d=2 and a constant in d=3. It does not reach the desired order in any d>=2.

### Theorem D: exact d=1 formula (elementary comparison case)

For n=2m uniform points on [0,1],

\[
 M_n\sim\operatorname{Beta}(m,m+1),\qquad
 \mu_n={m\over2m+1},\qquad
 V_n={m(m+1)\over(2m+1)^2(2m+2)}={n\over4(n+1)^2}\sim{1\over4n}. \tag{D}
\]

Proof. Sort the points U_(1)<...<U_(2m). The optimal matching is consecutive pairs: the leftmost point can be paired to the second by an exchange of two edges without increasing the total, and induction completes the argument. More explicitly, for a<=b<=c<=e the pairing (a,b),(c,e) costs at most either other pairing, with the difference 2(c-b) for (a,c),(b,e) and for (a,e),(b,c). Thus M_n=sum_(j=1)^m (U_(2j)-U_(2j-1)). The n+1 uniform spacings have the Dirichlet(1,...,1) law, so the sum of these m spacings has the displayed beta law. Its variance gives (D). Equivalently write the spacings as independent rate-one exponentials divided by their sum; summing m selected and m+1 remaining exponentials yields independent Gamma(m,1), Gamma(m+1,1) variables and the same beta law. The ordinary CLT and delta method give sqrt(n)(M_n-mu_n) -> N(0,1/4), which also establishes the n^(-1/2) anti-concentration scale in this one-dimensional comparison. □

### Theorem E: a weaker all-n anti-concentration bound, d >= 2

For every fixed d>=2, M_n has fluctuations of order at least n^(-1/d) in Chatterjee's Definition 1.1. This loses a factor sqrt(n) against the requested scale n^(1/2-1/d).

Proof. Use the already proved constants A_d,B_d in (1)–(2), and put a=1-1/d and p_0=A_d/(2B_d)>0. Since E M_n>=A_d n^a and M_n<=B_d n^a, the elementary inequality

\[
 E M_n\leq (A_d/2)n^a+B_d n^a P(M_n\geq (A_d/2)n^a)
\]

gives P(M_n>=(A_d/2)n^a)>=p_0. Set alpha=min(1,p_0/(2d)), X'_i=X_i/(1+alpha/n), and M'_n=M_n/(1+alpha/n). The total variation distance between the two configuration laws is exactly

\[
 1-(1+\alpha/n)^{-dn}\leq d\alpha\leq p_0/2.
\]

On the preceding event, M_n-M'_n=alpha M_n/(n+alpha)>=D_n, where D_n=(alpha A_d/4)n^(-1/d). For any interval I of width at most D_n/2, both M_n and M'_n belonging to I implies M_n-M'_n<=D_n/2, an event of probability at most 1-p_0. Also the two probabilities of belonging to I differ by at most p_0/2, by data processing for total variation. Inclusion–exclusion therefore gives

\[
 2P(M_n\in I)\leq 1+P(M_n\in I,M'_n\in I)+p_0/2
                 \leq 2-p_0/2.
\]

Thus P(M_n in I)<=1-p_0/4, uniformly over I, proving the assertion with c_1=alpha A_d/8 and c_2=p_0/4. This is the elementary dilation version of Chatterjee's coupling principle at perturbation size 1/n; the uniform configuration laws stay close in total variation at this perturbation size. □

## Gaps that cannot be replaced by assertions

To get the desired all-n variance lower bound from (A), it would suffice to prove |mu_n-mu_(n-2)|>=c_d n^(-1/d) for every sufficiently large even n. The first-order limit alone does not imply this finite-difference estimate: the abstract even-index sequence a_n=beta*(4 floor(n/4))^(1-1/d) has the same leading asymptotic but zero increments at n=4k+2. This is an illustration of the inference gap, not a model for the matching mean. The telescope proves only (B). No monotonicity or differentiability of the asymptotic mean sequence is assumed.

A generic stabilization theorem also does not close the problem. Smooth subadditivity, which the matching functional does satisfy, is different from localization of its optimal edges or of a suitable add-two cost. A matching-specific stabilization argument, its moment bounds, the strictly positive *binomial* variance after fixing the point count, and the boundary/de-Poissonization steps would all need proof. None is supplied here.

Even an isolated close pair need not be matched internally. On a line, put a=-epsilon, b=epsilon, x=-R, y=R, with R>epsilon>0. Pairing a,b together and x,y together costs 2R+2epsilon, whereas pairing x,a and b,y costs 2R-2epsilon. This embeds in any dimension and persists under small perturbations. Therefore an empty surrounding annulus alone cannot justify independent local variance contributions. This is an obstruction to that proposed proof, not a counterexample to the variance conjecture.

Finally, neither (B) nor (C), nor even an all-n variance lower bound by itself, proves Definition 1.1 at the target scale. The direct bound (E) only reaches the smaller scale n^(-1/d). A direct coupling/anti-concentration argument, or adequate higher-moment control combined with a variance bound, is still required for Chatterjee's literal fluctuation question in d>=2.

## Literature audit

The search ran on 13 November 2026, covering work appearing from 2017 through that date and the older foundational references named in the request. Full primary texts were used when accessible. Failure to find a theorem is a bounded search result, not a proof that no such theorem exists. The unqualified name “Gold” did not identify a relevant primary reference despite searches with matching, variance, fluctuations, and Euclidean CLTs; no theorem is attributed to an unidentified author.

| Reference and exact location in the text read | What it proves and why it does or does not answer item (3) |
|---|---|
| [Chatterjee, arXiv:1706.04290v3](https://arxiv.org/abs/1706.04290v3), Definition 1.1, p.3; Lemma 1.2, p.3; Theorem 1.7, p.7; Corollary 1.8, p.9 | A coupling bound on interval probabilities, with a Hellinger/total-variation estimate for small multiplicative perturbations. This is a genuine fluctuation method; the smooth-density hypotheses matter. |
| Same paper, Theorem 2.1 and Corollary 2.2, p.11; explanatory paragraph p.12 | For homogeneous functionals under densities in P(d) or P+(d), the fluctuation lower bound is n^(-1/2)t_n. For one-colour matching with d>=2, t_n has order n^(1-1/d), giving the target exponent. Uniform cube density is outside these classes. |
| Same paper, Theorem 2.3, p.12, proof pp.12–14 | Target-order lower fluctuations for the **travelling salesman tour** on uniform cube points, d>=2. Its argument is not a matching theorem. The paper's other examples, Sections 2.2–2.5, pp.14–27, concern SK, first-passage percolation, independent-edge assignment, and determinants. |
| [Talagrand (1995), *Concentration of measure and isoperimetric inequalities in product spaces*](https://www.numdam.org/articles/10.1007/BF02699376/), Publ. Math. IHÉS 81, 73–205, Section 11.5, printed pp.187–191 = PDF pp.116–120; Theorem 11.5.3, printed p.189 = PDF p.118 | Treats the correct one-colour ordinary-distance model. Printed p.188 = PDF p.117 reports Rhee's O((log n)^2) planar variance bound and announces n^(1-2/d) times a dimension-dependent logarithmic power for d>=3. Its suggested n^(1-2/d) lower bound is explicitly unverified prose, **not a proved theorem**. The displayed theorem controls a Poissonized concentration distance. |
| [Feng, arXiv:2610.14337v2](https://arxiv.org/abs/2610.14337v2), 3 November 2026, Theorem 1.1 and Theorem 1.2, PDF p.2; cube specialization proof and historical discussion pp.3–4 | Theorem 1.2 states V_n <= C d n^(1-2/d) for the exact uniform-cube model, d>=2, n even. It is a **preprint upper bound**, not a lower bound or a CLT. For fixed d it supplies the proposed sharp upper order. It does not settle E0031. No part of proofs A–E relies on this preprint. |
| [Steele (1997), *Probability Theory and Combinatorial Optimization*](https://doi.org/10.1137/1.9781611970029), CBMS-NSF Applied Mathematics 69, cited p.63, equation (3.28) | Chatterjee cites this book for upper bounds. Feng p.3 reports that integrating (3.28) gives exponent (d-1)/(2d), whereas the subsequent printed exponent is (d-2)/(2d). The full SIAM chapter was inaccessible here, so this typo diagnosis is **reported from Feng**, not independently verified from the book. It cannot be used as an established exact variance upper bound. |
| [Barthe–Bordenave, arXiv:1103.2734v2](https://arxiv.org/abs/1103.2734v2), Theorem 2, PDF p.3, and Theorem 3, p.4; published in *Séminaire de Probabilités XLV*, LNM 2078 (2013), 483–535 | First-order limits/bounds for **bipartite** costs with power p and d>2p. These are not lower bounds on the centred variance. The date in the PDF body differs from its arXiv version stamp; the stamp is 5 October 2011. |
| [Goldman–Trevisan, arXiv:2009.04128v2](https://arxiv.org/abs/2009.04128v2), Theorem 1.1, PDF p.2; published *Probability and Mathematical Physics* 2 (2021), 341–362 | For bipartite matching, d>=3 and p>=1, n^(p/d-1) times the **expected** total cost converges to a positive constant. This is an expectation theorem, not a variance theorem. |
| [Goldman–Trevisan, arXiv:2209.14615v2](https://arxiv.org/abs/2209.14615v2), Theorem 1.1, PDF pp.3–4, and Corollary 1.5, p.4 | Extends first-order asymptotics for bipartite geometric optimization, d>=3 and 1<=p<d, including almost sure statements for uniform sampling. It is not a variance lower bound. |
| [Ambrosio–Stra–Trevisan, arXiv:1611.04960v1](https://arxiv.org/abs/1611.04960), Theorem 1.1, PDF p.3, equation (1.2); published *Probab. Theory Related Fields* 173 (2019), 433–477 | In d=2, for **squared-distance bipartite** matching on the square or flat torus, E[total squared cost]/log n ->1/(2 pi). The empirical-to-uniform analogue has 1/(4 pi). These are first-order quadratic transportation costs, not the non-bipartite p=1 variance in E0031. The text read is v1, 15 November 2016; the published paper appeared in 2019. |
| [Ambrosio–Glaudo (2019), *Finer estimates on the 2-dimensional matching problem*](https://jep.centre-mersenne.org/articles/10.5802/jep.105/), Theorems 1.1 and 1.2, printed p.740 = PDF p.5 | Improved expected-cost asymptotics for bipartite and semi-discrete **quadratic** transport, including surfaces. No non-bipartite p=1 variance conclusion. |
| [Ambrosio–Goldman–Trevisan, arXiv:2110.14372](https://arxiv.org/abs/2110.14372), Theorems 1.1 and 1.2, PDF p.3 | Planar domains and positive Hölder densities; expectation asymptotics for empirical-to-density and **bipartite squared-distance** cost. Theorem 1.2 gives area/(2 pi) for equal sample sizes after the log normalization. |
| [Armegioiu–Goldman–Grotto–Trevisan, arXiv:2609.08717v2](https://arxiv.org/abs/2609.08717v2), Theorem 1.1, PDF p.2 | A 2026 preprint on exact **first-order expected** bipartite costs on the flat torus, every finite power q>=1. It does not provide the variance lower bound here. |
| [Dereich–Scheutzow–Schottstedt (2013)](https://numdam.org/articles/10.1214/12-AIHP489/), Ann. IHP Probab. Statist. 49, 1183–1203; Theorem 1, printed p.1186 = PDF p.4; Theorem 2, printed p.1187 = PDF p.5 | Empirical-measure quantization in p-Wasserstein cost for 1<=p<d/2, with moment bounds and high-resolution first-order formulae. This is not one-colour matching variance. |
| [Ledoux (2019), *A fluctuation result in dual Sobolev norm for the optimal matching problem*](https://perso.math.univ-toulouse.fr/ledoux/files/2022/03/matchingclt.pdf), Theorem 1, PDF p.3; Corollary 2 and following paragraph, p.4 | A limit for a renormalized H^(-1) quadratic energy, d<=3, and regularized empirical transport. The paragraph after Corollary 2 explains why this does not give the unregularized W_2 result. It is not a theorem on M_n. |
| [Ledoux–Zhu, arXiv:1911.07579](https://arxiv.org/abs/1911.07579), Theorem 1, PDF p.3 | Gaussian empirical-to-law transport: expected p-Wasserstein cost has order n^(-p/d) for d>=3, 1<=p<d. Different distribution, functional, and moment. |
| [Yukich, *Limit theorems in discrete stochastic geometry*](https://www.lehigh.edu/~jey0/SpringerLNMsurvey-JY.pdf), 2013 survey: Theorem 8.1 printed p.249 = PDF p.11; Theorem 8.3 printed p.251 = PDF p.13; Theorem 8.5 printed p.258 = PDF p.20; Theorem 8.6 printed p.266 = PDF p.28 | MM appears among **smooth subadditive** examples; these hypotheses yield first-order laws. The variance/CLT results require additional score stabilization and moment hypotheses. The binomial variance subtracts a squared mean add-one term from the Poisson variance; positivity does not follow merely from a positive Poisson variance. No matching-specific verification was found. |
| Penrose–Yukich (2001), *Central limit theorems for some graphs in computational geometry*, Ann. Appl. Probab. 11, 1005–1041, DOI [10.1214/aoap/1015345393](https://doi.org/10.1214/aoap/1015345393); [Penrose–Yukich (2005) preprint](https://www.lehigh.edu/~jey0/Steinpaper.pdf), Theorem 2.1, PDF p.5, Corollary 2.1, p.6, remarks p.7 | General CLT frameworks with explicit stabilization assumptions, the assumptions must be verified separately for minimum matching. Theorem 2.1 of the 2001 paper, printed pp.1008–1009 = PDF pp.4–5, and Corollary 2.1, printed p.1009 = PDF p.5, were subsequently checked through the original paper mirrored at [SciSpace](https://scispace.com/pdf/central-limit-theorems-for-some-graphs-in-computational-36766b1t9t.pdf). Printed p.1010 = PDF p.6 explicitly lists minimal matching as an open application for which stabilization had not been proved. The accessible 2005 paper states separately that the variance asymptotic and its positivity require further arguments. Its theorem numbering differs from the published book chapter. |
| Kesten–Lee (1996), *The central limit theorem for weighted minimal spanning trees on random points*, Ann. Appl. Probab. 6, 495–527, DOI [10.1214/aoap/1034968141](https://doi.org/10.1214/aoap/1034968141); [Chatterjee–Sen (2017)](https://arxiv.org/abs/1307.1661), Ann. Appl. Probab. 27, 1588–1645 | These concern **minimum spanning trees**, including positive-variance CLTs and quantitative normal approximation, not perfect matching. Kesten–Lee Theorem 1, printed p.496 = PDF p.2, was checked in the [original paper text at a mirror](https://scispace.com/pdf/the-central-limit-theorem-for-weighted-minimal-spanning-5cejoxqcuk.pdf); for every alpha>0 and d>=2 it gives the centred MST weight divided by n^((d-2alpha)/(2d)) converging to N(0,sigma^2), sigma^2>0. |
| [Cao, arXiv:1905.08366](https://arxiv.org/abs/1905.08366), Theorem 2.1 and Theorem 2.2, PDF p.5; published Ann. Appl. Probab. 31 (2021), 1687–1723 | CLTs for maximum-weight sparse Erdős–Rényi matching and lambda-diluted minimum matching with **independent edge weights**. Euclidean distances share point coordinates and have geometric dependence. These are different models. |
| [Chatterjee–Ray, arXiv:2410.21513v1](https://arxiv.org/abs/2410.21513), Section 3.8, final paragraph, PDF p.77; Remark 3.9.6, p.79 | Studies perturbation stability and near-optimal solution sets. It explicitly leaves matching stability challenging. This “stability” is not identical to score stabilization for CLTs; the paper is not a variance solution. |
| [Holroyd–Janson–Wästlund (2022), *Minimal matchings of point processes*](https://doi.org/10.1007/s00440-022-01151-y), Probab. Theory Related Fields 184, 571–611, Theorems 5 and 6, PDF p.7; Theorem 7, PDF p.8 (online-first typesetting, without final journal page numbers) | Infinite-volume, locally minimal matchings and edge-length tails, especially d=1. Existence/local minimality and edge tails do not yield the fixed-n total-cost variance required here. |

The source files preserve version stamps and page breaks. Retrieval limits are stated where the original text was unavailable. In particular, the named “Gold” lead and the inaccessible Steele chapter prevent calling this a completely exhaustive literature audit.

For a concrete check on why the smooth-density dilation cannot simply be reused, let U be uniform on Q^n and U' uniform on ((1+epsilon)^(-1)Q)^n. Then d_TV(U,U')=1-(1+epsilon)^(-dn), which tends to 1 for epsilon=alpha/sqrt(n). The small-TV step of Chatterjee's smooth-density coupling therefore fails at the target perturbation size.

The full query/disposition record is in sources/SEARCH.txt.

## Computation and verification

The main experiment contains 7,680 independent configurations: d=2,3,4; n=32,64,128,256,512,1024,2048; respectively 500,500,400,400,320,240,200 samples per dimension. The sample plan was fixed before the run. Each sample uses a complete-graph **Blossom V** solve for the non-bipartite perfect matching. No geometric edge truncation or bipartite solver was substituted.

The implementation is Vladimir Kolmogorov's Blossom V 2.05, described in *Mathematical Programming Computation* 1 (2009), 43–67, [author's source distribution](https://pub.ista.ac.at/~vnk/software.html). The research-only source, licence, archive checksum and local modifications are in code/vendor/. The private wrapper uses 64-bit integral costs round(10^12 times distance). Every instance passes the integral dual-feasibility and complementary-slackness checker at zero tolerance, over all edges of the complete graph. The reported cost is the selected matching's ordinary Euclidean length.

**Numerical exactness:** this is an exact optimizer of the discretized weights, not a symbolic exact comparison of sums of square roots. With S=10^12 and n/2 edges, rounding contributes at most n/(4S) to the cost of any matching, so the selected real cost exceeds the true optimum by at most n/(2S), plus floating-point distance-evaluation error. At n=2048 the explicit quantization part is 1.024e-9. This error is negligible relative to the observed fluctuations.

Checks before sampling: 120 exhaustive enumerations for n<=12 in dimensions 1–4; 36 independent NetworkX integer-weight comparisons for n=16,32,64; 15 comparisons to consecutive pairing in d=1 through n=2048; and 12 duplicate-pair tests. All passed. The largest difference in ordinary lengths between independently obtained matchings in those NetworkX checks was 1.78e-15. The final audit additionally regenerates one configuration and re-solves one sample in each of the 21 groups, verifies its point hash and partners, and independently re-sums its edge lengths.

The run used one numerical thread and nice 10 throughout. Peak recorded resident memory was 433.1 MiB (0.454 GB). The sample count, priority, integer-certificate status and memory are recorded in data/samples.csv. The source inventory contains only plain text; the final filesystem audit checks that no PDFs or raster images were retained.

The following are unbiased sample variances (denominator samples minus one). Intervals are approximate 95% percentile nonparametric bootstrap intervals from 4,000 resamples within each (d,n) group. They describe Monte Carlo uncertainty at fixed n, not asymptotic validity of a proposed scaling law.

| d | n | samples | sample variance | 95% bootstrap interval | variance / n^(1-2/d) |
|---:|---:|---:|---:|---:|---:|
| 2 | 32 | 500 | 0.0341928 | [0.0301709, 0.0383895] | 0.0341928 |
| 2 | 64 | 500 | 0.0281685 | [0.0247885, 0.031606] | 0.0281685 |
| 2 | 128 | 400 | 0.0228233 | [0.0198363, 0.0259232] | 0.0228233 |
| 2 | 256 | 400 | 0.0213771 | [0.0186337, 0.0242907] | 0.0213771 |
| 2 | 512 | 320 | 0.0180975 | [0.01533, 0.0210357] | 0.0180975 |
| 2 | 1024 | 240 | 0.017853 | [0.014771, 0.0209973] | 0.017853 |
| 2 | 2048 | 200 | 0.0194815 | [0.0154717, 0.0237442] | 0.0194815 |
| 3 | 32 | 500 | 0.0816024 | [0.0721312, 0.0909929] | 0.0257032 |
| 3 | 64 | 500 | 0.0800191 | [0.0697494, 0.0905566] | 0.0200048 |
| 3 | 128 | 400 | 0.0936708 | [0.0806812, 0.107181] | 0.0185866 |
| 3 | 256 | 400 | 0.100236 | [0.0872719, 0.113173] | 0.0157862 |
| 3 | 512 | 320 | 0.12877 | [0.10813, 0.150658] | 0.0160963 |
| 3 | 1024 | 240 | 0.137822 | [0.114668, 0.161234] | 0.0136737 |
| 3 | 2048 | 200 | 0.20024 | [0.16461, 0.236954] | 0.0157679 |
| 4 | 32 | 500 | 0.120068 | [0.105847, 0.135041] | 0.0212252 |
| 4 | 64 | 500 | 0.135507 | [0.120499, 0.151498] | 0.0169383 |
| 4 | 128 | 400 | 0.188698 | [0.164945, 0.214086] | 0.0166787 |
| 4 | 256 | 400 | 0.248246 | [0.215747, 0.282716] | 0.0155154 |
| 4 | 512 | 320 | 0.315547 | [0.265206, 0.367785] | 0.0139453 |
| 4 | 1024 | 240 | 0.414052 | [0.348909, 0.480234] | 0.0129391 |
| 4 | 2048 | 200 | 0.607753 | [0.49629, 0.720414] | 0.0134296 |

For n>=256, exploratory regressions of log sample variance on log n give:

| d | fitted slope | 95% bootstrap interval | target exponent 1-2/d |
|---:|---:|---:|---:|
| 2 | -0.042 | [-0.157, 0.069] | 0.000 |
| 3 | 0.309 | [0.205, 0.412] | 0.333 |
| 4 | 0.427 | [0.315, 0.528] | 0.500 |

The planar variance falls overall from 0.0342 at n=32 to 0.0195 at n=2048, with a small rise between the last two sizes. The variances in dimensions 3 and 4 grow overall, while the target-normalized variances also retain finite-size drift. These observations neither establish nor refute a positive asymptotic variance constant. In particular, a finite-range fitted exponent is not a theorem about liminf or anti-concentration. Fits over the full n>=32 range are also retained in data/trends.json.

A separate d=1 calibration used 10,000 sorted-sample exact pairings at each of n=32,128,512,2048. The empirical/exact variance ratios were 0.984, 0.974, 0.992, 1.010, respectively; see data/d1_summary.json. These additional 40,000 observations are not counted among the 7,680 Blossom experiments.

The written proof was checked independently at its main identities: duplicate deletion by an edge exchange; the projection inequalities by orthogonality and covariance; the boundary identity both by integration by parts and differentiation of the scaled-cube integral; and the d=1 variance both from beta moments and Dirichlet spacing covariances. For n=2,d=1, exact polynomial integration gives Var(g(X))=1/180 and integral h^2=2/45, so 2 Var(g(X))+integral h^2=1/18. The rational audit checks the corresponding one-dimensional mean, increment and variance identities for every even n from 2 to 200. These finite checks support the analytic arguments; they are not proofs of a higher-dimensional asymptotic claim.

Raw observations, per-group summaries, bootstrap trends, run metadata, saved example point sets, verification results, and the plot data/variance.svg are in data/. Reproduction commands are in code/README.txt. The final audit is data/final_audit.json and the artifact checksums are data/manifest.json.

The uniform all-large-even-n lower bound c_d n^(1-2/d) in d>=2, and the target-scale anti-concentration conclusion, remain unproved here. The label PARTIAL refers to the proved weaker bounds and subsequence result, not to a full solution or a confirmed literature resolution.

Task: “Open problem E0031.” Request/run start: 13 November 2026, 13:15 Asia/Tbilisi (+04), as recorded in the original run log.
