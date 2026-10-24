TASK: B16 ACCOUNT: account02 RUN: 2026-09-21T16:25:24.332857+00:00 — FEI signed transport: exact active entropy-baseline Laplacian and a sharp linear-in-dimension cancellation necessity.

MODEL: GPT-5.6 Sol
THINKING LEVEL: UNKNOWN; source=not exposed; requested=maximum actually supported
THINKING USAGE: NOT_EXPOSED; provider thinking time=NOT_EXPOSED; coverage=unavailable
EXECUTION: WITHOUT_VERIFIED_BRAIN
FULL FEI STATUS: OPEN / NOT PROVED

# 0. Movement and route choice

The entering account02 chain had already established:

1. a weight-four q-flip basis of `C_0=RM(1,n)^\perp` and exact signed Aumann--Shapley disintegration of the R32 residual;
2. the account04 Shapley--plaquette identity
   \[
   \frac8N L_v=E(g_v)-\mathcal C_v-\Theta_v,
   \]
   with the raw one-q-flip dual entropy `E(g_v)` canceled only by signed plaquette curvature and the exact terminal share;
3. a spectral law for the **number** of actually frustrated q-flips, showing that random basis selection leaves `Theta(NJ/n)` active channels; and
4. for monomial defects, an exact Shapley-refunded multiplier collapse.

A remaining possible escape was that, although the number of active channels is large, the active filter might preferentially retain dual generators of such low entropy that the positive generator term
\[
\sum_{v:\,z_v=-1}E(g_v)
\]
is already `O(J)`. This run refutes that escape sharply and universally for the random ordered-min q-flip basis.

The three deliberately different FLEET_RULES moves are:

* **#1 CHANGE THE CATEGORY:** recast the random-basis active generator term as a radial jump-Laplacian acting on the original-coordinate derivative signs.
* **#7 TAKE THE LIMIT:** compute the two endpoint eigenvalues and their exact large-`n` asymptotics.
* **#20 FIND WHY THE ALGORITHM FAILS:** test the proposed “active filtering removes the dimension factor” algorithm and identify its exact obstruction.

This scope is complementary to account04/B16's Hardy/R16 signed collision domination and account03/B16's Ward stopping route. I do not spend either of those banks here.

# 1. Setup

Let
\[
G=\mathbb F_2^n,\qquad N=2^n,\qquad f:G\to\{\pm1\}.
\]

Choose a uniform coordinate order `pi` and a uniform anchor `a`. For every displacement `v` of Hamming weight at least two, let `i(v)` be the first coordinate of `supp(v)` in `pi`, and set
\[
B_v(a)=\{a,a+e_{i(v)},a+v,a+v+e_{i(v)}\}.
\]
The inherited q-flip theorem says these `N-n-1` relations form a basis of `C_0`.

For a pivot of rank `r` in the order, the inherited dual-generator theorem identifies the quotient dual `g_v` as a one-subcube defect of codimension
\[
c=n-r+1.
\]
Write `H_c` for its Fourier entropy in **bits**. Its squared Fourier law has one atom
\[
p_0=(1-2^{1-c})^2
\]
and `2^c-1` equal atoms
\[
p_1=2^{2-2c}.
\]
Thus
\[
H_c=-p_0\log_2 p_0-(2^c-1)p_1\log_2 p_1.
\tag{1.1}
\]

Define the random active positive baseline
\[
\mathscr B_n(f)
:=
\mathbb E_{\pi,a}
\sum_{\substack{v:\ |v|\ge2\\ f_{B_v(a)}=-1}}
H_{c_\pi(i(v))}.
\tag{1.2}
\]
This is **only** the positive `E(g_v)` term in the Shapley--plaquette bridge. No curvature or terminal refund is included.

For a physical coordinate `i`, define the derivative sign
\[
\tau_i(x)=f(x)f(x+e_i).
\tag{1.3}
\]
It is invariant under `x -> x+e_i`; hence its Walsh spectrum lives on labels not containing `i`. Let
\[
C_i(w)=\mathbb E_x\,\tau_i(x)\tau_i(x+w),\qquad w_i=0.
\tag{1.4}
\]

