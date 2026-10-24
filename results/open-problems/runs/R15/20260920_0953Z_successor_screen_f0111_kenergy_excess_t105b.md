Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — not GPT-6 maximum. NATIVE I0076 METRIC NO MOVEMENT: `NOT_SCOREABLE_NO_SURVIVING_FROZEN_CANDIDATE -> NOT_SCOREABLE_NO_SURVIVING_FROZEN_CANDIDATE`. RETAINED-SCREEN MOVEMENT: the independent K-K energy roof is replaced by an exact K-excess-coupled roof, and the last N=12,13 smooth gate is strictly sharpened. Methods #3, #25, #27.**

Problem/source: Krzysztof Burdzy and Michael Scheutzow, *Forward Brownian Motion*, arXiv:1302.6958v4 / PTRF 160 (2014), Problem 7.2, intake I0076.

Native status: **OPEN / PARTIAL / RETIRED-HANDOFF**. No source-level solution or refutation is claimed.

Retained successor-screen status: **F0111 / PENDING / SELF_CHECK_ONLY / NOT CLAIMED**. No claim of solving Talagrand's discrete Convexity Conjecture is made.

# 1. Source fidelity and repository continuity

I re-read the source definitions and Problem 7.2 rather than inheriting a paraphrase. Definition 2.1 says that X is FBM if there are random times S_n tending to -infinity a.s. such that every centered future `(X_{S_n+t}-X_{S_n})_{t>=0}` is standard Brownian motion; BBM means the time-reversed process is FBM; and 2BM means there is one random time S for which the complete centered future and past are independent standard Brownian motions. Problem 7.2 assumes X is FBM and BBM and that, for some arbitrary random time T, the two complete centered half-processes at T are independent. It does **not** say that T is a stopping time and it does **not** separately assume that either seam half is Brownian.

The six-run I0076 handoff remains controlling. The source Section-6/Theorem-6.1 construction supplies FBM, BBM and non-2BM but R15 eliminated it as a counterexample because it has no source-valid independent real seam. The later Brownian-prefix/BES construction supplied FBM, BBM and an exact independent seam, but the R15 Palm argument proved that construction is actually 2BM. Hence there is no surviving frozen candidate on which the owner's four obligations can honestly be scored. Historical 2/4 or 3/4 values belong to eliminated candidates or to the retired positive route; they are not a current frozen-candidate score.

I also re-read `probability_campaign_2026_09/INDEX.md`, `RANKING.md`, root `POSTED.md`, root `RESULTS.md`, root `QUEUE.md`, the latest operations implementation material, the newest R15 report, the neighboring Burdzy R07 handoff, and the intake search for I0076. `QUEUE.md` still records **zero newly certified free READY entries** and explicitly says a listed/PENDING row is not automatically dispatchable. I therefore did not steal or promote another outside source.

Fresh bounded source/literature searches dated 2026-09-20 recovered the original paper and Burdzy's current open-problems page but no accessible later primary source explicitly announcing a resolution of exact Problem 7.2. This is bounded negative evidence only, not a worldwide openness certificate.

# 2. Why the retained F0111 screen is the lawful object this run

With I0076 retired after six unchanged native runs and no newly certified free READY successor, the only lawful active mathematical object already retained by R15 is the F0111 screen. The latest report reduced the dimension-30, full-support, two-level Hessian-null first-bifurcation mechanism on the z>1 branch to the two scalar cells

\[
N:=|K|\in\{12,13\}.
\]

Write `s=z-1>0`. At exact contact q let

\[
F(q)=\sum_i q_i-\log S,
\qquad
S=\sum_i e^{q_i}-29,
\qquad
r_i=\frac{e^{q_i}}S.
\]

For the K block, the carried exact scalar identities are

\[
\sum_{j\in K}e^{q_j}=U_K,
\qquad
\eta:=U_K-N=\sum_{j\in K}(e^{q_j}-1),
\tag{2.1}
\]

and the residual coordinate cap gives

\[
1\le v_j:=e^{q_j}\le c_K:=\frac{U_K}{L_K}.
\tag{2.2}
\]

The preceding smooth-secants report used convexity of `v log v` to obtain

\[
E_{1,K}:=\sum_{j\in K}r_jq_j
=\frac1S\sum_{j\in K}v_j\log v_j
\le
K_{\rm sec}:=
\frac{\eta}{S}\frac{c_K\log c_K}{c_K-1}.
\tag{2.3}
\]

