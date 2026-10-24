Model actually run: **GPT-5.6 Sol**. Reasoning-effort metadata: **UNVERIFIED**.

# T05 — low-degree residual correction gives `theta > 0.172406`

**Status: PARTIAL / complete candidate bound pending later independent review.** The exact exponent remains unknown. The old proposal `theta_{2,H}=H(1-H)` is neither assumed nor used.

## 0. Short handoff and controlling scope

`operations/PROGRESS20_2026-09-20.md` on `master` assigns NM13-09 to T05 and prioritizes new mathematics with only essential dependency checks. Root `POSTED.md` does not close this T05 target.

The latest own substantive report entering this run was

`proofnet24/NM13-09/progress-persistence/runs/2026-09-20/2026-09-20T1543Z__trace_multimode_composition_172344.md`

which established the complete repository candidate

\[
\frac{21543}{125000}=0.172344<\theta_{2,1/4}\le\frac14
\]

for the corrected `r=22/25` comparator, using the scale-correct fourth-trace cap

\[
\operatorname{tr}(K^4)<\frac{1143510223}{10^9}=1.143510223,
\]

the exact degree-40 non-Perron fourth-mass subtraction

\[
L_{40}>0.16635513479783687,
\]

and the inherited degree-56 Perron witness

\[
0.9155053441<\mu<0.9155053442,\qquad
\varepsilon^2<2.70154\times 10^{-5}.
\]

That run identified the Perron residual as the dominant obstruction.

A first attack in the present run recomputed a numerically optimized degree-56 Ritz vector for the *actual corrected operator*. High-precision reconnaissance gave

\[
\mu_{\rm num}=0.915514418850826431\ldots,\qquad
\varepsilon^2_{\rm num}=1.9140460860\ldots\times10^{-5},
\]

which would support a numerical synthesis near `theta=0.17241227`. However a full all-entries exact interval recomputation of the new 57-coefficient witness exceeded a 180-second local execution budget. It is therefore **not promoted**.

Instead, this run executes a different rigorous route: correct the already-certified degree-56 witness only by a degree-7 polynomial. Then all new one-step/two-step information is carried by rectangular cross moments against degrees `0,...,7`, while the old full degree-56 aggregate certificate remains usable. The resulting exact checker completes and yields the strict source-model advance below.

## 1. Frozen source event, normalization, existence, and proved literature bounds

Let standard fractional Brownian motion at `H=1/4` have covariance

\[
\mathbb E B_{1/4}(t)B_{1/4}(s)
=\frac12\left(t^{1/2}+s^{1/2}-|t-s|^{1/2}\right),
\]

and define ordinary integrated fBM

\[
I(t)=\int_0^t B_{1/4}(u)\,du.
\]

The exact one-sided continuous-time event is frozen as

\[
\Pr\{I(t)<1\ \forall\,0<t<T\}=T^{-\theta_{2,1/4}+o(1)}.
\]

Direct integration gives

\[
\operatorname{Var}I(1)=\frac25,
\]

and `I` is self-similar of index `5/4`. Hence the unit-variance stationary Lamperti dual is

\[
X(\tau)=\sqrt{\frac52}\,e^{-5\tau/4}I(e^\tau).
\]

Molchan, arXiv:2509.10265v11, Statement 1.2(a), states that for interior parameters `(alpha,H)` the persistence exponents of the self-similar process and its Lamperti dual exist and are identical. Thus no separate exponent-existence proof is needed at `(alpha,H)=(2,1/4)`. The same revision explicitly says the one-sided `alpha=2, H != 1/2` values remain unsolved and reports the long-standing `H(1-H)` hypothesis refuted.

Evaluating the proved bounds quoted in that source at `H=1/4` gives the external/source bracket

\[
\boxed{\frac18\le \theta_{2,1/4}\le\frac14}.
\]

A bounded later-primary check in this run also inspected Molchan arXiv:2608.26680 (multivariate-time fBM persistence), Aurzada--Helmer arXiv:2608.17463 (fractional Levy fields on manifolds), and Zhang arXiv:2604.01701 (Chung/small-ball laws for weighted integrated fractional processes). These concern different index sets/processes/observables and do not determine the present one-sided integrated-fBM exponent. This is bounded negative evidence only.

