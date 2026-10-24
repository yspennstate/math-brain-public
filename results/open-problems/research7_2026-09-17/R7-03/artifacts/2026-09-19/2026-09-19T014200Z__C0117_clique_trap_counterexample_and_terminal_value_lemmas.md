Model actually running: **GPT-5.6 Sol. Reasoning level: UNVERIFIED** — this is **not GPT-6 at maximum**; no authenticated runtime model/effort telemetry or binding selector is exposed.

# C0117 — clique-trap counterexample, sharpness of the geometric-mean exponent, and terminal-value lemmas

Target: Jian Ding, James R. Lee, Yuval Peres, *Cover times, blanket times, and majorizing measures*, Annals of Mathematics 175 (2012), Section 5, Question 5.2, printed p. 1466, DOI `10.4007/annals.2012.175.3.8`.

Run-start master snapshot: `c102e9b2dcee04a7d0fe698fd7048f62e6df023b`.
Fresh pre-write master: `07dad0a9301d7b73e77be22c724207a41ca719b0`.
Owner: `R7-03`, native ID `6aabe7be74008191b526b109ee4e9e80`, canonical claim `operations/claims/C0117.md`.

## Source scope and verdict of this artifact

Ding--Lee--Peres ask, after recalling Aldous's qualitative concentration theorem in the regime `t_cov/t_hit -> infinity`, whether the standard deviation of `tau_cov` is bounded on the maximal-hitting-time scale and, furthermore, whether `(tau_cov-t_cov)/t_hit` has exponential decay with constant rate.

This artifact gives a family of finite connected **unweighted simple graphs** for which

` t_cov/t_hit -> infinity `

but

` SD_x(tau_cov)/t_hit -> infinity `

for **every starting vertex** `x`. Thus the intended universal `O(t_hit)` reading of the first clause is REFUTED, not merely the coefficient-one reading refuted by the preceding finite graph. Moreover, any standard universal two-sided exponential-tail reading

` P_x(|tau_cov-t_cov| >= u t_hit) <= A exp(-a u) `

with constants `A,a>0` is impossible, because such a bound would force a uniform second-moment bound while the normalized variance below diverges.

The same family shows that the existing geometric-mean exponent is optimal: for every fixed `beta>1/2` there is no universal constant `C_beta` such that

` SD(tau_cov) <= C_beta t_hit^beta t_cov^(1-beta) `

on all finite connected graphs. Therefore the frozen R7-03 metric `beta_cert=1/2` does not numerically move, but this run proves it is a sharp endpoint.

No novelty claim is made solely from negative searches. Independent source-level audits and the required paper package do not yet exist, so protocol closure is not asserted here.

---

# Method B22 — read the old loss: a sharper terminal-set estimate inside Aldous's block proof

Aldous, *Threshold Limits for Cover Times* (J. Theoret. Probab. 1991), decomposes a finite irreducible chain into iid return blocks `S_1,S_2,...` from a state `s`. Let

- `R_i=S_1 union ... union S_i`,
- `C=min{i:R_i=S}` be the block cover time,
- `B_i=S\R_i` the remaining set,
- `T=B_{C-1}` the terminal set,
- `c(B)=E C(B)` for a fresh iid block process covering `B`, and
- `eta=min_j P_s(T_j<xi_1)`, where `xi_1` is the first return time to `s`.

Aldous proves, as equation (24), that for every deterministic `B subset S`,

` P(B subset S_1) <= 4/[eta c(B)^2]. `

His Proposition 6 then obtains `E c(T) <= 4 (EC)^(3/4) eta^(-1/4)` by truncating at a deterministic `K`, union-bounding over `i<=K`, applying Markov to `C>K`, and optimizing twice.

There is a direct survival-weighted summation that removes that truncation loss.

## Lemma B22.1 (terminal-value tail)

For every `u>0`,

` P(c(T)>=u) <= 4 EC/(eta u^2). `

### Proof