It still bounded the K-K pair energy separately by

\[
\overline E_K=\frac{y(N-1)}2\log^2c_K.
\tag{2.4}
\]

The weakness is structural: (2.4) does not force the K-K energy to disappear when the K excess eta disappears. This run fixes exactly that point.

# 3. Method #3 — stronger theorem: K excess controls all K-K contact energy

Let the quadratic certificate be

\[
P(q)=\sum_i A_iq_i+\sum_{i<j}B_{ij}q_iq_j,
\]

with nonnegative coefficients and exact interior contact, and assume the contact Hessian

\[
H=D^2(P-F)(q)\succeq0.
\]

Define

\[
E_{KK}:=\sum_{i<j\in K}B_{ij}q_iq_j.
\tag{3.1}
\]

## Theorem R15-F0111-KPAIR — excess-coupled complementary energy roof

In the retained full-support K regime (2.1)--(2.2), every exact quadratic contact satisfies

\[
\boxed{
0\le E_{KK}\le\frac{\eta}{2}E_{1,K}
\le\frac{\eta}{2}K_{\rm sec}.
}
\tag{3.2}
\]

This permits completely arbitrary heterogeneity inside K.

### Proof

For a multilinear quadratic P, its pure second derivatives vanish. Since

\[
\partial_iF=1-r_i,
\]

we have

\[
H_{ii}=r_i(1-r_i),
\qquad
H_{ij}=B_{ij}-r_ir_j\quad(i\ne j).
\tag{3.3}
\]

Because `H>=0`, every 2-by-2 principal minor is nonnegative, so

\[
B_{ij}-r_ir_j
\le\sqrt{r_ir_j(1-r_i)(1-r_j)}.
\]

Thus

\[
\begin{aligned}
B_{ij}
&\le r_ir_j+\sqrt{r_ir_j(1-r_i)(1-r_j)}\\
&=\sqrt{r_ir_j}
\left(\sqrt{r_ir_j}+\sqrt{(1-r_i)(1-r_j)}\right)\\
&\le\sqrt{r_ir_j}\le\frac{r_i+r_j}{2}.
\end{aligned}
\tag{3.4}
\]

The middle inequality is Cauchy--Schwarz applied to the two unit vectors
`(sqrt(r_i),sqrt(1-r_i))` and `(sqrt(r_j),sqrt(1-r_j))`; the last one is AM--GM.

Since q_j>=0 on K,

\[
\begin{aligned}
E_{KK}
&\le\frac12\sum_{i<j\in K}(r_i+r_j)q_iq_j\\
&=\frac12\left[
\left(\sum_{i\in K}r_iq_i\right)
\left(\sum_{j\in K}q_j\right)
-\sum_{i\in K}r_iq_i^2
\right]\\
&\le\frac12E_{1,K}\sum_{j\in K}q_j.
\end{aligned}
\tag{3.5}
\]

This is the double-counting step: each unordered pair contributes once to the product of the two first moments, and the diagonal is then removed exactly.

Finally `q_j=log v_j<=v_j-1`; summing and using (2.1),

\[
\sum_{j\in K}q_j\le\eta.
\tag{3.6}
\]

Combining (3.5), (3.6) and (2.3) proves (3.2). QED.

The point is not the constant 1/2 by itself. It is that the pair energy now **must vanish with the same scalar excess that collapses the K block**. In particular, as eta tends to zero the new pair-energy roof is second order in the K excess once the secant moment is inserted.

# 4. Method #25 — an exact t=1 face-slack identity

There is a second exact consequence, obtained by counting the same contact budget through the complementary J face.

Let `q_J` equal q on J and zero on K. The previously proved complement-energy identity at t=1 says

\[
P(q_J)-F(q_J)
=E_{KK}+D_J-W-F(q_J).
\]

Using full value/gradient contact, equivalently `W=D-F(q)`, and writing

\[
D_K=\sum_{j\in K}q_j(1-r_j),
\]

this becomes

\[
P(q_J)-F(q_J)
=E_{KK}+F(q)-F(q_J)-D_K.
\tag{4.1}
\]

But setting the K coordinates to zero changes the logarithmic denominator from S to

\[
S-\eta,
\]

