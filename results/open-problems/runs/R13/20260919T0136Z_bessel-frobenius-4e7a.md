Model actually run: **GPT-5.6 Sol**; reasoning level **UNVERIFIED** — not authenticated GPT-6 maximum. **FIXED METRIC MOVED:** `B_R13(86): 739097/100000 = 7.39097 -> 72991/10000 = 7.29910`, exact decrease `9187/100000 = 0.09187`. Methods actually used: **#3 PROVE SOMETHING STRONGER, #17 LOOK FOR YOUR NUMBERS SOMEWHERE ELSE, #20 FIND WHY THE ALGORITHM FAILS.**

Run ID: `20260919T0136Z_bessel-frobenius-4e7a`  
Repository/branch: `yspennstate/math-open-problems` / `master`.

## 1. Continuity, source status, and fixed metric

R13 remains the exclusive HARD OUTSIDE owner of Boolean Komlós / intake `E0042`. Before doing new mathematics I reread/reconciled the current campaign `INDEX.md` and `RANKING.md`, root `POSTED.md`, root `RESULTS.md`, root `QUEUE.md`, `operations/NEW_METHODS_2026-09-16.md`, the E0042 intake record in `probability_1000_intake_E_20260908/batches/b05_bandeira.json`, the newest complete R13 report `runs/R13/20260919T0045Z_laplace-tail-31d8.md`, and current neighboring discrepancy evidence. No shared root or peer file was edited.

The source-status correction remains in force. The qualitative Komlós conjecture is **KNOWN in the current 2026 preprint literature**: Guo--Fang--Lu, *Vector Balancing via Directional Total Variation*, arXiv:2609.11189v1, submitted 10 September 2026, prove the genuine real-Boolean bound `3 sqrt(2 pi)`; Karingula--Lovett, ECCC TR26-188, 17 September 2026, give an independent elementary proof with constant `36`; Akbas--Sra, *Boolean Small-Ball Inequalities for Discrepancy Theory*, arXiv:2609.20785, submitted 17 September 2026, recover Komlós among their corollaries. Bansal--Jiang arXiv:2508.03961v2 remains the earlier polylogarithmic real-Boolean comparison source. R13 therefore makes **no claim to solve the qualitative conjecture**; its owner-defined metric is the complete finite-dimensional real-Boolean upper envelope.

For

\[
K_n^*:=\sup_{m\ge1}\ \sup_{\substack{A\in\mathbb R^{m\times n}\\
\|A_{\cdot j}\|_2\le1}}
\min_{\varepsilon\in\{\pm1\}^n}\|A\varepsilon\|_\infty,
\]

this run proves

\[
\boxed{K_{86}^*\le \frac{72991}{10000}=7.2991}.
\tag{1.1}
\]

The predecessor's certified value was

\[
K_{86}^*\le \frac{739097}{100000}=7.39097,
\]

so the fixed metric moves by the exact amount

\[
\frac{739097}{100000}-\frac{72991}{10000}
=\boxed{\frac{9187}{100000}}=0.09187.
\tag{1.2}
\]

The fixed-metric stagnation count is reset to `0`.

## 2. Retained finite-dimensional DTV reduction

This run keeps the previously proved `p=9/5` cosine-power density, but replaces the scalar Laplace estimate by a stronger one.

For `D>=1`, on the cube `(-C,C)^D` take the product density

\[
\rho_{C,p}(x)\propto\prod_{i=1}^D
\cos^p\!\left(\frac{\pi x_i}{2C}\right),
\qquad p=\frac95.
\tag{2.1}
\]

If

\[
T_i=\tan\!\left(\frac{\pi X_i}{2C}\right),
\]

then the change of variables gives

\[
T_i\stackrel d=\frac{G_i}{\sqrt{S_i}},
\qquad G_i\sim N(0,1),\quad S_i\sim\chi^2_{p+1},
\tag{2.2}
\]

independently. Since

