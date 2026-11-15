MINOR

The four numbered results in `claim_files/REPORT.md` are correct for Bradley's **linear** coefficient $r^*(n)$. I found no false inequality, invalid use of interlacing, missing boundary case within the stated power-asymptotic class, or incorrect normalization in the two examples. This is a valid partial result, not a solution of D0036. The minor verdict concerns the missing source package and incomplete literature verification, not the proofs. No mathematical novelty is established: the power-zero obstruction follows from classical past/future theory, finite filtering gives sufficiency, and differenced white noise is elementary. I did not locate the exact finite-zero theorem or the exact cusp bound in print.

There is a useful strengthening: for the claimed cusp density, actually $r(n)=r^*(n)=1$ for **every** $n$. I give explicit witnesses below. The claimed lower bound $1/2$ is therefore true but far from sharp.

The errors and gaps found are:

1. **Missing supporting files.** Locations: claim report lines 28, 340 and 352, and its references to `sources/`. There is no `claim_files/sources/` in the supplied package, although the report cites a full Bradley text, literature ledger, and raw search record there. `claim_files/data/plaintext_source_sha256.txt` does not substitute for the missing texts. Fix: supply the source package or remove the assertions that it is attached. I independently fetched the principal accessible texts into this audit's `sources/`.
2. **Publication status remains unverified.** Locations: claim report lines 3–8 and 338–361. The important chapters of Bradley's three volumes, Peller's 2003 book, and several original articles were not inspected in full. The report acknowledges this, correctly; consequently neither “Question 8 is still open in 2026” nor “these partial statements are new” is an established result. Fix: retain the qualified wording and obtain direct chapter/theorem evidence before making either stronger assertion. My independent search also leaves this access gap. The newly located Hallin–Tran 1996 example should be added when discussing prior work on non-integer powers.

There are no further proof errors to list in statements (1)–(4). Absence of explicit non-even-power test arrays in the claimant's proof is not a logical gap: its classical-factorization contradiction is sufficient. I supply arrays because the referee request explicitly asks for them. The weak cusp bound is an opportunity to improve the result, not an error.

