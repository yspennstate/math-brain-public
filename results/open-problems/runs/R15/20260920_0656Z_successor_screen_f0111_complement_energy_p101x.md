Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — not GPT-6 maximum. NATIVE I0076 METRIC NO MOVEMENT: `NOT_SCOREABLE_NO_SURVIVING_FROZEN_CANDIDATE -> NOT_SCOREABLE_NO_SURVIVING_FROZEN_CANDIDATE`. RETAINED-SCREEN MOVEMENT: for the last `n=30` F0111 `k=2` cells `N=12,13`, I prove an exact complement-energy duality that eliminates the unknown cross block from every coordinate-face test, and combine it with the projective residual Gram representation to obtain a heterogeneity-sensitive coefficient-free feasibility gate. Methods #3 PROVE SOMETHING STRONGER, #11 DUALIZE, #25 COUNT THE SAME THING TWICE.**

# R15 retained screen — complement-energy duality and a heterogeneity-sensitive coefficient elimination

Date checked: 2026-09-20 UTC.  
Repository / branch: private `yspennstate/math-open-problems` / `master`.  
Worker: R15, CLOSABLE OUTSIDE.

Everything about Talagrand/F0111 below remains **PENDING / SELF_CHECK_ONLY / NOT CLAIMED**. This report does not reopen Burdzy--Scheutzow Problem 7.2, does not promote F0111 to READY, does not solve Talagrand's discrete Convexity Conjecture, and does not satisfy the two-other-track audit closure rule.

The immediately preceding complete R15 report used methods `#6/#14/#20`. The R15 history has already exhausted all thirty Section-B move numbers, so the present `#3/#11/#25` triple is a nonconsecutive re-entry on a genuinely new reduced object, not a claim that these numbers have never appeared before.

The research route was written before any validation code in

`artifacts/R15/f0111_complement_energy_idea_p101x.md`

at commit

`64c623c4750bca4a63bfcdc9702980d0aef4d42b`.

No finite numerical claim is introduced in this run, so I did **not** manufacture another checker merely to produce a certificate. The new statements below are theorem-sized analytic identities/inequalities and are proved on the page.

## 1. Whole-repository continuity, source, ownership, exclusions

Before new mathematics I reread or source-recovered:

- `probability_campaign_2026_09/INDEX.md` and `RANKING.md`;
- root `POSTED.md`, `RESULTS.md`, and `QUEUE.md`;
- `operations/FOLLOWUP_IMPLEMENTATION_2026-09-16.md`;
- the controlling I0076 handoff `runs/R15/20260916_2354Z_i0076_sixrun_handoff_phasefield_a20.md`;
- the newest R15 report `runs/R15/20260920_0640Z_successor_screen_f0111_n1213_kexcess_block_o100w.md`;
- the neighboring Burdzy--Scheutzow Problem 7.8 terminal handoff `runs/R07/20260919T093413Z_i0077_random_reroot_periodic_completion_59_handoff_rr59s3.md`;
- current queue/admission state. `QUEUE.md` still distinguishes listed/PENDING candidates from genuinely READY inventory and still records zero newly certified free READY entries. I therefore did not claim another worker's source, promote a PENDING row, or edit a shared root.

### Exact I0076 source rechecked from the primary PDF

Primary source: Krzysztof Burdzy and Michael Scheutzow, *Forward Brownian Motion*, arXiv:1302.6958v4 / PTRF 160 (2014), 95--126.

Definition 2.1 says:

- FBM: there exist random times `S_n -> -infinity` a.s. such that each complete centered future `(X_{S_n+t}-X_{S_n})_{t>=0}` is standard Brownian motion;
- BBM: the time reversed process is FBM;
- 2BM: there is one random time `S` such that the complete centered future and complete centered past at `S` are independent standard Brownian motions.

Problem 7.2 asks whether **FBM + BBM + existence of an arbitrary random time `T` for which the complete centered future and past half-processes are independent** implies 2BM. The source does **not** say that `T` is a stopping time and does **not** separately assume that either half at `T` is Brownian. Problem 7.5 is distinct and remains excluded.

