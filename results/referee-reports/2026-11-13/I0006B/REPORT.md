PROVED

# I0006B: the critical lower tail of the divisible sandpile

Matching upper and lower bounds are proved below, including the logarithmic correction and the secondary stretched-exponential case.

## Statement

Let $d\ge5$, $P f(x)=(2d)^{-1}\sum_{y\sim x}f(y)$, and
\[
 u_0=0,\qquad u_{n+1}=(\eta+Pu_n)_+.
\]
Suppose the scenery is i.i.d., has mean zero and positive finite variance, and has an exponential moment of its absolute value. Put $p=d/2$. Assume there are positive constants $c_0,C_0,t_0$ such that
\[
 e^{-C_0t^p}\le\mathbb P(\eta(0)<-t)\le e^{-c_0t^p},\qquad t\ge t_0. \tag{1}
\]
Then
\[
 \boxed{\quad \mathbb E u_n(0)\asymp
 (\log n)^{2/d}(\log\log n)^{1-2/d}\quad} \qquad(n\longrightarrow\infty). \tag{2}
\]
Here and throughout, $\asymp$ means two inequalities with positive constants, not convergence of the ratio. There is no assertion of a universal leading constant. One may replace the logarithms in (2) by $\log(n+e^e)$ and $\log\log(n+e^e)$ for a statement including small $n$.

The rare-event cost at mean height $m$ is, up to constants,
\[
 \Phi(m):=\frac{(1+m)^p}{[\log(e+m)]^{p-1}}. \tag{3}
\]
In particular, the exponent in the question is $m^{d/2}/(\log m)^{d/2-1}$, and the extra factor in the mean is a positive power of $\log\log n$.

There is also a result for the secondary question. If $0<\gamma<1$, replace (1) by two-sided bounds $e^{-Ct^\gamma}\le\mathbb P(\eta(0)<-t)\le Ce^{-ct^\gamma}$, retain mean zero and nondegeneracy, and assume $\mathbb P(\eta(0)>t)\le Ce^{-ct}$, then
\[
 \boxed{\quad\mathbb E u_n(0)\asymp(\log n)^{1/\gamma}.\quad} \tag{4}
\]
The proof of (4) uses no exponential moment of $|\eta|$.

All constants below can depend on $d$, the one-site law and the fixed constants in its moment and tail bounds. Constants denoted $c,C$ can change between displays. None depends on time, a Green truncation time, a deviation level, or a radius. All logarithms are natural.

## 1. Sources, normalization, and the exact gap in print

