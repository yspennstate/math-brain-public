# R16 — layer-cake completion of the positive cross-term bound

**Model actually run: GPT-5.6 Sol. Reasoning level: UNVERIFIED — not GPT-6 maximum. FIXED-METRIC MOVEMENT: nominal Beck–Fiala remains the KNOWN CURRENT-PREPRINT BASELINE `B(t,n)<3 sqrt(2 pi t)` for every integer `t>=1`; active H0002 improves from `G_cross` to `G_layer>=G_cross`, strictly whenever `G_cross<1`. Methods actually used: #5 ADD A PARAMETER AND DIFFERENTIATE IN IT, #25 COUNT THE SAME THING TWICE, #4 PROVE SOMETHING WEAKER COMPLETELY.**

Status: **PARTIAL / SOURCE OPEN-LOOKING / ACTIVE** for H0002. Supported unchanged count stays at `0` because the active endpoint moved.

## 1. Continuation, ownership, exclusions, and current sources

This run continued the newest R16 state rather than restarting the resolved nominal Beck–Fiala source. I re-read/recovered the controlling repository surfaces required by the owner: `probability_campaign_2026_09/INDEX.md`, `probability_campaign_2026_09/RANKING.md`, root `POSTED.md`, root `RESULTS.md`, root `QUEUE.md`, `operations/new_methods_2026-09-16/OWNER_DIRECTIVE.md`, `operations/claims/H0002.md`, the H-intake verification for arXiv:2608.19145 Question 5.1, the newest R16 report

`runs/R16/2026-09-19T20-51-05Z_h0002-positive-cross-term-recovery_c7f1.md`,

and the newest same-paper neighboring handoff surfaced in the repository. H0002 remains exclusively owned by R16; the neighboring G0011 item is a distinct long-cycle question already in terminal handoff. No shared root or peer file is modified by this run.

Fresh source/status check on 2026-09-19 UTC:

* Bansal–Jiang, arXiv:2508.03961v2 (last revised 9 Sep 2025), still states Beck–Fiala `O(sqrt(t))` directly for `t>=log^2 n`, with a polylogarithmically weaker estimate below that range: https://arxiv.org/abs/2508.03961 .
* Guo–Fang–Lu, arXiv:2609.11189v1 (submitted 10 Sep 2026), proves a `3 sqrt(2 pi)` Komlós bound and explicitly deduces imbalance `<3 sqrt(2 pi t)` for every integer `t>=1`, independent of `n`: https://arxiv.org/abs/2609.11189 . Thus the literal Beck–Fiala existence target is a current-preprint baseline rather than honest new R16 progress.
* Karingula–Lovett, ECCC TR26-188 (17 Sep 2026), independently gives an elementary Komlós proof with constant `36`: https://eccc.weizmann.ac.il/report/2026/188/ .
* Altschuler, arXiv:2609.19714v1 (17 Sep 2026), gives improved **algorithmic** Beck–Fiala guarantees under bounded set size, using a Bansal–Jiang bootstrapping scheme. This is relevant follow-up literature but does not supersede the unrestricted Guo–Fang–Lu existence bound: https://arxiv.org/abs/2609.19714 .
* Christoph–Morawski–Wigderson, arXiv:2608.19145v1 (19 Aug 2026), remains the current source surfaced for H0002 / Question 5.1: https://arxiv.org/abs/2608.19145 . A bounded fresh title/author/arXiv-ID search did not surface a later source-matching resolution. This is negative evidence only, not a novelty certificate.

Therefore the nominal discrepancy metric is unchanged and labeled `KNOWN_CURRENT_PREPRINT_BASELINE`. The source-valid active successor remains H0002.

## 2. Incoming endpoint and notation

Retain all frozen H1–H2–H3 hypotheses and all endpoint notation from the incoming report. On the outside-degree coordinate `q in [0,u_P]`:

