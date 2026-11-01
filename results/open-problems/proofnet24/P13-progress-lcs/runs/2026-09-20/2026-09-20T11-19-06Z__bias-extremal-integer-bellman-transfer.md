Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — not GPT-6 maximum.**

# P13 / T02 — exact integer Bellman sharpening and bias-extremal finite-to-infinite transfer

## 0. Before / after, separated by level

### Source-level binary Chvatal–Sankoff interval

The preceding P13 report carried the repository-internal exact certificate

\[
L\le \gamma_2\le U_*,\qquad L=0.792665992=\frac{99083249}{125000000},
\]

from P02's 09:05 residue-optimal dual report. The newest completed P02 companion report is

`proofnet24/P02-progress-lcs/runs/2026-09-20/2026-09-20T10-03-15Z__matched-successor-defect-report.md`, blob `2596bca4d6d8b52b27b80626df09a3b0caaa7829`.

It proves a strictly smaller exact internal upper endpoint `U_new<U_*`, with separator

\[
\boxed{
U_{new}<
0.82627594276228262501510658153729663282346199619319002388080618331256294443029952
<U_*.
}
\]

Hence the source-level certified interval strictly shrinks from `U_*-L` to `U_new-L`. This source movement is companion-derived; P13 does not duplicate P02's covering/cone argument. P02 reports a diagnostic decrease of approximately `1.0655909281446033e-80`, while its finite dual defect improves by about 27.22%.

### P13 mechanism-level movement

The preceding P13 width-6 Bellman report certified

\[
\frac{3119319222655621}{4000000000000000}
\le \gamma_6\le
\frac{3119319222655638}{4000000000000000},
\]

of width

\[
\frac{17}{4000000000000000}=4.25\times 10^{-15}.
\]

This run replaces it by the strictly nested exact interval

\[
\boxed{
\frac{6238638445311257066}{8000000000000000000}
\le \gamma_6\le
\frac{6238638445311257073}{8000000000000000000}
}
\tag{0.1}
\]

of width

\[
\boxed{
\frac{7}{8000000000000000000}=8.75\times10^{-19}.
}
\tag{0.2}
\]

The old/new width ratio is exactly

\[
\frac{17/(4\cdot10^{15})}{7/(8\cdot10^{18})}
=\frac{34000}{7}
=4857.142857\ldots.
\tag{0.3}
\]

More importantly, this run proves a new **bias-extremal finite-to-infinite theorem**. If a Bellman potential has residual span `epsilon`, then starting a finite-horizon computation at a bias minimizer gives a lower stationary certificate with only `epsilon` loss and **no `1/N` boundary term**; starting at a bias maximizer gives the analogous upper certificate. This is a genuine finite-to-infinite transfer, not a promotion of finite computation by itself.

Status: **PARTIAL / source OPEN / exact internal candidates pending later independent review and public-priority checking.**

## 1. Scope, source, model, continuity, and handoff

This run follows `operations/PROGRESS20_2026-09-20.md`, blob `4a207f06e5c8294c83bcabcd9a1477f26f54b441`, whose LIVE20 assignment keeps P13 on T02: dependence-preserving boundary recursion for binary LCS, complementary to P02's stationary/variational route.

The target is

\[
\gamma_2=\lim_{n\to\infty}\frac{\mathbf E\,LCS(X_1^n,Y_1^n)}n
\]

for two independent iid uniform binary strings. The same raw `X` and `Y` letters are reused across rows and columns of the LCS dynamic-programming grid. Therefore the match indicators are dependent. The independent Bernoulli matching model is not used.

Fresh source navigation retained Alexander Tiskin, `arXiv:2212.01582v2`, revised 2024-08-13. Its current record says the binary Chvatal–Sankoff coefficient remains unresolved and explicitly notes that claims in the earlier preprint about the stochastic process and `gamma` turned out to be incorrect and were removed in v2. None of those removed claims is used. The retained rigorous public lower endpoint is `0.792665992` from Heineman--Miller--Reichman--Salls--Sarkozy--Soiffer, `arXiv:2407.10925`.

The newest own substantive dependency is

`proofnet24/P13-progress-lcs/runs/2026-09-20/2026-09-20T10-16-08Z__width6-exact-bellman-obstruction.md`, blob `dfdaa32bec8b77bd4ca4e44f44f138962cb54656`.

That report proved that the width-6 recurrent class has exactly `5,735,086` states, established the exact Bellman-residual transfer, and showed `gamma_6<L`; therefore every fixed corridor `w<=6` is excluded from improving the retained source lower endpoint.

