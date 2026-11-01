Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — not GPT-6 maximum. NO FROZEN-METRIC MOVEMENT: `R_Cayley4: 1 -> 1`; Section-B methods actually tried this run: #5, #14, #18.**

# NM13-09 — P0245: Walsh reduction and a local four-state cover-time theorem

Date: 2026-09-18 UTC  
Track / namespace: `NM13-09` / `proofnet24/NM13-09/`  
Category: CLOSABLE OUTSIDE  
Repository / branch: private `yspennstate/math-open-problems` / `master`

## 1. Continuity, ownership, and controlling state

This invocation continues the already admitted **P0245 — Aldous–Fill Open Problem 6.30** assignment. It does not reopen intake and it does not create another ownership claim.

Before the mathematical attack I reread or targeted-recovered the controlling state required by the owner:

- `FLEET_RULES.md`;
- `operations/new_methods_2026-09-16/OWNER_DIRECTIVE.md`;
- `operations/NEW_METHODS_2026-09-16.md`;
- later owner-authorized amendment `operations/NM13_DEPLOYMENT_2026-09-17T203709Z.md`;
- root `QUEUE.md`, `POSTED.md`, and `RESULTS.md`;
- `probability_campaign_2026_09/INDEX.md` and `RANKING.md`;
- canonical claim `operations/claims/P0245.md`;
- newest own report `proofnet24/NM13-09/runs/2026-09-18/2026-09-18T00-45-12Z__p0245-cross-foster-symmetric-hitting.md`;
- newest visible neighboring NM13-08 report `proofnet24/NM13-08/runs/2026-09-18/2026-09-18T01-35-23Z__p0408-stuck-recovery-1.md`;
- newest visible neighboring NM13-10 report `proofnet24/NM13-10/runs/2026-09-18/2026-09-18T00-51-30Z__admission-delta-screen-5.md`;
- targeted P0245 intake, catalog, attempt, dedup-key, claim, and historical numerical-search records.

Large append-only intake/catalog objects can be connector-truncated when fetched wholesale. I therefore recovered continuity by exact source ID, canonical dedup key, claim path, and targeted attempt searches rather than pretending every repository byte was rendered in one response. No material P0245 history needed for this run was inaccessible.

Exclusive ownership remains unchanged:

- source / claim ID: **P0245**;
- owner: **NM13-09**;
- canonical dedup key: `exact_minimum_stationary_cover_time_for_reversible_chains`;
- SHA256: `642682b0fbba364a68d451232e8378be7074f75d1a8a86e5cff4b8037577e6fe`;
- shard residue: `8 mod 13`;
- claim path: `operations/claims/P0245.md`.

The historical campaign record is preserved rather than erased: P0245 was already `attempted_unsolved`; the campaign proved the two-state case, later ran exact subset-DP cover-time evaluation combined with floating-point Nelder–Mead searches on small orders, and found the complete-graph value for `n=3,4` and no smaller `n=5` candidate. Those searches are evidence, not a proof. No release, handoff, conflicting owner, retirement, `POSTED.md` closure, or campaign source-level closure was recovered. NM13-10 remains admission-pending and has not supplied an audit of P0245.

## 2. Exact source and fresh bounded literature status

Source: David Aldous and James Allen Fill, *Reversible Markov Chains and Random Walks on Graphs*, Chapter 6, §6.6.4, **Open Problem 6.30**. The current source page still states:

\[
\boxed{\mathbb E_\pi C\ge (n-1)h_{n-1}}
\]

for every reversible chain on `n` states, with the right side equal to the stationary cover time of random walk on the complete graph.

Fresh searches dated **2026-09-18** used the exact problem number, the displayed inequality, `stationary cover time reversible chain complete graph`, `minimum cover time reversible Markov chain`, and the new mechanism terms `four-state`, `Walsh`, `effective resistance`, `Foster`, and `stationary cover time`. They recovered the source page itself and the Feige / Chlamtac–Feige deterministic approximation literature for cover time of reversible chains, but no source-matching proof or counterexample to the exact stationary extremal inequality. These approximation papers address algorithmic approximation of cover times, not the exact extremal constant in Open Problem 6.30.

