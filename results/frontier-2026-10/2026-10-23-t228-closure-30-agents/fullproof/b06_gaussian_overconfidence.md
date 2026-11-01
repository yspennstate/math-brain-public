# Gaussian logistic scores: strict overconfidence at the risk-optimal scale

24 October 2026. Independent proof and scope audit by B06.

This note proves the scalar lemma requested for the ordinary Gaussian random-feature model. It verifies, with an elementary integral argument, the single-crossing assertion suggested in `a03/rows_T357_DOSSIER.md` on 20 October at 17:34. It does not assume that assertion or invoke an unverified total-positivity theorem. The normal-mixture representation of the logistic law is classical; a derivation is included. No publication-novelty claim is made.

## 1. Statement

Let $Z,G$ be independent standard normal variables, let $k,\tau,\beta>0$, and put

\[
U=kZ+\tau G,\qquad V=k^2+\tau^2.
\tag{1}
\]

Given $Z$, let $Y$ be Bernoulli with mean $\sigma(\beta Z)$, independently of $G$, where $\sigma(x)=(1+e^{-x})^{-1}$. Its conditional regression given the score coordinate is

\[
g(u):=\mathbb E[Y\mid U=u]
=\mathbb E_H\sigma(\lambda u+sH),\qquad
\lambda=\frac{\beta k}{V},\quad s=\frac{\beta\tau}{\sqrt V},
\tag{2}
\]

with $H$ standard normal. Consider the positive-scale predictors $p_c(u)=\sigma(cu)$ and their population cross-entropy

\[
R(c)=\mathbb E\{\log(1+e^{cU})-cU g(U)\}.
\tag{3}
\]

**Theorem.** For every $k,\tau,\beta>0$:

1. The function
   \[
   h(u)=\frac{\operatorname{logit}g(u)}u,\qquad u>0,
   \tag{4}
   \]
   is continuous and strictly increasing, with endpoint limits
   \[
   h(0+)=4g'(0)=4\lambda\mathbb E\sigma'(sH),
   \qquad h(+\infty)=\lambda.
   \tag{5}
   \]
2. $R$ has a unique global minimizer $c_*$, and
   \[
   4g'(0)<c_*<\lambda,\qquad R(c_*)<R(0)=\log2.
   \tag{6}
   \]
3. There is a unique $u_*>0$ such that
   \[
   \sigma(c_*u)-g(u)
   \begin{cases}>0,&0<u<u_*,\\=0,&u=u_*,\\<0,&u>u_*.
   \end{cases}
   \tag{7}
   \]
4. The average signed overconfidence is strictly positive:
   \[
   \operatorname{OC}(c_*):=
   \mathbb E\big[(\sigma(c_*U)-g(U))\operatorname{sign}U\big]>0.
   \tag{8}
   \]

Here the predicted class is $\mathbf1_{\{U>0\}}$, its confidence is $\sigma(c_*|U|)$, and its conditional probability of being correct is $g(|U|)$. With $S=c_*U$, conditioning on $U$ gives the equivalent exact definition

\[
\operatorname{OC}(c_*)=\mathbb E[(\sigma(S)-\sigma(\beta Z))\operatorname{sign}S].
\]

Thus (8) is exactly mean confidence minus mean accuracy. It is not a claim of overconfidence at every score: (7) proves underconfidence in the far tails.

## 2. Logistic noise as a normal variance mixture

Let $E_1,E_2,\ldots$ be independent exponential variables of mean one, and define

\[
W=2\sum_{j=1}^{\infty}\frac{E_j}{j^2}.
\tag{9}
\]

The series is finite almost surely, because its expectation is $2\sum j^{-2}=\pi^2/3<\infty$. If $N$ is an independent standard normal variable, the characteristic function of $\sqrt W N$ is

\[
\mathbb E e^{-t^2W/2}
=\prod_{j=1}^{\infty}(1+t^2/j^2)^{-1}
=\frac{\pi t}{\sinh(\pi t)},
\tag{10}
\]

