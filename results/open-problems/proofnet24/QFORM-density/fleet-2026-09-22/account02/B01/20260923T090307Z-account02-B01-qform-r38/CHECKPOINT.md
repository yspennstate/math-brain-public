# account02/B01 r38 checkpoint — rank-two bicore plus a source-disjoint hyperbolic receiver

Programme: `QFORM-DENSITY-3EIG-20260922`. Full conjecture remains OPEN.


Substantive checkpoint. Let a conditional form split over disjoint original-coordinate banks as

`Q_w = R_w(X_I,X_J) + H_w(X_{D1},X_{D2}) + c_w`,

where `A[I,J]=K` has rank two, `Delta=sigma_1(K)sigma_2(K)>0`, the self phases inside `I,J` are arbitrary, and

`H_w = 2 b U V + alpha_w U + beta_w V`, `U=<u,X_{D1}>`, `V=<v,X_{D2}>`,

with `D1,D2` disjoint and the displayed scalar form exact after conditioning. The rank-two projected-Plancherel envelope gives

`|phi_R(t)| <= min(1, 2*pi*Delta^(-1/2)/|t|)`.

A sign-resolved logarithmic-coordinate calculation sharpens the known product-density estimate: if independent `U,V` have density caps `N_U,N_V`, then

`||p_(UV)||_2 <= 2*sqrt(2)*sqrt(N_U*N_V)`,

hence after completing the affine rectangle

`||p_H||_2 <= 2*sqrt(N_U*N_V/|b|)`.

Therefore for every `T>0`, Cauchy-Schwarz on `|t|>T` gives

`||phi_Q||_1 <= 2T + 8*pi*sqrt(pi)*Delta^(-1/2)*sqrt(N_U*N_V/|b|)*T^(-1/2)`.

Optimizing yields the candidate supporting theorem

`||p_Q||_infinity <= 3*2^(2/3)*Delta^(-1/3)*(N_U*N_V/|b|)^(1/3)`.

Using the source-valid one-dimensional product-projection caps `N_U<=sqrt(2)/||u||_2`, `N_V<=sqrt(2)/||v||_2`, and `Gamma=|b| ||u||_2 ||v||_2`, this becomes

`||p_Q||_infinity <= 6 (Delta*Gamma)^(-1/3)`.

The remaining work this run is to audit constants and provenance, apply the newest account03/B01 definite-kernel receiver to a compatible comparison family, and test a strict-N3 diffuse rank-two-plus-hyperbolic family against the required Theorem D before publication.
