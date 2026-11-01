# PROB10-03 / R14 — third-full scale-Euler identity and four-scalar capacity reduction

Target is frozen at `kappa=-1`, iid Gaussian rows, exact sphere `||sigma||=sqrt(N)`, and `M=floor(alpha N)`.  Everything below is an exact statement about the interior third-full stationarized fl-RDT system used in Stojnic, arXiv:2312.16531.  It is **mechanism progress**, not by itself a new rigorous source endpoint.

The newest complementary work consumed before this derivation is NM13-03's exact third-full five-equation reduction and `alpha=12.288` numerical-only positive-comparison point, followed by NM13-07's exact score/overlap identities and derivative-free five-scalar capacity compiler.  The current repository-supported bracket remains

`6.30297437506 <= alpha_c(-1) <= 12.31963485`.

The owner-prescribed Campbell--O'Rourke Q1.8 handoff remains preserved at `artifacts/prob10_2026-09-20/PROB10-03/20260919T2354Z_campbell_q18_r14_handoff.md`; no Campbell claim is edited here.

## 1. Source-matched third-full notation

Work in the strict interior

`0 < p3 < p2 < 1`, `0 < q3 < q2 < 1`,

`c2 > c3 > 0`, `gamma_p>0`, `gamma_sq>0`.

Set

`Aq = 2 gamma_p - c2(1-q2)`,

`Dq = Aq - c3(q2-q3)`,

`B = c2/(4 gamma_sq)`, `m=c3/c2`.

After closing the q-Gaussian block, the third-full objective is

`Psi3 = L + H + gamma_sq - (alpha/c3) Q`,                         (1.1)

where

`L = 1/2(1-p2 q2)c2 + 1/2(p2 q2-p3 q3)c3 - gamma_p`,            (1.2)

`H = (1/(2c2)) log(Aq/(2 gamma_p))`
`    + (1/(2c3)) log(Dq/Aq) - q3/(2Dq)`,                        (1.3)

and `Q` is the nested perceptron Gaussian term.  Its dependence on the scale variables `(c2,c3,gamma_sq)` is only through `(m,B)`.

Use the secant slopes already proved in the preceding R14 report:

`r2 = q3/p3`,

`r1 = (q2-q3)/(p2-p3)`,

`r0 = (1-q2)/(1-p2)`.                                           (1.4)

The q-sector stationarity equations are equivalent to

`gamma_p = (1/2) r0 sqrt(r2)/r1`,                               (1.5)

`c3 = (r1-r2)/((p2-p3) r1 sqrt(r2))`,                           (1.6)

`c2 = (r0 r2-r1^2)/((1-p2) r0 r1 sqrt(r2))`,                   (1.7)

with the strict positivity cone

`r1>r2`, `r1^2<r0 r2`, hence `r0>r1>r2>0`.                      (1.8)

## 2. Attack 1 — exact scale-Euler identity

### Theorem R14-T03-SCALE-EULER

At every strict-interior third-full stationary point (all eight non-fixed source derivatives zero),

`Psi3 = 2 gamma_sq - r1/(r0 sqrt(r2))`.                          (2.1)

In particular, **the value and sign of the full third-level comparison objective at a stationary point do not require evaluating the nested perceptron integral `Q`**.

At a stationary capacity point `Psi3=0`, necessarily

`gamma_sq = r1/(2 r0 sqrt(r2))`,                                (2.2)

and therefore

`B = (r0 r2-r1^2)/(2(1-p2)r1^2)`.                              (2.3)

The right side of (2.3) is positive automatically on the strict cone (1.8).

### Proof

Scale simultaneously

`(c2,c3,gamma_p,gamma_sq) -> t(c2,c3,gamma_p,gamma_sq)`, `t>0`,

while keeping `(p2,p3,q2,q3,alpha)` fixed.

Then `Aq` and `Dq` scale by `t`, whereas the ratios

`Aq/(2 gamma_p)`, `Dq/Aq`, `m=c3/c2`, `B=c2/(4 gamma_sq)`

are unchanged.  Consequently `Q` is unchanged.  Thus along this one-dimensional scaling direction

