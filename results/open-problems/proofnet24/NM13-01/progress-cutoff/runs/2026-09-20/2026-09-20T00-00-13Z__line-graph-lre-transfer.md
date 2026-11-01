Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — not GPT-6 maximum.** No authenticated runtime metadata establishes a different model or effort level.

# NM13-01 / LIVE20 T08 — cutoff for a non-LRE transitive line-graph class

**Status: PARTIAL on Salez Problem 2.3, with a new complete special-class theorem and quantitative window.**

Repository/branch: `yspennstate/math-open-problems` / `master`.
Run namespace: `proofnet24/NM13-01/progress-cutoff/runs/2026-09-20/`.
Frozen pre-write master observed during the run: `d7b754a117c3353999c8c12e3abb12b5bb27ce0b` (concurrent fleet commits continued afterward).

## 1. LIVE20 continuity and short NM13-01 handoff

The controlling owner instruction is `operations/PROGRESS20_2026-09-20.md`, supplemented by the T08 section of `operations/PROB10_2026-09-20.md`. It supersedes NM13-01's old intake-only admission loop for this run.

The last pre-transition NM13-01 report was

`proofnet24/NM13-01/runs/2026-09-19/2026-09-19T23-12-00Z__admission-delta-screen-44-hard-releases-posted-update-no-r0-admission.md`.

That state is preserved, not rewritten: NM13-01 was then `ADMISSION_PENDING`; P0292 had already reached its mandatory handoff and is not silently reopened; no old claim is mutated here. LIVE20 now authorizes this worker to work on T08 as a complementary route. The canonical parent claim `operations/claims/I0112.md` remains the historical R16 claim and was read but not overwritten.

The historical R16/I0112 work was also recovered before deriving anything new. In particular:

- fixed Cartesian products preserve cutoff but are too decomposable;
- synchronous/direct squares of suitable transitive Ramanujan families had a repository proof candidate with `O(sqrt(log n))` continuous-time window;
- the universal `Omega(sqrt(log n))` continuous-time cutoff-window floor on bounded-degree expanders was recorded;
- a single automorphic matching between two layers was proved gauge-trivial;
- the terminal R16 handoff identified the unresolved arbitrary fixed-degree Cayley-expander case and warned that long-range expansion is only a sufficient hypothesis, not arbitrary spectral expansion.

I therefore did **not** redo a product/tensor proof, a one-matching perturbation, or the global curvature/subcommutation routes already killed by R16.

The LIVE20 partner root `proofnet24/P26-progress-cutoff-transfer/` was not present through the authorized GitHub path at the beginning of this run, so there was no saved P26 proof to consume. This run deliberately uses incidence/intertwining and transitivity rather than entropy/Green-function transfer.

## 2. Exact source and fresh primary status

Salez, `arXiv:2508.21055v1`, uses the continuous-time convention

`P_t = exp(t(T-I)) = e^{-t} sum_{k>=0} t^k T^k/k!`,

i.e. mean-one exponential holding times between transitions of the discrete kernel `T`. Problem 2.3 is literally:

> Prove that all vertex-transitive expanders exhibit cutoff.

Here an expander sequence has diverging size, uniformly bounded degree and spectral gap bounded away from zero.

The most important newer primary input is Altschuler, `arXiv:2609.14945v1` (submitted 14 September 2026). It proves that fixed-degree long-range expanders have Gaussian-profile cutoff; for lazy walk the center is

`(2d/(d-2)) log_{d-1} n`

with `Theta(sqrt(log n))` profile window. The same paper proves the strict hierarchy

`Ramanujan => long-range expansion => spectral expansion`,

with neither converse. Thus long-range expansion is **not** a synonym for the T08 source hypothesis.

Pedrotti--Salez, `arXiv:2607.05345`, gives the local-product/local-Poincare cutoff criterion. Salez's 2024 varentropy theorem gives the corresponding sparse-fast-mixing information criterion. Neither is used as a black box below; this route is complementary.

A bounded prior-art search on 20 September 2026 for combinations of `line graph`, `random walk cutoff`, `Ramanujan line graph`, `edge-transitive`, and `total variation cutoff` did not locate the exact transfer theorem below. Bordenave--Lacoin's covered-expander theorem is relevant background and may overlap some arithmetic subfamilies. Therefore the correct novelty label is:

**NEW REPOSITORY THEOREM / PUBLICATION NOVELTY UNVERIFIED.**

I make no claim that every explicit arithmetic instance is outside every older covered-expander theorem.

## 3. New class and theorem

Let `G=(V,E)` be a finite connected simple `d`-regular graph, `d>=3`, and let `L(G)` denote its line graph: vertices of `L(G)` are edges of `G`, and two are adjacent iff they share an endpoint.

### Theorem T08-NM01-1 — edge-transitive LRE ancestry gives non-LRE transitive cutoff

Fix `d>=3` and `c>0`. Let `(G_n)` be any sequence of connected simple `d`-regular **edge-transitive `c`-long-range expanders** with `n=|V(G_n)| -> infinity`. Put

`H_n = L(G_n)`,  `m_n=|V(H_n)|=dn/2`,  `q=d-1`,

and let continuous-time simple random walk on `H_n` use Salez's generator `Q_n-I`, where `Q_n` is the discrete simple-random-walk kernel on `H_n`.

Then:

1. `(H_n)` is a bounded-degree **vertex-transitive spectral-expander** sequence, of degree `2(d-1)`.
2. `(H_n)` is **not** a `c'`-long-range-expander sequence for any fixed `c'>0`.
3. `(H_n)` has total-variation cutoff at

```
T_n = [2(d-1)/(d-2)] log_{d-1} n
    = [2(d-1)/(d-2)] log_{d-1}(2m_n/d),
```

with window

`O(sqrt(log n)) = O(sqrt(log m_n))`.

Equivalently, for every fixed `epsilon in (0,1)`,

`t_mix^{H_n}(epsilon) = T_n + O_{d,c,epsilon}(sqrt(log n))`,

and the relative window is `O(1/sqrt(log n)) -> 0`.

In particular, this gives a source-valid class of bounded-degree vertex-transitive **spectral expanders lying strictly outside Altschuler's long-range-expansion hypothesis**.

The class is nonempty in a strong explicit sense: Kaufman--Lubotzky, `arXiv:1108.2960`, Theorem 3, construct for fixed prime-power `q` and growing `alpha` explicit `(q+1)`-regular **edge-transitive Ramanujan graphs**. Altschuler proves Ramanujan implies LRE, so their line graphs instantiate the theorem.

## 4. Exact incidence factorization

Everything begins with two Markov kernels attached to a `d`-regular graph `G`.

Let

- `C(e,v)=1/2` when vertex `v` is an endpoint of edge `e`, otherwise `0`; thus `C` maps an edge to a uniformly chosen endpoint.
- `D(v,e)=1/d` when edge `e` is incident to vertex `v`, otherwise `0`; thus `D` maps a vertex to a uniformly chosen incident edge.

Let `P` be simple random walk on `G`, `Q` simple random walk on `L(G)`, and set

`R=CD` on edges, `S=DC` on vertices.

A one-line transition calculation gives

```
S = (I+P)/2.                                      (4.1)
```

Indeed from `v`, choose one of its `d` incident edges and then one of that edge's two endpoints: stay at `v` with probability `1/2`, and move to each neighbor with probability `1/(2d)`.

For edges, `R(e,e)=1/d`, while for each of the `2(d-1)` line-neighbors `f` of `e`, `R(e,f)=1/(2d)`. Hence with

`beta = d/(d-1)`

we have

```
Q - I = beta (R-I).                               (4.2)
```

This identity is exact, not asymptotic.

Also, for every integer `k>=1`,

```
R^k = C S^(k-1) D.                                (4.3)
```

The proof is just associative multiplication:
`(CD)^k=C(DC)^(k-1)D`.

Finally `RC=CS`, so exponentiating (4.2) gives the exact intertwining

```
exp(t(Q-I)) C
 = C exp(beta t (S-I))
 = C exp(a t (P-I)),                              (4.4)
```

where

`a=beta/2=d/[2(d-1)]`.

This is the core transitivity-compatible mechanism: the line-graph walk viewed from a random endpoint is exactly a time-rescaled continuous-time walk on the base graph.

## 5. Vertex transitivity and spectral expansion

Because `G_n` is edge-transitive, `Aut(G_n)` acts transitively on `E(G_n)`. Those edges are precisely the vertices of `H_n=L(G_n)`, so `H_n` is vertex-transitive.

