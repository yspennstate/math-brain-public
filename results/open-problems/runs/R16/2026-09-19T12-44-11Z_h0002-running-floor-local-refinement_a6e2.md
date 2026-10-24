Model actually running: **GPT-5.6 Sol. Reasoning level: UNVERIFIED** — this is **not GPT-6 at maximum**. **FIXED-METRIC MOVEMENT:** active H0002 complete envelope `G_dep -> G_loc > G_dep`. Methods actually used: **B10 / B22 / B28**.

# R16 — local running-floor refinement strictly improves the energy-depleted threshold envelope

Date: 2026-09-19 UTC.
Target: `H0002`, HARD OUTSIDE, exclusive owner R16.
Status: **PARTIAL / source OPEN-looking / ACTIVE**.

## 1. Continuity, required repository reads, and current-source check

I continued from the newest immutable R16 report

`runs/R16/2026-09-19T11-43-54Z_h0002-energy-depleted-threshold-envelope_d19b.md`

rather than restarting. Before new mathematics I re-read/reconciled:

- `probability_campaign_2026_09/INDEX.md` and `RANKING.md`;
- root `POSTED.md`, `RESULTS.md`, and `QUEUE.md`;
- `operations/NEW_METHODS_2026-09-16.md` and the current owner directive it points to;
- `operations/claims/H0002.md`;
- the H-intake identity for H0002 under `probability_1000_intake_H_20260914/problems.jsonl`;
- the preceding R16 majorization / moment / tail-persistence chain; and
- the newest useful neighboring same-source record, R7-07/G0011, which is the distinct CMW long-cycle conjecture and is already in terminal handoff. It supplies no premise below and creates no H0002 ownership conflict.

Fresh primary checks on 2026-09-19:

- Bansal--Jiang, arXiv:2508.03961v2, proves the Beck--Fiala `O(sqrt(t))` scale directly for `t >= log^2 n` and retains a weaker polylogarithmic loss below that regime: https://arxiv.org/abs/2508.03961 .
- Guo--Fang--Lu, arXiv:2609.11189v1, submitted 2026-09-10, proves the stronger Komlos signing theorem with constant `3 sqrt(2 pi)` and explicitly deduces discrepancy `< 3 sqrt(2 pi t)` for every integer `t>=1`: https://arxiv.org/abs/2609.11189 .
- Karingula--Lovett, ECCC TR26-188, posted 2026-09-17, gives an elementary Komlos proof with constant `36`: https://eccc.weizmann.ac.il/report/2026/188/ .
- Christoph--Morawski--Wigderson, arXiv:2608.19145v1, submitted 2026-08-19, remains the current primary source surfaced for H0002. Its Question 5.1 asks for natural finite-graph conditions forcing a linear-size percolation component at `p >= (1+epsilon)/lambda(G)`. A bounded current title/author/arXiv-ID search did not surface a later source-matching resolution. This is negative evidence only.

Thus the nominal Beck--Fiala existence target remains a **KNOWN current-preprint baseline** rather than new R16 progress. The source-valid active R16 target remains H0002 on the frozen H1--H2--H3 sufficient-condition class.

For the variational mechanism I also checked generic isotonic / moment-extremizer and order-restricted optimization literature. The searches recovered standard extreme-point, moment-problem, majorization, and isotonic ideas, but no theorem whose hypotheses directly match the simultaneous lower-prefix obstacle, upper spectral `L^2` budget, and concave absorption functional used here. This is not a novelty certificate.

## 2. Incoming theorem and notation

All frozen H0002 hypotheses and every earlier established reduction are retained unchanged. In particular, with the notation fixed in the preceding reports:

- `d_P=d_pad<alpha`;
- `b_P=alpha-d_P>0`;
- `a_P=rho-b_P`;
- `Delta=epsilon(7-epsilon)/(8-epsilon)>0`;
- `t(b)` is the endpoint full-core threshold profile, extended by `t(b_P)=0`;
- `b_0>b_P` is the maximizing point selected on the fixed terminal compact interval;
- `t_0=t(b_0)>0`;
- `D_*:=b_P t_0>0`;
- `H_*:=a_P/D_*>t_0`;
- `phi_r(u):=1-exp(-r u)`;
- `g_r(u):=phi_r(u)/u`, with `g_r(0)=r`.

For a connected pre-absorption core `W` of density `a_3=c_3 a_P`, `c_3 up 1`, sort normalized outside degrees increasingly as `x(q)`. For every finite old anchor family `D`, let `L_{D,3}(q)` denote the corresponding old degree floor.

The earlier prefix-majorization theorem gives, uniformly in finite `D`,

`int_0^{b_0} (x-L_{D,3})_+ dq >= c_3 D_*-o(1)`,          (2.1)

