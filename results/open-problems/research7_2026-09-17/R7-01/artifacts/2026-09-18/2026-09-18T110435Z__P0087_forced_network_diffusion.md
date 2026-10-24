Model actually running: GPT-5.6 Sol. Reasoning level: UNVERIFIED — this is not GPT-6 at maximum; no authenticated runtime reasoning-effort telemetry or binding selector is exposed.

# P0087: Perron projection and the forced-network Wright–Fisher limit

Date: 2026-09-18.  
Worker: R7-01 (`6aabe777361481919c9e614646464772`).  
Status: **candidate source-level mathematical solution; operationally PARTIAL pending the independent audits and paper package required by the owner directive.**  
Novelty: **UNVERIFIED.**

## 1. Source model and exact question

Open Problem 16 of Aletti et al., *Open Problems in Stochastic Reinforcement Models* (published 2025; printed pp. 14–16) considers a network of `N>=2` interacting reinforced stochastic processes with binary actions and a forcing input. The network model is the one introduced by Aletti–Crimaldi–Ghiglietti; in that parent model the coordinate actions are conditionally independent given the past.

Put `Q=A^T`. The source assumptions are:

- `Q` is a nonnegative irreducible row-stochastic `N x N` matrix (`Q 1 = 1`);
- `p in [0,1]^N` is the forcing vector;
- conditional on `F_n`, the variables `X_{n+1,j}` are independent Bernoulli variables with
  `E[X_{n+1}|F_n]=Q Z_n`;
- for constants `r>0`, `f>=0`, `r+f<=1`,

`Z_{n+1}=(1-r-f)Z_n+rX_{n+1}+fp`.

The source asks for the fixed-parameter convergence/nonconvergence behavior and, in the regime `r -> 0`, `f ~ c r^2`, for a proper continuous-time scaling limit.

The campaign's earlier attempt `P0087-A001` already gave a complete fixed-parameter classification. I reproduce that argument in Section 2 so the present artifact is self-contained. Sections 3–8 prove the diffusion limit.

---

## 2. Fixed parameters: complete convergence classification

### Theorem 2.1

Assume `0<r`, `0<f`, `r+f<=1`, `Q` irreducible and row-stochastic, and the source conditional-mean equation. Then:

1. if `p=0`, `Z_n -> 0` almost surely;
2. if `p=1`, `Z_n -> 1` almost surely;
3. if `p` is neither the all-zero nor the all-one vector, then
   `P(Z_n converges)=0`.

Conditional independence is not needed for this fixed-parameter theorem.

### Proof

Let `pi` be the unique positive stationary probability row-vector of `Q`:

`pi^T Q = pi^T`, `pi_j>0`, `sum_j pi_j=1`.

First suppose `p=0`. Put `Y_n=pi^T Z_n`. Since `pi^T Q=pi^T`,

`E[Y_{n+1}|F_n]=(1-r-f)Y_n+r pi^T QZ_n=(1-f)Y_n`.

Hence `E Y_n=(1-f)^n E Y_0`. For every `delta>0`,

`sum_n P(Y_n>delta) <= delta^{-1} E Y_0 sum_n (1-f)^n < infinity`.

By Borel–Cantelli, `Y_n->0` a.s. Because all coordinates are nonnegative and `pi_j>0`,

`0 <= Z_{n,j} <= Y_n/pi_j`,

so every coordinate tends to zero. The case `p=1` follows by applying the same argument to `1-Z_n`.

Now suppose that on an event `E` the vector `Z_n` converges to `z`. Rearranging the recursion gives

`r X_{n+1}=Z_{n+1}-(1-r-f)Z_n-fp`.

Therefore on `E`, `X_{n+1}` converges. Since `X_{n+1}` takes values in the finite set `{0,1}^N`, it is eventually constant on `E`; write its eventual value as `x in {0,1}^N`. Taking limits gives

`(r+f)z=rx+fp`.                                      (2.1)

