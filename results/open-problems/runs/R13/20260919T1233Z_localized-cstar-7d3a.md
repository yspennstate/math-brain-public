Model actually run: **GPT-5.6 Sol**; reasoning level **UNVERIFIED** — this was not authenticated GPT-6 maximum. **FIXED UPPER METRIC MOVED:** `B_R13(86): 728143/100000 = 7.28143 -> 728141/100000 = 7.28141`, exact decrease `2/100000 = 0.00002`; fixed-upper unchanged count `1 -> 0`. Methods actually used: **#8 GO THE OTHER WAY AND DISCRETIZE, #12 FIND WHAT IS CONSERVED, #27 SWAP THE QUANTIFIERS.**

# R13 — Boolean Komlós: local transform-scale extraction, a conserved mean, and the active-count quantifier swap

Run ID: `20260919T1233Z_localized-cstar-7d3a`  
Repository / branch: private `yspennstate/math-open-problems` / `master`  
Worker: R13  
Lane: **HARD OUTSIDE**

## 1. Continuity, source status, ownership, and metric state

I continued from the newest immutable R13 report

`runs/R13/20260919T1129Z_balanced86-primaldual-91b4.md`

rather than restarting from the Boolean Komlós source or from the older tilted-transform calculation. The predecessor fixes

\[
K_{86}^*\le \frac{728143}{100000}=7.28143
\]

and the independent explicit lower obstruction

\[
K_{86}^*\ge \frac{225925611947}{10^{11}}=2.25925611947.
\]

Before new mathematics I reread/reconciled `probability_campaign_2026_09/INDEX.md`, `RANKING.md`, root `POSTED.md`, root `RESULTS.md`, root `QUEUE.md`, `operations/NEW_METHODS_2026-09-16.md`, the current I0091 reconciliation, the newest R13 report/checker chain, and the newest neighboring discrepancy/successor report visible in R02. The current queue explicitly records Boolean Komlós/R13 as assigned rather than free reserve inventory. I did not edit shared roots or peer-track files.

Current primary-source check on 2026-09-19:

- Guo--Fang--Lu, *Vector Balancing via Directional Total Variation*, arXiv:2609.11189, submitted 2026-09-10, prove the genuine real-sign dimension-free bound `3 sqrt(2 pi)`;
- Akbas--Sra, *Boolean Small-Ball Inequalities for Discrepancy Theory*, arXiv:2609.20785, submitted 2026-09-17, recover Komlós among their Boolean small-ball consequences;
- Bansal--Jiang, *Decoupling via Affine Spectral-Independence*, arXiv:2508.03961, and their 2026 exposition arXiv:2608.28452, remain the earlier `~O((log n)^(1/4))` real-Boolean comparison route;
- the current complex-phase paper arXiv:2609.15071 is a different signing class and is not substituted for the real Boolean problem.

Therefore the **qualitative source status is KNOWN / RESOLVED in current 2026 preprint literature**. R13 is only a finite-dimensional quantitative track. No qualitative solution claim is made here.

The immediately preceding R13 method triple was `#9/#2/#4`. This run deliberately uses three methods not used previously in the R13 history: `#8/#12/#27`.

## 2. Method #12 — FIND WHAT IS CONSERVED: the normalized inverse-gamma mean is exactly one for every exponent

The retained cosine-power family is

\[
\rho_{p,C}(x)\propto\prod_{i=1}^D
\cos^p\!\left(\frac{\pi x_i}{2C}\right),\qquad p>1.
\]

If `S_p ~ chi^2_{p+1}` and

\[
Y_p:=\frac{p-1}{S_p},
\]

then

\[
\mathbb E[S_p^{-1}]=\frac1{p-1}
\qquad\Longrightarrow\qquad
\boxed{\mathbb EY_p=1\quad\text{for every }p>1.}
\tag{2.1}
\]

Thus all homogeneous exponent choices have the same first-order Laplace behavior

\[
L_p(s)=\mathbb Ee^{-sY_p}=1-s+o(s).
\tag{2.2}
\]

The finite-`D` advantage of an exponent below the asymptotic optimizer `p=2` cannot come from changing the mean. It comes from the **nonanalytic fractional-power defect** and then competes against the deterministic directional-TV prefactor

