Model actually run: **GPT-5.6 Sol**; reasoning level **UNVERIFIED** — this was not authenticated GPT-6 maximum. **FIXED METRIC MOVED:** `B_R13(86): 73979/10000 = 7.3979 -> 739733/100000 = 7.39733`, an exact certified decrease of `57/100000 = 0.00057`. Methods actually used: **#2 ATTACK THE NEGATION FIRST, #21 ASK WHO ELSE HAS THIS SHAPE, #25 COUNT THE SAME THING TWICE.**

# R13 — Boolean Komlós: a two-band lower-tail DTV certificate

Run ID: `20260918T2203Z_twoband-middle-7d2c`  
Repository / branch: private `yspennstate/math-open-problems` / `master`  
Track: **R13 HARD OUTSIDE**  
Source ID: **E0042**

## 1. Continuity, ownership, and source scope

The source target remains the real Boolean Komlós problem. For a real `m x n` matrix `A` whose columns have Euclidean norm at most one, write

\[
\operatorname{disc}(A)=\min_{\varepsilon\in\{-1,+1\}^n}\|A\varepsilon\|_\infty,
\qquad
K_n^*=\sup_A\operatorname{disc}(A).
\]

R13's frozen metric is the **complete rigorously certified pointwise upper envelope** `B_R13(n)`. Complex phases, rank-two/vector colorings, and average-case estimates do not count as the Boolean target.

I continued from the newest complete R13 report

`runs/R13/20260918T2033Z_trunc-second-moment-9b6e.md`.

Its moving anchor was

\[
K_{86}^*\le \frac{73979}{10000}=7.3979.
\]

Before new research I reread/reconciled the required current repository surfaces: `probability_campaign_2026_09/INDEX.md`, `RANKING.md`, root `POSTED.md`, root `RESULTS.md`, root `QUEUE.md`, `operations/NEW_METHODS_2026-09-16.md`, the E0042 intake record in `probability_1000_intake_E_20260908/batches/b05_bandeira.json`, the newest R13 report/checker, and current neighboring R02/R12/R16 state. R13 remains the exclusive Boolean-Komlós owner; no queue/claim delta authorizes rotation away from it.

The old E0042 intake status paragraph is now historically stale: it predates the September 2026 papers. The source statement itself is unchanged and remains the object whose finite quantitative constants R13 is sharpening.

All thirty Section-B labels have already appeared somewhere in the long R13 history. Therefore a literally never-used label no longer exists. I obey the nonrepetition requirement by using a different triple from the immediately preceding `#11,#18,#30`, with materially new instantiations rather than pretending a label was unused.

## 2. Fresh primary-source and later-literature check

The current source picture checked this run is:

1. **Bansal--Jiang**, arXiv:`2508.03961v2`, last revised 9 September 2025, remains the earlier full real-Boolean advance with a `\widetilde O((\log n)^{1/4})` Komlós bound.
2. **Guo--Fang--Lu**, arXiv:`2609.11189v1`, submitted 10 September 2026, states the unrestricted deterministic real-Boolean bound
   \[
   \left\|\sum_j\varepsilon_jv_j\right\|_\infty<3\sqrt{2\pi}.
   \]
   R13's finite-dimensional DTV branches are sharpenings of the density calculation inside that Boolean theorem, not a complex/vector relaxation.
3. **Akbas--Sra**, arXiv:`2609.20785v1`, submitted 17 September 2026, proves Boolean small-ball inequalities and recovers Komlós among its corollaries. Its current abstract/source-level formulation uses universal constants rather than an explicit finite-dimensional numerical constant that improves the R13 envelope below, so it does not by itself move `B_R13(n)` here.
4. **Guillen--Kobzar**, arXiv:`2609.15071v1`, remains complex unit-modulus discrepancy / rank-two vector discrepancy on real inputs; it is not Boolean signing.

Targeted searches for a finite-dimensional Komlós sharpening using the specific `p=9/5` cosine-power density together with an inverse-chi-square **two-band** Bernstein decomposition did not return a matching paper. This is bounded negative evidence only; **novelty remains UNVERIFIED**.

