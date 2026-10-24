Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — not GPT-6 maximum. NO FROZEN-METRIC MOVEMENT: `R_Cayley4: 1 -> 1`; Section-B methods actually tried: #4, #14, #18. New source-relevant PARTIAL theorem: the Aldous–Fill 6.30 bound `E_pi C >= 11/2` holds for every positive loopless four-state chain whose three opposite-edge sums are equal and for which one opposite pair is balanced. This is the sixth consecutive unchanged P0245 invocation, so NM13-09 records a complete handoff and rotates; there must not be a seventh P0245 research run on this track.**

# NM13-09 — P0245: equal-opposite-sum two-axis Bernstein positivity and six-run handoff

Date: 2026-09-18 UTC  
Track / namespace: `NM13-09` / `proofnet24/NM13-09/`  
Category: `CLOSABLE OUTSIDE`  
Repository / branch: private `yspennstate/math-open-problems` / `master`  
Source / claim: `P0245`, `operations/claims/P0245.md`  
Parent source status after this run: **OPEN**  
NM13-09 status after this run: **PARTIAL / HANDOFF / ROTATE**

## 1. Runtime and control disclosure

The task prompt requests GPT-6 with maximum reasoning. This invocation actually identifies as **GPT-5.6 Sol**. No authenticated reasoning-effort telemetry is exposed to this report, so the reasoning level is **UNVERIFIED**. I do not claim GPT-6, a binding maximum-reasoning setting, or an hour-long execution.

The exposed task-control surface still provides ordinary prompt/title, schedule/relative-start, timing-mode and enabled-state controls, but it exposes **no bindable model-family selector and no bindable reasoning-effort selector**. Therefore `GPT-6 / maximum` remains prompt text only. Making it enforceable would require an owner-authorized product/workspace/API/admin surface that exposes those settings together with authenticated per-run runtime attestation. The historical P26 `You cannot modify this task` response is an authorization-context boundary; the repository now records a later successful P26 update from another authorized context. A denied edit must be handled through the owning/otherwise authorized surface or platform/admin support, not by duplication or access-control bypass. No schedule, workflow, permission, email, Drive item or public surface was changed in this run.

## 2. Continuity, ownership, and required repository recovery

This invocation continues the already admitted **P0245** source. It does not reopen intake, reset the metric, create a duplicate claim, or overwrite the canonical claim.

Before mathematics I reread or targeted-recovered the owner-required current state:

- `FLEET_RULES.md`;
- `operations/new_methods_2026-09-16/OWNER_DIRECTIVE.md`;
- `operations/NEW_METHODS_2026-09-16.md`;
- later owner-authorized deployment amendment `operations/NM13_DEPLOYMENT_2026-09-17T203709Z.md`;
- root `QUEUE.md`, `POSTED.md`, and `RESULTS.md`;
- `probability_campaign_2026_09/INDEX.md` and `RANKING.md`;
- canonical claim `operations/claims/P0245.md`;
- newest own report `proofnet24/NM13-09/runs/2026-09-18/2026-09-18T03-41-23Z__p0245-one-axis-cross-energy.md` and the preceding P0245 reports needed for the exact reduction;
- newest neighboring NM13-08 report `proofnet24/NM13-08/runs/2026-09-18/2026-09-18T03-39-55Z__p0408-path-omitted-handoff.md`;
- newest neighboring NM13-10 report `proofnet24/NM13-10/runs/2026-09-18/2026-09-18T03-48-08Z__admission-delta-screen-8.md`;
- historical exact attempt `prob1000_lean_20260908/p0245.py` and the indexed canonical dedup identity;
- current exact-ID / exact-dedup-key searches for claims, attempts, handoffs and audits.

The large append-only intake/catalog JSONL files are connector-bounded when fetched wholesale. I therefore recovered continuity by exact source ID, canonical dedup key, claim path, dedup index, historical attempt, current claim searches, queue/campaign state and neighboring reports rather than pretending every historical byte was rendered. No material P0245 history needed for this run was inaccessible.

The canonical identity is unchanged:

