# account02/B18 early calculation — stable-rank / fifth-volume funnel

Programme: `QFORM-DENSITY-3EIG-20260922`  
Run: `account02-B18-20260924T020253Z-r11`  
Status: substantive checkpoint; full QFORM remains OPEN.

The newest designated-partner receiver (account03/B18, `0a7f288f8c823b2912d7a76a9a7a8029d5bae705`) pays a zero-self original-coordinate cross block `B` whenever

`r(B)=floor(||B||_HS^2/||B||_op^2) >= 2`,

with `||p_Q||_infinity <= sqrt(2) C_RV ||B||_op^{-1}`.  The primary Rudelson--Vershynin source was checked at Theorem 1.2 and Corollary 8.6; no moments, support, log-concavity, iid, centering, symmetry, or rotated-coordinate independence are used.

The pinned `e5f71d79...` Fourier report gives, for every original-coordinate cut and with arbitrary diagonal blocks, the fifth-volume bound

`||p_Q||_infinity <= 5 sqrt(2e) e_5(B^T B)^(-1/10)`.

The following deterministic inequality connects failure of that receiver to a low-rank carrier.  Write the singular values of `B` as `sigma_1>=sigma_2>=...>=0`, set `x_j=sigma_j^2`, `Z_5=e_5(x)`, and

`R_5=sum_{j>=5} x_j`.

Then

`Z_5 >= x_1 (R_5/4)^4`,

hence

`R_5 <= 4 (Z_5/x_1)^(1/4)`.

Proof of the only nonstandard step: for any decreasing nonnegative sequence `y_1>=y_2>=...` and `R=sum_{j>=4} y_j`,

`e_4(y) >= (R/4)^4`.

If `y_4>=R/4`, the single term `y_1y_2y_3y_4` suffices.  Otherwise the normalized tail `(y_4,y_5,...)/R` has total mass one and every atom is at most `1/4`.  The vector `(1/4,1/4,1/4,1/4,0,...)` majorizes every such vector, while `e_4` is Schur-concave (for a two-coordinate transfer at fixed sum, only the product term changes and decreases when the pair is made more unequal).  Thus the tail `e_4` is at least `4^-4`.  Apply this with `y=(x_2,x_3,...)` and use `Z_5=x_1e_4(y)+e_5(y)`.

Consequently, if

`Z_5 < 2^-24 sigma_1^10`,

then the rank-four truncated SVD `B_4` satisfies

`||B-B_4||_HS^2=R_5 < sigma_1^2/16`,

so

`||B-B_4||_HS < sigma_1/4` and `||B-B_4||_op < sigma_1/4`.

A genuine owner-target family shows why the pinned fifth-volume theorem adds scope beyond the stable-rank receiver.  Let

`B=diag(1,1/4,1/4,1/4,1/4)`

and

`A = [[0,B,0],[B,0,0],[0,0,1]]`.

Its spectrum is `{+1,-1,+1,+1/4 (four copies),-1/4 (four copies)}`, so it has exactly three eigenvalues of modulus at least one.  Yet

`floor(||B||_HS^2/||B||_op^2)=floor(1+4/16)=1`,

so the newest stable-rank receiver is unavailable.  On the other hand

`Z_5=e_5(B^T B)=(1/4)^8=2^-16`,

and the pinned `D_5` theorem gives the actual whole-line target inequality

`||p_{X^T A X}||_infinity <= 5 sqrt(2e) 2^(8/5) = 35.3411141011...`.

Thus a low stable-rank cross block need not be an obstruction: fifth-volume aggregation pays a genuine stable-rank-one target family.  The remaining cross obstruction must have both `r(B)=1` and small normalized fifth volume, which forces the quantitative rank-four carrier above; the residual must be retained rather than deleted.
