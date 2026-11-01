Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — not GPT-6 maximum. NO FROZEN-METRIC MOVEMENT: `R_Cayley4: 1 -> 1`; Section-B methods actually tried: #8, #16, #23. New source-relevant PARTIAL theorem: on the positive loopless four-state one-axis opposite-edge-imbalance class, the residual cross-energy is exactly nonnegative, hence the Aldous–Fill Open Problem 6.30 bound `E_pi C >= 11/2` holds on that class.**

# NM13-09 — P0245: exact one-axis cross-energy and a larger four-state class

Date: 2026-09-18 UTC  
Track / namespace: `NM13-09` / `proofnet24/NM13-09/`  
Category: `CLOSABLE OUTSIDE`  
Repository / branch: private `yspennstate/math-open-problems` / `master`  
Source / claim: `P0245`, `operations/claims/P0245.md`

## 1. Runtime/control disclosure

The task prompt requests GPT-6 with maximum reasoning. This invocation actually identifies as **GPT-5.6 Sol**. No authenticated reasoning-effort telemetry is exposed, so the reasoning level is **UNVERIFIED**. I do not claim GPT-6, a binding maximum-reasoning setting, or an hour-long execution.

The exposed task-control surface still has prompt/title, schedule/relative-start, timing-mode, enabled-state, and ordinary task-update fields, but **no bindable model-family selector and no bindable reasoning-effort selector**. Thus GPT-6/maximum remains prompt text only. Making it binding would require an owner-authorized product/workspace/API/admin surface exposing those controls together with per-run attestation. The historical P26 `You cannot modify this task` result is authorization-context-specific: repository policy records a later successful P26 update from another authorized context. The lawful workaround for a denied edit is the owning/authorized surface or platform support, not duplication or access-control bypass. No schedule, workflow, permission, email, Drive item, or public surface was changed in this run.

## 2. Continuity and ownership recovered before research

This run continues the already admitted P0245 assignment. It does **not** reopen intake and it does not create or overwrite a claim.

I reread or targeted-recovered the required current state before mathematics:

- `FLEET_RULES.md`;
- `operations/new_methods_2026-09-16/OWNER_DIRECTIVE.md`;
- `operations/NEW_METHODS_2026-09-16.md`;
- later owner-authorized amendment `operations/NM13_DEPLOYMENT_2026-09-17T203709Z.md`;
- root `QUEUE.md`, `POSTED.md`, and `RESULTS.md`;
- `probability_campaign_2026_09/INDEX.md` and `RANKING.md`;
- canonical claim `operations/claims/P0245.md`;
- newest own report `proofnet24/NM13-09/runs/2026-09-18/2026-09-18T03-12-49Z__p0245-stuck-recovery-1.md`;
- the preceding cross-Foster and Walsh/cross-energy P0245 reports;
- newest visible neighboring reports `proofnet24/NM13-08/runs/2026-09-18/2026-09-18T02-39-30Z__p0408-distance-two-resonance-null.md` and `proofnet24/NM13-10/runs/2026-09-18/2026-09-18T02-54-00Z__admission-delta-screen-7.md`;
- the historical exact-functional attempt `prob1000_lean_20260908/p0245.py`;
- current P0245 claim/dedup/attempt/audit/handoff searches and the intake dedup index.

The append-only intake/catalog files are too large to pretend every byte was rendered through the connector in one response. I therefore recovered continuity by exact source ID, canonical key, claim path, historical attempt, and current searches. No material P0245 history needed for this run was inaccessible.

Exclusive ownership remains:

- source / claim ID: **P0245**;
- owner: **NM13-09**;
- canonical dedup key: `exact_minimum_stationary_cover_time_for_reversible_chains`;
- SHA256: `642682b0fbba364a68d451232e8378be7074f75d1a8a86e5cff4b8037577e6fe`;
- shard residue: `8 mod 13`;
- canonical claim: `operations/claims/P0245.md`.

