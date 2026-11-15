# Exact rescaling of the simplex kernel

Status: algebraic identity and interval recipe, unaudited.

Set U(a)=exp(-a)T_+(a), jbar(x)=exp(kappa x^2)Jtilde_+(x), s=x^2+y^2, a=2rho xy/d, d=1-rho^2, kappa=rho^2/d. Direct substitution in (148)-(151) gives

A(x,y) sqrt(jbar(x)jbar(y)) = (2/d) exp(-Q0) U(a) - (4j(1)/d) a exp(-Qminus) - 2 exp(-Qc)(ell(x)+ell(y)),

Q0=(x^2+y^2-4rho xy)/(2d), Qminus=(x^2+y^2+4rho xy)/(2d), Qc=(1-kappa)(x^2+y^2)/2.

The identity uses 1+kappa=1/d. Every term refers to the actual centered weighted kernel in CELL_BOUND.md. On rho<1/2, write the numerator of Q0 as (x-y)^2+2(1-2rho)xy. Both summands are nonnegative. Directed bounds on the difference interval, xy, rho and d therefore enclose Q0 without splitting its cancelling quadratic terms. Qminus and Qc use nonnegative interval operations directly.

Each U table leaf is obtained by multiplying the original certified T_+ leaf enclosure by an Arb enclosure of exp(-a) over that same leaf. This is a proved enclosure, not an approximation assumption. Range-min/range-max queries preserve it on arbitrary argument intervals. The exponential table is rebuilt in Arb over a proved domain containing Q0, Qminus and Qc. The source analytic tail is unchanged because the kernel is identical.

The unscaled coarse-table majorants at rho=.42 and .43 gave upper bounds 2.03771 and 2.07069. These failed certificates are not lower bounds or counterexamples. This exact rescaling addresses the interval dependency in exp(-s/(2d))*T_+(a); it does not change the operator or the target.
