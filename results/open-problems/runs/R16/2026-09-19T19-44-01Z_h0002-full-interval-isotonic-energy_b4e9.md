Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — this is not GPT-6 at maximum. FIXED-METRIC MOVEMENT:** the nominal Beck--Fiala metric remains the current-preprint baseline `B(t,n)<3 sqrt(2 pi t)` for every integer `t>=1` and every `n`; on the active exclusive R16/H0002 successor, the complete endpoint giant-fraction envelope moves from `G_H2sup` to `G_iso>=G_H2sup`, with `G_iso>G_H2sup` whenever `G_H2sup<1`. Methods actually used: **#30 DO ONE SCALE, ONE DIRECTION AT A TIME; #18 SAY IT IN ANOTHER LANGUAGE; #24 FIND THE EXTREMAL OBJECT**. All thirty Section-B moves have already appeared somewhere in the recovered H0002 history, so these are deliberate nonconsecutive reuses; the preceding triple was #2/#27/#5.

# R16 — H0002: full-interval opposite monotonicity plus the isotonic running floor

Date: 2026-09-19 UTC.
Target: `H0002`, HARD OUTSIDE, exclusive owner R16.
Status: **PARTIAL / source OPEN-looking / ACTIVE**.

## 1. Continuity, required reads, ownership, and current sources

This run continues from

`runs/R16/2026-09-19T18-46-32Z_h0002-endpoint-quantifier-envelope_7a42.md`

rather than restarting Beck--Fiala or any retired R16 predecessor.

Before new mathematics I re-read/reconciled:

- `probability_campaign_2026_09/INDEX.md` and `RANKING.md`;
- root `POSTED.md`, `RESULTS.md`, and `QUEUE.md`;
- `operations/NEW_METHODS_2026-09-16.md` and `operations/new_methods_2026-09-16/OWNER_DIRECTIVE.md`;
- canonical exclusive claim `operations/claims/H0002.md`;
- the H-intake identity `arxiv_2608_19145::Question 5.1; Section 5, Concluding remarks`;
- the newest own endpoint/H2-energy/Stieltjes/running-prefix reports needed for the current constants; and
- the neighboring same-paper G0011 terminal handoff. G0011 is the distinct long-cycle problem and does not conflict with H0002 ownership.

The shared root `RESULTS.md` still warns that its R-series table is stale and that newer complete own-track reports must be recovered before replacing those values. Per owner policy, this worker does not edit shared roots; the structured delta is recorded only in this immutable report.

### Current primary-source check, 2026-09-19

The nominal scheduler title is no longer an honest unresolved existence target at the current manuscript level.

- Nikhil Bansal and Haotian Jiang, *Decoupling via Affine Spectral-Independence: Beck-Fiala and Komlós Bounds Beyond Banaszczyk*, arXiv:2508.03961v2 (revised 2025-09-09), prove the Beck--Fiala `O(sqrt(t))` scale directly for `t>=log^2 n` and give a weaker polylogarithmic-loss estimate below that range. Their results are algorithmic. URL: https://arxiv.org/abs/2508.03961 .
- Shengtao Guo, Ethan X. Fang and Junwei Lu, *Vector Balancing via Directional Total Variation*, arXiv:2609.11189v1 (submitted 2026-09-10), prove the stronger Komlós theorem with constant `3 sqrt(2 pi)` and explicitly deduce set-system discrepancy `<3 sqrt(2 pi t)` for every integer `t>=1`, independent of `n`. URL: https://arxiv.org/abs/2609.11189 .
- Sankeerth Rao Karingula and Shachar Lovett, ECCC TR26-188 (posted 2026-09-17), give an elementary proof of Komlós with constant `36`. URL: https://eccc.weizmann.ac.il/report/2026/188/ .

These are extremely recent preprints / technical reports rather than mature refereed consensus. On their stated theorems, literal Beck--Fiala is a **KNOWN CURRENT-PREPRINT BASELINE**, not new R16 progress.

The active source remains Micha Christoph, Patryk Morawski and Yuval Wigderson, *The critical probability for percolation on finite graphs*, arXiv:2608.19145v1 (2026-08-19), Question 5.1. The source asks for natural conditions under which `p>=(1+epsilon)/lambda(G)` forces an `Omega(n)` component and explicitly identifies localization of the spectral radius as the main obstruction. A fresh bounded title/author/question search again surfaced the August 19 source and no later source-matching resolution. This is negative bounded-search evidence only, not a worldwide novelty certificate. URL: https://arxiv.org/abs/2608.19145 .

