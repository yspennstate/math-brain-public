# P01 T06 idea — same-law static/derivative compatibility below lambda=1

Target family: `P(nu=1)=1-p`, `P(nu=D)=p`, parent bias `lambda<1` (`beta=1/lambda`). Continue the exact Aidekon reduction from the 08:01 P01 report; do not count the historical Baum--Connes target as probability progress.

The previous run sharpened the static degree-tilt ratio to

`c_D/c_1 <= (1+lambda)/(D+lambda)`

under `D(1-lambda)>=1+lambda`, but the derivative score still used only `a_1-a_D<=1/(1-lambda)`. The present idea is to force a positive lower bound on `a_D` from the *same offspring law*.

Let `c=1-lambda`, let `B` be the branch escape probability, and let `R=-B'/B`. The inherited minimum-one estimate is `0<=R<=1/c`. If the branch root itself has `D` children, write `T=sum_{j=1}^D B_j` and `M=lambda+D c`. The escape recursion gives

`B=T/(lambda+T) >= D c/M`

and

`R=(1+lambda sum_j B_j R_j/T)/(lambda+T) <= 1/[c M]`.

Therefore the nonnegative compatibility variable

`Z:=B(1-cR)=B+cB'`

satisfies, on the event `{nu=D}`,

`Z >= D c(M-1)/M^2`.

Hence for the two-point law

`E Z >= p D c(M-1)/M^2`.

For current degree `k=D`, with `S=sum_{i=0}^D B_i`, `U=sum B_i R_i`,

`w_D=S/((D+1)(S-c))`,
`-c_D'=E[(S-cU)/((D+1)(S-c)^2)]`.

Since `S-cU=sum Z_i`, `S-c<=D+lambda`, and `c_D<=1/D`,

`a_D:=-c_D'/c_D >= p D^2 c(M-1)/(M^2(D+lambda)^2)`.

Because `M-1=(D-1)c`, define

`J_D(lambda)=D^2(D-1)(1-lambda)^2/[(D-(D-1)lambda)^2(D+lambda)^2]`.

Then

`a_1-a_D <= 1/(1-lambda)-p J_D(lambda)`.

The exact two-state derivative identity remains

`r'= (D-1) theta(1-theta)(a_1-a_D)`,
`ell'=2(lambda r'-r)/(r+lambda)^2`,
`r=1+(D-1)theta`.

Combining the previous static ratio with this new lower score should move the exact `{1,12}`, `p<=1/2` frontier past 0.668409..., and also repair the previous method failures at `{1,47}`, `p<=2/5`, `lambda=2/3` and `{1,222}`, `p<=19/50`, `lambda=2/3`.

Planned exact targets after proving a uniform lower bound for `lambda J_D(lambda)` on `[1/2,L]`:

1. `{1,12}`, `p<=1/2`, seek `L>=0.67` with an explicit `-ell'` margin.
2. fixed `L=2/3`, seek the largest immediate support upgrades above `D=46` for `p<=2/5` and above `D=221` for `p<=19/50`.
3. record exact first failures of this new sufficient certificate; they are method boundaries only.
