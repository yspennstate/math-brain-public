Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — GPT-6 maximum was requested, but this runtime exposes no authenticated selector/telemetry establishing GPT-6 or maximum effort.**

# PROB10-08 artifact — radial-average Shannon NBRW deficit controls the TV window; any counterexample needs polynomial typical path coalescence

Status: **PROVED auxiliary/source-wide mechanism theorem; Salez Problem 2.3 remains OPEN / PARTIAL; no source closure; independent validation pending; worldwide novelty UNVERIFIED.**

Repository/branch: `yspennstate/math-open-problems` / `master`.

Exact source: Justin Salez, arXiv:2508.21055v1, Problem 2.3, under the rate-one continuous-time simple-random-walk convention
\[
H_t=e^{t(P-I)}.
\]
The source target remains: every bounded-degree vertex-transitive spectral-expander sequence exhibits total-variation cutoff. This is not the already-posted Abelian-Cayley/product-condition target.

## 0. Recovered state and ownership

Before starting the new argument I read/recovered:

- `operations/PROB10_2026-09-20.md`;
- current root `POSTED.md`;
- `operations/claims/I0112.md`;
- preserved R16/H0002 successor handoff `artifacts/prob10_2026-09-20/PROB10-08/2026-09-19T23-45-09Z_r16-h0002-handoff.md`;
- historical I0112 stuck report `runs/R16/2026-09-16T22-43-00Z_i0112-stuck-recovery-1.md`, including the exhausted product-varentropy, synchronous/tensor, moving-weight/local-Poincare, Hecke/information-curvature, local-limit/AEP and global subcommutation routes;
- immediate own predecessor `runs/prob10_2026-09-20/PROB10-08/2026-09-20T10-44-12Z_equitable-lre-factor-cutoff_5e82.md`;
- newest neighboring cutoff work located before the write: P26's `proofnet24/P26-progress-cutoff-transfer/runs/2026-09-20/2026-09-20_13-00-56__all-distance-spherical-green-transfer.md`, which owns shell-Green / spherical-spectrum / radial-clock transfer, and NM13-01's `proofnet24/NM13-01/progress-cutoff/runs/2026-09-20/2026-09-20T09-13-06Z__growing-automorphism-memory-cutoff.md`, which owns semidirect growing-memory transfer.

The R16/H0002 handoff remains unchanged: the current non-PROB10 successor is Christoph--Morawski--Wigderson Question 5.1 with the all-prefix isotonic/KKT obstruction. Nothing below changes that ownership.

## 1. Primary-source check and exact place where LRE is used

I re-read the current full proof of Dylan J. Altschuler, arXiv:2609.14945. The bounded 20 September 2026 correction/version check still exposes v1, submitted 14 September 2026; no v2 or erratum was found.

The LRE input is localized as follows.

1. Lemma 3.2 transfers LRE from vertices to the oriented-edge NBRW state space and gives maximal-rate set growth.
2. Lemma 3.3 turns that all-set growth into a Shannon-entropy lower bound.
3. Proposition 3.1 obtains `H(K_j(x,.)) >= log n - C log log n` for the NBRW endpoint kernel at/after the entropic radius.
4. Lemma 3.4 then uses only a spectral gap plus entropy production to clean a small entropy deficit into TV mixing.
5. The covering-tree radial CLT converts NBRW mixing to the SRW Gaussian window.

The proof itself records the exact path-multiplicity identity
\[
H(K_j(x,\cdot))=\log D_j-\mathbb E\log M_j(x,Y),
\]
where `D_j=d(d-1)^{j-1}` is the number of length-`j` vertex-started NBRW paths and `M_j(x,Y)` is the multiplicity of the random endpoint. The new step below is not this identity; it is a source-wide finite-n window inequality at the **actual early mixing threshold** and the resulting necessary polynomial coalescence structure for any counterexample.

## 2. Idea before calculation/code

Do not try to recover Altschuler's all-set LRE inequality from ordinary expansion. Instead average the **Shannon endpoint deficit** over the exact universal-cover radial decomposition at the early TV threshold. If that average is sublinear in `log n`, the ordinary spectral gap finishes mixing in `o(log n)` time. Therefore failure of cutoff forces a linear Shannon deficit on a positive fraction of the typical NBRW shells. The path-multiplicity identity then converts this into a concrete statement: on a positive fraction of those shells, a positive fraction of NBRW mass must land on endpoints carrying polynomially many nonbacktracking paths.

This is deliberately different from P26's Green/chi-square route: Green control sees an arithmetic mean of path multiplicity, whereas the quantity below sees a logarithmic/Shannon mean and is insensitive to rare huge `L2` spikes.