## 2. Source-level before/after

The incoming valid repository candidate is

\[
0.172344<\theta_{2,1/4}\le\frac14.
\]

This run proves the stronger complete candidate

\[
\boxed{\theta_{2,1/4}>
\theta_*:=\frac{86203}{500000}=0.172406.}
\]

Therefore the candidate lower endpoint gains exactly

\[
\theta_*-\frac{21543}{125000}
=\frac{31}{500000}=0.000062,
\]

and the candidate bracket width shrinks

\[
0.077656\longrightarrow
\boxed{\frac{193985}{2500000}=0.077594}.
\]

The published/source bracket `1/8 <= theta <= 1/4` is unchanged. The new endpoint is a repository candidate pending independent review.

## 3. Continuous-time covariance comparison and zero interpolation loss

Writing `u=e^{-|t|/4}`, the Lamperti covariance is

\[
R(u)=
\frac{-2u^{10}+5u^6+5u^4+2(1-u^4)^{5/2}-2}{6u^5}.
\]

Retain the corrected comparator

\[
r=\frac{22}{25},\qquad
c=\frac{936901}{10^6},\qquad
s=\frac{936901}{940000},
\qquad
c=s\frac{1+r}{2}.
\]

For stationary standard Gaussian AR(1) states `(U_j)` with correlation `r`, iid standard Gaussians `(E_j)` independent of them, and

\[
Y_j=\frac{U_j+U_{j-1}}{\sqrt{2(1+r)}},\qquad
Z_j=\sqrt{s}\,Y_j+\sqrt{1-s}\,E_j,
\]

we have `Cov(Z_0,Z_k)=c r^{k-1}` for `k>=1`.

The exact checker re-executes

\[
\boxed{R(r^k)<c\,r^{k-1}\qquad(k\ge1).}
\]

For `k=1,2`, after isolating the positive radical and squaring, the exact rational margins display as

\[
1.334296986263307\times10^{-4},
\qquad
2.3302146180526656\times10^{-7}.
\]

For `k>=3`,

\[
(1-z)^{5/2}\le1-\frac52z+\frac{15}{8}z^2
\]

implies

\[
R(u)\le\frac56u+\frac58u^3-\frac13u^5.
\]

The remaining factor is monotone over the relevant interval, so `k=3` is worst; the exact endpoint margin is

\[
c-r\left(\frac56+\frac58r^6-\frac13r^{12}\right)
=0.011408957976493094\ldots>0.
\]

Set

\[
\Delta=-4\log r=4\log\frac{25}{22}.
\]

Continuity gives the literal event inclusion

\[
\{X(t)<0\ \forall\,0\le t\le n\Delta\}
\subseteq
\{X(j\Delta)<0,\ j=0,\ldots,n\}.
\]

Thus the continuum interpolation / missed-crossing loss is **exactly zero in the lower-bound direction actually used**. No reverse grid-to-continuum inference is asserted. Slepian then gives

\[
\theta_{2,1/4}\ge
\frac{-\log\lambda_1}{4\log(25/22)},
\]

where `lambda_1` is the Perron eigenvalue of the compact self-adjoint killed transfer operator of the comparator.

## 4. New mechanism: a degree-7 correction certified by cross moments

Let `f_0` be the inherited degree-56 polynomial witness stored at

`artifacts/prob10_2026-09-20/PROB10-05/2026-09-20T1055Z__degree56_witness.txt`

with blob `8c2448736bb1ea40eeb50babdde1b459711232f9`.

Its full same-operator certificate is

\[
\mu_0\in(0.9155053441,0.9155053442),
\qquad
\varepsilon_0^2<2.70154\times10^{-5}.
\]

Define

\[
f=f_0+g,\qquad g(x)=\sum_{j=0}^7 d_jx^j,
\]

with integer coefficients

\[
\begin{aligned}
(d_0,\ldots,d_7)=(&-1087105685652313791875237923618658991172095756466,\\
&1496574855703050430700931563947530380755550751779,\\
&-246895860741300460427139828024037096404334686770,\\
&-223447817588070398365714952341211778193532903211,\\
&15667059489881465851364439266901793139286427566,\\
&22102221035478010508170416919078582235719330693,\\
&-402002293201538370451473038427033964843164175,\\
&-678533929844847041298771443872518079448651294).
\end{aligned}
\]

