Model actually running: GPT-5.6 Sol. Reasoning level: UNVERIFIED — this is not GPT-6 at maximum; no authenticated runtime model/effort telemetry or binding selector is exposed.

# P0087: exact contraction, a closed stationary covariance hierarchy, and the compactified forcing boundary

Date: 2026-09-18.  
Worker: R7-01 (`6aabe777361481919c9e614646464772`).  
Source: G. Aletti et al., *Open Problems in Stochastic Reinforcement Models* (2025), Open Problem 16, printed pp. 14–16.  
Methods in this artifact: **B3 / B12 / B29**.  
Status: **PARTIAL operationally**. The cumulative R7-01 record already contains a candidate source-level proof of both source clauses. The frozen metric remains `M_clause(P0087)=2/2`; this artifact supplies new finite-step and endpoint structure but does not redefine that metric.

## 1. Setup recovered from the cumulative proof

Write

`epsilon=r_r`, `f=f_epsilon=r_f`, `Q=A^T`.

Under the source hypotheses, `Q` is a fixed irreducible row-stochastic `N x N` matrix, `p in [0,1]^N`, and, conditional on `F_n`, the coordinates of the binary action vector are independent with

`E[X_{n+1}|F_n]=Q Z_n`.

The exact recursion is

`Z_{n+1}=(1-epsilon-f)Z_n+epsilon X_{n+1}+f p`.             (1.1)

Let `pi` be the unique strictly positive stationary probability vector,

`pi^T Q=pi^T`, `pi^T 1=1`,

and put

`Y=pi^T Z`, `pbar=pi^T p`, `kappa=sum_j pi_j^2`,
`P=I-1 pi^T`, `W=PZ`, `H={w:pi^T w=0}`,
`B=(I-Q)|_H`.

The cumulative critical theorem is that when `f/epsilon^2 -> c in [0,infinity)` and after the `epsilon^{-1}` synchronization layer,

`Z_floor(t/epsilon^2) => 1 Y_t`,

where

`dY_t=c(pbar-Y_t)dt+sqrt(kappa Y_t(1-Y_t))dB_t`.            (1.2)

The present run asks for structure that is exact before taking the limit.

---

## 2. B3 — exact Wasserstein contraction and a single finite-step mean semigroup

The useful idea is to couple two copies by the same uniforms rather than estimate the stochastic approximation one regime at a time.

Define the weighted `l^1` norm

`||x||_(1,pi)=sum_j pi_j |x_j|`.

### Theorem 2.1 (exact one-step contraction)

Assume `epsilon>=0`, `f>0`, and `epsilon+f<=1`. Let `K_{epsilon,f}` be the Markov kernel of (1.1). Then for all states `z,z' in [0,1]^N`,

`W_(1,pi)(delta_z K,delta_z' K) <= (1-f)||z-z'||_(1,pi)`.   (2.1)

Consequently, for arbitrary probability laws `mu,nu`,

`W_(1,pi)(mu K^n,nu K^n) <= (1-f)^n W_(1,pi)(mu,nu)`.        (2.2)

In particular, for every finite `epsilon` and every `f>0`, the chain has a **unique invariant probability law** `mu_{epsilon,f}`, and every initial law converges to it exponentially in this Wasserstein distance.

#### Proof

For each coordinate choose independent `U_j~Unif[0,1]` and, for two starting states `z,z'`, define the monotone common-uniform coupling

`X_j=1{U_j <= (Qz)_j}`,
`X'_j=1{U_j <= (Qz')_j}`.

Then

`E|X_j-X'_j|=|(Qz)_j-(Qz')_j|`.

Writing `d=z-z'`, stationarity of `pi` and positivity of `Q` imply

`E||X-X'||_(1,pi)
 =sum_j pi_j |(Qd)_j|
 <=sum_j pi_j sum_k Q_jk |d_k|
 =sum_k pi_k |d_k|
 =||d||_(1,pi)`.                                           (2.3)

The forcing vector cancels between the two updates, so

`Z_1-Z'_1=(1-epsilon-f)d+epsilon(X-X')`.

Because all coefficients are nonnegative,

`E||Z_1-Z'_1||_(1,pi)
 <=(1-epsilon-f)||d||_(1,pi)+epsilon E||X-X'||_(1,pi)
 <=(1-f)||d||_(1,pi)`.                                     (2.4)

