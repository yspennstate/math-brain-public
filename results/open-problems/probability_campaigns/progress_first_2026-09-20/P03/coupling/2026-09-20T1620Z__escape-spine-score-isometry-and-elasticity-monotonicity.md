Model actually run: GPT-5.6 Sol. Reasoning level: UNVERIFIED — GPT-6 maximum reasoning is an owner preference, not authenticated runtime telemetry.

# P03-B coupling report — escape-spine score isometry and a quenched elasticity-monotonicity certificate

**Status:** PROVED PARTIAL / NEW MARTINGALE-FISHER REDUCTION / NEW QUENCHED MONOTONICITY CERTIFICATE. The full Lyons–Pemantle–Peres speed-monotonicity conjecture remains open.

**Native role:** P03-B, `6aabe777361481919c9e614646464772`, regeneration/coupling, spine comparison and bounded-support counterexample/certificate role under `operations/progress_first_2026-09-20/OWNER_DIRECTIVE.md` and `REGISTRY.md`.

**Captured master before write:** `0bc1be16c619f23a4843d8559b3224ff47c7f02b`.

**Previous own checkpoint:** `probability_campaigns/progress_first_2026-09-20/P03/coupling/2026-09-20T1504Z__escape-spine-elasticity-band-and-terminal-child-coupling.md`.

**Complementary P03-A checkpoint consumed, not duplicated:** `probability_campaigns/progress_first_2026-09-20/P03/analytic/2026-09-20T1539Z__finite-variance-terminal-monotonicity-via-zolotarev-secants.md`. P03-A now has a candidate whole terminal interval immediately above the critical outward bias `1/EZ` under only a finite second moment. This report stays in the distinct quenched bounded-support escape-spine/coupling regime `beta d>1`.

---

## 1. Source normalization and checked frontier

The source problem is Gerard Ben Arous, Alexander Fribergh and Vladas Sidoravicius, *A proof of the Lyons-Pemantle-Peres monotonicity conjecture for high biases*, arXiv:1111.5865. Their `beta` is the **outward child bias**. At a non-root vertex with `k` children,

\[
P_\beta(x,x^*)=\frac1{1+\beta k},
\qquad
P_\beta(x,x_i)=\frac\beta{1+\beta k}.
\tag{1.1}
\]

The tree is Galton-Watson without leaves, `P(Z=0)=0`; the conjecture asks that the speed increase in the transient interval `beta>1/EZ`. The old high-bias theorem is historical input, not the present frontier.

Bowditch--Tokushige, arXiv:1906.07913, prove differentiability in the ballistic/CLT regime and represent the derivative by a Gaussian covariance; arXiv:2006.03433 proves analyticity in the ballistic regime. These are regularity tools, not a sign theorem.

The strongest broad later primary monotonicity result retained after a fresh check is He Song, Longmin Wang and Kainan Xiang, *The speed of a biased walk on a Galton-Watson tree without leaves is monotonic for low values of bias*, Journal of Applied Probability 62 (2025), 1044--1052, DOI `10.1017/jpr.2024.113`. They use reciprocal **parent bias** `lambda=1/beta` and, for minimum offspring `d>=2`, prove strict decrease for

\[
0\le \lambda\le \frac{d}{1+\sqrt{1-1/d}}.
\tag{1.2}
\]

No inverse-parameter contradiction is inferred.

---

## 2. Inherited escape-spine structure

Fix a deterministic rooted tree with

\[
d\le k_x\le D<\infty,
\qquad \beta d>1.
\tag{2.1}
\]

For a non-root vertex `x`, let

\[
h_x=P_\beta^x(T_{x^*}<\infty),
\qquad t_x=1-h_x.
\tag{2.2}
\]

If `y` ranges over the children of `x`, define

\[
S_x=\sum_y t_y,
\qquad
\pi_x(y)=\frac{t_y}{S_x}.
\tag{2.3}
\]

The inherited exact recursion and escape elasticity are

