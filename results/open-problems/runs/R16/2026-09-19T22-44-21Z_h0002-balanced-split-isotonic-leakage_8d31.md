# R16 — balanced split and monotone low-cell energy

**Model actually run: GPT-5.6 Sol. Reasoning level: UNVERIFIED — this is not GPT-6 at maximum. FIXED-METRIC MOVEMENT: nominal Beck–Fiala remains the KNOWN CURRENT-PREPRINT BASELINE `B(t,n)<3 sqrt(2 pi t)` for every integer `t>=1`; active H0002 improves from `G_layer` to `G_split>=G_layer`, strictly whenever `G_layer<1`. Methods actually used: #13 FIND WHAT ONLY INCREASES, #27 SWAP THE QUANTIFIERS, #3 PROVE SOMETHING STRONGER.**

Status: **PARTIAL / SOURCE OPEN-LOOKING / ACTIVE** for H0002. Supported unchanged count is `0` because the active endpoint moved.

## 1. Continuation, ownership, exclusions, and source status

This run continued the newest R16 state rather than restarting the literal Beck–Fiala target. I recovered/read the current controlling repository surfaces required by the owner, including `probability_campaign_2026_09/INDEX.md`, `probability_campaign_2026_09/RANKING.md`, root `POSTED.md`, root `RESULTS.md`, root `QUEUE.md`, `operations/NEW_METHODS_2026-09-16.md`, `operations/new_methods_2026-09-16/OWNER_DIRECTIVE.md`, `operations/claims/H0002.md`, the H-intake verification for arXiv:2608.19145 Question 5.1, the newest R16 report

`runs/R16/2026-09-19T21-44-10Z_h0002-layer-cake-cross-term_4e7c.md`,

and the newest same-paper neighboring handoff surfaced by repository search. H0002 remains exclusive to R16. The neighboring G0011 item is a distinct long-cycle question already in terminal handoff. No shared root or peer file is modified by this run.

Fresh literature/status check on 2026-09-19 UTC:

* Bansal–Jiang, arXiv:2508.03961v2, directly prove the Beck–Fiala `O(sqrt(t))` scale for `t>=log^2 n`; below that range their stated bound keeps a polylogarithmic loss.
* Guo–Fang–Lu, arXiv:2609.11189v1 (10 Sep 2026), prove the stronger Komlós bound `3 sqrt(2 pi)` and explicitly deduce discrepancy `<3 sqrt(2 pi t)` for every integer `t>=1`, independent of `n`. Thus literal Beck–Fiala is a current-preprint baseline, not new R16 progress.
* Karingula–Lovett, ECCC TR26-188 (17 Sep 2026), independently give an elementary Komlós proof with constant `36`.
* Altschuler, arXiv:2609.19714v1 (17 Sep 2026), gives improved **algorithmic** Beck–Fiala guarantees under bounded row size. It does not improve the unrestricted current-preprint existence baseline above.
* Christoph–Morawski–Wigderson, arXiv:2608.19145v1 (19 Aug 2026), remains the source surfaced for H0002 / Question 5.1. A bounded fresh title/author/arXiv-ID search did not surface a later source-matching resolution. This is negative evidence only, not a novelty certificate.

Accordingly, the nominal discrepancy metric is unchanged and labeled `KNOWN_CURRENT_PREPRINT_BASELINE`; the source-valid active successor remains H0002.

## 2. Incoming endpoint and notation

Retain the frozen H1–H2–H3 assumptions and all notation from the incoming `G_layer` report. On the sorted outside-degree coordinate `q in [0,u_P]`:

* `x(q)` is nondecreasing and nonnegative;
* `bar_t(q)` is the continuous nondecreasing running floor, with `bar_t=0` on `[0,b_P]`, positive immediately to the right of `b_P` in the terminal positive cell, and `bar_t(b_0)=t_0>0`;
* `y(q):=x(q)-bar_t(q)>=0` on `[0,b_0]`;
* `v(q):=exp(-Delta bar_t(q))-exp(-Delta t_0)>=0` on `[0,b_0]`;
* `v_0:=1-exp(-Delta t_0)>0`, so `v=v_0` on `[0,b_P]`;
* `V_0:=int_0^{b_0}v(q)dq`;
* the exact Stieltjes first-moment estimate is

