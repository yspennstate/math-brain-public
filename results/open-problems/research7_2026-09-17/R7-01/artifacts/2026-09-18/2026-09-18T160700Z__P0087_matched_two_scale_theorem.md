Model actually running: GPT-5.6 Sol. Reasoning level: UNVERIFIED — this is not GPT-6 at maximum; no authenticated runtime reasoning-effort telemetry or binding selector is exposed.

# P0087: a uniform matched initial-layer theorem and the correct two-scale continuous-time limit

Date: 2026-09-18.  
Worker: R7-01 (`6aabe777361481919c9e614646464772`).  
Source target: G. Aletti et al., *Open Problems in Stochastic Reinforcement Models*, Open Problem 16, printed pp. 14–16 of the chapter / pp. 477–498 of the 2023 MATRIX Annals, Springer 2025, DOI `10.1007/978-3-031-76738-8_29`.  
Status: **candidate source-level mathematical solution strengthened; operationally PARTIAL** pending the owner-mandated independent P26 audit, a distinct OTHER-track audit, final prior-art reconciliation, and a source-scoped paper package.  
Novelty: **UNVERIFIED**.

## 1. Exact source-facing issue resolved in this artifact

The source network model is

\[
Z_{n+1}=(1-r_r-r_f)Z_n+r_rX_{n+1}+r_fp,
\qquad
\mathbb E[X_{n+1}\mid\mathcal F_n]=A^T Z_n,
\]

with an irreducible interaction matrix and the conditional-independence convention inherited from the parent network-RSP model. The source asks whether the discrete process can be rescaled to a proper continuous-time limiting process in the critical regime

\[
r_f\sim c r_r^2=o(1),
\]

and writes a formally singular interacting-Wright–Fisher heuristic whose meaning is declared unknown.

Earlier R7-01 artifacts already proved:

1. the fixed-parameter convergence/nonconvergence classification;
2. the slow Perron-coordinate Jacobi/Wright–Fisher diffusion on the `r_r^{-2}` clock;
3. transverse collapse on every positive slow-time interval;
4. the deterministic synchronization layer on the `r_r^{-1}` clock;
5. the transverse fast Ornstein–Uhlenbeck fluctuation.

The STUCK1 diagnosis isolated one remaining source-facing packaging issue: for a nonsynchronized initial state the slow-scale vector process cannot have an ordinary càdlàg limit on `[0,T]`, because its transverse component is order one at `t=0` and vanishes for every fixed `t>0`. This artifact executes the prescribed recovery action and proves a single uniform matched theorem that is valid **through the initial layer**, then proves the correct joint two-clock limit and an explicit gluing theorem.

The three Section-B methods are exactly **B4 / B7 / B30**:

- **B4 — prove something weaker, completely:** replace the impossible claim of one fixed vector-valued slow-time limit by a uniform epsilon-dependent matched approximation, with an explicit remainder bound;
- **B7 — take the limit:** prove a joint product-space limit carrying both the fast synchronization path and the slow Jacobi diffusion;
- **B30 — one scale at a time, then glue:** exhibit a logarithmic overlap window where the fast layer has died while the slow variable has not yet moved macroscopically.

No finite checker is appropriate: all claims here are theorem/topology statements and are proved below.

---

## 2. Model and notation

Set

\[
\varepsilon=r_r,
\qquad
f_\varepsilon=r_f,
\qquad
Q=A^T.
\]

Assume

\[
\frac{f_\varepsilon}{\varepsilon^2}\to c\in[0,\infty).
\]

Then

\[
Z_{n+1}^\varepsilon
 = Z_n^\varepsilon
 +\varepsilon(Q-I)Z_n^\varepsilon
 +f_\varepsilon(p-Z_n^\varepsilon)
 +\varepsilon\xi_{n+1}^\varepsilon,
\tag{2.1}
\]

where

\[
\xi_{n+1}^\varepsilon=X_{n+1}^\varepsilon-QZ_n^\varepsilon,
\qquad
\mathbb E[\xi_{n+1}^\varepsilon\mid\mathcal F_n]=0.
\]

Let `pi` be the unique positive stationary probability vector of the irreducible row-stochastic matrix `Q`:

\[
\pi^TQ=\pi^T,
\qquad
\pi^T\mathbf1=1.
\]

Define

