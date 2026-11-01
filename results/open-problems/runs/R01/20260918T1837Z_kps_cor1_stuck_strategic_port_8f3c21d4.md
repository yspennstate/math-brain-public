Model actually ran: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — this is not GPT-6 at maximum, and I do not claim otherwise. NO MOVEMENT: active `KPS-2026-NIELSEN-COR1` metric `W_AS: 1 -> 1`, local unchanged count `2 -> 3`; frozen Aldous--Fill I0024 remains `C=1`; status `OPEN / PARTIAL / STUCK_THINKING_1`; methods #1 CHANGE THE CATEGORY, #22 READ THE FAILURES, #29 ADD THE POINTS AT INFINITY.**

# R01 — mandatory stuck analysis for Nielsen Corollary 1

Run date: 2026-09-18 UTC  
Repository / branch: private `yspennstate/math-open-problems` / `master`  
Lane: **CLOSABLE OUTSIDE**

## 1. Runtime truth and repository continuity

The prompt requests GPT-6 with maximum reasoning. This invocation actually identifies as **GPT-5.6 Sol**. Authenticated reasoning-effort telemetry is not exposed, so the reasoning level is **UNVERIFIED**. I do not claim GPT-6, maximum reasoning, or a guaranteed hour-long execution.

I recovered the latest R01 state before doing any new work. The newest immutable R01 report is

`runs/R01/20260918T1748Z_kps_cor1_ghost_tower_hierarchy_nogo_6c2f91a8.md`,

whose structured ledger records `W_AS=1 -> 1`, local unchanged count `2`, status `OPEN / PARTIAL`, and methods `[11,19,30]`. I also reread the current campaign `probability_campaign_2026_09/INDEX.md` and `RANKING.md`, root `POSTED.md`, `RESULTS.md`, `QUEUE.md`, `operations/FOLLOWUP_IMPLEMENTATION_2026-09-16.md`, the exclusive claim `operations/claims/KPS-2026-NIELSEN-COR1.md`, the current intake structure under the `probability_1000_intake_*` trees, and the newest same-source neighboring report `runs/R06/20260918T1720Z_nielsen_t4_convexification_nogo_46.md`. R06 owns the distinct Nielsen-Theorem-4 question and does not conflict with R01's Corollary-1 claim.

Because this run leaves the active scalar unchanged for the third consecutive locally recorded run, Section I applies now. Accordingly **this is a thinking-only stuck run**: no new theorem/lemma is asserted below, no checker is manufactured, and no audit is requested. The purpose of the run is to diagnose the exact obstruction and select one genuinely different route.

## 2. Aldous--Fill I0024 remains frozen

The original R01 target remains internally complete at the exact distortion optimum

\[
\tau_2=
\inf_{R:\,BR=I_{H_0}}
\sup_{0\ne b\in H_0}
\frac{(Rb)^TC^{-1}(Rb)}{b^T\Pi^{-1}b},
\qquad
R_*=CB^TL^+,
\]

with `C=1`. The preserved distinct audits remain

- `R20-AUDIT-R01-I0024-03 = PASS_MATH_SOURCE_FIT`,
- `P26-AUDIT-R01-I0024-AF344-SINGULAR-RIGHT-INVERSE-10 = PASS`.

Nothing in this run reopens I0024 or changes its metric.

## 3. Active outside source and metric

R01's active create-only successor claim remains

`operations/claims/KPS-2026-NIELSEN-COR1.md`.

The source is M. Ali Khan, Arthur Paul Pedersen and Maxwell B. Stinchcombe, *Almost-Uniform Bayesian Convergence to the Truth Is Not Characterized by Countable Additivity on Conditional Hitting Times*, arXiv:2609.20683, submitted 17 September 2026. Its Section 10 leaves open in general the unsupported Nielsen Corollary 1 question:

> Do the approximation property and CHT together imply almost-sure convergence of the posteriors to the truth for an arbitrary probability function?

Fresh dated check, **2026-09-18**: exact-title, exact-arXiv-ID, author-plus-Corollary-1, and approximation+CHT+almost-sure searches found the current KPS paper but no later source-matching resolution. The official arXiv presentation still states that the corollary is established only for the authors' family and is left open in general. This is bounded negative search evidence only; it is not a priority claim.

For source-admissible `P,A`, retain

\[
F_A:=\{\omega:P_n(A)(\omega)\not\to\mathbf1_A(\omega)\},
\qquad
\Gamma_{\rm AS}:=\sup_{P,A}P(F_A),
\]

and the certified interval width

