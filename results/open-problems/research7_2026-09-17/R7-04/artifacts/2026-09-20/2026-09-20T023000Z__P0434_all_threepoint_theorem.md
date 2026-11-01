# P0434: factor-two theorem for every positive three-point service law

## Scope

Source: Ziv Scully, Mor Harchol-Balter, Alan Scheller-Wolf, *Simple Near-Optimal Scheduling for the M/G/1* (2020), Section 8, Conjecture 8.1, arXiv:1907.10792.

This note proves the conjectured factor-two inequality for **every service-time distribution with at most three positive support points**, at every stable load. It does **not** prove Conjecture 8.1 for arbitrary service laws. No independent audit is claimed.

## Theorem

Let the preemptive M/G/1 satisfy the source assumptions, with Poisson arrival rate `lambda`, unknown individual job sizes, known service law, attained service observable, and `rho=lambda E[X]<1`. If the positive part of `X` has at most three support points, then

\[
\boxed{\mathbb E T_{\rm M\text{-}SERPT}<2\,\mathbb E T_{\rm Gittins}}
\]

for every nondegenerate stable parameter choice. The weak inequality holds on all limiting support/mass boundaries.

A mass at zero is harmless: zero-size jobs use no service and have zero response, while the positive-size arrivals form a thinned Poisson process. The multiplicative factor `P(X>0)` therefore appears in both unconditional mean responses and cancels in the ratio. Thus it suffices to treat three strictly positive atoms.

## 1. Normalization and exact ranks

By scaling time, any three positive support points can be written

\[
X\in\{1,b,b+d\},\qquad b=1+s,\quad s,d>0,
\]

with masses

\[
P(X=1)=p,\qquad P(X=b)=q,\qquad P(X=b+d)=r,
\qquad p,q,r>0,\quad p+q+r=1.
\]

Indeed, for original smallest atom `a>0`, pass to `Y=X/a` and arrival rate `lambda'=a lambda`; the load is unchanged and every response time scales by `a`, so the policy ratio is unchanged.

Put

\[
t=q+r=1-p,
\qquad
\mu=1+ts,
\qquad
m=E[X]=\mu+rd.
\]

The SERPT values at the three support intervals start at

\[
m,\qquad H=s+\frac{rd}{t},\qquad d.
\]

Hence M-SERPT has constant rank levels

\[
r_M(a)=m\quad(0\le a<1),
\]

\[
r_M(a)=\max\{m,H\}\quad(1\le a<b),
\]

\[
r_M(a)=\max\{m,H,d\}\quad(b\le a<b+d).
\tag{1}
\]

The exact Gittins stopping candidates are

\[
r_G(a)=
\min\left\{
\frac{1-a}{p},
\frac{\mu-a}{1-r},
 m-a
\right\},
\qquad 0\le a<1,
\tag{2}
\]

\[
r_G(a)=
\min\left\{
\frac{t(b-a)}q,
(b-a)+\frac{rd}{t}
\right\},
\qquad 1\le a<b,
\tag{3}
\]

and

\[
r_G(a)=b+d-a,\qquad b\le a<b+d.
\tag{4}
\]

Define the four contact quantities

\[
h_0=\frac1p,
\qquad
h=\frac\mu{1-r},
\qquad
d_0=\frac{t(1-ps)}{pr},
\qquad
d_1=\frac{st}{q},
\tag{5}
\]

and the mass-gap discriminator

\[
\Delta=q-pst.
\tag{6}
\]

Direct algebra gives the complete ordering identities

\[
h-h_0=-\frac{\Delta}{p(1-r)},
\qquad
h-d_1=\frac{\Delta}{q(1-r)},
\tag{7}
\]

\[
d_0-h_0=\frac{\Delta}{pr},
\qquad
 d_0-h=\frac{\Delta}{pr(1-r)}.
\tag{8}
\]

Thus only two global topology orders are possible:

- if `Delta>=0`, then `d1<=h<=h0<=d0`;
- if `Delta<0`, then `d0<h0<h<d1` (with `d0` allowed to be negative).

This exhausts all three-point rank geometries.

## 2. Neutral cells

If `Delta>=0` and `d<=h`, then `H<=m` and `d<=m`. If `Delta<0` and `0<d<=d0`, then again `H<=m` and `d<m`. In either case M-SERPT has constant rank `m`, while every later Gittins hill is no higher than the fresh rank `m`. Hence once a job starts service, no later arrival preempts it. Both policies are sample-path FCFS, so

