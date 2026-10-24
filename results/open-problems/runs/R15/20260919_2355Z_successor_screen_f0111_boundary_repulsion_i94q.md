Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — not GPT-6 maximum. NATIVE I0076 METRIC NO MOVEMENT: `NOT_SCOREABLE_NO_SURVIVING_FROZEN_CANDIDATE -> NOT_SCOREABLE_NO_SURVIVING_FROZEN_CANDIDATE`. RETAINED-SCREEN MOVEMENT: the positive-mass polygon attack on the first `n=30` branch fails for an exact structural reason, but exact value contact plus block symmetrization proves a new boundary-repulsion theorem: no block-constant two-level Hessian-null exact quadratic contact can accumulate at the sharp outer boundary `z downarrow 1`. Methods #6, #14, #24.**

Repository / branch: private `yspennstate/math-open-problems` / `master`.  
Worker: R15, CLOSABLE OUTSIDE.  
Native source: Krzysztof Burdzy and Michael Scheutzow, *Forward Brownian Motion*, arXiv:1302.6958 / PTRF 160 (2014), Problem 7.2, intake I0076.  
Retained screen only: Michel Talagrand, *Are Many Small Sets Explicitly Small?*, STOC 2010, Problem 10.9 / F0111, specialized to the `k=2` hazard. F0111 remains **PENDING / SELF_CHECK_ONLY / NOT CLAIMED / NOT READY**.

## 1. Repository/source continuity and dispatch state

I began by rereading the current campaign `INDEX.md` and `RANKING.md`, root `POSTED.md`, `RESULTS.md`, `QUEUE.md`, `operations/FOLLOWUP_IMPLEMENTATION_2026-09-16.md`, the newest R15 report, the retired I0076 handoff, the intervening R15 successor claims/handoffs, and fresh successor-gate deltas from neighboring CLOSABLE workers.

The exact Burdzy--Scheutzow definitions remain controlling. `X` is FBM if there are random times `S_n -> -infinity` a.s. such that every centered future `(X_{S_n+t}-X_{S_n})_{t>=0}` is standard Brownian motion; BBM is the time-reversed notion; 2BM requires one random time at which the complete centered future and complete centered past are independent standard Brownian motions. Problem 7.2 assumes FBM + BBM and the existence of an arbitrary random real `T` at which the two complete centered half-processes are independent. It does **not** require `T` to be a stopping time and does **not** separately assume that either seam half is Brownian. Problem 7.5 is distinct and excluded.

The controlling six-run I0076 handoff remains `runs/R15/20260916_2354Z_i0076_sixrun_handoff_phasefield_a20.md`: the source-Theorem-6.1 construction has FBM, BBM and non-2BM but no source-valid independent seam; the later Brownian-prefix/BES construction has FBM, BBM and exact seam independence but was proved to be 2BM. Thus there is no surviving frozen counterexample candidate on which the four-obligation metric can honestly be rescored. The historical `2/4` is a retired positive-route handoff value, not a current candidate score.

Operational continuity also matters. R15 subsequently owned RS-2026-CL-B and I0124; both reached their mandatory CLOSABLE handoffs and are retired. The I0124 six-run handoff is `runs/R15/20260917_1857Z_i0124_sixrun_handoff_games_h38.md`. Fresh successor screens from multiple neighboring CLOSABLE gates through this invocation still report no lawful free READY+CLOSABLE successor. I therefore do not reopen I0076, RS-2026-CL-B or I0124, do not steal an owned target, and do not promote a PENDING queue row.

The newest prior R15 report is `runs/R15/20260919_2347Z_successor_screen_f0111_projective_polygon_h93p.md`. It proved an exact Gram-polygon criterion for the PSD/null/projective-fourth-order subsystem of a two-level mixed Hessian-null contact. This run continues that retained screen only because the native CLOSABLE lane has no lawful admitted successor.

## 2. Prior scalar notation

For the `k=2` hazard

`F(t)=sum_i t_i - log S(t)`,  `S(t)=sum_i exp(t_i)-(n-1)`,

let a nonnegative-coefficient quadratic global majorant `P` be exact at an interior point `q`, and put `G=P-F`, `H=D^2G(q)>=0`.

For a two-level mixed null direction normalize the irrelevant common scale to one and write

`h=(1+delta) 1_J - (1-delta) 1_K`,  `0<delta<1`,

with `M=|J|`, `N=|K|`, `n=M+N` in the full-support case. Put

`r_i=exp(q_i)/S(q)`, `x=sum_J r_i`, `y=sum_K r_i`, `k=1-x-y=-(n-1)/S(q)`.

