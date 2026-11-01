Runtime model actually running: **GPT-5.6 Sol. Reasoning level: UNVERIFIED.**

# T05 — exact log-certified Temple optimization gives `theta_{2,1/4}>0.171884611`

**Status: PARTIAL / complete candidate bound pending later independent review.** The exact exponent is not determined. The old proposal `theta_{2,H}=H(1-H)` is not used.

## 1. Short handoff and frozen source statement

LIVE20 assigns NM13-09 to T05. The latest stronger current-master persistence result is the complementary PROB10-05 report

`runs/prob10_2026-09-20/PROB10-05/2026-09-20T1115Z__degree56_quasimode_171884.md`,

which combines the exact all-lag covariance bridge, the corrected scale-safe fourth trace, NM13-09's degree-40 non-Perron Hermite mass, and a new exact degree-56 Perron quasimode to prove the repository candidate

\[
\frac{42971}{250000}=0.171884<\theta_{2,1/4}\le \frac14.
\tag{1.1}
\]

This run preserves that work and does not overwrite the PROB10 owner history. The new attack is a one-variable exact optimization of the inherited trace/Kato--Temple synthesis, together with a rational logarithm certificate replacing the coarse integer-power endpoint grid. It produces a strict source-level improvement without changing the process, interval, or normalization.

Freeze standard fractional Brownian motion at `H=1/4`,

\[
\mathbb E B_{1/4}(t)B_{1/4}(s)
=\frac12\left(t^{1/2}+s^{1/2}-|t-s|^{1/2}\right),
\]

and

\[
I(t)=\int_0^t B_{1/4}(u)\,du.
\tag{1.2}
\]

The exact source event is

\[
p(T)=\Pr\{I(t)<1\ \text{for every }0<t<T\}
=T^{-\theta_{2,1/4}+o(1)}.
\tag{1.3}
\]

Equivalently by continuity one may use `sup_{0<=t<=T}I(t)<=1`; no discretely sampled process is substituted for the source event. Direct integration gives

\[
\operatorname{Var}I(1)=\frac25,
\]

so the unit-variance Lamperti dual is

\[
X(\tau)=\sqrt{\frac52}\,e^{-5\tau/4}I(e^\tau).
\tag{1.4}
\]

The canonical repository claim is `operations/claims/MOLCHAN-2025-THETA2H.md`. Root `POSTED.md` contains no posting exclusion closing this integrated-fBM target.

Molchan, *Persistence probabilities for fractionally integrated fractional Brownian noise*, arXiv:2509.10265, current v11 revised 4 July 2026, is the governing primary source. Its current statement gives existence/equality of the self-similar and Lamperti-stationary persistence exponents in the relevant parameter region containing `(alpha,H)=(2,1/4)`, continues to treat the one-sided `alpha=2, H!=1/2` values as unresolved, and reports the former general formula `theta_{2,H}=H(1-H)` refuted. Thus no new exponent-existence proof is needed here.

The external/source bracket remains

\[
\frac18\le \theta_{2,1/4}\le\frac14.
\tag{1.5}
\]

A fresh bounded primary-source search on 20 September 2026 also checked Molchan's August 2026 multivariate-time fBM paper (arXiv:2608.26680), Aurzada--Helmer's August 2026 fractional-Levy-field persistence paper (arXiv:2608.17463), and Zhang's April 2026 weighted-integrated fractional-process Chung/small-ball paper (arXiv:2604.01701). The retrieved theorems concern different processes, index sets, or observables and do not determine this exact continuous one-sided exponent at `H=1/4`. This is bounded negative evidence only, not a worldwide novelty certificate.

## 2. Exact covariance/comparison bridge and continuum error

Retain the corrected comparator parameters

\[
r=\frac78,\qquad s=\frac{24861}{25000},\qquad
c=s\frac{1+r}{2}=\frac{74583}{80000}.
\tag{2.1}
\]

Writing `u=e^{-|t|/4}`, the normalized Lamperti covariance is

\[
R(u)=\frac{-2u^{10}+5u^6+5u^4+2(1-u^4)^{5/2}-2}{6u^5}.
\tag{2.2}
\]

The exact all-lag comparison is

\[
\boxed{R(r^k)<c r^{k-1}\qquad(k\ge1).}
\tag{2.3}
\]