with the continuous value one at $t=0$. The last identity is Euler's product for $\sinh$. On the other hand, the characteristic function of a standard logistic variable $L$ is

\[
\int_{-\infty}^{\infty}e^{itx}\frac{e^x}{(1+e^x)^2}\,dx
=\int_0^{\infty}\frac{r^{it}}{(1+r)^2}\,dr
=\Gamma(1+it)\Gamma(1-it)
=\frac{\pi t}{\sinh(\pi t)}.
\tag{11}
\]

The middle equality is the beta integral, and the last follows from the gamma reflection identity. Uniqueness of characteristic functions therefore proves

\[
L\ \overset d=\ \sqrt W N.
\tag{12}
\]

We also need strict support, not just a formal mixture. Write $W=2E_1+Q$, where $Q=2\sum_{j\ge2}E_j/j^2$. For every $w>0$, $\mathbb P(Q<w)>0$: choose a finite cutoff whose remaining tail has expectation less than $w/4$; the tail is below $w/2$ with positive probability by Markov's inequality, and the finite initial sum is below $w/2$ with positive probability, independently. Conditioning on $Q$ gives the density

\[
f_W(w)=\frac12 e^{-w/2}
\mathbb E\big[e^{Q/2}\mathbf1_{\{Q<w\}}\big]>0
\quad(w>0).
\tag{13}
\]

It is finite, since the integrand is bounded by $e^{w/2}$. Hence the CDF $F_W$ is strictly increasing on $(0,\infty)$, is positive at every positive argument, and vanishes at nonpositive arguments.

## 3. A direct strict single-crossing argument

For $s>0$, write

\[
F_s(x)=\mathbb E\sigma(x+sH),\qquad
\Lambda_s(x)=\operatorname{logit}F_s(x).
\tag{14}
\]

By symmetry of $H$, $F_s$ is the CDF of $L+sH$. Conditional on $W$, this is a centered normal variable of variance $W+s^2$. Consequently

\[
F_s(x)=\mathbb E\Phi\left(\frac{x}{\sqrt{W+s^2}}\right),
\qquad
\sigma(cx)=\mathbb E\Phi\left(\frac{x}{\sqrt W/c}\right)
\quad(c>0).
\tag{15}
\]

Set $x=e^t$. The difference of the CDFs of the logarithms of the two random scales in (15) is

\[
N_c(u)
=F_W(e^{2u}-s^2)-F_W(c^2e^{2u}).
\tag{16}
\]

Integration by parts yields

\[
D_c(t):=F_s(e^t)-\sigma(ce^t)
=\int_{\mathbb R}K(t-u)N_c(u)\,du,
\qquad K(v)=e^v\varphi(e^v).
\tag{17}
\]

For completeness, the function being integrated against the signed scale law is $u\mapsto\Phi(e^{t-u})$; its derivative is $-K(t-u)$. The boundary terms vanish because $N_c(u)\to0$ at both ends. The integral is absolutely convergent: $|N_c|\le1$ and $\int K(v)\,dv=1/2$.

If $c\ge1$, (13) and (16) give $N_c(u)<0$ for every finite $u$; hence $D_c(t)<0$ for every $t$. In particular

\[
\tfrac12<F_s(x)<\sigma(x)\quad(x>0).
\tag{18}
\]

The first strict inequality follows from symmetry and strict monotonicity of $F_s$.

For $0<c<1$, put

\[
u_c=\frac12\log\frac{s^2}{1-c^2}.
\tag{19}
\]

Strict monotonicity of $F_W$ implies

\[
N_c(u)<0\ (u<u_c),\qquad
N_c(u_c)=0,\qquad
N_c(u)>0\ (u>u_c).
\tag{20}
\]

For any $t_2>t_1$, the kernel ratio

\[
Q(u):=\frac{K(t_2-u)}{K(t_1-u)}
=e^{t_2-t_1}
\exp\left[-\frac{e^{2t_2}-e^{2t_1}}2e^{-2u}\right]
\tag{21}
\]

