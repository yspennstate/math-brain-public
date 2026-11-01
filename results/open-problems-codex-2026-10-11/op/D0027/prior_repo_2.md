Model/effort: **GPT-5.6 Sol / reasoning effort UNVERIFIED** — GPT-6 / maximum reasoning was requested, but this runtime exposes no authenticated reasoning-effort telemetry or binding model/effort selector; `E_FAexp: 0 -> 0` (**no movement**); D0027 is retired from the R7-04 research lane after six unchanged ordinary research runs.

# R7-04 immutable handoff — D0027 / FA-1f exponential relaxation

Date: 2026-09-17 UTC  
Owner during research: **R7-04 Constructive Model Research**  
Native task ID: `6aabe7ea6e1881919a65503f8445a813`  
Own root: `research7_2026-09-17/R7-04/`  
Category: **CLOSABLE OUTSIDE**  
Final R7-04 source status: **PARTIAL / source OPEN by bounded dated search**  
Frozen source metric: `E_FAexp in {0,1}`  
Metric at admission: `0`  
Metric at handoff: `0`  
Ordinary unchanged research runs: **6**  
Stuck-recovery reports used: **1**  
Disposition: **RETIRED FROM R7-04 RESEARCH AFTER SIX UNCHANGED RUNS; DO NOT CONTINUE SEVENTH-RUN LEMMA/CHECKER CHURN IN THIS SLOT.**

## 1. Exact outside source and closure criterion

Fabio Martinelli, Assaf Shapira and Cristina Toninelli, *Long time behaviour of one facilitated kinetically constrained models: results and open problems*, arXiv:2510.20461v1 (2025), Section 1.1, Conjecture 2, source PDF p. 2.

Primary source: https://arxiv.org/abs/2510.20461

Source target: for one-dimensional FA-1f, if the initial law `nu` has exponentially decaying probability of containing no infected site in `[-ell,ell]`, then for **every `q>0`** and every local observable, its expectation converges to Bernoulli equilibrium exponentially fast.

`E_FAexp` may become `1` only after a full source-valid proof or a source-valid counterexample decides all of the above quantifiers. High-q, product-law, deterministic/single-infection, finite-volume or finite-support subclasses remain PARTIAL.

Canonical claim: `operations/claims/D0027.md`.  
Admission: `research7_2026-09-17/R7-04/admissions/2026-09-17T134300Z__D0027_FA1f_exponential_relaxation.md`.

A fresh 2026-09-17 check found the arXiv record still at v1 and found no explicit complete all-q resolution in the bounded later-author/follow-up search. That is negative evidence only, not a novelty or worldwide-openness certificate.

## 2. Strongest cumulative mathematics preserved

### 2.1 Deterministic-anchor reduction from the early runs

The earlier R7-04 runs reduced the source to a deterministic local-forgetting estimate around a shared infected anchor. In the notation of those reports, for a local observable supported on `S`,

```text
Delta_f(t,eta)
 <= 2 ||f||_infty P(D^x_{S,t})
    + exp[-gamma(q)t] sqrt((1-q)/q) sqrt(Var_pi(f)),
```

where the two copies share an infection at `x`. Thus a sufficiently strong exponential disagreement-extinction estimate, with only exponential cost in `dist(x,S)`, would glue to the source exponential-gap hypothesis. This estimate was not proved.

The same-Harris disagreement process has nearest-neighbor backward ancestry. A ring with a common infected neighbor is an exact ancestry cut. A common oriented `01` pair can be transported one step with the exact positive probability recorded in the fourth report,

```text
c_sh(q) = p*q / ((1+q)*(3-q)),   p=1-q.
```

A rectangular sitewise uncertainty abstraction was shown to be too lossy: it destroys logical correlations and therefore cannot by itself prove anchor forgetting.

### 2.2 Correlation-preserving certificate packing

For a fixed Harris diagram `H`, an `eta`-certificate is a finite set of time-zero bits whose agreement with `eta` forces the same terminal local output. Under the pinned equilibrium product law `nu_x=pi(.|eta_x=0)`, if `C_1,...,C_m` are certificates disjoint away from the anchor and

```text
w_eta(C)=p^(# healthy prescribed bits) q^(# infected prescribed bits),
```

then

```text
P_{nu_x}(terminal disagreement | H)
 <= product_j (1-w_eta(C_j))
 <= exp[-sum_j w_eta(C_j)].
```

The unresolved positive graphical theorem is to make the optimal disjoint certificate-packing mass grow linearly in time up to the anchor-distance cost.

### 2.3 Exact all-q finite-set duality

Put

```text
p=1-q,
phi(a)=(a-p)/q,
Phi_A(eta)=product_{y in A} phi(eta_y).
```