\[
E[T_M]=E[T_G].
\tag{9}
\]

The second neutral cell is empty when `d0<=0`.

## 3. Delta>=0, terminal-only middle cell: `h<d<=d0`

Here M-SERPT stays at its fresh level through age `b` and has one terminal demotion. Gittins has fresh rank `h`, no age-one hill, and one terminal hill.

Write

\[
\beta=1-\lambda\mu,
\qquad
V=p+t b^2,
\qquad
M_2=E[X^2],
\]

\[
W_\infty=\frac{\lambda M_2}{2(1-\rho)\beta},
\qquad
W_h=\frac{\lambda(V+r h^2)}{2\beta}.
\]

The exact SOAP formulas are

\[
T_M(1)=1+\frac{\lambda V}{2\beta},
\qquad
T_M(b)=b+\frac{\lambda V}{2\beta},
\]

\[
T_M(b+d)=W_\infty+\frac{b+d}{\beta},
\tag{10}
\]

and

\[
T_G(1)=1+W_h,
\qquad
T_G(b)=b+W_h,
\]

\[
T_G(b+d)=W_\infty+\frac{b+d-h}{\beta}+h.
\tag{11}
\]

Averaging gives the exact additive penalty

\[
\boxed{
D:=E[T_M]-E[T_G]
=
\frac{\lambda r\mu^2}{2(1-r)(1-\lambda\mu)}.
}
\tag{12}
\]

Stability gives `1-lambda mu>lambda r d`, hence

\[
D<\frac{\mu^2}{2(1-r)d}<\frac\mu2,
\]

where the last inequality uses `d>h=mu/(1-r)`. Since `E[T_G]>=E[X]=m>mu`,

\[
\boxed{E[T_M]/E[T_G]<3/2.}
\tag{13}
\]

## 4. Delta<0, internal-switch cell: `d0<d<=d1`

This is the topology in which M-SERPT has one age-one demotion, Gittins has a genuine age-one hill, and the two Gittins candidates in `[1,b)` cross internally at

\[
a_*=b-\frac{qd}{t}.
\tag{14}
\]

Put `alpha=1-lambda`. The M-SERPT conditional responses are

\[
T_M(1)=1+\frac{\lambda}{2\alpha},
\qquad
T_M(b)=W_H+\frac b\alpha,
\qquad
T_M(b+d)=W_H+\frac{b+d}\alpha,
\tag{15}
\]

where

\[
W_H=\frac{\lambda M_2}{2(1-\rho)\alpha}.
\]

The Gittins fresh-threshold geometry changes only when the terminal residual crosses `h0=1/p`.

For `d<h0`, let

\[
\ell_0=h_0-\frac{rd}{t},
\qquad z=\frac{qd}{t},
\qquad
C_{0,L}=1+q\ell_0^2+r(h_0+z)^2.
\]

Then

\[
T_G(1)=1+\frac{\lambda C_{0,L}}{2\alpha},
\]

\[
T_G(b)=W_H+\frac{b-\ell_0}{\alpha}+\ell_0,
\]

\[
T_G(b+d)=W_H+\frac{b-\ell_0}{\alpha}+d+\ell_0.
\tag{16L}
\]

For `d>h0`, set

\[
\ell=\frac{q}{pt},
\qquad
C_{0,U}=1+t\ell^2+r h_0^2.
\]

Then

\[
T_G(1)=1+\frac{\lambda C_{0,U}}{2\alpha},
\]

\[
T_G(b)=W_H+\frac{b-\ell}{\alpha}+\ell,
\]

\[
T_G(b+d)=W_H+\frac{b+d-h_0}{\alpha}+h_0.
\tag{16U}
\]

Exact averaging yields

\[
D_L=
\frac{\lambda(t^2-p^2 q r d^2)}{2tp(1-\lambda)}
\qquad(d<h_0),
\]

\[
D_U=
\frac{\lambda(t^2-qr)}{2tp(1-\lambda)}
\qquad(d>h_0).
\]

Thus the entire cell has the single saturated prefix-charge identity

\[
\boxed{
D=
\frac{\lambda}{2tp(1-\lambda)}
\left[t^2-qr\min\{(pd)^2,1\}\right].
}
\tag{17}
\]

The first-demotion condition `d>d0` is exactly `H>h0`, so

\[
m-1=ts+rd>\frac tp.
\]

