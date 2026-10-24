Model actually running: **GPT-5.6 Sol. Reasoning level: UNVERIFIED** — this is **not GPT-6 at maximum**; no authenticated runtime model/effort telemetry or binding selector is exposed.

# C0117 — strict one-sided upper-tail refutation by a marked coupon-collector CLT

Target: Jian Ding, James R. Lee, Yuval Peres, *Cover times, blanket times, and majorizing measures*, Annals of Mathematics 175 (2012), Section 5, Question 5.2, printed p. 1466, DOI `10.4007/annals.2012.175.3.8`.

Owner: `R7-03`, native ID `6aabe7be74008191b526b109ee4e9e80`, canonical claim `operations/claims/C0117.md`.

Captured run-start master: `a67805ea67fa7f905e78f8aeb2c67dce5127ed4c`.
Fresh ownership/pre-artifact master: `33d97ce26d4927271639869338e291393c4ea8a8`.
Previous immutable report: `research7_2026-09-17/R7-03/runs/2026-09-19/2026-09-19T021803Z__report.md`, creation commit `44bfcf1977c7f3d6c3c0eb37cfac6b85c880656e`.
Previous construction artifact: `research7_2026-09-17/R7-03/artifacts/2026-09-19/2026-09-19T014200Z__C0117_clique_trap_counterexample_and_terminal_value_lemmas.md`, creation commit `fbe5b1409ab325cbca2ec89e8650273649665abf`.

Methods required by the preceding Section-I recovery diagnosis and used here: **B7 TAKE THE LIMIT / B27 SWAP THE QUANTIFIERS / B9 RANDOMIZE**.

Frozen metric: `beta_cert = 1/2 -> 1/2` (**NO NUMERICAL MOVEMENT**). The preceding construction already proved that every interpolation exponent `beta>1/2` is impossible, so the metric is sharp and cannot increase. The substantive movement here is different: the last unresolved source-semantic obligation, a strict one-sided upper-tail interpretation of the second clause of Question 5.2, is now directly refuted on the same graph family.

## 1. Source scope

The official DLP source states, after assuming

` t_cov(G_n) / t_hit(G_n) -> infinity, `

that Aldous proved qualitative concentration and then asks:

> Is the standard deviation of `tau_cov` bounded by the maximal hitting time `t_hit`? Furthermore, does `(tau_cov-t_cov)/t_hit` exhibit an exponential decay with constant rate?

The printed normalized expression has no absolute-value bars. The preceding R7-03 run therefore refused to infer from divergent variance alone that the strict one-sided upper-tail reading was false. This artifact removes that ambiguity mathematically.

The current bounded literature check, dated 2026-09-19, rechecked the official DLP text and the closest later results: Ding's geometric-mean-scale work, Zhai's 2018 general GFF exponential concentration theorem, Hermon's 2020 qualitative concentration characterization, Berestycki--Hermon--Teyssier's vertex-transitive Gumbel theorem, and their January 2026 stationary-hitting-time companion. None of those located sources states the unrestricted pure-`t_hit` conclusion asked here or this counterexample. This is negative evidence only and is not novelty certification.

## 2. The same simple unweighted graph family

For each integer `k>=2`, let `G_k` be the finite connected unweighted simple graph with:

- a center `s`;
- `k` pendant leaves `a_1,...,a_k` adjacent to `s`;
- a clique `Q={g,q_2,...,q_k}` of size `k`;
- one bridge edge `s-g`.

Write

`h_k = t_hit(G_k) = max_{x,y} E_x T_y`.

The preceding immutable artifact proves, by the commute-time/effective-resistance identity,

`h_k <= 6 k^2`,

and also proves

`t_cov(G_k)/h_k = Theta(log k) -> infinity`.

Thus this family lies in exactly the asymptotic regime immediately preceding DLP Question 5.2.

A completed trap excursion starts with a departure `s->g` and ends at the next return to `s`. Let its duration be `Y_k`. The preceding artifact gives the exact formulas

`mu_k := E Y_k = k^2-k+2`,

`sigma_k^2 := Var(Y_k) = (k-1)^2(k-2)+k^3(k-1)`

`                         = k^4-4k^2+5k-2`.

In particular, for all sufficiently large `k`,

