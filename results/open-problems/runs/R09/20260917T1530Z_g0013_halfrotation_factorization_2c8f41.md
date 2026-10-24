Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — NO MOVEMENT on active R09 successor G0013: `U_* = 1/9 -> 1/9`; Tang remains RETIRED/FROZEN at `UNBOUNDED_ABOVE` with supported retirement count `6`, and G0002 remains handed off at `Delta_8=UNMEASURED`. Methods used: B5 ADD A PARAMETER AND DIFFERENTIATE IN IT, B24 FIND THE EXTREMAL OBJECT, B13 FIND WHAT ONLY INCREASES.** GPT-6 / maximum was requested in prompt text, but the exposed scheduler surface still has no model-family selector, no reasoning-effort selector, and no authenticated applied-run telemetry, so I do not claim otherwise.

# R09 CLOSABLE OUTSIDE — G0013 third active run: exact half-rotation shuffle and the piece-merging obstruction

Date: 2026-09-17 UTC.  
Repository / branch: `yspennstate/math-open-problems` / `master`.

## 1. Continuity and controlling state

I did **not** reopen Tang Question 4.11. Its R09 periodic-tree work remains retired/frozen. I also did not reopen G0002 / Cerf 53.1, which remains handed off.

The controlling exclusive claim is `operations/claims/G0013.md`. With `lambda=Unif[0,1]`, `nu=lambda tensor lambda`,

`M = sup_{pi in Pi(lambda,lambda)} W_2^2(pi,nu)`.

Catalano--Lavenant conjecture `M=1/10`, with the diagonal and antidiagonal maximizers. The frozen R09 metric is

`U_* = smallest rigorous source-valid global upper bound on M established by R09`.

The preceding complete report `runs/R09/20260917T1431Z_g0013_chatterjee_jacobi_bound_1f6a93.md` proved the full-class bound `U_*=1/9`, via the exact Chatterjee-xi/Brenier representation and the sharp Wright--Fisher/Jacobi Poincare inequality. Therefore this run starts at

`1/10 <= M <= 1/9`.

### Required continuity reads

Before new work I reread/recovered the campaign `INDEX.md` and `RANKING.md`, root `POSTED.md`, root `RESULTS.md`, `QUEUE.md`, `operations/NEW_METHODS_2026-09-16.md`, the owner directive, the active G0013 claim, the newest complete R09 report, the prior G0013 finite-grid script, and the newest available neighboring R08 report. Repository-wide search again showed G0013 as an exclusive R09 claim; another current track explicitly excludes it for that reason.

Large intake JSONL ledgers are not rendered byte-for-byte by the connector in one response; I used the canonical G0013 claim plus exact-ID repository searches and preserved prior-attempt pointers rather than falsely claiming a visual reread of all intake rows.

## 2. Fresh source/current-literature/status check

Primary source: Marta Catalano and Hugo Lavenant, *Measures of Dependence based on Wasserstein distances*, arXiv:2510.06034, Remark 3. The source explicitly says that for the classical Euclidean quadratic Wasserstein distance and two uniform marginals the supremum problem is open and conjectures the monotone/antimonotone couplings.

Later source: Stefan Schrott, *Couplings Farthest from the Independent Gaussian*, arXiv:2609.10467v1, submitted 2026-09-09. Its abstract still describes the uniform statement as the Catalano--Lavenant conjecture and proves the Gaussian analogue instead.

Fresh bounded searches on 2026-09-17 included the exact source title/authors, Schrott's title, uniform-copula Wasserstein maximization, circular/rotation shuffles of Min, and Wasserstein distance of shuffles of Min from independence. I found no later source-matching resolution and no source stating the exact half-rotation calculation below. This is bounded negative evidence only: **publication novelty remains UNVERIFIED**.

## 3. B5 — add a circular-shuffle parameter; the midpoint factorizes exactly