Each edge of a simple `d`-regular graph meets `d-1` other edges at each endpoint, hence `H_n` is `2(d-1)`-regular.

Long-range expansion of the base implies a uniform one-sided spectral gap: write the normalized base eigenvalues as

`1=theta_1 >= theta_2 >= ...`, with `1-theta_2 >= gamma(d,c)>0`.

Equation (4.1) says the nonzero eigenvalues of `R=CD` are those of `S=DC`, namely `(1+theta_i)/2`; any remaining eigenvalues of `R` are zero. From

`Q = beta R - I/(d-1)`,

the corresponding line-graph eigenvalues are

```
mu_i = [d theta_i + d-2]/[2(d-1)]
     = 1 - a(1-theta_i),                          (5.1)
```

plus the extra value `-1/(d-1)`. Therefore

`1-mu_2 >= a gamma(d,c)>0`,

so `(H_n)` is a spectral-expander sequence.

## 6. Upper half of cutoff

Let `pi_V`, `pi_E` denote the uniform laws on vertices and edges. Since `G` is regular,

`pi_V D = pi_E`.

Let `N_t ~ Pois(beta t)`. By (4.2), continuous-time line-graph walk is the Poissonization of `R` at rate `beta`:

`exp(t(Q-I)) = e^{-beta t} sum_{k>=0} (beta t)^k R^k/k!`.

Start from an edge `e={u,v}` and let

`nu_e = delta_e C = (delta_u+delta_v)/2`.

If `N_t=k>=1`, equation (4.3) gives the conditional edge law

`nu_e S^(k-1) D`.

Markov kernels contract total variation, so if

`d_S(k)=max_x ||delta_x S^k-pi_V||_TV`,

then

```
||delta_e exp(t(Q-I)) - pi_E||_TV
 <= e^{-beta t}
    + E[ d_S(N_t-1) 1_{N_t>=1} ].                (6.1)
```

Now set

```
L_n = log_{d-1} n,
v   = (d-2)/d,
kappa_n = (2/v)L_n = [2d/(d-2)]L_n.
```

Altschuler's lazy-walk theorem applies to every fixed-degree LRE sequence and says that `S=(I+P)/2` has Gaussian-profile cutoff centered at `kappa_n`, with window `Theta(sqrt(L_n))`, uniformly over starts.

Define

`T_n = kappa_n/beta = [2(d-1)/(d-2)]L_n`.

Take `t=T_n+C sqrt(L_n)`. Then

`E N_t = kappa_n + beta C sqrt(L_n)`.

Put

`k_0=floor(kappa_n + (beta C/2)sqrt(L_n))`.

Monotonicity of `d_S` and (6.1) give

```
d_H(t)
 <= e^{-beta t}
    + P(N_t<k_0)
    + d_S(k_0-1).                                 (6.2)
```

Since `Var(N_t)=Theta(L_n)`, Chebyshev already yields

`limsup_n P(N_t<k_0) = O_d(C^{-2})`.

The Gaussian profile gives

`lim_{C->infty} limsup_n d_S(k_0-1)=0`.

Also `e^{-beta t}->0`. Therefore

```
lim_{C->infty} limsup_n d_H(T_n+C sqrt(L_n)) = 0. (6.3)
```

This proves the required upper window bound.

## 7. Lower half of cutoff in the source continuous-time convention

The endpoint map gives the lower bound without any entropy estimate. By (4.4),

```
delta_e exp(t(Q-I)) C
 = nu_e exp(a t(P-I)).                            (7.1)
```

Because applying the Markov kernel `C` can only decrease total variation,

```
||delta_e exp(t(Q-I))-pi_E||_TV
 >= ||nu_e exp(a t(P-I))-pi_V||_TV.               (7.2)
```

Thus it suffices to show that the right-hand side is near one before `T_n`.

Set

`tau_n=L_n/v=[d/(d-2)]L_n`.

Because `a=beta/2`, we have the exact center identity

```
a T_n = tau_n.                                    (7.3)
```

Take `t=T_n-C sqrt(L_n)` and put

`s=a t=tau_n-a C sqrt(L_n)`.

