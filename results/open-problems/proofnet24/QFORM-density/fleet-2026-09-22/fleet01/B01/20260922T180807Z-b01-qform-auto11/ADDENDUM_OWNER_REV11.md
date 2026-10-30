SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), slot B01, 2026-09-22T18:08:07Z.
attacking: test the revision-2026-09-22.11 scalar-conditioning reduction `sup_b ||p_{Q3|Q'=b}||_infinity` before using it in the full proof.

# Addendum — the scalar-conditioning supremum route is false


`M = sup_b ||p_{Q3 | Q'=b}||_infinity`

as the next full-target route. The exact example below shows that this new supremum is also not uniformly bounded. The failure already occurs for four iid uniform physical coordinates and a fixed positive-definite matrix with four distinct eigenvalues. The full output density is nevertheless bounded. Thus the scalar conditional identity is valid, but taking a supremum over the conditioning value is too lossy.

## 1. Fixed target-valid example with simple spectrum

Let `X_1,...,X_4` be iid `Uniform[-1/2,1/2]`. Let

`u_1=(1,1,-1,-1)/2`,
`u_2=(1,-1,1,-1)/2`,
`u_3=(1,-1,-1,1)/2`,
`u_4=(1,1,1,1)/2`.

These are an orthonormal basis. Put

`A = 1*u_1u_1^T + 2*u_2u_2^T + 3*u_3u_3^T + 4*u_4u_4^T`.

The spectrum is the simple spectrum `{1,2,3,4}`, so there is no repeated-eigenvalue choice behind the decomposition. Write `Y_j=<u_j,X>` and split

`Q_3 = Y_1^2+2Y_2^2+3Y_3^2`,
`Q'  = 4Y_4^2`,
`Q=Q_3+Q'`.

This matrix satisfies the owner target with four eigenvalues of modulus at least one.

## 2. Exact corner slice

Fix `s in (1/2,1)` and condition on `Y_4=s`. Write

`X_i=1/2-z_i`.

Since `Y_4=(X_1+...+X_4)/2`, the constraint is

`z_i>=0`, `sum_i z_i = delta := 2(1-s)`.

Because `delta<1`, the lower cube faces impose no further restriction. Hence, under the conditional law, `w_i=z_i/delta` is uniform on the standard three-dimensional simplex

`Delta_3={w_i>=0, sum_i w_i=1}`.

For `j<=3`, `u_j` is orthogonal to `(1,1,1,1)`, so

`Y_j = -delta <u_j,w>`.

Therefore

`Q_3 | (Y_4=s) = delta^2 V(w)`,
`V(w)=<u_1,w>^2+2<u_2,w>^2+3<u_3,w>^2`.                         (2.1)

Since every coordinate of each `u_j` has absolute value `1/2` and `w` is a probability vector,

`|<u_j,w>|<=1/2`.

Thus

`0 <= V(w) <= (1+2+3)/4 = 3/2`.                                (2.2)

For each fixed interior `s`, the pushforward in (2.1) has an absolutely continuous density (coarea on the three-dimensional simplex; the nonconstant quadratic has a critical set of zero three-dimensional measure). Its support has length at most `(3/2)delta^2`. Any probability density on an interval of length at most this value has essential supremum at least the reciprocal length. Hence

`||p_{Q_3 | Y_4=s}||_infinity >= 2/(3 delta^2)
 = 1/[6(1-s)^2].`                                               (2.3)

This diverges as `s ↑ 1`.

## 3. Passing from `Y_4=s` to the proposed scalar `Q'=b`

For `b in (1,4)`, conditioning on `Q'=b` is conditioning on

`Y_4 = +/- sqrt(b)/2`.

The cube law is invariant under `X -> -X`, and `Q_3` is even, so the two conditional laws of `Q_3` are identical. Thus with `s=sqrt(b)/2`,

`p_{Q_3 | Q'=b} = p_{Q_3 | Y_4=s}`

and (2.3) gives

`boxed( ||p_{Q_3 | Q'=b}||_infinity >= 1/[6(1-sqrt(b)/2)^2] )`.   (3.1)

Consequently

`boxed( sup_b ||p_{Q_3 | Q'=b}||_infinity = infinity )`.          (3.2)

This directly refutes the proposed uniform scalar-conditioning supremum bound.

## 4. The full quadratic-form density is bounded in the same example

This is not a QFORM counterexample. In fact `A` is positive definite with `det A=24`. Since the physical density is at most one, for `t>=0` and `h>0`,

`P(t <= X^TAX <= t+h)`
`<= Leb{x in R^4: t <= x^T A x <= t+h}`
`= (pi^2/2)/sqrt(24) * [(t+h)^2-t^2]`.

On the support cube, `X^TAX <= ||A|| ||X||^2 <=4`. Taking the derivative in `h` gives the crude but finite density bound

`||p_Q||_infinity <= 4 pi^2/sqrt(24) < 8.06`.                    (4.1)

So the unconditional output is harmless while the conditional supremum in (3.2) is infinite.

## 5. Exact lesson

The identity

`p_Q(y)=E_{Q'}[p_{Q_3|Q'}(y-Q')]`

is valid, but replacing the average by `sup_b ||p_{Q_3|Q'=b}||_infinity` throws away the probability weight of the rare near-corner levels `Q'≈4`. The correct scalar-conditioned currency must remain **averaged in `b`**, with the shift `y-b` retained. A plausible next object is a weighted/distribution-function estimate of the form

`sup_y int p_{Q'}(b) p_{Q_3|Q'=b}(y-b) db`,

controlled directly without taking a conditional `L^infinity` supremum. This is exactly analogous to why the earlier vector-section normalization failed.

## 6. Interaction with the other result from this run

The main report in this run also closes fleet03/B07's six-coordinate O0 collar: if its disjoint physical triples `H,T` satisfy `|det A[H,T]|>=1/256`, the completed B01 random-slope theorem gives

`||p_Q||_infinity <=3*256^(1/3)<19.049`

with a continuous density. That remains valid under revision `.11`; it is an integrated random-slope result in a quantified structural branch, not a universal `L^1`-Fourier claim.

## 7. Status

- `QFORM-SCALAR-CONDITIONAL-SUP-UNIFORM-v1`: **REFUTED INTERMEDIATE ROUTE** by the exact fixed four-dimensional example above.
- `QFORM-O0-THREE-BY-THREE-CROSS-COLLAR-PAYMENT-v1`: **PROVED** in the main report.
- Full QFORM: **OPEN**.
- Full continuity: **OPEN**.
