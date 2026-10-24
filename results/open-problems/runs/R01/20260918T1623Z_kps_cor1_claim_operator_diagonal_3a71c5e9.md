Model actually ran: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — not GPT-6 at maximum. I0024 remains frozen at `C=1`; R01 successor admission MOVED `PENDING_ADMISSION / UNMEASURED -> CLAIMED KPS-2026-NIELSEN-COR1 / W_AS=1`; within the new source metric `W_AS: 1 -> 1`; methods #8, #15, #27.**

# R01 — new CLOSABLE successor: Nielsen Corollary 1 after Khan–Pedersen–Stinchcombe

Run date: 2026-09-18 UTC  
Repository / branch: private `yspennstate/math-open-problems` / `master`  
Lane: **CLOSABLE OUTSIDE**

## 1. Runtime/control truth and continuity

The prompt requests GPT-6 with maximum reasoning. This invocation actually identifies as **GPT-5.6 Sol**. Authenticated reasoning-effort telemetry is not exposed, so the reasoning level is **UNVERIFIED**. I do not claim GPT-6, maximum reasoning, a binding scheduler model setting, or a guaranteed hour-long execution.

The exposed task-control surface continues to provide task identity/prompt/title, schedule or relative-start controls, timing mode and enabled state, but no bindable model-family selector, no bindable reasoning-effort selector, no guaranteed one-hour execution field, and no authenticated completed-run model/effort receipt. Making `GPT-6 / maximum` enforceable requires an owner-authorized product/workspace/API/admin surface that exposes persistent model and effort controls plus runtime attestation. The historical P26 `You cannot modify this task` response remains an authorization-context boundary; repository operations history records later successful modification from another authorized context. The lawful workaround is the owning/otherwise-authorized context or authorized platform support, not task duplication, permission bypass, or a repository edit presented as scheduler repair. I made no scheduler or permission change.

Before new work I recovered the current root `QUEUE.md`, `POSTED.md`, `RESULTS.md`, `probability_campaign_2026_09/INDEX.md`, `RANKING.md`, the current owner directive and implementation manifest, the newest R01 report, neighboring admission reports, the canonical claims directory, and the current D/E/F/G/H/I intake continuity. No canonical intake ledger or claim release had appeared since the preceding R01 report. The prior R01 successor cursor had reached I0130 (already owned) with no populated I0131+ row.

## 2. I0024 is preserved and not reopened

The completed Aldous–Fill source remains Open Problem 3.44, which asks for an exact infimum-over-flows characterization of relaxation time rather than the known Chapter-4 path-congestion upper bound. Fresh primary-source checking on 2026-09-18 confirms the source still states that exact question.

The frozen R01 answer remains

\[
\tau_2=
\inf_{R:\,BR=I_{H_0}}
\sup_{0\ne b\in H_0}
\frac{(Rb)^T C^{-1}(Rb)}{b^T\Pi^{-1}b},
\qquad
R_*=CB^TL^+,
\]

with fixed distortion metric `C=1` and the existing distinct audits

- `R20-AUDIT-R01-I0024-03 = PASS_MATH_SOURCE_FIT`;
- `P26-AUDIT-R01-I0024-AF344-SINGULAR-RIGHT-INVERSE-10 = PASS`.

The bounded fresh literature search again surfaced the Aldous–Fill exact question and the Chapter-4 non-exact upper bound, but no later primary source explicitly publishing the same stationary-weighted right-inverse formula as the resolution of OP3.44. Publication priority therefore remains **UNVERIFIED**, not claimed.

## 3. A genuinely new source changed the admission state

The previous admission bottleneck was broken by a source published after the older intake frontier:

M. Ali Khan, Arthur Paul Pedersen, Maxwell B. Stinchcombe, *Almost-Uniform Bayesian Convergence to the Truth Is Not Characterized by Countable Additivity on Conditional Hitting Times*, arXiv:2609.20683v1, submitted **17 September 2026**.

The paper repairs/refutes parts of Michael Nielsen's 2021 finitely additive Bayesian convergence results. Its Remark 6.11 and Section 10 explicitly leave open:

> Do the approximation property and CHT together imply almost-sure convergence to the truth for an arbitrary probability function?

This is exactly the unsupported statement of Nielsen's Corollary 1. Khan–Pedersen–Stinchcombe prove it only for the one-ultrafilter mixture family containing their counterexample; they explicitly state that the arbitrary-probability-function case remains open.

The source is an honest CLOSABLE yes/no target: a universal proof closes it; a single probability function satisfying the exact source positivity, approximation and CHT hypotheses but failing eventwise almost-sure posterior convergence refutes it.

Fresh repository searches immediately before claiming for `2609.20683`, the exact title, and `Nielsen Corollary 1 CHT` returned no match; the intended claim path returned 404. Root exclusions and claims had already been recovered, so no source-matching prior owner, POSTED exclusion, or canonical attempt was found. Fresh exact-title/current-literature searches dated 2026-09-18 found the new source and the original Nielsen paper but no later source-matching resolution. Because the paper is about one day old, this is necessarily bounded negative evidence rather than a novelty certificate.

I therefore created, create-only, the exclusive R01 successor claim

`operations/claims/KPS-2026-NIELSEN-COR1.md`

at commit

`e818b81b7f90b7eb7aae7b6b0b2a589f79479a6e`.

The lane state has therefore genuinely moved from `PENDING_ADMISSION` to an owned, source-exact `CLAIMED / READY / CLOSABLE OUTSIDE` target.

## 4. Frozen metric for the new target

For a source-admissible finitely additive probability function `P` and Borel event `A`, put

\[
F(P,A):=\{\omega:P_n(A)(\omega)\not\to\mathbf 1_A(\omega)\}.
\]

Define

\[
\Gamma_{\rm AS}:=\sup_{P,A}P(F(P,A)),
\]

with the supremum over exactly the source hypotheses, and track a certified interval

\[
L_{\rm AS}\le \Gamma_{\rm AS}\le U_{\rm AS}
\]

through the single scalar

\[
W_{\rm AS}:=U_{\rm AS}-L_{\rm AS}.
\]

The admission baseline is the rigorous trivial interval `0 <= Gamma_AS <= 1`, hence

\[
\boxed{W_{\rm AS}=1.}
\]

A proof of the corollary yields `Gamma_AS=0`; any certified counterexample with positive failure mass yields `L_AS>0` and already refutes the source statement even before the whole interval is identified. This run establishes the metric but does not improve the numeric width: `1 -> 1`.

## 5. Method #8 — DISCRETIZE: a general companion-measure / Boolean-homomorphism normal form

The source's counterexample obtains a countably additive companion only for its special ultrafilter mixture. The first new idea is that **every** probability function with the approximation property admits an exact finite-information normal form.

Let `Omega={0,1}^N`, let `B` be its Borel sigma-algebra, and let `C` be the clopen algebra generated by finite cylinders. Let `P` be any finitely additive probability function satisfying the source's positivity assumption and the approximation property.

### Theorem 5.1 — canonical companion normal form

There exist

1. a unique countably additive Borel probability `R` agreeing with `P` on every clopen event;
2. for every Borel `A`, a Borel function `f_A:Omega->[0,1]` defined `R`-a.e.;
3. under the approximation property, an `R`-measure-algebra element `Phi(A)` with `f_A=1_{Phi(A)}` `R`-a.e.;

such that for every length-`n` cylinder `C_n(omega)`,

\[
P_n(A)(\omega)
 =\frac{P(A\cap C_n(\omega))}{P(C_n(\omega))}
 =E_R[\mathbf 1_{\Phi(A)}\mid\mathscr F_n](\omega).
\]

Moreover `Phi` is a Boolean-algebra homomorphism from Borel events into the `R`-measure algebra, fixes every clopen event, and

\[
P(A)=R(\Phi(A)).
\]

### Proof

Restrict `P` to the clopen algebra. If pairwise-disjoint clopens `C_j` have clopen union `C`, compactness of `C` makes the open cover `{C_j}` finite after deleting empty members. Thus finite additivity already gives the premeasure identity for every countable clopen decomposition whose union stays clopen. The restriction therefore has a unique countably additive Borel extension `R`. The source positivity hypothesis gives positive `R`-mass to every nonempty cylinder.

