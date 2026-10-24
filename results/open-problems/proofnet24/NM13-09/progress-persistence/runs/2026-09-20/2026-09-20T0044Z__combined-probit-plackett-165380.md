Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — not GPT-6 maximum. T05 source metric MOVED: repository candidate `3307/20000 < theta_{2,1/4} <= 1/4` (width `1693/20000`) -> `8269/50000 < theta_{2,1/4} <= 1/4` (width `4231/50000`); demonstrated mechanism gain: cyclic fourth-trace cap `1.0862 -> 1.085231`, while the continuum-to-grid loss in this lower-bound direction remains exactly zero.**

# NM13-09 T05 progress — combine the degree-4 probit resolvent bound with the exact cyclic Plackett decrement

**Status: PARTIAL / CANDIDATE source-level improvement pending later independent review.** The exact exponent remains open. This run gives a complete internal argument, conditional only on the already archived exact degree-18 quasimode certificate for the same comparator parameters,

\[
\boxed{\theta_{2,1/4}>\frac{8269}{50000}=0.16538}.\tag{0.1}
\]

Together with the retained source-valid upper bound,

\[
\boxed{\frac{8269}{50000}<\theta_{2,1/4}\le \frac14},
\qquad
\boxed{W_{1/4}=\frac{4231}{50000}=0.08462}.\tag{0.2}
\]

The strongest current repository candidate at the start of this run was the newer PROB10-05 cyclic-Plackett report

`runs/prob10_2026-09-20/PROB10-05/2026-09-20T0058Z__cyclic_plackett_165350.md`,

which had already superseded this worker's earlier `0.1652` bound and established the candidate lower endpoint

\[
\theta_{2,1/4}>\frac{3307}{20000}=0.16535,
\qquad W_{1/4}=\frac{1693}{20000}=0.08465.
\tag{0.3}
\]

Thus the source-level lower endpoint increases by exactly `3/100000`, and the bracket width decreases by exactly the same amount.

## 1. Short handoff and exact source statement

`operations/PROGRESS20_2026-09-20.md` assigns LIVE20 slot NM09 to T05 and instructs this worker to develop covariance/comparison bounds for the continuous integrated-fBM persistence problem. Canonical parent ownership remains with the existing Molchan/PROB10-05 line; this report is complementary mathematics and does not overwrite that ownership or any peer file.

Let `B_H` be centered standard fractional Brownian motion,

\[
\mathbb E B_H(t)B_H(s)
=\frac12\left(t^{2H}+s^{2H}-|t-s|^{2H}\right),
\]

freeze `H=1/4`, and define the once-integrated process

\[
I(t)=\int_0^t B_{1/4}(u)\,du.
\tag{1.1}
\]

The exact continuous-time source event and normalization are

\[
p(T)=\Pr\{I(t)\le 1\text{ for every }0\le t\le T\},
\qquad
p(T)=T^{-\theta_{2,1/4}+o(1)}.
\tag{1.2}
\]

No discrete-grid probability is being declared to be the source persistence probability.

For this normalization,

\[
\operatorname{Var}I(1)=\frac25,
\qquad
X(\tau)=\sqrt{\frac52}\,e^{-5\tau/4}I(e^\tau)
\tag{1.3}
\]

is the unit-variance stationary Lamperti dual.

### Source-level literature baseline

I inspected the current Molchan PDF, arXiv:2509.10265, rather than using only the abstract. The paper states that the one-sided values `theta_{2,H}` for `H != 1/2` remain unsolved, gives the source bounds which at `H=1/4` imply

\[
\frac18\le \theta_{2,1/4}\le\frac14,
\tag{1.4}
\]

and Statement 1.2(a) states existence and equality of the self-similar and Lamperti-dual persistence exponents throughout `Omega={alpha+H>1,0<H<1}`. Hence exponent existence needed in (1.2) is already a source theorem at `(alpha,H)=(2,1/4)`. The current revision also establishes the symmetry that refutes the old general proposal `theta_{2,H}=H(1-H)`; this run neither assumes nor attempts to restore that formula.

A bounded 20 September 2026 primary-source search for later work recovered, among others, Li-Xin Zhang's 2026 Chung/small-ball work on integrated fractional processes, Molchan's August 2026 paper on multivariate-time fBM, and Aurzada--Helmer's 2026 fractional-Levy-field persistence work. These concern different observables or different processes and do not state an exact continuous one-sided value at integrated-fBM `H=1/4`. This is a dated bounded search, not a worldwide novelty certificate.