\[
\frac{3p\sqrt{\pi/2}}{\sqrt{p-1}}.
\]

At the retained exponent

\[
p=\frac{33}{20},\qquad
\beta=\frac{13}{40},\qquad
a=\frac{53}{40},
\]

the useful transform information begins with the `s^{53/40}` term. This invariant is what suggested attacking the coefficient of that term directly rather than doing another scalar search over `p`.

**Outcome #12:** a structural reduction. No metric is claimed from (2.1) alone, but it identifies the exact finite-dimensional quantity worth sharpening and rules out a misleading mean-shift explanation for the previous `p` improvements.

## 3. Method #27 — SWAP THE QUANTIFIERS: adapt the density to the actual number of active rows?

A tempting possible improvement is to avoid the worst-case `D=139` theorem when the active-row set happens to have only `k<139` rows, and to choose the best cosine exponent after seeing `k`.

That route has an exact monotonicity barrier.

Let `Y_1,Y_2,...` be iid nonnegative integrable random variables and

\[
\bar Y_D=\frac1D\sum_{i=1}^D Y_i.
\]

The weight vector

\[
(1/D,\ldots,1/D,0)
\]

majorizes

\[
(1/(D+1),\ldots,1/(D+1)).
\]

For exchangeable iid coordinates, weighted sums are ordered accordingly in convex order. Since `sqrt(x)` is concave,

\[
\boxed{
\mathbb E\sqrt{\bar Y_D}
\le
\mathbb E\sqrt{\bar Y_{D+1}}.}
\tag{3.1}
\]

Apply this to `Y_p=(p-1)/S_p`. For every fixed `p>1`,

\[
C_{p,D}:=
\frac{3p\sqrt{\pi/2}}{\sqrt{p-1}}
\mathbb E\sqrt{\bar Y_D}
\]

is nondecreasing in `D`. Therefore the pointwise optimized family

\[
C_D^{\rm hom}:=\inf_{p>1}C_{p,D}
\]

is also nondecreasing: for `D_1<D_2`, every `p` satisfies `C_{p,D_1}\le C_{p,D_2}`, so taking the infimum preserves the inequality.

Hence, within the homogeneous cosine-power/active-row framework, allowing the exponent to depend on the realized active count does **not** improve the worst case over `k<=139`: it is still attained at `k=139`.

**Outcome #27:** rigorous failure of the adaptive-active-count quantifier swap. A future improvement must change the finite-`D` transform bound, the density family, or the row-pruning mechanism itself; merely optimizing `p` after learning `k` cannot beat the `k=139` worst case.

## 4. Method #8 — DISCRETIZE THE SCALE: isolate a short transform interval and extract a new certified defect increment

This method moves the fixed metric.

For `p=33/20`, the predecessor has

\[
Y\sim\operatorname{InvGamma}\left(\frac{53}{40},\frac{13}{40}\right),
\qquad
X_D=\frac1D\sum_{i=1}^D Y_i,
\]

and

\[
C_{33/20,D}
=
\frac{3p\sqrt{\pi/2}}{\sqrt{p-1}}
\mathbb E\sqrt{X_D}.
\tag{4.1}
\]

Its exact Frobenius decomposition has a positive nonanalytic coefficient

\[
c_*=
\frac{\beta^{\beta-1}}{1+\beta}
\frac{\Gamma(1-\beta)}{\Gamma(\beta)},
\qquad \beta=\frac{13}{40}.
\tag{4.2}
\]

The previous global certificate used only

\[
c_*>0.78472.
\]

### 4.1 Sharpening only the coefficient

Let

\[
P_N=\prod_{k=0}^{N-1}\frac{40k+13}{40k+27}.
\]

The same Gautschi inequality used by the predecessor gives

\[
c_*^{40}>
\beta^{-27}P_N^{40}(N-\beta)^{14}(1+\beta)^{-40}.
\tag{4.3}
\]

At `N=10000`, exact integer/rational arithmetic proves

\[
\boxed{c_*>\frac{78476}{100000}=0.78476.}
\tag{4.4}
\]

Thus relative to the old lower transform we gain

\[
\Delta c=rac{4}{100000}.
\tag{4.5}
\]