`Psi3(t) = t X + t^{-1} Y`,                                    (2.4)

where

`X=L+gamma_sq`,

`Y=H-(alpha/c3)Q`

are evaluated at `t=1`.

Full stationarity includes stationarity in each of `c2,c3,gamma_p,gamma_sq`, so the derivative along their common scaling direction vanishes:

`0 = d/dt Psi3(t)|_{t=1} = X-Y`.

Hence `X=Y`, and (1.1) gives

`Psi3 = X+Y = 2X = 2(L+gamma_sq)`.                              (2.5)

It remains to simplify `2L` under q-sector stationarity.  Substitute (1.5)--(1.7), together with

`q3=p3 r2`,

`q2=q3+(p2-p3)r1`,

`1-q2=(1-p2)r0`.                                               (2.6)

A direct common-denominator calculation gives

`2L + r1/(r0 sqrt(r2)) = 0`.                                   (2.7)

For a compact verification, before imposing the last identity in (2.6), the left side of (2.7) vanishes after substituting

`p3 = [1-r0(1-p2)-p2 r1]/(r2-r1)`,

which is exactly the same relation `1-q2=(1-p2)r0` written using the first two equations in (2.6).  Combining (2.5) and (2.7) proves (2.1).

Setting `Psi3=0` gives (2.2).  Finally combine `B=c2/(4 gamma_sq)` with (1.7) and (2.2) to obtain (2.3).  QED.

## 3. Attack 2 — exact residual-dependency identity

The previous five-scalar derivative-free compiler used residuals

`R3, R2, Rc3, Rc2, Rcap`

in `(p2,p3,q2,q3,B)`, after q-sector reconstruction and after reconstructing `alpha` from the `gamma_sq` stationarity equation.

There is an exact hidden dependency among the last three.

### Proposition R14-T03-RESIDUAL-DEPENDENCY

Assume q-sector reconstruction and reconstruct `alpha` from `partial_{gamma_sq} Psi3=0`.  Then

`Rcap + c2 Rc2 + c3 Rc3`
`    = 2 gamma_sq - r1/(r0 sqrt(r2))`.                           (3.1)

Therefore, once the capacity scaling relation (2.2) is imposed, any two of `Rcap,Rc2,Rc3` force the third.  In particular, one must not count all three as independent equations in a capacity validator.

### Proof

Write `A0=L+H`, so `Psi3=A0+gamma_sq-(alpha/c3)Q`.  Let

`E2=c2 partial_{c2}A0`, `E3=c3 partial_{c3}A0`,

where source partial derivatives are taken before any reconstruction.  Put `Q_m=partial_m Q`, `Q_B=partial_B Q`.  Direct differentiation gives

`c3 Rc3 = E3 + (alpha/c3)Q - (alpha/c2)Q_m`,                    (3.2)

`c2 Rc2 = E2 - (alpha/c3)(B Q_B-m Q_m)`.                       (3.3)

The `gamma_sq` stationarity equation is

`alpha B Q_B/c3 = -gamma_sq`.                                  (3.4)

Adding (3.2), (3.3), and `Rcap=A0+gamma_sq-(alpha/c3)Q`, using `m=c3/c2` and (3.4), yields

`Rcap+c2 Rc2+c3 Rc3 = A0+E2+E3+2 gamma_sq`.                    (3.5)

Because q-sector stationarity includes `partial_{gamma_p}A0=0`, simultaneous scaling of `(c2,c3,gamma_p)` shows

`A0+E2+E3 = 2L`.                                               (3.6)

Equation (2.7) then turns (3.5) into (3.1).  QED.

## 4. Corollary — a four-scalar derivative-free capacity compiler

This improves the newest five-scalar compiler by one full dimension.

Choose only

`(p2,p3,q2,q3)`

in the strict domain.  Reconstruct `(c2,c3,gamma_p)` by (1.5)--(1.7), and set `(gamma_sq,B)` by (2.2)--(2.3).  Define the exact score moments from the preceding NM13-07 theorem,

`M1 = E_V <u_x>_V^2`,