For `k=1,...,5`, put `u=r^k`, `t_k=c r^{k-1}` and

\[
A_k=6u^5t_k+2u^{10}-5u^6-5u^4+2.
\]

The desired inequality follows from `A_k>0` and

\[
A_k^2-4(1-u^4)^5>0.
\tag{2.4}
\]

The exact checker below re-executes these five rational tests; the positive margins are displayed in its output. For `k>=6`, `u=r^k<1/2`. With `z=u^2<=1/4`, the inherited exact factorization

\[
P(z)^2-4(1+z)^2(1-z^2)^3=z^3Q(z),
\]

where

\[
P(z)=2+2z-3z^2-2z^3-2z^4,
\quad
Q(z)=8z^5+16z^4+8z^3-20z^2-7z+4,
\]

and

\[
Q(z)\ge4-7z-20z^2\ge1\qquad(0\le z\le1/4),
\]

gives `R(u)<=u`. Since `c/r>1`, `R(r^k)<=r^k<c r^{k-1}` for all `k>=6`.

Let `(U_j)` be stationary Gaussian AR(1) with correlation `r`, let `(E_j)` be iid standard Gaussian independent of it, and define

\[
Y_j=\frac{U_j+U_{j-1}}{\sqrt{2(1+r)}},\qquad
Z_j=\sqrt{s}\,Y_j+\sqrt{1-s}\,E_j.
\tag{2.5}
\]

Then `Cov(Z_0,Z_k)=c r^{k-1}`. With

\[
\Delta=4\log(8/7),
\tag{2.6}
\]

continuity gives the literal inclusion

\[
\{X(t)<0\ \forall\,0\le t\le n\Delta\}
\subseteq
\{X(j\Delta)<0,\ j=1,\ldots,n\}.
\tag{2.7}
\]

Therefore the continuum-to-grid missed-crossing/interpolation error is **exactly zero in the only direction used**. No reverse sampled-to-continuous implication is claimed. Slepian plus (2.3), followed by the Lamperti exponent identity, yields

\[
\theta_{2,1/4}\ge\frac{-\log\lambda_1}{4\log(8/7)},
\tag{2.8}
\]

where `lambda_1` is the Perron eigenvalue of the same compact self-adjoint soft-edge Gaussian operator

\[
(Kf)(x)=\int p_r(x,dy)\,
\Phi\!\left(-\sqrt{\frac{s}{1-s}}\frac{x+y}{\sqrt{2(1+r)}}\right)f(y)
\tag{2.9}
\]

on `L^2(phi)`.

## 3. New mechanism: optimize the exact trace/Temple synthesis and remove the power-grid bottleneck

Use only already exact-certified spectral inputs from current master:

\[
\operatorname{tr}K^4<\frac{54959}{50000}=1.09918,
\tag{3.1}
\]

\[
L_{40}:=\sum_{j=3}^{20}a_j^4+\frac{r^{160}}{16(1-r^8)}
=0.1469733479315881\ldots,
\tag{3.2}
\]

with the rational thresholds

`0.55438, 0.42915, 0.33136, 0.25537, 0.19652, 0.15106, 0.11602, 0.08907, 0.06838, 0.05253, 0.0404, 0.03113, 0.02404, 0.01859, 0.01437, 0.01107, 0.00847, 0.0064`,

and the degree-56 Perron quasimode bounds

\[
\frac{91221208}{10^8}<\mu<\frac{91221209}{10^8},
\qquad
\varepsilon^2<\frac{677}{50000000}.
\tag{3.3}
\]

The prior synthesis selected a convenient coarse endpoint and proved `theta>0.171884`. The limiting inequalities can instead be optimized jointly. Choose

\[
\theta_*:=\frac{171884611}{10^9}=0.171884611,
\]

\[
x:=\frac{45614016081}{50000000000}=0.91228032162,
\qquad
\beta:=\frac{7137703}{10^7}=0.7137703.
\tag{3.4}
\]

A direct gigantic integer-power test at this decimal resolution is unnecessary. For `0<w<1`,

