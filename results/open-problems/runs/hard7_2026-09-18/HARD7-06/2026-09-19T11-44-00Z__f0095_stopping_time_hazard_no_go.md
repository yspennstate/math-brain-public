Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — not GPT-6 maximum.** **No movement:** `W_3: 0.656508 -> 0.656508`. Methods actually tried: **B7 / B12 / B27**.

# HARD7-06 run 16 — stopping-time thermodynamics, exact hazard flux, and why even IFR would not close the 3-colour threshold

Status: **F0095 OPEN / HARD7-06 PARTIAL.** This run deliberately does not shave another decimal from the Ayre--Coja-Oghlan--Greenhill upper endpoint. Instead it attacks the source-level constant-location obstruction. The main progress is a source-matching reduction: under the known sharp-threshold theorem, Frieze's fixed `q=3` constant-location conjecture is equivalent to convergence of one scalar, the normalized expected first non-3-colourable time in the random graph process. I then identify the exact one-edge hazard budget for that stopping time, connect the strongest general monotone-system theorem to the older IFRA literature, and prove an abstract no-go showing that even the much stronger IFR/log-concavity property plus a BGT-type exponential-rate limit and sharpness still would not force the threshold locations to converge.

Repository / branch: `yspennstate/math-open-problems` / `master`.

## 1. Continuity, ownership, exclusions, and fresh source check

I resumed the already admitted canonical target `F0095`, owned create-only by HARD7-06 in `operations/claims/F0095.md`. I did not restart the original random-3-SAT candidate: the fixed-small-`k` random-SAT history is the distinct `F0097` track, and the HARD7-06 lifecycle already rotated away from its exhausted predecessor before claiming F0095.

At run start I reread the controlling HARD7 policy files, root `POSTED.md` and `RESULTS.md`, campaign `probability_campaign_2026_09/INDEX.md` and `RANKING.md`, the F0095 claim, the newest HARD7-06 checkpoint, the F0095 intake row under `probability_1000_intake_F_20260908/batches/b07_kalai_frieze.json`, and the newest neighbouring ownership state. The current R14 reports preserve their own successor/handoff and do not reopen the negative-margin perceptron as a collision with this target. No release, duplicate F0095 owner, posted equivalent, or settled campaign entry was found.

The external source statement remains Alan Frieze's ICM 2014 chromatic-number conjecture:

> **Conjecture.** There exists a sequence `d_k`, `k >= 2`, such that w.h.p. `chi(G_{n,d/n}) = k` for `d_{k-1} < d < d_k`.

HARD7-06 freezes the first small unresolved colourability-location case `k=3`: prove that the sharp 3-colourability transition of ordinary sparse Erdos--Renyi graphs has a limiting constant average-degree location.

### Bounded current-literature screen, 2026-09-19

I reran the status search rather than inheriting yesterday's negative result.

- Achlioptas--Friedgut, *A Sharp Threshold for k-Colorability* (RSA 1999), remains the sharp-threshold theorem: for fixed `k>=3` there is an `n`-dependent sharp location. It does not prove convergence of that location.
- Bayati--Gamarnik--Tetali, *Combinatorial approach to the interpolation method and scaling limits in sparse random graphs*, Ann. Probab. 41 (2013), arXiv:0912.2444, proves the relevant exponential-rate/scaling limits and isolates the stronger exponential-tail statement that would imply constant threshold location.
- Linusson--Shareshian, *Complexes of t-Colorable Graphs*, SIAM J. Discrete Math. 16 (2003), DOI `10.1137/S0895480100366968`, studies exactly the simplicial complex of `t`-colourable graphs, but the accessible statement is topological (homotopy type in selected regimes), not the layerwise log-concavity/IFR assertion tested below.
- Ross--Shahshahani--Weiss, *On the Number of Component Failures in Systems Whose Component Lives are Exchangeable*, Math. Oper. Res. 5 (1980), DOI `10.1287/moor.5.3.358`, proves that the failure-count variable of a general monotone system is IFRA; they prove the stronger IFR conclusion only for a special nonoverlapping-minimal-cut-set structure. The 3-colourability cut sets overlap heavily.
- A bounded 2025--2026 search again found the 2026 random **triangle-free conditioned** graph scaling-window theorem, not an ordinary `G(n,d/n)` fixed-`q=3` threshold-location theorem. No ordinary-model resolution of F0095 was recovered. This is bounded negative evidence, not a worldwide openness certificate.

