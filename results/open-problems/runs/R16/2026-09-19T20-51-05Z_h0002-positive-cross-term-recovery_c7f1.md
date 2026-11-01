# R16 — positive isotonic cross-term recovery

**Model actually run: GPT-5.6 Sol. Reasoning level: UNVERIFIED — not GPT-6 maximum. FIXED-METRIC MOVEMENT: nominal Beck–Fiala stays KNOWN CURRENT-PREPRINT BASELINE at `B(t,n)<3 sqrt(2 pi t)` for all integer `t>=1`; active H0002 endpoint improves from `G_iso` to `G_cross>=G_iso`, strictly whenever `G_iso<1`. Methods actually used: #2 ATTACK THE NEGATION FIRST, #11 DUALIZE, #20 FIND WHY THE ALGORITHM FAILS.**

Status: **PARTIAL / SOURCE OPEN-LOOKING / ACTIVE** for H0002. Supported unchanged count resets to `0` because the active endpoint moved.

## 1. Continuation and source checks

This run continued the newest R16 state rather than restarting Beck–Fiala. I read the current repository roots `probability_campaign_2026_09/INDEX.md`, `RANKING.md`, `POSTED.md`, `RESULTS.md`, `QUEUE.md`, the owner directive, `operations/claims/H0002.md`, the H-intake source verification, the newest R16 report

`runs/R16/2026-09-19T19-44-01Z_h0002-full-interval-isotonic-energy_b4e9.md`,

and the neighboring same-source G0011 material.

Current primary-source check, 19 Sep 2026:

* Bansal–Jiang, arXiv:2508.03961v2, still states Beck–Fiala `O(sqrt(t))` directly only for `t>=log^2 n`, with a polylogarithmically weaker bound below that regime.
* Guo–Fang–Lu, arXiv:2609.11189v1, submitted 10 Sep 2026, states a `3 sqrt(2 pi)` Komlos bound and explicitly deduces imbalance `<3 sqrt(2 pi t)` for every integer `t>=1`, independent of `n`. Therefore literal Beck–Fiala is not an honest new-existence target for R16 at current-preprint level.
* Karingula–Lovett, ECCC TR26-188, 17 Sep 2026, independently gives a constant-36 Komlos theorem.
* Christoph–Morawski–Wigderson, arXiv:2608.19145v1, 19 Aug 2026, is still the current source surfaced for H0002 / Question 5.1. The bounded title/author/question search did not surface a later source-matching resolution. This is negative evidence, not a proof of absence.

H0002 remains exclusively owned by R16 under the frozen H1–H2–H3 sufficient-condition program. No shared root or peer file was edited.

## 2. Incoming endpoint

Retain all notation and hypotheses of the incoming full-interval isotonic-energy report. In particular, on the endpoint outside-degree coordinate `q in [0,u_P]`:

* `x(q)` is the nondecreasing normalized outside degree profile;
* `bar_t(q)` is the deterministic running anchor floor, with `bar_t(q)=0` on `[0,b_P]`, `bar_t(q)>0` for `q>b_P` in the terminal positive cell, and `bar_t(b_0)=t_0>0`;
* `y(q)=x(q)-bar_t(q)>=0` on `[0,b_0]`;
* `v(q)=exp(-Delta bar_t(q))-exp(-Delta t_0)` on `[0,b_0]`, so `v` is nonnegative and nonincreasing;
* `V_0=int_0^{b_0} v(q)dq`;
* the exact Stieltjes argument already proved

`A:=int_0^{b_0} v(q)y(q)dq >= Theta >0`;

* H2 depletion already proved the outside quadratic-energy allowance

`E_out := a_P-kappa^2 a_P^3/alpha^4`;

* the incoming full-interval opposite-monotone step gave

`int_0^{b_0} v(q)y(q)^2 dq <= M_iso`,

where

`M_iso = (V_0/u_P) E_out - B_0`,

`B_0=int_0^{b_0} v(q) bar_t(q)^2 dq >0`;

* the incoming two-moment correction was

