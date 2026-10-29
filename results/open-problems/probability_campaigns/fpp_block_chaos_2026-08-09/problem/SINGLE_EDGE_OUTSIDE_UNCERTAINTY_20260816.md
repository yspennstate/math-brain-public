# Single-edge outside variance is sharp threshold uncertainty

Date: 2026-08-16  
Status: exact edge-level identity and sharp comparison proved; independent
audit required before use

Companions:

* `SINGLE_EDGE_TARGET_MASS_DIRECT_20260816.md`, SHA-256
  `4eea505ef965591bf4c06eb03f5915111e745725d7f4423ca26d593d4e39b923`;
* `SINGLE_EDGE_TARGET_MASS_SHARP_MONOTONE_20260816.md`, SHA-256
  `7b3039d5d74283d582bc996333bba27da81bb7569104c592088c06f91f14e68c`
  (independent audit pending).

The target-mass companions control the conditional mean of the positive
resampling increment when the old and replacement values of one edge are
shared.  This note computes the complementary conditional variance exactly.
It is governed by uncertainty in the edge-use threshold after the target value
is fixed.  A second sharp one-dimensional kernel inequality gives the constant
`3/32`.

This is still an edge-coordinate result.  Its final right side is not known to

## 1. Exact target/outside split

Let iid edge weights have density `rho` on `[a,b]`, with

`rho(t)>=alpha>0` almost everywhere.                               (1)

Fix an edge `e`.  Conditional on all other edge weights, write

`T_e=(best avoiding-e cost)-(best through-e cost with w_e removed)`

and let

`q_e(t)=P(T_e>t),`

where this probability averages the outside environment.  If `w_e'` is an
independent replacement and `z_e=(X^e-X)^+`, the direct-target identity is

`z_e=1_(w_e'>w_e) integral_(w_e)^(w_e') 1_(t<T_e)dt.`              (2)

Put `Y_e=(w_e,w_e')`, `m_e(Y_e)=E[z_e|Y_e]`, and

`V_e^out=E[Var(z_e|Y_e)].`                                        (3)

Expanding the two copies of the integral in (2) gives

`E[z_e^2]
 =integral_a^b integral_a^b q_e(max{s,t})
   F(min{s,t})[1-F(max{s,t})]dsdt,`                              (4)

whereas

`E[m_e(Y_e)^2]
 =integral_a^b integral_a^b q_e(s)q_e(t)
   F(min{s,t})[1-F(max{s,t})]dsdt.`                              (5)

Subtracting (5) from (4) is the exact outside variance.  Since `q_e` is
decreasing, the integrand for `s<=t` is

`q_e(t)[1-q_e(s)] F(s)[1-F(t)].`                                (6)

Thus no cancellation or absolute-value estimate has yet been used.

Use the generalized quantile of `F`, put

`q(u)=q_e(F^(-1)(u)),       K(u,v)=min(u,v)-uv,`

and abbreviate `rho_u=rho(F^(-1)(u))`.  Equations (3)--(6) give

`V_e^out
 =2 integral_(0<u<v<1)
   u(1-v) q(v)[1-q(u)]/(rho_u rho_v) du dv.`                    (7)

Since the kernel and every other factor are nonnegative, (1) implies

`V_e^out<=alpha^(-2) J(q),`                                    (8)

where

`J(q)=2 integral_(0<u<v<1)u(1-v)q(v)[1-q(u)]du dv.`            (9)

## 2. Sharp threshold-disagreement lemma

**Lemma.** For every decreasing `q:[0,1]->[0,1]`,

`J(q)<= (3/32) integral_0^1 q(u)[1-q(u)]du.`                  (10)

The constant `3/32` is sharp.

**Proof.** Any such `q` is, up to immaterial endpoint conventions, the
survival function of a random variable `Tau` in `[0,1]`:

`q(u)=P(Tau>u).`

Let `Tau_1,Tau_2` be iid.  Tonelli gives

`integral_0^1q(u)[1-q(u)]du
 =E[(Tau_1-Tau_2)^+].`                                        (11)

Similarly, with

`A(x,y)=integral_x^y integral_u^y u(1-v)dvdu,      x<y,`

equation (9) becomes

`J(q)=E[1_(Tau_2<Tau_1) 2A(Tau_2,Tau_1)].`                   (12)

It remains only to prove the pointwise inequality

`2A(x,y)/(y-x)<=3/32.`                                       (13)

Put `d=y-x`.  Direct integration yields

`2A(x,x+d)/d
 =d x(1-x)+(d^2/3)(1-3x)-d^3/4.`                           (14)

For fixed `d`, the right side is a concave quadratic in `x` on
`[0,1-d]`; its maximum is at `x=(1-d)/2`.  Substitution reduces (14) to

`d/4-d^2/6.`

This quadratic in `d` is maximized on `[0,1]` at `d=3/4`, with value
`3/32`.  Equations (11)--(13) prove (10).

Equality holds when `Tau` is supported on `{1/8,7/8}` with both masses
positive.  Equal pairs contribute zero to both sides of (10), while each
ordered unequal pair attains equality in (13).  Hence the constant is sharp.
QED

Combining (8) and (10) proves

`V_e^out
 <=(3/(32alpha^2)) E[q_e(w_e)(1-q_e(w_e))].`                (15)

Under the atomless law, the canonical geodesic uses `e` exactly when
`w_e<T_e`, up to a null tie event.  Therefore the right side is

`(3/(32alpha^2)) E[Var(1_(e in gamma)|w_e)].`                 (16)

It measures outside route uncertainty after the edge's own weight is fixed.

## 3. Combined edge ledger

Let

`p_e=P(e in gamma),`

`r_e=E[q_e(w_e)(1-q_e(w_e))].`                               (17)

The sharp target-mass companion and (15) give

`E[z_e^2]
 =E[m_e(Y_e)^2]+V_e^out
 <=alpha^(-2)[p_e^2/9+3r_e/32].`                             (18)

The uncertainty term has the exact Bernoulli-ANOVA identities

`r_e=p_e-E[q_e(w_e)^2]
    =p_e(1-p_e)-Var(q_e(w_e)).`                               (19)

Thus it is complementary to the target self-selection mass, rather than a
second copy of it.

Summing (15) over edges gives the edge-coordinate version of the outside mass:

`sum_e V_e^out
 <=(3/(32alpha^2)) sum_e r_e.`                              (20)

This is an exact reduction, not yet a useful passage-scale estimate.  The
trivial bound `r_e<=p_e` makes the right side comparable to expected geodesic
length, which is much larger than the conjectural variance scale.  A successful
use of (20) needs a new aggregate bound on conditional route uncertainty, or a
block analogue that preserves cancellations unavailable edge by edge.

## 4. Break checks and scope

1. If the outside threshold is deterministic, `q` is zero-one valued.  Both
   sides of (10) vanish and `z_e` is determined by `Y_e`, so `V_e^out=0`.
2. If `q` is the constant `c`, direct integration gives
   `J(q)=c(1-c)/12`, below the bound `3c(1-c)/32`.  The constant-function
   check does not determine the sharp constant.
   `3/32` by `1/12` would be false.
4. The two reciprocal densities in (7) each cost `alpha^(-1)`.  No density
   upper bound is used.
5. Equation (18) combines two separately sharp inequalities; it is not claimed
   to be jointly sharp for fixed `(p_e,r_e)`.
6. Neither (15) nor (20) bounds the conditional revealment term in the block
   spectral engine.  They identify its edge-level probabilistic content only.

An independent referee should verify (4)--(7), the pointwise optimization
(13)--(14), and the equality example before this note is used as a dependency.