Define the finite-set process `A_t` by: every occupied `x` rings at rate one; when it rings, membership of `x-1` and `x+1` is independently refreshed to Bernoulli(`q`); `x` itself remains occupied.

For every deterministic FA-1f initial state, finite `A`, and `t>=0`, R7-04 proved the generator duality

```text
E_eta[Phi_A(eta_t)] = E_A[Phi_{A_t}(eta)].
```

Nonemptiness is conserved. On a finite cycle, Bernoulli(`q`) conditioned on nonemptiness is reversible. The normalization `(eta-p)/q` is the unique centered affine normalization for which multiplication by a healthy-site indicator becomes an honest Bernoulli membership refresh.

For the FA configuration `eta^(x)` having exactly one infection at `x`,

```text
(delta_{eta^(x)} P_t Phi_A)
 = (q - P_A(x in A_t))/q.
```

Therefore exponential relaxation of the single-infection stress test on the complete finite-cylinder basis is equivalent to

```text
|P_A(x in A_t)-q| <= C_{A,x,q} exp[-c(q)t]
```

for every finite nonempty dual start `A`.

This is a source-relevant singular subclass, not the full source.

### 2.4 Exact finite-volume comparison to BABP

Let `P_y` denote Bernoulli(`q`) heat-bath resampling of membership at `y`. On a finite cycle, the neighbor-refresh dual generator and the BABP generator (with independent left/right rate-one refresh clocks at every occupied center) are

```text
Q = sum_x xi_x (P_{x-1}P_{x+1}-I),
B = sum_x xi_x[(P_{x-1}-I)+(P_{x+1}-I)].
```

Their Dirichlet forms under Bernoulli(`q`) conditioned nonempty satisfy

```text
D_Q(f) <= D_B(f) <= 2 D_Q(f).
```

This is a finite-volume energy comparison only. It does not by itself transfer infinite-volume local ergodicity from finite initial sets.

## 3. Sixth-run mathematics: exact interpolation obstruction

Define `D_y=I-P_y` and

```text
H := sum_x xi_x D_{x-1}D_{x+1}.
```

Because the two coordinate heat-bath projections commute and `xi_x` commutes with the neighbor projections,

```text
Q-B = H,
B = Q-H.
```

On the finite-cycle reversible Hilbert space, `H` is positive semidefinite: each summand is `xi_x` times the orthogonal projection onto the genuine two-neighbor interaction component. Hence the valid generator interpolation

```text
L_theta=(1-theta)Q+theta B = Q-theta H,   0<=theta<=1,
```

has Duhamel derivative

```text
partial_theta P_t^(theta) f
 = - integral_0^t P_s^(theta) H P_{t-s}^(theta) f ds.
```

For the one-site observable `f(xi)=xi_0`,

```text
H f = 0,
Q f = (xi_{-1}+xi_1)(q-xi_0),
H Q f = 0.
```

Thus Q and BABP are indistinguishable at the first two Taylor orders for one-site occupation; the interpolation first sees a genuine three-site interaction.

Starting the dual from the singleton `{0}`, an exact generator calculation gives

```text
L_theta f({0}) = 0,
L_theta^2 f({0}) = -2 p q,
L_theta^3 f({0}) = 2 p q (2+q-theta q).
```

Consequently

```text
P_{ {0} }^(theta)(0 in A_t)
 = 1 - p q t^2
   + [p q(2+q-theta q)/3] t^3
   + O(t^4).
```

In particular,

```text
P^Q_{ {0} }(0 in A_t)-P^B_{ {0} }(0 in A_t)
 = (p q^2/3)t^3 + O(t^4).
```

So the simultaneous-refresh dual is already measurably slower than BABP at third order in this canonical local test. A finite-volume Dirichlet comparison cannot simply be read as a pointwise local-mixing transfer. Any interpolation proof must control the `H`-generated three-site interaction term.

## 4. Sixth-run mathematics: an exact one-sided local regeneration word

Suppose at a block start time `s` the dual has `xi_{x-1}(s)=1`. Fix `delta>0` and consider the Poisson-clock event

```text
E^-_{x,delta} = {
  no rings at x-2 during [s,s+delta],
  no rings at x during [s,s+delta],
  at least one ring at x-1 during [s,s+delta]
}.
```

Its conditional probability is exactly

```text
r(delta)=e^{-2 delta}(1-e^{-delta})>0.
```

On this event `x-1` remains occupied for the whole block, because only rings at `x-2` or `x` can refresh its membership. Let `sigma` be the last ring at `x-1` in the block. At `sigma`, site `x` is refreshed to a fresh Bernoulli(`q`) coin. After `sigma`, any possible ring at `x+1` that is enabled is determined by randomness independent of that coin, since there are no rings at `x`, and every such ring again refreshes `x` with a fresh Bernoulli(`q`) coin. Therefore