* `x(q)` is the nondecreasing normalized outside-degree profile;
* `bar_t(q)` is the continuous nondecreasing running floor, with `bar_t(q)=0` on `[0,b_P]`, `bar_t(q)>0` immediately to the right of `b_P` in the terminal positive cell, and `bar_t(b_0)=t_0>0`;
* `y(q)=x(q)-bar_t(q)>=0` on `[0,b_0]`;
* `v(q)=exp(-Delta bar_t(q))-exp(-Delta t_0)>=0` on `[0,b_0]`;
* `v_0:=1-exp(-Delta t_0)>0`;
* `V_0:=int_0^{b_0} v(q)dq`;
* the exact Stieltjes first moment satisfies

`A:=int_0^{b_0} v(q)y(q)dq >= Theta>0`;

* H2 depletion gives the global outside-energy allowance

`E_out:=a_P-kappa^2 a_P^3/alpha^4`;

* the full-interval isotonic calculation gives

`int_0^{b_0} v(q)x(q)^2 dq <= (V_0/u_P)E_out`;

* `B_0:=int_0^{b_0} v(q)bar_t(q)^2 dq>0`;
* the exact cross term is

`C:=int_0^{b_0} v(q)bar_t(q)y(q)dq`;

and the identity

`int v y^2 = int v x^2-B_0-2C`

holds exactly.

The incoming run proved a uniform `C>=Psi>0` by a two-case argument. Its constants were

`ell(h):=Leb{q in (b_P,b_0): 0<bar_t(q)<h}`,

`Psi_1:=sup_{0<h<t_0} h [Theta/2-v_0 sqrt(E_out ell(h))]_+`,

`c_0:=Theta/(2v_0 b_P)`,

`h_2:=min{t_0/2,c_0/2}`,

`v_2:=exp(-Delta h_2)-exp(-Delta t_0)`,

`J_2:=int_{b_P}^{b_0} bar_t(q) 1_{bar_t(q)<=h_2}dq`,

`Psi_2:=(c_0/2)v_2 J_2`,

and

`Psi:=min{Psi_1,Psi_2}>0`.

Consequently

`M_cross:=M_iso-2Psi`,

`eta_cross:=Theta g_Delta(M_cross/Theta)`,

`g_Delta(z):=(1-exp(-Delta z))/z`,

and the complete incoming endpoint was

`G_cross:=min{1,G_coreavg+E_rfgap+eta_cross}`.

The remaining loss in that proof is now identifiable: Case I charged only **one** floor threshold `h`, while `C` itself counts every floor level below `bar_t(q)`; Case II replaced the exact forced spillover `c_0-bar_t(q)` by the constants `c_0/2` and `v_2`.

## 3. Method #25 + #5: count the same cross term by all floor levels

Assume first the incoming Case I condition

`A_0:=v_0 int_0^{b_P}x(q)dq <= Theta/2`.

Then the weighted surplus on the positive-floor segment obeys

`int_{b_P}^{b_0} v(q)y(q)dq >= Theta/2`.                 (3.1)

For each level `h in (0,t_0)`, put

`L_h:={q in (b_P,b_0):0<bar_t(q)<h}`,

`H_h:={q in (b_P,b_0):bar_t(q)>=h}`.

The same Cauchy–Schwarz estimate used in the preceding report gives

`int_{L_h}v y <= v_0 sqrt(E_out ell(h))`.                 (3.2)

Hence the weighted surplus above level `h` satisfies

`int_{H_h}v y >= F(h)`,                                    (3.3)

where

`F(h):=[Theta/2-v_0 sqrt(E_out ell(h))]_+`.               (3.4)

Now use the layer-cake identity rather than selecting a single threshold. Since `0<=bar_t<=t_0` on the prefix,

`bar_t(q)=int_0^{t_0} 1_{h<=bar_t(q)} dh`,

so Tonelli gives the exact second count

`C`
`=int_{b_P}^{b_0} v(q)bar_t(q)y(q)dq`
`=int_0^{t_0} [int_{H_h}v(q)y(q)dq] dh`.                  (3.5)

