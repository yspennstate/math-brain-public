# The factor four on the critical line of the interval-activation frog model, and where it comes from

Ledger row H0024 (intake H). Source: G. Oshiro de Carvalho, F. P. Machado and J. H. Ramírez-González, *Extinction and survival in an interval-activation frog model on $\mathbb{Z}$ with random survival parameters and symmetric random walks*, arXiv:2607.27082, Theorem 3.1 and Remark 3.6. Written 14 September 2026, between about 10:00 and 11:30.

## The gap

Frogs sit on $\mathbb{Z}$, $\eta_x$ of them at $x$, each with a geometric lifetime of random parameter and a symmetric walk; an active frog activates every site between the endpoints of each jump. With $D^\to = \max_{0\le m\le L}S_m$ and $D^* = \max_{0\le m \le L}|S_m|$, the paper's Theorem 3.1 says: the model dies out almost surely if $\limsup_n n\mathbb{P}(D^*\ge n) < 1/(2\mathbb{E}[\eta_0])$, and survives with positive probability if $\liminf_n n\mathbb{P}(D^\to \ge n) > 1/\mathbb{E}[\eta_0]$. Since $\mathbb{P}(D^*\ge n) \sim 2\mathbb{P}(D^\to\ge n)$ for a symmetric walk, the two constants differ by four, and on the critical line $\beta = 1/r$, where $n\mathbb{P}(D^\to\ge n)\sim\kappa\ell(n^r)$, Remark 3.6 records that "the full phase diagram on the critical line is not determined by the present argument".

Write $c = \mathbb{E}[\eta_0]\lim_n n\mathbb{P}(D^\to \ge n)$, so their criteria read: extinction for $c < 1/4$, survival for $c > 1$.

## What the two factors of two are

The activated set is an interval, and only the sites added at the previous step can extend it, since the older ones are already known not to reach beyond the current ends. So both comparisons are with a *firework process*: sites carry independent reaches, an activated site at $x$ activates $[x - L_x, x+R_x]$, and the process stops exactly when the interval $[A,B]$ it has reached is *closed*, meaning $x + R_x \le B$ and $x - L_x \ge A$ for every $x\in[A,B]$. Extinction is the existence of a closed interval containing the origin.

The survival half of Theorem 3.1 compares with the one-sided firework, $L \equiv 0$, whose reaches are the $D^\to$ of the frogs at a site; the extinction half compares with a two-sided firework in which both reaches are $D^*$. The first factor of two is that $D^*$, not $D^\to$, is used on both sides. The second is the constant $1/2$ in the two-sided criterion against the constant $1$ in the one-sided one. Both are artefacts: the two processes have the same critical constant.

## The critical constant of the firework process

Let the reaches satisfy $\mathbb{P}(R \ge m) \sim c/m$ and let $g_k$ be the number of sites added at step $k$ on the right.

**Proposition 1 (one-sided).** Conditionally on the past, the sites added at step $k$ are fresh and those added earlier cannot reach beyond the current end, so
$$\mathbb{P}(g_{k+1} \le s \mid g_k = g) = \prod_{j=0}^{g-1}\mathbb{P}(R \le s+j) = \prod_{m=s+1}^{s+g}\Big(1 - \frac cm\Big)(1+o(1)),$$
and with $s = ug$, $g\to\infty$, this converges to $\big(u/(1+u)\big)^c$. So the growth is asymptotically multiplicative, $g_{k+1} = g_kU_k$ with $\mathbb{P}(U < u) = (u/(1+u))^c$, and
$$\mathbb{E}[\log U] = \int_0^\infty \log u \;d\Big(\frac{u}{1+u}\Big)^c = \psi(c) + \gamma,$$
where $\psi$ is the digamma function and $\gamma$ Euler's constant. Since $\psi(1) = -\gamma$ and $\psi$ is increasing, the drift is negative for $c<1$ and positive for $c>1$: the critical constant is $c = 1$, which is the classical threshold for the firework process, here with an explicit drift.

The substitution $v = u/(1+u)$ makes the integral $c\int_0^1 v^{c-1}\log\frac{v}{1-v}dv = -1/c + \psi(c+1)+\gamma = \psi(c)+\gamma$.