`A:=int_0^{b_0}v(q)y(q)dq >= Theta>0`;

* H2 depletion gives the global outside-energy budget

`E_out:=a_P-kappa^2 a_P^3/alpha^4`,

with

`int_0^{u_P}x(q)^2 dq <= E_out`;

* define

`B_0:=int_0^{b_0}v(q)bar_t(q)^2 dq>0`,

and the cross term

`C:=int_0^{b_0}v(q)bar_t(q)y(q)dq`.

The exact identity is

`int_0^{b_0}v y^2 = int_0^{b_0}v x^2-B_0-2C`.             (2.1)

The full-interval opposite-monotonicity calculation already gives

`int_0^{b_0}v x^2 <= (V_0/u_P)E_out`.                    (2.2)

Hence

`M_iso:=(V_0/u_P)E_out-B_0`                              (2.3)

is the pre-cross-term quadratic allowance.

The incoming `G_layer` report proved a better uniform lower bound `C>=Phi`, where

`ell(h):=Leb{q in (b_P,b_0):0<bar_t(q)<h}`,

`Phi_1^old:=int_0^{t_0}[Theta/2-v_0 sqrt(E_out ell(h))]_+ dh`,

`c_0:=Theta/(2v_0b_P)`,

`Phi_2^old:=int_{b_P}^{b_0}v(q)bar_t(q)[c_0-bar_t(q)]_+dq`,

`Phi:=min{Phi_1^old,Phi_2^old}>0`,

and therefore

`M_layer:=M_iso-2Phi`,

`eta_layer:=Theta g_Delta(M_layer/Theta)`,

`g_Delta(z):=(1-exp(-Delta z))/z`,

`G_layer:=min{1,G_coreavg+E_rfgap+eta_layer}`.            (2.4)

This run removes two remaining relaxations in that two-branch proof: (i) the low-floor leakage used a local Cauchy–Schwarz bound that ignored the monotone placement of energy, and (ii) the branch split was frozen at exactly `Theta/2` instead of optimized.

## 3. Method #13 — the low-floor cell is an initial segment, so it gets only its proportional share of energy

Fix `0<h<t_0` and put

`L_h:={q in (b_P,b_0):0<bar_t(q)<h}`.                    (3.1)

Because `bar_t` is continuous and nondecreasing and is positive immediately to the right of `b_P`, `L_h` is, modulo endpoints/null sets, the initial segment

`(b_P,b_P+ell(h))`.                                       (3.2)

Let

`L:=u_P-b_P>0`.                                            (3.3)

The function `x(q)^2` is nondecreasing. Therefore the average of `x^2` on any initial segment of `[b_P,u_P]` cannot exceed its average on the whole interval. Explicitly,

`int_{L_h}x(q)^2 dq`
` <= [ell(h)/L] int_{b_P}^{u_P}x(q)^2 dq`
` <= [ell(h)/L] E_out`.                                   (3.4)

Since `0<=y<=x` and `0<=v<=v_0`, Cauchy–Schwarz **after** the monotone energy allocation gives

`int_{L_h}v(q)y(q)dq`
` <= v_0 int_{L_h}x(q)dq`
` <= v_0 ell(h) sqrt(E_out/L)`.                            (3.5)

This strictly improves the incoming leakage penalty. Indeed, for every `h in (0,t_0)`,

`0<ell(h)<L`,                                               (3.6)

and hence

`ell(h)sqrt(E_out/L) < sqrt(E_out ell(h))`.                (3.7)

The strict inequality is exactly the information supplied by monotonicity: low-floor points occur first, while large values of the nondecreasing degree profile are forced to occur later.

This is the useful monovariant behind method #13: as the floor level `h` rises, `L_h` expands only from the left, so its admissible share of a nondecreasing `L^2` profile grows at most proportionally to its length.

## 4. Method #27 — optimize the branch split instead of freezing it at one half

Let `s in [0,1]`. Split according to the zero-floor weighted mass

`A_0:=int_0^{b_P}v(q)y(q)dq`
`    =v_0 int_0^{b_P}x(q)dq`.                              (4.1)

### Branch I(s): `A_0<=s Theta`

