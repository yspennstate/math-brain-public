Model actually run: GPT-5.6 Sol. Reasoning level: UNVERIFIED — this is not GPT-6 at maximum, and I do not claim otherwise.

# P03-B coupling report — exact super-regeneration backstep law and a backstep-only negative-debt bound

**Status:** PROVED PARTIAL. The full Lyons–Pemantle–Peres speed-monotonicity conjecture remains unresolved here. This report proves a new exact one-dimensional description of the auxiliary super-regeneration block and uses it to replace the previous all-separated-time debt estimate by a strictly sharper backstep-only estimate. No external-novelty claim is made.

**Native role:** P03-B, `6aabe777361481919c9e614646464772`, probabilistic regeneration/coupling and counterexample-search role under `operations/progress_first_2026-09-20/OWNER_DIRECTIVE.md` and `REGISTRY.md`.

**Captured master immediately before write:** `be2d45e130ba3d677b586965a9d0d3c64021f56e`.

**Previous own checkpoint:** `probability_campaigns/progress_first_2026-09-20/P03/coupling/2026-09-20T0217Z__occupation-debt-and-interface-obstruction.md`.

**Latest complementary P03-A checkpoint consumed only to avoid duplication:** `probability_campaigns/progress_first_2026-09-20/P03/analytic/2026-09-20T0259Z__unbounded-support-mean-defect-extension.md`. P03-A now has an escape-tilt stochastic-domination lemma and an unbounded-support finite-mean near-regular monotonicity criterion. I do not reproduce its Aïdékon-formula analysis below.

## 1. Minimal source continuity and convention

The primary coupling source remains Gérard Ben Arous, Alexander Fribergh and Vladas Sidoravicius, *A proof of the Lyons-Pemantle-Peres monotonicity conjecture for high biases*, arXiv:1111.5865. It assumes a Galton–Watson offspring variable `Z` with

\[
\mathbf P(Z=0)=0,
\]

and uses **outward child bias** `beta`: at a non-root vertex with `k` children,

\[
q_k(\beta):=P_\beta(\text{parent})=\frac1{1+\beta k},
\qquad
P_\beta(\text{a specified child})=\frac\beta{1+\beta k}.
\tag{1.1}
\]

Thus larger `beta` means stronger bias away from the root. The walk is transient for `beta>1/EZ`; the conjecture asks that `v(beta)` increase throughout that interval. The old arXiv posting proves a high-bias range and explicitly builds the common one-dimensional super-regeneration coupling. Its printed `tau<=3B+1` sublemma was corrected in the preceding P03-B run to the sharp deterministic `tau<=4B+1`; nothing below uses the false printed `3B+1` inequality.

The requested differentiability source Adam Bowditch and Yuki Tokushige, arXiv:1906.07913, proves differentiability in the ballistic/CLT regime and represents the derivative by a Gaussian covariance; arXiv:2006.03433 proves analyticity in the ballistic regime. These results do not give the missing sign.

The strongest source-uniform later range retained in the campaign is Song–Wang–Xiang, *Journal of Applied Probability* 62 (2025), DOI `10.1017/jpr.2024.113`: in their reciprocal parent-bias convention `lambda=1/beta`, if the minimum offspring is `d>=2`, the speed is strictly decreasing for

\[
0\le\lambda\le \frac{d}{1+\sqrt{1-1/d}}.
\tag{1.2}
\]

This is consistent with increasing speed in outward `beta`. For minimum degree one, the older Aïdékon monotonicity range `lambda<=1/2`, i.e. `beta>=2`, is already known; no restricted calculation below is presented as improving that published range.

A bounded source check dated 20 September 2026 did not surface a full-source resolution. A search miss is not a proof of worldwide openness.

The fixed full-source metric remains

`R_full: 1 -> 1`.

## 2. Inherited obstruction and the point of this run

The preceding P03-B report proved the exact finite-horizon response identity

\[
\frac d{d\beta}E_\beta|X_n|
=
E_\beta\sum_t
\frac{K_t}{(1+\beta K_t)^2}
\bigl(2+F_{t,n}^{+}-F_{t,n}^{-}\bigr),
\tag{2.1}
\]

