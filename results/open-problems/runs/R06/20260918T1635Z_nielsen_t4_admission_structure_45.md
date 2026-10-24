Model actually ran: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — not GPT-6 maximum. SUCCESSOR ADMITTED: the successor metric moved from `UNMEASURED` to the rigorously initialized interval `0 <= Delta_CHT <= 1/2`, so `W_CHT: UNMEASURED -> 1/2`; frozen I0056/H_{5,5} width remains `0 -> 0`; methods #2 ATTACK THE NEGATION FIRST, #18 SAY IT IN ANOTHER LANGUAGE, #24 FIND THE EXTREMAL OBJECT.**

# R06 — Nielsen Theorem 4 successor admission and structural reductions

Date: 2026-09-18 UTC  
Worker: R06  
Lane: CLOSABLE OUTSIDE  
Repository: private `yspennstate/math-open-problems`, branch `master`

## 1. Continuity: I0056 stays frozen and rotated

I started from the newest immutable R06 report

`runs/R06/20260918T1524Z_successor_admission_f0138_resolution_delta_44.md`

and reread the required campaign roots, current queue/admission evidence, the latest operations implementation manifest, current neighboring admission work, and the latest ownership deltas before acting. I did **not** reopen Lyons--Peres I0056.

Its exact source remains Question 6.20 of Lyons--Peres:

> What is `Phi_V(G)` for regular co-regular plane graphs `G`? What are `Phi_E(G)` and `Phi_V(G)` for more general transitive plane graphs `G`?

For the frozen outer-vertex normalization on the Schlaefli `{5,5}` tessellation,

\[
\Phi_V(H_{5,5})=\sqrt5,\qquad [L,U]=[\sqrt5,\sqrt5],\qquad U-L=0.
\]

The H55 subtarget remains PROVED / audit-complete. The full two-clause Question 6.20 remains PARTIAL. Haslegrave--Panagiotis face degrees 3 and 4 remain excluded prior art. The I0056 attacking lifecycle remains ROTATED / NOT REOPENED.

## 2. New admissible successor found and claimed create-only

The latest coordinator admission delta still had `E_READY_SUCCESSOR=0` through the old I-series frontier, but a newer outside source created a genuinely new frontier. On 2026-09-17, M. Ali Khan, Arthur Paul Pedersen and Maxwell B. Stinchcombe posted

*Almost-Uniform Bayesian Convergence to the Truth Is Not Characterized by Countable Additivity on Conditional Hitting Times*, arXiv:2609.20683v1.

The paper proves that the published proof of Michael Nielsen's 2021 Theorem 4 is invalid and explicitly leaves its standalone truth undecided. Section 10 asks:

> Is Nielsen's Theorem 4 true?

The exact theorem, under Nielsen's Assumption 1, is:

> There are uncountably many probability functions on the Borel subsets of Cantor space that have the CHT property but not the approximation property.

The source itself restates the theorem in Section 2.5 and explains in Section 7.1 why the original extension construction cannot work: a finitely additive Borel probability agreeing with a regular countably additive Borel probability on every open set must in fact agree on every Borel set.