`sigma_k^2 >= k^4/2`,

while `mu_k >= k^2/2` for every `k>=2`.

We now analyze the *positive* fluctuations of the random total trap time accumulated while the pendant leaves are collected.

---

# 3. B9 — RANDOMIZE: exact marked coupon-collector decomposition

Fix `r in {k-1,k}` specified pendant leaves that remain unvisited when the walk is at `s`. Let `Lambda_{k,r}` be the additional time, starting from `s`, until all those `r` leaves have been visited. We do **not** require the clique to be uncovered or covered in the definition of `Lambda_{k,r}`.

At every departure from `s`, the selected neighbor is uniform among the `k` leaves and `g`. Suppose `j` of the target leaves are still unvisited. Ignore departures to already visited/nontarget leaves. Among the remaining relevant departure types,

- a new target leaf is selected with conditional probability `j/(j+1)`;
- the trap edge `s-g` is selected with conditional probability `1/(j+1)`.

Let `N_j` be the number of trap departures before the next new target leaf is selected at this stage. By the iid departure sequence and the strong Markov/renewal property at the discovery of a new target,

`N_j ~ Geom0(p_j=j/(j+1))`,

and `N_1,...,N_r` are mutually independent. Here `Geom0(p)` counts failures before the first success. Its exact moments give

`E N_j = 1/j`,

`Var(N_j) = (j+1)/j^2 = 1/j + 1/j^2`,

`E N_j^3 = 1/j + 6/j^2 + 6/j^3 <= 13/j`.

Attach to the trap symbols iid marks `Y_{k,j,l}`, all distributed as `Y_k` and independent of the departure-category process. Define the trap-time contribution in stage `j` by

`Z_{k,j} = sum_{l=1}^{N_j} Y_{k,j,l}`

and the full trap-time contribution by

`S_{k,r} = sum_{j=1}^r Z_{k,j}`.

The variables `Z_{k,1},...,Z_{k,r}` are independent. The random-sum variance formula gives exactly

`Var(Z_{k,j}) = sigma_k^2/j + mu_k^2(1/j+1/j^2)`.

Consequently, with `H_r=sum_{j<=r}1/j` and `H_r^(2)=sum_{j<=r}1/j^2`,

`b_{k,r}^2 := Var(S_{k,r})`

` = (sigma_k^2+mu_k^2) H_r + mu_k^2 H_r^(2).`        (3.1)

For `r=k` or `k-1`,

`b_{k,r} ~ k^2 sqrt(2 log k)`.                              (3.2)

This is the fluctuation scale hidden by the cover-state martingale in the preceding runs.

---

# 4. B7 — TAKE THE LIMIT: a Lyapunov CLT for the marked trap sum

We prove a genuine central limit theorem for `S_{k,r}`. The only nontrivial point is a uniform third-moment estimate.

## Lemma 4.1. `E Y_k^3 = O(k^6)`.

### Proof

Use the exact representation from the preceding artifact. At the gateway `g`, let `F` be the number of failed attempts to exit to `s` before the successful attempt. Then

`F ~ Geom0(1/k)`.

On each failure the walk takes one step from `g` into `Q\{g}` and then returns to `g`. If `G` is the hitting time of `g` from a fixed non-gateway clique vertex, then

`G ~ Geom1(1/(k-1))`.

Put `D=1+G`. With iid copies `D_i`, independent of `F`,

`Y_k = 2 + sum_{i=1}^F D_i`.

The raw third moments of these geometric variables satisfy

`E F^3 = O(k^3)`,   `E D^3 = O(k^3)`.

For nonnegative numbers,

`(sum_{i=1}^m d_i)^3 <= m^2 sum_{i=1}^m d_i^3`.

Conditioning on `F` therefore gives

`E[(sum_{i=1}^F D_i)^3 | F] <= F^3 E D^3`.

Taking expectations yields `O(k^6)`. Adding the deterministic `2` changes only the universal constant. QED.

## Lemma 4.2. Lyapunov condition.

For `r in {k-1,k}`,

`sum_{j=1}^r E|Z_{k,j}-E Z_{k,j}|^3 / b_{k,r}^3 -> 0`.

### Proof

Again using nonnegativity,