This is **bounded negative evidence only**, not proof of worldwide openness or publication novelty. The linear-algebra mechanisms used below are standard tools; publication novelty of the exact reduction or local theorem is **UNVERIFIED**.

## 3. Frozen metric and counters

The admitted frozen metric remains

\[
R_{\mathrm{Cayley},4}
=\inf\frac{\mathbb E_\pi C}{11/2}
\]

over irreducible reversible translation-invariant chains on a group of order four, with source hypotheses retained. It was solved exactly at admission and is not silently replaced by a broader-class flag.

- **Before:** `1`.
- **After:** `1`.
- **Movement:** none.
- **Consecutive unchanged runs since metric movement:** `3`.
- **Stuck recoveries used:** `0`.

This run contains substantive source-relevant progress outside the frozen metric, but policy requires the metric to remain unchanged. Because this is the third consecutive unchanged run, the **next NM13-09 invocation must be the Section-I thinking-only stuck-recovery run, with no new mathematical claim**.

P0245 remains **OPEN / NM13-09 PARTIAL**.

## 4. Starting point from the preceding run

Restrict for this attack to a positive, loopless reversible chain on four states. Write the six conductances

\[
a=w_{01},\quad b=w_{02},\quad c=w_{03},\quad
d=w_{12},\quad e=w_{13},\quad f=w_{23},
\]

let `d_i=sum_{j ne i} w_ij`, and let `W=sum_i d_i`. The previous report proved:

1. `D_1=1` for the first discovery increment;
2. `D_2>=3/2` by the two-target Dirichlet inequality;
3. the exact cross-Foster bound
   \[
   \sum_e w_eR_{e^*}\ge3;
   \]
4. and, for the final discovery increment,
   \[
   D_3
   =\sum_e w_eR_{e^*}
   +\frac2W\,\mathcal E_*(r,\psi),
   \tag{4.1}
   \]
   where
   \[
   \mathcal E_*(r,\psi)
   =\sum_{k<l}c^*_{kl}(r_l-r_k)(\psi_l-\psi_k),
   \qquad
   c^*_{kl}=\frac{w_{ab}}{F_{kl}},
   \tag{4.2}
   \]
   `{a,b}` is the pair opposite `{k,l}`, `F_kl` is the separating two-forest polynomial, `r_i` is the spanning-tree polynomial of the three-vertex graph obtained by deleting vertex `i`, and
   \[
   \psi_i=\frac12\sum_z d_zR_{iz}.
   \]

Thus an inequality `E_*>=0` would imply `D_3>=3`, and hence

\[
\mathbb E_\pi C=D_1+D_2+D_3\ge 1+\frac32+3=\frac{11}{2}.
\tag{4.3}
\]

The preceding run did **not** prove the global sign of `E_*`. The purpose of this run is to understand that one obstruction rather than manufacture another certificate for the already solved Cayley metric.

## 5. New idea before code

The six raw conductances obscure the tetrahedral symmetry. Pair opposite edges and split each pair into its sum and imbalance:

\[
A=a+f,\quad B=b+e,\quad C=c+d,
\qquad
x=a-f,\quad y=b-e,\quad z=c-d.
\tag{5.1}
\]

Thus

\[
a=\frac{A+x}{2},\ f=\frac{A-x}{2},\quad
b=\frac{B+y}{2},\ e=\frac{B-y}{2},\quad
c=\frac{C+z}{2},\ d=\frac{C-z}{2}.
\tag{5.2}
\]

Positivity gives `|x|<A`, `|y|<B`, `|z|<C`. The point `(x,y,z)=(0,0,0)` is exactly the opposite-edge-balanced four-state Cayley locus. The intended route is therefore:

- **#14:** quotient by the tetrahedral symmetry using the three nonconstant Walsh characters;
- **#18:** rewrite the residual obstruction as a Dirichlet cross-form between two explicit three-dimensional operators;
- **#5:** deform only the imbalance vector `(x,y,z)` away from the solved point and compute the exact second variation.

The key payoff is that the solved Cayley locus is not an isolated miracle: the cross-energy has a strictly positive quadratic form in every nontrivial imbalance direction.

## 6. Method #14 — tetrahedral symmetry in Walsh coordinates

Put

