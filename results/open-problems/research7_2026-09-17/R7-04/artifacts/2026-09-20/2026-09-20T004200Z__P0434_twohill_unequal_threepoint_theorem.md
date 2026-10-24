Model actually running: **GPT-5.6 Sol. Reasoning level: UNVERIFIED** — GPT-6 maximum is the requested preference, but this runtime exposes no authenticated binding model/effort telemetry.

# P0434 / P01-A — complete two-Gittins-hill unequal-mass three-point cell

## Source and scope

Source: Ziv Scully, Mor Harchol-Balter, Alan Scheller-Wolf, *Simple Near-Optimal Scheduling for the M/G/1* (2020), Conjecture 8.1, arXiv:1907.10792, DOI 10.1145/3379477.

This artifact proves the factor-two inequality on a new full-dimensional unequal-mass three-point rank cell. It is a **PROVED PARTIAL** result, not a proof of Conjecture 8.1 for arbitrary service laws.

We use the exact SOAP mean-response theorem of Scully--Harchol-Balter--Scheller-Wolf (2018): if `r` is the tagged job's worst future rank at arrival and `r(a)` its worst future rank at age `a`, then

\[
E[T_x]=
\frac{\lambda\sum_i E[(X_i^{\rm old}[r])^2]}
{2(1-\rho_0^{\rm old}[r])(1-\rho^{\rm new}[r])}
+
\int_0^x\frac{da}{1-\rho^{\rm new}[r(a)]}.
\]

## The three-point family and cell

Let

\[
X\in\{1,2,2+d\},
\qquad
P(X=1)=p,\quad P(X=2)=q,\quad P(X=2+d)=r,
\]

with `p,q,r>0`, `p+q+r=1`. Put

\[
t=q+r=1-p,\qquad \mu=2-p=1+t,\qquad m=EX=\mu+rd.
\]

Assume the neighboring cell

\[
\boxed{r>t^2,\qquad d>\frac{t}{q}.}
\tag{C}
\]

Define

\[
h_0=\frac1p,\qquad h_1=\frac tq,\qquad
\ell=\frac{q}{pt},
\]

so `(C)` gives

\[
0<\ell<1,\qquad h_0<h_1<d.
\]

Indeed

\[
h_1-h_0=\frac{r-t^2}{p q}>0.
\]

## Exact rank topology

### M-SERPT

The three M-SERPT plateau levels are

\[
M_0=m,\qquad
M_1=1+\frac{rd}{t},\qquad
M_2=d.
\]

The two differences are

\[
M_1-M_0=\frac{prd-t^2}{t}>0,
\]

and

\[
M_2-M_1=\frac{qd-t}{t}>0.
\]

The first inequality follows because `d>t/q` and `r>t^2`; the second is exactly `d>t/q`. Thus M-SERPT has two strict demotions:

\[
[0,1):m,\qquad [1,2):M_1,\qquad [2,2+d):d.
\]

### Gittins

Before age `1`, the three stopping candidates are

\[
A_1(a)=\frac{1-a}{p},\qquad
A_2(a)=\frac{\mu-a}{1-r},\qquad
A_3(a)=m-a.
\]

Condition `r>t^2` gives `A_1(0)<A_2(0)`, while `d>t/q>t^2/(pr)` gives `A_1(0)<A_3(0)`. Since `A_1` has the most negative slope, it remains the lower envelope on `[0,1)`.

On `[1,2)`, the candidates are

\[
B_1(a)=\frac{t(2-a)}q,\qquad
B_2(a)=(2-a)+\frac{rd}{t}.
\]

At age `1`,

\[
B_2(1)-B_1(1)=r\left(\frac d t-\frac1q\right)>0,
\]

and `B_1` decreases faster, so `B_1` is the lower envelope throughout `[1,2)`.

After age `2`, the size is known and the rank is deterministic residual service. Hence

\[
\boxed{
r_G(a)=
\begin{cases}
(1-a)/p,&0\le a<1,\\[2mm]
t(2-a)/q,&1\le a<2,\\[2mm]
2+d-a,&2\le a<2+d.
\end{cases}}
\tag{1}
\]

The jumps at `1` and `2` have heights `h_1` and `d`, with

\[
h_0<h_1<d.
\]

Thus this is genuinely a **two-Gittins-hill** cell, unlike the one-hill cell proved in the preceding R7-04 report.

## Exact SOAP response formulas

Write

\[
\alpha=1-\lambda,\qquad
\beta=1-\lambda\mu,\qquad
\rho=\lambda m<1,
\]

