# Checks for `QFORM-R46-GLOBAL-FOURSTAR-E3-OR-LATENT8-v1`

All checks below are deterministic consequences of the source-pinned inequalities in `REPORT.md`; they are not an independent audit.

## Constants

`delta=2^-16=0.0000152587890625`.

`eta=2*sqrt(3)*delta=sqrt(3)/32768=0.00005285799583645255...`.

Physical `E_3` receiver constant:

`C_E3=8.45302122552817687470491804598...`.

Therefore the paid star branch satisfies

`C_E3/delta=C_E3*65536=553977.1990362146... <553978`.

Partner strong-cross constant:

`gamma_0=28159/(4194304*sqrt(2))=0.00474725242887306...`.

Hence

`sqrt(gamma_0)=0.06890030790114846...`.

After the global latent-eight compression:

`1/64-eta=0.015572142004163547... >0`,

`sqrt(gamma_0)-eta=0.06884744990531200... >0`,

and their product is

`0.0010721022665500545...`.

The same-bank spectral fork gives

`1/2-eta=0.49994714200416355...`.

## Operator-norm compression identity

For a four-bank vector `x=(x_1,x_2,x_3,x_4)`,

`sum_a ||x_{G_a^c}||^2 = 3 ||x||^2`.

Thus if every star residual after top-two projection is `<delta`,

`||(I-P)S x||^2 < 3 delta^2 ||x||^2`,

so

`||(I-P)S||<sqrt(3)delta`.

Symmetry gives `||S(I-P)||<sqrt(3)delta`, and

`S-PSP=(I-P)S+PS(I-P)`

implies

`||S-PSP||<2sqrt(3)delta=eta`.

No Frobenius-to-operator dimension factor is used.

## Singular-value monotonicity used in the partner application

The global balanced physical block is

`B=[N  A[R,O]]`.

Then

`BB^T = NN^T + A[R,O]A[R,O]^T >= NN^T`

in positive-semidefinite order. Hence every singular value of `B` is at least the corresponding singular value of `N`, in particular

`s_2(B)>=1/64`,

`s_1(B)s_2(B)>gamma_0`.

Since `s_1(B)>=s_2(B)`, the latter implies `s_1(B)>sqrt(gamma_0)`.

The latent balanced block differs from `B` in operator norm by `<eta`, so Weyl yields the stated lower bounds.

## Spectral-fork check

If `s_3(K_8)<1/2`, choose a rank-two singular truncation `K_2` with

`||K_8-K_2||=s_3(K_8)<1/2`.

Since `s_3(A)>=1` and `||E||<eta`,

`s_3(D+K_2)>1/2-eta`.

Because `K_2` itself is a rank-two approximation to `D+K_2`,

`s_3(D+K_2)=dist_op(D+K_2,{rank<=2})<=||D||`.

Therefore `||D||>1/2-eta`. Since `D` is block diagonal, one actual principal same-bank block has that operator norm.

## Scope check

The paid branch uses a literal original-coordinate cross block. The unpaid branch retains the exact original same-bank blocks and a nonzero global operator tail. The bank projections are deterministic coefficient projections; only the four disjoint original-coordinate banks are declared independent. No claim is made that the coordinates inside a projected two-vector are independent.