No code is needed; the work is analytic.

## 3. Exact radial decomposition

Fix a finite connected `d`-regular vertex-transitive graph `G=(V,E)`, `n=|V|`, `d>=3`, `q=d-1`, uniform stationary law `pi`, and one-sided SRW gap
\[
\gamma=1-\lambda_2(P)>0.
\]
Let
\[
H_t=e^{t(P-I)}.
\]

For `j>=1`, let `K_j(x,.)` be the endpoint law of a uniformly chosen nonbacktracking path of length `j` starting at `x`; put `K_0(x,.)=\delta_x`. Let `R_t` be the distance from the root of rate-one continuous-time SRW on the infinite `d`-regular tree.

The universal-cover construction gives the exact identity
\[
\boxed{
H_t(x,\cdot)=\sum_{j\ge0}\Pr(R_t=j)K_j(x,\cdot).
}
\tag{3.1}
\]
Because `G` is vertex-transitive, all entropy quantities below are independent of the chosen root.

Define the shell Shannon deficit
\[
\delta_j:=D(K_j(x,\cdot)\|\pi)
=\log n-H(K_j(x,\cdot))\in[0,\log n].
\tag{3.2}
\]
For any `t>=0`, set
\[
A(t):=\mathbb E[\delta_{R_t}].
\tag{3.3}
\]
By convexity of relative entropy and (3.1),
\[
\boxed{
D(H_t(x,\cdot)\|\pi)\le A(t).
}
\tag{3.4}
\]

## 4. Theorem A — finite-n TV-window bound from radial-average Shannon deficit

Fix `epsilon in (0,1/2)` and write
\[
t_-:=t_{\rm mix}(1-\epsilon),
\qquad
w_\epsilon:=t_{\rm mix}(\epsilon)-t_-.
\]
Let
\[
\eta:=1-e^{-\gamma}.
\]

### Theorem A

For every such finite graph,
\[
\boxed{
 w_\epsilon
 \le
 1+\frac{4}{\eta\epsilon^2}A(t_-).
}
\tag{4.1}
\]
Consequently, for a bounded-degree vertex-transitive expander sequence,
\[
A(t_{\rm mix}(1-\epsilon))=o(\log n)
\quad\Longrightarrow\quad
\frac{t_{\rm mix}(\epsilon)-t_{\rm mix}(1-\epsilon)}{t_{\rm mix}(1/2)}\to0.
\tag{4.2}
\]
If the radial-average deficit is `O((log n)^alpha)` for some `alpha<1`, then the same fixed-threshold window is `O((log n)^alpha+1)`.

### Proof

Take the time-one continuous kernel
\[
Q:=H_1=e^{P-I}.
\]
Its eigenvalues are positive. On constants the eigenvalue is one; on the orthogonal complement they are at most `e^{-gamma}`. Hence its absolute spectral gap is at least `eta=1-e^{-gamma}`.

Altschuler's Lemma 3.4 records the entropy-production consequence of Ozawa's inequality: for every probability law `nu`,
\[
H(\nu Q)-H(\nu)
\ge \frac{\eta}{4}\|\nu-\pi\|_{TV}^2.
\tag{4.3}
\]
Apply (4.3) successively to `nu,nu Q,...,nu Q^{s-1}`. Total variation is decreasing in time, so
\[
\frac{\eta s}{4}\|\nu Q^s-\pi\|_{TV}^2
\le \log n-H(\nu)
=D(\nu\|\pi).
\tag{4.4}
\]
Set `nu=H_{t_-}(x,.)`. By (3.4), its entropy deficit is at most `A(t_-)`. Therefore any integer
\[
s\ge \frac{4A(t_-)}{\eta\epsilon^2}
\]
puts the law within TV distance `epsilon` of stationarity. Since `Q^s=H_s`, (4.1) follows.

For bounded-degree expanders, `t_mix(1/2)=Theta(log n)`: the upper bound follows from the spectral gap and `pi_min=1/n`; the lower bound follows from bounded-degree support growth together with the Poisson jump count. Thus (4.2) follows immediately. QED.

### Quantitative support lower bound used above

If degrees are bounded by `D`, then at time `t=c_D log n` with sufficiently small fixed `c_D>0`, the Poisson jump count is at most `2t` with probability `1-o(1)`, while a graph ball of radius `2t` has at most `n^rho` vertices for some fixed `rho<1`. Hence the walk puts `1-o(1)` mass on a set of stationary mass `o(1)`. This gives the required `Omega(log n)` lower mixing scale without any finite-size extrapolation.