and the spectral energy bound gives

`int x(q)^2 dq <= c_3 a_P+o(1)`.                           (2.2)

The exact two-moment term is

`eta_* = exp(-Delta t_0) D_* g_Delta(H_*)`.                (2.3)

The tail-persistence run set

`Gamma:=H_*-t_0`,
`T_+:=t_0+Gamma/4`,
`Y:=t_0+Gamma/2`,                                          (2.4)

and established a fixed `delta_loc>0` such that

`L_{D,3}(q) <= c_3 T_+ + o(1)`                             (2.5)

uniformly on

`q in [b_0,b_0+delta_loc]`.                                (2.6)

The immediately preceding report then deformed the dichotomy through `X in [T_+,Y]`. Its no-cross branch was

`A(X)=exp(-Delta t_0)D_*[g_Delta(X)-g_Delta(H_*)]`,        (2.7)

while the cross branch used

`V(X):=a_P-delta_loc X^2`,                                 (2.8)

`C(X):=exp(-Delta t_0)D_*`
`      *[g_Delta(V(X)/D_*)-g_Delta(H_*)]`                  (2.9)

when `V(X)>0`, together with the direct tail term

`delta_loc[phi_Delta(X)-phi_Delta(T_+)]`.                  (2.10)

Thus

`B(X)=C(X)+delta_loc[phi_Delta(X)-phi_Delta(T_+)]`         (2.11)

on the feasible branch, and `B(X)=+infinity` when the tail branch is asymptotically impossible. The incoming improvement is

`zeta_dep := sup_{X in [T_+,Y]} min{A(X),B(X)}`,           (2.12)

with

`G_dep := min{1,G_coreavg+eta_*+zeta_dep}`.                (2.13)

Every fixed `g<G_dep` is already certified to satisfy

`P(L_1(G_p)>=g n) -> 1`                                    (2.14)

uniformly on the frozen H1--H2--H3 class for every

`p >= (1+epsilon)/lambda(G)`.                              (2.15)

The goal here is to retain one more piece of information that (2.5) deliberately flattened away.

## 3. B10 — derandomize the arbitrary finite anchor floor into its deterministic running envelope

For `q` below the isolated old-anchor threshold `beta`, define the deterministic running profile

`bar_t(q):=sup{t(b): b_P<=b<=q}`.                          (3.1)

For every finite anchor family `D`, its endpoint floor obeys

`L_D(q) <= bar_t(q)`.                                      (3.2)

The same statement, multiplied by `c_3` up to the inherited vanishing finite-size error, holds for `L_{D,3}`.

By construction of `b_0`,

`bar_t(b_0)=t_0`.                                          (3.3)

The local continuity used already in the preceding tail-persistence theorem to obtain the coarser level `T_+` can be used at any intermediate level. Fix

`S := (t_0+T_+)/2`,                                       (3.4)

so

`t_0<S<T_+<Y<H_*`.                                        (3.5)

After shrinking only the *local comparison interval* and not changing any earlier theorem, choose

`0<delta_S<=delta_loc`                                     (3.6)

small enough that it remains below the special `beta` boundary and

`bar_t(q)<=S` for all `q in [b_0,b_0+delta_S]`.            (3.7)

Consequently, uniformly over every finite old anchor family,

`boxed: L_{D,3}(q) <= c_3 S+o(1)`                         (3.8)

throughout this shorter interval.

This is the key derandomization step: instead of reasoning separately about whatever finite family happened to approximate the old supremum, the deterministic running envelope gives one local strict gap `S<T_+` valid for all of them at once.

## 4. Sharpen the crossing branch on a two-level tail

The no-cross estimate (2.7) remains valid for every

`X in [S,Y]`,                                               (4.1)

because its proof uses only the prefix surplus (2.1), the upper cap on the prefix degree, and the strict decrease of `g_Delta`.

Now suppose the no-cross case fails: some prefix degree exceeds `X`. Since `x(q)` is nondecreasing, the whole tail interval `[b_0,b_0+delta_loc]` then satisfies

`x(q)>=X-o(1)`.                                            (4.2)

Therefore the same energy depletion as before still applies on the *full* tail:

`int_{b_0}^{b_0+delta_loc} x(q)^2dq`
`    >= delta_loc X^2-o(1)`.                              (4.3)

Thus the prefix two-moment correction is still `C(X)` from (2.9), with the same convention that an energy-infeasible cross branch has cost `+infinity`.

The direct absorption gain can now be sharpened because the first `delta_S` part of the tail has the lower old floor `S` rather than `T_+`. Define

`J_loc(X):=`