Instead of perturbing the Brenier deficit directly, put the conjectured diagonal into the one-parameter deterministic-copula family

`g_c(s) = (s+c) mod 1`,  `0 <= c <= 1`,

and let

`pi_c = Law(S,g_c(S))`,  `S ~ Unif[0,1]`.

Thus `pi_0` is the diagonal copula. Swapping the two coordinates sends `pi_c` to `pi_{1-c}`; since the independent square and Euclidean cost are swap-invariant,

`W_2^2(pi_c,nu)=W_2^2(pi_{1-c},nu)`.                         (3.1)

The midpoint `c=1/2` is special. I can solve its transport problem exactly.

> **Proposition (exact half-rotation value).** Let
>
> `pi_H = Law(S, (S+1/2) mod 1)`.
>
> Then
>
> `W_2^2(pi_H, lambda tensor lambda) = 1/20`.                 (3.2)

### Proof

Let `(X,Y)~nu` and introduce the orthogonal coordinates up to scale

`Z=X+Y`,  `D=Y-X`.

For a target point `(U,V)`, similarly write `Z'=U+V`, `D'=V-U`. Then exactly

`(X-U)^2+(Y-V)^2 = [(Z-Z')^2+(D-D')^2]/2`.                  (3.3)

For the half-rotation target:

- when `0<=S<1/2`, `(U,V)=(S,S+1/2)`, hence `D'=+1/2` and `Z'=2S+1/2`;
- when `1/2<=S<=1`, `(U,V)=(S,S-1/2)`, hence `D'=-1/2` and `Z'=2S-1/2`.

Therefore under `pi_H`,

`Z' ~ Unif[1/2,3/2]`,
`D' ~ (delta_{-1/2}+delta_{+1/2})/2`,

and, crucially, **`Z'` and `D'` are independent**, because the conditional law of `Z'` is the same uniform interval in each sign branch.

For the source square, `Z` has triangular density

`f_Z(z)=z` on `[0,1]`, `f_Z(z)=2-z` on `[1,2]`.

In `(Z,D)` coordinates the square is

`|D| <= min(Z,2-Z)`

with constant density `1/2`. Hence conditional on any admissible `Z=z`, `D` is uniform on a symmetric interval. It follows that `sgn(D)` is a fair sign **independent of `Z`** (the null event `D=0` is irrelevant).

Now define

`Z' = 1/2 + F_Z(Z)`,
`D' = (1/2) sgn(D)`.                                        (3.4)

Because `F_Z(Z)` is uniform on `[0,1]` and `sgn(D)` is independent of `Z`, (3.4) has exactly the target product law just described, hence inverting

`U=(Z'-D')/2`, `V=(Z'+D')/2`

gives exactly `pi_H`.

Moreover, (3.4) simultaneously realizes the **one-dimensional monotone optimal couplings** in both coordinates:

- `Z -> 1/2+F_Z(Z)` is the quantile coupling from the triangular law of `Z` to `Unif[1/2,3/2]`;
- `D -> sgn(D)/2` is the quantile coupling from the symmetric triangular law of `D` to the two-point law at `+-1/2`.

For any coupling to `pi_H`, (3.3) therefore gives the marginal lower bound

`cost >= (1/2) W_2^2(Law(Z),Unif[1/2,3/2])`
`       + (1/2) W_2^2(Law(D),(delta_-1/2+delta_+1/2)/2)`.     (3.5)

The coupling (3.4) attains both marginal lower bounds simultaneously, so (3.5) is equality and is the global two-dimensional optimum.

The two exact contributions are

`C_D = int_0^1 (d-1/2)^2 (1-d) dd = 1/24`,                 (3.6)

and, with `F_Z(z)=z^2/2` on `[0,1]` and `F_Z(z)=1-(2-z)^2/2` on `[1,2]`,

`C_Z = (1/2) int_0^2 [z-(1/2+F_Z(z))]^2 f_Z(z) dz = 1/120`. (3.7)

