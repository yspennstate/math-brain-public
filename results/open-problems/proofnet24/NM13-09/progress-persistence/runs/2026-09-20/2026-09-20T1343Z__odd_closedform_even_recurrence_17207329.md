Model actually run: **GPT-5.6 Sol**. Reasoning-effort metadata: **UNVERIFIED**.

# T05 — exact odd-Hermite summation + degree-2000 even recurrence at the corrected `r=22/25` comparator

**Status: PARTIAL / complete candidate bound pending later independent review.** The exact exponent is not determined. The old proposal `theta_{2,H}=H(1-H)` is not assumed or used.

## 1. Short handoff and frozen source statement

LIVE20 assigns NM13-09 to T05. The previous NM13-09 run repaired the four-cycle trace normalization for the useful `r=22/25` soft comparator and established the complete internal candidate

\[
\frac{3441457}{20000000}=0.17207285<\theta_{2,1/4}\le \frac14.
\]

That correction remains in force. In particular, I still do **not** use the neighboring PROB10 endpoint claims `0.172052` and `0.172096247...` as proved baselines, because their theorem-deciding four-cycle correlations omit the normalized-cycle variance factor

\[
G_0=\frac{1+r^4}{1-r^4}.
\]

Their useful covariance and direct one-/two-step moment data remain preserved where unaffected.

The source process is standard fBM at `H=1/4`,

\[
\mathbb E B_{1/4}(t)B_{1/4}(s)=\frac12\bigl(t^{1/2}+s^{1/2}-|t-s|^{1/2}\bigr),
\]

with ordinary integrated fBM

\[
I(t)=\int_0^t B_{1/4}(u)\,du.
\]

The exact source event is the **continuous** one-sided event

\[
\Pr\{I(t)<1\ \forall\,0<t<T\}=T^{-\theta_{2,1/4}+o(1)}.
\tag{1.1}
\]

Direct integration gives `Var I(1)=2/5`. Since `I` is self-similar with index `5/4`, the unit-variance Lamperti dual is

\[
X(\tau)=\sqrt{\frac52}\,e^{-5\tau/4}I(e^\tau).
\tag{1.2}
\]

Molchan, arXiv:2509.10265v11 (revised 4 July 2026), was re-inspected directly. Its Statement 1.2(a) states that in the interior parameter domain the persistence exponents of the self-similar process and its stationary dual **exist and are identical**. The same paper says the one-sided `alpha=2`, `H!=1/2` values remain unsolved and reports the former `H(1-H)` hypothesis refuted. Thus no separate existence theorem is required at `(alpha,H)=(2,1/4)`.

The primary-source published bracket remains

\[
\boxed{\frac18\le\theta_{2,1/4}\le\frac14}.
\tag{1.3}
\]

A bounded fresh later-primary check also inspected Molchan, *Fractional Brownian motion with multivariate time: persistence exponents*, arXiv:2608.26680 (submitted 27 August 2026), and Aurzada--Helmer, *Persistence probabilities of fractional Levy fields indexed by hyperbolic space and other Riemannian manifolds*, arXiv:2608.17463 (submitted 18 August 2026). The retrieved statements concern different processes/index sets and do not determine (1.1). This is bounded negative evidence only, not a worldwide novelty certificate.

## 2. Source-level before/after

The strongest valid internal candidate entering this run was

\[
L_{\rm in}=\frac{3441457}{20000000}=0.17207285.
\]

This run proves the stronger complete candidate

\[
\boxed{\theta_{2,1/4}>\theta_*:=\frac{17207329}{10^8}=0.17207329.}
\tag{2.1}
\]

Therefore the internal candidate bracket moves

\[
0.17207285<\theta_{2,1/4}\le\frac14
\quad\longrightarrow\quad
\boxed{0.17207329<\theta_{2,1/4}\le\frac14},
\]

with exact lower-endpoint gain

\[
\theta_*-L_{\rm in}=\frac{44}{10^8}=\frac{11}{25,000,000}=4.4\times10^{-7}.
\tag{2.2}
\]

The candidate bracket width moves

\[
0.07792715\longrightarrow
\boxed{\frac{7792671}{10^8}=0.07792671}.
\tag{2.3}
\]

This is a self-certified repository candidate, not a published theorem and not an exact determination.

## 3. Continuous-time covariance comparison: exact all-lag domination and zero interpolation loss

Writing `u=e^{-|t|/4}`, the Lamperti covariance is

\[
R(u)=\frac{-2u^{10}+5u^6+5u^4+2(1-u^4)^{5/2}-2}{6u^5}.
\tag{3.1}
\]

