# fleet01/B07 r29 early calculation — one-hub Plucker conditioning

Run: `fleet01-B07-20260923T170819Z-r29`.

Let `K` be a physical cross block with complete squared-`2x2`-minor mass `Omega>0`, determinant law `W`, and let `W0=mu x nu` be the product Plucker law of the best rank-two truncation. Assume `dTV(W,W0)<=eps`.

For a two-dimensional left singular plane with orthonormal frame `U`, the Plucker pair law is

`mu({i,j})=det U[{i,j},:]^2`,

and its exact coordinate inclusion marginal is

`sum_(j!=i) mu({i,j})=ell_i:=||U[i,:]||_2^2`.

If a physical coordinate `h` is the unique leverage hub above `3/4`, then conditional on `h` being in the Plucker pair,

`mu_h(i)=mu({h,i})/ell_h <= ell_i <=3/4`,

because `det(U_h,U_i)^2<=ell_h ell_i`.

Take `eps=1/64`. If each singular plane has at least one `>3/4` hub and one side has a unique such hub `h`, choose any `>3/4` hub `k` on the other side and let `A={h in R,k in C}`. Then

`W0(A)=ell_h m_k>9/16`,
`W(A)>=9/16-1/64=35/64`.

For conditional laws,

`dTV(W(.|A),W0(.|A)) <= 2 eps/W(A) <=2/35`.

Therefore the residual inclusion marginals on the unique-hub side are at most

`eta=3/4+2/35=113/140<1`.

The actual anchored E2 mass is `G=Omega W(A)>=35 Omega/64`. Applying the already proved anchored E2-to-E1 shadow and mixed order-2/order-1 half-Riesz theorem with

`w=eta=113/140`, `q=2 eta=113/70`, `r=1+eta=253/140`

gives

`H_(1/2)(R) <= C G^(-35/253) R_h^(27/506)`

with `C=36.2238134022`; since `R_h<=||K||_F=sqrt(E)`, this is

`H_(1/2)(R) <=39.3781 Omega^(-35/253) E^(27/1012)`.

If one singular plane has no `>3/4` hub, the actual determinant-law marginals on that side are at most `3/4+1/64=49/64`; the existing E2 half-Riesz theorem at `q=49/32` gives

`H_(1/2)(R) <=17.8863 Omega^(-1/8)`.

If both singular planes have at least two `>3/4` hubs, Bonferroni gives a fixed Plucker pair of mass `>1/2` on each side, so one literal physical `2x2` minor has

`det^2 >= Omega(1/4-1/64)=15 Omega/64`.

Thus `dTV(W,W0)<=1/64` yields an exhaustive `MACRO-MINOR OR HALF-RIESZ` dichotomy before reciprocal pivot inversion. Full proof and partner application will be written in `REPORT.md`.