Stability therefore implies

\[
\frac{\lambda}{1-\lambda}<\frac pt.
\]

Since the bracket in (17) is `<t^2`,

\[
0<D<\frac12.
\]

Since `E[T_G]>=m>1`,

\[
\boxed{E[T_M]/E[T_G]<3/2.}
\tag{18}
\]

Notably, formula (17) is independent of the middle gap `s`; `s` only decides whether the topology exists.

## 5. Delta<0, two-hill far-tail cell: `d>d1`

Here both policies have two demotions, and Gittins has genuine hills at ages `1` and `b`. Put

\[
h_1=\frac{st}{q},
\qquad
\ell=\frac{q}{pt},
\qquad
\alpha=1-\lambda,
\qquad
\beta=1-\lambda\mu.
\]

M-SERPT has

\[
T_M(1)=1+\frac{\lambda}{2\alpha},
\]

\[
T_M(b)=\frac b\alpha+\frac{\lambda V}{2\alpha\beta},
\]

\[
T_M(b+d)=W_\infty+\frac{b+d}{\beta}.
\tag{19}
\]

Gittins has

\[
T_G(1)=1+
\frac{\lambda(1+t\ell^2+r h_0^2)}{2\alpha},
\]

\[
T_G(b)=
\frac{\lambda(V+r h_1^2)}{2\alpha\beta}
+\frac{b-\ell}{\alpha}+\ell,
\]

\[
T_G(b+d)=W_\infty+
\frac{b+d-h_1}{\beta}
+\frac{h_1-h_0}{\alpha}+h_0.
\tag{20}
\]

Averaging gives the exact tail-location cancellation

\[
\boxed{
D=
\frac{\lambda}{2(1-\lambda)}
\left[
\frac{q^2+rt}{pt}
+
\frac{r s^2 t^2}{q(1-\lambda\mu)}
\right],
}
\tag{21}
\]

which contains no `d`.

Set

\[
m_*=1+\frac{s t^2}{q}.
\]

Because `d>d1=st/q`, we have `m>m_*`, so stability implies `lambda<1/m_*`. The right side of (21) is increasing in `lambda`; evaluate it at `lambda_*=1/m_*`. Since

\[
\frac{\lambda_*}{1-\lambda_*}=\frac{q}{s t^2},
\]

and

\[
1-\lambda_*\mu=\frac{s t r}{q m_*},
\]

we obtain

\[
D< D_*=
\frac{q}{2s t^2}\frac{q^2+rt}{pt}
+\frac{q m_*}{2t}.
\tag{22}
\]

Now `q^2+rt=t^2-qr<t^2`, while `Delta<0` means `pst>q`. Therefore

\[
\frac{q}{s t^2}\frac{q^2+rt}{pt}
<\frac{q}{pst}<1.
\]

Hence the first term in (22) is `<1/2`, and the second is `<m_*/2`. Since `m_*>1`,

\[
D<m_*<m\le E[T_G].
\]

Thus

\[
\boxed{E[T_M]/E[T_G]<2.}
\tag{23}
\]

This proof replaces the earlier fixed-middle-gap Bernstein argument by a direct stability estimate valid for arbitrary `s`.

## 6. Delta>=0, one-hill far-tail cell: `d>d0`

This is the only cell requiring an exact compact semialgebraic certificate. M-SERPT has two demotions; Gittins has no age-one hill and one terminal hill. With the same `alpha,beta,V,W_h,W_infty`, the exact responses are

\[
T_M(1)=1+\frac{\lambda}{2\alpha},
\]

\[
T_M(b)=\frac b\alpha+\frac{\lambda V}{2\alpha\beta},
\]

\[
T_M(b+d)=W_\infty+\frac{b+d}{\beta},
\tag{24}
\]

and

\[
T_G(1)=1+W_h,
\qquad
T_G(b)=b+W_h,
\]

\[
T_G(b+d)=W_\infty+\frac{b+d-h}{\beta}+h.
\tag{25}
\]

Consequently

\[
D=
 p\left(\frac{\lambda}{2\alpha}-W_h\right)
+q\left(\frac{\lambda b}{\alpha}
+\frac{\lambda V}{2\alpha\beta}-W_h\right)
+r\frac{\lambda\mu h}{\beta},
\tag{26}
\]

so

\[
\boxed{\partial_d D=0.}
\tag{27}
\]