## 5. Exact Shannon path-multiplicity form

For `j>=1`, write
\[
D_j=dq^{j-1}
\]
for the number of length-`j` nonbacktracking paths from `x`, and let
\[
M_j(x,y):=\#\{\text{length-}j\text{ NBRW paths from }x\text{ to }y\}.
\]
Then
\[
K_j(x,y)=\frac{M_j(x,y)}{D_j}.
\tag{5.1}
\]
If `Y_j~K_j(x,.)`, direct substitution gives
\[
\boxed{
\delta_j
=\log n-\log D_j+\mathbb E\log M_j(x,Y_j)
=\mathbb E\log\bigl(nK_j(x,Y_j)\bigr).
}
\tag{5.2}
\]
Thus Theorem A says that the cutoff window is controlled by the radial average of a **logarithmic path-overload statistic**.

For comparison, the shell collision/Green quantity is
\[
1+\chi^2(K_j(x,\cdot)\|\pi)
=n\sum_yK_j(x,y)^2
=\mathbb E_{Y_j\sim K_j}[nK_j(x,Y_j)],
\tag{5.3}
\]
which averages the likelihood itself rather than its logarithm. Jensen gives
\[
\delta_j\le \log(1+\chi^2),
\]
but the converse can fail badly because rare huge likelihood values dominate (5.3). This is exactly why the present route is not a restatement of the P26 Green-shell program and why the earlier Haiman polynomial-`L2` obstruction does not by itself settle TV mixing.

## 6. Theorem B — any source counterexample needs polynomial typical NBRW coalescence

The following is the main obstruction extracted this run.

### Theorem B

Suppose a bounded-degree vertex-transitive spectral-expander sequence fails total-variation cutoff. Passing to a subsequence of constant degree `d>=3`, there exist constants
\[
\epsilon\in(0,1/2),\quad a>0,\quad b>0,\quad C<\infty
\]
and times
\[
t_n=t_{\rm mix}^{(n)}(1-\epsilon)
\]
such that, for all sufficiently large `n`, the following holds.

Let `R_{t_n}` be the universal-tree radial variable and put `v=(d-2)/d`. With probability at least `b` over `j=R_{t_n}`,
\[
|j-vt_n|\le C\sqrt{\log n}
\tag{6.1}
\]
and simultaneously
\[
\boxed{
K_j(x,\{y:M_j(x,y)\ge n^a\})\ge b.
}
\tag{6.2}
\]
In words: failure of cutoff forces a **positive fraction of typical radial shells** on which a **positive fraction of NBRW endpoint mass** lies on vertices reached by polynomially many distinct nonbacktracking paths.

This is much stronger than merely failing long-range expansion. A large structured set can violate LRE without producing the positive-mass polynomial path coalescence in (6.2).

### Proof

Failure of cutoff means that for some fixed `epsilon` there is a subsequence and `kappa>0` such that
\[
w_\epsilon\ge \kappa t_n.
\tag{6.3}
\]
The bounded-degree support lower bound gives `t_n>=c log n`, while spectral expansion gives `t_n<=C_1 log n`. Theorem A therefore forces
\[
A(t_n)\ge a_0\log n
\tag{6.4}
\]
for some constant `a_0>0` depending only on the subsequence parameters.

The radial walk on the infinite `d`-regular tree has drift `v=(d-2)/d`. As in Altschuler's covering-tree argument, away from the root its increments are `+1` and `-1` with probabilities `q/d` and `1/d`, and the total number of visits to the root is tight. After Poissonization this gives
\[
R_t=vt+O_P(\sqrt t).
\tag{6.5}
\]
Because `t_n=Theta(log n)`, choose `C` so that the probability of the complement of (6.1) is at most `a_0/4`.

Normalize `X_j=\delta_j/\log n in [0,1]`. From (6.4), `E X_{R_{t_n}}>=a_0`. Removing the radial tail costs at most `a_0/4`. If the event
\[
B_n:=\{|j-vt_n|\le C\sqrt{\log n},\ \delta_j\ge (a_0/2)\log n\}
\]
had radial probability below `a_0/4`, then
\[
E X_{R_{t_n}}<a_0/4+a_0/4+a_0/2=a_0,
\]
a contradiction. Hence
\[
\Pr(R_{t_n}\in B_n)\ge a_0/4.
\tag{6.6}
\]

