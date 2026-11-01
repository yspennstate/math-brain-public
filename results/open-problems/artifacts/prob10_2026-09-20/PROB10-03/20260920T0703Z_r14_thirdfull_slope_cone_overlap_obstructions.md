# PROB10-03 / R14 — third-full slope-cone reduction and two exact route obstructions

Model/runtime metadata for this run is reported in the immutable run report; the mathematics below does not depend on a model label.

Target is frozen at `kappa=-1`, iid Gaussian rows, exact sphere `||sigma||=sqrt(N)`, `M=floor(alpha N)`.  This artifact is auxiliary mechanism progress unless and until a complete source-matched comparison certificate is obtained.

## 1. Exact third-full q-sector compiler

Use the `r=3` stationarized complete full-lifting notation of Stojnic, arXiv:2312.16531, Section 4.2.5--4.2.6.  Work in the strict interior

`0 < p3 < p2 < 1`, `0 < q3 < q2 < 1`,

with positive lifting parameters `c2,c3,gamma_p`.  Define the three secant slopes

`r2 = q3/p3`,

`r1 = (q2-q3)/(p2-p3)`,

`r0 = (1-q2)/(1-p2)`.

The source's exact q-sector stationarity relations (its equations (142), (145), (147)) can be rewritten as

`gamma_p = (1/2) r0 sqrt(r2)/r1`,

`c3 = (r1-r2)/((p2-p3) r1 sqrt(r2))`,

`c2 = (r0 r2-r1^2)/((1-p2) r0 r1 sqrt(r2))`.          (1.1)

### Theorem R14-T03-THIRDFULL-SLOPE-CONE

Under the strict-interior hypotheses above, the three original stationarity equations with respect to `q3`, `q2`, and `gamma_p` are equivalent to the reconstruction (1.1), provided the resulting denominators are positive.  In particular

`c2>0 and c3>0`

is equivalent to

`r1>r2` and `r1^2<r0 r2`.                              (1.2)

Hence every genuine positive-`c` third-full stationary point satisfies the strict slope hierarchy

`r0 > r1 > r2 > 0`.                                    (1.3)

The stronger condition `r1^2<r0 r2` says that the three secant slopes are strictly log-convex at the middle level.

### Proof

Set

`A2 = 2 gamma_p-c2(1-q2)`,

`A3 = A2-c3(q2-q3)`.

The source's `q3` stationarity equation gives

`p3=q3/A3^2`,

so positivity of the source denominators forces

`A3=sqrt(q3/p3)=sqrt(r2)`.                              (1.4)

The `q2` stationarity equation gives

`p2-p3=(q2-q3)/(A2 A3)`,

and therefore

`A2=r1/sqrt(r2)`.                                       (1.5)

Subtracting (1.4) from (1.5) and using the definition of `A3` gives

`c3(q2-q3)=A2-A3=(r1-r2)/sqrt(r2)`,

which is the formula for `c3` in (1.1).

The `gamma_p` stationarity equation is the source identity

`1=(1-q2)/(2 gamma_p A2)+(q2-q3)/(A2 A3)+p3`.

The second term equals `p2-p3` by the `q2` equation, so

`1-p2=(1-q2)/(2 gamma_p A2)`.

Using (1.5) and `r0=(1-q2)/(1-p2)` gives

`gamma_p=(1/2) r0 sqrt(r2)/r1`.

Finally

`c2(1-q2)=2 gamma_p-A2`

and substitution of the formulas just obtained yields

`c2=(r0 r2-r1^2)/((1-p2)r0 r1 sqrt(r2))`.

This proves necessity.

Conversely, start from `p2,p3,q2,q3` in the strict domain and define `gamma_p,c2,c3` by (1.1).  Direct substitution gives

`A2=r1/sqrt(r2)`, `A3=sqrt(r2)`.

Therefore

`q3/A3^2=p3`,

`(q2-q3)/(A2 A3)=p2-p3`,

and

