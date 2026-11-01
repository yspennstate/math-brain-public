Model actually run: **GPT-5.6 Sol**. Reasoning-effort metadata: **UNVERIFIED**.

# T05 — corrected trace / multimode composition gives `theta > 0.172344`

**Status: PARTIAL / complete candidate bound pending later independent review.** The exact exponent remains unknown. The old proposal `theta_{2,H}=H(1-H)` is neither assumed nor used.

## 0. Short handoff and controlling scope

The controlling directive is `operations/PROGRESS20_2026-09-20.md` on `master`, which assigns NM13-09 to T05 and asks for progress-first continuous-time persistence work. I did not reopen historical audit loops.

The latest own substantive report was

`proofnet24/NM13-09/progress-persistence/runs/2026-09-20/2026-09-20T1446Z__mesh22_degree40_multimode_172340.md`

(blob `a6e5b3c433b64012ac4a4362ac5aca7279d8480c`). It established the candidate

\[
\frac{8617}{50000}=0.17234<\theta_{2,1/4}\le \frac14,
\tag{0.1}
\]

using the corrected `r=22/25` comparator, a degree-40 exact Hermite min-max subtraction, and the already certified degree-56 Perron quasimode.

A newer complementary PROB10-05 report,

`runs/prob10_2026-09-20/PROB10-05/2026-09-20T1501Z__fixedpoint_K10000_172073340.md`

(blob `55e1ca02a9fd99fc46772e7d1b44eacfc6f3c1e1`), is weaker at source level than (0.1), but it gives a strictly sharper **scale-correct** same-operator fourth-trace cap

\[
\operatorname{tr}(K^4)<\frac{1143510223}{10^9}=1.143510223.
\tag{0.2}
\]

Its archived exact output has `trace upper = 1.1435102224529188` and ends `ALL_EXACT_CHECKS_PASS = True`. The new mathematics in this run is to compose (0.2), which did not use the multimode subtraction, with the exact own `L40` certificate and then re-optimize the trace/Kato--Temple contradiction. Neither peer report is modified.

Root `POSTED.md` has no exclusion closing this T05 target in the currently inherited track; canonical ownership remains HARD7-05 / the Molchan claim. No ownership, permission, schedule, or historical file is changed.

## 1. Frozen source event, normalization, existence, and external bounds

Let standard fractional Brownian motion at `H=1/4` have covariance

\[
\mathbb E B_{1/4}(t)B_{1/4}(s)
=\frac12\left(t^{1/2}+s^{1/2}-|t-s|^{1/2}\right),
\]

and define ordinary integrated fBM

\[
I(t)=\int_0^t B_{1/4}(u)\,du.
\tag{1.1}
\]

The exact source event remains

\[
\Pr\{I(t)<1\ \forall\,0<t<T\}
=T^{-\theta_{2,1/4}+o(1)}.
\tag{1.2}
\]

Direct integration gives

\[
\operatorname{Var}I(1)=\frac25,
\]

and `I` is self-similar of index `5/4`. Hence the unit-variance stationary Lamperti dual is

\[
X(\tau)=\sqrt{\frac52}\,e^{-5\tau/4}I(e^\tau).
\tag{1.3}
\]

Molchan, arXiv:2509.10265v11 (revision dated 4 July 2026), is still the governing primary source. Statement 1.2(a) states existence and equality of the self-similar and Lamperti-dual persistence exponents throughout the interior domain containing `(alpha,H)=(2,1/4)`, so no separate existence proof is needed. The paper explicitly says the one-sided `alpha=2, H != 1/2` values remain unsolved, and its abstract reports the old general `H(1-H)` hypothesis refuted. At `H=1/4`, its displayed source bounds give

\[
\boxed{\frac18\le\theta_{2,1/4}\le\frac14}.
\tag{1.4}
\]

A bounded fresh primary-source check on 20 September 2026 also inspected Molchan arXiv:2608.26680 (multivariate-time fBM persistence), Aurzada--Helmer arXiv:2608.17463 (fractional Levy fields on manifolds), Aurzada--Müller arXiv:2603.14934 (random Hurst exponent), and Zhang arXiv:2604.01701 (Chung/small-ball laws for weighted integrated fractional processes). Their retrieved results concern different processes, index sets, or observables and do not determine (1.2). This is bounded negative evidence only, not a worldwide novelty certificate.

