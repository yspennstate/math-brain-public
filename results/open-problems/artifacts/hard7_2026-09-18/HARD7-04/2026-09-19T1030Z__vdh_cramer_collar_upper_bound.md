# HARD7-04 — Cramér-collar upper bound for the post-giant largest component

**Status:** theorem-sized route result / **PARTIAL**. This note does **not** close van der Hofstad's Section 8.3 discrete-duality question. It proves the sharp Erdős–Rényi-scale *upper* leading constant for the largest component in the exact post-giant configuration-model remainder under the active finite-third-moment hypotheses. The matching lower bound, and hence the full source question, remain open on this track.

## 1. Setting and previously established inputs

Let the original deterministic degree sequence satisfy the active `VDH-8.3-DUALITY` source regime

\[
\nu_n=1+\varepsilon_n,\qquad \varepsilon_n\downarrow0,
\qquad \varepsilon_n n^{1/3}\to\infty,
\qquad \frac1n\sum_i d_i^3\to \mathbb E D^3<\infty,
\tag{1.1}
\]

with positive limiting mean, critical limiting law `D`, and the nondegeneracy used throughout the admitted track. Put

\[
N_n:=n\varepsilon_n^3\longrightarrow\infty,
\qquad
R_*:=\frac{\mathbb E[D(D-2)^2]}{\mathbb ED}>0.
\tag{1.2}
\]

The preceding HARD7-04 checkpoints establish the following facts for the completed-component stopping boundary at the end of the giant excursion.

1. The exact sleeping remainder is a configuration model on a random degree sequence `d^{post}`.
2. With probability `1-o(1)`, its largest component is the original graph's second-largest component `C_{2,n}`.
3. Writing
   \[
   M_n:=\sum_{v\in S_n^{post}}d_v,
   \quad
   Q_n^{post}:=\frac1{M_n}\sum_{v\in S_n^{post}}d_v(d_v-2),
   \quad
   R_n^{post}:=\frac1{M_n}\sum_{v\in S_n^{post}}d_v(d_v-2)^2,
   \tag{1.3}
   \]
   one has
   \[
   M_n/n\to_p\mu:=\mathbb ED>0,
   \qquad
   Q_n^{post}=-\varepsilon_n+o_p(\varepsilon_n),
   \qquad
   R_n^{post}\to_p R_*.
   \tag{1.4}
   \]
4. If `E_i~Exp(d_i)` are the independent auxiliary clocks from the exploration and `tau_n` is the post-giant stopping time, then
   \[
   S_n^{post}\subseteq\{i:E_i>\tau_n\},
   \qquad
   \frac{\tau_n}{\varepsilon_n}\to_p\frac2{R_*}.
   \tag{1.5}
   \]

The preceding report also proved the sharp residual-hub estimate

\[
\frac{\varepsilon_n\Delta_n^{post}}{\log N_n}
\le \frac{R_*}{2}+o_p(1),
\tag{1.6}
\]

but the proof below does not require the stronger Coulson--Perarnau condition `Delta |Q|=o(R)`, which can fail in the active source class.

The primary source remains Remco van der Hofstad, *Stochastic processes on random graphs*, preliminary monograph dated 4 August 2026, Notes on Section 8.3, printed p. 245 / PDF p. 255, which asks of the barely-supercritical finite-third-moment configuration model: **“Does the discrete duality principle still hold?”**

---

## 2. Main theorem

### Theorem 2.1 (sharp leading upper constant after the giant)

Under (1.1)--(1.5), for every fixed `delta>0`,

\[
\boxed{
\mathbb P\!\left(
|C_{2,n}|>
(1+\delta)\frac{2R_*}{\varepsilon_n^2}
\log(n\varepsilon_n^3)
\right)\longrightarrow0.
}
\tag{2.1}
\]

Equivalently, if `L_1^{post}` is the largest component of the exact post-giant configuration-model remainder,

\[
\boxed{
L_1^{post}\le
(1+o_p(1))\frac{2R_*}{\varepsilon_n^2}\log N_n.
}
\tag{2.2}
\]

This is an upper theorem only. No matching lower bound is claimed here.

---

## 3. B6 — deform to an exponentially collared residual law

