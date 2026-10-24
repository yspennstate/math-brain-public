# Free strong unimodality: the Cauchy laws, and what the problem reduces to

**Problem.** Hasebe and Ueda, ALEA 15 (2018), Problem 3.11: does there exist a freely strongly unimodal
probability measure that is not a delta measure? A measure $\lambda$ is *freely strongly unimodal* if
$\lambda\boxplus\nu$ is unimodal for every unimodal $\nu$.

Their Theorem 1.4 already answers this for every $\lambda$ of finite variance, so the problem lives
entirely in the infinite-variance regime, which the quoted statement does not say. What follows removes
one natural family from the candidates and says what is left.

**Proposition.** *No Cauchy distribution is freely strongly unimodal.*

**Corollary.** *If $\lambda$ is not a delta and lies in the free domain of attraction of a Cauchy law,
then $\lambda$ is not freely strongly unimodal.*

Since finite variance is exactly the free domain of attraction of the semicircle, their theorem and this
corollary together say: a counterexample to Problem 3.11, if one exists, is attracted to neither the
semicircle nor the Cauchy.

## The Cauchy laws

Write $C_t$ for the Cauchy law of scale $t$, with density $t/(\pi(t^2+x^2))$.

The whole point is an identity that is special to the Cauchy family. Its Cauchy transform is
$G_{C_t}(z) = 1/(z+it)$ on the upper half plane, so $K_{C_t}(w) = 1/w - it$ and the $R$-transform is the
constant $R_{C_t}(w) = -it$. Free convolution adds $R$-transforms, so for any $\mu$,
$$K_{\mu\boxplus C_t}(w) = K_\mu(w) - it \quad\Longrightarrow\quad G_{\mu\boxplus C_t}(z) = G_\mu(z+it).$$
On the other side, the density of $\mu * C_t$ at $x$ is the Poisson integral
$\tfrac1\pi\int t\,d\mu(y)/((x-y)^2+t^2) = -\tfrac1\pi\operatorname{Im}G_\mu(x+it)$, so
$G_{\mu*C_t}(z) = G_\mu(z+it)$ as well. Hence
$$\mu \boxplus C_t \ = \ \mu * C_t \qquad\text{for every } \mu \text{ and every } t>0,$$
the free and classical convolutions with a Cauchy law coinciding.

Now the Proposition. The Cauchy density is not log-concave, so by Ibragimov's characterisation of
classically strongly unimodal laws, $C_t$ is not strongly unimodal: there is a unimodal $\nu$ with
$\nu * C_t$ not unimodal. By the identity, $\nu \boxplus C_t = \nu * C_t$ is not unimodal either, and
$\nu$ is unimodal, so $C_t$ is not freely strongly unimodal. $\blacksquare$

The appeal to Ibragimov can be replaced by an explicit measure, which is worth having because the source
invokes the existence without exhibiting one. Take
$$\nu \;=\; \tfrac{1}{10}\,U_{[0,\,0.05]} \;+\; \tfrac{9}{10}\,U_{[0,\,16]},$$
a mixture of two uniform laws anchored at the origin. Its density is nonincreasing on $[0,\infty)$ and
vanishes to the left, so $\nu$ is unimodal with mode $0$. Its Cauchy convolution is elementary,
$$(\nu * C_t)(x) \;=\; \sum_i \frac{w_i}{\pi a_i}\Big[\arctan\tfrac{x}{t} - \arctan\tfrac{x-a_i}{t}\Big],$$
and at $t=1$ it has two local maxima, $0.0618096$ at $x = 0.3264$ and $0.0523808$ at $x = 6.4072$, with a
minimum of $0.0522654$ at $x = 3.7590$ between them. The dip is shallow, $1.15\times10^{-4}$ below the
lower of the two modes, but the density is an explicit combination of arctangents and the values above are
computed from it directly at a spacing of $4\times10^{-6}$, so the second maximum is real and not a
sampling artefact. The mechanism is plain: each term of the mixture contributes a bump with its mode at
$a_i/2$, so two widely separated scales put two bumps in the convolution while the mixture itself stays
nonincreasing.