`Z_{k,j}^3 <= N_j^2 sum_{l=1}^{N_j} Y_{k,j,l}^3`.

After conditioning on `N_j`,

`E Z_{k,j}^3 <= E N_j^3 * E Y_k^3 <= C k^6/j`.

Also `|X-EX|^3 <= (X+EX)^3 <= 4(X^3+(EX)^3) <= 8 E[X^3]` after expectation for any nonnegative `X`. Hence

`E|Z_{k,j}-E Z_{k,j}|^3 <= C' k^6/j`.

Summing over `j<=r` gives `O(k^6 log k)`. By (3.1)--(3.2),

`b_{k,r}^3 = Theta(k^6 (log k)^(3/2))`.

The ratio is therefore `O((log k)^(-1/2)) -> 0`. QED.

By the Lyapunov triangular-array central limit theorem,

`(S_{k,r}-E S_{k,r})/b_{k,r} => N(0,1)`              (4.1)

uniformly for the two possibilities `r=k,k-1`.

## 4.3. The ordinary leaf time is negligible on the CLT scale

Delete all trap symbols from the departure sequence. The remaining leaf labels are iid uniform on the `k` leaves. Let `L_{k,r}` be the number of leaf departures required to collect the `r` target labels. When `j` targets remain, the next success among leaf departures has probability `j/k`, so

`E L_{k,r} = k H_r`,

`Var(L_{k,r})`

` = sum_{j=1}^r (1-j/k)/(j/k)^2`

` <= k^2 sum_{j>=1} 1/j^2`

` <= (pi^2/6) k^2`.                                      (4.2)

Every nonfinal leaf excursion has duration two (`s->a->s`), while the final target is covered upon the first step `s->a`. Thus pathwise

`Lambda_{k,r} = S_{k,r} + 2 L_{k,r} - 1`.                 (4.3)

No independence between `S_{k,r}` and `L_{k,r}` is required. Equation (4.2) and `b_{k,r}=Theta(k^2 sqrt(log k))` imply

`2(L_{k,r}-E L_{k,r})/b_{k,r} -> 0`

in `L^2`, hence in probability. Combining (4.1)--(4.3) with Slutsky's theorem gives

`(Lambda_{k,r}-E Lambda_{k,r})/b_{k,r} => N(0,1)`.        (4.4)

The mean is also exact:

`E Lambda_{k,r}`

` = mu_k H_r + 2 k H_r - 1`

` = (k^2+k+2) H_r - 1`.                                  (4.5)

---

# 5. Transfer the CLT to the source's worst-start centering

For each `k`, choose a vertex `x_k` attaining the source convention

`t_cov(G_k)=E_{x_k} tau_cov`.

Let `T_s` be the first hitting time of the center `s`. If `x_k` is a pendant leaf, exactly that one pendant leaf has already been visited before the first arrival at `s`, so put `r_k=k-1`. If `x_k=s` or `x_k` lies in the clique, no pendant leaf has been visited before the first hit of `s`, so put `r_k=k`.

By the strong Markov property at `T_s`, define

`V_k = T_s + Lambda_{k,r_k}`,

where the future `Lambda` process starts fresh from `s`. Pathwise,

`tau_cov >= V_k`,                                              (5.1)

because the graph cannot be covered before all remaining pendant leaves are visited.

## Lemma 5.1. `T_s` is negligible on the `b_{k,r_k}` scale.

Since `E_z T_s <= h_k` for every state `z`, Markov's inequality and the strong Markov property at deterministic blocks yield

`P_z(T_s > 2m h_k) <= 2^{-m}`,  `m>=0`.

Hence `E_z T_s^2 = O(h_k^2)=O(k^4)` uniformly in `z`. Because

`b_{k,r_k}^2 = Theta(k^4 log k)`,

we have

`(T_s-E T_s)/b_{k,r_k} -> 0`

in `L^2`. Combining with (4.4),

`(V_k-E V_k)/b_{k,r_k} => N(0,1)`.                         (5.2)

The remaining issue is that `E V_k` need not equal `t_cov`. We now show their difference is negligible compared with `b_{k,r_k}`.

---

# 6. Centering lemma: the clique is covered by leaf-completion time with probability `1-o(1)`