No release, current competing owner, handoff, retirement, `POSTED.md` closure, campaign closure, or passed P0245 audit was recovered. NM13-10 remains admission-pending and is not counted as an audit. P26 is likewise not counted as an audit.

## 3. Exact source and fresh bounded literature check

Source: David Aldous and James Allen Fill, *Reversible Markov Chains and Random Walks on Graphs*, Chapter 6, section 6.6.4, **Open Problem 6.30**. The current Berkeley HTML source still states:

\[
\boxed{\mathbb E_\pi C\ge (n-1)h_{n-1}}
\]

for every reversible chain on `n` states, with the right side the complete-graph value. The source itself distinguishes this exact finite conjecture from Feige's asymptotic theorem for unweighted graphs.

Fresh searches dated **2026-09-18** used the exact problem number, the displayed inequality, `minimum stationary cover time reversible Markov chain complete graph`, `four-state reversible cover time`, and the present mechanism terms `opposite edge`, `effective resistance`, `cross energy`, and `spanning forest`. The search recovered the current Aldous–Fill source and Feige's 1995 asymptotic unweighted-graph lower bound, plus unrelated approximation and cover-time literature, but no source-matching proof/counterexample and no reference found in this bounded pass for the exact one-axis formula proved below.

This is **bounded negative evidence only**, not proof of worldwide openness and not a publication-novelty certificate. The matrix-tree theorem, effective-resistance identities, Tetali hitting-time identity, and Dirichlet methods used in the reduction are standard machinery.

## 4. Frozen metric and policy counters

The admitted metric remains exactly

\[
R_{\mathrm{Cayley},4}
=\inf_{\substack{\text{irreducible reversible}\\
\text{translation-invariant }|G|=4}}
\frac{\mathbb E_\pi C}{11/2}.
\]

It was proved exactly at admission and is not replaced by a broader-class flag.

- **Before:** `1`.
- **After:** `1`.
- **Movement:** none.
- **Consecutive unchanged runs since metric movement:** `5`.
- **Stuck recoveries used:** `1`.
- Parent source: **OPEN**.
- NM13-09 status: **PARTIAL**.

This run executes the previous Section-I recovery choice: try to refute the stronger residual sign before spending more time proving it. One more unchanged P0245 invocation remains before the CLOSABLE six-run rotation gate. If that next invocation does not close the source or otherwise legitimately move the frozen quantity, it must preserve a handoff and rotate; there must not be a seventh unchanged P0245 research run.

## 5. Recovered exact reduction

Use the loopless four-state conductance notation

\[
a=w_{01},\quad b=w_{02},\quad c=w_{03},\quad
 d=w_{12},\quad e=w_{13},\quad f=w_{23},
\]

and let `W=sum_i d_i`, `tau` be the weighted spanning-tree polynomial, `F_kl` the separating two-forest polynomial, `R_kl=F_kl/tau`, and `r_i` the spanning-tree polynomial after deleting vertex `i`. Put

\[
\psi_i=\frac12\sum_z d_zR_{iz}.
\]

The previous exact reports proved, for arbitrary positive loopless four-state reversible chains,

\[
D_1=1,\qquad D_2\ge\frac32,
\tag{5.1}
\]

and

\[
D_3
=\sum_e w_eR_{e^*}+\frac2W\mathcal E_*(r,\psi),
\tag{5.2}
\]

where `e*` is the opposite vertex pair and

\[
\mathcal E_*(r,\psi)
=\sum_{k<l}\frac{w_{ab}}{F_{kl}}
(r_l-r_k)(\psi_l-\psi_k),
\tag{5.3}
\]

with `{a,b}` complementary to `{k,l}`. It also proved the exact cross-Foster identity. Write opposite-edge sums and imbalances

\[
A=a+f,\quad B=b+e,\quad C=c+d,
\qquad x=a-f,\quad y=b-e,\quad z=c-d.
\tag{5.4}
\]

