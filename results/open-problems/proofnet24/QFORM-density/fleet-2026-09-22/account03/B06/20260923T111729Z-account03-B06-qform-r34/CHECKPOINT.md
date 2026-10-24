# Early substantive checkpoint — opposite-sign semi-aligned two-sheet kernel

Status: supporting theorem in progress; full QFORM remains open.

## Source premises actually used

1. account02/B16 r11 (`proofnet24/QFORM-density/fleet-2026-09-22/account02/B16/20260923T082859Z-account02-B16-QFORM-r11/REPORT.md`): for `delta beta >= 0`, the semi-aligned source-scalar/square transducer keeps an original independent scalar through the half-Riesz kernel. I attack the complementary sign `delta beta < 0` rather than reprove it.
2. Newest Claude `COUNTEREXAMPLE_SEARCH.md`, Theorem C: a target-valid rank-three signature `(+, +, -)` form with all three spectral moduli at least one has `p(s) <= pi sqrt(2)` on its one-sheet side `s>=0`; product-projection line marginals, not rotated independence, are used.

## New two-sheet estimate

Let `(H,U)` be arbitrary. Let `X,V,(H,U)` be mutually independent source objects. Assume

`||p_X||_inf <= L_X`, `||p_U||_inf <= L_U`, `||p_V||_inf <= L_V`.

Let `gamma,k,beta,delta` be nonzero with `delta beta < 0`, put

`Y = gamma X + H`,
`Q = delta Y^2 + 2 k U Y + beta V^2`.

Reflect `Q` if necessary, so `beta>0` and `delta=-a<0`. For every `s<0`, writing

`W=-aY^2+2kUY`,

the square-density envelope gives

`p_Q(s) <= L_V beta^(-1/2) E[(s-W)_+^(-1/2)]`.                      (1)

Condition on `(H,U)=(h,u)`. Then `Y=gamma X+h` has a density cap

`L_Y=L_X/|gamma|`,                                                   (2)

with no claim on `U|H`. Completing the deterministic quadratic,

`W=-a(Y-ku/a)^2 + k^2u^2/a`.                                       (3)

Since `s<0`, define

`R = k^2u^2/a - s > 0`.

For

`K(y)=(a(y-ku/a)^2-R)_+^(-1/2)`,

the superlevel set `K>lambda` is two short shells and has exact total length

`2 a^(-1/2) [sqrt(R+lambda^(-2))-sqrt(R)]`

and therefore

`|{K>lambda}| <= [sqrt(a R) lambda^2]^(-1)`.                       (4)

Layer cake using only the cap (2) and probability normalization gives

`E[K(Y)|H=h,U=u]`
` <= int_0^inf min(1, L_Y/(sqrt(aR) lambda^2)) d lambda`
` = 2 sqrt(L_Y) a^(-1/4) R^(-1/4)`.                               (5)

Because `R >= k^2u^2/a`,

`a^(-1/4)R^(-1/4) <= |k|^(-1/2)|u|^(-1/2)`.                       (6)

The sharp cap-one-dimensional bathtub estimate is

`E|U|^(-1/2) <= 2 sqrt(2 L_U)`.                                    (7)

Averaging (5)-(7) and inserting into (1) yields the new bound

`p_Q(s) <= 4 sqrt(2) L_V sqrt( L_X L_U / |beta gamma k| )`,         (8)

for the entire two-sheet side `s beta<0` in invariant sign notation. Crucially, the constant is UNIFORM as `delta -> 0` through the opposite-sign side. Dependence between `H` and `U` is arbitrary; no conditional cap for `U|H` is used.

## Target-valid sign-opposite near-coloop family

Let `c in (0,1)`, `a0=1-c`, take even `m` and balanced `epsilon_j in {+1,-1}`, and define disjoint-source projections

`T=m^(-1/2) sum X_j`, `U=m^(-1/2) sum epsilon_j X_j`, `V=m^(-1/2) sum Z_j`.

For `eta>=0`, set

`Y=sqrt(c)X_0+sqrt(a0)T`,
`Q_{c,-eta}= -eta Y^2 + 2 sqrt(1+eta) UY + V^2`.                    (9)

The deterministic 3x3 spectral matrix is

`B_eta=[[-eta,sqrt(1+eta),0],[sqrt(1+eta),0,0],[0,0,1]]`,

with eigenvalues exactly

`{1,-(1+eta),1}`.                                                    (10)

Thus all three spectral moduli are at least one. The projection-density theorem gives `L_U,L_V<=sqrt(2)`, and (8) gives on `s<0`

`p(s) <= 2^(13/4) [c(1+eta)]^(-1/4)`.                              (11)

For the near-coloop chamber `c>63/64`, this is `<9.552`.

On `s>=0`, the newest Claude ruled one-sheet theorem applies directly to the actual signature `(+, +, -)` form (10) and gives

`p(s) <= pi sqrt(2) < 4.443`.                                      (12)

Therefore the entire target-valid sign-opposite family (9) has

`||p||_inf < 9.552` for `c>63/64`, uniformly in `eta>=0`, including `eta downarrow0` from the previously uncovered sign side.

Remaining gap: this does not yet handle the generic case where the final square variable shares source coordinates with the dependent pair, or a non-semi-aligned higher-rank ambient tail. Those remain target-level debts.