The two sources are Ahmed Bou-Rabee and Christoforos Panagiotis, [*Sharpness and critical scaling of parking*, arXiv:2609.02820v1](https://arxiv.org/html/2609.02820v1), and [*Quantitative explosion and percolation of the divisible sandpile*, arXiv:2609.02829v1](https://arxiv.org/html/2609.02829v1). Both v1 submission dates are 2 September 2026. Page references below are the printed pages, verified in the staged paginated texts, not HTML line numbers.

The parking paper's Theorem 3.4, p.14, uses exactly the recursion in this report, with scenery called $\eta$. The companion uses $\zeta=(\sigma-1)/(2d)$, with the same recursion; see its Lemma 2.1, p.15. Thus set $\eta=\zeta$ to use its estimates. The companion's odometer is mass emitted **to each neighbor**, whereas the parking paper rescales by (2d). This distinction changes constants only, but no factor of (2d) is being hidden in the displayed recursion here. Real signed scenery is permitted; the quoted parking theorem explicitly allows it.

Both complete plain-text sources are in `sources/`. They were already staged when work began. For independent verification, both arXiv HTML responses were downloaded into memory and converted to additional plain-text files, retaining MathML `alttext` formulas. `data/source_manifest.json` records URLs, retrieval information, and SHA-256 hashes. No PDF, page image, or scan was downloaded or retained in this directory.

The requested passage was read in full. Its argument has the following structure.

| Location in the companion | What is used, and what happens at the endpoint |
| --- | --- |
| Theorem 1.3(iii)(b), p.6 | States the two-sided mean order for $\gamma\in[1,\infty)\setminus\{d/2\}$. The exclusion is explicit. |
| Proof overview, p.10 | Explicitly says the borderline $\gamma=d/2$ is not treated. |
| Assumption (85), p.51 | An exponential moment of $\lvert\zeta\rvert$; no condition on $\gamma$. |
| (86), p.51 | Exact reflected-increment identity. It uses mean zero and stationarity, not the tail exponent. |
| (87), p.51 | Decreasing mean increments, hence increment at time $t$ at most $\mathbb E u_t/t$. No strict exponent condition. |
| Theorem 6.1, pp.51–52, (88)–(90) | Uniform point concentration and a constant-depth negative-ball lower bound, of cost $m^{d/2}$. Works at the endpoint. |
| Corollary 6.2, pp.52–53 | Removes the exponential-moment assumption from the universal lower bound for a fixed integrable nondegenerate law. No endpoint exclusion. |
| Proposition 6.3, p.53, (91) | Adds the one-deep-hole lower bound. It takes the minimum of the one-hole cost $m^\gamma$ and negative-ball cost $m^{d/2}$. No strict inequality is used in this comparison. |
| Lemma 6.4, pp.53–54, (92) | **The analytic source of the exclusion.** Put $q=\gamma/(\gamma-1)$. For $\gamma<d/2$, it uses $\sum_yG(0,y)^q<\infty$; for $\gamma>d/2$, the inner radial power sum is strictly polynomial. At equality it is logarithmic. |
| Lemma 6.5, p.54 | Concentration of $P^m(u_n-\mathbb E u_n)$, using the Green time tail's supremum and squared sum. No $\gamma$ occurs. |
| Theorem 6.6, pp.55–56, (93) | Imports Lemma 6.4's exponent. At the endpoint replace $s^{\min\{\gamma,d/2\}}$ by $\Phi(s)$. |
| (94), p.55 | Crude $\mathbb E u_t\le C\log(t+2)$. Uses only exponential-moment concentration. It remains valid at the endpoint. |
| (95)–(98), pp.55–56 | The smoothing and time-window argument remains valid. The smoothed term costs $h^{d/2}$, which is stronger than $\Phi(h)$. Integrate the modified increment estimate and invert $\Phi$. |

More precisely, the divergent sum restricted to radius $L$ is
\[
 \sum_{|y|\le L}G(0,y)^{d/(d-2)}\asymp\log(2+L).
\]
The Laplace proof should not keep $L$ arbitrarily large: its crossover radius is $L\asymp\lambda^{1/(d-2)}$. Consequently the missing term is $\lambda^{d/(d-2)}\log\lambda$ in the log Laplace transform. Its Legendre transform costs $s^{d/2}/(\log s)^{d/2-1}$, not $s^{d/2}$.

The printed endpoint bounds in the question follow: Proposition 6.3 gives the lower bound $(\log n)^{1/p}$, and Theorem 6.6 applied with any exponent strictly below $p$ gives $C_\varepsilon(\log n)^{1/p+\varepsilon}$. No uniform control of those constants as the exponent approaches $p$ is printed or assumed here.

## 2. Heuristic and the variational problem

Write $w_y=G(0,y)\asymp(1+|y|)^{2-d}$ and $q=p/(p-1)=d/(d-2)$. For a finite ball, the exact power-cost problem is
\[
 \inf\left\{\sum_{|y|\le L}a_y^p:
 a_y\ge0,\ \sum_{|y|\le L}w_ya_y\ge m\right\}
 =\frac{m^p}{S_L^{p-1}},\qquad
 S_L=\sum_{|y|\le L}w_y^q. \tag{5}
\]
Hölder gives the lower bound, and equality is attained at
\[
 a_y=\frac{m}{S_L}w_y^{1/(p-1)}.
\]
Thus $S_L\asymp\log L$, and the optimal depths have shape
\[
 a_y\asymp\frac{m}{\log L}(1+|y|)^{-2}. \tag{6}
\]

A single hole costs order $m^p$. A constant-depth ball giving deficit $m$ also costs order $m^p$. Splitting only between these two configurations changes a constant, since minimizing $c_1a^p+c_2b^p$ with $a+b=m$ still costs order $m^p$. The logarithmic gain comes from distributing the deficit among order $\log m$ annuli. Each dyadic annulus has the same power-cost/deficit relation at this exponent.

One must not send $L\to\infty$ in (5) and claim zero cost. Small mean shifts have a quadratic cost, while a pointwise event that every site is negative has a nonzero cost per site. A convenient convex variational model retaining the small-shift cost is
\[
 \mathcal I(m)=\inf\left\{\sum_yJ(a_y):
 a_y\ge0,\ \sum_yw_ya_y\ge m\right\},\qquad
 J(a)=a^2+a^p. \tag{7}
\]
This is a comparison variational problem, not a claim that the law's exact rate function equals $J$. It can be solved up to constants:
\[
 \mathcal I(m)\asymp\frac{m^p}{(\log m)^{p-1}}. \tag{8}
\]

For the lower bound, its conjugate satisfies $J^*(t)\le Ct^2$ for $t\le1$ and $J^*(t)\le Ct^q$ for $t\ge1$. Splitting at $r_\lambda\asymp\lambda^{1/(d-2)}$ gives
\[
 \sum_y J^*(\lambda w_y)\le C\lambda^q\log(e+\lambda).
\]
Fenchel's inequality gives $\sum J(a_y)\ge\lambda m-C\lambda^q\log(e+\lambda)$; choosing $\lambda=b[m/\log m]^{p-1}$ with small fixed $b>0$ proves the lower bound in (8). For the upper bound choose
\[
 a_y=\frac{A}{1+|y|^2}\,1_{\{|y|\le\sqrt A\}},\qquad A=Cm/\log m.
\]
The Green deficit is at least $cA\log A$, hence at least $m$ after fixing $C$ large. The power cost is $O(A^p\log A)$, and the quadratic cost is $O(A^p)$: indeed
$A^2\sum_{|y|\le\sqrt A}(1+|y|^2)^{-2}\le CA^2A^{(d-4)/2}=CA^p$.
This proves (8).

Equivalently, the Euler equation $2a+pa^{p-1}=\lambda w_y$ yields $a_y\asymp A|y|^{-2}$ in the core and $a_y\asymp\lambda w_y$ outside, where $A=\lambda^{1/(p-1)}$. The transition radius is $L\asymp\sqrt A$, the deficit is $m\asymp A\log A$, and the cost is $A^p\log A$. The proof below makes this profile force an actual reflected increment, so it does not rely on identifying a scenery large deviation with an odometer event.

## 3. Common elementary estimates

Put $M_n=\mathbb E u_n(0)$ and $A_n=\eta(0)+Pu_n(0)$. Monotone iteration gives $u_{n+1}\ge u_n\ge0$. The bound $u_n\le\sum_{j<n}P^j\eta_+$ makes every finite-time expectation finite. Stationarity and mean zero give
\[
 M_{n+1}-M_n=\mathbb E(-A_n)_+
 =\int_{M_n}^\infty\mathbb P(A_n-M_n<-h)\,dh. \tag{9}
\]
Strict or nonstrict inequalities inside this integral have the same integral, including for atomic scenery. Moreover
\[
 0\le M_{n+1}-M_n\le B:=\mathbb E\eta(0)_-<\infty, \tag{10}
\]
and the increments decrease because $A_n$ increases pointwise. These are the companion's Lemma 2.4, p.16, and (86)–(87), p.51.

Let $g_k(x,y)=\sum_{j=0}^{k-1}P^j(x,y)$. Iterating the 1-Lipschitz positive-part map gives the deterministic coordinate bound
\[
 |u_n(x;\eta)-u_n(x;\widetilde\eta)|
 \le\sum_y g_n(x,y)|\eta(y)-\widetilde\eta(y)|. \tag{11}
\]
This also follows from the optimal-stopping representation, Theorem 2.2, p.15. It needs no atomlessness or differentiability. Every function here depends on finitely many scenery variables. Thus $u_n(x)$ has coordinate constants $g_n(x,y)\le G(x,y)$, and $A_n$ has coordinate constants $g_{n+1}(0,y)\le G(0,y)$.

The random-walk estimates used below are
\[
 c(1+|y|)^{2-d}\le G(0,y)\le C(1+|y|)^{2-d},
 \qquad \sum_{|y|>R}G(0,y)^2\le CR^{4-d}. \tag{12}
\]
In particular $G(0,\cdot)\in\ell^2$. For $H_k(y)=\sum_{j\ge k}P^j(0,y)$,
\[
 \|H_k\|_\infty\le Ck^{-(d-2)/2},\qquad
 \sum_yH_k(y)^2\le Ck^{-(d-4)/2}. \tag{13}
\]
These are the companion's Section 3.1, in particular (37)–(39), p.21. They can also be checked directly: the heat-kernel bound $P^j(0,y)\le Cj^{-d/2}$ gives the supremum, and symmetry and convolution give
$\sum_yH_k(y)^2=\sum_{i,j\ge k}P^{i+j}(0,0)\le C\sum_{r\ge2k}(r-2k+1)r^{-d/2}\le Ck^{2-d/2}$.
The spatial Green estimates follow by summing Gaussian heat-kernel bounds; for the lower bound sum the admissible-parity times of order $|y|^2$. Lattice annular counting then gives (12).

We use the following concentration consequence of the exponential moment. If $F$ has coordinate constants $\ell_y$, then
\[
 \mathbb P(|F-\mathbb EF|>s)\le C\exp\left[-c\min\left\{
 \frac{s^2}{\sum\ell_y^2},\frac{s}{\max\ell_y}\right\}\right]. \tag{14}
\]
This is Lemma 3.2(b), pp.21–22, of the companion. For completeness, expose the coordinates and let $D_y$ be the resulting Doob differences. Conditional on preceding coordinates, a difference is a centered $\ell_y$-Lipschitz function of one fresh scenery variable. Its conditional $k$-th absolute moment is at most $k!C^k\ell_y^k$. Taylor expansion and conditional mean zero yield
$\mathbb E(e^{\lambda D_y}\mid\mathcal F_{y-1})\le\exp(C\lambda^2\ell_y^2)$ for $|\lambda|\max\ell_y\le c$. Iteration and Chernoff with $\lambda$ a small constant times $\min\{s/\sum\ell_y^2,1/\max\ell_y\}$ prove (14). All constants depend only on the fixed one-site exponential moment.

Applying (14) to $A_n$, then (9), gives $M_{n+1}-M_n\le Ce^{-cM_n}$. The bounded-increment argument in Section 6 below therefore gives
\[
 M_n\le C\log(n+2). \tag{15}
\]

## 4. Critical upper bound

### 4.1. Keep the logarithm in the Green average

The upper half of (1), centering, and the moment assumption imply
\[
 \log\mathbb E e^{-t\eta(0)}\le
 \begin{cases}Ct^2,&0\le t\le1,\\ Ct^q,&t\ge1.\end{cases} \tag{16}
\]
For small $t$, use the centered Taylor expansion, bounded by the exponential moment near zero; on any remaining compact subinterval of $(0,1]$, enlarge $C$. For large $t$, the negative-tail integral is bounded by Young's inequality $ts\le(c_0/2)s^p+C t^q$, while positive scenery contributes at most one. This proves (16) without a positive-tail moment of order $p$.

For every truncation time $k\ge1$, independence gives, with $\lambda\ge1$,
\[
 K_k(\lambda):=\log\mathbb E\exp\left(-\lambda\sum_yg_k(0,y)\eta(y)\right)
 \le C\lambda^q\log(e+\lambda). \tag{17}
\]
To check uniformity in $k$, choose $R=C_1\lambda^{1/(d-2)}$, $C_1$ large enough that $\lambda G(0,y)\le1$ for $|y|>R$. On the inner ball, (16) is bounded by $C(\lambda G)^q$, also when $\lambda g_k<1$, because $q<2$. Its sum is $C\lambda^q\log(2+R)$. The outer sum is at most
$C\lambda^2\sum_{|y|>R}G(0,y)^2\le C\lambda^2R^{4-d}=C\lambda^q$.
This proves (17).

Choose
\[
 \lambda=b\left[\frac{s}{\log(e+s)}\right]^{p-1}.
\]
For large $s$ this exceeds one. The negative Chernoff term is of order $-bs^p/(\log s)^{p-1}$; the positive term in (17) is at most $C b^q s^p/(\log s)^{p-1}$, since $(p-1)q=p$. Fix $b>0$ small enough that the latter is at most half the former. Increasing $C$ for bounded $s$, we obtain, uniformly in $k$,
\[
 \mathbb P\left(\sum_yg_k(0,y)\eta(y)\le-s\right)
 \le C e^{-c\Phi(s)},\qquad s\ge1. \tag{18}
\]

### 4.2. Transfer the Green tail to reflected increments

From (11), the coordinate constants of $P^k u_j(0)$ are bounded by $H_k$. Thus (13)–(14) give, for $k\ge1,j\ge0,s\ge1$,
\[
 \mathbb P\left(P^k(u_j-M_j)(0)\le-s\right)
 \le C\exp[-c\min\{s^2k^{(d-4)/2},s k^{(d-2)/2}\}]. \tag{19}
\]
This reproduces Lemma 6.5, with all time parameters uniform.

Fix $\varepsilon\in(0,1)$ with $\varepsilon B\le1/8$. For $M_n\le h\le\sqrt n$, put $k=\lfloor\varepsilon h\rfloor$. When $M_n$ is sufficiently large, $1\le k\le n$, $k\asymp h$, and (10) gives $M_n-M_{n-k}\le h/8$. Iterating $u_{j+1}\ge\eta+Pu_j$ gives
\[
 A_n-M_n\ge \sum_{i=0}^kP^i\eta(0)
       +P^{k+1}(u_{n-k}-M_{n-k})(0)-h/8.
\]
Consequently $A_n-M_n\le-h$ implies that at least one of the two random terms is at most $-7h/16$. By (18) the first probability is at most $Ce^{-c\Phi(h)}$. By (19) the second is at most $Ce^{-ch^p}$, since both powers in its minimum equal $h^{d/2}$ up to constants. Therefore
\[
 \mathbb P(A_n-M_n\le-h)\le Ce^{-c\Phi(h)},
       \quad M_n\le h\le\sqrt n. \tag{20}
\]

For $h>\sqrt n$, the crude concentration (14) gives an integrated contribution $Ce^{-c\sqrt n}$. By (15), this is at most $Ce^{-c'\Phi(M_n)}$. The function $\Phi$ is increasing and its derivative is at least one for all sufficiently large arguments: logarithmic differentiation gives
$\Phi'(s)/\Phi(s)=p/(1+s)-(p-1)/[(e+s)\log(e+s)]$, and $\Phi'(s)\asymp(s/\log s)^{p-1}$.
Thus integrating (20) in (9) yields
\[
 M_{n+1}-M_n\le C e^{-c\Phi(M_n)}. \tag{21}
\]
For bounded $M_n$, (10) permits the same estimate after enlarging $C$. This completes the analytic upper bound; Section 6 converts it into (2).

## 5. Critical lower bound: a logarithmic supersolution

This step supplies the logarithmic gain missing from Proposition 6.3. Let
\[
 f(x)=\log(1+|x|^2).
\]
For $s=1+|x|^2$ and coordinate $i$, the exact identity is
\[
 f(x+e_i)+f(x-e_i)-2f(x)
 =\log\frac{(s+1)^2-4x_i^2}{s^2}
 \le2\log(1+1/s).
\]
The logarithm's numerator is positive, being the product of two positive numbers. Summing and dividing by (2d) proves
\[
 (P-I)f(x)\le\log(1+1/s)\le\frac1{1+|x|^2}. \tag{22}
\]
No sign or lower bound on this discrete Laplacian is needed.

Fix $n$ and put $M=M_n$. Suppose $M$ is large. Let $a>0$ be the unique solution of
\[
 a\log(1+a)=2M+1, \tag{23}
\]
let $R=\lceil\sqrt a\rceil$, let $D=\{x\in\mathbb Z^d:|x|<R\}$, and let $\partial^+D$ be its exterior vertex boundary. Set $w=af$. Consider the event
\[
 E_n=\left\{\eta(x)\le-\frac{2a}{1+|x|^2}\text{ for all }x\in D\right\}
 \cap\{u_n(z)\le2M+1\text{ for all }z\in\partial^+D\}. \tag{24}
\]
For boundary sites, $|z|\ge R\ge\sqrt a$, so (23) gives $w(z)\ge2M+1$. Time monotonicity therefore gives $u_j(z)\le w(z)$ on the boundary for every $j\le n$. Since $u_0=0\le w$, induction using (22) gives $u_j\le w$ on $D$ for all $j\le n$: indeed, whenever the comparison holds for all neighbors,
\[
 \eta(x)+Pu_j(x)\le w(x)-\frac{a}{1+|x|^2}\le w(x),
\]
and taking the positive part preserves the last inequality because $w\ge0$.

In particular, all neighbors of zero satisfy $u_n(e)\le a\log2$, while $\eta(0)\le-2a$. Hence on $E_n$,
\[
 A_n\le-(2-\log2)a,\qquad(-A_n)_+\ge a. \tag{25}
\]

We now check the probability of the entire event, including its dependent boundary part. The lower half of (1) and monotonicity of the tail imply, for every $t\ge0$,
\[
 \mathbb P(\eta(0)\le-t)\ge\exp[-C(1+t^p)]. \tag{26}
\]
For small $t$, use the fixed positive probability of being below one sufficiently large negative level. All events in (24) are decreasing functions of the independent scenery. Product-measure positive association therefore gives a lower bound by the product of their individual probabilities, even though the boundary odometers depend on the scenery inside $D$. Markov's inequality gives
\[
 \mathbb P(u_n(z)\le2M+1)\ge1-\frac{M}{2M+1}\ge\frac12.
\]
Independence for the scenery conditions, or the same association inequality, now gives
\[
 -\log\mathbb P(E_n)\le
 C|D|+C a^p\sum_{x\in D}(1+|x|^2)^{-p}
       +(\log2)|\partial^+D|. \tag{27}
\]
For $a\ge1$, $R\le2\sqrt a$, and even the crude count
$|D|+|\partial^+D|\le C(R+1)^d\le Ca^p$ suffices. At $2p=d$, annular counting gives
\[
 \sum_{|x|<R}(1+|x|^2)^{-p}\le C\log(2+R).
\]
Thus
\[
 \mathbb P(E_n)\ge\exp[-C a^p\log(e+a)]. \tag{28}
\]

Equation (23) implies $a\asymp M/\log M$ and $\log a\asymp\log M$: take logarithms of $a\log a\asymp M$, noting $a\to\infty$. Equations (9), (25), and (28), with $a\ge1$, give
\[
 M_{n+1}-M_n\ge e^{-C\Phi(M_n)} \tag{29}
\]
when $M_n$ is large. For bounded $M_n$, a one-hole event and the boundary Markov argument, or the same construction with constants enlarged, give a positive constant lower bound. Thus $c e^{-C\Phi(M_n)}$ is a lower bound for every $n$.

The construction also proves $\mathbb P(A_n\le-1)\ge e^{-C\Phi(M_n)}$ for large $n$. Together with (20) at $h=M_n+1$, which is admissible by (15) for large $n$, this shows that the actual reflected-update event has logarithmic probability of order $-\Phi(M_n)$. It is not merely a variational prediction for a linear field.

## 6. Integrating the increment bounds

Here is the discrete argument, including the possible overshoot at threshold crossings. Suppose $M_0=0$, $M_n$ increases, its increments are at most $B$, and
\[
 c e^{-C\Psi(M_n)}\le M_{n+1}-M_n\le C e^{-c\Psi(M_n)}, \tag{30}
\]
where $\Psi$ is increasing, $\Psi(s/2)\asymp\Psi(s)$ at infinity, and $\log(s+2)=O(\Psi(s))$. The functions used here, $\Phi(s)$ and $(1+s)^\gamma$, have these properties.

For the lower bound, let $F(s)=c^{-1}\int_0^s e^{C\Psi(r)}dr$. Since $F'$ is increasing, (30) implies
$F(M_{n+1})-F(M_n)\ge F'(M_n)(M_{n+1}-M_n)\ge1$.
Thus $n\le F(M_n)\le C'e^{C'\Psi(M_n)}$, so $\Psi(M_n)\ge c'\log n$ for large $n$. The lower increment bound also ensures $M_n\to\infty$: a bounded sequence would have increments bounded below by a positive constant.

For the upper bound, set $\tau_R=\inf\{n:M_n\ge R\}$. It is finite by the preceding observation. Then $M_{\tau_R}\le R+B$. For $R>2B$, the total increase from $\tau_R$ to $\tau_{2R}$ is at least $R-B\ge R/2$, while every increment in this interval is at most $Ce^{-c\Psi(R)}$. Therefore
\[
 \tau_{2R}-\tau_R\ge\frac{R}{2C}e^{c\Psi(R)}.
\]
For large $n$, take the real threshold $R=M_n/2$. Since $\tau_{2R}\le n$, this gives $\Psi(M_n)\le C'\log n$. This argument also proves (15) from the one-sided exponential increment bound; for that use only the upper-bound crossing argument, with the assertion trivial if a threshold is never reached.

Applying this to (21), (29), and (10) gives
\[
 \Phi(M_n)\asymp\log n.
\]
If $L\to\infty$, then
\[
 \Phi\left(L^{1/p}(\log L)^{(p-1)/p}\right)\asymp L,
\]
because the logarithm of its argument is asymptotic to $(\log L)/p$. This proves (2), including both powers of the logarithms.

## 7. Secondary question: $0<\gamma<1$

The assumed two-sided stretched-exponential lower tail and exponential upper tail imply
\[
 \mathbb E\exp(b|\eta(0)|^\gamma)<\infty \tag{31}
\]
for some $b>0$, and all ordinary moments are finite. They do not imply an exponential moment of $|\eta|$, and none is used in this section.

We first prove the concentration statement needed in place of (14). Let $F$ depend on finitely many independent copies of a variable satisfying (31), and have deterministic coordinate Lipschitz constants $\ell_i$ such that
$\sum_i\ell_i^2\le S$ and $\max_i\ell_i\le L$, with fixed finite $S,L$. Then, uniformly over the number of coordinates,
\[
 \mathbb P(|F-\mathbb EF|>s)\le C e^{-cs^\gamma},\qquad s\ge1. \tag{32}
\]

To prove it, let $D_i$ be the Doob differences and ignore coordinates with $\ell_i=0$. Conditionally on the preceding coordinates, $D_i$ is a centered $\ell_i$-Lipschitz function of a fresh input. For a Lipschitz function $h$,
$|h(\eta)-\mathbb Eh(\eta)|\le\ell_i(|\eta|+\mathbb E|\eta|)$.
Since $(a+b)^\gamma\le a^\gamma+b^\gamma$, (31) therefore gives, with fixed constants $K,b_1>0$,
\[
 \mathbb E\left[\exp\{b_1(|D_i|/\ell_i)^\gamma\}\mid\mathcal F_{i-1}\right]\le K. \tag{33}
\]
In particular, the conditional tail is bounded by $K e^{-b_1(t/\ell_i)^\gamma}$.

Fix $s\ge1$, choose a small $b_2>0$ with $b_2L^\gamma\le b_1/2$, and set $\lambda=b_2s^{\gamma-1}$. For $|D_i|\le s$,
\[
 \lambda|D_i|\le b_2|D_i|^\gamma
       \le(b_1/2)(|D_i|/\ell_i)^\gamma.
\]
Consequently (33), and boundedness of $z^2e^{-(b_1/2)z^\gamma}$, imply
\[
 \mathbb E[D_i^2e^{\lambda|D_i|}1_{\{|D_i|\le s\}}\mid\mathcal F_{i-1}]
       \le C\ell_i^2.
\]
Also, by (33),
\[
 T_i:=\mathbb E[|D_i|1_{\{|D_i|>s\}}\mid\mathcal F_{i-1}]
 \le C\ell_i e^{-b_3(s/\ell_i)^\gamma}. \tag{34}
\]
One can take a deterministic right-hand side in (34). Splitting its exponential into two factors shows, uniformly for $s\ge1$ and $0<\ell_i\le L$,
\[
 \sum_i K e^{-b_1(s/\ell_i)^\gamma}\le C S e^{-c s^\gamma},
 \qquad\sum_i T_i\le C S e^{-c s^\gamma}. \tag{35}
\]
For example, use $(s/\ell_i)^\gamma\ge s^\gamma/L^\gamma$ in one factor and $e^{-b/(2\ell_i^\gamma)}\le C\ell_i^2$ in the other. For the second estimate use $\ell_i e^{-b/(2\ell_i^\gamma)}\le C\ell_i^2$. Constants depend on $L,b,\gamma$, not the number of coordinates.

Using $e^z\le1+z+\tfrac12z^2e^{|z|}$ and conditional mean zero gives
\[
 \mathbb E[e^{\lambda D_i}1_{\{|D_i|\le s\}}\mid\mathcal F_{i-1}]
       \le\exp(\lambda T_i+C\lambda^2\ell_i^2).
\]
Iterate this bound, retaining the product of the truncation indicators. The probability of any discarded large difference is bounded by (35). On the event that no difference was discarded, exponential Markov gives
\[
 \mathbb P\left(\sum_iD_i>s\right)
 \le CS e^{-cs^\gamma}
   +\exp[-\lambda s+C\lambda^2S+\lambda CS e^{-cs^\gamma}]
 \le C'e^{-c's^\gamma}.
\]
Here $\lambda s=b_2s^\gamma$ and $\lambda\le b_2$, so all positive terms in the last exponent are bounded constants. Apply the same argument to $-F$ to obtain (32). This proof avoids an invalid use of exponential-moment Bernstein bounds for the untruncated scenery.

