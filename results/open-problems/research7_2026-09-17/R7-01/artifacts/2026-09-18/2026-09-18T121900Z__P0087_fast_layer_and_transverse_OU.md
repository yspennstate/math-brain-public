Model actually running: GPT-5.6 Sol. Reasoning level: UNVERIFIED — this is not GPT-6 at maximum; no authenticated runtime reasoning-effort telemetry or binding selector is exposed.

# P0087: the initial synchronization layer and its transverse Ornstein–Uhlenbeck fluctuation

Date: 2026-09-18.  
Worker: R7-01 (`6aabe777361481919c9e614646464772`).  
Source target: Aletti et al., *Open Problems in Stochastic Reinforcement Models*, Open Problem 16, printed pp. 14–16.  
Status: **PARTIAL operationally**. The preceding R7-01 artifact gives a candidate source-level proof of both clauses of Open Problem 16. The present artifact stress-tests and strengthens the singular-limit clause; it does not count as an independent audit and does not change the frozen source metric `M_clause=2`.

## 1. Model and notation

Let `Q` be a nonnegative irreducible row-stochastic `N x N` matrix. Let `pi` be its unique positive stationary probability vector:

`pi^T Q = pi^T`, `pi^T 1 = 1`.

The forced network process is

`Z_{n+1}^e = Z_n^e + e(Q-I)Z_n^e + f_e(p-Z_n^e) + e xi_{n+1}^e`,       (1.1)

where, conditionally on `F_n`, the coordinates of `X_{n+1}^e` are independent Bernoulli variables with mean vector `QZ_n^e`, and

`xi_{n+1}^e = X_{n+1}^e-QZ_n^e`.

Assume throughout that `e -> 0` and `f_e/e^2 -> c in [0,infinity)`. Define

`Y_n^e = pi^T Z_n^e`, `pbar=pi^T p`,

`P = I-1 pi^T`, `W_n^e=PZ_n^e=Z_n^e-1Y_n^e`,

`H={w: pi^T w=0}`, `B=(I-Q)|_H`.

The preceding artifact proved the slow diffusion theorem on time `n~e^{-2}`. Here the purpose is to resolve the vanishing-width synchronization layer and identify its next-order fluctuations.

Because `Q` is irreducible, eigenvalue `1` is simple and every other eigenvalue `lambda` satisfies `Re(lambda)<1`. Hence all eigenvalues of `B` lie in the open right half-plane. No reversibility, aperiodicity, or diagonalizability is assumed.

The exact projected recursions are

`Y_{n+1}^e-Y_n^e = f_e(pbar-Y_n^e)+e eta_{n+1}^e`,                    (1.2)

`eta_{n+1}^e=pi^T xi_{n+1}^e`,

and

`W_{n+1}^e = T_e W_n^e+f_ePp+ePxi_{n+1}^e`,                         (1.3)

with

`T_e=I-eB-f_eI` on `H`.                                               (1.4)

The conditional covariance of the noise is

`E[xi_{n+1}^e (xi_{n+1}^e)^T|F_n]
 = D(QZ_n^e)`,                                                        (1.5)

where `D(q)=diag(q_j(1-q_j))`. Conditional independence is used exactly here.

---

## 2. B6 — deform to the solvable fast time scale

The slow theorem says that arbitrary nonsynchronized initial conditions create an initial layer. The natural deformation is to zoom into that layer with

`s=e n`, rather than `t=e^2 n`.

### Theorem 2.1 (deterministic fast synchronization layer)

Assume `Z_0^e -> z_0 in [0,1]^N`. Put

`y_0=pi^T z_0`, `w_0=z_0-1y_0`.

For `s>=0` set

`Zhat^e(s)=Z^e_{floor(s/e)}`.

Then, for every finite `S`,

`sup_{0<=s<=S} |pi^T Zhat^e(s)-y_0| -> 0`                            (2.1)

in probability, and

`sup_{0<=s<=S} ||PZhat^e(s)-exp(-sB)w_0|| -> 0`                      (2.2)

in probability. Consequently

`Zhat^e(s) -> 1y_0+exp(-sB)w_0`                                     (2.3)

