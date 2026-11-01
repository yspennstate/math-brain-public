Runtime model actually running: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — this is not GPT-6 at maximum, and I do not claim otherwise. PROB10-05 source metric MOVED: `3307/20000 < theta_{2,1/4} <= 1/4` (width `1693/20000 = 0.08465`) -> `517/3125 < theta_{2,1/4} <= 1/4` (width `1057/12500 = 0.08456`).**

# PROB10-05 bounded research iteration — certified piecewise Plackett quadrature and `theta_{2,1/4}>0.16544`

**Status: PARTIAL / source target OPEN / new lower bound pending independent validation.**

For centered standard fractional Brownian motion `B_{1/4}` and

\[
I(t)=\int_0^t B_{1/4}(s)\,ds,
\]

with the continuous fixed-barrier persistence convention

\[
\Pr\left\{\sup_{0\le t\le T}I(t)\le1\right\}=T^{-\theta_{2,1/4}+o(1)},
\]

this run proves, conditional only on already archived and explicitly cited PROB10-05/HARD7-05 inputs reconstructed below,

\[
\boxed{\theta_{2,1/4}>\frac{517}{3125}=0.16544}.\tag{0.1}
\]

Together with the retained source-valid upper bound `theta_{2,1/4}<=1/4`, the candidate repository bracket is

\[
\boxed{\frac{517}{3125}<\theta_{2,1/4}\le\frac14},
\qquad
\boxed{W_{1/4}=\frac{1057}{12500}=0.08456}.\tag{0.2}
\]

The incoming fleet lower endpoint was `3307/20000=0.16535`, so the source-level improvement is exactly

\[
\frac{517}{3125}-\frac{3307}{20000}=\frac9{100000}=0.00009.\tag{0.3}
\]

No finite path simulation is used. The lower-bound direction remains a continuous-path theorem because the continuous survival event is contained in every sampled survival event, so the continuum-to-grid error in this direction is exactly zero.

## 1. Consumed state, ownership, HARD7-05 history, and source status

This run read the controlling `operations/PROB10_2026-09-20.md`, root `POSTED.md`, canonical claim

`operations/claims/MOLCHAN-2025-THETA2H.md`,

the newest PROB10-05 report

`runs/prob10_2026-09-20/PROB10-05/2026-09-20T0058Z__cyclic_plackett_165350.md`

at creation commit

`bb65a20ebf36b4aa420fc63fbdef76456b5ac67a`,

and the relevant predecessor HARD7-05 report

`runs/hard7_2026-09-18/HARD7-05/2026-09-19T2250Z__triple_orthant_trace_164800.md`

at creation commit

`4f7031479268b0fb4cd2ffebbc6f82483e3001b2`.

The latter records the actual latest HARD7-05 target before the PROB10 refocus: the same Molchan integrated-fBM persistence problem, with a softened AR-edge comparator, exact four-cycle orthant representation and degree-18 quasimode. Therefore no new handoff or ownership transfer is needed in this run; PROB10-05 is the continuation of the same canonical owner rather than a target switch. The complementary `proofnet24/NM13-09/progress-persistence` route remains non-owning and was not edited.

The current source is G. Molchan, *Persistence probabilities for fractionally integrated fractional Brownian noise*, arXiv:2509.10265v11, repository-current revision recorded as 4 July 2026. The full-source read already archived by this track identifies Statement 1.2(a): throughout

\[
\Omega=\{(\alpha,H):\alpha+H>1,\ 0<H<1\},
\]

the relevant self-similar persistence exponent exists and equals that of the Lamperti-dual stationary process. Thus `(alpha,H)=(2,1/4)` lies in the proved existence regime. The same source explicitly reports that the old general formula `theta_{2,H}=H(1-H)` is false; this is source literature, not fleet work, and is not used as a conjecture here.

The external literature baseline retained from Molchan is

\[
\frac18\le\theta_{2,1/4}\le\frac14.\tag{1.1}
\]

The stronger lower endpoints in this repository are internal candidate advances, not numbers quoted from Molchan.

### Fresh bounded literature check

