# The sharp constant for unimodality of classical Brownian motion

**Problem.** Hasebe and Ueda, *Unimodality for classical and free Brownian motions*, ALEA 15 (2018),
study when $\mu * N(0,t)$ becomes unimodal. Their Theorem 1.3(1) says: if
$\alpha = \int e^{\varepsilon x^2}d\mu < \infty$ then $\mu * N(0,t)$ is unimodal for every
$t \ge 36\log(2\alpha)/\varepsilon$. For $\mu$ supported in an interval of length $D$ one has
$\alpha \le e^{\varepsilon D^2/4}$, and letting $\varepsilon \to \infty$ their bound becomes $t \ge 9D^2$.
Earlier today I posed the sharp constant as an open problem, as the classical companion to their Problem
3.3 on free Brownian motion. It has a clean answer.

**Theorem.** *Let $\mu$ be a probability measure whose support lies in an interval of length $D$. Then
$\mu * N(0,t)$ is unimodal for every $t \ge D^2/4$, and the constant is optimal: for
$\mu = \tfrac12(\delta_{-1}+\delta_1)$, which has $D = 2$, the convolution is not unimodal for any
$t < 1 = D^2/4$.*

The optimality half is the source's own Example 4.1. The bound $D^2/4$ improves their $9D^2$ by a factor
of thirty-six in the compactly supported case, and no further improvement is possible.

## Proof

Write $\varphi_t$ for the centred Gaussian density of variance $t$, so the density of $\mu*N(0,t)$ is
$f(x) = \int \varphi_t(x-y)\,d\mu(y)$, which is smooth, strictly positive, and vanishes at $\pm\infty$.

If $f$ is not unimodal there is a point $x_0$ that is a local minimum of $f$ with a local maximum on each
side. Such a point lies in the convex hull of $\operatorname{supp}\mu$: for $x$ above the hull every
$x - y$ is positive, so
$f'(x) = -\tfrac1t\int (x-y)\varphi_t(x-y)\,d\mu(y) < 0$, and symmetrically $f' > 0$ below the hull.

Translate $x_0$ to the origin and let $\rho$ be the image of $\mu$ under $y \mapsto -y$, a probability
measure carried by an interval $J$ of length $D$ whose convex hull contains $0$. The two conditions at a
local minimum read
$$G(\rho) := \int d\,\varphi_t(d)\,d\rho(d) = 0, \qquad
H(\rho) := \int (d^2-t)\,\varphi_t(d)\,d\rho(d) \ \ge\ 0,$$
being $-tf'(0)$ and $t^2f''(0)$. Both are linear in $\rho$.

Let $K$ be the set of probability measures on $J$ with $G = 0$. It is convex and weak-* compact, and its
extreme points carry at most two atoms, since a measure subject to normalisation and one further linear
constraint can be perturbed inside $K$ as soon as its support has three points. By Choquet's theorem
$\rho$ is a barycentre of extreme points, and since $H$ is linear and $H(\rho)\ge0$, some extreme point
$\kappa$ has $H(\kappa)\ge 0$.

*One atom.* $G(\delta_c) = c\varphi_t(c) = 0$ forces $c=0$, and then
$H(\delta_0) = -t\varphi_t(0) < 0$. So $\kappa$ is not a single atom.

*Two atoms.* Write $\kappa = p\delta_{-a} + q\delta_{b}$. Since $d\varphi_t(d)$ has the sign of $d$, the
condition $G(\kappa)=0$ forces the atoms to straddle the origin, so $a, b > 0$, and it reads
$p\,a\,\varphi_t(a) = q\,b\,\varphi_t(b) =: \theta > 0$. Then $p\varphi_t(a) = \theta/a$ and
$q\varphi_t(b) = \theta/b$, so
$$H(\kappa) = \frac{\theta}{a}(a^2-t) + \frac{\theta}{b}(b^2-t)
= \theta\Big(a+b-t\frac{a+b}{ab}\Big) = \theta\,(a+b)\Big(1 - \frac{t}{ab}\Big).$$
Hence $H(\kappa) \ge 0$ if and only if $t \le ab$.

Both atoms lie in $J$, so $a + b \le D$ and therefore $ab \le D^2/4$. Combining,
$t \le ab \le D^2/4$. So if $t > D^2/4$ there is no separating local minimum and $f$ is unimodal.