\[
\partial_i\log\rho_{C,p}(x)
=-\frac{p\pi}{2C}
\tan\!\left(\frac{\pi x_i}{2C}\right),
\]

conditioning on the `S_i` gives for every direction `u`

\[
V_u(\rho_{C,p})
=\frac{p\sqrt{\pi/2}}{C}
\mathbb E\sqrt{\sum_i\frac{u_i^2}{S_i}}.
\tag{2.3}
\]

Let

\[
Y_i:=\frac{p-1}{S_i}=\frac4{5S_i},
\qquad
X_D:=\frac1D\sum_{i=1}^D Y_i.
\tag{2.4}
\]

For `w_i=u_i^2/||u||_2^2`, the map

\[
w\longmapsto\mathbb E\sqrt{\sum_iw_iY_i}
\]

is symmetric and concave on the simplex, hence is maximized at the uniform weight. Therefore

\[
V_u(\rho_{C,9/5})
\le
\frac{9\sqrt{\pi/2}}{5C\sqrt{4/5}}
\mathbb E\sqrt{X_D}\,\|u\|_2.
\tag{2.5}
\]

The Guo--Fang--Lu finite-step directional-TV theorem applies when this coefficient is at most `1/3`. Thus every finite family of real vectors in `R^D` of Euclidean norm at most one admits **Boolean** signs with coordinate discrepancy strictly below

\[
\boxed{
C_D=\frac{27\sqrt{10\pi}}{20}\,\mathbb E\sqrt{X_D}.}
\tag{2.6}
\]

No complex phase, vector coloring, or average-case relaxation is used.

For `p=9/5`, `Y` is inverse-gamma with

\[
a=\frac75,\qquad \beta=\frac25,
\]

so

\[
f_Y(y)=\frac{\beta^a}{\Gamma(a)}y^{-a-1}e^{-\beta/y},
\qquad y>0,
\qquad \mathbb EY=1.
\tag{2.7}
\]

## 3. Methods #17 and #20 — the missing coefficient in the natural Laplace algorithm

The predecessor bounded the inverse-gamma Laplace transform by returning to an integral representation, throwing away `z<1`, and crudely lower-bounding the remaining exponential factor. That route certified only the nonanalytic coefficient

\[
\frac{39}{125}\frac{25}{14}
=\frac{39}{70}=0.557142857\ldots
\]

in front of the leading `s^{7/5}` term. The exact special-function expansion shows that this was the main quantitative loss.

Write

\[
L(s):=\mathbb E e^{-sY}.
\]

The inverse-gamma transform is

\[
L(s)=
\frac{2(\beta s)^{a/2}}{\Gamma(a)}
K_a(2\sqrt{\beta s}).
\tag{3.1}
\]

Using the standard relation between `K_a` and `I_{\pm a}`, together with the power series for `I`, gives the exact Frobenius decomposition for nonintegral `a`:

\[
L(s)=
{}_0F_1(;1-a;\beta s)
+
\frac{\Gamma(-a)}{\Gamma(a)}(\beta s)^a
{}_0F_1(;1+a;\beta s).
\tag{3.2}
\]

At `a=7/5`, `beta=2/5`,

\[
L(s)=
{}_0F_1\!\left(; -\frac25;\frac{2s}{5}\right)
+c_*s^{7/5}
{}_0F_1\!\left(;\frac{12}{5};\frac{2s}{5}\right),
\tag{3.3}
\]

where

\[
c_*=
\frac{25}{14}
\frac{\Gamma(3/5)}{\Gamma(2/5)}
\left(\frac25\right)^{2/5}.
\tag{3.4}
\]

The second hypergeometric factor has positive coefficients and is at least one. For the coefficient itself, set

\[
P_N:=\prod_{k=0}^{N-1}\frac{5k+2}{5k+3},
\qquad N=1000.
\]

Gautschi's gamma-ratio inequality at `x=N-2/5`, `s=4/5` gives

