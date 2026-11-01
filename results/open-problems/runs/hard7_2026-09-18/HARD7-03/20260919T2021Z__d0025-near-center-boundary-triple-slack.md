Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — this is not GPT-6 at maximum, and I do not claim otherwise. Frozen metric MOVED: `L <= Delta_2(Q): 50000/584101 -> 5000000/58398337`. Methods tried: B11 / B14 / B25.**

# HARD7-03 — near-edge and central structural zero-gap triple slack

Status: **PARTIAL**. Seppäläinen Problem 4 remains open in its full source scope.

## 1. Continuity, source, ownership, and current-status checks

This run resumes the exclusive canonical claim

`operations/claims/D0025.md`, owner `HARD7-03`, canonical key `disordered_asep_open_1999::problem_4`, status `ADMITTED_ACTIVE / HARD / PARTIAL`.

At run start I re-read the governing files

- `operations/hard7_2026-09-18/CONTROL.md`,
- `operations/NEW_METHODS_2026-09-16.md`,
- `operations/new_methods_2026-09-16/OWNER_DIRECTIVE.md`,
- `probability_campaign_2026_09/INDEX.md` and `RANKING.md`,
- root `POSTED.md`, `RESULTS.md`, and `QUEUE.md`,
- `operations/claims/D0025.md` and the D0025 intake/search trail,
- the newest own checkpoint `runs/hard7_2026-09-18/HARD7-03/20260919T1921Z__d0025-edge-boundary-triple-slack.md`,
- and the newest visible neighboring HARD7-02 / HARD7-04 directory state.

The neighboring workers are on distinct non-Hermitian heavy-tail and growing-random-graph targets, respectively. A repository-wide exact-key/alias search still identifies HARD7-03 as the D0025 owner; no release, collision, posted equivalent, or external-resolution record was found. Shared root ledgers were not edited in this run.

The primary source remains Timo Seppäläinen, *Recent Results and Open Problems on the Hydrodynamics of Disordered Asymmetric Exclusion and Zero-Range Processes*, Resenhas IME-USP 4(1) (1999), 1--15, Problem 4, arXiv `math/9906194`, DOI `10.11606/resimeusp.v4i1.74889`. The source asks whether the disordered asymmetric finite-capacity `K`-exclusion model has the analogous phase transition, in particular a flat macroscopic-flux segment around density `K/2`.

A fresh bounded literature check on **19 September 2026** used the exact source title together with the queries `disordered K-exclusion plateau K=2 site disorder`, `partial exclusion random environment asymmetric site disorder plateau`, and variants. It recovered Floreani--Redig--Sau, *Hydrodynamics for the partial exclusion process in random environment* (`arXiv:1911.12564`, SPA 142 (2021), 124--158), whose random environment is random maximal site occupancy, and Gonçalves--Hayashi--Sasada, *Characterization of Gradient Condition for Asymmetric Partial Exclusion Processes and Their Scaling Limits* (`arXiv:2405.15142`), whose asymmetric partial-exclusion rates are in a different product-rate/gradient class. No theorem closing the exact iid site-rate `K>=2` residual surfaced. The honest status is therefore **OPEN_BY_BOUNDED_SEARCH**, not a worldwide-openness or novelty certificate.

The frozen first case and tracked quantity are unchanged:

\[
K=2,\qquad Q=\frac12\delta_{1/2}+\frac12\delta_1,
\]

\[
\Delta_2(Q)=\sup\{\delta\ge0:f_{2,Q}\text{ is constant on }[1-\delta,1+\delta]\},
\]

with the fixed metric a rigorous lower bound `L <= Delta_2(Q)`.

### Runtime capability honesty

The exposed task surface still provides task title/prompt, schedule/timing and enabled-state controls, but **no binding model selector, no reasoning-effort selector, no authenticated reasoning telemetry and no guaranteed run-duration field**. Hence GPT-6/maximum remains prompt-requested only. This invocation identifies as GPT-5.6 Sol and the reasoning level is unavailable, so it is recorded as `UNVERIFIED`.