For `i>=1`, on `{C>i-1}` the last uncovered set just before block `i` is `B_{i-1}`. The event `{C=i}` is exactly `{C>i-1, B_{i-1} subset S_i}`. Since `S_i` is independent of `F_{i-1}=sigma(S_1,...,S_{i-1})`, equation (24) applies conditionally, pointwise in the realized `B_{i-1}`. Therefore

`P(c(T)>=u)`

`= sum_{i>=1} E[ 1_{C>i-1} 1_{c(B_{i-1})>=u} P(B_{i-1} subset S_i | F_{i-1}) ]`

`<= [4/(eta u^2)] sum_{i>=1} P(C>i-1)`

`= 4 EC/(eta u^2)`.

The last identity is the standard tail-sum formula for the positive integer-valued variable `C`. QED.

## Corollary B22.2 (improved terminal expectation)

` E c(T) <= 4 sqrt(EC/eta). `

### Proof

Monotonicity gives `0<=c(T)<=c(S)=EC`. Put `a=4EC/eta`. By the lemma,

`E c(T) = integral_0^{EC} P(c(T)>=u) du`

`<= integral_0^{EC} min(1,a/u^2) du`.

If `sqrt(a)<=EC`, splitting at `sqrt(a)` gives at most `2sqrt(a)=4sqrt(EC/eta)`. If `sqrt(a)>EC`, the trivial bound `E c(T)<=EC` is already at most `4sqrt(EC/eta)` because `eta EC<4` in that case. QED.

Combining this with Aldous Theorem 1(b),

` Var(C)/(EC)^2 <= kappa E c(T)/EC, `

gives the sharper block-level estimate

` Var(C)/(EC)^2 <= 4 kappa / sqrt(eta EC). `

This is real progress inside the 1991 mechanism, but it does **not** prove DLP Question 5.2. Return-block durations carry an independent fluctuation channel, and Method B24 below makes that obstruction decisive.

---

# Method B12 — the conserved terminal-value budget

For the abstract iid-set cover process, define `B_i=S\R_i` and `c(empty)=0`. The dynamic-programming identity is

` c(B)=1+E[c(B\S_1)] `

for every nonempty `B`.

## Lemma B12.1 (value martingale)

` M_i = (i wedge C) + c(B_{i wedge C}) `

is a martingale, with `M_0=EC` and `M_C=C`.

### Proof

If `i>=C`, the process is stopped. If `i<C`, then conditional on `F_i`, the next block is fresh and

`E[M_{i+1}|F_i]=i+1+E[c(B_i\S_{i+1})|F_i]=i+c(B_i)=M_i`.

QED.

Let

` D_i = c(B_i)-c(B_{i+1}) `

for `i<C`. Then pathwise

` sum_{i=0}^{C-1} D_i = c(S)-c(empty)=EC, `

while the dynamic-programming identity gives

` E[D_i|F_i]=1 `

on `{i<C}`. Consequently

` C-EC = sum_{i=0}^{C-1} (1-D_i). `

For finite irreducible chains the block cover time has finite moments; stopping first at `C wedge n`, using orthogonality of martingale increments, and then letting `n->infinity` yields the exact predictable-quadratic-variation identity

` Var(C) = E sum_{i=0}^{C-1} E[(D_i-1)^2 | F_i]. `

Thus `c(B_i)` is an intrinsic conserved budget for the **number of blocks**. The counterexample below shows why this alone cannot settle the source: one can keep the block/coupon geometry benign while making already-covered detours have variance of order `t_hit^2` and repeat about `log k` times before the last coupon is found.

---

# Method B24 — extremal construction: a star with a clique delay trap

For each integer `k>=2`, define the unweighted simple graph `G_k` as follows.

- There is a center `s`.
- Attach `k` pendant leaves `a_1,...,a_k` to `s`.
- Take a clique `Q={g,q_2,...,q_k}` of size `k`.
- Add one bridge edge `s-g`, and no other edge between `Q` and the star.