A fresh 20 September 2026 web/arXiv search for the exact Molchan title, `theta_{2,H}`, `H=1/4`, and integrated-fBM persistence recovered:

- Molchan, arXiv:2509.10265v11;
- Aurzada--Kilian, *Asymptotics of the Persistence Exponent of Integrated Fractional Brownian Motion and Fractionally Integrated Brownian Motion*, Theory Probab. Appl. 67 (2022), 77--88, which gives endpoint asymptotics rather than an exact `H=1/4` value;
- Aurzada--Helmer, arXiv:2608.17463 (18 August 2026), on fractional Levy fields on hyperbolic/Riemannian index sets, a different process;
- Molchan, arXiv:2608.26680 (27 August 2026), on multivariate-time fractional Brownian motion, again a different problem.

I found no later primary theorem in this bounded dated search determining the exact continuous `theta_{2,1/4}`. This is negative search evidence only, not a worldwide novelty certificate.

## 2. Inherited continuous-time comparison and spectral data

Freeze the existing comparator parameters

\[
r=\frac78,\qquad s=\frac{24861}{25000}.
\tag{2.1}
\]

The earlier HARD7-05/PROB10-05 chain proves an all-lag covariance domination of the sampled Lamperti source by the softened Gaussian edge comparator and therefore

\[
\theta_{2,1/4}\ge
\frac{-\log\lambda_1}{4\log(8/7)},\tag{2.2}
\]

where `lambda_1` is the Perron eigenvalue of the compact self-adjoint killed transfer operator `K=K_{r,s}`.

The direction is source-valid in continuous time. If `X` denotes the stationary Lamperti process and `Delta=4 log(8/7)`, then

\[
\{X(t)<0\ \forall 0\le t\le n\Delta\}
\subseteq
\{X(j\Delta)<0\ \forall j=1,\dots,n\}.\tag{2.3}
\]

Thus a sampled upper bound on survival yields a continuous upper bound on survival and hence a lower bound on the continuous persistence exponent, with no missed-crossing error.

The inherited normalized degree-18 quasimode `f` satisfies

\[
\mu=\langle f,Kf\rangle,
\qquad
\varepsilon^2=\|(K-\mu)f\|_2^2,
\]

with exact archived bounds

\[
\frac{9116948312}{10^{10}}<\mu<\frac{9116948313}{10^{10}},
\qquad
\varepsilon^2<\frac{47004495}{10^{11}}.\tag{2.4}
\]

The preceding PROB10-05 report also proves the cyclic four-cycle identity

\[
\operatorname{tr}(K^4)=\frac{P(b)}{1-r^4},\tag{2.5}
\]

where `P(c)` is the negative-orthant probability for the centered Gaussian correlation matrix

\[
\Sigma(c)=
\begin{pmatrix}
1&a&c&a\\
a&1&a&c\\
c&a&1&a\\
a&c&a&1
\end{pmatrix},\tag{2.6}
\]

with

\[
a=\frac{168557580}{170952323},
\qquad
b=\frac{167065920}{170952323}.\tag{2.7}
\]

At `c=a`, the equicorrelated comparison already gives

\[
\frac{P(a)}{1-r^4}<\frac{273011}{250000}=1.092044.\tag{2.8}
\]

The previous run used a single uniform Plackett derivative floor and obtained the weaker final cyclic trace cap `1.0862`. This run improves the same exact cyclic step rather than changing the source process, grid, or comparator.

## 3. Three materially different attacks

The mathematical idea was written before checker construction in

`artifacts/prob10_2026-09-20/PROB10-05/2026-09-20T0137Z__piecewise_plackett_quadrature_idea.md`

at commit

`60d75fe3399a81dee1df91af571d35b4b732ab11`,

and read back at that commit.

### Attack A — piecewise certified Plackett quadrature: SUCCESS

The exact derivative from the preceding report is

\[
P'(c)=\frac{1}{\pi\sqrt{1-c^2}}
\left[\frac14+\frac{\arcsin q(c)}{2\pi}\right],\tag{3.1}
\]