**Source and definitions.** The full independently downloaded arXiv text is [sources/bradley_2005.txt](sources/bradley_2005.txt). The requested statements, extracted verbatim from that download, are in [sources/bradley_requested_statements.txt](sources/bradley_requested_statements.txt). Their locations are journal p.130 for Theorem 6.2, p.131 for Theorems 6.3–6.5, and p.132 for Question 8. Source retrieval streamed PDF bytes through `pdftotext` using pipes; no PDF or page image was written. The mathematical formulations, preserving all hypotheses and conjunctions, are as follows. [Bradley 2005](https://arxiv.org/abs/math/0511078).

Here CCWS means centered, complex, weakly stationary, with finite second moments. Theorems 6.2 and 6.3 apply to any CCWS sequence; Theorems 6.4 and 6.5 assume it is nondegenerate. The circle carries normalized Lebesgue measure $dm(t)=dt/(2\pi)$. A tilde denotes the harmonic conjugate.

- **Theorem 6.2:** $r(n)\to0$ is equivalent to the existence of a spectral density
  \[
  f=|p|^2\exp(u+\widetilde v),
  \]
  with $p$ a polynomial and $u,v$ continuous real functions on the circle.
- **Theorem 6.3:** these three assertions are equivalent: existence of a continuous spectral density; $\zeta(n)\to0$; $\kappa(n)\to0$.
- **Theorem 6.4:** these three assertions are equivalent: existence of a spectral density bounded between two positive constants, without a continuity requirement; $r^*(1)<1$; $r(1)<1$ together with $r^*(N)<1$ for some integer $N\ge1$.
- **Theorem 6.5:** these four assertions are equivalent: existence of a continuous density positive at every point of the circle; $r^*(1)<1$ together with $r^*(n)\to0$; $r(1)<1$ together with $r^*(n)\to0$; $r(1)<1$, $r^*(N)<1$ for some integer $N\ge1$, and $\zeta(n)\to0$.

Question 8 reads: “What condition on a spectral density function is necessary and sufficient for a CCWS random sequence to satisfy $r^*(n)\to0$ as $n\to\infty$?” The exact extracted source statements above also preserve the original wording of all four theorems.

Bradley's equations (6.3), (6.5), and (6.7), pp.128–129, give
\[
 r_f^*(n)=\sup_{\operatorname{dist}(S,T)\ge n}
 \frac{\left|\int A\overline B f\,dm\right|}
 {\left(\int|A|^2f\,dm\right)^{1/2}
  \left(\int|B|^2f\,dm\right)^{1/2}},
 \quad A(z)=\sum_{s\in S}a_sz^s,\quad B(z)=\sum_{t\in T}b_tz^t.
\]
Both sets are nonempty and finite, arbitrary apart from
$\operatorname{dist}(S,T)=\min_{s,t}|s-t|\ge n$. They can alternate any number of times. Their coefficient arrays are independently arbitrary complex arrays; Bradley uses a single array on the disjoint union, which is equivalent. The convention for a zero denominator is zero. Taking closed **complex linear spans** changes no supremum: approximate two nonzero vectors by finite combinations and pass to the normalized inner product. Passing from finite to arbitrary index sets likewise changes nothing after finite approximation. The past/future coefficient $r(n)$ restricts the sets to opposite half-lines.

The Hermitian covariance is
\[
 \gamma(k)=E[X_k\overline{X_0}],\qquad
 E\left[\sum a_sX_s\;\overline{\sum b_tX_t}\right]
 =\sum_{s,t}a_s\overline{b_t}\gamma$s-t$
 =\int A\overline B f\,dm.
\]
Overbars are sometimes lost in text extraction; they must be restored as here. The claimant's definitions, lines 21–26, match these definitions exactly.

The task's use of the symbol $\rho^*$ needs this qualification. Bradley's $\rho^*$ in Section 2 maximizes over arbitrary square-integrable measurable functions of the variables, not just linear combinations. It equals $r^*$ for centered stationary real Gaussian sequences, by (7.1), but need not do so for general second-order sequences. A simple counterexample to any literal nonlinear version of sufficiency is $X_k=Z\varepsilon_k$, where independent symmetric signs $\varepsilon_k$ are independent of a positive nonconstant $Z\in\{1,2\}$. Its spectral density is the positive constant $E Z^2$, whereas $|X_k|=Z$ gives $\rho^*(n)=1$ at every gap. The actual claimant report expressly uses $r^*$, so this is not a fault in that report.

**Line-by-line sufficiency audit.** Claim report lines 80–96 define $E_j(g)$ as best uniform approximation by trigonometric polynomials of degree at most $j$, with $m_0=\min g>0$. These details matter: the approximation must allow negative Fourier exponents. For each term of $A\overline B$, the exponent is $s-t$, whose absolute value is at least $n$. Multiplication by any degree-$(n-1)$ trigonometric polynomial $q$ cannot create exponent zero. Thus
\[
 \int A\overline Bq\,dm=0.
\]
Subtracting $q$, applying the supremum norm bound, and then ordinary Cauchy–Schwarz gives
\[
 |\langle A,B\rangle_g|
 \le\|g-q\|_\infty\|A\|_2\|B\|_2
 \le \frac{\|g-q\|_\infty}{m_0}\|A\|_g\|B\|_g.
\]
There are two square-root lower bounds in the last step, whose product is $m_0$; no square or factor two is missing. Infimizing over $q$ and taking the supremum over arrays proves
\[
 r_g^*(n)\le\min\{1,E_{n-1}(g)/m_0\}.
\]
Uniform trigonometric approximation makes the right-hand approximation term tend to zero. No assumption about the cardinalities or the ordering of the two sets was used.

For lines 98–116 put $P(z)=\sum_{j=0}^dp_jz^j\ne0$. Multiplication is an isometry from polynomial tests in $L^2(|P|^2g)$ to their images in $L^2(g)$:
\[
 \langle A,B\rangle_{|P|^2g}=\langle PA,PB\rangle_g,
 \qquad \|A\|_{|P|^2g}=\|PA\|_g.
\]
For any potentially nonzero exponents $s+i,t+j$ in those two images,
\[
 |(s+i)-(t+j)|\ge |s-t|-|i-j|\ge n-d,
 \qquad 0\le i,j\le d.
\]
This is the precise interlacing check. The loss is $d$, not $2d$, because $i-j\in[-d,d]$. Internal overlaps or cancellations within either enlarged support cause no difficulty. When $n>d$, the two enlarged supports are disjoint and admissible at gap $n-d\ge1$. Surjectivity onto all $g$-tests is unnecessary for this upper bound. Consequently
\[
 \boxed{\quad r_{|P|^2g}^*(n)
 \le r_g^*(n-d)
 \le \min\left\{1,\frac{E_{n-d-1}(g)}{\min g}\right\},\qquad n>d.\quad}
\]
The index $n-d-1$ is correct, including at $n=d+1$. For $n\le d$ use the trivial bound 1. For a Laurent polynomial the effective $d$ is the width of its exponent support after removing a monomial. Circle roots are allowed; off-circle roots can be absorbed into $g$. The zero polynomial gives the trivial zero sequence, which is separately excluded in the displayed nonzero factorization.

The report's additional AR bound (14) is also correct for its $0<a<1$ convention. The Fourier tail of $g=(1-a^2)/|1-az|^2$, cut at degree $n-d-1$, is at most $2a^{n-d}/(1-a)$, and $\min g=(1-a)/(1+a)$. Their quotient is $2(1+a)a^{n-d}/(1-a)^2$, with an optional cap at 1.

I also checked the auxiliary continuous-density necessity in lines 43–76. The random-split identity is correct. It gives the two-sided coefficient norm bounds on $N$-spaced sets with constants $(1\pm r^*(N))/(1\mp r^*(N))$. Partition into residue classes modulo $N$ gives the claimed upper bound with the factor $N$. It does not give a global lower bound. Dominating the spectral measure by $M\,m$ and then using $\kappa(n)\le M r^*(n)$ is legitimate; Theorem 6.3 supplies continuity. There is no hidden proof here of the still-missing global converse.

**Power zeros: both directions.** The precise hypotheses are those in claim report lines 120–126: $f\not\equiv0$ is continuous, its zero set is finite, and at each zero
\[
 f(e^{i(\theta_j+t)})=c_j|t|^{\beta_j}(1+o(1)),
 \qquad c_j>0,\quad 0<\beta_j<\infty,
\]
with the same limiting constant from both sides. The exact theorem is correct.

For necessity, the report uses Theorem 6.2 only after observing $r(n)\le r^*(n)$. The logarithms in line 139 are integrable under the hypotheses. The estimate for $Q_r$ in lines 148–155 follows from $1-2r\cos t+r^2=(1-r)^2+2r(1-\cos t)$. Subtracting the value of continuous $v$ at the chosen zero bounds the near contribution by an arbitrarily small constant times $\log(1/(1-r))$; the contribution outside a fixed neighborhood is bounded. Thus
\[
 Q_r*v(\theta_j)=o\bigl(\log(1/(1-r))\bigr).
\]
If the factor polynomial has multiplicity $m_j$ there, the remaining logarithm is
$(\beta_j-2m_j)\log|t|+C+o(1)$. Its radial Poisson mean equals
\[
 (\beta_j-2m_j)\log(1-r)+O(1),
\]
since the Poisson extension of $\log|1-e^{it}|$ is $\log|1-re^{i\theta}|$. Away from the chosen zero the Poisson kernel is $O(1-r)$; integrable singularities at other polynomial roots therefore contribute no divergent term. Comparing the two estimates forces $\beta_j=2m_j$. No unjustified boundary value of a harmonic conjugate is used. This proof is sound.

As a second check, [Peller 1998, Theorem 10.1, p.95](https://library.slmath.org/books/Book33/files/peller.pdf) states the past/future criterion as $f=|p|^2e^\varphi$, with real $\varphi\in\mathrm{VMO}$. On $(\delta,2\delta)$, a residual $a\log t+C+o(1)$, $a\ne0$, has mean oscillation tending to
\[
 |a|\int_1^2|\log x-(2\log2-1)|\,dx
 =|a|(8/e-4\log2)>0.
\]
It cannot be VMO. This independently confirms the exponent conclusion. The claim correctly avoids the misleading sentence following Bradley's Theorem 6.2 that mentions VMO of $f$ itself: the relevant object is the logarithm after removing a polynomial factor.

For sufficiency let all $\beta_j=2m_j$ and set $P(z)=\prod_j(z-e^{i\theta_j})^{m_j}$. At the $j$-th zero the quotient extends with the value
\[
 g(e^{i\theta_j})=
 \frac{c_j}{\prod_{\ell\ne j}|e^{i\theta_j}-e^{i\theta_\ell}|^{2m_\ell}}>0.
\]
The chord-to-angle ratio tends to 1. The two-sided asymptotic supplies the same quotient limit from both sides, so the extension is continuous. Away from the finite zero set it is continuous and positive. Compactness then gives $\min g>0$, and the preceding sufficiency proof applies.

This deals with several zeros, including a zero at the chosen angular cut of the circle. There is no uniform assertion as $\beta_j$ approaches an even integer: the nonmixing lower bound may become arbitrarily small. At an exact positive even integer the obstruction vanishes. The zero-free case uses $P=1$. A putative zero with $\beta=0,c>0$ contradicts continuity; infinite-order zeros and nonconvergent or unequal one-sided quotients are outside the theorem. Replacing asymptotic equivalence by two-sided comparability would invalidate the quotient-extension step; the report explicitly does not do that.

In fact the proof yields, in this restricted class,
\[
 r(n)\to0\quad\Longleftrightarrow\quad r^*(n)\to0
 \quad\Longleftrightarrow\quad \text{all zero exponents are positive even integers}.
\]
Thus the necessity here already belongs to the weaker, classical past/future problem.

**Explicit test arrays for every non-even exponent.** Here is an independent construction, which does not invoke the factorization theorem. Fix one zero $\theta_0$ with exponent $\beta>0$ not an even integer. Define
\[
 \phi(x)=\begin{cases}\exp\bigl(4-1/(x(1-x))\bigr),&0<x<1,\\0,&\text{otherwise},\end{cases}
 \qquad \psi(x)=\phi(x-2).
\]
For integer $L\to\infty$ use finite arrays
\[
 a_k^{(L)}=e^{-ik\theta_0}\phi(k/L),\qquad
 b_k^{(L)}=e^{-ik\theta_0}\psi(k/L).
\]
Their supports are $S_L=\{1,\ldots,L-1\}$ and $T_L=\{2L+1,\ldots,3L-1\}$, at distance $L+2$. They are admissible for any prescribed gap $n$ once $L+2\ge n$, even for the ordered coefficient $r(n)$ after translation.

Use the transform $\widehat\phi(u)=\int\phi(x)e^{iux}\,dx$. Riemann sums give
\[
 L^{-1}A_L(e^{i(\theta_0+u/L)})\to\widehat\phi(u),
 \qquad L^{-1}B_L(e^{i(\theta_0+u/L)})\to\widehat\psi(u).
\]
Repeated discrete summation by parts gives, for every integer $M$, a bound $C_M(1+|u|)^{-M}$ for these normalized polynomials on $|u|\le\pi L$. Smooth compact support is essential here. Near the zero, $L^\beta f(e^{i(\theta_0+u/L)})\le C|u|^\beta$; outside a fixed neighborhood the same bound follows from boundedness of $f$ and $|u|\ge\delta L$. Dominated convergence therefore proves
\[
 L^{\beta-1}\|A_L\|_f^2\to cD_\beta,
 \quad L^{\beta-1}\|B_L\|_f^2\to cD_\beta,
 \quad L^{\beta-1}\langle A_L,B_L\rangle_f\to cI_\beta,
\]
where
\[
 D_\beta=\frac1{2\pi}\int_{\mathbb R}|u|^\beta|\widehat\phi(u)|^2\,du>0,
 \qquad I_\beta=\frac1{2\pi}\int_{\mathbb R}|u|^\beta\widehat\phi(u)\overline{\widehat\psi(u)}\,du.
\]
The inverse Fourier transform of $|u|^\beta$, away from the origin, is
\[
 C_\beta|x|^{-1-\beta},\qquad
 C_\beta=-\frac{\Gamma(\beta+1)\sin(\pi\beta/2)}{\pi}.
\]
For example this follows by inserting $e^{-\varepsilon|u|}$, evaluating the Laplace integral, and letting $\varepsilon\downarrow0$ away from zero. Applying the distribution to the cross-correlation of the two smooth bumps is legitimate: that cross-correlation is supported away from zero. Consequently
\[
 I_\beta=C_\beta\int_0^1\int_2^3
 \frac{\phi(x)\psi(y)}{|x-y|^{1+\beta}}\,dy\,dx\ne0.
\]
The double integral is strictly positive and finite, and $C_\beta\ne0$ precisely when $\beta$ is not an even integer. It follows that
\[
 \boxed{\quad r_f^*(n)\ge r_f(n)\ge |I_\beta|/D_\beta>0
 \quad\text{for every }n\ge1.\quad}
\]
The constant depends on $\beta$; it is not claimed uniform near even integers. Other zeros are harmless because modulation isolates $\theta_0$ and the smooth arrays suppress the rest of the spectrum. Odd exponents are included without an exceptional case. The code tests this construction; at $\beta=2,4$ the far-block covariance is exactly zero.

**The cusp and the difference example.** For $f(e^{it})=(\pi/4)|1-e^{it}|$, independent Fourier integration gives
\[
 \gamma(k)=\frac12\int_0^\pi\sin(t/2)\cos(kt)\,dt
 =\frac1{1-4k^2}.
\]
In particular $\gamma(0)=1$. The function is continuous, Lipschitz, and positive except at 0. Since
\[
 \sum_{k=1}^{\infty}\frac1{4k^2-1}=\frac12,
\]
its covariance sequence has absolute sum 2 and signed sum 0.

Writing $V(L)=\operatorname{Var}(X_1+\cdots+X_L)$, I checked both the covariance sum and its first difference:
\[
 V(L)=L+2\sum_{h=1}^{L-1}\frac{L-h}{1-4h^2}
 =\sum_{j=1}^L\frac1{2j-1}
 =\tfrac12\log L+O(1),
 \qquad V(L+1)-V(L)=\frac1{2L+1}.
\]
For adjacent equal blocks the covariance is $(V(2L)-2V(L))/2$, hence correlation tends to $-1/2$. At any fixed gap $n$, shifting the second block changes at most $2(n-1)$ variables. Its $L^2$ difference norm is at most $2(n-1)$, because $\|X_k\|_2=1$. Dividing the resulting covariance error by $V(L)$ gives at most $2(n-1)/\sqrt{V(L)}\to0$. Thus the claimant's $r^*(n)\ge1/2$ holds for every fixed $n$, with the stated normalization.

A stronger witness uses
\[
 U_L=\sum_{k=-L+1}^{0}(1+k/L)X_k,\qquad
 W_{L,1}=\sum_{k=1}^{L}(1-(k-1)/L)X_k.
\]
These are disjoint triangular tapers, with equal variance $v_L$. For any finitely supported real array $a$, absolute summability and $\sum_h\gamma(h)=0$ give the exact identity
\[
 \operatorname{Var}\Bigl(\sum a_kX_k\Bigr)
 =\sum_{h=1}^{\infty}\frac1{4h^2-1}
   \sum_{k\in\mathbb Z}(a_{k+h}-a_k)^2.
\]
For either taper and $1\le h\le L/2$, the inner sum is at least $h/4$, by considering shifts across its height-one endpoint. Hence $v_L\ge(1/16)\sum_{h\le L/2}1/h\to\infty$.

The coefficient polynomial of $U_L+W_{L,1}$ is, up to a monomial factor,
\[
 L^{-1}D_L(z)D_{L+1}(z),\qquad D_j(z)=1+z+\cdots+z^{j-1}.
\]
Its modulus is at most $C\min\{L,(L|t|^2)^{-1}\}$ on $|t|\le\pi$. Since $f(e^{it})\le C|t|$, splitting its variance integral at $1/L$ bounds $\|U_L+W_{L,1}\|_2$ uniformly in $L$. Shift the second taper right by $n-1$ to obtain $W_{L,n}$. The coefficient array of the shift difference has $\ell^1$ norm at most $2(n-1)$, so $\|W_{L,n}-W_{L,1}\|_2\le2(n-1)$. Therefore $\|U_L+W_{L,n}\|_2$ stays bounded for each fixed $n$, whereas each separate variance tends to infinity. It follows that
\[
 \operatorname{Corr}(U_L,W_{L,n})
 =\frac{\operatorname{Var}(U_L+W_{L,n})-2v_L}{2v_L}\to-1.
\]
Their support distance is exactly $n$. This proves $r(n)=r^*(n)=1$ at every gap. No literature-priority claim is made for this strengthening.

For $X_k=Y_k-Y_{k-1}$ with orthogonal variance-one white noise,
\[
 f=|1-z|^2,\quad \gamma(0)=2,\quad\gamma(\pm1)=-1,
 \quad\gamma(h)=0\quad(|h|\ge2).
\]
Every cross covariance between gap-2 sets is zero, including arbitrarily interlaced sets. At gap 1 take equal-weight even and odd sets of size $L$: both variances are $2L$, and their covariance is $-(2L-1)$, since exactly $2L-1$ adjacent cross pairs occur. Their absolute correlation is $1-1/(2L)\to1$. Thus $r^*(1)=1$ and $r^*(n)=0$ for $n\ge2$. Every finite covariance matrix remains positive definite, as $f>0$ almost everywhere. The claimant's distinction between finite nonsingularity and a limiting correlation supremum is correct.

**Independent computation.** [code/independent_audit.py](code/independent_audit.py) was written from scratch. I did not import, copy, or run anything in `claim_files/code/`. The numerical evidence uses analytic Toeplitz covariance blocks for all canonical correlations. For $f_\beta=|1-e^{it}|^\beta$ normalized to variance one, I use
\[
 c_0=1,\qquad c_k=c_{k-1}\frac{k-1-\beta/2}{k+\beta/2},\quad k\ge1,
 \qquad c_{-k}=c_k.
\]
Direct numerical integration of the density checks this recurrence independently. Additional models are $|1-z|^2|1+z|^\beta$, with zeros at 0 and $\pi$, and $|1-z|^2g_{0.7}$. Their covariances are obtained by the finite second-difference filter applied to the underlying analytic covariance sequences.

For support sets $S,T$, put $A=C_{SS}, B=C_{TT}, C=C_{ST}$. I solve the generalized **Hermitian** eigenproblem
\[
 \begin{pmatrix}0&C\\C^*&0\end{pmatrix}v
 =\lambda\begin{pmatrix}A&0\\0&B\end{pmatrix}v.
\]
Its largest eigenvalue is the largest canonical correlation. An independent Cholesky/SVD calculation checks selected values. A modulated, non-even density tests complex conjugation and Hermitian rather than plain-transpose conventions. Positive definite within-set blocks are used without regularization, eigenvalue clipping, or pseudoinverses. Small within-set eigenvalues and generalized eigenvector residuals are retained with each result.

The 840 calculations cover windows 64, 128, 256; gaps 1, 2, 4, 8, 16; ordered blocks and genuinely alternating runs of widths 1, 4, 16, separated by unused gap sites; and exponents $0.2,0.5,1,1.9,2,2.1,3,3.9,4,4.1$. The last three models above add checks with several zeros and a positive nonconstant quotient. The table gives maxima over these **sampled families** at window 256, not over all subsets and not an estimate with a proved error bound for the infinite supremum.

| Density, up to scale | Gap 1 | Gap 2 | Gap 4 | Gap 8 | Gap 16 |
|---|---:|---:|---:|---:|---:|
| $\lvert1-z\rvert^{0.5}$ | .885715 | .539309 | .383035 | .251759 | .192866 |
| $\lvert1-z\rvert$, the cusp | .991013 | .530912 | .372160 | .278255 | .194646 |
| $\lvert1-z\rvert^{1.9}$ | .999882 | .076118 | .045937 | .029560 | .017488 |
| $\lvert1-z\rvert^2$ | .999925 | 0 | 0 | 0 | 0 |
| $\lvert1-z\rvert^{2.1}$ | .999953 | .077957 | .044034 | .027338 | .015570 |
| $\lvert1-z\rvert^3$ | .999999 | .701682 | .243165 | .126605 | .060500 |
| $\lvert1-z\rvert^{3.9}$ | 1.000000 | .959569 | .035426 | .014972 | .005954 |
| $\lvert1-z\rvert^4$ | 1.000000 | .969350 | 0 | 0 | 0 |
| $\lvert1-z\rvert^{4.1}$ | 1.000000 | .976976 | .035269 | .014145 | .005393 |
| $\lvert1-z\rvert^2\lvert1+z\rvert$ | .999544 | .987205 | .417393 | .295633 | .202461 |
| $\lvert1-z\rvert^2\lvert1+z\rvert^2$ | .999407 | .999703 | 0 | 0 | 0 |
| $\lvert1-z\rvert^2g_{0.7}$ | .997691 | .693717 | .338959 | .081028 | .004629 |

Rounded entries of 1 are not exact finite-window correlations of 1. The complete results, including the other exponents, are [data/canonical_correlations.csv](data/canonical_correlations.csv) and [data/sampled_maxima.csv](data/sampled_maxima.csv). Values below $1/2$ for the cusp at a large gap are consistent with both the claimant's bound and my stronger bound: fixed windows miss long test arrays. None of the falling rows proves mixing. In particular, exponents 1.9 and 2.1 can look numerically nearly mixed while their infinite coefficients stay bounded away from zero.

Separate files follow the flat cusp block witnesses to length 524288, the tapered cusp witnesses to length 32768, and the smooth power witnesses to scale 8192. For example, at gap 8 the tapered cusp absolute correlations at $L=8192,32768$ are approximately .49554 and .55375, and their sum variances stay near 2.65 while their individual variances grow. The proof, rather than this slow numerical increase, gives the limit 1.

For the smooth witnesses, positive FFT spectral quadrature evaluates norms without catastrophic cancellation. Their cross covariances use the exact analytic covariance recurrence and an FFT convolution of the bump weights, summed only over distant lags of a fixed sign. This avoids a noticeable low-frequency quadrature bias at small $\beta$, discovered by checking the continuum kernel formula. The raw spectral cross discrepancies are retained. [code/check_limits.py](code/check_limits.py) independently integrates the separated-bump kernel using Gauss–Legendre quadrature. At $L=8192$, the largest absolute discrepancy in the predicted versus observed scaled cross covariance is $2.03\times10^{-10}$; the non-even cross covariances are nonzero, and those for 2 and 4 are zero. Norm quadrature and all floating-point calculations remain numerical evidence, not certified bounds.

The main run made 114 numerical checks: Fourier quadrature, generalized eigenvalues versus Cholesky/SVD, complex modulation invariance, cusp variance identities, and the exact differenced-white-noise checkerboard formula $\cos(\pi/(W+1))$. The largest check discrepancy was $2.64\times10^{-12}$; the largest generalized eigenvector residual was $1.22\times10^{-12}$. Final stderr is empty. The run inherited nice 10, set numerical thread counts to one, took 6.69 seconds, and recorded peak RSS 1,538,342,912 bytes, below 4 GB. See [data/run_metadata.json](data/run_metadata.json), [data/checks.csv](data/checks.csv), and [data/kernel_limit_checks.csv](data/kernel_limit_checks.csv).

Reproduction, from a shell already at nice 10 or lower priority:

```sh
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 python3 code/independent_audit.py
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 python3 code/check_limits.py
```

**Literature result and value.** I searched using the question number and variants of interlaced, rho-star, $r^*$, spectral characterization, polynomial factors, and power zeros, with the requested authors and later dates through 2026-11-13. The primary-source reading and access limitations are recorded in [sources/LITERATURE_LEDGER.txt](sources/LITERATURE_LEDGER.txt). This is not a claim that every 1992–2026 paper has been inspected.

| Source | What was actually checked | Consequence for this claim |
|---|---|---|
| Bradley 1992, J. Theor. Probab. 5, 355–373 | Publisher abstract; Theorem 1 identified through Bradley 2005 p.131 | Continuous-positive characterization is classical; no original full-text zero-set theorem was verified. [Publisher](https://link.springer.com/article/10.1007/BF01046741). |
| Bradley 2002, Bernoulli 8, 175–193, with priority acknowledgement p.559; Bradley 2003, J. Multivar. Anal. 86, 108–125 | Theorems 1.6–1.7 of 2002 and Theorem 1.4/Remark 1.8 of 2003 checked via Bradley's own 2005 survey, pp.129–131; Euclid full-text request returned only an access page | These give Theorems 6.3–6.5, not the unqualified converse sought in Question 8. Do not infer a new characterization from their titles. [2002](https://projecteuclid.org/euclid.bj/1078866866), [2003](https://doi.org/10.1016/S0047-259X(02)00044-1). |
| Bradley 2007, all three volumes | Publisher contents: vol.1 ch.8, vol.2 ch.23, vol.3 chs.27–28; full chapters unavailable | Major remaining verification gap. A table of contents cannot settle whether a later formulation answers Question 8. [Publisher](https://kendrick.press/Richard-Bradley-Introduction-to-Strong-Mixing-Conditions.htm). |
| Bradley, Philipp-volume paper | Downloaded text, Remark 1.5(g), p.6; Remark 1.15, pp.12–13 | Refers to vol.3 Theorems 25.47 and 28.38 for Gaussian continuous-positive sufficiency and to ch.28 for linear spectral theory; the inspected discussion does not resolve the general zero problem. [Author text](https://www.stat.tugraz.at/philipp_volume/bradley.pdf). |
| Bradley 2014, *On Mixing Properties of Reversible Markov Chains*; Bradley 2025, ALEA 22, 657–694 | 2014 full arXiv text; 2025 abstract/introduction through publisher-hosted text | Markov-chain separation and CLT results, respectively, not spectral-density characterizations of $r^*$ for arbitrary CCWS sequences. A Markov transition-operator spectral gap is a different object from the scalar covariance spectral density. [2014](https://arxiv.org/abs/1403.4895), [2025](https://alea.impa.br/articles/v22/22-26.pdf). |
| Helson–Sarason 1967, *Past and Future*, Math. Scand. 21, 5–16; Sarason 1972, *An addendum to “Past and Future”*, Math. Scand. 30, 62–64 | Journal metadata; precise theorem content confirmed through Bradley 6.2 and Peller 10.1; original article text not available in usable form | The classical past/future characterization already supplies the necessity behind (2). It does not by itself characterize interlaced mixing. [Journal](https://journals.msp.org/mscand/article/view/2485). |
| Sarason, *Functions of vanishing mean oscillation*, Trans. AMS 207 (1975), 391–405; Peller–Khrushchev 1982, Russian Math. Surveys 37(1), 61–144 | Publication data/indexed primary material; direct PDF requests failed; classical formulation independently checked in Peller 1998 | VMO must be applied to the residual logarithm. The survey's bibliography says 1974 for Sarason; the published volume is 1975. [Sarason DOI](https://doi.org/10.1090/S0002-9947-1975-0377518-3), [1982](https://doi.org/10.1070/RM1982v037n01ABEH003192). |
| Peller 1998, *An Excursion into the Theory of Hankel Operators*, MSRI Publ.33, 65–120 | Full downloaded text, §10, pp.94–99; Theorem 10.1 p.95 and its proof | Explicitly works with the past and future half-line subspaces. The VMO factorization is old and does not answer Question 8. [Full text](https://library.slmath.org/books/Book33/files/peller.pdf). |
| Peller 2003, *Hankel Operators and Their Applications* | Publisher contents; ch.8 pp.379–413 and ch.9 pp.415–429; full chapters subscription-only | Relevant book coverage verified, but not a direct full-chapter exclusion of an interlaced characterization. The accessible 1998 theorem is the verified basis for the mathematical audit. [Book](https://link.springer.com/book/10.1007/978-0-387-21681-2). |
| Kolmogorov–Rozanov 1960; Ibragimov–Rozanov 1978, *Gaussian Random Processes* | Original publisher/index abstracts and book contents; Bradley §7 verifies the Gaussian equalities and classical attributions | Past/future mixing, Gaussian linear/nonlinear equality, and continuous-positive sufficiency are classical. Relevant book chapters IV–V were not read in full. [1960](https://doi.org/10.1137/1105018), [1978 book](https://link.springer.com/book/10.1007/978-1-4612-6275-6). |
| Miller 1994, *Three theorems on rho-star random fields*, J. Theor. Probab. 7, 867–882; Peligrad's related interlaced limit theory | Miller publisher abstract and Bradley survey p.132; Peligrad attributions in Bradley and Samorodnitsky, not a full inspection of every Peligrad paper | Spectral convergence and limit theorems are relevant consequences of mixing. The material checked gives no necessary-and-sufficient zero-set criterion. [Miller](https://link.springer.com/article/10.1007/BF02214377). |
| Hallin–Tran 1996, *Kernel density estimation for linear processes*, Ann. Inst. Statist. Math. 48, 429–449 | Downloaded full text, p.432 | Explicitly prints a Gaussian linear process with transfer $(1-z)^p$, noninteger $p>5$, and says it is not strongly mixing by Helson–Sarason. This is a printed special case of the non-even-power obstruction; it also shows that rapid covariance decay is no cure. It is not the exact multi-zero theorem or the cusp $\beta=1$ calculation. [Full text](https://www.ism.ac.jp/editsec/aism/pdf/048_3_0429.pdf). |
| Samorodnitsky, *Long Range Dependence*, §4, manuscript p.22 | Downloaded full text | Explicitly observes that an explicit interlaced Gaussian characterization had not been stated at that time. This corroborates historical status only, not status in 2026. [Author text](https://people.orie.cornell.edu/gennady/techreports/LRD-NOW.pdf). |

The literature conclusion is therefore limited but definite: I found no verified published resolution of Question 8 in the inspected sources, and no verified publication of the exact statements (2) or (3). The central obstruction in (2) is classical and has explicit printed special cases. The exact theorem's being absent from this search does not establish novelty. The simple finite-filter proof of (1) and the difference example (4) should be presented as consequences/examples, as the claimant already does. The explicit quantitative cusp calculation is useful exposition; its priority remains unverified.

What remains unproved **in the claim and this audit** is whether every nonzero CCWS sequence with $r^*(n)\to0$ admits
\[
 f=|P|^2g,\qquad g\in C(\mathbb T),\qquad\min g>0,
\]
or whether some more general spectral condition is required. Known necessary facts here are a continuous density, positivity almost everywhere, and the Helson–Sarason residual-logarithm factorization; they do not furnish the displayed stronger quotient regularity. Infinite zero sets, infinite-order zeros, and nonconvergent quotients at finite zeros are not settled by (2). These omissions are not counterexamples, and the converse could also fail. I cannot promote “unproved here” to a certified assertion about the whole published literature through 2026.

The exact accepted mathematical contribution is the displayed uniform sufficiency bound, its finite-power-zero equivalence (also equivalent to past/future decay in that class), the verified cusp counterexample to weaker smoothness/covariance conditions, and the exact differenced-white-noise coefficients. It is correct partial work with modest expository value and no established research priority. It does not close D0036.

Task: “independent referee … open problem D0036 … Break it if it is wrong … Write REPORT.md” — received 2026-11-13, approximately 10:40 +04.