The source's Proposition 6.2 proves a different stronger-seam obstruction for its Section-6 construction: there is no random seam at which the two halves are independent **and the forward half is Brownian**. That does not supply or exclude bare Problem-7.2 independence by itself.

### Native candidate/metric state

The controlling six-run handoff remains binding.

- The source Theorem-6.1 construction has FBM, BBM and failure of 2BM, but R15 eliminated it as a Problem-7.2 counterexample candidate because it has no source-valid independent seam.
- The later Brownian-prefix/BES candidate had FBM, BBM and an exact independent seam, but R15 proved it is actually 2BM.

Thus there is **no surviving frozen counterexample candidate** on which the user's four obligations can honestly be counted. Historical `2/4` and `3/4` diagnostics belong to eliminated candidates or to the later positive-route handoff metric; they are not a current frozen-candidate score.

Native status remains **OPEN / PARTIAL / RETIRED-HANDOFF**. The six-run unchanged count that triggered retirement is frozen at the handoff; it is not incremented by retained-screen work.

### Fresh dated literature pass, 2026-09-20

Queries included exact-title / exact-Problem-7.2 variants, Burdzy--Scheutzow later/citing work, the current Burdzy open-problems page, Talagrand `Problem 10.9`, `k=2`, `quadratic majorant`, the 2026 `k`-threshold reformulation, and Park's September comparison theorem.

For I0076, the searches recovered the primary paper, the current University of Washington publication page, and Burdzy's current open-problem page. The latter still lists a different descendant question about bounded concatenated Brownian pieces becoming 2BM, but I found no accessible later primary source explicitly announcing a solution of exact Problem 7.2. This is **bounded negative evidence only**, not a worldwide openness certificate.

For F0111, Ascoli--He--Park--Talagrand, arXiv:2608.11183 (2026-08-11), explicitly says the broader discrete Convexity Conjecture remains open and reformulates it using `k`-thresholds while proving substantial classes. Park, arXiv:2609.14681 (2026-09-13), gives a dimension-free comparison which its abstract describes as a bound *toward* the conjecture. Searches for the particular quadratic/complement-energy mechanism below found no matching accessible source. Novelty remains **UNVERIFIED**; the argument is elementary enough that it should not be advertised as new without a dedicated prior-art review.

## 2. Carried F0111 state

The retained screen is the cardinality-two hazard

\[
F(t)=\sum_{i=1}^{30}t_i-\log\!\left(\sum_{i=1}^{30}e^{t_i}-29\right).
\tag{2.1}
\]

The preceding exact reductions eliminate the `N=11` and `N=14` full-support two-level Hessian-null branches on the surviving outer scalar branch `z=1+s>1`. Any survivor of this particular first-bifurcation mechanism therefore has

\[
N=|K|\in\{12,13\}.
\tag{2.2}
\]

The previous report also proved, with arbitrary within-block heterogeneity,

\[
N=12:\quad r_*<1-15s,
\qquad
N=13:\quad r_*<1-17s,
\tag{2.3}
\]

and the exact K-excess roofs

\[
\sum_{j\in K}q_j\le \frac{15}{64}\quad(N=12),
\qquad
\sum_{j\in K}q_j\le \frac{439}{2197}\quad(N=13).
\tag{2.4}
\]

It completely eliminated the block-constant subfamily in both cells, but the direct heterogeneous entropy envelope still lost about a small fixed amount near the top of the cells. The stated obstruction was that heterogeneous light-`J` coordinates could route too much `J-J` coefficient energy. The present run attacks exactly that loss rather than changing constants in the old envelope.

Let a hypothetical global nonnegative quadratic certificate be

\[
P(t)=\sum_i A_it_i+\sum_{i<j}B_{ij}t_it_j,
\qquad A_i,B_{ij}\ge0,
\tag{2.5}
\]

with exact value and gradient contact at an interior point `q>0`.

Put

\[
r_i=\frac{e^{q_i}}{S(q)},\qquad
S(q)=\sum_i e^{q_i}-29,
\tag{2.6}
\]

