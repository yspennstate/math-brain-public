PARTIAL

# D0037: spectral density and Gaussian interlaced mixing

No complete necessary-and-sufficient spectral characterization was proved, and no published resolution was located in the accessible literature searched on 13 November 2026. Some requested monograph chapters and older articles were unavailable in full text. This is not a certification that the question remains open in 2026. The detailed search and access record is [sources/SEARCH.md](sources/SEARCH.md).

The target is rho-star(n) tending to zero, not just less than one at some lag. A positive lower bound is not necessary, even for a moving average. Conversely, continuity allowing zeros, even together with ordinary rho-mixing, is insufficient. This report proves these statements, the Gaussian angle reduction, and a sufficient class. Its necessity remains unproved.

## 1. Definitions and literature outcome

Center the real stationary Gaussian sequence and assume Var(X_0)>0. Put \(m(dt)=dt/(2\pi)\), so that
\[
 \gamma(k)=\operatorname{Cov}(X_k,X_0)=\int e^{ikt}f(t)\,m(dt).
\]
The density is even, nonnegative, integrable, and defined almost everywhere. “Continuous” means a continuous periodic representative; positivity everywhere of this representative implies a positive lower bound, unlike positivity almost everywhere.

For sigma-fields \(\mathcal A,\mathcal B\), maximal correlation is
\[
 \rho(\mathcal A,\mathcal B)=\sup\{|EUV|:U\in L^2_0(\mathcal A),
 V\in L^2_0(\mathcal B),\ \|U\|_2=\|V\|_2=1\}.
\]
Bradley's definition is
\[
 \rho^*(n)=\sup_{\operatorname{dist}(S,T)\ge n}
 \rho(\sigma(X_s:s\in S),\sigma(X_t:t\in T)),\quad
 \operatorname{dist}(S,T)=\min_{s\in S,t\in T}|s-t|.                 \tag{1}
\]
Nonempty sets may be infinite and interlaced. Ordinary rho(n) restricts to past \((-\infty,0]\) and future \([n,\infty)\). Survey (2.7)–(2.9), printed pp. 113–114, defines rho-star-mixing as convergence to zero. Question 9 is on printed p. 135, PDF page 29.

The literature pass preceded the proof work. In Bradley (2005), these are already established:

| Location | Result |
|---|---|
| (7.1), pp. 133–134 | Gaussian maximal correlations equal their linear versions \(r,r^*\). |
| Theorem 6.3 and paragraph after (6.8) | Interlaced mixing requires a continuous density. |
| Theorem 6.4 | \(0<m\le f\le M\) iff \(r^*(1)<1\); alternatively iff \(r(1)<1\) and \(r^*(N)<1\) for some N. |
| Theorem 6.5 | Continuous strictly positive f iff \(r^*(1)<1\) and \(r^*(n)\to0\); \(r(1)<1\) may replace \(r^*(1)<1\). |
| Theorems 6.1–6.2 and 7.1(1) | Ordinary rho-mixing has the Helson–Sarason polynomial-times-\(\exp(u+Hv)\) criterion with u,v continuous. |

Lag one and the extra ordinary lag-one assumption cannot be removed. Question 8 is the corresponding linear problem. These theorems do not resolve Question 9.

Sarason (1975), Section 3, explicitly studies past/future angles. Merely mentioning VMO does not provide an interlaced criterion. Samorodnitsky (2006), pp. 187–188, also records the absence of an explicit interlaced spectral iff condition. The later Bradley random-field papers checked concern rates or limit theorems. Full Bradley 2007 chapters were not obtained, so a theorem hidden there has not been ruled out. Exact references and access qualifications appear in Section 10.

## 2. Gaussian reduction to an angle in L2(f)

Define
\[
 H_S=\overline{\operatorname{span}_{\mathbb R}\{X_s:s\in S\}},
 \qquad E_S=\overline{\operatorname{span}_{\mathbb C}\{e^{ist}:s\in S\}}
 \subset L^2(f\,dm).
\]
Use the ordinary minimal angle, without removing the intersection: a shared nonzero vector gives cosine one.

