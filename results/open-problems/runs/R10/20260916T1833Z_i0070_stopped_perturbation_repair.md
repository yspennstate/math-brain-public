Model: GPT-5.6 Sol. Reasoning: UNVERIFIED — **NO NUMERIC METRIC MOVEMENT** (`theta_* = 1/2` as a supremum before and after; endpoint `theta=1/2` is not claimed). Scope/proof movement: the full-source candidate `R10-I0070-C003` is hardened by a deterministic-horizon stopped-perturbation argument that removes the two largest technical gaps in the preceding run. New Section-B methods actually used: **15 (BREAK THE SYMMETRY ON PURPOSE), 20 (FIND WHY THE ALGORITHM FAILS), 21 (ASK WHO ELSE HAS THIS SHAPE)**.

Problem/source: Antonio Agresti and Mark Veraar, *Nonlinear SPDEs and Maximal Regularity: An Extended Survey*, arXiv:2501.18561v5 / NoDEA 32 (2025), Article 123, Problem 6 (“Time regularization in Hilbert spaces”). Campaign status remains **PARTIAL**. The source problem is not called closed before two independent OTHER-track audits, including P26, and prior-art clearance.

# R10 I0070 — deterministic-horizon localization repairs the compact-tail endpoint route

Run ID: `20260916T1833Z_i0070_stopped_perturbation_repair`  
Repository/branch: `yspennstate/math-open-problems` / `master`  
Dated source/status check: 2026-09-16

No email/Gmail, Drive, public posting, purchase, permission change, workflow execution, scheduler mutation, peer-file edit, or shared-root edit was performed.

## 1. Continuity, whole-repository resume, ownership, and admission

I continued from the newest immutable R10 report rather than restarting:

`runs/R10/20260916T1753Z_i0070_compact_tail_endpoint.md`.

That report retained the fixed metric

`theta_* = 1/2` as a supremum,

proved the compact-tail absorption lemma `R10-I0070-C002`, and gave the full-source endpoint candidate `R10-I0070-C003`. Its explicit audit-sensitive points were: (i) progressive/operator measurability of the rank-one perturbation, (ii) legitimate use of stochastic maximal-regularity perturbation simultaneously at `p=2` and a higher exponent, and (iii) the `r=2` conclusion.

Before new mathematics I read/recovered on current `master`:

- `probability_campaign_2026_09/INDEX.md` and `RANKING.md`;
- root `POSTED.md`, `RESULTS.md`, and `QUEUE.md`;
- `operations/NEW_METHODS_2026-09-16.md`;
- `operations/claims/I0070.md`;
- the newest complete R10 report;
- the newest neighboring Agresti–Veraar P24 report found on current master;
- the newest R11 package found by repository search;
- current exact-ID/ownership surfaces for I0070.

The connector cannot render all roughly 780 intake JSONL rows byte-for-byte in one model response. I therefore do **not** claim a manual row-by-row reread of every intake file. The exact I0070 claim, queue entry, current source, neighboring ownership, and prior attempts were rechecked directly.

The canonical claim still says `PENDING_ADMISSION, not READY`; R10 does not edit coordinator-owned claim/root files. Research-side admission evidence remains complete: the current published source still prints Problem 6; no later source resolution was found in the bounded 2026-09-16 search; I0070 is exclusively reserved to R10; P19 explicitly declined it because of that claim; P24 is on distinct Problem 3 / I0063=I0069; and the already-written Problems 4–5 package is excluded. The retired square-lattice Cardy work remains preserved in older R10 reports and is not reopened.

## 2. Exact source scope retained

The current v5/journal source states Theorem 5.7 for `p>2`, `kappa=0`. Besides the hypotheses of Theorem 4.7 it assumes the source growth bound (5.21), and it assumes

`(A,B) in SMR^bullet_{r,alpha}`

for every `r>2` and `alpha in [0,r/2-1)`. It concludes, for every `theta<1/2`, every `r>=2`, and every `0<epsilon<theta`,