so `partial_i F(q)=1-r_i`.

## 3. Method #25 — count exact contact energy in two different ways

Fix **any** nonempty proper coordinate subset `J` and write `K=J^c`. Define

\[
E_{JJ}=\sum_{i<j\in J}B_{ij}q_iq_j,
\quad
E_{JK}=\sum_{i\in J,j\in K}B_{ij}q_iq_j,
\quad
E_{KK}=\sum_{i<j\in K}B_{ij}q_iq_j,
\tag{3.1}
\]

and

\[
W=E_{JJ}+E_{JK}+E_{KK}.
\tag{3.2}
\]

Also set

\[
D_J=\sum_{i\in J}q_i(1-r_i),
\qquad
A_J^{(q)}=\sum_{i\in J}A_iq_i.
\tag{3.3}
\]

Exact gradient contact, multiplied by `q_i` and summed over `J`, gives

\[
D_J=A_J^{(q)}+2E_{JJ}+E_{JK}.
\tag{3.4}
\]

For the full coordinate set, if

\[
D=\sum_iq_i(1-r_i),
\]

then gradient contact gives `D=A^{(q)}+2W` and value contact gives `F(q)=A^{(q)}+W`. Hence

\[
W=D-F(q).
\tag{3.5}
\]

Using `E_{JK}=W-E_{JJ}-E_{KK}` in (3.4),

\[
\boxed{
A_J^{(q)}=D_J-W-E_{JJ}+E_{KK}.
}
\tag{3.6}
\]

This is the conserved block budget that the preceding entropy estimates did not use.

## 4. Methods #3 and #11 — exact complement-energy theorem

Let `q_J` denote the vector equal to `q` on `J` and zero on `K`. On the ray `tq_J`, multilinearity gives

\[
P(tq_J)=tA_J^{(q)}+t^2E_{JJ}.
\tag{4.1}
\]

Global majorization implies

\[
tA_J^{(q)}+t^2E_{JJ}\ge F(tq_J),\qquad t>0.
\tag{4.2}
\]

Substitute (3.6), divide by `t`, and rearrange.

### Theorem R15-F0111-COMP1 — complement-energy family

For every nonempty proper `J` and every `t>0`, any global nonnegative quadratic certificate with exact interior contact satisfies

\[
\boxed{
E_{KK}+(t-1)E_{JJ}
\ge
W-D_J+\frac{F(tq_J)}t.
}
\tag{4.3}
\]

No symmetry, Hessian-null assumption, or `n=30` specialization is needed for (4.3).

This already has a useful interpretation: global safety on a `J`-face forces a definite amount of pair energy into the **complementary** face. Cross-block energy has disappeared exactly.

Now define

\[
g_J(t)=\frac{F(tq_J)}t,
\qquad
\Phi_J(B)=\sup_{t>0}\{g_J(t)-Bt\}.
\tag{4.4}
\]

The earlier R15 all-ray theorem proves that `g_J` is strictly concave whenever `J` has at least two positive coordinates; for one active coordinate the hazard on that ray is identically zero and the assertion below is trivial.

Taking the supremum in (4.3) gives the exact dual form.

### Theorem R15-F0111-COMP2 — exact dual complement cone

For every such `J`,

\[
\boxed{
E_{KK}
\ge
W-D_J+E_{JJ}+\Phi_J(E_{JJ}).
}
\tag{4.5}
\]

Moreover, (4.5) is equivalent to the entire one-parameter family (4.3).

### Proof

From (4.3),

\[
E_{KK}\ge W-D_J+g_J(t)-(t-1)E_{JJ}
\]

for every `t>0`. The supremum of the last two terms is

\[
\sup_{t>0}\{g_J(t)-tE_{JJ}\}+E_{JJ}
=\Phi_J(E_{JJ})+E_{JJ},
\]

which is (4.5). Conversely, the supremum dominates every individual `t`, so (4.5) implies every inequality (4.3). QED.

This is stronger operationally than checking a few coordinate faces: the unknown cross-block coefficient matrix has been **eliminated exactly**, and every ray of the face has been compressed into one one-dimensional convex-dual term.

