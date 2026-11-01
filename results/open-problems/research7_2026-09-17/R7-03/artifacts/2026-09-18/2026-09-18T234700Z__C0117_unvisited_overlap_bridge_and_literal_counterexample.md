Model actually running: **GPT-5.6 Sol. Reasoning level: UNVERIFIED** — this is **not GPT-6 at maximum**; no authenticated runtime model/effort telemetry or binding selector is exposed.

# C0117 — unvisited-set bridge, the exact missing correlation estimate, and a literal-constant counterexample

Source: Jian Ding, James R. Lee, Yuval Peres, *Cover times, blanket times, and majorizing measures*, Ann. Math. 175 (2012), Section 5, Question 5.2.

Status of this artifact: **PARTIAL**. It does not settle the source's constant-rate exponential-tail question and it does not prove `SD(tau_cov)=O(t_hit)` in full generality. It does give (i) a complete structural reduction to late-vertex correlations and (ii) an exact seven-vertex counterexample to the literal coefficient-one reading `SD(tau_cov) <= t_hit`.

## 0. Source-scope correction to the admission paraphrase

The primary source literally asks: “Is the standard deviation of `tau_cov` bounded by the maximal hitting time `t_hit`?” The admission record paraphrased this as existence of a universal constant in `SD=O(t_hit)`, because that is the scale-level interpretation suggested by the following tail question. That paraphrase is **not logically identical** to the printed wording.

Accordingly this artifact keeps two readings separate:

1. **Literal coefficient-one reading:** `SD(tau_cov) <= t_hit`.
2. **Scale reading:** `SD(tau_cov) <= C t_hit` for a universal finite `C`, consistent with the phrase “at the `t_hit` scale” and with the subsequent constant-rate tail question.

The exact finite certificate below refutes (1). It does **not** refute (2). This distinction must be retained in every later source-status statement.

## 1. Idea before code

The generic GFF/Ray–Knight concentration machinery controls the cover time on the geometric-mean scale `sqrt(t_cov t_hit)`. To reach the sharper `t_hit` scale one must exploit something that disappears after replacing the unvisited set by only the maximum of a Gaussian field.

The natural object is therefore not the cover time itself but

`U_t := number of vertices unvisited at time t`.

A one-vertex survival probability contracts universally on `t_hit` blocks. Thus the only way a `t_hit`-scale theorem can fail to follow immediately is that *late vertices survive in correlated clusters*. This suggests isolating the two-point/factorial-moment term of `U_t` as the missing object.

The three Section-B moves in this run are:

- **B18 — say it in another language:** rewrite cover-time concentration as decay of the unvisited-set process.
- **B11 — dualize:** replace the hitting-time maximum by first and second factorial moments of `U_t`, making the obstruction a correlation inequality.
- **B25 — count the same thing twice:** express `E[U_t^2]` both as a state-space moment and as a sum of pair-survival probabilities, and use the exact state-space recursion on a finite graph to test the source's literal coefficient-one bound.

These differ from the immediately preceding R7-03 triple B2/B6/B30.

## 2. Universal `2 t_hit` contraction of every unvisited vertex

Let `G=(V,E)` be a finite connected graph and let `(X_t)` be discrete-time simple random walk. For a vertex `v`, write

`T_v := inf{t >= 0 : X_t=v}`

and let

`h := t_hit = max_{x,v} E_x T_v`.

For a fixed starting state, define

`U_t := sum_{v in V} 1_{T_v>t}`.

### Lemma 2.1 (conditional block contraction)

For every deterministic time `t`, integer `k>=0`, and vertex `v`,

`P(T_v > t+2kh | F_t) <= 2^{-k} 1_{T_v>t}`.

Consequently,

`E[U_{t+2kh} | F_t] <= 2^{-k} U_t`

and, writing `m(t)=E U_t`,

`m(t+2kh) <= 2^{-k} m(t)`.

### Proof

If `T_v<=t`, the conditional probability on the left is zero. On `{T_v>t}`, the Markov property at time `t` gives a fresh walk from `X_t`. By the definition of `h`,

`E_{X_t} T_v <= h`.

Markov's inequality therefore gives