Short pre-LIVE20 handoff only: P0342 had already been terminally handed off at frozen `2/2`; the later P0205 screen admitted no successor because its source notation could not be frozen source-faithfully. Retired I0051/clade work remains retired and is not reopened.

Root `POSTED.md` was not modified; the latest P02 companion had already checked that no posting exclusion covers T02. No peer or historical file was overwritten.

## 2. Exact dependence-preserving strip recursion

Fix half-width `w` and put `m=2w`. A formal strip state is

\[
s=(x,g),\qquad x,g\in\{0,1\}^m.
\]

Set

\[
V_0=0,\qquad V_k=\sum_{i=1}^k g_i.
\]

For one fresh actual source pair `(u,v)`, define

\[
a_i={\bf1}_{\{x_{i+1}=v\}}\quad(0\le i<m),
\qquad a_m={\bf1}_{\{u=v\}}.
\]

Crucially, the **same incoming `Y` bit `v`** appears in every `a_i` in the whole column. The updated dynamic-programming profile is

\[
Q_0=\max\{V_1,V_0+a_0\},
\]

\[
Q_k=\max\{Q_{k-1},V_k+a_k,V_{k+1}\},\qquad 1\le k<m,
\]

\[
Q_m=\max\{Q_{m-1},V_m+a_m\},
\]

with

\[
x'=(x_2,\ldots,x_m,u),
\qquad g'_k=Q_k-Q_{k-1},
\]

and central one-step reward

\[
\rho(s;u,v)=Q_w-V_w\in\{0,1\}.
\]

All computations in this report use the four equiprobable genuine source pairs `(u,v)\in\{0,1\}^2` under exactly this recursion.

For `w=6`, the earlier analytic reset `A^{12}`, `A=(0,1)`, maps every formal state to `z_0=(0^{12};0^{12})`. Thus the class reachable from `z_0` is the unique recurrent class `R_6`; exact BFS gives

\[
|R_6|=5,735,086.
\]

## 3. Bellman residual notation

Let `R` be any finite closed recurrent class of a four-letter equiprobable Markov reward chain. For integer scale `Q>=1` and integer potential `H:R->Z`, write `h=H/Q` and define

\[
D_H(s)=Q\sum_{a=1}^4\rho(s,a)+\sum_{a=1}^4H(T_as)-4H(s).
\tag{3.1}
\]

Then

\[
\delta_H(s):=\frac{D_H(s)}{4Q}
=\bar\rho(s)+(Ph)(s)-h(s),
\tag{3.2}
\]

where `bar rho(s)` is the mean one-step reward.

Put

\[
\ell=\min_R\delta_H,
\qquad
u=\max_R\delta_H,
\qquad
\varepsilon=\nu-\ell.
\tag{3.3}
\]

Stationarity gives immediately

\[
\ell\le\gamma_R\le\nu,
\tag{3.4}
\]

because the stationary average of `(Ph-h)` is zero.

The previous report used the crude terminal estimate

\[
|P^Nh(s)-h(s)|\le h_{\max}-h_{\min}
\]

symmetrically on both sides. The next theorem removes that unnecessary factor of two and, at bias extremizers, removes the `1/N` term on the useful one-sided bound entirely.

## 4. New theorem: bias-extremal finite-to-infinite transfer

### Theorem 4.1

Let `R`, `P`, `rho`, `H`, `Q`, `h`, `ell`, `nu`, and `epsilon=nu-ell` be as above. Let

\[
A_N(s):=\frac{\mathbf E_s R_N}{N}
\]

be the expected finite-horizon average reward from state `s`. Then for every `s\in R` and every `N>=1`,

\[
\boxed{
A_N(s)-\varepsilon-\frac{h(s)-h_{\min}}N
\le \gamma_R\le
A_N(s)+\varepsilon+\frac{h_{\max}-h(s)}N.
}
\tag{4.1}
\]

Equivalently, the total width of this finite-to-infinite bracket is

\[
\boxed{
2\varepsilon+\frac{h_{\max}-h_{\min}}N.
}
\tag{4.2}
\]

This is half the boundary contribution of the previous symmetric use of `osc(h)` on both sides.

If `s_-` is a minimizer of `h`, then

\[
\boxed{
\gamma_R\ge A_N(s_-)-\varepsilon
}
\tag{4.3}
\]

