PARTIAL

# E0082: bridge constants and the first-passage obstruction

For every fixed real alpha, the bridge mean has the equivalent

\[
 \mathbb E T(\mathrm{BR}^{\alpha,n})\sim n\,c_{\rm BR}(\alpha).
\]

An explicit, convergent series of ordinary finite-dimensional integrals for the constant is given in (10) below. The proof includes convergence of the correctly weighted matching-matrix column sums, a lattice local limit argument, and uniform integrability. It uses a scaling limit to identify the weights; it is not a purely discrete inversion of the matching matrix.

For every fixed alpha<0, the reconstructed internal E0081 argument gives

\[
 c_\alpha n\log n\leq \mathbb E T(\mathrm{FP}^{\alpha,n})
       \leq C_\alpha n\log n.                                      \tag{1}
\]

Consequently, the requested **finite** first-passage limit on the scale n does not exist:

\[
 \lim_{n\to\infty}\frac{\mathbb E T(\mathrm{FP}^{\alpha,n})}{n}=+\infty.
                                                                    \tag{2}
\]

A sharp equivalent on the scale n log n, including a proof of existence or a value of its leading constant, is **not established here**. This is why the status is PARTIAL, rather than PROVED or RESOLVED_IN_LITERATURE. No constant on that scale is claimed from the numerical fits.

The task's premise about the source is incorrect for FP. Theorem 1.8(4), arXiv p. 6, bounds its mean between orders n and n^(5/4). The published chapter, p. 65, explicitly conjectures the n log n order. Internal E0081 concerns the same FP family, not a different one. Its method is credited as internal prior work and re-derived below.

## 1. Definitions, conventions, and exact source statements

Let X_1,X_2,... be independent symmetric signs, S_0=0 and S_j=sum_{i<=j} X_i. Write SW(n) for the paths w(0)=0, w(j)-w(j-1) in {-1,+1}. The source parameter is lambda; this report uses alpha=lambda.

The source's rounding convention, arXiv p. 5, is

\[
 a_n=\begin{cases}
 \lfloor\alpha\sqrt n\rfloor,&\lfloor\alpha\sqrt n\rfloor\equiv n\pmod2,\\
 \lfloor\alpha\sqrt n\rfloor+1,&\text{otherwise}.
 \end{cases}
\]

Thus a_n/sqrt(n) tends to alpha, including alpha=0 along odd n. The families on p. 6 are exactly

\[
 \mathrm{BR}^{\alpha,n}=\{w\in SW(n):w(n)=a_n\},
\]
\[
 \mathrm{FP}^{\alpha,n}=\{w\in SW(n):w(i)>w(n)=a_n\quad(0\leq i\leq n-1)\},
 \qquad\alpha<0.
\]

In particular FP requires a strict minimum at the right endpoint; merely ending at a negative value is insufficient. F_n is the least starting index s>=0 at which the n increments form a word in the specified family, and

\[
 T=n+F_n.
\]

All computations use this ending-time convention.

For a family A^n={A_1^n,...,A_k^n} of distinct words of common length n, the source defines

\[
 \epsilon_l(A_i^n,A_j^n)
 =\boldsymbol1\{A_{i1}^n=A_{j,1+l}^n,\ldots,A_{i,n-l}^n=A_{jn}^n\},
 \quad 0\leq l<n,
\]
\[
 M_{ij}=\sum_{l=0}^{n-1}2^{-l}\epsilon_l(A_i^n,A_j^n).               \tag{3}
\]

Here are the mathematical statements of **Theorem 2.1, p. 7**, transcribed without changing its notation:

1. The matching matrix M(A^n) is invertible and the expected waiting times for patterns in A^n:={A_1^n,...,A_{k(A^n)}^n} are given by

\[
 \left(\frac1{\mathbb ET(A_1^n)},\ldots,
             \frac1{\mathbb ET(A_{k(A^n)}^n)}\right)^T
   =\frac1{2^n}M(A^n)^{-1}(1,\ldots,1)^T.                         \tag{2.3 source}
\]

2. The expected waiting time till one of the patterns in A^n is observed satisfies

\[
 \frac1{\mathbb ET(A^n)}
 =\sum_{l=1}^{k(A^n)}\frac1{\mathbb ET(A_l^n)}
 =\frac1{2^n}(1,\ldots,1)M(A^n)^{-1}(1,\ldots,1)^T.              \tag{2.4 source}
\]

**Open problem 2.3, p. 13** (typography normalized):

Using the matching matrix method as in Theorem 2.1,

