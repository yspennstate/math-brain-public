Model actually running: GPT-5.6 Sol. Reasoning level: UNVERIFIED — this is not GPT-6 at maximum; no authenticated runtime reasoning-effort telemetry or binding selector is exposed.

# P0087: forcing-exponent phase diagram, Jacobi boundary law, and stationary small-step limits

Date: 2026-09-18.  
Worker: R7-01 (`6aabe777361481919c9e614646464772`).  
Source target: G. Aletti et al., *Open Problems in Stochastic Reinforcement Models* (published 2025), Open Problem 16, printed pp. 14–16.  
Status: **PARTIAL operationally**. The cumulative R7-01 record already contains a candidate source-level proof of both explicit source clauses; this artifact strengthens the diffusion half and maps the neighboring forcing regimes. Novelty remains **UNVERIFIED**.

## 1. Model and cumulative input

Write `epsilon=r_r` and `f_epsilon=r_f`. Put `Q=A^T`. Under the source hypotheses, `Q` is a fixed irreducible row-stochastic `N x N` matrix, `p in [0,1]^N`, and conditional on `F_n` the binary action coordinates are independent with

`E[X_{n+1}^epsilon | F_n] = Q Z_n^epsilon`.

The recursion is

`Z_{n+1}^epsilon = (1-epsilon-f_epsilon) Z_n^epsilon + epsilon X_{n+1}^epsilon + f_epsilon p`.       (1.1)

Let

`xi_{n+1}^epsilon = X_{n+1}^epsilon-QZ_n^epsilon`,

so that

`Z_{n+1}^epsilon-Z_n^epsilon
 = epsilon(Q-I)Z_n^epsilon + f_epsilon(p-Z_n^epsilon)+epsilon xi_{n+1}^epsilon`.                    (1.2)

Let `pi` be the unique positive stationary probability row vector,

`pi^T Q=pi^T`, `pi^T 1=1`,

and define

`Y_n^epsilon=pi^T Z_n^epsilon`, `pbar=pi^T p`, `kappa=sum_j pi_j^2`,
`P=I-1 pi^T`, `W_n^epsilon=PZ_n^epsilon`,
`H={w: pi^T w=0}`, `B=(I-Q)|_H`.                                      (1.3)

Irreducibility implies that every eigenvalue of `B` has strictly positive real part. The exact projected recursions are

`Y_{n+1}-Y_n = f_epsilon(pbar-Y_n)+epsilon eta_{n+1}`,                 (1.4)

where `eta_{n+1}=pi^T xi_{n+1}`, and

`W_{n+1}=T_epsilon W_n+f_epsilon Pp+epsilon Pxi_{n+1}`,
`T_epsilon=I-epsilon B-f_epsilon I` on `H`.                            (1.5)

Conditional independence gives

`E[eta_{n+1}^2|F_n]
 = v(Z_n):=sum_j pi_j^2 (QZ_n)_j(1-(QZ_n)_j)`.                         (1.6)

The preceding cumulative proof establishes the critical limit when `f_epsilon/epsilon^2 -> c`:

`dY_t=c(pbar-Y_t)dt+sqrt(kappa Y_t(1-Y_t)) dB_t`,                     (1.7)

with vector collapse to `1Y_t` after the `epsilon^{-1}` synchronization layer. The present artifact asks what happens on *all* power-law forcing scales and what the limiting diffusion says exactly about the source's boundary question.

The methods are B5 (add a parameter and differentiate), B18 (translate the statement), and B27 (swap the quantifiers).

---

## 2. B5 — add the forcing exponent and differentiate the network/forcing ratio

Assume throughout this section

`f_epsilon ~ c epsilon^alpha`, `c>0`, `alpha>0`.                       (2.1)

There are two independent small-step clocks: synchronization acts on `n~epsilon^{-1}`, forcing on `n~f_epsilon^{-1}`, and martingale diffusion on `n~epsilon^{-2}`. Their ordering changes exactly at `alpha=1` and `alpha=2`.

### Theorem 2.1 (complete power-law dynamical phase diagram)

Suppose `Z_0^epsilon -> z_0` in probability.

**(i) `0<alpha<1`: forcing precedes network mixing.** On the forcing scale

`Zhat^epsilon(t)=Z^epsilon_floor(t/f_epsilon)`,