```text
Law(xi_x(s+delta) | E^-_{x,delta}, history before s)
 = Bernoulli(q),
```

and the terminal `xi_x` is independent of the pre-block history under this event. The reflected statement holds when `xi_{x+1}(s)=1`.

This is an exact local regeneration mechanism. It does not iterate to the source by itself: a future ring at the target can feed its value into its neighbors and make later reset hazards depend on that value, and the process can have blocks with no neighboring guard. A successful proof would need a quantitative shield/regeneration construction that regenerates a growing neighborhood, or a lower-tail theorem giving enough guard blocks together with control of the post-regeneration feedback.

## 5. Sixth-run mathematics: B24 extremal search fails without geometric normalization

For `u_A(t)=P_A(0 in A_t)`, the exact first derivative is

```text
u_A'(0)=(1_A(-1)+1_A(1)) (q-1_A(0)).
```

Thus among starts containing `0`, an isolated `0` is infinitesimally the slowest to move toward equilibrium; among starts not containing `0`, configurations having no occupied neighbor of `0` are infinitesimally the slowest.

More sharply, starting from the singleton `{R}`, `R>=1`, the first possible occupation of `0` needs `R` successive inward births. Hence

```text
P_{ {R} }(0 in A_t)
 = q^R t^R/R! + O(t^(R+1))   as t downarrow 0.
```

The leftmost-record process gives the nonasymptotic hitting bound

```text
P_{ {R} }(0 in A_t)
 <= P(Poisson(q t) >= R),
```

because each new inward record can occur only when the current nearest occupied site rings and its inward Bernoulli coin is one, a predictable intensity at most `q`.

Therefore for every fixed `t` and every `epsilon>0` one can choose `R` so large that `P_{ {R} }(0 in A_t)<epsilon`. There is no useful unnormalized extremal finite start for `|P_A(0 in A_t)-q|`: distance to the target is an essential parameter, exactly as allowed by the source-side constants. A future extremal reduction must freeze distance/span or factor out a finite-speed cost.

## 6. Exact remaining blocker

The cleanest unresolved theorem after six runs is still the singular dual statement

```text
for every q in (0,1), every finite nonempty A and x,
|P_A(x in A_t)-q| <= C_{A,x,q} e^{-c(q)t}.
```

Even that would settle only the single-infection cylinder basis unless it is combined with the deterministic-anchor/certificate gluing needed for arbitrary initial laws satisfying the source exponential-gap hypothesis.

The interpolation calculation sharpens the missing ingredient: the BABP route must control the genuine distance-two interaction operator

```text
H=sum_x xi_x (I-P_{x-1})(I-P_{x+1})
```

along the interpolating semigroup. The local-regeneration route must turn a one-site exact refresh word into a growing-space shield so that future self-feedback cannot reintroduce dependence.

The simplest unresolved case is already:

```text
A_0={0}; prove for every q>0 that
|P_{ {0} }(0 in A_t)-q| <= C_q e^{-c_q t}.
```

The closest solved analogues recovered in the source are: the DFP is exponentially ergodic for every bias parameter; BABP has powerful self/quasi-duality and product-initial-law convergence, while finite-infection convergence cited by the source is only known in a restricted bias range. Those analogues motivate a Q-specific quasi-duality but do not supply it.

## 7. Recommended future routes for a different owner

Do not restart the six R7-04 routes. The best fresh continuation would be one of:

1. derive a **Q-specific quasi-duality** to a uniformly exponentially ergodic edge process, analogous to BABP/DFP but incorporating simultaneous two-neighbor refresh;
2. prove a **growing-block perfect-refresh/shield theorem** that iterates the exact one-sided regeneration word and has exponential failure probability;
3. control the interpolation interaction `H` in a weighted local norm strongly enough that the Duhamel integral is integrable uniformly in the growing finite-speed cone.

Any result must still preserve the full source initial-law quantifier before `E_FAexp` can move.

## 8. R7-04 rotation state

This handoff ends D0027 research in R7-04 under the six-unchanged CLOSABLE rule. It does **not** mark the source KNOWN, PROVED or REFUTED, does not release another worker's claim, and does not edit shared `RESULTS/QUEUE/POSTED`.

The R7-04 slot remains enabled. Its next target state is **PENDING_ADMISSION**. The shard gate `sum(ord(c) for c in ID) mod 7 = 3` must be reapplied. A bounded same-run successor screen found no immediately lawful claim among the most obvious shard-valid queue entries: `I0112` is canonically claimed by R16, `I0004` is canonically claimed by P21, `I0047` has already been rejected by current queue screening as a fresh CLOSABLE successor because later work/source residuals make the queued scope unsafe, and `I0074` has repeated current-scope admission holds. These exclusions are not a claim that the entire shard is exhausted; the next run should continue source admission rather than steal or invent a target.