The exact checker also reconstructs the predecessor's tilted lower polynomial and re-verifies its pointwise positivity margin

\[
Z_{\rm old}(u)\ge0
\quad(0\le u\le43/40),
\]

with certified factor margin

\[
0.0008358012867340186\ldots>0.
\tag{4.6}
\]

### 4.2 Do not rebuild the whole global polynomial

Write

\[
G(s)=e^sL(s).
\]

The predecessor proof has `G>=1+Z_old`, and its six retained binomial layers give a certified lower integrand `B_old`. Because the true positive Frobenius factor and `e^s` are both at least one, (4.4) strengthens the true transform by at least

\[
\Delta c\,s^{53/40}.
\]

Since `Z_old>=0`,

\[
G(s)^{139}-1
\ge
B_{\rm old}(s)+139\,\Delta c\,s^{53/40}.
\tag{4.7}
\]

Now localize instead of re-expanding globally. Put

\[
t=u^{40},\qquad 0\le u\le U:=\frac{41}{40},
\qquad T=U^{40}=2.6850638383\ldots .
\]

The degree-nine odd Taylor polynomial

\[
W_9(t)=\sum_{j=0}^9\frac{(-t)^j}{j!}
\]

is a global lower bound for `e^{-t}` by Taylor's theorem. After `t=u^{40}`, the entire incremental integral is rational:

\[
J
:=\int_0^T W_9(t)t^{-7/40}\,dt
=
40\sum_{j=0}^9
\frac{(-1)^j}{j!}
\frac{U^{33+40j}}{33+40j}.
\tag{4.8}
\]

Exact arithmetic gives

\[
J=1.081744371031429\ldots>0.
\]

The predecessor certificate also proves

\[
139^{-1/40}>\frac{8839437}{10^7},
\qquad
\frac1{2\sqrt\pi}>\frac{500000}{1772454}.
\]

Therefore the old Jensen-defect floor gains the **independent positive increment**

\[
\Delta_{\rm loc}
=
\frac{4}{100000}
\left(\frac{8839437}{10^7}\right)^{13}
J
\frac{500000}{1772454},
\tag{4.9}
\]

and the exact checker proves

\[
\boxed{\Delta_{\rm loc}>2.4552715423799785\times10^{-6}.}
\tag{4.10}
\]

Using only the predecessor's weaker rational floor

\[
1-\mathbb E\sqrt{X_{139}}
>\frac{53745767}{10^9},
\]

we now have

\[
1-\mathbb E\sqrt{X_{139}}
>
\frac{53745767}{10^9}+\Delta_{\rm loc}
=0.05374822227154238\ldots .
\tag{4.11}
\]

The retained exact prefactor majorant is

\[
\frac{3p\sqrt{\pi/2}}{\sqrt{p-1}}
<\frac{7694998}{10^6}=7.694998.
\]

Combining with (4.11),

\[
C_{33/20,139}
<7.2814055371169255\ldots
<\boxed{\frac{728141}{100000}=7.28141}.
\tag{4.12}
\]

This is not another scalar `p`-tuning pass. The exponent stays fixed at `33/20`; the new proof isolates one transform scale and adds a certified fractional-power contribution on top of the already archived global certificate.

**Outcome #8:** success; the fixed metric moves.

## 5. Row pruning and the new source-matching finite-dimensional theorem

Set

\[
h=\frac{728141}{100000}=7.28141.
\]

For an arbitrary real `m x 86` matrix whose columns have Euclidean norm at most one, call row `r_i` active when

\[
\|r_i\|_2>\frac h{\sqrt{86}}.
\]

Since

\[
\sum_i\|r_i\|_2^2\le86
\]

and exact arithmetic gives

\[
139<\frac{86^2}{h^2}
=139.49734139229653\ldots<140,
\tag{5.1}
\]

there are at most `139` active rows. The `D=139` real-Boolean DTV theorem with (4.12) handles the active rows; Cauchy--Schwarz gives at most `h` on every inactive row. Consequently

\[
\boxed{K_{86}^*\le\frac{728141}{100000}=7.28141.}
\tag{5.2}
\]

Relative to the predecessor,

\[
\frac{728143}{100000}-\frac{728141}{100000}
=\boxed{\frac{2}{100000}=0.00002}.
\]