\[
Q=
\begin{pmatrix}
1&1&1\\
1&-1&-1\\
-1&1&-1\\
-1&-1&1
\end{pmatrix}.
\tag{6.1}
\]

The columns of `Q/2` are an orthonormal basis of the mean-zero subspace of functions on the four vertices. If `L` is the weighted graph Laplacian, define its mean-zero representation

\[
M:=\frac14Q^TLQ.
\tag{6.2}
\]

Set

\[
p=B+C,\qquad q=A+C,\qquad s=A+B,
\qquad \Sigma=A+B+C.
\tag{6.3}
\]

A direct substitution of (5.2) into the Laplacian gives the exact quotient

\[
\boxed{
M=
\begin{pmatrix}
p&z&y\\
z&q&x\\
y&x&s
\end{pmatrix}.}
\tag{6.4}
\]

Because `Q/2` is orthonormal on `1^perp`, if `tau` denotes the weighted spanning-tree polynomial then

\[
\Delta:=\det M=4\tau>0.
\tag{6.5}
\]

For any vertex function `g`, write

\[
\widehat g:=\frac14Q^Tg,
\qquad
g=\bar g\,\mathbf 1+Q\widehat g.
\tag{6.6}
\]

### Lemma `NM13-09-P0245-WALSH4-04A`

For the vector `r=(r_0,r_1,r_2,r_3)^T` of deletion-tree polynomials,

\[
\boxed{
\widehat r
=\frac14
\begin{pmatrix}
yz-px\\xz-qy\\xy-sz\end{pmatrix}.}
\tag{6.7}
\]

Moreover, for the degree vector `d=(d_0,d_1,d_2,d_3)^T`,

\[
\boxed{\widehat d=\frac12(x,y,z)^T,\qquad W=2\Sigma.}
\tag{6.8}
\]

### Proof

Deleting one vertex from `K_4` leaves a weighted triangle. Its spanning-tree polynomial is the sum of the three pairwise products of its three edge weights. Substitute (5.2) into those four degree-two polynomials and take the three signed Walsh differences in (6.6). The constant terms cancel and the three remaining coordinates are exactly (6.7). Summing the three incident edge weights at each vertex and taking the same signed differences gives (6.8). `square`

Equation (6.7) is the first structural simplification: the asymmetric part of the four deletion-tree polynomials is only quadratic in the three imbalance coordinates.

## 7. Method #18 — the obstruction as an exact three-dimensional Dirichlet cross-form

Let `L^+` be the Moore–Penrose inverse of `L`. From (6.2),

\[
L^+=\frac14QM^{-1}Q^T.
\tag{7.1}
\]

Effective resistance satisfies

\[
R_{ij}=L^+_{ii}+L^+_{jj}-2L^+_{ij}.
\tag{7.2}
\]

The three off-diagonal cofactors of `M` give

\[
(M^{-1})_{23}=\frac{4\widehat r_1}{\Delta},\qquad
(M^{-1})_{13}=\frac{4\widehat r_2}{\Delta},\qquad
(M^{-1})_{12}=\frac{4\widehat r_3}{\Delta}.
\tag{7.3}
\]

Indeed the corresponding cofactors are respectively `yz-px`, `xz-qy`, and `xy-sz`, which are four times the coordinates in (6.7).

### Lemma `NM13-09-P0245-DUALENERGY-04B`

With `v=(x,y,z)^T`, the Walsh coordinates of `psi` are

\[
\boxed{
\widehat\psi
=\frac{W}{\Delta}\widehat r
-\frac12M^{-1}v.}
\tag{7.4}
\]

If `L_*` is the Laplacian on the same four labels with dual conductances `c^*_{kl}` from (4.2), and

\[
K:=\frac14Q^TL_*Q,
\tag{7.5}
\]

then

\[
\boxed{
\mathcal E_*(r,\psi)
=4\widehat r^{\,T}K\widehat\psi
=\frac{4W}{\Delta}\widehat r^{\,T}K\widehat r
-2\widehat r^{\,T}KM^{-1}v.}
\tag{7.6}
\]

### Proof

Expanding (7.2) in

\[
\psi_i=\frac12\sum_j d_jR_{ij}
\]

gives, up to an additive constant independent of `i`,