- source / claim ID: **P0245**;
- entering owner: **NM13-09**;
- canonical dedup key: `exact_minimum_stationary_cover_time_for_reversible_chains`;
- SHA256: `642682b0fbba364a68d451232e8378be7074f75d1a8a86e5cff4b8037577e6fe`;
- shard residue: `8 mod 13`;
- canonical claim path: `operations/claims/P0245.md`.

No competing owner, release, retirement, `POSTED.md` closure, campaign closure, P26 audit pass or NM13-10 audit pass was recovered. NM13-10 remains admission-pending and is **not** counted as an audit. This report records the required six-run handoff but does not mutate the canonical claim or pretend that ownership is released by fiat; reconciliation belongs to the owner/P26/shared-state maintainer.

## 3. Exact source and fresh bounded literature check

Source: David Aldous and James Allen Fill, *Reversible Markov Chains and Random Walks on Graphs*, Chapter 6, section 6.6.4, **Open Problem 6.30**. The current Berkeley source, re-read on **2026-09-18**, still asks:

\[
\boxed{\mathbb E_\pi C\ge (n-1)h_{n-1}}
\]

for every reversible chain on `n` states, with equality at random walk on the complete graph. The source explicitly separates this exact finite conjecture from Feige's asymptotic unweighted-graph result.

Fresh bounded searches dated **2026-09-18** used the exact problem number, the displayed inequality, `stationary cover time reversible chain complete graph minimum`, `four-state reversible Markov chain cover time`, and the present algebraic mechanism terms. They recovered the current Aldous–Fill source and adjacent cover-time literature, but no source-matching resolution and no published four-state theorem matching the restricted result below.

This is **bounded negative evidence only**, not proof of worldwide openness and not a novelty certificate. The matrix-tree theorem, forest minors, effective resistance, Dirichlet/Tetali identities, Bernstein polynomials and positivity-by-nonnegative-Bernstein-coefficients are standard machinery.

## 4. Frozen metric and mandatory six-run rotation

The admitted frozen metric remains

\[
R_{\mathrm{Cayley},4}
=\inf_{\substack{\text{irreducible reversible}\\
\text{translation-invariant }|G|=4}}
\frac{\mathbb E_\pi C}{11/2}.
\]

It was already proved exactly equal to one at admission and is not replaced by a theorem count, a larger-class flag, or the cross-energy sign.

- **Before:** `1`.
- **After:** `1`.
- **Movement:** none.
- **Consecutive unchanged P0245 invocations:** `6`.
- **Stuck recoveries used:** `1`.
- Parent source: **OPEN**.
- Track result: **PARTIAL**.

This is therefore the terminal P0245 invocation for NM13-09 under the CLOSABLE six-run rule. The mathematical work below is preserved in the handoff, but **NM13-09 must not execute a seventh P0245 research run**. Its next research state is `ADMISSION_PENDING` for a different genuinely unassigned residue-8 CLOSABLE source, after ordinary ownership/source-status admission checks.

## 5. Recovered exact four-state reduction

For a positive loopless four-state reversible chain write the six conductances

\[
a=w_{01},\quad b=w_{02},\quad c=w_{03},\quad
 d=w_{12},\quad e=w_{13},\quad f=w_{23},
\]

and opposite-edge sums/imbalances

\[
A=a+f,\quad B=b+e,\quad C=c+d,
\qquad x=a-f,\quad y=b-e,\quad z=c-d.
\tag{5.1}
\]

Let `tau` be the weighted spanning-tree polynomial, `F_kl` the separating two-forest polynomial for vertices `k,l`, `R_kl=F_kl/tau`, `r_i` the spanning-tree polynomial after deleting vertex `i`, and

\[
\psi_i=\frac12\sum_z d_zR_{iz}.
\]

The preceding P0245 reports proved for arbitrary positive loopless four-state chains

\[
D_1=1,\qquad D_2\ge \frac32,
\tag{5.2}
\]

and

\[
D_3=
\sum_e w_eR_{e^*}
+\frac2W\,\mathcal E_*(r,\psi),
\tag{5.3}
\]

where `e*` is the opposite vertex pair and

\[
\mathcal E_*(r,\psi)=
\sum_{k<l}\frac{w_{ab}}{F_{kl}}
(r_l-r_k)(\psi_l-\psi_k),
\tag{5.4}
\]

with `{a,b}` complementary to `{k,l}`. The exact cross-Foster identity is

