Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — not GPT-6 maximum, and I do not claim otherwise. SOURCE-LEVEL BEFORE/AFTER: the repository-internal binary-LCS interval strictly moves from `L <= gamma_2 <= U_C` to `L <= gamma_2 <= U_* < U_C` by P02's newest complementary residue-optimal defect certificate, with `L=0.792665992`. P13 MECHANISM BEFORE/AFTER: the previous dependence-preserving extremal-boundary theorem gave a width-`w` finite bracket of width at most `w/N`; this run builds an exact Bellman finite-to-infinite certificate on the complete width-6 recurrent strip class and proves `3119319222655621/4000000000000000 <= gamma_6 <= 3119319222655638/4000000000000000`, interval width `17/4000000000000000 = 4.25e-15`, with the exact upper endpoint lying `51344745344362/4000000000000000` below the retained source lower bound `L`. Hence every fixed corridor width `w<=6` is now rigorously excluded from improving `L`.**

# P13 / T02 — exact width-6 Bellman residual certificate and a decisive lower-route obstruction

## 1. Scope, source, continuity, and companion coordination

This run follows `operations/PROGRESS20_2026-09-20.md`, blob `4a207f06e5c8294c83bcabcd9a1477f26f54b441`, and its LIVE20 assignment of P13 to the dependence-preserving binary-LCS boundary recursion. The target is

\[
\gamma_2=\lim_{n\to\infty}\frac{\mathbf E LCS(X_1^n,Y_1^n)}n
\]

for two independent iid uniform binary strings. The match indicators are dependent along every row and column because they reuse the same source letters. No independent Bernoulli matching model is substituted anywhere below.

The newest own substantive dependency is

`proofnet24/P13-progress-lcs/runs/2026-09-20/2026-09-20T09-18-50Z__extremal-boundary-band-bracket.md`, blob `251221b18f3dfe30043804adee5a2df7b880f627`.

That report proved, for half-width `w`,

\[
A^-_{N,w}\le N\gamma_w\le A^+_{N,w},\qquad A^+_{N,w}-A^-_{N,w}\le w,
\]

and identified

\[
A^-_{N,w}=\mathbf E L^{\mathrm{band}}_{N,w},
\qquad
\frac{A^-_{N,w}}N\le\gamma_w\le\gamma_2.
\]

Thus finite band computation already had a proved source transfer, but the residual obstacle was state growth at widths large enough to challenge `L`.

Fresh source navigation on 2026-09-20 retained Alexander Tiskin, `arXiv:2212.01582v2`, revised 2024-08-13. The current arXiv record still calls the binary coefficient unresolved and explicitly states that earlier preprint claims about the stochastic process and `gamma` were incorrect and omitted in v2. None of those removed claims is used here. The retained rigorous public lower endpoint is

\[
L=0.792665992=\frac{99083249}{125000000}
\]

from Heineman–Miller–Reichman–Salls–Sárközy–Soiffer, `arXiv:2407.10925`.

P02 remains complementary. The newest visible P02 report is

`proofnet24/P02-progress-lcs/runs/2026-09-20/2026-09-20T09-05-20Z__residue-optimal-defect-report.md`, blob `7bb9d79003d46c3108123ff209a0bc1276838126`, creation commit `e32c737f0457b153e81c82ea0b5d75bf5732e581`.

It proves an exact dual rate `lambda_*<lambda_C` and therefore

\[
\boxed{L\le\gamma_2\le U_*<U_C},
\]

with the exact separator

\[
U_*<0.82627594276228262501510658153729663282346199619319002388080618331256294443029953<U_C.
\]

That is the source-level interval shrink for this invocation. P13 does not duplicate P02's covering/cone argument.

Short pre-LIVE20 handoff only: P0342 had already been terminally handed off at frozen `2/2`; the later P0205 screen admitted no successor because its source notation could not be frozen source-faithfully. Retired I0051/clade work remains retired and is not reopened.

## 2. Exact dependence-preserving strip chain

Fix half-width `w` and put `m=2w`. A formal state is

\[
s=(x,g),\qquad x,g\in\{0,1\}^m.
\]

Let

\[
V_0=0,\qquad V_k=\sum_{i=1}^k g_i.
\]

For one fresh actual source pair `(u,v)`, define

\[
a_i={\bf1}_{\{x_{i+1}=v\}}\quad(0\le i<m),
\qquad a_m={\bf1}_{\{u=v\}}.
\]

The same incoming source bit `v` appears in every `a_i`; this is the original binary-LCS dependence. The updated profile is

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

and central reward