## 5. A sharp threshold consequence of strict concavity

Put

\[
B_*:=g_J'(1),
\qquad
C_J(B):=B+\Phi_J(B).
\tag{5.1}
\]

On the nontrivial interior of the dual cone, let `t_B` be the unique point with

\[
g_J'(t_B)=B.
\]

The all-ray theorem gives

\[
\Phi_J'(B)=-t_B,
\qquad
C_J'(B)=1-t_B.
\tag{5.2}
\]

Because `g_J'` decreases strictly,

\[
B<B_*\quad\Longrightarrow\quad t_B>1
\quad\Longrightarrow\quad C_J'(B)<0.
\tag{5.3}
\]

Therefore:

### Corollary R15-F0111-COMP3 — upper-cap amplification

If an independent argument proves

\[
0\le E_{JJ}\le \overline E_J<B_*,
\tag{5.4}
\]

then (4.5) strengthens to

\[
\boxed{
E_{KK}
\ge
W-D_J+C_J(\overline E_J).
}
\tag{5.5}
\]

Indeed `C_J` is decreasing throughout `[0,B_*]`, so `C_J(E_{JJ})>=C_J(\overline E_J)`.

This identifies exactly what is needed from the heterogeneity calculation: not a global entropy bound, but an upper cap on `E_JJ` that lies below the tangent slope `g_J'(1)`.

## 6. The projective residual Gram matrix supplies the missing heterogeneity cap

Return to the remaining full-support two-level Hessian-null cells. Write

\[
h=a\mathbf1_J-b\mathbf1_K,\qquad a=1+\delta,\quad b=1-\delta.
\tag{6.1}
\]

The carried projective fourth-order condition gives a residual PSD Gram matrix with vectors `w_i` satisfying, for `i,j in J`,

\[
B_{ij}=\langle w_i,w_j\rangle+A_Jr_ir_j,
\qquad
\|w_i\|^2=e_i:=r_i(1-A_Jr_i).
\tag{6.2}
\]

The residual null relation is

\[
a\sum_{i\in J}w_i=b\sum_{j\in K}w_j.
\tag{6.3}
\]

Let

\[
T=\left\|\sum_{j\in K}w_j\right\|^2,
\qquad
T\le T_{\rm cap}:=y(N-L_K),
\tag{6.4}
\]

and put

\[
R_J=\sum_{i\in J}r_iq_i,
\qquad
Z_J=\sum_{i\in J}q_iw_i.
\tag{6.5}
\]

Expanding pair sums gives an **exact identity**:

\[
\boxed{
E_{JJ}
=
\frac12\left(\|Z_J\|^2-\sum_{i\in J}e_iq_i^2\right)
+
\frac{A_J}{2}
\left(R_J^2-\sum_{i\in J}r_i^2q_i^2\right).
}
\tag{6.6}
\]

Proof: use

\[
2\sum_{i<j}q_iq_j\langle w_i,w_j\rangle
=\left\|\sum_iq_iw_i\right\|^2-\sum_iq_i^2\|w_i\|^2
\]

and the analogous scalar identity for the rank-one `A_J r_ir_j` term. QED.

Now choose any real `theta`. From (6.3),

\[
Z_J
=
\theta\frac ba\sum_{j\in K}w_j
+
\sum_{i\in J}(q_i-\theta)w_i.
\tag{6.7}
\]

Hence, by the triangle inequality and (6.4),

\[
\|Z_J\|
\le
\frac ba|\theta|\sqrt{T_{\rm cap}}
+
\sum_{i\in J}|q_i-\theta|\sqrt{e_i}.
\tag{6.8}
\]

Substituting into (6.6) proves:

### Theorem R15-F0111-GRAMCAP — heterogeneity-sensitive `J-J` energy cap

Every surviving two-level contact satisfies, for every real `theta`,