This is distinct from the separate Section-10 Corollary-1 question claimed by R01. Immediately before claiming, I checked the exact prospective claim path (absent), searched repository commits for `Nielsen` (recovering only R01's distinct Corollary-1 claim), reread current admission evidence, and ran bounded current source/title/question searches. No source-matching Theorem-4 owner, exclusion, or later resolution was recovered. Because the source is about one day old, that literature search is necessarily shallow negative evidence, not a novelty certificate.

I therefore created the exclusive claim

`operations/claims/KPS-2026-NIELSEN-THEOREM4.md`

create-only at commit

`9aa2576e7b9b9b5c4cfe4b4b4f61ed8ab0bb6ef3`

and read it back at that exact commit. No other worker's claim was edited.

## 3. Frozen source metric

Let

\[
\Omega=\{0,1\}^{\mathbb N},\qquad \mathcal C=\text{clopen algebra},\qquad \mathcal B=\sigma(\mathcal C).
\]

For a source-admissible probability function `P`, put

\[
D(P):=\sup_{A\in\mathcal B}\inf_{C\in\mathcal C}P(A\triangle C)
\]

and

\[
\Delta_{\rm CHT}:=\sup\{D(P):P\text{ satisfies Assumption 1 and CHT}\}.
\]

For every `A`, either `C=empty` or `C=Omega` has error at most

\[
\min(P(A),1-P(A))\le \frac12,
\]

so

\[
\boxed{0\le\Delta_{\rm CHT}\le\frac12}.
\]

The single tracked quantity is

\[
W_{\rm CHT}=U-L.
\]

Admission initializes

\[
[L,U]=[0,1/2],\qquad \boxed{W_{\rm CHT}=1/2}.
\]

The lemmas below show that Nielsen's Theorem 4 is equivalent to `Delta_CHT>0`, so this metric is source-equivalent rather than merely a proxy.

## 4. Method #2 — attack the negation first: CHT forces every open/closed event to be clopen-approximable

The first attack was the opposite of Theorem 4: try to prove that CHT itself forces approximation. I cannot yet prove that for all Borel events, but the following full lemma is rigorous and removes the entire open/closed boundary.

### Lemma 4.1 (open-set approximation from CHT)

Let `P` satisfy Assumption 1 and CHT. If `G` is open, then for every `epsilon>0` there is a clopen `K` with

\[
P(G\triangle K)<\varepsilon.
\]

Consequently every closed event, and every finite Boolean combination of open events, is also clopen-approximable.

### Proof

Fix open `G` and `delta in (0,1)`. Let

\[
C_n=C_n(G,\delta)=\{P_n(G)>\delta\},\qquad
O_N=\bigcup_{n\le N}C_n,\qquad O=\bigcup_{n\ge1}C_n.
\]

Because `G` is open, every `x in G` lies in a finite cylinder contained in `G`. At that cylinder the posterior of `G` is exactly one. Hence

\[
G\subseteq O.
\]

Write `D_n` for the disjoint first-hitting pieces. Since `D_n` belongs to the finite sigma-algebra at time `n`, it is a finite union of length-`n` cylinders. On each such cylinder contained in `D_n`, the posterior of `G` exceeds `delta`; therefore exact finite additivity gives

\[
P(G\cap D_n)>\delta P(D_n).
\]

Summing over `n<=N`,

\[
P(G\cap O_N)>\delta P(O_N).
\]

CHT is precisely

\[
P(O_N)\longrightarrow P(O).
\]

Since `G cap O_N subseteq G`, monotonicity gives

\[
P(G)\ge \delta P(O).
\]

Together with `G subseteq O`,

\[
P(O\setminus G)=P(O)-P(G)\le (1-\delta)P(O)\le1-\delta.
\]

Also

\[
P(G\setminus O_N)\le P(O\setminus O_N)=P(O)-P(O_N)\longrightarrow0.
\]

Thus

\[
P(G\triangle O_N)
\le P(O)-P(O_N)+(1-\delta).
\]

Choose `delta` with `1-delta<epsilon/2`, then choose `N` so that `P(O)-P(O_N)<epsilon/2`. Since `O_N` is a finite union of clopen sets, it is clopen, and the desired inequality follows.

For a closed `F`, approximate `F^c` and complement the approximating clopen. Closure under finite Boolean operations follows from, e.g.,

\[
(A\cup B)\triangle(C\cup D)\subseteq(A\triangle C)\cup(B\triangle D)
\]

and finite subadditivity.  QED.

### Consequence

Any Theorem-4 witness must fail approximation on a genuinely infinitary Borel event. No open set, closed set, or finite Boolean combination of opens can witness failure. This is exactly where Nielsen's failed extension proof was too coarse: agreeing/behaving well on topologically finite-stage events does not settle the countable Borel closure.

## 5. Method #18 — say it in another language: the companion-measure / martingale representation

The second route moves the problem from finitely additive set functions to ordinary countably additive martingales plus a non-normal lifting.

### Lemma 5.1 (canonical companion and Radon--Nikodym densities)

Let `P` be any source-admissible probability function. There is a unique countably additive Borel probability `R` satisfying

\[
R(C)=P(C)\qquad(C\in\mathcal C).
\]

For each `A in B`, define on clopens

\[
\mu_A(C)=P(A\cap C).
\]

Then `mu_A` extends uniquely to a countably additive Borel measure dominated by `R`, so there is a density

\[
f_A=\frac{d\mu_A}{dR},\qquad 0\le f_A\le1.
\]

For every `n`,

\[
\boxed{P_n(A)=E_R[f_A\mid\mathscr F_n].}
\]

Moreover

\[
\boxed{
\inf_{C\in\mathcal C}P(A\triangle C)
=\int_\Omega \min(f_A,1-f_A)\,dR.
}
\]

Thus `A` is clopen-approximable under `P` iff `f_A` is `{0,1}`-valued `R`-almost surely.

### Proof

The clopen algebra is countable and every countable disjoint decomposition of a clopen set into clopen sets has only finitely many nonempty terms: the union is compact and the pieces form an open cover. Hence every finitely additive finite measure on the clopen algebra is already a premeasure. Caratheodory extension gives `R` from `P|C`.

The same argument applies to `mu_A`. On clopens,

\[
0\le\mu_A(C)\le P(C)=R(C),
\]

and the complementary premeasure `C -> P(A^c cap C)` shows after extension that `mu_A<=R`. Radon--Nikodym gives `f_A`.

For a length-`n` cylinder `B`,

\[
P(A\mid B)=\frac{P(A\cap B)}{P(B)}
=\frac{\int_B f_A\,dR}{R(B)},
\]

which is exactly the conditional expectation on the finite partition `F_n`.

For clopen `C`, finite additivity gives

\[
P(A\triangle C)
=P(A)+P(C)-2P(A\cap C)
=\int\bigl[f_A\mathbf 1_{C^c}+(1-f_A)\mathbf1_C\bigr]\,dR.
\]

Pointwise the best binary decision is `1` when `f_A>1/2` and `0` otherwise, with loss `min(f_A,1-f_A)`. Clopens are dense in `R`-measure among Borel sets on Cantor space, so clopen classifiers approximate this optimal Borel decision set and the displayed infimum follows. QED.

### CHT in this language

For `A,delta`, let

\[
M_n=E_R[f_A\mid\mathscr F_n],\qquad
O(A,\delta)=\{\sup_n M_n>\delta\}.
\]

Every finite `O_N` is clopen, hence `P(O_N)=R(O_N)`. Since `R` is countably additive,

\[
R(O_N)\uparrow R(O).
\]

Therefore

\[
\boxed{
P\text{ has CHT}
\iff
P(O(A,\delta))=R(O(A,\delta))
\quad\text{for every }A,\delta.
}
\]

So Theorem 4 becomes a very concrete question:

> Can a positive unital finite-information extension have a genuinely fractional density `f_A` on positive `R`-mass while agreeing with its countably additive companion on every self-generated martingale hitting open?

This is a smaller and more structured target than the original extension argument.

## 6. Uncountability is not the hard part: one witness amplifies to continuum many

The source asks for uncountably many probabilities. That quantifier can be removed completely.

### Lemma 6.1 (prefix amplification)

Suppose there exists one source-admissible probability function `P` with CHT and `D(P)>0`. Then there are continuum many distinct source-admissible probability functions with CHT and without the approximation property.

### Proof

Let `Q` be the fair-coin countably additive probability, and let

\[
h_b:\Omega\to[b],\qquad h_b(x)=bx,\qquad b\in\{0,1\}.
\]

For `lambda in (0,1)` define

\[
P_\lambda(A)=\lambda P(h_0^{-1}(A\cap[0]))
+(1-\lambda)Q(h_1^{-1}(A\cap[1])).
\]

Every nonempty cylinder has positive `P_lambda` probability, because after the first bit its mass is a positive scalar multiple of the corresponding positive component cylinder.

CHT is componentwise. At global time one the posterior on `[0]` is the constant `P(A_0)` and on `[1]` the constant `Q(A_1)`. If the relevant constant already exceeds the threshold, that whole component hits at time one. Otherwise, from time two onward the posterior process on that component is exactly the corresponding component posterior with time shifted by one. Thus the first-hitting continuity equation for `P_lambda` is the weighted sum of the CHT equation for `P` and the countably additive equation for `Q`.

If `A_0` witnesses `inf_C P(A_0 triangle C)=d>0`, put `B=h_0(A_0)`. For every global clopen `K`, its left restriction `K_0` is clopen and

\[
P_\lambda(B\triangle K)
\ge \lambda P(A_0\triangle K_0)
\ge \lambda d>0.
\]

So `P_lambda` fails approximation. Finally `P_lambda([0])=lambda`, hence distinct `lambda` give distinct probability functions. QED.

### Corollary 6.2 (metric is source-equivalent)

Nielsen Theorem 4 is true iff

\[
\boxed{\Delta_{\rm CHT}>0}.
\]

If the theorem is true, one of its probabilities has positive defect. Conversely, if `Delta_CHT>0`, some admissible `P` has `D(P)>0`, and Lemma 6.1 amplifies it to continuum many witnesses.

This removes the cardinality burden from all future runs. The only remaining mathematical question is whether a **single** CHT probability with positive approximation defect exists.

## 7. Method #24 — extremal object: the natural two-strand hidden-bit construction fails CHT for an exact reason

The RN formula says nonapproximation requires a genuinely fractional hidden density. The most direct extremal candidate is therefore a two-strand ultrafilter limit: take two sequences `d_k,e_k -> z` that are topologically indistinguishable at every fixed finite stage, and let

\[
v(A)=\lim_{k\to\mathcal U}\frac{\mathbf1_A(d_k)+\mathbf1_A(e_k)}2.
\]

For an event `H` containing every `d_k` and no `e_k`,

\[
v(H)=1/2,
\]

while every clopen event eventually contains both strands or neither, so

\[
v(H\triangle C)=1/2\qquad(C\in\mathcal C).
\]

This is exactly the desired maximal hidden-bit defect.

However, the obvious way to enforce positivity and tame later posteriors is to mix `v` with a symmetric countably additive component that gives positive atoms to both strands (plus a diffuse full-support component). That architecture fails CHT. For a threshold `delta>1/2`, the limit path can be arranged never to cross because its posterior of `H` is at most `1/2`, while every atomic `d_k in H` eventually has posterior tending to one and therefore crosses. Every fixed finite hitting union is clopen and hence has `v`-value zero at the limit fiber, but the full hitting open contains one strand on an ultrafilter-large set and therefore has `v`-value `1/2`. The CHT defect is the corresponding positive mixture weight times `1/2`.

The opposite choice, leaving the strands unatomized, runs into the same mechanism already isolated by Khan--Pedersen--Stinchcombe Proposition 6.3: a complement-of-the-distinguished-set event makes the unatomized paths cross at moving times and produces a positive CHT defect.

So the most obvious hidden-bit witness is ruled out from both sides:

- atoms reveal the hidden bit eventually and create a half-fiber hitting discontinuity;
- no atoms create the moving-time discontinuity of the source's Proposition 6.3.

This is useful failure information rather than a theorem-sized source claim. It says the next candidate must not be a finite multi-strand perturbation of the source's one-limit-point architecture.

## 8. Current blocker and next route

Using Lemma 5.1, write `T 1_A=f_A`. The next proof/refutation target is now:

\[
\boxed{
\text{Does CHT force every }f_A\text{ to be }\{0,1\}\text{-valued }R\text{-a.s.?}
}
\]

Lemma 4.1 proves this for every open/closed/constructible event. A source counterexample must therefore place genuinely fractional `f_A` on an infinitary Borel event while keeping every self-generated martingale hitting open `O(A,delta)` sharp enough to satisfy `P(O)=R(O)`.

The next three methods should not repeat `#2/#18/#24`. Best candidates are:

- #5 ADD A PARAMETER AND DIFFERENTIATE: study `delta -> O(A,delta)` and whether layer-cake identities force `min(f_A,1-f_A)` to vanish;
- #11 DUALIZE: formulate positive defect as a separation functional on the `L^1(R)` closure of clopen indicators and translate CHT into constraints on the dual witness;
- #29 ADD THE POINTS AT INFINITY: work directly on the Stone space of the Borel algebra, where failure of approximation is nontrivial conditional mass in fibers over Cantor space and CHT constrains which fiber points can lie over hitting-open boundaries.

No finite checker was built because this run's gains are structural infinite-dimensional lemmas, not a finite claim.

## 9. Model / scheduler control

The exposed task-management surface still provides prompt/title, timing/schedule, timing mode and enabled state, but no binding model-family selector, no reasoning-effort selector, no authenticated applied-run model/effort telemetry and no guaranteed hour-long execution field.

Therefore `GPT-6 / maximum` remains a prompt request only on this surface. This run actually identifies as GPT-5.6 Sol; reasoning effort is UNVERIFIED. The historical P26 `You cannot modify this task` response was authorization-context-specific; repository history records a later authorized context that succeeded. The lawful remedy remains an owner/admin/product/backend context exposing persistent model/reasoning settings and attested runtime metadata, not a worker-side bypass. No scheduler change was attempted.

## 10. Structured ledger delta

```yaml
ledger_delta:
  track: R06
  lane: "CLOSABLE OUTSIDE"
  preserved_source:
    id: I0056
    frozen_metric:
      name: "certified interval width U-L for Phi_V(H_{5,5})"
      before: 0
      after: 0
      status: "PROVED / AUDIT-COMPLETE / ROTATED / NOT REOPENED"
    full_question_6_20: "PARTIAL"
  successor:
    id: "KPS-2026-NIELSEN-THEOREM4"
    source: "Khan-Pedersen-Stinchcombe, arXiv:2609.20683v1, Nielsen Theorem 4 / Section 10"
    source_question: "Is Nielsen's Theorem 4 true?"
    exact_target: >-
      Under Assumption 1, uncountably many Borel probability functions on Cantor space
      have CHT but not the approximation property.
    ownership: "R06 exclusive create-only claim"
    claim_commit: "9aa2576e7b9b9b5c4cfe4b4b4f61ed8ab0bb6ef3"
    status: "OPEN / PARTIAL"
  fixed_metric:
    name: "W_CHT = width of certified interval for Delta_CHT"
    definition: >-
      Delta_CHT = sup_P sup_A inf_clopen_C P(A triangle C), over Assumption-1 + CHT P.
    before: "UNMEASURED"
    after: "1/2"
    interval: "[0, 1/2]"
    unchanged_count: 0
  tried_moves: [2, 18, 24]
  new_rigorous_results:
    - "CHT implies every open/closed event is clopen-approximable."
    - "Canonical companion R and densities f_A give P_n(A)=E_R[f_A|F_n]."
    - "Approximation defect equals integral min(f_A,1-f_A) dR."
    - "CHT is equivalent to P(O(A,delta))=R(O(A,delta)) on all self-generated hitting opens."
    - "One CHT/nonapprox witness amplifies by prefix splitting to continuum many; Theorem 4 iff Delta_CHT>0."
    - "Natural two-strand hidden-bit candidate is blocked by an explicit CHT discontinuity mechanism."
  remaining_obligation: >-
    Decide whether CHT forces every companion density f_A to be {0,1}-valued R-a.s.;
    equivalently decide whether Delta_CHT=0 or Delta_CHT>0. Do not reopen I0056.
  audit_ids: []
  next_moves: [5, 11, 29]
```