**Proposition 1.** For any S,T,
\[
 \rho(\sigma(X_s:s\in S),\sigma(X_t:t\in T))
 =\sup_{u\in H_S,v\in H_T}\frac{|\langle u,v\rangle|}{\|u\|\|v\|}
 =\|P_{E_S}P_{E_T}\|.                                           \tag{2}
\]
Thus
\[
 \rho^*(n)=\sup_{\operatorname{dist}(S,T)\ge n}\|P_{E_S}P_{E_T}\|.   \tag{3}
\]

**Proof.** For finite Gaussian vectors, remove deterministic directions, whiten the marginal covariances, and take an SVD of the cross covariance. Orthogonal coordinate changes give canonical pairs (U_i,V_i) of correlation c_i in [0,1]. Distinct pairs and unmatched coordinates are independent, by joint Gaussianity. Normalized Hermite polynomials obey
\[
 E[h_j(U_i)h_k(V_i)]=\mathbf1_{j=k}c_i^j.
\]
Tensor products form complete orthonormal bases of the two Gaussian L2 spaces. On centered functions, conditional expectation has singular values given by nonempty products of the c_i, together with zeros for unmatched coordinates. Its norm is \(\max_i c_i\), attained by linear forms. This proves equality of nonlinear and linear maximal correlations. Singular marginal covariance is handled by taking bases of the linear supports.

For infinite sets, exhaust them by finite sets. Conditional expectations of any fixed square-integrable functions onto these finite sigma-fields converge in L2. Variances and covariance converge. Hence infinite maximal correlation is the supremum of the finite correlations, just as for the closed linear spans. This includes supremum one without attainment.

Finally, \(\sum a_kX_k\mapsto\sum a_ke^{ikt}\) preserves norms by the covariance formula. It extends to the complexified linear space and carries the closed spans onto E_S. A real operator and its complexification have the same norm. The supremum of normalized inner products of two subspaces is the norm of their projection product. This proves (2)–(3). It is also survey (7.1), citing Kolmogorov–Rozanov (1960), Theorem 1. QED.

For finite S,T let \(A=(\gamma(s-s'))\), \(B=(\gamma(t-t'))\), \(C=(\gamma(s-t))\). Then
\[
 \rho(S,T)=\|A^{-1/2}CB^{-1/2}\|,\quad
 \rho(S,T)^2=\lambda_{\max}(CB^{-1}C^*,A).                         \tag{4}
\]
Marginal matrices are positive definite for any nonzero density: a nonzero trigonometric polynomial has finitely many zeros, so its squared f-norm is positive. Pseudoinverses are needed only for more general possibly singular spectral measures. Cholesky whitening has the same singular values as symmetric square-root whitening.

This exact operator reformulation is not itself a new solution of the spectral problem.

## 3. Boundedness: lag one versus some lag

**Proposition 2.** If \(0<m\le f\le M\), then
\[
 \rho^*(1)\le\frac{M-m}{M+m}<1.                                  \tag{5}
\]
Conversely, if \(c=\rho^*(1)<1\), set \(K=(1+c)/(1-c)\) and \(\gamma_0=\operatorname{Var}(X_0)\). Then
\[
                 \gamma_0/K\le f\le K\gamma_0\quad\text{a.e.}     \tag{6}
\]

**Proof.** Polynomials p,q with disjoint frequency supports are orthogonal in unweighted L2. Normalize their f-norms to one, adjusting a phase so that \(\langle p,q\rangle_f=b\ge0\). Their unweighted sum and difference have equal norms. Therefore
\[
 \frac{1+b}{1-b}=\frac{\|p+q\|_f^2}{\|p-q\|_f^2}\le M/m.
\]
The positive lower bound excludes b=1. Passing to closed spans proves (5).

Conversely, let \(Q(a)=\|\sum a_kX_k\|_2^2\). A sign choice splits the finite support into disjoint forms U,V. The correlation bound implies
\[
 (1-c)(\|U\|^2+\|V\|^2)\le\|U\pm V\|^2
       \le(1+c)(\|U\|^2+\|V\|^2).
\]
Thus \(K^{-1}Q(a)\le Q(\epsilon a)\le KQ(a)\). Average independent symmetric signs: the middle expression becomes \(\gamma_0\sum|a_k|^2\). Rearranging bounds Q(a) between \(\gamma_0/K\) and \(K\gamma_0\) times the coefficient norm squared. Test translated Fejer kernels at Lebesgue points to obtain (6). Complex coefficients are valid by complexification in Proposition 1. QED.

This is the classical Moore lag-one equivalence.