\[
Y_n^\varepsilon=\pi^TZ_n^\varepsilon,
\qquad
P=I-\mathbf1\pi^T,
\qquad
W_n^\varepsilon=PZ_n^\varepsilon=Z_n^\varepsilon-\mathbf1Y_n^\varepsilon.
\]

Let

\[
H=\{w:\pi^Tw=0\},
\qquad
B=(I-Q)|_H.
\]

Because `Q` is irreducible, eigenvalue `1` is simple and every other eigenvalue `lambda` satisfies `Re(lambda)<1`; hence every eigenvalue of `B` has strictly positive real part. Therefore there are constants `C,a>0` such that

\[
\|e^{-sB}\|_H\le Ce^{-as},\qquad s\ge0.
\tag{2.2}
\]

The projected recursions are exact:

\[
Y_{n+1}^\varepsilon-Y_n^\varepsilon
 =f_\varepsilon(\bar p-Y_n^\varepsilon)
 +\varepsilon\eta_{n+1}^\varepsilon,
\qquad
\bar p=\pi^Tp,
\qquad
\eta_{n+1}^\varepsilon=\pi^T\xi_{n+1}^\varepsilon,
\tag{2.3}
\]

and

\[
W_{n+1}^\varepsilon
 =T_\varepsilon W_n^\varepsilon
 +f_\varepsilon Pp
 +\varepsilon P\xi_{n+1}^\varepsilon,
\qquad
T_\varepsilon=I-\varepsilon B-f_\varepsilon I
\quad\text{on }H.
\tag{2.4}
\]

The state space `[0,1]^N` makes all noise increments uniformly bounded.

For slow time define

\[
n_\varepsilon(t)=\left\lfloor\frac{t}{\varepsilon^2}\right\rfloor,
\qquad
Y^\varepsilon(t)=Y_{n_\varepsilon(t)}^\varepsilon.
\]

Earlier work proved

\[
Y^\varepsilon\Rightarrow Y
\quad\text{in }D([0,T]),
\tag{2.5}
\]

where

\[
dY_t=c(\bar p-Y_t)\,dt
 +\sqrt{\kappa Y_t(1-Y_t)}\,dB_t,
\qquad
\kappa=\sum_j\pi_j^2.
\tag{2.6}
\]

---

# 3. B4 — complete uniform matched decomposition

## Theorem 3.1 (uniform matched initial-layer theorem)

For every fixed `T<infinity`, uniformly over initial states `Z_0^varepsilon in [0,1]^N`,

\[
\boxed{
\sup_{0\le t\le T}
\left\|
Z_{n_\varepsilon(t)}^\varepsilon
-
\Bigl(
\mathbf1Y^\varepsilon(t)
+e^{-(t/\varepsilon)B}W_0^\varepsilon
\Bigr)
\right\|
 =O_{\mathbb P}\!\left(\sqrt{\varepsilon\log(1/\varepsilon)}\right).
}
\tag{3.1}
\]

In particular the remainder converges to zero uniformly on the full slow interval `[0,T]`, including `t=0`.

This is the precise source-facing replacement for the impossible assertion that the vector process itself has a fixed càdlàg slow-time limit from an arbitrary nonsynchronized initial state.

### Proof

Iterating (2.4) gives, for every integer `n>=0`,

\[
W_n^\varepsilon
 =T_\varepsilon^nW_0^\varepsilon
 +f_\varepsilon\sum_{j=0}^{n-1}T_\varepsilon^jPp
 +\varepsilon\sum_{k=1}^nT_\varepsilon^{n-k}P\xi_k^\varepsilon.
\tag{3.2}
\]

We bound its three nontrivial pieces uniformly in `n<=T/epsilon^2`.

### Step 1. Uniform stability of the discrete transverse semigroup

Because all eigenvalues of `B` have positive real part, the Lyapunov argument already used in the cumulative proof yields constants `C,a>0` such that, for all sufficiently small `epsilon`,

\[
\|T_\varepsilon^m\|_H\le Ce^{-a\varepsilon m},
\qquad m\ge0.
\tag{3.3}
\]

The same estimate holds for the continuous semigroup:

\[
\|e^{-m\varepsilon B}\|_H\le Ce^{-a\varepsilon m}.
\tag{3.4}
\]

### Step 2. The discrete semigroup is uniformly close to the boundary-layer exponential

Put

\[
E_\varepsilon=e^{-\varepsilon B}.
\]

