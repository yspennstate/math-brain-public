PROVED

# Complete mixability on a bounded interval

**Theorem 1.** Let $F$ be a probability measure on a bounded interval, and suppose that its absolutely continuous part has positive mass. There exists an integer $N(F)$ such that $F$ is $n$-completely mixable for every integer $n\ge N(F)$. Consequently, the answer to D0007 is affirmative.

**Theorem 2.** Suppose $F$ is supported in an interval of length $R>0$, and, as measures,
\[
 F\ge q\,U[c-H,c+H],\qquad H>0,\quad 0<q\le1.
\]
Then $F$ is $n$-completely mixable for every integer
\[
 n\ge \frac{6R/H+1}{q}.                                      \tag{1}
\]
The remainder of $F$ may have atoms, gaps, or a singular part.

The proof below uses the established monotone-density mixability theorem as an input. It gives a complete derivation of Theorems 1 and 2 from that theorem, including the approximation and marginal-recovery arguments.

## 1. Literature and provenance

The survey first appeared as arXiv:1411.6190 in 2014 and was published as Ruodu Wang, *Current open questions in complete mixability*, Probability Surveys **12** (2015), 13–32, DOI [10.1214/14-PS250](https://doi.org/10.1214/14-PS250). The question is Open Problem 7, Section 2.6; PDF pagination differs between versions. Its Theorem 5 contains the positive- and negative-part norm inequalities considered below. The bound $f\ge3/[n(b-a)]$ comes from Puccetti, Wang and Wang (2013), *Complete mixability and asymptotic equivalence of worst-possible VaR and ES estimates*, Insurance: Mathematics and Economics **53**, 821–828.

The following sources were checked on 13 November 2026:

| Source | Relevant content and consequence |
| --- | --- |
| Wang and Wang (2011), J. Multivariate Anal. **102**, 1344–1360, Theorem 2.4 and Corollary 2.9; [author manuscript](https://sas.uwaterloo.ca/~wang/papers/2011Wang-Wang-JMVA.pdf) | A monotone density on $[a,b]$ is $n$-CM exactly when $a+(b-a)/n\le\mu\le b-(b-a)/n$. This includes power densities vanishing at an endpoint. |
| Puccetti, Wang and Wang (2012), J. Appl. Probab. **49**, 430–440; [author manuscript](https://sas.uwaterloo.ca/~wang/papers/2012Puccetti-Wang-Wang-JAP.pdf) | Convexity at a common center, weak closure, concave densities and other sufficient conditions. |
| Puccetti and Wang (2015), *Detecting complete and joint mixability*, J. Comput. Appl. Math. **280**, 174–187; [author manuscript](https://sas.uwaterloo.ca/~wang/papers/2015Puccetti-Wang-JCAM.pdf) | Numerical detection via rearrangements and discretization. This is distinct from proving eventual exact mixability. |
| Wang and Wang (2016), *Joint mixability*, Math. Oper. Res. **41**, 808–826, [DOI](https://doi.org/10.1287/moor.2015.0755), Theorem 3.2 | Joint mixability for densities with a common direction of monotonicity under the mean condition. It also supplies the input needed for the exact two-band example in Section 5. |
| Yin and Zhu, [arXiv:1706.05499v4](https://arxiv.org/abs/1706.05499v4), revised 11 May 2023, Example 2.4 | Claims a negative answer. The claim is contradicted by Theorem 2; the precise issue is explained in Section 4.5. No journal reference is supplied on the checked arXiv record. |
| Komisarski and Labuschagne, *The Distributions of the Mean of Random Vectors with Fixed Marginal Distribution*, J. Theoret. Probab. **37** (2024), 2121–2129, online 25 September 2023, [DOI](https://doi.org/10.1007/s10959-023-01277-2) | Its introduction still lists the classical sufficient conditions. Its main result constructs an unbounded marginal with prescribed laws for the mean; it does not settle this bounded-support question. |
| Koike, Lin and Wang, *Joint mixability and notions of negative dependence*, [arXiv:2204.11438](https://arxiv.org/abs/2204.11438); Wang's [working-paper catalogue](https://sas.uwaterloo.ca/~wang/pages/WPS3.html), including 2025 entries | Concerns compatibility of joint mixes with other dependence properties. The catalogue does not identify a settlement of Open Problem 7. |
| the author, *Absolutely continuous laws on a bounded interval are completely mixable for all large n*, [public manuscript and code](https://github.com/yspennstate/complete-mixability-large-n) | Already contains Theorems 1 and 2 and the construction verified here. Retrieved revision: `4bd67dbdd5b621c08a813b909d10219d4dd2d18f`, dated 11 November 2026. This is an existing author manuscript, not a refereed publication identified in this search. |

Searches covered the exact open-problem wording, eventual mixability, bounded and unimodal densities, the Yin–Zhu claim and later papers through the date above. The author names suggested in the question also lead to Bellini–Karaşan–Pınar on integer matrices and Bellini–Klar–Müller on risk measures; neither is a general theorem for bounded absolutely continuous laws. No refereed settlement of this exact question was located. This is a bounded literature-search conclusion, not a claim that every paper published in 2014–2026 has been examined.

The affirmative construction is attributed to the existing the author manuscript. This report verifies and presents it, rather than claiming a new discovery. The norm analysis, discretization experiments and exact two-band calculation supplement that verification. Downloaded sources and retrieval information are in `sources/`.

## 2. Necessary conditions and endpoint tails

Let $[a,b]$ be the essential support hull, $a<b$, and write $\mu=\int x\,F(dx)$. Every nondegenerate law on this interval has $a<\mu<b$. The usual necessary mean condition is therefore satisfied for every integer
\[
 n\ge\max\left\{\frac{b-a}{\mu-a},\frac{b-a}{b-\mu}\right\}.       \tag{2}
\]

The norm condition is more precisely stated with positive and negative parts. With $x_+=\max(x,0)$, $x_-=\max(-x,0)$, and $s=(n\mu-t)/(n-1)$, it is
\[
 \|(X-t)_+\|\le(n-1)\|(X-s)_-\|,\qquad
 \|(X-t)_-\|\le(n-1)\|(X-s)_+\|.                       \tag{3}
\]
For a complete mix, $X_i-t=-\sum_{j\ne i}(X_j-s)$; taking positive parts, using monotonicity on nonnegative variables and the triangle inequality proves (3) for every law-determined norm in the survey's definition.

For fixed $t$, $s\to\mu$. In particular, endpoint decay rates do not force the right sides of the $L^p$ versions of (3) to vanish. The following uniform statement also allows $t$ and $p$ to vary with $n$.

**Proposition 3.** Let $F$ be any nondegenerate bounded law. Put
\[
 Y=X-\mu,\qquad M=\|Y\|_\infty,
 \qquad d=E[Y_+]=E[Y_-]>0.
\]
For every integer $n\ge2+M/d$, both inequalities (3) hold for every $t\in\mathbb R$ and every $L^p$ norm, $1\le p\le\infty$.

**Proof.** Set $\lambda=n-1$, so $\lambda d\ge d+M$. For $u\in[-M,M]$,
\[
 E[(Y-u)_+]\le d+u_-,\qquad
 E[(-\lambda Y-u)_+]\ge\lambda d-u_+\ge d+u_-.
\]
For $u>M$ the first expectation vanishes. For $u<-M$, it equals $-u$, whereas the second is at least $-u$ by Jensen's inequality. Both $Y$ and $-\lambda Y$ have mean zero. The stop-loss characterization of convex order gives
\[
 Y\preceq_{cx}-\lambda Y.
\]
Applying the same argument to $-Y$ gives $-Y\preceq_{cx}\lambda Y$. Write $v=t-\mu$. For $1\le p<\infty$, the function $z\mapsto(z-v)_+^p$ is convex, and hence
\[
 E[(Y-v)_+^p]\le E[(-\lambda Y-v)_+^p]
 =\lambda^p E[(X-s)_-^p].
\]
Taking $p$-th roots gives the first inequality of (3); reflection gives the second. Taking the limit $p\to\infty$ proves the assertions for $L^\infty$. ∎

Thus none of these norm tests can obstruct eventual mixability, even for bounded laws without a density. They do not suffice for mixability: a Bernoulli law with irrational success probability cannot be $n$-CM for any $n$, because its constant sum would be an integer equal to an irrational number $np$. For the full class of law-determined norms, Theorem 1 and the direct necessity proof of (3) show that no eventual obstruction exists for the laws in the question. Proposition 3 makes an independent assertion only for $L^p$ norms.

Power decay, superpolynomial decay such as $e^{-1/(x-a)}$, and gaps therefore give no counterexample to D0007. Gaps can nevertheless cause substantial finite-$n$ obstructions; Section 5 gives an example with a sharp eventual threshold.

## 3. Proof of the affirmative theorem

The following classical input will be used: a probability law with monotone density on an interval $[u,v]$, with mean $m$, is $k$-CM if and only if
\[
 u+\frac{v-u}{k}\le m\le v-\frac{v-u}{k}.                 \tag{4}
\]
This is the Wang–Wang monotone-density theorem cited in Section 1. No general assertion about asymmetric unimodal densities is required.

### 3.1. Two lemmas

**Lemma 4 (linear densities).** For $H>0$ and $|\beta|\le1$, define a density on $[-H,H]$ by
\[
 \ell_{H,\beta}(z)=\frac{1}{2H}\left(1+\beta\frac zH\right).
\]
Its mean is $\beta H/3$, it is $k$-CM for every $k\ge3$, and its mixtures satisfy $E[\ell_{H,B}]=\ell_{H,EB}$ for any random $B\in[-1,1]$.

**Proof.** Integration gives total mass one and mean $\beta H/3$. The density is monotone. Since
\[
 |\beta H/3|\le H/3\le H-2H/k\quad(k\ge3),
\]
(4) applies. The mixture identity follows from the affine dependence on $\beta$. ∎

**Lemma 5 (bounded sum error).** Let $T$ be supported in an interval of length $R$, with mean $m_T$. For every integer $k\ge1$, there are exchangeable $V_1,\ldots,V_k\sim T$ whose sum $S_k$ satisfies
\[
 ES_k=km_T,\qquad |S_k-km_T|\le R\quad\text{almost surely}.       \tag{5}
\]

**Proof.** Let $Q$ be a quantile function for $T$, with finite endpoint values equal to the support bounds. Take $W\sim U(0,1)$ and, independently, a uniform permutation $\sigma$ of $0,\ldots,k-1$. Put $V_i=Q((\sigma(i)+W)/k)$. Each quantile argument is uniform on $(0,1)$, so each marginal is $T$. The sum is $\sum_{j=0}^{k-1}Q((j+W)/k)$. For each $j$, both this summand and $k\int_{j/k}^{(j+1)/k}Q(u)\,du$ lie between $Q(j/k)$ and $Q((j+1)/k)$. Summing the error bounds telescopes to at most $R$. The expectation follows from the marginals. ∎

### 3.2. A uniform component and one extra variable

**Proposition 6.** Suppose $G\ge qU[c-H,c+H]$, $G$ is supported in an interval of length $R$, and $E$ is supported in an interval of length $L\ge0$. The tuple consisting of $N$ copies of $G$ and one copy of $E$ is jointly mixable whenever
\[
 N\ge\frac{3(2R+L)/H+1}{q}.                              \tag{6}
\]

**Proof.** First suppose $q<1$ and write $G=qU[c-H,c+H]+(1-q)T$. Let $m_T,m_E$ denote the means of $T,E$, and put $\mu=qc+(1-q)m_T$. When $q=1$, take $T=\delta_c$; it will be assigned no positions. Both $c$ and the support of $T$ lie in the interval supporting $G$, so $|m_T-c|\le R$ and $2H\le R$.

First assume $T,E$ are finitely supported. Write $m=N(1-q)$. Choose an integer-valued $K$ in the two neighboring integers $\lfloor m\rfloor,\lceil m\rceil$, with $EK=m$. If $m$ is an integer set $K=m$. Every value of $K$ with positive probability satisfies $|K-m|<1$. Set $M_K=N-K$. By (6),
\[
 M_K>Nq-1\ge3(2R+L)/H\ge12.                              \tag{7}
\]

Conditionally on $K=k$, choose uniformly a set $A\subset\{1,\ldots,N\}$ of size $k$. Fill its positions with the exchangeable variables of Lemma 5, independently of the choice of $A$, and denote their sum by $S$. For $k=0$, put $S=0$. Independently take $Y\sim E$. Define
\[
 C=N\mu+m_E-S-Y-(N-k)c,
 \qquad \beta=\frac{3C}{(N-k)H}.                           \tag{8}
\]
The identity $N\mu=(N-m)c+mm_T$ gives
\[
 C=(m-k)(m_T-c)-(S-km_T)-(Y-m_E).
\]
By (5),
\[
 |C|\le2R+L,
 \qquad |\beta|\le\frac{3(2R+L)}{(N-k)H}\le1.              \tag{9}
\]
Fill the remaining $N-k$ positions with $c+Z_i$, where the $Z_i$ have density $\ell_{H,\beta}$ and sum $C$, using Lemma 4. Such a coupling exists by (7)–(9). Because $T,E$ are finitely supported, only finitely many values of $(k,S,Y)$, and hence of the required couplings, occur. No measurable-selection assertion is needed.

Write $X_i$ for the resulting variables in the $N$ positions. Their sum with $Y$ is exactly $N\mu+m_E$. It remains to identify the marginal law, since $\beta$ itself need not have mean zero.

Fix a position $i$ and a bounded Borel function $h$. When $i\in A$, its contribution to $Eh(X_i)$ is $(EK/N)\int h\,dT=(1-q)\int h\,dT$. When $i\notin A$, its contribution is
\[
 E\left[\frac{N-K}{N}\int_{-H}^H h(c+z)\ell_{H,\beta}(z)\,dz\right].
\]
The constant part of this integral has coefficient $E[(N-K)/N]=q$. The coefficient of its linear part is zero, because
\[
 E[(N-K)\beta]=\frac{3EC}{H}=0,
\]
where $E[S\mid K]=Km_T$, $EY=m_E$, and $EK=m$ were used in (8). Thus $X_i\sim(1-q)T+qU[c-H,c+H]=G$. This proves the assertion for finitely supported remainders and extra laws.

For general $T,E$, choose finitely supported $T_j,E_j$ converging weakly to them, supported in the same respective compact intervals, and set $G_j=qU[c-H,c+H]+(1-q)T_j$. Their means converge. The construction above provides constant-sum joint laws with these marginals, all supported in a common compact product. A subsequence converges weakly. Its marginals are the required copies of $G$ and $E$. If $c_j=N\mu_j+m_{E_j}\to c_*=N\mu+m_E$, continuity of the sum on this compact product gives
\[
 E\left[\left(\sum_iX_i+Y-c_*\right)^2\right]
 =\lim_j(c_j-c_*)^2=0.
\]
The limiting sum is constant. ∎

**Proof of Theorem 2.** Apply Proposition 6 with $E=\delta_0$ and $L=0$. Its $N$ copies of $F$ then sum to $N\mu$. ∎

### 3.3. Convolution and recovery of the original marginals

**Lemma 7.** If a bounded-support measure $F$ has a nonzero absolutely continuous part, then $F^{*2}\ge qU[c-H,c+H]$ for some $q,H>0$.

**Proof.** Let $f$ be the density of its absolutely continuous part and choose a bounded nonzero function $g=\min(f,B)$, $B>0$. Then $F\ge g(x)\,dx$ and $F^{*2}\ge(g*g)(x)\,dx$. Translation continuity in $L^1$ implies continuity of $g*g$, since
\[
 |(g*g)(x+h)-(g*g)(x)|\le\|g\|_\infty
       \int |g(v+h)-g(v)|\,dv\longrightarrow0.
\]
Moreover $g*g\ge0$ and $\int(g*g)=(\int g)^2>0$. It is therefore at least some $\delta>0$ on a nondegenerate closed interval $[c-H,c+H]$. Taking $q=2H\delta\le1$ proves the claim. ∎

**Lemma 8.** If $a$ copies of $F^{*2}$ and $b\in\{0,1\}$ copies of $F$ are jointly mixable, then $F$ is $(2a+b)$-CM.

**Proof.** Take independent $U,V\sim F$ and a regular conditional distribution $\kappa(s,\cdot)$ of $(U,V)$ given $U+V=s$. Such a kernel exists on these Borel spaces and is concentrated on $u+v=s$ for $F^{*2}$-almost every $s$. Let $P_1,\ldots,P_a\sim F^{*2}$, together with $Y\sim F$ if $b=1$, be a joint mix. Given them, sample each pair $(X_{2j-1},X_{2j})$ from $\kappa(P_j,\cdot)$. Each pair has unconditional law $F\otimes F$, so every coordinate has law $F$, and each pair sums to $P_j$ almost surely. Their total, with $Y$ when present, is the constant sum of the original joint mix. ∎

**Proof of Theorem 1.** Suppose $F$ is supported in an interval of length $R$. By Lemma 7, $G=F^{*2}$ dominates $qU[c-H,c+H]$; it is supported in an interval of length $2R$. Proposition 6 gives a joint mix of $a$ copies of $G$ for
\[
 a\ge(12R/H+1)/q,
\]
and a joint mix of $a$ copies of $G$ with one copy of $F$ for
\[
 a\ge(15R/H+1)/q.
\]
Lemma 8 handles even and odd numbers of coordinates, respectively. In particular,
\[
 N(F)=2\left\lceil\frac{15R/H+1}{q}\right\rceil             \tag{10}
\]
is a valid eventual threshold. ∎

## 4. Consequences and comparison with proposed counterexamples

### 4.1. Power decay and thin endpoint tails

Theorem 1 applies to every density with power decay at either or both endpoints, regardless of its behavior elsewhere, and equally to densities with superpolynomial decay. No endpoint asymptotic assumption is needed. For the particular density $f(x)=(k+1)x^k$ on $[0,1]$, $k\ge0$, the monotone-density theorem gives the sharper exact characterization
\[
 F\text{ is }n\text{-CM}\quad\Longleftrightarrow\quad n\ge k+2
\]
for integers $n\ge2$. Indeed its mean is $(k+1)/(k+2)$, and substitution into (2) gives this condition.

### 4.2. Gaps

Every absolutely continuous law with finitely many gaps is eventually $n$-CM. The same holds with infinitely many gaps, or with a density supported on a positive-measure set containing no interval. In the latter case $F$ need not dominate any uniform interval law; Lemma 7 supplies one in $F^{*2}$. This convolution step is essential to covering all densities with the same argument.

### 4.3. A positive continuous density on the interior

If $f>0$ is continuous on $(a,b)$, choose any nondegenerate compact interval $[c-H,c+H]\subset(a,b)$. Its minimum $\delta$ is positive. Then $q=2H\delta$ and Theorem 2 gives the explicit sufficient bound
\[
 n\ge\frac{6(b-a)/H+1}{2H\delta}.                         \tag{11}
\]
Values of the density at endpoints are irrelevant.

### 4.4. Gluing and stronger extensions

If finitely many laws $F_j$ are $n$-CM with the same mean, so is any convex mixture of them: choose $j$ with its mixture probability, then sample its complete mix. The conditional constant sum is the same for every $j$. Compactly supported weak limits preserve $n$-CM by the compactness argument in Proposition 6. These facts justify gluing components with a common center; arbitrary truncations with different means cannot be glued this way.

Symmetric unimodal densities already enjoy $n$-CM for every $n\ge2$. The present argument requires only monotone linear densities for the conditional corrections, so it does not presume an unsolved characterization of asymmetric unimodal laws.

The proof also covers bounded laws $F$ for which some convolution power $F^{*r}$ has a nonzero absolutely continuous part. Apply Lemma 7 to that power and group coordinates in blocks of $2r$. For each remainder $0\le s<2r$, use the extra law $E=F^{*s}$, then disintegrate the blocks and the extra sum. There are finitely many remainder classes, so one threshold works for all of them.

### 4.5. Yin–Zhu's Example 2.4

That example considers $f=\sum_{m\ge1}\alpha_mf_m$, where
\[
 f_m(x)=C_mx^{2m}(1-x^2)^{-1/2},\quad -1<x<1,
 \qquad\alpha_m>0,\quad\sum_m\alpha_m=1,
\]
and asserts failure for every odd dimension. However $C_1=2/\pi$, and on $[1/2,3/4]$,
\[
 f\ge\alpha_1f_1\ge\frac{\alpha_1}{\pi\sqrt3}.
\]
Thus $F\ge qU[1/2,3/4]$ with $q=\alpha_1/(4\pi\sqrt3)$, $R=2$, and $H=1/8$. Theorem 2 proves $n$-CM for every integer
\[
 n\ge\frac{388\pi\sqrt3}{\alpha_1},                       \tag{12}
\]
including odd integers. The finite-dimensional endpoint-concentration argument preceding the assertion cannot hold for all dimensions for a fixed absolutely continuous law: $P(|X|\le r/(r+1))\to1$, whereas its required upper bound tends to zero. Example 2.4 supplies no additional proof of the asserted universal obstruction. The assertion therefore cannot be used as a settled counterexample.

## 5. A sharp example with one gap

**Proposition 9.** Let
\[
 F=\tfrac12U[0,1/10]+\tfrac12U[9/10,1].
\]
For integers $n\ge2$, $F$ is $n$-CM if and only if $n$ is even or $n\ge19$. Its smallest eventual threshold is $18$.

**Proof.** Center $F$ at $1/2$, writing each coordinate as $Y_i=D\varepsilon_i+V_i$, where $D=9/20$, $\varepsilon_i\in\{-1,1\}$ specifies its band, and $V_i\in[-1/20,1/20]$. Each $V_i$ has the uniform marginal on this interval; independence is not assumed. For odd $n$, $|\sum_i\varepsilon_i|\ge1$. A zero-sum coupling would imply
\[
 D\le\left|\sum_i V_i\right|\le\sum_i|V_i|,
 \qquad D\le nE|V_i|=n/40.
\]
Hence every odd $n\le17$ is impossible. Symmetry gives a two-coordinate complete mix $(X,1-X)$, so every even $n$ is possible by concatenation.

It remains to construct a 19-coordinate mix. Put $k=9$, $n=19$, $\delta=1/10$, $\theta=19/20$, and let $U$ denote the uniform law on $I=[-\delta/2,\delta/2]$. For $0<p<1$, let $U_p^{\rm top}$ be uniform on the top subinterval of $I$ of length $p\delta$, and $U_{1-p}^{\rm bottom}$ uniform on the complementary bottom subinterval. Define
\[
 H_p^+=(1-\theta)U+\theta U_p^{\rm top},\qquad
 H_p^-=(1-\theta)U+\theta U_{1-p}^{\rm bottom}.
\]
These laws have increasing and decreasing densities, respectively, on the full interval $I$, and
\[
 pH_p^++(1-p)H_p^-=U,\quad
 m(H_p^+)=\theta(1-p)\delta/2,\quad
 m(H_p^-)=-\theta p\delta/2.                              \tag{13}
\]

Choose $K=9$ or $10$, each with probability $1/2$, and choose uniformly which $K$ positions use the upper band. When $K=9$, prescribe the upper positions the centered marginals $D+H_{9/19}^+$, and the lower positions $-D+H_{10/19}^+$. All these densities are increasing. The total of their means is
\[
 -D+\theta\frac{k(k+1)\delta}{n}
 =-\frac9{20}+\frac{19}{20}\frac{9\cdot10}{19\cdot10}=0.
\]
Their support intervals all have length $1/10$; the sums of their lower and upper endpoints are respectively $-7/5$ and $1/2$. The joint monotone-density mean condition is
\[
 -\frac75+\frac1{10}\le0\le\frac12-\frac1{10}.
\]
Theorem 3.2 of Wang–Wang (2016) therefore supplies a zero-sum joint mix with these prescribed marginals. For $K=10$, use $D+H_{9/19}^-$ on upper positions and $-D+H_{10/19}^-$ on lower positions. These densities are all decreasing. Their total mean is zero, their endpoint sums are $-1/2$ and $7/5$, and the same condition holds. Permuting within the two sets of positions gives the specified marginal at each chosen position.

For a fixed coordinate, conditional on being in the upper band, the probabilities of $K=9,10$ are $9/19,10/19$; (13) makes its deviation uniform. Conditional on being in the lower band those probabilities are $10/19,9/19$, and (13), now with $p=10/19$, again gives a uniform deviation. Each band has probability $1/2$. Adding $1/2$ back produces 19 marginals $F$ with sum $19/2$. Finally concatenate this mix with any number of the two-coordinate mixes to obtain every odd $n\ge19$. ∎

## 6. Numerical experiments

Five laws on \([0,1]\) were tested for every \(n=3,\ldots,20\):

| Code name | Density/law | Mean |
| --- | --- | --- |
| `power4` | \(5x^4\) | \(5/6\) |
| `beta_3_5` | \(105x^2(1-x)^4\) | \(3/8\) |
| `thin_exp` | \(Z^{-1}e^{-1/x}\), \(Z=\int_0^1e^{-1/x}dx\) | \(0.7386887965794423\) |
| `two_bands` | \(\tfrac12U[0,0.1]+\tfrac12U[0.9,1]\) | \(1/2\) |
| `beta_3_3` | \(30x^2(1-x)^2\) | \(1/2\) |

### 6.1. LP formulation and its meaning

Partition \([0,1]\) into \(B\) bins with index \(j=0,\ldots,B-1\), and let \(p_j=F((j+1)/B)-F(j/B)\). For a tuple let \(c_j\) count the coordinates in bin \(j\). A continuous complete mix necessarily satisfies
\[
 \sum_j c_j=n,\qquad
 \left\lceil Bn\mu-n\right\rceil\le\sum_jjc_j\le\left\lfloor Bn\mu\right\rfloor. \tag{14}
\]
Use a column \(c/n\) for every nonnegative integer occupation vector obeying (14). The LP minimizes the marginal \(L^1\) error
\[
 \min\left\{\|Aw-p\|_1:w\ge0,\ \mathbf1^Tw=1\right\}.      \tag{15}
\]
The bins with exactly zero computed mass are omitted. An infeasible support means that no occupation vector meets (14). A positive optimum excludes the bin relaxation; zero only means that the relaxation is feasible. It does not specify the required distributions within the bins.

Columns are generated by pricing against the LP dual. The pricing problem is solved over all admissible occupation vectors by the recurrence
\[
 D(r,s)=\min_j\{D(r-1,s-j)+a_j\},\quad D(0,0)=0,
\]
with the terminal sum restricted by (14). Thus columns are not a random subset of tuples. With dual variables \(u,\gamma\), the minimum reduced cost \(\rho=\min_c[-u\cdot c/n-\gamma]\) gives the corrected dual lower bound \(p\cdot u+\gamma+\min(0,\rho)\), up to floating-point solver tolerances. The saved `lp_lower` reports this bound. No interval-arithmetic LP certification is claimed. All negative conclusions highlighted here also have analytic proofs.

SciPy's HiGHS dual simplex solves (15); primal and dual tolerances are \(10^{-9}\), and feasibility is recorded at objective below \(10^{-8}\). Small negative objective values of order \(10^{-10}\) are numerical zero. The raw files retain them.

### 6.2. Full LP table

The base run uses \(B=80\). `F` means outer feasible, `I` means positive numerical LP optimum, and `S` means no admissible support tuple. In particular, `F` is not a claim of exact continuous complete mixability.

| n | power4 | beta_3_5 | thin_exp | two_bands | beta_3_3 |
| --- | --- | --- | --- | --- | --- |
| 3 | I | F | I | S | F |
| 4 | I | F | F | F | F |
| 5 | I | F | F | S | F |
| 6 | F | F | F | F | F |
| 7 | F | F | F | S | F |
| 8 | F | F | F | F | F |
| 9 | F | F | F | I | F |
| 10 | F | F | F | F | F |
| 11 | F | F | F | I | F |
| 12 | F | F | F | F | F |
| 13 | F | F | F | I | F |
| 14 | F | F | F | F | F |
| 15 | F | F | F | F | F |
| 16 | F | F | F | F | F |
| 17 | F | F | F | F | F |
| 18 | F | F | F | F | F |
| 19 | F | F | F | F | F |
| 20 | F | F | F | F | F |

### 6.3. Rearrangement algorithm

For \(M\) rows, every column initially contains a random permutation of the midpoint quantiles \(Q((i+1/2)/M)\). Each update replaces one column by its oppositely ordered matching to the sum of the other columns. Three deterministic seeded restarts and at most 80 full sweeps are used; the restart with smallest root mean square error is retained. The reported quantity is
\[
 \operatorname{RMS}=\left(M^{-1}\sum_{i=1}^M(S_i-n\mu)^2\right)^{1/2}. \tag{16}
\]
The raw CSV also includes the maximum error, range of row sums, mean bias, and number of sweeps. The base run uses \(M=2048\).

| n | power4 RMS | beta_3_5 RMS | thin_exp RMS | two_bands RMS | beta_3_3 RMS |
| --- | --- | --- | --- | --- | --- |
| 3 | 3.670e-02 | 1.145e-04 | 2.728e-03 | 3.839e-01 | 1.429e-04 |
| 4 | 9.212e-03 | 1.081e-04 | 1.022e-04 | 4.272e-05 | 1.326e-04 |
| 5 | 5.663e-05 | 9.425e-05 | 9.284e-05 | 3.306e-01 | 1.117e-04 |
| 6 | 5.761e-05 | 8.860e-05 | 8.604e-05 | 3.480e-05 | 1.055e-04 |
| 7 | 5.745e-05 | 8.421e-05 | 8.426e-05 | 2.798e-01 | 1.012e-04 |
| 8 | 5.825e-05 | 8.113e-05 | 8.089e-05 | 2.990e-05 | 9.686e-05 |
| 9 | 6.133e-05 | 8.054e-05 | 7.981e-05 | 2.296e-01 | 9.519e-05 |
| 10 | 6.402e-05 | 7.842e-05 | 7.856e-05 | 2.730e-05 | 9.340e-05 |
| 11 | 6.685e-05 | 7.937e-05 | 7.755e-05 | 1.793e-01 | 9.079e-05 |
| 12 | 7.018e-05 | 7.823e-05 | 7.796e-05 | 2.643e-05 | 9.037e-05 |
| 13 | 7.374e-05 | 7.629e-05 | 7.825e-05 | 1.297e-01 | 8.837e-05 |
| 14 | 7.774e-05 | 7.709e-05 | 7.975e-05 | 2.403e-05 | 8.686e-05 |
| 15 | 8.180e-05 | 7.777e-05 | 7.913e-05 | 7.995e-02 | 8.581e-05 |
| 16 | 8.558e-05 | 7.785e-05 | 8.013e-05 | 3.150e-03 | 8.527e-05 |
| 17 | 9.002e-05 | 7.896e-05 | 7.975e-05 | 2.945e-02 | 8.484e-05 |
| 18 | 9.394e-05 | 7.923e-05 | 8.167e-05 | 7.032e-05 | 8.545e-05 |
| 19 | 9.855e-05 | 7.983e-05 | 8.270e-05 | 4.883e-05 | 8.477e-05 |
| 20 | 1.027e-04 | 8.005e-05 | 8.302e-05 | 2.222e-05 | 8.402e-05 |

### 6.4. Refinement, smallest dimensions, and the trend

For the narrow-gap law, 80 bins are too coarse to detect the obstructions at \(n=15,17\). With 400 bins the LP excludes both and remains feasible at 19:

| n | B | Quantile rows | LP status | LP L1 error | Corrected dual lower bound | RA RMS |
| --- | --- | --- | --- | --- | --- | --- |
| 15 | 400 | 8192 | outer_infeasible | 0.161111 | 0.161111 | 8.043e-02 |
| 17 | 400 | 8192 | outer_infeasible | 0.0122059 | 0.0122059 | 2.997e-02 |
| 19 | 400 | 8192 | outer_feasible | 0 | 0 | 1.221e-05 |

The power-density case shows a different discretization error. For the continuous law \(f=5x^4\) at \(n=5\), any coupling satisfies
\[
 E[(S-25/6)^2]\ge\int_0^{1/6}(1/6-x)^2\,5x^4dx
 =\frac{1}{21\cdot6^7},
\]
because the other four coordinates are at most 1. Its continuous RMS is at least \(4.124401881\times10^{-4}\). The coarser RA value in the table is smaller than this lower bound: the midpoint quantile sample has missed the rare lower tail. Its smallest sample value is \((1/4096)^{1/5}>1/6\). Increasing to 16384 rows restores that part of the tail:

| n | B | Quantile rows | LP status | RA RMS |
| --- | --- | --- | --- | --- |
| 5 | 160 | 16384 | outer_infeasible | 7.558e-04 |
| 6 | 160 | 16384 | outer_feasible | 6.692e-06 |

There is also an optimization limitation: the unstructured RA run at `two_bands`, \(n=16\), has a visible residual despite the exact two-coordinate construction proving mixability. A residual from this heuristic is not a nonmixability certificate.

| Law | Smallest outer-feasible n in 3..20 | Rigorous conclusion about smallest n / eventual threshold |
| --- | --- | --- |
| power4 | 6 | Exactly n-CM for \(n\ge6\), by the monotone theorem. |
| beta_3_5 | 3 | The experiment is compatible with 3-CM; this report does not prove its minimum. Theorem 2 on \([1/4,3/4]\), where \(f\ge945/4096\), proves every \(n\ge217\). |
| thin_exp | 4 | Exactly n-CM for \(n\ge4\), by monotonicity and its mean. |
| two_bands | 4 | The smallest integer overall is 2; in 3..20 it is 4. The first feasible odd n on the refined grid is 19, proved exact in Proposition 9. The eventual threshold is 18. |
| beta_3_3 | 3 | Symmetric unimodality proves every \(n\ge2\); the smallest tested integer is 3. |

The trend is consistent with eventual mixability. Gaps produce a parity pattern, rather than monotone feasibility in n before the eventual threshold. Thin tails can conceal a genuine obstruction from a small quantile sample. For well-mixed cases the nonzero RA error includes finite-sample mean bias and optimization error, so no convergence rate is inferred from this finite table.

### 6.5. Code, data, and resource limits

- `numerics.py`: laws, DP pricing, LP column generation, RA, and positive/negative control checks.
- `data/results_b80_r2048_all.csv`: all 90 base cases.
- `data/results_b400_r8192_two_bands_n15-17-19.csv`: gap refinement.
- `data/results_b160_r16384_power4_n5-6.csv`: thin-tail refinement.
- The matching `.json` files record runtime and peak process resident memory.
- `sources/prior_check_general.py` and `data/exact_prior_audit.txt`: 1000 random rational reservoir inputs, three eligible dimensions each, zero failures.
- `verify_exact.py` and `data/additional_exact_checks.json`: rational checks of Proposition 9 and the variance lower bound above.
- `make_tables.py`: reproduces these tables and checks consistency with the analytic controls.
- `validate_lp_threads.py` and `data/lp_thread_validation.json`: recheck every LP with the native HiGHS scheduler explicitly limited to one thread.
- `data/environment.json`: Python and dependency versions.
- `sources/manifest.json`, `sources/prior_commit.json`, `sources/SHA256SUMS`: source URLs, retrieved revision and content hashes.

Reproduction commands, run from this folder:

```sh
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python3 numerics.py --self-check
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python3 numerics.py --bins 80 --rows 2048
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python3 numerics.py --bins 400 --rows 8192 --law two_bands --n 15 17 19
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python3 numerics.py --bins 160 --rows 16384 --law power4 --n 5 6
python3 sources/prior_check_general.py > data/exact_prior_audit.txt
python3 verify_exact.py
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python3 validate_lp_threads.py
python3 make_tables.py
```

The largest measured process RSS was 129,826,816 bytes (123.8 MiB), below 4 GB. Calculations used a single process per experiment, serial dual simplex, and one BLAS thread; no worker pools were created. NumPy, SciPy and threadpoolctl are the computational dependencies. The three experiment durations were 234.2 s, 10.4 s, 39.0 s; the final LP recheck took 189.5 s and changed no classifications.

## 7. Remaining questions

D0007 and all three requested density subclasses are resolved by Theorem 1. The bounds (1) and (10) are sufficient, and are generally far from the smallest possible threshold. Determining that threshold for a particular asymmetric density remains a separate problem. No threshold uniform over all bounded absolutely continuous laws can exist: the monotone densities $(k+1)x^k$ require $n\ge k+2$. Proposition 9 also gives arbitrarily late odd-dimensional obstructions at a fixed mean when the band lengths tend to zero.

For $F_\delta=\tfrac12U[0,\delta]+\tfrac12U[1-\delta,1]$, the obstruction in Proposition 9 gives $n\ge2(1-\delta)/\delta$ for every feasible odd dimension. Thus late obstructions also occur within a family having the fixed mean $1/2$.

This report does not characterize purely singular bounded laws. Some are covered by the convolution extension in Section 4.4; arbitrary bounded laws are excluded by the irrational Bernoulli example. The minimal $n$ for numerical examples without a sharp analytic characterization is not inferred from a finite-resolution feasible LP or from a small rearrangement residual.