**Proposition 3.** If \(c=\rho^*(N)<1\) for some N, then
\[
                 f\le N\frac{1+c}{1-c}\gamma_0\quad\text{a.e.}   \tag{7}
\]

**Proof.** Within one residue class modulo N, disjoint subsets have distance at least N. The same sign argument bounds its quadratic forms by \(K\gamma_0\) times the coefficient norm squared. Split any finite form into N residue-class forms U_r. Then
\[
 \|\sum_r U_r\|^2\le N\sum_r\|U_r\|^2
                 \le NK\gamma_0\sum_k|a_k|^2.
\]
The spectral upper bound follows as above. QED.

Under rho-star-mixing choose N as in Proposition 3, obtaining an upper bound M. Bradley's unnormalized interlaced covariance coefficient satisfies \(\kappa(n)\le M\rho^*(n)\to0\). His Theorem 6.3, from Bradley (2003), Theorem 1.4 and Remark 1.8, implies continuity of f. Also \(\rho(n)\le\rho^*(n)\), so the ordinary Helson–Sarason condition is necessary.

With the extra assumption \(\rho(1)<1\), Bradley's Theorems 6.4–6.5 sharpen this to
\[
 [\exists N:\rho^*(N)<1]\iff 0<m\le f\le M,\qquad
 \rho^*(n)\to0\iff f\text{ continuous and strictly positive}.      \tag{8}
\]
The extra assumption cannot be dropped.

## 4. Sufficient conditions, including polynomial zeros

**Proposition 4.** Continuous strictly positive f implies rho-star-mixing.

**Proof with a uniform bound.** Let \(m=\min f>0\). Choose a trigonometric polynomial q of degree d with \(\|f-q\|_\infty\le\delta\). If p,r have frequency supports at distance n>d, then \(\int q p\bar r\,dm=0\). Hence
\[
 |\langle p,r\rangle_f|\le\delta\|p\|_0\|r\|_0
                      \le(\delta/m)\|p\|_f\|r\|_f.
\]
Thus \(\rho^*(n)\le\delta/m\) for n>d. Uniform trigonometric approximation proves convergence, uniformly over all separated sets. QED.

This is the existing Kolmogorov–Rozanov/Rosenblatt argument.

**Proposition 5.** A sufficient class is
\[
       f(t)=|P(e^{it})|^2g(t),\qquad
       g\text{ continuous and strictly positive}.                \tag{9}
\]

**Proof by filtering.** For real \(P(z)=\sum_{j=0}^dp_jz^j\), take a real Gaussian Y of density g and set \(X_k=\sum p_jY_{k-j}\). Its density is (9). The sigma-field indexed by S for X is contained in that indexed by \(S-\{0,\ldots,d\}\) for Y. Expanded sets have distance at least n-d, giving
\[
                  \rho_X^*(n)\le\rho_Y^*(n-d)\to0.               \tag{10}
\]
The Gaussian law is determined by covariance.

A spectral proof covers (9) whenever the resulting density is even, without a real-factor assumption. If nonnegative trigonometric polynomials q_j satisfy
\[
       |f-q_j|\le\epsilon_j f\quad\text{a.e.},\qquad
       \epsilon_j\downarrow0,                                   \tag{11}
\]
then \(\rho^*(n)\le\epsilon_j\) for \(n>\deg q_j\): the polynomial cross term vanishes and weighted Cauchy–Schwarz controls the error. For (9), use \(|P|^2\) times uniform polynomial approximants of g, positive for sufficiently accurate approximation. QED.

In fact, (11) is equivalent to class (9). Fix q_0 with relative error less than one. Every sufficiently accurate q_j is comparable to f and hence to q_0. Nonzero nonnegative trigonometric polynomials have finitely many circle zeros, each of even integer order. Comparability forces the same zeros and orders for all q_j. Thus q_j/q_0 extends to a positive continuous function. These quotients converge in essential sup norm to f/q_0, bounded above and below. For continuous functions sup norm equals essential sup norm, so the quotients are uniformly Cauchy. Their limit is a continuous strictly positive representative of f/q_0. Fejer–Riesz factorization gives q_0=|P|^2. The reverse implication was just proved.

This relative approximation criterion has not been proved necessary for rho-star-mixing.

## 5. A polynomial zero compatible with interlaced mixing