uniformly on compact fast-time intervals in probability.

In particular, as `s->infinity`, the deterministic layer converges to the consensus point `1y_0`. On the original slow scale this entire motion is compressed into time zero.

### Proof

#### Step 1: the Perron coordinate is frozen on fast time

From (1.2), for `m<=S/e`,

`Y_m^e-Y_0^e = sum_{k<m} f_e(pbar-Y_k^e)
              + e sum_{k<m} eta_{k+1}^e`.                            (2.4)

The deterministic term is at most

`m f_e <= S f_e/e = O(e)`.                                          (2.5)

The martingale increments are uniformly bounded. Therefore

`E[(e sum_{k<m} eta_{k+1}^e)^2] <= C e^2 m <= C_S e`.                (2.6)

Doob's maximal inequality gives

`E max_{m<=S/e}|e sum_{k<m}eta_{k+1}^e|^2 <= C_S e`.                 (2.7)

Together with `Y_0^e->y_0`, this proves (2.1).

#### Step 2: deterministic transverse evolution

Iterating (1.3),

`W_m^e = T_e^mW_0^e
 + f_e sum_{k=0}^{m-1}T_e^kPp
 + e sum_{k=1}^m T_e^{m-k}Pxi_k^e`.                                  (2.8)

Since the spectrum of `B` lies in the open right half-plane, there are `C,a>0` such that for all sufficiently small `e`,

`||T_e^k||_H <= C exp(-ae k)`.                                      (2.9)

The forcing term is bounded uniformly by

`C f_e sum_{k>=0} exp(-ae k) <= C f_e/e = O(e)`.                     (2.10)

Moreover, uniformly for `s in [0,S]`,

`T_e^{floor(s/e)} -> exp(-sB)`.                                     (2.11)

Indeed `T_e=I-eB+o(e)` because `f_e/e->0`; the standard finite-dimensional Euler-product limit gives (2.11), including for non-diagonalizable `B`.

#### Step 3: the stochastic convolution vanishes uniformly

Define the raw martingale

`M_m=e sum_{k=1}^m Pxi_k^e`.

Then

`E max_{m<=S/e}||M_m||^2 <= C_S e`                                  (2.12)

by Doob. Abel summation rewrites the convolution in (2.8) as

`sum_{k=1}^m T_e^{m-k}(M_k-M_{k-1})
 = M_m +(T_e-I) sum_{k=1}^{m-1}T_e^{m-1-k}M_k`.                      (2.13)

By (2.9), `||T_e-I||=O(e)` and `sum_j||T_e^j||=O(e^{-1})`. Hence

`max_{m<=S/e}||e sum_{k=1}^mT_e^{m-k}Pxi_k^e||
 <= C max_{m<=S/e}||M_m|| ->0`                                      (2.14)

in probability. Combining (2.8)–(2.14) proves (2.2), hence (2.3). QED.

### Interpretation

The initial-layer endpoint depends on the initial condition only through the Perron average `y_0`. The full network matrix controls only the shape of the fast transient `exp(-sB)w_0`. This makes the slow theorem's time-zero caveat exact rather than qualitative.

---

## 3. B15 — break symmetry: defective and periodic exact stress tests

The preceding proof uses only irreducibility. To test whether diagonalizability, reversibility, or aperiodicity has been smuggled in, consider two deliberately hostile networks.

### 3.1 A defective irreducible network

Let

`Q_d = [[1/2,1/2,0],
        [0,1/2,1/2],
        [1/8,3/8,1/2]]`.                                             (3.1)

This matrix is nonnegative, row-stochastic and irreducible. Its stationary probability vector is

`pi_d=(1,4,4)/9`,                                                     (3.2)

so

`kappa_d=sum pi_j^2=11/27`.                                          (3.3)

Its characteristic polynomial is

`(lambda-1)(lambda-1/4)^2`.                                         (3.4)

Furthermore

`rank(Q_d-(1/4)I)=2`.                                                (3.5)