\[
W_{\rm AS}:=U_{\rm AS}-L_{\rm AS}.
\]

The rigorous interval is still `[0,1]`, so

\[
\boxed{W_{\rm AS}=1.}
\]

This run has no endpoint movement: `1 -> 1`, and the local unchanged count is now `3`.

## 4. (a) Exact blocking statement

The preceding R01 work reduces the source question to a single localized null-transfer problem. If `R` is the countably additive companion, `Phi` is the approximation-induced Boolean homomorphism fixing clopens, `b=Phi(A)` is represented by a Borel event `B`, and

\[
M_n^b=E_R[\mathbf1_B\mid\mathscr F_n],
\]

define its binary-divergence set

\[
D_b:=\left\{\min\left(\limsup_n M_n^b,\,1-\liminf_n M_n^b\right)>0\right\}.
\]

Ordinary martingale convergence gives `R(D_b)=0`, while the previous R01 exact reduction gives source failure mass `P(F_A)=R(Phi(D_b))`. The blocker is therefore

\[
\boxed{
R(D_b)=0
\quad\stackrel{?}{\Longrightarrow}\quad
R\!\left(\Phi(D_b)\right)=0
\qquad\text{for every }b\in\operatorname{ran}\Phi.
}
\tag{4.1}
\]

For every fixed `r>0`, the positive-amplitude slice

\[
D_b(r):=\left\{\min\left(\limsup_n M_n^b,\,1-\liminf_n M_n^b\right)>r\right\}
\]

is already known to satisfy `R(Phi(D_b(r)))=0`. But

\[
D_b=\bigcup_{m\ge1}D_b(1/m),
\]

and the source assumptions have not supplied the needed countable-null-union continuity. CHT controls one posterior threshold / first-hitting union at a time. The missing bridge is from those one-threshold controls to the shrinking-threshold diagonal union above.

## 5. (b) Routes already tried and the precise reason each failed

### Route 1 — attack the source with the KPS one-ultrafilter architecture

This does not refute the corollary. The source itself proves almost-sure convergence inside the family containing its main counterexample. The same atom protection that makes CHT work also controls the distinguished paths strongly enough to recover almost-sure learning. Thus the most obvious counterexample architecture points the wrong way for Corollary 1.

### Route 2 — approximation -> companion measure + Boolean homomorphism

The earlier R01 operator reduction is useful but not self-closing. Approximation yields a countably additive companion `R` and a Boolean homomorphism

\[
\Phi:\mathcal B\to\mathcal B/\!\sim_R
\]

fixing finite-information clopens, with

\[
P(A)=R(\Phi(A)),
\qquad
P_n(A)=E_R[1_{\Phi(A)}\mid\mathscr F_n].
\]

This moves the pathology into non-normality of `Phi`, but Booleanity gives only finite union/intersection control. The desired implication (4.1) is precisely a restricted sequential-continuity statement, which does not follow from Booleanity alone.

### Route 3 — fixed-threshold quantifier estimates

For every `r>0`, earlier R01 work recovered/proved the valid fixed-threshold conclusion

\[
P\{\limsup_n|P_n(A)-1_A|>r\}=0.
\]

This kills every fixed positive error scale. It does not kill the countable union over scales tending to zero. Replacing the union by a finite union would prove only the wrong quantifier order.

### Route 4 — binary-divergence duality

The exact identity

\[
P\{P_n(A)\not\to1_A\}=P(D_{\Phi(A)})
\]

removes the truth-mismatch distraction and localizes all possible failure mass on one canonical `R`-null martingale divergence set. It does not say that `Phi` kills that null set.

### Route 5 — positive-mass ghost tower

If a counterexample has failure mass `gamma>0`, the previous report constructs a decreasing tower

\[
G_1\supseteq G_2\supseteq\cdots,
\qquad
\bigcap_mG_m=\varnothing,
\qquad
P(G_m)=\gamma,
\qquad
\Phi(G_m)=\Phi(F)
\]

in the `R`-measure algebra. This is an exact obstruction, not a contradiction: a non-normal Boolean homomorphism can preserve every finite stage of a descending tower while failing at the countable intersection.

### Route 6 — countable atom-protected ultrafilter hierarchies

The preceding R01 run generalized the one-level KPS geometry to an arbitrary countable hierarchy of protected centers. CHT forces an inter-level coherence law, and the positive companion atoms make the ordinary martingale exceptional set `P`-null. Hence this natural recursive counterexample mechanism cannot work. Removing the protecting atoms in the source's one-limit-point geometry breaks CHT instead.