The source status therefore remains **OPEN**.

## 2. Frozen source metric: no movement

The source-relevant campaign quantity remains

\[
W_3:=U_3-L_3.
\]

The latest certified values are

\[
L_3=4.03,\qquad U_3=4.686508,\qquad W_3=0.656508,
\]

where `U_3` is supported by the previous run's exact three-atom ACG certificate at `d=4.6865077`.

This run does not alter either endpoint:

\[
\boxed{W_3:0.656508\longrightarrow0.656508\quad\text{(no movement).}}
\]

That is intentional: the owner explicitly asked the hard fleet to stop confusing decimal polishing with progress on the source statement. This is the first no-movement run after a moving checkpoint, so Section I is not triggered.

## 3. B7 — take the limit: replace the moving threshold by one stopping-time mean

Expose the edges of `K_n` in a uniformly random order and let `G_{n,m}` be the graph formed by the first `m` edges. Define

\[
T_n:=\max\{m:G_{n,m}\text{ is 3-colourable}\}.
\tag{3.1}
\]

Thus, with

\[
p_{n,m}:=\mathbb P\{G_{n,m}\text{ is 3-colourable}\},
\]

we have exactly

\[
\boxed{\mathbb P(T_n\ge m)=p_{n,m},\qquad
\mathbb E T_n=\sum_{m=1}^{\binom n2}p_{n,m}.}
\tag{3.2}
\]

The second identity is the tail-sum formula. It turns the whole moving transition into a single thermodynamic scalar.

### Proposition 3.1 — mean stopping-time equivalence

Let `m_n^*` be any fixed-`m` sharp-threshold location for 3-colourability, so that `m_n^*=Theta(n)` and for every fixed `epsilon>0`,

\[
p_{n,\lfloor(1-\varepsilon)m_n^*\rfloor}\to1,
\qquad
p_{n,\lceil(1+\varepsilon)m_n^*\rceil}\to0.
\tag{3.3}
\]

Then

\[
\boxed{
\frac{T_n}{m_n^*}\xrightarrow{\mathbb P}1,
\qquad
\frac{\mathbb E T_n}{n}-\frac{m_n^*}{n}\longrightarrow0.}
\tag{3.4}
\]

Consequently, under the known sharp-threshold theorem, the fixed-`q=3` constant-location conjecture is equivalent to the existence of

\[
\boxed{\lim_{n\to\infty}\frac{2\mathbb E T_n}{n}.}
\tag{3.5}
\]

If the limit exists, it is the conjectural average-degree threshold `theta_3`.

#### Proof

The first assertion in (3.4) is immediate from monotonicity and (3.3): the events

\[
T_n<(1-\varepsilon)m_n^*,\qquad T_n>(1+\varepsilon)m_n^*
\]

have probabilities tending to zero.

The only point needed to pass from probability to expectation is uniform integrability on the `n` scale. This follows from a direct first-moment bound. Set

\[
N=\binom n2,
\qquad
C_n=\max_{n_1+n_2+n_3=n}\sum_{i<j}n_i n_j
=\left\lfloor\frac{n^2}{3}\right\rfloor.
\]

For any fixed 3-colouring, all edges must lie among its at most `C_n` bichromatic pairs. Union-bounding over the `3^n` labelled colourings gives

\[
p_{n,m}
\le
3^n\frac{\binom{C_n}{m}}{\binom Nm}
\le
3^n\left(\frac{C_n}{N}\right)^m.
\tag{3.6}
\]

