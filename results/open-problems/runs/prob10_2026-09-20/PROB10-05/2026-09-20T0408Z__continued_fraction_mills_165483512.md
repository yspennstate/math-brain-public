Runtime model actually running: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — this is not GPT-6 at maximum, and I do not claim otherwise. PROB10-05 repository candidate metric MOVED: `165483/1000000 < theta_{2,1/4} <= 1/4` (width `84517/1000000 = 0.084517`) -> `20685439/125000000 < theta_{2,1/4} <= 1/4` (width `10564561/125000000 = 0.084516488`).**

# PROB10-05 bounded research iteration — continued-fraction Mills supersolution and `theta_{2,1/4}>0.165483512`

**Status: PARTIAL / source target OPEN / self-checked candidate pending independent validation.**

Freeze centered standard fractional Brownian motion with `H=1/4`,

\[
I(t)=\int_0^t B_{1/4}(s)\,ds,
\]

and the continuous fixed-barrier persistence event on `[0,T]`. The source exponent convention is the one-sided exponent

\[
\Pr\{I(t)<1\text{ for }0<t<T\}=T^{-\theta_{2,1/4}+o(1)}.
\]

The strict/non-strict deterministic barrier convention is inherited from the source/repository normalization; this run does not change the process, interval, graph, or barrier normalization.

The new result of this run, conditional only on the already archived all-lag covariance comparison, four-cycle Plackett decrement, and degree-18 quasimode data identified below, is

\[
\boxed{\theta_{2,1/4}>\frac{20685439}{125000000}=0.165483512}.\tag{0.1}
\]

Together with the retained source-valid upper endpoint `1/4`, the repository candidate bracket is

\[
\boxed{\frac{20685439}{125000000}<\theta_{2,1/4}\le\frac14},\qquad
\boxed{W_{1/4}=\frac{10564561}{125000000}=0.084516488}.\tag{0.2}
\]

The external published/source baseline remains `1/8 <= theta_{2,1/4} <= 1/4`; (0.1) is repository research progress, not a literature claim and not closure.

## 1. Continuity, ownership, source status, and consumed updates

Read/consumed on current `master`:

- `operations/PROB10_2026-09-20.md`;
- root `POSTED.md`;
- canonical claim `operations/claims/MOLCHAN-2025-THETA2H.md` (owner `HARD7-05`);
- previous own report `runs/prob10_2026-09-20/PROB10-05/2026-09-20T0302Z__mills_ratio_165480.md`;
- actual predecessor history `runs/hard7_2026-09-18/HARD7-05/2026-09-19T2250Z__triple_orthant_trace_164800.md` as linked by the preceding PROB10 reports;
- newest complementary covariance/comparison report `proofnet24/NM13-09/progress-persistence/runs/2026-09-20/2026-09-20__taylor-plackett-165483.md`.

The directory listing for the complementary route was checked before this write; its newest substantive report was the `165483` Taylor-Plackett report, so (0.1) does not overwrite a stronger same-route checkpoint. Canonical ownership remains `HARD7-05`; this file is the owner-directed PROB10 continuation and consumes, rather than takes over, NM13-09's 256-block decrement.

The primary source is G. Molchan, *Persistence probabilities for fractionally integrated fractional Brownian noise*, arXiv:2509.10265v11. A fresh bounded check of the full arXiv PDF on 20 September 2026 re-confirmed the relevant model: the natural persistence domain is `Omega={alpha+H>1,0<H<1}`, ordinary integrated fBM is the `alpha=2` line, the one-sided `alpha=2,H != 1/2` values are explicitly described as unsolved, and the old formula `theta_{2,H}=H(1-H)` is reported refuted via the new duality/monotonicity theory. The same bounded search recovered Aurzada--Kilian (2022) and later 2026 neighboring persistence papers but no exact continuous one-sided value at `H=1/4`. This is dated negative evidence only, not a worldwide novelty certificate.

The source's exponent-existence/Lamperti identification used by the repository remains the v11 Statement 1.2(a) result in the domain above. Thus no new existence claim is made here.

## 2. Frozen inherited comparison data

Keep the comparator parameters

\[
r=\frac78,\qquad s=\frac{24861}{25000},
\]

and the inherited all-lag covariance domination. With `Delta=4 log(8/7)`, continuous survival implies sampled survival:

\[
\{X(t)<0\ \forall\,0\le t\le n\Delta\}
\subseteq
\{X(j\Delta)<0,\ j=1,\ldots,n\}.
\tag{2.1}
\]

Hence the lower-bound direction has **zero continuous-to-grid interpolation loss**. Slepian plus the inherited comparator gives