Making GPT-6/maximum binding would require a platform scheduler/API surface that exposes model and reasoning-effort fields and authenticates the runtime selection. A repository edit cannot create that capability. The historical P26 `You cannot modify this task` response is an authorization/context restriction; the compliant workaround is modification from the owning/authorized account or workspace, or platform support/ownership remediation. It is not permissible to bypass the denial or create a duplicate schedule. No schedule was created, modified, reactivated, or disabled in this run.

## 2. Carry-in and the source-relevant before/after quantity

The preceding immutable checkpoint used

\[
\theta=\frac{57343}{100000}
\tag{2.1}
\]

and, after recovering an exact structural zero-gap correction at the two outer edge triples, certified

\[
G_1(0)\le A_{\rm carry}:=\frac{584101}{200000}=2.920505,
\tag{2.2}
\]

so the already proved D0025 transfer

\[
\Delta_2(Q)\ge \frac1{4G_1(0)}
\tag{2.3}
\]

gave

\[
L_{\rm carry}=\frac{50000}{584101}
=0.085601633963989\ldots.
\tag{2.4}
\]

That checkpoint explicitly left the analogous **near-edge and central structural equality strata** untreated. This run attacks those strata and proves

\[
\boxed{G_1(0)\le A_{\rm new}:=\frac{58398337}{20000000}=2.91991685,}
\tag{2.5}
\]

hence

\[
\boxed{
\Delta_2(Q)\ge L_{\rm new}
:=\frac{5000000}{58398337}
=0.085618876441636\ldots .}
\tag{2.6}
\]

Thus the frozen source-relevant metric moves rigorously

\[
\boxed{
L:\quad \frac{50000}{584101}
\longrightarrow
\frac{5000000}{58398337}}
\tag{2.7}
\]

with exact positive gain

\[
L_{\rm new}-L_{\rm carry}
=\frac{588150000}{34110527040037}>0.
\tag{2.8}
\]

This is a theorem for the frozen `K=2` binary-disorder case only. It does **not** close Seppäläinen's full general-`K` problem.

Before writing any checker, the mathematical routes were committed and read back in

- `artifacts/hard7_2026-09-18/HARD7-03/20260919T2021Z__idea-near-edge-boundary-triple-slack.md` @ `f1b5975dcf6f06bad97350bbebe4179dc4892de5`,
- `artifacts/hard7_2026-09-18/HARD7-03/20260919T2022Z__idea-center-boundary-triple-slack.md` @ `05b6715aeca6e09e2c4c42dbd2649b8bf4bb5f3e`.

The previous run used B4/B13/B30. This run uses the distinct triple **B11/B14/B25**.

## 3. The exact fresh-layer boundary bonus

Retain the inherited notation

\[
a=1-\theta,\qquad b=2-\theta,\qquad c=3-\theta,
\qquad \kappa=\frac{\theta}{bc}.
\tag{3.1}
\]

For predecessor gaps `u,v`, the exact fresh-layer triple-slack kernel from the preceding checkpoint chain is

\[
\Phi_\theta(u,v)
=\theta\int_0^\infty e^{\theta t}(1-e^{-t})
 e^{-(t-u)_+-(t-v)_+}\,dt.
\tag{3.2}
\]

When one gap is positive and the other is structurally zero, `u>=0,v=0`, direct splitting at `t=u` gives

\[
\Phi_\theta(u,0)
=\frac{\theta}{ab}(1-e^{-au})
+\frac{\theta}{bc}e^{-bu}.
\tag{3.3}
\]

The global local-minimum baseline already subtracted in the inherited envelope is `kappa`, so the unused nonnegative bonus is

\[
B_0(u)
:=\Phi_\theta(u,0)-\kappa
=\frac{\theta}{ab}(1-e^{-au})
-\frac{\theta}{bc}(1-e^{-bu}).
\tag{3.4}
\]

It is strictly positive for `u>0`, since `B_0(0)=0` and

\[
B_0'(u)=\frac{\theta}{b}(e^{-au}-e^{-bu})>0
\qquad (u>0),
\tag{3.5}
\]

because `0<a<b`.