- `delta_S[phi_Delta(X)-phi_Delta(S)]` for `S<=X<=T_+`;
- `delta_loc[phi_Delta(X)-phi_Delta(T_+)]`
  `+ delta_S[phi_Delta(T_+)-phi_Delta(S)]` for `T_+<=X<=Y`.

This is continuous at `T_+` and nonnegative on all of `[S,Y]`. Put

`B_loc(X):=C(X)+J_loc(X)`                                  (4.4)

on the feasible branch and `B_loc(X):=+infinity` when the cross branch is impossible.

On the whole incoming domain `[T_+,Y]`, set

`chi := delta_S[phi_Delta(T_+)-phi_Delta(S)]>0`.           (4.5)

Then, whenever the old cross branch is feasible,

`boxed: B_loc(X)=B(X)+chi`.                               (4.6)

If it is infeasible, both formulations correctly discard that branch.

The strengthened one-dimensional envelope is

`boxed: zeta_loc := sup_{X in [S,Y]} min{A(X),B_loc(X)}.` (4.7)

## 5. Strict improvement `zeta_loc > zeta_dep`

The preceding report already established the monotonic structure needed here: `A` is strictly decreasing in `X`, while the feasible cross-branch cost is increasing; if the cross branch becomes impossible, only the no-cross branch remains. Thus the old minimax value is attained at a crossing, a boundary, or the limiting energy-feasibility boundary.

Let `z:=zeta_dep` and take an old maximizing point / limiting maximizer `X_* in [T_+,Y]`.

### Case 1: the old optimum is cross-branch limited

If

`B(X_*)<A(X_*)`,                                           (5.1)

then by (4.6)

`B_loc(X_*)=B(X_*)+chi>z`,                                 (5.2)

while `A(X_*)>z`. Hence the new minimum is already strictly larger than `z` at the same threshold.

### Case 2: the old optimum is a genuine crossing

If

`A(X_*)=B(X_*)=z`,                                        (5.3)

then

`B_loc(X_*)=z+chi`.                                       (5.4)

Move `X` slightly to the left. Strict decrease of `A` means

`A(X)>z`,                                                  (5.5)

and continuity of the feasible `B_loc` keeps

`B_loc(X)>z`.                                              (5.6)

If `X_*=T_+`, the newly opened interval `[S,T_+)` is exactly what allows this left move; this is why merely adding `chi` on the old interval would not by itself be enough.

### Case 3: the old optimum is no-cross limited

If

`A(X_*)<B(X_*)`,                                           (5.7)

then the same left-move argument works: `A` rises strictly, while `B_loc` remains above `z` in a sufficiently small left neighborhood. Again, if `X_*=T_+`, the extension down to `S` supplies that neighborhood.

There is one apparent endpoint issue when the old optimum sits exactly where `V(X)` reaches zero. It is harmless. On the feasible side,

`C(X) -> exp(-Delta t_0)D_*[Delta-g_Delta(H_*)]`.          (5.8)

At such a boundary `X_c>0`,

`exp(-Delta t_0)D_*[Delta-g_Delta(H_*)] - A(X_c)`
` = exp(-Delta t_0)D_*[Delta-g_Delta(X_c)] > 0`,           (5.9)

because `g_Delta(X_c)<Delta`. Therefore the feasible-side cross cost is already strictly above the no-cross value at the energy boundary; the same left-neighborhood argument applies. If the cross branch is impossible on an entire neighborhood, then `B_loc=+infinity` there and the conclusion is even immediate.

All possibilities yield

`boxed: zeta_loc > zeta_dep`.                              (5.10)

This is a strict improvement over the **whole incoming one-threshold supremum**, not merely over one selected threshold.

## 6. The incoming envelope was not already capped at one

For strict movement of the complete giant fraction, the old envelope itself must have headroom. Since

`zeta_dep <= sup_{X in [T_+,Y]} A(X)=A(T_+)`,              (6.1)

we have

`eta_*+zeta_dep`
` <= eta_*+A(T_+)`
` = exp(-Delta t_0)D_* g_Delta(T_+)`
` < D_*/T_+`
` = b_P t_0/T_+`
` < b_P`,                                                   (6.2)

because `T_+>t_0` and `g_Delta(T_+)<1/T_+`.

The earlier full-core theorem gives

`G_coreavg <= 1-b_P`.                                      (6.3)

Therefore

`boxed: G_dep<1`.                                          (6.4)

Define the new complete envelope

`boxed: G_loc := min{1,G_coreavg+eta_*+zeta_loc}.`         (6.5)

Combining (5.10) and (6.4),

`boxed: G_loc>G_dep`.                                      (6.6)

A frozen coefficient strictly beyond the entire incoming complete envelope is