Fix Borel `A`. On clopens define

\[
\nu_A(C):=P(A\cap C),\qquad
\lambda_A(C):=P(A^c\cap C).
\]

Both are finite nonnegative premeasures on the clopen algebra and extend uniquely to countably additive Borel measures `mu_A` and `lambda_A`. On clopens, `nu_A+lambda_A=P=R`; uniqueness of extension gives

\[
\mu_A+\lambda_A=R.
\]

Hence `mu_A <= R`. Let

\[
f_A=\frac{d\mu_A}{dR},\qquad 0\le f_A\le1.
\]

For every nonempty finite cylinder `C`,

\[
P(A\cap C)=\mu_A(C)=\int_C f_A\,dR,
\]

and division by `P(C)=R(C)>0` gives the posterior identity with `E_R[f_A|F_n]`.

For a clopen `C`, finite additivity gives

\[
\begin{aligned}
P(A\triangle C)
 &=P(A\cap C^c)+P(A^c\cap C)\\
 &=\mu_A(C^c)+R(C)-\mu_A(C)\\
 &=\int |f_A-\mathbf1_C|\,dR.
\end{aligned}
\]

For every indicator `1_C`, pointwise

\[
|f_A-\mathbf1_C|\ge \min(f_A,1-f_A).
\]

The approximation property says the left integral can be made arbitrarily small by clopen `C`. Therefore

\[
\int\min(f_A,1-f_A)\,dR=0,
\]

so `f_A` is `{0,1}`-valued `R`-a.e. Define `Phi(A)` to be its support as an element of the `R`-measure algebra. Conversely, if every `f_A` is indicator-valued, ordinary clopen density under the countably additive regular probability `R` gives the source approximation property. Thus this indicator condition is in fact equivalent to approximation.

If `A,D` are disjoint then extension uniqueness gives `f_{A union D}=f_A+f_D`; complements give `f_{A^c}=1-f_A`; monotonicity handles intersections. Since the densities are indicators, these identities say exactly that `Phi` preserves finite Boolean operations modulo `R`. If `A` is clopen then `mu_A(C)=R(A cap C)` on clopens, hence `f_A=1_A`; so `Phi` fixes clopens. Finally

\[
P(A)=\mu_A(\Omega)=\int f_A\,dR=R(\Phi(A)).
\]

This proves the theorem. ∎

**Interpretation.** Under approximation, the entire finitely additive posterior process is ordinary countably additive martingale conditioning of the companion event `Phi(A)`. The finite-additive pathology has been moved completely into the Boolean homomorphism `Phi`, which may fail countable continuity.

This is the useful meaning of #8: finite probability spaces themselves cannot refute the source question because finite additivity equals countable additivity there. The correct finite-information discretization is the operator `Phi`, not enumeration of finite sample spaces.

## 6. CHT becomes a fixed-point condition on posterior first-hitting open sets

The same normal form translates the second source hypothesis exactly.

For a Borel `B` and `delta in (0,1)`, write

\[
O_R(B,\delta)
 :=\bigcup_{n\ge1}
 \left\{\omega:E_R[\mathbf1_B\mid\mathscr F_n](\omega)>\delta\right\}.
\]

Every finite partial union is clopen. For `B=Phi(A)`, Theorem 5.1 says this is exactly the source's conditional-posterior hitting union for `A`.

### Proposition 6.1 — exact CHT translation

Under the approximation property, `P` has CHT if and only if, for every Borel `A` and every `delta in (0,1)`,

\[
\boxed{
\Phi\bigl(O_R(\Phi(A),\delta)\bigr)
 =O_R(\Phi(A),\delta)
 \quad (R\text{-a.e.}).
}
\]

### Proof

Let `O_N` be the union through time `N` and `O` the infinite union. Every `O_N` is clopen, hence `P(O_N)=R(O_N)` and `Phi(O_N)=O_N`. CHT is exactly

\[
P(O)=\lim_NP(O_N)=\lim_NR(O_N)=R(O).
\]