where

\[
q(c)=\frac{c(1+c)-2a^2}{1+c-2a^2}.\tag{3.2}
\]

Instead of a single worst-case derivative bound over `[b,a]`, use a 16-block lower Riemann sum with exact rational lower envelopes for both factors. This succeeds and supplies the source-level improvement.

### Attack B — exact circulant-mode reduction: promising but not promoted

The orthogonal coordinates

\[
A=(X_0+X_2)/\sqrt2,\quad B=(X_0-X_2)/\sqrt2,
\quad C=(X_1+X_3)/\sqrt2,\quad D=(X_1-X_3)/\sqrt2
\]

make `(B,D)` independent of `(A,C)` and of each other. The four-orthant event becomes

\[
A<-|B|,\qquad C<-|D|.
\]

This reduces the exact four-dimensional geometry to a two-dimensional correlated Gaussian integral against two folded-normal thresholds. It should recover more of the gap between the certified decrement below and the true cyclic orthant probability, but I do not yet have a short outward-rational enclosure of the resulting integral that improves Attack A without introducing substantial numerical certification machinery. No theorem is claimed from this route.

### Attack C — reverse continuous-time interpolation for the upper endpoint: blocked at barrier-rate stability

For a new upper bound on `theta`, one would need a lower bound on the continuous persistence probability in terms of a sampled event. A deterministic mesh/margin inclusion plus a Gaussian modulus estimate controls missed crossings on each cell, but over `n` cells the raw union bound produces an exponential-in-`n` cost unless the sampled persistence rate is stable under a shrinking negative margin. The missing lemma is a uniform barrier-shift estimate of the form

\[
\lim_{\eta\downarrow0}\limsup_{n\to\infty}
\frac1n\left|
\log\Pr\{X(j\Delta)\le-\eta,\ 1\le j\le n\}
-
\log\Pr\{X(j\Delta)\le0,\ 1\le j\le n\}
\right|=0.\tag{3.3}
\]

with quantitative control strong enough to pay the cellwise modulus error. This run does not prove (3.3), so the source upper endpoint remains `1/4`.

## 4. New analytic lemma: rational lower envelope for the Plackett derivative

The denominator in (3.2) is positive on `[b,a]`. Differentiating and clearing that positive squared denominator gives

\[
\operatorname{num} q'(c)=(1-c)^2+4c(1-a^2)>0,\tag{4.1}
\]

so `q` is strictly increasing. The exact endpoint value satisfies

\[
q(b)=-\frac{351986807334240}{961688306315689}>-\frac38.\tag{4.2}
\]

Define

\[
F(q):=\frac14+\frac{\arcsin q}{2\pi}.\tag{4.3}
\]

We need elementary rational lower bounds for `F`.

### Negative `q`

Write `q=-u`, with `0\le u\le3/8`. Then

\[
\arcsin u=\int_0^u\frac{dt}{\sqrt{1-t^2}}
\le \frac{u}{\sqrt{1-u^2}}
\le \frac{40}{37}u.\tag{4.4}
\]

The last inequality follows because

\[
1-u^2\ge\frac{55}{64}>\left(\frac{37}{40}\right)^2.\tag{4.5}
\]

Since `pi>3`, multiplying by the negative quantity `q` in the correct direction gives

\[
F(q)\ge\frac14+\frac{20q}{111}.\tag{4.6}
\]

The preceding report also proved uniformly on this range

\[
F(q)>\frac3{16},\tag{4.7}
\]

using `arcsin(3/8)<pi/8`. Therefore for `-3/8<=q<0`,

\[
F(q)>B(q):=
\max\left\{\frac3{16},\frac14+\frac{20q}{111}\right\}.\tag{4.8}
\]

### Nonnegative `q`

For `q>=0`, `arcsin q>=q`, and the classical `pi<22/7` gives

\[
F(q)\ge\frac14+\frac{7q}{44}=:B(q).\tag{4.9}
\]

The piecewise function `B(q)` is nondecreasing, agrees at `q=0`, and is a rigorous lower envelope for `F(q)` on the full range traversed by `q(c)`.