Apply (32) to $A_n$, using (11)–(12). Its coordinate constants are bounded by $G$, whose squared sum and supremum are fixed. Thus (9) and a stretched-exponential tail integral give
\[
 M_{n+1}-M_n\le C e^{-c M_n^\gamma}. \tag{36}
\]
The tail integral's polynomial factor $O((1+M_n)^{1-\gamma})$ is absorbed by decreasing the positive constant in the exponent.

For the lower bound define $H=4d(M_n+1)$. Union bound and Markov give
\[
 \mathbb P(u_n(e)\le H\text{ for every }e\sim0)
 \ge1-\frac{2dM_n}{H}\ge\frac12.
\]
This event and $\{\eta(0)\le-H-1\}$ are decreasing, so positive association gives their joint probability at least half the latter probability. On their intersection $A_n\le-1$. The lower-tail hypothesis therefore yields
\[
 M_{n+1}-M_n\ge c e^{-C(1+M_n)^\gamma}. \tag{37}
\]
Use Section 6 with $\Psi(s)=(1+s)^\gamma$, together with (10), (36), and (37), to prove (4).

The one-site variational check agrees: for nonnegative depths and weights with maximum $w_*$,
$(\sum w_ya_y)^\gamma\le w_*^\gamma\sum a_y^\gamma$. Thus the finite pure-power minimum is exactly $(m/w_*)^\gamma$, attained at a site of maximum weight. Unlike the critical convex case, splitting the deficit cannot reduce this power cost. This observation is only a check; (32), (36), and (37) are the proof for the odometer.