is strictly increasing in $u$, and is bounded above by $e^{t_2-t_1}$. Therefore

\[
D_c(t_2)-Q(u_c)D_c(t_1)
=\int_{\mathbb R}K(t_1-u)
  [Q(u)-Q(u_c)]N_c(u)\,du>0.
\tag{22}
\]

Every factor except the bracket and $N_c$ is positive; these last two factors have the same strict sign on either side of $u_c$. The integral is finite by the bound on $Q$ and the integrability of $K$. In particular, a zero of $D_c$ is followed by strictly positive values. This proves the exact direction of the required single crossing without an appeal to a general variation-diminishing result.

Now fix $0<x_1<x_2$, and choose

\[
c=\frac{\Lambda_s(x_1)}{x_1}\in(0,1),
\tag{23}
\]

where membership in $(0,1)$ follows from (18). Then $D_c(\log x_1)=0$. Equation (22) gives

\[
F_s(x_2)>\sigma(cx_2),\quad\text{so}\quad
\frac{\Lambda_s(x_2)}{x_2}>
\frac{\Lambda_s(x_1)}{x_1}.
\tag{24}
\]

This is strict monotonicity for every pair $x_1<x_2$, without needing an analyticity argument.

At zero, dominated differentiation and $F_s(0)=1/2$ give

\[
\lim_{x\downarrow0}\frac{\Lambda_s(x)}x
=4\mathbb E\sigma'(sH)\in(0,1).
\tag{25}
\]

For the other endpoint,

\[
e^x[1-F_s(x)]
=\mathbb E\frac{e^{-sH}}{1+e^{-x-sH}}
\longrightarrow e^{s^2/2}
\tag{26}
\]

by dominated convergence, since $e^{-sH}$ is integrable. Thus

\[
\Lambda_s(x)=x-\frac{s^2}2+o(1),\qquad
\lim_{x\to\infty}\frac{\Lambda_s(x)}x=1.
\tag{27}
\]

Applying (24)--(27) with $x=\lambda u$ proves (4)--(5).

## 4. Risk minimization and strict signed overconfidence

The normal law of $U$ has all moments, so dominated differentiation gives