for every finite `T`,

`sup_{0<=t<=T} ||Zhat^epsilon(t)-z(t)|| -> 0` in probability,         (2.2)

where

`z'(t)=p-z(t)`, `z(0)=z_0`,

hence

`z(t)=p+e^{-t}(z_0-p)`.                                               (2.3)

**(ii) `alpha=1`: network and forcing compete on one deterministic scale.** If `f_epsilon/epsilon -> c`, then on `s=epsilon n`,

`Z^epsilon_floor(s/epsilon) -> z_c(s)`                                (2.4)

uniformly on compact intervals in probability, where

`z_c'(s)=(Q-I)z_c(s)+c(p-z_c(s))`, `z_c(0)=z_0`.                      (2.5)

Its unique equilibrium is

`z_c^* = 1 pbar + c(B+cI)^{-1}Pp`.                                   (2.6)

**(iii) `1<alpha<2`: synchronization precedes a deterministic forcing drift.** Put

`y(t)=pbar+(pi^T z_0-pbar)e^{-t}`.                                   (2.7)

Then for every `0<delta<T`,

`sup_{delta<=t<=T}
 ||Z^epsilon_floor(t/f_epsilon)-1 y(t)|| ->0` in probability.         (2.8)

If `Pz_0=0`, the convergence is uniform also on `[0,T]`.

**(iv) `alpha=2`: critical forced Wright–Fisher scale.** On `t=epsilon^2 n`, after the vanishing synchronization layer,

`Z^epsilon_floor(t/epsilon^2) => 1Y_t`,                              (2.9)

where `Y` solves (1.7).

**(v) `alpha>2`: forcing disappears on the diffusion scale.** On `t=epsilon^2 n`, after the same synchronization layer,

`Z^epsilon_floor(t/epsilon^2) => 1Y_t`,                              (2.10)

where

`dY_t=sqrt(kappa Y_t(1-Y_t))dB_t`.                                  (2.11)

Thus `alpha=1` is the deterministic network/forcing crossover and `alpha=2` is the deterministic-forcing/noise crossover after synchronization.

### Proof

For (i), define

`S_epsilon=(1-epsilon-f_epsilon)I+epsilon Q`.

Equation (1.1) is

`Z_{n+1}=S_epsilon Z_n+f_epsilon p+epsilon xi_{n+1}`.                 (2.12)

Because `Q` is row-stochastic and all coefficients are nonnegative for small `epsilon`,

`||S_epsilon^m||_infinity <= (1-f_epsilon)^m`.                       (2.13)

On `m<=T/f_epsilon`, the raw martingale

`M_m=epsilon sum_{k=1}^m xi_k`

satisfies, by bounded increments and Doob,

`E max_{m<=T/f_epsilon}||M_m||^2 <= C_T epsilon^2/f_epsilon ->0`,     (2.14)

since `alpha<2`. Abel summation transfers (2.14) to the filtered convolution

`epsilon sum_{k=1}^m S_epsilon^{m-k}xi_k`;                           (2.15)

the multiplier is bounded because

`||S_epsilon-I|| sum_{j>=0}||S_epsilon^j||
 <= C(epsilon+f_epsilon)/f_epsilon = O(1)`                           (2.16)

when `alpha<1`. Meanwhile

`S_epsilon=I+f_epsilon[-I+(epsilon/f_epsilon)(Q-I)]`,                (2.17)

and `epsilon/f_epsilon ->0`. The deterministic Euler scheme therefore converges uniformly on compact forcing-time intervals to `z'=p-z`. This proves (i).

For (ii),

`S_epsilon=I+epsilon[(Q-I)-cI]+o(epsilon)`,
`f_epsilon p=c epsilon p+o(epsilon)`.                                (2.18)

The martingale maximal second moment over `O(epsilon^-1)` steps is `O(epsilon)`. Standard finite-dimensional Euler convergence therefore gives (2.4)–(2.5). At equilibrium write `z=1y+w`, `w in H`. Perron projection gives `y=pbar`, while the transverse equation is

`(B+cI)w=cPp`,                                                       (2.19)

which gives (2.6).

For (iii), equation (1.4) is a scalar stable Euler recursion. On `m<=T/f_epsilon`, its martingale contribution has maximal second moment `O(epsilon^2/f_epsilon)->0`, and therefore

