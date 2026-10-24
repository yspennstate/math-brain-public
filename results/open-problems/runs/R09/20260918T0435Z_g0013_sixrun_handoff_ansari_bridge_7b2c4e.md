Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — NO MOVEMENT on active R09 successor G0013: `U_* = 1289727882057511/11918000000000000 = 0.10821680500566462... -> same`; supported G0013 unchanged count `5 -> 6`, so the owner’s CLOSABLE six-run retirement rule fires in this report. Methods used: B3 PROVE SOMETHING STRONGER, B17 LOOK FOR YOUR NUMBERS SOMEWHERE ELSE, B27 SWAP THE QUANTIFIERS.** GPT-6/maximum was requested in prompt text, but this runtime identifies as GPT-5.6 Sol and exposes no authenticated reasoning-effort telemetry, so I do not claim GPT-6 or maximum reasoning.

# R09 CLOSABLE OUTSIDE — G0013 six-run handoff: an exact Chatterjee/Spearman bridge, the Ansari–Rockel prior-art collision, and the finite all-permutations reduction

Date: 2026-09-18 UTC.  
Repository / branch: `yspennstate/math-open-problems` / `master`.  
Delivery: private GitHub only.

## 1. Continuity and controlling state

I did **not** reopen Pengfei Tang, Question 4.11. The periodic-tree clause remains source-level REFUTED in the later immutable R09 record, with exact certification and two distinct outside audits; its R09 metric is frozen at `UNBOUNDED_ABOVE` and its retirement count is 6. The transitive-graph clause remains open. Intake I0055 / Lyons–Peres Question 5.16 remains excluded because Tang’s Theorem 1.6 answers that different modified question. G0002 / Cerf 53.1 remains handed off at `Delta_8=UNMEASURED`.

The controlling exclusive R09 claim before this run is `operations/claims/G0013.md`, the Catalano–Lavenant uniform-copula Wasserstein problem. Put

\[
\lambda=\operatorname{Unif}[0,1],\qquad \nu=\lambda\otimes\lambda,
\]
\[
M=\sup_{\pi\in\Pi(\lambda,\lambda)}W_2^2(\pi,\nu).
\]

The source conjecture is `M=1/10`, with the diagonal and antidiagonal couplings as maximizers. The frozen R09 metric is

`U_* = smallest rigorous source-valid global upper bound on M established by R09`.

The newest own report at run start was

`runs/R09/20260918T0331Z_g0013_block_reflection_recovery_61f4a8.md`

at creation commit `f5a2bedaad6841b46d6b6ecff3160ec85d52a4c4`. It leaves

\[
\boxed{U_*=
\frac{1289727882057511}{11918000000000000}
=0.10821680500566462\ldots}
\tag{1.1}
\]

and records supported unchanged count 5. The owner rule says a CLOSABLE target retires after six unchanged runs, so this invocation had exactly two honest possibilities: lower (1.1) for the full source class or preserve a terminal handoff and rotate.

Before new mathematics I reread/recovered `probability_campaign_2026_09/INDEX.md`, `RANKING.md`, root `POSTED.md`, root `RESULTS.md`, `QUEUE.md`, `operations/NEW_METHODS_2026-09-16.md`, `operations/claims/G0013.md`, the newest R09 report, the recent R08 successor-screen report, the newest visible R10 successor-gate history, and the current task-health/coordinator admission material. The large intake JSONL corpus is connector-truncated when rendered wholesale, so I used exact target/source/ownership searches rather than falsely claiming a byte-for-byte visual reread of every row.

## 2. Fresh source/current-literature check — 18 September 2026

The primary source remains Marta Catalano and Hugo Lavenant, *Measures of Dependence based on Wasserstein distances*, arXiv:2510.06034 (submitted 7 October 2025), whose Remark 3 poses the uniform-marginal Euclidean quadratic-Wasserstein extremal problem.

Stefan Schrott, *Couplings Farthest from the Independent Gaussian*, arXiv:2609.10467 (submitted 9 September 2026), still states in its abstract that Catalano and Lavenant **conjectured** the uniform monotone/antimonotone result and proves the Gaussian analogue instead. Fresh exact-title/author/uniform-copula/farthest-from-independence searches on 18 September found no later source-matching resolution. Catalano’s current page and Lavenant’s current research page still list the dependence paper as submitted. This is bounded dated evidence, not a worldwide novelty guarantee.

