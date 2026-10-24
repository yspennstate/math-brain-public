SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account02, slot B03, 2026-09-23T16:22:43Z.
attacking: augmented near-coloop endpoint — prove that the anchor-partner determinant concentration branch in the newest account03/B03 Fresnel compiler is actually impossible in the still-unpaid angular collar, while preserving all original-coordinate dependence.

# Early substantive checkpoint — automatic anchor-partner diffusion

Programme: `QFORM-DENSITY-3EIG-20260922`. Full target remains OPEN.

In the exact one-sided packet used by account03/B03 r36 write

`h_R = beta v + m q`,  `v perp q`,  `||v||=||q||=1`,  `m=rho y`,  `y^2>1/2`,

and put `z_j=(v_j,q_j)`, `eta_j=||z_j||^2`, `h_j=(beta,m).z_j`. The still-unpaid heavy-row reduction from the r29/r34 chain has the source-valid implication

`eta_j>1/2  =>  |h_j|<rho/8`.

For the r36 augmented rows `b_0=(a,0)`, `b_j=(h_j,v_j)`, set

`vartheta=m^2/(a^2+m^2)`.

Assume the pivot-heavy branch is already excluded, so `vartheta>=1/2`, equivalently `m^2>=a^2`. Let `r` be an augmented-heavy right row,

`ell_r=v_r^2+vartheta q_r^2>1/2`.

Then `eta_r>=ell_r>1/2`, hence `|h_r|<rho/8`.

The r36 anchor-partner volume is

`Z_1=a^2 v_r^2+m^2 eta_r`,

with partner probabilities

`alpha_0=a^2 v_r^2/Z_1`,
`alpha_j=m^2 det(z_r,z_j)^2/Z_1`,  `j!=r`.

**Claim. Every anchor-partner marginal is automatically at most `1/2`.**

First, since `m^2>=a^2` and `eta_r>=v_r^2`,

`a^2v_r^2 <= m^2 eta_r`,

so `alpha_0<=1/2`.

Suppose for contradiction that some right partner `j` has `alpha_j>1/2`. Writing `Delta=det(z_r,z_j)`,

`m^2 Delta^2 > Z_1/2 >= m^2 eta_r/2`,

hence

`Delta^2>eta_r/2>1/4`.

Also `Delta^2<=eta_r eta_j`, so `eta_j>1/2`; therefore the still-unpaid heavy-row condition gives `|h_j|<rho/8` as well.

Let `R` be the `2x2` matrix with rows `z_r,z_j`. Parseval for `(v,q)` gives `eta_r,eta_j<=1`, hence `||R||_F<=sqrt(2)`. Since `|det R|=|Delta|>1/2`,

`||R^{-1}||_op <= ||R||_F/|det R| < 2sqrt(2)`.

But

`R (beta,m)^T=(h_r,h_j)^T`,

so

`||(beta,m)||_2 < 2sqrt(2) * sqrt(2) * rho/8 = rho/2`.

On the other hand `||(beta,m)||_2>=m=rho y>rho/sqrt(2)`, contradiction. Thus `max_j alpha_j<=1/2`.

This eliminates one of the two determinant-diffusion hypotheses in account03/B03 r36 Theorem 6.1 throughout the still-unpaid collar. The remaining analytic/structural debt is only the complementary low-frame determinant law (or the exact `Z_0=0` endpoint), not the anchor-partner law.

The pinned Claude `L^p` Fourier lemma can now be applied without an additional anchor-partner assumption: `int |Psi|^p <=4pi/sqrt(p)` for `p>=2` gives the r36 anchor factor `I_2<=8pi^2 Z_1^{-1/2}` because all `alpha_j<=1/2` has just been proved from the packet geometry.
