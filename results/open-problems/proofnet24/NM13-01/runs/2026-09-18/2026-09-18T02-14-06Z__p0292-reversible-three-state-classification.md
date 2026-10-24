Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — not GPT-6 maximum. NO FROZEN-METRIC MOVEMENT: `D_rev,0` stayed `0 -> 0`. Section-B methods actually tried: #1, #15, #19.**

# NM13-01 — P0292 full reversible three-state classification

**Track:** NM13-01  
**Category:** CLOSABLE OUTSIDE  
**Source ID / claim:** P0292 / `operations/claims/P0292.md`  
**Canonical dedup key:** `characterize_ctmc_speed_monotonicity_in_supermodular_order`  
**Canonical SHA-256 / shard:** `3aded70a56a908e9042798ee4a8ac614005a51635e52453716ea79167c073ae5`, residue `0 mod 13`  
**Source:** Lasse Leskelä, *Ross's second conjecture and supermodular stochastic ordering*, Queueing Systems 100 (2022), Problem 4, source p. 215  
**Source status:** OPEN in full generality in the bounded current-literature check below  
**Track status:** PARTIAL  
**Frozen metric:** `D_rev,0`, normalized frozen-limit first-order supermodular speed defect over finite stationary irreducible reversible CTMCs  
**Metric before / after:** `0 -> 0` exactly; **no movement**  
**Consecutive unchanged runs since metric movement:** 5  
**Stuck recoveries used:** 1  
**Audits:** P26 NOT REQUESTED / NOT PASSED; NM13-02 NOT REQUESTED / NOT PASSED  
**New internal claim label:** `NM13-01-P0292-REV3-FULL-05`  
**Artifacts:** none. The result is a parameter-uniform theorem with a complete symbolic proof on this page; no finite enumeration is used as evidence.

## 1. Authoritative continuity, ownership, and exclusions

I continued the admitted P0292 claim; I did **not** reopen intake, change the source, change the normalization, create a second claim, or treat the new theorem as source closure. Immediately before this write, `operations/claims/P0292.md` still named NM13-01 as exclusive owner, fixed the canonical key above, and recorded the source as OPEN. No release, handoff, retirement, competing owner, POSTED entry, or source-level PROVED/REFUTED/KNOWN correction for P0292 was recovered.

Before the mathematical attack I reread/recovered the current required repository state: `FLEET_RULES.md`; `operations/new_methods_2026-09-16/OWNER_DIRECTIVE.md`; `operations/NEW_METHODS_2026-09-16.md`; the later owner-authorized `operations/NM13_DEPLOYMENT_2026-09-17T203709Z.md`; root `QUEUE.md`, `POSTED.md`, and `RESULTS.md`; `probability_campaign_2026_09/INDEX.md` and `RANKING.md`; the canonical P0292 claim; the P0292 dedup entry and historical attempt material including `P0292-A002`; the old P0292 spectral/LP scripts; my newest report `2026-09-18T01-03-51Z__p0292-three-time-endpoint-flow.md`; and the newest neighboring NM13-02 report `2026-09-18T01-14-00Z__p0037-witness-congestion.md`. NM13-02 remains on its distinct P0037 claim and has no P0292 ownership conflict.

The historical state is preserved rather than re-counted: P0292-A002 had already handled two pieces of the reversible three-state star family and left its strict remaining half as numerical evidence; the later NM13-01 single-crossing report proved the full star classification and a general two-mode sufficient theorem; the immediately preceding report proved the complete **three-observation** reversible-three-state theorem under the slow endpoint-sign condition. None of those old pieces is represented below as new progress.

The current master head observed just before the final ownership read was `2f3db0564c5cd48436a0a722aa8ca38a701f20c7`. Shared roots and peer files are unchanged by this invocation.

## 2. Exact source and bounded literature check — 2026-09-18 UTC

I re-read the accepted-author source PDF (DOI `10.1007/s11134-022-09824-0`) and visually checked source p. 215. Problem 4 asks for a simple necessary-and-sufficient condition on a stationary ergodic CTMC under which the all-finite-dimensional speed order

\[
 c_1\le c_2 \quad\Longrightarrow\quad \lambda_{c_1}\ge_{\rm sm}\lambda_{c_2}
\]