## 2. Incoming endpoint theorem and notation

Keep exactly the frozen H1--H2--H3 class from `operations/claims/H0002.md`. In particular, for fixed `0<epsilon<=1` and fixed `rho,kappa>0`, write

`q0:=1-exp(-epsilon^2/288)`,

`alpha:=rho*q0/64`,

`Delta:=epsilon*(7-epsilon)/(8-epsilon)>0`.

The endpoint connected core has density `a_P`, with

`b_P:=rho-a_P>0`, `u_P:=1-a_P>0`.

The terminal threshold profile is

`t(b)=[a_P/(rho-b)] [F_pad(alpha-b)/b]`,

continuously extended by `t(b_P)=0`. Retain the already-selected `b_0>b_P` and

`t_0:=t(b_0)>0`,

and define the nondecreasing running floor

`bar_t(q):=sup_{b_P<=b<=q} t(b)` on `[b_P,b_0]`, extended by zero before `b_P`. Then `bar_t(b_0)=t_0`.

For the sorted normalized outside-degree profile into the endpoint core,

`x(q)=d_W(v_q)/lambda`,

`x` is nondecreasing on `[0,u_P]`. The established all-prefix constraints are

`int_0^b x(q)dq >= b t(b)`                                      (2.1)

for every certified terminal `b`, and in particular

`int_0^{b_0}x >= b_0 t_0`,                                     (2.2)

`x(q)>=t_0` for a.e. `q in [b_0,u_P]`.                          (2.3)

The preceding H2 double-counting theorem gives the total outside spectral-energy budget

`int_0^{u_P}x(q)^2dq <= E_out`,                                 (2.4)

where

`chi_P:=kappa^2 a_P^3/alpha^4>0`,

`E_out:=a_P-chi_P`.                                             (2.5)

Combining (2.2)--(2.4), the previous report used the prefix allowance

`A_H2:=E_out-(u_P-b_0)t_0^2`,                                  (2.6)

and feasibility gives

`E_out>=u_P t_0^2`, `A_H2>=b_0 t_0^2>0`.                       (2.7)

For a finite anchor family `D`, let `L_D<=bar_t` be its nondecreasing running floor, and put

`y_D:=[x-L_D]_+`.

The Stieltjes weight is

`v(q):=exp(-Delta bar_t(q))-exp(-Delta t_0)` on `[0,b_0]`,       (2.8)

with

`V_0:=int_0^{b_0}v(q)dq>0`.                                    (2.9)

The preceding dual argument gives the exact positive weighted first moment

`int_0^{b_0}v(q)y_D(q)dq >= Theta>0`,                           (2.10)

where

`Theta=int K(s) mu(ds)`,

`K(s)=s bar_t(s)-int_0^s bar_t(q)dq`,

`mu=Delta exp(-Delta bar_t)d bar_t`.                            (2.11)

The incoming weighted second-moment allowance was

`M_H2:=(V_0/b_0) A_H2`,                                        (2.12)

and therefore

`eta_H2:=Theta g_Delta(M_H2/Theta)`,                            (2.13)

where

`g_Delta(z):=(1-exp(-Delta z))/z`, `g_Delta(0)=Delta`.          (2.14)

The newest endpoint/quantifier report proved the complete incoming envelope

`G_H2sup:=min{1,G_coreavg+E_rfgap+eta_H2}`,                     (2.15)

meaning that every fixed `g<G_H2sup` is uniformly achieved a.a.s. on the same H1--H2--H3 class for every `p>=(1+epsilon)/lambda(G)`.

This run improves the second-moment input (2.12) itself.

## 3. Method #30 — isolate the obvious H2 alpha-scale route; it does not uniformly move the full envelope

There is a tempting direct consequence of H2. Average H2 over all `alpha n`-subsets of the connected core `W`. For every outside set `B` of size `alpha n`,

`e(W,B) >= (a_P/alpha) kappa lambda n-o(lambda n)`.

Therefore, apart from fewer than `alpha n+o(n)` outside vertices,

`d_W(v) >= h_alpha lambda-o(lambda)`,

where

`h_alpha:=a_P kappa/alpha^2`.                                  (3.1)