rewrote the response bracket as a difference of future degree-occupation measures, and gave a positive-probability `{2,6}`, `beta=3/5` finite cylinder on which a local response bracket is genuinely negative. Therefore pointwise nonnegativity of every derivative contribution is false.

The older regeneration debt bound then charged **every separated clock time** as potentially adverse. That throws away a much stronger structural fact already visible in the source coupling: if the auxiliary one-dimensional walk takes an up-step, then every tree walk whose offspring is at least the auxiliary minimum degree must also move outward, so the radial gap cannot decrease. Negative debt can occur only at auxiliary backsteps.

This run does two things:

1. computes the relevant one-dimensional backstep statistics exactly, without the invalid `3B+1` bound;
2. uses those exact statistics to charge negative coupling debt only at backsteps that occur after a possible separation.

## 3. Setup for the auxiliary walk

Assume for the coupling theorem that

\[
d\le Z\le D\quad\text{a.s.},
\qquad 1\le d\le D<\infty,
\qquad \beta d>1.
\tag{3.1}
\]

Set

\[
q:=q_d(\beta)=\frac1{1+\beta d},
\qquad
p:=1-q=\frac{\beta d}{1+\beta d},
\tag{3.2}
\]

and

\[
r:=\frac qp=\frac1{\beta d},
\qquad
c:=p-q=\frac{\beta d-1}{\beta d+1}.
\tag{3.3}
\]

Let `Y` be the nearest-neighbor walk with up probability `p` and down probability `q`, built from the same uniforms as the two tree walks, and condition on time zero being a one-dimensional super-regeneration time as in the source. Let `tau` be the first positive super-regeneration time and

\[
B:=\#\{1\le n\le\tau:\Delta Y_n=-1\}.
\tag{3.4}
\]

The law of `(B,tau)` depends only on the scalar `beta d`.

## 4. New exact representation: downcrossing counts form a reversible negative-binomial chain

For a drift-right nearest-neighbor path, after its first visit to level one define

\[
D_j:=\#\{n:Y_n=j+1,\ Y_{n+1}=j\},
\qquad j\ge0,
\tag{4.1}
\]

the total number of future downcrossings of the edge `(j,j+1)`.

Under the future part of the `0-SR` conditioning, `D_0=0`: after the initial step from zero to one the path never returns to zero.

### Lemma 4.1 — exact level-chain kernel

The sequence `(D_j)_{j>=0}`, conditional on `D_0=0`, is a Markov chain started at zero with transition kernel

\[
\boxed{
Q(k,\ell)
=\binom{k+\ell}{\ell}p^{k+1}q^\ell,
\qquad k,\ell\ge0.
}
\tag{4.2}
\]

It is reversible for the geometric probability law

\[
\boxed{
\pi_k=(1-r)r^k,
\qquad r=q/p.
}
\tag{4.3}
\]

#### Proof

Fix a level `j`. Each time the path crosses from `j` to `j+1`, it either never returns across that edge, with probability `1-r`, or eventually makes a downcrossing `j+1 -> j`, with probability `r=q/p`. Repeating after each return shows that `D_j` has the geometric law (4.3).

Now condition on `D_j=k`. There are exactly `k+1` upward crossings `j -> j+1`: one for each of the `k` returns plus the final escaping crossing. Before each such upward crossing, every visit to level `j` independently chooses `j+1` with probability `p` and `j-1` with probability `q`; a downward excursion to `j-1` returns to `j` almost surely because the one-dimensional walk drifts to `+infinity`. Thus the number of downward departures `j -> j-1` accumulated before the `k+1` upward crossings is a sum of `k+1` iid geometric-failure counts and hence

\[
P(D_{j-1}=\ell\mid D_j=k)
=\binom{k+\ell}{\ell}p^{k+1}q^\ell.
\tag{4.4}
\]

This is the backward-in-level transition kernel. But

\[
\pi_kQ(k,\ell)
=(1-r)r^k\binom{k+\ell}{\ell}p^{k+1}q^\ell
=(p-q)\binom{k+\ell}{k}q^{k+\ell},
\tag{4.5}
\]

which is symmetric in `k,ell`. Hence `Q` is reversible under `pi`, so the same kernel governs the chain forward in the level index. Conditioning `D_0=0` therefore starts that forward chain at zero. QED.

### Lemma 4.2 — regeneration is the first `0 -> 0` transition

Let