Let epsilon_k be independent N(0,1) and
\[
 X_k=\epsilon_k-\epsilon_{k-1},\qquad
 f(t)=|1-e^{it}|^2=2-2\cos t.
\]
Then \(\gamma(0)=2,\gamma(\pm1)=-1\), and \(\gamma(k)=0\) for \(|k|\ge2\). At distance at least two, the innovation sets \(S\cup(S-1)\) and \(T\cup(T-1)\) are disjoint. Their sigma-fields are independent, including for infinite sets. Thus \(\rho^*(n)=0\) for \(n\ge2\).

For lag one choose \(S=\{0,2,\ldots,2L-2\}\), \(T=\{1,3,\ldots,2L-1\}\). Marginal covariances are 2I and cross covariance is minus a bidiagonal matrix of ones. The normalized largest singular value is \(\cos(\pi/(2L+1))\), as follows by diagonalizing its tridiagonal product with its transpose. It tends to one. Consequently
\[
             \rho^*(1)=1,\qquad \rho^*(n)=0\quad(n\ge2).           \tag{12}
\]
This disproves candidate (a) as stated and the necessity direction of (b). A null-set change cannot fix the essential infimum zero. It also shows why “some lag” cannot replace “lag one” in Moore's theorem.

## 6. A bounded positive discontinuous density

Fix \(0<a<1\) and \(f_a(t)=1+a\,\operatorname{sgn}(\cos t)\). Values at the two jumps do not matter. It lies between 1-a and 1+a, with
\[
 \gamma(0)=1,\qquad
 \gamma(k)=\frac{2a}{\pi k}\sin(k\pi/2)\quad(k\ne0).                \tag{13}
\]

**Proposition 6.** Its coefficients are exactly
\[
                         \rho^*(n)=a\quad(n\ge1).                \tag{14}
\]

**Proof.** Proposition 2 gives the upper bound a. For the lower bound fix d with \(2d+1\ge n\). Use \(S=\{-2j:1\le j\le L\}\), \(T=\{2k+2d+1:1\le k\le L\}\). Each marginal covariance is I, since nonzero even Fourier coefficients vanish. Alternating signs turn the cross matrix into
\[
               \frac a\pi\left(\frac1{j+k+d+1/2}\right)_{j,k=1}^L.
\]
Choose coefficients \(j^{-1/2}\) normalized by \(H_L^{1/2}\), \(H_L=\sum_{j=1}^L1/j\). The correlation becomes
\[
 \frac a{\pi H_L}\sum_{j,k=1}^L
          \frac1{\sqrt{jk}(j+k+d+1/2)}.                           \tag{15}
\]
The sum dominates its decreasing summand integrated over \([1,L+1]^2\). Removing d+1/2 from the denominator changes the integral by \(O_d(1)\): \(1/(\sqrt{xy}(x+y)^2)\) is integrable on \([1,\infty)^2\). Substitute \(x=e^u,y=e^v\), \(R=\log(L+1)\). The remaining integral is
\[
 \int_0^R\int_0^R\frac{du\,dv}{2\cosh((u-v)/2)}
 =R\int_{-R}^{R}\frac{1-|s|/R}{2\cosh(s/2)}\,ds
 \sim\pi R.
\]
Since \(H_L\sim\log L\), (15) has lower limit at least a. Together with the upper bound this proves (14), without needing a Hilbert-matrix norm theorem. QED.

Thus bounds above and below imply a coefficient less than one but do not imply convergence to zero.

## 7. A continuous slow zero: ordinary rho-mixing but rho-star(n)=1

This also supplies an explicit example of \(\exp(Hv)\) with v continuous and Hv unbounded.

For \(|z|<1\) use principal analytic logarithms:
\[
 L(z)=\log\frac4{1-z},\qquad F(z)=\log L(z).
\]
They are well defined because \(\operatorname{Re}L(z)\ge\log2>0\). Set
\[
 v(t)=\operatorname{Im}F(e^{it}),\qquad v(0)=0.
\]
This is real, odd, and continuous on the circle. Indeed, \(|\operatorname{Im}L|\le\pi/2\), while \(\operatorname{Re}L\to\infty\) at z=1, so \(\arg L\to0\). Furthermore,
\[
 \|v\|_\infty\le\arctan\!\left(\frac{\pi}{2\log2}\right)<\pi/2.
\]
Use the conjugate-function convention \(H(\cos kt)=\sin kt\), \(H(\sin kt)=-\cos kt\), with zero mean. Then
\[
                Hv(t)=\log\log4-\log|L(e^{it})|.                 \tag{16}
\]
For justification, Im F is bounded harmonic, and F(0)=log log 4 is real. Parseval for its Taylor series shows that bounded L2 norms of Im F imply bounded L2 norms of Re F minus its constant. Thus F belongs to H2, and Fourier conjugacy gives (16) in L2 and almost everywhere. Its right side is unbounded below near zero.