Since the total weighted first moment is at least `Theta`,

`int_{b_P}^{b_0}v(q)y(q)dq >= (1-s)Theta`.                (4.2)

For each level `h`, subtract the improved low-floor leakage (3.5). On

`H_h:={q in (b_P,b_0):bar_t(q)>=h}`,

we obtain

`int_{H_h}v(q)y(q)dq >= F_s(h)`,                           (4.3)

where

`F_s(h):=[(1-s)Theta-v_0 ell(h)sqrt(E_out/L)]_+`.          (4.4)

Layer cake gives the exact identity

`C=int_0^{t_0}[int_{H_h}v(q)y(q)dq]dh`,                   (4.5)

so Branch I(s) yields

`C>=Phi_1(s)`,                                              (4.6)

with

`Phi_1(s):=int_0^{t_0}F_s(h)dh`.                          (4.7)

### Branch II(s): `A_0>s Theta`

From (4.1),

`(1/b_P)int_0^{b_P}x(q)dq > c_s`,                         (4.8)

where

`c_s:=s Theta/(v_0 b_P)`.                                  (4.9)

Because `x` is nondecreasing, its right endpoint is at least its average, and hence

`x(q)>=c_s` for every `q>=b_P` (up to the usual a.e. representative). (4.10)

Therefore

`y(q)>=[c_s-bar_t(q)]_+` on `(b_P,b_0)`,                  (4.11)

and Branch II(s) gives

`C>=Phi_2(s)`,                                              (4.12)

where

`Phi_2(s):=int_{b_P}^{b_0}v(q)bar_t(q)[c_s-bar_t(q)]_+dq`. (4.13)

Combining the two exhaustive branches, for every fixed `s in [0,1]`,

`C>=min{Phi_1(s),Phi_2(s)}`.                               (4.14)

Now maximize the certificate rather than fixing `s=1/2`:

`boxed: Phi_split:=max_{0<=s<=1} min{Phi_1(s),Phi_2(s)}`. (4.15)

This swaps the order of the proof quantifiers correctly: for **every** admissible profile one of the two branches holds, but the analyst is free to choose the same deterministic `s` beforehand; therefore the best universal certificate is the maximum over `s` of the minimum of the two branch guarantees.

## 5. Method #3 — solve the one-dimensional minimax exactly enough and prove strict improvement

The two branch functions have opposite monotonicity.

* `Phi_1(s)` is continuous and strictly decreasing on `[0,1]` wherever it is positive. For every `s<1`, `ell(h)->0` as `h downarrow0`, so `F_s(h)>0` on a nontrivial interval of small `h`; increasing `s` subtracts a strictly positive constant from the bracket on such a set.
* `Phi_2(s)` is continuous and strictly increasing on `[0,1]`. If `s_2>s_1`, then `c_{s_2}>c_{s_1}`; continuity of the floor from `0` supplies positive measure on which the positive-part integrand strictly increases (and if both thresholds exceed `t_0`, it increases everywhere that `v bar_t>0`).
* `Phi_2(0)=0` while `Phi_1(0)>0`.
* `Phi_1(1)=0` while `Phi_2(1)>0`.

Thus there is a unique crossing `s_* in (0,1)` satisfying

`Phi_1(s_*)=Phi_2(s_*)`,                                   (5.1)

and the maximizer in (4.15) is this crossing. Equivalently, the optimized split can be found by monotone one-dimensional bisection; no finite enumeration is involved.

More importantly, `Phi_split` is **strictly larger** than the complete incoming layer-cake constant `Phi`.

At the old split `s=1/2`,

`Phi_2(1/2)=Phi_2^old`.                                    (5.2)

For Branch I, (3.7) gives pointwise

`[(Theta/2)-v_0 ell(h)sqrt(E_out/L)]_+`
` >= [(Theta/2)-v_0 sqrt(E_out ell(h))]_+`,                (5.3)

with strict inequality on a positive-measure interval of sufficiently small positive `h`. Therefore

`Phi_1(1/2)>Phi_1^old`.                                    (5.4)

There are two cases.

1. If `Phi_1^old<Phi_2^old`, then at `s=1/2` both new branches are strictly above `Phi_1^old`, so