\[
R'(c)=\mathbb E[U(\sigma(cU)-g(U))],\qquad
R''(c)=\mathbb E[U^2\sigma'(cU)]>0.
\tag{28}
\]

Since $g(u)>1/2$ for $u>0$, symmetry implies $R'(0)<0$. On the other hand,

\[
\lim_{c\to\infty}R'(c)
=\mathbb E[|U|(1-g(|U|))]>0.
\tag{29}
\]

The integrand is strictly positive almost surely and is integrable. Thus the strictly convex function $R$ has a unique critical point $c_*>0$, and it is its global minimizer. Its value is strictly below $R(0)=\log2$.

Let $h_0=4g'(0)$. By the strict increase already proved, $h_0<h(u)<\lambda$ for every $u>0$. Hence $R'(c)<0$ for $c\le h_0$, and $R'(c)>0$ for $c\ge\lambda$. This proves $h_0<c_*<\lambda$. Continuity, strict increase and the endpoint limits produce a unique $u_*>0$ with $h(u_*)=c_*$, and (7) follows from the strict increase of $\sigma$.

Write $e(u)=\sigma(c_*u)-g(u)$, and let $\varphi_V$ denote the $N(0,V)$ density. The first-order condition and oddness of $e$ give

\[
0=R'(c_*)=2\int_0^\infty u\,e(u)\varphi_V(u)\,du.
\tag{30}
\]

Subtracting this identity divided by $u_*$ from the unweighted signed error gives

\[
\begin{aligned}
\operatorname{OC}(c_*)
&=2\int_0^\infty e(u)\varphi_V(u)\,du\\
&=2\int_0^\infty e(u)
    \left(1-\frac u{u_*}\right)\varphi_V(u)\,du
>0.
\end{aligned}
\tag{31}
\]

The two factors $e(u)$ and $1-u/u_*$ have the same strict sign for every $u>0$ other than $u_*$. Integrability follows from $|e|\le1$ and the first absolute normal moment. This completes the theorem.

One may compute $c_*$ through a one-dimensional strictly monotone equation. Stein's identity and the original representation (1) give

\[
Vc_*\,\mathbb E\sigma'(c_*\sqrt V\,H)
=k\beta\,\mathbb E\sigma'(\beta H).
\tag{32}
\]

Equation (28), rather than any presumed monotonicity of the individual factors in (32), proves uniqueness.

## 5. Exact scope of the consequence for T357

Suppose a first-step Gaussian random-feature theorem gives, conditional on the trained model,

\[
\mathcal L(Z,U_d\mid\text{model})
\longrightarrow \mathcal L(Z,kZ+\tau G)
\quad\text{in total variation in probability},
\tag{33}
\]

with $k,\tau>0$, and gives population cross-entropy convergence at every fixed deterministic scale. Taking the fixed scale $c=c_*$ from this note then yields

\[
\operatorname{OC}_d(c_*)\xrightarrow{\mathbb P}
\operatorname{OC}(c_*)>0,\qquad
R_d(c_*)\xrightarrow{\mathbb P}R(c_*)<\log2.
\tag{34}
\]

Indeed signed OC is the conditional expectation of the bounded measurable function

\[
(z,u)\longmapsto
[\sigma(c_*u)-\sigma(\beta z)]\operatorname{sign}u,
\tag{35}
\]

so total variation proves the first assertion directly. A second moment bound or the separately established risk-transfer theorem handles the unbounded cross-entropy integrand. In particular, fixed positive margins below $\log2$ and above zero hold simultaneously with probability tending to one. B04's first-step TV theorem and the previously audited first-step risk theorem are the relevant proposed inputs; this note does not replace their proofs.

Because $u\mapsto\sigma(c_*u)$ is one-to-one, the limiting exact unbinned calibration error is

\[
\mathbb E|\sigma(c_*U)-g(U)|
\ge\operatorname{OC}(c_*)>0.
\tag{36}
\]

The finite-model OC statement (34) itself does not require continuity of conditional regression: it uses the bounded test function (35). This is weaker in prerequisite than proving convergence of an entire conditional calibration curve.

The theorem treats all positive parameters in the Gaussian scalar experiment, not a selected categorical surrogate or one numerical parameter choice. It closes a signed-overconfidence proof obligation at a risk-optimal **first-step scale**. It does not establish a deterministic arbitrary-time neural-GD trajectory, interchange a training-time limit with dimension, optimize over all stopping times, or show that the scalar risk optimum is a global optimum over the full GD path. Those remain separate T357 obligations. The limiting predictor is overconfident near the boundary and underconfident in the tails, so a claim of pointwise overconfidence at all scores would be false.

## 6. An explicit common regime with the whole-trajectory stopping theorem

The risk-optimal scale above is not automatically a stable GD step. Nevertheless, there is an explicit nonempty regime in which it satisfies the small-step and sample-size conditions of B02's entire-trajectory theorem. Thus the overconfidence and stopping conclusions need not be about incompatible parameter choices.

Use the actual first-step law from the Gaussian tanh RF calculation, with the step scale factored out:
\[
S_1=cU,\qquad
k=a^2\mu_\beta,\qquad
\tau^2=\frac{\mu_\beta^2a^2v}{\gamma}
+\frac{a^4+v^2/\gamma}{4\alpha},
\tag{37}
\]
where
\[
a=\mathbb E[H\tanh H]>0,\quad
v=\mathbb E\tanh^2H>0,\quad
\nu=v-a^2>0,\quad
\mu_\beta=\mathbb E[H(\sigma(\beta H)-1/2)]
=\beta\mathbb E\sigma'(\beta H).
\]
These are exactly the coefficients in B01 equation (21), equivalently the previously audited Gaussian first-step theorem. For $\beta>0$, both $k$ and $\tau$ are strictly positive.

Fix any $\gamma>0$, and use B02's constants
\[
L=8\sqrt{1+\gamma},\qquad
s_0=\nu/2,\qquad
\kappa=\sqrt{s_0/2},\qquad
p_0=\frac{s_0^2}{20L^4},\qquad
B=\sqrt{2\log(4/p_0)}.
\]
Choose
\[
\frac{\alpha}{\gamma}>
C_0:=\max\left\{1,\left(\frac{256L}{\kappa p_0}\right)^2\right\},
\qquad
0<\beta<
\min\left\{\frac{\log3}{B},\frac{v}{8aL\sqrt\alpha}\right\}.
\tag{38}
\]
Every interval here has positive length. In particular this is a nonempty open set of proportional sample, width and teacher parameters, although its sample ratio is deliberately very conservative.

The first inequality on $\beta$ gives
$q_\beta=\sigma(-\beta B)>1/4$ and hence
$p_1=q_\beta p_0/2>p_0/8$ in B02. Thus its threshold satisfies
\[
C_*(\beta)=
\max\left\{1,\left(\frac{32L}{\kappa p_1}\right)^2\right\}
\le C_0<\alpha/\gamma.
\tag{39}
\]
Next, $\mu_\beta\le\beta/4$ and (37) give
\[
0<c_*<\frac{\beta k}{k^2+\tau^2}
\le\frac{a^2\alpha\gamma\beta^2}{v^2}
<\frac{\gamma}{64L^2}
<\frac{\gamma}{32L^2}
=\frac{\gamma}{2\Lambda},
\qquad\Lambda=16L^2.
\tag{40}
\]
This is precisely inside B02's stable fixed-step interval. The scalar risk optimum is therefore a valid fixed deterministic GD parameter in the same model for which B02 proves its all-time statements.

Consequently, after the companion finite-model transfer and whole-trajectory theorems are certified, this one model simultaneously has:

- A first positive iterate with population risk strictly below $\log2$ and strictly positive signed overconfidence, with probability tending to one.
- A fixed positive exact-calibration floor, with probability tending to one, simultaneously over every positive integer training time, the MLE, and any training-measurable stopping rule taking those values.
- A calibrated time-zero predictor with risk exactly $\log2$.

This also gives a nonvacuous risk-constrained stopping conclusion. For any fixed $\Delta>0$ and any training-measurable rule $T_d\in\{0,1,\ldots,\infty\}$ such that
\[
\mathbb P\{R_d(T_d)\le\log2-\Delta\}\longrightarrow1,
\tag{41}
\]
one necessarily has $\mathbb P(T_d>0)\to1$, because the risk at time zero is exactly $\log2$. The simultaneous positive calibration floor then applies to $T_d$. On the other hand, a fixed first-step rule satisfies (41) for every $\Delta<R(0)-R(c_*)$ by (34). Thus such risk improvement is attainable but cannot coexist with asymptotic exact calibration through stopping alone in this fixed-step regime.

This common regime still has sufficiently large $n/m$, so the fitted output layer is underparameterized. The random-feature architecture remains the original dense Gaussian nonlinear model; no categorical design is introduced. The argument does not extend the all-time statement to every overparameterized sample ratio or to dimension-dependent vanishing steps.

## 7. Source and originality note

The classical normal scale-mixture representation appears in L. A. Stefanski, *A normal scale mixture representation of the logistic distribution*, Statistics & Probability Letters 11(1), 69--70 (1991), [DOI 10.1016/0167-7152(91)90181-P](https://doi.org/10.1016/0167-7152(91)90181-P). Bibliographic identity was checked against the publisher's volume listing. The institutional full-text endpoint returned a fetch error during this audit; no inaccessible passage is used as a proof premise. Equations (9)--(13) establish the representation and strict support independently from standard characteristic-function and gamma identities.

The old local dossier already suggested a normal-mixture single-crossing route. The contribution of this audit is the explicit ratio calculation (21)--(24), the strict-support argument, and the fully stated risk-to-signed-OC implication. This verifies the local mathematical claim; it does not certify that the conclusion is new in the literature.