This proves (2.1); gluing the one-step couplings proves (2.2). The space of probability measures on compact `[0,1]^N` is complete in `W_1`. Since the pushforward `mu -> mu K` is a strict contraction when `f>0`, Banach's fixed-point theorem gives a unique invariant law and (2.2) gives convergence to it. QED.

This closes a finite-step gap deliberately left open in the previous run, which had formulated stationary limits for arbitrary invariant measures rather than assume uniqueness.

### Proposition 2.2 (exact finite-step mean solution)

Let

`S=(1-epsilon-f)I+epsilon Q=I-fI-epsilon(I-Q)`.             (2.5)

For `f>0`, the unique stationary mean `m=E_{mu_{epsilon,f}} Z` is

`m=1 pbar + rho(B+rho I)^(-1)Pp`, `rho=f/epsilon`,            (2.6)

with the evident `epsilon=0` interpretation `m=p`. Moreover, for every deterministic initial state,

`E_z Z_n-m=S^n(z-m)`.                                        (2.7)

Equivalently,

`pi^T E_z Z_n-pbar=(1-f)^n(pi^T z-pbar)`,                    (2.8)

and on the transverse space

`P E_z Z_n-m_W=T^n(Pz-m_W)`,                                 (2.9)

where

`T=I-epsilon B-fI`, `m_W=rho(B+rho I)^(-1)Pp`.               (2.10)

#### Proof

Taking conditional expectations in (1.1) gives `E[Z_{n+1}|Z_n]=SZ_n+fp`. The invariant mean therefore satisfies

`[epsilon(I-Q)+fI]m=fp`.                                     (2.11)

Multiplication by `pi^T` yields `pi^T m=pbar`. Projecting (2.11) to `H` yields

`(epsilon B+fI)m_W=fPp`,                                     (2.12)

which is (2.6). Subtracting the invariant mean from the expectation recursion gives (2.7); (2.8) and (2.9) are its Perron and transverse projections. QED.

Equations (2.6)–(2.10) are a single exact finite-step skeleton behind the five power-law regimes from the previous run. They are uniform in the two ratios `rho=f/epsilon` and `lambda=f/epsilon^2`. What B3 does **not** yet give is one path-space error theorem uniform across both crossover surfaces; near `rho~1` and `lambda~1`, the natural time parametrization itself changes. That is a genuine limitation of this method, not hidden as a proof claim.

---

## 3. B12 — an exact stationary polynomial hierarchy

The next idea is to ask what is conserved algebraically by stationarity before taking `epsilon -> 0`.

Let

`xi_{n+1}=X_{n+1}-QZ_n`.

Then `E[xi_{n+1}|F_n]=0`, and conditional independence gives

`E[xi xi^T|Z]=D(QZ)`,
`D(r)=diag(r_j(1-r_j))`.                                     (3.1)

### Theorem 3.1 (closed exact covariance equation)

Let `m` be (2.6) and let

`C=E_mu[(Z-m)(Z-m)^T]`, `qbar=Qm`.

Then the invariant covariance is characterized by the exact linear matrix equation

`C-SCS^T+epsilon^2 Diag(diag(QCQ^T))
 =epsilon^2 Diag(qbar o (1-qbar))`,                          (3.2)

where `o` denotes coordinatewise product.

#### Proof

Centering at the exact invariant mean gives

`Z_{n+1}-m=S(Z_n-m)+epsilon xi_{n+1}`.                       (3.3)

The cross terms vanish after expectation because `E[xi|Z]=0`, so stationarity gives

`C=SCS^T+epsilon^2 E D(QZ)`.                                 (3.4)

For each coordinate,

`E[(QZ)_j(1-(QZ)_j)]
 =qbar_j(1-qbar_j)-Var((QZ)_j)
 =qbar_j(1-qbar_j)-(QCQ^T)_{jj}`.                            (3.5)

Substitution of (3.5) into (3.4) is exactly (3.2). QED.

This is finite-dimensional and exact; no diffusion approximation appears.

### Proposition 3.2 (all polynomial moments close by degree)

For every integer `k>=1`, the stationary moments `E[Z^alpha]`, `|alpha|<=k`, satisfy a finite linear system involving no moment of degree larger than `k`.

#### Proof

Each coordinate of the update is affine in `(Z,X)`. Expanding any monomial of total degree at most `k` therefore gives a finite sum of terms `Z^a X^b` of total degree at most `k`. Since `X_j in {0,1}`, powers of a given `X_j` collapse to `X_j`. Conditional independence yields

