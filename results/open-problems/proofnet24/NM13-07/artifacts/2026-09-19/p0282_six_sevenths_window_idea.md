# P0282 idea before production validation — fifth-order Plancherel centering plus an analytic Cauchy remainder

Date: 2026-09-19 UTC

Target continuity: Chen fixed-size LIS log-concavity, canonical claim P0282, frozen metric currently `N_exact=94`. This note records the route before any new production checker is written.

All thirty Section-B methods have already been genuinely used on P0282, so this run must recycle a different triple from the predecessor. Actual routes selected:

- **#5 ADD A PARAMETER AND DIFFERENTIATE IN IT (RECYCLED):** put `t=1/n` and treat `G_j(t)=log E_Plancherel[R_mu(t)^2]` as an analytic function. Compute its fifth Taylor coefficient exactly and use Cauchy, rather than another term-by-term real-variable remainder estimate, for the entire order-six tail.
- **#21 ASK WHO ELSE HAS THIS SHAPE (RECYCLED):** identify the new Plancherel moment `E[S_4]` with the normalized regular-representation trace of the central Jucys--Murphy power sum `sum_i X_i^4`; reduce it to an exact count of length-four star-transposition words.
- **#4 PROVE SOMETHING WEAKER, COMPLETELY (RECYCLED):** aim only for a rigorous `Theta(n^(6/7))` long-LIS boundary window, not the full central-regime conjecture.

Candidate mechanism. Write `j=n-k`, `E_j(n)=ell_{n,n-j}`, and retain

`E_j(n)=((n)_j^2/j!) A_j(n)`,  `A_j(n)=E_mu[R_mu(n,j)^2]`.

For a column of height `h` and `a=j+c-1`, the coefficient of `n^-5` in `log R_mu` is

`-h a^4 + 2 h^2 a^3 - 2 h^3 a^2 + h^4 a - h^5/5`.

After converting column-height powers by forward differences, the per-cell contribution with content `x` should collapse to

`-j^4+2j^3-2j^2+j-1/5 + (-4j^3+6j^2-4j+1)x + (-6j^2+6j-2)x^2 + (-4j+2)x^3 - x^4`.

Thus only `C,S2,S3,S4` enter. Conjugation kills `E[C]` and `E[S3]`; the new quantity is `E[S4]`. For fixed `i`, the identity coefficient of `X_i^4`, where `X_i=sum_{a<i}(a i)`, is predicted to be `2(i-1)^2-(i-1)`, because a four-word of star transpositions multiplies to identity exactly in the paired cases. Summing over `i` predicts

`E[S4]=j(j-1)(4j-5)/6`.

The order-five coefficient of `log A_j` must also include the covariance between the order-two and order-three random terms. Since `B2=d2-C` and `B3=d3+(1-2j)C-S2`, conjugation gives `Cov(C,S2)=0`, so the covariance is `(2j-1) binom(j,2)`. The predicted exact coefficient is

`D5(j)=-2j^5-2j^4+(32/3)j^3-9j^2+(29/15)j`.

Its discrete curvature is predicted to be

`2D5(j)-D5(j-1)-D5(j+1)=40j^3+24j^2-44j+22`,

strictly positive for `j>=1`.

For a rigorous all-tail bound, define complex `t=1/n` and

`F_mu(t)=2 sum_c [log(1-a_c t)-log(1-(a_c-h_c)t)]`.

On `|t|<=1/(8j)`, use the integral form of the log difference and `sum h_c=j` to get `|F_mu(t)|<=1/3`. Hence `A_j(t)=E[e^{F_mu(t)}]` stays within `e^(1/3)-1<2/5` of 1, so `G_j(t)=log A_j(t)` is analytic there and `|G_j(t)|<1`. Cauchy then gives, for real `0<t<=1/(16j)`,

`|G_j(t)-sum_{m=1}^5 D_m(j)t^m| <= 2(8jt)^6 = 2^19 j^6/n^6`.

Applying the same bound to `j-1,j,j+1`, the Chen log-ratio error is at most `2^21 (j+1)^6/n^6`. Since `log((j+1)/j)>=1/(j+1)` and all deterministic discrete-curvature terms through order five are nonnegative, the clean sufficient condition

`n^6 >= 2^24 (j+1)^7`

should imply strict Chen log-concavity. This would give a `Theta(n^(6/7))` boundary window. Production validation should try to falsify every predicted moment/Taylor identity with exact partition enumeration before this is promoted to a theorem.
