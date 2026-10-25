# P0016. The worst-conditioned square subframe of a Gaussian frame at minimal redundancy

Random matrix theory, 13 September 2026.

## The problem is already solved

**P0016 is not open.** The rate is settled in Yitzchak Shmalo, *Extreme least singular values of
Gaussian row submatrices and a phase retrieval stability problem*, arXiv:2607.06249, 7 July 2026
(abstract fetched and read 2026-09-13; Einstein Institute, Hebrew University). Its Theorem 1.1
determines the exponential scale for every aspect ratio $\gamma>1$, and its Corollary 1.2 is exactly
Randomstrasse Open Problem 21: for $A_m\in\mathbb{R}^{(2m-1)\times m}$,
$$\tfrac1m\log\omega(A_m)\xrightarrow{P}-\log4,\qquad \omega(A_m)=4^{-m+o_P(m)},$$
with rate $\mathbb{P}\{|\tfrac1m\log\omega+\log4|>\varepsilon\}=O_\varepsilon(m^{-1})$ — so the
sharp exponential base in the Gaussian Balan--Wang problem is $1/4$.

The derivation below follows the paper's method: the same reduction to a left-out row, the same
second moment, and the same lemma about two conditionally independent Haar directions in the common
kernel (the paper's Lemma 4.1). It is recorded for two increments that the paper does not state:

* a **non-asymptotic two-sided bound at polynomial precision**: $\mathbb{P}(\omega\le\eta4^{-M})\le
  \eta/(2\sqrt\pi)$ for every $M$ and $\eta$, and $\omega\le\omega_M\sqrt M\,4^{-M}$ w.h.p. for any
  $\omega_M\to\infty$. The paper's statement is "for every $b>1/4$, $\mathbb{P}\{\omega\le R_mb^m\}
  \to1$; for every $b<1/4$ and fixed $C$, $\mathbb{P}\{\omega\le CR_mb^m\}\to0$" — exponential
  precision. Running the same second moment at the *critical* scale rather than an exponentially
  sub-critical one pins $\omega$ to within $\sqrt M$;
* a **conjectured limit law** $4^M\omega(A)\Rightarrow\mathrm{Exp}(\text{mean }2\sqrt\pi)$, with the
  numerics below. The paper states no limit law.

Ledger status: `P0016` is `resolved_in_literature`, resolver arXiv:2607.06249. The earlier attempt
row records a union-bound lower bound and a $C\log M/M$ upper bound.

## The problem

Source: `randomstrasse_2025_v1`, Open Problem 21 with Definition 10.1 (Entry 10); ledger id `P0016`,
status `attempted_unsolved`, verification `author_checked_limited_argument`.

As recorded: for a $(2M-1)\times M$ matrix $A$ of independent standard real Gaussians, determine the
asymptotic size of

$$\omega(A) \;=\; \min\big\{\sigma_{\min}(A_S)\;:\; S\subseteq[2M-1],\ \operatorname{rank}(A_{S^c})<M\big\},$$

in particular whether the decay is exponential and what the exponential rate is.

Two immediate normalisations. Almost surely every $M$ rows of $A$ are linearly independent, so
$\operatorname{rank}(A_{S^c})=\min(|S^c|,M)$ and the admissible sets are exactly those with
$|S|\ge M$. And $\sigma_{\min}(A_S)=\min_{\|x\|=1}\|A_Sx\|$ is nondecreasing under adjoining rows,
so the minimum is attained on sets of size exactly $M$:

$$\omega(A)=\min_{|S|=M}\sigma_{\min}(A_S),\qquad \#\{S\}=\binom{2M-1}{M}=\tfrac12\binom{2M}{M}\sim\frac{4^M}{2\sqrt{\pi M}} .$$

(Checked numerically, break test B1 below: over 300 draws at $M=4$ the minimum over $|S|=M+1$ never
fell below the minimum over $|S|=M$.)

What the quantity is. The condition "$\operatorname{rank}(A_{S^c})<M$" is the failure clause of the
*complement property* of Balan, Casazza and Edidin, the condition under which real phase retrieval
from $\{|\langle a_i,x\rangle|\}$ is injective; $2M-1$ is the minimal generic number of measurements
in $\mathbb{R}^M$. So $\omega(A)$ is a stability constant for phase retrieval at minimal redundancy,
and the question is how badly conditioned that problem is for a random frame.

## The earlier record

The ledger's last attempt on `P0016` proved

* a **lower** bound $\omega \ge \exp(-(\log 4+\epsilon)M)$ with probability $\to1$, by a union bound
  over the $\le 4^M$ square subframes together with
  $\mathbb{P}(\sigma_{\min}(G_M)\le t)\le\sqrt{2/\pi}\,M^{3/2}t$;
* an **upper** bound $\omega \le C\log M/M$ with probability $\to1$, by fixing $M-1$ rows, taking the
  unit normal $x$ of their span, and minimising $|\langle a_j,x\rangle|$ over the remaining $M$ rows.

So the record had an exponential lower bound against a *polynomial* upper bound: whether the decay is
exponential at all was open in the record. The theorem below settles it, as does arXiv:2607.06249.

## Result

**Theorem.** Let $A$ be $(2M-1)\times M$ with i.i.d. $N(0,1)$ entries.

1. (Lower.) For every $\eta\in(0,1]$ and every $M\ge2$,
   $$\mathbb{P}\big(\omega(A)\le \eta\,4^{-M}\big)\;\le\;\frac{\eta}{2\sqrt{\pi}} .$$
2. (Upper.) If $\varepsilon_M>0$ satisfies $\varepsilon_M\,4^{M}/\sqrt{M}\to\infty$, then
   $\mathbb{P}(\omega(A)\le\varepsilon_M)\to1$. In particular $\mathbb{P}(\omega(A)\le M\,4^{-M})\to1$.

Consequently the decay **is** exponential, the rate is exactly $\log 4$,

$$\frac1M\log\omega(A)\;\longrightarrow\;-\log 4\qquad\text{in probability},$$

and in fact $\omega(A)=4^{-M}$ up to a factor that is bounded below in probability and at most
$\omega_M\sqrt M$ for any $\omega_M\to\infty$.

Numerically (break test B3 and the table below) the sharper statement appears to hold:
$4^M\omega(A)$ converges in distribution to an exponential law. That last sentence is a
**conjecture supported by simulation only**; parts 1 and 2 are proved.

## Proof of part 1 (lower bound)

For a single $M$-subset $S$, $A_S$ is an $M\times M$ standard real Gaussian matrix. Edelman's exact
computation (equivalently Szarek's bound) gives

$$\mathbb{P}\big(\sigma_{\min}(G_M)\le t\big)\;\le\; t\sqrt{M}\qquad (t\ge0). \tag{$\ast$}$$

A self-contained weaker version needs nothing and suffices for the rate: if $\|G x\|\le t$ with
$\|x\|=1$ then some $|x_k|\ge M^{-1/2}$, and writing $Gx=\sum_i x_ic_i$ over the columns $c_i$,
$\operatorname{dist}(c_k,\operatorname{span}\{c_i\}_{i\ne k})\le t/|x_k|\le t\sqrt M$. Conditionally
on the other columns that distance is distributed as $|N(0,1)|$ (or a larger $\chi$), so
$\mathbb{P}(\sigma_{\min}(G_M)\le t)\le M\cdot\sqrt{2/\pi}\,t\sqrt M=\sqrt{2/\pi}M^{3/2}t$.

Union bound over the $\binom{2M-1}{M}\le 4^M/(2\sqrt{\pi M})$ square subframes, with $(\ast)$ and
$t=\eta4^{-M}$:

$$\mathbb{P}(\omega\le\eta4^{-M})\;\le\;\frac{4^M}{2\sqrt{\pi M}}\cdot\eta4^{-M}\sqrt M=\frac{\eta}{2\sqrt\pi}. \qquad\square$$

The $\sqrt M$ in $(\ast)$ and the $\sqrt M$ in the binomial cancel exactly. That cancellation is why
the answer has no polynomial factor, and it is why one should expect $4^M\omega$ to have a limit law.

*Numerical check of $(\ast)$.* The density of $\sigma_{\min}(G_M)$ at $0$, call it $\kappa_M$, was
estimated by Monte Carlo with Richardson extrapolation ($4\cdot10^5$ draws per $M$):
$\kappa_M/\sqrt M =$ 0.920, 0.914, 0.933, 0.966, 0.993, 0.972, 0.958, 0.968, 0.993 for
$M=2,\dots,10$. All below 1, consistent with $(\ast)$ and with $\kappa_M\sim\sqrt M$. I do **not**
extrapolate that ratio past $M=10$; the theorem does not need it.

## Proof of part 2 (upper bound)

Write $m=M-1$, let $B$ be the first $2m=2M-2$ rows of $A$ and $g=a_{2M-1}$ the last row, so $g\sim
N(0,I_M)$ is independent of $B$. For $T\in\binom{[2m]}{m}$ let $x_T$ be a unit vector spanning
$\ker(B_T)$ (a.s. one-dimensional: $m$ rows, $M=m+1$ columns). Put $N=\binom{2m}{m}$.

For every $T$ the set $S=T\cup\{2M-1\}$ has $|S|=M$ and $A_Sx_T$ has a single nonzero entry
$\langle g,x_T\rangle$, so

$$\omega(A)\;\le\;\min_{T}\;|\langle g,x_T\rangle| . \tag{1}$$

(Break test B2: verified numerically at $M=5$ on 200 draws, no violation.)

Fix $\varepsilon>0$ and set $Z=\#\{T:|\langle g,x_T\rangle|\le\varepsilon\}$, so $Z\ge1$ implies
$\omega\le\varepsilon$. Since $x_T$ is a unit vector measurable with respect to $B$ and $g$ is an
independent standard Gaussian, $\langle g,x_T\rangle\sim N(0,1)$ for every $T$, whence

$$\mathbb{E}Z=Nq,\qquad q:=2\Phi(\varepsilon)-1 .$$

$\mathbb{E}Z$ is deterministic — it does not depend on $B$ at all — which is what makes an
unconditional second moment enough.

**Lemma (the exact pair law).** Let $T\ne T'$ be $m$-subsets of $[2m]$ with $|T\setminus T'|=d$. Then

$$\rho_{TT'}:=\langle x_T,x_{T'}\rangle \;\overset{d}{=}\;\langle u,v\rangle,\qquad u,v
\ \text{i.i.d. uniform on } S^{d}\subset\mathbb{R}^{d+1}.$$

*Proof.* Put $C=T\cap T'$ ($|C|=m-d$), $U=T\setminus T'$, $U'=T'\setminus T$; $U$ and $U'$ are
disjoint and disjoint from $C$. Condition on the rows $B_C$. Almost surely $K:=\ker(B_C)$ has
dimension $M-(m-d)=d+1$. For $v\in K$ and any row $b$, $\langle b,v\rangle=\langle P_Kb,v\rangle$, so
$x_T$ is the unit vector of $K$ orthogonal to $\{P_Kb_i\}_{i\in U}$ and $x_{T'}$ the one orthogonal
to $\{P_Kb_i\}_{i\in U'}$. The rows $\{b_i\}_{i\in U\cup U'}$ are i.i.d. $N(0,I_M)$ and independent
of $B_C$, hence their projections are i.i.d. standard Gaussians on $K\cong\mathbb{R}^{d+1}$; $d$ of
them a.s. span a $d$-dimensional subspace, and the direction of the orthogonal complement inside $K$
is uniform on the sphere of $K$ by rotational invariance. Because $U\cap U'=\emptyset$ the two
families are independent, so $x_T,x_{T'}$ are conditionally i.i.d. uniform on $S(K)\cong S^d$. The
conditional law does not depend on $B_C$, so it is also the unconditional law. $\square$

The lemma gives $\rho$ the density $c_d(1-\rho^2)^{(d-2)/2}$ on $[-1,1]$, and hence, using
$\int_{-1}^1(1-\rho^2)^{a-1}d\rho=\sqrt\pi\,\Gamma(a)/\Gamma(a+\tfrac12)$,

$$g(d):=\mathbb{E}\big[(1-\rho^2)^{-1/2}\big]=\frac{\Gamma(\frac{d-1}{2})\,\Gamma(\frac{d+1}{2})}{\Gamma(\frac d2)^2},
\qquad g(1)=\infty,\ g(2)=\frac\pi2,\ g(3)=\frac4\pi,\ g(d)=1+\tfrac1{2d}+O(d^{-2}).$$

(Lemma and formula both checked against direct simulation; see `p0016_checks.py`. The closed form
agrees with Monte Carlo to four decimals at $d=2,3,4,5,8,16,32,64$.)

Now the second moment. For $T\ne T'$, conditionally on $B$ the pair
$(\langle g,x_T\rangle,\langle g,x_{T'}\rangle)$ is a centred bivariate Gaussian with unit variances
and correlation $\rho_{TT'}$, whose density is bounded by $(2\pi\sqrt{1-\rho^2})^{-1}$. Hence

$$\mathbb{P}\big(|\langle g,x_T\rangle|\le\varepsilon,\ |\langle g,x_{T'}\rangle|\le\varepsilon\big)\;\le\;\min\Big(q,\ \tfrac2\pi\varepsilon^2(1-\rho_{TT'}^2)^{-1/2}\Big).$$

The number of ordered pairs with $|T\setminus T'|=d$ is $N\binom md^2$, and $\sum_d\binom md^2=N$ by
Vandermonde. Therefore

$$\mathbb{E}Z^2\;\le\;\underbrace{Nq}_{T=T'}\;+\;N m^2\,P_1\;+\;\tfrac2\pi\varepsilon^2N\!\!\sum_{d\ge2}\binom md^2 g(d).$$

*The $d=1$ term.* Here $\rho=\cos\theta$ with $\theta$ uniform on $[0,\pi]$, so with
$\sin\theta\ge 2\theta/\pi$ on $[0,\pi/2]$ and crossover $\theta_0=\varepsilon^2/q$,

$$P_1\le\tfrac2\pi\!\int_0^{\pi/2}\!\min\!\Big(q,\tfrac{\varepsilon^2}{\theta}\Big)d\theta
=\tfrac2\pi\varepsilon^2\Big(1+\log\tfrac{\pi}{2\theta_0}\Big)\le C\varepsilon^2\big(1+\log\tfrac1\varepsilon\big).$$

Crucially this is $O(\varepsilon^2\log\frac1\varepsilon)$, not $O(\varepsilon)$: the nearly parallel
null directions cost almost nothing.

*The $d\ge2$ terms.* Let $H$ be the hypergeometric variable with $\mathbb{P}(H=d)=\binom md^2/N$
(the law of $|T\setminus T'|$ for a uniform $T'$). Then

$$S(m):=\frac1N\sum_{d\ge2}\binom md^2g(d)=\mathbb{E}\big[g(H)\mathbf 1_{H\ge2}\big]
\le 1+\mathbb{E}\big[(g(H)-1)\mathbf 1_{H\ge2}\big]\le 1+\frac{C}{m}+\Big(\frac\pi2-1\Big)e^{-cm},$$

because $g$ is decreasing with $g(d)-1=O(1/d)$, $H$ concentrates at $m/2$ with Gaussian tails, and
$g(d)\le\pi/2$ for all $d\ge2$. Computed exactly: $S(m)-1 =$ 1.16e-1, 2.03e-1, 7.76e-2, 3.45e-2,
1.64e-2, 8.00e-3, 3.95e-3, 1.96e-3 for $m=4,8,16,32,64,128,256,512$ — i.e. $S(m)=1+\frac1m+o(\frac1m)$.

Finally $q=\sqrt{2/\pi}\,\varepsilon(1+O(\varepsilon^2))$, so
$\frac2\pi\varepsilon^2=q^2(1+O(\varepsilon^2))$ and

$$\frac{\mathbb{E}Z^2}{(\mathbb{E}Z)^2}\;\le\;\frac1{Nq}\;+\;\frac{Cm^2\log\frac1\varepsilon}{N}\;+\;S(m)\big(1+O(\varepsilon^2)\big).$$

Take $\varepsilon=\varepsilon_M$ with $\varepsilon_M4^M/\sqrt M\to\infty$. Then
$Nq\asymp\varepsilon_M4^M/\sqrt M\to\infty$, and $m^2\log\frac1{\varepsilon_M}\le CM^3$ while
$N\asymp4^M/\sqrt M$, so the middle term is exponentially small. Hence
$\mathbb{E}Z^2\le(1+O(1/M))(\mathbb{E}Z)^2$ and by Cauchy--Schwarz

$$\mathbb{P}(\omega\le\varepsilon_M)\ \ge\ \mathbb{P}(Z\ge1)\ \ge\ \frac{(\mathbb{E}Z)^2}{\mathbb{E}Z^2}\ \ge\ 1-O(1/M)\longrightarrow1. \qquad\square$$

## Where the argument could fail

The strongest case against it:

* **The Lemma is the whole argument.** If the conditional law of $(x_T,x_{T'})$ were *not* two
  independent uniform directions — if the null-vector selection introduced a bias — then $g(d)$
  would be wrong and $S(m)$ could exceed $1$ by a constant. That would cost only the $1-o(1)$:
  Paley--Zygmund would still give probability bounded below, and the rate $\log4$ would survive.
  *Concrete check, done:* the empirical quantiles of $|\rho_{TT'}|$ at
  $(M,d)=(6,1),(6,2),(6,3),(6,5),(9,2),(9,4),(9,8)$ match the $S^d$ prediction to the third decimal
  on 4000 draws each.
* **The $d=1$ logarithm.** If $P_1$ were really of order $\varepsilon$ rather than
  $\varepsilon^2\log\frac1\varepsilon$, the constraint on $\varepsilon$ would tighten from
  $\varepsilon\gg\sqrt M4^{-M}$ to $\varepsilon\gg M^24^{-M}$ — a polynomial loss only. So the
  exponential-rate content is robust to both of the places I would most expect an error.
* **The lower bound leans on $(\ast)$.** If the sharp constant in $(\ast)$ were wrong, the statement
  $\mathbb{P}(\omega\le\eta4^{-M})\le\eta/(2\sqrt\pi)$ would change by a constant; with the
  self-contained $M^{3/2}$ bound one still gets $\mathbb{P}(\omega\le\eta4^{-M})\le CM\eta$, which
  gives the rate.
* **The reduction $\omega=\min_{|S|=M}\sigma_{\min}(A_S)$.** If the source's Definition 10.1 meant
  something else — the complement of a *column* subset, say, or a max-min rather than a min —
  everything changes. `LITERATURE_P2.md` quotes Definition 10.1 from the source, and it matches the
  reduction used here.

*The most informative single falsification*: simulate $4^M\omega(A)$ at $M=10$ and $M=12$ and see
whether the median moves. If the rate were $r\ne4$ the median of $4^M\omega$ would move by a factor
$(4/r)^2$ between them. It does not move.

## Numerical record

Direct computation of $\omega(A)$ by exhaustive minimisation over all $\binom{2M-1}{M}$ square
subframes (`p0016_sim.py`, seed 11):

| $M$ | trials | median $\omega$ | $\frac1M\log_4\omega$ | median $4^M\omega$ | #subsets |
|---|---|---|---|---|---|
| 2 | 4000 | 1.790e-01 | -0.620 | 2.865 | 3 |
| 3 | 4000 | 4.528e-02 | -0.744 | 2.898 | 10 |
| 4 | 3000 | 1.138e-02 | -0.807 | 2.914 | 35 |
| 5 | 2000 | 2.514e-03 | -0.864 | 2.574 | 126 |
| 6 | 1200 | 6.610e-04 | -0.880 | 2.707 | 462 |
| 7 | 600 | 1.611e-04 | -0.900 | 2.640 | 1716 |
| 8 | 300 | 3.607e-05 | -0.922 | 2.364 | 6435 |
| 9 | 150 | 8.805e-06 | -0.933 | 2.308 | 24310 |
| 10 | 60 | 2.494e-06 | -0.931 | 2.615 | 92378 |

The last column is flat over a range in which $\omega$ itself falls by five orders of magnitude.
That is the evidence for $\omega\asymp4^{-M}$ with no polynomial factor, beyond what is proved. The
$\frac1M\log_4\omega$ column drifts towards $-1$ slowly, exactly as a constant prefactor predicts.

The Poisson heuristic — treat the $\binom{2M-1}{M}$ events $\{\sigma_{\min}(A_S)\le\varepsilon\}$ as
independent — predicts $\mathbb{P}(\omega>\varepsilon)\approx\exp(-\binom{2M-1}{M}\kappa_M\varepsilon)$
and hence a median of $\log2/(\binom{2M-1}{M}\kappa_M)$. Against the measured medians
(`kappa.py`), the ratio measured/predicted is 1.009, 1.034, 1.072, 0.987, 1.072, 1.025, 0.908,
0.897, 1.043 for $M=2,\dots,10$: within 10% with no trend. In the limit
$\binom{2M-1}{M}\kappa_M4^{-M}\to1/(2\sqrt\pi)$, giving the conjecture

$$4^M\omega(A)\ \Longrightarrow\ \mathrm{Exp}\big(\text{mean }2\sqrt\pi=3.545\big),$$

whose median is $2\sqrt\pi\log2=2.457$ against the observed $2.3$–$2.9$. **Conjecture, numerics
only.** Proving it needs a Chen--Stein argument over overlapping subsets, which the second moment
above does not supply.

## Status

* $\frac1M\log\omega(A)\to-\log4$ in probability: **known** (arXiv:2607.06249, Cor. 1.2); proved
  the proof above follows the same method.
* $\mathbb{P}(\omega\le\eta4^{-M})\le\eta/(2\sqrt\pi)$: **proved** modulo the cited sharp form of
  $(\ast)$; **proved** unconditionally with an extra factor $M$.
* $\omega\le\omega_M\sqrt M4^{-M}$ w.h.p. for any $\omega_M\to\infty$: **proved**.
* $4^M\omega\Rightarrow\mathrm{Exp}(2\sqrt\pi)$: **conjecture, numerical support only**.

## Remaining obligation

Close the polynomial gap between $c4^{-M}$ and $\omega_M\sqrt M4^{-M}$, i.e. prove the limit law.
   **The reduction below is exact and reduces the whole thing to one concentration statement.**

### The exact reduction for the limit law

Run the second moment on the full family. Let $Y_\varepsilon=\#\{S:|S|=M,\ \sigma_{\min}(A_S)\le
\varepsilon\}$, $N=\binom{2M-1}{M}$, $p=\mathbb{P}(\sigma_{\min}(G_M)\le\varepsilon)$, so
$\mathbb{E}Y=Np$.

Fix $S\ne S'$ and let $C=S\cap S'$, $|C|=k\ge1$. The conditional-independence step, written out:
the index sets $C$, $S\setminus C$, $S'\setminus C$
are pairwise disjoint, the rows of $A$ are i.i.d., so $A_C$, $A_{S\setminus C}$, $A_{S'\setminus C}$
are three independent random matrices. The matrix $A_S$ consists exactly of the rows in $C$ and in
$S\setminus C$, so $\sigma_{\min}(A_S)=f(A_C,A_{S\setminus C})$ for a fixed measurable $f$ (it does
not depend on the order of the rows), and likewise
$\sigma_{\min}(A_{S'})=f(A_C,A_{S'\setminus C})$. Two measurable functions of $(A_C,X)$ and
$(A_C,X')$ with $X\perp X'$ and both independent of $A_C$ are conditionally independent given $A_C$.
Writing, for a
$k\times M$ matrix $B$,
$$\varphi_\varepsilon(B)\ :=\ \mathbb{P}\Big(\sigma_{\min}\begin{bmatrix}B\\ G\end{bmatrix}\le\varepsilon\Big),
\qquad G\ (M-k)\times M\ \text{standard Gaussian},$$
we get *exactly*
$$\mathbb{P}(\text{both})=\mathbb{E}\big[\varphi_\varepsilon(A_C)^2\big],\qquad
\mathbb{P}(\text{one})=\mathbb{E}\big[\varphi_\varepsilon(A_C)\big]=p,\qquad
\frac{\mathbb{P}(\text{both})}{p^2}=1+\rho_k,\quad
\rho_k:=\frac{\operatorname{Var}\varphi_\varepsilon(A_C)}{(\mathbb{E}\varphi_\varepsilon(A_C))^2}.$$
Summing, with $N_k$ the number of ordered pairs of overlap $k$,
$$\mathbb{E}\big[Y(Y-1)\big]=p^2\Big(N(N-1)+\sum_k N_k\rho_k\Big),$$
so the Poisson factorial-moment condition $\mathbb{E}[Y(Y-1)]\to\lambda^2=(Np)^2$ holds **iff**
$$\sum_k \frac{N_k}{N^2}\,\rho_k\ \longrightarrow\ 0 ,$$
and $N_k/N^2$ is the hypergeometric law of the overlap of two uniform $M$-subsets of $[2M-1]$,
concentrated at $k\approx M/2$ with Gaussian tails. Higher factorial moments factor the same way
(condition on the rows shared by the whole $r$-tuple), so the method of moments applies verbatim.

So everything reduces to: **is $\rho_k$ small for $k$ near $M/2$?** Two observations make this
plausible and put it in the territory of that paper. First, $\varphi_\varepsilon(B)$ depends on $B$
only through its singular values: $\varphi_\varepsilon(UBO)=\varphi_\varepsilon(B)$ for orthogonal
$U\in O(k)$, $O\in O(M)$, because $G\mapsto GO$ is distribution-preserving and left multiplication
by $\mathrm{diag}(U,I)$ preserves singular values. Second, for $k\approx M/2$ the singular values of
a $k\times M$ Gaussian obey a Marchenko–Pastur law with $O(1)$ (not $O(M)$) fluctuations of smooth
linear statistics. A concentration statement for $\varphi_\varepsilon$ as a functional of that
spectrum is the whole remaining content.

The two ends of the range are known by hand and bracket the question: $\rho_{M-1}>0$ strictly (there
$\varphi_\varepsilon(B)\propto\varepsilon\,h(B)$ with $h$ genuinely random, and
$\mathbb{E}h^2>(\mathbb{E}h)^2$ by Jensen), but those pairs number only $O(4^MM^2)$ against
$O(16^M)$ in total, so they cost nothing; $\rho_k$ for small $k$ should be near zero since $A_C$
then carries almost no information.

**Measured** (`p0016_rho_k.py`, 250–400 draws of $B$ and $6000$–$20000$ completions each,
$\varepsilon=0.02/\sqrt M$, binomial sampling noise subtracted):

| | $k=1$ | 2 | $M/2$ | $3M/4$ | $M-2$ | $M-1$ |
|---|---|---|---|---|---|---|
| $M=6$ | 0.005 | 0.024 | 0.033 | — | 0.086 | 7.99 |
| $M=8$ | 0.001 | 0.004 | 0.013 | 0.111 | 0.111 | 1.69 |
| $M=10$ | 0.001 | 0.003 | 0.015 | 0.051 | — | — |

At the overlap that carries all the weight, $k=M/2$, $\rho_k$ is $0.033,\,0.013,\,0.015$ for
$M=6,8,10$: small, and not growing. It blows up only at $k=M-1$, where Jensen forces it, and even
there it falls with $M$ ($7.99\to1.69$) while its weight $N_{M-1}/N^2=O(M^24^{-M})$ vanishes
exponentially. So every ingredient of the limit law is in place except a proof that
$\rho_{M/2}\to0$, and that is a Marchenko–Pastur concentration statement about a rotation-invariant
functional of the singular values of a half-height Gaussian block.

## Files

All in `code/`, with each script's output beside it as `.out`:
`p0016_checks.py` (Lemma, $g(d)$, $S(m)$), `p0016_sim.py` (exhaustive $\omega$), `kappa.py`
($\kappa_M$ and the Poisson prediction), `p0016_break.py` (break tests B1--B3).