\[
\rho(s;u,v)=Q_w-V_w\in\{0,1\}.
\]

All computations below use exactly these four equiprobable genuine source pairs `(u,v) in {0,1}^2`.

## 3. Why the width-6 BFS is the stationary recurrent class

Let

\[
A=(u,v)=(0,1),\qquad z_0=(0^m;0^m).
\]

The earlier P13 one-defect/reset theorem proved analytically that `A^m` maps every formal strip state to `z_0`. Each `A` column shifts in a raw `0`, which does not match the common incoming `v=1`, and extends the joint zero raw/gradient suffix by one site. After `m` consecutive `A` columns the whole raw window and gradient profile are zero.

Therefore every formal state has a positive-probability path to `z_0`. Any closed recurrent class must contain `z_0`; consequently there is a unique recurrent class, namely the class `R_w` reachable from `z_0`.

For `w=6`, exact breadth-first enumeration gives

\[
\boxed{|R_6|=5,735,086}.
\tag{3.1}
\]

The enumeration is exact over the `2^{24}=16,777,216` formal bit states and records all four genuine source-pair transitions from every discovered state.

## 4. Bellman-residual theorem: finite state to infinite stationary rate

### Theorem 4.1 — exact residual bracket

Let `R` be a finite closed class of a Markov reward chain with four equiprobable source letters. For `s in R`, write `T_a s` for the four successors and `rho(s,a)` for the one-step reward. Let `H:R->Z` and `Q>=1` be any integer potential and scale. Define

\[
D_H(s)
:=Q\sum_{a=1}^4\rho(s,a)
+\sum_{a=1}^4H(T_a s)-4H(s).
\tag{4.1}
\]

If

\[
d_-:=\min_{s\in R}D_H(s),\qquad d_+:=\max_{s\in R}D_H(s),
\]

then every stationary mean reward `gamma_R` on this class satisfies

\[
\boxed{\frac{d_-}{4Q}\le\gamma_R\le\frac{d_+}{4Q}.}
\tag{4.2}
\]

Moreover, with

\[
B_H:=\frac{\max_R H-\min_R H}{Q},
\]

for every initial `s in R` and every horizon `N>=1`,

\[
\boxed{
\frac{d_-}{4Q}-\frac{B_H}{N}
\le
\frac{\mathbf E_sR_N}{N}
\le
\frac{d_+}{4Q}+\frac{B_H}{N}.
}
\tag{4.3}
\]

Thus the finite computation has an explicit infinite-horizon transfer; the residual scan is not merely a numerical estimate.

#### Proof

Put `h=H/Q` and

\[
\bar\rho(s)=\frac14\sum_a\rho(s,a).
\]

Equation (4.1) is exactly

\[
\frac{D_H(s)}{4Q}=\bar\rho(s)+(Ph)(s)-h(s).
\tag{4.4}
\]

Let `pi` be stationary on `R`. Averaging (4.4) against `pi` cancels the potential term because `pi P=pi`:

\[
\sum_s\pi(s)\frac{D_H(s)}{4Q}
=
\sum_s\pi(s)\bar\rho(s)
=\gamma_R.
\]

A convex combination of the residual values lies between their minimum and maximum, proving (4.2).

For (4.3), apply the pointwise residual inequalities along the chain and sum from time `0` to `N-1`. The potential telescopes in expectation:

\[
N\frac{d_-}{4Q}
\le
\mathbf E_sR_N+\mathbf E_s h(S_N)-h(s)
\le
N\frac{d_+}{4Q}.
\]

Since

\[
|\mathbf E_s h(S_N)-h(s)|\le\operatorname{osc}(h)=B_H,
\]

dividing by `N` gives (4.3). QED.

For the width-6 strip, `R=R_6` and `gamma_R=gamma_6` by Section 3.

## 5. Candidate generation versus exact proof

The checker first performs relative value iteration on the complete `R_6` class only to *propose* a potential. That phase uses ordinary floating arithmetic and is not proof evidence.

After 180 iterations it freezes

\[
H(s)=\operatorname{round}(10^{15}h(s))
\]

as exact signed integers and then scans (4.1) for all `5,735,086` states using only integer arithmetic. The proof consists of this second scan plus Theorem 4.1.

The exact output is

\[
Q=10^{15},
\]

\[
\boxed{d_-=3119319222655621},
\qquad
\boxed{d_+=3119319222655638}.
\tag{5.1}
\]

It also gives

\[
\max H-\min H=4140891766281466,
\]

hence

\[
\boxed{B_H=4.140891766281466.}
\tag{5.2}
\]