Combining (3.3) and (3.5),

`boxed: C >= Phi_1 := int_0^{t_0} F(h) dh`.              (3.6)

This strictly improves the old single-threshold constant `Psi_1`.

To justify strictness carefully, `bar_t` is continuous and nondecreasing from `0` at `b_P` to `t_0` at `b_0`, and is positive immediately after `b_P`. Thus for any `0<h_1<h_2<t_0`, the set `{h_1<bar_t<h_2}` is a nonempty open interval (possibly a union of intervals) of positive measure, so `ell(h_2)>ell(h_1)`. Therefore `F` is strictly decreasing wherever it is positive. Also `ell(h)->0` as `h downarrow0`, hence `F(h)->Theta/2` and `F` is positive for all sufficiently small `h`.

The function `h F(h)` is upper semicontinuous on the compact interval after the natural endpoint definitions: `ell` is left-continuous and nondecreasing, so `F` is left-continuous with only downward right jumps. Hence `hF(h)` attains its maximum. At every positive maximizer `h_*`, strict decrease of `F` gives

`int_0^{h_*}F(s)ds > h_*F(h_*)`.

Thus

`boxed: Phi_1 > Psi_1`.                                    (3.7)

This is the successful `#5 ADD A PARAMETER` move: instead of optimizing over one `h`, keep the whole one-parameter family and integrate it.

## 4. Method #4: solve the second branch exactly enough, without the full KKT problem

Now assume the incoming Case II condition `A_0>Theta/2`. The preceding report already showed

`x(q)>=c_0` for every `q>=b_P`,                             (4.1)

where `c_0=Theta/(2v_0b_P)`.

Therefore on the whole positive-floor segment,

`y(q)=x(q)-bar_t(q) >= [c_0-bar_t(q)]_+`.                 (4.2)

Instead of freezing both factors at the coarse level `h_2`, retain their exact dependence on `bar_t` and define

`boxed: Phi_2 := int_{b_P}^{b_0}`
` v(q) bar_t(q) [c_0-bar_t(q)]_+ dq`.                     (4.3)

Then Case II gives simply

`boxed: C>=Phi_2`.                                         (4.4)

Moreover this strictly improves the old `Psi_2`. On the set `0<bar_t<=h_2`,

`[c_0-bar_t]_+ >= c_0/2`,

`v(q)>=v_2`,

so (4.3) implies `Phi_2>=Psi_2`. Because continuity from the zero floor gives a positive-measure set with `0<bar_t<h_2`, both displayed inequalities are strict there; hence

`boxed: Phi_2>Psi_2`.                                      (4.5)

This is deliberately weaker than solving the complete all-prefix isotonic/KKT problem, but it is complete: it removes the exact coarse relaxation used in the incoming Case II proof.

## 5. Uniform cross-term improvement

Define

`boxed: Phi:=min{Phi_1,Phi_2}`.                            (5.1)

Every admissible profile lies in Case I or Case II, so

`boxed: C>=Phi`.                                           (5.2)

By (3.7) and (4.5), both branch constants improve strictly; therefore

`boxed: Phi>min{Psi_1,Psi_2}=Psi`.                         (5.3)

This is a strict deterministic improvement on the **same** frozen endpoint class, not a new hypothesis.

The exact quadratic identity now gives

`int_0^{b_0}v y^2`
`<= (V_0/u_P)E_out-B_0-2Phi`.                              (5.4)

Define

`boxed: M_layer:=M_iso-2Phi`.                              (5.5)

Since `Phi>Psi`,

`boxed: M_layer<M_cross`.                                  (5.6)

There is no feasibility-sign problem. For every actual admissible endpoint profile,

`int v y^2 >= A^2/V_0 >= Theta^2/V_0>0`

by weighted Cauchy–Schwarz, while (5.4) is an upper bound for the same quantity. Hence on every nonempty frozen class

