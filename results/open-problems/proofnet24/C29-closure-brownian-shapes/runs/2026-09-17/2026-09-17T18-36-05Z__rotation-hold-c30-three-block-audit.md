Model actually running: GPT-5.6 Sol. Reasoning level: UNVERIFIED; this was not GPT-6 at maximum, and I do not claim otherwise. **NO ACTIVE C29 MATHEMATICAL TARGET / NO MOVEMENT — the retired directional-convexity fallback metric remains `2`, its unchanged-run count remains frozen at `6`, and no seventh same-target run is created. Successor metric remains UNMEASURED. This run's nonredundant work is the directed C30 audit below. Section-B moves actually used on that audit: B1 CHANGE THE CATEGORY, B8 DISCRETIZE, B25 COUNT THE SAME THING TWICE.**

# C29 rotation hold — I0077 exclusion refresh and independent audit of C30 equal-three-block stability

Repository / branch: `yspennstate/math-open-problems` / `master`.
Own root: `proofnet24/C29-closure-brownian-shapes`.

## 1. Continuity and admission state

The controlling C29 handoff remains

`proofnet24/C29-closure-brownian-shapes/runs/2026-09-16/2026-09-16T23-36-35Z__six-run-rotation-handoff.md`,

which froze the prior fallback metric at `2`, recorded six unchanged CLOSABLE runs, and put C29 into **ROTATION HOLD — SUCCESSOR ADMISSION REQUIRED**. The later 2026-09-17 refresh did not reopen that target, and neither does this run.

The old dimension-six MUB existence attack remains unchanged in **HARD RESERVE** under `proofnet24/C29-mub-six`:

- full-domain normalized residual lower bound remains exactly `0`;
- `11/756` remains an **upper bound / benchmark only**, not a positive lower bound and not a nonexistence theorem;
- exact phase examples, gauge/atlas reductions, auxiliary upper bounds and all failed proof routes remain preserved;
- one badly conditioned submatrix does not refute an existential claim that some good family may exist.

## 2. I0077 remains excluded from C29, now with fresher live-owner evidence

The canonical claim remains `operations/claims/I0077.md`:

- owner: **R07**;
- status: **PENDING_ADMISSION, not READY**;
- source: Burdzy--Scheutzow, *Forward Brownian Motion*, Problem 7.8.

R07 is not merely a stale reservation. Its newest report in this run is

`runs/R07/20260917T1826Z_i0077_geometric_alternating_halfline_fences_26.md`

at commit `da2664e864c9a99b9e8a567bcb73341baa7b8e35`, and it moves R07's own metric **`25 -> 26`** genuinely distinct nonparabolic shape families while keeping Problem 7.8 **PARTIAL**. C29 therefore has no ownership basis to run the originally proposed B2/B6/B23 construction attack on I0077.

The primary source was refreshed again on 2026-09-17. Problem 7.8 remains exactly the request to generalize Theorem 4.3 from parabolas to other space-time shapes; Problem 7.9 is the separate forward-Levy question. The bounded dated search again found the original paper and no later publication explicitly claiming a full resolution of Problem 7.8. This is negative bounded-search evidence only, not a worldwide openness or novelty certificate.

## 3. Successor admission remains blocked

The static queue still states that queue appearance is not dispatch permission and that newly certified READY entries were zero at its refresh. More importantly, the newer coordinator admission delta `operations/task_health/runs/2026-09-17T175800Z/queue_delta.md`, independently recovered through the newest P15 admission report, still establishes **no READY + CLOSABLE + UNASSIGNED successor** on the screened frontier. Several stale-looking queue rows were newly classified HOLD or HARD rather than promoted.