The retained lower obstruction does not move, so the current same-dimension certified interval is

\[
\boxed{
2.25925611947
\le K_{86}^*
\le7.28141.}
\tag{5.3}
\]

## 6. Complete fixed universal upper envelope after this run

Nothing is deleted from the predecessor metric. Define

\[
T_5=
\frac{2\sqrt2+3\sqrt3+2\sqrt{51+3\sqrt6}}{13}.
\tag{6.1}
\]

### 6.1 Oldest retained DTV row-pruning branch

\[
D_0(n)=\left\lceil\frac{10^6n^2}{7507^2}\right\rceil,
\qquad
p_D=\frac{2e^{-1/(18D)}}{81\sqrt{2\pi}D^{3/2}},
\]

\[
\delta_D=2[1-(1-p_D)^D],
\qquad
G_0(n)=\max\left\{\frac{7507}{1000},
3\sqrt{2\pi}(1-\delta_{D_0(n)})\right\}.
\tag{6.2}
\]

### 6.2 One-threshold branch

\[
D_*(n)=\left\lceil\frac{400000000n^2}{22114366681}\right\rceil-1,
\]

\[
\alpha_D=\frac{2-1/D}{3\sqrt{2\pi}\sqrt D},
\qquad
\beta_D=\frac{\alpha_D}{2(1+\alpha_D)},
\]

\[
H(n)=\max\left\{\frac{148709}{20000},
3\sqrt{2\pi}(1-\beta_{D_*(n)})\right\}.
\tag{6.3}
\]

### 6.3 Three-threshold upper-tail branch

With `c_{ell,D}^{(3)}` the exact coefficients of the certified three-threshold occupancy polynomial in the immutable predecessor chain,

\[
\beta_D^{\uparrow,3}
=\frac12\sum_{\ell=1}^Dc_{\ell,D}^{(3)}
\left[
\frac1{7\ell/5-1}-\frac1{7\ell/5-1/2}
\right],
\]

\[
D_9(n)=\left\lceil\frac{10^{10}n^2}{547864952041}\right\rceil-1,
\]

\[
J(n)=\max\left\{\frac{740179}{100000},
\frac{27\sqrt{10\pi}}{20}(1-\beta_{D_9(n)}^{\uparrow,3})\right\}.
\tag{6.4}
\]

### 6.4 Lower-tail infimum branches

For every integer `D>=135`,

\[
C_D^-=
\frac{27\sqrt{10\pi}}{20}
(1-\beta_D^{\uparrow,3}-\beta_D^{\downarrow,-}),
\qquad
L_-(n)=
\inf_{D\in\mathbb Z,\,D\ge135}
\max\left\{C_D^-,\frac n{\sqrt{D+1}}\right\},
\tag{6.5}
\]

and for `r=2,3,4`,

\[
C_D^{(r)}=
\frac{27\sqrt{10\pi}}{20}
(1-\beta_D^{\uparrow,3}-\beta_D^{\downarrow,r}),
\qquad
L_r(n)=
\inf_{D\in\mathbb Z,\,D\ge135}
\max\left\{C_D^{(r)},\frac n{\sqrt{D+1}}\right\}.
\tag{6.6}
\]

Each `beta_D^{downarrow,*}` is exactly the certified conditional lower-tail functional from its introducing immutable report, including the failed-threshold `0` convention. No parameter, threshold, support restriction, or zero convention is altered here.

### 6.5 Five-threshold occupancy/Cantelli branch

For integers `D>=135` and `k=1,...,5`,

\[
A_{k,D}=
\frac{5}{7(4437/5000)}
\left(1-\frac{2k}{5D}\right)
\left(\frac{2k}{5}\right)^{7/5}D^{-2/5},
\qquad a_k=A_{k,D}/D,
\]

with `a_0=0`, `d_k=a_k-a_{k-1}`, and

\[
F_{1,0}=1,
\qquad
F_{k,r}=\sum_{s=0}^rF_{k-1,r-s}\frac{d_k^s}{s!}
\quad(k=2,\ldots,5;\ 0\le r\le k-1).
\]

Define