1. determine the exact asymptotics for $\mathbb E T(\mathcal{BR}^{\lambda,n})$ where $\lambda\in\mathbb R$, as $n\rightarrow\infty$;
2. determine the exact asymptotics for $\mathbb E T(\mathcal{FP}^{\lambda,n})$ where $\lambda<0$, as $n\rightarrow\infty$.

These appear in the published version as **Theorem 6, equations (8)–(9), p. 57**, and **Open Problem 1, p. 65**. On p. 65, **Conjecture 1 (Peres), equation (30)**, states the two-sided n ln n bound for FP. That is an order conjecture, not an exact equivalent.

There are source errors that matter to using these formulas. In (2.3), the entries cannot generally be reciprocals of the standalone means for the individual words. For {+-, -+}, the matrix is [[1,1/2],[1/2,1]], the printed formula would assign individual mean 6, whereas either individual word has mean 4. The correct entries are first-hit probability divided by the family mean; the final inverse-matrix expression for the family mean is correct. Also the FP count in (2.18) needs |lambda_n|, rather than lambda_n, to be positive. The report uses the corrected probabilistic identities below. The source's Table 1 also fails an elementary exact lower bound; see Section 7.

## 2. The matching system and the measure that must be used

Let pi_j be the probability that the first family word is A_j^n and let e=E T(A^n). Li's gambling argument gives

\[
 M\pi=\frac e{2^n}{\bf1},\qquad {\bf1}^T\pi=1,
 \qquad e=\frac{2^n}{{\bf1}^TM^{-1}{\bf1}}.                       \tag{4}
\]

Equivalently, with the Conway/Li leading-number matrix C=2^n M, e=1/(1^T C^{-1}1). The factor 2^n must not be dropped when M is normalized as in (3).

For completeness, start one unit-stake gambler at each time, betting successively on the letters of target word i, doubling the capital on each correct sign and losing it on the first mismatch. At T the total surviving capital for this target is C_{ij} if the ending word is j: surviving bettors correspond precisely to suffix-prefix matches. Expected capital equals the expected number T of stakes. Optional stopping follows first at T capped by a deterministic time, then by dominated convergence: terminal capital is bounded by 2^(n+1) and e is finite by trials in independent blocks. Thus sum_j C_{ij} pi_j=e. Invertibility is Theorem 2.1's valid algebraic assertion, also supplied by the general pattern theory cited in LITERATURE.md. Summing its inverse system gives (4).

Let p_A=k/2^n and let

\[
 C_n(w_j)=\sum_i M_{ij}.
\]

Summing (4) over rows gives the particularly useful exact identity

\[
                p_A e=\mathbb E_\pi C_n(W).                       \tag{5}
\]

The expectation is over the **first-hit word**, not a uniformly selected family word. Replacing this law by the uniform law is generally invalid. For example, at n=8 and alpha=0 the bridge column means are 3.3458214802 under pi and 3.3837053571 under the uniform law. For FP at n=8, alpha=-1 they are 1.3230921869 and 1.2756696429.

Define, for attainable integer b,

\[
 p_l(b)=2^{-l}\binom l{(l+b)/2},\qquad
 f_l(b)=\frac b l p_l(b)\quad(b>0),
\]

setting unattainable probabilities to zero and p_0(0)=1. By the ballot theorem f_l(b) is the probability that a fresh walk first hits -b at l.

For the two families the column sums are exactly

\[
 C_n^{\rm BR}(w)=\sum_{l=0}^{n-1}p_l(w(l)),                       \tag{6}
\]
\[
 C_n^{\rm FP}(w)=1+\sum_{l=1}^{n-1}
                  \boldsymbol1_{\{w(l)<0\}}f_l(-w(l)).            \tag{7}
\]

Indeed, after a word w has occurred, a new word at shift l keeps its last n-l letters and appends l fresh letters. Its endpoint is correct precisely when those letters sum to w(l). For FP, w(l)<0 is necessary: otherwise the old endpoint is already at or below the proposed new terminal minimum. When w(l)<0, the retained suffix stays above that minimum, and the appended letters must first hit w(l) at their last step. This proves (6)–(7) and recovers source equation (2.21).

## 3. Bridge theorem and its explicit constant

Put phi_t(x)=(2 pi t)^(-1/2) exp(-x^2/(2t)), and phi=phi_1. Let B be standard Brownian motion and

\[
 Z(t)=B(t+1)-B(t),\qquad
 F_\alpha=\inf\{t\geq0:Z(t)=\alpha\}.
\]

The bridge constant is

\[
                     c_{\rm BR}(\alpha)=1+\mathbb E F_\alpha.       \tag{8}
\]