Call `Q` the **delay trap**. Let `tau_cov` be simple-random-walk cover time and

` h_k=t_hit(G_k)=max_{x,y} E_x T_y. `

The point is that each visit from `s` into the clique costs a random time of order `k^2`, while a specified ordinary leaf is hit after only order one such trap visits on average. Hence `h_k=Theta(k^2)`. Covering all `k` ordinary leaves, however, takes coupon-collector order `k log k` departures from `s`, and during that period the walk makes order `log k` independent trap excursions. Their variances add, producing standard deviation `k^2 sqrt(log k)`.

## Step 1. Uniform `O(k^2)` maximal hitting time

The number of edges is

` m_k = k + 1 + k(k-1)/2 = (k^2+k+2)/2. `

The effective-resistance diameter is at most `2+2/k`: two ordinary leaves have resistance `2`; a leaf and `g` have resistance `2`; a leaf and a non-gateway clique vertex have resistance `1+1+2/k`; and clique pairs have resistance `2/k`. The components hanging from the articulation point `g` carry no current when resistance is measured between two clique vertices.

By the commute identity

` H(x,y)+H(y,x)=2 m_k R_eff(x,y), `

we obtain

` h_k <= 2m_k(2+2/k) <= 6 k^2 `

for every `k>=2`.

## Step 2. Exact variance of one completed trap excursion

Condition on a departure from `s` choosing the trap edge. Let `Y_k` be the time from that departure at `s` until the next return to `s`; thus one step moves `s` to `g` and then the walk must hit `s` from `g`.

At `g` the degree is `k`. Each visit to `g` exits to `s` with probability `1/k`. On a failed exit attempt, the walk takes one step to a non-gateway clique vertex and then returns to `g`. From any non-gateway clique vertex, the hitting time `G` of `g` is geometric on `{1,2,...}` with success probability `1/(k-1)`. Hence

` E G = k-1,`

` Var(G)=(k-2)(k-1). `

Let `F` be the number of failed visits to `g` before the successful exit. Then `F` is geometric-on-failures with success probability `1/k`, so

` E F=k-1,`

` Var(F)=k(k-1). `

With iid copies `G_j`, independent of `F`,

` T_{g->s}=1+sum_{j=1}^F (1+G_j). `

Writing `D=1+G`, we have `ED=k` and `Var(D)=(k-2)(k-1)`. The random-sum variance formula gives

` Var(T_{g->s})`

`= (k-1)^2(k-2) + k^3(k-1)`

`>= (1/2) k^4. `

Therefore

` E Y_k = k^2-k+2, `

` Var(Y_k) >= k^4/2. `

This exact computation is the fluctuation reservoir.

## Step 3. The clique is already covered before the repeated delays matter

We need a positive-probability stopping state at which the clique has been covered but a linear number of ordinary leaves remain.

First consider a trap excursion started at `g`. Couple its internal motion, until exit, to simple random walk on `K_k`. Put

` t_0 = ceil(4(k-1) log k). `

For a fixed target vertex of `K_k`, whenever it has not yet been hit, the next step hits it with probability `1/(k-1)`. Hence a union bound gives

` P(K_k is not covered by time t_0) <= k exp[-t_0/(k-1)] <= k^{-3}. `

In the coupled `K_k` walk started from `g`, for every `t>=1`,

` P(X_t=g) <= 1/(k-1). `

Thus the expected number of opportunities to take the bridge exit during the first `t_0` internal steps is at most `1+t_0/(k-1) <= 2+4 log k`. Each such opportunity exits with probability `1/k`. Therefore

` P(exit before the clique is covered) <= k^{-3} + (2+4 log k)/k = o(1). `

Now start from an arbitrary vertex `x` of `G_k`, and first run until the walk is at `s`. Before this moment at most one ordinary leaf has been visited: one only if `x` itself was an ordinary leaf. From that visit to `s`, let `N` be the number of ordinary-leaf excursions before the first trap excursion. At each return to `s`, the trap is selected with probability `1/(k+1)`, so