\[
\tau\left(\sum_e w_eR_{e^*}-3\right)
=(B+C)x^2+(A+C)y^2+(A+B)z^2-3xyz.
\tag{5.5}
\]

The previous invocation proved `E_*>=0` globally along every one-axis imbalance slice, for example `y=z=0`. The unresolved issue was interaction between simultaneous imbalances.

## 6. Method #14 — FIND THE GROUP ACTING: equal opposite sums and a two-axis quotient

The automorphism group of `K_4` acts on its three opposite-edge pairs as `S_3`; vertex relabelings also reverse appropriate imbalance signs. I used that action to isolate the first genuinely coupled family that is still large enough to contain two simultaneous imbalances but small enough to admit an exact positivity certificate:

\[
A=B=C=:S>0,
\qquad z=0,
\qquad |x|<S,\ |y|<S.
\tag{6.1}
\]

By the `S_3` action there is no loss in choosing the balanced opposite pair to be the `c,d` pair. Global multiplication of every conductance by a positive scalar changes time scale quantities consistently and preserves the sign of `E_*`, so normalize `S=2`. Put

\[
a=\frac{2+X}{2},\qquad f=\frac{2-X}{2},
\qquad
b=\frac{2+Y}{2},\qquad e=\frac{2-Y}{2},
\qquad c=d=1,
\tag{6.2}
\]

where `|X|,|Y|<2`. In the original variables `X=2x/S`, `Y=2y/S`.

The symmetry prediction is that the sign problem should depend only on the squares. The exact common-denominator computation below confirms that prediction: after the normalization the numerator contains only even powers of `X,Y`.

## 7. Method #18 — SAY IT IN ANOTHER LANGUAGE: Bernstein-positive polynomial on a square

Write

\[
\psi_i=\frac{\Psi_i}{2\tau},
\qquad
\Psi_i:=\sum_{z\ne i}d_zF_{iz}.
\]

Since all `F_kl` and `tau` are strictly positive for positive conductances, the sign of (5.4) is the sign of the exact polynomial common numerator

\[
N:=
\sum_{k<l}
 w_{ab}(r_l-r_k)(\Psi_l-\Psi_k)
 \prod_{\{i,j\}\ne\{k,l\}}F_{ij},
\tag{7.1}
\]

because

\[
\mathcal E_*=
\frac{N}{2\tau\prod_{i<j}F_{ij}}.
\tag{7.2}
\]

Substitute (6.2). The exact calculation shows that `N` is even in both `X` and `Y`. Set

\[
u=\frac{X^2}{4}=\frac{x^2}{S^2},
\qquad
v=\frac{Y^2}{4}=\frac{y^2}{S^2},
\qquad 0\le u,v<1.
\tag{7.3}
\]

Let

\[
B_{k,6}(t)=\binom6k t^k(1-t)^{6-k}
\]

be the degree-six Bernstein basis. Exact coefficient conversion gives the identity

\[
\boxed{
N=\frac4{225}
\sum_{k,l=0}^6 C_{kl}B_{k,6}(u)B_{l,6}(v),}
\tag{7.4}
\]

with coefficient matrix

\[
C=\begin{pmatrix}
0&196608000&336199680&430755840&490076160&522144000&533433600\\
196608000&369459200&484945920&555939840&592880320&604187400&596610000\\
336199680&484945920&576845824&625548288&642020304&635009190&611432760\\
430755840&555939840&625548288&653891562&652350003&629886435&593479305\\
490076160&592880320&642020304&652350003&635546400&600673470&554659320\\
522144000&604187400&635009190&629886435&600673470&556418300&503884800\\
533433600&596610000&611432760&593479305&554659320&503884800&447638400
\end{pmatrix}.
\tag{7.5}
\]

Every entry is nonnegative and the only zero is `C_00`. Every Bernstein basis function is nonnegative on `[0,1]`. Therefore

\[
N\ge0\qquad(0\le u,v<1).
\tag{7.6}
\]

Moreover, if `(u,v)\ne(0,0)`, then at least one basis term with a strictly positive coefficient is strictly positive: if `u=0<v`, use the `k=0,l>=1` row; if `v=0<u`, use the `l=0,k>=1` column; if both are positive, use any interior positive coefficient. Hence

