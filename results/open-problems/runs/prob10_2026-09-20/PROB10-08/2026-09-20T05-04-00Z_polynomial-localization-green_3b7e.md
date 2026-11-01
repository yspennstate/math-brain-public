Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED** — GPT-6 maximum was requested, but authenticated runtime metadata does not establish GPT-6/maximum, so I do not claim it. **NO SOURCE-METRIC MOVEMENT:** Salez Problem 2.3 remains OPEN and historical `W_exp=1/2 provisional` is unchanged. **DIFFERENT-METHOD OBSTRUCTION PROVED:** non-cutoff forces positive heat-kernel mass on a polynomially sublinear set at a fixed mixing threshold; quantitatively, `n H_{2 t_mix}(o,o)=n^{o(1)}` at every fixed threshold is sufficient for cutoff, with an explicit window-ratio bound.

# PROB10-08 — polynomial localization and a subpolynomial Green criterion

Repository/branch: `yspennstate/math-open-problems` / `master`.

Status: **PARTIAL / OPEN / auxiliary reduction theorem proved / no new source graph class / independent validation pending / worldwide novelty UNVERIFIED**.

## 0. Required continuity, exclusions, and consumed updates

The required state was read before research:

- `operations/PROB10_2026-09-20.md`, current blob `6f0fcee836d93371d43b84af1a55150fedc80779`;
- current `POSTED.md`, blob `affe1b5f31545bb15be9ba2580548e9e88095e1b`; the posted Abelian Cayley/product-condition result remains excluded and is not this target;
- canonical `operations/claims/I0112.md`, blob `707af6a4ca81d0d6bcf52225c6f69c266ae981e9`;
- preserved R16 successor handoff `artifacts/prob10_2026-09-20/PROB10-08/2026-09-19T23-45-09Z_r16-h0002-handoff.md`, blob `fa18fa8669a638c362ad0f90300b733425e808e5`;
- newest own predecessor `runs/prob10_2026-09-20/PROB10-08/2026-09-20T03-58-30Z_affine-l2-spectral-barrier_d4c7.md`, blob `cbc8c02bc66e4a5331897d07d35bd4ddaaf07028`;
- historical stuck diagnosis `runs/R16/2026-09-16T22-43-00Z_i0112-stuck-recovery-1.md`, which records the moving-weight-Poincare/uniform-AEP obstruction and the exhausted product-varentropy, synchronous-tensor, Hecke/information-curvature, curvature and local-limit routes;
- newest neighboring P26 cutoff-transfer report `proofnet24/P26-progress-cutoff-transfer/runs/2026-09-20/2026-09-20_06-57-44__distance2-green-shell-transfer.md`, blob `6c74ae10ad9b700014cfc0d482e45f70eca33b1d`. P26's NBRW shell/distance-graph transfer direction is not duplicated here.

No old route was reset. The current affine stress-test theorem from the predecessor is used only as a falsification check: it showed that demanding actual L2 mixing at the TV scale is too strong.

A fresh bounded source check found Altschuler `arXiv:2609.14945` still at v1, submitted 14 September 2026, with no v2/correction/erratum surfaced. His theorem remains fixed-degree long-range-expander cutoff; its LRE premise is strictly stronger than spectral expansion and is not attributed to this track. Salez's source target remains Problem 2.3 in `arXiv:2508.21055` under rate-one continuous-time SRW.

## 1. Why this run satisfies the required obstruction/change-of-method rule

The preceding two own runs had no source-level TV metric movement. The contract therefore requires a written obstruction and a genuinely different method, not another L2 constant improvement.

This run changes the object from `chi^2 -> 0` to the **likelihood distribution under the heat-kernel law**. It proves that only a much weaker Green estimate is needed and identifies exactly what a counterexample must look like in its own mass. The retained statement is not a new graph-class theorem and is labelled auxiliary/reduction progress accordingly.

Three materially different approaches were compared:

1. **Likelihood-tail truncation + varentropy:** success; yields the quantitative theorem below.
2. **Ordinary spectral trace from the stationary gap:** fails; it still permits a polynomial doubled-time return excess, exactly as the affine stress test warns.
3. **Edge-expansion/coarea on the high-density set:** fails; many boundary edges do not force large heat flux when the density gaps across those edges are small, and the generic conversion loses the logarithmic factor that is fatal at `t_mix=Theta(log n)`.

Roughly all substantive effort was spent on these mathematical routes; there is no finite computation/checker because there is no finite core.

## 2. Main theorem proved this run

Freeze any source-admissible sequence `(G_n)` of connected `d_n`-regular vertex-transitive graphs with

`3 <= d_n <= D`, `|V_n|=n -> infinity`, and `gamma_n>=gamma>0`.

Let

`H_t=exp(t(P_n-I))`

be Salez's rate-one continuous-time semigroup. Fix `epsilon in (0,1/2)`, set

`t_n=t_mix^(n)(epsilon)`,

`w_n(epsilon)=t_mix^(n)(epsilon)-t_mix^(n)(1-epsilon)`,

and define

`R_n(epsilon)=n H_{2t_n}(o_n,o_n)`,

