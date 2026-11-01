Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — not GPT-6 maximum. T05 source metric MOVED: current repository candidate `517/3125 < theta_{2,1/4} <= 1/4` (width `1057/12500 = 0.08456`) -> `41369/250000 < theta_{2,1/4} <= 1/4` (width `21131/250000 = 0.084524`); demonstrated mechanism gain: certified cyclic fourth-trace cap `1.08331 -> 1.082139`, with continuous-to-grid loss exactly zero in the lower-bound direction.**

# T05 — stronger probit envelope + 64-block Plackett comparison

**Status: PARTIAL / CANDIDATE pending later independent review.** The exact exponent remains open.

## Frozen source and handoff

LIVE20 assigns NM09 to T05. My preceding report had `theta_{2,1/4}>0.16538`; current master subsequently advanced the same source to `0.16544` in `runs/prob10_2026-09-20/PROB10-05/2026-09-20T0158Z__piecewise_plackett_165440.md`. This run consumes that stronger baseline rather than resetting it. Canonical ownership stays `operations/claims/MOLCHAN-2025-THETA2H.md`.

For standard fBM `B_{1/4}` freeze

\[
I(t)=\int_0^tB_{1/4}(u)du,\qquad
p(T)=P\{I(t)\le1\ \forall 0\le t\le T\}=T^{-\theta_{2,1/4}+o(1)}.
\]

`Var I(1)=2/5`, so the unit-variance Lamperti dual is

\[
X(\tau)=\sqrt{5/2}\,e^{-5\tau/4}I(e^\tau).
\]

Molchan arXiv:2509.10265v11 was inspected directly. Statement 1.2(a) gives existence and equality of the self-similar and Lamperti-dual persistence exponents for `alpha+H>1`, hence at `(2,1/4)`; the paper still calls one-sided `theta_{2,H}`, `H!=1/2`, unsolved and reports the old general `H(1-H)` proposal refuted. I do not use that formula. The external source bracket remains `1/8 <= theta_{2,1/4} <= 1/4`.

A bounded 20 September 2026 primary-source check also inspected Zhang arXiv:2604.01701 (Chung/small-ball laws for integrated fractional processes), Aurzada--Helmer arXiv:2608.17463 (fractional Levy fields on Riemannian index sets), and Molchan arXiv:2608.26680 (multivariate-time fBM). None states an exact continuous one-sided integrated-fBM exponent at `H=1/4`. This is bounded negative evidence, not a worldwide novelty claim.

## 1. Exact continuous covariance comparison and zero interpolation loss

At `H=1/4`, with `u=e^{-|tau|/4}`,

\[
R(u)=\frac{-2u^{10}+5u^6+5u^4+2(1-u^4)^{5/2}-2}{6u^5}.
\]

Freeze

\[
r=7/8,\quad s=24861/25000,\quad c=s(1+r)/2=74583/80000.
\]

For the softened AR-edge comparator `Z`, `Cov(Z_0,Z_k)=c r^{k-1}`. The exact checker re-establishes

\[
\boxed{R(r^k)<c r^{k-1}\quad(k\ge1)}.
\]

For `k=1,...,5`, radical isolation and squaring give positive rational margins with decimal values
`0.00014165722905, 0.0227285119007, 0.116553907767, 0.101252472038, 0.0625352794438`.
For `k>=6`, `u=r^k<1/2`; with `z=u^2`,

\[
P(z)^2-4(1+z)^2(1-z^2)^3=z^3Q(z),
\]

`P(z)=2+2z-3z^2-2z^3-2z^4` and `Q(z)=8z^5+16z^4+8z^3-20z^2-7z+4>=4-7z-20z^2>=1` on `0<=z<=1/4`. Thus `R(u)<=u<c r^{k-1}`.

Set `Delta=4 log(8/7)`. Then

\[
\{X(t)<0\ \forall 0\le t\le n\Delta\}\subseteq
\{X(j\Delta)<0,1\le j\le n\}.
\]