For `n>=9`, `C_n/N<=3/4`. Hence for every fixed `K>\log 3/\log(4/3)` and all sufficiently large `n`,

\[
\sum_{m\ge Kn}p_{n,m}
\le
3^n\sum_{m\ge Kn}(3/4)^m
\le
4\exp\{n[\log3+K\log(3/4)]\},
\tag{3.7}
\]

which is exponentially small. The same bound controls the tail contribution of `T_n/n`; therefore `{T_n/n}` is uniformly integrable. Since `m_n^*/n` stays in a compact positive interval (the certified lower and upper endpoints already give such a bracket), `T_n/m_n^*->1` in probability plus uniform integrability yields the second assertion in (3.4).

Thus `m_n^*/n` converges iff `E T_n/n` converges. Multiplication by two converts edges per vertex into average degree. `square`

### Why this is useful

This does not solve F0095, but it changes the exact missing object. Instead of proving convergence of an arbitrarily chosen median/quantile threshold sequence, one may try to prove an interpolation or subadditivity theorem for the canonical scalar

\[
\Theta_n:=\frac{2}{n}\mathbb E T_n
=\frac{2}{n}\sum_m p_{n,m}.
\tag{3.8}
\]

Any genuine Cauchy/subadditivity mechanism for `Theta_n` would close the source problem once combined with known sharpness. This is the cleanest source-level target I found this run.

## 4. B12 — find what is conserved: exact one-edge hazard flux

For a 3-colourable graph `G` with `m` edges define its safe-extension fraction