\[
\theta_{2,1/4}\ge \frac{-\log\lambda_1}{4\log(8/7)},\tag{2.2}
\]

where `lambda_1` is the Perron eigenvalue of the compact self-adjoint killed transfer operator `K`.

The inherited normalized degree-18 quasimode obeys

\[
\frac{9116948312}{10^{10}}<\mu<\frac{9116948313}{10^{10}},\qquad
\varepsilon^2<\frac{47004495}{10^{11}}.\tag{2.3}
\]

From the previous PROB10 report, the equicorrelated four-cycle endpoint after the first Mills improvement obeys

\[
\frac{P_{\rm eq}}{1-r^4}<1.090902,\tag{2.4}
\]

where that displayed cap used the scalar resolvent bound `E[(1+qY^2)^(-1)]<0.91`. From the newest complementary NM13-09 report, consume the independent exact 256-block Plackett decrement

\[
P_{\rm eq}-P_{\rm cyc}>\frac{743}{200000}.\tag{2.5}
\]

No Plackett quadrature is redone in this run.

## 3. Idea-before-code checkpoint

Before any new checker, the new route and two alternatives were written and committed in

`artifacts/prob10_2026-09-20/PROB10-05/2026-09-20T0345Z__continued_fraction_mills_idea.md`

at commit `8938a30e636486b2b5b6e5787e00018dc690b5c8`.

The primary route is a new **continued-fraction/Riccati** sharpening of the Gaussian resolvent endpoint. It is distinct from NM13-09's finer Plackett quadrature and from the preceding algebraic square-root Mills supersolution.

## 4. New lemma: a tenth-convergent Mills supersolution

Let

\[
m(x)=e^{x^2/2}\int_x^\infty e^{-v^2/2}\,dv,\qquad x>0,
\]

be the Gaussian Mills ratio. Then

\[
m'(x)=xm(x)-1.\tag{4.1}
\]

Define

\[
u_{10}(x)=
\frac{x^{10}+54x^8+938x^6+6090x^4+12645x^2+3840}
{x\left(x^{10}+55x^8+990x^6+6930x^4+17325x^2+10395\right)}.
\tag{4.2}
\]

This is the even tenth convergent of the classical Gaussian continued fraction. Direct exact differentiation gives

\[
 u_{10}'(x)-(xu_{10}(x)-1)
 =-
 \frac{39916800}
 {x^2\left(x^{10}+55x^8+990x^6+6930x^4+17325x^2+10395\right)^2}
 <0.\tag{4.3}
\]

Set `d=u_{10}-m`. From (4.1)--(4.3),