`E[prod_{j in J}X_j | Z]=prod_{j in J}(QZ)_j`,               (3.6)

which is a polynomial in `Z` of degree `|J|`. Hence conditional expectation of every degree-`k` update monomial is a polynomial in `Z` of degree at most `k`; stationarity closes the hierarchy degree by degree. QED.

This does not magically provide a simple closed-form `N`-dimensional density, but it gives an exact finite algebraic route to any prescribed stationary moment. Uniqueness of the actual stationary moment vector follows from Theorem 2.1 because the invariant law itself is unique; I do not claim that every formal solution of every truncated linear system is probabilistically realizable.

---

## 4. B12 continued — a single stationary variance formula across the synchronized forcing regimes

Assume now

`epsilon -> 0`, `f>0`, `rho=f/epsilon ->0`.                  (4.1)

The second ratio

`lambda=f/epsilon^2`                                         (4.2)

is allowed to tend to zero, a finite positive number, or infinity.

Let the stationary centered variables be

`y=Y-pbar`, `w=W-m_W`,

and write

`V=E[y^2]`, `G=E[ww^T]`, `H=E[yw^T]`.

### Lemma 4.1 (transverse second moments)

There is a constant depending only on the fixed irreducible matrix `Q` such that, uniformly under (4.1),

`||G||=O(epsilon)`, `||H||=O(epsilon)`, `||m_W||=O(rho)`.     (4.3)

#### Proof

The centered transverse recursion is

`w'=Tw+epsilon Pxi`, `T=I-epsilon B-fI`.                     (4.4)

Since all eigenvalues of `B` have positive real part, there is a fixed equivalent norm and constants `C,a>0` such that

`||T^n|| <= C exp[-a epsilon n]`                              (4.5)

for all sufficiently small `epsilon` when `rho->0`. The stationary covariance equation is

`G=TGT^T+epsilon^2 P E[D(QZ)]P^T`.                            (4.6)

Because `0<=D(QZ)<=I/4` coordinatewise, iteration of (4.6) and (4.5) gives

`||G|| <= C epsilon^2 sum_{n>=0}exp(-2a epsilon n)=O(epsilon)`.

Similarly, using

`y'=(1-f)y+epsilon eta`, `eta=pi^T xi`,                       (4.7)

we get

`H=(1-f)HT^T+epsilon^2 E[eta(Pxi)^T]`.                       (4.8)

The forcing on the right is uniformly `O(epsilon^2)`, while the inverse geometric resolvent has norm `O(epsilon^{-1})`, giving `H=O(epsilon)`. Finally (2.10) and boundedness of `(B+rho I)^(-1)` for small `rho` give `m_W=O(rho)`. QED.

### Lemma 4.2 (quadratic variation reduction with an error rate)

For

`v(Z)=E[eta^2|Z]=sum_j pi_j^2 (QZ)_j(1-(QZ)_j)`,              (4.9)

one has

`E v(Z)=kappa[pbar(1-pbar)-V]+O(epsilon+rho)`.                (4.10)

#### Proof

Write `QZ=1Y+QW` and `a_j=(QW)_j`. Exactly,

`(QZ)_j(1-(QZ)_j)=Y(1-Y)+a_j(1-2Y)-a_j^2`.                  (4.11)

After weighting by `pi_j^2` and taking expectations, the first term is

`kappa E[Y(1-Y)]=kappa[pbar(1-pbar)-V]`.                     (4.12)

For the linear term, split `W=m_W+w` and `Y=pbar+y`. Its expectation is the sum of a deterministic contribution `O(||m_W||)=O(rho)` and a cross-covariance contribution controlled by `H=O(epsilon)`. The quadratic term is `O(E||W||^2)=O(epsilon+rho^2)`. This proves (4.10). QED.

### Theorem 4.3 (uniform stationary Perron-variance crossover)

Under (4.1), the unique finite-step invariant law satisfies

`[kappa+2lambda-lambda f] V
 =kappa pbar(1-pbar)+O(epsilon+rho)`.                          (4.13)

Equivalently,

`V={kappa pbar(1-pbar)+O(epsilon+rho)
    \over kappa+2lambda-lambda f}`.                          (4.14)

Hence:

1. if `lambda->0`, then
   `V->pbar(1-pbar)`;