\[
\frac{\Gamma(3/5)}{\Gamma(2/5)}
>P_N\left(N-\frac25\right)^{1/5}.
\]

The checker verifies the resulting fifth-power comparison exactly and obtains

\[
\boxed{c_*>\frac{8309}{10000}=0.8309.}
\tag{3.5}
\]

Thus the predecessor was discarding roughly one third of the leading nonanalytic coefficient. This is the precise failure of that natural Laplace lower-bound algorithm.

## 4. Method #3 — a stronger uniform Laplace lower bound

The analytic Frobenius branch has the beginning

\[
{}_0F_1\!\left(; -\frac25;\frac{2s}{5}\right)
=1-s-\frac{s^2}{3}-\frac{s^3}{36}-\cdots.
\tag{4.1}
\]

All nonconstant coefficients are negative. From the `s^3` term onward, the absolute ratio of consecutive terms is at most `s/26`. We take

\[
D=138,
\qquad
T=\left(\frac54\right)^{10}<10,
\qquad
0\le s=\frac tD\le\frac TD<\frac1{10},
\]

and define

\[
k_3:=
\frac{1}{36\left(1-T/(26D)\right)}.
\tag{4.2}
\]

Then (3.3)--(3.5) imply, uniformly on this interval,

\[
L(s)\ge
1-s+\frac{8309}{10000}s^{7/5}
-\frac{s^2}{3}-k_3s^3.
\tag{4.3}
\]

The exact fifth-power checker also proves

\[
\boxed{D^{-2/5}>\underline d:=\frac{139331196}{10^9}.}
\tag{4.4}
\]

Put

\[
\bar q(t)=
\frac{8309}{10000}\,\underline d\,t^{7/5}
-\frac{t^2}{3D}
-\frac{k_3t^3}{D^2},
\tag{4.5}
\]

and

\[
\bar y(t)=
\frac tD
-\frac{8309}{10000}\frac{\underline d}{D}t^{7/5}
+\frac{t^2}{3D^2}
+\frac{k_3t^3}{D^3}.
\tag{4.6}
\]

Thus `L(t/D)>=1-\bar y(t)`. The crude inequality in the checker shows `0<=\bar y(t)<1`; then

\[
\log(1-y)\ge-y-\frac{y^2}{2(1-y)}
\qquad(0\le y<1)
\]

and `t<=T` give

\[
D\log L(t/D)+t\ge R(t),
\tag{4.7}
\]

where

\[
\boxed{
R(t):=
\bar q(t)-
\frac{D^2}{2(D-T)}\bar y(t)^2.}
\tag{4.8}
\]

After the substitution `t=u^{10}`, `R(u^{10})` is an ordinary polynomial over the rationals. Its leading degree is `14`. To prove positivity on `0<=u<=5/4`, divide by `u^{14}`, discard every positive non-leading monomial, and place every negative monomial at the endpoint `u=5/4`. The exact residual margin is

\[
0.08982021081601134\ldots>0.
\tag{4.9}
\]

so

\[
R(t)\ge0\qquad(0\le t\le T).
\tag{4.10}
\]

This is a **uniform** transform inequality, stronger than merely estimating one tail event or one Jensen moment.

## 5. Exact polynomial lower bound for the Jensen defect

For every positive random variable with mean one,

\[
1-\mathbb E\sqrt X
=\frac1{2\sqrt\pi}
\int_0^\infty
\bigl(\mathbb E e^{-tX}-e^{-t}\bigr)t^{-3/2}\,dt.
\tag{5.1}
\]

Since the `Y_i` are independent,

\[
\mathbb E e^{-tX_D}=L(t/D)^D.
\]

On `[0,T]`, (4.7)--(4.10) imply

\[
L(t/D)^D-e^{-t}
\ge e^{-t}(e^{R(t)}-1).
\]

Use

\[
e^{R}-1\ge R+\frac{R^2}{2}
\]

and, with `M=500`,

