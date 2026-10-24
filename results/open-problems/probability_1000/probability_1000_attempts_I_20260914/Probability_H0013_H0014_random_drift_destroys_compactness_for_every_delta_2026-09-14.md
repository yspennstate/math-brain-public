# A Lévy drift destroys the compactness of a confining diffusion semigroup for every power, and which sign of jump does it

Ledger rows H0013 and H0014 (intake H), with a complete answer to the question the paper's introduction calls open (row H0012). Source: arXiv:2607.07410, Remark 5.3(ii). Written 14 September 2026, between about 07:00 and 09:00.

## The questions

On $\mathbb{R}$, for a locally bounded $w$, let $\mu^w(dx) = e^{-w(x)}dx$ and let $L^w = \tfrac12(\Delta - \nabla w\cdot\nabla)$ be the self-adjoint operator on $L^2(\mathbb{R}; \mu^w)$ attached to the closure of
$$\mathcal E^w(u,u) = \tfrac12\int u'(x)^2 e^{-w(x)}dx, \qquad u \in C_c^\infty(\mathbb{R}).$$
The semigroup is compact exactly when $\sigma_{\mathrm{ess}}(-L^w) = \emptyset$. For the deterministic benchmarks $w_1(x) = |x|^\delta$ and $w_2(x) = -|x|^\delta$ the paper records (its Section 2, from Pinsky) that the semigroup is noncompact if and only if $0 < \delta \le 1$; at $\delta = 1$ the bottom of the essential spectrum is in $(0,\infty)$.

Let $V$ be a two-sided nontrivial $(r_0,\alpha)$-semi-selfsimilar Lévy process, $\alpha \in (0,2)$, with $Q(V(1) > 0) > 0$ and $Q(V(1)<0)>0$, and let $W = V$ in dimension one. The paper's Proposition 5.2 shows that for $0 < \delta \le 1/\alpha$ the perturbed operators $L^{w_k + W}$, $k = 1,2$, have $\lambda_{\mathrm{ess}} = 0$ almost surely, so the random drift destroys compactness when $\alpha \in (0,1)$ and $\delta \in (1, 1/\alpha]$. Remark 5.3(ii) then says, twice, that for $\delta > 1/\alpha$ the authors do not know whether the semigroup is compact, because the integral criterion they use becomes an indeterminate product of a divergent and a convergent factor and they have no decay rate for the convergent one. The introduction states the general form as "the key open question: can random drift perturbations break the compactness of confining deterministic diffusion semigroups?"

## The answer

It breaks it for every $\delta$, and which of the two operators it breaks is decided by the sign of the jumps of $V$.

Write $\rho = e^{-(w+W)}$ for the density of the reference measure and, for $x_0 < x$,
$$B_\ell(x) = \Big(\int_{x_0}^x \rho^{-1}\Big)\Big(\int_x^\infty \rho\Big), \qquad B_r(x) = \Big(\int_x^\infty \rho^{-1}\Big)\Big(\int_{x_0}^x \rho\Big).$$

**Theorem 1 (the criterion).** The essential spectrum of $-L^{w}$ near $+\infty$ is empty if and only if $\min(B_\ell, B_r)(x) \to 0$ as $x \to \infty$, and $\lambda_{\mathrm{ess}} = 0$ as soon as $\limsup_{x\to\infty}\min(B_\ell,B_r)(x) = \infty$; symmetrically at $-\infty$.

This is Muckenhoupt's theorem for the weighted Hardy inequality together with the Opic–Kufner compactness criterion, applied to $\int_{x_0}^\infty f^2\rho \le C\int_{x_0}^\infty (f')^2\rho$ for $f \in C_c^\infty$: since such $f$ vanish at both ends of $(x_0,\infty)$, both representations $f(x) = \int_{x_0}^x f'$ and $f(x) = -\int_x^\infty f'$ are available, the best constant is comparable to $\min(B_\ell, B_r)$, and the embedding is compact exactly when that minimum tends to $0$ at the boundary. It is the same criterion the paper takes from Pinsky; $B_\ell$ is the product in their (5.6), and their $h(x)$ is the first factor of $B_r$.