2. if `lambda->c in (0,infinity)`, then
   `V->kappa pbar(1-pbar)/(kappa+2c)`;
3. if `lambda->infinity`, then
   `V->0`.

In particular, at the source-critical scaling `f=c epsilon^2`,

`Var_mu(Y)=kappa pbar(1-pbar)/(kappa+2c)+O(epsilon)`.          (4.15)

#### Proof

From (4.7), stationarity and conditional mean zero of `eta` give the exact scalar variance identity

`(2f-f^2)V=epsilon^2 E v(Z)`.                                (4.16)

Divide by `epsilon^2`; since `lambda=f/epsilon^2`,

`(2lambda-lambda f)V=E v(Z)`.                                (4.17)

Insert Lemma 4.2 and move the `kappa V` term to the left. This proves (4.13)–(4.14). In the critical case `rho=c epsilon`, so the numerator error is `O(epsilon)` and the denominator stays bounded away from zero, proving (4.15). QED.

This one formula recovers the stationary second-moment part of the previous three synchronized regimes without proving them separately. It also gives a quantitative `O(epsilon)` critical second-moment error not present in the earlier weak-limit theorem.

At `lambda->0`, the limiting variance is the **maximal possible variance on `[0,1]` with mean `pbar`**. Therefore every stationary subsequential limit must be supported on `{0,1}`, and the mean fixes it as `(1-pbar)delta_0+pbar delta_1`. At `lambda->infinity`, the variance vanishes, so the Perron coordinate concentrates at `pbar`.

---

## 5. B29 — compactify the Jacobi parameter and remove hidden endpoint conventions

The critical limiting family from (1.2) is

`dY=c(pbar-Y)dt+sqrt(kappa Y(1-Y))dB`,                       (5.1)

with `c>=0`. For `c>0` and `0<pbar<1`, set

`a=2c pbar/kappa`, `b=2c(1-pbar)/kappa`.                     (5.2)

The previous run identified its invariant law as `Beta(a,b)`. The endpoint cases can be included cleanly as follows.

### Theorem 5.1 (compactified slow family)

Fix `0<pbar<1` and `kappa>0`.

**Finite positive `c`.** The diffusion (5.1) has the unique invariant law

`nu_c=Beta(2c pbar/kappa, 2c(1-pbar)/kappa)`.                 (5.3)

The endpoint `0` is attainable from the interior iff `a<1`, and endpoint `1` is attainable iff `b<1`. Under the canonical Jacobi solution, an attainable endpoint with positive inward mutation is instantaneously reflecting rather than absorbing; for `a>=1` (respectively `b>=1`) that endpoint is inaccessible from the interior.

**The edge `c=0`.** Equation (5.1) becomes neutral Wright–Fisher diffusion. Both endpoints are absorbing, and from initial value `y` its long-time law is

`(1-y)delta_0+y delta_1`.                                     (5.4)

The invariant laws are precisely the probability measures supported on `{0,1}`. The family (5.3) has the selected weak limit

`nu_c => (1-pbar)delta_0+pbar delta_1` as `c downarrow0`.      (5.5)

**The edge `c=infinity`.** This is not a finite SDE coefficient on the `epsilon^{-2}` clock. In the synchronized regime `rho=f/epsilon->0`, if `lambda=f/epsilon^2->infinity`, one instead uses forcing time `t=fn`. Then martingale variance over unit forcing time is of order `epsilon^2/f=lambda^{-1}->0`, while synchronization has already occurred, and the Perron coordinate converges to

`dy/dt=pbar-y`.                                                (5.6)

Thus the stationary selection is

`nu_infinity=delta_pbar`.                                     (5.7)

The invariant variances fit one continuous compactified formula,

`Var(nu_c)=kappa pbar(1-pbar)/(kappa+2c)`,                    (5.8)

where the right side is interpreted by continuity as `pbar(1-pbar)` at `c=0` and `0` at `c=infinity`.

#### Proof

The finite-`c` statements are the standard one-dimensional scale/speed calculation for the Jacobi generator already derived in the previous run. For `c=0`, the process is a bounded martingale absorbed at `0` or `1`; optional stopping fixes the probability of eventual absorption at `1` to be the starting value `y`, giving (5.4). The only invariant mass can therefore lie on the absorbing set. The weak limit (5.5) follows, for example, from the Beta first moment `pbar` and variance tending to `pbar(1-pbar)`, which forces any weak limit with support `[0,1]` onto the two endpoints with those weights.