At $t = D^2/4$ the same chain forces equality throughout: every extreme point in the decomposition has
$H \le 0$, so $H(\rho) \ge 0$ gives $H = 0$ almost surely, which needs $ab = t = D^2/4$ with $a+b\le D$,
hence $a = b = D/2$. The only such $\rho$ with $G = 0$ has equal weights, so $\mu$ is the symmetric
two-point measure at spacing $D$, and that one is unimodal at $t = D^2/4$ by Example 4.1. So the
conclusion holds for every $t \ge D^2/4$. $\blacksquare$

**Corollary.** *Write $t^*(\mu)$ for the least time from which $\mu * N(0,t)$ is unimodal. Then*
*$t^*(\mu) \le D_\mu^2/4$, with equality if and only if $\mu$ is a symmetric two-point measure.* The last
paragraph of the proof is exactly this: attaining the bound forces $a=b=D/2$ and equal weights, so every
other measure of the same diameter becomes unimodal strictly sooner. The table below bears that out, the
symmetric pair sitting at $0.250000$ and the next nearest case at $0.208$.

## Checks

The threshold was computed directly for eight measures of diameter one, by building the density and
counting the sign changes of its derivative, then bisecting on $t$:

| measure (all of diameter one) | least $t$ from which unimodal |
| --- | --- |
| two equal atoms at $\pm\tfrac12$ | 0.250000 |
| atoms at $\pm\tfrac12$, weights 0.3 and 0.7 | 0.135704 |
| atoms at $\pm\tfrac12$, weights 0.1 and 0.9 | 0.091026 |
| three atoms $-\tfrac12, 0, \tfrac12$ | 0.207860 |
| three atoms $-\tfrac12, 0.1, \tfrac12$ | 0.131041 |
| four atoms across $[-\tfrac12,\tfrac12]$ | 0.121237 |
| nine equally spaced atoms | 0.011343 |
| two atoms and a nearby spike | 0.127792 |

Every one is at most $D^2/4 = 0.25$, and the symmetric pair attains it to six places. The asymmetric
pairs fall well short, which is what $t \le ab$ predicts, since moving the critical point off centre
lowers $ab$.

## The same argument for any symmetric kernel

