# Balance indices of the critical beta-splitting tree

Research task: 12 November 2026, approximately 23:06 Asia/Tbilisi.

All logarithms in this report are natural. Write $L=\log n$, $z=\zeta(2)=\pi^2/6$, and

\[
 \nu(dx)=\frac{dx}{2x(1-x)},\qquad
 H(x)=-x\log x-(1-x)\log(1-x).
\]

## 1. Results and their status

The following statements are proved below from the specified splitting law.

\[
\begin{aligned}
 \mathbb ES_n&=\frac{nL^2}{2z}+b nL+O(n),\\
 \mathbb EC_n&=\frac{nL^2}{2z}+
       \left(b-\frac{2\log2}{z}\right)nL+O(n),\\
 \mathbb E QC_n&\sim n^2L,
 \qquad b=\frac\gamma z+\frac{\zeta(3)}{z^2},                 \tag{1}
\end{aligned}
\]

\[
 \operatorname{Var}S_n\sim\operatorname{Var}C_n
 \sim\kappa n^2L^2,\qquad
 \kappa=\frac{2\zeta(3)-z}{z^2}
 =0.280574126406891865\ldots,                              \tag{2}
\]

\[
 \operatorname{Var}QC_n\sim\frac2{11}n^4L^2.              \tag{3}
\]

There is a nonnegative, nondegenerate random variable $Q$ such that

\[
 \frac{QC_n}{n^2\log n}\ \xrightarrow{d}\ Q,
\]

with convergence of every positive integer moment. Its moments determine its law uniquely and are specified in (24). In particular,

\[
 \mathbb EQ=1,\quad \mathbb EQ^2=\frac{13}{11},\quad
 \mathbb EQ^3=\frac{2457}{1507},\quad
 \mathbb EQ^4=\frac{5188313}{2005817}.                     \tag{4}
\]

The standardized quadratic Colless index therefore converges to

\[
 \frac{Q-1}{\sqrt{2/11}},
\]

a non-Gaussian law with skewness $1.095571564338\ldots$ and kurtosis $4.718284369910\ldots$. Kurtosis here means the fourth standardized moment, without subtracting 3.

For Sackin and Colless, their centered third and fourth moments have the same leading constants:

\[
 \frac{\mathbb E(X_n-\mathbb EX_n)^3}{n^3L^3}\longrightarrow a_3
 =0.107604590414363714\ldots>0,
\quad
 \frac{\mathbb E(X_n-\mathbb EX_n)^4}{n^4L^4}\longrightarrow a_4
 =0.308012262394708858\ldots,\quad X=S,C.                  \tag{5}
\]

Their skewness and kurtosis tend, respectively, to $0.724034681715\ldots$ and $3.912665923389\ldots$. Neither standardized index can converge to a Gaussian. Moreover,

\[
 \frac{(S_n-\mathbb ES_n)-(C_n-\mathbb EC_n)}{n\log n}
 \longrightarrow0\quad\hbox{in }L^2,\qquad
 \operatorname{Corr}(S_n,C_n)\longrightarrow1.             \tag{6}
\]

A full convergence theorem and uniqueness theorem for the Sackin/Colless candidate law are **not proved here**. An infinitesimal fixed-point equation consistent with all the proved moments is given in §9. No claim of priority beyond the papers actually inspected is made.

The computations are independent evidence, not premises of the proofs: first four moments through $n=4000$; an independent 45-digit first/second moment calculation; complete lattice probability arrays for every $2\le n\le200$; and Monte Carlo at $n=2000,10^5,10^6$. The finite PMFs use floating convolution, with error checks described in §10; they are not rational PMFs except for their small-$n$ verification.

## 2. What the literature check establishes

I read §§4.8–4.9 of the supplied [Aldous–Janson text](AJ_overview_2303.02529.txt), together with the adjacent discussion of the occupation-probability ansatz. The two toll claims in §4.9.1–2 are incorrect for the splitting law in the question. The corrected mean calculations and proofs are in §§3–5. The quadratic statistic is sensitive to large clades; its mean cannot be recovered by summing a fixed-clade limiting approximation without additional control.

In the supplied [Brandenberger–Chin–Mossel text](BCM_2505.24821.txt), I checked the introduction, Proposition 1.3, Corollaries 1.4–1.5, and the corresponding applications in §§4–5. Corollary 1.4 concerns fixed-size and fixed-shape clade counts. Corollary 1.5 concerns the **total length of the continuous-time tree**, with exponential holding-time tolls. It is not the total discrete leaf depth. Neither “Sackin” nor “Colless” occurs in the text, and the displayed recursions used for those corollaries do not treat the three indices here as random variables.

Proposition 1.3 requires, for positive constants and some \(\delta>0\),

\[
 |\mathbb EX_n-\mu n|=O(n^{1/2-\delta}),\quad
 |\operatorname{Var}X_n-\sigma^2n|=O(n^{1-\delta}),\quad
 \mathbb E|b_n|^3=O(n^{3/2-\delta}).                       \tag{7}
\]

Its split variable and toll may depend on each other; the random Colless toll is allowed by that part of its setup. However, all three statistics violate both growth assumptions in (7). Their original third absolute toll moments have orders $n^3,n^3,n^6$, respectively. For the last two assertions, the smaller split divided by $n$ tends to zero in probability, the normalized tolls are bounded, and bounded convergence applies. Centering does not repair their nonlinear variance growth. Thus Proposition 1.3 does not supply a CLT for these variables.