# 2. Exact rank-weighted active-channel formula

Fix `i` and nonzero `w` with `w_i=0`, and put `k=|w|`. The corresponding q-flip displacement is
\[
v=w+e_i.
\]
It has pivot `i` precisely when `i` occurs before all `k` coordinates of `w`.

If the rank of `i` is `r`, the probability that all `k` coordinates of `w` lie after it is
\[
\frac{\binom{n-r}{k}}{\binom{n-1}{k}},
\]
while `Pr(rank(i)=r)=1/n`. Therefore the expected dual entropy attached to this `(i,w)` channel is
\[
\boxed{
W_n(k)
=
\frac{1}{n\binom{n-1}{k}}
\sum_{c=k+1}^{n}
\binom{c-1}{k}H_c.
}
\tag{2.1}
\]

Conditional on using this pivot, the q-flip sign is
\[
f_{B_v(a)}=\tau_i(a)\tau_i(a+w),
\]
so anchor averaging gives active probability
\[
\frac{1-C_i(w)}2.
\tag{2.2}
\]

Hence:

## Theorem 2.1 — exact active entropy baseline in physical derivative coordinates

\[
\boxed{
\mathscr B_n(f)
=
\frac12\sum_{i=1}^n
\sum_{\substack{w\subseteq[n]\setminus\{i\}\\w\ne0}}
W_n(|w|)\,[1-C_i(w)].
}
\tag{2.3}
\]

No R32 coefficient has been absolute-valued. This theorem concerns the raw positive generator term before the inherited signed refunds act.

# 3. Diagonalization: a closed radial Laplacian multiplier

Write the normalized Walsh expansion
\[
C_i(w)
=
\sum_{S:\,i\notin S}\widehat{\tau_i}(S)^2(-1)^{S\cdot w}.
\tag{3.1}
\]
The constant mode cancels from `1-C_i(w)`. For `1<=ell<=n-1`, define
\[
G_n(\ell)
:=
\sum_{w\subseteq[n-1]}
W_n(|w|)\,[1-(-1)^{S\cdot w}],
\qquad |S|=\ell.
\tag{3.2}
\]
Then
\[
\boxed{
\mathscr B_n(f)
=
\frac12\sum_{i=1}^n
\sum_{\substack{S\ne\varnothing\\i\notin S}}
\widehat{\tau_i}(S)^2G_n(|S|).
}
\tag{3.3}
\]

The useful point is that `G_n` has an exact closed form.

## Theorem 3.1 — active entropy-baseline Laplacian

For every `1<=ell<=n-1`,
\[
\boxed{
G_n(\ell)
=
\frac1n\sum_{c=2}^n
2^{c-1}H_c
\left[
1-
\frac{\binom{n-1-\ell}{c-1}}{\binom{n-1}{c-1}}
\right],
}
\tag{3.4}
\]
where a binomial coefficient with lower index larger than the upper index is zero.

### Proof

Insert (2.1) into (3.2), group by `k=|w|`, and swap the `k,c` sums. For fixed `c`, after division by `2^{c-1}` the resulting coefficient can be represented by the following experiment on the `m=n-1` coordinates other than the pivot:

1. choose a uniform `(c-1)`-set `R`;
2. choose `W subseteq R` by independent fair coins.

Indeed, conditional on `|W|=k`, the set `W` is uniform among all `k`-sets and its weight is exactly
\[
2^{-(c-1)}\frac{\binom{c-1}{k}}{\binom{m}{k}}.
\]
For a fixed spectral label `S` of size `ell`,
\[
\mathbb E[(-1)^{|S\cap W|}\mid R]
=
\begin{cases}
1,&R\cap S=\varnothing,\\
0,&R\cap S\ne\varnothing.
\end{cases}
\]
Therefore
\[
2^{-(c-1)}
\sum_{k=0}^{c-1}
\frac{\binom{c-1}{k}}{\binom{m}{k}}
\sum_{|w|=k}[1-(-1)^{S\cdot w}]
=
1-\frac{\binom{m-\ell}{c-1}}{\binom{m}{c-1}}.
\]
Multiplying by `2^{c-1}H_c/n` and summing `c` gives (3.4). QED.