The outer-edge version of this mechanism was the entire new correction in the preceding run. The point of the present run is that **the same zero-gap phenomenon occurs on additional positive-measure near-edge and central order strata**, but their middle variable is a nontrivial maximum rather than a single shifted exponential.

## 4. B11 — dualize every zero-gap branch to one Laplace scalar

The key simplification is a transform identity that is stronger than the particular near-edge and central cases.

Suppose, after conditioning on older layers, an event has the form

\[
U>M>Y,
\tag{4.1}
\]

where the deterministic shifts of all three shifted unit exponentials are at most a common level `s_*`, while `M>s_*` on the event. Define

\[
T_r=\mathbb E\left[e^{\theta M-r(U-M)};U>M>Y\right],
\qquad r\ge0.
\tag{4.2}
\]

Conditional on `M=m>s_*`, the upper shifted exponential is already in its pure tail region. If its deterministic shift is `s_U`, then

\[
\mathbb E[e^{-rU};U>m]
=\int_m^\infty e^{-ru}e^{s_U-u}\,du
=\frac{e^{s_U-(1+r)m}}{1+r}.
\tag{4.3}
\]

Everything else in the conditional integrand is independent of `r`. Therefore

\[
\boxed{T_r=\frac{T_0}{1+r}.}
\tag{4.4}
\]

Substituting `r=a` and `r=b` into (3.4), using `1+a=b` and `1+b=c`, yields the exact universal boundary correction

\[
\begin{aligned}
C_0
&=\frac{\theta}{ab}(T_0-T_a)
 -\frac{\theta}{bc}(T_0-T_b)\\
&=\boxed{\theta T_0\left(\frac1{b^2}-\frac1{c^2}\right)}>0.
\end{aligned}
\tag{4.5}
\]

Thus each structural zero-gap branch reduces to a single positive scalar `T_0`; no separate evaluation of the `a`- and `b`-tilted transforms is needed.

**B11 outcome: successful.** The boundary problem is dualized to one scalar Laplace mass, and the positivity is automatic once `T_0>0`.

## 5. B25 — count the near-edge maximum exactly

Use the inherited layer-two variables

\[
\begin{aligned}
Y_{-2}&=A_{-1}+B_{-2},\\
Y_{-1}&=\max(A_{-1},A_0)+B_{-1},\\
Y_0&=\max(A_{-1},A_0,A_1)+B_0,\\
Y_1&=\max(A_0,A_1)+B_1,\\
Y_2&=A_1+B_2,
\end{aligned}
\tag{5.1}
\]

where the displayed `A` and `B` variables are independent unit exponentials.

For the right near-edge fourth-step triple (`d=1`) put

\[
S_0=\max(Y_{-1},Y_0,Y_1),\quad
S_1=\max(Y_0,Y_1,Y_2),\quad
S_2=\max(Y_1,Y_2),
\tag{5.2}
\]

and define

\[
M=\max(Y_1,Y_2),\qquad U=Y_{-1}.
\tag{5.3}
\]

On the strict event

\[
\mathcal E_{\rm near}=\{U>M>Y_0\},
\tag{5.4}
\]

we have

\[
S_0=U>S_1=S_2=M,
\tag{5.5}
\]

so the two predecessor gaps entering the triple kernel are exactly

\[
(u,v)=(U-M,0).
\tag{5.6}
\]

This is disjoint from the previously corrected strict mixed-sign branch

\[
\{Y_{-1}>Y_0>\max(Y_1,Y_2)\},
\tag{5.7}
\]

because (5.4) has the reverse strict ordering between `M` and `Y_0`.

Condition on the `A` layer and write

\[
s_U=\max(A_{-1},A_0),\quad
s_0=\max(A_{-1},A_0,A_1),\quad
s_1=\max(A_0,A_1),\quad s_2=A_1.
\tag{5.8}
\]

Deterministically `s_0>=s_U,s_1,s_2`. On (5.4), `M>Y_0>=s_0`, so every shifted exponential in the remaining integral is in its pure tail region. For `m>=s_0`, the density of `M=max(Y_1,Y_2)` is exactly

\[
f_M(m)=e^{s_1-m}+e^{s_2-m}-2e^{s_1+s_2-2m}.
\tag{5.9}
\]