Then

\[
\tau\left(\sum_e w_eR_{e^*}-3\right)
=(B+C)x^2+(A+C)y^2+(A+B)z^2-3xyz.
\tag{5.5}
\]

The previous stuck recovery identified the simplest analytically unresolved slice as `y=z=0` and instructed this run to try to falsify (5.3) there before attempting another proof lemma.

## 6. Method #8 — DISCRETIZE: attack the sign before trusting it

I first treated (5.3) as potentially false and evaluated it with exact rational arithmetic on two symmetry-unreduced finite grids, solely to decide whether the proposed proof route deserved symbolic work.

The archived checker enumerates every connected primitive six-edge vector in:

- positive weights `{1,2,3,4}^6`: **4031** cases, no negative `E_*`;
- boundary weights `{0,1,2,3}^6`: **3758** connected primitive cases, no negative `E_*`.

Both scans attain zero. These facts are exact finite computations, but they are explicitly **route diagnostics, not a continuous theorem** and not movement of the frozen metric. The output says this in capital letters so the finite scan cannot later be mistaken for a proof over the conductance cone.

The useful conclusion was methodological: the simplest refutation was not sitting on the first rational strata, so the next step should eliminate the one-axis slice exactly rather than create a denser grid.

## 7. Method #16 — COMPUTE EVERY SMALL CASE, THEN READ THE ALGEBRA

The finite scan suggested that the balanced locus is not hiding an immediately adjacent negative pocket. Instead of enumerating more points, I substituted the full one-axis family into the exact forest formula.

Set

\[
 y=z=0,
\qquad
 a=\frac{A+x}{2},\quad f=\frac{A-x}{2},
\quad b=e=\frac B2,\quad c=d=\frac C2,
\tag{7.1}
\]

with

\[
A,B,C>0,\qquad |x|<A.
\tag{7.2}
\]

Thus all six conductances are strictly positive. Define

\[
T=A+B+C,\qquad U=T^2-x^2,
\qquad V=A^2+A(B+C)+BC-x^2.
\tag{7.3}
\]

Direct exact elimination of the six separating-forest denominators gives the identity

\[
\boxed{
\mathcal E_*
=
\frac{2(B+C)x^2\bigl(U^2-B^2C^2\bigr)}
{(U-B^2)(U-C^2)V}.}
\tag{7.4}
\]

This is not numerical interpolation: the exact checker constructs the weighted Laplacian, all six two-forest polynomials, all four deletion-tree polynomials, the resistance-potential numerators, and (5.3), and then verifies coefficient-for-coefficient that subtracting the right side of (7.4) has zero numerator.

The same self-check gives the rational spot value

\[
(A,B,C,x)=(5,3,2,1)
\quad\Longrightarrow\quad
\mathcal E_* = \frac{217}{1045}>0.
\]

## 8. Method #23 — assume the stronger stagewise inequality is false

The previous stuck recovery deliberately asked this run to assume the proposer-facing stronger route might be wrong. Formula (7.4) answers that negation on the first unresolved slice: **there is no negative one-axis witness**.

### Theorem `NM13-09-P0245-ONEAXIS-05`

Let `(X_t)` be an irreducible loopless reversible Markov chain on four states, started from stationarity, whose six conductances have the form (7.1) with (7.2). Equivalently, two opposite edge pairs are balanced (`b=e` and `c=d`) while the third opposite pair may be imbalanced. Then

\[
\boxed{\mathcal E_*(r,\psi)\ge0,}
\tag{8.1}
\]

with equality in the positive family only when `x=0`. Consequently

\[
\boxed{\mathbb E_\pi C\ge\frac{11}{2}.}
\tag{8.2}
\]

Thus Aldous–Fill Open Problem 6.30 holds for this complete one-axis positive loopless four-state class.

### Proof

Start from the exact identity (7.4). Under `|x|<A`, every denominator factor is strictly positive. Indeed,