## 3. Method #2 — attack the negation first: direct six-column route

Before extending the DTV branch I tried the more valuable possible negation: perhaps the next finite-column theorem already forces a much better envelope.

The retained exact facts are

\[
K_5^*=T_5,
\qquad
T_5=
\frac{2\sqrt2+3\sqrt3+2\sqrt{51+3\sqrt6}}{13}
=1.79244719148\ldots,
\]

and

\[
K_6^*\ge\frac{36907093}{20000000}=1.84535465,
\qquad
K_6^*\le\frac3{\sqrt2}.
\]

A `K_6^*<1.91` theorem would propagate through the retained block-composition theorem and beat the present `n=86` DTV number. I therefore revisited the older proposed **intersection-aware cover** formulation on the 32 antipodal six-cube sign classes, rather than another scalar row-incidence estimate. The exact old six-column obstruction shows that the six-active-row regime is genuinely nontrivial, and the older report already proves that a purely rowwise bad-cardinality/energy charge cannot push the `3/sqrt(2)` theorem downward by itself.

This run did not produce an exact global cover dual for the six-row regime. I therefore make **no new `K_6^*` upper claim**, create no six-column checker, and do not replace a failed finite-cover search by a heuristic statement. This route remains the higher-payoff finite target for a later genuinely new attack.

## 4. Method #21 — ask who else has this shape

The immediately relevant new paper is Akbas--Sra's 17 September Boolean small-ball work. It uses the new Guo--Fang--Lu directional-variation theorem as an ingredient and turns existence into a Gibbs law on many good Boolean signings. This is exactly the neighboring shape that had to be checked before extending the DTV density calculation.

For the present fixed metric, however, the current source-level constants in that paper are universal rather than a directly extractable explicit finite-`D` number below the R13 certificate at `D=135`. Thus this literature route changes the conceptual neighborhood but does not supply the numerical movement below. I record it so later R13 runs do not treat the Boolean small-ball development as nonexistent.

## 5. Retained DTV setup

The successful route keeps the already-proved `p=9/5` cosine-power density. Let

\[
S_i\sim\chi^2_{14/5},
\qquad
Y_i=\frac4{5S_i},
\qquad
X_D=\frac1D\sum_{i=1}^D Y_i,
\qquad
a_D=\mathbb E\sqrt{X_D}.
\]

The retained directional-total-variation calculation gives a genuine Boolean signing cube with half-side

\[
C_D=rac{27\sqrt{10\pi}}{20}\,a_D.
\tag{5.1}
\]

Since `E X_D=1`,

\[
2(1-a_D)=\mathbb E(\sqrt{X_D}-1)^2.
\tag{5.2}
\]

The preceding R13 work supplies a rigorously proved upper-tail contribution `beta_D^up` from the disjoint event `X_D>=1`, and for `D=135` its exact checker gives

\[
\beta_{135}^{\uparrow}>0.021737695196183224\ldots .
\tag{5.3}
\]

The same preceding proof also established the following exact rational facts for

\[
U=\frac{157}{20},
\qquad
Z\stackrel d=Y\mid Y\le U:
\]

\[
\Pr(Y\le U)>p_0:=\frac{24683}{25000},
\tag{5.4}
\]

\[
\mathbb EZ<\mu:=\frac{662903}{987320},
\tag{5.5}
\]

and

\[
\operatorname{Var}(Z)<v_*:=
\frac{9691697959}{10^{10}}.
\tag{5.6}
\]

These are retained proved inequalities, not newly estimated decimals.

## 6. Method #25 — count the same lower-tail event twice

The preceding certificate demanded that **all** `Y_i` lie below `U`. That discards a substantial set of configurations in which one coordinate is moderately above `U` but the empirical average is still safely below one.

The new idea is to split the same lower-tail event into two **disjoint** pieces and certify both:

- `E_0`: every `Y_i<=U`;
- `E_1`: exactly one coordinate satisfies `U<Y_i<=V`, while all other coordinates satisfy `Y_j<=U`.

This is not another recheck of the old all-low event; it adds a new admissible band and a new combinatorial event class.

### 6.1 Exact positive probability for the middle band

Put

\[
s_0=\frac{16}{157},
\qquad
\rho=\frac{12}{11},
\qquad
V=U\rho^5
=\frac{9766656}{805255}
=12.1286499307\ldots .
\tag{6.1}
\]

For `S~chi^2_{14/5}`,

\[
\Pr(S\le z)=
\frac1{2^{7/5}\Gamma(7/5)}
\int_0^z s^{2/5}e^{-s/2}\,ds,
\tag{6.2}
\]

and `Y>y` is the event `S<4/(5y)`.

Use the exact rational root bounds

\[
\left(\frac{4011}{10000}\right)^5<s_0^2<
\left(\frac{1003}{2500}\right)^5,
\tag{6.3}
\]

\[
\left(\frac{2639}{1000}\right)^5<2^7<
\left(\frac{66}{25}\right)^5,
\tag{6.4}
\]

and the retained gamma bounds

\[
\frac{350840}{401787}<\Gamma(7/5)<\frac{88869}{100000}.
\tag{6.5}
\]

On `[0,s_0]`, `e^{-s/2}>=1-s_0/2`, hence

\[
\Pr(Y>U)>
L_U:=
\frac57
\frac{s_0(4011/10000)(1-s_0/2)}
{(66/25)(88869/100000)}.
\tag{6.6}
\]

For `V`, the corresponding chi-square cutoff is `s_0/rho^5`. Using `e^{-s/2}<=1` and the upper root/lower denominator bounds gives

\[
\Pr(Y>V)<
U_V:=
\frac57
\frac{s_0(1003/2500)}
{\rho^7(2639/1000)(350840/401787)}.
\tag{6.7}
\]

Therefore

\[
p_M:=\Pr(U<Y\le V)>L_U-U_V>0.
\tag{6.8}
\]

The exact checker evaluates the certified rational lower bound as

\[
L_U-U_V=0.00491818462206843\ldots .
\]

The decimal is only a rendering; the acceptance comparison is rational.

### 6.2 Bernstein certificate for the two disjoint cases

Take

\[
t=\frac{81}{100}=\left(\frac9{10}\right)^2.
\tag{6.9}
\]

For `N` low-band variables and any `x>mu`, Bernstein with (5.5)--(5.6) and the bound `0<=Z<=U` gives

\[
\Pr\!\left(\frac1N\sum_{j=1}^NZ_j\le x\right)
\ge1-e^{-E(N,x)},
\tag{6.10}
\]

where

\[
E(N,x)=
\frac{N(x-\mu)^2}
{2v_*+\frac23U(x-\mu)}.
\tag{6.11}
\]

To keep the certificate rational, define

\[
R_8(E)=1-
\left(\sum_{j=0}^8\frac{E^j}{j!}\right)^{-1}.
\tag{6.12}
\]

Since `exp(E)` is strictly larger than its eighth Taylor partial sum for `E>0`,

\[
1-e^{-E}>R_8(E).
\tag{6.13}
\]

For `D=135`, event `E_0` therefore has probability at least

\[
P_0=p_0^{135}R_8(E(135,t)).
\tag{6.14}
\]

For event `E_1`, the single middle-band variable contributes at most `V`. Thus it suffices that the remaining 134 low-band variables have average at most

\[
t_1=\frac{135t-V}{134}
=0.7255324632032293\ldots>\mu.
\tag{6.15}
\]

The `135` choices of the unique middle coordinate are disjoint, so

\[
P_1=
135\,(L_U-U_V)\,p_0^{134}
R_8(E(134,t_1))
\tag{6.16}
\]

is a rigorous lower bound for `Pr(E_1)`.

The exact checker gives