The preceding cubic-null reduction uses a scalar `z` for which the weighted directional mean is exactly

`p:=sum_i r_i h_i = delta+z`.

On the `z>1` outer branch,

`k = 2 z(1-z^2)/((1-delta^2)(delta+3z)) < 0`,

`x = ((delta+z)(1+z)(1+delta+2z))/(2(1+delta)(delta+3z))`,

`y = ((delta+z)(1-z)(1-delta-2z))/(2(1-delta)(delta+3z))`.

The prior projective calculation defines positive cap factors `A_J,A_K` such that the residual diagonal condition is

`r_i <= 1/A_J` on `J`, `r_i <= 1/A_K` on `K`.

For a full-support interior contact one also has the strict lower bound

`r_i > rho := -k/(n-1)`

because `q_i>0` implies `exp(q_i)>1` and `S(q)=(n-1)/(-k)`.

The previous dimension barrier showed that any full-support two-level null contact on `z>1` needs `n>=30`, with the sharp scalar lower bound approached only at `z downarrow 1`, `delta -> 1/2`.

## 3. #6/#24 first attack — why the positive-mass polygon route does **not** close n=30

The research idea was written before any computation/checking at

`artifacts/R15/f0111_n30_polygon_lowerbound_i94q_idea.md`

and committed/read back at `ea0d335a54b384e55c3c8ab8c13f370d2a1ae302`.

The first plan was to combine the new strict lower mass `rho` with the exact Gram-polygon criterion and rule out the first possible dimension `n=30`. That route fails for a clean reason which is itself useful.

Suppose `M,N>=2` and the aggregate interval conditions permit the block-uniform masses

`r_i=x/M` on `J`, `r_i=y/N` on `K`,

namely

`rho < x/M <= 1/A_J`,  `rho < y/N <= 1/A_K`.      (3.1)

The projective polygon lengths are then constant inside each block:

`L_J=(1+delta)sqrt((x/M)(1-A_J x/M))`,

`L_K=(1-delta)sqrt((y/N)(1-A_K y/N))`.

If `L_J>=L_K`, the total polygon length is at least `M L_J>=2L_J`; if `L_K>=L_J`, it is at least `N L_K>=2L_K`. Hence the exact polygon criterion

`2 max_i ell_i <= sum_i ell_i`

is automatically satisfied. Thus the strict positive lower bound does **not** strengthen the exact projective-local subsystem whenever both sign blocks have at least two coordinates and equalization is admissible.

This identifies the exact failure of the initial route: the Gram-polygon theorem from the previous run already solved all information contained in the local PSD/diagonal/null/projective budget, and permutation-symmetric mass allocations can saturate that local feasibility. To get further one must inject exact value/gradient contact or genuinely global majorization.

## 4. #14 — symmetrize an exact block-constant contact

The failed route points to the right extremal object. Assume now that the **contact itself** is block constant:

`q_i=u` on `J`,  `q_i=v` on `K`,

so necessarily

`r_J:=r_i=x/M`,  `r_K:=r_i=y/N`.

If any quadratic global majorant `P` is exact at this `q` and has the above null vector `h`, average `P` over the group `S_M x S_N`. Because `F`, `q` and `h` are invariant under this group, averaging preserves:

- coefficient nonnegativity;
- global majorization `P>=F`;
- exact value and gradient contact at `q`;
- `H>=0`;
- the null equation `Hh=0`.

Therefore it is enough to study the block-symmetric certificate

- singleton coefficients `alpha` on `J`, `gamma` on `K`;
- pair coefficient `beta_J` inside `J`;
- pair coefficient `beta_K` inside `K`;
- cross coefficient `eta` between `J` and `K`.

The null equations are exact. Since `p=delta+z`, put

`a=1+delta`, `b=1-delta`, `epsilon=z-1>0`.

Then

`a(M-1) beta_J - bN eta = r_J epsilon`,              (4.1)

`aM eta - b(N-1) beta_K = r_K(z+1)`.                (4.2)

Exact value contact can be written without `alpha,gamma`. Gradient contact gives

`sum_{i<j} B_ij q_i q_j = E`,

where

`E := log S(q) - x u - y v`.                         (4.3)

Thus

`C(M,2) beta_J u^2 + C(N,2) beta_K v^2 + MN eta uv = E`.    (4.4)

Substituting (4.1)--(4.2) into (4.4) gives the exact identity