\[
\begin{aligned}
U-B^2
&>(A+B+C)^2-A^2-B^2\\
&=C^2+2AB+2AC+2BC>0,
\end{aligned}
\]

and similarly

\[
U-C^2>B^2+2AB+2AC+2BC>0.
\]

Also

\[
V=(A^2-x^2)+A(B+C)+BC>0.
\]

Finally

\[
\begin{aligned}
U-BC
&>(A+B+C)^2-A^2-BC\\
&=B^2+BC+C^2+2A(B+C)>0,
\end{aligned}
\]

so `U>BC>0` and therefore

\[
U^2-B^2C^2=(U-BC)(U+BC)>0.
\]

Every factor in (7.4) is now positive except `x^2`, proving (8.1), with equality exactly at `x=0`.

For the cover-time bound, the exact cross-Foster identity (5.5) simplifies on the same slice to

\[
\tau\left(\sum_e w_eR_{e^*}-3\right)
=(B+C)x^2\ge0.
\tag{8.3}
\]

Since `tau>0`, equations (5.2), (8.1), and (8.3) give

\[
D_3\ge3.
\]

Combining this with the already proved all-loopless-four-state bounds (5.1),

\[
\mathbb E_\pi C=D_1+D_2+D_3
\ge1+\frac32+3
=\frac{11}{2}.
\]

This proves (8.2). `square`

The theorem is deliberately labeled **PARTIAL** relative to P0245: it treats a four-state positive loopless class, not arbitrary four-state reversible chains, chains with self-loops, or arbitrary `n`.

## 9. What this says about the failed refutation route

The Section-I recovery action was not wasted even though it did not produce a counterexample. It killed a concrete possibility: a negative cross-energy cannot occur anywhere on the entire one-axis family, including arbitrarily strong imbalance `|x|<A`. The local Hessian theorem from the prior run therefore extends globally along each coordinate axis of imbalance space.

What remains genuinely open in the present four-state route is interaction among **two or three simultaneous imbalance coordinates**. The full sign question is still

\[
\mathcal E_*(A,B,C;x,y,z)\stackrel{?}{\ge0
}
\qquad
(|x|<A,\ |y|<B,\ |z|<C),
\tag{9.1}
\]

and this report does not claim it. The bounded grids provide evidence only. A successful final P0245 run would need either an exact negative witness with source-total-slack analysis, or a global sign/total-slack mechanism that handles genuinely coupled `(x,y,z)`.

## 10. Exact self-check and archive

Only after deriving (7.4) and the proof above, I wrote and executed the exact self-check:

- `proofnet24/NM13-09/artifacts/2026-09-18/p0245_one_axis_cross_energy.py`
- `proofnet24/NM13-09/artifacts/2026-09-18/p0245_one_axis_cross_energy.out`

The script verifies the symbolic identity exactly, the rational spot value `217/1045`, and the two bounded exact grid diagnostics. The archived output ends:

`ALL_EXACT_CHECKS_PASS`

and explicitly warns that the grids are route diagnostics rather than continuous certificates.

Artifact commits:

- checker creation: `2a59ff54a32ae896d7073895557cad7d46c9caa2`;
- output archive: `37ff7d745ad23dd2aee21c3726e7c2db34c17195`.

Both artifacts were read back at their returned commits. This remains a **self-check**, not an independent audit. Neither P26 nor NM13-10 is counted as having audited P0245.

## 11. Section-B accounting

### #8 — GO THE OTHER WAY AND DISCRETIZE

**Attempted and useful as route selection, not proof.** Exact primitive integer grids over positive and connected-boundary conductances produced no negative cross-energy. This prevented premature investment in a denser numerical search and focused the run on symbolic elimination of the one-axis slice.

### #16 — COMPUTE EVERY SMALL CASE AND STARE AT THE SEQUENCE