Also

\[
\Pr(Y_0<m\mid A)=1-e^{s_0-m},
\qquad
\Pr(U>m\mid A)=e^{s_U-m}.
\tag{5.10}
\]

Consequently

\[
T_{0,\rm near}\mid A
=\int_{s_0}^\infty e^{\theta m}f_M(m)
(1-e^{s_0-m})e^{s_U-m}\,dm.
\tag{5.11}
\]

With `d=4-theta`, direct expansion and integration gives

\[
\boxed{
T_{0,\rm near}\mid A
=\frac{e^{s_U+s_1-bs_0}+e^{s_U+s_2-bs_0}}{bc}
-\frac{2e^{s_U+s_1+s_2-cs_0}}{cd}.}
\tag{5.12}
\]

On each of the six strict order cones of `(A_{-1},A_0,A_1)`, all the `s_j` in (5.12) are order statistics. If

\[
x_{\rm low}=z_1,\quad x_{\rm mid}=z_1+z_2,
\quad x_{\rm high}=z_1+z_2+z_3,
\tag{5.13}
\]

then the iid exponential density is `exp(-3z_1-2z_2-z_3)`. Thus each monomial in (5.12) integrates to a product of three reciprocal positive rational rates. At rational `theta`, the result is an exact rational number.

The exact checker obtains

\[
T_{0,\rm near}=0.707792202261255\ldots,
\tag{5.14}
\]

and hence from (4.5)

\[
\boxed{C_{\rm near}^{(0)}
=0.130505601012907\ldots>0.}
\tag{5.15}
\]

Reflection supplies the same correction at the left near-edge endpoint.

**B25 near-edge outcome: successful.** The nontrivial two-variable maximum is integrated completely, with no sampling or numerical quadrature.

## 6. B14/B25 — the two central structural-equality orientations

For the center fourth-step triple set

\[
S_{-1}=\max(Y_{-2},Y_{-1},Y_0),\quad
S_0=\max(Y_{-1},Y_0,Y_1),\quad
S_1=\max(Y_0,Y_1,Y_2).
\tag{6.1}
\]

Put

\[
M=\max(Y_0,Y_1),\qquad L=\max(Y_{-1},Y_2).
\tag{6.2}
\]

One orientation is

\[
\mathcal E_{\rm cen,L}=\{Y_{-2}>M>L\}.
\tag{6.3}
\]

Then

\[
S_{-1}=Y_{-2}>S_0=S_1=M,
\tag{6.4}
\]

so again `(u,v)=(Y_{-2}-M,0)`. Reflection gives the opposite orientation. The two are disjoint because (6.3) forces `Y_{-2}>Y_2`, while its reflection forces `Y_2>Y_{-2}`. They are also disjoint from the previously corrected strict mixed-sign central branches, because there the intermediate predecessor lies *above* the common-window maximum rather than below it.

Condition on the first layer and write

\[
s_U=A_{-1},\quad
s_0=\max(A_{-1},A_0,A_1),\quad
s_1=\max(A_0,A_1),
\tag{6.5}
\]

\[
\ell_1=\max(A_{-1},A_0),\qquad \ell_2=A_1.
\tag{6.6}
\]

Here `M=max(s_0+B_0,s_1+B_1)` is automatically at least `s_0`, and every other deterministic shift in (6.3) is at most `s_0`. Therefore the B11 identity (4.4) applies again.

For `m>=s_0`,

\[
f_M(m)=e^{s_0-m}+e^{s_1-m}-2e^{s_0+s_1-2m},
\tag{6.7}
\]

while

\[
\Pr(L<m\mid A)
=(1-e^{\ell_1-m})(1-e^{\ell_2-m}),
\qquad
\Pr(Y_{-2}>m\mid A)=e^{s_U-m}.
\tag{6.8}
\]

Thus

\[
T_{0,\rm center}\mid A
=\int_{s_0}^\infty e^{\theta m}f_M(m)
(1-e^{\ell_1-m})(1-e^{\ell_2-m})e^{s_U-m}\,dm.
\tag{6.9}
\]

