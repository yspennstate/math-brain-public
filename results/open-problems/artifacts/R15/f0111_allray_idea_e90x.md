# R15 F0111 idea before checking — replace subset faces by every nonnegative ray

Date: 2026-09-19 UTC.

Status at creation: IDEA ONLY / UNCHECKED / SELF-CHECK-ONLY. This does not reopen retired I0076 and is not a Talagrand claim.

The preceding R15 run solved the exact quadratic majorant cone on equal-coordinate subset rays. The next route is to ask whether the one-variable structure survives for an arbitrary nonnegative direction `c`.

For

`F(t)=sum_i t_i-log(sum_i exp(t_i)-(n-1))`

and positive active coordinates `c_i`, set

`f_c(s)=F(s c)`, `g_c(s)=f_c(s)/s`, `L_c(s)=log(sum_i exp(s c_i)-(m-1))`.

Then `g_c(s)=sum_i c_i-L_c(s)/s`. The candidate strengthening is:

> `L_c(s)/s` is strictly convex on `(0,infinity)` whenever at least two `c_i` are positive; equivalently `g_c` is strictly concave.

A dimensionless form may make this provable. Put `z_i=s c_i`,

`T=sum_i exp(z_i)-(m-1)`, `r_i=exp(z_i)/T`,
`M1=sum_i r_i z_i`, `M2=sum_i r_i z_i^2`,

and

`K(z)=2 log T-2 M1+M2-M1^2`.

Direct differentiation should give

`s^3 d^2/ds^2 [L_c(s)/s] = K(s c)`.

The proposed proof of `K>=0` is extremal rather than another Taylor estimate:

1. Boundary: if one `z_i=0`, deleting that coordinate leaves `T,M1,M2,K` unchanged, so induct on the number of active coordinates.
2. Infinity: after subtracting `M=max z_i`, the limit of `K` should be `Var_p(offset)+2 H(p)>=0` on the surviving top coordinates.
3. Interior: compute `partial_i K`. The hoped-for factorization is `r_i Q(z_i)` with one quadratic `Q`; an interior negative minimizer would force every coordinate to be one of at most two roots. The all-equal and two-root cases may then contradict `sum_i r_i>1`, the distinctive signed-normalization feature caused by `-(m-1)` in `T`.

If this works, it has two consequences worth pursuing before any code:

- **Every-ray exact cone:** for every nonnegative `c`, a quadratic restriction `A s+B s^2` majorizes `f_c` iff `A>=Phi_c(B):=sup_s(g_c(s)-Bs)`, with a unique tangent point for interior slopes.
- **Radial saturation:** at an exact interior contact `q`, value plus gradient contact force the radial coefficients to be precisely the tangent line to `g_q` at `s=1`. Strict concavity would then prove the radial ray is automatically globally safe and cannot be the source of certificate failure. The next obstruction must be genuinely nonradial.

Section-B moves in new roles: **#18 SAY IT IN ANOTHER LANGUAGE** (dimensionless moment functional `K`), **#20 FIND WHY THE ALGORITHM FAILS** (prove radial testing is automatically safe), **#27 SWAP THE QUANTIFIERS** (replace finitely many subset rays by one theorem for every nonnegative ray). All 30 method numbers have already appeared somewhere in the retained F0111 history, so this is a nonconsecutive reuse, not a claim that these numbers are globally new.