\[
H:=Y_\tau
\tag{4.6}
\]

be the first positive regeneration level. Then

\[
\boxed{
H=\min\{j\ge1:D_{j-1}=0=D_j\}.
}
\tag{4.7}
\]

Moreover

\[
\boxed{
B=\sum_{j=0}^{H-1}D_j,
\qquad
\tau=H+2B.
}
\tag{4.8}
\]

#### Proof

At the first hit of level `j`, regeneration requires two and only two things. The path must never step from `j` to `j-1`, which is `D_{j-1}=0`, and after it leaves `j` upward it must never return from `j+1`, which is `D_j=0`. Conversely those two zero-downcrossing conditions force the first visit to `j` to be a strict record whose future remains strictly above `j`.

Every downstep before the regeneration at level `H` crosses exactly one edge below `H`, and all downcrossings of such an edge occur before `tau`; after `tau` the path stays above `H`. Thus the first identity in (4.8) follows. If `U` and `B` are the numbers of up- and downsteps before `tau`, then `U-B=H` and `U+B=tau`, giving `tau=H+2B`. QED.

This representation explains the earlier sharp deterministic inequality `tau<=4B+1`: it is a statement about the area and first `0 -> 0` transition of this level chain. More importantly, the representation permits exact moments rather than a coarse deterministic length bound.

## 5. New theorem: exact first-block moments

Define the Lambert series

\[
\mathcal L(r)
:=\sum_{m=1}^{\infty}\frac{r^m}{1-r^m},
\qquad 0<r<1.
\tag{5.1}
\]

### Theorem 5.1 — exact super-regeneration backstep moments

Under the `0-SR` law,

\[
\boxed{
\widetilde P(B\ge1)=q,
}
\tag{5.2}
\]

\[
\boxed{
\widetilde E B=\frac{q}{c^2},
\qquad
\widetilde E\tau=\frac1{c^2},
}
\tag{5.3}
\]

and

\[
\boxed{
\widetilde E[B(B-1)]
=
\frac{2q^2}{c^4}
\left(1+3p+c\mathcal L(r)\right).
}
\tag{5.4}
\]

These formulas are exact for every `p>q`, not asymptotic high-bias estimates.

#### Proof, part I: one return cycle to zero

Let

\[
\sigma:=\inf\{n\ge1:D_n=0\}
\tag{5.5}
\]

be the first return time of the `D`-chain to zero and let

\[
C:=\sum_{j=0}^{\sigma-1}D_j
\tag{5.6}
\]

be its area. The stationary mass at zero is

\[
\pi_0=1-r=\frac cp.
\]

Kac's return-time formula gives

\[
E_0\sigma=\frac1{\pi_0}=\frac pc.
\tag{5.7}
\]

The stationary mean is

\[
E_\pi D=\frac{r}{1-r}=\frac qc.
\tag{5.8}
\]

The standard renewal-reward identity for cycles based at zero therefore yields

\[
\boxed{
E_0 C
=E_0\sigma\,E_\pi D
=\frac{pq}{c^2}.
}
\tag{5.9}
\]

For the second factorial moment, introduce for `0<=s<1`

\[
A_n:=\sum_{j=0}^{n-1}D_j,
\qquad
u_n(s):=E_0[s^{A_n};D_n=0],
\qquad
U(s):=\sum_{n\ge0}\nu_n(s).
\tag{5.10}
\]

The transition kernel has exponential generating action

\[
\sum_{\ell\ge0}Q(k,\ell)z^\ell
=\left(\frac p{1-qz}\right)^{k+1}.
\tag{5.11}
\]

Weighting state `k` by `s^k` therefore maps an exponential `z^ell` to

\[
\frac p{1-qz}
\left(\frac{sp}{1-qz}\right)^k.
\tag{5.12}
\]

Starting from the terminal indicator of state zero corresponds to `z_0=0`. Iterating

\[
z_{m+1}=\frac{sp}{1-qz_m}
\tag{5.13}
\]

shows that

\[
\nu_n(s)=\frac{p^n}{A_n(s)},
\tag{5.14}
\]

where, to avoid conflict with the area notation, the denominator sequence satisfies

\[
A_0(s)=A_1(s)=1,
\qquad
A_{n+1}(s)=A_n(s)-spqA_{n-1}(s).
\tag{5.15}
\]