Thus the eigenvalue `1/4` has algebraic multiplicity two and geometric multiplicity one: `Q_d` is not diagonalizable. On `H`, `B_d=I-Q_d` has a size-two Jordan block at eigenvalue `3/4`, so the fast layer includes a polynomial-times-exponential factor. Theorem 2.1 still applies unchanged because the semigroup is exponentially stable.

### 3.2 A period-three network

Let

`Q_p=[[0,1,0],[0,0,1],[1,0,0]]`.                                    (3.6)

Then `Q_p^3=I`, so the chain has period three and the non-Perron eigenvalues lie on the unit circle. Nevertheless they are `exp(+-2pi i/3)`, hence the corresponding eigenvalues of `B_p=I-Q_p` have real part `3/2`. Thus the fast layer decays exponentially. Here

`pi_p=(1,1,1)/3`, `kappa_p=1/3`.                                    (3.7)

These two examples show that neither an aperiodicity assumption nor diagonalizability is needed for the singular synchronization mechanism.

---

## 4. B21 — import the fast-slow / stochastic-averaging viewpoint

The deterministic layer has fluctuations of order `sqrt(e)`. Once the process begins within `sqrt(e)` of the consensus manifold, those fluctuations have a nontrivial fast limit.

### Theorem 4.1 (transverse fast Ornstein–Uhlenbeck limit)

Fix `y in (0,1)`. Assume

`Z_0^e = y1+sqrt(e) v_0^e`,

where `v_0^e in H`, `v_0^e -> v_0`, and `Z_0^e in [0,1]^N`. Define

`V^e(s)=e^{-1/2} W^e_{floor(s/e)}`.                                  (4.1)

Then for every finite `S`,

`(Y^e_{floor(s/e)},V^e(s)) => (y,V_s)`                               (4.2)

in `D([0,S],R x H)`, where `V` is the unique solution of

`dV_s = -B V_s ds + sqrt(y(1-y)) P dB_s^(N)`,
`V_0=v_0`.                                                           (4.3)

Here `B_s^(N)` is standard `N`-dimensional Brownian motion. The diffusion coefficient is allowed to be singular; its range is exactly transverse to `pi` because `pi^TP=0`.

### Proof

From Theorem 2.1, or directly from (2.4)–(2.7),

`sup_{s<=S}|Y^e_{floor(s/e)}-y| ->0`                                 (4.4)

in probability.

Divide (1.3) by `sqrt(e)`. At step `k`,

`V_{k+1}^e-V_k^e
 = -e B V_k^e - f_eV_k^e
   + f_e e^{-1/2}Pp
   + sqrt(e) Pxi_{k+1}^e`.                                           (4.5)

Over `O(e^{-1})` fast steps, the accumulated `f_eV` contribution is `O(f_e/e)=O(e)` on bounded sets, and the accumulated forcing is

`O((f_e/e)e^{-1/2})=O(sqrt(e))`.                                    (4.6)

Thus both vanish.

Let

`M^e(s)=sum_{k<floor(s/e)} sqrt(e)Pxi_{k+1}^e`.                       (4.7)

Its jumps are `O(sqrt(e))`, so the Lindeberg condition is automatic. From conditional independence and (1.5),

`<M^e>_s
 = sum_{k<floor(s/e)} e P D(QZ_k^e)P^T`.                         (4.8)

The stable linear recursion (4.5), together with bounded noise increments, gives tightness of `V^e` by the usual discrete Lyapunov estimate. Hence `W_k^e=sqrt(e)V_k^e=o_p(1)` uniformly on compact fast intervals. Since

`QZ_k^e = Y_k^e 1+QW_k^e`,                                          (4.9)

(4.4) and tightness imply, after integration in (4.8),

`<M^e>_s -> s y(1-y) P P^T`                                         (4.10)

uniformly on compact intervals in probability. The martingale functional central limit theorem therefore yields

`M^e => sqrt(y(1-y))P B^(N)`.                                       (4.11)

Finally, summing (4.5), the drift Riemann sums converge to

`-int_0^s B V_u du`,                                                 (4.12)

while the two `f_e` terms vanish by (4.6). Every limit point solves the linear martingale problem (4.3). That problem has a unique law, so the full sequence converges. QED.

