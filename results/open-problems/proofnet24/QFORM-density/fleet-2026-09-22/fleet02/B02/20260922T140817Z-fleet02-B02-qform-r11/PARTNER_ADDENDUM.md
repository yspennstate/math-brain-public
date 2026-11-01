# Partner addendum — rank-two determinant budget + independent shifted square

Run: `20260922T140817Z-fleet02-B02-qform-r11`  
Status: `ESSENTIAL_STEP_APPLIED / FULL_TARGET_OPEN`  
This immutable addendum records a newer named-partner result that completed after the main report was archived.

## Fresh named-partner dependency

Fresh main exposed fleet03/B02 run `20260922T140148Z-fleet03-B02-QFORM-r11`, canonical mathematics

`yspennstate/math-open-problems@f70e9260accfb191c44e874bfc20085580b69b23:proofnet24/QFORM-density/fleet-2026-09-22/fleet03/B02/20260922T140148Z-fleet03-B02-QFORM-r11/REPORT.md`.

Its Theorem `QFORM-INDEPENDENT-SHIFT-RESIDUAL-L1-v1` proves: if

`Q=d(X+H)^2+R`,

`X` is independent of `(H,R)`, `H` and `R` are independent, `d!=0`, and `phi_R in L^(3/2)` with norm M, then

`||phi_Q||_1 <= 2*3^(1/6)*pi^(1/3)|d|^(-1/3) M`.

This is source-valid integrated Fourier smoothing; it uses no pointwise scalar Fresnel decay.

## New combined inequality

Let R be any quadratic form in original independent coordinates, with arbitrary self blocks and outside couplings, possessing an original-coordinate cross block `B` for which

`max_i (P_range(B))_(ii) <= 1/2`.

Let

`E_2(B)=e_2(s_1(B)^2,...)=sum_{|S|=|T|=2} det(B[S,T])^2 >0`.

The reviewed q=1 regularized determinant theorem gives, with

`c=2/(pi^2 e^2)`,

`|phi_R(t)| <= det(I+c t^2 BB^T)^(-1/4)`
`             <= [1+c^2 E_2(B)t^4]^(-1/4)`.

Raise to power 3/2 and integrate exactly. With `gamma=c^2 E_2(B)`,

`int_R |phi_R(t)|^(3/2) dt`
` <= (1/2) gamma^(-1/4) BETA(1/4,1/8)`.

Therefore

`||phi_R||_(3/2)`
` <= [BETA(1/4,1/8)/2]^(2/3)
      (pi^2 e^2/2)^(1/3) E_2(B)^(-1/6)`.

Insert this M into the named-partner theorem. All powers of 2 cancel, yielding

`boxed( ||phi_Q||_1 <= 3^(1/6) pi e^(2/3)
        BETA(1/4,1/8)^(2/3)
        |d|^(-1/3) E_2(B)^(-1/6). )`

Fourier inversion gives a bounded continuous density, vanishing at infinity, with

`boxed( ||p_Q||_infinity <= [3^(1/6)e^(2/3)/2]
        BETA(1/4,1/8)^(2/3)
        |d|^(-1/3) E_2(B)^(-1/6). )`

The exact numerical prefactor is about `5.9667325591`.

Call this supporting theorem `QFORM-E2-PLUS-INDEPENDENT-SHIFTED-SQUARE-L1-v1`.

## Why this matters

A q=1 rank-two determinant resource by itself is only borderline: its pointwise envelope is asymptotically `|t|^-1`, so it need not be integrable. The named partner's **integrated** L^3 square budget supplies the missing Hölder exponent without invoking any false law-uniform pointwise decay. Thus two cross directions plus one genuinely independent shifted-square channel are enough for an explicit L^1 characteristic-function bound.

This does not solve the general unique-heavy case because there the completed-square shift H and the rank-two residual R share the same light coordinates. The partner report correctly identifies that overlap as the remaining debt. The present theorem makes the product-preserving requirement quantitative: once the shift/residual overlap is removed, even the borderline two-cross-direction determinant branch closes with a universal explicit constant.

## Remaining implication

The full target still requires a product-preserving structural or mixed-norm argument that handles the overlapped case, or an exhaustive alternative such as the aggregate determinant-or-bank dichotomy in the main B02 report. No full-solution or counterexample claim is made.