`E = [MN/(2ab)] (b u + a v)^2 eta
     + [M r_J epsilon/(2a)] u^2
     - [N r_K(z+1)/(2b)] v^2`.                       (4.5)

No approximation has been used in (4.1)--(4.5).

## 5. #6 — boundary deformation and the new repulsion theorem

### Theorem R15-BR — symmetric outer-boundary repulsion

Fix `0<delta<1` and integers `M,N>=2`. Along the cubic-null `z>1` outer branch, there is **no sequence** of block-constant interior exact quadratic contacts with Hessian null vector

`h=(1+delta)1_J-(1-delta)1_K`

and `z downarrow 1`.

Equivalently: for every fixed `(delta,M,N)` there exists `epsilon_0>0` such that no such contact exists whenever

`1<z<1+epsilon_0`.

This is a necessary-condition theorem for the retained F0111 `k=2` screen; it is not a solution of Problem 10.9.

### Proof

Let `epsilon=z-1 ->0+`. The exact scalar formulas above give

`k = -kappa epsilon + O(epsilon^2)`,

with

`kappa = 4/((1-delta^2)(delta+3)) >0`,

and

`x=1+O(epsilon)`, `y=O(epsilon)`.

Hence

`S(q)=(n-1)/(-k)=Theta(epsilon^{-1})`,

`r_J=1/M+O(epsilon)`, `r_K=O(epsilon)`.

Because the contact is block constant,

`u=log(S r_J)=log(1/epsilon)+O(1) -> infinity`,

while

`v=log(S r_K)=O(1)`.

Also

`E=log S-xu-yv -> log M`.                            (5.1)

Indeed `u=log S+log x-log M`, so

`E=(1-x)log S-x log x+x log M-yv`,

and every term except `x log M` has limit zero.

In (4.5), the two correction terms tend to zero because

`epsilon u^2 ->0`, `r_K=O(epsilon)`, `v=O(1)`.

Therefore, using `u->infinity` and bounded `v`, (4.5) yields

`eta u^2 -> 2a log M/(MN b)`.                        (5.2)

Now solve (4.2) for `beta_K`:

`beta_K = [aM eta-r_K(z+1)]/[b(N-1)]`.

Multiplying by `u^2` and using (5.2) plus `r_K u^2->0`,

`u^2 beta_K -> 2 a^2 log M/(b^2 N(N-1)) >0`.        (5.3)

But the contact Hessian has diagonal entry

`H_ii=r_K-r_K^2`

on `K` and off-diagonal entry

`H_ij=beta_K-r_K^2`

for distinct `i,j in K`. Hence every vector supported on `K` and orthogonal to `1_K` is an eigenvector with eigenvalue

`lambda_K = r_K-beta_K`.                             (5.4)

Combining (5.3) with `r_K u^2->0` gives

`u^2 lambda_K -> - 2 a^2 log M/(b^2 N(N-1)) <0`.

Thus `lambda_K<0` for all sufficiently small `epsilon`, contradicting the necessary condition `H>=0`. This proves the theorem. QED.

### Sharp interpretation

The previous `n>=30` projective dimension bound on the `z>1` branch is sharp only at the scalar boundary `z downarrow1`, `delta->1/2`. The theorem above shows that the most symmetric realization of that sharp boundary is **not** an actual exact contact: exact value contact forces a within-`K` negative Hessian eigenvalue of order `1/(log(1/epsilon))^2`, whereas the hazard mass `r_K` is only order `epsilon`.

So a genuine first `n=30` survivor, if one exists at all, must exploit **within-block heterogeneity**. The equal-mass extremal configuration that makes the projective Gram-polygon constraints easiest cannot realize the sharp boundary.

This is a stronger conclusion than another aggregate dimension inequality: it identifies the precise scale mismatch that destroys the symmetric boundary candidate.

## 6. What moved, what failed, and the next route

The initial positive-mass polygon attack did not close `n=30`; its exact failure is Section 3. The new movement is Theorem R15-BR, which couples three ingredients not previously used together in this retained screen:

1. group averaging of a block-constant exact certificate;
2. the exact null-flow equations;
3. exact value contact, whose entropy-sized right-hand side tends to `log M`.

The obstruction is a scale mismatch:

`value-contact demand = Theta(1)`,

while PSD on the vanishing `K` block would force all relevant quadratic coefficients to be only `O(epsilon)`; the exact solution instead has `beta_K=Theta(1/log^2(1/epsilon))`, which is asymptotically much larger than `r_K=Theta(epsilon)` and makes the within-`K` Hessian mode negative.