for **every** horizon `N`: the lower finite-to-infinite transfer has no `1/N` penalty.

If `s_+` is a maximizer of `h`, then

\[
\boxed{
\gamma_R\le A_N(s_+)+\varepsilon
}
\tag{4.4}
\]

for every `N`.

Thus two finite computations started at the bias extremizers give the stationary bracket

\[
\boxed{
A_N(s_-)-\varepsilon
\le\gamma_R\le
A_N(s_+)+\varepsilon,
}
\tag{4.5}
\]

with no explicit horizon-boundary correction.

### Proof

Summing the pointwise residual identity (3.2) along the chain and taking expectations gives

\[
\ell
\le
A_N(s)+\frac{P^Nh(s)-h(s)}N
\le
\nu.
\tag{4.6}
\]

Define the boundary-corrected finite estimator

\[
C_N(s):=A_N(s)+\frac{P^Nh(s)-h(s)}N.
\tag{4.7}
\]

Equation (4.6) says `C_N(s)\in[ell,nu]`. By (3.4), also `gamma_R\in[ell,nu]`. Therefore

\[
C_N(s)-\varepsilon\le\gamma_R\le C_N(s)+\varepsilon.
\tag{4.8}
\]

Since

\[
h_{\min}-h(s)
\le P^Nh(s)-h(s)
\le h_{\max}-h(s),
\tag{4.9}
\]

substituting the two endpoints of (4.9) into (4.8) yields (4.1). Summing the two one-sided penalties gives (4.2).

If `h(s_-)=h_min`, then the lower terminal drift in (4.9) is zero, so (4.3) follows. If `h(s_+)=h_max`, then the upper terminal drift is zero, giving (4.4). Combining gives (4.5). QED.

### Why this is a genuine transfer

A finite value `A_N(s)` alone is not promoted to a statement about the infinite mean. The theorem uses a globally verified Bellman residual interval and a proved potential-drift identity. The `epsilon` subtraction in (4.3) is logically essential even though it is tiny in the executed width-6 certificate.

## 5. New exact integer Bellman sharpening

The previous exact potential used scale `Q=10^15` after floating relative value iteration, then scanned all residuals in integer arithmetic. Its exact residual span was `17` numerator units.

This run changes the candidate-construction mechanism before the proof scan:

1. enumerate the same exact `R_6` and all four genuine source transitions;
2. use ordinary floating relative value iteration only as a coarse seed;
3. freeze at the much larger signed-integer scale
   \[
   Q=2\cdot10^{18};
   \]
4. perform `120` **exact integer relative-value refinements**
   \[
   H_{new}(s)=\operatorname{round}\!\left(
   \frac{Q\sum_a\rho(s,a)+\sum_aH(T_as)}4
   \right)-c,
   \tag{5.1}
   \]
   where `c` is the common normalizing value chosen so `H_new(z_0)=0`;
5. after refinement, ignore all convergence heuristics and scan (3.1) on every one of the `5,735,086` states using exact integer / `__int128` arithmetic.

No theorem claim depends on floating convergence or on the integer iteration being monotone. The final potential is simply an explicitly generated integer vector; Theorem 3.4 applies once the exhaustive residual scan is exact.

The executed checker returns

\[
Q=2\cdot10^{18},
\]

\[
\boxed{d_-=6238638445311257066},
\qquad
\boxed{d_+=6238638445311257073},
\tag{5.2}
\]

so the numerator span is exactly `7`.

It also returns

\[
\boxed{H_{\min}=-417968688415616699},
\]

\[
\boxed{H_{\max}=7863814844147315928},
\]

and therefore

\[
\boxed{
\operatorname{osc}(h)
=\frac{8281783532562932627}{2\cdot10^{18}}
=4.1408917662814663135\ldots.
}
\tag{5.3}
\]

The executed output ends `ALL_EXACT_CHECKS_PASS`.

## 6. Strictly smaller exact width-6 interval

Applying (3.4) to (5.2) gives (0.1):

\[
\boxed{
\frac{6238638445311257066}{8000000000000000000}
\le\gamma_6\le
\frac{6238638445311257073}{8000000000000000000}.
}
\]

To verify strict nesting inside the previous interval, rewrite the old denominator `4*10^15` on denominator `8*10^18`, multiplying old numerators by `2000`:

\[
6238638445311242000
<6238638445311257066,
\]

\[
6238638445311257073
<6238638445311276000.
\]

Thus both endpoints move strictly inward.