\[
P_0>0.11110966821452067\ldots,
\qquad
P_1>0.01944499249587635\ldots,
\tag{6.17}
\]

hence

\[
\Pr(X_{135}\le81/100)>P_0+P_1
>0.13055466071039704\ldots .
\tag{6.18}
\]

Because `(1-sqrt(x))^2>=1/100` on `x<=81/100`, equation (5.2) yields the new lower-tail Jensen contribution

\[
\boxed{
\beta_{135}^{\downarrow,3}
:=\frac{P_0+P_1}{200}
>0.0006527733035519851\ldots .}
\tag{6.19}
\]

The upper-tail event used in (5.3) lies in `X_D>=1`, so it is disjoint from the new lower-tail event `X_D<=0.81`. Their Jensen contributions therefore add without inclusion-exclusion loss.

## 7. The new `D=135` Boolean signing constant

Combining (5.1), (5.3), and (6.19), and using the exact rational bound

\[
\sqrt{10\pi}<\frac{1121}{200},
\tag{7.1}
\]

gives

\[
C_{135}
<
\frac{27}{20}\frac{1121}{200}
\left(1-\beta_{135}^{\uparrow}-\beta_{135}^{\downarrow,3}\right)
<7.397326922479628\ldots .
\tag{7.2}
\]

Hence the clean rational certificate is

\[
\boxed{C_{135}<\frac{739733}{100000}=7.39733.}
\tag{7.3}
\]

This is a theorem about genuine real Boolean signs because it plugs into the retained Guo--Fang--Lu directional-TV finite-step theorem; no complex phase or vector coloring is introduced.

## 8. Row pruning and the moved source metric at `n=86`

Let

\[
h=\frac{739733}{100000}.
\]

For an arbitrary real `m x 86` matrix with unit Euclidean columns, write its rows as `r_i` and call a row active when

\[
\|r_i\|_2>\frac{h}{\sqrt{86}}.
\tag{8.1}
\]

The Frobenius budget gives

\[
\sum_i\|r_i\|_2^2\le86.
\tag{8.2}
\]

The exact checker verifies

\[
135<\frac{86^2}{h^2}<136.
\tag{8.3}
\]

Because activity is strict, (8.1)--(8.3) imply there are at most 135 active rows. Restrict to those rows and zero-pad to ambient row dimension 135. Equation (7.3) supplies Boolean signs with every active-row discrepancy strictly below `h`. For every inactive row, Cauchy--Schwarz gives

\[
|r_i\cdot\varepsilon|
\le\|r_i\|_2\sqrt{86}\le h.
\tag{8.4}
\]

Therefore

\[
\boxed{K_{86}^*\le\frac{739733}{100000}=7.39733.}
\tag{8.5}
\]

The preceding certificate was `73979/10000`, so the fixed metric moves by exactly

\[
\frac{73979}{10000}-\frac{739733}{100000}
=oxed{\frac{57}{100000}=0.00057}.
\tag{8.6}
\]

The fixed-metric stagnation count resets to **0**.

## 9. General new two-band branch

For completeness, the construction is not isolated to `D=135`. For every integer `D>=135`, define

\[
t_1(D)=\frac{Dt-V}{D-1}.
\]

Since `V>t`, this is increasing in `D`, and the exact `D=135` inequality `t_1(135)>mu` proves `t_1(D)>mu` for all `D>=135`.

Let

\[
P_{0,D}=p_0^D R_8(E(D,t)),
\]

\[
P_{1,D}=D(L_U-U_V)p_0^{D-1}R_8(E(D-1,t_1(D))),
\]

and

\[
\beta_D^{\downarrow,3}=\frac{P_{0,D}+P_{1,D}}{200}.
\tag{9.1}
\]

With the retained three-threshold upper-tail defect `beta_D^up`, put

\[
C_D^{(3)}=
\frac{27\sqrt{10\pi}}{20}
\left(1-\beta_D^{\uparrow}-\beta_D^{\downarrow,3}\right).
\tag{9.2}
\]