The executed output terminates `ALL_EXACT_CHECKS_PASS`.

## 6. New exact width-6 interval

Applying Theorem 4.1 gives

\[
\boxed{
\frac{3119319222655621}{4000000000000000}
\le\gamma_6\le
\frac{3119319222655638}{4000000000000000}.
}
\tag{6.1}
\]

Numerically, only for readability,

\[
0.779829805663905\le\gamma_6\le0.779829805663909.
\]

The exact interval width is

\[
\boxed{
\frac{17}{4000000000000000}=4.25\times10^{-15}.
}
\tag{6.2}
\]

The finite-horizon transfer (4.3) specializes to

\[
\boxed{
\frac{3119319222655621}{4000000000000000}
-
\frac{4140891766281466}{10^{15}N}
\le
\frac{\mathbf E_sR_N}{N}
\le
\frac{3119319222655638}{4000000000000000}
+
\frac{4140891766281466}{10^{15}N}
}
\tag{6.3}
\]

for every starting state in the recurrent class. This is a genuine finite-to-infinite error bound on the true dependent strip chain. No finite enumeration is promoted to `gamma_6` without the Bellman proof.

## 7. Decisive obstruction: width 6 cannot improve the retained source lower endpoint

Write the retained lower endpoint with the same denominator:

\[
L=\frac{99083249}{125000000}
=\frac{3170663968000000}{4000000000000000}.
\]

Subtracting the exact Bellman upper endpoint in (6.1),

\[
L-\frac{3119319222655638}{4000000000000000}
=
\boxed{\frac{51344745344362}{4000000000000000}}>0.
\tag{7.1}
\]

Therefore

\[
\boxed{\gamma_6<L.}
\tag{7.2}
\]

The band corridors are nested, so the band constants are monotone. To avoid notation collision with the source constant, write `beta_w` for the half-width-`w` band constant. Then

\[
\beta_1\le\beta_2\le\cdots\le\beta_6< L\le\gamma_2.
\]

Hence **no exact finite or stationary certificate confined to a fixed corridor `w<=6` can raise the current source lower endpoint**, because every such finite lower value is at most its limiting band constant.

This corrects the previous operational hope that width 6 might be the first useful lower-bound width. It is not. The next lower-side source improvement must use width at least 7, and likely requires a compressed recurrence rather than full-state enumeration.

## 8. What moved and what did not

### Source-level movement

Before this invocation, the newest P13 report carried

\[
L\le\gamma_2\le U_C.
\]

The newest P02 companion now proves

\[
\boxed{L\le\gamma_2\le U_*<U_C}.
\]

That strict source-level shrink is companion-derived. P13 does **not** claim a new source lower endpoint in this run.

### P13 mechanism movement

Before:

\[
A^-_{N,w}\le N\gamma_w\le A^+_{N,w},
\qquad A^+_{N,w}-A^-_{N,w}\le w,
\]

with the zero-subtraction lower transfer `A^-_{N,w}/N<=gamma_2`.

After, at the largest width now exactly certified by the complete recurrent quotient:

\[
\boxed{
\gamma_6\in
\left[
\frac{3119319222655621}{4\cdot10^{15}},
\frac{3119319222655638}{4\cdot10^{15}}
\right]
}
\]

and the reusable residual theorem (4.2)–(4.3) converts any finite integer potential on a reachable strip quotient directly into a rigorous infinite-horizon bracket and finite-horizon error bound.

The demonstrated gain is not merely a smaller auxiliary constant: it decisively excludes all widths `w<=6` from the lower-endpoint route and tells the next computation exactly where not to spend resources.

## 9. Failure / obstruction

The hoped-for source-lower attack at width 6 fails decisively: the exact upper certificate places `gamma_6` roughly `0.0128361863360905` below `L`. No amount of longer finite-horizon computation at this fixed width can overcome that structural gap.

The full-state quotient also exposes the scale problem. Width 6 already has `5,735,086` recurrent states. The naive formal index for width 7 has `2^{28}` states before reachability pruning, and the observed reachable-state growth makes a direct extension unattractive. This is a computational obstruction, not a proof that width 7 is impossible.

An earlier `Q=10^12` exploratory Bellman certificate from this same invocation remains immutably archived in the artifact directory; it is superseded by the stronger `Q=10^15` certificate above and is not used for any final claim.

## 10. Next attack

The next P13 route is a **carry-augmented local Bellman lift** rather than a full width-7/11 state enumeration.

