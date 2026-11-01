Model actually ran: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — not GPT-6 maximum. NO METRIC MOVEMENT: `W_CHT: 1/2 -> 1/2`; frozen I0056/H_{5,5} width remains `0 -> 0`; successor unchanged count `0 -> 1`; methods #5 ADD A PARAMETER AND DIFFERENTIATE IN IT, #11 DUALIZE, #29 ADD THE POINTS AT INFINITY.**

# R06 — Nielsen Theorem 4: convexification no-go for the KPS ultrafilter architecture

Date: 2026-09-18 UTC  
Worker: R06  
Lane: CLOSABLE OUTSIDE  
Repository / branch: private `yspennstate/math-open-problems` / `master`

## 1. Continuity and source state

I continued from the newest immutable R06 report

`runs/R06/20260918T1635Z_nielsen_t4_admission_structure_45.md`

and from the create-only canonical claim

`operations/claims/KPS-2026-NIELSEN-THEOREM4.md`.

The historical native-title source, Russell Lyons and Yuval Peres, *Probability on Trees and Networks*, Question 6.20 / intake I0056, remains frozen and is **not reopened**. Its exact source question is:

> What is `Phi_V(G)` for regular co-regular plane graphs `G`? What are `Phi_E(G)` and `Phi_V(G)` for more general transitive plane graphs `G`?

For R06's frozen outer-vertex normalization on the `{5,5}` tessellation,

\[
\Phi_V(H_{5,5})=\sqrt5,\qquad [L,U]=[\sqrt5,\sqrt5],\qquad U-L=0.
\]

That subtarget is PROVED / audit-complete; the full two-clause source Question 6.20 remains PARTIAL. Haslegrave--Panagiotis face degrees 3 and 4 remain excluded prior art. The I0056 attacking lifecycle remains rotated.

The active R06 source is instead the lawfully claimed successor from M. Ali Khan, Arthur Paul Pedersen and Maxwell B. Stinchcombe, *Almost-Uniform Bayesian Convergence to the Truth Is Not Characterized by Countable Additivity on Conditional Hitting Times*, arXiv:2609.20683v1 (submitted 2026-09-17), Section 10. They invalidate Nielsen's published proof of Theorem 4 and explicitly leave its standalone truth undecided. The exact target, under Nielsen's Assumption 1, is:

> There are uncountably many probability functions on the Borel subsets of Cantor space that have the CHT property but not the approximation property.

The current claim is distinct from R01's `KPS-2026-NIELSEN-COR1`, which concerns the separate arbitrary-probability almost-sure-convergence question.

## 2. Required repository and literature reread

Before new mathematics I recovered the campaign `probability_campaign_2026_09/INDEX.md` and `RANKING.md`, root `POSTED.md`, root `RESULTS.md`, root `QUEUE.md`, the operative follow-up implementation record `operations/FOLLOWUP_IMPLEMENTATION_2026-09-16.md`, the canonical Theorem-4 claim, the newest R06 report, and the neighboring R01 Nielsen-Corollary-1 report. The latest coordinator/admission searches continue to recognize the R06 Theorem-4 claim as exclusively owned; no competing owner or audit-complete resolution was found.

Dated primary-literature check: **2026-09-18**. The official arXiv page still shows only `v1`, submitted 2026-09-17 16:52:41 UTC. Its Introduction says explicitly that Nielsen Theorem 4's proof invokes the failed extension claim and that the authors **do not decide the standalone truth**. Section 7.1 says the original proof draws on two distinct extreme points of an extension set that in fact has no such nontrivial points. Bounded exact-title, arXiv-ID, exact-question, `Theorem 4`, `CHT`, `convex combination`, and `ultrafilter` searches found no later primary source resolving the question or recording the no-go result below. This is bounded negative evidence only; no publication-priority claim is made.

The source also gives two pieces used below:

1. its one-limit-point geometry has `z=0^infinity` and `d_k=0^{k-1}10^infinity`, so `d_k -> z`;
2. Theorem 7.3 constructs, for every free ultrafilter and an ordinarily vanishing shell-error sequence, a merely finitely additive probability satisfying positivity and almost-uniform convergence, hence in particular approximation and CHT.

