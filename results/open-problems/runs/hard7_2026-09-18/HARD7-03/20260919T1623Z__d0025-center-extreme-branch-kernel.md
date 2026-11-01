Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — this is not GPT-6 at maximum, and I do not claim otherwise. Frozen metric MOVED: `L <= Delta_2(Q): 625000/7314597 -> 25000000/292367491`. Methods tried: B1 / B11 / B15.**

# HARD7-03 — one-sided extreme-branch kernel improves the nonnested centre pair

Status: **PARTIAL**. Seppäläinen Problem 4 is not solved in full.

## 1. Continuity, ownership, and capability honesty

This execution resumes the exclusive claim `operations/claims/D0025.md`, owner `HARD7-03`, canonical key `disordered_asep_open_1999::problem_4`, status `ADMITTED_ACTIVE / HARD / PARTIAL`.

At run start I re-read `operations/hard7_2026-09-18/CONTROL.md`, `operations/NEW_METHODS_2026-09-16.md`, `operations/new_methods_2026-09-16/OWNER_DIRECTIVE.md`, `probability_campaign_2026_09/INDEX.md`, `probability_campaign_2026_09/RANKING.md`, root `POSTED.md`, `RESULTS.md`, `QUEUE.md`, the D0025 claim/source trail, the newest own checkpoint `20260919T1523Z__d0025-exact-nested-pair-kernel.md`, and the newest visible neighboring HARD7-02/HARD7-04 reports. No D0025 collision, release, posted equivalent, or ownership change was found. Shared root ledgers were not edited; this report supplies a `ledger_delta` only.

The large intake ledgers are not safely renderable byte-for-byte in one connector response, so their indexed D0025 source/alias trail was checked rather than falsely claiming a literal whole-file dump.

The exposed task interface still has no model selector or reasoning-effort selector and no guaranteed execution duration. GPT-6/maximum therefore remains prompt-requested only. This execution identifies as GPT-5.6 Sol; reasoning telemetry is not exposed, hence `UNVERIFIED`. Changing model/reasoning would require an authorized platform interface that actually exposes those controls. Historical `You cannot modify this task` failures are authorization/context restrictions; the compliant workaround is the owning/authorized context or platform support, never a permission bypass or duplicate schedule. No schedule was created, disabled, re-enabled, or modified here.

## 2. Source and bounded current-literature refresh

Primary source remains Timo Seppäläinen, *Recent Results and Open Problems on the Hydrodynamics of Disordered Asymmetric Exclusion and Zero-Range Processes*, Resenhas IME-USP 4(1) (1999), 1–15, Problem 4, arXiv `math/9906194`, DOI `10.11606/resimeusp.v4i1.74889`.

The frozen residual is the source's finite-capacity disordered asymmetric exclusion flat-flux question after excluding the known ordinary `K=1` iid site-disorder theorem. The test case is

\[
K=2,\qquad Q=\tfrac12\delta_{1/2}+\tfrac12\delta_1,
\]

and

\[
\Delta_2(Q)=\sup\{\delta\ge0:f_{2,Q}\text{ is constant on }[1-\delta,1+\delta]\}.
\]

A bounded 2026-09-19 search using the source title and the phrases `disordered asymmetric K-exclusion plateau site disorder K=2`, `partial exclusion random environment asymmetric site disorder flux plateau`, and `Seppalainen Problem 4 K-exclusion disorder flux plateau` found no theorem closing this exact iid site-rate `K>=2` residual. Closest visible later literature remained: Allan Sly, arXiv `1609.06589` (`K=1` iid disorder); Floreani–Redig–Sau, arXiv `1911.12564`, SPA 142 (2021), random site capacities rather than these iid site rates; Gonçalves–Hayashi–Sasada, arXiv `2405.15142`, a product-rate/gradient partial-exclusion class; and Ayyer–Misra, J. Phys. A 57 (2024) 315001, a different integrable K-exclusion model. Honest status: **OPEN_BY_BOUNDED_SEARCH**, not a worldwide-openness or novelty certificate.

## 3. Frozen metric and carry-in

The stable source-relevant metric is a rigorous lower bound

\[
L\le\Delta_2(Q).
\]

The preceding exact nested-pair checkpoint certified

