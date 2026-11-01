# P0282 idea before production validation — Plancherel content cancellation and an `n^(3/4)` defect window

Date: 2026-09-19 UTC  
Track: NM13-07  
Target: P0282, Chen fixed-size LIS log-concavity

This note is written before any new checker or row-92 production computation in this invocation. It records the mathematical route to test; it is not itself a certificate.

The current retained exact factorization for defect `j=n-k` is

`E_j(n)=ell_{n,n-j}=((n)_j^2/j!) A_j(n)`

with

`A_j(n)=E_{mu~Plancherel(j)}[R_mu(n,j)^2]`,

`R_mu(n,j)=prod_c (n-j-c+1)/(n-j-c+1+mu'_c)`.

The already proved `n^(2/3)` window uses only the shape-uniform first-order conservation `sum_c mu'_c=j` and pays an `O(j^2/n^2)` error in `log A_j`. The new route is to expand one order deeper and exploit conjugation symmetry of Plancherel measure.

For `h_c=mu'_c`, `a_c=j+c-1`, `d_c=n-a_c`, and content sum

`C(mu)=sum_{(r,c) in mu}(c-r)=n(mu')-n(mu)`,

the proposed pointwise second-order expansion is

`log R_mu(n,j)`

`= -j/n + (-j^2+j/2-C(mu))/n^2 + rho_mu`,

with a uniform explicit remainder `|rho_mu| <= 20 j^3/n^3` for `n>=4j`.

The crucial cancellation is

`C(mu')=-C(mu)` and `f^(mu')=f^mu`,

so under Plancherel measure `C` has a symmetric law and mean zero. Therefore the dangerous shape-dependent `O(j^2/n^2)` term does not survive linearly in the Plancherel average. Writing

`D_j(n)=-2j/n+(-2j^2+j)/n^2`,

the target bound is

`log A_j(n)=D_j(n)+epsilon_j(n)`,

`|epsilon_j(n)| <= 41 j^3/n^3`.

The planned proof controls the content moment-generating function only by symmetry and the deterministic bound `|C(mu)|<=j(j-1)/2`, using `cosh x <= exp(x^2/2)`. No external Plancherel CLT is needed.

In the exact Chen ratio

`Q_j(n)=E_j(n)^2/(E_{j-1}(n)E_{j+1}(n))`

`=((j+1)/j)((n-j+1)/(n-j))^2 A_j(n)^2/(A_{j-1}(n)A_{j+1}(n))`,

the deterministic second-order approximation has favorable discrete curvature

`2D_j-D_{j-1}-D_{j+1}=4/n^2`.

If the error bound above is valid for `j-1,j,j+1`, then

`log Q_j(n) > 1/(j+1) - 410 j^3/n^3`.

A clean sufficient condition would be

`n^3 >= 512 (j+1)^4`,

which implies strict Chen log-concavity and gives a boundary window

`j+1 <= n^(3/4)/512^(1/4)`.

This would improve the previously proved `Theta(n^(2/3))` window to `Theta(n^(3/4))` without changing the source statement or frozen metric.

Section-B methods actually being attempted in this route (all RECYCLED because all 30 numbered methods have already genuinely been used on P0282):

- **#12 FIND WHAT IS CONSERVED** — the second-order random term is the Young-diagram content, whose Plancherel mean cancels by conjugation.
- **#9 RANDOMIZE** — treat the residual partition under Plancherel measure and control its content MGF rather than using the worst shape linearly.
- **#30 DO ONE SCALE, ONE DIRECTION AT A TIME** — isolate the boundary defect regime and ask what error scale is needed to move from `n^(2/3)` to `n^(3/4)`.

Validation plan after this note: prove every remainder inequality on the page; exact-symbolic self-check the algebraic expansion and discrete curvature; then independently move the frozen row metric from 91 to 92 with the existing Gessel/CRT low-LIS seam plus the retained all-`n` defect theorem `j<=66`.