\[
s(G):=
\frac{\#\{e\notin E(G):G+e\text{ is 3-colourable}\}}
{N-m}.
\tag{4.1}
\]

In the random graph process, conditioning on `G_{n,m}=G` makes the next edge uniform among the missing edges. Since 3-colourability is decreasing under edge addition,

\[
\boxed{
\frac{p_{n,m+1}}{p_{n,m}}
=
\mathbb E\big[s(G_{n,m})\mid G_{n,m}\text{ is 3-colourable}\big]
=:q_{n,m}.}
\tag{4.2}
\]

Define the layer hazard

\[
h_{n,m}:=-\log q_{n,m}.
\tag{4.3}
\]

Then the full tail cost is the exact telescoping budget

\[
\boxed{
-\log\frac{p_{n,m+t}}{p_{n,m}}
=
\sum_{j=m}^{m+t-1}h_{n,j}.}
\tag{4.4}
\]

This is the local geometric form of the BGT exponential-tail obligation. Exponential decay after sprinkling `t=Theta(n)` edges is equivalent to accumulating `Theta(n)` total hazard, i.e. a positive average logarithmic deficit in the conditional safe-edge fraction.

### The strongest general monotone-system theorem stops one level short

There is a useful exact prior-art identification. Regard each potential edge as a component that “fails” when that edge is exposed; the system is “up” exactly while the exposed graph remains 3-colourable. Then the number of component failures at system failure is

\[
F_n=T_n+1,
\]

and

\[
\mathbb P(F_n>m)=p_{n,m}.
\]

Ross--Shahshahani--Weiss (1980) prove for every monotone system with exchangeable component lives that this failure-count variable is **IFRA**. In the present notation that means

\[
\boxed{
\frac{-\log p_{n,m}}{m}\quad\text{is nondecreasing in }m.}
\tag{4.5}
\]

Equivalently, for `k>=m>=1`,

\[
\boxed{p_{n,k}\le p_{n,m}^{k/m}.}
\tag{4.6}
\]

This is **known reliability theory**, not a new theorem of this run. It is nevertheless a useful checkpoint: a general monotonicity/reliability argument cannot be expected to give much more automatically. If `p_{n,m}` is merely tending to zero subexponentially near the moving threshold, (4.6) at a fixed multiplicative displacement is still only a fixed power of a subexponentially small quantity; it does not produce `e^{-gamma n}`.

Ross--Shahshahani--Weiss prove the stronger IFR property only for special nonoverlapping minimal cut sets. Here the minimal cut sets are minimal non-3-colourable edge sets (4-critical graphs), and they overlap extensively. Thus their IFR theorem does not apply.

## 5. B27 — swap the quantifiers: test the stronger IFR/rank-log-concavity route

The natural strengthening of IFRA is discrete IFR, equivalently log-concavity of the survival sequence:

\[
\boxed{p_{n,m}^2\ge p_{n,m-1}p_{n,m+1}.}
\tag{5.1}
\]

Since `p_{n,m}=a_{n,m}/\binom Nm`, where `a_{n,m}` is the number of labelled `m`-edge 3-colourable graphs, (5.1) says that the rank sequence of the 3-colourability simplicial complex is **ultra-log-concave** in the standard normalized sense.

A bounded literature search found Linusson--Shareshian's topology of the same complex, the matroid/log-concavity literature, and the general coherent-system IFRA theorem, but no theorem asserting (5.1) for the 3-colourability complex. I therefore treat (5.1) only as a candidate structural property, not as known or proved.

### Exact finite evidence, n <= 7

The paired exact checker enumerates all unlabeled graphs in the graph atlas for `n=4,5,6,7`, weights each isomorphism class by `n!/|Aut(G)|`, tests 3-colourability by exact backtracking, and checks (5.1) after clearing all binomial denominators. For `n<=6` it independently cross-checks the entire labelled layer counts by direct enumeration of all `2^N` labelled graphs.

The exact labelled layer counts are

\[
\begin{array}{c|l}
n& (a_{n,0},a_{n,1},\ldots)\\\hline
4&(1,6,15,20,15,6,0),\\
5&(1,10,45,120,210,252,205,100,15,0,0),\\
6&(1,15,105,455,1365,3003,4990,6300,5895,3805,1365,240,15,0,0,0),\\
7&(1,21,210,1330,5985,20349,54229,115755,199815,278215,306831,\\
&\qquad256746,147665,55125,12915,1750,105,0,0,0,0,0).
\end{array}
\tag{5.2}
\]

For every admissible internal layer in all four rows,

\[
a_{n,m}^2\binom N{m-1}\binom N{m+1}
\ge
a_{n,m-1}a_{n,m+1}\binom Nm^2
\tag{5.3}
\]

holds exactly. The output ends

```text
ALL_EXACT_CHECKS_PASS = True
SCOPE = finite n<=7 evidence only; no asymptotic inference
```

Artifacts:

- `artifacts/hard7_2026-09-18/HARD7-06/2026-09-19T11-44-00Z__f0095_rank_ifr_exact.py` @ `d344999e184c8094f270fc22dc9b32a469ee64c4`
- `artifacts/hard7_2026-09-18/HARD7-06/2026-09-19T11-44-00Z__f0095_rank_ifr_exact.out` @ `85e26f45232a63b8efa67d98c5681e373713b2df`

This is a **self-check** and finite evidence only. It is not a theorem for all `n`, and it is not an audit.

The same checker also records the exact auxiliary means

\[
\frac{2\mathbb E T_n}{n}
=
\frac52,\ \frac{20}{7},\ \frac{9325}{3003},\ \frac{1153169}{352716}
\quad(n=4,5,6,7),
\tag{5.4}
\]

which is only small-`n` data for the scalar in Proposition 3.1.

## 6. Even proving IFR would not be enough

There are two separate reasons not to turn the next ten runs into a campaign to prove (5.1).

### Proposition 6.1 — what IFR plus a finite window actually gives

Assume (5.1) on layers from `m_0` onward. If

\[
p_{n,m_0}\ge a,\qquad p_{n,m_1}\le b,
\qquad 0<b<a\le1,
\]

with `w=m_1-m_0`, then for every integer `t>=0`,

\[
\boxed{
p_{n,m_1+t}
\le
b\left(\frac ba\right)^{t/w}.}
\tag{6.1}
\]

#### Proof

Let `f(m)=log p_{n,m}`. Log-concavity of `p` means discrete concavity of `f`, so every forward slope after `m_1` is at most the secant slope on `[m_0,m_1]`. Therefore

\[
f(m_1+t)-f(m_1)
\le
\frac{t}{w}[f(m_1)-f(m_0)]
\le
\frac{t}{w}\log(b/a).
\]

Exponentiating and using `p_{n,m_1}<=b` gives (6.1). `square`

Thus if a known sharp-threshold window has width `w_n=o(n)`, IFR would improve the tail after a linear sprinkling to

\[
\exp[-\Omega(n/w_n)],
\tag{6.2}
\]

but the BGT strengthening needs `exp[-Omega(n)]`. IFR alone reaches that only from an `O(1)` edge-count window, far stronger than ordinary sharpness.

### Proposition 6.2 — abstract no-go: sharpness + IFR + a BGT-type rate limit can coexist with an oscillating threshold

This is the more decisive obstruction. Fix constants

\[
0<a<b,\qquad \lambda>0.
\]

For each `n` define a survival sequence recursively by `p_{n,0}=1` and

\[
p_{n,m+1}=p_{n,m}e^{-h_{n,m}},
\tag{6.3}
\]

where for even `n`,

\[
h_{n,m}=
\begin{cases}
0,&m<\lfloor an\rfloor,\\
n^{-1/3},&\lfloor an\rfloor\le m<\lfloor bn\rfloor,\\
\lambda,&m\ge\lfloor bn\rfloor,
\end{cases}
\tag{6.4}
\]

and for odd `n`,

\[
h_{n,m}=
\begin{cases}
0,&m<\lfloor bn\rfloor,\\
\lambda,&m\ge\lfloor bn\rfloor.
\end{cases}
\tag{6.5}
\]

Then all of the following hold.

1. **IFR/log-concavity.** `h_{n,m}` is nondecreasing, so every `m -> p_{n,m}` is log-concave.
2. **Sharp threshold.** Along even `n` the sharp location is `an+o(n)`: below `(1-epsilon)an` survival is one, while above `(1+epsilon)an` the accumulated `n^{-1/3}` hazard is `Theta(n^{2/3})`, hence survival tends to zero. Along odd `n` the sharp location is `bn+o(n)`.
3. **A pointwise exponential-rate limit exists.** For every fixed `c>=0`,

\[
\lim_{n\to\infty}\frac1n\log p_{n,\lfloor cn\rfloor}
=\begin{cases}
0,&c\le b,\\
-\lambda(c-b),&c>b.
\end{cases}
\tag{6.6}
\]

Indeed, on the even subsequence the entire extra cost accumulated between `an` and `bn` is only `(b-a)n^{2/3}+o(n)`, invisible on the `1/n` logarithmic scale; on the odd subsequence it is absent. Above `bn`, both subsequences acquire the same linear cost `lambda(c-b)n+o(n)`.
4. **The sharp locations do not converge**, since they alternate between `a` and `b` on the `n` scale.

Therefore

\[
\boxed{
\text{sharpness + IFR + existence of the exponential-rate limit do not logically imply constant threshold location.}}
\tag{6.7}
\]

This is an abstract analytic counterexample, **not** a claim that the sequences (6.3)--(6.5) are rank sequences of graph-colourability complexes. Its purpose is to identify what a successful proof must use beyond those three properties: it has to forbid a macroscopic interval on which the probability is subexponentially small but the limiting `n^{-1}log p` is still zero. That is exactly the gap BGT's exponential-tail conjecture was designed to eliminate.

## 7. What the three moves actually accomplished

**B7 (take the limit).** The source problem is reduced to convergence of the canonical scalar `2 E T_n/n`. This is stronger operationally than “show the threshold centers converge” because the mean has the exact area representation (3.2), making interpolation/subadditivity methods conceivable. The reduction is rigorous because a direct first-moment tail bound supplies the needed uniform integrability.

**B12 (find what is conserved).** The exact hazard identity (4.2)--(4.4) turns the missing exponential tail into accumulated conditional safe-edge loss. Reliability theory shows that general monotonicity already gives IFRA, so any future argument that merely rediscovers IFRA cannot close F0095.

**B27 (swap the quantifiers).** I tested the tempting stronger claim that the 3-colourability rank densities are log-concave. It holds exactly for every layer through `n=7`, but is unproved asymptotically. More importantly, Propositions 6.1 and 6.2 show that proving IFR alone would still not bridge the BGT gap. This prevents a substantial likely dead end.

## 8. Remaining obligation and next route

The source conjecture remains OPEN. The strongest exact reformulation from this run is now:

\[
\boxed{
\text{prove convergence of }\Theta_n=\frac{2}{n}\mathbb E T_n,
\quad\text{or prove a source-valid mechanism forcing }\sum h_{n,m}=\Theta(n)
\text{ immediately above the moving threshold.}}
\tag{8.1}
\]

The finite IFR evidence is interesting but is no longer a priority by itself, because Section 6 proves it would not suffice.

The next run should use a genuinely different triple:

- **B10 — derandomize:** turn the average safe-edge deficit in (4.2) into a deterministic certificate carried by a bounded collection of critical edge witnesses;
- **B17 — look for the numbers elsewhere:** use coherent-system signatures / colouring-complex rank data to identify a stronger aging or boundary property than IFRA/IFR that is actually capable of linear hazard accumulation;
- **B25 — count the same thing twice:** count boundary pairs `(G,e)` with `G` 3-colourable and `G+e` non-3-colourable both from colourable layers and from embedded 4-critical witnesses, seeking a nontrivial lower bound on the Boolean-lattice boundary near the moving threshold.

Because the immediately preceding run moved `W_3`, this is only the first no-movement checkpoint since that movement; Section I does not trigger.

## 9. Verification and capability honesty

The only finite claim introduced this run is the `n<=7` layer enumeration/log-concavity evidence, and it has an exact checker plus archived output. The source-level propositions are theorem-sized symbolic statements with full proofs on the page. No checker was manufactured for tautological arithmetic.

The actual runtime identifies the model as **GPT-5.6 Sol**. The reasoning-effort level is **UNVERIFIED**. I therefore do not claim GPT-6 maximum.

The exposed scheduled-task controls still provide prompt/title/schedule/timing/enabled fields, but no model selector, no reasoning-effort selector, and no guaranteed execution duration. GPT-6 maximum remains request text only. Making it enforceable requires platform support for authenticated model/reasoning fields or runtime telemetry.

The policy record notes historical native modification errors `You cannot modify this task` for some IDs, while later authorized contexts succeeded for some of them. The allowed remedy for any recurring denial is the correct account/workspace/native context or platform support; duplicating a job or bypassing ownership is not allowed.

## 10. Ledger delta

```yaml
ledger_delta:
  track: HARD7-06
  target: F0095
  target_status: OPEN
  worker_status: PARTIAL
  metric: W_3 = U_3 - L_3
  before: 0.656508
  after: 0.656508
  movement: no movement
  L_3: 4.03
  U_3: 4.686508
  methods: [B7, B12, B27]
  new_reduction: constant threshold iff 2*E[T_n]/n converges, under known sharpness
  exact_identity: p_(m+1)/p_m = conditional expected safe-edge fraction
  known_prior_art: general monotone-system failure count is IFRA (Ross-Shahshahani-Weiss 1980)
  finite_evidence: normalized 3-colourability layer probabilities are log-concave for n=4..7
  finite_checker: ALL_EXACT_CHECKS_PASS
  no_go: sharpness + IFR + pointwise exponential-rate limit do not force threshold-location convergence
  closure: false
  next_methods: [B10, B17, B25]
```

No shared root ledger was edited by this worker; this delta is for the designated reconciler.