No finite exact checker is relevant to the theorem below: the new claim is an analytic finite-additivity argument with no finite computational core.

## 3. Frozen successor metric

As in the preceding report, for a source-admissible probability function `P` let

\[
D(P)=\sup_{A\in\mathcal B}\inf_{C\in\mathcal C}P(A\triangle C),
\]

and

\[
\Delta_{\rm CHT}=\sup\{D(P):P\text{ satisfies Assumption 1 and CHT}\}.
\]

Track

\[
W_{\rm CHT}=U-L
\]

for a certified interval `L <= Delta_CHT <= U`. The previous run rigorously initialized

\[
0\le\Delta_{\rm CHT}\le\frac12,
\]

and proved that Nielsen Theorem 4 is true iff `Delta_CHT>0`. Therefore

\[
W_{\rm CHT}=\frac12
\]

is the exact current metric. This run does **not** improve that interval, so the successor unchanged count becomes `1`.

The run does, however, eliminate the most natural repair of Nielsen's failed convex-extreme-point construction.

## 4. Idea before proof

Nielsen's invalid proof sought nontrivial convex combinations of extreme finitely additive extensions. Khan--Pedersen--Stinchcombe replace the nonexistent extensions by a valid family indexed by free ultrafilters. The first repair to test is therefore obvious:

> take two valid KPS ultrafilter probabilities and convexify them, hoping that the mixture ceases to have the approximation property while retaining CHT.

It does cease to be extremal, and it can create exactly the desired fractional hidden density. But CHT is not convex. The limit point `z` exposes the mixture: the hidden event has posterior uniformly below a threshold along the zero cylinders, while a positive charge of atom-protected distinguished paths eventually crosses that same threshold. The resulting first-hitting union misses `z` but contains positive finitely additive mass at infinity. This creates an explicit CHT gap.

The theorem below proves this not only for two ultrafilters, but for every non-two-valued free charge in the KPS one-limit-point architecture.

## 5. Method #5 — add the mixture parameter: quantitative non-extremality forces a CHT gap

Let

\[
\Omega=\{0,1\}^{\mathbb N},\qquad
z=0^\infty,\qquad
d_k=0^{k-1}10^\infty.
\]

Let `lambda` be a finitely additive probability on `N` such that `lambda(F)=0` for every finite `F`. Define the induced probability function on Borel subsets of `Omega` by

\[
v_\lambda(B)=\lambda\bigl(\{k:d_k\in B\}\bigr).
\]

Let `mu` be a countably additive Borel probability with `mu({z})=0`, let `alpha in (0,1)`, and put

\[
P=\alpha v_\lambda+(1-\alpha)\mu.
\]

Assume `P` satisfies Nielsen's positivity Assumption 1, and assume the distinguished paths are atom-protected on a `lambda`-full set:

\[
J:=\{k:\mu(\{d_k\})>0\},\qquad \lambda(J)=1.
\]

### Theorem 5.1 — non-two-valued free charge is incompatible with CHT

If `lambda` is not `{0,1}`-valued, then `P` does **not** have CHT.

More precisely, if `S subseteq J` has

\[
q:=\lambda(S)\in(0,1),
\]

then for every

\[
\delta\in\bigl(1-\alpha(1-q),1\bigr)
\]

there is a Borel event `A` whose conditional-hitting union `O=O(A,delta)` satisfies

\[
P(O)-\lim_{N\to\infty}P(O_N)\ge \alpha q>0.
\]

#### Proof

Because `lambda` is not two-valued, choose `T subseteq N` with `lambda(T)=q in (0,1)`. Replacing `T` by `S=T cap J` does not change its `lambda`-mass, because `lambda(J^c)=0`; thus we may assume `S subseteq J` and `lambda(S)=q`.

Define the countable Borel event

\[
A:=\{d_k:k\in S\}.
\]

For `n>=1`, let

\[
Z_n=[0^n].
\]

Since `d_k in Z_n` exactly when `k>n`, freeness of `lambda` gives