## 2. Continuous source-to-grid comparison: exact zero interpolation loss in the direction used

At `H=1/4`, writing `u=e^{-|\tau|/4}`, the Lamperti covariance is

\[
R(u)=
\frac{-2u^{10}+5u^6+5u^4+2(1-u^4)^{5/2}-2}{6u^5}.
\tag{2.1}
\]

Use the existing comparator parameters

\[
r=\frac78,
\qquad s=\frac{24861}{25000},
\qquad c=s\frac{1+r}{2}=\frac{74583}{80000}.
\tag{2.2}
\]

If `(U_j)` is standard stationary Gaussian AR(1) with correlation `r`, `(E_j)` is iid standard Gaussian independent of it, and

\[
Y_j=\frac{U_j+U_{j-1}}{\sqrt{2(1+r)}},
\qquad
Z_j=\sqrt{s}\,Y_j+\sqrt{1-s}\,E_j,
\tag{2.3}
\]

then

\[
\operatorname{Cov}(Z_0,Z_k)=c r^{k-1},\qquad k\ge1.
\tag{2.4}
\]

The all-lag covariance estimate used by the fleet is

\[
\boxed{R(r^k)<c r^{k-1}\quad(k\ge1).}\tag{2.5}
\]

I re-executed the exact check in this run. For `k=1,...,5`, radical isolation reduces (2.5) to rational inequalities with positive squared margins

`0.000141657229..., 0.022728511900..., 0.116553907766..., 0.101252472038..., 0.062535279443...`.

For `k>=6`, `u=r^k<1/2`. With `z=u^2`, the identity

\[
P(z)^2-4(1+z)^2(1-z^2)^3=z^3Q(z),
\]

\[
P(z)=2+2z-3z^2-2z^3-2z^4,
\qquad
Q(z)=8z^5+16z^4+8z^3-20z^2-7z+4
\]

and `Q(z)>=4-7z-20z^2>=1` on `0<=z<=1/4` imply `R(u)<=u`; since `c/r>1`, this gives (2.5) for all remaining lags.

Set

\[
\Delta=-4\log r=4\log(8/7).
\tag{2.6}
\]

For the zero-level stationary event

\[
A_{n\Delta}=\{X(t)<0\text{ for all }0\le t\le n\Delta\}
\]

and its grid event `G_n={X(j Delta)<0, j=1,...,n}`, there is the deterministic inclusion

\[
A_{n\Delta}\subseteq G_n.
\tag{2.7}
\]

Therefore the continuum interpolation error in the only direction used here is **exactly zero**. By (2.5) and Slepian,

\[
\Pr(A_{n\Delta})\le \Pr(G_n)
\le \Pr(Z_1<0,\ldots,Z_n<0).
\tag{2.8}
\]

If `lambda_1` is the Perron eigenvalue of the inherited compact self-adjoint killed transfer operator `K=K_{r,s}`, then

\[
\Pr(Z_1<0,\ldots,Z_n<0)\le \lambda_1^n,
\qquad
\theta_{2,1/4}\ge\frac{-\log\lambda_1}{4\log(8/7)}.
\tag{2.9}
\]

A reverse grid-to-continuum transfer would be needed for a new upper bound on `theta`; no such reverse interpolation claim is made here.

## 3. The new mechanism: sharpen the equicorrelated orthant and then keep the cyclic Plackett gain

The exact four-cycle trace has the form

\[
\operatorname{tr}(K^4)=\frac{P_b}{1-r^4},
\tag{3.1}
\]

where `P_b` is the negative orthant probability of the cyclic Gaussian correlation matrix

\[
\Sigma(b)=
\begin{pmatrix}
1&a&b&a\\
a&1&a&b\\
b&a&1&a\\
a&b&a&1
\end{pmatrix},
\tag{3.2}
\]

with

\[
a=\frac{168557580}{170952323},
\qquad
b=\frac{167065920}{170952323}<a.
\tag{3.3}
\]

Two independently obtained improvements existed on current master but had not yet been composed:

1. This worker had sharpened the **equicorrelated** endpoint `P_a` by improving the probit product envelope.
2. PROB10-05 had quantified the **cyclic decrement** `P_a-P_b` using a Plackett interpolation.

This run composes them and also improves the probit integration one step further.

### Lemma 3.1 — degree-4 resolvent majorant