Let `xi_{n+1}=X_{n+1}-QZ_n`. This is a bounded martingale difference. The martingale strong law gives

`(1/n) sum_{k=0}^{n-1} xi_{k+1} -> 0` a.s.

On `E`, Cesàro convergence and eventual constancy of `X` therefore imply

`x=Qz`.                                                (2.2)

If some coordinate `x_j=0`, then `(Qz)_j=0`. Since `Q` and `z` are nonnegative, every `i` with `Q_{ji}>0` has `z_i=0`. Equation (2.1) then forces `x_i=p_i=0` for all such predecessors. Iterating through the directed graph and using irreducibility forces `x=p=0` on all coordinates. Thus, if `x` has any zero coordinate, the only possible forcing vector is `p=0`.

If `x` has no zero coordinate, then `x=1`. From `Qz=1`, every positive predecessor entering any row must have `z_i=1`; irreducibility and (2.1) force `p=1`. Thus convergence is possible only for the two degenerate forcing vectors already handled. QED.

---

## 3. The singular scaling and the correct slow coordinate

Set `epsilon=r` and let `f_epsilon/epsilon^2 -> c` with `c>=0`. For each `epsilon`, write

`Z_{n+1}^e = Z_n^e + epsilon (Q-I)Z_n^e + f_e(p-Z_n^e) + epsilon xi_{n+1}^e`,   (3.1)

where

`xi_{n+1}^e := X_{n+1}^e-QZ_n^e`,

so `E[xi_{n+1}^e|F_n]=0`.

The source heuristic leaves an interaction term that is singular on the `epsilon^{-2}` scale. The singularity is real but it does not create a new vector-valued noise term: it forces all non-Perron modes to collapse on a much faster `epsilon^{-1}` step scale.

Let `pi` be as above and define

`Y_n^e := pi^T Z_n^e`,  `pbar := pi^T p`,  `kappa := sum_j pi_j^2`.

Multiplying (3.1) by `pi^T` annihilates the interaction drift exactly:

`Y_{n+1}^e-Y_n^e = f_e(pbar-Y_n^e) + epsilon eta_{n+1}^e`,  (3.2)

where

`eta_{n+1}^e := pi^T xi_{n+1}^e`

is a bounded martingale difference.

Conditional independence gives, with `q_n=QZ_n^e`,

`E[(eta_{n+1}^e)^2|F_n]
   = v(Z_n^e)
   := sum_j pi_j^2 q_{n,j}(1-q_{n,j})`.              (3.3)

Thus `pi^T Z` is the unique slow scalar coordinate.

---

## 4. Fast synchronization: a quantitative lemma

Let

`P := I-1 pi^T`,  `W_n^e := PZ_n^e = Z_n^e-1Y_n^e`.

Then `pi^T W_n^e=0`. Since `Q1=1` and `pi^TQ=pi^T`, `P` commutes with `Q`. Applying `P` to (3.1) gives the exact linear recursion

`W_{n+1}^e = T_e W_n^e + f_e Pp + epsilon P xi_{n+1}^e`,                 (4.1)

where, on the hyperplane `H={w:pi^T w=0}`,

`T_e := I-epsilon(I-Q)-f_e I`.

### Lemma 4.1 (spectral contraction)

There are constants `a>0`, `C<infinity` and `e_0>0`, depending only on `Q`, such that for `0<epsilon<e_0`,

`||T_e^m w|| <= C exp(-a epsilon m)||w||` for every `w in H` and `m>=0`.   (4.2)

#### Proof

The eigenvalue 1 of an irreducible stochastic matrix is simple. Every other eigenvalue `lambda` of `Q` satisfies `Re(lambda)<1`; this remains true when `Q` is periodic, because a unit-modulus eigenvalue `lambda != 1` still has `Re(lambda)<1`. Therefore all eigenvalues of `B=(I-Q)|_H` have strictly positive real parts.