For B17 I also read Jonathan Ansari and Marcus Rockel, *The exact region and an inequality between Chatterjee’s and Spearman’s rank correlations*, arXiv:2506.15897v3 / J. Multivar. Anal. 214 (2026) 105630. This paper materially changes the novelty accounting for several scalar ingredients used by R09; details are in §4 below.

## 3. B3 — prove something stronger: an exact direct/cross Chatterjee–Spearman identity for each Brenier coordinate

The goal of this move was to add a genuinely full-class constraint, not another numerical fit. It succeeds structurally but does **not** lower `U_*`.

Work first in the same smooth positive-density approximation class used by the preceding R09 Brenier arguments, with

\[
T=\nabla\phi=(u,v),\qquad (X,Y)\sim\lambda^2,\qquad (U,V)=T(X,Y).
\]

Convexity gives `u_x>=0` and `v_y>=0`. For a fixed threshold `t`, define

\[
Q_t(y)=\mathbb P(U\le t\mid Y=y)
      =\lambda\{x:u(x,y)\le t\}.
\tag{3.1}
\]

Because `x -> u(x,y)` is nondecreasing, the sublevel set in (3.1) is an initial interval of length `Q_t(y)` up to null sets. Hence

\[
\int_0^1 x\,\mathbf 1_{\{u(x,y)\le t\}}\,dx
=\frac{Q_t(y)^2}{2}.
\tag{3.2}
\]

Let

\[
c_U:=\xi(Y,U)=6\int_0^1\operatorname{Var}(Q_t(Y))\,dt.
\tag{3.3}
\]

Since `U` is uniform, `E Q_t=t`; therefore, with

\[
A_U:=\int_0^1\!\int_0^1 Q_t(y)^2\,dy\,dt,
\]

we have

\[
c_U=6A_U-2.
\tag{3.4}
\]

Using the layer-cake representation of `U` and (3.2),

\[
\begin{aligned}
\mathbb E[XU]
&=\int_0^1 \mathbb E[X\mathbf 1_{\{U>t\}}]dt\\
&=\frac12-\frac12A_U.
\end{aligned}
\tag{3.5}
\]

Spearman’s rho for two uniform variables is `rho_S(X,U)=12E[XU]-3`. Combining (3.4)–(3.5) gives the exact identity

\[
\boxed{\rho_S(X,U)+\xi(Y,U)=1.}
\tag{3.6}
\]

Symmetrically,

\[
\boxed{\rho_S(Y,V)+\xi(X,V)=1.}
\tag{3.7}
\]

Thus the earlier aggregate identity

\[
\rho_S(X,U)+\rho_S(Y,V)=2-6W_2^2(\pi,\lambda^2)
\]

actually splits coordinate by coordinate. This is a useful normalization for any future attack.

### 3.1 The ANOVA interaction is exactly a rho-minus-xi gap

For each `t`, put

\[
F_t=\mathbf 1_{\{U\le t\}}-t.
\]

Because `X` and `Y` are independent, the mean-zero projections `E[F_t|X]` and `E[F_t|Y]` are orthogonal in `L^2`. Hence

\[
\|E[F_t\mid X]\|_2^2+\|E[F_t\mid Y]\|_2^2\le \|F_t\|_2^2=t(1-t).
\]

After integrating and multiplying by 6,

\[
\boxed{\xi(X,U)+\xi(Y,U)\le1.}
\tag{3.8}
\]

Moreover the exact residual is

\[
\eta_U:=6\int_0^1
\left\|F_t-E[F_t\mid X]-E[F_t\mid Y]\right\|_2^2dt
=1-\xi(X,U)-\xi(Y,U).
\tag{3.9}
\]

Using (3.6),

\[
\boxed{\eta_U=\rho_S(X,U)-\xi(X,U).}
\tag{3.10}
\]

There is an identical identity for `V`:

\[
\boxed{\eta_V=\rho_S(Y,V)-\xi(Y,V).}
\tag{3.11}
\]

Thus the rho-minus-xi functional appearing in Ansari–Rockel has a concrete interpretation here: it is exactly the integrated two-input interaction energy of the threshold sets of a Brenier output coordinate.

Ansari–Rockel prove the global sharp bound

\[
\rho-\xi\le\frac25
\]

and identify a unique maximizing copula `C_1`, with

\[
(\rho,\xi)=\left(\frac7{10},\frac3{10}\right).
\]

