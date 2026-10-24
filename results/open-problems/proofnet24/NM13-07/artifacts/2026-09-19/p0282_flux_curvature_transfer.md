# P0282 structural follow-up — exact curvature-reserve identity for the insertion flux

Date: 2026-09-19 UTC  
Track: `NM13-07`  
Source: `P0282` — Chen fixed-size LIS log-concavity

The exact validation of the preceding universal-preserver idea found that the actual LIS insertion profile already fails that stronger kernel property at `(n,k)=(4,3)`, even though the source Chen inequality remains positive in row 5. The missing quantity is the strict curvature already present in the incoming row. This note records the exact transfer identity before any further numerical search.

Let

`q_k = a_k p_k + c_{k-1}p_{k-1}`,  with `c_i=1-a_i`,

and fix an interior `k`. Put

`x=p_{k-1}>0`, `y=p_k>0`, `r=y/x`,

`Delta_- = x^2-p_{k-2}y`,

`Delta_+ = y^2-x p_{k+1}`.

For a log-concave input, `Delta_-,Delta_+ >= 0`. Define the geometric-envelope neighbors

`G_- = x(a_{k-1}+c_{k-2}/r)`,

`G_+ = x r(a_{k+1}r+c_k)`,

and the curvature deductions

`U = c_{k-2} Delta_- / y`,

`V = a_{k+1} Delta_+ / x`.

Then the outer input identities

`p_{k-2}=x/r-Delta_-/y`,

`p_{k+1}=yr-Delta_+/x`

give immediately

`q_{k-1}=G_- - U`,

`q_{k+1}=G_+ - V`,

while `q_k=x(a_k r+c_{k-1})`.

Let

`P_k(r)=(a_k r+c_{k-1})^2-(a_{k-1}r+c_{k-2})(a_{k+1}r+c_k)`

be the universal-preserver quadratic from the preceding note. Direct substitution gives the exact identity

`q_k^2-q_{k-1}q_{k+1}`

`= x^2 P_k(r) + U G_+ + V G_- - UV`

`= x^2 P_k(r) + U q_{k+1} + V G_-`

`= x^2 P_k(r) + V q_{k-1} + U G_+`.

This is a full proof: the first equality is just expansion of `(G_--U)(G_+-V)`, and the last two use `q_{k+1}=G_+-V` and `q_{k-1}=G_--U` respectively.

Consequences:

1. `P_k(r)>=0` is sufficient because the curvature terms are nonnegative.
2. `P_k(r)<0` does **not** imply failure for the actual row; incoming strict log-concavity can rescue the step.
3. The correct induction target is therefore quantitative: compare the negative geometric-envelope term `-x^2 P_k(r)` against one of the explicit curvature reserves `U q_{k+1}+V G_-` or `V q_{k-1}+U G_+`.
4. The first exact actual failure of the stronger envelope route, `(n,k)=(4,3)`, has `x^2P=-16321/561600`, while the actual next-row normalized Chen margin is `613/2880`; the exact rescue is `8491/35100`.

This identity replaces the false goal “prove that the insertion kernel preserves every log-concave sequence.” A source-specific proof can instead exploit how the Plancherel row's two neighboring Chen curvatures control the insertion-profile defect.
