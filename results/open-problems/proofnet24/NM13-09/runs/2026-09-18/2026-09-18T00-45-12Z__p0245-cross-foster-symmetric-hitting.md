Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — not GPT-6 maximum. NO FROZEN-METRIC MOVEMENT: `R_Cayley4: 1 -> 1`; Section-B methods actually tried this run: #3, #12, #25.**

# NM13-09 — P0245: cross-Foster reduction and the symmetric-hitting four-state class

Date: 2026-09-18 UTC  
Track / namespace: `NM13-09` / `proofnet24/NM13-09/`  
Category: CLOSABLE OUTSIDE  
Repository / branch: private `yspennstate/math-open-problems` / `master`

## 1. Continuity, ownership, and controlling state

This run continues the already admitted **P0245 — Aldous–Fill Open Problem 6.30** assignment. It does not reopen intake and it does not create a second claim.

I reread or targeted-recovered the required controlling and continuity surfaces before the attack:

- `FLEET_RULES.md`;
- `operations/new_methods_2026-09-16/OWNER_DIRECTIVE.md`;
- `operations/NEW_METHODS_2026-09-16.md`;
- later owner-authorized amendment `operations/NM13_DEPLOYMENT_2026-09-17T203709Z.md`;
- root `QUEUE.md`, `POSTED.md`, and `RESULTS.md`;
- `probability_campaign_2026_09/INDEX.md` and `RANKING.md`;
- canonical claim `operations/claims/P0245.md`;
- newest own report `proofnet24/NM13-09/runs/2026-09-17/2026-09-17T23-41-09Z__p0245-s3star4-dirichlet.md`;
- newest visible neighboring NM13-08 and NM13-10 reports;
- targeted P0245 source/intake/attempt/claim searches, including the Codex catalog and dedup index.

Large catalog/JSONL objects can be connector-truncated when fetched wholesale, so this is a targeted continuity recovery keyed by exact source ID, canonical dedup key, and claim path rather than a claim that every repository byte was rendered in one response.

Exclusive ownership is unchanged:

- source / claim ID: **P0245**;
- owner: **NM13-09**;
- canonical dedup key: `exact_minimum_stationary_cover_time_for_reversible_chains`;
- SHA256: `642682b0fbba364a68d451232e8378be7074f75d1a8a86e5cff4b8037577e6fe`;
- shard residue: `8 mod 13`;
- claim: `operations/claims/P0245.md`.

No release, conflicting owner, handoff, POSTED closure, retirement, or source-specific amendment superseding this assignment was recovered. NM13-10 remains admission-pending and therefore is not silently counted as an audit.

## 2. Exact source and fresh bounded literature status

Source: David Aldous and James Allen Fill, *Reversible Markov Chains and Random Walks on Graphs*, Chapter 6, **Open Problem 6.30**. The source asks to prove, for every irreducible reversible discrete-time chain on `n` states,

\[
\mathbb E_\pi C\ge (n-1)H_{n-1},
\]

with equality value supplied by simple random walk on the complete graph. The currently accessible text still labels this exact statement **Open Problem 6.30**.

Fresh searches on 2026-09-18 included the exact problem number and inequality, `stationary cover time reversible chain complete graph`, and the new mechanism terms `symmetric hitting times`, `effective resistance`, `opposite edges`, and `Foster`. They recovered later stationary-cover-time work such as Rivera–Sauerwald–Sylvester on multiple walks, and the established literature on graphs with symmetric hitting times (notably Chang–Xu, 2017), but no source-matching proof/counterexample to Open Problem 6.30 and no paper found in this bounded search stating the four-vertex cross-Foster inequality proved below. This is **bounded negative evidence only**, not a worldwide-openness or publication-novelty certificate. The symmetric-hitting class itself is established literature; no novelty is claimed for that terminology or its standard hitting-time identities.

## 3. Frozen metric and counters

The admitted metric remains

\[
R_{\mathrm{Cayley},4}
=\inf\frac{\mathbb E_\pi C}{11/2}
\]

over reversible translation-invariant four-state chains, with source hypotheses retained.

It was solved exactly at admission and is not replaced by a new quantity merely because the present work attacks a larger class.

- **Before:** `1`.
- **After:** `1`.
- **Movement:** none.
- **Consecutive unchanged runs since metric movement:** `2`.
- **Stuck recoveries used:** `0`.