`M2 = E_V <u_x^2>_V`,

`MB = -E_V <u_B>_V`,

`QM = E_V <u>_V`,

as well as the nested log-partition `Q`.  Reconstruct

`alpha = c2^2/(4 B^2 MB)`.                                     (4.1)

Then a strict-domain capacity point is equivalent to the four residual equations

`R3 := q3 - M1/(4B^2 MB) = 0`,                                 (4.2)

`R2 := q2 - M2/(4B^2 MB) = 0`,                                 (4.3)

`Rc3 := A_c3 + alpha Q/c3^2 - alpha QM/(c2 c3) = 0`,            (4.4)

`Rc2 := A_c2 - alpha Q_c2/c3 = 0`,                             (4.5)

where

`Q_B=-m MB`,

`Q_c2=(B Q_B-m QM)/c2`,                                        (4.6)

and `A_c2,A_c3` are the exact closed q-side derivatives already written in the NM13-07 report.

Indeed, q-sector stationarity is automatic by reconstruction; (4.2)--(4.3) are the two `p` equations; (4.1) is the `gamma_sq` equation; (4.4)--(4.5) are the two `c` equations; and (2.1)--(2.3) force `Psi3=0`.  Conversely every strict interior capacity point satisfies these four equations and all reconstructions.

Thus the third-full capacity certification problem is now a **four-variable derivative-free Gaussian-moment root problem**.  No numerical differentiation and no separate objective residual are needed.

## 5. Attack 3 — numerical-only falsification and conditioning scout

Only after the exact reduction above, I independently evaluated the four-scalar system by product Gauss--Hermite quadrature.  These calculations are **NUMERICAL ONLY** and are not bracket endpoints.

First, at NM13-03's independent stationary point at `alpha=12.288`, (2.1) gives

`2 gamma_sq-r1/(r0 sqrt(r2)) = 2.6597739161970946e-5`,

matching the independently reported positive comparison value `2.65977391709358e-5` to the displayed numerical accuracy.  This is a falsification check of the scaling identity against a stationary point obtained by a different worker and different implementation.

Second, solving the new four-variable system at Gauss--Hermite orders `60,80,100,120,160,200` gives respectively

`12.2872227715011`,
`12.2872221830901`,
`12.2872222240457`,
`12.2872222215128`,
`12.2872222215935`,
`12.2872222215930`.

This reproduces NM13-03's independently found third-full zero near `12.28722222159`, but with one fewer unknown and without numerical differentiation of the nested Gaussian term.

At order 160, a finite-difference diagnostic of the new four-dimensional residual Jacobian has singular values approximately

`0.763438929792, 0.515049883318, 0.0105132668077, 0.000268730576534`,

condition number about `2.84e3`.  This is only a numerical conditioning diagnostic, but it is substantially more favorable than the `~1.65e5` fixed-density reduced Jacobian reported in the earlier five-variable scout.  The systems are not identical, so this comparison is evidence for certification design, not a theorem.

## 6. Consequence for rigorous certification

The rigorous source bracket is **unchanged** in this artifact:

`alpha_L=6.30297437506`,

`alpha_U=12.31963485`,

`width=6.01666047494`.

The new mechanism gain is exact:

1. stationary objective/comparison sign is pattern-free by (2.1);
2. the capacity scale `gamma_sq` and `B` are algebraically reconstructed by (2.2)--(2.3);
3. the capacity root drops from five variables to four;
4. one of the previous `{Rcap,Rc2,Rc3}` equations is provably redundant after the capacity scaling relation;
5. the numerical third-full zero remains numerical until an outward-rounded root enclosure and the source comparison implication are independently validated.

The next bracket-moving attack should build a four-dimensional Krawczyk/interval box in `(p2,p3,q2,q3)`, outward-enclose `Q,M1,M2,MB,QM`, and certify the four residuals (4.2)--(4.5).  Because (2.1) is exact, a fixed-density stationary validator at `alpha=12.288` can also certify the comparison sign from the algebraic scale gap instead of separately enclosing the small difference of the full objective terms.