\[
e^{-t}\ge\left(1-\frac t{500}\right)^{500}
\qquad(0\le t\le T<500).
\]

Therefore

\[
1-\mathbb E\sqrt{X_{138}}
\ge\frac{I}{2\sqrt\pi},
\tag{5.2}
\]

where

\[
I:=\int_0^T
\left(1-\frac t{500}\right)^{500}
\left(R(t)+\frac{R(t)^2}{2}\right)t^{-3/2}\,dt.
\tag{5.3}
\]

Now set `t=u^{10}`. All fractional powers disappear and

\[
t^{-3/2}dt=10u^{-6}du,
\qquad 0\le u\le\frac54.
\]

Thus (5.3) is an **exact rational polynomial integral**. The executed `Fraction` checker gives

\[
I=0.12542867374311936\ldots.
\tag{5.4}
\]

Using the exact rational certificates

\[
\pi<\frac{355}{113},
\qquad
\sqrt\pi<\frac{1773}{1000},
\]

we get

\[
\boxed{
1-\mathbb E\sqrt{X_{138}}
>0.035371876408099086\ldots.}
\tag{5.5}
\]

Finally,

\[
\sqrt{10\pi}<\frac{1121}{200}
\]

and (2.6) yield

\[
C_{138}
<7.299099854189016\ldots
<\boxed{\frac{72991}{10000}=7.2991}.
\tag{5.6}
\]

Every acceptance inequality behind (3.5), (4.4), (4.9), (5.4)--(5.6) is checked with exact rational arithmetic; the displayed decimals are only renderings.

## 6. Row pruning: the `n=86` theorem

Let `A` be any real `m x 86` matrix whose columns have Euclidean norm at most one, and set

\[
h:=\frac{72991}{10000}.
\]

Call a row `r_i` active when

\[
\|r_i\|_2>\frac h{\sqrt{86}}.
\]

The Frobenius budget gives

\[
\sum_i\|r_i\|_2^2\le86.
\]

Hence, if `d` rows are active,

\[
d<\frac{86^2}{h^2}.
\]

The checker proves exactly

\[
138<\frac{86^2}{h^2}
=138.8219930295101\ldots<139,
\tag{6.1}
\]

so `d<=138`. Zero-pad the active-row submatrix to ambient dimension `138` and apply (5.6). Every inactive row obeys, for every Boolean sign vector,

\[
|r_i\cdot\varepsilon|
\le\|r_i\|_2\sqrt{86}\le h.
\]

Therefore

\[
\boxed{K_{86}^*\le7.2991},
\]

which proves (1.1).

## 7. Complete fixed metric after this run

No older certified branch is discarded or weakened. Let `B_prev(n)` denote **exactly** the complete predecessor envelope defined in `runs/R13/20260919T0045Z_laplace-tail-31d8.md` at its immutable creation commit `4f4da156c8a65951e875c5043b4baef0475e62b4`. In particular that function retains, with their exact definitions and domain restrictions, the branches

- the exact `n=1,2,3,4` values;
- `sqrt(3n/4)`;
- the five-column block branch `T_5 sqrt(ceil(n/5))`, with
  \[
  T_5=\frac{2\sqrt2+3\sqrt3+2\sqrt{51+3\sqrt6}}{13};
  \]
- `G_0`, `H`, `J`;
- the lower-tail branches `L_-`, `L_2`, `L_3`, `L_4`, `L_5`;
- the predecessor Laplace branch
  \[
  L_{\rm LT}(n)=\max\left\{\frac{739097}{100000},\frac n{\sqrt{136}}\right\}.
  \]

Equivalently, its top-level piecewise form is

\[
B_{\rm prev}(n)=
\begin{cases}
1,&n=1,\\
\sqrt2,&n=2,\\
(\sqrt{11}+\sqrt2)/3,&n=3,\\
\sqrt3,&n=4,\\
\min\{\sqrt{3n/4},T_5\sqrt{\lceil n/5\rceil},G_0,L_-,L_2,L_3,L_4,L_5,L_{\rm LT}\}(n),&5\le n\le85,\\
\min\{G_0,H,J,L_-,L_2,L_3,L_4,L_5,L_{\rm LT}\}(n),&n\ge86.
\end{cases}
\tag{7.1}
\]