`eta_iso = Theta g_Delta(M_iso/Theta)`,

where

`g_Delta(z)=(1-exp(-Delta z))/z`;

* and the complete endpoint was

`G_iso = min{1, G_coreavg + E_rfgap + eta_iso}`.

The incoming proof dropped the cross term in the exact identity

`y^2 = x^2 + bar_t^2 - 2 x bar_t = x^2-bar_t^2-2 bar_t y`.

Equivalently,

`int v y^2 = int v x^2 - B_0 - 2 C`,

where

`C:=int_0^{b_0} v(q)bar_t(q)y(q)dq >=0`.

The previous report retained only `C>=0`. The question this run attacked was whether an admissible profile can force `C=0` while still satisfying the already-proved weighted first moment `A>=Theta`.

## 3. New lemma: the discarded cross term is uniformly positive

Set

`v_0 := 1-exp(-Delta t_0)>0`.

On `[0,b_P]` we have `bar_t=0`, hence `v=v_0` and `y=x`. Define the zero-floor contribution

`A_0 := v_0 int_0^{b_P} x(q)dq`.

We split according to whether the established weighted first moment can be concentrated mainly on the zero-floor segment.

### Case I: `A_0 <= Theta/2`

Then

`int_{b_P}^{b_0} v(q)y(q)dq >= Theta/2`.                     (3.1)

For `h in (0,t_0)`, put

`ell(h):=Leb{q in (b_P,b_0): 0<bar_t(q)<h}`.                 (3.2)

The terminal positive-cell facts from the incoming report imply `ell(h)->0` as `h downarrow 0`: `bar_t` is continuous, equals zero at `b_P`, and is strictly positive at every point immediately to its right inside the positive cell.

On the low-floor set `L_h={0<bar_t<h}`, using `y<=x`, `v<=v_0`, Cauchy–Schwarz, and the global outside-energy allowance,

`int_{L_h} v y <= v_0 sqrt(E_out ell(h))`.                    (3.3)

Therefore on `H_h={bar_t>=h}`,

`int_{H_h} v y >= [Theta/2-v_0 sqrt(E_out ell(h))]_+`.       (3.4)

Multiplying by `bar_t>=h` on `H_h` gives

`C >= h [Theta/2-v_0 sqrt(E_out ell(h))]_+`.                 (3.5)

Define the deterministic frozen constant

`Psi_1 := sup_{0<h<t_0} h [Theta/2-v_0 sqrt(E_out ell(h))]_+`. (3.6)

Because `ell(h)->0`, some sufficiently small positive `h` makes the bracket at least `Theta/4`; hence

`Psi_1>0`.                                                   (3.7)

Thus Case I gives `C>=Psi_1`.

### Case II: `A_0 > Theta/2`

Write

`m_0:=int_0^{b_P}x(q)dq > Theta/(2v_0)`.

Since `x` is nondecreasing,

`x(q) >= x(b_P) >= m_0/b_P > c_0`, for every `q>=b_P`,       (3.8)

where

`c_0:=Theta/(2v_0 b_P)>0`.                                  (3.9)

Let

`h_2:=min{t_0/2,c_0/2}>0`,                                  (3.10)

`v_2:=exp(-Delta h_2)-exp(-Delta t_0)>0`,                    (3.11)

and

`J_2:=int_{b_P}^{b_0} bar_t(q) 1_{bar_t(q)<=h_2} dq`.        (3.12)

The continuity and strict positive-cell property imply `J_2>0`: immediately to the right of `b_P`, `bar_t` takes positive values below `h_2` on a positive-length interval.

On the set in (3.12), (3.8) and `bar_t<=h_2<=c_0/2` give

`y=x-bar_t >= c_0/2`,

while `v>=v_2`. Therefore

`C >= (c_0/2) v_2 J_2 =: Psi_2 >0`.                         (3.13)

### Uniform conclusion

Set

`Psi:=min{Psi_1,Psi_2}>0`.                                  (3.14)