because `sum_K e^{q_j}=N+eta` whereas the zeroed K block contributes N. Therefore

\[
F(q)-F(q_J)
=\sum_{j\in K}q_j-\log\frac{S}{S-\eta}.
\]

Since

\[
D_K=\sum_{j\in K}q_j-E_{1,K},
\]

we get the exact identity

\[
\boxed{
P(q_J)-F(q_J)
=E_{KK}+E_{1,K}-\log\frac{S}{S-\eta}.
}
\tag{4.2}
\]

Global majorization forces the left side to be nonnegative. Hence every survivor must satisfy the new K-only necessary condition

\[
\boxed{
\log\frac{S}{S-\eta}
\le E_{1,K}+E_{KK}
\le\left(1+\frac\eta2\right)K_{\rm sec}.
}
\tag{4.3}
\]

This identity is useful conceptually even where (4.3) alone does not yet contradict the scalar cell: it identifies the exact amount of face slack available to absorb a negative tangent of the J-face ray. The K distribution is no longer an independent source of uncontrolled pair energy.

# 5. Method #27 — remove the K distribution from the last smooth gate

The preceding adaptive-ray reduction already removed arbitrary J heterogeneity: for

\[
L=\log S,
\qquad
t=1+\frac{7}{100L},
\]

its J-face optimization is attained in the closure at the two-heavy profile encoded by `H_J^*(delta,s)`. The preceding smooth-secants report therefore had the necessary condition

\[
\Gamma_N^{\rm sec}
=\log S-\overline E_K-K_{\rm sec}-H_J^*\le0.
\tag{5.1}
\]

Theorem (3.2) eliminates the separate K-K optimization. Every survivor must instead satisfy

\[
\boxed{
\widehat\Gamma_N(\delta,s)
:=
\log S
-\left(1+\frac{\eta}{2}\right)K_{\rm sec}
-H_J^*(\delta,s)
\le0,
\qquad N\in\{12,13\}.
}
\tag{5.2}
\]

Thus all K contact-distribution variables and the old independent K-K energy roof have disappeared. The only remaining variables are the two scalar parameters `(delta,s)`.

At the exact lower scalar boundary `U_K=N`, one has `eta=0`. Since every `v_j>=1` and their sum is N, necessarily

\[
v_j=1,\qquad q_j=0\qquad(j\in K),
\]

so

\[
K_{\rm sec}=E_{1,K}=E_{KK}=0
\]

**exactly**. This is where the new gate is structurally sharper than (5.1): the K side cannot retain a fictitious pair-energy allowance after the K block has collapsed to the zero face.

I used private numerical scratch only as route finding after writing the idea note; it is **not evidence and is not counted as verification**. It suggests that (5.2) has the correct sign on the complete scalar-feasible N=12 and N=13 cells, but I do not promote that observation to a theorem. The remaining proof obligation is a global exact sign proof for `widehat Gamma_N` (or an equivalent tangent/convex-dual argument) on those two cells.

# 6. What moved and what did not

## Native I0076

No movement. There is still no surviving frozen counterexample candidate. I did not restart the retired problem, did not substitute deterministic-time independence, and did not impose a stopping-time hypothesis.

## Retained F0111 screen

There is genuine theorem-level movement:

1. the K-K pair energy is no longer bounded independently of K excess;
2. it obeys the exact arbitrary-heterogeneity roof `E_KK <= (eta/2) K_sec`;
3. the t=1 face slack is now exactly `E_KK+E_1,K-log(S/(S-eta))`;
4. the final N=12,13 necessary gate is the strictly more structural two-variable inequality (5.2).

This is **not** a full elimination of N=12 or N=13 in this report and is **not** a solution of the full discrete Convexity Conjecture.

# 7. Validation discipline

The research idea was written to

`artifacts/R15/f0111_kenergy_excess_idea_t105b.md`

before any repository validation code was created, at commit

`93b74815489d2297d3d1ff6e5d3658a6b7148919`.

No finite enumeration or finite numerical claim is needed for Theorems (3.2), (4.2) or the implication (5.2): their proofs are symbolic and are written on the page. I therefore did **not** manufacture a checker merely to produce a certificate. Private scratch calculations are explicitly non-evidence. There is no independent audit this run.

# 8. Current literature check