\[
C_{D,5}(x)=
\sum_{r=0}^4\frac{D!}{(D-r)!}F_{5,r}x^r(1-a_5x)^{D-r},
\]

\[
1-C_{D,5}(x)=\sum_{\ell=1}^Dc_{\ell,D}^{(5)}x^\ell,
\]

\[
\beta_{D,5}^{\uparrow}
=\frac12\sum_{\ell=1}^Dc_{\ell,D}^{(5)}
\left[
\frac1{7\ell/5-1}-\frac1{7\ell/5-1/2}
\right].
\tag{6.7}
\]

Let `beta_{D,5}^{downarrow}` be the exact truncated-`U=157/20`, four-shell, two-moment Cantelli functional from `runs/R13/20260918T2334Z_cantelli-cascade-c4a7.md`, with zero contribution whenever its certified residual threshold fails to exceed the certified conditional-mean upper bound. Then

\[
C_D^{(5)}=
\frac{27\sqrt{10\pi}}{20}
(1-\beta_{D,5}^{\uparrow}-\beta_{D,5}^{\downarrow}),
\]

\[
L_5(n)=
\inf_{D\in\mathbb Z,\,D\ge135}
\max\left\{C_D^{(5)},\frac n{\sqrt{D+1}}\right\}.
\tag{6.8}
\]

### 6.6 Continuous-Laplace and new localized-transform branches

The retained continuous branch is

\[
L_{\rm LT}(n)=
\max\left\{\frac{739097}{100000},\frac n{\sqrt{136}}\right\}.
\tag{6.9}
\]

The old `p=33/20` anchor is replaced pointwise by the strictly stronger branch

\[
\boxed{
L_{33/20}^{\rm loc}(n)=
\max\left\{\frac{728141}{100000},\frac n{\sqrt{140}}\right\}.}
\tag{6.10}
\]

Thus the complete rigorously certified universal bound after this run is

\[
\boxed{
B_{R13}(n)=
\begin{cases}
1,&n=1,\\[1mm]
\sqrt2,&n=2,\\[1mm]
(\sqrt{11}+\sqrt2)/3,&n=3,\\[1mm]
\sqrt3,&n=4,\\[1mm]
\min\{\sqrt{3n/4},T_5\sqrt{\lceil n/5\rceil},G_0(n),L_-(n),L_2(n),L_3(n),L_4(n),L_5(n),L_{\rm LT}(n),L_{33/20}^{\rm loc}(n)\},&5\le n\le85,\\[2mm]
\min\{G_0(n),H(n),J(n),L_-(n),L_2(n),L_3(n),L_4(n),L_5(n),L_{\rm LT}(n),L_{33/20}^{\rm loc}(n)\},&n\ge86.
\end{cases}}
\tag{6.11}
\]

All integer restrictions, ceilings, occupancy coefficients, conditional-threshold conventions, and predecessor finite lower-tail definitions are retained exactly. In particular this report does not silently replace the complete metric by the `n=86` headline.

## 7. Exact checker, execution, and prior-art scope

The exact checker is

`artifacts/R13/20260919T1233Z_localized-cstar-7d3a_checker.py`

creation commit

`d568ddc907c28c1ec6bc5d4284c1d581b54bc852`.

It was read back at that exact commit. The executed output is

`artifacts/R13/20260919T1233Z_localized-cstar-7d3a.out`

creation commit

`dc592ba0d0bc3ad17ae2812aa0beef312f52812c`,

also read back at creation. Its acceptance line is

```text
R13_LOCALIZED_CSTAR_INCREMENT_EXACT_PASS
```

and it records `C_upper=7.2814055371169255...`, `new_h=7.28141`, and `139<86^2/h^2<140`. The checker uses exact `Fraction` arithmetic for every acceptance test; decimals are diagnostics only.

A bounded prior-art search on 2026-09-19 used the queries `"cosine-power" inverse-gamma Komlos discrepancy directional total variation`, `"33/20" Komlos discrepancy inverse gamma`, and `Gautschi inverse gamma directional total variation vector balancing`. It did not locate the specific finite-`D` coefficient-localization argument above. That is negative bounded search evidence only; it is **not** a priority proof. The general directional-TV theorem is Guo--Fang--Lu's, the gamma-ratio inequality is classical, and the inverse-gamma/Frobenius mechanism is not claimed as folklore-free solely because the exact decimal was not found.