Hence the continuum interpolation error in the direction used here is **exactly zero**. Slepian and the all-lag covariance bound give

\[
P\{X(t)<0\ \forall t\in[0,n\Delta]\}
\le P\{Z_j<0,1\le j\le n\}.
\]

If `lambda_1` is the Perron eigenvalue of the inherited self-adjoint killed transfer operator `K=K_{r,s}`, then

\[
\theta_{2,1/4}\ge-\log\lambda_1/(4\log(8/7)).
\]

No reverse grid-to-continuum claim is made; the upper endpoint is unchanged.

## 2. New analytic lemma: a stronger probit product bound

At the equicorrelated four-cycle endpoint

\[
\rho=168557580/170952323,
\]

write `C^2=rho/(1-rho)`, `U=Phi(-CZ)`, `Q=U(1-U)`. Symmetry and the bivariate Gaussian sign identity give

\[
P_{eq}=EU^4=\arcsin(\rho)/\pi+EQ^2.
\]

### Lemma
For every real `x`,

\[
\boxed{\Phi(x)\Phi(-x)\le
\frac{e^{-x^2/2}}{4\sqrt{1+6x^2/25}}.}
\]

**Proof.** By symmetry take `x>=0`, set `y=x/sqrt(2)` and `a=12/25`. The claim is `F(y)>=0` where

\[
F(y)=erf(y)^2+e^{-y^2}(1+ay^2)^{-1/2}-1.
\]

Writing `F'=e^{-y^2}g`,

\[
g(y)=4erf(y)/\sqrt\pi-A(y),\qquad
A(y)=y[(2+a)+2ay^2](1+ay^2)^{-3/2}.
\]

Moreover

\[
A'(y)=[2+a+2a(1-a)y^2](1+ay^2)^{-5/2}.
\]

For `H(y)=e^{y^2}A'(y)`, direct differentiation gives

\[
H'(y)=\frac{e^{y^2}y}{(1+ay^2)^{7/2}}
[4a^2(1-a)y^4+(6a^3-8a^2+8a)y^2+4-4a-9a^2].
\]

At `a=12/25` all three bracket coefficients are positive; the constant is exactly `4/625`. Thus `H` is strictly increasing. Also `H(0)=62/25<28/11<8/pi` (`pi<22/7`) and `H->infinity`, so `g'=e^{-y^2}(8/pi-H)` changes sign exactly once from positive to negative. Finally `g(0)=0` and `g(infinity)=4/sqrt(pi)-2/sqrt(a)<0` because `4a=48/25<3<pi`. Hence `g` has exactly one positive zero, so `F` first increases then decreases. Since `F(0)=F(infinity)=0`, `F>=0`. QED.

Squaring and using `1/(1+t)<=1-t+t^2-t^3+t^4` for `t>=0` gives, with `A_*=(1+rho)/(1-rho)` and `q=6rho/[25(1+rho)]`,

\[
EQ^2\le\frac{A_*^{-1/2}}{16}(1-q+3q^2-15q^3+105q^4).
\]

Exact outward rational bounds for `pi`, `asin(rho)` and the square root certify

\[
\boxed{P_{eq}/(1-r^4)<1.091019}.
\]

The prior NM13-09 endpoint cap was `1.091102175...`; this is a strict mechanism improvement.

## 3. New 64-block Plackett refinement

For the cyclic path with opposite correlation `b=167065920/170952323`,

\[
P'(c)=\frac1{\pi\sqrt{1-c^2}}
\left[\frac14+\frac{\arcsin q(c)}{2\pi}\right],
\quad
q(c)=\frac{c(1+c)-2\rho^2}{1+c-2\rho^2},
\]

and `q` is increasing. Use the rigorous envelope

\[
B(q)=\begin{cases}
\max\{3/16,1/4+20q/111\},&q<0,\\
1/4+7q/44,&q\ge0.
\end{cases}
\]