So $\nu\boxplus C_1 = \nu * C_1$ is not unimodal, and the Proposition holds with a witness rather than an
appeal.

The non-log-concavity of the Cauchy density is also where Hasebe and Ueda begin their Lemma 3.9, that
semicircle laws are not freely strongly unimodal; there it supplies a measure whose Cauchy smoothing is
not unimodal, and the semicircle conclusion comes through their Lemma 3.1. Here the Cauchy does the work
directly, because for it the two convolutions are the same operation.

## The corollary

Their proof of Theorem 3.10 uses finite variance in exactly one place, the free central limit theorem,
and the rest of the argument is indifferent to which stable law appears in the limit.

Suppose $\lambda$ is freely strongly unimodal. Then so is $\lambda^{\boxplus n}$ for every $n$, by
induction: $\lambda^{\boxplus n}\boxplus\nu = \lambda\boxplus(\lambda^{\boxplus n-1}\boxplus \nu)$, and
the inner measure is unimodal by the inductive hypothesis. Let $\nu$ be unimodal with
$\nu\boxplus C_1$ not unimodal, which the Proposition provides.

Let $b_n>0$ and $a_n\in\mathbb{R}$ be such that $D_{1/b_n}(\lambda^{\boxplus n})$ shifted by $a_n$
converges weakly to $C_1$, which is what membership of the free domain of attraction means. Since
$D_{b_n}(\nu)$ is unimodal, the hypothesis makes $D_{b_n}(\nu)\boxplus\lambda^{\boxplus n}$ unimodal.
Dilations pass through free convolution, $D_c(\alpha\boxplus\beta) = D_c\alpha\boxplus D_c\beta$, so
applying $D_{1/b_n}$ and the shift leaves
$$\nu \boxplus \big(D_{1/b_n}(\lambda^{\boxplus n})\ \text{shifted by } a_n\big)$$
unimodal for every $n$. Free convolution is continuous in the weak topology and the unimodal measures are
weakly closed, so the limit $\nu\boxplus C_1$ is unimodal, contradicting the choice of $\nu$.
$\blacksquare$

## What is left

Putting the two together with their Theorem 1.4: a non-delta measure that is freely strongly unimodal
cannot have finite variance, and cannot be attracted to a Cauchy law. The same argument shows more
generally that $\lambda$ is disqualified as soon as it is attracted to *any* free stable law that is
itself not freely strongly unimodal. So Problem 3.11 reduces to two questions:

1. Is some free stable law of index $\alpha\in(0,2)$, $\alpha\ne1$, freely strongly unimodal?
2. Among measures in the free domain of attraction of nothing at all, is one freely strongly unimodal?

The first is the substantial one. The free stable laws are all unimodal, by Hasebe and Thorbjørnsen, so
the obstruction cannot be that they fail unimodality themselves; what is needed is a unimodal $\nu$ whose
free convolution with a given free stable law is not unimodal. For $\alpha=1$ the identity above hands it
over; for $\alpha=2$ their Lemma 3.1 does; in between, neither tool applies and I do not know the answer.

## The same witness against the other stable laws

The reduction leaves the free stable laws of index other than one and two as the case to settle, and the
explicit $\nu$ above turns out to work against most of them.

Free convolutions $\lambda_\alpha \boxplus \nu$ were computed by the Belinschi and Bercovici subordination
iteration, with $G_\nu(z) = \sum_i (w_i/a_i)\log\big(z/(z-a_i)\big)$ and $G_{\lambda_\alpha}$ obtained from
$K(w) = 1/w - i(iw)^{\alpha-1}$, the $R$-transform that gives the Cauchy at $\alpha=1$ and the semicircle at
$\alpha=2$. The resulting density has two interior maxima for every index tested from $0.7$ up:

| $\alpha$ | 1.95 | 1.8 | 1.6 | 1.4 | 1.2 | 1.0 | 0.9 | 0.8 | 0.7 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| maxima at | $-0.12$, $6.36$ | $-0.12$, $6.36$ | $0.01$, $6.36$ | $0.01$, $6.36$ | $0.13$, $6.36$ | $0.39$, $6.36$ | $0.52$, $6.36$ | $0.77$, $6.36$ | $1.15$, $6.49$ |

So for those indices $\lambda_\alpha$ is not freely strongly unimodal, and by the corollary neither is any
non-delta measure attracted to them. At $\alpha=1$ this is a theorem, by the identity above; for the rest
it is a numerical statement, and its warrant is that the same computation at $\alpha=1$ reproduces the
exact Cauchy convolution, peak $0.061765$ against the closed-form $0.0618096$, and puts its maxima at
$0.39$ and $6.36$ against the exact $0.3264$ and $6.4072$.

Below $\alpha \approx 0.65$ the witness stops working: at $\alpha = 0.6, 0.55, 0.5, 0.45, 0.4, 0.35$ and
$0.3$ the same $\nu$ gives a single maximum, robustly across three grids, and three other mixtures of
one-sided uniforms tried at $\alpha=0.5$ give one as well. That is not evidence that those laws *are*
freely strongly unimodal, only that this family of test measures does not break them; a heavier-tailed
kernel smooths the two bumps together. Finding a witness there, or showing none exists, is what the
remaining case needs.

One counting trap is worth recording, since it nearly put a wrong row in the table. A mode counter that
looks for a rise followed by a fall counts the window's edge when the density is still climbing there, and
it reported two modes at $\alpha=0.3$ on the narrower grid while listing only one maximum. Every entry
above is the list of interior maxima, not a count.

## Checks

The identity $\mu\boxplus C_t = \mu * C_t$ was verified numerically as well as derived. Computing free
convolutions by the Belinschi and Bercovici subordination iteration: $C_1\boxplus C_1$ comes out with peak
density $0.159154$ against the exact $1/(2\pi) = 0.159155$ for the Cauchy of scale two, and with
$0.079577$ at $x=2$ against the exact $0.079577$; and the free convolution of the standard semicircle with
$C_{0.7}$ agrees with the Poisson integral of the semicircle at height $0.7$ to $3.6\times10^{-6}$ in
supremum over a grid, that being the solver's tolerance rather than a discrepancy.

## Status

Partial. Problem 3.11 is not answered; what is done is to remove the Cauchy laws and everything attracted
to them from the field of candidates, to point out that the quoted problem is really a question about
infinite variance since the source's own Theorem 1.4 settles the rest, and to reduce what remains to the
free stable laws of index other than one and two. Verification: author checked; the identity is derived in
two lines from the $R$-transform and confirmed numerically to six places, and the corollary is the
source's own argument with the limit law changed. Prior art: the identity $\mu\boxplus C_t = \mu * C_t$ is
classical and I claim no novelty in it; the observation that it disposes of free strong unimodality for
the Cauchy family is what is added here. Not a clearance.

## New open problems

1. **The heavy-tailed free stable laws.** The numerics above break free strong unimodality for every
   index from $0.7$ to $2$. Below about $0.65$ the witness fails. Is a free stable law of index
   $\alpha \lesssim 0.65$ freely strongly unimodal, and if not, what unimodal measure witnesses it? A
   negative answer across the whole range would leave Problem 3.11 open only for measures lying in no
   domain of attraction at all.
2. **Which laws have $\boxplus$ and $*$ agreeing?** The Cauchy family has $\mu\boxplus C_t = \mu*C_t$ for
   every $\mu$. Is it the only family with that property, and is there a characterisation of the pairs
   $(\mu,\nu)$ with $\mu\boxplus\nu = \mu*\nu$ beyond the known examples?
3. **A free Ibragimov theorem.** Classically, strong unimodality is exactly log-concavity. The free side
   has no such characterisation and, by the source's Theorem 1.4 and the results here, the class is very
   nearly empty. Is there a property of $\lambda$ equivalent to "$\lambda\boxplus\nu$ is unimodal for every
   unimodal $\nu$", even if it turns out to hold only for delta measures?