holds. The source explicitly says that outside stochastically monotone CTMCs not much was known even for state spaces of size three. On the preceding page it records the Bäuerle--Rolski sufficient class: a reversible stochastically monotone CTMC satisfies the desired order.

Fresh bounded searches dated 2026-09-18 covered the exact source title and Problem 4 wording, Leskelä's current paper/author metadata, `three-state reversible Markov chain supermodular lag`, `slow eigenfunction stochastic monotonicity`, and later dependence-order papers. The nearest recovered literature remains:

- Hu--Joe (1995), *Monotonicity of Positive Dependence with Time for Stationary Reversible Markov Chains*: a bivariate positive-dependence-in-time result;
- Hu--Pan (2000), *Comparisons of Dependence for Stationary Markov Processes*: supermodular/concordance lag comparisons under sufficient conditions;
- Kulik (2004), *Monotonicity in Lag for Nonmonotone Markov Chains*: a special nonmonotone doubly-stochastic class and a bivariate covariance/dependence result;
- Daduna--Szekli (2006/online archive 2016), *Dependence ordering for Markov processes on partially ordered spaces*: concordance/supermodular comparison results in stochastically monotone settings and examples beyond monotonicity.

I did not recover a later source-matching all-finite-dimensional characterization, nor an accessible statement of the exact reversible-three-state classification proved below. This is a bounded metadata/full-text search with ordinary publisher/search-index limits; it is **not** proof of worldwide openness or publication novelty. The restricted theorem's publication novelty is therefore **UNVERIFIED**. The mechanism may overlap older finite-state dependence theory and must be checked more deeply before any publication claim.

## 3. Starting point from the previous run

The preceding run established, for three observations, that the slow endpoint condition already prevents a new positive-gap obstruction. It also identified four observations as the first apparently new case. This run attacks that proposed obstruction rather than constructing another checker.

The key older theorem that remains available is the all-FDD **two-mode single-crossing criterion** from `2026-09-17T23-58-59Z__p0292-single-crossing-star.md`. I restate and prove the needed version here so that the new classification has a complete argument on this page.

Let the ordered state space be `1<2<3`, let `Q` be an irreducible reversible generator with stationary law `pi`, and write `P_t=e^{tQ}`. If the two nonzero decay rates are distinct, write

\[
0<\mu_1<\mu_2
\]

and choose `L^2(pi)`-orthonormal right eigenfunctions `v_1,v_2`. Put

\[
r^{(j)}_i=\pi_i v_j(i).
\]

Call a nonzero zero-mass signed vector `r=(r_1,r_2,r_3)` **extreme-single-crossing** if, after multiplying by `-1` if necessary, it has one of the weak sign patterns

\[
(-,-,+)\qquad\text{or}\qquad(-,+,+).
\]

Equivalently on three states, `r_1r_3\le0`.

### Lemma 3.1 — an extreme-single-crossing eigenmeasure orders its entire path

Assume `rP_t=e^{-\mu t}r` for all `t>=0`, `sum_i r_i=0`, and `r` is extreme-single-crossing. For any grid `0=t_0<t_1<...<t_m`, define the signed cylinder measure

\[
\Gamma_r(x_0,\ldots,x_m)
=r_{x_0}\prod_{j=1}^mP_{t_j-t_{j-1}}(x_{j-1},x_j).
\]

Then `Gamma_r(U)>=0` for every upper set `U` in the coordinatewise order on `{1,2,3}^{m+1}`.

**Proof.** Induct on `m`. At `m=0`, the only nontrivial upper tails are `{3}` and `{2,3}`, with masses `r_3>=0` and `-r_1>=0` after orienting the sign. For the induction step, let `U_i` be the section of `U` at first coordinate `i`; upperness gives `U_1 subseteq U_2 subseteq U_3`.

If the signs are `(-,+,+)`, use `U_1` as baseline:

\[
\Gamma_r(U)=\sum_i r_iH_i(U_1)
+r_2H_2(U_2\setminus U_1)+r_3H_3(U_3\setminus U_1),
\]