Thus

`W_2^2(pi_H,nu)=C_D+C_Z=1/24+1/120=1/20`.                  (3.8)

QED.

The exact-rational self-check for (3.6)--(3.8) is

`artifacts/R09/20260917T1530Z_g0013_halfrotation_exact.py`

and its executed output is

`artifacts/R09/20260917T1530Z_g0013_halfrotation_exact.out`.

The output is

`D_component=1/24`
`Z_component=1/120`
`total_W2_squared=1/20`
`PASS`.

The checker source was created at commit `64c03e65472639d1deb233e936c4be0e4d7b84c8`; the archived output at `4a628388512270f8c359b221f09aa72c25f5aa10`.

### What the parameter revealed

The midpoint does **not** challenge the conjectured extremizer: it is exactly half as far from independence in squared `W_2` as the diagonal,

`W_2^2(pi_{1/2},nu)=1/20 < 1/10 = W_2^2(pi_0,nu)`.

The useful mechanism is the factorization in rotated `(Z,D)` coordinates. At `c=1/2`, the target's sum coordinate and difference-sign coordinate become independent, allowing the 2D transport problem to split into two 1D monotone transports. For general `c`, the two sign branches have different `Z'` intervals, so this exact product factorization disappears. That pinpoints a concrete obstruction to differentiating an explicit closed formula in `c`.

## 4. B24 — the extremal-object guess becomes a piece-coarsening problem

The previous run already established the legitimate density reduction: shuffles of Min are dense in the copula class and the original `W_2` functional is continuous, so it is enough, in principle, to control arbitrarily fine deterministic shuffles. This run asks what geometry should make the one-piece diagonal extremal among those shuffles.

The exact half-rotation calculation suggests the following **strategy, not theorem**:

> Fragmenting a monotone graph into translated pieces tends to create an additional discrete difference-coordinate degree of freedom, which gives the independent square more ways to match the target and can lower the optimal cost. Conversely, a coarsening operation that merges compatible shuffle pieces might increase distance from independence, terminating at the diagonal or antidiagonal.

The half-rotation is the cleanest nontrivial test: two equal parallel diagonal pieces have exact cost `1/20`, whereas their one-piece diagonal endpoint has exact cost `1/10`.

This reframes the source conjecture as an extremal operation problem: define a source-valid merge on shuffle intervals and prove that it cannot decrease `W_2^2(pi,nu)`. Iterating would reduce arbitrary same-orientation shuffles to a single diagonal segment; mixed orientations would require a second merge/reflection rule.

No such merge inequality is proved here. Accordingly this is research direction, not movement of `U_*`.

## 5. B13 — attempt a monovariant; identify exactly why the naive proof fails

I tried to promote the piece-coarsening heuristic into a monovariant. The obvious tools do **not** give it:

1. `pi -> W_2^2(pi,nu)` is convex, but a deterministic shuffle is generally an extreme copula, so merging two graph pieces is not naturally a convex averaging operation between the pre-merge and post-merge copulas.
2. The merge is also not obviously a Wasserstein displacement interpolation with `nu` fixed. Thus geodesic convexity does not give the desired direction.
3. In the circular family `pi_c`, the exact symmetry `c <-> 1-c` and the solvable midpoint do not by themselves imply monotonicity from `c=0` to `1/2`. Exploratory finite-grid calculations do not support treating this one-parameter value as a simple monotone function, so I do not promote that claim or archive it as a theorem.

Thus the **failed step is precise**: a useful merge theorem needs a coupling-level comparison that survives re-optimization of the transport plan. It cannot be obtained merely from convexity of `W_2^2` in the target measure.

This failure is valuable because it tells the next run not to spend time differentiating a guessed smooth `c -> W_2^2(pi_c,nu)` formula. The more promising object is a local rearrangement inequality for the transport dual or Brenier deficit under one explicit shuffle merge.

## 6. Metric, status, and exact scope

The active global metric does **not** move this run:

`U_* : 1/9 -> 1/9`.

This is the first supported unchanged G0013 run after two consecutive metric improvements (`UNMEASURED -> 1/6 -> 1/9`). The source remains **OPEN / PARTIAL** in R09.

The exact new restricted theorem is

`W_2^2(Law(S,(S+1/2) mod 1), lambda^2)=1/20`.

It is source-relevant but it is a single deterministic shuffle, hence **PARTIAL** and does not change the frozen global upper-bound metric.

No closure is claimed. In particular, I do not claim that every two-piece shuffle is controlled, that piece merging is monotone, or that the source conjecture is proved.

## 7. Next genuinely different methods

If G0013 remains active next run, do **not** repeat B5/B24/B13. The next useful triple is:

- **B4 PROVE SOMETHING WEAKER, COMPLETELY:** solve the full two-piece equal-orientation shuffle class, not just the symmetric half-rotation;
- **B18 SAY IT IN ANOTHER LANGUAGE:** formulate one shuffle-piece merge in Kantorovich dual variables / convex order of `(Z,D)` sections;
- **B20 FIND WHY THE ALGORITHM FAILS:** write the candidate local merge algorithm and isolate the exact transport-plan obstruction when orientations or interval lengths differ.

A stronger alternative is to return to the global deficit identity only if one of these operations gives a quantitative contribution to the missing `1/60` deficit.

## 8. Model / scheduler control status

The scheduler limitation is still the same in the interface actually exposed to this run. It offers task title, prompt, schedule/start-offset, enabled state and timing mode. It exposes **no model-family selector, no reasoning-effort selector, and no authenticated completed-run model telemetry**. Therefore GPT-6/maximum remains a prompt request, not an enforceable or verifiable runtime setting here.

To make it enforceable, the product/API must expose model and reasoning fields for the task plus applied-run telemetry, or the task must be administered from an authorized owning surface that exposes those controls.

The historical `You cannot modify this task` response for P26 was authorization-context dependent: repository evidence records that P26 was later updated successfully from another authorized context, while another context denied it and several other tasks. The lawful workaround is the owning authorized context, an ownership/admin transfer, or platform support. It is **not** task duplication, permission bypass, or a repository-only edit.

No scheduler modification, email, Drive write, public posting, purchase, permission change, workflow execution, shared-root edit, or peer-file edit was performed in this run.

## 9. Structured ledger_delta

```json
{
  "track": "R09",
  "predecessors": {
    "Tang-2020-Q4.11": {
      "metric": "UNBOUNDED_ABOVE",
      "status": "RETIRED_FROZEN",
      "supported_retirement_count": 6
    },
    "G0002": {
      "metric": "Delta_8=UNMEASURED",
      "status": "HANDOFF_FROM_R09"
    }
  },
  "active": {
    "target": "G0013 / Catalano-Lavenant uniform-copula Wasserstein conjecture",
    "metric": "U_* = smallest rigorous source-valid global upper bound on M",
    "before": "1/9",
    "after": "1/9",
    "movement": "NO_MOVEMENT",
    "supported_unchanged_runs_on_G0013": 1,
    "status": "PARTIAL / OPEN_CURRENT"
  },
  "new_exact_restricted_result": {
    "family": "half-rotation shuffle g(s)=(s+1/2) mod 1",
    "value": "W_2^2=1/20",
    "scope": "PARTIAL; single deterministic shuffle; does not move U_*",
    "checker": "artifacts/R09/20260917T1530Z_g0013_halfrotation_exact.py",
    "checker_output": "artifacts/R09/20260917T1530Z_g0013_halfrotation_exact.out",
    "checker_status": "PASS"
  },
  "methods": [5, 24, 13],
  "next_methods": [4, 18, 20],
  "publication_novelty": "UNVERIFIED"
}
```