Define
\[
 f_-(t)=\exp(Hv(t))
       =\frac{\log4}{|\log(4/(1-e^{it}))|}\quad(t\ne0),
 \qquad f_-(0)=0.                                               \tag{17}
\]
It is even, continuous, bounded by 2, positive away from zero, and
\[
                 f_-(t)\sim\frac{\log4}{\log(4/|t|)}
                 \quad(t\to0).                                 \tag{18}
\]
The Gaussian sequence is ordinary rho-mixing by Helson–Sarason, with P=1, u=0, and continuous v. Since \(\|v\|_\infty<\pi/2\), the Helson–Szego criterion (survey Theorem 6.1 with n=1) also gives \(\rho(1)<1\).

Nevertheless,
\[
                    \rho^*_{f_-}(n)=1\quad\text{for all }n.      \tag{19}
\]
One verification is Bradley's Theorem 6.4(c): if any coefficient were less than one, the additional \(\rho(1)<1\) would force a positive lower bound on f, contradicting (18). The following independent construction proves (19) directly.

**Periodic-block obstruction.** Suppose f is continuous, even, \(0\le f\le M\), and f(0)=0. Fix n and g=n-1. For width w put p=2(w+g). In N consecutive periods of length p take S to be the first w integers of each period, and \(T=S+(w+g)\). Then \(\operatorname{dist}(S,T)=g+1=n\). Set \(A_N=\sum_{s\in S}X_s\), \(B_N=\sum_{t\in T}X_t\). Write
\[
 D_w(t)=\sum_{r=0}^{w-1}e^{irt},\quad t_j=2\pi j/p.
\]
The Fejer-kernel limit gives
\[
 \frac{\operatorname{Var}(A_N)}N\longrightarrow
 V_w=\frac1p\sum_{j=0}^{p-1}f(t_j)|D_w(t_j)|^2,                   \tag{20}
\]
\[
 \frac{\operatorname{Cov}(A_N,B_N)}N\longrightarrow
 C_w=\frac1p\sum_{j=0}^{p-1}(-1)^jf(t_j)|D_w(t_j)|^2.             \tag{21}
\]
To verify the limits, the coefficient polynomial of A_N is
\(D_w(t)\sum_{k=0}^{N-1}e^{ikpt}\). Split the integral into p arcs, substitute theta=pt on each, and apply Fejer approximation to the continuous folded integrand. The shift of B_N contributes \(\exp(i p t/2)=(-1)^j\) at the pth roots. Marginal variances are equal by stationarity.

The union S union T omits exactly 2g residues per period. At every nonzero pth root, its coefficient polynomial equals minus that of the omitted residues. At the root one the spectral weight f(0) is zero. Discrete Parseval therefore gives
\[
                          2V_w+2C_w\le2gM.                     \tag{22}
\]
For fixed g and large w, the j=1 term alone yields
\[
 V_w\ge\frac1p f(2\pi/p)
       \frac{\sin^2(\pi w/p)}{\sin^2(\pi/p)}
       \ge c\,w f\!\left(\frac{\pi}{w+g}\right),                 \tag{23}
\]
with an absolute c>0 once w exceeds g. If the last expression is unbounded along widths, V_w diverges along a subsequence. Equations (22) and Cauchy–Schwarz then give \(C_w/V_w\to-1\). First let N tend to infinity for a fixed w, and then take those widths. Absolute correlations of finite separated sets approach one, proving rho-star(n)=1.

For (17), \(w f_-(\pi/(w+g))\sim w\log4/\log w\to\infty\). This proves (19) independently of Bradley's lag-one theorem. Continuity alone, and even continuity plus ordinary rho-mixing, are therefore insufficient.