But `P(O)=R(Phi(O))`. Since `O_N subset O`, Boolean monotonicity gives `O_N=Phi(O_N) subset Phi(O)` modulo `R` for each `N`. Countable additivity of `R` then gives `O subset Phi(O)` modulo `R`. Consequently equality of their `R`-masses is equivalent to `Phi(O)=O` modulo `R`. ∎

This is a sharper formulation of the open problem: **does a Boolean homomorphism fixing all clopens and all posterior first-hitting opens generated by its own range necessarily have enough sequential continuity to force eventwise almost-sure learning?**

No closure is claimed from this reduction.

## 7. Method #27 — SWAP THE QUANTIFIERS: every fixed positive error threshold is already P-null

The source carefully identifies the valid output of the failed sufficiency proof:

for every probability budget `epsilon>0` and every accuracy `delta>0`, there exist an event `E` and time `N` such that `P(E)<epsilon` and the posterior error is at most `delta` for every `n>=N` off `E`.

That valid statement already yields a stronger source-wide partial theorem than the present reports had recorded.

### Proposition 7.1 — fixed-threshold nullity

For every source-admissible `P`, every Borel `A`, and every fixed `r>0`,

\[
F_r(P,A):=
\left\{\omega:\limsup_{n\to\infty}
|P_n(A)(\omega)-\mathbf1_A(\omega)|>r\right\}
\]

has

\[
\boxed{P(F_r(P,A))=0.}
\]

### Proof

The claim is trivial for `r>=1`, so take `0<r<1`. Fix arbitrary `epsilon>0` and apply the source's valid quantifier statement with accuracy `delta=r/2`. It gives `E,N` with `P(E)<epsilon` and error at most `r/2` for all `n>=N` outside `E`. A point with limsup error greater than `r` cannot lie outside `E`, hence `F_r subset E`. Therefore

\[
P(F_r)\le P(E)<\epsilon.
\]

Because `epsilon` is arbitrary and `P(F_r)` is a real number, `P(F_r)=0`. ∎

Now the full nonconvergence event is exactly

\[
F(P,A)=\bigcup_{m\ge1}F_{1/m}(P,A).
\]

Thus any counterexample to Nielsen's Corollary 1 must be a **pure diagonal failure**: every fixed positive error threshold has a `P`-null limsup set, while their countable union has positive `P`-mass. This is possible in principle under finite additivity, so Proposition 7.1 does not solve the source problem; it identifies the only remaining mechanism.

Equivalently, in the `Phi` normal form the missing step is a very particular countable-union continuity property of the kernel ideal

\[
\mathcal I_\Phi=\{E:\Phi(E)=0\ \ R\text{-a.e.}\}.
\]

The source question becomes whether CHT forces this ideal to absorb the specific increasing union generated by the posterior-error threshold null events.

## 8. Method #15 — BREAK THE SYMMETRY: refutation-first attacks and the first obstruction

I followed the contract and tried to refute before proving more.

The obvious attack is to take the Khan–Pedersen–Stinchcombe one-ultrafilter mixture and remove the countably additive atoms at its distinguished paths so that posterior errors can persist there. The source itself proves this route fails: Proposition 6.3 shows that if the countably additive component leaves a large set of distinguished paths atomless, CHT fails; Proposition 6.7 then shows that inside this entire architecture CHT forces enough atoms to protect the paths from the countably additive exceptional set and hence forces almost-sure convergence.

So a source-valid counterexample must leave that symmetric one-level architecture.

I explored a two-level/hierarchical replacement: an outer finitely additive charge would range over parent paths, while each parent would carry an inner generalized-point/ultrafilter charge over descendants. The intended diagonal mechanism is to make the persistent error amplitude depend on the outer level so that every fixed `r` sees a null set while the union over `r downarrow 0` remains charged.

The first obstruction is **coherence**. A one-level ultrafilter gives a single Boolean evaluation of each event along its distinguished sequence. At two levels, the parent evaluation and the inner child evaluations need not agree on an outer-large set. If they disagree, the posterior first-hitting open set can acquire a positive generalized charge not seen by the finite partial hitting unions — exactly the CHT defect isolated by the source's Proposition 6.3. Merely nesting arbitrary ultrafilters therefore does not survive CHT.