\[
\psi_i=\frac W2 L^+_{ii}-(L^+d)_i+\text{constant}.
\tag{7.7}
\]

Take nonconstant Walsh coordinates. Equation (7.3) says that the nonconstant Walsh coordinates of the diagonal of `L^+` equal `2\widehat r/\Delta`; while (7.1) and (6.8) give the nonconstant coordinates of `L^+d` as `M^{-1}v/2`. This proves (7.4).

For the second assertion, the definition of a weighted graph Laplacian gives

\[
\mathcal E_*(r,\psi)=r^TL_*\psi.
\]

Constants vanish under `L_*`, and (6.6) gives

\[
r^TL_*\psi
=(Q\widehat r)^TL_*(Q\widehat\psi)
=4\widehat r^TK\widehat\psi.
\]

Substituting (7.4) yields (7.6). `square`

This language explains both the hope and the obstruction. The first term of (7.6) is nonnegative because `K` is a graph-Laplacian form on `1^perp`. But the second term is a genuine mixed form; positivity of `K` and `M` separately does **not** give its sign. So the preceding run's sign problem is not resolved by a formal positive-definite-matrix slogan.

## 8. Method #5 — deform the opposite-edge imbalance and compute the exact Hessian

Fix positive `A,B,C` and a direction `(x,y,z)`. Introduce

\[
(x_t,y_t,z_t)=t(x,y,z),
\qquad -\varepsilon<t<\varepsilon,
\tag{8.1}
\]

with `A,B,C` held fixed. For sufficiently small `|t|`, all six conductances in (5.2) remain positive. Write `E(t)` for the corresponding cross-energy `E_*(r,psi)`.

At `t=0`,

\[
M_0=\operatorname{diag}(p,q,s),
\qquad \Delta_0=pqs,
\qquad \widehat r(0)=\widehat\psi(0)=0.
\tag{8.2}
\]

The dual conductances also become opposite-edge balanced. For each individual edge of the three opposite types they are

\[
\frac{2A}{p(q+s)},\qquad
\frac{2B}{q(p+s)},\qquad
\frac{2C}{s(p+q)}.
\tag{8.3}
\]

It is convenient to denote the corresponding **opposite-pair sums** by

\[
\alpha=\frac{4A}{p(q+s)},\qquad
\beta =\frac{4B}{q(p+s)},\qquad
\gamma=\frac{4C}{s(p+q)}.
\tag{8.4}
\]

Then

\[
K_0=\operatorname{diag}(\kappa_x,\kappa_y,\kappa_z),
\qquad
\kappa_x=\beta+\gamma,\quad
\kappa_y=\alpha+\gamma,\quad
\kappa_z=\alpha+\beta,
\tag{8.5}
\]

and every `kappa` is strictly positive.

Differentiate (6.7):

\[
\widehat r'(0)
=-\frac14(px,qy,sz)^T.
\tag{8.6}
\]

Differentiate (7.4). Since `W=2Sigma` is fixed and `\widehat r(0)=0`, derivatives of `Delta^{-1}` do not contribute at first order, so

\[
\widehat\psi'(0)
=-\frac12
\begin{pmatrix}
 x\left(\frac1p+\frac{\Sigma}{qs}\right)\\[2mm]
 y\left(\frac1q+\frac{\Sigma}{ps}\right)\\[2mm]
 z\left(\frac1s+\frac{\Sigma}{pq}\right)
\end{pmatrix}.
\tag{8.7}
\]

Because `E(t)=4\widehat r(t)^TK(t)\widehat\psi(t)` and both endpoint vectors vanish at `t=0`,

\[
E(0)=E'(0)=0,
\qquad
E''(0)=8\widehat r'(0)^TK_0\widehat\psi'(0).
\tag{8.8}
\]

Substituting (8.5)–(8.7) gives the exact diagonal Hessian formula

\[
\boxed{
\begin{aligned}
E''(0)={}&\kappa_xx^2\left(1+\frac{p\Sigma}{qs}\right)
+\kappa_yy^2\left(1+\frac{q\Sigma}{ps}\right)\\
&+\kappa_zz^2\left(1+\frac{s\Sigma}{pq}\right).
\end{aligned}}
\tag{8.9}
\]

Every coefficient in (8.9) is strictly positive.

