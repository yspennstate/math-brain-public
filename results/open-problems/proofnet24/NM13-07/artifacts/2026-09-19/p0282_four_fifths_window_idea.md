# P0282 idea before archival validation — third-order Plancherel centering and an `n^(4/5)` defect window

Date: 2026-09-19 UTC  
Track: NM13-07  
Target: P0282, Chen fixed-size LIS log-concavity

This note is written before any **archival** checker/output or row-93 production certificate in this invocation. It records the mathematical route to test; it is not itself a certificate.

Retained notation: for defect `j=n-k`,

`E_j(n)=ell_{n,n-j}=((n)_j^2/j!) A_j(n)`,

`A_j(n)=E_{mu~Plancherel(j)}[R_mu(n,j)^2]`,

`R_mu(n,j)=prod_c (n-j-c+1)/(n-j-c+1+mu'_c)`.

The preceding run expanded `log R_mu` through `n^-2`. Its random second-order term is the content sum `C(mu)` and vanishes to first order after Plancherel averaging, yielding an `O(j^3/n^3)` error and a `Theta(n^(3/4))` defect window.

The new route expands one order deeper. Put `h_c=mu'_c`, `a_c=j+c-1`, `u=c-1`, and define

`C(mu)=sum_{(r,c) in mu}(c-r)`,

`S2(mu)=sum_{(r,c) in mu}(c-r)^2`.

A direct cellwise calculation predicts the exact third-order coefficient

`B3(mu)=-j^3+j^2-j/3 +(1-2j) C(mu)-S2(mu)`

in

`log R_mu=-j/n+(-j^2+j/2-C(mu))/n^2+B3(mu)/n^3+O(j^4/n^4)`.

The key extra centering identity should be

`E_Plancherel[S2(mu)]=j(j-1)/2`.

A short representation-theoretic proof is available through Jucys--Murphy elements: on a standard tableau, `sum_i X_i^2` has eigenvalue `S2(mu)`; in the regular representation the coefficient of the identity in `sum_i X_i^2` is `sum_i(i-1)=j(j-1)/2`.

After centering both `C` and `S2`, the random third-order perturbation has mean zero. A bounded-variable/Hoeffding estimate should make its logarithmic moment-generating contribution only `O(j^4/n^4)`, while a direct Taylor remainder through cubic order is also `O(j^4/n^4)` for `n>=8j`.

The target deterministic approximation is

`D3_j(n)=-2j/n+(-2j^2+j)/n^2+(-2j^3+j^2+j/3)/n^3`,

with

`log A_j(n)=D3_j(n)+epsilon_j(n)`, `|epsilon_j(n)| <= 60 j^4/n^4`.

Its discrete curvature is favorable:

`2D3_j-D3_{j-1}-D3_{j+1}=4/n^2+(12j-2)/n^3 > 0`.

Combining this with the exact Chen ratio and the retained all-`n` fixed-defect theorem `j<=66` should yield the clean global sufficient condition

`n^4 >= 256 (j+1)^5  =>  E_j(n)^2 > E_{j-1}(n)E_{j+1}(n)`.

For `j>=67`, that condition implies `n>=8(j+1)`, so the cubic Taylor bounds apply; for `j<=66`, the retained exact fixed-defect theorem already gives the source inequality. This would improve the rigorous growing-defect exponent from `3/4` to `4/5` without changing the source or frozen metric.

Section-B methods actually attempted here (all **RECYCLED**, because all 30 numbered methods have already genuinely been used on P0282, and this triple differs from the predecessor's #12/#9/#30):

- **#5 ADD A PARAMETER AND DIFFERENTIATE IN IT** — treat `1/n` as the expansion parameter and extract one more coefficient of the hook correction;
- **#14 FIND THE GROUP ACTING** — use symmetric-group/Jucys--Murphy structure to identify the exact Plancherel mean of squared contents;
- **#3 PROVE SOMETHING STRONGER** — target a stronger uniform `Theta(n^(4/5))` boundary theorem rather than merely moving one finite row.

Validation plan after this note: prove every cubic/remainder estimate on the page; exact-symbolically self-check the `B3` identity, Plancherel content moments, and discrete curvature; then independently move the frozen row metric from 92 to 93 with the Gessel/CRT low-LIS seam plus the retained `j<=66` theorem.