## 5. Sixteen-block certified lower quadrature

Let

\[
c_j=b+\frac{j}{16}(a-b),\qquad 0\le j\le15.\tag{5.1}
\]

Use the rational upper caps

\[
(s_0,\dots,s_{15})=
\left(
\frac{2121}{10000},\frac{419}{2000},\frac{207}{1000},\frac{511}{2500},
\frac{2017}{10000},\frac{1991}{10000},\frac{491}{2500},\frac{121}{625},
\frac{477}{2500},\frac{47}{250},\frac{463}{2500},\frac{911}{5000},
\frac{1793}{10000},\frac{881}{5000},\frac{433}{2500},\frac{17}{100}
\right).\tag{5.2}
\]

The exact checker verifies, for every `j`,

\[
s_j^2>1-c_j^2.\tag{5.3}
\]

For `c in [c_j,c_{j+1}]`, positivity of `c`, monotonicity of `q`, and monotonicity of `F` imply

\[
\frac1{\pi\sqrt{1-c^2}}F(q(c))
>
\frac7{22s_j}B(q(c_j)).\tag{5.4}
\]

Integrating blockwise gives

\[
P(a)-P(b)
>
\frac{a-b}{16}
\sum_{j=0}^{15}\frac7{22s_j}B(q(c_j)).\tag{5.5}
\]

Every term in (5.5) is rational. The executed exact checker evaluates the right side exactly and proves

\[
\frac{a-b}{16}
\sum_{j=0}^{15}\frac7{22s_j}B(q(c_j))
=0.003615359439736785\ldots
>\boxed{\frac{723}{200000}=0.003615}.\tag{5.6}
\]

The decimal is explanatory only; the strict comparison is exact integer/rational arithmetic.

This raises the certified cyclic decrement from the previous `0.00243` to `0.003615`, a mechanism gain of `0.001185` before the `1/(1-r^4)` trace normalization.

## 6. Improved fourth-trace cap

By (2.5), (2.8), and (5.6),

\[
\operatorname{tr}(K^4)
<\frac{273011}{250000}
-\frac{723/200000}{1-(7/8)^4}.\tag{6.1}
\]

Exact simplification gives

\[
\frac{273011}{250000}
-\frac{723/200000}{1-(7/8)^4}
=\frac{30603459}{28250000}
=1.0833082831858407\ldots
<\boxed{\frac{108331}{100000}=1.08331}.\tag{6.2}
\]

Thus the rigorous cyclic trace cap improves from the incoming `1.0862` to `1.08331`.

## 7. Spectral-tail separation and Temple contradiction at `theta*=0.16544`

Set

\[
\theta_*:=\frac{517}{3125}=0.16544.\tag{7.1}
\]

It suffices by (2.2) to prove

\[
\lambda_1<r^{4\theta_*}=r^{2068/3125}.\tag{7.2}
\]

Take

\[
x=\frac{457713}{500000}=0.915426.\tag{7.3}
\]

The exact checker verifies the integer-power inequality

\[
x^{3125}<r^{2068},\tag{7.4}
\]

hence `x<r^{2068/3125}`.

Assume for contradiction that `lambda_1>=r^{2068/3125}`. Then `lambda_1>x`. Since `K` is compact self-adjoint,

\[
\operatorname{tr}(K^4)=\sum_j\lambda_j^4.\tag{7.5}
\]

By (6.2), every non-Perron spectral point obeys

\[
|\lambda_j|^4
<\frac{108331}{100000}-x^4.\tag{7.6}
\]

Choose

\[
\beta=\frac{196421}{250000}=0.785684.\tag{7.7}
\]

The exact checker proves

\[
\beta^4-\left(\frac{108331}{100000}-x^4\right)
=4.651198905454953\ldots\times10^{-7}>0,\tag{7.8}
\]

so every non-Perron spectral point is at most `beta` and

\[
\beta<\mu<\lambda_1.\tag{7.9}
\]

For completeness, the residual inequality used here follows directly from the spectral measure `nu_f` of the normalized trial vector. On the support of `nu_f`,