For the factor-two slack `F=2E[T_G]-E[T_M]=E[T_G]-D`, exact differentiation gives

\[
\boxed{
F'(d)=r\left[
\frac{\lambda}{2\beta}
\left(
\frac{2r(b+d)}{1-\rho}
+
\frac{\lambda rM_2}{(1-\rho)^2}
\right)
+\frac1\beta
\right]>0.
}
\tag{28}
\]

Thus it suffices to prove `F>0` at the one-sided contact boundary `d=d0`, where `m=1/p`.

Parameterize the entire `Delta>=0` mass-gap region by

\[
p=1-T,
\qquad r=T V_0,
\qquad q=T(1-V_0),
\]

\[
s=\frac{U(1-V_0)}{1-T},
\qquad 0<T,V_0,U<1,
\]

and write

\[
\lambda=X(1-T),\qquad 0<X<1.
\]

Here `U<=1` is exactly `Delta>=0`. At contact,

\[
d_0=\frac{1-U(1-V_0)}{(1-T)V_0},
\qquad
\rho=X.
\]

Exact simplification gives

\[
F_0=\frac{P(T,V_0,U,X)}{
2(1-T)(1-X)(1-TV_0)
[1-X(1-T)]
[1-X(1-T)\mu]
},
\tag{29}
\]

where the denominator is strictly positive on the open cube and `P` has multidegree

\[
(5,4,2,3).
\]

The exact tensor-product Bernstein expansion of `P` on `[0,1]^4` has

- `360` coefficients total,
- `293` strictly positive,
- `67` zero,
- `0` negative,
- smallest positive coefficient `1/40`.

Every Bernstein basis function is strictly positive in the open cube, so `P>0` there. Hence `F_0>0`, and (28) yields `F(d)>0` for every `d>d0`. Therefore

\[
\boxed{E[T_M]/E[T_G]<2}
\tag{30}
\]

throughout the final topology.

The exact certificate generating (17), (21), (27), (28), and all 360 Bernstein coefficients is

`research7_2026-09-17/R7-04/artifacts/2026-09-20/2026-09-20T022700Z__P0434_arbitrary_threepoint_certificate.py`.

Its archived output ends with `ALL_EXACT_CHECKS_PASS` and reports `293` positive, `67` zero, `0` negative Bernstein coefficients.

## 7. Exhaustion of all three-point laws

The ordering identities (7)--(8) give the exact partition.

If `Delta>=0`:

1. `d<=h`: neutral / FCFS, ratio `1`;
2. `h<d<=d0`: terminal-only theorem, ratio `<3/2`;
3. `d>d0`: one-hill far-tail theorem, ratio `<2`.

If `Delta<0`:

1. `0<d<=d0` when nonempty: neutral / FCFS, ratio `1`;
2. `d0<d<=d1`: internal-switch theorem, ratio `<3/2`;
3. `d>d1`: two-hill far-tail theorem, ratio `<2`.

Equality surfaces are covered directly by the adjacent formulas or by continuity at finite stable parameters. Thus every positive three-point service law is covered.

## 8. Structural consequence for the arbitrary-law proof

The three-point theorem makes the finite-law mechanism more precise.

1. The additive penalty `D=E[T_M]-E[T_G]` is often **independent of the far-tail location** once the relevant rank topology is fixed.
2. In the internal-switch cell, outward tail motion **decreases** the prefix charge until fresh-rank contact and then the charge saturates:

\[
D=
\frac{\lambda}{2tp(1-\lambda)}
\left[t^2-qr\min\{(pd)^2,1\}\right].
\]

3. In the one-hill far-tail cell, `D` is constant while the factor-two slack `F` is strictly increasing in the tail location, so the hardest configuration is exactly the **envelope-contact boundary**.
4. In the two-hill far-tail cell, the same tail-location cancellation persists, and stability alone controls the remaining prefix charge.

Thus a source-valid counterexample to Conjecture 8.1, if one exists, must have at least four positive support points. More importantly for P01-B, an extremal-measure reduction showing that the worst factor-two slack occurs on at most three support points would now close the full conjecture immediately. The finite-law evidence favors a **prefix-credit plus envelope-contact transport** principle rather than a valleywise nonnegative charge.

## Status

**PROVED PARTIAL** relative to the full source conjecture: complete for all service laws with at most three positive support points, every stable load. The full arbitrary-law factor-two statement remains open in this project and the fixed source interval `[2,5]` is unchanged.