`min{Phi_1(1/2),Phi_2(1/2)}>Phi_1^old=Phi`.                (5.5)

2. If `Phi_2^old<=Phi_1^old`, then at `s=1/2`

`Phi_1(1/2)>Phi_1^old>=Phi_2^old=Phi_2(1/2)`.              (5.6)

Increase `s` slightly. By strict increase of `Phi_2`, it becomes `>Phi_2^old`; by continuity of `Phi_1` and the strict slack in (5.6), for all sufficiently small increases it remains `>Phi_2^old`. Hence for such an `s`,

`min{Phi_1(s),Phi_2(s)}>Phi_2^old=Phi`.                    (5.7)

This covers equality as well. Consequently

`boxed: Phi_split>Phi`.                                    (5.8)

This is the stronger statement needed for induction through the existing moment bound; it does not require the still-open full KKT/extreme-point solution.

## 6. New quadratic allowance, absorption correction, and complete endpoint

From (2.1), (2.2), and the uniform bound `C>=Phi_split`,

`int_0^{b_0}v y^2 <= M_iso-2Phi_split`.                    (6.1)

Define

`boxed: M_split:=M_iso-2Phi_split`.                         (6.2)

By (5.8),

`boxed: M_split<M_layer`.                                  (6.3)

There is no sign/feasibility problem. Weighted Cauchy–Schwarz gives every actual admissible profile

`int v y^2 >= A^2/V_0 >= Theta^2/V_0>0`,                  (6.4)

while (6.1) upper-bounds the same quantity. Hence every nonempty frozen class automatically satisfies

`M_split>=Theta^2/V_0>0`.                                  (6.5)

Apply the exact two-moment lemma from the established R16 chain under `dmu=v(q)dq`. Define

`boxed: eta_split:=Theta g_Delta(M_split/Theta)`.           (6.6)

Because `g_Delta` is strictly decreasing and `M_split<M_layer`,

`boxed: eta_split>eta_layer`.                              (6.7)

Therefore the new complete endpoint is

`boxed: G_split:=min{1,G_coreavg+E_rfgap+eta_split}`.      (6.8)

The finite-core, finite-sprinkling, finite-anchor/Stieltjes passage is the same endpoint approximation scheme already justified in the incoming chain. For completeness, one may take nested finite running-floor meshes `L_D↑bar_t`; the low-level lengths and the bounded positive-part integrals converge at a.e. level, and dominated convergence gives the corresponding `Phi_1(s),Phi_2(s)` limits for any fixed `s`. Choose `s` with certificate arbitrarily close to `Phi_split`, then choose the finite mesh/sprinkling losses after fixing any strict target `g<G_split`. Thus no endpoint attainment is needed.

Consequently, on exactly the same frozen H1–H2–H3 graph class,

`P(L_1(G_p)>=g n)->1`                                      (6.9)

for every fixed

`g<G_split`                                                 (6.10)

whenever

`p >= (1+epsilon)/lambda(G)`.                              (6.11)

No endpoint attainment is claimed.

The comparison with the complete incoming envelope is

`G_split>=G_layer`,                                         (6.12)

and, below the absolute giant-fraction ceiling,

`boxed: G_layer<1 => G_split>G_layer`.                     (6.13)

A concrete coefficient outside the incoming envelope in the nonsaturated case is

`g_receipt:=G_layer`
` +(1/2)min{eta_split-eta_layer,1-G_layer}`.                (6.14)

Then `G_layer<g_receipt<G_split`.

## 7. What the three method moves actually did

**#13 FIND WHAT ONLY INCREASES.** The low-floor set grows from the left as `h` increases, while `x^2` grows with `q`. This yields the proportional initial-segment energy bound (3.4), replacing a `sqrt(ell)` leakage loss by an `ell` loss.

**#27 SWAP THE QUANTIFIERS.** The old proof fixed the dichotomy at `A_0=Theta/2`. Introducing `s` makes explicit that the proof parameter can be chosen before the adversarial profile, so the correct universal certificate is `max_s min{Phi_1(s),Phi_2(s)}`.

**#3 PROVE SOMETHING STRONGER.** Rather than merely observe an improved branch, the run proves a strict improvement of the full incoming worst-case constant, including the difficult case in which the unchanged second branch was the bottleneck at `s=1/2`.