The new exact width is `7/(8*10^18)`. Compared with `17/(4*10^15)`, the shrink factor is exactly `34000/7` as in (0.3).

The width-6 obstruction to the public lower endpoint remains decisive. On denominator `8*10^18`,

\[
L=\frac{6341327936000000000}{8000000000000000000},
\]

so

\[
\boxed{
L-\gamma_6^{upper}
\ge
\frac{102689490688742927}{8000000000000000000}>0.
}
\tag{6.1}
\]

Hence this sharper computation still does **not** improve the source lower endpoint. It strengthens the exclusion of fixed widths `w<=6` rather than changing that conclusion.

## 7. Concrete finite-to-infinite gains at width 6

For the reset state `z_0`, the normalization has `h(z_0)=0`. Theorem 4.1 gives

\[
\gamma_6\ge
A_N(z_0)
-\frac{7}{8\cdot10^{18}}
-\frac{417968688415616699}{2\cdot10^{18}N},
\tag{7.1}
\]

and

\[
\gamma_6\le
A_N(z_0)
+\frac{7}{8\cdot10^{18}}
+\frac{7863814844147315928}{2\cdot10^{18}N}.
\tag{7.2}
\]

Thus the lower finite-to-infinite boundary coefficient is only

\[
0.2089843442078083495\ldots,
\]

instead of the previous symmetric `4.140891766281466...`. That is an improvement by a factor about `19.81` on the lower side from the canonical reset state.

The total `1/N` width contribution is now exactly `osc(h)/N`, rather than `2 osc(h)/N`; it is a factor-two improvement over the preceding Bellman finite-horizon bracket. Relative to the earlier sharp pathwise `|E_sR_N-N gamma_6|<=12`, whose two-sided interval width contribution was `24/N`, the new state-adapted total contribution is smaller by a factor about `5.796`.

At a bias minimizer `s_-`, Theorem 4.1 is stronger:

\[
\boxed{
\gamma_6\ge A_N(s_-)-\frac7{8\cdot10^{18}}
}
\tag{7.3}
\]

for every `N`, with no `1/N` term at all. Likewise, at a bias maximizer `s_+`,

\[
\boxed{
\gamma_6\le A_N(s_+)+\frac7{8\cdot10^{18}}.
}
\tag{7.4}
\]

This is the main reusable mechanism advance of the run: a finite-horizon computation can be made almost stationary **by choosing its starting boundary through the Bellman bias**, not by waiting for a long mixing or synchronization time.

## 8. Source-level companion movement

P13's previous report saw P02's `U_*`. The newest P02 report proves a larger exact two-step dual defect `D_new`, with exact finite comparison

\[
\frac{D_{new}}{D_*}=1.2722326445088614\ldots,
\]

and derives an exact rate `lambda_new<lambda_*`, hence

\[
\boxed{L\le\gamma_2\le U_{new}<U_*}.
\tag{8.1}
\]

The strict separator quoted in Section 0 certifies the source interval shrink. That movement belongs to P02's complementary variational/covering route. P13's width-6 Bellman sharpening is kept separate and is not misreported as a new lower endpoint for `gamma_2`.

## 9. Obstruction and failures

The source-lower route through width six is closed: even the newly sharpened exact upper endpoint for `gamma_6` lies more than `0.0128` below `L`. Therefore spending additional runs merely adding decimals to `gamma_6` would be stagnation, despite the exact interval improvement in this invocation.

The new bias-extremal theorem solves the finite-to-infinite boundary-loss problem **once a useful wider-strip bias is available**, but it does not by itself construct that bias at `w>=7`. Full recurrent enumeration at width seven remains the computational bottleneck. No width-7 source claim is made.

A coarse local-lift idea from the previous report remains plausible but unproved at useful strength: a central width-6 block in a wider strip is driven by its local raw/gradient bits plus a one-bit entering carry and a small amount of right-edge context. A rigorous lifted potential must control those omitted outer contexts without assuming independent matches. This is the actual remaining proof obstruction.

No claim from an unexecuted width-7 computation, no independent-Bernoulli substitution, and no finite value without an asymptotic transfer is used.

## 10. Next attack

The next P13 attack should no longer refine width six. Use the exact width-6 bias as a **local core potential** inside width seven, but augment it by the true entering carry and the minimal right-edge context required by the shared-`Y` column recursion. The target is a Bellman lower inequality on all width-7 reachable local contexts without enumerating the full width-7 recurrent class.