Let `c_j=b+j(rho-b)/64` and `s_j=10^{-7} ceil(10^7 sqrt(1-c_j^2))`. Then `s_j^2>=1-c_j^2`, and monotonicity plus `1/pi>7/22` gives the exact rational lower sum

\[
P(\rho)-P(b)>
\frac{\rho-b}{64}\sum_{j=0}^{63}\frac7{22s_j}B(q(c_j))
=0.003675824655322\ldots
>\boxed{147/40000}.
\]

The current-master certified decrement was `>0.003615`. With the inherited exact identity `tr(K^4)=P(b)/(1-r^4)`,

\[
tr(K^4)<1.091019-\frac{147/40000}{1-(7/8)^4}
=1.082138292035398\ldots<\boxed{1.082139}.
\]

Thus the rigorous cyclic fourth-trace cap moves `1.08331 -> 1.082139`.

## 4. Spectral step and source-level gain

The archived exact degree-18 quasimode at the same `(r,s)` certifies

\[
9116948312/10^{10}<\mu<9116948313/10^{10},\qquad
\varepsilon^2<47004495/10^{11}.
\]

Set

\[
\theta_*=41369/250000=0.165476,
\quad x=9154083/10^7,
\quad \beta=196277/250000=0.785108.
\]

Because `4 theta_*=41369/62500`, exact integer arithmetic gives `x^62500<r^41369`, so `x<r^(4 theta_*)`. If `lambda_1>=r^(4 theta_*)`, then `lambda_1>x`. The new trace cap forces every non-Perron spectral point below `beta` in modulus because

\[
\beta^4-(1.082139-x^4)>9.36909\times10^{-7}>0.
\]

Temple's spectral-measure inequality gives

\[
\varepsilon^2\ge(\lambda_1-\mu)(\mu-\beta)
>(x-\mu_{hi})(\mu_{lo}-\beta),
\]

while the exact checker proves

\[
(x-\mu_{hi})(\mu_{lo}-\beta)-47004495/10^{11}
>3.12854\times10^{-8}>0,
\]

contradiction. Therefore `lambda_1<r^(4 theta_*)`, and section 1 yields

\[
\boxed{\theta_{2,1/4}>41369/250000=0.165476}.
\]

So the current repository candidate bracket strictly improves from

\[
517/3125<\theta_{2,1/4}\le1/4,\qquad W=0.08456,
\]

to

\[
\boxed{41369/250000<\theta_{2,1/4}\le1/4},\qquad
\boxed{W=21131/250000=0.084524}.
\]

The source metric gain is exactly `9/250000=0.000036`.

## 5. Essential executed exact code/output

All theorem-deciding finite comparisons were executed with Python `Fraction`/integer arithmetic. The full in-run checker used rational Machin bounds for `pi=16 atan(1/5)-4 atan(1/239)` and outward integer-square-root / `asin` enclosures. The essential exact core is:

```python
from fractions import Fraction as F
from math import isqrt
r=F(7,8); s=F(24861,25000)
rho=F(168557580,170952323); b=F(167065920,170952323)

# covariance k<=5; tail k>=6
c=s*(1+r)/2
def Ppoly(z): return 2+2*z-3*z*z-2*z**3-2*z**4
for k in range(1,6):
    u=r**k; cap=c*r**(k-1); z=u*u
    T=Ppoly(z)+6*u**5*(cap-u)/(1-u*u)
    assert T>0 and T*T-4*(1+z)**2*(1-z*z)**3>0
assert r**6<F(1,2) and c/r>1
assert F(4)-F(7,4)-F(20,16)==1

# analytic probit-lemma sign conditions at a=12/25
ap=F(12,25)
assert 4*ap*ap*(1-ap)>0
assert 6*ap**3-8*ap*ap+8*ap>0
assert 4-4*ap-9*ap*ap==F(4,625)>0
assert 2+ap<F(28,11) and 4*ap<3

# Full run's outward irrational enclosures certify:
EQ_TRACE_CAP=F(1091019,1000000)
# exact computed equicorrelated normalized upper = 1.091018749789182...

# 64-block exact Plackett sum
def qpl(cc): return (cc*(1+cc)-2*rho*rho)/(1+cc-2*rho*rho)
def B(q):
    return max(F(3,16),F(1,4)+F(20,111)*q) if q<0 else F(1,4)+F(7,44)*q
def sqrt_up(x):
    D=10**7; x=F(x); m=isqrt((D*D*x.numerator)//x.denominator); lo=F(m,D)
    return lo if lo*lo>=x else F(m+1,D)
delta=F(0)
for j in range(64):
    cj=b+(rho-b)*F(j,64); sj=sqrt_up(1-cj*cj)
    assert sj*sj>=1-cj*cj
    delta+=(rho-b)*F(1,64)*F(7,22)/sj*B(qpl(cj))
assert delta>F(147,40000)
trace_upper=EQ_TRACE_CAP-F(147,40000)/(1-r**4)
trace_cap=F(1082139,1000000)
assert trace_upper<trace_cap

mu_lo=F(9116948312,10_000_000_000); mu_hi=F(9116948313,10_000_000_000)
eps2=F(47004495,100_000_000_000)
theta=F(41369,250000); exp=4*theta
x=F(9154083,10_000_000); beta=F(196277,250000)
assert exp==F(41369,62500)
assert x.numerator**exp.denominator*r.denominator**exp.numerator < x.denominator**exp.denominator*r.numerator**exp.numerator
assert beta<mu_lo<mu_hi<x
assert beta**4-(trace_cap-x**4)>0
assert (x-mu_hi)*(mu_lo-beta)-eps2>0
assert theta-F(517,3125)==F(9,250000)
```

Executed output:

```text
covariance squared margins k=1..5 = ['0.00014165722905', '0.0227285119007', '0.116553907767', '0.101252472038', '0.0625352794438']
probit H-prime coefficients = 0.479232 2.660352 0.0064
equicorrelated trace upper < 1.091018749789182
equicorrelated trace cap = 1.091019 margin = 2.50210817601e-07
64-block Plackett lower = 0.003675824655322 > 0.003675
combined trace upper = 1.082138292035398
combined trace cap = 1.082139 margin = 7.0796460177e-07
theta before = 0.16544
theta target = 0.165476
x = 0.9154083 power_check = True
beta = 0.785108
spectral-tail margin = 9.36909152503e-07
Temple margin = 3.12854933834e-08
width before = 0.08456
width after = 0.084524
metric improvement = 3.6e-05
ALL_EXACT_CHECKS_PASS = True
```

## 6. Residual obstruction and next attack

The exact value remains unknown; the source upper endpoint `1/4` is unchanged. A reverse grid-to-continuum theorem would need barrier-rate stability strong enough to pay cellwise Gaussian modulus costs, and is not claimed. On the lower-bound route the best next move is a certified direct two-mode integral for the cyclic four-orthant probability, or a smaller residual for the inherited quasimode.

```yaml
ledger_delta:
  worker: NM13-09
  target: T05
  source_claim: MOLCHAN-2025-THETA2H
  source_status: PARTIAL
  metric: W_1_4
  before_lower: 517/3125
  before_upper: 1/4
  before_width: 1057/12500
  after_lower: 41369/250000
  after_upper: 1/4
  after_width: 21131/250000
  source_gain: 9/250000
  mechanism_before_trace_cap: 1.08331
  mechanism_after_trace_cap: 1.082139
  continuum_interpolation_loss_used_direction: 0
  exponent_existence: source_Statement_1_2a
  status: PARTIAL_CANDIDATE_PENDING_LATER_REVIEW
  unchanged_substantive_runs: 0
  failed_recoveries: 0
  runtime_model: GPT-5.6-Sol
  runtime_reasoning: UNVERIFIED
  next_attack: certified_direct_circulant_two_mode_integral_or_stronger_quasimode
```