The next high-value attack is now specific: quantify this repulsion uniformly on the narrow scalar region where `n=30` passes the earlier aggregate projective bounds, or prove that heterogeneity can only make the value-contact/PSD conflict worse. Either route would upgrade the qualitative boundary theorem into a complete exclusion of the first surviving dimension. A weaker but still useful target is an exact stability inequality measuring how far the normalized masses inside `J` and `K` must deviate from uniformity as `z downarrow1`.

No numerical path sample, floating-point Brownian check, or finite grid is counted as proof. No new exact-arithmetic checker is required for Theorem R15-BR because the claim is a parameter-uniform analytic asymptotic theorem; its complete argument is on the page. The only exploratory numerics used internally were route-finding and are not evidence.

## 7. Current literature / prior-art check

Fresh dated checks on 2026-09-19/20 recovered Burdzy--Scheutzow's primary Problem 7.2 source and no accessible later primary paper explicitly resolving exact Problem 7.2; this is bounded negative evidence, not a worldwide-openness certificate.

For the retained Talagrand screen, Ascoli--He--Park--Talagrand, arXiv:2608.11183 (submitted 11 August 2026), reformulate the discrete Convexity Conjecture via `k`-thresholds and prove broad graph classes, while retaining the universal statement as conjectural. Jinyoung Park, arXiv:2609.14681 (submitted 13 September 2026), gives a dimension-independent comparison explicitly described as a bound **toward** the discrete Convexity Conjecture. A bounded search for the specific log-sum-exp quadratic-majorant / Hessian-null boundary mechanism above found only generic log-sum-exp quadratic-approximation literature, not this F0111 specialization. Novelty therefore remains **UNVERIFIED**.

## 8. Model/scheduler control boundary

The runtime prompt asks for GPT-6 with maximum reasoning, but this run actually uses **GPT-5.6 Sol** and no authenticated reasoning-effort telemetry is exposed, so the reasoning level is **UNVERIFIED**.

The exposed scheduler/task surface still provides title/prompt, schedule/timing, enablement/listing and ordinary update operations, but no binding model-family selector, no binding reasoning-effort selector, no authenticated applied-model/effort receipt, and no guaranteed hour-long execution field. Therefore GPT-6/maximum remains prompt text only. Enforcing it would require an owner-authorized product/workspace/API/admin surface that persists model/effort routing into inference and returns trustworthy runtime attestation.

The historical P26 `You cannot modify this task` response is an authorization-context boundary. Repository continuity records that a later authorized P/C context successfully updated P26. The compliant workaround for any such denial is the same task through its owning/authorized workspace/account/API/admin context, supported ownership repair, or platform support — never permission bypass or task duplication.

No scheduler, permission, Gmail/email, Drive, public-posting or purchase action was taken.

## 9. Structured ledger delta

```yaml
ledger_delta:
  worker: R15
  native_source: "Krzysztof Burdzy and Michael Scheutzow, Forward Brownian Motion, Problem 7.2 / I0076"
  native_metric: "number of four source-matching obligations proved for one frozen counterexample candidate"
  native_metric_before: "NOT_SCOREABLE_NO_SURVIVING_FROZEN_CANDIDATE"
  native_metric_after: "NOT_SCOREABLE_NO_SURVIVING_FROZEN_CANDIDATE"
  native_status: "OPEN / PARTIAL / RETIRED-HANDOFF"
  historical_positive_route_value: "2/4; retired handoff value only"
  active_successor_available: false
  retained_screen: "F0111 / Talagrand Problem 10.9, k=2; PENDING / SELF_CHECK_ONLY / NOT CLAIMED / NOT READY"
  retained_screen_movement:
    - "proved exact failure of positive-mass Gram-polygon attack for block-uniform masses when both sign blocks have size >=2"
    - "proved block-symmetrization reduction for block-constant exact contacts"
    - "proved Theorem R15-BR: no block-constant two-level Hessian-null exact quadratic contact can accumulate at z downarrow 1"
  tried_moves: [6, 14, 24]
  remaining_obligation: "quantify boundary repulsion uniformly over the full n=30 locally feasible scalar region, or prove heterogeneity cannot repair the value-contact/PSD conflict; non-two-level and second-contact mechanisms remain"
  evidence:
    idea_commit: "ea0d335a54b384e55c3c8ab8c13f370d2a1ae302"
    prior_exact_polygon_report: "runs/R15/20260919_2347Z_successor_screen_f0111_projective_polygon_h93p.md"
    proof: "this report, Sections 3-5"
  audits: []
  closure: false
```