Expanding the three density terms in (6.7) against the four CDF terms in (6.8) produces twelve exponential monomials. Every term has the form

\[
C\,e^{\alpha_Us_U+\alpha_0s_0+\alpha_1s_1+eta_1\ell_1+eta_2\ell_2}
\int_{s_0}^\infty e^{-\lambda m}\,dm,
\tag{6.10}
\]

with a positive rational `lambda` at (2.1). The integral is `e^{-lambda s_0}/lambda`, after which the same six order-cone change of variables (5.13) evaluates the entire expression in exact rational arithmetic.

The checker obtains, for one orientation,

\[
T_{0,\rm center}=0.555468234624386\ldots,
\tag{6.11}
\]

and hence

\[
\boxed{C_{\rm center}^{(0)}
=0.102419489182895\ldots>0.}
\tag{6.12}
\]

Reflection supplies a second disjoint copy.

**B14 outcome: successful.** Reflection is used only after proving disjointness, so the central correction is doubled without overlap.

**B25 center outcome: successful.** The genuine maximum-vs-maximum branch is reduced to twelve exact monomials and integrated exhaustively over all six first-layer order cones.

## 7. No double counting with earlier corrections

There are three separate reasons the new subtraction is legitimate.

First, the deterministic max/min identity used in the four-step recursion separates the adjacent-pair terms from the triple-slack term. The present corrections modify only the triple-slack lower bound; they do not overlap any pair correction.

Second, within the triple term, the earlier exact strict mixed-sign corrections and the present structural-zero-gap branches occupy disjoint strict order events. For the near edge the old event is `U>Y_0>M`, whereas the new event is `U>M>Y_0`. For the center the analogous intermediate ordering is likewise reversed.

Third, the two near-edge reflected contributions belong to different fourth-step endpoints, and the two center orientations force opposite strict orderings of the two outer variables. Hence the four new pieces can be added.

The preceding outer-edge structural-zero-gap correction is already built into the carry-in envelope. The new exact checker reconstructs that carry-in value and subtracts **only** the newly proved near-edge and central pieces.

## 8. Exact certificate and the moved shape/plateau bound

At (2.1), the new exact corrections are

\[
C_{\rm near}^{(0)}=0.130505601012907\ldots,
\qquad
C_{\rm center}^{(0)}=0.102419489182895\ldots.
\tag{8.1}
\]

Their reflected total triple-slack increment is

\[
\Delta H
=2C_{\rm near}^{(0)}+2C_{\rm center}^{(0)}>0.
\tag{8.2}
\]

The triple slack enters the inherited four-step moment envelope divided by `q=1-theta`, so

\[
U_{4,\rm new}
=U_{4,\rm carry}-\frac{\Delta H}{1-\theta}.
\tag{8.3}
\]

The exact checker obtains

\[
U_{4,\rm carry}=811.446461083686813\ldots,
\tag{8.4}
\]

\[
\frac{\Delta H}{1-\theta}
=1.092083785525482\ldots,
\tag{8.5}
\]

and therefore

\[
U_{4,\rm new}=810.354377298161353\ldots.
\tag{8.6}
\]

Choose the rational candidate

\[
A_{\rm new}=\frac{58398337}{20000000}=2.91991685.
\tag{8.7}
\]

Set

\[
x=4\theta A_{\rm new}
=\frac{3348735838591}{500000000000}.
\tag{8.8}
\]

For `x>0`,

\[
S_{32}(x):=\sum_{k=0}^{32}\frac{x^k}{k!}<e^x.
\tag{8.9}
\]

The executed checker proves in exact rational arithmetic

\[
S_{32}(x)-U_{4,\rm new}>0,
\tag{8.10}
\]

with numerical margin

\[
S_{32}(x)-U_{4,\rm new}
=1.811500473005034\times10^{-5}\ldots .
\tag{8.11}
\]

Hence

\[
U_{4,\rm new}<S_{32}(x)<e^{4\theta A_{\rm new}}.
\tag{8.12}
\]

The already established four-step block Chernoff argument therefore gives (2.5), and the inherited plateau transfer (2.3) gives (2.6).

The exact checker is