The row-pruning compiler then gives the valid source-matching branch

\[
\boxed{
L_3(n)=
\inf_{D\in\mathbb Z,\ D\ge135}
\max\left\{C_D^{(3)},\frac{n}{\sqrt{D+1}}\right\}.}
\tag{9.3}
\]

I do **not** claim in this report that `L_3` is the winning branch for every `n`; the exact demonstrated pointwise movement is `n=86`.

## 10. Complete retained fixed metric after this run

I record the complete chosen envelope rather than only its best-looking exponent.

First retain

\[
T_5=
\frac{2\sqrt2+3\sqrt3+2\sqrt{51+3\sqrt6}}{13}.
\tag{10.1}
\]

### 10.1 Earlier finite-DTV branch `G_0`

Define

\[
D_0(n)=\left\lceil\frac{10^6n^2}{7507^2}\right\rceil,
\]

\[
p_D=\frac{2e^{-1/(18D)}}{81\sqrt{2\pi}D^{3/2}},
\qquad
\delta_D=2\left[1-(1-p_D)^D\right],
\]

\[
G_0(n)=
\max\left\{
\frac{7507}{1000},
3\sqrt{2\pi}(1-\delta_{D_0(n)})
\right\}.
\tag{10.2}
\]

### 10.2 Continuous layer-cake branch `H`

Define

\[
D_*(n)=
\left\lceil\frac{400000000n^2}{22114366681}\right\rceil-1,
\]

\[
\alpha_D=\frac{2-1/D}{3\sqrt{2\pi}\sqrt D},
\qquad
\beta_D=\frac{\alpha_D}{2(1+\alpha_D)},
\]

\[
H(n)=
\max\left\{
\frac{148709}{20000},
3\sqrt{2\pi}(1-\beta_{D_*(n)})
\right\}.
\tag{10.3}
\]

### 10.3 `p=9/5` three-threshold upper-tail branch `J`

Put `GammaU=88869/100000` and, for `k=1,2,3`,

\[
A_{k,D}=
\frac{5}{7\,\Gamma_U}
\left(\frac{2k}{5}\right)^{7/5}
\left(1-\frac{2k}{5D}\right)D^{-2/5},
\qquad
a_{k,D}=\frac{A_{k,D}}D.
\]

Define

\[
\begin{aligned}
Q_D(x)=1&-(1-a_{3,D}x)^D\\
&-D(a_{3,D}-a_{1,D})x(1-a_{3,D}x)^{D-1}\\
&-\binom D2\left[(a_{3,D}-a_{2,D})^2
+2(a_{2,D}-a_{1,D})(a_{3,D}-a_{2,D})\right]
 x^2(1-a_{3,D}x)^{D-2}.
\end{aligned}
\tag{10.4}
\]

If

\[
Q_D(x)=\sum_{\ell=1}^D c_{\ell,D}x^\ell,
\]

then the retained upper-tail defect is

\[
\beta_D^{\uparrow}
=\frac12\sum_{\ell=1}^D c_{\ell,D}
\left[
\frac1{7\ell/5-1}-
\frac1{7\ell/5-1/2}
\right].
\tag{10.5}
\]

Set

\[
D_9(n)=
\left\lceil\frac{10^{10}n^2}{547864952041}\right\rceil-1,
\]

\[
J(n)=
\max\left\{
\frac{740179}{100000},
\frac{27\sqrt{10\pi}}{20}
(1-\beta_{D_9(n)}^{\uparrow})
\right\}.
\tag{10.6}
\]

### 10.4 Retained one-band lower-tail branch `L_-`

Let

\[
\Delta_-=rac{8183}{10000}-\mu,
\]

\[
E_D^-=
\frac{D\Delta_-^2}
{2U\mu+\frac23U\Delta_-},
\]

\[
R_D^-=1-
\left(1+E_D^-+\frac{(E_D^-)^2}{2}+\frac{(E_D^-)^3}{6}\right)^{-1},
\]