\[
v_\lambda(Z_n)=1,
\qquad
v_\lambda(A\cap Z_n)=\lambda(S\cap\{k>n\})=q.
\]

Write

\[
t_n=\mu(Z_n),\qquad m_n=\mu(A\cap Z_n),
\]

so `0<=m_n<=t_n<=1`. The posterior of `A` along the limit path is therefore

\[
P(A\mid Z_n)
=\frac{\alpha q+(1-\alpha)m_n}
       {\alpha+(1-\alpha)t_n}.
\]

Subtracting from one gives

\[
1-P(A\mid Z_n)
=\frac{\alpha(1-q)+(1-\alpha)(t_n-m_n)}
       {\alpha+(1-\alpha)t_n}.
\]

The numerator is at least `alpha(1-q)` and the denominator is at most one. Hence, **uniformly in n**,

\[
P(A\mid Z_n)\le 1-\alpha(1-q)<\delta.
\]

Thus the limit point never crosses the threshold:

\[
z\notin O(A,\delta).
\]

Now fix `k in S`. For `n>=k`, the cylinder

\[
B_{k,n}:=[d_k\mathord{\upharpoonright}n]
\]

contains `d_k` but no other distinguished path `d_j`. Hence

\[
v_\lambda(B_{k,n})=v_\lambda(A\cap B_{k,n})=0.
\]

Consequently

\[
P(A\mid B_{k,n})
=\frac{\mu(A\cap B_{k,n})}{\mu(B_{k,n})}.
\]

Because `k in J`, `mu({d_k})>0`. The cylinders `B_{k,n}` decrease to `{d_k}`, and countable additivity of `mu` gives

\[
\mu(B_{k,n})\downarrow\mu(\{d_k\}),
\qquad
\mu(A\cap B_{k,n})\downarrow\mu(\{d_k\}).
\]

Therefore

\[
P(A\mid B_{k,n})\longrightarrow1.
\]

Since `delta<1`, every `d_k` with `k in S` eventually crosses. Thus

\[
\{k:d_k\in O\}\supseteq S
\]

and hence

\[
v_\lambda(O)\ge q.
\]

Introduce the countably additive companion

\[
R=\alpha\delta_z+(1-\alpha)\mu.
\]

Every clopen `C` satisfies

\[
v_\lambda(C)=\mathbf 1_C(z),
\]

because `d_k->z` and membership in a clopen set is eventually constant along the sequence. Therefore

\[
P(C)=R(C)\qquad(C\text{ clopen}).
\]

Each finite hitting union `O_N` is clopen, so

\[
P(O_N)=R(O_N).
\]

Countable additivity of `R` and `O_N up O` yield

\[
\lim_N P(O_N)=\lim_N R(O_N)=R(O).
\]

But `z notin O`, so

\[
R(O)=(1-\alpha)\mu(O),
\]

whereas

\[
P(O)=\alpha v_\lambda(O)+(1-\alpha)\mu(O).
\]

Thus

\[
P(O)-\lim_NP(O_N)
=\alpha v_\lambda(O)
\ge\alpha q>0.
\]

This violates CHT. QED.

### Corollary 5.2 — extremality is necessary inside the atom-protected one-limit-point architecture

Under the hypotheses above, CHT forces `lambda` to be `{0,1}`-valued. Equivalently, the free charge on the distinguished-index set must be an ultrafilter charge.

This is a one-way structural theorem. It does not say every ultrafilter charge gives CHT for arbitrary `mu`; KPS Proposition 6.3 shows the atom condition itself is also necessary on an ultrafilter-large set in their geometry. What Theorem 5.1 says is that **atomic protection plus a genuinely fractional free charge cannot coexist with CHT**.

## 6. Method #11 — dualize Nielsen's extreme-point idea: CHT is nonconvex

KPS Section 7.1 records that Nielsen's Theorem-4 proof draws on two distinct extreme points of an extension set. The extension set collapses to a singleton, so that proof fails. Their Theorem 7.3 supplies a valid family parameterized by free ultrafilters, which makes the most natural replacement attempt to convexify two of those valid probabilities.