(Equivalently one may rename these denominators `R_n`; only the recurrence matters.) If

\[
\Delta(s):=\sqrt{1-4spq},
\qquad
\lambda_\pm(s):=\frac{1\pm\Delta(s)}2,
\tag{5.16}
\]

then

\[
A_n(s)=
\frac{\lambda_+(s)^{n+1}-\lambda_-(s)^{n+1}}
{\lambda_+(s)-\lambda_-(s)}.
\tag{5.17}
\]

Hence, writing

\[
a(s):=\frac p{\lambda_+(s)},
\qquad
\rho(s):=\frac{\lambda_-(s)}{\lambda_+(s)},
\qquad
C_0(s):=\frac{\Delta(s)}{\lambda_+(s)},
\tag{5.18}
\]

we get

\[
U(s)
=C_0(s)
\sum_{n\ge0}
\frac{a(s)^n}{1-\rho(s)^{n+1}}.
\tag{5.19}
\]

Split the sum as

\[
\sum_{n\ge0}\frac{a^n}{1-\rho^{n+1}}
=
\frac1{1-a}
+
\sum_{n\ge0}
\frac{a^n\rho^{n+1}}{1-\rho^{n+1}}.
\tag{5.20}
\]

As `s` increases to one, the second series converges to `mathcal L(r)`. Put `delta=1-s`. Direct expansion at `s=1`, using `lambda_+(1)=p`, gives

\[
1-a(1-\delta)
=\frac qc\,\delta
-
\frac{q^2(p+c)}{c^3}\,\delta^2
+O(\delta^3),
\tag{5.21}
\]

and

\[
C_0(1-\delta)
=\frac cp+\frac q{pc}\,\delta+O(\delta^2).
\tag{5.22}
\]

Substitution into (5.19)--(5.20) yields the singular expansion

\[
\boxed{
U(1-\delta)
=
\frac{c^2}{pq}\,\frac1\delta
+
\left(3+\frac cp\mathcal L(r)\right)
+O(\delta).
}
\tag{5.23}
\]

Every return path to zero is a unique concatenation of first-return cycles, and the area is additive across cycles. If

\[
\phi(s):=E_0[s^C],
\]

then therefore

\[
U(s)=1+\phi(s)+\phi(s)^2+\cdots=\frac1{1-\phi(s)},
\qquad
\phi(s)=1-\frac1{U(s)}.
\tag{5.24}
\]

Comparing the expansion

\[
\phi(1-\delta)
=1-(E C)\delta
+\frac12E[C(C-1)]\delta^2+O(\delta^3)
\tag{5.25}
\]

with (5.23)--(5.24) gives again (5.9) and also

\[
\boxed{
E[C(C-1)]
=2\left(\frac{pq}{c^2}\right)^2
\left(3+\frac cp\mathcal L(r)\right).
}
\tag{5.26}
\]

#### Proof, part II: from return cycles to the first regeneration

At state zero,

\[
Q(0,0)=p,
\tag{5.27}
\]

so the first positive regeneration occurs exactly when a return cycle is the one-step self-loop `0 -> 0`. Before that happens there are