`u in H^{theta,r}_loc((0,sigma);X_{1-theta}) cap C^{theta-epsilon}_loc((0,sigma);X_{1-theta})`.

Problem 6 asks whether this regularization result extends to `p=2` when `X0` is Hilbert and the critical equality occurs. At `p=2`, writing

`s_j := 2 beta_j - 1 in (0,1)`, 

the critical restriction is

`s_j(rho_j+1) <= 1`,

with equality allowed/required for at least one critical pair. I retain **all** Theorem-5.7 hypotheses, including (5.21), although the compact-tail proof below does not appear to use (5.21).

The basic p=2 solution supplied by the source has, on localizing intervals,

`u in L^2(X1) cap C(H)`,  where `H:=X_{1/2,2}`.

Since `X0` is Hilbert, `X1=D(A)` with graph norm is Hilbert, and the Hilbert interpolation space `H` is Hilbert.

## 3. Current literature screen and what is / is not new

Dated 2026-09-16 searches covered the exact Problem-6 wording, Theorem 5.7, critical p=2 Hilbert regularization, compactness/spectral-tail variants, later Agresti–Veraar papers, and recent maximal-regularity papers.

The current source is the published NoDEA article (1 September 2025) / arXiv v5 and still prints Problem 6. Lorist–van Neerven–Veraar, arXiv:2608.20266 (20 August 2026), gives sharp necessary Banach-geometry information for stochastic maximal regularity and in particular singles out Hilbert geometry at `p=2`, but it does not state the nonlinear Problem-6 regularization theorem proved below. The bounded search found no later paper resolving Problem 6. This is **not** a worldwide novelty certificate.

The perturbation step itself is not new: Agresti–Veraar Part II (J. Evol. Equ. 22 (2022), Article 56) explicitly invokes Corollary 3.15 to preserve `SMR^bullet_p` under small progressively measurable perturbations of both the deterministic and stochastic leading operators. Their continuation proof localizes on stopping events and uses the perturbation theorem after coefficient differences are made small. This run ports that architecture to the critical semilinear endpoint. The new mechanism in the R10 candidate is the source of smallness: **uniform Hilbert spectral-tail smallness of a compact solution path**, rather than smallness of a coefficient difference in the trace norm.

## 4. Retained compact-tail lemma C002

I do not re-prove the entire preceding report, but record the exact input needed below.

Let

`H=X_{1/2,2}`

and represent the Hilbert couple `(H,X1)` by a positive self-adjoint operator `L` on `H` with form domain `D(L^{1/2})=X1` and equivalent form norm. Put

`P_R = 1_[0,R](L)`.

Then `P_R -> I` strongly on `H`, `P_R` is uniformly bounded on `H` and `X1`, and

`||P_R x||_{X1} <= C R^{1/2} ||x||_H`.

Because a continuous map from a compact time interval into `H` has compact range and the `P_R` are uniformly bounded,

`sup_{t in I} ||(I-P_R)u(t)||_H -> 0`

on every compact path interval `I`.

The source reiteration at `p=2` gives, for `s_j=2beta_j-1`,

`X_{beta_j,1} = (H,X1)_{s_j,1}`

and

`||x||_{X_{beta_j,1}} <= C_j ||x||_H^(1-s_j) ||x||_{X1}^{s_j}`.

From Assumption 4.1 and `s_j(rho_j+1)<=1`, the preceding report proved:

### `R10-I0070-C002` (retained)
For every `K>0` and every `a>0` there exists `eta=eta(K,a)>0` such that for each fixed `R` there is `C=C(K,a,R)` satisfying

`||F(x)||_{X0} + ||G(x)||_{gamma(U,H)} <= a ||x||_{X1} + C`

whenever

`||x||_H<=K`,  `||(I-P_R)x||_H<=eta`.

At a critical pair the highest `X1` power is exactly one, but its coefficient contains `eta^(1-s_j)` with `1-s_j>0`; this is what can be made arbitrarily small. Strictly subcritical powers are absorbed by Young.

The exact critical-exponent arithmetic was already archived in

`artifacts/R10/20260916T1753Z_i0070_compact_tail_checker.py`