`Y_floor(t/f_epsilon) -> y(t)`                                      (2.20)

uniformly on `[0,T]` in probability. Iterating (1.5), use stability of `B`: for small `epsilon`, there are `C,a>0` with

`||T_epsilon^j||_H <= C exp(-a epsilon j)`.                          (2.21)

The deterministic forcing contribution is `O(f_epsilon/epsilon)->0`. The initial transverse term at time `t/f_epsilon` is bounded by

`C exp[-a epsilon t/f_epsilon]||W_0||`,                              (2.22)

which tends to zero uniformly for `t>=delta>0` because `epsilon/f_epsilon -> infinity`. The filtered transverse martingale again vanishes uniformly: the raw martingale on `T/f_epsilon` steps is `O_p(epsilon/sqrt(f_epsilon))=o_p(1)`, and Abel summation contributes only the bounded factor

`||T_epsilon-I|| sum_j||T_epsilon^j||=O(1)`.                         (2.23)

This proves (2.8). If `W_0=0`, the initial term is absent and `delta=0` is allowed.

Case (iv) is the already proved R7-01 critical theorem. For (v), the identical martingale-problem proof applies with

`f_epsilon/epsilon^2 ->0`;                                           (2.24)

therefore the forcing drift vanishes while synchronization and the Perron-projected quadratic variation are unchanged. This gives (2.11). QED.

### Proposition 2.2 (exact deterministic crossover curve and its derivative)

Let

`rho=f_epsilon/epsilon >0`                                           (2.25)

be held fixed in the deterministic mean dynamics. Its unique equilibrium is

`z_rho^*=1 pbar+rho(B+rho I)^{-1}Pp`.                               (2.26)

The curve is differentiable and

`d z_rho^*/d rho = B(B+rho I)^{-2}Pp`.                              (2.27)

Moreover

`z_rho^*=1pbar+rho B^{-1}Pp+O(rho^2)` as `rho downarrow0`,           (2.28)

and

`z_rho^*=p-rho^{-1}B Pp+O(rho^{-2})` as `rho to infinity`.           (2.29)

#### Proof

Equation (2.26) is (2.19) with `c` replaced by `rho`. Because `B` commutes with every rational function of itself,

`d/drho [rho(B+rho I)^{-1}]
=(B+rho I)^{-1}-rho(B+rho I)^{-2}
=B(B+rho I)^{-2}`.                                                   (2.30)

The two expansions are the ordinary resolvent expansions at zero and infinity, and `1pbar+Pp=p`. QED.

This derivative gives an exact interpolation between consensus at the Perron-weighted forcing average and direct pinning to the coordinate-wise forcing vector.

---

## 3. B18 — translate the critical limit into the standard Jacobi/Wright–Fisher language

The source asks, informally, whether the continuous-time limit stays away from the extreme points or can touch them repeatedly. For the candidate limit this is a classical one-dimensional boundary-classification question.

Assume now `c>0` and `0<pbar<1`. Define

`a = 2c pbar/kappa`, `b=2c(1-pbar)/kappa`.                           (3.1)

### Theorem 3.1 (Jacobi form, invariant law, and exact boundary thresholds)

The critical limiting generator

`L phi(y)=c(pbar-y)phi'(y)+(kappa/2)y(1-y)phi''(y)`                  (3.2)

is, after the deterministic time change `tau=kappa t`, the standard Wright–Fisher/Jacobi generator

`(1/2)y(1-y)phi''(y)
 +(1/2)[a(1-y)-b y]phi'(y)`.                                         (3.3)

It has the unique invariant law

`Y_infinity ~ Beta(a,b)`,                                            (3.4)

with density proportional to

`y^(a-1)(1-y)^(b-1)`,                                                (3.5)

mean `pbar`, and variance

`Var(Y_infinity)=kappa pbar(1-pbar)/(2c+kappa)`.                     (3.6)

The exact boundary thresholds are:

- `0` is attainable from the interior iff `a<1`, equivalently `2c pbar<kappa`; it is inaccessible iff `a>=1`;
- `1` is attainable from the interior iff `b<1`, equivalently `2c(1-pbar)<kappa`; it is inaccessible iff `b>=1`.