Let `B_k` be the event that the clique `Q` is not fully covered by time `V_k`.

The preceding artifact established the following bound for a trap excursion begun at `g`. Put

`t_0=ceil(4(k-1) log k)`.

Couple the internal trajectory before bridge exit to simple random walk on `K_k`. A union bound gives

`P(K_k not covered by t_0) <= k^{-3}`.

The expected number of visits/opportunities at `g` through that time is at most `2+4 log k`, and each opportunity exits across the bridge with probability `1/k`. Therefore

`delta_k := P(a trap excursion returns to s before covering Q)`

` <= k^{-3} + (2+4 log k)/k`

` = O(log k/k)`.                                           (6.1)

Now consider the process after `T_s`. In the departure sequence restricted to the symbols consisting of the trap and the `r_k` still-unvisited target leaves, all `r_k+1` symbols are symmetric. The event that no trap appears before all `r_k` target labels have appeared is exactly the event that the trap symbol is the last of these `r_k+1` symbols to make its first appearance. Hence

`P(no trap before all target leaves are collected) = 1/(r_k+1)`. (6.2)

If at least one trap occurs and the first trap excursion covers `Q`, then `B_k` is impossible. Combining (6.1)--(6.2),

`P(B_k) <= 1/(r_k+1) + delta_k = O(log k/k)`.              (6.3)

This bound remains valid if `x_k` starts inside the clique, since prior clique visits can only make later clique coverage easier.

Define the nonnegative centering defect

`d_k := t_cov(G_k)-E V_k`

`     = E_{x_k}(tau_cov-V_k)`,

where the equality uses the worst-start choice of `x_k` and (5.1). On `B_k^c`, all graph vertices are covered at time `V_k`, so `tau_cov=V_k`. On `B_k`, after `V_k` the conditional expected time to cover the remaining clique vertices is at most a fresh full-graph cover time from the current vertex, hence at most `t_cov(G_k)`. Therefore

`0 <= d_k <= P(B_k) t_cov(G_k)`.                            (6.4)

Matthews' bound and `|V(G_k)|=2k+1` give

`t_cov(G_k) <= h_k H_{2k} = O(k^2 log k)`.                 (6.5)

Equations (6.3)--(6.5) imply

`d_k = O(k log^2 k) = o(k^2 sqrt(log k)) = o(b_{k,r_k}).`  (6.6)

Thus the source's exact centering differs from the explicit leaf-completion centering by a negligible amount on the fluctuation scale.

---

# 7. Main theorem: a constant positive upper tail at a growing `t_hit`-normalized deviation

## Theorem 7.1

For the graph family `G_k`, choose any worst-mean starting vertex `x_k` satisfying

`E_{x_k} tau_cov = t_cov(G_k)`.

Then

`liminf_{k->infinity} P_{x_k}(`

`  (tau_cov-t_cov(G_k))/t_hit(G_k) >= (1/40) sqrt(log k)`

`) >= 1-Phi(1/2) > 0.30`,                                  (7.1)

where `Phi` is the standard normal distribution function.

### Proof

Write `b_k=b_{k,r_k}`. By (5.2),

`P(V_k-EV_k >= b_k/2) -> 1-Phi(1/2)`.

By (6.6), for all sufficiently large `k`, `d_k<=b_k/4`. On the event above, using `tau_cov>=V_k`,

`tau_cov-t_cov`

` >= V_k-(E V_k+d_k)`

` >= b_k/4`.                                                (7.2)

It remains to compare `b_k` with `h_k`. From (3.1), for large `k`,

`b_k^2 >= (sigma_k^2+mu_k^2) H_{k-1}`

`      >= (3/4) k^4 H_{k-1}`.

For all sufficiently large `k`, `H_{k-1}>=(1/2)log k`, so

`b_k >= sqrt(3/8) k^2 sqrt(log k)`.

Since `h_k<=6k^2`,

`(b_k/4)/h_k >= [sqrt(3/8)/24] sqrt(log k)`

`              > (1/40) sqrt(log k)`.                      (7.3)

Equations (7.2)--(7.3) prove (7.1). QED.

The theorem is stronger than needed for the strict one-sided tail question: at a deviation level that diverges as `sqrt(log k)` in units of `t_hit`, the positive tail probability stays bounded away from zero.