The raw fourth moment of the post-giant degree sequence can be as large as order `epsilon_n^{-1}`, so the usual fourth-moment hypothesis is unavailable. The giant-removal clock, however, creates exactly the exponential collar needed at the Cramér scale.

### Lemma 3.1 (exponential fourth-moment collar)

For every fixed

\[
0<\lambda<\frac2{R_*},
\tag{3.1}
\]

one has

\[
\boxed{
\frac{\varepsilon_n}{n}
\sum_{v\in S_n^{post}}d_v^4e^{\lambda\varepsilon_n d_v}
\to_p0,
}
\tag{3.2}
\]

and

\[
\boxed{
\frac1n\sum_{v\in S_n^{post}}d_ve^{\lambda\varepsilon_n d_v}=O_p(1).
}
\tag{3.3}
\]

#### Proof

Choose `b` with

\[
\lambda<b<2/R_*.
\tag{3.4}
\]

By (1.5), `P(tau_n<b epsilon_n)->0`. On the complementary event, every sleeping vertex is an auxiliary clock survivor at deterministic time `b epsilon_n`, so

\[
\sum_{v\in S_n^{post}}d_v^4e^{\lambda\varepsilon_n d_v}
\le
\sum_i d_i^4e^{\lambda\varepsilon_n d_i}
\mathbf1_{\{E_i>b\varepsilon_n\}}.
\tag{3.5}
\]

The expectation of `epsilon_n/n` times the right side equals

\[
\frac1n\sum_i d_i^3
\bigl[\varepsilon_n d_i e^{-(b-\lambda)\varepsilon_n d_i}\bigr].
\tag{3.6}
\]

This tends to zero. Indeed, for each fixed cutoff `K`, the contribution from `d_i<=K` tends to zero uniformly because `epsilon_n K->0`; while the contribution from `d_i>K` is bounded by

\[
\sup_{x\ge0}xe^{-(b-\lambda)x}
\cdot
\frac1n\sum_{i:d_i>K}d_i^3,
\tag{3.7}
\]

which is uniformly small as `K->infinity` by convergence of the empirical third moments. Markov's inequality and `P(tau_n<b epsilon_n)->0` prove (3.2).

Similarly,

\[
\mathbb E\sum_i d_i e^{\lambda\varepsilon_n d_i}
\mathbf1_{\{E_i>b\varepsilon_n\}}
=
\sum_i d_i e^{-(b-\lambda)\varepsilon_n d_i}
\le \sum_i d_i=O(n),
\tag{3.8}
\]

which proves (3.3). `square`

### Corollary 3.2 (uniform Cramér expansion)

Conditional on the post-giant degree sequence, let

\[
\eta_n=\widehat D_n^{post}-2,
\qquad
\phi_n(\theta)=\mathbb E[e^{\theta\eta_n}],
\tag{3.9}
\]

where `\widehat D_n^{post}` is size-biased from the post-giant degrees. Fix any

\[
\frac1{R_*}<\lambda<\frac2{R_*}.
\tag{3.10}
\]

Uniformly for `0<=theta<=lambda epsilon_n`, in probability,

\[
\phi_n'(\theta)=-\varepsilon_n+R_*\theta+o(\varepsilon_n),
\tag{3.11}
\]

\[
\phi_n(\theta)=1-\varepsilon_n\theta+rac{R_*}{2}\theta^2+o(\varepsilon_n^2).
\tag{3.12}
\]

Consequently the unique positive minimizer `theta_n` in this interval satisfies

\[
\theta_n=(1+o_p(1))\frac{\varepsilon_n}{R_*},
\qquad
I_n:=-\log\phi_n(\theta_n)
=(1+o_p(1))\frac{\varepsilon_n^2}{2R_*}.
\tag{3.13}
\]

#### Proof

From (1.4),

\[
\phi_n'(0)=Q_n^{post}=-\varepsilon_n+o_p(\varepsilon_n),
\qquad
\phi_n''(0)=R_n^{post}=R_*+o_p(1).
\tag{3.14}
\]

For `theta<=lambda epsilon_n`, using `M_n=Theta_p(n)`,