\[
\beta_D^{\downarrow,-}
=\frac12\left(\frac{477}{5000}\right)^2p_0^D R_D^-,
\]

\[
C_D^-=
\frac{27\sqrt{10\pi}}{20}
\left(1-\beta_D^{\uparrow}-\beta_D^{\downarrow,-}\right),
\]

\[
L_-(n)=
\inf_{D\ge135}
\max\left\{C_D^-,\frac n{\sqrt{D+1}}\right\}.
\tag{10.7}
\]

### 10.5 Retained conditional-second-moment branch `L_2`

Let

\[
t_2=\frac{987}{1250},
\qquad
q_2=\frac{557}{5000},
\qquad
\Delta_2=t_2-\mu,
\]

\[
E_D^{(2)}=
\frac{D\Delta_2^2}
{2v_*+\frac23U\Delta_2},
\]

\[
R_D^{(2)}=1-
\left(\sum_{j=0}^8\frac{(E_D^{(2)})^j}{j!}\right)^{-1},
\]

\[
\beta_D^{\downarrow,2}
=\frac{q_2^2}{2}p_0^D R_D^{(2)},
\]

\[
C_D^{(2)}=
\frac{27\sqrt{10\pi}}{20}
\left(1-\beta_D^{\uparrow}-\beta_D^{\downarrow,2}\right),
\]

\[
L_2(n)=
\inf_{D\ge135}
\max\left\{C_D^{(2)},\frac n{\sqrt{D+1}}\right\}.
\tag{10.8}
\]

### 10.6 New two-band branch `L_3`

`L_3(n)` is exactly (9.3), with all constants `U,V,p_0,mu,v_*,L_U,U_V,t` and `R_8` explicitly defined in Sections 5--9 above.

The complete certified pointwise envelope after this run is therefore

\[
\boxed{
B_{R13}(n)=
\begin{cases}
1,&n=1,\\[1mm]
\sqrt2,&n=2,\\[1mm]
(\sqrt{11}+\sqrt2)/3,&n=3,\\[1mm]
\sqrt3,&n=4,\\[1mm]
\min\!\left\{
\sqrt{3n/4},
T_5\sqrt{\lceil n/5\rceil},
G_0(n),L_-(n),L_2(n),L_3(n)
\right\},&5\le n\le85,\\[2mm]
\min\!\left\{
G_0(n),H(n),J(n),L_-(n),L_2(n),L_3(n)
\right\},&n\ge86.
\end{cases}}
\tag{10.9}
\]

The equality in (10.9) defines the **chosen certified upper envelope**, not the unknown exact values `K_n^*` except where separately proved exact (`n<=4` and the R13 theorem `K_5^*=T_5`).

The retained explicit lower-obstruction history is

\[
K_6^*\ge1.84535465,
\qquad
K_{11}^*\ge1.99488049,
\qquad
K_{12}^*\ge2.013108.
\tag{10.10}
\]

These lower bounds do not redefine the fixed upper metric.

## 11. Exact self-check and repository artifacts

The finite arithmetic checker was created only after the two-band idea produced a strict mathematical improvement:

`artifacts/R13/20260918T2203Z_twoband-middle-7d2c_checker.py`

creation/readback commit:

`20de7bcaec6c2fb75acc29bab1c6a72ac9684b86`.

It uses Python `Fraction` for every acceptance comparison. In particular it verifies:

- the rational fifth-power brackets in (6.3)--(6.4);
- positivity of the middle-band mass lower bound;
- the retained exact three-threshold `beta_135^up` calculation;
- both Bernstein exponents and eighth-order rational exponential lower certificates;
- disjoint-event probability addition;
- `C_135 < 739733/100000`;
- `135 < 86^2/h^2 < 136`;
- exact movement `73979/10000-h=57/100000`.

The executed output is archived at

`artifacts/R13/20260918T2203Z_twoband-middle-7d2c_checker.out`

creation/readback commit:

`86904ca15a3762e1e6a71243818835f88975704a`.

It terminates