\[
\boxed{
\begin{aligned}
E_{JJ}\le G_J(\theta):={}&
\frac12\left[
\left(
\frac ba|\theta|\sqrt{T_{\rm cap}}
+
\sum_{i\in J}|q_i-\theta|\sqrt{r_i(1-A_Jr_i)}
\right)^2
-
\sum_{i\in J}r_i(1-A_Jr_i)q_i^2
\right]\\
&+
\frac{A_J}{2}
\left[
\left(\sum_{i\in J}r_iq_i\right)^2
-
\sum_{i\in J}r_i^2q_i^2
\right].
\end{aligned}
}
\tag{6.9}
\]

Therefore

\[
\boxed{E_{JJ}\le \overline E_J:=\inf_{\theta\in\mathbb R}G_J(\theta).}
\tag{6.10}
\]

This is the heterogeneity penalty missing from the preceding run. It is strong in both regimes which defeated the old crude bound:

- if the `J` coordinates are nearly equal, choose `theta` near their common value and the deviation sum in (6.9) collapses;
- if one `J` mass is heavy, its residual norm `sqrt(r_i(1-A_Jr_i))` is small, so its large `q_i` is strongly discounted rather than multiplied by the full aggregate coefficient mass.

The old estimate `E_JJ<=U q_(1)q_(2)` has neither property.

## 7. Exact coefficient-free gate for the last two scalar cells

The preceding K-excess invariant supplies a scalar upper bound on the complementary energy as well.

Let

\[
\eta_K:=U_K-N=\sum_{j\in K}(e^{q_j}-1).
\tag{7.1}
\]

Since every `q_j>=0`,

\[
q_j\le\log(1+\eta_K).
\tag{7.2}
\]

The aggregate `K-K` coefficient mass is

\[
V=\frac12(T-y+A_Ky^2)
\le
V_{\max}:=\frac12(T_{\rm cap}-y+A_Ky^2).
\tag{7.3}
\]

Hence

\[
\boxed{
E_{KK}\le
\overline E_K:=V_{\max}[\log(1+\eta_K)]^2.
}
\tag{7.4}
\]

Combining Sections 4--7 yields a new exact feasibility reduction.

### Corollary R15-F0111-LASTCELLS — coefficient elimination

For either remaining cell `N=12` or `N=13`, every full-support two-level Hessian-null exact global quadratic contact must satisfy

\[
0\le E_{JJ}\le\overline E_J,
\tag{7.5}
\]

and

\[
\boxed{
W-D_J+C_J(E_{JJ})\le\overline E_K.
}
\tag{7.6}
\]

In particular, if

\[
\overline E_J<B_*=g_J'(1),
\tag{7.7}
\]

then necessarily

\[
\boxed{
W-D_J+C_J(\overline E_J)\le\overline E_K.
}
\tag{7.8}
\]

The pair-coefficient matrix `B=(B_ij)` no longer appears in (7.8). Everything is expressed in the contact masses/coordinates `r_i,q_i`, the two scalar null parameters, one one-dimensional minimization in `theta`, and one one-dimensional Legendre transform `Phi_J`.

This is the main movement of the run. The preceding heterogeneous entropy route failed because it separately upper-bounded `E_JJ` and lower-bounded total entropy; (7.8) instead makes the exact face deficit and the residual Gram geometry talk to each other before any worst-case relaxation is taken.

## 8. What remains and the next attack

This run does **not** eliminate the full `N=12` or `N=13` cells. It replaces the remaining coefficient-matrix feasibility problem by a much smaller contact-distribution problem.

The exact remaining task for this first-bifurcation mechanism is now:

1. maximize the right side allowed by (6.9) over the admissible `J` mass simplex under the carried heavy cap and residual coordinate caps;
2. prove either `\overline E_J<B_*` throughout a cell and violate (7.8), or identify the extremal mass profile where equality is closest;
3. repeat only if needed for the other cell.

A natural choice of `theta` is a weighted median or the dominant `J` coordinate value. The formulas suggest a two-point extremizer: one heavy `J` mass and one aggregate light mass. If that reduction can be proved by convexity/majorization, the last two cells become a two-variable exact problem rather than a high-dimensional graph-flow problem.