\[
h_x=\frac1{1+\beta S_x},
\qquad
g_x:=\beta\,\partial_\beta\log t_x
=-\frac{\beta h_x'}{1-h_x}.
\tag{2.4}
\]

The preceding P03-B report proved the escape-spine Green representation

\[
\boxed{
 g_x=E_x^\pi\left[\sum_{n\ge0}\prod_{j=0}^n h_{Y_j}\right],
}
\tag{2.5}
\]

where the escape spine is the Markov chain

\[
P(Y_{n+1}=y\mid Y_n=x)=\pi_x(y).
\tag{2.6}
\]

It also proved the sharp support band

\[
\frac1{\beta D}\le h_x\le\frac1{\beta d},
\qquad
\frac1{\beta D-1}\le g_x\le\frac1{\beta d-1}.
\tag{2.7}
\]

Write

\[
r:=\frac1{\beta d},
\qquad
\Delta:=\Delta_{d,D}(\beta)
=\frac1{\beta d-1}-\frac1{\beta D-1}.
\tag{2.8}
\]

The unresolved issue was how to combine the centered terminal-child score over several descendant levels without paying a linear union bound.

---

## 3. Exact escape-spine score martingale

Let

\[
\mathcal F_n=\sigma(Y_0,\ldots,Y_n),
\qquad
\bar g_x:=\sum_y\pi_x(y)g_y.
\tag{3.1}
\]

For the transition `Y_n -> Y_{n+1}`, define the ordinary `beta`-score increment

\[
\zeta_{n+1}
:=\partial_\beta\log\pi_{Y_n}(Y_{n+1}).
\tag{3.2}
\]

Because

\[
\beta\,\partial_\beta\log\pi_x(y)=g_y-\bar g_x,
\tag{3.3}
\]

we have exactly

\[
\boxed{
\zeta_{n+1}=\frac{g_{Y_{n+1}}-\bar g_{Y_n}}\beta.
}
\tag{3.4}
\]

### Theorem 3.1 — stopped score isometry

The sequence `(zeta_{n+1})` is a martingale-difference sequence under the quenched escape-spine law:

\[
E[\zeta_{n+1}\mid\mathcal F_n]=0.
\tag{3.5}
\]

Moreover

\[
E[\zeta_{n+1}^2\mid\mathcal F_n]
=\frac{\operatorname{Var}_{\pi_{Y_n}}(g)}{\beta^2}
\le \frac{\Delta^2}{4\beta^2}.
\tag{3.6}
\]

Hence for every bounded stopping time `N`, with

\[
\mathcal S_N^{\rm sel}:=\sum_{n=0}^{N-1}\zeta_{n+1},
\tag{3.7}
\]

we have the exact orthogonal decomposition

\[
\boxed{
E[(\mathcal S_N^{\rm sel})^2]
=E\sum_{n<N}
\frac{\operatorname{Var}_{\pi_{Y_n}}(g)}{\beta^2}
\le
\frac{\Delta^2}{4\beta^2}EN.
}
\tag{3.8}
\]

#### Proof

Equation (3.5) is immediate from centering in (3.4). Therefore distinct increments are orthogonal. For bounded `N`, expand the square of (3.7), discard cross terms by conditional expectation, and use Popoviciu's inequality together with the band (2.7):

\[
\operatorname{Var}_{\pi_x}(g)\le\frac14
(\max_y g_y-\min_y g_y)^2\le\frac{\Delta^2}{4}.
\]

This proves (3.8). `square`

The important point is structural: **terminal-child selection information adds in quadratic energy, not linearly in depth**.

### Corollary 3.2 — covariance bound for any stopped continuation reward

Let `F` be square-integrable and `\mathcal F_N`-measurable. The contribution to `d E_beta F/d beta` coming only from motion of the terminal-child transition kernels `pi` is

\[
E[(F-EF)\mathcal S_N^{\rm sel}],
\tag{3.9}
\]

and therefore

\[
\boxed{
\left|E[(F-EF)\mathcal S_N^{\rm sel}]\right|
\le
\frac{\Delta}{2\beta}
\sqrt{EN\,\operatorname{Var}(F)}.
}
\tag{3.10}
\]

This is the global analogue of the preceding one-step Gruss bound. It is `sqrt(N)` rather than `N` at the score level.

### Corollary 3.3 — local multi-level coupling cost

For deterministic depth `N=n`, standard first-order total-variation differentiation gives

\[
\boxed{
\|P_{\beta+\varepsilon}^{(n)}-P_\beta^{(n)}\|_{\rm TV}
\le
\frac{|\varepsilon|\Delta}{4\beta}\sqrt n
+o(|\varepsilon|),
}
\tag{3.11}
\]

for the escape-spine child sequence up to depth `n`. Thus a maximal coupling can be chosen whose terminal-child mismatch probability grows at most like `sqrt(n)` to first order, rather than the linear bound obtained by summing one-step mismatch probabilities.

This is a coupling statement for the coarse escape-spine child identities. It is not a speed-monotonicity theorem.

---

## 4. Infinite discounted score energy is finite

The Green representation (2.5) naturally discounts deep levels by products of return probabilities. Let

\[
W_n:=\prod_{j=0}^n h_{Y_j}.
\tag{4.1}
\]

Then `W_n` is `F_n`-measurable and

\[
0\le W_n\le r^{n+1}.
\tag{4.2}
\]

Put the dimensionless centered child score

\[
\eta_{n+1}:=g_{Y_{n+1}}-\bar g_{Y_n}=\beta\zeta_{n+1}.
\tag{4.3}
\]

By orthogonality,

\[
\boxed{
E\left[\left(\sum_{n\ge0}W_n\eta_{n+1}\right)^2\right]
=
E\sum_{n\ge0}W_n^2
\operatorname{Var}_{\pi_{Y_n}}(g)
\le
\frac{\Delta^2}{4}\frac{r^2}{1-r^2}.
}
\tag{4.4}
\]

Hence the infinite-depth descendant selection score that is weighted in the same geometric scale as the escape Green kernel has a finite, explicit `L^2` budget. This is the first point in the P03-B line where the recursively repeated terminal-child selection can be treated globally without either a depth cutoff or a linear union bound.

---

## 5. Differentiating the Green representation: direct contraction versus branch-selection noise

The preceding martingale estimate can be pushed one step further to obtain a genuine sign theorem for the escape elasticity itself.

Define the logarithmic derivative operator

\[
D:=\beta\frac d{d\beta}.
\tag{5.1}
\]

From the definition of `g`,

\[
D h_x=-t_x g_x,
\qquad
D\log h_x=-\frac{t_xg_x}{h_x}.
\tag{5.2}
\]

For a finite truncation

\[
G_N:=\sum_{n=0}^N W_n,
\tag{5.3}
\]

there are two contributions to `D E^pi G_N`:

1. the direct decrease of the return factors `h`, and
2. movement of the escape-spine transition law `pi`.

The geometric bounds above make both terms absolutely summable, so `N -> infinity` is justified by dominated convergence.

### 5.1 Direct negative term

Set

\[
a_x:=\frac{t_xg_x}{h_x}.
\tag{5.4}
\]

Using (2.7),

\[
t_x\ge1-r,
\qquad h_x\le r,
\qquad g_x\ge\frac1{\beta D-1},
\]

and therefore

\[
\boxed{
a_x\ge c_0:=\frac{\beta d-1}{\beta D-1}.}
\tag{5.5}
\]

The direct contribution has magnitude

\[
A:=E^\pi\sum_{n\ge0}W_n\sum_{j=0}^n a_{Y_j}.
\tag{5.6}
\]

Also `h_x>=1/(beta D)`. Hence

\[
\begin{aligned}
A
&\ge c_0\sum_{n\ge0}(n+1)(\beta D)^{-(n+1)}\\
&=\boxed{
\frac{\beta D(\beta d-1)}{(\beta D-1)^3}.
}
\tag{5.7}
\end{aligned}
\]

### 5.2 Branch-selection term

At transition `j`, only the future tail

\[
R_{j+1}:=\sum_{n\ge j+1}W_n
\tag{5.8}
\]

can correlate with the centered score `eta_{j+1}`. Conditional on `F_j`,

\[
0\le R_{j+1}\le W_j\frac r{1-r}.
\tag{5.9}
\]

The conditional range of `eta_{j+1}` is at most `Delta`. Weighted Gruss therefore gives

\[
\left|E[\eta_{j+1}R_{j+1}\mid\mathcal F_j]\right|
\le
\frac\Delta4W_j\frac r{1-r}.
\tag{5.10}
\]

Summing and using `W_j<=r^{j+1}` yields the complete branch-selection envelope

\[
\boxed{
|B|
\le
\frac\Delta4\frac{r^2}{(1-r)^2}.
}
\tag{5.11}
\]

Since

\[
D g_x=-A+B,
\tag{5.12}
\]

we obtain an explicit uniform sufficient condition for `g_x` itself to decrease with outward bias.

---

## 6. New quenched monotonicity certificate for the escape elasticity

Write

\[
x:=\beta d>1,
\qquad
\kappa:=\frac Dd\ge1.
\tag{6.1}
\]

Then

\[
\Delta=
\frac{x(\kappa-1)}{(x-1)(\kappa x-1)},
\qquad
r=\frac1x.
\tag{6.2}
\]

Comparing (5.7) and (5.11) gives the condition

\[
\boxed{
4\kappa(x-1)^4
>
(\kappa-1)(\kappa x-1)^2.
}
\tag{6.3}
\]

### Theorem 6.1 — uniform decrease of escape elasticity

For every deterministic rooted tree with offspring counts in `[d,D]`, if `beta d>1` and (6.3) holds, then at every non-root vertex

\[
\boxed{
\frac d{d\beta}g_x(\beta)<0.
}
\tag{6.4}
\]

Thus in this parameter region the harmonic escape elasticity is itself strictly decreasing with outward bias, despite the fact that terminal-child identities need not admit a pointwise monotone ordering.

This is a **quenched component theorem**. It does not by itself imply that the annealed asymptotic speed is increasing.

### Near-regular consequence

As `kappa=1+epsilon ->1`, the positive root of the equality in (6.3) satisfies

\[
\boxed{
 x_*(\kappa)=1+\frac12\sqrt{\kappa-1}+O(\kappa-1).
}
\tag{6.5}
\]

So the certificate approaches the full descendant-contraction threshold `beta d>1` for nearly regular offspring support.

### Exact `{2,3}` consequence

For `d=2,D=3`, condition (6.3) is equivalent, in the relevant region `beta>1/2`, to

\[
192\beta^4-384\beta^3+279\beta^2-90\beta+11>0.
\tag{6.6}
\]

Its relevant root is

\[
\boxed{
\beta_*=0.826892471630794\ldots .
}
\tag{6.7}
\]

Hence for every deterministic `[2,3]`-degree tree,

\[
\boxed{
g_x'(\beta)<0\quad\text{for all }\beta>0.826892471630794\ldots .}
\tag{6.8}
\]

For comparison only, the 2025 Song--Wang--Xiang full-speed theorem with `d=2` corresponds to outward bias

\[
\beta\ge \frac{1+1/\sqrt2}{2}
=0.853553390593\ldots .
\tag{6.9}
\]

Thus the **component** monotonicity certificate penetrates slightly into a region not covered by that full-speed theorem. This is not being relabeled as a new speed-monotonicity interval.

For `d=3,D=4`, equality in (6.3) occurs exactly at `x=3/2`, so the component theorem holds for

\[
\boxed{\beta>1/2.}
\tag{6.10}
\]

---

## 7. What this changes in the P03-B proof architecture

The previous run left a centered terminal-child score at every descendant level. Treating those scores separately would accumulate the one-step total-variation bound linearly and quickly erase the useful coupling margin.

The present run changes that in two ways.

First, the scores are an exact martingale-difference sequence and their Fisher information is additive. Any stopped continuation reward pays the square-root energy bound (3.10), and geometrically discounted descendants have the finite infinite-depth budget (4.4).

Second, after differentiating the same escape-spine Green representation, the deterministic negative contraction beats the entire branch-selection score whenever (6.3) holds. In the `[2,3]` case this is already true at `beta>0.826892...`, below the outward-bias endpoint `0.853553...` of the strongest checked full-speed theorem.

This identifies a more precise remaining obstruction: **not descendant terminal-child score accumulation itself, but its covariance with regeneration time/radial reward together with parent-side selected-ancestor transport.** The descendant harmonic kernel now has both an `L^2` energy budget and a nontrivial quenched sign region.

---

## 8. Remaining obstruction and next attack

The full LPP conjecture remains open. Nothing here proves that the derivative of the asymptotic speed has the correct sign.

The next P03-B attack is to insert the score isometry directly into one regeneration block. Write the block derivative as the sum of:

- direct radial drift / decisive-exit response;
- parent-side common-spine and selected-ancestor terms already bounded in earlier P03-B reports;
- terminal-child selection score `S_sel`.

The target is to prove a block covariance estimate of the form

\[
\left|\operatorname{Cov}(\tau_{\rm reg},S_{\rm sel})\right|
\le
\frac{\Delta}{2\beta}
\sqrt{E N_{\rm esc}\,\operatorname{Var}(\tau_{\rm reg})},
\tag{8.1}
\]

with an analogous estimate for the regeneration displacement, then compare the resulting explicit constant with the inherited positive direct margin. The key point is that upstream/common-spine score is orthogonal to each *future centered child-selection increment* until the continuation reward couples them, so score energy should combine quadratically rather than by a worst-case sum.

If this fails quantitatively, the fallback is a source-valid bounded-support cylinder showing that regeneration-time variance, rather than terminal branch selection itself, consumes the margin. That would give a rigorous obstruction to the current coupling mechanism and a clean handoff to the Bowditch--Tokushige covariance representation.

---

## 9. Obligation ledger

- **Full-source LPP conjecture:** OPEN.
- **Bias convention:** outward `beta`; parent probability `1/(1+beta k)`; no inverse-parametrization confusion.
- **High-bias literature:** historical only; not repeated as new progress.
- **New theorem A:** exact stopped escape-spine score/Fisher isometry, proved.
- **New theorem B:** finite infinite-depth discounted selection-energy bound, proved.
- **New theorem C:** uniform quenched decrease of `g_x` under (6.3), proved.
- **Concrete nontrivial family:** `[2,3]` support certificate `beta>0.826892471630794...`; component only.
- **Remaining gap:** convert these descendant score bounds plus existing parent-side estimates into a positive regeneration speed derivative.
- **Next attack:** regeneration-block covariance with `S_sel`, not another admission/audit loop.