\[
(\lambda-\lambda_1)(\lambda-\beta)\ge0,\tag{7.10}
\]

because it vanishes at `lambda_1` and both factors are nonpositive on the rest of the spectrum. Integrating and using `int lambda dnu_f=mu` gives

\[
\varepsilon^2
=\int(\lambda-\mu)^2d\nu_f(\lambda)
\ge(\lambda_1-\mu)(\mu-\beta).\tag{7.11}
\]

Under the contradictory assumption `lambda_1>x`, the archived interval (2.4) yields the conservative lower bound

\[
\varepsilon^2
>(x-\mu_{\rm hi})(\mu_{\rm lo}-\beta).\tag{7.12}
\]

Exact arithmetic gives

\[
(x-\mu_{\rm hi})(\mu_{\rm lo}-\beta)
-\frac{47004495}{10^{11}}
=
1.2271923442344\ldots\times10^{-7}>0,\tag{7.13}
\]

contradicting the inherited residual upper bound in (2.4). Hence (7.2) holds.

Finally,

\[
\theta_{2,1/4}
\ge\frac{-\log\lambda_1}{4\log(8/7)}
>
\frac{-\log r^{4\theta_*}}{4\log(8/7)}
=\theta_*,\tag{7.14}
\]

which proves (0.1).

## 8. Exact artifacts and actual tests

The pre-code idea checkpoint is

`artifacts/prob10_2026-09-20/PROB10-05/2026-09-20T0137Z__piecewise_plackett_quadrature_idea.md`

at commit `60d75fe3399a81dee1df91af571d35b4b732ab11`.

The final exact checker is

`artifacts/prob10_2026-09-20/PROB10-05/2026-09-20T0151Z__piecewise_plackett_165440_exact_check.py`

at commit `ccd06b39be3c9cd564081e5f233d56fc4991ce6d`.

Its executed output is

`artifacts/prob10_2026-09-20/PROB10-05/2026-09-20T0151Z__piecewise_plackett_165440_exact_check.out`

at commit `7bbc31e946c991a56fc9063e7bc3239c392644bb`.

Both final artifacts were read back at their returned commits. The output ends

`ALL_EXACT_CHECKS_PASS = True`.

The checker verifies: `q(b)>-3/8`; all 16 square-root caps; the exact 16-block rational sum; the strict `0.003615` decrement; the `1.08331` trace cap; the exact power comparison `x^3125<r^2068`; spectral-tail separation; the residual/Temple contradiction; and the source-metric decrease.

An earlier in-run feasibility checker targeting only `0.1654` is retained as immutable history under the same artifact directory, but it is superseded by the final `0.16544` checker above and is not the reported endpoint.

## 9. Before/after metrics and remaining full-scope gap

### Source-level metric

Before:

\[
\frac{3307}{20000}<\theta_{2,1/4}\le\frac14,
\qquad W_{1/4}=\frac{1693}{20000}=0.08465.
\]

After:

\[
\boxed{\frac{517}{3125}<\theta_{2,1/4}\le\frac14},
\qquad
\boxed{W_{1/4}=\frac{1057}{12500}=0.08456}.
\]

The width moves by exactly `9/100000`.

### Auxiliary mechanism progress

- certified cyclic Plackett decrement: `>0.00243 -> >0.003615`;
- rigorous fourth-trace cap: `1.0862 -> 1.08331`;
- no change to the source process, Hurst parameter, event, comparator `(r,s)`, continuous-time direction, or inherited quasimode.

### Unresolved full-scope gap

The exact value of `theta_{2,1/4}` remains unknown, with a certified candidate gap `0.08456`. The source's full family `theta_{2,H}` is much broader and remains open. The present progress moves only the lower endpoint at `H=1/4`; it does not improve the `1/4` upper endpoint. A reverse grid-to-continuum theorem of the barrier-rate-stability type (3.3), a sharper exact cyclic orthant evaluation, or a substantially stronger operator spectral certificate is still required for a larger advance.

No closure, novelty certification, or independent-audit completion is claimed.