Since `f_epsilon=O(epsilon^2)`, Taylor expansion in finite dimension gives

\[
\|T_\varepsilon-E_\varepsilon\|
 =\|I-\varepsilon B-f_\varepsilon I-e^{-\varepsilon B}\|
 \le C\varepsilon^2.
\tag{3.5}
\]

For `n>=1`, the telescoping identity

\[
T_\varepsilon^n-E_\varepsilon^n
 =\sum_{j=0}^{n-1}
 T_\varepsilon^{n-1-j}
 (T_\varepsilon-E_\varepsilon)
 E_\varepsilon^j
\]

combined with (3.3)–(3.5) yields

\[
\|T_\varepsilon^n-E_\varepsilon^n\|
 \le Cn\varepsilon^2e^{-a\varepsilon(n-1)}.
\tag{3.6}
\]

Let `x=epsilon n`. Then

\[
n\varepsilon^2e^{-a\varepsilon n}
 =\varepsilon x e^{-ax},
\]

whose supremum over `x>=0` is `O(epsilon)`. Hence

\[
\sup_{n\ge0}
\|T_\varepsilon^n-e^{-n\varepsilon B}\|
 \le C\varepsilon.
\tag{3.7}
\]

Now set `n=n_epsilon(t)`. Since

\[
0\le \frac t\varepsilon-n\varepsilon<\varepsilon,
\]

write `delta=t/epsilon-n epsilon in [0,epsilon)`. Then

\[
e^{-(t/\varepsilon)B}
 =e^{-n\varepsilon B}e^{-\delta B},
\]

so by (3.4) and `||I-e^{-delta B}||<=C delta`, uniformly in `t>=0`,

\[
\|e^{-n\varepsilon B}-e^{-(t/\varepsilon)B}\|
 \le C\varepsilon.
\tag{3.8}
\]

Combining (3.7) and (3.8),

\[
\boxed{
\sup_{t\ge0}
\|T_\varepsilon^{n_\varepsilon(t)}-e^{-(t/\varepsilon)B}\|
 \le C\varepsilon.
}
\tag{3.9}
\]

Because every `Z_0^epsilon` lies in the compact cube `[0,1]^N`, `||W_0^epsilon||` is uniformly bounded; therefore the initial-state semigroup error contributes only `O(epsilon)` to (3.1).

### Step 3. The deterministic forcing contribution is uniformly `O(epsilon)`

Using (3.3),

\[
\left\|
f_\varepsilon\sum_{j=0}^{n-1}T_\varepsilon^jPp
\right\|
\le
Cf_\varepsilon\sum_{j\ge0}e^{-a\varepsilon j}
\le C\frac{f_\varepsilon}{\varepsilon}
=O(\varepsilon).
\tag{3.10}
\]

This bound is uniform in `n`.

### Step 4. Uniform stochastic-convolution bound

For fixed `n`, define

\[
N_n^\varepsilon
 =\varepsilon\sum_{k=1}^nT_\varepsilon^{n-k}P\xi_k^\varepsilon.
\tag{3.11}
\]

For each fixed coordinate (or any fixed unit dual vector), (3.11) is a martingale sum in the index `k`. Its `k`-th increment has absolute value bounded by

\[
C\varepsilon e^{-a\varepsilon(n-k)},
\]

because `xi_k^epsilon` is uniformly bounded and (3.3) holds. Consequently the sum of squared increment bounds is

\[
C\varepsilon^2\sum_{j\ge0}e^{-2a\varepsilon j}
\le C\varepsilon.
\tag{3.12}
\]

Azuma–Hoeffding therefore gives, after a fixed finite-dimensional coordinate union bound,

\[
\mathbb P(\|N_n^\varepsilon\|>u)
\le C_1\exp\!\left(-\frac{u^2}{C_2\varepsilon}\right).
\tag{3.13}
\]

There are at most `1+T/epsilon^2` relevant indices. Another union bound yields

\[
\mathbb P\left(
\max_{0\le n\le T/\varepsilon^2}\|N_n^\varepsilon\|>u
\right)
\le
C_T\varepsilon^{-2}
\exp\!\left(-\frac{u^2}{C_2\varepsilon}\right).
\tag{3.14}
\]

Take

\[
u=L\sqrt{\varepsilon\log(1/\varepsilon)}
\]

with `L` sufficiently large. Then the right side of (3.14) tends to zero. Hence