Retain the corrected soft comparator parameters

\[
r=\frac{22}{25},\qquad c=\frac{936901}{10^6},\qquad s=\frac{936901}{940000},
\qquad c=s\frac{1+r}{2}.
\tag{3.2}
\]

Let `(U_j)` be stationary standard Gaussian AR(1) with correlation `r`, `(E_j)` iid standard Gaussian independent of it, and

\[
Y_j=\frac{U_j+U_{j-1}}{\sqrt{2(1+r)}},\qquad
Z_j=\sqrt{s}\,Y_j+\sqrt{1-s}\,E_j.
\tag{3.3}
\]

Then

\[
\operatorname{Cov}(Z_0,Z_k)=c r^{k-1}\qquad(k\ge1).
\]

The exact checker re-proves

\[
\boxed{R(r^k)<c r^{k-1}\qquad(k\ge1).}
\tag{3.4}
\]

For `k=1,2`, after isolating the radical in (3.1), the exact rational squared margins are positive; their decimal displays are

`1.334296986263307e-4`, `2.3302146180526656e-7`.

For `k>=3`, Taylor's theorem gives

\[
(1-z)^{5/2}\le1-\frac52z+\frac{15}{8}z^2,
\]

hence

\[
R(u)\le \frac56u+\frac58u^3-\frac13u^5.
\]

After division by `r^{k-1}`, the right side is maximal at `k=3`; the exact endpoint margin is

`c-r(5/6+(5/8)r^6-(1/3)r^12)=0.011408957976493094...>0`.

Set

\[
\Delta=-4\log r=4\log\frac{25}{22}.
\tag{3.5}
\]

By Slepian, sampled survival of `X` is bounded by sampled survival of `Z`. More importantly, continuity gives the literal inclusion

\[
\{X(t)<0\ \forall\,0\le t\le n\Delta\}
\subseteq
\{X(j\Delta)<0,\ 1\le j\le n\}.
\tag{3.6}
\]

Thus the continuum-to-grid interpolation/missed-crossing loss is **exactly zero in the lower-bound direction used here**. No reverse sampled-to-continuous implication is claimed; in particular no new upper endpoint is inferred from grid data.

For the compact self-adjoint killed transfer operator `K` of this comparator, with Perron eigenvalue `lambda_1`, the inherited comparison gives

\[
\theta_{2,1/4}\ge\frac{-\log\lambda_1}{4\log(25/22)}.
\tag{3.7}
\]

## 4. Correct four-cycle scale retained

Under the normalized four-cycle trace law of the AR kernel,

\[
G_0=\frac{1+r^4}{1-r^4}=\frac{624881}{156369}=3.9961948979\ldots .
\]

After multiplying the AR-cycle `v,g,h` quantities by `G_0` **before** adding the independent softening noise, the exact corrected correlations are

\[
\rho_a=\frac{25975580225}{26207003696}=0.991169403656\ldots,
\]

\[
\rho_o=\frac{6441194375}{6551750924}=0.983125648352\ldots .
\tag{4.1}
\]

Put

\[
q=\frac{2\rho_a}{1+\rho_o}=\frac{23422525}{23431822}=0.999603231878\ldots,
\]

\[
A=\frac{1+\rho_o}{1-\rho_o}=117.5230722786\ldots,
\qquad h=1+A.
\tag{4.2}
\]

The normalized four-negative probability is

\[
p_4=\mathbb E[g_A(G_0)g_A(G_1)],
\]

where `(G_0,G_1)` are standard normal with correlation `q` and

\[
g_A(z)=\mathbf 1_{\{z>0\}}\bigl(2\Phi(\sqrt A\,z)-1\bigr).
\tag{4.3}
\]

Writing

\[
d_n=\mathbb E[g_A(G)\operatorname{He}_n(G)],\qquad
w_n=\frac{d_n^2}{n!},
\]

Mehler gives

\[
p_4=m^2+\sum_{n\ge1}q^n w_n,
\qquad
m=\frac{\arctan\sqrt A}{\pi}.
\tag{4.4}
\]

The previous scale-correct run bounded this series by brute-force exact Hermite coefficients through degree 500 plus a Parseval tail and obtained

\[
\operatorname{tr}(K^4)<1.143652.
\tag{4.5}
\]

The bottleneck was `q` extremely close to one, making a single undifferentiated Parseval tail converge slowly.

## 5. New mechanism I: sum **all odd Hermite modes exactly**

Define