The immutable predecessor is the controlling exact definition of every inherited symbol in (7.1); this run does not silently alter any of their constants, logarithms, ceilings, infima, or integer-dimension restrictions.

The new source-matching branch is valid for **every positive integer `n`**:

\[
\boxed{
L_{\rm BF}(n):=
\max\left\{
\frac{72991}{10000},
\frac n{\sqrt{139}}
\right\}.}
\tag{7.2}
\]

Indeed, if the row threshold is `h_n=L_BF(n)/sqrt(n)`, then

\[
d<\frac{n^2}{L_{\rm BF}(n)^2}\le139,
\]

so the integer active-row count is at most `138`; (5.6) handles the active rows and Cauchy--Schwarz handles the rest.

Thus the **complete current rigorously certified universal envelope** is

\[
\boxed{
B_{R13}(n)=\min\{B_{\rm prev}(n),L_{\rm BF}(n)\},
\qquad n\in\mathbb N.}
\tag{7.3}
\]

This is a pointwise real-Boolean bound. I do not claim `L_BF` dominates every predecessor branch in every dimension. The certified movement recorded this run is the exact `n=86` improvement (1.2).

The retained finite lower-obstruction history is unchanged:

\[
K_5^*=T_5=1.792447191483\ldots,
\qquad K_6^*\ge1.84535465,
\]
\[
K_{11}^*\ge1.99488049,
\qquad K_{12}^*\ge2.013108.
\tag{7.4}
\]

## 8. Prior-art/current-source search and novelty status

Current primary-source checks in this run covered the exact/current titles and identifiers for Guo--Fang--Lu (`2609.11189`), Akbas--Sra (`2609.20785`), and Karingula--Lovett (`ECCC TR26-188`), plus a bounded search combining `Komlos`, `directional total variation`, `inverse gamma`, `Bessel`, and `finite dimensional`. The searches recovered the current qualitative Komlós resolutions and neighboring Boolean-small-ball work, but did not locate a source matching the finite-dimensional Bessel/Frobenius sharpening in Sections 3--7.

That is bounded negative evidence, not a worldwide priority proof. **Novelty remains UNVERIFIED.** The exact special-function identity itself is classical; the claim here is only the new way it is combined with the directional-TV signing density and row pruning to sharpen the finite-dimensional constant.

## 9. What the three methods did

**#3 PROVE SOMETHING STRONGER.** Instead of another tail event or a scalar retuning, I proved the uniform transform lower bound (4.7) on an entire interval and integrated it. **Outcome: success; fixed metric moved.**

**#17 LOOK FOR YOUR NUMBERS SOMEWHERE ELSE.** The inverse-gamma law's transform is a modified-Bessel `K` function whose nonintegral Frobenius expansion exposes the true leading fractional-power coefficient. **Outcome: success; the certified coefficient rose from the predecessor's effective `39/70≈0.55714` to `>0.8309`.**

**#20 FIND WHY THE ALGORITHM FAILS.** The predecessor's natural integral proof discarded `z<1` and thereby lost a large part of precisely that `s^{7/5}` coefficient. **Outcome: exact obstruction identified and removed.**

All thirty Section-B labels had already appeared in R13 history, so `[3,17,20]` is a nonrepeating triple with materially new instantiations, not a false claim that these label numbers had never been named before.

## 10. Exact checker, execution, and audit status

The exact-arithmetic self-check is

`artifacts/R13/20260919T0136Z_bessel-frobenius-4e7a_checker.py`

created at commit

`464ae82b1391346f52a645ce607e6dc40e19286f`

and read back at that exact commit.

Its executed output is archived as

`artifacts/R13/20260919T0136Z_bessel-frobenius-4e7a_checker.out`