A viable hierarchical counterexample would need an additional Fubini/idempotent-style coherence law ensuring that all first-hitting opens are evaluated canonically at every level while the threshold-null ideal still fails the final diagonal union. I did not construct such a coherent hierarchy this run. This is a failed route with a precise obstruction, not a refutation of the source statement.

A second attempted proof route also stops at a precise place. Because CHT fixes every first-hitting open `O_R(B,delta)`, one might hope to recover a range event `B` by sending `delta up to 1`. Under `R`, intersections of those decreasing hitting opens recover `B` modulo the usual martingale exceptional set. But `Phi` has only finite Boolean continuity; passing from `Phi(O_delta)=O_delta` for every fixed threshold to the countable intersection is exactly another form of the missing diagonal step. Repeating CHT does not automatically remove it because CHT records **first** crossings, not later recrossings after an arbitrary time. This explains why the naive tail-shift proof does not close.

## 9. What moved, what did not, and next attack

The important movement is operational and mathematical:

- R01 is no longer waiting for an admissible successor: a fresh, explicitly open, unowned, source-exact CLOSABLE probability problem was found and claimed.
- The new source has a general canonical companion/Boolean-homomorphism representation, not limited to the source's special ultrafilter family.
- CHT has been translated exactly into a fixed-point property for a family of posterior hitting opens.
- The source-wide valid quantifier estimate has been sharpened to `P(F_r)=0` for every fixed error threshold `r>0`, so any counterexample must be an intrinsically diagonal countable-union failure.
- The one-level atom-removal refutation route is ruled out by the source, and a naive two-level ultrafilter replacement exposes a concrete coherence obstruction.

The numeric gap metric itself does **not** move in this first claimed run: `W_AS=1 -> 1`. No finite checker was built, because none of the new claims has a finite core whose certification would move `W_AS`; the proofs above are analytic and written on the page. No audit was requested: this package is OPEN/PARTIAL, not closure-ready.

The next run should not repeat #8/#15/#27. The best next methods are **#11 DUALIZE, #19 MAKE IT AN ALGORITHM, #30 ONE SCALE/ONE DIRECTION AT A TIME**: dualize the Boolean-homomorphism fixed-point constraints into a statement about the kernel ideal, formulate a constructive hierarchy/coherence algorithm for a counterexample, and separately attack the YES direction by proving countable-union closure first for nested posterior-error sets of one event.

## 10. Structured ledger delta

```yaml
ledger_delta:
  worker: R01
  frozen_previous_source: I0024
  frozen_previous_metric: "C=1"
  source: KPS-2026-NIELSEN-COR1
  source_url: "https://arxiv.org/abs/2609.20683"
  source_scope: "Khan-Pedersen-Stinchcombe Section 10 / Nielsen Corollary 1: approximation + CHT => eventwise almost-sure posterior convergence for arbitrary source probability functions"
  lane_status_before: PENDING_ADMISSION
  lane_status_after: "CLAIMED / READY / CLOSABLE OUTSIDE / OPEN"
  claim_commit: e818b81b7f90b7eb7aae7b6b0b2a589f79479a6e
  metric: "W_AS = U_AS - L_AS for Gamma_AS = sup_{P,A} P(nonconvergence event)"
  metric_before: 1
  metric_after: 1
  unchanged_count: 1
  tried_moves: [8, 15, 27]
  remaining_obligation: "Either prove CHT forces the diagonal countable-union closure needed for P(F)=0, or construct a coherent non-one-level finitely additive counterexample satisfying exact CHT with P(F)>0."
  evidence:
    - "Theorem 5.1 canonical companion / Boolean-homomorphism normal form"
    - "Proposition 6.1 exact CHT fixed-point translation"
    - "Proposition 7.1 fixed-threshold nullity P(F_r)=0"
    - "source Propositions 6.3 and 6.7 rule out the naive atomless one-ultrafilter refutation route"
  audit_ids: []
  status: OPEN
```