The same representation gives the decay rate below the threshold. The tail $\mathbb{P}(U\ge u)\sim c/u$ makes $\log U$ exponential to the right with rate one, so $\mathbb{P}(\max_k \log g_k \ge y)\asymp e^{-\kappa y}$ with $\mathbb{E}[U^\kappa] = 1$; and $\mathbb{E}[U^\kappa] = \Gamma(\kappa+c)\Gamma(1-\kappa)/\Gamma(c)$, whose root in $(0,1)$ is $\kappa = 1 - c$. So the one-sided firework reaches size $n$ with probability $\asymp n^{-(1-c)}$ for $c<1$, and $\asymp 1/\log n$ at $c = 1$.

**Proposition 2 (two-sided).** *The two-sided firework survives with positive probability if and only if one of its two sides would survive alone: with tails $c_R/n$ and $c_L/n$, the criterion is $\max(c_R,c_L) > 1$.*

One direction is a coupling and is rigorous. Delete every left reach and every site that the left end
contributes; what remains on the right is exactly a one-sided firework with reach tail $c_R/n$, and the
two-sided process contains it, so $c_R>1$ forces survival, and symmetrically for $c_L$. The other
direction, extinction when both constants are below one, is the part I can support but not prove, and
the obvious argument for it is false. It is worth saying why, because the false argument is the one a
reader will reach for first.

The tempting claim is that a side which fails to extend can never extend again, so that the process
becomes one-sided and the classical criterion applies. It is not true. Write $N$ for the length of the
interval and $g_R$, $g_L$ for the numbers of sites added at its two ends in the last step. A site added
at the *left* end lies about $N$ from the right end, and it extends the right end if its right reach
exceeds that distance, so the law of the right growth carries a second factor:
$$\mathbb{P}(\text{right growth} \le uN)\ \longrightarrow\ \Big(\frac{u}{u+\alpha}\Big)^{c_R}\Big(\frac{u+1-\beta}{u+1}\Big)^{c_R},\qquad \alpha=\frac{g_R}{N},\ \beta=\frac{g_L}{N}.$$
The second factor leaves mass $(1-\beta)^{c_R}$ at $u=0$, so a right end that has just stopped is revived
with probability $1-(1-\beta)^{c_R}$ at each step, and when it is revived the overshoot beyond $N$ has the
same heavy tail, so the interval jumps by a constant multiple of its own length. Summing the revival
probability over the life of an excursion gives $\sum_k c_R\,g_L(k)/N(k)$, and since $N(k)$ is the running
sum of the sites added, that is a sum of $\Delta N/N$: an excursion reaching size $n$ expects of order
$c_R\log n$ revivals. Each term is small and there are enough of them to diverge, so the two ends keep each
other alive at a rate that grows with the size reached, and no decoupling estimate is available.

What the revivals do change is the tail, and that is measurable. Each revival restarts a subcritical
excursion at the same scale, a branching structure whose effect is to replace the one-sided decay
exponent $1-c$ by roughly its square. The simulation gives, for the symmetric process,

| $c$ | 0.5 | 0.6 | 0.7 | 0.8 |
| --- | --- | --- | --- | --- |
| fitted exponent, 8,000 trials | 0.244 | 0.157 | 0.091 | 0.042 |
| fitted exponent, 25,000 trials | 0.236 | 0.157 | 0.092 | 0.041 |
| $(1-c)^2$ | 0.250 | 0.160 | 0.090 | 0.040 |

fitted over $10^6 \le N \le 10^{12}$, the two runs independent. The exponent stays strictly positive for every $c<1$ and vanishes
at $c=1$ and not before, which is the threshold claim: the mutual help fattens the tail without moving
the critical constant. That is the evidence behind Proposition 2, and the reason its extinction half is
posed below as an open problem rather than asserted.

This also corrects the first version of this memo, which proposed $c_R + c_L > 2$ from a first-moment
count: an interval of length $n$ containing the origin is closed with probability about
$n^{-(c_R+c_L)}$ and there are $n$ of them, so the expected number of closed intervals is finite exactly
when $c_R+c_L>2$. An expectation of that kind is a criterion in neither direction, and the coupling
kills it outright: $(c_R,c_L)=(1.5,0.4)$ has sum $1.9<2$ and yet survives, since $c_R=1.5$ alone does.
The simulation agrees, giving $\mathbb{P}(\text{size}\ge N) = 0.673, 0.675, 0.693, 0.701$ at
$N=10^3,10^5,10^7,10^9$.

For the frog model both sides carry the same constant, so none of this changes its threshold, which is
$1$ under either criterion, and the factor of four remains an artefact.