## 2. Source-level before/after

The incoming valid internal frontier is (0.1). This run proves the stronger complete candidate

\[
\boxed{\theta_{2,1/4}>\theta_*:=\frac{21543}{125000}=0.172344.}
\tag{2.1}
\]

Thus the candidate lower endpoint gains exactly

\[
\theta_*-\frac{8617}{50000}=\frac1{250000}=0.000004,
\tag{2.2}
\]

and the internal bracket width shrinks

\[
0.07766\longrightarrow
\boxed{\frac{9707}{125000}=0.077656}.
\tag{2.3}
\]

The published/source bracket (1.4) is unchanged. Equation (2.1) remains a repository candidate pending independent review.

## 3. Continuous-time covariance comparison and interpolation direction

Writing `u=e^{-|t|/4}`, the Lamperti covariance is

\[
R(u)=\frac{-2u^{10}+5u^6+5u^4+2(1-u^4)^{5/2}-2}{6u^5}.
\tag{3.1}
\]

Retain the corrected comparator

\[
r=\frac{22}{25},\qquad
c=\frac{936901}{10^6},\qquad
s=\frac{936901}{940000},\qquad
c=s\frac{1+r}{2}.
\tag{3.2}
\]

For stationary standard Gaussian AR(1) states `(U_j)` with correlation `r`, iid standard Gaussians `(E_j)` independent of them, and

\[
Y_j=\frac{U_j+U_{j-1}}{\sqrt{2(1+r)}},\qquad
Z_j=\sqrt{s}\,Y_j+\sqrt{1-s}\,E_j,
\tag{3.3}
\]

we have `Cov(Z_0,Z_k)=c r^{k-1}` for `k>=1`.

The exact checker below re-executes

\[
\boxed{R(r^k)<c r^{k-1}\qquad(k\ge1).}
\tag{3.4}
\]

For `k=1,2`, isolate the positive radical in (3.1) and square. The exact rational squared margins are positive; their decimal displays are

`1.334296986263307e-4`, `2.3302146180526656e-7`.

For `k>=3`, Taylor's theorem gives

\[
(1-z)^{5/2}\le1-\frac52z+\frac{15}{8}z^2,
\]

hence

\[
R(u)\le\frac56u+\frac58u^3-\frac13u^5.
\tag{3.5}
\]

After dividing by `r^{k-1}`, set `q=r^{2k}`. The remaining factor

\[
g(q)=\frac56+\frac58q-\frac13q^2
\]

is increasing on `0<=q<=r^6`, since `5/8-(2/3)r^6>0`. Therefore `k=3` is worst, and the exact endpoint margin is

\[
c-r\left(\frac56+\frac58r^6-\frac13r^{12}\right)
=0.011408957976493094\ldots>0.
\tag{3.6}
\]

Set

\[
\Delta=-4\log r=4\log\frac{25}{22}.
\tag{3.7}
\]

Continuity gives the literal event inclusion

\[
\{X(t)<0\ \forall\,0\le t\le n\Delta\}
\subseteq
\{X(j\Delta)<0,\ j=0,\ldots,n\}.
\tag{3.8}
\]

Thus the continuum interpolation / missed-crossing loss is **exactly zero in the lower-bound direction actually used**. No reverse grid-to-continuum inference is made. Slepian and (3.4) give

\[
\theta_{2,1/4}\ge
\frac{-\log\lambda_1}{4\log(25/22)},
\tag{3.9}
\]

where `lambda_1` is the Perron eigenvalue of the compact self-adjoint killed transfer operator `K` for the comparator.

## 4. Demonstrated mechanism gain: cross-certificate spectral composition

This run does not claim the new trace cap (0.2) as its own derivation; that is the fresh neighboring PROB10 certificate. Its gain over the cap used in my previous run is

\[
1.143529-1.143510223=0.000018777.
\tag{4.1}
\]

The own degree-40 min-max certificate supplies the exact lower bounds