\[
N\sim\mathrm{Geom}(p)
\tag{5.28}

positive excursions, where `N` counts failures before the first success:

\[
P(N=n)=pq^n,
\qquad
EN=\frac qp,
\qquad
E[N(N-1)]=\frac{2q^2}{p^2}.
\tag{5.29}
\]

Let `C^+` denote the return-cycle area conditional on being positive. Since `C=0` on the immediate self-loop and a positive cycle occurs with probability `q`,

\[
E C^+=\frac{E C}{q},
\qquad
E[C^+(C^+-1)]=\frac{E[C(C-1)]}{q}.
\tag{5.30}
\]

The block backstep count is

\[
B=C_1^++\cdots+C_N^+.
\tag{5.31}
\]

This immediately gives `P(B>=1)=P(N>=1)=q` and

\[
E B
=\frac qp\frac{E C}{q}
=\frac q{c^2}.
\tag{5.32}
\]

The compound-sum factorial-moment formula gives

\[
E[B(B-1)]
=EN\,E[C^+(C^+-1)]
+E[N(N-1)](E C^+)^2.
\tag{5.33}
\]

Substituting (5.9), (5.26), and (5.29)--(5.30) simplifies exactly to (5.4).

For the level increment, a positive return excursion has mean length

\[
E[\sigma\mid C>0]
=\frac{E\sigma-p}{q}
=\frac{2p}{c}.
\tag{5.34}
\]

Therefore

\[
E H
=1+EN\,E[\sigma\mid C>0]
=1+\frac qp\frac{2p}{c}
=\frac1c.
\tag{5.35}
\]

Finally `tau=H+2B` from Lemma 4.2, so

\[
E\tau
=\frac1c+2\frac q{c^2}
=\frac1{c^2}.
\tag{5.36}
\]

This proves Theorem 5.1. QED.

## 6. New theorem: negative coupling debt occurs only at auxiliary backsteps

Compare the `beta` walk `X^-` and the `beta+eps` walk `X^+`, `eps>0`, with a common uniform radial coupling. Define

\[
\delta_k
:=q_k(\beta)-q_k(\beta+\varepsilon)>0,
\tag{6.1}
\]

\[
\delta_{\min}:=\min_{d\le k\le D}\delta_k,
\qquad
\delta_{\max}:=\max_{d\le k\le D}\delta_k,
\tag{6.2}
\]

and

\[
R_\varepsilon
:=\max_{d\le i,j\le D}
[q_i(\beta+\varepsilon)-q_j(\beta)]_+
=[q_d(\beta+\varepsilon)-q_D(\beta)]_+.
\tag{6.3}
\]

Let

\[
G_n:=|X_n^+|-|X_n^-|.
\tag{6.4}
\]

### Theorem 6.1 — exact-backstep debt inequality

With the common super-regeneration block above,

\[
\boxed{
\widetilde E G_\tau
\ge
2\delta_{\min}
-
2R_\varepsilon\delta_{\max}
\frac{1+3p+c\mathcal L(r)}{c^4}.
}
\tag{6.5}
\]

Equivalently, a sufficient condition for strict speed increase is

\[
\boxed{
\delta_{\min}
>
R_\varepsilon\delta_{\max}
\frac{1+3p+c\mathcal L(r)}{c^4}.
}
\tag{6.6}
\]

This replaces the previous P03-B bound involving `E[B(4B+1)]`. It does not use `tau<=4B+1` at all.

#### Proof

Condition on the complete binary sign path of `Y` through `tau`. Write its `B` backstep indices in chronological order as

\[
t_1<t_2<\cdots<t_B.
\]

Because the event defining the one-dimensional sign path depends only on whether each uniform lies in `[0,q]` or `(q,1]`, conditional on the sign path each `U_{t_j}` is uniform on `[0,q]` and these residual uniforms are independent of the sign indicators.

If a clock time is **not** one of the `t_j`, then `U>q=q_d(beta)`. Since every actual offspring is at least `d`,

\[
q_k(\beta)\le q,
\qquad
q_k(\beta+\varepsilon)\le q.
\]

Therefore both tree walks are forced to move outward at every non-backstep time. Their radial gap does not change there, even after spatial separation.

At the first auxiliary backstep `t_1`, if it exists, the two walks are still together: non-backstep times cannot separate them under the common child coupling. If their common degree is `k`, the less-biased walk moves inward while the more-biased walk moves outward on an interval of conditional length

\[
\frac{\delta_k}{q}.
\]

Hence

\[
E[\Delta G_{t_1}\mid Y,\mathcal F_{t_1-1}]
=\frac{2\delta_k}{q}
\ge\frac{2\delta_{\min}}q.
\tag{6.7}
\]

At a later auxiliary backstep `t_j`, if the walks are currently at degrees `i` for `X^+` and `ell` for `X^-`, then conditional on `U_{t_j}<=q`, the exact expected radial-gap increment is

\[
\frac{2}{q}
\left(q_\ell(\beta)-q_i(\beta+\varepsilon)\right).
\tag{6.8}
\]

Thus, if the walks are already spatially separated, its negative part is at most

\[
\frac{2R_\varepsilon}{q}.
\tag{6.9}
\]

If they are still together, (6.8) is nonnegative.

Before the `j`-th auxiliary backstep, separation can only have happened at one of the preceding `j-1` auxiliary backsteps. At any such earlier backstep, conditional on still being together, the separation probability is at most `delta_max/q`. Consequently the union bound gives

\[
\widetilde P(\text{already separated before }t_j\mid Y)
\le
(j-1)\frac{\delta_{\max}}q.
\tag{6.10}
\]

Combining (6.9) and (6.10), and discarding every later positive contribution, yields conditional on `Y`

\[
E[G_\tau\mid Y]
\ge
\frac{2\delta_{\min}}q\mathbf 1_{\{B\ge1\}}
-
\frac{2R_\varepsilon\delta_{\max}}{q^2}
\sum_{j=2}^{B}(j-1).
\tag{6.11}
\]

Since

\[
2\sum_{j=2}^{B}(j-1)=B(B-1),
\]

we have

\[
E[G_\tau\mid Y]
\ge
\frac{2\delta_{\min}}q\mathbf 1_{\{B\ge1\}}
-
\frac{R_\varepsilon\delta_{\max}}{q^2}B(B-1).
\tag{6.12}
\]

Average (6.12), use `P(B>=1)=q` and the exact factorial moment (5.4), and obtain (6.5). QED.

### Corollary 6.2 — explicit speed and derivative lower bounds

The common regeneration law gives

\[
v(\beta+\varepsilon)-v(\beta)
=\frac{\widetilde E G_\tau}{\widetilde E\tau}.
\tag{6.13}
\]

Using `E tau=1/c^2`, Theorem 6.1 gives

\[
\boxed{
 v(\beta+\varepsilon)-v(\beta)
\ge
2c^2
\left[
\delta_{\min}
-
R_\varepsilon\delta_{\max}
\frac{1+3p+c\mathcal L(r)}{c^4}
\right].
}
\tag{6.14}
\]

When `D>d` and `beta d>1`, the function

\[
a_k(\beta):=\frac{k}{(1+\beta k)^2}
\tag{6.15}
\]

is decreasing over `k in [d,D]`. Therefore

\[
\frac{\delta_{\min}}\varepsilon\to a_D(\beta),
\qquad
\frac{\delta_{\max}}\varepsilon\to a_d(\beta),
\tag{6.16}
\]

and

\[
R_\varepsilon\to
R_0
:=q_d(\beta)-q_D(\beta)
=\frac{\beta(D-d)}{(1+\beta d)(1+\beta D)}.
\tag{6.17}
\]

Hence the lower right Dini derivative satisfies

\[
\boxed{
\liminf_{\varepsilon\downarrow0}
\frac{v(\beta+\varepsilon)-v(\beta)}\varepsilon
\ge
2c^2
\left[
a_D(\beta)
-
R_0a_d(\beta)
\frac{1+3p+c\mathcal L(r)}{c^4}
\right].
}
\tag{6.18}
\]

Where Bowditch–Tokushige differentiability applies, the left side is simply `v'(beta)`.

This is the requested new lemma controlling negative derivative contributions: the entire adverse term is reduced to an **exact one-dimensional Lambert-series factor multiplied by the worst reverse degree mismatch**. No solver, simulation, or unproved regeneration-tail estimate enters (6.18).

## 7. Calibration and a rigorous limitation of the worst-pair mechanism

The exact formula also tells us when this still-crude worst-pair charging cannot be the end of the proof.

For the bounded family `Z in {1,2}`, write `x=beta>1`. Condition (6.18) reduces to

\[
\frac{2(1+x)^3}{x(1+2x)}
>
K(x),
\tag{7.1}
\]

where

\[
K(x)
:=
\frac{
1+\frac{3x}{1+x}
+\frac{x-1}{x+1}\mathcal L(1/x)
}
{\left(\frac{x-1}{x+1}\right)^4}.
\tag{7.2}
\]

At the already-known Aïdékon endpoint `beta=2`,

\[
\mathcal L(1/2)>1,
\]

so

\[
K(2)>270,
\qquad
\frac{2(1+2)^3}{2(1+4)}=\frac{27}{5}.
\tag{7.3}
\]

Thus the worst-pair debt bound misses that published range by a large margin. This is a rigorous obstruction to trying to finish the problem merely by making the one-dimensional `B` tail estimate sharper: the `B` law is now exact, and the remaining loss is the use of a worst possible degree mismatch at every separated backstep.

As a sanity check only, not a new monotonicity theorem, the scalar criterion does hold for all `beta>=8` in the `{1,2}` family. Indeed

\[
\mathcal L(1/x)
\le \frac{x}{(x-1)^2},
\qquad x>1,
\tag{7.4}
\]

because `1-x^{-m}>=1-x^{-1}` termwise. Replacing `mathcal L` by this upper bound, the difference between the left side of (7.1) and the resulting upper bound on `K(x)` is

\[
\frac{(x+1)^3}{x(x-1)^5(2x+1)}
P(x),
\tag{7.5}
\]

with

\[
P(x)=2x^5-18x^4+20x^3-16x^2+11x-2.
\tag{7.6}
\]

Writing `x=8+y`,

\[
P(8+y)
=2y^5+62y^4+724y^3+3792y^2+7691y+1110>0
\tag{7.7}
\]

for every `y>=0`. This only validates the new inequality; it does not beat the already-known universal `beta>=2` range and is not counted as progress in the full-source metric.

## 8. What changed mathematically

The obligation ledger is now:

* `C1` exact source convention and no-leaf assumptions: **PRESERVED**.
* `C2` universal pathwise radial domination: **RIGOROUSLY IMPOSSIBLE** for small bias increments when `d<D` (earlier P03-B result).
* `C3` source arXiv-v1 deterministic `tau<=3B+1`: **REFUTED AS PRINTED**; sharp replacement `tau<=4B+1` preserved from the preceding run.
* `C4` finite-horizon response bracket as degree-occupation debt: **PROVED** in the preceding run.
* `C5` pointwise nonnegative response brackets: **RIGOROUSLY FALSE** by the preceding `{2,6}` finite cylinder.
* `C6` exact auxiliary downcrossing chain `Q`, first-`0->0` regeneration representation, and exact moments (5.2)--(5.4): **NEW PROVED PARTIAL**.
* `C7` all-separated-time coupling charge `E[B(4B+1)]`: **SUPERSEDED** by the strictly sharper backstep-only Theorem 6.1.
* `C8` exact one-dimensional lower-Dini derivative bound (6.18): **NEW PROVED PARTIAL**.
* `C9` annealed control of the **degree-selection** factor at separated backsteps, replacing worst-case `R_0`: **OPEN**.
* `C10` full-source derivative sign throughout `beta>1/EZ`: **OPEN**.

The headline source metric remains unchanged because (6.18) is a sufficient lower bound, not a proof that its bracket is positive throughout the source range.

## 9. Remaining obstruction and next attack

The exact one-dimensional part is no longer the main unknown. The factor

\[
\frac{1+3p+c\mathcal L(r)}{c^4}
\]

is now explicit and comes from the actual super-regeneration backstep law. The real loss in (6.18) is

\[
R_0
=\max_{i,j}
[q_i(\beta)-q_j(\beta)]_+,
\]

which pretends that every separated auxiliary backstep sees the maximally adverse degree pair.

The next P03-B attack should therefore return to the fresh/history split identified in the previous report, but with the exact `D`-chain now available as the clock. At the `j`-th auxiliary backstep define the actual reverse mismatch

\[
\mathcal R_j
:=
[q_{K_j^+}(\beta)-q_{K_j^-}(\beta)]_+
\tag{9.1}
\]

(at infinitesimal bias, with the obvious orientation). The target is a bound of the form

\[
E\left[
\sum_{j\ge2}
\mathbf 1_{\{t_j<\tau,\,\text{already separated}\}}
\mathcal R_j
\right]
\le
\text{explicit selection factor}
\times E[B(B-1)],
\tag{9.2}
\]

where the selection factor is **strictly smaller than the worst-pair `R_0`** and vanishes when both current vertices carry fresh iid offspring. The previous report already proves fresh-fresh annealed gap drift is positive, so only revisits / ancestral selection need be charged.

A promising concrete route is to mark each state of the reversible downcrossing chain by whether the two tree vertices are fresh or historically selected, then use the exact negative-binomial excursion kernel (4.2) to control how many adverse marked backsteps occur per positive `D`-excursion. This is probabilistic and complementary to P03-A's recursive escape identities.

No new admission loop, audit wait, simulation claim, schedule change, peer overwrite, email, Drive action, or public posting occurred in this run.