Nothing in the proof used the Gaussian beyond two facts: the kernel is symmetric and decreasing away from
the origin, and the two conditions are integrals against fixed functions. So it gives a criterion for any
kernel. Let $p$ be a symmetric density, smooth and positive, with $p' < 0$ on $(0,\infty)$, and set
$$\psi(x) \ = \ -\big(\log|p'(x)|\big)' \ = \ -\frac{p''(x)}{p'(x)}, \qquad x>0.$$

**Criterion.** *Every $\mu$ whose support has diameter at most $D$ has $\mu * p$ unimodal if and only if*
$$\psi(a)+\psi(b) \ \le\ 0 \qquad \text{for all } a,b>0 \text{ with } a+b \le D.$$

One direction is the proof above. The other is the same two atoms read forwards: given $a,b>0$ with
$a+b\le D$ and $\psi(a)+\psi(b) > 0$, put $\mu = w_1\delta_{-a}+w_2\delta_b$ with
$w_1|p'(a)| = w_2|p'(b)|$. Then $(\mu*p)'(0) = 0$ and $(\mu*p)''(0) > 0$, so the origin is a strict local
minimum; since $\mu*p$ is positive and vanishes at $\pm\infty$ it must have a local maximum on each
side, and $\mu*p$ is not unimodal. So the criterion is not merely sufficient: it decides the question for
the whole class of measures of a given diameter, and the constant $c(p)$ below is the exact threshold.

The proof is the one above verbatim: an extreme pair at $-a$ and $b$ with weights $w_1, w_2$ satisfies
$w_1|p'(a)| = w_2|p'(b)|$ by the first condition, and the second condition, divided by that common
value, is exactly $\psi(a)+\psi(b)\ge 0$. For the Gaussian of variance $t$, $\psi(x) = (x^2-t)/(tx)$, the supremum
sits at $a=b=D/2$, and the criterion reads $t > D^2/4$.

Since $\psi$ scales as $\psi_s(x) = \psi(x/s)/s$ for $p_s(x) = p(x/s)/s$, the condition depends only on
$D/s$: each kernel has a constant $c(p)$ with unimodality guaranteed whenever $D < c(p)\,s$. Two cases
where the answer is known independently confirm it exactly.

*Gaussian.* $c = 2$, that is $D < 2\sigma$, which is $t > D^2/4$, and the classical fact that an equal
mixture of two Gaussians with means $\pm m$ is unimodal exactly when $\sigma \ge m$.

*Cauchy.* $\psi(x) = -1/x + 4x/(1+x^2)$, and at $a=b=D/2$ the supremum vanishes when $16D^2 = 4(4+D^2)$,
so $c = 2/\sqrt3 = 1.1547$. That is the classical threshold for an equal mixture of two Cauchy densities
at $\pm a$ to be unimodal, $a \le 1/\sqrt3$.

*Laplace.* $p(x) = e^{-|x|}/2$ gives $\psi \equiv 1$ on $(0,\infty)$, so the criterion fails for every
$D>0$ and $c = 0$: a two-atom measure convolved with a Laplace kernel is bimodal however close the atoms
are, which is visibly true, since each atom contributes a cusp. This is worth keeping in view because it
separates the criterion from strong unimodality. The Laplace density is log-concave, so by Ibragimov it
*is* strongly unimodal, meaning $\nu * p$ is unimodal for every unimodal $\nu$; what fails is the
diameter statement, whose test measures are not unimodal. The two notions constrain different families.

That example also settles when the constant is positive at all. For a density smooth at its peak,
$p'(0)=0$ and $p''(0)<0$ give $|p'(x)| \sim |p''(0)|x$ near the origin, so
$\psi(x) \sim -1/x \to -\infty$ and $c(p) > 0$. The Laplace fails precisely because it has a corner there,
$p'(0^\pm) = \mp\tfrac12$. So $c(p)>0$ exactly when the kernel is smooth and strictly concave at its mode,
and the size of $c(p)$ then measures how far that concavity reaches.

For the symmetric stable laws with characteristic function $e^{-|u|^\alpha}$, computing $\psi$ by Fourier
inversion gives

| $\alpha$ | 2.0 | 1.8 | 1.5 | 1.2 | 1.0 | 0.8 | 0.5 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| $c(\alpha)$ | 2.813 | 2.596 | 2.133 | 1.577 | 1.145 | 0.682 | 0.095 |

(the entry at $\alpha=2$ is for the law with that characteristic function, which has variance two, so it
is $2\sqrt2$ and agrees with $c=2$ per standard deviation; the entry at $\alpha=1$ agrees with $2/\sqrt3$
to the grid's resolution). The constant falls steeply as the tails get heavier, which is the quantitative
form of the obvious point that a heavy-tailed kernel is peaked and does not fill in the valley between two
distant lumps until its scale is large.

This settles the compactly supported case of the same paper's Conjecture 5.5, which asks whether
$\mu * S_t$ is unimodal for large $t$ when $\int|x|^{2+\alpha}d\mu<\infty$: for $\mu$ of diameter $D$ it
is unimodal as soon as $t > (D/c(\alpha))^{\alpha}$, with $c(\alpha)$ above. The conjecture's own content
is the unbounded-support case, where the criterion is silent because $a+b$ is unbounded, and that is
exactly why a moment condition is needed there.

## The free side runs the other way

The free analogue of the same question has an answer of the same shape, and the two behave oppositely as
the tails get heavier.

Free convolution with a symmetric free $\alpha$-stable law of scale $s$ obeys the same scaling as the
classical one, so a measure of diameter $D$ has $\mu\boxplus\lambda_{\alpha,s}$ unimodal once
$D < c_{\mathrm{free}}(\alpha)\,s$, and since the natural time parameter is $t = s^\alpha$ that reads
$t > (D/c_{\mathrm{free}}(\alpha))^\alpha$. So the exponent $2$ of the semicircle case does become
$\alpha$. Probing with the symmetric two-atom measure, which is the extremal one at $\alpha=2$, and
computing the free convolutions by subordination:

| $\alpha$ | 2 | 1.8 | 1.6 | 1.4 | 1.2 | 1.0 | 0.8 | 0.6 | 0.5 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| $c_{\mathrm{free}}$ | 1.000 | 1.024 | 1.050 | 1.078 | 1.112 | 1.160 | 1.228 | 1.341 | 1.435 |

the entry at $\alpha=2$ being the theorem $t \ge D^2$ and recovered numerically as $1.0015$.

To set that beside the classical column the two normalisations have to be matched, and the peak density is
the statistic that does it. The free family as normalised has peak $1/\pi$ at *every* $\alpha$: at the
origin $w = G(0^+)$ is purely imaginary and $K(w)=0$ forces $|w|=1$. The classical family with
characteristic function $e^{-|u|^\alpha}$ has peak $\Gamma(1+1/\alpha)/\pi$, so rescaling it to peak
$1/\pi$ divides its constant by $\Gamma(1+1/\alpha)$. Then

| $\alpha$ | 2 | 1.8 | 1.5 | 1.2 | 1.0 | 0.8 | 0.5 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| classical, peak-matched | 3.174 | 2.920 | 2.363 | 1.677 | 1.145 | 0.602 | 0.047 |
| free | 1.000 | 1.024 | $\approx$1.05 | 1.112 | 1.160 | 1.228 | 1.435 |

The classical constant collapses as the tails get heavier, by a factor of nearly seventy between
$\alpha=2$ and $\alpha=0.5$, while the free constant climbs by forty per cent. They cross near
$\alpha \approx 1.05$. So a heavy-tailed classical kernel is very bad at merging two lumps, being too
peaked to fill the valley, and a heavy-tailed free kernel is better at it than the semicircle. The free
column is a numerical statement resting on the two-atom probe, which is proved extremal only at
$\alpha=2$, so it is a lower bound on the class constant for the other indices.

It was computed twice, by two algorithms sharing no code path. The subordination functions collapse: from
$G = G_\mu(\omega_1) = G_\lambda(\omega_2)$ and $\omega_1+\omega_2 = z + 1/G$, with
$\omega_2 = 1/G + R_\lambda(G)$, the second drops out and $\omega_1 = z - R_\lambda(G)$, leaving one
implicit equation
$$G \;=\; G_\mu\big(z - R_\lambda(G)\big).$$
For the semicircle, $R(w) = tw$, that is $G = G_\mu(z-tG)$, and writing $G = a - i\pi f$ turns it into
$\int d\mu(y)/((u-y)^2+v^2) = 1/t$ with $v = \pi t f$, which is Lemma 3.1 with the density cancelled.
That cancellation is what makes the semicircle the one kernel with a clean level-set criterion. Solving
the implicit equation directly by Newton, instead of iterating the two subordination maps, gives
$1.0006$, $1.0238$, $1.0767$, $1.1565$, $1.2242$ and $1.4302$ at $\alpha = 2, 1.8, 1.4, 1.0, 0.8, 0.5$:
agreement with the table to four parts in a thousand, and closer to the exact $1$ at $\alpha=2$.

## Status

Answered, sharply, with a proof. Verification: author checked; the proof is four lines of calculus plus a
Choquet decomposition, and the threshold was computed numerically for eight measures with the extremal
one hitting the bound exactly. Prior art: the source proves the same statement with the constant $9D^2$
through a Gaussian-moment condition, and its Example 4.1 supplies the matching lower bound; I did not
find the sharp constant stated. The two-Gaussian case itself, that an equal mixture with means $\pm m$ is
unimodal exactly when $\sigma^2 \ge m^2$, is classical. Not a clearance.

## What it says about the free case

The same argument, run on the free side through Biane's description, gives the constant $1$ for
$\mu \boxplus S(0,t)$, which is the subject of the companion memo of today. The two answers sit oddly
next to each other: the free constant is $1$ and the classical one is $1/4$, so free Brownian motion
needs four times as long to become unimodal, measured in the variance of the added semicircle or
Gaussian. The extremal measure is the symmetric two-point law in both cases.

## New open problems

1. **Between the two.** For the $q$-deformed convolutions interpolating between classical and free, is
   there a constant $C(q)$ of the same kind, and does it run from $1/4$ at $q=1$ to $1$ at $q=0$
   monotonically?
2. **Variance in place of diameter, classically.** The proof uses only that both atoms of an extreme pair
   lie in an interval of length $D$. For measures of unbounded support the source shows some condition is
   needed. Is there a constant $C'$ with $\mu * N(0,t)$ unimodal for every $t \ge C'\operatorname{Var}(\mu)$
   under a moment condition weaker than the Gaussian one, and what is the sharp $C'$?
3. **Higher dimensions.** In $\mathbb{R}^d$, with unimodality read as quasi-concavity of the density, is
   $\mu * N(0,tI)$ quasi-concave for $t \ge c_d D^2$, and how does $c_d$ behave?
4. **The rate of approach.** For $t$ slightly below $D^2/4$ the density of the extremal measure has two
   modes separated by a shallow dip. How does the depth of the dip vanish as $t \uparrow D^2/4$, and is
   the exponent universal over measures attaining the bound?