` P(N <= floor(k/2)) = 1 - [k/(k+1)]^{floor(k/2)+1} -> 1-e^{-1/2}. `

On this event, at the start of the first trap excursion at most `1+floor(k/2)` ordinary leaves have been covered. If that trap excursion covers the clique before returning to `s`, then at its return time `sigma` the whole clique is covered and at least

` r >= k-1-floor(k/2) >= k/3 `

ordinary leaves remain for all sufficiently large `k`.

Let `E_k` denote this event. By the preceding two bounds and the strong Markov property, uniformly over the initial vertex `x`,

` inf_x P_x(E_k) >= 1/4 `

for all sufficiently large `k`.

## Step 4. Exact coupon count of later trap excursions

On `E_k`, at time `sigma` the walk is at `s`, all clique vertices are already covered, and `r>=k/3` specified ordinary leaves remain unvisited. From this point, the cover time ends exactly when those `r` leaf labels have all been selected on departures from `s`.

Let `N_r` be the number of departures from `s` needed to see all `r` remaining target leaves. When `j` target leaves remain, the chance that the next departure finds a new one is `j/(k+1)`, hence

` E N_r = (k+1) H_r. `

Let `J_r` be the number of trap departures among these `N_r` departures. The departure categories are iid uniform among the `k+1` neighbors of `s`; `N_r` is a stopping time for this category sequence. Wald's identity therefore gives

` E J_r = [1/(k+1)] E N_r = H_r. `

Conditional on the entire departure-category sequence, all ordinary-leaf excursions have deterministic duration `2` except the final one, of duration `1`, while the `J_r` trap excursions have iid durations distributed as `Y_k`, independent of the category sequence. If `R_r` is the additional time required after `sigma`, the law of total variance yields

` Var(R_r) >= E[J_r] Var(Y_k) = H_r Var(Y_k) >= (1/2) k^4 H_r. `

## Step 5. Divergent normalized variance, uniformly in the start

Condition on the stopped history `F_sigma`. On `E_k`, the past duration is fixed and the remaining cover time has law `R_r` for some `r>=k/3`. Therefore the conditional-variance formula gives, for every initial vertex `x`,

` Var_x(tau_cov)`

`>= E_x[ 1_{E_k} Var_x(tau_cov | F_sigma) ]`

`>= P_x(E_k) * (1/2) k^4 H_{floor(k/3)}.`

For all sufficiently large `k`, `P_x(E_k)>=1/4` and `H_{floor(k/3)} >= (1/2) log k`, so

` Var_x(tau_cov) >= (1/16) k^4 log k, `

and hence

` SD_x(tau_cov) >= (1/4) k^2 sqrt(log k). `

Since `h_k<=6k^2`,

` SD_x(tau_cov)/h_k >= sqrt(log k)/24 -> infinity. `

This is uniform over **every** starting vertex. In particular it applies to a vertex attaining the worst-start expectation `t_cov`.

## Step 6. The family lies in the exact Aldous/DLP concentration regime

Still on `E_k`, the expected future time contributed by later trap excursions alone is

` E[J_r] E[Y_k] = H_r (k^2-k+2). `

Therefore, for any start and in particular for the worst start,

` t_cov(G_k) >= c k^2 log k `

for a universal `c>0` and all large `k`. Together with `h_k<=6k^2`,

` t_cov(G_k)/h_k -> infinity. `

Conversely Matthews' general bound gives, with `|V(G_k)|=2k+1`,

` t_cov(G_k) <= h_k H_{2k} = O(h_k log k). `

Thus in fact

` t_cov(G_k)/h_k = Theta(log k). `

So this is not a counterexample obtained by leaving the regime stated immediately before DLP Question 5.2.

## Step 7. The geometric-mean exponent `1/2` is optimal

The preceding bounds imply

` SD(tau_cov) >= c h_k sqrt(log k) `

and

` t_cov <= C h_k log k. `