`g_receipt := G_dep`
` + (1/2) min{zeta_loc-zeta_dep, 1-G_dep}`.                (6.7)

Hence

`G_dep < g_receipt < G_loc`.                               (6.8)

The same finite-family approximation, connected-core trimming, independent final sprinkling, and Poisson-binomial concentration argument from the previous reports now gives:

> **Theorem.** On the unchanged frozen H1--H2--H3 class, for every fixed `g<G_loc` and every `p >= (1+epsilon)/lambda(G)`,
>
> `P(L_1(G_p)>=g n) -> 1`.

No endpoint attainment is claimed.

## 7. B22 — read the failure in the preceding relaxation

The preceding threshold theorem was not failing because its two-moment inequality was weak: that inequality is sharp for the abstract two-moment problem. The actual leak was the subsequent replacement of the complete running floor by the single constant `T_+` over an entire right-neighborhood of `b_0`.

Reading that failure literally suggests the present fix: preserve just one additional level of the running floor. The resulting `chi` is fixed, positive, uniform over all finite old anchor families, and costs no extra probabilistic reserve.

The external method search found general order-restricted/moment extreme-point principles, but nothing that directly supplies this exact graph-specific two-level comparison. Majorization, running maxima, and moment extremization are standard machinery; no novelty claim is inferred from a negative search.

## 8. B28 — typical-anchor replacement was tried and rejected

I also tried replacing the universal finite-family comparison by a random/typical anchor or a random deficient density `b`. This gives average lower bounds on `e(W,B)` and can recover the same expected prefix mass, but it does **not** control the bottom prefix of the sorted degree vector uniformly over every graph in H1--H2--H3. An adversarial low-degree block can be missed by a typical anchor while still determining the absorption minimum.

Because the tracked quantity is a complete **uniform** bound over the frozen host-graph class, that typical-instance route cannot move the metric without an additional concentration principle not supplied by H1--H2--H3. I retain no theorem from B28.

## 9. What changed and the next obstruction

The complete metric moved strictly:

`G_dep -> G_loc > G_dep`.

Supported unchanged count therefore remains `0` and no stuck recovery is triggered.

The remaining loss is now explicit: the argument keeps only two levels, `S` and `T_+`, of the full deterministic running profile `bar_t(q)`. A genuine next move would solve, or finitely reduce, the full isotonic obstacle problem

`min int phi_Delta(x(q)) dq`

subject to

`x nondecreasing`,

`int_0^b x(q)dq >= b t(b)` for every certified `b`,

and

`int x(q)^2dq <= a_P`.

The natural conjecture is that an extremizer is a finite-plateau profile whose breakpoints occur at contact points of the lower-prefix obstacle plus at most one energy-saturation plateau. That statement is not proved here.

No finite checker was manufactured: the new claim is analytic and the complete theorem-sized argument is written above.

## 10. Model / scheduler control status

The exposed scheduler/task-control surface still provides prompt/title, scheduling or relative-start fields, timing mode, and enablement, but **no binding model-family selector, no reasoning-effort selector, and no authenticated applied-model/reasoning receipt**. GPT-6/maximum is therefore still prompt-only; actually enforcing it would require platform-level model/reasoning fields plus per-run runtime attestation.

No scheduler modification was attempted because the current owner instruction for this worker forbids scheduler changes. The historical `You cannot modify this task` result for some native tasks, including the earlier P26 context, is authorization-context-specific: the current repository ledger records that P26 was later updated successfully from an authorized context. If a task still rejects modification, the compliant workaround is the owning authorized workspace/account or platform support, never duplication or permission bypass.

## 11. Structured ledger delta

```yaml
ledger_delta:
  worker: R16
  claim: H0002
  source: Christoph-Morawski-Wigderson_arXiv_2608_19145v1_Q5.1
  nominal_beck_fiala_status: KNOWN_CURRENT_PREPRINT_BASELINE
  nominal_uniform_bound_current_primary_source: "B(t,n) < 3*sqrt(2*pi*t) for every integer t>=1 (Guo-Fang-Lu v1)"
  metric_name: g_twoaxis_complete_envelope
  before: G_dep
  after: G_loc = min(1, G_coreavg + eta_* + zeta_loc)
  movement: STRICT_INCREASE
  status: PARTIAL
  supported_unchanged_count: 0
  methods: [10, 22, 28]
  finite_checker: NOT_APPLICABLE_ANALYTIC
  closure_audits: []
  remaining_obligation: >-
    Replace the two-level running-floor relaxation by the full nested prefix
    obstacle, ideally through a finite-plateau/extreme-point theorem for the
    isotonic moment problem. The source Question 5.1 remains broader than
    the frozen H1-H2-H3 sufficient-condition theorem.
```