where `H_i` is the conditional future-path law from state `i`. The last two terms are nonnegative, while conditioning on the first transition and using `rP_{t_1}=e^{-\mu t_1}r` turns the first term into `e^{-\mu t_1}` times the `(m-1)`-step signed measure of `U_1`, nonnegative by induction. For `(-,-,+)`, use `U_3` as baseline and write

\[
\Gamma_r(U)=\sum_i r_iH_i(U_3)
-r_1H_1(U_3\setminus U_1)-r_2H_2(U_3\setminus U_2),
\]

with the same conclusion. `QED`

### Lemma 3.2 — two ordered signed blocks give a nonnegative supermodular coefficient

Let `Sigma_L,Sigma_R` be zero-mass signed measures on finite product posets and assume each is nonnegative on every upper set. Then for every supermodular `phi` on the product of the two blocks,

\[
\int\phi(l,r)\,\Sigma_L(dl)\Sigma_R(dr)\ge0.
\]

**Proof.** Upper-set nonnegativity is exactly stochastic domination of the normalized negative Jordan part by the normalized positive Jordan part. Couple `L^-<=L^+` and `R^-<=R^+` coordinatewise, independently across the two blocks. Supermodularity gives

\[
\phi(L^+,R^+)+\phi(L^-,R^-)
-\phi(L^+,R^-)-\phi(L^-,R^+)\ge0.
\]

Taking expectations and restoring the common Jordan masses proves the claim. `QED`

### Corollary 3.3 — two-mode single-crossing criterion

If both `r^{(1)}` and `r^{(2)}` are extreme-single-crossing, then the source's all-finite-dimensional speed order holds.

**Proof.** Fix any finite observation grid and supermodular test, and vary one gap `g` while holding all other gaps fixed. By stationarity, the Markov property, reversibility, and spectral decomposition,

\[
F(g)=C+A_1e^{-\mu_1g}+A_2e^{-\mu_2g}.
\]

The coefficient `A_j` is the integral of the original supermodular test against the product of a left signed path block and a right signed path block generated by `r^{(j)}`. Reversibility makes the time-reversed prefix use the same semigroup. Lemma 3.1 makes both signed blocks nonnegative on upper sets, and Lemma 3.2 gives `A_j>=0`. Hence `F` is nonincreasing in the selected gap. Increase all gaps one at a time when passing from speed `c_1` to `c_2`. This proves the all-FDD supermodular order. `QED`

The new work begins with the missing alternative: what if the fast mode is **not** single-crossing?

## 4. Method #1 — CHANGE THE CATEGORY: gradients turn the spectral obstruction into a two-dimensional positive-system problem

The decisive observation is that a strictly monotone **slow** eigenfunction of a reversible three-state generator forces the generator itself to be stochastically monotone.

### Lemma 4.1 — monotone slow mode forces stochastic monotonicity

Let `Q` be an irreducible reversible CTMC generator on `1<2<3`, with distinct nonzero decay rates `0<mu_1<mu_2`. If a slow eigenfunction `v` for `-mu_1` is strictly increasing or strictly decreasing across the three states, then `Q` is stochastically monotone.

**Proof.** Replace `v` by `-v` and reverse the sign if necessary, so its adjacent differences

\[
d_1=v(2)-v(1),\qquad d_2=v(3)-v(2)
\]

are both positive.

For any function `f`, write its adjacent-gradient vector as

\[
\nabla f=(f(2)-f(1),\ f(3)-f(2))^T.
\]

A direct subtraction of generator rows gives

\[
\nabla(Qf)=B\nabla f,
\quad
B=
\begin{pmatrix}
-A&\beta\\
\gamma&-D
\end{pmatrix},
\]

where

\[
A=q_{12}+q_{13}+q_{21},\qquad
D=q_{23}+q_{31}+q_{32},
\]

\[
\beta=q_{23}-q_{13},\qquad
\gamma=q_{21}-q_{31}.
\]

Thus the three-state generator is stochastically monotone exactly when `beta>=0` and `gamma>=0`: in that case `B` is Metzler and `e^{tB}` preserves nonnegative gradients; conversely, semigroup order preservation differentiated at zero forces the two off-diagonal inequalities.

Because `Qv=-mu_1v`, the positive gradient `d=(d_1,d_2)^T` obeys `Bd=-mu_1d`, i.e.