The Iksanov–Nikitin–Yakymiv paper was **not one of the two supplied files**. To check the stated distinction, I additionally read the primary [arXiv HTML, Theorem 1.2 and its definitions](https://arxiv.org/html/2510.17343). That theorem concerns a uniformly sampled leaf's discrete and continuous heights and decrement counts along its path. The text contains neither Sackin nor Colless. This additional source was checked directly; no theorem from it is used in our proofs. A sampled leaf CLT does not imply a CLT for the sum of all leaf depths, whose correlations must be accounted for.

## 3. Exact split tolls

Put $h=h_{m-1}$, $J=\min(I,m-I)$. Direct cancellation gives

\[
 \mathbb E[I(m-I)]
 =\sum_{i=1}^{m-1}\frac{m}{2h}
 =\frac{m(m-1)}{2h}.                                    \tag{8}
\]

Consequently the quadratic toll has the exact mean

\[
 g(m)=\mathbb E(m-2I)^2=m^2-\frac{2m(m-1)}h\sim m^2.      \tag{9}
\]

For completeness, an exact formula for the smaller daughter is

\[
 \mathbb EJ=\begin{cases}
 \displaystyle\frac mh(h_{m-1}-h_r),&m=2r+1,\\[3pt]
 \displaystyle\frac mh(h_{m-1}-h_r+1/m),&m=2r.
 \end{cases}                                             \tag{10}
\]

To obtain (10), pair the terms $i,m-i$. Each paired contribution for $i<m/2$ is $m/[h(m-i)]$; for even $m$, the central contribution is $1/h$. Harmonic-sum integral comparison now gives

\[
 \mathbb EJ=\frac{m\log2}{h}+O(1/h),\qquad
 c(m)=m-\frac{2m\log2}{h}+O(1/h)\sim m.                  \tag{11}
\]

An independent inequality already settles the leading coefficient: since $m-J\ge m/2$, $J\le2I(m-I)/m$, whence \(\mathbb EJ\le(m-1)/h\). Thus $c(m)/m\to1$. Equations (8)–(11) settle both tolls without a clade occupation approximation.

There is also a useful pathwise check of (9). At every split,

\[
 m^2-i^2-(m-i)^2=2i(m-i).
\]

Summing this identity over a tree telescopes to $n^2-n$. Therefore

\[
 QC_n=\sum_{\text{internal clades }v}|v|^2-2n(n-1).       \tag{12}
\]

The deterministic subtraction changes the mean but not the variance.

## 4. A comparison lemma for binary recursions

Define

\[
 (\mathcal D f)_n=f_n-\sum_{i=1}^{n-1}q(n,i)(f_i+f_{n-i}),
 \qquad
 \psi(p)=\int_0^1[1-x^p-(1-x)^p]\,\nu(dx).
\]

For $p>0$, the integral is finite: at an endpoint its numerator is $O(x+x^p)$. For integers $p\ge2$,

\[
 \psi(p)=h_{p-1}.                                       \tag{13}
\]

Indeed, 
\(\psi(p+1)-\psi(p)=\int[x^p(1-x)+(1-x)^px]\nu(dx)=1/p\), and \(\psi(2)=1\). Also \(\psi(p)<0\) for \(0<p<1\).

For $p>1$ and an integer $r\ge0$, let $f_n=n^p(\log n)^r$, with the natural values at $n=1$. Then

\[
 (\mathcal D f)_n\sim\psi(p)\frac{n^p(\log n)^r}{h_{n-1}}.\tag{14}
\]

For $r=0$, the same statement holds for $0<p<1$. To prove this, put $x=i/n$, expand \((\log n+\log x)^r\), and multiply the defect by \(h_{n-1}/[n^p(\log n)^r]\). Its leading term is the Riemann sum

\[
 \frac1n\sum_{i=1}^{n-1}
 \frac{1-(i/n)^p-(1-i/n)^p}{2(i/n)(1-i/n)}.
\]

It tends to \(\psi(p)\). The remaining finite number of sums have integrable endpoint bounds $x^{p-1}|\log x|^j$ and its reflection, and have extra factors \((\log n)^{-j}\), \(j\ge1\). To justify the improper Riemann sums explicitly, restrict first to \([\varepsilon,1-\varepsilon]\). On \((0,\varepsilon)\), the summands are bounded by sums of $x^{a-1}|\log x|^j$, $a>0$; comparison on the mesh intervals, or splitting once at the function's maximum, bounds their total by a constant times \(\varepsilon^{a}(1+|\log\varepsilon|^j)\), plus a vanishing mesh term. Let \(\varepsilon\downarrow0\). This also proves the asserted bounds for all sufficiently large $n$.

**Transfer lemma.** Suppose $u_n=\mathbb E(u_I+u_{n-I})+t_n$, with finite initial values, and

\[
 t_n\sim A\frac{n^p(\log n)^r}{h_{n-1}},\qquad p>1.
\]

Then \(u_n\sim[A/\psi(p)]n^p(\log n)^r\) when $A\ne0$; more generally the ratio tends to $A/\psi(p)$, also for signed sequences. An $O(\cdot)$ toll gives the corresponding $O(\cdot)$ bound on $u_n$.

For a proof, (14) makes the defects of

\[
 (A/\psi(p)+\varepsilon)f_n+Kn,
 \quad (A/\psi(p)-\varepsilon)f_n-Kn
\]

eventually lie above and below $t_n$. The defect of $Kn$ is zero. Choose $K$ large enough to bracket the finitely many earlier values. The positive coefficients in the recursion propagate both inequalities by induction. Divide by $f_n$, use $n/f_n\to0$, and let \(\varepsilon\downarrow0\). Fixed upper and lower multiples prove the $O$ version. This proof does not assume a contraction bounded away from one.

## 5. Mean asymptotics

For a symmetric split toll $t_n(i)$, the mean always satisfies

\[
 \mu_n=\mathbb E(\mu_I+\mu_{n-I}+t_n(I)),\qquad\mu_1=0.\tag{15}
\]

For Sackin take

\[
 f_n=n\left(\frac{(\log n)^2}{2z}+b\log n\right).
\]

Let

\[
 A_n=\sum_{i=1}^{n-1}\frac{-\log(i/n)}{n-i},\qquad
 B_n=\sum_{i=1}^{n-1}\frac{\log^2(i/n)}{n-i}.
\]

Symmetry of $q$ gives the exact expression

\[
 (\mathcal D f)_n=\frac n{h_{n-1}}
 \left(\frac{2L A_n-B_n}{2z}+b A_n\right).
\]

The integrals of \((-\log x)^r/(1-x)\), for $r=1,2$, are $z,2\zeta(3)$: expand \((1-x)^{-1}\) into its nonnegative geometric series and integrate. These integrands decrease on \((0,1)\); bounding the omitted first mesh interval gives

\[
 A_n=z+O(L/n),\qquad B_n=2\zeta(3)+O(L^2/n).
\]

Using \(h_{n-1}=L+\gamma+O(1/n)\) and the value of $b$ in (1), we obtain

\[
 (\mathcal D f)_n=n+O(\log n).
\]

The $O(\log n)$ defect error accumulates to only $O(n)$, as follows. Put \(v_n=n-\sqrt n\). Its defect is strictly positive for every $n\ge2$, because \(\sqrt i+\sqrt{n-i}>\sqrt n\); (14) with $p=1/2$ gives

\[
 (\mathcal D v)_n\sim-\psi(1/2)\frac{\sqrt n}{h_{n-1}}.
\]

This dominates \(\log n\). A sufficiently large multiple $Kv_n$ dominates the absolute error in the Sackin mean equation at every $n$. Induction on (15) proves \(|\mu_n-f_n|\le Kv_n=O(n)\). This proves the first line of (1), without importing an expansion from another paper.

For $D_n=S_n-C_n$, the split toll is exactly $2\min(i,n-i)$. By (11) its mean is \(2n\log2/h_{n-1}+O(1/h_{n-1})\). Put \(d=2\log2/z\). The defect of $d n\log n$ is

\[
 \frac{dn}{h_{n-1}}A_n
 =\frac{2n\log2}{h_{n-1}}+O(L/h_{n-1}).
\]

The residual is bounded. Since \(\mathcal D(n-1)=1\), comparison with multiples of $n-1$ yields

\[
 \mathbb ED_n=d n\log n+O(n).
\]

Subtracting proves the Colless assertion. In particular, its leading constant is \(1/(2z)=3/\pi^2\).

For QC, (9) gives a mean toll asymptotic to $n^2$. Use (14)–(15) with $p=2,r=1$. Since \(\psi(2)=1\) and \(\log n/h_{n-1}\to1\), the transfer lemma gives \(\mathbb EQC_n\sim n^2\log n\). This argument uses the whole recursion, including the large clades, and proves the last line of (1).

## 6. Sackin and Colless: variances and asymptotic non-normality

We prove the statements for either $X=S$ or $X=C$ simultaneously. Write

\[
 \mu_n=\mathbb EX_n,\quad v_n=\operatorname{Var}X_n,\quad
 u_{r,n}=\mathbb E(X_n-\mu_n)^r,\quad
 B_n(i)=t_n(i)+\mu_i+\mu_{n-i}-\mu_n.
\]

Thus $\mathbb EB_n(I)=0$. Conditional on the split, the two centered daughter variables are independent. The mean expansions just proved, and $0\le t_n(i)\le n$, show uniformly in $1\le i<n$ that

\[
 B_n(i)=-\frac{nL}{z}H(i/n)+O(n).                         \tag{16}
\]

Indeed, if $x=i/n$, $y=1-x$, then

\[
 i\log^2i+(n-i)\log^2(n-i)-nL^2
 =n[-2LH(x)+x\log^2x+y\log^2y].
\]

The last two functions, and $x\log x+y\log y$, are bounded. The three $O(\cdot)$ mean remainders sum to $O(n)$ uniformly. All constants in this section can be chosen separately for S and C; the leading terms coincide.

The improper Riemann-sum argument of §4 applies to $H^r\nu$, $r\ge1$, because $H(x)=O(x(1+|\log x|))$ near zero. Thus

\[
 \mathbb EH(I/n)^r\sim\frac1{h_{n-1}}\int H^r\,d\nu.
\]

In particular (16) implies

\[
 \mathbb E|B_n(I)|=O(n),\qquad
 \mathbb E|B_n(I)|^r=O(n^rL^{r-1})\quad(r\ge2).           \tag{17}
\]

The variance recursion is exact:

\[
 v_n=\mathbb E(v_I+v_{n-I})+\mathbb EB_n(I)^2.             \tag{18}
\]

By (16), its toll is asymptotic to

\[
 \frac{n^2L^2}{z^2h_{n-1}}J_2,\qquad J_2=\int H^2\,d\nu.
\]

The error in squaring (16) is bounded in expectation by
$O(n^2L\mathbb EH+n^2)=O(n^2)$, which is smaller than the displayed leading term. Expanding $H^2$ gives

\[
 J_2=\int_0^1\frac{x}{1-x}\log^2x\,dx
       +\int_0^1\log x\log(1-x)\,dx
     =(2\zeta(3)-2)+(2-z)=2\zeta(3)-z.                   \tag{19}
\]

The first integral follows by the geometric series used above. For the second, expand $-\log(1-x)=\sum_{k\ge1}x^k/k$ and integrate $-\log x$, obtaining $\sum_{k\ge1}1/[k(k+1)^2]=2-z$. All the interchanges have nonnegative summands. Apply the transfer lemma with $p=2,r=2$, using $\psi(2)=1$. This proves (2).

The next two central recursions are also exact:

\[
\begin{aligned}
 u_{3,n}&=\mathbb E(u_{3,I}+u_{3,n-I})
       +3\mathbb E[B_n(v_I+v_{n-I})]+\mathbb EB_n^3,\\
 u_{4,n}&=\mathbb E(u_{4,I}+u_{4,n-I})
       +6\mathbb E[v_Iv_{n-I}]
       +4\mathbb E[B_n(u_{3,I}+u_{3,n-I})]\\
       &\hspace{15mm}+6\mathbb E[B_n^2(v_I+v_{n-I})]
       +\mathbb EB_n^4.                                 \tag{20}
\end{aligned}
\]

Here and below the arguments of $B_n$ are $I$. We give the limiting calculation, including the cancellations needed at the singular endpoints.

First, $v_j\sim\kappa j^2\log^2j$ implies the uniform approximation

\[
 v_i+v_{n-i}-v_n
 =\kappa n^2L^2[x^2+y^2-1]+o(n^2L^2).                  \tag{21}
\]

For clarity, uniformity follows by bounding the asymptotic error for $j\ge j_0$ by $\varepsilon j^2\log^2j$, treating $j<j_0$ as a fixed bounded remainder, and using that $x^2\log x$ and $x^2\log^2x$ are bounded. Then let $\varepsilon\downarrow0$.

Since $\mathbb EB_n=0$, one may subtract $v_n$ inside the term linear in $B_n$. The uniform error in (21), multiplied by $\mathbb E|B_n|=O(n)$, is $o(n^3L^2)$. In the main term, substituting (16) incurs only $O(n^3L^2/h_{n-1})$, because $x^2+y^2-1=-2xy$ vanishes at both endpoints. Therefore the nonrecursive toll in the cubic equation, divided by $n^3L^2$, tends to

\[
 \frac{3\kappa}{z}\int[-H(x)](x^2+y^2-1)\,d\nu
       -\frac1{z^3}\int H^3\,d\nu
 =\frac{3\kappa}{2z}-\frac{J_3}{z^3},
\]

where $\int H(x)\,dx=1/2$. For $B_n^3$, expanding the $O(n)$ error in (16) and using $\mathbb EH^r=O(1/h_{n-1})$ makes every remaining term $o(n^3L^2)$. Transfer with $p=3,r=3$ now yields

\[
 a_3=\frac{1}{\psi(3)}
       \left(\frac{3\kappa}{2z}-\frac{J_3}{z^3}\right)
     =\frac\kappa z-\frac{2J_3}{3z^3},\qquad
 J_3=6\zeta(4)-3\zeta(3)-\frac32z.                       \tag{22}
\]

Here is an evaluation of the last integral. Expanding $H^3$ and using symmetry gives

\[
 J_3=-\int_0^1\frac{x^2}{1-x}\log^3x\,dx
       -3\int_0^1x\log^2x\log(1-x)\,dx.
\]

The first integral before its minus sign is $51/8-6\zeta(4)$. For the second, expand $-\log(1-x)$; its value is
$-2\sum_{k\ge1}1/[k(k+2)^3]=\zeta(3)+z/2-17/8$, by partial fractions. These give (22). Also $H\le\log2$, so $J_3\le(\log2)J_2$ and

\[
 a_3\ge\frac\kappa z\left(1-\frac{2\log2}{3}\right)>0.
\]

For the fourth equation in (20), exactly the same uniform-error argument applies to $u_{3,i}+u_{3,n-i}-u_{3,n}$. Its multiplier has mean zero and $\mathbb E|B_n|=O(n)$. The other terms use integrable endpoint products, or (17). More explicitly, after division by $n^4L^3$, the four toll terms tend, in their displayed order, to

\[
 \frac{\kappa^2}{2},\quad
 \frac{3a_3}{z},\quad
 \frac{6\kappa}{z^2}\int H^2(x)(x^2+y^2)\,d\nu,\quad
 \frac1{z^4}\int H^4\,d\nu.
\]

For the first term use $\int x^2y^2d\nu=1/12$. For the second use $x^3+y^3-1=-3xy$ and $\int Hdx=1/2$. In the third, the uniform error in replacing $v_i+v_{n-i}$ is $o(n^2L^2)$ and is multiplied by $\mathbb EB_n^2=O(n^2L)$. The error in replacing $B_n^2$ is at most $O(n^2L H+n^2)$; multiplication by $O(n^2L^2)$ and averaging is $O(n^4L^2)$. The fourth term follows by expansion of (16), with all errors $O(n^4L^2+n^4)$ by the same endpoint bounds. These estimates justify every replacement without a convergence-rate assumption for $v_n$ or $u_{3,n}$.

Consequently transfer with $p=4,r=4$ gives (5), with

\[
 a_4=\frac6{11}\left[
 \frac{\kappa^2}{2}+\frac{3a_3}{z}
 +\frac{6\kappa}{z^2}\int H^2(x)(x^2+(1-x)^2)\,d\nu
 +\frac1{z^4}\int H^4\,d\nu\right].                     \tag{23}
\]

This proves the stated limiting skewness and kurtosis. It also proves the absence of a Gaussian limit, rather than merely suggesting it from a histogram. If the standardized $X_n$ converged to a standard normal, the bounded standardized fourth moments would make their cubes uniformly integrable: $\mathbb E[|Z_n|^3;|Z_n|>R]\le \mathbb EZ_n^4/R$. Their third moments would then tend to zero, contradicting $a_3/\kappa^{3/2}>0$. Any other nondegenerate normal limit under deterministic centering and scaling would, by this moment bound and (2), give the same contradiction after standardization.

Finally the mean of $D=S-C$ was proved in §5. Its centered split toll is $2\min(i,n-i)-dnH(i/n)+O(n)$, uniformly $O(n)$. The variance recursion has toll $O(n^2)$. Transfer with $p=2,r=1$ gives $\operatorname{Var}D_n=O(n^2\log n)$. Dividing by $n^2L^2$ proves (6). The covariance identity
$2\operatorname{Cov}(S,C)=\operatorname{Var}S+\operatorname{Var}C-\operatorname{Var}(S-C)$ proves the correlation assertion. The centered pair is tight at scale $nL$, every subsequential law is supported on the diagonal, and its marginal has mean zero, variance $\kappa$, and third moment $a_3$ by uniform integrability. Thus every such marginal is non-Gaussian, although uniqueness of this subsequential law is not claimed.

## 7. Quadratic Colless: all moments and a limit law

Let $M_{k,n}=\mathbb E QC_n^k$, $M_{0,n}=1$, and $T_n(i)=(n-2i)^2$. Conditional independence gives the finite, exact recursion

\[
 M_{k,n}=\sum_iq(n,i)
 \sum_{a+b+c=k}\frac{k!}{a!b!c!}
          M_{a,i}M_{b,n-i}T_n(i)^c.
\]

We prove by induction on $k\ge1$ that

\[
 M_{k,n}\sim m_k n^{2k}L^k,
\quad m_0=1,\quad
 m_k=\frac{ k m_{k-1}
       +\frac12\sum_{j=1}^{k-1}\binom{k}{j}m_jm_{k-j}
                   B(2j,2k-2j)}{h_{2k-1}}.              \tag{24}
\]

Here $B(a,b)=\int_0^1x^{a-1}(1-x)^{b-1}dx$. For positive integers $a,b$, integration by parts gives $B(a,b)=(a-1)!(b-1)!/(a+b-1)!$. Thus all the constants in (24) are rational.

The case $k=1$ is the QC mean calculation. For the induction step, isolate the two terms $M_{k,i}+M_{k,n-i}$. All remaining daughter moments have order at most $k-1$ and hence obey both the induction asymptotic and a bound
$M_{j,l}\le K_j l^{2j}\log^j(el)$ for $j\ge1$.

If $c=0$, both daughter exponents are positive. Riemann sums, divided by $n^{2k}L^k/h_{n-1}$, converge to

\[
 \frac12\binom{k}{j}m_jm_{k-j}B(2j,2k-2j).
\]

The preceding bounds control an endpoint by a constant times $x^{2j-1}(1-x)^{2k-2j-1}$, so no mass is lost at a small daughter.

If $c=1$, the terms with one daughter exponent zero together contribute

\[
 k\mathbb E\{T_n(I)[M_{k-1,I}+M_{k-1,n-I}]\}
 \sim k m_{k-1}n^{2k}L^{k-1},\qquad k\ge2.
\]

To see this rigorously, for any fixed $\varepsilon>0$ the probability of $\varepsilon n\le I\le(1-\varepsilon)n$ is $O(1/h_{n-1})$. On its complement, the larger daughter's moment, divided by $n^{2k-2}L^{k-1}$, is uniformly close to $m_{k-1}$ as first $n\to\infty$ and then $\varepsilon\downarrow0$. The smaller daughter's normalized contribution tends to zero, and $T_n/n^2\to1$. All normalized summands are bounded by the induction bound. This proves the assertion. Terms with $c=1$ and both daughter exponents positive have one additional factor $1/h_{n-1}$ and are negligible.

If $c\ge2$, $T_n\le n^2$ and the moment bounds give $O(n^{2k}L^{k-c})=o(n^{2k}L^{k-1})$ for each term. This covers also a daughter exponent zero.

Therefore the nonrecursive toll is asymptotic to $n^{2k}L^{k-1}$ times the numerator in (24). Transfer with $p=2k,r=k$ proves (24), because $\psi(2k)=h_{2k-1}$. This completes the induction.

In particular $m_1=1$ and
$m_2=(2+1/6)/(11/6)=13/11$. Subtracting the square of the mean proves (3). The next two steps of the same finite rational recurrence give (4).

There is a second analytic derivation of the variance constant, useful as a check on the raw-moment calculation. Directly expanding the defect of $f_n=n^2L$ gives

\[
 (\mathcal D f)_n=\frac{n^2}{h_{n-1}}
 \left[L\frac{n-1}{n}+O(1)\right]
 =n^2+O(n^2/h_{n-1}).
\]

The bounded term is the Riemann sum of $[-x^2\log x-(1-x)^2\log(1-x)]/[2x(1-x)]$. Equation (9) and the $O$ transfer lemma with $p=2,r=0$ therefore sharpen the mean to $\mu_n=n^2L+O(n^2)$. Its centered split toll is, uniformly in the daughter size,

\[
 T_n(i)+\mu_i+\mu_{n-i}-\mu_n
   =-2n^2Lx(1-x)+O(n^2),\qquad x=i/n.
\]

Its second moment is asymptotic to

\[
 \frac{n^4L^2}{h_{n-1}}\int 4x^2(1-x)^2\,d\nu
 =\frac{n^4L^2}{3h_{n-1}}.
\]

The cross error is $O(n^4L\mathbb E[x(1-x)])=O(n^4)$ and the squared remainder is also $O(n^4)$. Apply the conditional-variance recursion and transfer with $p=4,r=2$ to obtain the independent constant $(1/3)/(11/6)=2/11$.

We now prove that these moment limits imply a unique limit distribution; this is necessary because moment convergence alone need not do so. Inductively,

\[
                  0\le m_k\le k!\quad(k\ge0).            \tag{25}
\]

It holds for $k=0,1$. Assuming the previous bounds, the numerator in (24) is at most

\[
 k!\left[1+\int\sum_{j=1}^{k-1}x^{2j}(1-x)^{2k-2j}\,d\nu\right]
 \le k!\left(1+\frac1{12}\right),\qquad k\ge2.
\]

Indeed, the sum in the integrand is bounded by
$x^2(1-x)^2[x^2+(1-x)^2]^{k-2}\le x^2(1-x)^2$ by the binomial theorem. Divide by $h_{2k-1}\ge11/6$ to obtain (25).

The nonnegative variables $QC_n/(n^2L)$ are tight by their bounded means. Every weakly convergent subsequence has all moments $m_k$, since the already proved bounded $(k+1)$st moments ensure uniform integrability of the $k$th powers. For such a subsequential limit, monotone convergence and (25) give

\[
 \mathbb E e^{tQ}=\sum_{k\ge0}\frac{t^km_k}{k!}
 \le\frac1{1-t},\qquad0\le t<1.
\]

Thus its moment generating function exists near zero and its Taylor coefficients determine it uniquely. For completeness, this gives uniqueness of the law: the moment generating functions are analytic on a vertical strip about the imaginary axis, agree near zero, and hence agree on that strip by analytic continuation; their characteristic functions coincide, which determines their distributions. Every subsequence therefore has the same weak limit, and the full sequence converges. The first two moments in (4) make it nondegenerate. Its nonnegative support excludes a nondegenerate Gaussian law. All-moment convergence also proves the asserted limiting skewness and kurtosis.

## 8. An infinitesimal fixed-point characterization of the QC limit

Let $\phi(s)=\mathbb E e^{-sQ}$. The law just proved is the unique nonnegative law with an exponential moment near zero whose Laplace transform satisfies

\[
 s\phi(s)=\int_0^1
   [\phi(sx^2)\phi(s(1-x)^2)-\phi(s)]\,\nu(dx),
 \qquad s>0,\quad\phi(0)=1.                             \tag{26}
\]

Unlike a first-root-split equation at fixed $n$, (26) retains the nontrivial effect after the degenerate root split. It is an infinitesimal binary-splitting equation with a unit additive accumulation rate and squared daughter weights.

Here is a proof independent of any assumed continuum-fragmentation construction. By (25), expand the Laplace transforms for sufficiently small $s$. The coefficient of $(-s)^k/k!$ on the right of (26) is

\[
 -h_{2k-1}m_k+
 \frac12\sum_{j=1}^{k-1}\binom{k}{j}m_jm_{k-j}B(2j,2k-2j)
 =-k m_{k-1},
\]

which is precisely the coefficient on the left. Interchanging the series and integral is justified, for example, by bounding the integral of the absolute $k$th coefficient by $k![h_{2k-1}+1/12]$ and summing against $s^k/k!$ for $|s|<1$.

For arbitrary positive $s$, the integral is finite. Near zero, $|\phi(sx^2)-1|\le sx^2\mathbb EQ$, and $|\phi(s(1-x)^2)-\phi(s)|\le s(2x-x^2)\mathbb EQ$, giving an $O(x)$ numerator. The other endpoint is symmetric. These bounds also give local uniform holomorphy for $\Re s>0$, so the identity for small positive $s$ extends to all $s>0$. Conversely, differentiating (26) at zero for a law with an exponential moment gives (24), beginning with $m_1=1$. The just-proved moment uniqueness proves the characterization. This establishes an identified non-Gaussian limit without invoking an external fragmentation limit theorem.

## 9. What remains conjectural for Sackin and Colless

The natural candidate for their common centered limit $W$ is characterized formally by a first-order binary-splitting equation with a unit drift and entropy displacement. For its characteristic function $\chi(t)=\mathbb E e^{itW}$, the equation is

\[
 0=it\chi(t)+\int_0^1\left[
 e^{-itH(x)/z}\chi(tx)\chi(t(1-x))-\chi(t)\right]\nu(dx),
 \quad\chi(0)=1,\quad\mathbb EW=0.                       \tag{27}
\]

This equation is consistent with (2), (22) and (23): expand formally through fourth order, use $\int H\,d\nu=z$, and isolate the pure daughter moments with coefficient $\psi(k)=h_{k-1}$. These are exactly the moment calculations already proved from the finite recursions. For example, its quadratic coefficient gives $\kappa z^2=J_2$; its cubic coefficient gives (22).

The conjecture is that $(S_n-\mathbb ES_n)/(nL)$ converges to a uniquely specified $W$ satisfying (27), and hence that the centered pair converges to $(W,W)$. Tightness, equality of all subsequential coordinates, non-Gaussianity of all marginal subsequential limits, and the first three marginal moments have been proved. Existence of a solution of (27), proof that each subsequential law satisfies it, and uniqueness of that solution have not been established here. Matching four moments is evidence for the candidate, not a substitute for those steps.

## 10. Numerical results and independent checks

### Finite moment recursions

The code in [moments.py](moments.py) uses conditional central moments, rather than subtracting two large second raw moments. It evaluates the exact recursive formulas in floating arithmetic for all $n\le4000$. It also computes the covariance of S and C and moments of $D=S-C$. The arrays and a readable table are [moments.npz](moments.npz) and [moments.csv](moments.csv).

An independent program, [verify_decimal.py](verify_decimal.py), uses **raw** first and second moment recursions, pairs symmetric daughter sizes, and uses Decimal arithmetic at 45 digits. Thus the variance check differs both algebraically and numerically from the central recursion. Every mean and variance through $n=2000$ agrees to within $1.98\times10^{-14}$ relative error; extending the check through $n=4000$ gives a worst relative difference $1.19\times10^{-13}$. The larger error belongs to the ordinary floating recursion, whose repeatedly accumulated harmonic sum has roundoff. On this ARM machine NumPy longdouble has only 52 stored fraction bits; its name is not evidence of extra precision. Exact rational raw-moment recursions through $n=30$ provide a third check, agreeing within $2.41\times10^{-15}$. The independent results are in [verification_decimal45.json](verification_decimal45.json) and [verification_rational.json](verification_rational.json); the $n=2000$ 45-digit values are also retained in LOG.md.

For $n=2000$, the independent high-precision calculation gives:

| Index | Mean | Variance |
|---|---:|---:|
| S | 48771.6874151457163 | 38240870.7116170733 |
| C | 34857.2753097922714 | 42414263.9345222725 |
| QC | 22179489.4166408022 | 118737385942860.563 |

The finite-$n$ trends below use the central recursion. A further independent 45-digit computation, [verify_raw4.py](verify_raw4.py), evaluates the raw binomial recursions through fourth order for every $n\le4000$, then centers at high precision. The maximum relative differences for the mean and second, third and fourth central moments are respectively $1.78\times10^{-14}$, $1.19\times10^{-13}$, $3.04\times10^{-13}$ and $8.51\times10^{-14}$. Thus every table entry below has a second calculation, including the skewness and kurtosis at $n=4000$. See [verification_raw4.json](verification_raw4.json). There are also independent full-PMF moment checks through $n=200$. The theoretical limits are derived in the proofs, with separate numerical checks of their integrals.

| $n$ | $\operatorname{Var}S/(n^2L^2)$ | S skewness | S kurtosis | $\operatorname{Var}C/(n^2L^2)$ | C skewness | C kurtosis | $\operatorname{Var}QC/(n^4L^2)$ | QC skewness | QC kurtosis |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 100 | .107630 | .840667 | 3.947211 | .137504 | .739949 | 3.733950 | .095623 | .919646 | 3.914150 |
| 500 | .143265 | .825073 | 4.009341 | .165629 | .766214 | 3.872910 | .116496 | .982871 | 4.197088 |
| 2000 | .165477 | .809718 | 4.013155 | .183536 | .769618 | 3.916465 | .128451 | 1.011228 | 4.327061 |
| 4000 | .174339 | .803003 | 4.010350 | .190764 | .769045 | 3.927270 | .133029 | 1.020861 | 4.371642 |
| Proved limit | .280574 | .724035 | 3.912666 | .280574 | .724035 | 3.912666 | .181818 | 1.095572 | 4.718284 |

Convergence is slow. Some of the skewness and kurtosis sequences are not monotone. The small-$n$ variance ratios do not estimate the asymptotic constants reliably without the analytic calculation.

### Full probability arrays

[distributions.py](distributions.py) computes the complete integer-lattice distribution using

\[
 p_n(s)=\sum_{i=1}^{n-1}q(n,i)
       \sum_u p_i(u)p_{n-i}(s-t_n(i)-u).
\]

It stores every lattice point between the exact attainable minimum and maximum, including gaps. No tails are pruned. Direct convolution is used when one input is short; otherwise FFT convolution is used. Each resulting array has tiny negative roundoff entries clipped to zero and is normalized. Such arrays give numerical PMFs, not rigorous intervals for each coefficient; relative errors in very small tail probabilities are not certified.

The folders [pmf/S](pmf/S), [pmf/C](pmf/C), and [pmf/QC](pmf/QC) contain distributions for every $2\le n\le200$. For example, QC at $n=200$ is represented by 2,607,020 consecutive lattice positions, from 80 through 2,607,099. Read the offset from the corresponding offsets.json; array entry $j$ is the probability at offset+$j$. The leaf distribution is deterministically a point mass at zero.

Exact rational convolution through $n=12$ checks the full small PMFs independently. [audit_results.py](audit_results.py) then rereads all saved arrays and recomputes four moments by elementwise reductions. Every array is finite, nonnegative and normalized to within $4.45\times10^{-16}$. Across all $n\le200$ and indices, the largest relative disagreements with the independent central recursion are, respectively, less than $1.84\times10^{-15}$, $1.86\times10^{-14}$, $4.40\times10^{-13}$ and $2.68\times10^{-12}$ for mean, variance, third and fourth central moment. The largest negative mass clipped in any pre-normalized array was below $1.99\times10^{-17}$. See [pmf_audit.json](pmf_audit.json) and each folder's checks.csv.

The initial diagnostic dot products produced floating status warnings in the installed BLAS despite finite, consistent outputs. The saved-array audit uses elementwise reductions, so these warnings are not silently treated as a verification. It reproduces the moment agreement independently.

### Constants

[constants.py](constants.py) computes $\kappa$ both from the zeta expression and by 60-digit quadrature of the entropy integral. It computes the first 16 QC moments as exact fractions using beta factorials, and independently recomputes the first four by quadrature of the split integrals. It evaluates $a_3$ using both its zeta expression and the entropy integral. It evaluates $a_4$ by (23), by formal coefficient extraction from (27), and independently using derivatives of the beta function in place of the entropy quadrature. The independent calculations agree beyond 50 decimal places. Results are in [constants.json](constants.json). The decimal values in the main results are rounded from those checks.

### Monte Carlo

[monte_carlo.cpp](monte_carlo.cpp) generates independent trees and accumulates the three indices. For symmetric statistics, a split can be drawn using $K$ with probability $1/[h_{m-1}K]$, and daughters $K,m-K$: its symmetrization is exactly $q(m,\cdot)$. The main sampler uses small-size alias tables and a logarithmic rejection sampler for larger sizes. In the latter, the proposal $K=\lfloor e^{U\log m}\rfloor$ has mass $\log(1+1/K)/\log m$ and is accepted with probability $\log2/[K\log(1+1/K)]$, giving the required harmonic law. A second sampler independently inverts the harmonic cumulative sums by binary search. Sizes 2 and 3 have deterministic statistics and are accumulated without random draws.

The runs were: 20,000 alias and 100,000 cumulative-inversion trees at $n=2000$; 10,000 alias and 5,000 cumulative-inversion trees at $10^5$; and 5,000 alias trees at $10^6$. Seeds and exact commands are in §11. The independent $n=2000$ inversion run compares to the exact recursion as follows; the deviations are in estimated standard errors, using empirical fourth moments for the variance error.

| Index | Mean deviation | Variance deviation |
|---|---:|---:|
| S | -.767 | -1.182 |
| C | -.665 | -1.218 |
| QC | -.284 | -.687 |

The earlier 20,000-tree alias run had mean deviations between 1.63 and 2.14 and variance deviations between 2.16 and 2.44 standard errors. Both runs are retained. Their contrast is a reminder that these checks have sampling error; it is not evidence to round the exact recurrence towards a simulation.

Representative large-tree results are:

| $n$ | Replicates | Index | Scaled variance | Skewness | Kurtosis |
|---:|---:|---|---:|---:|---:|
| $10^5$ | 10,000 | S | .209993 | .809308 | 4.137478 |
| $10^5$ | 10,000 | C | .221650 | .786685 | 4.076092 |
| $10^5$ | 10,000 | QC | .154448 | 1.075515 | 4.867840 |
| $10^6$ | 5,000 | S | .207560 | .736995 | 3.745700 |
| $10^6$ | 5,000 | C | .216494 | .724112 | 3.721269 |
| $10^6$ | 5,000 | QC | .147774 | 1.041616 | 4.329597 |

Here the variance scaling is $n^2L^2$ for S,C and $n^4L^2$ for QC. At $10^6$, estimated standard errors for these scaled variances are about .0049, .0051 and .0038. They still lie below the limiting constants: finite-size corrections remain material even for a million leaves. The Monte Carlo tables are checks of shape and order, not precise measurements of the limiting constants. The $10^5$ second-sampler QC mean differs from the first run by about 2.9 combined standard errors; the corresponding S,C mean differences are about 1.9. The exact $n=2000$ checks and analytic correctness of both sampling schemes provide the stronger validation. No agreement within a chosen tolerance is assumed as a premise of any theorem.

The full summaries, including estimated mean and variance errors, are in [mc_summary.json](mc_summary.json). [verify_mc.py](verify_mc.py) independently recomputes each sample's raw integer power sums exactly and centers them with 80-digit Decimal arithmetic. All reported Monte Carlo means, variances, skewnesses and kurtoses agree with that second computation within $2.67\times10^{-15}$ relative error. This checks the sample summaries; it does not remove sampling uncertainty.

![Standardized exact finite laws and large-tree simulations](laws.png)

![Finite moment trends and proved limiting constants](trends.png)

Standalone vector versions are [laws.pdf](laws.pdf) and [trends.pdf](trends.pdf). The approximate density curves use exact-recursion probabilities at $n=200$ and independently standardized Monte Carlo samples at $10^6$, with a standard normal for reference. They are not a numerical solution of (27).

## 11. Reproduction, resources and remaining scope

All source programs were saved before execution. All writes and outputs stayed in this directory. No agents, pushes, deployments or visible windows were used. Numerical thread environment variables are set before imports in common.py; the C++ code is serial and uses no numerical library. The initial attempt to add nice priority was rejected by the sandbox; the supplied outer launcher already requested nice 10, and no privileged retry was attempted. macOS rejected a restrictive address-space limit because of its address-space reservation policy; the actual numerical allocation sizes were kept bounded and checked by RSS instead.

The largest calculation is the full QC distribution table. The stored PMF coefficient arrays together take approximately 1.0 GB; the working FFT and reduction arrays add well under 1 GB at $n\le200$. Its periodic peak-RSS checks never reached the 3.7 GB stop threshold. The independent complete-array audit recorded a peak of 597,491,712 bytes, and the million-leaf C++ sampler recorded 10,289,152 bytes. Thus each computation remains below 4 GB. No simulation worker pool was used. Small cache directories for plotting are local.

To reproduce the numerical work, from this directory run the following saved programs in order. NumPy, SciPy, mpmath and Matplotlib are required; no installation was performed.

    python3 moments.py --n 4000
    python3 verify_decimal.py --n 4000
    python3 verify_raw4.py --n 4000
    python3 distributions.py --n 200
    python3 audit_results.py
    python3 constants.py
    clang++ -O3 -std=c++17 monte_carlo.cpp -o monte_carlo
    ./monte_carlo 2000 20000 346907 alias mc_2000.csv
    ./monte_carlo 2000 100000 550571 cdf mc_2000_cdf.csv
    ./monte_carlo 100000 10000 461381 alias mc_100000.csv
    ./monte_carlo 100000 5000 829133 cdf mc_100000_cdf.csv
    ./monte_carlo 1000000 5000 791939 alias mc_1000000.csv
    python3 mc_summary.py
    python3 verify_mc.py
    python3 figures.py

Rerunning overwrites the corresponding numerical artifacts and appends timestamped findings to [LOG.md](LOG.md). The PMFs retain tiny floating tail errors, Monte Carlo has finite sample error, and a full limiting-law theorem for Sackin/Colless remains open within this work. The leading variances, their non-Gaussian conclusions, the corrected mean asymptotics, the limiting third/fourth centered moments, and the QC limit theorem do not depend on those numerical approximations.

Final audit completed 12 November 2026 at 23:30 Asia/Tbilisi. Independent raw and central moment calculations, full-PMF moment checks, exact integer checks of the Monte Carlo summaries, report links, equation numbering and mathematical delimiters passed. All numerical jobs have finished. The separate conjectural status of the full Sackin/Colless law is retained.

Task: “study the distributions of tree balance indices for DTCS(n) beyond the expectations” — received 12 November 2026, approximately 23:06 Asia/Tbilisi.