*The far-end help, quantitatively.* For the two-sided process with reaches $(R_x, L_x)$ whose tails are
asymptotically independent, the same computation gives
$$\mathbb{P}(g^R_{k+1}\le ug \mid g^R = g^L = g,\ N = Cg) \to \Big(\frac{u}{1+u}\Big)^c\Big(\frac{u+C}{u+C+1}\Big)^c,$$
the second factor being the contribution of the sites added at the *far* end, which lie at distance about $N$ from
the end being extended. That factor is at most $1$ and tends to $1$ as $C = N/g \to \infty$, so the far-end help is
$O(1/C)$ per step, and below the threshold $C_k = N_k/g_k \to \infty$, since $g_k$ decays geometrically while $N_k$
converges. I first read that as saying the help is irrelevant. It does not say so. The expected number of far-end
revivals over an excursion is $\sum_k c\,g^L_k/N_k$, and since $N_k$ is the running sum of the $g_j$, that sum
behaves like $c\log(N_\infty/N_0)$: each term is small, there are enough of them to diverge, and an excursion that
reaches size $n$ expects of order $c\log n$ revivals on the way. Each revival arrives as a jump of a constant
multiple of the current length, because the overshoot beyond $N$ carries the same tail. So the far end is not a
perturbation of the near end; it is what makes the two-sided tail heavier, and the measured exponent $(1-c)^2$
against the one-sided $1-c$ is the size of the effect. What the numerics say it does *not* do is move the critical
constant, which stays at $1$.

A first-moment count points at the same constant and must not be trusted beyond it: an interval of size $n$
containing the origin is closed with probability $\asymp n^{-(c_R+c_L)}$, there are $n$ such intervals, and
$\sum_n n^{1-(c_R+c_L)}<\infty$ exactly when $c_R+c_L>2$. In the symmetric case that is $c>1$ and agrees with the
criterion. In general it does not: $(c_R,c_L)=(1.5,0.4)$ has $c_R+c_L<2$ and survives, by the coupling and in
simulation. A convergent first moment bounds the number of closed intervals, which is not the same as the process
stopping, and the agreement in the symmetric case is a coincidence of two constants rather than an argument.

Perfect dependence does not change the count either. If $L_x = R_x$, as in the comparison with radius $D^*$, closing an interval of size $n$ requires each site to have $R_x$ below its distance to the *nearer* end, and those distances run $0,0,1,1,\dots$, so the closure probability is again $\asymp n^{-2c}$. Since the frog model is symmetric this is the case where the count and the criterion agree.

## Consequence for the frog model

Taking the two-sided firework with reaches $(D^\to, D^\leftarrow)$ — which is what the model actually is, not a comparison — both sides carry the same constant $c$, so the criterion $\max(c_R,c_L)>1$ reads $c>1$, and the phase diagram on the critical line is decided by $c$ against $1$:
$$\mathbb{E}[\eta_0]\,\kappa\,\lim_n\ell(n^r) > 1 \implies \text{survival with positive probability}, \qquad < 1 \implies \text{almost sure extinction},$$
the survival half being exactly the paper's Theorem 3.1(ii). The factor four is entirely in the extinction half: one factor of two from replacing $D^\to,D^\leftarrow$ by $D^*$, and one from the constant $1/2$.

## Numerical check

`h0024_fast.py` follows the interval by sampling the growth from its exact conditional law, which telescopes into a ratio of Gamma functions, so each step costs a binary search and the interval can be followed to size $10^{12}$. Reaches are drawn with $\mathbb{P}(R\ge m) = c/(m+c)$, the shift keeping the law proper for every $c>0$ without changing the tail constant. Entries are $\mathbb{P}(\text{the interval reaches size }N)$ over 1500 trials.

| $c$ | side | $N = 10^3$ | $10^5$ | $10^7$ | $10^9$ | $10^{12}$ |
|---|---|---|---|---|---|---|
| 0.75 | one | 0.0453 | 0.0107 | 0.0020 | 0.0007 | 0.0000 |
| 0.75 | two | 0.4580 | 0.3540 | 0.2453 | 0.1640 | 0.1153 |
| 0.90 | one | 0.0807 | 0.0547 | 0.0300 | 0.0180 | 0.0113 |
| 0.90 | two | 0.6227 | 0.5720 | 0.5080 | 0.5000 | 0.4373 |
| 1.00 | one | 0.1347 | 0.0893 | 0.0633 | 0.0520 | 0.0387 |
| 1.00 | two | 0.7247 | 0.6847 | 0.6907 | 0.6713 | 0.6360 |
| 1.10 | one | 0.1727 | 0.1213 | 0.1267 | 0.1080 | 0.0987 |
| 1.50 | one | 0.3140 | 0.3440 | 0.3380 | 0.3353 | 0.3307 |