Lift simple random walk from either endpoint of `e` to the universal covering `d`-regular tree. Graph distance downstairs is no larger than tree distance upstairs. Let `Y_m` be the tree radial chain after `m` discrete steps. Away from zero its increments are `+1` with probability `(d-1)/d` and `-1` with probability `1/d`; at zero it moves to one. Its positive-level drift is

`v=(d-2)/d`.

Write

```
Y_m = v m + (1-v) L_m + M_m,                      (7.4)
```

where `L_m` counts visits to zero before steps and `M_m` is a martingale with increments bounded in absolute value by `2`. The total number `L_infinity` of root visits has a geometric tail because, after departing from the root, the biased radial walk returns with probability `1/(d-1)`.

Let `K~Pois(s)`, independently, and choose

`r_n = L_n - (v a C/2) sqrt(L_n)`.

If `Y_K>r_n`, then from (7.4) at least one of the following occurs:

1. `K-s > (a C/6)sqrt(L_n)`;
2. `M_K > (v a C/6)sqrt(L_n)`;
3. `(1-v)L_K > (v a C/6)sqrt(L_n)`.

The first event has probability at most

`36 s/(a^2 C^2 L_n) = O_d(C^{-2})`.

For the second event, restrict first to `K<=2 tau_n` (the complement is exponentially small in `L_n`). Azuma--Hoeffding applied conditionally on `K=k` gives

```
P(M_K > (v a C/6)sqrt(L_n), K<=2tau_n)
 <= exp[-v^3 a^2 C^2/576].                        (7.5)
```

The third probability tends to zero for every fixed `C`, because its threshold is of order `sqrt(L_n)` while `L_infinity` has a geometric tail.

Consequently, uniformly for each of the two endpoint starts,

```
P(dist_G(X_s,start) <= r_n)
 >= 1 - O_d(C^{-2}) - exp(-c_d C^2) - o_n(1).     (7.6)
```

Let

`A_n = B_G(u,r_n) union B_G(v,r_n)`.

A `d`-regular graph has

`|B_G(x,r)| <= C_d (d-1)^r`,

so

```
pi_V(A_n)
 <= C_d (d-1)^{r_n}/n
 <= C_d (d-1)^{-(v a C/2)sqrt(L_n)} -> 0.          (7.7)
```

The mixture `nu_e exp(s(P-I))` assigns to `A_n` the lower bound in (7.6). Using (7.2),

```
lim_{C->infty} liminf_n d_H(T_n-C sqrt(L_n)) = 1. (7.8)
```

Together with (6.3), this proves cutoff at `T_n` with `O(sqrt(log n))` window.

## 8. Why this class is genuinely outside long-range expansion

Let `D_H=2(d-1)` be the degree of the line graph, so the LRE tree-growth base for `H` is

`Q_H=D_H-1=2d-3`.

Fix an edge `e={u,v}` of `G`. If another edge `f` lies at line-graph distance at most `r` from `e`, then one endpoint of `f` lies within base-graph distance at most `r` of `{u,v}`. Therefore

```
|B_H(e,r)|
 <= d |B_G({u,v},r)|
 <= C_d (d-1)^r.                                  (8.1)
```

But `d-1 < 2d-3` for every `d>=3`.

Suppose for contradiction that `(H_n)` were `c'`-LRE for some fixed `c'>0`. Take the singleton set `{e}` and

`r_n=floor((1/2) log_{2d-3} m_n)`.

For large `n`, the LRE minimum is in its growing branch, because `c'(2d-3)^{r_n}=O(sqrt(m_n))<3m_n/4`. Thus LRE would force

`|B_H(e,r_n)| >= c'(2d-3)^{r_n}`.

Equation (8.1) gives instead

```
|B_H(e,r_n)| / (2d-3)^{r_n}
 <= C_d [(d-1)/(2d-3)]^{r_n} -> 0,
```

a contradiction. Hence no fixed LRE constant exists.

This is stronger than merely observing that LRE and spectral expansion differ in general: it gives an explicit **vertex-transitive spectral-expander cutoff class outside LRE**.

## 9. Obstruction removed: extensive short-cycle modes are fast, not slow

The line graph has abundant short cycles: the `d` edges incident to every base vertex form a `K_d` in `L(G)`. Thus these examples deliberately destroy the tree-like local geometry that powers the LRE theorem.

Nevertheless the incidence factorization isolates those local cycles spectrally. On edge functions, every vector in `ker D` is annihilated by