When `0<a,b<infinity`, an attainable endpoint is the standard instantaneously reflecting Wright–Fisher/Jacobi boundary; positive recurrence then implies recurrent returns to every accessible boundary neighborhood, and the regular boundary itself is visited repeatedly in the accessible regime. If `pbar=0` or `1`, irreducibility of `Q` implies respectively `p=0` or `p=1`, and the corresponding endpoint is absorbing.

### Proof

Equation (3.3) follows by dividing (3.2) by `kappa` and observing

`c(pbar-y)/kappa=(1/2)[a(1-y)-by]`.                                 (3.7)

The speed-density calculation gives

`m(y) proportional to [y(1-y)]^{-1}
 exp(int^y 2c(pbar-u)/(kappa u(1-u)) du)`.                            (3.8)

Since

`(pbar-u)/(u(1-u))=pbar/u-(1-pbar)/(1-u)`,                           (3.9)

(3.8) is exactly (3.5). Both exponents exceed `-1`, so this density is normalizable for `a,b>0` and gives the unique invariant law. The Beta mean and variance formulas yield (3.6).

For the boundary test at zero, the scale-density exponent is governed by `a`; Feller's one-dimensional boundary test gives attainability precisely for `a<1`. The symmetric calculation at one gives `b<1`. These are the standard Wright–Fisher-with-mutation boundary thresholds. QED.

### Corollary 3.2 (network topology enters the slow boundary law through one scalar)

For fixed `p`, the slow diffusion sees `Q` only through

`pbar=pi^T p`, `kappa=||pi||_2^2`.                                  (3.10)

Since `pi` is a positive probability vector,

`1/N <= kappa < 1`.                                                   (3.11)

For homogeneous forcing `p=q1`, `pbar=q` for every network. Hence:

- if `c >= 1/[2 min(q,1-q)]`, then both endpoints are inaccessible for every irreducible `Q`;
- if `c < 1/[2N max(q,1-q)]`, then both endpoints are attainable for every irreducible `Q`;
- between these two network-uniform regions, endpoint accessibility can depend on `kappa` and hence on network imbalance;
- the stationary variance `kappa q(1-q)/(2c+kappa)` is strictly increasing in `kappa`, so doubly stochastic networks (`kappa=1/N`) minimize the slow limiting variance among stationary vectors on `N` vertices.

The first two bullets are sufficient uniform statements, not claimed to be mutually sharp in the intermediate region.

---

## 4. B27 — swap the long-time and small-step limits

The source is phrased dynamically. A stronger consistency question is whether one may first run each finite-`epsilon` chain to stationarity and *then* let `epsilon` tend to zero. This also checks that the diffusion limit is not an artifact of taking the small-step limit before long time.

For every `epsilon` with `f_epsilon>0`, the transition kernel on the compact cube `[0,1]^N` is Feller, so at least one invariant probability measure `mu_epsilon` exists. No uniqueness of `mu_epsilon` is assumed below.

### Lemma 4.1 (stationary first and second moment identities)

Under any invariant law `mu_epsilon`,

`E_mu Y=pbar`,                                                       (4.1)

and, with `V_epsilon=Var_mu(Y)`,

`(2f_epsilon-f_epsilon^2)V_epsilon
 = epsilon^2 E_mu[v(Z)]`.                                            (4.2)

Also, if

`m_W=f_epsilon(epsilon B+f_epsilon I)^{-1}Pp`,                       (4.3)

then

`E_mu W=m_W`.                                                        (4.4)

In the regimes `f_epsilon=o(epsilon)` there is a constant `C` independent of the chosen invariant measure such that

`E_mu ||W-m_W||^2 <= C epsilon`.                                     (4.5)

#### Proof

Stationarity in (1.4), followed by expectation, gives (4.1). Centering (1.4) at `pbar`, the conditional cross term vanishes, so

`V_epsilon=(1-f_epsilon)^2V_epsilon+epsilon^2E_mu v(Z)`,             (4.6)

which is (4.2). Taking expectations in (1.5) gives (4.3)–(4.4).

For (4.5), let `U=W-m_W`. Then

`U_{n+1}=T_epsilon U_n+epsilon Pxi_{n+1}`.                           (4.7)

Because `B` is Hurwitz, choose a positive definite quadratic form `M` on `H` and `a>0` so that, for small `epsilon` with `f_epsilon=o(epsilon)`,

