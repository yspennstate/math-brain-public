Model actually ran: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — this is not GPT-6 at maximum, and I do not claim otherwise. NO MOVEMENT in the active scalar: `KPS-2026-NIELSEN-COR1`, `W_AS: 1 -> 1`; frozen Aldous--Fill I0024 remains `C=1 -> 1`; status `OPEN / PARTIAL`; methods #11 DUALIZE, #19 MAKE IT AN ALGORITHM, #30 ONE SCALE / ONE DIRECTION AT A TIME.**

# R01 — exact binary-divergence reduction for the Nielsen Corollary-1 successor

Date: 2026-09-18 UTC  
Worker: R01  
Lane: CLOSABLE OUTSIDE  
Repository: private `yspennstate/math-open-problems`, branch `master`

## 1. Continuity and source recovery

I recovered the current campaign state before doing mathematics: `probability_campaign_2026_09/INDEX.md`, `RANKING.md`, root `POSTED.md`, `RESULTS.md`, `QUEUE.md`, the current follow-up implementation manifest, the newest R01 report, the current R01 successor claim, the neighboring R06 Nielsen-Theorem-4 claim/report, and the currently populated probability-intake directories. I did not reopen settled or exclusively owned neighboring work.

The original R01 source remains David Aldous and James Fill, *Reversible Markov Chains and Random Walks on Graphs*, Open Problem 3.44. The live source still asks whether relaxation time has an exact infimum-over-flows characterization, not merely the known path-congestion upper bound. R01's frozen answer remains

\[
\tau_2=
\inf_{R:\,BR=I_{H_0}}
\sup_{0\ne b\in H_0}
\frac{(Rb)^T C^{-1}(Rb)}{b^T\Pi^{-1}b},
\qquad
R_*=CB^TL^+,
\]

with distortion `C=1`, and the existing independent audits remain

- `R20-AUDIT-R01-I0024-03 = PASS_MATH_SOURCE_FIT`,
- `P26-AUDIT-R01-I0024-AF344-SINGULAR-RIGHT-INVERSE-10 = PASS`.

I0024 is therefore frozen and not attacked again.

The active R01 successor is the exclusive create-only claim

`operations/claims/KPS-2026-NIELSEN-COR1.md`,

from M. Ali Khan, Arthur Paul Pedersen, and Maxwell B. Stinchcombe, *Almost-Uniform Bayesian Convergence to the Truth Is Not Characterized by Countable Additivity on Conditional Hitting Times*, arXiv:2609.20683v1 (submitted 2026-09-17). The source leaves open in general Nielsen's Corollary 1: whether the approximation property plus CHT forces posterior convergence to the truth almost surely.

The frozen scalar is

\[
\Gamma_{\rm AS}
:=\sup_{P,A}P\{\omega:P_n(A)(\omega)\not\to 1_A(\omega)\},
\]

tracked through a certified interval `[L_AS,U_AS]` and width

\[
W_{\rm AS}:=U_{\rm AS}-L_{\rm AS}.
\]

The admission baseline remains

\[
0\le \Gamma_{\rm AS}\le1,
\qquad W_{\rm AS}=1.
\]

No numerical endpoint moved this run.

## 2. Idea written before validation

The previous run showed that approximation turns a finitely additive probability `P` into an ordinary countably additive companion `R` together with a Boolean homomorphism

\[
\Phi:\mathcal B\longrightarrow \mathcal B/\!\sim_R
\]

fixing finite-information clopens, with

\[
P(A)=R(\Phi(A)),
\qquad
P_n(A)=E_R[1_{\Phi(A)}\mid\mathscr F_n].
\]

It also showed that, for every fixed `r>0`, the fixed-error event

\[
F_r(P,A)
:=\left\{\limsup_n |P_n(A)-1_A|>r\right\}
\]

has `P`-mass zero.

The new idea was to stop comparing the companion martingale to the *truth event* `A` at every point and instead separate two possible failure mechanisms:

1. the companion martingale itself fails to approach either binary value `0` or `1`;
2. it approaches a binary value, but that value disagrees with `1_A`.