Novelty status therefore remains **UNVERIFIED**. Outside audits of this new sharpening remain `0/2`; this is a self-check, not closure.

## 8. What the three methods taught us

- **#8 DISCRETIZE:** successful. A short exact transform interval can be added on top of the old global certificate without rebuilding it, and this moved `B_R13(86)` by `2e-5`.
- **#12 CONSERVED QUANTITY:** successful structurally. `E[(p-1)/S_p]=1` for every `p>1`, so the finite-dimensional improvement lives in the fractional transform term rather than the mean.
- **#27 SWAP QUANTIFIERS:** failed as an improvement but closed cleanly. Even if the density exponent is chosen after learning the active-row count, convex-order monotonicity makes `k=139` the worst case among `k<=139` within the homogeneous cosine-power family.

The next run should **not** spend its research budget on another decimal tightening of `c_*`. The higher-value routes are now: a genuinely nonproduct or non-homogeneous DTV density that escapes the convex-order barrier above; a source-matching explicit constant extraction from the Akbas--Sra Boolean small-ball chain; or an upper theorem for small column count strong enough to improve the block compiler. If the fixed metric stops moving for three consecutive runs, the prescribed Section-I stuck protocol applies.

## 9. Model / scheduler-control truthfulness

The scheduler-control surface exposed here still provides task title/prompt, schedule or relative start, timing mode, enablement, and task identity/update controls, but **no binding model-family selector, no reasoning-effort selector, no guaranteed-duration field, and no authenticated completed-run model/effort telemetry**. Therefore `GPT-6 / maximum` remains prompt text only on this surface. This run actually identifies as GPT-5.6 Sol; reasoning effort is UNVERIFIED.

Making GPT-6/maximum enforceable would require an owner-authorized product/workspace/admin/API scheduling surface that persists explicit model-family and reasoning-effort fields into execution routing and returns authenticated applied-model/applied-effort telemetry. Repository policy also records that a historical P26 update returned `You cannot modify this task` in one authorization context and later succeeded from another authorized context. The lawful workaround is the owning/authorized task surface or platform/workspace support, not duplication, identity substitution, or permission bypass.

No scheduler, permission, workflow, email, Drive, purchase, public-posting, or shared-root mutation was attempted in this run.

## 10. Structured ledger delta

```yaml
ledger_delta:
  worker: R13
  lane: HARD_OUTSIDE
  canonical_intake_alias: I0091
  source_target: real Boolean Komlos signing
  source_qualitative_status: KNOWN_IN_2026_PREPRINT_LITERATURE
  quantitative_track_status: PARTIAL
  metric:
    name: B_R13_complete_universal_upper_envelope
    before_at_n86: "728143/100000 = 7.28143"
    after_at_n86: "728141/100000 = 7.28141"
    exact_movement: "2/100000"
    movement: true
  same_dimension_lower_obstruction:
    before: "225925611947/10^11 = 2.25925611947"
    after: "225925611947/10^11 = 2.25925611947"
    movement: false
  methods: [8, 12, 27]
  previous_methods: [9, 2, 4]
  fixed_upper_unchanged_count_before: 1
  fixed_upper_unchanged_count_after: 0
  source_status: KNOWN
  result_status: PARTIAL
  proof_status: full_written_argument_for_new_sharpening
  exact_self_check: PASS
  outside_audits_new_sharpening: "0/2"
  novelty: UNVERIFIED
  checker:
    path: artifacts/R13/20260919T1233Z_localized-cstar-7d3a_checker.py
    creation_commit: d568ddc907c28c1ec6bc5d4284c1d581b54bc852
  output:
    path: artifacts/R13/20260919T1233Z_localized-cstar-7d3a.out
    creation_commit: dc592ba0d0bc3ad17ae2812aa0beef312f52812c
    result: R13_LOCALIZED_CSTAR_INCREMENT_EXACT_PASS
  shared_root_edits: false
  peer_file_edits: false
  scheduler_changes: false
  remaining_obligation: "Find a qualitatively different finite-dimensional upper mechanism; do not spend the next research run merely tightening the same c_* decimal."
```