Every admissible endpoint profile belongs to one of the two cases, so

`boxed: C>=Psi>0`.                                           (3.15)

This is the key new result. The attempted negation `C=0` has only two possible mechanisms: put the weighted surplus on positive-floor points, in which case Case I charges it directly; or put most of it on the zero-floor prefix, in which case monotonicity of `x` propagates a positive degree level into the positive-floor cell and Case II charges that spillover.

## 4. Strict second-moment improvement

The full-interval rearrangement inequality from the incoming report remains unchanged:

`int_0^{b_0} v x^2 <= (V_0/u_P) E_out`.                      (4.1)

Combining (4.1) with the exact identity and (3.15),

`int_0^{b_0} v y^2`
`= int_0^{b_0} v x^2 - B_0 -2C`
`<= (V_0/u_P)E_out-B_0-2Psi`
`= M_iso-2Psi`.                                               (4.2)

Define

`boxed: M_cross:=M_iso-2Psi < M_iso`.                         (4.3)

There is no positivity loophole in (4.3). For every feasible profile, Cauchy–Schwarz gives

`int v y^2 >= A^2/V_0 >= Theta^2/V_0>0`,

so the proved upper bound itself satisfies

`M_cross >= Theta^2/V_0>0`.                                  (4.4)

Thus (4.3) is a legitimate strictly smaller frozen second-moment allowance on the same graph class.

## 5. Improved absorption correction and endpoint

Use the exact two-moment lemma already proved in the R16 chain: if under a finite positive measure `mu`, `int z dmu>=A` and `int z^2 dmu<=B`, then

`int (1-exp(-Delta z)) dmu >= A g_Delta(B/A)`,                (5.1)

and the right-hand side is increasing in `A` and decreasing in `B` over the feasible range.

Apply (5.1) to `dmu=v(q)dq`, `z=y(q)`, with `A>=Theta` and the new `B<=M_cross`. This yields

`boxed: eta_cross:=Theta g_Delta(M_cross/Theta)`.             (5.2)

Since `g_Delta` is strictly decreasing on `(0,infinity)` and `M_cross<M_iso`,

`boxed: eta_cross>eta_iso`.                                  (5.3)

Define the new complete endpoint

`boxed: G_cross := min{1, G_coreavg+E_rfgap+eta_cross}`.      (5.4)

Exactly the same finite connected-core, finite sprinkling, finite-anchor/Stieltjes approximation and concentration argument used for the incoming endpoint applies: all newly used constants are frozen deterministic functionals of the same endpoint profile and H1–H2–H3 parameters. Consequently, on the unchanged class,

`Pr(L_1(G_p)>=g n) -> 1`                                     (5.5)

for every fixed

`g<G_cross`                                                   (5.6)

and every

`p >= (1+epsilon)/lambda(G)`.                                (5.7)

No endpoint attainment is claimed.

Because of (5.3),

`G_cross>=G_iso`,                                             (5.8)

and whenever the incoming endpoint is nonsaturated,

`boxed: G_iso<1 => G_cross>G_iso`.                            (5.9)

A concrete coefficient outside the entire incoming envelope in the nonsaturated case is

`g_receipt = G_iso + (1/2) min{eta_cross-eta_iso, 1-G_iso}`.  (5.10)

If `G_iso=1`, the tracked giant-fraction coefficient is already at its absolute ceiling rather than mathematically stagnant.

## 6. What the three method moves did

**#2 ATTACK THE NEGATION FIRST.** I tried to realize the exact obstruction to improving `M_iso`: an admissible profile with the discarded cross term `C=int v bar_t y` equal to zero. The two-case argument above rules out that obstruction quantitatively.

**#11 DUALIZE.** The earlier Stieltjes duality had already produced the strictly positive weighted first moment `Theta`. This run used it as a resource constraint: either that mass lies on positive floor and directly pays `C`, or putting it on the zero floor forces, by isotonicity, a positive dual payment immediately afterward.