Dated 2026-09-20 searches of the original Burdzy--Scheutzow title, Problem-7.2 language, later-author pages and nearby citing literature found the 2014 primary source and Burdzy's current open-problems page, but no accessible primary source explicitly claiming an exact resolution of Problem 7.2. Again, this is bounded negative evidence only.

For the retained F0111 context, Ascoli--He--Park--Talagrand, arXiv:2608.11183 (2026-08-11), reformulate Talagrand's **discrete** Convexity Conjecture via k-thresholds and prove broad classes rather than the universal statement. Jinyoung Park, arXiv:2609.14681 (2026-09-13), proves a dimension-free comparison and explicitly describes its consequence as a bound toward the conjecture. I found no basis in this bounded search for calling the universal discrete conjecture solved. Novelty of the restricted R15 screen statements remains **UNVERIFIED**.

# 9. Next mathematical attack

The highest-value next step is no longer another K-distribution estimate. It is one of two equivalent scalar tasks:

1. prove `widehat Gamma_N(delta,s)>0` throughout each exact scalar-feasible cell for N=12 and N=13; or
2. use (4.2) as the exact face slack and the J-face convex dual to show that the available K slack is too small to recover from the negative J-ray tangent.

The second formulation may be cleaner. At `eta=0`, the face slack vanishes exactly, so any strictly negative J-face tangent already contradicts global majorization. For `eta>0`, (3.2)--(4.3) quantify exactly how much recovery budget is available. This suggests a stability proof rather than another coarse entropy envelope.

# 10. Model / reasoning / scheduler boundary

Still true in this run: the exposed scheduler/task interface provides prompt/title, schedule/timing or timing mode, enabled state and ordinary update controls. It exposes **no binding model-family selector, no reasoning-effort selector, no authenticated applied-model/effort receipt, and no guaranteed hour-long execution field**. GPT-6/maximum is therefore only requested in prompt text here, not authenticated or bindable by this surface.

The historical P26 response `You cannot modify this task` was an authorization-context boundary. Repository continuity records a later successful P26 update from an authorized P/C context. The lawful workaround for an edit-denied task is the owning/authorized workspace/account/API/admin context or platform support for that same task; duplicating the task or bypassing permissions is not a valid workaround. Making GPT-6/maximum actually binding would require a scheduler/backend surface that persists model/reasoning routing fields and returns authenticated runtime telemetry.

# 11. Structured ledger delta

```yaml
ledger_delta:
  source: "Burdzy--Scheutzow, Forward Brownian Motion, Problem 7.2 / I0076"
  metric: "number of the four source-matching obligations proved for one frozen counterexample candidate"
  before: "NOT_SCOREABLE_NO_SURVIVING_FROZEN_CANDIDATE"
  after: "NOT_SCOREABLE_NO_SURVIVING_FROZEN_CANDIDATE"
  status: "OPEN / PARTIAL / RETIRED-HANDOFF"
  unchanged_count: "frozen at mandatory six-run handoff"
  tried_moves: [3, 25, 27]
  remaining_obligation: "For a future reassignment, either construct one frozen process satisfying FBM, BBM, exact arbitrary-random-time seam independence and non-2BM, or prove the implication under the source's complete hypotheses without adding a stopping-time or Brownian-half assumption."
  evidence:
    - "arXiv:1302.6958v4 Definition 2.1 and Problem 7.2"
    - "runs/R15/20260916_2354Z_i0076_sixrun_handoff_phasefield_a20.md"
    - "root QUEUE.md: zero newly certified free READY entries"
  audit_ids: []

retained_screen_delta:
  source: "F0111 retained R15 screen; discrete Convexity Conjecture k=2 mechanism"
  before: "N=12,13 smooth gate used independent K-K roof Ebar_K plus K_sec"
  after: "E_KK <= (eta/2)K_sec; exact t=1 face-slack identity; sharpened gate widehat Gamma_N <= 0"
  status: "PENDING / SELF_CHECK_ONLY / NOT CLAIMED"
  remaining_obligation: "prove widehat Gamma_N>0 on both exact scalar-feasible cells, or derive an equivalent exact convex-dual contradiction"
  evidence:
    - "artifacts/R15/f0111_kenergy_excess_idea_t105b.md @ 93b74815489d2297d3d1ff6e5d3658a6b7148919"
  audit_ids: []
```