`artifacts/hard7_2026-09-18/HARD7-03/zero_gap_near_center_20260919T2021Z.py`

created at commit

`d47866eec4d85eb80138f2996bbd842baadb857e`.

Its archived exact output is

`artifacts/hard7_2026-09-18/HARD7-03/zero_gap_near_center_20260919T2021Z.out`

at commit

`16e60e0e89d6d289f292babf2da2f3476f5d81b4`.

The checker was re-executed during this run with Python exact `Fraction` arithmetic. The independently executed values agree with the archived output:

- `T0_near = 0.707792202261255...`,
- `C_near0 = 0.130505601012907...`,
- `T0_center = 0.555468234624386...`,
- `C_center0 = 0.102419489182895...`,
- `U_refined = 810.3543772981614...`,
- `S32_minus_U_refined = 1.811500473005034e-05 > 0`,
- `L_new = 5000000/58398337`.

The archived output terminates

`ALL_EXACT_CHECKS_PASS = True`.

This is a **self-check**, not an independent audit.

## 9. What the three new-method moves taught us

### B11 — dualize

Successful. The decisive simplification is not another ad hoc order-cone inequality: every pure-tail structural-zero-gap branch has the exact transform `T_r=T_0/(1+r)`. This removes two thirds of the transform work and turns positivity into a one-scalar question.

### B14 — find the group acting

Successful. Reflection doubles both the near-edge and central corrections, but only after exact disjointness checks. At the center it is especially important not to treat the two orientations as the same event: they force opposite strict outer-variable orderings.

### B25 — count the same thing twice

Successful. Instead of bounding the nested maxima, expand their exact density/CDF products. The near edge becomes three monomials after integration; the center becomes twelve. Each is then an order-cone rational integral. This is a more scalable route than manufacturing another coarse domination event.

The tracked quantity moved, so section-I stuck rotation is **not** triggered.

## 10. Remaining obligation and next route

The full source problem is still far beyond the frozen certificate. Even for the frozen `K=2` binary case, the four-step Chernoff envelope is not the exact homogeneous lazy-LPP central shape. The present run completes the obvious positive-measure structural family in which one predecessor gap is exactly zero and the other is positive at the five fourth-step locations, but other strict two-gap order chambers still lose slack.

The next run should not repeat B11/B14/B25. A useful next triple is **B5 / B19 / B24**:

- **B5:** treat the Chernoff parameter and a chamber-selection parameter jointly rather than optimizing theta only after the inequality is frozen;
- **B19:** turn the remaining triple-kernel chamber expansion into a finite exploration algorithm that emits disjoint order cells automatically;
- **B24:** identify which unresolved chamber maximizes the lost slack and attack that extremal obstruction first.

The next source-relevant milestone remains the same frozen quantity `L <= Delta_2(Q)`, not a finite-size current simulation.

## 11. Ledger delta for the authorized reconciler

```yaml
ledger_delta:
  track: HARD7-03
  canonical_claim: D0025
  source_key: disordered_asep_open_1999::problem_4
  status: PARTIAL
  source_status: OPEN_BY_BOUNDED_SEARCH
  metric: "rigorous lower bound L <= Delta_2(Q) for K=2, Q=(delta_1/2+delta_1)/2"
  before: "50000/584101"
  after: "5000000/58398337"
  before_decimal: 0.085601633963989
  after_decimal: 0.085618876441636
  exact_gain: "588150000/34110527040037"
  methods: [B11, B14, B25]
  checker: artifacts/hard7_2026-09-18/HARD7-03/zero_gap_near_center_20260919T2021Z.py
  output: artifacts/hard7_2026-09-18/HARD7-03/zero_gap_near_center_20260919T2021Z.out
  checker_commit: d47866eec4d85eb80138f2996bbd842baadb857e
  output_commit: 16e60e0e89d6d289f292babf2da2f3476f5d81b4
  exact_check: ALL_EXACT_CHECKS_PASS
  closure: false
  audits: "not requested; source not closed"
  next_methods: [B5, B19, B24]
```

No shared-root file was edited. No email, Drive action, public post, peer-track file edit, schedule edit, duplicate schedule, or closure claim was made.