### Route 7 — convexification / fractional free charges

The newest neighboring R06 work, on the distinct Nielsen-Theorem-4 target, shows why averaging valid ultrafilter constructions is not an escape hatch: CHT is nonconvex in the relevant one-limit-point architecture, and a non-two-valued free charge creates an explicit CHT defect. This is not an R01 theorem or audit, but it eliminates a tempting construction direction for the shared source family.

### Route 8 — force global sigma-ideal / sigma-continuity of the kernel

If one simply assumes that the `Phi`-kernel is a sigma-ideal, or that `Phi` is order-continuous on all increasing/decreasing sequences, (4.1) is immediate. But that assumption is exactly the kind of countable continuity that arbitrary finite additivity lacks. It would insert the missing conclusion rather than derive it from approximation + CHT.

### Route 9 — fixed-gap or finitely quantized oscillation architectures

Earlier R01 work showed that every fixed positive oscillation amplitude is null. Therefore any construction in which nonconvergence has a uniform positive gap, or only finitely many positive amplitudes, cannot produce a source counterexample. A counterexample must have infinitely many scales accumulating at zero.

## 6. (c) What a successful proof or refutation must contain that no tried route contains

A **positive** solution does not need full countable additivity of `P` or global normality of `Phi`. It needs a genuinely localized sequential-continuity mechanism strong enough to prove (4.1) for the special martingale-divergence sets `D_b`. Equivalently, it must turn the family of one-threshold CHT identities into control of an **infinite sequence of shrinking thresholds / alternating crossings**. No current route contains that bootstrap.

A **negative** solution needs the opposite object: a coherent non-normal homomorphism `Phi` that

1. fixes every finite-information clopen;
2. satisfies the source approximation property;
3. fixes, modulo `R`, every range-generated posterior first-hitting open required by CHT;
4. nevertheless maps some canonical `R`-null martingale divergence set `D_b` to positive `R`-mass.

The existing ultrafilter constructions fail item 3 when atom protection is removed, and item 4 when enough atom protection is added. The missing ingredient is therefore not merely a more complicated ultrafilter: it is **coherence of non-normality with all CHT hitting opens while retaining a diagonal null-union defect**.

## 7. (d) Simplest special case still unproved

The simplest current special case I do not know how to settle is the fully diffuse companion case.

Let `R=Q` be fair-coin measure on Cantor space, and let `Phi` be a source-admissible approximation-induced Boolean homomorphism fixing every clopen and satisfying the exact CHT fixed-point identities for all events and thresholds. For one `b in ran(Phi)`, with `B` a representative and

\[
M_n^b=E_Q[1_B\mid\mathscr F_n],
\qquad
D_b=\{M_n^b\text{ fails to approach }0\text{ or }1\},
\]

the unresolved special case is

\[
\boxed{
Q(D_b)=0
\quad\stackrel{?}{\Longrightarrow}\quad
Q(\Phi(D_b))=0.
}
\tag{7.1}
\]

This removes all companion atoms and all countable protected-center bookkeeping. A proof of (7.1) would not by itself settle the full source, but it would isolate whether atomic support is essential to any counterexample. A counterexample to (7.1), if source-admissible, would immediately identify the genuinely diffuse obstruction that current constructions lack.

## 8. (e) Nearest solved literature problem and the missing input

The closest general convergence result I found to port is Roger A. Purves and William D. Sudderth, **“Some Finitely Additive Probability,” Annals of Probability 4 (1976), 259--276**, DOI `10.1214/aop/1176996133`.

Their setting is not arbitrary finite additivity. It grows from the Dubins--Savage / strategic-product framework and supplies enough regularity that Borel events can be squeezed between open and closed sets in the usual measure-theoretic manner; with that extension machinery, classical limit theorems including martingale convergence can be recovered in the finitely additive setting. The point relevant here is the **extra sequential/product regularity**. R01 currently has only:

- clopen approximation encoded by `Phi`, and
- CHT continuity on a highly special family of posterior first-hitting opens.

It does **not** yet have the strategic/product regularity or open/closed squeezing principle needed to transfer `R`-null martingale exceptional sets through `Phi`.

A modern corroborating comparison is Morenikeji Neri, **“The pointwise ergodic theorem on finitely additive spaces,” Ergodic Theory and Dynamical Systems (online 10 July 2026), DOI `10.1017/etds.2026.10322`**. Neri emphasizes that ordinary almost-sure ergodic convergence, the strong law, and martingale convergence can fail under arbitrary finite additivity; his replacement uses finite almost-sure / fluctuation / metastability notions. The paper also recalls an older recovery theorem whose extra hypothesis includes precisely a countable-null-union property on the relevant invariant sigma-algebra. That is structurally the same kind of ingredient missing in (4.1): fixed-scale nullity is not enough without a mechanism controlling the countable union.