\[
G_1(0)\le A_{\rm old}:=\frac{7314597}{2500000}=2.9258388,
\]

and through the already established D0025 disorder-to-plateau transfer

\[
L_{\rm old}=\frac1{4A_{\rm old}}=\frac{625000}{7314597}=0.0854455823061749\ldots.
\]

That checkpoint removed the common-window loss exactly for the nested edge and near-edge adjacent-pair classes. The remaining pair-level structural loss was the genuinely nonnested centre pair.

## 4. Idea before code; method rotation

Before writing the checker I committed `artifacts/hard7_2026-09-18/HARD7-03/20260919T1623Z__idea-center-extreme-branch-kernel.md` at `3a8e6a34fe689113c036622e9393ebce3e6195ce` and read it back. That exploratory note contained one event-label error: it called the second aligned event for a fixed left-centre pair the `A_1`-maximum event. Before theorem-level use I wrote and read back the immutable correction `artifacts/hard7_2026-09-18/HARD7-03/20260919T1623Z__idea-correction-center-events.md` at `794a3bf116f2117b2d92f5678a0d4a0429673d61`. The correct second event is `A_0` maximal; the proposed rational correction was unchanged.

The previous run used B6/B23/B28. This run uses:

- **B1 — CHANGE THE CATEGORY.** Replace the full centre-pair order-cone integral by a deterministic two-clock kernel plus a common-core gap variable. **Successful.**
- **B11 — DUALIZE.** Integrate only the positive one-sided gap transform discarded by the common-window bound instead of the full joint law. **Successful.**
- **B15 — BREAK THE SYMMETRY ON PURPOSE.** Restrict to first-layer cones where one unique outer branch shares exactly the common-core shift. **Successful.**

## 5. Exact deterministic two-clock kernel

Let `C,D` be iid unit exponentials, `0<theta<1`, and put

\[
q=1-\theta,\qquad a=2-\theta.
\]

For deterministic `s,t`, define

\[
K_\theta(s,t)=\mathbb E e^{\theta\min(s+C,t+D)}.
\]

The previous checkpoint's exact calculation is equivalently

\[
\boxed{
K_\theta(s,t)=\frac{e^{\theta\min(s,t)}}q-
\frac{\theta}{qa}e^{\min(s,t)-q\max(s,t)}.}
\tag{5.1}
\]

Thus

\[
K_\theta(R,R)=\frac2a e^{\theta R}.
\tag{5.2}
\]

Coordinatewise monotonicity of the minimum gives, for `g>0` and every `T>=R`,

\[
K_\theta(R+g,T)-K_\theta(R,R)
\ge K_\theta(R+g,R)-K_\theta(R,R).
\]

Substitution into (5.1) yields

\[
\boxed{
K_\theta(R+g,R)-K_\theta(R,R)
=e^{\theta R}\frac{\theta}{qa}(1-e^{-qg}).}
\tag{5.3}
\]

This is the new route: a strict correction can be certified without solving the whole nonnested joint law.

## 6. Centre-pair geometry

For the left-centre adjacent pair set

\[
R=\max(Y_{-1},Y_0),\qquad X=Y_{-2},\qquad Z=Y_1,
\]

so

\[
S=\max(R,X),\qquad T=\max(R,Z).
\tag{6.1}
\]

With first-layer iid unit exponentials `(A_{-1},A_0,A_1)` and independent second-layer unit exponentials,

\[
\begin{aligned}
Y_{-2}&=A_{-1}+B_{-2},\\
Y_{-1}&=\max(A_{-1},A_0)+B_{-1},\\
Y_0&=\max(A_{-1},A_0,A_1)+B_0,\\
Y_1&=\max(A_0,A_1)+B_1.
\end{aligned}
\tag{6.2}
\]

There are two disjoint first-layer events on which one unique branch and both common branches have the same shift.

On

\[
E_L=\{A_{-1}\ge A_0,A_1\},
\]

we have `X=A_{-1}+B_{-2}` and `R=A_{-1}+M`, where `M=max(B_{-1},B_0)`. On `B_{-2}>M`, put `g=B_{-2}-M`; then `S=R+g`, `T>=R`, so (5.3) applies.

On the disjoint event

\[
E_M=\{A_0\ge A_{-1},A_1\},
\]