Here is an explicit integral series, so (8) is not the only specification of the constant. For integer m>=0 and 0<theta<1, set x_0=0 and define

\[
 H_h(m+\theta)=
 \int_{0<x_1<\cdots<x_{m+1}}\int_{y_0<\cdots<y_{m+1}}
  \det[\phi_\theta(y_j-x_i)]_{i,j=0}^{m+1}
  \det[\phi_{1-\theta}(x_{j+1}-h-y_i)]_{i,j=0}^{m}
  \,dy_0\cdots dy_{m+1}\,dx_1\cdots dx_{m+1}.                    \tag{9}
\]

These are ordinary Lebesgue integrals of nonnegative functions. Then

\[
 \boxed{\displaystyle
 c_{\rm BR}(\alpha)=1+\sum_{m=0}^{\infty}\int_0^1
                \{H_\alpha(m+\theta)+H_{-\alpha}(m+\theta)\}
                \,d\theta.}                                     \tag{10}
\]

The second determinant has duration **1-theta**, as in Shepp's original equation (2.25), not theta. Equation (9) is the unconditional form of Shepp (1971), equations (2.25)–(2.26), p. 950. The integer counterpart is (2.15)–(2.16), p. 949. The derivation below also verifies the normalization and sign of h.

### 3.1 Proof of bridge convergence and convergence of means

The linearly interpolated S_{nt}/sqrt(n) converges on compact time intervals to B by Donsker's theorem. Consequently its moving increments converge to Z. At consecutive lattice starting times the length-n window sum changes by 0 or +/-2. Since a_n has the correct parity, the interpolated increment first reaches a_n exactly at a lattice time. Thus F_n/n is exactly the first hitting time of a_n/sqrt(n) by the interpolated moving increments.

We check the continuity needed for this hitting functional. On any unit interval, conditional on Z at its two endpoints x,y, the process is a variance-2 Brownian bridge from x to y. To see this on [0,1], write B on its two independent unit increments as U and V. Then

\[
 Z(t)=(1-t)U(1)+tV(1)+\beta_V(t)-\beta_U(t),
\]

where the two beta's are independent standard bridges, independent of U(1),V(1). Their difference is a variance-2 bridge. The joint endpoint density is strictly positive everywhere. The law on the unit interval is therefore mutually absolutely continuous with that of variance-2 Brownian motion started at an independent nondegenerate normal variable: conditional bridge laws agree, and both endpoint densities are positive. This also proves the source's local absolute continuity lemma directly.

Brownian motion crosses a fixed level immediately after its first hit, almost surely, by the strong Markov property and the reflection principle. Local absolute continuity transfers this assertion to Z. Taking the countable collection of unit intervals suffices. Hits at integer endpoints have probability zero. Also F_alpha is finite almost surely, since Z(0),Z(1),... are independent N(0,1) variables and hence take values on both sides of alpha almost surely. For continuous paths which cross immediately at their first hit and start off the level, uniform convergence of paths and convergence of levels imply convergence of first hitting times: compactness excludes a hit a fixed distance before the limiting hit, and the sign change just after it forces a nearby hit. Therefore

\[
 F_n/n\ \Rightarrow\ F_\alpha,
 \qquad
 W_n^*(u):=\frac{S_{F_n+nu}-S_{F_n}}{\sqrt n}
       \ \Rightarrow\ W^*(u):=B(F_\alpha+u)-B(F_\alpha).             \tag{11}
\]

This is joint convergence, including the entire path on [0,1]. W^* is a bridge-like first-hit path, not asserted to be an ordinary uniformly sampled Brownian bridge.

For convergence of means we need more than (11). Let

\[
 q_n=\Pr(S_n<a_n),\qquad r_n=\Pr(S_n>a_n).
\]

The window sums at starts 0,n,2n,... are independent. If F_n>kn, all k+1 such sums must lie strictly on the same side of a_n: any change of side forces a hit by the +/-2 lattice property. Hence

\[
 \Pr(F_n>kn)\leq q_n^{k+1}+r_n^{k+1}.                            \tag{12}
\]

The central limit theorem gives q_n->Phi(alpha), r_n->1-Phi(alpha), both strictly below 1. Thus (12) is a uniform geometric tail for all sufficiently large n. It implies uniform integrability of F_n/n, even uniform boundedness of all its fixed positive moments. Taking expectations in (11) proves (8) and the claimed equivalent. It also proves 1<c_BR(alpha)<infinity and c_BR(alpha)=c_BR(-alpha).

### 3.2 Passing the matching sums to the limit

The span-2 binomial local limit theorem gives