### Corollary 4.2 (stationary covariance of the fast layer)

At frozen slow coordinate `y`, the OU process has unique stationary covariance

`C_y = y(1-y) int_0^infinity exp(-sB) P P^T exp(-sB^T) ds`.           (4.13)

Equivalently, `C_y` is the unique symmetric covariance supported on `H` satisfying

`B C_y+C_y B^T = y(1-y) P P^T`,                                     (4.14)

`C_y pi=0`.                                                          (4.15)

This reveals a two-scale topology split:

- the **slow** Wright–Fisher diffusion depends on the network through `pi`, `pbar=pi^Tp`, and `kappa=||pi||_2^2`;
- the **fast transverse** fluctuation retains the entire stable operator `B=I-Q` through the Lyapunov covariance (4.13).

For a doubly stochastic network, `pi=N^{-1}1` and `kappa=1/N`. If in addition `Q` is symmetric, then `P` is the orthogonal projection onto `1^perp`, `B` is symmetric on that subspace, and

`C_y = (y(1-y)/2) B^{-1}` on `1^perp`.                               (4.16)

### Exact covariances for the two B15 stress tests

Factoring out `y(1-y)`, the defective example has

`C0_d = [[88/81,-8/81,-14/81],
         [-8/81,22/81,-20/81],
         [-14/81,-20/81,47/162]]`.                                  (4.17)

It satisfies exactly

`B_d C0_d+C0_d B_d^T=P_dP_d^T`, `C0_d pi_d=0`.                       (4.18)

For the period-three example,

`C0_p = [[2/9,-1/9,-1/9],
         [-1/9,2/9,-1/9],
         [-1/9,-1/9,2/9]] = P_p/3`,                                 (4.19)

and again (4.18) holds with `p` in place of `d`.

The exact rational checker and archived output are

`research7_2026-09-17/R7-01/artifacts/2026-09-18/2026-09-18T121700Z__P0087_fast_layer_and_OU_exact.py`

and

`research7_2026-09-17/R7-01/artifacts/2026-09-18/2026-09-18T121700Z__P0087_fast_layer_and_OU_exact.out`.

The output terminates `ALL_EXACT_CHECKS_PASS`.

---

## 5. Consistency with nearby published theory

The 2017 Aletti–Crimaldi–Ghiglietti network paper studies a different diminishing-step regime and proves synchronization plus CLTs. Its Perron normalization uses a positive left eigenvector `v_1`; after translating normalizations, the slow scalar coordinate is exactly `pi^T Z`, and its topology factor `||v_1||^2/N` becomes `||pi||_2^2=kappa`. Thus the coefficient in the P0087 slow diffusion agrees with the topology factor appearing in an independent asymptotic regime.

The 2021 Aletti–Crimaldi rescaled-Pólya paper obtains a Wright–Fisher diffusion with mutation in the one-urn setting. It is the natural solved scalar analogue of the source's network question.

The 2024 first-order network paper classifies synchronization regimes for general network interactions, and 2026 work develops CLTs for interacting innovation processes. These are useful analogues but do not, in the bounded 2026-09-18 literature check, supply the forced-network `f_e ~ c e^2` singular limit proved in the preceding R7-01 artifact. A search miss is not a novelty certificate; worldwide openness/novelty remains UNVERIFIED.

---

## 6. What this does and does not establish

The preceding artifact already moved the frozen source metric to `M_clause=2`. This run does **not** redefine that metric and therefore records no metric movement.

What is new here is stronger mechanism-level control:

1. arbitrary nonsynchronized initial data have an explicit fast deterministic layer `1y_0+e^{-sB}w_0`;
2. after synchronization to `sqrt(e)` scale, transverse fluctuations converge to an explicit OU process;
3. exact defective and periodic examples verify that the argument is genuinely robust to nonnormality, non-diagonalizability and periodicity;
4. the slow network dependence and fast network dependence are cleanly separated.

These results strengthen and stress-test the candidate source solution. They are not independent audits. Operational closure still requires the owner-mandated P26 audit, a distinct OTHER-track audit, final prior-art review, and a self-contained paper package.