Fix any `j in B_n` and let
\[
L_j(y):=nK_j(x,y)\le n.
\]
Equation (5.2) gives
\[
E_{K_j}\log L_j(Y)\ge (a_0/2)\log n.
\]
If
\[
p_j:=K_j(x,\{y:L_j(y)\ge n^{a_0/4}\}),
\]
then, because `log L_j/log n<=1`,
\[
\frac{E\log L_j}{\log n}
\le p_j+(1-p_j)\frac{a_0}{4}.
\]
Thus
\[
p_j\ge \frac{a_0}{4-a_0}=:b_0>0.
\tag{6.7}
\]

Finally, the universal tree lower bound gives
\[
t_{\rm mix}(1-\epsilon)\ge (1-o(1))\frac{d}{d-2}\log_q n.
\tag{6.8}
\]
Indeed, at any fixed fraction less than this time, the tree radial position is below `(1-c)log_q n` with high probability, so the projected walk is supported on a graph ball of `o(n)` vertices. Combining (6.1) and (6.8) yields
\[
j\ge \log_q n-o(\log n)
\]
on the relevant shells. Therefore
\[
\frac{D_j}{n}=n^{-o(1)}\quad\text{or larger}.
\]
Since `L_j=nM_j/D_j`, the likelihood lower bound in (6.7) implies
\[
M_j(x,y)\ge n^{a_0/4-o(1)}.
\]
After decreasing the exponent, e.g. take `a=a_0/5` for all large `n`, and set `b=min(a_0/4,b_0)`, we obtain (6.2). QED.

## 7. Corollary — a concrete weaker-than-LRE source criterion

Theorem B has the following contrapositive form. It is a useful target, but until a genuinely new non-LRE family is proved to satisfy it, I count it as **auxiliary mechanism progress**, not source-level class progress.

Fix a source-admissible sequence of fixed degree `d` and gap at least `gamma`. Let `L_n=log_{d-1}n`. Choose a sufficiently large constant `C_0=C_0(d,gamma)`.

Assume that for every fixed `a>0`,
\[
\boxed{
\sup_{L_n/2\le j\le C_0L_n}
K_j\bigl(x,\{y:nK_j(x,y)\ge n^a\}\bigr)\longrightarrow0.
}
\tag{7.1}
\]
Then the sequence has total-variation cutoff.

### Proof

For `L=nK_j(x,Y_j)`,
\[
\delta_j=E\log L\le E(\log L)^+.
\]
Splitting at `n^a` gives
\[
\frac{\delta_j}{\log n}
\le a+K_j(L\ge n^a).
\tag{7.2}
\]
Condition (7.1), followed by `a downarrow0`, yields
\[
\sup_{L_n/2\le j\le C_0L_n}\delta_j=o(\log n).
\]
The universal tree lower bound and spectral upper bound place `R_{t_mix(1-epsilon)}` in this interval with probability `1-o(1)`. Outside the interval the deficit is at most `log n`, so its radial-average contribution is `o(log n)`. Theorem A now gives cutoff. QED.

Condition (7.1) controls **typical polynomial overload**, not all-set growth and not chi-square. Altschuler's LRE theorem implies much stronger entropy control. The converse need not hold at the level of the condition: (7.1) allows exceptional endpoints or exceptional sets carrying vanishing NBRW mass.

## 8. Two alternative approaches checked and stopped

### Approach 2 — exact radial birth-death reduction

A tempting route is to make `dist(o,X_t)` an exact one-dimensional birth-death chain and apply Ding--Lubetzky--Peres, who prove for continuous-time birth-death families that `t_rel=o(t_mix)` is equivalent to TV cutoff, with window at most `sqrt(t_mix*t_rel)`.

This route is **vacuous in the bounded-degree source asymptotic**. If the distance partition about every root is strongly lumpable for SRW, then the numbers of neighbors from a vertex in sphere `i` going to spheres `i-1,i,i+1` depend only on `i`; for a vertex-transitive graph this is exactly distance-regularity. Markowsky's survey records this birth-death projection for distance-regular graphs.

But the Bannai--Ito conjecture was proved by Bang--Dubickas--Koolen--Moulton: for every fixed valency greater than two there are only finitely many distance-regular graphs. A uniformly bounded-degree sequence has a constant-degree subsequence; degree two gives cycles and cannot have a uniform spectral gap. Therefore **no source-admissible sequence with `n->infinity` can admit this exact distance-regular birth-death reduction**.

So DLP is a mathematically valid theorem but cannot furnish a nonvacuous bounded-degree transitive-expander class through exact radial lumpability. Any useful radial reduction must be approximate/weighted and cannot simply impose distance-regularity.

### Approach 3 — exact tree injectivity/local-limit transfer through the cutoff scale