### Theorem `NM13-09-P0245-LOCAL4-04C`

For every positive opposite-edge-balanced loopless four-state reversible chain, the cross-energy `E_*` has a strict local minimum in the three opposite-edge imbalance directions. Equivalently, fixing its positive opposite-pair sums `A,B,C`, there exists

\[
\varepsilon(A,B,C)>0
\]

such that every positive conductance vector with

\[
x^2+y^2+z^2<\varepsilon(A,B,C)^2
\tag{8.10}
\]

satisfies

\[
\boxed{\mathcal E_*(r,\psi)\ge0,}
\tag{8.11}
\]

with equality locally only at `x=y=z=0`.

Consequently there is an open conductance neighborhood of every positive opposite-edge-balanced loopless four-state chain in which

\[
\boxed{\mathbb E_\pi C\ge\frac{11}{2}.}
\tag{8.12}
\]

### Proof

On the open positive-conductance region, every spanning-tree and separating-forest denominator occurring in `E_*` is positive, so `E_*` is real analytic in the conductances. Equations (8.8)–(8.9) show that its value and gradient vanish at the balanced point and that its Hessian restricted to the imbalance coordinates is positive definite. Taylor's theorem therefore gives (8.10)–(8.11) for some positive neighborhood radius depending on `A,B,C`.

For the cover-time conclusion, combine (8.11) with the exact decomposition (4.1) and the preceding run's cross-Foster inequality:

\[
D_3\ge \sum_e w_eR_{e^*}\ge3.
\]

The already proved `D_1=1` and `D_2>=3/2` then yield (8.12). `square`

This is a genuine enlargement of the exactly solved Cayley/opposite-balanced locus to an **open** family of non-Cayley conductance vectors. It is nevertheless only a restricted `n=4`, loopless theorem and therefore remains PARTIAL relative to Open Problem 6.30.

## 9. Why the global deformation did not close

Method #5 was also tested as a possible global interpolation strategy: keep `A,B,C` fixed and move `t` from `0` to `1` in (8.1), hoping for monotonicity of `E(t)` or `D_3(t)`. The exact second variation proves the desired sign only locally. Away from `t=0`, both `K(t)` and `M(t)^{-1}` vary, and differentiating the mixed term in (7.6) produces higher-order contributions with no sign supplied by the current identities.

I therefore **do not** claim global monotonicity, global positivity of `E_*`, or the arbitrary loopless four-state case. The useful output of the deformation is precisely the certified positive Hessian and the resulting open-neighborhood theorem.

## 10. Section-B accounting

### #14 — FIND THE GROUP ACTING

**Success.** The tetrahedral symmetry collapses six conductances to three opposite-pair sums and three imbalance variables, and the mean-zero Laplacian becomes the explicit `3x3` matrix (6.4). The deletion-tree vector reduces to the quadratic Walsh expression (6.7).

### #18 — SAY IT IN ANOTHER LANGUAGE

**Success as a reduction, not a global sign proof.** The residual cover-time obstruction becomes the exact three-dimensional Dirichlet cross-form (7.6). It isolates one positive quadratic term and one genuinely indefinite mixed term, explaining why the preceding sign problem is nontrivial.

### #5 — ADD A PARAMETER AND DIFFERENTIATE IN IT

**Local success / global stall.** Scaling the imbalance gives the exact Hessian (8.9), positive in every nonzero direction, hence the open-neighborhood cover-time theorem. The hoped-for global monotonicity along the full deformation is not established.

These methods are genuinely different from the preceding run's `#3/#12/#25` triple and had not previously been credited on P0245.

## 11. Verification discipline

The identities above were derived symbolically from the weighted Laplacian, the matrix-tree/cofactor formulas, and the three Walsh characters, and the full derivation needed for the theorem is written on this page. This is a parameter-uniform theorem-sized claim, not a finite enumeration claim, so I did **not** manufacture a new checker-only artifact merely to certify an unchanged frozen metric.

The exact finite self-check from the preceding run remains available for its own cross-Foster and harmonic-bias identities, but it is not represented here as an independent audit of the new theorem.

## 12. Literature / novelty interpretation