`rho_n(epsilon)=log R_n(epsilon)/log n`.

The matching proof artifact proves the following.

### Theorem A — quantitative doubled-time Green criterion

There is a constant `C=C(D,gamma,epsilon)` such that, for every `a in (0,1)` (the estimate is pointwise in `a`, with `C` independent of `a`),

`w_n(epsilon)/t_n`

` <= C [ 1/log n + a + sqrt(n^(rho_n-a)+n^(-a)) ].`            (2.1)

Consequently, if

`rho_n(epsilon)=o(1)`, i.e.

`n H_{2t_mix(epsilon)}(o_n,o_n)=n^{o(1)}`,                     (2.2)

then taking

`a_n=rho_n+4 log log n/log n`

gives

`w_n(epsilon)/t_n`

` = O_{D,gamma,epsilon}(rho_n+log log n/log n)=o(1).`           (2.3)

Thus (2.2) for every fixed `epsilon in (0,1/2)` implies total-variation cutoff.

This is strictly weaker than L2 mixing at `t_n`: since

`chi^2(H_{t_n}(o_n,.),pi_n)=R_n-1`,

`chi^2` is allowed to diverge subpolynomially.

## 3. Complete proof mechanism

The full proof is in

`artifacts/prob10_2026-09-20/PROB10-08/2026-09-20T05-04-00Z_polynomial-localization-green_3b7e.md`,

created at commit

`7a50482acaa460092c8ef867c821705b0421da34`

and read back at that exact commit.

The essential steps are short enough to record here as an audit map.

### Step 1 — information has only polynomial range at `t_mix`

Uniform bounded degree and spectral gap imply

`t_n=Theta(log n)`

and `diam(G_n)=O(log n)`. The lower mixing-time bound follows from the Poisson jump count plus the size of a bounded-degree ball; the upper bound follows from the stationary spectral gap. For any `y`, a geodesic of length `r=O(log n)` contributes the term

`e^{-t_n} t_n^r/(r! d_n^r)`

to the continuous-time kernel. Since also `t_n>=c log n`, there is a uniform `K<infinity` such that

`|log(nH_{t_n}(o_n,y))| <= K log n`.                            (3.1)

### Step 2 — two exact moments control opposite likelihood tails

Let

`mu_n(y)=H_{t_n}(o_n,y)`, `Z_n(y)=n mu_n(y)`, `Y_n~mu_n`.

Reversibility and the semigroup identity give

`E_mu Z_n = n sum_y mu_n(y)^2 = nH_{2t_n}(o_n,o_n)=R_n`.        (3.2)

There is also the exact reciprocal identity

`E_mu Z_n^{-1}=1`.                                             (3.3)

Therefore, for every `a>0`,

`P_mu(Z_n>=n^a) <= n^(rho_n-a)`,                               (3.4)

`P_mu(Z_n<=n^(-a)) <= n^(-a)`.                                 (3.5)

The negative polynomial tail is universally negligible; only positive polynomial overweight can obstruct information concentration.

### Step 3 — truncate varentropy

Put

`W_n=log Z_n(Y_n)/log n`.

Using (3.1), split according to `|W_n|<=a`, `W_n>a`, `W_n<-a`. Then

`Var(W_n) <= a^2+K^2[n^(rho_n-a)+n^(-a)]`.                     (3.6)

Thus

`V_KL^(n)(t_n)`

` <= (log n)^2 {a^2+K^2[n^(rho_n-a)+n^(-a)]}.`                 (3.7)

Salez's general varentropy width theorem gives

`w_n(epsilon) <= C_epsilon gamma_n^{-1}`

`                 [1+sqrt(V_KL^(n)(t_n))]`.                    (3.8)

Since `gamma_n>=gamma` and `t_n>=c(D)log n`, (2.1) follows. Constants in the truncation are independent of `a`, so the `n`-dependent choice used in (2.3) is legitimate.

## 4. Stronger obstruction: a counterexample must macroscopically localize

Define the high-likelihood set

`B_n(a)={y:nH_{t_n}(o_n,y)>=n^a}`

and its own-law mass

`L_n(a)=H_{t_n}(o_n,B_n(a))`.

The proof establishes a second theorem.

### Theorem B — polynomial-delocalization criterion

If for every fixed `epsilon in (0,1/2)` and every fixed `a>0`,

`L_n(a) -> 0`,                                                  (4.1)

then `(G_n)` has TV cutoff.

Indeed, (3.5), (4.1), and the compact range (3.1) imply

`V_KL(t_n)=o(log^2 n)`,

and then Salez's criterion closes.

Therefore any genuine counterexample to Problem 2.3 must have fixed constants

`epsilon in (0,1/2)`, `a>0`, `b>0`

and a subsequence for which

`H_{t_mix(epsilon)}(o_n,B_n(a)) >= b`,                          (4.2)

while, automatically,

`|B_n(a)| <= n^(1-a)`.                                         (4.3)

This is stronger than saying the L2 norm is large: a **positive amount of the walk's own probability mass** must be concentrated on a polynomially sublinear set.