For `c=infinity`, use the exact scalar recursion

`Y_{n+1}-Y_n=f(pbar-Y_n)+epsilon eta_{n+1}`.                  (5.9)

Over `O(f^{-1})` steps the martingale quadratic variation is `O(epsilon^2/f)=O(lambda^{-1})`, hence vanishes; the Euler drift converges to (5.6). The stationary concentration also follows directly from Theorem 4.3. Equation (5.8) is the Beta variance for finite positive `c`, together with its two limits. QED.

### Proposition 5.2 (degenerate forcing averages)

If `pbar=0`, positivity of the stationary vector `pi` and `p in [0,1]^N` force `p=0`. Then `0` is absorbing and, for `c>0`,

`E_y Y_t=y e^{-ct}`,

so `Y_t->0` in `L^1`; the unique invariant law is `delta_0`. The case `pbar=1` is symmetric, with invariant law `delta_1`.

#### Proof

If `sum_j pi_j p_j=0` with all `pi_j>0` and all `p_j>=0`, every `p_j=0`. Taking expectations in (5.1) gives `dE Y_t/dt=-cE Y_t`, proving the first statement. The other endpoint is obtained by replacing `Y` with `1-Y`. QED.

A qualification matters at the `c=infinity` face: if `rho=f/epsilon` does **not** tend to zero, the network has not synchronized before forcing acts. Then the scalar Jacobi compactification branches into the `rho~1` or `rho->infinity` deterministic vector regimes from the preceding phase diagram. I therefore do not identify those different faces with (5.6).

---

## 6. What moved mathematically, and what did not

Frozen source metric:

`M_clause(P0087): 2 -> 2 (NO MOVEMENT)`.                      (6.1)

The metric is already saturated and cannot be increased honestly. The new mathematical content is instead:

1. an exact finite-step Wasserstein contraction coefficient `1-f`, proving uniqueness and exponential attraction of the invariant law whenever forcing is positive;
2. an exact closed covariance equation and degree-by-degree polynomial stationary hierarchy;
3. a single stationary variance crossover formula uniform for `rho->0` and arbitrary `lambda=f/epsilon^2`, including an `O(epsilon)` critical variance error;
4. a clean compactification of the slow Jacobi family at `c=0`, `c=infinity`, `pbar=0,1`, with the relevant time-scale warning at `c=infinity`.

The precise remaining limitations are:

- B3 did not produce one path-space approximation theorem uniform across both crossover surfaces; the natural clock changes there.
- B12 does not provide a closed-form joint invariant density for general `N`; it provides exact finite moment equations and the fully explicit Perron second-moment asymptotics above.
- B29's `c=infinity` edge is a forcing-time deterministic limit only in the synchronized face `f/epsilon->0`.
- worldwide novelty/current openness cannot be certified from bounded searching.
- operational closure still requires the owner-mandated independent P26 audit, one distinct OTHER-track audit, final prior-art reconciliation, and a self-contained source-scoped paper package.

This is the **third consecutive ordinary research run with the already saturated frozen metric unchanged**. Under the owner protocol, the next R7-01 run must therefore be the prescribed **thinking-only stuck diagnosis**, not another ordinary theorem/checker run.

## 7. Dated literature boundary

On 2026-09-18 the current primary source remains Aletti et al., *Open Problems in Stochastic Reinforcement Models*, DOI `10.1007/978-3-031-76738-8_29`. Its Open Problem 16 explicitly leaves the forced-network time-rescaled dynamics/asymptotics unknown.

The closest recovered prior work remains:

- Aletti–Crimaldi (2021), *The Rescaled Pólya Urn and the Wright–Fisher Process with Mutation*, which treats the scalar rescaled urn and obtains the Wright–Fisher-with-mutation limit;
- Aletti–Crimaldi–Ghiglietti (2024), *Networks of reinforced stochastic processes: A complete description of the first-order asymptotics*, SPA 176, 104427, which studies first-order synchronization regimes for the network model but not this forced `f~c epsilon^2` limit;
- the authors' 2026 publication lists contain later work on interacting innovation models/CLTs, but the bounded search did not locate a theorem matching the exact Open Problem 16 forced-network scaling.

That last statement is negative evidence only. Novelty and worldwide openness remain **UNVERIFIED**.