\[
V=p+4(q+r)=4-3p,
\qquad
M_2^{(2)}=E[X^2]=p+4q+r(2+d)^2,
\]

and

\[
W_\infty=
\frac{\lambda M_2^{(2)}}{2(1-\rho)\beta}.
\]

### M-SERPT

Direct SOAP evaluation gives

\[
\boxed{T_M(1)=1+\frac{\lambda}{2\alpha},}
\tag{2}
\]

\[
\boxed{T_M(2)=
\frac2\alpha+
\frac{\lambda V}{2\alpha\beta},}
\tag{3}
\]

and

\[
\boxed{T_M(2+d)=W_\infty+\frac{2+d}{\beta}.}
\tag{4}
\]

### Gittins, size 1

At threshold `h_0`, a new job has zero strict `h_0`-work. An old job has:

- an original interval of length `1` always;
- a first recycled interval of length `ell=q/(pt)` with probability `t`;
- a terminal recycled interval of length `h_0` with probability `r`.

Therefore

\[
C_0=1+t\ell^2+r h_0^2,
\]

and

\[
\boxed{T_G(1)=1+\frac{\lambda C_0}{2\alpha}.}
\tag{5}
\]

### Gittins, size 2

Its arrival worst-future rank is `h_1`. New `h_1`-work is exactly one unit, while old original `h_1`-work is `min(X,2)` and a long old job contributes one terminal recycled interval of length `h_1`. Thus the waiting term is

\[
W_1=
\frac{\lambda(V+r h_1^2)}{2\alpha\beta}.
\]

As the tagged size-2 job ages through `[1,2)`, its decreasing rank crosses the fresh rank `h_0` exactly `ell` units before age `2`. Hence

\[
\boxed{
T_G(2)=
W_1+\frac{2-\ell}{\alpha}+\ell.
}
\tag{6}
\]

### Gittins, long job

Its arrival worst-future rank is `d`. At rank `d`, new work is `min(X,2)` and old original work is the whole job, so its waiting term is exactly `W_infinity`.

For its residence term, after age `2` the residual rank descends from `d` to `0`. The new-work load is:

- `lambda mu` while residual rank exceeds `h_1`;
- `lambda` while residual rank lies in `(h_0,h_1]`;
- `0` while residual rank lies in `[0,h_0]`.

Therefore

\[
\boxed{
T_G(2+d)=
W_\infty+
\frac{2+d-h_1}{\beta}
+
\frac{h_1-h_0}{\alpha}
+h_0.
}
\tag{7}
\]

Equations `(2)--(7)` are exact for every stable load in cell `(C)`.

## Structural theorem: tail-location cancellation survives an extra Gittins hill

Let

\[
E_M=pT_M(1)+qT_M(2)+rT_M(2+d),
\]

\[
E_G=pT_G(1)+qT_G(2)+rT_G(2+d),
\]

and define the additive policy gap

\[
D=E_M-E_G.
\]

The size-specific differences from `(2)--(7)` simplify to

\[
T_M(1)-T_G(1)
=-\frac{\lambda}{2\alpha}
\left(t\ell^2+r h_0^2\right),
\]

\[
T_M(2)-T_G(2)
=
\frac{\lambda}{\alpha}
\left(\ell-\frac{r h_1^2}{2\beta}\right),
\]

and

\[
T_M(2+d)-T_G(2+d)
=
\frac{\lambda}{\alpha}
\left(h_0+\frac{t h_1}{\beta}\right).
\]

Using `ell*h_1=h_0`, averaging yields the compact identity

\[
\boxed{
D=
\frac{\lambda}{2\alpha}
\left[
\frac{q^2+rt}{pt}
+
\frac{rt^2}{q\beta}
\right].
}
\tag{8}
\]

In particular,

\[
\boxed{\frac{\partial D}{\partial d}=0.}
\tag{9}
\]

This extends the preceding R7-04 tail-location cancellation from a one-Gittins-hill cell to a genuinely **two-Gittins-hill** cell. The cancellation is therefore not an artifact of having only one Gittins valley.

## Monotone reduction to the hill-contact boundary

Put

\[
F(d)=2E_G-E_M=E_G-D.
\]

Since `D` is independent of `d`, only the long-job Gittins term contributes to `F'(d)`. Exact differentiation gives

\[
\boxed{
F'(d)=
r\left[
\frac{\lambda}{2\beta}
\left(
\frac{2r(2+d)}{1-\rho}
+
\frac{\lambda rM_2^{(2)}}{(1-\rho)^2}
\right)
+
\frac1\beta
\right]>0.
}
\tag{10}
\]