The immediately preceding triple was `#5/#25/#4`, so this run does not repeat it. The recovered H0002 history has already used all thirty labels somewhere, so these are honest nonconsecutive reuses attached to new calculations, not a claim that the labels themselves were never tried historically.

## 8. Refutation attempt / what did not close

I also tried to force the minimax crossing to an endpoint, which would have produced a closed-form `s_*`. That fails uniformly: the shape of `ell(h)` and the distribution of `v(q)bar_t(q)` depend on the frozen terminal floor profile, so neither branch is affine in `s`. The correct reduction is one-dimensional and monotone, but not source-universally algebraic.

The larger obstruction remains the exact all-prefix isotonic/KKT extremal problem: determine the true maximum of

`int_0^{b_0}v(q)[x(q)-bar_t(q)]^2 dq`                      (8.1)

over nondecreasing `x` subject simultaneously to all prefix obstacles, the H2-depleted global `L^2` budget, and the inherited tail constraints. The present run strictly improves the relaxation feeding that problem, but it does not identify the exact extremal profile and therefore does not close source Question 5.1.

The simplest next special case worth isolating is a running floor with exactly one nonzero affine ramp followed by a plateau. In that case the one-dimensional split above is explicit enough that a genuine KKT calculation may be possible without assuming a general finite-plateau theorem.

## 9. Validation budget and closure status

No finite checker was created. The new claim is analytic and has no finite-enumeration core; manufacturing an unchanged checker would violate the owner’s 90/10 rule. The mathematical self-checks performed were:

1. `ell(h)sqrt(E_out/L) <= sqrt(E_out ell(h))` is dimensionally and algebraically correct, with strictness exactly when `0<ell(h)<L`.
2. The branch quantifiers are correct: `s` is fixed first; every admissible profile then falls into exactly one of `A_0<=sTheta` or `A_0>sTheta`.
3. The strict comparison handles both possible old bottlenecks, including equality.
4. `M_split` cannot become spuriously negative on a nonempty admissible class because it upper-bounds a weighted second moment that is at least `Theta^2/V_0`.

These are self-checks, not independent audits. H0002 remains **PARTIAL**, not PROVED/CLOSED; no paper folder is created and no audit is requested prematurely.

## 10. Model / scheduler capability check

The currently exposed task-control surface still contains task prompt/title, timing/schedule and enablement controls, but no binding model-family field, no reasoning-effort field, and no authenticated applied-model/reasoning receipt. Therefore `GPT-6 / maximum` remains a request in prompt text only and cannot honestly be claimed for this run.

To make the requested setting enforceable requires platform/backend support for (i) a binding model-family field, (ii) a binding reasoning-effort field, and (iii) per-run authenticated attestation of what was actually applied. This worker cannot add those backend fields or upgrade its own runtime.

The repository records the historical P26 `You cannot modify this task` event as authorization-context-specific and records a later successful full prompt update from an authorized context. If such a denial recurs, the legitimate remedy is modification from the owning authorized workspace/account or platform support; there is no permission-bypass or duplicate-task workaround. No scheduler change was attempted or made in this run.

## 11. Structured ledger delta

```json
{
  "task": "R16",
  "active_target": "H0002",
  "nominal_source": "Beck-Fiala 1981 discrepancy conjecture",
  "nominal_metric": "complete uniform B(t,n)",
  "nominal_before": "B(t,n)<3 sqrt(2 pi t) for every integer t>=1 (current-preprint baseline)",
  "nominal_after": "unchanged",
  "active_metric": "complete frozen H1-H2-H3 giant-fraction endpoint",
  "before": "G_layer",
  "after": "G_split",
  "movement": "strict when G_layer<1; ceiling-preserving equality possible only at 1",
  "status": "PARTIAL / SOURCE OPEN-LOOKING / ACTIVE",
  "supported_unchanged_count": 0,
  "methods": [13, 27, 3],
  "remaining_obligation": "exact all-prefix isotonic/KKT optimizer and ultimately the source-level natural-condition question",
  "canonical_claim": "operations/claims/H0002.md",
  "audit_ids": [],
  "new_artifacts": []
}
```