`(1-q2)/(2 gamma_p A2)+(q2-q3)/(A2 A3)+p3=(1-p2)+(p2-p3)+p3=1`.

Thus all three original q-sector stationarity equations hold.  This proves equivalence.

Because every remaining factor in the denominators of (1.1) is positive, `c3>0 iff r1>r2` and `c2>0 iff r1^2<r0 r2`.  If both hold, then

`r0 > r1^2/r2 > r1 > r2`,

proving (1.3).  QED.

## 2. Five-scalar reduction of the remaining third-full search

The preceding theorem removes three variables before any Gaussian quadrature is attempted.

Choose

`(p2,p3,r1,r2,B)`

with `0<p3<p2<1`, define

`q3=p3 r2`,

`q2=q3+(p2-p3)r1`,

`r0=(1-q2)/(1-p2)`,

and require `0<q3<q2<1` and the cone inequalities (1.2).  Reconstruct `gamma_p,c2,c3` by (1.1), and set

`gamma_sq=c2/(4B)`, `B>0`.

Then the three q-sector stationarity equations are automatic.  The full third-level certificate is reduced to the remaining five original stationarity/comparison obligations evaluated after this reconstruction.  No differentiation of a numerically minimized surrogate is needed, and no q-sector root finder is needed.

This is an exact reduction, not a claim that the remaining five equations have been solved.

### Source-table consistency check, numerical only

Stojnic's rounded `kappa=-1` third-full table gives approximately

`p3=0.6252`, `p2=0.9691`, `q3=0.2500`, `q2=0.6536`,

`c3=3.03`, `c2=12.1`, `gamma_p=3.0237`, `gamma_sq=0.0835`, `alpha=12.29`.

The slopes computed from the rounded values are approximately

`r2=0.3998720`, `r1=1.1735970`, `r0=11.2103560`,

with large strict cone margins

`r1-r2 approximately 0.773725`,

`r0*r2-r1^2 approximately 3.10538`.

Formula (1.1) reconstructs approximately

`gamma_p=3.02017`, `c3=3.03162`, `c2=12.0797`,

consistent with the table's coarse rounding.  This is only a sanity check.  The displayed `alpha=12.29` remains numerical and is NOT promoted to a rigorous bracket endpoint.

## 3. Lower-side overlap route: exact curvature obstruction for the MZZ second-moment bound at kappa=-1

Montanari--Zhong--Zhou, arXiv:2110.15824, Definition 1, define for `kappa<0` the unique positive `c*=c*(kappa)` solving

`c* Q(kappa+c*)=phi(kappa+c*)`,

where `Q=1-Phi`, and the weighted two-replica kernel

`K(q)=E_q[w(G1)w(G2)]`,

`w(x)=exp(-c*x) 1{x>=kappa}`.

Their lower threshold `delta_lb(kappa)` requires, among other things, strict local curvature `Psi''(0)>0` for

`Psi(q)=-log K(q)-(1/(2 delta))log(1-q^2)`.

### Theorem R14-T03-MZZ-CURVATURE-CAP

For every `kappa<0`, at the MZZ choice `c=c*(kappa)`,

`Psi''(0)=1/delta-kappa^2 c^2`.                         (3.1)

Consequently

`delta_lb(kappa) <= 1/(kappa^2 c*(kappa)^2)`.           (3.2)

At `kappa=-1`, one has `c*(-1)>1/2`, hence

`delta_lb(-1)<4`.                                       (3.3)

On the other hand MZZ's rigorous LP threshold is

`delta_lin(-1)=1/Phi(-1)>4`.

Therefore MZZ Theorem 4.1's particular weighted second-moment route is rigorously incapable of improving the already used LP lower endpoint at `kappa=-1`.

### Proof of (3.1)

Let `H_j` be probabilists' Hermite polynomials and

`m_j=E[w(G)H_j(G)]`.

Mehler's expansion, valid near `q=0` because this truncated exponential weight is in `L^2`, gives

`K(q)=sum_{j>=0} m_j^2 q^j/j!`.

Put `a=kappa+c`.  Completing the square gives