The second mechanism has a fixed error gap (indeed gap one) and is therefore already killed by the fixed-threshold theorem. This suggests that **all source-level failure mass must equal the finitely additive mass of the first mechanism alone**. That turns the open problem into an exact statement about whether `P` can charge an `R`-null martingale-divergence set whose every positive-amplitude slice is `P`-null.

No code was written before this reduction was proved.

## 3. Setup from the previous structural reduction

Let

\[
\Omega=\{0,1\}^{\mathbb N},\qquad
\mathcal F_n=\sigma(\text{length-}n\text{ cylinders}),
\]

and let `P` satisfy the source positivity assumption, approximation property, and CHT. Let `R` and `Phi` be the companion probability and measure-algebra homomorphism from the previous R01 report.

For a measure-algebra element `b in ran(Phi)`, choose any Borel representative `B` and define

\[
M_n^b(\omega)
:=E_R[1_B\mid\mathcal F_n](\omega).
\]

This is independent of the representative **pointwise**, not merely `R`-a.e.: if `B` and `B'` differ by an `R`-null set, then every finite cylinder has positive `R`-mass and the integrals of `1_B` and `1_{B'}` on every cylinder agree, so the finite-partition conditional expectations agree on every cylinder.

For every `A` with `Phi(A)=b`,

\[
P_n(A)=M_n^b
\]

pointwise. By ordinary countably additive martingale convergence under `R`,

\[
M_n^b\longrightarrow 1_B
\qquad R\text{-a.s.}
\]

## 4. Method #11 — DUALIZE: an exact binary-divergence formula

Define the binary-divergence amplitude

\[
\eta_b(\omega)
:=
\min\left\{
\limsup_{n\to\infty}M_n^b(\omega),
\;1-\liminf_{n\to\infty}M_n^b(\omega)
\right\}.
\]

Because `0<=M_n^b<=1`,

\[
\eta_b(\omega)>0
\]

if and only if the sequence `M_n^b(omega)` fails to converge to one of the two binary values `0` or `1`. Put

\[
D_b:=\{\eta_b>0\}.
\]

Since the ordinary martingale converges to `1_B` `R`-almost surely,

\[
R(D_b)=0.
\]

The key point is that `P(D_b)` need not be zero merely from `R(D_b)=0`, because `P` can charge `R`-null Borel sets through the non-normal Boolean homomorphism `Phi`.

### Theorem 4.1 (exact failure-mass identity)

For every source-admissible `P` having approximation and CHT, every Borel event `A`, and

\[
b=\Phi(A),
\]

one has

\[
\boxed{
P\{P_n(A)\not\to1_A\}=P(D_b).
}
\]

Equivalently, the only source-level almost-sure failure mass is the `P`-mass of the set on which the companion martingale fails to approach either binary value.

#### Proof

Let

\[
F(P,A):=\{P_n(A)\not\to1_A\}.
\]

If `omega in D_b`, then `M_n^b(omega)=P_n(A)(omega)` does not converge to either `0` or `1`. Since `1_A(omega)` is binary,

\[
D_b\subseteq F(P,A).
\]

Now take `omega notin D_b`. By the definition of `eta_b`, the bounded sequence `M_n^b(omega)` converges to a value

\[
\ell(\omega)\in\{0,1\}.
\]

If `omega` is nevertheless in `F(P,A)`, then necessarily

\[
\ell(\omega)\ne1_A(\omega).
\]

Hence

\[
|P_n(A)(\omega)-1_A(\omega)|\longrightarrow1.
\]

In particular

\[
F(P,A)\setminus D_b\subseteq F_{1/2}(P,A).
\]

The fixed-threshold theorem from the previous R01 run gives

\[
P(F_{1/2}(P,A))=0.
\]

Therefore

\[
P(F(P,A)\setminus D_b)=0.
\]

Because `D_b subset F(P,A)` and the decomposition is disjoint, finite additivity is enough:

\[
P(F(P,A))
=P(D_b)+P(F(P,A)\setminus D_b)
=P(D_b).
\]

This proves the identity. QED.

### Corollary 4.2 (exact operator formulation of the source question)

For fixed `P`, define

\[
\Gamma_{\rm AS}(P)
:=\sup_A P(F(P,A)).
\]

Then

