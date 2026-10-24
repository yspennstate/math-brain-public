# Prepublication source refresh — latest designated-partner improvement

Fresh source refresh after the main report found a newer completed designated-partner theorem:

`yspennstate/math-open-problems@df738b7f0821d9af56dfd992cab10ecc6704e3fb`

account02/B03, `QFORM-Z3-CROSSING-MARGINAL-FREE-v1`. For every actual physical cross cut with

`Z_3=e_3(A_{L,R}A_{L,R}^T)>0`,

it proves

`||p_Q||_infinity <= C_3^p Z_3^(-1/6)`,
`C_3^p=3*2^(4/3)*e^(1/3)=10.550168831164775...`,

with a continuous density, and the dependence-safe whole-copy estimate

`int |t|^(-1/2)|phi_Q(t)|^2dt
 <= R_3^p Z_3^(-1/12)`,
`R_3^p=(24/5)2^(2/3)sqrt(pi)e^(1/6)=15.954575413555695...`.

This supersedes only the numerical constant used for the disjoint-overlap sector in the main report; the overlap decomposition and all other arguments are unchanged.

Recall the exact random-cut identity proved in the main report:

`E_cut Z_3(A_{L,R})=E_0/64`.

Therefore some actual product-coordinate cut obeys `Z_3>=E_0/64`. Applying the new account02/B03 theorem at this exact inequality gives

`boxed:
 ||p_Q||_infinity
 <= 2 C_3^p E_0^(-1/6)
 =21.10033766232955... E_0^(-1/6).}`

This is the latest designated-partner result applied to an actual target-level inequality. In particular, if `s=s_3(A)` and `E_0>=theta_0 s^6`, then

`||p_Q||_infinity
 <=21.10033766232955... theta_0^(-1/6)s^(-1)`.

At `theta_0=1/4`, the coefficient is

`26.58475958065858...`.

The same cut gives the whole-copy time integral

`boxed:
 int |t|^(-1/2)|phi_Q(t)|^2dt
 <= sqrt(2) R_3^p E_0^(-1/12)
 =22.563176931754793... E_0^(-1/12).}`

The scalar identity `|phi_Q(t)|^2=E exp(it(Q-Q'))` remains intact; no coordinate sum/difference independence is asserted.

The older account02/B03 critical `k=1,ell=1` square theorem at `38920ffa423ec07886112206314249deb7294dd4` is still separately used in Section 5.4 of the main report for the heavy-row subbranch of the one-overlap compiler, where it improves the coefficient to `12.337686603263526... [a^2E_1(h)]^(-1/8)`.

Full QFORM status remains **OPEN**. This refresh adds no new assumption and does not alter the remaining zero/small-diagonal, definite/near-singular-pair, or principal-overlap gaps.