Theorem 5.1 rules this out exactly.

### Corollary 6.1 — convex combinations of distinct KPS ultrafilter probabilities can lose CHT

Fix the ordinary-convergence KPS data from Theorem 7.3: one sequence `theta_k -> 0`, one `alpha in (0,1)`, and the corresponding countably additive component `R_0^theta`, which has positive mass at every distinguished point `d_k`. Let `U` and `V` be distinct free ultrafilters and let

\[
P_U=\alpha u_U+(1-\alpha)R_0^\theta,
\qquad
P_V=\alpha u_V+(1-\alpha)R_0^\theta.
\]

KPS Theorem 7.3 gives almost-uniform convergence for each endpoint; in particular, each endpoint satisfies approximation and CHT.

For `t in (0,1)`, however,

\[
P_t=tP_U+(1-t)P_V
=\alpha\bigl(tu_U+(1-t)u_V\bigr)+(1-\alpha)R_0^\theta.
\]

Because `U != V`, choose `S in U` with `S notin V`; then `S^c in V` and

\[
\lambda_t(S)=t
\]

for `lambda_t=t u_U+(1-t)u_V`. Thus `lambda_t` is not two-valued. Theorem 5.1 applies and shows that `P_t` fails CHT.

For the symmetric mixture `t=1/2`, an explicit witness has a CHT gap at least

\[
\boxed{\alpha/2}.
\]

Hence the class of source-admissible CHT probabilities is **not convex**, even though both endpoints can satisfy the stronger almost-uniform convergence property.

This is the precise obstruction to repairing Nielsen's failed extreme-point proof by simply replacing its nonexistent extreme extensions with two valid KPS ultrafilter constructions and averaging them.

No literature-novelty claim is made; the bounded current search did not locate this observation.

## 7. Method #29 — add the point at infinity: the entire defect lives at `z`

The proof identifies the missing boundary term exactly. At every finite stage `O_N`, the finitely additive charge and its countably additive companion agree because `O_N` is clopen:

\[
P(O_N)=R(O_N).
\]

The failure appears only after adjoining the infinite hitting union. The event is open but arranged so that

\[
z\notin O,
\qquad
v_\lambda(O)\ge q.
\]

Thus the finite stages converge to the companion value `R(O)`, while the finitely additive limit carries extra mass

\[
\alpha v_\lambda(O).
\]

The limit point `z` is therefore not cosmetic. It is the compactification point against which finite-information events cannot distinguish a free charge from `delta_z`; a nonextreme charge then splits at infinity, and the split is exactly what CHT detects.

This also explains why adding atoms to the distinguished paths does not rescue convexification. The atoms make each selected `d_k` eventually reveal its membership in `A`, while the zero path retains the fractional free-charge posterior. Those two facts pull the hitting union apart.

## 8. What this rules out, and what remains

The preceding run already showed:

- CHT forces every open/closed event and every finite Boolean combination of opens to be clopen-approximable;
- every source-admissible `P` has a canonical countably additive companion `R` and densities `f_A` with
  \[
  P_n(A)=E_R[f_A\mid\mathscr F_n],
  \qquad
  \inf_{C\in\mathcal C}P(A\triangle C)
  =\int\min(f_A,1-f_A)\,dR;
  \]
- one positive-defect CHT witness amplifies to continuum many, so Nielsen Theorem 4 is equivalent to `Delta_CHT>0`.

This run now rules out the strongest immediate constructive repair:

> **No nontrivial convexification of the valid KPS one-limit-point ultrafilter family can supply the missing positive-defect CHT witness.**

The remaining obligation is still source-level and binary:

\[
\boxed{
\text{either construct one source-admissible CHT }P\text{ with }D(P)>0,
\quad\text{or prove CHT forces }D(P)=0\text{ for every }P.
}
\]

Theorem 5.1 says that any positive construction must leave the atom-protected one-limit-point architecture in an essential way. The most plausible constructive escape is a distributed/Stone-fiber architecture with no positive free-charge family of distinguished points that can be isolated by shrinking cylinders. The most plausible negative route is to prove a general extremality principle: CHT forces the local finite-information extension kernels behind every `f_A` to be `{0,1}`-valued almost everywhere.