\[
\begin{array}{rclcrcl}
\lambda_3&>&0.568227,&&\lambda_4&>&0.444701,\\
\lambda_5&>&0.347205,&&\lambda_6&>&0.270606,\\
\lambda_7&>&0.210618,&&\lambda_8&>&0.163758,\\
\lambda_9&>&0.127228,&&\lambda_{10}&>&0.098807,\\
\lambda_{11}&>&0.076732,&&\lambda_{12}&>&0.059615,\\
\lambda_{13}&>&0.046360,&&\lambda_{14}&>&0.036105,\\
\lambda_{15}&>&0.028166,&&\lambda_{16}&>&0.022000,\\
\lambda_{17}&>&0.017179,&&\lambda_{18}&>&0.013377,\\
\lambda_{19}&>&0.010355,&&\lambda_{20}&>&0.007919,
\end{array}
\tag{4.2}
\]

plus, from the even-Hermite min-max subspaces,

\[
\lambda_j\ge\frac12r^{2(j-1)}\qquad(j\ge1).
\tag{4.3}
\]

Therefore the forced fourth spectral mass away from the top two modes is

\[
L_{40}:=\sum_{j=3}^{20}a_j^4+\frac{r^{160}}{16(1-r^8)}
=0.16635513479783687\ldots .
\tag{4.4}
\]

Retain the same-operator degree-56 Perron quasimode bounds

\[
\frac{9155053441}{10^{10}}<\mu<\frac{9155053442}{10^{10}},
\qquad
\varepsilon^2<\frac{270154}{10^{10}}.
\tag{4.5}
\]

The new synthesis chooses

\[
x=\frac{91564617}{10^8}=0.91564617,
\qquad
\beta=\frac{7236486}{10^7}=0.7236486.
\tag{4.6}
\]

Suppose `lambda_1>=x`. If `lambda_2>=beta`, then (0.2) and (4.4) would require

\[
\operatorname{tr}(K^4)\ge x^4+\beta^4+L_{40},
\]

but the exact checker proves

\[
\beta^4-\left(\frac{1143510223}{10^9}-x^4-L_{40}\right)
>1.7025593108\times10^{-7}.
\tag{4.7}
\]

Hence `lambda_2<beta<mu`. Kato--Temple then yields

\[
\lambda_1\le\mu+\frac{\varepsilon^2}{\mu-\beta}.
\]

Using only the outward bounds in (4.5), the exact rational margin is

\[
(x-\mu_+)(\mu_- -\beta)-\varepsilon_+^2
>2.97947327778\times10^{-9},
\tag{4.8}
\]

so the right side is strictly below `x`, contradiction. Thus

\[
\lambda_1<x.
\tag{4.9}
\]

Finally `4 theta_*=21543/31250`, and the checker verifies the exact integer-power inequality

\[
\boxed{x^{31250}<r^{21543}},
\tag{4.10}
\]

so `x<r^{4theta_*}`. Equations (3.9), (4.9), and (4.10) prove (2.1).

The demonstrated mechanism-level before/after is therefore: the trace cap improves by `1.8777e-5` from complementary prior work; composing it with the existing exact multimode subtraction tightens the contradiction separator from the previous convenient `beta=0.724` to `beta=0.7236486`, while retaining a positive exact Temple margin, and transfers this to a source endpoint gain of `4e-6`.

## 5. Essential executed exact checker and output

The theorem-deciding arithmetic was re-executed in this run using Python `Fraction`; no Monte Carlo or sampled-path persistence fit is involved.