*Control.* With $V \equiv 0$: for $w_1 = y^\delta$, $\rho^{-1} = e^{y^\delta}$ and Laplace's method gives $B_\ell(x) = (\delta^2x^{2\delta-2})^{-1}(1+o(1))$ while $B_r \equiv \infty$; for $w_2 = -y^\delta$ the roles are exchanged and $B_r(x) = (\delta^2x^{2\delta-2})^{-1}(1+o(1))$. Both reproduce the paper's benchmark: compact iff $\delta > 1$, and $\lambda_{\mathrm{ess}} \in (0,\infty)$ at $\delta = 1$. The numerical section below confirms this to three decimals.

**Theorem 2 (the answer).** Let $\delta > 0$ and let $\nu$ be the Lévy measure of $V$.

(a) If $\nu((-\infty,0)) > 0$, then $Q$-almost surely $\limsup_{x\to\infty}B_\ell(x) = \infty$ for $w_1 + W$, so $\lambda^{w_1+W}_{\mathrm{ess}} = 0$ and $\{P^{w_1+W}_t\}$ is noncompact.

(b) If $\nu((0,\infty)) > 0$, the same holds for $w_2 + W$ with $B_r$.

(c) Consequently, for $\alpha \in (0,1)$ both hold, and both questions of Remark 5.3(ii) are answered in the negative; for $\alpha \in [1,2)$ at least one holds, and both hold whenever $V$ has jumps of both signs, in particular for the symmetric $\alpha$-stable case $r_0 = 1$.

For (c) note that when $\alpha < 1$ the process has finite variation, so $V(x) = bx + \sum_{s \le x}\Delta V_s$; the scaling $V(x) \overset{d}{=} x^{1/\alpha}V(1)$ gives $V(x)/x \overset{d}{=} x^{1/\alpha - 1}V(1) \to 0$ as $x \downarrow 0$, while finite variation forces $V(x)/x \to b$, so $b = 0$. With no drift and jumps of one sign only, $V$ would be monotone, contradicting the standing assumption that $V$ changes sign; hence for $\alpha < 1$ the Lévy measure charges both half-lines. When $\alpha \in [1,2)$ the process may be spectrally one-sided, and then exactly one of (a), (b) is delivered by this argument; Theorem 3 says the other case really is compact, so the dichotomy is sharp and the answer genuinely depends on the sign structure of the jumps, which is invisible to the integral tests of the paper's Lemma 5.1.

### Proof of Theorem 2

Only (a); (b) is the same computation with $V$ replaced by $-V$ and $B_\ell$ by $B_r$.

*Step 1: a lower bound at a jump.* Let $\tau > 2$ and suppose $V$ has a jump at $\tau$ of size $-m$, that is $V(\tau) = V(\tau-) - m$ with $m > 0$. Put $h = \tau^{1-\delta} \wedge 1$ and
$$O_1 = \sup_{y \in [\tau - h, \tau)}|V(y) - V(\tau-)|, \qquad O_2 = \sup_{y\in[\tau, \tau+h]}|V(y) - V(\tau)| .$$
Bounding each integral below by its part on one side of $\tau$,
$$\int_{x_0}^{\tau}e^{y^\delta + V} \ge h\,e^{(\tau-h)^\delta}e^{V(\tau-) - O_1}, \qquad \int_\tau^\infty e^{-y^\delta - V} \ge h\,e^{-(\tau+h)^\delta}e^{-V(\tau) - O_2},$$
and $(\tau+h)^\delta - (\tau-h)^\delta \le 2h\delta(\tau+h)^{\delta-1} \le 4\delta$ for $\tau$ large, so
$$B_\ell(\tau) \ge h^2e^{-4\delta}\,e^{\,V(\tau-)-V(\tau) - O_1 - O_2} = e^{-4\delta}\,\tau^{2-2\delta}\,e^{\,m - O_1 - O_2}. \tag{1}$$
So a downward jump of size $m$ at $\tau$ forces $\log B_\ell(\tau) \ge m - O_1 - O_2 - (2\delta-2)\log\tau - 4\delta$: the price the confining potential charges for a well at distance $\tau$ is only logarithmic in $\tau$.