and its `.out`; this run does not manufacture a redundant checker for the same unchanged finite algebra.

## 5. Move 15 — break the symmetry: keep B nonzero and use two different SMR exponents

The most dangerous hidden strengthening in the preceding proof would have been to make `B=0`, or to use one perturbation threshold for all `p`. I therefore broke that symmetry deliberately.

Let a requested final integrability exponent be `r0>=2`, and choose one auxiliary exponent

`q > max(r0, 2, 1/epsilon)`.

The source assumptions give both

`(A,B) in SMR^bullet_{2,0}`

and

`(A,B) in SMR^bullet_{q,0}`.

Corollary 3.15 has (possibly different) deterministic/stochastic perturbation constants at exponent 2 and exponent q. Choose the scalar `a>0` in C002 smaller than **both** perturbation budgets, e.g. sufficiently small that

`Cdet_2 a + Csto_2 a < 1/2`,

`Cdet_q a + Csto_q a < 1/2`.

No common all-p estimate is needed; only the two fixed exponents `2` and `q` are used. The stochastic perturbation produced from `G` is absorbed into the existing, possibly large, nonzero operator `B`. Thus the route keeps the full nonzero-`B` source scope.

Outcome of move 15: **survives**. The proof does not need `B=0`, small `B`, or a perturbation constant uniform in `p`.

## 6. Move 20 — find why the previous algorithm could fail, then repair it

The preceding proof said “stop where the tail is small, apply the perturbation theorem, and identify by p=2 uniqueness.” Written that way, it hid two genuine obligations:

1. Corollary 3.15 is easiest to apply on a deterministic horizon, whereas the useful small-tail set is defined by a stopping time.
2. The rank-one coefficient field must be strongly progressively measurable in the sense needed by the perturbation theorem.

Both can be repaired without new assumptions.

### 6.1 A Borel rank-one decomposition

Set

`Y := X0 direct_sum_1 gamma(U,H)`,  `N(x):=(F(x),G(x))`.

On the C002 region, write `X=||x||_{X1}` and `Y0=||N(x)||_Y`, so

`Y0 <= a X + C`.

Define a scalar Borel split

- if `Y0<=C`, set `N_1(x)=0`, `N_0(x)=N(x)`;
- if `Y0>C`, set `N_0(x)= (C/Y0) N(x)` and `N_1(x)=N(x)-N_0(x)`.

Then

`||N_0(x)||_Y <= C`,  `||N_1(x)||_Y <= a||x||_{X1}`.

For `x!=0` define the rank-one operator

`R_x z = <z,x>_{X1}/||x||_{X1}^2 * N_1(x)`,

and set `R_0=0`. Then

`||R_x||_{L(X1,Y)} <= a`,  `R_x x=N_1(x)`,

so

`N(x)=R_x x + N_0(x)`.

The formula is Borel in `(x,N(x))`; projecting `Y` onto its two factors yields

`F(x)=C_x x + f_x`,

`G(x)=D_x x + g_x`,

with

`||C_x||+||D_x|| <= a`,  `||f_x||+||g_x|| <= C`.

A source strong solution is progressively measurable in `X0` and belongs to `L^2(X1)`. On the a.e. set where it is `X1`-valued, one may take the standard strongly progressively measurable `X1` representative (equivalently: on the essentially separable `X1` range, the continuous injective embedding `X1 -> X0` has a Borel inverse onto its image). Hence for each fixed `z in X1`, `C_{u(t)}z` and `D_{u(t)}z` are progressively measurable. This is precisely the strong progressive measurability required for the time-dependent perturbation pair.

This explicitly closes the measurability point left for audit in the previous report.

### 6.2 Deterministic-horizon zero extension

Fix a compact positive-time interval `[a,b] subset (0,sigma)` and choose deterministic `a0<a<T`. Let `chi` be a deterministic smooth cutoff with

`chi(a0)=0`,  `chi=1` on `[a,b]`.

Let `sigma_n` be a source localizing sequence for the p=2 maximal solution. For deterministic integers `K,R`, define the stopping time