The source page continues to label the exact statement Open Problem 6.30. The bounded current search did not recover a source-matching resolution. The Feige and Chlamtac–Feige papers found in the search concern deterministic approximation of cover time (including reversible Markov chains), not this exact stationary extremal lower bound.

I did not recover a publication stating the Walsh cross-energy formula (7.6) or the local imbalance theorem (8.12). That is only a bounded search result. The linear-algebra and perturbation mechanisms may be folklore, and **publication novelty remains UNVERIFIED**.

## 13. Status, stuck threshold, next route, and audits

Source status: **OPEN**.  
NM13-09 status: **PARTIAL**.  
P26 audit: **not requested / not passed**.  
NM13-10 audit: **not requested / not passed**.

The frozen metric has now failed to move for **three consecutive runs**. Under the owner protocol, the **next invocation must be a Section-I thinking-only stuck-recovery report with no new theorem or finite claim**. It must state the exact blocking formula, every route and failure reason, the ingredient still missing, the simplest unproved special case, and the nearest solved literature comparison, and then select exactly one permitted recovery action.

Prospective next lenses, **not counted as tried in this run**, are:

- **#1 CHANGE THE CATEGORY:** reinterpret the dual cross-energy using spanning-tree/matroid or electrical-network correlation language;
- **#20 FIND WHY THE ALGORITHM FAILS:** isolate the exact obstruction to turning the positive local operator comparison into a global one;
- **#24 FIND THE EXTREMAL OBJECT:** in the thinking-only recovery, identify the boundary/interior conductance strata that could minimize the normalized cross-energy and choose one legal recovery action.

The exact current blocker remains the global sign problem

\[
\boxed{
\mathcal E_*(r,\psi)
=\sum_{k<l}\frac{w_{ab}}{F_{kl}}
(r_l-r_k)(\psi_l-\psi_k)\stackrel{?}{\ge}0
}
\tag{13.1}
\]

for arbitrary positive loopless four-state conductances. This run proves (13.1) only in an open neighborhood of the opposite-edge-balanced locus.

## 14. Model / task-control status

The task prompt requests GPT-6 with maximum reasoning, but this invocation actually identifies as **GPT-5.6 Sol** and exposes no authenticated reasoning-effort telemetry; therefore the reasoning level is **UNVERIFIED**. I do not claim a binding GPT-6 setting, maximum reasoning, or an hour-long execution.

The exposed task-control surface still provides title/prompt, schedule or relative-start fields, timing mode, enablement, and ordinary update operations, but **no binding model-family selector and no reasoning-effort selector**. Thus GPT-6/maximum remains prompt-only here. Enforcing it would require an owner-authorized product/workspace/API/admin surface that exposes those fields plus runtime attestation.

Repository policy records historical native modification probes for P26/P01/P03 returning `You cannot modify this task`, while later repository reconciliation records a successful P26 update from another authorized context. The appropriate workaround for such a refusal is therefore the owning/authorized task or workspace/product/admin surface (or a platform capability change), not task duplication, permission bypass, or a repository edit presented as a scheduler change. No schedule was created or modified in this invocation.

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
  methods_attempted: [5, 14, 18]
  method_outcomes:
    5: "imbalance deformation has strictly positive exact Hessian at every positive opposite-balanced point; gives a local open-neighborhood theorem, but no global monotonicity"
    14: "tetrahedral quotient gives explicit 3x3 Walsh Laplacian and quadratic deletion-tree coordinates"
    18: "residual last-stage obstruction becomes an exact 3-dimensional dual Dirichlet cross-form"
  new_claim_ids:
    - NM13-09-P0245-WALSH4-04A
    - NM13-09-P0245-DUALENERGY-04B
    - NM13-09-P0245-LOCAL4-04C
  exact_checker: NONE_NEW_THEOREM_SIZED_FULL_PROOF_ON_PAGE
  p26_audit: NOT_REQUESTED
  secondary_audit_partner: NM13-10
  secondary_audit: NOT_REQUESTED
  unchanged_runs_since_metric_movement: 3
  stuck_recoveries_used: 0
  next_run_protocol: SECTION_I_THINKING_ONLY_NO_NEW_CLAIMS
  next_methods: [1, 20, 24]
  next_step: "perform the mandatory Section-I recovery around the global sign obstruction (13.1); do not redefine the frozen metric"
```
