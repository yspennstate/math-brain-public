# Addendum — sharp universal block-row nonconformality ceiling

This strengthens the numerical constant in `REPORT.md` and leaves its scope/status unchanged.

For a `2 x 2` block `B` of the orthogonal exterior-square matrix `O=Lambda^2 U`, let its singular values be `s_1,s_2`. Because `B` is a compression of an orthogonal matrix,

`0 <= s_1,s_2 <= 1`.

With

`R=(s_1^2+s_2^2)/2`, `D^2=s_1^2 s_2^2`,

we have exactly

`R^2-D^2 = (s_1^2-s_2^2)^2/4`.

Since `x=s_1^2,y=s_2^2` lie in `[0,1]`,

`(x-y)^2 <= x+y`.

For one exterior block row `alpha`, orthogonality gives

`sum_beta (s_{1,alpha beta}^2+s_{2,alpha beta}^2)=2`.

Therefore

`boxed( E_alpha = sum_beta(R_{alpha beta}^2-D_{alpha beta}^2) <= 1/2 )`.   (A1)

This constant is sharp for the abstract block-row constraints: two complementary rank-one projections and a zero third block give equality.

Hence on the generic mixed-Schur edge `e={alpha,gamma}`, the exact B07 lower bound and the account02/B07 roof identity yield

`1 >= E_alpha+E_gamma >= 4Q h_e
   = 16 h_e (gamma+r_tau)(gamma+r_{tau^c})`,

where

`h_e=lambda_alpha lambda_gamma/(lambda_alpha+lambda_gamma)`.

Thus the sharpened target-level necessary condition is

`boxed( 16 h_e (gamma+r_tau)(gamma+r_{tau^c}) <= 1 )`,          (A2)

and in particular

`boxed( gamma <= 1/(4 sqrt(h_e))
              = sqrt((lambda_alpha+lambda_gamma)/(16 lambda_alpha lambda_gamma)) )`.   (A3)

This improves the ceiling in the main report by a factor `sqrt(2)` in the positive-gap bound. It is still only a necessary condition on the generic mixed-Schur branch, not a proof of MOC4.