The same obstruction proves rho-star(n)=1 at every lag for
\[
                         f(t)=|1-e^{it}|^\alpha,\quad0<\alpha<1,
\]
since the expression in (23) grows like \(w^{1-\alpha}\). At alpha=2 the moving-average example instead has zero coefficients for n>=2. This calculation does not settle all intermediate zero types.

For the opposite sign of the unbounded conjugate, let \(f_+=\exp(-Hv)=1/f_-\) almost everywhere. It grows like log(1/|t|)/log 4, so is integrable and essentially unbounded, and it is bounded below by 1/2. It is ordinary rho-mixing by the same criterion with -v. Proposition 3 proves rho-star(n)=1 at every lag, because otherwise f_+ would be essentially bounded above.

These failures concern essential bounds, not a value assigned at one point.

## 8. Numerical checks and their limits

[code/checks.py](code/checks.py) computes finite-set correlations using Cholesky whitening/SVD and independently using the generalized eigenvalue problem (4). It also computes the periodic Fejer limits (20)–(21). Dependencies are NumPy and SciPy; run python3 code/checks.py. All outputs are in data/.

The 324 finite covariance checks cover white noise, differenced white noise, the AR(1) covariance \(0.7^{|k|}\), the jump density a=0.6, the fractional zero alpha=0.5, and (17). The first five have exact covariance formulas. For (17) only, midpoint FFT quadrature is exploratory. The sets include past/future intervals, even/odd half-line subsets, and alternating blocks, at lags 1,2,4,8,16,32 and sizes 16,64,128.

Finite correlations are lower bounds on rho-star. They cannot certify convergence to zero. The jump density has exact coefficient 0.6 at every lag, but the largest found among these modest matrices decreases from about 0.564 at lag one to 0.239 at lag 32. Likewise the small matrices suggest decay for (17), whose exact coefficients are all one.

The periodic calculation exposes the missed dependence. These are limits of finite-set correlations as the number of periods tends to infinity, justified by (20)–(21), not a claim that a particular finite vector attains the limit:

| Density, width 16,384 | Lag 2 | Lag 8 | Lag 32 |
|---|---:|---:|---:|
| Differenced white noise | <1e-12 | <1e-12 | <1e-12 |
| Fractional zero alpha=0.5 | 0.993029 | 0.976198 | 0.946121 |
| Continuous slow zero (17) | 0.999039 | 0.997060 | 0.991387 |

The numerical root sums agree with the analytic gap argument: for a fixed lag the latter two correlations tend to one as width grows.

Validation in [data/checks.json](data/checks.json) records:

- Maximum SVD/generalized-eigenvalue discrepancy: \(3.34\times10^{-16}\) or less.
- White-noise correlations and differenced-noise lag>=2 correlations: exactly zero.
- Moving-average lag-one singular values checked against \(\cos(\pi/(2L+1))\); largest absolute error below \(4\times10^{-16}\).
- AR Fourier quadrature checked against its exact covariance: error below \(2.3\times10^{-16}\).
- Slow-zero covariance discrepancy between midpoint grids 32,768 and 65,536: about \(1.15\times10^{-7}\). These FFT values are not used in proofs.
- 108 periodic checks; runtime about 0.55 seconds, peak resident memory about 93 MB on this Mac.

All computations use one BLAS thread, inherited nice=15 (lower priority than nice=10), and matrices no larger than 128 by 128. No subagents, publication, or pushes.

The final artifact audit is [data/audit.json](data/audit.json); downloaded source hashes and verified PDF page counts are in [sources/MANIFEST.json](sources/MANIFEST.json).

## 9. Candidate verdicts and the remaining gap

| Candidate or repair | Verdict |
|---|---|
| rho-star-mixing iff continuous strictly positive f | Sufficiency holds; necessity fails by (12). |
| Some rho-star(N)<1 iff f bounded above and below | Sufficiency holds at N=1; necessity fails by (12). |
| rho-star(1)<1 iff f bounded above and below | True, classical; proved in Proposition 2. |
| Some rho-star(N)<1 implies convergence to zero | False: (14) has constant coefficient a in (0,1). |
| Continuity allowing zeros is sufficient | False: (17)–(19). |
| Continuity plus ordinary rho-mixing is sufficient | False: the same example. |
| \(f=|P|^2g\), g continuous strictly positive | Sufficient; necessity not proved. |
| Relative polynomial approximation (11) | Equivalent to this sufficient class; not proved necessary for interlaced mixing. |