This is where the next run should spend its research time. Another scalar Bernstein wall or another generic entropy estimate would ignore the new exact structure.

## 9. Prior-art / status boundary

The broader discrete Convexity Conjecture is still described as open in the August 2026 Ascoli--He--Park--Talagrand paper, and Park's September 2026 comparison result gives a dimension-independent bound toward it. Nothing in this report is claimed to resolve that conjecture. The present theorem concerns only the `k=2`, `n=30`, full-support, two-level Hessian-null first-bifurcation screen, and even there it is a reduction rather than complete elimination of the final two cells.

Publication novelty of COMP1--COMP3 / GRAMCAP is **UNVERIFIED**. The ingredients are elementary exact-contact bookkeeping, one-dimensional Fenchel duality, and Gram geometry, so a dedicated literature check is required before any novelty claim.

## 10. Model / reasoning control and denied-task boundary

Actual report model: **GPT-5.6 Sol**. Actual reasoning level is **UNVERIFIED**; this run is not claimed to be GPT-6 maximum.

The currently exposed scheduler/update surface still has prompt/title, timing/schedule, enabled-state and ordinary update controls, but no binding model-family selector, no reasoning-effort selector, no authenticated applied-model/effort receipt, and no guaranteed hour-long execution control. Thus the text `Model: GPT-6. Reasoning: maximum` remains a request in the prompt, not an enforceable scheduler field on this surface.

The historical P26 scheduler ID returned `You cannot modify this task` from one authorization context. The repository later records successful P26 modification/reconciliation from an authorized P/C context. The compliant workaround for any task that still refuses modification is the owning/authorized workspace/account/API/admin context or platform support; duplicating the task or bypassing permissions is not acceptable.

This worker did not attempt a scheduler mutation because the current operating contract explicitly forbids scheduler changes.

## 11. Structured ledger_delta

```yaml
ledger_delta:
  task: R15
  lane: CLOSABLE_OUTSIDE
  source: "Krzysztof Burdzy and Michael Scheutzow, Forward Brownian Motion, Problem 7.2, I0076"
  source_metric: "number of four source-matching obligations proved for one frozen counterexample candidate"
  metric_before: NOT_SCOREABLE_NO_SURVIVING_FROZEN_CANDIDATE
  metric_after: NOT_SCOREABLE_NO_SURVIVING_FROZEN_CANDIDATE
  metric_movement: NO_MOVEMENT
  source_status: OPEN_PARTIAL_RETIRED_HANDOFF
  native_unchanged_count: "6 at mandatory handoff; frozen after retirement"
  tried_moves: [3, 11, 25]
  remaining_source_obligation: "construct a new source-valid frozen counterexample candidate satisfying FBM, BBM and bare random-time half-process independence while failing 2BM, or prove the full source implication without adding stopping-time/Brownian-seam hypotheses"
  source_candidate: NONE_SURVIVING
  evidence:
    - "runs/R15/20260916_2354Z_i0076_sixrun_handoff_phasefield_a20.md"
    - "runs/R15/20260920_0640Z_successor_screen_f0111_n1213_kexcess_block_o100w.md"
    - "artifacts/R15/f0111_complement_energy_idea_p101x.md @ 64c623c4750bca4a63bfcdc9702980d0aef4d42b"
  retained_screen:
    source: "Talagrand F0111 / discrete Convexity Conjecture, k=2 screen"
    admission: PENDING_SELF_CHECK_ONLY_NOT_CLAIMED
    before: "last n=30 two-level scalar cells N={12,13}; heterogeneous coefficient-energy routing unresolved"
    after: "same two cells, but exact complement-energy duality + heterogeneity-sensitive Gram cap eliminate the coefficient matrix and reduce feasibility to contact-distribution inequalities"
    new_results:
      - R15-F0111-COMP1
      - R15-F0111-COMP2
      - R15-F0111-COMP3
      - R15-F0111-GRAMCAP
      - R15-F0111-LASTCELLS
  independent_audits: []
  closure: false
```

No shared root was edited. No email, Drive, public posting, purchase, permission change, or scheduler change was attempted.