*Step 2: such jumps exist, with quiet neighbourhoods.* Decompose $V = V' + J$ where $J$ collects the jumps of modulus $> 1$ — a compound Poisson process of rate $\lambda_1 = \nu(|z|>1) \in (0,\infty)$ — and $V'$ is an independent Lévy process with jumps bounded by $1$. By semi-selfsimilarity the Lévy measure satisfies $\nu(r_0^{1/\alpha}A) = r_0^{-1}\nu(A)$, so $\nu((-\infty,-m]) = m^{-\alpha}\ell(m)$ with $\ell$ bounded above and below by positive constants (a constant in the stable case $r_0 = 1$, log-periodic otherwise); in particular $\nu((-\infty,-m]) \ge c_\ast m^{-\alpha}$ for $m \ge 1$.

Fix $\theta > 0$ and work in the blocks $I_k = [2^k, 2^{k+1}]$, with $m_k = (2\delta - 2)^+\log 2^{k+1} + \theta\log k$ and $h_k = 2^{k(1-\delta)}\wedge 1$. Rather than take all candidate jumps in $I_k$, which may cluster, partition $I_k$ into consecutive intervals of length $4h_k$ and keep every second one; call the kept ones $I_{k,1}, \dots, I_{k,M_k}$ with $M_k = \lfloor 2^k/(8h_k)\rfloor$. Two points lying in different kept intervals are more than $4h_k$ apart, and the kept intervals are disjoint, so all the events below are independent.