`tau = sigma_n wedge T wedge inf{t>=a0: ||u(t)||_H >= K or ||(I-P_R)u(t)||_H >= eta}`,

where `eta=eta(K,a)` is supplied by C002 for the perturbation size fixed in Section 5.

For `t<=tau`, use the Borel decomposition above and set

`C_t=C_{u(t)}`, `D_t=D_{u(t)}`, `f_t=f_{u(t)}`, `g_t=g_{u(t)}`.

After `tau`, extend all four fields by zero. The stopped fields remain strongly progressively measurable, and

`||C_t||+||D_t||<=a`,

`||f_t||+||g_t||<=C(K,a,R)`

on the whole deterministic interval `[a0,T]`.

Now consider the **auxiliary deterministic-horizon linear equation**

`dZ + (A-C_t)Z dt = [chi f_t + 1_{t<=tau} chi' u]dt + [(B+D_t)Z + chi g_t]dW`,

`Z(a0)=0`.

All coefficient fields and forcing terms are zero-extended after `tau`. The forcing is in every finite `L^q(Omega x (a0,T))`: the remainders are deterministically bounded after localization, and `1_{t<=tau}chi'u` is bounded in `H`, hence in `X0`, by `K`.

By the choice of `a`, Corollary 3.15 gives the perturbed pair simultaneously in

`SMR^bullet_{2,0}` and `SMR^bullet_{q,0}`

on the deterministic horizon. Therefore the auxiliary equation has a unique q-solution `Z^(q)` with

`Z^(q) in H^{theta,q}(a0,T;X_{1-theta})`

for every `theta<1/2`. Since `q>2` and the underlying probability-time measure is finite, `Z^(q)` also belongs to the p=2 solution class.

On `[a0,tau]`, the cutoff process `z=chi u` satisfies **the same** auxiliary linear equation: linearity gives

`chi C_t u = C_t(chi u)=C_t z`,

`chi D_t u = D_t z`.

The p=2 uniqueness statement therefore gives

`Z^(q)=chi u`

up to `tau`.

This is the rigorous deterministic-horizon version of the localization step. It avoids applying the perturbation theorem “on a random interval” by fiat.

### 6.3 Removing the stops by compact Hilbert tails

For almost every path with `b<sigma`, choose `n` with `b<sigma_n`. Since

`u in C([a0,b];H)`, 

its range is compact and bounded. Hence there is an integer `K` with

`sup_[a0,b] ||u||_H<K`,

and, by uniform strong convergence of `P_R` on compact subsets of `H`, an integer `R` with

`sup_[a0,b] ||(I-P_R)u||_H < eta(K,a)`.

Thus `tau>b` for some triple `(n,K,R)`. The countable union over integers `n,K,R` covers `{b<sigma}`. On every event in that union,

`u = Z^(q)` on `[a,b]`,

so

`u in H^{theta,q}([a,b];X_{1-theta})`.

Since `[a,b]` was an arbitrary positive-time compact interval, this is local regularity on `(0,sigma)`.

Outcome of move 20: **the two largest implementation gaps of C003 are repaired**. The price is only a countable stopping decomposition, not a new hypothesis.

## 7. The r=2 point no longer needs a separate endpoint time theorem

The preceding report flagged `r=2` as an audit point because `SMR^bullet_{2,0}` itself has a special definition and should not be silently treated as if it already supplied every `H^{theta,2}` estimate.

The repair is simpler: for any requested `r0>=2`, choose one `q>max(r0,2)`. Section 6 yields

`u in H^{theta,q}_loc(X_{1-theta})`.

On a finite compact time interval, the standard same-smoothness embedding

`H^{theta,q} -> H^{theta,r0}`

holds for `q>=r0`. Therefore the `r0=2` conclusion follows from the higher-q estimate; no direct p=2 bullet time-regularity assertion is used. Likewise choose `q>1/epsilon` and use the one-dimensional Sobolev embedding

`H^{theta,q} -> C^{theta-1/q} -> C^{theta-epsilon}`.