we have `Z=A_0+B_1` and `R=A_0+max(B_{-1},B_0)`. On `B_1>M`, the same bound applies with identical expectation. The events are disjoint almost surely because the `A` variables are continuous.

## 7. Exact Laplace integrals

Put `b=3-theta`. The first-layer transform is

\[
\begin{aligned}
J_A&:=\mathbb E[e^{\theta A_{-1}};E_L]\\
&=\int_0^\infty e^{-qx}(1-e^{-x})^2\,dx\\
&=\frac1q-\frac2a+\frac1b
=\boxed{\frac{2}{qab}}.
\end{aligned}
\tag{7.1}
\]

For `M=max(B_1,B_2)`, `f_M(m)=2e^{-m}(1-e^{-m})`. With independent `B~Exp(1)`,

\[
\int_m^\infty e^{-x}(1-e^{-q(x-m)})\,dx
=\frac{q}{a}e^{-m}.
\]

Hence

\[
\begin{aligned}
J_B&:=\mathbb E[e^{\theta M}(1-e^{-q(B-M)})\mathbf 1_{\{B>M\}}]\\
&=\frac{2q}{a}\left(\frac1a-\frac1b\right)
=\boxed{\frac{2q}{a^2b}}.
\end{aligned}
\tag{7.2}
\]

One aligned extreme event therefore contributes

\[
\delta_{\rm one}=\frac{\theta}{qa}J_AJ_B
=\boxed{\frac{4\theta}{q a^4 b^2}}.
\tag{7.3}
\]

Using both disjoint events gives, for one centre adjacent pair,

\[
\boxed{
\delta_{\rm ctr}\ge\frac{8\theta}{q a^4b^2}.}
\tag{7.4}
\]

This is only a lower bound: the unused first-layer cone and other helpful gap configurations are deliberately discarded.

## 8. Four-step correction

There are two reflected centre adjacent pairs, and the already-certified four-step deterministic identity counts each adjacent pair in two fourth-step predecessor windows. Thus the total pair subtraction improves by at least

\[
\boxed{
\Delta C_{\rm ctr}=4\delta_{\rm ctr}
=\frac{32\theta}{q a^4b^2}.}
\tag{8.1}
\]

At

\[
\theta=\frac{723}{1250},\quad q=\frac{527}{1250},\quad a=\frac{1777}{1250},\quad b=\frac{3027}{1250},
\]

the checker gives exactly

\[
J_A=\frac{3906250000}{2834721933},\qquad
J_B=\frac{1646875000}{9558445683},
\]

\[
\delta_{\rm one}=\frac{3677368164062500000000}{16049588934017308109901},
\]

\[
\delta_{\rm ctr}=\frac{7354736328125000000000}{16049588934017308109901}
=0.4582507600887237\ldots,
\]

and

\[
\Delta C_{\rm ctr}=\frac{29418945312500000000000}{16049588934017308109901}
=1.8330030403548947\ldots .
\]

The previous exact bound was

\[
U_4^{\rm nested}=\frac{464527332753365031710169245072092857523367477290039062500000}{533551258662847599879934006185557225047638076531060575909}.
\]

The four-step recurrence divides pair-subtraction improvements by `q`, so

\[
U_4^{\rm new}=U_4^{\rm nested}-\frac{\Delta C_{\rm ctr}}q
\]

and exact simplification gives

\[
\boxed{
U_4^{\rm new}=\frac{462207595847970865379094425847318588877127242915039062500000}{533551258662847599879934006185557225047638076531060575909}
=866.2852693972202\ldots.}
\tag{8.2}
\]

This strictly improves `870.6329995688399...`.

## 9. Exact Chernoff comparison and metric movement

Set

\[
A_{\rm new}=\frac{292367491}{100000000}=2.92367491,
\qquad
x=4\theta A_{\rm new}=\frac{211381695993}{31250000000}.
\]

The exact checker evaluates

\[
S_{32}(x)=\sum_{k=0}^{32}\frac{x^k}{k!}<e^x
\]

and verifies the exact rational inequality

\[
S_{32}(x)-U_4^{\rm new}>0,
\]

with decimal margin `6.12242087777812e-06`. Hence

\[
U_4^{\rm new}<e^{4\theta A_{\rm new}}.
\]