---

# 8. B27 — SWAP THE QUANTIFIERS: direct contradiction to every constant-rate upper exponential tail

Suppose, contrary to the strictest plausible reading of DLP Question 5.2, that there exist universal constants `A,a>0` such that for every finite connected graph in the stated regime, the relevant worst-start walk, and every `u>=0`,

`P((tau_cov-t_cov)/t_hit >= u) <= A exp(-a u)`.             (8.1)

Fix the arbitrary constants `A,a` and choose the already-defined `G_k`. Set

`u_k=(1/40)sqrt(log k)`.

By Theorem 7.1,

`liminf P((tau_cov-t_cov)/t_hit >= u_k) > 0.30`,

whereas

`A exp(-a u_k) -> 0`.

This contradicts (8.1). Therefore:

**There do not exist universal constants `A,a>0` giving a constant-rate exponential upper-tail bound at the pure `t_hit` scale for all graphs in the DLP regime.**

This directly refutes the strict one-sided reading; no appeal to variance or to an implicit two-sided interpretation is needed.

Moreover, because `x_k` is a worst-mean start and Theorem 7.1 gives a constant-probability positive deviation of order `h_k sqrt(log k)`, it also immediately implies

`Var_{x_k}(tau_cov) >= c h_k^2 log k`

for a universal `c>0` and all large `k`. Thus the same one-sided theorem gives an independent route to the already-written conclusion

`SD_{x_k}(tau_cov)/t_hit(G_k) -> infinity`.

Together with `t_cov/h_k -> infinity`, both clauses of the source question are refuted by one explicit family under the source's worst-mean centering convention.

---

# 9. Status, prior art, and remaining protocol obligations

## Mathematical source verdict

At theorem level, the source endpoint is now **REFUTED**:

1. `t_cov(G_k)/t_hit(G_k) -> infinity`;
2. for a source worst-mean start, `SD(tau_cov)/t_hit -> infinity`, refuting universal `O(t_hit)` fluctuations;
3. even the strict one-sided positive tail satisfies (7.1), refuting any universal constant-rate exponential decay at the `t_hit` scale.

The frozen interpolation metric remains numerically `beta_cert=1/2`, because the earlier run already established that `1/2` is the sharp unrestricted exponent; this run closes a separate mandatory source obligation rather than changing that number.

## Current bounded literature check, 2026-09-19

Checked/rechecked:

- DLP official source, Section 5 Question 5.2, DOI `10.4007/annals.2012.175.3.8`;
- Jian Ding, *Asymptotics of cover times via Gaussian free fields: bounded-degree graphs and general trees*, arXiv `1103.4402`;
- Alex Zhai, *Exponential concentration of cover times*, arXiv `1407.7617`, Electronic Journal of Probability 23 (2018), DOI `10.1214/18-EJP149`;
- Jonathan Hermon, *A Spectral Characterization for Concentration of the Cover Time*, Journal of Theoretical Probability 33 (2020), DOI `10.1007/s10959-019-00946-5`;
- Nathanaël Berestycki, Jonathan Hermon, Lucas Teyssier, *On the universality of fluctuations for the cover time*, arXiv `2202.02255`, vertex-transitive bounded-degree scope;
- Berestycki--Hermon--Teyssier, *Stationary hitting times on vertex-transitive graphs*, arXiv `2601.03864`, January 7, 2026.

Bounded exact-phrase and mechanism searches did not locate a paper giving this unrestricted clique-trap refutation of DLP Question 5.2. **Negative search results do not certify novelty or openness.** A dedicated citation-level prior-art closure review remains required before any publication claim.

## Protocol status

This artifact is a full written mathematical proof, but repository closure is **not yet protocol-complete**. Still missing:

- dedicated prior-art closure review at exact claim scope;
- actual P26 independent full-proof audit;
- one distinct OTHER-track independent full-proof audit;
- self-contained `paper_<name>/` folder with proof/source-scope README and useful support material.

No self-check is counted as an independent audit. No shared `RESULTS.md`, `QUEUE.md`, `POSTED.md`, peer report, scheduler, email, Drive destination, or public page is modified by this artifact.