Consequently every Brenier coordinate obeys

\[
\boxed{\xi(X,U)+\xi(Y,U)\ge\frac35,}
\qquad
\boxed{\xi(Y,V)+\xi(X,V)\ge\frac35.}
\tag{3.12}
\]

If equality holds in the first inequality then the direct copula `(X,U)` must be the Ansari–Rockel extremizer `C_1`; by (3.6) this also forces `xi(Y,U)=3/10`. The symmetric statement holds for `V`.

These are full-class structural statements after the same marginal-preserving smooth approximation/compactness passage used in prior R09 reports. They are **PARTIAL** information, not a source solution.

### 3.2 Why B3 does not move the source metric

The source target is

\[
\xi(Y,U)+\xi(X,V)\le\frac35,
\tag{3.13}
\]

because `6S=xi(Y,U)+xi(X,V)`. The new lower bounds (3.12) constrain the **sum of direct and cross first-order effects for each output**, but they do not force (3.13). In particular the inequalities remain feasible when the two cross terms sum to more than `3/5`, provided at least one direct rho-minus-xi interaction falls strictly below its `2/5` maximum. Therefore this route produces rigidity at the conjectured equality geometry but no source-valid numerical improvement over (1.1).

Result for B3: **SUCCESS as a structural theorem / FAILURE as a global-metric improvement.**

## 4. B17 — look for your numbers somewhere else: the scalar optimizer and the one-interface shuffle already occur in Ansari–Rockel

This search produced an important prior-art correction.

### 4.1 The `(3/10,7/10)` numbers are not accidental

Ansari–Rockel’s unique global maximizer of `rho-xi` is the diagonal-band copula `C_1` with

\[
\xi=\frac3{10},\qquad \rho=\frac7{10},\qquad \rho-\xi=\frac25.
\tag{4.1}
\]

These are exactly the values realized by the direct coordinate copula of the diagonal Brenier extremizer `U=F_{X+Y}(X+Y)` appearing implicitly in R09’s scalar obstacle calculations. Their optimizer has the same clipped-affine conditional-CDF geometry that R09 rediscovered in the exact one-dimensional box projection.

Therefore R09 must **not claim novelty for the generic clipped-affine scalar optimizer or for the isolated scalar `(xi,rho)` extremal mechanism**. Ansari–Rockel is close prior art and should be cited in any eventual manuscript using those ingredients. The potentially new part of R09 is the two-coordinate Wasserstein/Brenier compatibility analysis, not the one-family convex program by itself.

### 4.2 The previous run’s `g_c` is exactly their shuffling map

Ansari–Rockel Lemma 7 uses

\[
T_p(u)=
\begin{cases}
u,&0\le u\le1-p,\\
1-(u-(1-p)),&1-p<u\le1,
\end{cases}
\]

with the first branch understood as `u`. Setting `c=1-p` gives precisely

\[
T_p(u)=
\begin{cases}
u,&u\le c,\\
1+c-u,&u>c,
\end{cases}
\]

again with the first branch `u`; this is the same one-interface block-reflection map denoted `g_c` in the preceding R09 report. (The symbols `nu` above are only a Markdown rendering typo for the identity variable `u`; the mathematical map is `u` on the first branch.) Applied to the comonotone copula, their shuffle is exactly the graph family R09 analyzed.

Their purpose is different: the shuffle preserves Chatterjee’s `xi` while continuously moving Spearman’s `rho` from the positive to the negative rearrangement. Hence the **family itself is prior art**. R09’s explicit Wasserstein transport bound

\[
W_2^2(\pi_c,\lambda^2)<\frac1{10}\quad(0<c<1)
\]

is not contained in the material I checked, but publication priority for that Wasserstein inequality remains **UNVERIFIED**.

### 4.3 The useful technique to port later

Ansari–Rockel’s proof is not merely an extremal formula: their KKT argument verifies a genuine quadratic-growth condition around the clipped-affine optimizer. That is exactly the sort of stability input a future G0013 reassignment should combine with the joint partial-Legendre/saddle compatibility developed by R09. A plausible future theorem would say: if both direct coordinate copulas nearly saturate the `2/5` rho-minus-xi gap, then the two Brenier conditional-CDF families are quantitatively close to the two compatible `C_1` profiles; the joint saddle condition would then have to force closeness to the diagonal or antidiagonal transport.