\[
J_m(h)=\int_0^\infty \operatorname{He}_m(z)e^{-hz^2/2}\,dz.
\]

From the Hermite generating function,

\[
\sum_{m\ge0}\frac{J_m(h)}{m!}t^m
=\sqrt{\frac{\pi}{2h}}\,e^{-A t^2/(2h)}
\left(1+\operatorname{erf}\frac{t}{\sqrt{2h}}\right).
\tag{5.1}
\]

Since

\[
d_n=\frac{\sqrt A}{\pi}J_{n-1}(h),
\tag{5.2}
\]

the even-index `J_{2j}` term comes only from the even exponential factor in (5.1):

\[
J_{2j}(h)=\sqrt{\frac{\pi}{2h}}\,
\frac{(2j)!}{j!}\left(-\frac{A}{2h}\right)^j.
\tag{5.3}
\]

Therefore

\[
w_{2j+1}
=\frac{A}{2\pi h}\,
\frac{\binom{2j}{j}}{2j+1}
\left(\frac{A}{2h}\right)^{2j}.
\tag{5.4}
\]

Using

\[
\frac{\arcsin(2x)}{2x}
=\sum_{j\ge0}\frac{\binom{2j}{j}}{2j+1}x^{2j},
\]

we obtain the exact infinite odd-mode sum

\[
\sum_{j\ge0}q^{2j+1}w_{2j+1}
=\frac{1}{2\pi}\arcsin\left(\frac{qA}{h}\right).
\tag{5.5}
\]

But

\[
\frac{qA}{h}=\rho_a
\]

**exactly**, so

\[
\boxed{
\sum_{j\ge0}q^{2j+1}w_{2j+1}
=\frac{\arcsin\rho_a}{2\pi}.
}
\tag{5.6}
\]

This removes the entire odd Hermite tail rather than bounding it by one common `q^M` factor.

## 6. New mechanism II: positive exact recurrence for the even modes

The remaining modes can also be generated without expanding enormous Hermite polynomials. Integration by parts and

\[
\operatorname{He}_m(z)=z\operatorname{He}_{m-1}(z)-(m-1)\operatorname{He}_{m-2}(z)
\]

give

\[
J_m(h)=\frac{\operatorname{He}_{m-1}(0)}{h}
-(m-1)\frac{A}{h}J_{m-2}(h).
\tag{6.1}
\]

For `j>=1`, let

\[
L_j:=J_{2j-1}(h),\qquad D_j:=(2j-3)!!,
\qquad y_j:=(-1)^{j-1}\frac{L_j}{D_j}.
\]

Since `He_{2j-2}(0)=(-1)^{j-1}D_j`, (6.1) becomes the **positive rational recurrence**

\[
y_1=\frac1h,
\qquad
y_j=\frac1h+\frac{2j-2}{2j-3}\frac{A}{h}y_{j-1}.
\tag{6.2}
\]

Define

\[
C_j:=\frac{D_j^2}{(2j)!}.
\]

Then

\[
C_1=\frac12,
\qquad
\frac{C_j}{C_{j-1}}
=\frac{(2j-3)^2}{(2j)(2j-1)},
\tag{6.3}
\]

and the even Hermite weights are simply

\[
\boxed{w_{2j}=\frac{A}{\pi^2}C_j y_j^2.}
\tag{6.4}
\]

All quantities in (6.2)--(6.4), except the common factor `pi^{-2}`, are exact rationals. This makes thousands of modes certifiable without symbolic Hermite expansion.

There is also a parity-exact Parseval remainder. Because `g_A(z)g_A(-z)=0` a.e., its even and odd parts have equal squared norm:

\[
\|g_{\rm even}\|_2^2=\|g_{\rm odd}\|_2^2=\frac{e_2}{2},
\]

where

\[
e_2=\mathbb E g_A(G)^2
=\frac1\pi\arctan\frac{A}{\sqrt{1+2A}}.
\tag{6.5}
\]

The constant mode `m` is even, so

\[
\sum_{j\ge1}w_{2j}=\frac{e_2}{2}-m^2.
\tag{6.6}
\]

After computing exactly the first `J=1000` even modes (`n=2,...,2000`), all omitted even modes satisfy `q^{2j}<=q^{2002}`. Hence

\[
\begin{aligned}
p_4\le {}&m^2+\frac{\arcsin\rho_a}{2\pi}
+\sum_{j=1}^{1000}q^{2j}w_{2j}\\
&+q^{2002}\left(
\frac{e_2}{2}-m^2-\sum_{j=1}^{1000}w_{2j}
\right).
\end{aligned}
\tag{6.7}
\]