This is a genuine deterministic quantile, but it does **not** uniformly improve the incoming complete envelope. The frozen H1--H2--H3 hypotheses do not imply `h_alpha>t_0`, nor do they imply pointwise domination of the already-optimized full-core/running-floor rate frontier. In parameter ranges with `h_alpha<=t_0`, inserting this one extra scale produces no certified gain over the existing minimax/Stieltjes theorem.

I therefore retain no metric claim from this direct alpha-scale route. Its failure identifies the right target: use the **ordering of the entire degree profile**, rather than another isolated degree threshold.

## 4. Method #18 — rewrite the remaining loss as one isotonic weighted-energy problem

The incoming estimate (2.12) applies opposite-monotone rearrangement only on the prefix `[0,b_0]` after first discarding all energy forced after `b_0`. There is a stronger formulation.

Extend the weight by zero to the entire outside interval:

`tilde_v(q):=v(q)` for `0<=q<=b_0`,

`tilde_v(q):=0` for `b_0<q<=u_P`.                              (4.1)

Because `bar_t` is nondecreasing and `v(b_0)=0`, `tilde_v` is nonincreasing on `[0,u_P]`. Since `x` is nondecreasing and nonnegative, `x^2` is nondecreasing.

The finite anchor floors also inherit the isotonic structure. If `b_j in D`, then from (2.1) and monotonicity of `x`,

`x(b_j) >= (1/b_j) int_0^{b_j}x >= t(b_j)`.                   (4.2)

Hence for `q>=b_j`, `x(q)>=t(b_j)`, and therefore

`boxed: x(q)>=L_D(q)`                                          (4.3)

for every finite anchor family `D`. Letting dense finite families approach the running supremum gives, at the endpoint,

`boxed: x(q)>=bar_t(q)` for a.e. `q<=b_0`.                    (4.4)

Thus the running floor is not merely an average obstacle; it is a genuine pointwise isotonic obstacle forced by the family of prefix inequalities.

## 5. Method #24 — solve the extremal weighted-energy relaxation exactly enough to improve `M_H2`

### 5.1 Use opposite monotonicity on the whole outside interval

For integrable oppositely monotone functions `f,g` on an interval of length `u`, the reversed Chebyshev inequality is

`int f g <= (1/u)(int f)(int g)`.                              (5.1)

Here it follows directly from

`u int f g-(int f)(int g)`
` = (1/2) int int [f(q)-f(r)][g(q)-g(r)] dq dr <=0`.           (5.2)

Apply (5.1) to `f=tilde_v` and `g=x^2` on `[0,u_P]`. Using (2.4),

`int_0^{b_0} v(q)x(q)^2dq`
` =int_0^{u_P} tilde_v(q)x(q)^2dq`
` <= (V_0/u_P) E_out`.                                        (5.3)

This already dominates the previous prefix-only Chebyshev step. Indeed, by (2.6),

`M_H2-(V_0/u_P)E_out`
` = [V_0(u_P-b_0)/(b_0 u_P)] [E_out-u_P t_0^2] >=0`.          (5.4)

### 5.2 Do not throw away the positive running floor inside the square

The old proof then used only `y_D<=x`. Equation (4.3) yields more:

`y_D=x-L_D`,                                                   (5.5)

and

`(x-L_D)^2=x^2-2L_D x+L_D^2 <= x^2-L_D^2`.                   (5.6)

Therefore

`int_0^{b_0}v(q)y_D(q)^2dq`
` <= (V_0/u_P)E_out-B_D`,                                     (5.7)

where

`B_D:=int_0^{b_0}v(q)L_D(q)^2dq`.                             (5.8)

Because `bar_t` is continuous (it is the running maximum of the continuous terminal profile `t`) and finite anchor meshes can approximate it uniformly from below, there exist nested finite families `D_m` with

`L_{D_m} -> bar_t` uniformly on `[0,b_0]`.                     (5.9)

Hence

`B_{D_m} -> B_0`,                                              (5.10)

where

`boxed: B_0:=int_0^{b_0}v(q)bar_t(q)^2dq >0`.                 (5.11)

The strict positivity in (5.11) is structural. The terminal positive cell has `t(b)>0` for `b>b_P`, while `t(b_P)=0` and `t_0>0`; by continuity, on a positive-length interval immediately to the right of `b_P` we have

`0<bar_t(q)<t_0`,

so simultaneously `bar_t(q)^2>0` and `v(q)>0`.

Define the new endpoint energy allowance

`boxed: M_iso:=(V_0/u_P) E_out-B_0`.                           (5.12)