\[
|\phi_n'''(\theta)|
\le C+\frac{C}{M_n}
\sum_{v\in S_n^{post}}d_v^4e^{\lambda\varepsilon_n d_v}
=o_p(\varepsilon_n^{-1})
\tag{3.15}
\]

by Lemma 3.1. Taylor's theorem therefore gives (3.11)--(3.12). Since `lambda R_*>1`, (3.11) is negative at zero and positive at `lambda epsilon_n` with probability tending to one, while `phi_n''>R_*/2` throughout the interval with probability tending to one. Hence the minimizer is unique. Solving (3.11) and substituting into (3.12) gives (3.13). `square`

**Outcome of B6.** The obstruction is not the large raw fourth moment itself. After giant removal, the residual law has enough exponential integrability on the *shrinking* `theta=O(epsilon_n)` Cramér window to recover the quadratic rate `epsilon_n^2/(2R_*)`.

---

## 4. B20 — why the standard algorithm fails, and a local-CLT-free repair

The Coulson--Perarnau exploration proof uses a tilted local central limit estimate. Their general hypotheses guarantee the needed uniform local estimate, but those hypotheses are not inherited by the post-giant sequence in the full source class. Here the local estimate can be recovered from two fixed atoms alone.

### Lemma 4.1 (two-atom anti-concentration)

Let `Y` be integer valued. Suppose that for fixed distinct integers `a,b` and a fixed `c>0`,

\[
\mathbb P(Y=a)\ge c,
\qquad
\mathbb P(Y=b)\ge c.
\tag{4.1}
\]

Then for iid copies `Y_1,...,Y_t`,

\[
\boxed{
\sup_{z\in\mathbb Z}
\mathbb P\left(\sum_{j=1}^tY_j=z\right)
\le \frac{C_c}{\sqrt t}
}
\tag{4.2}
\]

for all `t>=1`.

#### Proof

Write the law of `Y` as

\[
2c\left(\tfrac12\delta_a+\tfrac12\delta_b\right)+(1-2c)\rho
\tag{4.3}
\]

for a probability law `rho` (if the two atom masses exceed `c`, put all excess mass into `rho`). Let `J~Bin(t,2c)` count the summands drawn from the two-atom component. Conditional on `J` and on all `rho`-summands, the remaining random contribution is

\[
Ja+(b-a)B_J,
\qquad B_J\sim Bin(J,1/2),
\tag{4.4}
\]

so every atom has probability at most `C/\sqrt{J+1}`. On `J>=ct` this is `O(t^{-1/2})`; on `J<ct`, a Chernoff bound is exponentially small. Averaging proves (4.2). `square`

### Why the two atoms exist here

Criticality gives

\[
\mathbb E[D(D-2)]=0.
\tag{4.5}
\]

Since `R_*>0`, there must be positive limiting mass at degree `1` and at some fixed degree `k>=3`: degree `1` is the only negative contribution to (4.5), while a positive contribution requires some degree at least `3`. Therefore the size-biased increment `D^*-2` has fixed positive masses at

\[
-1,\qquad k-2.
\tag{4.6}
\]

Empirical convergence of the exact post-giant degree law preserves positive lower bounds for those two atom masses with probability tending to one. Exponential tilting by any `theta=O(epsilon_n)` also preserves positive lower bounds, since the tilt factors on fixed atoms tend to one and the normalizer tends to one.

Thus Lemma 4.1 supplies the only `t^{-1/2}` point-mass estimate needed below, without a fourth-moment local CLT and without a stable-lattice hypothesis.

---

## 5. B25 — count large components twice

Fix `delta>0` and define the Erdős--Rényi-scale benchmark

\[
T_n:=\frac{2R_*}{\varepsilon_n^2}\log N_n.
\tag{5.1}
\]

Let

\[
K_n:=\left\lfloor(1+\delta/2)T_n\right\rfloor.
\tag{5.2}
\]

We condition on a post-giant degree sequence on which all conclusions above hold. Since `M_n=Theta(n)` and `N_n=n epsilon_n^3`,

\[
\frac{K_n}{M_n}
=O\left(\frac{\varepsilon_n\log N_n}{N_n}\right)
=o(\varepsilon_n).
\tag{5.3}
\]

### 5.1 An iid walk that dominates finite-population exploration

Let `eta_n` have the initial size-biased increment law from (3.9). Put

\[
A_n:=\frac{M_n}{M_n-2K_n+1}=1+o(\varepsilon_n).
\tag{5.4}
\]

Define an integer-valued random variable `beta_n` on `{-1,0,1,...}` by

\[
\mathbb P(\beta_n=\ell)=A_n\mathbb P(\eta_n=\ell),
\qquad \ell\ge0,
\tag{5.5}
\]

and

\[
\mathbb P(\beta_n=-1)
=A_n\mathbb P(\eta_n=-1)-(A_n-1).
\tag{5.6}
\]

For large `n`, (5.6) is positive because the degree-1 size-biased mass stays bounded below and `A_n-1=o(1)`. The probabilities sum to one.

During any of the first `K_n` pairings in a configuration-model component exploration, the partner half-edge denominator is at least `M_n-2K_n+1`. Therefore, for every nonnegative increment threshold, the conditional tail of the actual increment is at most `A_n` times the corresponding initial `eta_n` tail. A collision has increment `-2`, which can only make the actual queue smaller. Hence `beta_n` first-order stochastically dominates every actual exploration increment through time `K_n`.

Its mgf is exactly

\[
\phi_{\beta,n}(\theta)
=A_n\phi_n(\theta)-(A_n-1)e^{-\theta}.
\tag{5.7}
\]

By (5.3), `A_n-1=o(epsilon_n)`. Equations (3.11)--(3.15) therefore persist for `phi_{beta,n}`. In particular its Cramér minimizer and rate satisfy

\[
\theta_{\beta,n}=(1+o(1))\frac{\varepsilon_n}{R_*},
\qquad
I_{\beta,n}:=-\log\phi_{\beta,n}(\theta_{\beta,n})
=(1+o(1))\frac{\varepsilon_n^2}{2R_*}.
\tag{5.8}
\]

The exponentially tilted `beta_n` law at `theta_{beta,n}` retains the two fixed atoms from (4.6), so Lemma 4.1 applies uniformly.

### 5.2 Hitting-time tail

Let

\[
W_t=s+\sum_{j=1}^t\beta_{n,j},
\qquad
\tau_s:=\inf\{t\ge0:W_t=0\},
\tag{5.9}
\]

with `s>=1`. Since `beta_n>=-1`, the cyclic/Kemperman identity gives

\[
\mathbb P(\tau_s=t)
=\frac{s}{t}\,
\mathbb P\left(\sum_{j=1}^t\beta_{n,j}=-s\right).
\tag{5.10}
\]

Under exponential tilt at `theta_{beta,n}`,

\[
\mathbb P\left(\sum_{j=1}^t\beta_{n,j}=-s\right)
=e^{\theta_{\beta,n}s}
\phi_{\beta,n}(\theta_{\beta,n})^t
\mathbb P_{\theta_{\beta,n}}
\left(\sum_{j=1}^t\beta_{n,j}=-s\right).
\tag{5.11}
\]

Lemma 4.1 bounds the last factor by `C/\sqrt t`. Hence

\[
\mathbb P(\tau_s=t)
\le
C s e^{\theta_{\beta,n}s}
 e^{-I_{\beta,n}t}t^{-3/2}.
\tag{5.12}
\]

Summing the geometric tail and using `1-e^{-I_{beta,n}}\asymp I_{beta,n}` gives

\[
\boxed{
\mathbb P(\tau_s\ge K_n)
\le
\frac{C s e^{\theta_{\beta,n}s}}
{I_{\beta,n}K_n^{3/2}}
 e^{-I_{\beta,n}K_n}.
}
\tag{5.13}
\]

By stochastic domination, the same right side bounds the probability that a configuration-model exploration rooted at a vertex of degree `s` is still alive after `K_n` edge pairings.

### 5.3 Global double count

Let `Z_n` be the number of post-giant components with more than `(1+delta)T_n` vertices. For all large `n`, such a connected component has at least `K_n` edges. Counting every large component once and then by its vertices,

\[
Z_n
\le \frac1{K_n}
\sum_{v\in S_n^{post}}
\mathbf1\{\text{the exploration from }v\text{ survives }K_n\text{ pairings}\}.
\tag{5.14}
\]

Taking conditional expectations and using (5.13),

\[
\mathbb E[Z_n\mid d^{post}]
\le
\frac{C e^{-I_{\beta,n}K_n}}
{I_{\beta,n}K_n^{5/2}}
\sum_{v\in S_n^{post}}d_v e^{\theta_{\beta,n}d_v}.
\tag{5.15}
\]

Choose once and for all `lambda` satisfying (3.10). With probability tending to one, `theta_{beta,n}<=lambda epsilon_n`, so Lemma 3.1 gives

\[
\sum_{v\in S_n^{post}}d_v e^{\theta_{\beta,n}d_v}=O_p(n).
\tag{5.16}
\]

Also (5.8) and (5.2) imply

\[
I_{\beta,n}K_n
=(1+\delta/2+o_p(1))\log N_n.
\tag{5.17}
\]

Moreover

\[
\frac{n}{I_{\beta,n}K_n^{5/2}}
=O_p\left(\frac{n\varepsilon_n^3}{(\log N_n)^{5/2}}\right)
=O_p\left(\frac{N_n}{(\log N_n)^{5/2}}\right).
\tag{5.18}
\]

Combining (5.15)--(5.18), for example on an event of probability tending to one on which the `o_p(1)` in (5.17) is smaller than `delta/6`,

\[
\mathbb E[Z_n\mid d^{post}]
=O_p\left(
\frac{N_n^{-\delta/3}}{(\log N_n)^{5/2}}
\right)
\to_p0.
\tag{5.19}
\]

Since conditional probabilities are bounded by `min(1,E[Z_n|d^{post}])`, convergence in probability in (5.19) plus bounded convergence yields

\[
\mathbb P(Z_n>0)\to0.
\tag{5.20}
\]

This proves (2.2). The preceding stopping-time reduction identifies `L_1^{post}=|C_{2,n}|` with probability `1-o(1)`, proving (2.1). `square`

**Outcome of B25.** The global factor is exactly `N_n=n epsilon_n^3`: the Cramér penalty contributes `N_n^{-(1+delta/2+o(1))}`, while double counting and the `t^{-3/2}` excursion prefactor contribute the compensating `N_n` scale. This recovers the sharp upper coefficient `2R_*` without forcing the residual sequence into the stronger maximum-degree regime of the existing black-box theorem.

---

## 6. What remains

The matching statement

\[
\boxed{
\mathbb P\!\left(
L_1^{post}<
(1-\delta)\frac{2R_*}{\varepsilon_n^2}\log N_n
\right)\to0
}
\tag{6.1}
\]

is **not proved** here. A first-moment count below the threshold is not enough because component indicators are strongly dependent. The natural next obstruction is a lower excursion estimate together with collision/overlap control for many candidate roots. Heuristically, a tilted excursion of length `t\asymp epsilon_n^{-2}log N_n` has queue area on the order `t^{3/2}`, and

\[
\frac{t^{3/2}}n
\asymp
\frac{(\log N_n)^{3/2}}{N_n}\to0,
\tag{6.2}
\]

so collision losses should be negligible at the relevant scale. Turning (6.2) into a uniform conditioned-excursion theorem for the triangular, exponentially collared residual law is the missing step; (6.2) itself is only a route heuristic, not a theorem claimed in this note.

## 7. Literature/status boundary

A fresh bounded status screen on 19 September 2026 rechecked:

- van der Hofstad's 4 August 2026 monograph, where the question remains explicitly posed;
- Coulson--Perarnau, *Largest component of subcritical random graphs with given degree sequence*, EJP 28 (2023), DOI `10.1214/23-EJP921`, arXiv `2111.11780`;
- van der Hofstad--Luczak--Spencer's 2010 supercritical 2D Hamming-graph paper, a different model that gives evidence for discrete duality.

Queries for the exact discrete-duality wording and for barely-supercritical second-largest components in configuration models did not locate a later theorem closing the precise deterministic-degree finite-third-moment source question. This is **bounded negative evidence only**, not a worldwide novelty certificate.

No finite exhaustive claim is made in this note, so no checker was manufactured. The theorem-sized claim is proved on the page above.