Recent commits do contain new READY+CLOSABLE claims, but they are already assigned to their claiming tracks (for example R02's D0031 claim) and hence are not free inventory for C29. No lawful create-only C29 successor claim is created here.

C29 therefore remains

**ROTATION HOLD — SUCCESSOR ADMISSION REQUIRED.**

Any future successor metric remains **UNMEASURED** until source/current-status/history/ownership admission is complete.

## 4. New directed audit duty: C30's actual next claim

C30 now has a genuinely new mathematical claim after the theorem previously audited by C29:

`C30-EQUAL-THREE-BLOCK-STABILITY-20260917`.

It is a restricted continuum theorem for the fixed source graph `H=K_{5,5}\setminus C_{10}`. For a symmetric entrywise-nonnegative `3 x 3` matrix `A` whose rows sum to `3`, interpreted as an equal-three-block regular kernel, put

\[
\rho=1-\min_{i,j}A_{ij}.
\]

The claim is

\[
t_H(A)\ge 1+\frac{725117}{3179904}\rho^4
       \ge 1+\frac15\rho^4,
\]

with equality in `t_H(A)>=1` only at the all-ones matrix, and consequently

\[
t_H(A)\ge 1+\frac1{20}\|A-1\|_{L^2}^4.
\]

C30 correctly labels this **PARTIAL** relative to universal Sidorenko and records zero external independent audits before this run.

### Audit verdict

\[
\boxed{\texttt{C29-AUDIT-C30-EQUAL-THREE-BLOCK-STABILITY-05 = PASS (claim-scoped)}}.
\]

This is an independent re-derivation, not execution of C30's supplied verifier.

Artifacts:

- `proofnet24/C29-closure-brownian-shapes/artifacts/2026-09-17T18-36-05Z__audit_c30_three_block_stability.py`
- `proofnet24/C29-closure-brownian-shapes/artifacts/2026-09-17T18-36-05Z__audit_c30_three_block_stability.out`

The audit script was written independently with SymPy exact polynomials and Python exact `Fraction` arithmetic. It does not import C30's `verify.py` or `results.json`.

## 5. What was independently checked

### B1 — change category: graphon statement to a finite exact polynomial

Using the source labeling in which right vertex `y_i` is adjacent to `x_i,x_{i+1},x_{i+2}` modulo five, I independently formed

\[
D_{ijk}=\sum_{w=0}^2 A_{wi}A_{wj}A_{wk}
\]

and then

\[
F(a,b,c)=\sum_{z\in\{0,1,2\}^5}\prod_{i=0}^4D_{z_i,z_{i+1},z_{i+2}}-3^{10}.
\]

With

\[
A(a,b,c)=
\begin{pmatrix}
1-a-b&1+a&1+b\\
1+a&1-a-c&1+c\\
1+b&1+c&1-b-c
\end{pmatrix},
\]

the independently generated polynomial has exactly **664** nonzero monomials. Its homogeneous monomial counts are

`{4:15, 6:28, 7:33, 8:45, 9:52, 10:66, 11:75, 12:82, 13:87, 14:90, 15:91}`,

matching C30's certificate exactly. The absence of degrees below four also has the clean structural explanation C30 gives: in the expansion `A=J+B`, any edge subset with a degree-one vertex vanishes because `B` has zero row sums; a nonempty surviving subgraph of this simple bipartite `H` must contain a cycle and therefore has at least four edges.

As a normalization/orientation regression, the audit also performs a complete direct sum over all `3^10=59049` vertex colorings at the nontrivial polytope vertex `(a,b,c)=(2,-1,-1)` and agrees exactly with the independently generated polynomial.

### B8 — discretize the continuum by exact Bernstein control

The admissible domain is exactly

\[
a,b,c\ge-1,\qquad a+b,a+c,b+c\le1.
\]

Moreover

\[
1-A_{ij}\in\{-a,-b,-c,a+b,a+c,b+c\},
\]
so

\[
\rho=\max\{-a,-b,-c,a+b,a+c,b+c\}.
\]

For every nonzero admissible point, dividing `(a,b,c)` by `rho` therefore lands on a boundary face. Coordinate permutations reduce the six faces to the lower and upper representative triangles used by C30. The two face charts, followed by `u=s`, `v=(1-s)t`, cover those closed triangles exactly.

I then independently transformed

\[
\frac{F(r f_\pm(s,(1-s)t))}{3^{10}r^4}
\]

into tensor Bernstein form of degree `(11,15,15)`, splitting only the `s` variable at `1/2`. There are `3072` control coefficients on each of the four cubes. The exact minima are independently recovered as

- lower, first half: `17929/38220`;
- lower, second half: `43/84`;
- upper, first half: `725117/3179904`;
- upper, second half: `5055/11648`.

Every coefficient is strictly larger than `1/5`, and the global minimum is exactly

\[
\frac{725117}{3179904}>\frac15.
\]

Because tensor Bernstein basis functions are nonnegative and sum to one on the cube, this certifies the continuum lower bound, not merely sampled points.

### B25 — count the same object twice

The independent audit compares two exact constructions of the homomorphism quantity: the right-color contraction polynomial and the direct `3^{10}` full coloring count at a nontrivial boundary matrix. They agree exactly. This checks both the fifteen-edge graph normalization and the contraction orientation without relying on C30's implementation.

## 6. Remaining analytic steps checked on the page

The equality statement follows from the certified strict term `rho^4/5`: if `rho>0`, then `t_H(A)>1`; if `rho=0`, the six linear deficits vanish, hence `a=b=c=0` and `A=J`.

For the `L^2` bound, set `B=A-J` and, when `rho>0`, `A_*=J+B/rho`. The radial construction keeps `A_*` symmetric, nonnegative and row-sum three, so `P_*=A_*/3` is symmetric stochastic. Jensen row by row gives `||P_*v||_2<=||v||_2`, hence its two mean-zero eigenvalues lie in `[-1,1]`. Therefore the two mean-zero eigenvalues of `B/3` have absolute value at most `rho`, and

\[
\|A-1\|_{L^2}^2=\operatorname{Tr}((B/3)^2)\le2\rho^2.
\]

Thus `rho^4 >= ||A-1||_{L^2}^4/4`, and the already certified `rho^4/5` term yields the claimed `1/20` constant.

The unnormalized regular-kernel version is valid by the fifteen-edge homogeneity `t_H(dA)=d^{15}t_H(A)`; when `d=0`, nonnegativity and zero row sums force the zero matrix. The structured tensor-product consequence is also valid by Fubini factorization of homomorphism densities. These extensions do not enlarge the audit scope to arbitrary three-block measures, irregular kernels, arbitrary block number, or general graphons.

## 7. Audit limitations and closure state

This PASS certifies the mathematics of `C30-EQUAL-THREE-BLOCK-STABILITY-20260917` in its stated restricted class. It does **not**:

- prove universal Sidorenko for `K_{5,5}\setminus C_{10}`;
- move C30's frozen complete-simple-host metric beyond `n=10`;
- certify the order-eleven `m>=31` cases;
- certify novelty or publication status;
- erase C30's mandatory HARD handoff or create a third stuck recovery.

C30's own bounded literature search found no later source-exact resolution, but novelty of this restricted three-block theorem remains UNVERIFIED. That status is preserved.

## 8. ledger_delta for P26

```yaml
ledger_delta:
  track: C29
  allocation: CLOSABLE_OUTSIDE
  active_target: NONE_ROTATION_HOLD
  retired_fallback_metric: 2
  retired_unchanged_count: 6
  successor_metric: UNMEASURED
  proposed_I0077:
    status_for_C29: EXCLUDED_OWNED
    owner: R07
    canonical_status: PENDING_ADMISSION_NOT_READY
    latest_owner_metric: "25 -> 26 shape families"
    latest_owner_commit: da2664e864c9a99b9e8a567bcb73341baa7b8e35
  successor_admission:
    new_ready_closable_unassigned_claim: null
    state: PENDING
  c30_second_audit:
    claim: C30-EQUAL-THREE-BLOCK-STABILITY-20260917
    verdict: "C29-AUDIT-C30-EQUAL-THREE-BLOCK-STABILITY-05 = PASS"
    scope: "equal-three-block symmetric nonnegative regular kernels; quantitative rho^4 and L2 stability"
    universal_sidorenko_certified: false
    novelty_certified: false
  MUB_hard_reserve:
    residual_lower_bound: 0
    benchmark_11_over_756: UPPER_BOUND_ONLY
```

P26 should treat this as the first independent OTHER-track audit of the C30 three-block claim and should not infer any broader Sidorenko closure.

## 9. Model/task-control status

The exposed task-management surface still provides prompt/title, schedule/timing and enabled-state controls but no binding model-family selector, no reasoning-effort selector and no authenticated applied-runtime telemetry. GPT-6/maximum remains prompt-requested only. Enforcing and verifying it requires scheduler/backend or authorized enclosing-runtime support exposing and binding those fields.

Because C29 still has no admitted successor, recurring mathematical invocations remain blocked; the task should stay disabled until an authorized successor admission occurs. This audit does not reactivate the retired C29 research chain.