**#20 FIND WHY THE ALGORITHM FAILS.** The previous full-interval energy calculation was not blocked by the opposite-monotone rearrangement step. Its exact loss was the algebraic relaxation

`(x-bar_t)^2 <= x^2-bar_t^2`,

which discarded `2 bar_t(x-bar_t)`. Recovering a uniform positive portion of precisely that term moves the endpoint.

The preceding triple was #30/#18/#24, so this run does not repeat it. All thirty section-B moves have appeared somewhere in the recovered H0002 history; these are honest nonconsecutive reuses, not a claim that they were historically untried.

## 7. What remains

The scalar/full-floor relaxations are now increasingly close to the genuine obstacle problem, but the exact optimizer is still unknown. The remaining variational core can be stated cleanly as: maximize the residual weighted quadratic energy

`int_0^{b_0} v(q)[x(q)-bar_t(q)]^2 dq`

among nondecreasing `x`, subject simultaneously to the complete family of prefix lower constraints, the H2-depleted global `L^2` budget, and the inherited tail constraints. A true KKT/extreme-point theorem for this isotonic moment problem could lower `M_cross` beyond the universal `2Psi` recovery. Another one-threshold split is unlikely to be the right next move.

The source-level CMW Question 5.1 remains open-ended: H0002 proves increasingly strong sufficient conditions inside the frozen H1–H2–H3 class, not a classification of all natural conditions and not a solution of every graph sequence.

## 8. Validation and checker decision

This is an analytic theorem-sized claim and its argument is on the page. There is no finite-enumeration core, so I did **not** manufacture another exact checker. The only finite/action-side work this run was source/current-status verification and repository delivery/readback.

No independent audit is claimed. Closure criteria are not met, and the correct label remains PARTIAL.

## 9. Structured ledger_delta

```yaml
ledger_delta:
  worker: R16
  active_claim: H0002
  nominal_source: Beck-Fiala 1981
  nominal_metric_before: B(t,n) < 3*sqrt(2*pi*t) for all integer t>=1, all n, current-preprint baseline
  nominal_metric_after: unchanged
  nominal_status: KNOWN_CURRENT_PREPRINT_BASELINE
  active_source: Christoph-Morawski-Wigderson arXiv:2608.19145v1 Question 5.1
  active_metric_before: G_iso
  active_metric_after: G_cross = min(1, G_coreavg + E_rfgap + eta_cross)
  strict_movement_condition: G_iso < 1
  eta_before: eta_iso = Theta*g_Delta(M_iso/Theta)
  eta_after: eta_cross = Theta*g_Delta((M_iso-2*Psi)/Theta)
  proved_gap: Psi > 0
  status: PARTIAL
  unchanged_count: 0
  methods: [2, 11, 20]
  finite_checker: not_applicable_analytic_claim
  audit_ids: []
  remaining_obligation: exact all-prefix isotonic/KKT optimizer or another source-matching strengthening
```

## 10. Runtime/model-control truth

The task-control surface exposed in this run still provides ordinary task prompt/title, schedule/start, enabled state, timing mode and related delivery metadata, but no binding model-family selector and no binding reasoning-effort selector. It also provides no authenticated per-run applied-model/reasoning receipt. Therefore `GPT-6 / maximum` remains prompt text only here; the actual model available to this run identifies as GPT-5.6 Sol and the reasoning level is UNVERIFIED.

A real fix requires platform/backend scheduler fields selecting model family and reasoning effort, propagation of those fields into inference routing, and trustworthy per-run attestation of the applied route. No scheduler change was made in this run.

The repository's current P26 history still treats the earlier `You cannot modify this task` response as an authorization-context boundary, and records later successful P26 work from an authorized context. The legitimate workaround for a still-denied task is to modify it from its owning authorized workspace/account or escalate through platform support; duplication or permission bypass is not a valid workaround.

## 11. Delivery

Intended immutable path:

`runs/R16/2026-09-19T20-51-05Z_h0002-positive-cross-term-recovery_c7f1.md`

This report is the sole R16 write for the run; no shared roots or peer files were modified.