`R13_TWOBAND_LOWERTAIL_EXACT_PASS`.

This is a **self-check**, not an independent OTHER-track audit.

## 12. Status, remaining obligation, and next genuinely new routes

Status:

**PARTIAL QUANTITATIVE / FIXED METRIC MOVED / full written proof / exact self-check PASS / outside audits of this new sharpening 0/2 / novelty UNVERIFIED.**

The fixed-metric stagnation count is **0**.

The two highest-value next routes are now:

1. return to the six-column target only with a truly intersection-aware exact cover/diagonal dual capable of proving a `K_6^*` upper bound below about `1.91`; do not return to scalar bad-family cardinality charging;
2. exploit the new Akbas--Sra Boolean small-ball machinery only if its constants can be specialized explicitly enough to beat the current finite envelope, rather than citing abundance qualitatively.

A third route is a genuinely symmetric nonproduct cube density. I do **not** recommend another scalar retuning of `U`, `V`, `t`, or `p` as the primary next run.

No closure claim is made; the source-level qualitative conjecture is now claimed solved by Guo--Fang--Lu, while R13 remains a finite-quantitative sharpening track.

## 13. Model / scheduler-control truth

The exposed task-control interface still has no binding model-family selector, no reasoning-effort selector, and no authenticated completed-run reasoning-effort receipt. GPT-6/maximum therefore remains prompt text only and cannot be truthfully attested for this run.

Making that enforceable requires an owner-authorized product/workspace/API/admin surface that exposes persistent model/reasoning controls and authenticated run telemetry. The historical `You cannot modify this task` response is an authorization-context boundary; repository continuity records that P26 was later editable from an authorized P/C context. The lawful workaround is the owning/otherwise-authorized task surface or platform support, not duplication, permission bypass, or a repository edit represented as a scheduler change.

No scheduler, permission, workflow, email, Drive, purchase, or public-posting action was taken.

```yaml
ledger_delta:
  worker: R13
  category: HARD_OUTSIDE
  source_id: E0042
  target: real Boolean Komlos quantitative envelope
  fixed_metric: complete rigorously certified pointwise upper envelope B_R13(n)
  before:
    anchor_n86: 73979/10000
    value: 7.3979
  after:
    anchor_n86: 739733/100000
    value: 7.39733
    new_branch: L3_two_band_inverse_chi_square_DTV
  movement:
    moved: true
    exact_delta_at_n86: 57/100000
  methods_this_run: [2, 21, 25]
  method_outcomes:
    2: K6_INTERSECTION_AWARE_ROUTE_NOT_CLOSED_NO_CLAIM
    21: AKBAS_SRA_2609_20785_CURRENT_NEIGHBOR_NO_EXPLICIT_FINITE_CONSTANT_MOVEMENT
    25: TWO_DISJOINT_LOWER_TAIL_BANDS_SUCCEED
  finite_claim:
    statement: K_86_star <= 739733/100000
    checker: artifacts/R13/20260918T2203Z_twoband-middle-7d2c_checker.py
    checker_commit: 20de7bcaec6c2fb75acc29bab1c6a72ac9684b86
    output: artifacts/R13/20260918T2203Z_twoband-middle-7d2c_checker.out
    output_commit: 86904ca15a3762e1e6a71243818835f88975704a
    self_check: PASS
  source_status:
    bansal_jiang: arXiv:2508.03961v2
    guo_fang_lu: arXiv:2609.11189v1_REAL_BOOLEAN_CONSTANT_BOUND
    akbas_sra: arXiv:2609.20785v1_BOOLEAN_SMALL_BALL_CURRENT_NEIGHBOR
    guillen_kobzar: COMPLEX_RANK_TWO_NOT_BOOLEAN
  audits_new_claim: 0/2
  novelty: UNVERIFIED
  stagnation_count: 0
  next_attack: K6_INTERSECTION_AWARE_EXACT_DUAL_OR_EXPLICIT_SMALL_BALL_CONSTANT_SPECIALIZATION
```