By Cauchy--Schwarz, (4.2)--(4.3) imply

`n H_{2t_mix(epsilon)}(o_n,o_n) >= b^2 n^a`.                   (4.4)

So any counterexample necessarily has polynomial doubled-time on-diagonal heat-kernel excess. The converse is not asserted; the preceding affine run is precisely a warning that polynomial chi-square excess can be caused by a rare spike whose own mass vanishes.

## 5. Why the two attempted closures fail

### 5.1 Stationary spectral gap cannot prove (2.2)

The ordinary trace estimate is only

`R_n(t) <= 1+(n-1)e^{-2gamma t}`.                               (5.1)

At a generic `Theta(log n)` mixing time this can remain `n^c` for fixed `c>0`. Nothing in an ordinary spectral gap alone turns (5.1) into `n^{o(1)}`. The previous affine source-admissible example makes this obstruction concrete and prevents counting another stationary spectral estimate as a new route.

### 5.2 Edge expansion alone cannot eliminate (4.2)

A polynomially small superlevel set has a large edge boundary in an expander. But heat flow across an edge is controlled by the **density difference** across that edge. An arbitrarily large boundary can sit almost entirely inside a narrow likelihood band, producing small flux. Coarea/dyadic arguments without further transitivity-sensitive regularity recover only the familiar logarithmic loss, not a sharp mixing window. This is the point where the old moving-weight-Poincare route stalled; the new formulation makes the missing object concrete: rule out positive own-law mass on polynomially small superlevel sets, rather than trying to prove a Poincare inequality for every evolving weight.

## 6. Relation to Altschuler and neighboring work

Altschuler's long-range expansion is used to make the NBRW endpoint entropy nearly maximal before a short entropy-cleanup stage. Theorem A gives a formally weaker cleanup input for the **actual heat kernel**: subpolynomial doubled-time return density at the mixing scale is enough. This does not show that transitivity plus ordinary expansion implies that estimate.

P26's current route is deliberately nonduplicated: it proves shell/NBRW collision transfer theorems and explicit distance-graph classes. Theorem A uses no shell graph, no distance transform, and no graph transfer. Its obstruction applies directly to a hypothetical source counterexample.

The old R16 product-varentropy, synchronous-tensor, moving-weight/local-Poincare, Hecke/information-curvature, tree-subcommutation and local-limit failures remain preserved and are not re-labelled as progress.

## 7. Self-check and artifact readback note

No finite computation, simulation, or finite mixing plot was run. There is no finite core requiring an exact checker. The proof uses only exact semigroup identities, Poisson support, Cheeger growth, Markov/Cauchy--Schwarz inequalities, and Salez's published varentropy width theorem.

The proof artifact was read back at its creation commit. One harmless internal cross-reference typo was noticed on readback: in artifact §6, “Lemma 4.2's negative-tail estimate” means **Lemma 4.1**. The mathematical inequality cited is displayed explicitly as (4.2) there, so no proof content changes. Also, artifact (5.4) is derived with constants uniform in `a`; therefore its subsequent application to the `n`-dependent `a_n` is valid despite the preceding prose saying “fixed `a`.” This report records that quantifier precisely.

These are self-checks, not independent audits.

## 8. Source before/after and structured ledger delta

```yaml
ledger_delta:
  target: "Salez arXiv:2508.21055 Problem 2.3"
  source_status_before: "OPEN / PARTIAL"
  source_status_after: "OPEN / PARTIAL"
  source_metric: "W_exp"
  source_metric_before: "1/2 provisional"
  source_metric_after: "1/2 provisional"
  source_metric_movement: false
  mechanism_before: "actual L2 can be polynomially bad at a tree-scale benchmark; near-L2 mixing cannot be the universal mechanism"
  mechanism_after: "proved subpolynomial doubled-time Green sufficient condition and necessary macroscopic polynomial-localization obstruction for every counterexample"
  independent_audits: 0
  finite_checker: "not applicable"
  status_label: "OPEN/PARTIAL"
```

This is the third consecutive own run without source-level TV metric movement, so it does **not** continue the same route. It supplies the required obstruction and changes method from L2 spectral analysis to own-law likelihood tails/Green localization.

## 9. Remaining full-scope gap

The next legitimate source-level target is now sharply delimited:

> Prove, using vertex transitivity plus a uniform spectral gap alone, that at every fixed mixing threshold either
>
> `H_{t_mix}(o,{y:nH_{t_mix}(o,y)>=n^a}) ->0` for every fixed `a>0`,
>
> or at least
>
> `nH_{2t_mix}(o,o)=n^{o(1)}`.

Ordinary spectral trace, generic edge expansion, the old moving-weight Poincare route, and near-uniform L2 mixing are insufficient. A successful next route must use a genuinely transitivity-sensitive mass-transport, positive-definite, representation-theoretic, or Green-function mechanism to exclude the macroscopic polynomial localization (4.2)--(4.3), or else construct a source-admissible family realizing it and thereby produce a credible counterexample direction.

No scheduler state, cadence, enabled state, email, Drive object, public posting, permissions, shared ledger, peer-track files, workflows, or force push were changed.