P0245 remains **OPEN / NM13-09 PARTIAL**. This is not yet a Section-I stuck run: only two consecutive no-movement runs have accumulated.

## 4. New idea before code

The preceding run reduced the loopless four-state source inequality to the last discovery stage. Write

\[
\tau_m=\min\{t:\lvert\{X_0,\dots,X_t\}\rvert=m\},
\qquad
D_j=\mathbb E(\tau_{j+1}-\tau_j),\quad j=1,2,3.
\]

For a loopless chain, `D1=1`. The previous exact Dirichlet argument proved `D2 >= 3/2`. Thus the source bound follows if one can prove

\[
D_3\ge 3.
\tag{4.1}
\]

Equivalently, with `S_k=sum_{|A|=k} E_pi T_A`,

\[
S_1-2S_2=D_3-3,
\]

so the proposed stronger inequality `S1 >= 2 S2` is exactly (4.1).

The new route is to stop expanding six hitting times separately. In a loopless four-state chain, the **unordered last pair is already determined by the first edge traversed**. That gives an exact conservation law for the last-pair mass. Combining it with the commute identity turns the symmetric part of `D3` into a new tetrahedral effective-resistance sum. That sum admits a short exact polynomial / spanning-forest proof with lower bound `3`. What remains in the fully asymmetric case is one explicit Dirichlet cross-energy.

This separates the genuine obstruction from the part that is already forced by reversibility.

## 5. Setup

Let the state set be `{0,1,2,3}` and let a loopless reversible chain be represented by symmetric conductances

\[
w_{ij}=w_{ji}\ge0,\qquad d_i=\sum_{j\ne i}w_{ij},
\qquad W=\sum_i d_i.
\]

The transition law and stationary law are

\[
P_{ij}=\frac{w_{ij}}{d_i},\qquad \pi_i=\frac{d_i}{W}.
\]

The graph of positive conductances is assumed connected. Let `H_ij=E_i T_j`, let `R_ij` be effective resistance, and let `tau` be the weighted spanning-tree polynomial. For a pair `{i,j}`, let `F_ij` be the weighted sum of spanning two-forests separating `i` and `j`. Then

\[
R_{ij}=\frac{F_{ij}}{\tau},
\qquad
H_{ij}+H_{ji}=W R_{ij}.
\tag{5.1}
\]

For an edge `e={i,j}`, write `e*` for the opposite vertex-pair in the tetrahedron: `01* = 23`, `02* = 13`, `03* = 12`, and conversely.

## 6. Method #12 — the conserved unordered last-pair mass

### Lemma `NM13-09-P0245-LASTPAIR-03A`

For distinct `k,l`, let `{a,b}` be the complementary pair. Then

\[
\boxed{
\Pr(\{\text{third state},\text{last state}\}=\{k,l\})
=\frac{2w_{ab}}{W}.
}
\tag{6.1}
\]

### Proof

Because the chain is loopless, `X_1 != X_0`. Therefore after one step exactly two distinct states have been seen, namely the endpoints of the first transition. The unordered last pair is `{k,l}` if and only if that first transition traverses the complementary edge `{a,b}`. Starting from stationarity and using reversibility,

\[
\Pr(X_0=a,X_1=b)+\Pr(X_0=b,X_1=a)
=\pi_aP_{ab}+\pi_bP_{ba}
=\frac{2w_{ab}}{W}.
\]

This proves (6.1). `square`

This conservation law is exact and uses no assumption of vertex transitivity, regularity, or symmetric hitting times.

## 7. Method #25 — a cross-Foster inequality on the weighted tetrahedron

### Theorem `NM13-09-P0245-CROSSFOSTER4-03B`

For every connected nonnegative weighted graph on four labeled vertices,

\[
\boxed{
\sum_{e} w_e R_{e^*}\ge 3.
}
\tag{7.1}
\]

The sum runs over all six unordered edges of the ambient `K4`; zero conductances are allowed.

### Proof

Write

\[
a=w_{01},\ b=w_{02},\ c=w_{03},\ d=w_{12},\ e=w_{13},\ f=w_{23}.
\]

By the all-minors matrix-tree theorem, `R_ij=F_ij/tau`. Enumerating the sixteen spanning trees and the separating two-forests gives the exact identity