\[
 \sqrt n\,p_n(a_n)\longrightarrow2\phi(\alpha),
 \qquad
 p_l(b)\leq C/\sqrt l.                                          \tag{13}
\]

For l/n in [delta,1], uniformly over attainable b,

\[
 \sqrt n\,p_l(b)=2\phi_{l/n}(b/\sqrt n)+o(1).
\]

For clarity, these elementary local limits follow by inserting Stirling's formula into the binomial coefficient on |b|<=K sqrt(l); outside that range the binomial Gaussian bound controls the tails, and then K tends to infinity. The bound in (13) is also immediate by comparing each binomial coefficient with the central one. A convenient stronger bound used below is p_l(b)<=C l^(-1/2) exp(-c b^2/l). For |b|<=l/2 this follows from Stirling and the entropy bound; for |b|>l/2, the binomial tail estimate absorbs the extra polynomial factor into the exponential.

If scaled lattice paths w_n converge uniformly to w, (6), the uniform local limit on [delta,1], and Riemann sums give

\[
 \frac{C_n^{\rm BR}(w_n)}{\sqrt n}
    \longrightarrow K(w):=2\int_0^1\phi_t(w(t))\,dt.              \tag{14}
\]

Here are the needed domination details. The contribution from l<delta n, including l=0, is at most

\[
 \frac1{\sqrt n}+\frac C{\sqrt n}\sum_{l\leq\delta n}l^{-1/2}
       \leq o(1)+C'\sqrt\delta.
\]

The analogous integral over [0,delta] is at most C' sqrt(delta), uniformly in w. On [delta,1], uniform convergence of paths and the local limit justify the Riemann limit. Sending delta down to zero proves (14), and also shows K is a bounded continuous functional under uniform path convergence. In particular C_n^{BR}/sqrt(n) is uniformly bounded.

Apply (14) to the first-hit paths (11), then take expectations by bounded convergence in a Skorokhod coupling, or equivalently by the bounded continuous mapping argument. The exact identity (5), with p_A=p_n(a_n), now yields

\[
 \lim_n\frac{\mathbb ET(\mathrm{BR}^{\alpha,n})}{n}
  =\frac{\mathbb E K(W^*)}{2\phi(\alpha)}
  =\frac1{\phi(\alpha)}\mathbb E\int_0^1\phi_t(W^*(t))\,dt.        \tag{15}
\]

As a check on the importance of the weights, replace W^* at alpha=0 by an ordinary Brownian bridge U. Since U(t) has variance t(1-t),

\[
 \mathbb E\phi_t(U(t))=\frac1{\sqrt{2\pi t(2-t)}},
 \qquad
 \frac1{\phi(0)}\mathbb E\int_0^1\phi_t(U(t))dt=\frac\pi2.
\]

That uniform-bridge calculation gives a different constant from the first-hit calculation (approximately 1.544). It is therefore not an admissible replacement of the weights in (15).

Together with (8), this evaluates the limit of the inverse-matrix sum as well:

\[
 \frac n{2^n}{\bf1}^TM_n^{-1}{\bf1}\longrightarrow1/c_{\rm BR}(\alpha).
\]

Thus the matching sums do pass to the limit. Their weights were identified through (11), not replaced by uniform bridge weights. The independent tail proof in Section 3.1 checks that the constant in (15) is the same as the explicit series (10).

### 3.3 Proof of the explicit integral series

It suffices to use the identically distributed process Z'(t)=B(t)-B(t+1). The event Z'(t)<h on [0,m+theta] is equivalent to ordering the following Brownian pieces:

* on [0,theta], B(i+t)+ih, i=0,...,m+1, are in increasing order;
* on [theta,1], B(i+t)+ih, i=0,...,m, are in increasing order.

Set x_i=B(i)+ih, y_i=B(i+theta)+ih. Then x_0=0, and ordering requires 0<x_1<...<x_{m+1} and y_0<...<y_{m+1}. Conditional on these endpoints, all the Brownian bridge pieces are independent. Their noncollision transition densities are the two determinants in (9).

To verify that fact without an additional black box: for independent Brownian motions with ordered starts u_i and ordered ends v_i, expand det[phi_t(v_j-u_i)] over permutations. Reflect and exchange the tails of the first pair that collide. This is a measure-preserving, sign-reversing pairing of the colliding paths ending in different permutations. The unpaired paths never collide and end in the identity order. Thus the determinant is exactly their transition density. Applying this reflection argument separately to the two disjoint collections of time pieces gives (9), with no missing density factor: the determinants already contain the unconditional densities of all the Brownian increments. The second group ends at x_{i+1}-h, which explains the sign and duration in its kernel.