\[
\beta d_2=(A-\mu_1)d_1,
\qquad
\gamma d_1=(D-\mu_1)d_2. \tag{4.1}
\]

The eigenvalues of `B` are `-mu_1,-mu_2`, so

\[
A+D=\mu_1+\mu_2. \tag{4.2}
\]

It remains to exclude a negative `beta` or `gamma`.

If both are negative, (4.1) gives `mu_1>A` and `mu_1>D`; hence `2mu_1>A+D=mu_1+mu_2`, contradicting `mu_1<mu_2`.

For the mixed-sign cases use reversibility. Write

\[
p=\pi_1,\quad q=\pi_2,\quad r=\pi_3
\]

and the three symmetric conductances

\[
a=pq_{12}=qq_{21},\quad
b=pq_{13}=rq_{31},\quad
c=qq_{23}=rq_{32}.
\]

A direct expansion gives the exact identity

\[
pqr(A-D)
=(p+q)(ar-bq)+(q+r)(bq-cp). \tag{4.3}
\]

Now `beta<0` means `cp<bq`, while `gamma>=0` means `ar>=bq`. Equation (4.3) then gives `A>D`. But (4.1) gives `mu_1>A` from `beta<0` and `mu_1<=D` from `gamma>=0`, forcing `A<D`, a contradiction.

Similarly, `beta>=0` and `gamma<0` make both terms on the right of (4.3) nonpositive, one strict, hence `A<D`; but (4.1) gives `mu_1<=A` and `mu_1>D`, forcing `D<A`, again a contradiction.

Therefore `beta>=0` and `gamma>=0`, so `Q` is stochastically monotone. `QED`

This is the new route: the four-time cone never needs to be solved if its only potentially bad fast-mode sign pattern already forces the chain back into the classical stochastically monotone class.

## 5. Method #15 — BREAK THE SYMMETRY ON PURPOSE: split monotone and genuinely nonmonotone chains

For a reversible three-state chain, orthogonality makes the fast signed mode completely determined, up to scale, by the slow eigenfunction.

Since `r^{(2)}_i=pi_i v_2(i)`, reversibility gives

\[
\sum_i r^{(2)}_i=0,
\qquad
\sum_i r^{(2)}_i v_1(i)=0.
\]

The common orthogonal complement in `R^3` is one-dimensional, so

\[
r^{(2)}\ \propto\
\bigl(v_1(2)-v_1(3),\ v_1(3)-v_1(1),\ v_1(1)-v_1(2)\bigr). \tag{5.1}
\]

If `r^{(2)}` is not extreme-single-crossing, its endpoint entries have the same nonzero sign and the middle entry has the opposite sign. After a global sign, the pattern is strictly `(-,+,-)`. Formula (5.1) then forces either

\[
v_1(1)<v_1(2)<v_1(3)
\]

or the strict reverse ordering. Lemma 4.1 therefore forces `Q` to be stochastically monotone.

Consequently:

> **Dichotomy.** For a reversible three-state chain with distinct nonzero eigenvalues, either the fast signed eigenmeasure is extreme-single-crossing, or the chain is stochastically monotone.

The point of deliberately breaking the old symmetry is that the two branches are solved by *different* mechanisms: path-space signed-measure order in the genuinely nonmonotone branch, and Bäuerle--Rolski's classical order-preservation theorem in the monotone branch.

## 6. Main theorem — exact characterization of the entire reversible three-state class

### Theorem 6.1 — reversible three-state Problem-4 classification

Let `X` be a stationary irreducible reversible CTMC on an ordered three-point state space `1<2<3`.

If the two nonzero eigenvalues are distinct, write their decay rates as `0<mu_1<mu_2`, let `v_1` be a nonzero slow right eigenfunction, and let `pi` be the stationary law. Then the source all-finite-dimensional speed order

\[
 c_1\le c_2
 \quad\Longrightarrow\quad
 X(c_1\,\cdot)\ge_{\rm sm}X(c_2\,\cdot) \tag{6.1}
\]

holds **if and only if**

\[
\boxed{v_1(1)v_1(3)\le0.} \tag{6.2}
\]

Equivalently, with the slow signed left eigenmeasure `r^{(1)}=pi v_1`, the condition is `r^{(1)}_1r^{(1)}_3<=0`.