Thus one large auxiliary exponent q supplies both the whole finite-r range below q and the desired Hölder exponent.

## 8. `R10-I0070-C004` — stopped compact-tail perturbation compiler

**STATUS: AUTHOR-SIDE PROVED.**

Assume exactly the p=2 Hilbert/Theorem-5.7 hypotheses recorded in Section 2 and retain C002. Fix a local p=2 solution `u`, a positive-time compact interval `[a,b]`, a target `r0>=2`, `theta<1/2`, and `0<epsilon<theta`. Choose `q>max(r0,1/epsilon,2)`. Then there exists a countable family of deterministic-horizon stopped linear perturbation problems, each satisfying the source perturbation smallness simultaneously at exponents 2 and q, whose events cover `{b<sigma}` and on which the corresponding q-solution equals `u` on `[a,b]`. Consequently

`u in H^{theta,r0}([a,b];X_{1-theta}) cap C^{theta-epsilon}([a,b];X_{1-theta})`

on `{b<sigma}`.

Dependencies: source p=2 existence/uniqueness; C002; Hilbert-couple spectral calculus; Corollary 3.15 small perturbations; the source all-r SMR hypothesis. No compact embedding, `B=0`, small-B assumption, stronger initial space, or stronger nonlinear norm is introduced.

## 9. Status of `R10-I0070-C003`

After C004, the previous full-source candidate can be restated cleanly:

> Under exactly the p=2 Hilbert specialization of the hypotheses of Theorem 5.7, with `s_j(rho_j+1)<=1` and equality allowed, the maximal solution satisfies
>
> `u in H^{theta,r}_loc((0,sigma);X_{1-theta}) cap C^{theta-epsilon}_loc((0,sigma);X_{1-theta})`
>
> for every `theta<1/2`, every `r>=2`, and every `0<epsilon<theta`.

**Author-side proof status: PROVED CANDIDATE, strengthened this run by C004. Campaign/source status: PARTIAL until the closure protocol is met.**

The fixed numeric metric remains

`theta_* = 1/2` as a supremum,

so this is the second consecutive run with no numeric metric movement after the special-model run first established that supremum. Under the owner policy the unchanged count is therefore `2`, not zero and not UNKNOWN. One more unchanged run would trigger the five-part stuck protocol unless an audit/closure event or genuine metric/scope movement changes the state.

## 10. Move 21 — who else has this shape?

The nearest source-internal analogue is Agresti–Veraar Part II itself: its continuation argument makes time/random leading-operator differences small, applies Corollary 3.15, and then removes localization. This validates the **architecture** of Section 6, but not the new compact-tail estimate C002.

The recent Lorist–van Neerven–Veraar preprint arXiv:2608.20266 proves necessary Banach-geometry conditions for stochastic maximal regularity and characterizes an endpoint `p=2` kernel condition by Hilbert geometry. It is conceptually consistent with the fact that the R10 mechanism uses Hilbert spectral calculus in an essential way. It does not state or imply C002/C004 directly.

A bounded search for “critical maximal regularity + compact spectral tail / compact path + small perturbation” found general compactness-rigidity paradigms in critical PDE, but no direct source-equivalent theorem. I therefore record the mechanism as **prior-art not cleared**, not as novel.

Outcome of move 21: the perturbation/localization half is demonstrably standard in the authors’ own toolkit; the specific tail-smallness bridge remains the part requiring independent scrutiny.

## 11. Adversarial checks of the strongest claim

I specifically tried to break C003/C004 in the following ways.

1. **Nonzero B.** Survives: the stochastic rank-one part perturbs `B` and Corollary 3.15 treats both leading operators.
2. **Different perturbation radii at p=2 and q.** Survives: choose `a` below the minimum of the two fixed budgets; no uniform-in-p constant is required.
3. **Random stopping interval.** Repaired: zero-extend coefficients/forcing and solve on a deterministic horizon.
4. **Measurability of rank-one operators.** Repaired by the explicit Borel split and Hilbert Riesz functional; use the standard `X1` progressive representative of the strong solution.
5. **r=2 conclusion.** Repaired by first proving a q>2 estimate and embedding at unchanged smoothness.
6. **Noncompact X1->H embedding.** Not needed: uniform tail convergence is on the compact path range, using strong convergence of bounded spectral projections, not compactness of the embedding.
7. **Pathwise choice of R.** Repaired by countable deterministic integers `(n,K,R)` and event decomposition; no random spectral projector is introduced.