The exact column recursion propagates information left-to-right through a one-bit carry. Therefore a central width-6 block inside a wider corridor can be updated from its local raw/gradient bits plus the carry entering the block. The plan is to use the certified width-6 bias as a local potential, augment it by that entering carry, and derive exact worst-case residual corrections for the omitted outer context. If the correction can be made small enough at widths where the band rate exceeds `L`, it yields a rational Bellman lower certificate without materializing the full wider recurrent class.

The first target is a source-valid lower certificate at the smallest tractable width `w>=7`; if local residuals remain too loose, enlarge the local window before increasing the global width. This is materially different from the now-closed width-6 full-state route.

P02 should continue the complementary covering/cone variational upper-bound route; P13 should not duplicate its residue/slack computation.

## 11. Exact artifacts and readback

Final checker:

`proofnet24/P13-progress-lcs/artifacts/2026-09-20/2026-09-20T10-13-09Z__w6_bellman_exact_certificate_strong.cpp`

creation commit `cfd2a0b2c3506f6281cbc59a581fd2f3bb1e9fd7`, verified read-back blob `1c82608767c466a4fbfcbbacd92fbff6485126f3`.

Executed output:

`proofnet24/P13-progress-lcs/artifacts/2026-09-20/2026-09-20T10-13-09Z__w6_bellman_exact_certificate_strong.out`

creation commit `47826f15b32f90bcf9c6252499dd579c260b50c1`, verified read-back blob `bf1870aa8d4ed056364f6123817279a1cdd4fd50`.

The checker uses floating arithmetic only to propose `H`; every asserted interval endpoint, width, recurrent-class count, and comparison with `L` is checked afterward by exact integer arithmetic. The output ends `ALL_EXACT_CHECKS_PASS`.

## 12. Ledger delta

```yaml
ledger_delta:
  slot: P13
  native_assignment: T02_binary_LCS
  status: PARTIAL_SOURCE_OPEN
  runtime:
    model: GPT-5.6_Sol
    reasoning_level: UNVERIFIED
    requested_gpt6_maximum_satisfied: false
  source_metric:
    lower: "L = 0.792665992 = 99083249/125000000"
    before: "L <= gamma_2 <= U_C"
    after: "L <= gamma_2 <= U_* < U_C"
    movement_origin: "P02 companion residue-optimal defect certificate"
    p13_lower_endpoint_movement: none
  p13_mechanism:
    new_transfer: "integer Bellman residual theorem: d_-/(4Q) <= gamma_R <= d_+/(4Q), with finite-horizon correction osc(H)/(Q N)"
    width6_recurrent_states: 5735086
    width6_lower: "3119319222655621/4000000000000000"
    width6_upper: "3119319222655638/4000000000000000"
    width6_interval_width: "17/4000000000000000 = 4.25e-15"
    width6_gap_below_L: "51344745344362/4000000000000000"
    width6_Hosc_over_Q: "4140891766281466/1000000000000000"
    consequence: "all fixed band widths w<=6 are rigorously below L and cannot improve the retained source lower endpoint"
  checker:
    code_path: "proofnet24/P13-progress-lcs/artifacts/2026-09-20/2026-09-20T10-13-09Z__w6_bellman_exact_certificate_strong.cpp"
    code_commit: cfd2a0b2c3506f6281cbc59a581fd2f3bb1e9fd7
    code_blob: 1c82608767c466a4fbfcbbacd92fbff6485126f3
    output_path: "proofnet24/P13-progress-lcs/artifacts/2026-09-20/2026-09-20T10-13-09Z__w6_bellman_exact_certificate_strong.out"
    output_commit: 47826f15b32f90bcf9c6252499dd579c260b50c1
    output_blob: bf1870aa8d4ed056364f6123817279a1cdd4fd50
    status: ALL_EXACT_CHECKS_PASS
  failure:
    - "width 6 is decisively below L, so the previous hope of a width-6 source lower improvement is closed"
    - "naive wider full-state enumeration has severe state growth; no width>=7 exact source lower certificate is claimed"
  next_attack: "carry-augmented local Bellman lift of the width-6 bias into wider true-source strips; certify a lower residual above L without full-state enumeration"
  companion:
    P02_latest_report: "proofnet24/P02-progress-lcs/runs/2026-09-20/2026-09-20T09-05-20Z__residue-optimal-defect-report.md"
    P02_latest_commit: e32c737f0457b153e81c82ea0b5d75bf5732e581
    coordination: "P02 upper variational/cone route; P13 dependent boundary/Bellman lower-route and finite-to-infinite transfer"
  previous_successor_handoff: "P0342 terminal handoff preserved at 2/2; P0205 not admitted; I0051 clade work remains retired"
```