For every `y>=0`,

\[
\boxed{\frac1{1+y}\le 1-y+y^2-y^3+y^4.}\tag{3.4}
\]

Indeed, multiplying by `1+y` gives `1+y^5`, so the difference from `1/(1+y)` is exactly `y^5/(1+y)>=0`.

From the previously proved pointwise probit inequality

\[
\Phi(x)\Phi(-x)
\le \frac{e^{-x^2/2}}{4\sqrt{1+x^2/5}},
\tag{3.5}
\]

let the equicorrelated one-factor representation have correlation `rho=a`, let

\[
C^2=\frac{\rho}{1-\rho},
\qquad U=\Phi(-CZ),
\qquad Q=U(1-U),
\]

for `Z~N(0,1)`. Then

\[
Q^2\le \frac{e^{-C^2Z^2}}{16(1+C^2Z^2/5)}.
\tag{3.6}
\]

Put

\[
A_0=1+2C^2=\frac{1+\rho}{1-\rho},
\qquad
q=\frac{C^2/5}{A_0}=\frac{\rho}{5(1+\rho)}.
\tag{3.7}
\]

The weighted Gaussian moments are exact:

\[
\mathbb E\left[e^{-C^2Z^2}Z^{2k}\right]
=(2k-1)!!\,A_0^{-k-1/2}.
\tag{3.8}
\]

Applying (3.4) term-by-term to (3.6) therefore gives

\[
\mathbb E Q^2
\le \frac1{16}A_0^{-1/2}
\left(1-q+3q^2-15q^3+105q^4\right).
\tag{3.9}
\]

By symmetry of `U` and the bivariate Gaussian sign identity,

\[
P_a=\mathbb E U^4
=\frac{\arcsin\rho}{\pi}+\mathbb E Q^2.
\tag{3.10}
\]

Using outward rational enclosures for `pi`, `asin(rho)` and the square root, the exact checker below proves

\[
\boxed{\frac{P_a}{1-r^4}<1.091102175027}.\tag{3.11}
\]

The previous quadratic majorant gave `1.091158975644...`; thus (3.9) is a genuine mechanism improvement. The next even truncation is not better here: the alternating moment expansion is already entering its asymptotic regime, so degree 4 is the useful stopping point.

### Lemma 3.2 — keep the exact cyclic decrement

Along the positive-definite path `Sigma(c)`, `b<=c<=a`, the PROB10-05 Plackett calculation gives

\[
P'(c)=\frac1{\pi\sqrt{1-c^2}}
\left[\frac14+\frac1{2\pi}\arcsin q(c)\right],
\qquad
q(c)=\frac{c(1+c)-2a^2}{1+c-2a^2}.
\tag{3.12}
\]

The exact endpoint check gives `q(b)>-3/8`, and monotonicity of `q` gives this over the entire path. Since `asin(3/8)<pi/8`, `pi<22/7`, and `sqrt(1-b^2)<213/1000`, integration yields

\[
P_a-P_b>
\frac{3(a-b)}{16(22/7)(213/1000)}
>\frac{243}{100000}.
\tag{3.13}
\]

This run independently re-executed all rational endpoint inequalities in (3.13).

Combining (3.11) and (3.13),

\[
\operatorname{tr}(K^4)
=\frac{P_b}{1-r^4}
<1.091102175027
-\frac{243/100000}{1-(7/8)^4}
<1.085230034.
\tag{3.14}
\]

Hence the simple certified cap

\[
\boxed{\operatorname{tr}(K^4)<\frac{1085231}{10^6}=1.085231}.\tag{3.15}
\]

The previous current-master cyclic cap was `1.0862`, so (3.15) is the demonstrated mechanism gain of this run.

## 4. Temple step at `theta_*=8269/50000`

The inherited exact degree-18 quasimode certificate, at the same `(r,s)`, gives for normalized `f`

\[
\mu=\langle f,Kf\rangle,
\qquad
\varepsilon^2=\|(K-\mu)f\|_2^2,
\]

\[
\frac{9116948312}{10^{10}}<\mu<\frac{9116948313}{10^{10}},
\qquad
\varepsilon^2<\frac{47004495}{10^{11}}.
\tag{4.1}
\]

Set

\[
\theta_*=\frac{8269}{50000},
\qquad
x=\frac{9154553}{10^7},
\qquad
\beta=\frac{393313}{500000}=0.786626.
\tag{4.2}
\]