\[
\begin{aligned}
\tau\left(\sum_e w_eR_{e^*}-3\right)
={}&(b+e+c+d)(a-f)^2\\
&+(a+f+c+d)(b-e)^2\\
&+(a+f+b+e)(c-d)^2\\
&-3(a-f)(b-e)(c-d).
\end{aligned}
\tag{7.2}
\]

Put

\[
A=a+f,\quad B=b+e,\quad C=c+d,
\qquad
x=a-f,\quad y=b-e,\quad z=c-d.
\]

Then the right side of (7.2) is

\[
Q=(B+C)x^2+(A+C)y^2+(A+B)z^2-3xyz.
\tag{7.3}
\]

If `xyz <= 0`, every term in the quadratic part is nonnegative and `-3xyz >= 0`, so `Q >= 0`.

If `xyz > 0`, AM–GM gives

\[
(B+C)x^2+(A+C)y^2+(A+B)z^2
\ge
3\bigl((A+B)(A+C)(B+C)x^2y^2z^2\bigr)^{1/3}.
\]

Since `|x|<=A`, `|y|<=B`, `|z|<=C`, we have `xyz<=ABC`; and

\[
(A+B)(A+C)(B+C)\ge ABC.
\]

Hence the cube root is at least `xyz`, proving that the quadratic part is at least `3xyz`. Thus again `Q>=0`. Since connectedness gives `tau>0`, (7.1) follows. `square`

### Double-count interpretation

Equation (7.2) is not an unexplained symbolic accident. Multiplying `R_{e*}` by `tau` counts weighted spanning two-forests separating the opposite pair. Equivalently, one can group the tetrahedron's spanning trees into opposite-edge path pairs. The differences within those pairs create the three square terms in (7.2); the residual orientation term is exactly the cubic `-3xyz`. This is the #25 route: the same weighted forest objects are counted once through effective resistance and once through the opposite-edge decomposition.

## 8. Method #3 — a complete larger special class

The attack on the stronger statement `D3>=3` does not close the arbitrary loopless four-state case in this run. It does, however, close a natural class strictly broader than the already solved Cayley class.

### Theorem `NM13-09-P0245-SYMHIT4-03C`

Let `(X_t)` be an irreducible loopless reversible Markov chain on four states, started from stationarity. Assume its hitting times are symmetric:

\[
H_{ij}=H_{ji}\qquad\text{for all }i,j.
\tag{8.1}
\]

Then

\[
\boxed{\mathbb E_\pi C\ge\frac{11}{2}.}
\tag{8.2}
\]

### Proof

We already have `D1=1`. The previous run's all-two-target Dirichlet argument gives

\[
D_2\ge\frac32.
\tag{8.3}
\]

For completeness, its core is the matrix inequality

\[
\mathbb E_\pi T_A
=\pi_B^\top L_B^{-1}\pi_B
\ge \frac{\pi(B)^2}{Q(B,A)}
\]

for every two-set `A` with complement `B`; summing over all six two-sets gives `S2>=9/2`, and `S2=3D1+D2` yields (8.3).

Now fix a possible unordered last pair `{k,l}`, and write `{a,b}` for its complement. By Lemma 03A its probability is `2w_ab/W`. Once the third state is reached, the chain is at either `k` or `l`, with the other one still unseen. Under (8.1), either orientation has the same expected remaining time. By the commute identity,

\[
H_{kl}=H_{lk}=\frac{W R_{kl}}2.
\]

Therefore this unordered pair contributes exactly

\[
\frac{2w_{ab}}W\cdot\frac{W R_{kl}}2
=w_{ab}R_{kl}
\]

to `D3`. Summing over the six complementary pairs and applying Theorem 03B,

\[
D_3=\sum_e w_eR_{e^*}\ge3.
\]

Consequently

\[
\mathbb E_\pi C=D_1+D_2+D_3
\ge 1+\frac32+3=\frac{11}{2}.
\]

This proves (8.2). `square`

The class `H_ij=H_ji` is not invented terminology: graphs/chains with symmetric hitting times have an existing literature. What is asserted here is only the above source-specific four-state implication, with publication novelty **UNVERIFIED**.

## 9. Exact reduction of the remaining loopless four-state obstruction

The same calculation isolates the only term not controlled by Cross-Foster in the fully asymmetric case.

For vertex `i`, let `r_i` be the weighted spanning-tree polynomial of the induced three-vertex graph obtained by deleting `i`. For pair `{k,l}` with complement `{a,b}`, let