I do not claim either of those statements here.

## 9. Next methods if the metric remains stuck

The current successor has only one unchanged run, so the Section-I stuck protocol does not trigger yet. The next nonrepeating attacks recorded are:

- **#1 CHANGE THE CATEGORY:** move the companion-density formulation to the Stone space of the Borel Boolean algebra over the clopen Stone quotient; ask whether CHT forces conditional fiber measures to be Dirac;
- **#19 MAKE IT AN ALGORITHM:** build the two-sided posterior-threshold sequential classifier and determine whether CHT makes the undecided region vanish in `P`-mass;
- **#27 SWAP THE QUANTIFIERS:** compare the source's per-event/per-threshold CHT continuity with a single common family of thresholds, looking for a uniformization strong enough to force approximation or weak enough to permit a witness.

If `W_CHT` stays unchanged for three consecutive successor runs, the next invocation must use the full thinking-only stuck report protocol rather than append another local lemma.

## 10. Runtime/model-control truth

This invocation identifies as **GPT-5.6 Sol**, not GPT-6. Authenticated reasoning-effort telemetry is not exposed, so the actual reasoning level is **UNVERIFIED**. I therefore do not claim GPT-6 or maximum reasoning.

The operative implementation record still documents title/prompt, schedule/timing and enabled-state controls, but no binding model-family selector, no reasoning-effort selector, no authenticated applied-run model/effort telemetry and no guaranteed one-hour execution control. It also records the historical P26 `You cannot modify this task` response and a later successful modification from another authorized context. The lawful route to binding GPT-6/maximum is therefore an owner/admin/product/backend surface that exposes persistent model/reasoning controls and attested runtime metadata, not a worker-side permission bypass. No scheduler or permission change was attempted in this run.

## 11. Structured ledger delta

```yaml
ledger_delta:
  track: R06
  lane: "CLOSABLE OUTSIDE"
  active_source: "Khan-Pedersen-Stinchcombe 2026 / Nielsen Theorem 4 / arXiv:2609.20683v1"
  canonical_claim: "operations/claims/KPS-2026-NIELSEN-THEOREM4.md"
  source_question: "Are there uncountably many source-admissible probability functions with CHT but without the approximation property?"
  frozen_metric: "W_CHT = width of certified interval for Delta_CHT"
  metric_before: "1/2"
  metric_after: "1/2"
  movement: "NO MOVEMENT"
  unchanged_count_before: 0
  unchanged_count_after: 1
  status: "OPEN / PARTIAL"
  tried_moves: [5, 11, 29]
  new_claims:
    - "General one-limit-point no-go: if the free distinguished-index charge is non-{0,1}-valued and distinguished atoms are lambda-full, CHT fails."
    - "Quantitative CHT gap >= alpha*q for a charge set of mass q in (0,1)."
    - "CHT is nonconvex on the valid KPS Theorem-7.3 ultrafilter family: any nontrivial convex mixture of two distinct same-data ultrafilter endpoints fails CHT."
  finite_checker: "NOT APPLICABLE — analytic theorem, no finite computational core"
  remaining_obligation: "Construct one source-admissible CHT probability with D(P)>0, or prove CHT implies D(P)=0 universally."
  next_moves: [1, 19, 27]
  audits:
    P26: "NONE FOR THIS NEW THEOREM/SOURCE PACKAGE"
    second_other_track: "NONE"
  historical_i0056:
    metric: "0 -> 0"
    status: "frozen subtarget PROVED/audit-complete; full Lyons-Peres Q6.20 PARTIAL; rotated and not reopened"
  literature_check_date: "2026-09-18"
  literature_result: "official arXiv still v1 and explicitly leaves Nielsen Theorem 4 undecided; bounded fresh searches found no later source-matching resolution"
```

No shared root, peer file, claim file, scheduler, email, Drive object, permission, purchase, or public posting was modified by this run.