`m0=e^{c^2/2} Q(a)`,

`m1=e^{c^2/2}(phi(a)-c Q(a))=0`

by the defining equation for `c*`.  Also

`m2=e^{c^2/2} integral_a^infty ((y-c)^2-1)phi(y)dy`

`   =e^{c^2/2}[c^2 Q(a)+(a-2c)phi(a)]`

`   =kappa c m0`.

Hence `K'(0)=0`, `K''(0)=m2^2`, and

`(-log K)''(0)=-(m2/m0)^2=-kappa^2 c^2`.

The second derivative at zero of `-(2delta)^{-1}log(1-q^2)` is `1/delta`, proving (3.1).  The curvature requirement in the definition of `delta_lb` gives (3.2).

### Exact elementary proof that c*(-1)>1/2

MZZ prove existence and uniqueness of `c*` and monotonicity of the corresponding Mills-ratio equation.  It therefore suffices to show at `c=1/2`

`(1/2) Phi(1/2) < phi(1/2)`.                            (3.4)

We use only classical rational bounds.  From `pi<22/7`,

`phi(0)=1/sqrt(2pi)>199/500`.

From `pi>25/8`, `phi(0)<2/5`, and therefore

`Phi(1/2)<1/2+(1/2)phi(0)<7/10`.

The alternating Taylor series gives

`exp(-1/8)>1-1/8+1/128-1/3072=2711/3072`.

Thus

`2 phi(1/2) > 2*(199/500)*(2711/3072)`

`             =539489/768000`

`             >7/10`

because the last difference is `1889/768000>0`.  This proves (3.4), so `c*(-1)>1/2` and (3.3) follows.

Finally `Phi(-1)=Q(1)<phi(1)<1/4`: the first inequality is the elementary Mills estimate

`integral_1^infty phi(t)dt < integral_1^infty t phi(t)dt=phi(1)`,

and `phi(1)<1/4` follows from `e>8/3` and `pi>3`, which imply `2 pi e>16`.  Hence `delta_lin(-1)>4`.

QED.

## 4. Dual-feasibility negation test: the standard first Shor SDP is identically feasible

A natural attempt to dualize the exact sphere is to lift `X=xx^T` and drop rank one.  The standard first Shor relaxation of

`||x||^2=1`, `Gx>=-1`

contains the constraints

`Tr(X)=1`,

`[[1,x^T],[x,X]] >= 0`,

`Gx>=-1`.

### Proposition R14-T03-SHOR-NOGO

For every deterministic matrix `G`, every dimension `N`, and every number of rows, this relaxation is feasible.  Indeed

`x=0`, `X=I_N/N`

satisfies all three displayed conditions.  Therefore the standard degree-two/Shor relaxation, without additional localizing constraints coupling the Gaussian inequalities to the lifted moments, can never certify UNSAT for the negative-margin spherical perceptron at any density.

This is a certified obstruction to a tempting dual-feasibility shortcut.  A useful SDP/SOS route must keep nontrivial higher-order coupling; merely lifting the sphere and retaining the linear constraints loses the problem at the origin.

## 5. Consequences for the next iteration

1. The second-full mechanism is already essentially saturated near `12.31963435`; further decimal shaving is not a material route.
2. The third-full source table near `12.29` now has an exact five-scalar search domain with a strict algebraic cone.  The next useful upper-side task is to derive the remaining five stationarity/comparison residuals in `(p2,p3,r1,r2,B)` and then build directed enclosures near the source's `kappa=-1` candidate.
3. The MZZ weighted second-moment lower bound is now analytically ruled out as a way to beat the current LP lower endpoint at `kappa=-1`; do not spend another run globally optimizing its overlap functional for this purpose.
4. A naive Shor/degree-two SDP is identically feasible, so any SOS attack must add genuinely higher-degree/localizing information rather than another solver pass on that relaxation.

No source-level endpoint is promoted by this artifact.  In particular, `12.29` remains numerical until the remaining third-full equations and the source comparison implication are certified.