\[
h_x=\Pr_x(T_k<T_l),\qquad x\in\{a,b\}.
\]

The two-vertex Dirichlet system, or equivalently the rooted two-forest formula, gives

\[
\boxed{
h_a+h_b-1=\frac{r_l-r_k}{F_{kl}}.}
\tag{9.1}
\]

Let

\[
\psi_i=\frac12\sum_z d_zR_{iz}.
\]

Tetali's hitting-time identity gives

\[
H_{kl}-H_{lk}=2(\psi_l-\psi_k).
\tag{9.2}
\]

The ordered last-pair probabilities are

\[
\mu_{kl}=\frac{w_{ab}}W(h_a+h_b),
\qquad
\mu_{lk}=\frac{w_{ab}}W(2-h_a-h_b).
\]

Using (9.1), (9.2), and the commute identity, the contribution of `{k,l}` to `D3` is exactly

\[
\mu_{kl}H_{kl}+\mu_{lk}H_{lk}
=
 w_{ab}R_{kl}
 +\frac{2w_{ab}}{W F_{kl}}(r_l-r_k)(\psi_l-\psi_k).
\tag{9.3}
\]

Therefore

\[
\boxed{
D_3
=
\sum_e w_eR_{e^*}
+\frac2W\sum_{k<l}c^*_{kl}(r_l-r_k)(\psi_l-\psi_k),
}
\tag{9.4}
\]

where

\[
c^*_{kl}=\frac{w_{ab}}{F_{kl}}\ge0
\]

and `{a,b}` is the pair opposite `{k,l}`.

The first term is now rigorously at least `3`. Thus the arbitrary loopless `n=4` source problem is reduced to the sign of the explicit tetrahedral cross-energy

\[
\mathcal E_*(r,\psi)
:=\sum_{k<l}c^*_{kl}(r_l-r_k)(\psi_l-\psi_k).
\tag{9.5}
\]

Symmetric hitting times make `psi` constant, so this term vanishes and Theorem 03C follows. I did **not** prove `E_*(r,psi)>=0` in full generality here, and therefore I do not call the arbitrary loopless four-state case solved.

This is the precise failure of method #3: the stronger inequality has been reduced to one exact cross-energy sign, but that sign is not yet certified for all positive conductances.

## 10. Section-B accounting

### #3 — PROVE SOMETHING STRONGER

Attempted the stronger `S1>=2S2`, equivalently `D3>=3`. Outcome: **partial success**. It is proved for the entire symmetric-hitting loopless four-state class, and the general case is reduced exactly to (9.5). No claim is made beyond that.

### #12 — FIND WHAT IS CONSERVED

Outcome: **success**. The unordered last-pair probability is exactly the stationary mass of the complementary first edge, equation (6.1). This removes all discovery-order ambiguity from the symmetric part of the last stage.

### #25 — COUNT THE SAME THING TWICE

Outcome: **success**. Effective resistance via separating two-forests and a second grouping by opposite tetrahedral edges yield the exact cross-Foster identity (7.2), hence the universal lower bound (7.1).

These three methods were not the previous run's triple (#11/#15/#30).

## 11. Exact self-check

Only after the above identities and proof route were obtained, I wrote a small exact symbolic self-check:

- `proofnet24/NM13-09/artifacts/2026-09-18/p0245_cross_foster_check.py`
- `proofnet24/NM13-09/artifacts/2026-09-18/p0245_cross_foster_check.out`

The script independently constructs the weighted Laplacian and separating two-forest polynomials, verifies for all six pairs that the killed `2x2` determinant equals `F_kl`, verifies the exact harmonic-bias identity behind (9.1), and verifies (7.2) coefficient-for-coefficient. The archived output ends

`ALL_EXACT_CHECKS_PASS`.

This is explicitly a **self-check**, not an independent P26 or NM13-10 audit.

Artifact commits:

- checker: `fadcb1c1fa549d1541448cd33df251ee98369375`;
- archived output: `c1c65d74bf62c66dddb27892b7c5c2bf6452dc35`.

Both files were read back at their returned commits in this invocation.

## 12. Literature / prior-art interpretation