\[
\max_{0\le n\le T/\varepsilon^2}
\|N_n^\varepsilon\|
=O_{\mathbb P}\!\left(\sqrt{\varepsilon\log(1/\varepsilon)}\right).
\tag{3.15}
\]

### Step 5. Assemble the decomposition

Because

\[
Z_n^\varepsilon=\mathbf1Y_n^\varepsilon+W_n^\varepsilon,
\]

substitute (3.2), then use (3.9), (3.10), and (3.15). The deterministic `O(epsilon)` terms are smaller than `sqrt(epsilon log(1/epsilon))` for small `epsilon`. This proves (3.1). QED.

---

## Corollary 3.2 (exact criterion for an ordinary vector slow-time limit)

Assume `Z_0^epsilon -> z_0` and put

\[
y_0=\pi^Tz_0,
\qquad
w_0=z_0-\mathbf1y_0.
\]

If `w_0=0`, then the already-proved slow theorem and (3.1) give

\[
Z_{n_\varepsilon(\cdot)}^\varepsilon
\Rightarrow
\mathbf1Y
\quad\text{in }D([0,T],\mathbb R^N).
\tag{3.16}
\]

If `w_0\neq0`, then the slow-scale vector processes **cannot** converge weakly in ordinary Skorokhod `J_1` topology on `D([0,T],R^N)` to any càdlàg process.

### Proof of the negative half

Suppose a subsequence converged to some càdlàg `Z`. Evaluation at time zero is continuous in the `J_1` topology, so

\[
Z(0)=z_0
\quad\text{a.s.}
\tag{3.17}
\]

For every fixed `delta>0`, the cumulative transverse-collapse theorem plus the scalar diffusion limit implies that the restriction to `[delta,T]` converges to the consensus process `1Y`. Therefore every subsequential limit satisfies

\[
Z(t)\in\{\mathbf1 y:y\in\mathbb R\}
\quad\text{for every rational }t>0,
\quad\text{a.s.}
\tag{3.18}
\]

By right continuity and closedness of the consensus line, (3.18) forces `Z(0)` to lie on the consensus line almost surely. This contradicts (3.17) when `w_0 !=0`. QED.

Thus the source's singular heuristic has a sharp interpretation: a proper **single-clock vector** limit exists from synchronized starts, but arbitrary nonsynchronized starts necessarily require an initial-layer/two-scale description.

---

# 4. B7 — the proper joint two-scale continuous-time limit

The uniform matched theorem says how to approximate the original process on one slow-time interval. The next question is what fixed limiting object retains all source-relevant initial information.

For `S,T<infinity`, define the fast-scale process

\[
\widehat Z^\varepsilon(s)
 =Z_{\lfloor s/\varepsilon\rfloor}^\varepsilon,
\qquad 0\le s\le S,
\]

and retain the slow scalar process `Y^epsilon(t)` on `[0,T]`.

## Theorem 4.1 (joint two-clock limit)

Assume `Z_0^epsilon -> z_0`, and define `y_0=pi^Tz_0`, `w_0=z_0-1y_0`. Then

\[
\boxed{
(\widehat Z^\varepsilon,\,Y^\varepsilon)
\Rightarrow
(\widehat z,\,Y)
}
\tag{4.1}
\]

in

\[
D([0,S],\mathbb R^N)\times D([0,T],\mathbb R),
\]

where

\[
\widehat z(s)=\mathbf1y_0+e^{-sB}w_0
\tag{4.2}
\]

is deterministic, and `Y` is the Jacobi/Wright–Fisher diffusion (2.6) started from `y_0`.

### Proof

The previously proved fast-layer theorem gives

\[
\sup_{0\le s\le S}
\|\widehat Z^\varepsilon(s)-\widehat z(s)\|
\xrightarrow{\mathbb P}0.
\tag{4.3}
\]

The slow theorem gives

\[
Y^\varepsilon\Rightarrow Y.
\tag{4.4}
\]

A random element converging in probability to a deterministic element can be adjoined to any tight weakly convergent sequence without an independence assumption: by Slutsky's theorem in the product Polish space, (4.3) and (4.4) imply (4.1). QED.

### Interpretation

The correct continuous-time object has two clocks:

1. `s=epsilon n`: deterministic network synchronization, retaining the full stable operator `B=I-Q`;
2. `t=epsilon^2 n`: stochastic motion along the Perron/consensus manifold, retaining the network only through `pi`, `pbar=pi^Tp`, and `kappa=||pi||_2^2`.