## 8. Checks and literature search

The proof uses the exact recurrence, not a scaling-limit approximation. The load-bearing identities were checked in two forms: Hölder and Fenchel duality for the cost; Laplace optimization and radial profiles for its logarithmic power; the exact paired finite-difference identity and direct coordinate differences for the barrier; and threshold crossing and direct asymptotic substitution for inversion of the mean scale. The boundary event was kept in the probability calculation rather than treated as independent of the holes. The finite-time smoothing argument checks both time indices, mean loss $h/8$, the $7h/16$ split, the range $h\le\sqrt n$, and the remaining tail.

`code/check_variational.py` performs deterministic numerical checks only. All 20 finite Hölder optimizer checks passed, including algebraic examples in dimensions 3 and 4. These low-dimensional examples check the finite variational identity only; they do not extend the high-dimensional odometer theorem to dimensions 3 or 4. The 12 radial $a^2+a^p$ calculations in $d=5,6,8$ agree with the predicted cost and were repeated with twice the quadrature resolution. The largest relative cost change was below $7\times10^{-8}$; the maximum relative Euler-equation residual was below $4\times10^{-15}$. The radial weights are explicitly proxy kernels, not numerically evaluated lattice Green functions.

The discrete logarithmic-barrier identity was checked at 201, 625, 2,197, and 16,807 points in dimensions 1, 2, 3, and 5 respectively. The direct and paired formulas agreed within $2.1\times10^{-15}$. Nine finite one-site comparisons for $\gamma<1$ also passed. Detailed values are in `data/*.csv`; runtime and memory measurements are in `data/check_summary.json`. There were zero random samples. The run used one thread, inherited nice 10, and about 15.5 MB peak RSS, far below 4 GB. The sandbox refused an OS address-space-limit change; the report does not claim that such a limit was installed.

Literature search was performed on 13 November 2026. Queries included the exact titles and identifier, `divisible sandpile lower tail critical exponent gamma d/2 2026`, `2609.02829 critical lower tail logarithm`, exact borderline/gamma variants, and `divisible sandpile log log`. Both current arXiv records and both authors' publication pages were checked: [Bou-Rabee](https://nitromannitol.github.io/) and [Panagiotis](https://sites.google.com/view/christoforos-panagiotis/). The records listed only v1, and no later paper settling this endpoint was found. This is a search result, not proof that no such work exists. Search-engine summaries that state the noncritical formula without its exclusion were not used as mathematical evidence. The classification is therefore based on the proof in this report, not `RESOLVED_IN_LITERATURE`.

No publication, push, external message, or shared-state edit was made. Files produced for this task are confined to this directory. `LOG.md` contains the work record; `code/` contains the source retrieval and deterministic checks; `data/` contains provenance and numerical output; `sources/` contains plain text only.

Task: “Open problem I0006B, a borderline case left open in print.” Received 2026-11-13 at approximately 15:18 Asia/Tbilisi (first recorded shell time 15:18:24).