Hence the hardest point in the entire continuum `d>t/q` is the one-sided contact boundary

\[
\boxed{d_0=\frac tq.}
\tag{11}
\]

This is precisely where the second-stage Gittins candidates `B_1` and `B_2` make contact at age `1`.

## Exact factor-two certificate on the contact boundary

Rectangularize the mass condition `r>t^2` by

\[
p=1-t,\qquad
r=t^2+u t(1-t),\qquad 0<t,u<1.
\]

Then

\[
q=t(1-t)(1-u),
\qquad
h_1=\frac1{(1-t)(1-u)}.
\]

At the contact boundary `d=h_1`, the mean size is

\[
m_0=
\frac{1-u(1-t)}{(1-t)(1-u)}.
\]

Write the boundary load as

\[
\lambda=\frac{x}{m_0},\qquad 0<x<1,
\]

so `x=rho` at the boundary.

Set

\[
K=1-u(1-t),
\]

\[
A=K-x(1-t)(1-u),
\qquad
B=K-x(1-t)(1-u)(1+t).
\]

Here `A>0` and `B>0`; they are the positive numerators of `alpha` and `beta` under the above substitution.

Exact simplification gives

\[
\boxed{
F_0(t,u,x)=
\frac{Q(t,u,x)}
{2(1-t)(1-u)(1-x)A B},
}
\tag{12}
\]

where `Q` is a polynomial of degree `(6,5,3)` in `(t,u,x)` with 123 nonzero power-basis terms.

The exact tensor-product Bernstein expansion of `Q` over `[0,1]^3` has

\[
168\text{ coefficients}=132\text{ positive}+36\text{ zero}+0\text{ negative},
\]

with smallest strictly positive coefficient

\[
\boxed{1/180.}
\]

Because every Bernstein basis function is strictly positive in the open cube and at least one coefficient is positive,

\[
Q(t,u,x)>0
\qquad (0<t,u,x<1).
\]

Thus `F_0>0`. By `(10)`, every strict cell point `d>t/q` satisfies

\[
F(d)>F_0>0.
\]

Therefore

\[
\boxed{
\frac{E[T_{\rm M\text{-}SERPT}]}{E[T_{\rm Gittins}]}<2
}
\]

for every stable load and every three-point law satisfying `(C)`.

## What this changes

This run solves a second full-dimensional unequal-mass topology:

\[
\boxed{
r>(q+r)^2,\qquad d>\frac{q+r}{q}.}
\]

The previous R7-04 theorem solved

\[
r\le(q+r)^2,\qquad d>\frac{(q+r)^2}{pr}.
\]

Thus the factor-two theorem now covers both sides of the mass bifurcation `r=(q+r)^2` once the far-tail location lies beyond the appropriate final-rank contact threshold.

The unresolved neighboring wedge is now sharply localized to the topology-change region

\[
r>(q+r)^2,\qquad
\frac{(q+r)^2}{pr}<d\le\frac{q+r}{q},
\]

plus the no-first-demotion region `d<= (q+r)^2/(pr)`. In the wedge, the second-stage Gittins lower envelope switches internally between `B_2` and `B_1`, and the long job's worst-future rank is the age-one hill rather than the terminal jump. This is where the simple far-tail cancellation proof must be modified.

## Structural handoff to P01-B

The useful general-proof lesson is stronger than another support-three bound:

> **Two-hill cancellation lemma.** In a finite law where a terminal support point lies strictly beyond all earlier Gittins envelope hills, translating that terminal point farther outward can leave `E[T_MS]-E[T_G]` exactly invariant even when the Gittins rank has multiple earlier hills. Meanwhile `2E[T_G]-E[T_MS]` increases strictly.

The one-hill and two-hill exact identities now give two independent finite-law instances of the same mechanism. This supports a general arbitrary-law strategy in which terminal tail displacement is pushed to envelope-contact boundaries, with cross-hill prefix charge retained rather than requiring nonnegative charge on each individual valley.

## Exact certificate

Exact SymPy certificate:

`research7_2026-09-17/R7-04/artifacts/2026-09-20/2026-09-20T003800Z__P0434_twohill_unequal_threepoint_certificate.py`

Archived output:

`research7_2026-09-17/R7-04/artifacts/2026-09-20/2026-09-20T003800Z__P0434_twohill_unequal_threepoint_certificate.out`

The certificate verifies `(8)`, `(9)`, `(10)`, `(12)`, and the full exact Bernstein sign count. This is exact self-checking of the restricted theorem, not an independent audit and not full-source closure.