All square roots, `pi`, `atan` and `asin` terms in the checker are enclosed outward by exact rational intervals: Machin's formula for `pi`, integer square-root brackets at denominator `10^90`, alternating `atan` series, and `asin x=atan(x/sqrt(1-x^2))`.

The executed exact arithmetic gives

\[
p_4<0.45775980172253833\ldots
\]

and therefore

\[
\boxed{
\operatorname{tr}(K^4)<1.1435285929299703\ldots
<\frac{1143529}{10^6}=1.143529.
}
\tag{6.8}
\]

Compared with (4.5), the clean certified trace cap improves by

\[
1.143652-1.143529=0.000123.
\tag{6.9}
\]

This is the demonstrated mechanism gain of the run.

### Failed route retained

I first tested whether the preceding neighboring **even-block HGR** idea survives the corrected four-cycle scale. With the corrected `(rho_a,rho_o)`, its numerical trace upper is about `1.144474`, which is worse than the existing scale-correct `1.143652`; it was therefore not promoted. The exact odd-sum/even-recurrence route above is materially different and succeeds.

## 7. Exact Kato--Temple synthesis

The unaffected degree-56 trial vector for this same `r=22/25` operator certifies

\[
\frac{9155053441}{10^{10}}<\mu<\frac{9155053442}{10^{10}},
\qquad
\varepsilon^2<\frac{270154}{10^{10}}.
\tag{7.1}
\]

Choose

\[
\theta_*=\frac{17207329}{10^8},
\quad
x=\frac{1831545863}{2\cdot10^9}=0.9157729315,
\quad
\beta=\frac{8145459}{10^7}=0.8145459.
\tag{7.2}
\]

Assume for contradiction that `lambda_1>=r^{4 theta_*}>x`. From (6.8), every non-Perron eigenvalue obeys

\[
|\lambda_j|^4<1.143529-x^4<\beta^4.
\]

The exact rational trace-separation margin is positive, with decimal display

`5.297253340176426e-7`.

Since `mu_->beta`, Kato--Temple gives

\[
\lambda_1\le\mu+\frac{\varepsilon^2}{\mu-\beta}.
\]

A sufficient outward-rational condition for this to be `<x` is

\[
(x-\mu_+)(\mu_- -\beta)>\varepsilon_+^2.
\tag{7.3}
\]

The exact margin is positive, with decimal display

`6.505621993e-11`.

Finally, `x<r^{4 theta_*}` is certified without floating logarithms from

\[
\operatorname{artanh}z
=\sum_{k=0}^m\frac{z^{2k+1}}{2k+1}+R_m,
\qquad
0<R_m<\frac{z^{2m+3}}{(2m+3)(1-z^2)},
\]

using

\[
-\log x=2\operatorname{artanh}\frac{1-x}{1+x},
\qquad
-\log r=2\operatorname{artanh}\frac{1-r}{1+r}
\]

with `m=10`. The exact lower-minus-upper margin for

\[
-\log x>4\theta_*(-\log r)
\]

is positive; its decimal display is

`5.918528110859414e-10`.

Thus `lambda_1<x<r^{4 theta_*}`, and (3.7) proves (2.1).

## 8. Essential executed checker core and output

The theorem-deciding new recurrence/tail core that was actually executed is:

```python
# q,A,h,rho_adj are the exact rationals from the corrected four-cycle.
# All transcendental quantities below use outward rational pi/sqrt/atan intervals.

# all odd modes exactly
sq = sqrt_bounds(1-rho_adj*rho_adj)
asin_arg=(rho_adj/sq[1],rho_adj/sq[0])
asinI=atan_pos_interval(*asin_arg)
oddI=(asinI[0]/(2*PI[1]),asinI[1]/(2*PI[0]))
assert q*A/h == rho_adj

# even modes n=2,...,2000 by rational recurrence
JMAX=1000
y=1/h
C=F(1,2)
q2=q*q
qpow=q2
Sq=F(0); Sw=F(0)
for j in range(1,JMAX+1):
    if j>1:
        y = 1/h + F(2*j-2,2*j-3)*(A/h)*y
        C *= F((2*j-3)**2,(2*j)*(2*j-1))
        qpow *= q2
    coeff=C*y*y
    Sq += qpow*coeff
    Sw += coeff

even_q_hi=A*Sq/(PI[0]*PI[0])
even_w_lo=A*Sw/(PI[1]*PI[1])
resid_even_hi=e2I[1]/2-m2I[0]-even_w_lo
qnext=q**(2*JMAX+2)
p_upper=m2I[1]+oddI[1]+even_q_hi+qnext*resid_even_hi
trace_upper=p_upper/(1-r**4)
trace_cap=F(1143529,10**6)
assert trace_upper<trace_cap

mu_lo=F(9155053441,10_000_000_000)
mu_hi=F(9155053442,10_000_000_000)
eps2_hi=F(270154,10_000_000_000)
theta=F(17207329,100000000)
x=F(1831545863,2000000000)
beta=F(8145459,10000000)
assert beta**4-(trace_cap-x**4)>0
assert (x-mu_hi)*(mu_lo-beta)-eps2_hi>0
```