`T_epsilon^T M T_epsilon <= (1-a epsilon)M`.                         (4.8)

Using stationarity, boundedness of `xi`, and the zero conditional cross term,

`E U^T M U
 <=(1-aepsilon)E U^T M U+Cepsilon^2`,                         (4.9)

which gives `E||U||^2<=C'epsilon`. QED.

### Theorem 4.2 (stationary phase diagram; no finite-step uniqueness assumption)

Let `mu_epsilon` be *any* invariant law of the finite-`epsilon` chain.

**(a) `0<alpha<1`.** If `f_epsilon~c epsilon^alpha`, then

`mu_epsilon => delta_p`.                                             (4.10)

**(b) `alpha=1`.** If `f_epsilon/epsilon->c`, then

`mu_epsilon => delta_{z_c^*}`,                                      (4.11)

with `z_c^*` from (2.6).

**(c) `1<alpha<2`.** Then

`mu_epsilon => delta_{1pbar}`.                                       (4.12)

**(d) `alpha=2`.** If `f_epsilon/epsilon^2->c in (0,infinity)`, then

`mu_epsilon => Law(1Y)`,                                             (4.13)

where

`Y~Beta(2cpbar/kappa, 2c(1-pbar)/kappa)`                             (4.14)

when `0<pbar<1`, with the obvious degenerate endpoint laws when `pbar=0` or `1`.

**(e) `alpha>2`.** Then

`mu_epsilon => (1-pbar) delta_0vector + pbar delta_1vector`.          (4.15)

Thus in every power-law regime the small-step limit of *every* invariant law is unique, even though no uniqueness theorem for the prelimit invariant measure was used.

### Proof

For `alpha<2`, the deterministic contraction time is faster than the accumulated noise at equilibrium. More explicitly, in cases (a) and (b) the full deterministic matrix has contraction rate comparable respectively to `f_epsilon` and `epsilon`; the one-step noise is `O(epsilon)`, so stationary quadratic fluctuations are bounded by `O(epsilon^2/f_epsilon)` in (a) and `O(epsilon)` in (b). Their stationary means solve the exact deterministic balance equation and are respectively asymptotic to `p` and equal asymptotically to `z_c^*`. This proves (4.10)–(4.11).

For (c), (4.2) gives

`V_epsilon <= C epsilon^2/f_epsilon ->0`.                            (4.16)

Also (4.3) gives `m_W=O(f_epsilon/epsilon)->0`, while (4.5) gives `W->0` in `L^2`. Together with `EY=pbar`, this proves (4.12).

For (d), (4.3)–(4.5) again give `W->0` in `L^2`. Hence

`v(Z)-kappa Y(1-Y) ->0` in `L^1`.                                   (4.17)

The exact identity (4.2) already yields the limiting stationary variance. Indeed, if `V` is any subsequential limit,

`V=(kappa/(2c))[pbar(1-pbar)-V]`,                                   (4.18)

so

`V=kappa pbar(1-pbar)/(2c+kappa)`,                                  (4.19)

matching (3.6).

To identify the whole law, let `phi in C^3([0,1])`. Stationarity gives

`0=E_mu[phi(Y_{n+1})-phi(Y_n)]`.                                    (4.20)

Taylor-expand with

`Delta Y=f_epsilon(pbar-Y)+epsilon eta`.                             (4.21)

Divide by `epsilon^2`. The first-order term tends to

`c E[(pbar-Y)phi'(Y)]`.                                              (4.22)

The conditional second-order term tends, using (4.17), to

`(kappa/2)E[Y(1-Y)phi''(Y)]`.                                       (4.23)

The `f_epsilon^2` part of `E[(Delta Y)^2|F]` is `o(epsilon^2)`, and since `|Delta Y|<=Cepsilon`, the third-order Taylor remainder divided by `epsilon^2` is `O(epsilon)`. Therefore every subsequential scalar limit `nu` satisfies

`int [c(pbar-y)phi'(y)+(kappa/2)y(1-y)phi''(y)] nu(dy)=0`.           (4.24)

The Jacobi diffusion has the unique invariant Beta law (3.4), so every subsequence has the same limit. Since `W->0`, (4.13) follows.

For (e), (4.3)–(4.5) still imply `W->0`, because `f_epsilon=o(epsilon)`. From (4.2),