For any fixed `beta>1/2`,

` h_k^beta t_cov^(1-beta) <= C_beta h_k (log k)^(1-beta). `

Hence

` SD(tau_cov) / [h_k^beta t_cov^(1-beta)] >= c_beta (log k)^(beta-1/2) -> infinity. `

Therefore no source-compatible universal interpolation bound can have exponent strictly larger than `1/2`. The existing `beta=1/2` geometric-mean scale is exponent-sharp on the full class of finite connected graphs.

## Step 8. Consequence for the exponential-tail clause

Suppose the second DLP clause were interpreted in the standard universal two-sided form: there are constants `A,a>0` such that for all graphs, all starts in the relevant convention, and all `u>=0`,

` P(|tau_cov-t_cov| >= u t_hit) <= A e^{-a u}. `

Then, writing `Z=(tau_cov-t_cov)/t_hit`,

` E Z^2 = integral_0^infinity 2u P(|Z|>=u) du <= 2A/a^2. `

But `E Z^2 >= Var(tau_cov)/t_hit^2`, and the latter diverges like at least a constant times `log k` on `G_k`. Contradiction. Thus the standard universal constant-rate exponential-tail interpretation is also false.

---

# Literature/status check dated 2026-09-19

Primary source checked directly:

- Ding--Lee--Peres, Annals of Mathematics 175 (2012), Section 5 Question 5.2, DOI `10.4007/annals.2012.175.3.8`, official PDF `https://annals.math.princeton.edu/wp-content/uploads/annals-v175-n3-p08-p.pdf`.

Follow-up and neighboring results checked:

- D. Aldous, *Threshold Limits for Cover Times* (J. Theoret. Probab. 1991): qualitative concentration under `t_cov/t_hit -> infinity`, and the return-block/terminal-set proof analyzed above.
- J. Ding, *Asymptotics of cover times via Gaussian free fields: bounded-degree graphs and general trees*, Ann. Probab.; arXiv `1103.4402`: geometric-mean-scale concentration for trees.
- A. Zhai, *Exponential concentration of cover times*, EJP; arXiv `1407.7617`: general GFF-based exponential concentration at the generic geometric-mean-plus-hitting-time scale, not the pure `t_hit` scale.
- J. Hermon, *A Spectral Characterization for Concentration of the Cover Time*, J. Theoret. Probab. 33 (2020), DOI `10.1007/s10959-019-00946-5`: qualitative concentration criteria on transitive and broader reversible classes.
- D. Aldous, later compact-covering work was checked for reuse of the terminal-set method; it does not supply the source endpoint located here.

Fresh bounded searches on 2026-09-19 for the exact DLP question, the phrases `standard deviation` / `maximal hitting time`, and trap/clique/star cover-time counterexamples did not return a paper resolving Question 5.2 by this construction. **This is negative evidence only and does not certify novelty.** A dedicated citation-level prior-art review remains mandatory before publication.

Repository prior work recovered and not counted as new: canonical attempt `C0117-A001`; R7-03's preceding finite coefficient-one witness and unvisited-set bridge; R7-03's exact spider/Gumbel calibration and dumbbell late-cluster obstruction.

---

# What is proved and what is not

**Written theorem-level proof in this artifact:** the clique-trap-star family `G_k` satisfies `t_cov/t_hit -> infinity` and `inf_x SD_x(tau_cov)/t_hit -> infinity`; consequently the intended `O(t_hit)` standard-deviation clause is false, every interpolation exponent `beta>1/2` is impossible, and any universal two-sided constant-rate exponential tail at `t_hit` scale is false.

**Secondary proved lemmas:** the sharpened Aldous terminal-value tail/expectation estimate and the exact terminal-value martingale/quadratic-variation identity.

**Not yet protocol-complete:** no P26 audit, no distinct OTHER-track independent audit, no paper package, and no dedicated novelty certification. No shared `RESULTS.md`, `QUEUE.md`, or `POSTED.md` is edited by R7-03.