The bias-extremal theorem gives the payoff criterion: once such a wider potential has residual span `epsilon_7`, identify a bias-minimizing start and certify

\[
\gamma_7\ge A_N(s_-)-\epsilon_7
\]

with no `1/N` penalty. If the resulting exact lower value still lies below `L`, that is a decisive width-7 obstruction; if it exceeds `L`, then monotonicity `gamma_7<=gamma_2` gives a genuine source lower improvement.

If the carry-augmented local lift cannot make the residual lower bound useful after a substantive attempt, the materially different recovery route is the event-specific mixed-terminal-suffix coupling inherited from the earlier identity `gamma_w=2/3+pi_w(B_w)/3`, not another full-state reset-language refinement.

## 11. Essential executed artifacts

Final checker used for the certified values above:

`proofnet24/P13-progress-lcs/artifacts/2026-09-20/2026-09-20T11-15-00Z__w6_integer_bellman_refinement.cpp`

creation commit `eeda6725c4cc435d2d2542f212c089b9bfffd604`.

Executed output:

`proofnet24/P13-progress-lcs/artifacts/2026-09-20/2026-09-20T11-15-00Z__w6_integer_bellman_refinement.out`

creation commit `1691d79b7b03579a237102610702c629389cf40e`.

The output records `reachable=5735086`, exact residual numerators, `Hmin`, `Hmax`, the exact old/new width ratio, the asymmetric reset-state boundary coefficients, and terminates `ALL_EXACT_CHECKS_PASS`. Local execution used ordinary CPU only; no paid compute or workflow execution was used.

## 12. ledger_delta

```yaml
ledger_delta:
  slot: P13
  parent: T02-binary-LCS
  model: iid-uniform-binary-strings
  independent_bernoulli_matching_used: false
  policy:
    file: operations/PROGRESS20_2026-09-20.md
    blob: 4a207f06e5c8294c83bcabcd9a1477f26f54b441
  source_status:
    public_lower: "0.792665992"
    before_internal_upper: "U_*"
    after_internal_upper: "U_new"
    strict_source_movement: "U_new < U_*"
    source_movement_owner: P02
  p13_before:
    gamma6_lower: "3119319222655621/4000000000000000"
    gamma6_upper: "3119319222655638/4000000000000000"
    gamma6_width: "17/4000000000000000"
  p13_after:
    gamma6_lower: "6238638445311257066/8000000000000000000"
    gamma6_upper: "6238638445311257073/8000000000000000000"
    gamma6_width: "7/8000000000000000000"
    old_over_new_width: "34000/7"
    recurrent_states: 5735086
    H_min: -417968688415616699
    H_max: 7863814844147315928
    H_scale: 2000000000000000000
  proved_new:
    - "bias-extremal finite-to-infinite theorem: A_N-epsilon-(h-hmin)/N <= gamma <= A_N+epsilon+(hmax-h)/N"
    - "at h-minimizer: gamma >= A_N-epsilon with no 1/N penalty"
    - "at h-maximizer: gamma <= A_N+epsilon with no 1/N penalty"
    - "exact integer relative-value refinement followed by exhaustive exact residual scan"
  obstruction:
    - "gamma_6 remains strictly below retained source lower endpoint"
    - "full width-7 recurrent enumeration remains the bottleneck"
  source_lower_improved_by_p13: false
  failed_or_rejected:
    - "no further width-6 decimal polishing should be treated as source progress"
    - "no independent-match or unproved width-7 inference"
  next_attack: "carry-augmented local lift of the exact width-6 bias into width 7; otherwise event-specific mixed-suffix coupling"
  previous_successor_handoff: "P0342 terminal 2/2; P0205 screen admitted no successor; retired I0051/clade not reopened"
  artifacts:
    code: "proofnet24/P13-progress-lcs/artifacts/2026-09-20/2026-09-20T11-15-00Z__w6_integer_bellman_refinement.cpp"
    code_commit: eeda6725c4cc435d2d2542f212c089b9bfffd604
    output: "proofnet24/P13-progress-lcs/artifacts/2026-09-20/2026-09-20T11-15-00Z__w6_integer_bellman_refinement.out"
    output_commit: 1691d79b7b03579a237102610702c629389cf40e
  peer_files_modified: false
  historical_files_modified: false
  email_or_drive_used: false
  public_posting: false
  paid_compute: false
  schedule_or_permission_changes: false
  runtime_model: "GPT-5.6 Sol"
  reasoning_effort: "UNVERIFIED"
```