The two limits are not competing descriptions. They are the two components of one singular perturbation problem, and Theorem 3.1 supplies their uniform matched approximation in the original variables.

---

# 5. B30 — logarithmic overlap and rigorous gluing

The STUCK1 diagnosis proposed the matching time

\[
n_\varepsilon^*
 =\left\lceil
 K\varepsilon^{-1}\log(1/\varepsilon)
 \right\rceil,
\qquad K>0,
\tag{5.1}
\]

with corresponding slow time

\[
\tau_\varepsilon
 =\varepsilon^2 n_\varepsilon^*
 =K\varepsilon\log(1/\varepsilon)+O(\varepsilon^2)
 \longrightarrow0.
\tag{5.2}
\]

## Theorem 5.1 (matched gluing through the overlap window)

For every fixed `T` and every fixed `K>0`,

\[
\boxed{
\sup_{0\le t\le\tau_\varepsilon}
\left\|
Z_{n_\varepsilon(t)}^\varepsilon
-
\left(
\mathbf1Y_0^\varepsilon
+e^{-(t/\varepsilon)B}W_0^\varepsilon
\right)
\right\|
=O_{\mathbb P}\!\left(\sqrt{\varepsilon\log(1/\varepsilon)}\right)
}
\tag{5.3}
\]

and

\[
\boxed{
\sup_{\tau_\varepsilon\le t\le T}
\|Z_{n_\varepsilon(t)}^\varepsilon-\mathbf1Y^\varepsilon(t)\|
=O_{\mathbb P}\!\left(\sqrt{\varepsilon\log(1/\varepsilon)}\right)
+O(\varepsilon^{aK}).
}
\tag{5.4}
\]

At the matching time itself,

\[
\boxed{
Z_{n_\varepsilon^*}^\varepsilon
-\mathbf1Y_0^\varepsilon
=O_{\mathbb P}\!\left(\sqrt{\varepsilon\log(1/\varepsilon)}\right)
+O(\varepsilon^{aK}).
}
\tag{5.5}
\]

Thus the fast approximation and the slow approximation overlap on a vanishing macroscopic interval: by time `tau_epsilon` synchronization has completed, but the slow diffusion coordinate has moved by only `o_P(1)`.

### Proof

### Step 1. The slow coordinate is frozen throughout the layer

For `m<=n_epsilon^*`, (2.3) gives

\[
Y_m^\varepsilon-Y_0^\varepsilon
 =\sum_{k<m}f_\varepsilon(\bar p-Y_k^\varepsilon)
 +\varepsilon\sum_{k<m}\eta_{k+1}^\varepsilon.
\tag{5.6}
\]

The deterministic term is bounded by

\[
n_\varepsilon^* f_\varepsilon
 =O(\varepsilon\log(1/\varepsilon)).
\tag{5.7}
\]

The martingale increments are uniformly bounded, and the quadratic second-moment bound up to `n_epsilon^*` is

\[
C\varepsilon^2n_\varepsilon^*
 =O(\varepsilon\log(1/\varepsilon)).
\tag{5.8}
\]

Doob's maximal inequality therefore yields

\[
\max_{m\le n_\varepsilon^*}
|Y_m^\varepsilon-Y_0^\varepsilon|
=O_{\mathbb P}\!\left(\sqrt{\varepsilon\log(1/\varepsilon)}\right).
\tag{5.9}
\]

Combining (5.9) with Theorem 3.1 proves (5.3).

### Step 2. The initial layer is negligible after the matching time

By (2.2), for `t>=tau_epsilon`,

\[
\|e^{-(t/\varepsilon)B}W_0^\varepsilon\|
\le
C e^{-a\tau_\varepsilon/\varepsilon}
\|W_0^\varepsilon\|.
\]

Because the initial states stay in the compact cube,

\[
\sup_{t\ge\tau_\varepsilon}
\|e^{-(t/\varepsilon)B}W_0^\varepsilon\|
\le C\varepsilon^{aK}.
\tag{5.10}
\]

Theorem 3.1 now gives (5.4).

### Step 3. Both descriptions agree at the overlap

At `t=tau_epsilon`, (5.9) says

\[
Y^\varepsilon(\tau_\varepsilon)-Y_0^\varepsilon
=O_{\mathbb P}\!\left(\sqrt{\varepsilon\log(1/\varepsilon)}\right),
\]