\[
\boxed{
\Gamma_{\rm AS}(P)
=
\sup_{b\in\operatorname{ran}\Phi}P(D_b)
=
\sup_{b\in\operatorname{ran}\Phi}R(\Phi(D_b)).
}
\]

and globally

\[
\Gamma_{\rm AS}
=
\sup_P\sup_{b\in\operatorname{ran}\Phi}R(\Phi(D_b)).
\]

Thus Nielsen's Corollary 1 is exactly equivalent to the following continuity statement:

> Every approximation+CHT homomorphism `Phi` must annihilate, after applying `Phi`, the `R`-null binary-divergence set `D_b` of every range martingale `b`.

This is sharper than saying merely that a counterexample would exploit failure of countable additivity: it identifies the exact `R`-null set whose non-normal image would carry every bit of failure mass.

## 5. Method #30 — ONE SCALE AT A TIME: every positive-amplitude slice is null

For `r>0`, define

\[
D_b(r):=\{\eta_b>r\}.
\]

### Proposition 5.1 (all fixed positive amplitude is killed)

For every `r>0`, every `A` with `Phi(A)=b`,

\[
\boxed{P(D_b(r))=0.}
\]

#### Proof

If `eta_b>r`, then simultaneously

\[
\limsup_n M_n^b>r,
\qquad
1-\liminf_n M_n^b>r.
\]

If `1_A=0`, then

\[
\limsup_n|P_n(A)-1_A|
=\limsup_n M_n^b>r.
\]

If `1_A=1`, then

\[
\limsup_n|P_n(A)-1_A|
=1-\liminf_n M_n^b>r.
\]

Thus

\[
D_b(r)\subseteq F_r(P,A).
\]

The previous fixed-threshold theorem gives `P(F_r(P,A))=0`, so monotonicity gives `P(D_b(r))=0`. QED.

But

\[
D_b=\bigcup_{m\ge1}D_b(1/m).
\]

Therefore a counterexample is forced into the pure diagonal pattern

\[
P(D_b)>0,
\qquad
P(D_b(1/m))=0\quad\forall m.
\]

This is a stronger localization than the previous report's generic fixed-error statement: it is now expressed entirely in terms of the companion martingale, independently of the truth mismatch.

### Corollary 5.2 (fixed-gap constructions cannot work)

If for a given `b` there is some `rho>0` such that

\[
\eta_b(\omega)>0\implies\eta_b(\omega)\ge\rho,
\]

then

\[
P(D_b)=0.
\]

Indeed, `D_b subset D_b(rho/2)`. Hence no counterexample can come from a posterior architecture whose nonbinary divergence has a uniform positive amplitude.

In particular, any finite-amplitude or finitely quantized candidate in which positive divergence amplitudes are bounded away from zero is ruled out. A genuine counterexample must contain **infinitely many positive oscillation scales accumulating at zero**, and finite additivity must charge their union while annihilating each fixed positive-amplitude cut.

This is the exact obstruction a construction must now engineer.

## 6. Method #19 — MAKE IT AN ALGORITHM: constructive test for candidates

The reduction gives a concrete design-and-falsification procedure for future candidate constructions.

A proposed counterexample can be organized as the following finite-description obligations, even though the final object is infinite:

1. Specify a countably additive companion `R` on Cantor space and a Boolean homomorphism
   \[
   \Phi:\mathcal B\to\mathcal B/\!\sim_R
   \]
   fixing every finite-information clopen.
2. Define
   \[
   P(E):=R(\Phi(E))
   \]
   and verify the source positivity condition.
3. Verify CHT in the already-derived operator form: every range-generated posterior first-hitting open is fixed by `Phi` modulo `R`.
4. Choose `b in ran(Phi)` and compute the finite-information martingale `M_n^b`.
5. Compute its binary-divergence amplitude `eta_b` and set `D_b={eta_b>0}`.
6. Check the mandatory scale condition
   \[
   R(\Phi(D_b(r)))=0\quad\text{for every }r>0.
   \]
   Any fixed-gap violation kills the candidate immediately.
7. The construction refutes Corollary 1 **if and only if**
   \[
   R(\Phi(D_b))>0.
   \]

Theorem 4.1 then gives the exact posterior failure mass, with no additional truth-event analysis.