Consequently H_h(t)=Pr(Z'(u)<h for every 0<=u<=t). Since Z' is continuous, avoiding alpha throughout an interval means staying wholly below or wholly above it. Symmetry therefore gives

\[
 \Pr(F_\alpha>t)=H_\alpha(t)+H_{-\alpha}(t).
\]

The level-touching boundary events have probability zero for deterministic t, by the local absolute continuity argument in Section 3.1. Integrating this tail probability proves (10), by Tonelli's theorem. Convergence is explicit: evaluating Z' at integers shows

\[
 H_h(t)\leq\Phi(h)^{\lfloor t\rfloor+1}.
\]

A sharper tail bound is useful numerically. Shepp's t=1 formula, or the two-bridge reflection calculation, gives

\[
 r_h:=H_h(1)=\Phi(h)^2-h\phi(h)\Phi(h)-\phi(h)^2.                  \tag{16}
\]

For example it follows by integrating
Q_h(1|x)=Phi(h)-phi(h)Phi(x)/phi(x), x<h, against phi(x)dx.
The events of staying below h on [0,1],[2,3],... use disjoint Brownian increments. Hence H_h(t)<=r_h^{floor((t+1)/2)}. After M complete slabs, the omitted part for one h is bounded by

\[
 R_h(M)=\begin{cases}
 r_h^{M/2}(1+r_h)/(1-r_h),&M\text{ even},\\
 2r_h^{(M+1)/2}/(1-r_h),&M\text{ odd}.
 \end{cases}                                                     \tag{17}
\]

The omitted part of (10) is at most R_alpha(M)+R_{-alpha}(M). This bound does not include quadrature error.

## 4. First passage: complete proof of the n log n order

Write a=-a_n>0 for the positive discrete drop; in this section a/sqrt(n)->|alpha|. Constants may depend on fixed alpha. Put m=floor(n/2), and let A_s denote an FP occurrence starting at s. By the ballot theorem and (13),

\[
 \Pr(A_s)=f_n(a)\sim\sqrt{2/\pi}\,|\alpha|e^{-\alpha^2/2}/n.
                                                                    \tag{18}
\]

Let q=Pr(union_{s=0}^m A_s). We prove c/log n<=q<=C/log n and then translate this into waiting times.

### 4.1 The return potential at record times

Let X,Y be independent simple symmetric walks starting at zero. A time j>=1 is a descending record of Y when Y_j<min_{0<=i<j}Y_i; time zero is included by convention. Set

\[
 g_j=\Pr(j\text{ is a descending record of }Y,\ X_j=Y_j)
     =\sum_{b>0} f_j(b)p_j(b)
     =\frac1j\sum_{b>0}b\,p_j(b)^2.                              \tag{19}
\]

The span-2 local limit, including parity, gives

\[
                 g_j\sim\frac1{2\pi j},\qquad
 G_m:=1+\sum_{j=1}^m g_j\sim\frac{\log m}{2\pi}.                \tag{20}
\]

To check the coefficient, put x=b/sqrt(j) and sum with mesh 2/sqrt(j). Then

\[
 \sum_{b>0}b\,p_j(b)^2
   \longrightarrow2\int_0^\infty x\phi(x)^2\,dx=\frac1{2\pi}.
\]

The Gaussian binomial bound in Section 3.2 dominates the tails of this Riemann sum. The finitely many small j do not affect the logarithmic equivalent. This proves (20), rather than assuming a continuum approximation at time zero.

Let R_m be the number of distinct values of X_j-Y_j attained at descending records j<=m of Y. Let V_L be the total number of records of Y up to L, including zero. The ballot identity implies

\[
 \mathbb EV_L=1+\sum_{j=1}^L\sum_{b>0}\frac b j p_j(b)
       \leq1+\sum_{j=1}^L j^{-1/2}\leq C\sqrt{L+1}.              \tag{21}
\]

For each integer z, let sigma_z be its first attainment by X-Y at a record of Y. This is a stopping time for the joint walk. At sigma_z, Y is at its running minimum. Conditional on sigma_z<=m, the subsequent increments of X,Y are fresh independent walks. Their expected number of future visits to z at records, during the next m steps including the starting visit, is exactly G_m. All these visits occur before 2m. Counting each record under its unique value z, and using nonnegativity to sum over z, gives

\[
 G_m\mathbb ER_m
 =\sum_z\Pr(\sigma_z\leq m)G_m
 \leq\mathbb EV_{2m}\leq C\sqrt m.
\]

Thus

\[
                     \mathbb ER_m\leq C\sqrt m/\log m.           \tag{22}
\]

This is the record-range argument reconstructed from internal E0081.

### 4.2 Upper bound on the probability of any FP in a block

Split the original walk into X_s=S_s (s<=m), the independent middle increment D=S_n-S_m, and Y_s=S_{n+s}-S_n (s<=m). These three objects are independent. If A_s occurs, the part of its window after time n forces s to be a descending record of Y (or s=0). Its prescribed endpoint also forces

\[
                     D=X_s-Y_s-X_m-a.
\]

Condition on the full X,Y paths. The possible right sides, as s runs over records, have at most R_m distinct values. Every point mass of D is at most C/sqrt(n-m)<=C'/sqrt(n). Therefore, by (22),

\[
                     q\leq C\mathbb ER_m/\sqrt n
                        \leq C'/\log n.                          \tag{23}
\]

Only a necessary part of the first-passage condition was used, so the inequality has the correct direction. It is not a sharp block-probability equivalent.

### 4.3 Lower bound on the block probability from the overlaps

Let N=sum_{s=0}^m 1_{A_s}. Equation (18) gives EN=(m+1)f_n(a)>=c_alpha>0 for sufficiently large n. At the first success, whose ending time is a stopping time, the word w is known and future signs are independent. At shift l<n the probability of another success is exactly the term in (7). The Gaussian binomial bound gives, uniformly over b>0,

\[
                     f_l(b)\leq C/l.                             \tag{24}
\]

Indeed b p_l(b)/l <= (C/l)(b/sqrt(l))exp(-c b^2/l), whose last factor is bounded. Conditional on the first success, the expected number of successes through the end of this block, including the first, is at most 1+C sum_{l=1}^m 1/l<=C' log n. Before the first success there are none. Hence

\[
           c_\alpha\leq\mathbb EN\leq q C'\log n,
           \qquad q\geq c'_\alpha/\log n.                        \tag{25}
\]

This uses the exact matching overlap probabilities, not independent-window heuristics.

### 4.4 From block probabilities to waiting-time bounds

For the upper bound on ET, test the event in (25) in successive disjoint pieces of the increment sequence of length n+m. Those tests are independent. Each has success probability q, and a success completes a pattern within that piece. Thus

\[
                    \mathbb ET\leq(n+m)/q\leq C_\alpha n\log n.
\]

For the lower bound, cover starting indices through K m by at most K+1 blocks of m+1 consecutive starts. Stationarity and (23), with a union bound, give

\[
 \Pr(F_n\leq Km)\leq(K+1)C/\log n.
\]

Taking K to be a sufficiently small positive constant times log n makes this at most 1/2. Then EF_n>=Km/2>=c n log n for all sufficiently large n. Since T=n+F_n, this proves (1) and (2).

No step above gives equality of the upper and lower constants. In particular G_m's exact coefficient in (20) does not by itself determine the sharp mean constant.

## 5. Why the proposed FP dominated-convergence argument fails

For l/n->t>0 and scaled w(l)->w(t), (7) formally has the continuum kernel

\[
                 2\boldsymbol1_{\{w(t)<0\}}f_t(-w(t)),
 \qquad f_t(b)=\frac b t\phi_t(b)\quad(b>0).                      \tag{26}
\]

This kernel is critical at t=0. For an unrestricted Brownian initial segment,

\[
 \mathbb E\{2\boldsymbol1_{\{B_t<0\}}f_t(-B_t)\}
     =\frac2t\int_0^\infty b\phi_t(b)^2\,db
     =\frac1{2\pi t}.                                           \tag{27}
\]

It is not integrable at zero. An ordinary Brownian first-passage bridge ending at fixed -|alpha| is locally absolutely continuous with respect to Brownian motion, with initial-segment likelihood tending to 1 as its duration tends to zero. Thus it has the same singular expectation to leading order. There is no counterpart to the uniform C sqrt(delta) error used for bridges.

One can make this precise directly in the discrete matrix. If U_n is a **uniform** FP word with drop a, then

\[
              \mathbb EC_n^{\rm FP}(U_n)\sim\frac{\log n}{2\pi}.
                                                                    \tag{28}
\]

Here is a proof, included to isolate the obstruction rather than confuse U_n with the first-hit law. For b=1,...,a-1, the reflection principle gives

\[
 \Pr(U_n(l)=-b)
  =\frac{[p_l(b)-p_l(2a-b)]f_{n-l}(a-b)}{f_n(a)}.                 \tag{29}
\]

For l<=delta n, l sufficiently large, and b<=K sqrt(l), first let n tend to infinity. The local limits show that the multiplier of p_l(b) on the right of (29) tends uniformly to 1 as delta tends to zero: b/a<=C_alpha K sqrt(delta), and the reflected term is exponentially small in a^2/l. This remains valid for attainable parities. More explicitly the unreflected likelihood ratio has leading expression

\[
 \frac{a-b}{a}\left(\frac n{n-l}\right)^{3/2}
    \exp\!\left(\frac{a^2}{2n}-\frac{(a-b)^2}{2(n-l)}\right),
\]

which tends uniformly to 1 in this range as delta tends to zero. For all b and l<=delta n<=n/2 this likelihood ratio is bounded by a constant depending on alpha: f_{n-l}<=C/n and f_n(a)>=c_alpha/n. Gaussian bounds then make the contribution from b>K sqrt(l), to l times the expected summand in (7), at most C_alpha exp(-c K^2). The finitely many small l contribute O(1). By (19)–(20), summing the remaining range gives coefficient 1/(2 pi) in front of log n, first taking n large, then K large and delta small. Finally l>=delta n contributes at most sum C/l<=C log(1/delta), by (24), independent of n. This proves (28).

Equation (28) is an averaged column-sum asymptotic, not an asymptotic for the inverse matrix. The first-hit distribution pi in (5) still has to be controlled on the logarithmic boundary layer. A uniform-word average or an ordinary Brownian first-passage bridge cannot be silently substituted for it. Resolving that issue sharply is the remaining part of E0082 in this report.

## 6. Numerical checks and reproducibility

All computations are evidence only. Exact rational arithmetic is identified separately from solving exact equations in floating point. No Monte Carlo value is used to prove a limit.

`code/exact_waiting.py` enumerates words, constructs C=2^n M with integer entries, and computes 1/(1^T C^{-1}1). For n=2,...,8 it also computes that rational number using fraction-free symbolic matrix inversion. For n=10,12 it solves in float64. It independently solves a sliding-window Markov chain whose states are the last n-1 bits. Initial averaging includes the first n-1 steps, giving ET=n-1+mean(h). Counts are checked against the binomial/ballot counts, and first-hit probabilities and identity (5) are checked. Results: `data/exact_waiting.csv`.

Selected exact rational results:

| n | family and parameter | E T |
|---:|:---|:---|
| 2 | BR, alpha=0 | 3 |
| 4 | BR, alpha=0 | 85/14 |
| 6 | BR, alpha=0 | 836953/91448 |
| 8 | BR, alpha=0 | 4610050917991422781/376756741306885616 |
| 4 | FP, alpha=-1 | 34/3 |
| 6 | FP, alpha=-1 | 296/17 |
| 8 | FP, alpha=-1 | 68202/2819 |

The n=12 floating solutions are 18.407555804650993 for BR alpha=0, 32.455292213965286 for BR alpha=1 (a_n=4), and 43.51636509590973 for FP alpha=-1 (a_n=-4). These are deterministic solutions of the finite exact equations, not exact decimal expansions. Their independent Markov-chain values agree to numerical precision.

`code/simulate.cpp` performs uncensored sequential simulation. A ring buffer tracks the endpoint difference. For FP, a monotone deque maintains the minimum over the n preceding prefix values, so the strict first-passage condition is tested exactly in O(1) amortized work per sign. It uses one thread and O(n) memory. Seeds, sample counts, ending-time means, and standard errors are saved in `data/monte_carlo.csv`; the driver is `code/run_simulations.py`. Gaussian-increment runs detect sign crossings of the sampled Slepian process and therefore retain a finite-grid upward bias.

`code/slepian_integrals.py` numerically evaluates (10) by conditioning on Brownian values at integers and integers+theta, then integrating the two conditional noncollision determinant probabilities. Randomized Sobol quadrature averages theta as another integration coordinate. This evaluates continuous-time crossing probabilities and avoids the time-grid bias of the Gaussian simulation. Eight independent scrambles, 16384 points per slab, are used. Scramble variation estimates quadrature variability; it is **not a certified error bound**. The analytic omitted-tail bound (17) is reported separately. Slab and constant data are in `data/slepian_slabs.csv` and `data/slepian_constants.csv`.

The integral evaluations give:

| alpha | estimated c_BR(alpha) | scramble standard error | proved omitted-tail bound |
|---:|---:|---:|---:|
| 0 | 1.5438789 | 0.0001901 | 0.00000135 |
| 1 | 2.4135127 | 0.0006130 | 0.00007150 |

These are numerical estimates, not certified decimal constants. The analytic tail bound controls only the omitted integrals, not the quadrature error. An independent check is available for alpha=0: on 0<t<1, the first-zero density is pi^(-1) sqrt((2-t)/t), giving

    integral_0^1 Pr(F_0>t) dt = 3/4 - 1/pi = 0.4316901138162093.

The first slab of the numerical integration is 0.4315716777 with scramble standard error 0.0001162559, a difference of 1.02 such errors. The same density follows by the variance-2 bridge reflection calculation used above.

Here are the uncensored sign-walk estimates of ET/n. The displayed errors are one sampling standard error:

| n | BR, alpha=0 | BR, alpha=1 | FP, alpha=-1 |
|---:|---:|---:|---:|
| 64 | 1.53510 +/- 0.00446 | 2.40814 +/- 0.01204 | 3.98695 +/- 0.02121 |
| 256 | 1.55300 +/- 0.00522 | 2.40576 +/- 0.01363 | 4.46768 +/- 0.02811 |
| 1024 | 1.53448 +/- 0.00614 | 2.40116 +/- 0.01663 | 4.91409 +/- 0.03902 |
| 4096 | 1.55292 +/- 0.00899 | 2.39829 +/- 0.02407 | 5.39219 +/- 0.06192 |
| 16384 | 1.52612 +/- 0.01241 | 2.41599 +/- 0.03364 | 5.82309 +/- 0.09558 |
| 65536 | 1.55228 +/- 0.01909 | 2.42099 +/- 0.04765 | 6.25536 +/- 0.15340 |

The bridge values are consistent with (10). The FP values increase on the scale n, as (1) requires. Slow logarithmic growth makes a fitted power exponent misleading; no finite FP constant on the scale n is estimated.

Validation checked 2317 words across all attainable endpoints for n=2,...,10: the enumerated matrix column sums agree exactly with (6) and (7). All 27 finite-family rows passed the independent Markov-chain comparison; 21 are exact rational calculations. The largest matching/Markov difference was 2.14e-14 and the largest first-hit-system residual was 2.07e-13. The three n=8 Monte Carlo comparisons were within 0.49 sampling standard errors of their exact means. At m=16384, m*g_m=0.1591500861, close to 1/(2 pi)=0.1591549431; return-potential checkpoints are in data/return_potential.csv.

The full validation record is data/validation.json. During the first numerical pass the Mac's Accelerate matmul reported spurious floating-point flags on vector products whose results were finite and agreed with the independent calculation. Those validation contractions were changed to explicit einsum, and the finite-matrix run was repeated without warnings.

Reproduction, from this directory:

```sh
python3 code/exact_waiting.py
c++ -O3 -std=c++17 code/simulate.cpp -o code/simulate
python3 code/run_simulations.py
python3 code/slepian_integrals.py
python3 code/validate.py
```

All scripts inherit nice=10 in this run; validation records it. The Python numerical scripts set native thread limits to one before importing NumPy/SciPy; C++ is single-threaded. Largest explicitly constructed dense matrices are 924 by 924; quadrature determinants are processed in batches of at most 1024, and the Monte Carlo ring/deque sizes are O(n), with n<=65536. These choices stay far below the 4 GB budget. Source PDFs were fetched into memory and converted through standard input, with only plain text saved in sources/. The artifact audit found no PDFs, paper page images, or scans in this directory.


## 7. Literature result and remaining work

The literature search and access limitations are documented in LITERATURE.md. The exact requested discrete equivalents were not found printed in the checked works. In particular, Shepp (1971), equations (2.15)–(2.16), p. 949, and (2.25)–(2.26), p. 950, provide the continuum probability integrals used here; they do not state the discrete limits. Pitman–Tang's published Theorem 6 is on p. 57, Open Problem 1 on p. 65, and Peres's n log n order conjecture is Conjecture 1, equation (30), on p. 65. No literature resolution is claimed from an inaccessible original theorem.

The source table cannot validate this calculation. The exact matching identity (5), or the gambler argument with C_n>=1, gives ET(FP)>=1/f_n(a). At alpha=-1, n=100, a=10, the lower bound is 206.2948964, whereas the source reports 179.805. The n=100,200,500,1000,2000 comparisons all fail in this direction; their exact lower-bound evaluations are saved by the validation script. The discrepancy is not used to infer its cause.

The bridge equivalent, its explicit integral constant, and the FP n log n order are proved above. A sharp FP leading constant, or an alternative sharp asymptotic if a constant fails to exist, remains open in this work. It would require control of the actual first-hit word law in (5) across the short-overlap scales. No publication or push was made.

Task: “Open problem E0082.” Received 13 November 2026, approximately 10:34 Asia/Tbilisi (the original message supplied no seconds).