\[
2\sum_{j=0}^{m}\frac{w^{2j+1}}{2j+1}
<2\operatorname{artanh}w
<2\sum_{j=0}^{m}\frac{w^{2j+1}}{2j+1}
+\frac{2w^{2m+3}}{(2m+3)(1-w^2)}.
\tag{3.5}
\]

Take `m=14`. Since

\[
-\log x=2\operatorname{artanh}\frac{1-x}{1+x},
\qquad
\log\frac87=2\operatorname{artanh}\frac1{15},
\]

the exact rational lower/upper series bounds satisfy

\[
(-\log x)_{\rm lo}-4\theta_*(\log(8/7))_{\rm hi}>0,
\tag{3.6}
\]

with displayed margin `2.8761480263971975e-11`. Hence

\[
x<r^{4\theta_*}.
\tag{3.7}
\]

Now suppose `lambda_1>=r^{4 theta_*}>x`. By (3.1)-(3.2),

\[
\lambda_2^4<\frac{54959}{50000}-x^4-L_{40}<\beta^4,
\tag{3.8}
\]

because the exact trace margin is positive (`5.911664403438328e-08`). Thus every non-Perron spectral point is below `beta`. Since `mu>beta`, Kato--Temple gives

\[
\lambda_1\le \mu+\frac{\varepsilon^2}{\mu-\beta}.
\tag{3.9}
\]

Using only the outward bounds (3.3), the exact sufficient inequality

\[
(x-\mu_+)(\mu_- -\beta)-\varepsilon_+^2>0
\tag{3.10}
\]

has margin `4.1250836e-12`. Therefore the right side of (3.9) is strictly below `x`, contradicting the assumption. Hence

\[
\lambda_1<x<r^{4\theta_*}.
\tag{3.11}
\]

Combining (3.11) with (2.8) proves the new candidate source-model bound

\[
\boxed{\theta_{2,1/4}>\frac{171884611}{10^9}=0.171884611.}
\tag{3.12}
\]

## 4. Source-level before/after versus mechanism-level gain

### Source-level metric

Incoming current-master candidate:

\[
\frac{42971}{250000}=0.171884<\theta_{2,1/4}\le\frac14,
\qquad W=0.078116.
\]

New candidate:

\[
\boxed{\frac{171884611}{10^9}<\theta_{2,1/4}\le\frac14},
\]

with

\[
\boxed{W<\frac{78115389}{10^9}=0.078115389.}
\]

The strict lower-endpoint gain is

\[
\boxed{\frac{611}{10^9}=6.11\times10^{-7}}.
\]

The published/source bracket remains `1/8 <= theta <= 1/4`; this internal strengthening is a candidate pending independent review.

### Demonstrated mechanism gain

The new ingredient is not another discrete-grid persistence estimate and not another quasimode. It is an exact optimization of the already certified trace/Kato--Temple inequalities, together with the rational atanh-series log certificate (3.5)-(3.7). This removes the endpoint quantization imposed by the preceding convenient integer-power choice and converts the available degree-56 residual budget into a strictly stronger source-level exponent bound. The continuum comparison remains exact in its needed direction, with zero interpolation loss.

## 5. Essential executed exact checker/output

The following checker was executed in this run. All theorem-deciding inequalities use `Fraction`; decimal values are display only.