This suggests the next constructive architecture much more specifically than the previous hierarchical-ultrafilter sketch: use countably many divergence bands whose amplitudes `rho_k` decrease to zero, arrange each fixed positive cut to miss an ultrafilter-large tail, but arrange the full union of bands to have positive finitely additive mass. The difficult constraint is coherence with CHT: the same homomorphism must fix every range-generated first-hitting open. I do **not** claim such a construction exists yet.

## 7. Failed stronger route this run

I tried to close the source by showing that CHT makes the kernel of `Phi` a sigma-ideal on the particular increasing family

\[
D_b(1)\subseteq D_b(1/2)\subseteq D_b(1/3)\subseteq\cdots,
\qquad
\bigcup_m D_b(1/m)=D_b.
\]

That would immediately imply `P(D_b)=0` and prove Corollary 1.

The route does not currently close. CHT supplies continuity from below only for the special first-hitting unions generated by posterior threshold events. The sets `D_b(1/m)` are tail limsup/liminf events; passing from fixed threshold to the union over shrinking thresholds is exactly the missing diagonal continuity. I found no valid identity representing `D_b` itself as one source-authorized CHT hitting union. Claiming sigma-continuity here would simply reinsert the countable-additivity step that the source problem is testing.

So the exact remaining obligation is now:

\[
\boxed{
\text{Does CHT force }R(\Phi(D_b))=0
\text{ for every }b\in\operatorname{ran}\Phi,
\text{ or can one build a coherent }\Phi
\text{ with }R(\Phi(D_b))>0?
}
\]

## 8. Current literature / prior-art check — 2026-09-18

I refreshed the original and current sources rather than relying on the prior run's search.

- Aldous--Fill's live Open Problem 3.44 page still asks for an exact infimum-over-flows characterization of relaxation time and distinguishes it from the Chapter-4 upper bound.
- Khan--Pedersen--Stinchcombe arXiv:2609.20683v1 is dated 2026-09-17. Its abstract explicitly says their counterexample does not refute Nielsen's corollary, that they establish the corollary for a family including their counterexample, and leave it open in general. No later source-matching resolution appeared in the bounded exact-title / exact-arXiv-ID / Corollary-1 searches on 2026-09-18. Because the source is about one day old, this is bounded negative evidence, not a novelty certificate.
- Klaus D. Schmidt, *The Andersen--Jessen theorem revisited*, Math. Proc. Cambridge Philos. Soc. 102 (1987), 351--361, is important nearby prior art. Its accessible abstract says Andersen--Jessen almost-sure convergence has extensions to processes induced by finitely additive set functions and relates them to conditional expectations and positive supermartingales. I could access the abstract/metadata but did **not** establish from the available text that its hypotheses imply the source's `P`-almost-sure convergence to the event truth. In the present reduction ordinary `R`-a.s. martingale convergence is already automatic; the unresolved issue is whether finitely additive `P` can charge the `R`-null divergence set. I therefore record Schmidt as a must-read neighboring theorem, not as a resolution.
- Morenikeji Neri, *The pointwise ergodic theorem on finitely additive spaces*, arXiv:2511.01676, explicitly notes failure of ordinary almost-sure convergence in general finitely additive settings and introduces a finite-almost-sure replacement. This is contextual support for treating the diagonal null-union obstruction seriously, not a direct solution of the Bayesian CHT question.

Search/access limitation: I did not obtain full paywalled theorem statements/proofs for Schmidt's 1987 paper during this run, so no claim depending on those inaccessible hypotheses is made.

## 9. Neighboring work and audit budget

R06 owns the distinct `KPS-2026-NIELSEN-THEOREM4` question. Its newest report proves useful structural lemmas for that separate target, including open-set clopen-approximation under CHT, but its package is not a completed source-level closure requiring R01 as the second independent auditor. I therefore spent no audit budget and did not modify R06 files.

No exact-arithmetic checker was created this run. The new claims are analytic identities proved on the page and have no finite computational core. Creating a decorative checker would violate the 90/10 rule.

## 10. Metric and status

Active successor metric:

\[
W_{\rm AS}:1\longrightarrow1.
\]