Since `4 theta_*=8269/12500`, the exact integer-power check

\[
x^{12500}<r^{8269}
\tag{4.3}
\]

proves `x<r^{4 theta_*}` without floating logarithms.

Assume for contradiction that

\[
\lambda_1\ge r^{4\theta_*}>x.
\tag{4.4}
\]

From the fourth-trace cap (3.15), all non-Perron spectral points satisfy `|lambda_j|<beta` provided

\[
\beta^4>\frac{1085231}{10^6}-x^4.
\tag{4.5}
\]

The exact checker gives positive margin `1.548414922...e-7` in (4.5). It also gives `mu_lo>beta` and

\[
(x-\mu_{hi})(\mu_{lo}-\beta)-\varepsilon^2_{hi}
>2.724750731\times10^{-7}>0.
\tag{4.6}
\]

Kato--Temple then implies

\[
\lambda_1
\le \mu+\frac{\varepsilon^2}{\mu-\beta}
<x,
\]

contradicting (4.4). Therefore

\[
\lambda_1<r^{4\theta_*}.
\]

Using (2.9) yields the claimed strict source-level bound (0.1).

## 5. Essential executed exact checker and output

The theorem-deciding finite comparisons were executed with Python `Fraction`/integer arithmetic; `pi`, `sqrt`, and `asin` are enclosed outward by rational series/roots. The exact script executed in this run was:

```python
from fractions import Fraction as F
from math import isqrt
r=F(7,8); s=F(24861,25000); csrc=s*(1+r)/2

def Ppoly(z): return 2+2*z-3*z*z-2*z**3-2*z**4
cov_margins=[]
for k in range(1,6):
    u=r**k; cap=csrc*r**(k-1); z=u*u
    T=Ppoly(z)+6*u**5*(cap-u)/(1-u*u)
    margin=T*T-4*(1+z)**2*(1-z*z)**3
    assert T>0 and margin>0
    cov_margins.append(margin)
assert r**6<F(1,2) and csrc/r>1

aa=(r+r**3)/(1+r**4); bb=2*r*r/(1+r**4)
v=(1+aa)/(1+r); g=(1+bb+2*aa)/(2*(1+r)); h=(aa+bb)/(1+r)
varV=s*v+(1-s); A=s*g/varV; B=s*h/varV
assert A==F(168557580,170952323) and B==F(167065920,170952323)
den=1+B-2*A*A; qB=(B*(1+B)-2*A*A)/den
assert den>0 and qB>-F(3,8) and 1-2*A+B>0
assert F(213,1000)**2>1-B*B
dec_orth=3*(A-B)/(16*F(22,7)*F(213,1000))
assert dec_orth>F(243,100000)

def atan_series_bounds(x,m):
    x=F(x); ss=F(0)
    for k in range(m+1): ss += F((-1)**k,2*k+1)*x**(2*k+1)
    nxt=F((-1)**(m+1),2*(m+1)+1)*x**(2*(m+1)+1)
    return min(ss,ss+nxt),max(ss,ss+nxt)
a5=atan_series_bounds(F(1,5),90); a239=atan_series_bounds(F(1,239),30)
PI=(16*a5[0]-4*a239[1],16*a5[1]-4*a239[0])
DROOT=10**80

def sqrt_bounds(x):
    m=isqrt((DROOT*DROOT*x.numerator)//x.denominator)
    lo,hi=F(m,DROOT),F(m+1,DROOT)
    assert lo*lo<=x<hi*hi
    return lo,hi

def asin_bounds_pos(rho):
    slo,shi=sqrt_bounds(1-rho*rho); tlo,thi=slo/rho,shi/rho
    al,_=atan_series_bounds(tlo,140); _,ah=atan_series_bounds(thi,140)
    return PI[0]/2-ah,PI[1]/2-al

asinA=asin_bounds_pos(A); sqrt_ratio=sqrt_bounds((1-A)/(1+A))
q=A/(5*(1+A)); factor4=1-q+3*q*q-15*q**3+105*q**4
J_upper=sqrt_ratio[1]*factor4
p4_eq_upper=asinA[1]/PI[0]+J_upper/16
pref=1/(1-r**4)
trace_eq_upper=pref*p4_eq_upper
trace_cyclic_upper=trace_eq_upper-pref*F(243,100000)
trace_cap=F(1085231,1000000)
assert trace_cyclic_upper<trace_cap

mu_lo=F(9116948312,10_000_000_000); mu_hi=F(9116948313,10_000_000_000)
eps2_hi=F(47004495,100_000_000_000)
theta=F(8269,50000); x=F(9154553,10_000_000); beta=F(393313,500000)
assert x**12500<r**8269 and x>mu_hi
assert beta**4>trace_cap-x**4 and mu_lo>beta
assert (x-mu_hi)*(mu_lo-beta)>eps2_hi
assert theta>F(3307,20000)
print('ALL_EXACT_CHECKS_PASS = True')
```

