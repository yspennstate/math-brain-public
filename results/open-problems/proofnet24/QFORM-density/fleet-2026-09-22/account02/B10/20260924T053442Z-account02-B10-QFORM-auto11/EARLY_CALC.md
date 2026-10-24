# account02/B10 early calculation — a diffuse harmonic frame forces square-bank contamination

Programme: `QFORM-DENSITY-3EIG-20260922`. Full exact rank three and full QFORM remain open.

The first unpaid implication tested here is the conversion of the newest account03/B10 endpoint-stable certificate

`|d| ||r_U||_2^2 ||y_V||_2^2 > 1/32724`

for disjoint ORIGINAL banks `U,V` into either (i) a clean independent square bank, or (ii) an exact regression-clean reservoir. The calculation below shows that both conversions can fail simultaneously in one exact target-valid diffuse family.

Fix an odd integer `m>122`, angles `theta_j=2*pi*j/m`, and normalized leaf coefficient vectors

`r_j=sqrt(2/m) cos(theta_j)`,
`y_j=sqrt(2/m) sin(theta_j)`,
`z_j=sqrt(2/m) cos(2 theta_j)`.

Discrete Fourier orthogonality gives `r,y,z` pairwise orthonormal. For `0<rho<1/64`, `c=1-rho`, take physical spectral rows

`u_0=sqrt(c)e_1`,
`u_j=sqrt(rho) z_j e_1+r_j e_2+y_j e_3`, `1<=j<=m`,

and spectral core

`M_0=[[0,1,0],[1,0,0],[0,0,1]]`.

Then the columns of the physical frame are orthonormal, `A=R M_0 R^T` has exactly the nonzero spectrum `{1,-1,1}`, every leaf transverse leverage is `r_j^2+y_j^2=2/m<1/61`, and for independent cap-one ORIGINAL inputs

`Q=2(sqrt(c)H+sqrt(rho) Z)L+V^2`,
`Z=z.X_L`, `L=r.X_L`, `V=y.X_L`.

The key pointwise inequality is

`r_j^2+z_j^2 >= (4 sqrt(2)-5) y_j^2`.                         (E1)

Indeed with `x=cos^2(theta_j)`, after removing the common factor `2/m`, (E1) is

`x+(2x-1)^2-(4sqrt(2)-5)(1-x)
 =4(x-(1-sqrt(2)/2))^2 >=0`.

Hence every ORIGINAL subset `I` obeys

`||r_I||_2^2+||z_I||_2^2 >= (4sqrt(2)-5)||y_I||_2^2`.             (E2)

In particular, any square-heavy bank with `||y_I||_2^2>=1/162` necessarily carries at least

`(4sqrt(2)-5)/162 > 0.0040546`

of combined hub-partner/longitudinal contamination. Thus the newest partner certificate cannot in general be promoted to a nearly clean independent square bank by a selection argument whose contamination tends to zero.

The exact-regression alternative fails at the same time. On a subset `I`, exact regression of the leakage into the two transverse directions means

`z_j=gamma r_j+eta y_j` for every `j in I`,

i.e.

`cos(2 theta_j)=gamma cos(theta_j)+eta sin(theta_j)`.

Unless this degree-two trigonometric polynomial is identically zero (impossible), it has at most four zeros on one period. Hence every exact-regression-clean subset has `|I|<=4`. Its transverse Gram

`G_I=sum_(j in I) (r_j,y_j)^T(r_j,y_j)`

has trace `2|I|/m`, so by the two-by-two AM-GM bound

`det G_I <= (tr G_I/2)^2 <= 16/m^2`.                              (E3)

Thus the exact-regression reservoir degenerates as `m->infinity`, while every square-heavy bank retains a fixed fraction of same-bank contamination. This is a deterministic obstruction to two proof interfaces, not a counterexample to QFORM.

Next step: combine (E2)-(E3) with the completed account03/B10 hard-square theorem and the pinned ruled-side theorem at an actual density inequality, then record the precise three-direction receiver that remains unpaid.