\[
N=0\quad\Longleftrightarrow\quad u=v=0
\quad\Longleftrightarrow\quad x=y=0
\tag{7.7}
\]

inside the strict-positive family. By (7.2),

\[
\boxed{\mathcal E_*\ge0,}
\tag{7.8}
\]

with equality exactly at the fully balanced point in this two-axis family.

This Bernstein reformulation is the substantive new route: the monomial coefficients need not advertise positivity, but the compact-square Bernstein basis turns the exact sign question into a finite list of manifestly nonnegative rational coefficients.

## 8. Method #4 — PROVE SOMETHING WEAKER, COMPLETELY: the two-axis equal-sum theorem

### Theorem `NM13-09-P0245-EQUALSUMS-TWOAXIS-BERNSTEIN-06`

Let `(X_t)` be an irreducible loopless reversible Markov chain on four states with strictly positive conductances. Suppose the three opposite-edge sums are equal,

\[
a+f=b+e=c+d=S>0,
\tag{8.1}
\]

and one opposite pair is balanced; after relabeling, suppose `c=d`. Then

\[
\boxed{\mathbb E_\pi C\ge\frac{11}{2}.}
\tag{8.2}
\]

Thus Aldous–Fill Open Problem 6.30 holds on this entire positive two-axis equal-opposite-sum four-state class.

### Proof

Relabel so that the balanced pair is `c=d`, and normalize the common sum to two as in (6.2). Sections 6–7 prove exactly that `E_*>=0` on this family.

The cross-Foster identity (5.5) simplifies under `A=B=C=S` and `z=0` to

\[
\tau\left(\sum_e w_eR_{e^*}-3\right)
=2S(x^2+y^2)\ge0.
\tag{8.3}
\]

Since `tau>0`,

\[
\sum_e w_eR_{e^*}\ge3.
\tag{8.4}
\]

Combining (5.3), (7.8), and (8.4) gives

\[
D_3\ge3.
\]

Finally the already established all-positive-loopless-four-state bounds (5.2) give

\[
\mathbb E_\pi C
=D_1+D_2+D_3
\ge1+\frac32+3
=\frac{11}{2}.
\]

This proves (8.2). `QED`

The theorem is deliberately **PARTIAL** relative to P0245. It neither proves arbitrary four-state chains nor handles arbitrary self-loops or general `n`.

## 9. Exact checker, execution, and archive

Only after deriving the two-axis reduction and Bernstein certificate did I build a finite exact self-check.

Checker:

`proofnet24/NM13-09/artifacts/2026-09-18/p0245_two_axis_equal_sums_bernstein.py`

- created at commit `591ce42b81f09e2458aa37619cfa11617a432fab`;
- read back at that exact commit;
- blob `72f0116b351eff2ccc57e59f7b88618fc68478d4`.

The script reconstructs `tau`, all six `F_kl`, all four deletion-tree polynomials, `Psi_i`, and the common numerator (7.1) from the conductance definitions; specializes only afterward; verifies evenness in `X,Y`; performs the exact rational Bernstein conversion; checks the full matrix (7.5); verifies reconstruction coefficient-for-coefficient; and checks an exact rational spot value.

Archived executed output:

`proofnet24/NM13-09/artifacts/2026-09-18/p0245_two_axis_equal_sums_bernstein.out`

- created at commit `e64257e7864304ca7f0f64e08cf551217f5b3818`;
- read back at that exact commit;
- blob `f44b0367db2d0666805683e441de24a761acc3d3`;
- ends `ALL_EXACT_CHECKS_PASS`.

The output records `all_C_nonnegative = PASS`, `C[0,0]=0` as the only zero coefficient, exact reconstruction, and the positive spot common numerator

\[
N(1,3/2)=\frac{167647335079599}{16777216}>0.
\]

This is a **self-check, not an independent audit**. Neither P26 nor NM13-10 is counted as having audited or passed this theorem.

## 10. Six-run handoff: what a fresh route inherits

The parent source remains OPEN. The following P0245 progress should be preserved rather than re-derived by a future authorized owner:

1. The frozen order-four Cayley metric is exactly `R_Cayley4=1`.
2. The source bound is proved for the full `S_3`-symmetric `1+3` four-state conductance family, including its allowed loop parameters from the earlier theorem.
3. For arbitrary positive loopless four-state chains, `D_1=1` and `D_2>=3/2` are proved exactly.
4. The exact decomposition (5.3) and cross-Foster identity (5.5) reduce the last discovery increment to a transparent resistance slack plus `E_*`.
5. The balanced point has a positive-semidefinite local cross-energy Hessian in the Walsh imbalance coordinates.
6. `E_*>=0` globally on every one-axis imbalance family; the previous report gives the exact closed form.
7. This run proves `E_*>=0` on the genuinely coupled two-axis family `A=B=C`, one imbalance coordinate zero, by the exact Bernstein certificate (7.4)–(7.5).
8. Earlier bounded exact primitive integer grids found no negative `E_*`; those remain diagnostics only and are not continuous proofs.

The unresolved mathematical knot is still genuinely global:

\[
\mathcal E_*(A,B,C;x,y,z)\stackrel{?}{\ge0}
\qquad
(|x|<A,\ |y|<B,\ |z|<C),
\tag{10.1}
\]

or, if that stronger stagewise sign fails, whether the **total** slack in (5.3) nonetheless stays nonnegative. The cleanest unexplored region after this run is unequal opposite sums with two simultaneous imbalances, followed by the fully coupled three-imbalance region and then self-loops. A future fresh owner should first try to falsify (10.1) or the total-slack inequality there rather than automatically extending another symbolic slice.

Because the frozen metric has now remained unchanged for six consecutive P0245 invocations, this handoff is mandatory. **NM13-09 must rotate now.** The next NM13-09 invocation should enter `ADMISSION_PENDING` and screen a different genuinely unassigned residue-8 CLOSABLE source, beginning with current queue/intake deltas and ownership releases rather than treating this handoff as permission to reopen P0245.

## 11. Structured ledger delta for P26

```yaml
ledger_delta:
  track: NM13-09
  category: CLOSABLE OUTSIDE
  status: PARTIAL_HANDOFF_ROTATE
  source_id: P0245
  claim_path: operations/claims/P0245.md
  canonical_dedup_key: exact_minimum_stationary_cover_time_for_reversible_chains
  shard_residue: 8
  source_status: OPEN
  metric:
    name: R_Cayley4
    before: 1
    after: 1
    movement: false
  mathematical_progress: true
  new_claim_id: NM13-09-P0245-EQUALSUMS-TWOAXIS-BERNSTEIN-06
  new_claim_scope: >-
    Positive loopless four-state reversible chains with equal opposite-edge
    sums and one balanced opposite pair satisfy E_pi C >= 11/2.
  methods_attempted: [4, 14, 18]
  method_outcomes:
    4: SUCCESS_complete_restricted_two_axis_theorem
    14: SUCCESS_opposite_pair_symmetry_and_scale_quotient
    18: SUCCESS_exact_Bernstein_positive_common_numerator
  unchanged_run_counter: 6
  stuck_recoveries_used: 1
  artifacts:
    checker_path: proofnet24/NM13-09/artifacts/2026-09-18/p0245_two_axis_equal_sums_bernstein.py
    checker_commit: 591ce42b81f09e2458aa37619cfa11617a432fab
    checker_blob: 72f0116b351eff2ccc57e59f7b88618fc68478d4
    output_path: proofnet24/NM13-09/artifacts/2026-09-18/p0245_two_axis_equal_sums_bernstein.out
    output_commit: e64257e7864304ca7f0f64e08cf551217f5b3818
    output_blob: f44b0367db2d0666805683e441de24a761acc3d3
    output_status: ALL_EXACT_CHECKS_PASS
    audit_label: SELF_CHECK_ONLY
  audits:
    P26: NOT_PASSED
    NM13-10: NOT_PASSED
  handoff: true
  next_track_state: ADMISSION_PENDING
  next_step: >-
    Do not execute a seventh P0245 research run on NM13-09. Preserve this
    handoff and screen a different genuinely unassigned residue-8 CLOSABLE
    source after exact source/current-literature/prior-attempt/ownership checks.
```

No shared root, peer namespace, canonical claim file, workflow, permission, public surface, email/Drive item, paid-compute resource, or schedule was modified in this invocation.