It is nonnegative because (5.7) has a nonnegative left side along the approximating finite families; in fact `M_iso>0` follows from the positive first moment below and Cauchy--Schwarz.

### 5.3 Strict comparison with the entire incoming second-moment budget

Combining (2.6), (5.4), and (5.12) gives the exact gap

`M_H2-M_iso`
` = B_0`
` + [V_0(u_P-b_0)/(b_0 u_P)] [E_out-u_P t_0^2]`.              (5.13)

The second term is nonnegative by (2.7), and `B_0>0`. Therefore

`boxed: M_iso<M_H2`.                                           (5.14)

This is a strict structural improvement even in the extremal case where every unit of the old total-energy inequality is saturated.

## 6. Feed the sharper energy into the exact weighted two-moment theorem

The weighted first moment does not deteriorate when the floor is made dense. For every finite `D`, because `L_D<=bar_t`,

`int v y_D`
` =int v(x-L_D)`
` >=int v(x-bar_t)`
` >=Theta`.                                                     (6.1)

The last inequality is exactly the Stieltjes dual bound already proved in the incoming chain.

For the nested families `D_m`, (5.7)--(5.12) show that the weighted second moment can be made arbitrarily close to `M_iso` from above. The exact weighted two-moment lemma says that if

`A=int v y`, `B=int v y^2`,

then

`int v(1-exp(-Delta y)) >= A g_Delta(B/A)`.                   (6.2)

Since the right side increases with `A` and decreases with `B`, the endpoint correction is

`boxed: eta_iso:=Theta g_Delta(M_iso/Theta)`.                  (6.3)

Moreover, `g_Delta` is strictly decreasing on `(0,infinity)`. From (5.14),

`boxed: eta_iso>eta_H2`.                                       (6.4)

There is no zero-denominator pathology: (6.1), `Theta>0`, and Cauchy--Schwarz imply the relevant weighted second moment is positive, so `M_iso>0`.

## 7. Finite implementation and the new complete envelope

The endpoint expression above is a limit of finite certified proofs, not an uncountable probabilistic intersection.

Fix any requested final coefficient strictly below the new endpoint. Choose, in this order, all as constants independent of `n`:

1. a threshold `X` giving the inherited constant-weight contribution within a prescribed error of `E_rfgap`;
2. a sufficiently dense finite anchor family `D_m` so that `B_{D_m}>B_0-zeta` and its running floor is uniformly within the same prescribed error of `bar_t`;
3. a finite Stieltjes partition giving the weighted first-moment bound within the prescribed error of `Theta`;
4. the actual connected-core factor `c_3<1` and final sprinkling numerator `r<Delta` sufficiently close to their endpoint values.

All of these are finite choices before `n->infinity`. The already-established trimming and concentration errors are then `o(1)`. Equations (5.7) and (6.2) therefore produce every fixed weighted correction strictly below `eta_iso`, while the preceding endpoint/quantifier theorem produces every fixed base contribution strictly below `G_coreavg+E_rfgap`.

Define

`boxed: G_iso:=min{1,G_coreavg+E_rfgap+eta_iso}`.               (7.1)

### Theorem (full-interval isotonic-energy envelope)

On the unchanged frozen H1--H2--H3 class, for every fixed

`boxed: g<G_iso`,                                              (7.2)

and every

`p>=(1+epsilon)/lambda(G)`,                                    (7.3)

we have

`boxed: P(L_1(G_p)>=g n)->1`.                                 (7.4)

No endpoint attainment at `g=G_iso` is claimed.

Since `eta_iso>eta_H2`,

`G_iso>=G_H2sup`.                                               (7.5)

Whenever the incoming endpoint metric is not already saturated,

`G_H2sup<1  ==>  boxed: G_iso>G_H2sup`.                        (7.6)

For every nonsaturated frozen parameter triple a concrete coefficient outside the entire incoming envelope is

`boxed: g_receipt:=G_H2sup`
` +(1/2) min{eta_iso-eta_H2,1-G_H2sup}`,                       (7.7)

so

`G_H2sup<g_receipt<G_iso`.                                     (7.8)

If `G_H2sup=1`, the tracked giant-fraction number has already reached its absolute ceiling; (6.4) still strengthens the proof expression but cannot move a number above one.

## 8. Prior-art boundary and what is actually new in this run