created at commit

`a756ba580f5ceb796f491087acd0af7250989725`

and read back at that exact commit. It terminates

`R13_BESSEL_FROBENIUS_EXACT_PASS`.

This is a **self-check**, not an independent audit. The new sharpening has `0/2` required OTHER-track audits. Older R12/P26 audits of the Guo--Fang--Lu baseline do not audit this new Frobenius/Gautschi/Laplace calculation.

Status after this run:

`SOURCE QUALITATIVE STATUS KNOWN / R13 QUANTITATIVE STATUS PARTIAL / FIXED METRIC MOVED / FULL WRITTEN PROOF / EXACT SELF-CHECK PASS / OUTSIDE AUDITS 0/2 / NOVELTY UNVERIFIED / STAGNATION 0`.

## 11. Next route

The best next mathematical target is not a decimal retuning of `T`, `M`, or the rational coefficient. The exact Bessel representation shows that, at `D=138`, this product-density family has substantial residual information beyond the two-term lower exponential certificate. A genuinely new next route should be one of:

1. use a rigorous rational enclosure of the full Bessel/Frobenius transform on a partition of the Laplace interval, rather than a single global polynomial minorant;
2. couple the exact `K_5^*=T_5` block theorem into the DTV active-row reduction;
3. return to the exact `n=6` intersection-aware cover dual, but only if it can move a source-matching finite obstruction or upper constant rather than add another auxiliary lemma.

## 12. Model/scheduler-control truth

The model-control limitation is still unresolved. The exposed task-control surface provides title, prompt, schedule, enablement and timing-mode controls, but no binding model-family selector, no reasoning-effort selector, and no authenticated completed-run effort telemetry. Thus `GPT-6 / maximum` remains prompt text only here; this run cannot truthfully attest that it ran.

Changing that requires an authorized product/backend or workspace surface that actually exposes model/reasoning selectors and authenticated run telemetry. The historical P26 `You cannot modify this task` failure was context/authorization-dependent; repository history records a later successful P26 update from an authorized P/C context. The legitimate workaround is therefore the owning/authorized task surface or platform support, not duplication or permission bypass. No scheduler, permission, workflow, email, Drive, purchase, or public-posting action was made in this run.

## 13. Structured ledger_delta

```yaml
ledger_delta:
  worker: R13
  lane: HARD_OUTSIDE
  source_id: E0042
  source_target: Boolean Komlos real signs
  source_qualitative_status: KNOWN_IN_2026_PREPRINT_LITERATURE
  metric:
    name: complete_rigorously_certified_real_boolean_upper_envelope_B_R13_n
    tracked_anchor: n=86
    before: 739097/100000
    after: 72991/10000
    exact_improvement: 9187/100000
    moved: true
  new_branch:
    name: L_BF
    formula: max(72991/10000, n/sqrt(139))
    domain: positive integers n
    ambient_D_certificate: 138
  methods_this_run: [3, 17, 20]
  predecessor_report: runs/R13/20260919T0045Z_laplace-tail-31d8.md
  predecessor_creation_commit: 4f4da156c8a65951e875c5043b4baef0475e62b4
  checker:
    path: artifacts/R13/20260919T0136Z_bessel-frobenius-4e7a_checker.py
    creation_commit: 464ae82b1391346f52a645ce607e6dc40e19286f
    status: SELF_CHECK_PASS
  output:
    path: artifacts/R13/20260919T0136Z_bessel-frobenius-4e7a_checker.out
    creation_commit: a756ba580f5ceb796f491087acd0af7250989725
  outside_audits_new_claim: 0/2
  novelty: UNVERIFIED
  stagnation_count: 0
  report_path: runs/R13/20260919T0136Z_bessel-frobenius-4e7a.md
  shared_root_edits: 0
  peer_file_edits: 0
  next_primary_route: rigorous_piecewise_full_Bessel_transform_or_K5_DTV_hybrid
```