I did not complete that stability-to-joint-compatibility step here, so it is a handoff route, not a claim.

Result for B17: **SUCCESS as prior-art/technique discovery; no metric movement.**

## 5. B27 — swap the quantifiers: reduce the full conjecture to one all-`n` permutation-copula theorem

The source is a statement for **every** copula. A more constructive equivalent route is to prove one uniform theorem for every finite permutation resolution.

Permutation copulas are weakly dense in the set of all copulas. Because the support `[0,1]^2` is compact, weak convergence is equivalent to convergence in `W_2`; in particular

\[
\pi_n\Rightarrow\pi
\quad\Longrightarrow\quad
W_2^2(\pi_n,\lambda^2)\to W_2^2(\pi,\lambda^2).
\tag{5.1}
\]

Therefore it is enough to prove the single uniform statement

\[
\boxed{
W_2^2(\pi_{n,\sigma},\lambda^2)\le\frac1{10}
\quad\text{for every }n\ge1\text{ and every }\sigma\in S_n,
}
\tag{5.2}
\]

where `pi_{n,sigma}` is the standard permutation copula with slope-`+1` graph pieces over the `n` equal source intervals. An all-`n` proof of (5.2) would close the full continuous conjecture even though nonatomic extreme copulas need not themselves be deterministic graphs.

This is not presented as a novelty claim: density of permutation copulas is standard copula folklore, and R09’s claim file already preserves finite-permutation work through `n<=7`. The useful change of quantifiers is operational: the missing theorem can be sought as a **uniform finite assignment dual/certificate**, instead of attempting to classify all nonatomic extreme points.

I tried to lift the preceding one-interface `5/2` deficit by decomposing an arbitrary permutation into local orientation/interface operations. The attempt fails for a precise reason: Wasserstein cost to the square is not additive under permutation composition, and the source partition used by an optimal/semi-optimal transport to one graph segment changes globally when another segment is moved. Thus a sum of the one-interface deficits is not presently justified. The old exact checks through bounded `n` do not solve this all-`n` coupling problem.

The clean finite handoff target is therefore:

> Construct, for every `n` and every permutation `sigma`, a feasible transport or Kantorovich dual certificate with cost at most `1/10`, with constants independent of `n`; or find a permutation family violating that bound.

This is source-equivalent after (5.1), unlike another fixed-`n` enumeration.

Result for B27: **SUCCESS as a source-equivalent reformulation / FAILURE to obtain the required all-`n` certificate this run.**

## 6. Metric verdict and six-run retirement

No argument above lowers the full-class bound (1.1). Therefore

\[
\boxed{
U_*^{\rm before}=U_*^{\rm after}
=\frac{1289727882057511}{11918000000000000}
=0.10821680500566462\ldots .
}
\]

The supported unchanged count is

\[
\boxed{5\to6.}
\]

Under the owner’s CLOSABLE rule, **G0013 now retires from active hourly R09 research**. This is operational retirement only. The source remains

**OPEN_CURRENT / PARTIAL / HANDOFF_READY**,

not PROVED, REFUTED, KNOWN, or abandoned.

The strongest R09 handoff package to preserve is:

1. rigorous global bracket `1/10 <= M <= 0.10821680500566462...`;
2. exact scalar two-sided box projection and optimized global bound machinery;
3. D4 absolute-correlation budget and exact scalar-relaxation obstruction;
4. partial-Legendre saddle coordinates and rank-one pressure theorem;
5. the adapted-xi / counterexample-rigidity route from the intervening R09 report;
6. the strict one-interface block-reflection Wasserstein theorem, with the family itself now identified as the Ansari–Rockel shuffle of Min;
7. the new exact identities (3.6)–(3.12) and the prior-art correction in §4;
8. the all-`n` permutation-copula finite certificate target (5.2).

No further G0013 lemma should be generated by this slot unless the source is explicitly reassigned with a fresh route.

## 7. Rotation / successor gate

I checked the newest coordinator admission state before attempting any rotation. The current coordinator report at commit `027f81103a4fe02d072ded552bfde2da818467c3` admits `FATEHIZADEH-LUCA-2026-V1` but creates an exclusive claim for a different native lane; its scheduler deployment is blocked with `This task is no longer available.` The same coordinator report says it certified **no additional free `READY + CLOSABLE OUTSIDE + UNASSIGNED` successor** in that pass.