By the already established D0025 four-step Chernoff/shape transfer,

\[
G_1(0)\le A_{\rm new}=2.92367491.
\]

Then the previously proved disorder-to-plateau implication gives

\[
\boxed{
\Delta_2(Q)\ge L_{\rm new}
:=\frac1{4A_{\rm new}}
=\frac{25000000}{292367491}
=0.0855088228670403\ldots .}
\tag{9.1}
\]

Therefore the fixed metric moves

\[
\boxed{
\frac{625000}{7314597}
\longrightarrow
\frac{25000000}{292367491}.}
\]

The exact gain is

\[
\frac{135243125000}{2138550372566127}
=6.3240560865404\times 10^{-5}>0.
\]

This is a **PARTIAL** theorem on the frozen binary `K=2` case, not a solution of Seppäläinen Problem 4 in full.

## 10. Exact checker and output

Checker:

`artifacts/hard7_2026-09-18/HARD7-03/center_extreme_branch_20260919T1623Z.py`

creation commit `e2b8dd541849b79cccd0176f4731fe6793d54f24`.

The checker was executed this run with Python `fractions.Fraction`; archived stdout:

`artifacts/hard7_2026-09-18/HARD7-03/center_extreme_branch_20260919T1623Z.out`

commit `2bb6a74fbea1a09d764ac86782d98a421414d235`, ending

`ALL_EXACT_CHECKS_PASS = True`.

One checker comment says “left and right first-layer extreme events”; the arithmetic it checks is correct, and Sections 6–7 plus the immutable correction artifact give the precise events (`A_{-1}` maximal and `A_0` maximal for the fixed left-centre pair). A comment-only update attempt was blocked by the connector safety gate, so I did not bypass it. This is a self-check, not an independent closure audit.

## 11. Remaining obligation and next route

The remaining losses are now explicit: the third first-layer order cone is unused; even on the two used cones the one-sided monotonicity bound discards configurations where both unique branches help; the Chernoff parameter was inherited rather than globally reoptimized; and the four-step moment bound itself may still be loose.

A natural next attack is the **full conditional centre pair**. Conditional on the first layer,

\[
\min(\max(R,X),\max(R,Z))=\max(R,\min(X,Z)),
\]

which may permit a complete joint-survival integration rather than further event slicing. Suggested next triple: **B7 / B18 / B25** — take the full conditional centre kernel as the limit object, recast it via a joint-CDF/operator integral, and count the same contribution both by winner regions and survival functions as an internal consistency check. Do not repeat B1/B11/B15 immediately.

## 12. Closure discipline

- Source status: **OPEN_BY_BOUNDED_SEARCH**.
- Worker status: **PARTIAL**.
- Frozen metric: **MOVED**.
- No PROVED / REFUTED / KNOWN / CLOSED / audit-complete / paper-ready label is asserted.
- No independent audit was requested or fabricated.
- No shared root ledger, neighboring track file, scheduler, Gmail, Drive, public posting, workflow, or permission was modified.

## 13. Structured ledger delta

```yaml
ledger_delta:
  track: HARD7-03
  canonical_target: D0025
  owner_claim: operations/claims/D0025.md
  source: Seppalainen 1999 Problem 4
  frozen_case: K=2, Q=(1/2)delta_{1/2}+(1/2)delta_1
  metric: rigorous lower bound L <= Delta_2(Q)
  before: 625000/7314597
  after: 25000000/292367491
  before_decimal: 0.0854455823061749
  after_decimal: 0.0855088228670403
  movement: true
  status: PARTIAL
  source_status: OPEN_BY_BOUNDED_SEARCH
  methods: [B1, B11, B15]
  center_pair_gain_lower_bound: 7354736328125000000000/16049588934017308109901
  total_pair_subtraction_gain: 29418945312500000000000/16049588934017308109901
  U4_new_decimal: 866.2852693972202
  shape_bound: G_1(0) <= 292367491/100000000
  checker: artifacts/hard7_2026-09-18/HARD7-03/center_extreme_branch_20260919T1623Z.py
  output: artifacts/hard7_2026-09-18/HARD7-03/center_extreme_branch_20260919T1623Z.out
  exact_checker_tail: ALL_EXACT_CHECKS_PASS = True
  closure: false
```