What is established for every rho-star-mixing sequence is continuity and the ordinary Helson–Sarason condition. Positive continuous densities and their finite polynomial filters are sufficient. The periodic argument excludes slow zeros and proves exact maximal interlaced dependence for the examples above.

There remains a real gap for densities with zeros. There is no proof here that every admissible zero can be removed by a finite polynomial leaving a continuous strictly positive quotient, and no proof that another stated broader class is equivalent to rho-star-mixing. The operator reformulation is not counted as a solution. The status is PARTIAL, not PROVED or RESOLVED_IN_LITERATURE.

## 10. Exact references and source checks

1. R. C. Bradley, “Basic properties of strong mixing conditions. A survey and some open questions,” *Probability Surveys* **2** (2005), 107–144. DOI [10.1214/154957805100000104](https://doi.org/10.1214/154957805100000104); [arXiv:math/0511078](https://arxiv.org/abs/math/0511078). Full PDF downloaded. Definitions pp. 113–114; Section 6 pp. 127–133; Section 7 pp. 133–135; Question 9 p. 135.
2. R. C. Bradley, “On the spectral density and asymptotic normality of weakly dependent random fields,” *J. Theoret. Probab.* **5** (1992), 355–373. DOI [10.1007/BF01046741](https://doi.org/10.1007/BF01046741). Publisher abstract and metadata read; survey credits Theorem 1 for part of its positive-continuous result. Full paper unavailable.
3. R. C. Bradley, “Equivalent mixing conditions for random fields,” *Ann. Probab.* **21**(4) (1993), 1921–1926. DOI [10.1214/aop/1176989004](https://doi.org/10.1214/aop/1176989004). Theorem 1 and Remarks 1–3 identified via survey Theorem 2.1(2). Euclid access blocked; no direct full-text claim.
4. R. C. Bradley, “On positive spectral density functions,” *Bernoulli* **8**(2) (2002), 175–193; acknowledgement of priority, **8**, 559. MR1895889. Theorems 1.6–1.7 are the source of survey Theorems 6.4–6.5; their statements verified there. Full paper not obtained.
5. R. C. Bradley, “A criterion for a continuous spectral density,” *J. Multivar. Anal.* **86**(1) (2003), 108–125. DOI [10.1016/S0047-259X(02)00044-1](https://doi.org/10.1016/S0047-259X(02)00044-1). Theorem 1.4 / Remark 1.8 identified via survey Theorem 6.3. Publisher abstract checked.
6. R. C. Bradley, *Introduction to Strong Mixing Conditions*, vols. 1–3, Kendrick Press, Heber City, Utah, 2007. ISBNs 0-9740427-6-5, 0-9740427-7-3, 0-9740427-8-1. [Publisher contents](https://kendrick.press/Richard-Bradley-Introduction-to-Strong-Mixing-Conditions.htm) checked: chapters 9, 23, 27–29. Full chapters unavailable.
7. A. N. Kolmogorov and Yu. A. Rozanov, “On strong mixing conditions for stationary Gaussian processes,” *Theory Probab. Appl.* **5**(2) (1960), 204–208. DOI [10.1137/1105018](https://doi.org/10.1137/1105018). Original: *Teor. Veroyatnost. i Primenen.* **5**(2), 222–227. [MathNet record](https://www.mathnet.ru/eng/tvp4828) checked. Theorem 1 for Gaussian linear reduction and Theorem 2 for alpha/rho equivalence are identified via Bradley.
8. H. Helson and D. Sarason, “Past and future,” *Math. Scand.* **21** (1967), 5–16. DOI [10.7146/math.scand.a-10840](https://doi.org/10.7146/math.scand.a-10840). Official scan downloaded; Theorem 5, p. 10, its proof pp. 11–12, and Theorem 6, pp. 14–15, visually read. They concern ordinary past/future angles.
9. H. Helson and G. Szego, “A problem in prediction theory,” *Ann. Mat. Pura Appl.* (4) **51** (1960), 107–138. Lag-one criterion as stated in survey Theorem 6.1. Bibliography also checked in the Helson–Sarason scan.
10. D. Sarason, “An addendum to ‘Past and future’,” *Math. Scand.* **30** (1972), 62–64. Its continuous u,v criterion is restated in Sarason (1975), Section 3, read directly here. Bibliography checked in both Sarason 1975 and Bradley 2005. Addendum itself not obtained.
11. D. Sarason, “Functions of vanishing mean oscillation,” *Trans. Amer. Math. Soc.* **207** (1975), 391–405. DOI [10.1090/S0002-9947-1975-0377518-3](https://doi.org/10.1090/S0002-9947-1975-0377518-3). Publisher PDF downloaded; Section 3, pp. 396–398, read. Its VMO/weight formulation concerns past/future mixing. Simply requiring f itself to be VMO is not an answer: continuous example (17) belongs to ordinary VMO. Bradley's bibliography gives 1974; the publisher PDF and DOI metadata give 1975, used here.
12. I. A. Ibragimov and Yu. A. Rozanov, *Gaussian Random Processes*, Applications of Mathematics **9**, Springer, New York, 1978. DOI [10.1007/978-1-4612-6275-6](https://doi.org/10.1007/978-1-4612-6275-6). Official contents checked, particularly chapters IV–V, pp. 108–190. Full chapters unavailable.
13. V. V. Peller, *Hankel Operators and Their Applications*, Springer, New York, 2003. DOI [10.1007/978-0-387-21681-2](https://doi.org/10.1007/978-0-387-21681-2). Official contents checked, chapters 8–9, pp. 379–429. Full chapters unavailable. Past/future Hankel compactness does not by itself control all interlaced projections.
14. C. C. Moore, “The degree of randomness of a stationary time series,” *Ann. Math. Statist.* **34** (1963), 1253–1258. Theorem 1 identified through survey Theorem 6.4; its lag-one statement is reproved in Proposition 2.
15. C. Miller, “Three theorems on rho-star-mixing random fields,” *J. Theoret. Probab.* **7**(4) (1994), 867–882. DOI [10.1007/BF02214377](https://doi.org/10.1007/BF02214377). Springer renders the title as “Three theorems on rho-star random fields.” Abstract read directly: spectral-density convergence and CLTs, not a claimed Gaussian spectral iff result. Full paper unavailable.
16. M. Rosenblatt, “Central limit theorems for stationary processes,” *Proceedings of the Sixth Berkeley Symposium on Mathematical Statistics and Probability*, vol. 2 (1972), 551–561; and *Stationary Sequences and Random Fields*, Birkhauser, Boston, 1985, pp. 73–74, Theorem 7 and Lemma 2. These are survey references [140] and [142] for the interlaced Gaussian sufficiency. Bibliography verified in the survey; no direct full-text claim.
17. G. Samorodnitsky, “Long Range Dependence,” *Foundations and Trends in Stochastic Systems* **1**(3) (2006), 163–257. DOI [10.1561/0900000004](https://doi.org/10.1561/0900000004). Cornell author PDF read, pp. 187–188. Cover copyright is 2007; volume year is 2006.
18. R. C. Bradley, “On possible mixing rates for some strong mixing conditions for N-tuplewise independent random fields,” *Houston J. Math.* **38**(3) (2012), 815–832; [arXiv:1107.3854](https://arxiv.org/abs/1107.3854), 2011 preprint. Downloaded and screened; not a spectral characterization.
19. R. C. Bradley and C. Tone, “A central limit theorem for non-stationary strongly mixing random fields,” [arXiv:1512.01310](https://arxiv.org/abs/1512.01310), 2015 preprint. Downloaded and screened. No journal theorem number is inferred from the filename.
20. J. T. Shaw, *Spectral densities of discrete and continuous-indexed random fields*, PhD dissertation, Indiana University, August 2005. [IU full text](https://scholarworks.iu.edu/iuswrrest/api/core/bitstreams/f7eae880-4617-4ef7-898a-dcfbe34dbe58/content), downloaded. Read abstract, contents, Theorems 3.1–3.5 (pp. 11–15), proof of 3.3(C)=>(A), and Theorem 4.1 (p. 22). Theorems 3.3–3.4 independently confirm Bradley's lag-one-qualified criteria; the continuous-index result does not resolve Question 9. The PDF has 62 pages; an initial quick file-summary page count was wrong and was corrected using a PDF parser and the full extracted text.

Task: “Open problem D0037.” Received 13 November 2026, approximately 05:31 Asia/Tbilisi.