For a Hurwitz matrix `B` there is a positive-definite quadratic form `M` on `H` solving a Lyapunov inequality

`B^*M+MB >= 2a_0 M`

for some `a_0>0`. Expanding

`T_e^* M T_e-M`

and using `f_e=O(epsilon^2)` yields, for sufficiently small `epsilon`,

`T_e^* M T_e <= (1-a_0 epsilon)M`.

Iterating in the `M`-norm and using equivalence of norms on finite-dimensional `H` proves (4.2). QED.

### Lemma 4.2 (second-moment synchronization)

Uniformly for `n>=0`,

`E ||W_n^e||^2 <= C exp(-a epsilon n)||W_0^e||^2 + C epsilon`.            (4.3)

Consequently, for every fixed `T`,

`epsilon^2 sum_{n < T/epsilon^2} E||W_n^e|| -> 0`.                      (4.4)

#### Proof

Use the Lyapunov norm from Lemma 4.1 in (4.1). Conditional on `F_n`, the noise has mean zero and is uniformly bounded. For small epsilon,

`E[||W_{n+1}^e||_M^2|F_n]
 <= (1-a epsilon)||W_n^e||_M^2 + C epsilon^2 + C f_e^2/epsilon`.

The last term comes from absorbing the deterministic forcing cross term into half of the contraction. Since `f_e=O(epsilon^2)`, it is `O(epsilon^3)` and can be absorbed into `C epsilon^2`. Iteration gives (4.3). Taking square roots and summing a geometric transient plus the `O(sqrt(epsilon))` stationary term gives

`epsilon^2 sum_{n<T/epsilon^2} E||W_n^e||
 <= C epsilon + C T sqrt(epsilon) -> 0`.

QED.

### Lemma 4.3 (uniform collapse after the initial layer)

For every `0<delta<T`,

`sup_{delta <= t <= T} ||W^e(floor(t/epsilon^2))|| -> 0`

in probability. If `W_0^e -> 0`, then the same holds with `delta=0`.

#### Proof

Iterating (4.1),

`W_n^e=T_e^nW_0^e + f_e sum_{j=0}^{n-1}T_e^jPp
       + epsilon sum_{k=1}^n T_e^{n-k}Pxi_k^e`.                         (4.5)

The first term is at most `C exp(-a epsilon n)||W_0^e||`, so it vanishes uniformly for `n>=delta/epsilon^2`; if `W_0^e->0`, it is uniformly negligible from time zero. The forcing term is at most

`C f_e sum_{j>=0} exp(-a epsilon j)=O(f_e/epsilon)=O(epsilon)`.

For a fixed `n` and any fixed coordinate, the last term in (4.5) is a martingale sum with deterministic coefficient norms bounded by

`C epsilon exp(-a epsilon(n-k))`.

The sum of the squared increment bounds is `O(epsilon)`. Azuma–Hoeffding therefore gives

`P(||epsilon sum_{k=1}^n T_e^{n-k}Pxi_k^e||>u)
 <= C exp(-c u^2/epsilon)`.

There are only `O(epsilon^{-2})` indices `n<=T/epsilon^2`. A union bound yields

`P(max_{n<=T/epsilon^2} ||noise convolution||>u)
 <= C_T epsilon^{-2} exp(-c u^2/epsilon) -> 0`

for every fixed `u>0`. Combine the three terms. QED.

---

## 5. Quadratic variation collapses to a scalar coefficient

The function `h(x)=x(1-x)` is 1-Lipschitz on `[0,1]`. Since

`QZ_n^e = Y_n^e 1 + QW_n^e`,

(3.3) gives

`|v(Z_n^e)-kappa Y_n^e(1-Y_n^e)| <= C ||W_n^e||`.                      (5.1)

By (4.4), for every fixed `T`,

`epsilon^2 sum_{n<T/epsilon^2}
 |v(Z_n^e)-kappa Y_n^e(1-Y_n^e)| -> 0`