The remaining audit-sensitive point I would ask an independent reader to check first is the exact source formulation of Corollary 3.15 at `p=2` and its bullet/time-regularity convention. The Part-II application explicitly uses that perturbation result in an `SMR^bullet_p` continuation argument, which is strong supporting evidence, but source-level closure should include a line-by-line verification of the constants/interval convention.

## 12. R11 audit status

The newest R11 package found in this run is still

`runs/R11/2026-09-16T17-42-08Z_i0054-ncrp-tangent-8b6e.md`.

The preceding R10 run already independently audited its generator/projective-convergence core and recorded a PASS at that restricted scope. No newer R11 theorem package was found on current master, so I do **not** spend the research budget duplicating the same audit. This run creates no peer-file edit.

## 13. Model/runtime and denied-task controls

The actual runtime here identifies the model as GPT-5.6 Sol; reasoning effort is not exposed, hence `UNVERIFIED`. The scheduler interface exposed to this environment offers task title/prompt, schedule, enablement, and timing-mode controls. It exposes **no model-family selector and no reasoning-effort selector**. Therefore GPT-6/maximum can be requested in prompt text but cannot be set or verified from this interface.

Repository operations records clarify the historical P26 permission issue: one native context returned `You cannot modify this task`, while a later authorized context successfully updated P26. Thus the denial is context/ownership-specific, not proof of global immutability. The legitimate repair is to use the authorized workspace/task-owner context that owns the existing task, or platform support to repair/expose that ownership. Duplicating the job or bypassing permissions is not an acceptable workaround. No scheduler mutation was attempted in this run.

## 14. Structured ledger_delta

```yaml
ledger_delta:
  source: "Agresti-Veraar, Nonlinear SPDEs and Maximal Regularity: An Extended Survey, NoDEA 32 (2025), Problem 6; arXiv:2501.18561v5"
  target: "Extend Theorem 5.7 to p=2 when X0 is Hilbert in the critical case, preserving all theorem hypotheses/norms/parameter ranges"
  metric: "largest rigorously established time-regularity exponent theta for the fixed source-admissible critical p=2 problem"
  before: "theta_* = 1/2 as supremum; endpoint 1/2 not claimed; full-source proof candidate C003 with localization/measurability audit gaps"
  after: "theta_* = 1/2 as supremum; endpoint 1/2 not claimed; C004 repairs deterministic-horizon localization, progressive rank-one measurability, nonzero-B/two-exponent perturbation, and r=2 reduction"
  numeric_movement: false
  unchanged_count: 2
  status: PARTIAL
  exact_evidence:
    - "retained exact algebra: artifacts/R10/20260916T1753Z_i0070_compact_tail_checker.py and .out"
    - "new theorem-sized proof: this immutable report, Sections 5-9"
  audit_ids: []
  closure_blockers:
    - "P26 end-to-end audit of source statement and Corollary 3.15 conventions"
    - "second independent OTHER-track end-to-end audit"
    - "prior-art clearance for compact-tail absorption mechanism"
```

## 15. Next attack if another run occurs

Do **not** re-prove C002/C004 and do not repeat methods 15/20/21. The highest-value next run is an independent-failure hunt aimed at one of two outcomes:

1. find a source-valid counterexample to the compact-tail rank-one perturbation step, especially a measurability/interval-convention failure invisible to the algebra; or
2. if none survives, turn C002+C004+C003 into the minimal self-contained source-matching paper folder **only after** the two required OTHER-track audits exist.

If the numeric metric remains unchanged for that next run, it will be the third consecutive unchanged run and the owner’s five-part stuck protocol must be triggered unless closure/audit progress genuinely changes the tracked state.

No closure claim is made in this report.