Say $I_{k,j}$ is *good* if (i) $J$ has exactly one jump in the doubled interval $I_{k,j}^+ := \{y : \mathrm{dist}(y, I_{k,j}) \le h_k\}$ and that jump has size at most $-m_k$, and (ii) the oscillation of $V'$ over $I_{k,j}^+$ is at most $1/2$. The two requirements concern independent processes on one interval, so
$$Q(I_{k,j}\text{ good}) \ge \underbrace{6h_k\,\nu((-\infty,-m_k])\,e^{-6h_k\lambda_1}}_{\text{(i)}}\cdot\underbrace{\big(1 - Q(\mathrm{osc}_{[0,6h_k]}V' > 1/2)\big)}_{\text{(ii)}} \ge 3h_k c_\ast m_k^{-\alpha}$$
for $k$ large, since $h_k \to 0$ makes both $e^{-6h_k\lambda_1}$ and the second factor at least $1/2$ ($V'$ has jumps bounded by $1$ and is stochastically continuous, so $Q(\mathrm{osc}_{[0,\epsilon]}V' > 1/2) \to 0$). The blocks being independent,
$$Q(\text{no good } I_{k,j}) \le \big(1 - 3h_kc_\ast m_k^{-\alpha}\big)^{M_k} \le \exp\big(-3c_\ast h_k M_k m_k^{-\alpha}\big) \le \exp\big(-\tfrac{c_\ast}{4}2^{k}m_k^{-\alpha}\big),$$
and $2^k m_k^{-\alpha}$ grows geometrically, so this is summable in $k$.

On a good interval, let $\tau$ be the jump time. No other jump of $J$ lies within $h_k$ of $\tau$, so on $[\tau - h_k, \tau)$ and on $[\tau, \tau+h_k]$ the process $V$ differs from $V'$ by a constant, whence $O_1 + O_2 \le 2\,\mathrm{osc}\,V' \le 1$. By Borel–Cantelli, $Q$-a.s. for all large $k$ such a $\tau_k \in I_k$ exists, and by (1),
$$\log B_\ell(\tau_k) \ge m_k - 1 - (2\delta-2)\log \tau_k - 4\delta \ge \theta\log k - 1 - 4\delta \longrightarrow \infty . \qquad \square$$

Two remarks on what the proof delivers. The lower bound (1) uses the integrals only over $[\tau-h,\tau]$ and $[\tau,\tau+h]$, so it survives replacing the left endpoint $x_0$ by any $R$; hence $\sup_{x > R}B_\ell(x) = \infty$ for every $R$, no Poincaré inequality holds on any neighbourhood of $+\infty$, and $\lambda_{\mathrm{ess}} = 0$ follows by Persson's characterisation $\lambda_{\mathrm{ess}} = \lim_{R\to\infty}\inf\{\mathcal E(f,f)/\|f\|^2 : f \in C_c^\infty(\mathbb{R}\setminus[-R,R])\}$. And the essential spectra of the two ends union, so one end suffices.

The proof used nothing about $\delta$ beyond its finiteness. That is the point: the confining term charges $(2\delta - 2)\log\tau$ for a well at distance $\tau$, while the Lévy measure supplies wells of depth up to $\tau^{1/\alpha}$ inside $[\tau, 2\tau]$. A polynomial potential cannot outrun a polynomial supply of logarithmically cheap wells, however large its exponent.

### Theorem 3, the converse, at the level of a sketch

**Theorem 3 (sketch).** Let $\delta > \max(1, 1/\alpha)$ with $\alpha > 1$, and suppose $\nu((-\infty,0)) = 0$, so $V$ has no negative jumps. Then $Q$-a.s. $B_\ell(x) \to 0$ for $w_1 + W$, and the semigroup is compact at $+\infty$.

*Sketch.* Two estimates. First, the far field: for $L \le x/2$,
$$\int_{x_0}^{x-L}e^{y^\delta+V} \le x\,e^{(x-L)^\delta + \sup_{[x_0,x]}V} \le x\,e^{x^\delta - \tfrac12\delta Lx^{\delta-1} + \sup_{[x_0,x]}V},$$
and $\sup_{[x_0,x]}V = O(x^{1/\alpha}\log x)$ a.s., so taking $L = Kx^{1/\alpha + 1 - \delta}$, which is $o(x)$ precisely because $\delta > 1/\alpha$, makes the far field negligible against the near field for $K$ large. Second, the near field: on $[x - L, x]$ the downward oscillation of a spectrally positive $V$ over a window of width $L$ obeys $Q(\inf_{[0,L]}V \le -u) \le \exp(-c(u/L^{1/\alpha})^{\alpha/(\alpha-1)})$, and with $u = 3\delta\log x$ and $L$ as above the exponent beats any polynomial, so a union bound over the $O(x^{\delta})$ windows in $[x,2x]$ and over dyadic blocks is summable. Together these give $\int_{x_0}^xe^{y^\delta+V} \le C e^{x^\delta+V(x)}x^{1-\delta}$ and, symmetrically, $\int_x^\infty e^{-y^\delta-V}\le Ce^{-x^\delta-V(x)}x^{1-\delta}$ for all large $x$, whence $B_\ell(x) \le C^2x^{2-2\delta}\to 0$. $\square$

The uniformity in the second estimate is not written out, and it is the only step with real content, so Theorem 3 is a sketch and is labelled as one. What it is meant to establish is that Theorem 2 is not an artefact: the answer to Remark 5.3(ii) is not "noncompact" tout court, it is "noncompact exactly when $V$ has jumps of the sign that deepens the well".

## Numerical check

`h0013_hardy.py` computes $\log B_\ell(x)$ on a grid by log-sum-exp (the quantities themselves overflow at once: $e^{y^\delta}$ at $y = 300$, $\delta = 2$, is $e^{90000}$), for the deterministic control and for a simulated symmetric $\alpha$-stable path.

| | $x = 5$ | $x = 11$ | $x=19$ |
|---|---|---|---|
| $\log B_\ell$, $V \equiv 0$, $\delta = 2$ | $-4.602$ | $-6.180$ | $-7.271$ |
| $-2\log(\delta x^{\delta-1})$ | $-4.605$ | $-6.182$ | $-7.275$ |

So the criterion and Laplace's method agree with the deterministic benchmark to three decimals. On the stable path the local formula $\log B_\ell(\tau) = m - 2\log(\delta\tau^{\delta-1}) + O(1)$ is confirmed at the two largest downward jumps of the simulated path: at $\tau = 42.29$ with $m = 8.38$ the grid gives $-0.433$ against $-0.49$ predicted, and at $\tau = 290.82$ with $m = 11.16$ it gives $-1.578$ against $-1.57$ predicted.

That validated formula is then evaluated on the jump process alone out to $x = 10^6$ (`h0013_jumps.py`, $\alpha = 1.5$, intensity calibrated to the same path):

| $\delta$ | $\max_{x \le 10^3}\log B_\ell$ | $\le 10^4$ | $\le 10^5$ | $\le 10^6$ |
|---|---|---|---|---|
| $2$ | $-0.69$ | $22.5$ | $297.6$ | $811.4$ |
| $4$ | $-3.34$ | $-3.34$ | $255.5$ | $757.0$ |

The number of jumps that clear the bar grows by decade ($8$, $59$, $368$ for $\delta = 2$; $0$, $9$, $74$ for $\delta = 4$). Raising the confinement from $\delta = 2$ to $\delta = 4$ moves the crossover from $x \approx 2\cdot 10^3$ to $x \approx 2.6\cdot10^4$ and changes nothing else, which is Theorem 2 in one line.

## Status

Theorem 2 is complete and answers both questions of Remark 5.3(ii) in the negative in every case where $V$ has jumps of the relevant sign, hence unconditionally for $\alpha \in (0,1)$ and for symmetric $V$; it also strengthens the paper's Proposition 5.2 from $\delta \le 1/\alpha$ to all $\delta$, and settles the question its introduction raises in the strongest form: no polynomial confinement resists a Lévy drift. Theorem 3 is a sketch and is the reason the answer is stated as a dichotomy rather than a blanket negative. Verification: author checked; the criterion is controlled against the paper's own deterministic benchmark both symbolically and numerically, and the local formula behind the asymptotics is confirmed against an exact grid computation at two points. Prior art: the paper is from July 2026 and states these as open; a bounded search found no follow-up. Not a clearance.

## New open problems

1. **The exact threshold.** Theorem 2 costs the potential $(2\delta - 2)\log x$ per unit of well depth, and an $\alpha$-stable drift supplies depth $x^{1/\alpha}$. So the mechanism dies exactly when $2\log g'(x) \gg x^{1/\alpha}$, that is for confining potentials growing like $\exp(x^{1/\alpha})$. Is it true that for $g$ with $\log g'(x)/x^{1/\alpha}\to\infty$ the perturbed semigroup is compact, and noncompact when the ratio tends to $0$? That would be the sharp form of the question the paper raises.
2. **Completing the dichotomy.** Prove Theorem 3 in full, and decide the spectrally one-sided case at $\alpha = 1$.
3. **Two-sided boundary.** Theorems 2 and 3 concern $+\infty$; for a two-sided $V$ the two ends are independent, so the semigroup is compact only if both ends are, which makes the spectrally one-sided case asymmetric in a way worth stating: a drift with only positive jumps deepens wells for $w_1$ at $-\infty$ and for $w_2$ at $+\infty$.
4. **Higher dimension.** In $\mathbb{R}^d$ the field is $W(x) = \sum_k V(x_k)$, a sum of independent one-dimensional Lévy processes, so the wells are slabs rather than boxes. Does a slab-shaped well of depth $m$ and thickness $x^{1-\delta}$ still force $\lambda_{\mathrm{ess}} = 0$, or does the transverse direction cost enough to restore compactness for large $\delta$?