in `L^1`, hence in probability.                                                        (5.2)

This is the precise replacement for the source's unresolved matrix-valued heuristic noise.

---

## 6. Diffusion theorem

### Theorem 6.1 (forced-network Wright–Fisher limit)

Let `epsilon -> 0`, `f_e/epsilon^2 -> c in [0,infinity)`, and assume `Y_0^e=pi^T Z_0^e -> y_0`. Define the piecewise-constant rescaling

`Y^e(t)=Y^e_{floor(t/epsilon^2)}`.

Then for every `T<infinity`,

`Y^e => Y` in `D([0,T],[0,1])`,

where `Y` is the unique weak solution of

`dY_t = c(pbar-Y_t) dt + sqrt(kappa Y_t(1-Y_t)) dB_t`,   `Y_0=y_0`.     (6.1)

Moreover, for every `0<delta<T`,

`sup_{delta<=t<=T} ||Z^e_{floor(t/epsilon^2)}-1Y^e(t)|| -> 0`

in probability. If `Z_0^e-1Y_0^e ->0`, then the vector process itself converges on the full interval:

`Z^e_{floor(t/epsilon^2)} => 1Y_t` in `D([0,T],[0,1]^N)`.               (6.2)

For arbitrary nonsynchronized initial data, (6.2) holds on every `[delta,T]`, `delta>0`; the missing time-zero convergence is a genuine vanishing-width initial layer, not a mathematical gap.

### Proof

From (3.2), write

`Y^e(t)=Y_0^e+A^e(t)+M^e(t)`,

where

`A^e(t)=sum_{k<floor(t/epsilon^2)} f_e(pbar-Y_k^e)`

and

`M^e(t)=sum_{k<floor(t/epsilon^2)} epsilon eta_{k+1}^e`.

The drift increments on a macroscopic interval of length `theta` are bounded by `C(theta+epsilon^2)` because `f_e/epsilon^2` stays bounded. The predictable quadratic variation of the martingale over such an interval is also bounded by `C(theta+epsilon^2)`, since `v<=1`. Jumps are `O(epsilon)`. Aldous' tightness criterion therefore gives tightness of `{Y^e}` in `D([0,T])`; every limit is continuous.

To identify a subsequential limit, take `phi in C^3([0,1])`. From (3.2), conditional on `F_n`,

`E[Delta Y_n^e|F_n]=f_e(pbar-Y_n^e)`,

`E[(Delta Y_n^e)^2|F_n]
 = epsilon^2 v(Z_n^e)+f_e^2(pbar-Y_n^e)^2`,

and `|Delta Y_n^e|<=epsilon+f_e=O(epsilon)`. Taylor's theorem gives a one-step conditional generator

`E[phi(Y_{n+1}^e)-phi(Y_n^e)|F_n]
 = f_e(pbar-Y_n^e) phi'(Y_n^e)
   + (epsilon^2/2) v(Z_n^e) phi''(Y_n^e)
   + O(epsilon^3+f_e^2)`,

uniformly in the state. Summed over `O(epsilon^{-2})` steps, the remainder is `O(epsilon)+O(epsilon^2) ->0`.

The drift sum converges to

`integral_0^t c(pbar-Y_s)phi'(Y_s) ds`

because `f_e/epsilon^2->c`. By (5.2), the quadratic term converges to

`(1/2) integral_0^t kappa Y_s(1-Y_s) phi''(Y_s) ds`.

Hence every subsequential limit solves the martingale problem for

`L phi(y)=c(pbar-y)phi'(y)+(kappa/2)y(1-y)phi''(y)`.                    (6.3)

The drift is Lipschitz and the diffusion coefficient `sqrt(kappa y(1-y))` is one-half Hölder with the standard Yamada–Watanabe modulus; the Jacobi/Wright–Fisher SDE (6.1) has a unique weak law on `[0,1]`. Therefore the entire sequence converges.