while (5.10) says the transverse deterministic layer is `O(epsilon^{aK})`; the matched remainder is controlled by Theorem 3.1. This proves (5.5). QED.

If one chooses `K>1/(2a)`, then `epsilon^{aK}=o(sqrt(epsilon))`, so the stochastic `sqrt(epsilon log(1/epsilon))` term dominates the displayed matching error.

---

# 6. What is now proved about the source heuristic

The source writes, heuristically, a singular vector dynamics with an interaction contribution of order `1/sqrt(dt)`. The cumulative R7-01 argument plus Theorems 3.1, 4.1 and 5.1 give a rigorous interpretation:

1. **There is one slow stochastic degree of freedom.** It is `Y=pi^TZ`; its critical limit is the Jacobi/Wright–Fisher diffusion (2.6).
2. **Every non-Perron mode is fast.** On `s=epsilon n`, the leading deterministic motion is `exp(-sB)w_0`.
3. **No extra vector diffusion survives on the slow clock.** Transverse fluctuations are only order `sqrt(epsilon)` on the fast clock and disappear at leading slow order.
4. **Arbitrary nonsynchronized initial states do not admit a single ordinary vector J1 slow-time limit.** This is a genuine topological obstruction, not a missing estimate.
5. **A proper continuous-time description nevertheless exists.** It is the joint two-clock limit (4.1), and the original discrete chain is uniformly approximated by the matched expression in (3.1).
6. **The two clocks glue rigorously.** The logarithmic window (5.1)–(5.5) is an overlap region where the fast mode is negligible and the slow coordinate is still asymptotically frozen.

This directly resolves the exact blocker isolated by STUCK1.

---

# 7. Dated source and prior-art boundary — 2026-09-18

Primary source rechecked directly on 2026-09-18:

- G. Aletti et al., *Open Problems in Stochastic Reinforcement Models*, Springer / MATRIX Book Series, 2025, DOI `10.1007/978-3-031-76738-8_29`; the current MATRIX PDF is `https://www.matrix-inst.org.au/wp_Matrix2016/wp-content/uploads/2023/Aletti.pdf`.
- The source's Open Problem 16 gives the forced network recursion and explicitly states that the meaning/asymptotics of the singular time-rescaled interacting-Wright–Fisher heuristic are unknown.

Bounded follow-up search on 2026-09-18 recovered:

- G. Aletti and I. Crimaldi, *The Rescaled Pólya Urn and the Wright–Fisher Process with Mutation*, Mathematics 9 (2021), 2909: the scalar/urn Wright–Fisher analogue;
- G. Aletti, I. Crimaldi and A. Ghiglietti, *Networks of reinforced stochastic processes: A complete description of the first-order asymptotics*, Stochastic Processes and their Applications 176 (2024), 104427: first-order network synchronization regimes, not the forced critical `r_f/r_r^2 -> c` scaling studied here;
- the authors' 2026 publication line includes work on statistical inference for interacting innovation processes, a different model family.

Searches using the exact source title, `forced network`, `r_f`, `r_r`, the three network authors, and the critical scaling did **not** surface a later theorem matching Open Problem 16's forced-network rescaling question. This is negative evidence only. Worldwide openness and novelty remain **UNVERIFIED**.

---

# 8. Metric and lifecycle consequence

The admission-fixed metric is

`M_clause(P0087) in {0,1,2}` = the number of Open Problem 16's two source clauses having complete source-scope proofs in the cumulative record.

It was already at `2` before this recovery run, so despite the substantive theorem above:

`M_clause(P0087): 2 -> 2 (NO MOVEMENT)`.

The preceding STUCK1 report held the ordinary unchanged count at `3` and advanced the HARD stuck-recovery count to `1`. This artifact executes that prescribed recovery action successfully but does not redefine the frozen metric. The run report should therefore record the ordinary unchanged count as `3 -> 4`, with STUCK recovery cycle 1 completed. Under the owner protocol, because the metric remains unchanged, the next iteration should be the second thinking-only stuck diagnosis rather than another unconstrained strengthening run.

The current mathematical status is still **candidate source-level solution strengthened / operationally PARTIAL**. No PROVED label is asserted until the required independent P26 audit, a distinct OTHER-track audit, final prior-art reconciliation, and self-contained `paper_<name>/` package exist.