Executed diagnostic output:

```text
cov margins k=1..5 = [0.00014165722905023394, 0.02272851190071606, 0.11655390776668695, 0.10125247203802808, 0.06253527944379939]
rho_adj = 0.9859917492902392 rho_opp = 0.9772661585885557
q(B) = -0.36600924127145923
orthant decrement floor > 0.00244394745965848 (> 0.00243)
degree4 factor = 0.9258056804137995
equicorr trace upper < 1.0911021750260117
combined cyclic trace upper < 1.0852300334330913
trace cap = 1.085231 margin = 9.665669086104088e-07
power check = True
beta = 0.786626 tail margin = 1.5484149223752131e-07
Temple margin = 2.7247507318344e-07
old lower = 0.16535 new lower = 0.16538
old width = 0.08465 new width = 0.08462
source improvement = 3e-05
ALL_EXACT_CHECKS_PASS = True
```

## 6. What did not work, residual obstruction, and next attack

A natural attempt was to continue the alternating Gaussian-moment expansion past degree 4. It fails to improve the bound: because the expansion is asymptotic at this `q≈0.0993`, the degree-6 even majorant is already larger than the degree-4 one. I therefore did not manufacture progress from a worse certificate.

The remaining main obstruction is no longer continuum interpolation for the lower-bound direction; it is the spectral enclosure of the softened comparator. The most promising next attack is to exploit the exact two-mode decomposition of the cyclic four-dimensional orthant, or equivalently a sharper certified integral for `P_b`, to lower `tr(K^4)` further without changing `(r,s)` or rebuilding the degree-18 quasimode. A separate possible route is to optimize `(r,s)` while rebuilding the quasimode, but that is materially more expensive.

No upper endpoint improvement is claimed. A new upper bound on `theta` would require a reverse continuous interpolation estimate together with a lower persistence bound for a barrier-shrunk sampled process; this remains open here.

## 7. Source-level versus mechanism-level progress

**Source-level before:** repository candidate `3307/20000 < theta_{2,1/4} <= 1/4`, width `1693/20000 = 0.08465`.

**Source-level after:** candidate `8269/50000 < theta_{2,1/4} <= 1/4`, width `4231/50000 = 0.08462`.

**Demonstrated mechanism gain:** preserve the exact all-lag source covariance domination and zero-loss continuum inclusion; replace the equicorrelated quadratic resolvent majorant by the degree-4 majorant; then compose it with the exact cyclic Plackett decrement. This lowers the certified cyclic fourth-trace cap from `1.0862` to `1.085231` and makes the Temple contradiction work at `theta_*=0.16538`.

## 8. ledger_delta

```yaml
ledger_delta:
  live20_slot: NM09
  parent: T05
  source_status: OPEN
  report_status: PARTIAL_CANDIDATE
  exact_event: "P{ integral_0^t B_{1/4}(u)du <= 1 for all t in [0,T] }"
  exponent_existence: SOURCE_PROVED_MOLCHAN_STATEMENT_1_2
  literature_proved_bracket: "1/8 <= theta_{2,1/4} <= 1/4"
  repository_before_lower: "3307/20000"
  repository_after_lower: "8269/50000"
  repository_before_width: "1693/20000"
  repository_after_width: "4231/50000"
  source_gain: "3/100000"
  mechanism_before_trace_cap: "1.0862"
  mechanism_after_trace_cap: "1085231/1000000"
  continuum_interpolation_loss_lower_bound_direction: "0 exactly by event inclusion"
  finite_check: "ALL_EXACT_CHECKS_PASS"
  failed_route: "degree-6 alternating moment majorant is worse than degree 4"
  residual_obstruction: "sharper spectral/orthant enclosure or reverse interpolation for upper endpoint"
  next_attack: "certified exact/two-mode cyclic orthant integral at fixed r=7/8,s=24861/25000"
```