The bracket in (3.4) is the probability that a uniform `(c-1)`-subset meets a fixed `ell`-subset. It is strictly increasing in `ell`. Since `H_2>0`,
\[
\boxed{
G_n(1)<G_n(2)<\cdots<G_n(n-1).
}
\tag{3.5}
\]

Thus the active entropy baseline is exactly the Dirichlet form of a radial positive jump operator on each **physical** derivative field, with no change of cube coordinates.

# 4. Exact endpoints and asymptotics

Equation (3.4) gives
\[
\boxed{
G_n(1)
=
\frac{1}{n(n-1)}
\sum_{c=2}^{n}
(c-1)2^{c-1}H_c,
}
\tag{4.1}
\]
and
\[
\boxed{
G_n(n-1)
=
\frac1n
\sum_{c=2}^{n}
2^{c-1}H_c.
}
\tag{4.2}
\]

For `eps=2^{1-c}`, put
\[
\delta=1-(1-\varepsilon)^2=2\varepsilon-\varepsilon^2.
\]
Since the `2^c-1` small Fourier atoms all equal `eps^2`, (1.1) is exactly
\[
H_c
=
2(c-1)\delta-(1-\delta)\log_2(1-\delta).
\tag{4.3}
\]
Consequently
\[
2^{c-1}H_c
=
4(c-1)+\frac{2}{\ln2}+O(c2^{-c}).
\tag{4.4}
\]
Summing (4.4) in (4.1)--(4.2) yields
\[
\boxed{
G_n(1)
=
\frac43n-\frac23+\frac1{\ln2}+O(n^{-2}),
}
\tag{4.5}
\]
and
\[
\boxed{
G_n(n-1)
=
2n-2+\frac2{\ln2}+O(n^{-1}).
}
\tag{4.6}
\]

So active filtering does not remove the ambient-dimension factor. It merely places the positive baseline in a sharply identified radial spectrum whose eigenvalues range from about `(4/3)n` to `2n`.

# 5. Sharp folded-influence lower bound

Let
\[
j_i=\min\{\operatorname{Inf}_i(f),1-\operatorname{Inf}_i(f)\},
\qquad
J(f)=\sum_i j_i.
\]
Multiplication by a cube character leaves every q-flip sign unchanged because q-flips lie in `C_0`; therefore `mathscr B_n` is character-gauge invariant. Work in the minimizing gauge, so `Inf_i=j_i<=1/2`.

Parseval for the derivative sign gives
\[
\sum_{\varnothing\ne S}\widehat{\tau_i}(S)^2
=
1-(1-2j_i)^2
=
4j_i(1-j_i).
\tag{5.1}
\]
Using (3.3), monotonicity (3.5), and `j_i(1-j_i)>=j_i/2`,
\[
\begin{aligned}
\mathscr B_n(f)
&\ge
\frac12G_n(1)\sum_i4j_i(1-j_i)\\
&\ge
G_n(1)J(f).
\end{aligned}
\]
Hence:

## Theorem 5.1 — sharp universal active-baseline obstruction

For every Boolean `f`,
\[
\boxed{
\mathscr B_n(f)\ge G_n(1)J(f)
=
\left(\frac43n+O(1)\right)J(f).
}
\tag{5.2}
\]

This is sharp. Take the genuine Boolean parity-switch phase
\[
f(x)=(-1)^{x_1x_2}
\]
with `n-2` dummy variables. Then `J(f)=1`; the two nonconstant physical derivative fields are single Walsh characters of level one and every other derivative is constant. Thus
\[
\boxed{
\mathscr B_n(f)=G_n(1)J(f)
}
\tag{5.3}
\]
for every `n>=2`.