```python
from fractions import Fraction as F

r=F(22,25)
c=F(936901,10**6)
targets=[F(a,10**6) for a in [
    568227,444701,347205,270606,210618,163758,127228,98807,
    76732,59615,46360,36105,28166,22000,17179,13377,10355,7919]]
L40=sum(a**4 for a in targets)+r**160/(F(16)*(1-r**8))
T=F(1143510223,10**9)
mu_lo=F(9155053441,10**10)
mu_hi=F(9155053442,10**10)
eps2=F(270154,10**10)
theta=F(21543,125000)
x=F(91564617,10**8)
beta=F(7236486,10**7)

rad=[]
for k in (1,2):
    u=r**k
    cap=c*r**(k-1)
    A=6*u**5*cap+2*u**10-5*u**6-5*u**4+2
    margin=A*A-4*(1-u**4)**5
    assert A>0 and margin>0
    rad.append(margin)
deriv_margin=F(5,8)-F(2,3)*r**6
tail_endpoint=r*(F(5,6)+F(5,8)*r**6-F(1,3)*r**12)
assert deriv_margin>0 and tail_endpoint<c

trace_margin=beta**4-(T-x**4-L40)
temple_margin=(x-mu_hi)*(mu_lo-beta)-eps2
assert x>mu_hi>mu_lo>beta
assert trace_margin>0 and temple_margin>0
assert x**31250 < r**21543

incoming=F(8617,50000)
upper=F(1,4)
assert theta>incoming
print('L40 =',float(L40))
print('cov k=1,2 margins =',[float(z) for z in rad])
print('tail derivative margin =',float(deriv_margin))
print('tail endpoint c-margin =',float(c-tail_endpoint))
print('trace cap =',float(T))
print('theta =',theta,float(theta))
print('x =',float(x),'beta =',float(beta))
print('trace separation margin =',float(trace_margin))
print('Temple margin =',float(temple_margin))
print('exact power comparison =',x**31250 < r**21543)
print('incoming lower/width =',float(incoming),float(upper-incoming))
print('new lower/width =',float(theta),float(upper-theta))
print('source gain =',float(theta-incoming))
print('ALL_EXACT_CHECKS_PASS = True')
```

Executed output:

```text
L40 = 0.16635513479783687
cov k=1,2 margins = [0.0001334296986263307, 2.3302146180526656e-07]
tail derivative margin = 0.3153972754773333
tail endpoint c-margin = 0.011408957976493094
trace cap = 1.143510223
theta = 21543/125000 0.172344
x = 0.91564617 beta = 0.7236486
trace separation margin = 1.7025593108429841e-07
Temple margin = 2.97947327778e-09
exact power comparison = True
incoming lower/width = 0.17234 0.07766
new lower/width = 0.172344 0.077656
source gain = 4e-06
ALL_EXACT_CHECKS_PASS = True
```

## 6. Failures, unknowns, and next attack

The exact exponent is still unknown, the source upper endpoint remains `1/4`, and there is no reverse grid-to-continuum theorem here. I briefly tested a more finely quantized endpoint near the floating feasibility boundary; a naive direct rational power comparison with exponents of order `10^7` was computationally wasteful and was abandoned without promotion. The clean endpoint (2.1) uses an exact power comparison with exponents only `31250` and `21543` and retains comfortable spectral margins.

No unchanged-run trigger fires: this run makes a strict source gain and uses a new cross-certificate composition. The current bottleneck remains the degree-56 Perron residual, not the fourth-trace tail or second-mode separator. A materially higher-leverage next attack is a directly certified degree-64/72 same-operator Perron quasimode or a genuine two-vector Ritz enclosure. A distinct non-spectral route, if needed after further residual failures, is the reverse continuous interpolation / negative-margin grid-survival comparison; it is presently incomplete and therefore not used.

## 7. `ledger_delta`

```yaml
ledger_delta:
  target: T05 integrated-fBM persistence, H=1/4
  status: PARTIAL_CANDIDATE_FULL_PENDING_REVIEW
  source_event: "P{I(t)<1 for all 0<t<T}=T^{-theta+o(1)}"
  normalization: "Var I(1)=2/5; X(tau)=sqrt(5/2)e^{-5 tau/4}I(e^tau)"
  source_published_before: "1/8 <= theta <= 1/4"
  source_published_after: "1/8 <= theta <= 1/4"
  internal_before: "0.17234 < theta <= 0.25"
  internal_after: "0.172344 < theta <= 0.25"
  internal_lower_gain: 0.000004
  internal_width_before: 0.07766
  internal_width_after: 0.077656
  covariance_bridge: "R((22/25)^k) < (936901/1e6)(22/25)^(k-1), all k>=1"
  continuum_interpolation_loss_used_direction: 0
  inherited_new_trace_cap: "tr(K^4) < 1.143510223"
  multimode_mass: "L40 > 0.16635513479783687"
  new_separator: "lambda2 < 0.7236486 under lambda1>=0.91564617"
  exact_checks: PASS
  failures: "finer naive giant-power quantization abandoned as computationally wasteful; no mathematical claim"
  remaining_obstruction: "degree-56 Perron residual / no reverse-margin continuous interpolation theorem"
  next_attack: "degree-64/72 same-operator quasimode or two-vector Ritz enclosure"
```