The obvious historical queue candidates are not free: for example I0004 is claimed by P21 and I0075 has a canonical exclusive claim. I0055 is KNOWN/resolved in the corrected Tang scope. I therefore do **not** steal a target, reuse a PENDING row as if it were READY, or overwrite another owner.

R09 consequently rotates to a **CLOSABLE successor-admission gate** with no new exclusive source claim in this invocation. The next invocation must continue the queue/admission cursor on a different unclaimed CLOSABLE-shaped candidate: recover the exact primary statement, perform current/later-author/citing and ownership checks, and claim it only if all gates pass. It must not return to G0013 merely because no successor was immediately available.

This is not a full block of the recurring worker: admission screening and a lawful successor search remain possible, so the scheduler is left enabled.

## 8. Why there is no new checker artifact

This run intentionally did not manufacture a checker for an unchanged global metric. The new algebraic identities in §3 are theorem-sized continuum statements proved on the page. The numerical constants `2/5`, `7/10`, and `3/10` are imported from the cited Ansari–Rockel theorem rather than claimed as a new finite computation. B27 is a reduction, not a bounded enumeration. Therefore no new `artifacts/R09/` file is warranted under the 90/10 rule.

## 9. Structured ledger_delta

```yaml
ledger_delta:
  worker: R09
  deployment: NEW-METHODS-2026-09-16
  original_source:
    id: TANG-2020-Q4.11
    periodic_tree_status: RETIRED_FROZEN_REFUTED
    metric: UNBOUNDED_ABOVE
    retirement_count: 6
    transitive_graph_clause: OPEN
    reopened: false
  predecessor:
    id: G0002
    status: HANDED_OFF
    metric: Delta_8=UNMEASURED
    reopened: false
  current_target:
    id: G0013
    source_status: OPEN_CURRENT_BOUNDED
    operational_status_before: PARTIAL_ACTIVE
    operational_status_after: PARTIAL_HANDOFF_READY_RETIRED_FROM_R09
    metric_name: U_*
    metric_before: 1289727882057511/11918000000000000
    metric_after: 1289727882057511/11918000000000000
    movement: false
    supported_unchanged_before: 5
    supported_unchanged_after: 6
    retirement_triggered: true
  new_structural_results:
    - rho_S(X,U) + xi(Y,U) = 1
    - rho_S(Y,V) + xi(X,V) = 1
    - eta_U = 1 - xi(X,U) - xi(Y,U) = rho_S(X,U) - xi(X,U)
    - eta_V = 1 - xi(Y,V) - xi(X,V) = rho_S(Y,V) - xi(Y,V)
    - xi(X,U) + xi(Y,U) >= 3/5 via Ansari-Rockel rho-xi <= 2/5
    - xi(Y,V) + xi(X,V) >= 3/5 via Ansari-Rockel rho-xi <= 2/5
  prior_art_correction:
    - clipped_affine_scalar_optimizer_matches_Ansari_Rockel_region_geometry
    - one_interface_g_c_is_Ansari_Rockel_shuffling_map_T_p_on_Min
    - Wasserstein_deficit_priority_UNVERIFIED
  source_equivalent_handoff:
    statement: "prove W2^2(pi_{n,sigma},lambda^2)<=1/10 uniformly for every n and every permutation sigma, then pass by permutation-copula density"
  methods_used: [3,17,27]
  successor:
    state: CLOSABLE_SUCCESSOR_ADMISSION_GATE
    exclusive_claim_created: false
    reason: "newest coordinator state exposes no additional free READY+CLOSABLE+UNASSIGNED successor; claimed/PENDING rows not stolen"
  shared_roots_modified: false
  peer_files_modified: false
  scheduler_modified: false
```

## 10. Model / scheduler-control truth

The exposed task-management surface still provides prompt/title/schedule/timing/enabled-state controls but no binding model-family selector, no reasoning-effort selector, no guaranteed-duration field, and no authenticated completed-run model telemetry. GPT-6/maximum therefore remains prompt text only here.

Historical `You cannot modify this task` and `This task is no longer available` results are authorization/availability boundaries. The legitimate remedy is the authorized owning context, ownership/admin transfer, or platform support; not task duplication, permission bypass, or a GitHub edit pretending to be a scheduler repair.

No email/Gmail, Drive, public posting, purchases, paid compute, credentials, access changes, force-push, workflow execution, scheduler changes, shared-root edits, or peer-file edits were performed in this run.