(The common scale of a witness is irrelevant.)

The point of choosing a low-degree correction is that the old expensive aggregate can be retained. Write

\[
q_0=\langle f_0,f_0\rangle,\quad
m_0=\langle f_0,Kf_0\rangle,\quad
n_0=\langle Kf_0,Kf_0\rangle .
\]

The inherited certificate gives rigorous intervals for `m_0/q_0` and `n_0/q_0`. For `f=f_0+g`,

\[
\begin{aligned}
q&=q_0+2\langle f_0,g\rangle+\langle g,g\rangle,\\
m&=m_0+2\langle f_0,Kg\rangle+\langle g,Kg\rangle,\\
n&=n_0+2\langle Kf_0,Kg\rangle+\langle Kg,Kg\rangle.
\end{aligned}
\]

Every new cross term has one polynomial degree at most `7`. The checker evaluates these terms using the same exact Gaussian truncated-moment recurrences and outward fixed-point rational intervals as the inherited full checker, but only on the necessary rectangular block. It obtains

\[
\boxed{
0.9155135020229033<\mu<0.9155135021284977
}
\]

and

\[
\boxed{
\varepsilon^2<1.9849071121714623\times10^{-5}.
}
\]

For the final proof I retain only the coarser safe rationals

\[
\mu_-:=0.9155135020<\mu<
0.9155135022=:\mu_+,
\]

\[
\varepsilon^2<1.98491\times10^{-5}=:\varepsilon_+^2.
\]

Hence the certified residual upper bound falls from `2.70154e-5` to `1.98491e-5`, a reduction of about **26.53%**, without any new full 57-by-57 exact recomputation.

This is the mechanism-level advance of the run. It directly improves the Perron upper enclosure and therefore the source persistence lower bound.

## 5. Spectral synthesis

Retain the scale-correct fourth-trace cap

\[
T:=\operatorname{tr}(K^4)<1.143510223
\]

and the exact forced non-Perron fourth mass

\[
L_{40}>
0.16635513479783687.
\]

Choose

\[
x=\frac{5722607}{6250000}=0.91561712,
\qquad
\beta=\frac{14474147}{20000000}=0.72370735.
\]

Assume for contradiction `lambda_1>=x`. If `lambda_2>=beta`, then

\[
\operatorname{tr}(K^4)\ge x^4+\beta^4+L_{40},
\]

whereas the exact checker gives the positive separation margin

\[
\beta^4-(T-x^4-L_{40})
=3.38604364954114\times10^{-8}>0.
\]

Thus `lambda_2<beta<mu_-`. Kato--Temple gives

\[
\lambda_1\le
\mu+\frac{\varepsilon^2}{\mu-\lambda_2}
<
\mu_+ +\frac{\varepsilon_+^2}{\mu_- -\beta}.
\]

The exact rational contradiction margin is

\[
(x-\mu_+)(\mu_- -\beta)-\varepsilon_+^2
=2.54314967056\times10^{-8}>0.
\]

Therefore

\[
\lambda_1<x.
\]

Finally, with

\[
\theta_*=\frac{86203}{500000},
\qquad
4\theta_*=\frac{86203}{125000},
\]

the checker verifies the exact integer-power inequality

\[
\boxed{x^{125000}<r^{86203}}.
\]

Hence `x<r^{4 theta_*}`. Combined with the continuum Slepian reduction,

\[
\theta_{2,1/4}>
\frac{-\log x}{4\log(25/22)}
>\theta_*,
\]

which proves the candidate bound in Section 2.

## 6. Failed route and remaining obstruction

The full operator-specific degree-56 Ritz reoptimization is promising but not yet a theorem certificate in this run. Its high-precision values (`mu~0.9155144188508264`, `eps^2~1.9140460860e-5`) are numerically better than the certified low-degree-correction witness, and a floating synthesis suggests an endpoint near `0.17241227`. However the all-entry exact checker timed out locally at 180 seconds, so these numbers are **CONJECTURAL reconnaissance only**.

The degree-7 correction route avoids that computational obstruction while retaining most of the residual gain and has a fully executed exact checker.