The older R16 stuck analysis noted that a local weak limit only controls fixed times, whereas mixing occurs at `Theta(log n)`. A stronger attempt would demand exact tree injectivity far enough to transfer an infinite-tree AEP directly.

This too is too rigid. If a `d`-regular graph is tree-injective to radius `r`, the Moore volume bound gives
\[
n\ge 1+d\sum_{k<r}q^k,
\qquad r\le \log_q n+O_d(1).
\tag{8.1}
\]
The continuous-time tree walk reaches the entropic radial scale `log_q n` only at
\[
T_n=\frac d{d-2}\log_q n,
\]
because backtracking reduces radial speed to `(d-2)/d`. Thus exact trajectory/tree-word injectivity out to the full time scale would require a radius larger than the Moore scale by the fixed factor `d/(d-2)>1`, which is impossible. Even exact endpoint injectivity at the relevant reduced radius is Moore-extremal and therefore cannot be a general source mechanism.

The surviving replacement is precisely a **typical weighted collision statement** such as (7.1), not deterministic injectivity of all paths.

## 9. Comparison of the three nonexhausted approaches

1. **Radial-average Shannon NBRW deficit / typical path overload — retained.** This gives the finite-n window inequality (4.1) and the source-counterexample obstruction (6.2). It is the main mathematical progress of this run.
2. **Exact distance-radial birth-death reduction — stopped by a hard finiteness obstruction.** Strong lumpability forces distance-regularity, and Bannai--Ito makes bounded-degree asymptotic use vacuous.
3. **Exact local/tree injectivity through the mixing scale — stopped by the Moore/backtracking mismatch.** Deterministic lifting is too rigid; only typical path control can plausibly survive.

These do not restart the historical product/tensor, moving-weight-Poincare, Hecke/curvature or global-subcommutation attempts, and do not duplicate P26's shell-Green route or NM13's semidirect-memory route.

## 10. Source before / after

```yaml
ledger_delta:
  target: "Salez arXiv:2508.21055 Problem 2.3"
  exact_walk: "rate-one continuous-time simple random walk"
  source_status_before: "OPEN / PARTIAL"
  source_status_after: "OPEN / PARTIAL"
  source_metric: "W_exp"
  source_metric_before: "1/2 provisional"
  source_metric_after: "1/2 provisional"
  source_metric_movement: false
  concrete_new_nonbaseline_cutoff_family_this_run: false
  mechanism_progress:
    - "finite-n window bound by radial-average NBRW Shannon deficit"
    - "non-cutoff forces positive-mass polynomial NBRW path coalescence on typical radial shells"
    - "typical polynomial-overload criterion sufficient for cutoff"
    - "exact radial birth-death route ruled out asymptotically by Bannai-Ito"
    - "exact tree-injectivity route ruled out as a general mechanism by Moore/backtracking scale mismatch"
  independent_audits: 0
  worldwide_novelty: "UNVERIFIED"
```

I do **not** promote (7.1) as source-level class progress until membership is proved for a genuinely new non-LRE source family. In particular, no product/tensor example is counted.

## 11. Tests actually run

No finite mixing plot, graph census, Monte Carlo simulation, or finite-size extrapolation was used. No code was required. The checks were analytic and literature/source checks only:

- full current Altschuler proof re-read;
- bounded current search for v2/correction/erratum (none surfaced; current record remains v1);
- Ding--Lubetzky--Peres continuous-time birth-death cutoff criterion checked;
- Markowsky radial birth-death reduction for distance-regular graphs checked;
- Bang--Dubickas--Koolen--Moulton fixed-valency finiteness theorem checked before deciding that the radial-lumping route is vacuous.

## 12. Remaining full-scope gap and next delimited target

The source conjecture would follow from ruling out (6.2): prove that on every bounded-degree vertex-transitive expander, typical NBRW shells at the early SRW mixing threshold do **not** place positive mass on endpoints with polynomial path multiplicity.

The first concrete nonduplicating stress test should be the already-isolated Haiman affine family. Earlier R16 runs show that its chi-square/Green quantity can be polynomially bad because of a high-multiplicity spectral block, while its true slow matrix coefficients are `L1`-rare. The new theorem identifies the exact question that distinguishes those possibilities:

> Is the polynomial `L2` excess carried by vanishing NBRW mass (compatible with cutoff), or does a positive fraction of NBRW mass see polynomial endpoint multiplicity (a genuine counterexample mechanism)?

That is a Shannon/typical-mass question rather than another `L2` spectral estimate.

No scheduler state, cadence, enabled state, email, Drive object, public post, permission, shared ledger, peer-track file, workflow, or force push was changed.
