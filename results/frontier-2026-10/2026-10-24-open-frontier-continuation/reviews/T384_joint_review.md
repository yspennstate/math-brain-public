# Adversarial review: T384 joint initialization law

**Verdict: PASS for the four-dimensional initialization limit, with the scope and minor wording edits below.** I checked [T384_joint_limit.md](../research/T384_joint_limit.md) line by line. The primary [stable-tail source](https://arxiv.org/html/1802.00612v3) uses the characteristic-function normalization $\exp(-\sigma^\alpha|t|^\alpha)$ and gives one-sided tail constant $C_\alpha/2=\Gamma(\alpha)\sin(\pi\alpha/2)/\pi$ when $\sigma=1$ and skewness zero. This equals the note's $c_\alpha$ (also at $\alpha=1$ by continuity). No factor of two is missing.

## Product constant and marginal Lévy measures

For $X=WU_+$, the middle range $h(t)\le U\le t/h(t)$, $h(t)=\log t$, contributes

$$
c_\alpha t^{-\alpha}\,
\mathbb E[U_+^\alpha{\bf1}_{h(t)\le U\le t/h(t)}]
\sim \alpha c_\alpha^2 t^{-\alpha}\log t.
$$

The lower and upper ranges inside $U\le t$ are each $O(t^{-\alpha}\log h(t))=o(t^{-\alpha}\log t)$: use $\mathbb P(W>t/U)\le C(U/t)^\alpha$ and truncated $\alpha$-moment $O(1+\log v)$. The range $U>t$ is $O(t^{-\alpha})$. The negative tail is identical by $W$ symmetry. Since $b_m^\alpha=m\log m$ and $\log b_m/\log m\to1/\alpha$,

$$
m\mathbb P(X>b_m x)\to c_\alpha^2 x^{-\alpha}
$$

for $x>0$, likewise on the negative side. Thus the symmetric F Lévy density is $\alpha c_\alpha^2|x|^{-1-\alpha}$ on **each** half-axis and its characteristic exponent is $-c_\alpha|t|^\alpha$. The positive coordinates have tail constants $c_\alpha/2,c_\alpha/2,c_\alpha$ for $A,B,C$, respectively. Their positive $\beta=\alpha/2$ stable Laplace exponents are exactly these constants multiplied by $\Gamma(1-\beta)s^\beta$. These calculations validate every displayed transform and the total $H$ exponent $2c_\alpha\Gamma(1-\beta)$.

## Axes and independence

The two-coordinate estimate (4) is correct. For $Z_A+Z_B>\delta d_m$ one has $|W|>\sqrt\delta\,m^{1/\alpha}$. Above $L m^{1/\alpha}$ its $m$-scaled probability is at most $CL^{-\alpha}$; below $L m^{1/\alpha}$ a product jump $|X|>\epsilon b_m$ requires $U>(\epsilon/L)(\log m)^{1/\alpha}$. Independence of U and W makes the latter joint $m$-scaled probability vanish at fixed L. Send $L\to\infty$. Interchanging U and W proves the X/C version. Simultaneous W-square and U-square endpoint jumps have probability $O(m^{-2})$ per neuron, and A/B are disjoint per neuron. Therefore all vague limiting mass away from the origin lies on the four separate axes. The shared positive-U mark and W-sign do not leave a simultaneous order-one jump.

For fixed cutoffs, each one-observation retained-jump probability is $O(1/m)$, and the iid characteristic/Laplace product converges to an exponent which is the **sum** of the four axis integrals. Independence follows from that factorization, not merely from marginal stable laws. Tail truncation at large R is legitimate with $\limsup_m m\mathbb P(\|\text{one normalized jump}\|>R)=O(R^{-\alpha}+R^{-\beta})$.

The cutoff removal is also sufficient for joint convergence. Symmetry of W gives
$\mathbb E[X{\bf1}_{|X|\le\epsilon b_m}]=0$ exactly (even when $\alpha\le1$), and the product tail upper bound yields

$$
\limsup_m\frac{m}{b_m^2}
\mathbb E[X^2{\bf1}_{|X|\le\epsilon b_m}]
\le C\epsilon^{2-\alpha}.
$$

Chebyshev makes the centered small-X sum vanish as $\epsilon\downarrow0$. For each nonnegative $Z_J$ the bound $\mathbb P(Z_J>t)\le Ct^{-\beta}$ for all $t>0$ and $\beta<1$ yields

$$
\sup_m \frac{m}{d_m}
\mathbb E[Z_J{\bf1}_{Z_J\le\delta d_m}]
\le C\delta^{1-\beta};
$$

Markov removes the small positive sums. No Gaussian term, uncompensated drift, or residual dependence survives. The proof uses **unconditional** small-sum bounds, which are stronger than the conditional control needed for the converging-together argument; dependence on retained jumps poses no problem.

## Sign-selected corollary checked

Let $F,A,B,C$ be the independent limits. For fixed $y$, define $Q=C+A$ and $D=B$ when $y-F>0$, otherwise $Q=C+B$ and $D=A$. Since $F$ has a continuous stable law, $\mathbb P(F=y)=0$, so the same selection from $(F_m,A_m,B_m,C_m)$ converges by the continuous-mapping theorem. Conditional on $F$, the pair $(A_{\rm selected},A_{\rm other})$ is either $(A,B)$ or $(B,A)$; these have **the same product distribution** because A and B are iid and independent of $(F,C)$. Hence $(F,Q,D)$ are mutually independent, with

$$
\mathbb E e^{-sQ}
=\exp[-(3c_\alpha/2)\Gamma(1-\alpha/2)s^{\alpha/2}],
\qquad
\mathbb E e^{-sD}
=\exp[-(c_\alpha/2)\Gamma(1-\alpha/2)s^{\alpha/2}].
$$

This is a valid **initialization-law corollary**. It does not by itself show that the dynamical surviving and dead kernel masses converge to $Q$ and $D$ at positive training time; that requires a separate flow argument.

## Minor wording edits

1. Say “limsup for sufficiently large $m$” rather than a literal uniform $O(R^{-\alpha}+R^{-\beta})$ consequence of asymptotic (2)–(3) alone. The global tail upper bounds already present can make the uniform version precise.
2. In the iid exponent step, mention that the threshold discontinuity sets have zero limiting Lévy mass. For $\alpha\ge1$, use the symmetric two-sided cutoff for F as written, so the compensation/drift is exactly zero.
3. The assertion “none unpaid” applies only to the finite-dimensional **initialization** joint law under independent within-pair standard symmetric stable variables. Do not carry that phrase into a training-dynamics claim.

No substantive gap or incorrect constant found.