The vector statements now follow immediately from Lemma 4.3 and Slutsky's theorem in path space. QED.

---

## 7. What happens to the source's singular interaction term

The source informally writes the interaction contribution at the diffusion scale as something like

`-(I-Q)Y_t "(sqrt(dt))"`.

Theorem 6.1 gives its precise meaning. A non-Perron eigenmode with eigenvalue `lambda !=1` has deterministic one-step multiplier approximately

`1-epsilon(1-lambda)`.

Over `n=t/epsilon^2` steps its magnitude is approximately

`exp(-(1-Re lambda)t/epsilon)`,

which tends to zero for every `t>0`. Even if `Q` is periodic and `|lambda|=1`, one still has `Re lambda<1` for `lambda !=1`; e.g. the period-two eigenvalue `lambda=-1` decays like `exp(-2t/epsilon)`. Thus the singular term is an **infinitely fast synchronization constraint**, leaving only the Perron coordinate as a stochastic degree of freedom.

---

## 8. Sharp topology dependence of the limiting noise

The network enters the scalar diffusion through exactly two Perron statistics:

`pbar=pi^T p`,  `kappa=||pi||_2^2`.

Since `pi` is a probability vector,

`1/N <= kappa < 1`                                                       (8.1)

for every irreducible `N>=2` network. Equality `kappa=1/N` holds exactly when `pi` is uniform; in particular every irreducible doubly stochastic network attains the minimum. The supremum over irreducible networks is 1, approached by stationary distributions concentrating arbitrarily strongly on one vertex, but not attained while every `pi_j>0`.

So the diffusion coefficient is smallest for a balanced stationary network and can be made arbitrarily close to the single-agent coefficient in highly imbalanced networks.

---

## 9. Section-B method ledger

### B2 — attack the negation first

I attacked the possibility that the source's singular vector interaction survives on the `r^{-2}` scale. It does not: every non-Perron mode is damped at rate `exp(-a t/r)`. Periodicity of the irreducible network does not rescue any mode. This identifies the source heuristic's singular term as a fast constraint rather than a finite vector drift.

### B24 — find the extremal object

Once the limit is projected, network topology appears through `kappa=sum pi_j^2`. Cauchy–Schwarz gives the exact sharp minimum `1/N` at the uniform stationary law and supremum 1 over irreducible networks. This exposes the complete extremal range of the limiting noise strength.

### B11 — dualize

The stationary left Perron vector is the dual object that kills the interaction drift exactly. The identity

`pi^T(Q-I)=0`

reduces the singular N-dimensional recursion to the scalar martingale equation (3.2), after which the only remaining task is to prove fast collapse of the transverse modes and identify their effect on quadratic variation.

---

## 10. Scope, gaps, and prior art

Mathematically, Sections 2 and 6 answer both explicit parts of Open Problem 16 under the inherited conditionally independent network-RSP model. The only scope caveat is the unavoidable initial layer for nonsynchronized starting vectors: the full vector cannot converge in `D([0,T])` to a continuous consensus-valued process while retaining a nonsynchronized value at `t=0`; convergence holds on every `[delta,T]`, and on `[0,T]` when the initial vectors already approach the consensus manifold. The projected Perron coordinate always converges from time zero.

A bounded literature check on 2026-09-18 found the 2024 first-order-asymptotics and polarization papers by Aletti–Crimaldi–Ghiglietti, the scalar 2021 rescaled-Pólya/Wright–Fisher paper, and 2026 innovation/feature-allocation work by the same authors, but no paper identified in that search that states this forced-network singular-limit theorem. This is negative evidence only; **novelty and worldwide openness remain UNVERIFIED**.

No operational closure is claimed. The owner protocol still requires an independent P26 audit, a distinct OTHER-track audit, a final dated prior-art review, and a self-contained `paper_<name>/` package before the repository may label the source PROVED.