`R=CD`.

Since `m=dn/2` and `rank(D)<=n`,

`dim ker D >= m-n = (d/2-1)n`,

so this is an extensive, positive-density sector for every `d>2`. By (4.2), a zero mode of `R` is an eigenmode of the continuous line generator `Q-I` with eigenvalue exactly

`-beta = -d/(d-1)`.

Therefore all endpoint-invisible local-cycle fluctuations decay at the **constant rate** `d/(d-1)`, on `O(1)` time, while the global mixing transition occurs at `Theta(log n)`.

This removes a concrete obstruction exposed by the older T08 work: failure of tree-like long-range growth, or even a positive-density local cycle/clique sector, does **not** by itself prevent cutoff. The real slow modes live in the endpoint-visible quotient and evolve exactly as a lazy base walk. This separation is algebraic/transitivity-based and does not use P26's entropy/Green mechanism.

## 10. Exact finite sanity check

A checker was written before persistence and executed with Python's exact `Fraction` arithmetic on both a nonbipartite and a bipartite cubic example (`K4` and `K3,3`). It verifies:

- `BB^T=A+dI` and `B^TB=A_{L(G)}+2I`;
- `Q-I=[d/(d-1)](CD-I)`;
- `DC=(I+P)/2`;
- `(CD)^k=C(DC)^(k-1)D` for `1<=k<=6`;
- the exact rate arithmetic `a T=tau`;
- the strict branching-base inequality `d-1<2d-3`.

Archived files:

- `2026-09-20T00-00-13Z__line_graph_incidence_checker.py`
- `2026-09-20T00-00-13Z__line_graph_incidence_checker.out`

Actual output ends with:

`ALL_EXACT_CHECKS_PASS`.

This is a self-check of the finite algebra, not an independent audit of the theorem.

## 11. Source-level progress versus mechanism progress

### Original Salez problem — before / after

**Before:** the full statement “every bounded-degree vertex-transitive expander sequence has cutoff” was OPEN. Published baselines included Ramanujan/near-Ramanujan and, as of 14 September 2026, fixed-degree long-range expanders. Historical R16 had a separate synchronous-tensor special-class candidate with square-root window.

**After:** the full Salez conjecture is still **OPEN / PARTIAL**. This run adds the proved class

`H_n = L(G_n)` for arbitrary fixed-degree edge-transitive LRE bases `G_n`,

where the resulting `H_n` are vertex-transitive spectral expanders that **fail LRE**, with

```
t_mix(epsilon)
 = [2(d-1)/(d-2)] log_{d-1}(2|V(H_n)|/d)
   + O_{d,c,epsilon}(sqrt(log |V(H_n)|)).
```

Thus the new window-to-center ratio is `O(1/sqrt(log |V(H_n)|)) -> 0`.

No finite experiment is being promoted to an asymptotic theorem; the asymptotic proof is on the page.

### Mechanism progress

The exact endpoint-incidence intertwining shows that a large short-cycle sector can be peeled off at constant rate, leaving a lazy quotient dynamics. This is the obstruction removal achieved in the same run.

## 12. Prior-art limits and next attack

Dated bounded searches checked Salez 2508.21055, Altschuler 2609.14945, Pedrotti--Salez 2607.05345, Salez's varentropy work, Bordenave--Lacoin covered expanders, Lubetzky--Peres Ramanujan cutoff, Kaufman--Lubotzky edge-transitive Ramanujan constructions, and direct searches for line-graph cutoff transfer. No exact theorem matching T08-NM01-1 was found in that bounded search, but this is **not** a worldwide novelty certificate.

The next genuinely different T08 step is to try to replace the **edge-transitive-LRE ancestry** by a condition stated directly on an arbitrary vertex-transitive spectral expander. The useful lesson is now precise: seek a transitive Markov factor/fiber decomposition in which the fiber sector has a uniform `O(1)` decay rate and the quotient captures the `Theta(log n)` transport. That route is complementary to P26's entropy/Green transfer and does not require pretending that arbitrary spectral expansion implies LRE.

## ledger_delta

A structured delta is saved beside this report as

`2026-09-20T00-00-13Z__ledger_delta.json`.

No shared root ledger, historical report, peer namespace, claim, schedule, permission, email/Drive object, public surface, or paid-compute resource was modified.