A companion upper envelope follows from `j_i(1-j_i)<=j_i`:
\[
\boxed{
\mathscr B_n(f)\le2G_n(n-1)J(f)
=(4n+O(1))J(f).
}
\tag{5.4}
\]

For the complete quadratic phase in even dimension, every derivative spectrum lies at level `n-1`, and
\[
\mathscr B_n(f)/J(f)=G_n(n-1).
\tag{5.5}
\]

# 6. Consequence for the signed Shapley/plaquette programme

The account04 exact bridge writes, basis by basis,
\[
\frac8N L_v
=
H(g_v)-\mathcal C_v-\Theta_v.
\]
Summing the entropy curvatures gives the exact Shapley efficiency identity
\[
\sum_v\mathcal C_v
=
\sum_v H(g_v)-H(f),
\]
while the terminal shares sum to the retained terminal response.

Theorem 5.1 therefore proves a **necessary cancellation scale** for this proof architecture:

> the positive active-generator term is never `O(J)` except in bounded dimension; it is at least `(4n/3+O(1))J` for every noncharacter. Any dimension-independent FEI payment through this q-flip/Shapley compiler must cancel a linear-in-`n` amount through the genuinely signed plaquette/refund ledger before the already-paid terminal band is invoked.

This is stronger than the previous raw-support calculation, because the lower bound is imposed **after the exact frustration filter**. Randomizing the basis and discarding inactive q-flips cannot be the missing payment. The remaining universal target is therefore not channel sparsity or raw generator entropy. It is the signed refund operator itself: one must prove that the plaquette/R16/moment mechanism cancels this radial baseline to `O(J)` while preserving the `2 mod 4` credits and without replacing it by positive variation.

This conclusion does not spend the account04 Hardy/R16 bank and does not assert its pending signed domination inequality.

# 7. Self-check

`check_active_entropy_laplacian.py` was run natively and passed.

It checks:

* 506 exact rational identities for the formal coefficient of every `H_c` in the direct Krawtchouk multiplier versus the closed hitting-probability formula, for `2<=n<=12`;
* every one of the 256 Boolean functions in dimension three, comparing direct enumeration over all anchors and all coordinate orders against the spectral formula, with maximum floating discrepancy `6.22e-15`;
* the lower bound `mathscr B_n>=G_n(1)J` on all 256 dimension-three functions;
* exact sharpness numerically for `(-1)^(x_1x_2)` with dummies through `n=6`;
* the top-layer endpoint on complete quadratic phases in dimensions `2,4,6`.

Selected values:
\[
G_{10}(1)=13.891507090365252,\quad
G_{10}(9)=19.80553996817858,
\]
\[
G_{20}(1)=27.38959373933257,\quad
G_{20}(19)=40.34289840226812,
\]
\[
G_{40}(1)=54.09642558111172,\quad
G_{40}(39)=80.61414203346911.
\]

The checker is a self-check, not independent end-to-end FEI verification.

# 8. Literature/status check and next obligation

Fresh web checks on 21 September 2026 still show unrestricted FEI as open in the sources inspected. Potapov's arXiv:2609.21563 (submitted 18 September, updated 21 September) proves sharp class constants for plateaued and partially bent functions, not the universal conjecture. González--MacManus--Pereyra arXiv:2606.00246 gives further stopping-tree/classes and explicitly treats the universal implication as conditional. Han's 2025 Combinatorica bound is also weaker than FEI. No novelty or publication-priority claim is made for the internal q-flip multiplier formulation here.

**Residual universal obligation.** Having ruled out both pointwise q-flip payment and active-channel sparsification, the next B16 target is the signed operator left after subtracting the radial baseline (3.4): identify its low radial part with the authentic R16 first-separation deposits or produce an admissible Boolean counterexample to that domination. In particular, account04's pending weighted inequality must be tested/proved at the level of the genuine Borel coefficients, not by paying `H(g_v)` separately.

**Full FEI remains OPEN / NOT PROVED.**