`E_mu v(Z)
 = [(2f_epsilon-f_epsilon^2)/epsilon^2]V_epsilon ->0`.               (4.25)

Together with `W->0`, this gives

`E[kappa Y(1-Y)] ->0`.                                               (4.26)

Thus every scalar subsequential limit is supported on `{0,1}`. Equation (4.1) fixes its mean to `pbar`, so it must be

`(1-pbar)delta_0+pbar delta_1`.                                      (4.27)

Again `W->0`, giving (4.15). QED.

### Corollary 4.3 (commutation of limits at the source-critical scale)

When `f_epsilon/epsilon^2->c in (0,infinity)` and `0<pbar<1`, taking long time first and small step second gives the same Beta consensus law as taking the R7-01 diffusion limit first and then letting the limiting Jacobi diffusion reach stationarity:

`lim_{epsilon->0} (any invariant law of Z^epsilon)
 = Law(1Y_infinity)`                                                 (4.28)

with `Y_infinity` given by (3.4).

This is a quantifier swap not used in the source-level diffusion proof and supplies an independent structural consistency check.

---

## 5. What moved mathematically and what did not

The frozen source metric is still

`M_clause(P0087)=2/2`.                                                (5.1)

It cannot increase without redefining the owner-approved source metric, so this run is formally **NO MOVEMENT** on that metric. The new mathematics is nevertheless substantive:

1. the exact two-threshold forcing phase diagram (`alpha=1`, `alpha=2`) is proved;
2. the source-critical limiting process is identified explicitly as a Jacobi/Wright–Fisher diffusion with Beta stationary law and exact endpoint thresholds;
3. every finite-step invariant law has a unique small-step limit in all five power-law regimes, without assuming finite-step uniqueness;
4. at the critical scale, the long-time and small-step limits commute at the level of invariant laws.

These strengthen and stress-test the candidate source-level solution but do not substitute for the independent P26 audit, the distinct OTHER-track audit, final prior-art reconciliation, and self-contained paper package required for operational closure.

## 6. Literature boundary checked on 2026-09-18

The primary Open Problem 16 source itself contains the scalar frozen-input Wright–Fisher heuristic and then asks for a proper continuous-time limit of the forced **network** process, writing a singular interacting-Wright–Fisher expression whose meaning/asymptotics are left open.

The closest recovered prior work remains:

- Aletti–Crimaldi (2021), *The Rescaled Pólya Urn and the Wright–Fisher Process with Mutation*, which proves a Wright–Fisher-with-mutation limit for the scalar rescaled urn;
- Aletti–Crimaldi–Ghiglietti (2017), the parent network synchronization model;
- Aletti–Crimaldi–Ghiglietti (2024), *Networks of reinforced stochastic processes: A complete description of the first-order asymptotics*, which studies another network asymptotic regime;
- the standard Jacobi/Wright–Fisher boundary and stationary-density theory, which supplies the interpretation in Section 3 once the R7-01 limit SDE has been proved.

A bounded search on 2026-09-18 did not surface a later paper proving the exact forced-network `f_epsilon ~ c epsilon^2` limit, the five-regime phase diagram above, or the stationary-limit commutation theorem. This is negative evidence only and is **not** a novelty or worldwide-openness certificate.

## 7. Remaining gaps and next nonrepeating attacks

No new source clause remains mathematically unresolved in the cumulative candidate proof, but operational closure remains incomplete. The most useful next mathematical stress tests are nonrepeating methods **B3 / B12 / B29**:

- **B3 (prove something stronger):** state and prove one uniform singular-perturbation theorem parameterized by `rho_epsilon=f_epsilon/epsilon` and `lambda_epsilon=f_epsilon/epsilon^2`, with quantitative error bounds that specialize to all five regimes.
- **B12 (find what is conserved):** derive all exact prelimit stationary moment identities that survive the Perron projection and determine whether they characterize additional finite-`epsilon` structure beyond the first two moments.
- **B29 (add the points at infinity):** incorporate `c=0`, `c=infinity`, `pbar in {0,1}`, and boundary initial data into one compactified Jacobi parameter space so there is no hidden endpoint exception in the source-level statement.

If the frozen metric remains unchanged on the next ordinary research iteration, its ordinary unchanged count reaches three and the following R7-01 run must be the owner-required thinking-only stuck diagnosis.