```python
from fractions import Fraction as F
r=F(7,8); s=F(24861,25000); c=s*F(1+r,2)
trace4=F(54959,50000)
mu_lo=F(91221208,100000000); mu_hi=F(91221209,100000000)
eps2_hi=F(677,50000000)
targets=[F(27719,50000),F(8583,20000),F(2071,6250),F(25537,100000),
F(4913,25000),F(7553,50000),F(5801,50000),F(8907,100000),
F(3419,50000),F(5253,100000),F(101,2500),F(3113,100000),
F(601,25000),F(1859,100000),F(1437,100000),F(1107,100000),
F(847,100000),F(4,625)]
L40=sum(a**4 for a in targets)+r**160/(F(16)*(1-r**8))
theta=F(171884611,1000000000)
x=F(45614016081,50000000000)
beta=F(7137703,10000000)
def logb(w,m):
    S=sum(w**(2*k+1)/F(2*k+1) for k in range(m+1))
    lo=2*S
    return lo,lo+2*w**(2*m+3)/(F(2*m+3)*(1-w*w))
v=(1-x)/(1+x)
num_lo,_=logb(v,14); _,den_hi=logb(F(1,15),14)
log_margin=num_lo-4*theta*den_hi
trace_margin=beta**4-(trace4-x**4-L40)
temple_margin=(x-mu_hi)*(mu_lo-beta)-eps2_hi
assert log_margin>0 and trace_margin>0 and temple_margin>0
cov=[]
for k in range(1,6):
    u=r**k; tk=c*r**(k-1)
    A=6*u**5*tk+2*u**10-5*u**6-5*u**4+2
    m=A*A-4*(1-u**4)**5
    assert A>0 and m>0
    cov.append(m)
assert c/r>1 and F(4)-F(7,4)-F(20,16)==1
incoming=F(42971,250000); upper=F(1,4)
assert theta>incoming and upper-theta<upper-incoming
print('theta =',theta,float(theta))
print('width =',upper-theta,float(upper-theta))
print('source_gain =',theta-incoming,float(theta-incoming))
print('x =',x,float(x)); print('beta =',beta,float(beta))
print('log_margin =',float(log_margin))
print('trace_margin =',float(trace_margin))
print('Temple_margin =',float(temple_margin))
print('L40 =',float(L40))
print('covariance_finite_margins =',[float(z) for z in cov])
print('ALL_EXACT_CHECKS_PASS = True')
```

Executed output:

```text
theta = 171884611/1000000000 0.171884611
width = 78115389/1000000000 0.078115389
source_gain = 611/1000000000 6.11e-07
x = 45614016081/50000000000 0.91228032162
beta = 7137703/10000000 0.7137703
log_margin = 2.8761480263971975e-11
trace_margin = 5.911664403438328e-08
Temple_margin = 4.1250836e-12
L40 = 0.1469733479315881
covariance_finite_margins = [7.78146399812076e-06, 0.0038921584429475525, 0.03541217760593994, 0.04362455218596731, 0.03396025917319854]
ALL_EXACT_CHECKS_PASS = True
```

## 6. Failures / residual obstruction / next attack

No recovery failure occurred in this run. A contemplated extension of the degree-40 Hermite min-max thresholds was assessed numerically but would improve the fourth-moment budget only at the `~1e-5` level and, with the present degree-56 residual, has negligible leverage on the exponent compared with improving the Perron residual itself. It was therefore not promoted as a theorem claim.

The dominant obstruction remains the Perron quasimode residual. The most promising next materially useful route is a degree-64/72 exact Perron certificate or a genuine two-mode enclosure that reduces the Temple residual term; merely extending the endpoint arithmetic further now has diminishing returns.

## 7. ledger_delta

```yaml
ledger_delta:
  target: T05 integrated-fBM one-sided continuous persistence at H=1/4
  source_event: "P{I(t)<1 for all 0<t<T}=T^{-theta+o(1)}, I(t)=int_0^t B_{1/4}(u)du"
  normalization: "Var I(1)=2/5; X(tau)=sqrt(5/2)e^{-5 tau/4}I(e^tau)"
  existence: "Molchan arXiv:2509.10265v11 Statement 1.2(a); no new existence proof needed"
  published_before_after: "unchanged: 1/8 <= theta_{2,1/4} <= 1/4"
  repository_before: "42971/250000 = 0.171884 < theta <= 1/4"
  repository_after: "171884611/1e9 = 0.171884611 < theta <= 1/4"
  width_before: 0.078116
  width_after: 0.078115389
  source_gain: "611/1e9 = 6.11e-7"
  mechanism_gain: "exact joint trace/Temple optimization plus m=14 rational atanh log certificate removes coarse integer-power endpoint grid"
  covariance: "R((7/8)^k) < (74583/80000)(7/8)^(k-1), all k>=1; exact finite checks k<=5 plus factorized tail"
  continuum_interpolation_error: "exactly zero in the continuous->sampled inclusion direction used; no reverse implication claimed"
  old_H1mH_formula: "not used; current Molchan source reports it refuted"
  status: "PARTIAL / complete candidate pending later independent review"
  essential_check: "ALL_EXACT_CHECKS_PASS = True"
  next_attack: "reduce Perron residual via degree-64/72 exact quasimode or a genuine two-mode enclosure"
```