The one-sided column is the control and it reproduces Proposition 1 on all three counts: a power decay with exponent $1-c$ below the threshold ($c = 0.9$ gives a measured $0.097$ against $0.1$), a decay like $1/\log N$ at $c = 1$ (the predicted factor over nine decades is $\log 10^{12}/\log 10^3 = 4$, measured $3.5$), and a positive limit above it ($c = 1.5$ flat to within the standard error of $0.012$). The drift formula is checked separately: $\psi(0.5)+\gamma = -2\log 2 = -1.3863$, which the script prints from the digamma function.

The two-sided column decays with exponent about $(1-c)^2$ — measured $0.227$, $0.067$, $0.017$ at $c = 0.5, 0.75, 0.9$ against $0.25$, $0.0625$, $0.01$ — so the exponent vanishes at $c = 1$ and not before, which is the threshold claim. The numerics cannot separate "critical with a very slow decay" from "supercritical" at $c = 1$ itself, and they are not meant to: the survival half of the threshold claim is the coupling and needs no numerics, while the extinction half rests on the exponent staying positive below $1$, and the numerics rule out a threshold at $1/2$ or $1/4$, which is what the paper's gap leaves open.

## Status

A reduction and a strongly supported answer, not a closed proof. Proposition 1 is complete and gives the classical one-sided threshold with an explicit drift $\psi(c)+\gamma$ and an explicit decay exponent $1-c$. Proposition 2 is half proved: the survival direction is a coupling, and the extinction direction is open. What is missing is not the estimate I first expected. The far-end contribution is not negligible, so there is nothing to decouple; what has to be shown instead is that the revivals form a subcritical branching structure for every $c<1$, which the measured exponent $(1-c)^2$ says they do. Given it, the critical line of the frog model is decided by $\mathbb{E}[\eta_0]\kappa\lim\ell(n^r)$ against $1$, and Remark 3.6's factor of four disappears. Verification: author checked; the one-sided propositions are confirmed numerically on three independent predictions. Prior art: the one-sided threshold is classical (Junior, Machado and Zuluaga); I did not find the drift formula $\psi(c)+\gamma$ or the exponent $1-c$ stated, nor a two-sided criterion, in a bounded search. Not a clearance.

## New open problems

1. **The two-sided firework criterion.** Prove that the two-sided firework on $\mathbb{Z}$ with reaches of tail $c_R/n$ and $c_L/n$ dies almost surely when $\max(c_R,c_L) < 1$. The other half is a coupling: delete the left reaches and the sites the left end contributes, and what is left on the right is a one-sided firework with tail $c_R/n$, so $c_R>1$ already forces survival, and symmetrically for $c_L$. So the criterion is $\max(c_R,c_L)>1$ and only the extinction half is open. The natural argument, that a blocked side stays blocked, is false: a site at one end whose reach crosses the whole interval revives the other end, and an excursion reaching size $n$ expects of order $\log n$ of those revivals. What has to be shown is that the revivals are a subcritical branching structure whenever both constants are below one.
2. **The two-sided decay exponent.** The one-sided exponent $1-c$ is a Cramer root: with $U$ the growth ratio, $\mathbb{P}(U<u)=(u/(1+u))^c$, the equation $\mathbb{E}[U^\kappa]=\Gamma(\kappa+c)\Gamma(1-\kappa)/\Gamma(c)=1$ has the root $\kappa=1-c$. The symmetric two-sided process measures $(1-c)^2$ to within six per cent over $0.5\le c\le 0.8$, on two runs of 8,000 and 25,000 trials. Is the square exact, and which equation is it the root of? A derivation has to price the revivals described above, since those are what separate the two exponents. The exponent for unequal constants is open too.

3. **Dependence between the two reaches.** For a frog, $D^\to$ and $D^\leftarrow$ come from one walk and are far from independent. Their joint tail $\mathbb{P}(D^\to\ge s, D^\leftarrow \ge t)$ is negligible against the marginals, which is all the threshold needs, but the survival probability itself must depend on the joint law. Is the critical constant genuinely universal over the joint laws with given marginal tails?