`P_{X_t}(T_v>2h) <= 1/2`.

Apply the strong Markov property successively at times `t+2jh`, `j=0,...,k-1`. Each block contributes a conditional survival factor at most `1/2`, proving the vertexwise inequality. Sum over `v` and use conditional linearity of expectation. Taking expectations proves the last display. QED.

This is already at the exact scale requested in Question 5.2. It shows that **one-point late-vertex survival is not the missing estimate**.

## 3. Start-point centering costs at most one hitting-time scale

The source defines

`t_cov(G)=max_x E_x tau_cov`.

### Lemma 3.1

For any two starting vertices `x,y`,

`|E_x tau_cov - E_y tau_cov| <= h`.

In particular, every start-specific mean lies in `[t_cov-h, t_cov]`.

### Proof

Start from `x` and stop when `y` is first hit. At that time some vertices may already have been visited. The expected *remaining* time to cover the graph is therefore no larger than the expected cover time of a fresh walk started from `y`. Hence, by the strong Markov property,

`E_x tau_cov <= E_x T_y + E_y tau_cov <= h + E_y tau_cov`.

Swap `x,y` for the reverse inequality. QED.

Thus any universal exponential tail around each `E_x tau_cov` at scale `h` automatically transfers, with only a constant shift, to the source center `t_cov`.

## 4. B11/B25: the exact pair-correlation obstruction

The elementary identities are

`P(tau_cov>t)=P(U_t>0) <= E U_t = m(t)`

and

`E[U_t^2] = m(t) + sum_{u != v} P(T_u>t, T_v>t)`.

The second display is the B25 double count: expand the square of the sum of unvisited indicators, or count ordered surviving pairs directly.

The pair term is exactly what Lemma 2.1 does not control. If it were Poisson-like in the critical window, Question 5.2 would follow quickly.

### Proposition 4.1 (conditional full `t_hit`-window theorem)

Fix a starting vertex. Suppose there is a universal `C0` such that

`Var(U_t) <= C0 E U_t`

for every `t` up to the time when `E U_t` first enters `(1,2]`. Then there are universal `c,C>0` such that, for that starting vertex,

`P(|tau_cov-E tau_cov| > s h) <= C exp(-c s)`

for all `s>=0`. In particular `SD(tau_cov) <= C h`.

### Proof

Because one walk step can discover at most one new vertex,

`0 <= m(t)-m(t+1) <= 1`.

For `|V|>=3`, `m(0)=|V|-1>=2` and `m(t)->0`, hence there is an integer `t_*` with

`1 < m(t_*) <= 2`.

For the upper tail, Lemma 2.1 gives

`m(t_*+2kh) <= 2^{1-k}`.

Therefore Markov's inequality yields

`P(tau_cov>t_*+2kh) = P(U_{t_*+2kh}>0) <= 2^{1-k}`.

For the lower tail, apply Lemma 2.1 starting at `t_*-2kh` to obtain

`m(t_*-2kh) >= 2^k m(t_*) > 2^k`

whenever the left time is nonnegative. Chebyshev and the assumed variance bound give

`P(tau_cov <= t_*-2kh)`
`= P(U_{t_*-2kh}=0)`
`<= Var(U_{t_*-2kh}) / m(t_*-2kh)^2`
`<= C0 / m(t_*-2kh)`
`< C0 2^{-k}`.

Thus `tau_cov` has two-sided geometric tails in `2h` blocks around `t_*`. Summing these tails shows

`|E tau_cov-t_*| <= C_1 h`

and integrating/summing the squared-deviation tail gives

`Var(tau_cov) <= C_2 h^2`.

A shift of the center by `O(h)` preserves a constant-rate exponential tail after changing universal constants. QED.

### What this proposition does and does not say

It is a complete implication, but its variance hypothesis is **not proved universally**. In fact, a raw inequality of this form is suspicious on bottleneck graphs where many late vertices can remain unvisited as a block. The correct theorem may need a quotient into late-vertex clusters, a conditional factorial moment after revealing a bottleneck skeleton, or a different negative-dependence quantity. Therefore Proposition 4.1 is a reduction, not source closure.

It nevertheless isolates a precise target:

`sum_{u != v} [P(T_u>t,T_v>t)-P(T_u>t)P(T_v>t)]`.

That is the term which must be controlled, cancelled, or structurally decomposed to upgrade the known geometric-mean window to the hitting-time window.

## 5. Relation to the recovered Zhai bound

Zhai's general-graph concentration theorem centers at the GFF quantity `|E| M^2` and has deviation scale consisting of a `sqrt(lambda)` term of order `sqrt(t_hit t_cov)` plus a linear-in-`lambda` term of order `t_hit` (using the commute-time identity and `|E|M^2` comparable to `t_cov`). Thus it certifies the frozen admission metric

`beta_cert >= 1/2`.

Let `L=t_cov/t_hit`. At a requested deviation `s t_hit`, the generic geometric-mean term behaves like `sqrt(lambda L) t_hit`, so the recovered exponent in the moderate range is of Gaussian type roughly `lambda ~ s^2/L`, not the source's desired constant-rate `lambda ~ s`. Hence the unresolved gain grows precisely when `L -> infinity`, matching the regime highlighted immediately before DLP Question 5.2.

This is why simply replaying the GFF maximum concentration argument is not a new route.

## 6. Exact finite certificate: the literal coefficient-one inequality is false

Consider the seven-vertex graph with vertices `0,...,6` and edges

`(0,1),(0,2),(0,3),(1,2),(1,3),(2,3),(0,4),(0,5),(0,6)`.

Equivalently, vertices `0,1,2,3` induce `K_4`, and three pendant leaves are attached to vertex `0`.

Start the walk at vertex `1` (the same values hold at `2` and `3`). The exact checker archived beside this artifact solves the rational linear systems for all hitting times and for the first two cover-time moments on states `(current_vertex, visited_mask)`. It outputs

`t_hit = 20`,

`E_1 tau_cov = 932061/26180`,

and

`Var_1(tau_cov) = 895244678227/2056177200`.

The variance exceeds `t_hit^2=400` by the exact positive rational

`72773798227/2056177200 > 0`.

Therefore

`SD_1(tau_cov)/t_hit = sqrt(895244678227/822470880000)`

which is approximately `1.04330336656 > 1`.

The same exact dynamic program gives smaller mean cover times from the hub and leaves, while starts `1,2,3` attain

`t_cov(G)=932061/26180`.

Hence the certificate applies even if `tau_cov` in Question 5.2 is interpreted as beginning at a worst-case start for the expectation defining `t_cov`.

### Consequence

If the phrase “bounded by the maximal hitting time” is read literally as

`SD(tau_cov) <= t_hit`

with coefficient exactly one, that clause is **REFUTED** by this graph.

If the intended question is the scale statement

`SD(tau_cov)=O(t_hit)`

with an unspecified universal constant, this graph is only a lower calibration `C > 1.0433...`; it does not refute the scale conjecture.

The second source clause, universal constant-rate exponential decay of `(tau_cov-t_cov)/t_hit`, remains OPEN in this artifact.

## 7. Frozen metric and outcome

Fixed metric from admission:

`beta_cert = largest beta for which R7-03 has a written universal proof of SD <= C t_hit^beta t_cov^(1-beta)`.

Before: `1/2`.

After: `1/2`.

**NO MOVEMENT** on the frozen scale exponent. Ordinary unchanged count begins `0 -> 1` for the newly admitted target.

There is nevertheless genuine source progress: the coefficient-one interpretation of the first printed clause is exactly false, and the full scale problem has been reduced to a concrete late-vertex pair-correlation/cluster estimate.

## 8. Next attack

Do **not** retry B18/B11/B25 next run. The next attack should first test the raw overlap hypothesis on bottleneck graph families and, if it fails as expected, replace vertices by late clusters before attempting concentration. Candidate nonrepeating methods: **B14** (quotient by automorphisms/symmetry on two-block graphs), **B20** (identify the precise failure of the naive unvisited-vertex algorithm), and **B5** (introduce a bottleneck parameter and differentiate/compare the resulting late-cluster law).

No full source verdict is claimed. No audit is requested yet because the frozen metric has not moved to source closure.