`M_layer>=Theta^2/V_0>0`.                                  (5.7)

If a symbolic parameter tuple violates this, it has no admissible endpoint profile and the corresponding branch is vacuous rather than a counterexample to the theorem.

## 6. Improved absorption correction and complete endpoint

Apply the exact two-moment lemma already established in the R16 chain under the measure `dmu=v(q)dq`, with

`int y dmu>=Theta`,

`int y^2 dmu<=M_layer`.

It yields

`boxed: eta_layer:=Theta g_Delta(M_layer/Theta)`.          (6.1)

Since `g_Delta` is strictly decreasing and `M_layer<M_cross`,

`boxed: eta_layer>eta_cross`.                              (6.2)

Therefore define the new complete endpoint

`boxed: G_layer:=min{1,G_coreavg+E_rfgap+eta_layer}`.      (6.3)

The finite-core, finite-sprinkling, finite-anchor/Stieltjes approximation and concentration passage is unchanged: `Phi_1` is the monotone limit of finite layer sums, while `Phi_2` is a bounded continuous functional of the same running-floor approximation. Thus, for every fixed coefficient

`g<G_layer`,                                               (6.4)

the existing proof gives

`P(L_1(G_p)>=g n)->1`                                      (6.5)

uniformly on the same frozen H1–H2–H3 class whenever

`p >= (1+epsilon)/lambda(G)`.                              (6.6)

No endpoint attainment is asserted.

Because of (6.2),

`G_layer>=G_cross`,                                        (6.7)

and whenever the incoming endpoint is below the absolute giant-fraction ceiling,

`boxed: G_cross<1 => G_layer>G_cross`.                     (6.8)

A concrete coefficient outside the complete incoming envelope in the nonsaturated case is

`g_receipt := G_cross`
` +(1/2) min{eta_layer-eta_cross, 1-G_cross}`.             (6.9)

Then `G_cross<g_receipt<G_layer`.

## 7. What the three method moves did

**#5 ADD A PARAMETER AND DIFFERENTIATE IN IT.** The incoming Case I optimized one threshold `h`. Keeping the full `h`-family and integrating it reveals that the cross term was literally a layer-cake integral. No derivative formula was needed after the parameterization; monotonicity of `ell(h)` supplies the strict gain.

**#25 COUNT THE SAME THING TWICE.** The quantity `C=int v bar_t y` was counted once as a direct `q`-integral and again as `int_0^{t_0} int_{bar_t>=h} v y dq dh`. The second count retains all level constraints simultaneously and strictly dominates the former single-level certificate.

**#4 PROVE SOMETHING WEAKER, COMPLETELY.** I did not claim the unresolved KKT/extreme-point theorem. In Case II, the already-proved monotonic propagation `x>=c_0` is enough to integrate the exact forced spillover `[c_0-bar_t]_+` and strictly improve the previous coarse constants.

The preceding triple was `#2/#11/#20`, so this run does not repeat it. The recovered H0002 history already contains all thirty section-B labels somewhere; there is therefore no honest never-before-used label left. These are nonconsecutive reuses tied to genuinely new calculations, not a claim that the labels themselves are historically new.

## 8. What was tried and not retained

I also tested replacing (3.2) by a purely global monotone-energy bound on the whole low-floor initial segment. It gives a clean estimate of the form

`int_0^r x <= r sqrt(E_out/u_P)`

for a nondecreasing profile, because the endpoint level forced at `r` persists through the remaining interval. This is potentially useful, but it does not uniformly beat the layer-cake certificate for every frozen parameter tuple without another comparison lemma. I therefore retain no metric claim from that route in this run.

Likewise I did not package a finite checker. The new claim is analytic; a grid in `h` would only approximate an already proved integral identity and would violate the owner's instruction against certificate production without a finite deciding core.

## 9. Remaining obstruction

The scalar/full-floor relaxations now use:

1. the exact running prefix deficit;
2. the exact variable exponential weight;
3. full-interval opposite-order rearrangement;
4. H2 internal-energy depletion;
5. the positive isotonic cross term; and
6. all floor levels in that cross term through layer cake.

The substantive unresolved variational core is now genuinely the simultaneous all-prefix problem: determine the maximal possible

`int_0^{b_0} v(q)[x(q)-bar_t(q)]^2 dq`

among nondecreasing `x` satisfying every prefix lower obstacle, the H2-depleted global `L^2` budget, and the inherited tail constraints. A KKT/extreme-point theorem showing that an optimizer has finitely many plateaux would be a qualitatively new next step. Another one-threshold relaxation is unlikely to be worthwhile.

H0002 remains only a strengthened sufficient-condition theorem inside the frozen H1–H2–H3 class. It does not close the open-ended CMW Question 5.1 or classify all natural graph conditions.

## 10. Validation, status, and checker decision

The theorem-sized argument is written on the page. The strict step is reduced to two elementary facts: the layer-cake identity plus strict increase of the sublevel-length function `ell(h)`, and exact integration of the monotone spillover in Case II. No finite-enumeration claim is introduced, so no checker is manufactured.

No independent audit is claimed. Closure criteria are not met. Correct status remains **PARTIAL / SOURCE OPEN-LOOKING / ACTIVE**.

## 11. Structured ledger_delta

```yaml
ledger_delta:
  worker: R16
  lane: HARD_OUTSIDE
  nominal_source: Beck-Fiala 1981
  nominal_metric_before: B(t,n) < 3*sqrt(2*pi*t) for all integer t>=1, all n, current-preprint baseline
  nominal_metric_after: unchanged
  nominal_status: KNOWN_CURRENT_PREPRINT_BASELINE
  active_claim: H0002
  active_source: Christoph-Morawski-Wigderson arXiv:2608.19145v1 Question 5.1
  active_metric_before: G_cross = min(1, G_coreavg + E_rfgap + eta_cross)
  active_metric_after: G_layer = min(1, G_coreavg + E_rfgap + eta_layer)
  strict_movement_condition: G_cross < 1
  cross_before: Psi = min(Psi_1, Psi_2)
  cross_after: Phi = min(Phi_1, Phi_2)
  proved_relation: Phi > Psi
  second_moment_before: M_cross = M_iso - 2*Psi
  second_moment_after: M_layer = M_iso - 2*Phi
  absorption_before: eta_cross = Theta*g_Delta(M_cross/Theta)
  absorption_after: eta_layer = Theta*g_Delta(M_layer/Theta)
  status: PARTIAL
  unchanged_count: 0
  methods: [5, 25, 4]
  finite_checker: not_applicable_analytic_claim
  audit_ids: []
  remaining_obligation: exact all-prefix isotonic/KKT optimizer or another source-matching strengthening
```

## 12. Runtime/model-control truth

The task-control surface available to this run still exposes ordinary prompt/title, schedule/start, enablement and timing-mode controls, but no binding model-family selector, no reasoning-effort selector, and no authenticated applied-model/reasoning receipt. Therefore `GPT-6 / maximum` remains prompt text only; this report truthfully records the model actually exposed here as GPT-5.6 Sol and the reasoning level as UNVERIFIED. Making the requested setting enforceable requires platform/backend fields for model family and reasoning effort plus per-run attestation of the applied values.

The repository's current deployment ledger records that the historical P26 `You cannot modify this task` event was authorization-context-specific and that a later P26 update succeeded from an authorized context. A task that still returns that denial must be changed from its owning authorized workspace/account or escalated through platform support. Duplication, permission bypass, or pretending the edit succeeded is not an acceptable workaround.

No scheduler change, email, Drive action, public posting, workflow execution, permission change, purchase, or peer-file edit was performed.

## 13. Delivery

Intended immutable path:

`runs/R16/2026-09-19T21-44-10Z_h0002-layer-cake-cross-term_4e7c.md`

This is the sole R16 repository write for the run.