The source text still presents Open Problem 6.30 as open. The bounded current search did not recover a source-matching resolution. Rivera–Sauerwald–Sylvester's later work uses general stationary-cover-time lower bounds for multiple walks rather than proving the exact Aldous–Fill single-chain extremal constant. Chang–Xu and related work show that symmetric hitting times are a studied graph class, so the class mechanism itself must not be advertised as new.

I did not recover a reference for the exact opposite-edge inequality

\[
\sum_e w_eR_{e^*}\ge3
\]

on a weighted tetrahedron or for its use in this cover-time problem. That search was bounded and **publication novelty remains UNVERIFIED**.

## 13. Status, next route, and audits

Source status: **OPEN**.  
NM13-09 status: **PARTIAL**.  
P26 audit: **not requested / not passed**.  
NM13-10 audit: **not requested / not passed**.

The next route is the exact remaining sign problem (9.5), not another certificate for the already solved frozen Cayley metric. The next untried Section-B methods are:

- **#5 ADD A PARAMETER AND DIFFERENTIATE:** interpolate from the opposite-edge symmetrization to the given tetrahedral network and differentiate `E_*(r,psi)` or `D3`;
- **#14 FIND THE GROUP ACTING:** quotient the six conductances by the tetrahedral `S4` action and opposite-pair coordinates `(A,B,C;x,y,z)` before any algebra;
- **#18 SAY IT IN ANOTHER LANGUAGE:** reinterpret (9.5) as a Dirichlet cross-form on the dual tetrahedral conductances `c^*`, looking for a positive operator mapping `r` to `psi`.

A third consecutive no-movement run would bring the frozen metric to the stuck threshold; the following invocation must then obey the Section-I thinking-run protocol rather than manufacture another restricted lemma.

## 14. Model / task-control status

The current exposed task-control surface still provides prompt/title, timing/schedule, timing mode, and enabled-state controls but **no binding model-family field and no reasoning-effort field**. Therefore `GPT-6 / maximum` remains prompt text only in this runtime. Enforcing it requires an owner-authorized product/workspace/API scheduler surface that actually exposes model and reasoning selectors; a repository edit cannot bind those settings.

The historical P26 `You cannot modify this task` result remains best interpreted as context-specific authorization: current repository continuity records a later successful authorized P26 update. The lawful workaround for a future refusal is the owning/authorized product or workspace/admin surface (or a platform capability change), not cloning the task, bypassing permissions, or silently disabling it. No schedule was created or modified in this invocation.

## 15. Structured ledger delta for P26

```yaml
ledger_delta:
  worker: NM13-09
  category: CLOSABLE_OUTSIDE
  run_status: PARTIAL
  source_id: P0245
  source_title: Exact minimum stationary cover time for reversible chains
  canonical_dedup_key: exact_minimum_stationary_cover_time_for_reversible_chains
  shard_residue: 8
  claim_path: operations/claims/P0245.md
  source_status: OPEN
  worker_status: PARTIAL
  metric_name: R_Cayley4
  metric_before: 1
  metric_after: 1
  movement: false
  methods_attempted: [3, 12, 25]
  method_outcomes:
    3: "stronger D3>=3 proved for symmetric-hitting loopless n=4; general case reduced to explicit cross-energy"
    12: "exact unordered last-pair conservation 2*w_opposite/W"
    25: "cross-Foster two-forest identity and lower bound sum_e w_e R_e* >= 3"
  new_claim_ids:
    - NM13-09-P0245-LASTPAIR-03A
    - NM13-09-P0245-CROSSFOSTER4-03B
    - NM13-09-P0245-SYMHIT4-03C
  exact_checker: proofnet24/NM13-09/artifacts/2026-09-18/p0245_cross_foster_check.py
  checker_commit: fadcb1c1fa549d1541448cd33df251ee98369375
  exact_output: proofnet24/NM13-09/artifacts/2026-09-18/p0245_cross_foster_check.out
  output_commit: c1c65d74bf62c66dddb27892b7c5c2bf6452dc35
  self_check_result: ALL_EXACT_CHECKS_PASS
  p26_audit: NOT_REQUESTED
  secondary_audit_partner: NM13-10
  secondary_audit: NOT_REQUESTED
  unchanged_runs_since_metric_movement: 2
  stuck_recoveries_used: 0
  next_methods: [5, 14, 18]
  next_step: "decide the sign of the explicit dual-tetrahedron cross-energy E_*(r,psi); do not redefine the frozen metric"
```