The analytic mechanisms used here are classical/folklore: Chebyshev's integral inequality for oppositely monotone functions, rearrangement, monotone running maxima, Cauchy--Schwarz, and the exact two-moment inequality proved earlier in this R16 chain. A bounded search for `oppositely monotone Chebyshev integral inequality`, `rearrangement`, `isotonic weighted energy`, and the CMW source did not surface a source-matching theorem that packages the exact H0002 running-floor/Stieltjes/spectral-energy combination. That negative search is not a novelty certificate.

The retained mathematical gain is precise: the incoming proof spent H2's internal-core energy, but then allocated the remaining outside energy to the weighted prefix too generously and discarded the square of the certified running floor. Equations (5.12)--(5.14) repair both losses and strictly improve the same weighted correction term, without changing the graph class or adding a new probabilistic assumption.

## 9. What remains

This still does **not** solve the complete all-prefix isotonic/KKT problem. The new theorem uses:

- all prefix constraints to build the pointwise running obstacle;
- the entire outside interval for one opposite-monotone energy inequality; and
- the exact square of the running floor.

It does not yet optimize the residual shape `x-bar_t` under the continuum of prefix constraints. The next genuinely different target is the variational problem

`maximize int_0^{b_0} v(q)[x(q)-bar_t(q)]^2 dq`

subject to

`x nondecreasing`,

`int_0^b x >= b t(b)` for every certified `b`,

`int_0^{u_P}x^2 <= E_out`,

and the inherited tail constraints.

A finite-plateau/KKT theorem for that problem could reduce `M_iso` again. Repeating another scalar threshold or another conservative endpoint factor would not be a new route.

## 10. Checker / closure / status

No finite checker was manufactured. The new claim is analytic; its finite core is only a closed-form rearrangement identity, and the theorem-sized argument is written above. This run is a **self-check**, not an independent audit.

H0002 remains **PARTIAL / source OPEN-looking / ACTIVE**. It is a sufficient-condition theorem for the frozen H1--H2--H3 class, not a classification of all natural conditions in CMW Question 5.1. Closure protocol is therefore not triggered.

Supported unchanged count after this run: **0**, because the complete endpoint envelope moved from `G_H2sup` to `G_iso` at every nonsaturated parameter triple.

## 11. Structured ledger_delta

```yaml
ledger_delta:
  track: R16
  nominal_target: Beck-Fiala 1981 discrepancy conjecture
  nominal_metric: complete uniform B(t,n)
  nominal_value: "B(t,n) < 3*sqrt(2*pi*t) for every integer t>=1 and every n (Guo-Fang-Lu arXiv:2609.11189v1; current-preprint baseline)"
  nominal_status: KNOWN_CURRENT_PREPRINT_BASELINE
  active_target: H0002
  active_source: "Christoph-Morawski-Wigderson arXiv:2608.19145v1, Question 5.1"
  active_metric: g_twoaxis(epsilon,rho,kappa) / complete endpoint giant-fraction envelope
  before: G_H2sup
  after: G_iso
  relation: "G_iso >= G_H2sup for all frozen triples; G_iso > G_H2sup whenever G_H2sup < 1"
  new_energy_budget: "M_iso=(V_0/u_P)*(a_P-kappa^2*a_P^3/alpha^4)-int_0^{b_0} v(q)*bar_t(q)^2 dq"
  old_energy_budget: "M_H2=(V_0/b_0)*[(a_P-kappa^2*a_P^3/alpha^4)-(u_P-b_0)*t_0^2]"
  strict_gap: "M_H2-M_iso=B_0+[V_0(u_P-b_0)/(b_0 u_P)]*[E_out-u_P t_0^2] > 0"
  status: PARTIAL
  source_status: OPEN_LOOKING_BOUNDED_SEARCH_ONLY
  unchanged_count_after: 0
  closure: false
```

## 12. Model / scheduler-control status

The exposed task-control surface still provides task title/prompt, schedule/start or relative start, enablement, and timing mode. It still exposes **no binding model-family selector, no reasoning-effort selector, and no authenticated applied-model/reasoning receipt**. Therefore `GPT-6 / maximum` remains prompt-only here; making it enforceable requires platform-level model/reasoning fields plus per-run attestation.

The repository's current deployment ledger records that the historical P26 `You cannot modify this task` denial was authorization-context-specific and that a later P26 update succeeded from an authorized context. If any task still returns that denial, the compliant workaround is to modify it from its owning authorized workspace/account or escalate through platform support. Duplication or permission bypass is not valid. No scheduler modification was attempted in this run, as required by the current owner instruction.