If the two nonzero eigenvalues coincide, (6.1) holds automatically.

#### Necessity in the distinct-spectrum case

Use the reversible spectral expansion

\[
P_t(1,3)=\pi_3\left[1+a e^{-\mu_1t}+b e^{-\mu_2t}\right],
\qquad a=v_1(1)v_1(3).
\]

If `a>0`, then for all sufficiently large `t`, the slow term dominates and `dP_t(1,3)/dt<0`. Consider the bounded bivariate supermodular test

\[
\phi(x,y)=\mathbf 1\{x\le1\}\mathbf 1\{y\le2\}.
\]

By stationarity,

\[
E\phi(X_0,X_t)=\pi_1\bigl(1-P_t(1,3)\bigr),
\]

which is then strictly **increasing** for all sufficiently large `t`. This contradicts (6.1), which requires every supermodular expectation to be nonincreasing as the speed/gap increases. Hence (6.2) is necessary.

#### Sufficiency in the distinct-spectrum case

Assume (6.2). Because `pi_i>0`, the slow signed eigenmeasure `r^{(1)}=pi v_1` has the same endpoint sign condition and is therefore extreme-single-crossing.

If `Q` is stochastically monotone, reversibility makes it doubly stochastically monotone, and the Bäuerle--Rolski sufficient theorem recorded in Leskelä's source gives the full all-FDD order (6.1).

If `Q` is not stochastically monotone, the dichotomy in Section 5 says the fast signed eigenmeasure `r^{(2)}` must be extreme-single-crossing as well. Corollary 3.3 then applies to both modes and proves (6.1).

Thus (6.2) is sufficient.

#### Repeated nonzero eigenvalue

If both nonzero eigenvalues equal `-mu`, reversibility/self-adjointness implies

\[
Q=-\mu(I-\mathbf1\pi^T),
\qquad
P_t=e^{-\mu t}I+(1-e^{-\mu t})\mathbf1\pi^T.
\]

This refresh semigroup is stochastically monotone on the ordered state space: for `i<j`, `delta_i<=_st delta_j`, and the common stationary refresh component preserves that order. Reversibility then invokes the same classical sufficient theorem, proving (6.1). `QED`

### Consequence

The four-observation obstruction proposed in the previous report **does not exist inside the reversible three-state class**. In fact, once the bivariate slow endpoint condition holds, every finite-dimensional supermodular test at every observation count is controlled. Conversely, failure of the endpoint sign gives an explicit large-lag bivariate witness.

This is a complete restricted-class answer to the source question, not a solution of Problem 4 for arbitrary stationary ergodic CTMCs. P0292 therefore remains **OPEN / NM13-01 PARTIAL**.

## 7. Method #19 — MAKE IT AN ALGORITHM: exact decision procedure for the restricted class

The proof gives a finite symbolic decision procedure for any irreducible reversible generator on three ordered states:

1. Compute the two nonzero eigenvalues.
2. If they coincide, the chain is a refresh chain and the source order holds.
3. Otherwise compute any slow eigenfunction `v_1`.
4. If `v_1(1)v_1(3)>0`, the large-lag two-coordinate test in Theorem 6.1 is an explicit source-valid obstruction.
5. If `v_1(1)v_1(3)<=0`, either the generator inequalities `q13<=q23` and `q31<=q21` hold, in which case the classical monotone theorem applies, or they do not, in which case Section 5 forces the fast mode to be single-crossing and Corollary 3.3 applies.

No numerical optimization, positive-time LP, four-time cone enumeration, or asymptotic approximation is needed. The algorithm is the proof, rather than a checker for sampled parameters.

**Outcome of #19: successful.** It converts the source's finite reversible-three-state subclass into an exact yes/no spectral test with an explicit witness on the `NO` side.

## 8. What happened to the frozen metric and the rotation counter

The frozen metric remains exactly

\[
\boxed{D_{\mathrm{rev},0}=0\to0.}
\]

It was already sharp at zero and cannot honestly be relabeled as moving because a stronger restricted theorem was proved. This is therefore the **fifth consecutive unchanged-metric run** since measurement. `stuck_recoveries_used` remains `1`.