The next high-leverage attack is either:
- certify the full optimized degree-56 witness by a similarly factorized/cross-update argument, or
- add another low-degree Hermite/Ritz correction block to the present certified witness and update only the new rectangular cross moments.

Blindly extending the fourth-trace Hermite tail is lower leverage at the current residual scale.

## 7. Essential executed checker core and output

The exact checker reuses the immutable Gaussian moment recurrences from the previously certified degree-56 operator checker, but computes only rectangular cross blocks against `g`. The theorem-deciding synthesis is:

```python
from fractions import Fraction as F

r=F(22,25)
T=F(1143510223,10**9)

targets=[F(a,10**6) for a in [
 568227,444701,347205,270606,210618,163758,127228,98807,
 76732,59615,46360,36105,28166,22000,17179,13377,10355,7919]]
L40=sum(a**4 for a in targets)+r**160/(F(16)*(1-r**8))

# Outward coarsenings obtained by the exact rectangular cross-moment engine.
mu_lo=F(9155135020,10**10)
mu_hi=F(9155135022,10**10)
eps_hi=F(198491,10**10)

theta=F(86203,500000)
x=F(5722607,6250000)
beta=F(14474147,20000000)

trace_margin=beta**4-(T-x**4-L40)
temple_margin=(x-mu_hi)*(mu_lo-beta)-eps_hi

assert trace_margin>0
assert temple_margin>0
assert x**125000 < r**86203
assert theta > F(21543,125000)
```

Executed output:

```text
mu interval 0.9155135020229033 0.9155135021284977
eps upper exact-derived 1.9849071121714623e-05
mu coarse 0.915513502 0.9155135022 eps coarse 1.98491e-05
cov margins [0.0001334296986263307, 2.3302146180526656e-07] 0.011408957976493094
L40 0.16635513479783687 trace 1.143510223
theta,x,beta 0.172406 0.91561712 0.72370735
trace margin 3.38604364954114e-08
Temple margin 2.54314967056e-08
incoming/new widths 0.077656 0.077594
source gain 6.2e-05
ALL_EXACT_CHECKS_PASS = True
```

No Monte Carlo, sampled-path persistence fit, or reverse grid interpolation enters any promoted inequality.

## 8. ledger_delta

```yaml
ledger_delta:
  task: T05
  worker: NM13-09
  status: PARTIAL_CANDIDATE
  exact_event: "P{I(t)<1 for all 0<t<T}=T^{-theta_{2,1/4}+o(1)}"
  normalization:
    var_I1: "2/5"
    lamperti: "X(tau)=sqrt(5/2)e^{-5tau/4}I(e^tau)"
  existence: "Molchan arXiv:2509.10265v11 Statement 1.2(a)"
  external_proved_before: "[1/8,1/4]"
  external_proved_after: "[1/8,1/4]"
  repository_candidate_before: "[0.172344,0.25]"
  repository_candidate_after: "[0.172406,0.25]"
  source_lower_gain: "0.000062"
  candidate_width_before: "0.077656"
  candidate_width_after: "0.077594"
  comparator:
    r: "22/25"
    c: "936901/1000000"
    s: "936901/940000"
    all_lag: "R(r^k)<c r^(k-1), k>=1"
    continuum_loss_direction_used: "0 exactly"
  mechanism:
    type: "degree-7 correction of certified degree-56 witness with exact rectangular cross moments"
    old_eps2_upper: "2.70154e-5"
    new_eps2_upper: "1.98491e-5"
    residual_reduction_fraction: "~0.2653"
    trace_cap: "1.143510223"
    L40_lower: "0.16635513479783687"
    x: "0.91561712"
    beta: "0.72370735"
    trace_margin: "3.38604364954114e-8"
    temple_margin: "2.54314967056e-8"
    integer_power_transfer: "x^125000 < (22/25)^86203"
  failed_route:
    type: "full exact recomputation of numerically optimized degree-56 witness"
    outcome: "timed out locally at 180s; not promoted"
    numerical_only_endpoint: "~0.17241227"
  old_formula_H1mH: "not used; source reports refuted"
  discrete_grid_claim: "none"
  review: "complete candidate pending later independent review"
  next_attack: "factorized exact certification of full optimized witness or an additional low-degree correction block"
```