Executed output:

```text
r,c,s = 22/25 936901/1000000 936901/940000
covariance k=1,2 squared margins = [0.0001334296986263307, 2.3302146180526656e-07]
covariance tail c-margin = 0.011408957976493094
G0 = 3.9961948979657094
rho_adj,rho_opp,q,A = 0.9911694036569575 0.9831256483522571 0.9996032318784258 117.52307227860378
JMAX / max even Hermite degree = 1000 2000
odd all-modes contribution upper = 0.22883344133392064
finite even q-sum interval = 0.00733106616315595 0.00733106616315595
even residual-mass interval = 3.8410134121620467e-05 3.8410134121620467e-05
q_next = 0.4518127732418572
p4 upper = 0.45775980172253833
trace upper = 1.1435285929299703
trace cap/margin = 1.143529 4.070700296025376e-07
theta,x,beta = 0.17207329 0.9157729315 0.8145459
trace separation margin = 5.297253340176426e-07
Temple margin = 6.505621993e-11
log/atanh margin = 5.918528110859414e-10
incoming/new/gain = 0.17207285 0.17207329 4.4e-07
new width = 0.07792671
ALL_EXACT_CHECKS_PASS = True
```

## 9. Status, residual obstruction, and next attack

**Source-level gain:** internal candidate lower endpoint `0.17207285 -> 0.17207329`, width `0.07792715 -> 0.07792671`. The external published bracket remains `1/8 <= theta <= 1/4`.

**Demonstrated mechanism gain:** the fourth-trace cap improves `1.143652 -> 1.143529` by summing all odd Hermite modes in closed form and certifying the first 1000 nonconstant even modes through a positive rational recurrence plus parity-exact Parseval remainder. This directly tightens the Kato--Temple spectral separation for the same continuous-time covariance comparator.

**Continuum control:** the all-lag covariance comparison is exact and the continuum-to-grid interpolation loss is exactly zero in the direction used. No grid-only exponent is treated as the continuous answer.

**Failure preserved:** corrected-scale even-block HGR is weaker and was abandoned.

**Residual obstruction:** with the present degree-56 Perron residual, the spectral/Kato--Temple step is again the dominant bottleneck. Further extension of the even recurrence beyond degree 2000 has diminishing leverage. A higher-degree same-operator quasimode or a genuine two-mode/min-max separation is the next materially different high-leverage route.

The source metric moved in this run, so the consecutive-unchanged substantive-run count resets to `0`; no forced T01--T10 scope switch is triggered.

## ledger_delta

```yaml
ledger_delta:
  target: T05 integrated-fBM persistence at H=1/4
  source_event: "P{I(t)<1 for every 0<t<T}=T^{-theta_{2,1/4}+o(1)}"
  published_source_bracket_before: [0.125, 0.25]
  published_source_bracket_after: [0.125, 0.25]
  internal_valid_before_lower: 0.17207285
  internal_candidate_after_lower: 0.17207329
  exact_gain: 11/25000000
  internal_width_before: 0.07792715
  internal_width_after: 0.07792671
  comparator_r: 22/25
  covariance_all_lag: "R(r^k)<c r^(k-1), k>=1"
  continuum_interpolation_loss_used_direction: 0
  four_cycle_scale_G0: 624881/156369
  old_scale_correct_trace_cap: 1.143652
  new_trace_cap: 1.143529
  odd_modes: exact_closed_form_all_orders
  even_modes_certified_through_degree: 2000
  theta_candidate: 17207329/100000000
  status: PARTIAL_COMPLETE_CANDIDATE_PENDING_INDEPENDENT_REVIEW
  failed_route: corrected_scale_even_block_HGR_weaker
  unchanged_substantive_run_count_after: 0
  runtime_model: GPT-5.6-Sol
  runtime_reasoning_effort: UNVERIFIED
```