So there is **no scalar movement** this run. The gain is structural: the entire failure mass has been reduced exactly to one canonical `R`-null binary-divergence set, and all fixed positive-amplitude slices of that set are now ruled out.

Local unchanged count on the successor metric: **2** counting the admission run's `1 -> 1` and this run's `1 -> 1`. If the shared fleet ledger uses a different canonical counting convention, that count should be reconciled there rather than retroactively editing this immutable report.

Honest status: **OPEN / PARTIAL**. Nothing here proves or refutes Nielsen's Corollary 1.

## 11. Next nonrepeating methods

The next R01 run should not repeat `#11/#19/#30`. The best next triple is:

- **#6 DEFORM TO A POINT YOU CAN SOLVE:** build a scale-indexed family where the positive divergence amplitudes are `rho_k -> 0`, first in a deliberately CHT-free model, then identify the exact coherence equation needed to restore CHT.
- **#17 LOOK FOR YOUR NUMBERS SOMEWHERE ELSE:** inspect finitely additive martingale / amart / Andersen--Jessen literature for a theorem whose exceptional-set notion exactly controls `P(D_b)` rather than only `R(D_b)`.
- **#22 READ THE FAILURES, NOT THE SUCCESSES:** extract the hypotheses and failure modes in the finitely additive martingale convergence literature and compare them term-by-term to approximation+CHT.

The immediate mathematical choice is **constructive counterexample first**: engineer the necessary vanishing-amplitude diagonal architecture and let CHT be the falsification test.

## 12. Model/scheduler control boundary

The currently documented scheduler surface still exposes no binding model-family selector, no reasoning-effort selector, no authenticated applied-model receipt, and no guaranteed hour-long execution control. `GPT-6 / maximum` therefore remains prompt text, not an enforceable runtime setting on this surface. Enforcing it requires an owner-authorized product/backend/admin surface that exposes and attests those controls.

The recorded P26 `You cannot modify this task` failure remains an authorization-context boundary. Repository configuration history records later success from an authorized context; the lawful workaround is therefore the owning/authorized context or platform support, not duplication or permission bypass. No scheduler or permission change was attempted in this run.

## 13. Structured ledger delta

```yaml
ledger_delta:
  worker: R01
  frozen_original:
    source: "Aldous--Fill Open Problem 3.44 / I0024"
    metric: "uniform multiplicative distortion C"
    before: 1
    after: 1
    status: "PROVED / FROZEN"
    audit_ids:
      - "R20-AUDIT-R01-I0024-03"
      - "P26-AUDIT-R01-I0024-AF344-SINGULAR-RIGHT-INVERSE-10"
  active_source:
    id: "KPS-2026-NIELSEN-COR1"
    source: "Khan--Pedersen--Stinchcombe, arXiv:2609.20683v1, Nielsen Corollary 1 question"
    ownership: "exclusive R01 claim"
  metric:
    name: "W_AS = U_AS - L_AS for Gamma_AS"
    before: 1
    after: 1
    movement: "NO MOVEMENT"
    unchanged_count_local: 2
  status: "OPEN / PARTIAL"
  tried_moves: [11, 19, 30]
  new_results:
    - "Exact identity P{P_n(A) not -> 1_A} = P(D_{Phi(A)}), where D_b is the binary-divergence set of the companion R-martingale."
    - "For every r>0, P(D_b(r))=0; any counterexample must have positive mass only through amplitudes accumulating at zero."
    - "Exact operator target: Corollary 1 iff R(Phi(D_b))=0 for every range element b of every approximation+CHT homomorphism."
    - "Fixed-gap / finite-amplitude divergence architectures cannot refute the source."
  remaining_obligation: >-
    Prove that CHT forces R(Phi(D_b))=0 for every b in ran(Phi),
    or construct a coherent approximation+CHT Boolean homomorphism with
    R(Phi(D_b))>0 while every fixed positive-amplitude slice D_b(r) has zero mass.
  evidence:
    - "runs/R01/20260918T1623Z_kps_cor1_claim_operator_diagonal_3a71c5e9.md"
    - "operations/claims/KPS-2026-NIELSEN-COR1.md"
    - "this immutable report"
  successor_audits: []
  next_moves: [6, 17, 22]
```