Source-internal nearest solved special case: KPS Proposition 6.7 proves the Corollary-1 conclusion inside the authors' one-ultrafilter construction. Its proof has a special resource the unrestricted source does not: atom-protected distinguished paths and a two-valued ultrafilter dichotomy that gives pointwise shell control. The previous R01 hierarchy theorem shows that merely repeating that resource countably many times still cannot generate a counterexample.

### Literature query log (2026-09-18)

Fresh bounded queries included:

- exact arXiv ID `2609.20683` + `Corollary 1`;
- Khan / Pedersen / Stinchcombe + Nielsen + Corollary 1;
- `approximation property` + CHT + `almost sure` + finitely additive;
- exact title / citation search for Purves--Sudderth (1976);
- Purves--Sudderth + strategic measures + martingale convergence;
- Neri + pointwise ergodic theorem + finitely additive + null unions.

The KPS question remains presented as open in the current source. The Purves--Sudderth full Project Euclid page was not machine-readable through the available public fetch path during this run; its journal metadata and abstract-level description were recoverable through public indexing. Therefore I do **not** claim to have imported a specific numbered Purves--Sudderth lemma yet. That exact proof/hypothesis recovery is the next route, not a completed result of this run.

## 9. Section-B thinking moves used this run

### #1 CHANGE THE CATEGORY

I recast the obstruction from finitely additive probability into the category of Boolean algebras / measure algebras. In the already-proved normal form, `Phi` is a Boolean homomorphism but need not preserve countable joins. Stone-duality language makes the ghost tower concrete: a nonprincipal Stone point can lie in every member of a decreasing finite-intersection family even when the ordinary set-theoretic intersection is empty. CHT constrains a special collection of opens generated by posterior hitting events. This viewpoint clarifies the target but by itself supplies no reason that those CHT opens exclude all ghost Stone points.

Outcome: **useful reformulation, no metric movement, no new theorem claimed.**

### #22 READ THE FAILURES

The historical and modern finitely-additive convergence literature points to the same failure mode as the current R01 obstruction: finite/additive control of each scale survives, but ordinary almost-sure convergence requires some additional sequential regularity. Purves--Sudderth obtain martingale-type limit theorems in a strategic/product setting with Borel regularization; Neri obtains finite-a.s./metastable control under arbitrary finite additivity and explicitly highlights the missing null-union issue for classical a.s. conclusions.

Outcome: **identified a plausible external proof mechanism to port, but its exact hypotheses have not yet been matched to approximation+CHT.**

### #29 ADD THE POINTS AT INFINITY

The ghost tower suggests looking not only at Cantor space but at the Stone compactification of its full Borel Boolean algebra. The obstruction is then carried by boundary ultrafilters that respect every finite stage but not the countable limit. A positive proof would have to show that CHT keeps all `P`-mass away from the particular boundary fibers supporting martingale-divergence towers; a negative proof would deliberately put positive mass there while preserving every CHT hitting-open constraint.

Outcome: **sharpens what the boundary object must do; neither exclusion nor construction is presently proved.**

## 10. Exactly one action selected under Section I

I choose exactly one of the permitted stuck-task actions:

**PORT THE TECHNIQUE FROM THE NEAREST SOLVED PROBLEM.**

The next R01 research pass should port the Purves--Sudderth strategic/Borel-regularization mechanism to the **localized dynamic Boolean algebra generated by one range event `b`, finite-information clopens, and its CHT hitting opens**. Concretely, the route is to recover the exact martingale-convergence hypotheses/proof from Purves--Sudderth, isolate the minimal sequential regularity actually used to annihilate the martingale exceptional set, and test whether approximation+CHT forces that property on this localized algebra. The diffuse fair-coin special case (7.1) is the first testbed for the port.

This is one route, not three simultaneous obligations. If the strategic regularity cannot be derived, the precise failed implication becomes the design specification for a counterexample.

## 11. Next nonrepeating Section-B moves

For the next invocation, if this same target remains active, use a nonrepeating triple:

- **#3 PROVE SOMETHING STRONGER** — seek a localized strategic-regularity theorem on the dynamic algebra, strong enough to imply (4.1) but weaker than global normality of `Phi`;
- **#17 LOOK FOR YOUR NUMBERS SOMEWHERE ELSE** — compare crossing/fluctuation or metastability bounds for martingales with the `D_b(1/m)` scale structure and identify whether a quantitative tail can replace the missing countable union;
- **#26 HUNT THE SPORADIC CASE** — stress-test the port first on the diffuse fair-coin companion and on low-complexity range events where the exceptional set can be described explicitly.

Do not repeat `[11,19,30]` or `[1,22,29]` on the immediately following run.

## 12. Validation and audit budget

No exact finite claim was created, so no exact-arithmetic checker is appropriate. This is intentionally not another checker-only run.

No neighboring package is presently both complete and in need of R01 as its second independent audit. R06's Nielsen-Theorem-4 work remains a distinct OPEN/PARTIAL target, so no audit was spent there.

## 13. Model / scheduler control truth

The scheduler-control limitation remains unchanged. The exposed task interface has prompt/title, timing/schedule and enabled-state controls but no binding model-family selector, no reasoning-effort selector, no authenticated applied-model receipt, and no guaranteed hour-long runtime setting. GPT-6 / maximum can therefore be requested in prompt text but cannot be enforced or attested from this surface.

To change that requires an owner-authorized product/backend/admin surface that exposes **both** a model-family field and a reasoning-effort field and returns authenticated per-run application metadata. The historical P26 `You cannot modify this task` response was authorization-context-specific: current repository configuration evidence records that another authorized context later succeeded in updating P26. The legitimate workaround is the owning/authorized context or platform support, not duplication, permission bypass, or a replacement task. Per the governing owner addendum, **no scheduler change was attempted in this run**.

## 14. Structured ledger delta

```yaml
ledger_delta:
  worker: R01
  original_source:
    id: I0024
    source: "Aldous--Fill Open Problem 3.44"
    metric: "uniform multiplicative distortion C"
    before: 1
    after: 1
    status: "FROZEN / INTERNAL CLOSURE COMPLETE"
    audits:
      - R20-AUDIT-R01-I0024-03
      - P26-AUDIT-R01-I0024-AF344-SINGULAR-RIGHT-INVERSE-10
  active_source:
    id: KPS-2026-NIELSEN-COR1
    source_url: "https://arxiv.org/abs/2609.20683"
    source_scope: "Khan--Pedersen--Stinchcombe Section 10 / Nielsen Corollary 1: approximation + CHT => eventwise almost-sure posterior convergence for arbitrary probability functions"
    ownership: "R01 exclusive; operations/claims/KPS-2026-NIELSEN-COR1.md"
  metric:
    name: "W_AS = U_AS - L_AS for Gamma_AS = sup_{P,A} P(nonconvergence event)"
    before: 1
    after: 1
    movement: "NO MOVEMENT"
    unchanged_count_before: 2
    unchanged_count_after: 3
  status: "OPEN / PARTIAL / STUCK_THINKING_1"
  tried_moves: [1, 22, 29]
  stuck_blocker: "For b in ran(Phi), prove or refute R(D_b)=0 => R(Phi(D_b))=0, where D_b is the companion martingale's binary-divergence set."
  simplest_unproved_special_case: "Diffuse companion R=fair-coin Q, one range event b, source-admissible Phi satisfying approximation and CHT."
  selected_section_I_action: "PORT_TECHNIQUE_FROM_NEAREST_SOLVED_PROBLEM"
  selected_port: "Purves--Sudderth strategic/Borel regularization -> localized CHT dynamic algebra"
  next_moves: [3, 17, 26]
  remaining_obligation: "Derive localized sequential/null-union continuity for D_b from approximation+CHT, or construct a coherent non-normal Phi preserving all CHT hitting opens while giving positive mass to D_b."
  evidence:
    - "runs/R01/20260918T1748Z_kps_cor1_ghost_tower_hierarchy_nogo_6c2f91a8.md"
    - "runs/R01/20260918T1700Z_kps_cor1_binary_divergence_duality_6f2a91c8.md"
    - "operations/claims/KPS-2026-NIELSEN-COR1.md"
    - "runs/R06/20260918T1720Z_nielsen_t4_convexification_nogo_46.md"
    - "Khan--Pedersen--Stinchcombe arXiv:2609.20683 current source check 2026-09-18"
    - "Purves--Sudderth, Ann. Probab. 4 (1976), 259--276, DOI 10.1214/aop/1176996133"
    - "Neri, ETDS 2026, DOI 10.1017/etds.2026.10322"
  audit_ids: []
  checker: "NONE — mandatory thinking-only stuck run; no finite claim"
```