\[
(d(x)e^{-x^2/2})'
=e^{-x^2/2}\{u_{10}'-(xu_{10}-1)\}<0.\tag{4.4}
\]

Both `u_{10}(x)` and `m(x)` are `O(1/x)` as `x->infinity`, so

\[
\lim_{x\to\infty}d(x)e^{-x^2/2}=0.
\]

Integrating (4.4) from `x` to infinity therefore gives

\[
0-d(x)e^{-x^2/2}<0,
\]

hence

\[
\boxed{m(x)<u_{10}(x)\qquad(x>0).}\tag{4.5}
\]

This proof is global in `x`; no finite sampling is involved.

## 5. Exact resolvent specialization

The inherited endpoint reduction has

\[
q=\frac{202269096}{1697549515},\qquad x=q^{-1/2},
\]

and the exact identity

\[
\mathbb E\frac1{1+qY^2}=xm(x),\qquad Y\sim N(0,1).\tag{5.1}
\]

Multiplying (4.5) by `x` and substituting `q=x^{-2}` yields

\[
\mathbb E\frac1{1+qY^2}
< R_{10}(q),\tag{5.2}
\]

where

\[
R_{10}(q)=
\frac{1+54q+938q^2+6090q^3+12645q^4+3840q^5}
{1+55q+990q^2+6930q^3+17325q^4+10395q^5}.\tag{5.3}
\]

The executed exact checker gives

\[
R_{10}(q)=0.908852390107374841\ldots<0.909<0.91.\tag{5.4}
\]

Thus this run improves the scalar endpoint factor from the previous certified `<0.91` to `<0.908852391` (the displayed decimal is only a rendering of the exact rational in the checker).

## 6. Equicorrelated endpoint and fourth-trace improvement

The previous endpoint proof has the coefficient

\[
\frac1{16}\sqrt{\frac{1-\rho}{1+\rho}},
\qquad
\rho=\frac{168557580}{170952323},
\]

and had already certified

\[
\sqrt{\frac{1-\rho}{1+\rho}}>\frac{8398}{100000}.\tag{6.1}
\]

Therefore replacing `0.91` by `R_{10}(q)` improves the **normalized** equicorrelated endpoint by at least

\[
\delta_{\rm cf}:=
\frac{8398}{100000}
\frac{\frac{91}{100}-R_{10}(q)}{16(1-r^4)}.
\tag{6.2}
\]

Exact arithmetic gives

\[
\delta_{\rm cf}=1.45559453500649431\ldots\times10^{-5}.\tag{6.3}
\]

Consequently (2.4) sharpens to

\[
\frac{P_{\rm eq}}{1-r^4}
<1.090902-\delta_{\rm cf}
=1.09088744405464988\ldots.\tag{6.4}
\]

Combining (6.4) with the separately certified decrement (2.5),

\[
\operatorname{tr}(K^4)
<1.090902-\delta_{\rm cf}
-\frac{743/200000}{1-(7/8)^4}
=1.08191007532308658\ldots
<\frac{270477519}{250000000}.
\tag{6.5}
\]

Thus the cyclic fourth-trace cap moves

\[
1.081925\longrightarrow 1.081910076
\]

at the simple displayed rational level.

## 7. Spectral contradiction at `theta*=0.165483512`

Set

\[
\theta_*:=\frac{20685439}{125000000}=0.165483512,
\qquad
x_0:=\frac{572127961}{625000000}=0.9154047376,
\tag{7.1}
\]

and

\[
\beta:=\frac{7849948769}{10^{10}}=0.7849948769.\tag{7.2}
\]

### 7.1 Exact proof that `x_0<r^{4 theta_*}` without huge integer powers

For `0<a<1`, put `z=(1-a)/(1+a)`. Then

\[
-\log a
=2\sum_{k=0}^\infty \frac{z^{2k+1}}{2k+1}.\tag{7.3}
\]

For every `N>=0`, positivity gives the exact rational enclosure

\[
L_N(z):=2\sum_{k=0}^N\frac{z^{2k+1}}{2k+1}
< -\log a
< L_N(z)+
\frac{2z^{2N+3}}{(2N+3)(1-z^2)}=:U_N(z).\tag{7.4}
\]

At `N=3`, the checker proves exactly

\[
L_3(z_{x_0})-4\theta_*U_3(z_r)
=7.83853230708144104\ldots\times10^{-11}>0.\tag{7.5}
\]

Hence

\[
-\log x_0>4\theta_*(-\log r),
\]

so

\[
\boxed{x_0<r^{4\theta_*}}.\tag{7.6}
\]

### 7.2 Fourth-trace tail and Temple inequality

Assume for contradiction that

\[
\lambda_1\ge r^{4\theta_*}.
\]

By (7.6), `lambda_1>x_0`. From (6.5), every non-Perron spectral value satisfies

\[
|\lambda_j|^4
<\frac{270477519}{250000000}-x_0^4.
\]

The exact checker proves

\[
\beta^4-
\left(\frac{270477519}{250000000}-x_0^4\right)
=1.12967785182434199\ldots\times10^{-10}>0,\tag{7.7}
\]

so every non-Perron spectral value lies in `[-beta,beta]`.

Using the inherited quasimode interval (2.3), the spectral-measure/Temple inequality then gives

\[
\varepsilon^2
\ge(\lambda_1-\mu)(\mu-\beta)
>(x_0-\mu_{\rm hi})(\mu_{\rm lo}-\beta).\tag{7.8}
\]

But exact rational arithmetic gives

\[
(x_0-\mu_{\rm hi})(\mu_{\rm lo}-\beta)
-\frac{47004495}{10^{11}}
=\frac{866728209}{10^{20}}
>0,\tag{7.9}
\]

a contradiction. Therefore

\[
\lambda_1<r^{4\theta_*}.
\]

Substitution in (2.2) proves (0.1).

## 8. Three materially different attacks compared

### Attack A — even continued-fraction/Riccati Mills hierarchy: SUCCESS

This is Sections 4--7. It attacks the scalar resolvent endpoint and moves the candidate lower endpoint by

\[
\frac{20685439}{125000000}-\frac{165483}{10^6}
=\frac1{1953125}=5.12\times10^{-7}.
\]

The mechanism-level trace gain is much larger than the final source-level gain because the inherited quasimode/Temple margin is now close to saturation.

### Attack B — reverse continuous-time interpolation to attack the upper endpoint: BLOCKED by non-Markov conditioning

A useful upper-bound route would need a uniform grid-to-continuum estimate of the form

\[
\Pr\{X(t)<0\ \forall t\le n\Delta\}
\ge e^{-n\varepsilon(\Delta,\eta)}
\Pr\{X(j\Delta)<-\eta,\ 1\le j\le n\},\tag{8.1}
\]

with explicit `epsilon(Delta,eta)` that can be optimized. Conditioning only on adjacent endpoints is insufficient: the Lamperti dual is not Markov, so after conditioning on the entire grid the interior conditional mean depends on all grid values, and the regression coefficients need not have the sign needed to compare it with the two-endpoint bridge. The exact missing lemma is a uniform all-grid conditional bridge estimate

\[
\inf_{\mathbf x\le-\eta}
\Pr\{\sup_{0\le t\le\Delta}X(t)<0
\mid X(j\Delta)=x_j,\ j\in\mathbb Z\}
\ge1-\epsilon(\Delta,\eta).\tag{8.2}
\]

No such estimate is proved here. Therefore there is **no movement of the upper endpoint** and no discrete-sampling claim is promoted to continuous time.

### Attack C — positive-operator Collatz--Wielandt supersolution: OPEN, precise boundary obstruction retained

A pointwise `Kh<=lambda h` with `h>0` would yield `lambda_1<=lambda` directly and bypass `tr(K^4)` plus Temple. The natural probit/Gaussian ansatz can exploit closure of Gaussian integrals, but the killed boundary makes the ratio `Kh/h` singular if `h` decays too quickly, while the existing polynomial/Hermite quasimode only controls the residual in `L^2`. The missing statement is a boundary-adapted positive `h` with a **uniform relative residual** below `r^{4*0.165483512}`. No such function was proved in this run; this remains the most plausible route to a non-microscopic next gain on the lower endpoint.

These attacks are genuinely different: scalar Riccati comparison, continuum Gaussian bridge control, and positive-operator Perron comparison.

## 9. Exact checker and actual execution

The checker was created only after the idea checkpoint:

`artifacts/prob10_2026-09-20/PROB10-05/2026-09-20T0354Z__continued_fraction_mills_exact_check.py`

creation commit `acd30a35581997394c4668dc7d4e002acdc9b500`.

Executed stdout is archived at

`artifacts/prob10_2026-09-20/PROB10-05/2026-09-20T0354Z__continued_fraction_mills_exact_check.out`

creation commit `819d4ad31d5d197a769735c1a0a8340d02fa9e26`.

The process exited successfully and stdout ends

`ALL_EXACT_CHECKS_PASS = True`.

The checker verifies exactly:

1. the symbolic Riccati residual identity (4.3);
2. the exact rational `R_10(q)<0.909`;
3. the normalized endpoint improvement `delta_cf`;
4. the trace bound (6.5);
5. the exact logarithmic enclosure proving `x_0<r^{4 theta_*}`;
6. the fourth-trace spectral-tail separation;
7. the Temple contradiction margin;
8. the before/after source-candidate widths.

A Python startup hook emitted an unrelated spreadsheet-runtime warmup timeout on stderr after the checker stdout; the checker itself returned exit code `0`, all asserted theorem comparisons passed, and that unrelated environment message is not used as mathematical evidence.

## 10. Before/after and remaining full-scope gap

### External literature/source baseline

No change:

\[
\frac18\le\theta_{2,1/4}\le\frac14.
\]

No exact `H=1/4` value was found in the bounded current literature check.

### Repository candidate metric

Before, consuming the newest complementary report:

\[
\frac{165483}{10^6}<\theta_{2,1/4}\le\frac14,
\qquad W=\frac{84517}{10^6}=0.084517.
\]

After:

\[
\boxed{\frac{20685439}{125000000}<\theta_{2,1/4}\le\frac14},
\qquad
\boxed{W=\frac{10564561}{125000000}=0.084516488}.
\]

Candidate lower-end gain: `1/1953125 = 5.12e-7`.

### Auxiliary mechanism progress

- scalar Gaussian resolvent cap: `<0.91 -> <0.908852391`;
- normalized equicorrelated endpoint cap: `<1.090902 -> <1.0908874441`;
- cyclic fourth-trace cap: `<1.081925 -> <1.081910076`.

### Remaining full-scope gap

The exact exponent is still unknown and the upper endpoint remains `1/4`. This lower-bound architecture is visibly near saturation: the final Temple margin in (7.9) is only about `8.67e-12`. Further scalar endpoint polishing will therefore buy almost nothing unless accompanied by a stronger quasimode/pointwise Perron certificate. The next substantive run should change mechanism within this same problem: either (i) a boundary-adapted Collatz--Wielandt supersolution, or (ii) a valid reverse continuous-time interpolation theorem that can move the upper endpoint.

This report remains **PARTIAL / OPEN**. It is a self-check, not either of the independent validations required for source closure.