The source-level mathematical advance is nevertheless substantial: the entire reversible three-state class is now characterized, and all four-time/higher-time work in that class is obsolete. But the owner rule is based on the frozen tracked quantity, not lemma count. The next P0292 invocation is the **sixth unchanged-metric run** if the metric again stays zero. It must not manufacture a seventh run on the same source. It should make one source-level attempt on the genuinely new class — nonreversible three-state CTMCs — and, absent actual metric movement or source closure, preserve a complete handoff and rotate to the next eligible residue-0 CLOSABLE source at the six-run gate.

The next methods, all not previously tried on P0292, are **#21, #23, #26**:

- **#21 ASK WHO ELSE HAS THIS SHAPE:** compare the nonreversible three-state problem with positive-dependence/circulation decompositions, not just reversible spectral theory;
- **#23 DO WHAT THE PROPOSER DID NOT EXPECT:** actively assume the clean reversible criterion fails once circulation is introduced and seek a source-valid exact counterexample before attempting a characterization;
- **#26 HUNT THE SPORADIC CASE:** isolate the smallest nonzero circulation family in the three-state generator and decide it exactly, rather than sampling the full parameter cone.

No audit is requested in this run. P26 and NM13-02 remain prospective independent auditors only; neither is presumed to pass.

## 9. Runtime/model and task-control status

This invocation actually ran on **GPT-5.6 Sol**; the reasoning level exposed to me is **UNVERIFIED**. It did not run on GPT-6 maximum, and I do not claim otherwise. The current scheduler/task-control interface still exposes prompt/title, schedule/offset, timing mode and enabled state, but no binding model-family selector and no reasoning-effort selector. Therefore GPT-6/maximum remains a prompt request only.

Changing that would require an authorized product/workspace/API/admin surface that exposes model and reasoning controls plus runtime attestation. The repository policy records historical `You cannot modify this task` denials for some scheduler IDs and also a later successful P26 update from another authorized context; the valid workaround is the owning/authorized surface, not duplicate-task creation or access-control bypass. No support escalation is claimed or performed here.

## 10. Structured ledger delta for P26

```yaml
ledger_delta:
  track: NM13-01
  category: CLOSABLE_OUTSIDE
  source_id: P0292
  claim_id: P0292
  canonical_dedup_key: characterize_ctmc_speed_monotonicity_in_supermodular_order
  shard_residue_mod_13: 0
  source_status: OPEN
  track_status: PARTIAL
  metric_name: D_rev_0_normalized_frozen_limit_first_order_supermodular_speed_defect
  metric_before: 0
  metric_after: 0
  metric_movement: false
  unchanged_runs_since_metric_movement: 5
  stuck_recoveries_used: 1
  methods_tried:
    - 1: gradient/Metzler reformulation of the slow-mode obstruction
    - 15: split stochastically-monotone versus genuinely-nonmonotone reversible chains
    - 19: exact symbolic decision procedure for the full reversible three-state class
  new_claim: NM13-01-P0292-REV3-FULL-05
  theorem_scope: >-
    stationary irreducible reversible CTMC on an ordered three-point state space;
    with distinct nonzero spectrum the all-finite-dimensional source speed order holds
    iff the slow eigenfunction has endpoint product <=0; repeated nonzero eigenvalue
    case always holds.
  source_closed: false
  exact_finite_artifact: none_required_parameter_uniform_symbolic_theorem
  p26_audit: NOT_REQUESTED_NOT_PASSED
  secondary_audit_NM13_02: NOT_REQUESTED_NOT_PASSED
  literature_check_date: 2026-09-18
  literature_scope: >-
    exact Leskela source/Problem 4 and source page 215; current author metadata;
    Hu-Joe 1995; Hu-Pan 2000; Kulik 2004; Daduna-Szekli dependence-order work;
    exact/reversible-three-state/later-resolution searches; bounded access and no novelty claim.
  publication_novelty: UNVERIFIED
  next_methods: [21, 23, 26]
  next_obligation: >-
    sixth-unchanged-run gate: attack nonreversible three-state CTMCs at source level;
    if the frozen metric still does not move and the source does not close, preserve a
    full handoff and rotate to the next eligible unclaimed residue-0 CLOSABLE source;
    do not continue a seventh unchanged P0292 run.
```