**Attempted and converted into algebra.** Rather than file the finite scan as progress, I read its zero/nonnegative pattern as a prompt to substitute the minimal asymmetric family and eliminate the forest expressions exactly. That yielded (7.4).

### #23 — DO WHAT THE PROPOSER DID NOT EXPECT

**Attempted as the recovery's required negation attack.** I assumed the stronger stagewise sign might fail. It does not fail on the entire one-axis family: the exact factorization proves the opposite. This is a genuine outcome of the refutation-first route, not a claim that the full sign is true.

The previous run's triple was #1/#20/#24, so this run does not repeat it. These methods were not previously credited on P0245.

## 12. Next step and rotation discipline

There is room for exactly one more P0245 invocation before the CLOSABLE six-unchanged gate. The next attack should not enumerate more certificates for the same one-axis theorem. It should target the first truly coupled imbalance regime, preferably by one of two decisive outcomes:

1. derive a two-axis/global factorization or monotonicity principle that controls (9.1); or
2. find an exact negative `E_*` witness and immediately test the **full** cover-time slack, so a route counterexample is not misreported as a source counterexample.

Reserved next Section-B methods, **not tried here**, are **#6/#13/#29**: deform to a solved/boundary point, find a genuine monotone quantity if one exists, and compactify the connected boundary strata. If that next invocation leaves the frozen metric unchanged and does not close the source, it must preserve a handoff and rotate; a seventh unchanged P0245 run is forbidden.

## 13. Structured ledger delta for P26

```yaml
ledger_delta:
  worker: NM13-09
  source_id: P0245
  claim_path: operations/claims/P0245.md
  canonical_dedup_key: exact_minimum_stationary_cover_time_for_reversible_chains
  category: CLOSABLE_OUTSIDE
  source_status: OPEN
  worker_status: PARTIAL
  metric_name: R_Cayley4
  metric_before: 1
  metric_after: 1
  metric_movement: NONE
  run_kind: SUBSTANTIVE_POST_STUCK_RECOVERY
  actual_methods: [8, 16, 23]
  method_outcomes:
    8: "exact primitive positive/boundary rational grids found no negative E_*; used only as route diagnostics"
    16: "small-case pattern was converted into an exact symbolic one-axis formula rather than another grid"
    23: "negation attack fails on the entire one-axis family; exact factorization proves E_* >= 0 there"
  new_claim_ids:
    - NM13-09-P0245-ONEAXIS-05
  new_claim_scope: "positive loopless four-state chains with two balanced opposite edge pairs; E_* >= 0 and E_pi C >= 11/2"
  exact_checker: proofnet24/NM13-09/artifacts/2026-09-18/p0245_one_axis_cross_energy.py
  exact_checker_commit: 2a59ff54a32ae896d7073895557cad7d46c9caa2
  exact_output: proofnet24/NM13-09/artifacts/2026-09-18/p0245_one_axis_cross_energy.out
  exact_output_commit: 37ff7d745ad23dd2aee21c3726e7c2db34c17195
  exact_output_status: ALL_EXACT_CHECKS_PASS
  p26_audit: NOT_REQUESTED
  secondary_audit_partner: NM13-10
  secondary_audit: NOT_REQUESTED
  unchanged_runs_since_metric_movement: 5
  stuck_recoveries_used: 1
  next_methods: [6, 13, 29]
  next_step: "one final decisive P0245 attack on genuinely coupled imbalance coordinates; either prove a global/two-axis sign or find exact negative E_* and test full source slack"
  rotation_gate: "if next invocation is unchanged and source remains open, preserve handoff and rotate; no seventh unchanged P0245 research run"
  bounded_literature_check_date: 2026-09-18
  bounded_literature_result: "current Aldous-Fill source still labels OP6.30 open; Feige is asymptotic unweighted; no source-matching resolution or exact one-axis formula recovered in bounded search"
  access_limits: "bounded web/index and repository search; not a worldwide bibliographic or novelty certificate"
```
